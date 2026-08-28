
# LA-Q-ICP-MS Technique-Aligned Procedure Profile (laQicpmsTAPP) (Schema)

`ogch.techniqueProfile.geochemProfile.LA-Q-ICPMS.tapp` *v0.1*

Laser-ablation quadrupole ICP-MS extension of the base TAPP definition, generated from TAPPS20260813/Current TAPPs/LA-Q-ICP-MS_TAPP_v15.csv via the path-driven pipeline (bootstrap_schemapaths.py + build_pathdriven.py).

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### laQicpmsTAPP example Nakanishi2022
laQicpmsTAPP instance derived from Nakanishi et al. 2022 (GCA 319) CR chondrite metal (HSE) Spot analysis fs-LA-Q-ICP-MS Tokyo Institute of Technology.
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
  "@id": "ex:laQicpmsTAPP-Nakanishi2022",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Nakanishi et al. (2022) CR Chondrite Metal HSE fs-LA-ICP-MS Spot v1",
  "schema:description": "fs laser (260 nm Ti:sapphire) essential for HSE measurement in metal (reduces elemental fractionation and matrix effects); IVB iron meteorite standards (Warburton Range + Tawallah Valley) as matrix-matched standards for iron meteorite metal",
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
            "CR chondrite metal grains (interior, margin, and isolated types)"
          ]
        },
        {
          "@id": "ada:parameter/laQicpmsTAPP/sampleFormAnalyticalSubstrateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleFormAnalyticalSubstrateDefault",
          "schema:name": "Sample Form / Analytical Substrate",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "In situ — polished epoxy thick section (petropoxy 154 resin, 0.5 µm diamond finish)"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Thick sections in petropoxy 154 resin, polished to 0.5 µm diamond paste, C-coated for EPMA then surface polished before LA",
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
            "@id": "ada:parameter/laQicpmsTAPP/spikeOutlierFilteringApproachDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "spikeOutlierFilteringApproachDefault",
            "schema:name": "Spike / Outlier Filtering Approach",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Monitoring of Mg, Si, P, S to check for micro-inclusions (sulfides); analyses with elevated inclusion signals excluded entirely"
          },
          {
            "@id": "ada:parameter/laQicpmsTAPP/normalizationStandardsBasedCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "normalizationStandardsBasedCorrectionDefault",
            "schema:name": "Normalization / Standards-Based Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "No post-acquisition normalization; calibration curve method using IVB standards provides direct quantification"
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
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Single-collector quadrupole (Q-ICP-MS)",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Thermo Scientific X-series 2 (Q-ICP-MS)",
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
              "@id": "ada:parameter/laQicpmsTAPP/interfaceConeConfiguration",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/laQicpmsTAPP/interfaceConeConfiguration"
                }
              ],
              "schema:name": "Interface Cone Configuration",
              "schema:value": "Ni micro-skimmer cone Xs; Ni sampler cone"
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
            "ICP Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/laQicpmsTAPP/coolantGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantGasFlowRateDefault",
              "schema:name": "Coolant (Plasma) Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 12,
              "schema:description": "Cool gas: 12–13 l min⁻¹ Ar; Auxiliary: 0.6–1.2 l min⁻¹"
            },
            {
              "@id": "ada:parameter/laQicpmsTAPP/rfPowerDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "rfPowerDefault",
              "schema:name": "RF Power",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 1400,
              "schema:description": "1400 W"
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
          "@id": "ada:parameter/laQicpmsTAPP/massResolutionSetting",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSetting",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Unit resolution (quadrupole fixed)"
        }
      ],
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
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/module/LaserAblation/laserPulseDuration",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "laserPulseDuration",
          "schema:name": "Laser Pulse Duration",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:value": "~220 fs (Ti:sapphire IFRIT system)"
        }
      ],
      "schema:model": {
        "schema:name": "Cyber Laser IFRIT (Ti:sapphire fs UV laser, 260 nm)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "260 nm Ti:sapphire femtosecond UV; pulse duration ~220 fs (IFRIT system)",
      "ada:laserSpotGeometryDefault": "30 µm circular",
      "ada:laserFluenceDefault": "12 J cm⁻²",
      "ada:laserRepetitionRateDefault": "20 Hz",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/Laser-Ablation-System",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:carrierGasFlowRateDefault": "Carrier gas flow: 0.6 L/min; species not named (carrier gas identity not stated in Table 1 or text)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsTAPP/makeUpGasAndFlowRateDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "makeUpGasAndFlowRateDefault",
      "schema:name": "Make-up Gas and Flow Rate",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 0.9,
      "schema:description": "Ar make-up: 0.9–1.2 l min⁻¹; Ar auxiliary: 0.6–1.2 l min⁻¹"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign"
        }
      ],
      "schema:name": "Multi-Run Sequential Analysis Design",
      "schema:value": "Single spot per location (30 µm circular)"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/uncertaintyPropagationMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "uncertaintyPropagationMethodDefault",
      "schema:name": "Uncertainty Propagation Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "2SE of individual spot measurements reported"
    }
  ],
  "ada:analysisSequenceDefault": "IVB meteorite standards (Warburton Range external + Tawallah Valley secondary) measured alongside unknowns; exact bracketing not described",
  "ada:internalStandardApproach": "Single element externally measured by EPMA: ⁶¹Ni concentration from EPMA at exact analysis location used as IS",
  "ada:internalStandardElement": "⁶¹Ni; concentration from EPMA measured at exact analysis spot location",
  "ada:elementalFractionationCorrection": [
    "External calibration using calibration curve method with IVB iron meteorite standards; ⁶¹Ni as IS from EPMA corrects for ablation yield differences between sample and standard"
  ],
  "ada:signalIntegrationIntervalMethod": "Time-resolved signals monitored; analyses with elevated Mg, Si, P, S (inclusion indicators) excluded; stable signal intervals used for integration",
  "ada:blankBackgroundCorrectionMethod": "Gas blank measured before each spot; background period during single spot transient (rapid intensity rise and decay) used for background correction",
  "ada:primaryStandardNameDefault": "Warburton Range (IVB iron meteorite; Walker et al. 2008) — used as primary external standard and for calibration curve method",
  "ada:secondaryReferenceMaterialDefault": [
    "Tawallah Valley (IVB iron meteorite; Walker et al. 2008) — measured as secondary/check standard alongside unknowns"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "fs-LA-Q-ICP-MS"
    }
  ],
  "schema:creator": {
    "schema:name": "Nakanishi, Yokoyama, Okabayashi, Iwamori, Hirata",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Dept. of Earth and Planetary Sciences, Tokyo Institute of Technology, Japan"
  },
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "JSPS KAKENHI; Tokyo Institute of Technology"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Nakanishi et al. (2022) GCA 319, 254; Walker et al. (2008) for IVB standards"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "EPMA (electron probe microanalysis)",
        "schema:description": "EPMA used to measure Ni concentration at the exact LA-ICP-MS analysis spot location, required for internal standardization of HSE data [Section 2.3]"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:ablationSamplingMode": [
    "Spot (stationary)"
  ],
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "⁵⁹Co",
      "¹⁰¹Ru",
      "¹⁰³Rh",
      "¹⁰⁵Pd",
      "¹⁸⁵Re",
      "¹⁸⁹Os",
      "¹⁹³Ir",
      "¹⁹⁵Pt",
      "¹⁹⁷Au (9 HSE isotopes)",
      "²⁴Mg",
      "²⁹Si",
      "³¹P",
      "³³S monitored for inclusion detection",
      "⁶¹Ni as internal standard"
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
        "@id": "ada:analyteColumn/laQicpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "boolean",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "uri"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
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
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ablationSpotDurationDefault": -9999,
  "ada:backgroundCountTimeDefault": -9999,
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
  "ada:signalCollectionMode": "missing",
  "ada:targetSelectionCriteriaDefault": "missing",
  "ada:totalIntegrationTimePerOutputDataPointDefault": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:laQicpmsTAPP-Nakanishi2022",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Nakanishi et al. (2022) CR Chondrite Metal HSE fs-LA-ICP-MS Spot v1",
  "schema:description": "fs laser (260 nm Ti:sapphire) essential for HSE measurement in metal (reduces elemental fractionation and matrix effects); IVB iron meteorite standards (Warburton Range + Tawallah Valley) as matrix-matched standards for iron meteorite metal",
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
            "CR chondrite metal grains (interior, margin, and isolated types)"
          ]
        },
        {
          "@id": "ada:parameter/laQicpmsTAPP/sampleFormAnalyticalSubstrateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleFormAnalyticalSubstrateDefault",
          "schema:name": "Sample Form / Analytical Substrate",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "In situ \u2014 polished epoxy thick section (petropoxy 154 resin, 0.5 \u00b5m diamond finish)"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Thick sections in petropoxy 154 resin, polished to 0.5 \u00b5m diamond paste, C-coated for EPMA then surface polished before LA",
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
            "@id": "ada:parameter/laQicpmsTAPP/spikeOutlierFilteringApproachDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "spikeOutlierFilteringApproachDefault",
            "schema:name": "Spike / Outlier Filtering Approach",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Monitoring of Mg, Si, P, S to check for micro-inclusions (sulfides); analyses with elevated inclusion signals excluded entirely"
          },
          {
            "@id": "ada:parameter/laQicpmsTAPP/normalizationStandardsBasedCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "normalizationStandardsBasedCorrectionDefault",
            "schema:name": "Normalization / Standards-Based Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "No post-acquisition normalization; calibration curve method using IVB standards provides direct quantification"
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
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Single-collector quadrupole (Q-ICP-MS)",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Thermo Scientific X-series 2 (Q-ICP-MS)",
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
              "@id": "ada:parameter/laQicpmsTAPP/interfaceConeConfiguration",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/laQicpmsTAPP/interfaceConeConfiguration"
                }
              ],
              "schema:name": "Interface Cone Configuration",
              "schema:value": "Ni micro-skimmer cone Xs; Ni sampler cone"
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
            "ICP Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/laQicpmsTAPP/coolantGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantGasFlowRateDefault",
              "schema:name": "Coolant (Plasma) Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 12,
              "schema:description": "Cool gas: 12\u201313 l min\u207b\u00b9 Ar; Auxiliary: 0.6\u20131.2 l min\u207b\u00b9"
            },
            {
              "@id": "ada:parameter/laQicpmsTAPP/rfPowerDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "rfPowerDefault",
              "schema:name": "RF Power",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 1400,
              "schema:description": "1400 W"
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
          "@id": "ada:parameter/laQicpmsTAPP/massResolutionSetting",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSetting",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Unit resolution (quadrupole fixed)"
        }
      ],
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
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/module/LaserAblation/laserPulseDuration",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "laserPulseDuration",
          "schema:name": "Laser Pulse Duration",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:value": "~220 fs (Ti:sapphire IFRIT system)"
        }
      ],
      "schema:model": {
        "schema:name": "Cyber Laser IFRIT (Ti:sapphire fs UV laser, 260 nm)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "260 nm Ti:sapphire femtosecond UV; pulse duration ~220 fs (IFRIT system)",
      "ada:laserSpotGeometryDefault": "30 \u00b5m circular",
      "ada:laserFluenceDefault": "12 J cm\u207b\u00b2",
      "ada:laserRepetitionRateDefault": "20 Hz",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/Laser-Ablation-System",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:carrierGasFlowRateDefault": "Carrier gas flow: 0.6 L/min; species not named (carrier gas identity not stated in Table 1 or text)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsTAPP/makeUpGasAndFlowRateDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "makeUpGasAndFlowRateDefault",
      "schema:name": "Make-up Gas and Flow Rate",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 0.9,
      "schema:description": "Ar make-up: 0.9\u20131.2 l min\u207b\u00b9; Ar auxiliary: 0.6\u20131.2 l min\u207b\u00b9"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign"
        }
      ],
      "schema:name": "Multi-Run Sequential Analysis Design",
      "schema:value": "Single spot per location (30 \u00b5m circular)"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/uncertaintyPropagationMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "uncertaintyPropagationMethodDefault",
      "schema:name": "Uncertainty Propagation Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "2SE of individual spot measurements reported"
    }
  ],
  "ada:analysisSequenceDefault": "IVB meteorite standards (Warburton Range external + Tawallah Valley secondary) measured alongside unknowns; exact bracketing not described",
  "ada:internalStandardApproach": "Single element externally measured by EPMA: \u2076\u00b9Ni concentration from EPMA at exact analysis location used as IS",
  "ada:internalStandardElement": "\u2076\u00b9Ni; concentration from EPMA measured at exact analysis spot location",
  "ada:elementalFractionationCorrection": [
    "External calibration using calibration curve method with IVB iron meteorite standards; \u2076\u00b9Ni as IS from EPMA corrects for ablation yield differences between sample and standard"
  ],
  "ada:signalIntegrationIntervalMethod": "Time-resolved signals monitored; analyses with elevated Mg, Si, P, S (inclusion indicators) excluded; stable signal intervals used for integration",
  "ada:blankBackgroundCorrectionMethod": "Gas blank measured before each spot; background period during single spot transient (rapid intensity rise and decay) used for background correction",
  "ada:primaryStandardNameDefault": "Warburton Range (IVB iron meteorite; Walker et al. 2008) \u2014 used as primary external standard and for calibration curve method",
  "ada:secondaryReferenceMaterialDefault": [
    "Tawallah Valley (IVB iron meteorite; Walker et al. 2008) \u2014 measured as secondary/check standard alongside unknowns"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "fs-LA-Q-ICP-MS"
    }
  ],
  "schema:creator": {
    "schema:name": "Nakanishi, Yokoyama, Okabayashi, Iwamori, Hirata",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Dept. of Earth and Planetary Sciences, Tokyo Institute of Technology, Japan"
  },
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "JSPS KAKENHI; Tokyo Institute of Technology"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Nakanishi et al. (2022) GCA 319, 254; Walker et al. (2008) for IVB standards"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "EPMA (electron probe microanalysis)",
        "schema:description": "EPMA used to measure Ni concentration at the exact LA-ICP-MS analysis spot location, required for internal standardization of HSE data [Section 2.3]"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:ablationSamplingMode": [
    "Spot (stationary)"
  ],
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "\u2075\u2079Co",
      "\u00b9\u2070\u00b9Ru",
      "\u00b9\u2070\u00b3Rh",
      "\u00b9\u2070\u2075Pd",
      "\u00b9\u2078\u2075Re",
      "\u00b9\u2078\u2079Os",
      "\u00b9\u2079\u00b3Ir",
      "\u00b9\u2079\u2075Pt",
      "\u00b9\u2079\u2077Au (9 HSE isotopes)",
      "\u00b2\u2074Mg",
      "\u00b2\u2079Si",
      "\u00b3\u00b9P",
      "\u00b3\u00b3S monitored for inclusion detection",
      "\u2076\u00b9Ni as internal standard"
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
        "@id": "ada:analyteColumn/laQicpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "boolean",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "uri"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
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
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ablationSpotDurationDefault": -9999,
  "ada:backgroundCountTimeDefault": -9999,
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
  "ada:signalCollectionMode": "missing",
  "ada:targetSelectionCriteriaDefault": "missing",
  "ada:totalIntegrationTimePerOutputDataPointDefault": -9999,
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

ex:laQicpmsTAPP-Nakanishi2022 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Thick sections in petropoxy 154 resin, polished to 0.5 µm diamond paste, C-coated for EPMA then surface polished before LA" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/normalizationStandardsBasedCorrectionDefault>,
                        <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/spikeOutlierFilteringApproachDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/makeUpGasAndFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign>,
        <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/uncertaintyPropagationMethodDefault> ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Nakanishi, Yokoyama, Okabayashi, Iwamori, Hirata" ] ;
    schema1:datePublished "missing" ;
    schema1:description "fs laser (260 nm Ti:sapphire) essential for HSE measurement in metal (reduces elemental fractionation and matrix effects); IVB iron meteorite standards (Warburton Range + Tawallah Valley) as matrix-matched standards for iron meteorite metal" ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "JSPS KAKENHI; Tokyo Institute of Technology" ] ;
    schema1:instrument <https://example.org/instrument/ICPMS>,
        <https://example.org/instrument/Laser-Ablation-System> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Dept. of Earth and Planetary Sciences, Tokyo Institute of Technology, Japan" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "fs-LA-Q-ICP-MS" ] ;
    schema1:name "Nakanishi et al. (2022) CR Chondrite Metal HSE fs-LA-ICP-MS Spot v1" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "CR chondrite metal grains (interior, margin, and isolated types)" ],
                <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/sampleFormAnalyticalSubstrateDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Nakanishi et al. (2022) GCA 319, 254; Walker et al. (2008) for IVB standards" ] ;
            schema1:url "https://ada.astromat.org/missing" ],
        [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "EPMA used to measure Ni concentration at the exact LA-ICP-MS analysis spot location, required for internal standardization of HSE data [Section 2.3]" ;
                    schema1:name "EPMA (electron probe microanalysis)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:ablationPitDepthRateDefault "missing" ;
    ada:ablationSamplingMode "Spot (stationary)" ;
    ada:ablationSpotDurationDefault -9999 ;
    ada:analysisSequenceDefault "IVB meteorite standards (Warburton Range external + Tawallah Valley secondary) measured alongside unknowns; exact bracketing not described" ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/isobaricInterferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/limitOfQuantificationMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/monitoredMasses>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ;
            ada:defaultAnalytes "²⁴Mg",
                "²⁹Si",
                "³³S monitored for inclusion detection",
                "³¹P",
                "¹⁰³Rh",
                "¹⁰¹Ru",
                "¹⁰⁵Pd",
                "¹⁸⁵Re",
                "¹⁸⁹Os",
                "¹⁹³Ir",
                "¹⁹⁵Pt",
                "¹⁹⁷Au (9 HSE isotopes)",
                "⁵⁹Co",
                "⁶¹Ni as internal standard" ] ;
    ada:backgroundCountTimeDefault -9999 ;
    ada:blankBackgroundCorrectionMethod "Gas blank measured before each spot; background period during single spot transient (rapid intensity rise and decay) used for background correction" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:carrierGasFlowRateDefault "Carrier gas flow: 0.6 L/min; species not named (carrier gas identity not stated in Table 1 or text)" ;
    ada:constantsAndReferenceValuesUsedDefault "missing" ;
    ada:elementalFractionationCorrection "External calibration using calibration curve method with IVB iron meteorite standards; ⁶¹Ni as IS from EPMA corrects for ablation yield differences between sample and standard" ;
    ada:internalStandardApproach "Single element externally measured by EPMA: ⁶¹Ni concentration from EPMA at exact analysis location used as IS" ;
    ada:internalStandardElement "⁶¹Ni; concentration from EPMA measured at exact analysis spot location" ;
    ada:ionCounterDeadTimeDefault -9999 ;
    ada:massBiasCorrectionStrategy "missing" ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:primaryStandardNameDefault "Warburton Range (IVB iron meteorite; Walker et al. 2008) — used as primary external standard and for calibration curve method" ;
    ada:rasterLineSpacingDefault "missing" ;
    ada:sampleIntroduction "missing" ;
    ada:samplingUnit "missing" ;
    ada:secondaryReferenceMaterialDefault "Tawallah Valley (IVB iron meteorite; Walker et al. 2008) — measured as secondary/check standard alongside unknowns" ;
    ada:signalCollectionMode "missing" ;
    ada:signalIntegrationIntervalMethod "Time-resolved signals monitored; analyses with elevated Mg, Si, P, S (inclusion indicators) excluded; stable signal intervals used for integration" ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:totalIntegrationTimePerOutputDataPointDefault -9999 ;
    ada:uncertaintyLevel "missing" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/isobaricInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Isobaric Interference Corrections Applied" ;
    schema1:valueName "isobaricInterferenceCorrectionsApplied" ;
    ada:dataType "boolean" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "uri" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/monitoredMasses> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Monitored Masses" ;
    schema1:valueName "monitoredMasses" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/coolantGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 12 ;
    schema1:description "Cool gas: 12–13 l min⁻¹ Ar; Auxiliary: 0.6–1.2 l min⁻¹" ;
    schema1:name "Coolant (Plasma) Gas Flow Rate" ;
    schema1:valueName "coolantGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/makeUpGasAndFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 9e-01 ;
    schema1:description "Ar make-up: 0.9–1.2 l min⁻¹; Ar auxiliary: 0.6–1.2 l min⁻¹" ;
    schema1:name "Make-up Gas and Flow Rate" ;
    schema1:valueName "makeUpGasAndFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/massResolutionSetting> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Unit resolution (quadrupole fixed)" ;
    schema1:name "Mass Resolution Setting" ;
    schema1:valueName "massResolutionSetting" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/normalizationStandardsBasedCorrectionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "No post-acquisition normalization; calibration curve method using IVB standards provides direct quantification" ;
    schema1:name "Normalization / Standards-Based Correction" ;
    schema1:valueName "normalizationStandardsBasedCorrectionDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/rfPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1400 ;
    schema1:description "1400 W" ;
    schema1:name "RF Power" ;
    schema1:valueName "rfPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/sampleFormAnalyticalSubstrateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "In situ — polished epoxy thick section (petropoxy 154 resin, 0.5 µm diamond finish)" ;
    schema1:name "Sample Form / Analytical Substrate" ;
    schema1:valueName "sampleFormAnalyticalSubstrateDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/spikeOutlierFilteringApproachDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Monitoring of Mg, Si, P, S to check for micro-inclusions (sulfides); analyses with elevated inclusion signals excluded entirely" ;
    schema1:name "Spike / Outlier Filtering Approach" ;
    schema1:valueName "spikeOutlierFilteringApproachDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/uncertaintyPropagationMethodDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "2SE of individual spot measurements reported" ;
    schema1:name "Uncertainty Propagation Method" ;
    schema1:valueName "uncertaintyPropagationMethodDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/laserPulseDuration> a schema1:PropertyValueSpecification ;
    schema1:name "Laser Pulse Duration" ;
    schema1:value "~220 fs (Ti:sapphire IFRIT system)" ;
    schema1:valueName "laserPulseDuration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/massResolutionSetting> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Single-collector quadrupole (Q-ICP-MS)" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Thermo Scientific X-series 2 (Q-ICP-MS)" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/coolantGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/rfPowerDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Interface-Cone> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/interfaceConeConfiguration> ;
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
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/LaserAblation/laserPulseDuration> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Laser Ablation System" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Cyber Laser IFRIT (Ti:sapphire fs UV laser, 260 nm)" ] ;
    schema1:name "example instrumentName" ;
    ada:laserFluenceDefault "12 J cm⁻²" ;
    ada:laserRepetitionRateDefault "20 Hz" ;
    ada:laserSpotGeometryDefault "30 µm circular" ;
    ada:laserType "260 nm Ti:sapphire femtosecond UV; pulse duration ~220 fs (IFRIT system)" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/interfaceConeConfiguration> a schema1:PropertyValue ;
    schema1:name "Interface Cone Configuration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/interfaceConeConfiguration> ;
    schema1:value "Ni micro-skimmer cone Xs; Ni sampler cone" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign> a schema1:PropertyValue ;
    schema1:name "Multi-Run Sequential Analysis Design" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign> ;
    schema1:value "Single spot per location (30 µm circular)" .


