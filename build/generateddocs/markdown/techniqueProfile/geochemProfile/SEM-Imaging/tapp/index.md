
# SEM Imaging Technique-Aligned Protocol Profile (semImagingTAPP) (Schema)

`ogch.techniqueProfile.geochemProfile.SEM-Imaging.tapp` *v0.1*

Scanning electron microscopy imaging (SE/BSE/CL/EBSD) extension of the base TAPP definition. Basic protocol-tier fields are required top-level ada: properties; Advanced protocol-tier fields are schema:additionalProperty[] entries. No ada:analyteTemplate (imaging has no per-element analyte axis). Generated from docs/SEM_Imaging_TAPP_v4.xlsx by tools/build_tapp.py.

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
            "Carbonaceous nanoglobules, Tagish Lake (C2) meteorite (HCl/HF acid residue concentrate)"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "HCl and HF acid dissolution residue from pristine Tagish Lake pieces; deposited on lacey C TEM grid attached to Al-SEM stub; uncoated",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
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
  "ada:analyticalMode": [
    "SE Imaging"
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
  "ada:sampleTiltAngle": -9999,
  "ada:samplingUnit": "missing",
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
            "Carbonaceous nanoglobules, Tagish Lake (C2) meteorite (HCl/HF acid residue concentrate)"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "HCl and HF acid dissolution residue from pristine Tagish Lake pieces; deposited on lacey C TEM grid attached to Al-SEM stub; uncoated",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
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
  "ada:analyticalMode": [
    "SE Imaging"
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
  "ada:sampleTiltAngle": -9999,
  "ada:samplingUnit": "missing",
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

ex:semImagingTAPP-Garvie2008 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "HCl and HF acid dissolution residue from pristine Tagish Lake pieces; deposited on lacey C TEM grid attached to Al-SEM stub; uncoated" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "Sample imaged without coating; initial ~5% beam-induced shrinkage observed upon first e-beam exposure; sample stable thereafter; focusing performed away from particles of interest to minimise beam exposure" ;
    schema1:instrument <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "School of Earth and Space Exploration / School of Materials, Arizona State University" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semImaging" ;
            schema1:termCode "semImaging" ] ;
    schema1:name "semImaging protocol — Garvie2008" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Carbonaceous nanoglobules, Tagish Lake (C2) meteorite (HCl/HF acid residue concentrate)" ] ] ;
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
    ada:sampleTiltAngle -9999 ;
    ada:samplingUnit "missing" ;
    ada:targetSelectionCriteriaDefault "missing" .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:description "FIB-SEM dual-beam" ;
    schema1:hasPart <https://example.org/instrument/SEM/part/BSE-Detector>,
        <https://example.org/instrument/SEM/part/Electron-Source>,
        <https://example.org/instrument/SEM/part/SE-Detector> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "FEI / Thermo Fisher Scientific" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Nova 200 NanoLab DualBeam" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "500 V; 1 kV; 5 kV" ;
    ada:workingDistanceDefault "0.5–5.4 mm" .

<https://example.org/instrument/SEM/part/BSE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "BSE Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Unknown" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/SE-Detector> a schema1:Product,
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
  "schema:description": "semImagingTAPP instance derived from Genge et al. 2025 | Micrometeorite NG-1 (CV3-like) | BSE Imaging (ZEISS Sigma 1550VP, 10 kV) (publication column of SEM_Imaging_TAPP_v15.csv).",
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
            "Micrometeorite NG-1, Al-Cu-alloy-bearing, CV3-like composition; Democratic Republic of Congo"
          ]
        }
      ]
    }
  ],
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
      "schema:description": "VP-SEM / ESEM",
      "ada:acceleratingVoltageDefault": "10 kV",
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
  "ada:analyticalMode": [
    "BSE Imaging"
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
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
  "ada:samplingUnit": "missing",
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
  "schema:description": "semImagingTAPP instance derived from Genge et al. 2025 | Micrometeorite NG-1 (CV3-like) | BSE Imaging (ZEISS Sigma 1550VP, 10 kV) (publication column of SEM_Imaging_TAPP_v15.csv).",
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
            "Micrometeorite NG-1, Al-Cu-alloy-bearing, CV3-like composition; Democratic Republic of Congo"
          ]
        }
      ]
    }
  ],
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
      "schema:description": "VP-SEM / ESEM",
      "ada:acceleratingVoltageDefault": "10 kV",
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
  "ada:analyticalMode": [
    "BSE Imaging"
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
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
  "ada:samplingUnit": "missing",
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

ex:semImagingTAPP-Genge2025 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "semImagingTAPP instance derived from Genge et al. 2025 | Micrometeorite NG-1 (CV3-like) | BSE Imaging (ZEISS Sigma 1550VP, 10 kV) (publication column of SEM_Imaging_TAPP_v15.csv)." ;
    schema1:instrument <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "GPS Division Analytical Facility, California Institute of Technology" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semImaging" ;
            schema1:termCode "semImaging" ] ;
    schema1:name "semImaging protocol — Genge2025" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Micrometeorite NG-1, Al-Cu-alloy-bearing, CV3-like composition; Democratic Republic of Congo" ] ] ;
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
    ada:sampleTiltAngle -9999 ;
    ada:samplingUnit "missing" ;
    ada:targetSelectionCriteriaDefault "missing" .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:description "VP-SEM / ESEM" ;
    schema1:hasPart <https://example.org/instrument/SEM/part/BSE-Detector>,
        <https://example.org/instrument/SEM/part/Electron-Source>,
        <https://example.org/instrument/SEM/part/SE-Detector> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Zeiss" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "ZEISS 1550VP" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "10 kV" .

