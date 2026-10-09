
# SEM Imaging Technique-Aligned Protocol Profile (semImagingTAPP) (Schema)

`ogch.techniqueProfile.geochemProfile.SEM-Imaging.tapp` *v0.1*

Scanning electron microscopy imaging (SE/BSE/CL/EBSD) extension of the base TAPP definition. Basic protocol-tier fields are required top-level ada: properties; Advanced protocol-tier fields are schema:additionalProperty[] entries. No ada:targetSpeciesTemplate (imaging has no per-element analyte axis). Generated from docs/SEM_Imaging_TAPP_v4.xlsx by tools/build_tapp.py.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### semImagingTAPP example Garvie2008
semImagingTAPP instance derived from Garvie et al. 2008 | Tagish Lake (C2) nanoglobules | SE Imaging (FEI Nova 200 NanoLab).
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
  "@id": "ex:semImagingTAPP-Garvie2008",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semImaging protocol — Garvie2008",
  "schema:description": "Sample imaged without coating; initial ~5% beam-induced shrinkage observed upon first e-beam exposure; sample stable thereafter; focusing performed away from particles of interest to minimise beam exposure",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "carbonaceous nanoglobules"
    ],
    "ada:targetMaterialColumns": [
      {
        "schema:valueName": "targetMaterial",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
        "schema:name": "example instrumentName"
      }
    ]
  },
  "ada:samplingUnitSelectionCriteriaDefault": "N — no rule is given for which globules were imaged; the stated criterion is at sample level, \"Several millimeter-sized pieces of the pristine Tagish Lake meteorite free of fusion crust were digested in HCl and HF in order to concentrate the carbonaceous materials\" (p.1)",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "FEI / Thermo Fisher Scientific",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Nova 200 NanoLab DualBeam",
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
            "SE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "In-lens / TLD (through-the-lens)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/SEM/part/SE-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "BSE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/BSE-Detector"
        }
      ],
      "schema:description": "FIB-SEM dual-beam",
      "ada:acceleratingVoltageDefault": "500 V; 1 kV; 5 kV",
      "ada:workingDistanceDefault": "0.5–5.4 mm",
      "ada:mappingBeamCurrentDefault": "70 fA (500 V); 1.4 pA (1 kV); 98 pA (5 kV)",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "School of Earth and Space Exploration / School of Materials, Arizona State University"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "FIB milling and TEM cross-section preparation (same instrument)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Grain (individual carbonaceous nanoglobule) — \"low voltage scanning electron microscopy (SEM) was used to characterize the globule forms and external structures\" (p.1) of globules on an Al-SEM stub (p.2)",
  "ada:analyticalMode": [
    "SE Imaging"
  ],
  "ada:reportedProperties": [
    "globule morphology (nominal); globule size (µm); surface structure (nominal) — Globule morphology, size and surface structure (nominal, with sizes in µm) — the imaging is used \"to characterize the globule forms and external structures\" (p.1)"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "HCl and HF acid dissolution residue from pristine Tagish Lake pieces; deposited on lacey C TEM grid attached to Al-SEM stub; uncoated",
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
        "ada:ebsdIndexingMethod": "missing"
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
      "schema:name": "semImaging",
      "schema:termCode": "semImaging"
    }
  ],
  "ada:clAcquisitionMode": "missing",
  "ada:clIntegrationTimeDefault": -9999,
  "ada:clWavelengthRange": -9999,
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:ebsdDetectorConfiguration": "missing",
  "ada:ebsdPhaseListDefault": "missing",
  "ada:ebsdStepSizeDefault": -9999,
  "ada:sampleTiltAngle": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Imaging/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semImagingTAPP-Garvie2008",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semImaging protocol \u2014 Garvie2008",
  "schema:description": "Sample imaged without coating; initial ~5% beam-induced shrinkage observed upon first e-beam exposure; sample stable thereafter; focusing performed away from particles of interest to minimise beam exposure",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "carbonaceous nanoglobules"
    ],
    "ada:targetMaterialColumns": [
      {
        "schema:valueName": "targetMaterial",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
        "schema:name": "example instrumentName"
      }
    ]
  },
  "ada:samplingUnitSelectionCriteriaDefault": "N \u2014 no rule is given for which globules were imaged; the stated criterion is at sample level, \"Several millimeter-sized pieces of the pristine Tagish Lake meteorite free of fusion crust were digested in HCl and HF in order to concentrate the carbonaceous materials\" (p.1)",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "FEI / Thermo Fisher Scientific",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Nova 200 NanoLab DualBeam",
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
            "SE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "In-lens / TLD (through-the-lens)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/SEM/part/SE-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "BSE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/BSE-Detector"
        }
      ],
      "schema:description": "FIB-SEM dual-beam",
      "ada:acceleratingVoltageDefault": "500 V; 1 kV; 5 kV",
      "ada:workingDistanceDefault": "0.5\u20135.4 mm",
      "ada:mappingBeamCurrentDefault": "70 fA (500 V); 1.4 pA (1 kV); 98 pA (5 kV)",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "School of Earth and Space Exploration / School of Materials, Arizona State University"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "FIB milling and TEM cross-section preparation (same instrument)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Grain (individual carbonaceous nanoglobule) \u2014 \"low voltage scanning electron microscopy (SEM) was used to characterize the globule forms and external structures\" (p.1) of globules on an Al-SEM stub (p.2)",
  "ada:analyticalMode": [
    "SE Imaging"
  ],
  "ada:reportedProperties": [
    "globule morphology (nominal); globule size (\u00b5m); surface structure (nominal) \u2014 Globule morphology, size and surface structure (nominal, with sizes in \u00b5m) \u2014 the imaging is used \"to characterize the globule forms and external structures\" (p.1)"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "HCl and HF acid dissolution residue from pristine Tagish Lake pieces; deposited on lacey C TEM grid attached to Al-SEM stub; uncoated",
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
        "ada:ebsdIndexingMethod": "missing"
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
      "schema:name": "semImaging",
      "schema:termCode": "semImaging"
    }
  ],
  "ada:clAcquisitionMode": "missing",
  "ada:clIntegrationTimeDefault": -9999,
  "ada:clWavelengthRange": -9999,
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:ebsdDetectorConfiguration": "missing",
  "ada:ebsdPhaseListDefault": "missing",
  "ada:ebsdStepSizeDefault": -9999,
  "ada:sampleTiltAngle": -9999,
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

<ex:semImagingTAPP-Garvie2008> a cdi:Activity,
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
                    ada:ebsdIndexingMethod "missing" ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:description "HCl and HF acid dissolution residue from pristine Tagish Lake pieces; deposited on lacey C TEM grid attached to Al-SEM stub; uncoated" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "Sample imaged without coating; initial ~5% beam-induced shrinkage observed upon first e-beam exposure; sample stable thereafter; focusing performed away from particles of interest to minimise beam exposure" ;
    schema1:instrument <ex:instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "School of Earth and Space Exploration / School of Materials, Arizona State University" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semImaging" ;
            schema1:termCode "semImaging" ] ;
    schema1:name "semImaging protocol — Garvie2008" ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "FIB milling and TEM cross-section preparation (same instrument)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "SE Imaging" ;
    ada:clAcquisitionMode "missing" ;
    ada:clIntegrationTimeDefault -9999 ;
    ada:clWavelengthRange -9999 ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:ebsdDetectorConfiguration "missing" ;
    ada:ebsdPhaseListDefault "missing" ;
    ada:ebsdStepSizeDefault -9999 ;
    ada:reportedProperties "globule morphology (nominal); globule size (µm); surface structure (nominal) — Globule morphology, size and surface structure (nominal, with sizes in µm) — the imaging is used \"to characterize the globule forms and external structures\" (p.1)" ;
    ada:sampleTiltAngle -9999 ;
    ada:samplingUnitSelectionCriteriaDefault "N — no rule is given for which globules were imaged; the stated criterion is at sample level, \"Several millimeter-sized pieces of the pristine Tagish Lake meteorite free of fusion crust were digested in HCl and HF in order to concentrate the carbonaceous materials\" (p.1)" ;
    ada:samplingUnitType "Grain (individual carbonaceous nanoglobule) — \"low voltage scanning electron microscopy (SEM) was used to characterize the globule forms and external structures\" (p.1) of globules on an Al-SEM stub (p.2)" ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "carbonaceous nanoglobules" ;
            ada:targetMaterialColumns [ schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ] ] .

<ex:instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:description "FIB-SEM dual-beam" ;
    schema1:hasPart <ex:instrument/SEM/part/BSE-Detector>,
        <ex:instrument/SEM/part/Electron-Source>,
        <ex:instrument/SEM/part/SE-Detector> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "FEI / Thermo Fisher Scientific" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Nova 200 NanoLab DualBeam" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "500 V; 1 kV; 5 kV" ;
    ada:mappingBeamCurrentDefault "70 fA (500 V); 1.4 pA (1 kV); 98 pA (5 kV)" ;
    ada:workingDistanceDefault "0.5–5.4 mm" .

<ex:instrument/SEM/part/BSE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "BSE Detector" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Unknown" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/SE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SE Detector" ;
    schema1:name "In-lens / TLD (through-the-lens)" .


```


### semImagingTAPP example Genge2025
semImagingTAPP instance derived from Genge et al. 2025 | Micrometeorite NG-1 (CV3-like) | BSE Imaging (ZEISS Sigma 1550VP, 10 kV).
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
  "@id": "ex:semImagingTAPP-Genge2025",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semImaging protocol — Genge2025",
  "schema:description": "semImagingTAPP instance derived from Genge et al. 2025 | Micrometeorite NG-1 (CV3-like) | BSE Imaging (ZEISS Sigma 1550VP, 10 kV) (publication column of SEM_Imaging_TAPP_v44.csv).",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "micrometeorite"
    ],
    "ada:targetMaterialColumns": [
      {
        "schema:valueName": "targetMaterial",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
        "schema:name": "example instrumentName"
      }
    ]
  },
  "ada:samplingUnitSelectionCriteriaDefault": "N — the target phases are named (see `Sampling Unit Type`) but no rule is given for choosing the imaged areas",
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
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "BSE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/BSE-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "SE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/SE-Detector"
        }
      ],
      "schema:description": "VP-SEM",
      "ada:acceleratingVoltageDefault": "10 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName",
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:workingDistanceDefault": -9999
    }
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
        "schema:name": "EDS (same session, same instrument); EBSD (same instrument); EPMA (JEOL JXA-iHP200F, WDS, out of scope)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Whole sample (the NG-1 section) > Phase — BSE imaging was used \"to determine the composition and structure of the Al-Cu alloy phases and associated minerals\" in the NG-1 section, with settings given per phase (\"12 kV for metals and 10 kV for silicates and oxides, beam current at 10 nA for metals and 5 nA for silicates and oxides\", p.2)",
  "ada:analyticalMode": [
    "BSE Imaging"
  ],
  "ada:reportedProperties": [
    "texture (nominal); phase distribution (nominal); grain size (µm); modal abundance (vol%) — Texture and phase distribution (nominal), with grain sizes in µm and a modal estimate by area — e.g. \"subhedral crystals of Fe-bearing olivine (Fa11–25, 37 vol %), up to 10.8 µm in size\" (p.2)"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "semImaging",
      "schema:termCode": "semImaging"
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
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
        "ada:ebsdIndexingMethod": "missing"
      }
    ]
  },
  "ada:clAcquisitionMode": "missing",
  "ada:clIntegrationTimeDefault": -9999,
  "ada:clWavelengthRange": -9999,
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:ebsdDetectorConfiguration": "missing",
  "ada:ebsdPhaseListDefault": "missing",
  "ada:ebsdStepSizeDefault": -9999,
  "ada:sampleTiltAngle": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Imaging/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semImagingTAPP-Genge2025",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semImaging protocol \u2014 Genge2025",
  "schema:description": "semImagingTAPP instance derived from Genge et al. 2025 | Micrometeorite NG-1 (CV3-like) | BSE Imaging (ZEISS Sigma 1550VP, 10 kV) (publication column of SEM_Imaging_TAPP_v44.csv).",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "micrometeorite"
    ],
    "ada:targetMaterialColumns": [
      {
        "schema:valueName": "targetMaterial",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
        "schema:name": "example instrumentName"
      }
    ]
  },
  "ada:samplingUnitSelectionCriteriaDefault": "N \u2014 the target phases are named (see `Sampling Unit Type`) but no rule is given for choosing the imaged areas",
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
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "BSE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/BSE-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "SE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/SE-Detector"
        }
      ],
      "schema:description": "VP-SEM",
      "ada:acceleratingVoltageDefault": "10 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName",
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:workingDistanceDefault": -9999
    }
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
        "schema:name": "EDS (same session, same instrument); EBSD (same instrument); EPMA (JEOL JXA-iHP200F, WDS, out of scope)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Whole sample (the NG-1 section) > Phase \u2014 BSE imaging was used \"to determine the composition and structure of the Al-Cu alloy phases and associated minerals\" in the NG-1 section, with settings given per phase (\"12 kV for metals and 10 kV for silicates and oxides, beam current at 10 nA for metals and 5 nA for silicates and oxides\", p.2)",
  "ada:analyticalMode": [
    "BSE Imaging"
  ],
  "ada:reportedProperties": [
    "texture (nominal); phase distribution (nominal); grain size (\u00b5m); modal abundance (vol%) \u2014 Texture and phase distribution (nominal), with grain sizes in \u00b5m and a modal estimate by area \u2014 e.g. \"subhedral crystals of Fe-bearing olivine (Fa11\u201325, 37 vol %), up to 10.8 \u00b5m in size\" (p.2)"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "semImaging",
      "schema:termCode": "semImaging"
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
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
        "ada:ebsdIndexingMethod": "missing"
      }
    ]
  },
  "ada:clAcquisitionMode": "missing",
  "ada:clIntegrationTimeDefault": -9999,
  "ada:clWavelengthRange": -9999,
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:ebsdDetectorConfiguration": "missing",
  "ada:ebsdPhaseListDefault": "missing",
  "ada:ebsdStepSizeDefault": -9999,
  "ada:sampleTiltAngle": -9999,
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

<ex:semImagingTAPP-Genge2025> a cdi:Activity,
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
                    schema1:description "missing" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:ebsdIndexingMethod "missing" ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "semImagingTAPP instance derived from Genge et al. 2025 | Micrometeorite NG-1 (CV3-like) | BSE Imaging (ZEISS Sigma 1550VP, 10 kV) (publication column of SEM_Imaging_TAPP_v44.csv)." ;
    schema1:instrument <ex:instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "GPS Division Analytical Facility, California Institute of Technology" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semImaging" ;
            schema1:termCode "semImaging" ] ;
    schema1:name "semImaging protocol — Genge2025" ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "EDS (same session, same instrument); EBSD (same instrument); EPMA (JEOL JXA-iHP200F, WDS, out of scope)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "BSE Imaging" ;
    ada:clAcquisitionMode "missing" ;
    ada:clIntegrationTimeDefault -9999 ;
    ada:clWavelengthRange -9999 ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:ebsdDetectorConfiguration "missing" ;
    ada:ebsdPhaseListDefault "missing" ;
    ada:ebsdStepSizeDefault -9999 ;
    ada:reportedProperties "texture (nominal); phase distribution (nominal); grain size (µm); modal abundance (vol%) — Texture and phase distribution (nominal), with grain sizes in µm and a modal estimate by area — e.g. \"subhedral crystals of Fe-bearing olivine (Fa11–25, 37 vol %), up to 10.8 µm in size\" (p.2)" ;
    ada:sampleTiltAngle -9999 ;
    ada:samplingUnitSelectionCriteriaDefault "N — the target phases are named (see `Sampling Unit Type`) but no rule is given for choosing the imaged areas" ;
    ada:samplingUnitType "Whole sample (the NG-1 section) > Phase — BSE imaging was used \"to determine the composition and structure of the Al-Cu alloy phases and associated minerals\" in the NG-1 section, with settings given per phase (\"12 kV for metals and 10 kV for silicates and oxides, beam current at 10 nA for metals and 5 nA for silicates and oxides\", p.2)" ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "micrometeorite" ;
            ada:targetMaterialColumns [ schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ] ] .

<ex:instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:description "VP-SEM" ;
    schema1:hasPart <ex:instrument/SEM/part/BSE-Detector>,
        <ex:instrument/SEM/part/Electron-Source>,
        <ex:instrument/SEM/part/SE-Detector> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Zeiss" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "ZEISS 1550VP" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "10 kV" ;
    ada:mappingBeamCurrentDefault -9999 ;
    ada:workingDistanceDefault -9999 .

<ex:instrument/SEM/part/BSE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "BSE Detector" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Unknown" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/SE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SE Detector" ;
    schema1:name "missing" .


```


