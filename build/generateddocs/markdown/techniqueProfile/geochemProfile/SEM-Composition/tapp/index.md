
# SEM Composition (EDS/WDS) Technique-Aligned Protocol Profile (semCompositionTAPP) (Schema)

`ogch.techniqueProfile.geochemProfile.SEM-Composition.tapp` *v0.1*

Scanning electron microscopy compositional microanalysis (EDS/WDS) extension of the base TAPP definition, generated from docs/SEM_Composition_TAPP_v4.xlsx via the path-driven pipeline (bootstrap_schemapaths.py + build_pathdriven.py).

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### semCompositionTAPP example Genge2025
semCompositionTAPP instance derived from Genge et al. 2025 | Micrometeorite NG-1 (CV3-like) | EDS Point Analysis (ZEISS Sigma 1550VP, 10 kV).
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
  "@id": "ex:semCompositionTAPP-Genge2025",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semComposition protocol — Genge2025",
  "schema:description": "semCompositionTAPP instance derived from Genge et al. 2025 | Micrometeorite NG-1 (CV3-like) | EDS Point Analysis (ZEISS Sigma 1550VP, 10 kV) (publication column of SEM_Composition_TAPP_v83.csv).",
  "ada:targetMaterialTemplate": {
    "ada:targetMaterialDeclaration": "Al-Cu alloy phases; associated minerals — Micrometeorite NG-1, Al-Cu-alloy-bearing, CV3-like composition; Democratic Republic of Congo",
    "ada:defaultTargetMaterials": [
      "associated minerals"
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
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "N — the target phases are named (see `Sampling Unit Type`) but no rule is given for choosing the analysed points",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "Zeiss",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "ZEISS 1550VP",
        "@type": [
          "schema:ProductModel"
        ]
      },
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
          "@id": "ex:instrument/SEM/part/Electron-Source",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Oxford X-Max SDD system",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/SEM/part/EDS-Detector",
          "schema:name": "missing"
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
          "@id": "ex:instrument/SEM/part/WDS-Spectrometer"
        }
      ],
      "schema:description": "VP-SEM",
      "ada:acceleratingVoltageDefault": "10 kV",
      "ada:beamDiameterDefault": "N — the '0.1 μm beam diameter' (p.2) is the EPMA's, not the SEM's",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName",
      "ada:beamMode": "missing",
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:mappingBeamDiameterDefault": -9999,
      "ada:mappingBeamMode": "missing",
      "ada:workingDistanceDefault": -9999
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/semCompositionTAPP/beamDamageMinimizationDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "beamDamageMinimizationDefault",
      "schema:name": "Beam Damage Minimization",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N — 10 kV was chosen 'to reduce the excitation volume and increase spatial resolution' (p.2), not to limit beam damage"
    }
  ],
  "ada:matrixCorrectionMethod": "XPP (Simplified PAP)",
  "ada:monitoredElements": [
    "N — \"quantitative EDS analyses (with an Oxford X-Max SDD system and an XPP correction procedure calibrated with Oxford factory internal standards) were carried out at 10 kV\" (p.2), to determine the composition of the Al-Cu alloy phases and associated minerals; no element set is enumerated"
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "GPS Division Analytical Facility, California Institute of Technology"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "BSE Imaging (same session, same instrument); EBSD (same instrument); EPMA (JEOL JXA-iHP200F, WDS, out of scope)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Phase > Analysis point — \"quantitative EDS analyses\" of the alloy phases and associated minerals in the NG-1 section, with settings given per phase (\"12 kV for metals and 10 kV for silicates and oxides, beam current at 10 nA for metals and 5 nA for silicates and oxides\", p.2)",
  "ada:analyticalMode": [
    "EDS Point Analysis"
  ],
  "ada:reportedProperties": [
    "phase composition (normalised); fayalite content (Fa); phase identification (nominal) — Phase compositions as normalised analyses, with the olivine reported by fayalite content (Fa11–25) and \"Phase identification ... determined using normalised analyses, since the stoichiometry provides an adequate confirmation of analysis quality\" (p.2); phase identification is the nominal output"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "semComposition",
      "schema:termCode": "semComposition"
    }
  ],
  "schema:actionProcess": {
    "@type": [
      "schema:HowTo"
    ],
    "schema:step": [
      {
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
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
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2,
        "ada:detectionLimitMethod": "missing"
      }
    ]
  },
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:edsAcquisitionMode": "missing",
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semCompositionTAPP-Genge2025",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semComposition protocol \u2014 Genge2025",
  "schema:description": "semCompositionTAPP instance derived from Genge et al. 2025 | Micrometeorite NG-1 (CV3-like) | EDS Point Analysis (ZEISS Sigma 1550VP, 10 kV) (publication column of SEM_Composition_TAPP_v83.csv).",
  "ada:targetMaterialTemplate": {
    "ada:targetMaterialDeclaration": "Al-Cu alloy phases; associated minerals \u2014 Micrometeorite NG-1, Al-Cu-alloy-bearing, CV3-like composition; Democratic Republic of Congo",
    "ada:defaultTargetMaterials": [
      "associated minerals"
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
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "N \u2014 the target phases are named (see `Sampling Unit Type`) but no rule is given for choosing the analysed points",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "Zeiss",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "ZEISS 1550VP",
        "@type": [
          "schema:ProductModel"
        ]
      },
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
          "@id": "ex:instrument/SEM/part/Electron-Source",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Oxford X-Max SDD system",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/SEM/part/EDS-Detector",
          "schema:name": "missing"
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
          "@id": "ex:instrument/SEM/part/WDS-Spectrometer"
        }
      ],
      "schema:description": "VP-SEM",
      "ada:acceleratingVoltageDefault": "10 kV",
      "ada:beamDiameterDefault": "N \u2014 the '0.1 \u03bcm beam diameter' (p.2) is the EPMA's, not the SEM's",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName",
      "ada:beamMode": "missing",
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:mappingBeamDiameterDefault": -9999,
      "ada:mappingBeamMode": "missing",
      "ada:workingDistanceDefault": -9999
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/semCompositionTAPP/beamDamageMinimizationDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "beamDamageMinimizationDefault",
      "schema:name": "Beam Damage Minimization",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "N \u2014 10 kV was chosen 'to reduce the excitation volume and increase spatial resolution' (p.2), not to limit beam damage"
    }
  ],
  "ada:matrixCorrectionMethod": "XPP (Simplified PAP)",
  "ada:monitoredElements": [
    "N \u2014 \"quantitative EDS analyses (with an Oxford X-Max SDD system and an XPP correction procedure calibrated with Oxford factory internal standards) were carried out at 10 kV\" (p.2), to determine the composition of the Al-Cu alloy phases and associated minerals; no element set is enumerated"
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "GPS Division Analytical Facility, California Institute of Technology"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "BSE Imaging (same session, same instrument); EBSD (same instrument); EPMA (JEOL JXA-iHP200F, WDS, out of scope)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Phase > Analysis point \u2014 \"quantitative EDS analyses\" of the alloy phases and associated minerals in the NG-1 section, with settings given per phase (\"12 kV for metals and 10 kV for silicates and oxides, beam current at 10 nA for metals and 5 nA for silicates and oxides\", p.2)",
  "ada:analyticalMode": [
    "EDS Point Analysis"
  ],
  "ada:reportedProperties": [
    "phase composition (normalised); fayalite content (Fa); phase identification (nominal) \u2014 Phase compositions as normalised analyses, with the olivine reported by fayalite content (Fa11\u201325) and \"Phase identification ... determined using normalised analyses, since the stoichiometry provides an adequate confirmation of analysis quality\" (p.2); phase identification is the nominal output"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "semComposition",
      "schema:termCode": "semComposition"
    }
  ],
  "schema:actionProcess": {
    "@type": [
      "schema:HowTo"
    ],
    "schema:step": [
      {
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
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
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2,
        "ada:detectionLimitMethod": "missing"
      }
    ]
  },
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:edsAcquisitionMode": "missing",
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
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

<ex:semCompositionTAPP-Genge2025> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "missing" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:detectionLimitMethod "missing" ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/beamDamageMinimizationDefault> ;
    schema1:datePublished "missing" ;
    schema1:description "semCompositionTAPP instance derived from Genge et al. 2025 | Micrometeorite NG-1 (CV3-like) | EDS Point Analysis (ZEISS Sigma 1550VP, 10 kV) (publication column of SEM_Composition_TAPP_v83.csv)." ;
    schema1:instrument <ex:instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "GPS Division Analytical Facility, California Institute of Technology" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semComposition" ;
            schema1:termCode "semComposition" ] ;
    schema1:name "semComposition protocol — Genge2025" ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "BSE Imaging (same session, same instrument); EBSD (same instrument); EPMA (JEOL JXA-iHP200F, WDS, out of scope)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analyticalMode "EDS Point Analysis" ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "XPP (Simplified PAP)" ;
    ada:monitoredElements "N — \"quantitative EDS analyses (with an Oxford X-Max SDD system and an XPP correction procedure calibrated with Oxford factory internal standards) were carried out at 10 kV\" (p.2), to determine the composition of the Al-Cu alloy phases and associated minerals; no element set is enumerated" ;
    ada:reportedProperties "phase composition (normalised); fayalite content (Fa); phase identification (nominal) — Phase compositions as normalised analyses, with the olivine reported by fayalite content (Fa11–25) and \"Phase identification ... determined using normalised analyses, since the stoichiometry provides an adequate confirmation of analysis quality\" (p.2); phase identification is the nominal output" ;
    ada:samplingUnitSelectionCriteriaDefault "N — the target phases are named (see `Sampling Unit Type`) but no rule is given for choosing the analysed points" ;
    ada:samplingUnitType "Phase > Analysis point — \"quantitative EDS analyses\" of the alloy phases and associated minerals in the NG-1 section, with settings given per phase (\"12 kV for metals and 10 kV for silicates and oxides, beam current at 10 nA for metals and 5 nA for silicates and oxides\", p.2)" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "associated minerals" ;
            ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/backgroundCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/peakCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/primaryCalibrationStandardName> ;
            ada:targetMaterialDeclaration "Al-Cu alloy phases; associated minerals — Micrometeorite NG-1, Al-Cu-alloy-bearing, CV3-like composition; Democratic Republic of Congo" ] ;
    ada:wdsDeadTimeCorrection "missing" .

<ex:instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:description "VP-SEM" ;
    schema1:hasPart <ex:instrument/SEM/part/EDS-Detector>,
        <ex:instrument/SEM/part/Electron-Source>,
        <ex:instrument/SEM/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Zeiss" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "ZEISS 1550VP" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "10 kV" ;
    ada:beamDiameterDefault "N — the '0.1 μm beam diameter' (p.2) is the EPMA's, not the SEM's" ;
    ada:beamMode "missing" ;
    ada:mappingBeamCurrentDefault -9999 ;
    ada:mappingBeamDiameterDefault -9999 ;
    ada:mappingBeamMode "missing" ;
    ada:workingDistanceDefault -9999 .

<ex:instrument/SEM/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:description "Oxford X-Max SDD system" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Unknown" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/semCompositionTAPP/beamDamageMinimizationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "N — 10 kV was chosen 'to reduce the excitation volume and increase spatial resolution' (p.2), not to limit beam damage" ;
    schema1:name "Beam Damage Minimization" ;
    schema1:valueName "beamDamageMinimizationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/backgroundCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Background Counting Time" ;
    schema1:valueName "backgroundCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/peakCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Peak Counting Time" ;
    schema1:valueName "peakCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .


```


### semCompositionTAPP example Gucsik2013
semCompositionTAPP instance derived from Gucsik et al. 2013 | Forsterite, Kaba meteorite (CV3) | EDS Point Analysis (JEOL JSM-5410LV).
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
  "@id": "ex:semCompositionTAPP-Gucsik2013",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semComposition protocol — Gucsik2013",
  "schema:description": "Described as semiquantitative; BSE images also captured with this instrument at same conditions; EPMA (JEOL JXA-8900R WDS) used for quantitative analyses (out of scope)",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "constituent minerals"
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
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "Freedom from defects, after a prior survey — \"Following a systematic optical microscopecathodoluminescence study of a Kaba thin section, seven representative grains (designated as B-1 through B-7) were selected for further analyses because they did not contain any irregular fracturing or crystallographic imperfections\" (p.2); the same grains carry the microprobe analyses",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "JSM-5410LV",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:description": "Standard SEM",
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "ISIS analysis system (Oxford); detector type not specified",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/SEM/part/EDS-Detector",
          "schema:name": "missing"
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
          "@id": "ex:instrument/SEM/part/Electron-Source",
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
          "@id": "ex:instrument/SEM/part/WDS-Spectrometer"
        }
      ],
      "ada:beamMode": "all: Focused — 'The accelerating voltage was 15 kV and the beam current was 2.0 nA, with a focused beam' (p.2)",
      "ada:acceleratingVoltageDefault": "15 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName",
      "ada:beamDiameterDefault": -9999,
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:mappingBeamDiameterDefault": -9999,
      "ada:mappingBeamMode": "missing",
      "ada:workingDistanceDefault": -9999
    }
  ],
  "ada:monitoredElements": [
    "Mg, Al, Ca, Si, Ti, Cr, Mn, Fe — \"Among the detected elements were Mg, Al, Ca, Si, Ti, Cr, Mn, and Fe\" (p.2). NOTE the sentence attaches these to the WDS X-ray distribution maps; the EDS itself is described only as \"semiquantitative analyses for major elements\" and \"qualitative measurements by EDS\", so the EDS element set is not separately stated"
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "CL (same instrument); BSE Imaging (same instrument, same session); EPMA with WDS (JEOL JXA-8900R, out of scope)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Grain > Analysis point — \"Semiquantitative analyses\" on the same \"seven representative grains (designated as B-1 through B-7)\" of a Kaba thin section (p.2)",
  "ada:analyticalMode": [
    "EDS Point Analysis"
  ],
  "ada:reportedProperties": [
    "mineral composition; forsterite content (Fo) — Mineral compositions of the seven analysed grains, reported for the olivine as forsterite content (\"Fo: 99.2–99.7\", p.1), with WDS X-ray distribution maps alongside; detection limits are stated per element (\"ranged between 0.03 (light element…\", p.2)"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "semComposition",
      "schema:termCode": "semComposition"
    }
  ],
  "schema:actionProcess": {
    "@type": [
      "schema:HowTo"
    ],
    "schema:step": [
      {
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
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
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2,
        "ada:detectionLimitMethod": "missing"
      }
    ]
  },
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:edsAcquisitionMode": "missing",
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semCompositionTAPP-Gucsik2013",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semComposition protocol \u2014 Gucsik2013",
  "schema:description": "Described as semiquantitative; BSE images also captured with this instrument at same conditions; EPMA (JEOL JXA-8900R WDS) used for quantitative analyses (out of scope)",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "constituent minerals"
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
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "Freedom from defects, after a prior survey \u2014 \"Following a systematic optical microscopecathodoluminescence study of a Kaba thin section, seven representative grains (designated as B-1 through B-7) were selected for further analyses because they did not contain any irregular fracturing or crystallographic imperfections\" (p.2); the same grains carry the microprobe analyses",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "JSM-5410LV",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:description": "Standard SEM",
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "ISIS analysis system (Oxford); detector type not specified",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/SEM/part/EDS-Detector",
          "schema:name": "missing"
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
          "@id": "ex:instrument/SEM/part/Electron-Source",
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
          "@id": "ex:instrument/SEM/part/WDS-Spectrometer"
        }
      ],
      "ada:beamMode": "all: Focused \u2014 'The accelerating voltage was 15 kV and the beam current was 2.0 nA, with a focused beam' (p.2)",
      "ada:acceleratingVoltageDefault": "15 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName",
      "ada:beamDiameterDefault": -9999,
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:mappingBeamDiameterDefault": -9999,
      "ada:mappingBeamMode": "missing",
      "ada:workingDistanceDefault": -9999
    }
  ],
  "ada:monitoredElements": [
    "Mg, Al, Ca, Si, Ti, Cr, Mn, Fe \u2014 \"Among the detected elements were Mg, Al, Ca, Si, Ti, Cr, Mn, and Fe\" (p.2). NOTE the sentence attaches these to the WDS X-ray distribution maps; the EDS itself is described only as \"semiquantitative analyses for major elements\" and \"qualitative measurements by EDS\", so the EDS element set is not separately stated"
  ],
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "CL (same instrument); BSE Imaging (same instrument, same session); EPMA with WDS (JEOL JXA-8900R, out of scope)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Grain > Analysis point \u2014 \"Semiquantitative analyses\" on the same \"seven representative grains (designated as B-1 through B-7)\" of a Kaba thin section (p.2)",
  "ada:analyticalMode": [
    "EDS Point Analysis"
  ],
  "ada:reportedProperties": [
    "mineral composition; forsterite content (Fo) \u2014 Mineral compositions of the seven analysed grains, reported for the olivine as forsterite content (\"Fo: 99.2\u201399.7\", p.1), with WDS X-ray distribution maps alongside; detection limits are stated per element (\"ranged between 0.03 (light element\u2026\", p.2)"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "semComposition",
      "schema:termCode": "semComposition"
    }
  ],
  "schema:actionProcess": {
    "@type": [
      "schema:HowTo"
    ],
    "schema:step": [
      {
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
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
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2,
        "ada:detectionLimitMethod": "missing"
      }
    ]
  },
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:edsAcquisitionMode": "missing",
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
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

<ex:semCompositionTAPP-Gucsik2013> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "missing" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:detectionLimitMethod "missing" ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "Described as semiquantitative; BSE images also captured with this instrument at same conditions; EPMA (JEOL JXA-8900R WDS) used for quantitative analyses (out of scope)" ;
    schema1:instrument <ex:instrument/SEM> ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semComposition" ;
            schema1:termCode "semComposition" ] ;
    schema1:name "semComposition protocol — Gucsik2013" ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "CL (same instrument); BSE Imaging (same instrument, same session); EPMA with WDS (JEOL JXA-8900R, out of scope)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analyticalMode "EDS Point Analysis" ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:monitoredElements "Mg, Al, Ca, Si, Ti, Cr, Mn, Fe — \"Among the detected elements were Mg, Al, Ca, Si, Ti, Cr, Mn, and Fe\" (p.2). NOTE the sentence attaches these to the WDS X-ray distribution maps; the EDS itself is described only as \"semiquantitative analyses for major elements\" and \"qualitative measurements by EDS\", so the EDS element set is not separately stated" ;
    ada:reportedProperties "mineral composition; forsterite content (Fo) — Mineral compositions of the seven analysed grains, reported for the olivine as forsterite content (\"Fo: 99.2–99.7\", p.1), with WDS X-ray distribution maps alongside; detection limits are stated per element (\"ranged between 0.03 (light element…\", p.2)" ;
    ada:samplingUnitSelectionCriteriaDefault "Freedom from defects, after a prior survey — \"Following a systematic optical microscopecathodoluminescence study of a Kaba thin section, seven representative grains (designated as B-1 through B-7) were selected for further analyses because they did not contain any irregular fracturing or crystallographic imperfections\" (p.2); the same grains carry the microprobe analyses" ;
    ada:samplingUnitType "Grain > Analysis point — \"Semiquantitative analyses\" on the same \"seven representative grains (designated as B-1 through B-7)\" of a Kaba thin section (p.2)" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "constituent minerals" ;
            ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/backgroundCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/peakCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/primaryCalibrationStandardName> ] ;
    ada:wdsDeadTimeCorrection "missing" .

<ex:instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:description "Standard SEM" ;
    schema1:hasPart <ex:instrument/SEM/part/EDS-Detector>,
        <ex:instrument/SEM/part/Electron-Source>,
        <ex:instrument/SEM/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "JEOL" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "JSM-5410LV" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "15 kV" ;
    ada:beamDiameterDefault -9999 ;
    ada:beamMode "all: Focused — 'The accelerating voltage was 15 kV and the beam current was 2.0 nA, with a focused beam' (p.2)" ;
    ada:mappingBeamCurrentDefault -9999 ;
    ada:mappingBeamDiameterDefault -9999 ;
    ada:mappingBeamMode "missing" ;
    ada:workingDistanceDefault -9999 .

<ex:instrument/SEM/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:description "ISIS analysis system (Oxford); detector type not specified" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "missing" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/backgroundCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Background Counting Time" ;
    schema1:valueName "backgroundCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/peakCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Peak Counting Time" ;
    schema1:valueName "peakCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .


```


### semCompositionTAPP example Izawa2010
semCompositionTAPP instance derived from Izawa et al. 2010 | Tagish Lake (C2) meteorite | EDS Mapping (Leo 440).
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
  "@id": "ex:semCompositionTAPP-Izawa2010",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semComposition protocol — Izawa2010",
  "schema:description": "Full spectral imaging (Quartz XOne): all X-rays recorded per pixel, allowing post-hoc spectral analysis",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "carbonaceous chondrite"
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
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "Located by prior μXRD reconnaissance — the paper's stated strategy is \"an initial, non-destructive in situ reconnaissance step using micro X-ray diffraction (mXRD) ... to identify features of interest, followed by spatially correlated mXRD, scanning electron microscopy with energy-dispersive X-ray spectroscopy (SEM-EDX), and cathodoluminescence (CL) analysis\" (p.2)",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "Zeiss",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Leo 440",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:description": "Standard SEM",
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Gresham light element detector; Quartz XOne EDX analysis system (full spectral imaging)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/SEM/part/EDS-Detector",
          "schema:name": "missing"
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
          "@id": "ex:instrument/SEM/part/Electron-Source",
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
          "@id": "ex:instrument/SEM/part/WDS-Spectrometer"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName",
      "ada:acceleratingVoltageDefault": -9999,
      "ada:beamDiameterDefault": -9999,
      "ada:beamMode": "missing",
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:mappingBeamDiameterDefault": -9999,
      "ada:mappingBeamMode": "missing",
      "ada:workingDistanceDefault": -9999
    }
  ],
  "ada:edsAcquisitionMode": "Map",
  "ada:monitoredElements": [
    "N — the Leo 440 SEM carries \"a Gresham light element detector and a Quartz XOne EDX analysis system, capable of detecting all elements from C to U, with a detection limit of ~0.5 wt% for most elements\" (p.3). That is the detector's range, not the set monitored; the maps' elements are not enumerated"
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Surface Science Western"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "BSE Imaging (same instrument); CL (Hitachi S-2500C); micro-XRD; EPMA (out of scope)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Whole sample (polished thin section) > Phase — \"full spectral imaging, recording all X-rays collected from each pixel location\" over \"polished thin sections\" of Tagish Lake (p.2), read as elemental distribution (p.3)",
  "ada:analyticalMode": [
    "EDS Mapping"
  ],
  "ada:reportedProperties": [
    "elemental distribution (counts per pixel); phase identification (nominal) — Elemental distribution as X-ray maps (counts per pixel, \"full spectral imaging, recording all X-rays collected from each pixel location\", p.3) and the phase identifications read from them (nominal); BSE images give the accompanying textural relationships (nominal)"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "semComposition",
      "schema:termCode": "semComposition"
    }
  ],
  "schema:actionProcess": {
    "@type": [
      "schema:HowTo"
    ],
    "schema:step": [
      {
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
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
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2,
        "ada:detectionLimitMethod": "missing"
      }
    ]
  },
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semCompositionTAPP-Izawa2010",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semComposition protocol \u2014 Izawa2010",
  "schema:description": "Full spectral imaging (Quartz XOne): all X-rays recorded per pixel, allowing post-hoc spectral analysis",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "carbonaceous chondrite"
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
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "Located by prior \u03bcXRD reconnaissance \u2014 the paper's stated strategy is \"an initial, non-destructive in situ reconnaissance step using micro X-ray diffraction (mXRD) ... to identify features of interest, followed by spatially correlated mXRD, scanning electron microscopy with energy-dispersive X-ray spectroscopy (SEM-EDX), and cathodoluminescence (CL) analysis\" (p.2)",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "Zeiss",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Leo 440",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:description": "Standard SEM",
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Gresham light element detector; Quartz XOne EDX analysis system (full spectral imaging)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/SEM/part/EDS-Detector",
          "schema:name": "missing"
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
          "@id": "ex:instrument/SEM/part/Electron-Source",
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
          "@id": "ex:instrument/SEM/part/WDS-Spectrometer"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName",
      "ada:acceleratingVoltageDefault": -9999,
      "ada:beamDiameterDefault": -9999,
      "ada:beamMode": "missing",
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:mappingBeamDiameterDefault": -9999,
      "ada:mappingBeamMode": "missing",
      "ada:workingDistanceDefault": -9999
    }
  ],
  "ada:edsAcquisitionMode": "Map",
  "ada:monitoredElements": [
    "N \u2014 the Leo 440 SEM carries \"a Gresham light element detector and a Quartz XOne EDX analysis system, capable of detecting all elements from C to U, with a detection limit of ~0.5 wt% for most elements\" (p.3). That is the detector's range, not the set monitored; the maps' elements are not enumerated"
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Surface Science Western"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "BSE Imaging (same instrument); CL (Hitachi S-2500C); micro-XRD; EPMA (out of scope)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Whole sample (polished thin section) > Phase \u2014 \"full spectral imaging, recording all X-rays collected from each pixel location\" over \"polished thin sections\" of Tagish Lake (p.2), read as elemental distribution (p.3)",
  "ada:analyticalMode": [
    "EDS Mapping"
  ],
  "ada:reportedProperties": [
    "elemental distribution (counts per pixel); phase identification (nominal) \u2014 Elemental distribution as X-ray maps (counts per pixel, \"full spectral imaging, recording all X-rays collected from each pixel location\", p.3) and the phase identifications read from them (nominal); BSE images give the accompanying textural relationships (nominal)"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "semComposition",
      "schema:termCode": "semComposition"
    }
  ],
  "schema:actionProcess": {
    "@type": [
      "schema:HowTo"
    ],
    "schema:step": [
      {
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
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
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2,
        "ada:detectionLimitMethod": "missing"
      }
    ]
  },
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
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

<ex:semCompositionTAPP-Izawa2010> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "missing" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:detectionLimitMethod "missing" ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "Full spectral imaging (Quartz XOne): all X-rays recorded per pixel, allowing post-hoc spectral analysis" ;
    schema1:instrument <ex:instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Surface Science Western" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semComposition" ;
            schema1:termCode "semComposition" ] ;
    schema1:name "semComposition protocol — Izawa2010" ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "BSE Imaging (same instrument); CL (Hitachi S-2500C); micro-XRD; EPMA (out of scope)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analyticalMode "EDS Mapping" ;
    ada:edsAcquisitionMode "Map" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:monitoredElements "N — the Leo 440 SEM carries \"a Gresham light element detector and a Quartz XOne EDX analysis system, capable of detecting all elements from C to U, with a detection limit of ~0.5 wt% for most elements\" (p.3). That is the detector's range, not the set monitored; the maps' elements are not enumerated" ;
    ada:reportedProperties "elemental distribution (counts per pixel); phase identification (nominal) — Elemental distribution as X-ray maps (counts per pixel, \"full spectral imaging, recording all X-rays collected from each pixel location\", p.3) and the phase identifications read from them (nominal); BSE images give the accompanying textural relationships (nominal)" ;
    ada:samplingUnitSelectionCriteriaDefault "Located by prior μXRD reconnaissance — the paper's stated strategy is \"an initial, non-destructive in situ reconnaissance step using micro X-ray diffraction (mXRD) ... to identify features of interest, followed by spatially correlated mXRD, scanning electron microscopy with energy-dispersive X-ray spectroscopy (SEM-EDX), and cathodoluminescence (CL) analysis\" (p.2)" ;
    ada:samplingUnitType "Whole sample (polished thin section) > Phase — \"full spectral imaging, recording all X-rays collected from each pixel location\" over \"polished thin sections\" of Tagish Lake (p.2), read as elemental distribution (p.3)" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "carbonaceous chondrite" ;
            ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/backgroundCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/peakCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/primaryCalibrationStandardName> ] ;
    ada:wdsDeadTimeCorrection "missing" .

<ex:instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:description "Standard SEM" ;
    schema1:hasPart <ex:instrument/SEM/part/EDS-Detector>,
        <ex:instrument/SEM/part/Electron-Source>,
        <ex:instrument/SEM/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Zeiss" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Leo 440" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault -9999 ;
    ada:beamDiameterDefault -9999 ;
    ada:beamMode "missing" ;
    ada:mappingBeamCurrentDefault -9999 ;
    ada:mappingBeamDiameterDefault -9999 ;
    ada:mappingBeamMode "missing" ;
    ada:workingDistanceDefault -9999 .

<ex:instrument/SEM/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:description "Gresham light element detector; Quartz XOne EDX analysis system (full spectral imaging)" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "missing" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/backgroundCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Background Counting Time" ;
    schema1:valueName "backgroundCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/peakCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Peak Counting Time" ;
    schema1:valueName "peakCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .


```


### semCompositionTAPP example Izawa2010-2
semCompositionTAPP instance derived from Izawa et al. 2010 | Tagish Lake (C2) meteorite | EDS Point Analysis (Leo 1540 FIB/SEM CrossBeam).
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
  "@id": "ex:semCompositionTAPP-Izawa2010-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semComposition protocol — Izawa2010-2",
  "schema:description": "Additional BSE and EDX analyses also carried out with Hitachi S-4300SE/N (Texas Tech) and Hitachi SU6600 (UWO) — not captured as separate assessment columns Reported detail: ada:edsAcquisitionMode = Point / spot; Map.",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "carbonaceous chondrite"
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
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "Follow-up on features already located — this is the third stage of the paper's strategy, \"finally higher resolution SEM-BSE mapping to establish spatial context for textural variation\" (p.2), on features identified by the earlier μXRD and SEM-EDX/CL stages",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "Zeiss",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Leo 1540 FIB/SEM CrossBeam",
        "@type": [
          "schema:ProductModel"
        ]
      },
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
          "@id": "ex:instrument/SEM/part/Electron-Source",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Oxford Instruments INCA EDX system",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/SEM/part/EDS-Detector",
          "schema:name": "missing"
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
          "@id": "ex:instrument/SEM/part/WDS-Spectrometer"
        }
      ],
      "schema:description": "FIB-SEM dual-beam",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName",
      "ada:acceleratingVoltageDefault": -9999,
      "ada:beamDiameterDefault": -9999,
      "ada:beamMode": "missing",
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:mappingBeamDiameterDefault": -9999,
      "ada:mappingBeamMode": "missing",
      "ada:workingDistanceDefault": -9999
    }
  ],
  "ada:edsAcquisitionMode": "Point",
  "ada:monitoredElements": [
    "N — the Leo 1540 FIB/SEM CrossBeam is \"equipped with an Oxford Instruments INCA EDX system allowing for elemental analysis\" (p.3); no element set is stated"
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Nanofabrication Laboratory, University of Western Ontario"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "BSE Imaging (same instrument); CL (Hitachi S-2500C); micro-XRD; EPMA (out of scope)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Phase > Analysis point — \"High-resolution BSE imaging and EDX spot analysis were carried out with the Leo 1540 FIB/SEM CrossBeam field emission SEM\" (p.3)",
  "ada:analyticalMode": [
    "EDS Point Analysis"
  ],
  "ada:reportedProperties": [
    "elemental composition of the analysed phases; phase identification (nominal) — Elemental compositions of the analysed phases, used with the μXRD and CL data for phase identification (nominal); the EDX system detects \"all elements from C to U, with a detection limit of 0.5 wt% for most elements\" (p.3)"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "semComposition",
      "schema:termCode": "semComposition"
    }
  ],
  "schema:actionProcess": {
    "@type": [
      "schema:HowTo"
    ],
    "schema:step": [
      {
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
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
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2,
        "ada:detectionLimitMethod": "missing"
      }
    ]
  },
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semCompositionTAPP-Izawa2010-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semComposition protocol \u2014 Izawa2010-2",
  "schema:description": "Additional BSE and EDX analyses also carried out with Hitachi S-4300SE/N (Texas Tech) and Hitachi SU6600 (UWO) \u2014 not captured as separate assessment columns Reported detail: ada:edsAcquisitionMode = Point / spot; Map.",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "carbonaceous chondrite"
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
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "Follow-up on features already located \u2014 this is the third stage of the paper's strategy, \"finally higher resolution SEM-BSE mapping to establish spatial context for textural variation\" (p.2), on features identified by the earlier \u03bcXRD and SEM-EDX/CL stages",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "Zeiss",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Leo 1540 FIB/SEM CrossBeam",
        "@type": [
          "schema:ProductModel"
        ]
      },
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
          "@id": "ex:instrument/SEM/part/Electron-Source",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Oxford Instruments INCA EDX system",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/SEM/part/EDS-Detector",
          "schema:name": "missing"
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
          "@id": "ex:instrument/SEM/part/WDS-Spectrometer"
        }
      ],
      "schema:description": "FIB-SEM dual-beam",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName",
      "ada:acceleratingVoltageDefault": -9999,
      "ada:beamDiameterDefault": -9999,
      "ada:beamMode": "missing",
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:mappingBeamDiameterDefault": -9999,
      "ada:mappingBeamMode": "missing",
      "ada:workingDistanceDefault": -9999
    }
  ],
  "ada:edsAcquisitionMode": "Point",
  "ada:monitoredElements": [
    "N \u2014 the Leo 1540 FIB/SEM CrossBeam is \"equipped with an Oxford Instruments INCA EDX system allowing for elemental analysis\" (p.3); no element set is stated"
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Nanofabrication Laboratory, University of Western Ontario"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "BSE Imaging (same instrument); CL (Hitachi S-2500C); micro-XRD; EPMA (out of scope)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Phase > Analysis point \u2014 \"High-resolution BSE imaging and EDX spot analysis were carried out with the Leo 1540 FIB/SEM CrossBeam field emission SEM\" (p.3)",
  "ada:analyticalMode": [
    "EDS Point Analysis"
  ],
  "ada:reportedProperties": [
    "elemental composition of the analysed phases; phase identification (nominal) \u2014 Elemental compositions of the analysed phases, used with the \u03bcXRD and CL data for phase identification (nominal); the EDX system detects \"all elements from C to U, with a detection limit of 0.5 wt% for most elements\" (p.3)"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "semComposition",
      "schema:termCode": "semComposition"
    }
  ],
  "schema:actionProcess": {
    "@type": [
      "schema:HowTo"
    ],
    "schema:step": [
      {
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
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
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2,
        "ada:detectionLimitMethod": "missing"
      }
    ]
  },
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
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

<ex:semCompositionTAPP-Izawa2010-2> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "missing" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:detectionLimitMethod "missing" ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "Additional BSE and EDX analyses also carried out with Hitachi S-4300SE/N (Texas Tech) and Hitachi SU6600 (UWO) — not captured as separate assessment columns Reported detail: ada:edsAcquisitionMode = Point / spot; Map." ;
    schema1:instrument <ex:instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Nanofabrication Laboratory, University of Western Ontario" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semComposition" ;
            schema1:termCode "semComposition" ] ;
    schema1:name "semComposition protocol — Izawa2010-2" ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "BSE Imaging (same instrument); CL (Hitachi S-2500C); micro-XRD; EPMA (out of scope)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analyticalMode "EDS Point Analysis" ;
    ada:edsAcquisitionMode "Point" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:monitoredElements "N — the Leo 1540 FIB/SEM CrossBeam is \"equipped with an Oxford Instruments INCA EDX system allowing for elemental analysis\" (p.3); no element set is stated" ;
    ada:reportedProperties "elemental composition of the analysed phases; phase identification (nominal) — Elemental compositions of the analysed phases, used with the μXRD and CL data for phase identification (nominal); the EDX system detects \"all elements from C to U, with a detection limit of 0.5 wt% for most elements\" (p.3)" ;
    ada:samplingUnitSelectionCriteriaDefault "Follow-up on features already located — this is the third stage of the paper's strategy, \"finally higher resolution SEM-BSE mapping to establish spatial context for textural variation\" (p.2), on features identified by the earlier μXRD and SEM-EDX/CL stages" ;
    ada:samplingUnitType "Phase > Analysis point — \"High-resolution BSE imaging and EDX spot analysis were carried out with the Leo 1540 FIB/SEM CrossBeam field emission SEM\" (p.3)" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "carbonaceous chondrite" ;
            ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/backgroundCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/peakCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/primaryCalibrationStandardName> ] ;
    ada:wdsDeadTimeCorrection "missing" .

<ex:instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:description "FIB-SEM dual-beam" ;
    schema1:hasPart <ex:instrument/SEM/part/EDS-Detector>,
        <ex:instrument/SEM/part/Electron-Source>,
        <ex:instrument/SEM/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Zeiss" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Leo 1540 FIB/SEM CrossBeam" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault -9999 ;
    ada:beamDiameterDefault -9999 ;
    ada:beamMode "missing" ;
    ada:mappingBeamCurrentDefault -9999 ;
    ada:mappingBeamDiameterDefault -9999 ;
    ada:mappingBeamMode "missing" ;
    ada:workingDistanceDefault -9999 .

<ex:instrument/SEM/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:description "Oxford Instruments INCA EDX system" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Unknown" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/backgroundCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Background Counting Time" ;
    schema1:valueName "backgroundCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/peakCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Peak Counting Time" ;
    schema1:valueName "peakCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .


```


### semCompositionTAPP example Pascucci2026
semCompositionTAPP instance derived from Pascucci et al. 2026 | NWA 7317 CR6 chondrite | EDS Point Analysis (Zeiss Supra 40 FE-SEM, 20 kV).
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
  "@id": "ex:semCompositionTAPP-Pascucci2026",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semComposition protocol — Pascucci2026",
  "schema:description": "Spot analysis: 20 kV, 30 µm aperture, 30 s live time per spot, maximum process time (Oxford INCA Energy) Reported detail: ada:edsAcquisitionMode = Spot analysis.",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "carbonaceous chondrite"
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
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "Spatial co-registration with the spectral imagery — the SEM work targets \"almost the same portion of the VIS-IR SPIM images\" (p.4), so that the two datasets can be compared on the same area of the slab",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "Zeiss",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Supra 40",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Field emission gun (FEG) — subtype not specified",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/SEM/part/Electron-Source",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Oxford INCA Energy 350; X-ACT LN2-free Silicon Drift Detector (SDD)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/SEM/part/EDS-Detector",
          "schema:name": "missing"
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
          "@id": "ex:instrument/SEM/part/WDS-Spectrometer"
        }
      ],
      "schema:description": "ESEM",
      "ada:acceleratingVoltageDefault": "20 kV",
      "ada:beamDiameterDefault": "N — a 30 μm aperture is stated (p.3), not a beam diameter",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName",
      "ada:beamMode": "missing",
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:mappingBeamDiameterDefault": -9999,
      "ada:mappingBeamMode": "missing",
      "ada:workingDistanceDefault": -9999
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/semCompositionTAPP/beamDamageMinimizationDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "beamDamageMinimizationDefault",
      "schema:name": "Beam Damage Minimization",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "all: SEM-EDS run only after the SPIM reflectance measurements — 'This was done only after the SPIM reflectance acquisitions to try to avoid charging effects and by also reducing thermal damage' (p.3)"
    },
    {
      "@id": "ada:parameter/semCompositionTAPP/chamberPressureDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "chamberPressureDefault",
      "schema:name": "Chamber Pressure",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": "High vacuum"
    },
    {
      "@id": "ada:parameter/semCompositionTAPP/edsSpectralProcessingType",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/semCompositionTAPP/edsSpectralProcessingType"
        }
      ],
      "schema:name": "EDS Spectral Processing Type",
      "schema:value": "Semi-quantitative analysis with virtual standards (Oxford INCA Energy); mineral phase determination from atomic % of constituent elements"
    }
  ],
  "ada:edsAcquisitionMode": "N/A",
  "ada:targetSpeciesTemplate": {
    "ada:targetSpeciesDeclaration": "N — no element set is stated for the SEM-EDS spot analyses; the list 'Mg, Si, Fe, Ni, S, Na, Ca, Al' formerly here is not in the paper",
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
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/beamCurrent",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "beamCurrent",
        "schema:name": "Beam Current",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/wdsSpectrometerChannel",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "wdsSpectrometerChannel",
        "schema:name": "WDS Spectrometer Channel",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/xRayBackgroundCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayBackgroundCorrectionMethod",
        "schema:name": "X-ray Background Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/timeDependentIntensityCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "timeDependentIntensityCorrection",
        "schema:name": "Time-Dependent Intensity Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/targetSpeciesEstimationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "targetSpeciesEstimationMethod",
        "schema:name": "Target Species Estimation Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/blankCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "blankCorrection",
        "schema:name": "Blank Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/xRayLineOverlapCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayLineOverlapCorrectionsApplied",
        "schema:name": "X-ray Line Overlap Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/interferingElements",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingElements",
        "schema:name": "Interfering Elements",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/interferenceCorrectionStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionStandard",
        "schema:name": "Interference Correction Standard",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/analyticalPrecision",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalPrecision",
        "schema:name": "Analytical Precision",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/analyticalAccuracy",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracy",
        "schema:name": "Analytical Accuracy",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      }
    ],
    "ada:defaultTargetSpecies": []
  },
  "ada:edsLiveTimePerPointOrPixelDefault": "30 s live time per spot analysis",
  "ada:monitoredElements": [
    "N — the Zeiss Supra 40 FE-SEM carries an Oxford INCA Energy 350 EDS with an X-ACT SDD (p.3), but no element set is given for the SEM-EDS work. The paper's \"Si, Fe, Ca, Al, and S\" list (p.6) belongs to its EMPA-WDS mapping on a JEOL JXA/8230 — a different instrument and a different procedure — and is deliberately not read across"
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "CNR IMAA (Institute of Methodologies for Environmental Analysis), Italian National Research Council, Potenza, Italy"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "BSE Imaging (Zeiss Supra 40 FE-SEM); SE Imaging (Zeiss Supra 40 FE-SEM); EMPA-WDS (JEOL JXA-8230, separate instrument); VIS-IR spectroscopy (SPIM)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Phase > Analysis point — \"semi-quantitative analyses with virtual standards present within the INCA software\" (p.3), to \"determine its elemental composition\" for the \"NWA 7317 slab\", a \"small fragment of about 10 × 6 mm\" embedded in epoxy and polished (pp.3–4)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "acquisition",
      "schema:name": "Oxford INCA Energy"
    },
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Oxford INCA Energy (semi-quantitative phase determination from atomic proportions)"
    }
  ],
  "ada:analyticalMode": [
    "EDS Point Analysis"
  ],
  "ada:reportedProperties": [
    "atomic proportions of the constituent elements (%); phase identification (nominal) — Atomic proportions of the constituent elements (%), from which \"mineral phases were determined from atomic proportions in percentages (%) of constituent elements and compared to the atomic proportions of constituent elements in stoichiometric proportions\" (p.4); the phase identification is the nominal output"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Embedded in epoxy, polished to ¼ µm level, sputtered with 30-nm-thick carbon film",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
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
          "bios:LabProcess"
        ],
        "schema:position": 2,
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
      "schema:name": "semComposition",
      "schema:termCode": "semComposition"
    }
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semCompositionTAPP-Pascucci2026",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semComposition protocol \u2014 Pascucci2026",
  "schema:description": "Spot analysis: 20 kV, 30 \u00b5m aperture, 30 s live time per spot, maximum process time (Oxford INCA Energy) Reported detail: ada:edsAcquisitionMode = Spot analysis.",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "carbonaceous chondrite"
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
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "Spatial co-registration with the spectral imagery \u2014 the SEM work targets \"almost the same portion of the VIS-IR SPIM images\" (p.4), so that the two datasets can be compared on the same area of the slab",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "Zeiss",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Supra 40",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Field emission gun (FEG) \u2014 subtype not specified",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/SEM/part/Electron-Source",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Oxford INCA Energy 350; X-ACT LN2-free Silicon Drift Detector (SDD)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/SEM/part/EDS-Detector",
          "schema:name": "missing"
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
          "@id": "ex:instrument/SEM/part/WDS-Spectrometer"
        }
      ],
      "schema:description": "ESEM",
      "ada:acceleratingVoltageDefault": "20 kV",
      "ada:beamDiameterDefault": "N \u2014 a 30 \u03bcm aperture is stated (p.3), not a beam diameter",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName",
      "ada:beamMode": "missing",
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:mappingBeamDiameterDefault": -9999,
      "ada:mappingBeamMode": "missing",
      "ada:workingDistanceDefault": -9999
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/semCompositionTAPP/beamDamageMinimizationDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "beamDamageMinimizationDefault",
      "schema:name": "Beam Damage Minimization",
      "ada:dataType": "string",
      "ada:fieldScope": "session",
      "schema:defaultValue": "all: SEM-EDS run only after the SPIM reflectance measurements \u2014 'This was done only after the SPIM reflectance acquisitions to try to avoid charging effects and by also reducing thermal damage' (p.3)"
    },
    {
      "@id": "ada:parameter/semCompositionTAPP/chamberPressureDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "chamberPressureDefault",
      "schema:name": "Chamber Pressure",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": "High vacuum"
    },
    {
      "@id": "ada:parameter/semCompositionTAPP/edsSpectralProcessingType",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/semCompositionTAPP/edsSpectralProcessingType"
        }
      ],
      "schema:name": "EDS Spectral Processing Type",
      "schema:value": "Semi-quantitative analysis with virtual standards (Oxford INCA Energy); mineral phase determination from atomic % of constituent elements"
    }
  ],
  "ada:edsAcquisitionMode": "N/A",
  "ada:targetSpeciesTemplate": {
    "ada:targetSpeciesDeclaration": "N \u2014 no element set is stated for the SEM-EDS spot analyses; the list 'Mg, Si, Fe, Ni, S, Na, Ca, Al' formerly here is not in the paper",
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
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/beamCurrent",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "beamCurrent",
        "schema:name": "Beam Current",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/wdsSpectrometerChannel",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "wdsSpectrometerChannel",
        "schema:name": "WDS Spectrometer Channel",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/xRayBackgroundCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayBackgroundCorrectionMethod",
        "schema:name": "X-ray Background Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/timeDependentIntensityCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "timeDependentIntensityCorrection",
        "schema:name": "Time-Dependent Intensity Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/targetSpeciesEstimationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "targetSpeciesEstimationMethod",
        "schema:name": "Target Species Estimation Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/blankCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "blankCorrection",
        "schema:name": "Blank Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/xRayLineOverlapCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayLineOverlapCorrectionsApplied",
        "schema:name": "X-ray Line Overlap Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/interferingElements",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingElements",
        "schema:name": "Interfering Elements",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/interferenceCorrectionStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionStandard",
        "schema:name": "Interference Correction Standard",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/analyticalPrecision",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalPrecision",
        "schema:name": "Analytical Precision",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/analyticalAccuracy",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracy",
        "schema:name": "Analytical Accuracy",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      }
    ],
    "ada:defaultTargetSpecies": []
  },
  "ada:edsLiveTimePerPointOrPixelDefault": "30 s live time per spot analysis",
  "ada:monitoredElements": [
    "N \u2014 the Zeiss Supra 40 FE-SEM carries an Oxford INCA Energy 350 EDS with an X-ACT SDD (p.3), but no element set is given for the SEM-EDS work. The paper's \"Si, Fe, Ca, Al, and S\" list (p.6) belongs to its EMPA-WDS mapping on a JEOL JXA/8230 \u2014 a different instrument and a different procedure \u2014 and is deliberately not read across"
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "CNR IMAA (Institute of Methodologies for Environmental Analysis), Italian National Research Council, Potenza, Italy"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "BSE Imaging (Zeiss Supra 40 FE-SEM); SE Imaging (Zeiss Supra 40 FE-SEM); EMPA-WDS (JEOL JXA-8230, separate instrument); VIS-IR spectroscopy (SPIM)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Phase > Analysis point \u2014 \"semi-quantitative analyses with virtual standards present within the INCA software\" (p.3), to \"determine its elemental composition\" for the \"NWA 7317 slab\", a \"small fragment of about 10 \u00d7 6 mm\" embedded in epoxy and polished (pp.3\u20134)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "acquisition",
      "schema:name": "Oxford INCA Energy"
    },
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Oxford INCA Energy (semi-quantitative phase determination from atomic proportions)"
    }
  ],
  "ada:analyticalMode": [
    "EDS Point Analysis"
  ],
  "ada:reportedProperties": [
    "atomic proportions of the constituent elements (%); phase identification (nominal) \u2014 Atomic proportions of the constituent elements (%), from which \"mineral phases were determined from atomic proportions in percentages (%) of constituent elements and compared to the atomic proportions of constituent elements in stoichiometric proportions\" (p.4); the phase identification is the nominal output"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Embedded in epoxy, polished to \u00bc \u00b5m level, sputtered with 30-nm-thick carbon film",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
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
          "bios:LabProcess"
        ],
        "schema:position": 2,
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
      "schema:name": "semComposition",
      "schema:termCode": "semComposition"
    }
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
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

