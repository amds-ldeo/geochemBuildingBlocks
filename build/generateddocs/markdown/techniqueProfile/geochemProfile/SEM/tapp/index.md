
# SEM Technique-Aligned Protocol Profile (semTAPP) (Schema)

`ogch.techniqueProfile.geochemProfile.SEM.tapp` *v0.1*

Scanning electron microscopy superset (imaging + EDS/WDS composition + EBSD + FIB-SEM) extension of the base TAPP definition, generated from docs/SEM_TAPP_v4.xlsx via the path-driven pipeline.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### semTAPP example Garvie2008
semTAPP instance derived from Garvie et al. 2008 | Tagish Lake (C2) nanoglobules | SE Imaging (FEI Nova 200 NanoLab).
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
  "@id": "ex:semTAPP-Garvie2008",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol — Garvie2008",
  "schema:description": "Sample imaged without coating; initial ~5% beam-induced shrinkage observed upon first e-beam exposure; sample stable thereafter; focusing performed away from particles of interest to minimise beam exposure",
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
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
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
            "EDSDetector",
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
            "WDSSpectrometer",
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
            "xrayLine",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing"
        }
      ],
      "ada:acceleratingVoltageDefault": "500 V; 1 kV; 5 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
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
      "schema:name": "sem",
      "schema:termCode": "SEM"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-Garvie2008",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol \u2014 Garvie2008",
  "schema:description": "Sample imaged without coating; initial ~5% beam-induced shrinkage observed upon first e-beam exposure; sample stable thereafter; focusing performed away from particles of interest to minimise beam exposure",
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
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
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
            "EDSDetector",
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
            "WDSSpectrometer",
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
            "xrayLine",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing"
        }
      ],
      "ada:acceleratingVoltageDefault": "500 V; 1 kV; 5 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
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
      "schema:name": "sem",
      "schema:termCode": "SEM"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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

ex:semTAPP-Garvie2008 a cdi:Activity,
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
                    schema1:description "HCl and HF acid dissolution residue from pristine Tagish Lake pieces; deposited on lacey C TEM grid attached to Al-SEM stub; uncoated" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "Sample imaged without coating; initial ~5% beam-induced shrinkage observed upon first e-beam exposure; sample stable thereafter; focusing performed away from particles of interest to minimise beam exposure" ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "SEM" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "WDSSpectrometer" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "EDSDetector" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Electron source" ;
                    schema1:description "Unknown" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "xrayLine" ;
                    schema1:name "missing" ] ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "FEI / Thermo Fisher Scientific" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "Nova 200 NanoLab DualBeam" ] ;
            schema1:name "example instrumentName" ;
            ada:acceleratingVoltageDefault "500 V; 1 kV; 5 kV" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "School of Earth and Space Exploration / School of Materials, Arizona State University" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "sem" ;
            schema1:termCode "SEM" ] ;
    schema1:name "sem protocol — Garvie2008" ;
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
    ada:dwellTimePerPixelDefault -9999 ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:samplingUnit "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:wdsDeadTimeCorrection "missing" .


```


### semTAPP example Garvie2008-2
semTAPP instance derived from Garvie et al. 2008 | Tagish Lake (C2) nanoglobules | TEM Sample Preparation (FIB, FEI Nova 200 NanoLab).
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
  "@id": "ex:semTAPP-Garvie2008-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol — Garvie2008-2",
  "schema:description": "semTAPP instance derived from Garvie et al. 2008 | Tagish Lake (C2) nanoglobules | TEM Sample Preparation (FIB, FEI Nova 200 NanoLab) (publication column of SEM_TAPP_v17.xlsx).",
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
        "schema:name": "SE Imaging (same instrument, pre- and post-FIB milling)"
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
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
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
            "EDSDetector",
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
            "WDSSpectrometer",
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
            "xrayLine",
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
  "ada:analyticalMode": [
    "TEM Sample Preparation"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-Garvie2008-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol \u2014 Garvie2008-2",
  "schema:description": "semTAPP instance derived from Garvie et al. 2008 | Tagish Lake (C2) nanoglobules | TEM Sample Preparation (FIB, FEI Nova 200 NanoLab) (publication column of SEM_TAPP_v17.xlsx).",
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
        "schema:name": "SE Imaging (same instrument, pre- and post-FIB milling)"
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
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
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
            "EDSDetector",
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
            "WDSSpectrometer",
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
            "xrayLine",
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
  "ada:analyticalMode": [
    "TEM Sample Preparation"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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

ex:semTAPP-Garvie2008-2 a cdi:Activity,
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
                    schema1:description "HCl and HF acid dissolution residue from pristine Tagish Lake pieces; deposited on lacey C TEM grid attached to Al-SEM stub; uncoated" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "semTAPP instance derived from Garvie et al. 2008 | Tagish Lake (C2) nanoglobules | TEM Sample Preparation (FIB, FEI Nova 200 NanoLab) (publication column of SEM_TAPP_v17.xlsx)." ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "SEM" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "WDSSpectrometer" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "xrayLine" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Electron source" ;
                    schema1:description "Unknown" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "EDSDetector" ;
                    schema1:name "missing" ] ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "FEI / Thermo Fisher Scientific" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "Nova 200 NanoLab DualBeam" ] ;
            schema1:name "example instrumentName" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "School of Earth and Space Exploration / School of Materials, Arizona State University" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "sem" ;
            schema1:termCode "SEM" ] ;
    schema1:name "sem protocol — Garvie2008-2" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Carbonaceous nanoglobules, Tagish Lake (C2) meteorite (HCl/HF acid residue concentrate)" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SE Imaging (same instrument, pre- and post-FIB milling)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "TEM Sample Preparation" ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:samplingUnit "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:wdsDeadTimeCorrection "missing" .


```


### semTAPP example Genge2025
semTAPP instance derived from Genge et al. 2025 | Micrometeorite NG-1 (CV3-like) | BSE Imaging (ZEISS Sigma 1550VP, 10 kV).
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
  "@id": "ex:semTAPP-Genge2025",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol — Genge2025",
  "schema:description": "semTAPP instance derived from Genge et al. 2025 | Micrometeorite NG-1 (CV3-like) | BSE Imaging (ZEISS Sigma 1550VP, 10 kV) (publication column of SEM_TAPP_v17.xlsx).",
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
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
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
            "EDSDetector",
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
            "WDSSpectrometer",
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
            "xrayLine",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing"
        }
      ],
      "ada:acceleratingVoltageDefault": "10 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
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
      "schema:name": "sem",
      "schema:termCode": "SEM"
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
  "ada:dwellTimePerPixelDefault": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-Genge2025",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol \u2014 Genge2025",
  "schema:description": "semTAPP instance derived from Genge et al. 2025 | Micrometeorite NG-1 (CV3-like) | BSE Imaging (ZEISS Sigma 1550VP, 10 kV) (publication column of SEM_TAPP_v17.xlsx).",
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
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
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
            "EDSDetector",
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
            "WDSSpectrometer",
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
            "xrayLine",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing"
        }
      ],
      "ada:acceleratingVoltageDefault": "10 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
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
      "schema:name": "sem",
      "schema:termCode": "SEM"
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
  "ada:dwellTimePerPixelDefault": -9999,
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

ex:semTAPP-Genge2025 a cdi:Activity,
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
    schema1:description "semTAPP instance derived from Genge et al. 2025 | Micrometeorite NG-1 (CV3-like) | BSE Imaging (ZEISS Sigma 1550VP, 10 kV) (publication column of SEM_TAPP_v17.xlsx)." ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "SEM" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Electron source" ;
                    schema1:description "Unknown" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "EDSDetector" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "xrayLine" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "WDSSpectrometer" ;
                    schema1:name "missing" ] ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "Zeiss" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "ZEISS 1550VP" ] ;
            schema1:name "example instrumentName" ;
            ada:acceleratingVoltageDefault "10 kV" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "GPS Division Analytical Facility, California Institute of Technology" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "sem" ;
            schema1:termCode "SEM" ] ;
    schema1:name "sem protocol — Genge2025" ;
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
    ada:dwellTimePerPixelDefault -9999 ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:samplingUnit "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:wdsDeadTimeCorrection "missing" .


```


### semTAPP example Genge2025-2
semTAPP instance derived from Genge et al. 2025 | Micrometeorite NG-1 (CV3-like) | EDS Point Analysis (ZEISS Sigma 1550VP, 10 kV).
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
  "@id": "ex:semTAPP-Genge2025-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol — Genge2025-2",
  "schema:description": "semTAPP instance derived from Genge et al. 2025 | Micrometeorite NG-1 (CV3-like) | EDS Point Analysis (ZEISS Sigma 1550VP, 10 kV) (publication column of SEM_TAPP_v17.xlsx).",
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
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "EDSDetector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Oxford X-Max SDD system",
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
            "WDSSpectrometer",
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
            "xrayLine",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing"
        }
      ],
      "ada:acceleratingVoltageDefault": "10 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
    }
  ],
  "ada:analyticalMode": [
    "EDS"
  ],
  "ada:matrixCorrectionMethod": "XPP (Simplified PAP)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
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
  "ada:dwellTimePerPixelDefault": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-Genge2025-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol \u2014 Genge2025-2",
  "schema:description": "semTAPP instance derived from Genge et al. 2025 | Micrometeorite NG-1 (CV3-like) | EDS Point Analysis (ZEISS Sigma 1550VP, 10 kV) (publication column of SEM_TAPP_v17.xlsx).",
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
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "EDSDetector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Oxford X-Max SDD system",
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
            "WDSSpectrometer",
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
            "xrayLine",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing"
        }
      ],
      "ada:acceleratingVoltageDefault": "10 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
    }
  ],
  "ada:analyticalMode": [
    "EDS"
  ],
  "ada:matrixCorrectionMethod": "XPP (Simplified PAP)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
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
  "ada:dwellTimePerPixelDefault": -9999,
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

ex:semTAPP-Genge2025-2 a cdi:Activity,
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
    schema1:description "semTAPP instance derived from Genge et al. 2025 | Micrometeorite NG-1 (CV3-like) | EDS Point Analysis (ZEISS Sigma 1550VP, 10 kV) (publication column of SEM_TAPP_v17.xlsx)." ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "SEM" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Electron source" ;
                    schema1:description "Unknown" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "xrayLine" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "EDSDetector" ;
                    schema1:description "Oxford X-Max SDD system" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "WDSSpectrometer" ;
                    schema1:name "missing" ] ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "Zeiss" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "ZEISS 1550VP" ] ;
            schema1:name "example instrumentName" ;
            ada:acceleratingVoltageDefault "10 kV" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "GPS Division Analytical Facility, California Institute of Technology" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "sem" ;
            schema1:termCode "SEM" ] ;
    schema1:name "sem protocol — Genge2025-2" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Micrometeorite NG-1, Al-Cu-alloy-bearing, CV3-like composition; Democratic Republic of Congo" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "BSE Imaging (same session, same instrument); EBSD (same instrument); EPMA (JEOL JXA-iHP200F, WDS, out of scope)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "EDS" ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "XPP (Simplified PAP)" ;
    ada:samplingUnit "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:wdsDeadTimeCorrection "missing" .


```


### semTAPP example Genge2025-3
semTAPP instance derived from Genge et al. 2025 | Micrometeorite NG-1 (CV3-like) | EBSD (ZEISS Sigma 1550VP, 20 kV).
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
  "@id": "ex:semTAPP-Genge2025-3",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol — Genge2025-3",
  "schema:description": "EBSD done in variable pressure mode (25 Pa) to suppress charging on tilted sample; spatial resolution ~30 nm stated; calibrated with single-crystal silicon standard",
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
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
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
            "EDSDetector",
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
            "WDSSpectrometer",
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
            "xrayLine",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing"
        }
      ],
      "ada:acceleratingVoltageDefault": "20 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
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
      "schema:name": "sem",
      "schema:termCode": "SEM"
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
  "ada:dwellTimePerPixelDefault": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-Genge2025-3",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol \u2014 Genge2025-3",
  "schema:description": "EBSD done in variable pressure mode (25 Pa) to suppress charging on tilted sample; spatial resolution ~30 nm stated; calibrated with single-crystal silicon standard",
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
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
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
            "EDSDetector",
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
            "WDSSpectrometer",
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
            "xrayLine",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing"
        }
      ],
      "ada:acceleratingVoltageDefault": "20 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
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
      "schema:name": "sem",
      "schema:termCode": "SEM"
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
  "ada:dwellTimePerPixelDefault": -9999,
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

ex:semTAPP-Genge2025-3 a cdi:Activity,
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
    schema1:description "EBSD done in variable pressure mode (25 Pa) to suppress charging on tilted sample; spatial resolution ~30 nm stated; calibrated with single-crystal silicon standard" ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "SEM" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "EDSDetector" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Electron source" ;
                    schema1:description "Unknown" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "WDSSpectrometer" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "xrayLine" ;
                    schema1:name "missing" ] ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "Zeiss" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "ZEISS 1550VP" ] ;
            schema1:name "example instrumentName" ;
            ada:acceleratingVoltageDefault "20 kV" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "GPS Division Analytical Facility, California Institute of Technology" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "sem" ;
            schema1:termCode "SEM" ] ;
    schema1:name "sem protocol — Genge2025-3" ;
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
    ada:dwellTimePerPixelDefault -9999 ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:samplingUnit "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:wdsDeadTimeCorrection "missing" .


```


### semTAPP example Gucsik2013
semTAPP instance derived from Gucsik et al. 2013 | Forsterite, Kaba meteorite (CV3) | CL Mapping (JEOL JSM-5410LV).
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
  "@id": "ex:semTAPP-Gucsik2013",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol — Gucsik2013",
  "schema:description": "CL color imaging also done with separate luminoscope ELM-3R (cold cathode, 10 kV, 0.5 mA, <100 Torr) — standalone CL system, not SEM-based; spectrum deconvolution via Peak Analyzer in OriginPro 8J SR2",
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
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDSDetector",
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
            "Electron source",
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
            "WDSSpectrometer",
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
            "xrayLine",
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
  "ada:analyticalMode": [
    "CL"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
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
  "ada:dwellTimePerPixelDefault": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-Gucsik2013",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol \u2014 Gucsik2013",
  "schema:description": "CL color imaging also done with separate luminoscope ELM-3R (cold cathode, 10 kV, 0.5 mA, <100 Torr) \u2014 standalone CL system, not SEM-based; spectrum deconvolution via Peak Analyzer in OriginPro 8J SR2",
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
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDSDetector",
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
            "Electron source",
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
            "WDSSpectrometer",
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
            "xrayLine",
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
  "ada:analyticalMode": [
    "CL"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
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
  "ada:dwellTimePerPixelDefault": -9999,
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

ex:semTAPP-Gucsik2013 a cdi:Activity,
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
    schema1:description "CL color imaging also done with separate luminoscope ELM-3R (cold cathode, 10 kV, 0.5 mA, <100 Torr) — standalone CL system, not SEM-based; spectrum deconvolution via Peak Analyzer in OriginPro 8J SR2" ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "SEM" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "xrayLine" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "WDSSpectrometer" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Electron source" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "EDSDetector" ;
                    schema1:name "missing" ] ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "JEOL" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "JSM-5410LV" ] ;
            schema1:name "example instrumentName" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "sem" ;
            schema1:termCode "SEM" ] ;
    schema1:name "sem protocol — Gucsik2013" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Forsterite grains from Kaba (CV3) carbonaceous chondrite thin section" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "EDS and BSE Imaging (same instrument); EPMA with WDS (JEOL JXA-8900R, out of scope)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "CL" ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:samplingUnit "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:wdsDeadTimeCorrection "missing" .


```