### semImagingTAPP example Genge2025-2
semImagingTAPP instance derived from Genge et al. 2025 | Micrometeorite NG-1 (CV3-like) | EBSD (ZEISS Sigma 1550VP, 20 kV).
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
  "@id": "ex:semImagingTAPP-Genge2025-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semImaging protocol — Genge2025-2",
  "schema:description": "EBSD done in variable pressure mode (25 Pa) to suppress charging on tilted sample; spatial resolution ~30 nm stated; calibrated with single-crystal silicon standard",
  "ada:targetMaterialTemplate": {
    "ada:targetMaterialDeclaration": "Al-Cu alloy phases — Micrometeorite NG-1, Al-Cu-alloy-bearing, CV3-like composition; Democratic Republic of Congo",
    "ada:targetMaterialColumns": [
      {
        "schema:valueName": "targetMaterial",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
        "schema:name": "example instrumentName"
      }
    ],
    "ada:defaultTargetMaterials": []
  },
  "ada:samplingUnitSelectionCriteriaDefault": "N — no rule is given for choosing which grains were indexed",
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
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "BSE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/BSE-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "SE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/SE-Detector"
        }
      ],
      "schema:description": "VP-SEM",
      "ada:acceleratingVoltageDefault": "20 kV",
      "ada:mappingBeamCurrentDefault": "6 nA",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName",
      "ada:workingDistanceDefault": -9999
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/semImagingTAPP/chamberPressureDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "chamberPressureDefault",
      "schema:name": "Chamber Pressure",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 25,
      "schema:description": "25 Pa (variable pressure mode)"
    }
  ],
  "ada:sampleTiltAngle": "70 degrees",
  "schema:actionProcess": {
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
        "schema:description": "missing"
      },
      {
        "schema:name": "Data reduction",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/semImagingTAPP/crystalStructureDatabaseDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "crystalStructureDatabaseDefault",
            "schema:name": "Crystal Structure Database",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "ICSD (Inorganic Crystal Structure Database)"
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
        "ada:ebsdIndexingMethod": "missing"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
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
        "schema:name": "BSE Imaging and EDS (same instrument); SIMS (University of Wisconsin-Madison); EPMA (out of scope)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Phase > Grain — \"Electron back-scatter diffraction (EBSD) analyses were operated at 20 kV and 6 nA in focused beam mode\", the beam \"several nanometers in diameter\" with \"~30 nm\" resolution for diffracted electrons, run for \"Structural information\" on the alloy phases (p.2)",
  "ada:analyticalMode": [
    "EBSD"
  ],
  "ada:reportedProperties": [
    "crystal structure (nominal); crystal orientation (nominal); cell constants (Å) — Crystal structure and orientation of the alloy phases (nominal), acquired for \"Structural information\" at 20 kV and 6 nA with ~30 nm spatial resolution for the diffracted electrons (p.2)"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "semImaging",
      "schema:termCode": "semImaging"
    }
  ],
  "ada:clAcquisitionMode": "missing",
  "ada:clIntegrationTimeDefault": -9999,
  "ada:clWavelengthRange": -9999,
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:ebsdDetectorConfiguration": "missing",
  "ada:ebsdPhaseListDefault": "missing",
  "ada:ebsdStepSizeDefault": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Imaging/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semImagingTAPP-Genge2025-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semImaging protocol \u2014 Genge2025-2",
  "schema:description": "EBSD done in variable pressure mode (25 Pa) to suppress charging on tilted sample; spatial resolution ~30 nm stated; calibrated with single-crystal silicon standard",
  "ada:targetMaterialTemplate": {
    "ada:targetMaterialDeclaration": "Al-Cu alloy phases \u2014 Micrometeorite NG-1, Al-Cu-alloy-bearing, CV3-like composition; Democratic Republic of Congo",
    "ada:targetMaterialColumns": [
      {
        "schema:valueName": "targetMaterial",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
        "schema:name": "example instrumentName"
      }
    ],
    "ada:defaultTargetMaterials": []
  },
  "ada:samplingUnitSelectionCriteriaDefault": "N \u2014 no rule is given for choosing which grains were indexed",
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
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "BSE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/BSE-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "SE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/SE-Detector"
        }
      ],
      "schema:description": "VP-SEM",
      "ada:acceleratingVoltageDefault": "20 kV",
      "ada:mappingBeamCurrentDefault": "6 nA",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName",
      "ada:workingDistanceDefault": -9999
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/semImagingTAPP/chamberPressureDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "chamberPressureDefault",
      "schema:name": "Chamber Pressure",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 25,
      "schema:description": "25 Pa (variable pressure mode)"
    }
  ],
  "ada:sampleTiltAngle": "70 degrees",
  "schema:actionProcess": {
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
        "schema:description": "missing"
      },
      {
        "schema:name": "Data reduction",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/semImagingTAPP/crystalStructureDatabaseDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "crystalStructureDatabaseDefault",
            "schema:name": "Crystal Structure Database",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "ICSD (Inorganic Crystal Structure Database)"
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
        "ada:ebsdIndexingMethod": "missing"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
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
        "schema:name": "BSE Imaging and EDS (same instrument); SIMS (University of Wisconsin-Madison); EPMA (out of scope)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Phase > Grain \u2014 \"Electron back-scatter diffraction (EBSD) analyses were operated at 20 kV and 6 nA in focused beam mode\", the beam \"several nanometers in diameter\" with \"~30 nm\" resolution for diffracted electrons, run for \"Structural information\" on the alloy phases (p.2)",
  "ada:analyticalMode": [
    "EBSD"
  ],
  "ada:reportedProperties": [
    "crystal structure (nominal); crystal orientation (nominal); cell constants (\u00c5) \u2014 Crystal structure and orientation of the alloy phases (nominal), acquired for \"Structural information\" at 20 kV and 6 nA with ~30 nm spatial resolution for the diffracted electrons (p.2)"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "semImaging",
      "schema:termCode": "semImaging"
    }
  ],
  "ada:clAcquisitionMode": "missing",
  "ada:clIntegrationTimeDefault": -9999,
  "ada:clWavelengthRange": -9999,
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:ebsdDetectorConfiguration": "missing",
  "ada:ebsdPhaseListDefault": "missing",
  "ada:ebsdStepSizeDefault": -9999,
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

<ex:semImagingTAPP-Genge2025-2> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semImagingTAPP/crystalStructureDatabaseDefault> ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:ebsdIndexingMethod "missing" ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:description "missing" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semImagingTAPP/chamberPressureDefault> ;
    schema1:datePublished "missing" ;
    schema1:description "EBSD done in variable pressure mode (25 Pa) to suppress charging on tilted sample; spatial resolution ~30 nm stated; calibrated with single-crystal silicon standard" ;
    schema1:instrument <ex:instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "GPS Division Analytical Facility, California Institute of Technology" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semImaging" ;
            schema1:termCode "semImaging" ] ;
    schema1:name "semImaging protocol — Genge2025-2" ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "BSE Imaging and EDS (same instrument); SIMS (University of Wisconsin-Madison); EPMA (out of scope)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "EBSD" ;
    ada:clAcquisitionMode "missing" ;
    ada:clIntegrationTimeDefault -9999 ;
    ada:clWavelengthRange -9999 ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:ebsdDetectorConfiguration "missing" ;
    ada:ebsdPhaseListDefault "missing" ;
    ada:ebsdStepSizeDefault -9999 ;
    ada:reportedProperties "crystal structure (nominal); crystal orientation (nominal); cell constants (Å) — Crystal structure and orientation of the alloy phases (nominal), acquired for \"Structural information\" at 20 kV and 6 nA with ~30 nm spatial resolution for the diffracted electrons (p.2)" ;
    ada:sampleTiltAngle "70 degrees" ;
    ada:samplingUnitSelectionCriteriaDefault "N — no rule is given for choosing which grains were indexed" ;
    ada:samplingUnitType "Phase > Grain — \"Electron back-scatter diffraction (EBSD) analyses were operated at 20 kV and 6 nA in focused beam mode\", the beam \"several nanometers in diameter\" with \"~30 nm\" resolution for diffracted electrons, run for \"Structural information\" on the alloy phases (p.2)" ;
    ada:targetMaterialTemplate [ ada:targetMaterialColumns [ schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ] ;
            ada:targetMaterialDeclaration "Al-Cu alloy phases — Micrometeorite NG-1, Al-Cu-alloy-bearing, CV3-like composition; Democratic Republic of Congo" ] .

<ex:instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:description "VP-SEM" ;
    schema1:hasPart <ex:instrument/SEM/part/BSE-Detector>,
        <ex:instrument/SEM/part/Electron-Source>,
        <ex:instrument/SEM/part/SE-Detector> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Zeiss" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "ZEISS 1550VP" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "20 kV" ;
    ada:mappingBeamCurrentDefault "6 nA" ;
    ada:workingDistanceDefault -9999 .

<ex:instrument/SEM/part/BSE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "BSE Detector" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Unknown" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/SE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SE Detector" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/semImagingTAPP/chamberPressureDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 25 ;
    schema1:description "25 Pa (variable pressure mode)" ;
    schema1:name "Chamber Pressure" ;
    schema1:valueName "chamberPressureDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/semImagingTAPP/crystalStructureDatabaseDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "ICSD (Inorganic Crystal Structure Database)" ;
    schema1:name "Crystal Structure Database" ;
    schema1:valueName "crystalStructureDatabaseDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .


```


### semImagingTAPP example Gucsik2013
semImagingTAPP instance derived from Gucsik et al. 2013 | Forsterite, Kaba meteorite (CV3) | CL Mapping (JEOL JSM-5410LV).
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
  "@id": "ex:semImagingTAPP-Gucsik2013",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semImaging protocol — Gucsik2013",
  "schema:description": "CL color imaging also done with separate luminoscope ELM-3R (cold cathode, 10 kV, 0.5 mA, <100 Torr) — standalone CL system, not SEM-based; spectrum deconvolution via Peak Analyzer in OriginPro 8J SR2 Reported detail: ada:clAcquisitionMode = Panchromatic; Spectral point.",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "forsterite"
    ],
    "ada:targetMaterialColumns": [
      {
        "schema:valueName": "targetMaterial",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
        "schema:name": "example instrumentName"
      }
    ]
  },
  "ada:samplingUnitSelectionCriteriaDefault": "Freedom from defects, after a prior survey — \"Following a systematic optical microscopecathodoluminescence study of a Kaba thin section, seven representative grains (designated as B-1 through B-7) were selected for further analyses because they did not contain any irregular fracturing or crystallographic imperfections\" (p.2)",
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
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/semImagingTAPP/clDetectorConfiguration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semImagingTAPP/clDetectorConfiguration"
            }
          ],
          "schema:name": "CL Detector Configuration",
          "schema:value": "Mini-CL (Gatan, multialkali PMT) for scanning CL images; Oxford MonoCL2 grating monochromator with Hamamatsu R2228 PMT and parabolic mirror (75% efficiency) for spectral CL"
        },
        {
          "@id": "ada:parameter/semImagingTAPP/clGrating",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semImagingTAPP/clGrating"
            }
          ],
          "schema:name": "CL Grating",
          "schema:value": "1200 gr/mm, focal length 0.3 m, F/4.2, resolution 0.5 nm, slit width 4 mm (Oxford MonoCL2)"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "BSE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/BSE-Detector"
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
            "SE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/SE-Detector"
        }
      ],
      "schema:name": "example instrumentName",
      "ada:acceleratingVoltageDefault": -9999,
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:workingDistanceDefault": -9999
    }
  ],
  "ada:clAcquisitionMode": "Spectral point",
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "EDS and BSE Imaging (same instrument); EPMA with WDS (JEOL JXA-8900R, out of scope)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Grain > Region of interest (core and rim) — CL was measured on \"seven representative grains (designated as B-1 through B-7)\" (p.2); \"CL spectra of red luminescent forsterite grains\" are reported against their cores, which \"show CL blue luminescence\" (p.1)",
  "ada:analyticalMode": [
    "CL Mapping"
  ],
  "ada:reportedProperties": [
    "CL emission bands (nm); CL colour (nominal); CL zoning (nominal) — Cathodoluminescence emission bands, reported by wavelength (nm) and colour — \"two broad emission bands at approximately 630 nm (impurity center of divalent Mn ions) in the red region and above 700 nm (trivalent Cr ions) in the red–IR region\", with grain cores giving \"a characteristic broad band emission at 400 nm\" (p.1); the CL colour and its spatial zoning are nominal properties"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "semImaging",
      "schema:termCode": "semImaging"
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
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
        "ada:ebsdIndexingMethod": "missing"
      }
    ]
  },
  "ada:clIntegrationTimeDefault": -9999,
  "ada:clWavelengthRange": -9999,
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:ebsdDetectorConfiguration": "missing",
  "ada:ebsdPhaseListDefault": "missing",
  "ada:ebsdStepSizeDefault": -9999,
  "ada:sampleTiltAngle": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Imaging/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semImagingTAPP-Gucsik2013",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semImaging protocol \u2014 Gucsik2013",
  "schema:description": "CL color imaging also done with separate luminoscope ELM-3R (cold cathode, 10 kV, 0.5 mA, <100 Torr) \u2014 standalone CL system, not SEM-based; spectrum deconvolution via Peak Analyzer in OriginPro 8J SR2 Reported detail: ada:clAcquisitionMode = Panchromatic; Spectral point.",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "forsterite"
    ],
    "ada:targetMaterialColumns": [
      {
        "schema:valueName": "targetMaterial",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
        "schema:name": "example instrumentName"
      }
    ]
  },
  "ada:samplingUnitSelectionCriteriaDefault": "Freedom from defects, after a prior survey \u2014 \"Following a systematic optical microscopecathodoluminescence study of a Kaba thin section, seven representative grains (designated as B-1 through B-7) were selected for further analyses because they did not contain any irregular fracturing or crystallographic imperfections\" (p.2)",
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
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/semImagingTAPP/clDetectorConfiguration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semImagingTAPP/clDetectorConfiguration"
            }
          ],
          "schema:name": "CL Detector Configuration",
          "schema:value": "Mini-CL (Gatan, multialkali PMT) for scanning CL images; Oxford MonoCL2 grating monochromator with Hamamatsu R2228 PMT and parabolic mirror (75% efficiency) for spectral CL"
        },
        {
          "@id": "ada:parameter/semImagingTAPP/clGrating",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semImagingTAPP/clGrating"
            }
          ],
          "schema:name": "CL Grating",
          "schema:value": "1200 gr/mm, focal length 0.3 m, F/4.2, resolution 0.5 nm, slit width 4 mm (Oxford MonoCL2)"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "BSE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/BSE-Detector"
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
            "SE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/SE-Detector"
        }
      ],
      "schema:name": "example instrumentName",
      "ada:acceleratingVoltageDefault": -9999,
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:workingDistanceDefault": -9999
    }
  ],
  "ada:clAcquisitionMode": "Spectral point",
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "EDS and BSE Imaging (same instrument); EPMA with WDS (JEOL JXA-8900R, out of scope)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Grain > Region of interest (core and rim) \u2014 CL was measured on \"seven representative grains (designated as B-1 through B-7)\" (p.2); \"CL spectra of red luminescent forsterite grains\" are reported against their cores, which \"show CL blue luminescence\" (p.1)",
  "ada:analyticalMode": [
    "CL Mapping"
  ],
  "ada:reportedProperties": [
    "CL emission bands (nm); CL colour (nominal); CL zoning (nominal) \u2014 Cathodoluminescence emission bands, reported by wavelength (nm) and colour \u2014 \"two broad emission bands at approximately 630 nm (impurity center of divalent Mn ions) in the red region and above 700 nm (trivalent Cr ions) in the red\u2013IR region\", with grain cores giving \"a characteristic broad band emission at 400 nm\" (p.1); the CL colour and its spatial zoning are nominal properties"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "semImaging",
      "schema:termCode": "semImaging"
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
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
        "ada:ebsdIndexingMethod": "missing"
      }
    ]
  },
  "ada:clIntegrationTimeDefault": -9999,
  "ada:clWavelengthRange": -9999,
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:ebsdDetectorConfiguration": "missing",
  "ada:ebsdPhaseListDefault": "missing",
  "ada:ebsdStepSizeDefault": -9999,
  "ada:sampleTiltAngle": -9999,
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

<ex:semImagingTAPP-Gucsik2013> a cdi:Activity,
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
                    schema1:description "missing" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:ebsdIndexingMethod "missing" ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "CL color imaging also done with separate luminoscope ELM-3R (cold cathode, 10 kV, 0.5 mA, <100 Torr) — standalone CL system, not SEM-based; spectrum deconvolution via Peak Analyzer in OriginPro 8J SR2 Reported detail: ada:clAcquisitionMode = Panchromatic; Spectral point." ;
    schema1:instrument <ex:instrument/SEM> ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semImaging" ;
            schema1:termCode "semImaging" ] ;
    schema1:name "semImaging protocol — Gucsik2013" ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "EDS and BSE Imaging (same instrument); EPMA with WDS (JEOL JXA-8900R, out of scope)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "CL Mapping" ;
    ada:clAcquisitionMode "Spectral point" ;
    ada:clIntegrationTimeDefault -9999 ;
    ada:clWavelengthRange -9999 ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:ebsdDetectorConfiguration "missing" ;
    ada:ebsdPhaseListDefault "missing" ;
    ada:ebsdStepSizeDefault -9999 ;
    ada:reportedProperties "CL emission bands (nm); CL colour (nominal); CL zoning (nominal) — Cathodoluminescence emission bands, reported by wavelength (nm) and colour — \"two broad emission bands at approximately 630 nm (impurity center of divalent Mn ions) in the red region and above 700 nm (trivalent Cr ions) in the red–IR region\", with grain cores giving \"a characteristic broad band emission at 400 nm\" (p.1); the CL colour and its spatial zoning are nominal properties" ;
    ada:sampleTiltAngle -9999 ;
    ada:samplingUnitSelectionCriteriaDefault "Freedom from defects, after a prior survey — \"Following a systematic optical microscopecathodoluminescence study of a Kaba thin section, seven representative grains (designated as B-1 through B-7) were selected for further analyses because they did not contain any irregular fracturing or crystallographic imperfections\" (p.2)" ;
    ada:samplingUnitType "Grain > Region of interest (core and rim) — CL was measured on \"seven representative grains (designated as B-1 through B-7)\" (p.2); \"CL spectra of red luminescent forsterite grains\" are reported against their cores, which \"show CL blue luminescence\" (p.1)" ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "forsterite" ;
            ada:targetMaterialColumns [ schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ] ] .

<ex:instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semImagingTAPP/clDetectorConfiguration>,
        <https://ada.astromat.org/metadata/parameter/semImagingTAPP/clGrating> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:description "Standard SEM" ;
    schema1:hasPart <ex:instrument/SEM/part/BSE-Detector>,
        <ex:instrument/SEM/part/Electron-Source>,
        <ex:instrument/SEM/part/SE-Detector> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "JEOL" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "JSM-5410LV" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault -9999 ;
    ada:mappingBeamCurrentDefault -9999 ;
    ada:workingDistanceDefault -9999 .

<ex:instrument/SEM/part/BSE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "BSE Detector" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "missing" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/SE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SE Detector" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/semImagingTAPP/clDetectorConfiguration> a schema1:PropertyValue ;
    schema1:name "CL Detector Configuration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semImagingTAPP/clDetectorConfiguration> ;
    schema1:value "Mini-CL (Gatan, multialkali PMT) for scanning CL images; Oxford MonoCL2 grating monochromator with Hamamatsu R2228 PMT and parabolic mirror (75% efficiency) for spectral CL" .

<https://ada.astromat.org/metadata/parameter/semImagingTAPP/clGrating> a schema1:PropertyValue ;
    schema1:name "CL Grating" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semImagingTAPP/clGrating> ;
    schema1:value "1200 gr/mm, focal length 0.3 m, F/4.2, resolution 0.5 nm, slit width 4 mm (Oxford MonoCL2)" .


```


