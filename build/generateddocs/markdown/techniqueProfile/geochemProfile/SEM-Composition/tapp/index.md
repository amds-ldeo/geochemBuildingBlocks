
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
  "schema:description": "semCompositionTAPP instance derived from Genge et al. 2025 | Micrometeorite NG-1 (CV3-like) | EDS Point Analysis (ZEISS Sigma 1550VP, 10 kV) (publication column of SEM_Composition_TAPP_v24.csv).",
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
  "ada:matrixCorrectionMethod": "XPP (Simplified PAP)",
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
  "ada:analyticalMode": [
    "EDS Point Analysis"
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
  "ada:edsAcquisitionMode": "missing",
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:samplingUnit": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:targetSelectionCriteriaDefault": "missing",
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
  "schema:description": "semCompositionTAPP instance derived from Genge et al. 2025 | Micrometeorite NG-1 (CV3-like) | EDS Point Analysis (ZEISS Sigma 1550VP, 10 kV) (publication column of SEM_Composition_TAPP_v24.csv).",
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
  "ada:matrixCorrectionMethod": "XPP (Simplified PAP)",
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
  "ada:analyticalMode": [
    "EDS Point Analysis"
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
  "ada:edsAcquisitionMode": "missing",
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:samplingUnit": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:targetSelectionCriteriaDefault": "missing",
  "ada:wdsDeadTimeCorrection": "missing",
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

ex:semCompositionTAPP-Genge2025 a cdi:Activity,
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
    schema1:description "semCompositionTAPP instance derived from Genge et al. 2025 | Micrometeorite NG-1 (CV3-like) | EDS Point Analysis (ZEISS Sigma 1550VP, 10 kV) (publication column of SEM_Composition_TAPP_v24.csv)." ;
    schema1:instrument <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "GPS Division Analytical Facility, California Institute of Technology" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semComposition" ;
            schema1:termCode "semComposition" ] ;
    schema1:name "semComposition protocol — Genge2025" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Micrometeorite NG-1, Al-Cu-alloy-bearing, CV3-like composition; Democratic Republic of Congo" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "BSE Imaging (same session, same instrument); EBSD (same instrument); EPMA (JEOL JXA-iHP200F, WDS, out of scope)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "EDS Point Analysis" ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "XPP (Simplified PAP)" ;
    ada:samplingUnit "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:wdsDeadTimeCorrection "missing" .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:description "VP-SEM / ESEM" ;
    schema1:hasPart <https://example.org/instrument/SEM/part/EDS-Detector>,
        <https://example.org/instrument/SEM/part/Electron-Source>,
        <https://example.org/instrument/SEM/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Zeiss" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "ZEISS 1550VP" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "10 kV" .

<https://example.org/instrument/SEM/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:description "Oxford X-Max SDD system" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Unknown" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "missing" .


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
          "@id": "ex:instrument/SEM/part/Electron-Source"
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
      "schema:name": "example instrumentName"
    }
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
  "ada:analyticalMode": [
    "EDS Point Analysis"
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
  "ada:edsAcquisitionMode": "missing",
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:samplingUnit": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:targetSelectionCriteriaDefault": "missing",
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
          "@id": "ex:instrument/SEM/part/Electron-Source"
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
      "schema:name": "example instrumentName"
    }
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
  "ada:analyticalMode": [
    "EDS Point Analysis"
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
  "ada:edsAcquisitionMode": "missing",
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:samplingUnit": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:targetSelectionCriteriaDefault": "missing",
  "ada:wdsDeadTimeCorrection": "missing",
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

ex:semCompositionTAPP-Gucsik2013 a cdi:Activity,
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
    schema1:description "Described as semiquantitative; BSE images also captured with this instrument at same conditions; EPMA (JEOL JXA-8900R WDS) used for quantitative analyses (out of scope)" ;
    schema1:instrument <https://example.org/instrument/SEM> ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semComposition" ;
            schema1:termCode "semComposition" ] ;
    schema1:name "semComposition protocol — Gucsik2013" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Forsterite grains from Kaba (CV3) carbonaceous chondrite thin section" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "CL (same instrument); BSE Imaging (same instrument, same session); EPMA with WDS (JEOL JXA-8900R, out of scope)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "EDS Point Analysis" ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:samplingUnit "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:wdsDeadTimeCorrection "missing" .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:description "Standard SEM" ;
    schema1:hasPart <https://example.org/instrument/SEM/part/EDS-Detector>,
        <https://example.org/instrument/SEM/part/Electron-Source>,
        <https://example.org/instrument/SEM/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "JEOL" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "JSM-5410LV" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "15 kV" .

<https://example.org/instrument/SEM/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:description "ISIS analysis system (Oxford); detector type not specified" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "missing" .


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
          "@id": "ex:instrument/SEM/part/Electron-Source"
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
      "schema:name": "example instrumentName"
    }
  ],
  "ada:edsAcquisitionMode": "Map",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/semCompositionTAPP/detectionLimitDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "detectionLimitDefault",
      "schema:name": "Detection Limit",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 0.5,
      "schema:description": "~0.5 wt% for most elements"
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
        "schema:name": "BSE Imaging (same instrument); CL (Hitachi S-2500C); micro-XRD; EPMA (out of scope)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:analyticalMode": [
    "EDS Mapping"
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
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:samplingUnit": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:targetSelectionCriteriaDefault": "missing",
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
          "@id": "ex:instrument/SEM/part/Electron-Source"
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
      "schema:name": "example instrumentName"
    }
  ],
  "ada:edsAcquisitionMode": "Map",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/semCompositionTAPP/detectionLimitDefault",
      "@type": [
        "schema:PropertyValueSpecification"
      ],
      "schema:valueName": "detectionLimitDefault",
      "schema:name": "Detection Limit",
      "ada:dataType": "number",
      "ada:fieldScope": "session",
      "schema:defaultValue": 0.5,
      "schema:description": "~0.5 wt% for most elements"
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
        "schema:name": "BSE Imaging (same instrument); CL (Hitachi S-2500C); micro-XRD; EPMA (out of scope)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
    }
  ],
  "ada:analyticalMode": [
    "EDS Mapping"
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
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:samplingUnit": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:targetSelectionCriteriaDefault": "missing",
  "ada:wdsDeadTimeCorrection": "missing",
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

ex:semCompositionTAPP-Izawa2010 a cdi:Activity,
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
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/detectionLimitDefault> ;
    schema1:datePublished "missing" ;
    schema1:description "Full spectral imaging (Quartz XOne): all X-rays recorded per pixel, allowing post-hoc spectral analysis" ;
    schema1:instrument <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Surface Science Western" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semComposition" ;
            schema1:termCode "semComposition" ] ;
    schema1:name "semComposition protocol — Izawa2010" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Tagish Lake (C2) ungrouped carbonaceous chondrite; polished thin sections" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "BSE Imaging (same instrument); CL (Hitachi S-2500C); micro-XRD; EPMA (out of scope)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "EDS Mapping" ;
    ada:edsAcquisitionMode "Map" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:samplingUnit "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:wdsDeadTimeCorrection "missing" .

