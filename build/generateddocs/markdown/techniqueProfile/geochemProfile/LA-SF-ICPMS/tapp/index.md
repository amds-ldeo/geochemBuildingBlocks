
# LA-SF-ICP-MS Technique-Aligned Procedure Profile (laSficpmsTAPP) (Schema)

`ogch.techniqueProfile.geochemProfile.LA-SF-ICPMS.tapp` *v0.1*

Laser-ablation sector-field (high-resolution) ICP-MS extension of the base TAPP definition, generated from TAPPS20260813/Current TAPPs/LA-SF-ICP-MS_TAPP_v16.csv via the path-driven pipeline.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### laSficpmsTAPP example Zhang2022
laSficpmsTAPP instance derived from Zhang et al. 2022 (GCA 323) Iron meteorites Raster mapping + Spot (Ge) ns-LA-SF-ICP-MS Florida State University.
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
  "@id": "ex:laSficpmsTAPP-Zhang2022",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Zhang et al. (2022) Iron Meteorite LA-ICP-MS v1",
  "schema:description": "The raster pass gives the 23-element dataset; a separate set of 150 µm spots on five irons gives more precise Ge, since the raster 'failed to yield useful Ge abundances for Klamath Falls' (§2.2)",
  "ada:targetMaterialTemplate": {
    "ada:targetMaterialDeclaration": "Iron meteorite metal (kamacite + taenite); pyroxene-bearing pallasite metal",
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
        "@id": "ada:targetMaterialColumn/laSficpmsTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "Representativeness of the exsolution banding — the raster \"yielded more representative sampling of the kamacite-taenite banding\", and where it \"failed to yield useful Ge abundances for Klamath Falls ... To obtain more precise Ge, a set of five 150 μm spots were analyzed ... on five of the irons\" (p.4)",
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
      "schema:defaultValue": "Electron-microprobe mapping, for the pallasites only — \"Quantitative analysis, mixed WDS/EDS element mapping, and characterization of the mineral phases from NWA 1911 and Zinder were performed\" on the Bruker instrument, producing Si, Al, Cr, Fe, Mg, Ca, Na, P and Ni maps \"along with backscattered electron (BSE) maps\" at 6 μm per pixel (pp.5–6); for the irons the paper states only that the rasters were \"taken on polished surfaces\" (p.5)"
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
      "schema:defaultValue": "raster: 10 µm/s; Ge spots: N/A — 'scanned at 10 µm/s' (§2.2)"
    },
    {
      "@id": "ada:parameter/laSficpmsTAPP/interPassDataDependency",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsTAPP/interPassDataDependency"
        }
      ],
      "schema:name": "Inter-Pass Data Dependency",
      "schema:value": "N — the Ge value combines both passes (Combination Method), but no pass uses another's data"
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
        "schema:name": "Thermo Fisher Scientific Element XR (SF-ICP-MS)",
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
          "schema:defaultValue": "Low resolution (M/ΔM ≈ 400)"
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
          "schema:value": "Triple mode detection at 65% duty cycle — 'triple mode detection at 65% duty cycle' (§2.2)"
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
        "schema:name": "ElectroScientific Instruments New Wave UP193FX — §2.2",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserSpotGeometryDefault": "raster: 50 µm beam spot; Ge spots: 150 µm — §2.2",
      "ada:laserRepetitionRateDefault": "raster: 50 Hz; Ge spots: 50 Hz — §2.2",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/Laser-Ablation-System",
      "schema:name": "example instrumentName",
      "ada:laserFluenceDefault": -9999,
      "ada:laserType": "test value ada:laserType"
    }
  ],
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "P",
      "V",
      "Cr",
      "Mn",
      "Fe",
      "Co",
      "Ni",
      "Cu",
      "Ga",
      "Ge",
      "As",
      "Mo",
      "Ru",
      "Rh",
      "Pd",
      "Sn",
      "Sb",
      "W",
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
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
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
        "schema:description": "Polished slabs of the irons; a mount of Zinder and a section of NWA 1911 for the pallasites (§2.1); no acid treatment is described for the LA-ICP-MS specimens",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 1
      },
      {
        "schema:name": "Data acquisition",
        "schema:description": "raster; Ge spots — 'Irons were analyzed using a raster scan over a few millimeters'; 'To obtain more precise Ge, a set of five 150 µm spots were analyzed at 50 Hz for 20 s on five of the irons' (§2.2)",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
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
            "schema:defaultValue": "N — 'triple mode detection at 65% duty cycle' (§2.2); a cross-calibration is not described"
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 3,
        "ada:detectionLimitMethod": "test value ada:detectionLimitMethod"
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
      "schema:termCode": "LA-SF-ICP-MS"
    }
  ],
  "schema:creator": {
    "schema:name": "Zhang, Chabot, Rubin, Humayun et al.",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Plasma Analytical Facility, Florida State University, Tallahassee FL, USA"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Zhang et al. (2022) GCA 323, 202–219; Humayun (2012) for standardization"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "EPMA (Brown University CAMECA SX-100)",
        "schema:description": "Quantitative analysis, mixed WDS/EDS element mapping, and characterization of mineral phases from NWA 1911 and Zinder [Section 2.5]"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Whole sample (polished specimen surface) > Region of interest (raster) — irons \"were analyzed using a raster scan over a few millimeters\" with a 50 μm beam, and compositions are reported as \"raster averages\" per specimen (Table 3, pp.4–5); Ge comes from a set of five 150 μm spots on five of the irons (p.4)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "N — paper only states \"standardization techniques followed those of Humayun (2012)\"; no software named"
    }
  ],
  "ada:reportedProperties": [
    "P, Fe, Co, Ni (mg/g); V, Cr, Mn, Cu, Ga, Ge, As, Mo, Ru, Rh, Pd, Sn, Sb, W, Re, Os, Ir, Pt, Au (µg/g) — abundances in metal, Table 3 (raster averages) with spot averages in Appendix 2; 'Concentrations below detection limits are not shown'"
  ],
  "ada:ablationSamplingMode": [
    "raster: raster scan over a few millimeters; Ge spots: spot — §2.2"
  ],
  "ada:ablationSpotDurationDefault": "20 s for the Ge spots — 'analyzed at 50 Hz for 20 s' (§2.2); the raster duration is not stated",
  "ada:internalStandardApproach": "N — 'Standardization techniques followed those of Humayun (2012)' (§2.2)",
  "ada:elementalFractionationCorrection": [
    "N — 'Standardization techniques followed those of Humayun (2012)' (§2.2); the standards are under Primary Calibration Standard Name"
  ],
  "ada:internalStandardElement": "N — not stated; standardization follows Humayun (2012)",
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "test value schema:defaultValue"
    }
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:analysisSequenceDefault": "missing",
  "ada:backgroundCountTimeDefault": -9999,
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:carrierGasFlowRateDefault": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:massResolutionAssignment": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:laSficpmsTAPP-Zhang2022",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Zhang et al. (2022) Iron Meteorite LA-ICP-MS v1",
  "schema:description": "The raster pass gives the 23-element dataset; a separate set of 150 \u00b5m spots on five irons gives more precise Ge, since the raster 'failed to yield useful Ge abundances for Klamath Falls' (\u00a72.2)",
  "ada:targetMaterialTemplate": {
    "ada:targetMaterialDeclaration": "Iron meteorite metal (kamacite + taenite); pyroxene-bearing pallasite metal",
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
        "@id": "ada:targetMaterialColumn/laSficpmsTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "Representativeness of the exsolution banding \u2014 the raster \"yielded more representative sampling of the kamacite-taenite banding\", and where it \"failed to yield useful Ge abundances for Klamath Falls ... To obtain more precise Ge, a set of five 150 \u03bcm spots were analyzed ... on five of the irons\" (p.4)",
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
      "schema:defaultValue": "Electron-microprobe mapping, for the pallasites only \u2014 \"Quantitative analysis, mixed WDS/EDS element mapping, and characterization of the mineral phases from NWA 1911 and Zinder were performed\" on the Bruker instrument, producing Si, Al, Cr, Fe, Mg, Ca, Na, P and Ni maps \"along with backscattered electron (BSE) maps\" at 6 \u03bcm per pixel (pp.5\u20136); for the irons the paper states only that the rasters were \"taken on polished surfaces\" (p.5)"
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
      "schema:defaultValue": "raster: 10 \u00b5m/s; Ge spots: N/A \u2014 'scanned at 10 \u00b5m/s' (\u00a72.2)"
    },
    {
      "@id": "ada:parameter/laSficpmsTAPP/interPassDataDependency",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsTAPP/interPassDataDependency"
        }
      ],
      "schema:name": "Inter-Pass Data Dependency",
      "schema:value": "N \u2014 the Ge value combines both passes (Combination Method), but no pass uses another's data"
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
        "schema:name": "Thermo Fisher Scientific Element XR (SF-ICP-MS)",
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
          "schema:defaultValue": "Low resolution (M/\u0394M \u2248 400)"
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
          "schema:value": "Triple mode detection at 65% duty cycle \u2014 'triple mode detection at 65% duty cycle' (\u00a72.2)"
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
        "schema:name": "ElectroScientific Instruments New Wave UP193FX \u2014 \u00a72.2",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserSpotGeometryDefault": "raster: 50 \u00b5m beam spot; Ge spots: 150 \u00b5m \u2014 \u00a72.2",
      "ada:laserRepetitionRateDefault": "raster: 50 Hz; Ge spots: 50 Hz \u2014 \u00a72.2",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/Laser-Ablation-System",
      "schema:name": "example instrumentName",
      "ada:laserFluenceDefault": -9999,
      "ada:laserType": "test value ada:laserType"
    }
  ],
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "P",
      "V",
      "Cr",
      "Mn",
      "Fe",
      "Co",
      "Ni",
      "Cu",
      "Ga",
      "Ge",
      "As",
      "Mo",
      "Ru",
      "Rh",
      "Pd",
      "Sn",
      "Sb",
      "W",
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
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
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
        "schema:description": "Polished slabs of the irons; a mount of Zinder and a section of NWA 1911 for the pallasites (\u00a72.1); no acid treatment is described for the LA-ICP-MS specimens",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 1
      },
      {
        "schema:name": "Data acquisition",
        "schema:description": "raster; Ge spots \u2014 'Irons were analyzed using a raster scan over a few millimeters'; 'To obtain more precise Ge, a set of five 150 \u00b5m spots were analyzed at 50 Hz for 20 s on five of the irons' (\u00a72.2)",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
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
            "schema:defaultValue": "N \u2014 'triple mode detection at 65% duty cycle' (\u00a72.2); a cross-calibration is not described"
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 3,
        "ada:detectionLimitMethod": "test value ada:detectionLimitMethod"
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
      "schema:termCode": "LA-SF-ICP-MS"
    }
  ],
  "schema:creator": {
    "schema:name": "Zhang, Chabot, Rubin, Humayun et al.",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Plasma Analytical Facility, Florida State University, Tallahassee FL, USA"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Zhang et al. (2022) GCA 323, 202\u2013219; Humayun (2012) for standardization"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "EPMA (Brown University CAMECA SX-100)",
        "schema:description": "Quantitative analysis, mixed WDS/EDS element mapping, and characterization of mineral phases from NWA 1911 and Zinder [Section 2.5]"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Whole sample (polished specimen surface) > Region of interest (raster) \u2014 irons \"were analyzed using a raster scan over a few millimeters\" with a 50 \u03bcm beam, and compositions are reported as \"raster averages\" per specimen (Table 3, pp.4\u20135); Ge comes from a set of five 150 \u03bcm spots on five of the irons (p.4)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "N \u2014 paper only states \"standardization techniques followed those of Humayun (2012)\"; no software named"
    }
  ],
  "ada:reportedProperties": [
    "P, Fe, Co, Ni (mg/g); V, Cr, Mn, Cu, Ga, Ge, As, Mo, Ru, Rh, Pd, Sn, Sb, W, Re, Os, Ir, Pt, Au (\u00b5g/g) \u2014 abundances in metal, Table 3 (raster averages) with spot averages in Appendix 2; 'Concentrations below detection limits are not shown'"
  ],
  "ada:ablationSamplingMode": [
    "raster: raster scan over a few millimeters; Ge spots: spot \u2014 \u00a72.2"
  ],
  "ada:ablationSpotDurationDefault": "20 s for the Ge spots \u2014 'analyzed at 50 Hz for 20 s' (\u00a72.2); the raster duration is not stated",
  "ada:internalStandardApproach": "N \u2014 'Standardization techniques followed those of Humayun (2012)' (\u00a72.2)",
  "ada:elementalFractionationCorrection": [
    "N \u2014 'Standardization techniques followed those of Humayun (2012)' (\u00a72.2); the standards are under Primary Calibration Standard Name"
  ],
  "ada:internalStandardElement": "N \u2014 not stated; standardization follows Humayun (2012)",
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "test value schema:defaultValue"
    }
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:analysisSequenceDefault": "missing",
  "ada:backgroundCountTimeDefault": -9999,
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:carrierGasFlowRateDefault": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:massResolutionAssignment": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
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