<https://example.org/instrument/SEM/part/BSE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "BSE Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Unknown" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/SE-Detector> a schema1:Product,
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
            "Micrometeorite NG-1, Al-Cu-alloy-bearing, CV3-like composition; Democratic Republic of Congo"
          ]
        }
      ]
    }
  ],
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
      "schema:description": "VP-SEM / ESEM",
      "ada:acceleratingVoltageDefault": "20 kV",
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
          "schema:Action"
        ],
        "schema:name": "Sample preparation",
        "schema:additionalType": [
          "bios:LabProcess"
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
            "schema:defaultValue": "ICSD (Inorganic Crystal Structure Database)"
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
  "ada:analyticalMode": [
    "EBSD"
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
  "ada:samplingUnit": "missing",
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
            "Micrometeorite NG-1, Al-Cu-alloy-bearing, CV3-like composition; Democratic Republic of Congo"
          ]
        }
      ]
    }
  ],
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
      "schema:description": "VP-SEM / ESEM",
      "ada:acceleratingVoltageDefault": "20 kV",
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
          "schema:Action"
        ],
        "schema:name": "Sample preparation",
        "schema:additionalType": [
          "bios:LabProcess"
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
            "schema:defaultValue": "ICSD (Inorganic Crystal Structure Database)"
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
  "ada:analyticalMode": [
    "EBSD"
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
  "ada:samplingUnit": "missing",
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

ex:semImagingTAPP-Genge2025-2 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semImagingTAPP/crystalStructureDatabaseDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semImagingTAPP/chamberPressureDefault> ;
    schema1:datePublished "missing" ;
    schema1:description "EBSD done in variable pressure mode (25 Pa) to suppress charging on tilted sample; spatial resolution ~30 nm stated; calibrated with single-crystal silicon standard" ;
    schema1:instrument <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "GPS Division Analytical Facility, California Institute of Technology" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semImaging" ;
            schema1:termCode "semImaging" ] ;
    schema1:name "semImaging protocol — Genge2025-2" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Micrometeorite NG-1, Al-Cu-alloy-bearing, CV3-like composition; Democratic Republic of Congo" ] ] ;
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
    ada:sampleTiltAngle "70 degrees" ;
    ada:samplingUnit "missing" ;
    ada:targetSelectionCriteriaDefault "missing" .

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

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:description "VP-SEM / ESEM" ;
    schema1:hasPart <https://example.org/instrument/SEM/part/BSE-Detector>,
        <https://example.org/instrument/SEM/part/Electron-Source>,
        <https://example.org/instrument/SEM/part/SE-Detector> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Zeiss" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "ZEISS 1550VP" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "20 kV" .

<https://example.org/instrument/SEM/part/BSE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "BSE Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Unknown" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/SE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SE Detector" ;
    schema1:name "missing" .


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
            "Forsterite grains from Kaba (CV3) carbonaceous chondrite thin section"
          ]
        }
      ]
    }
  ],
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
          "@id": "ex:instrument/SEM/part/Electron-Source"
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
      "schema:name": "example instrumentName"
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
  "ada:analyticalMode": [
    "CL Mapping"
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
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
  "ada:samplingUnit": "missing",
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
            "Forsterite grains from Kaba (CV3) carbonaceous chondrite thin section"
          ]
        }
      ]
    }
  ],
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
          "@id": "ex:instrument/SEM/part/Electron-Source"
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
      "schema:name": "example instrumentName"
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
  "ada:analyticalMode": [
    "CL Mapping"
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
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
  "ada:samplingUnit": "missing",
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

ex:semImagingTAPP-Gucsik2013 a cdi:Activity,
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
                    schema1:name "Data reduction" ;
                    schema1:position 2 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "CL color imaging also done with separate luminoscope ELM-3R (cold cathode, 10 kV, 0.5 mA, <100 Torr) — standalone CL system, not SEM-based; spectrum deconvolution via Peak Analyzer in OriginPro 8J SR2 Reported detail: ada:clAcquisitionMode = Panchromatic; Spectral point." ;
    schema1:instrument <https://example.org/instrument/SEM> ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semImaging" ;
            schema1:termCode "semImaging" ] ;
    schema1:name "semImaging protocol — Gucsik2013" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Forsterite grains from Kaba (CV3) carbonaceous chondrite thin section" ] ] ;
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
    ada:sampleTiltAngle -9999 ;
    ada:samplingUnit "missing" ;
    ada:targetSelectionCriteriaDefault "missing" .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semImagingTAPP/clDetectorConfiguration>,
        <https://ada.astromat.org/metadata/parameter/semImagingTAPP/clGrating> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:description "Standard SEM" ;
    schema1:hasPart <https://example.org/instrument/SEM/part/BSE-Detector>,
        <https://example.org/instrument/SEM/part/Electron-Source>,
        <https://example.org/instrument/SEM/part/SE-Detector> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "JEOL" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "JSM-5410LV" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/SEM/part/BSE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "BSE Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/SE-Detector> a schema1:Product,
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
            "Tagish Lake (C2) ungrouped carbonaceous chondrite; polished thin sections"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Carbon-coated polished thin sections; high vacuum analysis",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
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
      "schema:name": "example instrumentName"
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
  "ada:samplingUnit": "missing",
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
            "Tagish Lake (C2) ungrouped carbonaceous chondrite; polished thin sections"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Carbon-coated polished thin sections; high vacuum analysis",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
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
      "schema:name": "example instrumentName"
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
  "ada:samplingUnit": "missing",
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

ex:semImagingTAPP-Izawa2010 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Carbon-coated polished thin sections; high vacuum analysis" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semImagingTAPP/chamberPressureDefault> ;
    schema1:datePublished "missing" ;
    schema1:description "Digiscan II beam controller used for CL raster; multi-channel color CL distinguishes ~4 spectral bands; beam-induced CL may persist from long-lived IR emission in carbonates" ;
    schema1:instrument <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Zircon and Accessory Phase Laboratory, University of Western Ontario" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semImaging" ;
            schema1:termCode "semImaging" ] ;
    schema1:name "semImaging protocol — Izawa2010" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Tagish Lake (C2) ungrouped carbonaceous chondrite; polished thin sections" ] ] ;
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
    ada:sampleTiltAngle -9999 ;
    ada:samplingUnit "missing" ;
    ada:targetSelectionCriteriaDefault "missing" ;
    bios:computationalTool [ schema1:name "Gatan DigitalMicrograph" ;
            ada:toolRole "dataReduction" ],
        [ schema1:name "Gatan DigitalMicrograph (CL image assembly)" ;
            ada:toolRole "acquisition" ] .

<https://ada.astromat.org/metadata/parameter/semImagingTAPP/chamberPressureDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "High vacuum" ;
    schema1:name "Chamber Pressure" ;
    schema1:valueName "chamberPressureDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semImagingTAPP/clDetectorConfiguration> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:description "Standard SEM" ;
    schema1:hasPart <https://example.org/instrument/SEM/part/BSE-Detector>,
        <https://example.org/instrument/SEM/part/Electron-Source>,
        <https://example.org/instrument/SEM/part/SE-Detector> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Hitachi" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "S-2500C" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "15–20 kV" ;
    ada:workingDistanceDefault "~10 mm" .

