
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
          "@id": "ada:parameter/module/LaserAblation/sampleFormAnalyticalSubstrateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleFormAnalyticalSubstrateDefault",
          "schema:name": "Sample Form Analytical Substrate",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "In situ — polished epoxy thick section (petropoxy 154 resin, 0.5 µm diamond finish)"
        }
      ]
    }
  ],
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
              "@id": "ada:parameter/module/ICPMS/configuration",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "configuration",
              "schema:name": "Configuration",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
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
              "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantPlasmaGasFlowRateDefault",
              "schema:name": "Coolant Plasma Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 12,
              "schema:description": "Cool gas: 12–13 l min⁻¹ Ar; Auxiliary: 0.6–1.2 l min⁻¹"
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
          "@id": "ada:parameter/module/ICPMS/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
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
      "@id": "ada:parameter/module/ICPMS/makeUpGasAndFlowRateDefault",
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
      "@id": "ada:parameter/module/LaserAblation/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "multiRunSequentialAnalysisDesign",
      "schema:name": "Multi Run Sequential Analysis Design",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "Single spot per location (30 µm circular)"
    }
  ],
  "ada:analysisSequenceDefault": "IVB meteorite standards (Warburton Range external + Tawallah Valley secondary) measured alongside unknowns; exact bracketing not described",
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
            "@id": "ada:parameter/module/ICPMS/filteringApproachDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "filteringApproachDefault",
            "schema:name": "Filtering Approach",
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
  "ada:internalStandardApproach": "Single element externally measured by EPMA: ⁶¹Ni concentration from EPMA at exact analysis location used as IS",
  "ada:elementalFractionationCorrection": [
    "External calibration using calibration curve method with IVB iron meteorite standards; ⁶¹Ni as IS from EPMA corrects for ablation yield differences between sample and standard"
  ],
  "ada:blankBackgroundCorrectionMethod": "Gas blank measured before each spot; background period during single spot transient (rapid intensity rise and decay) used for background correction",
  "ada:internalStandardElement": "⁶¹Ni; concentration from EPMA measured at exact analysis spot location",
  "ada:signalIntegrationIntervalMethod": "Time-resolved signals monitored; analyses with elevated Mg, Si, P, S (inclusion indicators) excluded; stable signal intervals used for integration",
  "ada:secondaryReferenceMaterialDefault": [
    "Tawallah Valley (IVB iron meteorite; Walker et al. 2008) — measured as secondary/check standard alongside unknowns"
  ],
  "ada:primaryStandardNameDefault": "Warburton Range (IVB iron meteorite; Walker et al. 2008) — used as primary external standard and for calibration curve method",
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ablationSpotDurationDefault": -9999,
  "ada:ageModelDefault": "missing",
  "ada:backgroundCountTimeDefault": -9999,
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:inheritedOrInitialSignalCorrectionDefault": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:massesMeasuredDefault": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:signalCollectionMode": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS-UPb/tapp/context.jsonld",
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
          "@id": "ada:parameter/module/LaserAblation/sampleFormAnalyticalSubstrateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleFormAnalyticalSubstrateDefault",
          "schema:name": "Sample Form Analytical Substrate",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "In situ \u2014 polished epoxy thick section (petropoxy 154 resin, 0.5 \u00b5m diamond finish)"
        }
      ]
    }
  ],
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
              "@id": "ada:parameter/module/ICPMS/configuration",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "configuration",
              "schema:name": "Configuration",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
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
              "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantPlasmaGasFlowRateDefault",
              "schema:name": "Coolant Plasma Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 12,
              "schema:description": "Cool gas: 12\u201313 l min\u207b\u00b9 Ar; Auxiliary: 0.6\u20131.2 l min\u207b\u00b9"
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
          "@id": "ada:parameter/module/ICPMS/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
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
      "@id": "ada:parameter/module/ICPMS/makeUpGasAndFlowRateDefault",
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
      "@id": "ada:parameter/module/LaserAblation/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "multiRunSequentialAnalysisDesign",
      "schema:name": "Multi Run Sequential Analysis Design",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "Single spot per location (30 \u00b5m circular)"
    }
  ],
  "ada:analysisSequenceDefault": "IVB meteorite standards (Warburton Range external + Tawallah Valley secondary) measured alongside unknowns; exact bracketing not described",
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
            "@id": "ada:parameter/module/ICPMS/filteringApproachDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "filteringApproachDefault",
            "schema:name": "Filtering Approach",
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
  "ada:internalStandardApproach": "Single element externally measured by EPMA: \u2076\u00b9Ni concentration from EPMA at exact analysis location used as IS",
  "ada:elementalFractionationCorrection": [
    "External calibration using calibration curve method with IVB iron meteorite standards; \u2076\u00b9Ni as IS from EPMA corrects for ablation yield differences between sample and standard"
  ],
  "ada:blankBackgroundCorrectionMethod": "Gas blank measured before each spot; background period during single spot transient (rapid intensity rise and decay) used for background correction",
  "ada:internalStandardElement": "\u2076\u00b9Ni; concentration from EPMA measured at exact analysis spot location",
  "ada:signalIntegrationIntervalMethod": "Time-resolved signals monitored; analyses with elevated Mg, Si, P, S (inclusion indicators) excluded; stable signal intervals used for integration",
  "ada:secondaryReferenceMaterialDefault": [
    "Tawallah Valley (IVB iron meteorite; Walker et al. 2008) \u2014 measured as secondary/check standard alongside unknowns"
  ],
  "ada:primaryStandardNameDefault": "Warburton Range (IVB iron meteorite; Walker et al. 2008) \u2014 used as primary external standard and for calibration curve method",
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ablationSpotDurationDefault": -9999,
  "ada:ageModelDefault": "missing",
  "ada:backgroundCountTimeDefault": -9999,
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:inheritedOrInitialSignalCorrectionDefault": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:massesMeasuredDefault": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:signalCollectionMode": "missing",
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