<ex:laSficpmsTAPP-Zhang2022> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:description "Polished slabs of the irons; a mount of Zinder and a section of NWA 1911 for the pallasites (§2.1); no acid treatment is described for the LA-ICP-MS specimens" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:description "raster; Ge spots — 'Irons were analyzed using a raster scan over a few millimeters'; 'To obtain more precise Ge, a set of five 150 µm spots were analyzed at 50 Hz for 20 s on five of the irons' (§2.2)" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrectionDefault> ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ;
                    ada:detectionLimitMethod "test value ada:detectionLimitMethod" ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/interPassDataDependency>,
        <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSizeDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Zhang, Chabot, Rubin, Humayun et al." ] ;
    schema1:datePublished "missing" ;
    schema1:description "The raster pass gives the 23-element dataset; a separate set of 150 µm spots on five irons gives more precise Ge, since the raster 'failed to yield useful Ge abundances for Klamath Falls' (§2.2)" ;
    schema1:instrument <ex:instrument/ICPMS>,
        <ex:instrument/Laser-Ablation-System> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Plasma Analytical Facility, Florida State University, Tallahassee FL, USA" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "LA-SF-ICP-MS" ] ;
    schema1:name "Zhang et al. (2022) Iron Meteorite LA-ICP-MS v1" ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "Quantitative analysis, mixed WDS/EDS element mapping, and characterization of mineral phases from NWA 1911 and Zinder [Section 2.5]" ;
                    schema1:name "EPMA (Brown University CAMECA SX-100)" ] ;
            schema1:url "https://ada.astromat.org/missing" ],
        [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Zhang et al. (2022) GCA 323, 202–219; Humayun (2012) for standardization" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "test value schema:defaultValue" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:ablationPitDepthRateDefault "missing" ;
    ada:ablationSamplingMode "raster: raster scan over a few millimeters; Ge spots: spot — §2.2" ;
    ada:ablationSpotDurationDefault "20 s for the Ge spots — 'analyzed at 50 Hz for 20 s' (§2.2); the raster duration is not stated" ;
    ada:analysisSequenceDefault "missing" ;
    ada:backgroundCountTimeDefault -9999 ;
    ada:blankBackgroundCorrectionMethod "missing" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:carrierGasFlowRateDefault "missing" ;
    ada:constantsAndReferenceValuesUsedDefault "missing" ;
    ada:elementalFractionationCorrection "N — 'Standardization techniques followed those of Humayun (2012)' (§2.2); the standards are under Primary Calibration Standard Name" ;
    ada:internalStandardApproach "N — 'Standardization techniques followed those of Humayun (2012)' (§2.2)" ;
    ada:internalStandardElement "N — not stated; standardization follows Humayun (2012)" ;
    ada:massBiasCorrectionStrategy "missing" ;
    ada:massResolutionAssignment "missing" ;
    ada:numberOfAcquisitionPasses -9999 ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:rasterLineSpacingDefault "missing" ;
    ada:reportedProperties "P, Fe, Co, Ni (mg/g); V, Cr, Mn, Cu, Ga, Ge, As, Mo, Ru, Rh, Pd, Sn, Sb, W, Re, Os, Ir, Pt, Au (µg/g) — abundances in metal, Table 3 (raster averages) with spot averages in Appendix 2; 'Concentrations below detection limits are not shown'" ;
    ada:sampleIntroduction "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "Representativeness of the exsolution banding — the raster \"yielded more representative sampling of the kamacite-taenite banding\", and where it \"failed to yield useful Ge abundances for Klamath Falls ... To obtain more precise Ge, a set of five 150 μm spots were analyzed ... on five of the irons\" (p.4)" ;
    ada:samplingUnitType "Whole sample (polished specimen surface) > Region of interest (raster) — irons \"were analyzed using a raster scan over a few millimeters\" with a 50 μm beam, and compositions are reported as \"raster averages\" per specimen (Table 3, pp.4–5); Ge comes from a set of five 150 μm spots on five of the irons (p.4)" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:targetMaterialTemplate [ ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/laSficpmsTAPP/primaryCalibrationStandardName> ;
            ada:targetMaterialDeclaration "Iron meteorite metal (kamacite + taenite); pyroxene-bearing pallasite metal" ] ;
    ada:targetSpeciesTemplate [ ada:defaultTargetSpecies "As",
                "Au",
                "Co",
                "Cr",
                "Cu",
                "Fe",
                "Ga",
                "Ge",
                "Ir",
                "Mn",
                "Mo",
                "Ni",
                "Os",
                "P",
                "Pd",
                "Pt",
                "Re",
                "Rh",
                "Ru",
                "Sb",
                "Sn",
                "V",
                "W" ;
            ada:targetSpeciesColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetSpecies" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/calibrationStrategyPerTargetSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/massResolutionAssignment>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/monitoredMasses>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/spectralInterferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ] ;
    ada:totalIntegrationTimePerOutputDataPointDefault -9999 ;
    ada:uncertaintyLevel "missing" ;
    bios:computationalTool [ schema1:name "N — paper only states \"standardization techniques followed those of Humayun (2012)\"; no software named" ;
            ada:toolRole "dataReduction" ] .

<ex:instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SingleCollector/detectorConfiguration> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS" ;
    schema1:hasPart <ex:instrument/ICPMS/part/ICP-Source>,
        <ex:instrument/ICPMS/part/Interface-Cone>,
        <ex:instrument/ICPMS/part/Torch> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "missing" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Thermo Fisher Scientific Element XR (SF-ICP-MS)" ] ;
    schema1:name "example instrumentName" .

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
            schema1:name "ElectroScientific Instruments New Wave UP193FX — §2.2" ] ;
    schema1:name "example instrumentName" ;
    ada:laserFluenceDefault -9999 ;
    ada:laserRepetitionRateDefault "raster: 50 Hz; Ge spots: 50 Hz — §2.2" ;
    ada:laserSpotGeometryDefault "raster: 50 µm beam spot; Ge spots: 150 µm — §2.2" ;
    ada:laserType "test value ada:laserType" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Low resolution (M/ΔM ≈ 400)" ;
    schema1:name "Mass Resolution Setting" ;
    schema1:valueName "massResolutionSettingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSizeDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "raster: 10 µm/s; Ge spots: N/A — 'scanned at 10 µm/s' (§2.2)" ;
    schema1:name "Transect Rate Mapping Rate or Step Size" ;
    schema1:valueName "transectRateMappingRateOrStepSizeDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Electron-microprobe mapping, for the pallasites only — \"Quantitative analysis, mixed WDS/EDS element mapping, and characterization of the mineral phases from NWA 1911 and Zinder were performed\" on the Bruker instrument, producing Si, Al, Cr, Fe, Mg, Ca, Na, P and Ni maps \"along with backscattered electron (BSE) maps\" at 6 μm per pixel (pp.5–6); for the irons the paper states only that the rasters were \"taken on polished surfaces\" (p.5)" ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:valueName "preAnalysisImagingAndScreeningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SingleCollector/detectorConfiguration> a schema1:PropertyValueSpecification ;
    schema1:name "Detector Configuration" ;
    schema1:value "Triple mode detection at 65% duty cycle — 'triple mode detection at 65% duty cycle' (§2.2)" ;
    schema1:valueName "detectorConfiguration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrectionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N — 'triple mode detection at 65% duty cycle' (§2.2); a cross-calibration is not described" ;
    schema1:name "Pulse Analog Detector Nonlinearity Correction" ;
    schema1:valueName "pulseAnalogDetectorNonlinearityCorrectionDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/targetMaterialColumn/laSficpmsTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/calibrationStrategyPerTargetSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Calibration Strategy per Target Species" ;
    schema1:valueName "calibrationStrategyPerTargetSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Internal (Within-Measurement) Analytical Precision and Assessment Method" ;
    schema1:valueName "internalAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/massResolutionAssignment> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Mass Resolution Assignment" ;
    schema1:valueName "massResolutionAssignment" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/monitoredMasses> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Monitored Masses" ;
    schema1:valueName "monitoredMasses" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/spectralInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Spectral Interference Corrections Applied" ;
    schema1:valueName "spectralInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/interPassDataDependency> a schema1:PropertyValue ;
    schema1:name "Inter-Pass Data Dependency" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/interPassDataDependency> ;
    schema1:value "N — the Ge value combines both passes (Combination Method), but no pass uses another's data" .


```


### laSficpmsTAPP example Chernonozhkin2021
laSficpmsTAPP instance derived from Chernonozhkin et al. 2021 (Chem Geol 562) Pallasite olivine Raster mapping (2D) ns-LA-SF-ICP-MS Ghent University.
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
  "@id": "ex:laSficpmsTAPP-Chernonozhkin2021",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Chernonozhkin et al. (2021) Pallasite Olivine 2D Mapping v1",
  "schema:description": "Cool plasma (800 W) mapping with a lateral resolution of approximately 20 µm; P-rich veinlets masked before averaging (§2.2.2, §3.1)",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "Pallasite olivine"
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
        "@id": "ada:targetMaterialColumn/laSficpmsTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "Position relative to the metal-olivine rim, sited on a prior μXRF survey — \"The locations for LA-ICP-MS mapping were selected to be close to the metal-olivine rims of large olivine crystals with the laser beam rastering from the olivine rim in the direction of the olivine core\", at locations \"indicated on the larger μXRF maps as black rectangles\" (p.4)",
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
      "schema:defaultValue": "μXRF mapping of larger sections, on which the ablation is sited — Fe Kα intensity maps identify the mineral phases \"based on the intensities of the Kα lines of the constituent major elements (Fe, Mg, Ni, Cr, S, Ca and P)\", and the LA-ICP-MS areas correspond \"to the locations indicated on the larger μXRF maps as black rectangles\" (p.4). The instrument is a Bruker M4 Tornado with a Rh-anode source at 50 kV and 150 μA, focused to \"a 25 μm spot (measured for Mo Kα)\" (p.3)"
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
      "schema:defaultValue": "all: 9 µm/s — translation speed (§2.2.2)"
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
      "schema:defaultValue": 0.81,
      "schema:description": "Ar, 0.81–0.99 L/min — Table B1; 'No N2 was blent into ICP to avoid elevated nitrogen-based spectral interferences'"
    },
    {
      "@id": "ada:parameter/laSficpmsTAPP/interPassDataDependency",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsTAPP/interPassDataDependency"
        }
      ],
      "schema:name": "Inter-Pass Data Dependency",
      "schema:value": "N/A — a single pass"
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Double-focusing sector field ICP-MS (explicitly stated: \"Thermo Scientific Element XR double-focusing sector field ICP-MS unit\")",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Thermo Fisher Scientific Element XR (SF-ICP-MS)",
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
              "schema:value": "Al standard sample cone (1.1 mm aperture); Al H-type skimmer (0.8 mm aperture)"
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
              "schema:defaultValue": 15,
              "schema:description": "Ar, 15 L/min — Table B1"
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
              "schema:defaultValue": 0.81,
              "schema:description": "Ar, 0.81 L/min — Table B1"
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
              "schema:defaultValue": 800,
              "schema:description": "800 W — cool plasma (§2.2.2, Table B1)"
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
              "schema:value": "all: cool plasma (800 W RF) — 'Cool plasma conditions (800 W RF power) were used to reduce Ar-based interferences and to increase the sensitivity of the analysis' (§2.2.2)"
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
          "@id": "ada:parameter/module/ICPMS/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Low (M/ΔM = 300) — §2.2.2"
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
          "schema:value": "Triple — Table B1 'Detection mode'"
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
          "schema:defaultValue": "N — oxide-based interferences 'were further minimized during tuning' (App. C4); no tuning procedure is described"
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
          "schema:defaultValue": "Washout typically less than 1 s — §2.2.2"
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
          "@id": "ada:parameter/module/LaserAblation/laserBeamEnergyProfile",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "laserBeamEnergyProfile",
          "schema:name": "Laser Beam Energy Profile",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:value": "Flat-topped — 'The laser beam is characterized by a flat-topped energy profile' (§2.2.2)"
        },
        {
          "@id": "ada:parameter/module/LaserAblation/laserPulseDuration",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "laserPulseDuration",
          "schema:name": "Laser Pulse Duration",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:value": "4 ns — Table B1; §2.2.2 says '<5 ns'"
        }
      ],
      "schema:model": {
        "schema:name": "Teledyne CETAC Technologies Analyte G2 (193 nm ArF excimer)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "193 nm ArF* excimer — §2.2.2",
      "schema:name": "HELEX II two-volume ablation cell",
      "ada:laserSpotGeometryDefault": "all: 20 µm × 20 µm square-masked — §2.2.2",
      "ada:laserFluenceDefault": "5–7 J cm⁻²",
      "ada:laserRepetitionRateDefault": "all: 20 Hz",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/Laser-Ablation-System"
    }
  ],
  "ada:carrierGasFlowRateDefault": "He: MFC-1 (cell) 0.200–0.260 l min⁻¹; MFC-2 (cup) 0.220–0.385 l min⁻¹",
  "ada:analysisSequenceDefault": "N — the glasses were 'measured in the same analytical session' (§2.1); the sequence is not described",
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Mg",
      "Al",
      "Si",
      "P",
      "Sc",
      "V",
      "Cr",
      "Mn",
      "Fe",
      "Ni",
      "Ga",
      "La",
      "Eu",
      "Pt"
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
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:massResolutionAssignment": "all: low resolution (M/ΔM = 300) — Table B1",
  "ada:backgroundCountTimeDefault": "10 gas-blank scans before each line, 80 during ablation — Table B1",
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Flat polished thick sections (§2.1)",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 1
      },
      {
        "schema:name": "Data acquisition",
        "schema:description": "map — a single pass: 'The laser scanned a grid of parallel, adjacent lines' (§2.2.2)",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
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
            "schema:defaultValue": "P-rich veinlet pixels masked: P2O5 above the best-fitting Gaussian of each map's P2O5 histogram plus 3 standard deviations — §3.1; 'A MATLAB script was applied to mask pixels representing veinlets'"
          },
          {
            "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "pulseAnalogDetectorNonlinearityCorrectionDefault",
            "schema:name": "Pulse Analog Detector Nonlinearity Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "N — 'Triple' detection (Table B1); a cross-calibration is not described"
          }
        ],
        "ada:detectionLimitMethod": "all: Longerich et al. (1996), LOD = 3SD/S × √(1/Nb + 1/Na) — Na = 1 and Nb = 10 for a pixel (App. C5)",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
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
      "schema:termCode": "LA-SF-ICP-MS"
    }
  ],
  "schema:creator": {
    "schema:name": "Chernonozhkin, Pittarello, Goderis, Vanhaecke et al.",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Dept. of Chemistry, Atomic & Mass Spectrometry, Ghent University, Belgium"
  },
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "N — the BELSPO, FWO, BOF-UGent and Humboldt support is for the study as a whole and is recorded under Funding Source for Analysis"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Chernonozhkin et al. (2021) Chem. Geol. 562; Liu et al. (2008) for IS method"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Grain (individual olivine crystal) > Region of interest (2D map) — \"2D trace element mapping of olivine crystals\" (p.1); the reported dataset is \"seven 2D element maps of PMG olivine crystals\", filtered and median-smoothed before analysis (p.6)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "In-house MatLab script (Appendix C1)"
    }
  ],
  "ada:reportedProperties": [
    "Mg, Al, Si, P, Sc, V, Cr, Mn, Fe, Ni, Ga, La, Eu, Pt (concentration maps, µg/g); Fa#; principal-component scores — '2D concentration matrices of all target elements'; pure-olivine averages in Table E1"
  ],
  "ada:ablationSamplingMode": [
    "all: grid of parallel, adjacent lines — §2.2.2; the grid runs 'from the metal-olivine margin to the olivine cores'"
  ],
  "ada:ablationSpotDurationDefault": "N/A — mapping mode",
  "ada:rasterLineSpacingDefault": "Adjacent lines — 'a grid of parallel, adjacent lines using a 20 µm × 20 µm square-masked laser spot' (§2.2.2)",
  "ada:internalStandardApproach": "all: sum normalization of MgO, FeO, SiO2 and P2O5 to 100 wt% in each pixel (Liu et al., 2008) — the oxide sum is a 'virtual, evenly distributed IS' (App. C1, equations 1–2)",
  "ada:calibrationMeasurementFrequency": "N — the glasses were 'measured in the same analytical session' (§2.1)",
  "ada:blankBackgroundCorrectionMethod": "Gas blank before each string of pixels; the average background preceding each analysis subtracted — App. C5",
  "ada:internalStandardElement": "all: none — a virtual internal standard from the oxide sum (App. C1)",
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "test value schema:defaultValue"
    }
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:sampleIntroduction": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:laSficpmsTAPP-Chernonozhkin2021",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Chernonozhkin et al. (2021) Pallasite Olivine 2D Mapping v1",
  "schema:description": "Cool plasma (800 W) mapping with a lateral resolution of approximately 20 \u00b5m; P-rich veinlets masked before averaging (\u00a72.2.2, \u00a73.1)",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "Pallasite olivine"
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
        "@id": "ada:targetMaterialColumn/laSficpmsTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "Position relative to the metal-olivine rim, sited on a prior \u03bcXRF survey \u2014 \"The locations for LA-ICP-MS mapping were selected to be close to the metal-olivine rims of large olivine crystals with the laser beam rastering from the olivine rim in the direction of the olivine core\", at locations \"indicated on the larger \u03bcXRF maps as black rectangles\" (p.4)",
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
      "schema:defaultValue": "\u03bcXRF mapping of larger sections, on which the ablation is sited \u2014 Fe K\u03b1 intensity maps identify the mineral phases \"based on the intensities of the K\u03b1 lines of the constituent major elements (Fe, Mg, Ni, Cr, S, Ca and P)\", and the LA-ICP-MS areas correspond \"to the locations indicated on the larger \u03bcXRF maps as black rectangles\" (p.4). The instrument is a Bruker M4 Tornado with a Rh-anode source at 50 kV and 150 \u03bcA, focused to \"a 25 \u03bcm spot (measured for Mo K\u03b1)\" (p.3)"
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
      "schema:defaultValue": "all: 9 \u00b5m/s \u2014 translation speed (\u00a72.2.2)"
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
      "schema:defaultValue": 0.81,
      "schema:description": "Ar, 0.81\u20130.99 L/min \u2014 Table B1; 'No N2 was blent into ICP to avoid elevated nitrogen-based spectral interferences'"
    },
    {
      "@id": "ada:parameter/laSficpmsTAPP/interPassDataDependency",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsTAPP/interPassDataDependency"
        }
      ],
      "schema:name": "Inter-Pass Data Dependency",
      "schema:value": "N/A \u2014 a single pass"
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Double-focusing sector field ICP-MS (explicitly stated: \"Thermo Scientific Element XR double-focusing sector field ICP-MS unit\")",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Thermo Fisher Scientific Element XR (SF-ICP-MS)",
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
              "schema:value": "Al standard sample cone (1.1 mm aperture); Al H-type skimmer (0.8 mm aperture)"
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
              "schema:defaultValue": 15,
              "schema:description": "Ar, 15 L/min \u2014 Table B1"
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
              "schema:defaultValue": 0.81,
              "schema:description": "Ar, 0.81 L/min \u2014 Table B1"
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
              "schema:defaultValue": 800,
              "schema:description": "800 W \u2014 cool plasma (\u00a72.2.2, Table B1)"
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
              "schema:value": "all: cool plasma (800 W RF) \u2014 'Cool plasma conditions (800 W RF power) were used to reduce Ar-based interferences and to increase the sensitivity of the analysis' (\u00a72.2.2)"
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
          "@id": "ada:parameter/module/ICPMS/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Low (M/\u0394M = 300) \u2014 \u00a72.2.2"
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
          "schema:value": "Triple \u2014 Table B1 'Detection mode'"
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
          "schema:defaultValue": "N \u2014 oxide-based interferences 'were further minimized during tuning' (App. C4); no tuning procedure is described"
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
          "schema:defaultValue": "Washout typically less than 1 s \u2014 \u00a72.2.2"
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
          "@id": "ada:parameter/module/LaserAblation/laserBeamEnergyProfile",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "laserBeamEnergyProfile",
          "schema:name": "Laser Beam Energy Profile",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:value": "Flat-topped \u2014 'The laser beam is characterized by a flat-topped energy profile' (\u00a72.2.2)"
        },
        {
          "@id": "ada:parameter/module/LaserAblation/laserPulseDuration",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "laserPulseDuration",
          "schema:name": "Laser Pulse Duration",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:value": "4 ns \u2014 Table B1; \u00a72.2.2 says '<5 ns'"
        }
      ],
      "schema:model": {
        "schema:name": "Teledyne CETAC Technologies Analyte G2 (193 nm ArF excimer)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "193 nm ArF* excimer \u2014 \u00a72.2.2",
      "schema:name": "HELEX II two-volume ablation cell",
      "ada:laserSpotGeometryDefault": "all: 20 \u00b5m \u00d7 20 \u00b5m square-masked \u2014 \u00a72.2.2",
      "ada:laserFluenceDefault": "5\u20137 J cm\u207b\u00b2",
      "ada:laserRepetitionRateDefault": "all: 20 Hz",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/Laser-Ablation-System"
    }
  ],
  "ada:carrierGasFlowRateDefault": "He: MFC-1 (cell) 0.200\u20130.260 l min\u207b\u00b9; MFC-2 (cup) 0.220\u20130.385 l min\u207b\u00b9",
  "ada:analysisSequenceDefault": "N \u2014 the glasses were 'measured in the same analytical session' (\u00a72.1); the sequence is not described",
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Mg",
      "Al",
      "Si",
      "P",
      "Sc",
      "V",
      "Cr",
      "Mn",
      "Fe",
      "Ni",
      "Ga",
      "La",
      "Eu",
      "Pt"
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
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:massResolutionAssignment": "all: low resolution (M/\u0394M = 300) \u2014 Table B1",
  "ada:backgroundCountTimeDefault": "10 gas-blank scans before each line, 80 during ablation \u2014 Table B1",
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Flat polished thick sections (\u00a72.1)",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 1
      },
      {
        "schema:name": "Data acquisition",
        "schema:description": "map \u2014 a single pass: 'The laser scanned a grid of parallel, adjacent lines' (\u00a72.2.2)",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
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
            "schema:defaultValue": "P-rich veinlet pixels masked: P2O5 above the best-fitting Gaussian of each map's P2O5 histogram plus 3 standard deviations \u2014 \u00a73.1; 'A MATLAB script was applied to mask pixels representing veinlets'"
          },
          {
            "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "pulseAnalogDetectorNonlinearityCorrectionDefault",
            "schema:name": "Pulse Analog Detector Nonlinearity Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "N \u2014 'Triple' detection (Table B1); a cross-calibration is not described"
          }
        ],
        "ada:detectionLimitMethod": "all: Longerich et al. (1996), LOD = 3SD/S \u00d7 \u221a(1/Nb + 1/Na) \u2014 Na = 1 and Nb = 10 for a pixel (App. C5)",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
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
      "schema:termCode": "LA-SF-ICP-MS"
    }
  ],
  "schema:creator": {
    "schema:name": "Chernonozhkin, Pittarello, Goderis, Vanhaecke et al.",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Dept. of Chemistry, Atomic & Mass Spectrometry, Ghent University, Belgium"
  },
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "N \u2014 the BELSPO, FWO, BOF-UGent and Humboldt support is for the study as a whole and is recorded under Funding Source for Analysis"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Chernonozhkin et al. (2021) Chem. Geol. 562; Liu et al. (2008) for IS method"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Grain (individual olivine crystal) > Region of interest (2D map) \u2014 \"2D trace element mapping of olivine crystals\" (p.1); the reported dataset is \"seven 2D element maps of PMG olivine crystals\", filtered and median-smoothed before analysis (p.6)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "In-house MatLab script (Appendix C1)"
    }
  ],
  "ada:reportedProperties": [
    "Mg, Al, Si, P, Sc, V, Cr, Mn, Fe, Ni, Ga, La, Eu, Pt (concentration maps, \u00b5g/g); Fa#; principal-component scores \u2014 '2D concentration matrices of all target elements'; pure-olivine averages in Table E1"
  ],
  "ada:ablationSamplingMode": [
    "all: grid of parallel, adjacent lines \u2014 \u00a72.2.2; the grid runs 'from the metal-olivine margin to the olivine cores'"
  ],
  "ada:ablationSpotDurationDefault": "N/A \u2014 mapping mode",
  "ada:rasterLineSpacingDefault": "Adjacent lines \u2014 'a grid of parallel, adjacent lines using a 20 \u00b5m \u00d7 20 \u00b5m square-masked laser spot' (\u00a72.2.2)",
  "ada:internalStandardApproach": "all: sum normalization of MgO, FeO, SiO2 and P2O5 to 100 wt% in each pixel (Liu et al., 2008) \u2014 the oxide sum is a 'virtual, evenly distributed IS' (App. C1, equations 1\u20132)",
  "ada:calibrationMeasurementFrequency": "N \u2014 the glasses were 'measured in the same analytical session' (\u00a72.1)",
  "ada:blankBackgroundCorrectionMethod": "Gas blank before each string of pixels; the average background preceding each analysis subtracted \u2014 App. C5",
  "ada:internalStandardElement": "all: none \u2014 a virtual internal standard from the oxide sum (App. C1)",
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "test value schema:defaultValue"
    }
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:sampleIntroduction": "missing",
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

<ex:laSficpmsTAPP-Chernonozhkin2021> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:description "Flat polished thick sections (§2.1)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:description "map — a single pass: 'The laser scanned a grid of parallel, adjacent lines' (§2.2.2)" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproachDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrectionDefault> ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ;
                    ada:detectionLimitMethod "all: Longerich et al. (1996), LOD = 3SD/S × √(1/Nb + 1/Na) — Na = 1 and Nb = 10 for a pixel (App. C5)" ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/interPassDataDependency>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSizeDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Chernonozhkin, Pittarello, Goderis, Vanhaecke et al." ] ;
    schema1:datePublished "missing" ;
    schema1:description "Cool plasma (800 W) mapping with a lateral resolution of approximately 20 µm; P-rich veinlets masked before averaging (§2.2.2, §3.1)" ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "N — the BELSPO, FWO, BOF-UGent and Humboldt support is for the study as a whole and is recorded under Funding Source for Analysis" ] ;
    schema1:instrument <ex:instrument/ICPMS>,
        <ex:instrument/Laser-Ablation-System> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Dept. of Chemistry, Atomic & Mass Spectrometry, Ghent University, Belgium" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "LA-SF-ICP-MS" ] ;
    schema1:name "Chernonozhkin et al. (2021) Pallasite Olivine 2D Mapping v1" ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Chernonozhkin et al. (2021) Chem. Geol. 562; Liu et al. (2008) for IS method" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "test value schema:defaultValue" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:ablationPitDepthRateDefault "missing" ;
    ada:ablationSamplingMode "all: grid of parallel, adjacent lines — §2.2.2; the grid runs 'from the metal-olivine margin to the olivine cores'" ;
    ada:ablationSpotDurationDefault "N/A — mapping mode" ;
    ada:analysisSequenceDefault "N — the glasses were 'measured in the same analytical session' (§2.1); the sequence is not described" ;
    ada:backgroundCountTimeDefault "10 gas-blank scans before each line, 80 during ablation — Table B1" ;
    ada:blankBackgroundCorrectionMethod "Gas blank before each string of pixels; the average background preceding each analysis subtracted — App. C5" ;
    ada:calibrationMeasurementFrequency "N — the glasses were 'measured in the same analytical session' (§2.1)" ;
    ada:carrierGasFlowRateDefault "He: MFC-1 (cell) 0.200–0.260 l min⁻¹; MFC-2 (cup) 0.220–0.385 l min⁻¹" ;
    ada:constantsAndReferenceValuesUsedDefault "missing" ;
    ada:internalStandardApproach "all: sum normalization of MgO, FeO, SiO2 and P2O5 to 100 wt% in each pixel (Liu et al., 2008) — the oxide sum is a 'virtual, evenly distributed IS' (App. C1, equations 1–2)" ;
    ada:internalStandardElement "all: none — a virtual internal standard from the oxide sum (App. C1)" ;
    ada:massBiasCorrectionStrategy "missing" ;
    ada:massResolutionAssignment "all: low resolution (M/ΔM = 300) — Table B1" ;
    ada:numberOfAcquisitionPasses -9999 ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:rasterLineSpacingDefault "Adjacent lines — 'a grid of parallel, adjacent lines using a 20 µm × 20 µm square-masked laser spot' (§2.2.2)" ;
    ada:reportedProperties "Mg, Al, Si, P, Sc, V, Cr, Mn, Fe, Ni, Ga, La, Eu, Pt (concentration maps, µg/g); Fa#; principal-component scores — '2D concentration matrices of all target elements'; pure-olivine averages in Table E1" ;
    ada:sampleIntroduction "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "Position relative to the metal-olivine rim, sited on a prior μXRF survey — \"The locations for LA-ICP-MS mapping were selected to be close to the metal-olivine rims of large olivine crystals with the laser beam rastering from the olivine rim in the direction of the olivine core\", at locations \"indicated on the larger μXRF maps as black rectangles\" (p.4)" ;
    ada:samplingUnitType "Grain (individual olivine crystal) > Region of interest (2D map) — \"2D trace element mapping of olivine crystals\" (p.1); the reported dataset is \"seven 2D element maps of PMG olivine crystals\", filtered and median-smoothed before analysis (p.6)" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "Pallasite olivine" ;
            ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/laSficpmsTAPP/primaryCalibrationStandardName> ] ;
    ada:targetSpeciesTemplate [ ada:defaultTargetSpecies "Al",
                "Cr",
                "Eu",
                "Fe",
                "Ga",
                "La",
                "Mg",
                "Mn",
                "Ni",
                "P",
                "Pt",
                "Sc",
                "Si",
                "V" ;
            ada:targetSpeciesColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetSpecies" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/calibrationStrategyPerTargetSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/massResolutionAssignment>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/monitoredMasses>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/spectralInterferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ] ;
    ada:totalIntegrationTimePerOutputDataPointDefault -9999 ;
    ada:uncertaintyLevel "missing" ;
    bios:computationalTool [ schema1:name "In-house MatLab script (Appendix C1)" ;
            ada:toolRole "dataReduction" ] .

<ex:instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuningDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigationDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SingleCollector/detectorConfiguration> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Double-focusing sector field ICP-MS (explicitly stated: \"Thermo Scientific Element XR double-focusing sector field ICP-MS unit\")",
        "ICPMS" ;
    schema1:hasPart <ex:instrument/ICPMS/part/ICP-Source>,
        <ex:instrument/ICPMS/part/Interface-Cone>,
        <ex:instrument/ICPMS/part/Torch> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "missing" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Thermo Fisher Scientific Element XR (SF-ICP-MS)" ] ;
    schema1:name "example instrumentName" .

<ex:instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/plasmaThermalMode>,
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
    schema1:name "missing" .

<ex:instrument/Laser-Ablation-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/LaserAblation/laserBeamEnergyProfile>,
        <https://ada.astromat.org/metadata/parameter/module/LaserAblation/laserPulseDuration> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Laser Ablation System" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Teledyne CETAC Technologies Analyte G2 (193 nm ArF excimer)" ] ;
    schema1:name "HELEX II two-volume ablation cell" ;
    ada:laserFluenceDefault "5–7 J cm⁻²" ;
    ada:laserRepetitionRateDefault "all: 20 Hz" ;
    ada:laserSpotGeometryDefault "all: 20 µm × 20 µm square-masked — §2.2.2" ;
    ada:laserType "193 nm ArF* excimer — §2.2.2" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 8.1e-01 ;
    schema1:description "Ar, 0.81 L/min — Table B1" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:valueName "auxiliaryGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/configuration> a schema1:PropertyValueSpecification ;
    schema1:name "Configuration" ;
    schema1:value "Al standard sample cone (1.1 mm aperture); Al H-type skimmer (0.8 mm aperture)" ;
    schema1:valueName "configuration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 15 ;
    schema1:description "Ar, 15 L/min — Table B1" ;
    schema1:name "Coolant Plasma Gas Flow Rate" ;
    schema1:valueName "coolantPlasmaGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproachDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "P-rich veinlet pixels masked: P2O5 above the best-fitting Gaussian of each map's P2O5 histogram plus 3 standard deviations — §3.1; 'A MATLAB script was applied to mask pixels representing veinlets'" ;
    schema1:name "Filtering Approach" ;
    schema1:valueName "filteringApproachDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N — oxide-based interferences 'were further minimized during tuning' (App. C4); no tuning procedure is described" ;
    schema1:name "ICP Tuning" ;
    schema1:valueName "icpTuningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 8.1e-01 ;
    schema1:description "Ar, 0.81–0.99 L/min — Table B1; 'No N2 was blent into ICP to avoid elevated nitrogen-based spectral interferences'" ;
    schema1:name "Make-up Gas and Flow Rate" ;
    schema1:valueName "makeUpGasAndFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Low (M/ΔM = 300) — §2.2.2" ;
    schema1:name "Mass Resolution Setting" ;
    schema1:valueName "massResolutionSettingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Washout typically less than 1 s — §2.2.2" ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:valueName "memoryEffectMitigationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/plasmaThermalMode> a schema1:PropertyValueSpecification ;
    schema1:name "Plasma Thermal Mode" ;
    schema1:value "all: cool plasma (800 W RF) — 'Cool plasma conditions (800 W RF power) were used to reduce Ar-based interferences and to increase the sensitivity of the analysis' (§2.2.2)" ;
    schema1:valueName "plasmaThermalMode" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 800 ;
    schema1:description "800 W — cool plasma (§2.2.2, Table B1)" ;
    schema1:name "RF Power" ;
    schema1:valueName "rfPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/laserBeamEnergyProfile> a schema1:PropertyValueSpecification ;
    schema1:name "Laser Beam Energy Profile" ;
    schema1:value "Flat-topped — 'The laser beam is characterized by a flat-topped energy profile' (§2.2.2)" ;
    schema1:valueName "laserBeamEnergyProfile" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/laserPulseDuration> a schema1:PropertyValueSpecification ;
    schema1:name "Laser Pulse Duration" ;
    schema1:value "4 ns — Table B1; §2.2.2 says '<5 ns'" ;
    schema1:valueName "laserPulseDuration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSizeDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "all: 9 µm/s — translation speed (§2.2.2)" ;
    schema1:name "Transect Rate Mapping Rate or Step Size" ;
    schema1:valueName "transectRateMappingRateOrStepSizeDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "μXRF mapping of larger sections, on which the ablation is sited — Fe Kα intensity maps identify the mineral phases \"based on the intensities of the Kα lines of the constituent major elements (Fe, Mg, Ni, Cr, S, Ca and P)\", and the LA-ICP-MS areas correspond \"to the locations indicated on the larger μXRF maps as black rectangles\" (p.4). The instrument is a Bruker M4 Tornado with a Rh-anode source at 50 kV and 150 μA, focused to \"a 25 μm spot (measured for Mo Kα)\" (p.3)" ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:valueName "preAnalysisImagingAndScreeningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SingleCollector/detectorConfiguration> a schema1:PropertyValueSpecification ;
    schema1:name "Detector Configuration" ;
    schema1:value "Triple — Table B1 'Detection mode'" ;
    schema1:valueName "detectorConfiguration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrectionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N — 'Triple' detection (Table B1); a cross-calibration is not described" ;
    schema1:name "Pulse Analog Detector Nonlinearity Correction" ;
    schema1:valueName "pulseAnalogDetectorNonlinearityCorrectionDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/targetMaterialColumn/laSficpmsTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/calibrationStrategyPerTargetSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Calibration Strategy per Target Species" ;
    schema1:valueName "calibrationStrategyPerTargetSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Internal (Within-Measurement) Analytical Precision and Assessment Method" ;
    schema1:valueName "internalAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/massResolutionAssignment> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Mass Resolution Assignment" ;
    schema1:valueName "massResolutionAssignment" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/monitoredMasses> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Monitored Masses" ;
    schema1:valueName "monitoredMasses" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/spectralInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Spectral Interference Corrections Applied" ;
    schema1:valueName "spectralInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/interPassDataDependency> a schema1:PropertyValue ;
    schema1:name "Inter-Pass Data Dependency" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/interPassDataDependency> ;
    schema1:value "N/A — a single pass" .


```


### laSficpmsTAPP example Chernonozhkin2021-2
laSficpmsTAPP instance derived from Chernonozhkin et al. 2021 (Chem Geol 562) Pallasite olivine Line scan (Run 1: major) + Spot (Run 2: trace) [Multi-run] ns-LA-SF-ICP-MS Ghent University.
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
  "@id": "ex:laSficpmsTAPP-Chernonozhkin2021-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Chernonozhkin et al. (2021) Pallasite Olivine Multi-run Spot/Transect v1",
  "schema:description": "Two line-scan runs on the same line after pre-ablation: run 1 (30 µm, medium resolution) gives the major elements and Cr, which normalises run 2 (130 µm, low resolution) for the trace elements (§2.2.3, App. C2)",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "Pallasite olivine"
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
        "@id": "ada:targetMaterialColumn/laSficpmsTAPP/primaryCalibrationStandardName",
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
            "@id": "ada:parameter/module/LaserAblation/preAblationSurfaceTreatmentDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "preAblationSurfaceTreatmentDefault",
            "schema:name": "Pre Ablation Surface Treatment",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Pre-ablation before each analysis: 2 J/cm², 20 Hz, 150 µm square-masked spot, 300 µm/s — 'to avoid bias in the trace element concentrations due to re-deposition of ablated sample material after previous analyses' (§2.2.3)"
          }
        ],
        "schema:description": "Flat polished thick sections (§2.1)",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 1
      },
      {
        "schema:name": "Data acquisition",
        "schema:description": "run 1 (major elements); run 2 (trace elements) — two line-scans on the same 400 µm line, each after pre-ablation; 'Every analysis was carried out 3 times' (§2.2.3)",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
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
            "schema:defaultValue": "Surface-impurity spikes removed with a 3 sigma filter; results with significant spikes not included in Table 1; Pb and U not presented because of multiple spikes — §3.3"
          },
          {
            "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "pulseAnalogDetectorNonlinearityCorrectionDefault",
            "schema:name": "Pulse Analog Detector Nonlinearity Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "N — 'Triple' detection (Table B1); at the 130 µm spot, major elements saturate the detector 'even when using the triple detection mode' (App. C2)"
          }
        ],
        "ada:detectionLimitMethod": "all: Longerich et al. (1996), LOD = 3SD/S × √(1/Nb + 1/Na) — Na = 24 and Nb = 5 (App. C5)",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 3
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "ada:samplingUnitSelectionCriteriaDefault": "Position relative to the metal-olivine rim — the line scans run \"from the olivine rim in the direction of the olivine core\" on large olivine crystals sited from the μXRF maps (p.4); the surface is pre-ablated before each analysis (p.3)",
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
      "schema:defaultValue": "μXRF mapping of larger sections, on which the ablation is sited — Fe Kα intensity maps identify the mineral phases \"based on the intensities of the Kα lines of the constituent major elements (Fe, Mg, Ni, Cr, S, Ca and P)\", and the LA-ICP-MS areas correspond \"to the locations indicated on the larger μXRF maps as black rectangles\" (p.4). The instrument is a Bruker M4 Tornado with a Rh-anode source at 50 kV and 150 μA, focused to \"a 25 μm spot (measured for Mo Kα)\" (p.3)"
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
      "schema:defaultValue": "run 1: 10 µm/s; run 2: 10 µm/s"
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
      "schema:defaultValue": 0.947,
      "schema:description": "Ar, 0.947 L/min (both runs) — Table B1; no N2 added"
    },
    {
      "@id": "ada:parameter/laSficpmsTAPP/interPassDataDependency",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsTAPP/interPassDataDependency"
        }
      ],
      "schema:name": "Inter-Pass Data Dependency",
      "schema:value": "run 1: N/A; run 2: normalised to the Cr concentration from run 1 — 'The Cr concentrations calculated from this run were then used for internal standardization to normalize the data of the second, trace element run' (§2.2.3)"
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Double-focusing sector field ICP-MS (explicitly stated)",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Thermo Fisher Scientific Element XR (SF-ICP-MS)",
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
              "schema:value": "Al standard sample cone (1.1 mm aperture); Al H-type skimmer (0.8 mm aperture)"
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
              "schema:defaultValue": 15,
              "schema:description": "Ar, 15 L/min — Table B1"
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
              "schema:defaultValue": 0.9,
              "schema:description": "Ar, 0.90 L/min — Table B1"
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
              "schema:defaultValue": 1000,
              "schema:description": "1000 W (run 1 major elements + run 2 trace elements)"
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
              "schema:value": "N — RF power 1000 W for both runs (Table B1); only the mapping is described as cool plasma"
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
          "@id": "ada:parameter/module/ICPMS/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "run 1: medium (M/ΔM = 4000); run 2: low (M/ΔM = 300) — §2.2.3"
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
          "schema:value": "Triple — Table B1 'Detection mode'"
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
          "schema:defaultValue": "11 s of washout per run — Table B1"
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
          "schema:value": "4 ns — Table B1; §2.2.2 says '<5 ns'"
        }
      ],
      "schema:model": {
        "schema:name": "Teledyne CETAC Technologies Analyte G2 (193 nm ArF excimer)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "193 nm ArF* excimer — §2.2.2",
      "schema:name": "HELEX II two-volume ablation cell",
      "ada:laserSpotGeometryDefault": "run 1: 30 µm diameter circular-masked; run 2: 130 µm diameter — §2.2.3",
      "ada:laserFluenceDefault": "4.72 J/cm² (both runs) — §2.2.3",
      "ada:laserRepetitionRateDefault": "run 1: 20 Hz; run 2: 40 Hz",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/Laser-Ablation-System"
    }
  ],
  "ada:carrierGasFlowRateDefault": "He: MFC-1 0.19 l min⁻¹; MFC-2 0.22 l min⁻¹",
  "ada:analysisSequenceDefault": "MPI-DING and USGS reference materials at the start and end of each analytical session; every analysis carried out 3 times — §2.2.3",
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Mg",
      "Si",
      "P",
      "Ca",
      "Cr",
      "Mn",
      "Fe",
      "Li",
      "Sc",
      "V",
      "Co",
      "Ni",
      "Cu",
      "Zn",
      "Y",
      "Zr",
      "Nb",
      "Cs",
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
      "Re",
      "Ir",
      "Pt",
      "Au",
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
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:massResolutionAssignment": "run 1: medium resolution (M/ΔM = 4000); run 2: low resolution (M/ΔM = 300) — §2.2.3",
  "ada:backgroundCountTimeDefault": "5 gas-blank scans and 24 ablation scans per analysis, both runs; 10 s of blank per run — Table B1",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-SF-ICP-MS"
    }
  ],
  "schema:creator": {
    "schema:name": "Chernonozhkin, Pittarello, Goderis, Vanhaecke et al.",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Dept. of Chemistry, Atomic & Mass Spectrometry, Ghent University, Belgium"
  },
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "N — the BELSPO, FWO, BOF-UGent and Humboldt support is for the study as a whole and is recorded under Funding Source for Analysis"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Chernonozhkin et al. (2021) Chem. Geol. 562; Liu et al. (2008) for IS method"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Grain (individual olivine crystal) > Region of interest (line scan) — \"a second line-scan was completed on top of the first one, using a laser spot of 130 μm diameter ... and a translation speed of 10 μm s−1\" (p.3)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "In-house MatLab script (Appendix C2)"
    }
  ],
  "ada:reportedProperties": [
    "Mg, Si, P, Ca, Cr, Mn, Fe, Li, Sc, V, Co, Ni, Cu, Zn, Y, Zr, Nb, Cs, Ba, La, Ce, Pr, Nd, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu, Hf, Ta, W, Re, Ir, Pt, Au, Th, U (µg/g); Fa# — Table 1, 'the average from 3 replicate measurements'"
  ],
  "ada:ablationSamplingMode": [
    "run 1: line scan, 400 µm; run 2: line scan on top of run 1, 400 µm — 'a second line-scan was completed on top of the first one' (§2.2.3)"
  ],
  "ada:ablationSpotDurationDefault": "50 s of sample ablation per 400 µm line, both runs — Table B1",
  "ada:rasterLineSpacingDefault": "N/A — line scan + spot; not 2D mapping",
  "ada:internalStandardApproach": "run 1: sum normalization of the oxides to 100 wt% (Liu et al., 2008); run 2: single element from run 1 — §2.2.3, App. C2",
  "ada:calibrationMeasurementFrequency": "Start and end of each analytical session — 'MPI-DING and USGS reference materials were measured at the start and end of each analytical session' (§2.2.3)",
  "ada:blankBackgroundCorrectionMethod": "Gas blank before each line analysis; the average background preceding each analysis subtracted — App. C5",
  "ada:internalStandardElement": "run 1: none (oxide sum); run 2: Cr (concentration from run 1) — §2.2.3",
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "test value schema:defaultValue"
    }
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:sampleIntroduction": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:laSficpmsTAPP-Chernonozhkin2021-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Chernonozhkin et al. (2021) Pallasite Olivine Multi-run Spot/Transect v1",
  "schema:description": "Two line-scan runs on the same line after pre-ablation: run 1 (30 \u00b5m, medium resolution) gives the major elements and Cr, which normalises run 2 (130 \u00b5m, low resolution) for the trace elements (\u00a72.2.3, App. C2)",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "Pallasite olivine"
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
        "@id": "ada:targetMaterialColumn/laSficpmsTAPP/primaryCalibrationStandardName",
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
            "@id": "ada:parameter/module/LaserAblation/preAblationSurfaceTreatmentDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "preAblationSurfaceTreatmentDefault",
            "schema:name": "Pre Ablation Surface Treatment",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Pre-ablation before each analysis: 2 J/cm\u00b2, 20 Hz, 150 \u00b5m square-masked spot, 300 \u00b5m/s \u2014 'to avoid bias in the trace element concentrations due to re-deposition of ablated sample material after previous analyses' (\u00a72.2.3)"
          }
        ],
        "schema:description": "Flat polished thick sections (\u00a72.1)",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 1
      },
      {
        "schema:name": "Data acquisition",
        "schema:description": "run 1 (major elements); run 2 (trace elements) \u2014 two line-scans on the same 400 \u00b5m line, each after pre-ablation; 'Every analysis was carried out 3 times' (\u00a72.2.3)",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
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
            "schema:defaultValue": "Surface-impurity spikes removed with a 3 sigma filter; results with significant spikes not included in Table 1; Pb and U not presented because of multiple spikes \u2014 \u00a73.3"
          },
          {
            "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "pulseAnalogDetectorNonlinearityCorrectionDefault",
            "schema:name": "Pulse Analog Detector Nonlinearity Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "N \u2014 'Triple' detection (Table B1); at the 130 \u00b5m spot, major elements saturate the detector 'even when using the triple detection mode' (App. C2)"
          }
        ],
        "ada:detectionLimitMethod": "all: Longerich et al. (1996), LOD = 3SD/S \u00d7 \u221a(1/Nb + 1/Na) \u2014 Na = 24 and Nb = 5 (App. C5)",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 3
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "ada:samplingUnitSelectionCriteriaDefault": "Position relative to the metal-olivine rim \u2014 the line scans run \"from the olivine rim in the direction of the olivine core\" on large olivine crystals sited from the \u03bcXRF maps (p.4); the surface is pre-ablated before each analysis (p.3)",
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
      "schema:defaultValue": "\u03bcXRF mapping of larger sections, on which the ablation is sited \u2014 Fe K\u03b1 intensity maps identify the mineral phases \"based on the intensities of the K\u03b1 lines of the constituent major elements (Fe, Mg, Ni, Cr, S, Ca and P)\", and the LA-ICP-MS areas correspond \"to the locations indicated on the larger \u03bcXRF maps as black rectangles\" (p.4). The instrument is a Bruker M4 Tornado with a Rh-anode source at 50 kV and 150 \u03bcA, focused to \"a 25 \u03bcm spot (measured for Mo K\u03b1)\" (p.3)"
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
      "schema:defaultValue": "run 1: 10 \u00b5m/s; run 2: 10 \u00b5m/s"
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
      "schema:defaultValue": 0.947,
      "schema:description": "Ar, 0.947 L/min (both runs) \u2014 Table B1; no N2 added"
    },
    {
      "@id": "ada:parameter/laSficpmsTAPP/interPassDataDependency",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsTAPP/interPassDataDependency"
        }
      ],
      "schema:name": "Inter-Pass Data Dependency",
      "schema:value": "run 1: N/A; run 2: normalised to the Cr concentration from run 1 \u2014 'The Cr concentrations calculated from this run were then used for internal standardization to normalize the data of the second, trace element run' (\u00a72.2.3)"
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Double-focusing sector field ICP-MS (explicitly stated)",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Thermo Fisher Scientific Element XR (SF-ICP-MS)",
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
              "schema:value": "Al standard sample cone (1.1 mm aperture); Al H-type skimmer (0.8 mm aperture)"
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
              "schema:defaultValue": 15,
              "schema:description": "Ar, 15 L/min \u2014 Table B1"
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
              "schema:defaultValue": 0.9,
              "schema:description": "Ar, 0.90 L/min \u2014 Table B1"
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
              "schema:defaultValue": 1000,
              "schema:description": "1000 W (run 1 major elements + run 2 trace elements)"
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
              "schema:value": "N \u2014 RF power 1000 W for both runs (Table B1); only the mapping is described as cool plasma"
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
          "@id": "ada:parameter/module/ICPMS/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "run 1: medium (M/\u0394M = 4000); run 2: low (M/\u0394M = 300) \u2014 \u00a72.2.3"
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
          "schema:value": "Triple \u2014 Table B1 'Detection mode'"
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
          "schema:defaultValue": "11 s of washout per run \u2014 Table B1"
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
          "schema:value": "4 ns \u2014 Table B1; \u00a72.2.2 says '<5 ns'"
        }
      ],
      "schema:model": {
        "schema:name": "Teledyne CETAC Technologies Analyte G2 (193 nm ArF excimer)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "193 nm ArF* excimer \u2014 \u00a72.2.2",
      "schema:name": "HELEX II two-volume ablation cell",
      "ada:laserSpotGeometryDefault": "run 1: 30 \u00b5m diameter circular-masked; run 2: 130 \u00b5m diameter \u2014 \u00a72.2.3",
      "ada:laserFluenceDefault": "4.72 J/cm\u00b2 (both runs) \u2014 \u00a72.2.3",
      "ada:laserRepetitionRateDefault": "run 1: 20 Hz; run 2: 40 Hz",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/Laser-Ablation-System"
    }
  ],
  "ada:carrierGasFlowRateDefault": "He: MFC-1 0.19 l min\u207b\u00b9; MFC-2 0.22 l min\u207b\u00b9",
  "ada:analysisSequenceDefault": "MPI-DING and USGS reference materials at the start and end of each analytical session; every analysis carried out 3 times \u2014 \u00a72.2.3",
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Mg",
      "Si",
      "P",
      "Ca",
      "Cr",
      "Mn",
      "Fe",
      "Li",
      "Sc",
      "V",
      "Co",
      "Ni",
      "Cu",
      "Zn",
      "Y",
      "Zr",
      "Nb",
      "Cs",
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
      "Re",
      "Ir",
      "Pt",
      "Au",
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
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:massResolutionAssignment": "run 1: medium resolution (M/\u0394M = 4000); run 2: low resolution (M/\u0394M = 300) \u2014 \u00a72.2.3",
  "ada:backgroundCountTimeDefault": "5 gas-blank scans and 24 ablation scans per analysis, both runs; 10 s of blank per run \u2014 Table B1",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-SF-ICP-MS"
    }
  ],
  "schema:creator": {
    "schema:name": "Chernonozhkin, Pittarello, Goderis, Vanhaecke et al.",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Dept. of Chemistry, Atomic & Mass Spectrometry, Ghent University, Belgium"
  },
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "N \u2014 the BELSPO, FWO, BOF-UGent and Humboldt support is for the study as a whole and is recorded under Funding Source for Analysis"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Chernonozhkin et al. (2021) Chem. Geol. 562; Liu et al. (2008) for IS method"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Grain (individual olivine crystal) > Region of interest (line scan) \u2014 \"a second line-scan was completed on top of the first one, using a laser spot of 130 \u03bcm diameter ... and a translation speed of 10 \u03bcm s\u22121\" (p.3)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "In-house MatLab script (Appendix C2)"
    }
  ],
  "ada:reportedProperties": [
    "Mg, Si, P, Ca, Cr, Mn, Fe, Li, Sc, V, Co, Ni, Cu, Zn, Y, Zr, Nb, Cs, Ba, La, Ce, Pr, Nd, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu, Hf, Ta, W, Re, Ir, Pt, Au, Th, U (\u00b5g/g); Fa# \u2014 Table 1, 'the average from 3 replicate measurements'"
  ],
  "ada:ablationSamplingMode": [
    "run 1: line scan, 400 \u00b5m; run 2: line scan on top of run 1, 400 \u00b5m \u2014 'a second line-scan was completed on top of the first one' (\u00a72.2.3)"
  ],
  "ada:ablationSpotDurationDefault": "50 s of sample ablation per 400 \u00b5m line, both runs \u2014 Table B1",
  "ada:rasterLineSpacingDefault": "N/A \u2014 line scan + spot; not 2D mapping",
  "ada:internalStandardApproach": "run 1: sum normalization of the oxides to 100 wt% (Liu et al., 2008); run 2: single element from run 1 \u2014 \u00a72.2.3, App. C2",
  "ada:calibrationMeasurementFrequency": "Start and end of each analytical session \u2014 'MPI-DING and USGS reference materials were measured at the start and end of each analytical session' (\u00a72.2.3)",
  "ada:blankBackgroundCorrectionMethod": "Gas blank before each line analysis; the average background preceding each analysis subtracted \u2014 App. C5",
  "ada:internalStandardElement": "run 1: none (oxide sum); run 2: Cr (concentration from run 1) \u2014 \u00a72.2.3",
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "test value schema:defaultValue"
    }
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:sampleIntroduction": "missing",
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

