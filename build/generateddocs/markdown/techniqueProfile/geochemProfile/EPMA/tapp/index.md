
# EPMA Technique-Aligned Protocol Profile (epmaTAPP) (Schema)

`ogch.techniqueProfile.geochemProfile.EPMA.tapp` *v0.1*

EPMA-specific extension of the base TAPP definition. Adds EPMA top-level properties (beam mode, accelerating voltage, matrix correction method), a parameter vocabulary, and an analyte-column template covering EPMA per-element acquisition and reporting fields. Vocabularies, parameter templates, and analyte-column templates ship as separate JSON files under vocab/, parameters/, and analyteColumns/ for maintainability.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### epmaTAPP example Ma2015
epmaTAPP instance derived from Ma+2015 | Caltech GPS | WDS Point Analysis (JEOL 8200).
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
  "@id": "ex:epmaTAPP-Ma2015",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS Major Element Silicates/Oxides, Tissint Mars Meteorite (Caltech GPS, JEOL 8200)",
  "schema:description": "Ma et al. 2015, Earth Planet. Sci. Lett. — tissintite discovery paper (Tissint Mars meteorite). Instrument stated as \"JEOL 8200 electron microprobe\" (no JXA prefix). WDS explicitly stated (\"WDS: 15 kV; 5 nA; beam in focused mode\"). Point analysis only; no X-ray mapping reported. Probe for EPMA stated; CITZAF correction procedure (Armstrong 1995). Full standard suite with X-ray lines given. Detection limits: K=0.02, Cr=0.05, Mn=0.06 wt% from Table 1 footnote. Caltech GPS Division Analytical Facility. Reported detail: ada:edsAcquisitionMode = N/A — WDS procedure; ada:analyticalMode = WDS Point Analysis — 'WDS: 15 kV; 5 nA; beam in focused mode'; point analyses only.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "ada:beamDiameterDefault": "N — 'beam in focused mode' is recorded under Beam Mode; no diameter is given",
      "ada:beamMode": "all: Focused — 'WDS: 15 kV; 5 nA; beam in focused mode' (p.3)",
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        }
      ],
      "schema:name": "example instrumentName",
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:mappingBeamDiameterDefault": -9999,
      "ada:mappingBeamMode": "missing"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "JEOL 8200 (stated as \"JEOL 8200 electron microprobe\"; no JXA prefix stated)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Si",
      "Ti",
      "Al",
      "Cr",
      "Fe",
      "Mn",
      "Mg",
      "Ca",
      "Na",
      "K"
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
        "@id": "ada:targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "targetSpeciesEstimationMethod",
        "schema:name": "Target Species Estimation Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalAccuracy",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracy",
        "schema:name": "Analytical Accuracy",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalPrecision",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalPrecision",
        "schema:name": "Analytical Precision",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayBackgroundCorrectionMethod",
        "schema:name": "X-ray Background Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/beamCurrent",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "beamCurrent",
        "schema:name": "Beam Current",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/blankCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "blankCorrection",
        "schema:name": "Blank Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionStandard",
        "schema:name": "Interference Correction Standard",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayLineOverlapCorrectionsApplied",
        "schema:name": "X-ray Line Overlap Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferingElements",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingElements",
        "schema:name": "Interfering Elements",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "timeDependentIntensityCorrection",
        "schema:name": "Time-Dependent Intensity Correction",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:edsAcquisitionMode": "N/A",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
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
          "schema:defaultValue": "SEM BSE imaging on a ZEISS 1550VP field-emission SEM, which locates the occurrences the probe then analyses — \"SEM BSE image showing tissintite in a shock melt pocket, in Tissint section UT2\" (Fig. 1 caption, p.2). The paper lists EPMA, SEM, EBSD, synchrotron XRD and micro-Raman as one suite (p.2) without stating the order"
        }
      ]
    }
  ],
  "ada:matrixCorrectionMethod": "CITZAF (Armstrong 1995)",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "tissintite",
      "maskelynite",
      "pigeonite",
      "fayalite"
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
        "@id": "ada:targetMaterialColumn/epmaTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "Textural position relative to the shock-melt pockets — the analyses are grouped as \"Wormy type tissintite\", \"Rimming tissintite\", \"Maskelynite associated with wormy tissintite\" and \"Maskelynite away from melt pockets\" (Table 1, p.5), the phase itself occurring \"only in maskelynite less than ~25 μm of a shock melt pocket\" (p.1)",
  "ada:monitoredElements": [
    "Si, Al, Ca, Na, Fe, Mg, Mn, Ti, Cr, K — all determined; no monitor-only element. \"Standards for analysis were anorthite (SiKα, AlKα, CaKα); albite (NaKα); fayalite (FeKα); forsterite (MgKα); Mn2SiO4 (MnKα); TiO2 (TiKα); Cr2O3 (CrKα); and microcline (KKα)\" (p.3)"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "EPMA-WDS"
    }
  ],
  "schema:creator": {
    "schema:name": "Chi Ma",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Caltech GPS Division Analytical Facility"
  },
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NSF EAR-0318518; NSF DMR-0080065 — 'SEM, EBSD and EPMA analyses were carried out at the Caltech GPS Division Analytical Facility, which is supported, in part, by NSF Grants EAR-0318518 and DMR-0080065'"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Ma et al. 2015, Earth Planet. Sci. Lett. 422:194-205; doi:10.1016/j.epsl.2015.03.057"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM (Carl Zeiss 1550VP FE-SEM, BSE imaging); EBSD (HKL system on ZEISS 1550VP); synchrotron XRD; micro-Raman"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Phase > Analysis point — Table 1 reports one column per phase and textural setting (\"Wormy type tissintite\", \"Maskelynite away from melt pockets\" …), each the mean of n = 5–17 focused-beam point analyses (p.5)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "acquisition",
      "schema:name": "Probe for EPMA (Probe Software, Inc.)"
    },
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "N — the 'CITZAF correction procedure' is recorded under Matrix Correction Method; the only software named is Probe for EPMA"
    }
  ],
  "ada:analyticalMode": [
    "WDS Point Analysis"
  ],
  "ada:reportedProperties": [
    "SiO2, TiO2, Al2O3, FeO, MgO, CaO, Na2O, K2O, Cr2O3, MnO; cations per formula unit; Ca/(Ca+Na+K); Ca-Eskola component; An content of the precursor plagioclase — oxide wt% with totals and 1 s.d. of the mean, cations on 6 or 8 oxygens (Table 1); Ca-Eskola (mol%) and An58–69 (p.1)"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished thin section; carbon coating N",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
        "ada:detectionLimitMethod": "test value ada:detectionLimitMethod"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "test value schema:defaultValue"
    }
  ],
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
  "schema:datePublished": "test value schema:datePublished"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:epmaTAPP-Ma2015",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS Major Element Silicates/Oxides, Tissint Mars Meteorite (Caltech GPS, JEOL 8200)",
  "schema:description": "Ma et al. 2015, Earth Planet. Sci. Lett. \u2014 tissintite discovery paper (Tissint Mars meteorite). Instrument stated as \"JEOL 8200 electron microprobe\" (no JXA prefix). WDS explicitly stated (\"WDS: 15 kV; 5 nA; beam in focused mode\"). Point analysis only; no X-ray mapping reported. Probe for EPMA stated; CITZAF correction procedure (Armstrong 1995). Full standard suite with X-ray lines given. Detection limits: K=0.02, Cr=0.05, Mn=0.06 wt% from Table 1 footnote. Caltech GPS Division Analytical Facility. Reported detail: ada:edsAcquisitionMode = N/A \u2014 WDS procedure; ada:analyticalMode = WDS Point Analysis \u2014 'WDS: 15 kV; 5 nA; beam in focused mode'; point analyses only.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "ada:beamDiameterDefault": "N \u2014 'beam in focused mode' is recorded under Beam Mode; no diameter is given",
      "ada:beamMode": "all: Focused \u2014 'WDS: 15 kV; 5 nA; beam in focused mode' (p.3)",
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        }
      ],
      "schema:name": "example instrumentName",
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:mappingBeamDiameterDefault": -9999,
      "ada:mappingBeamMode": "missing"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "JEOL 8200 (stated as \"JEOL 8200 electron microprobe\"; no JXA prefix stated)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Si",
      "Ti",
      "Al",
      "Cr",
      "Fe",
      "Mn",
      "Mg",
      "Ca",
      "Na",
      "K"
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
        "@id": "ada:targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "targetSpeciesEstimationMethod",
        "schema:name": "Target Species Estimation Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalAccuracy",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracy",
        "schema:name": "Analytical Accuracy",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalPrecision",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalPrecision",
        "schema:name": "Analytical Precision",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayBackgroundCorrectionMethod",
        "schema:name": "X-ray Background Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/beamCurrent",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "beamCurrent",
        "schema:name": "Beam Current",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/blankCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "blankCorrection",
        "schema:name": "Blank Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionStandard",
        "schema:name": "Interference Correction Standard",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayLineOverlapCorrectionsApplied",
        "schema:name": "X-ray Line Overlap Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferingElements",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingElements",
        "schema:name": "Interfering Elements",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "timeDependentIntensityCorrection",
        "schema:name": "Time-Dependent Intensity Correction",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:edsAcquisitionMode": "N/A",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
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
          "schema:defaultValue": "SEM BSE imaging on a ZEISS 1550VP field-emission SEM, which locates the occurrences the probe then analyses \u2014 \"SEM BSE image showing tissintite in a shock melt pocket, in Tissint section UT2\" (Fig. 1 caption, p.2). The paper lists EPMA, SEM, EBSD, synchrotron XRD and micro-Raman as one suite (p.2) without stating the order"
        }
      ]
    }
  ],
  "ada:matrixCorrectionMethod": "CITZAF (Armstrong 1995)",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "tissintite",
      "maskelynite",
      "pigeonite",
      "fayalite"
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
        "@id": "ada:targetMaterialColumn/epmaTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "Textural position relative to the shock-melt pockets \u2014 the analyses are grouped as \"Wormy type tissintite\", \"Rimming tissintite\", \"Maskelynite associated with wormy tissintite\" and \"Maskelynite away from melt pockets\" (Table 1, p.5), the phase itself occurring \"only in maskelynite less than ~25 \u03bcm of a shock melt pocket\" (p.1)",
  "ada:monitoredElements": [
    "Si, Al, Ca, Na, Fe, Mg, Mn, Ti, Cr, K \u2014 all determined; no monitor-only element. \"Standards for analysis were anorthite (SiK\u03b1, AlK\u03b1, CaK\u03b1); albite (NaK\u03b1); fayalite (FeK\u03b1); forsterite (MgK\u03b1); Mn2SiO4 (MnK\u03b1); TiO2 (TiK\u03b1); Cr2O3 (CrK\u03b1); and microcline (KK\u03b1)\" (p.3)"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "EPMA-WDS"
    }
  ],
  "schema:creator": {
    "schema:name": "Chi Ma",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Caltech GPS Division Analytical Facility"
  },
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NSF EAR-0318518; NSF DMR-0080065 \u2014 'SEM, EBSD and EPMA analyses were carried out at the Caltech GPS Division Analytical Facility, which is supported, in part, by NSF Grants EAR-0318518 and DMR-0080065'"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Ma et al. 2015, Earth Planet. Sci. Lett. 422:194-205; doi:10.1016/j.epsl.2015.03.057"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM (Carl Zeiss 1550VP FE-SEM, BSE imaging); EBSD (HKL system on ZEISS 1550VP); synchrotron XRD; micro-Raman"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Phase > Analysis point \u2014 Table 1 reports one column per phase and textural setting (\"Wormy type tissintite\", \"Maskelynite away from melt pockets\" \u2026), each the mean of n = 5\u201317 focused-beam point analyses (p.5)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "acquisition",
      "schema:name": "Probe for EPMA (Probe Software, Inc.)"
    },
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "N \u2014 the 'CITZAF correction procedure' is recorded under Matrix Correction Method; the only software named is Probe for EPMA"
    }
  ],
  "ada:analyticalMode": [
    "WDS Point Analysis"
  ],
  "ada:reportedProperties": [
    "SiO2, TiO2, Al2O3, FeO, MgO, CaO, Na2O, K2O, Cr2O3, MnO; cations per formula unit; Ca/(Ca+Na+K); Ca-Eskola component; An content of the precursor plagioclase \u2014 oxide wt% with totals and 1 s.d. of the mean, cations on 6 or 8 oxygens (Table 1); Ca-Eskola (mol%) and An58\u201369 (p.1)"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished thin section; carbon coating N",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
        "ada:detectionLimitMethod": "test value ada:detectionLimitMethod"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "test value schema:defaultValue"
    }
  ],
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
  "schema:datePublished": "test value schema:datePublished"
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

<ex:epmaTAPP-Ma2015> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:description "Polished thin section; carbon coating N" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:detectionLimitMethod "test value ada:detectionLimitMethod" ] ] ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Chi Ma" ] ;
    schema1:datePublished "test value schema:datePublished" ;
    schema1:description "Ma et al. 2015, Earth Planet. Sci. Lett. — tissintite discovery paper (Tissint Mars meteorite). Instrument stated as \"JEOL 8200 electron microprobe\" (no JXA prefix). WDS explicitly stated (\"WDS: 15 kV; 5 nA; beam in focused mode\"). Point analysis only; no X-ray mapping reported. Probe for EPMA stated; CITZAF correction procedure (Armstrong 1995). Full standard suite with X-ray lines given. Detection limits: K=0.02, Cr=0.05, Mn=0.06 wt% from Table 1 footnote. Caltech GPS Division Analytical Facility. Reported detail: ada:edsAcquisitionMode = N/A — WDS procedure; ada:analyticalMode = WDS Point Analysis — 'WDS: 15 kV; 5 nA; beam in focused mode'; point analyses only." ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NSF EAR-0318518; NSF DMR-0080065 — 'SEM, EBSD and EPMA analyses were carried out at the Caltech GPS Division Analytical Facility, which is supported, in part, by NSF Grants EAR-0318518 and DMR-0080065'" ] ;
    schema1:instrument <ex:instrument/EPMA>,
        <ex:instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Caltech GPS Division Analytical Facility" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "EPMA-WDS" ] ;
    schema1:name "EPMA-WDS Major Element Silicates/Oxides, Tissint Mars Meteorite (Caltech GPS, JEOL 8200)" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Ma et al. 2015, Earth Planet. Sci. Lett. 422:194-205; doi:10.1016/j.epsl.2015.03.057" ] ;
            schema1:url "https://ada.astromat.org/missing" ],
        [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SEM (Carl Zeiss 1550VP FE-SEM, BSE imaging); EBSD (HKL system on ZEISS 1550VP); synchrotron XRD; micro-Raman" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "test value schema:defaultValue" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analyticalMode "WDS Point Analysis" ;
    ada:edsAcquisitionMode "N/A" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "CITZAF (Armstrong 1995)" ;
    ada:monitoredElements "Si, Al, Ca, Na, Fe, Mg, Mn, Ti, Cr, K — all determined; no monitor-only element. \"Standards for analysis were anorthite (SiKα, AlKα, CaKα); albite (NaKα); fayalite (FeKα); forsterite (MgKα); Mn2SiO4 (MnKα); TiO2 (TiKα); Cr2O3 (CrKα); and microcline (KKα)\" (p.3)" ;
    ada:reportedProperties "SiO2, TiO2, Al2O3, FeO, MgO, CaO, Na2O, K2O, Cr2O3, MnO; cations per formula unit; Ca/(Ca+Na+K); Ca-Eskola component; An content of the precursor plagioclase — oxide wt% with totals and 1 s.d. of the mean, cations on 6 or 8 oxygens (Table 1); Ca-Eskola (mol%) and An58–69 (p.1)" ;
    ada:samplingUnitSelectionCriteriaDefault "Textural position relative to the shock-melt pockets — the analyses are grouped as \"Wormy type tissintite\", \"Rimming tissintite\", \"Maskelynite associated with wormy tissintite\" and \"Maskelynite away from melt pockets\" (Table 1, p.5), the phase itself occurring \"only in maskelynite less than ~25 μm of a shock melt pocket\" (p.1)" ;
    ada:samplingUnitType "Phase > Analysis point — Table 1 reports one column per phase and textural setting (\"Wormy type tissintite\", \"Maskelynite away from melt pockets\" …), each the mean of n = 5–17 focused-beam point analyses (p.5)" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "fayalite",
                "maskelynite",
                "pigeonite",
                "tissintite" ;
            ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/backgroundCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/peakCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName> ] ;
    ada:targetSpeciesTemplate [ ada:defaultTargetSpecies "Al",
                "Ca",
                "Cr",
                "Fe",
                "K",
                "Mg",
                "Mn",
                "Na",
                "Si",
                "Ti" ;
            ada:targetSpeciesColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetSpecies" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalAccuracy>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalPrecision>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/beamCurrent>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/blankCorrection>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferingElements>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied> ] ;
    ada:wdsDeadTimeCorrection "missing" ;
    bios:computationalTool [ schema1:name "Probe for EPMA (Probe Software, Inc.)" ;
            ada:toolRole "acquisition" ],
        [ schema1:name "N — the 'CITZAF correction procedure' is recorded under Matrix Correction Method; the only software named is Probe for EPMA" ;
            ada:toolRole "dataReduction" ] .

<ex:instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:hasPart <ex:instrument/EPMA/part/EDS-Detector>,
        <ex:instrument/EPMA/part/Electron-Source>,
        <ex:instrument/EPMA/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "JEOL" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "15 kV" ;
    ada:beamDiameterDefault "N — 'beam in focused mode' is recorded under Beam Mode; no diameter is given" ;
    ada:beamMode "all: Focused — 'WDS: 15 kV; 5 nA; beam in focused mode' (p.3)" ;
    ada:mappingBeamCurrentDefault -9999 ;
    ada:mappingBeamDiameterDefault -9999 ;
    ada:mappingBeamMode "missing" .

<ex:instrument/EPMA/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:name "missing" .

<ex:instrument/EPMA/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "missing" ;
    schema1:name "missing" .

<ex:instrument/EPMA/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "missing" .

<ex:instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "JEOL 8200 (stated as \"JEOL 8200 electron microprobe\"; no JXA prefix stated)" ] ;
    schema1:name "example instrumentName" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "SEM BSE imaging on a ZEISS 1550VP field-emission SEM, which locates the occurrences the probe then analyses — \"SEM BSE image showing tissintite in a shock melt pocket, in Tissint section UT2\" (Fig. 1 caption, p.2). The paper lists EPMA, SEM, EBSD, synchrotron XRD and micro-Raman as one suite (p.2) without stating the order" ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:valueName "preAnalysisImagingAndScreeningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/backgroundCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Background Counting Time" ;
    schema1:valueName "backgroundCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/peakCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Peak Counting Time" ;
    schema1:valueName "peakCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalAccuracy> a schema1:PropertyValueSpecification ;
    schema1:name "Analytical Accuracy" ;
    schema1:valueName "analyticalAccuracy" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalPrecision> a schema1:PropertyValueSpecification ;
    schema1:name "Analytical Precision" ;
    schema1:valueName "analyticalPrecision" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/beamCurrent> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Beam Current" ;
    schema1:valueName "beamCurrent" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/blankCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Blank Correction" ;
    schema1:valueName "blankCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard> a schema1:PropertyValueSpecification ;
    schema1:name "Interference Correction Standard" ;
    schema1:valueName "interferenceCorrectionStandard" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferingElements> a schema1:PropertyValueSpecification ;
    schema1:name "Interfering Elements" ;
    schema1:valueName "interferingElements" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Target Species Estimation Method" ;
    schema1:valueName "targetSpeciesEstimationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Time-Dependent Intensity Correction" ;
    schema1:valueName "timeDependentIntensityCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "X-ray Background Correction Method" ;
    schema1:valueName "xRayBackgroundCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "X-ray Line Overlap Corrections Applied" ;
    schema1:valueName "xRayLineOverlapCorrectionsApplied" ;
    ada:dataType "string" .


```


### epmaTAPP example Hu2020
epmaTAPP instance derived from Hu+2020 | IGGCAS | WDS Point Analysis (JEOL JXA-8100).
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
  "@id": "ex:epmaTAPP-Hu2020",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA Major Element Silicates/Oxides, NWA 8657 Shergottite (IGGCAS, JEOL JXA-8100)",
  "schema:description": "Hu et al. 2020, Geochim. Cosmochim. Acta — coesite in NWA 8657 shergottite. JEOL JXA-8100 at IGGCAS; 15 kV, 10 nA; point analysis only; WDS or EDS not stated. Matrix correction: Bence-Albee (not PAP). Full primary standard suite stated (kaersutite, jadeite, bustamite, K-feldspar, rutile, Cr2O3). Mn Kα / Cr Kβ interference correction applied. Detection limits 0.01-0.06 wt% stated per oxide. Analytical software not stated. Reported detail: ada:edsAcquisitionMode = N — WDS or EDS is not stated; ada:analyticalMode = N — quantitative point analyses ('Quantitative analyses of maskelynite ... were conducted by electron probe microanalysis'); WDS or EDS is not stated, and the list has no value without one.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "ada:beamDiameterDefault": "N — only 15 kV and 10 nA are given",
      "ada:beamMode": "N — only 15 kV and 10 nA are given",
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        }
      ],
      "schema:name": "example instrumentName",
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:mappingBeamDiameterDefault": -9999,
      "ada:mappingBeamMode": "missing"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "JXA-8100 (stated as \"JEOL JXA-8100\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Si",
      "Ti",
      "Al",
      "Cr",
      "Fe",
      "Mn",
      "Mg",
      "Ca",
      "Na",
      "K"
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
        "@id": "ada:targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "targetSpeciesEstimationMethod",
        "schema:name": "Target Species Estimation Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalAccuracy",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracy",
        "schema:name": "Analytical Accuracy",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalPrecision",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalPrecision",
        "schema:name": "Analytical Precision",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayBackgroundCorrectionMethod",
        "schema:name": "X-ray Background Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/beamCurrent",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "beamCurrent",
        "schema:name": "Beam Current",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/blankCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "blankCorrection",
        "schema:name": "Blank Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionStandard",
        "schema:name": "Interference Correction Standard",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayLineOverlapCorrectionsApplied",
        "schema:name": "X-ray Line Overlap Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferingElements",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingElements",
        "schema:name": "Interfering Elements",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "timeDependentIntensityCorrection",
        "schema:name": "Time-Dependent Intensity Correction",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:edsAcquisitionMode": "N/A",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
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
          "schema:defaultValue": "SEM imaging and EDS mapping on three instruments before the probe — \"Scanning electron microscopy (SEM) imaging and energy dispersive X-ray spectroscopy (EDS) mapping were conducted\" on a Nova NanoSEM 450 at IGGCAS, a SUPRA55 at NAOC and a JEOL JSM-7100F at NIPR, after which \"Quantitative analyses ... were conducted by electron probe microanalysis (EPMA) with the JEOL JXA-8100 at IGGCAS\" (p.2)"
        }
      ]
    }
  ],
  "ada:matrixCorrectionMethod": "Bence-Albee",
  "ada:targetMaterialTemplate": {
    "ada:targetMaterialDeclaration": "maskelynite; melt inclusion glasses; silica glasses; coesite aggregates; mesostasis — 'Quantitative analyses of maskelynite, melt inclusion glasses, silica glasses, coesite aggregates, and mesostasis were conducted by EPMA' (p.2)",
    "ada:defaultTargetMaterials": [
      "maskelynite",
      "silica glasses",
      "coesite aggregates",
      "mesostasis"
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
        "@id": "ada:targetMaterialColumn/epmaTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "N — the paper names the phases it analysed (see `Sampling Unit Type`) but states no rule for choosing the individual units",
  "ada:monitoredElements": [
    "Si, Mg, Fe, Na, Al, Ca, Mn, K, Ti, Cr — all determined. \"The EPMA standards were natural and synthetic minerals: natural kaersutite for Si, Mg and Fe, jadeite for Na and Al, bustamite for Ca and Mn, and K-feldspar for K, synthetic rutile for Ti and Cr2O3 for Cr\". Cr also carries the interference correction — \"X-ray interference of the Kα line of Mn by the Kβ line of Cr was corrected\" — but is itself determined, so it is not an orphan"
  ],
  "schema:creator": {
    "schema:name": "Sen Hu",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Institute of Geology and Geophysics, Chinese Academy of Sciences (IGGCAS), Beijing"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Hu et al. 2020, Geochim. Cosmochim. Acta 278:185-198; doi:10.1016/j.gca.2019.06.012"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-EDS (FEI Nova NanoSEM 450); Raman spectroscopy"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Phase > Analysis point — \"Quantitative analyses of maskelynite, melt inclusion glasses, silica glasses, coesite aggregates, and mesostasis were conducted by electron probe microanalysis\" (p.2); points are grouped by phase, not reported individually in the archived PDF",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "N — 'The Bence-Albee method was used' is recorded under Matrix Correction Method; no software is named"
    }
  ],
  "ada:reportedProperties": [
    "SiO2, TiO2, Al2O3, Cr2O3, FeO, MnO, MgO, CaO, Na2O, K2O — oxide wt% for maskelynite, melt inclusion glasses, silica glasses, coesite aggregates and mesostasis (p.2)"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished thick section (NWA 8657); carbon coating N",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
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
      "schema:name": "epma",
      "schema:termCode": "epma"
    }
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "test value schema:defaultValue"
    }
  ],
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
  "schema:datePublished": "test value schema:datePublished"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:epmaTAPP-Hu2020",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA Major Element Silicates/Oxides, NWA 8657 Shergottite (IGGCAS, JEOL JXA-8100)",
  "schema:description": "Hu et al. 2020, Geochim. Cosmochim. Acta \u2014 coesite in NWA 8657 shergottite. JEOL JXA-8100 at IGGCAS; 15 kV, 10 nA; point analysis only; WDS or EDS not stated. Matrix correction: Bence-Albee (not PAP). Full primary standard suite stated (kaersutite, jadeite, bustamite, K-feldspar, rutile, Cr2O3). Mn K\u03b1 / Cr K\u03b2 interference correction applied. Detection limits 0.01-0.06 wt% stated per oxide. Analytical software not stated. Reported detail: ada:edsAcquisitionMode = N \u2014 WDS or EDS is not stated; ada:analyticalMode = N \u2014 quantitative point analyses ('Quantitative analyses of maskelynite ... were conducted by electron probe microanalysis'); WDS or EDS is not stated, and the list has no value without one.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "ada:beamDiameterDefault": "N \u2014 only 15 kV and 10 nA are given",
      "ada:beamMode": "N \u2014 only 15 kV and 10 nA are given",
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        }
      ],
      "schema:name": "example instrumentName",
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:mappingBeamDiameterDefault": -9999,
      "ada:mappingBeamMode": "missing"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "JXA-8100 (stated as \"JEOL JXA-8100\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Si",
      "Ti",
      "Al",
      "Cr",
      "Fe",
      "Mn",
      "Mg",
      "Ca",
      "Na",
      "K"
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
        "@id": "ada:targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "targetSpeciesEstimationMethod",
        "schema:name": "Target Species Estimation Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalAccuracy",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracy",
        "schema:name": "Analytical Accuracy",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalPrecision",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalPrecision",
        "schema:name": "Analytical Precision",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayBackgroundCorrectionMethod",
        "schema:name": "X-ray Background Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/beamCurrent",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "beamCurrent",
        "schema:name": "Beam Current",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/blankCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "blankCorrection",
        "schema:name": "Blank Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionStandard",
        "schema:name": "Interference Correction Standard",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayLineOverlapCorrectionsApplied",
        "schema:name": "X-ray Line Overlap Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferingElements",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingElements",
        "schema:name": "Interfering Elements",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "timeDependentIntensityCorrection",
        "schema:name": "Time-Dependent Intensity Correction",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:edsAcquisitionMode": "N/A",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
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
          "schema:defaultValue": "SEM imaging and EDS mapping on three instruments before the probe \u2014 \"Scanning electron microscopy (SEM) imaging and energy dispersive X-ray spectroscopy (EDS) mapping were conducted\" on a Nova NanoSEM 450 at IGGCAS, a SUPRA55 at NAOC and a JEOL JSM-7100F at NIPR, after which \"Quantitative analyses ... were conducted by electron probe microanalysis (EPMA) with the JEOL JXA-8100 at IGGCAS\" (p.2)"
        }
      ]
    }
  ],
  "ada:matrixCorrectionMethod": "Bence-Albee",
  "ada:targetMaterialTemplate": {
    "ada:targetMaterialDeclaration": "maskelynite; melt inclusion glasses; silica glasses; coesite aggregates; mesostasis \u2014 'Quantitative analyses of maskelynite, melt inclusion glasses, silica glasses, coesite aggregates, and mesostasis were conducted by EPMA' (p.2)",
    "ada:defaultTargetMaterials": [
      "maskelynite",
      "silica glasses",
      "coesite aggregates",
      "mesostasis"
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
        "@id": "ada:targetMaterialColumn/epmaTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "N \u2014 the paper names the phases it analysed (see `Sampling Unit Type`) but states no rule for choosing the individual units",
  "ada:monitoredElements": [
    "Si, Mg, Fe, Na, Al, Ca, Mn, K, Ti, Cr \u2014 all determined. \"The EPMA standards were natural and synthetic minerals: natural kaersutite for Si, Mg and Fe, jadeite for Na and Al, bustamite for Ca and Mn, and K-feldspar for K, synthetic rutile for Ti and Cr2O3 for Cr\". Cr also carries the interference correction \u2014 \"X-ray interference of the K\u03b1 line of Mn by the K\u03b2 line of Cr was corrected\" \u2014 but is itself determined, so it is not an orphan"
  ],
  "schema:creator": {
    "schema:name": "Sen Hu",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Institute of Geology and Geophysics, Chinese Academy of Sciences (IGGCAS), Beijing"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Hu et al. 2020, Geochim. Cosmochim. Acta 278:185-198; doi:10.1016/j.gca.2019.06.012"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-EDS (FEI Nova NanoSEM 450); Raman spectroscopy"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Phase > Analysis point \u2014 \"Quantitative analyses of maskelynite, melt inclusion glasses, silica glasses, coesite aggregates, and mesostasis were conducted by electron probe microanalysis\" (p.2); points are grouped by phase, not reported individually in the archived PDF",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "N \u2014 'The Bence-Albee method was used' is recorded under Matrix Correction Method; no software is named"
    }
  ],
  "ada:reportedProperties": [
    "SiO2, TiO2, Al2O3, Cr2O3, FeO, MnO, MgO, CaO, Na2O, K2O \u2014 oxide wt% for maskelynite, melt inclusion glasses, silica glasses, coesite aggregates and mesostasis (p.2)"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished thick section (NWA 8657); carbon coating N",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
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
      "schema:name": "epma",
      "schema:termCode": "epma"
    }
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "test value schema:defaultValue"
    }
  ],
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
  "schema:datePublished": "test value schema:datePublished"
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

<ex:epmaTAPP-Hu2020> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:detectionLimitMethod "test value ada:detectionLimitMethod" ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:description "Polished thick section (NWA 8657); carbon coating N" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Sen Hu" ] ;
    schema1:datePublished "test value schema:datePublished" ;
    schema1:description "Hu et al. 2020, Geochim. Cosmochim. Acta — coesite in NWA 8657 shergottite. JEOL JXA-8100 at IGGCAS; 15 kV, 10 nA; point analysis only; WDS or EDS not stated. Matrix correction: Bence-Albee (not PAP). Full primary standard suite stated (kaersutite, jadeite, bustamite, K-feldspar, rutile, Cr2O3). Mn Kα / Cr Kβ interference correction applied. Detection limits 0.01-0.06 wt% stated per oxide. Analytical software not stated. Reported detail: ada:edsAcquisitionMode = N — WDS or EDS is not stated; ada:analyticalMode = N — quantitative point analyses ('Quantitative analyses of maskelynite ... were conducted by electron probe microanalysis'); WDS or EDS is not stated, and the list has no value without one." ;
    schema1:instrument <ex:instrument/EPMA>,
        <ex:instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Institute of Geology and Geophysics, Chinese Academy of Sciences (IGGCAS), Beijing" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "epma" ;
            schema1:termCode "epma" ] ;
    schema1:name "EPMA Major Element Silicates/Oxides, NWA 8657 Shergottite (IGGCAS, JEOL JXA-8100)" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Hu et al. 2020, Geochim. Cosmochim. Acta 278:185-198; doi:10.1016/j.gca.2019.06.012" ] ;
            schema1:url "https://ada.astromat.org/missing" ],
        [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SEM-EDS (FEI Nova NanoSEM 450); Raman spectroscopy" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "test value schema:defaultValue" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:edsAcquisitionMode "N/A" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "Bence-Albee" ;
    ada:monitoredElements "Si, Mg, Fe, Na, Al, Ca, Mn, K, Ti, Cr — all determined. \"The EPMA standards were natural and synthetic minerals: natural kaersutite for Si, Mg and Fe, jadeite for Na and Al, bustamite for Ca and Mn, and K-feldspar for K, synthetic rutile for Ti and Cr2O3 for Cr\". Cr also carries the interference correction — \"X-ray interference of the Kα line of Mn by the Kβ line of Cr was corrected\" — but is itself determined, so it is not an orphan" ;
    ada:reportedProperties "SiO2, TiO2, Al2O3, Cr2O3, FeO, MnO, MgO, CaO, Na2O, K2O — oxide wt% for maskelynite, melt inclusion glasses, silica glasses, coesite aggregates and mesostasis (p.2)" ;
    ada:samplingUnitSelectionCriteriaDefault "N — the paper names the phases it analysed (see `Sampling Unit Type`) but states no rule for choosing the individual units" ;
    ada:samplingUnitType "Phase > Analysis point — \"Quantitative analyses of maskelynite, melt inclusion glasses, silica glasses, coesite aggregates, and mesostasis were conducted by electron probe microanalysis\" (p.2); points are grouped by phase, not reported individually in the archived PDF" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "coesite aggregates",
                "maskelynite",
                "mesostasis",
                "silica glasses" ;
            ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/backgroundCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/peakCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName> ;
            ada:targetMaterialDeclaration "maskelynite; melt inclusion glasses; silica glasses; coesite aggregates; mesostasis — 'Quantitative analyses of maskelynite, melt inclusion glasses, silica glasses, coesite aggregates, and mesostasis were conducted by EPMA' (p.2)" ] ;
    ada:targetSpeciesTemplate [ ada:defaultTargetSpecies "Al",
                "Ca",
                "Cr",
                "Fe",
                "K",
                "Mg",
                "Mn",
                "Na",
                "Si",
                "Ti" ;
            ada:targetSpeciesColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetSpecies" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalAccuracy>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalPrecision>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/beamCurrent>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/blankCorrection>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferingElements>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied> ] ;
    ada:wdsDeadTimeCorrection "missing" ;
    bios:computationalTool [ schema1:name "N — 'The Bence-Albee method was used' is recorded under Matrix Correction Method; no software is named" ;
            ada:toolRole "dataReduction" ] .

<ex:instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:hasPart <ex:instrument/EPMA/part/EDS-Detector>,
        <ex:instrument/EPMA/part/Electron-Source>,
        <ex:instrument/EPMA/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "JEOL" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "15 kV" ;
    ada:beamDiameterDefault "N — only 15 kV and 10 nA are given" ;
    ada:beamMode "N — only 15 kV and 10 nA are given" ;
    ada:mappingBeamCurrentDefault -9999 ;
    ada:mappingBeamDiameterDefault -9999 ;
    ada:mappingBeamMode "missing" .

<ex:instrument/EPMA/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:name "missing" .

<ex:instrument/EPMA/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "missing" ;
    schema1:name "missing" .

<ex:instrument/EPMA/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "missing" .

<ex:instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "JXA-8100 (stated as \"JEOL JXA-8100\")" ] ;
    schema1:name "example instrumentName" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "SEM imaging and EDS mapping on three instruments before the probe — \"Scanning electron microscopy (SEM) imaging and energy dispersive X-ray spectroscopy (EDS) mapping were conducted\" on a Nova NanoSEM 450 at IGGCAS, a SUPRA55 at NAOC and a JEOL JSM-7100F at NIPR, after which \"Quantitative analyses ... were conducted by electron probe microanalysis (EPMA) with the JEOL JXA-8100 at IGGCAS\" (p.2)" ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:valueName "preAnalysisImagingAndScreeningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/backgroundCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Background Counting Time" ;
    schema1:valueName "backgroundCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/peakCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Peak Counting Time" ;
    schema1:valueName "peakCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalAccuracy> a schema1:PropertyValueSpecification ;
    schema1:name "Analytical Accuracy" ;
    schema1:valueName "analyticalAccuracy" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalPrecision> a schema1:PropertyValueSpecification ;
    schema1:name "Analytical Precision" ;
    schema1:valueName "analyticalPrecision" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/beamCurrent> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Beam Current" ;
    schema1:valueName "beamCurrent" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/blankCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Blank Correction" ;
    schema1:valueName "blankCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard> a schema1:PropertyValueSpecification ;
    schema1:name "Interference Correction Standard" ;
    schema1:valueName "interferenceCorrectionStandard" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferingElements> a schema1:PropertyValueSpecification ;
    schema1:name "Interfering Elements" ;
    schema1:valueName "interferingElements" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Target Species Estimation Method" ;
    schema1:valueName "targetSpeciesEstimationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Time-Dependent Intensity Correction" ;
    schema1:valueName "timeDependentIntensityCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "X-ray Background Correction Method" ;
    schema1:valueName "xRayBackgroundCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "X-ray Line Overlap Corrections Applied" ;
    schema1:valueName "xRayLineOverlapCorrectionsApplied" ;
    ada:dataType "string" .


```