### semImagingTAPP example Izawa2010
semImagingTAPP instance derived from Izawa et al. 2010 | Tagish Lake (C2) meteorite | CL Mapping (Hitachi S-2500C).
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
  "@id": "ex:semImagingTAPP-Izawa2010",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semImaging protocol — Izawa2010",
  "schema:description": "Digiscan II beam controller used for CL raster; multi-channel color CL distinguishes ~4 spectral bands; beam-induced CL may persist from long-lived IR emission in carbonates",
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
        "schema:name": "example instrumentName"
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
        "schema:name": "Hitachi",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "S-2500C",
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
          "schema:description": "Tungsten (W)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/SEM/part/Electron-Source",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "BSE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/BSE-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "SE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/SE-Detector"
        }
      ],
      "schema:description": "Standard SEM",
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/semImagingTAPP/clDetectorConfiguration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semImagingTAPP/clDetectorConfiguration"
            }
          ],
          "schema:name": "CL Detector Configuration",
          "schema:value": "Gatan ChromaCL detector; 4-channel pseudo-color detection (UV: ~300-400nm, Blue: ~400-500nm, Green: ~500-600nm, Red: ~600-850nm including near-IR ~700-850nm); Robinson Backscatter detector also present"
        }
      ],
      "ada:acceleratingVoltageDefault": "15–20 kV",
      "ada:workingDistanceDefault": "~10 mm",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName",
      "ada:mappingBeamCurrentDefault": -9999
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/semImagingTAPP/chamberPressureDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "chamberPressureDefault",
      "schema:name": "Chamber Pressure",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": "High vacuum"
    }
  ],
  "ada:clAcquisitionMode": "Multi-channel pseudo-color",
  "ada:clWavelengthRange": "300–850 nm (UV ~300-400, Blue ~400-500, Green ~500-600, Red ~600-850)",
  "ada:clIntegrationTimeDefault": "80–500 ms per pixel (varied based on IR luminescence duration in carbonates)",
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Zircon and Accessory Phase Laboratory, University of Western Ontario"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-EDX (Leo 440; Leo 1540); BSE Imaging; micro-XRD; EPMA-WDS (out of scope)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Whole sample (polished thin section) > Region of interest — \"colour SEM-CL analysis of polished thin sections\" (p.1), reported as CL zoning within named textural components, \"relict CAI spinel, in chondrule and AOA forsterite, and in calcite nodules\" (p.1)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "acquisition",
      "schema:name": "Gatan DigitalMicrograph (CL image assembly)"
    },
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Gatan DigitalMicrograph"
    }
  ],
  "ada:analyticalMode": [
    "CL Mapping"
  ],
  "ada:reportedProperties": [
    "CL colour (nominal); CL zoning (nominal) — Cathodoluminescence colour and zoning (nominal), recorded through four spectral channels — \"red (600–850 nm, including near-infrared from 700–850 nm), green (500…\", detected \"in the range 300–850 nm\" (p.3); the reported result is CL zoning in relict CAI spinel, chondrule and AOA forsterite and calcite nodules (p.1)"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Carbon-coated polished thin sections; high vacuum analysis",
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
        "ada:ebsdIndexingMethod": "missing"
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
      "schema:name": "semImaging",
      "schema:termCode": "semImaging"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:ebsdDetectorConfiguration": "missing",
  "ada:ebsdPhaseListDefault": "missing",
  "ada:ebsdStepSizeDefault": -9999,
  "ada:sampleTiltAngle": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Imaging/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semImagingTAPP-Izawa2010",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semImaging protocol \u2014 Izawa2010",
  "schema:description": "Digiscan II beam controller used for CL raster; multi-channel color CL distinguishes ~4 spectral bands; beam-induced CL may persist from long-lived IR emission in carbonates",
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
        "schema:name": "example instrumentName"
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
        "schema:name": "Hitachi",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "S-2500C",
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
          "schema:description": "Tungsten (W)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/SEM/part/Electron-Source",
          "schema:name": "missing"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "BSE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/BSE-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "SE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/SE-Detector"
        }
      ],
      "schema:description": "Standard SEM",
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/semImagingTAPP/clDetectorConfiguration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semImagingTAPP/clDetectorConfiguration"
            }
          ],
          "schema:name": "CL Detector Configuration",
          "schema:value": "Gatan ChromaCL detector; 4-channel pseudo-color detection (UV: ~300-400nm, Blue: ~400-500nm, Green: ~500-600nm, Red: ~600-850nm including near-IR ~700-850nm); Robinson Backscatter detector also present"
        }
      ],
      "ada:acceleratingVoltageDefault": "15\u201320 kV",
      "ada:workingDistanceDefault": "~10 mm",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName",
      "ada:mappingBeamCurrentDefault": -9999
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/semImagingTAPP/chamberPressureDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "chamberPressureDefault",
      "schema:name": "Chamber Pressure",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": "High vacuum"
    }
  ],
  "ada:clAcquisitionMode": "Multi-channel pseudo-color",
  "ada:clWavelengthRange": "300\u2013850 nm (UV ~300-400, Blue ~400-500, Green ~500-600, Red ~600-850)",
  "ada:clIntegrationTimeDefault": "80\u2013500 ms per pixel (varied based on IR luminescence duration in carbonates)",
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Zircon and Accessory Phase Laboratory, University of Western Ontario"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "SEM-EDX (Leo 440; Leo 1540); BSE Imaging; micro-XRD; EPMA-WDS (out of scope)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Whole sample (polished thin section) > Region of interest \u2014 \"colour SEM-CL analysis of polished thin sections\" (p.1), reported as CL zoning within named textural components, \"relict CAI spinel, in chondrule and AOA forsterite, and in calcite nodules\" (p.1)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "acquisition",
      "schema:name": "Gatan DigitalMicrograph (CL image assembly)"
    },
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Gatan DigitalMicrograph"
    }
  ],
  "ada:analyticalMode": [
    "CL Mapping"
  ],
  "ada:reportedProperties": [
    "CL colour (nominal); CL zoning (nominal) \u2014 Cathodoluminescence colour and zoning (nominal), recorded through four spectral channels \u2014 \"red (600\u2013850 nm, including near-infrared from 700\u2013850 nm), green (500\u2026\", detected \"in the range 300\u2013850 nm\" (p.3); the reported result is CL zoning in relict CAI spinel, chondrule and AOA forsterite and calcite nodules (p.1)"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Carbon-coated polished thin sections; high vacuum analysis",
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
        "ada:ebsdIndexingMethod": "missing"
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
      "schema:name": "semImaging",
      "schema:termCode": "semImaging"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:ebsdDetectorConfiguration": "missing",
  "ada:ebsdPhaseListDefault": "missing",
  "ada:ebsdStepSizeDefault": -9999,
  "ada:sampleTiltAngle": -9999,
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

<ex:semImagingTAPP-Izawa2010> a cdi:Activity,
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
                    ada:ebsdIndexingMethod "missing" ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:description "Carbon-coated polished thin sections; high vacuum analysis" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semImagingTAPP/chamberPressureDefault> ;
    schema1:datePublished "missing" ;
    schema1:description "Digiscan II beam controller used for CL raster; multi-channel color CL distinguishes ~4 spectral bands; beam-induced CL may persist from long-lived IR emission in carbonates" ;
    schema1:instrument <ex:instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Zircon and Accessory Phase Laboratory, University of Western Ontario" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semImaging" ;
            schema1:termCode "semImaging" ] ;
    schema1:name "semImaging protocol — Izawa2010" ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SEM-EDX (Leo 440; Leo 1540); BSE Imaging; micro-XRD; EPMA-WDS (out of scope)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "CL Mapping" ;
    ada:clAcquisitionMode "Multi-channel pseudo-color" ;
    ada:clIntegrationTimeDefault "80–500 ms per pixel (varied based on IR luminescence duration in carbonates)" ;
    ada:clWavelengthRange "300–850 nm (UV ~300-400, Blue ~400-500, Green ~500-600, Red ~600-850)" ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:ebsdDetectorConfiguration "missing" ;
    ada:ebsdPhaseListDefault "missing" ;
    ada:ebsdStepSizeDefault -9999 ;
    ada:reportedProperties "CL colour (nominal); CL zoning (nominal) — Cathodoluminescence colour and zoning (nominal), recorded through four spectral channels — \"red (600–850 nm, including near-infrared from 700–850 nm), green (500…\", detected \"in the range 300–850 nm\" (p.3); the reported result is CL zoning in relict CAI spinel, chondrule and AOA forsterite and calcite nodules (p.1)" ;
    ada:sampleTiltAngle -9999 ;
    ada:samplingUnitSelectionCriteriaDefault "Located by prior μXRD reconnaissance — the paper's stated strategy is \"an initial, non-destructive in situ reconnaissance step using micro X-ray diffraction (mXRD) ... to identify features of interest, followed by spatially correlated mXRD, scanning electron microscopy with energy-dispersive X-ray spectroscopy (SEM-EDX), and cathodoluminescence (CL) analysis\" (p.2)" ;
    ada:samplingUnitType "Whole sample (polished thin section) > Region of interest — \"colour SEM-CL analysis of polished thin sections\" (p.1), reported as CL zoning within named textural components, \"relict CAI spinel, in chondrule and AOA forsterite, and in calcite nodules\" (p.1)" ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "carbonaceous chondrite" ;
            ada:targetMaterialColumns [ schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ] ] ;
    bios:computationalTool [ schema1:name "Gatan DigitalMicrograph" ;
            ada:toolRole "dataReduction" ],
        [ schema1:name "Gatan DigitalMicrograph (CL image assembly)" ;
            ada:toolRole "acquisition" ] .

<ex:instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semImagingTAPP/clDetectorConfiguration> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:description "Standard SEM" ;
    schema1:hasPart <ex:instrument/SEM/part/BSE-Detector>,
        <ex:instrument/SEM/part/Electron-Source>,
        <ex:instrument/SEM/part/SE-Detector> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Hitachi" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "S-2500C" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "15–20 kV" ;
    ada:mappingBeamCurrentDefault -9999 ;
    ada:workingDistanceDefault "~10 mm" .

<ex:instrument/SEM/part/BSE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "BSE Detector" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Tungsten (W)" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/SE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SE Detector" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/semImagingTAPP/chamberPressureDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "High vacuum" ;
    schema1:name "Chamber Pressure" ;
    schema1:valueName "chamberPressureDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/semImagingTAPP/clDetectorConfiguration> a schema1:PropertyValue ;
    schema1:name "CL Detector Configuration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semImagingTAPP/clDetectorConfiguration> ;
    schema1:value "Gatan ChromaCL detector; 4-channel pseudo-color detection (UV: ~300-400nm, Blue: ~400-500nm, Green: ~500-600nm, Red: ~600-850nm including near-IR ~700-850nm); Robinson Backscatter detector also present" .


```


### semImagingTAPP example Izawa2010-2
semImagingTAPP instance derived from Izawa et al. 2010 | Tagish Lake (C2) meteorite | BSE Imaging (Leo 440).
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
  "@id": "ex:semImagingTAPP-Izawa2010-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semImaging protocol — Izawa2010-2",
  "schema:description": "semImagingTAPP instance derived from Izawa et al. 2010 | Tagish Lake (C2) meteorite | BSE Imaging (Leo 440) (publication column of SEM_Imaging_TAPP_v44.csv).",
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
        "schema:name": "example instrumentName"
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
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "BSE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/BSE-Detector"
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
            "SE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/SE-Detector"
        }
      ],
      "schema:name": "example instrumentName",
      "ada:acceleratingVoltageDefault": -9999,
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:workingDistanceDefault": -9999
    }
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
        "schema:name": "EDS (same instrument); CL (Hitachi S-2500C); BSE Imaging (Leo 1540); micro-XRD; EPMA (out of scope)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Whole sample (polished thin section) > Phase — \"Backscattered electron images and EDX element maps of the Tagish Lake sections were acquired with the Leo 440 SEM\", providing \"graphical representations of elemental distribution\" (p.3)",
  "ada:analyticalMode": [
    "BSE Imaging"
  ],
  "ada:reportedProperties": [
    "textural relationships (nominal) — 'Backscattered electron (BSE) imaging and elemental X-ray mapping provide graphical representations of elemental distribution' (p.3); the Leo 440's X-ray maps are recorded under the EDS Mapping column"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "semImaging",
      "schema:termCode": "semImaging"
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
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
        "ada:ebsdIndexingMethod": "missing"
      }
    ]
  },
  "ada:clAcquisitionMode": "missing",
  "ada:clIntegrationTimeDefault": -9999,
  "ada:clWavelengthRange": -9999,
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:ebsdDetectorConfiguration": "missing",
  "ada:ebsdPhaseListDefault": "missing",
  "ada:ebsdStepSizeDefault": -9999,
  "ada:sampleTiltAngle": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Imaging/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semImagingTAPP-Izawa2010-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semImaging protocol \u2014 Izawa2010-2",
  "schema:description": "semImagingTAPP instance derived from Izawa et al. 2010 | Tagish Lake (C2) meteorite | BSE Imaging (Leo 440) (publication column of SEM_Imaging_TAPP_v44.csv).",
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
        "schema:name": "example instrumentName"
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
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "BSE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/BSE-Detector"
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
            "SE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/SE-Detector"
        }
      ],
      "schema:name": "example instrumentName",
      "ada:acceleratingVoltageDefault": -9999,
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:workingDistanceDefault": -9999
    }
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
        "schema:name": "EDS (same instrument); CL (Hitachi S-2500C); BSE Imaging (Leo 1540); micro-XRD; EPMA (out of scope)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Whole sample (polished thin section) > Phase \u2014 \"Backscattered electron images and EDX element maps of the Tagish Lake sections were acquired with the Leo 440 SEM\", providing \"graphical representations of elemental distribution\" (p.3)",
  "ada:analyticalMode": [
    "BSE Imaging"
  ],
  "ada:reportedProperties": [
    "textural relationships (nominal) \u2014 'Backscattered electron (BSE) imaging and elemental X-ray mapping provide graphical representations of elemental distribution' (p.3); the Leo 440's X-ray maps are recorded under the EDS Mapping column"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "semImaging",
      "schema:termCode": "semImaging"
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
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
        "ada:ebsdIndexingMethod": "missing"
      }
    ]
  },
  "ada:clAcquisitionMode": "missing",
  "ada:clIntegrationTimeDefault": -9999,
  "ada:clWavelengthRange": -9999,
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:ebsdDetectorConfiguration": "missing",
  "ada:ebsdPhaseListDefault": "missing",
  "ada:ebsdStepSizeDefault": -9999,
  "ada:sampleTiltAngle": -9999,
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

<ex:semImagingTAPP-Izawa2010-2> a cdi:Activity,
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
                    schema1:description "missing" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:ebsdIndexingMethod "missing" ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "semImagingTAPP instance derived from Izawa et al. 2010 | Tagish Lake (C2) meteorite | BSE Imaging (Leo 440) (publication column of SEM_Imaging_TAPP_v44.csv)." ;
    schema1:instrument <ex:instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Surface Science Western" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semImaging" ;
            schema1:termCode "semImaging" ] ;
    schema1:name "semImaging protocol — Izawa2010-2" ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "EDS (same instrument); CL (Hitachi S-2500C); BSE Imaging (Leo 1540); micro-XRD; EPMA (out of scope)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "BSE Imaging" ;
    ada:clAcquisitionMode "missing" ;
    ada:clIntegrationTimeDefault -9999 ;
    ada:clWavelengthRange -9999 ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:ebsdDetectorConfiguration "missing" ;
    ada:ebsdPhaseListDefault "missing" ;
    ada:ebsdStepSizeDefault -9999 ;
    ada:reportedProperties "textural relationships (nominal) — 'Backscattered electron (BSE) imaging and elemental X-ray mapping provide graphical representations of elemental distribution' (p.3); the Leo 440's X-ray maps are recorded under the EDS Mapping column" ;
    ada:sampleTiltAngle -9999 ;
    ada:samplingUnitSelectionCriteriaDefault "Located by prior μXRD reconnaissance — the paper's stated strategy is \"an initial, non-destructive in situ reconnaissance step using micro X-ray diffraction (mXRD) ... to identify features of interest, followed by spatially correlated mXRD, scanning electron microscopy with energy-dispersive X-ray spectroscopy (SEM-EDX), and cathodoluminescence (CL) analysis\" (p.2)" ;
    ada:samplingUnitType "Whole sample (polished thin section) > Phase — \"Backscattered electron images and EDX element maps of the Tagish Lake sections were acquired with the Leo 440 SEM\", providing \"graphical representations of elemental distribution\" (p.3)" ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "carbonaceous chondrite" ;
            ada:targetMaterialColumns [ schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ] ] .

<ex:instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:description "Standard SEM" ;
    schema1:hasPart <ex:instrument/SEM/part/BSE-Detector>,
        <ex:instrument/SEM/part/Electron-Source>,
        <ex:instrument/SEM/part/SE-Detector> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Zeiss" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Leo 440" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault -9999 ;
    ada:mappingBeamCurrentDefault -9999 ;
    ada:workingDistanceDefault -9999 .

<ex:instrument/SEM/part/BSE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "BSE Detector" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "missing" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/SE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SE Detector" ;
    schema1:name "missing" .


```


### semImagingTAPP example Izawa2010-3
semImagingTAPP instance derived from Izawa et al. 2010 | Tagish Lake (C2) meteorite | BSE Imaging (Leo 1540 FIB/SEM CrossBeam).
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
  "@id": "ex:semImagingTAPP-Izawa2010-3",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semImaging protocol — Izawa2010-3",
  "schema:description": "semImagingTAPP instance derived from Izawa et al. 2010 | Tagish Lake (C2) meteorite | BSE Imaging (Leo 1540 FIB/SEM CrossBeam) (publication column of SEM_Imaging_TAPP_v44.csv).",
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
        "schema:name": "example instrumentName"
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
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "BSE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/BSE-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "SE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/SE-Detector"
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
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:workingDistanceDefault": -9999
    }
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
        "schema:name": "EDS (same instrument); BSE Imaging (Leo 440); CL (Hitachi S-2500C); micro-XRD; EPMA (out of scope)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Region of interest — \"High-resolution BSE imaging ... carried out with the Leo 1540 FIB/SEM CrossBeam field emission SEM\" (p.3), used for \"higher resolution SEM-BSE mapping to document smaller scale relationships\" within \"polished thin sections\" of Tagish Lake (p.2)",
  "ada:analyticalMode": [
    "BSE Imaging"
  ],
  "ada:reportedProperties": [
    "textural relationships (nominal) — Textural relationships at higher resolution (nominal) — the stage is \"higher resolution SEM-BSE mapping to establish spatial context for textural variation\" (p.2), reporting mineralogy and texture rather than a magnitude"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "semImaging",
      "schema:termCode": "semImaging"
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
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
        "ada:ebsdIndexingMethod": "missing"
      }
    ]
  },
  "ada:clAcquisitionMode": "missing",
  "ada:clIntegrationTimeDefault": -9999,
  "ada:clWavelengthRange": -9999,
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:ebsdDetectorConfiguration": "missing",
  "ada:ebsdPhaseListDefault": "missing",
  "ada:ebsdStepSizeDefault": -9999,
  "ada:sampleTiltAngle": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Imaging/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semImagingTAPP-Izawa2010-3",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semImaging protocol \u2014 Izawa2010-3",
  "schema:description": "semImagingTAPP instance derived from Izawa et al. 2010 | Tagish Lake (C2) meteorite | BSE Imaging (Leo 1540 FIB/SEM CrossBeam) (publication column of SEM_Imaging_TAPP_v44.csv).",
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
        "schema:name": "example instrumentName"
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
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "BSE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/BSE-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "SE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/SE-Detector"
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
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:workingDistanceDefault": -9999
    }
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
        "schema:name": "EDS (same instrument); BSE Imaging (Leo 440); CL (Hitachi S-2500C); micro-XRD; EPMA (out of scope)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Region of interest \u2014 \"High-resolution BSE imaging ... carried out with the Leo 1540 FIB/SEM CrossBeam field emission SEM\" (p.3), used for \"higher resolution SEM-BSE mapping to document smaller scale relationships\" within \"polished thin sections\" of Tagish Lake (p.2)",
  "ada:analyticalMode": [
    "BSE Imaging"
  ],
  "ada:reportedProperties": [
    "textural relationships (nominal) \u2014 Textural relationships at higher resolution (nominal) \u2014 the stage is \"higher resolution SEM-BSE mapping to establish spatial context for textural variation\" (p.2), reporting mineralogy and texture rather than a magnitude"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "semImaging",
      "schema:termCode": "semImaging"
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
          {
            "@id": "bios:LabProcess"
          }
        ],
        "schema:position": 2,
        "ada:ebsdIndexingMethod": "missing"
      }
    ]
  },
  "ada:clAcquisitionMode": "missing",
  "ada:clIntegrationTimeDefault": -9999,
  "ada:clWavelengthRange": -9999,
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:ebsdDetectorConfiguration": "missing",
  "ada:ebsdPhaseListDefault": "missing",
  "ada:ebsdStepSizeDefault": -9999,
  "ada:sampleTiltAngle": -9999,
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

