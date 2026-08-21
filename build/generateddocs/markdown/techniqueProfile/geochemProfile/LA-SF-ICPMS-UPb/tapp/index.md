
# LA-SF-ICP-MS U-Pb Geochronology TAPP (laSficpmsUPbTAPP) (Schema)

`ogch.techniqueProfile.geochemProfile.LA-SF-ICPMS-UPb.tapp` *v0.1*

Laser-ablation sector-field ICP-MS U-Pb geochronology extension of the base TAPP definition, generated from TAPPS20260813/Current TAPPs/LA-SF-ICP-MS_UPb_TAPP_v17.csv via the path-driven pipeline.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### laSficpmsUPbTAPP example Zhang2022
laSficpmsUPbTAPP instance derived from Zhang et al. 2022 (GCA 323) Iron meteorites Raster mapping + Spot (Ge) ns-LA-SF-ICP-MS Florida State University.
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
  "@id": "ex:laSficpmsUPbTAPP-Zhang2022",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Zhang et al. (2022) Iron Meteorite LA-ICP-MS v1",
  "schema:description": "Raster scans used for main element dataset (23 elements); separate spot analyses on 5 irons for more precise Ge abundances (150 µm spot, 50 Hz, 20 s); two different analysis modes represent distinct protocols but are reported in same paper Reported detail: ada:ablationSamplingMode = Raster area (2D mapping) for most irons; Spot (stationary) for Ge analysis on 5 irons.",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-ICP-MS",
      "schema:name": "LA-SF-ICP-MS"
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
            "Iron meteorite metal (kamacite + taenite); pyroxene-bearing pallasite metal"
          ]
        },
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleFormAnalyticalSubstrateDefault",
          "schema:name": "Sample Form / Analytical Substrate",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Polished metal slab (in situ)"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished metal slabs and thin sections; no acid treatment described",
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
            "@id": "ada:parameter/laSficpmsUPbTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "pulseAnalogDetectorNonlinearityCorrectionDefault",
            "schema:name": "Pulse/Analog Detector Nonlinearity Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Applied: triple mode detection at 65% duty cycle (pulse counting + analog + Faraday); specific cross-calibration not described"
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
        "schema:name": "ESI New Wave UP193FX (193 nm Nd:YAG frequency-quintupled solid state)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserSpotGeometryDefault": "Raster: 50 µm circular beam spot; Spot (Ge): 150 µm circular",
      "ada:laserRepetitionRateDefault": "Raster: 50 Hz; Spot (Ge): 50 Hz",
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
        "schema:name": "Thermo Fisher Scientific Element XR (SF-ICP-MS)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/massResolutionSettingDefault",
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
          "@id": "ada:parameter/laSficpmsUPbTAPP/detectorConfiguration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laSficpmsUPbTAPP/detectorConfiguration"
            }
          ],
          "schema:name": "Detector Configuration",
          "schema:value": "Triple mode detection (pulse counting + analog + Faraday) at 65% duty cycle"
        }
      ],
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
  "ada:ablationSamplingMode": [
    "Spot (stationary)"
  ],
  "ada:ablationSpotDurationDefault": "N/A (raster) / 20 s (spot Ge at 50 Hz)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSizeDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "transectRateMappingRateOrStepSizeDefault",
      "schema:name": "Transect Rate, Mapping Rate or Step Size",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "10 µm s⁻¹ (raster scan); N/A (spot Ge)"
    },
    {
      "@id": "ada:parameter/laSficpmsUPbTAPP/uncertaintyPropagationMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "uncertaintyPropagationMethodDefault",
      "schema:name": "Uncertainty Propagation Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Standard deviation (SD) across individual integration cycles of raster scans; uncertainty propagation not formally described"
    }
  ],
  "ada:analysisSequenceDefault": "Standards at start of session → raster unknowns → repeat → standards at end; separate session for Ge spot analyses",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "³¹P",
      "⁵¹V",
      "⁵³Cr",
      "⁵⁵Mn",
      "⁵⁷Fe",
      "⁵⁹Co",
      "⁶⁰Ni",
      "⁶³Cu",
      "⁷¹Ga",
      "⁷⁴Ge",
      "⁷⁵As",
      "⁹⁵Mo",
      "¹⁰²Ru",
      "¹⁰³Rh",
      "¹⁰⁶Pd",
      "¹²⁰Sn",
      "¹²¹Sb",
      "¹⁸²W",
      "¹⁸⁵Re",
      "¹⁹⁰Os",
      "¹⁹³Ir",
      "¹⁹⁵Pt",
      "¹⁹⁷Au (23 elements; 31P, 51V, 53Cr, 55Mn, 57Fe, 59Co, 60Ni, 63Cu, 71Ga for spot Ge runs)"
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
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/monitoredIsotopes",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredIsotopes",
        "schema:name": "Monitored Isotopes",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "boolean",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/normalizationStandardsBasedCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "normalizationStandardsBasedCorrection",
        "schema:name": "Normalization / Standards-Based Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "uri",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "uri"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/massResolutionPerAnalyte",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionPerAnalyte",
        "schema:name": "Mass Resolution per Analyte",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:internalStandardApproach": "Standardization techniques followed those of Humayun (2012) [Section 2.2; specific IS approach not restated in this paper]",
  "ada:elementalFractionationCorrection": [
    "Multi-point external calibration using series of iron meteorite reference materials (North Chile Filomena as primary standard for Fe/Co/Ni/Cu/Ga/Ge/As/W/Au; Hoba for Ru/Rh/Pd/Re/Os/Ir/Pt; NIST SRM 1263a V-Cr steel for V/Cr/Fe/Co/Ni/Cu/As/Mo/W/Au)"
  ],
  "ada:blankBackgroundCorrectionMethod": "Gas blank measured before each raster analysis; mean background subtracted",
  "ada:primaryStandardNameDefault": "North Chile Filomena (IIAB iron meteorite; Wasson et al. 1989) for Fe/Co/Ni/Cu/Ga/Ge/As/W/Au; Hoba (IVB; Walker et al. 2008) for Ru/Rh/Pd/Re/Os/Ir/Pt; NIST SRM 1263a V-Cr steel (Campbell & Humayun 2005) for V/Cr/Fe/Co/Ni/Cu/As/Mo/W/Au",
  "ada:calibrationMeasurementFrequency": "Standards at start and end of session; external bracketing",
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ageModelDefault": "missing",
  "ada:backgroundCountTimeDefault": -9999,
  "ada:carrierGasFlowRateDefault": "missing",
  "ada:inheritedOrInitialSignalCorrectionDefault": "missing",
  "ada:internalStandardElement": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:massResolutionAssignment": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
  "ada:signalIntegrationIntervalMethod": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS-UPb/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:laSficpmsUPbTAPP-Zhang2022",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Zhang et al. (2022) Iron Meteorite LA-ICP-MS v1",
  "schema:description": "Raster scans used for main element dataset (23 elements); separate spot analyses on 5 irons for more precise Ge abundances (150 \u00b5m spot, 50 Hz, 20 s); two different analysis modes represent distinct protocols but are reported in same paper Reported detail: ada:ablationSamplingMode = Raster area (2D mapping) for most irons; Spot (stationary) for Ge analysis on 5 irons.",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-ICP-MS",
      "schema:name": "LA-SF-ICP-MS"
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
            "Iron meteorite metal (kamacite + taenite); pyroxene-bearing pallasite metal"
          ]
        },
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleFormAnalyticalSubstrateDefault",
          "schema:name": "Sample Form / Analytical Substrate",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Polished metal slab (in situ)"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished metal slabs and thin sections; no acid treatment described",
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
            "@id": "ada:parameter/laSficpmsUPbTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "pulseAnalogDetectorNonlinearityCorrectionDefault",
            "schema:name": "Pulse/Analog Detector Nonlinearity Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Applied: triple mode detection at 65% duty cycle (pulse counting + analog + Faraday); specific cross-calibration not described"
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
        "schema:name": "ESI New Wave UP193FX (193 nm Nd:YAG frequency-quintupled solid state)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserSpotGeometryDefault": "Raster: 50 \u00b5m circular beam spot; Spot (Ge): 150 \u00b5m circular",
      "ada:laserRepetitionRateDefault": "Raster: 50 Hz; Spot (Ge): 50 Hz",
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
        "schema:name": "Thermo Fisher Scientific Element XR (SF-ICP-MS)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/massResolutionSettingDefault",
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
          "@id": "ada:parameter/laSficpmsUPbTAPP/detectorConfiguration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laSficpmsUPbTAPP/detectorConfiguration"
            }
          ],
          "schema:name": "Detector Configuration",
          "schema:value": "Triple mode detection (pulse counting + analog + Faraday) at 65% duty cycle"
        }
      ],
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
  "ada:ablationSamplingMode": [
    "Spot (stationary)"
  ],
  "ada:ablationSpotDurationDefault": "N/A (raster) / 20 s (spot Ge at 50 Hz)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSizeDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "transectRateMappingRateOrStepSizeDefault",
      "schema:name": "Transect Rate, Mapping Rate or Step Size",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "10 \u00b5m s\u207b\u00b9 (raster scan); N/A (spot Ge)"
    },
    {
      "@id": "ada:parameter/laSficpmsUPbTAPP/uncertaintyPropagationMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "uncertaintyPropagationMethodDefault",
      "schema:name": "Uncertainty Propagation Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Standard deviation (SD) across individual integration cycles of raster scans; uncertainty propagation not formally described"
    }
  ],
  "ada:analysisSequenceDefault": "Standards at start of session \u2192 raster unknowns \u2192 repeat \u2192 standards at end; separate session for Ge spot analyses",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "\u00b3\u00b9P",
      "\u2075\u00b9V",
      "\u2075\u00b3Cr",
      "\u2075\u2075Mn",
      "\u2075\u2077Fe",
      "\u2075\u2079Co",
      "\u2076\u2070Ni",
      "\u2076\u00b3Cu",
      "\u2077\u00b9Ga",
      "\u2077\u2074Ge",
      "\u2077\u2075As",
      "\u2079\u2075Mo",
      "\u00b9\u2070\u00b2Ru",
      "\u00b9\u2070\u00b3Rh",
      "\u00b9\u2070\u2076Pd",
      "\u00b9\u00b2\u2070Sn",
      "\u00b9\u00b2\u00b9Sb",
      "\u00b9\u2078\u00b2W",
      "\u00b9\u2078\u2075Re",
      "\u00b9\u2079\u2070Os",
      "\u00b9\u2079\u00b3Ir",
      "\u00b9\u2079\u2075Pt",
      "\u00b9\u2079\u2077Au (23 elements; 31P, 51V, 53Cr, 55Mn, 57Fe, 59Co, 60Ni, 63Cu, 71Ga for spot Ge runs)"
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
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/monitoredIsotopes",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredIsotopes",
        "schema:name": "Monitored Isotopes",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "boolean",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/normalizationStandardsBasedCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "normalizationStandardsBasedCorrection",
        "schema:name": "Normalization / Standards-Based Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "uri",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "uri"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/massResolutionPerAnalyte",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionPerAnalyte",
        "schema:name": "Mass Resolution per Analyte",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:internalStandardApproach": "Standardization techniques followed those of Humayun (2012) [Section 2.2; specific IS approach not restated in this paper]",
  "ada:elementalFractionationCorrection": [
    "Multi-point external calibration using series of iron meteorite reference materials (North Chile Filomena as primary standard for Fe/Co/Ni/Cu/Ga/Ge/As/W/Au; Hoba for Ru/Rh/Pd/Re/Os/Ir/Pt; NIST SRM 1263a V-Cr steel for V/Cr/Fe/Co/Ni/Cu/As/Mo/W/Au)"
  ],
  "ada:blankBackgroundCorrectionMethod": "Gas blank measured before each raster analysis; mean background subtracted",
  "ada:primaryStandardNameDefault": "North Chile Filomena (IIAB iron meteorite; Wasson et al. 1989) for Fe/Co/Ni/Cu/Ga/Ge/As/W/Au; Hoba (IVB; Walker et al. 2008) for Ru/Rh/Pd/Re/Os/Ir/Pt; NIST SRM 1263a V-Cr steel (Campbell & Humayun 2005) for V/Cr/Fe/Co/Ni/Cu/As/Mo/W/Au",
  "ada:calibrationMeasurementFrequency": "Standards at start and end of session; external bracketing",
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ageModelDefault": "missing",
  "ada:backgroundCountTimeDefault": -9999,
  "ada:carrierGasFlowRateDefault": "missing",
  "ada:inheritedOrInitialSignalCorrectionDefault": "missing",
  "ada:internalStandardElement": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:massResolutionAssignment": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
  "ada:signalIntegrationIntervalMethod": "missing",
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

ex:laSficpmsUPbTAPP-Zhang2022 a cdi:Activity,
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
                    schema1:description "Polished metal slabs and thin sections; no acid treatment described" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSizeDefault>,
        <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/uncertaintyPropagationMethodDefault> ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Zhang, Chabot, Rubin, Humayun et al." ] ;
    schema1:datePublished "missing" ;
    schema1:description "Raster scans used for main element dataset (23 elements); separate spot analyses on 5 irons for more precise Ge abundances (150 µm spot, 50 Hz, 20 s); two different analysis modes represent distinct protocols but are reported in same paper Reported detail: ada:ablationSamplingMode = Raster area (2D mapping) for most irons; Spot (stationary) for Ge analysis on 5 irons." ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "Laser Ablation System" ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "ESI New Wave UP193FX (193 nm Nd:YAG frequency-quintupled solid state)" ] ;
            schema1:name "example instrumentName" ;
            ada:laserRepetitionRateDefault "Raster: 50 Hz; Spot (Ge): 50 Hz" ;
            ada:laserSpotGeometryDefault "Raster: 50 µm circular beam spot; Spot (Ge): 150 µm circular" ],
        [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/detectorConfiguration>,
                <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/massResolutionSettingDefault> ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "ICPMS" ;
            schema1:hasPart [ a schema1:Product,
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
                        "Interface Cone" ;
                    schema1:name "missing" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "Thermo Fisher Scientific Element XR (SF-ICP-MS)" ] ;
            schema1:name "example instrumentName" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "Plasma Analytical Facility, Florida State University, Tallahassee FL, USA" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "LA-SF-ICP-MS" ;
            schema1:termCode "LA-ICP-MS" ] ;
    schema1:name "Zhang et al. (2022) Iron Meteorite LA-ICP-MS v1" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Iron meteorite metal (kamacite + taenite); pyroxene-bearing pallasite metal" ],
                <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Zhang et al. (2022) GCA 323, 202–219; Humayun (2012) for standardization" ] ;
            schema1:url "https://ada.astromat.org/missing" ],
        [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "Quantitative analysis, mixed WDS/EDS element mapping, and characterization of mineral phases from NWA 1911 and Zinder [Section 2.5]" ;
                    schema1:name "EPMA (Brown University CAMECA SX-100)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:ablationPitDepthRateDefault "missing" ;
    ada:ablationSamplingMode "Spot (stationary)" ;
    ada:ablationSpotDurationDefault "N/A (raster) / 20 s (spot Ge at 50 Hz)" ;
    ada:ageModelDefault "missing" ;
    ada:analysisSequenceDefault "Standards at start of session → raster unknowns → repeat → standards at end; separate session for Ge spot analyses" ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/detectionLimit>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/detectionLimitMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/isobaricInterferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/limitOfQuantificationMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/massResolutionPerAnalyte>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/monitoredIsotopes>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/normalizationStandardsBasedCorrection>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ;
            ada:defaultAnalytes "³¹P",
                "¹²¹Sb",
                "¹²⁰Sn",
                "¹⁰²Ru",
                "¹⁰³Rh",
                "¹⁰⁶Pd",
                "¹⁸²W",
                "¹⁸⁵Re",
                "¹⁹³Ir",
                "¹⁹⁰Os",
                "¹⁹⁵Pt",
                "¹⁹⁷Au (23 elements; 31P, 51V, 53Cr, 55Mn, 57Fe, 59Co, 60Ni, 63Cu, 71Ga for spot Ge runs)",
                "⁵³Cr",
                "⁵¹V",
                "⁵⁵Mn",
                "⁵⁷Fe",
                "⁵⁹Co",
                "⁶³Cu",
                "⁶⁰Ni",
                "⁷¹Ga",
                "⁷⁴Ge",
                "⁷⁵As",
                "⁹⁵Mo" ] ;
    ada:backgroundCountTimeDefault -9999 ;
    ada:blankBackgroundCorrectionMethod "Gas blank measured before each raster analysis; mean background subtracted" ;
    ada:calibrationMeasurementFrequency "Standards at start and end of session; external bracketing" ;
    ada:carrierGasFlowRateDefault "missing" ;
    ada:elementalFractionationCorrection "Multi-point external calibration using series of iron meteorite reference materials (North Chile Filomena as primary standard for Fe/Co/Ni/Cu/Ga/Ge/As/W/Au; Hoba for Ru/Rh/Pd/Re/Os/Ir/Pt; NIST SRM 1263a V-Cr steel for V/Cr/Fe/Co/Ni/Cu/As/Mo/W/Au)" ;
    ada:inheritedOrInitialSignalCorrectionDefault "missing" ;
    ada:internalStandardApproach "Standardization techniques followed those of Humayun (2012) [Section 2.2; specific IS approach not restated in this paper]" ;
    ada:internalStandardElement "missing" ;
    ada:ionCounterDeadTimeDefault -9999 ;
    ada:massBiasCorrectionStrategy "missing" ;
    ada:massResolutionAssignment "missing" ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:primaryStandardNameDefault "North Chile Filomena (IIAB iron meteorite; Wasson et al. 1989) for Fe/Co/Ni/Cu/Ga/Ge/As/W/Au; Hoba (IVB; Walker et al. 2008) for Ru/Rh/Pd/Re/Os/Ir/Pt; NIST SRM 1263a V-Cr steel (Campbell & Humayun 2005) for V/Cr/Fe/Co/Ni/Cu/As/Mo/W/Au" ;
    ada:rasterLineSpacingDefault "missing" ;
    ada:sampleIntroduction "missing" ;
    ada:samplingUnit "missing" ;
    ada:signalIntegrationIntervalMethod "missing" ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:totalIntegrationTimePerOutputDataPointDefault "missing" ;
    ada:uncertaintyLevel "missing" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/detectionLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimit" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/detectionLimitMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Detection Limit Method" ;
    schema1:valueName "detectionLimitMethod" ;
    ada:dataType "uri" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/isobaricInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Isobaric Interference Corrections Applied" ;
    schema1:valueName "isobaricInterferenceCorrectionsApplied" ;
    ada:dataType "boolean" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "uri" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/massResolutionPerAnalyte> a schema1:PropertyValueSpecification ;
    schema1:name "Mass Resolution per Analyte" ;
    schema1:valueName "massResolutionPerAnalyte" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/monitoredIsotopes> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Monitored Isotopes" ;
    schema1:valueName "monitoredIsotopes" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/normalizationStandardsBasedCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Normalization / Standards-Based Correction" ;
    schema1:valueName "normalizationStandardsBasedCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/massResolutionSettingDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Low resolution (M/ΔM ≈ 400)" ;
    schema1:name "Mass Resolution Setting" ;
    schema1:valueName "massResolutionSettingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Applied: triple mode detection at 65% duty cycle (pulse counting + analog + Faraday); specific cross-calibration not described" ;
    schema1:name "Pulse/Analog Detector Nonlinearity Correction" ;
    schema1:valueName "pulseAnalogDetectorNonlinearityCorrectionDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Polished metal slab (in situ)" ;
    schema1:name "Sample Form / Analytical Substrate" ;
    schema1:valueName "sampleFormAnalyticalSubstrateDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSizeDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "10 µm s⁻¹ (raster scan); N/A (spot Ge)" ;
    schema1:name "Transect Rate, Mapping Rate or Step Size" ;
    schema1:valueName "transectRateMappingRateOrStepSizeDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/uncertaintyPropagationMethodDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Standard deviation (SD) across individual integration cycles of raster scans; uncertainty propagation not formally described" ;
    schema1:name "Uncertainty Propagation Method" ;
    schema1:valueName "uncertaintyPropagationMethodDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/detectorConfiguration> a schema1:PropertyValue ;
    schema1:name "Detector Configuration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/detectorConfiguration> ;
    schema1:value "Triple mode detection (pulse counting + analog + Faraday) at 65% duty cycle" .