ex:laQicpmsUPbTAPP-Nakanishi2022 a cdi:Activity,
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
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproachDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Thick sections in petropoxy 154 resin, polished to 0.5 µm diamond paste, C-coated for EPMA then surface polished before LA" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/LaserAblation/multiRunSequentialAnalysisDesign> ;
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
                <https://ada.astromat.org/metadata/parameter/module/LaserAblation/sampleFormAnalyticalSubstrateDefault> ] ;
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
    ada:massesMeasuredDefault "missing" ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:primaryStandardNameDefault "Warburton Range (IVB iron meteorite; Walker et al. 2008) — used as primary external standard and for calibration curve method" ;
    ada:rasterLineSpacingDefault "missing" ;
    ada:sampleIntroduction "missing" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:secondaryReferenceMaterialDefault "Tawallah Valley (IVB iron meteorite; Walker et al. 2008) — measured as secondary/check standard alongside unknowns" ;
    ada:signalCollectionMode "missing" ;
    ada:signalIntegrationIntervalMethod "Time-resolved signals monitored; analyses with elevated Mg, Si, P, S (inclusion indicators) excluded; stable signal intervals used for integration" ;
    ada:totalIntegrationTimePerOutputDataPointDefault -9999 ;
    ada:uncertaintyLevel "missing" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/configuration> a schema1:PropertyValueSpecification ;
    schema1:name "Configuration" ;
    schema1:value "Ni micro-skimmer cone Xs; Ni sampler cone" ;
    schema1:valueName "configuration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 12 ;
    schema1:description "Cool gas: 12–13 l min⁻¹ Ar; Auxiliary: 0.6–1.2 l min⁻¹" ;
    schema1:name "Coolant Plasma Gas Flow Rate" ;
    schema1:valueName "coolantPlasmaGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproachDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Monitoring of Mg, Si, P, S to check for micro-inclusions (sulfides); analyses with elevated inclusion signals excluded entirely" ;
    schema1:name "Filtering Approach" ;
    schema1:valueName "filteringApproachDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 9e-01 ;
    schema1:description "Ar make-up: 0.9–1.2 l min⁻¹; Ar auxiliary: 0.6–1.2 l min⁻¹" ;
    schema1:name "Make-up Gas and Flow Rate" ;
    schema1:valueName "makeUpGasAndFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Unit resolution (quadrupole fixed)" ;
    schema1:name "Mass Resolution Setting" ;
    schema1:valueName "massResolutionSettingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1400 ;
    schema1:description "1400 W" ;
    schema1:name "RF Power" ;
    schema1:valueName "rfPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/laserPulseDuration> a schema1:PropertyValueSpecification ;
    schema1:name "Laser Pulse Duration" ;
    schema1:value "~220 fs (Ti:sapphire IFRIT system)" ;
    schema1:valueName "laserPulseDuration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/multiRunSequentialAnalysisDesign> a schema1:PropertyValueSpecification ;
    schema1:name "Multi Run Sequential Analysis Design" ;
    schema1:value "Single spot per location (30 µm circular)" ;
    schema1:valueName "multiRunSequentialAnalysisDesign" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/sampleFormAnalyticalSubstrateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "In situ — polished epoxy thick section (petropoxy 154 resin, 0.5 µm diamond finish)" ;
    schema1:name "Sample Form Analytical Substrate" ;
    schema1:valueName "sampleFormAnalyticalSubstrateDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault> ;
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
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault>,
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
          "@id": "ada:parameter/module/LaserAblation/sampleFormAnalyticalSubstrateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleFormAnalyticalSubstrateDefault",
          "schema:name": "Sample Form Analytical Substrate",
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
            "@id": "ada:parameter/module/LaserAblation/fusionFluxAndDilutionRatioDefault",
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
            "@id": "ada:parameter/module/ICPMS/filteringApproachDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "filteringApproachDefault",
            "schema:name": "Filtering Approach",
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
          "@id": "ada:parameter/module/ICPMS/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
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
          "@id": "ada:parameter/module/ICPMS/icpTuningDefault",
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
          "@id": "ada:parameter/module/ICPMS/memoryEffectMitigationDefault",
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
              "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantPlasmaGasFlowRateDefault",
              "schema:name": "Coolant Plasma Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 15,
              "schema:description": "Plasma gas flow: 15 l min⁻¹; Auxiliary gas: 0.85 l min⁻¹"
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
  "ada:analysisSequenceDefault": "Gas blank (25 s) → ablation (45 s) → washout (25 s); NIST 612 and 614 as external standards; BHVO-2 and 6 GRMs measured as unknowns",
  "ada:backgroundCountTimeDefault": "25 s gas blank before each ablation",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/module/LaserAblation/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "multiRunSequentialAnalysisDesign",
      "schema:name": "Multi Run Sequential Analysis Design",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "Single spot per location (45 s ablation at 1 Hz)"
    }
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
  "ada:internalStandardApproach": "Two internal standards: Si from XRF SiO₂ (for Co, Ni, Cu, Zn); Al from XRF Al₂O₃ (for all other trace elements); non-matrix-matched external standards (NIST 612 + 614) used; fs laser minimizes matrix effects",
  "ada:elementalFractionationCorrection": [
    "Femtosecond laser substantially reduces elemental fractionation and matrix effects (stated); non-matrix-matched external standards (NIST 612 + 614) used successfully with fs laser (verified by GRM accuracy assessment)"
  ],
  "ada:calibrationMeasurementFrequency": "NIST SRM 612 and 614 measured as external standards within session; BHVO-2 and other GRMs as unknowns",
  "ada:oxideProductionMethodAndThreshold": "ThO⁺/Th⁺ (mass 248/232) <0.3%; U/Th monitored at 0.95–1.05",
  "ada:blankBackgroundCorrectionMethod": "Gas blank measured for 25 s before each ablation; background subtracted per isotope",
  "ada:internalStandardElement": "Si (SiO₂ from XRF) for Co, Ni, Cu, Zn; Al (Al₂O₃ from XRF) for all other 28 trace elements",
  "ada:signalIntegrationIntervalMethod": "Time-resolved signals inspected visually; flux blank contributions to pollution elements (V, Co, Zn, Ba, La, Ce, Ta, U) identified and subtracted; 9-spot grid homogeneity tested before analysis",
  "ada:secondaryReferenceMaterialDefault": [
    "AC-E (granite, CRPG), GSR-1 (granite, NRCG), JB-1b (basalt, GSJ), GSR-3 (basalt, NRCG), AGV-2 (andesite, USGS), W-2A (diabase, USGS) — 6 GRMs covering mafic to felsic rock types analyzed as unknowns; also NWA14526 (lunar basalt) and NWA13190 (shergottite) compared with SN-ICP-MS"
  ],
  "ada:primaryStandardNameDefault": "NIST SRM 612 + NIST SRM 614 (non-matrix-matched external standards); self-made BHVO-2 lithium borate glass (matrix-matched) tested as alternative but NIST 612+614 found sufficient with fs laser",
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ageModelDefault": "missing",
  "ada:inheritedOrInitialSignalCorrectionDefault": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:massesMeasuredDefault": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:signalCollectionMode": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS-UPb/tapp/context.jsonld",
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
          "@id": "ada:parameter/module/LaserAblation/sampleFormAnalyticalSubstrateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleFormAnalyticalSubstrateDefault",
          "schema:name": "Sample Form Analytical Substrate",
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
            "@id": "ada:parameter/module/LaserAblation/fusionFluxAndDilutionRatioDefault",
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
            "@id": "ada:parameter/module/ICPMS/filteringApproachDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "filteringApproachDefault",
            "schema:name": "Filtering Approach",
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
          "@id": "ada:parameter/module/ICPMS/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
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
          "@id": "ada:parameter/module/ICPMS/icpTuningDefault",
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
          "@id": "ada:parameter/module/ICPMS/memoryEffectMitigationDefault",
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
              "@id": "ada:parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantPlasmaGasFlowRateDefault",
              "schema:name": "Coolant Plasma Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 15,
              "schema:description": "Plasma gas flow: 15 l min\u207b\u00b9; Auxiliary gas: 0.85 l min\u207b\u00b9"
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
  "ada:analysisSequenceDefault": "Gas blank (25 s) \u2192 ablation (45 s) \u2192 washout (25 s); NIST 612 and 614 as external standards; BHVO-2 and 6 GRMs measured as unknowns",
  "ada:backgroundCountTimeDefault": "25 s gas blank before each ablation",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/module/LaserAblation/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "multiRunSequentialAnalysisDesign",
      "schema:name": "Multi Run Sequential Analysis Design",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "Single spot per location (45 s ablation at 1 Hz)"
    }
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
  "ada:internalStandardApproach": "Two internal standards: Si from XRF SiO\u2082 (for Co, Ni, Cu, Zn); Al from XRF Al\u2082O\u2083 (for all other trace elements); non-matrix-matched external standards (NIST 612 + 614) used; fs laser minimizes matrix effects",
  "ada:elementalFractionationCorrection": [
    "Femtosecond laser substantially reduces elemental fractionation and matrix effects (stated); non-matrix-matched external standards (NIST 612 + 614) used successfully with fs laser (verified by GRM accuracy assessment)"
  ],
  "ada:calibrationMeasurementFrequency": "NIST SRM 612 and 614 measured as external standards within session; BHVO-2 and other GRMs as unknowns",
  "ada:oxideProductionMethodAndThreshold": "ThO\u207a/Th\u207a (mass 248/232) <0.3%; U/Th monitored at 0.95\u20131.05",
  "ada:blankBackgroundCorrectionMethod": "Gas blank measured for 25 s before each ablation; background subtracted per isotope",
  "ada:internalStandardElement": "Si (SiO\u2082 from XRF) for Co, Ni, Cu, Zn; Al (Al\u2082O\u2083 from XRF) for all other 28 trace elements",
  "ada:signalIntegrationIntervalMethod": "Time-resolved signals inspected visually; flux blank contributions to pollution elements (V, Co, Zn, Ba, La, Ce, Ta, U) identified and subtracted; 9-spot grid homogeneity tested before analysis",
  "ada:secondaryReferenceMaterialDefault": [
    "AC-E (granite, CRPG), GSR-1 (granite, NRCG), JB-1b (basalt, GSJ), GSR-3 (basalt, NRCG), AGV-2 (andesite, USGS), W-2A (diabase, USGS) \u2014 6 GRMs covering mafic to felsic rock types analyzed as unknowns; also NWA14526 (lunar basalt) and NWA13190 (shergottite) compared with SN-ICP-MS"
  ],
  "ada:primaryStandardNameDefault": "NIST SRM 612 + NIST SRM 614 (non-matrix-matched external standards); self-made BHVO-2 lithium borate glass (matrix-matched) tested as alternative but NIST 612+614 found sufficient with fs laser",
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ageModelDefault": "missing",
  "ada:inheritedOrInitialSignalCorrectionDefault": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:massesMeasuredDefault": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:signalCollectionMode": "missing",
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

