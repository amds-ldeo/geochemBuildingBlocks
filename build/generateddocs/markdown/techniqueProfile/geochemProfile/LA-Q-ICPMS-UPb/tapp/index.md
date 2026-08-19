
# LA-Q-ICP-MS U-Pb Geochronology TAPP (laQicpmsUPbTAPP) (Schema)

`ogch.techniqueProfile.geochemProfile.LA-Q-ICPMS-UPb.tapp` *v0.1*

Laser-ablation quadrupole ICP-MS U-Pb geochronology extension of the base TAPP definition, generated from TAPPS20260813/Current TAPPs/LA-Q-ICP-MS_UPb_TAPP_v16.csv via the path-driven pipeline.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### laQicpmsUPbTAPP example Nakanishi2022
laQicpmsUPbTAPP instance derived from Nakanishi et al. 2022 (GCA 319) CR chondrite metal (HSE) Spot analysis fs-LA-Q-ICP-MS Tokyo Institute of Technology.
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
  "@id": "ex:laQicpmsUPbTAPP-Nakanishi2022",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Nakanishi et al. (2022) CR Chondrite Metal HSE fs-LA-ICP-MS Spot v1",
  "schema:description": "fs laser (260 nm Ti:sapphire) essential for HSE measurement in metal (reduces elemental fractionation and matrix effects); IVB iron meteorite standards (Warburton Range + Tawallah Valley) as matrix-matched standards for iron meteorite metal",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-ICP-MS",
      "schema:name": "fs-LA-Q-ICP-MS"
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
          "@id": "ada:parameter/laQicpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault",
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
            "@id": "ada:parameter/laQicpmsUPbTAPP/spikeOutlierFilteringApproachDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "spikeOutlierFilteringApproachDefault",
            "schema:name": "Spike / Outlier Filtering Approach",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Monitoring of Mg, Si, P, S to check for micro-inclusions (sulfides); analyses with elevated inclusion signals excluded entirely"
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
        "Laser Ablation System",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
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
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/laQicpmsUPbTAPP/laserPulseDuration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laQicpmsUPbTAPP/laserPulseDuration"
            }
          ],
          "schema:name": "Laser Pulse Duration",
          "schema:value": "~220 fs (Ti:sapphire IFRIT system)"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
    },
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
              "@id": "ada:parameter/laQicpmsUPbTAPP/interfaceConeConfiguration",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/laQicpmsUPbTAPP/interfaceConeConfiguration"
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
              "@id": "ada:parameter/laQicpmsUPbTAPP/coolantGasFlowRateDefault",
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
              "@id": "ada:parameter/laQicpmsUPbTAPP/rfPowerDefault",
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
          "schema:name": "missing"
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/laQicpmsUPbTAPP/massResolutionSetting",
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
      "schema:name": "example instrumentName"
    }
  ],
  "ada:ablationSamplingMode": [
    "Spot (stationary)"
  ],
  "ada:carrierGasFlowRateDefault": "Carrier gas flow: 0.6 L/min; species not named (carrier gas identity not stated in Table 1 or text)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsUPbTAPP/plasmaMakeUpGasAdditionDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "plasmaMakeUpGasAdditionDefault",
      "schema:name": "Plasma / Make-up Gas Addition",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Ar make-up: 0.9–1.2 l min⁻¹; Ar auxiliary: 0.6–1.2 l min⁻¹"
    },
    {
      "@id": "ada:parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign"
        }
      ],
      "schema:name": "Multi-Run Sequential Analysis Design",
      "schema:value": "Single spot per location (30 µm circular)"
    },
    {
      "@id": "ada:parameter/laQicpmsUPbTAPP/uncertaintyPropagationMethodDefault",
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
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/monitoredIsotopes",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredIsotopes",
        "schema:name": "Monitored Isotopes",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "boolean",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/normalizationStandardsBasedCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "normalizationStandardsBasedCorrection",
        "schema:name": "Normalization / Standards-Based Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "uri",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "uri"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/massResolutionPerAnalyte",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionPerAnalyte",
        "schema:name": "Mass Resolution per Analyte",
        "ada:dataType": "string"
      }
    ]
  },
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
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ablationSpotDurationDefault": -9999,
  "ada:ageModelDefault": "missing",
  "ada:backgroundCountTimeDefault": -9999,
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:inheritedOrInitialSignalCorrectionDefault": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
  "ada:signalCollectionMode": "missing",
  "ada:targetSelectionCriteriaDefault": "missing",
  "ada:totalIntegrationTimePerOutputDataPointDefault": "missing",
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS-UPb/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:laQicpmsUPbTAPP-Nakanishi2022",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Nakanishi et al. (2022) CR Chondrite Metal HSE fs-LA-ICP-MS Spot v1",
  "schema:description": "fs laser (260 nm Ti:sapphire) essential for HSE measurement in metal (reduces elemental fractionation and matrix effects); IVB iron meteorite standards (Warburton Range + Tawallah Valley) as matrix-matched standards for iron meteorite metal",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-ICP-MS",
      "schema:name": "fs-LA-Q-ICP-MS"
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
          "@id": "ada:parameter/laQicpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault",
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
            "@id": "ada:parameter/laQicpmsUPbTAPP/spikeOutlierFilteringApproachDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "spikeOutlierFilteringApproachDefault",
            "schema:name": "Spike / Outlier Filtering Approach",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Monitoring of Mg, Si, P, S to check for micro-inclusions (sulfides); analyses with elevated inclusion signals excluded entirely"
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
        "Laser Ablation System",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
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
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/laQicpmsUPbTAPP/laserPulseDuration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laQicpmsUPbTAPP/laserPulseDuration"
            }
          ],
          "schema:name": "Laser Pulse Duration",
          "schema:value": "~220 fs (Ti:sapphire IFRIT system)"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
    },
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
              "@id": "ada:parameter/laQicpmsUPbTAPP/interfaceConeConfiguration",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/laQicpmsUPbTAPP/interfaceConeConfiguration"
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
              "@id": "ada:parameter/laQicpmsUPbTAPP/coolantGasFlowRateDefault",
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
              "@id": "ada:parameter/laQicpmsUPbTAPP/rfPowerDefault",
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
          "schema:name": "missing"
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/laQicpmsUPbTAPP/massResolutionSetting",
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
      "schema:name": "example instrumentName"
    }
  ],
  "ada:ablationSamplingMode": [
    "Spot (stationary)"
  ],
  "ada:carrierGasFlowRateDefault": "Carrier gas flow: 0.6 L/min; species not named (carrier gas identity not stated in Table 1 or text)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsUPbTAPP/plasmaMakeUpGasAdditionDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "plasmaMakeUpGasAdditionDefault",
      "schema:name": "Plasma / Make-up Gas Addition",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Ar make-up: 0.9\u20131.2 l min\u207b\u00b9; Ar auxiliary: 0.6\u20131.2 l min\u207b\u00b9"
    },
    {
      "@id": "ada:parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign"
        }
      ],
      "schema:name": "Multi-Run Sequential Analysis Design",
      "schema:value": "Single spot per location (30 \u00b5m circular)"
    },
    {
      "@id": "ada:parameter/laQicpmsUPbTAPP/uncertaintyPropagationMethodDefault",
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
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/monitoredIsotopes",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredIsotopes",
        "schema:name": "Monitored Isotopes",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "boolean",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/normalizationStandardsBasedCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "normalizationStandardsBasedCorrection",
        "schema:name": "Normalization / Standards-Based Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "uri",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "uri"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/massResolutionPerAnalyte",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionPerAnalyte",
        "schema:name": "Mass Resolution per Analyte",
        "ada:dataType": "string"
      }
    ]
  },
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
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ablationSpotDurationDefault": -9999,
  "ada:ageModelDefault": "missing",
  "ada:backgroundCountTimeDefault": -9999,
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:inheritedOrInitialSignalCorrectionDefault": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
  "ada:signalCollectionMode": "missing",
  "ada:targetSelectionCriteriaDefault": "missing",
  "ada:totalIntegrationTimePerOutputDataPointDefault": "missing",
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

ex:laQicpmsUPbTAPP-Nakanishi2022 a cdi:Activity,
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
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/spikeOutlierFilteringApproachDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign>,
        <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/plasmaMakeUpGasAdditionDefault>,
        <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/uncertaintyPropagationMethodDefault> ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Nakanishi, Yokoyama, Okabayashi, Iwamori, Hirata" ] ;
    schema1:datePublished "missing" ;
    schema1:description "fs laser (260 nm Ti:sapphire) essential for HSE measurement in metal (reduces elemental fractionation and matrix effects); IVB iron meteorite standards (Warburton Range + Tawallah Valley) as matrix-matched standards for iron meteorite metal" ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "JSPS KAKENHI; Tokyo Institute of Technology" ] ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/laserPulseDuration> ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "Laser Ablation System" ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "Cyber Laser IFRIT (Ti:sapphire fs UV laser, 260 nm)" ] ;
            schema1:name "example instrumentName" ;
            ada:laserFluenceDefault "12 J cm⁻²" ;
            ada:laserRepetitionRateDefault "20 Hz" ;
            ada:laserSpotGeometryDefault "30 µm circular" ;
            ada:laserType "260 nm Ti:sapphire femtosecond UV; pulse duration ~220 fs (IFRIT system)" ],
        [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/massResolutionSetting> ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "ICPMS",
                "Single-collector quadrupole (Q-ICP-MS)" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/interfaceConeConfiguration> ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Interface Cone" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/coolantGasFlowRateDefault>,
                        <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/rfPowerDefault> ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "ICP Source" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Collision Reaction Cell" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Torch" ;
                    schema1:name "missing" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "Thermo Scientific X-series 2 (Q-ICP-MS)" ] ;
            schema1:name "example instrumentName" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "Dept. of Earth and Planetary Sciences, Tokyo Institute of Technology, Japan" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "fs-LA-Q-ICP-MS" ;
            schema1:termCode "LA-ICP-MS" ] ;
    schema1:name "Nakanishi et al. (2022) CR Chondrite Metal HSE fs-LA-ICP-MS Spot v1" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "CR chondrite metal grains (interior, margin, and isolated types)" ],
                <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault> ] ;
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
    ada:ageModelDefault "missing" ;
    ada:analysisSequenceDefault "IVB meteorite standards (Warburton Range external + Tawallah Valley secondary) measured alongside unknowns; exact bracketing not described" ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/detectionLimit>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/detectionLimitMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/isobaricInterferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/limitOfQuantificationMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/massResolutionPerAnalyte>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/monitoredIsotopes>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/normalizationStandardsBasedCorrection>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ;
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
    ada:elementalFractionationCorrection "External calibration using calibration curve method with IVB iron meteorite standards; ⁶¹Ni as IS from EPMA corrects for ablation yield differences between sample and standard" ;
    ada:inheritedOrInitialSignalCorrectionDefault "missing" ;
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
    ada:totalIntegrationTimePerOutputDataPointDefault "missing" ;
    ada:uncertaintyLevel "missing" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/detectionLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimit" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/detectionLimitMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Detection Limit Method" ;
    schema1:valueName "detectionLimitMethod" ;
    ada:dataType "uri" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/isobaricInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Isobaric Interference Corrections Applied" ;
    schema1:valueName "isobaricInterferenceCorrectionsApplied" ;
    ada:dataType "boolean" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "uri" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/massResolutionPerAnalyte> a schema1:PropertyValueSpecification ;
    schema1:name "Mass Resolution per Analyte" ;
    schema1:valueName "massResolutionPerAnalyte" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/monitoredIsotopes> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Monitored Isotopes" ;
    schema1:valueName "monitoredIsotopes" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/normalizationStandardsBasedCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Normalization / Standards-Based Correction" ;
    schema1:valueName "normalizationStandardsBasedCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/coolantGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 12 ;
    schema1:description "Cool gas: 12–13 l min⁻¹ Ar; Auxiliary: 0.6–1.2 l min⁻¹" ;
    schema1:name "Coolant (Plasma) Gas Flow Rate" ;
    schema1:valueName "coolantGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/massResolutionSetting> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Unit resolution (quadrupole fixed)" ;
    schema1:name "Mass Resolution Setting" ;
    schema1:valueName "massResolutionSetting" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/plasmaMakeUpGasAdditionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Ar make-up: 0.9–1.2 l min⁻¹; Ar auxiliary: 0.6–1.2 l min⁻¹" ;
    schema1:name "Plasma / Make-up Gas Addition" ;
    schema1:valueName "plasmaMakeUpGasAdditionDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/rfPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1400 ;
    schema1:description "1400 W" ;
    schema1:name "RF Power" ;
    schema1:valueName "rfPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "In situ — polished epoxy thick section (petropoxy 154 resin, 0.5 µm diamond finish)" ;
    schema1:name "Sample Form / Analytical Substrate" ;
    schema1:valueName "sampleFormAnalyticalSubstrateDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/spikeOutlierFilteringApproachDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Monitoring of Mg, Si, P, S to check for micro-inclusions (sulfides); analyses with elevated inclusion signals excluded entirely" ;
    schema1:name "Spike / Outlier Filtering Approach" ;
    schema1:valueName "spikeOutlierFilteringApproachDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/uncertaintyPropagationMethodDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "2SE of individual spot measurements reported" ;
    schema1:name "Uncertainty Propagation Method" ;
    schema1:valueName "uncertaintyPropagationMethodDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/interfaceConeConfiguration> a schema1:PropertyValue ;
    schema1:name "Interface Cone Configuration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/interfaceConeConfiguration> ;
    schema1:value "Ni micro-skimmer cone Xs; Ni sampler cone" .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/laserPulseDuration> a schema1:PropertyValue ;
    schema1:name "Laser Pulse Duration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/laserPulseDuration> ;
    schema1:value "~220 fs (Ti:sapphire IFRIT system)" .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign> a schema1:PropertyValue ;
    schema1:name "Multi-Run Sequential Analysis Design" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign> ;
    schema1:value "Single spot per location (30 µm circular)" .