```


### laQicpmsTAPP example Liu2024
laQicpmsTAPP instance derived from Liu et al. 2024 (JAAS 39) Extraterrestrial samples (Li-borate flux glass) Spot analysis fs-LA-Q-ICP-MS Chinese Academy of Sciences.
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
  "@id": "ex:laQicpmsTAPP-Liu2024",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Liu et al. (2024) Extraterrestrial Flux Glass fs-LA-ICP-MS Spot v1",
  "schema:description": "Target: bulk trace element analysis of extraterrestrial samples using only 10 mg; Li-borate flux fusion (35:1 dilution) with fs laser — first reported use of fs laser for flux fusion glass analysis; non-matrix-matched external standards demonstrated accurate with fs laser",
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
            "Li-borate flux fusion glass (extraterrestrial sample preparation)"
          ]
        },
        {
          "@id": "ada:parameter/laQicpmsTAPP/sampleFormAnalyticalSubstrateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleFormAnalyticalSubstrateDefault",
          "schema:name": "Sample Form / Analytical Substrate",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Li-borate flux fusion glass disc (10 mg sample + 350 mg Li₂B₄O₇, 35:1 dilution)"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/laQicpmsTAPP/fusionFluxAndDilutionRatioDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "fusionFluxAndDilutionRatioDefault",
            "schema:name": "Fusion Flux and Dilution Ratio",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Li₂B₄O₇ flux; sample:flux = 1:35 (10 mg sample + 350 mg flux)"
          },
          {
            "@id": "ada:parameter/module/LaserAblation/preAblationSurfaceTreatmentDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "preAblationSurfaceTreatmentDefault",
            "schema:name": "Pre Ablation Surface Treatment",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Surface cleaning with ethanol before analysis"
          }
        ],
        "schema:description": "Li-borate fusion: 350 mg Li₂B₄O₇ + 10 mg powdered sample fused in Pt-Au crucible (M4 automatic fluxer); glass surface cleaned with ethanol before LA",
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
            "@id": "ada:parameter/laQicpmsTAPP/spikeOutlierFilteringApproachDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "spikeOutlierFilteringApproachDefault",
            "schema:name": "Spike / Outlier Filtering Approach",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Homogeneity index (H) applied to test element distribution; Co, Ni, Cu in high-Si glass (GSR-1) identified as near-LOD and flagged; flux blank contributions to pollution elements subtracted"
          },
          {
            "@id": "ada:parameter/laQicpmsTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "pulseAnalogDetectorNonlinearityCorrectionDefault",
            "schema:name": "Pulse/Analog Detector Nonlinearity Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Applied: dual detector mode (30 ms / 10 ms dwell alternation)"
          },
          {
            "@id": "ada:parameter/laQicpmsTAPP/normalizationStandardsBasedCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "normalizationStandardsBasedCorrectionDefault",
            "schema:name": "Normalization / Standards-Based Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "No post-acquisition normalization beyond IS approach (two IS elements applied element-specifically)"
          }
        ],
        "ada:detectionLimitMethod": "Pettke (2012) for most elements: LOD = (3.29 × √(Rbkg × DT × ...) + 2.71) / (Nan × DT × S); LOQ for pollution elements = blank value + 10SD (IUPAC Gold Book)",
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
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Agilent 8900 (Q-ICP-MS; ICP-MS/MS capable)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/massResolutionSetting",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSetting",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Unit resolution (quadrupole; ICP-MS/MS mode not specified)"
        },
        {
          "@id": "ada:parameter/laQicpmsTAPP/detectorConfiguration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laQicpmsTAPP/detectorConfiguration"
            }
          ],
          "schema:name": "Detector Configuration",
          "schema:value": "Dual mode detector (30 ms / 10 ms dwell alternation)"
        },
        {
          "@id": "ada:parameter/laQicpmsTAPP/icpTuningDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "icpTuningDefault",
          "schema:name": "ICP Tuning",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Gas flows optimized via spot ablation of NIST SRM 612 to obtain maximum signal intensities while maintaining ThO/Th <0.3% and U/Th at 0.95–1.05"
        },
        {
          "@id": "ada:parameter/laQicpmsTAPP/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "25 s washout between analyses (25 s gas blank → 45 s ablation → 25 s washout)"
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
              "@id": "ada:parameter/laQicpmsTAPP/coolantGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantGasFlowRateDefault",
              "schema:name": "Coolant (Plasma) Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 15,
              "schema:description": "Plasma gas flow: 15 l min⁻¹; Auxiliary gas: 0.85 l min⁻¹"
            },
            {
              "@id": "ada:parameter/laQicpmsTAPP/rfPowerDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "rfPowerDefault",
              "schema:name": "RF Power",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 1550,
              "schema:description": "1550 W"
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
        }
      ],
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
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/module/LaserAblation/laserPulseDuration",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "laserPulseDuration",
          "schema:name": "Laser Pulse Duration",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:value": "Femtosecond (exact value not stated; GenesisGEO fs laser)"
        }
      ],
      "schema:model": {
        "schema:name": "Shanghai Chemlab GenesisGEO (high-repetition-rate fs laser, 343 nm)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "343 nm fs (GenesisGEO high-repetition-rate femtosecond laser)",
      "ada:laserSpotGeometryDefault": "100×100 µm square (stated as 100 µm diameter spot at 1 Hz)",
      "ada:laserFluenceDefault": "6.79 J cm⁻²",
      "ada:laserRepetitionRateDefault": "1 Hz",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/Laser-Ablation-System",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:carrierGasFlowRateDefault": "He: 0.7 l min⁻¹ (chamber) + 0.1 l min⁻¹ (cup gas)",
  "ada:oxideProductionMethodAndThreshold": "ThO⁺/Th⁺ (mass 248/232) <0.3%; U/Th monitored at 0.95–1.05",
  "ada:analysisSequenceDefault": "Gas blank (25 s) → ablation (45 s) → washout (25 s); NIST 612 and 614 as external standards; BHVO-2 and 6 GRMs measured as unknowns",
  "ada:backgroundCountTimeDefault": "25 s gas blank before each ablation",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign"
        }
      ],
      "schema:name": "Multi-Run Sequential Analysis Design",
      "schema:value": "Single spot per location (45 s ablation at 1 Hz)"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/detectionLimitDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "detectionLimitDefault",
      "schema:name": "Detection Limit",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 32,
      "schema:description": "LODs for 32 elements in Li-borate glass BHVO-2: 0.005–23.5 µg g⁻¹ (dilution-limited; much higher than undiluted glass LODs); LODs for NIST 610: 0.007–0.45 µg g⁻¹; LOQ = 3.3 × LOD (Pettke 2012) for most elements; LOQ for pollution elements = blank + 10SD (Gold Book IUPAC)"
    }
  ],
  "ada:internalStandardApproach": "Two internal standards: Si from XRF SiO₂ (for Co, Ni, Cu, Zn); Al from XRF Al₂O₃ (for all other trace elements); non-matrix-matched external standards (NIST 612 + 614) used; fs laser minimizes matrix effects",
  "ada:internalStandardElement": "Si (SiO₂ from XRF) for Co, Ni, Cu, Zn; Al (Al₂O₃ from XRF) for all other 28 trace elements",
  "ada:elementalFractionationCorrection": [
    "Femtosecond laser substantially reduces elemental fractionation and matrix effects (stated); non-matrix-matched external standards (NIST 612 + 614) used successfully with fs laser (verified by GRM accuracy assessment)"
  ],
  "ada:signalIntegrationIntervalMethod": "Time-resolved signals inspected visually; flux blank contributions to pollution elements (V, Co, Zn, Ba, La, Ce, Ta, U) identified and subtracted; 9-spot grid homogeneity tested before analysis",
  "ada:blankBackgroundCorrectionMethod": "Gas blank measured for 25 s before each ablation; background subtracted per isotope",
  "ada:primaryStandardNameDefault": "NIST SRM 612 + NIST SRM 614 (non-matrix-matched external standards); self-made BHVO-2 lithium borate glass (matrix-matched) tested as alternative but NIST 612+614 found sufficient with fs laser",
  "ada:calibrationMeasurementFrequency": "NIST SRM 612 and 614 measured as external standards within session; BHVO-2 and other GRMs as unknowns",
  "ada:secondaryReferenceMaterialDefault": [
    "AC-E (granite, CRPG), GSR-1 (granite, NRCG), JB-1b (basalt, GSJ), GSR-3 (basalt, NRCG), AGV-2 (andesite, USGS), W-2A (diabase, USGS) — 6 GRMs covering mafic to felsic rock types analyzed as unknowns; also NWA14526 (lunar basalt) and NWA13190 (shergottite) compared with SN-ICP-MS"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "fs-LA-Q-ICP-MS"
    }
  ],
  "schema:creator": {
    "schema:name": "Liu, Xue, Li, Wang et al.",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "State Key Laboratory of Lithospheric Evolution and Environmental Coevolution, IGGCAS, Beijing, China"
  },
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NSFC; Chinese Academy of Sciences"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Liu et al. (2024) JAAS 39, 2728; Pettke et al. (2012) for LOD"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Iolite 4 (Paton et al. 2011)"
    }
  ],
  "ada:ablationSamplingMode": [
    "Spot (stationary; single spot at 1 Hz)"
  ],
  "ada:ablationSpotDurationDefault": "45 s ablation (after 25 s gas blank; 25 s washout between analyses)",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "²¹Sc",
      "⁵¹V",
      "⁵²Cr",
      "⁵⁹Co",
      "⁶⁰Ni",
      "⁶³Cu",
      "⁶⁶Zn",
      "⁶⁹Ga",
      "⁸⁵Rb",
      "⁸⁸Sr",
      "⁸⁹Y",
      "⁹⁰Zr",
      "⁹³Nb",
      "¹³³Cs",
      "¹³⁷Ba",
      "¹³⁹La",
      "¹⁴⁰Ce",
      "¹⁴¹Pr",
      "¹⁴⁶Nd",
      "¹⁴⁷Sm",
      "¹⁵³Eu",
      "¹⁵⁷Gd",
      "¹⁵⁹Tb",
      "¹⁶³Dy",
      "¹⁶⁵Ho",
      "¹⁶⁶Er",
      "¹⁶⁹Tm",
      "¹⁷²Yb",
      "¹⁷⁵Lu",
      "¹⁷⁸Hf",
      "¹⁸¹Ta",
      "²³²Th",
      "²³⁸U (32 trace elements)"
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
        "@id": "ada:analyteColumn/laQicpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "boolean",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "uri"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
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
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
  "ada:signalCollectionMode": "missing",
  "ada:targetSelectionCriteriaDefault": "missing",
  "ada:totalIntegrationTimePerOutputDataPointDefault": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:laQicpmsTAPP-Liu2024",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Liu et al. (2024) Extraterrestrial Flux Glass fs-LA-ICP-MS Spot v1",
  "schema:description": "Target: bulk trace element analysis of extraterrestrial samples using only 10 mg; Li-borate flux fusion (35:1 dilution) with fs laser \u2014 first reported use of fs laser for flux fusion glass analysis; non-matrix-matched external standards demonstrated accurate with fs laser",
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
            "Li-borate flux fusion glass (extraterrestrial sample preparation)"
          ]
        },
        {
          "@id": "ada:parameter/laQicpmsTAPP/sampleFormAnalyticalSubstrateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleFormAnalyticalSubstrateDefault",
          "schema:name": "Sample Form / Analytical Substrate",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Li-borate flux fusion glass disc (10 mg sample + 350 mg Li\u2082B\u2084O\u2087, 35:1 dilution)"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/laQicpmsTAPP/fusionFluxAndDilutionRatioDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "fusionFluxAndDilutionRatioDefault",
            "schema:name": "Fusion Flux and Dilution Ratio",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Li\u2082B\u2084O\u2087 flux; sample:flux = 1:35 (10 mg sample + 350 mg flux)"
          },
          {
            "@id": "ada:parameter/module/LaserAblation/preAblationSurfaceTreatmentDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "preAblationSurfaceTreatmentDefault",
            "schema:name": "Pre Ablation Surface Treatment",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Surface cleaning with ethanol before analysis"
          }
        ],
        "schema:description": "Li-borate fusion: 350 mg Li\u2082B\u2084O\u2087 + 10 mg powdered sample fused in Pt-Au crucible (M4 automatic fluxer); glass surface cleaned with ethanol before LA",
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
            "@id": "ada:parameter/laQicpmsTAPP/spikeOutlierFilteringApproachDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "spikeOutlierFilteringApproachDefault",
            "schema:name": "Spike / Outlier Filtering Approach",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Homogeneity index (H) applied to test element distribution; Co, Ni, Cu in high-Si glass (GSR-1) identified as near-LOD and flagged; flux blank contributions to pollution elements subtracted"
          },
          {
            "@id": "ada:parameter/laQicpmsTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "pulseAnalogDetectorNonlinearityCorrectionDefault",
            "schema:name": "Pulse/Analog Detector Nonlinearity Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Applied: dual detector mode (30 ms / 10 ms dwell alternation)"
          },
          {
            "@id": "ada:parameter/laQicpmsTAPP/normalizationStandardsBasedCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "normalizationStandardsBasedCorrectionDefault",
            "schema:name": "Normalization / Standards-Based Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "No post-acquisition normalization beyond IS approach (two IS elements applied element-specifically)"
          }
        ],
        "ada:detectionLimitMethod": "Pettke (2012) for most elements: LOD = (3.29 \u00d7 \u221a(Rbkg \u00d7 DT \u00d7 ...) + 2.71) / (Nan \u00d7 DT \u00d7 S); LOQ for pollution elements = blank value + 10SD (IUPAC Gold Book)",
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
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Agilent 8900 (Q-ICP-MS; ICP-MS/MS capable)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/massResolutionSetting",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSetting",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Unit resolution (quadrupole; ICP-MS/MS mode not specified)"
        },
        {
          "@id": "ada:parameter/laQicpmsTAPP/detectorConfiguration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laQicpmsTAPP/detectorConfiguration"
            }
          ],
          "schema:name": "Detector Configuration",
          "schema:value": "Dual mode detector (30 ms / 10 ms dwell alternation)"
        },
        {
          "@id": "ada:parameter/laQicpmsTAPP/icpTuningDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "icpTuningDefault",
          "schema:name": "ICP Tuning",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Gas flows optimized via spot ablation of NIST SRM 612 to obtain maximum signal intensities while maintaining ThO/Th <0.3% and U/Th at 0.95\u20131.05"
        },
        {
          "@id": "ada:parameter/laQicpmsTAPP/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "25 s washout between analyses (25 s gas blank \u2192 45 s ablation \u2192 25 s washout)"
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
              "@id": "ada:parameter/laQicpmsTAPP/coolantGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantGasFlowRateDefault",
              "schema:name": "Coolant (Plasma) Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 15,
              "schema:description": "Plasma gas flow: 15 l min\u207b\u00b9; Auxiliary gas: 0.85 l min\u207b\u00b9"
            },
            {
              "@id": "ada:parameter/laQicpmsTAPP/rfPowerDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "rfPowerDefault",
              "schema:name": "RF Power",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 1550,
              "schema:description": "1550 W"
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
        }
      ],
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
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/module/LaserAblation/laserPulseDuration",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "laserPulseDuration",
          "schema:name": "Laser Pulse Duration",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:value": "Femtosecond (exact value not stated; GenesisGEO fs laser)"
        }
      ],
      "schema:model": {
        "schema:name": "Shanghai Chemlab GenesisGEO (high-repetition-rate fs laser, 343 nm)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "343 nm fs (GenesisGEO high-repetition-rate femtosecond laser)",
      "ada:laserSpotGeometryDefault": "100\u00d7100 \u00b5m square (stated as 100 \u00b5m diameter spot at 1 Hz)",
      "ada:laserFluenceDefault": "6.79 J cm\u207b\u00b2",
      "ada:laserRepetitionRateDefault": "1 Hz",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/Laser-Ablation-System",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:carrierGasFlowRateDefault": "He: 0.7 l min\u207b\u00b9 (chamber) + 0.1 l min\u207b\u00b9 (cup gas)",
  "ada:oxideProductionMethodAndThreshold": "ThO\u207a/Th\u207a (mass 248/232) <0.3%; U/Th monitored at 0.95\u20131.05",
  "ada:analysisSequenceDefault": "Gas blank (25 s) \u2192 ablation (45 s) \u2192 washout (25 s); NIST 612 and 614 as external standards; BHVO-2 and 6 GRMs measured as unknowns",
  "ada:backgroundCountTimeDefault": "25 s gas blank before each ablation",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign"
        }
      ],
      "schema:name": "Multi-Run Sequential Analysis Design",
      "schema:value": "Single spot per location (45 s ablation at 1 Hz)"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/detectionLimitDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "detectionLimitDefault",
      "schema:name": "Detection Limit",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 32,
      "schema:description": "LODs for 32 elements in Li-borate glass BHVO-2: 0.005\u201323.5 \u00b5g g\u207b\u00b9 (dilution-limited; much higher than undiluted glass LODs); LODs for NIST 610: 0.007\u20130.45 \u00b5g g\u207b\u00b9; LOQ = 3.3 \u00d7 LOD (Pettke 2012) for most elements; LOQ for pollution elements = blank + 10SD (Gold Book IUPAC)"
    }
  ],
  "ada:internalStandardApproach": "Two internal standards: Si from XRF SiO\u2082 (for Co, Ni, Cu, Zn); Al from XRF Al\u2082O\u2083 (for all other trace elements); non-matrix-matched external standards (NIST 612 + 614) used; fs laser minimizes matrix effects",
  "ada:internalStandardElement": "Si (SiO\u2082 from XRF) for Co, Ni, Cu, Zn; Al (Al\u2082O\u2083 from XRF) for all other 28 trace elements",
  "ada:elementalFractionationCorrection": [
    "Femtosecond laser substantially reduces elemental fractionation and matrix effects (stated); non-matrix-matched external standards (NIST 612 + 614) used successfully with fs laser (verified by GRM accuracy assessment)"
  ],
  "ada:signalIntegrationIntervalMethod": "Time-resolved signals inspected visually; flux blank contributions to pollution elements (V, Co, Zn, Ba, La, Ce, Ta, U) identified and subtracted; 9-spot grid homogeneity tested before analysis",
  "ada:blankBackgroundCorrectionMethod": "Gas blank measured for 25 s before each ablation; background subtracted per isotope",
  "ada:primaryStandardNameDefault": "NIST SRM 612 + NIST SRM 614 (non-matrix-matched external standards); self-made BHVO-2 lithium borate glass (matrix-matched) tested as alternative but NIST 612+614 found sufficient with fs laser",
  "ada:calibrationMeasurementFrequency": "NIST SRM 612 and 614 measured as external standards within session; BHVO-2 and other GRMs as unknowns",
  "ada:secondaryReferenceMaterialDefault": [
    "AC-E (granite, CRPG), GSR-1 (granite, NRCG), JB-1b (basalt, GSJ), GSR-3 (basalt, NRCG), AGV-2 (andesite, USGS), W-2A (diabase, USGS) \u2014 6 GRMs covering mafic to felsic rock types analyzed as unknowns; also NWA14526 (lunar basalt) and NWA13190 (shergottite) compared with SN-ICP-MS"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "fs-LA-Q-ICP-MS"
    }
  ],
  "schema:creator": {
    "schema:name": "Liu, Xue, Li, Wang et al.",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "State Key Laboratory of Lithospheric Evolution and Environmental Coevolution, IGGCAS, Beijing, China"
  },
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NSFC; Chinese Academy of Sciences"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Liu et al. (2024) JAAS 39, 2728; Pettke et al. (2012) for LOD"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Iolite 4 (Paton et al. 2011)"
    }
  ],
  "ada:ablationSamplingMode": [
    "Spot (stationary; single spot at 1 Hz)"
  ],
  "ada:ablationSpotDurationDefault": "45 s ablation (after 25 s gas blank; 25 s washout between analyses)",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "\u00b2\u00b9Sc",
      "\u2075\u00b9V",
      "\u2075\u00b2Cr",
      "\u2075\u2079Co",
      "\u2076\u2070Ni",
      "\u2076\u00b3Cu",
      "\u2076\u2076Zn",
      "\u2076\u2079Ga",
      "\u2078\u2075Rb",
      "\u2078\u2078Sr",
      "\u2078\u2079Y",
      "\u2079\u2070Zr",
      "\u2079\u00b3Nb",
      "\u00b9\u00b3\u00b3Cs",
      "\u00b9\u00b3\u2077Ba",
      "\u00b9\u00b3\u2079La",
      "\u00b9\u2074\u2070Ce",
      "\u00b9\u2074\u00b9Pr",
      "\u00b9\u2074\u2076Nd",
      "\u00b9\u2074\u2077Sm",
      "\u00b9\u2075\u00b3Eu",
      "\u00b9\u2075\u2077Gd",
      "\u00b9\u2075\u2079Tb",
      "\u00b9\u2076\u00b3Dy",
      "\u00b9\u2076\u2075Ho",
      "\u00b9\u2076\u2076Er",
      "\u00b9\u2076\u2079Tm",
      "\u00b9\u2077\u00b2Yb",
      "\u00b9\u2077\u2075Lu",
      "\u00b9\u2077\u2078Hf",
      "\u00b9\u2078\u00b9Ta",
      "\u00b2\u00b3\u00b2Th",
      "\u00b2\u00b3\u2078U (32 trace elements)"
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
        "@id": "ada:analyteColumn/laQicpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "boolean",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "uri"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
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
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
  "ada:signalCollectionMode": "missing",
  "ada:targetSelectionCriteriaDefault": "missing",
  "ada:totalIntegrationTimePerOutputDataPointDefault": -9999,
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

ex:laQicpmsTAPP-Liu2024 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/fusionFluxAndDilutionRatioDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/LaserAblation/preAblationSurfaceTreatmentDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Li-borate fusion: 350 mg Li₂B₄O₇ + 10 mg powdered sample fused in Pt-Au crucible (M4 automatic fluxer); glass surface cleaned with ethanol before LA" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/normalizationStandardsBasedCorrectionDefault>,
                        <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault>,
                        <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/spikeOutlierFilteringApproachDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ;
                    ada:detectionLimitMethod "Pettke (2012) for most elements: LOD = (3.29 × √(Rbkg × DT × ...) + 2.71) / (Nan × DT × S); LOQ for pollution elements = blank value + 10SD (IUPAC Gold Book)" ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/detectionLimitDefault>,
        <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign> ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Liu, Xue, Li, Wang et al." ] ;
    schema1:datePublished "missing" ;
    schema1:description "Target: bulk trace element analysis of extraterrestrial samples using only 10 mg; Li-borate flux fusion (35:1 dilution) with fs laser — first reported use of fs laser for flux fusion glass analysis; non-matrix-matched external standards demonstrated accurate with fs laser" ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NSFC; Chinese Academy of Sciences" ] ;
    schema1:instrument <https://example.org/instrument/ICPMS>,
        <https://example.org/instrument/Laser-Ablation-System> ;
    schema1:location [ a schema1:Place ;
            schema1:name "State Key Laboratory of Lithospheric Evolution and Environmental Coevolution, IGGCAS, Beijing, China" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "fs-LA-Q-ICP-MS" ] ;
    schema1:name "Liu et al. (2024) Extraterrestrial Flux Glass fs-LA-ICP-MS Spot v1" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Li-borate flux fusion glass (extraterrestrial sample preparation)" ],
                <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/sampleFormAnalyticalSubstrateDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Liu et al. (2024) JAAS 39, 2728; Pettke et al. (2012) for LOD" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:ablationPitDepthRateDefault "missing" ;
    ada:ablationSamplingMode "Spot (stationary; single spot at 1 Hz)" ;
    ada:ablationSpotDurationDefault "45 s ablation (after 25 s gas blank; 25 s washout between analyses)" ;
    ada:analysisSequenceDefault "Gas blank (25 s) → ablation (45 s) → washout (25 s); NIST 612 and 614 as external standards; BHVO-2 and 6 GRMs measured as unknowns" ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/isobaricInterferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/limitOfQuantificationMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/monitoredMasses>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ;
            ada:defaultAnalytes "²³²Th",
                "²³⁸U (32 trace elements)",
                "²¹Sc",
                "¹³³Cs",
                "¹³⁷Ba",
                "¹³⁹La",
                "¹⁴¹Pr",
                "¹⁴⁰Ce",
                "¹⁴⁶Nd",
                "¹⁴⁷Sm",
                "¹⁵³Eu",
                "¹⁵⁷Gd",
                "¹⁵⁹Tb",
                "¹⁶³Dy",
                "¹⁶⁵Ho",
                "¹⁶⁶Er",
                "¹⁶⁹Tm",
                "¹⁷²Yb",
                "¹⁷⁵Lu",
                "¹⁷⁸Hf",
                "¹⁸¹Ta",
                "⁵²Cr",
                "⁵¹V",
                "⁵⁹Co",
                "⁶³Cu",
                "⁶⁰Ni",
                "⁶⁶Zn",
                "⁶⁹Ga",
                "⁸⁵Rb",
                "⁸⁸Sr",
                "⁸⁹Y",
                "⁹³Nb",
                "⁹⁰Zr" ] ;
    ada:backgroundCountTimeDefault "25 s gas blank before each ablation" ;
    ada:blankBackgroundCorrectionMethod "Gas blank measured for 25 s before each ablation; background subtracted per isotope" ;
    ada:calibrationMeasurementFrequency "NIST SRM 612 and 614 measured as external standards within session; BHVO-2 and other GRMs as unknowns" ;
    ada:carrierGasFlowRateDefault "He: 0.7 l min⁻¹ (chamber) + 0.1 l min⁻¹ (cup gas)" ;
    ada:constantsAndReferenceValuesUsedDefault "missing" ;
    ada:elementalFractionationCorrection "Femtosecond laser substantially reduces elemental fractionation and matrix effects (stated); non-matrix-matched external standards (NIST 612 + 614) used successfully with fs laser (verified by GRM accuracy assessment)" ;
    ada:internalStandardApproach "Two internal standards: Si from XRF SiO₂ (for Co, Ni, Cu, Zn); Al from XRF Al₂O₃ (for all other trace elements); non-matrix-matched external standards (NIST 612 + 614) used; fs laser minimizes matrix effects" ;
    ada:internalStandardElement "Si (SiO₂ from XRF) for Co, Ni, Cu, Zn; Al (Al₂O₃ from XRF) for all other 28 trace elements" ;
    ada:ionCounterDeadTimeDefault -9999 ;
    ada:massBiasCorrectionStrategy "missing" ;
    ada:oxideProductionMethodAndThreshold "ThO⁺/Th⁺ (mass 248/232) <0.3%; U/Th monitored at 0.95–1.05" ;
    ada:primaryStandardNameDefault "NIST SRM 612 + NIST SRM 614 (non-matrix-matched external standards); self-made BHVO-2 lithium borate glass (matrix-matched) tested as alternative but NIST 612+614 found sufficient with fs laser" ;
    ada:rasterLineSpacingDefault "missing" ;
    ada:sampleIntroduction "missing" ;
    ada:samplingUnit "missing" ;
    ada:secondaryReferenceMaterialDefault "AC-E (granite, CRPG), GSR-1 (granite, NRCG), JB-1b (basalt, GSJ), GSR-3 (basalt, NRCG), AGV-2 (andesite, USGS), W-2A (diabase, USGS) — 6 GRMs covering mafic to felsic rock types analyzed as unknowns; also NWA14526 (lunar basalt) and NWA13190 (shergottite) compared with SN-ICP-MS" ;
    ada:signalCollectionMode "missing" ;
    ada:signalIntegrationIntervalMethod "Time-resolved signals inspected visually; flux blank contributions to pollution elements (V, Co, Zn, Ba, La, Ce, Ta, U) identified and subtracted; 9-spot grid homogeneity tested before analysis" ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:totalIntegrationTimePerOutputDataPointDefault -9999 ;
    ada:uncertaintyLevel "missing" ;
    bios:computationalTool [ schema1:name "Iolite 4 (Paton et al. 2011)" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/isobaricInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Isobaric Interference Corrections Applied" ;
    schema1:valueName "isobaricInterferenceCorrectionsApplied" ;
    ada:dataType "boolean" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "uri" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/monitoredMasses> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Monitored Masses" ;
    schema1:valueName "monitoredMasses" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/coolantGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 15 ;
    schema1:description "Plasma gas flow: 15 l min⁻¹; Auxiliary gas: 0.85 l min⁻¹" ;
    schema1:name "Coolant (Plasma) Gas Flow Rate" ;
    schema1:valueName "coolantGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/detectionLimitDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 32 ;
    schema1:description "LODs for 32 elements in Li-borate glass BHVO-2: 0.005–23.5 µg g⁻¹ (dilution-limited; much higher than undiluted glass LODs); LODs for NIST 610: 0.007–0.45 µg g⁻¹; LOQ = 3.3 × LOD (Pettke 2012) for most elements; LOQ for pollution elements = blank + 10SD (Gold Book IUPAC)" ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimitDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/fusionFluxAndDilutionRatioDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Li₂B₄O₇ flux; sample:flux = 1:35 (10 mg sample + 350 mg flux)" ;
    schema1:name "Fusion Flux and Dilution Ratio" ;
    schema1:valueName "fusionFluxAndDilutionRatioDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/icpTuningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Gas flows optimized via spot ablation of NIST SRM 612 to obtain maximum signal intensities while maintaining ThO/Th <0.3% and U/Th at 0.95–1.05" ;
    schema1:name "ICP Tuning" ;
    schema1:valueName "icpTuningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/massResolutionSetting> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Unit resolution (quadrupole; ICP-MS/MS mode not specified)" ;
    schema1:name "Mass Resolution Setting" ;
    schema1:valueName "massResolutionSetting" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/memoryEffectMitigationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "25 s washout between analyses (25 s gas blank → 45 s ablation → 25 s washout)" ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:valueName "memoryEffectMitigationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/normalizationStandardsBasedCorrectionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "No post-acquisition normalization beyond IS approach (two IS elements applied element-specifically)" ;
    schema1:name "Normalization / Standards-Based Correction" ;
    schema1:valueName "normalizationStandardsBasedCorrectionDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Applied: dual detector mode (30 ms / 10 ms dwell alternation)" ;
    schema1:name "Pulse/Analog Detector Nonlinearity Correction" ;
    schema1:valueName "pulseAnalogDetectorNonlinearityCorrectionDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/rfPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1550 ;
    schema1:description "1550 W" ;
    schema1:name "RF Power" ;
    schema1:valueName "rfPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/sampleFormAnalyticalSubstrateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Li-borate flux fusion glass disc (10 mg sample + 350 mg Li₂B₄O₇, 35:1 dilution)" ;
    schema1:name "Sample Form / Analytical Substrate" ;
    schema1:valueName "sampleFormAnalyticalSubstrateDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/spikeOutlierFilteringApproachDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Homogeneity index (H) applied to test element distribution; Co, Ni, Cu in high-Si glass (GSR-1) identified as near-LOD and flagged; flux blank contributions to pollution elements subtracted" ;
    schema1:name "Spike / Outlier Filtering Approach" ;
    schema1:valueName "spikeOutlierFilteringApproachDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/laserPulseDuration> a schema1:PropertyValueSpecification ;
    schema1:name "Laser Pulse Duration" ;
    schema1:value "Femtosecond (exact value not stated; GenesisGEO fs laser)" ;
    schema1:valueName "laserPulseDuration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/preAblationSurfaceTreatmentDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Surface cleaning with ethanol before analysis" ;
    schema1:name "Pre Ablation Surface Treatment" ;
    schema1:valueName "preAblationSurfaceTreatmentDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/detectorConfiguration>,
        <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/icpTuningDefault>,
        <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/massResolutionSetting>,
        <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/memoryEffectMitigationDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Agilent 8900 (Q-ICP-MS; ICP-MS/MS capable)" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/coolantGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/rfPowerDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Interface-Cone> a schema1:Product,
        schema1:Thing ;
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
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/LaserAblation/laserPulseDuration> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Laser Ablation System" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Shanghai Chemlab GenesisGEO (high-repetition-rate fs laser, 343 nm)" ] ;
    schema1:name "example instrumentName" ;
    ada:laserFluenceDefault "6.79 J cm⁻²" ;
    ada:laserRepetitionRateDefault "1 Hz" ;
    ada:laserSpotGeometryDefault "100×100 µm square (stated as 100 µm diameter spot at 1 Hz)" ;
    ada:laserType "343 nm fs (GenesisGEO high-repetition-rate femtosecond laser)" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/detectorConfiguration> a schema1:PropertyValue ;
    schema1:name "Detector Configuration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/detectorConfiguration> ;
    schema1:value "Dual mode detector (30 ms / 10 ms dwell alternation)" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign> a schema1:PropertyValue ;
    schema1:name "Multi-Run Sequential Analysis Design" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign> ;
    schema1:value "Single spot per location (45 s ablation at 1 Hz)" .


```


