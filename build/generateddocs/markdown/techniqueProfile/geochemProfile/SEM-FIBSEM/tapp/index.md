
# FIB-SEM Technique-Aligned Protocol Profile (semFibsemTAPP) (Schema)

`ogch.techniqueProfile.geochemProfile.SEM-FIBSEM.tapp` *v0.1*

Focused-ion-beam SEM (FIB-SEM tomography, TEM lamella prep) extension of the base TAPP definition. Basic protocol-tier fields are required top-level ada: properties; Advanced protocol-tier fields are schema:additionalProperty[] entries. No ada:analyteTemplate. Generated from docs/SEM_FIBSEM_TAPP_v4.xlsx by tools/build_tapp.py.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### semFibsemTAPP example Garvie2008
semFibsemTAPP instance derived from Garvie et al. 2008 | Tagish Lake (C2) nanoglobules | TEM Sample Preparation (FIB, FEI Nova 200 NanoLab).
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
  "@id": "ex:semFibsemTAPP-Garvie2008",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semFibsem protocol — Garvie2008",
  "schema:description": "semFibsemTAPP instance derived from Garvie et al. 2008 | Tagish Lake (C2) nanoglobules | TEM Sample Preparation (FIB, FEI Nova 200 NanoLab) (publication column of SEM_FIBSEM_TAPP_v15.csv).",
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
        "ada:coarseMillingConditionsDefault": "30 kV, 10 pA Ga beam",
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
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Ion milling",
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
      "ada:workingDistanceDefault": "5.4 mm (eucentric height for electron and ion columns)",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "FIBSEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Ion Beam Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "Gallium LMIS (Ga+)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/FIBSEM/part/Ion-Beam-Source"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/FIBSEM",
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
        "schema:name": "SE Imaging (same instrument, pre- and post-FIB milling)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
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
      "schema:name": "semFibsem",
      "schema:termCode": "semFibsem"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:imageRegistration3DDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:segmentationMethod3DDefault": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-FIBSEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semFibsemTAPP-Garvie2008",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semFibsem protocol \u2014 Garvie2008",
  "schema:description": "semFibsemTAPP instance derived from Garvie et al. 2008 | Tagish Lake (C2) nanoglobules | TEM Sample Preparation (FIB, FEI Nova 200 NanoLab) (publication column of SEM_FIBSEM_TAPP_v15.csv).",
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
        "ada:coarseMillingConditionsDefault": "30 kV, 10 pA Ga beam",
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
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Ion milling",
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
      "ada:workingDistanceDefault": "5.4 mm (eucentric height for electron and ion columns)",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "FIBSEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Ion Beam Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "Gallium LMIS (Ga+)",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/FIBSEM/part/Ion-Beam-Source"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/FIBSEM",
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
        "schema:name": "SE Imaging (same instrument, pre- and post-FIB milling)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
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
      "schema:name": "semFibsem",
      "schema:termCode": "semFibsem"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:imageRegistration3DDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:segmentationMethod3DDefault": "missing",
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

ex:semFibsemTAPP-Garvie2008 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Ion milling" ;
                    schema1:position 3 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "HCl and HF acid dissolution residue from pristine Tagish Lake pieces; deposited on lacey C TEM grid attached to Al-SEM stub; uncoated" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ;
                    ada:coarseMillingConditionsDefault "30 kV, 10 pA Ga beam" ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "semFibsemTAPP instance derived from Garvie et al. 2008 | Tagish Lake (C2) nanoglobules | TEM Sample Preparation (FIB, FEI Nova 200 NanoLab) (publication column of SEM_FIBSEM_TAPP_v15.csv)." ;
    schema1:instrument <https://example.org/instrument/FIBSEM>,
        <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "School of Earth and Space Exploration / School of Materials, Arizona State University" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semFibsem" ;
            schema1:termCode "semFibsem" ] ;
    schema1:name "semFibsem protocol — Garvie2008" ;
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
    ada:imageRegistration3DDefault "missing" ;
    ada:samplingUnit "missing" ;
    ada:segmentationMethod3DDefault "missing" ;
    ada:targetSelectionCriteriaDefault "missing" .

<https://example.org/instrument/FIBSEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "FIBSEM" ;
    schema1:hasPart <https://example.org/instrument/FIBSEM/part/Ion-Beam-Source> ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/FIBSEM/part/Ion-Beam-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Ion Beam Source" ;
    schema1:name "Gallium LMIS (Ga+)" .

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
    ada:workingDistanceDefault "5.4 mm (eucentric height for electron and ion columns)" .

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