<ex:semCompositionTAPP-Pascucci2026> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Embedded in epoxy, polished to ¼ µm level, sputtered with 30-nm-thick carbon film" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:detectionLimitMethod "missing" ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/beamDamageMinimizationDefault>,
        <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/chamberPressureDefault>,
        <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/edsSpectralProcessingType> ;
    schema1:datePublished "missing" ;
    schema1:description "Spot analysis: 20 kV, 30 µm aperture, 30 s live time per spot, maximum process time (Oxford INCA Energy) Reported detail: ada:edsAcquisitionMode = Spot analysis." ;
    schema1:instrument <ex:instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "CNR IMAA (Institute of Methodologies for Environmental Analysis), Italian National Research Council, Potenza, Italy" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semComposition" ;
            schema1:termCode "semComposition" ] ;
    schema1:name "semComposition protocol — Pascucci2026" ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "BSE Imaging (Zeiss Supra 40 FE-SEM); SE Imaging (Zeiss Supra 40 FE-SEM); EMPA-WDS (JEOL JXA-8230, separate instrument); VIS-IR spectroscopy (SPIM)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analyticalMode "EDS Point Analysis" ;
    ada:edsAcquisitionMode "N/A" ;
    ada:edsLiveTimePerPointOrPixelDefault "30 s live time per spot analysis" ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:monitoredElements "N — the Zeiss Supra 40 FE-SEM carries an Oxford INCA Energy 350 EDS with an X-ACT SDD (p.3), but no element set is given for the SEM-EDS work. The paper's \"Si, Fe, Ca, Al, and S\" list (p.6) belongs to its EMPA-WDS mapping on a JEOL JXA/8230 — a different instrument and a different procedure — and is deliberately not read across" ;
    ada:reportedProperties "atomic proportions of the constituent elements (%); phase identification (nominal) — Atomic proportions of the constituent elements (%), from which \"mineral phases were determined from atomic proportions in percentages (%) of constituent elements and compared to the atomic proportions of constituent elements in stoichiometric proportions\" (p.4); the phase identification is the nominal output" ;
    ada:samplingUnitSelectionCriteriaDefault "Spatial co-registration with the spectral imagery — the SEM work targets \"almost the same portion of the VIS-IR SPIM images\" (p.4), so that the two datasets can be compared on the same area of the slab" ;
    ada:samplingUnitType "Phase > Analysis point — \"semi-quantitative analyses with virtual standards present within the INCA software\" (p.3), to \"determine its elemental composition\" for the \"NWA 7317 slab\", a \"small fragment of about 10 × 6 mm\" embedded in epoxy and polished (pp.3–4)" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "carbonaceous chondrite" ;
            ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/backgroundCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/peakCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/primaryCalibrationStandardName> ] ;
    ada:targetSpeciesTemplate [ ada:targetSpeciesColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetSpecies" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/analyticalAccuracy>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/analyticalPrecision>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/beamCurrent>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/blankCorrection>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/interferenceCorrectionStandard>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/interferingElements>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/targetSpeciesEstimationMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/timeDependentIntensityCorrection>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/wdsSpectrometerChannel>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/xRayBackgroundCorrectionMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/xRayLineOverlapCorrectionsApplied> ;
            ada:targetSpeciesDeclaration "N — no element set is stated for the SEM-EDS spot analyses; the list 'Mg, Si, Fe, Ni, S, Na, Ca, Al' formerly here is not in the paper" ] ;
    ada:wdsDeadTimeCorrection "missing" ;
    bios:computationalTool [ schema1:name "Oxford INCA Energy (semi-quantitative phase determination from atomic proportions)" ;
            ada:toolRole "dataReduction" ],
        [ schema1:name "Oxford INCA Energy" ;
            ada:toolRole "acquisition" ] .

<ex:instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:description "ESEM" ;
    schema1:hasPart <ex:instrument/SEM/part/EDS-Detector>,
        <ex:instrument/SEM/part/Electron-Source>,
        <ex:instrument/SEM/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Zeiss" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Supra 40" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "20 kV" ;
    ada:beamDiameterDefault "N — a 30 μm aperture is stated (p.3), not a beam diameter" ;
    ada:beamMode "missing" ;
    ada:mappingBeamCurrentDefault -9999 ;
    ada:mappingBeamDiameterDefault -9999 ;
    ada:mappingBeamMode "missing" ;
    ada:workingDistanceDefault -9999 .

<ex:instrument/SEM/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:description "Oxford INCA Energy 350; X-ACT LN2-free Silicon Drift Detector (SDD)" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Field emission gun (FEG) — subtype not specified" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/semCompositionTAPP/beamDamageMinimizationDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "all: SEM-EDS run only after the SPIM reflectance measurements — 'This was done only after the SPIM reflectance acquisitions to try to avoid charging effects and by also reducing thermal damage' (p.3)" ;
    schema1:name "Beam Damage Minimization" ;
    schema1:valueName "beamDamageMinimizationDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/semCompositionTAPP/chamberPressureDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "High vacuum" ;
    schema1:name "Chamber Pressure" ;
    schema1:valueName "chamberPressureDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/backgroundCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Background Counting Time" ;
    schema1:valueName "backgroundCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/peakCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Peak Counting Time" ;
    schema1:valueName "peakCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/analyticalAccuracy> a schema1:PropertyValueSpecification ;
    schema1:name "Analytical Accuracy" ;
    schema1:valueName "analyticalAccuracy" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/analyticalPrecision> a schema1:PropertyValueSpecification ;
    schema1:name "Analytical Precision" ;
    schema1:valueName "analyticalPrecision" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/beamCurrent> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Beam Current" ;
    schema1:valueName "beamCurrent" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/blankCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Blank Correction" ;
    schema1:valueName "blankCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/interferenceCorrectionStandard> a schema1:PropertyValueSpecification ;
    schema1:name "Interference Correction Standard" ;
    schema1:valueName "interferenceCorrectionStandard" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/interferingElements> a schema1:PropertyValueSpecification ;
    schema1:name "Interfering Elements" ;
    schema1:valueName "interferingElements" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/targetSpeciesEstimationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Target Species Estimation Method" ;
    schema1:valueName "targetSpeciesEstimationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/timeDependentIntensityCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Time-Dependent Intensity Correction" ;
    schema1:valueName "timeDependentIntensityCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/wdsSpectrometerChannel> a schema1:PropertyValueSpecification ;
    schema1:name "WDS Spectrometer Channel" ;
    schema1:valueName "wdsSpectrometerChannel" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/xRayBackgroundCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "X-ray Background Correction Method" ;
    schema1:valueName "xRayBackgroundCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/xRayLineOverlapCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "X-ray Line Overlap Corrections Applied" ;
    schema1:valueName "xRayLineOverlapCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/semCompositionTAPP/edsSpectralProcessingType> a schema1:PropertyValue ;
    schema1:name "EDS Spectral Processing Type" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/edsSpectralProcessingType> ;
    schema1:value "Semi-quantitative analysis with virtual standards (Oxford INCA Energy); mineral phase determination from atomic % of constituent elements" .