ex:laQicpmsUPbTAPP-Liu2024 a cdi:Activity,
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
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproachDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ;
                    ada:detectionLimitMethod "Pettke (2012) for most elements: LOD = (3.29 × √(Rbkg × DT × ...) + 2.71) / (Nan × DT × S); LOQ for pollution elements = blank value + 10SD (IUPAC Gold Book)" ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/LaserAblation/fusionFluxAndDilutionRatioDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/LaserAblation/preAblationSurfaceTreatmentDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Li-borate fusion: 350 mg Li₂B₄O₇ + 10 mg powdered sample fused in Pt-Au crucible (M4 automatic fluxer); glass surface cleaned with ethanol before LA" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/LaserAblation/multiRunSequentialAnalysisDesign> ;
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
                <https://ada.astromat.org/metadata/parameter/module/LaserAblation/sampleFormAnalyticalSubstrateDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Liu et al. (2024) JAAS 39, 2728; Pettke et al. (2012) for LOD" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:ablationPitDepthRateDefault "missing" ;
    ada:ablationSamplingMode "Spot (stationary; single spot at 1 Hz)" ;
    ada:ablationSpotDurationDefault "45 s ablation (after 25 s gas blank; 25 s washout between analyses)" ;
    ada:ageModelDefault "missing" ;
    ada:analysisSequenceDefault "Gas blank (25 s) → ablation (45 s) → washout (25 s); NIST 612 and 614 as external standards; BHVO-2 and 6 GRMs measured as unknowns" ;
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
    ada:massesMeasuredDefault "missing" ;
    ada:oxideProductionMethodAndThreshold "ThO⁺/Th⁺ (mass 248/232) <0.3%; U/Th monitored at 0.95–1.05" ;
    ada:primaryStandardNameDefault "NIST SRM 612 + NIST SRM 614 (non-matrix-matched external standards); self-made BHVO-2 lithium borate glass (matrix-matched) tested as alternative but NIST 612+614 found sufficient with fs laser" ;
    ada:rasterLineSpacingDefault "missing" ;
    ada:sampleIntroduction "missing" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:secondaryReferenceMaterialDefault "AC-E (granite, CRPG), GSR-1 (granite, NRCG), JB-1b (basalt, GSJ), GSR-3 (basalt, NRCG), AGV-2 (andesite, USGS), W-2A (diabase, USGS) — 6 GRMs covering mafic to felsic rock types analyzed as unknowns; also NWA14526 (lunar basalt) and NWA13190 (shergottite) compared with SN-ICP-MS" ;
    ada:signalCollectionMode "missing" ;
    ada:signalIntegrationIntervalMethod "Time-resolved signals inspected visually; flux blank contributions to pollution elements (V, Co, Zn, Ba, La, Ce, Ta, U) identified and subtracted; 9-spot grid homogeneity tested before analysis" ;
    ada:totalIntegrationTimePerOutputDataPointDefault -9999 ;
    ada:uncertaintyLevel "missing" ;
    bios:computationalTool [ schema1:name "Iolite 4 (Paton et al. 2011)" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Applied: dual detector mode (30 ms / 10 ms dwell alternation)" ;
    schema1:name "Pulse/Analog Detector Nonlinearity Correction" ;
    schema1:valueName "pulseAnalogDetectorNonlinearityCorrectionDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 15 ;
    schema1:description "Plasma gas flow: 15 l min⁻¹; Auxiliary gas: 0.85 l min⁻¹" ;
    schema1:name "Coolant Plasma Gas Flow Rate" ;
    schema1:valueName "coolantPlasmaGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproachDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Homogeneity index (H) applied to test element distribution; Co, Ni, Cu in high-Si glass (GSR-1) identified as near-LOD and flagged; flux blank contributions to pollution elements subtracted" ;
    schema1:name "Filtering Approach" ;
    schema1:valueName "filteringApproachDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Gas flows optimized via spot ablation of NIST SRM 612 to obtain maximum signal intensities while maintaining ThO/Th <0.3% and U/Th at 0.95–1.05" ;
    schema1:name "ICP Tuning" ;
    schema1:valueName "icpTuningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Unit resolution (quadrupole; ICP-MS/MS mode not specified)" ;
    schema1:name "Mass Resolution Setting" ;
    schema1:valueName "massResolutionSettingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "25 s washout between analyses (25 s gas blank → 45 s ablation → 25 s washout)" ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:valueName "memoryEffectMitigationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1550 ;
    schema1:description "1550 W" ;
    schema1:name "RF Power" ;
    schema1:valueName "rfPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/fusionFluxAndDilutionRatioDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Li₂B₄O₇ flux; sample:flux = 1:35 (10 mg sample + 350 mg flux)" ;
    schema1:name "Fusion Flux and Dilution Ratio" ;
    schema1:valueName "fusionFluxAndDilutionRatioDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/laserPulseDuration> a schema1:PropertyValueSpecification ;
    schema1:name "Laser Pulse Duration" ;
    schema1:value "Femtosecond (exact value not stated; GenesisGEO fs laser)" ;
    schema1:valueName "laserPulseDuration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/multiRunSequentialAnalysisDesign> a schema1:PropertyValueSpecification ;
    schema1:name "Multi Run Sequential Analysis Design" ;
    schema1:value "Single spot per location (45 s ablation at 1 Hz)" ;
    schema1:valueName "multiRunSequentialAnalysisDesign" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/preAblationSurfaceTreatmentDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Surface cleaning with ethanol before analysis" ;
    schema1:name "Pre Ablation Surface Treatment" ;
    schema1:valueName "preAblationSurfaceTreatmentDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/sampleFormAnalyticalSubstrateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Li-borate flux fusion glass disc (10 mg sample + 350 mg Li₂B₄O₇, 35:1 dilution)" ;
    schema1:name "Sample Form Analytical Substrate" ;
    schema1:valueName "sampleFormAnalyticalSubstrateDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/detectorConfiguration>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuningDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigationDefault> ;
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
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPowerDefault> ;
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

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/detectorConfiguration> a schema1:PropertyValue ;
    schema1:name "Detector Configuration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/detectorConfiguration> ;
    schema1:value "Dual mode detector (30 ms / 10 ms dwell alternation)" .


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
          "@id": "ada:parameter/module/LaserAblation/sampleFormAnalyticalSubstrateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleFormAnalyticalSubstrateDefault",
          "schema:name": "Sample Form Analytical Substrate",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "In situ — polished epoxy mount (experimental capsule half-section)"
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
        "schema:name": "Agilent 7900 (Q-ICP-MS)",
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
      "@id": "ada:parameter/module/ICPMS/makeUpGasAndFlowRateDefault",
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
      "@id": "ada:parameter/module/LaserAblation/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "multiRunSequentialAnalysisDesign",
      "schema:name": "Multi Run Sequential Analysis Design",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "Single spot per location (~40 s ablation at 7 Hz)"
    }
  ],
  "ada:analysisSequenceDefault": "NIST 610 as primary standard measured in session; NIST 612 and BCR-2G as monitoring standards; unknowns bracketed by standards",
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
            "@id": "ada:parameter/module/ICPMS/filteringApproachDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "filteringApproachDefault",
            "schema:name": "Filtering Approach",
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
  "ada:internalStandardApproach": "Single element from EMP: Si (SiO₂ from EMP for silicate glass); NIST 610 as external standard",
  "ada:elementalFractionationCorrection": [
    "Femtosecond laser reduces LIEF; NIST 610 external standard; Si IS from EMP corrects for ablation yield"
  ],
  "ada:calibrationMeasurementFrequency": "NIST 610 as primary; NIST 612 and BCR-2G as monitoring standards",
  "ada:internalStandardElement": "Si from EMP (SiO₂ wt% for silicate glass)",
  "ada:signalIntegrationIntervalMethod": "Time-resolved LA-ICP-MS signal inspected; micronuggets identified from spikes in Au signal and excluded from integration to obtain smooth signals (verified by Fig. 1 in paper)",
  "ada:secondaryReferenceMaterialDefault": [
    "NIST SRM 612 and BCR-2G (monitoring standards measured in same sessions)"
  ],
  "ada:primaryStandardNameDefault": "NIST 610 (primary external standard; Jochum et al. 2011); Si from EMP as IS",
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ageModelDefault": "missing",
  "ada:backgroundCountTimeDefault": -9999,
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:inheritedOrInitialSignalCorrectionDefault": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:massesMeasuredDefault": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:signalCollectionMode": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS-UPb/tapp/context.jsonld",
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
          "@id": "ada:parameter/module/LaserAblation/sampleFormAnalyticalSubstrateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleFormAnalyticalSubstrateDefault",
          "schema:name": "Sample Form Analytical Substrate",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "In situ \u2014 polished epoxy mount (experimental capsule half-section)"
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
        "schema:name": "Agilent 7900 (Q-ICP-MS)",
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
      "@id": "ada:parameter/module/ICPMS/makeUpGasAndFlowRateDefault",
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
      "@id": "ada:parameter/module/LaserAblation/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "multiRunSequentialAnalysisDesign",
      "schema:name": "Multi Run Sequential Analysis Design",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "Single spot per location (~40 s ablation at 7 Hz)"
    }
  ],
  "ada:analysisSequenceDefault": "NIST 610 as primary standard measured in session; NIST 612 and BCR-2G as monitoring standards; unknowns bracketed by standards",
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
            "@id": "ada:parameter/module/ICPMS/filteringApproachDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "filteringApproachDefault",
            "schema:name": "Filtering Approach",
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
  "ada:internalStandardApproach": "Single element from EMP: Si (SiO\u2082 from EMP for silicate glass); NIST 610 as external standard",
  "ada:elementalFractionationCorrection": [
    "Femtosecond laser reduces LIEF; NIST 610 external standard; Si IS from EMP corrects for ablation yield"
  ],
  "ada:calibrationMeasurementFrequency": "NIST 610 as primary; NIST 612 and BCR-2G as monitoring standards",
  "ada:internalStandardElement": "Si from EMP (SiO\u2082 wt% for silicate glass)",
  "ada:signalIntegrationIntervalMethod": "Time-resolved LA-ICP-MS signal inspected; micronuggets identified from spikes in Au signal and excluded from integration to obtain smooth signals (verified by Fig. 1 in paper)",
  "ada:secondaryReferenceMaterialDefault": [
    "NIST SRM 612 and BCR-2G (monitoring standards measured in same sessions)"
  ],
  "ada:primaryStandardNameDefault": "NIST 610 (primary external standard; Jochum et al. 2011); Si from EMP as IS",
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ageModelDefault": "missing",
  "ada:backgroundCountTimeDefault": -9999,
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:inheritedOrInitialSignalCorrectionDefault": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:massesMeasuredDefault": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:signalCollectionMode": "missing",
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
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproachDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/LaserAblation/multiRunSequentialAnalysisDesign> ;
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
                <https://ada.astromat.org/metadata/parameter/module/LaserAblation/sampleFormAnalyticalSubstrateDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Liu et al. (2025) GCA 393, 170; Xu et al. (2022) for experimental protocol" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:ablationPitDepthRateDefault "missing" ;
    ada:ablationSpotDurationDefault "~40 s (inferred from typical CetacAnalyte HE protocol for glass)" ;
    ada:ageModelDefault "missing" ;
    ada:analysisSequenceDefault "NIST 610 as primary standard measured in session; NIST 612 and BCR-2G as monitoring standards; unknowns bracketed by standards" ;
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
    ada:massesMeasuredDefault "missing" ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:primaryStandardNameDefault "NIST 610 (primary external standard; Jochum et al. 2011); Si from EMP as IS" ;
    ada:rasterLineSpacingDefault "missing" ;
    ada:sampleIntroduction "missing" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:secondaryReferenceMaterialDefault "NIST SRM 612 and BCR-2G (monitoring standards measured in same sessions)" ;
    ada:signalCollectionMode "missing" ;
    ada:signalIntegrationIntervalMethod "Time-resolved LA-ICP-MS signal inspected; micronuggets identified from spikes in Au signal and excluded from integration to obtain smooth signals (verified by Fig. 1 in paper)" ;
    ada:totalIntegrationTimePerOutputDataPointDefault -9999 ;
    ada:uncertaintyLevel "missing" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproachDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Micronuggets identified from Au signal spikes in time-resolved spectra; excluded from integration (smooth signals = fully dissolved Au; Fig. 1 shows this criterion)" ;
    schema1:name "Filtering Approach" ;
    schema1:valueName "filteringApproachDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N₂ or Ar mixed into He carrier for sensitivity optimization (amounts not stated)" ;
    schema1:name "Make-up Gas and Flow Rate" ;
    schema1:valueName "makeUpGasAndFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Unit resolution (quadrupole fixed)" ;
    schema1:name "Mass Resolution Setting" ;
    schema1:valueName "massResolutionSettingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/multiRunSequentialAnalysisDesign> a schema1:PropertyValueSpecification ;
    schema1:name "Multi Run Sequential Analysis Design" ;
    schema1:value "Single spot per location (~40 s ablation at 7 Hz)" ;
    schema1:valueName "multiRunSequentialAnalysisDesign" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/sampleFormAnalyticalSubstrateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "In situ — polished epoxy mount (experimental capsule half-section)" ;
    schema1:name "Sample Form Analytical Substrate" ;
    schema1:valueName "sampleFormAnalyticalSubstrateDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault> ;
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
          "@id": "ada:parameter/module/LaserAblation/sampleFormAnalyticalSubstrateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleFormAnalyticalSubstrateDefault",
          "schema:name": "Sample Form Analytical Substrate",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "In situ — polished epoxy mount (same capsule section as glass protocol)"
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
        "schema:name": "Agilent 7900 (Q-ICP-MS)",
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
      "@id": "ada:parameter/module/ICPMS/makeUpGasAndFlowRateDefault",
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
      "@id": "ada:parameter/module/LaserAblation/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "multiRunSequentialAnalysisDesign",
      "schema:name": "Multi Run Sequential Analysis Design",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "Single spot per location (sulfides; same acquisition parameters as glass but 20 µm spot)"
    }
  ],
  "ada:analysisSequenceDefault": "Same bracketing as silicate glass protocol",
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
            "@id": "ada:parameter/module/ICPMS/filteringApproachDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "filteringApproachDefault",
            "schema:name": "Filtering Approach",
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
  "ada:internalStandardApproach": "Single element from EMP: Fe (FeOT from EMP for sulfide); NIST 610 as external standard",
  "ada:elementalFractionationCorrection": [
    "Femtosecond laser reduces LIEF; NIST 610 external standard; Fe IS from EMP corrects for ablation yield; micronuggets identified from Au signal spikes and excluded from integration"
  ],
  "ada:calibrationMeasurementFrequency": "Same bracketing as silicate glass protocol",
  "ada:internalStandardElement": "Fe from EMP (FeOT wt% for sulfide)",
  "ada:signalIntegrationIntervalMethod": "Same approach as glass; micronugget identification from Au signal spikes critical for sulfide analyses",
  "ada:secondaryReferenceMaterialDefault": [
    "NIST SRM 612 and BCR-2G (same monitoring standard set as glass protocol)"
  ],
  "ada:primaryStandardNameDefault": "NIST 610 (primary external standard); Fe from EMP as IS",
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ageModelDefault": "missing",
  "ada:backgroundCountTimeDefault": -9999,
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:inheritedOrInitialSignalCorrectionDefault": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:massesMeasuredDefault": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:signalCollectionMode": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS-UPb/tapp/context.jsonld",
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
          "@id": "ada:parameter/module/LaserAblation/sampleFormAnalyticalSubstrateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleFormAnalyticalSubstrateDefault",
          "schema:name": "Sample Form Analytical Substrate",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "In situ \u2014 polished epoxy mount (same capsule section as glass protocol)"
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
        "schema:name": "Agilent 7900 (Q-ICP-MS)",
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
      "@id": "ada:parameter/module/ICPMS/makeUpGasAndFlowRateDefault",
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
      "@id": "ada:parameter/module/LaserAblation/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "multiRunSequentialAnalysisDesign",
      "schema:name": "Multi Run Sequential Analysis Design",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "Single spot per location (sulfides; same acquisition parameters as glass but 20 \u00b5m spot)"
    }
  ],
  "ada:analysisSequenceDefault": "Same bracketing as silicate glass protocol",
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
            "@id": "ada:parameter/module/ICPMS/filteringApproachDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "filteringApproachDefault",
            "schema:name": "Filtering Approach",
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
  "ada:internalStandardApproach": "Single element from EMP: Fe (FeOT from EMP for sulfide); NIST 610 as external standard",
  "ada:elementalFractionationCorrection": [
    "Femtosecond laser reduces LIEF; NIST 610 external standard; Fe IS from EMP corrects for ablation yield; micronuggets identified from Au signal spikes and excluded from integration"
  ],
  "ada:calibrationMeasurementFrequency": "Same bracketing as silicate glass protocol",
  "ada:internalStandardElement": "Fe from EMP (FeOT wt% for sulfide)",
  "ada:signalIntegrationIntervalMethod": "Same approach as glass; micronugget identification from Au signal spikes critical for sulfide analyses",
  "ada:secondaryReferenceMaterialDefault": [
    "NIST SRM 612 and BCR-2G (same monitoring standard set as glass protocol)"
  ],
  "ada:primaryStandardNameDefault": "NIST 610 (primary external standard); Fe from EMP as IS",
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ageModelDefault": "missing",
  "ada:backgroundCountTimeDefault": -9999,
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:inheritedOrInitialSignalCorrectionDefault": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:massesMeasuredDefault": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:signalCollectionMode": "missing",
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