<https://ada.astromat.org/metadata/parameter/semCompositionTAPP/detectionLimitDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 5e-01 ;
    schema1:description "~0.5 wt% for most elements" ;
    schema1:name "Detection Limit" ;
    schema1:valueName "detectionLimitDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:description "Standard SEM" ;
    schema1:hasPart <https://example.org/instrument/SEM/part/EDS-Detector>,
        <https://example.org/instrument/SEM/part/Electron-Source>,
        <https://example.org/instrument/SEM/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Zeiss" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Leo 440" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/SEM/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:description "Gresham light element detector; Quartz XOne EDX analysis system (full spectral imaging)" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "missing" .


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
      "schema:name": "example instrumentName"
    }
  ],
  "ada:edsAcquisitionMode": "Point / spot",
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
  "ada:analyticalMode": [
    "EDS Point Analysis"
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
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:samplingUnit": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:targetSelectionCriteriaDefault": "missing",
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
      "schema:name": "example instrumentName"
    }
  ],
  "ada:edsAcquisitionMode": "Point / spot",
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
  "ada:analyticalMode": [
    "EDS Point Analysis"
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
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:samplingUnit": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:targetSelectionCriteriaDefault": "missing",
  "ada:wdsDeadTimeCorrection": "missing",
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

ex:semCompositionTAPP-Izawa2010-2 a cdi:Activity,
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
    schema1:description "Additional BSE and EDX analyses also carried out with Hitachi S-4300SE/N (Texas Tech) and Hitachi SU6600 (UWO) — not captured as separate assessment columns Reported detail: ada:edsAcquisitionMode = Point / spot; Map." ;
    schema1:instrument <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Nanofabrication Laboratory, University of Western Ontario" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semComposition" ;
            schema1:termCode "semComposition" ] ;
    schema1:name "semComposition protocol — Izawa2010-2" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Tagish Lake (C2) ungrouped carbonaceous chondrite; polished thin sections" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "BSE Imaging (same instrument); CL (Hitachi S-2500C); micro-XRD; EPMA (out of scope)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "EDS Point Analysis" ;
    ada:edsAcquisitionMode "Point / spot" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:samplingUnit "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:wdsDeadTimeCorrection "missing" .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:description "FIB-SEM dual-beam" ;
    schema1:hasPart <https://example.org/instrument/SEM/part/EDS-Detector>,
        <https://example.org/instrument/SEM/part/Electron-Source>,
        <https://example.org/instrument/SEM/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Zeiss" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Leo 1540 FIB/SEM CrossBeam" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/SEM/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:description "Oxford Instruments INCA EDX system" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Unknown" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "missing" .


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
  "schema:description": "Spot analysis: 20 kV, 30 µm aperture, 30 s live time per spot, maximum process time (Oxford INCA Energy)",
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
      "schema:description": "N/A",
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
  "ada:edsLiveTimePerPointOrPixelDefault": "30 s live time per spot analysis",
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
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Mg",
      "Si",
      "Fe",
      "Ni",
      "S",
      "Na",
      "Ca",
      "Al"
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
        "@id": "ada:analyteColumn/semCompositionTAPP/beamCurrent",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "beamCurrent",
        "schema:name": "Beam Current",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/techniquePerAnalyte",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "techniquePerAnalyte",
        "schema:name": "Technique per Analyte",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/wdsSpectrometerChannel",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "wdsSpectrometerChannel",
        "schema:name": "WDS Spectrometer Channel",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/backgroundCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCorrectionMethod",
        "schema:name": "Background Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/timeDependentIntensityCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "timeDependentIntensityCorrection",
        "schema:name": "Time-Dependent Intensity Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/analyteEstimationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyteEstimationMethod",
        "schema:name": "Analyte Estimation Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/blankCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "blankCorrection",
        "schema:name": "Blank Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/primaryCalibrationStandardName",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "primaryCalibrationStandardName",
        "schema:name": "Primary Calibration Standard Name",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/secondaryReferenceMaterials",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "secondaryReferenceMaterials",
        "schema:name": "Secondary Reference Materials",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/interferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionsApplied",
        "schema:name": "Interference Corrections Applied",
        "ada:dataType": "boolean",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/interferingElements",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingElements",
        "schema:name": "Interfering Elements",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/interferenceCorrectionStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionStandard",
        "schema:name": "Interference Correction Standard",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/analyticalPrecision",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalPrecision",
        "schema:name": "Analytical Precision",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/analyticalAccuracy",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracy",
        "schema:name": "Analytical Accuracy",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      }
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
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:samplingUnit": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:targetSelectionCriteriaDefault": "missing",
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
  "schema:description": "Spot analysis: 20 kV, 30 \u00b5m aperture, 30 s live time per spot, maximum process time (Oxford INCA Energy)",
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
      "schema:description": "N/A",
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
  "ada:edsLiveTimePerPointOrPixelDefault": "30 s live time per spot analysis",
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
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Mg",
      "Si",
      "Fe",
      "Ni",
      "S",
      "Na",
      "Ca",
      "Al"
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
        "@id": "ada:analyteColumn/semCompositionTAPP/beamCurrent",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "beamCurrent",
        "schema:name": "Beam Current",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/techniquePerAnalyte",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "techniquePerAnalyte",
        "schema:name": "Technique per Analyte",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/wdsSpectrometerChannel",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "wdsSpectrometerChannel",
        "schema:name": "WDS Spectrometer Channel",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/backgroundCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCorrectionMethod",
        "schema:name": "Background Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/timeDependentIntensityCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "timeDependentIntensityCorrection",
        "schema:name": "Time-Dependent Intensity Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/analyteEstimationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyteEstimationMethod",
        "schema:name": "Analyte Estimation Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/blankCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "blankCorrection",
        "schema:name": "Blank Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/primaryCalibrationStandardName",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "primaryCalibrationStandardName",
        "schema:name": "Primary Calibration Standard Name",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/secondaryReferenceMaterials",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "secondaryReferenceMaterials",
        "schema:name": "Secondary Reference Materials",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/interferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionsApplied",
        "schema:name": "Interference Corrections Applied",
        "ada:dataType": "boolean",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/interferingElements",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingElements",
        "schema:name": "Interfering Elements",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/interferenceCorrectionStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionStandard",
        "schema:name": "Interference Correction Standard",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/analyticalPrecision",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalPrecision",
        "schema:name": "Analytical Precision",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/analyticalAccuracy",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracy",
        "schema:name": "Analytical Accuracy",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      }
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
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:samplingUnit": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:targetSelectionCriteriaDefault": "missing",
  "ada:wdsDeadTimeCorrection": "missing",
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

ex:semCompositionTAPP-Pascucci2026 a cdi:Activity,
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
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/chamberPressureDefault>,
        <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/edsSpectralProcessingType> ;
    schema1:datePublished "missing" ;
    schema1:description "Spot analysis: 20 kV, 30 µm aperture, 30 s live time per spot, maximum process time (Oxford INCA Energy)" ;
    schema1:instrument <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "CNR IMAA (Institute of Methodologies for Environmental Analysis), Italian National Research Council, Potenza, Italy" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semComposition" ;
            schema1:termCode "semComposition" ] ;
    schema1:name "semComposition protocol — Pascucci2026" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "NWA 7317 CR6 carbonaceous chondrite; polished slab (~10×6 mm fragment, 10.01g)" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "BSE Imaging (Zeiss Supra 40 FE-SEM); SE Imaging (Zeiss Supra 40 FE-SEM); EMPA-WDS (JEOL JXA-8230, separate instrument); VIS-IR spectroscopy (SPIM)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/analyteEstimationMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/analyticalAccuracy>,
                <https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/analyticalPrecision>,
                <https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/backgroundCorrectionMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/beamCurrent>,
                <https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/blankCorrection>,
                <https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/interferenceCorrectionStandard>,
                <https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/interferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/interferingElements>,
                <https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/primaryCalibrationStandardName>,
                <https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/secondaryReferenceMaterials>,
                <https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/techniquePerAnalyte>,
                <https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/timeDependentIntensityCorrection>,
                <https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/wdsSpectrometerChannel> ;
            ada:defaultAnalytes "Al",
                "Ca",
                "Fe",
                "Mg",
                "Na",
                "Ni",
                "S",
                "Si" ] ;
    ada:analyticalMode "EDS Point Analysis" ;
    ada:edsAcquisitionMode "N/A" ;
    ada:edsLiveTimePerPointOrPixelDefault "30 s live time per spot analysis" ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:samplingUnit "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:wdsDeadTimeCorrection "missing" ;
    bios:computationalTool [ schema1:name "Oxford INCA Energy (semi-quantitative phase determination from atomic proportions)" ;
            ada:toolRole "dataReduction" ],
        [ schema1:name "Oxford INCA Energy" ;
            ada:toolRole "acquisition" ] .