### epmaTAPP example Liu2016
epmaTAPP instance derived from Liu+2016_UT | Cameca SX100 | WDS Mapping (U.Tennessee).
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
  "@id": "ex:epmaTAPP-Liu2016",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA Major Element Silicates/Oxides+Mapping, Tissint (U. Tennessee, Cameca SX100)",
  "schema:description": "Liu et al. 2016, Meteorit. Planet. Sci. — Tissint mineral chemistry. Protocol 1 of 2: University of Tennessee Cameca SX100. Same paper also uses Caltech GPS JXA-8200 (see Liu+2016_Cal column). Point analysis AND X-ray mapping performed at UT. Specific mapping: BSE + Ca/Al/Fe/Mg Ka maps (15 kV, 20 nA, step 8-12 µm). Olivine megacryst mapping (15 kV, 200 nA, step 2 µm, dwell ~0.5 s) described as \"using the EMP\" — instrument ambiguous (may be UT or Caltech instrument). Standards, matrix correction, and software not stated. Reported detail: ada:edsAcquisitionMode = N — WDS or EDS is not stated; ada:analyticalMode = N — quantitative point analyses and elemental X-ray maps; WDS or EDS is not stated, and the list has no value without one.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "ada:beamDiameterDefault": "olivine, pyroxene, Fe-Ti-Cr oxides: 1–2 µm; maskelynite, phosphate, sulfide, glass: 5–10 µm — p.3",
      "ada:beamMode": "maskelynite, phosphate, sulfide, glass: Defocused; other: N — 'Maskelynite, phosphate, sulfide, and glass were analyzed using a defocused beam of 5–10 µm size'; for olivine, pyroxene and Fe-Ti-Cr oxides only a '1–2 µm beam diameter' is given, not a mode",
      "schema:manufacturer": {
        "schema:name": "Cameca",
        "@type": [
          "schema:Organization"
        ]
      },
      "ada:mappingBeamMode": "Focused (section maps and olivine megacryst maps) — 'a 20 nA focused beam'; 'a focused beam of 15 kV voltage and 200 nA current'",
      "ada:mappingBeamCurrentDefault": "20 nA (section maps: Ca, Al, Fe, Mg Kα); 200 nA (olivine megacryst maps) — p.3",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        }
      ],
      "schema:name": "example instrumentName",
      "ada:mappingBeamDiameterDefault": -9999
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "SX100 (stated as \"Cameca SX100\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Si",
      "Ti",
      "Al",
      "Mg",
      "Ca",
      "Fe",
      "Mn",
      "Cr",
      "Ni",
      "Na",
      "K",
      "P"
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
        "@id": "ada:targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "targetSpeciesEstimationMethod",
        "schema:name": "Target Species Estimation Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalAccuracy",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracy",
        "schema:name": "Analytical Accuracy",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalPrecision",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalPrecision",
        "schema:name": "Analytical Precision",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayBackgroundCorrectionMethod",
        "schema:name": "X-ray Background Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/beamCurrent",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "beamCurrent",
        "schema:name": "Beam Current",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/blankCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "blankCorrection",
        "schema:name": "Blank Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionStandard",
        "schema:name": "Interference Correction Standard",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayLineOverlapCorrectionsApplied",
        "schema:name": "X-ray Line Overlap Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferingElements",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingElements",
        "schema:name": "Interfering Elements",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "timeDependentIntensityCorrection",
        "schema:name": "Time-Dependent Intensity Correction",
        "ada:dataType": "string"
      }
    ]
  },
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/epmaTAPP/beamDamageMinimizationDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "beamDamageMinimizationDefault",
      "schema:name": "Beam Damage Minimization",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N — a defocused 5–10 µm beam at 10 nA is used for maskelynite, phosphate, sulfide and glass, but the paper gives no reason for it"
    }
  ],
  "ada:edsAcquisitionMode": "N/A",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
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
          "schema:defaultValue": "Petrographic microscopy and SEM — \"The petrography of these sections was examined using a petrographic microscope and a scanning electron microscope\" before the microprobe work (p.3)"
        }
      ]
    }
  ],
  "ada:stepSizePixelSizeDefault": "8-12 µm (BSE + Ca/Al/Fe/Mg Ka phase maps at UT); 2 µm (olivine megacryst Ka maps; instrument ambiguous)",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "olivine",
      "pyroxene",
      "Fe-Ti-Cr oxides",
      "maskelynite",
      "phosphate",
      "sulfide",
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
        "@id": "ada:targetMaterialColumn/epmaTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "N — the map areas are shown rather than specified: a \"Red box outlines the area of X-ray maps\" on an olivine megacryst (Fig. 3 caption, p.7), with no stated rule for placing them",
  "ada:monitoredElements": [
    "Si, Ti, Al, Mg, Ca, Fe, Mn, Cr, Ni, Na, K, P — point analyses on both instruments (the detection-limit sentence names their oxides); maps: 'Ca Ka, Al Ka, Fe Ka, and Mg Ka' (four sections) and 'Fe Ka, P Ka, Al Ka, Ca Ka, and Cr Ka' (two olivine megacrysts, collected on 'the EMP' — the instrument is not named)"
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Department of Earth and Planetary Sciences, University of Tennessee, Knoxville"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Liu et al. 2016, Meteorit. Planet. Sci.; doi:10.1111/maps.12726"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM (BSE imaging); petrographic microscopy; LA-ICP-MS (Agilent 7500ce, Virginia Tech)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Whole sample (thin section) > Phase — \"elemental X-ray maps (Ca Ka, Al Ka, Fe Ka, and Mg Ka) of four sections\" (p.3); the reported quantity is a modal fraction, \"the number of pixels attributed to each mineral ... divided by the total number of pixels in the whole section\" (p.3)",
  "ada:reportedProperties": [
    "SiO2, TiO2, Al2O3, Cr2O3, FeO, MnO, MgO, CaO, Na2O, NiO, P2O5, K2O, V2O3, La2O3, Ce2O3; modal-area fraction per mineral (vol%); Mg#; En, Fs, Wo — oxide wt% 'of selected minerals' (Table 2), with V2O3, La2O3 and Ce2O3 for the oxides and merrillite; glass means with 1σ (Table 3); modal abundances from the X-ray maps (Table 1)"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished thin sections (coating type N)",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
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
      "schema:name": "epma",
      "schema:termCode": "epma"
    }
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "test value schema:defaultValue"
    }
  ],
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:wdsDeadTimeCorrection": "missing",
  "schema:datePublished": "test value schema:datePublished"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:epmaTAPP-Liu2016",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA Major Element Silicates/Oxides+Mapping, Tissint (U. Tennessee, Cameca SX100)",
  "schema:description": "Liu et al. 2016, Meteorit. Planet. Sci. \u2014 Tissint mineral chemistry. Protocol 1 of 2: University of Tennessee Cameca SX100. Same paper also uses Caltech GPS JXA-8200 (see Liu+2016_Cal column). Point analysis AND X-ray mapping performed at UT. Specific mapping: BSE + Ca/Al/Fe/Mg Ka maps (15 kV, 20 nA, step 8-12 \u00b5m). Olivine megacryst mapping (15 kV, 200 nA, step 2 \u00b5m, dwell ~0.5 s) described as \"using the EMP\" \u2014 instrument ambiguous (may be UT or Caltech instrument). Standards, matrix correction, and software not stated. Reported detail: ada:edsAcquisitionMode = N \u2014 WDS or EDS is not stated; ada:analyticalMode = N \u2014 quantitative point analyses and elemental X-ray maps; WDS or EDS is not stated, and the list has no value without one.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "ada:beamDiameterDefault": "olivine, pyroxene, Fe-Ti-Cr oxides: 1\u20132 \u00b5m; maskelynite, phosphate, sulfide, glass: 5\u201310 \u00b5m \u2014 p.3",
      "ada:beamMode": "maskelynite, phosphate, sulfide, glass: Defocused; other: N \u2014 'Maskelynite, phosphate, sulfide, and glass were analyzed using a defocused beam of 5\u201310 \u00b5m size'; for olivine, pyroxene and Fe-Ti-Cr oxides only a '1\u20132 \u00b5m beam diameter' is given, not a mode",
      "schema:manufacturer": {
        "schema:name": "Cameca",
        "@type": [
          "schema:Organization"
        ]
      },
      "ada:mappingBeamMode": "Focused (section maps and olivine megacryst maps) \u2014 'a 20 nA focused beam'; 'a focused beam of 15 kV voltage and 200 nA current'",
      "ada:mappingBeamCurrentDefault": "20 nA (section maps: Ca, Al, Fe, Mg K\u03b1); 200 nA (olivine megacryst maps) \u2014 p.3",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        }
      ],
      "schema:name": "example instrumentName",
      "ada:mappingBeamDiameterDefault": -9999
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "SX100 (stated as \"Cameca SX100\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Si",
      "Ti",
      "Al",
      "Mg",
      "Ca",
      "Fe",
      "Mn",
      "Cr",
      "Ni",
      "Na",
      "K",
      "P"
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
        "@id": "ada:targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "targetSpeciesEstimationMethod",
        "schema:name": "Target Species Estimation Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalAccuracy",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracy",
        "schema:name": "Analytical Accuracy",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalPrecision",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalPrecision",
        "schema:name": "Analytical Precision",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayBackgroundCorrectionMethod",
        "schema:name": "X-ray Background Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/beamCurrent",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "beamCurrent",
        "schema:name": "Beam Current",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/blankCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "blankCorrection",
        "schema:name": "Blank Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionStandard",
        "schema:name": "Interference Correction Standard",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayLineOverlapCorrectionsApplied",
        "schema:name": "X-ray Line Overlap Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferingElements",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingElements",
        "schema:name": "Interfering Elements",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "timeDependentIntensityCorrection",
        "schema:name": "Time-Dependent Intensity Correction",
        "ada:dataType": "string"
      }
    ]
  },
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/epmaTAPP/beamDamageMinimizationDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "beamDamageMinimizationDefault",
      "schema:name": "Beam Damage Minimization",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N \u2014 a defocused 5\u201310 \u00b5m beam at 10 nA is used for maskelynite, phosphate, sulfide and glass, but the paper gives no reason for it"
    }
  ],
  "ada:edsAcquisitionMode": "N/A",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
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
          "schema:defaultValue": "Petrographic microscopy and SEM \u2014 \"The petrography of these sections was examined using a petrographic microscope and a scanning electron microscope\" before the microprobe work (p.3)"
        }
      ]
    }
  ],
  "ada:stepSizePixelSizeDefault": "8-12 \u00b5m (BSE + Ca/Al/Fe/Mg Ka phase maps at UT); 2 \u00b5m (olivine megacryst Ka maps; instrument ambiguous)",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "olivine",
      "pyroxene",
      "Fe-Ti-Cr oxides",
      "maskelynite",
      "phosphate",
      "sulfide",
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
        "@id": "ada:targetMaterialColumn/epmaTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "N \u2014 the map areas are shown rather than specified: a \"Red box outlines the area of X-ray maps\" on an olivine megacryst (Fig. 3 caption, p.7), with no stated rule for placing them",
  "ada:monitoredElements": [
    "Si, Ti, Al, Mg, Ca, Fe, Mn, Cr, Ni, Na, K, P \u2014 point analyses on both instruments (the detection-limit sentence names their oxides); maps: 'Ca Ka, Al Ka, Fe Ka, and Mg Ka' (four sections) and 'Fe Ka, P Ka, Al Ka, Ca Ka, and Cr Ka' (two olivine megacrysts, collected on 'the EMP' \u2014 the instrument is not named)"
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Department of Earth and Planetary Sciences, University of Tennessee, Knoxville"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Liu et al. 2016, Meteorit. Planet. Sci.; doi:10.1111/maps.12726"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM (BSE imaging); petrographic microscopy; LA-ICP-MS (Agilent 7500ce, Virginia Tech)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Whole sample (thin section) > Phase \u2014 \"elemental X-ray maps (Ca Ka, Al Ka, Fe Ka, and Mg Ka) of four sections\" (p.3); the reported quantity is a modal fraction, \"the number of pixels attributed to each mineral ... divided by the total number of pixels in the whole section\" (p.3)",
  "ada:reportedProperties": [
    "SiO2, TiO2, Al2O3, Cr2O3, FeO, MnO, MgO, CaO, Na2O, NiO, P2O5, K2O, V2O3, La2O3, Ce2O3; modal-area fraction per mineral (vol%); Mg#; En, Fs, Wo \u2014 oxide wt% 'of selected minerals' (Table 2), with V2O3, La2O3 and Ce2O3 for the oxides and merrillite; glass means with 1\u03c3 (Table 3); modal abundances from the X-ray maps (Table 1)"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished thin sections (coating type N)",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
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
      "schema:name": "epma",
      "schema:termCode": "epma"
    }
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "test value schema:defaultValue"
    }
  ],
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:wdsDeadTimeCorrection": "missing",
  "schema:datePublished": "test value schema:datePublished"
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

<ex:epmaTAPP-Liu2016> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:description "Polished thin sections (coating type N)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:detectionLimitMethod "test value ada:detectionLimitMethod" ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDamageMinimizationDefault> ;
    schema1:datePublished "test value schema:datePublished" ;
    schema1:description "Liu et al. 2016, Meteorit. Planet. Sci. — Tissint mineral chemistry. Protocol 1 of 2: University of Tennessee Cameca SX100. Same paper also uses Caltech GPS JXA-8200 (see Liu+2016_Cal column). Point analysis AND X-ray mapping performed at UT. Specific mapping: BSE + Ca/Al/Fe/Mg Ka maps (15 kV, 20 nA, step 8-12 µm). Olivine megacryst mapping (15 kV, 200 nA, step 2 µm, dwell ~0.5 s) described as \"using the EMP\" — instrument ambiguous (may be UT or Caltech instrument). Standards, matrix correction, and software not stated. Reported detail: ada:edsAcquisitionMode = N — WDS or EDS is not stated; ada:analyticalMode = N — quantitative point analyses and elemental X-ray maps; WDS or EDS is not stated, and the list has no value without one." ;
    schema1:instrument <ex:instrument/EPMA>,
        <ex:instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Department of Earth and Planetary Sciences, University of Tennessee, Knoxville" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "epma" ;
            schema1:termCode "epma" ] ;
    schema1:name "EPMA Major Element Silicates/Oxides+Mapping, Tissint (U. Tennessee, Cameca SX100)" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Liu et al. 2016, Meteorit. Planet. Sci.; doi:10.1111/maps.12726" ] ;
            schema1:url "https://ada.astromat.org/missing" ],
        [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SEM (BSE imaging); petrographic microscopy; LA-ICP-MS (Agilent 7500ce, Virginia Tech)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "test value schema:defaultValue" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:edsAcquisitionMode "N/A" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:monitoredElements "Si, Ti, Al, Mg, Ca, Fe, Mn, Cr, Ni, Na, K, P — point analyses on both instruments (the detection-limit sentence names their oxides); maps: 'Ca Ka, Al Ka, Fe Ka, and Mg Ka' (four sections) and 'Fe Ka, P Ka, Al Ka, Ca Ka, and Cr Ka' (two olivine megacrysts, collected on 'the EMP' — the instrument is not named)" ;
    ada:reportedProperties "SiO2, TiO2, Al2O3, Cr2O3, FeO, MnO, MgO, CaO, Na2O, NiO, P2O5, K2O, V2O3, La2O3, Ce2O3; modal-area fraction per mineral (vol%); Mg#; En, Fs, Wo — oxide wt% 'of selected minerals' (Table 2), with V2O3, La2O3 and Ce2O3 for the oxides and merrillite; glass means with 1σ (Table 3); modal abundances from the X-ray maps (Table 1)" ;
    ada:samplingUnitSelectionCriteriaDefault "N — the map areas are shown rather than specified: a \"Red box outlines the area of X-ray maps\" on an olivine megacryst (Fig. 3 caption, p.7), with no stated rule for placing them" ;
    ada:samplingUnitType "Whole sample (thin section) > Phase — \"elemental X-ray maps (Ca Ka, Al Ka, Fe Ka, and Mg Ka) of four sections\" (p.3); the reported quantity is a modal fraction, \"the number of pixels attributed to each mineral ... divided by the total number of pixels in the whole section\" (p.3)" ;
    ada:stepSizePixelSizeDefault "8-12 µm (BSE + Ca/Al/Fe/Mg Ka phase maps at UT); 2 µm (olivine megacryst Ka maps; instrument ambiguous)" ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "Fe-Ti-Cr oxides",
                "glass",
                "maskelynite",
                "olivine",
                "phosphate",
                "pyroxene",
                "sulfide" ;
            ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/backgroundCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/peakCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName> ] ;
    ada:targetSpeciesTemplate [ ada:defaultTargetSpecies "Al",
                "Ca",
                "Cr",
                "Fe",
                "K",
                "Mg",
                "Mn",
                "Na",
                "Ni",
                "P",
                "Si",
                "Ti" ;
            ada:targetSpeciesColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetSpecies" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalAccuracy>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalPrecision>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/beamCurrent>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/blankCorrection>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferingElements>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied> ] ;
    ada:wdsDeadTimeCorrection "missing" .

<ex:instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:hasPart <ex:instrument/EPMA/part/EDS-Detector>,
        <ex:instrument/EPMA/part/Electron-Source>,
        <ex:instrument/EPMA/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Cameca" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "15 kV" ;
    ada:beamDiameterDefault "olivine, pyroxene, Fe-Ti-Cr oxides: 1–2 µm; maskelynite, phosphate, sulfide, glass: 5–10 µm — p.3" ;
    ada:beamMode "maskelynite, phosphate, sulfide, glass: Defocused; other: N — 'Maskelynite, phosphate, sulfide, and glass were analyzed using a defocused beam of 5–10 µm size'; for olivine, pyroxene and Fe-Ti-Cr oxides only a '1–2 µm beam diameter' is given, not a mode" ;
    ada:mappingBeamCurrentDefault "20 nA (section maps: Ca, Al, Fe, Mg Kα); 200 nA (olivine megacryst maps) — p.3" ;
    ada:mappingBeamDiameterDefault -9999 ;
    ada:mappingBeamMode "Focused (section maps and olivine megacryst maps) — 'a 20 nA focused beam'; 'a focused beam of 15 kV voltage and 200 nA current'" .

<ex:instrument/EPMA/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:name "missing" .

<ex:instrument/EPMA/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "missing" ;
    schema1:name "missing" .

<ex:instrument/EPMA/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "missing" .

<ex:instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "SX100 (stated as \"Cameca SX100\")" ] ;
    schema1:name "example instrumentName" .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDamageMinimizationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N — a defocused 5–10 µm beam at 10 nA is used for maskelynite, phosphate, sulfide and glass, but the paper gives no reason for it" ;
    schema1:name "Beam Damage Minimization" ;
    schema1:valueName "beamDamageMinimizationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Petrographic microscopy and SEM — \"The petrography of these sections was examined using a petrographic microscope and a scanning electron microscope\" before the microprobe work (p.3)" ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:valueName "preAnalysisImagingAndScreeningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/backgroundCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Background Counting Time" ;
    schema1:valueName "backgroundCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/peakCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Peak Counting Time" ;
    schema1:valueName "peakCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalAccuracy> a schema1:PropertyValueSpecification ;
    schema1:name "Analytical Accuracy" ;
    schema1:valueName "analyticalAccuracy" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalPrecision> a schema1:PropertyValueSpecification ;
    schema1:name "Analytical Precision" ;
    schema1:valueName "analyticalPrecision" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/beamCurrent> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Beam Current" ;
    schema1:valueName "beamCurrent" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/blankCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Blank Correction" ;
    schema1:valueName "blankCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard> a schema1:PropertyValueSpecification ;
    schema1:name "Interference Correction Standard" ;
    schema1:valueName "interferenceCorrectionStandard" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferingElements> a schema1:PropertyValueSpecification ;
    schema1:name "Interfering Elements" ;
    schema1:valueName "interferingElements" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Target Species Estimation Method" ;
    schema1:valueName "targetSpeciesEstimationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Time-Dependent Intensity Correction" ;
    schema1:valueName "timeDependentIntensityCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "X-ray Background Correction Method" ;
    schema1:valueName "xRayBackgroundCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "X-ray Line Overlap Corrections Applied" ;
    schema1:valueName "xRayLineOverlapCorrectionsApplied" ;
    ada:dataType "string" .


```


### epmaTAPP example Liu2016-2
epmaTAPP instance derived from Liu+2016_Cal | JEOL JXA-8200 | WDS Point Analysis (Caltech GPS).
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
  "@id": "ex:epmaTAPP-Liu2016-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA Major Element Silicates/Oxides, Tissint (Caltech GPS, JEOL JXA-8200)",
  "schema:description": "Liu et al. 2016, Meteorit. Planet. Sci. — Tissint mineral chemistry. Protocol 2 of 2: Caltech GPS Division JEOL JXA-8200. Point analysis only (no mapping attributed to Caltech instrument). Conditions stated jointly for UT and Caltech instruments. Standards, matrix correction, and software not stated for EPMA. Reported detail: ada:edsAcquisitionMode = N — WDS or EDS is not stated; ada:analyticalMode = N — quantitative point analyses; WDS or EDS is not stated, and the list has no value without one.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "ada:beamDiameterDefault": "olivine, pyroxene, Fe-Ti-Cr oxides: 1–2 µm; maskelynite, phosphate, sulfide, glass: 5–10 µm — p.3",
      "ada:beamMode": "maskelynite, phosphate, sulfide, glass: Defocused; other: N — 'Maskelynite, phosphate, sulfide, and glass were analyzed using a defocused beam of 5–10 µm size'; for olivine, pyroxene and Fe-Ti-Cr oxides only a '1–2 µm beam diameter' is given, not a mode",
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        }
      ],
      "schema:name": "example instrumentName",
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:mappingBeamDiameterDefault": -9999,
      "ada:mappingBeamMode": "missing"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "JXA-8200 (stated as \"JEOL JXA-8200\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Si",
      "Ti",
      "Al",
      "Mg",
      "Ca",
      "Fe",
      "Mn",
      "Cr",
      "Ni",
      "Na",
      "K",
      "P"
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
        "@id": "ada:targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "targetSpeciesEstimationMethod",
        "schema:name": "Target Species Estimation Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalAccuracy",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracy",
        "schema:name": "Analytical Accuracy",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalPrecision",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalPrecision",
        "schema:name": "Analytical Precision",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayBackgroundCorrectionMethod",
        "schema:name": "X-ray Background Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/beamCurrent",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "beamCurrent",
        "schema:name": "Beam Current",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/blankCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "blankCorrection",
        "schema:name": "Blank Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionStandard",
        "schema:name": "Interference Correction Standard",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayLineOverlapCorrectionsApplied",
        "schema:name": "X-ray Line Overlap Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferingElements",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingElements",
        "schema:name": "Interfering Elements",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "timeDependentIntensityCorrection",
        "schema:name": "Time-Dependent Intensity Correction",
        "ada:dataType": "string"
      }
    ]
  },
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/epmaTAPP/beamDamageMinimizationDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "beamDamageMinimizationDefault",
      "schema:name": "Beam Damage Minimization",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N — a defocused 5–10 µm beam at 10 nA is used for maskelynite, phosphate, sulfide and glass, but the paper gives no reason for it"
    }
  ],
  "ada:edsAcquisitionMode": "N/A",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
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
          "schema:defaultValue": "Petrographic microscopy and SEM — \"The petrography of these sections was examined using a petrographic microscope and a scanning electron microscope\" (p.3); the same sections then went to both microprobes"
        }
      ]
    }
  ],
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "olivine",
      "pyroxene",
      "Fe-Ti-Cr oxides",
      "maskelynite",
      "phosphate",
      "sulfide",
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
        "@id": "ada:targetMaterialColumn/epmaTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "N — the paper names the phases it analysed (see `Sampling Unit Type`) but states no rule for choosing the individual units",
  "ada:monitoredElements": [
    "Si, Ti, Al, Mg, Ca, Fe, Mn, Cr, Ni, Na, K, P — all determined. \"Detection limits are typically <0.03 wt% for SiO2, TiO2, Al2O3, MgO, and CaO; <0.05–0.1 wt% for FeO, MnO, Cr2O3, NiO, Na2O, K2O, and P2O5\" (p.4)"
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Division of Geological and Planetary Sciences, Caltech"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Liu et al. 2016, Meteorit. Planet. Sci.; doi:10.1111/maps.12726"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM (BSE imaging); petrographic microscopy; LA-ICP-MS (Agilent 7500ce, Virginia Tech)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Phase > Analysis point — \"Major and minor element compositions of selected minerals\" by phase (Table 2, p.6); glass compositions are means, \"EMP avg (n = 73)\" and \"avg (n = 14)\" (Table 3, p.9)",
  "ada:reportedProperties": [
    "SiO2, TiO2, Al2O3, Cr2O3, FeO, MnO, MgO, CaO, Na2O, NiO, P2O5, K2O, V2O3, La2O3, Ce2O3; modal-area fraction per mineral (vol%); Mg#; En, Fs, Wo — oxide wt% 'of selected minerals' (Table 2), with V2O3, La2O3 and Ce2O3 for the oxides and merrillite; glass means with 1σ (Table 3); modal abundances from the X-ray maps (Table 1)"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished thin sections (coating type N)",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
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
      "schema:name": "epma",
      "schema:termCode": "epma"
    }
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "test value schema:defaultValue"
    }
  ],
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
  "schema:datePublished": "test value schema:datePublished"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:epmaTAPP-Liu2016-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA Major Element Silicates/Oxides, Tissint (Caltech GPS, JEOL JXA-8200)",
  "schema:description": "Liu et al. 2016, Meteorit. Planet. Sci. \u2014 Tissint mineral chemistry. Protocol 2 of 2: Caltech GPS Division JEOL JXA-8200. Point analysis only (no mapping attributed to Caltech instrument). Conditions stated jointly for UT and Caltech instruments. Standards, matrix correction, and software not stated for EPMA. Reported detail: ada:edsAcquisitionMode = N \u2014 WDS or EDS is not stated; ada:analyticalMode = N \u2014 quantitative point analyses; WDS or EDS is not stated, and the list has no value without one.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "ada:beamDiameterDefault": "olivine, pyroxene, Fe-Ti-Cr oxides: 1\u20132 \u00b5m; maskelynite, phosphate, sulfide, glass: 5\u201310 \u00b5m \u2014 p.3",
      "ada:beamMode": "maskelynite, phosphate, sulfide, glass: Defocused; other: N \u2014 'Maskelynite, phosphate, sulfide, and glass were analyzed using a defocused beam of 5\u201310 \u00b5m size'; for olivine, pyroxene and Fe-Ti-Cr oxides only a '1\u20132 \u00b5m beam diameter' is given, not a mode",
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        }
      ],
      "schema:name": "example instrumentName",
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:mappingBeamDiameterDefault": -9999,
      "ada:mappingBeamMode": "missing"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "JXA-8200 (stated as \"JEOL JXA-8200\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Si",
      "Ti",
      "Al",
      "Mg",
      "Ca",
      "Fe",
      "Mn",
      "Cr",
      "Ni",
      "Na",
      "K",
      "P"
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
        "@id": "ada:targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "targetSpeciesEstimationMethod",
        "schema:name": "Target Species Estimation Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalAccuracy",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracy",
        "schema:name": "Analytical Accuracy",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalPrecision",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalPrecision",
        "schema:name": "Analytical Precision",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayBackgroundCorrectionMethod",
        "schema:name": "X-ray Background Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/beamCurrent",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "beamCurrent",
        "schema:name": "Beam Current",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/blankCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "blankCorrection",
        "schema:name": "Blank Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionStandard",
        "schema:name": "Interference Correction Standard",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayLineOverlapCorrectionsApplied",
        "schema:name": "X-ray Line Overlap Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferingElements",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingElements",
        "schema:name": "Interfering Elements",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "timeDependentIntensityCorrection",
        "schema:name": "Time-Dependent Intensity Correction",
        "ada:dataType": "string"
      }
    ]
  },
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/epmaTAPP/beamDamageMinimizationDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "beamDamageMinimizationDefault",
      "schema:name": "Beam Damage Minimization",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N \u2014 a defocused 5\u201310 \u00b5m beam at 10 nA is used for maskelynite, phosphate, sulfide and glass, but the paper gives no reason for it"
    }
  ],
  "ada:edsAcquisitionMode": "N/A",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
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
          "schema:defaultValue": "Petrographic microscopy and SEM \u2014 \"The petrography of these sections was examined using a petrographic microscope and a scanning electron microscope\" (p.3); the same sections then went to both microprobes"
        }
      ]
    }
  ],
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "olivine",
      "pyroxene",
      "Fe-Ti-Cr oxides",
      "maskelynite",
      "phosphate",
      "sulfide",
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
        "@id": "ada:targetMaterialColumn/epmaTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "N \u2014 the paper names the phases it analysed (see `Sampling Unit Type`) but states no rule for choosing the individual units",
  "ada:monitoredElements": [
    "Si, Ti, Al, Mg, Ca, Fe, Mn, Cr, Ni, Na, K, P \u2014 all determined. \"Detection limits are typically <0.03 wt% for SiO2, TiO2, Al2O3, MgO, and CaO; <0.05\u20130.1 wt% for FeO, MnO, Cr2O3, NiO, Na2O, K2O, and P2O5\" (p.4)"
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Division of Geological and Planetary Sciences, Caltech"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Liu et al. 2016, Meteorit. Planet. Sci.; doi:10.1111/maps.12726"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM (BSE imaging); petrographic microscopy; LA-ICP-MS (Agilent 7500ce, Virginia Tech)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Phase > Analysis point \u2014 \"Major and minor element compositions of selected minerals\" by phase (Table 2, p.6); glass compositions are means, \"EMP avg (n = 73)\" and \"avg (n = 14)\" (Table 3, p.9)",
  "ada:reportedProperties": [
    "SiO2, TiO2, Al2O3, Cr2O3, FeO, MnO, MgO, CaO, Na2O, NiO, P2O5, K2O, V2O3, La2O3, Ce2O3; modal-area fraction per mineral (vol%); Mg#; En, Fs, Wo \u2014 oxide wt% 'of selected minerals' (Table 2), with V2O3, La2O3 and Ce2O3 for the oxides and merrillite; glass means with 1\u03c3 (Table 3); modal abundances from the X-ray maps (Table 1)"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished thin sections (coating type N)",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
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
      "schema:name": "epma",
      "schema:termCode": "epma"
    }
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "test value schema:defaultValue"
    }
  ],
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
  "schema:datePublished": "test value schema:datePublished"
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

<ex:epmaTAPP-Liu2016-2> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:detectionLimitMethod "test value ada:detectionLimitMethod" ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:description "Polished thin sections (coating type N)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDamageMinimizationDefault> ;
    schema1:datePublished "test value schema:datePublished" ;
    schema1:description "Liu et al. 2016, Meteorit. Planet. Sci. — Tissint mineral chemistry. Protocol 2 of 2: Caltech GPS Division JEOL JXA-8200. Point analysis only (no mapping attributed to Caltech instrument). Conditions stated jointly for UT and Caltech instruments. Standards, matrix correction, and software not stated for EPMA. Reported detail: ada:edsAcquisitionMode = N — WDS or EDS is not stated; ada:analyticalMode = N — quantitative point analyses; WDS or EDS is not stated, and the list has no value without one." ;
    schema1:instrument <ex:instrument/EPMA>,
        <ex:instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Division of Geological and Planetary Sciences, Caltech" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "epma" ;
            schema1:termCode "epma" ] ;
    schema1:name "EPMA Major Element Silicates/Oxides, Tissint (Caltech GPS, JEOL JXA-8200)" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Liu et al. 2016, Meteorit. Planet. Sci.; doi:10.1111/maps.12726" ] ;
            schema1:url "https://ada.astromat.org/missing" ],
        [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SEM (BSE imaging); petrographic microscopy; LA-ICP-MS (Agilent 7500ce, Virginia Tech)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "test value schema:defaultValue" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:edsAcquisitionMode "N/A" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:monitoredElements "Si, Ti, Al, Mg, Ca, Fe, Mn, Cr, Ni, Na, K, P — all determined. \"Detection limits are typically <0.03 wt% for SiO2, TiO2, Al2O3, MgO, and CaO; <0.05–0.1 wt% for FeO, MnO, Cr2O3, NiO, Na2O, K2O, and P2O5\" (p.4)" ;
    ada:reportedProperties "SiO2, TiO2, Al2O3, Cr2O3, FeO, MnO, MgO, CaO, Na2O, NiO, P2O5, K2O, V2O3, La2O3, Ce2O3; modal-area fraction per mineral (vol%); Mg#; En, Fs, Wo — oxide wt% 'of selected minerals' (Table 2), with V2O3, La2O3 and Ce2O3 for the oxides and merrillite; glass means with 1σ (Table 3); modal abundances from the X-ray maps (Table 1)" ;
    ada:samplingUnitSelectionCriteriaDefault "N — the paper names the phases it analysed (see `Sampling Unit Type`) but states no rule for choosing the individual units" ;
    ada:samplingUnitType "Phase > Analysis point — \"Major and minor element compositions of selected minerals\" by phase (Table 2, p.6); glass compositions are means, \"EMP avg (n = 73)\" and \"avg (n = 14)\" (Table 3, p.9)" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "Fe-Ti-Cr oxides",
                "glass",
                "maskelynite",
                "olivine",
                "phosphate",
                "pyroxene",
                "sulfide" ;
            ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/backgroundCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/peakCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName> ] ;
    ada:targetSpeciesTemplate [ ada:defaultTargetSpecies "Al",
                "Ca",
                "Cr",
                "Fe",
                "K",
                "Mg",
                "Mn",
                "Na",
                "Ni",
                "P",
                "Si",
                "Ti" ;
            ada:targetSpeciesColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetSpecies" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalAccuracy>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalPrecision>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/beamCurrent>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/blankCorrection>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferingElements>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied> ] ;
    ada:wdsDeadTimeCorrection "missing" .

<ex:instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:hasPart <ex:instrument/EPMA/part/EDS-Detector>,
        <ex:instrument/EPMA/part/Electron-Source>,
        <ex:instrument/EPMA/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "JEOL" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "15 kV" ;
    ada:beamDiameterDefault "olivine, pyroxene, Fe-Ti-Cr oxides: 1–2 µm; maskelynite, phosphate, sulfide, glass: 5–10 µm — p.3" ;
    ada:beamMode "maskelynite, phosphate, sulfide, glass: Defocused; other: N — 'Maskelynite, phosphate, sulfide, and glass were analyzed using a defocused beam of 5–10 µm size'; for olivine, pyroxene and Fe-Ti-Cr oxides only a '1–2 µm beam diameter' is given, not a mode" ;
    ada:mappingBeamCurrentDefault -9999 ;
    ada:mappingBeamDiameterDefault -9999 ;
    ada:mappingBeamMode "missing" .

<ex:instrument/EPMA/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:name "missing" .

<ex:instrument/EPMA/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "missing" ;
    schema1:name "missing" .

<ex:instrument/EPMA/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "missing" .

<ex:instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "JXA-8200 (stated as \"JEOL JXA-8200\")" ] ;
    schema1:name "example instrumentName" .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDamageMinimizationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N — a defocused 5–10 µm beam at 10 nA is used for maskelynite, phosphate, sulfide and glass, but the paper gives no reason for it" ;
    schema1:name "Beam Damage Minimization" ;
    schema1:valueName "beamDamageMinimizationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Petrographic microscopy and SEM — \"The petrography of these sections was examined using a petrographic microscope and a scanning electron microscope\" (p.3); the same sections then went to both microprobes" ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:valueName "preAnalysisImagingAndScreeningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/backgroundCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Background Counting Time" ;
    schema1:valueName "backgroundCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/peakCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Peak Counting Time" ;
    schema1:valueName "peakCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalAccuracy> a schema1:PropertyValueSpecification ;
    schema1:name "Analytical Accuracy" ;
    schema1:valueName "analyticalAccuracy" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalPrecision> a schema1:PropertyValueSpecification ;
    schema1:name "Analytical Precision" ;
    schema1:valueName "analyticalPrecision" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/beamCurrent> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Beam Current" ;
    schema1:valueName "beamCurrent" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/blankCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Blank Correction" ;
    schema1:valueName "blankCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard> a schema1:PropertyValueSpecification ;
    schema1:name "Interference Correction Standard" ;
    schema1:valueName "interferenceCorrectionStandard" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferingElements> a schema1:PropertyValueSpecification ;
    schema1:name "Interfering Elements" ;
    schema1:valueName "interferingElements" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Target Species Estimation Method" ;
    schema1:valueName "targetSpeciesEstimationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Time-Dependent Intensity Correction" ;
    schema1:valueName "timeDependentIntensityCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "X-ray Background Correction Method" ;
    schema1:valueName "xRayBackgroundCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "X-ray Line Overlap Corrections Applied" ;
    schema1:valueName "xRayLineOverlapCorrectionsApplied" ;
    ada:dataType "string" .


```