### semFibsemTAPP example Liu2017
semFibsemTAPP instance derived from Liu et al. 2017 | High-rank coal (Qinshui basin) | 3D Tomography (Carl Zeiss Crossbeam 540).
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
  "@id": "ex:semFibsemTAPP-Liu2017",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semFibsem protocol — Liu2017",
  "schema:description": "semFibsemTAPP instance derived from Liu et al. 2017 | High-rank coal (Qinshui basin) | 3D Tomography (Carl Zeiss Crossbeam 540) (publication column of SEM_FIBSEM_TAPP_v15.csv).",
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
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/semFibsemTAPP/protectiveCoatingDepositionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "protectiveCoatingDepositionDefault",
            "schema:name": "Protective Coating Deposition",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "No coating applied; not sputtered with gold or other materials"
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
      },
      {
        "schema:name": "Ion milling",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/semFibsemTAPP/sliceThicknessDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "sliceThicknessDefault",
            "schema:name": "Slice Thickness",
            "ada:dataType": "number",
            "ada:fieldScope": "session",
            "schema:defaultValue": 15,
            "schema:description": "15 nm (single layer scanning thickness = 9.0 µm total / 600 slices)"
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
    },
    {
      "@id": "ex:instrument/FIBSEM",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:additionalType": [
        "FIBSEM",
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
            "Ion Beam Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/FIBSEM/part/Ion-Beam-Source"
        }
      ]
    }
  ],
  "ada:segmentationMethod3DDefault": "Image denoising, binarization, and segmentation; 3D model established using Avizo 7 and Multiple-point geostatistics",
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
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Avizo 7 (3D digital core software); Multiple-point geostatistics for pore network model"
    }
  ],
  "ada:analyticalMode": [
    "3D Tomography"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "semFibsem",
      "schema:termCode": "semFibsem"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:imageRegistration3DDefault": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-FIBSEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semFibsemTAPP-Liu2017",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semFibsem protocol \u2014 Liu2017",
  "schema:description": "semFibsemTAPP instance derived from Liu et al. 2017 | High-rank coal (Qinshui basin) | 3D Tomography (Carl Zeiss Crossbeam 540) (publication column of SEM_FIBSEM_TAPP_v15.csv).",
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
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/semFibsemTAPP/protectiveCoatingDepositionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "protectiveCoatingDepositionDefault",
            "schema:name": "Protective Coating Deposition",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "No coating applied; not sputtered with gold or other materials"
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
        "schema:name": "Data reduction",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 2
      },
      {
        "schema:name": "Ion milling",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/semFibsemTAPP/sliceThicknessDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "sliceThicknessDefault",
            "schema:name": "Slice Thickness",
            "ada:dataType": "number",
            "ada:fieldScope": "session",
            "schema:defaultValue": 15,
            "schema:description": "15 nm (single layer scanning thickness = 9.0 \u00b5m total / 600 slices)"
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
    },
    {
      "@id": "ex:instrument/FIBSEM",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:additionalType": [
        "FIBSEM",
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
            "Ion Beam Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/FIBSEM/part/Ion-Beam-Source"
        }
      ]
    }
  ],
  "ada:segmentationMethod3DDefault": "Image denoising, binarization, and segmentation; 3D model established using Avizo 7 and Multiple-point geostatistics",
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
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Avizo 7 (3D digital core software); Multiple-point geostatistics for pore network model"
    }
  ],
  "ada:analyticalMode": [
    "3D Tomography"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "semFibsem",
      "schema:termCode": "semFibsem"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:imageRegistration3DDefault": "missing",
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

ex:semFibsemTAPP-Liu2017 a cdi:Activity,
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
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semFibsemTAPP/protectiveCoatingDepositionDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Small coal pillars (~2 mm diameter, 2 mm height) drilled orthogonal to bedding; polished with cross section polisher to remove ~1-2 µm oxide layer; no coating applied" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semFibsemTAPP/sliceThicknessDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Ion milling" ;
                    schema1:position 3 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "semFibsemTAPP instance derived from Liu et al. 2017 | High-rank coal (Qinshui basin) | 3D Tomography (Carl Zeiss Crossbeam 540) (publication column of SEM_FIBSEM_TAPP_v15.csv)." ;
    schema1:instrument <https://example.org/instrument/FIBSEM>,
        <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "China University of Mining and Technology, Xuzhou, China" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semFibsem" ;
            schema1:termCode "semFibsem" ] ;
    schema1:name "semFibsem protocol — Liu2017" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "High-rank coal (anthracite from Bofang Mine; lean coal from Yuwu Mine), southern Qinshui basin, China" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "X-ray CT (Xradia 520 Versa, Carl Zeiss)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "3D Tomography" ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:imageRegistration3DDefault "missing" ;
    ada:samplingUnit "missing" ;
    ada:segmentationMethod3DDefault "Image denoising, binarization, and segmentation; 3D model established using Avizo 7 and Multiple-point geostatistics" ;
    ada:targetSelectionCriteriaDefault "missing" ;
    bios:computationalTool [ schema1:name "Avizo 7 (3D digital core software); Multiple-point geostatistics for pore network model" ;
            ada:toolRole "dataReduction" ] .

<https://ada.astromat.org/metadata/parameter/semFibsemTAPP/protectiveCoatingDepositionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "No coating applied; not sputtered with gold or other materials" ;
    schema1:name "Protective Coating Deposition" ;
    schema1:valueName "protectiveCoatingDepositionDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/semFibsemTAPP/sliceThicknessDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 15 ;
    schema1:description "15 nm (single layer scanning thickness = 9.0 µm total / 600 slices)" ;
    schema1:name "Slice Thickness" ;
    schema1:valueName "sliceThicknessDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://example.org/instrument/FIBSEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "FIBSEM" ;
    schema1:hasPart <https://example.org/instrument/FIBSEM/part/Ion-Beam-Source> ;
    schema1:name "missing" .

<https://example.org/instrument/FIBSEM/part/Ion-Beam-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Ion Beam Source" ;
    schema1:name "missing" .

<https://example.org/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:hasPart <https://example.org/instrument/SEM/part/BSE-Detector>,
        <https://example.org/instrument/SEM/part/Electron-Source>,
        <https://example.org/instrument/SEM/part/SE-Detector> ;
    schema1:manufacturer [ a schema1:Organization ;
            schema1:name "Zeiss" ] ;
    schema1:model [ a schema1:ProductModel ;
            schema1:name "Crossbeam 540" ] ;
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


### semFibsemTAPP example Zhou2017
semFibsemTAPP instance derived from Zhou et al. 2017 | Coal (SC + HBC, Junggar Basin) | 3D Tomography (FEI Helios NanoLab 650).
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
  "@id": "ex:semFibsemTAPP-Zhou2017",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semFibsem protocol — Zhou2017",
  "schema:description": "Stage tilt 52° between electron and ion columns; SEM range 20V–30kV and FIB range 500V–30kV (system specs); destriping filter xStripes.jar applied; deconvolves y-axis by y/sin(52°) for pixel scale correction",
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
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Ion milling",
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
      "schema:description": "N/A",
      "ada:acceleratingVoltageDefault": "2 kV (SEM imaging)",
      "ada:workingDistanceDefault": "4 mm",
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
    },
    {
      "@id": "ex:instrument/FIBSEM",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:additionalType": [
        "FIBSEM",
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
            "Ion Beam Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/FIBSEM/part/Ion-Beam-Source"
        }
      ]
    }
  ],
  "ada:imageRegistration3DDefault": "Fiji/ImageJ StackReg and TurboReg plugins used for slice realignment",
  "ada:segmentationMethod3DDefault": "Semi-automatic porosity segmentation by grayscale thresholding; pore volume reconstruction using FEI Avizo Fire 8.1.1; connected component analysis for pore network extraction (PNE)",
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "China University of Geosciences, Beijing, China"
  },
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Fiji/ImageJ (StackReg/TurboReg for slice alignment; VolumeJ for volume rendering); Adobe Photoshop CS6 (image enhancement); FEI Avizo Fire 8.1.1 (pore volume reconstruction and segmentation)"
    }
  ],
  "ada:analyticalMode": [
    "3D Tomography"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "semFibsem",
      "schema:termCode": "semFibsem"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-FIBSEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semFibsemTAPP-Zhou2017",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semFibsem protocol \u2014 Zhou2017",
  "schema:description": "Stage tilt 52\u00b0 between electron and ion columns; SEM range 20V\u201330kV and FIB range 500V\u201330kV (system specs); destriping filter xStripes.jar applied; deconvolves y-axis by y/sin(52\u00b0) for pixel scale correction",
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
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Ion milling",
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
      "schema:description": "N/A",
      "ada:acceleratingVoltageDefault": "2 kV (SEM imaging)",
      "ada:workingDistanceDefault": "4 mm",
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
    },
    {
      "@id": "ex:instrument/FIBSEM",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:additionalType": [
        "FIBSEM",
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
            "Ion Beam Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/FIBSEM/part/Ion-Beam-Source"
        }
      ]
    }
  ],
  "ada:imageRegistration3DDefault": "Fiji/ImageJ StackReg and TurboReg plugins used for slice realignment",
  "ada:segmentationMethod3DDefault": "Semi-automatic porosity segmentation by grayscale thresholding; pore volume reconstruction using FEI Avizo Fire 8.1.1; connected component analysis for pore network extraction (PNE)",
  "schema:location": {
    "@type": [
      "schema:Place"
    ],
    "schema:name": "China University of Geosciences, Beijing, China"
  },
  "bios:computationalTool": [
    {
      "ada:toolRole": "dataReduction",
      "schema:name": "Fiji/ImageJ (StackReg/TurboReg for slice alignment; VolumeJ for volume rendering); Adobe Photoshop CS6 (image enhancement); FEI Avizo Fire 8.1.1 (pore volume reconstruction and segmentation)"
    }
  ],
  "ada:analyticalMode": [
    "3D Tomography"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "semFibsem",
      "schema:termCode": "semFibsem"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
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

ex:semFibsemTAPP-Zhou2017 a cdi:Activity,
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
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Ion milling" ;
                    schema1:position 3 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "Stage tilt 52° between electron and ion columns; SEM range 20V–30kV and FIB range 500V–30kV (system specs); destriping filter xStripes.jar applied; deconvolves y-axis by y/sin(52°) for pixel scale correction" ;
    schema1:instrument <https://example.org/instrument/FIBSEM>,
        <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "China University of Geosciences, Beijing, China" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semFibsem" ;
            schema1:termCode "semFibsem" ] ;
    schema1:name "semFibsem protocol — Zhou2017" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Subbituminous coal (SC) and high-volatile bituminous coal (HBC), Xishanyao Formation, southern Junggar Basin, NW China" ] ] ;
    ada:analyticalMode "3D Tomography" ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:imageRegistration3DDefault "Fiji/ImageJ StackReg and TurboReg plugins used for slice realignment" ;
    ada:samplingUnit "missing" ;
    ada:segmentationMethod3DDefault "Semi-automatic porosity segmentation by grayscale thresholding; pore volume reconstruction using FEI Avizo Fire 8.1.1; connected component analysis for pore network extraction (PNE)" ;
    ada:targetSelectionCriteriaDefault "missing" ;
    bios:computationalTool [ schema1:name "Fiji/ImageJ (StackReg/TurboReg for slice alignment; VolumeJ for volume rendering); Adobe Photoshop CS6 (image enhancement); FEI Avizo Fire 8.1.1 (pore volume reconstruction and segmentation)" ;
            ada:toolRole "dataReduction" ] .