```


### laQicpmsUPbTAPP example Liu2024
laQicpmsUPbTAPP instance derived from Liu et al. 2024 (JAAS 39) Extraterrestrial samples (Li-borate flux glass) Spot analysis fs-LA-Q-ICP-MS Chinese Academy of Sciences.
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
  "@id": "ex:laQicpmsUPbTAPP-Liu2024",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Liu et al. (2024) Extraterrestrial Flux Glass fs-LA-ICP-MS Spot v1",
  "schema:description": "Target: bulk trace element analysis of extraterrestrial samples using only 10 mg; Li-borate flux fusion (35:1 dilution) with fs laser — first reported use of fs laser for flux fusion glass analysis; non-matrix-matched external standards demonstrated accurate with fs laser Reported detail: ada:ablationSamplingMode = Spot (stationary; single spot at 1 Hz).",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-ICP-MS",
      "schema:name": "fs-LA-Q-ICP-MS"
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
          "@id": "ada:parameter/laQicpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault",
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
            "@id": "ada:parameter/laQicpmsUPbTAPP/fusionFluxAndDilutionRatioDefault",
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
            "@id": "ada:parameter/laQicpmsUPbTAPP/preAblationSurfaceTreatmentDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "preAblationSurfaceTreatmentDefault",
            "schema:name": "Pre-Ablation Surface Treatment",
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
            "@id": "ada:parameter/laQicpmsUPbTAPP/spikeOutlierFilteringApproachDefault",
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
            "@id": "ada:parameter/laQicpmsUPbTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "pulseAnalogDetectorNonlinearityCorrectionDefault",
            "schema:name": "Pulse/Analog Detector Nonlinearity Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Applied: dual detector mode (30 ms / 10 ms dwell alternation)"
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
        "Laser Ablation System",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
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
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/laQicpmsUPbTAPP/laserPulseDuration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laQicpmsUPbTAPP/laserPulseDuration"
            }
          ],
          "schema:name": "Laser Pulse Duration",
          "schema:value": "Femtosecond (exact value not stated; GenesisGEO fs laser)"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
    },
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
          "@id": "ada:parameter/laQicpmsUPbTAPP/massResolutionSetting",
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
          "@id": "ada:parameter/laQicpmsUPbTAPP/detectorConfiguration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laQicpmsUPbTAPP/detectorConfiguration"
            }
          ],
          "schema:name": "Detector Configuration",
          "schema:value": "Dual mode detector (30 ms / 10 ms dwell alternation)"
        },
        {
          "@id": "ada:parameter/laQicpmsUPbTAPP/icpTuningDefault",
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
          "@id": "ada:parameter/laQicpmsUPbTAPP/memoryEffectMitigationDefault",
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
              "@id": "ada:parameter/laQicpmsUPbTAPP/coolantGasFlowRateDefault",
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
              "@id": "ada:parameter/laQicpmsUPbTAPP/rfPowerDefault",
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
          "schema:name": "missing"
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
          "schema:name": "missing"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
    }
  ],
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Iolite 4 (Paton et al. 2011)"
    }
  ],
  "ada:ablationSamplingMode": [
    "Spot (stationary)"
  ],
  "ada:ablationSpotDurationDefault": "45 s ablation (after 25 s gas blank; 25 s washout between analyses)",
  "ada:carrierGasFlowRateDefault": "He: 0.7 l min⁻¹ (chamber) + 0.1 l min⁻¹ (cup gas)",
  "ada:oxideProductionMethodAndThreshold": "ThO⁺/Th⁺ (mass 248/232) <0.3%; U/Th monitored at 0.95–1.05",
  "ada:analysisSequenceDefault": "Gas blank (25 s) → ablation (45 s) → washout (25 s); NIST 612 and 614 as external standards; BHVO-2 and 6 GRMs measured as unknowns",
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
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/monitoredIsotopes",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredIsotopes",
        "schema:name": "Monitored Isotopes",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "boolean",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/normalizationStandardsBasedCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "normalizationStandardsBasedCorrection",
        "schema:name": "Normalization / Standards-Based Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "uri",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "uri"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/massResolutionPerAnalyte",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionPerAnalyte",
        "schema:name": "Mass Resolution per Analyte",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:backgroundCountTimeDefault": "25 s gas blank before each ablation",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign"
        }
      ],
      "schema:name": "Multi-Run Sequential Analysis Design",
      "schema:value": "Single spot per location (45 s ablation at 1 Hz)"
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
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ageModelDefault": "missing",
  "ada:inheritedOrInitialSignalCorrectionDefault": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
  "ada:signalCollectionMode": "missing",
  "ada:targetSelectionCriteriaDefault": "missing",
  "ada:totalIntegrationTimePerOutputDataPointDefault": "missing",
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS-UPb/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:laQicpmsUPbTAPP-Liu2024",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Liu et al. (2024) Extraterrestrial Flux Glass fs-LA-ICP-MS Spot v1",
  "schema:description": "Target: bulk trace element analysis of extraterrestrial samples using only 10 mg; Li-borate flux fusion (35:1 dilution) with fs laser \u2014 first reported use of fs laser for flux fusion glass analysis; non-matrix-matched external standards demonstrated accurate with fs laser Reported detail: ada:ablationSamplingMode = Spot (stationary; single spot at 1 Hz).",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-ICP-MS",
      "schema:name": "fs-LA-Q-ICP-MS"
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
          "@id": "ada:parameter/laQicpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault",
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
            "@id": "ada:parameter/laQicpmsUPbTAPP/fusionFluxAndDilutionRatioDefault",
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
            "@id": "ada:parameter/laQicpmsUPbTAPP/preAblationSurfaceTreatmentDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "preAblationSurfaceTreatmentDefault",
            "schema:name": "Pre-Ablation Surface Treatment",
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
            "@id": "ada:parameter/laQicpmsUPbTAPP/spikeOutlierFilteringApproachDefault",
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
            "@id": "ada:parameter/laQicpmsUPbTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "pulseAnalogDetectorNonlinearityCorrectionDefault",
            "schema:name": "Pulse/Analog Detector Nonlinearity Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Applied: dual detector mode (30 ms / 10 ms dwell alternation)"
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
        "Laser Ablation System",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
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
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/laQicpmsUPbTAPP/laserPulseDuration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laQicpmsUPbTAPP/laserPulseDuration"
            }
          ],
          "schema:name": "Laser Pulse Duration",
          "schema:value": "Femtosecond (exact value not stated; GenesisGEO fs laser)"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
    },
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
          "@id": "ada:parameter/laQicpmsUPbTAPP/massResolutionSetting",
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
          "@id": "ada:parameter/laQicpmsUPbTAPP/detectorConfiguration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laQicpmsUPbTAPP/detectorConfiguration"
            }
          ],
          "schema:name": "Detector Configuration",
          "schema:value": "Dual mode detector (30 ms / 10 ms dwell alternation)"
        },
        {
          "@id": "ada:parameter/laQicpmsUPbTAPP/icpTuningDefault",
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
          "@id": "ada:parameter/laQicpmsUPbTAPP/memoryEffectMitigationDefault",
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
              "@id": "ada:parameter/laQicpmsUPbTAPP/coolantGasFlowRateDefault",
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
              "@id": "ada:parameter/laQicpmsUPbTAPP/rfPowerDefault",
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
          "schema:name": "missing"
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
          "schema:name": "missing"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
    }
  ],
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Iolite 4 (Paton et al. 2011)"
    }
  ],
  "ada:ablationSamplingMode": [
    "Spot (stationary)"
  ],
  "ada:ablationSpotDurationDefault": "45 s ablation (after 25 s gas blank; 25 s washout between analyses)",
  "ada:carrierGasFlowRateDefault": "He: 0.7 l min\u207b\u00b9 (chamber) + 0.1 l min\u207b\u00b9 (cup gas)",
  "ada:oxideProductionMethodAndThreshold": "ThO\u207a/Th\u207a (mass 248/232) <0.3%; U/Th monitored at 0.95\u20131.05",
  "ada:analysisSequenceDefault": "Gas blank (25 s) \u2192 ablation (45 s) \u2192 washout (25 s); NIST 612 and 614 as external standards; BHVO-2 and 6 GRMs measured as unknowns",
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
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/monitoredIsotopes",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredIsotopes",
        "schema:name": "Monitored Isotopes",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "boolean",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/normalizationStandardsBasedCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "normalizationStandardsBasedCorrection",
        "schema:name": "Normalization / Standards-Based Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "uri",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "uri"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/massResolutionPerAnalyte",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionPerAnalyte",
        "schema:name": "Mass Resolution per Analyte",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:backgroundCountTimeDefault": "25 s gas blank before each ablation",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign"
        }
      ],
      "schema:name": "Multi-Run Sequential Analysis Design",
      "schema:value": "Single spot per location (45 s ablation at 1 Hz)"
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
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ageModelDefault": "missing",
  "ada:inheritedOrInitialSignalCorrectionDefault": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
  "ada:signalCollectionMode": "missing",
  "ada:targetSelectionCriteriaDefault": "missing",
  "ada:totalIntegrationTimePerOutputDataPointDefault": "missing",
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

ex:laQicpmsUPbTAPP-Liu2024 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault>,
                        <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/spikeOutlierFilteringApproachDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/fusionFluxAndDilutionRatioDefault>,
                        <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/preAblationSurfaceTreatmentDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Li-borate fusion: 350 mg Li₂B₄O₇ + 10 mg powdered sample fused in Pt-Au crucible (M4 automatic fluxer); glass surface cleaned with ethanol before LA" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign> ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Liu, Xue, Li, Wang et al." ] ;
    schema1:datePublished "missing" ;
    schema1:description "Target: bulk trace element analysis of extraterrestrial samples using only 10 mg; Li-borate flux fusion (35:1 dilution) with fs laser — first reported use of fs laser for flux fusion glass analysis; non-matrix-matched external standards demonstrated accurate with fs laser Reported detail: ada:ablationSamplingMode = Spot (stationary; single spot at 1 Hz)." ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NSFC; Chinese Academy of Sciences" ] ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/laserPulseDuration> ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "Laser Ablation System" ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "Shanghai Chemlab GenesisGEO (high-repetition-rate fs laser, 343 nm)" ] ;
            schema1:name "example instrumentName" ;
            ada:laserFluenceDefault "6.79 J cm⁻²" ;
            ada:laserRepetitionRateDefault "1 Hz" ;
            ada:laserSpotGeometryDefault "100×100 µm square (stated as 100 µm diameter spot at 1 Hz)" ;
            ada:laserType "343 nm fs (GenesisGEO high-repetition-rate femtosecond laser)" ],
        [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/detectorConfiguration>,
                <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/icpTuningDefault>,
                <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/massResolutionSetting>,
                <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/memoryEffectMitigationDefault> ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "ICPMS" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Torch" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Collision Reaction Cell" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/coolantGasFlowRateDefault>,
                        <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/rfPowerDefault> ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "ICP Source" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Interface Cone" ;
                    schema1:name "missing" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "Agilent 8900 (Q-ICP-MS; ICP-MS/MS capable)" ] ;
            schema1:name "example instrumentName" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "State Key Laboratory of Lithospheric Evolution and Environmental Coevolution, IGGCAS, Beijing, China" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "fs-LA-Q-ICP-MS" ;
            schema1:termCode "LA-ICP-MS" ] ;
    schema1:name "Liu et al. (2024) Extraterrestrial Flux Glass fs-LA-ICP-MS Spot v1" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Li-borate flux fusion glass (extraterrestrial sample preparation)" ],
                <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Liu et al. (2024) JAAS 39, 2728; Pettke et al. (2012) for LOD" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:ablationPitDepthRateDefault "missing" ;
    ada:ablationSamplingMode "Spot (stationary)" ;
    ada:ablationSpotDurationDefault "45 s ablation (after 25 s gas blank; 25 s washout between analyses)" ;
    ada:ageModelDefault "missing" ;
    ada:analysisSequenceDefault "Gas blank (25 s) → ablation (45 s) → washout (25 s); NIST 612 and 614 as external standards; BHVO-2 and 6 GRMs measured as unknowns" ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/detectionLimit>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/detectionLimitMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/isobaricInterferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/limitOfQuantificationMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/massResolutionPerAnalyte>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/monitoredIsotopes>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/normalizationStandardsBasedCorrection>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ;
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
    ada:elementalFractionationCorrection "Femtosecond laser substantially reduces elemental fractionation and matrix effects (stated); non-matrix-matched external standards (NIST 612 + 614) used successfully with fs laser (verified by GRM accuracy assessment)" ;
    ada:inheritedOrInitialSignalCorrectionDefault "missing" ;
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
    ada:totalIntegrationTimePerOutputDataPointDefault "missing" ;
    ada:uncertaintyLevel "missing" ;
    bios:computationalTool [ schema1:name "Iolite 4 (Paton et al. 2011)" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/detectionLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimit" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/detectionLimitMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Detection Limit Method" ;
    schema1:valueName "detectionLimitMethod" ;
    ada:dataType "uri" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/isobaricInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Isobaric Interference Corrections Applied" ;
    schema1:valueName "isobaricInterferenceCorrectionsApplied" ;
    ada:dataType "boolean" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "uri" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/massResolutionPerAnalyte> a schema1:PropertyValueSpecification ;
    schema1:name "Mass Resolution per Analyte" ;
    schema1:valueName "massResolutionPerAnalyte" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/monitoredIsotopes> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Monitored Isotopes" ;
    schema1:valueName "monitoredIsotopes" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/normalizationStandardsBasedCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Normalization / Standards-Based Correction" ;
    schema1:valueName "normalizationStandardsBasedCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/coolantGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 15 ;
    schema1:description "Plasma gas flow: 15 l min⁻¹; Auxiliary gas: 0.85 l min⁻¹" ;
    schema1:name "Coolant (Plasma) Gas Flow Rate" ;
    schema1:valueName "coolantGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/fusionFluxAndDilutionRatioDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Li₂B₄O₇ flux; sample:flux = 1:35 (10 mg sample + 350 mg flux)" ;
    schema1:name "Fusion Flux and Dilution Ratio" ;
    schema1:valueName "fusionFluxAndDilutionRatioDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/icpTuningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Gas flows optimized via spot ablation of NIST SRM 612 to obtain maximum signal intensities while maintaining ThO/Th <0.3% and U/Th at 0.95–1.05" ;
    schema1:name "ICP Tuning" ;
    schema1:valueName "icpTuningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/massResolutionSetting> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Unit resolution (quadrupole; ICP-MS/MS mode not specified)" ;
    schema1:name "Mass Resolution Setting" ;
    schema1:valueName "massResolutionSetting" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/memoryEffectMitigationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "25 s washout between analyses (25 s gas blank → 45 s ablation → 25 s washout)" ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:valueName "memoryEffectMitigationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/preAblationSurfaceTreatmentDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Surface cleaning with ethanol before analysis" ;
    schema1:name "Pre-Ablation Surface Treatment" ;
    schema1:valueName "preAblationSurfaceTreatmentDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Applied: dual detector mode (30 ms / 10 ms dwell alternation)" ;
    schema1:name "Pulse/Analog Detector Nonlinearity Correction" ;
    schema1:valueName "pulseAnalogDetectorNonlinearityCorrectionDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/rfPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1550 ;
    schema1:description "1550 W" ;
    schema1:name "RF Power" ;
    schema1:valueName "rfPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Li-borate flux fusion glass disc (10 mg sample + 350 mg Li₂B₄O₇, 35:1 dilution)" ;
    schema1:name "Sample Form / Analytical Substrate" ;
    schema1:valueName "sampleFormAnalyticalSubstrateDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/spikeOutlierFilteringApproachDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Homogeneity index (H) applied to test element distribution; Co, Ni, Cu in high-Si glass (GSR-1) identified as near-LOD and flagged; flux blank contributions to pollution elements subtracted" ;
    schema1:name "Spike / Outlier Filtering Approach" ;
    schema1:valueName "spikeOutlierFilteringApproachDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/detectorConfiguration> a schema1:PropertyValue ;
    schema1:name "Detector Configuration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/detectorConfiguration> ;
    schema1:value "Dual mode detector (30 ms / 10 ms dwell alternation)" .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/laserPulseDuration> a schema1:PropertyValue ;
    schema1:name "Laser Pulse Duration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/laserPulseDuration> ;
    schema1:value "Femtosecond (exact value not stated; GenesisGEO fs laser)" .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign> a schema1:PropertyValue ;
    schema1:name "Multi-Run Sequential Analysis Design" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign> ;
    schema1:value "Single spot per location (45 s ablation at 1 Hz)" .


```