### epmaTAPP example Ma2017
epmaTAPP instance derived from Ma+2017 | JEOL 8200 | WDS Point Analysis (Caltech GPS Analytical Facility).
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
  "@id": "ex:epmaTAPP-Ma2017",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS Major Element Silicates/Glasses, Zagami (Caltech GPS Analytical Facility, JEOL 8200)",
  "schema:description": "Ma et al. 2018, Meteorit. Planet. Sci. 53:50-61 (file dated 2017) — liebermannite (KAlSi3O8) discovery from Zagami. Instrument stated as \"JEOL 8200 electron microprobe\" (no JXA prefix in text). WDS explicitly stated (\"WDS: 15 kV, 5 nA\"). Probe for EPMA; CITZAF correction (Armstrong 1995) — NOT PAP. Full standard suite and X-ray lines stated. K-mapping by EPMA also performed (used for mineral identification) but mapping conditions (step size, dwell time, current) not stated. Na diffusion observed during analysis despite low 5 nA beam current. Detection limits stated (per-element wt% values). Analytical accuracy: 1-2% for Si, Al, Ca, Na, K (feldspar standards as unknowns). Caltech GPS Division Analytical Facility. Reported detail: ada:edsAcquisitionMode = N/A — WDS procedure; ada:analyticalMode = WDS Point Analysis — 'WDS: 15 kV, 5 nA'; the paper also mentions 'K-mapping by EPMA', with no detector or conditions.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "ada:beamDiameterDefault": "N — 'beam in focused mode' is recorded under Beam Mode; no diameter is given",
      "ada:beamMode": "all: Focused — 'WDS: 15 kV, 5 nA, beam in focused mode' (p.2)",
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        }
      ],
      "schema:name": "example instrumentName",
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:mappingBeamDiameterDefault": -9999,
      "ada:mappingBeamMode": "missing"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "JEOL 8200 (stated as \"JEOL 8200 electron microprobe\"; no JXA prefix in paper)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Si",
      "Al",
      "K",
      "Na",
      "Ca",
      "Fe",
      "Mg",
      "Ti",
      "Cr",
      "Mn"
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
        "@id": "ada:targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "targetSpeciesEstimationMethod",
        "schema:name": "Target Species Estimation Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalAccuracy",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracy",
        "schema:name": "Analytical Accuracy",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalPrecision",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalPrecision",
        "schema:name": "Analytical Precision",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayBackgroundCorrectionMethod",
        "schema:name": "X-ray Background Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/beamCurrent",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "beamCurrent",
        "schema:name": "Beam Current",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/blankCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "blankCorrection",
        "schema:name": "Blank Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionStandard",
        "schema:name": "Interference Correction Standard",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayLineOverlapCorrectionsApplied",
        "schema:name": "X-ray Line Overlap Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferingElements",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingElements",
        "schema:name": "Interfering Elements",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "timeDependentIntensityCorrection",
        "schema:name": "Time-Dependent Intensity Correction",
        "ada:dataType": "string"
      }
    ]
  },
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/epmaTAPP/beamDamageMinimizationDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "beamDamageMinimizationDefault",
      "schema:name": "Beam Damage Minimization",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "all: low beam current (5 nA) — 'Although a low beam current of 5 nA was used for the analysis, the low cation sum (0.92) for the K-site is likely due to diffusion of Na away from the electron beam' (p.3)"
    }
  ],
  "ada:edsAcquisitionMode": "N/A",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
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
          "schema:defaultValue": "SEM BSE imaging on a ZEISS 1550VP field-emission SEM — \"Backscattered electron (BSE) imaging was performed using a Carl Zeiss, LLC 1550VP field emission SEM\" (p.2), locating the three occurrences of the new mineral in the Zagami thin section (Fig. 1, p.2). The paper lists EPMA, SEM, EBSD, synchrotron XRD and micro-Raman as one suite (p.2) without stating the order"
        }
      ]
    }
  ],
  "ada:matrixCorrectionMethod": "CITZAF (Armstrong 1995)",
  "ada:secondaryReferenceMaterialDefault": [
    "feldspar standards — 'based on analysis of feldspar standards as unknowns'; not named individually"
  ],
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "liebermannite",
      "lingunite",
      "maskelynite"
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
        "@id": "ada:targetMaterialColumn/epmaTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "Occurrence of the target phase — the units analysed are the observed occurrences of the new mineral: \"A first occurrence of liebermannite was observed with lingunite, silica, ilmenite, and baddeleyite ... (this is the type material). A second occurrence ... A third occurrence is shown in Fig. 1c, close to the type occurrence\" (p.4)",
  "ada:monitoredElements": [
    "Si, Al, K, Ca, Na, Fe, Mg, Ti, Cr, Mn — all determined. \"Standards for analysis were Asbestos microcline (SiKa, AlKa, KKa), synthetic anorthite (CaKa), Amelia albite (NaKa), synthetic fayalite (FeKa), synthetic forsterite (MgKa), synthetic TiO2 (TiKa), synthetic Cr2O3 (CrKa), and synthetic Mn-olivine (MnKa)\", with detection limits quoted for the same ten (p.2)"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "EPMA-WDS"
    }
  ],
  "schema:creator": {
    "schema:name": "Chi Ma",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Division of Geological and Planetary Sciences Analytical Facility, Caltech"
  },
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NSF EAR-0318518; NSF EAR-1322082; NSF DMR-0080065 — 'SEM, EBSD, EPMA, and Raman measurements were carried out at the Geological and Planetary Science Division Analytical Facility at Caltech, which is supported in part by NSF grants EAR-0318518, EAR-1322082, and DMR-0080065'"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Ma et al. 2018, Meteorit. Planet. Sci. 53:50-61; doi:10.1111/maps.13000 (file dated 2017)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM (Carl Zeiss 1550VP FE-SEM, BSE imaging); EBSD; synchrotron XRD; micro-Raman"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Grain > Analysis point — Table 1 reports one column per occurrence (\"Type liebermannite\", \"The second liebermannite\", \"The third liebermannite\", \"Lingunite next to type liebermannite\" …), each the mean of n = 2–6 points (p.3)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "acquisition",
      "schema:name": "Probe for EPMA (Probe Software, Inc.)"
    },
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "N — the 'CITZAF correction procedure' is recorded under Matrix Correction Method; the only software named is Probe for EPMA"
    }
  ],
  "ada:analyticalMode": [
    "WDS Point Analysis"
  ],
  "ada:reportedProperties": [
    "SiO2, TiO2, Al2O3, FeO, CaO, Na2O, K2O; cations per formula unit; density — oxide wt% with totals and 1 s.d. of the mean, cations on 8 oxygens (Table 1); 'Magnesium, Cr, and Mn were also analyzed but were below the detection limit in all cases'; calculated density 3.98 g cm-3 (p.3)"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished thin section USNM 7619 (coating type N)",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
        "ada:detectionLimitMethod": "test value ada:detectionLimitMethod"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "test value schema:defaultValue"
    }
  ],
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
  "schema:datePublished": "test value schema:datePublished"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:epmaTAPP-Ma2017",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS Major Element Silicates/Glasses, Zagami (Caltech GPS Analytical Facility, JEOL 8200)",
  "schema:description": "Ma et al. 2018, Meteorit. Planet. Sci. 53:50-61 (file dated 2017) \u2014 liebermannite (KAlSi3O8) discovery from Zagami. Instrument stated as \"JEOL 8200 electron microprobe\" (no JXA prefix in text). WDS explicitly stated (\"WDS: 15 kV, 5 nA\"). Probe for EPMA; CITZAF correction (Armstrong 1995) \u2014 NOT PAP. Full standard suite and X-ray lines stated. K-mapping by EPMA also performed (used for mineral identification) but mapping conditions (step size, dwell time, current) not stated. Na diffusion observed during analysis despite low 5 nA beam current. Detection limits stated (per-element wt% values). Analytical accuracy: 1-2% for Si, Al, Ca, Na, K (feldspar standards as unknowns). Caltech GPS Division Analytical Facility. Reported detail: ada:edsAcquisitionMode = N/A \u2014 WDS procedure; ada:analyticalMode = WDS Point Analysis \u2014 'WDS: 15 kV, 5 nA'; the paper also mentions 'K-mapping by EPMA', with no detector or conditions.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "ada:beamDiameterDefault": "N \u2014 'beam in focused mode' is recorded under Beam Mode; no diameter is given",
      "ada:beamMode": "all: Focused \u2014 'WDS: 15 kV, 5 nA, beam in focused mode' (p.2)",
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        }
      ],
      "schema:name": "example instrumentName",
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:mappingBeamDiameterDefault": -9999,
      "ada:mappingBeamMode": "missing"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "JEOL 8200 (stated as \"JEOL 8200 electron microprobe\"; no JXA prefix in paper)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Si",
      "Al",
      "K",
      "Na",
      "Ca",
      "Fe",
      "Mg",
      "Ti",
      "Cr",
      "Mn"
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
        "@id": "ada:targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "targetSpeciesEstimationMethod",
        "schema:name": "Target Species Estimation Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalAccuracy",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracy",
        "schema:name": "Analytical Accuracy",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalPrecision",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalPrecision",
        "schema:name": "Analytical Precision",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayBackgroundCorrectionMethod",
        "schema:name": "X-ray Background Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/beamCurrent",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "beamCurrent",
        "schema:name": "Beam Current",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/blankCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "blankCorrection",
        "schema:name": "Blank Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionStandard",
        "schema:name": "Interference Correction Standard",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayLineOverlapCorrectionsApplied",
        "schema:name": "X-ray Line Overlap Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferingElements",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingElements",
        "schema:name": "Interfering Elements",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "timeDependentIntensityCorrection",
        "schema:name": "Time-Dependent Intensity Correction",
        "ada:dataType": "string"
      }
    ]
  },
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/epmaTAPP/beamDamageMinimizationDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "beamDamageMinimizationDefault",
      "schema:name": "Beam Damage Minimization",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "all: low beam current (5 nA) \u2014 'Although a low beam current of 5 nA was used for the analysis, the low cation sum (0.92) for the K-site is likely due to diffusion of Na away from the electron beam' (p.3)"
    }
  ],
  "ada:edsAcquisitionMode": "N/A",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
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
          "schema:defaultValue": "SEM BSE imaging on a ZEISS 1550VP field-emission SEM \u2014 \"Backscattered electron (BSE) imaging was performed using a Carl Zeiss, LLC 1550VP field emission SEM\" (p.2), locating the three occurrences of the new mineral in the Zagami thin section (Fig. 1, p.2). The paper lists EPMA, SEM, EBSD, synchrotron XRD and micro-Raman as one suite (p.2) without stating the order"
        }
      ]
    }
  ],
  "ada:matrixCorrectionMethod": "CITZAF (Armstrong 1995)",
  "ada:secondaryReferenceMaterialDefault": [
    "feldspar standards \u2014 'based on analysis of feldspar standards as unknowns'; not named individually"
  ],
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "liebermannite",
      "lingunite",
      "maskelynite"
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
        "@id": "ada:targetMaterialColumn/epmaTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "Occurrence of the target phase \u2014 the units analysed are the observed occurrences of the new mineral: \"A first occurrence of liebermannite was observed with lingunite, silica, ilmenite, and baddeleyite ... (this is the type material). A second occurrence ... A third occurrence is shown in Fig. 1c, close to the type occurrence\" (p.4)",
  "ada:monitoredElements": [
    "Si, Al, K, Ca, Na, Fe, Mg, Ti, Cr, Mn \u2014 all determined. \"Standards for analysis were Asbestos microcline (SiKa, AlKa, KKa), synthetic anorthite (CaKa), Amelia albite (NaKa), synthetic fayalite (FeKa), synthetic forsterite (MgKa), synthetic TiO2 (TiKa), synthetic Cr2O3 (CrKa), and synthetic Mn-olivine (MnKa)\", with detection limits quoted for the same ten (p.2)"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "EPMA-WDS"
    }
  ],
  "schema:creator": {
    "schema:name": "Chi Ma",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Division of Geological and Planetary Sciences Analytical Facility, Caltech"
  },
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NSF EAR-0318518; NSF EAR-1322082; NSF DMR-0080065 \u2014 'SEM, EBSD, EPMA, and Raman measurements were carried out at the Geological and Planetary Science Division Analytical Facility at Caltech, which is supported in part by NSF grants EAR-0318518, EAR-1322082, and DMR-0080065'"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Ma et al. 2018, Meteorit. Planet. Sci. 53:50-61; doi:10.1111/maps.13000 (file dated 2017)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM (Carl Zeiss 1550VP FE-SEM, BSE imaging); EBSD; synchrotron XRD; micro-Raman"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Grain > Analysis point \u2014 Table 1 reports one column per occurrence (\"Type liebermannite\", \"The second liebermannite\", \"The third liebermannite\", \"Lingunite next to type liebermannite\" \u2026), each the mean of n = 2\u20136 points (p.3)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "acquisition",
      "schema:name": "Probe for EPMA (Probe Software, Inc.)"
    },
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "N \u2014 the 'CITZAF correction procedure' is recorded under Matrix Correction Method; the only software named is Probe for EPMA"
    }
  ],
  "ada:analyticalMode": [
    "WDS Point Analysis"
  ],
  "ada:reportedProperties": [
    "SiO2, TiO2, Al2O3, FeO, CaO, Na2O, K2O; cations per formula unit; density \u2014 oxide wt% with totals and 1 s.d. of the mean, cations on 8 oxygens (Table 1); 'Magnesium, Cr, and Mn were also analyzed but were below the detection limit in all cases'; calculated density 3.98 g cm-3 (p.3)"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished thin section USNM 7619 (coating type N)",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
        "ada:detectionLimitMethod": "test value ada:detectionLimitMethod"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "test value schema:defaultValue"
    }
  ],
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
  "schema:datePublished": "test value schema:datePublished"
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

<ex:epmaTAPP-Ma2017> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:detectionLimitMethod "test value ada:detectionLimitMethod" ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:description "Polished thin section USNM 7619 (coating type N)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDamageMinimizationDefault> ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Chi Ma" ] ;
    schema1:datePublished "test value schema:datePublished" ;
    schema1:description "Ma et al. 2018, Meteorit. Planet. Sci. 53:50-61 (file dated 2017) — liebermannite (KAlSi3O8) discovery from Zagami. Instrument stated as \"JEOL 8200 electron microprobe\" (no JXA prefix in text). WDS explicitly stated (\"WDS: 15 kV, 5 nA\"). Probe for EPMA; CITZAF correction (Armstrong 1995) — NOT PAP. Full standard suite and X-ray lines stated. K-mapping by EPMA also performed (used for mineral identification) but mapping conditions (step size, dwell time, current) not stated. Na diffusion observed during analysis despite low 5 nA beam current. Detection limits stated (per-element wt% values). Analytical accuracy: 1-2% for Si, Al, Ca, Na, K (feldspar standards as unknowns). Caltech GPS Division Analytical Facility. Reported detail: ada:edsAcquisitionMode = N/A — WDS procedure; ada:analyticalMode = WDS Point Analysis — 'WDS: 15 kV, 5 nA'; the paper also mentions 'K-mapping by EPMA', with no detector or conditions." ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NSF EAR-0318518; NSF EAR-1322082; NSF DMR-0080065 — 'SEM, EBSD, EPMA, and Raman measurements were carried out at the Geological and Planetary Science Division Analytical Facility at Caltech, which is supported in part by NSF grants EAR-0318518, EAR-1322082, and DMR-0080065'" ] ;
    schema1:instrument <ex:instrument/EPMA>,
        <ex:instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Division of Geological and Planetary Sciences Analytical Facility, Caltech" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "EPMA-WDS" ] ;
    schema1:name "EPMA-WDS Major Element Silicates/Glasses, Zagami (Caltech GPS Analytical Facility, JEOL 8200)" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SEM (Carl Zeiss 1550VP FE-SEM, BSE imaging); EBSD; synchrotron XRD; micro-Raman" ] ;
            schema1:url "https://ada.astromat.org/missing" ],
        [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Ma et al. 2018, Meteorit. Planet. Sci. 53:50-61; doi:10.1111/maps.13000 (file dated 2017)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "test value schema:defaultValue" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analyticalMode "WDS Point Analysis" ;
    ada:edsAcquisitionMode "N/A" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "CITZAF (Armstrong 1995)" ;
    ada:monitoredElements "Si, Al, K, Ca, Na, Fe, Mg, Ti, Cr, Mn — all determined. \"Standards for analysis were Asbestos microcline (SiKa, AlKa, KKa), synthetic anorthite (CaKa), Amelia albite (NaKa), synthetic fayalite (FeKa), synthetic forsterite (MgKa), synthetic TiO2 (TiKa), synthetic Cr2O3 (CrKa), and synthetic Mn-olivine (MnKa)\", with detection limits quoted for the same ten (p.2)" ;
    ada:reportedProperties "SiO2, TiO2, Al2O3, FeO, CaO, Na2O, K2O; cations per formula unit; density — oxide wt% with totals and 1 s.d. of the mean, cations on 8 oxygens (Table 1); 'Magnesium, Cr, and Mn were also analyzed but were below the detection limit in all cases'; calculated density 3.98 g cm-3 (p.3)" ;
    ada:samplingUnitSelectionCriteriaDefault "Occurrence of the target phase — the units analysed are the observed occurrences of the new mineral: \"A first occurrence of liebermannite was observed with lingunite, silica, ilmenite, and baddeleyite ... (this is the type material). A second occurrence ... A third occurrence is shown in Fig. 1c, close to the type occurrence\" (p.4)" ;
    ada:samplingUnitType "Grain > Analysis point — Table 1 reports one column per occurrence (\"Type liebermannite\", \"The second liebermannite\", \"The third liebermannite\", \"Lingunite next to type liebermannite\" …), each the mean of n = 2–6 points (p.3)" ;
    ada:secondaryReferenceMaterialDefault "feldspar standards — 'based on analysis of feldspar standards as unknowns'; not named individually" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "liebermannite",
                "lingunite",
                "maskelynite" ;
            ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/backgroundCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/peakCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName> ] ;
    ada:targetSpeciesTemplate [ ada:defaultTargetSpecies "Al",
                "Ca",
                "Cr",
                "Fe",
                "K",
                "Mg",
                "Mn",
                "Na",
                "Si",
                "Ti" ;
            ada:targetSpeciesColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetSpecies" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalAccuracy>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalPrecision>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/beamCurrent>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/blankCorrection>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferingElements>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied> ] ;
    ada:wdsDeadTimeCorrection "missing" ;
    bios:computationalTool [ schema1:name "Probe for EPMA (Probe Software, Inc.)" ;
            ada:toolRole "acquisition" ],
        [ schema1:name "N — the 'CITZAF correction procedure' is recorded under Matrix Correction Method; the only software named is Probe for EPMA" ;
            ada:toolRole "dataReduction" ] .

<ex:instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:hasPart <ex:instrument/EPMA/part/EDS-Detector>,
        <ex:instrument/EPMA/part/Electron-Source>,
        <ex:instrument/EPMA/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "JEOL" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "15 kV" ;
    ada:beamDiameterDefault "N — 'beam in focused mode' is recorded under Beam Mode; no diameter is given" ;
    ada:beamMode "all: Focused — 'WDS: 15 kV, 5 nA, beam in focused mode' (p.2)" ;
    ada:mappingBeamCurrentDefault -9999 ;
    ada:mappingBeamDiameterDefault -9999 ;
    ada:mappingBeamMode "missing" .

<ex:instrument/EPMA/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:name "missing" .

<ex:instrument/EPMA/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "missing" ;
    schema1:name "missing" .

<ex:instrument/EPMA/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "missing" .

<ex:instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "JEOL 8200 (stated as \"JEOL 8200 electron microprobe\"; no JXA prefix in paper)" ] ;
    schema1:name "example instrumentName" .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDamageMinimizationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "all: low beam current (5 nA) — 'Although a low beam current of 5 nA was used for the analysis, the low cation sum (0.92) for the K-site is likely due to diffusion of Na away from the electron beam' (p.3)" ;
    schema1:name "Beam Damage Minimization" ;
    schema1:valueName "beamDamageMinimizationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "SEM BSE imaging on a ZEISS 1550VP field-emission SEM — \"Backscattered electron (BSE) imaging was performed using a Carl Zeiss, LLC 1550VP field emission SEM\" (p.2), locating the three occurrences of the new mineral in the Zagami thin section (Fig. 1, p.2). The paper lists EPMA, SEM, EBSD, synchrotron XRD and micro-Raman as one suite (p.2) without stating the order" ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:valueName "preAnalysisImagingAndScreeningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/backgroundCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Background Counting Time" ;
    schema1:valueName "backgroundCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/peakCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Peak Counting Time" ;
    schema1:valueName "peakCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalAccuracy> a schema1:PropertyValueSpecification ;
    schema1:name "Analytical Accuracy" ;
    schema1:valueName "analyticalAccuracy" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalPrecision> a schema1:PropertyValueSpecification ;
    schema1:name "Analytical Precision" ;
    schema1:valueName "analyticalPrecision" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/beamCurrent> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Beam Current" ;
    schema1:valueName "beamCurrent" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/blankCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Blank Correction" ;
    schema1:valueName "blankCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard> a schema1:PropertyValueSpecification ;
    schema1:name "Interference Correction Standard" ;
    schema1:valueName "interferenceCorrectionStandard" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferingElements> a schema1:PropertyValueSpecification ;
    schema1:name "Interfering Elements" ;
    schema1:valueName "interferingElements" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Target Species Estimation Method" ;
    schema1:valueName "targetSpeciesEstimationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Time-Dependent Intensity Correction" ;
    schema1:valueName "timeDependentIntensityCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "X-ray Background Correction Method" ;
    schema1:valueName "xRayBackgroundCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "X-ray Line Overlap Corrections Applied" ;
    schema1:valueName "xRayLineOverlapCorrectionsApplied" ;
    ada:dataType "string" .


```


### epmaTAPP example Frank2023
epmaTAPP instance derived from Frank+2023 | Cameca SX100 | WDS Point Analysis (ARES JSC).
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
  "@id": "ex:epmaTAPP-Frank2023",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA Major/Minor Element Silicates+Oxides+Sulfides, CI Chondrite (ARES JSC, Cameca SX100)",
  "schema:description": "Frank et al. 2023, Meteorit. Planet. Sci. 58:1495-1511 — CAI in Ivuna CI chondrite. ARES NASA JSC. Instrument stated as \"Cameca SX100 electron microprobe at ARES, Johnson Space Center\" — NOT JEOL JXA-8530F as in v2 header. Accelerating voltage 20 kV (not 15 kV). Both point analysis (20 kV, 20 nA, 1 µm focused) and X-ray mapping performed. X-ray mapping described but conditions (step size, dwell time, mapping beam mode) N. WDS not explicitly stated. Matrix correction and background correction method N. Peak counting time 10-50 s. Primary standard suite fully documented. No EPMA secondary standard is named (San Carlos olivine standardised the SIMS work). Detection limits stated per element group. Reported detail: ada:edsAcquisitionMode = N — WDS or EDS is not stated; ada:analyticalMode = N — point analyses and X-ray mapping ('electron microprobe, and X-ray mapping'); WDS or EDS is not stated, and the list has no value without one.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "20 kV",
      "ada:beamDiameterDefault": "all: 1 µm — p.3",
      "ada:beamMode": "all: Focused — 'Analyses were performed at 20 kV and 20 nA using a focused beam of 1 μm' (p.3)",
      "schema:manufacturer": {
        "schema:name": "Cameca",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        }
      ],
      "schema:name": "example instrumentName",
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:mappingBeamDiameterDefault": -9999,
      "ada:mappingBeamMode": "missing"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "SX100 (stated as \"Cameca SX100\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Si",
      "Al",
      "Ti",
      "K",
      "Na",
      "Fe",
      "Mg",
      "Ca",
      "S",
      "Mn",
      "Cr",
      "Ni",
      "P",
      "V"
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
        "@id": "ada:targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "targetSpeciesEstimationMethod",
        "schema:name": "Target Species Estimation Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalAccuracy",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracy",
        "schema:name": "Analytical Accuracy",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalPrecision",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalPrecision",
        "schema:name": "Analytical Precision",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayBackgroundCorrectionMethod",
        "schema:name": "X-ray Background Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/beamCurrent",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "beamCurrent",
        "schema:name": "Beam Current",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/blankCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "blankCorrection",
        "schema:name": "Blank Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionStandard",
        "schema:name": "Interference Correction Standard",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayLineOverlapCorrectionsApplied",
        "schema:name": "X-ray Line Overlap Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferingElements",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingElements",
        "schema:name": "Interfering Elements",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "timeDependentIntensityCorrection",
        "schema:name": "Time-Dependent Intensity Correction",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:edsAcquisitionMode": "N/A",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
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
          "schema:defaultValue": "Petrographic microscopy and SEM — \"The CAI was characterized by petrographic microscope, scanning electron microscope, electron microprobe, and X-ray mapping before being measured for oxygen isotopes\" (p.3); the object itself had been found during an earlier survey of matrix compositions (p.3)"
        }
      ]
    }
  ],
  "ada:secondaryReferenceMaterialDefault": [
    "N — no EPMA secondary standard is named; San Carlos olivine standardised the SIMS oxygen-isotope measurements, and Kakanui kaersutite is a primary standard"
  ],
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "melilite",
      "spinel",
      "grossmanite"
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
        "@id": "ada:targetMaterialColumn/epmaTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "Opportunistic — the object analysed \"was found by David Frank in Ivuna section MZ2 during a study of the minor-element compositions of matrix olivine and pyroxene in types 1, 2, and 3 chondrites\" (p.3); no rule was applied to choose it, and it is the section's only CAI",
  "ada:monitoredElements": [
    "Si, Al, Ti, K, Na, Fe, Mg, Ca, S, Mn, Cr, Ni, P, V — all determined. \"Standards were Kakanui kaersutite for silicon, aluminum, titanium, potassium, sodium, iron, magnesium, and calcium, Canyon Diablo troilite for sulfur, rhodonite for manganese, chromium metal for chromium, nickel metal for nickel, apatite for phosphorus, and vanadium metal for vanadium\" (pp.3–4)"
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "ARES, NASA Johnson Space Center"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Frank et al. 2023, Meteorit. Planet. Sci. 58:1495-1511; doi:10.1111/maps.14083"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Petrographic microscopy; SEM-BSE (JEOL 5900LV); EPMA X-ray mapping; Cameca ims1280 ion microprobe (O isotopes; 26Al-26Mg); FIB-TEM"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Phase > Analysis point — \"Representative electron-microprobe measurements of melilite, grossmanite, and spinel are given in Table 1\" (p.5), all within the single Ivuna CAI",
  "ada:reportedProperties": [
    "SO2, P2O5, Na2O, K2O, MgO, Al2O3, SiO2, CaO, TiO2, V2O3, FeO, Cr2O3, MnO, NiO; åkermanite content — oxide wt% with totals (Table 1); Åk14–31 (p.5)"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "epma",
      "schema:termCode": "epma"
    }
  ],
  "schema:actionProcess": {
    "@type": [
      "schema:HowTo"
    ],
    "schema:name": "missing",
    "schema:step": [
      {
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:name": "Sample preparation",
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 1,
        "schema:description": "test value schema:description"
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:name": "Data reduction",
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
        "ada:detectionLimitMethod": "test value ada:detectionLimitMethod"
      }
    ]
  },
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "test value schema:defaultValue"
    }
  ],
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
  "schema:datePublished": "test value schema:datePublished"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:epmaTAPP-Frank2023",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA Major/Minor Element Silicates+Oxides+Sulfides, CI Chondrite (ARES JSC, Cameca SX100)",
  "schema:description": "Frank et al. 2023, Meteorit. Planet. Sci. 58:1495-1511 \u2014 CAI in Ivuna CI chondrite. ARES NASA JSC. Instrument stated as \"Cameca SX100 electron microprobe at ARES, Johnson Space Center\" \u2014 NOT JEOL JXA-8530F as in v2 header. Accelerating voltage 20 kV (not 15 kV). Both point analysis (20 kV, 20 nA, 1 \u00b5m focused) and X-ray mapping performed. X-ray mapping described but conditions (step size, dwell time, mapping beam mode) N. WDS not explicitly stated. Matrix correction and background correction method N. Peak counting time 10-50 s. Primary standard suite fully documented. No EPMA secondary standard is named (San Carlos olivine standardised the SIMS work). Detection limits stated per element group. Reported detail: ada:edsAcquisitionMode = N \u2014 WDS or EDS is not stated; ada:analyticalMode = N \u2014 point analyses and X-ray mapping ('electron microprobe, and X-ray mapping'); WDS or EDS is not stated, and the list has no value without one.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "20 kV",
      "ada:beamDiameterDefault": "all: 1 \u00b5m \u2014 p.3",
      "ada:beamMode": "all: Focused \u2014 'Analyses were performed at 20 kV and 20 nA using a focused beam of 1 \u03bcm' (p.3)",
      "schema:manufacturer": {
        "schema:name": "Cameca",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        }
      ],
      "schema:name": "example instrumentName",
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:mappingBeamDiameterDefault": -9999,
      "ada:mappingBeamMode": "missing"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "SX100 (stated as \"Cameca SX100\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Si",
      "Al",
      "Ti",
      "K",
      "Na",
      "Fe",
      "Mg",
      "Ca",
      "S",
      "Mn",
      "Cr",
      "Ni",
      "P",
      "V"
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
        "@id": "ada:targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "targetSpeciesEstimationMethod",
        "schema:name": "Target Species Estimation Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalAccuracy",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracy",
        "schema:name": "Analytical Accuracy",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalPrecision",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalPrecision",
        "schema:name": "Analytical Precision",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayBackgroundCorrectionMethod",
        "schema:name": "X-ray Background Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/beamCurrent",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "beamCurrent",
        "schema:name": "Beam Current",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/blankCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "blankCorrection",
        "schema:name": "Blank Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionStandard",
        "schema:name": "Interference Correction Standard",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayLineOverlapCorrectionsApplied",
        "schema:name": "X-ray Line Overlap Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferingElements",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingElements",
        "schema:name": "Interfering Elements",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "timeDependentIntensityCorrection",
        "schema:name": "Time-Dependent Intensity Correction",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:edsAcquisitionMode": "N/A",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
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
          "schema:defaultValue": "Petrographic microscopy and SEM \u2014 \"The CAI was characterized by petrographic microscope, scanning electron microscope, electron microprobe, and X-ray mapping before being measured for oxygen isotopes\" (p.3); the object itself had been found during an earlier survey of matrix compositions (p.3)"
        }
      ]
    }
  ],
  "ada:secondaryReferenceMaterialDefault": [
    "N \u2014 no EPMA secondary standard is named; San Carlos olivine standardised the SIMS oxygen-isotope measurements, and Kakanui kaersutite is a primary standard"
  ],
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "melilite",
      "spinel",
      "grossmanite"
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
        "@id": "ada:targetMaterialColumn/epmaTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "Opportunistic \u2014 the object analysed \"was found by David Frank in Ivuna section MZ2 during a study of the minor-element compositions of matrix olivine and pyroxene in types 1, 2, and 3 chondrites\" (p.3); no rule was applied to choose it, and it is the section's only CAI",
  "ada:monitoredElements": [
    "Si, Al, Ti, K, Na, Fe, Mg, Ca, S, Mn, Cr, Ni, P, V \u2014 all determined. \"Standards were Kakanui kaersutite for silicon, aluminum, titanium, potassium, sodium, iron, magnesium, and calcium, Canyon Diablo troilite for sulfur, rhodonite for manganese, chromium metal for chromium, nickel metal for nickel, apatite for phosphorus, and vanadium metal for vanadium\" (pp.3\u20134)"
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "ARES, NASA Johnson Space Center"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Frank et al. 2023, Meteorit. Planet. Sci. 58:1495-1511; doi:10.1111/maps.14083"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Petrographic microscopy; SEM-BSE (JEOL 5900LV); EPMA X-ray mapping; Cameca ims1280 ion microprobe (O isotopes; 26Al-26Mg); FIB-TEM"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Phase > Analysis point \u2014 \"Representative electron-microprobe measurements of melilite, grossmanite, and spinel are given in Table 1\" (p.5), all within the single Ivuna CAI",
  "ada:reportedProperties": [
    "SO2, P2O5, Na2O, K2O, MgO, Al2O3, SiO2, CaO, TiO2, V2O3, FeO, Cr2O3, MnO, NiO; \u00e5kermanite content \u2014 oxide wt% with totals (Table 1); \u00c5k14\u201331 (p.5)"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "epma",
      "schema:termCode": "epma"
    }
  ],
  "schema:actionProcess": {
    "@type": [
      "schema:HowTo"
    ],
    "schema:name": "missing",
    "schema:step": [
      {
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:name": "Sample preparation",
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 1,
        "schema:description": "test value schema:description"
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:name": "Data reduction",
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
        "ada:detectionLimitMethod": "test value ada:detectionLimitMethod"
      }
    ]
  },
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "test value schema:defaultValue"
    }
  ],
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
  "schema:datePublished": "test value schema:datePublished"
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

<ex:epmaTAPP-Frank2023> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:name "missing" ;
            schema1:step [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:detectionLimitMethod "test value ada:detectionLimitMethod" ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:description "test value schema:description" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:datePublished "test value schema:datePublished" ;
    schema1:description "Frank et al. 2023, Meteorit. Planet. Sci. 58:1495-1511 — CAI in Ivuna CI chondrite. ARES NASA JSC. Instrument stated as \"Cameca SX100 electron microprobe at ARES, Johnson Space Center\" — NOT JEOL JXA-8530F as in v2 header. Accelerating voltage 20 kV (not 15 kV). Both point analysis (20 kV, 20 nA, 1 µm focused) and X-ray mapping performed. X-ray mapping described but conditions (step size, dwell time, mapping beam mode) N. WDS not explicitly stated. Matrix correction and background correction method N. Peak counting time 10-50 s. Primary standard suite fully documented. No EPMA secondary standard is named (San Carlos olivine standardised the SIMS work). Detection limits stated per element group. Reported detail: ada:edsAcquisitionMode = N — WDS or EDS is not stated; ada:analyticalMode = N — point analyses and X-ray mapping ('electron microprobe, and X-ray mapping'); WDS or EDS is not stated, and the list has no value without one." ;
    schema1:instrument <ex:instrument/EPMA>,
        <ex:instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "ARES, NASA Johnson Space Center" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "epma" ;
            schema1:termCode "epma" ] ;
    schema1:name "EPMA Major/Minor Element Silicates+Oxides+Sulfides, CI Chondrite (ARES JSC, Cameca SX100)" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "Petrographic microscopy; SEM-BSE (JEOL 5900LV); EPMA X-ray mapping; Cameca ims1280 ion microprobe (O isotopes; 26Al-26Mg); FIB-TEM" ] ;
            schema1:url "https://ada.astromat.org/missing" ],
        [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Frank et al. 2023, Meteorit. Planet. Sci. 58:1495-1511; doi:10.1111/maps.14083" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "test value schema:defaultValue" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:edsAcquisitionMode "N/A" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:monitoredElements "Si, Al, Ti, K, Na, Fe, Mg, Ca, S, Mn, Cr, Ni, P, V — all determined. \"Standards were Kakanui kaersutite for silicon, aluminum, titanium, potassium, sodium, iron, magnesium, and calcium, Canyon Diablo troilite for sulfur, rhodonite for manganese, chromium metal for chromium, nickel metal for nickel, apatite for phosphorus, and vanadium metal for vanadium\" (pp.3–4)" ;
    ada:reportedProperties "SO2, P2O5, Na2O, K2O, MgO, Al2O3, SiO2, CaO, TiO2, V2O3, FeO, Cr2O3, MnO, NiO; åkermanite content — oxide wt% with totals (Table 1); Åk14–31 (p.5)" ;
    ada:samplingUnitSelectionCriteriaDefault "Opportunistic — the object analysed \"was found by David Frank in Ivuna section MZ2 during a study of the minor-element compositions of matrix olivine and pyroxene in types 1, 2, and 3 chondrites\" (p.3); no rule was applied to choose it, and it is the section's only CAI" ;
    ada:samplingUnitType "Phase > Analysis point — \"Representative electron-microprobe measurements of melilite, grossmanite, and spinel are given in Table 1\" (p.5), all within the single Ivuna CAI" ;
    ada:secondaryReferenceMaterialDefault "N — no EPMA secondary standard is named; San Carlos olivine standardised the SIMS oxygen-isotope measurements, and Kakanui kaersutite is a primary standard" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "grossmanite",
                "melilite",
                "spinel" ;
            ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/backgroundCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/peakCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName> ] ;
    ada:targetSpeciesTemplate [ ada:defaultTargetSpecies "Al",
                "Ca",
                "Cr",
                "Fe",
                "K",
                "Mg",
                "Mn",
                "Na",
                "Ni",
                "P",
                "S",
                "Si",
                "Ti",
                "V" ;
            ada:targetSpeciesColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetSpecies" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalAccuracy>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalPrecision>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/beamCurrent>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/blankCorrection>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferingElements>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied> ] ;
    ada:wdsDeadTimeCorrection "missing" .

<ex:instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:hasPart <ex:instrument/EPMA/part/EDS-Detector>,
        <ex:instrument/EPMA/part/Electron-Source>,
        <ex:instrument/EPMA/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Cameca" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "20 kV" ;
    ada:beamDiameterDefault "all: 1 µm — p.3" ;
    ada:beamMode "all: Focused — 'Analyses were performed at 20 kV and 20 nA using a focused beam of 1 μm' (p.3)" ;
    ada:mappingBeamCurrentDefault -9999 ;
    ada:mappingBeamDiameterDefault -9999 ;
    ada:mappingBeamMode "missing" .

<ex:instrument/EPMA/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:name "missing" .

<ex:instrument/EPMA/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "missing" ;
    schema1:name "missing" .

<ex:instrument/EPMA/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "missing" .

<ex:instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "SX100 (stated as \"Cameca SX100\")" ] ;
    schema1:name "example instrumentName" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Petrographic microscopy and SEM — \"The CAI was characterized by petrographic microscope, scanning electron microscope, electron microprobe, and X-ray mapping before being measured for oxygen isotopes\" (p.3); the object itself had been found during an earlier survey of matrix compositions (p.3)" ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:valueName "preAnalysisImagingAndScreeningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/backgroundCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Background Counting Time" ;
    schema1:valueName "backgroundCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/peakCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Peak Counting Time" ;
    schema1:valueName "peakCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalAccuracy> a schema1:PropertyValueSpecification ;
    schema1:name "Analytical Accuracy" ;
    schema1:valueName "analyticalAccuracy" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalPrecision> a schema1:PropertyValueSpecification ;
    schema1:name "Analytical Precision" ;
    schema1:valueName "analyticalPrecision" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/beamCurrent> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Beam Current" ;
    schema1:valueName "beamCurrent" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/blankCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Blank Correction" ;
    schema1:valueName "blankCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard> a schema1:PropertyValueSpecification ;
    schema1:name "Interference Correction Standard" ;
    schema1:valueName "interferenceCorrectionStandard" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferingElements> a schema1:PropertyValueSpecification ;
    schema1:name "Interfering Elements" ;
    schema1:valueName "interferingElements" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Target Species Estimation Method" ;
    schema1:valueName "targetSpeciesEstimationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Time-Dependent Intensity Correction" ;
    schema1:valueName "timeDependentIntensityCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "X-ray Background Correction Method" ;
    schema1:valueName "xRayBackgroundCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "X-ray Line Overlap Corrections Applied" ;
    schema1:valueName "xRayLineOverlapCorrectionsApplied" ;
    ada:dataType "string" .


```