<ex:laSficpmsTAPP-Chernonozhkin2021-2> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:description "run 1 (major elements); run 2 (trace elements) — two line-scans on the same 400 µm line, each after pre-ablation; 'Every analysis was carried out 3 times' (§2.2.3)" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/LaserAblation/preAblationSurfaceTreatmentDefault> ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:description "Flat polished thick sections (§2.1)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproachDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrectionDefault> ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ;
                    ada:detectionLimitMethod "all: Longerich et al. (1996), LOD = 3SD/S × √(1/Nb + 1/Na) — Na = 24 and Nb = 5 (App. C5)" ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/interPassDataDependency>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSizeDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Chernonozhkin, Pittarello, Goderis, Vanhaecke et al." ] ;
    schema1:datePublished "missing" ;
    schema1:description "Two line-scan runs on the same line after pre-ablation: run 1 (30 µm, medium resolution) gives the major elements and Cr, which normalises run 2 (130 µm, low resolution) for the trace elements (§2.2.3, App. C2)" ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "N — the BELSPO, FWO, BOF-UGent and Humboldt support is for the study as a whole and is recorded under Funding Source for Analysis" ] ;
    schema1:instrument <ex:instrument/ICPMS>,
        <ex:instrument/Laser-Ablation-System> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Dept. of Chemistry, Atomic & Mass Spectrometry, Ghent University, Belgium" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "LA-SF-ICP-MS" ] ;
    schema1:name "Chernonozhkin et al. (2021) Pallasite Olivine Multi-run Spot/Transect v1" ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Chernonozhkin et al. (2021) Chem. Geol. 562; Liu et al. (2008) for IS method" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "test value schema:defaultValue" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:ablationPitDepthRateDefault "missing" ;
    ada:ablationSamplingMode "run 1: line scan, 400 µm; run 2: line scan on top of run 1, 400 µm — 'a second line-scan was completed on top of the first one' (§2.2.3)" ;
    ada:ablationSpotDurationDefault "50 s of sample ablation per 400 µm line, both runs — Table B1" ;
    ada:analysisSequenceDefault "MPI-DING and USGS reference materials at the start and end of each analytical session; every analysis carried out 3 times — §2.2.3" ;
    ada:backgroundCountTimeDefault "5 gas-blank scans and 24 ablation scans per analysis, both runs; 10 s of blank per run — Table B1" ;
    ada:blankBackgroundCorrectionMethod "Gas blank before each line analysis; the average background preceding each analysis subtracted — App. C5" ;
    ada:calibrationMeasurementFrequency "Start and end of each analytical session — 'MPI-DING and USGS reference materials were measured at the start and end of each analytical session' (§2.2.3)" ;
    ada:carrierGasFlowRateDefault "He: MFC-1 0.19 l min⁻¹; MFC-2 0.22 l min⁻¹" ;
    ada:constantsAndReferenceValuesUsedDefault "missing" ;
    ada:internalStandardApproach "run 1: sum normalization of the oxides to 100 wt% (Liu et al., 2008); run 2: single element from run 1 — §2.2.3, App. C2" ;
    ada:internalStandardElement "run 1: none (oxide sum); run 2: Cr (concentration from run 1) — §2.2.3" ;
    ada:massBiasCorrectionStrategy "missing" ;
    ada:massResolutionAssignment "run 1: medium resolution (M/ΔM = 4000); run 2: low resolution (M/ΔM = 300) — §2.2.3" ;
    ada:numberOfAcquisitionPasses -9999 ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:rasterLineSpacingDefault "N/A — line scan + spot; not 2D mapping" ;
    ada:reportedProperties "Mg, Si, P, Ca, Cr, Mn, Fe, Li, Sc, V, Co, Ni, Cu, Zn, Y, Zr, Nb, Cs, Ba, La, Ce, Pr, Nd, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu, Hf, Ta, W, Re, Ir, Pt, Au, Th, U (µg/g); Fa# — Table 1, 'the average from 3 replicate measurements'" ;
    ada:sampleIntroduction "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "Position relative to the metal-olivine rim — the line scans run \"from the olivine rim in the direction of the olivine core\" on large olivine crystals sited from the μXRF maps (p.4); the surface is pre-ablated before each analysis (p.3)" ;
    ada:samplingUnitType "Grain (individual olivine crystal) > Region of interest (line scan) — \"a second line-scan was completed on top of the first one, using a laser spot of 130 μm diameter ... and a translation speed of 10 μm s−1\" (p.3)" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "Pallasite olivine" ;
            ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/laSficpmsTAPP/primaryCalibrationStandardName> ] ;
    ada:targetSpeciesTemplate [ ada:defaultTargetSpecies "Au",
                "Ba",
                "Ca",
                "Ce",
                "Co",
                "Cr",
                "Cs",
                "Cu",
                "Dy",
                "Er",
                "Eu",
                "Fe",
                "Gd",
                "Hf",
                "Ho",
                "Ir",
                "La",
                "Li",
                "Lu",
                "Mg",
                "Mn",
                "Nb",
                "Nd",
                "Ni",
                "P",
                "Pr",
                "Pt",
                "Re",
                "Sc",
                "Si",
                "Sm",
                "Ta",
                "Tb",
                "Th",
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
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/calibrationStrategyPerTargetSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/massResolutionAssignment>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/monitoredMasses>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/spectralInterferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ] ;
    ada:totalIntegrationTimePerOutputDataPointDefault -9999 ;
    ada:uncertaintyLevel "missing" ;
    bios:computationalTool [ schema1:name "In-house MatLab script (Appendix C2)" ;
            ada:toolRole "dataReduction" ] .