ex:laQicpmsUPbTAPP-Liu2025-2 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproachDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Same capsule section as silicate glass; sulfide grains ≥20 µm selected by SEM-BSE" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/LaserAblation/multiRunSequentialAnalysisDesign> ;
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
                <https://ada.astromat.org/metadata/parameter/module/LaserAblation/sampleFormAnalyticalSubstrateDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Liu et al. (2025) GCA 393, 170; Xu et al. (2022)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:ablationPitDepthRateDefault "missing" ;
    ada:ablationSpotDurationDefault "~40 s (same protocol; grain size >20 µm selected)" ;
    ada:ageModelDefault "missing" ;
    ada:analysisSequenceDefault "Same bracketing as silicate glass protocol" ;
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
    ada:massesMeasuredDefault "missing" ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:primaryStandardNameDefault "NIST 610 (primary external standard); Fe from EMP as IS" ;
    ada:rasterLineSpacingDefault "missing" ;
    ada:sampleIntroduction "missing" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:secondaryReferenceMaterialDefault "NIST SRM 612 and BCR-2G (same monitoring standard set as glass protocol)" ;
    ada:signalCollectionMode "missing" ;
    ada:signalIntegrationIntervalMethod "Same approach as glass; micronugget identification from Au signal spikes critical for sulfide analyses" ;
    ada:totalIntegrationTimePerOutputDataPointDefault -9999 ;
    ada:uncertaintyLevel "missing" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproachDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Same approach as glass; Au spike identification critical for determining solubility vs. nugget contribution" ;
    schema1:name "Filtering Approach" ;
    schema1:valueName "filteringApproachDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N₂ or Ar mixed (same protocol as glass)" ;
    schema1:name "Make-up Gas and Flow Rate" ;
    schema1:valueName "makeUpGasAndFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Unit resolution (quadrupole fixed)" ;
    schema1:name "Mass Resolution Setting" ;
    schema1:valueName "massResolutionSettingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/multiRunSequentialAnalysisDesign> a schema1:PropertyValueSpecification ;
    schema1:name "Multi Run Sequential Analysis Design" ;
    schema1:value "Single spot per location (sulfides; same acquisition parameters as glass but 20 µm spot)" ;
    schema1:valueName "multiRunSequentialAnalysisDesign" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/sampleFormAnalyticalSubstrateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "In situ — polished epoxy mount (same capsule section as glass protocol)" ;
    schema1:name "Sample Form Analytical Substrate" ;
    schema1:valueName "sampleFormAnalyticalSubstrateDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault> ;
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
          "@id": "ada:parameter/module/LaserAblation/sampleFormAnalyticalSubstrateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleFormAnalyticalSubstrateDefault",
          "schema:name": "Sample Form Analytical Substrate",
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
      "@id": "ada:parameter/module/LaserAblation/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "multiRunSequentialAnalysisDesign",
      "schema:name": "Multi Run Sequential Analysis Design",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "Single spot analysis per location"
    }
  ],
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
  "ada:internalStandardApproach": "Normalization to 100 wt% oxide total (for silicates and oxides)",
  "ada:elementalFractionationCorrection": [
    "External calibration using NIST 610 glass standard analyzed before and after session; oxide-sum normalization corrects for ablation yield variation; no explicit downhole fractionation correction described"
  ],
  "ada:calibrationMeasurementFrequency": "NIST 610 glass standard analyzed before and after every session",
  "ada:blankBackgroundCorrectionMethod": "50 s background measurement before each analysis; background subtracted (method not explicitly described beyond counting duration)",
  "ada:internalStandardElement": "None (oxide sum normalization, 100 wt% total)",
  "ada:signalIntegrationIntervalMethod": "Time-lapse plots of each spot examined; only the plateau region used to quantify trace element abundances",
  "ada:primaryStandardNameDefault": "NIST 610 glass standard",
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
  "ada:massesMeasuredDefault": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:signalCollectionMode": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS-UPb/tapp/context.jsonld",
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
          "@id": "ada:parameter/module/LaserAblation/sampleFormAnalyticalSubstrateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleFormAnalyticalSubstrateDefault",
          "schema:name": "Sample Form Analytical Substrate",
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
      "@id": "ada:parameter/module/LaserAblation/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "multiRunSequentialAnalysisDesign",
      "schema:name": "Multi Run Sequential Analysis Design",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "Single spot analysis per location"
    }
  ],
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
  "ada:internalStandardApproach": "Normalization to 100 wt% oxide total (for silicates and oxides)",
  "ada:elementalFractionationCorrection": [
    "External calibration using NIST 610 glass standard analyzed before and after session; oxide-sum normalization corrects for ablation yield variation; no explicit downhole fractionation correction described"
  ],
  "ada:calibrationMeasurementFrequency": "NIST 610 glass standard analyzed before and after every session",
  "ada:blankBackgroundCorrectionMethod": "50 s background measurement before each analysis; background subtracted (method not explicitly described beyond counting duration)",
  "ada:internalStandardElement": "None (oxide sum normalization, 100 wt% total)",
  "ada:signalIntegrationIntervalMethod": "Time-lapse plots of each spot examined; only the plateau region used to quantify trace element abundances",
  "ada:primaryStandardNameDefault": "NIST 610 glass standard",
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
  "ada:massesMeasuredDefault": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:signalCollectionMode": "missing",
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