### laQicpmsUPbTAPP example Liu2025
laQicpmsUPbTAPP instance derived from Liu et al. 2025 (GCA 393) Experimental silicate glass Spot analysis ns-LA-Q-ICP-MS Guangzhou Inst. Geochemistry.
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
  "@id": "ex:laQicpmsUPbTAPP-Liu2025",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Liu et al. (2025) Experimental Silicate Glass LA-ICP-MS Spot v1",
  "schema:description": "Analysis of quenched experimental glasses from high-pressure (1 GPa) piston-cylinder experiments; Au and Cu solubility measurements; smooth time-resolved signals indicate fully dissolved Au (no micronuggets)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-ICP-MS",
      "schema:name": "LA-Q-ICP-MS"
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
          "@id": "ada:parameter/laQicpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault",
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
            "@id": "ada:parameter/laQicpmsUPbTAPP/spikeOutlierFilteringApproachDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "spikeOutlierFilteringApproachDefault",
            "schema:name": "Spike / Outlier Filtering Approach",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Micronuggets identified from Au signal spikes in time-resolved spectra; excluded from integration (smooth signals = fully dissolved Au; Fig. 1 shows this criterion)"
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
      ]
    },
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
          "@id": "ada:parameter/laQicpmsUPbTAPP/massResolutionSetting",
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
          "schema:name": "missing"
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
          "schema:name": "missing"
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
          "schema:name": "missing"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
    }
  ],
  "ada:ablationSpotDurationDefault": "~40 s (inferred from typical CetacAnalyte HE protocol for glass)",
  "ada:carrierGasFlowRateDefault": "He (flow rate not stated; carrier gas with N₂ or Ar mixed for sensitivity optimization)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsUPbTAPP/plasmaMakeUpGasAdditionDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "plasmaMakeUpGasAdditionDefault",
      "schema:name": "Plasma / Make-up Gas Addition",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N₂ or Ar mixed into He carrier for sensitivity optimization (amounts not stated)"
    },
    {
      "@id": "ada:parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign"
        }
      ],
      "schema:name": "Multi-Run Sequential Analysis Design",
      "schema:value": "Single spot per location (~40 s ablation at 7 Hz)"
    }
  ],
  "ada:analysisSequenceDefault": "NIST 610 as primary standard measured in session; NIST 612 and BCR-2G as monitoring standards; unknowns bracketed by standards",
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
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/monitoredIsotopes",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredIsotopes",
        "schema:name": "Monitored Isotopes",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "boolean",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/normalizationStandardsBasedCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "normalizationStandardsBasedCorrection",
        "schema:name": "Normalization / Standards-Based Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "uri",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "uri"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/massResolutionPerAnalyte",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionPerAnalyte",
        "schema:name": "Mass Resolution per Analyte",
        "ada:dataType": "string"
      }
    ]
  },
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
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ageModelDefault": "missing",
  "ada:backgroundCountTimeDefault": -9999,
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:inheritedOrInitialSignalCorrectionDefault": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
  "ada:signalCollectionMode": "missing",
  "ada:targetSelectionCriteriaDefault": "missing",
  "ada:totalIntegrationTimePerOutputDataPointDefault": "missing",
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS-UPb/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:laQicpmsUPbTAPP-Liu2025",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Liu et al. (2025) Experimental Silicate Glass LA-ICP-MS Spot v1",
  "schema:description": "Analysis of quenched experimental glasses from high-pressure (1 GPa) piston-cylinder experiments; Au and Cu solubility measurements; smooth time-resolved signals indicate fully dissolved Au (no micronuggets)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-ICP-MS",
      "schema:name": "LA-Q-ICP-MS"
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
          "@id": "ada:parameter/laQicpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault",
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
            "@id": "ada:parameter/laQicpmsUPbTAPP/spikeOutlierFilteringApproachDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "spikeOutlierFilteringApproachDefault",
            "schema:name": "Spike / Outlier Filtering Approach",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Micronuggets identified from Au signal spikes in time-resolved spectra; excluded from integration (smooth signals = fully dissolved Au; Fig. 1 shows this criterion)"
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
      ]
    },
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
          "@id": "ada:parameter/laQicpmsUPbTAPP/massResolutionSetting",
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
          "schema:name": "missing"
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
          "schema:name": "missing"
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
          "schema:name": "missing"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
    }
  ],
  "ada:ablationSpotDurationDefault": "~40 s (inferred from typical CetacAnalyte HE protocol for glass)",
  "ada:carrierGasFlowRateDefault": "He (flow rate not stated; carrier gas with N\u2082 or Ar mixed for sensitivity optimization)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsUPbTAPP/plasmaMakeUpGasAdditionDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "plasmaMakeUpGasAdditionDefault",
      "schema:name": "Plasma / Make-up Gas Addition",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N\u2082 or Ar mixed into He carrier for sensitivity optimization (amounts not stated)"
    },
    {
      "@id": "ada:parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign"
        }
      ],
      "schema:name": "Multi-Run Sequential Analysis Design",
      "schema:value": "Single spot per location (~40 s ablation at 7 Hz)"
    }
  ],
  "ada:analysisSequenceDefault": "NIST 610 as primary standard measured in session; NIST 612 and BCR-2G as monitoring standards; unknowns bracketed by standards",
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
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/monitoredIsotopes",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredIsotopes",
        "schema:name": "Monitored Isotopes",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "boolean",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/normalizationStandardsBasedCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "normalizationStandardsBasedCorrection",
        "schema:name": "Normalization / Standards-Based Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "uri",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "uri"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/massResolutionPerAnalyte",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionPerAnalyte",
        "schema:name": "Mass Resolution per Analyte",
        "ada:dataType": "string"
      }
    ]
  },
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
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ageModelDefault": "missing",
  "ada:backgroundCountTimeDefault": -9999,
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:inheritedOrInitialSignalCorrectionDefault": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
  "ada:signalCollectionMode": "missing",
  "ada:targetSelectionCriteriaDefault": "missing",
  "ada:totalIntegrationTimePerOutputDataPointDefault": "missing",
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

ex:laQicpmsUPbTAPP-Liu2025 a cdi:Activity,
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
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Experimental capsule longitudinally sectioned with wire saw; half mounted in epoxy for analysis" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/spikeOutlierFilteringApproachDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign>,
        <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/plasmaMakeUpGasAdditionDefault> ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Liu, Li, Xu, Xiong et al." ] ;
    schema1:datePublished "missing" ;
    schema1:description "Analysis of quenched experimental glasses from high-pressure (1 GPa) piston-cylinder experiments; Au and Cu solubility measurements; smooth time-resolved signals indicate fully dissolved Au (no micronuggets)" ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "Strategic Priority Research Program (B) CAS; NSFC 92062222, 42073057, 42250710679, 42250202, 42273023" ] ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/massResolutionSetting> ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "ICPMS" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Interface Cone" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "ICP Source" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Torch" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Collision Reaction Cell" ;
                    schema1:name "missing" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "Agilent 7900 (Q-ICP-MS)" ] ;
            schema1:name "example instrumentName" ],
        [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "Laser Ablation System" ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "Resonetics 193 nm ArF excimer laser (coupled to Cetac Analyte HE system)" ] ;
            schema1:name "Cetac Analyte HE system (stated as the laser ablation system coupled to Agilent 7900)" ;
            ada:laserFluenceDefault "~2.5 J cm⁻² (stated as \"energy of ~2.5 J/cm²\")" ;
            ada:laserRepetitionRateDefault "7 Hz" ;
            ada:laserSpotGeometryDefault "40 µm circular (silicate glass)" ;
            ada:laserType "193 nm (CetacAnalyte HE; ns pulse)" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "State Key Laboratory of Isotope Geochemistry, Guangzhou Institute of Geochemistry, CAS, China" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "LA-Q-ICP-MS" ;
            schema1:termCode "LA-ICP-MS" ] ;
    schema1:name "Liu et al. (2025) Experimental Silicate Glass LA-ICP-MS Spot v1" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Experimental dacitic silicate glass (quench product)" ],
                <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Liu et al. (2025) GCA 393, 170; Xu et al. (2022) for experimental protocol" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:ablationPitDepthRateDefault "missing" ;
    ada:ablationSpotDurationDefault "~40 s (inferred from typical CetacAnalyte HE protocol for glass)" ;
    ada:ageModelDefault "missing" ;
    ada:analysisSequenceDefault "NIST 610 as primary standard measured in session; NIST 612 and BCR-2G as monitoring standards; unknowns bracketed by standards" ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/detectionLimit>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/detectionLimitMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/isobaricInterferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/limitOfQuantificationMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/massResolutionPerAnalyte>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/monitoredIsotopes>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/normalizationStandardsBasedCorrection>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ;
            ada:defaultAnalytes "all detected via Agilent 7900 (exact isotope list not fully stated)",
                "¹⁹⁷Au",
                "⁶³Cu (primary targets)" ] ;
    ada:backgroundCountTimeDefault -9999 ;
    ada:blankBackgroundCorrectionMethod "missing" ;
    ada:calibrationMeasurementFrequency "NIST 610 as primary; NIST 612 and BCR-2G as monitoring standards" ;
    ada:carrierGasFlowRateDefault "He (flow rate not stated; carrier gas with N₂ or Ar mixed for sensitivity optimization)" ;
    ada:elementalFractionationCorrection "Femtosecond laser reduces LIEF; NIST 610 external standard; Si IS from EMP corrects for ablation yield" ;
    ada:inheritedOrInitialSignalCorrectionDefault "missing" ;
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
    ada:totalIntegrationTimePerOutputDataPointDefault "missing" ;
    ada:uncertaintyLevel "missing" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/detectionLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimit" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/detectionLimitMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Detection Limit Method" ;
    schema1:valueName "detectionLimitMethod" ;
    ada:dataType "uri" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/isobaricInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Isobaric Interference Corrections Applied" ;
    schema1:valueName "isobaricInterferenceCorrectionsApplied" ;
    ada:dataType "boolean" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "uri" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/massResolutionPerAnalyte> a schema1:PropertyValueSpecification ;
    schema1:name "Mass Resolution per Analyte" ;
    schema1:valueName "massResolutionPerAnalyte" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/monitoredIsotopes> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Monitored Isotopes" ;
    schema1:valueName "monitoredIsotopes" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/normalizationStandardsBasedCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Normalization / Standards-Based Correction" ;
    schema1:valueName "normalizationStandardsBasedCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/massResolutionSetting> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Unit resolution (quadrupole fixed)" ;
    schema1:name "Mass Resolution Setting" ;
    schema1:valueName "massResolutionSetting" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/plasmaMakeUpGasAdditionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N₂ or Ar mixed into He carrier for sensitivity optimization (amounts not stated)" ;
    schema1:name "Plasma / Make-up Gas Addition" ;
    schema1:valueName "plasmaMakeUpGasAdditionDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "In situ — polished epoxy mount (experimental capsule half-section)" ;
    schema1:name "Sample Form / Analytical Substrate" ;
    schema1:valueName "sampleFormAnalyticalSubstrateDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/spikeOutlierFilteringApproachDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Micronuggets identified from Au signal spikes in time-resolved spectra; excluded from integration (smooth signals = fully dissolved Au; Fig. 1 shows this criterion)" ;
    schema1:name "Spike / Outlier Filtering Approach" ;
    schema1:valueName "spikeOutlierFilteringApproachDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign> a schema1:PropertyValue ;
    schema1:name "Multi-Run Sequential Analysis Design" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign> ;
    schema1:value "Single spot per location (~40 s ablation at 7 Hz)" .


```


### laQicpmsUPbTAPP example Liu2025-2
laQicpmsUPbTAPP instance derived from Liu et al. 2025 (GCA 393) Experimental sulfide Spot analysis ns-LA-Q-ICP-MS Guangzhou Inst. Geochemistry.
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
  "@id": "ex:laQicpmsUPbTAPP-Liu2025-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Liu et al. (2025) Experimental Sulfide LA-ICP-MS Spot v1",
  "schema:description": "Analysis of quenched experimental pyrrhotite (Fe₁₋ₓS) from same piston-cylinder experiments; 20 µm spot required due to small grain size (5–50 µm); same instrument and analytical session as glass protocol",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-ICP-MS",
      "schema:name": "LA-Q-ICP-MS"
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
          "@id": "ada:parameter/laQicpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault",
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
            "@id": "ada:parameter/laQicpmsUPbTAPP/spikeOutlierFilteringApproachDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "spikeOutlierFilteringApproachDefault",
            "schema:name": "Spike / Outlier Filtering Approach",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Same approach as glass; Au spike identification critical for determining solubility vs. nugget contribution"
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
      ]
    },
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
          "@id": "ada:parameter/laQicpmsUPbTAPP/massResolutionSetting",
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
          "schema:name": "missing"
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
          "schema:name": "missing"
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
          "schema:name": "missing"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
    }
  ],
  "ada:ablationSpotDurationDefault": "~40 s (same protocol; grain size >20 µm selected)",
  "ada:carrierGasFlowRateDefault": "He (flow rate not stated; same system as glass protocol)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsUPbTAPP/plasmaMakeUpGasAdditionDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "plasmaMakeUpGasAdditionDefault",
      "schema:name": "Plasma / Make-up Gas Addition",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N₂ or Ar mixed (same protocol as glass)"
    },
    {
      "@id": "ada:parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign"
        }
      ],
      "schema:name": "Multi-Run Sequential Analysis Design",
      "schema:value": "Single spot per location (sulfides; same acquisition parameters as glass but 20 µm spot)"
    }
  ],
  "ada:analysisSequenceDefault": "Same bracketing as silicate glass protocol",
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
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/monitoredIsotopes",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredIsotopes",
        "schema:name": "Monitored Isotopes",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "boolean",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/normalizationStandardsBasedCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "normalizationStandardsBasedCorrection",
        "schema:name": "Normalization / Standards-Based Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "uri",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "uri"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/massResolutionPerAnalyte",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionPerAnalyte",
        "schema:name": "Mass Resolution per Analyte",
        "ada:dataType": "string"
      }
    ]
  },
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
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ageModelDefault": "missing",
  "ada:backgroundCountTimeDefault": -9999,
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:inheritedOrInitialSignalCorrectionDefault": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
  "ada:signalCollectionMode": "missing",
  "ada:targetSelectionCriteriaDefault": "missing",
  "ada:totalIntegrationTimePerOutputDataPointDefault": "missing",
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS-UPb/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:laQicpmsUPbTAPP-Liu2025-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Liu et al. (2025) Experimental Sulfide LA-ICP-MS Spot v1",
  "schema:description": "Analysis of quenched experimental pyrrhotite (Fe\u2081\u208b\u2093S) from same piston-cylinder experiments; 20 \u00b5m spot required due to small grain size (5\u201350 \u00b5m); same instrument and analytical session as glass protocol",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-ICP-MS",
      "schema:name": "LA-Q-ICP-MS"
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
          "@id": "ada:parameter/laQicpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault",
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
            "@id": "ada:parameter/laQicpmsUPbTAPP/spikeOutlierFilteringApproachDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "spikeOutlierFilteringApproachDefault",
            "schema:name": "Spike / Outlier Filtering Approach",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Same approach as glass; Au spike identification critical for determining solubility vs. nugget contribution"
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
      ]
    },
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
          "@id": "ada:parameter/laQicpmsUPbTAPP/massResolutionSetting",
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
          "schema:name": "missing"
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
          "schema:name": "missing"
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
          "schema:name": "missing"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
    }
  ],
  "ada:ablationSpotDurationDefault": "~40 s (same protocol; grain size >20 \u00b5m selected)",
  "ada:carrierGasFlowRateDefault": "He (flow rate not stated; same system as glass protocol)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsUPbTAPP/plasmaMakeUpGasAdditionDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "plasmaMakeUpGasAdditionDefault",
      "schema:name": "Plasma / Make-up Gas Addition",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N\u2082 or Ar mixed (same protocol as glass)"
    },
    {
      "@id": "ada:parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign"
        }
      ],
      "schema:name": "Multi-Run Sequential Analysis Design",
      "schema:value": "Single spot per location (sulfides; same acquisition parameters as glass but 20 \u00b5m spot)"
    }
  ],
  "ada:analysisSequenceDefault": "Same bracketing as silicate glass protocol",
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
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/monitoredIsotopes",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredIsotopes",
        "schema:name": "Monitored Isotopes",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "boolean",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/normalizationStandardsBasedCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "normalizationStandardsBasedCorrection",
        "schema:name": "Normalization / Standards-Based Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "uri",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "uri"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laQicpmsUPbTAPP/massResolutionPerAnalyte",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionPerAnalyte",
        "schema:name": "Mass Resolution per Analyte",
        "ada:dataType": "string"
      }
    ]
  },
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
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ageModelDefault": "missing",
  "ada:backgroundCountTimeDefault": -9999,
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:inheritedOrInitialSignalCorrectionDefault": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
  "ada:signalCollectionMode": "missing",
  "ada:targetSelectionCriteriaDefault": "missing",
  "ada:totalIntegrationTimePerOutputDataPointDefault": "missing",
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

ex:laQicpmsUPbTAPP-Liu2025-2 a cdi:Activity,
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
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Same capsule section as silicate glass; sulfide grains ≥20 µm selected by SEM-BSE" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/spikeOutlierFilteringApproachDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign>,
        <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/plasmaMakeUpGasAdditionDefault> ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Liu, Li, Xu, Xiong et al." ] ;
    schema1:datePublished "missing" ;
    schema1:description "Analysis of quenched experimental pyrrhotite (Fe₁₋ₓS) from same piston-cylinder experiments; 20 µm spot required due to small grain size (5–50 µm); same instrument and analytical session as glass protocol" ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "Strategic Priority Research Program (B) CAS; NSFC 92062222, 42073057, 42250710679, 42250202, 42273023" ] ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "Laser Ablation System" ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "Resonetics 193 nm ArF excimer laser (coupled to Cetac Analyte HE system; same system as glass protocol)" ] ;
            schema1:name "Cetac Analyte HE system (same as silicate glass protocol)" ;
            ada:laserFluenceDefault "~2.5 J cm⁻²" ;
            ada:laserRepetitionRateDefault "7 Hz" ;
            ada:laserSpotGeometryDefault "20 µm circular (sulfide; grain sizes >20 µm selected)" ;
            ada:laserType "193 nm (CetacAnalyte HE; ns pulse)" ],
        [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/massResolutionSetting> ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "ICPMS" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Collision Reaction Cell" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Torch" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Interface Cone" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "ICP Source" ;
                    schema1:name "missing" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "Agilent 7900 (Q-ICP-MS)" ] ;
            schema1:name "example instrumentName" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "State Key Laboratory of Isotope Geochemistry, Guangzhou Institute of Geochemistry, CAS, China" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "LA-Q-ICP-MS" ;
            schema1:termCode "LA-ICP-MS" ] ;
    schema1:name "Liu et al. (2025) Experimental Sulfide LA-ICP-MS Spot v1" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Experimental pyrrhotite (Fe₁₋ₓS) sulfide (quench product)" ],
                <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Liu et al. (2025) GCA 393, 170; Xu et al. (2022)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:ablationPitDepthRateDefault "missing" ;
    ada:ablationSpotDurationDefault "~40 s (same protocol; grain size >20 µm selected)" ;
    ada:ageModelDefault "missing" ;
    ada:analysisSequenceDefault "Same bracketing as silicate glass protocol" ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/detectionLimit>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/detectionLimitMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/isobaricInterferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/limitOfQuantificationMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/massResolutionPerAnalyte>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/monitoredIsotopes>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/normalizationStandardsBasedCorrection>,
                <https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ;
            ada:defaultAnalytes "¹⁹⁷Au",
                "⁶³Cu (primary targets; Si and Fe from EMP as internal standards)" ] ;
    ada:backgroundCountTimeDefault -9999 ;
    ada:blankBackgroundCorrectionMethod "missing" ;
    ada:calibrationMeasurementFrequency "Same bracketing as silicate glass protocol" ;
    ada:carrierGasFlowRateDefault "He (flow rate not stated; same system as glass protocol)" ;
    ada:elementalFractionationCorrection "Femtosecond laser reduces LIEF; NIST 610 external standard; Fe IS from EMP corrects for ablation yield; micronuggets identified from Au signal spikes and excluded from integration" ;
    ada:inheritedOrInitialSignalCorrectionDefault "missing" ;
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
    ada:totalIntegrationTimePerOutputDataPointDefault "missing" ;
    ada:uncertaintyLevel "missing" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/detectionLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimit" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/detectionLimitMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Detection Limit Method" ;
    schema1:valueName "detectionLimitMethod" ;
    ada:dataType "uri" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/isobaricInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Isobaric Interference Corrections Applied" ;
    schema1:valueName "isobaricInterferenceCorrectionsApplied" ;
    ada:dataType "boolean" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "uri" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/massResolutionPerAnalyte> a schema1:PropertyValueSpecification ;
    schema1:name "Mass Resolution per Analyte" ;
    schema1:valueName "massResolutionPerAnalyte" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/monitoredIsotopes> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Monitored Isotopes" ;
    schema1:valueName "monitoredIsotopes" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/normalizationStandardsBasedCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Normalization / Standards-Based Correction" ;
    schema1:valueName "normalizationStandardsBasedCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laQicpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/massResolutionSetting> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Unit resolution (quadrupole fixed)" ;
    schema1:name "Mass Resolution Setting" ;
    schema1:valueName "massResolutionSetting" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/plasmaMakeUpGasAdditionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N₂ or Ar mixed (same protocol as glass)" ;
    schema1:name "Plasma / Make-up Gas Addition" ;
    schema1:valueName "plasmaMakeUpGasAdditionDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "In situ — polished epoxy mount (same capsule section as glass protocol)" ;
    schema1:name "Sample Form / Analytical Substrate" ;
    schema1:valueName "sampleFormAnalyticalSubstrateDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/spikeOutlierFilteringApproachDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Same approach as glass; Au spike identification critical for determining solubility vs. nugget contribution" ;
    schema1:name "Spike / Outlier Filtering Approach" ;
    schema1:valueName "spikeOutlierFilteringApproachDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign> a schema1:PropertyValue ;
    schema1:name "Multi-Run Sequential Analysis Design" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign> ;
    schema1:value "Single spot per location (sulfides; same acquisition parameters as glass but 20 µm spot)" .


```