```


### laSficpmsUPbTAPP example Chernonozhkin2021
laSficpmsUPbTAPP instance derived from Chernonozhkin et al. 2021 (Chem Geol 562) Pallasite olivine Raster mapping (2D) ns-LA-SF-ICP-MS Ghent University.
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
  "@id": "ex:laSficpmsUPbTAPP-Chernonozhkin2021",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Chernonozhkin et al. (2021) Pallasite Olivine 2D Mapping v1",
  "schema:description": "Pallasite olivine 2D mapping in cool plasma mode (800 W) is a core methodological innovation; total of 8 PMG meteorites mapped; P-rich veinlets excluded from olivine averages; Fa# values verified against EMPA (Fig. 5A)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-ICP-MS",
      "schema:name": "LA-SF-ICP-MS"
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
      "schema:name": "Planet Topers (BELSPO Interuniversity Attraction Poles); FWO postdoctoral fellowship for SCh; FWO \"Excellence of Science\" (ET-HoME ID 30442502); FWO/BOF-UGent; Alexander von Humboldt Foundation; FWO/BELSPO/VUB for SG and PC"
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
            "Pallasite olivine ([Mg,Fe]₂SiO₄)"
          ]
        },
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleFormAnalyticalSubstrateDefault",
          "schema:name": "Sample Form / Analytical Substrate",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "In situ — polished epoxy thick section (HELEX II two-volume cell)"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "PMG thick sections polished; HELEX II two-volume cell; C-coated for SEM then coating removed before LA",
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
            "@id": "ada:parameter/laSficpmsUPbTAPP/signalSmoothingDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "signalSmoothingDefault",
            "schema:name": "Signal Smoothing",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "None (no signal smoothing device; N₂ not added)"
          },
          {
            "@id": "ada:parameter/laSficpmsUPbTAPP/spikeOutlierFilteringApproachDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "spikeOutlierFilteringApproachDefault",
            "schema:name": "Spike / Outlier Filtering Approach",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Manual identification and exclusion of P-rich veinlet pixels from olivine averages; anomalous spikes from inclusions excluded per line"
          },
          {
            "@id": "ada:parameter/laSficpmsUPbTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "pulseAnalogDetectorNonlinearityCorrectionDefault",
            "schema:name": "Pulse/Analog Detector Nonlinearity Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Applied: triple mode detection; cross-calibration between pulse-counting and analog modes performed"
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
        "schema:name": "Teledyne CETAC Technologies Analyte G2 (193 nm ArF excimer)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "193 nm ArF excimer; pulse duration ~5 ns",
      "schema:name": "HELEX II two-volume ablation cell",
      "ada:laserSpotGeometryDefault": "20×20 µm square",
      "ada:laserFluenceDefault": "5–7 J cm⁻²",
      "ada:laserRepetitionRateDefault": "20 Hz",
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/laserPulseDuration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laSficpmsUPbTAPP/laserPulseDuration"
            }
          ],
          "schema:name": "Laser Pulse Duration",
          "schema:value": "~5 ns (ArF excimer)"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ]
    },
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
              "@id": "ada:parameter/laSficpmsUPbTAPP/interfaceConeConfiguration",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/laSficpmsUPbTAPP/interfaceConeConfiguration"
                }
              ],
              "schema:name": "Interface Cone Configuration",
              "schema:value": "Al standard sample cone (1.1 mm aperture); Al H-type skimmer (0.8 mm aperture)"
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
              "@id": "ada:parameter/laSficpmsUPbTAPP/coolantGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantGasFlowRateDefault",
              "schema:name": "Coolant (Plasma) Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 15,
              "schema:description": "Cool: 15 l min⁻¹ Ar; Auxiliary: 0.81 l min⁻¹ (mapping)"
            },
            {
              "@id": "ada:parameter/laSficpmsUPbTAPP/rfPowerDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "rfPowerDefault",
              "schema:name": "RF Power",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 800,
              "schema:description": "800 W (cool plasma for mapping)"
            },
            {
              "@id": "ada:parameter/laSficpmsUPbTAPP/plasmaThermalMode",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/laSficpmsUPbTAPP/plasmaThermalMode"
                }
              ],
              "schema:name": "Plasma Thermal Mode",
              "schema:value": "Cool plasma (800 W RF) to reduce Ar-based argide interferences on ⁶⁰Ni and ⁷¹Ga"
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
          "@id": "ada:parameter/laSficpmsUPbTAPP/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Low resolution (M/ΔM = 300; cool plasma mapping)"
        },
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/detectorConfiguration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laSficpmsUPbTAPP/detectorConfiguration"
            }
          ],
          "schema:name": "Detector Configuration",
          "schema:value": "Triple mode detection (all analytical modes)"
        },
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/icpTuningDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "icpTuningDefault",
          "schema:name": "ICP Tuning",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Daily tuning; cool plasma conditions optimized; N₂ explicitly not added to avoid N-based interferences"
        },
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Gas blank measured before each ablation line; adequate washout ensured by duty cycle timing"
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
      "schema:name": "In-house MatLab script (Appendix C1)"
    }
  ],
  "ada:ablationSamplingMode": [
    "Raster area (2D elemental mapping)"
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSizeDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "transectRateMappingRateOrStepSizeDefault",
      "schema:name": "Transect Rate, Mapping Rate or Step Size",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "9 µm s⁻¹ (continuous raster)"
    },
    {
      "@id": "ada:parameter/laSficpmsUPbTAPP/plasmaMakeUpGasAdditionDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "plasmaMakeUpGasAdditionDefault",
      "schema:name": "Plasma / Make-up Gas Addition",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Ar make-up: 0.81–0.99 l min⁻¹ (mapping); N₂ explicitly not added"
    },
    {
      "@id": "ada:parameter/laSficpmsUPbTAPP/uncertaintyPropagationMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "uncertaintyPropagationMethodDefault",
      "schema:name": "Uncertainty Propagation Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Longerich et al. (1996) equation (3SD/S × √(1/Nb + 1/Na))"
    }
  ],
  "ada:rasterLineSpacingDefault": "20 µm (contiguous; 20×20 µm square spot = line spacing equals spot width)",
  "ada:carrierGasFlowRateDefault": "He: MFC-1 (cell) 0.200–0.260 l min⁻¹; MFC-2 (cup) 0.220–0.385 l min⁻¹",
  "ada:oxideProductionMethodAndThreshold": "ThO⁺/Th⁺ (mass 248/232); threshold not explicitly stated but minimized by cool plasma",
  "ada:analysisSequenceDefault": "(i) Gas blanks → (ii) all glass GRMs for external calibration → (iii) 1–3 cosmic spherule unknowns → (iv) blanks → (v) all glass GRMs again",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "²⁵Mg",
      "²⁷Al",
      "²⁹Si",
      "³¹P",
      "⁴⁵Sc",
      "⁵¹V",
      "⁵³Cr",
      "⁵⁵Mn",
      "⁵⁷Fe",
      "⁶⁰Ni",
      "⁷¹Ga",
      "¹³⁹La",
      "¹⁵³Eu",
      "¹⁹⁵Pt (14 nuclides)"
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
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/monitoredIsotopes",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredIsotopes",
        "schema:name": "Monitored Isotopes",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "boolean",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/normalizationStandardsBasedCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "normalizationStandardsBasedCorrection",
        "schema:name": "Normalization / Standards-Based Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "uri",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "uri"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/massResolutionPerAnalyte",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionPerAnalyte",
        "schema:name": "Mass Resolution per Analyte",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:backgroundCountTimeDefault": "Scans for gas blank: 10 per line (before each mapping line); 80 scans during ablation",
  "ada:internalStandardApproach": "Sum-of-major-oxide normalization: MgO+FeO+SiO₂+P₂O₅ = 100 wt% per pixel (Liu et al. 2008 approach; no EPMA required for IS)",
  "ada:internalStandardElement": "No single IS element; oxide sum normalization (MgO+FeO+SiO₂+P₂O₅) used as virtual IS per pixel",
  "ada:elementalFractionationCorrection": [
    "Internal normalization to MgO+FeO+SiO₂+P₂O₅ oxide sum corrects for point-to-point ablation yield variation; additional pixel-by-pixel normalization fixes oxide sum to 100 wt%"
  ],
  "ada:signalIntegrationIntervalMethod": "Manual visual inspection of time-resolved signal per line; anomalous spikes (inclusions, cracks, veinlets) excluded; P-rich veinlet regions identified and excluded from olivine averages",
  "ada:blankBackgroundCorrectionMethod": "Gas blank measured before each ablation line (10 scans of gas blank per mapping line); average background subtracted from each corresponding ablation line",
  "ada:primaryStandardNameDefault": "Multiple glass GRMs used together for linear regression external calibration: NIST SRM 612, NIST SRM 614, USGS GSD-1G (synthetic), USGS GSE-1G (synthetic), USGS BHVO-2G, USGS BIR-1G (natural basalt glasses)",
  "ada:calibrationMeasurementFrequency": "Each GRM analyzed 3–5× before and 3–5× after sample analyses (all GRMs at start and end of session)",
  "ada:secondaryReferenceMaterialDefault": [
    "MPI-DING glasses: GOR132-G, StHs6/80-G, T1-G; USGS: BCR-2G, BHVO-2G — measured as unknowns alongside samples and compared to GeoReM preferred values (Table 1 and Section 3.3)"
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ablationSpotDurationDefault": -9999,
  "ada:ageModelDefault": "missing",
  "ada:inheritedOrInitialSignalCorrectionDefault": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:massResolutionAssignment": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS-UPb/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:laSficpmsUPbTAPP-Chernonozhkin2021",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Chernonozhkin et al. (2021) Pallasite Olivine 2D Mapping v1",
  "schema:description": "Pallasite olivine 2D mapping in cool plasma mode (800 W) is a core methodological innovation; total of 8 PMG meteorites mapped; P-rich veinlets excluded from olivine averages; Fa# values verified against EMPA (Fig. 5A)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-ICP-MS",
      "schema:name": "LA-SF-ICP-MS"
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
      "schema:name": "Planet Topers (BELSPO Interuniversity Attraction Poles); FWO postdoctoral fellowship for SCh; FWO \"Excellence of Science\" (ET-HoME ID 30442502); FWO/BOF-UGent; Alexander von Humboldt Foundation; FWO/BELSPO/VUB for SG and PC"
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
            "Pallasite olivine ([Mg,Fe]\u2082SiO\u2084)"
          ]
        },
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleFormAnalyticalSubstrateDefault",
          "schema:name": "Sample Form / Analytical Substrate",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "In situ \u2014 polished epoxy thick section (HELEX II two-volume cell)"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "PMG thick sections polished; HELEX II two-volume cell; C-coated for SEM then coating removed before LA",
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
            "@id": "ada:parameter/laSficpmsUPbTAPP/signalSmoothingDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "signalSmoothingDefault",
            "schema:name": "Signal Smoothing",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "None (no signal smoothing device; N\u2082 not added)"
          },
          {
            "@id": "ada:parameter/laSficpmsUPbTAPP/spikeOutlierFilteringApproachDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "spikeOutlierFilteringApproachDefault",
            "schema:name": "Spike / Outlier Filtering Approach",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Manual identification and exclusion of P-rich veinlet pixels from olivine averages; anomalous spikes from inclusions excluded per line"
          },
          {
            "@id": "ada:parameter/laSficpmsUPbTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "pulseAnalogDetectorNonlinearityCorrectionDefault",
            "schema:name": "Pulse/Analog Detector Nonlinearity Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Applied: triple mode detection; cross-calibration between pulse-counting and analog modes performed"
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
        "schema:name": "Teledyne CETAC Technologies Analyte G2 (193 nm ArF excimer)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "193 nm ArF excimer; pulse duration ~5 ns",
      "schema:name": "HELEX II two-volume ablation cell",
      "ada:laserSpotGeometryDefault": "20\u00d720 \u00b5m square",
      "ada:laserFluenceDefault": "5\u20137 J cm\u207b\u00b2",
      "ada:laserRepetitionRateDefault": "20 Hz",
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/laserPulseDuration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laSficpmsUPbTAPP/laserPulseDuration"
            }
          ],
          "schema:name": "Laser Pulse Duration",
          "schema:value": "~5 ns (ArF excimer)"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ]
    },
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
              "@id": "ada:parameter/laSficpmsUPbTAPP/interfaceConeConfiguration",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/laSficpmsUPbTAPP/interfaceConeConfiguration"
                }
              ],
              "schema:name": "Interface Cone Configuration",
              "schema:value": "Al standard sample cone (1.1 mm aperture); Al H-type skimmer (0.8 mm aperture)"
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
              "@id": "ada:parameter/laSficpmsUPbTAPP/coolantGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantGasFlowRateDefault",
              "schema:name": "Coolant (Plasma) Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 15,
              "schema:description": "Cool: 15 l min\u207b\u00b9 Ar; Auxiliary: 0.81 l min\u207b\u00b9 (mapping)"
            },
            {
              "@id": "ada:parameter/laSficpmsUPbTAPP/rfPowerDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "rfPowerDefault",
              "schema:name": "RF Power",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 800,
              "schema:description": "800 W (cool plasma for mapping)"
            },
            {
              "@id": "ada:parameter/laSficpmsUPbTAPP/plasmaThermalMode",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/laSficpmsUPbTAPP/plasmaThermalMode"
                }
              ],
              "schema:name": "Plasma Thermal Mode",
              "schema:value": "Cool plasma (800 W RF) to reduce Ar-based argide interferences on \u2076\u2070Ni and \u2077\u00b9Ga"
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
          "@id": "ada:parameter/laSficpmsUPbTAPP/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Low resolution (M/\u0394M = 300; cool plasma mapping)"
        },
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/detectorConfiguration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laSficpmsUPbTAPP/detectorConfiguration"
            }
          ],
          "schema:name": "Detector Configuration",
          "schema:value": "Triple mode detection (all analytical modes)"
        },
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/icpTuningDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "icpTuningDefault",
          "schema:name": "ICP Tuning",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Daily tuning; cool plasma conditions optimized; N\u2082 explicitly not added to avoid N-based interferences"
        },
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Gas blank measured before each ablation line; adequate washout ensured by duty cycle timing"
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
      "schema:name": "In-house MatLab script (Appendix C1)"
    }
  ],
  "ada:ablationSamplingMode": [
    "Raster area (2D elemental mapping)"
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSizeDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "transectRateMappingRateOrStepSizeDefault",
      "schema:name": "Transect Rate, Mapping Rate or Step Size",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "9 \u00b5m s\u207b\u00b9 (continuous raster)"
    },
    {
      "@id": "ada:parameter/laSficpmsUPbTAPP/plasmaMakeUpGasAdditionDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "plasmaMakeUpGasAdditionDefault",
      "schema:name": "Plasma / Make-up Gas Addition",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Ar make-up: 0.81\u20130.99 l min\u207b\u00b9 (mapping); N\u2082 explicitly not added"
    },
    {
      "@id": "ada:parameter/laSficpmsUPbTAPP/uncertaintyPropagationMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "uncertaintyPropagationMethodDefault",
      "schema:name": "Uncertainty Propagation Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Longerich et al. (1996) equation (3SD/S \u00d7 \u221a(1/Nb + 1/Na))"
    }
  ],
  "ada:rasterLineSpacingDefault": "20 \u00b5m (contiguous; 20\u00d720 \u00b5m square spot = line spacing equals spot width)",
  "ada:carrierGasFlowRateDefault": "He: MFC-1 (cell) 0.200\u20130.260 l min\u207b\u00b9; MFC-2 (cup) 0.220\u20130.385 l min\u207b\u00b9",
  "ada:oxideProductionMethodAndThreshold": "ThO\u207a/Th\u207a (mass 248/232); threshold not explicitly stated but minimized by cool plasma",
  "ada:analysisSequenceDefault": "(i) Gas blanks \u2192 (ii) all glass GRMs for external calibration \u2192 (iii) 1\u20133 cosmic spherule unknowns \u2192 (iv) blanks \u2192 (v) all glass GRMs again",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "\u00b2\u2075Mg",
      "\u00b2\u2077Al",
      "\u00b2\u2079Si",
      "\u00b3\u00b9P",
      "\u2074\u2075Sc",
      "\u2075\u00b9V",
      "\u2075\u00b3Cr",
      "\u2075\u2075Mn",
      "\u2075\u2077Fe",
      "\u2076\u2070Ni",
      "\u2077\u00b9Ga",
      "\u00b9\u00b3\u2079La",
      "\u00b9\u2075\u00b3Eu",
      "\u00b9\u2079\u2075Pt (14 nuclides)"
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
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/monitoredIsotopes",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredIsotopes",
        "schema:name": "Monitored Isotopes",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "boolean",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/normalizationStandardsBasedCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "normalizationStandardsBasedCorrection",
        "schema:name": "Normalization / Standards-Based Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "uri",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "uri"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/massResolutionPerAnalyte",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionPerAnalyte",
        "schema:name": "Mass Resolution per Analyte",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:backgroundCountTimeDefault": "Scans for gas blank: 10 per line (before each mapping line); 80 scans during ablation",
  "ada:internalStandardApproach": "Sum-of-major-oxide normalization: MgO+FeO+SiO\u2082+P\u2082O\u2085 = 100 wt% per pixel (Liu et al. 2008 approach; no EPMA required for IS)",
  "ada:internalStandardElement": "No single IS element; oxide sum normalization (MgO+FeO+SiO\u2082+P\u2082O\u2085) used as virtual IS per pixel",
  "ada:elementalFractionationCorrection": [
    "Internal normalization to MgO+FeO+SiO\u2082+P\u2082O\u2085 oxide sum corrects for point-to-point ablation yield variation; additional pixel-by-pixel normalization fixes oxide sum to 100 wt%"
  ],
  "ada:signalIntegrationIntervalMethod": "Manual visual inspection of time-resolved signal per line; anomalous spikes (inclusions, cracks, veinlets) excluded; P-rich veinlet regions identified and excluded from olivine averages",
  "ada:blankBackgroundCorrectionMethod": "Gas blank measured before each ablation line (10 scans of gas blank per mapping line); average background subtracted from each corresponding ablation line",
  "ada:primaryStandardNameDefault": "Multiple glass GRMs used together for linear regression external calibration: NIST SRM 612, NIST SRM 614, USGS GSD-1G (synthetic), USGS GSE-1G (synthetic), USGS BHVO-2G, USGS BIR-1G (natural basalt glasses)",
  "ada:calibrationMeasurementFrequency": "Each GRM analyzed 3\u20135\u00d7 before and 3\u20135\u00d7 after sample analyses (all GRMs at start and end of session)",
  "ada:secondaryReferenceMaterialDefault": [
    "MPI-DING glasses: GOR132-G, StHs6/80-G, T1-G; USGS: BCR-2G, BHVO-2G \u2014 measured as unknowns alongside samples and compared to GeoReM preferred values (Table 1 and Section 3.3)"
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ablationSpotDurationDefault": -9999,
  "ada:ageModelDefault": "missing",
  "ada:inheritedOrInitialSignalCorrectionDefault": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:massResolutionAssignment": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
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

ex:laSficpmsUPbTAPP-Chernonozhkin2021 a cdi:Activity,
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
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault>,
                        <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/signalSmoothingDefault>,
                        <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/spikeOutlierFilteringApproachDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "PMG thick sections polished; HELEX II two-volume cell; C-coated for SEM then coating removed before LA" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/plasmaMakeUpGasAdditionDefault>,
        <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSizeDefault>,
        <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/uncertaintyPropagationMethodDefault> ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Chernonozhkin, Pittarello, Goderis, Vanhaecke et al." ] ;
    schema1:datePublished "missing" ;
    schema1:description "Pallasite olivine 2D mapping in cool plasma mode (800 W) is a core methodological innovation; total of 8 PMG meteorites mapped; P-rich veinlets excluded from olivine averages; Fa# values verified against EMPA (Fig. 5A)" ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "Planet Topers (BELSPO Interuniversity Attraction Poles); FWO postdoctoral fellowship for SCh; FWO \"Excellence of Science\" (ET-HoME ID 30442502); FWO/BOF-UGent; Alexander von Humboldt Foundation; FWO/BELSPO/VUB for SG and PC" ] ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/detectorConfiguration>,
                <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/icpTuningDefault>,
                <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/massResolutionSettingDefault>,
                <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/memoryEffectMitigationDefault> ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "Double-focusing sector field ICP-MS (explicitly stated: \"Thermo Scientific Element XR double-focusing sector field ICP-MS unit\")",
                "ICPMS" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/coolantGasFlowRateDefault>,
                        <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/plasmaThermalMode>,
                        <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/rfPowerDefault> ;
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
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/interfaceConeConfiguration> ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Interface Cone" ;
                    schema1:name "missing" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "Thermo Fisher Scientific Element XR (SF-ICP-MS)" ] ;
            schema1:name "example instrumentName" ],
        [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/laserPulseDuration> ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "Laser Ablation System" ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "Teledyne CETAC Technologies Analyte G2 (193 nm ArF excimer)" ] ;
            schema1:name "HELEX II two-volume ablation cell" ;
            ada:laserFluenceDefault "5–7 J cm⁻²" ;
            ada:laserRepetitionRateDefault "20 Hz" ;
            ada:laserSpotGeometryDefault "20×20 µm square" ;
            ada:laserType "193 nm ArF excimer; pulse duration ~5 ns" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "Dept. of Chemistry, Atomic & Mass Spectrometry, Ghent University, Belgium" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "LA-SF-ICP-MS" ;
            schema1:termCode "LA-ICP-MS" ] ;
    schema1:name "Chernonozhkin et al. (2021) Pallasite Olivine 2D Mapping v1" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Pallasite olivine ([Mg,Fe]₂SiO₄)" ],
                <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Chernonozhkin et al. (2021) Chem. Geol. 562; Liu et al. (2008) for IS method" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:ablationPitDepthRateDefault "missing" ;
    ada:ablationSamplingMode "Raster area (2D elemental mapping)" ;
    ada:ablationSpotDurationDefault -9999 ;
    ada:ageModelDefault "missing" ;
    ada:analysisSequenceDefault "(i) Gas blanks → (ii) all glass GRMs for external calibration → (iii) 1–3 cosmic spherule unknowns → (iv) blanks → (v) all glass GRMs again" ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/detectionLimit>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/detectionLimitMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/isobaricInterferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/limitOfQuantificationMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/massResolutionPerAnalyte>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/monitoredIsotopes>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/normalizationStandardsBasedCorrection>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ;
            ada:defaultAnalytes "²⁵Mg",
                "²⁷Al",
                "²⁹Si",
                "³¹P",
                "¹³⁹La",
                "¹⁵³Eu",
                "¹⁹⁵Pt (14 nuclides)",
                "⁴⁵Sc",
                "⁵³Cr",
                "⁵¹V",
                "⁵⁵Mn",
                "⁵⁷Fe",
                "⁶⁰Ni",
                "⁷¹Ga" ] ;
    ada:backgroundCountTimeDefault "Scans for gas blank: 10 per line (before each mapping line); 80 scans during ablation" ;
    ada:blankBackgroundCorrectionMethod "Gas blank measured before each ablation line (10 scans of gas blank per mapping line); average background subtracted from each corresponding ablation line" ;
    ada:calibrationMeasurementFrequency "Each GRM analyzed 3–5× before and 3–5× after sample analyses (all GRMs at start and end of session)" ;
    ada:carrierGasFlowRateDefault "He: MFC-1 (cell) 0.200–0.260 l min⁻¹; MFC-2 (cup) 0.220–0.385 l min⁻¹" ;
    ada:elementalFractionationCorrection "Internal normalization to MgO+FeO+SiO₂+P₂O₅ oxide sum corrects for point-to-point ablation yield variation; additional pixel-by-pixel normalization fixes oxide sum to 100 wt%" ;
    ada:inheritedOrInitialSignalCorrectionDefault "missing" ;
    ada:internalStandardApproach "Sum-of-major-oxide normalization: MgO+FeO+SiO₂+P₂O₅ = 100 wt% per pixel (Liu et al. 2008 approach; no EPMA required for IS)" ;
    ada:internalStandardElement "No single IS element; oxide sum normalization (MgO+FeO+SiO₂+P₂O₅) used as virtual IS per pixel" ;
    ada:ionCounterDeadTimeDefault -9999 ;
    ada:massBiasCorrectionStrategy "missing" ;
    ada:massResolutionAssignment "missing" ;
    ada:oxideProductionMethodAndThreshold "ThO⁺/Th⁺ (mass 248/232); threshold not explicitly stated but minimized by cool plasma" ;
    ada:primaryStandardNameDefault "Multiple glass GRMs used together for linear regression external calibration: NIST SRM 612, NIST SRM 614, USGS GSD-1G (synthetic), USGS GSE-1G (synthetic), USGS BHVO-2G, USGS BIR-1G (natural basalt glasses)" ;
    ada:rasterLineSpacingDefault "20 µm (contiguous; 20×20 µm square spot = line spacing equals spot width)" ;
    ada:sampleIntroduction "missing" ;
    ada:samplingUnit "missing" ;
    ada:secondaryReferenceMaterialDefault "MPI-DING glasses: GOR132-G, StHs6/80-G, T1-G; USGS: BCR-2G, BHVO-2G — measured as unknowns alongside samples and compared to GeoReM preferred values (Table 1 and Section 3.3)" ;
    ada:signalIntegrationIntervalMethod "Manual visual inspection of time-resolved signal per line; anomalous spikes (inclusions, cracks, veinlets) excluded; P-rich veinlet regions identified and excluded from olivine averages" ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:totalIntegrationTimePerOutputDataPointDefault "missing" ;
    ada:uncertaintyLevel "missing" ;
    bios:computationalTool [ schema1:name "In-house MatLab script (Appendix C1)" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/detectionLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimit" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/detectionLimitMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Detection Limit Method" ;
    schema1:valueName "detectionLimitMethod" ;
    ada:dataType "uri" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/isobaricInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Isobaric Interference Corrections Applied" ;
    schema1:valueName "isobaricInterferenceCorrectionsApplied" ;
    ada:dataType "boolean" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "uri" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/massResolutionPerAnalyte> a schema1:PropertyValueSpecification ;
    schema1:name "Mass Resolution per Analyte" ;
    schema1:valueName "massResolutionPerAnalyte" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/monitoredIsotopes> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Monitored Isotopes" ;
    schema1:valueName "monitoredIsotopes" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/normalizationStandardsBasedCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Normalization / Standards-Based Correction" ;
    schema1:valueName "normalizationStandardsBasedCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/coolantGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 15 ;
    schema1:description "Cool: 15 l min⁻¹ Ar; Auxiliary: 0.81 l min⁻¹ (mapping)" ;
    schema1:name "Coolant (Plasma) Gas Flow Rate" ;
    schema1:valueName "coolantGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/icpTuningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Daily tuning; cool plasma conditions optimized; N₂ explicitly not added to avoid N-based interferences" ;
    schema1:name "ICP Tuning" ;
    schema1:valueName "icpTuningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/massResolutionSettingDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Low resolution (M/ΔM = 300; cool plasma mapping)" ;
    schema1:name "Mass Resolution Setting" ;
    schema1:valueName "massResolutionSettingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/memoryEffectMitigationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Gas blank measured before each ablation line; adequate washout ensured by duty cycle timing" ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:valueName "memoryEffectMitigationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/plasmaMakeUpGasAdditionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Ar make-up: 0.81–0.99 l min⁻¹ (mapping); N₂ explicitly not added" ;
    schema1:name "Plasma / Make-up Gas Addition" ;
    schema1:valueName "plasmaMakeUpGasAdditionDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Applied: triple mode detection; cross-calibration between pulse-counting and analog modes performed" ;
    schema1:name "Pulse/Analog Detector Nonlinearity Correction" ;
    schema1:valueName "pulseAnalogDetectorNonlinearityCorrectionDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/rfPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 800 ;
    schema1:description "800 W (cool plasma for mapping)" ;
    schema1:name "RF Power" ;
    schema1:valueName "rfPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "In situ — polished epoxy thick section (HELEX II two-volume cell)" ;
    schema1:name "Sample Form / Analytical Substrate" ;
    schema1:valueName "sampleFormAnalyticalSubstrateDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/signalSmoothingDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "None (no signal smoothing device; N₂ not added)" ;
    schema1:name "Signal Smoothing" ;
    schema1:valueName "signalSmoothingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/spikeOutlierFilteringApproachDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Manual identification and exclusion of P-rich veinlet pixels from olivine averages; anomalous spikes from inclusions excluded per line" ;
    schema1:name "Spike / Outlier Filtering Approach" ;
    schema1:valueName "spikeOutlierFilteringApproachDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSizeDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "9 µm s⁻¹ (continuous raster)" ;
    schema1:name "Transect Rate, Mapping Rate or Step Size" ;
    schema1:valueName "transectRateMappingRateOrStepSizeDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/uncertaintyPropagationMethodDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Longerich et al. (1996) equation (3SD/S × √(1/Nb + 1/Na))" ;
    schema1:name "Uncertainty Propagation Method" ;
    schema1:valueName "uncertaintyPropagationMethodDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/detectorConfiguration> a schema1:PropertyValue ;
    schema1:name "Detector Configuration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/detectorConfiguration> ;
    schema1:value "Triple mode detection (all analytical modes)" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/interfaceConeConfiguration> a schema1:PropertyValue ;
    schema1:name "Interface Cone Configuration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/interfaceConeConfiguration> ;
    schema1:value "Al standard sample cone (1.1 mm aperture); Al H-type skimmer (0.8 mm aperture)" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/laserPulseDuration> a schema1:PropertyValue ;
    schema1:name "Laser Pulse Duration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/laserPulseDuration> ;
    schema1:value "~5 ns (ArF excimer)" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/plasmaThermalMode> a schema1:PropertyValue ;
    schema1:name "Plasma Thermal Mode" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/plasmaThermalMode> ;
    schema1:value "Cool plasma (800 W RF) to reduce Ar-based argide interferences on ⁶⁰Ni and ⁷¹Ga" .


```