### semTAPP example Gucsik2013-2
semTAPP instance derived from Gucsik et al. 2013 | Forsterite, Kaba meteorite (CV3) | EDS Point Analysis (JEOL JSM-5410LV).
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
  "@id": "ex:semTAPP-Gucsik2013-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol — Gucsik2013-2",
  "schema:description": "Described as semiquantitative; BSE images also captured with this instrument at same conditions; EPMA (JEOL JXA-8900R WDS) used for quantitative analyses (out of scope)",
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
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "EDSDetector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "ISIS analysis system (Oxford); detector type not specified",
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
            "Electron source",
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
            "WDSSpectrometer",
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
            "xrayLine",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
    }
  ],
  "ada:analyticalMode": [
    "EDS"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
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
  "ada:dwellTimePerPixelDefault": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-Gucsik2013-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol \u2014 Gucsik2013-2",
  "schema:description": "Described as semiquantitative; BSE images also captured with this instrument at same conditions; EPMA (JEOL JXA-8900R WDS) used for quantitative analyses (out of scope)",
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
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "EDSDetector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "ISIS analysis system (Oxford); detector type not specified",
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
            "Electron source",
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
            "WDSSpectrometer",
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
            "xrayLine",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
    }
  ],
  "ada:analyticalMode": [
    "EDS"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
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
  "ada:dwellTimePerPixelDefault": -9999,
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

ex:semTAPP-Gucsik2013-2 a cdi:Activity,
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
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "SEM" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "EDSDetector" ;
                    schema1:description "ISIS analysis system (Oxford); detector type not specified" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "xrayLine" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "WDSSpectrometer" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Electron source" ;
                    schema1:name "missing" ] ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "JEOL" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "JSM-5410LV" ] ;
            schema1:name "example instrumentName" ;
            ada:acceleratingVoltageDefault "15 kV" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "sem" ;
            schema1:termCode "SEM" ] ;
    schema1:name "sem protocol — Gucsik2013-2" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Forsterite grains from Kaba (CV3) carbonaceous chondrite thin section" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "CL (same instrument); BSE Imaging (same instrument, same session); EPMA with WDS (JEOL JXA-8900R, out of scope)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "EDS" ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:samplingUnit "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:wdsDeadTimeCorrection "missing" .


```


### semTAPP example Izawa2010
semTAPP instance derived from Izawa et al. 2010 | Tagish Lake (C2) meteorite | CL Mapping (Hitachi S-2500C).
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
  "@id": "ex:semTAPP-Izawa2010",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol — Izawa2010",
  "schema:description": "Digiscan II beam controller used for CL raster; multi-channel color CL distinguishes ~4 spectral bands; beam-induced CL may persist from long-lived IR emission in carbonates",
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
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Tungsten (W)",
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
            "EDSDetector",
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
            "WDSSpectrometer",
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
            "xrayLine",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing"
        }
      ],
      "ada:acceleratingVoltageDefault": "15–20 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
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
    "CL"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-Izawa2010",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol \u2014 Izawa2010",
  "schema:description": "Digiscan II beam controller used for CL raster; multi-channel color CL distinguishes ~4 spectral bands; beam-induced CL may persist from long-lived IR emission in carbonates",
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
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Tungsten (W)",
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
            "EDSDetector",
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
            "WDSSpectrometer",
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
            "xrayLine",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing"
        }
      ],
      "ada:acceleratingVoltageDefault": "15\u201320 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
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
    "CL"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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

ex:semTAPP-Izawa2010 a cdi:Activity,
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
    schema1:datePublished "missing" ;
    schema1:description "Digiscan II beam controller used for CL raster; multi-channel color CL distinguishes ~4 spectral bands; beam-induced CL may persist from long-lived IR emission in carbonates" ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "SEM" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Electron source" ;
                    schema1:description "Tungsten (W)" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "EDSDetector" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "xrayLine" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "WDSSpectrometer" ;
                    schema1:name "missing" ] ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "Hitachi" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "S-2500C" ] ;
            schema1:name "example instrumentName" ;
            ada:acceleratingVoltageDefault "15–20 kV" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "Zircon and Accessory Phase Laboratory, University of Western Ontario" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "sem" ;
            schema1:termCode "SEM" ] ;
    schema1:name "sem protocol — Izawa2010" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Tagish Lake (C2) ungrouped carbonaceous chondrite; polished thin sections" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SEM-EDX (Leo 440; Leo 1540); BSE Imaging; micro-XRD; EPMA-WDS (out of scope)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "CL" ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:samplingUnit "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:wdsDeadTimeCorrection "missing" ;
    bios:computationalTool [ schema1:name "Gatan DigitalMicrograph" ;
            ada:toolRole "dataReduction" ],
        [ schema1:name "Gatan DigitalMicrograph (CL image assembly)" ;
            ada:toolRole "acquisition" ] .


```


### semTAPP example Izawa2010-2
semTAPP instance derived from Izawa et al. 2010 | Tagish Lake (C2) meteorite | BSE Imaging (Leo 440).
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
  "@id": "ex:semTAPP-Izawa2010-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol — Izawa2010-2",
  "schema:description": "semTAPP instance derived from Izawa et al. 2010 | Tagish Lake (C2) meteorite | BSE Imaging (Leo 440) (publication column of SEM_TAPP_v17.xlsx).",
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
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDSDetector",
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
            "Electron source",
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
            "WDSSpectrometer",
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
            "xrayLine",
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
  "ada:analyticalMode": [
    "BSE Imaging"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
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
  "ada:dwellTimePerPixelDefault": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-Izawa2010-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol \u2014 Izawa2010-2",
  "schema:description": "semTAPP instance derived from Izawa et al. 2010 | Tagish Lake (C2) meteorite | BSE Imaging (Leo 440) (publication column of SEM_TAPP_v17.xlsx).",
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
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDSDetector",
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
            "Electron source",
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
            "WDSSpectrometer",
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
            "xrayLine",
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
  "ada:analyticalMode": [
    "BSE Imaging"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
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
  "ada:dwellTimePerPixelDefault": -9999,
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

ex:semTAPP-Izawa2010-2 a cdi:Activity,
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
    schema1:description "semTAPP instance derived from Izawa et al. 2010 | Tagish Lake (C2) meteorite | BSE Imaging (Leo 440) (publication column of SEM_TAPP_v17.xlsx)." ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "SEM" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "xrayLine" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "WDSSpectrometer" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Electron source" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "EDSDetector" ;
                    schema1:name "missing" ] ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "Zeiss" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "Leo 440" ] ;
            schema1:name "example instrumentName" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "Surface Science Western" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "sem" ;
            schema1:termCode "SEM" ] ;
    schema1:name "sem protocol — Izawa2010-2" ;
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
    ada:dwellTimePerPixelDefault -9999 ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:samplingUnit "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:wdsDeadTimeCorrection "missing" .


```


### semTAPP example Izawa2010-3
semTAPP instance derived from Izawa et al. 2010 | Tagish Lake (C2) meteorite | EDS Mapping (Leo 440).
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
  "@id": "ex:semTAPP-Izawa2010-3",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol — Izawa2010-3",
  "schema:description": "Full spectral imaging (Quartz XOne): all X-rays recorded per pixel, allowing post-hoc spectral analysis",
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
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "EDSDetector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Gresham light element detector; Quartz XOne EDX analysis system (full spectral imaging)",
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
            "Electron source",
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
            "WDSSpectrometer",
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
            "xrayLine",
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
  "ada:analyticalMode": [
    "EDS"
  ],
  "ada:edsAcquisitionMode": "Map",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
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
  "ada:dwellTimePerPixelDefault": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-Izawa2010-3",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol \u2014 Izawa2010-3",
  "schema:description": "Full spectral imaging (Quartz XOne): all X-rays recorded per pixel, allowing post-hoc spectral analysis",
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
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "EDSDetector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Gresham light element detector; Quartz XOne EDX analysis system (full spectral imaging)",
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
            "Electron source",
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
            "WDSSpectrometer",
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
            "xrayLine",
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
  "ada:analyticalMode": [
    "EDS"
  ],
  "ada:edsAcquisitionMode": "Map",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
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
  "ada:dwellTimePerPixelDefault": -9999,
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

ex:semTAPP-Izawa2010-3 a cdi:Activity,
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
    schema1:description "Full spectral imaging (Quartz XOne): all X-rays recorded per pixel, allowing post-hoc spectral analysis" ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "SEM" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "EDSDetector" ;
                    schema1:description "Gresham light element detector; Quartz XOne EDX analysis system (full spectral imaging)" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "WDSSpectrometer" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "xrayLine" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Electron source" ;
                    schema1:name "missing" ] ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "Zeiss" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "Leo 440" ] ;
            schema1:name "example instrumentName" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "Surface Science Western" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "sem" ;
            schema1:termCode "SEM" ] ;
    schema1:name "sem protocol — Izawa2010-3" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Tagish Lake (C2) ungrouped carbonaceous chondrite; polished thin sections" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "BSE Imaging (same instrument); CL (Hitachi S-2500C); micro-XRD; EPMA (out of scope)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "EDS" ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:edsAcquisitionMode "Map" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:samplingUnit "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:wdsDeadTimeCorrection "missing" .


```


### semTAPP example Izawa2010-4
semTAPP instance derived from Izawa et al. 2010 | Tagish Lake (C2) meteorite | BSE Imaging (Leo 1540 FIB/SEM CrossBeam).
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
  "@id": "ex:semTAPP-Izawa2010-4",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol — Izawa2010-4",
  "schema:description": "semTAPP instance derived from Izawa et al. 2010 | Tagish Lake (C2) meteorite | BSE Imaging (Leo 1540 FIB/SEM CrossBeam) (publication column of SEM_TAPP_v17.xlsx).",
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
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
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
            "EDSDetector",
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
            "WDSSpectrometer",
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
            "xrayLine",
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
  "ada:analyticalMode": [
    "BSE Imaging"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
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
  "ada:dwellTimePerPixelDefault": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-Izawa2010-4",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol \u2014 Izawa2010-4",
  "schema:description": "semTAPP instance derived from Izawa et al. 2010 | Tagish Lake (C2) meteorite | BSE Imaging (Leo 1540 FIB/SEM CrossBeam) (publication column of SEM_TAPP_v17.xlsx).",
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
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
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
            "EDSDetector",
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
            "WDSSpectrometer",
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
            "xrayLine",
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
  "ada:analyticalMode": [
    "BSE Imaging"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
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
  "ada:dwellTimePerPixelDefault": -9999,
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

ex:semTAPP-Izawa2010-4 a cdi:Activity,
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
    schema1:description "semTAPP instance derived from Izawa et al. 2010 | Tagish Lake (C2) meteorite | BSE Imaging (Leo 1540 FIB/SEM CrossBeam) (publication column of SEM_TAPP_v17.xlsx)." ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "SEM" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Electron source" ;
                    schema1:description "Unknown" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "WDSSpectrometer" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "EDSDetector" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "xrayLine" ;
                    schema1:name "missing" ] ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "Zeiss" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "Leo 1540 FIB/SEM CrossBeam" ] ;
            schema1:name "example instrumentName" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "Nanofabrication Laboratory, University of Western Ontario" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "sem" ;
            schema1:termCode "SEM" ] ;
    schema1:name "sem protocol — Izawa2010-4" ;
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
    ada:dwellTimePerPixelDefault -9999 ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:samplingUnit "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:wdsDeadTimeCorrection "missing" .


```


### semTAPP example Izawa2010-5
semTAPP instance derived from Izawa et al. 2010 | Tagish Lake (C2) meteorite | EDS Point Analysis (Leo 1540 FIB/SEM CrossBeam).
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
  "@id": "ex:semTAPP-Izawa2010-5",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol — Izawa2010-5",
  "schema:description": "Additional BSE and EDX analyses also carried out with Hitachi S-4300SE/N (Texas Tech) and Hitachi SU6600 (UWO) — not captured as separate assessment columns Reported detail: ada:edsAcquisitionMode = Point / spot; Map.",
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
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "EDSDetector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Oxford Instruments INCA EDX system",
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
            "WDSSpectrometer",
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
            "xrayLine",
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
  "ada:analyticalMode": [
    "EDS"
  ],
  "ada:edsAcquisitionMode": "Point / spot",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
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
  "ada:dwellTimePerPixelDefault": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-Izawa2010-5",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol \u2014 Izawa2010-5",
  "schema:description": "Additional BSE and EDX analyses also carried out with Hitachi S-4300SE/N (Texas Tech) and Hitachi SU6600 (UWO) \u2014 not captured as separate assessment columns Reported detail: ada:edsAcquisitionMode = Point / spot; Map.",
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
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "EDSDetector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Oxford Instruments INCA EDX system",
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
            "WDSSpectrometer",
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
            "xrayLine",
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
  "ada:analyticalMode": [
    "EDS"
  ],
  "ada:edsAcquisitionMode": "Point / spot",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
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
  "ada:dwellTimePerPixelDefault": -9999,
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

ex:semTAPP-Izawa2010-5 a cdi:Activity,
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
    schema1:description "Additional BSE and EDX analyses also carried out with Hitachi S-4300SE/N (Texas Tech) and Hitachi SU6600 (UWO) — not captured as separate assessment columns Reported detail: ada:edsAcquisitionMode = Point / spot; Map." ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "SEM" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "EDSDetector" ;
                    schema1:description "Oxford Instruments INCA EDX system" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "WDSSpectrometer" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Electron source" ;
                    schema1:description "Unknown" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "xrayLine" ;
                    schema1:name "missing" ] ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "Zeiss" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "Leo 1540 FIB/SEM CrossBeam" ] ;
            schema1:name "example instrumentName" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "Nanofabrication Laboratory, University of Western Ontario" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "sem" ;
            schema1:termCode "SEM" ] ;
    schema1:name "sem protocol — Izawa2010-5" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Tagish Lake (C2) ungrouped carbonaceous chondrite; polished thin sections" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "BSE Imaging (same instrument); CL (Hitachi S-2500C); micro-XRD; EPMA (out of scope)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "EDS" ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:edsAcquisitionMode "Point / spot" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:samplingUnit "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:wdsDeadTimeCorrection "missing" .


```


### semTAPP example Liu2017
semTAPP instance derived from Liu et al. 2017 | High-rank coal (Qinshui basin) | 3D Tomography (Carl Zeiss Crossbeam 540).
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
  "@id": "ex:semTAPP-Liu2017",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol — Liu2017",
  "schema:description": "semTAPP instance derived from Liu et al. 2017 | High-rank coal (Qinshui basin) | 3D Tomography (Carl Zeiss Crossbeam 540) (publication column of SEM_TAPP_v17.xlsx).",
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
        "schema:name": "X-ray CT (Xradia 520 Versa, Carl Zeiss)"
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
        "schema:description": "Small coal pillars (~2 mm diameter, 2 mm height) drilled orthogonal to bedding; polished with cross section polisher to remove ~1-2 µm oxide layer; no coating applied",
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
        "schema:name": "Crossbeam 540",
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
            "EDSDetector",
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
            "Electron source",
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
            "WDSSpectrometer",
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
            "xrayLine",
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
      "schema:name": "Avizo 7 (3D digital core software); Multiple-point geostatistics for pore network model"
    }
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-Liu2017",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol \u2014 Liu2017",
  "schema:description": "semTAPP instance derived from Liu et al. 2017 | High-rank coal (Qinshui basin) | 3D Tomography (Carl Zeiss Crossbeam 540) (publication column of SEM_TAPP_v17.xlsx).",
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
        "schema:name": "X-ray CT (Xradia 520 Versa, Carl Zeiss)"
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
        "schema:description": "Small coal pillars (~2 mm diameter, 2 mm height) drilled orthogonal to bedding; polished with cross section polisher to remove ~1-2 \u00b5m oxide layer; no coating applied",
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
        "schema:name": "Crossbeam 540",
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
            "EDSDetector",
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
            "Electron source",
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
            "WDSSpectrometer",
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
            "xrayLine",
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
      "schema:name": "Avizo 7 (3D digital core software); Multiple-point geostatistics for pore network model"
    }
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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