<https://example.org/instrument/FIBSEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "FIBSEM" ;
    schema1:hasPart <https://example.org/instrument/FIBSEM/part/Ion-Beam-Source> ;
    schema1:name "missing" .

<https://example.org/instrument/FIBSEM/part/Ion-Beam-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Ion Beam Source" ;
    schema1:name "missing" .

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
            schema1:name "Helios NanoLab 650" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "2 kV (SEM imaging)" ;
    ada:workingDistanceDefault "4 mm" .

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


### semFibsemTAPP example Zega2025
semFibsemTAPP instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | TEM Sample Preparation (Helios G3, U Arizona).
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
  "@id": "ex:semFibsemTAPP-Zega2025",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semFibsem protocol — Zega2025",
  "schema:description": "Sections thinned to electron transparency; BSE/SE images acquired before and after sectioning; methods follow refs. 72-75",
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
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/semFibsemTAPP/protectiveCoatingDepositionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "protectiveCoatingDepositionDefault",
            "schema:name": "Protective Coating Deposition",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "12-µm wide × 4-µm tall carbon capping layer deposited on matrix areas"
          }
        ],
        "ada:coarseMillingConditionsDefault": "Standard stair step; 30 keV, currents 2.5 to 0.8 nA",
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
      },
      {
        "schema:name": "Ion milling",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/semFibsemTAPP/liftOutMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/semFibsemTAPP/liftOutMethod"
              }
            ],
            "schema:name": "Lift-out Method",
            "schema:value": "In-situ lift-out (standard stair step)"
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
      "ada:acceleratingVoltageDefault": "30 keV (FIB milling and thinning)",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    },
    {
      "@id": "ex:instrument/FIBSEM",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:additionalType": [
        "FIBSEM",
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
            "Ion Beam Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/FIBSEM/part/Ion-Beam-Source"
        }
      ]
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
        "schema:name": "TEM analysis (HF5000 STEM, U Arizona); BSE/SE Imaging (Hitachi S-4800, U Arizona)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
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
      "schema:name": "semFibsem",
      "schema:termCode": "semFibsem"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:imageRegistration3DDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:segmentationMethod3DDefault": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-FIBSEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semFibsemTAPP-Zega2025",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semFibsem protocol \u2014 Zega2025",
  "schema:description": "Sections thinned to electron transparency; BSE/SE images acquired before and after sectioning; methods follow refs. 72-75",
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
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/semFibsemTAPP/protectiveCoatingDepositionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "protectiveCoatingDepositionDefault",
            "schema:name": "Protective Coating Deposition",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "12-\u00b5m wide \u00d7 4-\u00b5m tall carbon capping layer deposited on matrix areas"
          }
        ],
        "ada:coarseMillingConditionsDefault": "Standard stair step; 30 keV, currents 2.5 to 0.8 nA",
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
      },
      {
        "schema:name": "Ion milling",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/semFibsemTAPP/liftOutMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/semFibsemTAPP/liftOutMethod"
              }
            ],
            "schema:name": "Lift-out Method",
            "schema:value": "In-situ lift-out (standard stair step)"
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
      "ada:acceleratingVoltageDefault": "30 keV (FIB milling and thinning)",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    },
    {
      "@id": "ex:instrument/FIBSEM",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:additionalType": [
        "FIBSEM",
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
            "Ion Beam Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/FIBSEM/part/Ion-Beam-Source"
        }
      ]
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
        "schema:name": "TEM analysis (HF5000 STEM, U Arizona); BSE/SE Imaging (Hitachi S-4800, U Arizona)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
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
      "schema:name": "semFibsem",
      "schema:termCode": "semFibsem"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:imageRegistration3DDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:segmentationMethod3DDefault": "missing",
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

ex:semFibsemTAPP-Zega2025 a cdi:Activity,
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
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semFibsemTAPP/liftOutMethod> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Ion milling" ;
                    schema1:position 3 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semFibsemTAPP/protectiveCoatingDepositionDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Sections extracted from fine-grained matrix areas in polished sections; BSE and SE images acquired before and after sectioning" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ;
                    ada:coarseMillingConditionsDefault "Standard stair step; 30 keV, currents 2.5 to 0.8 nA" ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "Sections thinned to electron transparency; BSE/SE images acquired before and after sectioning; methods follow refs. 72-75" ;
    schema1:instrument <https://example.org/instrument/FIBSEM>,
        <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "K-ALFAA (Kuiper-Arizona Laboratory for Astromaterials Analysis), University of Arizona" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semFibsem" ;
            schema1:termCode "semFibsem" ] ;
    schema1:name "semFibsem protocol — Zega2025" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Asteroid (101955) Bennu particles (OSIRIS-REx sample return); fine-grained matrix areas" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "TEM analysis (HF5000 STEM, U Arizona); BSE/SE Imaging (Hitachi S-4800, U Arizona)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "TEM Sample Preparation" ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:imageRegistration3DDefault "missing" ;
    ada:samplingUnit "missing" ;
    ada:segmentationMethod3DDefault "missing" ;
    ada:targetSelectionCriteriaDefault "missing" .