### epmaTAPP example Broussard2026
epmaTAPP instance derived from Broussard+2026 | JEOL JXA-8200 | WDS Mapping (WashU).
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
  "@id": "ex:epmaTAPP-Broussard2026",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS Quantitative Mapping+Analysis, CI Chondrite Minerals (WashU, JEOL JXA-8200)",
  "schema:description": "Broussard et al. 2026, Meteorit. Planet. Sci. — OC002 CI chondrite links Bennu and Ryugu. Washington University in St. Louis. Instrument stated as \"JEOL JXA-8200 electron microprobe\" — NOT JXA-8230 as in v2 header. WDS explicitly stated (\"wavelength-dispersive quantitative compositional mapping and analysis\"). CITZAF matrix correction (Armstrong 1995) — NOT PAP or XPP. MAN background for most analytes; polynomial fit for F via LDE1 crystal. Both point analysis (15 kV, 25 nA) and quantitative stage mapping performed. O by stoichiometry from cations. F is the only explicitly named analyte in methods; full list N. An EDS spectrometer is on the instrument; its use is not stated. Smithsonian Microbeam standards as secondary QC. No peak counting time, beam diameter, detection limits, or interference corrections stated. Reported detail: ada:edsAcquisitionMode = N/A — WDS procedure; ada:analyticalMode = WDS Point Analysis; WDS Mapping — 'wavelength-dispersive quantitative compositional mapping and analysis'.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "5 wavelength-dispersive spectrometers (JEOL)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:name": "example instrumentName",
      "ada:beamDiameterDefault": -9999,
      "ada:beamMode": "missing",
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:mappingBeamDiameterDefault": -9999,
      "ada:mappingBeamMode": "missing"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "JXA-8200 (stated as \"JEOL JXA-8200 electron microprobe\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "F",
      "O",
      "CO2",
      "H2O"
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
        "@id": "ada:targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "targetSpeciesEstimationMethod",
        "schema:name": "Target Species Estimation Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalAccuracy",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracy",
        "schema:name": "Analytical Accuracy",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalPrecision",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalPrecision",
        "schema:name": "Analytical Precision",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayBackgroundCorrectionMethod",
        "schema:name": "X-ray Background Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/beamCurrent",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "beamCurrent",
        "schema:name": "Beam Current",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/blankCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "blankCorrection",
        "schema:name": "Blank Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionStandard",
        "schema:name": "Interference Correction Standard",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayLineOverlapCorrectionsApplied",
        "schema:name": "X-ray Line Overlap Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferingElements",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingElements",
        "schema:name": "Interfering Elements",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "timeDependentIntensityCorrection",
        "schema:name": "Time-Dependent Intensity Correction",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:edsAcquisitionMode": "N/A",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
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
          "schema:defaultValue": "Optical microscopy of the same thin section — \"Eleven OC002 LAB24-2 fragments were mounted and dry-polished in a petrographic thin section used for optical microscopy and electron probe microanalyses\" (p.3)"
        }
      ]
    }
  ],
  "ada:matrixCorrectionMethod": "CITZAF (Armstrong 1995)",
  "ada:secondaryReferenceMaterialDefault": [
    "Smithsonian Microbeam standards (specific materials and values N)"
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/epmaTAPP/stageScanVsBeamScan",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/epmaTAPP/stageScanVsBeamScan"
        }
      ],
      "schema:name": "Stage Scan vs. Beam Scan",
      "schema:value": "Stage scan"
    }
  ],
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "phyllosilicate",
      "oxide",
      "sulfide",
      "carbonate",
      "phosphate"
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
        "@id": "ada:targetMaterialColumn/epmaTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "N — the paper names the phases it analysed (see `Sampling Unit Type`) but states no rule for choosing the individual units",
  "ada:monitoredElements": [
    "F — 'Fluorine measurement was made using the LDE1 diffracting crystal'; no other element is named"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "EPMA-WDS"
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
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Broussard et al. 2026, Meteorit. Planet. Sci.; doi:10.1111/maps.70138"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Powder XRD (Rigaku MiniFlex 600); ICP-MS (Thermo Fisher iCAP Qc, WashU); K isotope MC-ICP-MS (Neptune Plus, WashU); CO2 laser-fluorination O isotope MS (U. New Mexico); AMS (PRIME Lab, Purdue)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Region of interest > Phase — \"wavelength-dispersive quantitative compositional mapping and analysis\" (p.3) of whole fragments; phases are identified within a map (\"Round Phy1 phyllosilicate clast\", \"Lithic clast (LC1)\", Fig. 3, p.6) and abundances given per section (\"sulfides which make up 2.3 areal% of the section\", p.6)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "acquisition",
      "schema:name": "Probe for EPMA microanalysis software"
    },
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Probe for EPMA (CITZAF matrix correction, Armstrong 1995); CalcImage and Quantitative Microanalysis Explorer web-based tool (for stage mapping)"
    }
  ],
  "ada:analyticalMode": [
    "WDS Point Analysis"
  ],
  "ada:reportedProperties": [
    "Element concentrations in the carbonates (wt%: Fe, Mn — \"Dolomite contains 2.0 ± 0.4 wt% Fe and 3.0 ± 0.9 wt% Mn (n = 37)\", p.5); phase abundance as areal fraction of the section (areal%, e.g. sulfides \"2.3 areal%\", p.6); phase identifications from the X-ray maps (nominal)"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Fragments mounted and dry-polished in a petrographic thin section; carbon coating N",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
        "ada:detectionLimitMethod": "test value ada:detectionLimitMethod"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "test value schema:defaultValue"
    }
  ],
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
  "schema:datePublished": "test value schema:datePublished"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:epmaTAPP-Broussard2026",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS Quantitative Mapping+Analysis, CI Chondrite Minerals (WashU, JEOL JXA-8200)",
  "schema:description": "Broussard et al. 2026, Meteorit. Planet. Sci. \u2014 OC002 CI chondrite links Bennu and Ryugu. Washington University in St. Louis. Instrument stated as \"JEOL JXA-8200 electron microprobe\" \u2014 NOT JXA-8230 as in v2 header. WDS explicitly stated (\"wavelength-dispersive quantitative compositional mapping and analysis\"). CITZAF matrix correction (Armstrong 1995) \u2014 NOT PAP or XPP. MAN background for most analytes; polynomial fit for F via LDE1 crystal. Both point analysis (15 kV, 25 nA) and quantitative stage mapping performed. O by stoichiometry from cations. F is the only explicitly named analyte in methods; full list N. An EDS spectrometer is on the instrument; its use is not stated. Smithsonian Microbeam standards as secondary QC. No peak counting time, beam diameter, detection limits, or interference corrections stated. Reported detail: ada:edsAcquisitionMode = N/A \u2014 WDS procedure; ada:analyticalMode = WDS Point Analysis; WDS Mapping \u2014 'wavelength-dispersive quantitative compositional mapping and analysis'.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "5 wavelength-dispersive spectrometers (JEOL)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:name": "example instrumentName",
      "ada:beamDiameterDefault": -9999,
      "ada:beamMode": "missing",
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:mappingBeamDiameterDefault": -9999,
      "ada:mappingBeamMode": "missing"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "JXA-8200 (stated as \"JEOL JXA-8200 electron microprobe\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "F",
      "O",
      "CO2",
      "H2O"
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
        "@id": "ada:targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "targetSpeciesEstimationMethod",
        "schema:name": "Target Species Estimation Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalAccuracy",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracy",
        "schema:name": "Analytical Accuracy",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalPrecision",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalPrecision",
        "schema:name": "Analytical Precision",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayBackgroundCorrectionMethod",
        "schema:name": "X-ray Background Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/beamCurrent",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "beamCurrent",
        "schema:name": "Beam Current",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/blankCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "blankCorrection",
        "schema:name": "Blank Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionStandard",
        "schema:name": "Interference Correction Standard",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayLineOverlapCorrectionsApplied",
        "schema:name": "X-ray Line Overlap Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferingElements",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingElements",
        "schema:name": "Interfering Elements",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "timeDependentIntensityCorrection",
        "schema:name": "Time-Dependent Intensity Correction",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:edsAcquisitionMode": "N/A",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
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
          "schema:defaultValue": "Optical microscopy of the same thin section \u2014 \"Eleven OC002 LAB24-2 fragments were mounted and dry-polished in a petrographic thin section used for optical microscopy and electron probe microanalyses\" (p.3)"
        }
      ]
    }
  ],
  "ada:matrixCorrectionMethod": "CITZAF (Armstrong 1995)",
  "ada:secondaryReferenceMaterialDefault": [
    "Smithsonian Microbeam standards (specific materials and values N)"
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/epmaTAPP/stageScanVsBeamScan",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/epmaTAPP/stageScanVsBeamScan"
        }
      ],
      "schema:name": "Stage Scan vs. Beam Scan",
      "schema:value": "Stage scan"
    }
  ],
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "phyllosilicate",
      "oxide",
      "sulfide",
      "carbonate",
      "phosphate"
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
        "@id": "ada:targetMaterialColumn/epmaTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "N \u2014 the paper names the phases it analysed (see `Sampling Unit Type`) but states no rule for choosing the individual units",
  "ada:monitoredElements": [
    "F \u2014 'Fluorine measurement was made using the LDE1 diffracting crystal'; no other element is named"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "EPMA-WDS"
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
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Broussard et al. 2026, Meteorit. Planet. Sci.; doi:10.1111/maps.70138"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Powder XRD (Rigaku MiniFlex 600); ICP-MS (Thermo Fisher iCAP Qc, WashU); K isotope MC-ICP-MS (Neptune Plus, WashU); CO2 laser-fluorination O isotope MS (U. New Mexico); AMS (PRIME Lab, Purdue)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Region of interest > Phase \u2014 \"wavelength-dispersive quantitative compositional mapping and analysis\" (p.3) of whole fragments; phases are identified within a map (\"Round Phy1 phyllosilicate clast\", \"Lithic clast (LC1)\", Fig. 3, p.6) and abundances given per section (\"sulfides which make up 2.3 areal% of the section\", p.6)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "acquisition",
      "schema:name": "Probe for EPMA microanalysis software"
    },
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Probe for EPMA (CITZAF matrix correction, Armstrong 1995); CalcImage and Quantitative Microanalysis Explorer web-based tool (for stage mapping)"
    }
  ],
  "ada:analyticalMode": [
    "WDS Point Analysis"
  ],
  "ada:reportedProperties": [
    "Element concentrations in the carbonates (wt%: Fe, Mn \u2014 \"Dolomite contains 2.0 \u00b1 0.4 wt% Fe and 3.0 \u00b1 0.9 wt% Mn (n = 37)\", p.5); phase abundance as areal fraction of the section (areal%, e.g. sulfides \"2.3 areal%\", p.6); phase identifications from the X-ray maps (nominal)"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Fragments mounted and dry-polished in a petrographic thin section; carbon coating N",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
        "ada:detectionLimitMethod": "test value ada:detectionLimitMethod"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "test value schema:defaultValue"
    }
  ],
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
  "schema:datePublished": "test value schema:datePublished"
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

<ex:epmaTAPP-Broussard2026> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:detectionLimitMethod "test value ada:detectionLimitMethod" ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:description "Fragments mounted and dry-polished in a petrographic thin section; carbon coating N" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/epmaTAPP/stageScanVsBeamScan> ;
    schema1:datePublished "test value schema:datePublished" ;
    schema1:description "Broussard et al. 2026, Meteorit. Planet. Sci. — OC002 CI chondrite links Bennu and Ryugu. Washington University in St. Louis. Instrument stated as \"JEOL JXA-8200 electron microprobe\" — NOT JXA-8230 as in v2 header. WDS explicitly stated (\"wavelength-dispersive quantitative compositional mapping and analysis\"). CITZAF matrix correction (Armstrong 1995) — NOT PAP or XPP. MAN background for most analytes; polynomial fit for F via LDE1 crystal. Both point analysis (15 kV, 25 nA) and quantitative stage mapping performed. O by stoichiometry from cations. F is the only explicitly named analyte in methods; full list N. An EDS spectrometer is on the instrument; its use is not stated. Smithsonian Microbeam standards as secondary QC. No peak counting time, beam diameter, detection limits, or interference corrections stated. Reported detail: ada:edsAcquisitionMode = N/A — WDS procedure; ada:analyticalMode = WDS Point Analysis; WDS Mapping — 'wavelength-dispersive quantitative compositional mapping and analysis'." ;
    schema1:instrument <ex:instrument/EPMA>,
        <ex:instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Washington University in St. Louis" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "EPMA-WDS" ] ;
    schema1:name "EPMA-WDS Quantitative Mapping+Analysis, CI Chondrite Minerals (WashU, JEOL JXA-8200)" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "Powder XRD (Rigaku MiniFlex 600); ICP-MS (Thermo Fisher iCAP Qc, WashU); K isotope MC-ICP-MS (Neptune Plus, WashU); CO2 laser-fluorination O isotope MS (U. New Mexico); AMS (PRIME Lab, Purdue)" ] ;
            schema1:url "https://ada.astromat.org/missing" ],
        [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Broussard et al. 2026, Meteorit. Planet. Sci.; doi:10.1111/maps.70138" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "test value schema:defaultValue" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analyticalMode "WDS Point Analysis" ;
    ada:edsAcquisitionMode "N/A" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "CITZAF (Armstrong 1995)" ;
    ada:monitoredElements "F — 'Fluorine measurement was made using the LDE1 diffracting crystal'; no other element is named" ;
    ada:reportedProperties "Element concentrations in the carbonates (wt%: Fe, Mn — \"Dolomite contains 2.0 ± 0.4 wt% Fe and 3.0 ± 0.9 wt% Mn (n = 37)\", p.5); phase abundance as areal fraction of the section (areal%, e.g. sulfides \"2.3 areal%\", p.6); phase identifications from the X-ray maps (nominal)" ;
    ada:samplingUnitSelectionCriteriaDefault "N — the paper names the phases it analysed (see `Sampling Unit Type`) but states no rule for choosing the individual units" ;
    ada:samplingUnitType "Region of interest > Phase — \"wavelength-dispersive quantitative compositional mapping and analysis\" (p.3) of whole fragments; phases are identified within a map (\"Round Phy1 phyllosilicate clast\", \"Lithic clast (LC1)\", Fig. 3, p.6) and abundances given per section (\"sulfides which make up 2.3 areal% of the section\", p.6)" ;
    ada:secondaryReferenceMaterialDefault "Smithsonian Microbeam standards (specific materials and values N)" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "carbonate",
                "oxide",
                "phosphate",
                "phyllosilicate",
                "sulfide" ;
            ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/backgroundCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/peakCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName> ] ;
    ada:targetSpeciesTemplate [ ada:defaultTargetSpecies "CO2",
                "F",
                "H2O",
                "O" ;
            ada:targetSpeciesColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetSpecies" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalAccuracy>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalPrecision>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/beamCurrent>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/blankCorrection>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferingElements>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied> ] ;
    ada:wdsDeadTimeCorrection "missing" ;
    bios:computationalTool [ schema1:name "Probe for EPMA microanalysis software" ;
            ada:toolRole "acquisition" ],
        [ schema1:name "Probe for EPMA (CITZAF matrix correction, Armstrong 1995); CalcImage and Quantitative Microanalysis Explorer web-based tool (for stage mapping)" ;
            ada:toolRole "dataReduction" ] .

<ex:instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:hasPart <ex:instrument/EPMA/part/EDS-Detector>,
        <ex:instrument/EPMA/part/Electron-Source>,
        <ex:instrument/EPMA/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "JEOL" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "15 kV" ;
    ada:beamDiameterDefault -9999 ;
    ada:beamMode "missing" ;
    ada:mappingBeamCurrentDefault -9999 ;
    ada:mappingBeamDiameterDefault -9999 ;
    ada:mappingBeamMode "missing" .

<ex:instrument/EPMA/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:name "missing" .

<ex:instrument/EPMA/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "missing" ;
    schema1:name "missing" .

<ex:instrument/EPMA/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "5 wavelength-dispersive spectrometers (JEOL)" .

<ex:instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "JXA-8200 (stated as \"JEOL JXA-8200 electron microprobe\")" ] ;
    schema1:name "example instrumentName" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Optical microscopy of the same thin section — \"Eleven OC002 LAB24-2 fragments were mounted and dry-polished in a petrographic thin section used for optical microscopy and electron probe microanalyses\" (p.3)" ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:valueName "preAnalysisImagingAndScreeningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/backgroundCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Background Counting Time" ;
    schema1:valueName "backgroundCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/peakCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Peak Counting Time" ;
    schema1:valueName "peakCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalAccuracy> a schema1:PropertyValueSpecification ;
    schema1:name "Analytical Accuracy" ;
    schema1:valueName "analyticalAccuracy" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalPrecision> a schema1:PropertyValueSpecification ;
    schema1:name "Analytical Precision" ;
    schema1:valueName "analyticalPrecision" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/beamCurrent> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Beam Current" ;
    schema1:valueName "beamCurrent" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/blankCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Blank Correction" ;
    schema1:valueName "blankCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard> a schema1:PropertyValueSpecification ;
    schema1:name "Interference Correction Standard" ;
    schema1:valueName "interferenceCorrectionStandard" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferingElements> a schema1:PropertyValueSpecification ;
    schema1:name "Interfering Elements" ;
    schema1:valueName "interferingElements" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Target Species Estimation Method" ;
    schema1:valueName "targetSpeciesEstimationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Time-Dependent Intensity Correction" ;
    schema1:valueName "timeDependentIntensityCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "X-ray Background Correction Method" ;
    schema1:valueName "xRayBackgroundCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "X-ray Line Overlap Corrections Applied" ;
    schema1:valueName "xRayLineOverlapCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/stageScanVsBeamScan> a schema1:PropertyValue ;
    schema1:name "Stage Scan vs. Beam Scan" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/stageScanVsBeamScan> ;
    schema1:value "Stage scan" .


```


### epmaTAPP example Seifert2026
epmaTAPP instance derived from Seifert+2026 | JEOL 8530 | WDS Point Analysis (ARES JSC).
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
  "@id": "ex:epmaTAPP-Seifert2026",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA Major Element Apatite incl. Halogens, Bennu (ARES JSC, JEOL 8530 EMPA)",
  "schema:description": "Seifert et al. 2026, Meteorit. Planet. Sci. — apatite in Bennu OSIRIS-REx samples. ARES NASA JSC. Instrument stated as \"JEOL 8530 EMPA at NASA JSC\" (no \"JXA\", no \"F\", no \"+\" suffix stated in paper). Analytical conditions: 15 kV, 20 nA, 2 µm probe size. Previous v2 values of 10/40-100 nA and 10 µm beam were WRONG — those were Durango apatite test conditions used to assess beam damage, not the actual protocol. Analytes: P, F, Cl, Ca, Mn, Fe, Na, Mg, Si, S. Apatite stoichiometry by Ketcham (2015) method (13-anion basis; OH by difference). Primary standards: SrF2, albite, olivine, quartz, apatite, barite, tugtupite, rhodonite, ilmenite. Sample preparation: fragments embedded in epoxy, dry-polished, ion-polished (one mount), carbon coated. 14 total analyses performed. Reported detail: ada:edsAcquisitionMode = N — WDS or EDS is not stated; ada:analyticalMode = N — 14 quantitative point analyses; WDS or EDS is not stated, and the list has no value without one.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "ada:beamDiameterDefault": "all: 2 µm — as above",
      "ada:beamMode": "N — 'a 2μm probe size' is recorded under Beam Diameter; no mode is named",
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        }
      ],
      "schema:name": "example instrumentName",
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:mappingBeamDiameterDefault": -9999,
      "ada:mappingBeamMode": "missing"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "JEOL 8530 EMPA (stated as \"JEOL 8530 EMPA at NASA JSC\"; no F suffix or JXA prefix stated)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "P",
      "F",
      "Cl",
      "Ca",
      "Mn",
      "Fe",
      "Na",
      "Mg",
      "Si",
      "S",
      "OH"
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
        "@id": "ada:targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "targetSpeciesEstimationMethod",
        "schema:name": "Target Species Estimation Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalAccuracy",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracy",
        "schema:name": "Analytical Accuracy",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalPrecision",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalPrecision",
        "schema:name": "Analytical Precision",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayBackgroundCorrectionMethod",
        "schema:name": "X-ray Background Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/beamCurrent",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "beamCurrent",
        "schema:name": "Beam Current",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/blankCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "blankCorrection",
        "schema:name": "Blank Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionStandard",
        "schema:name": "Interference Correction Standard",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayLineOverlapCorrectionsApplied",
        "schema:name": "X-ray Line Overlap Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferingElements",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingElements",
        "schema:name": "Interfering Elements",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "timeDependentIntensityCorrection",
        "schema:name": "Time-Dependent Intensity Correction",
        "ada:dataType": "string"
      }
    ]
  },
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/epmaTAPP/beamDamageMinimizationDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "beamDamageMinimizationDefault",
      "schema:name": "Beam Damage Minimization",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "all: Durango apatite compared at 10 μm and 3 μm spot sizes, with no significant volatile loss — 'in order to assess volatilization of halogens using our beam conditions'"
    },
    {
      "@id": "ada:parameter/epmaTAPP/halogenCorrectionOnOxygenDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "halogenCorrectionOnOxygenDefault",
      "schema:name": "Halogen Correction on Oxygen",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N — OH is 'calculated by difference based on 1–F–Cl=OH' (under Target Species Estimation Method); no oxygen-equivalent correction for F and Cl is stated"
    }
  ],
  "ada:edsAcquisitionMode": "N/A",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
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
          "schema:defaultValue": "SEM EDS mapping, then CL imaging, on the JEOL 7900F at JSC — \"Apatite grains in OREX-803079-0 and OREX-803080-0 were identified via EDS mapping and point analysis\", after which \"CL images were obtained for each apatite grain to search for zoning or internal structures not resolvable in EDS maps\", collected \"at 5 kV with beam currents ranging from 1 to 1.5 nA\" (p.2); the numbered grains (Ap. #1 …) tie the probe analyses back to those images"
        }
      ]
    }
  ],
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "Phosphate"
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
        "@id": "ada:targetMaterialColumn/epmaTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "Identification by EDS, then by CL — \"Apatite grains in OREX-803079-0 and OREX-803080-0 were identified via EDS mapping and point analysis\", after which \"CL images were obtained for each apatite grain to search for zoning or internal structures not resolvable in EDS maps\" (p.2)",
  "ada:monitoredElements": [
    "P, F, Cl, Ca, Mn, Fe, Na, Mg, Si, S — all determined. \"A total of 14 analyses were performed at 15 kV, 20 nA, using a 2 μm probe size, and included the elements P, F, Cl, Ca, Mn, Fe, Na, Mg, Si, and S\" (p.3)"
  ],
  "schema:creator": {
    "schema:name": "Logan B. Seifert",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "ARES, NASA Johnson Space Center"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Seifert et al. 2026, Meteorit. Planet. Sci.; doi:10.1111/maps.70167"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-EDS; SIMS (Cameca ims 1280); TEM-EDS"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Grain > Analysis point — Table 1 reports one column per apatite grain (\"Ap. #1\" … \"Ap. #5\") within each of the three particles (p.7)",
  "ada:reportedProperties": [
    "F, Cl, Na2O, MgO, SiO2, SO3, P2O5, CaO, MnO, FeO — wt% with totals, per named grain (Table 1)"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Fragments embedded in epoxy; dry-polished with diamond powder; one mount ion-polished before carbon coating",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
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
      "schema:name": "epma",
      "schema:termCode": "epma"
    }
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "test value schema:defaultValue"
    }
  ],
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
  "schema:datePublished": "test value schema:datePublished"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:epmaTAPP-Seifert2026",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA Major Element Apatite incl. Halogens, Bennu (ARES JSC, JEOL 8530 EMPA)",
  "schema:description": "Seifert et al. 2026, Meteorit. Planet. Sci. \u2014 apatite in Bennu OSIRIS-REx samples. ARES NASA JSC. Instrument stated as \"JEOL 8530 EMPA at NASA JSC\" (no \"JXA\", no \"F\", no \"+\" suffix stated in paper). Analytical conditions: 15 kV, 20 nA, 2 \u00b5m probe size. Previous v2 values of 10/40-100 nA and 10 \u00b5m beam were WRONG \u2014 those were Durango apatite test conditions used to assess beam damage, not the actual protocol. Analytes: P, F, Cl, Ca, Mn, Fe, Na, Mg, Si, S. Apatite stoichiometry by Ketcham (2015) method (13-anion basis; OH by difference). Primary standards: SrF2, albite, olivine, quartz, apatite, barite, tugtupite, rhodonite, ilmenite. Sample preparation: fragments embedded in epoxy, dry-polished, ion-polished (one mount), carbon coated. 14 total analyses performed. Reported detail: ada:edsAcquisitionMode = N \u2014 WDS or EDS is not stated; ada:analyticalMode = N \u2014 14 quantitative point analyses; WDS or EDS is not stated, and the list has no value without one.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "ada:beamDiameterDefault": "all: 2 \u00b5m \u2014 as above",
      "ada:beamMode": "N \u2014 'a 2\u03bcm probe size' is recorded under Beam Diameter; no mode is named",
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        }
      ],
      "schema:name": "example instrumentName",
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:mappingBeamDiameterDefault": -9999,
      "ada:mappingBeamMode": "missing"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "JEOL 8530 EMPA (stated as \"JEOL 8530 EMPA at NASA JSC\"; no F suffix or JXA prefix stated)",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "P",
      "F",
      "Cl",
      "Ca",
      "Mn",
      "Fe",
      "Na",
      "Mg",
      "Si",
      "S",
      "OH"
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
        "@id": "ada:targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "targetSpeciesEstimationMethod",
        "schema:name": "Target Species Estimation Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalAccuracy",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracy",
        "schema:name": "Analytical Accuracy",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalPrecision",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalPrecision",
        "schema:name": "Analytical Precision",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayBackgroundCorrectionMethod",
        "schema:name": "X-ray Background Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/beamCurrent",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "beamCurrent",
        "schema:name": "Beam Current",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/blankCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "blankCorrection",
        "schema:name": "Blank Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionStandard",
        "schema:name": "Interference Correction Standard",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayLineOverlapCorrectionsApplied",
        "schema:name": "X-ray Line Overlap Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferingElements",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingElements",
        "schema:name": "Interfering Elements",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "timeDependentIntensityCorrection",
        "schema:name": "Time-Dependent Intensity Correction",
        "ada:dataType": "string"
      }
    ]
  },
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/epmaTAPP/beamDamageMinimizationDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "beamDamageMinimizationDefault",
      "schema:name": "Beam Damage Minimization",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "all: Durango apatite compared at 10 \u03bcm and 3 \u03bcm spot sizes, with no significant volatile loss \u2014 'in order to assess volatilization of halogens using our beam conditions'"
    },
    {
      "@id": "ada:parameter/epmaTAPP/halogenCorrectionOnOxygenDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "halogenCorrectionOnOxygenDefault",
      "schema:name": "Halogen Correction on Oxygen",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N \u2014 OH is 'calculated by difference based on 1\u2013F\u2013Cl=OH' (under Target Species Estimation Method); no oxygen-equivalent correction for F and Cl is stated"
    }
  ],
  "ada:edsAcquisitionMode": "N/A",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
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
          "schema:defaultValue": "SEM EDS mapping, then CL imaging, on the JEOL 7900F at JSC \u2014 \"Apatite grains in OREX-803079-0 and OREX-803080-0 were identified via EDS mapping and point analysis\", after which \"CL images were obtained for each apatite grain to search for zoning or internal structures not resolvable in EDS maps\", collected \"at 5 kV with beam currents ranging from 1 to 1.5 nA\" (p.2); the numbered grains (Ap. #1 \u2026) tie the probe analyses back to those images"
        }
      ]
    }
  ],
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "Phosphate"
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
        "@id": "ada:targetMaterialColumn/epmaTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "Identification by EDS, then by CL \u2014 \"Apatite grains in OREX-803079-0 and OREX-803080-0 were identified via EDS mapping and point analysis\", after which \"CL images were obtained for each apatite grain to search for zoning or internal structures not resolvable in EDS maps\" (p.2)",
  "ada:monitoredElements": [
    "P, F, Cl, Ca, Mn, Fe, Na, Mg, Si, S \u2014 all determined. \"A total of 14 analyses were performed at 15 kV, 20 nA, using a 2 \u03bcm probe size, and included the elements P, F, Cl, Ca, Mn, Fe, Na, Mg, Si, and S\" (p.3)"
  ],
  "schema:creator": {
    "schema:name": "Logan B. Seifert",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "ARES, NASA Johnson Space Center"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Seifert et al. 2026, Meteorit. Planet. Sci.; doi:10.1111/maps.70167"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-EDS; SIMS (Cameca ims 1280); TEM-EDS"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Grain > Analysis point \u2014 Table 1 reports one column per apatite grain (\"Ap. #1\" \u2026 \"Ap. #5\") within each of the three particles (p.7)",
  "ada:reportedProperties": [
    "F, Cl, Na2O, MgO, SiO2, SO3, P2O5, CaO, MnO, FeO \u2014 wt% with totals, per named grain (Table 1)"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Fragments embedded in epoxy; dry-polished with diamond powder; one mount ion-polished before carbon coating",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
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
      "schema:name": "epma",
      "schema:termCode": "epma"
    }
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "test value schema:defaultValue"
    }
  ],
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
  "schema:datePublished": "test value schema:datePublished"
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

<ex:epmaTAPP-Seifert2026> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:description "Fragments embedded in epoxy; dry-polished with diamond powder; one mount ion-polished before carbon coating" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:detectionLimitMethod "test value ada:detectionLimitMethod" ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDamageMinimizationDefault>,
        <https://ada.astromat.org/metadata/parameter/epmaTAPP/halogenCorrectionOnOxygenDefault> ;
    schema1:creator [ a schema1:Person ;
            schema1:name "Logan B. Seifert" ] ;
    schema1:datePublished "test value schema:datePublished" ;
    schema1:description "Seifert et al. 2026, Meteorit. Planet. Sci. — apatite in Bennu OSIRIS-REx samples. ARES NASA JSC. Instrument stated as \"JEOL 8530 EMPA at NASA JSC\" (no \"JXA\", no \"F\", no \"+\" suffix stated in paper). Analytical conditions: 15 kV, 20 nA, 2 µm probe size. Previous v2 values of 10/40-100 nA and 10 µm beam were WRONG — those were Durango apatite test conditions used to assess beam damage, not the actual protocol. Analytes: P, F, Cl, Ca, Mn, Fe, Na, Mg, Si, S. Apatite stoichiometry by Ketcham (2015) method (13-anion basis; OH by difference). Primary standards: SrF2, albite, olivine, quartz, apatite, barite, tugtupite, rhodonite, ilmenite. Sample preparation: fragments embedded in epoxy, dry-polished, ion-polished (one mount), carbon coated. 14 total analyses performed. Reported detail: ada:edsAcquisitionMode = N — WDS or EDS is not stated; ada:analyticalMode = N — 14 quantitative point analyses; WDS or EDS is not stated, and the list has no value without one." ;
    schema1:instrument <ex:instrument/EPMA>,
        <ex:instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "ARES, NASA Johnson Space Center" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "epma" ;
            schema1:termCode "epma" ] ;
    schema1:name "EPMA Major Element Apatite incl. Halogens, Bennu (ARES JSC, JEOL 8530 EMPA)" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SEM-EDS; SIMS (Cameca ims 1280); TEM-EDS" ] ;
            schema1:url "https://ada.astromat.org/missing" ],
        [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Seifert et al. 2026, Meteorit. Planet. Sci.; doi:10.1111/maps.70167" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "test value schema:defaultValue" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:edsAcquisitionMode "N/A" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:monitoredElements "P, F, Cl, Ca, Mn, Fe, Na, Mg, Si, S — all determined. \"A total of 14 analyses were performed at 15 kV, 20 nA, using a 2 μm probe size, and included the elements P, F, Cl, Ca, Mn, Fe, Na, Mg, Si, and S\" (p.3)" ;
    ada:reportedProperties "F, Cl, Na2O, MgO, SiO2, SO3, P2O5, CaO, MnO, FeO — wt% with totals, per named grain (Table 1)" ;
    ada:samplingUnitSelectionCriteriaDefault "Identification by EDS, then by CL — \"Apatite grains in OREX-803079-0 and OREX-803080-0 were identified via EDS mapping and point analysis\", after which \"CL images were obtained for each apatite grain to search for zoning or internal structures not resolvable in EDS maps\" (p.2)" ;
    ada:samplingUnitType "Grain > Analysis point — Table 1 reports one column per apatite grain (\"Ap. #1\" … \"Ap. #5\") within each of the three particles (p.7)" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "Phosphate" ;
            ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/backgroundCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/peakCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName> ] ;
    ada:targetSpeciesTemplate [ ada:defaultTargetSpecies "Ca",
                "Cl",
                "F",
                "Fe",
                "Mg",
                "Mn",
                "Na",
                "OH",
                "P",
                "S",
                "Si" ;
            ada:targetSpeciesColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetSpecies" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalAccuracy>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalPrecision>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/beamCurrent>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/blankCorrection>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferingElements>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied> ] ;
    ada:wdsDeadTimeCorrection "missing" .

<ex:instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:hasPart <ex:instrument/EPMA/part/EDS-Detector>,
        <ex:instrument/EPMA/part/Electron-Source>,
        <ex:instrument/EPMA/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "JEOL" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "15 kV" ;
    ada:beamDiameterDefault "all: 2 µm — as above" ;
    ada:beamMode "N — 'a 2μm probe size' is recorded under Beam Diameter; no mode is named" ;
    ada:mappingBeamCurrentDefault -9999 ;
    ada:mappingBeamDiameterDefault -9999 ;
    ada:mappingBeamMode "missing" .

<ex:instrument/EPMA/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:name "missing" .

<ex:instrument/EPMA/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "missing" ;
    schema1:name "missing" .

<ex:instrument/EPMA/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "missing" .

<ex:instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "JEOL 8530 EMPA (stated as \"JEOL 8530 EMPA at NASA JSC\"; no F suffix or JXA prefix stated)" ] ;
    schema1:name "example instrumentName" .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDamageMinimizationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "all: Durango apatite compared at 10 μm and 3 μm spot sizes, with no significant volatile loss — 'in order to assess volatilization of halogens using our beam conditions'" ;
    schema1:name "Beam Damage Minimization" ;
    schema1:valueName "beamDamageMinimizationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/halogenCorrectionOnOxygenDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N — OH is 'calculated by difference based on 1–F–Cl=OH' (under Target Species Estimation Method); no oxygen-equivalent correction for F and Cl is stated" ;
    schema1:name "Halogen Correction on Oxygen" ;
    schema1:valueName "halogenCorrectionOnOxygenDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "SEM EDS mapping, then CL imaging, on the JEOL 7900F at JSC — \"Apatite grains in OREX-803079-0 and OREX-803080-0 were identified via EDS mapping and point analysis\", after which \"CL images were obtained for each apatite grain to search for zoning or internal structures not resolvable in EDS maps\", collected \"at 5 kV with beam currents ranging from 1 to 1.5 nA\" (p.2); the numbered grains (Ap. #1 …) tie the probe analyses back to those images" ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:valueName "preAnalysisImagingAndScreeningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/backgroundCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Background Counting Time" ;
    schema1:valueName "backgroundCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/peakCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Peak Counting Time" ;
    schema1:valueName "peakCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalAccuracy> a schema1:PropertyValueSpecification ;
    schema1:name "Analytical Accuracy" ;
    schema1:valueName "analyticalAccuracy" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalPrecision> a schema1:PropertyValueSpecification ;
    schema1:name "Analytical Precision" ;
    schema1:valueName "analyticalPrecision" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/beamCurrent> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Beam Current" ;
    schema1:valueName "beamCurrent" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/blankCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Blank Correction" ;
    schema1:valueName "blankCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard> a schema1:PropertyValueSpecification ;
    schema1:name "Interference Correction Standard" ;
    schema1:valueName "interferenceCorrectionStandard" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferingElements> a schema1:PropertyValueSpecification ;
    schema1:name "Interfering Elements" ;
    schema1:valueName "interferingElements" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Target Species Estimation Method" ;
    schema1:valueName "targetSpeciesEstimationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Time-Dependent Intensity Correction" ;
    schema1:valueName "timeDependentIntensityCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "X-ray Background Correction Method" ;
    schema1:valueName "xRayBackgroundCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "X-ray Line Overlap Corrections Applied" ;
    schema1:valueName "xRayLineOverlapCorrectionsApplied" ;
    ada:dataType "string" .


```