### laSficpmsUPbTAPP example Chernonozhkin2021-2
laSficpmsUPbTAPP instance derived from Chernonozhkin et al. 2021 (Chem Geol 562) Pallasite olivine Line scan (Run 1: major) + Spot (Run 2: trace) [Multi-run] ns-LA-SF-ICP-MS Ghent University.
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
  "@id": "ex:laSficpmsUPbTAPP-Chernonozhkin2021-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Chernonozhkin et al. (2021) Pallasite Olivine Multi-run Spot/Transect v1",
  "schema:description": "Multi-run sequential design is the key methodological innovation: Run 1 (major elements, 30 µm, MR) provides Cr IS for Run 2 (trace elements, 130 µm, LR); pre-ablation pass removes surface contamination before Run 1 Reported detail: ada:ablationSamplingMode = Transect (line scan, run 1) + Spot (run 2 on same location after pre-ablation).",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-ICP-MS",
      "schema:name": "LA-SF-ICP-MS"
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
      "schema:name": "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent"
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
            "Pallasite olivine ([Mg,Fe]₂SiO₄)"
          ]
        },
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleFormAnalyticalSubstrateDefault",
          "schema:name": "Sample Form / Analytical Substrate",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "In situ — polished epoxy thick section; pre-ablated before trace element run"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "PMG thick sections polished; pre-ablation pass (2 J cm⁻², 20 Hz, 150 µm square, 300 µm s⁻¹) before trace element run",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/laSficpmsUPbTAPP/preAblationSurfaceTreatmentDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "preAblationSurfaceTreatmentDefault",
            "schema:name": "Pre-Ablation Surface Treatment",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Pre-ablation pass: 150 µm square, 2 J cm⁻², 20 Hz, 300 µm s⁻¹ scan before trace element spot run; removes surface contamination and re-deposited material"
          }
        ],
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
            "@id": "ada:parameter/laSficpmsUPbTAPP/signalSmoothingDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "signalSmoothingDefault",
            "schema:name": "Signal Smoothing",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "None"
          },
          {
            "@id": "ada:parameter/laSficpmsUPbTAPP/spikeOutlierFilteringApproachDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "spikeOutlierFilteringApproachDefault",
            "schema:name": "Spike / Outlier Filtering Approach",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Manual inspection; analyses with elevated P, Ca, Co, Ni (phosphate or metal inclusions) excluded; Cr heterogeneities also flagged"
          },
          {
            "@id": "ada:parameter/laSficpmsUPbTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "pulseAnalogDetectorNonlinearityCorrectionDefault",
            "schema:name": "Pulse/Analog Detector Nonlinearity Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Applied: Run 1 medium resolution with Faraday for major elements; Run 2 low resolution; cross-calibration performed"
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
        "schema:name": "Teledyne CETAC Technologies Analyte G2 (193 nm ArF excimer)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "193 nm ArF excimer; pulse duration ~5 ns",
      "schema:name": "HELEX II two-volume ablation cell",
      "ada:laserSpotGeometryDefault": "Run 1 (major): 30 µm circular; Run 2 (trace): 130 µm circular",
      "ada:laserFluenceDefault": "Run 1 (major): 4.72 J cm⁻²; Run 2 (trace): 4.72 J cm⁻²",
      "ada:laserRepetitionRateDefault": "Run 1 (major): 20 Hz; Run 2 (trace): 40 Hz",
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/laserPulseDuration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laSficpmsUPbTAPP/laserPulseDuration"
            }
          ],
          "schema:name": "Laser Pulse Duration",
          "schema:value": "~5 ns (ArF excimer)"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ]
    },
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
              "@id": "ada:parameter/laSficpmsUPbTAPP/interfaceConeConfiguration",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/laSficpmsUPbTAPP/interfaceConeConfiguration"
                }
              ],
              "schema:name": "Interface Cone Configuration",
              "schema:value": "Al standard sample cone (1.1 mm aperture); Al H-type skimmer (0.8 mm aperture)"
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
              "@id": "ada:parameter/laSficpmsUPbTAPP/coolantGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantGasFlowRateDefault",
              "schema:name": "Coolant (Plasma) Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 15,
              "schema:description": "Cool: 15 l min⁻¹ Ar; Auxiliary: 0.90 l min⁻¹ (run 1 and run 2)"
            },
            {
              "@id": "ada:parameter/laSficpmsUPbTAPP/rfPowerDefault",
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
              "@id": "ada:parameter/laSficpmsUPbTAPP/plasmaThermalMode",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/laSficpmsUPbTAPP/plasmaThermalMode"
                }
              ],
              "schema:name": "Plasma Thermal Mode",
              "schema:value": "Normal plasma (1000 W RF)"
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
          "@id": "ada:parameter/laSficpmsUPbTAPP/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Run 1: Medium resolution (M/ΔM = 4000) for major elements; Run 2: Low resolution (M/ΔM = 300) for trace elements"
        },
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/detectorConfiguration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laSficpmsUPbTAPP/detectorConfiguration"
            }
          ],
          "schema:name": "Detector Configuration",
          "schema:value": "Triple mode detection; Faraday used for major elements in run 1"
        },
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/icpTuningDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "icpTuningDefault",
          "schema:name": "ICP Tuning",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Same instrument as mapping; tuning optimized per run (different RF power and resolution settings per run)"
        },
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Washout time: 11 s between runs (runs include 400 µm line + blank + washout)"
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
      "schema:name": "In-house MatLab script (Appendix C2)"
    }
  ],
  "ada:ablationSamplingMode": [
    "Transect (continuous line scan)"
  ],
  "ada:ablationSpotDurationDefault": "N/A (line scan run 1) / N/A (spot run 2 — duration set by 34 runs covering 400 µm + washout, not a fixed spot duration)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSizeDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "transectRateMappingRateOrStepSizeDefault",
      "schema:name": "Transect Rate, Mapping Rate or Step Size",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "10 µm s⁻¹ (line scan run 1); spot mode (run 2)"
    },
    {
      "@id": "ada:parameter/laSficpmsUPbTAPP/plasmaMakeUpGasAdditionDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "plasmaMakeUpGasAdditionDefault",
      "schema:name": "Plasma / Make-up Gas Addition",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Ar make-up: 0.947 l min⁻¹ (run 1 and run 2); N₂ not added"
    },
    {
      "@id": "ada:parameter/laSficpmsUPbTAPP/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/multiRunSequentialAnalysisDesign"
        }
      ],
      "schema:name": "Multi-Run Sequential Analysis Design",
      "schema:value": "Three-stage sequential design on same olivine location: (1) Pre-ablation pass (2 J cm⁻², 150 µm square, 300 µm s⁻¹) to remove surface contamination; (2) Run 1 — major elements (30 µm circular, MR M/ΔM=4000, 20 Hz, 7 nuclides); (3) Run 2 — trace elements (130 µm circular, LR M/ΔM=300, 40 Hz, 36 nuclides; Cr from run 1 as IS)"
    },
    {
      "@id": "ada:parameter/laSficpmsUPbTAPP/uncertaintyPropagationMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "uncertaintyPropagationMethodDefault",
      "schema:name": "Uncertainty Propagation Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Longerich et al. (1996) for LOD; uncertainty for concentrations not formally described"
    }
  ],
  "ada:carrierGasFlowRateDefault": "He: MFC-1 0.19 l min⁻¹; MFC-2 0.22 l min⁻¹",
  "ada:analysisSequenceDefault": "GRM block (3–5×) → unknowns → GRM block (3–5×); same structure for run 1 and run 2",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Run 1 (major): ²⁵Mg",
      "²⁹Si",
      "³¹P",
      "⁴⁴Ca",
      "⁵³Cr",
      "⁵⁵Mn",
      "⁵⁷Fe (7 nuclides; medium resolution)",
      "Run 2 (trace): ⁷Li",
      "⁴⁵Sc",
      "⁵¹V",
      "⁵³Cr",
      "⁵⁹Co",
      "⁶⁰Ni",
      "⁶³Cu",
      "⁶⁶Zn",
      "⁸⁹Y",
      "⁹⁰Zr",
      "⁹³Nb",
      "¹³³Cs",
      "¹³⁷Ba",
      "¹³⁹La–¹⁷⁵Lu (all REE)",
      "¹⁸⁰Hf",
      "¹⁸¹Ta",
      "¹⁸²W",
      "¹⁸⁵Re",
      "¹⁹³Ir",
      "¹⁹⁵Pt",
      "¹⁹⁷Au",
      "²³²Th",
      "²³⁸U (36 nuclides)"
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
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/monitoredIsotopes",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredIsotopes",
        "schema:name": "Monitored Isotopes",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "boolean",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/normalizationStandardsBasedCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "normalizationStandardsBasedCorrection",
        "schema:name": "Normalization / Standards-Based Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "uri",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "uri"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/massResolutionPerAnalyte",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionPerAnalyte",
        "schema:name": "Mass Resolution per Analyte",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:backgroundCountTimeDefault": "Run 1: 5 gas blank scans; 24 ablation scans; Run 2: 5 gas blank scans; 24 ablation scans",
  "ada:internalStandardApproach": "Run 1 (major elements): sum-of-oxide normalization (MgO+FeO+SiO₂+P₂O₅=100 wt%; Liu et al. 2008); Run 2 (trace elements): single element IS from Run 1 (⁵³Cr concentration from major element run used as IS for trace element run)",
  "ada:internalStandardElement": "Run 1: No single IS; oxide sum normalization; Run 2: ⁵³Cr (concentration from Run 1 major-element analysis on 30 µm spot used as IS for 130 µm spot trace element run)",
  "ada:elementalFractionationCorrection": [
    "Run 1: Oxide sum normalization corrects for ablation yield variation; external calibration using glass GRMs (NIST + USGS + MPI-DING); Run 2: Cr from run 1 as IS corrects for ablation yield; external calibration with expanded glass GRM set"
  ],
  "ada:signalIntegrationIntervalMethod": "Time-resolved signals inspected manually; unstable intervals at start and end discarded; Cr heterogeneities and inclusion signals (elevated P, Ca, Co, Ni) identified and excluded from integration",
  "ada:blankBackgroundCorrectionMethod": "Gas blank measured before each analysis (5 scans); average background value preceding each analysis subtracted from corresponding data",
  "ada:primaryStandardNameDefault": "Same glass GRM set as mapping for Run 1; expanded set additionally includes MPI-DING KL2-G, ML3B-G, StHs6/80-G, T1-G, ATHO-G, BM90/21-G, GOR128-G, GOR132-G for Run 2 trace elements",
  "ada:calibrationMeasurementFrequency": "Same as mapping protocol; GRMs at start and end",
  "ada:secondaryReferenceMaterialDefault": [
    "Same GRM set measured as unknowns for accuracy assessment"
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ageModelDefault": "missing",
  "ada:inheritedOrInitialSignalCorrectionDefault": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:massResolutionAssignment": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS-UPb/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:laSficpmsUPbTAPP-Chernonozhkin2021-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Chernonozhkin et al. (2021) Pallasite Olivine Multi-run Spot/Transect v1",
  "schema:description": "Multi-run sequential design is the key methodological innovation: Run 1 (major elements, 30 \u00b5m, MR) provides Cr IS for Run 2 (trace elements, 130 \u00b5m, LR); pre-ablation pass removes surface contamination before Run 1 Reported detail: ada:ablationSamplingMode = Transect (line scan, run 1) + Spot (run 2 on same location after pre-ablation).",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-ICP-MS",
      "schema:name": "LA-SF-ICP-MS"
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
      "schema:name": "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent"
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
            "Pallasite olivine ([Mg,Fe]\u2082SiO\u2084)"
          ]
        },
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleFormAnalyticalSubstrateDefault",
          "schema:name": "Sample Form / Analytical Substrate",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "In situ \u2014 polished epoxy thick section; pre-ablated before trace element run"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "PMG thick sections polished; pre-ablation pass (2 J cm\u207b\u00b2, 20 Hz, 150 \u00b5m square, 300 \u00b5m s\u207b\u00b9) before trace element run",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/laSficpmsUPbTAPP/preAblationSurfaceTreatmentDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "preAblationSurfaceTreatmentDefault",
            "schema:name": "Pre-Ablation Surface Treatment",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Pre-ablation pass: 150 \u00b5m square, 2 J cm\u207b\u00b2, 20 Hz, 300 \u00b5m s\u207b\u00b9 scan before trace element spot run; removes surface contamination and re-deposited material"
          }
        ],
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
            "@id": "ada:parameter/laSficpmsUPbTAPP/signalSmoothingDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "signalSmoothingDefault",
            "schema:name": "Signal Smoothing",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "None"
          },
          {
            "@id": "ada:parameter/laSficpmsUPbTAPP/spikeOutlierFilteringApproachDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "spikeOutlierFilteringApproachDefault",
            "schema:name": "Spike / Outlier Filtering Approach",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Manual inspection; analyses with elevated P, Ca, Co, Ni (phosphate or metal inclusions) excluded; Cr heterogeneities also flagged"
          },
          {
            "@id": "ada:parameter/laSficpmsUPbTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "pulseAnalogDetectorNonlinearityCorrectionDefault",
            "schema:name": "Pulse/Analog Detector Nonlinearity Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Applied: Run 1 medium resolution with Faraday for major elements; Run 2 low resolution; cross-calibration performed"
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
        "schema:name": "Teledyne CETAC Technologies Analyte G2 (193 nm ArF excimer)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "193 nm ArF excimer; pulse duration ~5 ns",
      "schema:name": "HELEX II two-volume ablation cell",
      "ada:laserSpotGeometryDefault": "Run 1 (major): 30 \u00b5m circular; Run 2 (trace): 130 \u00b5m circular",
      "ada:laserFluenceDefault": "Run 1 (major): 4.72 J cm\u207b\u00b2; Run 2 (trace): 4.72 J cm\u207b\u00b2",
      "ada:laserRepetitionRateDefault": "Run 1 (major): 20 Hz; Run 2 (trace): 40 Hz",
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/laserPulseDuration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laSficpmsUPbTAPP/laserPulseDuration"
            }
          ],
          "schema:name": "Laser Pulse Duration",
          "schema:value": "~5 ns (ArF excimer)"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ]
    },
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
              "@id": "ada:parameter/laSficpmsUPbTAPP/interfaceConeConfiguration",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/laSficpmsUPbTAPP/interfaceConeConfiguration"
                }
              ],
              "schema:name": "Interface Cone Configuration",
              "schema:value": "Al standard sample cone (1.1 mm aperture); Al H-type skimmer (0.8 mm aperture)"
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
              "@id": "ada:parameter/laSficpmsUPbTAPP/coolantGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantGasFlowRateDefault",
              "schema:name": "Coolant (Plasma) Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 15,
              "schema:description": "Cool: 15 l min\u207b\u00b9 Ar; Auxiliary: 0.90 l min\u207b\u00b9 (run 1 and run 2)"
            },
            {
              "@id": "ada:parameter/laSficpmsUPbTAPP/rfPowerDefault",
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
              "@id": "ada:parameter/laSficpmsUPbTAPP/plasmaThermalMode",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/laSficpmsUPbTAPP/plasmaThermalMode"
                }
              ],
              "schema:name": "Plasma Thermal Mode",
              "schema:value": "Normal plasma (1000 W RF)"
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
          "@id": "ada:parameter/laSficpmsUPbTAPP/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Run 1: Medium resolution (M/\u0394M = 4000) for major elements; Run 2: Low resolution (M/\u0394M = 300) for trace elements"
        },
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/detectorConfiguration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laSficpmsUPbTAPP/detectorConfiguration"
            }
          ],
          "schema:name": "Detector Configuration",
          "schema:value": "Triple mode detection; Faraday used for major elements in run 1"
        },
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/icpTuningDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "icpTuningDefault",
          "schema:name": "ICP Tuning",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Same instrument as mapping; tuning optimized per run (different RF power and resolution settings per run)"
        },
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/memoryEffectMitigationDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "memoryEffectMitigationDefault",
          "schema:name": "Memory Effect Mitigation",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Washout time: 11 s between runs (runs include 400 \u00b5m line + blank + washout)"
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
      "schema:name": "In-house MatLab script (Appendix C2)"
    }
  ],
  "ada:ablationSamplingMode": [
    "Transect (continuous line scan)"
  ],
  "ada:ablationSpotDurationDefault": "N/A (line scan run 1) / N/A (spot run 2 \u2014 duration set by 34 runs covering 400 \u00b5m + washout, not a fixed spot duration)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSizeDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "transectRateMappingRateOrStepSizeDefault",
      "schema:name": "Transect Rate, Mapping Rate or Step Size",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "10 \u00b5m s\u207b\u00b9 (line scan run 1); spot mode (run 2)"
    },
    {
      "@id": "ada:parameter/laSficpmsUPbTAPP/plasmaMakeUpGasAdditionDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "plasmaMakeUpGasAdditionDefault",
      "schema:name": "Plasma / Make-up Gas Addition",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Ar make-up: 0.947 l min\u207b\u00b9 (run 1 and run 2); N\u2082 not added"
    },
    {
      "@id": "ada:parameter/laSficpmsUPbTAPP/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/multiRunSequentialAnalysisDesign"
        }
      ],
      "schema:name": "Multi-Run Sequential Analysis Design",
      "schema:value": "Three-stage sequential design on same olivine location: (1) Pre-ablation pass (2 J cm\u207b\u00b2, 150 \u00b5m square, 300 \u00b5m s\u207b\u00b9) to remove surface contamination; (2) Run 1 \u2014 major elements (30 \u00b5m circular, MR M/\u0394M=4000, 20 Hz, 7 nuclides); (3) Run 2 \u2014 trace elements (130 \u00b5m circular, LR M/\u0394M=300, 40 Hz, 36 nuclides; Cr from run 1 as IS)"
    },
    {
      "@id": "ada:parameter/laSficpmsUPbTAPP/uncertaintyPropagationMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "uncertaintyPropagationMethodDefault",
      "schema:name": "Uncertainty Propagation Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Longerich et al. (1996) for LOD; uncertainty for concentrations not formally described"
    }
  ],
  "ada:carrierGasFlowRateDefault": "He: MFC-1 0.19 l min\u207b\u00b9; MFC-2 0.22 l min\u207b\u00b9",
  "ada:analysisSequenceDefault": "GRM block (3\u20135\u00d7) \u2192 unknowns \u2192 GRM block (3\u20135\u00d7); same structure for run 1 and run 2",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Run 1 (major): \u00b2\u2075Mg",
      "\u00b2\u2079Si",
      "\u00b3\u00b9P",
      "\u2074\u2074Ca",
      "\u2075\u00b3Cr",
      "\u2075\u2075Mn",
      "\u2075\u2077Fe (7 nuclides; medium resolution)",
      "Run 2 (trace): \u2077Li",
      "\u2074\u2075Sc",
      "\u2075\u00b9V",
      "\u2075\u00b3Cr",
      "\u2075\u2079Co",
      "\u2076\u2070Ni",
      "\u2076\u00b3Cu",
      "\u2076\u2076Zn",
      "\u2078\u2079Y",
      "\u2079\u2070Zr",
      "\u2079\u00b3Nb",
      "\u00b9\u00b3\u00b3Cs",
      "\u00b9\u00b3\u2077Ba",
      "\u00b9\u00b3\u2079La\u2013\u00b9\u2077\u2075Lu (all REE)",
      "\u00b9\u2078\u2070Hf",
      "\u00b9\u2078\u00b9Ta",
      "\u00b9\u2078\u00b2W",
      "\u00b9\u2078\u2075Re",
      "\u00b9\u2079\u00b3Ir",
      "\u00b9\u2079\u2075Pt",
      "\u00b9\u2079\u2077Au",
      "\u00b2\u00b3\u00b2Th",
      "\u00b2\u00b3\u2078U (36 nuclides)"
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
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/monitoredIsotopes",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredIsotopes",
        "schema:name": "Monitored Isotopes",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "boolean",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/normalizationStandardsBasedCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "normalizationStandardsBasedCorrection",
        "schema:name": "Normalization / Standards-Based Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "uri",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "uri"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/massResolutionPerAnalyte",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionPerAnalyte",
        "schema:name": "Mass Resolution per Analyte",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:backgroundCountTimeDefault": "Run 1: 5 gas blank scans; 24 ablation scans; Run 2: 5 gas blank scans; 24 ablation scans",
  "ada:internalStandardApproach": "Run 1 (major elements): sum-of-oxide normalization (MgO+FeO+SiO\u2082+P\u2082O\u2085=100 wt%; Liu et al. 2008); Run 2 (trace elements): single element IS from Run 1 (\u2075\u00b3Cr concentration from major element run used as IS for trace element run)",
  "ada:internalStandardElement": "Run 1: No single IS; oxide sum normalization; Run 2: \u2075\u00b3Cr (concentration from Run 1 major-element analysis on 30 \u00b5m spot used as IS for 130 \u00b5m spot trace element run)",
  "ada:elementalFractionationCorrection": [
    "Run 1: Oxide sum normalization corrects for ablation yield variation; external calibration using glass GRMs (NIST + USGS + MPI-DING); Run 2: Cr from run 1 as IS corrects for ablation yield; external calibration with expanded glass GRM set"
  ],
  "ada:signalIntegrationIntervalMethod": "Time-resolved signals inspected manually; unstable intervals at start and end discarded; Cr heterogeneities and inclusion signals (elevated P, Ca, Co, Ni) identified and excluded from integration",
  "ada:blankBackgroundCorrectionMethod": "Gas blank measured before each analysis (5 scans); average background value preceding each analysis subtracted from corresponding data",
  "ada:primaryStandardNameDefault": "Same glass GRM set as mapping for Run 1; expanded set additionally includes MPI-DING KL2-G, ML3B-G, StHs6/80-G, T1-G, ATHO-G, BM90/21-G, GOR128-G, GOR132-G for Run 2 trace elements",
  "ada:calibrationMeasurementFrequency": "Same as mapping protocol; GRMs at start and end",
  "ada:secondaryReferenceMaterialDefault": [
    "Same GRM set measured as unknowns for accuracy assessment"
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ageModelDefault": "missing",
  "ada:inheritedOrInitialSignalCorrectionDefault": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:massResolutionAssignment": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
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

ex:laSficpmsUPbTAPP-Chernonozhkin2021-2 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/preAblationSurfaceTreatmentDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "PMG thick sections polished; pre-ablation pass (2 J cm⁻², 20 Hz, 150 µm square, 300 µm s⁻¹) before trace element run" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault>,
                        <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/signalSmoothingDefault>,
                        <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/spikeOutlierFilteringApproachDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/multiRunSequentialAnalysisDesign>,
        <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/plasmaMakeUpGasAdditionDefault>,
        <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSizeDefault>,
        <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/uncertaintyPropagationMethodDefault> ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Chernonozhkin, Pittarello, Goderis, Vanhaecke et al." ] ;
    schema1:datePublished "missing" ;
    schema1:description "Multi-run sequential design is the key methodological innovation: Run 1 (major elements, 30 µm, MR) provides Cr IS for Run 2 (trace elements, 130 µm, LR); pre-ablation pass removes surface contamination before Run 1 Reported detail: ada:ablationSamplingMode = Transect (line scan, run 1) + Spot (run 2 on same location after pre-ablation)." ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent" ] ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/detectorConfiguration>,
                <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/icpTuningDefault>,
                <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/massResolutionSettingDefault>,
                <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/memoryEffectMitigationDefault> ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "Double-focusing sector field ICP-MS (explicitly stated)",
                "ICPMS" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/coolantGasFlowRateDefault>,
                        <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/plasmaThermalMode>,
                        <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/rfPowerDefault> ;
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
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/interfaceConeConfiguration> ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Interface Cone" ;
                    schema1:name "missing" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "Thermo Fisher Scientific Element XR (SF-ICP-MS)" ] ;
            schema1:name "example instrumentName" ],
        [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/laserPulseDuration> ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "Laser Ablation System" ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "Teledyne CETAC Technologies Analyte G2 (193 nm ArF excimer)" ] ;
            schema1:name "HELEX II two-volume ablation cell" ;
            ada:laserFluenceDefault "Run 1 (major): 4.72 J cm⁻²; Run 2 (trace): 4.72 J cm⁻²" ;
            ada:laserRepetitionRateDefault "Run 1 (major): 20 Hz; Run 2 (trace): 40 Hz" ;
            ada:laserSpotGeometryDefault "Run 1 (major): 30 µm circular; Run 2 (trace): 130 µm circular" ;
            ada:laserType "193 nm ArF excimer; pulse duration ~5 ns" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "Dept. of Chemistry, Atomic & Mass Spectrometry, Ghent University, Belgium" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "LA-SF-ICP-MS" ;
            schema1:termCode "LA-ICP-MS" ] ;
    schema1:name "Chernonozhkin et al. (2021) Pallasite Olivine Multi-run Spot/Transect v1" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Pallasite olivine ([Mg,Fe]₂SiO₄)" ],
                <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Chernonozhkin et al. (2021) Chem. Geol. 562; Liu et al. (2008) for IS method" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:ablationPitDepthRateDefault "missing" ;
    ada:ablationSamplingMode "Transect (continuous line scan)" ;
    ada:ablationSpotDurationDefault "N/A (line scan run 1) / N/A (spot run 2 — duration set by 34 runs covering 400 µm + washout, not a fixed spot duration)" ;
    ada:ageModelDefault "missing" ;
    ada:analysisSequenceDefault "GRM block (3–5×) → unknowns → GRM block (3–5×); same structure for run 1 and run 2" ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/detectionLimit>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/detectionLimitMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/isobaricInterferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/limitOfQuantificationMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/massResolutionPerAnalyte>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/monitoredIsotopes>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/normalizationStandardsBasedCorrection>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ;
            ada:defaultAnalytes "Run 1 (major): ²⁵Mg",
                "Run 2 (trace): ⁷Li",
                "²³²Th",
                "²³⁸U (36 nuclides)",
                "²⁹Si",
                "³¹P",
                "¹³³Cs",
                "¹³⁷Ba",
                "¹³⁹La–¹⁷⁵Lu (all REE)",
                "¹⁸²W",
                "¹⁸¹Ta",
                "¹⁸⁰Hf",
                "¹⁸⁵Re",
                "¹⁹³Ir",
                "¹⁹⁵Pt",
                "¹⁹⁷Au",
                "⁴⁴Ca",
                "⁴⁵Sc",
                "⁵³Cr",
                "⁵¹V",
                "⁵⁵Mn",
                "⁵⁷Fe (7 nuclides; medium resolution)",
                "⁵⁹Co",
                "⁶³Cu",
                "⁶⁰Ni",
                "⁶⁶Zn",
                "⁸⁹Y",
                "⁹³Nb",
                "⁹⁰Zr" ] ;
    ada:backgroundCountTimeDefault "Run 1: 5 gas blank scans; 24 ablation scans; Run 2: 5 gas blank scans; 24 ablation scans" ;
    ada:blankBackgroundCorrectionMethod "Gas blank measured before each analysis (5 scans); average background value preceding each analysis subtracted from corresponding data" ;
    ada:calibrationMeasurementFrequency "Same as mapping protocol; GRMs at start and end" ;
    ada:carrierGasFlowRateDefault "He: MFC-1 0.19 l min⁻¹; MFC-2 0.22 l min⁻¹" ;
    ada:elementalFractionationCorrection "Run 1: Oxide sum normalization corrects for ablation yield variation; external calibration using glass GRMs (NIST + USGS + MPI-DING); Run 2: Cr from run 1 as IS corrects for ablation yield; external calibration with expanded glass GRM set" ;
    ada:inheritedOrInitialSignalCorrectionDefault "missing" ;
    ada:internalStandardApproach "Run 1 (major elements): sum-of-oxide normalization (MgO+FeO+SiO₂+P₂O₅=100 wt%; Liu et al. 2008); Run 2 (trace elements): single element IS from Run 1 (⁵³Cr concentration from major element run used as IS for trace element run)" ;
    ada:internalStandardElement "Run 1: No single IS; oxide sum normalization; Run 2: ⁵³Cr (concentration from Run 1 major-element analysis on 30 µm spot used as IS for 130 µm spot trace element run)" ;
    ada:ionCounterDeadTimeDefault -9999 ;
    ada:massBiasCorrectionStrategy "missing" ;
    ada:massResolutionAssignment "missing" ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:primaryStandardNameDefault "Same glass GRM set as mapping for Run 1; expanded set additionally includes MPI-DING KL2-G, ML3B-G, StHs6/80-G, T1-G, ATHO-G, BM90/21-G, GOR128-G, GOR132-G for Run 2 trace elements" ;
    ada:rasterLineSpacingDefault "missing" ;
    ada:sampleIntroduction "missing" ;
    ada:samplingUnit "missing" ;
    ada:secondaryReferenceMaterialDefault "Same GRM set measured as unknowns for accuracy assessment" ;
    ada:signalIntegrationIntervalMethod "Time-resolved signals inspected manually; unstable intervals at start and end discarded; Cr heterogeneities and inclusion signals (elevated P, Ca, Co, Ni) identified and excluded from integration" ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:totalIntegrationTimePerOutputDataPointDefault "missing" ;
    ada:uncertaintyLevel "missing" ;
    bios:computationalTool [ schema1:name "In-house MatLab script (Appendix C2)" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/detectionLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimit" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/detectionLimitMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Detection Limit Method" ;
    schema1:valueName "detectionLimitMethod" ;
    ada:dataType "uri" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/isobaricInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Isobaric Interference Corrections Applied" ;
    schema1:valueName "isobaricInterferenceCorrectionsApplied" ;
    ada:dataType "boolean" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "uri" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/massResolutionPerAnalyte> a schema1:PropertyValueSpecification ;
    schema1:name "Mass Resolution per Analyte" ;
    schema1:valueName "massResolutionPerAnalyte" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/monitoredIsotopes> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Monitored Isotopes" ;
    schema1:valueName "monitoredIsotopes" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/normalizationStandardsBasedCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Normalization / Standards-Based Correction" ;
    schema1:valueName "normalizationStandardsBasedCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/coolantGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 15 ;
    schema1:description "Cool: 15 l min⁻¹ Ar; Auxiliary: 0.90 l min⁻¹ (run 1 and run 2)" ;
    schema1:name "Coolant (Plasma) Gas Flow Rate" ;
    schema1:valueName "coolantGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/icpTuningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Same instrument as mapping; tuning optimized per run (different RF power and resolution settings per run)" ;
    schema1:name "ICP Tuning" ;
    schema1:valueName "icpTuningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/massResolutionSettingDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Run 1: Medium resolution (M/ΔM = 4000) for major elements; Run 2: Low resolution (M/ΔM = 300) for trace elements" ;
    schema1:name "Mass Resolution Setting" ;
    schema1:valueName "massResolutionSettingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/memoryEffectMitigationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Washout time: 11 s between runs (runs include 400 µm line + blank + washout)" ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:valueName "memoryEffectMitigationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/plasmaMakeUpGasAdditionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Ar make-up: 0.947 l min⁻¹ (run 1 and run 2); N₂ not added" ;
    schema1:name "Plasma / Make-up Gas Addition" ;
    schema1:valueName "plasmaMakeUpGasAdditionDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/preAblationSurfaceTreatmentDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Pre-ablation pass: 150 µm square, 2 J cm⁻², 20 Hz, 300 µm s⁻¹ scan before trace element spot run; removes surface contamination and re-deposited material" ;
    schema1:name "Pre-Ablation Surface Treatment" ;
    schema1:valueName "preAblationSurfaceTreatmentDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Applied: Run 1 medium resolution with Faraday for major elements; Run 2 low resolution; cross-calibration performed" ;
    schema1:name "Pulse/Analog Detector Nonlinearity Correction" ;
    schema1:valueName "pulseAnalogDetectorNonlinearityCorrectionDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/rfPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1000 ;
    schema1:description "1000 W (run 1 major elements + run 2 trace elements)" ;
    schema1:name "RF Power" ;
    schema1:valueName "rfPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "In situ — polished epoxy thick section; pre-ablated before trace element run" ;
    schema1:name "Sample Form / Analytical Substrate" ;
    schema1:valueName "sampleFormAnalyticalSubstrateDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/signalSmoothingDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "None" ;
    schema1:name "Signal Smoothing" ;
    schema1:valueName "signalSmoothingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/spikeOutlierFilteringApproachDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Manual inspection; analyses with elevated P, Ca, Co, Ni (phosphate or metal inclusions) excluded; Cr heterogeneities also flagged" ;
    schema1:name "Spike / Outlier Filtering Approach" ;
    schema1:valueName "spikeOutlierFilteringApproachDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSizeDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "10 µm s⁻¹ (line scan run 1); spot mode (run 2)" ;
    schema1:name "Transect Rate, Mapping Rate or Step Size" ;
    schema1:valueName "transectRateMappingRateOrStepSizeDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/uncertaintyPropagationMethodDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Longerich et al. (1996) for LOD; uncertainty for concentrations not formally described" ;
    schema1:name "Uncertainty Propagation Method" ;
    schema1:valueName "uncertaintyPropagationMethodDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/detectorConfiguration> a schema1:PropertyValue ;
    schema1:name "Detector Configuration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/detectorConfiguration> ;
    schema1:value "Triple mode detection; Faraday used for major elements in run 1" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/interfaceConeConfiguration> a schema1:PropertyValue ;
    schema1:name "Interface Cone Configuration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/interfaceConeConfiguration> ;
    schema1:value "Al standard sample cone (1.1 mm aperture); Al H-type skimmer (0.8 mm aperture)" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/laserPulseDuration> a schema1:PropertyValue ;
    schema1:name "Laser Pulse Duration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/laserPulseDuration> ;
    schema1:value "~5 ns (ArF excimer)" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/multiRunSequentialAnalysisDesign> a schema1:PropertyValue ;
    schema1:name "Multi-Run Sequential Analysis Design" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/multiRunSequentialAnalysisDesign> ;
    schema1:value "Three-stage sequential design on same olivine location: (1) Pre-ablation pass (2 J cm⁻², 150 µm square, 300 µm s⁻¹) to remove surface contamination; (2) Run 1 — major elements (30 µm circular, MR M/ΔM=4000, 20 Hz, 7 nuclides); (3) Run 2 — trace elements (130 µm circular, LR M/ΔM=300, 40 Hz, 36 nuclides; Cr from run 1 as IS)" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/plasmaThermalMode> a schema1:PropertyValue ;
    schema1:name "Plasma Thermal Mode" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/plasmaThermalMode> ;
    schema1:value "Normal plasma (1000 W RF)" .


```


### laSficpmsUPbTAPP example Chernonozhkin2021-3
laSficpmsUPbTAPP instance derived from Chernonozhkin et al. 2021 (Chem Geol 562) Pallasite phosphate Spot analysis ns-LA-SF-ICP-MS Ghent University.
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
  "@id": "ex:laSficpmsUPbTAPP-Chernonozhkin2021-3",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Chernonozhkin et al. (2021) Pallasite Phosphate Spot v1",
  "schema:description": "Phosphate phase identification used LA-ICP-MS data combined with EMPA and µXRF (Fig. D9); merrillite, stanfieldite, farringtonite distinguished by REE patterns; oxide sum normalization applied to phosphate (not olivine IS approach)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-ICP-MS",
      "schema:name": "LA-SF-ICP-MS"
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
      "schema:name": "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent"
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
            "Pallasite Ca-phosphate (merrillite, stanfieldite, farringtonite)"
          ]
        },
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleFormAnalyticalSubstrateDefault",
          "schema:name": "Sample Form / Analytical Substrate",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "In situ — polished epoxy thick section"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "PMG thick sections polished; same as olivine mapping preparation",
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
            "@id": "ada:parameter/laSficpmsUPbTAPP/signalSmoothingDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "signalSmoothingDefault",
            "schema:name": "Signal Smoothing",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "None"
          },
          {
            "@id": "ada:parameter/laSficpmsUPbTAPP/spikeOutlierFilteringApproachDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "spikeOutlierFilteringApproachDefault",
            "schema:name": "Spike / Outlier Filtering Approach",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Anomalous time steps excluded during manual inspection"
          },
          {
            "@id": "ada:parameter/laSficpmsUPbTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "pulseAnalogDetectorNonlinearityCorrectionDefault",
            "schema:name": "Pulse/Analog Detector Nonlinearity Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Applied: triple mode detection"
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
        "schema:name": "Teledyne CETAC Technologies Analyte G2 (193 nm ArF excimer)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "193 nm ArF excimer; pulse duration ~5 ns",
      "schema:name": "HELEX II two-volume ablation cell",
      "ada:laserSpotGeometryDefault": "110 µm circular (spot mode)",
      "ada:laserFluenceDefault": "3.5 J cm⁻²",
      "ada:laserRepetitionRateDefault": "20 Hz",
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/laserPulseDuration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laSficpmsUPbTAPP/laserPulseDuration"
            }
          ],
          "schema:name": "Laser Pulse Duration",
          "schema:value": "~5 ns (ArF excimer)"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ]
    },
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
              "@id": "ada:parameter/laSficpmsUPbTAPP/interfaceConeConfiguration",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/laSficpmsUPbTAPP/interfaceConeConfiguration"
                }
              ],
              "schema:name": "Interface Cone Configuration",
              "schema:value": "Al standard sample cone (1.1 mm aperture); Al H-type skimmer (0.8 mm aperture)"
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
              "@id": "ada:parameter/laSficpmsUPbTAPP/coolantGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantGasFlowRateDefault",
              "schema:name": "Coolant (Plasma) Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 15,
              "schema:description": "Cool: 15 l min⁻¹ Ar; Auxiliary: 0.85 l min⁻¹"
            },
            {
              "@id": "ada:parameter/laSficpmsUPbTAPP/rfPowerDefault",
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
              "@id": "ada:parameter/laSficpmsUPbTAPP/plasmaThermalMode",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/laSficpmsUPbTAPP/plasmaThermalMode"
                }
              ],
              "schema:name": "Plasma Thermal Mode",
              "schema:value": "Normal plasma (1000 W RF)"
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
          "@id": "ada:parameter/laSficpmsUPbTAPP/massResolutionSettingDefault",
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
          "@id": "ada:parameter/laSficpmsUPbTAPP/detectorConfiguration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laSficpmsUPbTAPP/detectorConfiguration"
            }
          ],
          "schema:name": "Detector Configuration",
          "schema:value": "Triple mode detection"
        },
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/icpTuningDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "icpTuningDefault",
          "schema:name": "ICP Tuning",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Same instrument as olivine runs; tuned for normal plasma conditions"
        },
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/memoryEffectMitigationDefault",
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
      "schema:name": "example instrumentName"
    }
  ],
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "In-house MatLab script (Appendix C3)"
    }
  ],
  "ada:ablationSamplingMode": [
    "Spot (stationary)"
  ],
  "ada:ablationSpotDurationDefault": "20 s spot ablation (plus 10 s washout); 25 cycles acquisition",
  "ada:carrierGasFlowRateDefault": "He: MFC-1 0.270 l min⁻¹; MFC-2 0.250 l min⁻¹",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laSficpmsUPbTAPP/plasmaMakeUpGasAdditionDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "plasmaMakeUpGasAdditionDefault",
      "schema:name": "Plasma / Make-up Gas Addition",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Ar make-up: 0.96 l min⁻¹; N₂ not added"
    },
    {
      "@id": "ada:parameter/laSficpmsUPbTAPP/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/multiRunSequentialAnalysisDesign"
        }
      ],
      "schema:name": "Multi-Run Sequential Analysis Design",
      "schema:value": "Single spot analysis run per location (25 cycles: 15 s blank + 20 s ablation + 10 s washout); 3 replicates"
    },
    {
      "@id": "ada:parameter/laSficpmsUPbTAPP/uncertaintyPropagationMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "uncertaintyPropagationMethodDefault",
      "schema:name": "Uncertainty Propagation Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Longerich et al. (1996) for LOD; uncertainty not formally described"
    }
  ],
  "ada:analysisSequenceDefault": "MPI-DING and USGS GRMs at beginning → unknowns → repeated GRM at end",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "²³Na",
      "²⁵Mg",
      "²⁷Al",
      "²⁹Si",
      "³¹P",
      "³⁹K",
      "⁴⁴Ca",
      "⁴⁵Sc",
      "⁴⁷Ti",
      "⁵¹V",
      "⁵³Cr",
      "⁵⁵Mn",
      "⁵⁷Fe",
      "⁵⁹Co",
      "⁶⁰Ni",
      "⁶³Cu",
      "⁶⁶Zn",
      "⁸⁵Rb",
      "⁸⁸Sr",
      "⁸⁹Y",
      "⁹⁰Zr",
      "⁹³Nb",
      "¹³³Cs",
      "¹³⁷Ba",
      "¹³⁹La–¹⁷⁵Lu (all REE)",
      "¹⁸⁰Hf",
      "¹⁸¹Ta",
      "²⁰⁸Pb",
      "²³²Th",
      "²³⁸U (43 nuclides)"
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
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/monitoredIsotopes",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredIsotopes",
        "schema:name": "Monitored Isotopes",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "boolean",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/normalizationStandardsBasedCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "normalizationStandardsBasedCorrection",
        "schema:name": "Normalization / Standards-Based Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "uri",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "uri"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/massResolutionPerAnalyte",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionPerAnalyte",
        "schema:name": "Mass Resolution per Analyte",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:backgroundCountTimeDefault": "8 gas blank scans; 11 ablation scans (25 cycles measurement: 15 s blank + 20 s ablation + 10 s washout)",
  "ada:internalStandardApproach": "Sum-of-major-oxide normalization to 100 wt% (Liu et al. 2008; Appendix C3)",
  "ada:internalStandardElement": "No single IS; oxide sum normalization to 100 wt%",
  "ada:elementalFractionationCorrection": [
    "Oxide sum normalization to 100 wt% corrects for ablation yield and matrix effects; external calibration with MPI-DING and USGS glass GRMs"
  ],
  "ada:signalIntegrationIntervalMethod": "Anomalous time steps excluded (inclusions, cracks, heterogeneity); manual inspection",
  "ada:blankBackgroundCorrectionMethod": "Gas blank measured before each spot analysis (8 scans); average background subtracted",
  "ada:primaryStandardNameDefault": "MPI-DING and USGS glass GRMs (measured at beginning and repeatedly at end of each session; multipoint calibration)",
  "ada:calibrationMeasurementFrequency": "MPI-DING and USGS GRMs measured at beginning and repeatedly at end of each session",
  "ada:secondaryReferenceMaterialDefault": [
    "Same MPI-DING and USGS glasses measured as unknowns for accuracy assessment"
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ageModelDefault": "missing",
  "ada:inheritedOrInitialSignalCorrectionDefault": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:massResolutionAssignment": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS-UPb/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:laSficpmsUPbTAPP-Chernonozhkin2021-3",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Chernonozhkin et al. (2021) Pallasite Phosphate Spot v1",
  "schema:description": "Phosphate phase identification used LA-ICP-MS data combined with EMPA and \u00b5XRF (Fig. D9); merrillite, stanfieldite, farringtonite distinguished by REE patterns; oxide sum normalization applied to phosphate (not olivine IS approach)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-ICP-MS",
      "schema:name": "LA-SF-ICP-MS"
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
      "schema:name": "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent"
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
            "Pallasite Ca-phosphate (merrillite, stanfieldite, farringtonite)"
          ]
        },
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleFormAnalyticalSubstrateDefault",
          "schema:name": "Sample Form / Analytical Substrate",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "In situ \u2014 polished epoxy thick section"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "PMG thick sections polished; same as olivine mapping preparation",
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
            "@id": "ada:parameter/laSficpmsUPbTAPP/signalSmoothingDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "signalSmoothingDefault",
            "schema:name": "Signal Smoothing",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "None"
          },
          {
            "@id": "ada:parameter/laSficpmsUPbTAPP/spikeOutlierFilteringApproachDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "spikeOutlierFilteringApproachDefault",
            "schema:name": "Spike / Outlier Filtering Approach",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Anomalous time steps excluded during manual inspection"
          },
          {
            "@id": "ada:parameter/laSficpmsUPbTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "pulseAnalogDetectorNonlinearityCorrectionDefault",
            "schema:name": "Pulse/Analog Detector Nonlinearity Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Applied: triple mode detection"
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
        "schema:name": "Teledyne CETAC Technologies Analyte G2 (193 nm ArF excimer)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "193 nm ArF excimer; pulse duration ~5 ns",
      "schema:name": "HELEX II two-volume ablation cell",
      "ada:laserSpotGeometryDefault": "110 \u00b5m circular (spot mode)",
      "ada:laserFluenceDefault": "3.5 J cm\u207b\u00b2",
      "ada:laserRepetitionRateDefault": "20 Hz",
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/laserPulseDuration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laSficpmsUPbTAPP/laserPulseDuration"
            }
          ],
          "schema:name": "Laser Pulse Duration",
          "schema:value": "~5 ns (ArF excimer)"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ]
    },
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
              "@id": "ada:parameter/laSficpmsUPbTAPP/interfaceConeConfiguration",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/laSficpmsUPbTAPP/interfaceConeConfiguration"
                }
              ],
              "schema:name": "Interface Cone Configuration",
              "schema:value": "Al standard sample cone (1.1 mm aperture); Al H-type skimmer (0.8 mm aperture)"
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
              "@id": "ada:parameter/laSficpmsUPbTAPP/coolantGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantGasFlowRateDefault",
              "schema:name": "Coolant (Plasma) Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 15,
              "schema:description": "Cool: 15 l min\u207b\u00b9 Ar; Auxiliary: 0.85 l min\u207b\u00b9"
            },
            {
              "@id": "ada:parameter/laSficpmsUPbTAPP/rfPowerDefault",
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
              "@id": "ada:parameter/laSficpmsUPbTAPP/plasmaThermalMode",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/laSficpmsUPbTAPP/plasmaThermalMode"
                }
              ],
              "schema:name": "Plasma Thermal Mode",
              "schema:value": "Normal plasma (1000 W RF)"
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
          "@id": "ada:parameter/laSficpmsUPbTAPP/massResolutionSettingDefault",
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
          "@id": "ada:parameter/laSficpmsUPbTAPP/detectorConfiguration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laSficpmsUPbTAPP/detectorConfiguration"
            }
          ],
          "schema:name": "Detector Configuration",
          "schema:value": "Triple mode detection"
        },
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/icpTuningDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "icpTuningDefault",
          "schema:name": "ICP Tuning",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Same instrument as olivine runs; tuned for normal plasma conditions"
        },
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/memoryEffectMitigationDefault",
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
      "schema:name": "example instrumentName"
    }
  ],
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "In-house MatLab script (Appendix C3)"
    }
  ],
  "ada:ablationSamplingMode": [
    "Spot (stationary)"
  ],
  "ada:ablationSpotDurationDefault": "20 s spot ablation (plus 10 s washout); 25 cycles acquisition",
  "ada:carrierGasFlowRateDefault": "He: MFC-1 0.270 l min\u207b\u00b9; MFC-2 0.250 l min\u207b\u00b9",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laSficpmsUPbTAPP/plasmaMakeUpGasAdditionDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "plasmaMakeUpGasAdditionDefault",
      "schema:name": "Plasma / Make-up Gas Addition",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Ar make-up: 0.96 l min\u207b\u00b9; N\u2082 not added"
    },
    {
      "@id": "ada:parameter/laSficpmsUPbTAPP/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/multiRunSequentialAnalysisDesign"
        }
      ],
      "schema:name": "Multi-Run Sequential Analysis Design",
      "schema:value": "Single spot analysis run per location (25 cycles: 15 s blank + 20 s ablation + 10 s washout); 3 replicates"
    },
    {
      "@id": "ada:parameter/laSficpmsUPbTAPP/uncertaintyPropagationMethodDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "uncertaintyPropagationMethodDefault",
      "schema:name": "Uncertainty Propagation Method",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Longerich et al. (1996) for LOD; uncertainty not formally described"
    }
  ],
  "ada:analysisSequenceDefault": "MPI-DING and USGS GRMs at beginning \u2192 unknowns \u2192 repeated GRM at end",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "\u00b2\u00b3Na",
      "\u00b2\u2075Mg",
      "\u00b2\u2077Al",
      "\u00b2\u2079Si",
      "\u00b3\u00b9P",
      "\u00b3\u2079K",
      "\u2074\u2074Ca",
      "\u2074\u2075Sc",
      "\u2074\u2077Ti",
      "\u2075\u00b9V",
      "\u2075\u00b3Cr",
      "\u2075\u2075Mn",
      "\u2075\u2077Fe",
      "\u2075\u2079Co",
      "\u2076\u2070Ni",
      "\u2076\u00b3Cu",
      "\u2076\u2076Zn",
      "\u2078\u2075Rb",
      "\u2078\u2078Sr",
      "\u2078\u2079Y",
      "\u2079\u2070Zr",
      "\u2079\u00b3Nb",
      "\u00b9\u00b3\u00b3Cs",
      "\u00b9\u00b3\u2077Ba",
      "\u00b9\u00b3\u2079La\u2013\u00b9\u2077\u2075Lu (all REE)",
      "\u00b9\u2078\u2070Hf",
      "\u00b9\u2078\u00b9Ta",
      "\u00b2\u2070\u2078Pb",
      "\u00b2\u00b3\u00b2Th",
      "\u00b2\u00b3\u2078U (43 nuclides)"
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
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/monitoredIsotopes",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredIsotopes",
        "schema:name": "Monitored Isotopes",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "boolean",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/normalizationStandardsBasedCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "normalizationStandardsBasedCorrection",
        "schema:name": "Normalization / Standards-Based Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "uri",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "uri"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/massResolutionPerAnalyte",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionPerAnalyte",
        "schema:name": "Mass Resolution per Analyte",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:backgroundCountTimeDefault": "8 gas blank scans; 11 ablation scans (25 cycles measurement: 15 s blank + 20 s ablation + 10 s washout)",
  "ada:internalStandardApproach": "Sum-of-major-oxide normalization to 100 wt% (Liu et al. 2008; Appendix C3)",
  "ada:internalStandardElement": "No single IS; oxide sum normalization to 100 wt%",
  "ada:elementalFractionationCorrection": [
    "Oxide sum normalization to 100 wt% corrects for ablation yield and matrix effects; external calibration with MPI-DING and USGS glass GRMs"
  ],
  "ada:signalIntegrationIntervalMethod": "Anomalous time steps excluded (inclusions, cracks, heterogeneity); manual inspection",
  "ada:blankBackgroundCorrectionMethod": "Gas blank measured before each spot analysis (8 scans); average background subtracted",
  "ada:primaryStandardNameDefault": "MPI-DING and USGS glass GRMs (measured at beginning and repeatedly at end of each session; multipoint calibration)",
  "ada:calibrationMeasurementFrequency": "MPI-DING and USGS GRMs measured at beginning and repeatedly at end of each session",
  "ada:secondaryReferenceMaterialDefault": [
    "Same MPI-DING and USGS glasses measured as unknowns for accuracy assessment"
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ageModelDefault": "missing",
  "ada:inheritedOrInitialSignalCorrectionDefault": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:massResolutionAssignment": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
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

ex:laSficpmsUPbTAPP-Chernonozhkin2021-3 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "PMG thick sections polished; same as olivine mapping preparation" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault>,
                        <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/signalSmoothingDefault>,
                        <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/spikeOutlierFilteringApproachDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/multiRunSequentialAnalysisDesign>,
        <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/plasmaMakeUpGasAdditionDefault>,
        <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/uncertaintyPropagationMethodDefault> ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Chernonozhkin, Pittarello, Goderis, Vanhaecke et al." ] ;
    schema1:datePublished "missing" ;
    schema1:description "Phosphate phase identification used LA-ICP-MS data combined with EMPA and µXRF (Fig. D9); merrillite, stanfieldite, farringtonite distinguished by REE patterns; oxide sum normalization applied to phosphate (not olivine IS approach)" ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent" ] ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/detectorConfiguration>,
                <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/icpTuningDefault>,
                <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/massResolutionSettingDefault>,
                <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/memoryEffectMitigationDefault> ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "Double-focusing sector field ICP-MS (explicitly stated)",
                "ICPMS" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Torch" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/interfaceConeConfiguration> ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Interface Cone" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/coolantGasFlowRateDefault>,
                        <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/plasmaThermalMode>,
                        <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/rfPowerDefault> ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "ICP Source" ;
                    schema1:name "missing" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "Thermo Fisher Scientific Element XR (SF-ICP-MS)" ] ;
            schema1:name "example instrumentName" ],
        [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/laserPulseDuration> ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "Laser Ablation System" ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "Teledyne CETAC Technologies Analyte G2 (193 nm ArF excimer)" ] ;
            schema1:name "HELEX II two-volume ablation cell" ;
            ada:laserFluenceDefault "3.5 J cm⁻²" ;
            ada:laserRepetitionRateDefault "20 Hz" ;
            ada:laserSpotGeometryDefault "110 µm circular (spot mode)" ;
            ada:laserType "193 nm ArF excimer; pulse duration ~5 ns" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "Dept. of Chemistry, Atomic & Mass Spectrometry, Ghent University, Belgium" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "LA-SF-ICP-MS" ;
            schema1:termCode "LA-ICP-MS" ] ;
    schema1:name "Chernonozhkin et al. (2021) Pallasite Phosphate Spot v1" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Pallasite Ca-phosphate (merrillite, stanfieldite, farringtonite)" ],
                <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Chernonozhkin et al. (2021) Chem. Geol. 562; Liu et al. (2008) for IS method" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:ablationPitDepthRateDefault "missing" ;
    ada:ablationSamplingMode "Spot (stationary)" ;
    ada:ablationSpotDurationDefault "20 s spot ablation (plus 10 s washout); 25 cycles acquisition" ;
    ada:ageModelDefault "missing" ;
    ada:analysisSequenceDefault "MPI-DING and USGS GRMs at beginning → unknowns → repeated GRM at end" ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/detectionLimit>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/detectionLimitMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/isobaricInterferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/limitOfQuantificationMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/massResolutionPerAnalyte>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/monitoredIsotopes>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/normalizationStandardsBasedCorrection>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ;
            ada:defaultAnalytes "²³Na",
                "²³²Th",
                "²³⁸U (43 nuclides)",
                "²⁰⁸Pb",
                "²⁵Mg",
                "²⁷Al",
                "²⁹Si",
                "³¹P",
                "³⁹K",
                "¹³³Cs",
                "¹³⁷Ba",
                "¹³⁹La–¹⁷⁵Lu (all REE)",
                "¹⁸¹Ta",
                "¹⁸⁰Hf",
                "⁴⁴Ca",
                "⁴⁵Sc",
                "⁴⁷Ti",
                "⁵³Cr",
                "⁵¹V",
                "⁵⁵Mn",
                "⁵⁷Fe",
                "⁵⁹Co",
                "⁶³Cu",
                "⁶⁰Ni",
                "⁶⁶Zn",
                "⁸⁵Rb",
                "⁸⁸Sr",
                "⁸⁹Y",
                "⁹³Nb",
                "⁹⁰Zr" ] ;
    ada:backgroundCountTimeDefault "8 gas blank scans; 11 ablation scans (25 cycles measurement: 15 s blank + 20 s ablation + 10 s washout)" ;
    ada:blankBackgroundCorrectionMethod "Gas blank measured before each spot analysis (8 scans); average background subtracted" ;
    ada:calibrationMeasurementFrequency "MPI-DING and USGS GRMs measured at beginning and repeatedly at end of each session" ;
    ada:carrierGasFlowRateDefault "He: MFC-1 0.270 l min⁻¹; MFC-2 0.250 l min⁻¹" ;
    ada:elementalFractionationCorrection "Oxide sum normalization to 100 wt% corrects for ablation yield and matrix effects; external calibration with MPI-DING and USGS glass GRMs" ;
    ada:inheritedOrInitialSignalCorrectionDefault "missing" ;
    ada:internalStandardApproach "Sum-of-major-oxide normalization to 100 wt% (Liu et al. 2008; Appendix C3)" ;
    ada:internalStandardElement "No single IS; oxide sum normalization to 100 wt%" ;
    ada:ionCounterDeadTimeDefault -9999 ;
    ada:massBiasCorrectionStrategy "missing" ;
    ada:massResolutionAssignment "missing" ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:primaryStandardNameDefault "MPI-DING and USGS glass GRMs (measured at beginning and repeatedly at end of each session; multipoint calibration)" ;
    ada:rasterLineSpacingDefault "missing" ;
    ada:sampleIntroduction "missing" ;
    ada:samplingUnit "missing" ;
    ada:secondaryReferenceMaterialDefault "Same MPI-DING and USGS glasses measured as unknowns for accuracy assessment" ;
    ada:signalIntegrationIntervalMethod "Anomalous time steps excluded (inclusions, cracks, heterogeneity); manual inspection" ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:totalIntegrationTimePerOutputDataPointDefault "missing" ;
    ada:uncertaintyLevel "missing" ;
    bios:computationalTool [ schema1:name "In-house MatLab script (Appendix C3)" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/detectionLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimit" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/detectionLimitMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Detection Limit Method" ;
    schema1:valueName "detectionLimitMethod" ;
    ada:dataType "uri" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/isobaricInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Isobaric Interference Corrections Applied" ;
    schema1:valueName "isobaricInterferenceCorrectionsApplied" ;
    ada:dataType "boolean" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "uri" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/massResolutionPerAnalyte> a schema1:PropertyValueSpecification ;
    schema1:name "Mass Resolution per Analyte" ;
    schema1:valueName "massResolutionPerAnalyte" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/monitoredIsotopes> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Monitored Isotopes" ;
    schema1:valueName "monitoredIsotopes" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/normalizationStandardsBasedCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Normalization / Standards-Based Correction" ;
    schema1:valueName "normalizationStandardsBasedCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/coolantGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 15 ;
    schema1:description "Cool: 15 l min⁻¹ Ar; Auxiliary: 0.85 l min⁻¹" ;
    schema1:name "Coolant (Plasma) Gas Flow Rate" ;
    schema1:valueName "coolantGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/icpTuningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Same instrument as olivine runs; tuned for normal plasma conditions" ;
    schema1:name "ICP Tuning" ;
    schema1:valueName "icpTuningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/massResolutionSettingDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Low resolution (M/ΔM = 300)" ;
    schema1:name "Mass Resolution Setting" ;
    schema1:valueName "massResolutionSettingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/memoryEffectMitigationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "10 s washout time after 20 s spot ablation (specified in acquisition protocol)" ;
    schema1:name "Memory Effect Mitigation" ;
    schema1:valueName "memoryEffectMitigationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/plasmaMakeUpGasAdditionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Ar make-up: 0.96 l min⁻¹; N₂ not added" ;
    schema1:name "Plasma / Make-up Gas Addition" ;
    schema1:valueName "plasmaMakeUpGasAdditionDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Applied: triple mode detection" ;
    schema1:name "Pulse/Analog Detector Nonlinearity Correction" ;
    schema1:valueName "pulseAnalogDetectorNonlinearityCorrectionDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/rfPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1000 ;
    schema1:description "1000 W" ;
    schema1:name "RF Power" ;
    schema1:valueName "rfPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "In situ — polished epoxy thick section" ;
    schema1:name "Sample Form / Analytical Substrate" ;
    schema1:valueName "sampleFormAnalyticalSubstrateDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/signalSmoothingDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "None" ;
    schema1:name "Signal Smoothing" ;
    schema1:valueName "signalSmoothingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/spikeOutlierFilteringApproachDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Anomalous time steps excluded during manual inspection" ;
    schema1:name "Spike / Outlier Filtering Approach" ;
    schema1:valueName "spikeOutlierFilteringApproachDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/uncertaintyPropagationMethodDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Longerich et al. (1996) for LOD; uncertainty not formally described" ;
    schema1:name "Uncertainty Propagation Method" ;
    schema1:valueName "uncertaintyPropagationMethodDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/detectorConfiguration> a schema1:PropertyValue ;
    schema1:name "Detector Configuration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/detectorConfiguration> ;
    schema1:value "Triple mode detection" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/interfaceConeConfiguration> a schema1:PropertyValue ;
    schema1:name "Interface Cone Configuration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/interfaceConeConfiguration> ;
    schema1:value "Al standard sample cone (1.1 mm aperture); Al H-type skimmer (0.8 mm aperture)" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/laserPulseDuration> a schema1:PropertyValue ;
    schema1:name "Laser Pulse Duration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/laserPulseDuration> ;
    schema1:value "~5 ns (ArF excimer)" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/multiRunSequentialAnalysisDesign> a schema1:PropertyValue ;
    schema1:name "Multi-Run Sequential Analysis Design" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/multiRunSequentialAnalysisDesign> ;
    schema1:value "Single spot analysis run per location (25 cycles: 15 s blank + 20 s ablation + 10 s washout); 3 replicates" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/plasmaThermalMode> a schema1:PropertyValue ;
    schema1:name "Plasma Thermal Mode" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/plasmaThermalMode> ;
    schema1:value "Normal plasma (1000 W RF)" .


```


### laSficpmsUPbTAPP example Mittlefehldt2024
laSficpmsUPbTAPP instance derived from Mittlefehldt 2024 Appendix A Pallasite olivine Spot analysis ns-LA-SF-ICP-MS Johnson Space Center.
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
  "@id": "ex:laSficpmsUPbTAPP-Mittlefehldt2024",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Mittlefehldt (2024) Pallasite Olivine Spot v1",
  "schema:description": "Many instrument parameters lost during extended lab shutdown; 75 µm spot size in medium resolution mode on sector-field ICP-MS is unusual combination for olivine trace elements; 25 Mg IS from EPMA is standard approach",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-ICP-MS",
      "schema:name": "LA-SF-ICP-MS"
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
            "Pallasite olivine ([Mg,Fe]₂SiO₄)"
          ]
        },
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleFormAnalyticalSubstrateDefault",
          "schema:name": "Sample Form / Analytical Substrate",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "In situ — polished grain mount (olivine grain fragments)"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Olivine grain fragments repeatedly washed in dilute HCl and triply distilled H₂O, hand-picked, polished grain mounts",
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
            "@id": "ada:parameter/laSficpmsUPbTAPP/spikeOutlierFilteringApproachDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "spikeOutlierFilteringApproachDefault",
            "schema:name": "Spike / Outlier Filtering Approach",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Time steps with enhanced P, Ca, Co, Ni, Zn excluded (inclusions and heterogeneities); Grubb's test applied to EPMA data for outlier detection"
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
        "schema:name": "New Wave UP-193 (solid state, 193 nm)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "193 nm solid-state (New Wave UP-193)",
      "ada:laserSpotGeometryDefault": "75 µm circular",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "ICPMS",
        "Single-collector sector-field (SF-ICP-MS)",
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
          "@id": "ada:parameter/laSficpmsUPbTAPP/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Medium resolution (m/Δm ≈ 4000)"
        }
      ],
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
      "schema:name": "Excel spreadsheets developed by C.-T. A. Lee (Rice University)"
    }
  ],
  "ada:ablationSamplingMode": [
    "Spot (stationary)"
  ],
  "ada:analysisSequenceDefault": "BCR-2g, BHVO-2g, BIR-1g measured as calibration standards; Marjalahti as in-session control",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "²⁵Mg",
      "²⁷Al",
      "³¹P",
      "⁴³Ca",
      "⁴⁴Ca",
      "⁴⁵Sc",
      "⁴⁷Ti",
      "⁴⁹Ti",
      "⁵¹V",
      "⁵²Cr",
      "⁵³Cr",
      "⁵⁹Co",
      "⁶⁰Ni",
      "⁶¹Ni",
      "⁶²Ni",
      "⁶⁴Zn",
      "⁶⁶Zn",
      "⁶⁹Ga",
      "⁷¹Ga (19 nuclides)"
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
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/monitoredIsotopes",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredIsotopes",
        "schema:name": "Monitored Isotopes",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "boolean",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/normalizationStandardsBasedCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "normalizationStandardsBasedCorrection",
        "schema:name": "Normalization / Standards-Based Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "uri",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "uri"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/massResolutionPerAnalyte",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionPerAnalyte",
        "schema:name": "Mass Resolution per Analyte",
        "ada:dataType": "string"
      }
    ]
  },
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laSficpmsUPbTAPP/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/multiRunSequentialAnalysisDesign"
        }
      ],
      "schema:name": "Multi-Run Sequential Analysis Design",
      "schema:value": "Single spot per location (75 µm circular)"
    }
  ],
  "ada:internalStandardApproach": "Single element from EPMA: ²⁵Mg; the EMPA data used as the standardizing values",
  "ada:internalStandardElement": "²⁵Mg (indexing element; Mg concentration from EMPA)",
  "ada:elementalFractionationCorrection": [
    "External calibration using BCR-2g, BHVO-2g, BIR-1g; ²⁵Mg IS from EPMA corrects for ablation yield variation; no explicit downhole fractionation correction described"
  ],
  "ada:signalIntegrationIntervalMethod": "Time steps with enhanced P, Ca, Co, Ni, Zn count rates (indicating inclusions or cracks) excluded from integration; manual inspection",
  "ada:blankBackgroundCorrectionMethod": "Gas blank measured before each analysis (laser shutter closed); time steps with background-level signals excluded during data reduction",
  "ada:primaryStandardNameDefault": "USGS standard glasses BCR-2g, BHVO-2g, and BIR-1g; preferred values from GeoReM website",
  "ada:secondaryReferenceMaterialDefault": [
    "BCR-2G, BHVO-2G, BIR-1G processed as unknowns alongside samples (same standards as calibration — in-session validation)"
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ablationSpotDurationDefault": -9999,
  "ada:ageModelDefault": "missing",
  "ada:backgroundCountTimeDefault": -9999,
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:carrierGasFlowRateDefault": "missing",
  "ada:inheritedOrInitialSignalCorrectionDefault": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:massResolutionAssignment": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS-UPb/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:laSficpmsUPbTAPP-Mittlefehldt2024",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Mittlefehldt (2024) Pallasite Olivine Spot v1",
  "schema:description": "Many instrument parameters lost during extended lab shutdown; 75 \u00b5m spot size in medium resolution mode on sector-field ICP-MS is unusual combination for olivine trace elements; 25 Mg IS from EPMA is standard approach",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-ICP-MS",
      "schema:name": "LA-SF-ICP-MS"
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
            "Pallasite olivine ([Mg,Fe]\u2082SiO\u2084)"
          ]
        },
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleFormAnalyticalSubstrateDefault",
          "schema:name": "Sample Form / Analytical Substrate",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "In situ \u2014 polished grain mount (olivine grain fragments)"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Olivine grain fragments repeatedly washed in dilute HCl and triply distilled H\u2082O, hand-picked, polished grain mounts",
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
            "@id": "ada:parameter/laSficpmsUPbTAPP/spikeOutlierFilteringApproachDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "spikeOutlierFilteringApproachDefault",
            "schema:name": "Spike / Outlier Filtering Approach",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Time steps with enhanced P, Ca, Co, Ni, Zn excluded (inclusions and heterogeneities); Grubb's test applied to EPMA data for outlier detection"
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
        "schema:name": "New Wave UP-193 (solid state, 193 nm)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "193 nm solid-state (New Wave UP-193)",
      "ada:laserSpotGeometryDefault": "75 \u00b5m circular",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "ICPMS",
        "Single-collector sector-field (SF-ICP-MS)",
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
          "@id": "ada:parameter/laSficpmsUPbTAPP/massResolutionSettingDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "massResolutionSettingDefault",
          "schema:name": "Mass Resolution Setting",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Medium resolution (m/\u0394m \u2248 4000)"
        }
      ],
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
      "schema:name": "Excel spreadsheets developed by C.-T. A. Lee (Rice University)"
    }
  ],
  "ada:ablationSamplingMode": [
    "Spot (stationary)"
  ],
  "ada:analysisSequenceDefault": "BCR-2g, BHVO-2g, BIR-1g measured as calibration standards; Marjalahti as in-session control",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "\u00b2\u2075Mg",
      "\u00b2\u2077Al",
      "\u00b3\u00b9P",
      "\u2074\u00b3Ca",
      "\u2074\u2074Ca",
      "\u2074\u2075Sc",
      "\u2074\u2077Ti",
      "\u2074\u2079Ti",
      "\u2075\u00b9V",
      "\u2075\u00b2Cr",
      "\u2075\u00b3Cr",
      "\u2075\u2079Co",
      "\u2076\u2070Ni",
      "\u2076\u00b9Ni",
      "\u2076\u00b2Ni",
      "\u2076\u2074Zn",
      "\u2076\u2076Zn",
      "\u2076\u2079Ga",
      "\u2077\u00b9Ga (19 nuclides)"
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
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/monitoredIsotopes",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredIsotopes",
        "schema:name": "Monitored Isotopes",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "boolean",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/normalizationStandardsBasedCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "normalizationStandardsBasedCorrection",
        "schema:name": "Normalization / Standards-Based Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "uri",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "uri"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/massResolutionPerAnalyte",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionPerAnalyte",
        "schema:name": "Mass Resolution per Analyte",
        "ada:dataType": "string"
      }
    ]
  },
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laSficpmsUPbTAPP/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/multiRunSequentialAnalysisDesign"
        }
      ],
      "schema:name": "Multi-Run Sequential Analysis Design",
      "schema:value": "Single spot per location (75 \u00b5m circular)"
    }
  ],
  "ada:internalStandardApproach": "Single element from EPMA: \u00b2\u2075Mg; the EMPA data used as the standardizing values",
  "ada:internalStandardElement": "\u00b2\u2075Mg (indexing element; Mg concentration from EMPA)",
  "ada:elementalFractionationCorrection": [
    "External calibration using BCR-2g, BHVO-2g, BIR-1g; \u00b2\u2075Mg IS from EPMA corrects for ablation yield variation; no explicit downhole fractionation correction described"
  ],
  "ada:signalIntegrationIntervalMethod": "Time steps with enhanced P, Ca, Co, Ni, Zn count rates (indicating inclusions or cracks) excluded from integration; manual inspection",
  "ada:blankBackgroundCorrectionMethod": "Gas blank measured before each analysis (laser shutter closed); time steps with background-level signals excluded during data reduction",
  "ada:primaryStandardNameDefault": "USGS standard glasses BCR-2g, BHVO-2g, and BIR-1g; preferred values from GeoReM website",
  "ada:secondaryReferenceMaterialDefault": [
    "BCR-2G, BHVO-2G, BIR-1G processed as unknowns alongside samples (same standards as calibration \u2014 in-session validation)"
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ablationSpotDurationDefault": -9999,
  "ada:ageModelDefault": "missing",
  "ada:backgroundCountTimeDefault": -9999,
  "ada:calibrationMeasurementFrequency": "missing",
  "ada:carrierGasFlowRateDefault": "missing",
  "ada:inheritedOrInitialSignalCorrectionDefault": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:massResolutionAssignment": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
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

ex:laSficpmsUPbTAPP-Mittlefehldt2024 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Olivine grain fragments repeatedly washed in dilute HCl and triply distilled H₂O, hand-picked, polished grain mounts" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/spikeOutlierFilteringApproachDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/multiRunSequentialAnalysisDesign> ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Mittlefehldt" ] ;
    schema1:datePublished "missing" ;
    schema1:description "Many instrument parameters lost during extended lab shutdown; 75 µm spot size in medium resolution mode on sector-field ICP-MS is unusual combination for olivine trace elements; 25 Mg IS from EPMA is standard approach" ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "Laser Ablation System" ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "New Wave UP-193 (solid state, 193 nm)" ] ;
            schema1:name "example instrumentName" ;
            ada:laserSpotGeometryDefault "75 µm circular" ;
            ada:laserType "193 nm solid-state (New Wave UP-193)" ],
        [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/massResolutionSettingDefault> ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "ICPMS",
                "Single-collector sector-field (SF-ICP-MS)" ;
            schema1:hasPart [ a schema1:Product,
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
                    schema1:name "Thermo Fisher Scientific Element XR (SF-ICP-MS)" ] ;
            schema1:name "example instrumentName" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "ICP-MS Laboratory, NASA Johnson Space Center, Houston TX, USA" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "LA-SF-ICP-MS" ;
            schema1:termCode "LA-ICP-MS" ] ;
    schema1:name "Mittlefehldt (2024) Pallasite Olivine Spot v1" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Pallasite olivine ([Mg,Fe]₂SiO₄)" ],
                <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Mittlefehldt (2024) GCA; Lee (Rice University) Excel data reduction spreadsheet" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:ablationPitDepthRateDefault "missing" ;
    ada:ablationSamplingMode "Spot (stationary)" ;
    ada:ablationSpotDurationDefault -9999 ;
    ada:ageModelDefault "missing" ;
    ada:analysisSequenceDefault "BCR-2g, BHVO-2g, BIR-1g measured as calibration standards; Marjalahti as in-session control" ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/detectionLimit>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/detectionLimitMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/isobaricInterferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/limitOfQuantificationMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/massResolutionPerAnalyte>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/monitoredIsotopes>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/normalizationStandardsBasedCorrection>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ;
            ada:defaultAnalytes "²⁵Mg",
                "²⁷Al",
                "³¹P",
                "⁴³Ca",
                "⁴⁴Ca",
                "⁴⁵Sc",
                "⁴⁷Ti",
                "⁴⁹Ti",
                "⁵²Cr",
                "⁵³Cr",
                "⁵¹V",
                "⁵⁹Co",
                "⁶²Ni",
                "⁶¹Ni",
                "⁶⁰Ni",
                "⁶⁴Zn",
                "⁶⁶Zn",
                "⁶⁹Ga",
                "⁷¹Ga (19 nuclides)" ] ;
    ada:backgroundCountTimeDefault -9999 ;
    ada:blankBackgroundCorrectionMethod "Gas blank measured before each analysis (laser shutter closed); time steps with background-level signals excluded during data reduction" ;
    ada:calibrationMeasurementFrequency "missing" ;
    ada:carrierGasFlowRateDefault "missing" ;
    ada:elementalFractionationCorrection "External calibration using BCR-2g, BHVO-2g, BIR-1g; ²⁵Mg IS from EPMA corrects for ablation yield variation; no explicit downhole fractionation correction described" ;
    ada:inheritedOrInitialSignalCorrectionDefault "missing" ;
    ada:internalStandardApproach "Single element from EPMA: ²⁵Mg; the EMPA data used as the standardizing values" ;
    ada:internalStandardElement "²⁵Mg (indexing element; Mg concentration from EMPA)" ;
    ada:ionCounterDeadTimeDefault -9999 ;
    ada:massBiasCorrectionStrategy "missing" ;
    ada:massResolutionAssignment "missing" ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:primaryStandardNameDefault "USGS standard glasses BCR-2g, BHVO-2g, and BIR-1g; preferred values from GeoReM website" ;
    ada:rasterLineSpacingDefault "missing" ;
    ada:sampleIntroduction "missing" ;
    ada:samplingUnit "missing" ;
    ada:secondaryReferenceMaterialDefault "BCR-2G, BHVO-2G, BIR-1G processed as unknowns alongside samples (same standards as calibration — in-session validation)" ;
    ada:signalIntegrationIntervalMethod "Time steps with enhanced P, Ca, Co, Ni, Zn count rates (indicating inclusions or cracks) excluded from integration; manual inspection" ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:totalIntegrationTimePerOutputDataPointDefault "missing" ;
    ada:uncertaintyLevel "missing" ;
    bios:computationalTool [ schema1:name "Excel spreadsheets developed by C.-T. A. Lee (Rice University)" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/detectionLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimit" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/detectionLimitMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Detection Limit Method" ;
    schema1:valueName "detectionLimitMethod" ;
    ada:dataType "uri" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/isobaricInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Isobaric Interference Corrections Applied" ;
    schema1:valueName "isobaricInterferenceCorrectionsApplied" ;
    ada:dataType "boolean" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "uri" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/massResolutionPerAnalyte> a schema1:PropertyValueSpecification ;
    schema1:name "Mass Resolution per Analyte" ;
    schema1:valueName "massResolutionPerAnalyte" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/monitoredIsotopes> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Monitored Isotopes" ;
    schema1:valueName "monitoredIsotopes" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/normalizationStandardsBasedCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Normalization / Standards-Based Correction" ;
    schema1:valueName "normalizationStandardsBasedCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/massResolutionSettingDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Medium resolution (m/Δm ≈ 4000)" ;
    schema1:name "Mass Resolution Setting" ;
    schema1:valueName "massResolutionSettingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "In situ — polished grain mount (olivine grain fragments)" ;
    schema1:name "Sample Form / Analytical Substrate" ;
    schema1:valueName "sampleFormAnalyticalSubstrateDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/spikeOutlierFilteringApproachDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Time steps with enhanced P, Ca, Co, Ni, Zn excluded (inclusions and heterogeneities); Grubb's test applied to EPMA data for outlier detection" ;
    schema1:name "Spike / Outlier Filtering Approach" ;
    schema1:valueName "spikeOutlierFilteringApproachDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/multiRunSequentialAnalysisDesign> a schema1:PropertyValue ;
    schema1:name "Multi-Run Sequential Analysis Design" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/multiRunSequentialAnalysisDesign> ;
    schema1:value "Single spot per location (75 µm circular)" .


```


### laSficpmsUPbTAPP example Navarro2024
laSficpmsUPbTAPP instance derived from Navarro et al. 2024 (ACS ESC 8) Iron meteorites Spot analysis ns-LA-SF-ICP-MS University of Campinas.
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
  "@id": "ex:laSficpmsUPbTAPP-Navarro2024",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Navarro et al. (2024) Iron Meteorite Spot v1",
  "schema:description": "Key innovations: (1) use of two measurement standards (NIST SRM 612 + North Chile) with yield correction in iolite 3D DRS; (2) Fe+Ni+Co=100% normalization eliminates need for EPMA IS; Cr results not quantitative due to argide interferences",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-ICP-MS",
      "schema:name": "LA-SF-ICP-MS"
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
      "schema:name": "FAPESP (São Paulo Research Foundation); CNPq"
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
            "Iron meteorite metal (kamacite + taenite)"
          ]
        },
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleFormAnalyticalSubstrateDefault",
          "schema:name": "Sample Form / Analytical Substrate",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "In situ — polished epoxy mount (~1 cm fragments in epoxy, etched with Nital)"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Fragments ~1 cm mounted in epoxy resin, polished, cleaned with ultrapure water",
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
            "@id": "ada:parameter/laSficpmsUPbTAPP/guardElectrode",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/laSficpmsUPbTAPP/guardElectrode"
              }
            ],
            "schema:name": "Guard Electrode",
            "schema:value": "On (active)"
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
            "@id": "ada:parameter/laSficpmsUPbTAPP/signalSmoothingDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "signalSmoothingDefault",
            "schema:name": "Signal Smoothing",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "None"
          },
          {
            "@id": "ada:parameter/laSficpmsUPbTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "pulseAnalogDetectorNonlinearityCorrectionDefault",
            "schema:name": "Pulse/Analog Detector Nonlinearity Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Applied: triple mode detector (pulse counting, analog, Faraday); low relative abundance isotopes chosen for Ni and Fe to allow analog mode measurement of major matrix elements"
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
        "schema:name": "Teledyne Excite 193 (193 nm ArF excimer)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "193 nm ArF excimer; pulse duration 4 ns",
      "schema:name": "HelEx II two-volume sample cell",
      "ada:laserSpotGeometryDefault": "150 µm circular",
      "ada:laserFluenceDefault": "7 J cm⁻²",
      "ada:laserRepetitionRateDefault": "10 Hz",
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/laserPulseDuration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laSficpmsUPbTAPP/laserPulseDuration"
            }
          ],
          "schema:name": "Laser Pulse Duration",
          "schema:value": "4 ns (ArF excimer Excite 193)"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ]
    },
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
              "@id": "ada:parameter/laSficpmsUPbTAPP/interfaceConeConfiguration",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/laSficpmsUPbTAPP/interfaceConeConfiguration"
                }
              ],
              "schema:name": "Interface Cone Configuration",
              "schema:value": "Ni sampler cone; Ni skimmer cone"
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
              "@id": "ada:parameter/laSficpmsUPbTAPP/coolantGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantGasFlowRateDefault",
              "schema:name": "Coolant (Plasma) Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 16,
              "schema:description": "Plasma gas: 16 l min⁻¹; Auxiliary: 0.9 l min⁻¹; Nebulizer gas (from table): 1.1 l min⁻¹"
            },
            {
              "@id": "ada:parameter/laSficpmsUPbTAPP/rfPowerDefault",
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
          "@id": "ada:parameter/laSficpmsUPbTAPP/massResolutionSettingDefault",
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
          "@id": "ada:parameter/laSficpmsUPbTAPP/detectorConfiguration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laSficpmsUPbTAPP/detectorConfiguration"
            }
          ],
          "schema:name": "Detector Configuration",
          "schema:value": "Triple mode detector (pulse counting, analog, Faraday)"
        },
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/icpTuningDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "icpTuningDefault",
          "schema:name": "ICP Tuning",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "ICP and laser settings optimized daily for optimum signal intensity and low oxide formation (factory specifications; mass calibration and detector cross-calibration checked and redone if required)"
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
      "schema:name": "iolite 4.5.7 with 3D Trace Elements DRS"
    }
  ],
  "ada:ablationSamplingMode": [
    "Spot (stationary)"
  ],
  "ada:ablationSpotDurationDefault": "40 s on-sample ablation (after 20 s background measurement)",
  "ada:carrierGasFlowRateDefault": "He: 0.6 l min⁻¹ (MFC 1) + 0.7 l min⁻¹ (MFC 2) in HelEx II cell; combined with Ar makeup via T-piece near torch",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laSficpmsUPbTAPP/plasmaMakeUpGasAdditionDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "plasmaMakeUpGasAdditionDefault",
      "schema:name": "Plasma / Make-up Gas Addition",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Ar make-up gas (combined via T-piece in sample transport line near torch; flow rate not stated separately)"
    },
    {
      "@id": "ada:parameter/laSficpmsUPbTAPP/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/multiRunSequentialAnalysisDesign"
        }
      ],
      "schema:name": "Multi-Run Sequential Analysis Design",
      "schema:value": "Single acquisition run (20 spot analyses per sample under repeatability conditions)"
    }
  ],
  "ada:analysisSequenceDefault": "NIST SRM 612(×3) → North Chile(×3) → unknowns(×10) → NIST SRM 612(×2) → North Chile(×2) → unknowns(×10) → … (bracketing every 15)",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "⁵²Cr",
      "⁵⁷Fe",
      "⁵⁹Co",
      "⁶¹Ni",
      "⁶⁵Cu",
      "⁶⁹Ga",
      "⁷²Ge",
      "⁷⁵As",
      "⁹⁹Ru",
      "¹⁰³Rh",
      "¹⁰⁵Pd",
      "¹⁸²W",
      "¹⁸⁵Re",
      "¹⁸⁹Os",
      "¹⁹³Ir",
      "¹⁹⁵Pt",
      "¹⁹⁷Au (17 isotopes)",
      "low relative abundance isotopes chosen for Ni and Fe (analog mode)"
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
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/monitoredIsotopes",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredIsotopes",
        "schema:name": "Monitored Isotopes",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "boolean",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/normalizationStandardsBasedCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "normalizationStandardsBasedCorrection",
        "schema:name": "Normalization / Standards-Based Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "uri",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "uri"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/massResolutionPerAnalyte",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionPerAnalyte",
        "schema:name": "Mass Resolution per Analyte",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:backgroundCountTimeDefault": "20 s background measurement (laser shutter closed) before each 40 s ablation",
  "ada:internalStandardApproach": "Fe+Ni+Co sum normalization to 100% using iolite 3D Trace Elements DRS (eliminates need for independent EPMA IS)",
  "ada:internalStandardElement": "No single IS; Fe+Ni+Co mass fractions normalized to 100% via iolite 3D DRS (yield correction factors applied for NIST SRM 612 relative to North Chile)",
  "ada:elementalFractionationCorrection": [
    "External calibration using North Chile iron meteorite + NIST SRM 612 glass (yield correction applied in iolite 3D DRS for NIST relative to North Chile); ordinary least-squares fitting per 15 min calibration block; Fe+Ni+Co normalization eliminates need for independent EPMA IS"
  ],
  "ada:signalIntegrationIntervalMethod": "Time-resolved LA-ICP-MS signals inspected per analysis; background interval (20 s) and ablation interval (40 s) selected; no automated spike exclusion described",
  "ada:blankBackgroundCorrectionMethod": "Background signal measured for 20 s (laser shutter closed) before each 40 s ablation; background mean subtracted per isotope in iolite",
  "ada:primaryStandardNameDefault": "NIST SRM 612 glass (Jochum et al. 2011) + North Chile Filomena iron meteorite (Wasson et al. 1989) — used together with yield correction in iolite 3D DRS",
  "ada:calibrationMeasurementFrequency": "NIST SRM 612 and North Chile measured bracketing every 15 unknowns: 3×STD → 3×STD → 10×unknowns → repeat",
  "ada:secondaryReferenceMaterialDefault": [
    "North Chile Filomena measured as unknown on different days over 4 months to assess intermediate precision (Table 3 and Fig. 2)"
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ageModelDefault": "missing",
  "ada:inheritedOrInitialSignalCorrectionDefault": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:massResolutionAssignment": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS-UPb/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:laSficpmsUPbTAPP-Navarro2024",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Navarro et al. (2024) Iron Meteorite Spot v1",
  "schema:description": "Key innovations: (1) use of two measurement standards (NIST SRM 612 + North Chile) with yield correction in iolite 3D DRS; (2) Fe+Ni+Co=100% normalization eliminates need for EPMA IS; Cr results not quantitative due to argide interferences",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-ICP-MS",
      "schema:name": "LA-SF-ICP-MS"
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
      "schema:name": "FAPESP (S\u00e3o Paulo Research Foundation); CNPq"
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
            "Iron meteorite metal (kamacite + taenite)"
          ]
        },
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleFormAnalyticalSubstrateDefault",
          "schema:name": "Sample Form / Analytical Substrate",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "In situ \u2014 polished epoxy mount (~1 cm fragments in epoxy, etched with Nital)"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Fragments ~1 cm mounted in epoxy resin, polished, cleaned with ultrapure water",
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
            "@id": "ada:parameter/laSficpmsUPbTAPP/guardElectrode",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/laSficpmsUPbTAPP/guardElectrode"
              }
            ],
            "schema:name": "Guard Electrode",
            "schema:value": "On (active)"
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
            "@id": "ada:parameter/laSficpmsUPbTAPP/signalSmoothingDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "signalSmoothingDefault",
            "schema:name": "Signal Smoothing",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "None"
          },
          {
            "@id": "ada:parameter/laSficpmsUPbTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "pulseAnalogDetectorNonlinearityCorrectionDefault",
            "schema:name": "Pulse/Analog Detector Nonlinearity Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Applied: triple mode detector (pulse counting, analog, Faraday); low relative abundance isotopes chosen for Ni and Fe to allow analog mode measurement of major matrix elements"
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
        "schema:name": "Teledyne Excite 193 (193 nm ArF excimer)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "193 nm ArF excimer; pulse duration 4 ns",
      "schema:name": "HelEx II two-volume sample cell",
      "ada:laserSpotGeometryDefault": "150 \u00b5m circular",
      "ada:laserFluenceDefault": "7 J cm\u207b\u00b2",
      "ada:laserRepetitionRateDefault": "10 Hz",
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/laserPulseDuration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laSficpmsUPbTAPP/laserPulseDuration"
            }
          ],
          "schema:name": "Laser Pulse Duration",
          "schema:value": "4 ns (ArF excimer Excite 193)"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ]
    },
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
              "@id": "ada:parameter/laSficpmsUPbTAPP/interfaceConeConfiguration",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/laSficpmsUPbTAPP/interfaceConeConfiguration"
                }
              ],
              "schema:name": "Interface Cone Configuration",
              "schema:value": "Ni sampler cone; Ni skimmer cone"
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
              "@id": "ada:parameter/laSficpmsUPbTAPP/coolantGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantGasFlowRateDefault",
              "schema:name": "Coolant (Plasma) Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 16,
              "schema:description": "Plasma gas: 16 l min\u207b\u00b9; Auxiliary: 0.9 l min\u207b\u00b9; Nebulizer gas (from table): 1.1 l min\u207b\u00b9"
            },
            {
              "@id": "ada:parameter/laSficpmsUPbTAPP/rfPowerDefault",
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
          "@id": "ada:parameter/laSficpmsUPbTAPP/massResolutionSettingDefault",
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
          "@id": "ada:parameter/laSficpmsUPbTAPP/detectorConfiguration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laSficpmsUPbTAPP/detectorConfiguration"
            }
          ],
          "schema:name": "Detector Configuration",
          "schema:value": "Triple mode detector (pulse counting, analog, Faraday)"
        },
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/icpTuningDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "icpTuningDefault",
          "schema:name": "ICP Tuning",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "ICP and laser settings optimized daily for optimum signal intensity and low oxide formation (factory specifications; mass calibration and detector cross-calibration checked and redone if required)"
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
      "schema:name": "iolite 4.5.7 with 3D Trace Elements DRS"
    }
  ],
  "ada:ablationSamplingMode": [
    "Spot (stationary)"
  ],
  "ada:ablationSpotDurationDefault": "40 s on-sample ablation (after 20 s background measurement)",
  "ada:carrierGasFlowRateDefault": "He: 0.6 l min\u207b\u00b9 (MFC 1) + 0.7 l min\u207b\u00b9 (MFC 2) in HelEx II cell; combined with Ar makeup via T-piece near torch",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laSficpmsUPbTAPP/plasmaMakeUpGasAdditionDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "plasmaMakeUpGasAdditionDefault",
      "schema:name": "Plasma / Make-up Gas Addition",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Ar make-up gas (combined via T-piece in sample transport line near torch; flow rate not stated separately)"
    },
    {
      "@id": "ada:parameter/laSficpmsUPbTAPP/multiRunSequentialAnalysisDesign",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/multiRunSequentialAnalysisDesign"
        }
      ],
      "schema:name": "Multi-Run Sequential Analysis Design",
      "schema:value": "Single acquisition run (20 spot analyses per sample under repeatability conditions)"
    }
  ],
  "ada:analysisSequenceDefault": "NIST SRM 612(\u00d73) \u2192 North Chile(\u00d73) \u2192 unknowns(\u00d710) \u2192 NIST SRM 612(\u00d72) \u2192 North Chile(\u00d72) \u2192 unknowns(\u00d710) \u2192 \u2026 (bracketing every 15)",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "\u2075\u00b2Cr",
      "\u2075\u2077Fe",
      "\u2075\u2079Co",
      "\u2076\u00b9Ni",
      "\u2076\u2075Cu",
      "\u2076\u2079Ga",
      "\u2077\u00b2Ge",
      "\u2077\u2075As",
      "\u2079\u2079Ru",
      "\u00b9\u2070\u00b3Rh",
      "\u00b9\u2070\u2075Pd",
      "\u00b9\u2078\u00b2W",
      "\u00b9\u2078\u2075Re",
      "\u00b9\u2078\u2079Os",
      "\u00b9\u2079\u00b3Ir",
      "\u00b9\u2079\u2075Pt",
      "\u00b9\u2079\u2077Au (17 isotopes)",
      "low relative abundance isotopes chosen for Ni and Fe (analog mode)"
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
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/monitoredIsotopes",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredIsotopes",
        "schema:name": "Monitored Isotopes",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "boolean",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/normalizationStandardsBasedCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "normalizationStandardsBasedCorrection",
        "schema:name": "Normalization / Standards-Based Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "uri",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "uri"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/massResolutionPerAnalyte",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionPerAnalyte",
        "schema:name": "Mass Resolution per Analyte",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:backgroundCountTimeDefault": "20 s background measurement (laser shutter closed) before each 40 s ablation",
  "ada:internalStandardApproach": "Fe+Ni+Co sum normalization to 100% using iolite 3D Trace Elements DRS (eliminates need for independent EPMA IS)",
  "ada:internalStandardElement": "No single IS; Fe+Ni+Co mass fractions normalized to 100% via iolite 3D DRS (yield correction factors applied for NIST SRM 612 relative to North Chile)",
  "ada:elementalFractionationCorrection": [
    "External calibration using North Chile iron meteorite + NIST SRM 612 glass (yield correction applied in iolite 3D DRS for NIST relative to North Chile); ordinary least-squares fitting per 15 min calibration block; Fe+Ni+Co normalization eliminates need for independent EPMA IS"
  ],
  "ada:signalIntegrationIntervalMethod": "Time-resolved LA-ICP-MS signals inspected per analysis; background interval (20 s) and ablation interval (40 s) selected; no automated spike exclusion described",
  "ada:blankBackgroundCorrectionMethod": "Background signal measured for 20 s (laser shutter closed) before each 40 s ablation; background mean subtracted per isotope in iolite",
  "ada:primaryStandardNameDefault": "NIST SRM 612 glass (Jochum et al. 2011) + North Chile Filomena iron meteorite (Wasson et al. 1989) \u2014 used together with yield correction in iolite 3D DRS",
  "ada:calibrationMeasurementFrequency": "NIST SRM 612 and North Chile measured bracketing every 15 unknowns: 3\u00d7STD \u2192 3\u00d7STD \u2192 10\u00d7unknowns \u2192 repeat",
  "ada:secondaryReferenceMaterialDefault": [
    "North Chile Filomena measured as unknown on different days over 4 months to assess intermediate precision (Table 3 and Fig. 2)"
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ageModelDefault": "missing",
  "ada:inheritedOrInitialSignalCorrectionDefault": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:massResolutionAssignment": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
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

ex:laSficpmsUPbTAPP-Navarro2024 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault>,
                        <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/signalSmoothingDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Fragments ~1 cm mounted in epoxy resin, polished, cleaned with ultrapure water" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/guardElectrode> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/multiRunSequentialAnalysisDesign>,
        <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/plasmaMakeUpGasAdditionDefault> ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Navarro, Enzweiler, Crósta et al." ] ;
    schema1:datePublished "missing" ;
    schema1:description "Key innovations: (1) use of two measurement standards (NIST SRM 612 + North Chile) with yield correction in iolite 3D DRS; (2) Fe+Ni+Co=100% normalization eliminates need for EPMA IS; Cr results not quantitative due to argide interferences" ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "FAPESP (São Paulo Research Foundation); CNPq" ] ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/detectorConfiguration>,
                <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/icpTuningDefault>,
                <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/massResolutionSettingDefault> ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "ICPMS",
                "Sector field (SF-ICP-MS) (explicitly stated: \"sector field inductively coupled plasma mass spectrometer\")" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Torch" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/interfaceConeConfiguration> ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Interface Cone" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/coolantGasFlowRateDefault>,
                        <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/rfPowerDefault> ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "ICP Source" ;
                    schema1:name "missing" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "Thermo Fisher Scientific Element XR (SF-ICP-MS)" ] ;
            schema1:name "example instrumentName" ],
        [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/laserPulseDuration> ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "Laser Ablation System" ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "Teledyne Excite 193 (193 nm ArF excimer)" ] ;
            schema1:name "HelEx II two-volume sample cell" ;
            ada:laserFluenceDefault "7 J cm⁻²" ;
            ada:laserRepetitionRateDefault "10 Hz" ;
            ada:laserSpotGeometryDefault "150 µm circular" ;
            ada:laserType "193 nm ArF excimer; pulse duration 4 ns" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "Isotope Geology Laboratory, University of Campinas (UNICAMP), Brazil" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "LA-SF-ICP-MS" ;
            schema1:termCode "LA-ICP-MS" ] ;
    schema1:name "Navarro et al. (2024) Iron Meteorite Spot v1" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Iron meteorite metal (kamacite + taenite)" ],
                <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Navarro et al. (2024) ACS Earth Space Chem. 8, 281; Longerich et al. (1996)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:ablationPitDepthRateDefault "missing" ;
    ada:ablationSamplingMode "Spot (stationary)" ;
    ada:ablationSpotDurationDefault "40 s on-sample ablation (after 20 s background measurement)" ;
    ada:ageModelDefault "missing" ;
    ada:analysisSequenceDefault "NIST SRM 612(×3) → North Chile(×3) → unknowns(×10) → NIST SRM 612(×2) → North Chile(×2) → unknowns(×10) → … (bracketing every 15)" ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/detectionLimit>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/detectionLimitMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/isobaricInterferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/limitOfQuantificationMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/massResolutionPerAnalyte>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/monitoredIsotopes>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/normalizationStandardsBasedCorrection>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ;
            ada:defaultAnalytes "low relative abundance isotopes chosen for Ni and Fe (analog mode)",
                "¹⁰³Rh",
                "¹⁰⁵Pd",
                "¹⁸²W",
                "¹⁸⁵Re",
                "¹⁸⁹Os",
                "¹⁹³Ir",
                "¹⁹⁵Pt",
                "¹⁹⁷Au (17 isotopes)",
                "⁵²Cr",
                "⁵⁷Fe",
                "⁵⁹Co",
                "⁶¹Ni",
                "⁶⁵Cu",
                "⁶⁹Ga",
                "⁷²Ge",
                "⁷⁵As",
                "⁹⁹Ru" ] ;
    ada:backgroundCountTimeDefault "20 s background measurement (laser shutter closed) before each 40 s ablation" ;
    ada:blankBackgroundCorrectionMethod "Background signal measured for 20 s (laser shutter closed) before each 40 s ablation; background mean subtracted per isotope in iolite" ;
    ada:calibrationMeasurementFrequency "NIST SRM 612 and North Chile measured bracketing every 15 unknowns: 3×STD → 3×STD → 10×unknowns → repeat" ;
    ada:carrierGasFlowRateDefault "He: 0.6 l min⁻¹ (MFC 1) + 0.7 l min⁻¹ (MFC 2) in HelEx II cell; combined with Ar makeup via T-piece near torch" ;
    ada:elementalFractionationCorrection "External calibration using North Chile iron meteorite + NIST SRM 612 glass (yield correction applied in iolite 3D DRS for NIST relative to North Chile); ordinary least-squares fitting per 15 min calibration block; Fe+Ni+Co normalization eliminates need for independent EPMA IS" ;
    ada:inheritedOrInitialSignalCorrectionDefault "missing" ;
    ada:internalStandardApproach "Fe+Ni+Co sum normalization to 100% using iolite 3D Trace Elements DRS (eliminates need for independent EPMA IS)" ;
    ada:internalStandardElement "No single IS; Fe+Ni+Co mass fractions normalized to 100% via iolite 3D DRS (yield correction factors applied for NIST SRM 612 relative to North Chile)" ;
    ada:ionCounterDeadTimeDefault -9999 ;
    ada:massBiasCorrectionStrategy "missing" ;
    ada:massResolutionAssignment "missing" ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:primaryStandardNameDefault "NIST SRM 612 glass (Jochum et al. 2011) + North Chile Filomena iron meteorite (Wasson et al. 1989) — used together with yield correction in iolite 3D DRS" ;
    ada:rasterLineSpacingDefault "missing" ;
    ada:sampleIntroduction "missing" ;
    ada:samplingUnit "missing" ;
    ada:secondaryReferenceMaterialDefault "North Chile Filomena measured as unknown on different days over 4 months to assess intermediate precision (Table 3 and Fig. 2)" ;
    ada:signalIntegrationIntervalMethod "Time-resolved LA-ICP-MS signals inspected per analysis; background interval (20 s) and ablation interval (40 s) selected; no automated spike exclusion described" ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:totalIntegrationTimePerOutputDataPointDefault "missing" ;
    ada:uncertaintyLevel "missing" ;
    bios:computationalTool [ schema1:name "iolite 4.5.7 with 3D Trace Elements DRS" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/detectionLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimit" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/detectionLimitMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Detection Limit Method" ;
    schema1:valueName "detectionLimitMethod" ;
    ada:dataType "uri" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/isobaricInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Isobaric Interference Corrections Applied" ;
    schema1:valueName "isobaricInterferenceCorrectionsApplied" ;
    ada:dataType "boolean" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "uri" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/massResolutionPerAnalyte> a schema1:PropertyValueSpecification ;
    schema1:name "Mass Resolution per Analyte" ;
    schema1:valueName "massResolutionPerAnalyte" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/monitoredIsotopes> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Monitored Isotopes" ;
    schema1:valueName "monitoredIsotopes" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/normalizationStandardsBasedCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Normalization / Standards-Based Correction" ;
    schema1:valueName "normalizationStandardsBasedCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/coolantGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 16 ;
    schema1:description "Plasma gas: 16 l min⁻¹; Auxiliary: 0.9 l min⁻¹; Nebulizer gas (from table): 1.1 l min⁻¹" ;
    schema1:name "Coolant (Plasma) Gas Flow Rate" ;
    schema1:valueName "coolantGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/icpTuningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "ICP and laser settings optimized daily for optimum signal intensity and low oxide formation (factory specifications; mass calibration and detector cross-calibration checked and redone if required)" ;
    schema1:name "ICP Tuning" ;
    schema1:valueName "icpTuningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/massResolutionSettingDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Low resolution (M/ΔM = 300)" ;
    schema1:name "Mass Resolution Setting" ;
    schema1:valueName "massResolutionSettingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/plasmaMakeUpGasAdditionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Ar make-up gas (combined via T-piece in sample transport line near torch; flow rate not stated separately)" ;
    schema1:name "Plasma / Make-up Gas Addition" ;
    schema1:valueName "plasmaMakeUpGasAdditionDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Applied: triple mode detector (pulse counting, analog, Faraday); low relative abundance isotopes chosen for Ni and Fe to allow analog mode measurement of major matrix elements" ;
    schema1:name "Pulse/Analog Detector Nonlinearity Correction" ;
    schema1:valueName "pulseAnalogDetectorNonlinearityCorrectionDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/rfPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1200 ;
    schema1:description "1200 W" ;
    schema1:name "RF Power" ;
    schema1:valueName "rfPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "In situ — polished epoxy mount (~1 cm fragments in epoxy, etched with Nital)" ;
    schema1:name "Sample Form / Analytical Substrate" ;
    schema1:valueName "sampleFormAnalyticalSubstrateDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/signalSmoothingDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "None" ;
    schema1:name "Signal Smoothing" ;
    schema1:valueName "signalSmoothingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/detectorConfiguration> a schema1:PropertyValue ;
    schema1:name "Detector Configuration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/detectorConfiguration> ;
    schema1:value "Triple mode detector (pulse counting, analog, Faraday)" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/guardElectrode> a schema1:PropertyValue ;
    schema1:name "Guard Electrode" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/guardElectrode> ;
    schema1:value "On (active)" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/interfaceConeConfiguration> a schema1:PropertyValue ;
    schema1:name "Interface Cone Configuration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/interfaceConeConfiguration> ;
    schema1:value "Ni sampler cone; Ni skimmer cone" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/laserPulseDuration> a schema1:PropertyValue ;
    schema1:name "Laser Pulse Duration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/laserPulseDuration> ;
    schema1:value "4 ns (ArF excimer Excite 193)" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/multiRunSequentialAnalysisDesign> a schema1:PropertyValue ;
    schema1:name "Multi-Run Sequential Analysis Design" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/multiRunSequentialAnalysisDesign> ;
    schema1:value "Single acquisition run (20 spot analyses per sample under repeatability conditions)" .


```


### laSficpmsUPbTAPP example Navarro2024-2
laSficpmsUPbTAPP instance derived from Navarro et al. 2024 (ACS ESC 8) Iron meteorites Raster mapping (2D) ns-LA-SF-ICP-MS University of Campinas.
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
  "@id": "ex:laSficpmsUPbTAPP-Navarro2024-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Navarro et al. (2024) Iron Meteorite Raster Mapping v1",
  "schema:description": "Elemental mapping used as classification tool even without prior knowledge of structural variations (kamacite vs. plessite); demonstrates LA-ICP-MS mapping applicability for iron meteorite classification",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-ICP-MS",
      "schema:name": "LA-SF-ICP-MS"
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
      "schema:name": "FAPESP; CNPq"
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
            "Iron meteorite metal (kamacite + plessite)"
          ]
        },
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleFormAnalyticalSubstrateDefault",
          "schema:name": "Sample Form / Analytical Substrate",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "In situ — polished epoxy mount (same Augusto Pestana fragment as spot protocol)"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Same Augusto Pestana fragment etched with Nital solution (2% v/v HNO₃ in ethanol) to reveal kamacite and plessite",
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
            "@id": "ada:parameter/laSficpmsUPbTAPP/guardElectrode",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/laSficpmsUPbTAPP/guardElectrode"
              }
            ],
            "schema:name": "Guard Electrode",
            "schema:value": "On (active)"
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
            "@id": "ada:parameter/laSficpmsUPbTAPP/signalSmoothingDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "signalSmoothingDefault",
            "schema:name": "Signal Smoothing",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "None"
          },
          {
            "@id": "ada:parameter/laSficpmsUPbTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "pulseAnalogDetectorNonlinearityCorrectionDefault",
            "schema:name": "Pulse/Analog Detector Nonlinearity Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Applied (same as spot)"
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
        "schema:name": "Teledyne Excite 193 (193 nm ArF excimer)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "193 nm ArF excimer; pulse duration 4 ns",
      "schema:name": "HelEx II two-volume sample cell",
      "ada:laserSpotGeometryDefault": "150 µm square (mapping mode)",
      "ada:laserFluenceDefault": "7 J cm⁻²",
      "ada:laserRepetitionRateDefault": "10 Hz",
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/laserPulseDuration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laSficpmsUPbTAPP/laserPulseDuration"
            }
          ],
          "schema:name": "Laser Pulse Duration",
          "schema:value": "4 ns (ArF excimer Excite 193)"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ]
    },
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
              "@id": "ada:parameter/laSficpmsUPbTAPP/interfaceConeConfiguration",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/laSficpmsUPbTAPP/interfaceConeConfiguration"
                }
              ],
              "schema:name": "Interface Cone Configuration",
              "schema:value": "Ni sampler cone; Ni skimmer cone"
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
              "@id": "ada:parameter/laSficpmsUPbTAPP/coolantGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantGasFlowRateDefault",
              "schema:name": "Coolant (Plasma) Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 16,
              "schema:description": "Plasma gas: 16 l min⁻¹; Auxiliary: 0.9 l min⁻¹"
            },
            {
              "@id": "ada:parameter/laSficpmsUPbTAPP/rfPowerDefault",
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
          "@id": "ada:parameter/laSficpmsUPbTAPP/massResolutionSettingDefault",
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
          "@id": "ada:parameter/laSficpmsUPbTAPP/detectorConfiguration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laSficpmsUPbTAPP/detectorConfiguration"
            }
          ],
          "schema:name": "Detector Configuration",
          "schema:value": "Triple mode detector (pulse counting, analog, Faraday)"
        },
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/icpTuningDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "icpTuningDefault",
          "schema:name": "ICP Tuning",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Same as spot protocol"
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
      "schema:name": "iolite 4.5.7 with 3D Trace Elements DRS"
    }
  ],
  "ada:ablationSamplingMode": [
    "Raster area (2D elemental mapping)"
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSizeDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "transectRateMappingRateOrStepSizeDefault",
      "schema:name": "Transect Rate, Mapping Rate or Step Size",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "10 µm s⁻¹ (continuous raster scan)"
    },
    {
      "@id": "ada:parameter/laSficpmsUPbTAPP/plasmaMakeUpGasAdditionDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "plasmaMakeUpGasAdditionDefault",
      "schema:name": "Plasma / Make-up Gas Addition",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Ar make-up gas (same as spot protocol)"
    }
  ],
  "ada:carrierGasFlowRateDefault": "He: 0.6 l min⁻¹ (MFC 1) + 0.7 l min⁻¹ (MFC 2) in HelEx II cell",
  "ada:analysisSequenceDefault": "Background (1 min) → NIST SRM 612(×3) → North Chile(×3) → unknown map (30 min) → North Chile(×3) → NIST SRM 612(×3) → background",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "⁵²Cr",
      "⁵⁷Fe",
      "⁵⁹Co",
      "⁶¹Ni",
      "⁶⁵Cu",
      "⁶⁹Ga",
      "⁷²Ge",
      "⁷⁵As",
      "⁹⁹Ru",
      "¹⁰³Rh",
      "¹⁰⁵Pd",
      "¹⁸²W",
      "¹⁸⁵Re",
      "¹⁸⁹Os",
      "¹⁹³Ir",
      "¹⁹⁵Pt",
      "¹⁹⁷Au (same 17 isotopes as spot protocol)"
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
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/monitoredIsotopes",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredIsotopes",
        "schema:name": "Monitored Isotopes",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "boolean",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/normalizationStandardsBasedCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "normalizationStandardsBasedCorrection",
        "schema:name": "Normalization / Standards-Based Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "uri",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "uri"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/massResolutionPerAnalyte",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionPerAnalyte",
        "schema:name": "Mass Resolution per Analyte",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:backgroundCountTimeDefault": "60 s background measurement before mapping session start; 3 measurements each for NIST and North Chile after background",
  "ada:internalStandardApproach": "Fe+Ni+Co sum normalization to 100% (same DRS as spot protocol; mandatory for multi-phase mapping without prior IS knowledge)",
  "ada:internalStandardElement": "No single IS; Fe+Ni+Co=100% normalization (same as spot protocol)",
  "ada:elementalFractionationCorrection": [
    "Same calibration approach as spot protocol (iolite 3D DRS; same yield correction)"
  ],
  "ada:signalIntegrationIntervalMethod": "Same procedure as spot protocol; signal integration for mapping not separately described",
  "ada:blankBackgroundCorrectionMethod": "Background (1 min) measured at session start; additional 3 measurements of NIST and North Chile used for calibration (background included in regression line for gas blank)",
  "ada:primaryStandardNameDefault": "NIST SRM 612 (Jochum et al. 2011) + North Chile Filomena — same as spot protocol",
  "ada:calibrationMeasurementFrequency": "NIST SRM 612 and North Chile at start and end of mapping session (30 min map; 3 measurements each before and after)",
  "ada:secondaryReferenceMaterialDefault": [
    "North Chile and NIST SRM 612 measured before and after mapping session as QC materials"
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ablationSpotDurationDefault": -9999,
  "ada:ageModelDefault": "missing",
  "ada:inheritedOrInitialSignalCorrectionDefault": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:massResolutionAssignment": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS-UPb/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:laSficpmsUPbTAPP-Navarro2024-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "Navarro et al. (2024) Iron Meteorite Raster Mapping v1",
  "schema:description": "Elemental mapping used as classification tool even without prior knowledge of structural variations (kamacite vs. plessite); demonstrates LA-ICP-MS mapping applicability for iron meteorite classification",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "LA-ICP-MS",
      "schema:name": "LA-SF-ICP-MS"
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
      "schema:name": "FAPESP; CNPq"
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
            "Iron meteorite metal (kamacite + plessite)"
          ]
        },
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "sampleFormAnalyticalSubstrateDefault",
          "schema:name": "Sample Form / Analytical Substrate",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "In situ \u2014 polished epoxy mount (same Augusto Pestana fragment as spot protocol)"
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Same Augusto Pestana fragment etched with Nital solution (2% v/v HNO\u2083 in ethanol) to reveal kamacite and plessite",
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
            "@id": "ada:parameter/laSficpmsUPbTAPP/guardElectrode",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/laSficpmsUPbTAPP/guardElectrode"
              }
            ],
            "schema:name": "Guard Electrode",
            "schema:value": "On (active)"
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
            "@id": "ada:parameter/laSficpmsUPbTAPP/signalSmoothingDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "signalSmoothingDefault",
            "schema:name": "Signal Smoothing",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "None"
          },
          {
            "@id": "ada:parameter/laSficpmsUPbTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "pulseAnalogDetectorNonlinearityCorrectionDefault",
            "schema:name": "Pulse/Analog Detector Nonlinearity Correction",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Applied (same as spot)"
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
        "schema:name": "Teledyne Excite 193 (193 nm ArF excimer)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:laserType": "193 nm ArF excimer; pulse duration 4 ns",
      "schema:name": "HelEx II two-volume sample cell",
      "ada:laserSpotGeometryDefault": "150 \u00b5m square (mapping mode)",
      "ada:laserFluenceDefault": "7 J cm\u207b\u00b2",
      "ada:laserRepetitionRateDefault": "10 Hz",
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/laserPulseDuration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laSficpmsUPbTAPP/laserPulseDuration"
            }
          ],
          "schema:name": "Laser Pulse Duration",
          "schema:value": "4 ns (ArF excimer Excite 193)"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ]
    },
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
              "@id": "ada:parameter/laSficpmsUPbTAPP/interfaceConeConfiguration",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/laSficpmsUPbTAPP/interfaceConeConfiguration"
                }
              ],
              "schema:name": "Interface Cone Configuration",
              "schema:value": "Ni sampler cone; Ni skimmer cone"
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
              "@id": "ada:parameter/laSficpmsUPbTAPP/coolantGasFlowRateDefault",
              "@type": [
                "schema:PropertyValueSpecification"
              ],
              "schema:valueName": "coolantGasFlowRateDefault",
              "schema:name": "Coolant (Plasma) Gas Flow Rate",
              "ada:dataType": "number",
              "ada:fieldScope": "session",
              "schema:defaultValue": 16,
              "schema:description": "Plasma gas: 16 l min\u207b\u00b9; Auxiliary: 0.9 l min\u207b\u00b9"
            },
            {
              "@id": "ada:parameter/laSficpmsUPbTAPP/rfPowerDefault",
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
          "@id": "ada:parameter/laSficpmsUPbTAPP/massResolutionSettingDefault",
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
          "@id": "ada:parameter/laSficpmsUPbTAPP/detectorConfiguration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/laSficpmsUPbTAPP/detectorConfiguration"
            }
          ],
          "schema:name": "Detector Configuration",
          "schema:value": "Triple mode detector (pulse counting, analog, Faraday)"
        },
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/icpTuningDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "icpTuningDefault",
          "schema:name": "ICP Tuning",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "Same as spot protocol"
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
      "schema:name": "iolite 4.5.7 with 3D Trace Elements DRS"
    }
  ],
  "ada:ablationSamplingMode": [
    "Raster area (2D elemental mapping)"
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSizeDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "transectRateMappingRateOrStepSizeDefault",
      "schema:name": "Transect Rate, Mapping Rate or Step Size",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "10 \u00b5m s\u207b\u00b9 (continuous raster scan)"
    },
    {
      "@id": "ada:parameter/laSficpmsUPbTAPP/plasmaMakeUpGasAdditionDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "plasmaMakeUpGasAdditionDefault",
      "schema:name": "Plasma / Make-up Gas Addition",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "Ar make-up gas (same as spot protocol)"
    }
  ],
  "ada:carrierGasFlowRateDefault": "He: 0.6 l min\u207b\u00b9 (MFC 1) + 0.7 l min\u207b\u00b9 (MFC 2) in HelEx II cell",
  "ada:analysisSequenceDefault": "Background (1 min) \u2192 NIST SRM 612(\u00d73) \u2192 North Chile(\u00d73) \u2192 unknown map (30 min) \u2192 North Chile(\u00d73) \u2192 NIST SRM 612(\u00d73) \u2192 background",
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "\u2075\u00b2Cr",
      "\u2075\u2077Fe",
      "\u2075\u2079Co",
      "\u2076\u00b9Ni",
      "\u2076\u2075Cu",
      "\u2076\u2079Ga",
      "\u2077\u00b2Ge",
      "\u2077\u2075As",
      "\u2079\u2079Ru",
      "\u00b9\u2070\u00b3Rh",
      "\u00b9\u2070\u2075Pd",
      "\u00b9\u2078\u00b2W",
      "\u00b9\u2078\u2075Re",
      "\u00b9\u2078\u2079Os",
      "\u00b9\u2079\u00b3Ir",
      "\u00b9\u2079\u2075Pt",
      "\u00b9\u2079\u2077Au (same 17 isotopes as spot protocol)"
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
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/monitoredIsotopes",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "monitoredIsotopes",
        "schema:name": "Monitored Isotopes",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/dwellTimePerMass",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "dwellTimePerMass",
        "schema:name": "Dwell Time per Mass",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/isobaricInterferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "isobaricInterferenceCorrectionsApplied",
        "schema:name": "Isobaric Interference Corrections Applied",
        "ada:dataType": "boolean",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/interferingSpecies",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingSpecies",
        "schema:name": "Interfering Species",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/interferenceCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionMethod",
        "schema:name": "Interference Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/normalizationStandardsBasedCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "normalizationStandardsBasedCorrection",
        "schema:name": "Normalization / Standards-Based Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/detectionLimit",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimit",
        "schema:name": "Detection Limit",
        "ada:dataType": "number"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/detectionLimitMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "detectionLimitMethod",
        "schema:name": "Detection Limit Method",
        "ada:dataType": "uri",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/limitOfQuantificationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "limitOfQuantificationMethod",
        "schema:name": "Limit of Quantification (LOQ) Method",
        "ada:dataType": "uri"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "withinSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Within-Session Analytical Precision and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "betweenSessionAnalyticalPrecisionAndAssessmentMethod",
        "schema:name": "Between-Session (Long-Term) Analytical Precision and Assessment Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracyAndAssessmentMethod",
        "schema:name": "Analytical Accuracy and Assessment Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/laSficpmsUPbTAPP/massResolutionPerAnalyte",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "massResolutionPerAnalyte",
        "schema:name": "Mass Resolution per Analyte",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:backgroundCountTimeDefault": "60 s background measurement before mapping session start; 3 measurements each for NIST and North Chile after background",
  "ada:internalStandardApproach": "Fe+Ni+Co sum normalization to 100% (same DRS as spot protocol; mandatory for multi-phase mapping without prior IS knowledge)",
  "ada:internalStandardElement": "No single IS; Fe+Ni+Co=100% normalization (same as spot protocol)",
  "ada:elementalFractionationCorrection": [
    "Same calibration approach as spot protocol (iolite 3D DRS; same yield correction)"
  ],
  "ada:signalIntegrationIntervalMethod": "Same procedure as spot protocol; signal integration for mapping not separately described",
  "ada:blankBackgroundCorrectionMethod": "Background (1 min) measured at session start; additional 3 measurements of NIST and North Chile used for calibration (background included in regression line for gas blank)",
  "ada:primaryStandardNameDefault": "NIST SRM 612 (Jochum et al. 2011) + North Chile Filomena \u2014 same as spot protocol",
  "ada:calibrationMeasurementFrequency": "NIST SRM 612 and North Chile at start and end of mapping session (30 min map; 3 measurements each before and after)",
  "ada:secondaryReferenceMaterialDefault": [
    "North Chile and NIST SRM 612 measured before and after mapping session as QC materials"
  ],
  "ada:ablationPitDepthRateDefault": "missing",
  "ada:ablationSpotDurationDefault": -9999,
  "ada:ageModelDefault": "missing",
  "ada:inheritedOrInitialSignalCorrectionDefault": "missing",
  "ada:ionCounterDeadTimeDefault": -9999,
  "ada:massBiasCorrectionStrategy": "missing",
  "ada:massResolutionAssignment": "missing",
  "ada:oxideProductionMethodAndThreshold": "missing",
  "ada:rasterLineSpacingDefault": "missing",
  "ada:sampleIntroduction": "missing",
  "ada:samplingUnit": "missing",
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