<https://example.org/instrument/SEM/part/BSE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "BSE Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Tungsten (W)" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/SE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SE Detector" ;
    schema1:name "missing" .

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
  "schema:description": "semImagingTAPP instance derived from Izawa et al. 2010 | Tagish Lake (C2) meteorite | BSE Imaging (Leo 440) (publication column of SEM_Imaging_TAPP_v15.csv).",
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
            "Tagish Lake (C2) ungrouped carbonaceous chondrite; polished thin sections"
          ]
        }
      ]
    }
  ],
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
          "@id": "ex:instrument/SEM/part/Electron-Source"
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
      "schema:name": "example instrumentName"
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
  "ada:analyticalMode": [
    "BSE Imaging"
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
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
  "ada:samplingUnit": "missing",
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
  "schema:description": "semImagingTAPP instance derived from Izawa et al. 2010 | Tagish Lake (C2) meteorite | BSE Imaging (Leo 440) (publication column of SEM_Imaging_TAPP_v15.csv).",
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
            "Tagish Lake (C2) ungrouped carbonaceous chondrite; polished thin sections"
          ]
        }
      ]
    }
  ],
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
          "@id": "ex:instrument/SEM/part/Electron-Source"
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
      "schema:name": "example instrumentName"
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
  "ada:analyticalMode": [
    "BSE Imaging"
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
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
  "ada:samplingUnit": "missing",
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

ex:semImagingTAPP-Izawa2010-2 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "semImagingTAPP instance derived from Izawa et al. 2010 | Tagish Lake (C2) meteorite | BSE Imaging (Leo 440) (publication column of SEM_Imaging_TAPP_v15.csv)." ;
    schema1:instrument <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Surface Science Western" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semImaging" ;
            schema1:termCode "semImaging" ] ;
    schema1:name "semImaging protocol — Izawa2010-2" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Tagish Lake (C2) ungrouped carbonaceous chondrite; polished thin sections" ] ] ;
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
    ada:sampleTiltAngle -9999 ;
    ada:samplingUnit "missing" ;
    ada:targetSelectionCriteriaDefault "missing" .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:description "Standard SEM" ;
    schema1:hasPart <https://example.org/instrument/SEM/part/BSE-Detector>,
        <https://example.org/instrument/SEM/part/Electron-Source>,
        <https://example.org/instrument/SEM/part/SE-Detector> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Zeiss" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Leo 440" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/SEM/part/BSE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "BSE Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/SE-Detector> a schema1:Product,
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
  "schema:description": "semImagingTAPP instance derived from Izawa et al. 2010 | Tagish Lake (C2) meteorite | BSE Imaging (Leo 1540 FIB/SEM CrossBeam) (publication column of SEM_Imaging_TAPP_v15.csv).",
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
            "Tagish Lake (C2) ungrouped carbonaceous chondrite; polished thin sections"
          ]
        }
      ]
    }
  ],
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
      "schema:name": "example instrumentName"
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
  "ada:analyticalMode": [
    "BSE Imaging"
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
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
  "ada:samplingUnit": "missing",
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
  "schema:description": "semImagingTAPP instance derived from Izawa et al. 2010 | Tagish Lake (C2) meteorite | BSE Imaging (Leo 1540 FIB/SEM CrossBeam) (publication column of SEM_Imaging_TAPP_v15.csv).",
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
            "Tagish Lake (C2) ungrouped carbonaceous chondrite; polished thin sections"
          ]
        }
      ]
    }
  ],
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
      "schema:name": "example instrumentName"
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
  "ada:analyticalMode": [
    "BSE Imaging"
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
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
  "ada:samplingUnit": "missing",
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

ex:semImagingTAPP-Izawa2010-3 a cdi:Activity,
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
                    schema1:name "Data reduction" ;
                    schema1:position 2 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "semImagingTAPP instance derived from Izawa et al. 2010 | Tagish Lake (C2) meteorite | BSE Imaging (Leo 1540 FIB/SEM CrossBeam) (publication column of SEM_Imaging_TAPP_v15.csv)." ;
    schema1:instrument <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Nanofabrication Laboratory, University of Western Ontario" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semImaging" ;
            schema1:termCode "semImaging" ] ;
    schema1:name "semImaging protocol — Izawa2010-3" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Tagish Lake (C2) ungrouped carbonaceous chondrite; polished thin sections" ] ] ;
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
    ada:sampleTiltAngle -9999 ;
    ada:samplingUnit "missing" ;
    ada:targetSelectionCriteriaDefault "missing" .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:description "FIB-SEM dual-beam" ;
    schema1:hasPart <https://example.org/instrument/SEM/part/BSE-Detector>,
        <https://example.org/instrument/SEM/part/Electron-Source>,
        <https://example.org/instrument/SEM/part/SE-Detector> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Zeiss" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Leo 1540 FIB/SEM CrossBeam" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/SEM/part/BSE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "BSE Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Unknown" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/SE-Detector> a schema1:Product,
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
            "High-rank coal (anthracite from Bofang Mine; lean coal from Yuwu Mine), southern Qinshui basin, China"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Bulk coal polished to ~10 mm × 2-3 mm using polishing and burnishing machine; further polished with cross section polisher; thin gold coating applied by sputtering",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
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
      "schema:description": "N/A",
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
          "@id": "ex:instrument/SEM/part/Electron-Source"
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
      "schema:name": "example instrumentName"
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
  "ada:analyticalMode": [
    "SE Imaging"
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
  "ada:sampleTiltAngle": -9999,
  "ada:samplingUnit": "missing",
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
            "High-rank coal (anthracite from Bofang Mine; lean coal from Yuwu Mine), southern Qinshui basin, China"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Bulk coal polished to ~10 mm \u00d7 2-3 mm using polishing and burnishing machine; further polished with cross section polisher; thin gold coating applied by sputtering",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
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
      "schema:description": "N/A",
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
          "@id": "ex:instrument/SEM/part/Electron-Source"
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
      "schema:name": "example instrumentName"
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
  "ada:analyticalMode": [
    "SE Imaging"
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
  "ada:sampleTiltAngle": -9999,
  "ada:samplingUnit": "missing",
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

ex:semImagingTAPP-Liu2017 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Bulk coal polished to ~10 mm × 2-3 mm using polishing and burnishing machine; further polished with cross section polisher; thin gold coating applied by sputtering" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semImagingTAPP/chamberPressureDefault> ;
    schema1:datePublished "missing" ;
    schema1:description "Pore and mineral sizes >0.1 µm measured; minerals analyzed via EDS (surface energy spectrum analysis); magnification range 10³ to 10⁴" ;
    schema1:instrument <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "China University of Mining and Technology, Xuzhou, China" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semImaging" ;
            schema1:termCode "semImaging" ] ;
    schema1:name "semImaging protocol — Liu2017" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "High-rank coal (anthracite from Bofang Mine; lean coal from Yuwu Mine), southern Qinshui basin, China" ] ] ;
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
    ada:sampleTiltAngle -9999 ;
    ada:samplingUnit "missing" ;
    ada:targetSelectionCriteriaDefault "missing" .