### laQicpmsUPbTAPP example Liu2016
laQicpmsUPbTAPP instance derived from Liu et al. 2016 (M&PS 51) Tissint martian meteorite Silicates, oxides & glass Spot analysis LA-Q-ICP-MS Virginia Tech.
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
  "@id": "ex:laQicpmsUPbTAPP-Liu2016",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "laQicpmsUPb protocol — Liu2016",
  "schema:description": "Paper broadly follows Udry et al. (2012) and Pernet-Fisher et al. (2014) for procedure; two IS approaches used for different mineral phases (oxide-sum for silicates; EMP CaO for phosphate); 90 µm spot used on some olivines to evaluate whether low REE signals result from insufficient sampling volume",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-ICP-MS",
      "schema:name": "LA-ICP-MS (193 nm excimer laser + ICP-MS; top-level technique)"
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
          "@id": "ada:parameter/laQicpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault",
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
        "Laser Ablation System",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
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
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/laQicpmsUPbTAPP/laserEnergyDefault",
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
      "ada:laserFluenceDefault": "7–10 J/m² (stated in paper; units as written; likely a typographic error for J/cm²)",
      "ada:laserRepetitionRateDefault": "5 Hz",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
    },
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
          "schema:name": "missing"
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
          "schema:name": "missing"
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
          "schema:name": "missing"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
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
  "ada:analysisSequenceDefault": "NIST 610 glass standard analyzed before and after every session; unknowns in between",
  "ada:backgroundCountTimeDefault": "50 s (background counted for 50 s before each LA-ICP-MS analysis)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign"
        }
      ],
      "schema:name": "Multi-Run Sequential Analysis Design",
      "schema:value": "Single spot analysis per location"
    }
  ],
  "ada:internalStandardApproach": "Normalization to 100 wt% oxide total (for silicates and oxides)",
  "ada:internalStandardElement": "None (oxide sum normalization, 100 wt% total)",
  "ada:elementalFractionationCorrection": [
    "External calibration using NIST 610 glass standard analyzed before and after session; oxide-sum normalization corrects for ablation yield variation; no explicit downhole fractionation correction described"
  ],
  "ada:signalIntegrationIntervalMethod": "Time-lapse plots of each spot examined; only the plateau region used to quantify trace element abundances",
  "ada:blankBackgroundCorrectionMethod": "50 s background measurement before each analysis; background subtracted (method not explicitly described beyond counting duration)",
  "ada:primaryStandardNameDefault": "NIST 610 glass standard",
  "ada:calibrationMeasurementFrequency": "NIST 610 glass standard analyzed before and after every session",
  "schema:actionProcess": {
    "@type": [
      "schema:HowTo"
    ],
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
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 3
      }
    ]
  },
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ablationSpotDurationDefault": -9999,
  "ada:ageModelDefault": "missing",
  "ada:carrierGasFlowRateDefault": "missing",
  "ada:inheritedOrInitialSignalCorrectionDefault": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
  "ada:signalCollectionMode": "missing",
  "ada:targetSelectionCriteriaDefault": "missing",
  "ada:totalIntegrationTimePerOutputDataPointDefault": "missing",
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS-UPb/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:laQicpmsUPbTAPP-Liu2016",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "laQicpmsUPb protocol \u2014 Liu2016",
  "schema:description": "Paper broadly follows Udry et al. (2012) and Pernet-Fisher et al. (2014) for procedure; two IS approaches used for different mineral phases (oxide-sum for silicates; EMP CaO for phosphate); 90 \u00b5m spot used on some olivines to evaluate whether low REE signals result from insufficient sampling volume",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-ICP-MS",
      "schema:name": "LA-ICP-MS (193 nm excimer laser + ICP-MS; top-level technique)"
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
          "@id": "ada:parameter/laQicpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault",
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
        "Laser Ablation System",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
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
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/laQicpmsUPbTAPP/laserEnergyDefault",
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
      "ada:laserFluenceDefault": "7\u201310 J/m\u00b2 (stated in paper; units as written; likely a typographic error for J/cm\u00b2)",
      "ada:laserRepetitionRateDefault": "5 Hz",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
    },
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
          "schema:name": "missing"
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
          "schema:name": "missing"
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
          "schema:name": "missing"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
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
  "ada:analysisSequenceDefault": "NIST 610 glass standard analyzed before and after every session; unknowns in between",
  "ada:backgroundCountTimeDefault": "50 s (background counted for 50 s before each LA-ICP-MS analysis)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign"
        }
      ],
      "schema:name": "Multi-Run Sequential Analysis Design",
      "schema:value": "Single spot analysis per location"
    }
  ],
  "ada:internalStandardApproach": "Normalization to 100 wt% oxide total (for silicates and oxides)",
  "ada:internalStandardElement": "None (oxide sum normalization, 100 wt% total)",
  "ada:elementalFractionationCorrection": [
    "External calibration using NIST 610 glass standard analyzed before and after session; oxide-sum normalization corrects for ablation yield variation; no explicit downhole fractionation correction described"
  ],
  "ada:signalIntegrationIntervalMethod": "Time-lapse plots of each spot examined; only the plateau region used to quantify trace element abundances",
  "ada:blankBackgroundCorrectionMethod": "50 s background measurement before each analysis; background subtracted (method not explicitly described beyond counting duration)",
  "ada:primaryStandardNameDefault": "NIST 610 glass standard",
  "ada:calibrationMeasurementFrequency": "NIST 610 glass standard analyzed before and after every session",
  "schema:actionProcess": {
    "@type": [
      "schema:HowTo"
    ],
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
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 3
      }
    ]
  },
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ablationSpotDurationDefault": -9999,
  "ada:ageModelDefault": "missing",
  "ada:carrierGasFlowRateDefault": "missing",
  "ada:inheritedOrInitialSignalCorrectionDefault": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
  "ada:signalCollectionMode": "missing",
  "ada:targetSelectionCriteriaDefault": "missing",
  "ada:totalIntegrationTimePerOutputDataPointDefault": "missing",
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