<ex:instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigationDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SingleCollector/detectorConfiguration> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Double-focusing sector field ICP-MS (explicitly stated)",
        "ICPMS" ;
    schema1:hasPart <ex:instrument/ICPMS/part/ICP-Source>,
        <ex:instrument/ICPMS/part/Interface-Cone>,
        <ex:instrument/ICPMS/part/Torch> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "missing" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Thermo Fisher Scientific Element XR (SF-ICP-MS)" ] ;
    schema1:name "example instrumentName" .

<ex:instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/plasmaThermalMode>,
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
    schema1:name "missing" .

<ex:instrument/Laser-Ablation-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/LaserAblation/laserPulseDuration> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Laser Ablation System" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Teledyne CETAC Technologies Analyte G2 (193 nm ArF excimer)" ] ;
    schema1:name "HELEX II two-volume ablation cell" ;
    ada:laserFluenceDefault "4.72 J/cm² (both runs) — §2.2.3" ;
    ada:laserRepetitionRateDefault "run 1: 20 Hz; run 2: 40 Hz" ;
    ada:laserSpotGeometryDefault "run 1: 30 µm diameter circular-masked; run 2: 130 µm diameter — §2.2.3" ;
    ada:laserType "193 nm ArF* excimer — §2.2.2" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 9e-01 ;
    schema1:description "Ar, 0.90 L/min — Table B1" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:valueName "auxiliaryGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/configuration> a schema1:PropertyValueSpecification ;
    schema1:name "Configuration" ;
    schema1:value "Al standard sample cone (1.1 mm aperture); Al H-type skimmer (0.8 mm aperture)" ;
    schema1:valueName "configuration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 15 ;
    schema1:description "Ar, 15 L/min — Table B1" ;
    schema1:name "Coolant Plasma Gas Flow Rate" ;
    schema1:valueName "coolantPlasmaGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproachDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Surface-impurity spikes removed with a 3 sigma filter; results with significant spikes not included in Table 1; Pb and U not presented because of multiple spikes — §3.3" ;
    schema1:name "Filtering Approach" ;
    schema1:valueName "filteringApproachDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 9.47e-01 ;
    schema1:description "Ar, 0.947 L/min (both runs) — Table B1; no N2 added" ;
    schema1:name "Make-up Gas and Flow Rate" ;
    schema1:valueName "makeUpGasAndFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "run 1: medium (M/ΔM = 4000); run 2: low (M/ΔM = 300) — §2.2.3" ;
    schema1:name "Mass Resolution Setting" ;
    schema1:valueName "massResolutionSettingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "11 s of washout per run — Table B1" ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:valueName "memoryEffectMitigationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/plasmaThermalMode> a schema1:PropertyValueSpecification ;
    schema1:name "Plasma Thermal Mode" ;
    schema1:value "N — RF power 1000 W for both runs (Table B1); only the mapping is described as cool plasma" ;
    schema1:valueName "plasmaThermalMode" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1000 ;
    schema1:description "1000 W (run 1 major elements + run 2 trace elements)" ;
    schema1:name "RF Power" ;
    schema1:valueName "rfPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/laserPulseDuration> a schema1:PropertyValueSpecification ;
    schema1:name "Laser Pulse Duration" ;
    schema1:value "4 ns — Table B1; §2.2.2 says '<5 ns'" ;
    schema1:valueName "laserPulseDuration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/preAblationSurfaceTreatmentDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Pre-ablation before each analysis: 2 J/cm², 20 Hz, 150 µm square-masked spot, 300 µm/s — 'to avoid bias in the trace element concentrations due to re-deposition of ablated sample material after previous analyses' (§2.2.3)" ;
    schema1:name "Pre Ablation Surface Treatment" ;
    schema1:valueName "preAblationSurfaceTreatmentDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSizeDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "run 1: 10 µm/s; run 2: 10 µm/s" ;
    schema1:name "Transect Rate Mapping Rate or Step Size" ;
    schema1:valueName "transectRateMappingRateOrStepSizeDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "μXRF mapping of larger sections, on which the ablation is sited — Fe Kα intensity maps identify the mineral phases \"based on the intensities of the Kα lines of the constituent major elements (Fe, Mg, Ni, Cr, S, Ca and P)\", and the LA-ICP-MS areas correspond \"to the locations indicated on the larger μXRF maps as black rectangles\" (p.4). The instrument is a Bruker M4 Tornado with a Rh-anode source at 50 kV and 150 μA, focused to \"a 25 μm spot (measured for Mo Kα)\" (p.3)" ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:valueName "preAnalysisImagingAndScreeningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SingleCollector/detectorConfiguration> a schema1:PropertyValueSpecification ;
    schema1:name "Detector Configuration" ;
    schema1:value "Triple — Table B1 'Detection mode'" ;
    schema1:valueName "detectorConfiguration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrectionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N — 'Triple' detection (Table B1); at the 130 µm spot, major elements saturate the detector 'even when using the triple detection mode' (App. C2)" ;
    schema1:name "Pulse Analog Detector Nonlinearity Correction" ;
    schema1:valueName "pulseAnalogDetectorNonlinearityCorrectionDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/targetMaterialColumn/laSficpmsTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/calibrationStrategyPerTargetSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Calibration Strategy per Target Species" ;
    schema1:valueName "calibrationStrategyPerTargetSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Internal (Within-Measurement) Analytical Precision and Assessment Method" ;
    schema1:valueName "internalAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/massResolutionAssignment> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Mass Resolution Assignment" ;
    schema1:valueName "massResolutionAssignment" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/monitoredMasses> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Monitored Masses" ;
    schema1:valueName "monitoredMasses" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/spectralInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Spectral Interference Corrections Applied" ;
    schema1:valueName "spectralInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/interPassDataDependency> a schema1:PropertyValue ;
    schema1:name "Inter-Pass Data Dependency" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/interPassDataDependency> ;
    schema1:value "run 1: N/A; run 2: normalised to the Cr concentration from run 1 — 'The Cr concentrations calculated from this run were then used for internal standardization to normalize the data of the second, trace element run' (§2.2.3)" .