<https://ada.astromat.org/metadata/parameter/semImagingTAPP/chamberPressureDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "High vacuum" ;
    schema1:name "Chamber Pressure" ;
    schema1:valueName "chamberPressureDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:description "N/A" ;
    schema1:hasPart <https://example.org/instrument/SEM/part/BSE-Detector>,
        <https://example.org/instrument/SEM/part/Electron-Source>,
        <https://example.org/instrument/SEM/part/SE-Detector> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Unknown" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Quanta 250" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/SEM/part/BSE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "BSE Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/SE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SE Detector" ;
    schema1:name "missing" .


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
            "High-rank coal (anthracite from Bofang Mine; lean coal from Yuwu Mine), southern Qinshui basin, China"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Bulk coal polished to ~10 mm × 2-3 mm using polishing and burnishing machine; further polished with cross section polisher; thin gold coating applied by sputtering",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
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
      "schema:description": "N/A",
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
  "ada:analyticalMode": [
    "SE Imaging"
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
  "ada:sampleTiltAngle": -9999,
  "ada:samplingUnit": "missing",
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
            "High-rank coal (anthracite from Bofang Mine; lean coal from Yuwu Mine), southern Qinshui basin, China"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Bulk coal polished to ~10 mm \u00d7 2-3 mm using polishing and burnishing machine; further polished with cross section polisher; thin gold coating applied by sputtering",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
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
      "schema:description": "N/A",
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
  "ada:analyticalMode": [
    "SE Imaging"
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
  "ada:sampleTiltAngle": -9999,
  "ada:samplingUnit": "missing",
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

ex:semImagingTAPP-Liu2017-2 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Bulk coal polished to ~10 mm × 2-3 mm using polishing and burnishing machine; further polished with cross section polisher; thin gold coating applied by sputtering" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semImagingTAPP/chamberPressureDefault> ;
    schema1:datePublished "missing" ;
    schema1:description "Pore and mineral sizes >20 nm to <5 µm measured; EDS also used for mineral analysis; magnification range 10³ to 10⁵" ;
    schema1:instrument <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "China University of Mining and Technology, Xuzhou, China" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semImaging" ;
            schema1:termCode "semImaging" ] ;
    schema1:name "semImaging protocol — Liu2017-2" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "High-rank coal (anthracite from Bofang Mine; lean coal from Yuwu Mine), southern Qinshui basin, China" ] ] ;
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
    ada:sampleTiltAngle -9999 ;
    ada:samplingUnit "missing" ;
    ada:targetSelectionCriteriaDefault "missing" .

<https://ada.astromat.org/metadata/parameter/semImagingTAPP/chamberPressureDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "High vacuum" ;
    schema1:name "Chamber Pressure" ;
    schema1:valueName "chamberPressureDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:description "N/A" ;
    schema1:hasPart <https://example.org/instrument/SEM/part/BSE-Detector>,
        <https://example.org/instrument/SEM/part/Electron-Source>,
        <https://example.org/instrument/SEM/part/SE-Detector> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Zeiss" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "SUPRA 55" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/SEM/part/BSE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "BSE Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Unknown" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/SE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SE Detector" ;
    schema1:name "missing" .


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
            "Khatyrka CV3 carbonaceous chondrite; Al-Cu-Fe alloy metal phases (hollisterite, kryachkoite, stolperite, khatyrkite, icosahedrite) in section 126A"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished thin section (section 126A prepared from Grain 126); no coating or SEM-specific preparation stated",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
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
      "schema:name": "example instrumentName"
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
  "ada:analyticalMode": [
    "BSE Imaging"
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
  "ada:sampleTiltAngle": -9999,
  "ada:samplingUnit": "missing",
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
            "Khatyrka CV3 carbonaceous chondrite; Al-Cu-Fe alloy metal phases (hollisterite, kryachkoite, stolperite, khatyrkite, icosahedrite) in section 126A"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished thin section (section 126A prepared from Grain 126); no coating or SEM-specific preparation stated",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
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
      "schema:name": "example instrumentName"
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
  "ada:analyticalMode": [
    "BSE Imaging"
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
  "ada:sampleTiltAngle": -9999,
  "ada:samplingUnit": "missing",
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

ex:semImagingTAPP-Ma2017 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Polished thin section (section 126A prepared from Grain 126); no coating or SEM-specific preparation stated" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "BSE images obtained from both ZEISS 1550VP FE-SEM and JEOL 8200 electron microprobe (EPMA); quantitative EPMA on JEOL 8200 at 12 kV, 5 nA (out of scope for SEM TAPP)" ;
    schema1:instrument <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Caltech GPS Analytical Facility, California Institute of Technology, Pasadena, CA, USA" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semImaging" ;
            schema1:termCode "semImaging" ] ;
    schema1:name "semImaging protocol — Ma2017" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Khatyrka CV3 carbonaceous chondrite; Al-Cu-Fe alloy metal phases (hollisterite, kryachkoite, stolperite, khatyrkite, icosahedrite) in section 126A" ] ] ;
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
    ada:sampleTiltAngle -9999 ;
    ada:samplingUnit "missing" ;
    ada:targetSelectionCriteriaDefault "missing" .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:description "N/A" ;
    schema1:hasPart <https://example.org/instrument/SEM/part/BSE-Detector>,
        <https://example.org/instrument/SEM/part/Electron-Source>,
        <https://example.org/instrument/SEM/part/SE-Detector> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Zeiss" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "1550VP" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/SEM/part/BSE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "BSE Detector" ;
    schema1:name "N/A" .

<https://example.org/instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Unknown" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/SE-Detector> a schema1:Product,
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
            "Khatyrka CV3 carbonaceous chondrite; Al-Cu-Fe alloy metal phases (hollisterite, kryachkoite, stolperite, khatyrkite, icosahedrite) in section 126A"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished thin section (section 126A prepared from Grain 126); no coating or EBSD-specific preparation stated",
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
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
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
      "schema:description": "N/A",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:ebsdPhaseListDefault": "Hollisterite (C2/m FeAl3); kryachkoite (Cmc21 (Al,Cu)Fe6); stolperite (Pm3m AlCu)",
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
  "ada:analyticalMode": [
    "EBSD"
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
  "ada:samplingUnit": "missing",
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
            "Khatyrka CV3 carbonaceous chondrite; Al-Cu-Fe alloy metal phases (hollisterite, kryachkoite, stolperite, khatyrkite, icosahedrite) in section 126A"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished thin section (section 126A prepared from Grain 126); no coating or EBSD-specific preparation stated",
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
          "schema:Action"
        ],
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
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
      "schema:description": "N/A",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:ebsdPhaseListDefault": "Hollisterite (C2/m FeAl3); kryachkoite (Cmc21 (Al,Cu)Fe6); stolperite (Pm3m AlCu)",
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
  "ada:analyticalMode": [
    "EBSD"
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
  "ada:samplingUnit": "missing",
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

ex:semImagingTAPP-Ma2017-2 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Polished thin section (section 126A prepared from Grain 126); no coating or EBSD-specific preparation stated" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semImagingTAPP/crystalStructureDatabaseDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "EBSD performed at Caltech GPS Analytical Facility; EPMA (JEOL 8200) used for quantitative chemical analysis (out of scope for SEM TAPP)" ;
    schema1:instrument <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Caltech GPS Analytical Facility, California Institute of Technology, Pasadena, CA, USA" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semImaging" ;
            schema1:termCode "semImaging" ] ;
    schema1:name "semImaging protocol — Ma2017-2" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Khatyrka CV3 carbonaceous chondrite; Al-Cu-Fe alloy metal phases (hollisterite, kryachkoite, stolperite, khatyrkite, icosahedrite) in section 126A" ] ] ;
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
    ada:sampleTiltAngle -9999 ;
    ada:samplingUnit "missing" ;
    ada:targetSelectionCriteriaDefault "missing" .

<https://ada.astromat.org/metadata/parameter/semImagingTAPP/crystalStructureDatabaseDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Literature crystal structures: Black et al. 1961 (Cmc21 (Al,Cu)Fe6 for kryachkoite); Zhang et al. 2005 (Pm3m AlCu for stolperite)" ;
    schema1:name "Crystal Structure Database" ;
    schema1:valueName "crystalStructureDatabaseDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:description "N/A" ;
    schema1:hasPart <https://example.org/instrument/SEM/part/BSE-Detector>,
        <https://example.org/instrument/SEM/part/Electron-Source>,
        <https://example.org/instrument/SEM/part/SE-Detector> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Zeiss" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "1550VP" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/SEM/part/BSE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "BSE Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Unknown" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/SE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SE Detector" ;
    schema1:name "missing" .


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
            "NWA 7317 CR6 carbonaceous chondrite; polished slab (~10×6 mm fragment, 10.01g)"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Embedded in epoxy, polished to ¼ µm level, sputtered with 30-nm-thick carbon film",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
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
      "ada:acceleratingVoltageDefault": "20 kV",
      "ada:workingDistanceDefault": "8 mm",
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
  "bios:computationalTool": [
    {
      "ada:toolRole": "acquisition",
      "schema:name": "Oxford INCA Energy"
    }
  ],
  "ada:analyticalMode": [
    "BSE Imaging"
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
  "ada:sampleTiltAngle": -9999,
  "ada:samplingUnit": "missing",
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
            "NWA 7317 CR6 carbonaceous chondrite; polished slab (~10\u00d76 mm fragment, 10.01g)"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Embedded in epoxy, polished to \u00bc \u00b5m level, sputtered with 30-nm-thick carbon film",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
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
      "ada:acceleratingVoltageDefault": "20 kV",
      "ada:workingDistanceDefault": "8 mm",
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
  "bios:computationalTool": [
    {
      "ada:toolRole": "acquisition",
      "schema:name": "Oxford INCA Energy"
    }
  ],
  "ada:analyticalMode": [
    "BSE Imaging"
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
  "ada:sampleTiltAngle": -9999,
  "ada:samplingUnit": "missing",
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

ex:semImagingTAPP-Pascucci2026 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Embedded in epoxy, polished to ¼ µm level, sputtered with 30-nm-thick carbon film" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semImagingTAPP/chamberPressureDefault> ;
    schema1:datePublished "missing" ;
    schema1:description "10 BSE images acquired at ×138 magnification and mosaicked (4 consecutive per row) to cover ~9.7 mm area matching SPIM imagery" ;
    schema1:instrument <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "CNR IMAA (Institute of Methodologies for Environmental Analysis), Italian National Research Council, Potenza, Italy" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semImaging" ;
            schema1:termCode "semImaging" ] ;
    schema1:name "semImaging protocol — Pascucci2026" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "NWA 7317 CR6 carbonaceous chondrite; polished slab (~10×6 mm fragment, 10.01g)" ] ] ;
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
    ada:sampleTiltAngle -9999 ;
    ada:samplingUnit "missing" ;
    ada:targetSelectionCriteriaDefault "missing" ;
    bios:computationalTool [ schema1:name "Oxford INCA Energy" ;
            ada:toolRole "acquisition" ] .