<ex:semImagingTAPP-Izawa2010-3> a cdi:Activity,
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
                    ada:ebsdIndexingMethod "missing" ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:description "missing" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "semImagingTAPP instance derived from Izawa et al. 2010 | Tagish Lake (C2) meteorite | BSE Imaging (Leo 1540 FIB/SEM CrossBeam) (publication column of SEM_Imaging_TAPP_v44.csv)." ;
    schema1:instrument <ex:instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Nanofabrication Laboratory, University of Western Ontario" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semImaging" ;
            schema1:termCode "semImaging" ] ;
    schema1:name "semImaging protocol — Izawa2010-3" ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "EDS (same instrument); BSE Imaging (Leo 440); CL (Hitachi S-2500C); micro-XRD; EPMA (out of scope)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "BSE Imaging" ;
    ada:clAcquisitionMode "missing" ;
    ada:clIntegrationTimeDefault -9999 ;
    ada:clWavelengthRange -9999 ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:ebsdDetectorConfiguration "missing" ;
    ada:ebsdPhaseListDefault "missing" ;
    ada:ebsdStepSizeDefault -9999 ;
    ada:reportedProperties "textural relationships (nominal) — Textural relationships at higher resolution (nominal) — the stage is \"higher resolution SEM-BSE mapping to establish spatial context for textural variation\" (p.2), reporting mineralogy and texture rather than a magnitude" ;
    ada:sampleTiltAngle -9999 ;
    ada:samplingUnitSelectionCriteriaDefault "Follow-up on features already located — this is the third stage of the paper's strategy, \"finally higher resolution SEM-BSE mapping to establish spatial context for textural variation\" (p.2), on features identified by the earlier μXRD and SEM-EDX/CL stages" ;
    ada:samplingUnitType "Region of interest — \"High-resolution BSE imaging ... carried out with the Leo 1540 FIB/SEM CrossBeam field emission SEM\" (p.3), used for \"higher resolution SEM-BSE mapping to document smaller scale relationships\" within \"polished thin sections\" of Tagish Lake (p.2)" ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "carbonaceous chondrite" ;
            ada:targetMaterialColumns [ schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ] ] .

<ex:instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:description "FIB-SEM dual-beam" ;
    schema1:hasPart <ex:instrument/SEM/part/BSE-Detector>,
        <ex:instrument/SEM/part/Electron-Source>,
        <ex:instrument/SEM/part/SE-Detector> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Zeiss" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Leo 1540 FIB/SEM CrossBeam" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault -9999 ;
    ada:mappingBeamCurrentDefault -9999 ;
    ada:workingDistanceDefault -9999 .

<ex:instrument/SEM/part/BSE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "BSE Detector" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Unknown" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/SE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SE Detector" ;
    schema1:name "missing" .


```


### semImagingTAPP example Liu2017
semImagingTAPP instance derived from Liu et al. 2017 | High-rank coal (Qinshui basin) | SE Imaging (ESEM Quanta 250).
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
  "@id": "ex:semImagingTAPP-Liu2017",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semImaging protocol — Liu2017",
  "schema:description": "Pore and mineral sizes >0.1 µm measured; minerals analyzed via EDS (surface energy spectrum analysis); magnification range 10³ to 10⁴",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "anthracite",
      "lean coal"
    ],
    "ada:targetMaterialColumns": [
      {
        "schema:valueName": "targetMaterial",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
        "schema:name": "example instrumentName"
      }
    ]
  },
  "ada:samplingUnitSelectionCriteriaDefault": "N — the selection stated is of samples, not units: \"Two highrank coals formed from regional metamorphism collected from the southern Qinshui basin were selected\" (p.1); no rule is given for the imaged areas",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "Unknown",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Quanta 250",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:description": "ESEM",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "BSE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/BSE-Detector"
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
            "SE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/SE-Detector"
        }
      ],
      "schema:name": "example instrumentName",
      "ada:acceleratingVoltageDefault": -9999,
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:workingDistanceDefault": -9999
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/semImagingTAPP/chamberPressureDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "chamberPressureDefault",
      "schema:name": "Chamber Pressure",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": "High vacuum"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "China University of Mining and Technology, Xuzhou, China"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "FIB-SEM (Crossbeam 540) for 3D tomography; EDS for mineral analysis"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Whole sample (polished coal block) > Phase (pore types) — \"Electron microscopy observations further revealed there are coalification-related pores and mineral-related pores in the high-rank coal\" (p.1), imaged on the polished coal blocks \"#1\" and \"#2\" (Table 1, p.2)",
  "ada:analyticalMode": [
    "SE Imaging"
  ],
  "ada:reportedProperties": [
    "pore type (nominal); pore morphology (nominal); pore size (nm) — Pore type and morphology (nominal: \"secondary gas pores in organic matter and shrinkage-induced pores around quartz and clay minerals\", \"dissolution-created pores and intercrystalline pores\", p.1), with pore sizes in nm"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Bulk coal polished to ~10 mm × 2-3 mm using polishing and burnishing machine; further polished with cross section polisher; thin gold coating applied by sputtering",
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
        "ada:ebsdIndexingMethod": "missing"
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
      "schema:name": "semImaging",
      "schema:termCode": "semImaging"
    }
  ],
  "ada:clAcquisitionMode": "missing",
  "ada:clIntegrationTimeDefault": -9999,
  "ada:clWavelengthRange": -9999,
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:ebsdDetectorConfiguration": "missing",
  "ada:ebsdPhaseListDefault": "missing",
  "ada:ebsdStepSizeDefault": -9999,
  "ada:sampleTiltAngle": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Imaging/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semImagingTAPP-Liu2017",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semImaging protocol \u2014 Liu2017",
  "schema:description": "Pore and mineral sizes >0.1 \u00b5m measured; minerals analyzed via EDS (surface energy spectrum analysis); magnification range 10\u00b3 to 10\u2074",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "anthracite",
      "lean coal"
    ],
    "ada:targetMaterialColumns": [
      {
        "schema:valueName": "targetMaterial",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
        "schema:name": "example instrumentName"
      }
    ]
  },
  "ada:samplingUnitSelectionCriteriaDefault": "N \u2014 the selection stated is of samples, not units: \"Two highrank coals formed from regional metamorphism collected from the southern Qinshui basin were selected\" (p.1); no rule is given for the imaged areas",
  "schema:instrument": [
    {
      "schema:additionalType": [
        "SEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:manufacturer": {
        "schema:name": "Unknown",
        "@type": [
          "schema:Organization"
        ]
      },
      "schema:model": {
        "schema:name": "Quanta 250",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:description": "ESEM",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "BSE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/BSE-Detector"
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
            "SE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/SE-Detector"
        }
      ],
      "schema:name": "example instrumentName",
      "ada:acceleratingVoltageDefault": -9999,
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:workingDistanceDefault": -9999
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/semImagingTAPP/chamberPressureDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "chamberPressureDefault",
      "schema:name": "Chamber Pressure",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": "High vacuum"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "China University of Mining and Technology, Xuzhou, China"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "FIB-SEM (Crossbeam 540) for 3D tomography; EDS for mineral analysis"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Whole sample (polished coal block) > Phase (pore types) \u2014 \"Electron microscopy observations further revealed there are coalification-related pores and mineral-related pores in the high-rank coal\" (p.1), imaged on the polished coal blocks \"#1\" and \"#2\" (Table 1, p.2)",
  "ada:analyticalMode": [
    "SE Imaging"
  ],
  "ada:reportedProperties": [
    "pore type (nominal); pore morphology (nominal); pore size (nm) \u2014 Pore type and morphology (nominal: \"secondary gas pores in organic matter and shrinkage-induced pores around quartz and clay minerals\", \"dissolution-created pores and intercrystalline pores\", p.1), with pore sizes in nm"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Bulk coal polished to ~10 mm \u00d7 2-3 mm using polishing and burnishing machine; further polished with cross section polisher; thin gold coating applied by sputtering",
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
        "ada:ebsdIndexingMethod": "missing"
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
      "schema:name": "semImaging",
      "schema:termCode": "semImaging"
    }
  ],
  "ada:clAcquisitionMode": "missing",
  "ada:clIntegrationTimeDefault": -9999,
  "ada:clWavelengthRange": -9999,
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:ebsdDetectorConfiguration": "missing",
  "ada:ebsdPhaseListDefault": "missing",
  "ada:ebsdStepSizeDefault": -9999,
  "ada:sampleTiltAngle": -9999,
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

<ex:semImagingTAPP-Liu2017> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:description "Bulk coal polished to ~10 mm × 2-3 mm using polishing and burnishing machine; further polished with cross section polisher; thin gold coating applied by sputtering" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:ebsdIndexingMethod "missing" ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semImagingTAPP/chamberPressureDefault> ;
    schema1:datePublished "missing" ;
    schema1:description "Pore and mineral sizes >0.1 µm measured; minerals analyzed via EDS (surface energy spectrum analysis); magnification range 10³ to 10⁴" ;
    schema1:instrument <ex:instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "China University of Mining and Technology, Xuzhou, China" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semImaging" ;
            schema1:termCode "semImaging" ] ;
    schema1:name "semImaging protocol — Liu2017" ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "FIB-SEM (Crossbeam 540) for 3D tomography; EDS for mineral analysis" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "SE Imaging" ;
    ada:clAcquisitionMode "missing" ;
    ada:clIntegrationTimeDefault -9999 ;
    ada:clWavelengthRange -9999 ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:ebsdDetectorConfiguration "missing" ;
    ada:ebsdPhaseListDefault "missing" ;
    ada:ebsdStepSizeDefault -9999 ;
    ada:reportedProperties "pore type (nominal); pore morphology (nominal); pore size (nm) — Pore type and morphology (nominal: \"secondary gas pores in organic matter and shrinkage-induced pores around quartz and clay minerals\", \"dissolution-created pores and intercrystalline pores\", p.1), with pore sizes in nm" ;
    ada:sampleTiltAngle -9999 ;
    ada:samplingUnitSelectionCriteriaDefault "N — the selection stated is of samples, not units: \"Two highrank coals formed from regional metamorphism collected from the southern Qinshui basin were selected\" (p.1); no rule is given for the imaged areas" ;
    ada:samplingUnitType "Whole sample (polished coal block) > Phase (pore types) — \"Electron microscopy observations further revealed there are coalification-related pores and mineral-related pores in the high-rank coal\" (p.1), imaged on the polished coal blocks \"#1\" and \"#2\" (Table 1, p.2)" ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "anthracite",
                "lean coal" ;
            ada:targetMaterialColumns [ schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ] ] .

<ex:instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:description "ESEM" ;
    schema1:hasPart <ex:instrument/SEM/part/BSE-Detector>,
        <ex:instrument/SEM/part/Electron-Source>,
        <ex:instrument/SEM/part/SE-Detector> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Unknown" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Quanta 250" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault -9999 ;
    ada:mappingBeamCurrentDefault -9999 ;
    ada:workingDistanceDefault -9999 .

<ex:instrument/SEM/part/BSE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "BSE Detector" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "missing" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/SE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SE Detector" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/semImagingTAPP/chamberPressureDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "High vacuum" ;
    schema1:name "Chamber Pressure" ;
    schema1:valueName "chamberPressureDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .


```


### semImagingTAPP example Liu2017-2
semImagingTAPP instance derived from Liu et al. 2017 | High-rank coal (Qinshui basin) | SE Imaging (FESEM SUPRA 55).
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
  "@id": "ex:semImagingTAPP-Liu2017-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semImaging protocol — Liu2017-2",
  "schema:description": "Pore and mineral sizes >20 nm to <5 µm measured; EDS also used for mineral analysis; magnification range 10³ to 10⁵",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "anthracite",
      "lean coal"
    ],
    "ada:targetMaterialColumns": [
      {
        "schema:valueName": "targetMaterial",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
        "schema:name": "example instrumentName"
      }
    ]
  },
  "ada:samplingUnitSelectionCriteriaDefault": "N — the selection stated is of samples, not units: \"Two highrank coals formed from regional metamorphism collected from the southern Qinshui basin were selected\" (p.1); no rule is given for the imaged areas",
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
        "schema:name": "SUPRA 55",
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
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "BSE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/BSE-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "SE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/SE-Detector"
        }
      ],
      "schema:description": "ESEM",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName",
      "ada:acceleratingVoltageDefault": -9999,
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:workingDistanceDefault": -9999
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/semImagingTAPP/chamberPressureDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "chamberPressureDefault",
      "schema:name": "Chamber Pressure",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": "High vacuum"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "China University of Mining and Technology, Xuzhou, China"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "FIB-SEM (Crossbeam 540) for 3D tomography; EDS for mineral analysis"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Whole sample (polished coal block) > Phase (pore types) — higher-resolution imaging of the same pore types (p.1) on the polished coal blocks \"#1\" and \"#2\" (Table 1, p.2)",
  "ada:analyticalMode": [
    "SE Imaging"
  ],
  "ada:reportedProperties": [
    "pore type (nominal); pore morphology (nominal); pore size (nm) — Pore type and morphology at higher resolution (nominal), with pore sizes in nm — \"the shrinkage-induced pores are mainly mesopores\" (p.1)"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Bulk coal polished to ~10 mm × 2-3 mm using polishing and burnishing machine; further polished with cross section polisher; thin gold coating applied by sputtering",
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
        "ada:ebsdIndexingMethod": "missing"
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
      "schema:name": "semImaging",
      "schema:termCode": "semImaging"
    }
  ],
  "ada:clAcquisitionMode": "missing",
  "ada:clIntegrationTimeDefault": -9999,
  "ada:clWavelengthRange": -9999,
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:ebsdDetectorConfiguration": "missing",
  "ada:ebsdPhaseListDefault": "missing",
  "ada:ebsdStepSizeDefault": -9999,
  "ada:sampleTiltAngle": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Imaging/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semImagingTAPP-Liu2017-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semImaging protocol \u2014 Liu2017-2",
  "schema:description": "Pore and mineral sizes >20 nm to <5 \u00b5m measured; EDS also used for mineral analysis; magnification range 10\u00b3 to 10\u2075",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "anthracite",
      "lean coal"
    ],
    "ada:targetMaterialColumns": [
      {
        "schema:valueName": "targetMaterial",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
        "schema:name": "example instrumentName"
      }
    ]
  },
  "ada:samplingUnitSelectionCriteriaDefault": "N \u2014 the selection stated is of samples, not units: \"Two highrank coals formed from regional metamorphism collected from the southern Qinshui basin were selected\" (p.1); no rule is given for the imaged areas",
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
        "schema:name": "SUPRA 55",
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
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "BSE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/BSE-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "SE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/SE-Detector"
        }
      ],
      "schema:description": "ESEM",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName",
      "ada:acceleratingVoltageDefault": -9999,
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:workingDistanceDefault": -9999
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/semImagingTAPP/chamberPressureDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "chamberPressureDefault",
      "schema:name": "Chamber Pressure",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": "High vacuum"
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "China University of Mining and Technology, Xuzhou, China"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "FIB-SEM (Crossbeam 540) for 3D tomography; EDS for mineral analysis"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Whole sample (polished coal block) > Phase (pore types) \u2014 higher-resolution imaging of the same pore types (p.1) on the polished coal blocks \"#1\" and \"#2\" (Table 1, p.2)",
  "ada:analyticalMode": [
    "SE Imaging"
  ],
  "ada:reportedProperties": [
    "pore type (nominal); pore morphology (nominal); pore size (nm) \u2014 Pore type and morphology at higher resolution (nominal), with pore sizes in nm \u2014 \"the shrinkage-induced pores are mainly mesopores\" (p.1)"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Bulk coal polished to ~10 mm \u00d7 2-3 mm using polishing and burnishing machine; further polished with cross section polisher; thin gold coating applied by sputtering",
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
        "ada:ebsdIndexingMethod": "missing"
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
      "schema:name": "semImaging",
      "schema:termCode": "semImaging"
    }
  ],
  "ada:clAcquisitionMode": "missing",
  "ada:clIntegrationTimeDefault": -9999,
  "ada:clWavelengthRange": -9999,
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:ebsdDetectorConfiguration": "missing",
  "ada:ebsdPhaseListDefault": "missing",
  "ada:ebsdStepSizeDefault": -9999,
  "ada:sampleTiltAngle": -9999,
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

<ex:semImagingTAPP-Liu2017-2> a cdi:Activity,
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
                    ada:ebsdIndexingMethod "missing" ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:description "Bulk coal polished to ~10 mm × 2-3 mm using polishing and burnishing machine; further polished with cross section polisher; thin gold coating applied by sputtering" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semImagingTAPP/chamberPressureDefault> ;
    schema1:datePublished "missing" ;
    schema1:description "Pore and mineral sizes >20 nm to <5 µm measured; EDS also used for mineral analysis; magnification range 10³ to 10⁵" ;
    schema1:instrument <ex:instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "China University of Mining and Technology, Xuzhou, China" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semImaging" ;
            schema1:termCode "semImaging" ] ;
    schema1:name "semImaging protocol — Liu2017-2" ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "FIB-SEM (Crossbeam 540) for 3D tomography; EDS for mineral analysis" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "SE Imaging" ;
    ada:clAcquisitionMode "missing" ;
    ada:clIntegrationTimeDefault -9999 ;
    ada:clWavelengthRange -9999 ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:ebsdDetectorConfiguration "missing" ;
    ada:ebsdPhaseListDefault "missing" ;
    ada:ebsdStepSizeDefault -9999 ;
    ada:reportedProperties "pore type (nominal); pore morphology (nominal); pore size (nm) — Pore type and morphology at higher resolution (nominal), with pore sizes in nm — \"the shrinkage-induced pores are mainly mesopores\" (p.1)" ;
    ada:sampleTiltAngle -9999 ;
    ada:samplingUnitSelectionCriteriaDefault "N — the selection stated is of samples, not units: \"Two highrank coals formed from regional metamorphism collected from the southern Qinshui basin were selected\" (p.1); no rule is given for the imaged areas" ;
    ada:samplingUnitType "Whole sample (polished coal block) > Phase (pore types) — higher-resolution imaging of the same pore types (p.1) on the polished coal blocks \"#1\" and \"#2\" (Table 1, p.2)" ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "anthracite",
                "lean coal" ;
            ada:targetMaterialColumns [ schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ] ] .

<ex:instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:description "ESEM" ;
    schema1:hasPart <ex:instrument/SEM/part/BSE-Detector>,
        <ex:instrument/SEM/part/Electron-Source>,
        <ex:instrument/SEM/part/SE-Detector> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Zeiss" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "SUPRA 55" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault -9999 ;
    ada:mappingBeamCurrentDefault -9999 ;
    ada:workingDistanceDefault -9999 .

<ex:instrument/SEM/part/BSE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "BSE Detector" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Field emission gun (FEG) — subtype not specified" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/SE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SE Detector" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/semImagingTAPP/chamberPressureDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "High vacuum" ;
    schema1:name "Chamber Pressure" ;
    schema1:valueName "chamberPressureDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .


```


### semImagingTAPP example Ma2017
semImagingTAPP instance derived from Ma et al. 2017 | Khatyrka CV3 chondrite (metal phases) | BSE Imaging (ZEISS 1550VP FE-SEM).
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
  "@id": "ex:semImagingTAPP-Ma2017",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semImaging protocol — Ma2017",
  "schema:description": "BSE images obtained from both ZEISS 1550VP FE-SEM and JEOL 8200 electron microprobe (EPMA); quantitative EPMA on JEOL 8200 at 12 kV, 5 nA (out of scope for SEM TAPP)",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "hollisterite",
      "kryachkoite",
      "stolperite",
      "khatyrkite",
      "icosahedrite"
    ],
    "ada:targetMaterialColumns": [
      {
        "schema:valueName": "targetMaterial",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
        "schema:name": "example instrumentName"
      }
    ]
  },
  "ada:samplingUnitSelectionCriteriaDefault": "N — the imaged occurrences are shown rather than chosen by a stated rule; the three mineral locations are \"marked by rectangles\" in Fig. 1 (p.2) within \"section 126A of USNM 7908\" (p.1)",
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
        "schema:name": "1550VP",
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
            "BSE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "N/A",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/SEM/part/BSE-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "SE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/SE-Detector"
        }
      ],
      "schema:description": "N/A",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName",
      "ada:acceleratingVoltageDefault": -9999,
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:workingDistanceDefault": -9999
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Caltech GPS Analytical Facility, California Institute of Technology, Pasadena, CA, USA"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "EBSD (ZEISS 1550VP FE-SEM); EPMA (JEOL 8200, separate instrument)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Whole sample (section 126A) > Phase — the SEM was used \"to characterize chemical compositions and structures of minerals in section 126A\" (p.1); the metal assemblages are shown as whole-section context (Fig. 2, p.3)",
  "ada:analyticalMode": [
    "BSE Imaging"
  ],
  "ada:reportedProperties": [
    "textural relationships (nominal); phase assemblage (nominal); grain size (µm) — Textural relationships and phase assemblage (nominal) — the imaging documents the metal assemblage in which the new minerals occur, with grain sizes in µm (Fig. 2, p.3)"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished thin section (section 126A prepared from Grain 126); no coating or SEM-specific preparation stated",
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
        "ada:ebsdIndexingMethod": "missing"
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
      "schema:name": "semImaging",
      "schema:termCode": "semImaging"
    }
  ],
  "ada:clAcquisitionMode": "missing",
  "ada:clIntegrationTimeDefault": -9999,
  "ada:clWavelengthRange": -9999,
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:ebsdDetectorConfiguration": "missing",
  "ada:ebsdPhaseListDefault": "missing",
  "ada:ebsdStepSizeDefault": -9999,
  "ada:sampleTiltAngle": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Imaging/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semImagingTAPP-Ma2017",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semImaging protocol \u2014 Ma2017",
  "schema:description": "BSE images obtained from both ZEISS 1550VP FE-SEM and JEOL 8200 electron microprobe (EPMA); quantitative EPMA on JEOL 8200 at 12 kV, 5 nA (out of scope for SEM TAPP)",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "hollisterite",
      "kryachkoite",
      "stolperite",
      "khatyrkite",
      "icosahedrite"
    ],
    "ada:targetMaterialColumns": [
      {
        "schema:valueName": "targetMaterial",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
        "schema:name": "example instrumentName"
      }
    ]
  },
  "ada:samplingUnitSelectionCriteriaDefault": "N \u2014 the imaged occurrences are shown rather than chosen by a stated rule; the three mineral locations are \"marked by rectangles\" in Fig. 1 (p.2) within \"section 126A of USNM 7908\" (p.1)",
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
        "schema:name": "1550VP",
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
            "BSE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "N/A",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/SEM/part/BSE-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "SE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/SE-Detector"
        }
      ],
      "schema:description": "N/A",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName",
      "ada:acceleratingVoltageDefault": -9999,
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:workingDistanceDefault": -9999
    }
  ],
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Caltech GPS Analytical Facility, California Institute of Technology, Pasadena, CA, USA"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "EBSD (ZEISS 1550VP FE-SEM); EPMA (JEOL 8200, separate instrument)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Whole sample (section 126A) > Phase \u2014 the SEM was used \"to characterize chemical compositions and structures of minerals in section 126A\" (p.1); the metal assemblages are shown as whole-section context (Fig. 2, p.3)",
  "ada:analyticalMode": [
    "BSE Imaging"
  ],
  "ada:reportedProperties": [
    "textural relationships (nominal); phase assemblage (nominal); grain size (\u00b5m) \u2014 Textural relationships and phase assemblage (nominal) \u2014 the imaging documents the metal assemblage in which the new minerals occur, with grain sizes in \u00b5m (Fig. 2, p.3)"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished thin section (section 126A prepared from Grain 126); no coating or SEM-specific preparation stated",
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
        "ada:ebsdIndexingMethod": "missing"
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
      "schema:name": "semImaging",
      "schema:termCode": "semImaging"
    }
  ],
  "ada:clAcquisitionMode": "missing",
  "ada:clIntegrationTimeDefault": -9999,
  "ada:clWavelengthRange": -9999,
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:ebsdDetectorConfiguration": "missing",
  "ada:ebsdPhaseListDefault": "missing",
  "ada:ebsdStepSizeDefault": -9999,
  "ada:sampleTiltAngle": -9999,
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

<ex:semImagingTAPP-Ma2017> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:description "Polished thin section (section 126A prepared from Grain 126); no coating or SEM-specific preparation stated" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:ebsdIndexingMethod "missing" ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "BSE images obtained from both ZEISS 1550VP FE-SEM and JEOL 8200 electron microprobe (EPMA); quantitative EPMA on JEOL 8200 at 12 kV, 5 nA (out of scope for SEM TAPP)" ;
    schema1:instrument <ex:instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Caltech GPS Analytical Facility, California Institute of Technology, Pasadena, CA, USA" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semImaging" ;
            schema1:termCode "semImaging" ] ;
    schema1:name "semImaging protocol — Ma2017" ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "EBSD (ZEISS 1550VP FE-SEM); EPMA (JEOL 8200, separate instrument)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "BSE Imaging" ;
    ada:clAcquisitionMode "missing" ;
    ada:clIntegrationTimeDefault -9999 ;
    ada:clWavelengthRange -9999 ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:ebsdDetectorConfiguration "missing" ;
    ada:ebsdPhaseListDefault "missing" ;
    ada:ebsdStepSizeDefault -9999 ;
    ada:reportedProperties "textural relationships (nominal); phase assemblage (nominal); grain size (µm) — Textural relationships and phase assemblage (nominal) — the imaging documents the metal assemblage in which the new minerals occur, with grain sizes in µm (Fig. 2, p.3)" ;
    ada:sampleTiltAngle -9999 ;
    ada:samplingUnitSelectionCriteriaDefault "N — the imaged occurrences are shown rather than chosen by a stated rule; the three mineral locations are \"marked by rectangles\" in Fig. 1 (p.2) within \"section 126A of USNM 7908\" (p.1)" ;
    ada:samplingUnitType "Whole sample (section 126A) > Phase — the SEM was used \"to characterize chemical compositions and structures of minerals in section 126A\" (p.1); the metal assemblages are shown as whole-section context (Fig. 2, p.3)" ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "hollisterite",
                "icosahedrite",
                "khatyrkite",
                "kryachkoite",
                "stolperite" ;
            ada:targetMaterialColumns [ schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ] ] .

<ex:instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:description "N/A" ;
    schema1:hasPart <ex:instrument/SEM/part/BSE-Detector>,
        <ex:instrument/SEM/part/Electron-Source>,
        <ex:instrument/SEM/part/SE-Detector> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Zeiss" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "1550VP" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault -9999 ;
    ada:mappingBeamCurrentDefault -9999 ;
    ada:workingDistanceDefault -9999 .

<ex:instrument/SEM/part/BSE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "BSE Detector" ;
    schema1:name "N/A" .

<ex:instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Field emission gun (FEG) — subtype not specified" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/SE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SE Detector" ;
    schema1:name "missing" .


```


### semImagingTAPP example Ma2017-2
semImagingTAPP instance derived from Ma et al. 2017 | Khatyrka CV3 chondrite (metal phases) | EBSD (ZEISS 1550VP FE-SEM, HKL system, 20 kV).
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
  "@id": "ex:semImagingTAPP-Ma2017-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semImaging protocol — Ma2017-2",
  "schema:description": "EBSD performed at Caltech GPS Analytical Facility; EPMA (JEOL 8200) used for quantitative chemical analysis (out of scope for SEM TAPP)",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "hollisterite",
      "kryachkoite",
      "stolperite",
      "khatyrkite",
      "icosahedrite"
    ],
    "ada:targetMaterialColumns": [
      {
        "schema:valueName": "targetMaterial",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
        "schema:name": "example instrumentName"
      }
    ]
  },
  "ada:samplingUnitSelectionCriteriaDefault": "N — no rule is given for choosing which crystals were indexed; the patterns are reported for the type and associated crystals as they occur (Fig. 3, p.3)",
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
        "schema:name": "1550VP",
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
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "BSE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/BSE-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "SE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/SE-Detector"
        }
      ],
      "schema:description": "N/A",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName",
      "ada:acceleratingVoltageDefault": -9999,
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:workingDistanceDefault": -9999
    }
  ],
  "ada:ebsdPhaseListDefault": "Hollisterite (C2/m FeAl3); kryachkoite (Cmc21 (Al,Cu)Fe6); stolperite (Pm3m AlCu)",
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished thin section (section 126A prepared from Grain 126); no coating or EBSD-specific preparation stated",
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
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/semImagingTAPP/crystalStructureDatabaseDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "crystalStructureDatabaseDefault",
            "schema:name": "Crystal Structure Database",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Literature crystal structures: Black et al. 1961 (Cmc21 (Al,Cu)Fe6 for kryachkoite); Zhang et al. 2005 (Pm3m AlCu for stolperite)"
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
        "ada:ebsdIndexingMethod": "missing"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Caltech GPS Analytical Facility, California Institute of Technology, Pasadena, CA, USA"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "BSE Imaging (ZEISS 1550VP FE-SEM); EPMA (JEOL 8200, separate instrument)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Grain (single crystal) — one pattern per crystal, \"EBSD patterns of (a) the type hollisterite crystal, indexed with the C2/m Fe3Al structure\" (Fig. 3, p.3), each returning that crystal's cell parameters (p.3)",
  "ada:analyticalMode": [
    "EBSD"
  ],
  "ada:reportedProperties": [
    "crystal structure identification (nominal); unit-cell parameters (Å, Å3); mean angular deviation (degrees) — Crystal structure identification with unit-cell parameters (Å and Å3) and the fit quality as mean angular deviation (degrees) — e.g. \"with a mean angular deviation of 0.30°~0.45°, revealing the cell parameters: a = 15.60 Å, b = 7.94 Å, c = 12.51 Å\" and cell volume (p.3)"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "semImaging",
      "schema:termCode": "semImaging"
    }
  ],
  "ada:clAcquisitionMode": "missing",
  "ada:clIntegrationTimeDefault": -9999,
  "ada:clWavelengthRange": -9999,
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:ebsdDetectorConfiguration": "missing",
  "ada:ebsdStepSizeDefault": -9999,
  "ada:sampleTiltAngle": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Imaging/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semImagingTAPP-Ma2017-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semImaging protocol \u2014 Ma2017-2",
  "schema:description": "EBSD performed at Caltech GPS Analytical Facility; EPMA (JEOL 8200) used for quantitative chemical analysis (out of scope for SEM TAPP)",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "hollisterite",
      "kryachkoite",
      "stolperite",
      "khatyrkite",
      "icosahedrite"
    ],
    "ada:targetMaterialColumns": [
      {
        "schema:valueName": "targetMaterial",
        "ada:dataType": "string",
        "schema:readonlyValue": true,
        "schema:valueRequired": true,
        "ada:tier": "M",
        "ada:cdifPropertyPath": "#/schema:variableMeasured/schema:name",
        "schema:name": "example instrumentName"
      }
    ]
  },
  "ada:samplingUnitSelectionCriteriaDefault": "N \u2014 no rule is given for choosing which crystals were indexed; the patterns are reported for the type and associated crystals as they occur (Fig. 3, p.3)",
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
        "schema:name": "1550VP",
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
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "BSE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/BSE-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "SE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/SE-Detector"
        }
      ],
      "schema:description": "N/A",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName",
      "ada:acceleratingVoltageDefault": -9999,
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:workingDistanceDefault": -9999
    }
  ],
  "ada:ebsdPhaseListDefault": "Hollisterite (C2/m FeAl3); kryachkoite (Cmc21 (Al,Cu)Fe6); stolperite (Pm3m AlCu)",
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished thin section (section 126A prepared from Grain 126); no coating or EBSD-specific preparation stated",
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
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/semImagingTAPP/crystalStructureDatabaseDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "crystalStructureDatabaseDefault",
            "schema:name": "Crystal Structure Database",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Literature crystal structures: Black et al. 1961 (Cmc21 (Al,Cu)Fe6 for kryachkoite); Zhang et al. 2005 (Pm3m AlCu for stolperite)"
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
        "ada:ebsdIndexingMethod": "missing"
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Caltech GPS Analytical Facility, California Institute of Technology, Pasadena, CA, USA"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "BSE Imaging (ZEISS 1550VP FE-SEM); EPMA (JEOL 8200, separate instrument)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Grain (single crystal) \u2014 one pattern per crystal, \"EBSD patterns of (a) the type hollisterite crystal, indexed with the C2/m Fe3Al structure\" (Fig. 3, p.3), each returning that crystal's cell parameters (p.3)",
  "ada:analyticalMode": [
    "EBSD"
  ],
  "ada:reportedProperties": [
    "crystal structure identification (nominal); unit-cell parameters (\u00c5, \u00c53); mean angular deviation (degrees) \u2014 Crystal structure identification with unit-cell parameters (\u00c5 and \u00c53) and the fit quality as mean angular deviation (degrees) \u2014 e.g. \"with a mean angular deviation of 0.30\u00b0~0.45\u00b0, revealing the cell parameters: a = 15.60 \u00c5, b = 7.94 \u00c5, c = 12.51 \u00c5\" and cell volume (p.3)"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "semImaging",
      "schema:termCode": "semImaging"
    }
  ],
  "ada:clAcquisitionMode": "missing",
  "ada:clIntegrationTimeDefault": -9999,
  "ada:clWavelengthRange": -9999,
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:ebsdDetectorConfiguration": "missing",
  "ada:ebsdStepSizeDefault": -9999,
  "ada:sampleTiltAngle": -9999,
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

<ex:semImagingTAPP-Ma2017-2> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semImagingTAPP/crystalStructureDatabaseDefault> ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:ebsdIndexingMethod "missing" ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:description "Polished thin section (section 126A prepared from Grain 126); no coating or EBSD-specific preparation stated" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "EBSD performed at Caltech GPS Analytical Facility; EPMA (JEOL 8200) used for quantitative chemical analysis (out of scope for SEM TAPP)" ;
    schema1:instrument <ex:instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Caltech GPS Analytical Facility, California Institute of Technology, Pasadena, CA, USA" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semImaging" ;
            schema1:termCode "semImaging" ] ;
    schema1:name "semImaging protocol — Ma2017-2" ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "BSE Imaging (ZEISS 1550VP FE-SEM); EPMA (JEOL 8200, separate instrument)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "EBSD" ;
    ada:clAcquisitionMode "missing" ;
    ada:clIntegrationTimeDefault -9999 ;
    ada:clWavelengthRange -9999 ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:ebsdDetectorConfiguration "missing" ;
    ada:ebsdPhaseListDefault "Hollisterite (C2/m FeAl3); kryachkoite (Cmc21 (Al,Cu)Fe6); stolperite (Pm3m AlCu)" ;
    ada:ebsdStepSizeDefault -9999 ;
    ada:reportedProperties "crystal structure identification (nominal); unit-cell parameters (Å, Å3); mean angular deviation (degrees) — Crystal structure identification with unit-cell parameters (Å and Å3) and the fit quality as mean angular deviation (degrees) — e.g. \"with a mean angular deviation of 0.30°~0.45°, revealing the cell parameters: a = 15.60 Å, b = 7.94 Å, c = 12.51 Å\" and cell volume (p.3)" ;
    ada:sampleTiltAngle -9999 ;
    ada:samplingUnitSelectionCriteriaDefault "N — no rule is given for choosing which crystals were indexed; the patterns are reported for the type and associated crystals as they occur (Fig. 3, p.3)" ;
    ada:samplingUnitType "Grain (single crystal) — one pattern per crystal, \"EBSD patterns of (a) the type hollisterite crystal, indexed with the C2/m Fe3Al structure\" (Fig. 3, p.3), each returning that crystal's cell parameters (p.3)" ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "hollisterite",
                "icosahedrite",
                "khatyrkite",
                "kryachkoite",
                "stolperite" ;
            ada:targetMaterialColumns [ schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ] ] .

<ex:instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:description "N/A" ;
    schema1:hasPart <ex:instrument/SEM/part/BSE-Detector>,
        <ex:instrument/SEM/part/Electron-Source>,
        <ex:instrument/SEM/part/SE-Detector> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Zeiss" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "1550VP" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault -9999 ;
    ada:mappingBeamCurrentDefault -9999 ;
    ada:workingDistanceDefault -9999 .

<ex:instrument/SEM/part/BSE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "BSE Detector" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Field emission gun (FEG) — subtype not specified" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/SE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SE Detector" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/semImagingTAPP/crystalStructureDatabaseDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Literature crystal structures: Black et al. 1961 (Cmc21 (Al,Cu)Fe6 for kryachkoite); Zhang et al. 2005 (Pm3m AlCu for stolperite)" ;
    schema1:name "Crystal Structure Database" ;
    schema1:valueName "crystalStructureDatabaseDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .


```


### semImagingTAPP example Pascucci2026
semImagingTAPP instance derived from Pascucci et al. 2026 | NWA 7317 CR6 chondrite | BSE Imaging (Zeiss Supra 40 FE-SEM, 20 kV).
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
  "@id": "ex:semImagingTAPP-Pascucci2026",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semImaging protocol — Pascucci2026",
  "schema:description": "10 BSE images acquired at ×138 magnification and mosaicked (4 consecutive per row) to cover ~9.7 mm area matching SPIM imagery",
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
        "schema:name": "example instrumentName"
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
            "BSE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "N/A",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/SEM/part/BSE-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "SE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/SE-Detector"
        }
      ],
      "schema:description": "ESEM",
      "ada:acceleratingVoltageDefault": "20 kV",
      "ada:workingDistanceDefault": "8 mm",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName",
      "ada:mappingBeamCurrentDefault": -9999
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/semImagingTAPP/chamberPressureDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "chamberPressureDefault",
      "schema:name": "Chamber Pressure",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": "High vacuum"
    }
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
        "schema:name": "EDS (Zeiss Supra 40 FE-SEM); SE Imaging (Zeiss Supra 40 FE-SEM); EMPA-WDS (JEOL JXA-8230, separate instrument); VIS-IR spectroscopy (SPIM)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Whole sample (polished slab) > Phase — BSE images \"were used at high vacuum mode at 20.00 kV accelerating voltage\" (p.3) on the \"NWA 7317 slab\", a \"small fragment of about 10 × 6 mm\" embedded in epoxy and polished (pp.3–4)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "acquisition",
      "schema:name": "Oxford INCA Energy"
    }
  ],
  "ada:analyticalMode": [
    "BSE Imaging"
  ],
  "ada:reportedProperties": [
    "texture (nominal); phase distribution (nominal) — Textures and phase distribution across the slab (nominal), imaged at 20.00 kV and mosaicked into 10 BSE images covering the SPIM area (p.3)"
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
        "ada:ebsdIndexingMethod": "missing"
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
      "schema:name": "semImaging",
      "schema:termCode": "semImaging"
    }
  ],
  "ada:clAcquisitionMode": "missing",
  "ada:clIntegrationTimeDefault": -9999,
  "ada:clWavelengthRange": -9999,
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:ebsdDetectorConfiguration": "missing",
  "ada:ebsdPhaseListDefault": "missing",
  "ada:ebsdStepSizeDefault": -9999,
  "ada:sampleTiltAngle": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Imaging/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semImagingTAPP-Pascucci2026",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semImaging protocol \u2014 Pascucci2026",
  "schema:description": "10 BSE images acquired at \u00d7138 magnification and mosaicked (4 consecutive per row) to cover ~9.7 mm area matching SPIM imagery",
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
        "schema:name": "example instrumentName"
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
            "BSE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "N/A",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/SEM/part/BSE-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "SE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/SE-Detector"
        }
      ],
      "schema:description": "ESEM",
      "ada:acceleratingVoltageDefault": "20 kV",
      "ada:workingDistanceDefault": "8 mm",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName",
      "ada:mappingBeamCurrentDefault": -9999
    }
  ],
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/semImagingTAPP/chamberPressureDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "chamberPressureDefault",
      "schema:name": "Chamber Pressure",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": "High vacuum"
    }
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
        "schema:name": "EDS (Zeiss Supra 40 FE-SEM); SE Imaging (Zeiss Supra 40 FE-SEM); EMPA-WDS (JEOL JXA-8230, separate instrument); VIS-IR spectroscopy (SPIM)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Whole sample (polished slab) > Phase \u2014 BSE images \"were used at high vacuum mode at 20.00 kV accelerating voltage\" (p.3) on the \"NWA 7317 slab\", a \"small fragment of about 10 \u00d7 6 mm\" embedded in epoxy and polished (pp.3\u20134)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "acquisition",
      "schema:name": "Oxford INCA Energy"
    }
  ],
  "ada:analyticalMode": [
    "BSE Imaging"
  ],
  "ada:reportedProperties": [
    "texture (nominal); phase distribution (nominal) \u2014 Textures and phase distribution across the slab (nominal), imaged at 20.00 kV and mosaicked into 10 BSE images covering the SPIM area (p.3)"
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
        "ada:ebsdIndexingMethod": "missing"
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
      "schema:name": "semImaging",
      "schema:termCode": "semImaging"
    }
  ],
  "ada:clAcquisitionMode": "missing",
  "ada:clIntegrationTimeDefault": -9999,
  "ada:clWavelengthRange": -9999,
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:ebsdDetectorConfiguration": "missing",
  "ada:ebsdPhaseListDefault": "missing",
  "ada:ebsdStepSizeDefault": -9999,
  "ada:sampleTiltAngle": -9999,
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

<ex:semImagingTAPP-Pascucci2026> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:description "Embedded in epoxy, polished to ¼ µm level, sputtered with 30-nm-thick carbon film" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:ebsdIndexingMethod "missing" ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semImagingTAPP/chamberPressureDefault> ;
    schema1:datePublished "missing" ;
    schema1:description "10 BSE images acquired at ×138 magnification and mosaicked (4 consecutive per row) to cover ~9.7 mm area matching SPIM imagery" ;
    schema1:instrument <ex:instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "CNR IMAA (Institute of Methodologies for Environmental Analysis), Italian National Research Council, Potenza, Italy" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semImaging" ;
            schema1:termCode "semImaging" ] ;
    schema1:name "semImaging protocol — Pascucci2026" ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "EDS (Zeiss Supra 40 FE-SEM); SE Imaging (Zeiss Supra 40 FE-SEM); EMPA-WDS (JEOL JXA-8230, separate instrument); VIS-IR spectroscopy (SPIM)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "BSE Imaging" ;
    ada:clAcquisitionMode "missing" ;
    ada:clIntegrationTimeDefault -9999 ;
    ada:clWavelengthRange -9999 ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:ebsdDetectorConfiguration "missing" ;
    ada:ebsdPhaseListDefault "missing" ;
    ada:ebsdStepSizeDefault -9999 ;
    ada:reportedProperties "texture (nominal); phase distribution (nominal) — Textures and phase distribution across the slab (nominal), imaged at 20.00 kV and mosaicked into 10 BSE images covering the SPIM area (p.3)" ;
    ada:sampleTiltAngle -9999 ;
    ada:samplingUnitSelectionCriteriaDefault "Spatial co-registration with the spectral imagery — the SEM work targets \"almost the same portion of the VIS-IR SPIM images\" (p.4), so that the two datasets can be compared on the same area of the slab" ;
    ada:samplingUnitType "Whole sample (polished slab) > Phase — BSE images \"were used at high vacuum mode at 20.00 kV accelerating voltage\" (p.3) on the \"NWA 7317 slab\", a \"small fragment of about 10 × 6 mm\" embedded in epoxy and polished (pp.3–4)" ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "carbonaceous chondrite" ;
            ada:targetMaterialColumns [ schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ] ] ;
    bios:computationalTool [ schema1:name "Oxford INCA Energy" ;
            ada:toolRole "acquisition" ] .

<ex:instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:description "ESEM" ;
    schema1:hasPart <ex:instrument/SEM/part/BSE-Detector>,
        <ex:instrument/SEM/part/Electron-Source>,
        <ex:instrument/SEM/part/SE-Detector> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Zeiss" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Supra 40" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "20 kV" ;
    ada:mappingBeamCurrentDefault -9999 ;
    ada:workingDistanceDefault "8 mm" .

<ex:instrument/SEM/part/BSE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "BSE Detector" ;
    schema1:name "N/A" .

<ex:instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Field emission gun (FEG) — subtype not specified" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/SE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SE Detector" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/semImagingTAPP/chamberPressureDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "High vacuum" ;
    schema1:name "Chamber Pressure" ;
    schema1:valueName "chamberPressureDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .


```


### semImagingTAPP example Pascucci2026-2
semImagingTAPP instance derived from Pascucci et al. 2026 | NWA 7317 CR6 chondrite | SE Imaging (Zeiss Supra 40 FE-SEM).
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
  "@id": "ex:semImagingTAPP-Pascucci2026-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semImaging protocol — Pascucci2026-2",
  "schema:description": "SE imaging used for topographic examination; instrument capability: up to ×200,000 magnification, 5 nm resolution; SE acquired before EDS to minimize charging effects",
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
        "schema:name": "example instrumentName"
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
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "BSE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/BSE-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "SE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/SE-Detector"
        }
      ],
      "schema:description": "ESEM",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName",
      "ada:acceleratingVoltageDefault": -9999,
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:workingDistanceDefault": -9999
    }
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
        "schema:name": "BSE Imaging (Zeiss Supra 40 FE-SEM); EDS (Zeiss Supra 40 FE-SEM); EMPA-WDS (JEOL JXA-8230, separate instrument); VIS-IR spectroscopy (SPIM)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Whole sample (polished slab) > Region of interest — \"Secondary electrons were used to construct images enlarged up to ×200,000 and resolved up to 5 nm\" (p.3) on the \"NWA 7317 slab\", a \"small fragment of about 10 × 6 mm\" embedded in epoxy and polished (pp.3–4)",
  "ada:analyticalMode": [
    "SE Imaging"
  ],
  "ada:reportedProperties": [
    "surface topography (nominal); texture (nominal) — Surface topography and texture (nominal), imaged \"enlarged up to ×200,000 and resolved up to 5 nm\" (p.3)"
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
        "ada:ebsdIndexingMethod": "missing"
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
      "schema:name": "semImaging",
      "schema:termCode": "semImaging"
    }
  ],
  "ada:clAcquisitionMode": "missing",
  "ada:clIntegrationTimeDefault": -9999,
  "ada:clWavelengthRange": -9999,
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:ebsdDetectorConfiguration": "missing",
  "ada:ebsdPhaseListDefault": "missing",
  "ada:ebsdStepSizeDefault": -9999,
  "ada:sampleTiltAngle": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Imaging/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semImagingTAPP-Pascucci2026-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semImaging protocol \u2014 Pascucci2026-2",
  "schema:description": "SE imaging used for topographic examination; instrument capability: up to \u00d7200,000 magnification, 5 nm resolution; SE acquired before EDS to minimize charging effects",
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
        "schema:name": "example instrumentName"
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
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "BSE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/BSE-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "SE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/SE-Detector"
        }
      ],
      "schema:description": "ESEM",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName",
      "ada:acceleratingVoltageDefault": -9999,
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:workingDistanceDefault": -9999
    }
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
        "schema:name": "BSE Imaging (Zeiss Supra 40 FE-SEM); EDS (Zeiss Supra 40 FE-SEM); EMPA-WDS (JEOL JXA-8230, separate instrument); VIS-IR spectroscopy (SPIM)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Whole sample (polished slab) > Region of interest \u2014 \"Secondary electrons were used to construct images enlarged up to \u00d7200,000 and resolved up to 5 nm\" (p.3) on the \"NWA 7317 slab\", a \"small fragment of about 10 \u00d7 6 mm\" embedded in epoxy and polished (pp.3\u20134)",
  "ada:analyticalMode": [
    "SE Imaging"
  ],
  "ada:reportedProperties": [
    "surface topography (nominal); texture (nominal) \u2014 Surface topography and texture (nominal), imaged \"enlarged up to \u00d7200,000 and resolved up to 5 nm\" (p.3)"
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
        "ada:ebsdIndexingMethod": "missing"
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
      "schema:name": "semImaging",
      "schema:termCode": "semImaging"
    }
  ],
  "ada:clAcquisitionMode": "missing",
  "ada:clIntegrationTimeDefault": -9999,
  "ada:clWavelengthRange": -9999,
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:ebsdDetectorConfiguration": "missing",
  "ada:ebsdPhaseListDefault": "missing",
  "ada:ebsdStepSizeDefault": -9999,
  "ada:sampleTiltAngle": -9999,
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

<ex:semImagingTAPP-Pascucci2026-2> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:description "Embedded in epoxy, polished to ¼ µm level, sputtered with 30-nm-thick carbon film" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:ebsdIndexingMethod "missing" ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "SE imaging used for topographic examination; instrument capability: up to ×200,000 magnification, 5 nm resolution; SE acquired before EDS to minimize charging effects" ;
    schema1:instrument <ex:instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "CNR IMAA (Institute of Methodologies for Environmental Analysis), Italian National Research Council, Potenza, Italy" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semImaging" ;
            schema1:termCode "semImaging" ] ;
    schema1:name "semImaging protocol — Pascucci2026-2" ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "BSE Imaging (Zeiss Supra 40 FE-SEM); EDS (Zeiss Supra 40 FE-SEM); EMPA-WDS (JEOL JXA-8230, separate instrument); VIS-IR spectroscopy (SPIM)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "SE Imaging" ;
    ada:clAcquisitionMode "missing" ;
    ada:clIntegrationTimeDefault -9999 ;
    ada:clWavelengthRange -9999 ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:ebsdDetectorConfiguration "missing" ;
    ada:ebsdPhaseListDefault "missing" ;
    ada:ebsdStepSizeDefault -9999 ;
    ada:reportedProperties "surface topography (nominal); texture (nominal) — Surface topography and texture (nominal), imaged \"enlarged up to ×200,000 and resolved up to 5 nm\" (p.3)" ;
    ada:sampleTiltAngle -9999 ;
    ada:samplingUnitSelectionCriteriaDefault "Spatial co-registration with the spectral imagery — the SEM work targets \"almost the same portion of the VIS-IR SPIM images\" (p.4), so that the two datasets can be compared on the same area of the slab" ;
    ada:samplingUnitType "Whole sample (polished slab) > Region of interest — \"Secondary electrons were used to construct images enlarged up to ×200,000 and resolved up to 5 nm\" (p.3) on the \"NWA 7317 slab\", a \"small fragment of about 10 × 6 mm\" embedded in epoxy and polished (pp.3–4)" ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "carbonaceous chondrite" ;
            ada:targetMaterialColumns [ schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ] ] .

<ex:instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:description "ESEM" ;
    schema1:hasPart <ex:instrument/SEM/part/BSE-Detector>,
        <ex:instrument/SEM/part/Electron-Source>,
        <ex:instrument/SEM/part/SE-Detector> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Zeiss" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Supra 40" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault -9999 ;
    ada:mappingBeamCurrentDefault -9999 ;
    ada:workingDistanceDefault -9999 .

<ex:instrument/SEM/part/BSE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "BSE Detector" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Field emission gun (FEG) — subtype not specified" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/SE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SE Detector" ;
    schema1:name "missing" .


```


### semImagingTAPP example Zega2025
semImagingTAPP instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | BSE Imaging (JEOL 7600F, NASA JSC, 15 kV).
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
  "@id": "ex:semImagingTAPP-Zega2025",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semImaging protocol — Zega2025",
  "schema:description": "SE and BSE imaging; EDS point spectra; Oxford AZtec system; EDS detector: Oxford Instruments Ultim Max SDD 170 mm²",
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
        "schema:name": "example instrumentName"
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
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "BSE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/BSE-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "SE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/SE-Detector"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName",
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:workingDistanceDefault": -9999,
      "schema:description": "missing"
    }
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
        "schema:name": "EDS (JEOL 7600F, JSC); SE Imaging (JEOL 7600F, JSC); FIB-SEM TEM prep (Quanta3D600, JSC)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Region of interest — \"Characterization of regions of interest was performed at an accelerating voltage of 15 kV using both secondary electron (SE) and low-angle backscattered electron imaging modes\", on a particle \"attached to an Al cylinder SEM mount\" (p.9)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "acquisition",
      "schema:name": "Oxford AZtec (Point & ID programme)"
    }
  ],
  "ada:analyticalMode": [
    "BSE Imaging"
  ],
  "ada:reportedProperties": [
    "particle texture (nominal); phase occurrence (nominal); grain size (µm) — Particle textures and phase occurrences (nominal), with grain sizes in µm — angular, hummocky and other particle types imaged for the regions of interest (Fig. 1, p.2)"
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
        "ada:ebsdIndexingMethod": "missing"
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
      "schema:name": "semImaging",
      "schema:termCode": "semImaging"
    }
  ],
  "ada:clAcquisitionMode": "missing",
  "ada:clIntegrationTimeDefault": -9999,
  "ada:clWavelengthRange": -9999,
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:ebsdDetectorConfiguration": "missing",
  "ada:ebsdPhaseListDefault": "missing",
  "ada:ebsdStepSizeDefault": -9999,
  "ada:sampleTiltAngle": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Imaging/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semImagingTAPP-Zega2025",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semImaging protocol \u2014 Zega2025",
  "schema:description": "SE and BSE imaging; EDS point spectra; Oxford AZtec system; EDS detector: Oxford Instruments Ultim Max SDD 170 mm\u00b2",
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
        "schema:name": "example instrumentName"
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
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "BSE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/BSE-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "SE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/SE-Detector"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName",
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:workingDistanceDefault": -9999,
      "schema:description": "missing"
    }
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
        "schema:name": "EDS (JEOL 7600F, JSC); SE Imaging (JEOL 7600F, JSC); FIB-SEM TEM prep (Quanta3D600, JSC)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Region of interest \u2014 \"Characterization of regions of interest was performed at an accelerating voltage of 15 kV using both secondary electron (SE) and low-angle backscattered electron imaging modes\", on a particle \"attached to an Al cylinder SEM mount\" (p.9)",
  "bios:computationalTool": [
    {
      "ada:toolRole": "acquisition",
      "schema:name": "Oxford AZtec (Point & ID programme)"
    }
  ],
  "ada:analyticalMode": [
    "BSE Imaging"
  ],
  "ada:reportedProperties": [
    "particle texture (nominal); phase occurrence (nominal); grain size (\u00b5m) \u2014 Particle textures and phase occurrences (nominal), with grain sizes in \u00b5m \u2014 angular, hummocky and other particle types imaged for the regions of interest (Fig. 1, p.2)"
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
        "ada:ebsdIndexingMethod": "missing"
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
      "schema:name": "semImaging",
      "schema:termCode": "semImaging"
    }
  ],
  "ada:clAcquisitionMode": "missing",
  "ada:clIntegrationTimeDefault": -9999,
  "ada:clWavelengthRange": -9999,
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:ebsdDetectorConfiguration": "missing",
  "ada:ebsdPhaseListDefault": "missing",
  "ada:ebsdStepSizeDefault": -9999,
  "ada:sampleTiltAngle": -9999,
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

<ex:semImagingTAPP-Zega2025> a cdi:Activity,
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
                    ada:ebsdIndexingMethod "missing" ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:description "Attached to Al cylinder SEM mount with double-sided C tape; sputter coated with ~5 nm carbon" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "SE and BSE imaging; EDS point spectra; Oxford AZtec system; EDS detector: Oxford Instruments Ultim Max SDD 170 mm²" ;
    schema1:instrument <ex:instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "NASA Johnson Space Center (JSC), Houston, TX, USA" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semImaging" ;
            schema1:termCode "semImaging" ] ;
    schema1:name "semImaging protocol — Zega2025" ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "EDS (JEOL 7600F, JSC); SE Imaging (JEOL 7600F, JSC); FIB-SEM TEM prep (Quanta3D600, JSC)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "BSE Imaging" ;
    ada:clAcquisitionMode "missing" ;
    ada:clIntegrationTimeDefault -9999 ;
    ada:clWavelengthRange -9999 ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:ebsdDetectorConfiguration "missing" ;
    ada:ebsdPhaseListDefault "missing" ;
    ada:ebsdStepSizeDefault -9999 ;
    ada:reportedProperties "particle texture (nominal); phase occurrence (nominal); grain size (µm) — Particle textures and phase occurrences (nominal), with grain sizes in µm — angular, hummocky and other particle types imaged for the regions of interest (Fig. 1, p.2)" ;
    ada:sampleTiltAngle -9999 ;
    ada:samplingUnitSelectionCriteriaDefault "N — the passage says regions of interest were characterized (\"Characterization of regions of interest was performed at an accelerating voltage of 15 kV\", p.9) but gives no rule for choosing them" ;
    ada:samplingUnitType "Region of interest — \"Characterization of regions of interest was performed at an accelerating voltage of 15 kV using both secondary electron (SE) and low-angle backscattered electron imaging modes\", on a particle \"attached to an Al cylinder SEM mount\" (p.9)" ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "Bennu particles" ;
            ada:targetMaterialColumns [ schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ] ] ;
    bios:computationalTool [ schema1:name "Oxford AZtec (Point & ID programme)" ;
            ada:toolRole "acquisition" ] .

<ex:instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:description "missing" ;
    schema1:hasPart <ex:instrument/SEM/part/BSE-Detector>,
        <ex:instrument/SEM/part/Electron-Source>,
        <ex:instrument/SEM/part/SE-Detector> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "JEOL" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "7600F" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "15 kV" ;
    ada:mappingBeamCurrentDefault -9999 ;
    ada:workingDistanceDefault -9999 .

<ex:instrument/SEM/part/BSE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "BSE Detector" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Field emission gun (FEG) — subtype not specified" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/SE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SE Detector" ;
    schema1:name "missing" .


```