### epmaTAPP example Pang2016
epmaTAPP instance derived from Pang+2016 | JEOL JXA-8100 | WDS Point Analysis (Nanjing U.).
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
  "@id": "ex:epmaTAPP-Pang2016",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS Major Element Silicates/Oxides, NWA 8003 Eucrite (Nanjing U., JEOL JXA-8100)",
  "schema:description": "Pang et al. 2016, Sci. Rep. 6:26063 — NWA 8003 eucrite, Nanjing University. JEOL JXA-8100 (stated as \"JEOL 8100\"). WDS explicitly stated (\"JEOL 8100 WDS\"). ZAF matrix correction (NOT \"ZAF or PAP\" as in v2; paper states ZAF). Focused beam (20 nA) for most phases; defocused 2-5 µm for plagioclase and polymorphs. Natural and synthetic mineral standards (specific names N). Detection limit better than 0.02 wt% (as stated). Analytical software not stated. Reported detail: ada:edsAcquisitionMode = N/A — WDS procedure; ada:analyticalMode = WDS Point Analysis — 'Electron Probe Micro-Analyzer (EPMA) with wavelength dispersive spectrometers (WDS)'.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "ada:beamDiameterDefault": "plagioclase and its polymorphs: 2–5 µm; other: N — 'a defocused beam (2–5 μm in diameter)'",
      "ada:beamMode": "plagioclase and its polymorphs: Defocused; other: Focused — Methods",
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        }
      ],
      "schema:name": "example instrumentName",
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:mappingBeamDiameterDefault": -9999,
      "ada:mappingBeamMode": "missing"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "JXA-8100 (stated as \"JEOL 8100\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:targetSpeciesTemplate": {
    "ada:targetSpeciesDeclaration": "N — no element is named in the paper; the analysed elements are in Supplementary Table 4, which is not in the archived PDF",
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
        "@id": "ada:targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "targetSpeciesEstimationMethod",
        "schema:name": "Target Species Estimation Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalAccuracy",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracy",
        "schema:name": "Analytical Accuracy",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalPrecision",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalPrecision",
        "schema:name": "Analytical Precision",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayBackgroundCorrectionMethod",
        "schema:name": "X-ray Background Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/beamCurrent",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "beamCurrent",
        "schema:name": "Beam Current",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/blankCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "blankCorrection",
        "schema:name": "Blank Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionStandard",
        "schema:name": "Interference Correction Standard",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayLineOverlapCorrectionsApplied",
        "schema:name": "X-ray Line Overlap Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferingElements",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingElements",
        "schema:name": "Interfering Elements",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "timeDependentIntensityCorrection",
        "schema:name": "Time-Dependent Intensity Correction",
        "ada:dataType": "string"
      }
    ],
    "ada:defaultTargetSpecies": []
  },
  "ada:edsAcquisitionMode": "N/A",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
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
          "schema:defaultValue": "SEM petrography — \"The petrographic texture of NWA 8003 was observed using a JEOL 7000F field emission gun scanning electron microscope (FEG-SEM) at Hokkaido University\" (p.7); phase identifications also rest on Raman spectra and EBSD patterns (p.4)"
        }
      ]
    }
  ],
  "ada:matrixCorrectionMethod": "ZAF",
  "ada:targetMaterialTemplate": {
    "ada:targetMaterialDeclaration": "plagioclase and its polymorphs — 'Measurements of most minerals were performed with a focused beam ... whereas measurements of plagioclase and its polymorphs were performed with a defocused beam'; the other minerals are not listed (EPMA data in Supplementary Table 4)",
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
        "@id": "ada:targetMaterialColumn/epmaTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "Spatial position within the shock assemblage — garnet is analysed \"within the eclogitic mineral assemblage of zoned veins\" and contrasted with grains \"in either thin melt veins or the edge zones of zoned melt veins\" (p.4); the individual grains are not otherwise chosen by a stated rule",
  "ada:monitoredElements": [
    "N — \"Natural and synthetic standards were used\" (p.7) without naming them; the analysed elements are given in Supplementary Table 4, which is not in the archived PDF"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "EPMA-WDS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "State Key Laboratory for Mineral Deposits Research, Nanjing University"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Pang et al. 2016, Sci. Rep. 6:26063; doi:10.1038/srep26063"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM (BSE imaging); petrographic microscopy"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Phase > Analysis point — compositions are reported as per-phase means, \"The average compositions (Supplementary Table 1) of orthopyroxene\" (p.2) and \"41 ± 8 mol% on average; based on 13 analyses\" (p.4); the individual points are in a supplement not in the archived PDF",
  "ada:analyticalMode": [
    "WDS Point Analysis"
  ],
  "ada:reportedProperties": [
    "En, Fs, Wo; Ca-Eskola component; empirical formulae — mol% (p.2, p.4); the oxide analyses are in Supplementary Tables 1–4, not in the archived PDF"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished thin section; carbon coating N",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
        "ada:detectionLimitMethod": "test value ada:detectionLimitMethod"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "test value schema:defaultValue"
    }
  ],
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
  "schema:datePublished": "test value schema:datePublished"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:epmaTAPP-Pang2016",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS Major Element Silicates/Oxides, NWA 8003 Eucrite (Nanjing U., JEOL JXA-8100)",
  "schema:description": "Pang et al. 2016, Sci. Rep. 6:26063 \u2014 NWA 8003 eucrite, Nanjing University. JEOL JXA-8100 (stated as \"JEOL 8100\"). WDS explicitly stated (\"JEOL 8100 WDS\"). ZAF matrix correction (NOT \"ZAF or PAP\" as in v2; paper states ZAF). Focused beam (20 nA) for most phases; defocused 2-5 \u00b5m for plagioclase and polymorphs. Natural and synthetic mineral standards (specific names N). Detection limit better than 0.02 wt% (as stated). Analytical software not stated. Reported detail: ada:edsAcquisitionMode = N/A \u2014 WDS procedure; ada:analyticalMode = WDS Point Analysis \u2014 'Electron Probe Micro-Analyzer (EPMA) with wavelength dispersive spectrometers (WDS)'.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "ada:beamDiameterDefault": "plagioclase and its polymorphs: 2\u20135 \u00b5m; other: N \u2014 'a defocused beam (2\u20135 \u03bcm in diameter)'",
      "ada:beamMode": "plagioclase and its polymorphs: Defocused; other: Focused \u2014 Methods",
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        }
      ],
      "schema:name": "example instrumentName",
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:mappingBeamDiameterDefault": -9999,
      "ada:mappingBeamMode": "missing"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "JXA-8100 (stated as \"JEOL 8100\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:targetSpeciesTemplate": {
    "ada:targetSpeciesDeclaration": "N \u2014 no element is named in the paper; the analysed elements are in Supplementary Table 4, which is not in the archived PDF",
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
        "@id": "ada:targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "targetSpeciesEstimationMethod",
        "schema:name": "Target Species Estimation Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalAccuracy",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracy",
        "schema:name": "Analytical Accuracy",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalPrecision",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalPrecision",
        "schema:name": "Analytical Precision",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayBackgroundCorrectionMethod",
        "schema:name": "X-ray Background Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/beamCurrent",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "beamCurrent",
        "schema:name": "Beam Current",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/blankCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "blankCorrection",
        "schema:name": "Blank Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionStandard",
        "schema:name": "Interference Correction Standard",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayLineOverlapCorrectionsApplied",
        "schema:name": "X-ray Line Overlap Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferingElements",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingElements",
        "schema:name": "Interfering Elements",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "timeDependentIntensityCorrection",
        "schema:name": "Time-Dependent Intensity Correction",
        "ada:dataType": "string"
      }
    ],
    "ada:defaultTargetSpecies": []
  },
  "ada:edsAcquisitionMode": "N/A",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
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
          "schema:defaultValue": "SEM petrography \u2014 \"The petrographic texture of NWA 8003 was observed using a JEOL 7000F field emission gun scanning electron microscope (FEG-SEM) at Hokkaido University\" (p.7); phase identifications also rest on Raman spectra and EBSD patterns (p.4)"
        }
      ]
    }
  ],
  "ada:matrixCorrectionMethod": "ZAF",
  "ada:targetMaterialTemplate": {
    "ada:targetMaterialDeclaration": "plagioclase and its polymorphs \u2014 'Measurements of most minerals were performed with a focused beam ... whereas measurements of plagioclase and its polymorphs were performed with a defocused beam'; the other minerals are not listed (EPMA data in Supplementary Table 4)",
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
        "@id": "ada:targetMaterialColumn/epmaTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "Spatial position within the shock assemblage \u2014 garnet is analysed \"within the eclogitic mineral assemblage of zoned veins\" and contrasted with grains \"in either thin melt veins or the edge zones of zoned melt veins\" (p.4); the individual grains are not otherwise chosen by a stated rule",
  "ada:monitoredElements": [
    "N \u2014 \"Natural and synthetic standards were used\" (p.7) without naming them; the analysed elements are given in Supplementary Table 4, which is not in the archived PDF"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "EPMA-WDS"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "State Key Laboratory for Mineral Deposits Research, Nanjing University"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Pang et al. 2016, Sci. Rep. 6:26063; doi:10.1038/srep26063"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM (BSE imaging); petrographic microscopy"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Phase > Analysis point \u2014 compositions are reported as per-phase means, \"The average compositions (Supplementary Table 1) of orthopyroxene\" (p.2) and \"41 \u00b1 8 mol% on average; based on 13 analyses\" (p.4); the individual points are in a supplement not in the archived PDF",
  "ada:analyticalMode": [
    "WDS Point Analysis"
  ],
  "ada:reportedProperties": [
    "En, Fs, Wo; Ca-Eskola component; empirical formulae \u2014 mol% (p.2, p.4); the oxide analyses are in Supplementary Tables 1\u20134, not in the archived PDF"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished thin section; carbon coating N",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
        "ada:detectionLimitMethod": "test value ada:detectionLimitMethod"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "test value schema:defaultValue"
    }
  ],
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
  "schema:datePublished": "test value schema:datePublished"
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

<ex:epmaTAPP-Pang2016> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:description "Polished thin section; carbon coating N" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:detectionLimitMethod "test value ada:detectionLimitMethod" ] ] ;
    schema1:datePublished "test value schema:datePublished" ;
    schema1:description "Pang et al. 2016, Sci. Rep. 6:26063 — NWA 8003 eucrite, Nanjing University. JEOL JXA-8100 (stated as \"JEOL 8100\"). WDS explicitly stated (\"JEOL 8100 WDS\"). ZAF matrix correction (NOT \"ZAF or PAP\" as in v2; paper states ZAF). Focused beam (20 nA) for most phases; defocused 2-5 µm for plagioclase and polymorphs. Natural and synthetic mineral standards (specific names N). Detection limit better than 0.02 wt% (as stated). Analytical software not stated. Reported detail: ada:edsAcquisitionMode = N/A — WDS procedure; ada:analyticalMode = WDS Point Analysis — 'Electron Probe Micro-Analyzer (EPMA) with wavelength dispersive spectrometers (WDS)'." ;
    schema1:instrument <ex:instrument/EPMA>,
        <ex:instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "State Key Laboratory for Mineral Deposits Research, Nanjing University" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "EPMA-WDS" ] ;
    schema1:name "EPMA-WDS Major Element Silicates/Oxides, NWA 8003 Eucrite (Nanjing U., JEOL JXA-8100)" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SEM (BSE imaging); petrographic microscopy" ] ;
            schema1:url "https://ada.astromat.org/missing" ],
        [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Pang et al. 2016, Sci. Rep. 6:26063; doi:10.1038/srep26063" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "test value schema:defaultValue" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analyticalMode "WDS Point Analysis" ;
    ada:edsAcquisitionMode "N/A" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "ZAF" ;
    ada:monitoredElements "N — \"Natural and synthetic standards were used\" (p.7) without naming them; the analysed elements are given in Supplementary Table 4, which is not in the archived PDF" ;
    ada:reportedProperties "En, Fs, Wo; Ca-Eskola component; empirical formulae — mol% (p.2, p.4); the oxide analyses are in Supplementary Tables 1–4, not in the archived PDF" ;
    ada:samplingUnitSelectionCriteriaDefault "Spatial position within the shock assemblage — garnet is analysed \"within the eclogitic mineral assemblage of zoned veins\" and contrasted with grains \"in either thin melt veins or the edge zones of zoned melt veins\" (p.4); the individual grains are not otherwise chosen by a stated rule" ;
    ada:samplingUnitType "Phase > Analysis point — compositions are reported as per-phase means, \"The average compositions (Supplementary Table 1) of orthopyroxene\" (p.2) and \"41 ± 8 mol% on average; based on 13 analyses\" (p.4); the individual points are in a supplement not in the archived PDF" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetMaterialTemplate [ ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/backgroundCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/peakCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName> ;
            ada:targetMaterialDeclaration "plagioclase and its polymorphs — 'Measurements of most minerals were performed with a focused beam ... whereas measurements of plagioclase and its polymorphs were performed with a defocused beam'; the other minerals are not listed (EPMA data in Supplementary Table 4)" ] ;
    ada:targetSpeciesTemplate [ ada:targetSpeciesColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetSpecies" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalAccuracy>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalPrecision>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/beamCurrent>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/blankCorrection>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferingElements>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied> ;
            ada:targetSpeciesDeclaration "N — no element is named in the paper; the analysed elements are in Supplementary Table 4, which is not in the archived PDF" ] ;
    ada:wdsDeadTimeCorrection "missing" .

<ex:instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:hasPart <ex:instrument/EPMA/part/EDS-Detector>,
        <ex:instrument/EPMA/part/Electron-Source>,
        <ex:instrument/EPMA/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "JEOL" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "15 kV" ;
    ada:beamDiameterDefault "plagioclase and its polymorphs: 2–5 µm; other: N — 'a defocused beam (2–5 μm in diameter)'" ;
    ada:beamMode "plagioclase and its polymorphs: Defocused; other: Focused — Methods" ;
    ada:mappingBeamCurrentDefault -9999 ;
    ada:mappingBeamDiameterDefault -9999 ;
    ada:mappingBeamMode "missing" .

<ex:instrument/EPMA/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:name "missing" .

<ex:instrument/EPMA/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "missing" ;
    schema1:name "missing" .

<ex:instrument/EPMA/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "missing" .

<ex:instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "JXA-8100 (stated as \"JEOL 8100\")" ] ;
    schema1:name "example instrumentName" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "SEM petrography — \"The petrographic texture of NWA 8003 was observed using a JEOL 7000F field emission gun scanning electron microscope (FEG-SEM) at Hokkaido University\" (p.7); phase identifications also rest on Raman spectra and EBSD patterns (p.4)" ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:valueName "preAnalysisImagingAndScreeningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/backgroundCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Background Counting Time" ;
    schema1:valueName "backgroundCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/peakCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Peak Counting Time" ;
    schema1:valueName "peakCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalAccuracy> a schema1:PropertyValueSpecification ;
    schema1:name "Analytical Accuracy" ;
    schema1:valueName "analyticalAccuracy" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalPrecision> a schema1:PropertyValueSpecification ;
    schema1:name "Analytical Precision" ;
    schema1:valueName "analyticalPrecision" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/beamCurrent> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Beam Current" ;
    schema1:valueName "beamCurrent" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/blankCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Blank Correction" ;
    schema1:valueName "blankCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard> a schema1:PropertyValueSpecification ;
    schema1:name "Interference Correction Standard" ;
    schema1:valueName "interferenceCorrectionStandard" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferingElements> a schema1:PropertyValueSpecification ;
    schema1:name "Interfering Elements" ;
    schema1:valueName "interferingElements" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Target Species Estimation Method" ;
    schema1:valueName "targetSpeciesEstimationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Time-Dependent Intensity Correction" ;
    schema1:valueName "timeDependentIntensityCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "X-ray Background Correction Method" ;
    schema1:valueName "xRayBackgroundCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "X-ray Line Overlap Corrections Applied" ;
    schema1:valueName "xRayLineOverlapCorrectionsApplied" ;
    ada:dataType "string" .


```


### epmaTAPP example McCoy2025
epmaTAPP instance derived from McCoy+2025_SI | JEOL 8530F+ | WDS Point Analysis (Smithsonian).
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
  "@id": "ex:epmaTAPP-McCoy2025",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA Carbonate, Magnetite and Olivine Composition, Bennu (Smithsonian, JEOL 8530F+ Hyperprobe)",
  "schema:description": "McCoy et al. 2025, Nature 637:320-325 — Bennu evaporites. Protocol 1 of 2: Smithsonian Institution JEOL 8530 F+ Hyperprobe (Field Emission). Ir-coated specimens mounted on Ir-coated Parafilm. Carbonate analyses: 15 kV, 10 nA, 5 µm spot; LIFL (Fe,Mn), TAPL (Mg), PETL (Ca). Magnetite and olivine analyses: 15 kV, 10 nA, 1 µm spot; their own standard suite. Both primary and secondary standard suites fully documented with USNM catalog numbers. Acquisition software and matrix correction method N. WDS not explicitly stated in text (crystal designations LIFL/TAPL/PETL confirm WDS use). Reported detail: ada:edsAcquisitionMode = N — WDS or EDS is not stated; ada:analyticalMode = N — point analyses with named crystals (LIFL, TAPL, PETL); WDS or EDS is not stated, and the list has no value without one.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "ada:beamDiameterDefault": "carbonate: 5 µm; magnetite, olivine: 1 µm — 'with an analytical spot size of 5 µm' (carbonates); 'Analyses were conducted at 15kV and 10nA, with an analytical spot size of 1µm' (the magnetite and olivine sentence)",
      "ada:beamMode": "N — only spot sizes are given",
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "N — the crystals (LIFL, TAPL, PETL) are recorded under Diffracting Crystal; the spectrometer configuration and the X-ray lines are not stated",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:name": "example instrumentName",
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:mappingBeamDiameterDefault": -9999,
      "ada:mappingBeamMode": "missing"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "JXA-8530F Plus (stated as \"JEOL 8530 F+ Hyperprobe Field Emission Electron Probe Microanalyzer\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Fe",
      "Mn",
      "Mg",
      "Ca"
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
        "@id": "ada:targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "targetSpeciesEstimationMethod",
        "schema:name": "Target Species Estimation Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalAccuracy",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracy",
        "schema:name": "Analytical Accuracy",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalPrecision",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalPrecision",
        "schema:name": "Analytical Precision",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayBackgroundCorrectionMethod",
        "schema:name": "X-ray Background Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/beamCurrent",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "beamCurrent",
        "schema:name": "Beam Current",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/blankCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "blankCorrection",
        "schema:name": "Blank Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionStandard",
        "schema:name": "Interference Correction Standard",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayLineOverlapCorrectionsApplied",
        "schema:name": "X-ray Line Overlap Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferingElements",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingElements",
        "schema:name": "Interfering Elements",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "timeDependentIntensityCorrection",
        "schema:name": "Time-Dependent Intensity Correction",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:edsAcquisitionMode": "N/A",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
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
          "schema:defaultValue": "SEM mapping at the Smithsonian — particles 'analysed at 15 kV and around 0.5 nA in high vacuum using a Thermo Fisher Quattro FE-SEM'; 'Maps of loose grains were investigated, then used to inform sectioning' (p.7)"
        }
      ]
    }
  ],
  "ada:secondaryReferenceMaterialDefault": [
    "calcite, dolomite, rhodochrosite, magnetite, San Carlos olivine, Springwater olivine — carbonates: calcite, dolomite and rhodochrosite; magnetite and olivine: magnetite, San Carlos olivine and Springwater olivine (p.7)"
  ],
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "carbonate",
      "magnetite",
      "olivine"
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
        "@id": "ada:targetMaterialColumn/epmaTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "N — the paper names the phases it analysed (see `Sampling Unit Type`) but states no rule for choosing the individual units",
  "ada:monitoredElements": [
    "Fe, Mn, Mg, Ca — all determined. \"Carbonate analyses were run at 15 kV and 10 nA, with an analytical spot size of 5 µm. Fe and Mn were analysed using a LIFL crystal, Mg using a TAPL crystal and Ca using a PETL crystal\" (p.7)"
  ],
  "schema:creator": {
    "schema:name": "T. J. McCoy",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Smithsonian Institution, National Museum of Natural History"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "McCoy et al. 2025, Nature 637:320-325; doi:10.1038/s41586-024-08495-6"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-EDS (NHM London; Smithsonian; JSC); TEM-EDS/EELS; FIB-SEM; ToF-SIMS; XRD; XANES"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Phase > Analysis point — \"Electron microprobe analysis was conducted on Ir-coated specimens\" (p.7); results are reported by phase, e.g. \"the calcite has near-end member composition (4 mol.% or less MgCO3 and FeCO3)\" (p.2)",
  "ada:reportedProperties": [
    "Carbonate end-member composition (mol%: MgCO3, FeCO3, MnCO3 — calcite is \"near-end member composition (4 mol.% or less MgCO3 and FeCO3; 0.1 mol.% or less MnCO3)\", p.2); phase identifications (nominal)"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Ir-coated specimens — 'Electron microprobe analysis was conducted on Ir-coated specimens'; the mounting for the microprobe work is not stated",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
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
      "schema:name": "epma",
      "schema:termCode": "epma"
    }
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "test value schema:defaultValue"
    }
  ],
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
  "schema:datePublished": "test value schema:datePublished"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:epmaTAPP-McCoy2025",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA Carbonate, Magnetite and Olivine Composition, Bennu (Smithsonian, JEOL 8530F+ Hyperprobe)",
  "schema:description": "McCoy et al. 2025, Nature 637:320-325 \u2014 Bennu evaporites. Protocol 1 of 2: Smithsonian Institution JEOL 8530 F+ Hyperprobe (Field Emission). Ir-coated specimens mounted on Ir-coated Parafilm. Carbonate analyses: 15 kV, 10 nA, 5 \u00b5m spot; LIFL (Fe,Mn), TAPL (Mg), PETL (Ca). Magnetite and olivine analyses: 15 kV, 10 nA, 1 \u00b5m spot; their own standard suite. Both primary and secondary standard suites fully documented with USNM catalog numbers. Acquisition software and matrix correction method N. WDS not explicitly stated in text (crystal designations LIFL/TAPL/PETL confirm WDS use). Reported detail: ada:edsAcquisitionMode = N \u2014 WDS or EDS is not stated; ada:analyticalMode = N \u2014 point analyses with named crystals (LIFL, TAPL, PETL); WDS or EDS is not stated, and the list has no value without one.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "ada:beamDiameterDefault": "carbonate: 5 \u00b5m; magnetite, olivine: 1 \u00b5m \u2014 'with an analytical spot size of 5 \u00b5m' (carbonates); 'Analyses were conducted at 15kV and 10nA, with an analytical spot size of 1\u00b5m' (the magnetite and olivine sentence)",
      "ada:beamMode": "N \u2014 only spot sizes are given",
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "N \u2014 the crystals (LIFL, TAPL, PETL) are recorded under Diffracting Crystal; the spectrometer configuration and the X-ray lines are not stated",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:name": "example instrumentName",
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:mappingBeamDiameterDefault": -9999,
      "ada:mappingBeamMode": "missing"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "JXA-8530F Plus (stated as \"JEOL 8530 F+ Hyperprobe Field Emission Electron Probe Microanalyzer\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Fe",
      "Mn",
      "Mg",
      "Ca"
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
        "@id": "ada:targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "targetSpeciesEstimationMethod",
        "schema:name": "Target Species Estimation Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalAccuracy",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracy",
        "schema:name": "Analytical Accuracy",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalPrecision",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalPrecision",
        "schema:name": "Analytical Precision",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayBackgroundCorrectionMethod",
        "schema:name": "X-ray Background Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/beamCurrent",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "beamCurrent",
        "schema:name": "Beam Current",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/blankCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "blankCorrection",
        "schema:name": "Blank Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionStandard",
        "schema:name": "Interference Correction Standard",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayLineOverlapCorrectionsApplied",
        "schema:name": "X-ray Line Overlap Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferingElements",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingElements",
        "schema:name": "Interfering Elements",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "timeDependentIntensityCorrection",
        "schema:name": "Time-Dependent Intensity Correction",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:edsAcquisitionMode": "N/A",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
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
          "schema:defaultValue": "SEM mapping at the Smithsonian \u2014 particles 'analysed at 15 kV and around 0.5 nA in high vacuum using a Thermo Fisher Quattro FE-SEM'; 'Maps of loose grains were investigated, then used to inform sectioning' (p.7)"
        }
      ]
    }
  ],
  "ada:secondaryReferenceMaterialDefault": [
    "calcite, dolomite, rhodochrosite, magnetite, San Carlos olivine, Springwater olivine \u2014 carbonates: calcite, dolomite and rhodochrosite; magnetite and olivine: magnetite, San Carlos olivine and Springwater olivine (p.7)"
  ],
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "carbonate",
      "magnetite",
      "olivine"
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
        "@id": "ada:targetMaterialColumn/epmaTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "N \u2014 the paper names the phases it analysed (see `Sampling Unit Type`) but states no rule for choosing the individual units",
  "ada:monitoredElements": [
    "Fe, Mn, Mg, Ca \u2014 all determined. \"Carbonate analyses were run at 15 kV and 10 nA, with an analytical spot size of 5 \u00b5m. Fe and Mn were analysed using a LIFL crystal, Mg using a TAPL crystal and Ca using a PETL crystal\" (p.7)"
  ],
  "schema:creator": {
    "schema:name": "T. J. McCoy",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Smithsonian Institution, National Museum of Natural History"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "McCoy et al. 2025, Nature 637:320-325; doi:10.1038/s41586-024-08495-6"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-EDS (NHM London; Smithsonian; JSC); TEM-EDS/EELS; FIB-SEM; ToF-SIMS; XRD; XANES"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Phase > Analysis point \u2014 \"Electron microprobe analysis was conducted on Ir-coated specimens\" (p.7); results are reported by phase, e.g. \"the calcite has near-end member composition (4 mol.% or less MgCO3 and FeCO3)\" (p.2)",
  "ada:reportedProperties": [
    "Carbonate end-member composition (mol%: MgCO3, FeCO3, MnCO3 \u2014 calcite is \"near-end member composition (4 mol.% or less MgCO3 and FeCO3; 0.1 mol.% or less MnCO3)\", p.2); phase identifications (nominal)"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Ir-coated specimens \u2014 'Electron microprobe analysis was conducted on Ir-coated specimens'; the mounting for the microprobe work is not stated",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
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
      "schema:name": "epma",
      "schema:termCode": "epma"
    }
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "test value schema:defaultValue"
    }
  ],
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
  "schema:datePublished": "test value schema:datePublished"
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

<ex:epmaTAPP-McCoy2025> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:description "Ir-coated specimens — 'Electron microprobe analysis was conducted on Ir-coated specimens'; the mounting for the microprobe work is not stated" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:detectionLimitMethod "test value ada:detectionLimitMethod" ] ] ;
    schema1:creator [ a schema1:Person ;
            schema1:name "T. J. McCoy" ] ;
    schema1:datePublished "test value schema:datePublished" ;
    schema1:description "McCoy et al. 2025, Nature 637:320-325 — Bennu evaporites. Protocol 1 of 2: Smithsonian Institution JEOL 8530 F+ Hyperprobe (Field Emission). Ir-coated specimens mounted on Ir-coated Parafilm. Carbonate analyses: 15 kV, 10 nA, 5 µm spot; LIFL (Fe,Mn), TAPL (Mg), PETL (Ca). Magnetite and olivine analyses: 15 kV, 10 nA, 1 µm spot; their own standard suite. Both primary and secondary standard suites fully documented with USNM catalog numbers. Acquisition software and matrix correction method N. WDS not explicitly stated in text (crystal designations LIFL/TAPL/PETL confirm WDS use). Reported detail: ada:edsAcquisitionMode = N — WDS or EDS is not stated; ada:analyticalMode = N — point analyses with named crystals (LIFL, TAPL, PETL); WDS or EDS is not stated, and the list has no value without one." ;
    schema1:instrument <ex:instrument/EPMA>,
        <ex:instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Smithsonian Institution, National Museum of Natural History" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "epma" ;
            schema1:termCode "epma" ] ;
    schema1:name "EPMA Carbonate, Magnetite and Olivine Composition, Bennu (Smithsonian, JEOL 8530F+ Hyperprobe)" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SEM-EDS (NHM London; Smithsonian; JSC); TEM-EDS/EELS; FIB-SEM; ToF-SIMS; XRD; XANES" ] ;
            schema1:url "https://ada.astromat.org/missing" ],
        [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "McCoy et al. 2025, Nature 637:320-325; doi:10.1038/s41586-024-08495-6" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "test value schema:defaultValue" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:edsAcquisitionMode "N/A" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:monitoredElements "Fe, Mn, Mg, Ca — all determined. \"Carbonate analyses were run at 15 kV and 10 nA, with an analytical spot size of 5 µm. Fe and Mn were analysed using a LIFL crystal, Mg using a TAPL crystal and Ca using a PETL crystal\" (p.7)" ;
    ada:reportedProperties "Carbonate end-member composition (mol%: MgCO3, FeCO3, MnCO3 — calcite is \"near-end member composition (4 mol.% or less MgCO3 and FeCO3; 0.1 mol.% or less MnCO3)\", p.2); phase identifications (nominal)" ;
    ada:samplingUnitSelectionCriteriaDefault "N — the paper names the phases it analysed (see `Sampling Unit Type`) but states no rule for choosing the individual units" ;
    ada:samplingUnitType "Phase > Analysis point — \"Electron microprobe analysis was conducted on Ir-coated specimens\" (p.7); results are reported by phase, e.g. \"the calcite has near-end member composition (4 mol.% or less MgCO3 and FeCO3)\" (p.2)" ;
    ada:secondaryReferenceMaterialDefault "calcite, dolomite, rhodochrosite, magnetite, San Carlos olivine, Springwater olivine — carbonates: calcite, dolomite and rhodochrosite; magnetite and olivine: magnetite, San Carlos olivine and Springwater olivine (p.7)" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "carbonate",
                "magnetite",
                "olivine" ;
            ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/backgroundCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/peakCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName> ] ;
    ada:targetSpeciesTemplate [ ada:defaultTargetSpecies "Ca",
                "Fe",
                "Mg",
                "Mn" ;
            ada:targetSpeciesColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetSpecies" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalAccuracy>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalPrecision>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/beamCurrent>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/blankCorrection>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferingElements>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied> ] ;
    ada:wdsDeadTimeCorrection "missing" .

<ex:instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:hasPart <ex:instrument/EPMA/part/EDS-Detector>,
        <ex:instrument/EPMA/part/Electron-Source>,
        <ex:instrument/EPMA/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "JEOL" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "15 kV" ;
    ada:beamDiameterDefault "carbonate: 5 µm; magnetite, olivine: 1 µm — 'with an analytical spot size of 5 µm' (carbonates); 'Analyses were conducted at 15kV and 10nA, with an analytical spot size of 1µm' (the magnetite and olivine sentence)" ;
    ada:beamMode "N — only spot sizes are given" ;
    ada:mappingBeamCurrentDefault -9999 ;
    ada:mappingBeamDiameterDefault -9999 ;
    ada:mappingBeamMode "missing" .

<ex:instrument/EPMA/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:name "missing" .

<ex:instrument/EPMA/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Unknown" ;
    schema1:name "missing" .

<ex:instrument/EPMA/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "N — the crystals (LIFL, TAPL, PETL) are recorded under Diffracting Crystal; the spectrometer configuration and the X-ray lines are not stated" .

<ex:instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "JXA-8530F Plus (stated as \"JEOL 8530 F+ Hyperprobe Field Emission Electron Probe Microanalyzer\")" ] ;
    schema1:name "example instrumentName" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "SEM mapping at the Smithsonian — particles 'analysed at 15 kV and around 0.5 nA in high vacuum using a Thermo Fisher Quattro FE-SEM'; 'Maps of loose grains were investigated, then used to inform sectioning' (p.7)" ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:valueName "preAnalysisImagingAndScreeningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/backgroundCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Background Counting Time" ;
    schema1:valueName "backgroundCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/peakCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Peak Counting Time" ;
    schema1:valueName "peakCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalAccuracy> a schema1:PropertyValueSpecification ;
    schema1:name "Analytical Accuracy" ;
    schema1:valueName "analyticalAccuracy" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalPrecision> a schema1:PropertyValueSpecification ;
    schema1:name "Analytical Precision" ;
    schema1:valueName "analyticalPrecision" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/beamCurrent> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Beam Current" ;
    schema1:valueName "beamCurrent" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/blankCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Blank Correction" ;
    schema1:valueName "blankCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard> a schema1:PropertyValueSpecification ;
    schema1:name "Interference Correction Standard" ;
    schema1:valueName "interferenceCorrectionStandard" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferingElements> a schema1:PropertyValueSpecification ;
    schema1:name "Interfering Elements" ;
    schema1:valueName "interferingElements" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Target Species Estimation Method" ;
    schema1:valueName "targetSpeciesEstimationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Time-Dependent Intensity Correction" ;
    schema1:valueName "timeDependentIntensityCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "X-ray Background Correction Method" ;
    schema1:valueName "xRayBackgroundCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "X-ray Line Overlap Corrections Applied" ;
    schema1:valueName "xRayLineOverlapCorrectionsApplied" ;
    ada:dataType "string" .


```