```


### semCompositionTAPP example Pascucci2026-2
semCompositionTAPP instance derived from Pascucci et al. 2026 | NWA 7317 CR6 chondrite | EDS Mapping (Zeiss Supra 40 FE-SEM, 20 kV).
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
  "@id": "ex:semCompositionTAPP-Pascucci2026-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semComposition protocol — Pascucci2026-2",
  "schema:description": "EDS mapping: 20 kV, 60 µm aperture, 5 ms dwell per pixel, 1024×768 pixels, 2.5 µm pixel size, ~10 h total; element maps co-registered with BSE images Reported detail: ada:edsAcquisitionMode = Element mapping.",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "carbonaceous chondrite"
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
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "Spatial co-registration with the spectral imagery — the SEM work targets \"almost the same portion of the VIS-IR SPIM images\" (p.4), so that the two datasets can be compared on the same area of the slab",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "Zeiss",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Supra 40",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Field emission gun (FEG) — subtype not specified",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/SEM/part/Electron-Source",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Oxford INCA Energy 350; X-ACT LN2-free Silicon Drift Detector (SDD)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/SEM/part/EDS-Detector",
          "schema:name": "missing"
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
          "@id": "ex:instrument/SEM/part/WDS-Spectrometer"
        }
      ],
      "schema:description": "ESEM",
      "ada:acceleratingVoltageDefault": "20 kV",
      "ada:mappingBeamDiameterDefault": "N — a 60 μm aperture is stated (p.3), not a beam diameter",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName",
      "ada:beamDiameterDefault": -9999,
      "ada:beamMode": "missing",
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:mappingBeamMode": "missing",
      "ada:workingDistanceDefault": -9999
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/semCompositionTAPP/chamberPressureDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "chamberPressureDefault",
      "schema:name": "Chamber Pressure",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": "High vacuum"
    },
    {
      "@id": "ada:parameter/semCompositionTAPP/edsSpectralProcessingType",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/semCompositionTAPP/edsSpectralProcessingType"
        }
      ],
      "schema:name": "EDS Spectral Processing Type",
      "schema:value": "Semi-quantitative analysis with virtual standards (Oxford INCA Energy); mineral phase determination from atomic % of constituent elements"
    }
  ],
  "ada:edsAcquisitionMode": "Map",
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "O",
      "Si",
      "Mg",
      "Fe",
      "Al",
      "P",
      "Cr",
      "Ca",
      "Na",
      "S",
      "Ni"
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
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/beamCurrent",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "beamCurrent",
        "schema:name": "Beam Current",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/wdsSpectrometerChannel",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "wdsSpectrometerChannel",
        "schema:name": "WDS Spectrometer Channel",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/xRayBackgroundCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayBackgroundCorrectionMethod",
        "schema:name": "X-ray Background Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/timeDependentIntensityCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "timeDependentIntensityCorrection",
        "schema:name": "Time-Dependent Intensity Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/targetSpeciesEstimationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "targetSpeciesEstimationMethod",
        "schema:name": "Target Species Estimation Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/blankCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "blankCorrection",
        "schema:name": "Blank Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/xRayLineOverlapCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayLineOverlapCorrectionsApplied",
        "schema:name": "X-ray Line Overlap Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/interferingElements",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingElements",
        "schema:name": "Interfering Elements",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/interferenceCorrectionStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionStandard",
        "schema:name": "Interference Correction Standard",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/analyticalPrecision",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalPrecision",
        "schema:name": "Analytical Precision",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/analyticalAccuracy",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracy",
        "schema:name": "Analytical Accuracy",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:edsLiveTimePerPointOrPixelDefault": "5 ms dwell time per pixel",
  "ada:stepSizePixelSizeDefault": "2.5 µm",
  "ada:monitoredElements": [
    "O, Si, Mg, Fe, Al, P, Cr, Ca, Na, S, Ni — the SEM-EDS maps give 'a map on a pixel-by-pixel basis of the main elements (O, Si, Mg, Fe, Al, P, Cr, Ca, Na, S, Ni)', and the Cameo+ energy threshold covers 'Si, Mg, Fe, Al, P, Cr, Ca, Na, S, Ni, Ti'. The 'Si, Fe, Ca, Al, and S' list belongs to the EMPA-WDS mapping, a different procedure"
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "CNR IMAA (Institute of Methodologies for Environmental Analysis), Italian National Research Council, Potenza, Italy"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "BSE Imaging (Zeiss Supra 40 FE-SEM); SE Imaging (Zeiss Supra 40 FE-SEM); EMPA-WDS (JEOL JXA-8230, separate instrument); VIS-IR spectroscopy (SPIM)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Whole sample (polished slab) > Phase — elemental mapping of the \"NWA 7317 slab\", a \"small fragment of about 10 × 6 mm\" embedded in epoxy and polished (pp.3–4), acquired on \"almost the same portion of the VIS-IR SPIM images\" (p.4) so the two datasets can be compared pixel for pixel",
  "bios:computationalTool": [
    {
      "ada:toolRole": "acquisition",
      "schema:name": "Oxford INCA Energy"
    },
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Oxford INCA Energy (semi-quantitative phase determination from atomic proportions)"
    }
  ],
  "ada:analyticalMode": [
    "EDS Mapping"
  ],
  "ada:reportedProperties": [
    "element maps (pixel by pixel); Cameo+ energy-colour map (nominal); mineral phase map (nominal) — INCA gives 'a map on a pixel-by-pixel basis of the main elements (O, Si, Mg, Fe, Al, P, Cr, Ca, Na, S, Ni) so to derive the distribution of each mineral phase'; the SEM-EDS area is '10.5 × 4.0 mm wide'. The 'Si, Fe, Ca, Al, and S' maps at 3 μm resolution are the EMPA-WDS mapping's, a different procedure"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Embedded in epoxy, polished to ¼ µm level, sputtered with 30-nm-thick carbon film",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
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
          "bios:LabProcess"
        ],
        "schema:position": 2,
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
      "schema:name": "semComposition",
      "schema:termCode": "semComposition"
    }
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:wdsDeadTimeCorrection": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semCompositionTAPP-Pascucci2026-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semComposition protocol \u2014 Pascucci2026-2",
  "schema:description": "EDS mapping: 20 kV, 60 \u00b5m aperture, 5 ms dwell per pixel, 1024\u00d7768 pixels, 2.5 \u00b5m pixel size, ~10 h total; element maps co-registered with BSE images Reported detail: ada:edsAcquisitionMode = Element mapping.",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "carbonaceous chondrite"
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
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "Spatial co-registration with the spectral imagery \u2014 the SEM work targets \"almost the same portion of the VIS-IR SPIM images\" (p.4), so that the two datasets can be compared on the same area of the slab",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "Zeiss",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Supra 40",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Field emission gun (FEG) \u2014 subtype not specified",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/SEM/part/Electron-Source",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Oxford INCA Energy 350; X-ACT LN2-free Silicon Drift Detector (SDD)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/SEM/part/EDS-Detector",
          "schema:name": "missing"
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
          "@id": "ex:instrument/SEM/part/WDS-Spectrometer"
        }
      ],
      "schema:description": "ESEM",
      "ada:acceleratingVoltageDefault": "20 kV",
      "ada:mappingBeamDiameterDefault": "N \u2014 a 60 \u03bcm aperture is stated (p.3), not a beam diameter",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName",
      "ada:beamDiameterDefault": -9999,
      "ada:beamMode": "missing",
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:mappingBeamMode": "missing",
      "ada:workingDistanceDefault": -9999
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/semCompositionTAPP/chamberPressureDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "chamberPressureDefault",
      "schema:name": "Chamber Pressure",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": "High vacuum"
    },
    {
      "@id": "ada:parameter/semCompositionTAPP/edsSpectralProcessingType",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/semCompositionTAPP/edsSpectralProcessingType"
        }
      ],
      "schema:name": "EDS Spectral Processing Type",
      "schema:value": "Semi-quantitative analysis with virtual standards (Oxford INCA Energy); mineral phase determination from atomic % of constituent elements"
    }
  ],
  "ada:edsAcquisitionMode": "Map",
  "ada:targetSpeciesTemplate": {
    "ada:defaultTargetSpecies": [
      "O",
      "Si",
      "Mg",
      "Fe",
      "Al",
      "P",
      "Cr",
      "Ca",
      "Na",
      "S",
      "Ni"
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
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/beamCurrent",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "beamCurrent",
        "schema:name": "Beam Current",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/wdsSpectrometerChannel",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "wdsSpectrometerChannel",
        "schema:name": "WDS Spectrometer Channel",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/xRayBackgroundCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayBackgroundCorrectionMethod",
        "schema:name": "X-ray Background Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/timeDependentIntensityCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "timeDependentIntensityCorrection",
        "schema:name": "Time-Dependent Intensity Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/targetSpeciesEstimationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "targetSpeciesEstimationMethod",
        "schema:name": "Target Species Estimation Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/blankCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "blankCorrection",
        "schema:name": "Blank Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/xRayLineOverlapCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "xRayLineOverlapCorrectionsApplied",
        "schema:name": "X-ray Line Overlap Corrections Applied",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/interferingElements",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingElements",
        "schema:name": "Interfering Elements",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/interferenceCorrectionStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionStandard",
        "schema:name": "Interference Correction Standard",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/analyticalPrecision",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalPrecision",
        "schema:name": "Analytical Precision",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/analyticalAccuracy",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracy",
        "schema:name": "Analytical Accuracy",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:targetSpeciesColumn/semCompositionTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:edsLiveTimePerPointOrPixelDefault": "5 ms dwell time per pixel",
  "ada:stepSizePixelSizeDefault": "2.5 \u00b5m",
  "ada:monitoredElements": [
    "O, Si, Mg, Fe, Al, P, Cr, Ca, Na, S, Ni \u2014 the SEM-EDS maps give 'a map on a pixel-by-pixel basis of the main elements (O, Si, Mg, Fe, Al, P, Cr, Ca, Na, S, Ni)', and the Cameo+ energy threshold covers 'Si, Mg, Fe, Al, P, Cr, Ca, Na, S, Ni, Ti'. The 'Si, Fe, Ca, Al, and S' list belongs to the EMPA-WDS mapping, a different procedure"
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "CNR IMAA (Institute of Methodologies for Environmental Analysis), Italian National Research Council, Potenza, Italy"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "BSE Imaging (Zeiss Supra 40 FE-SEM); SE Imaging (Zeiss Supra 40 FE-SEM); EMPA-WDS (JEOL JXA-8230, separate instrument); VIS-IR spectroscopy (SPIM)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Whole sample (polished slab) > Phase \u2014 elemental mapping of the \"NWA 7317 slab\", a \"small fragment of about 10 \u00d7 6 mm\" embedded in epoxy and polished (pp.3\u20134), acquired on \"almost the same portion of the VIS-IR SPIM images\" (p.4) so the two datasets can be compared pixel for pixel",
  "bios:computationalTool": [
    {
      "ada:toolRole": "acquisition",
      "schema:name": "Oxford INCA Energy"
    },
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Oxford INCA Energy (semi-quantitative phase determination from atomic proportions)"
    }
  ],
  "ada:analyticalMode": [
    "EDS Mapping"
  ],
  "ada:reportedProperties": [
    "element maps (pixel by pixel); Cameo+ energy-colour map (nominal); mineral phase map (nominal) \u2014 INCA gives 'a map on a pixel-by-pixel basis of the main elements (O, Si, Mg, Fe, Al, P, Cr, Ca, Na, S, Ni) so to derive the distribution of each mineral phase'; the SEM-EDS area is '10.5 \u00d7 4.0 mm wide'. The 'Si, Fe, Ca, Al, and S' maps at 3 \u03bcm resolution are the EMPA-WDS mapping's, a different procedure"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Embedded in epoxy, polished to \u00bc \u00b5m level, sputtered with 30-nm-thick carbon film",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
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
          "bios:LabProcess"
        ],
        "schema:position": 2,
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
      "schema:name": "semComposition",
      "schema:termCode": "semComposition"
    }
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:wdsDeadTimeCorrection": "missing",
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

<ex:semCompositionTAPP-Pascucci2026-2> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Embedded in epoxy, polished to ¼ µm level, sputtered with 30-nm-thick carbon film" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:detectionLimitMethod "missing" ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/chamberPressureDefault>,
        <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/edsSpectralProcessingType> ;
    schema1:datePublished "missing" ;
    schema1:description "EDS mapping: 20 kV, 60 µm aperture, 5 ms dwell per pixel, 1024×768 pixels, 2.5 µm pixel size, ~10 h total; element maps co-registered with BSE images Reported detail: ada:edsAcquisitionMode = Element mapping." ;
    schema1:instrument <ex:instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "CNR IMAA (Institute of Methodologies for Environmental Analysis), Italian National Research Council, Potenza, Italy" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semComposition" ;
            schema1:termCode "semComposition" ] ;
    schema1:name "semComposition protocol — Pascucci2026-2" ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "BSE Imaging (Zeiss Supra 40 FE-SEM); SE Imaging (Zeiss Supra 40 FE-SEM); EMPA-WDS (JEOL JXA-8230, separate instrument); VIS-IR spectroscopy (SPIM)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analyticalMode "EDS Mapping" ;
    ada:edsAcquisitionMode "Map" ;
    ada:edsLiveTimePerPointOrPixelDefault "5 ms dwell time per pixel" ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:monitoredElements "O, Si, Mg, Fe, Al, P, Cr, Ca, Na, S, Ni — the SEM-EDS maps give 'a map on a pixel-by-pixel basis of the main elements (O, Si, Mg, Fe, Al, P, Cr, Ca, Na, S, Ni)', and the Cameo+ energy threshold covers 'Si, Mg, Fe, Al, P, Cr, Ca, Na, S, Ni, Ti'. The 'Si, Fe, Ca, Al, and S' list belongs to the EMPA-WDS mapping, a different procedure" ;
    ada:reportedProperties "element maps (pixel by pixel); Cameo+ energy-colour map (nominal); mineral phase map (nominal) — INCA gives 'a map on a pixel-by-pixel basis of the main elements (O, Si, Mg, Fe, Al, P, Cr, Ca, Na, S, Ni) so to derive the distribution of each mineral phase'; the SEM-EDS area is '10.5 × 4.0 mm wide'. The 'Si, Fe, Ca, Al, and S' maps at 3 μm resolution are the EMPA-WDS mapping's, a different procedure" ;
    ada:samplingUnitSelectionCriteriaDefault "Spatial co-registration with the spectral imagery — the SEM work targets \"almost the same portion of the VIS-IR SPIM images\" (p.4), so that the two datasets can be compared on the same area of the slab" ;
    ada:samplingUnitType "Whole sample (polished slab) > Phase — elemental mapping of the \"NWA 7317 slab\", a \"small fragment of about 10 × 6 mm\" embedded in epoxy and polished (pp.3–4), acquired on \"almost the same portion of the VIS-IR SPIM images\" (p.4) so the two datasets can be compared pixel for pixel" ;
    ada:stepSizePixelSizeDefault "2.5 µm" ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "carbonaceous chondrite" ;
            ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/backgroundCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/peakCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/primaryCalibrationStandardName> ] ;
    ada:targetSpeciesTemplate [ ada:defaultTargetSpecies "Al",
                "Ca",
                "Cr",
                "Fe",
                "Mg",
                "Na",
                "Ni",
                "O",
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
                <https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/analyticalAccuracy>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/analyticalPrecision>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/beamCurrent>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/blankCorrection>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/interferenceCorrectionStandard>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/interferingElements>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/targetSpeciesEstimationMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/timeDependentIntensityCorrection>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/wdsSpectrometerChannel>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/xRayBackgroundCorrectionMethod>,
                <https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/xRayLineOverlapCorrectionsApplied> ] ;
    ada:wdsDeadTimeCorrection "missing" ;
    bios:computationalTool [ schema1:name "Oxford INCA Energy (semi-quantitative phase determination from atomic proportions)" ;
            ada:toolRole "dataReduction" ],
        [ schema1:name "Oxford INCA Energy" ;
            ada:toolRole "acquisition" ] .

<ex:instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:description "ESEM" ;
    schema1:hasPart <ex:instrument/SEM/part/EDS-Detector>,
        <ex:instrument/SEM/part/Electron-Source>,
        <ex:instrument/SEM/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Zeiss" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Supra 40" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "20 kV" ;
    ada:beamDiameterDefault -9999 ;
    ada:beamMode "missing" ;
    ada:mappingBeamCurrentDefault -9999 ;
    ada:mappingBeamDiameterDefault "N — a 60 μm aperture is stated (p.3), not a beam diameter" ;
    ada:mappingBeamMode "missing" ;
    ada:workingDistanceDefault -9999 .

<ex:instrument/SEM/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:description "Oxford INCA Energy 350; X-ACT LN2-free Silicon Drift Detector (SDD)" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Field emission gun (FEG) — subtype not specified" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/semCompositionTAPP/chamberPressureDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "High vacuum" ;
    schema1:name "Chamber Pressure" ;
    schema1:valueName "chamberPressureDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/backgroundCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Background Counting Time" ;
    schema1:valueName "backgroundCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/peakCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Peak Counting Time" ;
    schema1:valueName "peakCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/analyticalAccuracy> a schema1:PropertyValueSpecification ;
    schema1:name "Analytical Accuracy" ;
    schema1:valueName "analyticalAccuracy" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/analyticalPrecision> a schema1:PropertyValueSpecification ;
    schema1:name "Analytical Precision" ;
    schema1:valueName "analyticalPrecision" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/beamCurrent> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Beam Current" ;
    schema1:valueName "beamCurrent" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/blankCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Blank Correction" ;
    schema1:valueName "blankCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/interferenceCorrectionStandard> a schema1:PropertyValueSpecification ;
    schema1:name "Interference Correction Standard" ;
    schema1:valueName "interferenceCorrectionStandard" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/interferingElements> a schema1:PropertyValueSpecification ;
    schema1:name "Interfering Elements" ;
    schema1:valueName "interferingElements" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/targetSpeciesEstimationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Target Species Estimation Method" ;
    schema1:valueName "targetSpeciesEstimationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/timeDependentIntensityCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Time-Dependent Intensity Correction" ;
    schema1:valueName "timeDependentIntensityCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/wdsSpectrometerChannel> a schema1:PropertyValueSpecification ;
    schema1:name "WDS Spectrometer Channel" ;
    schema1:valueName "wdsSpectrometerChannel" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/xRayBackgroundCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "X-ray Background Correction Method" ;
    schema1:valueName "xRayBackgroundCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/targetSpeciesColumn/semCompositionTAPP/xRayLineOverlapCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "X-ray Line Overlap Corrections Applied" ;
    schema1:valueName "xRayLineOverlapCorrectionsApplied" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/semCompositionTAPP/edsSpectralProcessingType> a schema1:PropertyValue ;
    schema1:name "EDS Spectral Processing Type" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/edsSpectralProcessingType> ;
    schema1:value "Semi-quantitative analysis with virtual standards (Oxford INCA Energy); mineral phase determination from atomic % of constituent elements" .


```


### semCompositionTAPP example Zega2025
semCompositionTAPP instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | EDS Point Analysis (JEOL 7600F, NASA JSC, 15 kV).
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
  "@id": "ex:semCompositionTAPP-Zega2025",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semComposition protocol — Zega2025",
  "schema:description": "semCompositionTAPP instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | EDS Point Analysis (JEOL 7600F, NASA JSC, 15 kV) (publication column of SEM_Composition_TAPP_v83.csv). Reported detail: ada:edsAcquisitionMode = Point spectra (spot analysis).",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "Bennu particles"
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
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "N — the passage says regions of interest were characterized (\"Characterization of regions of interest was performed at an accelerating voltage of 15 kV\", p.9) but gives no rule for choosing them",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "7600F",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Field emission gun (FEG) — subtype not specified",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/SEM/part/Electron-Source",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Oxford Instruments Ultim Max SDD, 170 mm²",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/SEM/part/EDS-Detector",
          "schema:name": "missing"
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
          "@id": "ex:instrument/SEM/part/WDS-Spectrometer"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName",
      "ada:beamDiameterDefault": -9999,
      "ada:beamMode": "missing",
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:mappingBeamDiameterDefault": -9999,
      "ada:mappingBeamMode": "missing",
      "ada:workingDistanceDefault": -9999,
      "schema:description": "missing"
    }
  ],
  "ada:edsAcquisitionMode": "Point",
  "ada:edsLiveTimePerPointOrPixelDefault": "20 to 200 s (per point)",
  "ada:monitoredElements": [
    "N — \"EDS spectra were acquired at 15 kV with acquisition times ranging from 20 to 200 s with an incident beam current of ~900 pA\" on the JEOL 7600F (p.9); no element set is stated"
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "NASA Johnson Space Center (JSC), Houston, TX, USA"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "BSE Imaging (JEOL 7600F, JSC); SE Imaging (JEOL 7600F, JSC); FIB-SEM TEM prep (Quanta3D600, JSC)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Region of interest > Analysis point — \"The Oxford AZtec 'Point & ID' programme was used for the acquisition of images and point spectra\" (p.9)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "acquisition",
      "schema:name": "Oxford AZtec (Point & ID programme)"
    },
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Oxford AZtec"
    }
  ],
  "ada:analyticalMode": [
    "EDS Point Analysis"
  ],
  "ada:reportedProperties": [
    "phase composition (At%); phase identification (nominal) — Phase compositions from point spectra, reported with the EMPA data as atomic proportions (At%: Fe + Co, S, Ni for the sulfides, Fig. 1, p.2); phase identification is the nominal output"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Attached to Al cylinder SEM mount with double-sided C tape; sputter coated with ~5 nm carbon",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
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
          "bios:LabProcess"
        ],
        "schema:position": 2,
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
      "schema:name": "semComposition",
      "schema:termCode": "semComposition"
    }
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semCompositionTAPP-Zega2025",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semComposition protocol \u2014 Zega2025",
  "schema:description": "semCompositionTAPP instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | EDS Point Analysis (JEOL 7600F, NASA JSC, 15 kV) (publication column of SEM_Composition_TAPP_v83.csv). Reported detail: ada:edsAcquisitionMode = Point spectra (spot analysis).",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "Bennu particles"
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
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "N \u2014 the passage says regions of interest were characterized (\"Characterization of regions of interest was performed at an accelerating voltage of 15 kV\", p.9) but gives no rule for choosing them",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "JEOL",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "7600F",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Electron Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Field emission gun (FEG) \u2014 subtype not specified",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/SEM/part/Electron-Source",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Oxford Instruments Ultim Max SDD, 170 mm\u00b2",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/SEM/part/EDS-Detector",
          "schema:name": "missing"
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
          "@id": "ex:instrument/SEM/part/WDS-Spectrometer"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName",
      "ada:beamDiameterDefault": -9999,
      "ada:beamMode": "missing",
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:mappingBeamDiameterDefault": -9999,
      "ada:mappingBeamMode": "missing",
      "ada:workingDistanceDefault": -9999,
      "schema:description": "missing"
    }
  ],
  "ada:edsAcquisitionMode": "Point",
  "ada:edsLiveTimePerPointOrPixelDefault": "20 to 200 s (per point)",
  "ada:monitoredElements": [
    "N \u2014 \"EDS spectra were acquired at 15 kV with acquisition times ranging from 20 to 200 s with an incident beam current of ~900 pA\" on the JEOL 7600F (p.9); no element set is stated"
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "NASA Johnson Space Center (JSC), Houston, TX, USA"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "BSE Imaging (JEOL 7600F, JSC); SE Imaging (JEOL 7600F, JSC); FIB-SEM TEM prep (Quanta3D600, JSC)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Region of interest > Analysis point \u2014 \"The Oxford AZtec 'Point & ID' programme was used for the acquisition of images and point spectra\" (p.9)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "acquisition",
      "schema:name": "Oxford AZtec (Point & ID programme)"
    },
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Oxford AZtec"
    }
  ],
  "ada:analyticalMode": [
    "EDS Point Analysis"
  ],
  "ada:reportedProperties": [
    "phase composition (At%); phase identification (nominal) \u2014 Phase compositions from point spectra, reported with the EMPA data as atomic proportions (At%: Fe + Co, S, Ni for the sulfides, Fig. 1, p.2); phase identification is the nominal output"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Attached to Al cylinder SEM mount with double-sided C tape; sputter coated with ~5 nm carbon",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
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
          "bios:LabProcess"
        ],
        "schema:position": 2,
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
      "schema:name": "semComposition",
      "schema:termCode": "semComposition"
    }
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
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