```


### laSficpmsTAPP example Chernonozhkin2021-3
laSficpmsTAPP instance derived from Chernonozhkin et al. 2021 (Chem Geol 562) Pallasite phosphate Spot analysis ns-LA-SF-ICP-MS Ghent University.
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
  "@id": "ex:laSficpmsTAPP-Chernonozhkin2021-3",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Chernonozhkin et al. (2021) Pallasite Phosphate Spot v1",
  "schema:description": "No phosphate reference material exists, so glasses calibrate (App. C3); grains identified as stanfieldite or merrillite from a Ca/(Ca + Mg) plot (§3.4)",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "stanfieldite",
      "merrillite"
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
        "@id": "ada:targetMaterialColumn/laSficpmsTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "Mineral identity, from the μXRF survey — phosphates are located as \"thin elongate inclusions in the kamacite-taenite metal matrix (e.g., μXRF map of Imilac at Fig. 1)\", the identification resting \"on the intensities of the Kα lines of the constituent major elements (Fe, Mg, Ni, Cr, S, Ca and P)\" (p.4)",
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
      "schema:defaultValue": "μXRF mapping of larger sections, on which the ablation is sited — Fe Kα intensity maps identify the mineral phases \"based on the intensities of the Kα lines of the constituent major elements (Fe, Mg, Ni, Cr, S, Ca and P)\", and the LA-ICP-MS areas correspond \"to the locations indicated on the larger μXRF maps as black rectangles\" (p.4). The instrument is a Bruker M4 Tornado with a Rh-anode source at 50 kV and 150 μA, focused to \"a 25 μm spot (measured for Mo Kα)\" (p.3)"
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
      "schema:defaultValue": 0.96,
      "schema:description": "Ar make-up: 0.96 l min⁻¹; N₂ not added"
    },
    {
      "@id": "ada:parameter/laSficpmsTAPP/interPassDataDependency",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsTAPP/interPassDataDependency"
        }
      ],
      "schema:name": "Inter-Pass Data Dependency",
      "schema:value": "N/A — a single pass"
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Double-focusing sector field ICP-MS (explicitly stated)",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Thermo Fisher Scientific Element XR (SF-ICP-MS)",
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
              "schema:value": "Al standard sample cone (1.1 mm aperture); Al H-type skimmer (0.8 mm aperture)"
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
              "schema:defaultValue": 15,
              "schema:description": "Ar, 15 L/min — Table B1"
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
              "schema:description": "Ar, 0.85 L/min — Table B1"
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
              "schema:defaultValue": 1000,
              "schema:description": "1000 W"
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
              "schema:value": "N — RF power 1000 W (Table B1)"
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
          "@id": "ada:parameter/module/ICPMS/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Low resolution (M/ΔM = 300)"
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
          "schema:value": "Triple — Table B1 'Detection mode'"
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
          "schema:defaultValue": "10 s washout time after 20 s spot ablation (specified in acquisition protocol)"
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
          "schema:value": "4 ns — Table B1; §2.2.2 says '<5 ns'"
        }
      ],
      "schema:model": {
        "schema:name": "Teledyne CETAC Technologies Analyte G2 (193 nm ArF excimer)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "193 nm ArF* excimer — §2.2.2",
      "schema:name": "HELEX II two-volume ablation cell",
      "ada:laserSpotGeometryDefault": "all: 110 µm diameter circular-masked — §2.2.4",
      "ada:laserFluenceDefault": "3.5 J cm⁻²",
      "ada:laserRepetitionRateDefault": "all: 20 Hz",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/Laser-Ablation-System"
    }
  ],
  "ada:carrierGasFlowRateDefault": "He: MFC-1 0.270 l min⁻¹; MFC-2 0.250 l min⁻¹",
  "ada:analysisSequenceDefault": "MPI-DING and USGS glasses at the beginning and repeatedly at the end of each analytical session — App. C3",
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Na",
      "Mg",
      "Al",
      "Si",
      "P",
      "K",
      "Ca",
      "Sc",
      "Ti",
      "V",
      "Cr",
      "Mn",
      "Fe",
      "Co",
      "Ni",
      "Cu",
      "Zn",
      "Rb",
      "Sr",
      "Y",
      "Zr",
      "Nb",
      "Cs",
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
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:backgroundCountTimeDefault": "8 gas blank scans; 11 ablation scans (25 cycles measurement: 15 s blank + 20 s ablation + 10 s washout)",
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Flat polished thick sections (§2.1)",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 1
      },
      {
        "schema:name": "Data acquisition",
        "schema:description": "spot — a single pass: 'All elements were measured during single spot ablation' (§2.2.4)",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
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
            "schema:defaultValue": "N — 'Triple' detection (Table B1)"
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 3,
        "ada:detectionLimitMethod": "test value ada:detectionLimitMethod"
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
      "schema:termCode": "LA-SF-ICP-MS"
    }
  ],
  "schema:creator": {
    "schema:name": "Chernonozhkin, Pittarello, Goderis, Vanhaecke et al.",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Dept. of Chemistry, Atomic & Mass Spectrometry, Ghent University, Belgium"
  },
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "N — the BELSPO, FWO, BOF-UGent and Humboldt support is for the study as a whole and is recorded under Funding Source for Analysis"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Chernonozhkin et al. (2021) Chem. Geol. 562; Liu et al. (2008) for IS method"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Grain (phosphate crystal) > Spot — compositions are reported per named phosphate grain (\"Ph1\" … \"Ph4\", with \"stanf\" or \"merr\"), each an average of numbered \"single parallel measurement\" spots (Table 2, p.10)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "In-house MatLab script (Appendix C3)"
    }
  ],
  "ada:reportedProperties": [
    "Na, Mg, Al, Si, P, K, Ca, Sc, Ti, V, Cr, Mn, Fe, Co, Ni, Cu, Zn, Rb, Sr, Y, Zr, Nb, Cs, Ba, La, Ce, Pr, Nd, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu, Hf, Ta, Pb, Th, U (µg/g); phosphate mineral (nominal) — Table 2, each 'single parallel measurement' listed per grain"
  ],
  "ada:ablationSamplingMode": [
    "all: single spot ablation — §2.2.4"
  ],
  "ada:ablationSpotDurationDefault": "20 s spot ablation (plus 10 s washout); 25 cycles acquisition",
  "ada:rasterLineSpacingDefault": "N/A — spot mode",
  "ada:internalStandardApproach": "all: sum normalization of the element oxides to 100 wt% (Liu et al., 2008) — App. C3",
  "ada:calibrationMeasurementFrequency": "Beginning and repeatedly at the end of each analytical session — App. C3",
  "ada:blankBackgroundCorrectionMethod": "Gas blank before each spot; the average background preceding each analysis subtracted — App. C5",
  "ada:internalStandardElement": "all: none — oxide-sum normalisation (App. C3)",
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "test value schema:defaultValue"
    }
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:massResolutionAssignment": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:sampleIntroduction": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:laSficpmsTAPP-Chernonozhkin2021-3",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Chernonozhkin et al. (2021) Pallasite Phosphate Spot v1",
  "schema:description": "No phosphate reference material exists, so glasses calibrate (App. C3); grains identified as stanfieldite or merrillite from a Ca/(Ca + Mg) plot (\u00a73.4)",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "stanfieldite",
      "merrillite"
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
        "@id": "ada:targetMaterialColumn/laSficpmsTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "Mineral identity, from the \u03bcXRF survey \u2014 phosphates are located as \"thin elongate inclusions in the kamacite-taenite metal matrix (e.g., \u03bcXRF map of Imilac at Fig. 1)\", the identification resting \"on the intensities of the K\u03b1 lines of the constituent major elements (Fe, Mg, Ni, Cr, S, Ca and P)\" (p.4)",
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
      "schema:defaultValue": "\u03bcXRF mapping of larger sections, on which the ablation is sited \u2014 Fe K\u03b1 intensity maps identify the mineral phases \"based on the intensities of the K\u03b1 lines of the constituent major elements (Fe, Mg, Ni, Cr, S, Ca and P)\", and the LA-ICP-MS areas correspond \"to the locations indicated on the larger \u03bcXRF maps as black rectangles\" (p.4). The instrument is a Bruker M4 Tornado with a Rh-anode source at 50 kV and 150 \u03bcA, focused to \"a 25 \u03bcm spot (measured for Mo K\u03b1)\" (p.3)"
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
      "schema:defaultValue": 0.96,
      "schema:description": "Ar make-up: 0.96 l min\u207b\u00b9; N\u2082 not added"
    },
    {
      "@id": "ada:parameter/laSficpmsTAPP/interPassDataDependency",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsTAPP/interPassDataDependency"
        }
      ],
      "schema:name": "Inter-Pass Data Dependency",
      "schema:value": "N/A \u2014 a single pass"
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Double-focusing sector field ICP-MS (explicitly stated)",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Thermo Fisher Scientific Element XR (SF-ICP-MS)",
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
              "schema:value": "Al standard sample cone (1.1 mm aperture); Al H-type skimmer (0.8 mm aperture)"
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
              "schema:defaultValue": 15,
              "schema:description": "Ar, 15 L/min \u2014 Table B1"
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
              "schema:description": "Ar, 0.85 L/min \u2014 Table B1"
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
              "schema:defaultValue": 1000,
              "schema:description": "1000 W"
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
              "schema:value": "N \u2014 RF power 1000 W (Table B1)"
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
          "@id": "ada:parameter/module/ICPMS/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Low resolution (M/\u0394M = 300)"
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
          "schema:value": "Triple \u2014 Table B1 'Detection mode'"
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
          "schema:defaultValue": "10 s washout time after 20 s spot ablation (specified in acquisition protocol)"
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
          "schema:value": "4 ns \u2014 Table B1; \u00a72.2.2 says '<5 ns'"
        }
      ],
      "schema:model": {
        "schema:name": "Teledyne CETAC Technologies Analyte G2 (193 nm ArF excimer)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "193 nm ArF* excimer \u2014 \u00a72.2.2",
      "schema:name": "HELEX II two-volume ablation cell",
      "ada:laserSpotGeometryDefault": "all: 110 \u00b5m diameter circular-masked \u2014 \u00a72.2.4",
      "ada:laserFluenceDefault": "3.5 J cm\u207b\u00b2",
      "ada:laserRepetitionRateDefault": "all: 20 Hz",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/Laser-Ablation-System"
    }
  ],
  "ada:carrierGasFlowRateDefault": "He: MFC-1 0.270 l min\u207b\u00b9; MFC-2 0.250 l min\u207b\u00b9",
  "ada:analysisSequenceDefault": "MPI-DING and USGS glasses at the beginning and repeatedly at the end of each analytical session \u2014 App. C3",
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Na",
      "Mg",
      "Al",
      "Si",
      "P",
      "K",
      "Ca",
      "Sc",
      "Ti",
      "V",
      "Cr",
      "Mn",
      "Fe",
      "Co",
      "Ni",
      "Cu",
      "Zn",
      "Rb",
      "Sr",
      "Y",
      "Zr",
      "Nb",
      "Cs",
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
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:backgroundCountTimeDefault": "8 gas blank scans; 11 ablation scans (25 cycles measurement: 15 s blank + 20 s ablation + 10 s washout)",
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Flat polished thick sections (\u00a72.1)",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 1
      },
      {
        "schema:name": "Data acquisition",
        "schema:description": "spot \u2014 a single pass: 'All elements were measured during single spot ablation' (\u00a72.2.4)",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
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
            "schema:defaultValue": "N \u2014 'Triple' detection (Table B1)"
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 3,
        "ada:detectionLimitMethod": "test value ada:detectionLimitMethod"
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
      "schema:termCode": "LA-SF-ICP-MS"
    }
  ],
  "schema:creator": {
    "schema:name": "Chernonozhkin, Pittarello, Goderis, Vanhaecke et al.",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Dept. of Chemistry, Atomic & Mass Spectrometry, Ghent University, Belgium"
  },
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "N \u2014 the BELSPO, FWO, BOF-UGent and Humboldt support is for the study as a whole and is recorded under Funding Source for Analysis"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Chernonozhkin et al. (2021) Chem. Geol. 562; Liu et al. (2008) for IS method"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Grain (phosphate crystal) > Spot \u2014 compositions are reported per named phosphate grain (\"Ph1\" \u2026 \"Ph4\", with \"stanf\" or \"merr\"), each an average of numbered \"single parallel measurement\" spots (Table 2, p.10)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "In-house MatLab script (Appendix C3)"
    }
  ],
  "ada:reportedProperties": [
    "Na, Mg, Al, Si, P, K, Ca, Sc, Ti, V, Cr, Mn, Fe, Co, Ni, Cu, Zn, Rb, Sr, Y, Zr, Nb, Cs, Ba, La, Ce, Pr, Nd, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu, Hf, Ta, Pb, Th, U (\u00b5g/g); phosphate mineral (nominal) \u2014 Table 2, each 'single parallel measurement' listed per grain"
  ],
  "ada:ablationSamplingMode": [
    "all: single spot ablation \u2014 \u00a72.2.4"
  ],
  "ada:ablationSpotDurationDefault": "20 s spot ablation (plus 10 s washout); 25 cycles acquisition",
  "ada:rasterLineSpacingDefault": "N/A \u2014 spot mode",
  "ada:internalStandardApproach": "all: sum normalization of the element oxides to 100 wt% (Liu et al., 2008) \u2014 App. C3",
  "ada:calibrationMeasurementFrequency": "Beginning and repeatedly at the end of each analytical session \u2014 App. C3",
  "ada:blankBackgroundCorrectionMethod": "Gas blank before each spot; the average background preceding each analysis subtracted \u2014 App. C5",
  "ada:internalStandardElement": "all: none \u2014 oxide-sum normalisation (App. C3)",
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "test value schema:defaultValue"
    }
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:massResolutionAssignment": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:sampleIntroduction": "missing",
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

<ex:laSficpmsTAPP-Chernonozhkin2021-3> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrectionDefault> ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ;
                    ada:detectionLimitMethod "test value ada:detectionLimitMethod" ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:description "spot — a single pass: 'All elements were measured during single spot ablation' (§2.2.4)" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:description "Flat polished thick sections (§2.1)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/interPassDataDependency>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSizeDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Chernonozhkin, Pittarello, Goderis, Vanhaecke et al." ] ;
    schema1:datePublished "missing" ;
    schema1:description "No phosphate reference material exists, so glasses calibrate (App. C3); grains identified as stanfieldite or merrillite from a Ca/(Ca + Mg) plot (§3.4)" ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "N — the BELSPO, FWO, BOF-UGent and Humboldt support is for the study as a whole and is recorded under Funding Source for Analysis" ] ;
    schema1:instrument <ex:instrument/ICPMS>,
        <ex:instrument/Laser-Ablation-System> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Dept. of Chemistry, Atomic & Mass Spectrometry, Ghent University, Belgium" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "LA-SF-ICP-MS" ] ;
    schema1:name "Chernonozhkin et al. (2021) Pallasite Phosphate Spot v1" ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Chernonozhkin et al. (2021) Chem. Geol. 562; Liu et al. (2008) for IS method" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "test value schema:defaultValue" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:ablationPitDepthRateDefault "missing" ;
    ada:ablationSamplingMode "all: single spot ablation — §2.2.4" ;
    ada:ablationSpotDurationDefault "20 s spot ablation (plus 10 s washout); 25 cycles acquisition" ;
    ada:analysisSequenceDefault "MPI-DING and USGS glasses at the beginning and repeatedly at the end of each analytical session — App. C3" ;
    ada:backgroundCountTimeDefault "8 gas blank scans; 11 ablation scans (25 cycles measurement: 15 s blank + 20 s ablation + 10 s washout)" ;
    ada:blankBackgroundCorrectionMethod "Gas blank before each spot; the average background preceding each analysis subtracted — App. C5" ;
    ada:calibrationMeasurementFrequency "Beginning and repeatedly at the end of each analytical session — App. C3" ;
    ada:carrierGasFlowRateDefault "He: MFC-1 0.270 l min⁻¹; MFC-2 0.250 l min⁻¹" ;
    ada:constantsAndReferenceValuesUsedDefault "missing" ;
    ada:internalStandardApproach "all: sum normalization of the element oxides to 100 wt% (Liu et al., 2008) — App. C3" ;
    ada:internalStandardElement "all: none — oxide-sum normalisation (App. C3)" ;
    ada:massBiasCorrectionStrategy "missing" ;
    ada:massResolutionAssignment "missing" ;
    ada:numberOfAcquisitionPasses -9999 ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:rasterLineSpacingDefault "N/A — spot mode" ;
    ada:reportedProperties "Na, Mg, Al, Si, P, K, Ca, Sc, Ti, V, Cr, Mn, Fe, Co, Ni, Cu, Zn, Rb, Sr, Y, Zr, Nb, Cs, Ba, La, Ce, Pr, Nd, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu, Hf, Ta, Pb, Th, U (µg/g); phosphate mineral (nominal) — Table 2, each 'single parallel measurement' listed per grain" ;
    ada:sampleIntroduction "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "Mineral identity, from the μXRF survey — phosphates are located as \"thin elongate inclusions in the kamacite-taenite metal matrix (e.g., μXRF map of Imilac at Fig. 1)\", the identification resting \"on the intensities of the Kα lines of the constituent major elements (Fe, Mg, Ni, Cr, S, Ca and P)\" (p.4)" ;
    ada:samplingUnitType "Grain (phosphate crystal) > Spot — compositions are reported per named phosphate grain (\"Ph1\" … \"Ph4\", with \"stanf\" or \"merr\"), each an average of numbered \"single parallel measurement\" spots (Table 2, p.10)" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "merrillite",
                "stanfieldite" ;
            ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/laSficpmsTAPP/primaryCalibrationStandardName> ] ;
    ada:targetSpeciesTemplate [ ada:defaultTargetSpecies "Al",
                "Ba",
                "Ca",
                "Ce",
                "Co",
                "Cr",
                "Cs",
                "Cu",
                "Dy",
                "Er",
                "Eu",
                "Fe",
                "Gd",
                "Hf",
                "Ho",
                "K",
                "La",
                "Lu",
                "Mg",
                "Mn",
                "Na",
                "Nb",
                "Nd",
                "Ni",
                "P",
                "Pb",
                "Pr",
                "Rb",
                "Sc",
                "Si",
                "Sm",
                "Sr",
                "Ta",
                "Tb",
                "Th",
                "Ti",
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
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/calibrationStrategyPerTargetSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/massResolutionAssignment>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/monitoredMasses>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/spectralInterferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ] ;
    ada:totalIntegrationTimePerOutputDataPointDefault -9999 ;
    ada:uncertaintyLevel "missing" ;
    bios:computationalTool [ schema1:name "In-house MatLab script (Appendix C3)" ;
            ada:toolRole "dataReduction" ] .

<ex:instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigationDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SingleCollector/detectorConfiguration> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Double-focusing sector field ICP-MS (explicitly stated)",
        "ICPMS" ;
    schema1:hasPart <ex:instrument/ICPMS/part/ICP-Source>,
        <ex:instrument/ICPMS/part/Interface-Cone>,
        <ex:instrument/ICPMS/part/Torch> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "missing" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Thermo Fisher Scientific Element XR (SF-ICP-MS)" ] ;
    schema1:name "example instrumentName" .

<ex:instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/plasmaThermalMode>,
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
    schema1:name "missing" .

<ex:instrument/Laser-Ablation-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/LaserAblation/laserPulseDuration> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Laser Ablation System" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Teledyne CETAC Technologies Analyte G2 (193 nm ArF excimer)" ] ;
    schema1:name "HELEX II two-volume ablation cell" ;
    ada:laserFluenceDefault "3.5 J cm⁻²" ;
    ada:laserRepetitionRateDefault "all: 20 Hz" ;
    ada:laserSpotGeometryDefault "all: 110 µm diameter circular-masked — §2.2.4" ;
    ada:laserType "193 nm ArF* excimer — §2.2.2" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 8.5e-01 ;
    schema1:description "Ar, 0.85 L/min — Table B1" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:valueName "auxiliaryGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/configuration> a schema1:PropertyValueSpecification ;
    schema1:name "Configuration" ;
    schema1:value "Al standard sample cone (1.1 mm aperture); Al H-type skimmer (0.8 mm aperture)" ;
    schema1:valueName "configuration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 15 ;
    schema1:description "Ar, 15 L/min — Table B1" ;
    schema1:name "Coolant Plasma Gas Flow Rate" ;
    schema1:valueName "coolantPlasmaGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 9.6e-01 ;
    schema1:description "Ar make-up: 0.96 l min⁻¹; N₂ not added" ;
    schema1:name "Make-up Gas and Flow Rate" ;
    schema1:valueName "makeUpGasAndFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Low resolution (M/ΔM = 300)" ;
    schema1:name "Mass Resolution Setting" ;
    schema1:valueName "massResolutionSettingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "10 s washout time after 20 s spot ablation (specified in acquisition protocol)" ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:valueName "memoryEffectMitigationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/plasmaThermalMode> a schema1:PropertyValueSpecification ;
    schema1:name "Plasma Thermal Mode" ;
    schema1:value "N — RF power 1000 W (Table B1)" ;
    schema1:valueName "plasmaThermalMode" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1000 ;
    schema1:description "1000 W" ;
    schema1:name "RF Power" ;
    schema1:valueName "rfPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/laserPulseDuration> a schema1:PropertyValueSpecification ;
    schema1:name "Laser Pulse Duration" ;
    schema1:value "4 ns — Table B1; §2.2.2 says '<5 ns'" ;
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
    schema1:defaultValue "μXRF mapping of larger sections, on which the ablation is sited — Fe Kα intensity maps identify the mineral phases \"based on the intensities of the Kα lines of the constituent major elements (Fe, Mg, Ni, Cr, S, Ca and P)\", and the LA-ICP-MS areas correspond \"to the locations indicated on the larger μXRF maps as black rectangles\" (p.4). The instrument is a Bruker M4 Tornado with a Rh-anode source at 50 kV and 150 μA, focused to \"a 25 μm spot (measured for Mo Kα)\" (p.3)" ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:valueName "preAnalysisImagingAndScreeningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SingleCollector/detectorConfiguration> a schema1:PropertyValueSpecification ;
    schema1:name "Detector Configuration" ;
    schema1:value "Triple — Table B1 'Detection mode'" ;
    schema1:valueName "detectorConfiguration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrectionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N — 'Triple' detection (Table B1)" ;
    schema1:name "Pulse Analog Detector Nonlinearity Correction" ;
    schema1:valueName "pulseAnalogDetectorNonlinearityCorrectionDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/targetMaterialColumn/laSficpmsTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/calibrationStrategyPerTargetSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Calibration Strategy per Target Species" ;
    schema1:valueName "calibrationStrategyPerTargetSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Internal (Within-Measurement) Analytical Precision and Assessment Method" ;
    schema1:valueName "internalAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/massResolutionAssignment> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Mass Resolution Assignment" ;
    schema1:valueName "massResolutionAssignment" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/monitoredMasses> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Monitored Masses" ;
    schema1:valueName "monitoredMasses" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/spectralInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Spectral Interference Corrections Applied" ;
    schema1:valueName "spectralInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/interPassDataDependency> a schema1:PropertyValue ;
    schema1:name "Inter-Pass Data Dependency" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/interPassDataDependency> ;
    schema1:value "N/A — a single pass" .


```


### laSficpmsTAPP example Mittlefehldt2024
laSficpmsTAPP instance derived from Mittlefehldt 2024 Appendix A Pallasite olivine Spot analysis ns-LA-SF-ICP-MS Johnson Space Center.
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
  "@id": "ex:laSficpmsTAPP-Mittlefehldt2024",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Mittlefehldt (2024) Pallasite Olivine Spot v1",
  "schema:description": "The files documenting the analysis parameters (gas flows, laser power, etc.) were lost during an extended shutdown of the JSC ICP-MS laboratory; the grains are the EMPA grain mounts, 'low in inclusions, [but] not devoid of them' (§3.3)",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "Pallasite olivine"
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
        "@id": "ada:targetMaterialColumn/laSficpmsTAPP/primaryCalibrationStandardName",
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
            "@id": "ada:parameter/module/LaserAblation/preAblationSurfaceTreatmentDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "preAblationSurfaceTreatmentDefault",
            "schema:name": "Pre Ablation Surface Treatment",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "N — grains imaged by SEM to locate inclusion-free regions"
          }
        ],
        "schema:description": "Olivine grain fragments repeatedly washed in dilute HCl and triply distilled H₂O, hand-picked, polished grain mounts",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 1
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:name": "Data acquisition",
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
        "schema:description": "test value schema:description",
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
            "schema:defaultValue": "N — parameters lost"
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
            "schema:defaultValue": "Time steps with enhanced count rates from inclusions or heterogeneity excluded from the data reduction — §3.3"
          },
          {
            "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "pulseAnalogDetectorNonlinearityCorrectionDefault",
            "schema:name": "Pulse Analog Detector Nonlinearity Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "N — parameters lost"
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 3,
        "ada:detectionLimitMethod": "test value ada:detectionLimitMethod"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "ada:samplingUnitSelectionCriteriaDefault": "Freedom from inclusions, checked by SEM beforehand — the grains were \"low in inclusions, [but] were not devoid of them\", so \"The grains were first imaged using a scanning electron microscope (SEM) to locate regions for analysis. Regions containing surface inclusions were avoided for analysis\" (p.5)",
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
      "schema:defaultValue": "SEM imaging of the grain mounts, used to place the spots — \"The grains were first imaged using a scanning electron microscope (SEM) to locate regions for analysis. Regions containing surface inclusions were avoided for analysis\" (p.5); the grains are the same mounts already used for EMPA (p.5)"
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
      "schema:defaultValue": "N — parameters lost"
    },
    {
      "@id": "ada:parameter/laSficpmsTAPP/interPassDataDependency",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsTAPP/interPassDataDependency"
        }
      ],
      "schema:name": "Inter-Pass Data Dependency",
      "schema:value": "N/A — a single pass"
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Magnetic-sector — 'magnetic-sector Thermo Fisher Element-XR ICP-MS' (§3.3)",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Thermo Fisher Scientific Element XR (SF-ICP-MS)",
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
              "schema:value": "N — parameters lost"
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
              "@id": "ada:parameter/module/ICPMS/rfPowerDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "rfPowerDefault",
              "schema:name": "RF Power",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": "N — parameters lost"
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
          "@id": "ada:parameter/module/ICPMS/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Medium (m/Δm of 4000) — §3.3"
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
          "schema:value": "N — parameters lost"
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
          "schema:defaultValue": "N — parameters lost"
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
          "schema:defaultValue": "N — parameters lost"
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
          "schema:value": "N — parameters lost"
        }
      ],
      "schema:model": {
        "schema:name": "New Wave UP-193 solid state laser — §3.3",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "193 nm solid-state (New Wave UP-193)",
      "schema:name": "N — standard cell; parameters lost",
      "ada:laserSpotGeometryDefault": "all: 75 µm spot size — §3.3",
      "ada:laserFluenceDefault": "N — parameters lost",
      "ada:laserRepetitionRateDefault": "N — parameters lost",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/Laser-Ablation-System"
    }
  ],
  "ada:carrierGasFlowRateDefault": "N — parameters lost",
  "ada:analysisSequenceDefault": "N — the Marjalahti control belongs to the EMPA work (§3.1)",
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Mg",
      "Al",
      "P",
      "Ca",
      "Sc",
      "Ti",
      "V",
      "Cr",
      "Co",
      "Ni",
      "Zn",
      "Ga"
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
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:massResolutionAssignment": "all: medium resolution (m/Δm of 4000) — §3.3",
  "ada:backgroundCountTimeDefault": "N — the analysis parameters were lost (§3.3)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-SF-ICP-MS"
    }
  ],
  "schema:creator": {
    "schema:name": "Mittlefehldt",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "ICP-MS Laboratory, NASA Johnson Space Center, Houston TX, USA"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Mittlefehldt (2024) GCA; Lee (Rice University) Excel data reduction spreadsheet"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Grain (olivine grain fragment) > Spot — \"The laser was run in spot mode with a 75 µm spot size\" (p.5); results are reported as average analyses per sample, and individual spots carry labels such as \"laser spot 059-Pa-1\" (p.8). Line scans across grain fragments were also run (p.3)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Excel spreadsheets developed by C.-T. A. Lee (Rice University)"
    }
  ],
  "ada:reportedProperties": [
    "Mg, Al, P, Ca, Sc, Ti, V, Cr, Co, Ni, Zn, Ga (µg/g) — olivine trace element contents, individual data in Table L1, averages per sample split in Table L2 and per meteorite in Table L3 (§4)"
  ],
  "ada:ablationSamplingMode": [
    "all: spot mode — 'The laser was run in spot mode' (§3.3)"
  ],
  "ada:ablationSpotDurationDefault": "N — parameters lost",
  "ada:rasterLineSpacingDefault": "N/A — spot mode",
  "ada:internalStandardApproach": "all: single element, its concentration from EMPA — '25Mg was used as the indexing element for quantification with the EMPA data used as the standardizing values' (§3.3)",
  "ada:calibrationMeasurementFrequency": "N — parameters lost",
  "ada:oxideProductionMethodAndThreshold": "N — parameters lost",
  "ada:internalStandardElement": "all: Mg (²⁵Mg) — §3.3",
  "ada:signalIntegrationIntervalMethod": "Time steps with enhanced count rates from inclusions or heterogeneity excluded — 'Analysis time steps that had enhanced count rates due to inclusions or heterogeneity were excluded from the data reduction'; inclusions show as 'time steps with enhanced P, Ca, Co, Ni and/or Zn count rates' (§3.3)",
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "test value schema:defaultValue"
    }
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:sampleIntroduction": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:laSficpmsTAPP-Mittlefehldt2024",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Mittlefehldt (2024) Pallasite Olivine Spot v1",
  "schema:description": "The files documenting the analysis parameters (gas flows, laser power, etc.) were lost during an extended shutdown of the JSC ICP-MS laboratory; the grains are the EMPA grain mounts, 'low in inclusions, [but] not devoid of them' (\u00a73.3)",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "Pallasite olivine"
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
        "@id": "ada:targetMaterialColumn/laSficpmsTAPP/primaryCalibrationStandardName",
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
            "@id": "ada:parameter/module/LaserAblation/preAblationSurfaceTreatmentDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "preAblationSurfaceTreatmentDefault",
            "schema:name": "Pre Ablation Surface Treatment",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "N \u2014 grains imaged by SEM to locate inclusion-free regions"
          }
        ],
        "schema:description": "Olivine grain fragments repeatedly washed in dilute HCl and triply distilled H\u2082O, hand-picked, polished grain mounts",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 1
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:name": "Data acquisition",
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
        "schema:description": "test value schema:description",
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
            "schema:defaultValue": "N \u2014 parameters lost"
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
            "schema:defaultValue": "Time steps with enhanced count rates from inclusions or heterogeneity excluded from the data reduction \u2014 \u00a73.3"
          },
          {
            "@id": "ada:parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "pulseAnalogDetectorNonlinearityCorrectionDefault",
            "schema:name": "Pulse Analog Detector Nonlinearity Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "N \u2014 parameters lost"
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 3,
        "ada:detectionLimitMethod": "test value ada:detectionLimitMethod"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "ada:samplingUnitSelectionCriteriaDefault": "Freedom from inclusions, checked by SEM beforehand \u2014 the grains were \"low in inclusions, [but] were not devoid of them\", so \"The grains were first imaged using a scanning electron microscope (SEM) to locate regions for analysis. Regions containing surface inclusions were avoided for analysis\" (p.5)",
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
      "schema:defaultValue": "SEM imaging of the grain mounts, used to place the spots \u2014 \"The grains were first imaged using a scanning electron microscope (SEM) to locate regions for analysis. Regions containing surface inclusions were avoided for analysis\" (p.5); the grains are the same mounts already used for EMPA (p.5)"
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
      "schema:defaultValue": "N \u2014 parameters lost"
    },
    {
      "@id": "ada:parameter/laSficpmsTAPP/interPassDataDependency",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsTAPP/interPassDataDependency"
        }
      ],
      "schema:name": "Inter-Pass Data Dependency",
      "schema:value": "N/A \u2014 a single pass"
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Magnetic-sector \u2014 'magnetic-sector Thermo Fisher Element-XR ICP-MS' (\u00a73.3)",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Thermo Fisher Scientific Element XR (SF-ICP-MS)",
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
              "schema:value": "N \u2014 parameters lost"
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
              "@id": "ada:parameter/module/ICPMS/rfPowerDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "rfPowerDefault",
              "schema:name": "RF Power",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": "N \u2014 parameters lost"
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
          "@id": "ada:parameter/module/ICPMS/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Medium (m/\u0394m of 4000) \u2014 \u00a73.3"
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
          "schema:value": "N \u2014 parameters lost"
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
          "schema:defaultValue": "N \u2014 parameters lost"
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
          "schema:defaultValue": "N \u2014 parameters lost"
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
          "schema:value": "N \u2014 parameters lost"
        }
      ],
      "schema:model": {
        "schema:name": "New Wave UP-193 solid state laser \u2014 \u00a73.3",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "193 nm solid-state (New Wave UP-193)",
      "schema:name": "N \u2014 standard cell; parameters lost",
      "ada:laserSpotGeometryDefault": "all: 75 \u00b5m spot size \u2014 \u00a73.3",
      "ada:laserFluenceDefault": "N \u2014 parameters lost",
      "ada:laserRepetitionRateDefault": "N \u2014 parameters lost",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/Laser-Ablation-System"
    }
  ],
  "ada:carrierGasFlowRateDefault": "N \u2014 parameters lost",
  "ada:analysisSequenceDefault": "N \u2014 the Marjalahti control belongs to the EMPA work (\u00a73.1)",
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Mg",
      "Al",
      "P",
      "Ca",
      "Sc",
      "Ti",
      "V",
      "Cr",
      "Co",
      "Ni",
      "Zn",
      "Ga"
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
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:massResolutionAssignment": "all: medium resolution (m/\u0394m of 4000) \u2014 \u00a73.3",
  "ada:backgroundCountTimeDefault": "N \u2014 the analysis parameters were lost (\u00a73.3)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-SF-ICP-MS"
    }
  ],
  "schema:creator": {
    "schema:name": "Mittlefehldt",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "ICP-MS Laboratory, NASA Johnson Space Center, Houston TX, USA"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Mittlefehldt (2024) GCA; Lee (Rice University) Excel data reduction spreadsheet"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Grain (olivine grain fragment) > Spot \u2014 \"The laser was run in spot mode with a 75 \u00b5m spot size\" (p.5); results are reported as average analyses per sample, and individual spots carry labels such as \"laser spot 059-Pa-1\" (p.8). Line scans across grain fragments were also run (p.3)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Excel spreadsheets developed by C.-T. A. Lee (Rice University)"
    }
  ],
  "ada:reportedProperties": [
    "Mg, Al, P, Ca, Sc, Ti, V, Cr, Co, Ni, Zn, Ga (\u00b5g/g) \u2014 olivine trace element contents, individual data in Table L1, averages per sample split in Table L2 and per meteorite in Table L3 (\u00a74)"
  ],
  "ada:ablationSamplingMode": [
    "all: spot mode \u2014 'The laser was run in spot mode' (\u00a73.3)"
  ],
  "ada:ablationSpotDurationDefault": "N \u2014 parameters lost",
  "ada:rasterLineSpacingDefault": "N/A \u2014 spot mode",
  "ada:internalStandardApproach": "all: single element, its concentration from EMPA \u2014 '25Mg was used as the indexing element for quantification with the EMPA data used as the standardizing values' (\u00a73.3)",
  "ada:calibrationMeasurementFrequency": "N \u2014 parameters lost",
  "ada:oxideProductionMethodAndThreshold": "N \u2014 parameters lost",
  "ada:internalStandardElement": "all: Mg (\u00b2\u2075Mg) \u2014 \u00a73.3",
  "ada:signalIntegrationIntervalMethod": "Time steps with enhanced count rates from inclusions or heterogeneity excluded \u2014 'Analysis time steps that had enhanced count rates due to inclusions or heterogeneity were excluded from the data reduction'; inclusions show as 'time steps with enhanced P, Ca, Co, Ni and/or Zn count rates' (\u00a73.3)",
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "test value schema:defaultValue"
    }
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:blankBackgroundCorrectionMethod": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:sampleIntroduction": "missing",
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