ex:semTAPP-Liu2017 a cdi:Activity,
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
                    schema1:description "Small coal pillars (~2 mm diameter, 2 mm height) drilled orthogonal to bedding; polished with cross section polisher to remove ~1-2 µm oxide layer; no coating applied" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "semTAPP instance derived from Liu et al. 2017 | High-rank coal (Qinshui basin) | 3D Tomography (Carl Zeiss Crossbeam 540) (publication column of SEM_TAPP_v17.xlsx)." ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "SEM" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "EDSDetector" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "WDSSpectrometer" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Electron source" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "xrayLine" ;
                    schema1:name "missing" ] ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "Zeiss" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "Crossbeam 540" ] ;
            schema1:name "example instrumentName" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "China University of Mining and Technology, Xuzhou, China" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "sem" ;
            schema1:termCode "SEM" ] ;
    schema1:name "sem protocol — Liu2017" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "High-rank coal (anthracite from Bofang Mine; lean coal from Yuwu Mine), southern Qinshui basin, China" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "X-ray CT (Xradia 520 Versa, Carl Zeiss)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:samplingUnit "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:wdsDeadTimeCorrection "missing" ;
    bios:computationalTool [ schema1:name "Avizo 7 (3D digital core software); Multiple-point geostatistics for pore network model" ;
            ada:toolRole "dataReduction" ] .


```


### semTAPP example Liu2017-2
semTAPP instance derived from Liu et al. 2017 | High-rank coal (Qinshui basin) | SE Imaging (ESEM Quanta 250).
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
  "@id": "ex:semTAPP-Liu2017-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol — Liu2017-2",
  "schema:description": "Pore and mineral sizes >0.1 µm measured; minerals analyzed via EDS (surface energy spectrum analysis); magnification range 10³ to 10⁴",
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
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDSDetector",
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
            "Electron source",
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
            "WDSSpectrometer",
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
            "xrayLine",
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
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-Liu2017-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol \u2014 Liu2017-2",
  "schema:description": "Pore and mineral sizes >0.1 \u00b5m measured; minerals analyzed via EDS (surface energy spectrum analysis); magnification range 10\u00b3 to 10\u2074",
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
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDSDetector",
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
            "Electron source",
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
            "WDSSpectrometer",
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
            "xrayLine",
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
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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

ex:semTAPP-Liu2017-2 a cdi:Activity,
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
    schema1:datePublished "missing" ;
    schema1:description "Pore and mineral sizes >0.1 µm measured; minerals analyzed via EDS (surface energy spectrum analysis); magnification range 10³ to 10⁴" ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "SEM" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "xrayLine" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Electron source" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "WDSSpectrometer" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "EDSDetector" ;
                    schema1:name "missing" ] ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "Unknown" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "Quanta 250" ] ;
            schema1:name "example instrumentName" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "China University of Mining and Technology, Xuzhou, China" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "sem" ;
            schema1:termCode "SEM" ] ;
    schema1:name "sem protocol — Liu2017-2" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "High-rank coal (anthracite from Bofang Mine; lean coal from Yuwu Mine), southern Qinshui basin, China" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "FIB-SEM (Crossbeam 540) for 3D tomography; EDS for mineral analysis" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:samplingUnit "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:wdsDeadTimeCorrection "missing" .


```


### semTAPP example Liu2017-3
semTAPP instance derived from Liu et al. 2017 | High-rank coal (Qinshui basin) | SE Imaging (FESEM SUPRA 55).
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
  "@id": "ex:semTAPP-Liu2017-3",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol — Liu2017-3",
  "schema:description": "Pore and mineral sizes >20 nm to <5 µm measured; EDS also used for mineral analysis; magnification range 10³ to 10⁵",
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
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
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
            "EDSDetector",
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
            "WDSSpectrometer",
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
            "xrayLine",
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
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-Liu2017-3",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol \u2014 Liu2017-3",
  "schema:description": "Pore and mineral sizes >20 nm to <5 \u00b5m measured; EDS also used for mineral analysis; magnification range 10\u00b3 to 10\u2075",
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
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
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
            "EDSDetector",
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
            "WDSSpectrometer",
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
            "xrayLine",
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
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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

ex:semTAPP-Liu2017-3 a cdi:Activity,
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
    schema1:datePublished "missing" ;
    schema1:description "Pore and mineral sizes >20 nm to <5 µm measured; EDS also used for mineral analysis; magnification range 10³ to 10⁵" ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "SEM" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "WDSSpectrometer" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "EDSDetector" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "xrayLine" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Electron source" ;
                    schema1:description "Unknown" ;
                    schema1:name "missing" ] ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "Zeiss" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "SUPRA 55" ] ;
            schema1:name "example instrumentName" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "China University of Mining and Technology, Xuzhou, China" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "sem" ;
            schema1:termCode "SEM" ] ;
    schema1:name "sem protocol — Liu2017-3" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "High-rank coal (anthracite from Bofang Mine; lean coal from Yuwu Mine), southern Qinshui basin, China" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "FIB-SEM (Crossbeam 540) for 3D tomography; EDS for mineral analysis" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:samplingUnit "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:wdsDeadTimeCorrection "missing" .


```


### semTAPP example Ma2017
semTAPP instance derived from Ma et al. 2017 | Khatyrka CV3 chondrite (metal phases) | BSE Imaging (ZEISS 1550VP FE-SEM).
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
  "@id": "ex:semTAPP-Ma2017",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol — Ma2017",
  "schema:description": "BSE images obtained from both ZEISS 1550VP FE-SEM and JEOL 8200 electron microprobe (EPMA); quantitative EPMA on JEOL 8200 at 12 kV, 5 nA (out of scope for SEM TAPP)",
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
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
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
            "EDSDetector",
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
            "WDSSpectrometer",
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
            "xrayLine",
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
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-Ma2017",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol \u2014 Ma2017",
  "schema:description": "BSE images obtained from both ZEISS 1550VP FE-SEM and JEOL 8200 electron microprobe (EPMA); quantitative EPMA on JEOL 8200 at 12 kV, 5 nA (out of scope for SEM TAPP)",
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
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
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
            "EDSDetector",
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
            "WDSSpectrometer",
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
            "xrayLine",
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
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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

ex:semTAPP-Ma2017 a cdi:Activity,
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
                    schema1:description "Polished thin section (section 126A prepared from Grain 126); no coating or SEM-specific preparation stated" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "BSE images obtained from both ZEISS 1550VP FE-SEM and JEOL 8200 electron microprobe (EPMA); quantitative EPMA on JEOL 8200 at 12 kV, 5 nA (out of scope for SEM TAPP)" ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "SEM" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "xrayLine" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Electron source" ;
                    schema1:description "Unknown" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "EDSDetector" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "WDSSpectrometer" ;
                    schema1:name "missing" ] ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "Zeiss" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "1550VP" ] ;
            schema1:name "example instrumentName" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "Caltech GPS Analytical Facility, California Institute of Technology, Pasadena, CA, USA" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "sem" ;
            schema1:termCode "SEM" ] ;
    schema1:name "sem protocol — Ma2017" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Khatyrka CV3 carbonaceous chondrite; Al-Cu-Fe alloy metal phases (hollisterite, kryachkoite, stolperite, khatyrkite, icosahedrite) in section 126A" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "EBSD (ZEISS 1550VP FE-SEM); EPMA (JEOL 8200, separate instrument)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:samplingUnit "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:wdsDeadTimeCorrection "missing" .


```


### semTAPP example Ma2017-2
semTAPP instance derived from Ma et al. 2017 | Khatyrka CV3 chondrite (metal phases) | EBSD (ZEISS 1550VP FE-SEM, HKL system, 20 kV).
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
  "@id": "ex:semTAPP-Ma2017-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol — Ma2017-2",
  "schema:description": "EBSD performed at Caltech GPS Analytical Facility; EPMA (JEOL 8200) used for quantitative chemical analysis (out of scope for SEM TAPP)",
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
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
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
            "EDSDetector",
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
            "WDSSpectrometer",
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
            "xrayLine",
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
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-Ma2017-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol \u2014 Ma2017-2",
  "schema:description": "EBSD performed at Caltech GPS Analytical Facility; EPMA (JEOL 8200) used for quantitative chemical analysis (out of scope for SEM TAPP)",
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
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
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
            "EDSDetector",
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
            "WDSSpectrometer",
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
            "xrayLine",
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
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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

ex:semTAPP-Ma2017-2 a cdi:Activity,
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
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "EBSD performed at Caltech GPS Analytical Facility; EPMA (JEOL 8200) used for quantitative chemical analysis (out of scope for SEM TAPP)" ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "SEM" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Electron source" ;
                    schema1:description "Unknown" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "xrayLine" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "EDSDetector" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "WDSSpectrometer" ;
                    schema1:name "missing" ] ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "Zeiss" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "1550VP" ] ;
            schema1:name "example instrumentName" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "Caltech GPS Analytical Facility, California Institute of Technology, Pasadena, CA, USA" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "sem" ;
            schema1:termCode "SEM" ] ;
    schema1:name "sem protocol — Ma2017-2" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Khatyrka CV3 carbonaceous chondrite; Al-Cu-Fe alloy metal phases (hollisterite, kryachkoite, stolperite, khatyrkite, icosahedrite) in section 126A" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "BSE Imaging (ZEISS 1550VP FE-SEM); EPMA (JEOL 8200, separate instrument)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:samplingUnit "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:wdsDeadTimeCorrection "missing" .


```


### semTAPP example Pascucci2026
semTAPP instance derived from Pascucci et al. 2026 | NWA 7317 CR6 chondrite | BSE Imaging (Zeiss Supra 40 FE-SEM, 20 kV).
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
  "@id": "ex:semTAPP-Pascucci2026",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol — Pascucci2026",
  "schema:description": "10 BSE images acquired at ×138 magnification and mosaicked (4 consecutive per row) to cover ~9.7 mm area matching SPIM imagery",
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
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
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
            "EDSDetector",
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
            "WDSSpectrometer",
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
            "xrayLine",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing"
        }
      ],
      "ada:acceleratingVoltageDefault": "20 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
    }
  ],
  "bios:computationalTool": [
    {
      "ada:toolRole": "acquisition",
      "schema:name": "Oxford INCA Energy"
    }
  ],
  "ada:analyticalMode": [
    "N/A"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-Pascucci2026",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol \u2014 Pascucci2026",
  "schema:description": "10 BSE images acquired at \u00d7138 magnification and mosaicked (4 consecutive per row) to cover ~9.7 mm area matching SPIM imagery",
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
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
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
            "EDSDetector",
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
            "WDSSpectrometer",
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
            "xrayLine",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing"
        }
      ],
      "ada:acceleratingVoltageDefault": "20 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
    }
  ],
  "bios:computationalTool": [
    {
      "ada:toolRole": "acquisition",
      "schema:name": "Oxford INCA Energy"
    }
  ],
  "ada:analyticalMode": [
    "N/A"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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

ex:semTAPP-Pascucci2026 a cdi:Activity,
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
    schema1:datePublished "missing" ;
    schema1:description "10 BSE images acquired at ×138 magnification and mosaicked (4 consecutive per row) to cover ~9.7 mm area matching SPIM imagery" ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "SEM" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "xrayLine" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "WDSSpectrometer" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Electron source" ;
                    schema1:description "Unknown" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "EDSDetector" ;
                    schema1:name "missing" ] ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "Zeiss" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "Supra 40" ] ;
            schema1:name "example instrumentName" ;
            ada:acceleratingVoltageDefault "20 kV" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "CNR IMAA (Institute of Methodologies for Environmental Analysis), Italian National Research Council, Potenza, Italy" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "sem" ;
            schema1:termCode "SEM" ] ;
    schema1:name "sem protocol — Pascucci2026" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "NWA 7317 CR6 carbonaceous chondrite; polished slab (~10×6 mm fragment, 10.01g)" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "EDS (Zeiss Supra 40 FE-SEM); SE Imaging (Zeiss Supra 40 FE-SEM); EMPA-WDS (JEOL JXA-8230, separate instrument); VIS-IR spectroscopy (SPIM)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "N/A" ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:samplingUnit "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:wdsDeadTimeCorrection "missing" ;
    bios:computationalTool [ schema1:name "Oxford INCA Energy" ;
            ada:toolRole "acquisition" ] .


```


### semTAPP example Pascucci2026-2
semTAPP instance derived from Pascucci et al. 2026 | NWA 7317 CR6 chondrite | EDS Point Analysis (Zeiss Supra 40 FE-SEM, 20 kV).
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
  "@id": "ex:semTAPP-Pascucci2026-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol — Pascucci2026-2",
  "schema:description": "Spot analysis: 20 kV, 30 µm aperture, 30 s live time per spot, maximum process time (Oxford INCA Energy)",
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
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "EDSDetector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Oxford INCA Energy 350; X-ACT LN2-free Silicon Drift Detector (SDD)",
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
            "WDSSpectrometer",
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
            "xrayLine",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing"
        }
      ],
      "ada:acceleratingVoltageDefault": "20 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
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
    "N/A"
  ],
  "ada:edsAcquisitionMode": "N/A",
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
        "@id": "ada:analyteColumn/semTAPP/beamCurrent",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "beamCurrent",
        "schema:name": "Beam Current",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:analyteColumn/semTAPP/techniquePerAnalyte",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "techniquePerAnalyte",
        "schema:name": "Technique per Analyte",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/diffractingCrystal",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "diffractingCrystal",
        "schema:name": "Diffracting Crystal",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/wdsSpectrometerChannel",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "wdsSpectrometerChannel",
        "schema:name": "WDS Spectrometer Channel",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/proportionalCounterDetector",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "proportionalCounterDetector",
        "schema:name": "Proportional Counter / Detector",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/wdsPhaSetting",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "wdsPhaSetting",
        "schema:name": "WDS PHA Setting",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:analyteColumn/semTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:analyteColumn/semTAPP/backgroundPosition",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundPosition",
        "schema:name": "Background Position(s)",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/backgroundCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCorrectionMethod",
        "schema:name": "Background Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/timeDependentIntensityCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "timeDependentIntensityCorrection",
        "schema:name": "Time-Dependent Intensity Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/analyteEstimationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyteEstimationMethod",
        "schema:name": "Analyte Estimation Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/blankCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "blankCorrection",
        "schema:name": "Blank Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/primaryCalibrationStandardName",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "primaryCalibrationStandardName",
        "schema:name": "Primary Calibration Standard Name",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/secondaryReferenceMaterials",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "secondaryReferenceMaterials",
        "schema:name": "Secondary Reference Materials",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/interferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionsApplied",
        "schema:name": "Interference Corrections Applied",
        "ada:dataType": "boolean",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/interferingElements",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingElements",
        "schema:name": "Interfering Elements",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/interferenceCorrectionStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionStandard",
        "schema:name": "Interference Correction Standard",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/analyticalPrecision",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalPrecision",
        "schema:name": "Analytical Precision",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/analyticalAccuracy",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracy",
        "schema:name": "Analytical Accuracy",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:edsLiveTimePerPointOrPixelDefault": "30 s live time per spot analysis",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/semTAPP/edsSpectralProcessingType",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/semTAPP/edsSpectralProcessingType"
        }
      ],
      "schema:name": "EDS Spectral Processing Type",
      "schema:value": "Semi-quantitative analysis with virtual standards (Oxford INCA Energy); mineral phase determination from atomic % of constituent elements"
    }
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-Pascucci2026-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol \u2014 Pascucci2026-2",
  "schema:description": "Spot analysis: 20 kV, 30 \u00b5m aperture, 30 s live time per spot, maximum process time (Oxford INCA Energy)",
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
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "EDSDetector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Oxford INCA Energy 350; X-ACT LN2-free Silicon Drift Detector (SDD)",
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
            "WDSSpectrometer",
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
            "xrayLine",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing"
        }
      ],
      "ada:acceleratingVoltageDefault": "20 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
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
    "N/A"
  ],
  "ada:edsAcquisitionMode": "N/A",
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
        "@id": "ada:analyteColumn/semTAPP/beamCurrent",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "beamCurrent",
        "schema:name": "Beam Current",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:analyteColumn/semTAPP/techniquePerAnalyte",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "techniquePerAnalyte",
        "schema:name": "Technique per Analyte",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/diffractingCrystal",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "diffractingCrystal",
        "schema:name": "Diffracting Crystal",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/wdsSpectrometerChannel",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "wdsSpectrometerChannel",
        "schema:name": "WDS Spectrometer Channel",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/proportionalCounterDetector",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "proportionalCounterDetector",
        "schema:name": "Proportional Counter / Detector",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/wdsPhaSetting",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "wdsPhaSetting",
        "schema:name": "WDS PHA Setting",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:analyteColumn/semTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:analyteColumn/semTAPP/backgroundPosition",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundPosition",
        "schema:name": "Background Position(s)",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/backgroundCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCorrectionMethod",
        "schema:name": "Background Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/timeDependentIntensityCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "timeDependentIntensityCorrection",
        "schema:name": "Time-Dependent Intensity Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/analyteEstimationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyteEstimationMethod",
        "schema:name": "Analyte Estimation Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/blankCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "blankCorrection",
        "schema:name": "Blank Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/primaryCalibrationStandardName",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "primaryCalibrationStandardName",
        "schema:name": "Primary Calibration Standard Name",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/secondaryReferenceMaterials",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "secondaryReferenceMaterials",
        "schema:name": "Secondary Reference Materials",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/interferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionsApplied",
        "schema:name": "Interference Corrections Applied",
        "ada:dataType": "boolean",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/interferingElements",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingElements",
        "schema:name": "Interfering Elements",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/interferenceCorrectionStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionStandard",
        "schema:name": "Interference Correction Standard",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/analyticalPrecision",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalPrecision",
        "schema:name": "Analytical Precision",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/analyticalAccuracy",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracy",
        "schema:name": "Analytical Accuracy",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/countingStatisticsError",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "countingStatisticsError",
        "schema:name": "Counting Statistics Error",
        "ada:dataType": "string"
      }
    ]
  },
  "ada:edsLiveTimePerPointOrPixelDefault": "30 s live time per spot analysis",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/semTAPP/edsSpectralProcessingType",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/semTAPP/edsSpectralProcessingType"
        }
      ],
      "schema:name": "EDS Spectral Processing Type",
      "schema:value": "Semi-quantitative analysis with virtual standards (Oxford INCA Energy); mineral phase determination from atomic % of constituent elements"
    }
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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

