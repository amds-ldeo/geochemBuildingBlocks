
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
  "schema:description": "laQicpmsTAPP instance derived from Nakanishi et al. 2022 (GCA 319) CR chondrite metal (HSE) Spot analysis fs-LA-Q-ICP-MS Tokyo Institute of Technology (publication column of LA-Q-ICP-MS_TAPP_v96.csv).",
  "ada:targetMaterialTemplate": {
    "ada:targetMaterialDeclaration": "CR chondrite metal — interior, margin and isolated metal grains (p.1); the IVB iron meteorites are the standards",
    "ada:targetMaterialColumns": [
      {
        "schema:valueName": "targetMaterial",
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
        "@id": "ada:targetMaterialColumn/laQicpmsTAPP/primaryCalibrationStandardName",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "primaryCalibrationStandardName",
        "schema:name": "Primary Calibration Standard Name",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ],
    "ada:defaultTargetMaterials": []
  },
  "ada:samplingUnitSelectionCriteriaDefault": "Picked off prior electron images — \"Based on the secondary electron images taken by EPMA, we selected analytical spots for LA-ICP-MS and sampling spots for micro-milling\" (p.4); the grains themselves are sorted by setting into interior, margin and isolated metal (p.1)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "preAnalysisImagingAndScreeningDefault",
      "schema:name": "Pre-Analysis Imaging and Screening",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Secondary-electron imaging on the EPMA, used to place every spot — \"Based on the secondary electron images taken by EPMA, we selected analytical spots for LA-ICP-MS and sampling spots for micro-milling\" (p.4); the spots carry numbers (\"spot No.\" 201, 202 …) that tie the analyses back to those images (table p.6)"
    },
    {
      "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSizeDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "transectRateMappingRateOrStepSizeDefault",
      "schema:name": "Transect Rate Mapping Rate or Step Size",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N/A — spot mode"
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
      "schema:defaultValue": 0.9,
      "schema:description": "Ar, 0.9–1.2 L/min — Table 1, 'Make-up gas'"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/interPassDataDependency",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/interPassDataDependency"
        }
      ],
      "schema:name": "Inter-Pass Data Dependency",
      "schema:value": "N/A — a single acquisition pass"
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
              "schema:value": "Nickel micro-skimmer cone, Xs; nickel sampler cone — Table 1"
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
              "schema:defaultValue": 16,
              "schema:description": "Ar, plasma gas 16 L/min; cool gas 12–13 L/min — Table 1 lists both rows under 'Ar gas flow rate'"
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
              "schema:defaultValue": 0.6,
              "schema:description": "Ar, 0.6–1.2 L/min — Table 1, 'Auxiliary'"
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
          "schema:additionalType": [
            "Torch",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "Quartz torch with quartz injector — Table 1",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Torch"
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
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/ICPMS",
      "schema:name": "example instrumentName",
      "schema:manufacturer": {
        "schema:name": "missing",
        "@type": [
          "schema:Organization"
        ]
      }
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
      "ada:laserSpotGeometryDefault": "all: 30 µm diameter — 'Each spot analysis on the sample produced a pit of 30 µm in diameter' (p.3)",
      "ada:laserFluenceDefault": "12 J cm⁻²",
      "ada:laserRepetitionRateDefault": "all: 20 Hz",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/Laser-Ablation-System",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:carrierGasFlowRateDefault": "Ar, 0.6 L/min — Table 1, under 'Ar gas flow rate': 'Carrier gas 0.6 L/min'",
  "ada:analysisSequenceDefault": "N — Warburton Range and Tawallah Valley 'were used as an external standard and a secondary standard, respectively' (p.3); the order of analyses is not described",
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Co",
      "Ru",
      "Rh",
      "Pd",
      "Re",
      "Os",
      "Ir",
      "Pt",
      "Au"
    ],
    "ada:targetSpeciesColumns": [
      {
        "schema:valueName": "targetSpecies",
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
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Thick sections embedded in petropoxy 154 resin, the surface finalised by polishing with 0.5 µm diamond paste; carbon-coated before the EPMA measurements (§2.1–2.2). Whether the coat was removed before ablation is not stated; the later 0.5 µm polish (§2.5) preceded micromilling, not ablation",
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
            "@id": "ada:parameter/module/ICPMS/filteringApproachDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "filteringApproachDefault",
            "schema:name": "Filtering Approach",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "N — ²⁴Mg, ²⁹Si, ³¹P and ³³S 'were simultaneously monitored to check the involvement of micro-inclusions' (p.3); what was done with an affected analysis is not stated"
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
      "schema:name": "N — the JSPS Grants-in-Aid support the study as a whole and are recorded under Funding Source for Analysis"
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
  "ada:samplingUnitType": "Grain > Spot — HSE abundances are reported per metal grain, each with its LA \"spot No.\" (table p.6); the grains are typed by where they sit — interior grains in a chondrule, margin grains in its surficial shell, isolated grains in the matrix (p.1)",
  "ada:reportedProperties": [
    "Ru, Rh, Pd, Re, Os, Ir, Pt, Au (ppm); HSE/Ir ratios; Re/Os abundance ratio — HSE abundances in metal, e.g. 'Ir abundance ranging from 1.08 to 2.53 ppm' (p.5), with major element abundances from EPMA alongside; the Re/Os abundance ratio feeds the reported 187Re/188Os, 'determined by the mean Re/Os abundance ratios for each of the 1–3 analytical spots measured by LA-ICP-MS' (Table 3, p.8)"
  ],
  "ada:ablationSamplingMode": [
    "all: Spot — 'ablated by a spot analysis mode' (p.3)"
  ],
  "ada:rasterLineSpacingDefault": "N/A — spot mode",
  "ada:internalStandardApproach": "all: single element, its concentration measured by EPMA at the ablated spot — '61Ni was monitored for internal standardization. The concentration of Ni in the ablated spot was obtained by EPMA' (p.3)",
  "ada:elementalFractionationCorrection": [
    "N — quantification is by 'the calibration curve method' against Warburton Range with ⁶¹Ni internal standardization (p.3); no fractionation correction as such is described"
  ],
  "ada:blankBackgroundCorrectionMethod": "N — the signal 'decayed to the background level immediately after the end of ablation' (p.3); the background correction is not described",
  "ada:internalStandardElement": "all: Ni (⁶¹Ni) — concentration from EPMA at the ablated spot (p.3)",
  "ada:signalIntegrationIntervalMethod": "N — the paper says only that 'the intensities of individual isotopes rapidly increased to the maximum and decayed to the background level immediately after the end of ablation' (p.3)",
  "ada:secondaryReferenceMaterialDefault": [
    "Tawallah Valley (IVB iron meteorite) — 'used as ... a secondary standard' (p.3), its HSE abundances from Walker et al. (2008)"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ablationSpotDurationDefault": -9999,
  "ada:backgroundCountTimeDefault": -9999,
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:sampleIntroduction": "missing",
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
  "schema:description": "laQicpmsTAPP instance derived from Nakanishi et al. 2022 (GCA 319) CR chondrite metal (HSE) Spot analysis fs-LA-Q-ICP-MS Tokyo Institute of Technology (publication column of LA-Q-ICP-MS_TAPP_v96.csv).",
  "ada:targetMaterialTemplate": {
    "ada:targetMaterialDeclaration": "CR chondrite metal \u2014 interior, margin and isolated metal grains (p.1); the IVB iron meteorites are the standards",
    "ada:targetMaterialColumns": [
      {
        "schema:valueName": "targetMaterial",
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
        "@id": "ada:targetMaterialColumn/laQicpmsTAPP/primaryCalibrationStandardName",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "primaryCalibrationStandardName",
        "schema:name": "Primary Calibration Standard Name",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ],
    "ada:defaultTargetMaterials": []
  },
  "ada:samplingUnitSelectionCriteriaDefault": "Picked off prior electron images \u2014 \"Based on the secondary electron images taken by EPMA, we selected analytical spots for LA-ICP-MS and sampling spots for micro-milling\" (p.4); the grains themselves are sorted by setting into interior, margin and isolated metal (p.1)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "preAnalysisImagingAndScreeningDefault",
      "schema:name": "Pre-Analysis Imaging and Screening",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Secondary-electron imaging on the EPMA, used to place every spot \u2014 \"Based on the secondary electron images taken by EPMA, we selected analytical spots for LA-ICP-MS and sampling spots for micro-milling\" (p.4); the spots carry numbers (\"spot No.\" 201, 202 \u2026) that tie the analyses back to those images (table p.6)"
    },
    {
      "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSizeDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "transectRateMappingRateOrStepSizeDefault",
      "schema:name": "Transect Rate Mapping Rate or Step Size",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N/A \u2014 spot mode"
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
      "schema:defaultValue": 0.9,
      "schema:description": "Ar, 0.9\u20131.2 L/min \u2014 Table 1, 'Make-up gas'"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/interPassDataDependency",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/interPassDataDependency"
        }
      ],
      "schema:name": "Inter-Pass Data Dependency",
      "schema:value": "N/A \u2014 a single acquisition pass"
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
              "schema:value": "Nickel micro-skimmer cone, Xs; nickel sampler cone \u2014 Table 1"
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
              "schema:defaultValue": 16,
              "schema:description": "Ar, plasma gas 16 L/min; cool gas 12\u201313 L/min \u2014 Table 1 lists both rows under 'Ar gas flow rate'"
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
              "schema:defaultValue": 0.6,
              "schema:description": "Ar, 0.6\u20131.2 L/min \u2014 Table 1, 'Auxiliary'"
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
          "schema:additionalType": [
            "Torch",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "Quartz torch with quartz injector \u2014 Table 1",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/ICPMS/part/Torch"
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
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/ICPMS",
      "schema:name": "example instrumentName",
      "schema:manufacturer": {
        "schema:name": "missing",
        "@type": [
          "schema:Organization"
        ]
      }
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
      "ada:laserSpotGeometryDefault": "all: 30 \u00b5m diameter \u2014 'Each spot analysis on the sample produced a pit of 30 \u00b5m in diameter' (p.3)",
      "ada:laserFluenceDefault": "12 J cm\u207b\u00b2",
      "ada:laserRepetitionRateDefault": "all: 20 Hz",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/Laser-Ablation-System",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:carrierGasFlowRateDefault": "Ar, 0.6 L/min \u2014 Table 1, under 'Ar gas flow rate': 'Carrier gas 0.6 L/min'",
  "ada:analysisSequenceDefault": "N \u2014 Warburton Range and Tawallah Valley 'were used as an external standard and a secondary standard, respectively' (p.3); the order of analyses is not described",
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Co",
      "Ru",
      "Rh",
      "Pd",
      "Re",
      "Os",
      "Ir",
      "Pt",
      "Au"
    ],
    "ada:targetSpeciesColumns": [
      {
        "schema:valueName": "targetSpecies",
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
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Thick sections embedded in petropoxy 154 resin, the surface finalised by polishing with 0.5 \u00b5m diamond paste; carbon-coated before the EPMA measurements (\u00a72.1\u20132.2). Whether the coat was removed before ablation is not stated; the later 0.5 \u00b5m polish (\u00a72.5) preceded micromilling, not ablation",
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
            "@id": "ada:parameter/module/ICPMS/filteringApproachDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "filteringApproachDefault",
            "schema:name": "Filtering Approach",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "N \u2014 \u00b2\u2074Mg, \u00b2\u2079Si, \u00b3\u00b9P and \u00b3\u00b3S 'were simultaneously monitored to check the involvement of micro-inclusions' (p.3); what was done with an affected analysis is not stated"
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
      "schema:name": "N \u2014 the JSPS Grants-in-Aid support the study as a whole and are recorded under Funding Source for Analysis"
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
  "ada:samplingUnitType": "Grain > Spot \u2014 HSE abundances are reported per metal grain, each with its LA \"spot No.\" (table p.6); the grains are typed by where they sit \u2014 interior grains in a chondrule, margin grains in its surficial shell, isolated grains in the matrix (p.1)",
  "ada:reportedProperties": [
    "Ru, Rh, Pd, Re, Os, Ir, Pt, Au (ppm); HSE/Ir ratios; Re/Os abundance ratio \u2014 HSE abundances in metal, e.g. 'Ir abundance ranging from 1.08 to 2.53 ppm' (p.5), with major element abundances from EPMA alongside; the Re/Os abundance ratio feeds the reported 187Re/188Os, 'determined by the mean Re/Os abundance ratios for each of the 1\u20133 analytical spots measured by LA-ICP-MS' (Table 3, p.8)"
  ],
  "ada:ablationSamplingMode": [
    "all: Spot \u2014 'ablated by a spot analysis mode' (p.3)"
  ],
  "ada:rasterLineSpacingDefault": "N/A \u2014 spot mode",
  "ada:internalStandardApproach": "all: single element, its concentration measured by EPMA at the ablated spot \u2014 '61Ni was monitored for internal standardization. The concentration of Ni in the ablated spot was obtained by EPMA' (p.3)",
  "ada:elementalFractionationCorrection": [
    "N \u2014 quantification is by 'the calibration curve method' against Warburton Range with \u2076\u00b9Ni internal standardization (p.3); no fractionation correction as such is described"
  ],
  "ada:blankBackgroundCorrectionMethod": "N \u2014 the signal 'decayed to the background level immediately after the end of ablation' (p.3); the background correction is not described",
  "ada:internalStandardElement": "all: Ni (\u2076\u00b9Ni) \u2014 concentration from EPMA at the ablated spot (p.3)",
  "ada:signalIntegrationIntervalMethod": "N \u2014 the paper says only that 'the intensities of individual isotopes rapidly increased to the maximum and decayed to the background level immediately after the end of ablation' (p.3)",
  "ada:secondaryReferenceMaterialDefault": [
    "Tawallah Valley (IVB iron meteorite) \u2014 'used as ... a secondary standard' (p.3), its HSE abundances from Walker et al. (2008)"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ablationSpotDurationDefault": -9999,
  "ada:backgroundCountTimeDefault": -9999,
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:sampleIntroduction": "missing",
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
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:laQicpmsTAPP-Nakanishi2022> a cdi:Activity,
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
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Thick sections embedded in petropoxy 154 resin, the surface finalised by polishing with 0.5 µm diamond paste; carbon-coated before the EPMA measurements (§2.1–2.2). Whether the coat was removed before ablation is not stated; the later 0.5 µm polish (§2.5) preceded micromilling, not ablation" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/interPassDataDependency>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSizeDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Nakanishi, Yokoyama, Okabayashi, Iwamori, Hirata" ] ;
    schema1:datePublished "missing" ;
    schema1:description "laQicpmsTAPP instance derived from Nakanishi et al. 2022 (GCA 319) CR chondrite metal (HSE) Spot analysis fs-LA-Q-ICP-MS Tokyo Institute of Technology (publication column of LA-Q-ICP-MS_TAPP_v96.csv)." ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "N — the JSPS Grants-in-Aid support the study as a whole and are recorded under Funding Source for Analysis" ] ;
    schema1:instrument <ex:instrument/ICPMS>,
        <ex:instrument/Laser-Ablation-System> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Dept. of Earth and Planetary Sciences, Tokyo Institute of Technology, Japan" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "fs-LA-Q-ICP-MS" ] ;
    schema1:name "Nakanishi et al. (2022) CR Chondrite Metal HSE fs-LA-ICP-MS Spot v1" ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Nakanishi et al. (2022) GCA 319, 254; Walker et al. (2008) for IVB standards" ] ;
            schema1:url "https://ada.astromat.org/missing" ],
        [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "EPMA used to measure Ni concentration at the exact LA-ICP-MS analysis spot location, required for internal standardization of HSE data [Section 2.3]" ;
                    schema1:name "EPMA (electron probe microanalysis)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:ablationPitDepthRateDefault "missing" ;
    ada:ablationSamplingMode "all: Spot — 'ablated by a spot analysis mode' (p.3)" ;
    ada:ablationSpotDurationDefault -9999 ;
    ada:analysisSequenceDefault "N — Warburton Range and Tawallah Valley 'were used as an external standard and a secondary standard, respectively' (p.3); the order of analyses is not described" ;
    ada:backgroundCountTimeDefault -9999 ;
    ada:blankBackgroundCorrectionMethod "N — the signal 'decayed to the background level immediately after the end of ablation' (p.3); the background correction is not described" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:carrierGasFlowRateDefault "Ar, 0.6 L/min — Table 1, under 'Ar gas flow rate': 'Carrier gas 0.6 L/min'" ;
    ada:constantsAndReferenceValuesUsedDefault "missing" ;
    ada:elementalFractionationCorrection "N — quantification is by 'the calibration curve method' against Warburton Range with ⁶¹Ni internal standardization (p.3); no fractionation correction as such is described" ;
    ada:internalStandardApproach "all: single element, its concentration measured by EPMA at the ablated spot — '61Ni was monitored for internal standardization. The concentration of Ni in the ablated spot was obtained by EPMA' (p.3)" ;
    ada:internalStandardElement "all: Ni (⁶¹Ni) — concentration from EPMA at the ablated spot (p.3)" ;
    ada:massBiasCorrectionStrategy "missing" ;
    ada:numberOfAcquisitionPasses -9999 ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:rasterLineSpacingDefault "N/A — spot mode" ;
    ada:reportedProperties "Ru, Rh, Pd, Re, Os, Ir, Pt, Au (ppm); HSE/Ir ratios; Re/Os abundance ratio — HSE abundances in metal, e.g. 'Ir abundance ranging from 1.08 to 2.53 ppm' (p.5), with major element abundances from EPMA alongside; the Re/Os abundance ratio feeds the reported 187Re/188Os, 'determined by the mean Re/Os abundance ratios for each of the 1–3 analytical spots measured by LA-ICP-MS' (Table 3, p.8)" ;
    ada:sampleIntroduction "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "Picked off prior electron images — \"Based on the secondary electron images taken by EPMA, we selected analytical spots for LA-ICP-MS and sampling spots for micro-milling\" (p.4); the grains themselves are sorted by setting into interior, margin and isolated metal (p.1)" ;
    ada:samplingUnitType "Grain > Spot — HSE abundances are reported per metal grain, each with its LA \"spot No.\" (table p.6); the grains are typed by where they sit — interior grains in a chondrule, margin grains in its surficial shell, isolated grains in the matrix (p.1)" ;
    ada:secondaryReferenceMaterialDefault "Tawallah Valley (IVB iron meteorite) — 'used as ... a secondary standard' (p.3), its HSE abundances from Walker et al. (2008)" ;
    ada:signalCollectionMode "missing" ;
    ada:signalIntegrationIntervalMethod "N — the paper says only that 'the intensities of individual isotopes rapidly increased to the maximum and decayed to the background level immediately after the end of ablation' (p.3)" ;
    ada:targetMaterialTemplate [ ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/laQicpmsTAPP/primaryCalibrationStandardName> ;
            ada:targetMaterialDeclaration "CR chondrite metal — interior, margin and isolated metal grains (p.1); the IVB iron meteorites are the standards" ] ;
    ada:targetSpeciesTemplate [ ada:defaultTargetSpecies "Au",
                "Co",
                "Ir",
                "Os",
                "Pd",
                "Pt",
                "Re",
                "Rh",
                "Ru" ;
            ada:targetSpeciesColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetSpecies" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/calibrationStrategyPerTargetSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/monitoredMasses>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/spectralInterferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ] ;
    ada:totalIntegrationTimePerOutputDataPointDefault -9999 ;
    ada:uncertaintyLevel "missing" .

<ex:instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Single-collector quadrupole (Q-ICP-MS)" ;
    schema1:hasPart <ex:instrument/ICPMS/part/Collision-Reaction-Cell>,
        <ex:instrument/ICPMS/part/ICP-Source>,
        <ex:instrument/ICPMS/part/Interface-Cone>,
        <ex:instrument/ICPMS/part/Torch> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "missing" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Thermo Scientific X-series 2 (Q-ICP-MS)" ] ;
    schema1:name "example instrumentName" .

<ex:instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "missing" .

<ex:instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPowerDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<ex:instrument/ICPMS/part/Interface-Cone> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/configuration> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Interface Cone" ;
    schema1:name "missing" .

<ex:instrument/ICPMS/part/Torch> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Torch" ;
    schema1:name "Quartz torch with quartz injector — Table 1" .

<ex:instrument/Laser-Ablation-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/LaserAblation/laserPulseDuration> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Laser Ablation System" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Cyber Laser IFRIT (Ti:sapphire fs UV laser, 260 nm)" ] ;
    schema1:name "example instrumentName" ;
    ada:laserFluenceDefault "12 J cm⁻²" ;
    ada:laserRepetitionRateDefault "all: 20 Hz" ;
    ada:laserSpotGeometryDefault "all: 30 µm diameter — 'Each spot analysis on the sample produced a pit of 30 µm in diameter' (p.3)" ;
    ada:laserType "260 nm Ti:sapphire femtosecond UV; pulse duration ~220 fs (IFRIT system)" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 6e-01 ;
    schema1:description "Ar, 0.6–1.2 L/min — Table 1, 'Auxiliary'" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:valueName "auxiliaryGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/configuration> a schema1:PropertyValueSpecification ;
    schema1:name "Configuration" ;
    schema1:value "Nickel micro-skimmer cone, Xs; nickel sampler cone — Table 1" ;
    schema1:valueName "configuration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 16 ;
    schema1:description "Ar, plasma gas 16 L/min; cool gas 12–13 L/min — Table 1 lists both rows under 'Ar gas flow rate'" ;
    schema1:name "Coolant Plasma Gas Flow Rate" ;
    schema1:valueName "coolantPlasmaGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproachDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N — ²⁴Mg, ²⁹Si, ³¹P and ³³S 'were simultaneously monitored to check the involvement of micro-inclusions' (p.3); what was done with an affected analysis is not stated" ;
    schema1:name "Filtering Approach" ;
    schema1:valueName "filteringApproachDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 9e-01 ;
    schema1:description "Ar, 0.9–1.2 L/min — Table 1, 'Make-up gas'" ;
    schema1:name "Make-up Gas and Flow Rate" ;
    schema1:valueName "makeUpGasAndFlowRateDefault" ;
    ada:dataType "number" ;
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

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSizeDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N/A — spot mode" ;
    schema1:name "Transect Rate Mapping Rate or Step Size" ;
    schema1:valueName "transectRateMappingRateOrStepSizeDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Secondary-electron imaging on the EPMA, used to place every spot — \"Based on the secondary electron images taken by EPMA, we selected analytical spots for LA-ICP-MS and sampling spots for micro-milling\" (p.4); the spots carry numbers (\"spot No.\" 201, 202 …) that tie the analyses back to those images (table p.6)" ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:valueName "preAnalysisImagingAndScreeningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/targetMaterialColumn/laQicpmsTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/calibrationStrategyPerTargetSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Calibration Strategy per Target Species" ;
    schema1:valueName "calibrationStrategyPerTargetSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Internal (Within-Measurement) Analytical Precision and Assessment Method" ;
    schema1:valueName "internalAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/monitoredMasses> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Monitored Masses" ;
    schema1:valueName "monitoredMasses" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/spectralInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Spectral Interference Corrections Applied" ;
    schema1:valueName "spectralInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/interPassDataDependency> a schema1:PropertyValue ;
    schema1:name "Inter-Pass Data Dependency" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/interPassDataDependency> ;
    schema1:value "N/A — a single acquisition pass" .


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
  "schema:description": "laQicpmsTAPP instance derived from Liu et al. 2024 (JAAS 39) Extraterrestrial samples (Li-borate flux glass) Spot analysis fs-LA-Q-ICP-MS Chinese Academy of Sciences (publication column of LA-Q-ICP-MS_TAPP_v96.csv).",
  "ada:targetMaterialTemplate": {
    "ada:targetMaterialDeclaration": "Li-borate flux fusion glass (extraterrestrial sample preparation)",
    "ada:targetMaterialColumns": [
      {
        "schema:valueName": "targetMaterial",
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
        "@id": "ada:targetMaterialColumn/laQicpmsTAPP/primaryCalibrationStandardName",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "primaryCalibrationStandardName",
        "schema:name": "Primary Calibration Standard Name",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ],
    "ada:defaultTargetMaterials": []
  },
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
        "schema:description": "Li2B4O7 flux (350.0 ± 0.3 mg) and powdered sample (10.00 ± 0.03 mg) weighed into a small Pt–Au crucible, mixed with a glass rod, NH4Br solution added as a releasing agent, and fused into a mini glass disk on an M4 automatic fluxer; the disk measured for major elements by WD-XRF, then its surface cleaned with ethanol before fs-LA-ICP-MS (§2.3)",
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
            "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "pulseAnalogDetectorNonlinearityCorrectionDefault",
            "schema:name": "Pulse Analog Detector Nonlinearity Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "N — Table 1 gives 'Detector mode: Dual'; a cross-calibration is not described"
          }
        ],
        "ada:detectionLimitMethod": "all: Pettke (2012) — §3.2",
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
  "ada:samplingUnitSelectionCriteriaDefault": "Coverage — \"Nine spot analyses ... were arranged in a grid pattern to cover the entire glass\" (p.5), the grid being the test of whether the fused disc is homogeneous",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "preAnalysisImagingAndScreeningDefault",
      "schema:name": "Pre-Analysis Imaging and Screening",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N — the fused glass discs are prepared for XRF and then ablated directly; no imaging or screening step is described before the LA-ICP-MS spots, whose grid is laid out to cover the whole disc (p.5)"
    },
    {
      "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSizeDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "transectRateMappingRateOrStepSizeDefault",
      "schema:name": "Transect Rate Mapping Rate or Step Size",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N/A — spot mode"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/interPassDataDependency",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/interPassDataDependency"
        }
      ],
      "schema:name": "Inter-Pass Data Dependency",
      "schema:value": "N/A — a single acquisition pass"
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "N — ICP-MS type not stated; Agilent 8900 model named but \"quadrupole\" or \"ICP-MS/MS\" not used in paper",
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
          "@id": "ada:parameter/module/SingleCollector/detectorConfiguration",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "detectorConfiguration",
          "schema:name": "Detector Configuration",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:value": "Dual — Table 1 'Detector mode: Dual'"
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
          "schema:defaultValue": "Gas flows optimised by spot ablation of NIST SRM 612 'to obtain maximum signal intensities while maintaining ThO/Th at <0.3% and U/Th at 0.95–1.05' (§2.2); sampling depth 8 mm (Table 1)"
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
          "schema:defaultValue": "25 s washout between analyses — §2.2"
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
              "schema:description": "15 L/min — Table 1 'Plasma gas flow'"
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
              "schema:defaultValue": 0.85,
              "schema:description": "0.85 L/min — Table 1 'Auxiliary gas flow'"
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
      "schema:name": "example instrumentName",
      "schema:manufacturer": {
        "schema:name": "missing",
        "@type": [
          "schema:Organization"
        ]
      }
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
          "schema:value": "N — 'femtosecond'; the laser's details are in Table S1, not in the archived PDF"
        }
      ],
      "schema:model": {
        "schema:name": "Shanghai Chemlab GenesisGEO (high-repetition-rate fs laser, 343 nm)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "343 nm fs (GenesisGEO high-repetition-rate femtosecond laser)",
      "ada:laserSpotGeometryDefault": "all: 100 µm — '100 µm-diameter ablating spots' (§2.2); Table 1 gives 'Ablation spot size 100 × 100 µm'",
      "ada:laserFluenceDefault": "6.79 J cm⁻²",
      "ada:laserRepetitionRateDefault": "all: 1 Hz",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/Laser-Ablation-System",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:carrierGasFlowRateDefault": "He: chamber gas 0.7 L/min; cup gas 0.1 L/min — Table 1",
  "ada:analysisSequenceDefault": "Per spot: 25 s gas blank, 45 s ablation, 25 s washout between analyses (§2.2); the order of standards and unknowns is not described",
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Sc",
      "V",
      "Cr",
      "Co",
      "Ni",
      "Cu",
      "Zn",
      "Ga",
      "Rb",
      "Sr",
      "Y",
      "Zr",
      "Nb",
      "Ba",
      "La",
      "Ce",
      "Pr",
      "Nd",
      "Sm",
      "Eu",
      "Gd",
      "Tb",
      "Dy",
      "Ho",
      "Er",
      "Tm",
      "Yb",
      "Lu",
      "Hf",
      "Ta",
      "Th",
      "U"
    ],
    "ada:targetSpeciesColumns": [
      {
        "schema:valueName": "targetSpecies",
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
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:backgroundCountTimeDefault": "25 s gas blank before each ablation",
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
      "schema:name": "N — the CAS Strategy Priority Research Program and NSFC grant support the study as a whole and are recorded under Funding Source for Analysis"
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
  "ada:samplingUnitType": "Aliquot (fused Li-borate glass disc) > Spot — \"Nine spot analyses ... were arranged in a grid pattern to cover the entire glass\" (p.5), and compositions are reported as the mean of those spots, \"fs-LA-ICP-MS (n = 9 spots)\" (Table 2, p.8)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Iolite 4 (Paton et al. 2011)"
    }
  ],
  "ada:reportedProperties": [
    "Sc, V, Cr, Co, Ni, Cu, Zn, Ga, Rb, Sr, Y, Zr, Nb, Ba, La, Ce, Pr, Nd, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu, Hf, Ta, Th, U — concentrations reported as 'Mean' with a '95% CI' per sample (Table 2), which gives no unit; the LODs are in µg g⁻¹ (§3.2). Relative standard deviations are the precision measure (§3.5)"
  ],
  "ada:ablationSamplingMode": [
    "all: Single spot — Table 1 'Ablation mode'"
  ],
  "ada:ablationSpotDurationDefault": "45 s ablation (after 25 s gas blank; 25 s washout between analyses)",
  "ada:rasterLineSpacingDefault": "N/A — spot mode",
  "ada:internalStandardApproach": "all: two internal standard elements, chosen per target element — Si for Co, Ni, Cu and Zn, and Al for the others, after comparing Si, Ca and Al on GSR-3 (§3.3); the disks were 'initially measured for major elements by WD-XRF' (§2.3)",
  "ada:elementalFractionationCorrection": [
    "N — the paper states that fs lasers 'are considered stoichiometric erosion processes without any element or isotope fractionation effects' (§3.4); no correction is described"
  ],
  "ada:oxideProductionMethodAndThreshold": "ThO⁺/Th⁺ (mass 248/232) <0.3%; U/Th monitored at 0.95–1.05",
  "ada:blankBackgroundCorrectionMethod": "25 s gas blank before each ablation; flux procedure-blank contributions deducted for V, Co, Zn, Ba, La, Ce, Ta and U — 'after measuring a gas blank for 25 s' (§2.2); 'All results of the eight pollution elements above have deducted the flux blank contributions' (§3.2)",
  "ada:internalStandardElement": "all: Si (for Co, Ni, Cu, Zn), Al (for the other trace elements) — §3.3",
  "ada:secondaryReferenceMaterialDefault": [
    "AC-E, GSR-1, JB-1b, GSR-3, AGV-2, W-2A — six silicate rock GRMs prepared as lithium borate glasses and 'analyzed to evaluate the performance of the proposed method' (§2.1); reference values from GeoReM (§3.5). The meteorites NWA13190 and NWA14526 are samples, compared with solution ICP-MS"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:sampleIntroduction": "missing",
  "ada:signalCollectionMode": "missing",
  "ada:signalIntegrationIntervalMethod": "missing",
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
  "schema:description": "laQicpmsTAPP instance derived from Liu et al. 2024 (JAAS 39) Extraterrestrial samples (Li-borate flux glass) Spot analysis fs-LA-Q-ICP-MS Chinese Academy of Sciences (publication column of LA-Q-ICP-MS_TAPP_v96.csv).",
  "ada:targetMaterialTemplate": {
    "ada:targetMaterialDeclaration": "Li-borate flux fusion glass (extraterrestrial sample preparation)",
    "ada:targetMaterialColumns": [
      {
        "schema:valueName": "targetMaterial",
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
        "@id": "ada:targetMaterialColumn/laQicpmsTAPP/primaryCalibrationStandardName",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "primaryCalibrationStandardName",
        "schema:name": "Primary Calibration Standard Name",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ],
    "ada:defaultTargetMaterials": []
  },
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
        "schema:description": "Li2B4O7 flux (350.0 \u00b1 0.3 mg) and powdered sample (10.00 \u00b1 0.03 mg) weighed into a small Pt\u2013Au crucible, mixed with a glass rod, NH4Br solution added as a releasing agent, and fused into a mini glass disk on an M4 automatic fluxer; the disk measured for major elements by WD-XRF, then its surface cleaned with ethanol before fs-LA-ICP-MS (\u00a72.3)",
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
            "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "pulseAnalogDetectorNonlinearityCorrectionDefault",
            "schema:name": "Pulse Analog Detector Nonlinearity Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "N \u2014 Table 1 gives 'Detector mode: Dual'; a cross-calibration is not described"
          }
        ],
        "ada:detectionLimitMethod": "all: Pettke (2012) \u2014 \u00a73.2",
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
  "ada:samplingUnitSelectionCriteriaDefault": "Coverage \u2014 \"Nine spot analyses ... were arranged in a grid pattern to cover the entire glass\" (p.5), the grid being the test of whether the fused disc is homogeneous",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "preAnalysisImagingAndScreeningDefault",
      "schema:name": "Pre-Analysis Imaging and Screening",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N \u2014 the fused glass discs are prepared for XRF and then ablated directly; no imaging or screening step is described before the LA-ICP-MS spots, whose grid is laid out to cover the whole disc (p.5)"
    },
    {
      "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSizeDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "transectRateMappingRateOrStepSizeDefault",
      "schema:name": "Transect Rate Mapping Rate or Step Size",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N/A \u2014 spot mode"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/interPassDataDependency",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/interPassDataDependency"
        }
      ],
      "schema:name": "Inter-Pass Data Dependency",
      "schema:value": "N/A \u2014 a single acquisition pass"
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "N \u2014 ICP-MS type not stated; Agilent 8900 model named but \"quadrupole\" or \"ICP-MS/MS\" not used in paper",
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
          "@id": "ada:parameter/module/SingleCollector/detectorConfiguration",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "detectorConfiguration",
          "schema:name": "Detector Configuration",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:value": "Dual \u2014 Table 1 'Detector mode: Dual'"
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
          "schema:defaultValue": "Gas flows optimised by spot ablation of NIST SRM 612 'to obtain maximum signal intensities while maintaining ThO/Th at <0.3% and U/Th at 0.95\u20131.05' (\u00a72.2); sampling depth 8 mm (Table 1)"
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
          "schema:defaultValue": "25 s washout between analyses \u2014 \u00a72.2"
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
              "schema:description": "15 L/min \u2014 Table 1 'Plasma gas flow'"
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
              "schema:defaultValue": 0.85,
              "schema:description": "0.85 L/min \u2014 Table 1 'Auxiliary gas flow'"
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
      "schema:name": "example instrumentName",
      "schema:manufacturer": {
        "schema:name": "missing",
        "@type": [
          "schema:Organization"
        ]
      }
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
          "schema:value": "N \u2014 'femtosecond'; the laser's details are in Table S1, not in the archived PDF"
        }
      ],
      "schema:model": {
        "schema:name": "Shanghai Chemlab GenesisGEO (high-repetition-rate fs laser, 343 nm)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "343 nm fs (GenesisGEO high-repetition-rate femtosecond laser)",
      "ada:laserSpotGeometryDefault": "all: 100 \u00b5m \u2014 '100 \u00b5m-diameter ablating spots' (\u00a72.2); Table 1 gives 'Ablation spot size 100 \u00d7 100 \u00b5m'",
      "ada:laserFluenceDefault": "6.79 J cm\u207b\u00b2",
      "ada:laserRepetitionRateDefault": "all: 1 Hz",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/Laser-Ablation-System",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:carrierGasFlowRateDefault": "He: chamber gas 0.7 L/min; cup gas 0.1 L/min \u2014 Table 1",
  "ada:analysisSequenceDefault": "Per spot: 25 s gas blank, 45 s ablation, 25 s washout between analyses (\u00a72.2); the order of standards and unknowns is not described",
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Sc",
      "V",
      "Cr",
      "Co",
      "Ni",
      "Cu",
      "Zn",
      "Ga",
      "Rb",
      "Sr",
      "Y",
      "Zr",
      "Nb",
      "Ba",
      "La",
      "Ce",
      "Pr",
      "Nd",
      "Sm",
      "Eu",
      "Gd",
      "Tb",
      "Dy",
      "Ho",
      "Er",
      "Tm",
      "Yb",
      "Lu",
      "Hf",
      "Ta",
      "Th",
      "U"
    ],
    "ada:targetSpeciesColumns": [
      {
        "schema:valueName": "targetSpecies",
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
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:backgroundCountTimeDefault": "25 s gas blank before each ablation",
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
      "schema:name": "N \u2014 the CAS Strategy Priority Research Program and NSFC grant support the study as a whole and are recorded under Funding Source for Analysis"
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
  "ada:samplingUnitType": "Aliquot (fused Li-borate glass disc) > Spot \u2014 \"Nine spot analyses ... were arranged in a grid pattern to cover the entire glass\" (p.5), and compositions are reported as the mean of those spots, \"fs-LA-ICP-MS (n = 9 spots)\" (Table 2, p.8)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Iolite 4 (Paton et al. 2011)"
    }
  ],
  "ada:reportedProperties": [
    "Sc, V, Cr, Co, Ni, Cu, Zn, Ga, Rb, Sr, Y, Zr, Nb, Ba, La, Ce, Pr, Nd, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu, Hf, Ta, Th, U \u2014 concentrations reported as 'Mean' with a '95% CI' per sample (Table 2), which gives no unit; the LODs are in \u00b5g g\u207b\u00b9 (\u00a73.2). Relative standard deviations are the precision measure (\u00a73.5)"
  ],
  "ada:ablationSamplingMode": [
    "all: Single spot \u2014 Table 1 'Ablation mode'"
  ],
  "ada:ablationSpotDurationDefault": "45 s ablation (after 25 s gas blank; 25 s washout between analyses)",
  "ada:rasterLineSpacingDefault": "N/A \u2014 spot mode",
  "ada:internalStandardApproach": "all: two internal standard elements, chosen per target element \u2014 Si for Co, Ni, Cu and Zn, and Al for the others, after comparing Si, Ca and Al on GSR-3 (\u00a73.3); the disks were 'initially measured for major elements by WD-XRF' (\u00a72.3)",
  "ada:elementalFractionationCorrection": [
    "N \u2014 the paper states that fs lasers 'are considered stoichiometric erosion processes without any element or isotope fractionation effects' (\u00a73.4); no correction is described"
  ],
  "ada:oxideProductionMethodAndThreshold": "ThO\u207a/Th\u207a (mass 248/232) <0.3%; U/Th monitored at 0.95\u20131.05",
  "ada:blankBackgroundCorrectionMethod": "25 s gas blank before each ablation; flux procedure-blank contributions deducted for V, Co, Zn, Ba, La, Ce, Ta and U \u2014 'after measuring a gas blank for 25 s' (\u00a72.2); 'All results of the eight pollution elements above have deducted the flux blank contributions' (\u00a73.2)",
  "ada:internalStandardElement": "all: Si (for Co, Ni, Cu, Zn), Al (for the other trace elements) \u2014 \u00a73.3",
  "ada:secondaryReferenceMaterialDefault": [
    "AC-E, GSR-1, JB-1b, GSR-3, AGV-2, W-2A \u2014 six silicate rock GRMs prepared as lithium borate glasses and 'analyzed to evaluate the performance of the proposed method' (\u00a72.1); reference values from GeoReM (\u00a73.5). The meteorites NWA13190 and NWA14526 are samples, compared with solution ICP-MS"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:sampleIntroduction": "missing",
  "ada:signalCollectionMode": "missing",
  "ada:signalIntegrationIntervalMethod": "missing",
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
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:laQicpmsTAPP-Liu2024> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/LaserAblation/fusionFluxAndDilutionRatioDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/LaserAblation/preAblationSurfaceTreatmentDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Li2B4O7 flux (350.0 ± 0.3 mg) and powdered sample (10.00 ± 0.03 mg) weighed into a small Pt–Au crucible, mixed with a glass rod, NH4Br solution added as a releasing agent, and fused into a mini glass disk on an M4 automatic fluxer; the disk measured for major elements by WD-XRF, then its surface cleaned with ethanol before fs-LA-ICP-MS (§2.3)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrectionDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ;
                    ada:detectionLimitMethod "all: Pettke (2012) — §3.2" ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "missing" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/interPassDataDependency>,
        <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSizeDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Liu, Xue, Li, Wang et al." ] ;
    schema1:datePublished "missing" ;
    schema1:description "laQicpmsTAPP instance derived from Liu et al. 2024 (JAAS 39) Extraterrestrial samples (Li-borate flux glass) Spot analysis fs-LA-Q-ICP-MS Chinese Academy of Sciences (publication column of LA-Q-ICP-MS_TAPP_v96.csv)." ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "N — the CAS Strategy Priority Research Program and NSFC grant support the study as a whole and are recorded under Funding Source for Analysis" ] ;
    schema1:instrument <ex:instrument/ICPMS>,
        <ex:instrument/Laser-Ablation-System> ;
    schema1:location [ a schema1:Place ;
            schema1:name "State Key Laboratory of Lithospheric Evolution and Environmental Coevolution, IGGCAS, Beijing, China" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "fs-LA-Q-ICP-MS" ] ;
    schema1:name "Liu et al. (2024) Extraterrestrial Flux Glass fs-LA-ICP-MS Spot v1" ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Liu et al. (2024) JAAS 39, 2728; Pettke et al. (2012) for LOD" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:ablationPitDepthRateDefault "missing" ;
    ada:ablationSamplingMode "all: Single spot — Table 1 'Ablation mode'" ;
    ada:ablationSpotDurationDefault "45 s ablation (after 25 s gas blank; 25 s washout between analyses)" ;
    ada:analysisSequenceDefault "Per spot: 25 s gas blank, 45 s ablation, 25 s washout between analyses (§2.2); the order of standards and unknowns is not described" ;
    ada:backgroundCountTimeDefault "25 s gas blank before each ablation" ;
    ada:blankBackgroundCorrectionMethod "25 s gas blank before each ablation; flux procedure-blank contributions deducted for V, Co, Zn, Ba, La, Ce, Ta and U — 'after measuring a gas blank for 25 s' (§2.2); 'All results of the eight pollution elements above have deducted the flux blank contributions' (§3.2)" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:carrierGasFlowRateDefault "He: chamber gas 0.7 L/min; cup gas 0.1 L/min — Table 1" ;
    ada:constantsAndReferenceValuesUsedDefault "missing" ;
    ada:elementalFractionationCorrection "N — the paper states that fs lasers 'are considered stoichiometric erosion processes without any element or isotope fractionation effects' (§3.4); no correction is described" ;
    ada:internalStandardApproach "all: two internal standard elements, chosen per target element — Si for Co, Ni, Cu and Zn, and Al for the others, after comparing Si, Ca and Al on GSR-3 (§3.3); the disks were 'initially measured for major elements by WD-XRF' (§2.3)" ;
    ada:internalStandardElement "all: Si (for Co, Ni, Cu, Zn), Al (for the other trace elements) — §3.3" ;
    ada:massBiasCorrectionStrategy "missing" ;
    ada:numberOfAcquisitionPasses -9999 ;
    ada:oxideProductionMethodAndThreshold "ThO⁺/Th⁺ (mass 248/232) <0.3%; U/Th monitored at 0.95–1.05" ;
    ada:rasterLineSpacingDefault "N/A — spot mode" ;
    ada:reportedProperties "Sc, V, Cr, Co, Ni, Cu, Zn, Ga, Rb, Sr, Y, Zr, Nb, Ba, La, Ce, Pr, Nd, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu, Hf, Ta, Th, U — concentrations reported as 'Mean' with a '95% CI' per sample (Table 2), which gives no unit; the LODs are in µg g⁻¹ (§3.2). Relative standard deviations are the precision measure (§3.5)" ;
    ada:sampleIntroduction "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "Coverage — \"Nine spot analyses ... were arranged in a grid pattern to cover the entire glass\" (p.5), the grid being the test of whether the fused disc is homogeneous" ;
    ada:samplingUnitType "Aliquot (fused Li-borate glass disc) > Spot — \"Nine spot analyses ... were arranged in a grid pattern to cover the entire glass\" (p.5), and compositions are reported as the mean of those spots, \"fs-LA-ICP-MS (n = 9 spots)\" (Table 2, p.8)" ;
    ada:secondaryReferenceMaterialDefault "AC-E, GSR-1, JB-1b, GSR-3, AGV-2, W-2A — six silicate rock GRMs prepared as lithium borate glasses and 'analyzed to evaluate the performance of the proposed method' (§2.1); reference values from GeoReM (§3.5). The meteorites NWA13190 and NWA14526 are samples, compared with solution ICP-MS" ;
    ada:signalCollectionMode "missing" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:targetMaterialTemplate [ ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/laQicpmsTAPP/primaryCalibrationStandardName> ;
            ada:targetMaterialDeclaration "Li-borate flux fusion glass (extraterrestrial sample preparation)" ] ;
    ada:targetSpeciesTemplate [ ada:defaultTargetSpecies "Ba",
                "Ce",
                "Co",
                "Cr",
                "Cu",
                "Dy",
                "Er",
                "Eu",
                "Ga",
                "Gd",
                "Hf",
                "Ho",
                "La",
                "Lu",
                "Nb",
                "Nd",
                "Ni",
                "Pr",
                "Rb",
                "Sc",
                "Sm",
                "Sr",
                "Ta",
                "Tb",
                "Th",
                "Tm",
                "U",
                "V",
                "Y",
                "Yb",
                "Zn",
                "Zr" ;
            ada:targetSpeciesColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetSpecies" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/calibrationStrategyPerTargetSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/monitoredMasses>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/spectralInterferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ] ;
    ada:totalIntegrationTimePerOutputDataPointDefault -9999 ;
    ada:uncertaintyLevel "missing" ;
    bios:computationalTool [ schema1:name "Iolite 4 (Paton et al. 2011)" ;
            ada:toolRole "dataReduction" ] .

<ex:instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuningDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigationDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SingleCollector/detectorConfiguration> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "N — ICP-MS type not stated; Agilent 8900 model named but \"quadrupole\" or \"ICP-MS/MS\" not used in paper" ;
    schema1:hasPart <ex:instrument/ICPMS/part/Collision-Reaction-Cell>,
        <ex:instrument/ICPMS/part/ICP-Source>,
        <ex:instrument/ICPMS/part/Interface-Cone>,
        <ex:instrument/ICPMS/part/Torch> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "missing" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Agilent 8900 (Q-ICP-MS; ICP-MS/MS capable)" ] ;
    schema1:name "example instrumentName" .

<ex:instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "missing" .

<ex:instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPowerDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<ex:instrument/ICPMS/part/Interface-Cone> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Interface Cone" ;
    schema1:name "missing" .

<ex:instrument/ICPMS/part/Torch> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Torch" ;
    schema1:name "missing" .

<ex:instrument/Laser-Ablation-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/LaserAblation/laserPulseDuration> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Laser Ablation System" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Shanghai Chemlab GenesisGEO (high-repetition-rate fs laser, 343 nm)" ] ;
    schema1:name "example instrumentName" ;
    ada:laserFluenceDefault "6.79 J cm⁻²" ;
    ada:laserRepetitionRateDefault "all: 1 Hz" ;
    ada:laserSpotGeometryDefault "all: 100 µm — '100 µm-diameter ablating spots' (§2.2); Table 1 gives 'Ablation spot size 100 × 100 µm'" ;
    ada:laserType "343 nm fs (GenesisGEO high-repetition-rate femtosecond laser)" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 8.5e-01 ;
    schema1:description "0.85 L/min — Table 1 'Auxiliary gas flow'" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:valueName "auxiliaryGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 15 ;
    schema1:description "15 L/min — Table 1 'Plasma gas flow'" ;
    schema1:name "Coolant Plasma Gas Flow Rate" ;
    schema1:valueName "coolantPlasmaGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Gas flows optimised by spot ablation of NIST SRM 612 'to obtain maximum signal intensities while maintaining ThO/Th at <0.3% and U/Th at 0.95–1.05' (§2.2); sampling depth 8 mm (Table 1)" ;
    schema1:name "ICP Tuning" ;
    schema1:valueName "icpTuningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "25 s washout between analyses — §2.2" ;
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
    schema1:value "N — 'femtosecond'; the laser's details are in Table S1, not in the archived PDF" ;
    schema1:valueName "laserPulseDuration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/preAblationSurfaceTreatmentDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Surface cleaning with ethanol before analysis" ;
    schema1:name "Pre Ablation Surface Treatment" ;
    schema1:valueName "preAblationSurfaceTreatmentDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSizeDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N/A — spot mode" ;
    schema1:name "Transect Rate Mapping Rate or Step Size" ;
    schema1:valueName "transectRateMappingRateOrStepSizeDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N — the fused glass discs are prepared for XRF and then ablated directly; no imaging or screening step is described before the LA-ICP-MS spots, whose grid is laid out to cover the whole disc (p.5)" ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:valueName "preAnalysisImagingAndScreeningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SingleCollector/detectorConfiguration> a schema1:PropertyValueSpecification ;
    schema1:name "Detector Configuration" ;
    schema1:value "Dual — Table 1 'Detector mode: Dual'" ;
    schema1:valueName "detectorConfiguration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrectionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N — Table 1 gives 'Detector mode: Dual'; a cross-calibration is not described" ;
    schema1:name "Pulse Analog Detector Nonlinearity Correction" ;
    schema1:valueName "pulseAnalogDetectorNonlinearityCorrectionDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/targetMaterialColumn/laQicpmsTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/calibrationStrategyPerTargetSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Calibration Strategy per Target Species" ;
    schema1:valueName "calibrationStrategyPerTargetSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Internal (Within-Measurement) Analytical Precision and Assessment Method" ;
    schema1:valueName "internalAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/monitoredMasses> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Monitored Masses" ;
    schema1:valueName "monitoredMasses" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/spectralInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Spectral Interference Corrections Applied" ;
    schema1:valueName "spectralInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/interPassDataDependency> a schema1:PropertyValue ;
    schema1:name "Inter-Pass Data Dependency" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/interPassDataDependency> ;
    schema1:value "N/A — a single acquisition pass" .


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
  "schema:description": "Run products of 1.0 GPa piston-cylinder experiments, analysed at two laboratories whose data 'exhibited good agreement, any differences being below 10 %' (§2.2.2)",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "quench product"
    ],
    "ada:targetMaterialColumns": [
      {
        "schema:valueName": "targetMaterial",
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
        "@id": "ada:targetMaterialColumn/laQicpmsTAPP/primaryCalibrationStandardName",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "primaryCalibrationStandardName",
        "schema:name": "Primary Calibration Standard Name",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:samplingUnitSelectionCriteriaDefault": "N — the paper states the beam diameter used for glasses (\"40 μm beam diameter for glasses\", p.4) but no rule for choosing where in a run product to ablate",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "preAnalysisImagingAndScreeningDefault",
      "schema:name": "Pre-Analysis Imaging and Screening",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Optical microscopy, then EMP — \"Following examination by optical microscopy to ascertain the integrity of the experiments and the state of the oxygen buffers, the solid components of the run products were analysed for major elements, S and Cu, using a JEOL JXA-8230 electron microprobe (EMP)\" (p.2); those EMP values are then the internal standards for the LA data, \"with Si and Fe obtained from EMP analyses as the internal standards\" (p.4)"
    },
    {
      "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSizeDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "transectRateMappingRateOrStepSizeDefault",
      "schema:name": "Transect Rate Mapping Rate or Step Size",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N/A — spot mode"
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
      "schema:description": "N2 or Ar mixed into the He carrier; amounts not stated — §2.2.2"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/interPassDataDependency",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/interPassDataDependency"
        }
      ],
      "schema:name": "Inter-Pass Data Dependency",
      "schema:value": "N/A — a single acquisition pass"
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "N — ICP-MS type not stated; Agilent 7900 model named but \"quadrupole\" not explicitly stated",
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
      "schema:name": "example instrumentName",
      "schema:manufacturer": {
        "schema:name": "missing",
        "@type": [
          "schema:Organization"
        ]
      }
    },
    {
      "schema:additionalType": [
        "Laser Ablation System",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Resonetic 193 nm ArF excimer laser; CetacAnalyte HE system — §2.2.2",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "193 nm ArF excimer — §2.2.2",
      "schema:name": "N — the paper names the 'CetacAnalyte HE system', not its cell",
      "ada:laserSpotGeometryDefault": "all: 40 µm beam diameter — 'a 40 μm beam diameter for glasses' (§2.2.2)",
      "ada:laserFluenceDefault": "~2.5 J cm⁻² (stated as \"energy of ~2.5 J/cm²\")",
      "ada:laserRepetitionRateDefault": "all: 7 Hz — 'operated at 7 Hz ablation frequency' (§2.2.2)",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/Laser-Ablation-System"
    }
  ],
  "ada:carrierGasFlowRateDefault": "He; flow not stated — 'Helium served as the carrier gas, to which nitrogen or argon gas was mixed for sensitivity optimization' (§2.2.2)",
  "ada:analysisSequenceDefault": "N — NIST 610 is the external standard and NIST 612 and BCR-2G the monitoring standards (§2.2.2); the sequence is not described",
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Au",
      "Cu"
    ],
    "ada:targetSpeciesColumns": [
      {
        "schema:valueName": "targetSpecies",
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
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Recovered capsules longitudinally sectioned with a wire saw, and one half mounted in epoxy resin (§2.1)",
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
            "@id": "ada:parameter/module/ICPMS/filteringApproachDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "filteringApproachDefault",
            "schema:name": "Filtering Approach",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Au micronugget spikes identified in the time-resolved signal and removed, or the analysis not considered — 'only analyses free from micronuggets or where the spikes from the micronuggets could be easily removed were considered (Fig. 1)' (§2.2.2)"
          }
        ],
        "ada:detectionLimitMethod": "N — stated as \"detection limits\" without specific formula",
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
    "schema:name": "Guangzhou Institute of Geochemistry, CAS; Hefei University of Technology — LA-ICP-MS 'was employed at both the Guangzhou Institute of Geochemistry and Hefei University of Technology' (§2.2.2)"
  },
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "N — the CAS Strategic Priority Research Program and NSFC grants support the study as a whole and are recorded under Funding Source for Analysis"
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
  "ada:samplingUnitType": "Phase (quenched silicate glass of one experimental run) > Spot — \"A Resonetic 193 nm ArF excimer laser with a 40 μm beam diameter for glasses\" (p.4); Au and Cu contents are reported per run (Table 1, p.3)",
  "ada:reportedProperties": [
    "Au (ppm); Cu (ppm) — Au and Cu contents of the quenched silicate melt, per run (Table 1, p.3); S and H2O come from other methods, and the derived quantity reported is the sulfide/melt partition coefficient DAu (dimensionless, p.2)"
  ],
  "ada:ablationSamplingMode": [
    "N — ablation mode not explicitly stated; \"beam diameter\" terminology used but \"spot\" or \"spot mode\" not written"
  ],
  "ada:rasterLineSpacingDefault": "N/A — spot mode",
  "ada:internalStandardApproach": "all: an element measured by EMP — 'with Si and Fe obtained from EMP analyses as the internal standards' (§2.2.2); which element serves the glass and which the sulfide is not stated",
  "ada:internalStandardElement": "all: Si, Fe — 'Si and Fe obtained from EMP analyses as the internal standards' (§2.2.2); the assignment to glass or sulfide is not stated",
  "ada:secondaryReferenceMaterialDefault": [
    "NIST 612; BCR-2G — 'NIST 612 and BCR-2G as monitoring standards' (§2.2.2)"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ablationSpotDurationDefault": -9999,
  "ada:backgroundCountTimeDefault": -9999,
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:signalCollectionMode": "missing",
  "ada:signalIntegrationIntervalMethod": "missing",
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
  "schema:description": "Run products of 1.0 GPa piston-cylinder experiments, analysed at two laboratories whose data 'exhibited good agreement, any differences being below 10 %' (\u00a72.2.2)",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "quench product"
    ],
    "ada:targetMaterialColumns": [
      {
        "schema:valueName": "targetMaterial",
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
        "@id": "ada:targetMaterialColumn/laQicpmsTAPP/primaryCalibrationStandardName",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "primaryCalibrationStandardName",
        "schema:name": "Primary Calibration Standard Name",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:samplingUnitSelectionCriteriaDefault": "N \u2014 the paper states the beam diameter used for glasses (\"40 \u03bcm beam diameter for glasses\", p.4) but no rule for choosing where in a run product to ablate",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "preAnalysisImagingAndScreeningDefault",
      "schema:name": "Pre-Analysis Imaging and Screening",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Optical microscopy, then EMP \u2014 \"Following examination by optical microscopy to ascertain the integrity of the experiments and the state of the oxygen buffers, the solid components of the run products were analysed for major elements, S and Cu, using a JEOL JXA-8230 electron microprobe (EMP)\" (p.2); those EMP values are then the internal standards for the LA data, \"with Si and Fe obtained from EMP analyses as the internal standards\" (p.4)"
    },
    {
      "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSizeDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "transectRateMappingRateOrStepSizeDefault",
      "schema:name": "Transect Rate Mapping Rate or Step Size",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N/A \u2014 spot mode"
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
      "schema:description": "N2 or Ar mixed into the He carrier; amounts not stated \u2014 \u00a72.2.2"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/interPassDataDependency",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/interPassDataDependency"
        }
      ],
      "schema:name": "Inter-Pass Data Dependency",
      "schema:value": "N/A \u2014 a single acquisition pass"
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "N \u2014 ICP-MS type not stated; Agilent 7900 model named but \"quadrupole\" not explicitly stated",
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
      "schema:name": "example instrumentName",
      "schema:manufacturer": {
        "schema:name": "missing",
        "@type": [
          "schema:Organization"
        ]
      }
    },
    {
      "schema:additionalType": [
        "Laser Ablation System",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Resonetic 193 nm ArF excimer laser; CetacAnalyte HE system \u2014 \u00a72.2.2",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "193 nm ArF excimer \u2014 \u00a72.2.2",
      "schema:name": "N \u2014 the paper names the 'CetacAnalyte HE system', not its cell",
      "ada:laserSpotGeometryDefault": "all: 40 \u00b5m beam diameter \u2014 'a 40 \u03bcm beam diameter for glasses' (\u00a72.2.2)",
      "ada:laserFluenceDefault": "~2.5 J cm\u207b\u00b2 (stated as \"energy of ~2.5 J/cm\u00b2\")",
      "ada:laserRepetitionRateDefault": "all: 7 Hz \u2014 'operated at 7 Hz ablation frequency' (\u00a72.2.2)",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/Laser-Ablation-System"
    }
  ],
  "ada:carrierGasFlowRateDefault": "He; flow not stated \u2014 'Helium served as the carrier gas, to which nitrogen or argon gas was mixed for sensitivity optimization' (\u00a72.2.2)",
  "ada:analysisSequenceDefault": "N \u2014 NIST 610 is the external standard and NIST 612 and BCR-2G the monitoring standards (\u00a72.2.2); the sequence is not described",
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Au",
      "Cu"
    ],
    "ada:targetSpeciesColumns": [
      {
        "schema:valueName": "targetSpecies",
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
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Recovered capsules longitudinally sectioned with a wire saw, and one half mounted in epoxy resin (\u00a72.1)",
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
            "@id": "ada:parameter/module/ICPMS/filteringApproachDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "filteringApproachDefault",
            "schema:name": "Filtering Approach",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Au micronugget spikes identified in the time-resolved signal and removed, or the analysis not considered \u2014 'only analyses free from micronuggets or where the spikes from the micronuggets could be easily removed were considered (Fig. 1)' (\u00a72.2.2)"
          }
        ],
        "ada:detectionLimitMethod": "N \u2014 stated as \"detection limits\" without specific formula",
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
    "schema:name": "Guangzhou Institute of Geochemistry, CAS; Hefei University of Technology \u2014 LA-ICP-MS 'was employed at both the Guangzhou Institute of Geochemistry and Hefei University of Technology' (\u00a72.2.2)"
  },
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "N \u2014 the CAS Strategic Priority Research Program and NSFC grants support the study as a whole and are recorded under Funding Source for Analysis"
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
  "ada:samplingUnitType": "Phase (quenched silicate glass of one experimental run) > Spot \u2014 \"A Resonetic 193 nm ArF excimer laser with a 40 \u03bcm beam diameter for glasses\" (p.4); Au and Cu contents are reported per run (Table 1, p.3)",
  "ada:reportedProperties": [
    "Au (ppm); Cu (ppm) \u2014 Au and Cu contents of the quenched silicate melt, per run (Table 1, p.3); S and H2O come from other methods, and the derived quantity reported is the sulfide/melt partition coefficient DAu (dimensionless, p.2)"
  ],
  "ada:ablationSamplingMode": [
    "N \u2014 ablation mode not explicitly stated; \"beam diameter\" terminology used but \"spot\" or \"spot mode\" not written"
  ],
  "ada:rasterLineSpacingDefault": "N/A \u2014 spot mode",
  "ada:internalStandardApproach": "all: an element measured by EMP \u2014 'with Si and Fe obtained from EMP analyses as the internal standards' (\u00a72.2.2); which element serves the glass and which the sulfide is not stated",
  "ada:internalStandardElement": "all: Si, Fe \u2014 'Si and Fe obtained from EMP analyses as the internal standards' (\u00a72.2.2); the assignment to glass or sulfide is not stated",
  "ada:secondaryReferenceMaterialDefault": [
    "NIST 612; BCR-2G \u2014 'NIST 612 and BCR-2G as monitoring standards' (\u00a72.2.2)"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ablationSpotDurationDefault": -9999,
  "ada:backgroundCountTimeDefault": -9999,
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:signalCollectionMode": "missing",
  "ada:signalIntegrationIntervalMethod": "missing",
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
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:laQicpmsTAPP-Liu2025> a cdi:Activity,
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
                    schema1:description "Recovered capsules longitudinally sectioned with a wire saw, and one half mounted in epoxy resin (§2.1)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproachDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ;
                    ada:detectionLimitMethod "N — stated as \"detection limits\" without specific formula" ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/interPassDataDependency>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSizeDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Liu, Li, Xu, Xiong et al." ] ;
    schema1:datePublished "missing" ;
    schema1:description "Run products of 1.0 GPa piston-cylinder experiments, analysed at two laboratories whose data 'exhibited good agreement, any differences being below 10 %' (§2.2.2)" ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "N — the CAS Strategic Priority Research Program and NSFC grants support the study as a whole and are recorded under Funding Source for Analysis" ] ;
    schema1:instrument <ex:instrument/ICPMS>,
        <ex:instrument/Laser-Ablation-System> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Guangzhou Institute of Geochemistry, CAS; Hefei University of Technology — LA-ICP-MS 'was employed at both the Guangzhou Institute of Geochemistry and Hefei University of Technology' (§2.2.2)" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "LA-Q-ICP-MS" ] ;
    schema1:name "Liu et al. (2025) Experimental Silicate Glass LA-ICP-MS Spot v1" ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Liu et al. (2025) GCA 393, 170; Xu et al. (2022) for experimental protocol" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:ablationPitDepthRateDefault "missing" ;
    ada:ablationSamplingMode "N — ablation mode not explicitly stated; \"beam diameter\" terminology used but \"spot\" or \"spot mode\" not written" ;
    ada:ablationSpotDurationDefault -9999 ;
    ada:analysisSequenceDefault "N — NIST 610 is the external standard and NIST 612 and BCR-2G the monitoring standards (§2.2.2); the sequence is not described" ;
    ada:backgroundCountTimeDefault -9999 ;
    ada:blankBackgroundCorrectionMethod "missing" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:carrierGasFlowRateDefault "He; flow not stated — 'Helium served as the carrier gas, to which nitrogen or argon gas was mixed for sensitivity optimization' (§2.2.2)" ;
    ada:constantsAndReferenceValuesUsedDefault "missing" ;
    ada:internalStandardApproach "all: an element measured by EMP — 'with Si and Fe obtained from EMP analyses as the internal standards' (§2.2.2); which element serves the glass and which the sulfide is not stated" ;
    ada:internalStandardElement "all: Si, Fe — 'Si and Fe obtained from EMP analyses as the internal standards' (§2.2.2); the assignment to glass or sulfide is not stated" ;
    ada:massBiasCorrectionStrategy "missing" ;
    ada:numberOfAcquisitionPasses -9999 ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:rasterLineSpacingDefault "N/A — spot mode" ;
    ada:reportedProperties "Au (ppm); Cu (ppm) — Au and Cu contents of the quenched silicate melt, per run (Table 1, p.3); S and H2O come from other methods, and the derived quantity reported is the sulfide/melt partition coefficient DAu (dimensionless, p.2)" ;
    ada:sampleIntroduction "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "N — the paper states the beam diameter used for glasses (\"40 μm beam diameter for glasses\", p.4) but no rule for choosing where in a run product to ablate" ;
    ada:samplingUnitType "Phase (quenched silicate glass of one experimental run) > Spot — \"A Resonetic 193 nm ArF excimer laser with a 40 μm beam diameter for glasses\" (p.4); Au and Cu contents are reported per run (Table 1, p.3)" ;
    ada:secondaryReferenceMaterialDefault "NIST 612; BCR-2G — 'NIST 612 and BCR-2G as monitoring standards' (§2.2.2)" ;
    ada:signalCollectionMode "missing" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "quench product" ;
            ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/laQicpmsTAPP/primaryCalibrationStandardName> ] ;
    ada:targetSpeciesTemplate [ ada:defaultTargetSpecies "Au",
                "Cu" ;
            ada:targetSpeciesColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetSpecies" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/calibrationStrategyPerTargetSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/monitoredMasses>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/spectralInterferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ] ;
    ada:totalIntegrationTimePerOutputDataPointDefault -9999 ;
    ada:uncertaintyLevel "missing" .

<ex:instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "N — ICP-MS type not stated; Agilent 7900 model named but \"quadrupole\" not explicitly stated" ;
    schema1:hasPart <ex:instrument/ICPMS/part/Collision-Reaction-Cell>,
        <ex:instrument/ICPMS/part/ICP-Source>,
        <ex:instrument/ICPMS/part/Interface-Cone>,
        <ex:instrument/ICPMS/part/Torch> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "missing" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Agilent 7900 (Q-ICP-MS)" ] ;
    schema1:name "example instrumentName" .

<ex:instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "missing" .

<ex:instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<ex:instrument/ICPMS/part/Interface-Cone> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Interface Cone" ;
    schema1:name "missing" .

<ex:instrument/ICPMS/part/Torch> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Torch" ;
    schema1:name "missing" .

<ex:instrument/Laser-Ablation-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Laser Ablation System" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Resonetic 193 nm ArF excimer laser; CetacAnalyte HE system — §2.2.2" ] ;
    schema1:name "N — the paper names the 'CetacAnalyte HE system', not its cell" ;
    ada:laserFluenceDefault "~2.5 J cm⁻² (stated as \"energy of ~2.5 J/cm²\")" ;
    ada:laserRepetitionRateDefault "all: 7 Hz — 'operated at 7 Hz ablation frequency' (§2.2.2)" ;
    ada:laserSpotGeometryDefault "all: 40 µm beam diameter — 'a 40 μm beam diameter for glasses' (§2.2.2)" ;
    ada:laserType "193 nm ArF excimer — §2.2.2" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproachDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Au micronugget spikes identified in the time-resolved signal and removed, or the analysis not considered — 'only analyses free from micronuggets or where the spikes from the micronuggets could be easily removed were considered (Fig. 1)' (§2.2.2)" ;
    schema1:name "Filtering Approach" ;
    schema1:valueName "filteringApproachDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 2 ;
    schema1:description "N2 or Ar mixed into the He carrier; amounts not stated — §2.2.2" ;
    schema1:name "Make-up Gas and Flow Rate" ;
    schema1:valueName "makeUpGasAndFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSizeDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N/A — spot mode" ;
    schema1:name "Transect Rate Mapping Rate or Step Size" ;
    schema1:valueName "transectRateMappingRateOrStepSizeDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Optical microscopy, then EMP — \"Following examination by optical microscopy to ascertain the integrity of the experiments and the state of the oxygen buffers, the solid components of the run products were analysed for major elements, S and Cu, using a JEOL JXA-8230 electron microprobe (EMP)\" (p.2); those EMP values are then the internal standards for the LA data, \"with Si and Fe obtained from EMP analyses as the internal standards\" (p.4)" ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:valueName "preAnalysisImagingAndScreeningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/targetMaterialColumn/laQicpmsTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/calibrationStrategyPerTargetSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Calibration Strategy per Target Species" ;
    schema1:valueName "calibrationStrategyPerTargetSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Internal (Within-Measurement) Analytical Precision and Assessment Method" ;
    schema1:valueName "internalAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/monitoredMasses> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Monitored Masses" ;
    schema1:valueName "monitoredMasses" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/spectralInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Spectral Interference Corrections Applied" ;
    schema1:valueName "spectralInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/interPassDataDependency> a schema1:PropertyValue ;
    schema1:name "Inter-Pass Data Dependency" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/interPassDataDependency> ;
    schema1:value "N/A — a single acquisition pass" .


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
  "schema:description": "Run products of 1.0 GPa piston-cylinder experiments, analysed at two laboratories whose data 'exhibited good agreement, any differences being below 10 %' (§2.2.2)",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "experimental sulfide"
    ],
    "ada:targetMaterialColumns": [
      {
        "schema:valueName": "targetMaterial",
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
        "@id": "ada:targetMaterialColumn/laQicpmsTAPP/primaryCalibrationStandardName",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "primaryCalibrationStandardName",
        "schema:name": "Primary Calibration Standard Name",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:samplingUnitSelectionCriteriaDefault": "Sulfide grains larger than 20 µm, wider than the beam — '20 μm for sulfides, selecting grain sizes larger than 20 µm for the latter' (§2.2.2)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "preAnalysisImagingAndScreeningDefault",
      "schema:name": "Pre-Analysis Imaging and Screening",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Optical microscopy, then EMP — \"Following examination by optical microscopy to ascertain the integrity of the experiments and the state of the oxygen buffers, the solid components of the run products were analysed for major elements, S and Cu, using a JEOL JXA-8230 electron microprobe (EMP)\" (p.2); those EMP values are then the internal standards for the LA data, \"with Si and Fe obtained from EMP analyses as the internal standards\" (p.4)"
    },
    {
      "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSizeDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "transectRateMappingRateOrStepSizeDefault",
      "schema:name": "Transect Rate Mapping Rate or Step Size",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N/A — spot mode"
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
      "schema:description": "N2 or Ar mixed into the He carrier; amounts not stated — §2.2.2"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/interPassDataDependency",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/interPassDataDependency"
        }
      ],
      "schema:name": "Inter-Pass Data Dependency",
      "schema:value": "N/A — a single acquisition pass"
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "N — ICP-MS type not stated",
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
      "schema:name": "example instrumentName",
      "schema:manufacturer": {
        "schema:name": "missing",
        "@type": [
          "schema:Organization"
        ]
      }
    },
    {
      "schema:additionalType": [
        "Laser Ablation System",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Resonetic 193 nm ArF excimer laser; CetacAnalyte HE system — §2.2.2",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "193 nm ArF excimer — §2.2.2",
      "schema:name": "N — the paper names the 'CetacAnalyte HE system', not its cell",
      "ada:laserSpotGeometryDefault": "all: 20 µm beam diameter — '20 μm for sulfides, selecting grain sizes larger than 20 µm for the latter' (§2.2.2)",
      "ada:laserFluenceDefault": "~2.5 J cm⁻²",
      "ada:laserRepetitionRateDefault": "all: 7 Hz — 'operated at 7 Hz ablation frequency' (§2.2.2)",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/Laser-Ablation-System"
    }
  ],
  "ada:carrierGasFlowRateDefault": "He; flow not stated — 'Helium served as the carrier gas, to which nitrogen or argon gas was mixed for sensitivity optimization' (§2.2.2)",
  "ada:analysisSequenceDefault": "N — NIST 610 is the external standard and NIST 612 and BCR-2G the monitoring standards (§2.2.2); the sequence is not described",
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Au",
      "Cu"
    ],
    "ada:targetSpeciesColumns": [
      {
        "schema:valueName": "targetSpecies",
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
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Recovered capsules longitudinally sectioned with a wire saw, and one half mounted in epoxy resin (§2.1)",
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
            "@id": "ada:parameter/module/ICPMS/filteringApproachDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "filteringApproachDefault",
            "schema:name": "Filtering Approach",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Au micronugget spikes identified in the time-resolved signal and removed, or the analysis not considered — 'only analyses free from micronuggets or where the spikes from the micronuggets could be easily removed were considered (Fig. 1)' (§2.2.2)"
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
    "schema:name": "Guangzhou Institute of Geochemistry, CAS; Hefei University of Technology — LA-ICP-MS 'was employed at both the Guangzhou Institute of Geochemistry and Hefei University of Technology' (§2.2.2)"
  },
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "N — the CAS Strategic Priority Research Program and NSFC grants support the study as a whole and are recorded under Funding Source for Analysis"
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
  "ada:samplingUnitType": "Phase (quenched sulfide of one experimental run) > Spot — \"20 μm for sulfides, selecting grain sizes larger than 20 µm for the latter\" (p.4); Au and Cu contents are reported per run (Table 1, p.3)",
  "ada:reportedProperties": [
    "Au (ppm); Cu (ppm) — Au and Cu contents of the quenched sulfide per run (Table 1, p.3), which with the coexisting glass give the sulfide/melt partition coefficient DAu (dimensionless, p.2)"
  ],
  "ada:ablationSamplingMode": [
    "N — ablation mode not explicitly stated"
  ],
  "ada:rasterLineSpacingDefault": "N/A — spot mode",
  "ada:internalStandardApproach": "all: an element measured by EMP — 'with Si and Fe obtained from EMP analyses as the internal standards' (§2.2.2); which element serves the glass and which the sulfide is not stated",
  "ada:internalStandardElement": "all: Si, Fe — 'Si and Fe obtained from EMP analyses as the internal standards' (§2.2.2); the assignment to glass or sulfide is not stated",
  "ada:secondaryReferenceMaterialDefault": [
    "NIST 612; BCR-2G — 'NIST 612 and BCR-2G as monitoring standards' (§2.2.2)"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ablationSpotDurationDefault": -9999,
  "ada:backgroundCountTimeDefault": -9999,
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:signalCollectionMode": "missing",
  "ada:signalIntegrationIntervalMethod": "missing",
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
  "schema:description": "Run products of 1.0 GPa piston-cylinder experiments, analysed at two laboratories whose data 'exhibited good agreement, any differences being below 10 %' (\u00a72.2.2)",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "experimental sulfide"
    ],
    "ada:targetMaterialColumns": [
      {
        "schema:valueName": "targetMaterial",
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
        "@id": "ada:targetMaterialColumn/laQicpmsTAPP/primaryCalibrationStandardName",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "primaryCalibrationStandardName",
        "schema:name": "Primary Calibration Standard Name",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
  "ada:samplingUnitSelectionCriteriaDefault": "Sulfide grains larger than 20 \u00b5m, wider than the beam \u2014 '20 \u03bcm for sulfides, selecting grain sizes larger than 20 \u00b5m for the latter' (\u00a72.2.2)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "preAnalysisImagingAndScreeningDefault",
      "schema:name": "Pre-Analysis Imaging and Screening",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Optical microscopy, then EMP \u2014 \"Following examination by optical microscopy to ascertain the integrity of the experiments and the state of the oxygen buffers, the solid components of the run products were analysed for major elements, S and Cu, using a JEOL JXA-8230 electron microprobe (EMP)\" (p.2); those EMP values are then the internal standards for the LA data, \"with Si and Fe obtained from EMP analyses as the internal standards\" (p.4)"
    },
    {
      "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSizeDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "transectRateMappingRateOrStepSizeDefault",
      "schema:name": "Transect Rate Mapping Rate or Step Size",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N/A \u2014 spot mode"
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
      "schema:description": "N2 or Ar mixed into the He carrier; amounts not stated \u2014 \u00a72.2.2"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/interPassDataDependency",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/interPassDataDependency"
        }
      ],
      "schema:name": "Inter-Pass Data Dependency",
      "schema:value": "N/A \u2014 a single acquisition pass"
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "N \u2014 ICP-MS type not stated",
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
      "schema:name": "example instrumentName",
      "schema:manufacturer": {
        "schema:name": "missing",
        "@type": [
          "schema:Organization"
        ]
      }
    },
    {
      "schema:additionalType": [
        "Laser Ablation System",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Resonetic 193 nm ArF excimer laser; CetacAnalyte HE system \u2014 \u00a72.2.2",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "193 nm ArF excimer \u2014 \u00a72.2.2",
      "schema:name": "N \u2014 the paper names the 'CetacAnalyte HE system', not its cell",
      "ada:laserSpotGeometryDefault": "all: 20 \u00b5m beam diameter \u2014 '20 \u03bcm for sulfides, selecting grain sizes larger than 20 \u00b5m for the latter' (\u00a72.2.2)",
      "ada:laserFluenceDefault": "~2.5 J cm\u207b\u00b2",
      "ada:laserRepetitionRateDefault": "all: 7 Hz \u2014 'operated at 7 Hz ablation frequency' (\u00a72.2.2)",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/Laser-Ablation-System"
    }
  ],
  "ada:carrierGasFlowRateDefault": "He; flow not stated \u2014 'Helium served as the carrier gas, to which nitrogen or argon gas was mixed for sensitivity optimization' (\u00a72.2.2)",
  "ada:analysisSequenceDefault": "N \u2014 NIST 610 is the external standard and NIST 612 and BCR-2G the monitoring standards (\u00a72.2.2); the sequence is not described",
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Au",
      "Cu"
    ],
    "ada:targetSpeciesColumns": [
      {
        "schema:valueName": "targetSpecies",
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
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Recovered capsules longitudinally sectioned with a wire saw, and one half mounted in epoxy resin (\u00a72.1)",
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
            "@id": "ada:parameter/module/ICPMS/filteringApproachDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "filteringApproachDefault",
            "schema:name": "Filtering Approach",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Au micronugget spikes identified in the time-resolved signal and removed, or the analysis not considered \u2014 'only analyses free from micronuggets or where the spikes from the micronuggets could be easily removed were considered (Fig. 1)' (\u00a72.2.2)"
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
    "schema:name": "Guangzhou Institute of Geochemistry, CAS; Hefei University of Technology \u2014 LA-ICP-MS 'was employed at both the Guangzhou Institute of Geochemistry and Hefei University of Technology' (\u00a72.2.2)"
  },
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "N \u2014 the CAS Strategic Priority Research Program and NSFC grants support the study as a whole and are recorded under Funding Source for Analysis"
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
  "ada:samplingUnitType": "Phase (quenched sulfide of one experimental run) > Spot \u2014 \"20 \u03bcm for sulfides, selecting grain sizes larger than 20 \u00b5m for the latter\" (p.4); Au and Cu contents are reported per run (Table 1, p.3)",
  "ada:reportedProperties": [
    "Au (ppm); Cu (ppm) \u2014 Au and Cu contents of the quenched sulfide per run (Table 1, p.3), which with the coexisting glass give the sulfide/melt partition coefficient DAu (dimensionless, p.2)"
  ],
  "ada:ablationSamplingMode": [
    "N \u2014 ablation mode not explicitly stated"
  ],
  "ada:rasterLineSpacingDefault": "N/A \u2014 spot mode",
  "ada:internalStandardApproach": "all: an element measured by EMP \u2014 'with Si and Fe obtained from EMP analyses as the internal standards' (\u00a72.2.2); which element serves the glass and which the sulfide is not stated",
  "ada:internalStandardElement": "all: Si, Fe \u2014 'Si and Fe obtained from EMP analyses as the internal standards' (\u00a72.2.2); the assignment to glass or sulfide is not stated",
  "ada:secondaryReferenceMaterialDefault": [
    "NIST 612; BCR-2G \u2014 'NIST 612 and BCR-2G as monitoring standards' (\u00a72.2.2)"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ablationSpotDurationDefault": -9999,
  "ada:backgroundCountTimeDefault": -9999,
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:signalCollectionMode": "missing",
  "ada:signalIntegrationIntervalMethod": "missing",
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
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:laQicpmsTAPP-Liu2025-2> a cdi:Activity,
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
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Recovered capsules longitudinally sectioned with a wire saw, and one half mounted in epoxy resin (§2.1)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/interPassDataDependency>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSizeDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Liu, Li, Xu, Xiong et al." ] ;
    schema1:datePublished "missing" ;
    schema1:description "Run products of 1.0 GPa piston-cylinder experiments, analysed at two laboratories whose data 'exhibited good agreement, any differences being below 10 %' (§2.2.2)" ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "N — the CAS Strategic Priority Research Program and NSFC grants support the study as a whole and are recorded under Funding Source for Analysis" ] ;
    schema1:instrument <ex:instrument/ICPMS>,
        <ex:instrument/Laser-Ablation-System> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Guangzhou Institute of Geochemistry, CAS; Hefei University of Technology — LA-ICP-MS 'was employed at both the Guangzhou Institute of Geochemistry and Hefei University of Technology' (§2.2.2)" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "LA-Q-ICP-MS" ] ;
    schema1:name "Liu et al. (2025) Experimental Sulfide LA-ICP-MS Spot v1" ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Liu et al. (2025) GCA 393, 170; Xu et al. (2022)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:ablationPitDepthRateDefault "missing" ;
    ada:ablationSamplingMode "N — ablation mode not explicitly stated" ;
    ada:ablationSpotDurationDefault -9999 ;
    ada:analysisSequenceDefault "N — NIST 610 is the external standard and NIST 612 and BCR-2G the monitoring standards (§2.2.2); the sequence is not described" ;
    ada:backgroundCountTimeDefault -9999 ;
    ada:blankBackgroundCorrectionMethod "missing" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:carrierGasFlowRateDefault "He; flow not stated — 'Helium served as the carrier gas, to which nitrogen or argon gas was mixed for sensitivity optimization' (§2.2.2)" ;
    ada:constantsAndReferenceValuesUsedDefault "missing" ;
    ada:internalStandardApproach "all: an element measured by EMP — 'with Si and Fe obtained from EMP analyses as the internal standards' (§2.2.2); which element serves the glass and which the sulfide is not stated" ;
    ada:internalStandardElement "all: Si, Fe — 'Si and Fe obtained from EMP analyses as the internal standards' (§2.2.2); the assignment to glass or sulfide is not stated" ;
    ada:massBiasCorrectionStrategy "missing" ;
    ada:numberOfAcquisitionPasses -9999 ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:rasterLineSpacingDefault "N/A — spot mode" ;
    ada:reportedProperties "Au (ppm); Cu (ppm) — Au and Cu contents of the quenched sulfide per run (Table 1, p.3), which with the coexisting glass give the sulfide/melt partition coefficient DAu (dimensionless, p.2)" ;
    ada:sampleIntroduction "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "Sulfide grains larger than 20 µm, wider than the beam — '20 μm for sulfides, selecting grain sizes larger than 20 µm for the latter' (§2.2.2)" ;
    ada:samplingUnitType "Phase (quenched sulfide of one experimental run) > Spot — \"20 μm for sulfides, selecting grain sizes larger than 20 µm for the latter\" (p.4); Au and Cu contents are reported per run (Table 1, p.3)" ;
    ada:secondaryReferenceMaterialDefault "NIST 612; BCR-2G — 'NIST 612 and BCR-2G as monitoring standards' (§2.2.2)" ;
    ada:signalCollectionMode "missing" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "experimental sulfide" ;
            ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/laQicpmsTAPP/primaryCalibrationStandardName> ] ;
    ada:targetSpeciesTemplate [ ada:defaultTargetSpecies "Au",
                "Cu" ;
            ada:targetSpeciesColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetSpecies" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/calibrationStrategyPerTargetSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/monitoredMasses>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/spectralInterferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ] ;
    ada:totalIntegrationTimePerOutputDataPointDefault -9999 ;
    ada:uncertaintyLevel "missing" .

<ex:instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "N — ICP-MS type not stated" ;
    schema1:hasPart <ex:instrument/ICPMS/part/Collision-Reaction-Cell>,
        <ex:instrument/ICPMS/part/ICP-Source>,
        <ex:instrument/ICPMS/part/Interface-Cone>,
        <ex:instrument/ICPMS/part/Torch> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "missing" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Agilent 7900 (Q-ICP-MS)" ] ;
    schema1:name "example instrumentName" .

<ex:instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "missing" .

<ex:instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<ex:instrument/ICPMS/part/Interface-Cone> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Interface Cone" ;
    schema1:name "missing" .

<ex:instrument/ICPMS/part/Torch> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Torch" ;
    schema1:name "missing" .

<ex:instrument/Laser-Ablation-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Laser Ablation System" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Resonetic 193 nm ArF excimer laser; CetacAnalyte HE system — §2.2.2" ] ;
    schema1:name "N — the paper names the 'CetacAnalyte HE system', not its cell" ;
    ada:laserFluenceDefault "~2.5 J cm⁻²" ;
    ada:laserRepetitionRateDefault "all: 7 Hz — 'operated at 7 Hz ablation frequency' (§2.2.2)" ;
    ada:laserSpotGeometryDefault "all: 20 µm beam diameter — '20 μm for sulfides, selecting grain sizes larger than 20 µm for the latter' (§2.2.2)" ;
    ada:laserType "193 nm ArF excimer — §2.2.2" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproachDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Au micronugget spikes identified in the time-resolved signal and removed, or the analysis not considered — 'only analyses free from micronuggets or where the spikes from the micronuggets could be easily removed were considered (Fig. 1)' (§2.2.2)" ;
    schema1:name "Filtering Approach" ;
    schema1:valueName "filteringApproachDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 2 ;
    schema1:description "N2 or Ar mixed into the He carrier; amounts not stated — §2.2.2" ;
    schema1:name "Make-up Gas and Flow Rate" ;
    schema1:valueName "makeUpGasAndFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSizeDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N/A — spot mode" ;
    schema1:name "Transect Rate Mapping Rate or Step Size" ;
    schema1:valueName "transectRateMappingRateOrStepSizeDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Optical microscopy, then EMP — \"Following examination by optical microscopy to ascertain the integrity of the experiments and the state of the oxygen buffers, the solid components of the run products were analysed for major elements, S and Cu, using a JEOL JXA-8230 electron microprobe (EMP)\" (p.2); those EMP values are then the internal standards for the LA data, \"with Si and Fe obtained from EMP analyses as the internal standards\" (p.4)" ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:valueName "preAnalysisImagingAndScreeningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/targetMaterialColumn/laQicpmsTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/calibrationStrategyPerTargetSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Calibration Strategy per Target Species" ;
    schema1:valueName "calibrationStrategyPerTargetSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Internal (Within-Measurement) Analytical Precision and Assessment Method" ;
    schema1:valueName "internalAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/monitoredMasses> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Monitored Masses" ;
    schema1:valueName "monitoredMasses" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/spectralInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Spectral Interference Corrections Applied" ;
    schema1:valueName "spectralInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/interPassDataDependency> a schema1:PropertyValue ;
    schema1:name "Inter-Pass Data Dependency" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/interPassDataDependency> ;
    schema1:value "N/A — a single acquisition pass" .


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
  "schema:description": "The procedure broadly follows Udry et al. (2012) and Pernet-Fisher et al. (2014). Two internal-standard approaches: oxide-total normalization for silicates and oxides, EMP CaO for phosphate. A 90 µm beam on some olivines tested whether low REE signals reflect insufficient sampling (Methods, p.4)",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "silicates",
      "oxides",
      "glass"
    ],
    "ada:targetMaterialColumns": [
      {
        "schema:valueName": "targetMaterial",
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
        "@id": "ada:targetMaterialColumn/laQicpmsTAPP/primaryCalibrationStandardName",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "primaryCalibrationStandardName",
        "schema:name": "Primary Calibration Standard Name",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
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
            "schema:defaultValue": "N/A — in situ"
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
            "schema:defaultValue": "N — not stated"
          }
        ],
        "schema:description": "N — sections UT1 to UT3 (p.3); their preparation is not described",
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
            "@id": "ada:parameter/module/LaserAblation/signalSmoothingDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "signalSmoothingDefault",
            "schema:name": "Signal Smoothing",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "N — not stated"
          }
        ],
        "ada:detectionLimitMethod": "all: 3σ of the background counts — Table 3 note d: 'LOD is the limit of detection estimated based on background counts to 3σ confidence interval'",
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
  "ada:samplingUnitSelectionCriteriaDefault": "N — spots are screened after the fact, not before: \"The time-lapse plots of each spot were examined, and only the plateau region was used to quantify the trace element abundances\" (p.4). That is a rejection rule (see `Analysis Inclusion and Rejection Criteria`), not a rule for choosing units",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "preAnalysisImagingAndScreeningDefault",
      "schema:name": "Pre-Analysis Imaging and Screening",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Petrographic microscopy, SEM and EMP — \"The petrography of these sections was examined using a petrographic microscope and a scanning electron microscope\", followed by BSE images and element maps (p.3); the EMP results then serve as internal standards for the ablation data, which are normalised using \"EMP CaO or MgO values\" for silicates and \"40Ca counts to CaO concentrations from the EMP analysis\" for phosphate (p.4)"
    },
    {
      "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSizeDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "transectRateMappingRateOrStepSizeDefault",
      "schema:name": "Transect Rate Mapping Rate or Step Size",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N/A — spot analysis"
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
      "schema:defaultValue": "N — not stated"
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
      "schema:value": "N — not stated"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/interPassDataDependency",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/interPassDataDependency"
        }
      ],
      "schema:name": "Inter-Pass Data Dependency",
      "schema:value": "N/A — a single acquisition pass"
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
              "schema:defaultValue": "N — not stated"
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
              "schema:defaultValue": "N — not stated"
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
          "schema:defaultValue": "N — not stated"
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
          "schema:defaultValue": "N — not stated"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/ICPMS",
      "schema:name": "example instrumentName",
      "schema:manufacturer": {
        "schema:name": "missing",
        "@type": [
          "schema:Organization"
        ]
      }
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
          "schema:description": "150 mJ output energy — Methods, p.4"
        }
      ],
      "schema:model": {
        "schema:name": "GeoLasPro 193 nm Excimer laser-ablation system — Methods, p.4",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "193 nm Excimer (ArF excimer)",
      "ada:laserSpotGeometryDefault": "all: 24 and 32 µm diameter, and 90 µm for a few olivine analyses — '24 and 32 µm diameter were commonly used for silicates and glass, and a few analyses were conducted on olivines using a 90 µm beam to evaluate whether the low signals of REEs are a result of insufficient sampling' (Methods, p.4)",
      "ada:laserFluenceDefault": "7–10 J/m² — as written: 'a fluence rate of 7–10 J/m2 on the sample' (Methods, p.4)",
      "ada:laserRepetitionRateDefault": "all: 5 Hz",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/Laser-Ablation-System",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:carrierGasFlowRateDefault": "N — not stated",
  "ada:analysisSequenceDefault": "N — 'A NIST 610 glass standard was analyzed before and after every session' (Methods, p.4); the order within a session is not described",
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Li",
      "Be",
      "K",
      "Sc",
      "Ti",
      "V",
      "Cr",
      "Mn",
      "Co",
      "Ni",
      "Cu",
      "Zn",
      "Ga",
      "Ge",
      "Rb",
      "Sr",
      "Y",
      "Zr",
      "Nb",
      "Ba",
      "La",
      "Ce",
      "Pr",
      "Nd",
      "Sm",
      "Eu",
      "Gd",
      "Tb",
      "Dy",
      "Ho",
      "Er",
      "Tm",
      "Yb",
      "Lu",
      "Hf",
      "Ta",
      "W",
      "Au",
      "Pb",
      "Th",
      "U"
    ],
    "ada:targetSpeciesColumns": [
      {
        "schema:valueName": "targetSpecies",
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
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:backgroundCountTimeDefault": "50 s — 'The background was counted for 50 sec before each LA-ICP-MS analysis' (Methods, p.4)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-ICP-MS — 'an Agilent 7500ce inductively coupled plasma–mass spectrometer (ICP-MS), coupled with a GeoLasPro 193 nm Excimer laser-ablation (LA) system' (Methods, p.4)"
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
        "schema:name": "Udry et al. (2012); Pernet-Fisher et al. (2014) — 'The analytical procedure is broadly similar to that of Udry et al. (2012) and Pernet-Fisher et al. (2014)' (Methods, p.4)"
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
        "schema:description": "EMP gives major element compositions; for spots with EMP data, oxide-total normalization 'generally agrees within <10% with the method using EMP CaO or MgO values as internal standards' — Methods, p.4"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Phase > Spot — \"The time-lapse plots of each spot were examined, and only the plateau region was used to quantify the trace element abundances\" (p.4); abundances are reported as per-phase means (\"n = 7\", \"n = 13\", table p.9), the individual spots being in a supplement not in the archived PDF",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "AMS ver. 1.0 (Mutchler et al. 2008; Analysis Management System, stand-alone software)"
    }
  ],
  "ada:reportedProperties": [
    "Li, Be, K, Sc, Ti, V, Cr, Mn, Co, Ni, Cu, Zn, Ga, Ge, Rb, Sr, Y, Zr, Nb, Ba, La, Ce, Pr, Nd, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu, Hf, Ta, W, Au, Pb, Th, U (ppm) — trace element abundances in ppm, glass averages with 1σ and n in Table 3; mineral data in Table S1, not in the archived PDF"
  ],
  "ada:ablationSamplingMode": [
    "all: Spot — 'The time-lapse plots of each spot were examined' (Methods, p.4)"
  ],
  "ada:ablationSpotDurationDefault": "N — not stated",
  "ada:rasterLineSpacingDefault": "N/A — spot analysis",
  "ada:internalStandardApproach": "all: normalization to 100 wt% oxide total — 'For silicates and oxides, trace element abundances were calculated by normalization to 100 wt% oxide total' (Methods, p.4)",
  "ada:calibrationMeasurementFrequency": "Before and after every session — 'A NIST 610 glass standard was analyzed before and after every session' (Methods, p.4)",
  "ada:oxideProductionMethodAndThreshold": "N — not stated",
  "ada:blankBackgroundCorrectionMethod": "N — the background 'was counted for 50 sec before each LA-ICP-MS analysis' (Methods, p.4); how it was subtracted is not described",
  "ada:internalStandardElement": "all: none — oxide-total normalization (Methods, p.4)",
  "ada:signalIntegrationIntervalMethod": "Plateau region of each spot's time-lapse plot — 'The time-lapse plots of each spot were examined, and only the plateau region was used to quantify the trace element abundances' (Methods, p.4)",
  "ada:secondaryReferenceMaterialDefault": [
    "N — not stated"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:sampleIntroduction": "missing",
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
  "schema:description": "The procedure broadly follows Udry et al. (2012) and Pernet-Fisher et al. (2014). Two internal-standard approaches: oxide-total normalization for silicates and oxides, EMP CaO for phosphate. A 90 \u00b5m beam on some olivines tested whether low REE signals reflect insufficient sampling (Methods, p.4)",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "silicates",
      "oxides",
      "glass"
    ],
    "ada:targetMaterialColumns": [
      {
        "schema:valueName": "targetMaterial",
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
        "@id": "ada:targetMaterialColumn/laQicpmsTAPP/primaryCalibrationStandardName",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "primaryCalibrationStandardName",
        "schema:name": "Primary Calibration Standard Name",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
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
            "schema:defaultValue": "N/A \u2014 in situ"
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
            "schema:defaultValue": "N \u2014 not stated"
          }
        ],
        "schema:description": "N \u2014 sections UT1 to UT3 (p.3); their preparation is not described",
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
            "@id": "ada:parameter/module/LaserAblation/signalSmoothingDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "signalSmoothingDefault",
            "schema:name": "Signal Smoothing",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "N \u2014 not stated"
          }
        ],
        "ada:detectionLimitMethod": "all: 3\u03c3 of the background counts \u2014 Table 3 note d: 'LOD is the limit of detection estimated based on background counts to 3\u03c3 confidence interval'",
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
  "ada:samplingUnitSelectionCriteriaDefault": "N \u2014 spots are screened after the fact, not before: \"The time-lapse plots of each spot were examined, and only the plateau region was used to quantify the trace element abundances\" (p.4). That is a rejection rule (see `Analysis Inclusion and Rejection Criteria`), not a rule for choosing units",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "preAnalysisImagingAndScreeningDefault",
      "schema:name": "Pre-Analysis Imaging and Screening",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Petrographic microscopy, SEM and EMP \u2014 \"The petrography of these sections was examined using a petrographic microscope and a scanning electron microscope\", followed by BSE images and element maps (p.3); the EMP results then serve as internal standards for the ablation data, which are normalised using \"EMP CaO or MgO values\" for silicates and \"40Ca counts to CaO concentrations from the EMP analysis\" for phosphate (p.4)"
    },
    {
      "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSizeDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "transectRateMappingRateOrStepSizeDefault",
      "schema:name": "Transect Rate Mapping Rate or Step Size",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N/A \u2014 spot analysis"
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
      "schema:defaultValue": "N \u2014 not stated"
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
      "schema:value": "N \u2014 not stated"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/interPassDataDependency",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/interPassDataDependency"
        }
      ],
      "schema:name": "Inter-Pass Data Dependency",
      "schema:value": "N/A \u2014 a single acquisition pass"
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
              "schema:defaultValue": "N \u2014 not stated"
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
              "schema:defaultValue": "N \u2014 not stated"
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
          "schema:defaultValue": "N \u2014 not stated"
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
          "schema:defaultValue": "N \u2014 not stated"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/ICPMS",
      "schema:name": "example instrumentName",
      "schema:manufacturer": {
        "schema:name": "missing",
        "@type": [
          "schema:Organization"
        ]
      }
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
          "schema:description": "150 mJ output energy \u2014 Methods, p.4"
        }
      ],
      "schema:model": {
        "schema:name": "GeoLasPro 193 nm Excimer laser-ablation system \u2014 Methods, p.4",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "193 nm Excimer (ArF excimer)",
      "ada:laserSpotGeometryDefault": "all: 24 and 32 \u00b5m diameter, and 90 \u00b5m for a few olivine analyses \u2014 '24 and 32 \u00b5m diameter were commonly used for silicates and glass, and a few analyses were conducted on olivines using a 90 \u00b5m beam to evaluate whether the low signals of REEs are a result of insufficient sampling' (Methods, p.4)",
      "ada:laserFluenceDefault": "7\u201310 J/m\u00b2 \u2014 as written: 'a fluence rate of 7\u201310 J/m2 on the sample' (Methods, p.4)",
      "ada:laserRepetitionRateDefault": "all: 5 Hz",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/Laser-Ablation-System",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:carrierGasFlowRateDefault": "N \u2014 not stated",
  "ada:analysisSequenceDefault": "N \u2014 'A NIST 610 glass standard was analyzed before and after every session' (Methods, p.4); the order within a session is not described",
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Li",
      "Be",
      "K",
      "Sc",
      "Ti",
      "V",
      "Cr",
      "Mn",
      "Co",
      "Ni",
      "Cu",
      "Zn",
      "Ga",
      "Ge",
      "Rb",
      "Sr",
      "Y",
      "Zr",
      "Nb",
      "Ba",
      "La",
      "Ce",
      "Pr",
      "Nd",
      "Sm",
      "Eu",
      "Gd",
      "Tb",
      "Dy",
      "Ho",
      "Er",
      "Tm",
      "Yb",
      "Lu",
      "Hf",
      "Ta",
      "W",
      "Au",
      "Pb",
      "Th",
      "U"
    ],
    "ada:targetSpeciesColumns": [
      {
        "schema:valueName": "targetSpecies",
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
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:backgroundCountTimeDefault": "50 s \u2014 'The background was counted for 50 sec before each LA-ICP-MS analysis' (Methods, p.4)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-ICP-MS \u2014 'an Agilent 7500ce inductively coupled plasma\u2013mass spectrometer (ICP-MS), coupled with a GeoLasPro 193 nm Excimer laser-ablation (LA) system' (Methods, p.4)"
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
        "schema:name": "Udry et al. (2012); Pernet-Fisher et al. (2014) \u2014 'The analytical procedure is broadly similar to that of Udry et al. (2012) and Pernet-Fisher et al. (2014)' (Methods, p.4)"
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
        "schema:description": "EMP gives major element compositions; for spots with EMP data, oxide-total normalization 'generally agrees within <10% with the method using EMP CaO or MgO values as internal standards' \u2014 Methods, p.4"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Phase > Spot \u2014 \"The time-lapse plots of each spot were examined, and only the plateau region was used to quantify the trace element abundances\" (p.4); abundances are reported as per-phase means (\"n = 7\", \"n = 13\", table p.9), the individual spots being in a supplement not in the archived PDF",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "AMS ver. 1.0 (Mutchler et al. 2008; Analysis Management System, stand-alone software)"
    }
  ],
  "ada:reportedProperties": [
    "Li, Be, K, Sc, Ti, V, Cr, Mn, Co, Ni, Cu, Zn, Ga, Ge, Rb, Sr, Y, Zr, Nb, Ba, La, Ce, Pr, Nd, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu, Hf, Ta, W, Au, Pb, Th, U (ppm) \u2014 trace element abundances in ppm, glass averages with 1\u03c3 and n in Table 3; mineral data in Table S1, not in the archived PDF"
  ],
  "ada:ablationSamplingMode": [
    "all: Spot \u2014 'The time-lapse plots of each spot were examined' (Methods, p.4)"
  ],
  "ada:ablationSpotDurationDefault": "N \u2014 not stated",
  "ada:rasterLineSpacingDefault": "N/A \u2014 spot analysis",
  "ada:internalStandardApproach": "all: normalization to 100 wt% oxide total \u2014 'For silicates and oxides, trace element abundances were calculated by normalization to 100 wt% oxide total' (Methods, p.4)",
  "ada:calibrationMeasurementFrequency": "Before and after every session \u2014 'A NIST 610 glass standard was analyzed before and after every session' (Methods, p.4)",
  "ada:oxideProductionMethodAndThreshold": "N \u2014 not stated",
  "ada:blankBackgroundCorrectionMethod": "N \u2014 the background 'was counted for 50 sec before each LA-ICP-MS analysis' (Methods, p.4); how it was subtracted is not described",
  "ada:internalStandardElement": "all: none \u2014 oxide-total normalization (Methods, p.4)",
  "ada:signalIntegrationIntervalMethod": "Plateau region of each spot's time-lapse plot \u2014 'The time-lapse plots of each spot were examined, and only the plateau region was used to quantify the trace element abundances' (Methods, p.4)",
  "ada:secondaryReferenceMaterialDefault": [
    "N \u2014 not stated"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:sampleIntroduction": "missing",
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
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:laQicpmsTAPP-Liu2016> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/LaserAblation/fusionFluxAndDilutionRatioDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/LaserAblation/preAblationSurfaceTreatmentDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "N — sections UT1 to UT3 (p.3); their preparation is not described" ;
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
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/LaserAblation/signalSmoothingDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ;
                    ada:detectionLimitMethod "all: 3σ of the background counts — Table 3 note d: 'LOD is the limit of detection estimated based on background counts to 3σ confidence interval'" ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/interPassDataDependency>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/instrumentWarmUpSessionDurationLimit>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSizeDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> ;
    schema1:datePublished "missing" ;
    schema1:description "The procedure broadly follows Udry et al. (2012) and Pernet-Fisher et al. (2014). Two internal-standard approaches: oxide-total normalization for silicates and oxides, EMP CaO for phosphate. A 90 µm beam on some olivines tested whether low REE signals reflect insufficient sampling (Methods, p.4)" ;
    schema1:instrument <ex:instrument/ICPMS>,
        <ex:instrument/Laser-Ablation-System> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Department of Geosciences, Virginia Tech" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "LA-ICP-MS — 'an Agilent 7500ce inductively coupled plasma–mass spectrometer (ICP-MS), coupled with a GeoLasPro 193 nm Excimer laser-ablation (LA) system' (Methods, p.4)" ] ;
    schema1:name "laQicpms protocol — Liu2016" ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "EMP gives major element compositions; for spots with EMP data, oxide-total normalization 'generally agrees within <10% with the method using EMP CaO or MgO values as internal standards' — Methods, p.4" ;
                    schema1:name "EPMA (EMP)" ] ;
            schema1:url "https://ada.astromat.org/missing" ],
        [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Udry et al. (2012); Pernet-Fisher et al. (2014) — 'The analytical procedure is broadly similar to that of Udry et al. (2012) and Pernet-Fisher et al. (2014)' (Methods, p.4)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:ablationPitDepthRateDefault "missing" ;
    ada:ablationSamplingMode "all: Spot — 'The time-lapse plots of each spot were examined' (Methods, p.4)" ;
    ada:ablationSpotDurationDefault "N — not stated" ;
    ada:analysisSequenceDefault "N — 'A NIST 610 glass standard was analyzed before and after every session' (Methods, p.4); the order within a session is not described" ;
    ada:backgroundCountTimeDefault "50 s — 'The background was counted for 50 sec before each LA-ICP-MS analysis' (Methods, p.4)" ;
    ada:blankBackgroundCorrectionMethod "N — the background 'was counted for 50 sec before each LA-ICP-MS analysis' (Methods, p.4); how it was subtracted is not described" ;
    ada:calibrationMeasurementFrequency "Before and after every session — 'A NIST 610 glass standard was analyzed before and after every session' (Methods, p.4)" ;
    ada:carrierGasFlowRateDefault "N — not stated" ;
    ada:constantsAndReferenceValuesUsedDefault "missing" ;
    ada:internalStandardApproach "all: normalization to 100 wt% oxide total — 'For silicates and oxides, trace element abundances were calculated by normalization to 100 wt% oxide total' (Methods, p.4)" ;
    ada:internalStandardElement "all: none — oxide-total normalization (Methods, p.4)" ;
    ada:massBiasCorrectionStrategy "missing" ;
    ada:numberOfAcquisitionPasses -9999 ;
    ada:oxideProductionMethodAndThreshold "N — not stated" ;
    ada:rasterLineSpacingDefault "N/A — spot analysis" ;
    ada:reportedProperties "Li, Be, K, Sc, Ti, V, Cr, Mn, Co, Ni, Cu, Zn, Ga, Ge, Rb, Sr, Y, Zr, Nb, Ba, La, Ce, Pr, Nd, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu, Hf, Ta, W, Au, Pb, Th, U (ppm) — trace element abundances in ppm, glass averages with 1σ and n in Table 3; mineral data in Table S1, not in the archived PDF" ;
    ada:sampleIntroduction "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "N — spots are screened after the fact, not before: \"The time-lapse plots of each spot were examined, and only the plateau region was used to quantify the trace element abundances\" (p.4). That is a rejection rule (see `Analysis Inclusion and Rejection Criteria`), not a rule for choosing units" ;
    ada:samplingUnitType "Phase > Spot — \"The time-lapse plots of each spot were examined, and only the plateau region was used to quantify the trace element abundances\" (p.4); abundances are reported as per-phase means (\"n = 7\", \"n = 13\", table p.9), the individual spots being in a supplement not in the archived PDF" ;
    ada:secondaryReferenceMaterialDefault "N — not stated" ;
    ada:signalCollectionMode "missing" ;
    ada:signalIntegrationIntervalMethod "Plateau region of each spot's time-lapse plot — 'The time-lapse plots of each spot were examined, and only the plateau region was used to quantify the trace element abundances' (Methods, p.4)" ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "glass",
                "oxides",
                "silicates" ;
            ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/laQicpmsTAPP/primaryCalibrationStandardName> ] ;
    ada:targetSpeciesTemplate [ ada:defaultTargetSpecies "Au",
                "Ba",
                "Be",
                "Ce",
                "Co",
                "Cr",
                "Cu",
                "Dy",
                "Er",
                "Eu",
                "Ga",
                "Gd",
                "Ge",
                "Hf",
                "Ho",
                "K",
                "La",
                "Li",
                "Lu",
                "Mn",
                "Nb",
                "Nd",
                "Ni",
                "Pb",
                "Pr",
                "Rb",
                "Sc",
                "Sm",
                "Sr",
                "Ta",
                "Tb",
                "Th",
                "Ti",
                "Tm",
                "U",
                "V",
                "W",
                "Y",
                "Yb",
                "Zn",
                "Zr" ;
            ada:targetSpeciesColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetSpecies" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/calibrationStrategyPerTargetSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/monitoredMasses>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/spectralInterferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ] ;
    ada:totalIntegrationTimePerOutputDataPointDefault -9999 ;
    ada:uncertaintyLevel "missing" ;
    bios:computationalTool [ schema1:name "AMS ver. 1.0 (Mutchler et al. 2008; Analysis Management System, stand-alone software)" ;
            ada:toolRole "dataReduction" ] .

<ex:instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuningDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigationDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS" ;
    schema1:hasPart <ex:instrument/ICPMS/part/Collision-Reaction-Cell>,
        <ex:instrument/ICPMS/part/ICP-Source>,
        <ex:instrument/ICPMS/part/Interface-Cone>,
        <ex:instrument/ICPMS/part/Torch> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "missing" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Agilent 7500ce ICP-MS" ] ;
    schema1:name "example instrumentName" .

<ex:instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "missing" .

<ex:instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPowerDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<ex:instrument/ICPMS/part/Interface-Cone> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Interface Cone" ;
    schema1:name "missing" .

<ex:instrument/ICPMS/part/Torch> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Torch" ;
    schema1:name "missing" .

<ex:instrument/Laser-Ablation-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/LaserAblation/laserEnergyDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Laser Ablation System" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "GeoLasPro 193 nm Excimer laser-ablation system — Methods, p.4" ] ;
    schema1:name "example instrumentName" ;
    ada:laserFluenceDefault "7–10 J/m² — as written: 'a fluence rate of 7–10 J/m2 on the sample' (Methods, p.4)" ;
    ada:laserRepetitionRateDefault "all: 5 Hz" ;
    ada:laserSpotGeometryDefault "all: 24 and 32 µm diameter, and 90 µm for a few olivine analyses — '24 and 32 µm diameter were commonly used for silicates and glass, and a few analyses were conducted on olivines using a 90 µm beam to evaluate whether the low signals of REEs are a result of insufficient sampling' (Methods, p.4)" ;
    ada:laserType "193 nm Excimer (ArF excimer)" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N — not stated" ;
    schema1:name "Coolant Plasma Gas Flow Rate" ;
    schema1:valueName "coolantPlasmaGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N — not stated" ;
    schema1:name "ICP Tuning" ;
    schema1:valueName "icpTuningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/instrumentWarmUpSessionDurationLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Instrument Warm up Session Duration Limit" ;
    schema1:value "N — not stated" ;
    schema1:valueName "instrumentWarmUpSessionDurationLimit" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N — not stated" ;
    schema1:name "Make-up Gas and Flow Rate" ;
    schema1:valueName "makeUpGasAndFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N — not stated" ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:valueName "memoryEffectMitigationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N — not stated" ;
    schema1:name "RF Power" ;
    schema1:valueName "rfPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/fusionFluxAndDilutionRatioDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N/A — in situ" ;
    schema1:name "Fusion Flux and Dilution Ratio" ;
    schema1:valueName "fusionFluxAndDilutionRatioDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/laserEnergyDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 150 ;
    schema1:description "150 mJ output energy — Methods, p.4" ;
    schema1:name "Laser Energy" ;
    schema1:valueName "laserEnergyDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/preAblationSurfaceTreatmentDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N — not stated" ;
    schema1:name "Pre Ablation Surface Treatment" ;
    schema1:valueName "preAblationSurfaceTreatmentDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/signalSmoothingDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N — not stated" ;
    schema1:name "Signal Smoothing" ;
    schema1:valueName "signalSmoothingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSizeDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N/A — spot analysis" ;
    schema1:name "Transect Rate Mapping Rate or Step Size" ;
    schema1:valueName "transectRateMappingRateOrStepSizeDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Petrographic microscopy, SEM and EMP — \"The petrography of these sections was examined using a petrographic microscope and a scanning electron microscope\", followed by BSE images and element maps (p.3); the EMP results then serve as internal standards for the ablation data, which are normalised using \"EMP CaO or MgO values\" for silicates and \"40Ca counts to CaO concentrations from the EMP analysis\" for phosphate (p.4)" ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:valueName "preAnalysisImagingAndScreeningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/targetMaterialColumn/laQicpmsTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/calibrationStrategyPerTargetSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Calibration Strategy per Target Species" ;
    schema1:valueName "calibrationStrategyPerTargetSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Internal (Within-Measurement) Analytical Precision and Assessment Method" ;
    schema1:valueName "internalAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/monitoredMasses> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Monitored Masses" ;
    schema1:valueName "monitoredMasses" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/spectralInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Spectral Interference Corrections Applied" ;
    schema1:valueName "spectralInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/interPassDataDependency> a schema1:PropertyValue ;
    schema1:name "Inter-Pass Data Dependency" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/interPassDataDependency> ;
    schema1:value "N/A — a single acquisition pass" .


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
  "schema:description": "laQicpmsTAPP instance derived from Liu et al. 2016 (M&PS 51) Tissint martian meteorite Phosphate (merrillite) Spot analysis LA-Q-ICP-MS Virginia Tech (publication column of LA-Q-ICP-MS_TAPP_v96.csv).",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "sodium-merrillite"
    ],
    "ada:targetMaterialColumns": [
      {
        "schema:valueName": "targetMaterial",
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
        "@id": "ada:targetMaterialColumn/laQicpmsTAPP/primaryCalibrationStandardName",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "primaryCalibrationStandardName",
        "schema:name": "Primary Calibration Standard Name",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
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
            "schema:defaultValue": "N/A — in situ"
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
            "schema:defaultValue": "N — not stated"
          }
        ],
        "schema:description": "N — sections UT1 to UT3 (p.3); their preparation is not described",
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
            "@id": "ada:parameter/module/LaserAblation/signalSmoothingDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "signalSmoothingDefault",
            "schema:name": "Signal Smoothing",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "N — not stated"
          }
        ],
        "ada:detectionLimitMethod": "all: 3σ of the background counts — Table 3 note d: 'LOD is the limit of detection estimated based on background counts to 3σ confidence interval'",
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
  "ada:samplingUnitSelectionCriteriaDefault": "N — spots are screened after the fact, not before: \"The time-lapse plots of each spot were examined, and only the plateau region was used to quantify the trace element abundances\" (p.4). That is a rejection rule (see `Analysis Inclusion and Rejection Criteria`), not a rule for choosing units",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "preAnalysisImagingAndScreeningDefault",
      "schema:name": "Pre-Analysis Imaging and Screening",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Petrographic microscopy, SEM and EMP — \"The petrography of these sections was examined using a petrographic microscope and a scanning electron microscope\", followed by BSE images and element maps (p.3); the EMP results then serve as internal standards for the ablation data, which are normalised using \"EMP CaO or MgO values\" for silicates and \"40Ca counts to CaO concentrations from the EMP analysis\" for phosphate (p.4)"
    },
    {
      "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSizeDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "transectRateMappingRateOrStepSizeDefault",
      "schema:name": "Transect Rate Mapping Rate or Step Size",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N/A — spot analysis"
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
      "schema:defaultValue": "N — not stated"
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
      "schema:value": "N — not stated"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/interPassDataDependency",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/interPassDataDependency"
        }
      ],
      "schema:name": "Inter-Pass Data Dependency",
      "schema:value": "N/A — a single acquisition pass"
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
              "schema:defaultValue": "N — not stated"
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
              "schema:defaultValue": "N — not stated"
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
          "schema:defaultValue": "N — not stated"
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
          "schema:defaultValue": "N — not stated"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/ICPMS",
      "schema:name": "example instrumentName",
      "schema:manufacturer": {
        "schema:name": "missing",
        "@type": [
          "schema:Organization"
        ]
      }
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
          "schema:description": "150 mJ output energy — Methods, p.4"
        }
      ],
      "schema:model": {
        "schema:name": "GeoLasPro 193 nm Excimer laser-ablation system — Methods, p.4",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "193 nm Excimer (ArF excimer)",
      "ada:laserSpotGeometryDefault": "all: ~24 µm diameter — 'The smaller spot (~24 µm) size was used for phosphate analysis' (Methods, p.4)",
      "ada:laserFluenceDefault": "7–10 J/m² — as written: 'a fluence rate of 7–10 J/m2 on the sample' (Methods, p.4)",
      "ada:laserRepetitionRateDefault": "all: 5 Hz",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/Laser-Ablation-System",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:carrierGasFlowRateDefault": "N — not stated",
  "ada:analysisSequenceDefault": "N — 'A NIST 610 glass standard was analyzed before and after every session' (Methods, p.4); the order within a session is not described",
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "La",
      "Ce",
      "Pr",
      "Nd",
      "Sm",
      "Eu",
      "Gd",
      "Tb",
      "Dy",
      "Ho",
      "Er",
      "Tm",
      "Yb",
      "Lu",
      "Sr",
      "Ti"
    ],
    "ada:targetSpeciesColumns": [
      {
        "schema:valueName": "targetSpecies",
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
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:backgroundCountTimeDefault": "50 s — 'The background was counted for 50 sec before each LA-ICP-MS analysis' (Methods, p.4)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-ICP-MS — 'an Agilent 7500ce inductively coupled plasma–mass spectrometer (ICP-MS), coupled with a GeoLasPro 193 nm Excimer laser-ablation (LA) system' (Methods, p.4)"
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
        "schema:name": "Udry et al. (2012); Pernet-Fisher et al. (2014) — 'The analytical procedure is broadly similar to that of Udry et al. (2012) and Pernet-Fisher et al. (2014)' (Methods, p.4)"
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
        "schema:description": "EMP CaO is the internal standard: 'we calculated the trace element abundances by normalizing the LA-ICP-MS 40Ca counts to CaO concentrations from the EMP analysis' — Methods, p.4"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Phase > Spot — \"The time-lapse plots of each spot were examined, and only the plateau region was used to quantify the trace element abundances\" (p.4); abundances are reported as per-phase means (\"n = 7\", \"n = 13\", table p.9), the individual spots being in a supplement not in the archived PDF",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "AMS ver. 1.0 (Mutchler et al. 2008)"
    }
  ],
  "ada:reportedProperties": [
    "La, Ce, Pr, Nd, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu (ppm); Sr; Ti — merrillite REE, chondrite-normalized in Fig. 9; data in Table S1, not in the archived PDF"
  ],
  "ada:ablationSamplingMode": [
    "all: Spot — 'The time-lapse plots of each spot were examined' (Methods, p.4)"
  ],
  "ada:ablationSpotDurationDefault": "N — not stated",
  "ada:rasterLineSpacingDefault": "N/A — spot analysis",
  "ada:internalStandardApproach": "all: single element measured by EMP — 'normalizing the LA-ICP-MS 40Ca counts to CaO concentrations from the EMP analysis' (Methods, p.4)",
  "ada:calibrationMeasurementFrequency": "Before and after every session — 'A NIST 610 glass standard was analyzed before and after every session' (Methods, p.4)",
  "ada:oxideProductionMethodAndThreshold": "N — not stated",
  "ada:blankBackgroundCorrectionMethod": "N — the background 'was counted for 50 sec before each LA-ICP-MS analysis' (Methods, p.4); how it was subtracted is not described",
  "ada:internalStandardElement": "all: Ca (⁴⁰Ca) — CaO from EMP (Methods, p.4)",
  "ada:signalIntegrationIntervalMethod": "Plateau region of each spot's time-lapse plot — 'The time-lapse plots of each spot were examined, and only the plateau region was used to quantify the trace element abundances' (Methods, p.4)",
  "ada:secondaryReferenceMaterialDefault": [
    "N — not stated"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:sampleIntroduction": "missing",
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
  "schema:description": "laQicpmsTAPP instance derived from Liu et al. 2016 (M&PS 51) Tissint martian meteorite Phosphate (merrillite) Spot analysis LA-Q-ICP-MS Virginia Tech (publication column of LA-Q-ICP-MS_TAPP_v96.csv).",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "sodium-merrillite"
    ],
    "ada:targetMaterialColumns": [
      {
        "schema:valueName": "targetMaterial",
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
        "@id": "ada:targetMaterialColumn/laQicpmsTAPP/primaryCalibrationStandardName",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "primaryCalibrationStandardName",
        "schema:name": "Primary Calibration Standard Name",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
    ]
  },
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
            "schema:defaultValue": "N/A \u2014 in situ"
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
            "schema:defaultValue": "N \u2014 not stated"
          }
        ],
        "schema:description": "N \u2014 sections UT1 to UT3 (p.3); their preparation is not described",
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
            "@id": "ada:parameter/module/LaserAblation/signalSmoothingDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "signalSmoothingDefault",
            "schema:name": "Signal Smoothing",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "N \u2014 not stated"
          }
        ],
        "ada:detectionLimitMethod": "all: 3\u03c3 of the background counts \u2014 Table 3 note d: 'LOD is the limit of detection estimated based on background counts to 3\u03c3 confidence interval'",
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
  "ada:samplingUnitSelectionCriteriaDefault": "N \u2014 spots are screened after the fact, not before: \"The time-lapse plots of each spot were examined, and only the plateau region was used to quantify the trace element abundances\" (p.4). That is a rejection rule (see `Analysis Inclusion and Rejection Criteria`), not a rule for choosing units",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "preAnalysisImagingAndScreeningDefault",
      "schema:name": "Pre-Analysis Imaging and Screening",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Petrographic microscopy, SEM and EMP \u2014 \"The petrography of these sections was examined using a petrographic microscope and a scanning electron microscope\", followed by BSE images and element maps (p.3); the EMP results then serve as internal standards for the ablation data, which are normalised using \"EMP CaO or MgO values\" for silicates and \"40Ca counts to CaO concentrations from the EMP analysis\" for phosphate (p.4)"
    },
    {
      "@id": "ada:parameter/module/LaserAblation/transectRateMappingRateOrStepSizeDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "transectRateMappingRateOrStepSizeDefault",
      "schema:name": "Transect Rate Mapping Rate or Step Size",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N/A \u2014 spot analysis"
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
      "schema:defaultValue": "N \u2014 not stated"
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
      "schema:value": "N \u2014 not stated"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/interPassDataDependency",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/interPassDataDependency"
        }
      ],
      "schema:name": "Inter-Pass Data Dependency",
      "schema:value": "N/A \u2014 a single acquisition pass"
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
              "schema:defaultValue": "N \u2014 not stated"
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
              "schema:defaultValue": "N \u2014 not stated"
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
          "schema:defaultValue": "N \u2014 not stated"
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
          "schema:defaultValue": "N \u2014 not stated"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/ICPMS",
      "schema:name": "example instrumentName",
      "schema:manufacturer": {
        "schema:name": "missing",
        "@type": [
          "schema:Organization"
        ]
      }
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
          "schema:description": "150 mJ output energy \u2014 Methods, p.4"
        }
      ],
      "schema:model": {
        "schema:name": "GeoLasPro 193 nm Excimer laser-ablation system \u2014 Methods, p.4",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "193 nm Excimer (ArF excimer)",
      "ada:laserSpotGeometryDefault": "all: ~24 \u00b5m diameter \u2014 'The smaller spot (~24 \u00b5m) size was used for phosphate analysis' (Methods, p.4)",
      "ada:laserFluenceDefault": "7\u201310 J/m\u00b2 \u2014 as written: 'a fluence rate of 7\u201310 J/m2 on the sample' (Methods, p.4)",
      "ada:laserRepetitionRateDefault": "all: 5 Hz",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/Laser-Ablation-System",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:carrierGasFlowRateDefault": "N \u2014 not stated",
  "ada:analysisSequenceDefault": "N \u2014 'A NIST 610 glass standard was analyzed before and after every session' (Methods, p.4); the order within a session is not described",
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "La",
      "Ce",
      "Pr",
      "Nd",
      "Sm",
      "Eu",
      "Gd",
      "Tb",
      "Dy",
      "Ho",
      "Er",
      "Tm",
      "Yb",
      "Lu",
      "Sr",
      "Ti"
    ],
    "ada:targetSpeciesColumns": [
      {
        "schema:valueName": "targetSpecies",
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
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:backgroundCountTimeDefault": "50 s \u2014 'The background was counted for 50 sec before each LA-ICP-MS analysis' (Methods, p.4)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-ICP-MS \u2014 'an Agilent 7500ce inductively coupled plasma\u2013mass spectrometer (ICP-MS), coupled with a GeoLasPro 193 nm Excimer laser-ablation (LA) system' (Methods, p.4)"
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
        "schema:name": "Udry et al. (2012); Pernet-Fisher et al. (2014) \u2014 'The analytical procedure is broadly similar to that of Udry et al. (2012) and Pernet-Fisher et al. (2014)' (Methods, p.4)"
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
        "schema:description": "EMP CaO is the internal standard: 'we calculated the trace element abundances by normalizing the LA-ICP-MS 40Ca counts to CaO concentrations from the EMP analysis' \u2014 Methods, p.4"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Phase > Spot \u2014 \"The time-lapse plots of each spot were examined, and only the plateau region was used to quantify the trace element abundances\" (p.4); abundances are reported as per-phase means (\"n = 7\", \"n = 13\", table p.9), the individual spots being in a supplement not in the archived PDF",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "AMS ver. 1.0 (Mutchler et al. 2008)"
    }
  ],
  "ada:reportedProperties": [
    "La, Ce, Pr, Nd, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu (ppm); Sr; Ti \u2014 merrillite REE, chondrite-normalized in Fig. 9; data in Table S1, not in the archived PDF"
  ],
  "ada:ablationSamplingMode": [
    "all: Spot \u2014 'The time-lapse plots of each spot were examined' (Methods, p.4)"
  ],
  "ada:ablationSpotDurationDefault": "N \u2014 not stated",
  "ada:rasterLineSpacingDefault": "N/A \u2014 spot analysis",
  "ada:internalStandardApproach": "all: single element measured by EMP \u2014 'normalizing the LA-ICP-MS 40Ca counts to CaO concentrations from the EMP analysis' (Methods, p.4)",
  "ada:calibrationMeasurementFrequency": "Before and after every session \u2014 'A NIST 610 glass standard was analyzed before and after every session' (Methods, p.4)",
  "ada:oxideProductionMethodAndThreshold": "N \u2014 not stated",
  "ada:blankBackgroundCorrectionMethod": "N \u2014 the background 'was counted for 50 sec before each LA-ICP-MS analysis' (Methods, p.4); how it was subtracted is not described",
  "ada:internalStandardElement": "all: Ca (\u2074\u2070Ca) \u2014 CaO from EMP (Methods, p.4)",
  "ada:signalIntegrationIntervalMethod": "Plateau region of each spot's time-lapse plot \u2014 'The time-lapse plots of each spot were examined, and only the plateau region was used to quantify the trace element abundances' (Methods, p.4)",
  "ada:secondaryReferenceMaterialDefault": [
    "N \u2014 not stated"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:sampleIntroduction": "missing",
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
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:laQicpmsTAPP-Liu2016-2> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/LaserAblation/signalSmoothingDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ;
                    ada:detectionLimitMethod "all: 3σ of the background counts — Table 3 note d: 'LOD is the limit of detection estimated based on background counts to 3σ confidence interval'" ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/LaserAblation/fusionFluxAndDilutionRatioDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/LaserAblation/preAblationSurfaceTreatmentDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "N — sections UT1 to UT3 (p.3); their preparation is not described" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "missing" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/interPassDataDependency>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/instrumentWarmUpSessionDurationLimit>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSizeDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> ;
    schema1:datePublished "missing" ;
    schema1:description "laQicpmsTAPP instance derived from Liu et al. 2016 (M&PS 51) Tissint martian meteorite Phosphate (merrillite) Spot analysis LA-Q-ICP-MS Virginia Tech (publication column of LA-Q-ICP-MS_TAPP_v96.csv)." ;
    schema1:instrument <ex:instrument/ICPMS>,
        <ex:instrument/Laser-Ablation-System> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Department of Geosciences, Virginia Tech" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "LA-ICP-MS — 'an Agilent 7500ce inductively coupled plasma–mass spectrometer (ICP-MS), coupled with a GeoLasPro 193 nm Excimer laser-ablation (LA) system' (Methods, p.4)" ] ;
    schema1:name "laQicpms protocol — Liu2016-2" ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "EMP CaO is the internal standard: 'we calculated the trace element abundances by normalizing the LA-ICP-MS 40Ca counts to CaO concentrations from the EMP analysis' — Methods, p.4" ;
                    schema1:name "EPMA (EMP)" ] ;
            schema1:url "https://ada.astromat.org/missing" ],
        [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Udry et al. (2012); Pernet-Fisher et al. (2014) — 'The analytical procedure is broadly similar to that of Udry et al. (2012) and Pernet-Fisher et al. (2014)' (Methods, p.4)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:ablationPitDepthRateDefault "missing" ;
    ada:ablationSamplingMode "all: Spot — 'The time-lapse plots of each spot were examined' (Methods, p.4)" ;
    ada:ablationSpotDurationDefault "N — not stated" ;
    ada:analysisSequenceDefault "N — 'A NIST 610 glass standard was analyzed before and after every session' (Methods, p.4); the order within a session is not described" ;
    ada:backgroundCountTimeDefault "50 s — 'The background was counted for 50 sec before each LA-ICP-MS analysis' (Methods, p.4)" ;
    ada:blankBackgroundCorrectionMethod "N — the background 'was counted for 50 sec before each LA-ICP-MS analysis' (Methods, p.4); how it was subtracted is not described" ;
    ada:calibrationMeasurementFrequency "Before and after every session — 'A NIST 610 glass standard was analyzed before and after every session' (Methods, p.4)" ;
    ada:carrierGasFlowRateDefault "N — not stated" ;
    ada:constantsAndReferenceValuesUsedDefault "missing" ;
    ada:internalStandardApproach "all: single element measured by EMP — 'normalizing the LA-ICP-MS 40Ca counts to CaO concentrations from the EMP analysis' (Methods, p.4)" ;
    ada:internalStandardElement "all: Ca (⁴⁰Ca) — CaO from EMP (Methods, p.4)" ;
    ada:massBiasCorrectionStrategy "missing" ;
    ada:numberOfAcquisitionPasses -9999 ;
    ada:oxideProductionMethodAndThreshold "N — not stated" ;
    ada:rasterLineSpacingDefault "N/A — spot analysis" ;
    ada:reportedProperties "La, Ce, Pr, Nd, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu (ppm); Sr; Ti — merrillite REE, chondrite-normalized in Fig. 9; data in Table S1, not in the archived PDF" ;
    ada:sampleIntroduction "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "N — spots are screened after the fact, not before: \"The time-lapse plots of each spot were examined, and only the plateau region was used to quantify the trace element abundances\" (p.4). That is a rejection rule (see `Analysis Inclusion and Rejection Criteria`), not a rule for choosing units" ;
    ada:samplingUnitType "Phase > Spot — \"The time-lapse plots of each spot were examined, and only the plateau region was used to quantify the trace element abundances\" (p.4); abundances are reported as per-phase means (\"n = 7\", \"n = 13\", table p.9), the individual spots being in a supplement not in the archived PDF" ;
    ada:secondaryReferenceMaterialDefault "N — not stated" ;
    ada:signalCollectionMode "missing" ;
    ada:signalIntegrationIntervalMethod "Plateau region of each spot's time-lapse plot — 'The time-lapse plots of each spot were examined, and only the plateau region was used to quantify the trace element abundances' (Methods, p.4)" ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "sodium-merrillite" ;
            ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/laQicpmsTAPP/primaryCalibrationStandardName> ] ;
    ada:targetSpeciesTemplate [ ada:defaultTargetSpecies "Ce",
                "Dy",
                "Er",
                "Eu",
                "Gd",
                "Ho",
                "La",
                "Lu",
                "Nd",
                "Pr",
                "Sm",
                "Sr",
                "Tb",
                "Ti",
                "Tm",
                "Yb" ;
            ada:targetSpeciesColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetSpecies" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/calibrationStrategyPerTargetSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/monitoredMasses>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/spectralInterferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ] ;
    ada:totalIntegrationTimePerOutputDataPointDefault -9999 ;
    ada:uncertaintyLevel "missing" ;
    bios:computationalTool [ schema1:name "AMS ver. 1.0 (Mutchler et al. 2008)" ;
            ada:toolRole "dataReduction" ] .

<ex:instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuningDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigationDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS" ;
    schema1:hasPart <ex:instrument/ICPMS/part/Collision-Reaction-Cell>,
        <ex:instrument/ICPMS/part/ICP-Source>,
        <ex:instrument/ICPMS/part/Interface-Cone>,
        <ex:instrument/ICPMS/part/Torch> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "missing" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Agilent 7500ce ICP-MS" ] ;
    schema1:name "example instrumentName" .

<ex:instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "missing" .

<ex:instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPowerDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<ex:instrument/ICPMS/part/Interface-Cone> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Interface Cone" ;
    schema1:name "missing" .

<ex:instrument/ICPMS/part/Torch> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Torch" ;
    schema1:name "missing" .

<ex:instrument/Laser-Ablation-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/LaserAblation/laserEnergyDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Laser Ablation System" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "GeoLasPro 193 nm Excimer laser-ablation system — Methods, p.4" ] ;
    schema1:name "example instrumentName" ;
    ada:laserFluenceDefault "7–10 J/m² — as written: 'a fluence rate of 7–10 J/m2 on the sample' (Methods, p.4)" ;
    ada:laserRepetitionRateDefault "all: 5 Hz" ;
    ada:laserSpotGeometryDefault "all: ~24 µm diameter — 'The smaller spot (~24 µm) size was used for phosphate analysis' (Methods, p.4)" ;
    ada:laserType "193 nm Excimer (ArF excimer)" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N — not stated" ;
    schema1:name "Coolant Plasma Gas Flow Rate" ;
    schema1:valueName "coolantPlasmaGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N — not stated" ;
    schema1:name "ICP Tuning" ;
    schema1:valueName "icpTuningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/instrumentWarmUpSessionDurationLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Instrument Warm up Session Duration Limit" ;
    schema1:value "N — not stated" ;
    schema1:valueName "instrumentWarmUpSessionDurationLimit" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N — not stated" ;
    schema1:name "Make-up Gas and Flow Rate" ;
    schema1:valueName "makeUpGasAndFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N — not stated" ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:valueName "memoryEffectMitigationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N — not stated" ;
    schema1:name "RF Power" ;
    schema1:valueName "rfPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/fusionFluxAndDilutionRatioDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N/A — in situ" ;
    schema1:name "Fusion Flux and Dilution Ratio" ;
    schema1:valueName "fusionFluxAndDilutionRatioDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/laserEnergyDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 150 ;
    schema1:description "150 mJ output energy — Methods, p.4" ;
    schema1:name "Laser Energy" ;
    schema1:valueName "laserEnergyDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/preAblationSurfaceTreatmentDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N — not stated" ;
    schema1:name "Pre Ablation Surface Treatment" ;
    schema1:valueName "preAblationSurfaceTreatmentDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/signalSmoothingDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N — not stated" ;
    schema1:name "Signal Smoothing" ;
    schema1:valueName "signalSmoothingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSizeDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N/A — spot analysis" ;
    schema1:name "Transect Rate Mapping Rate or Step Size" ;
    schema1:valueName "transectRateMappingRateOrStepSizeDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Petrographic microscopy, SEM and EMP — \"The petrography of these sections was examined using a petrographic microscope and a scanning electron microscope\", followed by BSE images and element maps (p.3); the EMP results then serve as internal standards for the ablation data, which are normalised using \"EMP CaO or MgO values\" for silicates and \"40Ca counts to CaO concentrations from the EMP analysis\" for phosphate (p.4)" ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:valueName "preAnalysisImagingAndScreeningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/targetMaterialColumn/laQicpmsTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/calibrationStrategyPerTargetSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Calibration Strategy per Target Species" ;
    schema1:valueName "calibrationStrategyPerTargetSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Internal (Within-Measurement) Analytical Precision and Assessment Method" ;
    schema1:valueName "internalAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/monitoredMasses> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Monitored Masses" ;
    schema1:valueName "monitoredMasses" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/spectralInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Spectral Interference Corrections Applied" ;
    schema1:valueName "spectralInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/interPassDataDependency> a schema1:PropertyValue ;
    schema1:name "Inter-Pass Data Dependency" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/interPassDataDependency> ;
    schema1:value "N/A — a single acquisition pass" .


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
  "schema:description": "laQicpmsTAPP instance derived from Wu+etal2023 | Analyte G2 + iCAP TQ ICP-MS/MS | IGGCAS (publication column of LA-Q-ICP-MS_TAPP_v96.csv). Reported detail: ada:signalCollectionMode = Peak jump.",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "xenotime",
      "apatite",
      "garnet"
    ],
    "ada:targetMaterialColumns": [
      {
        "schema:valueName": "targetMaterial",
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
        "@id": "ada:targetMaterialColumn/laQicpmsTAPP/primaryCalibrationStandardName",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "primaryCalibrationStandardName",
        "schema:name": "Primary Calibration Standard Name",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
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
              "@id": "ada:parameter/module/ICPMS/configuration",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "configuration",
              "schema:name": "Configuration",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "High sensitivity sample and skimmer cones"
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
              "schema:defaultValue": 15.0,
              "schema:description": "15.00 L min-1 Ar"
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
              "schema:description": "0.80 L min-1 Ar"
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
          "schema:additionalType": [
            "Collision Reaction Cell",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/CollisionCell/cellExitDiscriminationVoltageDefault",
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
              "@id": "ada:parameter/module/CollisionCell/reactionGasType",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "reactionGasType",
              "schema:name": "Reaction Gas Type",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "all: NH3, high purity (>99.999%) — supplied in T4; He (>99.999%, T1) was pre-mixed with NH3 before the cell in a test of mixture composition"
            }
          ],
          "schema:name": "all: TQ mode with NH3 reaction gas, the first quadrupole at 1 amu — tuning first in SQ no-gas mode; 'To avoid interference from 175Lu reaction products ... the required prefiltered mass resolution is 1 amu' (§3.1)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
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
          "schema:defaultValue": "~300"
        },
        {
          "@id": "ada:parameter/module/SingleCollector/detectorConfiguration",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "detectorConfiguration",
          "schema:name": "Detector Configuration",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:value": "Single SEM in double mode, counting and analog"
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
          "schema:defaultValue": "Two-stage: first optimised in solution single-quadrupole and no-gas modes to tune for a robust plasma (U/Th = 1.00-1.05) and minimise oxides (ThO/Th < 0.5%); then switched to TQ and NH3 mode, with lenses tuned to maximise sensitivity for Hf reaction products while keeping Lu and Yb reaction rates low"
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
      "ada:laserSpotGeometryDefault": "all: 50, 90, 150 µm — Table 1 'Spot size'; chosen according to Lu and Hf contents",
      "ada:laserFluenceDefault": "4 J cm-2",
      "ada:laserRepetitionRateDefault": "all: 10 Hz — Table 1",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/Laser-Ablation-System"
    }
  ],
  "ada:carrierGasFlowRateDefault": "He ablation gas 900 mL/min; Ar carrier gas 0.65 L/min — Table 1 'Ablation gas flow (He)' and 'Carrier gas flow (Ar)'",
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
      "schema:defaultValue": 2,
      "schema:description": "N2 enhancement gas, 4.0 mL min-1, added to the carrier gas after the sample chamber to enhance sensitivity; an 80% sensitivity improvement is reported"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/collisionReactionGasMixtureRatioDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "collisionReactionGasMixtureRatioDefault",
      "schema:name": "Collision/Reaction Gas Mixture Ratio",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "all: high-purity NH3 — found more effective than the commonly used 1:9 NH3-He mixture; He pre-mixed with NH3 was tested for the effect of mixture composition"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/reactionProductIonMassShiftTransition",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/reactionProductIonMassShiftTransition"
        }
      ],
      "schema:name": "Reaction Product Ion / Mass-Shift Transition",
      "schema:value": "(172+82)Yb, (175+82)Lu, (176+82)Hf, (177+82)Hf, (178+82)Hf: ammonia cluster adduct, mass shift +82; other: N — (176+82)Hf = 176Hf(14N1H)(14N1H2)3(14N1H3)3; Lu, Yb and Hf reaction products identified over 175–300 amu"
    }
  ],
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Lu",
      "Hf"
    ],
    "ada:targetSpeciesColumns": [
      {
        "schema:valueName": "targetSpecies",
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
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:signalCollectionMode": "N/A",
  "ada:totalIntegrationTimePerOutputDataPointDefault": "0.659 s",
  "ada:backgroundCountTimeDefault": "N — gas-blank correction applied in Iolite, duration not stated",
  "ada:constantsAndReferenceValuesUsedDefault": "NIST SRM 610 recommended values 176Lu/177Hf = 0.1379 +/- 0.0050 and 176Hf/177Hf = 0.282111 +/- 0.000009, as determined by ID-MC-ICP-MS; 176Lu/175Lu = 0.02655; 176Yb/172Yb = 0.5887; 177Hf/178Hf = 0.682; 176Lu half-life ~37.12 Ga",
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
  "ada:samplingUnitType": "Laser spot — 246 spot analyses on XN02 alone; spot diameters 50-150 um depending on Lu and Hf contents",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Iolite v.3.7 for gas-blank-corrected intensities, raw ratios and uncertainties; an in-house Microsoft Excel spreadsheet for drift, elemental fractionation and matrix-induced bias; IsoplotR for isochron and weighted-mean ages"
    }
  ],
  "ada:reportedProperties": [
    "176Lu/177Hf; 176Hf/177Hf; common-Hf-corrected single-spot age (Ma); Lu-Hf isochron age (Ma); Lu-Hf weighted-mean age (Ma); Lu concentration; Hf concentration — single-spot ages from eqn (11); isochron and weighted-mean ages in IsoplotR; Lu and Hf concentrations from Iolite's 'Trace_Element' DRS"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "N — not described; §2.1 gives only the origin of the megacrysts and single crystals, and the acknowledgements credit sample preparation without stating a method",
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
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 3,
        "ada:detectionLimitMethod": "missing"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "ada:ablationSamplingMode": [
    "all: Single hole drilling, two cleaning pulses — Table 1 'Sampling mode/pattern'"
  ],
  "ada:ablationSpotDurationDefault": "25 s",
  "ada:uncertaintyLevel": "2SE for single-spot ages; uncertainties on weighted-mean ages quoted at 2s",
  "ada:oxideProductionMethodAndThreshold": "ThO/Th < 0.5%, checked during SQ no-gas tuning",
  "ada:blankBackgroundCorrectionMethod": "Gas-blank-corrected intensities calculated in Iolite v.3.7 from time-resolved intensities",
  "ada:secondaryReferenceMaterialDefault": [
    "ARM-1; MG-1, BS-1, XENOA, M1567; Otter Lake, NW-1, MAP-3 — ARM-1 'is used for the quality control' of Lu and Hf concentrations; the xenotime and apatite U–Pb reference materials test the Lu–Hf ages against their ID-TIMS U–Pb ages"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:analysisSequenceDefault": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:internalStandardApproach": "missing",
  "ada:internalStandardElement": "missing",
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
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
  "schema:description": "laQicpmsTAPP instance derived from Wu+etal2023 | Analyte G2 + iCAP TQ ICP-MS/MS | IGGCAS (publication column of LA-Q-ICP-MS_TAPP_v96.csv). Reported detail: ada:signalCollectionMode = Peak jump.",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "xenotime",
      "apatite",
      "garnet"
    ],
    "ada:targetMaterialColumns": [
      {
        "schema:valueName": "targetMaterial",
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
        "@id": "ada:targetMaterialColumn/laQicpmsTAPP/primaryCalibrationStandardName",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "primaryCalibrationStandardName",
        "schema:name": "Primary Calibration Standard Name",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      }
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
              "@id": "ada:parameter/module/ICPMS/configuration",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "configuration",
              "schema:name": "Configuration",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "High sensitivity sample and skimmer cones"
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
              "schema:defaultValue": 15.0,
              "schema:description": "15.00 L min-1 Ar"
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
              "schema:description": "0.80 L min-1 Ar"
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
          "schema:additionalType": [
            "Collision Reaction Cell",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/module/CollisionCell/cellExitDiscriminationVoltageDefault",
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
              "@id": "ada:parameter/module/CollisionCell/reactionGasType",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "reactionGasType",
              "schema:name": "Reaction Gas Type",
              "ada:dataType": "string",
              "ada:fieldScope": "session",
              "schema:value": "all: NH3, high purity (>99.999%) \u2014 supplied in T4; He (>99.999%, T1) was pre-mixed with NH3 before the cell in a test of mixture composition"
            }
          ],
          "schema:name": "all: TQ mode with NH3 reaction gas, the first quadrupole at 1 amu \u2014 tuning first in SQ no-gas mode; 'To avoid interference from 175Lu reaction products ... the required prefiltered mass resolution is 1 amu' (\u00a73.1)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
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
          "schema:defaultValue": "~300"
        },
        {
          "@id": "ada:parameter/module/SingleCollector/detectorConfiguration",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "detectorConfiguration",
          "schema:name": "Detector Configuration",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:value": "Single SEM in double mode, counting and analog"
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
          "schema:defaultValue": "Two-stage: first optimised in solution single-quadrupole and no-gas modes to tune for a robust plasma (U/Th = 1.00-1.05) and minimise oxides (ThO/Th < 0.5%); then switched to TQ and NH3 mode, with lenses tuned to maximise sensitivity for Hf reaction products while keeping Lu and Yb reaction rates low"
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
      "ada:laserSpotGeometryDefault": "all: 50, 90, 150 \u00b5m \u2014 Table 1 'Spot size'; chosen according to Lu and Hf contents",
      "ada:laserFluenceDefault": "4 J cm-2",
      "ada:laserRepetitionRateDefault": "all: 10 Hz \u2014 Table 1",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/Laser-Ablation-System"
    }
  ],
  "ada:carrierGasFlowRateDefault": "He ablation gas 900 mL/min; Ar carrier gas 0.65 L/min \u2014 Table 1 'Ablation gas flow (He)' and 'Carrier gas flow (Ar)'",
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
      "schema:defaultValue": 2,
      "schema:description": "N2 enhancement gas, 4.0 mL min-1, added to the carrier gas after the sample chamber to enhance sensitivity; an 80% sensitivity improvement is reported"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/collisionReactionGasMixtureRatioDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "collisionReactionGasMixtureRatioDefault",
      "schema:name": "Collision/Reaction Gas Mixture Ratio",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "all: high-purity NH3 \u2014 found more effective than the commonly used 1:9 NH3-He mixture; He pre-mixed with NH3 was tested for the effect of mixture composition"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/reactionProductIonMassShiftTransition",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/reactionProductIonMassShiftTransition"
        }
      ],
      "schema:name": "Reaction Product Ion / Mass-Shift Transition",
      "schema:value": "(172+82)Yb, (175+82)Lu, (176+82)Hf, (177+82)Hf, (178+82)Hf: ammonia cluster adduct, mass shift +82; other: N \u2014 (176+82)Hf = 176Hf(14N1H)(14N1H2)3(14N1H3)3; Lu, Yb and Hf reaction products identified over 175\u2013300 amu"
    }
  ],
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Lu",
      "Hf"
    ],
    "ada:targetSpeciesColumns": [
      {
        "schema:valueName": "targetSpecies",
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
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:signalCollectionMode": "N/A",
  "ada:totalIntegrationTimePerOutputDataPointDefault": "0.659 s",
  "ada:backgroundCountTimeDefault": "N \u2014 gas-blank correction applied in Iolite, duration not stated",
  "ada:constantsAndReferenceValuesUsedDefault": "NIST SRM 610 recommended values 176Lu/177Hf = 0.1379 +/- 0.0050 and 176Hf/177Hf = 0.282111 +/- 0.000009, as determined by ID-MC-ICP-MS; 176Lu/175Lu = 0.02655; 176Yb/172Yb = 0.5887; 177Hf/178Hf = 0.682; 176Lu half-life ~37.12 Ga",
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
  "ada:samplingUnitType": "Laser spot \u2014 246 spot analyses on XN02 alone; spot diameters 50-150 um depending on Lu and Hf contents",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Iolite v.3.7 for gas-blank-corrected intensities, raw ratios and uncertainties; an in-house Microsoft Excel spreadsheet for drift, elemental fractionation and matrix-induced bias; IsoplotR for isochron and weighted-mean ages"
    }
  ],
  "ada:reportedProperties": [
    "176Lu/177Hf; 176Hf/177Hf; common-Hf-corrected single-spot age (Ma); Lu-Hf isochron age (Ma); Lu-Hf weighted-mean age (Ma); Lu concentration; Hf concentration \u2014 single-spot ages from eqn (11); isochron and weighted-mean ages in IsoplotR; Lu and Hf concentrations from Iolite's 'Trace_Element' DRS"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "N \u2014 not described; \u00a72.1 gives only the origin of the megacrysts and single crystals, and the acknowledgements credit sample preparation without stating a method",
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
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 3,
        "ada:detectionLimitMethod": "missing"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "ada:ablationSamplingMode": [
    "all: Single hole drilling, two cleaning pulses \u2014 Table 1 'Sampling mode/pattern'"
  ],
  "ada:ablationSpotDurationDefault": "25 s",
  "ada:uncertaintyLevel": "2SE for single-spot ages; uncertainties on weighted-mean ages quoted at 2s",
  "ada:oxideProductionMethodAndThreshold": "ThO/Th < 0.5%, checked during SQ no-gas tuning",
  "ada:blankBackgroundCorrectionMethod": "Gas-blank-corrected intensities calculated in Iolite v.3.7 from time-resolved intensities",
  "ada:secondaryReferenceMaterialDefault": [
    "ARM-1; MG-1, BS-1, XENOA, M1567; Otter Lake, NW-1, MAP-3 \u2014 ARM-1 'is used for the quality control' of Lu and Hf concentrations; the xenotime and apatite U\u2013Pb reference materials test the Lu\u2013Hf ages against their ID-TIMS U\u2013Pb ages"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:analysisSequenceDefault": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:internalStandardApproach": "missing",
  "ada:internalStandardElement": "missing",
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnitSelectionCriteriaDefault": "missing",
  "ada:signalIntegrationIntervalMethod": "missing",
  "schema:datePublished": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:laQicpmsTAPP-P6> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
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
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "N — not described; §2.1 gives only the origin of the megacrysts and single crystals, and the acknowledgements credit sample preparation without stating a method" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/collisionReactionGasMixtureRatioDefault>,
        <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/reactionProductIonMassShiftTransition>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRateDefault> ;
    schema1:datePublished "missing" ;
    schema1:description "laQicpmsTAPP instance derived from Wu+etal2023 | Analyte G2 + iCAP TQ ICP-MS/MS | IGGCAS (publication column of LA-Q-ICP-MS_TAPP_v96.csv). Reported detail: ada:signalCollectionMode = Peak jump." ;
    schema1:instrument <ex:instrument/ICPMS>,
        <ex:instrument/Laser-Ablation-System> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Institute of Geology and Geophysics, Chinese Academy of Sciences (IGGCAS)" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "LA-ICP-MS/MS (LA-Q-ICP-MS, triple-quadrupole platform)" ] ;
    schema1:name "laQicpms protocol — P6" ;
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:ablationPitDepthRateDefault "missing" ;
    ada:ablationSamplingMode "all: Single hole drilling, two cleaning pulses — Table 1 'Sampling mode/pattern'" ;
    ada:ablationSpotDurationDefault "25 s" ;
    ada:analysisSequenceDefault "missing" ;
    ada:backgroundCountTimeDefault "N — gas-blank correction applied in Iolite, duration not stated" ;
    ada:blankBackgroundCorrectionMethod "Gas-blank-corrected intensities calculated in Iolite v.3.7 from time-resolved intensities" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:carrierGasFlowRateDefault "He ablation gas 900 mL/min; Ar carrier gas 0.65 L/min — Table 1 'Ablation gas flow (He)' and 'Carrier gas flow (Ar)'" ;
    ada:constantsAndReferenceValuesUsedDefault "NIST SRM 610 recommended values 176Lu/177Hf = 0.1379 +/- 0.0050 and 176Hf/177Hf = 0.282111 +/- 0.000009, as determined by ID-MC-ICP-MS; 176Lu/175Lu = 0.02655; 176Yb/172Yb = 0.5887; 177Hf/178Hf = 0.682; 176Lu half-life ~37.12 Ga" ;
    ada:internalStandardApproach "missing" ;
    ada:internalStandardElement "missing" ;
    ada:massBiasCorrectionStrategy "missing" ;
    ada:numberOfAcquisitionPasses -9999 ;
    ada:oxideProductionMethodAndThreshold "ThO/Th < 0.5%, checked during SQ no-gas tuning" ;
    ada:rasterLineSpacingDefault "missing" ;
    ada:reportedProperties "176Lu/177Hf; 176Hf/177Hf; common-Hf-corrected single-spot age (Ma); Lu-Hf isochron age (Ma); Lu-Hf weighted-mean age (Ma); Lu concentration; Hf concentration — single-spot ages from eqn (11); isochron and weighted-mean ages in IsoplotR; Lu and Hf concentrations from Iolite's 'Trace_Element' DRS" ;
    ada:sampleIntroduction "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "missing" ;
    ada:samplingUnitType "Laser spot — 246 spot analyses on XN02 alone; spot diameters 50-150 um depending on Lu and Hf contents" ;
    ada:secondaryReferenceMaterialDefault "ARM-1; MG-1, BS-1, XENOA, M1567; Otter Lake, NW-1, MAP-3 — ARM-1 'is used for the quality control' of Lu and Hf concentrations; the xenotime and apatite U–Pb reference materials test the Lu–Hf ages against their ID-TIMS U–Pb ages" ;
    ada:signalCollectionMode "N/A" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "apatite",
                "garnet",
                "xenotime" ;
            ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/laQicpmsTAPP/primaryCalibrationStandardName> ] ;
    ada:targetSpeciesTemplate [ ada:defaultTargetSpecies "Hf",
                "Lu" ;
            ada:targetSpeciesColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetSpecies" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/calibrationStrategyPerTargetSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/monitoredMasses>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/spectralInterferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ] ;
    ada:totalIntegrationTimePerOutputDataPointDefault "0.659 s" ;
    ada:uncertaintyLevel "2SE for single-spot ages; uncertainties on weighted-mean ages quoted at 2s" ;
    bios:computationalTool [ schema1:name "Iolite v.3.7 for gas-blank-corrected intensities, raw ratios and uncertainties; an in-house Microsoft Excel spreadsheet for drift, elemental fractionation and matrix-induced bias; IsoplotR for isochron and weighted-mean ages" ;
            ada:toolRole "dataReduction" ] .

<ex:instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuningDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SingleCollector/detectorConfiguration> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Triple quadrupole (ICP-MS/MS) — operated in both single-quadrupole (SQ) and triple-quadrupole (TQ) modes" ;
    schema1:hasPart <ex:instrument/ICPMS/part/Collision-Reaction-Cell>,
        <ex:instrument/ICPMS/part/ICP-Source>,
        <ex:instrument/ICPMS/part/Interface-Cone>,
        <ex:instrument/ICPMS/part/Torch> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Thermo Fisher Scientific" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "iCap TQ ICP-MS/MS (Thermo Fisher Scientific, Bremen, Germany)" ] ;
    schema1:name "example instrumentName" .

<ex:instrument/ICPMS/part/Collision-Reaction-Cell> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/CollisionCell/cellExitDiscriminationVoltageDefault>,
        <https://ada.astromat.org/metadata/parameter/module/CollisionCell/reactionGasType> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Collision Reaction Cell" ;
    schema1:name "all: TQ mode with NH3 reaction gas, the first quadrupole at 1 amu — tuning first in SQ no-gas mode; 'To avoid interference from 175Lu reaction products ... the required prefiltered mass resolution is 1 amu' (§3.1)" .

<ex:instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPowerDefault> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICP Source" ;
    schema1:name "missing" .

<ex:instrument/ICPMS/part/Interface-Cone> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/configuration>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/samplerAndSkimmerConeMaterial> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Interface Cone" ;
    schema1:name "missing" .

<ex:instrument/ICPMS/part/Torch> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Torch" ;
    schema1:name "missing" .

<ex:instrument/Laser-Ablation-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/LaserAblation/laserPulseDuration> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Laser Ablation System" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Photon Machines Analyte G2 (Teledyne CETAC, Omaha, USA)" ] ;
    schema1:name "HelEx ablation cell" ;
    ada:laserFluenceDefault "4 J cm-2" ;
    ada:laserRepetitionRateDefault "all: 10 Hz — Table 1" ;
    ada:laserSpotGeometryDefault "all: 50, 90, 150 µm — Table 1 'Spot size'; chosen according to Lu and Hf contents" ;
    ada:laserType "193 nm" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/collisionReactionGasMixtureRatioDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "all: high-purity NH3 — found more effective than the commonly used 1:9 NH3-He mixture; He pre-mixed with NH3 was tested for the effect of mixture composition" ;
    schema1:name "Collision/Reaction Gas Mixture Ratio" ;
    schema1:valueName "collisionReactionGasMixtureRatioDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/CollisionCell/cellExitDiscriminationVoltageDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue -4e+01 ;
    schema1:description "CR exit lens -40.00 V (cell bias -4.200 V, CR amplitude 189.3 V, CR entry lens -144.0 V also tabulated)" ;
    schema1:name "Cell Exit Discrimination Voltage" ;
    schema1:valueName "cellExitDiscriminationVoltageDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/CollisionCell/reactionGasType> a schema1:PropertyValueSpecification ;
    schema1:name "Reaction Gas Type" ;
    schema1:value "all: NH3, high purity (>99.999%) — supplied in T4; He (>99.999%, T1) was pre-mixed with NH3 before the cell in a test of mixture composition" ;
    schema1:valueName "reactionGasType" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 8e-01 ;
    schema1:description "0.80 L min-1 Ar" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:valueName "auxiliaryGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/configuration> a schema1:PropertyValueSpecification ;
    schema1:name "Configuration" ;
    schema1:value "High sensitivity sample and skimmer cones" ;
    schema1:valueName "configuration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1.5e+01 ;
    schema1:description "15.00 L min-1 Ar" ;
    schema1:name "Coolant Plasma Gas Flow Rate" ;
    schema1:valueName "coolantPlasmaGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Two-stage: first optimised in solution single-quadrupole and no-gas modes to tune for a robust plasma (U/Th = 1.00-1.05) and minimise oxides (ThO/Th < 0.5%); then switched to TQ and NH3 mode, with lenses tuned to maximise sensitivity for Hf reaction products while keeping Lu and Yb reaction rates low" ;
    schema1:name "ICP Tuning" ;
    schema1:valueName "icpTuningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 2 ;
    schema1:description "N2 enhancement gas, 4.0 mL min-1, added to the carrier gas after the sample chamber to enhance sensitivity; an 80% sensitivity improvement is reported" ;
    schema1:name "Make-up Gas and Flow Rate" ;
    schema1:valueName "makeUpGasAndFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "~300" ;
    schema1:name "Mass Resolution Setting" ;
    schema1:valueName "massResolutionSettingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1350 ;
    schema1:description "1350 W" ;
    schema1:name "RF Power" ;
    schema1:valueName "rfPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/samplerAndSkimmerConeMaterial> a schema1:PropertyValueSpecification ;
    schema1:name "Sampler and Skimmer Cone Material" ;
    schema1:value "N — 'high sensitivity' cones specified, material not stated" ;
    schema1:valueName "samplerAndSkimmerConeMaterial" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/laserPulseDuration> a schema1:PropertyValueSpecification ;
    schema1:name "Laser Pulse Duration" ;
    schema1:value "4-5 ns" ;
    schema1:valueName "laserPulseDuration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SingleCollector/detectorConfiguration> a schema1:PropertyValueSpecification ;
    schema1:name "Detector Configuration" ;
    schema1:value "Single SEM in double mode, counting and analog" ;
    schema1:valueName "detectorConfiguration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/targetMaterialColumn/laQicpmsTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/calibrationStrategyPerTargetSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Calibration Strategy per Target Species" ;
    schema1:valueName "calibrationStrategyPerTargetSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Internal (Within-Measurement) Analytical Precision and Assessment Method" ;
    schema1:valueName "internalAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/monitoredMasses> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Monitored Masses" ;
    schema1:valueName "monitoredMasses" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/spectralInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Spectral Interference Corrections Applied" ;
    schema1:valueName "spectralInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/reactionProductIonMassShiftTransition> a schema1:PropertyValue ;
    schema1:name "Reaction Product Ion / Mass-Shift Transition" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/reactionProductIonMassShiftTransition> ;
    schema1:value "(172+82)Yb, (175+82)Lu, (176+82)Hf, (177+82)Hf, (178+82)Hf: ammonia cluster adduct, mass shift +82; other: N — (176+82)Hf = 176Hf(14N1H)(14N1H2)3(14N1H3)3; Lu, Yb and Hf reaction products identified over 175–300 amu" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: LA-Q-ICP-MS Technique-Aligned Procedure Profile (laQicpmsTAPP)
description: Laser-ablation quadrupole ICP-MS extension of the base TAPP definition,
  generated from tapp/Current TAPPs/LA-Q-ICP-MS_TAPP_v96.csv via the path-driven pipeline
  (bootstrap_schemapaths.py + build_pathdriven.py).
allOf:
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/calibrationFactor/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/targetSpecies/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/compositionQC/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/collisionCell/schema.yaml#/$defs/ProcedureIdentification
- type: object
  properties:
    ada:targetMaterialTemplate:
      type: object
      properties:
        ada:defaultTargetMaterials:
          type: array
          items:
            anyOf:
            - type: string
            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/DefinedTerm
            - type: object
        ada:targetMaterialColumns:
          type: array
          items:
            anyOf:
            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/TargetMaterialIdentifierColumn
            - title: Primary Calibration Standard Name
              description: "Name and reference material identifier of the primary
                reference material(s) against which the instrument is calibrated \u2014
                converting raw signal intensities to concentrations, or anchoring
                an isotope ratio as the bracketing standard or zero-delta reference.
                Give the material name, its source or supplier, and a citation for
                the accepted values used. Where calibration instead uses the vendor's
                stored library or theoretical response factors rather than measured
                reference materials \u2014 'standardless' or 'semi-quantitative' quantification
                \u2014 record that here, naming the library or model used. 'None'
                means no calibration was performed at all, which is a different answer."
              type: object
              properties:
                '@id':
                  const: ada:targetMaterialColumn/laQicpmsTAPP/primaryCalibrationStandardName
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: primaryCalibrationStandardName
                schema:name:
                  const: Primary Calibration Standard Name
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
              title: Primary Calibration Standard Name
              description: "Name and reference material identifier of the primary
                reference material(s) against which the instrument is calibrated \u2014
                converting raw signal intensities to concentrations, or anchoring
                an isotope ratio as the bracketing standard or zero-delta reference.
                Give the material name, its source or supplier, and a citation for
                the accepted values used. Where calibration instead uses the vendor's
                stored library or theoretical response factors rather than measured
                reference materials \u2014 'standardless' or 'semi-quantitative' quantification
                \u2014 record that here, naming the library or model used. 'None'
                means no calibration was performed at all, which is a different answer."
              type: object
              properties:
                '@id':
                  const: ada:targetMaterialColumn/laQicpmsTAPP/primaryCalibrationStandardName
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: primaryCalibrationStandardName
                schema:name:
                  const: Primary Calibration Standard Name
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
      - ada:defaultTargetMaterials
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
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Procedure_signalSmoothing
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_filteringApproach
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/singleCollector/schema.yaml#/$defs/Param_Procedure_pulseAnalogDetectorNonlinearityCorrection
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_isotopeDilutionDataReductionMethod
                      - title: Analysis Inclusion and Rejection Criteria
                        description: 'The rules determining which individual results
                          contribute to a combined result, together with the outcome
                          of applying them: how many results were obtained, how many
                          were included, and on what grounds any were excluded. An
                          individual result is the value of the reported quantity
                          obtained from one acquisition: a replicate measurement of
                          the same solution or location, a spot or grain within a
                          sample, or an independently prepared aliquot or digestion,
                          whichever the procedure combines. Distinct from filtering
                          the acquired signal during data reduction (removing spikes,
                          cycles or scans, or discarding an acquisition whose signal
                          is compromised): this field records which finished results
                          enter the combined result, and on what grounds.'
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/laQicpmsTAPP/analysisInclusionAndRejectionCriteria
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/laQicpmsTAPP/analysisInclusionAndRejectionCriteria
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
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/singleCollector/schema.yaml#/$defs/Param_Procedure_pulseAnalogDetectorNonlinearityCorrection
                      minContains: 0
                      maxContains: 1
                    - contains:
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Procedure_isotopeDilutionDataReductionMethod
                      minContains: 0
                      maxContains: 1
                    - contains:
                        title: Analysis Inclusion and Rejection Criteria
                        description: 'The rules determining which individual results
                          contribute to a combined result, together with the outcome
                          of applying them: how many results were obtained, how many
                          were included, and on what grounds any were excluded. An
                          individual result is the value of the reported quantity
                          obtained from one acquisition: a replicate measurement of
                          the same solution or location, a spot or grain within a
                          sample, or an independently prepared aliquot or digestion,
                          whichever the procedure combines. Distinct from filtering
                          the acquired signal during data reduction (removing spikes,
                          cycles or scans, or discarding an acquisition whose signal
                          is compromised): this field records which finished results
                          enter the combined result, and on what grounds.'
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/laQicpmsTAPP/analysisInclusionAndRejectionCriteria
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/laQicpmsTAPP/analysisInclusionAndRejectionCriteria
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
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Procedure_matrixOffsetCorrectionLief
        - title: Collision/Reaction Gas Mixture Ratio
          description: Where the collision or reaction cell is supplied with a mixture
            of gases rather than a single gas, the identities and proportions of that
            mixture. Recorded separately from the gas identity. Record 'N/A' where
            a single gas is used.
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsTAPP/collisionReactionGasMixtureRatioDefault
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
              const: ada:parameter/laQicpmsTAPP/reactionProductIonMassShiftTransition
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laQicpmsTAPP/reactionProductIonMassShiftTransition
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
        - title: Inter-Pass Data Dependency
          description: "Which earlier acquisition pass supplied inputs to this one,
            and what those inputs are \u2014 for example a concentration measured
            in one pass and used as the internal standard for a later pass on the
            same location. Records the dependency only; the settings of each pass
            are carried by the fields keyed by acquisition pass, and the passes themselves
            are enumerated by Acquisition Pass. Leave empty for a pass that consumes
            no earlier output. Not applicable to raster mapping, where each spatial
            location is visited exactly once."
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsTAPP/interPassDataDependency
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laQicpmsTAPP/interPassDataDependency
            schema:name:
              const: Inter-Pass Data Dependency
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
          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Procedure_matrixOffsetCorrectionLief
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
              const: ada:parameter/laQicpmsTAPP/collisionReactionGasMixtureRatioDefault
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
              const: ada:parameter/laQicpmsTAPP/reactionProductIonMassShiftTransition
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laQicpmsTAPP/reactionProductIonMassShiftTransition
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
      - contains:
          title: Inter-Pass Data Dependency
          description: "Which earlier acquisition pass supplied inputs to this one,
            and what those inputs are \u2014 for example a concentration measured
            in one pass and used as the internal standard for a later pass on the
            same location. Records the dependency only; the settings of each pass
            are carried by the fields keyed by acquisition pass, and the passes themselves
            are enumerated by Acquisition Pass. Leave empty for a pass that consumes
            no earlier output. Not applicable to raster mapping, where each spatial
            location is visited exactly once."
          type: object
          properties:
            '@id':
              const: ada:parameter/laQicpmsTAPP/interPassDataDependency
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laQicpmsTAPP/interPassDataDependency
            schema:name:
              const: Inter-Pass Data Dependency
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
                  - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/singleCollector/schema.yaml#/$defs/Param_Procedure_detectorConfiguration
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
                      The acceptable threshold is typically <1% or <3%. Record both
                      the threshold and the measured value.
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
                    $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/singleCollector/schema.yaml#/$defs/Param_Procedure_detectorConfiguration
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
                      The acceptable threshold is typically <1% or <3%. Record both
                      the threshold and the measured value.
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
    ada:targetSpeciesTemplate:
      type: object
      properties:
        ada:defaultTargetSpecies:
          type: array
          items:
            anyOf:
            - type: string
            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/DefinedTerm
            - type: object
        ada:targetSpeciesColumns:
          type: array
          items:
            anyOf:
            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/TargetSpeciesIdentifierColumn
            - title: Monitored Masses
              description: Specific masses monitored in this procedure, grouped by
                the target species element they serve where they serve one. Covers
                atomic isotopes and, where a reaction cell shifts an target species
                onto a different mass, the product mass actually measured. Includes
                interference-monitor and internal-standard masses, which serve no
                target species and so have no parent element. The target species list
                is given by the Target Species field and is never inferred from the
                element symbols appearing here.
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/laQicpmsTAPP/monitoredMasses
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
                  const: ada:targetSpeciesColumn/laQicpmsTAPP/dwellTimePerMass
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
                  const: ada:targetSpeciesColumn/laQicpmsTAPP/calibrationStrategyPerTargetSpecies
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
            - title: Spectral Interference Corrections Applied
              description: Whether mathematical corrections for isobaric, polyatomic
                or residual interferences are applied in data reduction, supplementary
                to any suppression already achieved by chemical separation, mass resolution,
                or a collision/reaction cell. Detail for each affected mass is carried
                by Interfering Species and Interference Correction Method.
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/laQicpmsTAPP/spectralInterferenceCorrectionsApplied
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
                  const: ada:targetSpeciesColumn/laQicpmsTAPP/interferingSpecies
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
                  const: ada:targetSpeciesColumn/laQicpmsTAPP/interferenceCorrectionMethod
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
                  const: ada:targetSpeciesColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod
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
                  const: ada:targetSpeciesColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod
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
                  const: ada:targetSpeciesColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod
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
                  const: ada:targetSpeciesColumn/laQicpmsTAPP/countingStatisticsError
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
                  const: ada:targetSpeciesColumn/laQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod
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
          allOf:
          - contains:
              title: Monitored Masses
              description: Specific masses monitored in this procedure, grouped by
                the target species element they serve where they serve one. Covers
                atomic isotopes and, where a reaction cell shifts an target species
                onto a different mass, the product mass actually measured. Includes
                interference-monitor and internal-standard masses, which serve no
                target species and so have no parent element. The target species list
                is given by the Target Species field and is never inferred from the
                element symbols appearing here.
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/laQicpmsTAPP/monitoredMasses
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
                  const: ada:targetSpeciesColumn/laQicpmsTAPP/dwellTimePerMass
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
                  const: ada:targetSpeciesColumn/laQicpmsTAPP/calibrationStrategyPerTargetSpecies
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
              title: Spectral Interference Corrections Applied
              description: Whether mathematical corrections for isobaric, polyatomic
                or residual interferences are applied in data reduction, supplementary
                to any suppression already achieved by chemical separation, mass resolution,
                or a collision/reaction cell. Detail for each affected mass is carried
                by Interfering Species and Interference Correction Method.
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/laQicpmsTAPP/spectralInterferenceCorrectionsApplied
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
                  const: ada:targetSpeciesColumn/laQicpmsTAPP/interferingSpecies
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
                  const: ada:targetSpeciesColumn/laQicpmsTAPP/interferenceCorrectionMethod
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
                  const: ada:targetSpeciesColumn/laQicpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod
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
                  const: ada:targetSpeciesColumn/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod
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
                  const: ada:targetSpeciesColumn/laQicpmsTAPP/analyticalAccuracyAndAssessmentMethod
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
                  const: ada:targetSpeciesColumn/laQicpmsTAPP/countingStatisticsError
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
                  const: ada:targetSpeciesColumn/laQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod
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
      required:
      - ada:defaultTargetSpecies
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
    ada:totalIntegrationTimePerOutputDataPointDefault:
      description: "Total duty-cycle time for one complete mass-scan sweep \u2014
        the sum of all per-isotope dwell times plus inter-mass settling times. Not
        recoverable from Dwell Time per Mass alone, because settling time is not captured
        there. Applies to sequential (quadrupole and single-collector sector-field)
        acquisition."
      anyOf:
      - type: number
      - type: string
    ada:massBiasCorrectionStrategy:
      description: 'Strategy used to correct instrumental isotopic mass fractionation,
        also called mass bias or mass discrimination. Distinct from Elemental Fractionation
        Correction, which addresses inter-element fractionation during ablation and
        transport: this field addresses discrimination between isotopes of the same
        element, and applies wherever the procedure reports isotope ratios.'
      type: string
      readOnly: true
    ada:constantsAndReferenceValuesUsedDefault:
      description: Physical constants and reference values used in data reduction
        to calculate the final reported quantity (e.g., decay constants for age calculation,
        standard isotope ratios, or other citable reference values used in a correction
        or calculation), together with their source. Distinct from the Group 6 reference-material
        fields, which document accepted values for specific calibration/validation
        materials rather than universal physical constants. Record "None" if no citable,
        revisable physical constants feed into this procedure's data reduction.
      type: string
    ada:numberOfAcquisitionPasses:
      description: Number of acquisition passes the procedure runs. A count of the
        passes enumerated in Acquisition Pass, recorded separately so multi-pass procedures
        are findable without parsing that field.
      anyOf:
      - type: integer
      - type: string
      readOnly: true
    ada:analyticalMode:
      type: array
      items:
        type: string
        enum:
        - Spot
        - Transect
        - Mapping
  required:
  - ada:signalCollectionMode
  - ada:totalIntegrationTimePerOutputDataPointDefault
  - ada:massBiasCorrectionStrategy
  - ada:constantsAndReferenceValuesUsedDefault
  - ada:numberOfAcquisitionPasses

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
    "nxs": "https://manual.nexusformat.org/classes/",
    "dqv": "http://www.w3.org/ns/dqv#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "wd": "https://www.wikidata.org/entity/",
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