<https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/analyteEstimationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Analyte Estimation Method" ;
    schema1:valueName "analyteEstimationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/analyticalAccuracy> a schema1:PropertyValueSpecification ;
    schema1:name "Analytical Accuracy" ;
    schema1:valueName "analyticalAccuracy" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/analyticalPrecision> a schema1:PropertyValueSpecification ;
    schema1:name "Analytical Precision" ;
    schema1:valueName "analyticalPrecision" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/backgroundCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Background Correction Method" ;
    schema1:valueName "backgroundCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/beamCurrent> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Beam Current" ;
    schema1:valueName "beamCurrent" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/blankCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Blank Correction" ;
    schema1:valueName "blankCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/interferenceCorrectionStandard> a schema1:PropertyValueSpecification ;
    schema1:name "Interference Correction Standard" ;
    schema1:valueName "interferenceCorrectionStandard" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/interferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Corrections Applied" ;
    schema1:valueName "interferenceCorrectionsApplied" ;
    ada:dataType "boolean" .

<https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/interferingElements> a schema1:PropertyValueSpecification ;
    schema1:name "Interfering Elements" ;
    schema1:valueName "interferingElements" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/secondaryReferenceMaterials> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Secondary Reference Materials" ;
    schema1:valueName "secondaryReferenceMaterials" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/techniquePerAnalyte> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Technique per Analyte" ;
    schema1:valueName "techniquePerAnalyte" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/timeDependentIntensityCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Time-Dependent Intensity Correction" ;
    schema1:valueName "timeDependentIntensityCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/wdsSpectrometerChannel> a schema1:PropertyValueSpecification ;
    schema1:name "WDS Spectrometer Channel" ;
    schema1:valueName "wdsSpectrometerChannel" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/semCompositionTAPP/chamberPressureDefault> a schema1:PropertyValueSpecification ;
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
    schema1:hasPart <https://example.org/instrument/SEM/part/EDS-Detector>,
        <https://example.org/instrument/SEM/part/Electron-Source>,
        <https://example.org/instrument/SEM/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Zeiss" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Supra 40" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "20 kV" .

<https://example.org/instrument/SEM/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:description "Oxford INCA Energy 350; X-ACT LN2-free Silicon Drift Detector (SDD)" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Unknown" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "missing" .

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
      "schema:description": "N/A",
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
  "ada:edsLiveTimePerPointOrPixelDefault": "5 ms dwell time per pixel",
  "ada:stepSizePixelSizeDefault": "2.5 µm",
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
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Mg",
      "Si",
      "Fe",
      "Ni",
      "S",
      "Na",
      "Ca",
      "Al (element mapping)"
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
        "@id": "ada:analyteColumn/semCompositionTAPP/beamCurrent",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "beamCurrent",
        "schema:name": "Beam Current",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/techniquePerAnalyte",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "techniquePerAnalyte",
        "schema:name": "Technique per Analyte",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/wdsSpectrometerChannel",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "wdsSpectrometerChannel",
        "schema:name": "WDS Spectrometer Channel",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/backgroundCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCorrectionMethod",
        "schema:name": "Background Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/timeDependentIntensityCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "timeDependentIntensityCorrection",
        "schema:name": "Time-Dependent Intensity Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/analyteEstimationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyteEstimationMethod",
        "schema:name": "Analyte Estimation Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/blankCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "blankCorrection",
        "schema:name": "Blank Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/primaryCalibrationStandardName",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "primaryCalibrationStandardName",
        "schema:name": "Primary Calibration Standard Name",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/secondaryReferenceMaterials",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "secondaryReferenceMaterials",
        "schema:name": "Secondary Reference Materials",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/interferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionsApplied",
        "schema:name": "Interference Corrections Applied",
        "ada:dataType": "boolean",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/interferingElements",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingElements",
        "schema:name": "Interfering Elements",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/interferenceCorrectionStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionStandard",
        "schema:name": "Interference Correction Standard",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/analyticalPrecision",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalPrecision",
        "schema:name": "Analytical Precision",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/analyticalAccuracy",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracy",
        "schema:name": "Analytical Accuracy",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      }
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
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:samplingUnit": "missing",
  "ada:targetSelectionCriteriaDefault": "missing",
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
      "schema:description": "N/A",
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
  "ada:edsLiveTimePerPointOrPixelDefault": "5 ms dwell time per pixel",
  "ada:stepSizePixelSizeDefault": "2.5 \u00b5m",
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
  "ada:analyteTemplate": {
    "ada:defaultAnalytes": [
      "Mg",
      "Si",
      "Fe",
      "Ni",
      "S",
      "Na",
      "Ca",
      "Al (element mapping)"
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
        "@id": "ada:analyteColumn/semCompositionTAPP/beamCurrent",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "beamCurrent",
        "schema:name": "Beam Current",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/techniquePerAnalyte",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "techniquePerAnalyte",
        "schema:name": "Technique per Analyte",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/wdsSpectrometerChannel",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "wdsSpectrometerChannel",
        "schema:name": "WDS Spectrometer Channel",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/backgroundCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCorrectionMethod",
        "schema:name": "Background Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/timeDependentIntensityCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "timeDependentIntensityCorrection",
        "schema:name": "Time-Dependent Intensity Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/analyteEstimationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyteEstimationMethod",
        "schema:name": "Analyte Estimation Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/blankCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "blankCorrection",
        "schema:name": "Blank Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/primaryCalibrationStandardName",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "primaryCalibrationStandardName",
        "schema:name": "Primary Calibration Standard Name",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/secondaryReferenceMaterials",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "secondaryReferenceMaterials",
        "schema:name": "Secondary Reference Materials",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/interferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionsApplied",
        "schema:name": "Interference Corrections Applied",
        "ada:dataType": "boolean",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/interferingElements",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingElements",
        "schema:name": "Interfering Elements",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/interferenceCorrectionStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionStandard",
        "schema:name": "Interference Correction Standard",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/analyticalPrecision",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalPrecision",
        "schema:name": "Analytical Precision",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/analyticalAccuracy",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracy",
        "schema:name": "Analytical Accuracy",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semCompositionTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      }
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
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:samplingUnit": "missing",
  "ada:targetSelectionCriteriaDefault": "missing",
  "ada:wdsDeadTimeCorrection": "missing",
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

ex:semCompositionTAPP-Pascucci2026-2 a cdi:Activity,
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
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/chamberPressureDefault>,
        <https://ada.astromat.org/metadata/parameter/semCompositionTAPP/edsSpectralProcessingType> ;
    schema1:datePublished "missing" ;
    schema1:description "EDS mapping: 20 kV, 60 µm aperture, 5 ms dwell per pixel, 1024×768 pixels, 2.5 µm pixel size, ~10 h total; element maps co-registered with BSE images Reported detail: ada:edsAcquisitionMode = Element mapping." ;
    schema1:instrument <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "CNR IMAA (Institute of Methodologies for Environmental Analysis), Italian National Research Council, Potenza, Italy" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semComposition" ;
            schema1:termCode "semComposition" ] ;
    schema1:name "semComposition protocol — Pascucci2026-2" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "NWA 7317 CR6 carbonaceous chondrite; polished slab (~10×6 mm fragment, 10.01g)" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "BSE Imaging (Zeiss Supra 40 FE-SEM); SE Imaging (Zeiss Supra 40 FE-SEM); EMPA-WDS (JEOL JXA-8230, separate instrument); VIS-IR spectroscopy (SPIM)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyteTemplate [ ada:analyteColumns [ a schema1:PropertyValueSpecification ;
                    schema1:name "example instrumentName" ;
                    schema1:readonlyValue true ;
                    schema1:valueName "analyte" ;
                    schema1:valueRequired true ;
                    ada:cdifPropertyPath "#/schema:variableMeasured/schema:name" ;
                    ada:dataType "string" ;
                    ada:tier "M" ],
                <https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/analyteEstimationMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/analyticalAccuracy>,
                <https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/analyticalPrecision>,
                <https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/backgroundCorrectionMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/beamCurrent>,
                <https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/blankCorrection>,
                <https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/interferenceCorrectionStandard>,
                <https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/interferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/interferingElements>,
                <https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/primaryCalibrationStandardName>,
                <https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/secondaryReferenceMaterials>,
                <https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/techniquePerAnalyte>,
                <https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/timeDependentIntensityCorrection>,
                <https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/wdsSpectrometerChannel> ;
            ada:defaultAnalytes "Al (element mapping)",
                "Ca",
                "Fe",
                "Mg",
                "Na",
                "Ni",
                "S",
                "Si" ] ;
    ada:analyticalMode "EDS Mapping" ;
    ada:edsAcquisitionMode "Map" ;
    ada:edsLiveTimePerPointOrPixelDefault "5 ms dwell time per pixel" ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:samplingUnit "missing" ;
    ada:stepSizePixelSizeDefault "2.5 µm" ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:wdsDeadTimeCorrection "missing" ;
    bios:computationalTool [ schema1:name "Oxford INCA Energy (semi-quantitative phase determination from atomic proportions)" ;
            ada:toolRole "dataReduction" ],
        [ schema1:name "Oxford INCA Energy" ;
            ada:toolRole "acquisition" ] .