<https://ada.astromat.org/metadata/parameter/semImagingTAPP/chamberPressureDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "High vacuum" ;
    schema1:name "Chamber Pressure" ;
    schema1:valueName "chamberPressureDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:description "N/A" ;
    schema1:hasPart <https://example.org/instrument/SEM/part/BSE-Detector>,
        <https://example.org/instrument/SEM/part/Electron-Source>,
        <https://example.org/instrument/SEM/part/SE-Detector> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Zeiss" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Supra 40" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "20 kV" ;
    ada:workingDistanceDefault "8 mm" .

<https://example.org/instrument/SEM/part/BSE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "BSE Detector" ;
    schema1:name "N/A" .

<https://example.org/instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Unknown" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/SE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SE Detector" ;
    schema1:name "missing" .


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
            "NWA 7317 CR6 carbonaceous chondrite; polished slab (~10×6 mm fragment, 10.01g)"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Embedded in epoxy, polished to ¼ µm level, sputtered with 30-nm-thick carbon film",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
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
      "schema:description": "N/A",
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
  "ada:analyticalMode": [
    "SE Imaging"
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
  "ada:sampleTiltAngle": -9999,
  "ada:samplingUnit": "missing",
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
            "NWA 7317 CR6 carbonaceous chondrite; polished slab (~10\u00d76 mm fragment, 10.01g)"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Embedded in epoxy, polished to \u00bc \u00b5m level, sputtered with 30-nm-thick carbon film",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
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
      "schema:description": "N/A",
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
  "ada:analyticalMode": [
    "SE Imaging"
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
  "ada:sampleTiltAngle": -9999,
  "ada:samplingUnit": "missing",
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

ex:semImagingTAPP-Pascucci2026-2 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Embedded in epoxy, polished to ¼ µm level, sputtered with 30-nm-thick carbon film" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "SE imaging used for topographic examination; instrument capability: up to ×200,000 magnification, 5 nm resolution; SE acquired before EDS to minimize charging effects" ;
    schema1:instrument <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "CNR IMAA (Institute of Methodologies for Environmental Analysis), Italian National Research Council, Potenza, Italy" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semImaging" ;
            schema1:termCode "semImaging" ] ;
    schema1:name "semImaging protocol — Pascucci2026-2" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "NWA 7317 CR6 carbonaceous chondrite; polished slab (~10×6 mm fragment, 10.01g)" ] ] ;
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
    ada:sampleTiltAngle -9999 ;
    ada:samplingUnit "missing" ;
    ada:targetSelectionCriteriaDefault "missing" .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:description "N/A" ;
    schema1:hasPart <https://example.org/instrument/SEM/part/BSE-Detector>,
        <https://example.org/instrument/SEM/part/Electron-Source>,
        <https://example.org/instrument/SEM/part/SE-Detector> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Zeiss" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Supra 40" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/SEM/part/BSE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "BSE Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Unknown" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/SE-Detector> a schema1:Product,
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
            "Asteroid (101955) Bennu particles (OSIRIS-REx sample return); hummocky and angular particles"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Attached to Al cylinder SEM mount with double-sided C tape; sputter coated with ~5 nm carbon",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
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
      "ada:acceleratingVoltageDefault": "15 kV",
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
  "bios:computationalTool": [
    {
      "ada:toolRole": "acquisition",
      "schema:name": "Oxford AZtec (Point & ID programme)"
    }
  ],
  "ada:analyticalMode": [
    "BSE Imaging"
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
  "ada:sampleTiltAngle": -9999,
  "ada:samplingUnit": "missing",
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
            "Asteroid (101955) Bennu particles (OSIRIS-REx sample return); hummocky and angular particles"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Attached to Al cylinder SEM mount with double-sided C tape; sputter coated with ~5 nm carbon",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
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
      "ada:acceleratingVoltageDefault": "15 kV",
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
  "bios:computationalTool": [
    {
      "ada:toolRole": "acquisition",
      "schema:name": "Oxford AZtec (Point & ID programme)"
    }
  ],
  "ada:analyticalMode": [
    "BSE Imaging"
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
  "ada:sampleTiltAngle": -9999,
  "ada:samplingUnit": "missing",
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

ex:semImagingTAPP-Zega2025 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Attached to Al cylinder SEM mount with double-sided C tape; sputter coated with ~5 nm carbon" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "SE and BSE imaging; EDS point spectra; Oxford AZtec system; EDS detector: Oxford Instruments Ultim Max SDD 170 mm²" ;
    schema1:instrument <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "NASA Johnson Space Center (JSC), Houston, TX, USA" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semImaging" ;
            schema1:termCode "semImaging" ] ;
    schema1:name "semImaging protocol — Zega2025" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Asteroid (101955) Bennu particles (OSIRIS-REx sample return); hummocky and angular particles" ] ] ;
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
    ada:sampleTiltAngle -9999 ;
    ada:samplingUnit "missing" ;
    ada:targetSelectionCriteriaDefault "missing" ;
    bios:computationalTool [ schema1:name "Oxford AZtec (Point & ID programme)" ;
            ada:toolRole "acquisition" ] .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:hasPart <https://example.org/instrument/SEM/part/BSE-Detector>,
        <https://example.org/instrument/SEM/part/Electron-Source>,
        <https://example.org/instrument/SEM/part/SE-Detector> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "JEOL" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "7600F" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "15 kV" .

<https://example.org/instrument/SEM/part/BSE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "BSE Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Unknown" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/SE-Detector> a schema1:Product,
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
            "Asteroid (101955) Bennu particles (OSIRIS-REx sample return); polished sections"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished sections; coated with 0.1 nm carbon for charge mitigation",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
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
      "schema:name": "example instrumentName"
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
  "ada:analyticalMode": [
    "SE Imaging"
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
  "ada:sampleTiltAngle": -9999,
  "ada:samplingUnit": "missing",
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
            "Asteroid (101955) Bennu particles (OSIRIS-REx sample return); polished sections"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished sections; coated with 0.1 nm carbon for charge mitigation",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
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
      "schema:name": "example instrumentName"
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
  "ada:analyticalMode": [
    "SE Imaging"
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
  "ada:sampleTiltAngle": -9999,
  "ada:samplingUnit": "missing",
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

ex:semImagingTAPP-Zega2025-2 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Polished sections; coated with 0.1 nm carbon for charge mitigation" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "Cold FEG; system range 0.5-30 keV; SE and BSE imaging detectors; also equipped with Oxford Instruments Aztec Live/x-stream/Ultimax 170 SDD EDS; specific operating voltage not stated" ;
    schema1:instrument <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "K-ALFAA (Kuiper-Arizona Laboratory for Astromaterials Analysis), University of Arizona" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semImaging" ;
            schema1:termCode "semImaging" ] ;
    schema1:name "semImaging protocol — Zega2025-2" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Asteroid (101955) Bennu particles (OSIRIS-REx sample return); polished sections" ] ] ;
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
    ada:sampleTiltAngle -9999 ;
    ada:samplingUnit "missing" ;
    ada:targetSelectionCriteriaDefault "missing" .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:hasPart <https://example.org/instrument/SEM/part/BSE-Detector>,
        <https://example.org/instrument/SEM/part/Electron-Source>,
        <https://example.org/instrument/SEM/part/SE-Detector> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Hitachi" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "S-4800" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/SEM/part/BSE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "BSE Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Unknown" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/SE-Detector> a schema1:Product,
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
            "Asteroid (101955) Bennu particles (OSIRIS-REx sample return); polished sections"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished sections; coated with 0.1 nm carbon for charge mitigation",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
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
      "schema:name": "example instrumentName"
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
  "ada:analyticalMode": [
    "BSE Imaging"
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
  "ada:sampleTiltAngle": -9999,
  "ada:samplingUnit": "missing",
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
            "Asteroid (101955) Bennu particles (OSIRIS-REx sample return); polished sections"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished sections; coated with 0.1 nm carbon for charge mitigation",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
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
      "schema:name": "example instrumentName"
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
  "ada:analyticalMode": [
    "BSE Imaging"
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
  "ada:sampleTiltAngle": -9999,
  "ada:samplingUnit": "missing",
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

ex:semImagingTAPP-Zega2025-3 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Polished sections; coated with 0.1 nm carbon for charge mitigation" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "Cold FEG; system range 0.5-30 keV; SE and BSE imaging; EDS mapping; specific operating voltage not stated" ;
    schema1:instrument <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "K-ALFAA (Kuiper-Arizona Laboratory for Astromaterials Analysis), University of Arizona" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semImaging" ;
            schema1:termCode "semImaging" ] ;
    schema1:name "semImaging protocol — Zega2025-3" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Asteroid (101955) Bennu particles (OSIRIS-REx sample return); polished sections" ] ] ;
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
    ada:sampleTiltAngle -9999 ;
    ada:samplingUnit "missing" ;
    ada:targetSelectionCriteriaDefault "missing" .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:hasPart <https://example.org/instrument/SEM/part/BSE-Detector>,
        <https://example.org/instrument/SEM/part/Electron-Source>,
        <https://example.org/instrument/SEM/part/SE-Detector> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Hitachi" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "S-4800" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/SEM/part/BSE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "BSE Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Unknown" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/SE-Detector> a schema1:Product,
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
            "Asteroid (101955) Bennu particles (OSIRIS-REx sample return); olivine and carbonate grains"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished thin sections; ~100 nm graphite coating (as stated in CL emitting volume calculation)",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
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
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:clAcquisitionMode": "Panchromatic",
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
  "ada:analyticalMode": [
    "CL Mapping"
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
  "ada:clIntegrationTimeDefault": -9999,
  "ada:clWavelengthRange": -9999,
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:ebsdDetectorConfiguration": "missing",
  "ada:ebsdPhaseListDefault": "missing",
  "ada:ebsdStepSizeDefault": -9999,
  "ada:sampleTiltAngle": -9999,
  "ada:samplingUnit": "missing",
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
            "Asteroid (101955) Bennu particles (OSIRIS-REx sample return); olivine and carbonate grains"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Polished thin sections; ~100 nm graphite coating (as stated in CL emitting volume calculation)",
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
      }
    ],
    "@type": [
      "schema:HowTo"
    ]
  },
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
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    }
  ],
  "ada:clAcquisitionMode": "Panchromatic",
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
  "ada:analyticalMode": [
    "CL Mapping"
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
  "ada:clIntegrationTimeDefault": -9999,
  "ada:clWavelengthRange": -9999,
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:ebsdDetectorConfiguration": "missing",
  "ada:ebsdPhaseListDefault": "missing",
  "ada:ebsdStepSizeDefault": -9999,
  "ada:sampleTiltAngle": -9999,
  "ada:samplingUnit": "missing",
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

ex:semImagingTAPP-Zega2025-4 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Polished thin sections; ~100 nm graphite coating (as stated in CL emitting volume calculation)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "CL emitting volume at 5 keV: up to 230 nm depth, 200 nm sideways (assuming 100-nm graphite coating); recording below focal plane for magnifications <×500 to minimize hotspot effect Reported detail: ada:clAcquisitionMode = Panchromatic imaging; hyperspectral analysis; monochromatic imaging." ;
    schema1:instrument <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Université Côte d'Azur / Observatoire de la Côte d'Azur, Valbonne, France" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semImaging" ;
            schema1:termCode "semImaging" ] ;
    schema1:name "semImaging protocol — Zega2025-4" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Asteroid (101955) Bennu particles (OSIRIS-REx sample return); olivine and carbonate grains" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "BSE/EDS (JEOL 7600F, JSC); SE/BSE/EDS (Hitachi S-4800, U Arizona)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "CL Mapping" ;
    ada:clAcquisitionMode "Panchromatic" ;
    ada:clIntegrationTimeDefault -9999 ;
    ada:clWavelengthRange -9999 ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:ebsdDetectorConfiguration "missing" ;
    ada:ebsdPhaseListDefault "missing" ;
    ada:ebsdStepSizeDefault -9999 ;
    ada:sampleTiltAngle -9999 ;
    ada:samplingUnit "missing" ;
    ada:targetSelectionCriteriaDefault "missing" .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semImagingTAPP/clDetectorConfiguration> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:hasPart <https://example.org/instrument/SEM/part/BSE-Detector>,
        <https://example.org/instrument/SEM/part/Electron-Source>,
        <https://example.org/instrument/SEM/part/SE-Detector> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "JEOL" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "JSM-7000F" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "5 keV" .