ex:semTAPP-Pascucci2026-2 a cdi:Activity,
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
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semTAPP/edsSpectralProcessingType> ;
    schema1:datePublished "missing" ;
    schema1:description "Spot analysis: 20 kV, 30 µm aperture, 30 s live time per spot, maximum process time (Oxford INCA Energy)" ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "SEM" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "WDSSpectrometer" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "xrayLine" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "EDSDetector" ;
                    schema1:description "Oxford INCA Energy 350; X-ACT LN2-free Silicon Drift Detector (SDD)" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Electron source" ;
                    schema1:description "Unknown" ;
                    schema1:name "missing" ] ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "Zeiss" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "Supra 40" ] ;
            schema1:name "example instrumentName" ;
            ada:acceleratingVoltageDefault "20 kV" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "CNR IMAA (Institute of Methodologies for Environmental Analysis), Italian National Research Council, Potenza, Italy" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "sem" ;
            schema1:termCode "SEM" ] ;
    schema1:name "sem protocol — Pascucci2026-2" ;
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
                <https://ada.astromat.org/metadata/analyteColumn/semTAPP/analyteEstimationMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/semTAPP/analyticalAccuracy>,
                <https://ada.astromat.org/metadata/analyteColumn/semTAPP/analyticalPrecision>,
                <https://ada.astromat.org/metadata/analyteColumn/semTAPP/backgroundCorrectionMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/semTAPP/backgroundCountingTime>,
                <https://ada.astromat.org/metadata/analyteColumn/semTAPP/backgroundPosition>,
                <https://ada.astromat.org/metadata/analyteColumn/semTAPP/beamCurrent>,
                <https://ada.astromat.org/metadata/analyteColumn/semTAPP/blankCorrection>,
                <https://ada.astromat.org/metadata/analyteColumn/semTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/analyteColumn/semTAPP/diffractingCrystal>,
                <https://ada.astromat.org/metadata/analyteColumn/semTAPP/interferenceCorrectionStandard>,
                <https://ada.astromat.org/metadata/analyteColumn/semTAPP/interferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/analyteColumn/semTAPP/interferingElements>,
                <https://ada.astromat.org/metadata/analyteColumn/semTAPP/peakCountingTime>,
                <https://ada.astromat.org/metadata/analyteColumn/semTAPP/primaryCalibrationStandardName>,
                <https://ada.astromat.org/metadata/analyteColumn/semTAPP/proportionalCounterDetector>,
                <https://ada.astromat.org/metadata/analyteColumn/semTAPP/secondaryReferenceMaterials>,
                <https://ada.astromat.org/metadata/analyteColumn/semTAPP/techniquePerAnalyte>,
                <https://ada.astromat.org/metadata/analyteColumn/semTAPP/timeDependentIntensityCorrection>,
                <https://ada.astromat.org/metadata/analyteColumn/semTAPP/wdsPhaSetting>,
                <https://ada.astromat.org/metadata/analyteColumn/semTAPP/wdsSpectrometerChannel> ;
            ada:defaultAnalytes "Al",
                "Ca",
                "Fe",
                "Mg",
                "Na",
                "Ni",
                "S",
                "Si" ] ;
    ada:analyticalMode "N/A" ;
    ada:dwellTimePerPixelDefault -9999 ;
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

<https://ada.astromat.org/metadata/analyteColumn/semTAPP/analyteEstimationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Analyte Estimation Method" ;
    schema1:valueName "analyteEstimationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semTAPP/analyticalAccuracy> a schema1:PropertyValueSpecification ;
    schema1:name "Analytical Accuracy" ;
    schema1:valueName "analyticalAccuracy" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semTAPP/analyticalPrecision> a schema1:PropertyValueSpecification ;
    schema1:name "Analytical Precision" ;
    schema1:valueName "analyticalPrecision" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semTAPP/backgroundCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Background Correction Method" ;
    schema1:valueName "backgroundCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semTAPP/backgroundCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Background Counting Time" ;
    schema1:valueName "backgroundCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/semTAPP/backgroundPosition> a schema1:PropertyValueSpecification ;
    schema1:name "Background Position(s)" ;
    schema1:valueName "backgroundPosition" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semTAPP/beamCurrent> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Beam Current" ;
    schema1:valueName "beamCurrent" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/semTAPP/blankCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Blank Correction" ;
    schema1:valueName "blankCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semTAPP/diffractingCrystal> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Diffracting Crystal" ;
    schema1:valueName "diffractingCrystal" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semTAPP/interferenceCorrectionStandard> a schema1:PropertyValueSpecification ;
    schema1:name "Interference Correction Standard" ;
    schema1:valueName "interferenceCorrectionStandard" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semTAPP/interferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Corrections Applied" ;
    schema1:valueName "interferenceCorrectionsApplied" ;
    ada:dataType "boolean" .

<https://ada.astromat.org/metadata/analyteColumn/semTAPP/interferingElements> a schema1:PropertyValueSpecification ;
    schema1:name "Interfering Elements" ;
    schema1:valueName "interferingElements" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semTAPP/peakCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Peak Counting Time" ;
    schema1:valueName "peakCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/semTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semTAPP/proportionalCounterDetector> a schema1:PropertyValueSpecification ;
    schema1:name "Proportional Counter / Detector" ;
    schema1:valueName "proportionalCounterDetector" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semTAPP/secondaryReferenceMaterials> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Secondary Reference Materials" ;
    schema1:valueName "secondaryReferenceMaterials" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semTAPP/techniquePerAnalyte> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Technique per Analyte" ;
    schema1:valueName "techniquePerAnalyte" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semTAPP/timeDependentIntensityCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Time-Dependent Intensity Correction" ;
    schema1:valueName "timeDependentIntensityCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semTAPP/wdsPhaSetting> a schema1:PropertyValueSpecification ;
    schema1:name "WDS PHA Setting" ;
    schema1:valueName "wdsPhaSetting" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semTAPP/wdsSpectrometerChannel> a schema1:PropertyValueSpecification ;
    schema1:name "WDS Spectrometer Channel" ;
    schema1:valueName "wdsSpectrometerChannel" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/semTAPP/edsSpectralProcessingType> a schema1:PropertyValue ;
    schema1:name "EDS Spectral Processing Type" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/edsSpectralProcessingType> ;
    schema1:value "Semi-quantitative analysis with virtual standards (Oxford INCA Energy); mineral phase determination from atomic % of constituent elements" .


```


### semTAPP example Pascucci2026-3
semTAPP instance derived from Pascucci et al. 2026 | NWA 7317 CR6 chondrite | EDS Mapping (Zeiss Supra 40 FE-SEM, 20 kV).
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
  "@id": "ex:semTAPP-Pascucci2026-3",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol — Pascucci2026-3",
  "schema:description": "EDS mapping: 20 kV, 60 µm aperture, 5 ms dwell per pixel, 1024×768 pixels, 2.5 µm pixel size, ~10 h total; element maps co-registered with BSE images Reported detail: ada:edsAcquisitionMode = Element mapping.",
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
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "EDSDetector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Oxford INCA Energy 350; X-ACT LN2-free Silicon Drift Detector (SDD)",
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
            "WDSSpectrometer",
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
            "xrayLine",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing"
        }
      ],
      "ada:acceleratingVoltageDefault": "20 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
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
    "N/A"
  ],
  "ada:edsAcquisitionMode": "Map",
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
        "@id": "ada:analyteColumn/semTAPP/beamCurrent",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "beamCurrent",
        "schema:name": "Beam Current",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:analyteColumn/semTAPP/techniquePerAnalyte",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "techniquePerAnalyte",
        "schema:name": "Technique per Analyte",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/diffractingCrystal",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "diffractingCrystal",
        "schema:name": "Diffracting Crystal",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/wdsSpectrometerChannel",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "wdsSpectrometerChannel",
        "schema:name": "WDS Spectrometer Channel",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/proportionalCounterDetector",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "proportionalCounterDetector",
        "schema:name": "Proportional Counter / Detector",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/wdsPhaSetting",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "wdsPhaSetting",
        "schema:name": "WDS PHA Setting",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:analyteColumn/semTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:analyteColumn/semTAPP/backgroundPosition",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundPosition",
        "schema:name": "Background Position(s)",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/backgroundCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCorrectionMethod",
        "schema:name": "Background Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/timeDependentIntensityCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "timeDependentIntensityCorrection",
        "schema:name": "Time-Dependent Intensity Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/analyteEstimationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyteEstimationMethod",
        "schema:name": "Analyte Estimation Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/blankCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "blankCorrection",
        "schema:name": "Blank Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/primaryCalibrationStandardName",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "primaryCalibrationStandardName",
        "schema:name": "Primary Calibration Standard Name",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/secondaryReferenceMaterials",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "secondaryReferenceMaterials",
        "schema:name": "Secondary Reference Materials",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/interferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionsApplied",
        "schema:name": "Interference Corrections Applied",
        "ada:dataType": "boolean",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/interferingElements",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingElements",
        "schema:name": "Interfering Elements",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/interferenceCorrectionStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionStandard",
        "schema:name": "Interference Correction Standard",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/analyticalPrecision",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalPrecision",
        "schema:name": "Analytical Precision",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/analyticalAccuracy",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracy",
        "schema:name": "Analytical Accuracy",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/countingStatisticsError",
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
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/semTAPP/edsSpectralProcessingType",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/semTAPP/edsSpectralProcessingType"
        }
      ],
      "schema:name": "EDS Spectral Processing Type",
      "schema:value": "Semi-quantitative analysis with virtual standards (Oxford INCA Energy); mineral phase determination from atomic % of constituent elements"
    }
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-Pascucci2026-3",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol \u2014 Pascucci2026-3",
  "schema:description": "EDS mapping: 20 kV, 60 \u00b5m aperture, 5 ms dwell per pixel, 1024\u00d7768 pixels, 2.5 \u00b5m pixel size, ~10 h total; element maps co-registered with BSE images Reported detail: ada:edsAcquisitionMode = Element mapping.",
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
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "EDSDetector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Oxford INCA Energy 350; X-ACT LN2-free Silicon Drift Detector (SDD)",
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
            "WDSSpectrometer",
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
            "xrayLine",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing"
        }
      ],
      "ada:acceleratingVoltageDefault": "20 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
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
    "N/A"
  ],
  "ada:edsAcquisitionMode": "Map",
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
        "@id": "ada:analyteColumn/semTAPP/beamCurrent",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "beamCurrent",
        "schema:name": "Beam Current",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:analyteColumn/semTAPP/techniquePerAnalyte",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "techniquePerAnalyte",
        "schema:name": "Technique per Analyte",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/diffractingCrystal",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "diffractingCrystal",
        "schema:name": "Diffracting Crystal",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/wdsSpectrometerChannel",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "wdsSpectrometerChannel",
        "schema:name": "WDS Spectrometer Channel",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/proportionalCounterDetector",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "proportionalCounterDetector",
        "schema:name": "Proportional Counter / Detector",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/wdsPhaSetting",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "wdsPhaSetting",
        "schema:name": "WDS PHA Setting",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/peakCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "peakCountingTime",
        "schema:name": "Peak Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:analyteColumn/semTAPP/backgroundCountingTime",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCountingTime",
        "schema:name": "Background Counting Time",
        "ada:dataType": "number",
        "schema:defaultValue": 1
      },
      {
        "@id": "ada:analyteColumn/semTAPP/backgroundPosition",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundPosition",
        "schema:name": "Background Position(s)",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/backgroundCorrectionMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "backgroundCorrectionMethod",
        "schema:name": "Background Correction Method",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/timeDependentIntensityCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "timeDependentIntensityCorrection",
        "schema:name": "Time-Dependent Intensity Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/analyteEstimationMethod",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyteEstimationMethod",
        "schema:name": "Analyte Estimation Method",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/blankCorrection",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "blankCorrection",
        "schema:name": "Blank Correction",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/primaryCalibrationStandardName",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "primaryCalibrationStandardName",
        "schema:name": "Primary Calibration Standard Name",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/secondaryReferenceMaterials",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "secondaryReferenceMaterials",
        "schema:name": "Secondary Reference Materials",
        "ada:dataType": "string",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/interferenceCorrectionsApplied",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionsApplied",
        "schema:name": "Interference Corrections Applied",
        "ada:dataType": "boolean",
        "schema:defaultValue": "example value"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/interferingElements",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferingElements",
        "schema:name": "Interfering Elements",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/interferenceCorrectionStandard",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "interferenceCorrectionStandard",
        "schema:name": "Interference Correction Standard",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/analyticalPrecision",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalPrecision",
        "schema:name": "Analytical Precision",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/analyticalAccuracy",
        "@type": [
          "schema:PropertyValueSpecification"
        ],
        "schema:valueName": "analyticalAccuracy",
        "schema:name": "Analytical Accuracy",
        "ada:dataType": "string"
      },
      {
        "@id": "ada:analyteColumn/semTAPP/countingStatisticsError",
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
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/semTAPP/edsSpectralProcessingType",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/semTAPP/edsSpectralProcessingType"
        }
      ],
      "schema:name": "EDS Spectral Processing Type",
      "schema:value": "Semi-quantitative analysis with virtual standards (Oxford INCA Energy); mineral phase determination from atomic % of constituent elements"
    }
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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

ex:semTAPP-Pascucci2026-3 a cdi:Activity,
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
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semTAPP/edsSpectralProcessingType> ;
    schema1:datePublished "missing" ;
    schema1:description "EDS mapping: 20 kV, 60 µm aperture, 5 ms dwell per pixel, 1024×768 pixels, 2.5 µm pixel size, ~10 h total; element maps co-registered with BSE images Reported detail: ada:edsAcquisitionMode = Element mapping." ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "SEM" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "WDSSpectrometer" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Electron source" ;
                    schema1:description "Unknown" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "EDSDetector" ;
                    schema1:description "Oxford INCA Energy 350; X-ACT LN2-free Silicon Drift Detector (SDD)" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "xrayLine" ;
                    schema1:name "missing" ] ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "Zeiss" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "Supra 40" ] ;
            schema1:name "example instrumentName" ;
            ada:acceleratingVoltageDefault "20 kV" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "CNR IMAA (Institute of Methodologies for Environmental Analysis), Italian National Research Council, Potenza, Italy" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "sem" ;
            schema1:termCode "SEM" ] ;
    schema1:name "sem protocol — Pascucci2026-3" ;
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
                <https://ada.astromat.org/metadata/analyteColumn/semTAPP/analyteEstimationMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/semTAPP/analyticalAccuracy>,
                <https://ada.astromat.org/metadata/analyteColumn/semTAPP/analyticalPrecision>,
                <https://ada.astromat.org/metadata/analyteColumn/semTAPP/backgroundCorrectionMethod>,
                <https://ada.astromat.org/metadata/analyteColumn/semTAPP/backgroundCountingTime>,
                <https://ada.astromat.org/metadata/analyteColumn/semTAPP/backgroundPosition>,
                <https://ada.astromat.org/metadata/analyteColumn/semTAPP/beamCurrent>,
                <https://ada.astromat.org/metadata/analyteColumn/semTAPP/blankCorrection>,
                <https://ada.astromat.org/metadata/analyteColumn/semTAPP/countingStatisticsError>,
                <https://ada.astromat.org/metadata/analyteColumn/semTAPP/diffractingCrystal>,
                <https://ada.astromat.org/metadata/analyteColumn/semTAPP/interferenceCorrectionStandard>,
                <https://ada.astromat.org/metadata/analyteColumn/semTAPP/interferenceCorrectionsApplied>,
                <https://ada.astromat.org/metadata/analyteColumn/semTAPP/interferingElements>,
                <https://ada.astromat.org/metadata/analyteColumn/semTAPP/peakCountingTime>,
                <https://ada.astromat.org/metadata/analyteColumn/semTAPP/primaryCalibrationStandardName>,
                <https://ada.astromat.org/metadata/analyteColumn/semTAPP/proportionalCounterDetector>,
                <https://ada.astromat.org/metadata/analyteColumn/semTAPP/secondaryReferenceMaterials>,
                <https://ada.astromat.org/metadata/analyteColumn/semTAPP/techniquePerAnalyte>,
                <https://ada.astromat.org/metadata/analyteColumn/semTAPP/timeDependentIntensityCorrection>,
                <https://ada.astromat.org/metadata/analyteColumn/semTAPP/wdsPhaSetting>,
                <https://ada.astromat.org/metadata/analyteColumn/semTAPP/wdsSpectrometerChannel> ;
            ada:defaultAnalytes "Al (element mapping)",
                "Ca",
                "Fe",
                "Mg",
                "Na",
                "Ni",
                "S",
                "Si" ] ;
    ada:analyticalMode "N/A" ;
    ada:dwellTimePerPixelDefault -9999 ;
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

<https://ada.astromat.org/metadata/analyteColumn/semTAPP/analyteEstimationMethod> a schema1:PropertyValueSpecification ;
    schema1:name "Analyte Estimation Method" ;
    schema1:valueName "analyteEstimationMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semTAPP/analyticalAccuracy> a schema1:PropertyValueSpecification ;
    schema1:name "Analytical Accuracy" ;
    schema1:valueName "analyticalAccuracy" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semTAPP/analyticalPrecision> a schema1:PropertyValueSpecification ;
    schema1:name "Analytical Precision" ;
    schema1:valueName "analyticalPrecision" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semTAPP/backgroundCorrectionMethod> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Background Correction Method" ;
    schema1:valueName "backgroundCorrectionMethod" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semTAPP/backgroundCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Background Counting Time" ;
    schema1:valueName "backgroundCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/semTAPP/backgroundPosition> a schema1:PropertyValueSpecification ;
    schema1:name "Background Position(s)" ;
    schema1:valueName "backgroundPosition" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semTAPP/beamCurrent> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Beam Current" ;
    schema1:valueName "beamCurrent" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/semTAPP/blankCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Blank Correction" ;
    schema1:valueName "blankCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semTAPP/countingStatisticsError> a schema1:PropertyValueSpecification ;
    schema1:name "Counting Statistics Error" ;
    schema1:valueName "countingStatisticsError" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semTAPP/diffractingCrystal> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Diffracting Crystal" ;
    schema1:valueName "diffractingCrystal" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semTAPP/interferenceCorrectionStandard> a schema1:PropertyValueSpecification ;
    schema1:name "Interference Correction Standard" ;
    schema1:valueName "interferenceCorrectionStandard" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semTAPP/interferenceCorrectionsApplied> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Interference Corrections Applied" ;
    schema1:valueName "interferenceCorrectionsApplied" ;
    ada:dataType "boolean" .

<https://ada.astromat.org/metadata/analyteColumn/semTAPP/interferingElements> a schema1:PropertyValueSpecification ;
    schema1:name "Interfering Elements" ;
    schema1:valueName "interferingElements" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semTAPP/peakCountingTime> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 1 ;
    schema1:name "Peak Counting Time" ;
    schema1:valueName "peakCountingTime" ;
    ada:dataType "number" .

<https://ada.astromat.org/metadata/analyteColumn/semTAPP/primaryCalibrationStandardName> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Primary Calibration Standard Name" ;
    schema1:valueName "primaryCalibrationStandardName" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semTAPP/proportionalCounterDetector> a schema1:PropertyValueSpecification ;
    schema1:name "Proportional Counter / Detector" ;
    schema1:valueName "proportionalCounterDetector" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semTAPP/secondaryReferenceMaterials> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Secondary Reference Materials" ;
    schema1:valueName "secondaryReferenceMaterials" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semTAPP/techniquePerAnalyte> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "example value" ;
    schema1:name "Technique per Analyte" ;
    schema1:valueName "techniquePerAnalyte" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semTAPP/timeDependentIntensityCorrection> a schema1:PropertyValueSpecification ;
    schema1:name "Time-Dependent Intensity Correction" ;
    schema1:valueName "timeDependentIntensityCorrection" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semTAPP/wdsPhaSetting> a schema1:PropertyValueSpecification ;
    schema1:name "WDS PHA Setting" ;
    schema1:valueName "wdsPhaSetting" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/analyteColumn/semTAPP/wdsSpectrometerChannel> a schema1:PropertyValueSpecification ;
    schema1:name "WDS Spectrometer Channel" ;
    schema1:valueName "wdsSpectrometerChannel" ;
    ada:dataType "string" .

<https://ada.astromat.org/metadata/parameter/semTAPP/edsSpectralProcessingType> a schema1:PropertyValue ;
    schema1:name "EDS Spectral Processing Type" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semTAPP/edsSpectralProcessingType> ;
    schema1:value "Semi-quantitative analysis with virtual standards (Oxford INCA Energy); mineral phase determination from atomic % of constituent elements" .


```