### laQicpmsTAPP example Liu2025
laQicpmsTAPP instance derived from Liu et al. 2025 (GCA 393) Experimental silicate glass Spot analysis ns-LA-Q-ICP-MS Guangzhou Inst. Geochemistry.
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
  "@id": "ex:laQicpmsTAPP-Liu2025",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Liu et al. (2025) Experimental Silicate Glass LA-ICP-MS Spot v1",
  "schema:description": "Analysis of quenched experimental glasses from high-pressure (1 GPa) piston-cylinder experiments; Au and Cu solubility measurements; smooth time-resolved signals indicate fully dissolved Au (no micronuggets)",
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
            "Experimental dacitic silicate glass (quench product)"
          ]
        },
        {
          "@id": "ada:parameter/laQicpmsTAPP/sampleFormAnalyticalSubstrateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleFormAnalyticalSubstrateDefault",
          "schema:name": "Sample Form / Analytical Substrate",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "In situ — polished epoxy mount (experimental capsule half-section)"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Experimental capsule longitudinally sectioned with wire saw; half mounted in epoxy for analysis",
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
            "@id": "ada:parameter/laQicpmsTAPP/spikeOutlierFilteringApproachDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "spikeOutlierFilteringApproachDefault",
            "schema:name": "Spike / Outlier Filtering Approach",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Micronuggets identified from Au signal spikes in time-resolved spectra; excluded from integration (smooth signals = fully dissolved Au; Fig. 1 shows this criterion)"
          },
          {
            "@id": "ada:parameter/laQicpmsTAPP/normalizationStandardsBasedCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "normalizationStandardsBasedCorrectionDefault",
            "schema:name": "Normalization / Standards-Based Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "No post-acquisition normalization beyond IS (Si from EMP)"
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
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Agilent 7900 (Q-ICP-MS)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/massResolutionSetting",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSetting",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Unit resolution (quadrupole fixed)"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/ICPMS",
      "schema:hasPart": [
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
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "Laser Ablation System",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Resonetics 193 nm ArF excimer laser (coupled to Cetac Analyte HE system)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "193 nm (CetacAnalyte HE; ns pulse)",
      "schema:name": "Cetac Analyte HE system (stated as the laser ablation system coupled to Agilent 7900)",
      "ada:laserSpotGeometryDefault": "40 µm circular (silicate glass)",
      "ada:laserFluenceDefault": "~2.5 J cm⁻² (stated as \"energy of ~2.5 J/cm²\")",
      "ada:laserRepetitionRateDefault": "7 Hz",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/Laser-Ablation-System"
    }
  ],
  "ada:carrierGasFlowRateDefault": "He (flow rate not stated; carrier gas with N₂ or Ar mixed for sensitivity optimization)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsTAPP/makeUpGasAndFlowRateDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "makeUpGasAndFlowRateDefault",
      "schema:name": "Make-up Gas and Flow Rate",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N₂ or Ar mixed into He carrier for sensitivity optimization (amounts not stated)"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign"
        }
      ],
      "schema:name": "Multi-Run Sequential Analysis Design",
      "schema:value": "Single spot per location (~40 s ablation at 7 Hz)"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/detectionLimitDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "detectionLimitDefault",
      "schema:name": "Detection Limit",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 0.01,
      "schema:description": "Detection limits for Au ~0.01 ppm; Cu ~0.1 ppm in silicate melt (stated in paper)"
    }
  ],
  "ada:analysisSequenceDefault": "NIST 610 as primary standard measured in session; NIST 612 and BCR-2G as monitoring standards; unknowns bracketed by standards",
  "ada:internalStandardApproach": "Single element from EMP: Si (SiO₂ from EMP for silicate glass); NIST 610 as external standard",
  "ada:internalStandardElement": "Si from EMP (SiO₂ wt% for silicate glass)",
  "ada:elementalFractionationCorrection": [
    "Femtosecond laser reduces LIEF; NIST 610 external standard; Si IS from EMP corrects for ablation yield"
  ],
  "ada:signalIntegrationIntervalMethod": "Time-resolved LA-ICP-MS signal inspected; micronuggets identified from spikes in Au signal and excluded from integration to obtain smooth signals (verified by Fig. 1 in paper)",
  "ada:primaryStandardNameDefault": "NIST 610 (primary external standard; Jochum et al. 2011); Si from EMP as IS",
  "ada:calibrationMeasurementFrequency": "NIST 610 as primary; NIST 612 and BCR-2G as monitoring standards",
  "ada:secondaryReferenceMaterialDefault": [
    "NIST SRM 612 and BCR-2G (monitoring standards measured in same sessions)"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-Q-ICP-MS"
    }
  ],
  "schema:creator": {
    "schema:name": "Liu, Li, Xu, Xiong et al.",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "State Key Laboratory of Isotope Geochemistry, Guangzhou Institute of Geochemistry, CAS, China"
  },
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "Strategic Priority Research Program (B) CAS; NSFC 92062222, 42073057, 42250710679, 42250202, 42273023"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Liu et al. (2025) GCA 393, 170; Xu et al. (2022) for experimental protocol"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:ablationSpotDurationDefault": "~40 s (inferred from typical CetacAnalyte HE protocol for glass)",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "¹⁹⁷Au",
      "⁶³Cu (primary targets)",
      "all detected via Agilent 7900 (exact isotope list not fully stated)"
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
        "@id": "ada:analyteColumn/laQicpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "boolean",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "uri"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
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
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:backgroundCountTimeDefault": -9999,
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
  "ada:signalCollectionMode": "missing",
  "ada:targetSelectionCriteriaDefault": "missing",
  "ada:totalIntegrationTimePerOutputDataPointDefault": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:laQicpmsTAPP-Liu2025",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Liu et al. (2025) Experimental Silicate Glass LA-ICP-MS Spot v1",
  "schema:description": "Analysis of quenched experimental glasses from high-pressure (1 GPa) piston-cylinder experiments; Au and Cu solubility measurements; smooth time-resolved signals indicate fully dissolved Au (no micronuggets)",
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
            "Experimental dacitic silicate glass (quench product)"
          ]
        },
        {
          "@id": "ada:parameter/laQicpmsTAPP/sampleFormAnalyticalSubstrateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleFormAnalyticalSubstrateDefault",
          "schema:name": "Sample Form / Analytical Substrate",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "In situ \u2014 polished epoxy mount (experimental capsule half-section)"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Experimental capsule longitudinally sectioned with wire saw; half mounted in epoxy for analysis",
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
            "@id": "ada:parameter/laQicpmsTAPP/spikeOutlierFilteringApproachDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "spikeOutlierFilteringApproachDefault",
            "schema:name": "Spike / Outlier Filtering Approach",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Micronuggets identified from Au signal spikes in time-resolved spectra; excluded from integration (smooth signals = fully dissolved Au; Fig. 1 shows this criterion)"
          },
          {
            "@id": "ada:parameter/laQicpmsTAPP/normalizationStandardsBasedCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "normalizationStandardsBasedCorrectionDefault",
            "schema:name": "Normalization / Standards-Based Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "No post-acquisition normalization beyond IS (Si from EMP)"
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
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Agilent 7900 (Q-ICP-MS)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/massResolutionSetting",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSetting",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Unit resolution (quadrupole fixed)"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/ICPMS",
      "schema:hasPart": [
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
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "Laser Ablation System",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Resonetics 193 nm ArF excimer laser (coupled to Cetac Analyte HE system)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "193 nm (CetacAnalyte HE; ns pulse)",
      "schema:name": "Cetac Analyte HE system (stated as the laser ablation system coupled to Agilent 7900)",
      "ada:laserSpotGeometryDefault": "40 \u00b5m circular (silicate glass)",
      "ada:laserFluenceDefault": "~2.5 J cm\u207b\u00b2 (stated as \"energy of ~2.5 J/cm\u00b2\")",
      "ada:laserRepetitionRateDefault": "7 Hz",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/Laser-Ablation-System"
    }
  ],
  "ada:carrierGasFlowRateDefault": "He (flow rate not stated; carrier gas with N\u2082 or Ar mixed for sensitivity optimization)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsTAPP/makeUpGasAndFlowRateDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "makeUpGasAndFlowRateDefault",
      "schema:name": "Make-up Gas and Flow Rate",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N\u2082 or Ar mixed into He carrier for sensitivity optimization (amounts not stated)"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign"
        }
      ],
      "schema:name": "Multi-Run Sequential Analysis Design",
      "schema:value": "Single spot per location (~40 s ablation at 7 Hz)"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/detectionLimitDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "detectionLimitDefault",
      "schema:name": "Detection Limit",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 0.01,
      "schema:description": "Detection limits for Au ~0.01 ppm; Cu ~0.1 ppm in silicate melt (stated in paper)"
    }
  ],
  "ada:analysisSequenceDefault": "NIST 610 as primary standard measured in session; NIST 612 and BCR-2G as monitoring standards; unknowns bracketed by standards",
  "ada:internalStandardApproach": "Single element from EMP: Si (SiO\u2082 from EMP for silicate glass); NIST 610 as external standard",
  "ada:internalStandardElement": "Si from EMP (SiO\u2082 wt% for silicate glass)",
  "ada:elementalFractionationCorrection": [
    "Femtosecond laser reduces LIEF; NIST 610 external standard; Si IS from EMP corrects for ablation yield"
  ],
  "ada:signalIntegrationIntervalMethod": "Time-resolved LA-ICP-MS signal inspected; micronuggets identified from spikes in Au signal and excluded from integration to obtain smooth signals (verified by Fig. 1 in paper)",
  "ada:primaryStandardNameDefault": "NIST 610 (primary external standard; Jochum et al. 2011); Si from EMP as IS",
  "ada:calibrationMeasurementFrequency": "NIST 610 as primary; NIST 612 and BCR-2G as monitoring standards",
  "ada:secondaryReferenceMaterialDefault": [
    "NIST SRM 612 and BCR-2G (monitoring standards measured in same sessions)"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-Q-ICP-MS"
    }
  ],
  "schema:creator": {
    "schema:name": "Liu, Li, Xu, Xiong et al.",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "State Key Laboratory of Isotope Geochemistry, Guangzhou Institute of Geochemistry, CAS, China"
  },
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "Strategic Priority Research Program (B) CAS; NSFC 92062222, 42073057, 42250710679, 42250202, 42273023"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Liu et al. (2025) GCA 393, 170; Xu et al. (2022) for experimental protocol"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:ablationSpotDurationDefault": "~40 s (inferred from typical CetacAnalyte HE protocol for glass)",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "\u00b9\u2079\u2077Au",
      "\u2076\u00b3Cu (primary targets)",
      "all detected via Agilent 7900 (exact isotope list not fully stated)"
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
        "@id": "ada:analyteColumn/laQicpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "boolean",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "uri"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
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
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:backgroundCountTimeDefault": -9999,
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
  "ada:signalCollectionMode": "missing",
  "ada:targetSelectionCriteriaDefault": "missing",
  "ada:totalIntegrationTimePerOutputDataPointDefault": -9999,
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