### epmaTAPP example McCoy2025-2
epmaTAPP instance derived from McCoy+2025_UA | Cameca SX-100 | WDS Point Analysis (K-ALFAA U.Arizona).
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
  "@id": "ex:epmaTAPP-McCoy2025-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS Phosphate+Carbonate Composition, Bennu (K-ALFAA U.Arizona, Cameca SX-100)",
  "schema:description": "McCoy et al. 2025, Nature 637:320-325 — Bennu evaporites. Protocol 2 of 2: U. Arizona K-ALFAA Cameca SX-100. 20 nm carbon coat. WDS explicitly stated for phosphate analyses. Mg,Na phosphate analyses: 15 kV, 8 nA, 1 µm. Carbonate analyses at K-ALFAA also mentioned; conditions N. Full primary standard suite documented for phosphates and carbonates. Acquisition software and matrix correction method N. Reported detail: ada:edsAcquisitionMode = N/A — WDS procedure; ada:analyticalMode = WDS Point Analysis — 'Wavelength-dispersive X-ray spectroscopy analyses of Mg,Na phosphate'.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "ada:beamDiameterDefault": "\"Mg,Na phosphate\": 1 µm; other: N — 'using a 1-µm beam size'",
      "ada:beamMode": "N — only a '1-µm beam size' is given, for the phosphate analyses",
      "schema:manufacturer": {
        "schema:name": "Cameca",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        }
      ],
      "schema:name": "example instrumentName",
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:mappingBeamDiameterDefault": -9999,
      "ada:mappingBeamMode": "missing"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "SX-100 (stated as \"Cameca SX-100 electron microprobe located at K-ALFAA\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "F",
      "P",
      "Ca",
      "Si",
      "Mg",
      "Fe",
      "Al",
      "S",
      "K",
      "Cl",
      "Na",
      "Mn"
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
        "@id": "ada:targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "targetSpeciesEstimationMethod",
        "schema:name": "Target Species Estimation Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalAccuracy",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracy",
        "schema:name": "Analytical Accuracy",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalPrecision",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalPrecision",
        "schema:name": "Analytical Precision",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayBackgroundCorrectionMethod",
        "schema:name": "X-ray Background Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/beamCurrent",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "beamCurrent",
        "schema:name": "Beam Current",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/blankCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "blankCorrection",
        "schema:name": "Blank Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionStandard",
        "schema:name": "Interference Correction Standard",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayLineOverlapCorrectionsApplied",
        "schema:name": "X-ray Line Overlap Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferingElements",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingElements",
        "schema:name": "Interfering Elements",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "timeDependentIntensityCorrection",
        "schema:name": "Time-Dependent Intensity Correction",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:edsAcquisitionMode": "N/A",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
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
          "schema:defaultValue": "N — the paper describes SEM characterisation at JSC, the NHM, the Smithsonian and Curtin, not for the K-ALFAA microprobe work"
        }
      ]
    }
  ],
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "\"Mg",
      "Na phosphate\"",
      "carbonate"
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
        "@id": "ada:targetMaterialColumn/epmaTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "N — the paper names the phases it analysed (see `Sampling Unit Type`) but states no rule for choosing the individual units",
  "ada:monitoredElements": [
    "F, P, Ca, Si, Mg, Fe, Al, S, K, Cl, Na, Mn — as for Target Species"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "EPMA-WDS"
    }
  ],
  "schema:creator": {
    "schema:name": "T. J. Zega",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Kuiper-Arizona Laboratory for Astromaterials Analysis (K-ALFAA), University of Arizona"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "McCoy et al. 2025, Nature 637:320-325; doi:10.1038/s41586-024-08495-6"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-EDS (NHM London; Smithsonian; JSC); TEM-EDS/EELS; FIB-SEM; ToF-SIMS; XRD; XANES"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Phase > Analysis point — \"EMPA analyses were carried out using a Cameca SX-100 electron microprobe located at K-ALFAA\" (p.7); results are reported by phase, not per named point",
  "ada:analyticalMode": [
    "WDS Point Analysis"
  ],
  "ada:reportedProperties": [
    "N — phosphate and carbonate compositions are reported by phase (p.2); the quantitative analyses are in the supplementary tables, not in the archived PDF"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished section; 20 nm carbon coat",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
        "ada:detectionLimitMethod": "test value ada:detectionLimitMethod"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "test value schema:defaultValue"
    }
  ],
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
  "schema:datePublished": "test value schema:datePublished"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:epmaTAPP-McCoy2025-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS Phosphate+Carbonate Composition, Bennu (K-ALFAA U.Arizona, Cameca SX-100)",
  "schema:description": "McCoy et al. 2025, Nature 637:320-325 \u2014 Bennu evaporites. Protocol 2 of 2: U. Arizona K-ALFAA Cameca SX-100. 20 nm carbon coat. WDS explicitly stated for phosphate analyses. Mg,Na phosphate analyses: 15 kV, 8 nA, 1 \u00b5m. Carbonate analyses at K-ALFAA also mentioned; conditions N. Full primary standard suite documented for phosphates and carbonates. Acquisition software and matrix correction method N. Reported detail: ada:edsAcquisitionMode = N/A \u2014 WDS procedure; ada:analyticalMode = WDS Point Analysis \u2014 'Wavelength-dispersive X-ray spectroscopy analyses of Mg,Na phosphate'.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "ada:beamDiameterDefault": "\"Mg,Na phosphate\": 1 \u00b5m; other: N \u2014 'using a 1-\u00b5m beam size'",
      "ada:beamMode": "N \u2014 only a '1-\u00b5m beam size' is given, for the phosphate analyses",
      "schema:manufacturer": {
        "schema:name": "Cameca",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        }
      ],
      "schema:name": "example instrumentName",
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:mappingBeamDiameterDefault": -9999,
      "ada:mappingBeamMode": "missing"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "SX-100 (stated as \"Cameca SX-100 electron microprobe located at K-ALFAA\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "F",
      "P",
      "Ca",
      "Si",
      "Mg",
      "Fe",
      "Al",
      "S",
      "K",
      "Cl",
      "Na",
      "Mn"
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
        "@id": "ada:targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "targetSpeciesEstimationMethod",
        "schema:name": "Target Species Estimation Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalAccuracy",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracy",
        "schema:name": "Analytical Accuracy",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalPrecision",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalPrecision",
        "schema:name": "Analytical Precision",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayBackgroundCorrectionMethod",
        "schema:name": "X-ray Background Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/beamCurrent",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "beamCurrent",
        "schema:name": "Beam Current",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/blankCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "blankCorrection",
        "schema:name": "Blank Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionStandard",
        "schema:name": "Interference Correction Standard",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayLineOverlapCorrectionsApplied",
        "schema:name": "X-ray Line Overlap Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferingElements",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingElements",
        "schema:name": "Interfering Elements",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "timeDependentIntensityCorrection",
        "schema:name": "Time-Dependent Intensity Correction",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:edsAcquisitionMode": "N/A",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
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
          "schema:defaultValue": "N \u2014 the paper describes SEM characterisation at JSC, the NHM, the Smithsonian and Curtin, not for the K-ALFAA microprobe work"
        }
      ]
    }
  ],
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "\"Mg",
      "Na phosphate\"",
      "carbonate"
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
        "@id": "ada:targetMaterialColumn/epmaTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "N \u2014 the paper names the phases it analysed (see `Sampling Unit Type`) but states no rule for choosing the individual units",
  "ada:monitoredElements": [
    "F, P, Ca, Si, Mg, Fe, Al, S, K, Cl, Na, Mn \u2014 as for Target Species"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "EPMA-WDS"
    }
  ],
  "schema:creator": {
    "schema:name": "T. J. Zega",
    "@type": [
      "schema:Person"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Kuiper-Arizona Laboratory for Astromaterials Analysis (K-ALFAA), University of Arizona"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "McCoy et al. 2025, Nature 637:320-325; doi:10.1038/s41586-024-08495-6"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-EDS (NHM London; Smithsonian; JSC); TEM-EDS/EELS; FIB-SEM; ToF-SIMS; XRD; XANES"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Phase > Analysis point \u2014 \"EMPA analyses were carried out using a Cameca SX-100 electron microprobe located at K-ALFAA\" (p.7); results are reported by phase, not per named point",
  "ada:analyticalMode": [
    "WDS Point Analysis"
  ],
  "ada:reportedProperties": [
    "N \u2014 phosphate and carbonate compositions are reported by phase (p.2); the quantitative analyses are in the supplementary tables, not in the archived PDF"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished section; 20 nm carbon coat",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
        "ada:detectionLimitMethod": "test value ada:detectionLimitMethod"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "test value schema:defaultValue"
    }
  ],
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
  "schema:datePublished": "test value schema:datePublished"
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

<ex:epmaTAPP-McCoy2025-2> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:detectionLimitMethod "test value ada:detectionLimitMethod" ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:description "Polished section; 20 nm carbon coat" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:creator [ a schema1:Person ;
            schema1:name "T. J. Zega" ] ;
    schema1:datePublished "test value schema:datePublished" ;
    schema1:description "McCoy et al. 2025, Nature 637:320-325 — Bennu evaporites. Protocol 2 of 2: U. Arizona K-ALFAA Cameca SX-100. 20 nm carbon coat. WDS explicitly stated for phosphate analyses. Mg,Na phosphate analyses: 15 kV, 8 nA, 1 µm. Carbonate analyses at K-ALFAA also mentioned; conditions N. Full primary standard suite documented for phosphates and carbonates. Acquisition software and matrix correction method N. Reported detail: ada:edsAcquisitionMode = N/A — WDS procedure; ada:analyticalMode = WDS Point Analysis — 'Wavelength-dispersive X-ray spectroscopy analyses of Mg,Na phosphate'." ;
    schema1:instrument <ex:instrument/EPMA>,
        <ex:instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Kuiper-Arizona Laboratory for Astromaterials Analysis (K-ALFAA), University of Arizona" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "EPMA-WDS" ] ;
    schema1:name "EPMA-WDS Phosphate+Carbonate Composition, Bennu (K-ALFAA U.Arizona, Cameca SX-100)" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "McCoy et al. 2025, Nature 637:320-325; doi:10.1038/s41586-024-08495-6" ] ;
            schema1:url "https://ada.astromat.org/missing" ],
        [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SEM-EDS (NHM London; Smithsonian; JSC); TEM-EDS/EELS; FIB-SEM; ToF-SIMS; XRD; XANES" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "test value schema:defaultValue" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analyticalMode "WDS Point Analysis" ;
    ada:edsAcquisitionMode "N/A" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:monitoredElements "F, P, Ca, Si, Mg, Fe, Al, S, K, Cl, Na, Mn — as for Target Species" ;
    ada:reportedProperties "N — phosphate and carbonate compositions are reported by phase (p.2); the quantitative analyses are in the supplementary tables, not in the archived PDF" ;
    ada:samplingUnitSelectionCriteriaDefault "N — the paper names the phases it analysed (see `Sampling Unit Type`) but states no rule for choosing the individual units" ;
    ada:samplingUnitType "Phase > Analysis point — \"EMPA analyses were carried out using a Cameca SX-100 electron microprobe located at K-ALFAA\" (p.7); results are reported by phase, not per named point" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "\"Mg",
                "Na phosphate\"",
                "carbonate" ;
            ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/backgroundCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/peakCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName> ] ;
    ada:targetSpeciesTemplate [ ada:defaultTargetSpecies "Al",
                "Ca",
                "Cl",
                "F",
                "Fe",
                "K",
                "Mg",
                "Mn",
                "Na",
                "P",
                "S",
                "Si" ;
            ada:targetSpeciesColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetSpecies" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalAccuracy>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalPrecision>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/beamCurrent>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/blankCorrection>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferingElements>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied> ] ;
    ada:wdsDeadTimeCorrection "missing" .

<ex:instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:hasPart <ex:instrument/EPMA/part/EDS-Detector>,
        <ex:instrument/EPMA/part/Electron-Source>,
        <ex:instrument/EPMA/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Cameca" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "15 kV" ;
    ada:beamDiameterDefault "\"Mg,Na phosphate\": 1 µm; other: N — 'using a 1-µm beam size'" ;
    ada:beamMode "N — only a '1-µm beam size' is given, for the phosphate analyses" ;
    ada:mappingBeamCurrentDefault -9999 ;
    ada:mappingBeamDiameterDefault -9999 ;
    ada:mappingBeamMode "missing" .

<ex:instrument/EPMA/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:name "missing" .

<ex:instrument/EPMA/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "missing" ;
    schema1:name "missing" .

<ex:instrument/EPMA/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "missing" .

<ex:instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "SX-100 (stated as \"Cameca SX-100 electron microprobe located at K-ALFAA\")" ] ;
    schema1:name "example instrumentName" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N — the paper describes SEM characterisation at JSC, the NHM, the Smithsonian and Curtin, not for the K-ALFAA microprobe work" ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:valueName "preAnalysisImagingAndScreeningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/backgroundCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Background Counting Time" ;
    schema1:valueName "backgroundCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/peakCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Peak Counting Time" ;
    schema1:valueName "peakCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalAccuracy> a schema1:PropertyValueSpecification ;
    schema1:name "Analytical Accuracy" ;
    schema1:valueName "analyticalAccuracy" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalPrecision> a schema1:PropertyValueSpecification ;
    schema1:name "Analytical Precision" ;
    schema1:valueName "analyticalPrecision" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/beamCurrent> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Beam Current" ;
    schema1:valueName "beamCurrent" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/blankCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Blank Correction" ;
    schema1:valueName "blankCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard> a schema1:PropertyValueSpecification ;
    schema1:name "Interference Correction Standard" ;
    schema1:valueName "interferenceCorrectionStandard" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferingElements> a schema1:PropertyValueSpecification ;
    schema1:name "Interfering Elements" ;
    schema1:valueName "interferingElements" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Target Species Estimation Method" ;
    schema1:valueName "targetSpeciesEstimationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Time-Dependent Intensity Correction" ;
    schema1:valueName "timeDependentIntensityCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "X-ray Background Correction Method" ;
    schema1:valueName "xRayBackgroundCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "X-ray Line Overlap Corrections Applied" ;
    schema1:valueName "xRayLineOverlapCorrectionsApplied" ;
    ada:dataType "string" .


```


### epmaTAPP example Zega2025
epmaTAPP instance derived from Zega+2025 | Cameca SX-100 Ultra | WDS Point Analysis (K-ALFAA U.Arizona).
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
  "@id": "ex:epmaTAPP-Zega2025",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA Major Element Silicates/Sulfides/Oxides/Phosphates/Carbonates, Bennu (K-ALFAA, Cameca SX-100 Ultra)",
  "schema:description": "Zega et al. 2025, Nat. Geosci. — mineralogical evidence for hydrothermal alteration of Bennu. K-ALFAA, University of Arizona. Instrument stated as \"SX-100 Ultra electron microprobe in the K-ALFAA\". IMPORTANT: v2 had \"no protocol details reported\" — this was WRONG. The paper provides detailed EPMA conditions: X-ray maps and BSE images: 15 kV, 20 nA. Silicates/sulfides/oxides: 15 kV, 20 nA, focused, 20 s peak, 10 s on each background. Phosphates: 15 kV, 8 nA, 2 µm defocused, 20 s peak and 10 s background. Carbonates: 15 kV, 4 nA, 2 µm defocused, 10 s peak and 5 s background. Standards: \"well-characterized natural and synthetic materials\" (specific names N). Phase maps generated using XMapTools. WDS and matrix correction NOT explicitly stated in paper. Reported detail: ada:edsAcquisitionMode = N — WDS or EDS is not stated; ada:analyticalMode = N — quantitative point analyses and X-ray maps ('BSE images, element maps and quantitative compositional analyses'); WDS or EDS is not stated, and the list has no value without one.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "ada:beamDiameterDefault": "phosphates, carbonates: 2 µm; other: N — p.9",
      "ada:beamMode": "silicates, sulfides, oxides: Focused; phosphates, carbonates: Defocused — 'Quantitative analyses of silicates, sulfides and oxides were run using a focused beam ... A 2-μm defocused beam size ... for phosphate and carbonate analyses'",
      "schema:manufacturer": {
        "schema:name": "Cameca",
        "@type": [
          "schema:Organization"
        ]
      },
      "ada:mappingBeamCurrentDefault": "20 nA — 'X-ray maps and BSE images were run at 15kV and 20nA'",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        }
      ],
      "schema:name": "example instrumentName",
      "ada:mappingBeamDiameterDefault": -9999,
      "ada:mappingBeamMode": "missing"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "SX-100 Ultra (stated as \"SX-100 Ultra electron microprobe in the K-ALFAA\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/epmaTAPP/beamDamageMinimizationDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "beamDamageMinimizationDefault",
      "schema:name": "Beam Damage Minimization",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "phosphates, carbonates: 2 µm defocused beam, lower beam currents and shorter count times; other: N — 'to minimize possible beam damage effects'"
    }
  ],
  "ada:edsAcquisitionMode": "N/A",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
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
          "schema:defaultValue": "SEM imaging and EDS mapping before the probe — particles were characterized by SE and BSE imaging and by EDS mapping of \"The compositional heterogeneity of the particles\" (p.9), and the paper's Fig. 1 pairs those BSE images with the EMPA data (p.2); the Methods list SEM before electron microprobe analysis without stating an explicit order"
        }
      ]
    }
  ],
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "silicates",
      "sulfides",
      "oxides",
      "phosphates",
      "carbonates"
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
        "@id": "ada:targetMaterialColumn/epmaTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "N — beam conditions are given per phase (\"Quantitative analyses of silicates, sulfides and oxides were run using a focused beam\"; \"A 2-μm defocused beam size, lower beam currents and shorter count times were used for phosphate and carbonate analyses\", p.9), but that is a setting per phase, not a rule for choosing which grains were analysed",
  "ada:monitoredElements": [
    "N — \"Well-characterized natural and synthetic materials were used as standards\" (p.9); the paper gives beam conditions and count times for silicates, sulfides, oxides, phosphates and carbonates but names no element"
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Kuiper-Arizona Laboratory for Astromaterials Analysis (K-ALFAA), University of Arizona"
  },
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA Planetary Science Enabling Facilities 80NSSC23K0327; NASA Planetary Major Equipment NNX12AL47G and NNX15AJ22G; NASA Early Career Award 80NSSC20K1087; NSF Major Research Instrumentation 1531243 and 0619599; Gordon and Betty Moore Foundation; State of Arizona Technology and Research Initiative Fund — acknowledged 'for supporting K-ALFAA operations' and 'for supporting the instrumentation in K-ALFAA'; which award bought the microprobe is not stated"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Zega et al. 2025, Nat. Geosci.; doi:10.1038/s41561-025-01741-0"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-EDS; TEM-EDS/EELS; FIB-SEM; XRD; XANES"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Grain > Phase — sulfide compositions are reported per grain within named particles (\"Pyrrhotite compositions measured by EMPA\", p.2), and \"phase mapping via electron microprobe analysis (EMPA)\" gives modal abundances of carbonates, sulfides and magnetite per particle (p.2)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "XMapTools (for phase maps)"
    }
  ],
  "ada:reportedProperties": [
    "Fe + Co, S, Ni; modal abundance of carbonates, sulfides and magnetite — sulfide compositions in at% (Fig. 1); modal abundances '0.4–3.4%, ~3–8% and ~3–5%' from the EMPA phase maps (p.2)"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "epma",
      "schema:termCode": "epma"
    }
  ],
  "schema:actionProcess": {
    "@type": [
      "schema:HowTo"
    ],
    "schema:name": "missing",
    "schema:step": [
      {
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:name": "Sample preparation",
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 1,
        "schema:description": "test value schema:description"
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:name": "Data reduction",
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
        "ada:detectionLimitMethod": "test value ada:detectionLimitMethod"
      }
    ]
  },
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "test value schema:defaultValue"
    }
  ],
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
  "schema:datePublished": "test value schema:datePublished"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:epmaTAPP-Zega2025",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA Major Element Silicates/Sulfides/Oxides/Phosphates/Carbonates, Bennu (K-ALFAA, Cameca SX-100 Ultra)",
  "schema:description": "Zega et al. 2025, Nat. Geosci. \u2014 mineralogical evidence for hydrothermal alteration of Bennu. K-ALFAA, University of Arizona. Instrument stated as \"SX-100 Ultra electron microprobe in the K-ALFAA\". IMPORTANT: v2 had \"no protocol details reported\" \u2014 this was WRONG. The paper provides detailed EPMA conditions: X-ray maps and BSE images: 15 kV, 20 nA. Silicates/sulfides/oxides: 15 kV, 20 nA, focused, 20 s peak, 10 s on each background. Phosphates: 15 kV, 8 nA, 2 \u00b5m defocused, 20 s peak and 10 s background. Carbonates: 15 kV, 4 nA, 2 \u00b5m defocused, 10 s peak and 5 s background. Standards: \"well-characterized natural and synthetic materials\" (specific names N). Phase maps generated using XMapTools. WDS and matrix correction NOT explicitly stated in paper. Reported detail: ada:edsAcquisitionMode = N \u2014 WDS or EDS is not stated; ada:analyticalMode = N \u2014 quantitative point analyses and X-ray maps ('BSE images, element maps and quantitative compositional analyses'); WDS or EDS is not stated, and the list has no value without one.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "ada:beamDiameterDefault": "phosphates, carbonates: 2 \u00b5m; other: N \u2014 p.9",
      "ada:beamMode": "silicates, sulfides, oxides: Focused; phosphates, carbonates: Defocused \u2014 'Quantitative analyses of silicates, sulfides and oxides were run using a focused beam ... A 2-\u03bcm defocused beam size ... for phosphate and carbonate analyses'",
      "schema:manufacturer": {
        "schema:name": "Cameca",
        "@type": [
          "schema:Organization"
        ]
      },
      "ada:mappingBeamCurrentDefault": "20 nA \u2014 'X-ray maps and BSE images were run at 15kV and 20nA'",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        }
      ],
      "schema:name": "example instrumentName",
      "ada:mappingBeamDiameterDefault": -9999,
      "ada:mappingBeamMode": "missing"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "SX-100 Ultra (stated as \"SX-100 Ultra electron microprobe in the K-ALFAA\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/epmaTAPP/beamDamageMinimizationDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "beamDamageMinimizationDefault",
      "schema:name": "Beam Damage Minimization",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "phosphates, carbonates: 2 \u00b5m defocused beam, lower beam currents and shorter count times; other: N \u2014 'to minimize possible beam damage effects'"
    }
  ],
  "ada:edsAcquisitionMode": "N/A",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
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
          "schema:defaultValue": "SEM imaging and EDS mapping before the probe \u2014 particles were characterized by SE and BSE imaging and by EDS mapping of \"The compositional heterogeneity of the particles\" (p.9), and the paper's Fig. 1 pairs those BSE images with the EMPA data (p.2); the Methods list SEM before electron microprobe analysis without stating an explicit order"
        }
      ]
    }
  ],
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "silicates",
      "sulfides",
      "oxides",
      "phosphates",
      "carbonates"
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
        "@id": "ada:targetMaterialColumn/epmaTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "N \u2014 beam conditions are given per phase (\"Quantitative analyses of silicates, sulfides and oxides were run using a focused beam\"; \"A 2-\u03bcm defocused beam size, lower beam currents and shorter count times were used for phosphate and carbonate analyses\", p.9), but that is a setting per phase, not a rule for choosing which grains were analysed",
  "ada:monitoredElements": [
    "N \u2014 \"Well-characterized natural and synthetic materials were used as standards\" (p.9); the paper gives beam conditions and count times for silicates, sulfides, oxides, phosphates and carbonates but names no element"
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Kuiper-Arizona Laboratory for Astromaterials Analysis (K-ALFAA), University of Arizona"
  },
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA Planetary Science Enabling Facilities 80NSSC23K0327; NASA Planetary Major Equipment NNX12AL47G and NNX15AJ22G; NASA Early Career Award 80NSSC20K1087; NSF Major Research Instrumentation 1531243 and 0619599; Gordon and Betty Moore Foundation; State of Arizona Technology and Research Initiative Fund \u2014 acknowledged 'for supporting K-ALFAA operations' and 'for supporting the instrumentation in K-ALFAA'; which award bought the microprobe is not stated"
    }
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Zega et al. 2025, Nat. Geosci.; doi:10.1038/s41561-025-01741-0"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-EDS; TEM-EDS/EELS; FIB-SEM; XRD; XANES"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Grain > Phase \u2014 sulfide compositions are reported per grain within named particles (\"Pyrrhotite compositions measured by EMPA\", p.2), and \"phase mapping via electron microprobe analysis (EMPA)\" gives modal abundances of carbonates, sulfides and magnetite per particle (p.2)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "XMapTools (for phase maps)"
    }
  ],
  "ada:reportedProperties": [
    "Fe + Co, S, Ni; modal abundance of carbonates, sulfides and magnetite \u2014 sulfide compositions in at% (Fig. 1); modal abundances '0.4\u20133.4%, ~3\u20138% and ~3\u20135%' from the EMPA phase maps (p.2)"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "epma",
      "schema:termCode": "epma"
    }
  ],
  "schema:actionProcess": {
    "@type": [
      "schema:HowTo"
    ],
    "schema:name": "missing",
    "schema:step": [
      {
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:name": "Sample preparation",
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 1,
        "schema:description": "test value schema:description"
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:name": "Data reduction",
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
        "ada:detectionLimitMethod": "test value ada:detectionLimitMethod"
      }
    ]
  },
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "test value schema:defaultValue"
    }
  ],
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
  "schema:datePublished": "test value schema:datePublished"
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

<ex:epmaTAPP-Zega2025> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:name "missing" ;
            schema1:step [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:description "test value schema:description" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:detectionLimitMethod "test value ada:detectionLimitMethod" ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDamageMinimizationDefault> ;
    schema1:datePublished "test value schema:datePublished" ;
    schema1:description "Zega et al. 2025, Nat. Geosci. — mineralogical evidence for hydrothermal alteration of Bennu. K-ALFAA, University of Arizona. Instrument stated as \"SX-100 Ultra electron microprobe in the K-ALFAA\". IMPORTANT: v2 had \"no protocol details reported\" — this was WRONG. The paper provides detailed EPMA conditions: X-ray maps and BSE images: 15 kV, 20 nA. Silicates/sulfides/oxides: 15 kV, 20 nA, focused, 20 s peak, 10 s on each background. Phosphates: 15 kV, 8 nA, 2 µm defocused, 20 s peak and 10 s background. Carbonates: 15 kV, 4 nA, 2 µm defocused, 10 s peak and 5 s background. Standards: \"well-characterized natural and synthetic materials\" (specific names N). Phase maps generated using XMapTools. WDS and matrix correction NOT explicitly stated in paper. Reported detail: ada:edsAcquisitionMode = N — WDS or EDS is not stated; ada:analyticalMode = N — quantitative point analyses and X-ray maps ('BSE images, element maps and quantitative compositional analyses'); WDS or EDS is not stated, and the list has no value without one." ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NASA Planetary Science Enabling Facilities 80NSSC23K0327; NASA Planetary Major Equipment NNX12AL47G and NNX15AJ22G; NASA Early Career Award 80NSSC20K1087; NSF Major Research Instrumentation 1531243 and 0619599; Gordon and Betty Moore Foundation; State of Arizona Technology and Research Initiative Fund — acknowledged 'for supporting K-ALFAA operations' and 'for supporting the instrumentation in K-ALFAA'; which award bought the microprobe is not stated" ] ;
    schema1:instrument <ex:instrument/EPMA>,
        <ex:instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Kuiper-Arizona Laboratory for Astromaterials Analysis (K-ALFAA), University of Arizona" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "epma" ;
            schema1:termCode "epma" ] ;
    schema1:name "EPMA Major Element Silicates/Sulfides/Oxides/Phosphates/Carbonates, Bennu (K-ALFAA, Cameca SX-100 Ultra)" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Zega et al. 2025, Nat. Geosci.; doi:10.1038/s41561-025-01741-0" ] ;
            schema1:url "https://ada.astromat.org/missing" ],
        [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SEM-EDS; TEM-EDS/EELS; FIB-SEM; XRD; XANES" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "test value schema:defaultValue" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:edsAcquisitionMode "N/A" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:monitoredElements "N — \"Well-characterized natural and synthetic materials were used as standards\" (p.9); the paper gives beam conditions and count times for silicates, sulfides, oxides, phosphates and carbonates but names no element" ;
    ada:reportedProperties "Fe + Co, S, Ni; modal abundance of carbonates, sulfides and magnetite — sulfide compositions in at% (Fig. 1); modal abundances '0.4–3.4%, ~3–8% and ~3–5%' from the EMPA phase maps (p.2)" ;
    ada:samplingUnitSelectionCriteriaDefault "N — beam conditions are given per phase (\"Quantitative analyses of silicates, sulfides and oxides were run using a focused beam\"; \"A 2-μm defocused beam size, lower beam currents and shorter count times were used for phosphate and carbonate analyses\", p.9), but that is a setting per phase, not a rule for choosing which grains were analysed" ;
    ada:samplingUnitType "Grain > Phase — sulfide compositions are reported per grain within named particles (\"Pyrrhotite compositions measured by EMPA\", p.2), and \"phase mapping via electron microprobe analysis (EMPA)\" gives modal abundances of carbonates, sulfides and magnetite per particle (p.2)" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "carbonates",
                "oxides",
                "phosphates",
                "silicates",
                "sulfides" ;
            ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/backgroundCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/peakCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName> ] ;
    ada:wdsDeadTimeCorrection "missing" ;
    bios:computationalTool [ schema1:name "XMapTools (for phase maps)" ;
            ada:toolRole "dataReduction" ] .

<ex:instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:hasPart <ex:instrument/EPMA/part/EDS-Detector>,
        <ex:instrument/EPMA/part/Electron-Source>,
        <ex:instrument/EPMA/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Cameca" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "15 kV" ;
    ada:beamDiameterDefault "phosphates, carbonates: 2 µm; other: N — p.9" ;
    ada:beamMode "silicates, sulfides, oxides: Focused; phosphates, carbonates: Defocused — 'Quantitative analyses of silicates, sulfides and oxides were run using a focused beam ... A 2-μm defocused beam size ... for phosphate and carbonate analyses'" ;
    ada:mappingBeamCurrentDefault "20 nA — 'X-ray maps and BSE images were run at 15kV and 20nA'" ;
    ada:mappingBeamDiameterDefault -9999 ;
    ada:mappingBeamMode "missing" .

<ex:instrument/EPMA/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:name "missing" .

<ex:instrument/EPMA/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "missing" ;
    schema1:name "missing" .

<ex:instrument/EPMA/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "missing" .

<ex:instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "SX-100 Ultra (stated as \"SX-100 Ultra electron microprobe in the K-ALFAA\")" ] ;
    schema1:name "example instrumentName" .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/beamDamageMinimizationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "phosphates, carbonates: 2 µm defocused beam, lower beam currents and shorter count times; other: N — 'to minimize possible beam damage effects'" ;
    schema1:name "Beam Damage Minimization" ;
    schema1:valueName "beamDamageMinimizationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "SEM imaging and EDS mapping before the probe — particles were characterized by SE and BSE imaging and by EDS mapping of \"The compositional heterogeneity of the particles\" (p.9), and the paper's Fig. 1 pairs those BSE images with the EMPA data (p.2); the Methods list SEM before electron microprobe analysis without stating an explicit order" ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:valueName "preAnalysisImagingAndScreeningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/backgroundCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Background Counting Time" ;
    schema1:valueName "backgroundCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/peakCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Peak Counting Time" ;
    schema1:valueName "peakCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .


```


### epmaTAPP example Barnes2025
epmaTAPP instance derived from Barnes+2025 | JEOL JXA-8230 | WDS Point Analysis (CRPG Nancy).
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
  "@id": "ex:epmaTAPP-Barnes2025",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA Major Element Silicates/Oxides/Carbonates, Bennu Anhydrous Minerals (CRPG Nancy, JEOL JXA-8230)",
  "schema:description": "Barnes et al. 2025, Nat. Astron. — variety and origin of accreted materials in Bennu. Protocol 1 of 2: CRPG Nancy, JEOL JXA-8230. Instrument has 5 WDS spectrometers + 1 SDD EDS; per-analyte technique (WDS vs. EDS) not stated. Two analytical sessions: session 1 (no Na, K); session 2 (with Na, K). Counting times are stated as total peak + background combined: 200 ms for minor elements (Al, Ti, Ca, Mn, Cr) and 20 ms for major elements (Mg, Fe, Si). Full primary standard suite stated with element assignments. Full per-element detection limits stated. Matrix correction method not stated. Sample preparation done at Université Côte d'Azur (not at CRPG). Beam current not stated for NHM protocol; 3 nA mentioned in text is for SEM-EDS (different instrument). Reported detail: ada:edsAcquisitionMode = N — WDS or EDS is not stated; ada:analyticalMode = N — quantitative point analyses on an instrument 'equipped with five wavelength-dispersive spectrometers and one silicon drift detector energy dispersive spectrometer'; which detector measured which element is not stated.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "20 kV",
      "ada:beamDiameterDefault": "all: 1 µm — as above",
      "ada:beamMode": "carbonates: Rastered; other: N — 'For carbonates, we rastered the beam over 5×5 µm2'",
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "5 wavelength-dispersive spectrometers (JEOL)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:name": "example instrumentName",
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:mappingBeamDiameterDefault": -9999,
      "ada:mappingBeamMode": "missing"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "JXA-8230 (stated as \"JEOL JXA-8230 electron microprobe analyser (EPMA)\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Al",
      "Ti",
      "Ca",
      "Cr",
      "Mn",
      "Ni",
      "Mg",
      "Fe",
      "Si",
      "Na",
      "K"
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
        "@id": "ada:targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "targetSpeciesEstimationMethod",
        "schema:name": "Target Species Estimation Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalAccuracy",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracy",
        "schema:name": "Analytical Accuracy",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalPrecision",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalPrecision",
        "schema:name": "Analytical Precision",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayBackgroundCorrectionMethod",
        "schema:name": "X-ray Background Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/beamCurrent",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "beamCurrent",
        "schema:name": "Beam Current",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/blankCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "blankCorrection",
        "schema:name": "Blank Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionStandard",
        "schema:name": "Interference Correction Standard",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayLineOverlapCorrectionsApplied",
        "schema:name": "X-ray Line Overlap Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferingElements",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingElements",
        "schema:name": "Interfering Elements",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "timeDependentIntensityCorrection",
        "schema:name": "Time-Dependent Intensity Correction",
        "ada:dataType": "string"
      }
    ]
  },
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/epmaTAPP/beamRasterDimensionsDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "beamRasterDimensionsDefault",
      "schema:name": "Beam Raster Dimensions",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 5,
      "schema:description": "carbonates: 5 × 5 µm²; other: N/A — as above"
    }
  ],
  "ada:edsAcquisitionMode": "N/A",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
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
          "schema:defaultValue": "SEM imaging and multi-element EDS mapping — \"SEM observations were performed on the samples using a JEOL JSM-6510 with 3-nA primary beam at 15 kV. We also performed multi-element EDS mapping (Mg, Si, Fe, Ni, S, Na, Ca and Al) of the different grains\", after which \"Quantitative chemical analyses were performed using a JEOL JXA-8230 electron microprobe\" (p.11)"
        }
      ]
    }
  ],
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "carbonates"
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
        "@id": "ada:targetMaterialColumn/epmaTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "Size — \"Aggregate particles (<1 mm) were mounted in epoxy, polished and were subsequently carbon coated\" (p.11); the grains analysed within them are not otherwise chosen by a stated rule",
  "ada:monitoredElements": [
    "Al, Ti, Ca, Cr, Mn, Ni, Mg, Fe, Si, Na, K — as for Target Species"
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Centre de Recherches Pétrographiques et Géochimiques (CRPG), Nancy, France"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Barnes et al. 2025, Nat. Astron.; doi:10.1038/s41550-025-02631-6"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-BSE (JEOL JSM-6510, 15 kV, 3 nA); SEM-EDS (multi-element mapping); SIMS (CAMECA IMS 1270 E7, CRPG); NanoSIMS (K-ALFAA); ICP-MS; MC-ICP-MS; noble gas MS"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Grain > Analysis point — \"Aggregate particles (<1 mm) were mounted in epoxy\" and mapped \"of the different grains\"; \"Quantitative analyses were performed with ... beam diameter of 1 µm\", the beam rastered \"over 5 × 5 µm2\" for carbonates (p.11)",
  "ada:reportedProperties": [
    "Al, Ti, Ca, Cr, Mn, Ni, Mg, Fe, Si, Na, K — mineral compositions for the two element suites; values 'compiled in Supplementary Table 14', not in the archived PDF"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Aggregate particles (<1 mm) mounted in epoxy at Université Côte d'Azur; polished; carbon coated (thickness N)",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
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
      "schema:name": "epma",
      "schema:termCode": "epma"
    }
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "test value schema:defaultValue"
    }
  ],
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
  "schema:datePublished": "test value schema:datePublished"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:epmaTAPP-Barnes2025",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA Major Element Silicates/Oxides/Carbonates, Bennu Anhydrous Minerals (CRPG Nancy, JEOL JXA-8230)",
  "schema:description": "Barnes et al. 2025, Nat. Astron. \u2014 variety and origin of accreted materials in Bennu. Protocol 1 of 2: CRPG Nancy, JEOL JXA-8230. Instrument has 5 WDS spectrometers + 1 SDD EDS; per-analyte technique (WDS vs. EDS) not stated. Two analytical sessions: session 1 (no Na, K); session 2 (with Na, K). Counting times are stated as total peak + background combined: 200 ms for minor elements (Al, Ti, Ca, Mn, Cr) and 20 ms for major elements (Mg, Fe, Si). Full primary standard suite stated with element assignments. Full per-element detection limits stated. Matrix correction method not stated. Sample preparation done at Universit\u00e9 C\u00f4te d'Azur (not at CRPG). Beam current not stated for NHM protocol; 3 nA mentioned in text is for SEM-EDS (different instrument). Reported detail: ada:edsAcquisitionMode = N \u2014 WDS or EDS is not stated; ada:analyticalMode = N \u2014 quantitative point analyses on an instrument 'equipped with five wavelength-dispersive spectrometers and one silicon drift detector energy dispersive spectrometer'; which detector measured which element is not stated.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "20 kV",
      "ada:beamDiameterDefault": "all: 1 \u00b5m \u2014 as above",
      "ada:beamMode": "carbonates: Rastered; other: N \u2014 'For carbonates, we rastered the beam over 5\u00d75 \u00b5m2'",
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "5 wavelength-dispersive spectrometers (JEOL)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:name": "example instrumentName",
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:mappingBeamDiameterDefault": -9999,
      "ada:mappingBeamMode": "missing"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "JXA-8230 (stated as \"JEOL JXA-8230 electron microprobe analyser (EPMA)\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Al",
      "Ti",
      "Ca",
      "Cr",
      "Mn",
      "Ni",
      "Mg",
      "Fe",
      "Si",
      "Na",
      "K"
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
        "@id": "ada:targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "targetSpeciesEstimationMethod",
        "schema:name": "Target Species Estimation Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalAccuracy",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracy",
        "schema:name": "Analytical Accuracy",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalPrecision",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalPrecision",
        "schema:name": "Analytical Precision",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayBackgroundCorrectionMethod",
        "schema:name": "X-ray Background Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/beamCurrent",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "beamCurrent",
        "schema:name": "Beam Current",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/blankCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "blankCorrection",
        "schema:name": "Blank Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionStandard",
        "schema:name": "Interference Correction Standard",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayLineOverlapCorrectionsApplied",
        "schema:name": "X-ray Line Overlap Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferingElements",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingElements",
        "schema:name": "Interfering Elements",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "timeDependentIntensityCorrection",
        "schema:name": "Time-Dependent Intensity Correction",
        "ada:dataType": "string"
      }
    ]
  },
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/epmaTAPP/beamRasterDimensionsDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "beamRasterDimensionsDefault",
      "schema:name": "Beam Raster Dimensions",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 5,
      "schema:description": "carbonates: 5 \u00d7 5 \u00b5m\u00b2; other: N/A \u2014 as above"
    }
  ],
  "ada:edsAcquisitionMode": "N/A",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
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
          "schema:defaultValue": "SEM imaging and multi-element EDS mapping \u2014 \"SEM observations were performed on the samples using a JEOL JSM-6510 with 3-nA primary beam at 15 kV. We also performed multi-element EDS mapping (Mg, Si, Fe, Ni, S, Na, Ca and Al) of the different grains\", after which \"Quantitative chemical analyses were performed using a JEOL JXA-8230 electron microprobe\" (p.11)"
        }
      ]
    }
  ],
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "carbonates"
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
        "@id": "ada:targetMaterialColumn/epmaTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "Size \u2014 \"Aggregate particles (<1 mm) were mounted in epoxy, polished and were subsequently carbon coated\" (p.11); the grains analysed within them are not otherwise chosen by a stated rule",
  "ada:monitoredElements": [
    "Al, Ti, Ca, Cr, Mn, Ni, Mg, Fe, Si, Na, K \u2014 as for Target Species"
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Centre de Recherches P\u00e9trographiques et G\u00e9ochimiques (CRPG), Nancy, France"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Barnes et al. 2025, Nat. Astron.; doi:10.1038/s41550-025-02631-6"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-BSE (JEOL JSM-6510, 15 kV, 3 nA); SEM-EDS (multi-element mapping); SIMS (CAMECA IMS 1270 E7, CRPG); NanoSIMS (K-ALFAA); ICP-MS; MC-ICP-MS; noble gas MS"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Grain > Analysis point \u2014 \"Aggregate particles (<1 mm) were mounted in epoxy\" and mapped \"of the different grains\"; \"Quantitative analyses were performed with ... beam diameter of 1 \u00b5m\", the beam rastered \"over 5 \u00d7 5 \u00b5m2\" for carbonates (p.11)",
  "ada:reportedProperties": [
    "Al, Ti, Ca, Cr, Mn, Ni, Mg, Fe, Si, Na, K \u2014 mineral compositions for the two element suites; values 'compiled in Supplementary Table 14', not in the archived PDF"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Aggregate particles (<1 mm) mounted in epoxy at Universit\u00e9 C\u00f4te d'Azur; polished; carbon coated (thickness N)",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
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
      "schema:name": "epma",
      "schema:termCode": "epma"
    }
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "test value schema:defaultValue"
    }
  ],
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
  "schema:datePublished": "test value schema:datePublished"
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