<https://ada.astromat.org/metadata/parameter/semFibsemTAPP/protectiveCoatingDepositionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "12-µm wide × 4-µm tall carbon capping layer deposited on matrix areas" ;
    schema1:name "Protective Coating Deposition" ;
    schema1:valueName "protectiveCoatingDepositionDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/FIBSEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "FIBSEM" ;
    schema1:hasPart <https://example.org/instrument/FIBSEM/part/Ion-Beam-Source> ;
    schema1:name "missing" .

<https://example.org/instrument/FIBSEM/part/Ion-Beam-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Ion Beam Source" ;
    schema1:name "missing" .

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
            schema1:name "Helios G3" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "30 keV (FIB milling and thinning)" .

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

<https://ada.astromat.org/metadata/parameter/semFibsemTAPP/liftOutMethod> a schema1:PropertyValue ;
    schema1:name "Lift-out Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semFibsemTAPP/liftOutMethod> ;
    schema1:value "In-situ lift-out (standard stair step)" .


```


### semFibsemTAPP example Zega2025-2
semFibsemTAPP instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | TEM Sample Preparation (Helios G4 UX, UC Berkeley).
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
  "@id": "ex:semFibsemTAPP-Zega2025-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semFibsem protocol — Zega2025-2",
  "schema:description": "Thicker sections (<100 nm) for TEM; sections up to 600 nm for Fe-L XANES and tomography",
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
        "ada:coarseMillingConditionsDefault": "Ga+ ion beam at 16–30 keV (coarse milling)",
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
      },
      {
        "schema:name": "Ion milling",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/semFibsemTAPP/finePolishingConditionsDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "finePolishingConditionsDefault",
            "schema:name": "Fine Polishing Conditions",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Various voltages down to 1 keV (polishing)"
          },
          {
            "@id": "ada:parameter/semFibsemTAPP/foilThicknessDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "foilThicknessDefault",
            "schema:name": "Foil Thickness",
            "ada:dataType": "number",
            "ada:fieldScope": "session",
            "schema:defaultValue": 100,
            "schema:description": "<100 to 600 nm (variable, depending on targeted experiment)"
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
      "ada:acceleratingVoltageDefault": "16 to 30 keV (coarse milling); down to 1 keV (polishing)",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "FIBSEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Ion Beam Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "N/A",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/FIBSEM/part/Ion-Beam-Source"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/FIBSEM",
      "schema:name": "example instrumentName"
    }
  ],
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
  "ada:analyticalMode": [
    "TEM Sample Preparation"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "semFibsem",
      "schema:termCode": "semFibsem"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:imageRegistration3DDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:segmentationMethod3DDefault": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-FIBSEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semFibsemTAPP-Zega2025-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semFibsem protocol \u2014 Zega2025-2",
  "schema:description": "Thicker sections (<100 nm) for TEM; sections up to 600 nm for Fe-L XANES and tomography",
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
        "ada:coarseMillingConditionsDefault": "Ga+ ion beam at 16\u201330 keV (coarse milling)",
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
      },
      {
        "schema:name": "Ion milling",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/semFibsemTAPP/finePolishingConditionsDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "finePolishingConditionsDefault",
            "schema:name": "Fine Polishing Conditions",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Various voltages down to 1 keV (polishing)"
          },
          {
            "@id": "ada:parameter/semFibsemTAPP/foilThicknessDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "foilThicknessDefault",
            "schema:name": "Foil Thickness",
            "ada:dataType": "number",
            "ada:fieldScope": "session",
            "schema:defaultValue": 100,
            "schema:description": "<100 to 600 nm (variable, depending on targeted experiment)"
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
      "ada:acceleratingVoltageDefault": "16 to 30 keV (coarse milling); down to 1 keV (polishing)",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "FIBSEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Ion Beam Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "N/A",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/FIBSEM/part/Ion-Beam-Source"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/FIBSEM",
      "schema:name": "example instrumentName"
    }
  ],
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
  "ada:analyticalMode": [
    "TEM Sample Preparation"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "semFibsem",
      "schema:termCode": "semFibsem"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:imageRegistration3DDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:segmentationMethod3DDefault": "missing",
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

ex:semFibsemTAPP-Zega2025-2 a cdi:Activity,
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
                    schema1:position 1 ;
                    ada:coarseMillingConditionsDefault "Ga+ ion beam at 16–30 keV (coarse milling)" ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semFibsemTAPP/finePolishingConditionsDefault>,
                        <https://ada.astromat.org/metadata/parameter/semFibsemTAPP/foilThicknessDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Ion milling" ;
                    schema1:position 3 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "Thicker sections (<100 nm) for TEM; sections up to 600 nm for Fe-L XANES and tomography" ;
    schema1:instrument <https://example.org/instrument/FIBSEM>,
        <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "Molecular Foundry, Lawrence Berkeley National Laboratory (UC Berkeley)" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semFibsem" ;
            schema1:termCode "semFibsem" ] ;
    schema1:name "semFibsem protocol — Zega2025-2" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Asteroid (101955) Bennu particles (OSIRIS-REx sample return)" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "Synchrotron XANES (ALS, Berkeley); TEM analysis" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "TEM Sample Preparation" ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:imageRegistration3DDefault "missing" ;
    ada:samplingUnit "missing" ;
    ada:segmentationMethod3DDefault "missing" ;
    ada:targetSelectionCriteriaDefault "missing" .

<https://ada.astromat.org/metadata/parameter/semFibsemTAPP/finePolishingConditionsDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Various voltages down to 1 keV (polishing)" ;
    schema1:name "Fine Polishing Conditions" ;
    schema1:valueName "finePolishingConditionsDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/semFibsemTAPP/foilThicknessDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 100 ;
    schema1:description "<100 to 600 nm (variable, depending on targeted experiment)" ;
    schema1:name "Foil Thickness" ;
    schema1:valueName "foilThicknessDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://example.org/instrument/FIBSEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "FIBSEM" ;
    schema1:hasPart <https://example.org/instrument/FIBSEM/part/Ion-Beam-Source> ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/FIBSEM/part/Ion-Beam-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Ion Beam Source" ;
    schema1:name "N/A" .

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
            schema1:name "Helios G4 UX" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "16 to 30 keV (coarse milling); down to 1 keV (polishing)" .

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


### semFibsemTAPP example Zega2025-3
semFibsemTAPP instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | TEM Sample Preparation (Quanta3D600, NASA JSC).
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
  "@id": "ex:semFibsemTAPP-Zega2025-3",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semFibsem protocol — Zega2025-3",
  "schema:description": "Multi-step milling: e-beam C deposition then FIB C capping, 30 kV → 16 kV → 5 kV; Pt weld to Cu half grids",
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
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/semFibsemTAPP/protectiveCoatingDepositionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "protectiveCoatingDepositionDefault",
            "schema:name": "Protective Coating Deposition",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Electron-beam deposited carbon (~0.5–1 µm); followed by ion beam-deposited carbon (~2–3 µm capping layer)"
          }
        ],
        "ada:coarseMillingConditionsDefault": "Ga+ ion beam at 30 kV (initial milling); 16 kV (intermediate)",
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
      },
      {
        "schema:name": "Ion milling",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/semFibsemTAPP/finePolishingConditionsDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "finePolishingConditionsDefault",
            "schema:name": "Fine Polishing Conditions",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Ga+ ion beam at 5 kV (final thinning) until ~100 nm thick"
          },
          {
            "@id": "ada:parameter/semFibsemTAPP/foilThicknessDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "foilThicknessDefault",
            "schema:name": "Foil Thickness",
            "ada:dataType": "number",
            "ada:fieldScope": "session",
            "schema:defaultValue": 100,
            "schema:description": "~100 nm"
          },
          {
            "@id": "ada:parameter/semFibsemTAPP/liftOutMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/semFibsemTAPP/liftOutMethod"
              }
            ],
            "schema:name": "Lift-out Method",
            "schema:value": "In-situ lift-out; ion beam-deposited Pt weld to Cu half grids"
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
      "ada:acceleratingVoltageDefault": "30 kV (initial milling); 16 kV (intermediate); 5 kV (final thinning)",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "FIBSEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Ion Beam Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "N/A",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/FIBSEM/part/Ion-Beam-Source"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/FIBSEM",
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
        "schema:name": "TEM analysis (NASA JSC); BSE/SE Imaging (JEOL 7600F, JSC)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
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
      "schema:name": "semFibsem",
      "schema:termCode": "semFibsem"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:imageRegistration3DDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:segmentationMethod3DDefault": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-FIBSEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semFibsemTAPP-Zega2025-3",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semFibsem protocol \u2014 Zega2025-3",
  "schema:description": "Multi-step milling: e-beam C deposition then FIB C capping, 30 kV \u2192 16 kV \u2192 5 kV; Pt weld to Cu half grids",
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
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/semFibsemTAPP/protectiveCoatingDepositionDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "protectiveCoatingDepositionDefault",
            "schema:name": "Protective Coating Deposition",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Electron-beam deposited carbon (~0.5\u20131 \u00b5m); followed by ion beam-deposited carbon (~2\u20133 \u00b5m capping layer)"
          }
        ],
        "ada:coarseMillingConditionsDefault": "Ga+ ion beam at 30 kV (initial milling); 16 kV (intermediate)",
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
      },
      {
        "schema:name": "Ion milling",
        "schema:additionalProperty": [
          {
            "@id": "ada:parameter/semFibsemTAPP/finePolishingConditionsDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "finePolishingConditionsDefault",
            "schema:name": "Fine Polishing Conditions",
            "ada:dataType": "string",
            "ada:fieldScope": "session",
            "schema:defaultValue": "Ga+ ion beam at 5 kV (final thinning) until ~100 nm thick"
          },
          {
            "@id": "ada:parameter/semFibsemTAPP/foilThicknessDefault",
            "@type": [
              "schema:PropertyValueSpecification"
            ],
            "schema:valueName": "foilThicknessDefault",
            "schema:name": "Foil Thickness",
            "ada:dataType": "number",
            "ada:fieldScope": "session",
            "schema:defaultValue": 100,
            "schema:description": "~100 nm"
          },
          {
            "@id": "ada:parameter/semFibsemTAPP/liftOutMethod",
            "@type": [
              "schema:PropertyValue"
            ],
            "schema:propertyID": [
              {
                "@id": "ada:parameter/semFibsemTAPP/liftOutMethod"
              }
            ],
            "schema:name": "Lift-out Method",
            "schema:value": "In-situ lift-out; ion beam-deposited Pt weld to Cu half grids"
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
      "ada:acceleratingVoltageDefault": "30 kV (initial milling); 16 kV (intermediate); 5 kV (final thinning)",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/SEM",
      "schema:name": "example instrumentName"
    },
    {
      "schema:additionalType": [
        "FIBSEM",
        {
          "@id": "https://www.wikidata.org/wiki/Q3099911"
        }
      ],
      "schema:hasPart": [
        {
          "schema:additionalType": [
            "Ion Beam Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "N/A",
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "@id": "ex:instrument/FIBSEM/part/Ion-Beam-Source"
        }
      ],
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "@id": "ex:instrument/FIBSEM",
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
        "schema:name": "TEM analysis (NASA JSC); BSE/SE Imaging (JEOL 7600F, JSC)"
      },
      "@type": [
        "schema:CreativeWork"
      ],
      "schema:url": "https://ada.astromat.org/missing"
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
      "schema:name": "semFibsem",
      "schema:termCode": "semFibsem"
    }
  ],
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:imageRegistration3DDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:segmentationMethod3DDefault": "missing",
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

ex:semFibsemTAPP-Zega2025-3 a cdi:Activity,
        schema1:Action,
        prov:Plan,
        ada:TAPPDefinition,
        bios:LabProtocol ;
    schema1:actionProcess [ a schema1:HowTo ;
            schema1:step [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semFibsemTAPP/finePolishingConditionsDefault>,
                        <https://ada.astromat.org/metadata/parameter/semFibsemTAPP/foilThicknessDefault>,
                        <https://ada.astromat.org/metadata/parameter/semFibsemTAPP/liftOutMethod> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Ion milling" ;
                    schema1:position 3 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/semFibsemTAPP/protectiveCoatingDepositionDefault> ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:description "Particles dispersed on conductive carbon dots on Al SEM pin mounts" ;
                    schema1:name "Sample preparation" ;
                    schema1:position 1 ;
                    ada:coarseMillingConditionsDefault "Ga+ ion beam at 30 kV (initial milling); 16 kV (intermediate)" ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Data reduction" ;
                    schema1:position 2 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "Multi-step milling: e-beam C deposition then FIB C capping, 30 kV → 16 kV → 5 kV; Pt weld to Cu half grids" ;
    schema1:instrument <https://example.org/instrument/FIBSEM>,
        <https://example.org/instrument/SEM> ;
    schema1:location [ a schema1:Place ;
            schema1:name "NASA Johnson Space Center (JSC), Houston, TX, USA" ] ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semFibsem" ;
            schema1:termCode "semFibsem" ] ;
    schema1:name "semFibsem protocol — Zega2025-3" ;
    schema1:object [ a schema1:DefinedTerm,
                schema1:Thing,
                <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
            schema1:additionalProperty [ schema1:name "Target Material" ;
                    schema1:value "Asteroid (101955) Bennu particles (OSIRIS-REx sample return)" ] ] ;
    schema1:relatedLink [ a schema1:CreativeWork ;
            schema1:linkRelationship "coupledTechnique" ;
            schema1:target [ schema1:name "TEM analysis (NASA JSC); BSE/SE Imaging (JEOL 7600F, JSC)" ] ;
            schema1:url "https://ada.astromat.org/missing" ] ;
    ada:analyticalMode "TEM Sample Preparation" ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:imageRegistration3DDefault "missing" ;
    ada:samplingUnit "missing" ;
    ada:segmentationMethod3DDefault "missing" ;
    ada:targetSelectionCriteriaDefault "missing" .

<https://ada.astromat.org/metadata/parameter/semFibsemTAPP/finePolishingConditionsDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Ga+ ion beam at 5 kV (final thinning) until ~100 nm thick" ;
    schema1:name "Fine Polishing Conditions" ;
    schema1:valueName "finePolishingConditionsDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/semFibsemTAPP/foilThicknessDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue 100 ;
    schema1:description "~100 nm" ;
    schema1:name "Foil Thickness" ;
    schema1:valueName "foilThicknessDefault" ;
    ada:dataType "number" ;
    ada:fieldScope "session" .

<https://ada.astromat.org/metadata/parameter/semFibsemTAPP/protectiveCoatingDepositionDefault> a schema1:PropertyValueSpecification ;
    schema1:defaultValue "Electron-beam deposited carbon (~0.5–1 µm); followed by ion beam-deposited carbon (~2–3 µm capping layer)" ;
    schema1:name "Protective Coating Deposition" ;
    schema1:valueName "protectiveCoatingDepositionDefault" ;
    ada:dataType "string" ;
    ada:fieldScope "session" .

<https://example.org/instrument/FIBSEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "FIBSEM" ;
    schema1:hasPart <https://example.org/instrument/FIBSEM/part/Ion-Beam-Source> ;
    schema1:name "example instrumentName" .

<https://example.org/instrument/FIBSEM/part/Ion-Beam-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Ion Beam Source" ;
    schema1:name "N/A" .

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
            schema1:name "Quanta 3D 600" ] ;
    schema1:name "example instrumentName" ;
    ada:acceleratingVoltageDefault "30 kV (initial milling); 16 kV (intermediate); 5 kV (final thinning)" .

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

<https://ada.astromat.org/metadata/parameter/semFibsemTAPP/liftOutMethod> a schema1:PropertyValue ;
    schema1:name "Lift-out Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/semFibsemTAPP/liftOutMethod> ;
    schema1:value "In-situ lift-out; ion beam-deposited Pt weld to Cu half grids" .


```