### semImagingTAPP example Zega2025-2
semImagingTAPP instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | SE Imaging (Hitachi S-4800, U Arizona).
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
  "@id": "ex:semImagingTAPP-Zega2025-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semImaging protocol — Zega2025-2",
  "schema:description": "Cold FEG; system range 0.5-30 keV; SE and BSE imaging detectors; also equipped with Oxford Instruments Aztec Live/x-stream/Ultimax 170 SDD EDS; specific operating voltage not stated",
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
        "schema:name": "example instrumentName"
      }
    ]
  },
  "ada:samplingUnitSelectionCriteriaDefault": "N — the passage states the mounting and imaging conditions only, and no rule for choosing units (p.9)",
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
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "BSE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/BSE-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "SE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/SE-Detector"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName",
      "ada:acceleratingVoltageDefault": -9999,
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:workingDistanceDefault": -9999,
      "schema:description": "missing"
    }
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
        "schema:name": "BSE Imaging (Hitachi S-4800, U Arizona); EDS (Hitachi S-4800, U Arizona); FIB-SEM TEM prep (Helios G3, U Arizona); EMPA (Cameca SX-100 Ultra, out of scope)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Whole sample (polished section) > Region of interest — \"SE and BSE images were acquired using a Hitachi S-4800 SEM\" on \"Polished sections\" (p.9); the imaged fields are not labelled",
  "ada:analyticalMode": [
    "SE Imaging"
  ],
  "ada:reportedProperties": [
    "surface morphology (nominal); texture (nominal) — Particle surface morphology and texture (nominal) — pitted sulfide surfaces and particle shapes (p.2)"
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
        "ada:ebsdIndexingMethod": "missing"
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
      "schema:name": "semImaging",
      "schema:termCode": "semImaging"
    }
  ],
  "ada:clAcquisitionMode": "missing",
  "ada:clIntegrationTimeDefault": -9999,
  "ada:clWavelengthRange": -9999,
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:ebsdDetectorConfiguration": "missing",
  "ada:ebsdPhaseListDefault": "missing",
  "ada:ebsdStepSizeDefault": -9999,
  "ada:sampleTiltAngle": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Imaging/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semImagingTAPP-Zega2025-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semImaging protocol \u2014 Zega2025-2",
  "schema:description": "Cold FEG; system range 0.5-30 keV; SE and BSE imaging detectors; also equipped with Oxford Instruments Aztec Live/x-stream/Ultimax 170 SDD EDS; specific operating voltage not stated",
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
        "schema:name": "example instrumentName"
      }
    ]
  },
  "ada:samplingUnitSelectionCriteriaDefault": "N \u2014 the passage states the mounting and imaging conditions only, and no rule for choosing units (p.9)",
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
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "BSE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/BSE-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "SE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/SE-Detector"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName",
      "ada:acceleratingVoltageDefault": -9999,
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:workingDistanceDefault": -9999,
      "schema:description": "missing"
    }
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
        "schema:name": "BSE Imaging (Hitachi S-4800, U Arizona); EDS (Hitachi S-4800, U Arizona); FIB-SEM TEM prep (Helios G3, U Arizona); EMPA (Cameca SX-100 Ultra, out of scope)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Whole sample (polished section) > Region of interest \u2014 \"SE and BSE images were acquired using a Hitachi S-4800 SEM\" on \"Polished sections\" (p.9); the imaged fields are not labelled",
  "ada:analyticalMode": [
    "SE Imaging"
  ],
  "ada:reportedProperties": [
    "surface morphology (nominal); texture (nominal) \u2014 Particle surface morphology and texture (nominal) \u2014 pitted sulfide surfaces and particle shapes (p.2)"
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
        "ada:ebsdIndexingMethod": "missing"
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
      "schema:name": "semImaging",
      "schema:termCode": "semImaging"
    }
  ],
  "ada:clAcquisitionMode": "missing",
  "ada:clIntegrationTimeDefault": -9999,
  "ada:clWavelengthRange": -9999,
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:ebsdDetectorConfiguration": "missing",
  "ada:ebsdPhaseListDefault": "missing",
  "ada:ebsdStepSizeDefault": -9999,
  "ada:sampleTiltAngle": -9999,
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

<ex:semImagingTAPP-Zega2025-2> a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:description "Polished sections; coated with 0.1 nm carbon for charge mitigation" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ;
                    ada:ebsdIndexingMethod "missing" ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "Cold FEG; system range 0.5-30 keV; SE and BSE imaging detectors; also equipped with Oxford Instruments Aztec Live/x-stream/Ultimax 170 SDD EDS; specific operating voltage not stated" ;
    schema1:instrument <ex:instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "K-ALFAA (Kuiper-Arizona Laboratory for Astromaterials Analysis), University of Arizona" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semImaging" ;
            schema1:termCode "semImaging" ] ;
    schema1:name "semImaging protocol — Zega2025-2" ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "BSE Imaging (Hitachi S-4800, U Arizona); EDS (Hitachi S-4800, U Arizona); FIB-SEM TEM prep (Helios G3, U Arizona); EMPA (Cameca SX-100 Ultra, out of scope)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "SE Imaging" ;
    ada:clAcquisitionMode "missing" ;
    ada:clIntegrationTimeDefault -9999 ;
    ada:clWavelengthRange -9999 ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:ebsdDetectorConfiguration "missing" ;
    ada:ebsdPhaseListDefault "missing" ;
    ada:ebsdStepSizeDefault -9999 ;
    ada:reportedProperties "surface morphology (nominal); texture (nominal) — Particle surface morphology and texture (nominal) — pitted sulfide surfaces and particle shapes (p.2)" ;
    ada:sampleTiltAngle -9999 ;
    ada:samplingUnitSelectionCriteriaDefault "N — the passage states the mounting and imaging conditions only, and no rule for choosing units (p.9)" ;
    ada:samplingUnitType "Whole sample (polished section) > Region of interest — \"SE and BSE images were acquired using a Hitachi S-4800 SEM\" on \"Polished sections\" (p.9); the imaged fields are not labelled" ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "Bennu particles" ;
            ada:targetMaterialColumns [ schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ] ] .

<ex:instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:description "missing" ;
    schema1:hasPart <ex:instrument/SEM/part/BSE-Detector>,
        <ex:instrument/SEM/part/Electron-Source>,
        <ex:instrument/SEM/part/SE-Detector> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Hitachi" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "S-4800" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault -9999 ;
    ada:mappingBeamCurrentDefault -9999 ;
    ada:workingDistanceDefault -9999 .

<ex:instrument/SEM/part/BSE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "BSE Detector" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Unknown" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/SE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SE Detector" ;
    schema1:name "missing" .


```


### semImagingTAPP example Zega2025-3
semImagingTAPP instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | BSE Imaging (Hitachi S-4800, U Arizona).
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
  "@id": "ex:semImagingTAPP-Zega2025-3",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semImaging protocol — Zega2025-3",
  "schema:description": "Cold FEG; system range 0.5-30 keV; SE and BSE imaging; EDS mapping; specific operating voltage not stated",
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
        "schema:name": "example instrumentName"
      }
    ]
  },
  "ada:samplingUnitSelectionCriteriaDefault": "N — the passage states the mounting and imaging conditions only, and no rule for choosing units (p.9)",
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
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "BSE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/BSE-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "SE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/SE-Detector"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName",
      "ada:acceleratingVoltageDefault": -9999,
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:workingDistanceDefault": -9999,
      "schema:description": "missing"
    }
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
        "schema:name": "SE Imaging (Hitachi S-4800, U Arizona); EDS (Hitachi S-4800, U Arizona); FIB-SEM TEM prep (Helios G3, U Arizona); EMPA (Cameca SX-100 Ultra, out of scope)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Whole sample (polished section) > Region of interest — \"SE and BSE images were acquired using a Hitachi S-4800 SEM\" on \"Polished sections\" (p.9); the imaged fields are not labelled",
  "ada:analyticalMode": [
    "BSE Imaging"
  ],
  "ada:reportedProperties": [
    "phase distribution (nominal); texture (nominal); grain size (µm) — Phase distribution and texture within the polished sections (nominal), with grain sizes in µm (Fig. 1, p.2)"
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
        "ada:ebsdIndexingMethod": "missing"
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
      "schema:name": "semImaging",
      "schema:termCode": "semImaging"
    }
  ],
  "ada:clAcquisitionMode": "missing",
  "ada:clIntegrationTimeDefault": -9999,
  "ada:clWavelengthRange": -9999,
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:ebsdDetectorConfiguration": "missing",
  "ada:ebsdPhaseListDefault": "missing",
  "ada:ebsdStepSizeDefault": -9999,
  "ada:sampleTiltAngle": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Imaging/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semImagingTAPP-Zega2025-3",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semImaging protocol \u2014 Zega2025-3",
  "schema:description": "Cold FEG; system range 0.5-30 keV; SE and BSE imaging; EDS mapping; specific operating voltage not stated",
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
        "schema:name": "example instrumentName"
      }
    ]
  },
  "ada:samplingUnitSelectionCriteriaDefault": "N \u2014 the passage states the mounting and imaging conditions only, and no rule for choosing units (p.9)",
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
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "BSE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/BSE-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "SE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/SE-Detector"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName",
      "ada:acceleratingVoltageDefault": -9999,
      "ada:mappingBeamCurrentDefault": -9999,
      "ada:workingDistanceDefault": -9999,
      "schema:description": "missing"
    }
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
        "schema:name": "SE Imaging (Hitachi S-4800, U Arizona); EDS (Hitachi S-4800, U Arizona); FIB-SEM TEM prep (Helios G3, U Arizona); EMPA (Cameca SX-100 Ultra, out of scope)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Whole sample (polished section) > Region of interest \u2014 \"SE and BSE images were acquired using a Hitachi S-4800 SEM\" on \"Polished sections\" (p.9); the imaged fields are not labelled",
  "ada:analyticalMode": [
    "BSE Imaging"
  ],
  "ada:reportedProperties": [
    "phase distribution (nominal); texture (nominal); grain size (\u00b5m) \u2014 Phase distribution and texture within the polished sections (nominal), with grain sizes in \u00b5m (Fig. 1, p.2)"
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
        "ada:ebsdIndexingMethod": "missing"
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
      "schema:name": "semImaging",
      "schema:termCode": "semImaging"
    }
  ],
  "ada:clAcquisitionMode": "missing",
  "ada:clIntegrationTimeDefault": -9999,
  "ada:clWavelengthRange": -9999,
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:ebsdDetectorConfiguration": "missing",
  "ada:ebsdPhaseListDefault": "missing",
  "ada:ebsdStepSizeDefault": -9999,
  "ada:sampleTiltAngle": -9999,
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

<ex:semImagingTAPP-Zega2025-3> a cdi:Activity,
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
                    ada:ebsdIndexingMethod "missing" ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:description "Polished sections; coated with 0.1 nm carbon for charge mitigation" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "Cold FEG; system range 0.5-30 keV; SE and BSE imaging; EDS mapping; specific operating voltage not stated" ;
    schema1:instrument <ex:instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "K-ALFAA (Kuiper-Arizona Laboratory for Astromaterials Analysis), University of Arizona" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semImaging" ;
            schema1:termCode "semImaging" ] ;
    schema1:name "semImaging protocol — Zega2025-3" ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SE Imaging (Hitachi S-4800, U Arizona); EDS (Hitachi S-4800, U Arizona); FIB-SEM TEM prep (Helios G3, U Arizona); EMPA (Cameca SX-100 Ultra, out of scope)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "BSE Imaging" ;
    ada:clAcquisitionMode "missing" ;
    ada:clIntegrationTimeDefault -9999 ;
    ada:clWavelengthRange -9999 ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:ebsdDetectorConfiguration "missing" ;
    ada:ebsdPhaseListDefault "missing" ;
    ada:ebsdStepSizeDefault -9999 ;
    ada:reportedProperties "phase distribution (nominal); texture (nominal); grain size (µm) — Phase distribution and texture within the polished sections (nominal), with grain sizes in µm (Fig. 1, p.2)" ;
    ada:sampleTiltAngle -9999 ;
    ada:samplingUnitSelectionCriteriaDefault "N — the passage states the mounting and imaging conditions only, and no rule for choosing units (p.9)" ;
    ada:samplingUnitType "Whole sample (polished section) > Region of interest — \"SE and BSE images were acquired using a Hitachi S-4800 SEM\" on \"Polished sections\" (p.9); the imaged fields are not labelled" ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "Bennu particles" ;
            ada:targetMaterialColumns [ schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ] ] .

<ex:instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:description "missing" ;
    schema1:hasPart <ex:instrument/SEM/part/BSE-Detector>,
        <ex:instrument/SEM/part/Electron-Source>,
        <ex:instrument/SEM/part/SE-Detector> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Hitachi" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "S-4800" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault -9999 ;
    ada:mappingBeamCurrentDefault -9999 ;
    ada:workingDistanceDefault -9999 .

<ex:instrument/SEM/part/BSE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "BSE Detector" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Unknown" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/SE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SE Detector" ;
    schema1:name "missing" .


```


### semImagingTAPP example Zega2025-4
semImagingTAPP instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | CL Mapping (JEOL JSM-7000F, Universite Cote d'Azur, 5 keV).
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
  "@id": "ex:semImagingTAPP-Zega2025-4",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semImaging protocol — Zega2025-4",
  "schema:description": "CL emitting volume at 5 keV: up to 230 nm depth, 200 nm sideways (assuming 100-nm graphite coating); recording below focal plane for magnifications <×500 to minimize hotspot effect Reported detail: ada:clAcquisitionMode = Panchromatic imaging; hyperspectral analysis; monochromatic imaging.",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "olivine",
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
        "schema:name": "example instrumentName"
      }
    ]
  },
  "ada:samplingUnitSelectionCriteriaDefault": "N — the passage states the mounting and imaging conditions only, and no rule for choosing units (p.9)",
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
        "schema:name": "JSM-7000F",
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
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "BSE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/BSE-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "SE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/SE-Detector"
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/semImagingTAPP/clDetectorConfiguration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semImagingTAPP/clDetectorConfiguration"
            }
          ],
          "schema:name": "CL Detector Configuration",
          "schema:value": "MonoCL4 GATAN monochromator; high-sensitivity array detector and photomultiplier; paraboloidal mirror collection (CRHEA Valbonne, France)"
        }
      ],
      "ada:acceleratingVoltageDefault": "5 keV",
      "ada:mappingBeamCurrentDefault": "1 to 4 nA",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName",
      "ada:workingDistanceDefault": -9999,
      "schema:description": "missing"
    }
  ],
  "ada:clAcquisitionMode": "Monochromatic imaging",
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Université Côte d'Azur / Observatoire de la Côte d'Azur, Valbonne, France"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "BSE/EDS (JEOL 7600F, JSC); SE/BSE/EDS (Hitachi S-4800, U Arizona)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Whole sample (particle thin section) > Region of interest — panchromatic and monochromatic CL imaging of \"Bennu particle thin sections\", the emitting volume reaching \"up to 230 nm below the bombarded sample surface and around to 200 nm sideways\" (p.9)",
  "ada:analyticalMode": [
    "CL Mapping"
  ],
  "ada:reportedProperties": [
    "panchromatic CL images; monochromatic CL images; hyperspectral CL; luminescence zoning (nominal) — Panchromatic and monochromatic CL images, and hyperspectral CL, collected at 5 keV with 1–4 nA (p.9); the reported result is luminescence zoning within carbonate grains, e.g. \"a core-shell texture, with Fe–Mn-rich magnesite (M) non-luminescent crystals forming the core\" (Fig. 6, p.6) — nominal"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished thin sections; ~100 nm graphite coating (as stated in CL emitting volume calculation)",
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
        "ada:ebsdIndexingMethod": "missing"
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
      "schema:name": "semImaging",
      "schema:termCode": "semImaging"
    }
  ],
  "ada:clIntegrationTimeDefault": -9999,
  "ada:clWavelengthRange": -9999,
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:ebsdDetectorConfiguration": "missing",
  "ada:ebsdPhaseListDefault": "missing",
  "ada:ebsdStepSizeDefault": -9999,
  "ada:sampleTiltAngle": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Imaging/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semImagingTAPP-Zega2025-4",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semImaging protocol \u2014 Zega2025-4",
  "schema:description": "CL emitting volume at 5 keV: up to 230 nm depth, 200 nm sideways (assuming 100-nm graphite coating); recording below focal plane for magnifications <\u00d7500 to minimize hotspot effect Reported detail: ada:clAcquisitionMode = Panchromatic imaging; hyperspectral analysis; monochromatic imaging.",
  "ada:targetMaterialTemplate": {
    "ada:defaultTargetMaterials": [
      "olivine",
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
        "schema:name": "example instrumentName"
      }
    ]
  },
  "ada:samplingUnitSelectionCriteriaDefault": "N \u2014 the passage states the mounting and imaging conditions only, and no rule for choosing units (p.9)",
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
        "schema:name": "JSM-7000F",
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
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "BSE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/BSE-Detector"
        },
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "SE Detector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/SEM/part/SE-Detector"
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/semImagingTAPP/clDetectorConfiguration",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/semImagingTAPP/clDetectorConfiguration"
            }
          ],
          "schema:name": "CL Detector Configuration",
          "schema:value": "MonoCL4 GATAN monochromator; high-sensitivity array detector and photomultiplier; paraboloidal mirror collection (CRHEA Valbonne, France)"
        }
      ],
      "ada:acceleratingVoltageDefault": "5 keV",
      "ada:mappingBeamCurrentDefault": "1 to 4 nA",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName",
      "ada:workingDistanceDefault": -9999,
      "schema:description": "missing"
    }
  ],
  "ada:clAcquisitionMode": "Monochromatic imaging",
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Universit\u00e9 C\u00f4te d'Azur / Observatoire de la C\u00f4te d'Azur, Valbonne, France"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "BSE/EDS (JEOL 7600F, JSC); SE/BSE/EDS (Hitachi S-4800, U Arizona)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:samplingUnitType": "Whole sample (particle thin section) > Region of interest \u2014 panchromatic and monochromatic CL imaging of \"Bennu particle thin sections\", the emitting volume reaching \"up to 230 nm below the bombarded sample surface and around to 200 nm sideways\" (p.9)",
  "ada:analyticalMode": [
    "CL Mapping"
  ],
  "ada:reportedProperties": [
    "panchromatic CL images; monochromatic CL images; hyperspectral CL; luminescence zoning (nominal) \u2014 Panchromatic and monochromatic CL images, and hyperspectral CL, collected at 5 keV with 1\u20134 nA (p.9); the reported result is luminescence zoning within carbonate grains, e.g. \"a core-shell texture, with Fe\u2013Mn-rich magnesite (M) non-luminescent crystals forming the core\" (Fig. 6, p.6) \u2014 nominal"
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished thin sections; ~100 nm graphite coating (as stated in CL emitting volume calculation)",
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
        "ada:ebsdIndexingMethod": "missing"
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
      "schema:name": "semImaging",
      "schema:termCode": "semImaging"
    }
  ],
  "ada:clIntegrationTimeDefault": -9999,
  "ada:clWavelengthRange": -9999,
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:ebsdDetectorConfiguration": "missing",
  "ada:ebsdPhaseListDefault": "missing",
  "ada:ebsdStepSizeDefault": -9999,
  "ada:sampleTiltAngle": -9999,
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