<ex:epmaTAPP-Barnes2025> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:description "Aggregate particles (<1 mm) mounted in epoxy at Université Côte d'Azur; polished; carbon coated (thickness N)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:detectionLimitMethod "test value ada:detectionLimitMethod" ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamRasterDimensionsDefault> ;
    schema1:datePublished "test value schema:datePublished" ;
    schema1:description "Barnes et al. 2025, Nat. Astron. — variety and origin of accreted materials in Bennu. Protocol 1 of 2: CRPG Nancy, JEOL JXA-8230. Instrument has 5 WDS spectrometers + 1 SDD EDS; per-analyte technique (WDS vs. EDS) not stated. Two analytical sessions: session 1 (no Na, K); session 2 (with Na, K). Counting times are stated as total peak + background combined: 200 ms for minor elements (Al, Ti, Ca, Mn, Cr) and 20 ms for major elements (Mg, Fe, Si). Full primary standard suite stated with element assignments. Full per-element detection limits stated. Matrix correction method not stated. Sample preparation done at Université Côte d'Azur (not at CRPG). Beam current not stated for NHM protocol; 3 nA mentioned in text is for SEM-EDS (different instrument). Reported detail: ada:edsAcquisitionMode = N — WDS or EDS is not stated; ada:analyticalMode = N — quantitative point analyses on an instrument 'equipped with five wavelength-dispersive spectrometers and one silicon drift detector energy dispersive spectrometer'; which detector measured which element is not stated." ;
    schema1:instrument <ex:instrument/EPMA>,
        <ex:instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Centre de Recherches Pétrographiques et Géochimiques (CRPG), Nancy, France" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "epma" ;
            schema1:termCode "epma" ] ;
    schema1:name "EPMA Major Element Silicates/Oxides/Carbonates, Bennu Anhydrous Minerals (CRPG Nancy, JEOL JXA-8230)" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Barnes et al. 2025, Nat. Astron.; doi:10.1038/s41550-025-02631-6" ] ;
            schema1:url "https://ada.astromat.org/missing" ],
        [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SEM-BSE (JEOL JSM-6510, 15 kV, 3 nA); SEM-EDS (multi-element mapping); SIMS (CAMECA IMS 1270 E7, CRPG); NanoSIMS (K-ALFAA); ICP-MS; MC-ICP-MS; noble gas MS" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "test value schema:defaultValue" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:edsAcquisitionMode "N/A" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:monitoredElements "Al, Ti, Ca, Cr, Mn, Ni, Mg, Fe, Si, Na, K — as for Target Species" ;
    ada:reportedProperties "Al, Ti, Ca, Cr, Mn, Ni, Mg, Fe, Si, Na, K — mineral compositions for the two element suites; values 'compiled in Supplementary Table 14', not in the archived PDF" ;
    ada:samplingUnitSelectionCriteriaDefault "Size — \"Aggregate particles (<1 mm) were mounted in epoxy, polished and were subsequently carbon coated\" (p.11); the grains analysed within them are not otherwise chosen by a stated rule" ;
    ada:samplingUnitType "Grain > Analysis point — \"Aggregate particles (<1 mm) were mounted in epoxy\" and mapped \"of the different grains\"; \"Quantitative analyses were performed with ... beam diameter of 1 µm\", the beam rastered \"over 5 × 5 µm2\" for carbonates (p.11)" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "carbonates" ;
            ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/backgroundCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/peakCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName> ] ;
    ada:targetSpeciesTemplate [ ada:defaultTargetSpecies "Al",
                "Ca",
                "Cr",
                "Fe",
                "K",
                "Mg",
                "Mn",
                "Na",
                "Ni",
                "Si",
                "Ti" ;
            ada:targetSpeciesColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetSpecies" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalAccuracy>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalPrecision>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/beamCurrent>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/blankCorrection>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferingElements>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied> ] ;
    ada:wdsDeadTimeCorrection "missing" .

<ex:instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:hasPart <ex:instrument/EPMA/part/EDS-Detector>,
        <ex:instrument/EPMA/part/Electron-Source>,
        <ex:instrument/EPMA/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "JEOL" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "20 kV" ;
    ada:beamDiameterDefault "all: 1 µm — as above" ;
    ada:beamMode "carbonates: Rastered; other: N — 'For carbonates, we rastered the beam over 5×5 µm2'" ;
    ada:mappingBeamCurrentDefault -9999 ;
    ada:mappingBeamDiameterDefault -9999 ;
    ada:mappingBeamMode "missing" .

<ex:instrument/EPMA/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:name "missing" .

<ex:instrument/EPMA/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "missing" ;
    schema1:name "missing" .

<ex:instrument/EPMA/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "5 wavelength-dispersive spectrometers (JEOL)" .

<ex:instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "JXA-8230 (stated as \"JEOL JXA-8230 electron microprobe analyser (EPMA)\")" ] ;
    schema1:name "example instrumentName" .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/beamRasterDimensionsDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 5 ;
    schema1:description "carbonates: 5 × 5 µm²; other: N/A — as above" ;
    schema1:name "Beam Raster Dimensions" ;
    schema1:valueName "beamRasterDimensionsDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "SEM imaging and multi-element EDS mapping — \"SEM observations were performed on the samples using a JEOL JSM-6510 with 3-nA primary beam at 15 kV. We also performed multi-element EDS mapping (Mg, Si, Fe, Ni, S, Na, Ca and Al) of the different grains\", after which \"Quantitative chemical analyses were performed using a JEOL JXA-8230 electron microprobe\" (p.11)" ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:valueName "preAnalysisImagingAndScreeningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/backgroundCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Background Counting Time" ;
    schema1:valueName "backgroundCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/peakCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Peak Counting Time" ;
    schema1:valueName "peakCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalAccuracy> a schema1:PropertyValueSpecification ;
    schema1:name "Analytical Accuracy" ;
    schema1:valueName "analyticalAccuracy" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalPrecision> a schema1:PropertyValueSpecification ;
    schema1:name "Analytical Precision" ;
    schema1:valueName "analyticalPrecision" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/beamCurrent> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Beam Current" ;
    schema1:valueName "beamCurrent" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/blankCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Blank Correction" ;
    schema1:valueName "blankCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard> a schema1:PropertyValueSpecification ;
    schema1:name "Interference Correction Standard" ;
    schema1:valueName "interferenceCorrectionStandard" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferingElements> a schema1:PropertyValueSpecification ;
    schema1:name "Interfering Elements" ;
    schema1:valueName "interferingElements" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Target Species Estimation Method" ;
    schema1:valueName "targetSpeciesEstimationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Time-Dependent Intensity Correction" ;
    schema1:valueName "timeDependentIntensityCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "X-ray Background Correction Method" ;
    schema1:valueName "xRayBackgroundCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "X-ray Line Overlap Corrections Applied" ;
    schema1:valueName "xRayLineOverlapCorrectionsApplied" ;
    ada:dataType "string" .


```


### epmaTAPP example Barnes2025-2
epmaTAPP instance derived from Barnes+2025 | Cameca SX100 | WDS Point Analysis (NHM London).
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
  "@id": "ex:epmaTAPP-Barnes2025-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA Major/Minor Element Anhydrous Silicates, Bennu (NHM London, Cameca SX100)",
  "schema:description": "Barnes et al. 2025, Nat. Astron. — variety and origin of accreted materials in Bennu. Protocol 2 of 2: NHM London, CAMECA SX100. Stated instrument: \"CAMECA SX100 electron microprobe\". Target minerals: olivine and pyroxene (anhydrous silicates). 20 kV, 1 µm focused beam. Beam current not stated for EPMA (3 nA in text refers to SEM-EDS on separate Zeiss EVO instrument). Detection limits ~250 ppm for transition metals. Standards, matrix correction, WDS spectrometer details not stated. Analyte list not given. SEM-EDS at NHM is a separate instrument (Zeiss EVO 15LS + Oxford X-Max80) calibrated at 20 kV, 3 nA. Carbon coat: initial coat for SEM/EPMA (thickness N); additional coat to ~30 nm total was for subsequent SIMS, not EPMA. Reported detail: ada:edsAcquisitionMode = N — WDS or EDS is not stated; ada:analyticalMode = N — point analyses ('Analyses were performed at 20 kV, using a focused 1-μm beam'); WDS or EDS is not stated, and the list has no value without one.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "20 kV",
      "ada:beamDiameterDefault": "all: 1 µm — as above",
      "ada:beamMode": "all: Focused — 'Analyses were performed at 20 kV, using a focused 1-μm beam'",
      "schema:manufacturer": {
        "schema:name": "Cameca",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        }
      ],
      "schema:name": "example instrumentName",
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:mappingBeamDiameterDefault": -9999,
      "ada:mappingBeamMode": "missing"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "SX100 (stated as \"CAMECA SX100 electron microprobe\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:edsAcquisitionMode": "N/A",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
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
          "schema:defaultValue": "SEM characterisation at the NHM — \"Olivine and pyroxene grains were identified and characterized at the NHM\" and \"Following characterization by SEM/EPMA, an additional carbon coat was added for a total thickness of ~30 nm\" (p.13); additional quantitative data came from a Zeiss EVO 15LS analytical SEM with an Oxford X-Max80 EDS (p.13)"
        }
      ]
    }
  ],
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "olivine",
      "pyroxene"
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
        "@id": "ada:targetMaterialColumn/epmaTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "Phase identity — \"Olivine and pyroxene grains were identified and characterized at the NHM\" (p.13), the paper's target being the anhydrous silicates in particles P1 and P2",
  "ada:monitoredElements": [
    "N — the paper gives beam conditions and a detection limit for transition metals of about 250 ppm for the NHM London instrument (p.13) but names no element"
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Natural History Museum (NHM), London, UK"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Barnes et al. 2025, Nat. Astron.; doi:10.1038/s41550-025-02631-6"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-EDS (Zeiss EVO 15LS + Oxford X-Max80, 20 kV, 3 nA); NanoSIMS (OU); SIMS (CAMECA ims-1280-HR, Hokkaido); laser fluorination O isotopes (OU)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Grain > Analysis point — \"Olivine and pyroxene grains were identified and characterized at the NHM\" in particles P1 and P2, and \"Analyses were performed at 20 kV, using a focused 1-μm beam\" (p.13)",
  "ada:reportedProperties": [
    "major and minor element abundances; Mg# — 'Major and minor element abundances' of olivine and pyroxene; 'the Mg# of olivine grains is >83' (p.13)"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Mounted in resin blocks; polished at NHM London; fragmented during polishing (P1, P2); initial carbon coat for SEM/EPMA (thickness N); additional coat added after for SIMS (total ~30 nm)",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
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
      "schema:name": "epma",
      "schema:termCode": "epma"
    }
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "test value schema:defaultValue"
    }
  ],
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
  "schema:datePublished": "test value schema:datePublished"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:epmaTAPP-Barnes2025-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA Major/Minor Element Anhydrous Silicates, Bennu (NHM London, Cameca SX100)",
  "schema:description": "Barnes et al. 2025, Nat. Astron. \u2014 variety and origin of accreted materials in Bennu. Protocol 2 of 2: NHM London, CAMECA SX100. Stated instrument: \"CAMECA SX100 electron microprobe\". Target minerals: olivine and pyroxene (anhydrous silicates). 20 kV, 1 \u00b5m focused beam. Beam current not stated for EPMA (3 nA in text refers to SEM-EDS on separate Zeiss EVO instrument). Detection limits ~250 ppm for transition metals. Standards, matrix correction, WDS spectrometer details not stated. Analyte list not given. SEM-EDS at NHM is a separate instrument (Zeiss EVO 15LS + Oxford X-Max80) calibrated at 20 kV, 3 nA. Carbon coat: initial coat for SEM/EPMA (thickness N); additional coat to ~30 nm total was for subsequent SIMS, not EPMA. Reported detail: ada:edsAcquisitionMode = N \u2014 WDS or EDS is not stated; ada:analyticalMode = N \u2014 point analyses ('Analyses were performed at 20 kV, using a focused 1-\u03bcm beam'); WDS or EDS is not stated, and the list has no value without one.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "20 kV",
      "ada:beamDiameterDefault": "all: 1 \u00b5m \u2014 as above",
      "ada:beamMode": "all: Focused \u2014 'Analyses were performed at 20 kV, using a focused 1-\u03bcm beam'",
      "schema:manufacturer": {
        "schema:name": "Cameca",
        "@type": [
          "schema:Organization"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/EDS-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        }
      ],
      "schema:name": "example instrumentName",
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:mappingBeamDiameterDefault": -9999,
      "ada:mappingBeamMode": "missing"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "SX100 (stated as \"CAMECA SX100 electron microprobe\")",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:edsAcquisitionMode": "N/A",
  "schema:object": [
    {
      "@type": [
        "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample",
        "schema:DefinedTerm",
        "schema:Thing"
      ],
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
          "schema:defaultValue": "SEM characterisation at the NHM \u2014 \"Olivine and pyroxene grains were identified and characterized at the NHM\" and \"Following characterization by SEM/EPMA, an additional carbon coat was added for a total thickness of ~30 nm\" (p.13); additional quantitative data came from a Zeiss EVO 15LS analytical SEM with an Oxford X-Max80 EDS (p.13)"
        }
      ]
    }
  ],
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "olivine",
      "pyroxene"
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
        "@id": "ada:targetMaterialColumn/epmaTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "Phase identity \u2014 \"Olivine and pyroxene grains were identified and characterized at the NHM\" (p.13), the paper's target being the anhydrous silicates in particles P1 and P2",
  "ada:monitoredElements": [
    "N \u2014 the paper gives beam conditions and a detection limit for transition metals of about 250 ppm for the NHM London instrument (p.13) but names no element"
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Natural History Museum (NHM), London, UK"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Barnes et al. 2025, Nat. Astron.; doi:10.1038/s41550-025-02631-6"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-EDS (Zeiss EVO 15LS + Oxford X-Max80, 20 kV, 3 nA); NanoSIMS (OU); SIMS (CAMECA ims-1280-HR, Hokkaido); laser fluorination O isotopes (OU)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Grain > Analysis point \u2014 \"Olivine and pyroxene grains were identified and characterized at the NHM\" in particles P1 and P2, and \"Analyses were performed at 20 kV, using a focused 1-\u03bcm beam\" (p.13)",
  "ada:reportedProperties": [
    "major and minor element abundances; Mg# \u2014 'Major and minor element abundances' of olivine and pyroxene; 'the Mg# of olivine grains is >83' (p.13)"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Mounted in resin blocks; polished at NHM London; fragmented during polishing (P1, P2); initial carbon coat for SEM/EPMA (thickness N); additional coat added after for SIMS (total ~30 nm)",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
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
      "schema:name": "epma",
      "schema:termCode": "epma"
    }
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "test value schema:defaultValue"
    }
  ],
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
  "schema:datePublished": "test value schema:datePublished"
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

<ex:epmaTAPP-Barnes2025-2> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:detectionLimitMethod "test value ada:detectionLimitMethod" ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:description "Mounted in resin blocks; polished at NHM London; fragmented during polishing (P1, P2); initial carbon coat for SEM/EPMA (thickness N); additional coat added after for SIMS (total ~30 nm)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:datePublished "test value schema:datePublished" ;
    schema1:description "Barnes et al. 2025, Nat. Astron. — variety and origin of accreted materials in Bennu. Protocol 2 of 2: NHM London, CAMECA SX100. Stated instrument: \"CAMECA SX100 electron microprobe\". Target minerals: olivine and pyroxene (anhydrous silicates). 20 kV, 1 µm focused beam. Beam current not stated for EPMA (3 nA in text refers to SEM-EDS on separate Zeiss EVO instrument). Detection limits ~250 ppm for transition metals. Standards, matrix correction, WDS spectrometer details not stated. Analyte list not given. SEM-EDS at NHM is a separate instrument (Zeiss EVO 15LS + Oxford X-Max80) calibrated at 20 kV, 3 nA. Carbon coat: initial coat for SEM/EPMA (thickness N); additional coat to ~30 nm total was for subsequent SIMS, not EPMA. Reported detail: ada:edsAcquisitionMode = N — WDS or EDS is not stated; ada:analyticalMode = N — point analyses ('Analyses were performed at 20 kV, using a focused 1-μm beam'); WDS or EDS is not stated, and the list has no value without one." ;
    schema1:instrument <ex:instrument/EPMA>,
        <ex:instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Natural History Museum (NHM), London, UK" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "epma" ;
            schema1:termCode "epma" ] ;
    schema1:name "EPMA Major/Minor Element Anhydrous Silicates, Bennu (NHM London, Cameca SX100)" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Barnes et al. 2025, Nat. Astron.; doi:10.1038/s41550-025-02631-6" ] ;
            schema1:url "https://ada.astromat.org/missing" ],
        [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SEM-EDS (Zeiss EVO 15LS + Oxford X-Max80, 20 kV, 3 nA); NanoSIMS (OU); SIMS (CAMECA ims-1280-HR, Hokkaido); laser fluorination O isotopes (OU)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "test value schema:defaultValue" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:edsAcquisitionMode "N/A" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:monitoredElements "N — the paper gives beam conditions and a detection limit for transition metals of about 250 ppm for the NHM London instrument (p.13) but names no element" ;
    ada:reportedProperties "major and minor element abundances; Mg# — 'Major and minor element abundances' of olivine and pyroxene; 'the Mg# of olivine grains is >83' (p.13)" ;
    ada:samplingUnitSelectionCriteriaDefault "Phase identity — \"Olivine and pyroxene grains were identified and characterized at the NHM\" (p.13), the paper's target being the anhydrous silicates in particles P1 and P2" ;
    ada:samplingUnitType "Grain > Analysis point — \"Olivine and pyroxene grains were identified and characterized at the NHM\" in particles P1 and P2, and \"Analyses were performed at 20 kV, using a focused 1-μm beam\" (p.13)" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "olivine",
                "pyroxene" ;
            ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/backgroundCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/peakCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName> ] ;
    ada:wdsDeadTimeCorrection "missing" .

<ex:instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:hasPart <ex:instrument/EPMA/part/EDS-Detector>,
        <ex:instrument/EPMA/part/Electron-Source>,
        <ex:instrument/EPMA/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Cameca" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "20 kV" ;
    ada:beamDiameterDefault "all: 1 µm — as above" ;
    ada:beamMode "all: Focused — 'Analyses were performed at 20 kV, using a focused 1-μm beam'" ;
    ada:mappingBeamCurrentDefault -9999 ;
    ada:mappingBeamDiameterDefault -9999 ;
    ada:mappingBeamMode "missing" .

<ex:instrument/EPMA/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:name "missing" .

<ex:instrument/EPMA/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "missing" ;
    schema1:name "missing" .

<ex:instrument/EPMA/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "missing" .

<ex:instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "SX100 (stated as \"CAMECA SX100 electron microprobe\")" ] ;
    schema1:name "example instrumentName" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "SEM characterisation at the NHM — \"Olivine and pyroxene grains were identified and characterized at the NHM\" and \"Following characterization by SEM/EPMA, an additional carbon coat was added for a total thickness of ~30 nm\" (p.13); additional quantitative data came from a Zeiss EVO 15LS analytical SEM with an Oxford X-Max80 EDS (p.13)" ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:valueName "preAnalysisImagingAndScreeningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/backgroundCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Background Counting Time" ;
    schema1:valueName "backgroundCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/peakCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Peak Counting Time" ;
    schema1:valueName "peakCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .


```


### epmaTAPP example Neuman2025
epmaTAPP instance derived from Neuman+2025 | WashU St. Louis | WDS Mapping (JEOL JXA-8200).
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
  "@id": "ex:epmaTAPP-Neuman2025",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS quantitative compositional mapping, Apollo 17 core 73001 continuous thin sections (Washington University in St. Louis)",
  "schema:description": "Multi-pass WDS mapping: two passes per stage map, five elements each; 18 hr per map; 20 x 10^6 fully quantitative analyses across all slides. Recorded in the acquisition-pass proposal (2026-09-08) as the evidence that EPMA partitions the target-species domain across passes. Reported detail: ada:matrixCorrectionMethod = Full Phi(rho-z) correction applied at each pixel, of the form C = k x ZAF, where ZAF is the compositionally dependent correction for atomic number, X-ray absorption and characteristic fluorescence in both sample and standard; ada:analyticalMode = WDS Mapping — 'five EPMA stage maps were acquired using fixed wavelength-dispersive spectrometers (WDS)'.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV (stage maps and BSE mosaic)",
      "ada:beamDiameterDefault": "N/A — mapping-only procedure; map beam under Mapping Beam Diameter",
      "ada:beamMode": "N/A — mapping-only procedure; map conditions under Mapping Beam Mode",
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "N/A — WDS mapping procedure",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/EPMA/part/EDS-Detector",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "Fixed wavelength-dispersive spectrometers; count not stated (five elements collected per pass)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "ada:mappingBeamMode": "Fixed 10 µm beam (stated 'a fixed 10 um electron beam')",
      "ada:mappingBeamCurrentDefault": "100 nA probe current (stage maps)",
      "ada:mappingBeamDiameterDefault": "10 µm (fixed)",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "JEOL JXA-8200",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Mg",
      "Al",
      "Fe",
      "Ca",
      "Ti",
      "Na",
      "Si",
      "Mn",
      "K",
      "Cr"
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
        "@id": "ada:targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "targetSpeciesEstimationMethod",
        "schema:name": "Target Species Estimation Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalAccuracy",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracy",
        "schema:name": "Analytical Accuracy",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalPrecision",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalPrecision",
        "schema:name": "Analytical Precision",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayBackgroundCorrectionMethod",
        "schema:name": "X-ray Background Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/beamCurrent",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "beamCurrent",
        "schema:name": "Beam Current",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/blankCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "blankCorrection",
        "schema:name": "Blank Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionStandard",
        "schema:name": "Interference Correction Standard",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayLineOverlapCorrectionsApplied",
        "schema:name": "X-ray Line Overlap Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferingElements",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingElements",
        "schema:name": "Interfering Elements",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "timeDependentIntensityCorrection",
        "schema:name": "Time-Dependent Intensity Correction",
        "ada:dataType": "string"
      }
    ]
  },
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/epmaTAPP/beamRasterDimensionsDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "beamRasterDimensionsDefault",
      "schema:name": "Beam Raster Dimensions",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N/A — stage scan, not beam scan"
    },
    {
      "@id": "ada:parameter/epmaTAPP/stageScanVsBeamScan",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/epmaTAPP/stageScanVsBeamScan"
        }
      ],
      "schema:name": "Stage Scan vs. Beam Scan",
      "schema:value": "Stage scan (stated 'EPMA stage maps')"
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
          "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "preAnalysisImagingAndScreeningDefault",
          "schema:name": "Pre-Analysis Imaging and Screening",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "BSE mosaic: approximately 325 backscattered-electron images collected with the JEOL guide-net mapping software at 15 kV, 2 nA probe current and 70x magnification, stitched with the ImageJ Fiji grid-collection stitching plug-in (Donovan et al., 2021) into a 20k x 5k pixel mosaic at ~1.5 um pixel resolution"
        }
      ]
    }
  ],
  "ada:matrixCorrectionMethod": "ZAF",
  "ada:stepSizePixelSizeDefault": "9.5 um (stage maps); ~1.5 um per pixel (BSE mosaic)",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "lunar regolith"
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
        "@id": "ada:targetMaterialColumn/epmaTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "N - continuous thin sections of the whole core; five stage maps per section, no selection rule stated",
  "ada:monitoredElements": [
    "Mg, Al, Fe, Ca, Ti, Na, Si, Mn, K, Cr — 'Two passes were used to collect X-ray intensities for Mg, Al, Fe, Ca, and Ti in pass 1, and Na, Si, Mn, K, and Cr in pass 2' (p.6)"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "EPMA-WDS"
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
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Neuman et al. 2025, J. Geophys. Res. Planets 130, e2024JE008556; doi:10.1029/2024JE008556 (section 2.6)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "BSE mosaic imaging (same JEOL JXA-8200); QEMSCAN (FEI QUANTA 650 FEG-SEM, Univ. Manchester); optical microscopy (Keyence VHX 7000, NASA JSC); micro-XCT (custom NSI instrument, UTCT)",
        "schema:description": "Single-element and RGB composite X-ray maps are compared with BSE and optical image mosaics (reflected light, plane polarized, crossed polars) to discriminate crystalline from glassy phases; an Al-Mg-Fe RGB composite X-ray map is used to discriminate feldspathic (red) from ferromagnesian (green and blue) phases"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Analysis point - each map pixel is a fully quantitative analysis (1,024 x 1,024 per stage map; five stage maps per thin section; 20 x 10^6 analyses across all slides)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "acquisition",
      "schema:name": "JEOL guide-net mapping software (BSE mosaic); N for the WDS stage maps"
    },
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Probe Software CalcImage and Probe for EPMA (full Phi(rho-z) correction at each pixel); MATLAB routines generating 32-bit floating point .tiff quantitative maps; Fiji and MATLAB for stitching; ENVI input image stacks"
    }
  ],
  "ada:analyticalMode": [
    "WDS Mapping"
  ],
  "ada:reportedProperties": [
    "element wt% maps; oxide wt% maps; cation stoichiometry; mineral endmember maps — 32-bit floating point .tiff"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Core extruded and dissected in 0.5 cm depth intervals; the remaining material impregnated with epoxy to create a continuous thin section set of the entire core; sections are 50 x 25 mm. Carbon coating N",
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
        "schema:name": "Data reduction",
        "ada:detectionLimitMethod": "N — attributed to the MAN background correction dedicating all map collection time to on-peak measurement, 'which improves precision and detection limits'",
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
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "test value schema:defaultValue"
    }
  ],
  "ada:edsAcquisitionMode": "missing",
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:wdsDeadTimeCorrection": "missing",
  "schema:datePublished": "test value schema:datePublished"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:epmaTAPP-Neuman2025",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "EPMA-WDS quantitative compositional mapping, Apollo 17 core 73001 continuous thin sections (Washington University in St. Louis)",
  "schema:description": "Multi-pass WDS mapping: two passes per stage map, five elements each; 18 hr per map; 20 x 10^6 fully quantitative analyses across all slides. Recorded in the acquisition-pass proposal (2026-09-08) as the evidence that EPMA partitions the target-species domain across passes. Reported detail: ada:matrixCorrectionMethod = Full Phi(rho-z) correction applied at each pixel, of the form C = k x ZAF, where ZAF is the compositionally dependent correction for atomic number, X-ray absorption and characteristic fluorescence in both sample and standard; ada:analyticalMode = WDS Mapping \u2014 'five EPMA stage maps were acquired using fixed wavelength-dispersive spectrometers (WDS)'.",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "EPMA",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV (stage maps and BSE mosaic)",
      "ada:beamDiameterDefault": "N/A \u2014 mapping-only procedure; map beam under Mapping Beam Diameter",
      "ada:beamMode": "N/A \u2014 mapping-only procedure; map conditions under Mapping Beam Mode",
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "N/A \u2014 WDS mapping procedure",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/EPMA/part/EDS-Detector",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "WDS Spectrometer",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "Fixed wavelength-dispersive spectrometers; count not stated (five elements collected per pass)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/EPMA/part/WDS-Spectrometer"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/EPMA/part/Electron-Source",
          "schema:description": "missing"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "ada:mappingBeamMode": "Fixed 10 \u00b5m beam (stated 'a fixed 10 um electron beam')",
      "ada:mappingBeamCurrentDefault": "100 nA probe current (stage maps)",
      "ada:mappingBeamDiameterDefault": "10 \u00b5m (fixed)",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/EPMA",
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:model": {
        "schema:name": "JEOL JXA-8200",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "Mg",
      "Al",
      "Fe",
      "Ca",
      "Ti",
      "Na",
      "Si",
      "Mn",
      "K",
      "Cr"
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
        "@id": "ada:targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "targetSpeciesEstimationMethod",
        "schema:name": "Target Species Estimation Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalAccuracy",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracy",
        "schema:name": "Analytical Accuracy",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/analyticalPrecision",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalPrecision",
        "schema:name": "Analytical Precision",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayBackgroundCorrectionMethod",
        "schema:name": "X-ray Background Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/beamCurrent",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "beamCurrent",
        "schema:name": "Beam Current",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/blankCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "blankCorrection",
        "schema:name": "Blank Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionStandard",
        "schema:name": "Interference Correction Standard",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayLineOverlapCorrectionsApplied",
        "schema:name": "X-ray Line Overlap Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/interferingElements",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingElements",
        "schema:name": "Interfering Elements",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "timeDependentIntensityCorrection",
        "schema:name": "Time-Dependent Intensity Correction",
        "ada:dataType": "string"
      }
    ]
  },
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/epmaTAPP/beamRasterDimensionsDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "beamRasterDimensionsDefault",
      "schema:name": "Beam Raster Dimensions",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N/A \u2014 stage scan, not beam scan"
    },
    {
      "@id": "ada:parameter/epmaTAPP/stageScanVsBeamScan",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/epmaTAPP/stageScanVsBeamScan"
        }
      ],
      "schema:name": "Stage Scan vs. Beam Scan",
      "schema:value": "Stage scan (stated 'EPMA stage maps')"
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
          "@id": "ada:parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault",
          "@type": [
            "schema:PropertyValueSpecification"
          ],
          "schema:valueName": "preAnalysisImagingAndScreeningDefault",
          "schema:name": "Pre-Analysis Imaging and Screening",
          "ada:dataType": "string",
          "ada:fieldScope": "session",
          "schema:defaultValue": "BSE mosaic: approximately 325 backscattered-electron images collected with the JEOL guide-net mapping software at 15 kV, 2 nA probe current and 70x magnification, stitched with the ImageJ Fiji grid-collection stitching plug-in (Donovan et al., 2021) into a 20k x 5k pixel mosaic at ~1.5 um pixel resolution"
        }
      ]
    }
  ],
  "ada:matrixCorrectionMethod": "ZAF",
  "ada:stepSizePixelSizeDefault": "9.5 um (stage maps); ~1.5 um per pixel (BSE mosaic)",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "lunar regolith"
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
        "@id": "ada:targetMaterialColumn/epmaTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "N - continuous thin sections of the whole core; five stage maps per section, no selection rule stated",
  "ada:monitoredElements": [
    "Mg, Al, Fe, Ca, Ti, Na, Si, Mn, K, Cr \u2014 'Two passes were used to collect X-ray intensities for Mg, Al, Fe, Ca, and Ti in pass 1, and Na, Si, Mn, K, and Cr in pass 2' (p.6)"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "EPMA-WDS"
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
      "schema:linkRelationship": "techniquePublication",
      "schema:target": {
        "schema:name": "Neuman et al. 2025, J. Geophys. Res. Planets 130, e2024JE008556; doi:10.1029/2024JE008556 (section 2.6)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    },
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "BSE mosaic imaging (same JEOL JXA-8200); QEMSCAN (FEI QUANTA 650 FEG-SEM, Univ. Manchester); optical microscopy (Keyence VHX 7000, NASA JSC); micro-XCT (custom NSI instrument, UTCT)",
        "schema:description": "Single-element and RGB composite X-ray maps are compared with BSE and optical image mosaics (reflected light, plane polarized, crossed polars) to discriminate crystalline from glassy phases; an Al-Mg-Fe RGB composite X-ray map is used to discriminate feldspathic (red) from ferromagnesian (green and blue) phases"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Analysis point - each map pixel is a fully quantitative analysis (1,024 x 1,024 per stage map; five stage maps per thin section; 20 x 10^6 analyses across all slides)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "acquisition",
      "schema:name": "JEOL guide-net mapping software (BSE mosaic); N for the WDS stage maps"
    },
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Probe Software CalcImage and Probe for EPMA (full Phi(rho-z) correction at each pixel); MATLAB routines generating 32-bit floating point .tiff quantitative maps; Fiji and MATLAB for stitching; ENVI input image stacks"
    }
  ],
  "ada:analyticalMode": [
    "WDS Mapping"
  ],
  "ada:reportedProperties": [
    "element wt% maps; oxide wt% maps; cation stoichiometry; mineral endmember maps \u2014 32-bit floating point .tiff"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Core extruded and dissected in 0.5 cm depth intervals; the remaining material impregnated with epoxy to create a continuous thin section set of the entire core; sections are 50 x 25 mm. Carbon coating N",
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
        "schema:name": "Data reduction",
        "ada:detectionLimitMethod": "N \u2014 attributed to the MAN background correction dedicating all map collection time to on-peak measurement, 'which improves precision and detection limits'",
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
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "test value schema:defaultValue"
    }
  ],
  "ada:edsAcquisitionMode": "missing",
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:wdsDeadTimeCorrection": "missing",
  "schema:datePublished": "test value schema:datePublished"
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

<ex:epmaTAPP-Neuman2025> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:description "Core extruded and dissected in 0.5 cm depth intervals; the remaining material impregnated with epoxy to create a continuous thin section set of the entire core; sections are 50 x 25 mm. Carbon coating N" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:detectionLimitMethod "N — attributed to the MAN background correction dedicating all map collection time to on-peak measurement, 'which improves precision and detection limits'" ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/epmaTAPP/beamRasterDimensionsDefault>,
        <https://ada.astromat.org/metadata/parameter/epmaTAPP/stageScanVsBeamScan> ;
    schema1:datePublished "test value schema:datePublished" ;
    schema1:description "Multi-pass WDS mapping: two passes per stage map, five elements each; 18 hr per map; 20 x 10^6 fully quantitative analyses across all slides. Recorded in the acquisition-pass proposal (2026-09-08) as the evidence that EPMA partitions the target-species domain across passes. Reported detail: ada:matrixCorrectionMethod = Full Phi(rho-z) correction applied at each pixel, of the form C = k x ZAF, where ZAF is the compositionally dependent correction for atomic number, X-ray absorption and characteristic fluorescence in both sample and standard; ada:analyticalMode = WDS Mapping — 'five EPMA stage maps were acquired using fixed wavelength-dispersive spectrometers (WDS)'." ;
    schema1:instrument <ex:instrument/EPMA>,
        <ex:instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Washington University in St. Louis" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "EPMA-WDS" ] ;
    schema1:name "EPMA-WDS quantitative compositional mapping, Apollo 17 core 73001 continuous thin sections (Washington University in St. Louis)" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "techniquePublication" ;
            schema1:target [ schema1:name "Neuman et al. 2025, J. Geophys. Res. Planets 130, e2024JE008556; doi:10.1029/2024JE008556 (section 2.6)" ] ;
            schema1:url "https://ada.astromat.org/missing" ],
        [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:description "Single-element and RGB composite X-ray maps are compared with BSE and optical image mosaics (reflected light, plane polarized, crossed polars) to discriminate crystalline from glassy phases; an Al-Mg-Fe RGB composite X-ray map is used to discriminate feldspathic (red) from ferromagnesian (green and blue) phases" ;
                    schema1:name "BSE mosaic imaging (same JEOL JXA-8200); QEMSCAN (FEI QUANTA 650 FEG-SEM, Univ. Manchester); optical microscopy (Keyence VHX 7000, NASA JSC); micro-XCT (custom NSI instrument, UTCT)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "test value schema:defaultValue" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analyticalMode "WDS Mapping" ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "ZAF" ;
    ada:monitoredElements "Mg, Al, Fe, Ca, Ti, Na, Si, Mn, K, Cr — 'Two passes were used to collect X-ray intensities for Mg, Al, Fe, Ca, and Ti in pass 1, and Na, Si, Mn, K, and Cr in pass 2' (p.6)" ;
    ada:reportedProperties "element wt% maps; oxide wt% maps; cation stoichiometry; mineral endmember maps — 32-bit floating point .tiff" ;
    ada:samplingUnitSelectionCriteriaDefault "N - continuous thin sections of the whole core; five stage maps per section, no selection rule stated" ;
    ada:samplingUnitType "Analysis point - each map pixel is a fully quantitative analysis (1,024 x 1,024 per stage map; five stage maps per thin section; 20 x 10^6 analyses across all slides)" ;
    ada:stepSizePixelSizeDefault "9.5 um (stage maps); ~1.5 um per pixel (BSE mosaic)" ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "lunar regolith" ;
            ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/backgroundCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/peakCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName> ] ;
    ada:targetSpeciesTemplate [ ada:defaultTargetSpecies "Al",
                "Ca",
                "Cr",
                "Fe",
                "K",
                "Mg",
                "Mn",
                "Na",
                "Si",
                "Ti" ;
            ada:targetSpeciesColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetSpecies" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalAccuracy>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalPrecision>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/beamCurrent>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/blankCorrection>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferingElements>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied> ] ;
    ada:wdsDeadTimeCorrection "missing" ;
    bios:computationalTool [ schema1:name "JEOL guide-net mapping software (BSE mosaic); N for the WDS stage maps" ;
            ada:toolRole "acquisition" ],
        [ schema1:name "Probe Software CalcImage and Probe for EPMA (full Phi(rho-z) correction at each pixel); MATLAB routines generating 32-bit floating point .tiff quantitative maps; Fiji and MATLAB for stitching; ENVI input image stacks" ;
            ada:toolRole "dataReduction" ] .

<ex:instrument/EPMA> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EPMA" ;
    schema1:hasPart <ex:instrument/EPMA/part/EDS-Detector>,
        <ex:instrument/EPMA/part/Electron-Source>,
        <ex:instrument/EPMA/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "JEOL" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "15 kV (stage maps and BSE mosaic)" ;
    ada:beamDiameterDefault "N/A — mapping-only procedure; map beam under Mapping Beam Diameter" ;
    ada:beamMode "N/A — mapping-only procedure; map conditions under Mapping Beam Mode" ;
    ada:mappingBeamCurrentDefault "100 nA probe current (stage maps)" ;
    ada:mappingBeamDiameterDefault "10 µm (fixed)" ;
    ada:mappingBeamMode "Fixed 10 µm beam (stated 'a fixed 10 um electron beam')" .

<ex:instrument/EPMA/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:description "N/A — WDS mapping procedure" ;
    schema1:name "missing" .

<ex:instrument/EPMA/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "missing" ;
    schema1:name "missing" .

<ex:instrument/EPMA/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "Fixed wavelength-dispersive spectrometers; count not stated (five elements collected per pass)" .

<ex:instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "JEOL JXA-8200" ] ;
    schema1:name "example instrumentName" .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/beamRasterDimensionsDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N/A — stage scan, not beam scan" ;
    schema1:name "Beam Raster Dimensions" ;
    schema1:valueName "beamRasterDimensionsDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/module/SamplingUnitSelection/preAnalysisImagingAndScreeningDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "BSE mosaic: approximately 325 backscattered-electron images collected with the JEOL guide-net mapping software at 15 kV, 2 nA probe current and 70x magnification, stitched with the ImageJ Fiji grid-collection stitching plug-in (Donovan et al., 2021) into a 20k x 5k pixel mosaic at ~1.5 um pixel resolution" ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:valueName "preAnalysisImagingAndScreeningDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/backgroundCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Background Counting Time" ;
    schema1:valueName "backgroundCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/peakCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Peak Counting Time" ;
    schema1:valueName "peakCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalAccuracy> a schema1:PropertyValueSpecification ;
    schema1:name "Analytical Accuracy" ;
    schema1:valueName "analyticalAccuracy" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/analyticalPrecision> a schema1:PropertyValueSpecification ;
    schema1:name "Analytical Precision" ;
    schema1:valueName "analyticalPrecision" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/beamCurrent> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Beam Current" ;
    schema1:valueName "beamCurrent" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/blankCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Blank Correction" ;
    schema1:valueName "blankCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard> a schema1:PropertyValueSpecification ;
    schema1:name "Interference Correction Standard" ;
    schema1:valueName "interferenceCorrectionStandard" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/interferingElements> a schema1:PropertyValueSpecification ;
    schema1:name "Interfering Elements" ;
    schema1:valueName "interferingElements" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Target Species Estimation Method" ;
    schema1:valueName "targetSpeciesEstimationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Time-Dependent Intensity Correction" ;
    schema1:valueName "timeDependentIntensityCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "X-ray Background Correction Method" ;
    schema1:valueName "xRayBackgroundCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "X-ray Line Overlap Corrections Applied" ;
    schema1:valueName "xRayLineOverlapCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/epmaTAPP/stageScanVsBeamScan> a schema1:PropertyValue ;
    schema1:name "Stage Scan vs. Beam Scan" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/epmaTAPP/stageScanVsBeamScan> ;
    schema1:value "Stage scan (stated 'EPMA stage maps')" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: EPMA/EPMA Technique-Aligned Protocol Profile (epmaTAPP)