### semFibsemTAPP example Barnes2025
semFibsemTAPP instance derived from Barnes et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | TEM Sample Preparation (FEI Helios G4 DualBeam, NASA JSC).
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
  "@id": "ex:semFibsemTAPP-Barnes2025",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semFibsem protocol — Barnes2025",
  "schema:description": "No FIB-based TEM sample preparation at NASA JSC described in this paper (Barnes et al. 2025). This paper does not include TEM analysis or FIB-SEM-based sample preparation. FIB-based TEM foil preparation using FEI Helios G4 and related instruments at NASA JSC is described in the companion paper Zega et al. 2025 (Nat. Geosci., ref. 7 therein).",
  "ada:analyticalMode": [
    "TEM Sample Preparation"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "semFibsem",
      "schema:termCode": "semFibsem"
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
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Ion milling",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 3
      }
    ]
  },
  "schema:instrument": [
    {
      "@id": "ex:instrument/FIBSEM",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:additionalType": [
        "FIBSEM",
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
            "Ion Beam Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/FIBSEM/part/Ion-Beam-Source"
        }
      ]
    },
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
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:imageRegistration3DDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:segmentationMethod3DDefault": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-FIBSEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semFibsemTAPP-Barnes2025",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semFibsem protocol \u2014 Barnes2025",
  "schema:description": "No FIB-based TEM sample preparation at NASA JSC described in this paper (Barnes et al. 2025). This paper does not include TEM analysis or FIB-SEM-based sample preparation. FIB-based TEM foil preparation using FEI Helios G4 and related instruments at NASA JSC is described in the companion paper Zega et al. 2025 (Nat. Geosci., ref. 7 therein).",
  "ada:analyticalMode": [
    "TEM Sample Preparation"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "semFibsem",
      "schema:termCode": "semFibsem"
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
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Ion milling",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 3
      }
    ]
  },
  "schema:instrument": [
    {
      "@id": "ex:instrument/FIBSEM",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:additionalType": [
        "FIBSEM",
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
            "Ion Beam Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/FIBSEM/part/Ion-Beam-Source"
        }
      ]
    },
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
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:imageRegistration3DDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:segmentationMethod3DDefault": "missing",
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