<https://example.org/instrument/SEM/part/BSE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "BSE Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Unknown" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/SE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SE Detector" ;
    schema1:name "missing" .

<https://ada.astromat.org/metadata/parameter/semImagingTAPP/clDetectorConfiguration> a schema1:PropertyValue ;
    schema1:name "CL Detector Configuration" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semImagingTAPP/clDetectorConfiguration> ;
    schema1:value "MonoCL4 GATAN monochromator; high-sensitivity array detector and photomultiplier; paraboloidal mirror collection (CRHEA Valbonne, France)" .


```


### semImagingTAPP example Barnes2025
semImagingTAPP instance derived from Barnes et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | BSE Imaging (FEI Quanta 3D DualBeam + Helios DualBeam, NASA JSC).
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
  "@id": "ex:semImagingTAPP-Barnes2025",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semImaging protocol — Barnes2025",
  "schema:description": "No BSE imaging with FEI Quanta 3D DualBeam or Helios DualBeam at NASA JSC described in this paper (Barnes et al. 2025). BSE mosaic imaging was performed using a Hitachi TM4000plus at the University of Arizona (K-ALFAA) at 15-keV electron beam to identify suitable matrix areas for NanoSIMS analysis (Methods, p.11). No JSC BSE imaging conditions or instrument stated.",
  "ada:analyticalMode": [
    "BSE Imaging"
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
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
          "@id": "ex:instrument/SEM/part/Electron-Source"
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
      ]
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
  "ada:samplingUnit": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Imaging/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semImagingTAPP-Barnes2025",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semImaging protocol \u2014 Barnes2025",
  "schema:description": "No BSE imaging with FEI Quanta 3D DualBeam or Helios DualBeam at NASA JSC described in this paper (Barnes et al. 2025). BSE mosaic imaging was performed using a Hitachi TM4000plus at the University of Arizona (K-ALFAA) at 15-keV electron beam to identify suitable matrix areas for NanoSIMS analysis (Methods, p.11). No JSC BSE imaging conditions or instrument stated.",
  "ada:analyticalMode": [
    "BSE Imaging"
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
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
          "@id": "ex:instrument/SEM/part/Electron-Source"
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
      ]
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
  "ada:samplingUnit": "missing",
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

ex:semImagingTAPP-Barnes2025 a cdi:Activity,
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
                    schema1:name "Data reduction" ;
                    schema1:position 2 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "No BSE imaging with FEI Quanta 3D DualBeam or Helios DualBeam at NASA JSC described in this paper (Barnes et al. 2025). BSE mosaic imaging was performed using a Hitachi TM4000plus at the University of Arizona (K-ALFAA) at 15-keV electron beam to identify suitable matrix areas for NanoSIMS analysis (Methods, p.11). No JSC BSE imaging conditions or instrument stated." ;
    schema1:instrument <https://example.org/instrument/SEM> ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semImaging" ;
            schema1:termCode "semImaging" ] ;
    schema1:name "semImaging protocol — Barnes2025" ;
    ada:analyticalMode "BSE Imaging" ;
    ada:clAcquisitionMode "missing" ;
    ada:clIntegrationTimeDefault -9999 ;
    ada:clWavelengthRange -9999 ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:ebsdDetectorConfiguration "missing" ;
    ada:ebsdPhaseListDefault "missing" ;
    ada:ebsdStepSizeDefault -9999 ;
    ada:sampleTiltAngle -9999 ;
    ada:samplingUnit "missing" ;
    ada:targetSelectionCriteriaDefault "missing" .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:hasPart <https://example.org/instrument/SEM/part/BSE-Detector>,
        <https://example.org/instrument/SEM/part/Electron-Source>,
        <https://example.org/instrument/SEM/part/SE-Detector> ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/BSE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "BSE Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/SE-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SE Detector" ;
    schema1:name "missing" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: SEM Imaging Technique-Aligned Protocol Profile (semImagingTAPP)
description: 'Scanning electron microscopy imaging (SE/BSE/CL/EBSD) extension of the
  base TAPP definition. Basic protocol-tier fields are required top-level ada: properties;
  Advanced protocol-tier fields are schema:additionalProperty[] entries. No ada:analyteTemplate
  (imaging has no per-element analyte axis). Generated from tapp/Current TAPPs/SEM_Imaging_TAPP_v15.csv
  by tools/build_tapp.py.'
allOf:
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/targetSelection/schema.yaml#/$defs/ProcedureIdentification
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
                              - Silicate mineral
                              - Oxide
                              - Sulfide
                              - Carbonate
                              - Phosphate
                              - Metal alloy
                              - Organic matter
                              - Glass
                              - Regolith
                              - Whole rock / polished section
                              - Porous material
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
                  schema:description:
                    description: Method by which samples were prepared for SEM analysis
                      prior to loading in the instrument. Includes mounting medium
                      (epoxy, carbon tape, stub), polishing steps (alumina, colloidal
                      silica, argon ion mill), and conductive coating type and thickness.
                      For VP-SEM/ESEM analyses, note whether an uncoated sample was
                      used and the gas type used. FIB-specific in-session operations
                      (protective coating deposition, milling conditions, lamella
                      preparation) are documented separately in Group 4.
                    anyOf:
                    - type: string
                    - type: array
                      items:
                        type: string
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
                  const: Sample preparation
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
                      measurement, recorded as a controlled value so that procedures
                      can be found by vendor. Where a procedure couples a sample-introduction
                      system to an analysing instrument, this records the analysing
                      instrument. Instrument Model gives the specific designation.
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
                            - Schottky FEG
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
                              - Schottky FEG
                              - LaB6 / CeB6
                              - Tungsten (W)
                              - Unknown
                              - N/A
                              - None
                              - missing
                              readOnly: true
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
                          description: Type of backscattered electron detector. Solid-state
                            diode detectors (single or segmented) are standard; YAG
                            scintillator detectors offer high sensitivity at low voltage.
                            Segmented detectors can operate in composition mode (segments
                            summed) or topography mode (differential signal between
                            segments). In-lens BSE detectors provide improved BSE
                            collection at short working distances.
                          anyOf:
                          - type: string
                            enum:
                            - Solid-state diode (single)
                            - Solid-state diode (segmented, composition mode)
                            - Solid-state diode (segmented, topography mode)
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
                              - In-lens BSE
                              - YAG scintillator
                              - N/A
                              - None
                              - missing
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
                description: 'Broad platform type of the instrument. ''Standard SEM'':
                  dedicated electron-only SEM column. ''FIB-SEM dual-beam'': combined
                  focused ion beam and SEM columns (enables TEM specimen preparation,
                  3D serial sectioning, ion-beam milling). ''VP-SEM / ESEM'': variable-pressure
                  or environmental SEM for imaging uncoated, hydrated, or charging
                  specimens. An instrument may combine categories (e.g., FIB-SEM with
                  VP capability).'
                anyOf:
                - type: string
                  enum:
                  - Standard SEM
                  - FIB-SEM dual-beam
                  - VP-SEM / ESEM
                  - FIB-SEM dual-beam + VP
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
                    - VP-SEM / ESEM
                    - FIB-SEM dual-beam + VP
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
                description: Electron beam accelerating voltage in kilovolts. Affects
                  X-ray generation depth (EDS/WDS), EBSD pattern quality, imaging
                  resolution, and beam penetration. Low voltages (1-5 kV) improve
                  surface sensitivity and reduce beam damage; high voltages (15-20
                  kV) improve X-ray generation for quantitative analysis.
                anyOf:
                - type: number
                - type: string
              ada:workingDistanceDefault:
                description: Distance between the objective lens pole piece and the
                  specimen surface in millimetres. Affects spatial resolution, depth
                  of focus, EDS X-ray take-off angle, and EBSD geometry.
                anyOf:
                - type: number
                - type: string
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
    ada:analyteTemplate:
      type: object
      properties:
        ada:analyteColumns:
          type: array
          items:
            anyOf:
            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/AnalyteIdentifierColumn
            - title: Beam Current
              description: Electron beam probe current. Higher current improves signal-to-noise
                for X-ray analysis (EDS/WDS, EBSD) and CL but may increase beam damage
                and reduce spatial resolution. Express in nA; for sub-nA values use
                decimal notation (e.g., 0.4 nA).
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/semImagingTAPP/beamCurrent
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
              description: Electron beam probe current. Higher current improves signal-to-noise
                for X-ray analysis (EDS/WDS, EBSD) and CL but may increase beam damage
                and reduce spatial resolution. Express in nA; for sub-nA values use
                decimal notation (e.g., 0.4 nA).
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/semImagingTAPP/beamCurrent
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
            nm or \xB5m. Defines spatial sampling of SE or BSE images. For large-area
            mosaic imaging, report the pixel size of individual tiles and the number
            and arrangement of tiles."
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
            nm or \xB5m. Defines spatial sampling of SE or BSE images. For large-area
            mosaic imaging, report the pixel size of individual tiles and the number
            and arrangement of tiles."
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
      description: Time the electron beam dwells on each pixel during raster scanning
        (imaging modes) or on each step position during compositional mapping (EDS
        and WDS mapping modes), in microseconds or milliseconds. Longer dwell time
        improves signal-to-noise and counting statistics but increases total dose
        and can cause beam damage or contamination on sensitive materials. For WDS
        mapping, the dwell time is per spectrometer per pixel.
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
      - Spectral point
      - Hyperspectral map
      - Multi-channel pseudo-color
      - N/A
      - None
      - missing
      readOnly: true
    ada:clWavelengthRange:
      description: Detection wavelength range of the CL system in nm. The range is
        set by the detector sensitivity and any optical filters installed.
      anyOf:
      - type: number
      - type: string
      readOnly: true
    ada:clIntegrationTimeDefault:
      description: Acquisition time per pixel (hyperspectral map mode) or per spectrum
        (spectral point mode), in ms or s. Longer integration improves signal-to-noise
        but increases beam dose and acquisition time.
      anyOf:
      - type: number
      - type: string
    ada:sampleTiltAngle:
      description: Sample tilt angle for EBSD acquisition in degrees, measured from
        horizontal. Standard EBSD geometry uses 70 degrees tilt toward the EBSD camera
        to maximise diffracted electron signal.
      anyOf:
      - type: number
      - type: string
      readOnly: true
    ada:ebsdStepSizeDefault:
      description: "Distance between adjacent EBSD measurement points in the map in
        nm or \xB5m. Must be smaller than the smallest grain of interest to resolve
        grain boundary positions and intragrain orientation gradients."
      anyOf:
      - type: number
      - type: string
    ada:ebsdPhaseListDefault:
      description: Mineral phases included in the EBSD reference pattern library for
        this procedure. The procedure specifies the expected phase suite for the target
        material; analysts may add phases for specific sample compositions.
      type: string
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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Imaging/tapp/context.jsonld)

## Sources

* [SEM_Imaging_TAPP_v4.xlsx (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/SEM-Imaging/tapp`