ex:laQicpmsUPbTAPP-Liu2016 a cdi:Activity,
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
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign> ;
    schema1:datePublished "missing" ;
    schema1:description "Paper broadly follows Udry et al. (2012) and Pernet-Fisher et al. (2014) for procedure; two IS approaches used for different mineral phases (oxide-sum for silicates; EMP CaO for phosphate); 90 µm spot used on some olivines to evaluate whether low REE signals result from insufficient sampling volume" ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "ICPMS" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Collision Reaction Cell" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Torch" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "ICP Source" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Interface Cone" ;
                    schema1:name "missing" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "Agilent 7500ce ICP-MS" ] ;
            schema1:name "example instrumentName" ],
        [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/laserEnergyDefault> ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "Laser Ablation System" ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "GeoLasPro (193 nm Excimer laser-ablation system; manufacturer not stated by name; GeoLasPro is a Lambda Physik/Coherent product)" ] ;
            schema1:name "example instrumentName" ;
            ada:laserFluenceDefault "7–10 J/m² (stated in paper; units as written; likely a typographic error for J/cm²)" ;
            ada:laserRepetitionRateDefault "5 Hz" ;
            ada:laserSpotGeometryDefault "24 and 32 µm diameter (commonly used for silicates and glass); 90 µm (some olivine analyses to evaluate low REE signal sampling)" ;
            ada:laserType "193 nm Excimer (ArF excimer)" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "Department of Geosciences, Virginia Tech" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "LA-ICP-MS (193 nm excimer laser + ICP-MS; top-level technique)" ;
            schema1:termCode "LA-ICP-MS" ] ;
    schema1:name "laQicpmsUPb protocol — Liu2016" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Martian meteorite (Tissint) silicates, oxides, and glass: olivine, low-Ca pyroxene, augite, maskelynite, Fe-Ti-Cr oxides, shock melt glass, fusion crust" ],
                <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault> ] ;
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
    ada:ageModelDefault "missing" ;
    ada:analysisSequenceDefault "NIST 610 glass standard analyzed before and after every session; unknowns in between" ;
    ada:backgroundCountTimeDefault "50 s (background counted for 50 s before each LA-ICP-MS analysis)" ;
    ada:blankBackgroundCorrectionMethod "50 s background measurement before each analysis; background subtracted (method not explicitly described beyond counting duration)" ;
    ada:calibrationMeasurementFrequency "NIST 610 glass standard analyzed before and after every session" ;
    ada:carrierGasFlowRateDefault "missing" ;
    ada:elementalFractionationCorrection "External calibration using NIST 610 glass standard analyzed before and after session; oxide-sum normalization corrects for ablation yield variation; no explicit downhole fractionation correction described" ;
    ada:inheritedOrInitialSignalCorrectionDefault "missing" ;
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
    ada:totalIntegrationTimePerOutputDataPointDefault "missing" ;
    ada:uncertaintyLevel "missing" ;
    bios:computationalTool [ schema1:name "AMS ver. 1.0 (Mutchler et al. 2008; Analysis Management System, stand-alone software)" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/laserEnergyDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 150 ;
    schema1:description "150 mJ output energy" ;
    schema1:name "Laser Energy" ;
    schema1:valueName "laserEnergyDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "In situ — polished thin section (Tissint sections: Tata-2-C3, Tata-3-C2, UT1, UT3)" ;
    schema1:name "Sample Form / Analytical Substrate" ;
    schema1:valueName "sampleFormAnalyticalSubstrateDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign> a schema1:PropertyValue ;
    schema1:name "Multi-Run Sequential Analysis Design" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign> ;
    schema1:value "Single spot analysis per location" .


```


### laQicpmsUPbTAPP example Liu2016-2
laQicpmsUPbTAPP instance derived from Liu et al. 2016 (M&PS 51) Tissint martian meteorite Phosphate (merrillite) Spot analysis LA-Q-ICP-MS Virginia Tech.
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
  "@id": "ex:laQicpmsUPbTAPP-Liu2016-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "laQicpmsUPb protocol — Liu2016-2",
  "schema:description": "N/A — see silicate column for general notes",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-ICP-MS",
      "schema:name": "LA-ICP-MS (same as silicate protocol)"
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
          "@id": "ada:parameter/laQicpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault",
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
        "Laser Ablation System",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
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
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/laQicpmsUPbTAPP/laserEnergyDefault",
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
      "ada:laserFluenceDefault": "7–10 J/m² (same as silicate protocol)",
      "ada:laserRepetitionRateDefault": "5 Hz",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
    },
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
          "schema:name": "missing"
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
          "schema:name": "missing"
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
          "schema:name": "missing"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
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
  "ada:analysisSequenceDefault": "Same as silicate protocol",
  "ada:backgroundCountTimeDefault": "50 s (same as silicate protocol)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign"
        }
      ],
      "schema:name": "Multi-Run Sequential Analysis Design",
      "schema:value": "Single spot analysis per location"
    }
  ],
  "ada:internalStandardApproach": "Single element IS: EMP CaO concentration used; LA-ICP-MS 40Ca counts normalized to CaO from EMP analysis at the same spot",
  "ada:internalStandardElement": "40Ca; CaO wt% from EMP at the analysis spot",
  "ada:elementalFractionationCorrection": [
    "External calibration using NIST 610; EMP CaO as IS corrects for ablation yield; no explicit downhole correction described"
  ],
  "ada:signalIntegrationIntervalMethod": "Time-lapse plots examined; only plateau region used (same as silicate protocol)",
  "ada:blankBackgroundCorrectionMethod": "50 s background measurement before each analysis (same as silicate protocol)",
  "ada:primaryStandardNameDefault": "NIST 610 glass standard",
  "ada:calibrationMeasurementFrequency": "NIST 610 analyzed before and after every session (same as silicate protocol)",
  "schema:actionProcess": {
    "@type": [
      "schema:HowTo"
    ],
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
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 3
      }
    ]
  },
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ablationSpotDurationDefault": -9999,
  "ada:ageModelDefault": "missing",
  "ada:carrierGasFlowRateDefault": "missing",
  "ada:inheritedOrInitialSignalCorrectionDefault": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
  "ada:signalCollectionMode": "missing",
  "ada:targetSelectionCriteriaDefault": "missing",
  "ada:totalIntegrationTimePerOutputDataPointDefault": "missing",
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS-UPb/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:laQicpmsUPbTAPP-Liu2016-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "laQicpmsUPb protocol \u2014 Liu2016-2",
  "schema:description": "N/A \u2014 see silicate column for general notes",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-ICP-MS",
      "schema:name": "LA-ICP-MS (same as silicate protocol)"
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
          "@id": "ada:parameter/laQicpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault",
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
        "Laser Ablation System",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
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
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/laQicpmsUPbTAPP/laserEnergyDefault",
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
      "ada:laserFluenceDefault": "7\u201310 J/m\u00b2 (same as silicate protocol)",
      "ada:laserRepetitionRateDefault": "5 Hz",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
    },
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
          "schema:name": "missing"
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
          "schema:name": "missing"
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
          "schema:name": "missing"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
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
  "ada:analysisSequenceDefault": "Same as silicate protocol",
  "ada:backgroundCountTimeDefault": "50 s (same as silicate protocol)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign"
        }
      ],
      "schema:name": "Multi-Run Sequential Analysis Design",
      "schema:value": "Single spot analysis per location"
    }
  ],
  "ada:internalStandardApproach": "Single element IS: EMP CaO concentration used; LA-ICP-MS 40Ca counts normalized to CaO from EMP analysis at the same spot",
  "ada:internalStandardElement": "40Ca; CaO wt% from EMP at the analysis spot",
  "ada:elementalFractionationCorrection": [
    "External calibration using NIST 610; EMP CaO as IS corrects for ablation yield; no explicit downhole correction described"
  ],
  "ada:signalIntegrationIntervalMethod": "Time-lapse plots examined; only plateau region used (same as silicate protocol)",
  "ada:blankBackgroundCorrectionMethod": "50 s background measurement before each analysis (same as silicate protocol)",
  "ada:primaryStandardNameDefault": "NIST 610 glass standard",
  "ada:calibrationMeasurementFrequency": "NIST 610 analyzed before and after every session (same as silicate protocol)",
  "schema:actionProcess": {
    "@type": [
      "schema:HowTo"
    ],
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
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 3
      }
    ]
  },
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ablationSpotDurationDefault": -9999,
  "ada:ageModelDefault": "missing",
  "ada:carrierGasFlowRateDefault": "missing",
  "ada:inheritedOrInitialSignalCorrectionDefault": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
  "ada:signalCollectionMode": "missing",
  "ada:targetSelectionCriteriaDefault": "missing",
  "ada:totalIntegrationTimePerOutputDataPointDefault": "missing",
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

ex:laQicpmsUPbTAPP-Liu2016-2 a cdi:Activity,
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
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign> ;
    schema1:datePublished "missing" ;
    schema1:description "N/A — see silicate column for general notes" ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "ICPMS" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Collision Reaction Cell" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Interface Cone" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "ICP Source" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Torch" ;
                    schema1:name "missing" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "Agilent 7500ce ICP-MS" ] ;
            schema1:name "example instrumentName" ],
        [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/laserEnergyDefault> ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "Laser Ablation System" ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "GeoLasPro 193 nm Excimer laser-ablation system (same as silicate protocol)" ] ;
            schema1:name "example instrumentName" ;
            ada:laserFluenceDefault "7–10 J/m² (same as silicate protocol)" ;
            ada:laserRepetitionRateDefault "5 Hz" ;
            ada:laserSpotGeometryDefault "~24 µm diameter" ;
            ada:laserType "193 nm Excimer (ArF excimer)" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "Department of Geosciences, Virginia Tech" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "LA-ICP-MS (same as silicate protocol)" ;
            schema1:termCode "LA-ICP-MS" ] ;
    schema1:name "laQicpmsUPb protocol — Liu2016-2" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Martian meteorite (Tissint) phosphate: sodium-merrillite" ],
                <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault> ] ;
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
    ada:ageModelDefault "missing" ;
    ada:analysisSequenceDefault "Same as silicate protocol" ;
    ada:backgroundCountTimeDefault "50 s (same as silicate protocol)" ;
    ada:blankBackgroundCorrectionMethod "50 s background measurement before each analysis (same as silicate protocol)" ;
    ada:calibrationMeasurementFrequency "NIST 610 analyzed before and after every session (same as silicate protocol)" ;
    ada:carrierGasFlowRateDefault "missing" ;
    ada:elementalFractionationCorrection "External calibration using NIST 610; EMP CaO as IS corrects for ablation yield; no explicit downhole correction described" ;
    ada:inheritedOrInitialSignalCorrectionDefault "missing" ;
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
    ada:totalIntegrationTimePerOutputDataPointDefault "missing" ;
    ada:uncertaintyLevel "missing" ;
    bios:computationalTool [ schema1:name "AMS ver. 1.0 (Mutchler et al. 2008)" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/laserEnergyDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 150 ;
    schema1:description "150 mJ output energy" ;
    schema1:name "Laser Energy" ;
    schema1:valueName "laserEnergyDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "In situ — polished thin section (same sections as silicate protocol)" ;
    schema1:name "Sample Form / Analytical Substrate" ;
    schema1:valueName "sampleFormAnalyticalSubstrateDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign> a schema1:PropertyValue ;
    schema1:name "Multi-Run Sequential Analysis Design" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign> ;
    schema1:value "Single spot analysis per location" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: LA-Q-ICP-MS U-Pb Geochronology TAPP (laQicpmsUPbTAPP)
description: Laser-ablation quadrupole ICP-MS U-Pb geochronology extension of the
  base TAPP definition, generated from TAPPS20260813/Current TAPPs/LA-Q-ICP-MS_UPb_TAPP_v16.csv
  via the path-driven pipeline.
allOf:
- $ref: https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/BaseSchema/tappDefinition/schema.yaml
- type: object
  properties:
    schema:name:
      type: string
      readOnly: true
    schema:measurementTechnique:
      type: array
      items:
        type: object
        properties:
          schema:termCode:
            description: Top-level analytical technique identifier.
            type: string
            enum:
            - LA-ICP-MS
            - LA-ICP-OES
            - LA-MC-ICP-MS
            - LA-ICP-ToF-MS
            - LA-ICP-MS/MS
            - missing
            readOnly: true
    schema:creator:
      type: object
      properties:
        schema:name:
          type: string
          readOnly: true
    schema:location:
      type: object
      properties:
        schema:name:
          description: Name of the laboratory or institution hosting the instrument.
          type: string
        schema:identifier:
          description: Persistent identifier for the laboratory (e.g., ROR ID).
          type: string
    schema:datePublished:
      type: string
      readOnly: true
    schema:funding:
      type: array
      items:
        type: object
        properties:
          schema:name:
            type: string
            readOnly: true
    schema:relatedLink:
      type: array
      items:
        type: object
        allOf:
        - if:
            properties:
              schema:linkRelationship:
                const: techniquePublication
            required:
            - schema:linkRelationship
          then:
            properties:
              schema:target:
                type: object
                properties:
                  schema:name:
                    type: string
                    readOnly: true
        - if:
            properties:
              schema:linkRelationship:
                const: coupledTechnique
            required:
            - schema:linkRelationship
          then:
            properties:
              schema:target:
                type: object
                properties:
                  schema:name:
                    description: "Other analytical techniques applied to the same
                      sample(s) whose results are intended to be interpreted together
                      with data from this procedure. Document coupling with any technique
                      whose results are functionally linked to this dataset \u2014
                      providing calibration inputs, complementary spatial context,
                      or required companion measurements. Use the same controlled
                      vocabulary as the Technique field. Enter \"None\" if no coupling
                      is intended."
                    anyOf:
                    - type: string
                      enum:
                      - EPMA
                      - SIMS
                      - ICP-MS (solution)
                      - Noble Gas MS
                      - None
                      - N/A
                      - missing
                    - type: string
                  schema:description:
                    description: "Description of how this procedure is coupled with
                      the technique(s) listed above. Include: (1) the functional relationship
                      \u2014 what data or context flows between techniques, or how
                      results are combined (e.g. which output from the coupled technique
                      serves as input to data reduction for this technique); and (2)
                      the analytical sequence \u2014 which technique is performed
                      first and why (e.g. non-destructive before destructive). Required
                      when Coupled Technique(s) is not \"None\"."
                    type: string
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
                              and procedure matching.
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
                        const: ada:parameter/laQicpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault
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
    ada:samplingUnit:
      description: "The physical subdivision of the sample to which one row of reported
        values corresponds \u2014 the unit that is analysed and reported, as distinct
        from the sample as a whole. State the unit type at procedure level and the
        units actually analysed at analysis level. Where units nest (e.g. confined
        tracks within grains), state both levels."
      anyOf:
      - type: string
        enum:
        - Whole sample
        - Aliquot
        - Grain
        - Spot
        - Analysis point
        - Phase
        - Sub-volume
        - Region of interest
        - N/A
        - None
        - missing
      - type: string
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
                            const: ada:parameter/laQicpmsUPbTAPP/fusionFluxAndDilutionRatioDefault
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
                      - title: Pre-Ablation Surface Treatment
                        description: Procedure applied immediately before each analysis
                          to remove surface contamination or condition the sample
                          surface. Distinct from general sample preparation. For spot
                          analysis, pre-ablation pulses are discarded before signal
                          acquisition begins. For mapping, this step is typically
                          omitted as the large area ablated averages out surface effects.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/laQicpmsUPbTAPP/preAblationSurfaceTreatmentDefault
                          '@type':
                            const:
                            - schema:PropertyValueSpecification
                          schema:valueName:
                            const: preAblationSurfaceTreatmentDefault
                          schema:name:
                            const: Pre-Ablation Surface Treatment
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
                        title: Fusion Flux and Dilution Ratio
                        description: For procedures using fused glass, the flux type
                          and sample:flux dilution ratio used to prepare the analytical
                          glass.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/laQicpmsUPbTAPP/fusionFluxAndDilutionRatioDefault
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
                        title: Pre-Ablation Surface Treatment
                        description: Procedure applied immediately before each analysis
                          to remove surface contamination or condition the sample
                          surface. Distinct from general sample preparation. For spot
                          analysis, pre-ablation pulses are discarded before signal
                          acquisition begins. For mapping, this step is typically
                          omitted as the large area ablated averages out surface effects.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/laQicpmsUPbTAPP/preAblationSurfaceTreatmentDefault
                          '@type':
                            const:
                            - schema:PropertyValueSpecification
                          schema:valueName:
                            const: preAblationSurfaceTreatmentDefault
                          schema:name:
                            const: Pre-Ablation Surface Treatment
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
                  schema:description:
                    description: Description of how samples were prepared for analysis
                      (mounting, polishing, coating, fusion procedure, etc.).
                    anyOf:
                    - type: string
                    - type: array
                      items:
                        type: string
                  ada:chemicalAbrasionConditions:
                    description: 'Annealing and partial-dissolution conditions applied
                      to mitigate Pb loss before analysis, following Mattinson (2005):
                      annealing temperature and duration, and the acid, temperature
                      and duration of the partial-dissolution step. Condon et al.
                      (2024) require these where chemical abrasion was applied, and
                      state that it generally should be for zircon. Record ''None''
                      where grains were analysed untreated, since the absence of treatment
                      materially affects how discordance should be read.'
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
                          const: ada:parameter/laQicpmsUPbTAPP/guardElectrode
                        '@type':
                          const:
                          - schema:PropertyValue
                        schema:propertyID:
                          const:
                          - '@id': ada:parameter/laQicpmsUPbTAPP/guardElectrode
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
                            const: ada:parameter/laQicpmsUPbTAPP/guardElectrode
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/laQicpmsUPbTAPP/guardElectrode
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
                            const: ada:parameter/laQicpmsUPbTAPP/signalSmoothingDefault
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
                            const: ada:parameter/laQicpmsUPbTAPP/spikeOutlierFilteringApproachDefault
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
                            const: ada:parameter/laQicpmsUPbTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault
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
                            const: ada:parameter/laQicpmsUPbTAPP/isotopeDilutionDataReductionMethod
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/laQicpmsUPbTAPP/isotopeDilutionDataReductionMethod
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
                      - title: Calibration Factor and Determination Method
                        description: 'An externally-calibrated factor that converts
                          the measured quantity into the reported quantity, how it
                          was determined, and its uncertainty. Applies where the conversion
                          depends on a factor calibrated against a reference of independently
                          known value, rather than on the instrument response alone.
                          Distinct from the fields that name the calibration material
                          and that state which approach applies to which analyte,
                          where the technique has them: this field records the resulting
                          factor itself.'
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/laQicpmsUPbTAPP/calibrationFactorAndDeterminationMethodDefault
                          '@type':
                            const:
                            - schema:PropertyValueSpecification
                          schema:valueName:
                            const: calibrationFactorAndDeterminationMethodDefault
                          schema:name:
                            const: Calibration Factor and Determination Method
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
                      - title: Analysis Inclusion and Rejection Criteria
                        description: 'The rules determining which individual analyses
                          contribute to a reported aggregate result, together with
                          the outcome of applying them: how many analyses were acquired,
                          how many were included, and on what grounds any were excluded.
                          Distinct from within-analysis outlier filtering, which removes
                          anomalous points inside a single analysis: this field decides
                          which whole analyses enter the reported value. Criteria
                          and outcome are combined in one field because neither is
                          interpretable without the other, following the precision/accuracy
                          precedent.'
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/laQicpmsUPbTAPP/analysisInclusionAndRejectionCriteria
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/laQicpmsUPbTAPP/analysisInclusionAndRejectionCriteria
                          schema:name:
                            const: Analysis Inclusion and Rejection Criteria
                          schema:value:
                            type: string
                        required:
                        - '@id'
                        - '@type'
                        - schema:propertyID
                        - schema:name
                        - schema:value
                      - title: Intermediate Daughter Disequilibrium Correction
                        description: "Correction for initial disequilibrium in intermediate
                          daughter products of the U decay chains \u2014 principally
                          230Th, and where relevant 231Pa \u2014 together with the
                          Th/U or Pa/U partitioning value assumed and its source.
                          Unique to U-Pb among dating systems, because the chains
                          are long enough for intermediate-daughter disequilibrium
                          at crystallisation to bias the 206Pb/238U date, most severely
                          in young samples. Record 'None' with a justification where
                          no correction was applied. Condon et al. (2024) write \"we
                          recommend these dates be reported corrected for initial
                          230Th and 231Pa daughter isotope disequilibrium\" \u2014
                          recommended rather than required, hence Advanced."
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/laQicpmsUPbTAPP/intermediateDaughterDisequilibriumCorrection
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/laQicpmsUPbTAPP/intermediateDaughterDisequilibriumCorrection
                          schema:name:
                            const: Intermediate Daughter Disequilibrium Correction
                          schema:value:
                            type: string
                        required:
                        - '@id'
                        - '@type'
                        - schema:propertyID
                        - schema:name
                        - schema:value
                        readOnly: true
                      - title: Constants and Reference Values Used
                        description: Physical constants and reference values used
                          in data reduction to calculate the final reported quantity
                          (e.g., decay constants for age calculation, standard isotope
                          ratios, or other citable reference values used in a correction
                          or calculation), together with their source. Distinct from
                          the Group 6 reference-material fields, which document accepted
                          values for specific calibration/validation materials rather
                          than universal physical constants. Record "None" if no citable,
                          revisable physical constants feed into this procedure's
                          data reduction.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/laQicpmsUPbTAPP/constantsAndReferenceValuesUsedDefault
                          '@type':
                            const:
                            - schema:PropertyValueSpecification
                          schema:valueName:
                            const: constantsAndReferenceValuesUsedDefault
                          schema:name:
                            const: Constants and Reference Values Used
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
                      - title: Faraday Cup Gain Calibration Method
                        description: ''
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/laQicpmsUPbTAPP/faradayCupGainCalibrationMethod
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/laQicpmsUPbTAPP/faradayCupGainCalibrationMethod
                          schema:name:
                            const: Faraday Cup Gain Calibration Method
                          schema:value:
                            type: string
                        required:
                        - '@id'
                        - '@type'
                        - schema:propertyID
                        - schema:name
                        - schema:value
                        readOnly: true
                      - title: Double-Spike Inversion Algorithm
                        description: ''
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/laQicpmsUPbTAPP/doubleSpikeInversionAlgorithm
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/laQicpmsUPbTAPP/doubleSpikeInversionAlgorithm
                          schema:name:
                            const: Double-Spike Inversion Algorithm
                          schema:value:
                            type: string
                        required:
                        - '@id'
                        - '@type'
                        - schema:propertyID
                        - schema:name
                        - schema:value
                        readOnly: true
                      - title: Normalization/Standards-Based Correction
                        description: ''
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/laQicpmsUPbTAPP/normalizationStandardsBasedCorrection
                          '@type':
                            const:
                            - schema:PropertyValueSpecification
                          schema:valueName:
                            const: normalizationStandardsBasedCorrection
                          schema:name:
                            const: Normalization/Standards-Based Correction
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
                            const: ada:parameter/laQicpmsUPbTAPP/signalSmoothingDefault
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
                            const: ada:parameter/laQicpmsUPbTAPP/spikeOutlierFilteringApproachDefault
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
                            const: ada:parameter/laQicpmsUPbTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault
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
                            const: ada:parameter/laQicpmsUPbTAPP/isotopeDilutionDataReductionMethod
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/laQicpmsUPbTAPP/isotopeDilutionDataReductionMethod
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
                        title: Calibration Factor and Determination Method
                        description: 'An externally-calibrated factor that converts
                          the measured quantity into the reported quantity, how it
                          was determined, and its uncertainty. Applies where the conversion
                          depends on a factor calibrated against a reference of independently
                          known value, rather than on the instrument response alone.
                          Distinct from the fields that name the calibration material
                          and that state which approach applies to which analyte,
                          where the technique has them: this field records the resulting
                          factor itself.'
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/laQicpmsUPbTAPP/calibrationFactorAndDeterminationMethodDefault
                          '@type':
                            const:
                            - schema:PropertyValueSpecification
                          schema:valueName:
                            const: calibrationFactorAndDeterminationMethodDefault
                          schema:name:
                            const: Calibration Factor and Determination Method
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
                        title: Analysis Inclusion and Rejection Criteria
                        description: 'The rules determining which individual analyses
                          contribute to a reported aggregate result, together with
                          the outcome of applying them: how many analyses were acquired,
                          how many were included, and on what grounds any were excluded.
                          Distinct from within-analysis outlier filtering, which removes
                          anomalous points inside a single analysis: this field decides
                          which whole analyses enter the reported value. Criteria
                          and outcome are combined in one field because neither is
                          interpretable without the other, following the precision/accuracy
                          precedent.'
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/laQicpmsUPbTAPP/analysisInclusionAndRejectionCriteria
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/laQicpmsUPbTAPP/analysisInclusionAndRejectionCriteria
                          schema:name:
                            const: Analysis Inclusion and Rejection Criteria
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
                        title: Intermediate Daughter Disequilibrium Correction
                        description: "Correction for initial disequilibrium in intermediate
                          daughter products of the U decay chains \u2014 principally
                          230Th, and where relevant 231Pa \u2014 together with the
                          Th/U or Pa/U partitioning value assumed and its source.
                          Unique to U-Pb among dating systems, because the chains
                          are long enough for intermediate-daughter disequilibrium
                          at crystallisation to bias the 206Pb/238U date, most severely
                          in young samples. Record 'None' with a justification where
                          no correction was applied. Condon et al. (2024) write \"we
                          recommend these dates be reported corrected for initial
                          230Th and 231Pa daughter isotope disequilibrium\" \u2014
                          recommended rather than required, hence Advanced."
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/laQicpmsUPbTAPP/intermediateDaughterDisequilibriumCorrection
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/laQicpmsUPbTAPP/intermediateDaughterDisequilibriumCorrection
                          schema:name:
                            const: Intermediate Daughter Disequilibrium Correction
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
                        title: Constants and Reference Values Used
                        description: Physical constants and reference values used
                          in data reduction to calculate the final reported quantity
                          (e.g., decay constants for age calculation, standard isotope
                          ratios, or other citable reference values used in a correction
                          or calculation), together with their source. Distinct from
                          the Group 6 reference-material fields, which document accepted
                          values for specific calibration/validation materials rather
                          than universal physical constants. Record "None" if no citable,
                          revisable physical constants feed into this procedure's
                          data reduction.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/laQicpmsUPbTAPP/constantsAndReferenceValuesUsedDefault
                          '@type':
                            const:
                            - schema:PropertyValueSpecification
                          schema:valueName:
                            const: constantsAndReferenceValuesUsedDefault
                          schema:name:
                            const: Constants and Reference Values Used
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
                        title: Faraday Cup Gain Calibration Method
                        description: ''
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/laQicpmsUPbTAPP/faradayCupGainCalibrationMethod
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/laQicpmsUPbTAPP/faradayCupGainCalibrationMethod
                          schema:name:
                            const: Faraday Cup Gain Calibration Method
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
                        title: Double-Spike Inversion Algorithm
                        description: ''
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/laQicpmsUPbTAPP/doubleSpikeInversionAlgorithm
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/laQicpmsUPbTAPP/doubleSpikeInversionAlgorithm
                          schema:name:
                            const: Double-Spike Inversion Algorithm
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
                        title: Normalization/Standards-Based Correction
                        description: ''
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/laQicpmsUPbTAPP/normalizationStandardsBasedCorrection
                          '@type':
                            const:
                            - schema:PropertyValueSpecification
                          schema:valueName:
                            const: normalizationStandardsBasedCorrection
                          schema:name:
                            const: Normalization/Standards-Based Correction
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
    ada:targetSelectionCriteriaDefault:
      description: "The rules governing which part of the sample is analysed, and
        why. Covers the criteria applied when choosing grains, aliquots, spots, or
        a region of interest \u2014 size, morphology, clarity, freedom from inclusions
        or alteration, phase identity, or spatial position. Distinct from Target Material,
        which states the material type the procedure is designed for: this field states
        how, within such a sample, the analysed portion is picked out."
      type: string
    schema:additionalProperty:
      type: array
      items:
        anyOf:
        - title: Pre-Analysis Imaging and Screening
          description: Imaging or other characterisation performed before the measurement
            in order to select or locate the analysed target, including the technique,
            instrument and settings used, and how individual analyses are linked back
            to the images. Distinct from any imaging the procedure performs as its
            own measurement. Where the imaging is performed on a separate instrument,
            it should also be recorded in the Group 1 coupling fields.
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreeningDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: preAnalysisImagingAndScreeningDefault
            schema:name:
              const: Pre-Analysis Imaging and Screening
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
        - title: Transect Rate, Mapping Rate or Step Size
          description: "For continuous line scan (transect) and raster mapping: the
            stage translation speed in \xB5m s\u207B\xB9. This is the procedure-level
            parameter that, together with spot size and repetition rate, determines
            spatial resolution along the scan direction. For mapping, the mapping
            rate (mm\xB2 h\u207B\xB9) may be reported as an alternative when scan
            speed is session-variable. For stepped line profiles: the distance between
            successive spot positions in \xB5m."
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsUPbTAPP/transectRateMappingRateOrStepSizeDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: transectRateMappingRateOrStepSizeDefault
            schema:name:
              const: Transect Rate, Mapping Rate or Step Size
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
        - title: Plasma / Make-up Gas Addition
          description: "Additional gas(es) mixed into the carrier stream downstream
            of the ablation cell, with the procedure-registered target flow rate.
            Ar make-up gas is standard. Small N\u2082 additions can enhance sensitivity
            for some elements. If N\u2082 is not added, state \"None\" explicitly
            to distinguish from not reported."
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsUPbTAPP/plasmaMakeUpGasAdditionDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: plasmaMakeUpGasAdditionDefault
            schema:name:
              const: Plasma / Make-up Gas Addition
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
        - title: Instrument Warm-up / Session Duration Limit
          description: Minimum warm-up time required after plasma ignition before
            analyses begin, and any maximum session duration enforced to maintain
            stable operating conditions. These constraints are part of the procedure
            and cannot be varied by the analyst.
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsUPbTAPP/instrumentWarmUpSessionDurationLimit
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laQicpmsUPbTAPP/instrumentWarmUpSessionDurationLimit
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
              const: ada:parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign
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
              const: ada:parameter/laQicpmsUPbTAPP/uncertaintyPropagationMethodDefault
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
              const: ada:parameter/laQicpmsUPbTAPP/matrixOffsetCorrection
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laQicpmsUPbTAPP/matrixOffsetCorrection
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
        - title: Age Datum / Reference Epoch
          description: 'The zero point from which the reported age is measured, where
            this is not the present day, and the date it corresponds to. Record ''Present
            day'' where the conventional datum applies. Explicitly required wherever
            the datum is not the present: year of sample collection for luminescence
            (Mahan et al. 2023), end of irradiation for 40Ar/39Ar decay corrections
            (Schaen et al. 2021).'
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsUPbTAPP/ageDatumReferenceEpochDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: ageDatumReferenceEpochDefault
            schema:name:
              const: Age Datum / Reference Epoch
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
        - title: Discordance Definition and Values
          description: "How discordance between the 206Pb/238U, 207Pb/235U and 207Pb/206Pb
            chronometers is defined for this procedure, and the discordance values
            obtained. Several definitions are in circulation and they are not interchangeable,
            so the formula must be stated. Genuinely specific to U-Pb: it is the only
            system in routine use with two independent decay schemes in the same mineral,
            so agreement between them is an internal consistency test no other system
            can run. The rule for excluding discordant analyses, and how many were
            excluded, belong in Analysis Inclusion and Rejection Criteria. Condon
            et al. (2024) write that for samples older than a few hundred million
            years \"it is also useful to provide a measure of discordance\" \u2014
            useful and age-conditional rather than required, hence Advanced."
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsUPbTAPP/discordanceDefinitionAndValues
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laQicpmsUPbTAPP/discordanceDefinitionAndValues
            schema:name:
              const: Discordance Definition and Values
            schema:value:
              type: string
          required:
          - '@id'
          - '@type'
          - schema:propertyID
          - schema:name
          - schema:value
          readOnly: true
        - title: Error Correlation Between Reported Quantities
          description: The correlation coefficient between pairs of reported quantities
            whose uncertainties are not independent, together with the pair it applies
            to and how it was obtained. Concordia and isochron regressions cannot
            be reconstructed without it.
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsUPbTAPP/errorCorrelationBetweenReportedQuantitiesDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: errorCorrelationBetweenReportedQuantitiesDefault
            schema:name:
              const: Error Correlation Between Reported Quantities
            ada:dataType:
              const: number
            ada:fieldScope:
              const: session
            schema:readonlyValue:
              const: false
            ada:tier:
              const: R
            schema:unitText:
              const: dimensionless
          required:
          - '@id'
          - '@type'
          - schema:valueName
          - schema:name
          - ada:dataType
          - ada:fieldScope
        - title: E-scan Range
          description: ''
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsUPbTAPP/eScanRange
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laQicpmsUPbTAPP/eScanRange
            schema:name:
              const: E-scan Range
            schema:value:
              type: string
          required:
          - '@id'
          - '@type'
          - schema:propertyID
          - schema:name
          - schema:value
          readOnly: true
        - title: Triple Scanning Mode
          description: ''
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsUPbTAPP/tripleScanningMode
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laQicpmsUPbTAPP/tripleScanningMode
            schema:name:
              const: Triple Scanning Mode
            schema:value:
              type: string
          required:
          - '@id'
          - '@type'
          - schema:propertyID
          - schema:name
          - schema:value
          readOnly: true
        - title: Imaging
          description: ''
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsUPbTAPP/imaging
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: imaging
            schema:name:
              const: Imaging
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
        - title: Ablation Pit Depth/Ablation Rate
          description: ''
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsUPbTAPP/ablationPitDepthAblationRate
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: ablationPitDepthAblationRate
            schema:name:
              const: Ablation Pit Depth/Ablation Rate
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
        - title: "Make-up Gas Flow (L min\u207B\xB9)"
          description: ''
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsUPbTAPP/makeUpGasFlow
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: makeUpGasFlow
            schema:name:
              const: "Make-up Gas Flow (L min\u207B\xB9)"
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
        - title: Number of Blocks per Measurement
          description: ''
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsUPbTAPP/numberOfBlocksPerMeasurement
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: numberOfBlocksPerMeasurement
            schema:name:
              const: Number of Blocks per Measurement
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
        - title: Number of Cycles per Block
          description: ''
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsUPbTAPP/numberOfCyclesPerBlock
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: numberOfCyclesPerBlock
            schema:name:
              const: Number of Cycles per Block
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
        - title: Integration Time per Cycle
          description: ''
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsUPbTAPP/integrationTimePerCycle
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: integrationTimePerCycle
            schema:name:
              const: Integration Time per Cycle
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
        - title: IC Dead Time (ns)
          description: ''
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsUPbTAPP/icDeadTime
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: icDeadTime
            schema:name:
              const: IC Dead Time (ns)
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
        - title: Baseline Measurement Approach
          description: ''
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsUPbTAPP/baselineMeasurementApproach
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laQicpmsUPbTAPP/baselineMeasurementApproach
            schema:name:
              const: Baseline Measurement Approach
            schema:value:
              type: string
          required:
          - '@id'
          - '@type'
          - schema:propertyID
          - schema:name
          - schema:value
          readOnly: true
        - title: Other Information
          description: ''
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsUPbTAPP/otherInformation
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: otherInformation
            schema:name:
              const: Other Information
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
        - title: Mass Fractionation Law
          description: ''
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsUPbTAPP/massFractionationLaw
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laQicpmsUPbTAPP/massFractionationLaw
            schema:name:
              const: Mass Fractionation Law
            schema:value:
              type: string
          required:
          - '@id'
          - '@type'
          - schema:propertyID
          - schema:name
          - schema:value
          readOnly: true
        - title: Uncertainty Level and Propagation
          description: ''
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsUPbTAPP/uncertaintyLevelAndPropagation
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: uncertaintyLevelAndPropagation
            schema:name:
              const: Uncertainty Level and Propagation
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
        - title: Double-Spike Isotope Pair
          description: ''
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsUPbTAPP/doubleSpikeIsotopePair
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laQicpmsUPbTAPP/doubleSpikeIsotopePair
            schema:name:
              const: Double-Spike Isotope Pair
            schema:value:
              type: string
          required:
          - '@id'
          - '@type'
          - schema:propertyID
          - schema:name
          - schema:value
          readOnly: true
        - title: Double-Spike Mixing Ratio
          description: ''
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsUPbTAPP/doubleSpikeMixingRatio
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: doubleSpikeMixingRatio
            schema:name:
              const: Double-Spike Mixing Ratio
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
      allOf:
      - contains:
          title: Pre-Analysis Imaging and Screening
          description: Imaging or other characterisation performed before the measurement
            in order to select or locate the analysed target, including the technique,
            instrument and settings used, and how individual analyses are linked back
            to the images. Distinct from any imaging the procedure performs as its
            own measurement. Where the imaging is performed on a separate instrument,
            it should also be recorded in the Group 1 coupling fields.
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreeningDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: preAnalysisImagingAndScreeningDefault
            schema:name:
              const: Pre-Analysis Imaging and Screening
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
          title: Transect Rate, Mapping Rate or Step Size
          description: "For continuous line scan (transect) and raster mapping: the
            stage translation speed in \xB5m s\u207B\xB9. This is the procedure-level
            parameter that, together with spot size and repetition rate, determines
            spatial resolution along the scan direction. For mapping, the mapping
            rate (mm\xB2 h\u207B\xB9) may be reported as an alternative when scan
            speed is session-variable. For stepped line profiles: the distance between
            successive spot positions in \xB5m."
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsUPbTAPP/transectRateMappingRateOrStepSizeDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: transectRateMappingRateOrStepSizeDefault
            schema:name:
              const: Transect Rate, Mapping Rate or Step Size
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
          title: Plasma / Make-up Gas Addition
          description: "Additional gas(es) mixed into the carrier stream downstream
            of the ablation cell, with the procedure-registered target flow rate.
            Ar make-up gas is standard. Small N\u2082 additions can enhance sensitivity
            for some elements. If N\u2082 is not added, state \"None\" explicitly
            to distinguish from not reported."
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsUPbTAPP/plasmaMakeUpGasAdditionDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: plasmaMakeUpGasAdditionDefault
            schema:name:
              const: Plasma / Make-up Gas Addition
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
          title: Instrument Warm-up / Session Duration Limit
          description: Minimum warm-up time required after plasma ignition before
            analyses begin, and any maximum session duration enforced to maintain
            stable operating conditions. These constraints are part of the procedure
            and cannot be varied by the analyst.
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsUPbTAPP/instrumentWarmUpSessionDurationLimit
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laQicpmsUPbTAPP/instrumentWarmUpSessionDurationLimit
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
              const: ada:parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laQicpmsUPbTAPP/multiRunSequentialAnalysisDesign
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
              const: ada:parameter/laQicpmsUPbTAPP/uncertaintyPropagationMethodDefault
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
              const: ada:parameter/laQicpmsUPbTAPP/matrixOffsetCorrection
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laQicpmsUPbTAPP/matrixOffsetCorrection
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
          title: Age Datum / Reference Epoch
          description: 'The zero point from which the reported age is measured, where
            this is not the present day, and the date it corresponds to. Record ''Present
            day'' where the conventional datum applies. Explicitly required wherever
            the datum is not the present: year of sample collection for luminescence
            (Mahan et al. 2023), end of irradiation for 40Ar/39Ar decay corrections
            (Schaen et al. 2021).'
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsUPbTAPP/ageDatumReferenceEpochDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: ageDatumReferenceEpochDefault
            schema:name:
              const: Age Datum / Reference Epoch
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
          title: Discordance Definition and Values
          description: "How discordance between the 206Pb/238U, 207Pb/235U and 207Pb/206Pb
            chronometers is defined for this procedure, and the discordance values
            obtained. Several definitions are in circulation and they are not interchangeable,
            so the formula must be stated. Genuinely specific to U-Pb: it is the only
            system in routine use with two independent decay schemes in the same mineral,
            so agreement between them is an internal consistency test no other system
            can run. The rule for excluding discordant analyses, and how many were
            excluded, belong in Analysis Inclusion and Rejection Criteria. Condon
            et al. (2024) write that for samples older than a few hundred million
            years \"it is also useful to provide a measure of discordance\" \u2014
            useful and age-conditional rather than required, hence Advanced."
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsUPbTAPP/discordanceDefinitionAndValues
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laQicpmsUPbTAPP/discordanceDefinitionAndValues
            schema:name:
              const: Discordance Definition and Values
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
          title: Error Correlation Between Reported Quantities
          description: The correlation coefficient between pairs of reported quantities
            whose uncertainties are not independent, together with the pair it applies
            to and how it was obtained. Concordia and isochron regressions cannot
            be reconstructed without it.
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsUPbTAPP/errorCorrelationBetweenReportedQuantitiesDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: errorCorrelationBetweenReportedQuantitiesDefault
            schema:name:
              const: Error Correlation Between Reported Quantities
            ada:dataType:
              const: number
            ada:fieldScope:
              const: session
            schema:readonlyValue:
              const: false
            ada:tier:
              const: R
            schema:unitText:
              const: dimensionless
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
          title: E-scan Range
          description: ''
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsUPbTAPP/eScanRange
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laQicpmsUPbTAPP/eScanRange
            schema:name:
              const: E-scan Range
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
          title: Triple Scanning Mode
          description: ''
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsUPbTAPP/tripleScanningMode
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laQicpmsUPbTAPP/tripleScanningMode
            schema:name:
              const: Triple Scanning Mode
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
          title: Imaging
          description: ''
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsUPbTAPP/imaging
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: imaging
            schema:name:
              const: Imaging
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
          title: Ablation Pit Depth/Ablation Rate
          description: ''
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsUPbTAPP/ablationPitDepthAblationRate
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: ablationPitDepthAblationRate
            schema:name:
              const: Ablation Pit Depth/Ablation Rate
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
          title: "Make-up Gas Flow (L min\u207B\xB9)"
          description: ''
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsUPbTAPP/makeUpGasFlow
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: makeUpGasFlow
            schema:name:
              const: "Make-up Gas Flow (L min\u207B\xB9)"
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
          title: Number of Blocks per Measurement
          description: ''
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsUPbTAPP/numberOfBlocksPerMeasurement
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: numberOfBlocksPerMeasurement
            schema:name:
              const: Number of Blocks per Measurement
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
          title: Number of Cycles per Block
          description: ''
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsUPbTAPP/numberOfCyclesPerBlock
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: numberOfCyclesPerBlock
            schema:name:
              const: Number of Cycles per Block
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
          title: Integration Time per Cycle
          description: ''
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsUPbTAPP/integrationTimePerCycle
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: integrationTimePerCycle
            schema:name:
              const: Integration Time per Cycle
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
          title: IC Dead Time (ns)
          description: ''
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsUPbTAPP/icDeadTime
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: icDeadTime
            schema:name:
              const: IC Dead Time (ns)
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
          title: Baseline Measurement Approach
          description: ''
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsUPbTAPP/baselineMeasurementApproach
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laQicpmsUPbTAPP/baselineMeasurementApproach
            schema:name:
              const: Baseline Measurement Approach
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
          title: Other Information
          description: ''
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsUPbTAPP/otherInformation
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: otherInformation
            schema:name:
              const: Other Information
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
          title: Mass Fractionation Law
          description: ''
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsUPbTAPP/massFractionationLaw
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laQicpmsUPbTAPP/massFractionationLaw
            schema:name:
              const: Mass Fractionation Law
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
          title: Uncertainty Level and Propagation
          description: ''
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsUPbTAPP/uncertaintyLevelAndPropagation
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: uncertaintyLevelAndPropagation
            schema:name:
              const: Uncertainty Level and Propagation
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
          title: Double-Spike Isotope Pair
          description: ''
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsUPbTAPP/doubleSpikeIsotopePair
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laQicpmsUPbTAPP/doubleSpikeIsotopePair
            schema:name:
              const: Double-Spike Isotope Pair
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
          title: Double-Spike Mixing Ratio
          description: ''
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsUPbTAPP/doubleSpikeMixingRatio
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: doubleSpikeMixingRatio
            schema:name:
              const: Double-Spike Mixing Ratio
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
    schema:instrument:
      type: array
      items:
        type: object
        allOf:
        - if:
            properties:
              schema:additionalType:
                contains:
                  const: Laser Ablation System
            required:
            - schema:additionalType
          then:
            properties:
              schema:model:
                type: object
                properties:
                  schema:name:
                    description: Manufacturer and model of the laser ablation system.
                    type: string
                    readOnly: true
              ada:laserType:
                description: Wavelength and type of the laser used for ablation in
                  nanometres.
                anyOf:
                - type: string
                  readOnly: true
                - type: array
                  items:
                    type: string
                    readOnly: true
              schema:name:
                description: Type, design origin, and internal volume of the ablation
                  cell. Cell volume is a primary determinant of aerosol washout time
                  and therefore the achievable time resolution of the data.
                anyOf:
                - type: string
                  readOnly: true
                - type: array
                  items:
                    type: string
                    readOnly: true
              ada:laserSpotGeometryDefault:
                description: "Shape and dimensions of the laser ablation spot in micrometres
                  registered by the procedure. For circular spots, report diameter;
                  for square or rectangular spots, report width \xD7 length. The procedure
                  registers the typical geometry; analysts may adjust within procedure-allowed
                  range."
                anyOf:
                - type: string
                - type: array
                  items:
                    type: string
              schema:additionalProperty:
                type: array
                items:
                  anyOf:
                  - title: Laser Energy
                    description: "Laser pulse energy in millijoules as set at the
                      laser output or measured at the sample surface. Less commonly
                      reported than fluence because it does not account for spot area.
                      Report only when the system displays energy directly. Laser
                      fluence (J cm\u207B\xB2) is the preferred quantity and is captured
                      in Default Laser Fluence."
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/laQicpmsUPbTAPP/laserEnergyDefault
                      '@type':
                        const:
                        - schema:PropertyValueSpecification
                      schema:valueName:
                        const: laserEnergyDefault
                      schema:name:
                        const: Laser Energy
                      ada:dataType:
                        const: number
                      ada:fieldScope:
                        const: session
                      schema:readonlyValue:
                        const: false
                      ada:tier:
                        const: R
                      schema:unitText:
                        const: mJ
                    required:
                    - '@id'
                    - '@type'
                    - schema:valueName
                    - schema:name
                    - ada:dataType
                    - ada:fieldScope
                  - title: Laser Beam Energy Profile
                    description: Spatial energy distribution of the laser beam at
                      the sample surface, and whether a beam homogenizer is installed.
                      A flat-top (top-hat) profile produces more uniform ablation
                      craters and more reproducible crater morphology than a Gaussian
                      beam. This is a fixed hardware property of the laser system.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/laQicpmsUPbTAPP/laserBeamEnergyProfile
                      '@type':
                        const:
                        - schema:PropertyValue
                      schema:propertyID:
                        const:
                        - '@id': ada:parameter/laQicpmsUPbTAPP/laserBeamEnergyProfile
                      schema:name:
                        const: Laser Beam Energy Profile
                      schema:value:
                        type: string
                    required:
                    - '@id'
                    - '@type'
                    - schema:propertyID
                    - schema:name
                    - schema:value
                    readOnly: true
                  - title: Laser Pulse Duration
                    description: 'Duration of each individual laser pulse, including
                      units. Pulse duration determines the ablation regime: nanosecond
                      (ns) pulses involve significant thermal effects and elemental
                      fractionation; femtosecond (fs) pulses are non-thermal and substantially
                      reduce elemental fractionation and matrix effects. This is a
                      fixed hardware property of the laser system.'
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/laQicpmsUPbTAPP/laserPulseDuration
                      '@type':
                        const:
                        - schema:PropertyValue
                      schema:propertyID:
                        const:
                        - '@id': ada:parameter/laQicpmsUPbTAPP/laserPulseDuration
                      schema:name:
                        const: Laser Pulse Duration
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
                    title: Laser Energy
                    description: "Laser pulse energy in millijoules as set at the
                      laser output or measured at the sample surface. Less commonly
                      reported than fluence because it does not account for spot area.
                      Report only when the system displays energy directly. Laser
                      fluence (J cm\u207B\xB2) is the preferred quantity and is captured
                      in Default Laser Fluence."
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/laQicpmsUPbTAPP/laserEnergyDefault
                      '@type':
                        const:
                        - schema:PropertyValueSpecification
                      schema:valueName:
                        const: laserEnergyDefault
                      schema:name:
                        const: Laser Energy
                      ada:dataType:
                        const: number
                      ada:fieldScope:
                        const: session
                      schema:readonlyValue:
                        const: false
                      ada:tier:
                        const: R
                      schema:unitText:
                        const: mJ
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
                    title: Laser Beam Energy Profile
                    description: Spatial energy distribution of the laser beam at
                      the sample surface, and whether a beam homogenizer is installed.
                      A flat-top (top-hat) profile produces more uniform ablation
                      craters and more reproducible crater morphology than a Gaussian
                      beam. This is a fixed hardware property of the laser system.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/laQicpmsUPbTAPP/laserBeamEnergyProfile
                      '@type':
                        const:
                        - schema:PropertyValue
                      schema:propertyID:
                        const:
                        - '@id': ada:parameter/laQicpmsUPbTAPP/laserBeamEnergyProfile
                      schema:name:
                        const: Laser Beam Energy Profile
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
                    title: Laser Pulse Duration
                    description: 'Duration of each individual laser pulse, including
                      units. Pulse duration determines the ablation regime: nanosecond
                      (ns) pulses involve significant thermal effects and elemental
                      fractionation; femtosecond (fs) pulses are non-thermal and substantially
                      reduce elemental fractionation and matrix effects. This is a
                      fixed hardware property of the laser system.'
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/laQicpmsUPbTAPP/laserPulseDuration
                      '@type':
                        const:
                        - schema:PropertyValue
                      schema:propertyID:
                        const:
                        - '@id': ada:parameter/laQicpmsUPbTAPP/laserPulseDuration
                      schema:name:
                        const: Laser Pulse Duration
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
              ada:laserFluenceDefault:
                description: "Laser pulse energy per unit area at the sample surface
                  in J cm\u207B\xB2, as registered by the procedure. Fluence is the
                  physically meaningful quantity controlling ablation rate, crater
                  morphology, elemental fractionation, and particle size distribution.
                  If the system reports only as % of maximum output, include that
                  value and note the system maximum where known."
                anyOf:
                - type: number
                - type: string
              ada:laserRepetitionRateDefault:
                description: Laser pulse repetition rate in hertz registered by the
                  procedure. For mapping methods, repetition rate together with scan
                  speed and spot size determines pixel size and spatial resolution.
                  Analysts may adjust within procedure-allowed bounds.
                anyOf:
                - type: number
                - type: string
        - if:
            properties:
              schema:additionalType:
                contains:
                  const: ICPMS
            required:
            - schema:additionalType
          then:
            properties:
              schema:model:
                type: object
                properties:
                  schema:name:
                    description: Manufacturer and model of the ICP-MS instrument.
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
                        const: ada:parameter/laQicpmsUPbTAPP/instrumentSerialNumberOrLabIdentifierDefault
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
                        const: ada:parameter/laQicpmsUPbTAPP/massResolutionSetting
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
                        const: ada:parameter/laQicpmsUPbTAPP/detectorConfiguration
                      '@type':
                        const:
                        - schema:PropertyValue
                      schema:propertyID:
                        const:
                        - '@id': ada:parameter/laQicpmsUPbTAPP/detectorConfiguration
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
                        const: ada:parameter/laQicpmsUPbTAPP/icpTuningDefault
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
                        const: ada:parameter/laQicpmsUPbTAPP/doublyChargedSpeciesMonitorDefault
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
                        const: ada:parameter/laQicpmsUPbTAPP/doublyChargedSpeciesProductionDefault
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
                        const: ada:parameter/laQicpmsUPbTAPP/memoryEffectMitigationDefault
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
                        const: ada:parameter/laQicpmsUPbTAPP/instrumentSerialNumberOrLabIdentifierDefault
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
                        const: ada:parameter/laQicpmsUPbTAPP/massResolutionSetting
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
                        const: ada:parameter/laQicpmsUPbTAPP/detectorConfiguration
                      '@type':
                        const:
                        - schema:PropertyValue
                      schema:propertyID:
                        const:
                        - '@id': ada:parameter/laQicpmsUPbTAPP/detectorConfiguration
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
                        const: ada:parameter/laQicpmsUPbTAPP/icpTuningDefault
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
                        const: ada:parameter/laQicpmsUPbTAPP/doublyChargedSpeciesMonitorDefault
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
                        const: ada:parameter/laQicpmsUPbTAPP/doublyChargedSpeciesProductionDefault
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
                        const: ada:parameter/laQicpmsUPbTAPP/memoryEffectMitigationDefault
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
                                  const: ada:parameter/laQicpmsUPbTAPP/interfaceConeConfiguration
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laQicpmsUPbTAPP/interfaceConeConfiguration
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
                                  const: ada:parameter/laQicpmsUPbTAPP/samplerAndSkimmerConeMaterial
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laQicpmsUPbTAPP/samplerAndSkimmerConeMaterial
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
                                  const: ada:parameter/laQicpmsUPbTAPP/interfaceConeConfiguration
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laQicpmsUPbTAPP/interfaceConeConfiguration
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
                                  const: ada:parameter/laQicpmsUPbTAPP/samplerAndSkimmerConeMaterial
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laQicpmsUPbTAPP/samplerAndSkimmerConeMaterial
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
                                const: ada:parameter/laQicpmsUPbTAPP/torchDepthDefault
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
                                  const: ada:parameter/laQicpmsUPbTAPP/torchDepthDefault
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
                            - STD (standard mode, no gas)
                            - KED (kinetic energy discrimination, He gas)
                            - DRC (dynamic reaction cell, reactive gas)
                            - ICP-MS/MS (triple-quadrupole mode)
                            - N/A
                            - None
                            - missing
                            readOnly: true
                          - type: array
                            items:
                              type: string
                              enum:
                              - STD (standard mode, no gas)
                              - KED (kinetic energy discrimination, He gas)
                              - DRC (dynamic reaction cell, reactive gas)
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
                                  const: ada:parameter/laQicpmsUPbTAPP/collisionGasType
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laQicpmsUPbTAPP/collisionGasType
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
                                  const: ada:parameter/laQicpmsUPbTAPP/collisionGasFlowRateDefault
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
                                  const: ada:parameter/laQicpmsUPbTAPP/cellExitDiscriminationVoltageDefault
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
                                  const: ada:parameter/laQicpmsUPbTAPP/reactionGasType
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laQicpmsUPbTAPP/reactionGasType
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
                                  const: ada:parameter/laQicpmsUPbTAPP/reactionGasFlowRateDefault
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
                                  const: ada:parameter/laQicpmsUPbTAPP/collisionGasType
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laQicpmsUPbTAPP/collisionGasType
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
                                  const: ada:parameter/laQicpmsUPbTAPP/collisionGasFlowRateDefault
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
                                  const: ada:parameter/laQicpmsUPbTAPP/cellExitDiscriminationVoltageDefault
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
                                  const: ada:parameter/laQicpmsUPbTAPP/reactionGasType
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laQicpmsUPbTAPP/reactionGasType
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
                                  const: ada:parameter/laQicpmsUPbTAPP/reactionGasFlowRateDefault
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
                                  const: ada:parameter/laQicpmsUPbTAPP/coolantGasFlowRateDefault
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
                                  const: ada:parameter/laQicpmsUPbTAPP/auxiliaryGasFlowRateDefault
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
                                  const: ada:parameter/laQicpmsUPbTAPP/rfPowerDefault
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
                                  const: ada:parameter/laQicpmsUPbTAPP/plasmaThermalMode
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laQicpmsUPbTAPP/plasmaThermalMode
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
                                  const: ada:parameter/laQicpmsUPbTAPP/coolantGasFlowRateDefault
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
                                  const: ada:parameter/laQicpmsUPbTAPP/auxiliaryGasFlowRateDefault
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
                                  const: ada:parameter/laQicpmsUPbTAPP/rfPowerDefault
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
                                  const: ada:parameter/laQicpmsUPbTAPP/plasmaThermalMode
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laQicpmsUPbTAPP/plasmaThermalMode
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
                  - if:
                      properties:
                        schema:additionalType:
                          contains:
                            const: Collector
                      required:
                      - schema:additionalType
                    then:
                      properties:
                        schema:additionalProperty:
                          type: array
                          items:
                            anyOf:
                            - title: Faraday Cup Array Configuration
                              description: ''
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laQicpmsUPbTAPP/faradayCupArrayConfiguration
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laQicpmsUPbTAPP/faradayCupArrayConfiguration
                                schema:name:
                                  const: Faraday Cup Array Configuration
                                schema:value:
                                  type: string
                              required:
                              - '@id'
                              - '@type'
                              - schema:propertyID
                              - schema:name
                              - schema:value
                              readOnly: true
                            - title: Faraday Cup Amplifier Resistor Values
                              description: ''
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laQicpmsUPbTAPP/faradayCupAmplifierResistorValues
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laQicpmsUPbTAPP/faradayCupAmplifierResistorValues
                                schema:name:
                                  const: Faraday Cup Amplifier Resistor Values
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
                              title: Faraday Cup Array Configuration
                              description: ''
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laQicpmsUPbTAPP/faradayCupArrayConfiguration
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laQicpmsUPbTAPP/faradayCupArrayConfiguration
                                schema:name:
                                  const: Faraday Cup Array Configuration
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
                              title: Faraday Cup Amplifier Resistor Values
                              description: ''
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laQicpmsUPbTAPP/faradayCupAmplifierResistorValues
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laQicpmsUPbTAPP/faradayCupAmplifierResistorValues
                                schema:name:
                                  const: Faraday Cup Amplifier Resistor Values
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
                        schema:description:
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
                          const: Interface Cone
                    required:
                    - schema:additionalType
                - contains:
                    properties:
                      schema:additionalType:
                        contains:
                          const: Collision Reaction Cell
                    required:
                    - schema:additionalType
                - contains:
                    properties:
                      schema:additionalType:
                        contains:
                          const: ICP Source
                    required:
                    - schema:additionalType
      allOf:
      - contains:
          properties:
            schema:additionalType:
              contains:
                const: Laser Ablation System
          required:
          - schema:additionalType
      - contains:
          properties:
            schema:additionalType:
              contains:
                const: ICPMS
          required:
          - schema:additionalType
    bios:computationalTool:
      type: array
      items:
        type: object
        allOf:
        - if:
            properties:
              ada:toolRole:
                const: acquisition
            required:
            - ada:toolRole
          then:
            properties:
              schema:name:
                description: Instrument control and data acquisition software used
                  to collect raw signal data, including version number. Separate from
                  data reduction software.
                anyOf:
                - type: string
                - type: array
                  items:
                    type: string
        - if:
            properties:
              ada:toolRole:
                const: dataReduction
            required:
            - ada:toolRole
          then:
            properties:
              schema:name:
                description: Software used for signal processing, background subtraction,
                  and concentration calculation, including version number.
                anyOf:
                - type: string
                - type: array
                  items:
                    type: string
        required:
        - ada:toolRole
    ada:sampleIntroduction:
      description: "Configuration by which the ablated aerosol is delivered to the
        plasma, including tubing, any signal-homogenising device, and any co-aspirated
        solution introduced alongside the aerosol \u2014 for example a Tl solution
        used for instrumental mass bias correction, or an isotopic spike used for
        isotope dilution. Distinct from the carrier and make-up gas fields, which
        record gas identity and flow rather than what else enters the plasma."
      type: string
      readOnly: true
    ada:analyticalMode:
      type: array
      items:
        description: Primary analytical mode(s) executed under this procedure. For
          single-mode procedures, records one value (e.g., Spot). For multi-mode procedures
          (e.g., spot analysis combined with transect scanning), list all applicable
          modes. Serves as the procedure-level declaration of measurement type, distinct
          from the mode flag columns which indicate per-field applicability.
        type: string
        enum:
        - Spot
        - Transect
        - Mapping
        - Spot; Transect
        - missing
        readOnly: true
    ada:ablationSamplingMode:
      type: array
      items:
        description: Sampling mode or ablation pattern used during analysis.
        type: string
        enum:
        - Spot (stationary)
        - Transect (continuous line scan)
        - Raster area (2D elemental mapping)
        - Stepped line profile
        - N/A
        - None
        - missing
        readOnly: true
    ada:ablationSpotDurationDefault:
      description: 'Total on-sample ablation (signal acquisition) time per individual
        spot in seconds, as set in the acquisition method. This is a procedure-level
        parameter for spot analysis: it reflects the deliberate trade-off between
        signal accumulation (longer = lower LOD), sample consumption, and session
        throughput. For transect analysis, the equivalent procedure-level parameter
        is scan speed (captured in Transect Rate, Mapping Rate or Step Size). For
        mapping analysis, total acquisition time is sample-area-dependent and therefore
        analysis-level, not captured here.'
      anyOf:
      - type: number
      - type: string
    ada:ablationPitDepthRateDefault:
      description: Depth of the ablation pit produced under the registered laser conditions,
        the method used to measure it, and the resulting per-pulse ablation rate.
        Sets the achievable depth resolution and governs downhole elemental fractionation.
        For transect and mapping the equivalent quantity is trench depth under the
        same conditions.
      type: string
    ada:rasterLineSpacingDefault:
      description: Distance between adjacent raster lines in a 2D elemental map, measured
        perpendicular to the scan direction, in micrometres. Together with spot size,
        this determines whether adjacent lines are contiguous (line spacing = spot
        size), overlapping (line spacing < spot size), or have gaps (line spacing
        > spot size). Applies to raster mapping only.
      type: string
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
        ada:defaultAnalytes:
          type: array
          items:
            anyOf:
            - type: string
            - $ref: https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/DefinedTerm
        ada:analyteColumns:
          type: array
          items:
            anyOf:
            - $ref: https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/AnalyteIdentifierColumn
            - title: Monitored Isotopes
              description: Specific isotope(s) monitored in this procedure, grouped
                by the analyte element they serve where they serve one. Includes interference-monitor
                and internal-standard masses, which serve no analyte and so have no
                parent element. The analyte list is given by the Analyte field and
                is never inferred from the element symbols appearing here.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/laQicpmsUPbTAPP/monitoredIsotopes
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: monitoredIsotopes
                schema:name:
                  const: Monitored Isotopes
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
                  const: ada:analyteColumn/laQicpmsUPbTAPP/dwellTimePerMass
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: dwellTimePerMass
                schema:name:
                  const: Dwell Time per Mass
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
            - title: Isobaric Interference Corrections Applied
              description: 'Whether isobaric interference corrections were applied
                for any measured isotope in this procedure. A procedure-level Boolean:
                if the procedure includes interference corrections, this is always
                Yes. Detail for each affected mass is captured in Interfering Species
                and Interference Correction Method.'
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/laQicpmsUPbTAPP/isobaricInterferenceCorrectionsApplied
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
                  const: ada:analyteColumn/laQicpmsUPbTAPP/interferingSpecies
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
                  const: ada:analyteColumn/laQicpmsUPbTAPP/interferenceCorrectionMethod
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
            - title: Normalization / Standards-Based Correction
              description: Any post-acquisition normalization applied to correct for
                systematic biases identified from secondary reference materials, or
                stoichiometric normalization applied per pixel in mapping. Distinct
                from the primary internal standard approach captured in Internal Standard
                Approach.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/laQicpmsUPbTAPP/normalizationStandardsBasedCorrection
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: normalizationStandardsBasedCorrection
                schema:name:
                  const: Normalization / Standards-Based Correction
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
            - title: Detection Limit
              description: "Session detection limit, one per reported concentration
                variable (one per analyte, these being the same set), expressed in
                \xB5g g\u207B\xB9, ng g\u207B\xB9, or wt% as appropriate. Mandatory
                at analysis level to demonstrate the reliability of reported near-detection-limit
                concentrations. The calculation method is captured separately in Detection
                Limit Method."
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/laQicpmsUPbTAPP/detectionLimit
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
              description: Reference or description of the method used to calculate
                session detection limits. Mandatory at analysis level. Must be consistent
                with the method applied to generate the Detection Limit values reported
                above.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/laQicpmsUPbTAPP/detectionLimitMethod
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: detectionLimitMethod
                schema:name:
                  const: Detection Limit Method
                ada:dataType:
                  const: uri
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
                  const: ada:analyteColumn/laQicpmsUPbTAPP/limitOfQuantificationMethod
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
              description: "Reproducibility of repeated measurements within a single
                analytical session. Report both the assessment method and the precision
                values. Assessment method must specify: (1) the reference material
                used, (2) number of replicates n, and (3) the statistic reported (1\u03C3
                RSD, 2\u03C3 RSD, etc.). For mapping: assess from repeated analyses
                of a reference material area at session start and end, or from replicate
                analyses of a homogeneous reference phase within the map."
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/laQicpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod
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
              description: 'Reproducibility of measurements across multiple analytical
                sessions over weeks to months (long-term or intermediate precision).
                Report both the assessment method and the precision values. Specify:
                reference material used, number of sessions n, time span covered,
                and statistic reported. Long-term precision is typically assessed
                from a compiled record of secondary reference material values across
                all sessions.'
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/laQicpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod
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
                  const: ada:analyteColumn/laQicpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod
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
            - title: Mass Resolution per Analyte
              description: ''
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/laQicpmsUPbTAPP/massResolutionPerAnalyte
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: massResolutionPerAnalyte
                schema:name:
                  const: Mass Resolution per Analyte
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: true
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
              title: Monitored Isotopes
              description: Specific isotope(s) monitored in this procedure, grouped
                by the analyte element they serve where they serve one. Includes interference-monitor
                and internal-standard masses, which serve no analyte and so have no
                parent element. The analyte list is given by the Analyte field and
                is never inferred from the element symbols appearing here.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/laQicpmsUPbTAPP/monitoredIsotopes
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: monitoredIsotopes
                schema:name:
                  const: Monitored Isotopes
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
                  const: ada:analyteColumn/laQicpmsUPbTAPP/dwellTimePerMass
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: dwellTimePerMass
                schema:name:
                  const: Dwell Time per Mass
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
              title: Isobaric Interference Corrections Applied
              description: 'Whether isobaric interference corrections were applied
                for any measured isotope in this procedure. A procedure-level Boolean:
                if the procedure includes interference corrections, this is always
                Yes. Detail for each affected mass is captured in Interfering Species
                and Interference Correction Method.'
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/laQicpmsUPbTAPP/isobaricInterferenceCorrectionsApplied
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
                  const: ada:analyteColumn/laQicpmsUPbTAPP/interferingSpecies
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
                  const: ada:analyteColumn/laQicpmsUPbTAPP/interferenceCorrectionMethod
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
              title: Normalization / Standards-Based Correction
              description: Any post-acquisition normalization applied to correct for
                systematic biases identified from secondary reference materials, or
                stoichiometric normalization applied per pixel in mapping. Distinct
                from the primary internal standard approach captured in Internal Standard
                Approach.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/laQicpmsUPbTAPP/normalizationStandardsBasedCorrection
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: normalizationStandardsBasedCorrection
                schema:name:
                  const: Normalization / Standards-Based Correction
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
              title: Detection Limit
              description: "Session detection limit, one per reported concentration
                variable (one per analyte, these being the same set), expressed in
                \xB5g g\u207B\xB9, ng g\u207B\xB9, or wt% as appropriate. Mandatory
                at analysis level to demonstrate the reliability of reported near-detection-limit
                concentrations. The calculation method is captured separately in Detection
                Limit Method."
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/laQicpmsUPbTAPP/detectionLimit
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
              description: Reference or description of the method used to calculate
                session detection limits. Mandatory at analysis level. Must be consistent
                with the method applied to generate the Detection Limit values reported
                above.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/laQicpmsUPbTAPP/detectionLimitMethod
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: detectionLimitMethod
                schema:name:
                  const: Detection Limit Method
                ada:dataType:
                  const: uri
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
                  const: ada:analyteColumn/laQicpmsUPbTAPP/limitOfQuantificationMethod
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
              description: "Reproducibility of repeated measurements within a single
                analytical session. Report both the assessment method and the precision
                values. Assessment method must specify: (1) the reference material
                used, (2) number of replicates n, and (3) the statistic reported (1\u03C3
                RSD, 2\u03C3 RSD, etc.). For mapping: assess from repeated analyses
                of a reference material area at session start and end, or from replicate
                analyses of a homogeneous reference phase within the map."
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/laQicpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod
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
              description: 'Reproducibility of measurements across multiple analytical
                sessions over weeks to months (long-term or intermediate precision).
                Report both the assessment method and the precision values. Specify:
                reference material used, number of sessions n, time span covered,
                and statistic reported. Long-term precision is typically assessed
                from a compiled record of secondary reference material values across
                all sessions.'
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/laQicpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod
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
                  const: ada:analyteColumn/laQicpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod
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
              title: Mass Resolution per Analyte
              description: ''
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/laQicpmsUPbTAPP/massResolutionPerAnalyte
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: massResolutionPerAnalyte
                schema:name:
                  const: Mass Resolution per Analyte
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: true
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
    ada:reportedPropertyTemplate:
      type: object
      properties:
        ada:defaultReportedProperties:
          type: array
          items:
            description: "The final variable(s) this procedure reports and their units
              \u2014 distinct from the fields recording what was *acquired* rather
              than what is reported. A procedure may acquire many channels and report
              a small number of derived quantities; without this field a data consumer
              cannot tell which. Record every reported variable, including intermediate
              quantities reported alongside final ones (e.g. both the 206Pb/238U ratio
              and the 206Pb/238U date). Where a reported variable is a nominal property
              with no magnitude (e.g. a mineral identification), record the variable
              and give the unit as 'N/A \u2014 nominal property'."
            type: string
            readOnly: true
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
      type: string
      readOnly: true
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
    ada:ageCalculationMethod:
      type: array
      items:
        description: The equation used to convert the measured quantities into an
          age or date, together with a citation for that equation. Name the equation
          unambiguously; where a procedure supports more than one, state which is
          used and under what conditions. Required by every geochronology reporting
          standard surveyed (Condon et al. 2024; Schaen et al. 2021; Rooney et al.
          2024; Flowers et al. 2024; Kohn et al. 2024; Mahan et al. 2023). Distinct
          from Age Model and Software, which records how multiple analyses are combined
          into a single reported result.
        type: string
        readOnly: true
    ada:reportedDateType:
      type: array
      items:
        description: The kind of date or age the procedure reports. Most dating systems
          derive several different date types from the same measurements, so a reported
          age is ambiguous without this. Where more than one type is reported, list
          all, separated by semicolons. Kohn et al. (2024) carry this as a named required
          item ("fission-track age type"); the equivalent distinction is required
          by all five other standards surveyed.
        type: string
        enum:
        - Weighted mean 206Pb/238U
        - Weighted mean 207Pb/235U
        - Weighted mean 207Pb/206Pb
        - Concordia upper intercept
        - Concordia lower intercept
        - Tera-Wasserburg intercept
        - Single-grain date
        - Isochron date
        - N/A
        - None
        - missing
    ada:inheritedOrInitialSignalCorrectionDefault:
      description: 'How any non-radiogenic, inherited or pre-existing component of
        the measured signal was accounted for, including the composition assumed,
        its source, and its uncertainty. Record ''None'' where the measured quantity
        accumulates from zero and no such component exists. Applies to five of the
        six dating systems surveyed; fission track is the sole genuine exception,
        as tracks accumulate from zero. D=Editable rather than Read-Only: the procedure
        registers the correction method and any default composition, but the value
        actually applied is frequently sample-specific (a two-stage model composition
        is evaluated at the interpreted age) or session-derived (a trapped composition
        solved from an isochron intercept), and a revision to the assumed composition
        should not require registering a new procedure. Same reasoning as Rule 5''s
        Constants and Reference Values Used.'
      type: string
    ada:ageModelDefault:
      description: "The statistical model used to combine individual analyses into
        a single reported age, including any criteria governing which model is applied.
        This is a methodological choice that changes the result: a Model-1 and a Model-3
        regression of the same data yield different ages and different uncertainties.
        Record the model only \u2014 the software implementing it belongs in Data
        Reduction Software (Group 3), whose scope already extends to age calculation;
        where reduction and age regression use different packages, list both there.
        Required in some form by all six geochronology reporting standards surveyed."
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
    schema:description:
      description: "Any procedure- or analysis-specific information not captured by
        a structured field anywhere in this TAPP \u2014 including anomalies, deviations
        from the registered procedure, instrument modifications, and supplementary
        context. Scope is the whole document, not Group 6: this is the last field
        of the TAPP and covers all six groups. Use sparingly; a structured field is
        preferred for anything that can be formally categorised."
      type: string
    ada:spotDiameterDefault:
      type: string
      readOnly: true
    ada:massesMeasuredDefault:
      type: string
      readOnly: true
    ada:dwellTimesDefault:
      type: string
      readOnly: true
    ada:gasBlank:
      type: string
      readOnly: true
    ada:internalNormalizationElementAndIsotopeRatio:
      type: string
      readOnly: true
    ada:commonPbCorrectionCompositionAndUncertainty:
      type: string
      readOnly: true
  required:
  - schema:name
  - schema:datePublished
  - ada:samplingUnit
  - ada:targetSelectionCriteriaDefault
  - ada:sampleIntroduction
  - ada:ablationSpotDurationDefault
  - ada:ablationPitDepthRateDefault
  - ada:rasterLineSpacingDefault
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
  - ada:inheritedOrInitialSignalCorrectionDefault
  - ada:ageModelDefault
  - ada:primaryStandardNameDefault
  - ada:calibrationMeasurementFrequency

```

Links to the schema:

* YAML version: [schema.yaml](https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS-UPb/tapp/schema.json)
* JSON version: [schema.json](https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS-UPb/tapp/schema.yaml)


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
[context.jsonld](https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS-UPb/tapp/context.jsonld)

## Sources

* [LA-Q-ICP-MS_UPb_TAPP_v16.csv (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/LA-Q-ICPMS-UPb/tapp`