<ex:laSficpmsTAPP-Mittlefehldt2024> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:description "test value schema:description" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproachDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/LaserAblation/signalSmoothingDefault>,
                        <https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrectionDefault> ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ;
                    ada:detectionLimitMethod "test value ada:detectionLimitMethod" ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/LaserAblation/preAblationSurfaceTreatmentDefault> ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:description "Olivine grain fragments repeatedly washed in dilute HCl and triply distilled H₂O, hand-picked, polished grain mounts" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/interPassDataDependency>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSizeDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Mittlefehldt" ] ;
    schema1:datePublished "missing" ;
    schema1:description "The files documenting the analysis parameters (gas flows, laser power, etc.) were lost during an extended shutdown of the JSC ICP-MS laboratory; the grains are the EMPA grain mounts, 'low in inclusions, [but] not devoid of them' (§3.3)" ;
    schema1:instrument <ex:instrument/ICPMS>,
        <ex:instrument/Laser-Ablation-System> ;
    schema1:location [ a schema1:Place ;
            schema1:name "ICP-MS Laboratory, NASA Johnson Space Center, Houston TX, USA" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "LA-SF-ICP-MS" ] ;
    schema1:name "Mittlefehldt (2024) Pallasite Olivine Spot v1" ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Mittlefehldt (2024) GCA; Lee (Rice University) Excel data reduction spreadsheet" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "test value schema:defaultValue" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:ablationPitDepthRateDefault "missing" ;
    ada:ablationSamplingMode "all: spot mode — 'The laser was run in spot mode' (§3.3)" ;
    ada:ablationSpotDurationDefault "N — parameters lost" ;
    ada:analysisSequenceDefault "N — the Marjalahti control belongs to the EMPA work (§3.1)" ;
    ada:backgroundCountTimeDefault "N — the analysis parameters were lost (§3.3)" ;
    ada:blankBackgroundCorrectionMethod "missing" ;
    ada:calibrationMeasurementFrequency "N — parameters lost" ;
    ada:carrierGasFlowRateDefault "N — parameters lost" ;
    ada:constantsAndReferenceValuesUsedDefault "missing" ;
    ada:internalStandardApproach "all: single element, its concentration from EMPA — '25Mg was used as the indexing element for quantification with the EMPA data used as the standardizing values' (§3.3)" ;
    ada:internalStandardElement "all: Mg (²⁵Mg) — §3.3" ;
    ada:massBiasCorrectionStrategy "missing" ;
    ada:massResolutionAssignment "all: medium resolution (m/Δm of 4000) — §3.3" ;
    ada:numberOfAcquisitionPasses -9999 ;
    ada:oxideProductionMethodAndThreshold "N — parameters lost" ;
    ada:rasterLineSpacingDefault "N/A — spot mode" ;
    ada:reportedProperties "Mg, Al, P, Ca, Sc, Ti, V, Cr, Co, Ni, Zn, Ga (µg/g) — olivine trace element contents, individual data in Table L1, averages per sample split in Table L2 and per meteorite in Table L3 (§4)" ;
    ada:sampleIntroduction "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "Freedom from inclusions, checked by SEM beforehand — the grains were \"low in inclusions, [but] were not devoid of them\", so \"The grains were first imaged using a scanning electron microscope (SEM) to locate regions for analysis. Regions containing surface inclusions were avoided for analysis\" (p.5)" ;
    ada:samplingUnitType "Grain (olivine grain fragment) > Spot — \"The laser was run in spot mode with a 75 µm spot size\" (p.5); results are reported as average analyses per sample, and individual spots carry labels such as \"laser spot 059-Pa-1\" (p.8). Line scans across grain fragments were also run (p.3)" ;
    ada:signalIntegrationIntervalMethod "Time steps with enhanced count rates from inclusions or heterogeneity excluded — 'Analysis time steps that had enhanced count rates due to inclusions or heterogeneity were excluded from the data reduction'; inclusions show as 'time steps with enhanced P, Ca, Co, Ni and/or Zn count rates' (§3.3)" ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "Pallasite olivine" ;
            ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/laSficpmsTAPP/primaryCalibrationStandardName> ] ;
    ada:targetSpeciesTemplate [ ada:defaultTargetSpecies "Al",
                "Ca",
                "Co",
                "Cr",
                "Ga",
                "Mg",
                "Ni",
                "P",
                "Sc",
                "Ti",
                "V",
                "Zn" ;
            ada:targetSpeciesColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetSpecies" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/calibrationStrategyPerTargetSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/massResolutionAssignment>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/monitoredMasses>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/spectralInterferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ] ;
    ada:totalIntegrationTimePerOutputDataPointDefault -9999 ;
    ada:uncertaintyLevel "missing" ;
    bios:computationalTool [ schema1:name "Excel spreadsheets developed by C.-T. A. Lee (Rice University)" ;
            ada:toolRole "dataReduction" ] .

<ex:instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuningDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigationDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SingleCollector/detectorConfiguration> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Magnetic-sector — 'magnetic-sector Thermo Fisher Element-XR ICP-MS' (§3.3)" ;
    schema1:hasPart <ex:instrument/ICPMS/part/ICP-Source>,
        <ex:instrument/ICPMS/part/Interface-Cone>,
        <ex:instrument/ICPMS/part/Torch> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "missing" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Thermo Fisher Scientific Element XR (SF-ICP-MS)" ] ;
    schema1:name "example instrumentName" .

<ex:instrument/ICPMS/part/ICP-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPowerDefault> ;
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
    schema1:name "missing" .

<ex:instrument/Laser-Ablation-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/LaserAblation/laserPulseDuration> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Laser Ablation System" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "New Wave UP-193 solid state laser — §3.3" ] ;
    schema1:name "N — standard cell; parameters lost" ;
    ada:laserFluenceDefault "N — parameters lost" ;
    ada:laserRepetitionRateDefault "N — parameters lost" ;
    ada:laserSpotGeometryDefault "all: 75 µm spot size — §3.3" ;
    ada:laserType "193 nm solid-state (New Wave UP-193)" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/configuration> a schema1:PropertyValueSpecification ;
    schema1:name "Configuration" ;
    schema1:value "N — parameters lost" ;
    schema1:valueName "configuration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/filteringApproachDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Time steps with enhanced count rates from inclusions or heterogeneity excluded from the data reduction — §3.3" ;
    schema1:name "Filtering Approach" ;
    schema1:valueName "filteringApproachDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N — parameters lost" ;
    schema1:name "ICP Tuning" ;
    schema1:valueName "icpTuningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N — parameters lost" ;
    schema1:name "Make-up Gas and Flow Rate" ;
    schema1:valueName "makeUpGasAndFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Medium (m/Δm of 4000) — §3.3" ;
    schema1:name "Mass Resolution Setting" ;
    schema1:valueName "massResolutionSettingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/memoryEffectMitigationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N — parameters lost" ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:valueName "memoryEffectMitigationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N — parameters lost" ;
    schema1:name "RF Power" ;
    schema1:valueName "rfPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/laserPulseDuration> a schema1:PropertyValueSpecification ;
    schema1:name "Laser Pulse Duration" ;
    schema1:value "N — parameters lost" ;
    schema1:valueName "laserPulseDuration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/preAblationSurfaceTreatmentDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N — grains imaged by SEM to locate inclusion-free regions" ;
    schema1:name "Pre Ablation Surface Treatment" ;
    schema1:valueName "preAblationSurfaceTreatmentDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/signalSmoothingDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N — parameters lost" ;
    schema1:name "Signal Smoothing" ;
    schema1:valueName "signalSmoothingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSizeDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N/A — spot mode" ;
    schema1:name "Transect Rate Mapping Rate or Step Size" ;
    schema1:valueName "transectRateMappingRateOrStepSizeDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "SEM imaging of the grain mounts, used to place the spots — \"The grains were first imaged using a scanning electron microscope (SEM) to locate regions for analysis. Regions containing surface inclusions were avoided for analysis\" (p.5); the grains are the same mounts already used for EMPA (p.5)" ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:valueName "preAnalysisImagingAndScreeningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SingleCollector/detectorConfiguration> a schema1:PropertyValueSpecification ;
    schema1:name "Detector Configuration" ;
    schema1:value "N — parameters lost" ;
    schema1:valueName "detectorConfiguration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrectionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N — parameters lost" ;
    schema1:name "Pulse Analog Detector Nonlinearity Correction" ;
    schema1:valueName "pulseAnalogDetectorNonlinearityCorrectionDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/targetMaterialColumn/laSficpmsTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/calibrationStrategyPerTargetSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Calibration Strategy per Target Species" ;
    schema1:valueName "calibrationStrategyPerTargetSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Internal (Within-Measurement) Analytical Precision and Assessment Method" ;
    schema1:valueName "internalAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/massResolutionAssignment> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Mass Resolution Assignment" ;
    schema1:valueName "massResolutionAssignment" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/monitoredMasses> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Monitored Masses" ;
    schema1:valueName "monitoredMasses" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/spectralInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Spectral Interference Corrections Applied" ;
    schema1:valueName "spectralInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/interPassDataDependency> a schema1:PropertyValue ;
    schema1:name "Inter-Pass Data Dependency" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/interPassDataDependency> ;
    schema1:value "N/A — a single pass" .


```


### laSficpmsTAPP example Navarro2024
laSficpmsTAPP instance derived from Navarro et al. 2024 (ACS ESC 8) Iron meteorites Spot analysis ns-LA-SF-ICP-MS University of Campinas.
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
  "@id": "ex:laSficpmsTAPP-Navarro2024",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Navarro et al. (2024) Iron Meteorite Spot v1",
  "schema:description": "Two measurement standards complement each other: North Chile for matrix similarity and NIST SRM 612 for its well-known composition; Fe + Ni + Co = 100% normalisation removes the need for an internal standard",
  "ada:targetMaterialTemplate": {
    "ada:targetMaterialDeclaration": "Iron meteorite metal (kamacite + taenite)",
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
        "@id": "ada:targetMaterialColumn/laSficpmsTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "Phase targeting, as the stated alternative to rastering — \"depending on the specific objectives, spot sampling at specific phases may also fulfill the analytical requirements\", against the problem that irons have an \"inherent natural inhomogeneity, a result of their lamellar exsolution patterns\" (p.2)",
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
      "schema:defaultValue": "N — the preparation is stated without an imaging step: \"Before analyses, fragments about 1 cm were mounted in epoxy resin, polished, and cleaned with ultrapure water\" (p.3). The meteorites' structural classes were known beforehand (Table 1, p.2) but no screening of this material is described"
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
      "schema:description": "Ar makeup gas, combined via a T-piece near the torch; Table 2 lists a nebulizer gas flow rate of 1.1 L/min — Table 2"
    },
    {
      "@id": "ada:parameter/laSficpmsTAPP/interPassDataDependency",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsTAPP/interPassDataDependency"
        }
      ],
      "schema:name": "Inter-Pass Data Dependency",
      "schema:value": "N/A — a single pass"
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Sector field (SF-ICP-MS) (explicitly stated: \"sector field inductively coupled plasma mass spectrometer\")",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Thermo Fisher Scientific Element XR (SF-ICP-MS)",
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
              "schema:value": "Ni sampler cone; Ni skimmer cone"
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
              "schema:description": "16 L/min — Table 2 'plasma gas flow rate'"
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
              "schema:defaultValue": 0.9,
              "schema:description": "0.9 L/min — Table 2"
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
              "schema:defaultValue": 1200,
              "schema:description": "1200 W"
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
          "@id": "ada:parameter/module/ICPMS/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Low resolution (M/ΔM = 300)"
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
          "schema:value": "Triple mode — Table 2 'detector range'; 'performed in low-resolution and triple mode detection'"
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
          "schema:defaultValue": "ICP-MS and laser settings optimised daily 'to achieve the compromise between optimum signal intensity and low oxide formation, as specified by the factory'; mass calibration and detector cross-calibration 'systematically checked and redone if required' — Experimental section"
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
          "schema:value": "4 ns — Table 2"
        }
      ],
      "schema:model": {
        "schema:name": "Excite 193 (Teledyne) — Table 2",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "193 nm ArF excimer; pulse duration 4 ns",
      "schema:name": "HelEx II two-volume sample cell",
      "ada:laserSpotGeometryDefault": "all: 150 µm — Table 2 'spot diameter'",
      "ada:laserFluenceDefault": "7 J cm⁻²",
      "ada:laserRepetitionRateDefault": "all: 10 Hz",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/Laser-Ablation-System"
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Fragments ~1 cm mounted in epoxy resin, polished, cleaned with ultrapure water",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
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
            "schema:value": "On (active)"
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
        "schema:description": "test value schema:description"
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
            "schema:defaultValue": "N — 'detector cross-calibration were systematically checked and redone if required'; Fe and Ni measured on low-abundance isotopes in analog mode"
          }
        ],
        "ada:detectionLimitMethod": "all: Longerich et al., calculated for each acquisition in iolite 4 — 'the LOD must be calculated for each acquisition'; Table 3 gives the medians",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 3
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "ada:carrierGasFlowRateDefault": "He: 0.6 l min⁻¹ (MFC 1) + 0.7 l min⁻¹ (MFC 2) in HelEx II cell; combined with Ar makeup via T-piece near torch",
  "ada:analysisSequenceDefault": "3 × NIST SRM 612 and 3 × North Chile, then blocks of ten unknowns, each followed by 2 × NIST SRM 612 and 2 × North Chile — Experimental section",
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Cr",
      "Fe",
      "Co",
      "Ni",
      "Cu",
      "Ga",
      "Ge",
      "As",
      "Ru",
      "Rh",
      "Pd",
      "W",
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
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:massResolutionAssignment": "all: low resolution (300) — Table 2",
  "ada:backgroundCountTimeDefault": "20 s — laser firing with the shutter closed, before each ablation",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-SF-ICP-MS"
    }
  ],
  "schema:creator": {
    "schema:name": "Navarro, Enzweiler, Crósta et al.",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Isotope Geology Laboratory, University of Campinas (UNICAMP), Brazil"
  },
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "N — the acknowledgements name CNPq grant 316191/2021-3 (J.E.) and support for a conference presentation; neither is for procedure development"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Navarro et al. (2024) ACS Earth Space Chem. 8, 281; Longerich et al. (1996)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Whole sample (polished ~1 cm fragment) > Spot — \"fragments about 1 cm were mounted in epoxy resin, polished, and cleaned with ultrapure water\" (p.3); the reported quantity is the meteorite's bulk composition for chemical classification (Table 1, p.2)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "iolite 4.5.7 with 3D Trace Elements DRS"
    }
  ],
  "ada:reportedProperties": [
    "Fe, Ni (g/100 g); Cr, Co, Cu, Ga, Ge, As, Ru, Rh, Pd, W, Re, Os, Ir, Pt, Au (µg/g); chemical classification (nominal) — Table 3 and Table 5"
  ],
  "ada:ablationSamplingMode": [
    "all: spot — Experimental section"
  ],
  "ada:ablationSpotDurationDefault": "40 s — '20 s of blank measurement (laser-firing with the shutter closed), followed by 40 s of sample ablation'",
  "ada:rasterLineSpacingDefault": "N/A — spot mode",
  "ada:internalStandardApproach": "all: sum normalization, Fe + Ni + Co = 100% — 'In the final step, sum normalization was applied to the major constituents of iron meteorites, specifically Fe + Ni + Co = 100%. This ... eliminated the conventional practice of needing an internal standard'",
  "ada:calibrationMeasurementFrequency": "Every ten unknowns (about every 15 min) — calibration blocks bracket blocks of ten unknowns; 'every 15 min calibration block'",
  "ada:blankBackgroundCorrectionMethod": "20 s blank before each spot, laser firing with the shutter closed; LODs calculated per acquisition in iolite 4 — Experimental section",
  "ada:internalStandardElement": "all: none — Fe + Ni + Co sum normalisation",
  "ada:secondaryReferenceMaterialDefault": [
    "North Chile — 'also measured as an unknown sample several times, on different days, over four months', for intermediate precision; eight other known iron meteorites validate against published INAA values"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "test value schema:defaultValue"
    }
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:sampleIntroduction": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:laSficpmsTAPP-Navarro2024",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Navarro et al. (2024) Iron Meteorite Spot v1",
  "schema:description": "Two measurement standards complement each other: North Chile for matrix similarity and NIST SRM 612 for its well-known composition; Fe + Ni + Co = 100% normalisation removes the need for an internal standard",
  "ada:targetMaterialTemplate": {
    "ada:targetMaterialDeclaration": "Iron meteorite metal (kamacite + taenite)",
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
        "@id": "ada:targetMaterialColumn/laSficpmsTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "Phase targeting, as the stated alternative to rastering \u2014 \"depending on the specific objectives, spot sampling at specific phases may also fulfill the analytical requirements\", against the problem that irons have an \"inherent natural inhomogeneity, a result of their lamellar exsolution patterns\" (p.2)",
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
      "schema:defaultValue": "N \u2014 the preparation is stated without an imaging step: \"Before analyses, fragments about 1 cm were mounted in epoxy resin, polished, and cleaned with ultrapure water\" (p.3). The meteorites' structural classes were known beforehand (Table 1, p.2) but no screening of this material is described"
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
      "schema:description": "Ar makeup gas, combined via a T-piece near the torch; Table 2 lists a nebulizer gas flow rate of 1.1 L/min \u2014 Table 2"
    },
    {
      "@id": "ada:parameter/laSficpmsTAPP/interPassDataDependency",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsTAPP/interPassDataDependency"
        }
      ],
      "schema:name": "Inter-Pass Data Dependency",
      "schema:value": "N/A \u2014 a single pass"
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Sector field (SF-ICP-MS) (explicitly stated: \"sector field inductively coupled plasma mass spectrometer\")",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Thermo Fisher Scientific Element XR (SF-ICP-MS)",
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
              "schema:value": "Ni sampler cone; Ni skimmer cone"
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
              "schema:description": "16 L/min \u2014 Table 2 'plasma gas flow rate'"
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
              "schema:defaultValue": 0.9,
              "schema:description": "0.9 L/min \u2014 Table 2"
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
              "schema:defaultValue": 1200,
              "schema:description": "1200 W"
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
          "@id": "ada:parameter/module/ICPMS/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Low resolution (M/\u0394M = 300)"
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
          "schema:value": "Triple mode \u2014 Table 2 'detector range'; 'performed in low-resolution and triple mode detection'"
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
          "schema:defaultValue": "ICP-MS and laser settings optimised daily 'to achieve the compromise between optimum signal intensity and low oxide formation, as specified by the factory'; mass calibration and detector cross-calibration 'systematically checked and redone if required' \u2014 Experimental section"
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
          "schema:value": "4 ns \u2014 Table 2"
        }
      ],
      "schema:model": {
        "schema:name": "Excite 193 (Teledyne) \u2014 Table 2",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "193 nm ArF excimer; pulse duration 4 ns",
      "schema:name": "HelEx II two-volume sample cell",
      "ada:laserSpotGeometryDefault": "all: 150 \u00b5m \u2014 Table 2 'spot diameter'",
      "ada:laserFluenceDefault": "7 J cm\u207b\u00b2",
      "ada:laserRepetitionRateDefault": "all: 10 Hz",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/Laser-Ablation-System"
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Fragments ~1 cm mounted in epoxy resin, polished, cleaned with ultrapure water",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
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
            "schema:value": "On (active)"
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
        "schema:description": "test value schema:description"
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
            "schema:defaultValue": "N \u2014 'detector cross-calibration were systematically checked and redone if required'; Fe and Ni measured on low-abundance isotopes in analog mode"
          }
        ],
        "ada:detectionLimitMethod": "all: Longerich et al., calculated for each acquisition in iolite 4 \u2014 'the LOD must be calculated for each acquisition'; Table 3 gives the medians",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 3
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "ada:carrierGasFlowRateDefault": "He: 0.6 l min\u207b\u00b9 (MFC 1) + 0.7 l min\u207b\u00b9 (MFC 2) in HelEx II cell; combined with Ar makeup via T-piece near torch",
  "ada:analysisSequenceDefault": "3 \u00d7 NIST SRM 612 and 3 \u00d7 North Chile, then blocks of ten unknowns, each followed by 2 \u00d7 NIST SRM 612 and 2 \u00d7 North Chile \u2014 Experimental section",
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Cr",
      "Fe",
      "Co",
      "Ni",
      "Cu",
      "Ga",
      "Ge",
      "As",
      "Ru",
      "Rh",
      "Pd",
      "W",
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
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:massResolutionAssignment": "all: low resolution (300) \u2014 Table 2",
  "ada:backgroundCountTimeDefault": "20 s \u2014 laser firing with the shutter closed, before each ablation",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-SF-ICP-MS"
    }
  ],
  "schema:creator": {
    "schema:name": "Navarro, Enzweiler, Cr\u00f3sta et al.",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Isotope Geology Laboratory, University of Campinas (UNICAMP), Brazil"
  },
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "N \u2014 the acknowledgements name CNPq grant 316191/2021-3 (J.E.) and support for a conference presentation; neither is for procedure development"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Navarro et al. (2024) ACS Earth Space Chem. 8, 281; Longerich et al. (1996)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Whole sample (polished ~1 cm fragment) > Spot \u2014 \"fragments about 1 cm were mounted in epoxy resin, polished, and cleaned with ultrapure water\" (p.3); the reported quantity is the meteorite's bulk composition for chemical classification (Table 1, p.2)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "iolite 4.5.7 with 3D Trace Elements DRS"
    }
  ],
  "ada:reportedProperties": [
    "Fe, Ni (g/100 g); Cr, Co, Cu, Ga, Ge, As, Ru, Rh, Pd, W, Re, Os, Ir, Pt, Au (\u00b5g/g); chemical classification (nominal) \u2014 Table 3 and Table 5"
  ],
  "ada:ablationSamplingMode": [
    "all: spot \u2014 Experimental section"
  ],
  "ada:ablationSpotDurationDefault": "40 s \u2014 '20 s of blank measurement (laser-firing with the shutter closed), followed by 40 s of sample ablation'",
  "ada:rasterLineSpacingDefault": "N/A \u2014 spot mode",
  "ada:internalStandardApproach": "all: sum normalization, Fe + Ni + Co = 100% \u2014 'In the final step, sum normalization was applied to the major constituents of iron meteorites, specifically Fe + Ni + Co = 100%. This ... eliminated the conventional practice of needing an internal standard'",
  "ada:calibrationMeasurementFrequency": "Every ten unknowns (about every 15 min) \u2014 calibration blocks bracket blocks of ten unknowns; 'every 15 min calibration block'",
  "ada:blankBackgroundCorrectionMethod": "20 s blank before each spot, laser firing with the shutter closed; LODs calculated per acquisition in iolite 4 \u2014 Experimental section",
  "ada:internalStandardElement": "all: none \u2014 Fe + Ni + Co sum normalisation",
  "ada:secondaryReferenceMaterialDefault": [
    "North Chile \u2014 'also measured as an unknown sample several times, on different days, over four months', for intermediate precision; eight other known iron meteorites validate against published INAA values"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "test value schema:defaultValue"
    }
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:sampleIntroduction": "missing",
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

<ex:laSficpmsTAPP-Navarro2024> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrectionDefault> ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ;
                    ada:detectionLimitMethod "all: Longerich et al., calculated for each acquisition in iolite 4 — 'the LOD must be calculated for each acquisition'; Table 3 gives the medians" ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/guardElectrode> ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:description "test value schema:description" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:description "Fragments ~1 cm mounted in epoxy resin, polished, cleaned with ultrapure water" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/interPassDataDependency>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSizeDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Navarro, Enzweiler, Crósta et al." ] ;
    schema1:datePublished "missing" ;
    schema1:description "Two measurement standards complement each other: North Chile for matrix similarity and NIST SRM 612 for its well-known composition; Fe + Ni + Co = 100% normalisation removes the need for an internal standard" ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "N — the acknowledgements name CNPq grant 316191/2021-3 (J.E.) and support for a conference presentation; neither is for procedure development" ] ;
    schema1:instrument <ex:instrument/ICPMS>,
        <ex:instrument/Laser-Ablation-System> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Isotope Geology Laboratory, University of Campinas (UNICAMP), Brazil" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "LA-SF-ICP-MS" ] ;
    schema1:name "Navarro et al. (2024) Iron Meteorite Spot v1" ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Navarro et al. (2024) ACS Earth Space Chem. 8, 281; Longerich et al. (1996)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "test value schema:defaultValue" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:ablationPitDepthRateDefault "missing" ;
    ada:ablationSamplingMode "all: spot — Experimental section" ;
    ada:ablationSpotDurationDefault "40 s — '20 s of blank measurement (laser-firing with the shutter closed), followed by 40 s of sample ablation'" ;
    ada:analysisSequenceDefault "3 × NIST SRM 612 and 3 × North Chile, then blocks of ten unknowns, each followed by 2 × NIST SRM 612 and 2 × North Chile — Experimental section" ;
    ada:backgroundCountTimeDefault "20 s — laser firing with the shutter closed, before each ablation" ;
    ada:blankBackgroundCorrectionMethod "20 s blank before each spot, laser firing with the shutter closed; LODs calculated per acquisition in iolite 4 — Experimental section" ;
    ada:calibrationMeasurementFrequency "Every ten unknowns (about every 15 min) — calibration blocks bracket blocks of ten unknowns; 'every 15 min calibration block'" ;
    ada:carrierGasFlowRateDefault "He: 0.6 l min⁻¹ (MFC 1) + 0.7 l min⁻¹ (MFC 2) in HelEx II cell; combined with Ar makeup via T-piece near torch" ;
    ada:constantsAndReferenceValuesUsedDefault "missing" ;
    ada:internalStandardApproach "all: sum normalization, Fe + Ni + Co = 100% — 'In the final step, sum normalization was applied to the major constituents of iron meteorites, specifically Fe + Ni + Co = 100%. This ... eliminated the conventional practice of needing an internal standard'" ;
    ada:internalStandardElement "all: none — Fe + Ni + Co sum normalisation" ;
    ada:massBiasCorrectionStrategy "missing" ;
    ada:massResolutionAssignment "all: low resolution (300) — Table 2" ;
    ada:numberOfAcquisitionPasses -9999 ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:rasterLineSpacingDefault "N/A — spot mode" ;
    ada:reportedProperties "Fe, Ni (g/100 g); Cr, Co, Cu, Ga, Ge, As, Ru, Rh, Pd, W, Re, Os, Ir, Pt, Au (µg/g); chemical classification (nominal) — Table 3 and Table 5" ;
    ada:sampleIntroduction "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "Phase targeting, as the stated alternative to rastering — \"depending on the specific objectives, spot sampling at specific phases may also fulfill the analytical requirements\", against the problem that irons have an \"inherent natural inhomogeneity, a result of their lamellar exsolution patterns\" (p.2)" ;
    ada:samplingUnitType "Whole sample (polished ~1 cm fragment) > Spot — \"fragments about 1 cm were mounted in epoxy resin, polished, and cleaned with ultrapure water\" (p.3); the reported quantity is the meteorite's bulk composition for chemical classification (Table 1, p.2)" ;
    ada:secondaryReferenceMaterialDefault "North Chile — 'also measured as an unknown sample several times, on different days, over four months', for intermediate precision; eight other known iron meteorites validate against published INAA values" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:targetMaterialTemplate [ ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/laSficpmsTAPP/primaryCalibrationStandardName> ;
            ada:targetMaterialDeclaration "Iron meteorite metal (kamacite + taenite)" ] ;
    ada:targetSpeciesTemplate [ ada:defaultTargetSpecies "As",
                "Au",
                "Co",
                "Cr",
                "Cu",
                "Fe",
                "Ga",
                "Ge",
                "Ir",
                "Ni",
                "Os",
                "Pd",
                "Pt",
                "Re",
                "Rh",
                "Ru",
                "W" ;
            ada:targetSpeciesColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetSpecies" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/calibrationStrategyPerTargetSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/massResolutionAssignment>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/monitoredMasses>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/spectralInterferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ] ;
    ada:totalIntegrationTimePerOutputDataPointDefault -9999 ;
    ada:uncertaintyLevel "missing" ;
    bios:computationalTool [ schema1:name "iolite 4.5.7 with 3D Trace Elements DRS" ;
            ada:toolRole "dataReduction" ] .

<ex:instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuningDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SingleCollector/detectorConfiguration> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Sector field (SF-ICP-MS) (explicitly stated: \"sector field inductively coupled plasma mass spectrometer\")" ;
    schema1:hasPart <ex:instrument/ICPMS/part/ICP-Source>,
        <ex:instrument/ICPMS/part/Interface-Cone>,
        <ex:instrument/ICPMS/part/Torch> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "missing" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Thermo Fisher Scientific Element XR (SF-ICP-MS)" ] ;
    schema1:name "example instrumentName" .

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
    schema1:name "missing" .

<ex:instrument/Laser-Ablation-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/LaserAblation/laserPulseDuration> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Laser Ablation System" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Excite 193 (Teledyne) — Table 2" ] ;
    schema1:name "HelEx II two-volume sample cell" ;
    ada:laserFluenceDefault "7 J cm⁻²" ;
    ada:laserRepetitionRateDefault "all: 10 Hz" ;
    ada:laserSpotGeometryDefault "all: 150 µm — Table 2 'spot diameter'" ;
    ada:laserType "193 nm ArF excimer; pulse duration 4 ns" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 9e-01 ;
    schema1:description "0.9 L/min — Table 2" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:valueName "auxiliaryGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/configuration> a schema1:PropertyValueSpecification ;
    schema1:name "Configuration" ;
    schema1:value "Ni sampler cone; Ni skimmer cone" ;
    schema1:valueName "configuration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 16 ;
    schema1:description "16 L/min — Table 2 'plasma gas flow rate'" ;
    schema1:name "Coolant Plasma Gas Flow Rate" ;
    schema1:valueName "coolantPlasmaGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/guardElectrode> a schema1:PropertyValueSpecification ;
    schema1:name "Guard Electrode" ;
    schema1:value "On (active)" ;
    schema1:valueName "guardElectrode" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "ICP-MS and laser settings optimised daily 'to achieve the compromise between optimum signal intensity and low oxide formation, as specified by the factory'; mass calibration and detector cross-calibration 'systematically checked and redone if required' — Experimental section" ;
    schema1:name "ICP Tuning" ;
    schema1:valueName "icpTuningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 2 ;
    schema1:description "Ar makeup gas, combined via a T-piece near the torch; Table 2 lists a nebulizer gas flow rate of 1.1 L/min — Table 2" ;
    schema1:name "Make-up Gas and Flow Rate" ;
    schema1:valueName "makeUpGasAndFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Low resolution (M/ΔM = 300)" ;
    schema1:name "Mass Resolution Setting" ;
    schema1:valueName "massResolutionSettingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1200 ;
    schema1:description "1200 W" ;
    schema1:name "RF Power" ;
    schema1:valueName "rfPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/laserPulseDuration> a schema1:PropertyValueSpecification ;
    schema1:name "Laser Pulse Duration" ;
    schema1:value "4 ns — Table 2" ;
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
    schema1:defaultValue "N — the preparation is stated without an imaging step: \"Before analyses, fragments about 1 cm were mounted in epoxy resin, polished, and cleaned with ultrapure water\" (p.3). The meteorites' structural classes were known beforehand (Table 1, p.2) but no screening of this material is described" ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:valueName "preAnalysisImagingAndScreeningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SingleCollector/detectorConfiguration> a schema1:PropertyValueSpecification ;
    schema1:name "Detector Configuration" ;
    schema1:value "Triple mode — Table 2 'detector range'; 'performed in low-resolution and triple mode detection'" ;
    schema1:valueName "detectorConfiguration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrectionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N — 'detector cross-calibration were systematically checked and redone if required'; Fe and Ni measured on low-abundance isotopes in analog mode" ;
    schema1:name "Pulse Analog Detector Nonlinearity Correction" ;
    schema1:valueName "pulseAnalogDetectorNonlinearityCorrectionDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/targetMaterialColumn/laSficpmsTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/calibrationStrategyPerTargetSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Calibration Strategy per Target Species" ;
    schema1:valueName "calibrationStrategyPerTargetSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Internal (Within-Measurement) Analytical Precision and Assessment Method" ;
    schema1:valueName "internalAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/massResolutionAssignment> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Mass Resolution Assignment" ;
    schema1:valueName "massResolutionAssignment" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/monitoredMasses> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Monitored Masses" ;
    schema1:valueName "monitoredMasses" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/spectralInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Spectral Interference Corrections Applied" ;
    schema1:valueName "spectralInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/interPassDataDependency> a schema1:PropertyValue ;
    schema1:name "Inter-Pass Data Dependency" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/interPassDataDependency> ;
    schema1:value "N/A — a single pass" .


```


### laSficpmsTAPP example Navarro2024-2
laSficpmsTAPP instance derived from Navarro et al. 2024 (ACS ESC 8) Iron meteorites Raster mapping (2D) ns-LA-SF-ICP-MS University of Campinas.
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
  "@id": "ex:laSficpmsTAPP-Navarro2024-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Navarro et al. (2024) Iron Meteorite Raster Mapping v1",
  "schema:description": "Mapping over regions with diverse phases of Augusto Pestana; Fe + Ni + Co = 100% normalisation 'is mandatory when acquiring elemental maps of multiphasic samples'",
  "ada:targetMaterialTemplate": {
    "ada:targetMaterialDeclaration": "Iron meteorite metal (kamacite + plessite)",
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
        "@id": "ada:targetMaterialColumn/laSficpmsTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "Representativeness, and phase diversity — \"the approach of rastering large areas may improve representative sampling compared with spot analysis\" (p.2), and the mapping is \"conducted within regions featuring diverse phases of the Augusto Pestana meteorite\" (p.1)",
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
      "schema:defaultValue": "Chemical etching to reveal the phases before mapping — \"For the mapping experiment, the polished surface of the Augusto Pestana sample was etched with freshly prepared Nital solution (2% v/v HNO3 ... in 99.5% absolute ethanol) to reveal the presence of different phases (in this case, kamacite and plessite)\" (p.3). Not imaging, but the screening step that sites the map"
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
      "schema:defaultValue": "all: 10 µm/s — 'scanning at a speed of 10 μm s−1'"
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
      "schema:description": "Ar makeup gas, combined via a T-piece near the torch; Table 2 lists a nebulizer gas flow rate of 1.1 L/min — Table 2"
    },
    {
      "@id": "ada:parameter/laSficpmsTAPP/interPassDataDependency",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsTAPP/interPassDataDependency"
        }
      ],
      "schema:name": "Inter-Pass Data Dependency",
      "schema:value": "N/A — a single pass"
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Sector field (SF-ICP-MS) (explicitly stated)",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Thermo Fisher Scientific Element XR (SF-ICP-MS)",
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
              "schema:value": "Ni sampler cone; Ni skimmer cone"
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
              "schema:description": "16 L/min — Table 2 'plasma gas flow rate'"
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
              "schema:defaultValue": 0.9,
              "schema:description": "0.9 L/min — Table 2"
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
              "schema:defaultValue": 1200,
              "schema:description": "1200 W"
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
          "@id": "ada:parameter/module/ICPMS/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Low resolution (M/ΔM = 300)"
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
          "schema:value": "Triple mode — Table 2 'detector range'; 'performed in low-resolution and triple mode detection'"
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
          "schema:defaultValue": "ICP-MS and laser settings optimised daily 'to achieve the compromise between optimum signal intensity and low oxide formation, as specified by the factory'; mass calibration and detector cross-calibration 'systematically checked and redone if required' — Experimental section"
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
          "schema:value": "4 ns — Table 2"
        }
      ],
      "schema:model": {
        "schema:name": "Excite 193 (Teledyne) — Table 2",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "193 nm ArF excimer; pulse duration 4 ns",
      "schema:name": "HelEx II two-volume sample cell",
      "ada:laserSpotGeometryDefault": "all: 150 µm² square spot — as written: 'targeting a 150 μm2 square spot'",
      "ada:laserFluenceDefault": "7 J cm⁻²",
      "ada:laserRepetitionRateDefault": "all: 10 Hz",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/Laser-Ablation-System"
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Same Augusto Pestana fragment etched with Nital solution (2% v/v HNO₃ in ethanol) to reveal kamacite and plessite",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
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
            "schema:value": "On (active)"
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
        "schema:description": "test value schema:description"
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
            "schema:defaultValue": "N — 'detector cross-calibration were systematically checked and redone if required'; Fe and Ni measured on low-abundance isotopes in analog mode"
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 3,
        "ada:detectionLimitMethod": "test value ada:detectionLimitMethod"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "ada:carrierGasFlowRateDefault": "He: 0.6 l min⁻¹ (MFC 1) + 0.7 l min⁻¹ (MFC 2) in HelEx II cell",
  "ada:analysisSequenceDefault": "1 min background, 3 × NIST SRM 612, 3 × North Chile, a 30 min measurement over the unknown area, then 3 × North Chile, 3 × NIST SRM 612 and background — Experimental section",
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Cr",
      "Fe",
      "Co",
      "Ni",
      "Cu",
      "Ga",
      "Ge",
      "As",
      "Ru",
      "Rh",
      "Pd",
      "W",
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
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:massResolutionAssignment": "all: low resolution (300) — Table 2",
  "ada:backgroundCountTimeDefault": "1 min at the start and at the end of the mapping sequence — Experimental section",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-SF-ICP-MS"
    }
  ],
  "schema:creator": {
    "schema:name": "Navarro, Enzweiler, Crósta et al.",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Isotope Geology Laboratory, University of Campinas (UNICAMP), Brazil"
  },
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "N — the acknowledgements name CNPq grant 316191/2021-3 (J.E.) and support for a conference presentation; neither is for procedure development"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Navarro et al. (2024) ACS Earth Space Chem. 8, 281; Longerich et al. (1996)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Region of interest > Phase — \"elemental mapping, conducted within regions featuring diverse phases of the Augusto Pestana meteorite\" (p.1); the map is read for the phases it resolves, \"even without prior knowledge regarding natural structural variations\" (p.1)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "iolite 4.5.7 with 3D Trace Elements DRS"
    }
  ],
  "ada:reportedProperties": [
    "Fe, Ni (g/100 g); Cr, Co, Cu, Ga, Ge, As, Ru, Rh, Pd, W, Re, Os, Ir, Pt, Au (µg/g); chemical classification (nominal) — Table 3 and Table 5"
  ],
  "ada:ablationSamplingMode": [
    "all: scanning (elemental mapping) — Experimental section"
  ],
  "ada:ablationSpotDurationDefault": "N/A — mapping mode",
  "ada:internalStandardApproach": "all: sum normalization, Fe + Ni + Co = 100% — 'In the final step, sum normalization was applied to the major constituents of iron meteorites, specifically Fe + Ni + Co = 100%. This ... eliminated the conventional practice of needing an internal standard'",
  "ada:calibrationMeasurementFrequency": "Before and after the 30 min map — Experimental section",
  "ada:blankBackgroundCorrectionMethod": "1 min background at the start and end of the mapping sequence — Experimental section",
  "ada:internalStandardElement": "all: none — Fe + Ni + Co sum normalisation",
  "ada:secondaryReferenceMaterialDefault": [
    "North Chile — 'also measured as an unknown sample several times, on different days, over four months', for intermediate precision; eight other known iron meteorites validate against published INAA values"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "test value schema:defaultValue"
    }
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:laSficpmsTAPP-Navarro2024-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Navarro et al. (2024) Iron Meteorite Raster Mapping v1",
  "schema:description": "Mapping over regions with diverse phases of Augusto Pestana; Fe + Ni + Co = 100% normalisation 'is mandatory when acquiring elemental maps of multiphasic samples'",
  "ada:targetMaterialTemplate": {
    "ada:targetMaterialDeclaration": "Iron meteorite metal (kamacite + plessite)",
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
        "@id": "ada:targetMaterialColumn/laSficpmsTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "Representativeness, and phase diversity \u2014 \"the approach of rastering large areas may improve representative sampling compared with spot analysis\" (p.2), and the mapping is \"conducted within regions featuring diverse phases of the Augusto Pestana meteorite\" (p.1)",
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
      "schema:defaultValue": "Chemical etching to reveal the phases before mapping \u2014 \"For the mapping experiment, the polished surface of the Augusto Pestana sample was etched with freshly prepared Nital solution (2% v/v HNO3 ... in 99.5% absolute ethanol) to reveal the presence of different phases (in this case, kamacite and plessite)\" (p.3). Not imaging, but the screening step that sites the map"
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
      "schema:defaultValue": "all: 10 \u00b5m/s \u2014 'scanning at a speed of 10 \u03bcm s\u22121'"
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
      "schema:description": "Ar makeup gas, combined via a T-piece near the torch; Table 2 lists a nebulizer gas flow rate of 1.1 L/min \u2014 Table 2"
    },
    {
      "@id": "ada:parameter/laSficpmsTAPP/interPassDataDependency",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsTAPP/interPassDataDependency"
        }
      ],
      "schema:name": "Inter-Pass Data Dependency",
      "schema:value": "N/A \u2014 a single pass"
    }
  ],
  "schema:instrument": [
    {
      "schema:additionalType": [
        "ICPMS",
        "Sector field (SF-ICP-MS) (explicitly stated)",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "Thermo Fisher Scientific Element XR (SF-ICP-MS)",
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
              "schema:value": "Ni sampler cone; Ni skimmer cone"
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
              "schema:description": "16 L/min \u2014 Table 2 'plasma gas flow rate'"
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
              "schema:defaultValue": 0.9,
              "schema:description": "0.9 L/min \u2014 Table 2"
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
              "schema:defaultValue": 1200,
              "schema:description": "1200 W"
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
          "@id": "ada:parameter/module/ICPMS/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Low resolution (M/\u0394M = 300)"
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
          "schema:value": "Triple mode \u2014 Table 2 'detector range'; 'performed in low-resolution and triple mode detection'"
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
          "schema:defaultValue": "ICP-MS and laser settings optimised daily 'to achieve the compromise between optimum signal intensity and low oxide formation, as specified by the factory'; mass calibration and detector cross-calibration 'systematically checked and redone if required' \u2014 Experimental section"
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
          "schema:value": "4 ns \u2014 Table 2"
        }
      ],
      "schema:model": {
        "schema:name": "Excite 193 (Teledyne) \u2014 Table 2",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "193 nm ArF excimer; pulse duration 4 ns",
      "schema:name": "HelEx II two-volume sample cell",
      "ada:laserSpotGeometryDefault": "all: 150 \u00b5m\u00b2 square spot \u2014 as written: 'targeting a 150 \u03bcm2 square spot'",
      "ada:laserFluenceDefault": "7 J cm\u207b\u00b2",
      "ada:laserRepetitionRateDefault": "all: 10 Hz",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/Laser-Ablation-System"
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Same Augusto Pestana fragment etched with Nital solution (2% v/v HNO\u2083 in ethanol) to reveal kamacite and plessite",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
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
            "schema:value": "On (active)"
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
        "schema:description": "test value schema:description"
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
            "schema:defaultValue": "N \u2014 'detector cross-calibration were systematically checked and redone if required'; Fe and Ni measured on low-abundance isotopes in analog mode"
          }
        ],
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 3,
        "ada:detectionLimitMethod": "test value ada:detectionLimitMethod"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "ada:carrierGasFlowRateDefault": "He: 0.6 l min\u207b\u00b9 (MFC 1) + 0.7 l min\u207b\u00b9 (MFC 2) in HelEx II cell",
  "ada:analysisSequenceDefault": "1 min background, 3 \u00d7 NIST SRM 612, 3 \u00d7 North Chile, a 30 min measurement over the unknown area, then 3 \u00d7 North Chile, 3 \u00d7 NIST SRM 612 and background \u2014 Experimental section",
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Cr",
      "Fe",
      "Co",
      "Ni",
      "Cu",
      "Ga",
      "Ge",
      "As",
      "Ru",
      "Rh",
      "Pd",
      "W",
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
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/monitoredMasses",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredMasses",
        "schema:name": "Monitored Masses",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/massResolutionAssignment",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionAssignment",
        "schema:name": "Mass Resolution Assignment",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/calibrationStrategyPerTargetSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "calibrationStrategyPerTargetSpecies",
        "schema:name": "Calibration Strategy per Target Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/spectralInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "spectralInterferenceCorrectionsApplied",
        "schema:name": "Spectral Interference Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/laSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "internalAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Internal (Within-Measurement) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:massResolutionAssignment": "all: low resolution (300) \u2014 Table 2",
  "ada:backgroundCountTimeDefault": "1 min at the start and at the end of the mapping sequence \u2014 Experimental section",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-SF-ICP-MS"
    }
  ],
  "schema:creator": {
    "schema:name": "Navarro, Enzweiler, Cr\u00f3sta et al.",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Isotope Geology Laboratory, University of Campinas (UNICAMP), Brazil"
  },
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "N \u2014 the acknowledgements name CNPq grant 316191/2021-3 (J.E.) and support for a conference presentation; neither is for procedure development"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Navarro et al. (2024) ACS Earth Space Chem. 8, 281; Longerich et al. (1996)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Region of interest > Phase \u2014 \"elemental mapping, conducted within regions featuring diverse phases of the Augusto Pestana meteorite\" (p.1); the map is read for the phases it resolves, \"even without prior knowledge regarding natural structural variations\" (p.1)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "iolite 4.5.7 with 3D Trace Elements DRS"
    }
  ],
  "ada:reportedProperties": [
    "Fe, Ni (g/100 g); Cr, Co, Cu, Ga, Ge, As, Ru, Rh, Pd, W, Re, Os, Ir, Pt, Au (\u00b5g/g); chemical classification (nominal) \u2014 Table 3 and Table 5"
  ],
  "ada:ablationSamplingMode": [
    "all: scanning (elemental mapping) \u2014 Experimental section"
  ],
  "ada:ablationSpotDurationDefault": "N/A \u2014 mapping mode",
  "ada:internalStandardApproach": "all: sum normalization, Fe + Ni + Co = 100% \u2014 'In the final step, sum normalization was applied to the major constituents of iron meteorites, specifically Fe + Ni + Co = 100%. This ... eliminated the conventional practice of needing an internal standard'",
  "ada:calibrationMeasurementFrequency": "Before and after the 30 min map \u2014 Experimental section",
  "ada:blankBackgroundCorrectionMethod": "1 min background at the start and end of the mapping sequence \u2014 Experimental section",
  "ada:internalStandardElement": "all: none \u2014 Fe + Ni + Co sum normalisation",
  "ada:secondaryReferenceMaterialDefault": [
    "North Chile \u2014 'also measured as an unknown sample several times, on different days, over four months', for intermediate precision; eight other known iron meteorites validate against published INAA values"
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "test value schema:defaultValue"
    }
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:constantsAndReferenceValuesUsedDefault": "missing",
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:numberOfAcquisitionPasses": -9999,
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
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