ex:semFibsemTAPP-Barnes2025 a cdi:Activity,
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
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Ion milling" ;
                    schema1:position 3 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "No FIB-based TEM sample preparation at NASA JSC described in this paper (Barnes et al. 2025). This paper does not include TEM analysis or FIB-SEM-based sample preparation. FIB-based TEM foil preparation using FEI Helios G4 and related instruments at NASA JSC is described in the companion paper Zega et al. 2025 (Nat. Geosci., ref. 7 therein)." ;
    schema1:instrument <https://example.org/instrument/FIBSEM>,
        <https://example.org/instrument/SEM> ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semFibsem" ;
            schema1:termCode "semFibsem" ] ;
    schema1:name "semFibsem protocol — Barnes2025" ;
    ada:analyticalMode "TEM Sample Preparation" ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:imageRegistration3DDefault "missing" ;
    ada:samplingUnit "missing" ;
    ada:segmentationMethod3DDefault "missing" ;
    ada:targetSelectionCriteriaDefault "missing" .

<https://example.org/instrument/FIBSEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "FIBSEM" ;
    schema1:hasPart <https://example.org/instrument/FIBSEM/part/Ion-Beam-Source> ;
    schema1:name "missing" .

<https://example.org/instrument/FIBSEM/part/Ion-Beam-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Ion Beam Source" ;
    schema1:name "missing" .

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