ex:laQicpmsTAPP-Liu2025 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Experimental capsule longitudinally sectioned with wire saw; half mounted in epoxy for analysis" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/normalizationStandardsBasedCorrectionDefault>,
                        <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/spikeOutlierFilteringApproachDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/detectionLimitDefault>,
        <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/makeUpGasAndFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign> ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Liu, Li, Xu, Xiong et al." ] ;
    schema1:datePublished "missing" ;
    schema1:description "Analysis of quenched experimental glasses from high-pressure (1 GPa) piston-cylinder experiments; Au and Cu solubility measurements; smooth time-resolved signals indicate fully dissolved Au (no micronuggets)" ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "Strategic Priority Research Program (B) CAS; NSFC 92062222, 42073057, 42250710679, 42250202, 42273023" ] ;
    schema1:instrument <https://example.org/instrument/ICPMS>,
        <https://example.org/instrument/Laser-Ablation-System> ;
    schema1:location [ a schema1:Place ;
            schema1:name "State Key Laboratory of Isotope Geochemistry, Guangzhou Institute of Geochemistry, CAS, China" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "LA-Q-ICP-MS" ] ;
    schema1:name "Liu et al. (2025) Experimental Silicate Glass LA-ICP-MS Spot v1" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Experimental dacitic silicate glass (quench product)" ],
                <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/sampleFormAnalyticalSubstrateDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Liu et al. (2025) GCA 393, 170; Xu et al. (2022) for experimental protocol" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:ablationPitDepthRateDefault "missing" ;
    ada:ablationSpotDurationDefault "~40 s (inferred from typical CetacAnalyte HE protocol for glass)" ;
    ada:analysisSequenceDefault "NIST 610 as primary standard measured in session; NIST 612 and BCR-2G as monitoring standards; unknowns bracketed by standards" ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/isobaricInterferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/limitOfQuantificationMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/monitoredMasses>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ;
            ada:defaultAnalytes "all detected via Agilent 7900 (exact isotope list not fully stated)",
                "¹⁹⁷Au",
                "⁶³Cu (primary targets)" ] ;
    ada:backgroundCountTimeDefault -9999 ;
    ada:blankBackgroundCorrectionMethod "missing" ;
    ada:calibrationMeasurementFrequency "NIST 610 as primary; NIST 612 and BCR-2G as monitoring standards" ;
    ada:carrierGasFlowRateDefault "He (flow rate not stated; carrier gas with N₂ or Ar mixed for sensitivity optimization)" ;
    ada:constantsAndReferenceValuesUsedDefault "missing" ;
    ada:elementalFractionationCorrection "Femtosecond laser reduces LIEF; NIST 610 external standard; Si IS from EMP corrects for ablation yield" ;
    ada:internalStandardApproach "Single element from EMP: Si (SiO₂ from EMP for silicate glass); NIST 610 as external standard" ;
    ada:internalStandardElement "Si from EMP (SiO₂ wt% for silicate glass)" ;
    ada:ionCounterDeadTimeDefault -9999 ;
    ada:massBiasCorrectionStrategy "missing" ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:primaryStandardNameDefault "NIST 610 (primary external standard; Jochum et al. 2011); Si from EMP as IS" ;
    ada:rasterLineSpacingDefault "missing" ;
    ada:sampleIntroduction "missing" ;
    ada:samplingUnit "missing" ;
    ada:secondaryReferenceMaterialDefault "NIST SRM 612 and BCR-2G (monitoring standards measured in same sessions)" ;
    ada:signalCollectionMode "missing" ;
    ada:signalIntegrationIntervalMethod "Time-resolved LA-ICP-MS signal inspected; micronuggets identified from spikes in Au signal and excluded from integration to obtain smooth signals (verified by Fig. 1 in paper)" ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:totalIntegrationTimePerOutputDataPointDefault -9999 ;
    ada:uncertaintyLevel "missing" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/isobaricInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Isobaric Interference Corrections Applied" ;
    schema1:valueName "isobaricInterferenceCorrectionsApplied" ;
    ada:dataType "boolean" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "uri" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/monitoredMasses> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Monitored Masses" ;
    schema1:valueName "monitoredMasses" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/detectionLimitDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1e-02 ;
    schema1:description "Detection limits for Au ~0.01 ppm; Cu ~0.1 ppm in silicate melt (stated in paper)" ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimitDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/makeUpGasAndFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N₂ or Ar mixed into He carrier for sensitivity optimization (amounts not stated)" ;
    schema1:name "Make-up Gas and Flow Rate" ;
    schema1:valueName "makeUpGasAndFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/massResolutionSetting> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Unit resolution (quadrupole fixed)" ;
    schema1:name "Mass Resolution Setting" ;
    schema1:valueName "massResolutionSetting" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/normalizationStandardsBasedCorrectionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "No post-acquisition normalization beyond IS (Si from EMP)" ;
    schema1:name "Normalization / Standards-Based Correction" ;
    schema1:valueName "normalizationStandardsBasedCorrectionDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/sampleFormAnalyticalSubstrateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "In situ — polished epoxy mount (experimental capsule half-section)" ;
    schema1:name "Sample Form / Analytical Substrate" ;
    schema1:valueName "sampleFormAnalyticalSubstrateDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/spikeOutlierFilteringApproachDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Micronuggets identified from Au signal spikes in time-resolved spectra; excluded from integration (smooth signals = fully dissolved Au; Fig. 1 shows this criterion)" ;
    schema1:name "Spike / Outlier Filtering Approach" ;
    schema1:valueName "spikeOutlierFilteringApproachDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/massResolutionSetting> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Agilent 7900 (Q-ICP-MS)" ] ;
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
            schema1:name "Resonetics 193 nm ArF excimer laser (coupled to Cetac Analyte HE system)" ] ;
    schema1:name "Cetac Analyte HE system (stated as the laser ablation system coupled to Agilent 7900)" ;
    ada:laserFluenceDefault "~2.5 J cm⁻² (stated as \"energy of ~2.5 J/cm²\")" ;
    ada:laserRepetitionRateDefault "7 Hz" ;
    ada:laserSpotGeometryDefault "40 µm circular (silicate glass)" ;
    ada:laserType "193 nm (CetacAnalyte HE; ns pulse)" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign> a schema1:PropertyValue ;
    schema1:name "Multi-Run Sequential Analysis Design" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign> ;
    schema1:value "Single spot per location (~40 s ablation at 7 Hz)" .


```


### laQicpmsTAPP example Liu2025-2
laQicpmsTAPP instance derived from Liu et al. 2025 (GCA 393) Experimental sulfide Spot analysis ns-LA-Q-ICP-MS Guangzhou Inst. Geochemistry.
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
  "@id": "ex:laQicpmsTAPP-Liu2025-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Liu et al. (2025) Experimental Sulfide LA-ICP-MS Spot v1",
  "schema:description": "Analysis of quenched experimental pyrrhotite (Fe₁₋ₓS) from same piston-cylinder experiments; 20 µm spot required due to small grain size (5–50 µm); same instrument and analytical session as glass protocol",
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
            "Experimental pyrrhotite (Fe₁₋ₓS) sulfide (quench product)"
          ]
        },
        {
          "@id": "ada:parameter/laQicpmsTAPP/sampleFormAnalyticalSubstrateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleFormAnalyticalSubstrateDefault",
          "schema:name": "Sample Form / Analytical Substrate",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "In situ — polished epoxy mount (same capsule section as glass protocol)"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Same capsule section as silicate glass; sulfide grains ≥20 µm selected by SEM-BSE",
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
            "@id": "ada:parameter/laQicpmsTAPP/spikeOutlierFilteringApproachDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "spikeOutlierFilteringApproachDefault",
            "schema:name": "Spike / Outlier Filtering Approach",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Same approach as glass; Au spike identification critical for determining solubility vs. nugget contribution"
          },
          {
            "@id": "ada:parameter/laQicpmsTAPP/normalizationStandardsBasedCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "normalizationStandardsBasedCorrectionDefault",
            "schema:name": "Normalization / Standards-Based Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "No post-acquisition normalization beyond IS (Fe from EMP)"
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
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Agilent 7900 (Q-ICP-MS)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/massResolutionSetting",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSetting",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Unit resolution (quadrupole fixed)"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/ICPMS",
      "schema:hasPart": [
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
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "Laser Ablation System",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Resonetics 193 nm ArF excimer laser (coupled to Cetac Analyte HE system; same system as glass protocol)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "193 nm (CetacAnalyte HE; ns pulse)",
      "schema:name": "Cetac Analyte HE system (same as silicate glass protocol)",
      "ada:laserSpotGeometryDefault": "20 µm circular (sulfide; grain sizes >20 µm selected)",
      "ada:laserFluenceDefault": "~2.5 J cm⁻²",
      "ada:laserRepetitionRateDefault": "7 Hz",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/Laser-Ablation-System"
    }
  ],
  "ada:carrierGasFlowRateDefault": "He (flow rate not stated; same system as glass protocol)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsTAPP/makeUpGasAndFlowRateDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "makeUpGasAndFlowRateDefault",
      "schema:name": "Make-up Gas and Flow Rate",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N₂ or Ar mixed (same protocol as glass)"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign"
        }
      ],
      "schema:name": "Multi-Run Sequential Analysis Design",
      "schema:value": "Single spot per location (sulfides; same acquisition parameters as glass but 20 µm spot)"
    }
  ],
  "ada:analysisSequenceDefault": "Same bracketing as silicate glass protocol",
  "ada:internalStandardApproach": "Single element from EMP: Fe (FeOT from EMP for sulfide); NIST 610 as external standard",
  "ada:internalStandardElement": "Fe from EMP (FeOT wt% for sulfide)",
  "ada:elementalFractionationCorrection": [
    "Femtosecond laser reduces LIEF; NIST 610 external standard; Fe IS from EMP corrects for ablation yield; micronuggets identified from Au signal spikes and excluded from integration"
  ],
  "ada:signalIntegrationIntervalMethod": "Same approach as glass; micronugget identification from Au signal spikes critical for sulfide analyses",
  "ada:primaryStandardNameDefault": "NIST 610 (primary external standard); Fe from EMP as IS",
  "ada:calibrationMeasurementFrequency": "Same bracketing as silicate glass protocol",
  "ada:secondaryReferenceMaterialDefault": [
    "NIST SRM 612 and BCR-2G (same monitoring standard set as glass protocol)"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-Q-ICP-MS"
    }
  ],
  "schema:creator": {
    "schema:name": "Liu, Li, Xu, Xiong et al.",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "State Key Laboratory of Isotope Geochemistry, Guangzhou Institute of Geochemistry, CAS, China"
  },
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "Strategic Priority Research Program (B) CAS; NSFC 92062222, 42073057, 42250710679, 42250202, 42273023"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Liu et al. (2025) GCA 393, 170; Xu et al. (2022)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:ablationSpotDurationDefault": "~40 s (same protocol; grain size >20 µm selected)",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "¹⁹⁷Au",
      "⁶³Cu (primary targets; Si and Fe from EMP as internal standards)"
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
        "@id": "ada:analyteColumn/laQicpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "boolean",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "uri"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
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
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:backgroundCountTimeDefault": -9999,
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
  "ada:signalCollectionMode": "missing",
  "ada:targetSelectionCriteriaDefault": "missing",
  "ada:totalIntegrationTimePerOutputDataPointDefault": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:laQicpmsTAPP-Liu2025-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Liu et al. (2025) Experimental Sulfide LA-ICP-MS Spot v1",
  "schema:description": "Analysis of quenched experimental pyrrhotite (Fe\u2081\u208b\u2093S) from same piston-cylinder experiments; 20 \u00b5m spot required due to small grain size (5\u201350 \u00b5m); same instrument and analytical session as glass protocol",
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
            "Experimental pyrrhotite (Fe\u2081\u208b\u2093S) sulfide (quench product)"
          ]
        },
        {
          "@id": "ada:parameter/laQicpmsTAPP/sampleFormAnalyticalSubstrateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleFormAnalyticalSubstrateDefault",
          "schema:name": "Sample Form / Analytical Substrate",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "In situ \u2014 polished epoxy mount (same capsule section as glass protocol)"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Same capsule section as silicate glass; sulfide grains \u226520 \u00b5m selected by SEM-BSE",
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
            "@id": "ada:parameter/laQicpmsTAPP/spikeOutlierFilteringApproachDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "spikeOutlierFilteringApproachDefault",
            "schema:name": "Spike / Outlier Filtering Approach",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Same approach as glass; Au spike identification critical for determining solubility vs. nugget contribution"
          },
          {
            "@id": "ada:parameter/laQicpmsTAPP/normalizationStandardsBasedCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "normalizationStandardsBasedCorrectionDefault",
            "schema:name": "Normalization / Standards-Based Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "No post-acquisition normalization beyond IS (Fe from EMP)"
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
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Agilent 7900 (Q-ICP-MS)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/massResolutionSetting",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSetting",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Unit resolution (quadrupole fixed)"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/ICPMS",
      "schema:hasPart": [
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
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "Laser Ablation System",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Resonetics 193 nm ArF excimer laser (coupled to Cetac Analyte HE system; same system as glass protocol)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "193 nm (CetacAnalyte HE; ns pulse)",
      "schema:name": "Cetac Analyte HE system (same as silicate glass protocol)",
      "ada:laserSpotGeometryDefault": "20 \u00b5m circular (sulfide; grain sizes >20 \u00b5m selected)",
      "ada:laserFluenceDefault": "~2.5 J cm\u207b\u00b2",
      "ada:laserRepetitionRateDefault": "7 Hz",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/Laser-Ablation-System"
    }
  ],
  "ada:carrierGasFlowRateDefault": "He (flow rate not stated; same system as glass protocol)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsTAPP/makeUpGasAndFlowRateDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "makeUpGasAndFlowRateDefault",
      "schema:name": "Make-up Gas and Flow Rate",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N\u2082 or Ar mixed (same protocol as glass)"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign"
        }
      ],
      "schema:name": "Multi-Run Sequential Analysis Design",
      "schema:value": "Single spot per location (sulfides; same acquisition parameters as glass but 20 \u00b5m spot)"
    }
  ],
  "ada:analysisSequenceDefault": "Same bracketing as silicate glass protocol",
  "ada:internalStandardApproach": "Single element from EMP: Fe (FeOT from EMP for sulfide); NIST 610 as external standard",
  "ada:internalStandardElement": "Fe from EMP (FeOT wt% for sulfide)",
  "ada:elementalFractionationCorrection": [
    "Femtosecond laser reduces LIEF; NIST 610 external standard; Fe IS from EMP corrects for ablation yield; micronuggets identified from Au signal spikes and excluded from integration"
  ],
  "ada:signalIntegrationIntervalMethod": "Same approach as glass; micronugget identification from Au signal spikes critical for sulfide analyses",
  "ada:primaryStandardNameDefault": "NIST 610 (primary external standard); Fe from EMP as IS",
  "ada:calibrationMeasurementFrequency": "Same bracketing as silicate glass protocol",
  "ada:secondaryReferenceMaterialDefault": [
    "NIST SRM 612 and BCR-2G (same monitoring standard set as glass protocol)"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-Q-ICP-MS"
    }
  ],
  "schema:creator": {
    "schema:name": "Liu, Li, Xu, Xiong et al.",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "State Key Laboratory of Isotope Geochemistry, Guangzhou Institute of Geochemistry, CAS, China"
  },
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "Strategic Priority Research Program (B) CAS; NSFC 92062222, 42073057, 42250710679, 42250202, 42273023"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Liu et al. (2025) GCA 393, 170; Xu et al. (2022)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:ablationSpotDurationDefault": "~40 s (same protocol; grain size >20 \u00b5m selected)",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "\u00b9\u2079\u2077Au",
      "\u2076\u00b3Cu (primary targets; Si and Fe from EMP as internal standards)"
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
        "@id": "ada:analyteColumn/laQicpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "boolean",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "uri"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
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
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:backgroundCountTimeDefault": -9999,
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
  "ada:signalCollectionMode": "missing",
  "ada:targetSelectionCriteriaDefault": "missing",
  "ada:totalIntegrationTimePerOutputDataPointDefault": -9999,
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

ex:laQicpmsTAPP-Liu2025-2 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/normalizationStandardsBasedCorrectionDefault>,
                        <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/spikeOutlierFilteringApproachDefault> ;
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
                    schema1:description "Same capsule section as silicate glass; sulfide grains ≥20 µm selected by SEM-BSE" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/makeUpGasAndFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign> ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Liu, Li, Xu, Xiong et al." ] ;
    schema1:datePublished "missing" ;
    schema1:description "Analysis of quenched experimental pyrrhotite (Fe₁₋ₓS) from same piston-cylinder experiments; 20 µm spot required due to small grain size (5–50 µm); same instrument and analytical session as glass protocol" ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "Strategic Priority Research Program (B) CAS; NSFC 92062222, 42073057, 42250710679, 42250202, 42273023" ] ;
    schema1:instrument <https://example.org/instrument/ICPMS>,
        <https://example.org/instrument/Laser-Ablation-System> ;
    schema1:location [ a schema1:Place ;
            schema1:name "State Key Laboratory of Isotope Geochemistry, Guangzhou Institute of Geochemistry, CAS, China" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "LA-Q-ICP-MS" ] ;
    schema1:name "Liu et al. (2025) Experimental Sulfide LA-ICP-MS Spot v1" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Experimental pyrrhotite (Fe₁₋ₓS) sulfide (quench product)" ],
                <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/sampleFormAnalyticalSubstrateDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Liu et al. (2025) GCA 393, 170; Xu et al. (2022)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:ablationPitDepthRateDefault "missing" ;
    ada:ablationSpotDurationDefault "~40 s (same protocol; grain size >20 µm selected)" ;
    ada:analysisSequenceDefault "Same bracketing as silicate glass protocol" ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/isobaricInterferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/limitOfQuantificationMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/monitoredMasses>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ;
            ada:defaultAnalytes "¹⁹⁷Au",
                "⁶³Cu (primary targets; Si and Fe from EMP as internal standards)" ] ;
    ada:backgroundCountTimeDefault -9999 ;
    ada:blankBackgroundCorrectionMethod "missing" ;
    ada:calibrationMeasurementFrequency "Same bracketing as silicate glass protocol" ;
    ada:carrierGasFlowRateDefault "He (flow rate not stated; same system as glass protocol)" ;
    ada:constantsAndReferenceValuesUsedDefault "missing" ;
    ada:elementalFractionationCorrection "Femtosecond laser reduces LIEF; NIST 610 external standard; Fe IS from EMP corrects for ablation yield; micronuggets identified from Au signal spikes and excluded from integration" ;
    ada:internalStandardApproach "Single element from EMP: Fe (FeOT from EMP for sulfide); NIST 610 as external standard" ;
    ada:internalStandardElement "Fe from EMP (FeOT wt% for sulfide)" ;
    ada:ionCounterDeadTimeDefault -9999 ;
    ada:massBiasCorrectionStrategy "missing" ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:primaryStandardNameDefault "NIST 610 (primary external standard); Fe from EMP as IS" ;
    ada:rasterLineSpacingDefault "missing" ;
    ada:sampleIntroduction "missing" ;
    ada:samplingUnit "missing" ;
    ada:secondaryReferenceMaterialDefault "NIST SRM 612 and BCR-2G (same monitoring standard set as glass protocol)" ;
    ada:signalCollectionMode "missing" ;
    ada:signalIntegrationIntervalMethod "Same approach as glass; micronugget identification from Au signal spikes critical for sulfide analyses" ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:totalIntegrationTimePerOutputDataPointDefault -9999 ;
    ada:uncertaintyLevel "missing" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/isobaricInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Isobaric Interference Corrections Applied" ;
    schema1:valueName "isobaricInterferenceCorrectionsApplied" ;
    ada:dataType "boolean" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "uri" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/monitoredMasses> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Monitored Masses" ;
    schema1:valueName "monitoredMasses" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/makeUpGasAndFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N₂ or Ar mixed (same protocol as glass)" ;
    schema1:name "Make-up Gas and Flow Rate" ;
    schema1:valueName "makeUpGasAndFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/massResolutionSetting> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Unit resolution (quadrupole fixed)" ;
    schema1:name "Mass Resolution Setting" ;
    schema1:valueName "massResolutionSetting" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/normalizationStandardsBasedCorrectionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "No post-acquisition normalization beyond IS (Fe from EMP)" ;
    schema1:name "Normalization / Standards-Based Correction" ;
    schema1:valueName "normalizationStandardsBasedCorrectionDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/sampleFormAnalyticalSubstrateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "In situ — polished epoxy mount (same capsule section as glass protocol)" ;
    schema1:name "Sample Form / Analytical Substrate" ;
    schema1:valueName "sampleFormAnalyticalSubstrateDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/spikeOutlierFilteringApproachDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Same approach as glass; Au spike identification critical for determining solubility vs. nugget contribution" ;
    schema1:name "Spike / Outlier Filtering Approach" ;
    schema1:valueName "spikeOutlierFilteringApproachDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/massResolutionSetting> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Agilent 7900 (Q-ICP-MS)" ] ;
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
            schema1:name "Resonetics 193 nm ArF excimer laser (coupled to Cetac Analyte HE system; same system as glass protocol)" ] ;
    schema1:name "Cetac Analyte HE system (same as silicate glass protocol)" ;
    ada:laserFluenceDefault "~2.5 J cm⁻²" ;
    ada:laserRepetitionRateDefault "7 Hz" ;
    ada:laserSpotGeometryDefault "20 µm circular (sulfide; grain sizes >20 µm selected)" ;
    ada:laserType "193 nm (CetacAnalyte HE; ns pulse)" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign> a schema1:PropertyValue ;
    schema1:name "Multi-Run Sequential Analysis Design" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign> ;
    schema1:value "Single spot per location (sulfides; same acquisition parameters as glass but 20 µm spot)" .


```