<ex:laSficpmsTAPP-Navarro2024-2> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrectionDefault> ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ;
                    ada:detectionLimitMethod "test value ada:detectionLimitMethod" ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/guardElectrode> ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:description "test value schema:description" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:description "Same Augusto Pestana fragment etched with Nital solution (2% v/v HNO₃ in ethanol) to reveal kamacite and plessite" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/interPassDataDependency>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRateDefault>,
        <https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSizeDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Navarro, Enzweiler, Crósta et al." ] ;
    schema1:datePublished "missing" ;
    schema1:description "Mapping over regions with diverse phases of Augusto Pestana; Fe + Ni + Co = 100% normalisation 'is mandatory when acquiring elemental maps of multiphasic samples'" ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "N — the acknowledgements name CNPq grant 316191/2021-3 (J.E.) and support for a conference presentation; neither is for procedure development" ] ;
    schema1:instrument <ex:instrument/ICPMS>,
        <ex:instrument/Laser-Ablation-System> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Isotope Geology Laboratory, University of Campinas (UNICAMP), Brazil" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "LA-SF-ICP-MS" ] ;
    schema1:name "Navarro et al. (2024) Iron Meteorite Raster Mapping v1" ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Navarro et al. (2024) ACS Earth Space Chem. 8, 281; Longerich et al. (1996)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "test value schema:defaultValue" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:ablationPitDepthRateDefault "missing" ;
    ada:ablationSamplingMode "all: scanning (elemental mapping) — Experimental section" ;
    ada:ablationSpotDurationDefault "N/A — mapping mode" ;
    ada:analysisSequenceDefault "1 min background, 3 × NIST SRM 612, 3 × North Chile, a 30 min measurement over the unknown area, then 3 × North Chile, 3 × NIST SRM 612 and background — Experimental section" ;
    ada:backgroundCountTimeDefault "1 min at the start and at the end of the mapping sequence — Experimental section" ;
    ada:blankBackgroundCorrectionMethod "1 min background at the start and end of the mapping sequence — Experimental section" ;
    ada:calibrationMeasurementFrequency "Before and after the 30 min map — Experimental section" ;
    ada:carrierGasFlowRateDefault "He: 0.6 l min⁻¹ (MFC 1) + 0.7 l min⁻¹ (MFC 2) in HelEx II cell" ;
    ada:constantsAndReferenceValuesUsedDefault "missing" ;
    ada:internalStandardApproach "all: sum normalization, Fe + Ni + Co = 100% — 'In the final step, sum normalization was applied to the major constituents of iron meteorites, specifically Fe + Ni + Co = 100%. This ... eliminated the conventional practice of needing an internal standard'" ;
    ada:internalStandardElement "all: none — Fe + Ni + Co sum normalisation" ;
    ada:massBiasCorrectionStrategy "missing" ;
    ada:massResolutionAssignment "all: low resolution (300) — Table 2" ;
    ada:numberOfAcquisitionPasses -9999 ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:rasterLineSpacingDefault "missing" ;
    ada:reportedProperties "Fe, Ni (g/100 g); Cr, Co, Cu, Ga, Ge, As, Ru, Rh, Pd, W, Re, Os, Ir, Pt, Au (µg/g); chemical classification (nominal) — Table 3 and Table 5" ;
    ada:sampleIntroduction "missing" ;
    ada:samplingUnitSelectionCriteriaDefault "Representativeness, and phase diversity — \"the approach of rastering large areas may improve representative sampling compared with spot analysis\" (p.2), and the mapping is \"conducted within regions featuring diverse phases of the Augusto Pestana meteorite\" (p.1)" ;
    ada:samplingUnitType "Region of interest > Phase — \"elemental mapping, conducted within regions featuring diverse phases of the Augusto Pestana meteorite\" (p.1); the map is read for the phases it resolves, \"even without prior knowledge regarding natural structural variations\" (p.1)" ;
    ada:secondaryReferenceMaterialDefault "North Chile — 'also measured as an unknown sample several times, on different days, over four months', for intermediate precision; eight other known iron meteorites validate against published INAA values" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:targetMaterialTemplate [ ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/laSficpmsTAPP/primaryCalibrationStandardName> ;
            ada:targetMaterialDeclaration "Iron meteorite metal (kamacite + plessite)" ] ;
    ada:targetSpeciesTemplate [ ada:defaultTargetSpecies "As",
                "Au",
                "Co",
                "Cr",
                "Cu",
                "Fe",
                "Ga",
                "Ge",
                "Ir",
                "Ni",
                "Os",
                "Pd",
                "Pt",
                "Re",
                "Rh",
                "Ru",
                "W" ;
            ada:targetSpeciesColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetSpecies" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/calibrationStrategyPerTargetSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/massResolutionAssignment>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/monitoredMasses>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/spectralInterferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ] ;
    ada:totalIntegrationTimePerOutputDataPointDefault -9999 ;
    ada:uncertaintyLevel "missing" ;
    bios:computationalTool [ schema1:name "iolite 4.5.7 with 3D Trace Elements DRS" ;
            ada:toolRole "dataReduction" ] .

<ex:instrument/ICPMS> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuningDefault>,
        <https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault>,
        <https://ada.astromat.org/metadata/parameter/module/SingleCollector/detectorConfiguration> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "ICPMS",
        "Sector field (SF-ICP-MS) (explicitly stated)" ;
    schema1:hasPart <ex:instrument/ICPMS/part/ICP-Source>,
        <ex:instrument/ICPMS/part/Interface-Cone>,
        <ex:instrument/ICPMS/part/Torch> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "missing" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Thermo Fisher Scientific Element XR (SF-ICP-MS)" ] ;
    schema1:name "example instrumentName" .

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
    schema1:name "missing" .

<ex:instrument/Laser-Ablation-System> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/LaserAblation/laserPulseDuration> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Laser Ablation System" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Excite 193 (Teledyne) — Table 2" ] ;
    schema1:name "HelEx II two-volume sample cell" ;
    ada:laserFluenceDefault "7 J cm⁻²" ;
    ada:laserRepetitionRateDefault "all: 10 Hz" ;
    ada:laserSpotGeometryDefault "all: 150 µm² square spot — as written: 'targeting a 150 μm2 square spot'" ;
    ada:laserType "193 nm ArF excimer; pulse duration 4 ns" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/auxiliaryGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 9e-01 ;
    schema1:description "0.9 L/min — Table 2" ;
    schema1:name "Auxiliary Gas Flow Rate" ;
    schema1:valueName "auxiliaryGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/configuration> a schema1:PropertyValueSpecification ;
    schema1:name "Configuration" ;
    schema1:value "Ni sampler cone; Ni skimmer cone" ;
    schema1:valueName "configuration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/coolantPlasmaGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 16 ;
    schema1:description "16 L/min — Table 2 'plasma gas flow rate'" ;
    schema1:name "Coolant Plasma Gas Flow Rate" ;
    schema1:valueName "coolantPlasmaGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/guardElectrode> a schema1:PropertyValueSpecification ;
    schema1:name "Guard Electrode" ;
    schema1:value "On (active)" ;
    schema1:valueName "guardElectrode" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/icpTuningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "ICP-MS and laser settings optimised daily 'to achieve the compromise between optimum signal intensity and low oxide formation, as specified by the factory'; mass calibration and detector cross-calibration 'systematically checked and redone if required' — Experimental section" ;
    schema1:name "ICP Tuning" ;
    schema1:valueName "icpTuningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/makeUpGasAndFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 2 ;
    schema1:description "Ar makeup gas, combined via a T-piece near the torch; Table 2 lists a nebulizer gas flow rate of 1.1 L/min — Table 2" ;
    schema1:name "Make-up Gas and Flow Rate" ;
    schema1:valueName "makeUpGasAndFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/massResolutionSettingDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Low resolution (M/ΔM = 300)" ;
    schema1:name "Mass Resolution Setting" ;
    schema1:valueName "massResolutionSettingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/ICPMS/rfPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1200 ;
    schema1:description "1200 W" ;
    schema1:name "RF Power" ;
    schema1:valueName "rfPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/laserPulseDuration> a schema1:PropertyValueSpecification ;
    schema1:name "Laser Pulse Duration" ;
    schema1:value "4 ns — Table 2" ;
    schema1:valueName "laserPulseDuration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/LaserAblation/transectRateMappingRateOrStepSizeDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "all: 10 µm/s — 'scanning at a speed of 10 μm s−1'" ;
    schema1:name "Transect Rate Mapping Rate or Step Size" ;
    schema1:valueName "transectRateMappingRateOrStepSizeDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Chemical etching to reveal the phases before mapping — \"For the mapping experiment, the polished surface of the Augusto Pestana sample was etched with freshly prepared Nital solution (2% v/v HNO3 ... in 99.5% absolute ethanol) to reveal the presence of different phases (in this case, kamacite and plessite)\" (p.3). Not imaging, but the screening step that sites the map" ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:valueName "preAnalysisImagingAndScreeningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SingleCollector/detectorConfiguration> a schema1:PropertyValueSpecification ;
    schema1:name "Detector Configuration" ;
    schema1:value "Triple mode — Table 2 'detector range'; 'performed in low-resolution and triple mode detection'" ;
    schema1:valueName "detectorConfiguration" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SingleCollector/pulseAnalogDetectorNonlinearityCorrectionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N — 'detector cross-calibration were systematically checked and redone if required'; Fe and Ni measured on low-abundance isotopes in analog mode" ;
    schema1:name "Pulse Analog Detector Nonlinearity Correction" ;
    schema1:valueName "pulseAnalogDetectorNonlinearityCorrectionDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/targetMaterialColumn/laSficpmsTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/calibrationStrategyPerTargetSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Calibration Strategy per Target Species" ;
    schema1:valueName "calibrationStrategyPerTargetSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Internal (Within-Measurement) Analytical Precision and Assessment Method" ;
    schema1:valueName "internalAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/massResolutionAssignment> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Mass Resolution Assignment" ;
    schema1:valueName "massResolutionAssignment" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/monitoredMasses> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Monitored Masses" ;
    schema1:valueName "monitoredMasses" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/spectralInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Spectral Interference Corrections Applied" ;
    schema1:valueName "spectralInterferenceCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/laSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/interPassDataDependency> a schema1:PropertyValue ;
    schema1:name "Inter-Pass Data Dependency" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/interPassDataDependency> ;
    schema1:value "N/A — a single pass" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: LA-SF-ICP-MS Technique-Aligned Procedure Profile (laSficpmsTAPP)