ex:laSficpmsUPbTAPP-Navarro2024-2 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Same Augusto Pestana fragment etched with Nital solution (2% v/v HNO₃ in ethanol) to reveal kamacite and plessite" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/guardElectrode> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data acquisition" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault>,
                        <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/signalSmoothingDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 3 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/plasmaMakeUpGasAdditionDefault>,
        <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSizeDefault> ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Navarro, Enzweiler, Crósta et al." ] ;
    schema1:datePublished "missing" ;
    schema1:description "Elemental mapping used as classification tool even without prior knowledge of structural variations (kamacite vs. plessite); demonstrates LA-ICP-MS mapping applicability for iron meteorite classification" ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "FAPESP; CNPq" ] ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/laserPulseDuration> ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "Laser Ablation System" ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "Teledyne Excite 193 (193 nm ArF excimer)" ] ;
            schema1:name "HelEx II two-volume sample cell" ;
            ada:laserFluenceDefault "7 J cm⁻²" ;
            ada:laserRepetitionRateDefault "10 Hz" ;
            ada:laserSpotGeometryDefault "150 µm square (mapping mode)" ;
            ada:laserType "193 nm ArF excimer; pulse duration 4 ns" ],
        [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/detectorConfiguration>,
                <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/icpTuningDefault>,
                <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/massResolutionSettingDefault> ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "ICPMS",
                "Sector field (SF-ICP-MS) (explicitly stated)" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/coolantGasFlowRateDefault>,
                        <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/rfPowerDefault> ;
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
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/interfaceConeConfiguration> ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Interface Cone" ;
                    schema1:name "missing" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "Thermo Fisher Scientific Element XR (SF-ICP-MS)" ] ;
            schema1:name "example instrumentName" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "Isotope Geology Laboratory, University of Campinas (UNICAMP), Brazil" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "LA-SF-ICP-MS" ;
            schema1:termCode "LA-ICP-MS" ] ;
    schema1:name "Navarro et al. (2024) Iron Meteorite Raster Mapping v1" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Iron meteorite metal (kamacite + plessite)" ],
                <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Navarro et al. (2024) ACS Earth Space Chem. 8, 281; Longerich et al. (1996)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:ablationPitDepthRateDefault "missing" ;
    ada:ablationSamplingMode "Raster area (2D elemental mapping)" ;
    ada:ablationSpotDurationDefault -9999 ;
    ada:ageModelDefault "missing" ;
    ada:analysisSequenceDefault "Background (1 min) → NIST SRM 612(×3) → North Chile(×3) → unknown map (30 min) → North Chile(×3) → NIST SRM 612(×3) → background" ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/detectionLimit>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/detectionLimitMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/dwellTimePerMass>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/interferenceCorrectionMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/interferingSpecies>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/isobaricInterferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/limitOfQuantificationMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/massResolutionPerAnalyte>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/monitoredIsotopes>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/normalizationStandardsBasedCorrection>,
                <https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> ;
            ada:defaultAnalytes "¹⁰³Rh",
                "¹⁰⁵Pd",
                "¹⁸²W",
                "¹⁸⁵Re",
                "¹⁸⁹Os",
                "¹⁹³Ir",
                "¹⁹⁵Pt",
                "¹⁹⁷Au (same 17 isotopes as spot protocol)",
                "⁵²Cr",
                "⁵⁷Fe",
                "⁵⁹Co",
                "⁶¹Ni",
                "⁶⁵Cu",
                "⁶⁹Ga",
                "⁷²Ge",
                "⁷⁵As",
                "⁹⁹Ru" ] ;
    ada:backgroundCountTimeDefault "60 s background measurement before mapping session start; 3 measurements each for NIST and North Chile after background" ;
    ada:blankBackgroundCorrectionMethod "Background (1 min) measured at session start; additional 3 measurements of NIST and North Chile used for calibration (background included in regression line for gas blank)" ;
    ada:calibrationMeasurementFrequency "NIST SRM 612 and North Chile at start and end of mapping session (30 min map; 3 measurements each before and after)" ;
    ada:carrierGasFlowRateDefault "He: 0.6 l min⁻¹ (MFC 1) + 0.7 l min⁻¹ (MFC 2) in HelEx II cell" ;
    ada:elementalFractionationCorrection "Same calibration approach as spot protocol (iolite 3D DRS; same yield correction)" ;
    ada:inheritedOrInitialSignalCorrectionDefault "missing" ;
    ada:internalStandardApproach "Fe+Ni+Co sum normalization to 100% (same DRS as spot protocol; mandatory for multi-phase mapping without prior IS knowledge)" ;
    ada:internalStandardElement "No single IS; Fe+Ni+Co=100% normalization (same as spot protocol)" ;
    ada:ionCounterDeadTimeDefault -9999 ;
    ada:massBiasCorrectionStrategy "missing" ;
    ada:massResolutionAssignment "missing" ;
    ada:oxideProductionMethodAndThreshold "missing" ;
    ada:primaryStandardNameDefault "NIST SRM 612 (Jochum et al. 2011) + North Chile Filomena — same as spot protocol" ;
    ada:rasterLineSpacingDefault "missing" ;
    ada:sampleIntroduction "missing" ;
    ada:samplingUnit "missing" ;
    ada:secondaryReferenceMaterialDefault "North Chile and NIST SRM 612 measured before and after mapping session as QC materials" ;
    ada:signalIntegrationIntervalMethod "Same procedure as spot protocol; signal integration for mapping not separately described" ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:totalIntegrationTimePerOutputDataPointDefault "missing" ;
    ada:uncertaintyLevel "missing" ;
    bios:computationalTool [ schema1:name "iolite 4.5.7 with 3D Trace Elements DRS" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Analytical Accuracy and Assessment Method" ;
    schema1:valueName "analyticalAccuracyAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Between-Session (Long-Term) Analytical Precision and Assessment Method" ;
    schema1:valueName "betweenSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/detectionLimit> a schema1:PropertyValueSpecification ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimit" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/detectionLimitMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Detection Limit Method" ;
    schema1:valueName "detectionLimitMethod" ;
    ada:dataType "uri" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/dwellTimePerMass> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Dwell Time per Mass" ;
    schema1:valueName "dwellTimePerMass" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/interferenceCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Correction Method" ;
    schema1:valueName "interferenceCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/interferingSpecies> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interfering Species" ;
    schema1:valueName "interferingSpecies" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/isobaricInterferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Isobaric Interference Corrections Applied" ;
    schema1:valueName "isobaricInterferenceCorrectionsApplied" ;
    ada:dataType "boolean" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/limitOfQuantificationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Limit of Quantification (LOQ) Method" ;
    schema1:valueName "limitOfQuantificationMethod" ;
    ada:dataType "uri" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/massResolutionPerAnalyte> a schema1:PropertyValueSpecification ;
    schema1:name "Mass Resolution per Analyte" ;
    schema1:valueName "massResolutionPerAnalyte" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/monitoredIsotopes> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Monitored Isotopes" ;
    schema1:valueName "monitoredIsotopes" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/normalizationStandardsBasedCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Normalization / Standards-Based Correction" ;
    schema1:valueName "normalizationStandardsBasedCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/laSficpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Within-Session Analytical Precision and Assessment Method" ;
    schema1:valueName "withinSessionAnalyticalPrecisionAndAssessmentMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/coolantGasFlowRateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 16 ;
    schema1:description "Plasma gas: 16 l min⁻¹; Auxiliary: 0.9 l min⁻¹" ;
    schema1:name "Coolant (Plasma) Gas Flow Rate" ;
    schema1:valueName "coolantGasFlowRateDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/icpTuningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Same as spot protocol" ;
    schema1:name "ICP Tuning" ;
    schema1:valueName "icpTuningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/massResolutionSettingDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Low resolution (M/ΔM = 300)" ;
    schema1:name "Mass Resolution Setting" ;
    schema1:valueName "massResolutionSettingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/plasmaMakeUpGasAdditionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Ar make-up gas (same as spot protocol)" ;
    schema1:name "Plasma / Make-up Gas Addition" ;
    schema1:valueName "plasmaMakeUpGasAdditionDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Applied (same as spot)" ;
    schema1:name "Pulse/Analog Detector Nonlinearity Correction" ;
    schema1:valueName "pulseAnalogDetectorNonlinearityCorrectionDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/rfPowerDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1200 ;
    schema1:description "1200 W" ;
    schema1:name "RF Power" ;
    schema1:valueName "rfPowerDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "In situ — polished epoxy mount (same Augusto Pestana fragment as spot protocol)" ;
    schema1:name "Sample Form / Analytical Substrate" ;
    schema1:valueName "sampleFormAnalyticalSubstrateDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/signalSmoothingDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "None" ;
    schema1:name "Signal Smoothing" ;
    schema1:valueName "signalSmoothingDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSizeDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "10 µm s⁻¹ (continuous raster scan)" ;
    schema1:name "Transect Rate, Mapping Rate or Step Size" ;
    schema1:valueName "transectRateMappingRateOrStepSizeDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/detectorConfiguration> a schema1:PropertyValue ;
    schema1:name "Detector Configuration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/detectorConfiguration> ;
    schema1:value "Triple mode detector (pulse counting, analog, Faraday)" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/guardElectrode> a schema1:PropertyValue ;
    schema1:name "Guard Electrode" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/guardElectrode> ;
    schema1:value "On (active)" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/interfaceConeConfiguration> a schema1:PropertyValue ;
    schema1:name "Interface Cone Configuration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/interfaceConeConfiguration> ;
    schema1:value "Ni sampler cone; Ni skimmer cone" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/laserPulseDuration> a schema1:PropertyValue ;
    schema1:name "Laser Pulse Duration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/laserPulseDuration> ;
    schema1:value "4 ns (ArF excimer Excite 193)" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: LA-SF-ICP-MS U-Pb Geochronology TAPP (laSficpmsUPbTAPP)
description: Laser-ablation sector-field ICP-MS U-Pb geochronology extension of the
  base TAPP definition, generated from TAPPS20260813/Current TAPPs/LA-SF-ICP-MS_UPb_TAPP_v17.csv
  via the path-driven pipeline.
allOf:
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml
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
                        const: ada:parameter/laSficpmsUPbTAPP/sampleFormAnalyticalSubstrateDefault
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
                            const: ada:parameter/laSficpmsUPbTAPP/fusionFluxAndDilutionRatioDefault
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
                            const: ada:parameter/laSficpmsUPbTAPP/preAblationSurfaceTreatmentDefault
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
                            const: ada:parameter/laSficpmsUPbTAPP/fusionFluxAndDilutionRatioDefault
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
                            const: ada:parameter/laSficpmsUPbTAPP/preAblationSurfaceTreatmentDefault
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
                          const: ada:parameter/laSficpmsUPbTAPP/guardElectrode
                        '@type':
                          const:
                          - schema:PropertyValue
                        schema:propertyID:
                          const:
                          - '@id': ada:parameter/laSficpmsUPbTAPP/guardElectrode
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
                            const: ada:parameter/laSficpmsUPbTAPP/guardElectrode
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/laSficpmsUPbTAPP/guardElectrode
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
                            const: ada:parameter/laSficpmsUPbTAPP/signalSmoothingDefault
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
                            const: ada:parameter/laSficpmsUPbTAPP/spikeOutlierFilteringApproachDefault
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
                            const: ada:parameter/laSficpmsUPbTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault
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
                            const: ada:parameter/laSficpmsUPbTAPP/isotopeDilutionDataReductionMethod
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/laSficpmsUPbTAPP/isotopeDilutionDataReductionMethod
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
                            const: ada:parameter/laSficpmsUPbTAPP/calibrationFactorAndDeterminationMethodDefault
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
                            const: ada:parameter/laSficpmsUPbTAPP/analysisInclusionAndRejectionCriteria
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/laSficpmsUPbTAPP/analysisInclusionAndRejectionCriteria
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
                            const: ada:parameter/laSficpmsUPbTAPP/intermediateDaughterDisequilibriumCorrection
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/laSficpmsUPbTAPP/intermediateDaughterDisequilibriumCorrection
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
                            const: ada:parameter/laSficpmsUPbTAPP/constantsAndReferenceValuesUsedDefault
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
                            const: ada:parameter/laSficpmsUPbTAPP/faradayCupGainCalibrationMethod
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/laSficpmsUPbTAPP/faradayCupGainCalibrationMethod
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
                            const: ada:parameter/laSficpmsUPbTAPP/doubleSpikeInversionAlgorithm
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/laSficpmsUPbTAPP/doubleSpikeInversionAlgorithm
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
                            const: ada:parameter/laSficpmsUPbTAPP/normalizationStandardsBasedCorrection
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
                            const: ada:parameter/laSficpmsUPbTAPP/signalSmoothingDefault
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
                            const: ada:parameter/laSficpmsUPbTAPP/spikeOutlierFilteringApproachDefault
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
                            const: ada:parameter/laSficpmsUPbTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault
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
                            const: ada:parameter/laSficpmsUPbTAPP/isotopeDilutionDataReductionMethod
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/laSficpmsUPbTAPP/isotopeDilutionDataReductionMethod
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
                            const: ada:parameter/laSficpmsUPbTAPP/calibrationFactorAndDeterminationMethodDefault
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
                            const: ada:parameter/laSficpmsUPbTAPP/analysisInclusionAndRejectionCriteria
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/laSficpmsUPbTAPP/analysisInclusionAndRejectionCriteria
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
                            const: ada:parameter/laSficpmsUPbTAPP/intermediateDaughterDisequilibriumCorrection
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/laSficpmsUPbTAPP/intermediateDaughterDisequilibriumCorrection
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
                            const: ada:parameter/laSficpmsUPbTAPP/constantsAndReferenceValuesUsedDefault
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
                            const: ada:parameter/laSficpmsUPbTAPP/faradayCupGainCalibrationMethod
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/laSficpmsUPbTAPP/faradayCupGainCalibrationMethod
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
                            const: ada:parameter/laSficpmsUPbTAPP/doubleSpikeInversionAlgorithm
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/laSficpmsUPbTAPP/doubleSpikeInversionAlgorithm
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
                            const: ada:parameter/laSficpmsUPbTAPP/normalizationStandardsBasedCorrection
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
              const: ada:parameter/laSficpmsUPbTAPP/preAnalysisImagingAndScreeningDefault
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
              const: ada:parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSizeDefault
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
              const: ada:parameter/laSficpmsUPbTAPP/plasmaMakeUpGasAdditionDefault
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
              const: ada:parameter/laSficpmsUPbTAPP/instrumentWarmUpSessionDurationLimit
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laSficpmsUPbTAPP/instrumentWarmUpSessionDurationLimit
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
        - title: E-scan Range
          description: Electric scan range used for peak acquisition, expressed as
            percentage of the centre mass (%). Varies the accelerating voltage to
            cover masses in the vicinity of the set magnetic mass without re-scanning
            the magnet. Record 'N/A' if E-scan acquisition mode is not used.
          type: object
          properties:
            '@id':
              const: ada:parameter/laSficpmsUPbTAPP/eScanRange
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laSficpmsUPbTAPP/eScanRange
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
            the results averaged (Y/N). Used to reduce noise from short-term magnetic
            field instabilities on sector-field instruments. Triple scanning affects
            the effective integration time per cycle and should be reported. Record
            'N/A' if not applicable to the instrument.
          type: object
          properties:
            '@id':
              const: ada:parameter/laSficpmsUPbTAPP/tripleScanningMode
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laSficpmsUPbTAPP/tripleScanningMode
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
              const: ada:parameter/laSficpmsUPbTAPP/multiRunSequentialAnalysisDesign
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laSficpmsUPbTAPP/multiRunSequentialAnalysisDesign
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
              const: ada:parameter/laSficpmsUPbTAPP/uncertaintyPropagationMethodDefault
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
              const: ada:parameter/laSficpmsUPbTAPP/matrixOffsetCorrection
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laSficpmsUPbTAPP/matrixOffsetCorrection
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
              const: ada:parameter/laSficpmsUPbTAPP/ageDatumReferenceEpochDefault
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
              const: ada:parameter/laSficpmsUPbTAPP/discordanceDefinitionAndValues
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laSficpmsUPbTAPP/discordanceDefinitionAndValues
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
              const: ada:parameter/laSficpmsUPbTAPP/errorCorrelationBetweenReportedQuantitiesDefault
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
        - title: Imaging
          description: ''
          type: object
          properties:
            '@id':
              const: ada:parameter/laSficpmsUPbTAPP/imaging
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
              const: ada:parameter/laSficpmsUPbTAPP/ablationPitDepthAblationRate
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
              const: ada:parameter/laSficpmsUPbTAPP/makeUpGasFlow
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
              const: ada:parameter/laSficpmsUPbTAPP/numberOfBlocksPerMeasurement
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
              const: ada:parameter/laSficpmsUPbTAPP/numberOfCyclesPerBlock
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
              const: ada:parameter/laSficpmsUPbTAPP/integrationTimePerCycle
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
              const: ada:parameter/laSficpmsUPbTAPP/icDeadTime
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
              const: ada:parameter/laSficpmsUPbTAPP/baselineMeasurementApproach
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laSficpmsUPbTAPP/baselineMeasurementApproach
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
              const: ada:parameter/laSficpmsUPbTAPP/otherInformation
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
              const: ada:parameter/laSficpmsUPbTAPP/massFractionationLaw
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laSficpmsUPbTAPP/massFractionationLaw
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
              const: ada:parameter/laSficpmsUPbTAPP/uncertaintyLevelAndPropagation
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
              const: ada:parameter/laSficpmsUPbTAPP/doubleSpikeIsotopePair
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laSficpmsUPbTAPP/doubleSpikeIsotopePair
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
              const: ada:parameter/laSficpmsUPbTAPP/doubleSpikeMixingRatio
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
              const: ada:parameter/laSficpmsUPbTAPP/preAnalysisImagingAndScreeningDefault
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
              const: ada:parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSizeDefault
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
              const: ada:parameter/laSficpmsUPbTAPP/plasmaMakeUpGasAdditionDefault
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
              const: ada:parameter/laSficpmsUPbTAPP/instrumentWarmUpSessionDurationLimit
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laSficpmsUPbTAPP/instrumentWarmUpSessionDurationLimit
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
          title: E-scan Range
          description: Electric scan range used for peak acquisition, expressed as
            percentage of the centre mass (%). Varies the accelerating voltage to
            cover masses in the vicinity of the set magnetic mass without re-scanning
            the magnet. Record 'N/A' if E-scan acquisition mode is not used.
          type: object
          properties:
            '@id':
              const: ada:parameter/laSficpmsUPbTAPP/eScanRange
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laSficpmsUPbTAPP/eScanRange
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
            the results averaged (Y/N). Used to reduce noise from short-term magnetic
            field instabilities on sector-field instruments. Triple scanning affects
            the effective integration time per cycle and should be reported. Record
            'N/A' if not applicable to the instrument.
          type: object
          properties:
            '@id':
              const: ada:parameter/laSficpmsUPbTAPP/tripleScanningMode
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laSficpmsUPbTAPP/tripleScanningMode
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
              const: ada:parameter/laSficpmsUPbTAPP/multiRunSequentialAnalysisDesign
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laSficpmsUPbTAPP/multiRunSequentialAnalysisDesign
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
              const: ada:parameter/laSficpmsUPbTAPP/uncertaintyPropagationMethodDefault
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
              const: ada:parameter/laSficpmsUPbTAPP/matrixOffsetCorrection
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laSficpmsUPbTAPP/matrixOffsetCorrection
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
              const: ada:parameter/laSficpmsUPbTAPP/ageDatumReferenceEpochDefault
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
              const: ada:parameter/laSficpmsUPbTAPP/discordanceDefinitionAndValues
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laSficpmsUPbTAPP/discordanceDefinitionAndValues
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
              const: ada:parameter/laSficpmsUPbTAPP/errorCorrelationBetweenReportedQuantitiesDefault
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
          title: Imaging
          description: ''
          type: object
          properties:
            '@id':
              const: ada:parameter/laSficpmsUPbTAPP/imaging
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
              const: ada:parameter/laSficpmsUPbTAPP/ablationPitDepthAblationRate
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
              const: ada:parameter/laSficpmsUPbTAPP/makeUpGasFlow
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
              const: ada:parameter/laSficpmsUPbTAPP/numberOfBlocksPerMeasurement
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
              const: ada:parameter/laSficpmsUPbTAPP/numberOfCyclesPerBlock
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
              const: ada:parameter/laSficpmsUPbTAPP/integrationTimePerCycle
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
              const: ada:parameter/laSficpmsUPbTAPP/icDeadTime
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
              const: ada:parameter/laSficpmsUPbTAPP/baselineMeasurementApproach
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laSficpmsUPbTAPP/baselineMeasurementApproach
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
              const: ada:parameter/laSficpmsUPbTAPP/otherInformation
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
              const: ada:parameter/laSficpmsUPbTAPP/massFractionationLaw
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laSficpmsUPbTAPP/massFractionationLaw
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
              const: ada:parameter/laSficpmsUPbTAPP/uncertaintyLevelAndPropagation
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
              const: ada:parameter/laSficpmsUPbTAPP/doubleSpikeIsotopePair
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/laSficpmsUPbTAPP/doubleSpikeIsotopePair
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
              const: ada:parameter/laSficpmsUPbTAPP/doubleSpikeMixingRatio
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
                        const: ada:parameter/laSficpmsUPbTAPP/laserEnergyDefault
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
                        const: ada:parameter/laSficpmsUPbTAPP/laserBeamEnergyProfile
                      '@type':
                        const:
                        - schema:PropertyValue
                      schema:propertyID:
                        const:
                        - '@id': ada:parameter/laSficpmsUPbTAPP/laserBeamEnergyProfile
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
                        const: ada:parameter/laSficpmsUPbTAPP/laserPulseDuration
                      '@type':
                        const:
                        - schema:PropertyValue
                      schema:propertyID:
                        const:
                        - '@id': ada:parameter/laSficpmsUPbTAPP/laserPulseDuration
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
                        const: ada:parameter/laSficpmsUPbTAPP/laserEnergyDefault
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
                        const: ada:parameter/laSficpmsUPbTAPP/laserBeamEnergyProfile
                      '@type':
                        const:
                        - schema:PropertyValue
                      schema:propertyID:
                        const:
                        - '@id': ada:parameter/laSficpmsUPbTAPP/laserBeamEnergyProfile
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
                        const: ada:parameter/laSficpmsUPbTAPP/laserPulseDuration
                      '@type':
                        const:
                        - schema:PropertyValue
                      schema:propertyID:
                        const:
                        - '@id': ada:parameter/laSficpmsUPbTAPP/laserPulseDuration
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
                        const: ada:parameter/laSficpmsUPbTAPP/instrumentSerialNumberOrLabIdentifierDefault
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
                    description: Operating mass resolution of the mass analyser. The
                      analyst selects low, medium, or high resolution to balance sensitivity
                      against spectral interference suppression.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/laSficpmsUPbTAPP/massResolutionSettingDefault
                      '@type':
                        const:
                        - schema:PropertyValueSpecification
                      schema:valueName:
                        const: massResolutionSettingDefault
                      schema:name:
                        const: Mass Resolution Setting
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
                  - title: Detector Configuration
                    description: Type(s) of detector(s) installed in the mass spectrometer.
                      For single-collector instruments, note whether dual pulse-counting/analog
                      mode is used. For multi-collector instruments, describe the
                      Faraday/multiplier cup layout.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/laSficpmsUPbTAPP/detectorConfiguration
                      '@type':
                        const:
                        - schema:PropertyValue
                      schema:propertyID:
                        const:
                        - '@id': ada:parameter/laSficpmsUPbTAPP/detectorConfiguration
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
                        const: ada:parameter/laSficpmsUPbTAPP/icpTuningDefault
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
                        const: ada:parameter/laSficpmsUPbTAPP/doublyChargedSpeciesMonitorDefault
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
                        const: ada:parameter/laSficpmsUPbTAPP/doublyChargedSpeciesProductionDefault
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
                        const: ada:parameter/laSficpmsUPbTAPP/memoryEffectMitigationDefault
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
                        const: ada:parameter/laSficpmsUPbTAPP/instrumentSerialNumberOrLabIdentifierDefault
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
                    description: Operating mass resolution of the mass analyser. The
                      analyst selects low, medium, or high resolution to balance sensitivity
                      against spectral interference suppression.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/laSficpmsUPbTAPP/massResolutionSettingDefault
                      '@type':
                        const:
                        - schema:PropertyValueSpecification
                      schema:valueName:
                        const: massResolutionSettingDefault
                      schema:name:
                        const: Mass Resolution Setting
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
                    title: Detector Configuration
                    description: Type(s) of detector(s) installed in the mass spectrometer.
                      For single-collector instruments, note whether dual pulse-counting/analog
                      mode is used. For multi-collector instruments, describe the
                      Faraday/multiplier cup layout.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/laSficpmsUPbTAPP/detectorConfiguration
                      '@type':
                        const:
                        - schema:PropertyValue
                      schema:propertyID:
                        const:
                        - '@id': ada:parameter/laSficpmsUPbTAPP/detectorConfiguration
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
                        const: ada:parameter/laSficpmsUPbTAPP/icpTuningDefault
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
                        const: ada:parameter/laSficpmsUPbTAPP/doublyChargedSpeciesMonitorDefault
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
                        const: ada:parameter/laSficpmsUPbTAPP/doublyChargedSpeciesProductionDefault
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
                        const: ada:parameter/laSficpmsUPbTAPP/memoryEffectMitigationDefault
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
                                  const: ada:parameter/laSficpmsUPbTAPP/interfaceConeConfiguration
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laSficpmsUPbTAPP/interfaceConeConfiguration
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
                                  const: ada:parameter/laSficpmsUPbTAPP/samplerAndSkimmerConeMaterial
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laSficpmsUPbTAPP/samplerAndSkimmerConeMaterial
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
                                  const: ada:parameter/laSficpmsUPbTAPP/interfaceConeConfiguration
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laSficpmsUPbTAPP/interfaceConeConfiguration
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
                                  const: ada:parameter/laSficpmsUPbTAPP/samplerAndSkimmerConeMaterial
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laSficpmsUPbTAPP/samplerAndSkimmerConeMaterial
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
                                const: ada:parameter/laSficpmsUPbTAPP/torchDepthDefault
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
                                  const: ada:parameter/laSficpmsUPbTAPP/torchDepthDefault
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
                                  const: ada:parameter/laSficpmsUPbTAPP/coolantGasFlowRateDefault
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
                                  const: ada:parameter/laSficpmsUPbTAPP/auxiliaryGasFlowRateDefault
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
                                  const: ada:parameter/laSficpmsUPbTAPP/rfPowerDefault
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
                                  const: ada:parameter/laSficpmsUPbTAPP/plasmaThermalMode
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laSficpmsUPbTAPP/plasmaThermalMode
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
                                  const: ada:parameter/laSficpmsUPbTAPP/coolantGasFlowRateDefault
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
                                  const: ada:parameter/laSficpmsUPbTAPP/auxiliaryGasFlowRateDefault
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
                                  const: ada:parameter/laSficpmsUPbTAPP/rfPowerDefault
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
                                  const: ada:parameter/laSficpmsUPbTAPP/plasmaThermalMode
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laSficpmsUPbTAPP/plasmaThermalMode
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
                            const: Collision Reaction Cell
                      required:
                      - schema:additionalType
                    then:
                      properties:
                        schema:name:
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
                            anyOf:
                            - title: Collision Gas Type
                              description: ''
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laSficpmsUPbTAPP/collisionGasType
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laSficpmsUPbTAPP/collisionGasType
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
                              description: ''
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laSficpmsUPbTAPP/collisionGasFlowRate
                                '@type':
                                  const:
                                  - schema:PropertyValueSpecification
                                schema:valueName:
                                  const: collisionGasFlowRate
                                schema:name:
                                  const: Collision Gas Flow Rate
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
                            - title: Cell Exit Discrimination Voltage
                              description: ''
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laSficpmsUPbTAPP/cellExitDiscriminationVoltage
                                '@type':
                                  const:
                                  - schema:PropertyValueSpecification
                                schema:valueName:
                                  const: cellExitDiscriminationVoltage
                                schema:name:
                                  const: Cell Exit Discrimination Voltage
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
                            - title: Reaction Gas Type
                              description: ''
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laSficpmsUPbTAPP/reactionGasType
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laSficpmsUPbTAPP/reactionGasType
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
                              description: ''
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laSficpmsUPbTAPP/reactionGasFlowRate
                                '@type':
                                  const:
                                  - schema:PropertyValueSpecification
                                schema:valueName:
                                  const: reactionGasFlowRate
                                schema:name:
                                  const: Reaction Gas Flow Rate
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
                              title: Collision Gas Type
                              description: ''
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laSficpmsUPbTAPP/collisionGasType
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laSficpmsUPbTAPP/collisionGasType
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
                              description: ''
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laSficpmsUPbTAPP/collisionGasFlowRate
                                '@type':
                                  const:
                                  - schema:PropertyValueSpecification
                                schema:valueName:
                                  const: collisionGasFlowRate
                                schema:name:
                                  const: Collision Gas Flow Rate
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
                              title: Cell Exit Discrimination Voltage
                              description: ''
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laSficpmsUPbTAPP/cellExitDiscriminationVoltage
                                '@type':
                                  const:
                                  - schema:PropertyValueSpecification
                                schema:valueName:
                                  const: cellExitDiscriminationVoltage
                                schema:name:
                                  const: Cell Exit Discrimination Voltage
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
                              title: Reaction Gas Type
                              description: ''
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laSficpmsUPbTAPP/reactionGasType
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laSficpmsUPbTAPP/reactionGasType
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
                              description: ''
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laSficpmsUPbTAPP/reactionGasFlowRate
                                '@type':
                                  const:
                                  - schema:PropertyValueSpecification
                                schema:valueName:
                                  const: reactionGasFlowRate
                                schema:name:
                                  const: Reaction Gas Flow Rate
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
                                  const: ada:parameter/laSficpmsUPbTAPP/faradayCupArrayConfiguration
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laSficpmsUPbTAPP/faradayCupArrayConfiguration
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
                                  const: ada:parameter/laSficpmsUPbTAPP/faradayCupAmplifierResistorValues
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laSficpmsUPbTAPP/faradayCupAmplifierResistorValues
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
                                  const: ada:parameter/laSficpmsUPbTAPP/faradayCupArrayConfiguration
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laSficpmsUPbTAPP/faradayCupArrayConfiguration
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
                                  const: ada:parameter/laSficpmsUPbTAPP/faradayCupAmplifierResistorValues
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laSficpmsUPbTAPP/faradayCupAmplifierResistorValues
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
            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/DefinedTerm
        ada:analyteColumns:
          type: array
          items:
            anyOf:
            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/AnalyteIdentifierColumn
            - title: Monitored Isotopes
              description: Specific isotope(s) monitored in this procedure, grouped
                by the analyte element they serve where they serve one. Includes interference-monitor
                and internal-standard masses, which serve no analyte and so have no
                parent element. The analyte list is given by the Analyte field and
                is never inferred from the element symbols appearing here.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/laSficpmsUPbTAPP/monitoredIsotopes
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
                  const: ada:analyteColumn/laSficpmsUPbTAPP/dwellTimePerMass
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
                  const: ada:analyteColumn/laSficpmsUPbTAPP/isobaricInterferenceCorrectionsApplied
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
                  const: ada:analyteColumn/laSficpmsUPbTAPP/interferingSpecies
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
                  const: ada:analyteColumn/laSficpmsUPbTAPP/interferenceCorrectionMethod
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
                  const: ada:analyteColumn/laSficpmsUPbTAPP/normalizationStandardsBasedCorrection
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
                  const: ada:analyteColumn/laSficpmsUPbTAPP/detectionLimit
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
                  const: ada:analyteColumn/laSficpmsUPbTAPP/detectionLimitMethod
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
                  const: ada:analyteColumn/laSficpmsUPbTAPP/limitOfQuantificationMethod
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
                  const: ada:analyteColumn/laSficpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod
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
                  const: ada:analyteColumn/laSficpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod
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
                  const: ada:analyteColumn/laSficpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod
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
                  const: ada:analyteColumn/laSficpmsUPbTAPP/massResolutionPerAnalyte
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
                  const: ada:analyteColumn/laSficpmsUPbTAPP/monitoredIsotopes
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
                  const: ada:analyteColumn/laSficpmsUPbTAPP/dwellTimePerMass
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
                  const: ada:analyteColumn/laSficpmsUPbTAPP/isobaricInterferenceCorrectionsApplied
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
                  const: ada:analyteColumn/laSficpmsUPbTAPP/interferingSpecies
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
                  const: ada:analyteColumn/laSficpmsUPbTAPP/interferenceCorrectionMethod
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
                  const: ada:analyteColumn/laSficpmsUPbTAPP/normalizationStandardsBasedCorrection
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
                  const: ada:analyteColumn/laSficpmsUPbTAPP/detectionLimit
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
                  const: ada:analyteColumn/laSficpmsUPbTAPP/detectionLimitMethod
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
                  const: ada:analyteColumn/laSficpmsUPbTAPP/limitOfQuantificationMethod
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
                  const: ada:analyteColumn/laSficpmsUPbTAPP/withinSessionAnalyticalPrecisionAndAssessmentMethod
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
                  const: ada:analyteColumn/laSficpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethod
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
                  const: ada:analyteColumn/laSficpmsUPbTAPP/analyticalAccuracyAndAssessmentMethod
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
                  const: ada:analyteColumn/laSficpmsUPbTAPP/massResolutionPerAnalyte
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
    ada:massResolutionAssignment:
      description: Mass resolution mode assigned to each acquired mass. The selected
        resolution determines which polyatomic interferences are physically resolved
        by the magnetic sector. One analyte may be acquired at more than one resolution,
        so the assignment is per acquired mass rather than per element. The overall
        mode(s) used in the procedure are recorded in Mass Resolution Setting (Group
        3).
      type: string
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
    ada:signalCollectionMode:
      type: string
      readOnly: true
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
  - ada:massResolutionAssignment
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

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS-UPb/tapp/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS-UPb/tapp/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS-UPb/tapp/context.jsonld)

## Sources

* [LA-SF-ICP-MS_UPb_TAPP_v17.csv (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/LA-SF-ICPMS-UPb/tapp`