### laQicpmsTAPP example Liu2016
laQicpmsTAPP instance derived from Liu et al. 2016 (M&PS 51) Tissint martian meteorite Silicates, oxides & glass Spot analysis LA-Q-ICP-MS Virginia Tech.
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
  "@id": "ex:laQicpmsTAPP-Liu2016",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "laQicpms protocol — Liu2016",
  "schema:description": "Paper broadly follows Udry et al. (2012) and Pernet-Fisher et al. (2014) for procedure; two IS approaches used for different mineral phases (oxide-sum for silicates; EMP CaO for phosphate); 90 µm spot used on some olivines to evaluate whether low REE signals result from insufficient sampling volume",
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
            "Martian meteorite (Tissint) silicates, oxides, and glass: olivine, low-Ca pyroxene, augite, maskelynite, Fe-Ti-Cr oxides, shock melt glass, fusion crust"
          ]
        },
        {
          "@id": "ada:parameter/laQicpmsTAPP/sampleFormAnalyticalSubstrateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleFormAnalyticalSubstrateDefault",
          "schema:name": "Sample Form / Analytical Substrate",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "In situ — polished thin section (Tissint sections: Tata-2-C3, Tata-3-C2, UT1, UT3)"
        }
      ]
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Agilent 7500ce ICP-MS",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/ICPMS",
      "schema:hasPart": [
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
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "Laser Ablation System",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/module/LaserAblation/laserEnergyDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "laserEnergyDefault",
          "schema:name": "Laser Energy",
          "ada:dataType": "number",
          "ada:fieldScope": "session",
          "schema:defaultValue": 150,
          "schema:description": "150 mJ output energy"
        }
      ],
      "schema:model": {
        "schema:name": "GeoLasPro (193 nm Excimer laser-ablation system; manufacturer not stated by name; GeoLasPro is a Lambda Physik/Coherent product)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "193 nm Excimer (ArF excimer)",
      "ada:laserSpotGeometryDefault": "24 and 32 µm diameter (commonly used for silicates and glass); 90 µm (some olivine analyses to evaluate low REE signal sampling)",
      "ada:laserFluenceDefault": "7–10 J/m² (stated in paper; units as written; likely a typographic error for J/cm²)",
      "ada:laserRepetitionRateDefault": "5 Hz",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/Laser-Ablation-System",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:analysisSequenceDefault": "NIST 610 glass standard analyzed before and after every session; unknowns in between",
  "ada:backgroundCountTimeDefault": "50 s (background counted for 50 s before each LA-ICP-MS analysis)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign"
        }
      ],
      "schema:name": "Multi-Run Sequential Analysis Design",
      "schema:value": "Single spot analysis per location"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/detectionLimitDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "detectionLimitDefault",
      "schema:name": "Detection Limit",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 3,
      "schema:description": "Referenced in Table 3 and Table S1; specific values not directly stated in main text; REE in olivines below detection limits at 24–32 µm conditions"
    }
  ],
  "ada:internalStandardApproach": "Normalization to 100 wt% oxide total (for silicates and oxides)",
  "ada:internalStandardElement": "None (oxide sum normalization, 100 wt% total)",
  "ada:elementalFractionationCorrection": [
    "External calibration using NIST 610 glass standard analyzed before and after session; oxide-sum normalization corrects for ablation yield variation; no explicit downhole fractionation correction described"
  ],
  "ada:signalIntegrationIntervalMethod": "Time-lapse plots of each spot examined; only the plateau region used to quantify trace element abundances",
  "ada:blankBackgroundCorrectionMethod": "50 s background measurement before each analysis; background subtracted (method not explicitly described beyond counting duration)",
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
            "@id": "ada:parameter/laQicpmsTAPP/normalizationStandardsBasedCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "normalizationStandardsBasedCorrectionDefault",
            "schema:name": "Normalization / Standards-Based Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "100% oxide total normalization applied per analysis for silicates and oxides; NIST 610 used for external calibration before and after session"
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
  "ada:primaryStandardNameDefault": "NIST 610 glass standard",
  "ada:calibrationMeasurementFrequency": "NIST 610 glass standard analyzed before and after every session",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-ICP-MS (193 nm excimer laser + ICP-MS; top-level technique)"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Department of Geosciences, Virginia Tech"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Udry et al. (2012) and Pernet-Fisher et al. (2014) cited as broad references for the analytical procedure"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "EPMA (EMP)",
        "schema:description": "EPMA provides major element concentrations for comparison with LA-ICP-MS oxide-sum normalization results; agreement within <10% verified"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "AMS ver. 1.0 (Mutchler et al. 2008; Analysis Management System, stand-alone software)"
    }
  ],
  "ada:ablationSamplingMode": [
    "Spot (stationary)"
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ablationSpotDurationDefault": -9999,
  "ada:carrierGasFlowRateDefault": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
  "ada:signalCollectionMode": "missing",
  "ada:targetSelectionCriteriaDefault": "missing",
  "ada:totalIntegrationTimePerOutputDataPointDefault": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:laQicpmsTAPP-Liu2016",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "laQicpms protocol \u2014 Liu2016",
  "schema:description": "Paper broadly follows Udry et al. (2012) and Pernet-Fisher et al. (2014) for procedure; two IS approaches used for different mineral phases (oxide-sum for silicates; EMP CaO for phosphate); 90 \u00b5m spot used on some olivines to evaluate whether low REE signals result from insufficient sampling volume",
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
            "Martian meteorite (Tissint) silicates, oxides, and glass: olivine, low-Ca pyroxene, augite, maskelynite, Fe-Ti-Cr oxides, shock melt glass, fusion crust"
          ]
        },
        {
          "@id": "ada:parameter/laQicpmsTAPP/sampleFormAnalyticalSubstrateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleFormAnalyticalSubstrateDefault",
          "schema:name": "Sample Form / Analytical Substrate",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "In situ \u2014 polished thin section (Tissint sections: Tata-2-C3, Tata-3-C2, UT1, UT3)"
        }
      ]
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Agilent 7500ce ICP-MS",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/ICPMS",
      "schema:hasPart": [
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
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "Laser Ablation System",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/module/LaserAblation/laserEnergyDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "laserEnergyDefault",
          "schema:name": "Laser Energy",
          "ada:dataType": "number",
          "ada:fieldScope": "session",
          "schema:defaultValue": 150,
          "schema:description": "150 mJ output energy"
        }
      ],
      "schema:model": {
        "schema:name": "GeoLasPro (193 nm Excimer laser-ablation system; manufacturer not stated by name; GeoLasPro is a Lambda Physik/Coherent product)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "193 nm Excimer (ArF excimer)",
      "ada:laserSpotGeometryDefault": "24 and 32 \u00b5m diameter (commonly used for silicates and glass); 90 \u00b5m (some olivine analyses to evaluate low REE signal sampling)",
      "ada:laserFluenceDefault": "7\u201310 J/m\u00b2 (stated in paper; units as written; likely a typographic error for J/cm\u00b2)",
      "ada:laserRepetitionRateDefault": "5 Hz",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/Laser-Ablation-System",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:analysisSequenceDefault": "NIST 610 glass standard analyzed before and after every session; unknowns in between",
  "ada:backgroundCountTimeDefault": "50 s (background counted for 50 s before each LA-ICP-MS analysis)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign"
        }
      ],
      "schema:name": "Multi-Run Sequential Analysis Design",
      "schema:value": "Single spot analysis per location"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/detectionLimitDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "detectionLimitDefault",
      "schema:name": "Detection Limit",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 3,
      "schema:description": "Referenced in Table 3 and Table S1; specific values not directly stated in main text; REE in olivines below detection limits at 24\u201332 \u00b5m conditions"
    }
  ],
  "ada:internalStandardApproach": "Normalization to 100 wt% oxide total (for silicates and oxides)",
  "ada:internalStandardElement": "None (oxide sum normalization, 100 wt% total)",
  "ada:elementalFractionationCorrection": [
    "External calibration using NIST 610 glass standard analyzed before and after session; oxide-sum normalization corrects for ablation yield variation; no explicit downhole fractionation correction described"
  ],
  "ada:signalIntegrationIntervalMethod": "Time-lapse plots of each spot examined; only the plateau region used to quantify trace element abundances",
  "ada:blankBackgroundCorrectionMethod": "50 s background measurement before each analysis; background subtracted (method not explicitly described beyond counting duration)",
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
            "@id": "ada:parameter/laQicpmsTAPP/normalizationStandardsBasedCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "normalizationStandardsBasedCorrectionDefault",
            "schema:name": "Normalization / Standards-Based Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "100% oxide total normalization applied per analysis for silicates and oxides; NIST 610 used for external calibration before and after session"
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
  "ada:primaryStandardNameDefault": "NIST 610 glass standard",
  "ada:calibrationMeasurementFrequency": "NIST 610 glass standard analyzed before and after every session",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-ICP-MS (193 nm excimer laser + ICP-MS; top-level technique)"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Department of Geosciences, Virginia Tech"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Udry et al. (2012) and Pernet-Fisher et al. (2014) cited as broad references for the analytical procedure"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "EPMA (EMP)",
        "schema:description": "EPMA provides major element concentrations for comparison with LA-ICP-MS oxide-sum normalization results; agreement within <10% verified"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "AMS ver. 1.0 (Mutchler et al. 2008; Analysis Management System, stand-alone software)"
    }
  ],
  "ada:ablationSamplingMode": [
    "Spot (stationary)"
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ablationSpotDurationDefault": -9999,
  "ada:carrierGasFlowRateDefault": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
  "ada:signalCollectionMode": "missing",
  "ada:targetSelectionCriteriaDefault": "missing",
  "ada:totalIntegrationTimePerOutputDataPointDefault": -9999,
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

ex:laQicpmsTAPP-Liu2016 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/normalizationStandardsBasedCorrectionDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ],
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
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/detectionLimitDefault>,
        <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign> ;
    schema1:datePublished "missing" ;
    schema1:description "Paper broadly follows Udry et al. (2012) and Pernet-Fisher et al. (2014) for procedure; two IS approaches used for different mineral phases (oxide-sum for silicates; EMP CaO for phosphate); 90 µm spot used on some olivines to evaluate whether low REE signals result from insufficient sampling volume" ;
    schema1:instrument <https://example.org/instrument/ICPMS>,
        <https://example.org/instrument/Laser-Ablation-System> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Department of Geosciences, Virginia Tech" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "LA-ICP-MS (193 nm excimer laser + ICP-MS; top-level technique)" ] ;
    schema1:name "laQicpms protocol — Liu2016" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Martian meteorite (Tissint) silicates, oxides, and glass: olivine, low-Ca pyroxene, augite, maskelynite, Fe-Ti-Cr oxides, shock melt glass, fusion crust" ],
                <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/sampleFormAnalyticalSubstrateDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "EPMA provides major element concentrations for comparison with LA-ICP-MS oxide-sum normalization results; agreement within <10% verified" ;
                    schema1:name "EPMA (EMP)" ] ;
            schema1:url "https://ada.astromat.org/missing" ],
        [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Udry et al. (2012) and Pernet-Fisher et al. (2014) cited as broad references for the analytical procedure" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:ablationPitDepthRateDefault "missing" ;
    ada:ablationSamplingMode "Spot (stationary)" ;
    ada:ablationSpotDurationDefault -9999 ;
    ada:analysisSequenceDefault "NIST 610 glass standard analyzed before and after every session; unknowns in between" ;
    ada:backgroundCountTimeDefault "50 s (background counted for 50 s before each LA-ICP-MS analysis)" ;
    ada:blankBackgroundCorrectionMethod "50 s background measurement before each analysis; background subtracted (method not explicitly described beyond counting duration)" ;
    ada:calibrationMeasurementFrequency "NIST 610 glass standard analyzed before and after every session" ;
    ada:carrierGasFlowRateDefault "missing" ;
    ada:constantsAndReferenceValuesUsedDefault "missing" ;
    ada:elementalFractionationCorrection "External calibration using NIST 610 glass standard analyzed before and after session; oxide-sum normalization corrects for ablation yield variation; no explicit downhole fractionation correction described" ;
    ada:internalStandardApproach "Normalization to 100 wt% oxide total (for silicates and oxides)" ;
    ada:internalStandardElement "None (oxide sum normalization, 100 wt% total)" ;
    ada:ionCounterDeadTimeDefault -9999 ;
    ada:massBiasCorrectionStrategy "missing" ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:primaryStandardNameDefault "NIST 610 glass standard" ;
    ada:rasterLineSpacingDefault "missing" ;
    ada:sampleIntroduction "missing" ;
    ada:samplingUnit "missing" ;
    ada:signalCollectionMode "missing" ;
    ada:signalIntegrationIntervalMethod "Time-lapse plots of each spot examined; only the plateau region used to quantify trace element abundances" ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:totalIntegrationTimePerOutputDataPointDefault -9999 ;
    ada:uncertaintyLevel "missing" ;
    bios:computationalTool [ schema1:name "AMS ver. 1.0 (Mutchler et al. 2008; Analysis Management System, stand-alone software)" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/detectionLimitDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 3 ;
    schema1:description "Referenced in Table 3 and Table S1; specific values not directly stated in main text; REE in olivines below detection limits at 24–32 µm conditions" ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimitDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/normalizationStandardsBasedCorrectionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "100% oxide total normalization applied per analysis for silicates and oxides; NIST 610 used for external calibration before and after session" ;
    schema1:name "Normalization / Standards-Based Correction" ;
    schema1:valueName "normalizationStandardsBasedCorrectionDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/sampleFormAnalyticalSubstrateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "In situ — polished thin section (Tissint sections: Tata-2-C3, Tata-3-C2, UT1, UT3)" ;
    schema1:name "Sample Form / Analytical Substrate" ;
    schema1:valueName "sampleFormAnalyticalSubstrateDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/laserEnergyDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 150 ;
    schema1:description "150 mJ output energy" ;
    schema1:name "Laser Energy" ;
    schema1:valueName "laserEnergyDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Agilent 7500ce ICP-MS" ] ;
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

<https://example.org/instrument/ICPMS/part/Torch> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Torch" ;
    schema1:name "missing" .

<https://example.org/instrument/Laser-Ablation-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/LaserAblation/laserEnergyDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Laser Ablation System" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "GeoLasPro (193 nm Excimer laser-ablation system; manufacturer not stated by name; GeoLasPro is a Lambda Physik/Coherent product)" ] ;
    schema1:name "example instrumentName" ;
    ada:laserFluenceDefault "7–10 J/m² (stated in paper; units as written; likely a typographic error for J/cm²)" ;
    ada:laserRepetitionRateDefault "5 Hz" ;
    ada:laserSpotGeometryDefault "24 and 32 µm diameter (commonly used for silicates and glass); 90 µm (some olivine analyses to evaluate low REE signal sampling)" ;
    ada:laserType "193 nm Excimer (ArF excimer)" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign> a schema1:PropertyValue ;
    schema1:name "Multi-Run Sequential Analysis Design" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign> ;
    schema1:value "Single spot analysis per location" .


```


### laQicpmsTAPP example Liu2016-2
laQicpmsTAPP instance derived from Liu et al. 2016 (M&PS 51) Tissint martian meteorite Phosphate (merrillite) Spot analysis LA-Q-ICP-MS Virginia Tech.
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
  "@id": "ex:laQicpmsTAPP-Liu2016-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "laQicpms protocol — Liu2016-2",
  "schema:description": "N/A — see silicate column for general notes",
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
            "Martian meteorite (Tissint) phosphate: sodium-merrillite"
          ]
        },
        {
          "@id": "ada:parameter/laQicpmsTAPP/sampleFormAnalyticalSubstrateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleFormAnalyticalSubstrateDefault",
          "schema:name": "Sample Form / Analytical Substrate",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "In situ — polished thin section (same sections as silicate protocol)"
        }
      ]
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Agilent 7500ce ICP-MS",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/ICPMS",
      "schema:hasPart": [
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
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "Laser Ablation System",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/module/LaserAblation/laserEnergyDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "laserEnergyDefault",
          "schema:name": "Laser Energy",
          "ada:dataType": "number",
          "ada:fieldScope": "session",
          "schema:defaultValue": 150,
          "schema:description": "150 mJ output energy"
        }
      ],
      "schema:model": {
        "schema:name": "GeoLasPro 193 nm Excimer laser-ablation system (same as silicate protocol)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "193 nm Excimer (ArF excimer)",
      "ada:laserSpotGeometryDefault": "~24 µm diameter",
      "ada:laserFluenceDefault": "7–10 J/m² (same as silicate protocol)",
      "ada:laserRepetitionRateDefault": "5 Hz",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/Laser-Ablation-System",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:analysisSequenceDefault": "Same as silicate protocol",
  "ada:backgroundCountTimeDefault": "50 s (same as silicate protocol)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign"
        }
      ],
      "schema:name": "Multi-Run Sequential Analysis Design",
      "schema:value": "Single spot analysis per location"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/detectionLimitDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "detectionLimitDefault",
      "schema:name": "Detection Limit",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 3,
      "schema:description": "Referenced in Table 3 and Table S1; specific values not directly stated in main text; merrillite REE at 14–414 ppm range above detection"
    }
  ],
  "ada:internalStandardApproach": "Single element IS: EMP CaO concentration used; LA-ICP-MS 40Ca counts normalized to CaO from EMP analysis at the same spot",
  "ada:internalStandardElement": "40Ca; CaO wt% from EMP at the analysis spot",
  "ada:elementalFractionationCorrection": [
    "External calibration using NIST 610; EMP CaO as IS corrects for ablation yield; no explicit downhole correction described"
  ],
  "ada:signalIntegrationIntervalMethod": "Time-lapse plots examined; only plateau region used (same as silicate protocol)",
  "ada:blankBackgroundCorrectionMethod": "50 s background measurement before each analysis (same as silicate protocol)",
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
            "@id": "ada:parameter/laQicpmsTAPP/normalizationStandardsBasedCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "normalizationStandardsBasedCorrectionDefault",
            "schema:name": "Normalization / Standards-Based Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "No post-acquisition normalization; EMP CaO applied directly as IS; NIST 610 for external calibration"
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
  "ada:primaryStandardNameDefault": "NIST 610 glass standard",
  "ada:calibrationMeasurementFrequency": "NIST 610 analyzed before and after every session (same as silicate protocol)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-ICP-MS (same as silicate protocol)"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Department of Geosciences, Virginia Tech"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Same as silicate protocol"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "EPMA (EMP)",
        "schema:description": "EPMA provides CaO concentration at exact analysis spot, used as internal standard for LA-ICP-MS data reduction (LA-ICP-MS 40Ca counts normalized to EMP CaO)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "AMS ver. 1.0 (Mutchler et al. 2008)"
    }
  ],
  "ada:ablationSamplingMode": [
    "Spot (stationary)"
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ablationSpotDurationDefault": -9999,
  "ada:carrierGasFlowRateDefault": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
  "ada:signalCollectionMode": "missing",
  "ada:targetSelectionCriteriaDefault": "missing",
  "ada:totalIntegrationTimePerOutputDataPointDefault": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:laQicpmsTAPP-Liu2016-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "laQicpms protocol \u2014 Liu2016-2",
  "schema:description": "N/A \u2014 see silicate column for general notes",
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
            "Martian meteorite (Tissint) phosphate: sodium-merrillite"
          ]
        },
        {
          "@id": "ada:parameter/laQicpmsTAPP/sampleFormAnalyticalSubstrateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleFormAnalyticalSubstrateDefault",
          "schema:name": "Sample Form / Analytical Substrate",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "In situ \u2014 polished thin section (same sections as silicate protocol)"
        }
      ]
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Agilent 7500ce ICP-MS",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/ICPMS",
      "schema:hasPart": [
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
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "Laser Ablation System",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/module/LaserAblation/laserEnergyDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "laserEnergyDefault",
          "schema:name": "Laser Energy",
          "ada:dataType": "number",
          "ada:fieldScope": "session",
          "schema:defaultValue": 150,
          "schema:description": "150 mJ output energy"
        }
      ],
      "schema:model": {
        "schema:name": "GeoLasPro 193 nm Excimer laser-ablation system (same as silicate protocol)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "193 nm Excimer (ArF excimer)",
      "ada:laserSpotGeometryDefault": "~24 \u00b5m diameter",
      "ada:laserFluenceDefault": "7\u201310 J/m\u00b2 (same as silicate protocol)",
      "ada:laserRepetitionRateDefault": "5 Hz",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/Laser-Ablation-System",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:analysisSequenceDefault": "Same as silicate protocol",
  "ada:backgroundCountTimeDefault": "50 s (same as silicate protocol)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign"
        }
      ],
      "schema:name": "Multi-Run Sequential Analysis Design",
      "schema:value": "Single spot analysis per location"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/detectionLimitDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "detectionLimitDefault",
      "schema:name": "Detection Limit",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 3,
      "schema:description": "Referenced in Table 3 and Table S1; specific values not directly stated in main text; merrillite REE at 14\u2013414 ppm range above detection"
    }
  ],
  "ada:internalStandardApproach": "Single element IS: EMP CaO concentration used; LA-ICP-MS 40Ca counts normalized to CaO from EMP analysis at the same spot",
  "ada:internalStandardElement": "40Ca; CaO wt% from EMP at the analysis spot",
  "ada:elementalFractionationCorrection": [
    "External calibration using NIST 610; EMP CaO as IS corrects for ablation yield; no explicit downhole correction described"
  ],
  "ada:signalIntegrationIntervalMethod": "Time-lapse plots examined; only plateau region used (same as silicate protocol)",
  "ada:blankBackgroundCorrectionMethod": "50 s background measurement before each analysis (same as silicate protocol)",
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
            "@id": "ada:parameter/laQicpmsTAPP/normalizationStandardsBasedCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "normalizationStandardsBasedCorrectionDefault",
            "schema:name": "Normalization / Standards-Based Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "No post-acquisition normalization; EMP CaO applied directly as IS; NIST 610 for external calibration"
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
  "ada:primaryStandardNameDefault": "NIST 610 glass standard",
  "ada:calibrationMeasurementFrequency": "NIST 610 analyzed before and after every session (same as silicate protocol)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-ICP-MS (same as silicate protocol)"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Department of Geosciences, Virginia Tech"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Same as silicate protocol"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "EPMA (EMP)",
        "schema:description": "EPMA provides CaO concentration at exact analysis spot, used as internal standard for LA-ICP-MS data reduction (LA-ICP-MS 40Ca counts normalized to EMP CaO)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "AMS ver. 1.0 (Mutchler et al. 2008)"
    }
  ],
  "ada:ablationSamplingMode": [
    "Spot (stationary)"
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ablationSpotDurationDefault": -9999,
  "ada:carrierGasFlowRateDefault": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
  "ada:signalCollectionMode": "missing",
  "ada:targetSelectionCriteriaDefault": "missing",
  "ada:totalIntegrationTimePerOutputDataPointDefault": -9999,
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

ex:laQicpmsTAPP-Liu2016-2 a cdi:Activity,
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
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/normalizationStandardsBasedCorrectionDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/detectionLimitDefault>,
        <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign> ;
    schema1:datePublished "missing" ;
    schema1:description "N/A — see silicate column for general notes" ;
    schema1:instrument <https://example.org/instrument/ICPMS>,
        <https://example.org/instrument/Laser-Ablation-System> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Department of Geosciences, Virginia Tech" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "LA-ICP-MS (same as silicate protocol)" ] ;
    schema1:name "laQicpms protocol — Liu2016-2" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Martian meteorite (Tissint) phosphate: sodium-merrillite" ],
                <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/sampleFormAnalyticalSubstrateDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "EPMA provides CaO concentration at exact analysis spot, used as internal standard for LA-ICP-MS data reduction (LA-ICP-MS 40Ca counts normalized to EMP CaO)" ;
                    schema1:name "EPMA (EMP)" ] ;
            schema1:url "https://ada.astromat.org/missing" ],
        [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Same as silicate protocol" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:ablationPitDepthRateDefault "missing" ;
    ada:ablationSamplingMode "Spot (stationary)" ;
    ada:ablationSpotDurationDefault -9999 ;
    ada:analysisSequenceDefault "Same as silicate protocol" ;
    ada:backgroundCountTimeDefault "50 s (same as silicate protocol)" ;
    ada:blankBackgroundCorrectionMethod "50 s background measurement before each analysis (same as silicate protocol)" ;
    ada:calibrationMeasurementFrequency "NIST 610 analyzed before and after every session (same as silicate protocol)" ;
    ada:carrierGasFlowRateDefault "missing" ;
    ada:constantsAndReferenceValuesUsedDefault "missing" ;
    ada:elementalFractionationCorrection "External calibration using NIST 610; EMP CaO as IS corrects for ablation yield; no explicit downhole correction described" ;
    ada:internalStandardApproach "Single element IS: EMP CaO concentration used; LA-ICP-MS 40Ca counts normalized to CaO from EMP analysis at the same spot" ;
    ada:internalStandardElement "40Ca; CaO wt% from EMP at the analysis spot" ;
    ada:ionCounterDeadTimeDefault -9999 ;
    ada:massBiasCorrectionStrategy "missing" ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:primaryStandardNameDefault "NIST 610 glass standard" ;
    ada:rasterLineSpacingDefault "missing" ;
    ada:sampleIntroduction "missing" ;
    ada:samplingUnit "missing" ;
    ada:signalCollectionMode "missing" ;
    ada:signalIntegrationIntervalMethod "Time-lapse plots examined; only plateau region used (same as silicate protocol)" ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:totalIntegrationTimePerOutputDataPointDefault -9999 ;
    ada:uncertaintyLevel "missing" ;
    bios:computationalTool [ schema1:name "AMS ver. 1.0 (Mutchler et al. 2008)" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/detectionLimitDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 3 ;
    schema1:description "Referenced in Table 3 and Table S1; specific values not directly stated in main text; merrillite REE at 14–414 ppm range above detection" ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimitDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/normalizationStandardsBasedCorrectionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "No post-acquisition normalization; EMP CaO applied directly as IS; NIST 610 for external calibration" ;
    schema1:name "Normalization / Standards-Based Correction" ;
    schema1:valueName "normalizationStandardsBasedCorrectionDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/sampleFormAnalyticalSubstrateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "In situ — polished thin section (same sections as silicate protocol)" ;
    schema1:name "Sample Form / Analytical Substrate" ;
    schema1:valueName "sampleFormAnalyticalSubstrateDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/laserEnergyDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 150 ;
    schema1:description "150 mJ output energy" ;
    schema1:name "Laser Energy" ;
    schema1:valueName "laserEnergyDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Agilent 7500ce ICP-MS" ] ;
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

<https://example.org/instrument/ICPMS/part/Torch> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Torch" ;
    schema1:name "missing" .

<https://example.org/instrument/Laser-Ablation-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/LaserAblation/laserEnergyDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Laser Ablation System" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "GeoLasPro 193 nm Excimer laser-ablation system (same as silicate protocol)" ] ;
    schema1:name "example instrumentName" ;
    ada:laserFluenceDefault "7–10 J/m² (same as silicate protocol)" ;
    ada:laserRepetitionRateDefault "5 Hz" ;
    ada:laserSpotGeometryDefault "~24 µm diameter" ;
    ada:laserType "193 nm Excimer (ArF excimer)" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign> a schema1:PropertyValue ;
    schema1:name "Multi-Run Sequential Analysis Design" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign> ;
    schema1:value "Single spot analysis per location" .


```


### laQicpmsTAPP example P6
laQicpmsTAPP instance derived from Wu+etal2023 | Analyte G2 + iCAP TQ ICP-MS/MS | IGGCAS.
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
  "@id": "ex:laQicpmsTAPP-P6",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "laQicpms protocol — P6",
  "schema:description": "laQicpmsTAPP instance derived from Wu+etal2023 | Analyte G2 + iCAP TQ ICP-MS/MS | IGGCAS (publication column of LA-Q-ICP-MS_TAPP_v30.csv).",
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
            "Xenotime, apatite and garnet — accessory and metamorphic minerals for in situ Lu-Hf geochronology"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Megacrysts and single crystals; XN02 megacrysts from the Datas alluvial deposits, SE Brazil",
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
            "@id": "ada:parameter/laQicpmsTAPP/normalizationStandardsBasedCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "normalizationStandardsBasedCorrectionDefault",
            "schema:name": "Normalization / Standards-Based Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Two-step calibration: external correction of mass bias and fractionation against NIST SRM 610, then a matrix-induced correction against matrix-matched XN02 xenotime"
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
            "schema:value": "Acquired and included counts both stated: 'A total of 246 spot analyses were undertaken in 20 analytical sessions over 3 months, 236 of which yielded a weighted-mean age of 515.4 +/- 1.2 Ma'. The rejection rule itself is not stated"
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
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Triple quadrupole (ICP-MS/MS) — operated in both single-quadrupole (SQ) and triple-quadrupole (TQ) modes",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "iCap TQ ICP-MS/MS (Thermo Fisher Scientific, Bremen, Germany)",
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
              "@id": "ada:parameter/laQicpmsTAPP/interfaceConeConfiguration",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/laQicpmsTAPP/interfaceConeConfiguration"
                }
              ],
              "schema:name": "Interface Cone Configuration",
              "schema:value": "High sensitivity sample and skimmer cones"
            },
            {
              "@id": "ada:parameter/laQicpmsTAPP/samplerAndSkimmerConeMaterial",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/laQicpmsTAPP/samplerAndSkimmerConeMaterial"
                }
              ],
              "schema:name": "Sampler and Skimmer Cone Material",
              "schema:value": "N — 'high sensitivity' cones specified, material not stated"
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
          "schema:name": "ICP-MS/MS (triple-quadrupole mode)",
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/laQicpmsTAPP/cellExitDiscriminationVoltageDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "cellExitDiscriminationVoltageDefault",
              "schema:name": "Cell Exit Discrimination Voltage",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": -40.0,
              "schema:description": "CR exit lens -40.00 V (cell bias -4.200 V, CR amplitude 189.3 V, CR entry lens -144.0 V also tabulated)"
            },
            {
              "@id": "ada:parameter/laQicpmsTAPP/reactionGasType",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/laQicpmsTAPP/reactionGasType"
                }
              ],
              "schema:name": "Reaction Gas Type",
              "schema:value": "NH3, high purity (>99.999%), supplied in T4; He (>99.999%, T1) pre-mixed with NH3 before the cell in a test of mixture composition. High-purity NH3 found more effective than the commonly used 1:9 NH3-He mixture"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Collision-Reaction-Cell"
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
              "@id": "ada:parameter/laQicpmsTAPP/coolantGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantGasFlowRateDefault",
              "schema:name": "Coolant (Plasma) Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 15.0,
              "schema:description": "15.00 L min-1 Ar"
            },
            {
              "@id": "ada:parameter/laQicpmsTAPP/auxiliaryGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "auxiliaryGasFlowRateDefault",
              "schema:name": "Auxiliary Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 0.8,
              "schema:description": "0.80 L min-1 Ar"
            },
            {
              "@id": "ada:parameter/laQicpmsTAPP/rfPowerDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "rfPowerDefault",
              "schema:name": "RF Power",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 1350,
              "schema:description": "1350 W"
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
          "@id": "ada:parameter/laQicpmsTAPP/massResolutionSetting",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSetting",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "~300"
        },
        {
          "@id": "ada:parameter/laQicpmsTAPP/detectorConfiguration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laQicpmsTAPP/detectorConfiguration"
            }
          ],
          "schema:name": "Detector Configuration",
          "schema:value": "Single SEM in double mode, counting and analog"
        },
        {
          "@id": "ada:parameter/laQicpmsTAPP/icpTuningDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "icpTuningDefault",
          "schema:name": "ICP Tuning",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Two-stage: first optimised in solution single-quadrupole and no-gas modes to tune for a robust plasma (U/Th = 1.00-1.05) and minimise oxides (ThO/Th < 0.5%); then switched to TQ and NH3 mode, with lenses tuned to maximise sensitivity for Hf reaction products while keeping Lu and Yb reaction rates low"
        }
      ],
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
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/module/LaserAblation/laserPulseDuration",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "laserPulseDuration",
          "schema:name": "Laser Pulse Duration",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:value": "4-5 ns"
        }
      ],
      "schema:model": {
        "schema:name": "Photon Machines Analyte G2 (Teledyne CETAC, Omaha, USA)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "193 nm",
      "schema:name": "HelEx ablation cell",
      "ada:laserFluenceDefault": "4 J cm-2",
      "ada:laserRepetitionRateDefault": "10 Hz",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/Laser-Ablation-System"
    }
  ],
  "ada:carrierGasFlowRateDefault": "He, 900 mL min-1 ablation gas flow",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsTAPP/makeUpGasAndFlowRateDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "makeUpGasAndFlowRateDefault",
      "schema:name": "Make-up Gas and Flow Rate",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 2,
      "schema:description": "N2 enhancement gas, 4.0 mL min-1, added to the carrier gas after the sample chamber to enhance sensitivity; an 80% sensitivity improvement is reported"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/uncertaintyPropagationMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "uncertaintyPropagationMethodDefault",
      "schema:name": "Uncertainty Propagation Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Uncertainty propagation workflow implemented in IsoplotR"
    }
  ],
  "ada:oxideProductionMethodAndThreshold": "ThO/Th < 0.5%, checked during SQ no-gas tuning",
  "ada:signalCollectionMode": "N/A",
  "ada:totalIntegrationTimePerOutputDataPointDefault": "0.659 s",
  "ada:backgroundCountTimeDefault": "N — gas-blank correction applied in Iolite, duration not stated",
  "ada:uncertaintyLevel": "2SE for single-spot ages; uncertainties on weighted-mean ages quoted at 2s",
  "ada:blankBackgroundCorrectionMethod": "Gas-blank-corrected intensities calculated in Iolite v.3.7 from time-resolved intensities",
  "ada:constantsAndReferenceValuesUsedDefault": "NIST SRM 610 recommended values 176Lu/177Hf = 0.1379 +/- 0.0050 and 176Hf/177Hf = 0.282111 +/- 0.000009, as determined by ID-MC-ICP-MS; 176Lu/175Lu = 0.02655; 176Yb/172Yb = 0.5887; 177Hf/178Hf = 0.682; 176Lu half-life ~37.12 Ga",
  "ada:primaryStandardNameDefault": "NIST SRM 610",
  "ada:secondaryReferenceMaterialDefault": [
    "XN02 xenotime as a matrix-matched reference material to correct matrix-induced elemental fractionation of Lu/Hf between SRM 610 and the samples"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-ICP-MS/MS (LA-Q-ICP-MS, triple-quadrupole platform)"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Institute of Geology and Geophysics, Chinese Academy of Sciences (IGGCAS)"
  },
  "ada:samplingUnit": "Laser spot — 246 spot analyses on XN02 alone; spot diameters 50-150 um depending on Lu and Hf contents",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Iolite v.3.7 for gas-blank-corrected intensities, raw ratios and uncertainties; an in-house Microsoft Excel spreadsheet for drift, elemental fractionation and matrix-induced bias; IsoplotR for isochron and weighted-mean ages"
    }
  ],
  "ada:reportedProperties": [
    "176Lu/177Hf and 176Hf/177Hf ratios; Lu-Hf isochron and weighted-mean ages (Ma)"
  ],
  "ada:ablationSamplingMode": [
    "Single hole drilling, two cleaning pulses"
  ],
  "ada:ablationSpotDurationDefault": "25 s",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Lu and Hf (with Yb monitored for interference)",
      "Al",
      "Ca",
      "Y and Zr monitored for inclusions"
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
        "@id": "ada:analyteColumn/laQicpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "boolean",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "uri"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
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
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "@type": [
        "cdi:InstanceVariable"
      ]
    }
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:analysisSequenceDefault": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:internalStandardApproach": "missing",
  "ada:internalStandardElement": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:signalIntegrationIntervalMethod": "missing",
  "ada:targetSelectionCriteriaDefault": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:laQicpmsTAPP-P6",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "laQicpms protocol \u2014 P6",
  "schema:description": "laQicpmsTAPP instance derived from Wu+etal2023 | Analyte G2 + iCAP TQ ICP-MS/MS | IGGCAS (publication column of LA-Q-ICP-MS_TAPP_v30.csv).",
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
            "Xenotime, apatite and garnet \u2014 accessory and metamorphic minerals for in situ Lu-Hf geochronology"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Megacrysts and single crystals; XN02 megacrysts from the Datas alluvial deposits, SE Brazil",
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
            "@id": "ada:parameter/laQicpmsTAPP/normalizationStandardsBasedCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "normalizationStandardsBasedCorrectionDefault",
            "schema:name": "Normalization / Standards-Based Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Two-step calibration: external correction of mass bias and fractionation against NIST SRM 610, then a matrix-induced correction against matrix-matched XN02 xenotime"
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
            "schema:value": "Acquired and included counts both stated: 'A total of 246 spot analyses were undertaken in 20 analytical sessions over 3 months, 236 of which yielded a weighted-mean age of 515.4 +/- 1.2 Ma'. The rejection rule itself is not stated"
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
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Triple quadrupole (ICP-MS/MS) \u2014 operated in both single-quadrupole (SQ) and triple-quadrupole (TQ) modes",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "iCap TQ ICP-MS/MS (Thermo Fisher Scientific, Bremen, Germany)",
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
              "@id": "ada:parameter/laQicpmsTAPP/interfaceConeConfiguration",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/laQicpmsTAPP/interfaceConeConfiguration"
                }
              ],
              "schema:name": "Interface Cone Configuration",
              "schema:value": "High sensitivity sample and skimmer cones"
            },
            {
              "@id": "ada:parameter/laQicpmsTAPP/samplerAndSkimmerConeMaterial",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/laQicpmsTAPP/samplerAndSkimmerConeMaterial"
                }
              ],
              "schema:name": "Sampler and Skimmer Cone Material",
              "schema:value": "N \u2014 'high sensitivity' cones specified, material not stated"
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
          "schema:name": "ICP-MS/MS (triple-quadrupole mode)",
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/laQicpmsTAPP/cellExitDiscriminationVoltageDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "cellExitDiscriminationVoltageDefault",
              "schema:name": "Cell Exit Discrimination Voltage",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": -40.0,
              "schema:description": "CR exit lens -40.00 V (cell bias -4.200 V, CR amplitude 189.3 V, CR entry lens -144.0 V also tabulated)"
            },
            {
              "@id": "ada:parameter/laQicpmsTAPP/reactionGasType",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/laQicpmsTAPP/reactionGasType"
                }
              ],
              "schema:name": "Reaction Gas Type",
              "schema:value": "NH3, high purity (>99.999%), supplied in T4; He (>99.999%, T1) pre-mixed with NH3 before the cell in a test of mixture composition. High-purity NH3 found more effective than the commonly used 1:9 NH3-He mixture"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Collision-Reaction-Cell"
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
              "@id": "ada:parameter/laQicpmsTAPP/coolantGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantGasFlowRateDefault",
              "schema:name": "Coolant (Plasma) Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 15.0,
              "schema:description": "15.00 L min-1 Ar"
            },
            {
              "@id": "ada:parameter/laQicpmsTAPP/auxiliaryGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "auxiliaryGasFlowRateDefault",
              "schema:name": "Auxiliary Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 0.8,
              "schema:description": "0.80 L min-1 Ar"
            },
            {
              "@id": "ada:parameter/laQicpmsTAPP/rfPowerDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "rfPowerDefault",
              "schema:name": "RF Power",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 1350,
              "schema:description": "1350 W"
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
          "@id": "ada:parameter/laQicpmsTAPP/massResolutionSetting",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSetting",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "~300"
        },
        {
          "@id": "ada:parameter/laQicpmsTAPP/detectorConfiguration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laQicpmsTAPP/detectorConfiguration"
            }
          ],
          "schema:name": "Detector Configuration",
          "schema:value": "Single SEM in double mode, counting and analog"
        },
        {
          "@id": "ada:parameter/laQicpmsTAPP/icpTuningDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "icpTuningDefault",
          "schema:name": "ICP Tuning",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Two-stage: first optimised in solution single-quadrupole and no-gas modes to tune for a robust plasma (U/Th = 1.00-1.05) and minimise oxides (ThO/Th < 0.5%); then switched to TQ and NH3 mode, with lenses tuned to maximise sensitivity for Hf reaction products while keeping Lu and Yb reaction rates low"
        }
      ],
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
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/module/LaserAblation/laserPulseDuration",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "laserPulseDuration",
          "schema:name": "Laser Pulse Duration",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:value": "4-5 ns"
        }
      ],
      "schema:model": {
        "schema:name": "Photon Machines Analyte G2 (Teledyne CETAC, Omaha, USA)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "193 nm",
      "schema:name": "HelEx ablation cell",
      "ada:laserFluenceDefault": "4 J cm-2",
      "ada:laserRepetitionRateDefault": "10 Hz",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/Laser-Ablation-System"
    }
  ],
  "ada:carrierGasFlowRateDefault": "He, 900 mL min-1 ablation gas flow",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsTAPP/makeUpGasAndFlowRateDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "makeUpGasAndFlowRateDefault",
      "schema:name": "Make-up Gas and Flow Rate",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 2,
      "schema:description": "N2 enhancement gas, 4.0 mL min-1, added to the carrier gas after the sample chamber to enhance sensitivity; an 80% sensitivity improvement is reported"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/uncertaintyPropagationMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "uncertaintyPropagationMethodDefault",
      "schema:name": "Uncertainty Propagation Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Uncertainty propagation workflow implemented in IsoplotR"
    }
  ],
  "ada:oxideProductionMethodAndThreshold": "ThO/Th < 0.5%, checked during SQ no-gas tuning",
  "ada:signalCollectionMode": "N/A",
  "ada:totalIntegrationTimePerOutputDataPointDefault": "0.659 s",
  "ada:backgroundCountTimeDefault": "N \u2014 gas-blank correction applied in Iolite, duration not stated",
  "ada:uncertaintyLevel": "2SE for single-spot ages; uncertainties on weighted-mean ages quoted at 2s",
  "ada:blankBackgroundCorrectionMethod": "Gas-blank-corrected intensities calculated in Iolite v.3.7 from time-resolved intensities",
  "ada:constantsAndReferenceValuesUsedDefault": "NIST SRM 610 recommended values 176Lu/177Hf = 0.1379 +/- 0.0050 and 176Hf/177Hf = 0.282111 +/- 0.000009, as determined by ID-MC-ICP-MS; 176Lu/175Lu = 0.02655; 176Yb/172Yb = 0.5887; 177Hf/178Hf = 0.682; 176Lu half-life ~37.12 Ga",
  "ada:primaryStandardNameDefault": "NIST SRM 610",
  "ada:secondaryReferenceMaterialDefault": [
    "XN02 xenotime as a matrix-matched reference material to correct matrix-induced elemental fractionation of Lu/Hf between SRM 610 and the samples"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-ICP-MS/MS (LA-Q-ICP-MS, triple-quadrupole platform)"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Institute of Geology and Geophysics, Chinese Academy of Sciences (IGGCAS)"
  },
  "ada:samplingUnit": "Laser spot \u2014 246 spot analyses on XN02 alone; spot diameters 50-150 um depending on Lu and Hf contents",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Iolite v.3.7 for gas-blank-corrected intensities, raw ratios and uncertainties; an in-house Microsoft Excel spreadsheet for drift, elemental fractionation and matrix-induced bias; IsoplotR for isochron and weighted-mean ages"
    }
  ],
  "ada:reportedProperties": [
    "176Lu/177Hf and 176Hf/177Hf ratios; Lu-Hf isochron and weighted-mean ages (Ma)"
  ],
  "ada:ablationSamplingMode": [
    "Single hole drilling, two cleaning pulses"
  ],
  "ada:ablationSpotDurationDefault": "25 s",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Lu and Hf (with Yb monitored for interference)",
      "Al",
      "Ca",
      "Y and Zr monitored for inclusions"
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
        "@id": "ada:analyteColumn/laQicpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "boolean",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "uri"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
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
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "@type": [
        "cdi:InstanceVariable"
      ]
    }
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:analysisSequenceDefault": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:internalStandardApproach": "missing",
  "ada:internalStandardElement": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:signalIntegrationIntervalMethod": "missing",
  "ada:targetSelectionCriteriaDefault": "missing",
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