### semTAPP example Pascucci2026-4
semTAPP instance derived from Pascucci et al. 2026 | NWA 7317 CR6 chondrite | SE Imaging (Zeiss Supra 40 FE-SEM).
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
  "@id": "ex:semTAPP-Pascucci2026-4",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol — Pascucci2026-4",
  "schema:description": "SE imaging used for topographic examination; instrument capability: up to ×200,000 magnification, 5 nm resolution; SE acquired before EDS to minimize charging effects",
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
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
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
            "EDSDetector",
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
            "WDSSpectrometer",
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
            "xrayLine",
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
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-Pascucci2026-4",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol \u2014 Pascucci2026-4",
  "schema:description": "SE imaging used for topographic examination; instrument capability: up to \u00d7200,000 magnification, 5 nm resolution; SE acquired before EDS to minimize charging effects",
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
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
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
            "EDSDetector",
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
            "WDSSpectrometer",
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
            "xrayLine",
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
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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

ex:semTAPP-Pascucci2026-4 a cdi:Activity,
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
    schema1:datePublished "missing" ;
    schema1:description "SE imaging used for topographic examination; instrument capability: up to ×200,000 magnification, 5 nm resolution; SE acquired before EDS to minimize charging effects" ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "SEM" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "EDSDetector" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "WDSSpectrometer" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Electron source" ;
                    schema1:description "Unknown" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "xrayLine" ;
                    schema1:name "missing" ] ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "Zeiss" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "Supra 40" ] ;
            schema1:name "example instrumentName" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "CNR IMAA (Institute of Methodologies for Environmental Analysis), Italian National Research Council, Potenza, Italy" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "sem" ;
            schema1:termCode "SEM" ] ;
    schema1:name "sem protocol — Pascucci2026-4" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "NWA 7317 CR6 carbonaceous chondrite; polished slab (~10×6 mm fragment, 10.01g)" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "BSE Imaging (Zeiss Supra 40 FE-SEM); EDS (Zeiss Supra 40 FE-SEM); EMPA-WDS (JEOL JXA-8230, separate instrument); VIS-IR spectroscopy (SPIM)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:samplingUnit "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:wdsDeadTimeCorrection "missing" .


```


### semTAPP example Zhou2017
semTAPP instance derived from Zhou et al. 2017 | Coal (SC + HBC, Junggar Basin) | 3D Tomography (FEI Helios NanoLab 650).
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
  "@id": "ex:semTAPP-Zhou2017",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol — Zhou2017",
  "schema:description": "Stage tilt 52° between electron and ion columns; SEM range 20V–30kV and FIB range 500V–30kV (system specs); destriping filter xStripes.jar applied; deconvolves y-axis by y/sin(52°) for pixel scale correction",
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "China University of Geosciences, Beijing, China"
  },
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
            "Subbituminous coal (SC) and high-volatile bituminous coal (HBC), Xishanyao Formation, southern Junggar Basin, NW China"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Cuboidal samples (~0.5×1×1 cm) polished with dry emery paper and argon ion polishing; high-pressure freezing and freeze-drying; glued onto sample holder",
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
        "schema:name": "Helios NanoLab 650",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:acceleratingVoltageDefault": "2 kV (SEM imaging)",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDSDetector",
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
            "Electron source",
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
            "WDSSpectrometer",
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
            "xrayLine",
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
      "schema:name": "Fiji/ImageJ (StackReg/TurboReg for slice alignment; VolumeJ for volume rendering); Adobe Photoshop CS6 (image enhancement); FEI Avizo Fire 8.1.1 (pore volume reconstruction and segmentation)"
    }
  ],
  "ada:analyticalMode": [
    "N/A"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-Zhou2017",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol \u2014 Zhou2017",
  "schema:description": "Stage tilt 52\u00b0 between electron and ion columns; SEM range 20V\u201330kV and FIB range 500V\u201330kV (system specs); destriping filter xStripes.jar applied; deconvolves y-axis by y/sin(52\u00b0) for pixel scale correction",
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "China University of Geosciences, Beijing, China"
  },
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
            "Subbituminous coal (SC) and high-volatile bituminous coal (HBC), Xishanyao Formation, southern Junggar Basin, NW China"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Cuboidal samples (~0.5\u00d71\u00d71 cm) polished with dry emery paper and argon ion polishing; high-pressure freezing and freeze-drying; glued onto sample holder",
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
        "schema:name": "Helios NanoLab 650",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "ada:acceleratingVoltageDefault": "2 kV (SEM imaging)",
      "schema:hasPart": [
        {
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:additionalType": [
            "EDSDetector",
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
            "Electron source",
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
            "WDSSpectrometer",
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
            "xrayLine",
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
      "schema:name": "Fiji/ImageJ (StackReg/TurboReg for slice alignment; VolumeJ for volume rendering); Adobe Photoshop CS6 (image enhancement); FEI Avizo Fire 8.1.1 (pore volume reconstruction and segmentation)"
    }
  ],
  "ada:analyticalMode": [
    "N/A"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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

ex:semTAPP-Zhou2017 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Cuboidal samples (~0.5×1×1 cm) polished with dry emery paper and argon ion polishing; high-pressure freezing and freeze-drying; glued onto sample holder" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "Stage tilt 52° between electron and ion columns; SEM range 20V–30kV and FIB range 500V–30kV (system specs); destriping filter xStripes.jar applied; deconvolves y-axis by y/sin(52°) for pixel scale correction" ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "SEM" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "WDSSpectrometer" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Electron source" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "xrayLine" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "EDSDetector" ;
                    schema1:name "missing" ] ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "Unknown" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "Helios NanoLab 650" ] ;
            schema1:name "example instrumentName" ;
            ada:acceleratingVoltageDefault "2 kV (SEM imaging)" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "China University of Geosciences, Beijing, China" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "sem" ;
            schema1:termCode "SEM" ] ;
    schema1:name "sem protocol — Zhou2017" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Subbituminous coal (SC) and high-volatile bituminous coal (HBC), Xishanyao Formation, southern Junggar Basin, NW China" ] ] ;
    ada:analyticalMode "N/A" ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:samplingUnit "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:wdsDeadTimeCorrection "missing" ;
    bios:computationalTool [ schema1:name "Fiji/ImageJ (StackReg/TurboReg for slice alignment; VolumeJ for volume rendering); Adobe Photoshop CS6 (image enhancement); FEI Avizo Fire 8.1.1 (pore volume reconstruction and segmentation)" ;
            ada:toolRole "dataReduction" ] .


```


### semTAPP example Zega2025
semTAPP instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | BSE Imaging (JEOL 7600F, NASA JSC, 15 kV).
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
  "@id": "ex:semTAPP-Zega2025",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol — Zega2025",
  "schema:description": "SE and BSE imaging; EDS point spectra; Oxford AZtec system; EDS detector: Oxford Instruments Ultim Max SDD 170 mm²",
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
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
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
            "EDSDetector",
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
            "WDSSpectrometer",
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
            "xrayLine",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
    }
  ],
  "bios:computationalTool": [
    {
      "ada:toolRole": "acquisition",
      "schema:name": "Oxford AZtec (Point & ID programme)"
    }
  ],
  "ada:analyticalMode": [
    "N/A"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-Zega2025",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol \u2014 Zega2025",
  "schema:description": "SE and BSE imaging; EDS point spectra; Oxford AZtec system; EDS detector: Oxford Instruments Ultim Max SDD 170 mm\u00b2",
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
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
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
            "EDSDetector",
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
            "WDSSpectrometer",
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
            "xrayLine",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
    }
  ],
  "bios:computationalTool": [
    {
      "ada:toolRole": "acquisition",
      "schema:name": "Oxford AZtec (Point & ID programme)"
    }
  ],
  "ada:analyticalMode": [
    "N/A"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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

ex:semTAPP-Zega2025 a cdi:Activity,
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
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "SEM" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "xrayLine" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "EDSDetector" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "WDSSpectrometer" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Electron source" ;
                    schema1:description "Unknown" ;
                    schema1:name "missing" ] ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "JEOL" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "7600F" ] ;
            schema1:name "example instrumentName" ;
            ada:acceleratingVoltageDefault "15 kV" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "NASA Johnson Space Center (JSC), Houston, TX, USA" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "sem" ;
            schema1:termCode "SEM" ] ;
    schema1:name "sem protocol — Zega2025" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Asteroid (101955) Bennu particles (OSIRIS-REx sample return); hummocky and angular particles" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "EDS (JEOL 7600F, JSC); SE Imaging (JEOL 7600F, JSC); FIB-SEM TEM prep (Quanta3D600, JSC)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "N/A" ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:samplingUnit "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:wdsDeadTimeCorrection "missing" ;
    bios:computationalTool [ schema1:name "Oxford AZtec (Point & ID programme)" ;
            ada:toolRole "acquisition" ] .