ex:laQicpmsUPbTAPP-Liu2016 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
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
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/LaserAblation/multiRunSequentialAnalysisDesign> ;
    schema1:datePublished "missing" ;
    schema1:description "Paper broadly follows Udry et al. (2012) and Pernet-Fisher et al. (2014) for procedure; two IS approaches used for different mineral phases (oxide-sum for silicates; EMP CaO for phosphate); 90 µm spot used on some olivines to evaluate whether low REE signals result from insufficient sampling volume" ;
    schema1:instrument <https://example.org/instrument/ICPMS>,
        <https://example.org/instrument/Laser-Ablation-System> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Department of Geosciences, Virginia Tech" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "LA-ICP-MS (193 nm excimer laser + ICP-MS; top-level technique)" ] ;
    schema1:name "laQicpmsUPb protocol — Liu2016" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Martian meteorite (Tissint) silicates, oxides, and glass: olivine, low-Ca pyroxene, augite, maskelynite, Fe-Ti-Cr oxides, shock melt glass, fusion crust" ],
                <https://ada.astromat.org/metadata/parameter/module/LaserAblation/sampleFormAnalyticalSubstrateDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Udry et al. (2012) and Pernet-Fisher et al. (2014) cited as broad references for the analytical procedure" ] ;
            schema1:url "https://ada.astromat.org/missing" ],
        [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "EPMA provides major element concentrations for comparison with LA-ICP-MS oxide-sum normalization results; agreement within <10% verified" ;
                    schema1:name "EPMA (EMP)" ] ;
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
    ada:massesMeasuredDefault "missing" ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:primaryStandardNameDefault "NIST 610 glass standard" ;
    ada:rasterLineSpacingDefault "missing" ;
    ada:sampleIntroduction "missing" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:signalCollectionMode "missing" ;
    ada:signalIntegrationIntervalMethod "Time-lapse plots of each spot examined; only the plateau region used to quantify trace element abundances" ;
    ada:totalIntegrationTimePerOutputDataPointDefault -9999 ;
    ada:uncertaintyLevel "missing" ;
    bios:computationalTool [ schema1:name "AMS ver. 1.0 (Mutchler et al. 2008; Analysis Management System, stand-alone software)" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/laserEnergyDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 150 ;
    schema1:description "150 mJ output energy" ;
    schema1:name "Laser Energy" ;
    schema1:valueName "laserEnergyDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/multiRunSequentialAnalysisDesign> a schema1:PropertyValueSpecification ;
    schema1:name "Multi Run Sequential Analysis Design" ;
    schema1:value "Single spot analysis per location" ;
    schema1:valueName "multiRunSequentialAnalysisDesign" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/sampleFormAnalyticalSubstrateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "In situ — polished thin section (Tissint sections: Tata-2-C3, Tata-3-C2, UT1, UT3)" ;
    schema1:name "Sample Form Analytical Substrate" ;
    schema1:valueName "sampleFormAnalyticalSubstrateDefault" ;
    ada:dataType "string" ;
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
          "@id": "ada:parameter/module/LaserAblation/sampleFormAnalyticalSubstrateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleFormAnalyticalSubstrateDefault",
          "schema:name": "Sample Form Analytical Substrate",
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
      "@id": "ada:parameter/module/LaserAblation/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "multiRunSequentialAnalysisDesign",
      "schema:name": "Multi Run Sequential Analysis Design",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "Single spot analysis per location"
    }
  ],
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
  "ada:internalStandardApproach": "Single element IS: EMP CaO concentration used; LA-ICP-MS 40Ca counts normalized to CaO from EMP analysis at the same spot",
  "ada:elementalFractionationCorrection": [
    "External calibration using NIST 610; EMP CaO as IS corrects for ablation yield; no explicit downhole correction described"
  ],
  "ada:calibrationMeasurementFrequency": "NIST 610 analyzed before and after every session (same as silicate protocol)",
  "ada:blankBackgroundCorrectionMethod": "50 s background measurement before each analysis (same as silicate protocol)",
  "ada:internalStandardElement": "40Ca; CaO wt% from EMP at the analysis spot",
  "ada:signalIntegrationIntervalMethod": "Time-lapse plots examined; only plateau region used (same as silicate protocol)",
  "ada:primaryStandardNameDefault": "NIST 610 glass standard",
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
  "ada:massesMeasuredDefault": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:signalCollectionMode": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS-UPb/tapp/context.jsonld",
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
          "@id": "ada:parameter/module/LaserAblation/sampleFormAnalyticalSubstrateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleFormAnalyticalSubstrateDefault",
          "schema:name": "Sample Form Analytical Substrate",
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
      "@id": "ada:parameter/module/LaserAblation/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "multiRunSequentialAnalysisDesign",
      "schema:name": "Multi Run Sequential Analysis Design",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:value": "Single spot analysis per location"
    }
  ],
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
  "ada:internalStandardApproach": "Single element IS: EMP CaO concentration used; LA-ICP-MS 40Ca counts normalized to CaO from EMP analysis at the same spot",
  "ada:elementalFractionationCorrection": [
    "External calibration using NIST 610; EMP CaO as IS corrects for ablation yield; no explicit downhole correction described"
  ],
  "ada:calibrationMeasurementFrequency": "NIST 610 analyzed before and after every session (same as silicate protocol)",
  "ada:blankBackgroundCorrectionMethod": "50 s background measurement before each analysis (same as silicate protocol)",
  "ada:internalStandardElement": "40Ca; CaO wt% from EMP at the analysis spot",
  "ada:signalIntegrationIntervalMethod": "Time-lapse plots examined; only plateau region used (same as silicate protocol)",
  "ada:primaryStandardNameDefault": "NIST 610 glass standard",
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
  "ada:massesMeasuredDefault": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:signalCollectionMode": "missing",
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