ex:laQicpmsTAPP-P6 a cdi:Activity,
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
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/normalizationStandardsBasedCorrectionDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Megacrysts and single crystals; XN02 megacrysts from the Datas alluvial deposits, SE Brazil" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/makeUpGasAndFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/uncertaintyPropagationMethodDefault> ;
    schema1:datePublished "missing" ;
    schema1:description "laQicpmsTAPP instance derived from Wu+etal2023 | Analyte G2 + iCAP TQ ICP-MS/MS | IGGCAS (publication column of LA-Q-ICP-MS_TAPP_v30.csv)." ;
    schema1:instrument <https://example.org/instrument/ICPMS>,
        <https://example.org/instrument/Laser-Ablation-System> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Institute of Geology and Geophysics, Chinese Academy of Sciences (IGGCAS)" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "LA-ICP-MS/MS (LA-Q-ICP-MS, triple-quadrupole platform)" ] ;
    schema1:name "laQicpms protocol — P6" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Xenotime, apatite and garnet — accessory and metamorphic minerals for in situ Lu-Hf geochronology" ] ] ;
    schema1:variableMeasured [ a cdi:InstanceVariable ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:ablationPitDepthRateDefault "missing" ;
    ada:ablationSamplingMode "Single hole drilling, two cleaning pulses" ;
    ada:ablationSpotDurationDefault "25 s" ;
    ada:analysisSequenceDefault "missing" ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/isobaricInterferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/limitOfQuantificationMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/monitoredMasses>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ;
            ada:defaultAnalytes "Al",
                "Ca",
                "Lu and Hf (with Yb monitored for interference)",
                "Y and Zr monitored for inclusions" ] ;
    ada:backgroundCountTimeDefault "N — gas-blank correction applied in Iolite, duration not stated" ;
    ada:blankBackgroundCorrectionMethod "Gas-blank-corrected intensities calculated in Iolite v.3.7 from time-resolved intensities" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:carrierGasFlowRateDefault "He, 900 mL min-1 ablation gas flow" ;
    ada:constantsAndReferenceValuesUsedDefault "NIST SRM 610 recommended values 176Lu/177Hf = 0.1379 +/- 0.0050 and 176Hf/177Hf = 0.282111 +/- 0.000009, as determined by ID-MC-ICP-MS; 176Lu/175Lu = 0.02655; 176Yb/172Yb = 0.5887; 177Hf/178Hf = 0.682; 176Lu half-life ~37.12 Ga" ;
    ada:internalStandardApproach "missing" ;
    ada:internalStandardElement "missing" ;
    ada:ionCounterDeadTimeDefault -9999 ;
    ada:massBiasCorrectionStrategy "missing" ;
    ada:oxideProductionMethodAndThreshold "ThO/Th < 0.5%, checked during SQ no-gas tuning" ;
    ada:primaryStandardNameDefault "NIST SRM 610" ;
    ada:rasterLineSpacingDefault "missing" ;
    ada:reportedProperties "176Lu/177Hf and 176Hf/177Hf ratios; Lu-Hf isochron and weighted-mean ages (Ma)" ;
    ada:sampleIntroduction "missing" ;
    ada:samplingUnit "Laser spot — 246 spot analyses on XN02 alone; spot diameters 50-150 um depending on Lu and Hf contents" ;
    ada:secondaryReferenceMaterialDefault "XN02 xenotime as a matrix-matched reference material to correct matrix-induced elemental fractionation of Lu/Hf between SRM 610 and the samples" ;
    ada:signalCollectionMode "N/A" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:totalIntegrationTimePerOutputDataPointDefault "0.659 s" ;
    ada:uncertaintyLevel "2SE for single-spot ages; uncertainties on weighted-mean ages quoted at 2s" ;
    bios:computationalTool [ schema1:name "Iolite v.3.7 for gas-blank-corrected intensities, raw ratios and uncertainties; an in-house Microsoft Excel spreadsheet for drift, elemental fractionation and matrix-induced bias; IsoplotR for isochron and weighted-mean ages" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/isobaricInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Isobaric Interference Corrections Applied" ;
    schema1:valueName "isobaricInterferenceCorrectionsApplied" ;
    ada:dataType "boolean" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "uri" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/monitoredMasses> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Monitored Masses" ;
    schema1:valueName "monitoredMasses" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/auxiliaryGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 8e-01 ;
    schema1:description "0.80 L min-1 Ar" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:valueName "auxiliaryGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/cellExitDiscriminationVoltageDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue -4e+01 ;
    schema1:description "CR exit lens -40.00 V (cell bias -4.200 V, CR amplitude 189.3 V, CR entry lens -144.0 V also tabulated)" ;
    schema1:name "Cell Exit Discrimination Voltage" ;
    schema1:valueName "cellExitDiscriminationVoltageDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/coolantGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1.5e+01 ;
    schema1:description "15.00 L min-1 Ar" ;
    schema1:name "Coolant (Plasma) Gas Flow Rate" ;
    schema1:valueName "coolantGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/icpTuningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Two-stage: first optimised in solution single-quadrupole and no-gas modes to tune for a robust plasma (U/Th = 1.00-1.05) and minimise oxides (ThO/Th < 0.5%); then switched to TQ and NH3 mode, with lenses tuned to maximise sensitivity for Hf reaction products while keeping Lu and Yb reaction rates low" ;
    schema1:name "ICP Tuning" ;
    schema1:valueName "icpTuningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/makeUpGasAndFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 2 ;
    schema1:description "N2 enhancement gas, 4.0 mL min-1, added to the carrier gas after the sample chamber to enhance sensitivity; an 80% sensitivity improvement is reported" ;
    schema1:name "Make-up Gas and Flow Rate" ;
    schema1:valueName "makeUpGasAndFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/massResolutionSetting> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "~300" ;
    schema1:name "Mass Resolution Setting" ;
    schema1:valueName "massResolutionSetting" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/normalizationStandardsBasedCorrectionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Two-step calibration: external correction of mass bias and fractionation against NIST SRM 610, then a matrix-induced correction against matrix-matched XN02 xenotime" ;
    schema1:name "Normalization / Standards-Based Correction" ;
    schema1:valueName "normalizationStandardsBasedCorrectionDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/rfPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1350 ;
    schema1:description "1350 W" ;
    schema1:name "RF Power" ;
    schema1:valueName "rfPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/uncertaintyPropagationMethodDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Uncertainty propagation workflow implemented in IsoplotR" ;
    schema1:name "Uncertainty Propagation Method" ;
    schema1:valueName "uncertaintyPropagationMethodDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/Aggregation/analysisInclusionAndRejectionCriteriaDefault> a schema1:PropertyValueSpecification ;
    schema1:name "Analysis Inclusion and Rejection Criteria" ;
    schema1:value "Acquired and included counts both stated: 'A total of 246 spot analyses were undertaken in 20 analytical sessions over 3 months, 236 of which yielded a weighted-mean age of 515.4 +/- 1.2 Ma'. The rejection rule itself is not stated" ;
    schema1:valueName "analysisInclusionAndRejectionCriteriaDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/laserPulseDuration> a schema1:PropertyValueSpecification ;
    schema1:name "Laser Pulse Duration" ;
    schema1:value "4-5 ns" ;
    schema1:valueName "laserPulseDuration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/detectorConfiguration>,
        <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/icpTuningDefault>,
        <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/massResolutionSetting> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Triple quadrupole (ICP-MS/MS) — operated in both single-quadrupole (SQ) and triple-quadrupole (TQ) modes" ;
    schema1:hasPart <https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell>,
        <https://example.org/instrument/ICPMS/part/ICP-Source>,
        <https://example.org/instrument/ICPMS/part/Interface-Cone>,
        <https://example.org/instrument/ICPMS/part/Torch> ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "iCap TQ ICP-MS/MS (Thermo Fisher Scientific, Bremen, Germany)" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/cellExitDiscriminationVoltageDefault>,
        <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/reactionGasType> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "ICP-MS/MS (triple-quadrupole mode)" .

<https://example.org/instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/auxiliaryGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/coolantGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/rfPowerDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<https://example.org/instrument/ICPMS/part/Interface-Cone> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/interfaceConeConfiguration>,
        <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/samplerAndSkimmerConeMaterial> ;
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
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/LaserAblation/laserPulseDuration> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Laser Ablation System" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Photon Machines Analyte G2 (Teledyne CETAC, Omaha, USA)" ] ;
    schema1:name "HelEx ablation cell" ;
    ada:laserFluenceDefault "4 J cm-2" ;
    ada:laserRepetitionRateDefault "10 Hz" ;
    ada:laserType "193 nm" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/detectorConfiguration> a schema1:PropertyValue ;
    schema1:name "Detector Configuration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/detectorConfiguration> ;
    schema1:value "Single SEM in double mode, counting and analog" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/interfaceConeConfiguration> a schema1:PropertyValue ;
    schema1:name "Interface Cone Configuration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/interfaceConeConfiguration> ;
    schema1:value "High sensitivity sample and skimmer cones" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/reactionGasType> a schema1:PropertyValue ;
    schema1:name "Reaction Gas Type" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/reactionGasType> ;
    schema1:value "NH3, high purity (>99.999%), supplied in T4; He (>99.999%, T1) pre-mixed with NH3 before the cell in a test of mixture composition. High-purity NH3 found more effective than the commonly used 1:9 NH3-He mixture" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/samplerAndSkimmerConeMaterial> a schema1:PropertyValue ;
    schema1:name "Sampler and Skimmer Cone Material" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/samplerAndSkimmerConeMaterial> ;
    schema1:value "N — 'high sensitivity' cones specified, material not stated" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: LA-Q-ICP-MS Technique-Aligned Procedure Profile (laQicpmsTAPP)