description: Laser-ablation sector-field (high-resolution) ICP-MS extension of the
  base TAPP definition, generated from tapp/Current TAPPs/LA-SF-ICP-MS_TAPP_v93.csv
  via the path-driven pipeline.
allOf:
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/calibrationFactor/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/targetSpecies/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/compositionQC/schema.yaml#/$defs/ProcedureIdentification
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
                  const: ada:targetMaterialColumn/laSficpmsTAPP/primaryCalibrationStandardName
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
                  const: ada:targetMaterialColumn/laSficpmsTAPP/primaryCalibrationStandardName
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
                            const: ada:parameter/laSficpmsTAPP/analysisInclusionAndRejectionCriteria
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/laSficpmsTAPP/analysisInclusionAndRejectionCriteria
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
                            const: ada:parameter/laSficpmsTAPP/analysisInclusionAndRejectionCriteria
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/laSficpmsTAPP/analysisInclusionAndRejectionCriteria
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
        - title: E-scan Range
          description: Electric scan range used for peak acquisition, expressed as
            percentage of the centre mass (%). Record 'N/A' if E-scan acquisition
            mode is not used.
          type: object
          properties:
            '@id':
              const: ada:parameter/laSficpmsTAPP/eScanRange
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laSficpmsTAPP/eScanRange
            schema:name:
              const: E-scan Range
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
          readOnly: true
        - title: Triple Scanning Mode
          description: Whether each mass peak is scanned three times per cycle and
            the results averaged (Y/N). Record 'N/A' if not applicable to the instrument.
          type: object
          properties:
            '@id':
              const: ada:parameter/laSficpmsTAPP/tripleScanningMode
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laSficpmsTAPP/tripleScanningMode
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
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Procedure_matrixOffsetCorrectionLief
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
              const: ada:parameter/laSficpmsTAPP/interPassDataDependency
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laSficpmsTAPP/interPassDataDependency
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
          title: E-scan Range
          description: Electric scan range used for peak acquisition, expressed as
            percentage of the centre mass (%). Record 'N/A' if E-scan acquisition
            mode is not used.
          type: object
          properties:
            '@id':
              const: ada:parameter/laSficpmsTAPP/eScanRange
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laSficpmsTAPP/eScanRange
            schema:name:
              const: E-scan Range
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
          readOnly: true
        minContains: 0
        maxContains: 1
      - contains:
          title: Triple Scanning Mode
          description: Whether each mass peak is scanned three times per cycle and
            the results averaged (Y/N). Record 'N/A' if not applicable to the instrument.
          type: object
          properties:
            '@id':
              const: ada:parameter/laSficpmsTAPP/tripleScanningMode
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laSficpmsTAPP/tripleScanningMode
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
          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Procedure_matrixOffsetCorrectionLief
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
              const: ada:parameter/laSficpmsTAPP/interPassDataDependency
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laSficpmsTAPP/interPassDataDependency
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
                        const: ada:parameter/laSficpmsTAPP/doublyChargedSpeciesMonitorDefault
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
                      schema:defaultValue:
                        type: string
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
                        const: ada:parameter/laSficpmsTAPP/doublyChargedSpeciesProductionDefault
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
                      schema:defaultValue:
                        type: string
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
                        const: ada:parameter/laSficpmsTAPP/doublyChargedSpeciesMonitorDefault
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
                      schema:defaultValue:
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
                - contains:
                    title: Doubly-Charged Species Production
                    description: Measured percentage of doubly-charged ion production
                      for the monitored species at the time of instrument tuning.
                      The acceptable threshold is typically <1% or <3%. Record both
                      the threshold and the measured value.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/laSficpmsTAPP/doublyChargedSpeciesProductionDefault
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
                      schema:defaultValue:
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
                  const: ada:targetSpeciesColumn/laSficpmsTAPP/monitoredMasses
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
            - title: Mass Resolution Assignment
              description: Mass resolution mode used for acquisition. One target species
                may be acquired at more than one resolution, so the assignment is
                per acquired mass rather than per element. The overall mode(s) used
                in the procedure are recorded in Mass Resolution Setting (Group 3).
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/laSficpmsTAPP/massResolutionAssignment
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
                  const: ada:targetSpeciesColumn/laSficpmsTAPP/dwellTimePerMass
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
                  const: ada:targetSpeciesColumn/laSficpmsTAPP/calibrationStrategyPerTargetSpecies
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
                  const: ada:targetSpeciesColumn/laSficpmsTAPP/spectralInterferenceCorrectionsApplied
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
                  const: ada:targetSpeciesColumn/laSficpmsTAPP/interferingSpecies
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
                  const: ada:targetSpeciesColumn/laSficpmsTAPP/interferenceCorrectionMethod
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
                  const: ada:targetSpeciesColumn/laSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod
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
                  const: ada:targetSpeciesColumn/laSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod
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
                  const: ada:targetSpeciesColumn/laSficpmsTAPP/analyticalAccuracyAndAssessmentMethod
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
                  const: ada:targetSpeciesColumn/laSficpmsTAPP/countingStatisticsError
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
                  const: ada:targetSpeciesColumn/laSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod
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
                  const: ada:targetSpeciesColumn/laSficpmsTAPP/monitoredMasses
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
              title: Mass Resolution Assignment
              description: Mass resolution mode used for acquisition. One target species
                may be acquired at more than one resolution, so the assignment is
                per acquired mass rather than per element. The overall mode(s) used
                in the procedure are recorded in Mass Resolution Setting (Group 3).
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/laSficpmsTAPP/massResolutionAssignment
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
                  const: ada:targetSpeciesColumn/laSficpmsTAPP/dwellTimePerMass
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
                  const: ada:targetSpeciesColumn/laSficpmsTAPP/calibrationStrategyPerTargetSpecies
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
                  const: ada:targetSpeciesColumn/laSficpmsTAPP/spectralInterferenceCorrectionsApplied
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
                  const: ada:targetSpeciesColumn/laSficpmsTAPP/interferingSpecies
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
                  const: ada:targetSpeciesColumn/laSficpmsTAPP/interferenceCorrectionMethod
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
                  const: ada:targetSpeciesColumn/laSficpmsTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod
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
                  const: ada:targetSpeciesColumn/laSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod
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
                  const: ada:targetSpeciesColumn/laSficpmsTAPP/analyticalAccuracyAndAssessmentMethod
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
                  const: ada:targetSpeciesColumn/laSficpmsTAPP/countingStatisticsError
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
                  const: ada:targetSpeciesColumn/laSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethod
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
    ada:massResolutionAssignment:
      description: Mass resolution mode used for acquisition. One target species may
        be acquired at more than one resolution, so the assignment is per acquired
        mass rather than per element. The overall mode(s) used in the procedure are
        recorded in Mass Resolution Setting (Group 3).
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
  - ada:massResolutionAssignment
  - ada:totalIntegrationTimePerOutputDataPointDefault
  - ada:massBiasCorrectionStrategy
  - ada:constantsAndReferenceValuesUsedDefault
  - ada:numberOfAcquisitionPasses

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS/tapp/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS/tapp/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS/tapp/context.jsonld)

## Sources

* [LA-SF-ICP-MS_TAPP_v16.csv (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/LA-SF-ICPMS/tapp`