### semFibsemTAPP example Barnes2025-2
semFibsemTAPP instance derived from Barnes et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | TEM Sample Preparation (FEI Helios 660 G3, NASA JSC).
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
  "@id": "ex:semFibsemTAPP-Barnes2025-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semFibsem protocol — Barnes2025-2",
  "schema:description": "No FIB-based TEM sample preparation at NASA JSC described in this paper (Barnes et al. 2025). This paper does not include TEM analysis or FIB-SEM-based sample preparation. TEM foil preparation using FEI Helios 660 G3 and related instruments at NASA JSC is described in the companion paper Zega et al. 2025 (Nat. Geosci., ref. 7 therein).",
  "ada:analyticalMode": [
    "TEM Sample Preparation"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "semFibsem",
      "schema:termCode": "semFibsem"
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
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Ion milling",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 3
      }
    ]
  },
  "schema:instrument": [
    {
      "@id": "ex:instrument/FIBSEM",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:additionalType": [
        "FIBSEM",
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
            "Ion Beam Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/FIBSEM/part/Ion-Beam-Source"
        }
      ]
    },
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
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:imageRegistration3DDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:segmentationMethod3DDefault": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-FIBSEM/tapp/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:semFibsemTAPP-Barnes2025-2",
  "@type": [
    "prov:Plan",
    "cdi:Activity",
    "schema:Action",
    "ada:TAPPDefinition",
    "bios:LabProtocol"
  ],
  "schema:name": "semFibsem protocol \u2014 Barnes2025-2",
  "schema:description": "No FIB-based TEM sample preparation at NASA JSC described in this paper (Barnes et al. 2025). This paper does not include TEM analysis or FIB-SEM-based sample preparation. TEM foil preparation using FEI Helios 660 G3 and related instruments at NASA JSC is described in the companion paper Zega et al. 2025 (Nat. Geosci., ref. 7 therein).",
  "ada:analyticalMode": [
    "TEM Sample Preparation"
  ],
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "semFibsem",
      "schema:termCode": "semFibsem"
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
      },
      {
        "@type": [
          "cdi:Activity",
          "schema:Action"
        ],
        "schema:name": "Ion milling",
        "schema:additionalType": [
          "bios:LabProcess"
        ],
        "schema:position": 3
      }
    ]
  },
  "schema:instrument": [
    {
      "@id": "ex:instrument/FIBSEM",
      "@type": [
        "schema:Product",
        "schema:Thing"
      ],
      "schema:additionalType": [
        "FIBSEM",
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
            "Ion Beam Source",
            {
              "@id": "https://www.wikidata.org/wiki/Q3099911"
            }
          ],
          "schema:name": "missing",
          "@id": "ex:instrument/FIBSEM/part/Ion-Beam-Source"
        }
      ]
    },
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
  "ada:dwellTimePerPixelDefault": -9999,
  "ada:imageRegistration3DDefault": "missing",
  "ada:samplingUnit": "missing",
  "ada:segmentationMethod3DDefault": "missing",
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

ex:semFibsemTAPP-Barnes2025-2 a cdi:Activity,
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
                    schema1:position 2 ],
                [ a cdi:Activity,
                        schema1:Action ;
                    schema1:additionalType "bios:LabProcess" ;
                    schema1:name "Ion milling" ;
                    schema1:position 3 ] ] ;
    schema1:datePublished "missing" ;
    schema1:description "No FIB-based TEM sample preparation at NASA JSC described in this paper (Barnes et al. 2025). This paper does not include TEM analysis or FIB-SEM-based sample preparation. TEM foil preparation using FEI Helios 660 G3 and related instruments at NASA JSC is described in the companion paper Zega et al. 2025 (Nat. Geosci., ref. 7 therein)." ;
    schema1:instrument <https://example.org/instrument/FIBSEM>,
        <https://example.org/instrument/SEM> ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:name "semFibsem" ;
            schema1:termCode "semFibsem" ] ;
    schema1:name "semFibsem protocol — Barnes2025-2" ;
    ada:analyticalMode "TEM Sample Preparation" ;
    ada:dwellTimePerPixelDefault -9999 ;
    ada:imageRegistration3DDefault "missing" ;
    ada:samplingUnit "missing" ;
    ada:segmentationMethod3DDefault "missing" ;
    ada:targetSelectionCriteriaDefault "missing" .

<https://example.org/instrument/FIBSEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "FIBSEM" ;
    schema1:hasPart <https://example.org/instrument/FIBSEM/part/Ion-Beam-Source> ;
    schema1:name "missing" .