ex:laQicpmsUPbTAPP-Liu2016-2 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
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
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/LaserAblation/multiRunSequentialAnalysisDesign> ;
    schema1:datePublished "missing" ;
    schema1:description "N/A — see silicate column for general notes" ;
    schema1:instrument <https://example.org/instrument/ICPMS>,
        <https://example.org/instrument/Laser-Ablation-System> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Department of Geosciences, Virginia Tech" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "LA-ICP-MS (same as silicate protocol)" ] ;
    schema1:name "laQicpmsUPb protocol — Liu2016-2" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Martian meteorite (Tissint) phosphate: sodium-merrillite" ],
                <https://ada.astromat.org/metadata/parameter/module/LaserAblation/sampleFormAnalyticalSubstrateDefault> ] ;
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
    ada:massesMeasuredDefault "missing" ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:primaryStandardNameDefault "NIST 610 glass standard" ;
    ada:rasterLineSpacingDefault "missing" ;
    ada:sampleIntroduction "missing" ;
    ada:samplingUnit "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:signalCollectionMode "missing" ;
    ada:signalIntegrationIntervalMethod "Time-lapse plots examined; only plateau region used (same as silicate protocol)" ;
    ada:totalIntegrationTimePerOutputDataPointDefault -9999 ;
    ada:uncertaintyLevel "missing" ;
    bios:computationalTool [ schema1:name "AMS ver. 1.0 (Mutchler et al. 2008)" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/laserEnergyDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 150 ;
    schema1:description "150 mJ output energy" ;
    schema1:name "Laser Energy" ;
    schema1:valueName "laserEnergyDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/multiRunSequentialAnalysisDesign> a schema1:PropertyValueSpecification ;
    schema1:name "Multi Run Sequential Analysis Design" ;
    schema1:value "Single spot analysis per location" ;
    schema1:valueName "multiRunSequentialAnalysisDesign" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/sampleFormAnalyticalSubstrateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "In situ — polished thin section (same sections as silicate protocol)" ;
    schema1:name "Sample Form Analytical Substrate" ;
    schema1:valueName "sampleFormAnalyticalSubstrateDefault" ;
    ada:dataType "string" ;
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


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: LA-Q-ICP-MS U-Pb Geochronology TAPP (laQicpmsUPbTAPP)
description: Laser-ablation quadrupole ICP-MS U-Pb geochronology extension of the
  base TAPP definition, generated from TAPPS20260813/Current TAPPs/LA-Q-ICP-MS_UPb_TAPP_v16.csv
  via the path-driven pipeline.
allOf:
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/calibrationFactor/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/geochronology/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/uPb/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/analyte/schema.yaml#/$defs/ProcedureIdentification
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
                              - Silicate mineral
                              - Silicate glass
                              - Oxide
                              - Sulfide
                              - Carbonate
                              - Phosphate
                              - Metal or alloy
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
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Procedure_signalSmoothing
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_filteringApproach
                      - title: Pulse/Analog Detector Nonlinearity Correction
                        description: Whether a correction was applied for nonlinear
                          detector response at the transition between pulse-counting
                          and analog (and Faraday, for triple-mode instruments) detection
                          modes. Cross-calibration factors between detector modes
                          must be confirmed, typically measured each session. Record
                          'Applied' and describe the method, the detector modes involved
                          and the analytes affected; 'None' where a crossover exists
                          on this instrument but no correction was made, giving the
                          reason; and 'N/A' where the detector is pulse-counting only
                          and no crossover exists.
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
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_isotopeDilutionDataReductionMethod
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/aggregation/schema.yaml#/$defs/Param_Procedure_analysisInclusionAndRejectionCriteria
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/uPb/schema.yaml#/$defs/Param_Procedure_intermediateDaughterDisequilibriumCorrection
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Procedure_constantsReferenceValues
                    allOf:
                    - contains:
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Procedure_signalSmoothing
                      minContains: 0
                      maxContains: 1
                    - contains:
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_filteringApproach
                      minContains: 0
                      maxContains: 1
                    - contains:
                        title: Pulse/Analog Detector Nonlinearity Correction
                        description: Whether a correction was applied for nonlinear
                          detector response at the transition between pulse-counting
                          and analog (and Faraday, for triple-mode instruments) detection
                          modes. Cross-calibration factors between detector modes
                          must be confirmed, typically measured each session. Record
                          'Applied' and describe the method, the detector modes involved
                          and the analytes affected; 'None' where a crossover exists
                          on this instrument but no correction was made, giving the
                          reason; and 'N/A' where the detector is pulse-counting only
                          and no crossover exists.
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
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_isotopeDilutionDataReductionMethod
                      minContains: 0
                      maxContains: 1
                    - contains:
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/aggregation/schema.yaml#/$defs/Param_Procedure_analysisInclusionAndRejectionCriteria
                      minContains: 0
                      maxContains: 1
                    - contains:
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/uPb/schema.yaml#/$defs/Param_Procedure_intermediateDaughterDisequilibriumCorrection
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
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Procedure_preAnalysisImagingAndScreening
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Procedure_transectRateMappingRateOrStepSize
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_makeUpGasAndFlowRate
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_instrumentWarmUpSessionDurationLimit
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Procedure_multiRunSequentialAnalysisDesign
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Procedure_matrixOffsetCorrectionLief
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/uPb/schema.yaml#/$defs/Param_Procedure_discordanceDefinitionAndValues
        - title: Error Correlation Between Reported Quantities
          description: The correlation coefficient between pairs of reported quantities
            whose uncertainties are not independent, together with the pair it applies
            to and how it was obtained.
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
      allOf:
      - contains:
          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Procedure_preAnalysisImagingAndScreening
        minContains: 0
        maxContains: 1
      - contains:
          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Procedure_transectRateMappingRateOrStepSize
        minContains: 0
        maxContains: 1
      - contains:
          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_makeUpGasAndFlowRate
        minContains: 0
        maxContains: 1
      - contains:
          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_instrumentWarmUpSessionDurationLimit
        minContains: 0
        maxContains: 1
      - contains:
          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Procedure_multiRunSequentialAnalysisDesign
        minContains: 0
        maxContains: 1
      - contains:
          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Procedure_matrixOffsetCorrectionLief
        minContains: 0
        maxContains: 1
      - contains:
          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/uPb/schema.yaml#/$defs/Param_Procedure_discordanceDefinitionAndValues
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
                  - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_instrumentSerialNumberOrLabIdentifier
                  - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_massResolutionSetting
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
                      The acceptable threshold is typically <1% or <3%. Record both
                      the threshold and the measured value.
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
                  - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_memoryEffectMitigation
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
                      The acceptable threshold is typically <1% or <3%. Record both
                      the threshold and the measured value.
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
                    $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_memoryEffectMitigation
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
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_coolantPlasmaGasFlowRate
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_auxiliaryGasFlowRate
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_rfPower
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_plasmaThermalMode
                          allOf:
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_coolantPlasmaGasFlowRate
                            minContains: 0
                            maxContains: 1
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_auxiliaryGasFlowRate
                            minContains: 0
                            maxContains: 1
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_rfPower
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
                  const: ada:analyteColumn/laQicpmsUPbTAPP/monitoredMasses
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
              description: Count (dwell) time at the mass position, in milliseconds.
                Where the procedure defines it per sweep or per scan rather than per
                measurement, state that basis.
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
            - title: Per-Analyte Calibration Strategy
              description: Approach used to convert measured ion signals to reported
                concentrations, and specifically any case where different analytes
                or analyte groups within one procedure are calibrated differently
                - different primary standards for different mass ranges or phases,
                or one element serving as internal standard while others are externally
                calibrated. Where a single strategy applies to all analytes, record
                that strategy. Where the procedure reports isotope ratios only and
                no concentrations, record 'Not applicable (isotope ratios only)'.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/laQicpmsUPbTAPP/perAnalyteCalibrationStrategy
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: perAnalyteCalibrationStrategy
                schema:name:
                  const: Per-Analyte Calibration Strategy
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
            - title: Spectral Interference Corrections Applied
              description: Whether mathematical corrections for isobaric, polyatomic
                or residual interferences are applied in data reduction, supplementary
                to any suppression already achieved by chemical separation, mass resolution,
                or a collision/reaction cell. Detail for each affected mass is carried
                by Interfering Species and Interference Correction Method.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/laQicpmsUPbTAPP/spectralInterferenceCorrectionsApplied
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
              description: Equation or procedure used to calculate and remove each
                interference contribution, together with how its magnitude was established
                - a monitor mass measured simultaneously and scaled by natural abundance
                ratios, a production-rate factor measured on a reference material
                or interference standard solution, or a tailing factor measured on
                a pure standard. Name the reference material used.
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
              description: "Precision of measurements across multiple analytical sessions
                over weeks to months \u2014 long-term or intermediate precision \u2014
                and the method used to assess it. Report both the assessment method
                and the precision values, specifying the reference material, the number
                of measurements and sessions, the time span covered, and the statistic
                reported."
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
                  const: ada:analyteColumn/laQicpmsUPbTAPP/monitoredMasses
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
              description: Count (dwell) time at the mass position, in milliseconds.
                Where the procedure defines it per sweep or per scan rather than per
                measurement, state that basis.
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
              title: Per-Analyte Calibration Strategy
              description: Approach used to convert measured ion signals to reported
                concentrations, and specifically any case where different analytes
                or analyte groups within one procedure are calibrated differently
                - different primary standards for different mass ranges or phases,
                or one element serving as internal standard while others are externally
                calibrated. Where a single strategy applies to all analytes, record
                that strategy. Where the procedure reports isotope ratios only and
                no concentrations, record 'Not applicable (isotope ratios only)'.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/laQicpmsUPbTAPP/perAnalyteCalibrationStrategy
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: perAnalyteCalibrationStrategy
                schema:name:
                  const: Per-Analyte Calibration Strategy
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
              title: Spectral Interference Corrections Applied
              description: Whether mathematical corrections for isobaric, polyatomic
                or residual interferences are applied in data reduction, supplementary
                to any suppression already achieved by chemical separation, mass resolution,
                or a collision/reaction cell. Detail for each affected mass is carried
                by Interfering Species and Interference Correction Method.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/laQicpmsUPbTAPP/spectralInterferenceCorrectionsApplied
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
              description: Equation or procedure used to calculate and remove each
                interference contribution, together with how its magnitude was established
                - a monitor mass measured simultaneously and scaled by natural abundance
                ratios, a production-rate factor measured on a reference material
                or interference standard solution, or a tailing factor measured on
                a pure standard. Name the reference material used.
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
              description: "Precision of measurements across multiple analytical sessions
                over weeks to months \u2014 long-term or intermediate precision \u2014
                and the method used to assess it. Report both the assessment method
                and the precision values, specifying the reference material, the number
                of measurements and sessions, the time span covered, and the statistic
                reported."
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
    ada:massesMeasuredDefault:
      description: Specific masses monitored in this procedure, grouped by the analyte
        element they serve where they serve one. Covers atomic isotopes and, where
        a reaction cell shifts an analyte onto a different mass, the product mass
        actually measured. Includes interference-monitor and internal-standard masses,
        which serve no analyte and so have no parent element. The analyte list is
        given by the Analyte field and is never inferred from the element symbols
        appearing here.
      type: string
      readOnly: true
    ada:signalCollectionMode:
      description: Mode used to collect ion signal across the monitored masses. In
        peak hopping mode, the quadrupole jumps sequentially between pre-set mass
        positions and dwells at each peak; in scanning mode, the quadrupole sweeps
        continuously across a defined mass range.
      type: string
      enum:
      - Peak hopping
      - Scanning
      - N/A
      - None
      - missing
      readOnly: true
    ada:massBiasCorrectionStrategy:
      description: 'Strategy used to correct instrumental isotopic mass fractionation,
        also called mass bias or mass discrimination. Distinct from Elemental Fractionation
        Correction, which addresses inter-element fractionation during ablation and
        transport: this field addresses discrimination between isotopes of the same
        element, and applies wherever the procedure reports isotope ratios.'
      type: string
      readOnly: true
    ada:totalIntegrationTimePerOutputDataPointDefault:
      description: "Total duty-cycle time for one complete mass-scan sweep \u2014
        the sum of all per-isotope dwell times plus inter-mass settling times. Not
        recoverable from Dwell Time per Mass alone, because settling time is not captured
        there. Applies to sequential (quadrupole and single-collector sector-field)
        acquisition."
      anyOf:
      - type: number
      - type: string
    ada:analyticalMode:
      type: array
      items:
        type: string
        enum:
        - Spot
        - Transect
        - Mapping
  required:
  - ada:massesMeasuredDefault
  - ada:signalCollectionMode
  - ada:massBiasCorrectionStrategy
  - ada:totalIntegrationTimePerOutputDataPointDefault

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS-UPb/tapp/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS-UPb/tapp/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS-UPb/tapp/context.jsonld)

## Sources

* [LA-Q-ICP-MS_UPb_TAPP_v16.csv (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/LA-Q-ICPMS-UPb/tapp`