<ex:semCompositionTAPP-Zega2025> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:detectionLimitMethod "missing" ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Attached to Al cylinder SEM mount with double-sided C tape; sputter coated with ~5 nm carbon" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "semCompositionTAPP instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | EDS Point Analysis (JEOL 7600F, NASA JSC, 15 kV) (publication column of SEM_Composition_TAPP_v83.csv). Reported detail: ada:edsAcquisitionMode = Point spectra (spot analysis)." ;
    schema1:instrument <ex:instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "NASA Johnson Space Center (JSC), Houston, TX, USA" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semComposition" ;
            schema1:termCode "semComposition" ] ;
    schema1:name "semComposition protocol — Zega2025" ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "BSE Imaging (JEOL 7600F, JSC); SE Imaging (JEOL 7600F, JSC); FIB-SEM TEM prep (Quanta3D600, JSC)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analyticalMode "EDS Point Analysis" ;
    ada:edsAcquisitionMode "Point" ;
    ada:edsLiveTimePerPointOrPixelDefault "20 to 200 s (per point)" ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:monitoredElements "N — \"EDS spectra were acquired at 15 kV with acquisition times ranging from 20 to 200 s with an incident beam current of ~900 pA\" on the JEOL 7600F (p.9); no element set is stated" ;
    ada:reportedProperties "phase composition (At%); phase identification (nominal) — Phase compositions from point spectra, reported with the EMPA data as atomic proportions (At%: Fe + Co, S, Ni for the sulfides, Fig. 1, p.2); phase identification is the nominal output" ;
    ada:samplingUnitSelectionCriteriaDefault "N — the passage says regions of interest were characterized (\"Characterization of regions of interest was performed at an accelerating voltage of 15 kV\", p.9) but gives no rule for choosing them" ;
    ada:samplingUnitType "Region of interest > Analysis point — \"The Oxford AZtec 'Point & ID' programme was used for the acquisition of images and point spectra\" (p.9)" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "Bennu particles" ;
            ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/backgroundCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/peakCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/primaryCalibrationStandardName> ] ;
    ada:wdsDeadTimeCorrection "missing" ;
    bios:computationalTool [ schema1:name "Oxford AZtec" ;
            ada:toolRole "dataReduction" ],
        [ schema1:name "Oxford AZtec (Point & ID programme)" ;
            ada:toolRole "acquisition" ] .

<ex:instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:description "missing" ;
    schema1:hasPart <ex:instrument/SEM/part/EDS-Detector>,
        <ex:instrument/SEM/part/Electron-Source>,
        <ex:instrument/SEM/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "JEOL" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "7600F" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "15 kV" ;
    ada:beamDiameterDefault -9999 ;
    ada:beamMode "missing" ;
    ada:mappingBeamCurrentDefault -9999 ;
    ada:mappingBeamDiameterDefault -9999 ;
    ada:mappingBeamMode "missing" ;
    ada:workingDistanceDefault -9999 .

<ex:instrument/SEM/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:description "Oxford Instruments Ultim Max SDD, 170 mm²" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Field emission gun (FEG) — subtype not specified" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/backgroundCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Background Counting Time" ;
    schema1:valueName "backgroundCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/peakCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Peak Counting Time" ;
    schema1:valueName "peakCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .


```


### semCompositionTAPP example Zega2025-2
semCompositionTAPP instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | EDS Mapping (Hitachi S-4800, U Arizona).
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
  "@id": "ex:semCompositionTAPP-Zega2025-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semComposition protocol — Zega2025-2",
  "schema:description": "Compositional heterogeneity assessed through EDS mapping; no specific kV, current, dwell time stated for S-4800 EDS Reported detail: ada:edsAcquisitionMode = EDS mapping.",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "Bennu particles"
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
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "Coverage of heterogeneity — \"The compositional heterogeneity of the particles was assessed through EDS mapping\" (p.9); no finer rule is given for placing the maps",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "Hitachi",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "S-4800",
        "@type": [
          "schema:ProductModel"
        ]
      },
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
          "@id": "ex:instrument/SEM/part/Electron-Source",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Oxford Instruments Aztec Live/x-stream/Ultimax 170 SDD",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/SEM/part/EDS-Detector",
          "schema:name": "missing"
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
          "@id": "ex:instrument/SEM/part/WDS-Spectrometer"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName",
      "ada:acceleratingVoltageDefault": -9999,
      "ada:beamDiameterDefault": -9999,
      "ada:beamMode": "missing",
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:mappingBeamDiameterDefault": -9999,
      "ada:mappingBeamMode": "missing",
      "ada:workingDistanceDefault": -9999,
      "schema:description": "missing"
    }
  ],
  "ada:edsAcquisitionMode": "Map",
  "ada:monitoredElements": [
    "N — \"The compositional heterogeneity of the particles was assessed through EDS mapping\" on the Hitachi S-4800 (p.9); no element set is stated"
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "K-ALFAA (Kuiper-Arizona Laboratory for Astromaterials Analysis), University of Arizona"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SE/BSE Imaging (Hitachi S-4800, U Arizona); FIB-SEM TEM prep (Helios G3, U Arizona); EMPA (Cameca SX-100 Ultra, out of scope)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Whole sample (particle) > Phase — \"The compositional heterogeneity of the particles was assessed through EDS mapping\" (p.9)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "acquisition",
      "schema:name": "Oxford Instruments Aztec Live/x-stream"
    },
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Oxford Instruments Aztec"
    }
  ],
  "ada:analyticalMode": [
    "EDS Mapping"
  ],
  "ada:reportedProperties": [
    "element maps; phase identification (nominal) — Elemental maps used to assess \"The compositional heterogeneity of the particles\" (p.9); the phases resolved from them are the nominal output"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished sections; coated with 0.1 nm carbon for charge mitigation",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
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
          "bios:LabProcess"
        ],
        "schema:position": 2,
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
      "schema:name": "semComposition",
      "schema:termCode": "semComposition"
    }
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semCompositionTAPP-Zega2025-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semComposition protocol \u2014 Zega2025-2",
  "schema:description": "Compositional heterogeneity assessed through EDS mapping; no specific kV, current, dwell time stated for S-4800 EDS Reported detail: ada:edsAcquisitionMode = EDS mapping.",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "Bennu particles"
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
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "Coverage of heterogeneity \u2014 \"The compositional heterogeneity of the particles was assessed through EDS mapping\" (p.9); no finer rule is given for placing the maps",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "Hitachi",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "S-4800",
        "@type": [
          "schema:ProductModel"
        ]
      },
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
          "@id": "ex:instrument/SEM/part/Electron-Source",
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "EDS Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Oxford Instruments Aztec Live/x-stream/Ultimax 170 SDD",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/SEM/part/EDS-Detector",
          "schema:name": "missing"
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
          "@id": "ex:instrument/SEM/part/WDS-Spectrometer"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName",
      "ada:acceleratingVoltageDefault": -9999,
      "ada:beamDiameterDefault": -9999,
      "ada:beamMode": "missing",
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:mappingBeamDiameterDefault": -9999,
      "ada:mappingBeamMode": "missing",
      "ada:workingDistanceDefault": -9999,
      "schema:description": "missing"
    }
  ],
  "ada:edsAcquisitionMode": "Map",
  "ada:monitoredElements": [
    "N \u2014 \"The compositional heterogeneity of the particles was assessed through EDS mapping\" on the Hitachi S-4800 (p.9); no element set is stated"
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "K-ALFAA (Kuiper-Arizona Laboratory for Astromaterials Analysis), University of Arizona"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SE/BSE Imaging (Hitachi S-4800, U Arizona); FIB-SEM TEM prep (Helios G3, U Arizona); EMPA (Cameca SX-100 Ultra, out of scope)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Whole sample (particle) > Phase \u2014 \"The compositional heterogeneity of the particles was assessed through EDS mapping\" (p.9)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "acquisition",
      "schema:name": "Oxford Instruments Aztec Live/x-stream"
    },
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Oxford Instruments Aztec"
    }
  ],
  "ada:analyticalMode": [
    "EDS Mapping"
  ],
  "ada:reportedProperties": [
    "element maps; phase identification (nominal) \u2014 Elemental maps used to assess \"The compositional heterogeneity of the particles\" (p.9); the phases resolved from them are the nominal output"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished sections; coated with 0.1 nm carbon for charge mitigation",
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
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
          "bios:LabProcess"
        ],
        "schema:position": 2,
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
      "schema:name": "semComposition",
      "schema:termCode": "semComposition"
    }
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
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

<ex:semCompositionTAPP-Zega2025-2> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:detectionLimitMethod "missing" ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Polished sections; coated with 0.1 nm carbon for charge mitigation" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "Compositional heterogeneity assessed through EDS mapping; no specific kV, current, dwell time stated for S-4800 EDS Reported detail: ada:edsAcquisitionMode = EDS mapping." ;
    schema1:instrument <ex:instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "K-ALFAA (Kuiper-Arizona Laboratory for Astromaterials Analysis), University of Arizona" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semComposition" ;
            schema1:termCode "semComposition" ] ;
    schema1:name "semComposition protocol — Zega2025-2" ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SE/BSE Imaging (Hitachi S-4800, U Arizona); FIB-SEM TEM prep (Helios G3, U Arizona); EMPA (Cameca SX-100 Ultra, out of scope)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analyticalMode "EDS Mapping" ;
    ada:edsAcquisitionMode "Map" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:monitoredElements "N — \"The compositional heterogeneity of the particles was assessed through EDS mapping\" on the Hitachi S-4800 (p.9); no element set is stated" ;
    ada:reportedProperties "element maps; phase identification (nominal) — Elemental maps used to assess \"The compositional heterogeneity of the particles\" (p.9); the phases resolved from them are the nominal output" ;
    ada:samplingUnitSelectionCriteriaDefault "Coverage of heterogeneity — \"The compositional heterogeneity of the particles was assessed through EDS mapping\" (p.9); no finer rule is given for placing the maps" ;
    ada:samplingUnitType "Whole sample (particle) > Phase — \"The compositional heterogeneity of the particles was assessed through EDS mapping\" (p.9)" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "Bennu particles" ;
            ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/backgroundCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/peakCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/primaryCalibrationStandardName> ] ;
    ada:wdsDeadTimeCorrection "missing" ;
    bios:computationalTool [ schema1:name "Oxford Instruments Aztec Live/x-stream" ;
            ada:toolRole "acquisition" ],
        [ schema1:name "Oxford Instruments Aztec" ;
            ada:toolRole "dataReduction" ] .

<ex:instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:description "missing" ;
    schema1:hasPart <ex:instrument/SEM/part/EDS-Detector>,
        <ex:instrument/SEM/part/Electron-Source>,
        <ex:instrument/SEM/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Hitachi" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "S-4800" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault -9999 ;
    ada:beamDiameterDefault -9999 ;
    ada:beamMode "missing" ;
    ada:mappingBeamCurrentDefault -9999 ;
    ada:mappingBeamDiameterDefault -9999 ;
    ada:mappingBeamMode "missing" ;
    ada:workingDistanceDefault -9999 .

<ex:instrument/SEM/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:description "Oxford Instruments Aztec Live/x-stream/Ultimax 170 SDD" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Unknown" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/backgroundCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Background Counting Time" ;
    schema1:valueName "backgroundCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/peakCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Peak Counting Time" ;
    schema1:valueName "peakCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .


```