<https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/analyteEstimationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Analyte Estimation Method" ;
    schema1:valueName "analyteEstimationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/analyticalAccuracy> a schema1:PropertyValueSpecification ;
    schema1:name "Analytical Accuracy" ;
    schema1:valueName "analyticalAccuracy" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/analyticalPrecision> a schema1:PropertyValueSpecification ;
    schema1:name "Analytical Precision" ;
    schema1:valueName "analyticalPrecision" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/backgroundCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Background Correction Method" ;
    schema1:valueName "backgroundCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/beamCurrent> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Beam Current" ;
    schema1:valueName "beamCurrent" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/blankCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Blank Correction" ;
    schema1:valueName "blankCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/interferenceCorrectionStandard> a schema1:PropertyValueSpecification ;
    schema1:name "Interference Correction Standard" ;
    schema1:valueName "interferenceCorrectionStandard" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/interferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Corrections Applied" ;
    schema1:valueName "interferenceCorrectionsApplied" ;
    ada:dataType "boolean" .

<https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/interferingElements> a schema1:PropertyValueSpecification ;
    schema1:name "Interfering Elements" ;
    schema1:valueName "interferingElements" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/secondaryReferenceMaterials> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Secondary Reference Materials" ;
    schema1:valueName "secondaryReferenceMaterials" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/techniquePerAnalyte> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Technique per Analyte" ;
    schema1:valueName "techniquePerAnalyte" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/timeDependentIntensityCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Time-Dependent Intensity Correction" ;
    schema1:valueName "timeDependentIntensityCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semCompositionTAPP/wdsSpectrometerChannel> a schema1:PropertyValueSpecification ;
    schema1:name "WDS Spectrometer Channel" ;
    schema1:valueName "wdsSpectrometerChannel" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/semCompositionTAPP/chamberPressureDefault> a schema1:PropertyValueSpecification ;
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
    schema1:hasPart <https://example.org/instrument/SEM/part/EDS-Detector>,
        <https://example.org/instrument/SEM/part/Electron-Source>,
        <https://example.org/instrument/SEM/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Zeiss" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Supra 40" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "20 kV" .

<https://example.org/instrument/SEM/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:description "Oxford INCA Energy 350; X-ACT LN2-free Silicon Drift Detector (SDD)" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Unknown" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "missing" .

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
  "schema:description": "semCompositionTAPP instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | EDS Point Analysis (JEOL 7600F, NASA JSC, 15 kV) (publication column of SEM_Composition_TAPP_v24.csv).",
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
            "Asteroid (101955) Bennu particles (OSIRIS-REx sample return)"
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
      "schema:name": "example instrumentName"
    }
  ],
  "ada:edsAcquisitionMode": "N/A",
  "ada:edsLiveTimePerPointOrPixelDefault": "20 to 200 s (per point)",
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
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "semComposition",
      "schema:termCode": "semComposition"
    }
  ],
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:samplingUnit": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:targetSelectionCriteriaDefault": "missing",
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
  "schema:description": "semCompositionTAPP instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | EDS Point Analysis (JEOL 7600F, NASA JSC, 15 kV) (publication column of SEM_Composition_TAPP_v24.csv).",
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
            "Asteroid (101955) Bennu particles (OSIRIS-REx sample return)"
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
      "schema:name": "example instrumentName"
    }
  ],
  "ada:edsAcquisitionMode": "N/A",
  "ada:edsLiveTimePerPointOrPixelDefault": "20 to 200 s (per point)",
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
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "semComposition",
      "schema:termCode": "semComposition"
    }
  ],
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:samplingUnit": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:targetSelectionCriteriaDefault": "missing",
  "ada:wdsDeadTimeCorrection": "missing",
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

ex:semCompositionTAPP-Zega2025 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Attached to Al cylinder SEM mount with double-sided C tape; sputter coated with ~5 nm carbon" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "semCompositionTAPP instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | EDS Point Analysis (JEOL 7600F, NASA JSC, 15 kV) (publication column of SEM_Composition_TAPP_v24.csv)." ;
    schema1:instrument <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "NASA Johnson Space Center (JSC), Houston, TX, USA" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semComposition" ;
            schema1:termCode "semComposition" ] ;
    schema1:name "semComposition protocol — Zega2025" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Asteroid (101955) Bennu particles (OSIRIS-REx sample return)" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "BSE Imaging (JEOL 7600F, JSC); SE Imaging (JEOL 7600F, JSC); FIB-SEM TEM prep (Quanta3D600, JSC)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "EDS Point Analysis" ;
    ada:edsAcquisitionMode "N/A" ;
    ada:edsLiveTimePerPointOrPixelDefault "20 to 200 s (per point)" ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:samplingUnit "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:wdsDeadTimeCorrection "missing" ;
    bios:computationalTool [ schema1:name "Oxford AZtec" ;
            ada:toolRole "dataReduction" ],
        [ schema1:name "Oxford AZtec (Point & ID programme)" ;
            ada:toolRole "acquisition" ] .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:hasPart <https://example.org/instrument/SEM/part/EDS-Detector>,
        <https://example.org/instrument/SEM/part/Electron-Source>,
        <https://example.org/instrument/SEM/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "JEOL" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "7600F" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "15 kV" .