description: Electron-probe microanalysis (EPMA/EPMA, WDS/EDS) extension of the base
  TAPP definition, generated from tapp/Current TAPPs/EPMA_TAPP_v88.csv via the path-driven
  pipeline (bootstrap_schemapaths.py + build_pathdriven.py).
allOf:
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/calibrationFactor/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/targetSpecies/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/compositionQC/schema.yaml#/$defs/ProcedureIdentification
- type: object
  properties:
    schema:instrument:
      type: array
      items:
        type: object
        allOf:
        - if:
            properties:
              schema:additionalType:
                contains:
                  const: EPMA
                schema:inDefinedTermSet: ada:vocab/instrumentType
            required:
            - schema:additionalType
          then:
            properties:
              ada:acceleratingVoltageDefault:
                description: Electron beam accelerating voltage in kilovolts (kV).
                  Justify any deviation from the standard operating voltage.
                anyOf:
                - type: number
                - type: string
              ada:beamDiameterDefault:
                description: Diameter of the electron beam in micrometers. 0 indicates
                  a fully focused beam. Document defocused diameter when used to minimize
                  beam damage or improve spatial averaging for beam-sensitive phases.
                anyOf:
                - type: number
                - type: string
              ada:beamMode:
                description: Whether the electron beam was operated as a stationary
                  focused spot, defocused to a specified diameter, or rastered over
                  a small area during a single-point analysis. Must be consistent
                  with the Beam Diameter and Beam Raster Dimensions fields. For mapping,
                  beam scanning is controlled by Step Size / Pixel Size and Stage
                  Scan vs. Beam Scan instead.
                anyOf:
                - type: string
                  enum:
                  - Focused
                  - Defocused
                  - Rastered
                  - N/A
                  - None
                  - missing
                - type: string
                readOnly: true
              schema:hasPart:
                type: array
                items:
                  type: object
                  allOf:
                  - if:
                      properties:
                        schema:additionalType:
                          contains:
                            const: EDS Detector
                          schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                      required:
                      - schema:additionalType
                    then:
                      properties:
                        schema:description:
                          description: EDS detector type, manufacturer, number of
                            detector elements, active area and solid angle, window
                            type, and geometry (take-off angle, position). List multiple
                            detectors separately. Record 'N/A' where the procedure
                            has no EDS detector.
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
                            const: Electron Source
                          schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                      required:
                      - schema:additionalType
                    then:
                      properties:
                        schema:description:
                          description: Type of electron gun used in the instrument.
                          anyOf:
                          - type: string
                            enum:
                            - Cold-FEG
                            - Schottky FEG (X-FEG)
                            - Schottky FEG (standard)
                            - "Field emission gun (FEG) \u2014 subtype not specified"
                            - LaB6 / CeB6
                            - Tungsten (W)
                            - Unknown
                            - N/A
                            - None
                            - missing
                            readOnly: true
                          - type: array
                            items:
                              type: string
                              enum:
                              - Cold-FEG
                              - Schottky FEG (X-FEG)
                              - Schottky FEG (standard)
                              - "Field emission gun (FEG) \u2014 subtype not specified"
                              - LaB6 / CeB6
                              - Tungsten (W)
                              - Unknown
                              - N/A
                              - None
                              - missing
                              readOnly: true
                      required:
                      - schema:description
                  - if:
                      properties:
                        schema:additionalType:
                          contains:
                            const: WDS Spectrometer
                          schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                      required:
                      - schema:additionalType
                    then:
                      properties:
                        schema:name:
                          description: Number, type, and crystal range of WDS spectrometers
                            on the instrument. Include manufacturer, model, and crystal
                            range. For SEM-WDS configurations (third-party WDS on
                            a non-EPMA platform), include WDS manufacturer and model.
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
                          const: Electron Source
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
                    - JEOL
                    - Cameca
                    - Unknown
                    - N/A
                    - None
                    - missing
                    readOnly: true
                required:
                - schema:name
              ada:mappingBeamMode:
                description: Whether the electron beam was focused or defocused to
                  a stated diameter during X-ray mapping. How the beam or stage moves
                  across the mapped area is recorded by Stage Scan vs. Beam Scan and
                  Step Size / Pixel Size.
                anyOf:
                - type: string
                  enum:
                  - Focused
                  - Defocused
                  - N/A
                  - None
                  - missing
                - type: string
                readOnly: true
              ada:mappingBeamCurrentDefault:
                description: Probe current in nanoamperes (nA) used during X-ray mapping.
                anyOf:
                - type: number
                - type: string
              ada:mappingBeamDiameterDefault:
                description: Diameter of the electron beam in micrometres during X-ray
                  mapping. 0 indicates a fully focused beam.
                anyOf:
                - type: number
                - type: string
            required:
            - ada:acceleratingVoltageDefault
            - ada:beamDiameterDefault
            - ada:beamMode
            - ada:mappingBeamCurrentDefault
            - ada:mappingBeamDiameterDefault
            - ada:mappingBeamMode
            - schema:manufacturer
        - if:
            properties:
              schema:additionalType:
                contains:
                  const: SEM
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
            required:
            - schema:model
      allOf:
      - contains:
          properties:
            schema:additionalType:
              contains:
                const: EPMA
              schema:inDefinedTermSet: ada:vocab/instrumentType
          required:
          - schema:additionalType
      - contains:
          properties:
            schema:additionalType:
              contains:
                const: SEM
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
            - title: Target Species Estimation Method
              description: Whether elemental concentrations were calculated directly
                from measured X-ray intensities, or estimated by cation stoichiometry
                (e.g., oxygen calculated from cation proportions in silicates; carbon
                from stoichiometry in carbonates).
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: targetSpeciesEstimationMethod
                schema:name:
                  const: Target Species Estimation Method
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: true
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
            - title: Analytical Accuracy
              description: Offset between measured and accepted reference values for
                secondary standards, expressed as percent relative bias. Include reference
                material, reference value source, and the measured value.
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/epmaTAPP/analyticalAccuracy
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: analyticalAccuracy
                schema:name:
                  const: Analytical Accuracy
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
            - title: Analytical Precision
              description: Reproducibility of repeated measurements on the same or
                equivalent reference material, expressed as 1-sigma relative standard
                deviation (%). Include reference material name, number of analyses
                (n), and the measured value.
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/epmaTAPP/analyticalPrecision
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: analyticalPrecision
                schema:name:
                  const: Analytical Precision
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
            - title: X-ray Background Correction Method
              description: 'Method used to estimate and subtract background X-ray
                intensity beneath the peak. For WDS: typically 2-point off-peak linear
                interpolation or Mean Atomic Number (MAN) background model. For EDS:
                spectral background fitting or top-hat filter applied during spectral
                processing.'
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: xRayBackgroundCorrectionMethod
                schema:name:
                  const: X-ray Background Correction Method
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
            - title: Beam Current
              description: Probe current in nanoamperes (nA). Often varies by phase
                type or target species; record the procedure-standard value(s).
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/epmaTAPP/beamCurrent
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: beamCurrent
                schema:name:
                  const: Beam Current
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
            - title: Blank Correction
              description: Method and reference material(s) used to determine and
                subtract blank signal contributions (e.g., carbon coat contribution
                to C signal, or background contamination for trace elements).
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/epmaTAPP/blankCorrection
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: blankCorrection
                schema:name:
                  const: Blank Correction
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
                  const: ada:targetSpeciesColumn/epmaTAPP/countingStatisticsError
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
            - title: Interference Correction Standard
              description: Reference material used to quantify and calibrate the interference
                correction.
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: interferenceCorrectionStandard
                schema:name:
                  const: Interference Correction Standard
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: true
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
            - title: X-ray Line Overlap Corrections Applied
              description: Whether a spectral interference correction was applied.
                Common interferences include Ti Kb on V Ka, Cr Kb on Mn Ka, and Ba
                La on Ti Ka.
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: xRayLineOverlapCorrectionsApplied
                schema:name:
                  const: X-ray Line Overlap Corrections Applied
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
            - title: Interfering Elements
              description: Element(s) whose X-ray lines overlap with the measured
                peak, requiring a correction.
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/epmaTAPP/interferingElements
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: interferingElements
                schema:name:
                  const: Interfering Elements
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: true
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
            - title: Time-Dependent Intensity Correction
              description: Type of time-dependent intensity (TDI) correction applied
                to compensate for beam-induced volatilization or migration of sensitive
                elements (e.g., Na, K, F in glasses, feldspars, carbonates).
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: timeDependentIntensityCorrection
                schema:name:
                  const: Time-Dependent Intensity Correction
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
              title: Target Species Estimation Method
              description: Whether elemental concentrations were calculated directly
                from measured X-ray intensities, or estimated by cation stoichiometry
                (e.g., oxygen calculated from cation proportions in silicates; carbon
                from stoichiometry in carbonates).
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/epmaTAPP/targetSpeciesEstimationMethod
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: targetSpeciesEstimationMethod
                schema:name:
                  const: Target Species Estimation Method
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: true
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
              title: Analytical Accuracy
              description: Offset between measured and accepted reference values for
                secondary standards, expressed as percent relative bias. Include reference
                material, reference value source, and the measured value.
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/epmaTAPP/analyticalAccuracy
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: analyticalAccuracy
                schema:name:
                  const: Analytical Accuracy
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
              title: Analytical Precision
              description: Reproducibility of repeated measurements on the same or
                equivalent reference material, expressed as 1-sigma relative standard
                deviation (%). Include reference material name, number of analyses
                (n), and the measured value.
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/epmaTAPP/analyticalPrecision
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: analyticalPrecision
                schema:name:
                  const: Analytical Precision
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
              title: X-ray Background Correction Method
              description: 'Method used to estimate and subtract background X-ray
                intensity beneath the peak. For WDS: typically 2-point off-peak linear
                interpolation or Mean Atomic Number (MAN) background model. For EDS:
                spectral background fitting or top-hat filter applied during spectral
                processing.'
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/epmaTAPP/xRayBackgroundCorrectionMethod
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: xRayBackgroundCorrectionMethod
                schema:name:
                  const: X-ray Background Correction Method
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
              title: Beam Current
              description: Probe current in nanoamperes (nA). Often varies by phase
                type or target species; record the procedure-standard value(s).
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/epmaTAPP/beamCurrent
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: beamCurrent
                schema:name:
                  const: Beam Current
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
              title: Blank Correction
              description: Method and reference material(s) used to determine and
                subtract blank signal contributions (e.g., carbon coat contribution
                to C signal, or background contamination for trace elements).
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/epmaTAPP/blankCorrection
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: blankCorrection
                schema:name:
                  const: Blank Correction
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
                  const: ada:targetSpeciesColumn/epmaTAPP/countingStatisticsError
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
              title: Interference Correction Standard
              description: Reference material used to quantify and calibrate the interference
                correction.
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/epmaTAPP/interferenceCorrectionStandard
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: interferenceCorrectionStandard
                schema:name:
                  const: Interference Correction Standard
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: true
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
              title: X-ray Line Overlap Corrections Applied
              description: Whether a spectral interference correction was applied.
                Common interferences include Ti Kb on V Ka, Cr Kb on Mn Ka, and Ba
                La on Ti Ka.
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/epmaTAPP/xRayLineOverlapCorrectionsApplied
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: xRayLineOverlapCorrectionsApplied
                schema:name:
                  const: X-ray Line Overlap Corrections Applied
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
              title: Interfering Elements
              description: Element(s) whose X-ray lines overlap with the measured
                peak, requiring a correction.
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/epmaTAPP/interferingElements
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: interferingElements
                schema:name:
                  const: Interfering Elements
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: true
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
              title: Time-Dependent Intensity Correction
              description: Type of time-dependent intensity (TDI) correction applied
                to compensate for beam-induced volatilization or migration of sensitive
                elements (e.g., Na, K, F in glasses, feldspars, carbonates).
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/epmaTAPP/timeDependentIntensityCorrection
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: timeDependentIntensityCorrection
                schema:name:
                  const: Time-Dependent Intensity Correction
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
    ada:targetMaterialTemplate:
      type: object
      properties:
        ada:targetMaterialColumns:
          type: array
          items:
            anyOf:
            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/TargetMaterialIdentifierColumn
            - title: Background Counting Time
              description: Total time spent counting at off-peak background position(s)
                in seconds, summed across all background positions.
              type: object
              properties:
                '@id':
                  const: ada:targetMaterialColumn/epmaTAPP/backgroundCountingTime
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: backgroundCountingTime
                schema:name:
                  const: Background Counting Time
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
            - title: Peak Counting Time
              description: Time spent counting X-ray intensity at the peak position,
                in seconds. Adjustments stay within procedure-defined bounds.
              type: object
              properties:
                '@id':
                  const: ada:targetMaterialColumn/epmaTAPP/peakCountingTime
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: peakCountingTime
                schema:name:
                  const: Peak Counting Time
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
                  const: ada:targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName
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
              title: Background Counting Time
              description: Total time spent counting at off-peak background position(s)
                in seconds, summed across all background positions.
              type: object
              properties:
                '@id':
                  const: ada:targetMaterialColumn/epmaTAPP/backgroundCountingTime
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: backgroundCountingTime
                schema:name:
                  const: Background Counting Time
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
              title: Peak Counting Time
              description: Time spent counting X-ray intensity at the peak position,
                in seconds. Adjustments stay within procedure-defined bounds.
              type: object
              properties:
                '@id':
                  const: ada:targetMaterialColumn/epmaTAPP/peakCountingTime
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: peakCountingTime
                schema:name:
                  const: Peak Counting Time
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
                  const: ada:targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName
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
        ada:defaultTargetMaterials:
          type: array
          items:
            anyOf:
            - type: string
            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/DefinedTerm
            - type: object
      required:
      - ada:defaultTargetMaterials
    ada:monitoredPropertyTemplate:
      type: object
      properties:
        ada:monitoredPropertyColumns:
          type: array
          items:
            anyOf:
            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/MonitoredPropertyIdentifierColumn
            - title: Background Position(s)
              description: Location(s) of off-peak background measurement(s) relative
                to the peak, in mm or sin-theta, and whether on the high- or low-energy
                side.
              type: object
              properties:
                '@id':
                  const: ada:monitoredPropertyColumn/epmaTAPP/backgroundPosition
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: backgroundPosition
                schema:name:
                  const: Background Position(s)
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: false
                ada:tier:
                  const: R
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
            - title: Diffracting Crystal
              description: Analyzing crystal (monochromator).
              type: object
              properties:
                '@id':
                  const: ada:monitoredPropertyColumn/epmaTAPP/diffractingCrystal
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: diffractingCrystal
                schema:name:
                  const: Diffracting Crystal
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
            - title: Dwell Time per Pixel
              description: 'Time spent acquiring X-ray signal at each pixel during
                X-ray mapping, in milliseconds. For WDS: one value per spectrometer
                assignment per pixel. For EDS: total live-time per spectrum per pixel,
                a single value.'
              type: object
              properties:
                '@id':
                  const: ada:monitoredPropertyColumn/epmaTAPP/dwellTimePerPixel
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: dwellTimePerPixel
                schema:name:
                  const: Dwell Time per Pixel
                ada:dataType:
                  const: number
                schema:readonlyValue:
                  const: false
                ada:tier:
                  const: M
                schema:defaultValue:
                  anyOf:
                  - anyOf:
                    - type: number
                    - type: string
                  - type: array
                    items:
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
            - title: Proportional Counter / Detector
              description: Type of detector used.
              type: object
              properties:
                '@id':
                  const: ada:monitoredPropertyColumn/epmaTAPP/proportionalCounterDetector
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: proportionalCounterDetector
                schema:name:
                  const: Proportional Counter / Detector
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: true
                ada:tier:
                  const: R
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
            - title: Sequence
              description: "Order in which spectrometer assignments are acquired,
                and \u2014 where the element suite exceeds the number of spectrometers
                \u2014 the passes the acquisition is divided into. Within a single
                pass all assigned spectrometers collect simultaneously, including
                at every pixel in X-ray mapping; a suite larger than the spectrometer
                count therefore requires the acquisition to be run more than once,
                each pass covering a different subset of elements."
              type: object
              properties:
                '@id':
                  const: ada:monitoredPropertyColumn/epmaTAPP/sequence
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: sequence
                schema:name:
                  const: Sequence
                ada:dataType:
                  const: integer
                schema:readonlyValue:
                  const: true
                ada:tier:
                  const: R
                schema:defaultValue:
                  anyOf:
                  - anyOf:
                    - type: number
                    - type: string
                  - type: array
                    items:
                      anyOf:
                      - type: number
                      - type: string
              required:
              - '@id'
              - '@type'
              - schema:valueName
              - schema:name
              - ada:dataType
            - title: WDS PHA Setting
              description: Pulse height analyzer (PHA) setting for the WDS detector.
                Integral mode accepts all pulses above a threshold; Differential mode
                selects a narrow energy window to reject higher-order reflections
                and escape peaks.
              type: object
              properties:
                '@id':
                  const: ada:monitoredPropertyColumn/epmaTAPP/wdsPhaSetting
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: wdsPhaSetting
                schema:name:
                  const: WDS PHA Setting
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: true
                ada:tier:
                  const: R
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
            - title: X-ray Line
              description: X-ray emission line measured.
              type: object
              properties:
                '@id':
                  const: ada:monitoredPropertyColumn/epmaTAPP/xRayLine
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: xRayLine
                schema:name:
                  const: X-ray Line
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
            - title: X-ray Detection Method per Monitored Element
              description: 'The X-ray detection method used to measure the monitored
                element: wavelength-dispersive (WDS), in which a crystal spectrometer
                separates the X-rays by wavelength and a proportional counter counts
                them, or energy-dispersive (EDS), in which a solid-state detector
                sorts every photon by energy at once. Applies where a procedure uses
                both.'
              type: object
              properties:
                '@id':
                  const: ada:monitoredPropertyColumn/epmaTAPP/xRayDetectionMethodPerMonitoredElement
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: xRayDetectionMethodPerMonitoredElement
                schema:name:
                  const: X-ray Detection Method per Monitored Element
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
              title: Background Position(s)
              description: Location(s) of off-peak background measurement(s) relative
                to the peak, in mm or sin-theta, and whether on the high- or low-energy
                side.
              type: object
              properties:
                '@id':
                  const: ada:monitoredPropertyColumn/epmaTAPP/backgroundPosition
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: backgroundPosition
                schema:name:
                  const: Background Position(s)
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: false
                ada:tier:
                  const: R
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
            minContains: 0
            maxContains: 1
          - contains:
              title: Diffracting Crystal
              description: Analyzing crystal (monochromator).
              type: object
              properties:
                '@id':
                  const: ada:monitoredPropertyColumn/epmaTAPP/diffractingCrystal
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: diffractingCrystal
                schema:name:
                  const: Diffracting Crystal
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
              title: Dwell Time per Pixel
              description: 'Time spent acquiring X-ray signal at each pixel during
                X-ray mapping, in milliseconds. For WDS: one value per spectrometer
                assignment per pixel. For EDS: total live-time per spectrum per pixel,
                a single value.'
              type: object
              properties:
                '@id':
                  const: ada:monitoredPropertyColumn/epmaTAPP/dwellTimePerPixel
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: dwellTimePerPixel
                schema:name:
                  const: Dwell Time per Pixel
                ada:dataType:
                  const: number
                schema:readonlyValue:
                  const: false
                ada:tier:
                  const: M
                schema:defaultValue:
                  anyOf:
                  - anyOf:
                    - type: number
                    - type: string
                  - type: array
                    items:
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
              title: Proportional Counter / Detector
              description: Type of detector used.
              type: object
              properties:
                '@id':
                  const: ada:monitoredPropertyColumn/epmaTAPP/proportionalCounterDetector
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: proportionalCounterDetector
                schema:name:
                  const: Proportional Counter / Detector
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: true
                ada:tier:
                  const: R
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
            minContains: 0
            maxContains: 1
          - contains:
              title: Sequence
              description: "Order in which spectrometer assignments are acquired,
                and \u2014 where the element suite exceeds the number of spectrometers
                \u2014 the passes the acquisition is divided into. Within a single
                pass all assigned spectrometers collect simultaneously, including
                at every pixel in X-ray mapping; a suite larger than the spectrometer
                count therefore requires the acquisition to be run more than once,
                each pass covering a different subset of elements."
              type: object
              properties:
                '@id':
                  const: ada:monitoredPropertyColumn/epmaTAPP/sequence
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: sequence
                schema:name:
                  const: Sequence
                ada:dataType:
                  const: integer
                schema:readonlyValue:
                  const: true
                ada:tier:
                  const: R
                schema:defaultValue:
                  anyOf:
                  - anyOf:
                    - type: number
                    - type: string
                  - type: array
                    items:
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
              title: WDS PHA Setting
              description: Pulse height analyzer (PHA) setting for the WDS detector.
                Integral mode accepts all pulses above a threshold; Differential mode
                selects a narrow energy window to reject higher-order reflections
                and escape peaks.
              type: object
              properties:
                '@id':
                  const: ada:monitoredPropertyColumn/epmaTAPP/wdsPhaSetting
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: wdsPhaSetting
                schema:name:
                  const: WDS PHA Setting
                ada:dataType:
                  const: string
                schema:readonlyValue:
                  const: true
                ada:tier:
                  const: R
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
            minContains: 0
            maxContains: 1
          - contains:
              title: X-ray Line
              description: X-ray emission line measured.
              type: object
              properties:
                '@id':
                  const: ada:monitoredPropertyColumn/epmaTAPP/xRayLine
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: xRayLine
                schema:name:
                  const: X-ray Line
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
              title: X-ray Detection Method per Monitored Element
              description: 'The X-ray detection method used to measure the monitored
                element: wavelength-dispersive (WDS), in which a crystal spectrometer
                separates the X-rays by wavelength and a proportional counter counts
                them, or energy-dispersive (EDS), in which a solid-state detector
                sorts every photon by energy at once. Applies where a procedure uses
                both.'
              type: object
              properties:
                '@id':
                  const: ada:monitoredPropertyColumn/epmaTAPP/xRayDetectionMethodPerMonitoredElement
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: xRayDetectionMethodPerMonitoredElement
                schema:name:
                  const: X-ray Detection Method per Monitored Element
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
        ada:defaultMonitoredProperties:
          type: array
          items:
            anyOf:
            - type: string
            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/DefinedTerm
            - type: object
    schema:additionalProperty:
      type: array
      items:
        anyOf:
        - title: Beam Damage Minimization
          description: Measures taken to minimize beam damage, particularly volatilization
            or migration of Na, K, F, and Cl in hydrous minerals, glasses, feldspars,
            phosphates, and carbonates. Document approach, beam conditions used, and
            phases for which it was applied.
          type: object
          properties:
            '@id':
              const: ada:parameter/epmaTAPP/beamDamageMinimizationDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: beamDamageMinimizationDefault
            schema:name:
              const: Beam Damage Minimization
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
        - title: Beam Raster Dimensions
          description: "Dimensions of the small area over which the beam is rastered
            at a single analysis point, reported as width \xD7 height in \xB5m. Applicable
            when Beam Mode = Rastered; defines the effective spatial footprint of
            the measurement. Not applicable when mapping."
          type: object
          properties:
            '@id':
              const: ada:parameter/epmaTAPP/beamRasterDimensionsDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: beamRasterDimensionsDefault
            schema:name:
              const: Beam Raster Dimensions
            ada:dataType:
              const: number
            ada:fieldScope:
              const: session
            schema:readonlyValue:
              const: false
            ada:tier:
              const: R
            schema:defaultValue:
              anyOf:
              - type: number
              - type: string
            schema:unitText:
              const: "\xB5m x \xB5m"
          required:
          - '@id'
          - '@type'
          - schema:valueName
          - schema:name
          - ada:dataType
          - ada:fieldScope
        - title: Drift Correction
          description: Method used to monitor and correct for instrument drift (beam
            current drift, spectrometer drift) during the analytical session.
          type: object
          properties:
            '@id':
              const: ada:parameter/epmaTAPP/driftCorrectionDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: driftCorrectionDefault
            schema:name:
              const: Drift Correction
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
        - title: EDS Spectral Processing Type
          description: Method used to process EDS spectra and extract net peak intensities
            from raw spectral data. Applied before quantification (see Matrix Correction
            Method). Common approaches include background fitting and subtraction
            followed by peak integration, and filter fit or Gaussian deconvolution
            for overlapping peaks.
          type: object
          properties:
            '@id':
              const: ada:parameter/epmaTAPP/edsSpectralProcessingType
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/epmaTAPP/edsSpectralProcessingType
            schema:name:
              const: EDS Spectral Processing Type
            schema:value:
              type: string
          required:
          - '@id'
          - '@type'
          - schema:propertyID
          - schema:name
          - schema:value
          readOnly: true
        - title: Halogen Correction on Oxygen
          description: Whether oxygen content was adjusted to account for halogen
            substitution (F and/or Cl replacing OH) in halogen-bearing phases such
            as apatite, amphibole, and mica, where oxygen is calculated by stoichiometry.
          type: object
          properties:
            '@id':
              const: ada:parameter/epmaTAPP/halogenCorrectionOnOxygenDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: halogenCorrectionOnOxygenDefault
            schema:name:
              const: Halogen Correction on Oxygen
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
        - title: Stage Scan vs. Beam Scan
          description: For mapping modes, whether the map was acquired by moving the
            stage while the beam is held fixed (stage scan), or by deflecting the
            beam across the field while the stage is stationary (beam scan).
          type: object
          properties:
            '@id':
              const: ada:parameter/epmaTAPP/stageScanVsBeamScan
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/epmaTAPP/stageScanVsBeamScan
            schema:name:
              const: Stage Scan vs. Beam Scan
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
          title: Beam Damage Minimization
          description: Measures taken to minimize beam damage, particularly volatilization
            or migration of Na, K, F, and Cl in hydrous minerals, glasses, feldspars,
            phosphates, and carbonates. Document approach, beam conditions used, and
            phases for which it was applied.
          type: object
          properties:
            '@id':
              const: ada:parameter/epmaTAPP/beamDamageMinimizationDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: beamDamageMinimizationDefault
            schema:name:
              const: Beam Damage Minimization
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
          title: Beam Raster Dimensions
          description: "Dimensions of the small area over which the beam is rastered
            at a single analysis point, reported as width \xD7 height in \xB5m. Applicable
            when Beam Mode = Rastered; defines the effective spatial footprint of
            the measurement. Not applicable when mapping."
          type: object
          properties:
            '@id':
              const: ada:parameter/epmaTAPP/beamRasterDimensionsDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: beamRasterDimensionsDefault
            schema:name:
              const: Beam Raster Dimensions
            ada:dataType:
              const: number
            ada:fieldScope:
              const: session
            schema:readonlyValue:
              const: false
            ada:tier:
              const: R
            schema:defaultValue:
              anyOf:
              - type: number
              - type: string
            schema:unitText:
              const: "\xB5m x \xB5m"
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
          title: Drift Correction
          description: Method used to monitor and correct for instrument drift (beam
            current drift, spectrometer drift) during the analytical session.
          type: object
          properties:
            '@id':
              const: ada:parameter/epmaTAPP/driftCorrectionDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: driftCorrectionDefault
            schema:name:
              const: Drift Correction
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
          title: EDS Spectral Processing Type
          description: Method used to process EDS spectra and extract net peak intensities
            from raw spectral data. Applied before quantification (see Matrix Correction
            Method). Common approaches include background fitting and subtraction
            followed by peak integration, and filter fit or Gaussian deconvolution
            for overlapping peaks.
          type: object
          properties:
            '@id':
              const: ada:parameter/epmaTAPP/edsSpectralProcessingType
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/epmaTAPP/edsSpectralProcessingType
            schema:name:
              const: EDS Spectral Processing Type
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
          title: Halogen Correction on Oxygen
          description: Whether oxygen content was adjusted to account for halogen
            substitution (F and/or Cl replacing OH) in halogen-bearing phases such
            as apatite, amphibole, and mica, where oxygen is calculated by stoichiometry.
          type: object
          properties:
            '@id':
              const: ada:parameter/epmaTAPP/halogenCorrectionOnOxygenDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: halogenCorrectionOnOxygenDefault
            schema:name:
              const: Halogen Correction on Oxygen
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
          title: Stage Scan vs. Beam Scan
          description: For mapping modes, whether the map was acquired by moving the
            stage while the beam is held fixed (stage scan), or by deflecting the
            beam across the field while the stage is stationary (beam scan).
          type: object
          properties:
            '@id':
              const: ada:parameter/epmaTAPP/stageScanVsBeamScan
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/epmaTAPP/stageScanVsBeamScan
            schema:name:
              const: Stage Scan vs. Beam Scan
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
    ada:edsAcquisitionMode:
      description: "Spatial acquisition sub-strategy for EDS measurements: stationary-beam
        point acquisition, line scan (beam stepped along a transect at defined intervals),
        or area map / spectrum image (beam rastered over a pixel grid). Specifies
        how the beam is positioned during data collection within the declared analytical
        mode. Record 'N/A' where the procedure has no EDS detector. 'Point' covers
        what the literature also calls spot or point-spectrum analysis. 'Map' and
        'Spectrum image' are distinct acquisitions, not synonyms: a map may retain
        element intensities alone, whereas a spectrum image retains a full spectrum
        at every pixel and can be requantified afterwards \u2014 record which was
        acquired. Where more than one mode was used, join them with '; ' rather than
        looking for a combined member."
      type: string
      enum:
      - Point
      - Line scan
      - Map
      - Spectrum image
      - N/A
      - None
      - missing
      readOnly: true
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
                  $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Procedure_preAnalysisImagingAndScreening
                allOf:
                - contains:
                    $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Procedure_preAnalysisImagingAndScreening
                  minContains: 0
                  maxContains: 1
    ada:edsLiveTimePerPointOrPixelDefault:
      description: EDS spectral acquisition live time per analysis point in seconds.
        Previously referred to as "EDS Acquisition Time" in this TAPP and commonly
        used under that name in EPMA and SEM-EDS contexts. Renamed to align with TEM-EDS
        usage, where the per-point vs. per-pixel distinction (point/line mode vs.
        spectrum image) is explicit. In EPMA, acquisition is always per point.
      anyOf:
      - type: number
      - type: string
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
                    const: Data reduction
                required:
                - schema:name
              then:
                properties:
                  schema:additionalProperty:
                    type: array
                    items:
                      anyOf:
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
                            const: ada:parameter/epmaTAPP/analysisInclusionAndRejectionCriteriaDefault
                          '@type':
                            const:
                            - schema:PropertyValueSpecification
                          schema:valueName:
                            const: analysisInclusionAndRejectionCriteriaDefault
                          schema:name:
                            const: Analysis Inclusion and Rejection Criteria
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
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Procedure_constantsReferenceValues
                    allOf:
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
                            const: ada:parameter/epmaTAPP/analysisInclusionAndRejectionCriteriaDefault
                          '@type':
                            const:
                            - schema:PropertyValueSpecification
                          schema:valueName:
                            const: analysisInclusionAndRejectionCriteriaDefault
                          schema:name:
                            const: Analysis Inclusion and Rejection Criteria
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
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Procedure_constantsReferenceValues
                      minContains: 0
                      maxContains: 1
          allOf:
          - contains:
              properties:
                schema:name:
                  const: Data reduction
              required:
              - schema:name
    ada:massAbsorptionCoefficients:
      description: Database of mass absorption coefficients used in the matrix correction.
      type: string
      enum:
      - LINEMU
      - CITZMU
      - MCMASTER
      - MAC30
      - MACJTA
      - FFAST
      - Unknown
      - N/A
      - None
      - missing
      readOnly: true
    ada:matrixCorrectionMethod:
      description: "X-ray matrix correction algorithm applied during quantitative
        EDS or WDS data reduction. For X-ray mapping, applies when raw count maps
        are converted to quantitative concentration maps. Where the k-factors or calibration
        constants themselves came from \u2014 measured standards, a vendor library,
        or theoretical cross-sections \u2014 is a separate question answered by this
        technique's calibration-standard field, not here; a procedure may be both
        absorption-corrected and standardless."
      anyOf:
      - type: string
        enum:
        - PAP (Pouchou & Pichoir Full)
        - XPP (Simplified PAP)
        - PhiRhoZ Bastin (EPQ-91)
        - Love-Scott I
        - Love-Scott II
        - Armstrong / Love-Scott
        - ZAF
        - CITZAF (Armstrong 1995)
        - Bence-Albee
        - Unknown
        - N/A
        - None
        - missing
      - type: string
      readOnly: true
    ada:stepSizePixelSizeDefault:
      description: Distance between adjacent measurement points in the X-ray map in
        micrometers, defining the spatial resolution. Report both X and Y step if
        they differ.
      anyOf:
      - type: number
      - type: string
    ada:wdsDeadTimeCorrection:
      description: "Method used to correct for WDS proportional counter dead time
        at high count rates. Unlike EDS dead time \u2014 which is hardware-managed
        and reported as a session QC percentage (see EDS Dead Time) \u2014 WDS dead
        time correction is a user-selectable algorithm in the data reduction software.
        No separate measured WDS dead time value is reported; the correction is applied
        transparently during intensity-to-concentration conversion. Record the algorithm
        here and any instrument-specific constant alongside it \u2014 'Default constant
        (manufacturer) \u2014 3 \xB5s, Cameca'. The instrument vendor itself is recorded
        by Instrument Manufacturer, not by this field's allowed values."
      anyOf:
      - type: string
        enum:
        - Default constant (manufacturer)
        - Adjusted constant
        - Logarithmic
        - High-precision (Probe for EPMA)
        - Super-precision (Probe for EPMA)
        - Unknown
        - N/A
        - None
        - missing
      - type: string
      readOnly: true
    ada:monitoredElements:
      type: array
      items:
        description: Specific elements monitored in this procedure, grouped by the
          target species they serve where they serve one. Includes elements monitored
          only to correct an interference, which serve no target species and so have
          no parent. The target species list is given by the Target Species field
          and is never inferred from the elements appearing here. A target species
          determined by stoichiometry or by difference, rather than measured, has
          no monitored element. The X-ray line, diffracting crystal, spectrometer
          assignment and counting times used for each monitored element are recorded
          in their own fields, keyed to this one.
        type: string
        readOnly: true
    ada:analyticalMode:
      type: array
      items:
        type: string
        enum:
        - EDS Point Analysis
        - EDS Mapping
        - WDS Point Analysis
        - WDS Mapping
  required:
  - ada:edsAcquisitionMode
  - ada:edsLiveTimePerPointOrPixelDefault
  - ada:massAbsorptionCoefficients
  - ada:matrixCorrectionMethod
  - ada:stepSizePixelSizeDefault
  - ada:wdsDeadTimeCorrection

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/tapp/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/tapp/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/tapp/context.jsonld)

## Sources

* [TAPP_EPMA_filled.xlsx (Components / TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/EPMA/tapp`