description: Laser-ablation quadrupole ICP-MS extension of the base TAPP definition,
  generated from tapp/Current TAPPs/LA-Q-ICP-MS_TAPP_v30.csv via the path-driven pipeline
  (bootstrap_schemapaths.py + build_pathdriven.py).
allOf:
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/targetSelection/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/calibrationFactor/schema.yaml#/$defs/ProcedureIdentification
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
                              - Silicate glass
                              - Feldspar
                              - Pyroxene
                              - Olivine
                              - Oxide
                              - Sulfide
                              - Carbonate
                              - Phosphate
                              - Native metal
                              - Iron meteorite
                              - Fluid inclusion
                              - Melt inclusion
                              - Whole rock
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
                    title: Sample Form / Analytical Substrate
                    description: Physical form of the material as it enters the ablation
                      cell. Editable to accommodate legitimate variations (e.g., thin
                      section vs. mount) that do not alter the analytical procedure.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/laQicpmsTAPP/sampleFormAnalyticalSubstrateDefault
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
                            const: ada:parameter/laQicpmsTAPP/fusionFluxAndDilutionRatioDefault
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
                            const: ada:parameter/laQicpmsTAPP/fusionFluxAndDilutionRatioDefault
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
                          const: ada:parameter/laQicpmsTAPP/guardElectrode
                        '@type':
                          const:
                          - schema:PropertyValue
                        schema:propertyID:
                          const:
                          - '@id': ada:parameter/laQicpmsTAPP/guardElectrode
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
                            const: ada:parameter/laQicpmsTAPP/guardElectrode
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/laQicpmsTAPP/guardElectrode
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
                            const: ada:parameter/laQicpmsTAPP/signalSmoothingDefault
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
                            const: ada:parameter/laQicpmsTAPP/spikeOutlierFilteringApproachDefault
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
                      - title: Pulse/Analog Detector Nonlinearity Correction
                        description: Whether a correction was applied for nonlinear
                          response at the transition between pulse-counting and analog
                          detector modes.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/laQicpmsTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault
                          '@type':
                            const:
                            - schema:PropertyValueSpecification
                          schema:valueName:
                            const: pulseAnalogDetectorNonlinearityCorrectionDefault
                          schema:name:
                            const: Pulse/Analog Detector Nonlinearity Correction
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
                      - title: Isotope Dilution Data Reduction Method
                        description: Mass balance approach used to calculate sample
                          mass fractions from spike-sample isotope ratio measurements
                          in isotope dilution (ID) analysis. Record 'None' if isotope
                          dilution is not used.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/laQicpmsTAPP/isotopeDilutionDataReductionMethod
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/laQicpmsTAPP/isotopeDilutionDataReductionMethod
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
                            const: ada:parameter/laQicpmsTAPP/normalizationStandardsBasedCorrectionDefault
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
                    allOf:
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
                            const: ada:parameter/laQicpmsTAPP/signalSmoothingDefault
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
                            const: ada:parameter/laQicpmsTAPP/spikeOutlierFilteringApproachDefault
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
                        title: Pulse/Analog Detector Nonlinearity Correction
                        description: Whether a correction was applied for nonlinear
                          response at the transition between pulse-counting and analog
                          detector modes.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/laQicpmsTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault
                          '@type':
                            const:
                            - schema:PropertyValueSpecification
                          schema:valueName:
                            const: pulseAnalogDetectorNonlinearityCorrectionDefault
                          schema:name:
                            const: Pulse/Analog Detector Nonlinearity Correction
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
                        title: Isotope Dilution Data Reduction Method
                        description: Mass balance approach used to calculate sample
                          mass fractions from spike-sample isotope ratio measurements
                          in isotope dilution (ID) analysis. Record 'None' if isotope
                          dilution is not used.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/laQicpmsTAPP/isotopeDilutionDataReductionMethod
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/laQicpmsTAPP/isotopeDilutionDataReductionMethod
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
                            const: ada:parameter/laQicpmsTAPP/normalizationStandardsBasedCorrectionDefault
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
                  const: Data acquisition
              required:
              - schema:name
          - contains:
              properties:
                schema:name:
                  const: Data reduction
              required:
              - schema:name
    schema:additionalProperty:
      type: array
      items:
        anyOf:
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/targetSelection/schema.yaml#/$defs/Param_Procedure_preAnalysisImagingAndScreening
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Procedure_transectRateMappingRateOrStepSize
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
              const: ada:parameter/laQicpmsTAPP/makeUpGasAndFlowRateDefault
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
        - title: Instrument Warm-up / Session Duration Limit
          description: Minimum warm-up time required after plasma ignition before
            analyses begin, and any maximum session duration enforced to maintain
            stable operating conditions. These constraints are part of the procedure
            and cannot be varied by the analyst.
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsTAPP/instrumentWarmUpSessionDurationLimit
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laQicpmsTAPP/instrumentWarmUpSessionDurationLimit
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
              const: ada:parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign
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
              const: ada:parameter/laQicpmsTAPP/uncertaintyPropagationMethodDefault
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
        - title: Matrix Offset Correction (LIEF)
          description: Whether an empirical correction was applied to account for
            systematic differences in laser-induced elemental fractionation (LIEF)
            patterns between the external calibration standard and the sample matrix.
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsTAPP/matrixOffsetCorrection
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laQicpmsTAPP/matrixOffsetCorrection
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
        - title: Detection Limit
          description: "Session detection limit, one per reported concentration variable
            (one per analyte, these being the same set), expressed in \xB5g g\u207B\xB9,
            ng g\u207B\xB9, or wt% as appropriate. Mandatory at analysis level to
            demonstrate the reliability of reported near-detection-limit concentrations.
            The calculation method is captured separately in Detection Limit Method."
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsTAPP/detectionLimitDefault
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
      allOf:
      - contains:
          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/targetSelection/schema.yaml#/$defs/Param_Procedure_preAnalysisImagingAndScreening
        minContains: 0
        maxContains: 1
      - contains:
          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Procedure_transectRateMappingRateOrStepSize
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
              const: ada:parameter/laQicpmsTAPP/makeUpGasAndFlowRateDefault
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
          title: Instrument Warm-up / Session Duration Limit
          description: Minimum warm-up time required after plasma ignition before
            analyses begin, and any maximum session duration enforced to maintain
            stable operating conditions. These constraints are part of the procedure
            and cannot be varied by the analyst.
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsTAPP/instrumentWarmUpSessionDurationLimit
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laQicpmsTAPP/instrumentWarmUpSessionDurationLimit
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
              const: ada:parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laQicpmsTAPP/multiRunSequentialAnalysisDesign
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
              const: ada:parameter/laQicpmsTAPP/uncertaintyPropagationMethodDefault
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
      - contains:
          title: Matrix Offset Correction (LIEF)
          description: Whether an empirical correction was applied to account for
            systematic differences in laser-induced elemental fractionation (LIEF)
            patterns between the external calibration standard and the sample matrix.
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsTAPP/matrixOffsetCorrection
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laQicpmsTAPP/matrixOffsetCorrection
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
          title: Detection Limit
          description: "Session detection limit, one per reported concentration variable
            (one per analyte, these being the same set), expressed in \xB5g g\u207B\xB9,
            ng g\u207B\xB9, or wt% as appropriate. Mandatory at analysis level to
            demonstrate the reliability of reported near-detection-limit concentrations.
            The calculation method is captured separately in Detection Limit Method."
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsTAPP/detectionLimitDefault
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
                        const: ada:parameter/laQicpmsTAPP/instrumentSerialNumberOrLabIdentifierDefault
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
                      design.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/laQicpmsTAPP/massResolutionSetting
                      '@type':
                        const:
                        - schema:PropertyValueSpecification
                      schema:valueName:
                        const: massResolutionSetting
                      schema:name:
                        const: Mass Resolution Setting
                      ada:dataType:
                        const: string
                      ada:fieldScope:
                        const: session
                      schema:readonlyValue:
                        const: true
                      ada:tier:
                        const: R
                    required:
                    - '@id'
                    - '@type'
                    - schema:valueName
                    - schema:name
                    - ada:dataType
                    - ada:fieldScope
                    readOnly: true
                  - title: Detector Configuration
                    description: Type(s) of detector(s) installed in the mass spectrometer.
                      For single-collector instruments, note whether dual pulse-counting/analog
                      mode is used. For multi-collector instruments, describe the
                      Faraday/multiplier cup layout.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/laQicpmsTAPP/detectorConfiguration
                      '@type':
                        const:
                        - schema:PropertyValue
                      schema:propertyID:
                        const:
                        - '@id': ada:parameter/laQicpmsTAPP/detectorConfiguration
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
                  - title: ICP Tuning
                    description: Description of the approach used to optimise ICP
                      plasma conditions prior to analysis, including the reference
                      material used for tuning and the acceptance criteria (e.g.,
                      oxide production threshold, sensitivity targets, mass calibration).
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/laQicpmsTAPP/icpTuningDefault
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
                        const: ada:parameter/laQicpmsTAPP/doublyChargedSpeciesMonitorDefault
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
                        const: ada:parameter/laQicpmsTAPP/doublyChargedSpeciesProductionDefault
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
                        const: ada:parameter/laQicpmsTAPP/memoryEffectMitigationDefault
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
                        const: ada:parameter/laQicpmsTAPP/instrumentSerialNumberOrLabIdentifierDefault
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
                      design.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/laQicpmsTAPP/massResolutionSetting
                      '@type':
                        const:
                        - schema:PropertyValueSpecification
                      schema:valueName:
                        const: massResolutionSetting
                      schema:name:
                        const: Mass Resolution Setting
                      ada:dataType:
                        const: string
                      ada:fieldScope:
                        const: session
                      schema:readonlyValue:
                        const: true
                      ada:tier:
                        const: R
                    required:
                    - '@id'
                    - '@type'
                    - schema:valueName
                    - schema:name
                    - ada:dataType
                    - ada:fieldScope
                    readOnly: true
                  minContains: 0
                  maxContains: 1
                - contains:
                    title: Detector Configuration
                    description: Type(s) of detector(s) installed in the mass spectrometer.
                      For single-collector instruments, note whether dual pulse-counting/analog
                      mode is used. For multi-collector instruments, describe the
                      Faraday/multiplier cup layout.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/laQicpmsTAPP/detectorConfiguration
                      '@type':
                        const:
                        - schema:PropertyValue
                      schema:propertyID:
                        const:
                        - '@id': ada:parameter/laQicpmsTAPP/detectorConfiguration
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
                    title: ICP Tuning
                    description: Description of the approach used to optimise ICP
                      plasma conditions prior to analysis, including the reference
                      material used for tuning and the acceptance criteria (e.g.,
                      oxide production threshold, sensitivity targets, mass calibration).
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/laQicpmsTAPP/icpTuningDefault
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
                        const: ada:parameter/laQicpmsTAPP/doublyChargedSpeciesMonitorDefault
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
                        const: ada:parameter/laQicpmsTAPP/doublyChargedSpeciesProductionDefault
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
                        const: ada:parameter/laQicpmsTAPP/memoryEffectMitigationDefault
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
                                  const: ada:parameter/laQicpmsTAPP/interfaceConeConfiguration
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laQicpmsTAPP/interfaceConeConfiguration
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
                                  const: ada:parameter/laQicpmsTAPP/samplerAndSkimmerConeMaterial
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laQicpmsTAPP/samplerAndSkimmerConeMaterial
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
                                  const: ada:parameter/laQicpmsTAPP/interfaceConeConfiguration
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laQicpmsTAPP/interfaceConeConfiguration
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
                                  const: ada:parameter/laQicpmsTAPP/samplerAndSkimmerConeMaterial
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laQicpmsTAPP/samplerAndSkimmerConeMaterial
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
                                const: ada:parameter/laQicpmsTAPP/torchDepthDefault
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
                                  const: ada:parameter/laQicpmsTAPP/torchDepthDefault
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
                            which lack collision/reaction cells.
                          anyOf:
                          - type: string
                            enum:
                            - Not installed
                            - STD (standard mode, no gas)
                            - KED (kinetic energy discrimination, He gas)
                            - DRC (dynamic reaction cell, reactive gas)
                            - KED+DRC
                            - ICP-MS/MS (triple-quadrupole mode)
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
                              - KED+DRC
                              - ICP-MS/MS (triple-quadrupole mode)
                              - N/A
                              - None
                              - missing
                              readOnly: true
                        schema:additionalProperty:
                          type: array
                          items:
                            anyOf:
                            - title: Collision Gas Type
                              description: Type of collision gas introduced into the
                                collision/reaction cell in KED mode. Helium (He) is
                                the standard collision gas for kinetic energy discrimination
                                due to its low mass and chemical inertness. Record
                                'None' if the CRC is in STD mode or not installed.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laQicpmsTAPP/collisionGasType
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laQicpmsTAPP/collisionGasType
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
                              description: Flow rate of the collision gas (typically
                                He) introduced into the collision/reaction cell, in
                                mL/min. Controls the degree of ion thermalization
                                and KED efficiency. Record 'None' if the CRC is in
                                STD mode.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laQicpmsTAPP/collisionGasFlowRateDefault
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
                              description: Bias voltage applied at the collision/reaction
                                cell exit to discriminate between analyte ions and
                                low-energy polyatomic interferences in KED mode, in
                                volts (V). A negative bias preferentially retards
                                slow polyatomic ions while transmitting faster analyte
                                ions. Record 'None' if the CRC is in STD mode.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laQicpmsTAPP/cellExitDiscriminationVoltageDefault
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
                              description: "Type of reactive gas introduced into the
                                dynamic reaction cell (DRC) for interference removal
                                through ion-molecule reactions. Common reaction gases
                                include NH\u2083 (e.g., for Fe, Ca, K isotopes) and
                                O\u2082 (e.g., for As, Ge). Record 'None' if DRC mode
                                is not used."
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laQicpmsTAPP/reactionGasType
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laQicpmsTAPP/reactionGasType
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
                              description: Flow rate of the reactive gas introduced
                                into the dynamic reaction cell (DRC), in mL/min.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laQicpmsTAPP/reactionGasFlowRateDefault
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
                              description: Type of collision gas introduced into the
                                collision/reaction cell in KED mode. Helium (He) is
                                the standard collision gas for kinetic energy discrimination
                                due to its low mass and chemical inertness. Record
                                'None' if the CRC is in STD mode or not installed.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laQicpmsTAPP/collisionGasType
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laQicpmsTAPP/collisionGasType
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
                              description: Flow rate of the collision gas (typically
                                He) introduced into the collision/reaction cell, in
                                mL/min. Controls the degree of ion thermalization
                                and KED efficiency. Record 'None' if the CRC is in
                                STD mode.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laQicpmsTAPP/collisionGasFlowRateDefault
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
                              description: Bias voltage applied at the collision/reaction
                                cell exit to discriminate between analyte ions and
                                low-energy polyatomic interferences in KED mode, in
                                volts (V). A negative bias preferentially retards
                                slow polyatomic ions while transmitting faster analyte
                                ions. Record 'None' if the CRC is in STD mode.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laQicpmsTAPP/cellExitDiscriminationVoltageDefault
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
                              description: "Type of reactive gas introduced into the
                                dynamic reaction cell (DRC) for interference removal
                                through ion-molecule reactions. Common reaction gases
                                include NH\u2083 (e.g., for Fe, Ca, K isotopes) and
                                O\u2082 (e.g., for As, Ge). Record 'None' if DRC mode
                                is not used."
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laQicpmsTAPP/reactionGasType
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laQicpmsTAPP/reactionGasType
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
                              description: Flow rate of the reactive gas introduced
                                into the dynamic reaction cell (DRC), in mL/min.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laQicpmsTAPP/reactionGasFlowRateDefault
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
                            - title: Coolant (Plasma) Gas Flow Rate
                              description: Flow rate of the outer (coolant/plasma)
                                argon gas stream that sustains the ICP plasma, in
                                L/min. Determines plasma volume and stability. Set
                                during initial plasma optimisation and confirmed at
                                each session start.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laQicpmsTAPP/coolantGasFlowRateDefault
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
                                argon gas stream that positions the plasma relative
                                to the load coil, in L/min. Affects ion extraction
                                efficiency and oxide production rates. Distinct from
                                the carrier gas (which transports ablation aerosol)
                                and the coolant (plasma) gas.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laQicpmsTAPP/auxiliaryGasFlowRateDefault
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
                                  const: ada:parameter/laQicpmsTAPP/rfPowerDefault
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
                                  const: ada:parameter/laQicpmsTAPP/plasmaThermalMode
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laQicpmsTAPP/plasmaThermalMode
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
                              title: Coolant (Plasma) Gas Flow Rate
                              description: Flow rate of the outer (coolant/plasma)
                                argon gas stream that sustains the ICP plasma, in
                                L/min. Determines plasma volume and stability. Set
                                during initial plasma optimisation and confirmed at
                                each session start.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laQicpmsTAPP/coolantGasFlowRateDefault
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
                                argon gas stream that positions the plasma relative
                                to the load coil, in L/min. Affects ion extraction
                                efficiency and oxide production rates. Distinct from
                                the carrier gas (which transports ablation aerosol)
                                and the coolant (plasma) gas.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laQicpmsTAPP/auxiliaryGasFlowRateDefault
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
                                  const: ada:parameter/laQicpmsTAPP/rfPowerDefault
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
                                  const: ada:parameter/laQicpmsTAPP/plasmaThermalMode
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laQicpmsTAPP/plasmaThermalMode
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
                          const: ICP Source
                        schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                    required:
                    - schema:additionalType
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
                  - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Procedure_laserEnergy
                  - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Procedure_laserBeamEnergyProfile
                  - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Procedure_laserPulseDuration
                allOf:
                - contains:
                    $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Procedure_laserEnergy
                  minContains: 0
                  maxContains: 1
                - contains:
                    $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Procedure_laserBeamEnergyProfile
                  minContains: 0
                  maxContains: 1
                - contains:
                    $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Procedure_laserPulseDuration
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
      - contains:
          properties:
            schema:additionalType:
              contains:
                const: Laser Ablation System
              schema:inDefinedTermSet: ada:vocab/instrumentType
          required:
          - schema:additionalType
    ada:sampleIntroduction:
      description: "Configuration by which the ablated aerosol is delivered to the
        plasma, including tubing, any signal-homogenising device, and any co-aspirated
        solution introduced alongside the aerosol \u2014 for example a Tl solution
        used for instrumental mass bias correction, or an isotopic spike used for
        isotope dilution. Distinct from the carrier and make-up gas fields, which
        record gas identity and flow rather than what else enters the plasma."
      type: string
      readOnly: true
    ada:carrierGasFlowRateDefault:
      description: "Gas used to transport ablated aerosol from the ablation cell to
        the ICP-MS torch, with the procedure-registered target flow rate(s). Helium
        is standard for most UV laser systems due to superior aerosol transport. Flow
        rates are procedure targets; actual session values may be adjusted within
        \xB110% during tuning."
      type: string
    ada:oxideProductionMethodAndThreshold:
      description: "Method used to quantify plasma oxide production and the acceptance
        threshold applied before commencing analysis. Record both the monitored mass
        ratio(s) and the maximum allowed threshold(s). Measured values are recorded
        in Oxide Production. The ThO\u207A/Th\u207A ratio (mass 248/232) is most widely
        used, but UO\u207A/U\u207A (mass 254/238) or CeO\u207A/Ce\u207A (mass 156/140)
        may also be used."
      type: string
      readOnly: true
    ada:analysisSequenceDefault:
      description: Repeating order of primary calibration standard(s), quality control
        standard(s), and unknown analyses within a measurement session. Editable to
        allow minor adjustments while maintaining the bracketing strategy defined
        in the procedure.
      type: string
    ada:analyteTemplate:
      type: object
      properties:
        ada:analyteColumns:
          type: array
          items:
            anyOf:
            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/AnalyteIdentifierColumn
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
                  const: ada:analyteColumn/laQicpmsTAPP/monitoredMasses
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
            - title: Dwell Time per Mass
              description: 'Count time (dwell time) per mass position for each measured
                isotope in milliseconds. Longer dwell times improve counting statistics
                and lower detection limits but reduce the number of isotopes measurable
                within a given scan cycle time. For mapping, scan cycle time directly
                determines spatial resolution at a given scan speed: shorter cycle
                time = finer spatial resolution.'
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/laQicpmsTAPP/dwellTimePerMass
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: dwellTimePerMass
                schema:name:
                  const: Dwell Time per Mass
                ada:dataType:
                  const: number
                schema:readonlyValue:
                  const: false
                ada:tier:
                  const: M
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
              - schema:defaultValue
            - title: Isobaric Interference Corrections Applied
              description: 'Whether isobaric interference corrections were applied
                for any measured isotope in this procedure. A procedure-level Boolean:
                if the procedure includes interference corrections, this is always
                Yes. Detail for each affected mass is captured in Interfering Species
                and Interference Correction Method.'
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/laQicpmsTAPP/isobaricInterferenceCorrectionsApplied
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: isobaricInterferenceCorrectionsApplied
                schema:name:
                  const: Isobaric Interference Corrections Applied
                ada:dataType:
                  const: boolean
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
            - title: Interfering Species
              description: Elemental or molecular species (oxides, argides, doubly
                charged ions) overlapping with the measured isotope.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/laQicpmsTAPP/interferingSpecies
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
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
              - schema:defaultValue
            - title: Interference Correction Method
              description: Equation or procedure used to correct for isobaric interferences,
                including the production rate factor and the reference material used
                to measure it.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/laQicpmsTAPP/interferenceCorrectionMethod
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
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
              - schema:defaultValue
            - title: Limit of Quantification (LOQ) Method
              description: 'Reference or description of the method used to calculate
                the limit of quantification (LOQ): the lowest concentration reliably
                measurable with acceptable precision and accuracy. Mandatory at analysis
                level when concentrations near the LOD are reported. Concentrations
                between LOD and LOQ are detectable but not reliably quantifiable.'
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/laQicpmsTAPP/limitOfQuantificationMethod
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
                  const: ada:analyteColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod
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
            - title: Between-Session (Long-Term) Analytical Precision and Assessment
                Method
              description: "Precision of measurements across multiple analytical sessions
                over weeks to months \u2014 long-term or intermediate precision \u2014
                and the method used to assess it. Report both the assessment method
                and the precision values, specifying the reference material, the number
                of measurements and sessions, the time span covered, and the statistic
                reported. Long-term precision is normally poorer than within-session
                precision and is the figure a data user should carry when comparing
                results from different sessions."
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod
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
            - title: Analytical Accuracy and Assessment Method
              description: 'Offset between measured and accepted reference values
                for secondary reference materials, expressed as % relative bias. Report
                both the assessment method and the accuracy values. Specify: (1) secondary
                RM used and source of reference values, (2) number of analyses, and
                (3) elements or element groups assessed. Report any systematic biases
                and likely causes.'
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod
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
                  const: ada:analyteColumn/laQicpmsTAPP/monitoredMasses
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
              title: Dwell Time per Mass
              description: 'Count time (dwell time) per mass position for each measured
                isotope in milliseconds. Longer dwell times improve counting statistics
                and lower detection limits but reduce the number of isotopes measurable
                within a given scan cycle time. For mapping, scan cycle time directly
                determines spatial resolution at a given scan speed: shorter cycle
                time = finer spatial resolution.'
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/laQicpmsTAPP/dwellTimePerMass
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: dwellTimePerMass
                schema:name:
                  const: Dwell Time per Mass
                ada:dataType:
                  const: number
                schema:readonlyValue:
                  const: false
                ada:tier:
                  const: M
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
              - schema:defaultValue
            minContains: 0
            maxContains: 1
          - contains:
              title: Isobaric Interference Corrections Applied
              description: 'Whether isobaric interference corrections were applied
                for any measured isotope in this procedure. A procedure-level Boolean:
                if the procedure includes interference corrections, this is always
                Yes. Detail for each affected mass is captured in Interfering Species
                and Interference Correction Method.'
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/laQicpmsTAPP/isobaricInterferenceCorrectionsApplied
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: isobaricInterferenceCorrectionsApplied
                schema:name:
                  const: Isobaric Interference Corrections Applied
                ada:dataType:
                  const: boolean
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
              title: Interfering Species
              description: Elemental or molecular species (oxides, argides, doubly
                charged ions) overlapping with the measured isotope.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/laQicpmsTAPP/interferingSpecies
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
              description: Equation or procedure used to correct for isobaric interferences,
                including the production rate factor and the reference material used
                to measure it.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/laQicpmsTAPP/interferenceCorrectionMethod
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
              description: 'Reference or description of the method used to calculate
                the limit of quantification (LOQ): the lowest concentration reliably
                measurable with acceptable precision and accuracy. Mandatory at analysis
                level when concentrations near the LOD are reported. Concentrations
                between LOD and LOQ are detectable but not reliably quantifiable.'
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/laQicpmsTAPP/limitOfQuantificationMethod
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
                  const: ada:analyteColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod
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
          - contains:
              title: Between-Session (Long-Term) Analytical Precision and Assessment
                Method
              description: "Precision of measurements across multiple analytical sessions
                over weeks to months \u2014 long-term or intermediate precision \u2014
                and the method used to assess it. Report both the assessment method
                and the precision values, specifying the reference material, the number
                of measurements and sessions, the time span covered, and the statistic
                reported. Long-term precision is normally poorer than within-session
                precision and is the figure a data user should carry when comparing
                results from different sessions."
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod
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
              title: Analytical Accuracy and Assessment Method
              description: 'Offset between measured and accepted reference values
                for secondary reference materials, expressed as % relative bias. Report
                both the assessment method and the accuracy values. Specify: (1) secondary
                RM used and source of reference values, (2) number of analyses, and
                (3) elements or element groups assessed. Report any systematic biases
                and likely causes.'
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod
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
    ada:signalCollectionMode:
      description: Mode used to collect ion signal across the monitored masses. In
        peak hopping mode, the quadrupole jumps sequentially between pre-set mass
        positions and dwells at each peak; in scanning mode, the quadrupole sweeps
        continuously across a defined mass range. Peak hopping is standard for multi-element
        trace analysis as it maximises integration time at each mass.
      type: string
      enum:
      - Peak hopping
      - Scanning
      - N/A
      - None
      - missing
      readOnly: true
    ada:ionCounterDeadTimeDefault:
      description: Dead time of each ion-counting detector channel, used in the dead-time
        correction applied to high count rates. Distinct from pulse/analog cross-calibration,
        which relates the two detector modes rather than correcting counting losses
        within the pulse-counting mode.
      anyOf:
      - type: number
      - type: string
    ada:totalIntegrationTimePerOutputDataPointDefault:
      description: "Total duty-cycle time for one complete mass-scan sweep \u2014
        the sum of all per-isotope dwell times plus inter-mass settling times. Sets
        the time resolution of the downhole signal, and is not recoverable from Dwell
        Time per Mass alone because settling time is not captured there. Applies to
        sequential (quadrupole and single-collector sector-field) acquisition."
      anyOf:
      - type: number
      - type: string
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
    ada:perAnalyteCalibrationStrategy:
      type: array
      items:
        description: "Documents cases where different analytes or analyte groups within
          the same session are calibrated using different strategies \u2014 for example,
          one element used as the internal standard while trace elements are calibrated
          by an external reference material, or different primary standards applied
          to different mass ranges or mineral phases. If a single calibration strategy
          applies uniformly to all analytes, state that here and refer to Internal
          Standard Approach and Normalization / Standards-Based Correction for details.
          Free text; list the strategy for each analyte or analyte group as needed."
        type: string
        readOnly: true
    ada:elementalFractionationCorrection:
      type: array
      items:
        description: Method used to correct for laser-induced elemental fractionation
          (LIEF), including downhole fractionation during prolonged ablation, matrix-dependent
          fractionation between sample and calibration standard, and any specific
          correction algorithm applied. Reference the software function or publication.
        type: string
        readOnly: true
    ada:massBiasCorrectionStrategy:
      description: 'Strategy used to correct instrumental isotopic mass fractionation,
        also called mass bias or mass discrimination. Distinct from Elemental Fractionation
        Correction, which addresses inter-element fractionation during ablation and
        transport: this field addresses discrimination between isotopes of the same
        element, and applies wherever the procedure reports isotope ratios.'
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
    ada:blankBackgroundCorrectionMethod:
      description: 'Method used to subtract the gas blank (background signal with
        laser off) from the ablation signal. For spot and transect analysis: typically
        the mean of a pre-ablation gas blank interval is subtracted per isotope per
        analysis. For mapping: background may be subtracted per raster line, per map
        session, or using a separate gas blank map acquired under identical conditions.'
      type: string
      readOnly: true
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
        - title: Normalization / Standards-Based Correction
          description: Any post-acquisition normalization applied to correct for systematic
            biases identified from secondary reference materials, or stoichiometric
            normalization applied per pixel in mapping. Distinct from the primary
            internal standard approach captured in Internal Standard Approach.
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsTAPP/normalizationStandardsBasedCorrectionDefault
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
        - title: Detection Limit
          description: "Session detection limit, one per reported concentration variable
            (one per analyte, these being the same set), expressed in \xB5g g\u207B\xB9,
            ng g\u207B\xB9, or wt% as appropriate. Mandatory at analysis level to
            demonstrate the reliability of reported near-detection-limit concentrations.
            The calculation method is captured separately in Detection Limit Method."
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsTAPP/detectionLimitDefault
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
      allOf:
      - contains:
          title: Normalization / Standards-Based Correction
          description: Any post-acquisition normalization applied to correct for systematic
            biases identified from secondary reference materials, or stoichiometric
            normalization applied per pixel in mapping. Distinct from the primary
            internal standard approach captured in Internal Standard Approach.
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsTAPP/normalizationStandardsBasedCorrectionDefault
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
          title: Detection Limit
          description: "Session detection limit, one per reported concentration variable
            (one per analyte, these being the same set), expressed in \xB5g g\u207B\xB9,
            ng g\u207B\xB9, or wt% as appropriate. Mandatory at analysis level to
            demonstrate the reliability of reported near-detection-limit concentrations.
            The calculation method is captured separately in Detection Limit Method."
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsTAPP/detectionLimitDefault
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
    ada:constantsAndReferenceValuesUsedDefault:
      description: Physical constants and reference values used in data reduction
        to calculate the final reported quantity (e.g., decay constants for age calculation,
        standard isotope ratios, or other citable reference values used in a correction
        or calculation), together with their source. Distinct from the Group 6 reference-material
        fields, which document accepted values for specific calibration/validation
        materials rather than universal physical constants. Record "None" if no citable,
        revisable physical constants feed into this procedure's data reduction.
      type: string
    ada:primaryStandardNameDefault:
      description: Primary reference material(s) used to calibrate the instrument
        and convert raw signal intensities to concentrations or isotope ratios. Include
        material name, source institution, and citation for the accepted values used.
        Editable because the specific lot or certification vintage may differ between
        sessions while the material type remains the same.
      type: string
    ada:calibrationMeasurementFrequency:
      description: How often the primary calibration standard is measured relative
        to unknown samples within a session. For LA-ICP-MS, this defines the bracketing
        interval between calibration standard ablations used to monitor and correct
        for instrumental drift.
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
    ada:analyticalMode:
      type: array
      items:
        type: string
        enum:
        - Spot
        - Transect
        - Mapping
  required:
  - ada:sampleIntroduction
  - ada:carrierGasFlowRateDefault
  - ada:oxideProductionMethodAndThreshold
  - ada:analysisSequenceDefault
  - ada:signalCollectionMode
  - ada:ionCounterDeadTimeDefault
  - ada:totalIntegrationTimePerOutputDataPointDefault
  - ada:backgroundCountTimeDefault
  - ada:internalStandardApproach
  - ada:internalStandardElement
  - ada:massBiasCorrectionStrategy
  - ada:uncertaintyLevel
  - ada:signalIntegrationIntervalMethod
  - ada:blankBackgroundCorrectionMethod
  - ada:constantsAndReferenceValuesUsedDefault
  - ada:primaryStandardNameDefault
  - ada:calibrationMeasurementFrequency

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS/tapp/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS/tapp/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS/tapp/context.jsonld)

## Sources

* [LA-Q-ICP-MS_TAPP_v15.csv (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/LA-Q-ICPMS/tapp`