<https://example.org/instrument/SEM/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:description "Oxford Instruments Ultim Max SDD, 170 mm²" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Unknown" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "missing" .


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
      "schema:name": "example instrumentName"
    }
  ],
  "ada:edsAcquisitionMode": "Map",
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
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "semComposition",
      "schema:termCode": "semComposition"
    }
  ],
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:samplingUnit": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:targetSelectionCriteriaDefault": "missing",
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
      "schema:name": "example instrumentName"
    }
  ],
  "ada:edsAcquisitionMode": "Map",
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
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "semComposition",
      "schema:termCode": "semComposition"
    }
  ],
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:samplingUnit": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:targetSelectionCriteriaDefault": "missing",
  "ada:wdsDeadTimeCorrection": "missing",
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

ex:semCompositionTAPP-Zega2025-2 a cdi:Activity,
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
    schema1:description "Compositional heterogeneity assessed through EDS mapping; no specific kV, current, dwell time stated for S-4800 EDS Reported detail: ada:edsAcquisitionMode = EDS mapping." ;
    schema1:instrument <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "K-ALFAA (Kuiper-Arizona Laboratory for Astromaterials Analysis), University of Arizona" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semComposition" ;
            schema1:termCode "semComposition" ] ;
    schema1:name "semComposition protocol — Zega2025-2" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Asteroid (101955) Bennu particles (OSIRIS-REx sample return); polished sections" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SE/BSE Imaging (Hitachi S-4800, U Arizona); FIB-SEM TEM prep (Helios G3, U Arizona); EMPA (Cameca SX-100 Ultra, out of scope)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "EDS Mapping" ;
    ada:edsAcquisitionMode "Map" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:samplingUnit "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:wdsDeadTimeCorrection "missing" ;
    bios:computationalTool [ schema1:name "Oxford Instruments Aztec" ;
            ada:toolRole "dataReduction" ],
        [ schema1:name "Oxford Instruments Aztec Live/x-stream" ;
            ada:toolRole "acquisition" ] .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:hasPart <https://example.org/instrument/SEM/part/EDS-Detector>,
        <https://example.org/instrument/SEM/part/Electron-Source>,
        <https://example.org/instrument/SEM/part/WDS-Spectrometer> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Hitachi" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "S-4800" ] ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/SEM/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:description "Oxford Instruments Aztec Live/x-stream/Ultimax 170 SDD" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:description "Unknown" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "missing" .


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
            "Asteroid (101955) Bennu aggregate QL particles; O-rich presolar silicate and oxide grains; sample OREX-501018-100"
          ]
        }
      ]
    }
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
  "ada:analyticalMode": [
    "EDS Mapping"
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
          "@id": "ex:instrument/SEM/part/Electron-Source"
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
      ]
    }
  ],
  "ada:edsAcquisitionMode": "missing",
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:samplingUnit": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:targetSelectionCriteriaDefault": "missing",
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
            "Asteroid (101955) Bennu aggregate QL particles; O-rich presolar silicate and oxide grains; sample OREX-501018-100"
          ]
        }
      ]
    }
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
  "ada:analyticalMode": [
    "EDS Mapping"
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
          "@id": "ex:instrument/SEM/part/Electron-Source"
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
      ]
    }
  ],
  "ada:edsAcquisitionMode": "missing",
  "ada:edsLiveTimePerPointOrPixelDefault": -9999,
  "ada:massAbsorptionCoefficients": "missing",
  "ada:matrixCorrectionMethod": "missing",
  "ada:samplingUnit": "missing",
  "ada:stepSizePixelSizeDefault": -9999,
  "ada:targetSelectionCriteriaDefault": "missing",
  "ada:wdsDeadTimeCorrection": "missing",
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

ex:semCompositionTAPP-Barnes2025 a cdi:Activity,
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
    schema1:description "SEM-EDS (referred to as SEM-EDX in Extended Data Fig. 8) used to confirm phase identifications of two O-rich presolar grains identified by NanoSIMS isotope mapping: one grain confirmed as ferromagnesian silicate; one confirmed as Al,Mg-bearing oxide (Barnes et al. 2025, p.2 and Extended Data Fig. 8 caption). No instrument name, accelerating voltage, beam current, or sample preparation specifics stated for the JSC SEM-EDS step in this paper." ;
    schema1:instrument <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Astromaterials Research and Exploration Science Division (ARES), NASA Johnson Space Center, Houston, TX, USA" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:termCode "SEM-EDS (Scanning Electron Microscopy–Energy Dispersive X-ray Spectroscopy)" ] ;
    schema1:name "semComposition protocol — Barnes2025" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Asteroid (101955) Bennu aggregate QL particles; O-rich presolar silicate and oxide grains; sample OREX-501018-100" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "NanoSIMS isotope mapping (CAMECA NanoSIMS 50L, NASA JSC); presolar grains identified by NanoSIMS then confirmed by SEM-EDS phase characterisation" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "EDS Mapping" ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:samplingUnit "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:wdsDeadTimeCorrection "missing" .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:hasPart <https://example.org/instrument/SEM/part/EDS-Detector>,
        <https://example.org/instrument/SEM/part/Electron-Source>,
        <https://example.org/instrument/SEM/part/WDS-Spectrometer> ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/EDS-Detector> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "EDS Detector" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/Electron-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Electron Source" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM/part/WDS-Spectrometer> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "WDS Spectrometer" ;
    schema1:name "missing" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: SEM Composition (EDS/WDS) Technique-Aligned Protocol Profile (semCompositionTAPP)
description: Scanning electron microscopy compositional microanalysis (EDS/WDS) extension
  of the base TAPP definition, generated from tapp/Current TAPPs/SEM_Composition_TAPP_v24.csv
  via the path-driven pipeline (bootstrap_schemapaths.py + build_pathdriven.py).