### semCompositionTAPP example Barnes2025
semCompositionTAPP instance derived from Barnes et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | EDS Mapping (JEOL 7600F, NASA JSC, 15 kV).
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
  "@id": "ex:semCompositionTAPP-Barnes2025",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semComposition protocol — Barnes2025",
  "schema:description": "SEM-EDS (referred to as SEM-EDX in Extended Data Fig. 8) used to confirm phase identifications of two O-rich presolar grains identified by NanoSIMS isotope mapping: one grain confirmed as ferromagnesian silicate; one confirmed as Al,Mg-bearing oxide (Barnes et al. 2025, p.2 and Extended Data Fig. 8 caption). No instrument name, accelerating voltage, beam current, or sample preparation specifics stated for the JSC SEM-EDS step in this paper.",
  "ada:targetMaterialTemplate": {
    "ada:targetMaterialDeclaration": "O-rich presolar grains — Asteroid (101955) Bennu aggregate QL particles; O-rich presolar silicate and oxide grains; sample OREX-501018-100",
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
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "Isotopic anomaly, found by prior NanoSIMS imaging — grains \"were considered presolar if their isotopic composition differed from the reference ratios by >5σ and if the isotopic anomaly was present in multiple consecutive frames\", and of those \"Two O-rich presolar grains were also analysed by SEM-EDS to further constrain the phase\" (p.11)",
  "ada:monitoredElements": [
    "N — no element set is named for the JSC SEM-EDS of the two presolar grains (p.2, p.11, Extended Data Fig. 8). The 'multi-element EDS mapping (Mg, Si, Fe, Ni, S, Na, Ca and Al) of the different grains' (p.11) is the CRPG JEOL JSM-6510 work on other samples"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "SEM-EDS (Scanning Electron Microscopy–Energy Dispersive X-ray Spectroscopy)"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Astromaterials Research and Exploration Science Division (ARES), NASA Johnson Space Center, Houston, TX, USA"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "NanoSIMS isotope mapping (CAMECA NanoSIMS 50L, NASA JSC); presolar grains identified by NanoSIMS then confirmed by SEM-EDS phase characterisation"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Grain (presolar grain) > Phase — EDS was used on grains first found by NanoSIMS raster imaging of \"aggregate QL material pressed onto a gold (Au) foil mount\": \"Two O-rich presolar grains were also analysed by SEM-EDS to further constrain the phase and to confirm the phase identifications\" (pp.10–11)",
  "ada:analyticalMode": [
    "EDS Mapping"
  ],
  "ada:reportedProperties": [
    "elemental composition of the presolar grains; phase assignment (nominal: silicate vs oxide) — Elemental composition of the two presolar grains, used \"to further constrain the phase and to confirm the phase identifications made based on the NanoSIMS data\" (p.11); the reported output is the phase assignment (nominal: silicate vs oxide)"
  ],
  "schema:actionProcess": {
    "@type": [
      "schema:HowTo"
    ],
    "schema:step": [
      {
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
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
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2,
        "ada:detectionLimitMethod": "missing"
      }
    ]
  },
  "schema:instrument": [
    {
      "@id": "ex:instrument/SEM",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:name": "missing",
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
          "@id": "ex:instrument/SEM/part/EDS-Detector"
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
          "@id": "ex:instrument/SEM/part/Electron-Source",
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
          "@id": "ex:instrument/SEM/part/WDS-Spectrometer"
        }
      ],
      "ada:acceleratingVoltageDefault": -9999,
      "ada:beamDiameterDefault": -9999,
      "ada:beamMode": "missing",
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:mappingBeamDiameterDefault": -9999,
      "ada:mappingBeamMode": "missing",
      "ada:workingDistanceDefault": -9999,
      "schema:description": "missing",
      "schema:manufacturer": {
        "schema:name": "missing",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "missing",
        "@type": [
          "schema:ProductModel"
        ]
      }
    }
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:edsAcquisitionMode": "missing",
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semCompositionTAPP-Barnes2025",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semComposition protocol \u2014 Barnes2025",
  "schema:description": "SEM-EDS (referred to as SEM-EDX in Extended Data Fig. 8) used to confirm phase identifications of two O-rich presolar grains identified by NanoSIMS isotope mapping: one grain confirmed as ferromagnesian silicate; one confirmed as Al,Mg-bearing oxide (Barnes et al. 2025, p.2 and Extended Data Fig. 8 caption). No instrument name, accelerating voltage, beam current, or sample preparation specifics stated for the JSC SEM-EDS step in this paper.",
  "ada:targetMaterialTemplate": {
    "ada:targetMaterialDeclaration": "O-rich presolar grains \u2014 Asteroid (101955) Bennu aggregate QL particles; O-rich presolar silicate and oxide grains; sample OREX-501018-100",
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
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:targetMaterialColumn/semCompositionTAPP/primaryCalibrationStandardName",
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
  "ada:samplingUnitSelectionCriteriaDefault": "Isotopic anomaly, found by prior NanoSIMS imaging \u2014 grains \"were considered presolar if their isotopic composition differed from the reference ratios by >5\u03c3 and if the isotopic anomaly was present in multiple consecutive frames\", and of those \"Two O-rich presolar grains were also analysed by SEM-EDS to further constrain the phase\" (p.11)",
  "ada:monitoredElements": [
    "N \u2014 no element set is named for the JSC SEM-EDS of the two presolar grains (p.2, p.11, Extended Data Fig. 8). The 'multi-element EDS mapping (Mg, Si, Fe, Ni, S, Na, Ca and Al) of the different grains' (p.11) is the CRPG JEOL JSM-6510 work on other samples"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "SEM-EDS (Scanning Electron Microscopy\u2013Energy Dispersive X-ray Spectroscopy)"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Astromaterials Research and Exploration Science Division (ARES), NASA Johnson Space Center, Houston, TX, USA"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "NanoSIMS isotope mapping (CAMECA NanoSIMS 50L, NASA JSC); presolar grains identified by NanoSIMS then confirmed by SEM-EDS phase characterisation"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Grain (presolar grain) > Phase \u2014 EDS was used on grains first found by NanoSIMS raster imaging of \"aggregate QL material pressed onto a gold (Au) foil mount\": \"Two O-rich presolar grains were also analysed by SEM-EDS to further constrain the phase and to confirm the phase identifications\" (pp.10\u201311)",
  "ada:analyticalMode": [
    "EDS Mapping"
  ],
  "ada:reportedProperties": [
    "elemental composition of the presolar grains; phase assignment (nominal: silicate vs oxide) \u2014 Elemental composition of the two presolar grains, used \"to further constrain the phase and to confirm the phase identifications made based on the NanoSIMS data\" (p.11); the reported output is the phase assignment (nominal: silicate vs oxide)"
  ],
  "schema:actionProcess": {
    "@type": [
      "schema:HowTo"
    ],
    "schema:step": [
      {
        "@type": [
          "cdi:Activity",
          "schema:Action",
          "schema:HowToStep"
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
          "schema:Action",
          "schema:HowToStep"
        ],
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2,
        "ada:detectionLimitMethod": "missing"
      }
    ]
  },
  "schema:instrument": [
    {
      "@id": "ex:instrument/SEM",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:name": "missing",
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
          "@id": "ex:instrument/SEM/part/EDS-Detector"
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
          "@id": "ex:instrument/SEM/part/Electron-Source",
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
          "@id": "ex:instrument/SEM/part/WDS-Spectrometer"
        }
      ],
      "ada:acceleratingVoltageDefault": -9999,
      "ada:beamDiameterDefault": -9999,
      "ada:beamMode": "missing",
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:mappingBeamDiameterDefault": -9999,
      "ada:mappingBeamMode": "missing",
      "ada:workingDistanceDefault": -9999,
      "schema:description": "missing",
      "schema:manufacturer": {
        "schema:name": "missing",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "missing",
        "@type": [
          "schema:ProductModel"
        ]
      }
    }
  ],
  "schema:variableMeasured": [
    {
      "schema:name": "Calibration Factor and Determination Method",
      "schema:defaultValue": "missing"
    }
  ],
  "ada:edsAcquisitionMode": "missing",
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:wdsDeadTimeCorrection": "missing",
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

<ex:semCompositionTAPP-Barnes2025> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:detectionLimitMethod "missing" ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "missing" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "SEM-EDS (referred to as SEM-EDX in Extended Data Fig. 8) used to confirm phase identifications of two O-rich presolar grains identified by NanoSIMS isotope mapping: one grain confirmed as ferromagnesian silicate; one confirmed as Al,Mg-bearing oxide (Barnes et al. 2025, p.2 and Extended Data Fig. 8 caption). No instrument name, accelerating voltage, beam current, or sample preparation specifics stated for the JSC SEM-EDS step in this paper." ;
    schema1:instrument <ex:instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Astromaterials Research and Exploration Science Division (ARES), NASA Johnson Space Center, Houston, TX, USA" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "SEM-EDS (Scanning Electron Microscopy–Energy Dispersive X-ray Spectroscopy)" ] ;
    schema1:name "semComposition protocol — Barnes2025" ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "NanoSIMS isotope mapping (CAMECA NanoSIMS 50L, NASA JSC); presolar grains identified by NanoSIMS then confirmed by SEM-EDS phase characterisation" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    schema1:variableMeasured [ schema1:defaultValue "missing" ;
            schema1:name "Calibration Factor and Determination Method" ] ;
    ada:analyticalMode "EDS Mapping" ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:monitoredElements "N — no element set is named for the JSC SEM-EDS of the two presolar grains (p.2, p.11, Extended Data Fig. 8). The 'multi-element EDS mapping (Mg, Si, Fe, Ni, S, Na, Ca and Al) of the different grains' (p.11) is the CRPG JEOL JSM-6510 work on other samples" ;
    ada:reportedProperties "elemental composition of the presolar grains; phase assignment (nominal: silicate vs oxide) — Elemental composition of the two presolar grains, used \"to further constrain the phase and to confirm the phase identifications made based on the NanoSIMS data\" (p.11); the reported output is the phase assignment (nominal: silicate vs oxide)" ;
    ada:samplingUnitSelectionCriteriaDefault "Isotopic anomaly, found by prior NanoSIMS imaging — grains \"were considered presolar if their isotopic composition differed from the reference ratios by >5σ and if the isotopic anomaly was present in multiple consecutive frames\", and of those \"Two O-rich presolar grains were also analysed by SEM-EDS to further constrain the phase\" (p.11)" ;
    ada:samplingUnitType "Grain (presolar grain) > Phase — EDS was used on grains first found by NanoSIMS raster imaging of \"aggregate QL material pressed onto a gold (Au) foil mount\": \"Two O-rich presolar grains were also analysed by SEM-EDS to further constrain the phase and to confirm the phase identifications\" (pp.10–11)" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetMaterialTemplate [ ada:targetMaterialColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/backgroundCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/peakCountingTime>,
                <https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/primaryCalibrationStandardName> ;
            ada:targetMaterialDeclaration "O-rich presolar grains — Asteroid (101955) Bennu aggregate QL particles; O-rich presolar silicate and oxide grains; sample OREX-501018-100" ] ;
    ada:wdsDeadTimeCorrection "missing" .

<ex:instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:description "missing" ;
    schema1:hasPart <ex:instrument/SEM/part/EDS-Detector>,
        <ex:instrument/SEM/part/Electron-Source>,
        <ex:instrument/SEM/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "missing" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "missing" ] ;
    schema1:name "missing" ;
    ada:acceleratingVoltageDefault -9999 ;
    ada:beamDiameterDefault -9999 ;
    ada:beamMode "missing" ;
    ada:mappingBeamCurrentDefault -9999 ;
    ada:mappingBeamDiameterDefault -9999 ;
    ada:mappingBeamMode "missing" ;
    ada:workingDistanceDefault -9999 .

<ex:instrument/SEM/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "missing" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/backgroundCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Background Counting Time" ;
    schema1:valueName "backgroundCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/peakCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Peak Counting Time" ;
    schema1:valueName "peakCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/targetMaterialColumn/semCompositionTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: SEM Composition (EDS/WDS) Technique-Aligned Protocol Profile (semCompositionTAPP)
description: Scanning electron microscopy compositional microanalysis (EDS/WDS) extension
  of the base TAPP definition, generated from tapp/Current TAPPs/SEM_Composition_TAPP_v83.csv
  via the path-driven pipeline (bootstrap_schemapaths.py + build_pathdriven.py).