```


### semTAPP example Zega2025-2
semTAPP instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | EDS Point Analysis (JEOL 7600F, NASA JSC, 15 kV).
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
  "@id": "ex:semTAPP-Zega2025-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol — Zega2025-2",
  "schema:description": "semTAPP instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | EDS Point Analysis (JEOL 7600F, NASA JSC, 15 kV) (publication column of SEM_TAPP_v17.xlsx).",
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
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "EDSDetector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Oxford Instruments Ultim Max SDD, 170 mm²",
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
            "WDSSpectrometer",
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
            "xrayLine",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
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
    "N/A"
  ],
  "ada:edsAcquisitionMode": "N/A",
  "ada:edsLiveTimePerPointOrPixelDefault": "20 to 200 s (per point)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-Zega2025-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol \u2014 Zega2025-2",
  "schema:description": "semTAPP instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | EDS Point Analysis (JEOL 7600F, NASA JSC, 15 kV) (publication column of SEM_TAPP_v17.xlsx).",
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
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "EDSDetector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Oxford Instruments Ultim Max SDD, 170 mm\u00b2",
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
            "WDSSpectrometer",
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
            "xrayLine",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing"
        }
      ],
      "ada:acceleratingVoltageDefault": "15 kV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
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
    "N/A"
  ],
  "ada:edsAcquisitionMode": "N/A",
  "ada:edsLiveTimePerPointOrPixelDefault": "20 to 200 s (per point)",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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

ex:semTAPP-Zega2025-2 a cdi:Activity,
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
    schema1:description "semTAPP instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | EDS Point Analysis (JEOL 7600F, NASA JSC, 15 kV) (publication column of SEM_TAPP_v17.xlsx)." ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "SEM" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "WDSSpectrometer" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "EDSDetector" ;
                    schema1:description "Oxford Instruments Ultim Max SDD, 170 mm²" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Electron source" ;
                    schema1:description "Unknown" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "xrayLine" ;
                    schema1:name "missing" ] ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "JEOL" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "7600F" ] ;
            schema1:name "example instrumentName" ;
            ada:acceleratingVoltageDefault "15 kV" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "NASA Johnson Space Center (JSC), Houston, TX, USA" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "sem" ;
            schema1:termCode "SEM" ] ;
    schema1:name "sem protocol — Zega2025-2" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Asteroid (101955) Bennu particles (OSIRIS-REx sample return)" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "BSE Imaging (JEOL 7600F, JSC); SE Imaging (JEOL 7600F, JSC); FIB-SEM TEM prep (Quanta3D600, JSC)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "N/A" ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:edsAcquisitionMode "N/A" ;
    ada:edsLiveTimePerPointOrPixelDefault "20 to 200 s (per point)" ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:samplingUnit "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:wdsDeadTimeCorrection "missing" ;
    bios:computationalTool [ schema1:name "Oxford AZtec (Point & ID programme)" ;
            ada:toolRole "acquisition" ],
        [ schema1:name "Oxford AZtec" ;
            ada:toolRole "dataReduction" ] .


```


### semTAPP example Zega2025-3
semTAPP instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | SE Imaging (Hitachi S-4800, U Arizona).
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
  "@id": "ex:semTAPP-Zega2025-3",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol — Zega2025-3",
  "schema:description": "Cold FEG; system range 0.5-30 keV; SE and BSE imaging detectors; also equipped with Oxford Instruments Aztec Live/x-stream/Ultimax 170 SDD EDS; specific operating voltage not stated",
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
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
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
            "EDSDetector",
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
            "WDSSpectrometer",
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
            "xrayLine",
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
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-Zega2025-3",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol \u2014 Zega2025-3",
  "schema:description": "Cold FEG; system range 0.5-30 keV; SE and BSE imaging detectors; also equipped with Oxford Instruments Aztec Live/x-stream/Ultimax 170 SDD EDS; specific operating voltage not stated",
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
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
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
            "EDSDetector",
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
            "WDSSpectrometer",
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
            "xrayLine",
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
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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

ex:semTAPP-Zega2025-3 a cdi:Activity,
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
    schema1:description "Cold FEG; system range 0.5-30 keV; SE and BSE imaging detectors; also equipped with Oxford Instruments Aztec Live/x-stream/Ultimax 170 SDD EDS; specific operating voltage not stated" ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "SEM" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "WDSSpectrometer" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Electron source" ;
                    schema1:description "Unknown" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "xrayLine" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "EDSDetector" ;
                    schema1:name "missing" ] ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "Hitachi" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "S-4800" ] ;
            schema1:name "example instrumentName" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "K-ALFAA (Kuiper-Arizona Laboratory for Astromaterials Analysis), University of Arizona" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "sem" ;
            schema1:termCode "SEM" ] ;
    schema1:name "sem protocol — Zega2025-3" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Asteroid (101955) Bennu particles (OSIRIS-REx sample return); polished sections" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "BSE Imaging (Hitachi S-4800, U Arizona); EDS (Hitachi S-4800, U Arizona); FIB-SEM TEM prep (Helios G3, U Arizona); EMPA (Cameca SX-100 Ultra, out of scope)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:samplingUnit "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:wdsDeadTimeCorrection "missing" .


```


### semTAPP example Zega2025-4
semTAPP instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | BSE Imaging (Hitachi S-4800, U Arizona).
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
  "@id": "ex:semTAPP-Zega2025-4",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol — Zega2025-4",
  "schema:description": "Cold FEG; system range 0.5-30 keV; SE and BSE imaging; EDS mapping; specific operating voltage not stated",
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
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
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
            "EDSDetector",
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
            "WDSSpectrometer",
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
            "xrayLine",
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
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-Zega2025-4",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol \u2014 Zega2025-4",
  "schema:description": "Cold FEG; system range 0.5-30 keV; SE and BSE imaging; EDS mapping; specific operating voltage not stated",
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
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
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
            "EDSDetector",
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
            "WDSSpectrometer",
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
            "xrayLine",
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
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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

ex:semTAPP-Zega2025-4 a cdi:Activity,
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
    schema1:description "Cold FEG; system range 0.5-30 keV; SE and BSE imaging; EDS mapping; specific operating voltage not stated" ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "SEM" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "EDSDetector" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "xrayLine" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "WDSSpectrometer" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Electron source" ;
                    schema1:description "Unknown" ;
                    schema1:name "missing" ] ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "Hitachi" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "S-4800" ] ;
            schema1:name "example instrumentName" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "K-ALFAA (Kuiper-Arizona Laboratory for Astromaterials Analysis), University of Arizona" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "sem" ;
            schema1:termCode "SEM" ] ;
    schema1:name "sem protocol — Zega2025-4" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Asteroid (101955) Bennu particles (OSIRIS-REx sample return); polished sections" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SE Imaging (Hitachi S-4800, U Arizona); EDS (Hitachi S-4800, U Arizona); FIB-SEM TEM prep (Helios G3, U Arizona); EMPA (Cameca SX-100 Ultra, out of scope)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:samplingUnit "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:wdsDeadTimeCorrection "missing" .


```


### semTAPP example Zega2025-5
semTAPP instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | EDS Mapping (Hitachi S-4800, U Arizona).
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
  "@id": "ex:semTAPP-Zega2025-5",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol — Zega2025-5",
  "schema:description": "Compositional heterogeneity assessed through EDS mapping; no specific kV, current, dwell time stated for S-4800 EDS Reported detail: ada:analyticalMode = EDS mapping; ada:edsAcquisitionMode = EDS mapping.",
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
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "EDSDetector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Oxford Instruments Aztec Live/x-stream/Ultimax 170 SDD",
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
            "WDSSpectrometer",
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
            "xrayLine",
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
      "ada:toolRole": "acquisition",
      "schema:name": "Oxford Instruments Aztec Live/x-stream"
    },
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Oxford Instruments Aztec"
    }
  ],
  "ada:analyticalMode": [
    "EDS"
  ],
  "ada:edsAcquisitionMode": "Map",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-Zega2025-5",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol \u2014 Zega2025-5",
  "schema:description": "Compositional heterogeneity assessed through EDS mapping; no specific kV, current, dwell time stated for S-4800 EDS Reported detail: ada:analyticalMode = EDS mapping; ada:edsAcquisitionMode = EDS mapping.",
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
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "missing"
        },
        {
          "schema:additionalType": [
            "EDSDetector",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Oxford Instruments Aztec Live/x-stream/Ultimax 170 SDD",
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
            "WDSSpectrometer",
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
            "xrayLine",
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
      "ada:toolRole": "acquisition",
      "schema:name": "Oxford Instruments Aztec Live/x-stream"
    },
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Oxford Instruments Aztec"
    }
  ],
  "ada:analyticalMode": [
    "EDS"
  ],
  "ada:edsAcquisitionMode": "Map",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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

ex:semTAPP-Zega2025-5 a cdi:Activity,
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
    schema1:description "Compositional heterogeneity assessed through EDS mapping; no specific kV, current, dwell time stated for S-4800 EDS Reported detail: ada:analyticalMode = EDS mapping; ada:edsAcquisitionMode = EDS mapping." ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "SEM" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "xrayLine" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "WDSSpectrometer" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "EDSDetector" ;
                    schema1:description "Oxford Instruments Aztec Live/x-stream/Ultimax 170 SDD" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Electron source" ;
                    schema1:description "Unknown" ;
                    schema1:name "missing" ] ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "Hitachi" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "S-4800" ] ;
            schema1:name "example instrumentName" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "K-ALFAA (Kuiper-Arizona Laboratory for Astromaterials Analysis), University of Arizona" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "sem" ;
            schema1:termCode "SEM" ] ;
    schema1:name "sem protocol — Zega2025-5" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Asteroid (101955) Bennu particles (OSIRIS-REx sample return); polished sections" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "SE/BSE Imaging (Hitachi S-4800, U Arizona); FIB-SEM TEM prep (Helios G3, U Arizona); EMPA (Cameca SX-100 Ultra, out of scope)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "EDS" ;
    ada:dwellTimePerPixelDefault -9999 ;
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


```


### semTAPP example Zega2025-6
semTAPP instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | TEM Sample Preparation (Helios G3, U Arizona).
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
  "@id": "ex:semTAPP-Zega2025-6",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol — Zega2025-6",
  "schema:description": "Sections thinned to electron transparency; BSE/SE images acquired before and after sectioning; methods follow refs. 72-75",
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
        "schema:name": "TEM analysis (HF5000 STEM, U Arizona); BSE/SE Imaging (Hitachi S-4800, U Arizona)"
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
            "Asteroid (101955) Bennu particles (OSIRIS-REx sample return); fine-grained matrix areas"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Sections extracted from fine-grained matrix areas in polished sections; BSE and SE images acquired before and after sectioning",
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
        "schema:name": "Helios G3",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
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
            "EDSDetector",
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
            "WDSSpectrometer",
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
            "xrayLine",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing"
        }
      ],
      "ada:acceleratingVoltageDefault": "30 keV (FIB milling and thinning)",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
    }
  ],
  "ada:analyticalMode": [
    "N/A"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-Zega2025-6",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol \u2014 Zega2025-6",
  "schema:description": "Sections thinned to electron transparency; BSE/SE images acquired before and after sectioning; methods follow refs. 72-75",
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
        "schema:name": "TEM analysis (HF5000 STEM, U Arizona); BSE/SE Imaging (Hitachi S-4800, U Arizona)"
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
            "Asteroid (101955) Bennu particles (OSIRIS-REx sample return); fine-grained matrix areas"
          ]
        }
      ]
    }
  ],
  "schema:actionProcess": {
    "schema:step": [
      {
        "schema:name": "Sample preparation",
        "schema:description": "Sections extracted from fine-grained matrix areas in polished sections; BSE and SE images acquired before and after sectioning",
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
        "schema:name": "Helios G3",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
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
            "EDSDetector",
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
            "WDSSpectrometer",
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
            "xrayLine",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing"
        }
      ],
      "ada:acceleratingVoltageDefault": "30 keV (FIB milling and thinning)",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
    }
  ],
  "ada:analyticalMode": [
    "N/A"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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

ex:semTAPP-Zega2025-6 a cdi:Activity,
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
                    schema1:description "Sections extracted from fine-grained matrix areas in polished sections; BSE and SE images acquired before and after sectioning" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "Sections thinned to electron transparency; BSE/SE images acquired before and after sectioning; methods follow refs. 72-75" ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "SEM" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "xrayLine" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "WDSSpectrometer" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "EDSDetector" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Electron source" ;
                    schema1:description "Unknown" ;
                    schema1:name "missing" ] ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "Unknown" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "Helios G3" ] ;
            schema1:name "example instrumentName" ;
            ada:acceleratingVoltageDefault "30 keV (FIB milling and thinning)" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "K-ALFAA (Kuiper-Arizona Laboratory for Astromaterials Analysis), University of Arizona" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "sem" ;
            schema1:termCode "SEM" ] ;
    schema1:name "sem protocol — Zega2025-6" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Asteroid (101955) Bennu particles (OSIRIS-REx sample return); fine-grained matrix areas" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "TEM analysis (HF5000 STEM, U Arizona); BSE/SE Imaging (Hitachi S-4800, U Arizona)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "N/A" ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:samplingUnit "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:wdsDeadTimeCorrection "missing" .


```


### semTAPP example Zega2025-7
semTAPP instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | TEM Sample Preparation (Helios G4 UX, UC Berkeley).
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
  "@id": "ex:semTAPP-Zega2025-7",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol — Zega2025-7",
  "schema:description": "Thicker sections (<100 nm) for TEM; sections up to 600 nm for Fe-L XANES and tomography",
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Molecular Foundry, Lawrence Berkeley National Laboratory (UC Berkeley)"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Synchrotron XANES (ALS, Berkeley); TEM analysis"
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
        "schema:description": "Particles placed on PELCO carbon conductive tabs on Al SEM round; no protective coating stated",
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
        "schema:name": "Helios G4 UX",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
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
            "EDSDetector",
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
            "WDSSpectrometer",
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
            "xrayLine",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing"
        }
      ],
      "ada:acceleratingVoltageDefault": "16 to 30 keV (coarse milling); down to 1 keV (polishing)",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
    }
  ],
  "ada:analyticalMode": [
    "N/A"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-Zega2025-7",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol \u2014 Zega2025-7",
  "schema:description": "Thicker sections (<100 nm) for TEM; sections up to 600 nm for Fe-L XANES and tomography",
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "Molecular Foundry, Lawrence Berkeley National Laboratory (UC Berkeley)"
  },
  "schema:relatedLink": [
    {
      "schema:linkRelationship": "coupledTechnique",
      "schema:target": {
        "schema:name": "Synchrotron XANES (ALS, Berkeley); TEM analysis"
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
        "schema:description": "Particles placed on PELCO carbon conductive tabs on Al SEM round; no protective coating stated",
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
        "schema:name": "Helios G4 UX",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
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
            "EDSDetector",
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
            "WDSSpectrometer",
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
            "xrayLine",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing"
        }
      ],
      "ada:acceleratingVoltageDefault": "16 to 30 keV (coarse milling); down to 1 keV (polishing)",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
    }
  ],
  "ada:analyticalMode": [
    "N/A"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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

ex:semTAPP-Zega2025-7 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Particles placed on PELCO carbon conductive tabs on Al SEM round; no protective coating stated" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "Thicker sections (<100 nm) for TEM; sections up to 600 nm for Fe-L XANES and tomography" ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "SEM" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Electron source" ;
                    schema1:description "Unknown" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "xrayLine" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "EDSDetector" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "WDSSpectrometer" ;
                    schema1:name "missing" ] ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "Unknown" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "Helios G4 UX" ] ;
            schema1:name "example instrumentName" ;
            ada:acceleratingVoltageDefault "16 to 30 keV (coarse milling); down to 1 keV (polishing)" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "Molecular Foundry, Lawrence Berkeley National Laboratory (UC Berkeley)" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "sem" ;
            schema1:termCode "SEM" ] ;
    schema1:name "sem protocol — Zega2025-7" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Asteroid (101955) Bennu particles (OSIRIS-REx sample return)" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "Synchrotron XANES (ALS, Berkeley); TEM analysis" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "N/A" ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:samplingUnit "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:wdsDeadTimeCorrection "missing" .