allOf:
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/ProcedureIdentification
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
                  schema:additionalProperty:
                    type: array
                    items:
                      anyOf:
                      - title: Normalization / Standards-Based Correction
                        description: Post-acquisition normalization applied using
                          secondary reference materials to correct for session-to-session
                          calibration drift.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/semCompositionTAPP/normalizationStandardsBasedCorrectionDefault
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
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Procedure_constantsReferenceValues
                    allOf:
                    - contains:
                        title: Normalization / Standards-Based Correction
                        description: Post-acquisition normalization applied using
                          secondary reference materials to correct for session-to-session
                          calibration drift.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/semCompositionTAPP/normalizationStandardsBasedCorrectionDefault
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
                    - contains:
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Procedure_constantsReferenceValues
                      minContains: 0
                      maxContains: 1
                  ada:detectionLimitMethod:
                    description: Formula or approach used to calculate detection limits.
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
                            const: EDS Detector
                          schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                      required:
                      - schema:additionalType
                    then:
                      properties:
                        schema:description:
                          description: EDS detector type, manufacturer, active area,
                            solid angle, window type, and geometry (take-off angle,
                            position). Multiple detectors should be listed separately.
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
              ada:beamMode:
                description: Whether the electron beam was operated as a stationary
                  focused spot, defocused to a specified diameter, or rastered over
                  a small area during analysis. Controls the effective sampling volume
                  and irradiation footprint; critical for beam-sensitive phases such
                  as hydrous minerals, glasses, and carbonates. Must be consistent
                  with the Beam Diameter and Beam Raster Dimensions fields.
                anyOf:
                - type: string
                  enum:
                  - Focused
                  - Defocused
                  - Rastered
                  - N/A
                  - None
                  - missing
                  readOnly: true
                - type: array
                  items:
                    type: string
                    enum:
                    - Focused
                    - Defocused
                    - Rastered
                    - N/A
                    - None
                    - missing
                    readOnly: true
              ada:acceleratingVoltageDefault:
                description: Electron beam accelerating voltage in kilovolts. Affects
                  X-ray generation depth (EDS/WDS), EBSD pattern quality, imaging
                  resolution, and beam penetration. Low voltages (1-5 kV) improve
                  surface sensitivity and reduce beam damage; high voltages (15-20
                  kV) improve X-ray generation for quantitative analysis.
                anyOf:
                - type: number
                - type: string
              ada:beamDiameterDefault:
                description: Nominal electron beam diameter (spot size) at the sample
                  surface, in nanometres or micrometres, as set by the condenser aperture
                  and working distance. Controls the spatial resolution and X-ray
                  excitation volume. For mapping modes, the effective spatial sampling
                  interval is further defined by Step Size / Pixel Size.
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
                  const: ada:analyteColumn/semCompositionTAPP/beamCurrent
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
            - title: Technique per Analyte
              description: For each analyte, records which X-ray detection technique
                (EDS or WDS) was used to collect the measurement. Required when a
                procedure employs both EDS and WDS simultaneously, assigning each
                element to the detector appropriate to its concentration range, line
                overlap situation, or required precision. List in the same order as
                the Analyte field.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/semCompositionTAPP/techniquePerAnalyte
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: techniquePerAnalyte
                schema:name:
                  const: Technique per Analyte
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
            - title: WDS Spectrometer Channel
              description: "WDS spectrometer position(s) assigned to each analyte,
                one entry per assignment. An analyte may be assigned to more than
                one spectrometer with intensities aggregated (aggregate intensity
                counting), and one spectrometer serves several analytes across a run,
                so the assignment \u2014 not the analyte \u2014 is the unit carrying
                the spectrometer setup. Different spectrometers may have different
                crystal configurations."
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/semCompositionTAPP/wdsSpectrometerChannel
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
            - title: Background Correction Method
              description: 'Method used to estimate and subtract background X-ray
                intensity beneath the peak. For WDS: typically 2-point off-peak linear
                interpolation or Mean Atomic Number (MAN) background model. For EDS:
                spectral background fitting or top-hat filter applied during spectral
                processing.'
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/semCompositionTAPP/backgroundCorrectionMethod
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: backgroundCorrectionMethod
                schema:name:
                  const: Background Correction Method
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
                elements (e.g., Na, K, F in glasses, feldspars, carbonates). Most
                commonly applied in WDS point analysis; uncommon for EDS or X-ray
                mapping.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/semCompositionTAPP/timeDependentIntensityCorrection
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
            - title: Analyte Estimation Method
              description: Whether elemental concentrations were calculated directly
                from measured X-ray intensities, or estimated by cation stoichiometry
                (e.g., oxygen calculated from cation proportions in silicates; carbon
                from stoichiometry in carbonates).
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/semCompositionTAPP/analyteEstimationMethod
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: analyteEstimationMethod
                schema:name:
                  const: Analyte Estimation Method
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
                  const: ada:analyteColumn/semCompositionTAPP/blankCorrection
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
            - title: Primary Calibration Standard Name
              description: Name(s) of the primary reference material(s) used for intensity
                calibration in EDS or WDS quantification. Include the material name,
                its source or supplier, and a citation for the accepted values used,
                since results calibrated against different published values for the
                same material are not directly comparable.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/semCompositionTAPP/primaryCalibrationStandardName
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
            - title: Secondary Reference Materials
              description: Quality-control reference material(s) analyzed alongside
                unknowns to verify calibration accuracy. Include material name, assessed
                elements, number of analyses (n), and measured vs. accepted values
                where available.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/semCompositionTAPP/secondaryReferenceMaterials
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: secondaryReferenceMaterials
                schema:name:
                  const: Secondary Reference Materials
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
            - title: Interference Corrections Applied
              description: Whether a spectral interference correction was applied
                for each analyte. Common interferences include Ti Kb on V Ka, Cr Kb
                on Mn Ka, and Ba La on Ti Ka.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/semCompositionTAPP/interferenceCorrectionsApplied
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: interferenceCorrectionsApplied
                schema:name:
                  const: Interference Corrections Applied
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
            - title: Interfering Elements
              description: Element(s) whose X-ray lines overlap with the measured
                peak for one or more analytes, requiring a correction.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/semCompositionTAPP/interferingElements
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
                correction for each affected analyte.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/semCompositionTAPP/interferenceCorrectionStandard
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
                (n), and value per analyte or element group.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/semCompositionTAPP/analyticalPrecision
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
                material, reference value source, and per-analyte value.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/semCompositionTAPP/analyticalAccuracy
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
                sigma level stated. Derived from the counts on the analyte together
                with those on any background or blank subtracted from it. Distinct
                from the scatter actually observed within a measurement or between
                repeated measurements, which is recorded separately: where a procedure
                reports both, agreement indicates the measurement is shot-noise limited,
                and a larger observed scatter indicates a further source of variance."
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/semCompositionTAPP/countingStatisticsError
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
              description: Electron beam probe current. Higher current improves signal-to-noise
                for X-ray analysis (EDS/WDS, EBSD) and CL but may increase beam damage
                and reduce spatial resolution. Express in nA; for sub-nA values use
                decimal notation (e.g., 0.4 nA).
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/semCompositionTAPP/beamCurrent
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
              title: Technique per Analyte
              description: For each analyte, records which X-ray detection technique
                (EDS or WDS) was used to collect the measurement. Required when a
                procedure employs both EDS and WDS simultaneously, assigning each
                element to the detector appropriate to its concentration range, line
                overlap situation, or required precision. List in the same order as
                the Analyte field.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/semCompositionTAPP/techniquePerAnalyte
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: techniquePerAnalyte
                schema:name:
                  const: Technique per Analyte
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
              title: WDS Spectrometer Channel
              description: "WDS spectrometer position(s) assigned to each analyte,
                one entry per assignment. An analyte may be assigned to more than
                one spectrometer with intensities aggregated (aggregate intensity
                counting), and one spectrometer serves several analytes across a run,
                so the assignment \u2014 not the analyte \u2014 is the unit carrying
                the spectrometer setup. Different spectrometers may have different
                crystal configurations."
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/semCompositionTAPP/wdsSpectrometerChannel
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
              title: Background Correction Method
              description: 'Method used to estimate and subtract background X-ray
                intensity beneath the peak. For WDS: typically 2-point off-peak linear
                interpolation or Mean Atomic Number (MAN) background model. For EDS:
                spectral background fitting or top-hat filter applied during spectral
                processing.'
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/semCompositionTAPP/backgroundCorrectionMethod
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: backgroundCorrectionMethod
                schema:name:
                  const: Background Correction Method
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
                elements (e.g., Na, K, F in glasses, feldspars, carbonates). Most
                commonly applied in WDS point analysis; uncommon for EDS or X-ray
                mapping.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/semCompositionTAPP/timeDependentIntensityCorrection
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
              title: Analyte Estimation Method
              description: Whether elemental concentrations were calculated directly
                from measured X-ray intensities, or estimated by cation stoichiometry
                (e.g., oxygen calculated from cation proportions in silicates; carbon
                from stoichiometry in carbonates).
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/semCompositionTAPP/analyteEstimationMethod
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: analyteEstimationMethod
                schema:name:
                  const: Analyte Estimation Method
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
                  const: ada:analyteColumn/semCompositionTAPP/blankCorrection
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
              title: Primary Calibration Standard Name
              description: Name(s) of the primary reference material(s) used for intensity
                calibration in EDS or WDS quantification. Include the material name,
                its source or supplier, and a citation for the accepted values used,
                since results calibrated against different published values for the
                same material are not directly comparable.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/semCompositionTAPP/primaryCalibrationStandardName
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
          - contains:
              title: Secondary Reference Materials
              description: Quality-control reference material(s) analyzed alongside
                unknowns to verify calibration accuracy. Include material name, assessed
                elements, number of analyses (n), and measured vs. accepted values
                where available.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/semCompositionTAPP/secondaryReferenceMaterials
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: secondaryReferenceMaterials
                schema:name:
                  const: Secondary Reference Materials
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
              title: Interference Corrections Applied
              description: Whether a spectral interference correction was applied
                for each analyte. Common interferences include Ti Kb on V Ka, Cr Kb
                on Mn Ka, and Ba La on Ti Ka.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/semCompositionTAPP/interferenceCorrectionsApplied
                '@type':
                  const:
                  - schema:PropertyValueSpecification
                schema:valueName:
                  const: interferenceCorrectionsApplied
                schema:name:
                  const: Interference Corrections Applied
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
              title: Interfering Elements
              description: Element(s) whose X-ray lines overlap with the measured
                peak for one or more analytes, requiring a correction.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/semCompositionTAPP/interferingElements
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
                correction for each affected analyte.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/semCompositionTAPP/interferenceCorrectionStandard
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
                (n), and value per analyte or element group.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/semCompositionTAPP/analyticalPrecision
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
                material, reference value source, and per-analyte value.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/semCompositionTAPP/analyticalAccuracy
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
                sigma level stated. Derived from the counts on the analyte together
                with those on any background or blank subtracted from it. Distinct
                from the scatter actually observed within a measurement or between
                repeated measurements, which is recorded separately: where a procedure
                reports both, agreement indicates the measurement is shot-noise limited,
                and a larger observed scatter indicates a further source of variance."
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/semCompositionTAPP/countingStatisticsError
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
    schema:additionalProperty:
      type: array
      items:
        anyOf:
        - title: Beam Raster Dimensions
          description: "Dimensions of the small area over which the beam is rastered
            during a single analysis point, reported as width \xD7 height in \xB5m.
            Applicable when Beam Mode = Rastered; defines the effective spatial footprint
            of the measurement and distributes dose over a larger area to reduce beam
            damage on sensitive phases."
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
              type: string
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
            acquisition sequences, or rotating between multiple points. Particularly
            important for volatile-bearing phases, hydrous minerals, glasses, organic
            materials, and biological samples.'
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
            software, or reanalysis of a reference point at regular intervals. Particularly
            relevant for long mapping runs and high-magnification sessions where positional
            accuracy affects data quality.'
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
          description: For mapping modes, records whether the map was acquired by
            moving the stage while the beam is held fixed (stage scan) or by deflecting
            the beam across the field while the stage is stationary (beam scan). Stage
            scan is preferred for large areas or high-accuracy geometric fidelity;
            beam scan is faster for smaller fields but may introduce geometric distortion
            at the map edges.
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
              const: boolean
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
        - title: Detection Limit
          description: Method detection limit at 99% confidence, one per reported
            concentration variable (one per analyte, these being the same set). Include
            the method used and the resulting value for each.
          type: object
          properties:
            '@id':
              const: ada:parameter/semCompositionTAPP/detectionLimitDefault
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
          title: Beam Raster Dimensions
          description: "Dimensions of the small area over which the beam is rastered
            during a single analysis point, reported as width \xD7 height in \xB5m.
            Applicable when Beam Mode = Rastered; defines the effective spatial footprint
            of the measurement and distributes dose over a larger area to reduce beam
            damage on sensitive phases."
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
          title: Beam Damage Minimization
          description: 'Describes any measures taken to reduce electron beam damage
            to the sample during analysis. Examples: reduced accelerating voltage,
            lowered beam current, defocused or rastered beam, cooled stage, short
            acquisition sequences, or rotating between multiple points. Particularly
            important for volatile-bearing phases, hydrous minerals, glasses, organic
            materials, and biological samples.'
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
            software, or reanalysis of a reference point at regular intervals. Particularly
            relevant for long mapping runs and high-magnification sessions where positional
            accuracy affects data quality.'
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
          description: For mapping modes, records whether the map was acquired by
            moving the stage while the beam is held fixed (stage scan) or by deflecting
            the beam across the field while the stage is stationary (beam scan). Stage
            scan is preferred for large areas or high-accuracy geometric fidelity;
            beam scan is faster for smaller fields but may introduce geometric distortion
            at the map edges.
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
              const: boolean
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
      - contains:
          title: Detection Limit
          description: Method detection limit at 99% confidence, one per reported
            concentration variable (one per analyte, these being the same set). Include
            the method used and the resulting value for each.
          type: object
          properties:
            '@id':
              const: ada:parameter/semCompositionTAPP/detectionLimitDefault
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
    ada:channelTemplate:
      type: object
      properties:
        ada:channelColumns:
          type: array
          items:
            anyOf:
            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/ChannelIdentifierColumn
            - title: Dwell Time per Pixel
              description: Time the electron beam dwells on each pixel during raster
                scanning (imaging modes) or on each step position during compositional
                mapping (EDS and WDS mapping modes), in microseconds or milliseconds.
                Longer dwell time improves signal-to-noise and counting statistics
                but increases total dose and can cause beam damage or contamination
                on sensitive materials. For WDS mapping, the dwell time is per spectrometer
                per pixel.
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/semCompositionTAPP/dwellTimePerPixel
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
              description: X-ray emission line measured on each spectrometer assignment.
                Line choice affects sensitivity, matrix correction accuracy, and susceptibility
                to peak overlap and spectral interference.
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/semCompositionTAPP/xRayLine
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
              description: Analyzing crystal (monochromator) used on each spectrometer
                assignment. Crystal choice determines the detectable wavelength range
                and dispersion.
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/semCompositionTAPP/diffractingCrystal
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
              description: Order in which spectrometer assignments are acquired during
                point analysis. Relevant for minimizing beam damage (volatile elements
                measured first) and for sequential multi-channel setups. Not applicable
                to X-ray mapping, where all assigned spectrometers collect simultaneously
                at each pixel.
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/semCompositionTAPP/sequence
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
              description: Type of detector used on each spectrometer assignment.
                Affects sensitivity and count rate linearity.
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/semCompositionTAPP/proportionalCounterDetector
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
                  const: ada:channelColumn/semCompositionTAPP/wdsPhaSetting
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
            - title: Peak Counting Time
              description: Time spent counting X-ray intensity at the peak position,
                in seconds, on each spectrometer assignment. Procedure specifies standard
                values; analysts may adjust within procedure-defined bounds.
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/semCompositionTAPP/peakCountingTime
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
            - title: Background Counting Time
              description: Total time spent counting at off-peak background position(s)
                in seconds, summed across all background positions.
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/semCompositionTAPP/backgroundCountingTime
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
            - title: Background Position(s)
              description: Location(s) of off-peak background measurement(s) relative
                to the peak, in mm or sin-theta, and whether on the high- or low-energy
                side.
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/semCompositionTAPP/backgroundPosition
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
          allOf:
          - contains:
              title: Dwell Time per Pixel
              description: Time the electron beam dwells on each pixel during raster
                scanning (imaging modes) or on each step position during compositional
                mapping (EDS and WDS mapping modes), in microseconds or milliseconds.
                Longer dwell time improves signal-to-noise and counting statistics
                but increases total dose and can cause beam damage or contamination
                on sensitive materials. For WDS mapping, the dwell time is per spectrometer
                per pixel.
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/semCompositionTAPP/dwellTimePerPixel
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
              description: X-ray emission line measured on each spectrometer assignment.
                Line choice affects sensitivity, matrix correction accuracy, and susceptibility
                to peak overlap and spectral interference.
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/semCompositionTAPP/xRayLine
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
              description: Analyzing crystal (monochromator) used on each spectrometer
                assignment. Crystal choice determines the detectable wavelength range
                and dispersion.
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/semCompositionTAPP/diffractingCrystal
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
              description: Order in which spectrometer assignments are acquired during
                point analysis. Relevant for minimizing beam damage (volatile elements
                measured first) and for sequential multi-channel setups. Not applicable
                to X-ray mapping, where all assigned spectrometers collect simultaneously
                at each pixel.
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/semCompositionTAPP/sequence
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
              description: Type of detector used on each spectrometer assignment.
                Affects sensitivity and count rate linearity.
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/semCompositionTAPP/proportionalCounterDetector
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
                  const: ada:channelColumn/semCompositionTAPP/wdsPhaSetting
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
              title: Peak Counting Time
              description: Time spent counting X-ray intensity at the peak position,
                in seconds, on each spectrometer assignment. Procedure specifies standard
                values; analysts may adjust within procedure-defined bounds.
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/semCompositionTAPP/peakCountingTime
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
              title: Background Counting Time
              description: Total time spent counting at off-peak background position(s)
                in seconds, summed across all background positions.
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/semCompositionTAPP/backgroundCountingTime
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
              title: Background Position(s)
              description: Location(s) of off-peak background measurement(s) relative
                to the peak, in mm or sin-theta, and whether on the high- or low-energy
                side.
              type: object
              properties:
                '@id':
                  const: ada:channelColumn/semCompositionTAPP/backgroundPosition
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
    ada:edsAcquisitionMode:
      description: 'Spatial acquisition sub-strategy for EDS measurements: stationary-beam
        point acquisition, linescan (beam stepped along a transect at defined intervals),
        or area map (beam rastered over a pixel grid). Specifies how the beam is positioned
        during data collection within the declared Analytical Mode. Particularly important
        when a procedure includes linescans as a distinct acquisition approach not
        fully captured by the mode flag columns.'
      type: string
      enum:
      - Point / spot
      - Line scan
      - Map
      - Automated mineralogy
      - N/A
      - None
      - missing
      readOnly: true
    ada:edsLiveTimePerPointOrPixelDefault:
      description: EDS spectral acquisition live time per analysis point or per pixel
        in seconds. Longer live time improves counting statistics but increases beam
        damage risk and total acquisition time.
      anyOf:
      - type: number
      - type: string
    ada:stepSizePixelSizeDefault:
      description: "Centre-to-centre distance between adjacent measurement points
        (WDS mapping) or pixels (EDS mapping) in \xB5m. Defines the spatial sampling
        interval of the map and, together with the pixel-grid dimensions, determines
        the total mapped area. Smaller step sizes increase spatial resolution but
        extend acquisition time."
      anyOf:
      - type: number
      - type: string
    ada:matrixCorrectionMethod:
      description: X-ray matrix correction algorithm applied during quantitative EDS
        or WDS data reduction. For X-ray mapping, applies when raw count maps are
        converted to quantitative concentration maps.
      type: string
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
      readOnly: true
    ada:massAbsorptionCoefficients:
      description: Database of mass absorption coefficients used in the matrix correction.
        MAC database choice affects accuracy particularly for light elements (B, C,
        N, O, F, Na).
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
          description: Post-acquisition normalization applied using secondary reference
            materials to correct for session-to-session calibration drift.
          type: object
          properties:
            '@id':
              const: ada:parameter/semCompositionTAPP/normalizationStandardsBasedCorrectionDefault
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
          description: Method detection limit at 99% confidence, one per reported
            concentration variable (one per analyte, these being the same set). Include
            the method used and the resulting value for each.
          type: object
          properties:
            '@id':
              const: ada:parameter/semCompositionTAPP/detectionLimitDefault
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
        - title: Goodness-of-Fit or Dispersion Statistic
          description: The statistic reported to show whether scatter among the contributing
            analyses exceeds what analytical uncertainty alone predicts, together
            with its value. Answers whether a reported aggregate is defensible as
            a single population. Procedure-level tier is N/A because the value cannot
            be known before the analysis; the procedure may still state an acceptance
            threshold, which belongs with the inclusion criteria.
          type: object
          properties:
            '@id':
              const: ada:parameter/semCompositionTAPP/goodnessOfFitOrDispersionStatisticDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: goodnessOfFitOrDispersionStatisticDefault
            schema:name:
              const: Goodness-of-Fit or Dispersion Statistic
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
          title: Normalization / Standards-Based Correction
          description: Post-acquisition normalization applied using secondary reference
            materials to correct for session-to-session calibration drift.
          type: object
          properties:
            '@id':
              const: ada:parameter/semCompositionTAPP/normalizationStandardsBasedCorrectionDefault
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
          description: Method detection limit at 99% confidence, one per reported
            concentration variable (one per analyte, these being the same set). Include
            the method used and the resulting value for each.
          type: object
          properties:
            '@id':
              const: ada:parameter/semCompositionTAPP/detectionLimitDefault
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
      - contains:
          title: Goodness-of-Fit or Dispersion Statistic
          description: The statistic reported to show whether scatter among the contributing
            analyses exceeds what analytical uncertainty alone predicts, together
            with its value. Answers whether a reported aggregate is defensible as
            a single population. Procedure-level tier is N/A because the value cannot
            be known before the analysis; the procedure may still state an acceptance
            threshold, which belongs with the inclusion criteria.
          type: object
          properties:
            '@id':
              const: ada:parameter/semCompositionTAPP/goodnessOfFitOrDispersionStatisticDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: goodnessOfFitOrDispersionStatisticDefault
            schema:name:
              const: Goodness-of-Fit or Dispersion Statistic
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
    ada:wdsDeadTimeCorrection:
      description: "Method used to correct for WDS proportional counter dead time
        at high count rates. Dead time errors are most significant for major elements
        with high count rates (e.g., Si, Fe, Ca). Unlike EDS dead time \u2014 which
        is hardware-managed and reported as a session QC percentage (see EDS Dead
        Time) \u2014 WDS dead time correction is a user-selectable algorithm in the
        data reduction software. No separate measured WDS dead time value is reported;
        the correction is applied transparently during intensity-to-concentration
        conversion."
      type: string
      enum:
      - Default constant (manufacturer)
      - Adjusted constant
      - High-precision (Probe for EPMA)
      - Logarithmic
      - Unknown
      - N/A
      - None
      - missing
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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/tapp/context.jsonld)

## Sources

* [SEM_Composition_TAPP_v4.xlsx (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/SEM-Composition/tapp`