<ex:semImagingTAPP-Zega2025-4> a cdi:Activity,
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
                    ada:ebsdIndexingMethod "missing" ],
                [ a cdi:Activity,
                        schema1:Action,
                        schema1:HowToStep ;
                    schema1:additionalType bios:LabProcess ;
                    schema1:description "Polished thin sections; ~100 nm graphite coating (as stated in CL emitting volume calculation)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "CL emitting volume at 5 keV: up to 230 nm depth, 200 nm sideways (assuming 100-nm graphite coating); recording below focal plane for magnifications <×500 to minimize hotspot effect Reported detail: ada:clAcquisitionMode = Panchromatic imaging; hyperspectral analysis; monochromatic imaging." ;
    schema1:instrument <ex:instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Université Côte d'Azur / Observatoire de la Côte d'Azur, Valbonne, France" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semImaging" ;
            schema1:termCode "semImaging" ] ;
    schema1:name "semImaging protocol — Zega2025-4" ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "BSE/EDS (JEOL 7600F, JSC); SE/BSE/EDS (Hitachi S-4800, U Arizona)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "CL Mapping" ;
    ada:clAcquisitionMode "Monochromatic imaging" ;
    ada:clIntegrationTimeDefault -9999 ;
    ada:clWavelengthRange -9999 ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:ebsdDetectorConfiguration "missing" ;
    ada:ebsdPhaseListDefault "missing" ;
    ada:ebsdStepSizeDefault -9999 ;
    ada:reportedProperties "panchromatic CL images; monochromatic CL images; hyperspectral CL; luminescence zoning (nominal) — Panchromatic and monochromatic CL images, and hyperspectral CL, collected at 5 keV with 1–4 nA (p.9); the reported result is luminescence zoning within carbonate grains, e.g. \"a core-shell texture, with Fe–Mn-rich magnesite (M) non-luminescent crystals forming the core\" (Fig. 6, p.6) — nominal" ;
    ada:sampleTiltAngle -9999 ;
    ada:samplingUnitSelectionCriteriaDefault "N — the passage states the mounting and imaging conditions only, and no rule for choosing units (p.9)" ;
    ada:samplingUnitType "Whole sample (particle thin section) > Region of interest — panchromatic and monochromatic CL imaging of \"Bennu particle thin sections\", the emitting volume reaching \"up to 230 nm below the bombarded sample surface and around to 200 nm sideways\" (p.9)" ;
    ada:targetMaterialTemplate [ ada:defaultTargetMaterials "carbonate",
                "olivine" ;
            ada:targetMaterialColumns [ schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "targetMaterial" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ] ] .

<ex:instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semImagingTAPP/clDetectorConfiguration> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:description "missing" ;
    schema1:hasPart <ex:instrument/SEM/part/BSE-Detector>,
        <ex:instrument/SEM/part/Electron-Source>,
        <ex:instrument/SEM/part/SE-Detector> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "JEOL" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "JSM-7000F" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "5 keV" ;
    ada:mappingBeamCurrentDefault "1 to 4 nA" ;
    ada:workingDistanceDefault -9999 .

<ex:instrument/SEM/part/BSE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "BSE Detector" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Field emission gun (FEG) — subtype not specified" ;
    schema1:name "missing" .

<ex:instrument/SEM/part/SE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SE Detector" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/semImagingTAPP/clDetectorConfiguration> a schema1:PropertyValue ;
    schema1:name "CL Detector Configuration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semImagingTAPP/clDetectorConfiguration> ;
    schema1:value "MonoCL4 GATAN monochromator; high-sensitivity array detector and photomultiplier; paraboloidal mirror collection (CRHEA Valbonne, France)" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: SEM Imaging Technique-Aligned Protocol Profile (semImagingTAPP)
description: 'Scanning electron microscopy imaging (SE/BSE/CL/EBSD) extension of the
  base TAPP definition. Basic protocol-tier fields are required top-level ada: properties;
  Advanced protocol-tier fields are schema:additionalProperty[] entries. No ada:targetSpeciesTemplate
  (imaging has no per-element analyte axis). Generated from tapp/Current TAPPs/SEM_Imaging_TAPP_v44.csv
  by tools/build_tapp.py.'
allOf:
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/ProcedureIdentification
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
                            const: SE Detector
                          schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                      required:
                      - schema:additionalType
                    then:
                      properties:
                        schema:name:
                          description: Type of secondary electron detector used. Everhart-Thornley
                            (ET) detector is the standard off-axis collector sensitive
                            to SE2 and some BSE; in-lens (TLD) detectors collect high-resolution
                            SE1 signal at short working distances; GSED/ESED detectors
                            operate in VP/ESEM mode by using the chamber gas as the
                            signal amplification medium.
                          anyOf:
                          - type: string
                            enum:
                            - Everhart-Thornley (ET)
                            - In-lens / TLD (through-the-lens)
                            - GSED (VP/ESEM)
                            - ESED (VP/ESEM)
                            - N/A
                            - None
                            - missing
                            readOnly: true
                          - type: array
                            items:
                              type: string
                              enum:
                              - Everhart-Thornley (ET)
                              - In-lens / TLD (through-the-lens)
                              - GSED (VP/ESEM)
                              - ESED (VP/ESEM)
                              - N/A
                              - None
                              - missing
                              readOnly: true
                      required:
                      - schema:name
                  - if:
                      properties:
                        schema:additionalType:
                          contains:
                            const: BSE Detector
                          schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                      required:
                      - schema:additionalType
                    then:
                      properties:
                        schema:name:
                          description: Type of backscattered electron detector. Segmented
                            detectors can operate in composition mode (segments summed)
                            or topography mode (differential signal between segments).
                          anyOf:
                          - type: string
                            enum:
                            - Solid-state diode (single)
                            - Solid-state diode (segmented, composition mode)
                            - Solid-state diode (segmented, topography mode)
                            - Solid-state diode (segmented, mode not specified)
                            - Solid-state diode (type not specified)
                            - In-lens BSE
                            - YAG scintillator
                            - N/A
                            - None
                            - missing
                            readOnly: true
                          - type: array
                            items:
                              type: string
                              enum:
                              - Solid-state diode (single)
                              - Solid-state diode (segmented, composition mode)
                              - Solid-state diode (segmented, topography mode)
                              - Solid-state diode (segmented, mode not specified)
                              - Solid-state diode (type not specified)
                              - In-lens BSE
                              - YAG scintillator
                              - N/A
                              - None
                              - missing
                              readOnly: true
                      required:
                      - schema:name
                allOf:
                - contains:
                    properties:
                      schema:additionalType:
                        contains:
                          const: Electron Source
                        schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                    required:
                    - schema:additionalType
                - contains:
                    properties:
                      schema:additionalType:
                        contains:
                          const: SE Detector
                        schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                    required:
                    - schema:additionalType
                - contains:
                    properties:
                      schema:additionalType:
                        contains:
                          const: BSE Detector
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
              schema:additionalProperty:
                type: array
                items:
                  anyOf:
                  - title: CL Detector Configuration
                    description: CL detector type, manufacturer, model, collection
                      optics (e.g., parabolic mirror, elliptical mirror, light guide),
                      and spectral detection configuration (PMT for panchromatic,
                      CCD/EMCCD for spectral, multi-channel for pseudo-color CL).
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/semImagingTAPP/clDetectorConfiguration
                      '@type':
                        const:
                        - schema:PropertyValue
                      schema:propertyID:
                        const:
                        - '@id': ada:parameter/semImagingTAPP/clDetectorConfiguration
                      schema:name:
                        const: CL Detector Configuration
                      schema:value:
                        type: string
                    required:
                    - '@id'
                    - '@type'
                    - schema:propertyID
                    - schema:name
                    - schema:value
                    readOnly: true
                  - title: CL Grating
                    description: Diffraction grating specification for spectral or
                      hyperspectral CL acquisition, including groove density and blaze
                      wavelength. Not applicable to panchromatic-only acquisition.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/semImagingTAPP/clGrating
                      '@type':
                        const:
                        - schema:PropertyValue
                      schema:propertyID:
                        const:
                        - '@id': ada:parameter/semImagingTAPP/clGrating
                      schema:name:
                        const: CL Grating
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
                    title: CL Detector Configuration
                    description: CL detector type, manufacturer, model, collection
                      optics (e.g., parabolic mirror, elliptical mirror, light guide),
                      and spectral detection configuration (PMT for panchromatic,
                      CCD/EMCCD for spectral, multi-channel for pseudo-color CL).
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/semImagingTAPP/clDetectorConfiguration
                      '@type':
                        const:
                        - schema:PropertyValue
                      schema:propertyID:
                        const:
                        - '@id': ada:parameter/semImagingTAPP/clDetectorConfiguration
                      schema:name:
                        const: CL Detector Configuration
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
                    title: CL Grating
                    description: Diffraction grating specification for spectral or
                      hyperspectral CL acquisition, including groove density and blaze
                      wavelength. Not applicable to panchromatic-only acquisition.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/semImagingTAPP/clGrating
                      '@type':
                        const:
                        - schema:PropertyValue
                      schema:propertyID:
                        const:
                        - '@id': ada:parameter/semImagingTAPP/clGrating
                      schema:name:
                        const: CL Grating
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
              ada:acceleratingVoltageDefault:
                description: Electron beam accelerating voltage in kilovolts.
                anyOf:
                - type: number
                - type: string
              ada:workingDistanceDefault:
                description: Distance between the objective lens pole piece and the
                  specimen surface in millimetres.
                anyOf:
                - type: number
                - type: string
              ada:mappingBeamCurrentDefault:
                description: 'Electron beam probe current used while the beam scans
                  an area: an X-ray or CL map, an EBSD map, or an SE or BSE image,
                  including images taken during FIB-SEM work. For sub-nA values use
                  decimal notation (e.g., 0.4 nA). Ion-beam currents used for milling
                  belong in the milling condition fields.'
                anyOf:
                - type: number
                - type: string
            required:
            - ada:acceleratingVoltageDefault
            - ada:mappingBeamCurrentDefault
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
    ada:ebsdDetectorConfiguration:
      description: EBSD detector manufacturer, model, and camera resolution. Include
        whether EBSD and EDS are acquired simultaneously (common on modern combined
        EBSD-EDS systems).
      type: string
      readOnly: true
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
                  const: ada:targetSpeciesColumn/semImagingTAPP/beamCurrent
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
                  const: ada:targetSpeciesColumn/semImagingTAPP/beamCurrent
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
    schema:additionalProperty:
      type: array
      items:
        anyOf:
        - title: Chamber Pressure
          description: Chamber pressure and gas type during analysis. Required for
            variable pressure (VP-SEM) and environmental SEM (ESEM) modes. Report
            value and unit (Pa or Torr) and gas composition. Use 'None' for standard
            high-vacuum operation.
          type: object
          properties:
            '@id':
              const: ada:parameter/semImagingTAPP/chamberPressureDefault
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
            schema:defaultValue:
              anyOf:
              - type: number
              - type: string
            schema:unitText:
              type: string
          required:
          - '@id'
          - '@type'
          - schema:valueName
          - schema:name
          - ada:dataType
          - ada:fieldScope
        - title: Image Pixel Size
          description: "Physical size of each image pixel at the sample surface, in
            nm or \xB5m. For large-area mosaic imaging, report the pixel size of individual
            tiles and the number and arrangement of tiles."
          type: object
          properties:
            '@id':
              const: ada:parameter/semImagingTAPP/imagePixelSizeDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: imagePixelSizeDefault
            schema:name:
              const: Image Pixel Size
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
              type: string
          required:
          - '@id'
          - '@type'
          - schema:valueName
          - schema:name
          - ada:dataType
          - ada:fieldScope
        - title: CL Wavelength Calibration Reference
          description: Reference light source or standard material used to calibrate
            the wavelength axis of the CL spectrometer. Required for quantitative
            spectral CL and hyperspectral mapping.
          type: object
          properties:
            '@id':
              const: ada:parameter/semImagingTAPP/clWavelengthCalibrationReferenceDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: clWavelengthCalibrationReferenceDefault
            schema:name:
              const: CL Wavelength Calibration Reference
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
      allOf:
      - contains:
          title: Chamber Pressure
          description: Chamber pressure and gas type during analysis. Required for
            variable pressure (VP-SEM) and environmental SEM (ESEM) modes. Report
            value and unit (Pa or Torr) and gas composition. Use 'None' for standard
            high-vacuum operation.
          type: object
          properties:
            '@id':
              const: ada:parameter/semImagingTAPP/chamberPressureDefault
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
            schema:defaultValue:
              anyOf:
              - type: number
              - type: string
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
          title: Image Pixel Size
          description: "Physical size of each image pixel at the sample surface, in
            nm or \xB5m. For large-area mosaic imaging, report the pixel size of individual
            tiles and the number and arrangement of tiles."
          type: object
          properties:
            '@id':
              const: ada:parameter/semImagingTAPP/imagePixelSizeDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: imagePixelSizeDefault
            schema:name:
              const: Image Pixel Size
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
          title: CL Wavelength Calibration Reference
          description: Reference light source or standard material used to calibrate
            the wavelength axis of the CL spectrometer. Required for quantitative
            spectral CL and hyperspectral mapping.
          type: object
          properties:
            '@id':
              const: ada:parameter/semImagingTAPP/clWavelengthCalibrationReferenceDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: clWavelengthCalibrationReferenceDefault
            schema:name:
              const: CL Wavelength Calibration Reference
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
    ada:dwellTimePerPixelDefault:
      description: Time the electron beam dwells on each pixel during raster scanning,
        or on each step position during mapping, in microseconds or milliseconds.
      anyOf:
      - type: number
      - type: string
    ada:clAcquisitionMode:
      description: 'CL data collection strategy. Panchromatic: total light intensity
        collected by PMT across the full detector wavelength range. Spectral point:
        full CL spectrum at discrete point locations. Hyperspectral map: full CL spectrum
        acquired at each pixel of a raster scan.'
      type: string
      enum:
      - Panchromatic
      - Monochromatic imaging
      - Spectral point
      - Hyperspectral map
      - Multi-channel pseudo-color
      - N/A
      - None
      - missing
      readOnly: true
    ada:clWavelengthRange:
      description: Detection wavelength range of the CL system in nm.
      anyOf:
      - type: number
      - type: string
      readOnly: true
    ada:clIntegrationTimeDefault:
      description: Acquisition time per pixel (hyperspectral map mode) or per spectrum
        (spectral point mode), in ms or s.
      anyOf:
      - type: number
      - type: string
    ada:sampleTiltAngle:
      description: Sample tilt angle for EBSD acquisition in degrees, measured from
        horizontal.
      anyOf:
      - type: number
      - type: string
      readOnly: true
    ada:ebsdStepSizeDefault:
      description: "Distance between adjacent EBSD measurement points in the map in
        nm or \xB5m. Must be smaller than the smallest grain of interest."
      anyOf:
      - type: number
      - type: string
    ada:ebsdPhaseListDefault:
      description: Mineral phases included in the EBSD reference pattern library for
        this procedure. Phases may be added for specific sample compositions beyond
        the expected suite for the target material.
      type: string
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
                  ada:ebsdIndexingMethod:
                    description: Algorithm used to index EBSD diffraction patterns
                      and assign crystal orientations. Hough-transform methods fit
                      Kikuchi band positions analytically; dictionary indexing (DI)
                      matches experimental patterns to a pre-computed library of simulated
                      patterns.
                    anyOf:
                    - type: string
                      enum:
                      - Hough transform
                      - Dictionary indexing (DI)
                      - Neural network
                      - Unknown
                      - N/A
                      - None
                      - missing
                      readOnly: true
                    - type: array
                      items:
                        type: string
                        enum:
                        - Hough transform
                        - Dictionary indexing (DI)
                        - Neural network
                        - Unknown
                        - N/A
                        - None
                        - missing
                        readOnly: true
                  schema:additionalProperty:
                    type: array
                    items:
                      anyOf:
                      - title: Crystal Structure Database
                        description: Crystal structure database used for EBSD phase
                          identification and Kikuchi pattern simulation.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/semImagingTAPP/crystalStructureDatabaseDefault
                          '@type':
                            const:
                            - schema:PropertyValueSpecification
                          schema:valueName:
                            const: crystalStructureDatabaseDefault
                          schema:name:
                            const: Crystal Structure Database
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
                        title: Crystal Structure Database
                        description: Crystal structure database used for EBSD phase
                          identification and Kikuchi pattern simulation.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/semImagingTAPP/crystalStructureDatabaseDefault
                          '@type':
                            const:
                            - schema:PropertyValueSpecification
                          schema:valueName:
                            const: crystalStructureDatabaseDefault
                          schema:name:
                            const: Crystal Structure Database
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
                required:
                - ada:ebsdIndexingMethod
          allOf:
          - contains:
              properties:
                schema:name:
                  const: Data reduction
              required:
              - schema:name
    dqv:hasQualityMeasurement:
      type: array
      items:
        type: object
        allOf:
        - if:
            properties:
              dqv:isMeasurementOf:
                const: EBSD Pattern Quality Threshold
            required:
            - dqv:isMeasurementOf
          then:
            properties:
              dqv:value:
                description: Minimum pattern quality or confidence index threshold
                  applied during EBSD data processing to exclude unreliably indexed
                  points from orientation maps. Include metric name and threshold
                  value.
                anyOf:
                - type: string
                - type: array
                  items:
                    type: string
    ada:analyticalMode:
      type: array
      items:
        type: string
        enum:
        - SE Imaging
        - BSE Imaging
        - CL Point Analysis
        - CL Mapping
        - EBSD
  required:
  - ada:ebsdDetectorConfiguration
  - ada:dwellTimePerPixelDefault
  - ada:clAcquisitionMode
  - ada:clWavelengthRange
  - ada:clIntegrationTimeDefault
  - ada:sampleTiltAngle
  - ada:ebsdStepSizeDefault
  - ada:ebsdPhaseListDefault

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Imaging/tapp/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Imaging/tapp/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Imaging/tapp/context.jsonld)

## Sources

* [SEM_Imaging_TAPP_v4.xlsx (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/SEM-Imaging/tapp`