```


### semTAPP example Zega2025-8
semTAPP instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | TEM Sample Preparation (Quanta3D600, NASA JSC).
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
  "@id": "ex:semTAPP-Zega2025-8",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol — Zega2025-8",
  "schema:description": "Multi-step milling: e-beam C deposition then FIB C capping, 30 kV → 16 kV → 5 kV; Pt weld to Cu half grids",
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
        "schema:name": "TEM analysis (NASA JSC); BSE/SE Imaging (JEOL 7600F, JSC)"
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
        "schema:description": "Particles dispersed on conductive carbon dots on Al SEM pin mounts",
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
        "schema:name": "Quanta 3D 600",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
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
            "EDSDetector",
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
            "WDSSpectrometer",
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
            "xrayLine",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing"
        }
      ],
      "ada:acceleratingVoltageDefault": "30 kV (initial milling); 16 kV (intermediate); 5 kV (final thinning)",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
    }
  ],
  "ada:analyticalMode": [
    "N/A"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-Zega2025-8",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol \u2014 Zega2025-8",
  "schema:description": "Multi-step milling: e-beam C deposition then FIB C capping, 30 kV \u2192 16 kV \u2192 5 kV; Pt weld to Cu half grids",
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
        "schema:name": "TEM analysis (NASA JSC); BSE/SE Imaging (JEOL 7600F, JSC)"
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
        "schema:description": "Particles dispersed on conductive carbon dots on Al SEM pin mounts",
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
        "schema:name": "Quanta 3D 600",
        "@type": [
          "schema:ProductModel"
        ]
      },
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
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
            "EDSDetector",
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
            "WDSSpectrometer",
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
            "xrayLine",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing"
        }
      ],
      "ada:acceleratingVoltageDefault": "30 kV (initial milling); 16 kV (intermediate); 5 kV (final thinning)",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
    }
  ],
  "ada:analyticalMode": [
    "N/A"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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

ex:semTAPP-Zega2025-8 a cdi:Activity,
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
                    schema1:description "Particles dispersed on conductive carbon dots on Al SEM pin mounts" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "Multi-step milling: e-beam C deposition then FIB C capping, 30 kV → 16 kV → 5 kV; Pt weld to Cu half grids" ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "SEM" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "xrayLine" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "WDSSpectrometer" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "EDSDetector" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Electron source" ;
                    schema1:description "Unknown" ;
                    schema1:name "missing" ] ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "Unknown" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "Quanta 3D 600" ] ;
            schema1:name "example instrumentName" ;
            ada:acceleratingVoltageDefault "30 kV (initial milling); 16 kV (intermediate); 5 kV (final thinning)" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "NASA Johnson Space Center (JSC), Houston, TX, USA" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "sem" ;
            schema1:termCode "SEM" ] ;
    schema1:name "sem protocol — Zega2025-8" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Asteroid (101955) Bennu particles (OSIRIS-REx sample return)" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "TEM analysis (NASA JSC); BSE/SE Imaging (JEOL 7600F, JSC)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "N/A" ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:samplingUnit "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:wdsDeadTimeCorrection "missing" .


```


### semTAPP example Zega2025-9
semTAPP instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | CL Mapping (JEOL JSM-7000F, Universite Cote d'Azur, 5 keV).
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
  "@id": "ex:semTAPP-Zega2025-9",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol — Zega2025-9",
  "schema:description": "CL emitting volume at 5 keV: up to 230 nm depth, 200 nm sideways (assuming 100-nm graphite coating); recording below focal plane for magnifications <×500 to minimize hotspot effect Reported detail: ada:analyticalMode = Panchromatic CL imaging; hyperspectral CL; monochromatic CL imaging.",
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
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
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
            "EDSDetector",
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
            "WDSSpectrometer",
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
            "xrayLine",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing"
        }
      ],
      "ada:acceleratingVoltageDefault": "5 keV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
    }
  ],
  "ada:analyticalMode": [
    "CL"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-Zega2025-9",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol \u2014 Zega2025-9",
  "schema:description": "CL emitting volume at 5 keV: up to 230 nm depth, 200 nm sideways (assuming 100-nm graphite coating); recording below focal plane for magnifications <\u00d7500 to minimize hotspot effect Reported detail: ada:analyticalMode = Panchromatic CL imaging; hyperspectral CL; monochromatic CL imaging.",
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
            "Electron source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:description": "Unknown",
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
            "EDSDetector",
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
            "WDSSpectrometer",
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
            "xrayLine",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing"
        }
      ],
      "ada:acceleratingVoltageDefault": "5 keV",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:name": "example instrumentName"
    }
  ],
  "ada:analyticalMode": [
    "CL"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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

ex:semTAPP-Zega2025-9 a cdi:Activity,
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
                    schema1:description "Polished thin sections; ~100 nm graphite coating (as stated in CL emitting volume calculation)" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "CL emitting volume at 5 keV: up to 230 nm depth, 200 nm sideways (assuming 100-nm graphite coating); recording below focal plane for magnifications <×500 to minimize hotspot effect Reported detail: ada:analyticalMode = Panchromatic CL imaging; hyperspectral CL; monochromatic CL imaging." ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "SEM" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "xrayLine" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "EDSDetector" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "WDSSpectrometer" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Electron source" ;
                    schema1:description "Unknown" ;
                    schema1:name "missing" ] ;
            schema1:manufacturer [ a schema1:Organization ;
                    schema1:name "JEOL" ] ;
            schema1:model [ a schema1:ProductModel ;
                    schema1:name "JSM-7000F" ] ;
            schema1:name "example instrumentName" ;
            ada:acceleratingVoltageDefault "5 keV" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "Université Côte d'Azur / Observatoire de la Côte d'Azur, Valbonne, France" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "sem" ;
            schema1:termCode "SEM" ] ;
    schema1:name "sem protocol — Zega2025-9" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Asteroid (101955) Bennu particles (OSIRIS-REx sample return); olivine and carbonate grains" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "BSE/EDS (JEOL 7600F, JSC); SE/BSE/EDS (Hitachi S-4800, U Arizona)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "CL" ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:samplingUnit "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:wdsDeadTimeCorrection "missing" .


```


### semTAPP example Barnes2025
semTAPP instance derived from Barnes et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | EDS Mapping (JEOL 7600F, NASA JSC, 15 kV).
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
  "@id": "ex:semTAPP-Barnes2025",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol — Barnes2025",
  "schema:description": "SEM-EDS (referred to as SEM-EDX in Extended Data Fig. 8) used to confirm phase identifications of two O-rich presolar grains identified by NanoSIMS isotope mapping: one grain confirmed as ferromagnesian silicate; one confirmed as Al,Mg-bearing oxide (Barnes et al. 2025, p.2 and Extended Data Fig. 8 caption). No instrument name, accelerating voltage, beam current, or sample preparation specifics stated for the JSC SEM-EDS step in this paper.",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "SEM",
      "schema:name": "SEM-EDS (Scanning Electron Microscopy–Energy Dispersive X-ray Spectroscopy)"
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
  "ada:analyticalMode": [
    "N/A"
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
            "EDSDetector",
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
            "Electron source",
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
            "WDSSpectrometer",
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
            "xrayLine",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing"
        }
      ]
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-Barnes2025",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol \u2014 Barnes2025",
  "schema:description": "SEM-EDS (referred to as SEM-EDX in Extended Data Fig. 8) used to confirm phase identifications of two O-rich presolar grains identified by NanoSIMS isotope mapping: one grain confirmed as ferromagnesian silicate; one confirmed as Al,Mg-bearing oxide (Barnes et al. 2025, p.2 and Extended Data Fig. 8 caption). No instrument name, accelerating voltage, beam current, or sample preparation specifics stated for the JSC SEM-EDS step in this paper.",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:termCode": "SEM",
      "schema:name": "SEM-EDS (Scanning Electron Microscopy\u2013Energy Dispersive X-ray Spectroscopy)"
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
  "ada:analyticalMode": [
    "N/A"
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
            "EDSDetector",
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
            "Electron source",
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
            "WDSSpectrometer",
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
            "xrayLine",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing"
        }
      ]
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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

ex:semTAPP-Barnes2025 a cdi:Activity,
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
    schema1:description "SEM-EDS (referred to as SEM-EDX in Extended Data Fig. 8) used to confirm phase identifications of two O-rich presolar grains identified by NanoSIMS isotope mapping: one grain confirmed as ferromagnesian silicate; one confirmed as Al,Mg-bearing oxide (Barnes et al. 2025, p.2 and Extended Data Fig. 8 caption). No instrument name, accelerating voltage, beam current, or sample preparation specifics stated for the JSC SEM-EDS step in this paper." ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "SEM" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "WDSSpectrometer" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Electron source" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "EDSDetector" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "xrayLine" ;
                    schema1:name "missing" ] ;
            schema1:name "missing" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "Astromaterials Research and Exploration Science Division (ARES), NASA Johnson Space Center, Houston, TX, USA" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "SEM-EDS (Scanning Electron Microscopy–Energy Dispersive X-ray Spectroscopy)" ;
            schema1:termCode "SEM" ] ;
    schema1:name "sem protocol — Barnes2025" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Asteroid (101955) Bennu aggregate QL particles; O-rich presolar silicate and oxide grains; sample OREX-501018-100" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "NanoSIMS isotope mapping (CAMECA NanoSIMS 50L, NASA JSC); presolar grains identified by NanoSIMS then confirmed by SEM-EDS phase characterisation" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "N/A" ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:samplingUnit "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:wdsDeadTimeCorrection "missing" .


```


### semTAPP example Barnes2025-2
semTAPP instance derived from Barnes et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | BSE Imaging (FEI Quanta 3D DualBeam + Helios DualBeam, NASA JSC).
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
  "@id": "ex:semTAPP-Barnes2025-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol — Barnes2025-2",
  "schema:description": "No BSE imaging with FEI Quanta 3D DualBeam or Helios DualBeam at NASA JSC described in this paper (Barnes et al. 2025). BSE mosaic imaging was performed using a Hitachi TM4000plus at the University of Arizona (K-ALFAA) at 15-keV electron beam to identify suitable matrix areas for NanoSIMS analysis (Methods, p.11). No JSC BSE imaging conditions or instrument stated.",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
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
            "EDSDetector",
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
            "Electron source",
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
            "WDSSpectrometer",
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
            "xrayLine",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing"
        }
      ]
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-Barnes2025-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol \u2014 Barnes2025-2",
  "schema:description": "No BSE imaging with FEI Quanta 3D DualBeam or Helios DualBeam at NASA JSC described in this paper (Barnes et al. 2025). BSE mosaic imaging was performed using a Hitachi TM4000plus at the University of Arizona (K-ALFAA) at 15-keV electron beam to identify suitable matrix areas for NanoSIMS analysis (Methods, p.11). No JSC BSE imaging conditions or instrument stated.",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
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
            "EDSDetector",
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
            "Electron source",
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
            "WDSSpectrometer",
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
            "xrayLine",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing"
        }
      ]
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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

ex:semTAPP-Barnes2025-2 a cdi:Activity,
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
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "SEM" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Electron source" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "xrayLine" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "EDSDetector" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "WDSSpectrometer" ;
                    schema1:name "missing" ] ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "sem" ;
            schema1:termCode "SEM" ] ;
    schema1:name "sem protocol — Barnes2025-2" ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:samplingUnit "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:wdsDeadTimeCorrection "missing" .


```


### semTAPP example Barnes2025-3
semTAPP instance derived from Barnes et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | TEM Sample Preparation (FEI Helios G4 DualBeam, NASA JSC).
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
  "@id": "ex:semTAPP-Barnes2025-3",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol — Barnes2025-3",
  "schema:description": "No FIB-based TEM sample preparation at NASA JSC described in this paper (Barnes et al. 2025). This paper does not include TEM analysis or FIB-SEM-based sample preparation. FIB-based TEM foil preparation using FEI Helios G4 and related instruments at NASA JSC is described in the companion paper Zega et al. 2025 (Nat. Geosci., ref. 7 therein).",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
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
            "EDSDetector",
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
            "Electron source",
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
            "WDSSpectrometer",
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
            "xrayLine",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing"
        }
      ]
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-Barnes2025-3",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol \u2014 Barnes2025-3",
  "schema:description": "No FIB-based TEM sample preparation at NASA JSC described in this paper (Barnes et al. 2025). This paper does not include TEM analysis or FIB-SEM-based sample preparation. FIB-based TEM foil preparation using FEI Helios G4 and related instruments at NASA JSC is described in the companion paper Zega et al. 2025 (Nat. Geosci., ref. 7 therein).",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
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
            "EDSDetector",
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
            "Electron source",
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
            "WDSSpectrometer",
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
            "xrayLine",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing"
        }
      ]
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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

ex:semTAPP-Barnes2025-3 a cdi:Activity,
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
    schema1:description "No FIB-based TEM sample preparation at NASA JSC described in this paper (Barnes et al. 2025). This paper does not include TEM analysis or FIB-SEM-based sample preparation. FIB-based TEM foil preparation using FEI Helios G4 and related instruments at NASA JSC is described in the companion paper Zega et al. 2025 (Nat. Geosci., ref. 7 therein)." ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "SEM" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Electron source" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "EDSDetector" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "WDSSpectrometer" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "xrayLine" ;
                    schema1:name "missing" ] ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "sem" ;
            schema1:termCode "SEM" ] ;
    schema1:name "sem protocol — Barnes2025-3" ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:samplingUnit "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:wdsDeadTimeCorrection "missing" .


```


### semTAPP example Barnes2025-4
semTAPP instance derived from Barnes et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | TEM Sample Preparation (FEI Helios 660 G3, NASA JSC).
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
  "@id": "ex:semTAPP-Barnes2025-4",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol — Barnes2025-4",
  "schema:description": "No FIB-based TEM sample preparation at NASA JSC described in this paper (Barnes et al. 2025). This paper does not include TEM analysis or FIB-SEM-based sample preparation. TEM foil preparation using FEI Helios 660 G3 and related instruments at NASA JSC is described in the companion paper Zega et al. 2025 (Nat. Geosci., ref. 7 therein).",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
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
            "EDSDetector",
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
            "Electron source",
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
            "WDSSpectrometer",
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
            "xrayLine",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing"
        }
      ]
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semTAPP-Barnes2025-4",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "sem protocol \u2014 Barnes2025-4",
  "schema:description": "No FIB-based TEM sample preparation at NASA JSC described in this paper (Barnes et al. 2025). This paper does not include TEM analysis or FIB-SEM-based sample preparation. TEM foil preparation using FEI Helios 660 G3 and related instruments at NASA JSC is described in the companion paper Zega et al. 2025 (Nat. Geosci., ref. 7 therein).",
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "sem",
      "schema:termCode": "SEM"
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
            "EDSDetector",
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
            "Electron source",
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
            "WDSSpectrometer",
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
            "xrayLine",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing"
        }
      ]
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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

ex:semTAPP-Barnes2025-4 a cdi:Activity,
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
    schema1:description "No FIB-based TEM sample preparation at NASA JSC described in this paper (Barnes et al. 2025). This paper does not include TEM analysis or FIB-SEM-based sample preparation. TEM foil preparation using FEI Helios 660 G3 and related instruments at NASA JSC is described in the companion paper Zega et al. 2025 (Nat. Geosci., ref. 7 therein)." ;
    schema1:instrument [ a schema1:Product,
                schema1:Thing ;
            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                "SEM" ;
            schema1:hasPart [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "Electron source" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "WDSSpectrometer" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "EDSDetector" ;
                    schema1:name "missing" ],
                [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                        "xrayLine" ;
                    schema1:name "missing" ] ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "sem" ;
            schema1:termCode "SEM" ] ;
    schema1:name "sem protocol — Barnes2025-4" ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:edsAcquisitionMode "missing" ;
    ada:edsLiveTimePerPointOrPixelDefault -9999 ;
    ada:massAbsorptionCoefficients "missing" ;
    ada:matrixCorrectionMethod "missing" ;
    ada:samplingUnit "missing" ;
    ada:stepSizePixelSizeDefault -9999 ;
    ada:targetSelectionCriteriaDefault "missing" ;
    ada:wdsDeadTimeCorrection "missing" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: SEM Technique-Aligned Protocol Profile (semTAPP)
description: Scanning electron microscopy superset (imaging + EDS/WDS composition
  + EBSD + FIB-SEM) extension of the base TAPP definition, generated from TAPPS20260813/Current
  TAPPs/SEM_TAPP_v17.xlsx via the path-driven pipeline.