allOf:
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/calibrationFactor/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/targetSpecies/schema.yaml#/$defs/ProcedureIdentification
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
            - title: Peak Counting Time
              description: Time spent counting X-ray intensity at the peak position,
                in seconds. Adjustments stay within procedure-defined bounds.
              type: object
              properties:
                '@id':
                  const: ada:targetMaterialColumn/semCompositionTAPP/peakCountingTime
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
            - title: Background Counting Time
              description: Total time spent counting at off-peak background position(s)
                in seconds, summed across all background positions.
              type: object
              properties:
                '@id':
                  const: ada:targetMaterialColumn/semCompositionTAPP/backgroundCountingTime
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
                  const: ada:targetMaterialColumn/semCompositionTAPP/primaryCalibrationStandardName
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
              title: Peak Counting Time
              description: Time spent counting X-ray intensity at the peak position,
                in seconds. Adjustments stay within procedure-defined bounds.
              type: object
              properties:
                '@id':
                  const: ada:targetMaterialColumn/semCompositionTAPP/peakCountingTime
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
              title: Background Counting Time
              description: Total time spent counting at off-peak background position(s)
                in seconds, summed across all background positions.
              type: object
              properties:
                '@id':
                  const: ada:targetMaterialColumn/semCompositionTAPP/backgroundCountingTime
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
                  const: ada:targetMaterialColumn/semCompositionTAPP/primaryCalibrationStandardName
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
    schema:instrument:
      type: array
      items:
        type: object
        allOf:
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
                    - Zeiss
                    - FEI / Thermo Fisher Scientific
                    - Hitachi
                    - Tescan
                    - Phenom
                    - Unknown
                    - N/A
                    - None
                    - missing
                    readOnly: true
                required:
                - schema:name
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
              schema:hasPart:
                type: array
                items:
                  type: object
                  allOf:
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
              schema:description:
                description: "Broad platform type of the instrument. 'Standard SEM':
                  dedicated electron-only SEM column. 'FIB-SEM dual-beam': combined
                  focused ion beam and SEM columns (enables TEM specimen preparation,
                  3D serial sectioning, ion-beam milling). 'VP-SEM': variable-pressure
                  SEM, a dry gas at low chamber pressure for uncoated or charging
                  specimens. 'ESEM': environmental SEM, water vapour at higher pressure
                  for hydrated specimens, requiring a gaseous secondary electron detector.
                  Where an instrument combines categories, join them with '; ' \u2014
                  'FIB-SEM dual-beam; VP-SEM' \u2014 rather than looking for a combined
                  member. This field records the COLUMN AND CHAMBER configuration
                  only: field emission is a source type and belongs in Electron Source,
                  not here."
                anyOf:
                - type: string
                  enum:
                  - Standard SEM
                  - FIB-SEM dual-beam
                  - VP-SEM
                  - ESEM
                  - N/A
                  - None
                  - missing
                  readOnly: true
                - type: array
                  items:
                    type: string
                    enum:
                    - Standard SEM
                    - FIB-SEM dual-beam
                    - VP-SEM
                    - ESEM
                    - N/A
                    - None
                    - missing
                    readOnly: true
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
              ada:acceleratingVoltageDefault:
                description: Electron beam accelerating voltage in kilovolts.
                anyOf:
                - type: number
                - type: string
              ada:beamDiameterDefault:
                description: Nominal electron beam diameter (spot size) at the sample
                  surface for point analysis, in nanometres or micrometres, as set
                  by the condenser aperture and working distance. The beam used for
                  mapping is recorded under Mapping Beam Diameter.
                anyOf:
                - type: number
                - type: string
              ada:workingDistanceDefault:
                description: Distance between the objective lens pole piece and the
                  specimen surface in millimetres.
                anyOf:
                - type: number
                - type: string
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
            - ada:workingDistanceDefault
            - schema:description
            - schema:manufacturer
            - schema:model
      allOf:
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
        ada:targetSpeciesColumns:
          type: array
          items:
            anyOf:
            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/TargetSpeciesIdentifierColumn
            - title: Beam Current
              description: Electron beam probe current for point analysis. For sub-nA
                values use decimal notation (e.g., 0.4 nA). The current used while
                the beam scans an area, for a map or an image, is recorded under Mapping
                Beam Current.
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/semCompositionTAPP/beamCurrent
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
            - title: WDS Spectrometer Channel
              description: "WDS spectrometer position(s) assigned to each target species,
                one entry per assignment. An target species may be assigned to more
                than one spectrometer with intensities aggregated (aggregate intensity
                counting), and one spectrometer serves several target species across
                a run, so the assignment \u2014 not the target species \u2014 is the
                unit carrying the spectrometer setup."
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/semCompositionTAPP/wdsSpectrometerChannel
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: wdsSpectrometerChannel
                schema:name:
                  const: WDS Spectrometer Channel
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
            - title: X-ray Background Correction Method
              description: 'Method used to estimate and subtract background X-ray
                intensity beneath the peak. For WDS: typically 2-point off-peak linear
                interpolation or Mean Atomic Number (MAN) background model. For EDS:
                spectral background fitting or top-hat filter applied during spectral
                processing.'
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/semCompositionTAPP/xRayBackgroundCorrectionMethod
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
            - title: Time-Dependent Intensity Correction
              description: Type of time-dependent intensity (TDI) correction applied
                to compensate for beam-induced volatilisation or migration of sensitive
                elements (e.g., Na, K, F in glasses, feldspars, carbonates).
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/semCompositionTAPP/timeDependentIntensityCorrection
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
            - title: Target Species Estimation Method
              description: Whether elemental concentrations were calculated directly
                from measured X-ray intensities, or estimated by cation stoichiometry
                (e.g., oxygen calculated from cation proportions in silicates; carbon
                from stoichiometry in carbonates).
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/semCompositionTAPP/targetSpeciesEstimationMethod
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
            - title: Blank Correction
              description: Method and reference material(s) used to determine and
                subtract blank signal contributions (e.g., carbon coat contribution
                to C signal, or background contamination for trace elements).
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/semCompositionTAPP/blankCorrection
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
            - title: X-ray Line Overlap Corrections Applied
              description: Whether a spectral interference correction was applied.
                Common interferences include Ti Kb on V Ka, Cr Kb on Mn Ka, and Ba
                La on Ti Ka.
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/semCompositionTAPP/xRayLineOverlapCorrectionsApplied
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
                  const: ada:targetSpeciesColumn/semCompositionTAPP/interferingElements
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
            - title: Interference Correction Standard
              description: Reference material used to quantify and calibrate the interference
                correction.
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/semCompositionTAPP/interferenceCorrectionStandard
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
            - title: Analytical Precision
              description: Reproducibility of repeated measurements on the same or
                equivalent reference material, expressed as 1-sigma relative standard
                deviation (%). Include reference material name, number of analyses
                (n), and the measured value.
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/semCompositionTAPP/analyticalPrecision
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
            - title: Analytical Accuracy
              description: Offset between measured and accepted reference values for
                secondary standards, expressed as percent relative bias. Include reference
                material, reference value source, and the measured value.
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/semCompositionTAPP/analyticalAccuracy
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
                  const: ada:targetSpeciesColumn/semCompositionTAPP/countingStatisticsError
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
          allOf:
          - contains:
              title: Beam Current
              description: Electron beam probe current for point analysis. For sub-nA
                values use decimal notation (e.g., 0.4 nA). The current used while
                the beam scans an area, for a map or an image, is recorded under Mapping
                Beam Current.
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/semCompositionTAPP/beamCurrent
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
              title: WDS Spectrometer Channel
              description: "WDS spectrometer position(s) assigned to each target species,
                one entry per assignment. An target species may be assigned to more
                than one spectrometer with intensities aggregated (aggregate intensity
                counting), and one spectrometer serves several target species across
                a run, so the assignment \u2014 not the target species \u2014 is the
                unit carrying the spectrometer setup."
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/semCompositionTAPP/wdsSpectrometerChannel
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: wdsSpectrometerChannel
                schema:name:
                  const: WDS Spectrometer Channel
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
              title: X-ray Background Correction Method
              description: 'Method used to estimate and subtract background X-ray
                intensity beneath the peak. For WDS: typically 2-point off-peak linear
                interpolation or Mean Atomic Number (MAN) background model. For EDS:
                spectral background fitting or top-hat filter applied during spectral
                processing.'
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/semCompositionTAPP/xRayBackgroundCorrectionMethod
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
              title: Time-Dependent Intensity Correction
              description: Type of time-dependent intensity (TDI) correction applied
                to compensate for beam-induced volatilisation or migration of sensitive
                elements (e.g., Na, K, F in glasses, feldspars, carbonates).
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/semCompositionTAPP/timeDependentIntensityCorrection
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
          - contains:
              title: Target Species Estimation Method
              description: Whether elemental concentrations were calculated directly
                from measured X-ray intensities, or estimated by cation stoichiometry
                (e.g., oxygen calculated from cation proportions in silicates; carbon
                from stoichiometry in carbonates).
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/semCompositionTAPP/targetSpeciesEstimationMethod
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
              title: Blank Correction
              description: Method and reference material(s) used to determine and
                subtract blank signal contributions (e.g., carbon coat contribution
                to C signal, or background contamination for trace elements).
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/semCompositionTAPP/blankCorrection
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
              title: X-ray Line Overlap Corrections Applied
              description: Whether a spectral interference correction was applied.
                Common interferences include Ti Kb on V Ka, Cr Kb on Mn Ka, and Ba
                La on Ti Ka.
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/semCompositionTAPP/xRayLineOverlapCorrectionsApplied
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
                  const: ada:targetSpeciesColumn/semCompositionTAPP/interferingElements
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
              title: Interference Correction Standard
              description: Reference material used to quantify and calibrate the interference
                correction.
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/semCompositionTAPP/interferenceCorrectionStandard
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
              title: Analytical Precision
              description: Reproducibility of repeated measurements on the same or
                equivalent reference material, expressed as 1-sigma relative standard
                deviation (%). Include reference material name, number of analyses
                (n), and the measured value.
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/semCompositionTAPP/analyticalPrecision
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
              title: Analytical Accuracy
              description: Offset between measured and accepted reference values for
                secondary standards, expressed as percent relative bias. Include reference
                material, reference value source, and the measured value.
              type: object
              properties:
                '@id':
                  const: ada:targetSpeciesColumn/semCompositionTAPP/analyticalAccuracy
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
                  const: ada:targetSpeciesColumn/semCompositionTAPP/countingStatisticsError
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
        ada:defaultTargetSpecies:
          type: array
          items:
            anyOf:
            - type: string
            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/DefinedTerm
            - type: object
      required:
      - ada:defaultTargetSpecies
    schema:additionalProperty:
      type: array
      items:
        anyOf:
        - title: Beam Raster Dimensions
          description: "Dimensions of the small area over which the beam is rastered
            at a single analysis point, reported as width \xD7 height in \xB5m. Applicable
            when Beam Mode = Rastered; defines the effective spatial footprint of
            the measurement. Not applicable when mapping."
          type: object
          properties:
            '@id':
              const: ada:parameter/semCompositionTAPP/beamRasterDimensionsDefault
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
            schema:unitText:
              const: "\xB5m x \xB5m"
          required:
          - '@id'
          - '@type'
          - schema:valueName
          - schema:name
          - ada:dataType
          - ada:fieldScope
        - title: Beam Damage Minimization
          description: 'Describes any measures taken to reduce electron beam damage
            to the sample during analysis. Examples: reduced accelerating voltage,
            lowered beam current, defocused or rastered beam, cooled stage, short
            acquisition sequences, or rotating between multiple points.'
          type: object
          properties:
            '@id':
              const: ada:parameter/semCompositionTAPP/beamDamageMinimizationDefault
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
          required:
          - '@id'
          - '@type'
          - schema:valueName
          - schema:name
          - ada:dataType
          - ada:fieldScope
        - title: Drift Correction
          description: 'Describes whether and how stage or beam drift was monitored
            and corrected during the measurement session. Examples: periodic stage
            realignment to a fiducial marker, automated beam drift correction in acquisition
            software, or reanalysis of a reference point at regular intervals.'
          type: object
          properties:
            '@id':
              const: ada:parameter/semCompositionTAPP/driftCorrectionDefault
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
              const: ada:parameter/semCompositionTAPP/stageScanVsBeamScan
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/semCompositionTAPP/stageScanVsBeamScan
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
        - title: Chamber Pressure
          description: Chamber pressure and gas type during analysis. Required for
            variable pressure (VP-SEM) and environmental SEM (ESEM) modes. Report
            value and unit (Pa or Torr) and gas composition. Use 'None' for standard
            high-vacuum operation.
          type: object
          properties:
            '@id':
              const: ada:parameter/semCompositionTAPP/chamberPressureDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: chamberPressureDefault
            schema:name:
              const: Chamber Pressure
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
        - title: Halogen Correction on Oxygen
          description: Whether oxygen content was adjusted to account for halogen
            substitution (F and/or Cl replacing OH) in halogen-bearing phases such
            as apatite, amphibole, and mica, where oxygen is calculated by stoichiometry.
          type: object
          properties:
            '@id':
              const: ada:parameter/semCompositionTAPP/halogenCorrectionOnOxygenDefault
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
              const: ada:parameter/semCompositionTAPP/edsSpectralProcessingType
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/semCompositionTAPP/edsSpectralProcessingType
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
      allOf:
      - contains:
          title: Beam Raster Dimensions
          description: "Dimensions of the small area over which the beam is rastered
            at a single analysis point, reported as width \xD7 height in \xB5m. Applicable
            when Beam Mode = Rastered; defines the effective spatial footprint of
            the measurement. Not applicable when mapping."
          type: object
          properties:
            '@id':
              const: ada:parameter/semCompositionTAPP/beamRasterDimensionsDefault
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
          title: Beam Damage Minimization
          description: 'Describes any measures taken to reduce electron beam damage
            to the sample during analysis. Examples: reduced accelerating voltage,
            lowered beam current, defocused or rastered beam, cooled stage, short
            acquisition sequences, or rotating between multiple points.'
          type: object
          properties:
            '@id':
              const: ada:parameter/semCompositionTAPP/beamDamageMinimizationDefault
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
          description: 'Describes whether and how stage or beam drift was monitored
            and corrected during the measurement session. Examples: periodic stage
            realignment to a fiducial marker, automated beam drift correction in acquisition
            software, or reanalysis of a reference point at regular intervals.'
          type: object
          properties:
            '@id':
              const: ada:parameter/semCompositionTAPP/driftCorrectionDefault
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
              const: ada:parameter/semCompositionTAPP/stageScanVsBeamScan
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/semCompositionTAPP/stageScanVsBeamScan
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
      - contains:
          title: Chamber Pressure
          description: Chamber pressure and gas type during analysis. Required for
            variable pressure (VP-SEM) and environmental SEM (ESEM) modes. Report
            value and unit (Pa or Torr) and gas composition. Use 'None' for standard
            high-vacuum operation.
          type: object
          properties:
            '@id':
              const: ada:parameter/semCompositionTAPP/chamberPressureDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: chamberPressureDefault
            schema:name:
              const: Chamber Pressure
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
      - contains:
          title: Halogen Correction on Oxygen
          description: Whether oxygen content was adjusted to account for halogen
            substitution (F and/or Cl replacing OH) in halogen-bearing phases such
            as apatite, amphibole, and mica, where oxygen is calculated by stoichiometry.
          type: object
          properties:
            '@id':
              const: ada:parameter/semCompositionTAPP/halogenCorrectionOnOxygenDefault
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
              const: ada:parameter/semCompositionTAPP/edsSpectralProcessingType
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/semCompositionTAPP/edsSpectralProcessingType
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
    ada:monitoredPropertyTemplate:
      type: object
      properties:
        ada:monitoredPropertyColumns:
          type: array
          items:
            anyOf:
            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/MonitoredPropertyIdentifierColumn
            - title: Dwell Time per Pixel
              description: Time the electron beam dwells on each pixel during raster
                scanning (imaging modes) or on each step position during compositional
                mapping (EDS and WDS mapping modes), in microseconds or milliseconds.
                For WDS mapping, the dwell time is per spectrometer per pixel.
              type: object
              properties:
                '@id':
                  const: ada:monitoredPropertyColumn/semCompositionTAPP/dwellTimePerPixel
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
            - title: X-ray Line
              description: X-ray emission line measured.
              type: object
              properties:
                '@id':
                  const: ada:monitoredPropertyColumn/semCompositionTAPP/xRayLine
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
            - title: Diffracting Crystal
              description: Analyzing crystal (monochromator).
              type: object
              properties:
                '@id':
                  const: ada:monitoredPropertyColumn/semCompositionTAPP/diffractingCrystal
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
                  const: ada:monitoredPropertyColumn/semCompositionTAPP/sequence
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
            - title: Proportional Counter / Detector
              description: Type of detector used.
              type: object
              properties:
                '@id':
                  const: ada:monitoredPropertyColumn/semCompositionTAPP/proportionalCounterDetector
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
            - title: WDS PHA Setting
              description: Pulse height analyzer (PHA) setting for the WDS detector.
                Integral mode accepts all pulses above a threshold; Differential mode
                selects a narrow energy window to reject higher-order reflections
                and escape peaks.
              type: object
              properties:
                '@id':
                  const: ada:monitoredPropertyColumn/semCompositionTAPP/wdsPhaSetting
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
            - title: Background Position(s)
              description: Location(s) of off-peak background measurement(s) relative
                to the peak, in mm or sin-theta, and whether on the high- or low-energy
                side.
              type: object
              properties:
                '@id':
                  const: ada:monitoredPropertyColumn/semCompositionTAPP/backgroundPosition
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
                  const: ada:monitoredPropertyColumn/semCompositionTAPP/xRayDetectionMethodPerMonitoredElement
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
              title: Dwell Time per Pixel
              description: Time the electron beam dwells on each pixel during raster
                scanning (imaging modes) or on each step position during compositional
                mapping (EDS and WDS mapping modes), in microseconds or milliseconds.
                For WDS mapping, the dwell time is per spectrometer per pixel.
              type: object
              properties:
                '@id':
                  const: ada:monitoredPropertyColumn/semCompositionTAPP/dwellTimePerPixel
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
              title: X-ray Line
              description: X-ray emission line measured.
              type: object
              properties:
                '@id':
                  const: ada:monitoredPropertyColumn/semCompositionTAPP/xRayLine
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
              title: Diffracting Crystal
              description: Analyzing crystal (monochromator).
              type: object
              properties:
                '@id':
                  const: ada:monitoredPropertyColumn/semCompositionTAPP/diffractingCrystal
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
                  const: ada:monitoredPropertyColumn/semCompositionTAPP/sequence
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
              title: Proportional Counter / Detector
              description: Type of detector used.
              type: object
              properties:
                '@id':
                  const: ada:monitoredPropertyColumn/semCompositionTAPP/proportionalCounterDetector
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
              title: WDS PHA Setting
              description: Pulse height analyzer (PHA) setting for the WDS detector.
                Integral mode accepts all pulses above a threshold; Differential mode
                selects a narrow energy window to reject higher-order reflections
                and escape peaks.
              type: object
              properties:
                '@id':
                  const: ada:monitoredPropertyColumn/semCompositionTAPP/wdsPhaSetting
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
              title: Background Position(s)
              description: Location(s) of off-peak background measurement(s) relative
                to the peak, in mm or sin-theta, and whether on the high- or low-energy
                side.
              type: object
              properties:
                '@id':
                  const: ada:monitoredPropertyColumn/semCompositionTAPP/backgroundPosition
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
                  const: ada:monitoredPropertyColumn/semCompositionTAPP/xRayDetectionMethodPerMonitoredElement
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
      - Automated mineralogy
      - N/A
      - None
      - missing
      readOnly: true
    ada:edsLiveTimePerPointOrPixelDefault:
      description: EDS spectral acquisition live time per analysis point or per pixel
        in seconds.
      anyOf:
      - type: number
      - type: string
    ada:stepSizePixelSizeDefault:
      description: "Centre-to-centre distance between adjacent measurement points
        (WDS mapping) or pixels (EDS mapping) in \xB5m."
      anyOf:
      - type: number
      - type: string
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
        - XPP (Simplified PAP)
        - PAP (Pouchou & Pichoir Full)
        - ZAF
        - CITZAF (Armstrong 1995)
        - Phi-rho-z (EPQ-91)
        - Unknown
        - N/A
        - None
        - missing
      - type: string
      readOnly: true
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
                            const: ada:parameter/semCompositionTAPP/analysisInclusionAndRejectionCriteriaDefault
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
                            const: ada:parameter/semCompositionTAPP/analysisInclusionAndRejectionCriteriaDefault
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
  - ada:stepSizePixelSizeDefault
  - ada:matrixCorrectionMethod
  - ada:massAbsorptionCoefficients
  - ada:wdsDeadTimeCorrection

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/tapp/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/tapp/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/tapp/context.jsonld)

## Sources

* [SEM_Composition_TAPP_v4.xlsx (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/SEM-Composition/tapp`