<https://example.org/instrument/FIBSEM/part/Ion-Beam-Source> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "Ion Beam Source" ;
    schema1:name "missing" .

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
title: FIB-SEM Technique-Aligned Protocol Profile (semFibsemTAPP)
description: 'Focused-ion-beam SEM (FIB-SEM tomography, TEM lamella prep) extension
  of the base TAPP definition. Basic protocol-tier fields are required top-level ada:
  properties; Advanced protocol-tier fields are schema:additionalProperty[] entries.
  No ada:analyteTemplate. Generated from tapp/Current TAPPs/SEM_FIBSEM_TAPP_v15.csv
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
                  schema:additionalProperty:
                    type: array
                    items:
                      title: Protective Coating Deposition
                      description: 'Type and deposition conditions of the protective
                        coating applied to the sample surface before FIB milling.
                        E-beam deposition causes less surface damage than ion-beam
                        deposition and should be applied as the initial layer. Typical
                        coatings: platinum (Pt) or carbon (C). State material, deposition
                        method, beam conditions, and approximate thickness.'
                      type: object
                      properties:
                        '@id':
                          const: ada:parameter/semFibsemTAPP/protectiveCoatingDepositionDefault
                        '@type':
                          const:
                          - schema:PropertyValueSpecification
                        schema:valueName:
                          const: protectiveCoatingDepositionDefault
                        schema:name:
                          const: Protective Coating Deposition
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
                        title: Protective Coating Deposition
                        description: 'Type and deposition conditions of the protective
                          coating applied to the sample surface before FIB milling.
                          E-beam deposition causes less surface damage than ion-beam
                          deposition and should be applied as the initial layer. Typical
                          coatings: platinum (Pt) or carbon (C). State material, deposition
                          method, beam conditions, and approximate thickness.'
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/semFibsemTAPP/protectiveCoatingDepositionDefault
                          '@type':
                            const:
                            - schema:PropertyValueSpecification
                          schema:valueName:
                            const: protectiveCoatingDepositionDefault
                          schema:name:
                            const: Protective Coating Deposition
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
                  ada:coarseMillingConditionsDefault:
                    description: 'Ion beam voltage and current used for bulk material
                      removal during FIB milling. For TEM specimen preparation: bulk
                      trenching to isolate the lamella and intermediate thinning.
                      For 3D tomography: face preparation and initial slice removal.'
                    anyOf:
                    - type: string
                    - type: array
                      items:
                        type: string
            - if:
                properties:
                  schema:name:
                    const: Ion milling
                required:
                - schema:name
              then:
                properties:
                  schema:additionalProperty:
                    type: array
                    items:
                      anyOf:
                      - title: Fine Polishing Conditions
                        description: Ion beam voltage and current for final thinning
                          and surface polishing of the TEM lamella. Low-voltage polishing
                          (2 kV or below) minimises Ga implantation depth, surface
                          amorphisation, and curtaining artifacts.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/semFibsemTAPP/finePolishingConditionsDefault
                          '@type':
                            const:
                            - schema:PropertyValueSpecification
                          schema:valueName:
                            const: finePolishingConditionsDefault
                          schema:name:
                            const: Fine Polishing Conditions
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
                      - title: Foil Thickness
                        description: 'Target thickness of the electron-transparent
                          TEM lamella after final FIB polishing, in nanometres. Actual
                          thickness may differ from target. Typical range: 50-150
                          nm for standard TEM/STEM; 200-600 nm for XANES or tomography
                          sections.'
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/semFibsemTAPP/foilThicknessDefault
                          '@type':
                            const:
                            - schema:PropertyValueSpecification
                          schema:valueName:
                            const: foilThicknessDefault
                          schema:name:
                            const: Foil Thickness
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
                      - title: Lift-out Method
                        description: Method used to transfer the FIB-prepared lamella
                          to the TEM support grid. In-situ lift-out uses a micromanipulator
                          inside the FIB-SEM chamber and is the standard method for
                          small or precious specimens.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/semFibsemTAPP/liftOutMethod
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/semFibsemTAPP/liftOutMethod
                          schema:name:
                            const: Lift-out Method
                          schema:value:
                            type: string
                        required:
                        - '@id'
                        - '@type'
                        - schema:propertyID
                        - schema:name
                        - schema:value
                        readOnly: true
                      - title: Slice Thickness
                        description: Thickness of each FIB-milled slice during serial
                          sectioning in nanometres. Controls the Z-axis resolution
                          of the 3D reconstruction.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/semFibsemTAPP/sliceThicknessDefault
                          '@type':
                            const:
                            - schema:PropertyValueSpecification
                          schema:valueName:
                            const: sliceThicknessDefault
                          schema:name:
                            const: Slice Thickness
                          ada:dataType:
                            const: number
                          ada:fieldScope:
                            const: session
                          schema:readonlyValue:
                            const: false
                          ada:tier:
                            const: R
                          schema:unitText:
                            const: nm
                        required:
                        - '@id'
                        - '@type'
                        - schema:valueName
                        - schema:name
                        - ada:dataType
                        - ada:fieldScope
                    allOf:
                    - contains:
                        title: Fine Polishing Conditions
                        description: Ion beam voltage and current for final thinning
                          and surface polishing of the TEM lamella. Low-voltage polishing
                          (2 kV or below) minimises Ga implantation depth, surface
                          amorphisation, and curtaining artifacts.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/semFibsemTAPP/finePolishingConditionsDefault
                          '@type':
                            const:
                            - schema:PropertyValueSpecification
                          schema:valueName:
                            const: finePolishingConditionsDefault
                          schema:name:
                            const: Fine Polishing Conditions
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
                        title: Foil Thickness
                        description: 'Target thickness of the electron-transparent
                          TEM lamella after final FIB polishing, in nanometres. Actual
                          thickness may differ from target. Typical range: 50-150
                          nm for standard TEM/STEM; 200-600 nm for XANES or tomography
                          sections.'
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/semFibsemTAPP/foilThicknessDefault
                          '@type':
                            const:
                            - schema:PropertyValueSpecification
                          schema:valueName:
                            const: foilThicknessDefault
                          schema:name:
                            const: Foil Thickness
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
                        title: Lift-out Method
                        description: Method used to transfer the FIB-prepared lamella
                          to the TEM support grid. In-situ lift-out uses a micromanipulator
                          inside the FIB-SEM chamber and is the standard method for
                          small or precious specimens.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/semFibsemTAPP/liftOutMethod
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/semFibsemTAPP/liftOutMethod
                          schema:name:
                            const: Lift-out Method
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
                        title: Slice Thickness
                        description: Thickness of each FIB-milled slice during serial
                          sectioning in nanometres. Controls the Z-axis resolution
                          of the 3D reconstruction.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/semFibsemTAPP/sliceThicknessDefault
                          '@type':
                            const:
                            - schema:PropertyValueSpecification
                          schema:valueName:
                            const: sliceThicknessDefault
                          schema:name:
                            const: Slice Thickness
                          ada:dataType:
                            const: number
                          ada:fieldScope:
                            const: session
                          schema:readonlyValue:
                            const: false
                          ada:tier:
                            const: R
                          schema:unitText:
                            const: nm
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
                    description: Ion beam voltage and current used to mill each slice
                      during FIB-SEM serial sectioning. These parameters determine
                      material removal rate per slice and exposed surface quality.
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
                      $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Procedure_constantsReferenceValues
                    allOf:
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
                  const: Ion milling
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
        - if:
            properties:
              schema:additionalType:
                contains:
                  const: FIBSEM
                schema:inDefinedTermSet: ada:vocab/instrumentType
            required:
            - schema:additionalType
          then:
            properties:
              schema:hasPart:
                type: array
                items:
                  type: object
                  allOf:
                  - if:
                      properties:
                        schema:additionalType:
                          contains:
                            const: Ion Beam Source
                          schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                      required:
                      - schema:additionalType
                    then:
                      properties:
                        schema:name:
                          description: Ion beam source type in a FIB-SEM dual-beam
                            system. Gallium LMIS (Ga+) is the most common ion source;
                            xenon plasma FIB (PFIB) provides higher material removal
                            rates for large-volume milling; helium and neon ion microscopes
                            (GFIS) provide nanometre-resolution imaging and low-damage
                            milling.
                          anyOf:
                          - type: string
                            enum:
                            - Gallium LMIS (Ga+)
                            - Xenon plasma FIB (PFIB)
                            - Helium GFIS
                            - Neon GFIS
                            - N/A
                            - None
                            - missing
                            readOnly: true
                          - type: array
                            items:
                              type: string
                              enum:
                              - Gallium LMIS (Ga+)
                              - Xenon plasma FIB (PFIB)
                              - Helium GFIS
                              - Neon GFIS
                              - N/A
                              - None
                              - missing
                              readOnly: true
                allOf:
                - contains:
                    properties:
                      schema:additionalType:
                        contains:
                          const: Ion Beam Source
                        schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                    required:
                    - schema:additionalType
      allOf:
      - contains:
          properties:
            schema:additionalType:
              contains:
                const: SEM
              schema:inDefinedTermSet: ada:vocab/instrumentType
          required:
          - schema:additionalType
      - contains:
          properties:
            schema:additionalType:
              contains:
                const: FIBSEM
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
                  const: ada:analyteColumn/semFibsemTAPP/beamCurrent
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
                  const: ada:analyteColumn/semFibsemTAPP/beamCurrent
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
    ada:imageRegistration3DDefault:
      description: Method used to align consecutive SEM image slices in the 3D stack
        to correct for drift, vibration, and curtaining artifacts. Include software
        used.
      type: string
    ada:segmentationMethod3DDefault:
      description: Method and software used to segment phases and features in the
        aligned 3D image stack, transforming the grayscale stack into labelled 3D
        regions (pores, mineral phases, grain boundaries, organic matter).
      type: string
    ada:analyticalMode:
      type: array
      items:
        type: string
        enum:
        - TEM Sample Preparation
        - 3D Tomography
  required:
  - ada:dwellTimePerPixelDefault
  - ada:imageRegistration3DDefault
  - ada:segmentationMethod3DDefault

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-FIBSEM/tapp/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-FIBSEM/tapp/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-FIBSEM/tapp/context.jsonld)

## Sources

* [SEM_FIBSEM_TAPP_v4.xlsx (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/SEM-FIBSEM/tapp`