allOf:
- $ref: https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/BaseSchema/tappDefinition/schema.yaml
- type: object
  properties:
    schema:name:
      description: "A short descriptive name for this analytical procedure, including
        a version number. Should identify the instrument, the technique, and the scope
        of what is measured \u2014 analyte, material, or feature."
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
            - SEM
            - SEM/FIB-SEM
            - N/A
            - None
            - missing
            readOnly: true
    schema:creator:
      type: object
      properties:
        schema:name:
          description: Person(s) or laboratory responsible for developing and registering
            this procedure. ORCID recommended for individuals.
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
      description: First date this procedure configuration was used in production.
      type: string
      readOnly: true
    schema:funding:
      type: array
      items:
        type: object
        properties:
          schema:name:
            description: Grants and other funding sources that supported instrument
              acquisition, major upgrades, procedure development, and associated personnel
              time. Include grant numbers and funding agencies where applicable.
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
                    description: DOI or URL for peer-reviewed publications or technical
                      reports describing, validating, or benchmarking this procedure.
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
                      - EPMA; NanoSIMS
                      - XCT (pre-SEM overview)
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
                              this procedure is designed to analyze.
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
                            const: ada:parameter/semTAPP/analysisInclusionAndRejectionCriteriaDefault
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
                            const: ada:parameter/semTAPP/constantsAndReferenceValuesUsedDefault
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
                    allOf:
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
                            const: ada:parameter/semTAPP/analysisInclusionAndRejectionCriteriaDefault
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
                            const: ada:parameter/semTAPP/constantsAndReferenceValuesUsedDefault
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
    ada:targetSelectionCriteriaDefault:
      description: "The rules governing which part of the sample is analysed, and
        why. Covers the criteria applied when choosing grains, aliquots, spots, or
        a region of interest \u2014 size, morphology, clarity, freedom from inclusions
        or alteration, phase identity, or spatial position. Distinct from Target Material,
        which states the material type the procedure is designed for: this field states
        how, within such a sample, the analysed portion is picked out."
      type: string
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
            required:
            - schema:additionalType
          then:
            properties:
              schema:manufacturer:
                type: object
                properties:
                  schema:name:
                    description: Make of the instrument used for this procedure.
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
                    description: Model designation of the SEM or FIB-SEM instrument,
                      including generation suffix if applicable.
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
                            const: Electron source
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
                            const: EDSDetector
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
                            const: WDSSpectrometer
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
                  - if:
                      properties:
                        schema:additionalType:
                          contains:
                            const: xrayLine
                      required:
                      - schema:additionalType
                    then:
                      properties:
                        schema:name:
                          description: X-ray emission line measured on each spectrometer
                            assignment. Line choice affects sensitivity, matrix correction
                            accuracy, and susceptibility to peak overlap and spectral
                            interference.
                          anyOf:
                          - type: string
                            enum:
                            - Ka
                            - Kb
                            - La
                            - Lb
                            - Lg
                            - Ma
                            - Mb
                            - N/A
                            - None
                            - missing
                            readOnly: true
                          - type: array
                            items:
                              type: string
                              enum:
                              - Ka
                              - Kb
                              - La
                              - Lb
                              - Lg
                              - Ma
                              - Mb
                              - N/A
                              - None
                              - missing
                              readOnly: true
                allOf:
                - contains:
                    properties:
                      schema:additionalType:
                        contains:
                          const: Electron source
                    required:
                    - schema:additionalType
                - contains:
                    properties:
                      schema:additionalType:
                        contains:
                          const: xrayLine
                    required:
                    - schema:additionalType
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
      allOf:
      - contains:
          properties:
            schema:additionalType:
              contains:
                const: SEM
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
                description: Software used to control the SEM and acquire data, including
                  version number. For FIB-SEM 3D tomography, include the automated
                  slice-and-view module name and version.
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
                description: Software used for post-acquisition data reduction and
                  analysis. List all packages with version numbers.
                anyOf:
                - type: string
                - type: array
                  items:
                    type: string
        required:
        - ada:toolRole
    ada:analyticalMode:
      type: array
      items:
        description: Primary analytical mode(s) executed under this procedure. For
          multi-mode procedures (e.g., simultaneous BSE + EDS mapping), list all active
          modes.
        type: string
        enum:
        - SE Imaging
        - BSE Imaging
        - EDS
        - SEM-WDS
        - CL
        - EBSD
        - TEM Sample Preparation
        - 3D Tomography
        - N/A
        - None
        - missing
        readOnly: true
    ada:analyteTemplate:
      type: object
      properties:
        ada:analyteColumns:
          type: array
          items:
            anyOf:
            - $ref: https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/AnalyteIdentifierColumn
            - title: Beam Current
              description: Electron beam probe current. Higher current improves signal-to-noise
                for X-ray analysis (EDS/WDS, EBSD) and CL but may increase beam damage
                and reduce spatial resolution. Express in nA; for sub-nA values use
                decimal notation (e.g., 0.4 nA).
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/semTAPP/beamCurrent
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
                  const: ada:analyteColumn/semTAPP/techniquePerAnalyte
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
            - title: Diffracting Crystal
              description: Analyzing crystal (monochromator) used on each spectrometer
                assignment. Crystal choice determines the detectable wavelength range
                and dispersion.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/semTAPP/diffractingCrystal
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
                  const: ada:analyteColumn/semTAPP/wdsSpectrometerChannel
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
            - title: Proportional Counter / Detector
              description: Type of detector used on each spectrometer assignment.
                Affects sensitivity and count rate linearity.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/semTAPP/proportionalCounterDetector
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
                  const: ada:analyteColumn/semTAPP/wdsPhaSetting
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
                  const: ada:analyteColumn/semTAPP/peakCountingTime
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
                  const: ada:analyteColumn/semTAPP/backgroundCountingTime
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
            - title: Background Position(s)
              description: Location(s) of off-peak background measurement(s) relative
                to the peak, in mm or sin-theta, and whether on the high- or low-energy
                side.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/semTAPP/backgroundPosition
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
                  const: ada:analyteColumn/semTAPP/backgroundCorrectionMethod
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
                  const: ada:analyteColumn/semTAPP/timeDependentIntensityCorrection
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
                  const: ada:analyteColumn/semTAPP/analyteEstimationMethod
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
                  const: ada:analyteColumn/semTAPP/blankCorrection
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
                  const: ada:analyteColumn/semTAPP/primaryCalibrationStandardName
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
                  const: ada:analyteColumn/semTAPP/secondaryReferenceMaterials
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
                  const: ada:analyteColumn/semTAPP/interferenceCorrectionsApplied
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
                  const: ada:analyteColumn/semTAPP/interferingElements
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
                  const: ada:analyteColumn/semTAPP/interferenceCorrectionStandard
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
                  const: ada:analyteColumn/semTAPP/analyticalPrecision
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
                  const: ada:analyteColumn/semTAPP/analyticalAccuracy
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
              description: 1-sigma uncertainty propagated from counting statistics
                on peak and background intensities, for each reported concentration
                variable per analysis.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/semTAPP/countingStatisticsError
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
                  const: ada:analyteColumn/semTAPP/beamCurrent
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
                  const: ada:analyteColumn/semTAPP/techniquePerAnalyte
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
              title: Diffracting Crystal
              description: Analyzing crystal (monochromator) used on each spectrometer
                assignment. Crystal choice determines the detectable wavelength range
                and dispersion.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/semTAPP/diffractingCrystal
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
                  const: ada:analyteColumn/semTAPP/wdsSpectrometerChannel
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
              title: Proportional Counter / Detector
              description: Type of detector used on each spectrometer assignment.
                Affects sensitivity and count rate linearity.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/semTAPP/proportionalCounterDetector
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
                  const: ada:analyteColumn/semTAPP/wdsPhaSetting
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
                  const: ada:analyteColumn/semTAPP/peakCountingTime
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
                  const: ada:analyteColumn/semTAPP/backgroundCountingTime
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
              title: Background Position(s)
              description: Location(s) of off-peak background measurement(s) relative
                to the peak, in mm or sin-theta, and whether on the high- or low-energy
                side.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/semTAPP/backgroundPosition
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
                  const: ada:analyteColumn/semTAPP/backgroundCorrectionMethod
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
                  const: ada:analyteColumn/semTAPP/timeDependentIntensityCorrection
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
                  const: ada:analyteColumn/semTAPP/analyteEstimationMethod
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
                  const: ada:analyteColumn/semTAPP/blankCorrection
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
                  const: ada:analyteColumn/semTAPP/primaryCalibrationStandardName
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
                  const: ada:analyteColumn/semTAPP/secondaryReferenceMaterials
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
                  const: ada:analyteColumn/semTAPP/interferenceCorrectionsApplied
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
                  const: ada:analyteColumn/semTAPP/interferingElements
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
                  const: ada:analyteColumn/semTAPP/interferenceCorrectionStandard
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
                  const: ada:analyteColumn/semTAPP/analyticalPrecision
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
                  const: ada:analyteColumn/semTAPP/analyticalAccuracy
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
              description: 1-sigma uncertainty propagated from counting statistics
                on peak and background intensities, for each reported concentration
                variable per analysis.
              type: object
              properties:
                '@id':
                  const: ada:analyteColumn/semTAPP/countingStatisticsError
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
        ada:defaultAnalytes:
          type: array
          items:
            anyOf:
            - type: string
            - $ref: https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/DefinedTerm
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
              const: ada:parameter/semTAPP/beamRasterDimensionsDefault
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
              const: ada:parameter/semTAPP/beamDamageMinimizationDefault
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
              const: ada:parameter/semTAPP/driftCorrectionDefault
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
              const: ada:parameter/semTAPP/stageScanVsBeamScan
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/semTAPP/stageScanVsBeamScan
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
        - title: Sequence
          description: Order in which spectrometer assignments are acquired during
            point analysis. Relevant for minimizing beam damage (volatile elements
            measured first) and for sequential multi-channel setups. Not applicable
            to X-ray mapping, where all assigned spectrometers collect simultaneously
            at each pixel.
          type: object
          properties:
            '@id':
              const: ada:parameter/semTAPP/sequence
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/semTAPP/sequence
            schema:name:
              const: Sequence
            schema:value:
              anyOf:
              - type: number
              - type: string
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
              const: ada:parameter/semTAPP/halogenCorrectionOnOxygenDefault
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
              const: ada:parameter/semTAPP/edsSpectralProcessingType
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/semTAPP/edsSpectralProcessingType
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
            during a single analysis point, reported as width \xD7 height in \xB5m.
            Applicable when Beam Mode = Rastered; defines the effective spatial footprint
            of the measurement and distributes dose over a larger area to reduce beam
            damage on sensitive phases."
          type: object
          properties:
            '@id':
              const: ada:parameter/semTAPP/beamRasterDimensionsDefault
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
              const: ada:parameter/semTAPP/beamDamageMinimizationDefault
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
              const: ada:parameter/semTAPP/driftCorrectionDefault
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
              const: ada:parameter/semTAPP/stageScanVsBeamScan
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/semTAPP/stageScanVsBeamScan
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
          title: Sequence
          description: Order in which spectrometer assignments are acquired during
            point analysis. Relevant for minimizing beam damage (volatile elements
            measured first) and for sequential multi-channel setups. Not applicable
            to X-ray mapping, where all assigned spectrometers collect simultaneously
            at each pixel.
          type: object
          properties:
            '@id':
              const: ada:parameter/semTAPP/sequence
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/semTAPP/sequence
            schema:name:
              const: Sequence
            schema:value:
              anyOf:
              - type: number
              - type: string
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
              const: ada:parameter/semTAPP/halogenCorrectionOnOxygenDefault
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
              const: ada:parameter/semTAPP/edsSpectralProcessingType
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/semTAPP/edsSpectralProcessingType
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
    ada:reportedProperties:
      type: array
      items:
        description: "The final variable(s) this procedure reports and their units
          \u2014 distinct from the fields recording what was *acquired* rather than
          what is reported. A procedure may acquire many channels and report a small
          number of derived quantities; without this field a data consumer cannot
          tell which. Record every reported variable, including intermediate quantities
          reported alongside final ones (e.g. both the 206Pb/238U ratio and the 206Pb/238U
          date). Where a reported variable is a nominal property with no magnitude
          (e.g. a mineral identification), record the variable and give the unit as
          'N/A \u2014 nominal property'."
        type: string
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
        - title: Normalization / Standards-Based Correction
          description: Post-acquisition normalization applied using secondary reference
            materials to correct for session-to-session calibration drift.
          type: object
          properties:
            '@id':
              const: ada:parameter/semTAPP/normalizationStandardsBasedCorrectionDefault
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
        - title: Calibration Factor and Determination Method
          description: 'An externally-calibrated factor that converts the measured
            quantity into the reported quantity, how it was determined, and its uncertainty.
            Applies where the conversion depends on a factor calibrated against a
            reference of independently known value, rather than on the instrument
            response alone. Distinct from the fields that name the calibration material
            and that state which approach applies to which analyte, where the technique
            has them: this field records the resulting factor itself.'
          type: object
          properties:
            '@id':
              const: ada:parameter/semTAPP/calibrationFactorAndDeterminationMethodDefault
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
        - title: Detection Limit
          description: Method detection limit at 99% confidence, one per reported
            concentration variable (one per analyte, these being the same set). Include
            the method used and the resulting value for each.
          type: object
          properties:
            '@id':
              const: ada:parameter/semTAPP/detectionLimitDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: detectionLimitDefault
            schema:name:
              const: Detection Limit
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
        - title: Detection Limit Method
          description: Formula or approach used to calculate detection limits.
          type: object
          properties:
            '@id':
              const: ada:parameter/semTAPP/detectionLimitMethod
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: detectionLimitMethod
            schema:name:
              const: Detection Limit Method
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
              const: ada:parameter/semTAPP/goodnessOfFitOrDispersionStatisticDefault
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
              const: ada:parameter/semTAPP/normalizationStandardsBasedCorrectionDefault
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
          title: Calibration Factor and Determination Method
          description: 'An externally-calibrated factor that converts the measured
            quantity into the reported quantity, how it was determined, and its uncertainty.
            Applies where the conversion depends on a factor calibrated against a
            reference of independently known value, rather than on the instrument
            response alone. Distinct from the fields that name the calibration material
            and that state which approach applies to which analyte, where the technique
            has them: this field records the resulting factor itself.'
          type: object
          properties:
            '@id':
              const: ada:parameter/semTAPP/calibrationFactorAndDeterminationMethodDefault
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
          title: Detection Limit
          description: Method detection limit at 99% confidence, one per reported
            concentration variable (one per analyte, these being the same set). Include
            the method used and the resulting value for each.
          type: object
          properties:
            '@id':
              const: ada:parameter/semTAPP/detectionLimitDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: detectionLimitDefault
            schema:name:
              const: Detection Limit
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
          title: Detection Limit Method
          description: Formula or approach used to calculate detection limits.
          type: object
          properties:
            '@id':
              const: ada:parameter/semTAPP/detectionLimitMethod
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: detectionLimitMethod
            schema:name:
              const: Detection Limit Method
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
              const: ada:parameter/semTAPP/goodnessOfFitOrDispersionStatisticDefault
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
    schema:description:
      description: "Any procedure- or analysis-specific information not captured by
        a structured field anywhere in this TAPP \u2014 including anomalies, deviations
        from the registered procedure, instrument modifications, and supplementary
        context. Scope is the whole document, not Group 6: this is the last field
        of the TAPP and covers all six groups. Use sparingly; a structured field is
        preferred for anything that can be formally categorised."
      type: string
  required:
  - schema:name
  - schema:datePublished
  - ada:samplingUnit
  - ada:targetSelectionCriteriaDefault
  - ada:dwellTimePerPixelDefault
  - ada:edsAcquisitionMode
  - ada:edsLiveTimePerPointOrPixelDefault
  - ada:stepSizePixelSizeDefault
  - ada:matrixCorrectionMethod
  - ada:massAbsorptionCoefficients
  - ada:wdsDeadTimeCorrection

```

Links to the schema:

* YAML version: [schema.yaml](https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/tapp/schema.json)
* JSON version: [schema.json](https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/tapp/schema.yaml)


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
[context.jsonld](https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/tapp/context.jsonld)

## Sources

* [SEM_TAPP_v4.xlsx (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/SEM/tapp`

