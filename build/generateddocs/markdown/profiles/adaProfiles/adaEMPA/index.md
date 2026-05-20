
# ADA EMPA Profile (Schema)

`ogch.profiles.adaProfiles.adaEMPA` *v0.1*

Technique-specific profile for Electron Microprobe Analysis (EMPA) products

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# ADA EMPA Profile

Technique-specific metadata profile for Electron Microprobe Analysis (EMPA) products in the Astromat Data Archive. EMPA uses focused electron beams to determine chemical composition of small volumes of solid materials through characteristic X-ray emission.

## Product Types
- **EMPA Image** - Backscattered electron or secondary electron images
- **EMPA Collection** - Sets of EMPA images or maps
- **EMPA QEA** - Quantitative elemental analysis tabular data
- **EMPA SPC** - Spectral data from electron microprobe

## Valid Component Types
- `ada:EMPAImageMap` - Image maps with spectrometer and signal detail (empa_detail)
- `ada:EMPAImage` - Individual EMPA images
- `ada:EMPAQEATabular` - Quantitative elemental analysis tables (empa_detail)
- `ada:EMPAImageCollection` - Collections of EMPA images
- `ada:analysisLocation` - Supplemental analysis location images
- `ada:supplementaryImage` - Supplementary visual materials
- `ada:calibrationFile` - Calibration documents
- `ada:methodDescription` - Method description documents
- `ada:instrumentMetadata` - Instrument metadata documents

## Detail Type
`empa_detail` with properties: `spectrometersUsed`, `signalUsed`

## Examples

### EMPA Product Example
Hand-authored synthetic example with all properties populated. Mock data
for validation and testing.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://cdif.org/0.1/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "prov": "http://www.w3.org/ns/prov#",
    "spdx": "http://spdx.org/rdf/terms#",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "dcterms": "http://purl.org/dc/terms/",
    "geosparql": "http://www.opengis.net/ont/geosparql#",
    "ex": "https://example.org/",
    "dcat": "http://www.w3.org/ns/dcat#"
  },
  "@id": "ex:adaEMPA-example-001",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "EMPA Analysis of Meteorite ALH 84001 Fragment",
  "schema:description": "Example Electron Microprobe Analysis (EMPA) product metadata demonstrating all properties defined by the adaEMPA profile. Contains mock data for testing and validation.",
  "schema:additionalType": [
    "Electron Microprobe Analysis Image (EMPA)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.99999/adaempa-example-001",
    "schema:url": "https://doi.org/10.99999/adaempa-example-001"
  },
  "schema:url": "https://astromat.org/products/adaempa-example-001",
  "schema:dateModified": "2026-01-15",
  "schema:version": "1.0",
  "schema:conditionsOfAccess": [
    "Unrestricted access for research purposes"
  ],
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:creativeWorkStatus": "Published",
  "schema:keywords": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Electron Microprobe Analysis Image",
      "schema:termCode": "EMPA",
      "schema:inDefinedTermSet": "https://ada.astromat.org/vocabulary/techniques",
      "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/EMPA"
    },
    "meteorite",
    "astromaterials"
  ],
  "schema:creator": {
    "@list": [
      {
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Analytica, Maria",
        "schema:identifier": "https://orcid.org/0000-0001-2345-6789",
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "Lunar and Planetary Institute"
        },
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "analytica@example.org"
        }
      },
      {
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Researcher, John Q.",
        "schema:identifier": "https://orcid.org/0000-0002-9876-5432",
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "NASA Johnson Space Center"
        },
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "researcher@example.org"
        }
      }
    ]
  },
  "schema:contributor": [
    {
      "@type": [
        "schema:Role"
      ],
      "schema:roleName": "principalInvestigator",
      "schema:contributor": {
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Leadscientist, Patricia",
        "schema:identifier": "https://orcid.org/0000-0003-1111-2222",
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "leadscientist@example.org"
        }
      }
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "award number",
        "schema:value": "NNX17AE48G"
      },
      "schema:name": "Astromaterials Curation and Analysis",
      "schema:funder": {
        "@type": [
          "schema:Organization"
        ],
        "schema:additionalType": [
          "schema:FundingAgency"
        ],
        "schema:name": "NASA - National Aeronautics and Space Administration"
      }
    }
  ],
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Electron Microprobe Analysis (EMPA)",
    "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/EMPA"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-empa-20260110-001",
      "schema:startDate": "2026-01-10T09:30:00",
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": [
            "nxs:BaseClass/NXinstrument",
            "ada:EMPAInstrument"
          ],
          "schema:name": "Example EMPA Instrument",
          "schema:identifier": [
            "ex:instrument-empa-001"
          ]
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Analytical Sciences Laboratory",
        "schema:identifier": "https://ror.org/00hx57361",
        "schema:additionalType": [
          "nxs:BaseClass/NXsource"
        ]
      },
      "schema:object": [
        {
          "@type": [
            "schema:Thing",
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalType": [
            "MaterialSample"
          ],
          "schema:name": "ALH 84001,123",
          "schema:identifier": [
            "igsn:10.60471/GSEEXAMPLE001"
          ],
          "schema:description": "Thin section of Allan Hills 84001 martian meteorite"
        }
      ]
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "ex:adaEMPA-var-001",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "measurement_value",
      "schema:alternateName": [
        "EMPA primary measurement"
      ],
      "schema:description": "Primary measured quantity from Electron Microprobe Analysis (EMPA) analysis. This is example mock data for testing.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/variables/empa_primary"
      ],
      "schema:unitText": "counts",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "counts",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-var-002",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "position_x",
      "schema:alternateName": [
        "X coordinate"
      ],
      "schema:description": "Horizontal position coordinate on sample surface.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/variables/position_x"
      ],
      "schema:unitText": "micrometer",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "DimensionComponent",
      "cdi:simpleUnitOfMeasure": "um",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#float"
      ]
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "adaEMPA-ALH84001-archive.zip",
      "schema:description": "Archive containing EMPA data files and supplementary materials",
      "schema:contentUrl": "https://astromat.org/downloads/adaempa-example-001.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2"
      },
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 15728640,
        "schema:unitText": "byte"
      },
      "schema:provider": [
        {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "Astromat Data Archive"
        }
      ],
      "schema:hasPart": [
        {
          "@id": "ex:adaEMPA-file-001",
          "@type": [
            "schema:MediaObject",
            "ada:imageMap",
            "schema:ImageObject"
          ],
          "schema:name": "ALH84001_EMPA_001.tif",
          "schema:description": "EMPA data file for ALH 84001 thin section",
          "schema:additionalType": [
            "ada:EMPAImageMap"
          ],
          "schema:encodingFormat": [
            "image/tiff"
          ],
          "schema:size": {
            "@type": [
              "schema:QuantitativeValue"
            ],
            "schema:value": 10485760,
            "schema:unitText": "byte"
          },
          "spdx:checksum": {
            "@type": [
              "spdx:Checksum"
            ],
            "spdx:algorithm": "MD5",
            "spdx:checksumValue": "d41d8cd98f00b204e9800998ecf8427e"
          },
          "ada:componentType": "ada:EMPAImageMap"
        },
        {
          "@id": "ex:adaEMPA-file-002",
          "@type": [
            "schema:MediaObject",
            "ada:document",
            "schema:DigitalDocument"
          ],
          "schema:name": "ALH84001_EMPA_methods.pdf",
          "schema:description": "Method description document for this analysis",
          "schema:additionalType": [
            "ada:methodDescription"
          ],
          "schema:encodingFormat": [
            "application/pdf"
          ],
          "schema:size": {
            "@type": [
              "schema:QuantitativeValue"
            ],
            "schema:value": 524288,
            "schema:unitText": "byte"
          },
          "ada:componentType": "ada:methodDescription"
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:adaEMPA-metadata-001",
    "schema:about": {
      "@id": "ex:adaEMPA-example-001"
    },
    "schema:dateModified": "2026-01-15",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaEMPA"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaProduct"
      }
    ],
    "schema:maintainer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Astromat Data Archive"
    },
    "schema:sdDatePublished": "2026-01-15T12:00:00Z",
    "schema:includedInDataCatalog": {
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:name": "Astromat Data Archive",
      "schema:url": "https://astromat.org"
    }
  }
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
      "prov": "http://www.w3.org/ns/prov#",
      "dcterms": "http://purl.org/dc/terms/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/profiles/adaProfiles/adaEMPA/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://cdif.org/0.1/",
      "csvw": "http://www.w3.org/ns/csvw#",
      "prov": "http://www.w3.org/ns/prov#",
      "spdx": "http://spdx.org/rdf/terms#",
      "nxs": "http://purl.org/nexusformat/definitions/",
      "dcterms": "http://purl.org/dc/terms/",
      "geosparql": "http://www.opengis.net/ont/geosparql#",
      "ex": "https://example.org/",
      "dcat": "http://www.w3.org/ns/dcat#"
    }
  ],
  "@id": "ex:adaEMPA-example-001",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "EMPA Analysis of Meteorite ALH 84001 Fragment",
  "schema:description": "Example Electron Microprobe Analysis (EMPA) product metadata demonstrating all properties defined by the adaEMPA profile. Contains mock data for testing and validation.",
  "schema:additionalType": [
    "Electron Microprobe Analysis Image (EMPA)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.99999/adaempa-example-001",
    "schema:url": "https://doi.org/10.99999/adaempa-example-001"
  },
  "schema:url": "https://astromat.org/products/adaempa-example-001",
  "schema:dateModified": "2026-01-15",
  "schema:version": "1.0",
  "schema:conditionsOfAccess": [
    "Unrestricted access for research purposes"
  ],
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:creativeWorkStatus": "Published",
  "schema:keywords": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Electron Microprobe Analysis Image",
      "schema:termCode": "EMPA",
      "schema:inDefinedTermSet": "https://ada.astromat.org/vocabulary/techniques",
      "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/EMPA"
    },
    "meteorite",
    "astromaterials"
  ],
  "schema:creator": {
    "@list": [
      {
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Analytica, Maria",
        "schema:identifier": "https://orcid.org/0000-0001-2345-6789",
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "Lunar and Planetary Institute"
        },
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "analytica@example.org"
        }
      },
      {
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Researcher, John Q.",
        "schema:identifier": "https://orcid.org/0000-0002-9876-5432",
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "NASA Johnson Space Center"
        },
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "researcher@example.org"
        }
      }
    ]
  },
  "schema:contributor": [
    {
      "@type": [
        "schema:Role"
      ],
      "schema:roleName": "principalInvestigator",
      "schema:contributor": {
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Leadscientist, Patricia",
        "schema:identifier": "https://orcid.org/0000-0003-1111-2222",
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "leadscientist@example.org"
        }
      }
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "award number",
        "schema:value": "NNX17AE48G"
      },
      "schema:name": "Astromaterials Curation and Analysis",
      "schema:funder": {
        "@type": [
          "schema:Organization"
        ],
        "schema:additionalType": [
          "schema:FundingAgency"
        ],
        "schema:name": "NASA - National Aeronautics and Space Administration"
      }
    }
  ],
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Electron Microprobe Analysis (EMPA)",
    "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/EMPA"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-empa-20260110-001",
      "schema:startDate": "2026-01-10T09:30:00",
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": [
            "nxs:BaseClass/NXinstrument",
            "ada:EMPAInstrument"
          ],
          "schema:name": "Example EMPA Instrument",
          "schema:identifier": [
            "ex:instrument-empa-001"
          ]
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Analytical Sciences Laboratory",
        "schema:identifier": "https://ror.org/00hx57361",
        "schema:additionalType": [
          "nxs:BaseClass/NXsource"
        ]
      },
      "schema:object": [
        {
          "@type": [
            "schema:Thing",
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalType": [
            "MaterialSample"
          ],
          "schema:name": "ALH 84001,123",
          "schema:identifier": [
            "igsn:10.60471/GSEEXAMPLE001"
          ],
          "schema:description": "Thin section of Allan Hills 84001 martian meteorite"
        }
      ]
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "ex:adaEMPA-var-001",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "measurement_value",
      "schema:alternateName": [
        "EMPA primary measurement"
      ],
      "schema:description": "Primary measured quantity from Electron Microprobe Analysis (EMPA) analysis. This is example mock data for testing.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/variables/empa_primary"
      ],
      "schema:unitText": "counts",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "counts",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-var-002",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "position_x",
      "schema:alternateName": [
        "X coordinate"
      ],
      "schema:description": "Horizontal position coordinate on sample surface.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/variables/position_x"
      ],
      "schema:unitText": "micrometer",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "DimensionComponent",
      "cdi:simpleUnitOfMeasure": "um",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#float"
      ]
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "adaEMPA-ALH84001-archive.zip",
      "schema:description": "Archive containing EMPA data files and supplementary materials",
      "schema:contentUrl": "https://astromat.org/downloads/adaempa-example-001.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2"
      },
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 15728640,
        "schema:unitText": "byte"
      },
      "schema:provider": [
        {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "Astromat Data Archive"
        }
      ],
      "schema:hasPart": [
        {
          "@id": "ex:adaEMPA-file-001",
          "@type": [
            "schema:MediaObject",
            "ada:imageMap",
            "schema:ImageObject"
          ],
          "schema:name": "ALH84001_EMPA_001.tif",
          "schema:description": "EMPA data file for ALH 84001 thin section",
          "schema:additionalType": [
            "ada:EMPAImageMap"
          ],
          "schema:encodingFormat": [
            "image/tiff"
          ],
          "schema:size": {
            "@type": [
              "schema:QuantitativeValue"
            ],
            "schema:value": 10485760,
            "schema:unitText": "byte"
          },
          "spdx:checksum": {
            "@type": [
              "spdx:Checksum"
            ],
            "spdx:algorithm": "MD5",
            "spdx:checksumValue": "d41d8cd98f00b204e9800998ecf8427e"
          },
          "ada:componentType": "ada:EMPAImageMap"
        },
        {
          "@id": "ex:adaEMPA-file-002",
          "@type": [
            "schema:MediaObject",
            "ada:document",
            "schema:DigitalDocument"
          ],
          "schema:name": "ALH84001_EMPA_methods.pdf",
          "schema:description": "Method description document for this analysis",
          "schema:additionalType": [
            "ada:methodDescription"
          ],
          "schema:encodingFormat": [
            "application/pdf"
          ],
          "schema:size": {
            "@type": [
              "schema:QuantitativeValue"
            ],
            "schema:value": 524288,
            "schema:unitText": "byte"
          },
          "ada:componentType": "ada:methodDescription"
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:adaEMPA-metadata-001",
    "schema:about": {
      "@id": "ex:adaEMPA-example-001"
    },
    "schema:dateModified": "2026-01-15",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaEMPA"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaProduct"
      }
    ],
    "schema:maintainer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Astromat Data Archive"
    },
    "schema:sdDatePublished": "2026-01-15T12:00:00Z",
    "schema:includedInDataCatalog": {
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:name": "Astromat Data Archive",
      "schema:url": "https://astromat.org"
    }
  }
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://cdif.org/0.1/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema1: <http://schema.org/> .
@prefix spdx: <http://spdx.org/rdf/terms#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:adaEMPA-example-001 a schema1:Dataset,
        schema1:Product ;
    schema1:additionalType "Electron Microprobe Analysis Image (EMPA)",
        "ada:DataDeliveryPackage" ;
    schema1:conditionsOfAccess "Unrestricted access for research purposes" ;
    schema1:contributor [ a schema1:Role ;
            schema1:contributor [ a schema1:Person ;
                    schema1:contactPoint [ a schema1:ContactPoint ;
                            schema1:email "leadscientist@example.org" ] ;
                    schema1:identifier "https://orcid.org/0000-0003-1111-2222" ;
                    schema1:name "Leadscientist, Patricia" ] ;
            schema1:roleName "principalInvestigator" ] ;
    schema1:creativeWorkStatus "Published" ;
    schema1:creator ( [ a schema1:Person ;
                schema1:affiliation [ a schema1:Organization ;
                        schema1:name "Lunar and Planetary Institute" ] ;
                schema1:contactPoint [ a schema1:ContactPoint ;
                        schema1:email "analytica@example.org" ] ;
                schema1:identifier "https://orcid.org/0000-0001-2345-6789" ;
                schema1:name "Analytica, Maria" ] [ a schema1:Person ;
                schema1:affiliation [ a schema1:Organization ;
                        schema1:name "NASA Johnson Space Center" ] ;
                schema1:contactPoint [ a schema1:ContactPoint ;
                        schema1:email "researcher@example.org" ] ;
                schema1:identifier "https://orcid.org/0000-0002-9876-5432" ;
                schema1:name "Researcher, John Q." ] ) ;
    schema1:dateModified "2026-01-15" ;
    schema1:description "Example Electron Microprobe Analysis (EMPA) product metadata demonstrating all properties defined by the adaEMPA profile. Contains mock data for testing and validation." ;
    schema1:distribution [ a schema1:DataDownload ;
            schema1:contentUrl "https://astromat.org/downloads/adaempa-example-001.zip" ;
            schema1:description "Archive containing EMPA data files and supplementary materials" ;
            schema1:encodingFormat "application/zip" ;
            schema1:hasPart ex:adaEMPA-file-001,
                ex:adaEMPA-file-002 ;
            schema1:name "adaEMPA-ALH84001-archive.zip" ;
            schema1:provider [ a schema1:Organization ;
                    schema1:name "Astromat Data Archive" ] ;
            schema1:size [ a schema1:QuantitativeValue ;
                    schema1:unitText "byte" ;
                    schema1:value 15728640 ] ;
            spdx:checksum [ a spdx:Checksum ;
                    spdx:algorithm "SHA256" ;
                    spdx:checksumValue "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2" ] ] ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:funder [ a schema1:Organization ;
                    schema1:additionalType "schema:FundingAgency" ;
                    schema1:name "NASA - National Aeronautics and Space Administration" ] ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:propertyID "award number" ;
                    schema1:value "NNX17AE48G" ] ;
            schema1:name "Astromaterials Curation and Analysis" ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://registry.identifiers.org/registry/doi" ;
            schema1:url "https://doi.org/10.99999/adaempa-example-001" ;
            schema1:value "10.99999/adaempa-example-001" ] ;
    schema1:keywords [ a schema1:DefinedTerm ;
            schema1:identifier "https://ada.astromat.org/vocabulary/techniques/EMPA" ;
            schema1:inDefinedTermSet "https://ada.astromat.org/vocabulary/techniques" ;
            schema1:name "Electron Microprobe Analysis Image" ;
            schema1:termCode "EMPA" ],
        "astromaterials",
        "meteorite" ;
    schema1:license "https://creativecommons.org/licenses/by/4.0/" ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:identifier "https://ada.astromat.org/vocabulary/techniques/EMPA" ;
            schema1:name "Electron Microprobe Analysis (EMPA)" ] ;
    schema1:name "EMPA Analysis of Meteorite ALH 84001 Fragment" ;
    schema1:subjectOf ex:adaEMPA-metadata-001 ;
    schema1:url "https://astromat.org/products/adaempa-example-001" ;
    schema1:variableMeasured ex:adaEMPA-var-001,
        ex:adaEMPA-var-002 ;
    schema1:version "1.0" ;
    prov:wasGeneratedBy [ a schema1:Action,
                prov:Activity ;
            schema1:identifier "session-empa-20260110-001" ;
            schema1:location [ a schema1:Place ;
                    schema1:additionalType "nxs:BaseClass/NXsource" ;
                    schema1:identifier "https://ror.org/00hx57361" ;
                    schema1:name "Analytical Sciences Laboratory" ] ;
            schema1:object [ a schema1:Thing,
                        <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalType "MaterialSample" ;
                    schema1:description "Thin section of Allan Hills 84001 martian meteorite" ;
                    schema1:identifier "igsn:10.60471/GSEEXAMPLE001" ;
                    schema1:name "ALH 84001,123" ] ;
            schema1:startDate "2026-01-10T09:30:00" ;
            prov:used [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType "ada:EMPAInstrument",
                        "nxs:BaseClass/NXinstrument" ;
                    schema1:identifier "ex:instrument-empa-001" ;
                    schema1:name "Example EMPA Instrument" ] ] .

ex:adaEMPA-file-001 a schema1:ImageObject,
        schema1:MediaObject,
        ada:imageMap ;
    schema1:additionalType "ada:EMPAImageMap" ;
    schema1:description "EMPA data file for ALH 84001 thin section" ;
    schema1:encodingFormat "image/tiff" ;
    schema1:name "ALH84001_EMPA_001.tif" ;
    schema1:size [ a schema1:QuantitativeValue ;
            schema1:unitText "byte" ;
            schema1:value 10485760 ] ;
    spdx:checksum [ a spdx:Checksum ;
            spdx:algorithm "MD5" ;
            spdx:checksumValue "d41d8cd98f00b204e9800998ecf8427e" ] ;
    ada:componentType "ada:EMPAImageMap" .

ex:adaEMPA-file-002 a schema1:DigitalDocument,
        schema1:MediaObject,
        ada:document ;
    schema1:additionalType "ada:methodDescription" ;
    schema1:description "Method description document for this analysis" ;
    schema1:encodingFormat "application/pdf" ;
    schema1:name "ALH84001_EMPA_methods.pdf" ;
    schema1:size [ a schema1:QuantitativeValue ;
            schema1:unitText "byte" ;
            schema1:value 524288 ] ;
    ada:componentType "ada:methodDescription" .

ex:adaEMPA-metadata-001 a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.0>,
        <https://w3id.org/cdif/data_description/1.0>,
        <https://w3id.org/cdif/discovery/1.0>,
        <https://w3id.org/cdif/manifest/1.0>,
        <https://w3id.org/cdif/provenance/1.0>,
        <https://w3id.org/geochem/metadata/profiles/adaEMPA>,
        <https://w3id.org/geochem/metadata/profiles/adaProduct> ;
    schema1:about ex:adaEMPA-example-001 ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:dateModified "2026-01-15" ;
    schema1:includedInDataCatalog [ a schema1:DataCatalog ;
            schema1:name "Astromat Data Archive" ;
            schema1:url "https://astromat.org" ] ;
    schema1:maintainer [ a schema1:Organization ;
            schema1:name "Astromat Data Archive" ] ;
    schema1:sdDatePublished "2026-01-15T12:00:00Z" .

ex:adaEMPA-var-001 a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "counts" ;
    schema1:alternateName "EMPA primary measurement" ;
    schema1:description "Primary measured quantity from Electron Microprobe Analysis (EMPA) analysis. This is example mock data for testing." ;
    schema1:name "measurement_value" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/variables/empa_primary" ;
    schema1:unitText "counts" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-var-002 a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "DimensionComponent" ;
    cdi:simpleUnitOfMeasure "um" ;
    schema1:alternateName "X coordinate" ;
    schema1:description "Horizontal position coordinate on sample surface." ;
    schema1:name "position_x" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/variables/position_x" ;
    schema1:unitText "micrometer" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#float" .


```


### EMPA Bundle — All Six componentTypes
Hand-authored synthetic example of an EMPA ZIP bundle distribution with
one hasPart per EMPA-specific ada:componentType (EMPAImageMap, EMPAImage,
EMPAQEATabular, EMPAImageCollection, EMPAESPCTabular, EMPAESPCPlot).
Exercises the componentType-nested detailEMPA pattern (spectrometersUsed,
signalUsed) on parts whose underlying file-shape schemas wire detailEMPA.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://cdif.org/0.1/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "prov": "http://www.w3.org/ns/prov#",
    "spdx": "http://spdx.org/rdf/terms#",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "dcterms": "http://purl.org/dc/terms/",
    "geosparql": "http://www.opengis.net/ont/geosparql#",
    "ex": "https://example.org/",
    "dcat": "http://www.w3.org/ns/dcat#"
  },
  "@id": "ex:adaEMPA-bundle-example-001",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "EMPA Bundle of ALH 84001 Fragment — Full Analytical Package",
  "schema:description": "Example Electron Microprobe Analysis (EMPA) product metadata demonstrating a bundled distribution that packages all six EMPA-specific ada:componentType values together: elemental image map, backscattered-electron image, quantitative elemental-abundance table, image collection, X-ray spectrum table, and rendered X-ray spectrum plot. Mock data for testing and validation.",
  "schema:additionalType": [
    "Electron Microprobe Analysis (EMPA) Collection",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.99999/adaempa-bundle-example-001",
    "schema:url": "https://doi.org/10.99999/adaempa-bundle-example-001"
  },
  "schema:url": "https://astromat.org/products/adaempa-bundle-example-001",
  "schema:dateModified": "2026-04-24",
  "schema:datePublished": "2026-04-20",
  "schema:version": "1.0",
  "schema:inLanguage": "en",
  "schema:conditionsOfAccess": [
    "Unrestricted access for research purposes"
  ],
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:creativeWorkStatus": "Published",
  "schema:keywords": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Electron Microprobe Analysis",
      "schema:termCode": "EMPA",
      "schema:inDefinedTermSet": "https://ada.astromat.org/vocabulary/techniques",
      "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/EMPA"
    },
    "meteorite",
    "astromaterials",
    "pyroxene",
    "olivine"
  ],
  "schema:creator": {
    "@list": [
      {
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Analytica, Maria",
        "schema:identifier": "https://orcid.org/0000-0001-2345-6789",
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "Lunar and Planetary Institute"
        },
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "analytica@example.org"
        }
      },
      {
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Researcher, John Q.",
        "schema:identifier": "https://orcid.org/0000-0002-9876-5432",
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "NASA Johnson Space Center"
        },
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "researcher@example.org"
        }
      }
    ]
  },
  "schema:contributor": [
    {
      "@type": [
        "schema:Role"
      ],
      "schema:roleName": "principalInvestigator",
      "schema:contributor": {
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Leadscientist, Patricia",
        "schema:identifier": "https://orcid.org/0000-0003-1111-2222",
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "leadscientist@example.org"
        }
      }
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "award number",
        "schema:value": "NNX17AE48G"
      },
      "schema:name": "Astromaterials Curation and Analysis",
      "schema:funder": {
        "@type": [
          "schema:Organization"
        ],
        "schema:additionalType": [
          "schema:FundingAgency"
        ],
        "schema:name": "NASA - National Aeronautics and Space Administration"
      }
    }
  ],
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Electron Microprobe Analysis (EMPA)",
    "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/EMPA"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-empa-20260110-001",
      "schema:startDate": "2026-01-10T09:30:00",
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": [
            "nxs:BaseClass/NXinstrument",
            "ada:EMPAInstrument"
          ],
          "schema:name": "JEOL JXA-8530F Field Emission Electron Probe Microanalyzer",
          "schema:identifier": [
            "ex:instrument-empa-001"
          ]
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Analytical Sciences Laboratory",
        "schema:identifier": "https://ror.org/00hx57361",
        "schema:additionalType": [
          "nxs:BaseClass/NXsource"
        ]
      },
      "schema:object": [
        {
          "@type": [
            "schema:Thing",
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalType": [
            "MaterialSample"
          ],
          "schema:name": "ALH 84001,123",
          "schema:identifier": [
            "igsn:10.60471/GSEEXAMPLE001"
          ],
          "schema:description": "Thin section of Allan Hills 84001 martian meteorite"
        }
      ]
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "ex:adaEMPA-var-mg",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "MgO_wt_pct",
      "schema:alternateName": [
        "MgO (weight percent)"
      ],
      "schema:description": "Magnesium oxide weight percent derived from electron microprobe analysis with ZAF matrix correction.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/variables/MgO_wt_pct"
      ],
      "schema:unitText": "wt%",
      "schema:minValue": 0,
      "schema:maxValue": 100,
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-var-x",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "position_x",
      "schema:alternateName": [
        "Stage X coordinate"
      ],
      "schema:description": "Horizontal position coordinate on sample surface referenced to stage origin.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/variables/position_x"
      ],
      "schema:unitText": "micrometer",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "DimensionComponent",
      "cdi:simpleUnitOfMeasure": "um",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#float"
      ]
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "adaEMPA-ALH84001-bundle.zip",
      "schema:description": "ZIP archive containing all EMPA data products for ALH 84001,123 — image map, backscattered image, quantitative tabular data, image collection, X-ray spectrum table, and rendered spectrum plot.",
      "schema:contentUrl": "https://astromat.org/downloads/adaempa-bundle-example-001.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2"
      },
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 52428800,
        "schema:unitText": "byte"
      },
      "schema:provider": [
        {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "Astromat Data Archive"
        }
      ],
      "schema:hasPart": [
        {
          "@id": "ex:adaEMPA-part-imagemap",
          "@type": [
            "schema:MediaObject",
            "ada:imageMap",
            "schema:ImageObject"
          ],
          "schema:name": "ALH84001_Mg_elemental_map.tif",
          "schema:description": "Spatially registered Mg-Kα elemental map acquired by wavelength-dispersive spectrometer.",
          "schema:encodingFormat": [
            "image/tiff"
          ],
          "schema:size": {
            "@type": [
              "schema:QuantitativeValue"
            ],
            "schema:value": 10485760,
            "schema:unitText": "byte"
          },
          "spdx:checksum": {
            "@type": [
              "spdx:Checksum"
            ],
            "spdx:algorithm": "MD5",
            "spdx:checksumValue": "d41d8cd98f00b204e9800998ecf8427e"
          },
          "ada:acquisitionTime": "2026-01-10T09:45:00",
          "ada:numPixelsX": 1024,
          "ada:numPixelsY": 1024,
          "ada:channel1": "Mg Kα",
          "ada:illuminationType": "Electron beam",
          "ada:imageType": "Wavelength-dispersive X-ray intensity map",
          "ada:componentType": "ada:EMPAImageMap",
          "ada:spatialRegistration": {
            "ada:originX": 0,
            "ada:originY": 0,
            "ada:pixelScaleX": 1.5,
            "ada:pixelScaleY": 1.5,
            "ada:pixelUnits": "micrometer",
            "ada:originLocation": "upperLeft",
            "ada:coordDef": "pixel-defined, upperLeftPixel",
            "ada:coordUnits": "micrometer"
          },
          "ada:spectrometersUsed": "WDS #2 (TAP crystal), WDS #3 (PET crystal)",
          "ada:signalUsed": "BSE"
        },
        {
          "@id": "ex:adaEMPA-part-image",
          "@type": [
            "schema:MediaObject",
            "ada:image",
            "schema:ImageObject"
          ],
          "schema:name": "ALH84001_BSE_overview.tif",
          "schema:description": "Backscattered-electron overview image of thin section showing phase contrast.",
          "schema:encodingFormat": [
            "image/tiff"
          ],
          "schema:size": {
            "@type": [
              "schema:QuantitativeValue"
            ],
            "schema:value": 4194304,
            "schema:unitText": "byte"
          },
          "spdx:checksum": {
            "@type": [
              "spdx:Checksum"
            ],
            "spdx:algorithm": "MD5",
            "spdx:checksumValue": "e0aa021e21dddbd6d8cecec71e9cf564"
          },
          "ada:acquisitionTime": "2026-01-10T09:35:00",
          "ada:signalUsed": "BSE",
          "ada:pixelSize": "0.5 micrometer",
          "ada:illuminationType": "Electron beam",
          "ada:imageType": "Backscattered electron atomic-number contrast",
          "ada:componentType": "ada:EMPAImage"
        },
        {
          "@id": "ex:adaEMPA-part-qea",
          "@type": [
            "schema:MediaObject",
            "cdi:TabularTextDataSet",
            "ada:tabularData"
          ],
          "schema:name": "ALH84001_point_analyses.csv",
          "schema:description": "Quantitative elemental abundances for 42 point analyses on pyroxene and olivine grains.",
          "schema:encodingFormat": [
            "text/csv"
          ],
          "schema:size": {
            "@type": [
              "schema:QuantitativeValue"
            ],
            "schema:value": 32768,
            "schema:unitText": "byte"
          },
          "spdx:checksum": {
            "@type": [
              "spdx:Checksum"
            ],
            "spdx:algorithm": "MD5",
            "spdx:checksumValue": "7d793037a0760186574b0282f2f435e7"
          },
          "ada:xCoordCol": "position_x_um",
          "ada:yCoordCol": "position_y_um",
          "ada:coordUnits": "micrometer",
          "ada:componentType": "ada:EMPAQEATabular",
          "cdi:isDelimited": true,
          "ada:spectrometersUsed": "WDS #1 (LiF crystal), WDS #2 (TAP crystal), WDS #3 (PET crystal), WDS #4 (LDE1), WDS #5 (LDE2)",
          "ada:signalUsed": "Characteristic X-rays: Si Kα, Ti Kα, Al Kα, Fe Kα, Mn Kα, Mg Kα, Ca Kα, Na Kα, K Kα, Cr Kα",
          "cdif:hasPhysicalMapping": [
            {
              "cdif:index": 0,
              "cdif:physicalDataType": "String",
              "cdi:nullSequence": "NA"
            }
          ]
        },
        {
          "@id": "ex:adaEMPA-part-imagecollection",
          "@type": [
            "schema:MediaObject",
            "ada:collection",
            "https://schema.org/Collection"
          ],
          "schema:name": "ALH84001_element_maps/",
          "schema:description": "Collection of per-element wavelength-dispersive X-ray intensity maps (Mg, Ca, Fe, Si, Al).",
          "schema:encodingFormat": [
            "image/tiff"
          ],
          "schema:size": {
            "@type": [
              "schema:QuantitativeValue"
            ],
            "schema:value": 26214400,
            "schema:unitText": "byte"
          },
          "ada:componentType": "ada:EMPAImageCollection",
          "ada:memberTypes": [
            "ada:EMPAImageMap"
          ],
          "ada:nFiles": 5,
          "ada:filelist": [
            {
              "ada:fileNamePattern": "ALH84001_*_map.tif",
              "ada:componentType": "ada:EMPAImageMap",
              "schema:encodingFormat": "image/tiff"
            }
          ]
        },
        {
          "@id": "ex:adaEMPA-part-espctable",
          "@type": [
            "schema:MediaObject",
            "cdi:TabularTextDataSet",
            "ada:tabularData"
          ],
          "schema:name": "ALH84001_xray_spectrum.csv",
          "schema:description": "Energy-dispersive X-ray spectrum channel counts (energy, counts) from a representative pyroxene point.",
          "schema:encodingFormat": [
            "text/csv"
          ],
          "schema:size": {
            "@type": [
              "schema:QuantitativeValue"
            ],
            "schema:value": 16384,
            "schema:unitText": "byte"
          },
          "spdx:checksum": {
            "@type": [
              "spdx:Checksum"
            ],
            "spdx:algorithm": "MD5",
            "spdx:checksumValue": "3b0c44298fc1c149afbf4c8996fb9242"
          },
          "ada:componentType": "ada:EMPAESPCTabular",
          "cdi:isDelimited": true,
          "ada:spectrometersUsed": "Energy-dispersive Si(Li) detector",
          "ada:signalUsed": "Full X-ray spectrum, 0–20 keV, 10 eV channel width",
          "cdif:hasPhysicalMapping": [
            {
              "cdif:index": 0,
              "cdif:physicalDataType": "String",
              "cdi:nullSequence": "NA"
            }
          ]
        },
        {
          "@id": "ex:adaEMPA-part-espcplot",
          "@type": [
            "schema:MediaObject",
            "ada:image",
            "schema:ImageObject"
          ],
          "schema:name": "ALH84001_xray_spectrum_plot.png",
          "schema:description": "Rendered plot of the energy-dispersive X-ray spectrum shown above, annotated with characteristic peak labels.",
          "schema:encodingFormat": [
            "image/png"
          ],
          "schema:size": {
            "@type": [
              "schema:QuantitativeValue"
            ],
            "schema:value": 262144,
            "schema:unitText": "byte"
          },
          "spdx:checksum": {
            "@type": [
              "spdx:Checksum"
            ],
            "spdx:algorithm": "MD5",
            "spdx:checksumValue": "5ebe2294ecd0e0f08eab7690d2a6ee69"
          },
          "schema:relatedLink": [
            {
              "@type": [
                "schema:LinkRole"
              ],
              "schema:linkRelationship": "rendering-of",
              "schema:target": {
                "@type": [
                  "schema:EntryPoint"
                ],
                "schema:encodingFormat": "text/csv",
                "schema:name": "ALH84001_xray_spectrum.csv"
              }
            }
          ],
          "ada:imageType": "Annotated line plot of X-ray spectrum",
          "ada:componentType": "ada:EMPAESPCPlot"
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:adaEMPA-bundle-metadata-001",
    "schema:about": {
      "@id": "ex:adaEMPA-bundle-example-001"
    },
    "schema:dateModified": "2026-04-24",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaEMPA"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaProduct"
      }
    ],
    "schema:maintainer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Astromat Data Archive"
    },
    "schema:sdDatePublished": "2026-04-24T12:00:00Z",
    "schema:includedInDataCatalog": {
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:name": "Astromat Data Archive",
      "schema:url": "https://astromat.org"
    }
  }
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
      "prov": "http://www.w3.org/ns/prov#",
      "dcterms": "http://purl.org/dc/terms/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/profiles/adaProfiles/adaEMPA/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://cdif.org/0.1/",
      "csvw": "http://www.w3.org/ns/csvw#",
      "prov": "http://www.w3.org/ns/prov#",
      "spdx": "http://spdx.org/rdf/terms#",
      "nxs": "http://purl.org/nexusformat/definitions/",
      "dcterms": "http://purl.org/dc/terms/",
      "geosparql": "http://www.opengis.net/ont/geosparql#",
      "ex": "https://example.org/",
      "dcat": "http://www.w3.org/ns/dcat#"
    }
  ],
  "@id": "ex:adaEMPA-bundle-example-001",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "EMPA Bundle of ALH 84001 Fragment \u2014 Full Analytical Package",
  "schema:description": "Example Electron Microprobe Analysis (EMPA) product metadata demonstrating a bundled distribution that packages all six EMPA-specific ada:componentType values together: elemental image map, backscattered-electron image, quantitative elemental-abundance table, image collection, X-ray spectrum table, and rendered X-ray spectrum plot. Mock data for testing and validation.",
  "schema:additionalType": [
    "Electron Microprobe Analysis (EMPA) Collection",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.99999/adaempa-bundle-example-001",
    "schema:url": "https://doi.org/10.99999/adaempa-bundle-example-001"
  },
  "schema:url": "https://astromat.org/products/adaempa-bundle-example-001",
  "schema:dateModified": "2026-04-24",
  "schema:datePublished": "2026-04-20",
  "schema:version": "1.0",
  "schema:inLanguage": "en",
  "schema:conditionsOfAccess": [
    "Unrestricted access for research purposes"
  ],
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:creativeWorkStatus": "Published",
  "schema:keywords": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Electron Microprobe Analysis",
      "schema:termCode": "EMPA",
      "schema:inDefinedTermSet": "https://ada.astromat.org/vocabulary/techniques",
      "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/EMPA"
    },
    "meteorite",
    "astromaterials",
    "pyroxene",
    "olivine"
  ],
  "schema:creator": {
    "@list": [
      {
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Analytica, Maria",
        "schema:identifier": "https://orcid.org/0000-0001-2345-6789",
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "Lunar and Planetary Institute"
        },
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "analytica@example.org"
        }
      },
      {
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Researcher, John Q.",
        "schema:identifier": "https://orcid.org/0000-0002-9876-5432",
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "NASA Johnson Space Center"
        },
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "researcher@example.org"
        }
      }
    ]
  },
  "schema:contributor": [
    {
      "@type": [
        "schema:Role"
      ],
      "schema:roleName": "principalInvestigator",
      "schema:contributor": {
        "@type": [
          "schema:Person"
        ],
        "schema:name": "Leadscientist, Patricia",
        "schema:identifier": "https://orcid.org/0000-0003-1111-2222",
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "leadscientist@example.org"
        }
      }
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:identifier": {
        "@type": [
          "schema:PropertyValue"
        ],
        "schema:propertyID": "award number",
        "schema:value": "NNX17AE48G"
      },
      "schema:name": "Astromaterials Curation and Analysis",
      "schema:funder": {
        "@type": [
          "schema:Organization"
        ],
        "schema:additionalType": [
          "schema:FundingAgency"
        ],
        "schema:name": "NASA - National Aeronautics and Space Administration"
      }
    }
  ],
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Electron Microprobe Analysis (EMPA)",
    "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/EMPA"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-empa-20260110-001",
      "schema:startDate": "2026-01-10T09:30:00",
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": [
            "nxs:BaseClass/NXinstrument",
            "ada:EMPAInstrument"
          ],
          "schema:name": "JEOL JXA-8530F Field Emission Electron Probe Microanalyzer",
          "schema:identifier": [
            "ex:instrument-empa-001"
          ]
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Analytical Sciences Laboratory",
        "schema:identifier": "https://ror.org/00hx57361",
        "schema:additionalType": [
          "nxs:BaseClass/NXsource"
        ]
      },
      "schema:object": [
        {
          "@type": [
            "schema:Thing",
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalType": [
            "MaterialSample"
          ],
          "schema:name": "ALH 84001,123",
          "schema:identifier": [
            "igsn:10.60471/GSEEXAMPLE001"
          ],
          "schema:description": "Thin section of Allan Hills 84001 martian meteorite"
        }
      ]
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "ex:adaEMPA-var-mg",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "MgO_wt_pct",
      "schema:alternateName": [
        "MgO (weight percent)"
      ],
      "schema:description": "Magnesium oxide weight percent derived from electron microprobe analysis with ZAF matrix correction.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/variables/MgO_wt_pct"
      ],
      "schema:unitText": "wt%",
      "schema:minValue": 0,
      "schema:maxValue": 100,
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-var-x",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "position_x",
      "schema:alternateName": [
        "Stage X coordinate"
      ],
      "schema:description": "Horizontal position coordinate on sample surface referenced to stage origin.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/variables/position_x"
      ],
      "schema:unitText": "micrometer",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "DimensionComponent",
      "cdi:simpleUnitOfMeasure": "um",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#float"
      ]
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "adaEMPA-ALH84001-bundle.zip",
      "schema:description": "ZIP archive containing all EMPA data products for ALH 84001,123 \u2014 image map, backscattered image, quantitative tabular data, image collection, X-ray spectrum table, and rendered spectrum plot.",
      "schema:contentUrl": "https://astromat.org/downloads/adaempa-bundle-example-001.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2"
      },
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 52428800,
        "schema:unitText": "byte"
      },
      "schema:provider": [
        {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "Astromat Data Archive"
        }
      ],
      "schema:hasPart": [
        {
          "@id": "ex:adaEMPA-part-imagemap",
          "@type": [
            "schema:MediaObject",
            "ada:imageMap",
            "schema:ImageObject"
          ],
          "schema:name": "ALH84001_Mg_elemental_map.tif",
          "schema:description": "Spatially registered Mg-K\u03b1 elemental map acquired by wavelength-dispersive spectrometer.",
          "schema:encodingFormat": [
            "image/tiff"
          ],
          "schema:size": {
            "@type": [
              "schema:QuantitativeValue"
            ],
            "schema:value": 10485760,
            "schema:unitText": "byte"
          },
          "spdx:checksum": {
            "@type": [
              "spdx:Checksum"
            ],
            "spdx:algorithm": "MD5",
            "spdx:checksumValue": "d41d8cd98f00b204e9800998ecf8427e"
          },
          "ada:acquisitionTime": "2026-01-10T09:45:00",
          "ada:numPixelsX": 1024,
          "ada:numPixelsY": 1024,
          "ada:channel1": "Mg K\u03b1",
          "ada:illuminationType": "Electron beam",
          "ada:imageType": "Wavelength-dispersive X-ray intensity map",
          "ada:componentType": "ada:EMPAImageMap",
          "ada:spatialRegistration": {
            "ada:originX": 0,
            "ada:originY": 0,
            "ada:pixelScaleX": 1.5,
            "ada:pixelScaleY": 1.5,
            "ada:pixelUnits": "micrometer",
            "ada:originLocation": "upperLeft",
            "ada:coordDef": "pixel-defined, upperLeftPixel",
            "ada:coordUnits": "micrometer"
          },
          "ada:spectrometersUsed": "WDS #2 (TAP crystal), WDS #3 (PET crystal)",
          "ada:signalUsed": "BSE"
        },
        {
          "@id": "ex:adaEMPA-part-image",
          "@type": [
            "schema:MediaObject",
            "ada:image",
            "schema:ImageObject"
          ],
          "schema:name": "ALH84001_BSE_overview.tif",
          "schema:description": "Backscattered-electron overview image of thin section showing phase contrast.",
          "schema:encodingFormat": [
            "image/tiff"
          ],
          "schema:size": {
            "@type": [
              "schema:QuantitativeValue"
            ],
            "schema:value": 4194304,
            "schema:unitText": "byte"
          },
          "spdx:checksum": {
            "@type": [
              "spdx:Checksum"
            ],
            "spdx:algorithm": "MD5",
            "spdx:checksumValue": "e0aa021e21dddbd6d8cecec71e9cf564"
          },
          "ada:acquisitionTime": "2026-01-10T09:35:00",
          "ada:signalUsed": "BSE",
          "ada:pixelSize": "0.5 micrometer",
          "ada:illuminationType": "Electron beam",
          "ada:imageType": "Backscattered electron atomic-number contrast",
          "ada:componentType": "ada:EMPAImage"
        },
        {
          "@id": "ex:adaEMPA-part-qea",
          "@type": [
            "schema:MediaObject",
            "cdi:TabularTextDataSet",
            "ada:tabularData"
          ],
          "schema:name": "ALH84001_point_analyses.csv",
          "schema:description": "Quantitative elemental abundances for 42 point analyses on pyroxene and olivine grains.",
          "schema:encodingFormat": [
            "text/csv"
          ],
          "schema:size": {
            "@type": [
              "schema:QuantitativeValue"
            ],
            "schema:value": 32768,
            "schema:unitText": "byte"
          },
          "spdx:checksum": {
            "@type": [
              "spdx:Checksum"
            ],
            "spdx:algorithm": "MD5",
            "spdx:checksumValue": "7d793037a0760186574b0282f2f435e7"
          },
          "ada:xCoordCol": "position_x_um",
          "ada:yCoordCol": "position_y_um",
          "ada:coordUnits": "micrometer",
          "ada:componentType": "ada:EMPAQEATabular",
          "cdi:isDelimited": true,
          "ada:spectrometersUsed": "WDS #1 (LiF crystal), WDS #2 (TAP crystal), WDS #3 (PET crystal), WDS #4 (LDE1), WDS #5 (LDE2)",
          "ada:signalUsed": "Characteristic X-rays: Si K\u03b1, Ti K\u03b1, Al K\u03b1, Fe K\u03b1, Mn K\u03b1, Mg K\u03b1, Ca K\u03b1, Na K\u03b1, K K\u03b1, Cr K\u03b1",
          "cdif:hasPhysicalMapping": [
            {
              "cdif:index": 0,
              "cdif:physicalDataType": "String",
              "cdi:nullSequence": "NA"
            }
          ]
        },
        {
          "@id": "ex:adaEMPA-part-imagecollection",
          "@type": [
            "schema:MediaObject",
            "ada:collection",
            "https://schema.org/Collection"
          ],
          "schema:name": "ALH84001_element_maps/",
          "schema:description": "Collection of per-element wavelength-dispersive X-ray intensity maps (Mg, Ca, Fe, Si, Al).",
          "schema:encodingFormat": [
            "image/tiff"
          ],
          "schema:size": {
            "@type": [
              "schema:QuantitativeValue"
            ],
            "schema:value": 26214400,
            "schema:unitText": "byte"
          },
          "ada:componentType": "ada:EMPAImageCollection",
          "ada:memberTypes": [
            "ada:EMPAImageMap"
          ],
          "ada:nFiles": 5,
          "ada:filelist": [
            {
              "ada:fileNamePattern": "ALH84001_*_map.tif",
              "ada:componentType": "ada:EMPAImageMap",
              "schema:encodingFormat": "image/tiff"
            }
          ]
        },
        {
          "@id": "ex:adaEMPA-part-espctable",
          "@type": [
            "schema:MediaObject",
            "cdi:TabularTextDataSet",
            "ada:tabularData"
          ],
          "schema:name": "ALH84001_xray_spectrum.csv",
          "schema:description": "Energy-dispersive X-ray spectrum channel counts (energy, counts) from a representative pyroxene point.",
          "schema:encodingFormat": [
            "text/csv"
          ],
          "schema:size": {
            "@type": [
              "schema:QuantitativeValue"
            ],
            "schema:value": 16384,
            "schema:unitText": "byte"
          },
          "spdx:checksum": {
            "@type": [
              "spdx:Checksum"
            ],
            "spdx:algorithm": "MD5",
            "spdx:checksumValue": "3b0c44298fc1c149afbf4c8996fb9242"
          },
          "ada:componentType": "ada:EMPAESPCTabular",
          "cdi:isDelimited": true,
          "ada:spectrometersUsed": "Energy-dispersive Si(Li) detector",
          "ada:signalUsed": "Full X-ray spectrum, 0\u201320 keV, 10 eV channel width",
          "cdif:hasPhysicalMapping": [
            {
              "cdif:index": 0,
              "cdif:physicalDataType": "String",
              "cdi:nullSequence": "NA"
            }
          ]
        },
        {
          "@id": "ex:adaEMPA-part-espcplot",
          "@type": [
            "schema:MediaObject",
            "ada:image",
            "schema:ImageObject"
          ],
          "schema:name": "ALH84001_xray_spectrum_plot.png",
          "schema:description": "Rendered plot of the energy-dispersive X-ray spectrum shown above, annotated with characteristic peak labels.",
          "schema:encodingFormat": [
            "image/png"
          ],
          "schema:size": {
            "@type": [
              "schema:QuantitativeValue"
            ],
            "schema:value": 262144,
            "schema:unitText": "byte"
          },
          "spdx:checksum": {
            "@type": [
              "spdx:Checksum"
            ],
            "spdx:algorithm": "MD5",
            "spdx:checksumValue": "5ebe2294ecd0e0f08eab7690d2a6ee69"
          },
          "schema:relatedLink": [
            {
              "@type": [
                "schema:LinkRole"
              ],
              "schema:linkRelationship": "rendering-of",
              "schema:target": {
                "@type": [
                  "schema:EntryPoint"
                ],
                "schema:encodingFormat": "text/csv",
                "schema:name": "ALH84001_xray_spectrum.csv"
              }
            }
          ],
          "ada:imageType": "Annotated line plot of X-ray spectrum",
          "ada:componentType": "ada:EMPAESPCPlot"
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:adaEMPA-bundle-metadata-001",
    "schema:about": {
      "@id": "ex:adaEMPA-bundle-example-001"
    },
    "schema:dateModified": "2026-04-24",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaEMPA"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaProduct"
      }
    ],
    "schema:maintainer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Astromat Data Archive"
    },
    "schema:sdDatePublished": "2026-04-24T12:00:00Z",
    "schema:includedInDataCatalog": {
      "@type": [
        "schema:DataCatalog"
      ],
      "schema:name": "Astromat Data Archive",
      "schema:url": "https://astromat.org"
    }
  }
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://cdif.org/0.1/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema: <https://schema.org/> .
@prefix schema1: <http://schema.org/> .
@prefix spdx: <http://spdx.org/rdf/terms#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:adaEMPA-bundle-example-001 a schema1:Dataset,
        schema1:Product ;
    schema1:additionalType "Electron Microprobe Analysis (EMPA) Collection",
        "ada:DataDeliveryPackage" ;
    schema1:conditionsOfAccess "Unrestricted access for research purposes" ;
    schema1:contributor [ a schema1:Role ;
            schema1:contributor [ a schema1:Person ;
                    schema1:contactPoint [ a schema1:ContactPoint ;
                            schema1:email "leadscientist@example.org" ] ;
                    schema1:identifier "https://orcid.org/0000-0003-1111-2222" ;
                    schema1:name "Leadscientist, Patricia" ] ;
            schema1:roleName "principalInvestigator" ] ;
    schema1:creativeWorkStatus "Published" ;
    schema1:creator ( [ a schema1:Person ;
                schema1:affiliation [ a schema1:Organization ;
                        schema1:name "Lunar and Planetary Institute" ] ;
                schema1:contactPoint [ a schema1:ContactPoint ;
                        schema1:email "analytica@example.org" ] ;
                schema1:identifier "https://orcid.org/0000-0001-2345-6789" ;
                schema1:name "Analytica, Maria" ] [ a schema1:Person ;
                schema1:affiliation [ a schema1:Organization ;
                        schema1:name "NASA Johnson Space Center" ] ;
                schema1:contactPoint [ a schema1:ContactPoint ;
                        schema1:email "researcher@example.org" ] ;
                schema1:identifier "https://orcid.org/0000-0002-9876-5432" ;
                schema1:name "Researcher, John Q." ] ) ;
    schema1:dateModified "2026-04-24" ;
    schema1:datePublished "2026-04-20" ;
    schema1:description "Example Electron Microprobe Analysis (EMPA) product metadata demonstrating a bundled distribution that packages all six EMPA-specific ada:componentType values together: elemental image map, backscattered-electron image, quantitative elemental-abundance table, image collection, X-ray spectrum table, and rendered X-ray spectrum plot. Mock data for testing and validation." ;
    schema1:distribution [ a schema1:DataDownload ;
            schema1:contentUrl "https://astromat.org/downloads/adaempa-bundle-example-001.zip" ;
            schema1:description "ZIP archive containing all EMPA data products for ALH 84001,123 — image map, backscattered image, quantitative tabular data, image collection, X-ray spectrum table, and rendered spectrum plot." ;
            schema1:encodingFormat "application/zip" ;
            schema1:hasPart ex:adaEMPA-part-espcplot,
                ex:adaEMPA-part-espctable,
                ex:adaEMPA-part-image,
                ex:adaEMPA-part-imagecollection,
                ex:adaEMPA-part-imagemap,
                ex:adaEMPA-part-qea ;
            schema1:name "adaEMPA-ALH84001-bundle.zip" ;
            schema1:provider [ a schema1:Organization ;
                    schema1:name "Astromat Data Archive" ] ;
            schema1:size [ a schema1:QuantitativeValue ;
                    schema1:unitText "byte" ;
                    schema1:value 52428800 ] ;
            spdx:checksum [ a spdx:Checksum ;
                    spdx:algorithm "SHA256" ;
                    spdx:checksumValue "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2" ] ] ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:funder [ a schema1:Organization ;
                    schema1:additionalType "schema:FundingAgency" ;
                    schema1:name "NASA - National Aeronautics and Space Administration" ] ;
            schema1:identifier [ a schema1:PropertyValue ;
                    schema1:propertyID "award number" ;
                    schema1:value "NNX17AE48G" ] ;
            schema1:name "Astromaterials Curation and Analysis" ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://registry.identifiers.org/registry/doi" ;
            schema1:url "https://doi.org/10.99999/adaempa-bundle-example-001" ;
            schema1:value "10.99999/adaempa-bundle-example-001" ] ;
    schema1:inLanguage "en" ;
    schema1:keywords [ a schema1:DefinedTerm ;
            schema1:identifier "https://ada.astromat.org/vocabulary/techniques/EMPA" ;
            schema1:inDefinedTermSet "https://ada.astromat.org/vocabulary/techniques" ;
            schema1:name "Electron Microprobe Analysis" ;
            schema1:termCode "EMPA" ],
        "astromaterials",
        "meteorite",
        "olivine",
        "pyroxene" ;
    schema1:license "https://creativecommons.org/licenses/by/4.0/" ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:identifier "https://ada.astromat.org/vocabulary/techniques/EMPA" ;
            schema1:name "Electron Microprobe Analysis (EMPA)" ] ;
    schema1:name "EMPA Bundle of ALH 84001 Fragment — Full Analytical Package" ;
    schema1:subjectOf ex:adaEMPA-bundle-metadata-001 ;
    schema1:url "https://astromat.org/products/adaempa-bundle-example-001" ;
    schema1:variableMeasured ex:adaEMPA-var-mg,
        ex:adaEMPA-var-x ;
    schema1:version "1.0" ;
    prov:wasGeneratedBy [ a schema1:Action,
                prov:Activity ;
            schema1:identifier "session-empa-20260110-001" ;
            schema1:location [ a schema1:Place ;
                    schema1:additionalType "nxs:BaseClass/NXsource" ;
                    schema1:identifier "https://ror.org/00hx57361" ;
                    schema1:name "Analytical Sciences Laboratory" ] ;
            schema1:object [ a schema1:Thing,
                        <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalType "MaterialSample" ;
                    schema1:description "Thin section of Allan Hills 84001 martian meteorite" ;
                    schema1:identifier "igsn:10.60471/GSEEXAMPLE001" ;
                    schema1:name "ALH 84001,123" ] ;
            schema1:startDate "2026-01-10T09:30:00" ;
            prov:used [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType "ada:EMPAInstrument",
                        "nxs:BaseClass/NXinstrument" ;
                    schema1:identifier "ex:instrument-empa-001" ;
                    schema1:name "JEOL JXA-8530F Field Emission Electron Probe Microanalyzer" ] ] .

ex:adaEMPA-bundle-metadata-001 a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.0>,
        <https://w3id.org/cdif/data_description/1.0>,
        <https://w3id.org/cdif/discovery/1.0>,
        <https://w3id.org/cdif/manifest/1.0>,
        <https://w3id.org/cdif/provenance/1.0>,
        <https://w3id.org/geochem/metadata/profiles/adaEMPA>,
        <https://w3id.org/geochem/metadata/profiles/adaProduct> ;
    schema1:about ex:adaEMPA-bundle-example-001 ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:dateModified "2026-04-24" ;
    schema1:includedInDataCatalog [ a schema1:DataCatalog ;
            schema1:name "Astromat Data Archive" ;
            schema1:url "https://astromat.org" ] ;
    schema1:maintainer [ a schema1:Organization ;
            schema1:name "Astromat Data Archive" ] ;
    schema1:sdDatePublished "2026-04-24T12:00:00Z" .

ex:adaEMPA-part-espcplot a schema1:ImageObject,
        schema1:MediaObject,
        ada:image ;
    schema1:description "Rendered plot of the energy-dispersive X-ray spectrum shown above, annotated with characteristic peak labels." ;
    schema1:encodingFormat "image/png" ;
    schema1:name "ALH84001_xray_spectrum_plot.png" ;
    schema1:relatedLink [ a schema1:LinkRole ;
            schema1:linkRelationship "rendering-of" ;
            schema1:target [ a schema1:EntryPoint ;
                    schema1:encodingFormat "text/csv" ;
                    schema1:name "ALH84001_xray_spectrum.csv" ] ] ;
    schema1:size [ a schema1:QuantitativeValue ;
            schema1:unitText "byte" ;
            schema1:value 262144 ] ;
    spdx:checksum [ a spdx:Checksum ;
            spdx:algorithm "MD5" ;
            spdx:checksumValue "5ebe2294ecd0e0f08eab7690d2a6ee69" ] ;
    ada:componentType "ada:EMPAESPCPlot" ;
    ada:imageType "Annotated line plot of X-ray spectrum" .

ex:adaEMPA-part-espctable a cdi:TabularTextDataSet,
        schema1:MediaObject,
        ada:tabularData ;
    cdi:isDelimited true ;
    schema1:description "Energy-dispersive X-ray spectrum channel counts (energy, counts) from a representative pyroxene point." ;
    schema1:encodingFormat "text/csv" ;
    schema1:name "ALH84001_xray_spectrum.csv" ;
    schema1:size [ a schema1:QuantitativeValue ;
            schema1:unitText "byte" ;
            schema1:value 16384 ] ;
    spdx:checksum [ a spdx:Checksum ;
            spdx:algorithm "MD5" ;
            spdx:checksumValue "3b0c44298fc1c149afbf4c8996fb9242" ] ;
    ada:componentType "ada:EMPAESPCTabular" ;
    ada:signalUsed "Full X-ray spectrum, 0–20 keV, 10 eV channel width" ;
    ada:spectrometersUsed "Energy-dispersive Si(Li) detector" ;
    cdif:hasPhysicalMapping [ cdi:nullSequence "NA" ;
            cdif:index 0 ;
            cdif:physicalDataType "String" ] .

ex:adaEMPA-part-image a schema1:ImageObject,
        schema1:MediaObject,
        ada:image ;
    schema1:description "Backscattered-electron overview image of thin section showing phase contrast." ;
    schema1:encodingFormat "image/tiff" ;
    schema1:name "ALH84001_BSE_overview.tif" ;
    schema1:size [ a schema1:QuantitativeValue ;
            schema1:unitText "byte" ;
            schema1:value 4194304 ] ;
    spdx:checksum [ a spdx:Checksum ;
            spdx:algorithm "MD5" ;
            spdx:checksumValue "e0aa021e21dddbd6d8cecec71e9cf564" ] ;
    ada:acquisitionTime "2026-01-10T09:35:00" ;
    ada:componentType "ada:EMPAImage" ;
    ada:illuminationType "Electron beam" ;
    ada:imageType "Backscattered electron atomic-number contrast" ;
    ada:pixelSize "0.5 micrometer" ;
    ada:signalUsed "BSE" .

ex:adaEMPA-part-imagecollection a schema1:MediaObject,
        ada:collection,
        schema:Collection ;
    schema1:description "Collection of per-element wavelength-dispersive X-ray intensity maps (Mg, Ca, Fe, Si, Al)." ;
    schema1:encodingFormat "image/tiff" ;
    schema1:name "ALH84001_element_maps/" ;
    schema1:size [ a schema1:QuantitativeValue ;
            schema1:unitText "byte" ;
            schema1:value 26214400 ] ;
    ada:componentType "ada:EMPAImageCollection" ;
    ada:filelist [ schema1:encodingFormat "image/tiff" ;
            ada:componentType "ada:EMPAImageMap" ;
            ada:fileNamePattern "ALH84001_*_map.tif" ] ;
    ada:memberTypes "ada:EMPAImageMap" ;
    ada:nFiles 5 .

ex:adaEMPA-part-imagemap a schema1:ImageObject,
        schema1:MediaObject,
        ada:imageMap ;
    schema1:description "Spatially registered Mg-Kα elemental map acquired by wavelength-dispersive spectrometer." ;
    schema1:encodingFormat "image/tiff" ;
    schema1:name "ALH84001_Mg_elemental_map.tif" ;
    schema1:size [ a schema1:QuantitativeValue ;
            schema1:unitText "byte" ;
            schema1:value 10485760 ] ;
    spdx:checksum [ a spdx:Checksum ;
            spdx:algorithm "MD5" ;
            spdx:checksumValue "d41d8cd98f00b204e9800998ecf8427e" ] ;
    ada:acquisitionTime "2026-01-10T09:45:00" ;
    ada:channel1 "Mg Kα" ;
    ada:componentType "ada:EMPAImageMap" ;
    ada:illuminationType "Electron beam" ;
    ada:imageType "Wavelength-dispersive X-ray intensity map" ;
    ada:numPixelsX 1024 ;
    ada:numPixelsY 1024 ;
    ada:signalUsed "BSE" ;
    ada:spatialRegistration [ ada:coordDef "pixel-defined, upperLeftPixel" ;
            ada:coordUnits "micrometer" ;
            ada:originLocation "upperLeft" ;
            ada:originX 0 ;
            ada:originY 0 ;
            ada:pixelScaleX 1.5e+00 ;
            ada:pixelScaleY 1.5e+00 ;
            ada:pixelUnits "micrometer" ] ;
    ada:spectrometersUsed "WDS #2 (TAP crystal), WDS #3 (PET crystal)" .

ex:adaEMPA-part-qea a cdi:TabularTextDataSet,
        schema1:MediaObject,
        ada:tabularData ;
    cdi:isDelimited true ;
    schema1:description "Quantitative elemental abundances for 42 point analyses on pyroxene and olivine grains." ;
    schema1:encodingFormat "text/csv" ;
    schema1:name "ALH84001_point_analyses.csv" ;
    schema1:size [ a schema1:QuantitativeValue ;
            schema1:unitText "byte" ;
            schema1:value 32768 ] ;
    spdx:checksum [ a spdx:Checksum ;
            spdx:algorithm "MD5" ;
            spdx:checksumValue "7d793037a0760186574b0282f2f435e7" ] ;
    ada:componentType "ada:EMPAQEATabular" ;
    ada:coordUnits "micrometer" ;
    ada:signalUsed "Characteristic X-rays: Si Kα, Ti Kα, Al Kα, Fe Kα, Mn Kα, Mg Kα, Ca Kα, Na Kα, K Kα, Cr Kα" ;
    ada:spectrometersUsed "WDS #1 (LiF crystal), WDS #2 (TAP crystal), WDS #3 (PET crystal), WDS #4 (LDE1), WDS #5 (LDE2)" ;
    ada:xCoordCol "position_x_um" ;
    ada:yCoordCol "position_y_um" ;
    cdif:hasPhysicalMapping [ cdi:nullSequence "NA" ;
            cdif:index 0 ;
            cdif:physicalDataType "String" ] .

ex:adaEMPA-var-mg a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:alternateName "MgO (weight percent)" ;
    schema1:description "Magnesium oxide weight percent derived from electron microprobe analysis with ZAF matrix correction." ;
    schema1:maxValue 100 ;
    schema1:minValue 0 ;
    schema1:name "MgO_wt_pct" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/variables/MgO_wt_pct" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-var-x a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "DimensionComponent" ;
    cdi:simpleUnitOfMeasure "um" ;
    schema1:alternateName "Stage X coordinate" ;
    schema1:description "Horizontal position coordinate on sample surface referenced to stage origin." ;
    schema1:name "position_x" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/variables/position_x" ;
    schema1:unitText "micrometer" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#float" .


```


### adaEMPA — P0 (Richard & Deng 2026 (synthetic comprehensive WDS example))
Auto-generated adaEMPA dataset record for publication P0.
schema:variableMeasured is derived from the empaTAPP TAPP definition's
ada:defaultAnalytes; schema:hasPart carries the paired detailEMPA fields
and references the TAPP via schema:measurementTechnique. Synthetic
placeholders are used for DOI, file size, and dates.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://cdif.org/0.1/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "prov": "http://www.w3.org/ns/prov#",
    "spdx": "http://spdx.org/rdf/terms#",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "dcterms": "http://purl.org/dc/terms/",
    "ex": "https://example.org/",
    "dcat": "http://www.w3.org/ns/dcat#"
  },
  "@id": "ex:adaEMPA-P0",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "adaEMPA dataset for P0 (Richard & Deng 2026 (synthetic comprehensive WDS example))",
  "schema:description": "Auto-generated adaEMPA profile-level Dataset for publication P0: Richard & Deng 2026 (synthetic comprehensive WDS example). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p0); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes.",
  "schema:additionalType": [
    "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.PLACEHOLDER/adaempa-p0"
  },
  "schema:url": "https://astromat.org/products/adaempa-p0",
  "schema:dateModified": "2026-04-29",
  "schema:version": "0.1",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:creativeWorkStatus": "Draft",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Electron Microprobe Analysis (EMPA)",
    "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/EMPA"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-empa-p0",
      "schema:startDate": "2026-04-29",
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": [
            "nxs:BaseClass/NXinstrument",
            "ada:EMPAInstrument"
          ],
          "schema:name": "Cameca SXFiveFE",
          "schema:identifier": [
            "ex:instrument-empa-001"
          ],
          "schema:manufacturer": {
            "@type": [
              "schema:Organization"
            ],
            "schema:name": "Cameca"
          }
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "IEDA| Columbia University",
        "schema:additionalType": [
          "nxs:BaseClass/NXsource"
        ]
      },
      "schema:object": [
        {
          "@type": [
            "schema:Thing",
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalType": [
            "MaterialSample"
          ],
          "schema:name": "Sample analyzed in P0",
          "schema:identifier": [
            "igsn:10.60471/PLACEHOLDER-P0"
          ],
          "schema:description": "Sample of: Feldspar"
        }
      ]
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "ex:adaEMPA-P0-var-Si",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Si",
      "schema:description": "Si abundance measured by EMPA WDS (20 s peak counting; 10 s background counting).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Si"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P0-var-Al",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Al",
      "schema:description": "Al abundance measured by EMPA WDS (20 s peak counting; 10 s background counting).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Al"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P0-var-K",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "K",
      "schema:description": "K abundance measured by EMPA WDS (20 s peak counting; 10 s background counting).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/K"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P0-var-Ca",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Ca",
      "schema:description": "Ca abundance measured by EMPA WDS (20 s peak counting; 10 s background counting).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Ca"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P0-var-Na",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Na",
      "schema:description": "Na abundance measured by EMPA WDS (30 s peak counting; 10 s background counting).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Na"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P0-var-Fe",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Fe",
      "schema:description": "Fe abundance measured by EMPA WDS (20 s peak counting; 10 s background counting).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Fe"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P0-var-Mg",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Mg",
      "schema:description": "Mg abundance measured by EMPA WDS (20 s peak counting; 10 s background counting).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Mg"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P0-var-Ti",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Ti",
      "schema:description": "Ti abundance measured by EMPA WDS (60 s peak counting; 10 s background counting).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Ti"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P0-var-Cr",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Cr",
      "schema:description": "Cr abundance measured by EMPA WDS (60 s peak counting; 10 s background counting).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Cr"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P0-var-Mn",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Mn",
      "schema:description": "Mn abundance measured by EMPA WDS (60 s peak counting; 10 s background counting).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Mn"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "adaEMPA-P0-archive.zip",
      "schema:description": "Archive containing tabular EMPA data for P0.",
      "schema:contentUrl": "https://astromat.org/downloads/adaempa-p0.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "0000000000000000000000000000000000000000000000000000000000000000"
      },
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 1048576,
        "schema:unitText": "byte"
      },
      "schema:hasPart": [
        {
          "@id": "ex:adaEMPA-P0-data-001",
          "@type": [
            "schema:MediaObject",
            "ada:tabularData",
            "cdi:TabularTextDataSet",
            "schema:Thing"
          ],
          "schema:name": "adaEMPA-P0-data.csv",
          "schema:description": "Per-point quantitative EMPA analyses (Richard & Deng 2026 (synthetic comprehensive WDS example)).",
          "schema:additionalType": [
            "ada:EMPAQEATabular"
          ],
          "schema:encodingFormat": [
            "text/csv"
          ],
          "cdi:isDelimited": true,
          "cdi:isFixedWidth": false,
          "csvw:delimiter": ",",
          "csvw:header": true,
          "ada:componentType": "ada:EMPAQEATabular",
          "ada:spectrometersUsed": "5x WDS",
          "ada:signalUsed": "Kα x-ray lines",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-p0"
          },
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/empaTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/acceleratingVoltage",
              "schema:name": "Default Accelerating Voltage",
              "schema:value": 20,
              "schema:unitText": "kV"
            },
            {
              "@id": "ada:parameter/empaTAPP/beamDiameter",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/beamDiameter",
              "schema:name": "Default Beam Diameter",
              "schema:value": 5,
              "schema:unitText": "µm"
            },
            {
              "@id": "ada:parameter/empaTAPP/BeamRasterDimension",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/BeamRasterDimension",
              "schema:name": "Beam Raster Dimensions",
              "schema:value": "10 by 10",
              "schema:unitText": "µm × µm"
            },
            {
              "@id": "ada:parameter/empaTAPP/reportedAnalyte",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/reportedAnalyte",
              "schema:name": "Target Element",
              "schema:value": "Si|Al|K|Ca|Na|Fe|Mg|Ti|Cr|Mn"
            }
          ],
          "cdif:hasPhysicalMapping": [
            {
              "cdif:index": 0,
              "cdif:physicalDataType": "String",
              "cdi:nullSequence": "NA"
            }
          ]
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:adaEMPA-P0-metadata",
    "schema:about": {
      "@id": "ex:adaEMPA-P0"
    },
    "schema:dateModified": "2026-04-29",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaEMPA"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaProduct"
      }
    ],
    "schema:maintainer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Astromat Data Archive"
    },
    "schema:sdDatePublished": "2026-04-29T12:00:00Z"
  }
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
      "csvw": "http://www.w3.org/ns/csvw#",
      "prov": "http://www.w3.org/ns/prov#",
      "dcterms": "http://purl.org/dc/terms/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/profiles/adaProfiles/adaEMPA/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://cdif.org/0.1/",
      "csvw": "http://www.w3.org/ns/csvw#",
      "prov": "http://www.w3.org/ns/prov#",
      "spdx": "http://spdx.org/rdf/terms#",
      "nxs": "http://purl.org/nexusformat/definitions/",
      "dcterms": "http://purl.org/dc/terms/",
      "ex": "https://example.org/",
      "dcat": "http://www.w3.org/ns/dcat#"
    }
  ],
  "@id": "ex:adaEMPA-P0",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "adaEMPA dataset for P0 (Richard & Deng 2026 (synthetic comprehensive WDS example))",
  "schema:description": "Auto-generated adaEMPA profile-level Dataset for publication P0: Richard & Deng 2026 (synthetic comprehensive WDS example). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p0); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes.",
  "schema:additionalType": [
    "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.PLACEHOLDER/adaempa-p0"
  },
  "schema:url": "https://astromat.org/products/adaempa-p0",
  "schema:dateModified": "2026-04-29",
  "schema:version": "0.1",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:creativeWorkStatus": "Draft",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Electron Microprobe Analysis (EMPA)",
    "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/EMPA"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-empa-p0",
      "schema:startDate": "2026-04-29",
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": [
            "nxs:BaseClass/NXinstrument",
            "ada:EMPAInstrument"
          ],
          "schema:name": "Cameca SXFiveFE",
          "schema:identifier": [
            "ex:instrument-empa-001"
          ],
          "schema:manufacturer": {
            "@type": [
              "schema:Organization"
            ],
            "schema:name": "Cameca"
          }
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "IEDA| Columbia University",
        "schema:additionalType": [
          "nxs:BaseClass/NXsource"
        ]
      },
      "schema:object": [
        {
          "@type": [
            "schema:Thing",
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalType": [
            "MaterialSample"
          ],
          "schema:name": "Sample analyzed in P0",
          "schema:identifier": [
            "igsn:10.60471/PLACEHOLDER-P0"
          ],
          "schema:description": "Sample of: Feldspar"
        }
      ]
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "ex:adaEMPA-P0-var-Si",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Si",
      "schema:description": "Si abundance measured by EMPA WDS (20 s peak counting; 10 s background counting).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Si"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P0-var-Al",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Al",
      "schema:description": "Al abundance measured by EMPA WDS (20 s peak counting; 10 s background counting).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Al"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P0-var-K",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "K",
      "schema:description": "K abundance measured by EMPA WDS (20 s peak counting; 10 s background counting).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/K"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P0-var-Ca",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Ca",
      "schema:description": "Ca abundance measured by EMPA WDS (20 s peak counting; 10 s background counting).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Ca"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P0-var-Na",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Na",
      "schema:description": "Na abundance measured by EMPA WDS (30 s peak counting; 10 s background counting).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Na"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P0-var-Fe",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Fe",
      "schema:description": "Fe abundance measured by EMPA WDS (20 s peak counting; 10 s background counting).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Fe"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P0-var-Mg",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Mg",
      "schema:description": "Mg abundance measured by EMPA WDS (20 s peak counting; 10 s background counting).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Mg"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P0-var-Ti",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Ti",
      "schema:description": "Ti abundance measured by EMPA WDS (60 s peak counting; 10 s background counting).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Ti"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P0-var-Cr",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Cr",
      "schema:description": "Cr abundance measured by EMPA WDS (60 s peak counting; 10 s background counting).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Cr"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P0-var-Mn",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Mn",
      "schema:description": "Mn abundance measured by EMPA WDS (60 s peak counting; 10 s background counting).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Mn"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "adaEMPA-P0-archive.zip",
      "schema:description": "Archive containing tabular EMPA data for P0.",
      "schema:contentUrl": "https://astromat.org/downloads/adaempa-p0.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "0000000000000000000000000000000000000000000000000000000000000000"
      },
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 1048576,
        "schema:unitText": "byte"
      },
      "schema:hasPart": [
        {
          "@id": "ex:adaEMPA-P0-data-001",
          "@type": [
            "schema:MediaObject",
            "ada:tabularData",
            "cdi:TabularTextDataSet",
            "schema:Thing"
          ],
          "schema:name": "adaEMPA-P0-data.csv",
          "schema:description": "Per-point quantitative EMPA analyses (Richard & Deng 2026 (synthetic comprehensive WDS example)).",
          "schema:additionalType": [
            "ada:EMPAQEATabular"
          ],
          "schema:encodingFormat": [
            "text/csv"
          ],
          "cdi:isDelimited": true,
          "cdi:isFixedWidth": false,
          "csvw:delimiter": ",",
          "csvw:header": true,
          "ada:componentType": "ada:EMPAQEATabular",
          "ada:spectrometersUsed": "5x WDS",
          "ada:signalUsed": "K\u03b1 x-ray lines",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-p0"
          },
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/empaTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/acceleratingVoltage",
              "schema:name": "Default Accelerating Voltage",
              "schema:value": 20,
              "schema:unitText": "kV"
            },
            {
              "@id": "ada:parameter/empaTAPP/beamDiameter",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/beamDiameter",
              "schema:name": "Default Beam Diameter",
              "schema:value": 5,
              "schema:unitText": "\u00b5m"
            },
            {
              "@id": "ada:parameter/empaTAPP/BeamRasterDimension",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/BeamRasterDimension",
              "schema:name": "Beam Raster Dimensions",
              "schema:value": "10 by 10",
              "schema:unitText": "\u00b5m \u00d7 \u00b5m"
            },
            {
              "@id": "ada:parameter/empaTAPP/reportedAnalyte",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/reportedAnalyte",
              "schema:name": "Target Element",
              "schema:value": "Si|Al|K|Ca|Na|Fe|Mg|Ti|Cr|Mn"
            }
          ],
          "cdif:hasPhysicalMapping": [
            {
              "cdif:index": 0,
              "cdif:physicalDataType": "String",
              "cdi:nullSequence": "NA"
            }
          ]
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:adaEMPA-P0-metadata",
    "schema:about": {
      "@id": "ex:adaEMPA-P0"
    },
    "schema:dateModified": "2026-04-29",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaEMPA"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaProduct"
      }
    ],
    "schema:maintainer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Astromat Data Archive"
    },
    "schema:sdDatePublished": "2026-04-29T12:00:00Z"
  }
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://cdif.org/0.1/> .
@prefix csvw: <http://www.w3.org/ns/csvw#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix spdx: <http://spdx.org/rdf/terms#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://ada.astromat.org/metadata/parameter/empaTAPP/BeamRasterDimension> a schema1:PropertyValue ;
    schema1:name "Beam Raster Dimensions" ;
    schema1:propertyID "ada:parameter/empaTAPP/BeamRasterDimension" ;
    schema1:unitText "µm × µm" ;
    schema1:value "10 by 10" .

<https://ada.astromat.org/metadata/parameter/empaTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:name "Default Accelerating Voltage" ;
    schema1:propertyID "ada:parameter/empaTAPP/acceleratingVoltage" ;
    schema1:unitText "kV" ;
    schema1:value 20 .

<https://ada.astromat.org/metadata/parameter/empaTAPP/beamDiameter> a schema1:PropertyValue ;
    schema1:name "Default Beam Diameter" ;
    schema1:propertyID "ada:parameter/empaTAPP/beamDiameter" ;
    schema1:unitText "µm" ;
    schema1:value 5 .

<https://ada.astromat.org/metadata/parameter/empaTAPP/reportedAnalyte> a schema1:PropertyValue ;
    schema1:name "Target Element" ;
    schema1:propertyID "ada:parameter/empaTAPP/reportedAnalyte" ;
    schema1:value "Si|Al|K|Ca|Na|Fe|Mg|Ti|Cr|Mn" .

ex:adaEMPA-P0 a schema1:Dataset,
        schema1:Product ;
    schema1:additionalType "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
        "ada:DataDeliveryPackage" ;
    schema1:creativeWorkStatus "Draft" ;
    schema1:dateModified "2026-04-29" ;
    schema1:description "Auto-generated adaEMPA profile-level Dataset for publication P0: Richard & Deng 2026 (synthetic comprehensive WDS example). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p0); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes." ;
    schema1:distribution [ a schema1:DataDownload ;
            schema1:contentUrl "https://astromat.org/downloads/adaempa-p0.zip" ;
            schema1:description "Archive containing tabular EMPA data for P0." ;
            schema1:encodingFormat "application/zip" ;
            schema1:hasPart ex:adaEMPA-P0-data-001 ;
            schema1:name "adaEMPA-P0-archive.zip" ;
            schema1:size [ a schema1:QuantitativeValue ;
                    schema1:unitText "byte" ;
                    schema1:value 1048576 ] ;
            spdx:checksum [ a spdx:Checksum ;
                    spdx:algorithm "SHA256" ;
                    spdx:checksumValue "0000000000000000000000000000000000000000000000000000000000000000" ] ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://registry.identifiers.org/registry/doi" ;
            schema1:value "10.PLACEHOLDER/adaempa-p0" ] ;
    schema1:license "https://creativecommons.org/licenses/by/4.0/" ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:identifier "https://ada.astromat.org/vocabulary/techniques/EMPA" ;
            schema1:name "Electron Microprobe Analysis (EMPA)" ] ;
    schema1:name "adaEMPA dataset for P0 (Richard & Deng 2026 (synthetic comprehensive WDS example))" ;
    schema1:subjectOf ex:adaEMPA-P0-metadata ;
    schema1:url "https://astromat.org/products/adaempa-p0" ;
    schema1:variableMeasured ex:adaEMPA-P0-var-Al,
        ex:adaEMPA-P0-var-Ca,
        ex:adaEMPA-P0-var-Cr,
        ex:adaEMPA-P0-var-Fe,
        ex:adaEMPA-P0-var-K,
        ex:adaEMPA-P0-var-Mg,
        ex:adaEMPA-P0-var-Mn,
        ex:adaEMPA-P0-var-Na,
        ex:adaEMPA-P0-var-Si,
        ex:adaEMPA-P0-var-Ti ;
    schema1:version "0.1" ;
    prov:wasGeneratedBy [ a schema1:Action,
                prov:Activity ;
            schema1:identifier "session-empa-p0" ;
            schema1:location [ a schema1:Place ;
                    schema1:additionalType "nxs:BaseClass/NXsource" ;
                    schema1:name "IEDA| Columbia University" ] ;
            schema1:object [ a schema1:Thing,
                        <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalType "MaterialSample" ;
                    schema1:description "Sample of: Feldspar" ;
                    schema1:identifier "igsn:10.60471/PLACEHOLDER-P0" ;
                    schema1:name "Sample analyzed in P0" ] ;
            schema1:startDate "2026-04-29" ;
            prov:used [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType "ada:EMPAInstrument",
                        "nxs:BaseClass/NXinstrument" ;
                    schema1:identifier "ex:instrument-empa-001" ;
                    schema1:manufacturer [ a schema1:Organization ;
                            schema1:name "Cameca" ] ;
                    schema1:name "Cameca SXFiveFE" ] ] .

ex:adaEMPA-P0-data-001 a cdi:TabularTextDataSet,
        schema1:MediaObject,
        schema1:Thing,
        ada:tabularData ;
    cdi:isDelimited true ;
    cdi:isFixedWidth false ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/empaTAPP/BeamRasterDimension>,
        <https://ada.astromat.org/metadata/parameter/empaTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/empaTAPP/beamDiameter>,
        <https://ada.astromat.org/metadata/parameter/empaTAPP/reportedAnalyte> ;
    schema1:additionalType "ada:EMPAQEATabular" ;
    schema1:description "Per-point quantitative EMPA analyses (Richard & Deng 2026 (synthetic comprehensive WDS example))." ;
    schema1:encodingFormat "text/csv" ;
    schema1:measurementTechnique ex:empaTAPP-p0 ;
    schema1:name "adaEMPA-P0-data.csv" ;
    csvw:delimiter "," ;
    csvw:header true ;
    ada:componentType "ada:EMPAQEATabular" ;
    ada:signalUsed "Kα x-ray lines" ;
    ada:spectrometersUsed "5x WDS" ;
    cdif:hasPhysicalMapping [ cdi:nullSequence "NA" ;
            cdif:index 0 ;
            cdif:physicalDataType "String" ] .

ex:adaEMPA-P0-metadata a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.0>,
        <https://w3id.org/cdif/data_description/1.0>,
        <https://w3id.org/cdif/discovery/1.0>,
        <https://w3id.org/cdif/manifest/1.0>,
        <https://w3id.org/cdif/provenance/1.0>,
        <https://w3id.org/geochem/metadata/profiles/adaEMPA>,
        <https://w3id.org/geochem/metadata/profiles/adaProduct> ;
    schema1:about ex:adaEMPA-P0 ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:dateModified "2026-04-29" ;
    schema1:maintainer [ a schema1:Organization ;
            schema1:name "Astromat Data Archive" ] ;
    schema1:sdDatePublished "2026-04-29T12:00:00Z" .

ex:adaEMPA-P0-var-Al a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Al abundance measured by EMPA WDS (20 s peak counting; 10 s background counting)." ;
    schema1:name "Al" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Al" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P0-var-Ca a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Ca abundance measured by EMPA WDS (20 s peak counting; 10 s background counting)." ;
    schema1:name "Ca" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Ca" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P0-var-Cr a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Cr abundance measured by EMPA WDS (60 s peak counting; 10 s background counting)." ;
    schema1:name "Cr" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Cr" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P0-var-Fe a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Fe abundance measured by EMPA WDS (20 s peak counting; 10 s background counting)." ;
    schema1:name "Fe" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Fe" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P0-var-K a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "K abundance measured by EMPA WDS (20 s peak counting; 10 s background counting)." ;
    schema1:name "K" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/K" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P0-var-Mg a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Mg abundance measured by EMPA WDS (20 s peak counting; 10 s background counting)." ;
    schema1:name "Mg" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Mg" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P0-var-Mn a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Mn abundance measured by EMPA WDS (60 s peak counting; 10 s background counting)." ;
    schema1:name "Mn" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Mn" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P0-var-Na a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Na abundance measured by EMPA WDS (30 s peak counting; 10 s background counting)." ;
    schema1:name "Na" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Na" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P0-var-Si a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Si abundance measured by EMPA WDS (20 s peak counting; 10 s background counting)." ;
    schema1:name "Si" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Si" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P0-var-Ti a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Ti abundance measured by EMPA WDS (60 s peak counting; 10 s background counting)." ;
    schema1:name "Ti" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Ti" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .


```


### adaEMPA — P1 (Chi et al. 2015 (Tissintite, EPSL))
Auto-generated adaEMPA dataset record for publication P1.
schema:variableMeasured is derived from the empaTAPP TAPP definition's
ada:defaultAnalytes; schema:hasPart carries the paired detailEMPA fields
and references the TAPP via schema:measurementTechnique. Synthetic
placeholders are used for DOI, file size, and dates.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://cdif.org/0.1/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "prov": "http://www.w3.org/ns/prov#",
    "spdx": "http://spdx.org/rdf/terms#",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "dcterms": "http://purl.org/dc/terms/",
    "ex": "https://example.org/",
    "dcat": "http://www.w3.org/ns/dcat#"
  },
  "@id": "ex:adaEMPA-P1",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "adaEMPA dataset for P1 (Chi et al. 2015 (Tissintite, EPSL))",
  "schema:description": "Auto-generated adaEMPA profile-level Dataset for publication P1: Chi et al. 2015 (Tissintite, EPSL). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p1); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes.",
  "schema:additionalType": [
    "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.PLACEHOLDER/adaempa-p1"
  },
  "schema:url": "https://astromat.org/products/adaempa-p1",
  "schema:dateModified": "2026-04-29",
  "schema:version": "0.1",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:creativeWorkStatus": "Draft",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Electron Microprobe Analysis (EMPA)",
    "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/EMPA"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-empa-p1",
      "schema:startDate": "2026-04-29",
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": [
            "nxs:BaseClass/NXinstrument",
            "ada:EMPAInstrument"
          ],
          "schema:name": "JEOL JXA-8200",
          "schema:identifier": [
            "ex:instrument-empa-001"
          ],
          "schema:manufacturer": {
            "@type": [
              "schema:Organization"
            ],
            "schema:name": "JEOL"
          }
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Caltech GPS Division Analytical Facility",
        "schema:additionalType": [
          "nxs:BaseClass/NXsource"
        ]
      },
      "schema:object": [
        {
          "@type": [
            "schema:Thing",
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalType": [
            "MaterialSample"
          ],
          "schema:name": "Sample analyzed in P1",
          "schema:identifier": [
            "igsn:10.60471/PLACEHOLDER-P1"
          ],
          "schema:description": "Sample of: Silicate minerals (tissintite, maskelynite, pigeonite, fayalite)"
        }
      ]
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "ex:adaEMPA-P1-var-Si",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Si",
      "schema:description": "Si abundance measured by EMPA WDS (Kα emission line; 20 s peak counting; 10 s background counting; calibrated against Anorthite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Si"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P1-var-Al",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Al",
      "schema:description": "Al abundance measured by EMPA WDS (Kα emission line; 20 s peak counting; 10 s background counting; calibrated against Anorthite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Al"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P1-var-Ca",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Ca",
      "schema:description": "Ca abundance measured by EMPA WDS (Kα emission line; 20 s peak counting; 10 s background counting; calibrated against Anorthite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Ca"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P1-var-Na",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Na",
      "schema:description": "Na abundance measured by EMPA WDS (Kα emission line; 20 s peak counting; 10 s background counting; calibrated against Albite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Na"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P1-var-Fe",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Fe",
      "schema:description": "Fe abundance measured by EMPA WDS (Kα emission line; 20 s peak counting; 10 s background counting; calibrated against Fayalite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Fe"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P1-var-Mg",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Mg",
      "schema:description": "Mg abundance measured by EMPA WDS (Kα emission line; 20 s peak counting; 10 s background counting; calibrated against Forsterite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Mg"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P1-var-Mn",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Mn",
      "schema:description": "Mn abundance measured by EMPA WDS (Kα emission line; 20 s peak counting; 10 s background counting; calibrated against Mn2SiO4).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Mn"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P1-var-Ti",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Ti",
      "schema:description": "Ti abundance measured by EMPA WDS (Kα emission line; 20 s peak counting; 10 s background counting; calibrated against TiO2).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Ti"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P1-var-Cr",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Cr",
      "schema:description": "Cr abundance measured by EMPA WDS (Kα emission line; 20 s peak counting; 10 s background counting; calibrated against Cr2O3).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Cr"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P1-var-K",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "K",
      "schema:description": "K abundance measured by EMPA WDS (Kα emission line; 20 s peak counting; 10 s background counting; calibrated against Microcline).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/K"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "adaEMPA-P1-archive.zip",
      "schema:description": "Archive containing tabular EMPA data for P1.",
      "schema:contentUrl": "https://astromat.org/downloads/adaempa-p1.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "0000000000000000000000000000000000000000000000000000000000000000"
      },
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 1048576,
        "schema:unitText": "byte"
      },
      "schema:hasPart": [
        {
          "@id": "ex:adaEMPA-P1-data-001",
          "@type": [
            "schema:MediaObject",
            "ada:tabularData",
            "cdi:TabularTextDataSet",
            "schema:Thing"
          ],
          "schema:name": "adaEMPA-P1-data.csv",
          "schema:description": "Per-point quantitative EMPA analyses (Chi et al. 2015 (Tissintite, EPSL)).",
          "schema:additionalType": [
            "ada:EMPAQEATabular"
          ],
          "schema:encodingFormat": [
            "text/csv"
          ],
          "cdi:isDelimited": true,
          "cdi:isFixedWidth": false,
          "csvw:delimiter": ",",
          "csvw:header": true,
          "ada:componentType": "ada:EMPAQEATabular",
          "ada:spectrometersUsed": "5x WDS",
          "ada:signalUsed": "Kα x-ray lines",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-p1"
          },
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/empaTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/acceleratingVoltage",
              "schema:name": "Default Accelerating Voltage",
              "schema:value": 15,
              "schema:unitText": "kV"
            },
            {
              "@id": "ada:parameter/empaTAPP/beamDiameter",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/beamDiameter",
              "schema:name": "Default Beam Diameter",
              "schema:value": "0 (focused)",
              "schema:unitText": "µm"
            },
            {
              "@id": "ada:parameter/empaTAPP/reportedAnalyte",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/reportedAnalyte",
              "schema:name": "Target Element",
              "schema:value": "Si|Al|Ca|Na|Fe|Mg|Mn|Ti|Cr|K"
            }
          ],
          "cdif:hasPhysicalMapping": [
            {
              "cdif:index": 0,
              "cdif:physicalDataType": "String",
              "cdi:nullSequence": "NA"
            }
          ]
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:adaEMPA-P1-metadata",
    "schema:about": {
      "@id": "ex:adaEMPA-P1"
    },
    "schema:dateModified": "2026-04-29",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaEMPA"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaProduct"
      }
    ],
    "schema:maintainer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Astromat Data Archive"
    },
    "schema:sdDatePublished": "2026-04-29T12:00:00Z"
  }
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
      "csvw": "http://www.w3.org/ns/csvw#",
      "prov": "http://www.w3.org/ns/prov#",
      "dcterms": "http://purl.org/dc/terms/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/profiles/adaProfiles/adaEMPA/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://cdif.org/0.1/",
      "csvw": "http://www.w3.org/ns/csvw#",
      "prov": "http://www.w3.org/ns/prov#",
      "spdx": "http://spdx.org/rdf/terms#",
      "nxs": "http://purl.org/nexusformat/definitions/",
      "dcterms": "http://purl.org/dc/terms/",
      "ex": "https://example.org/",
      "dcat": "http://www.w3.org/ns/dcat#"
    }
  ],
  "@id": "ex:adaEMPA-P1",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "adaEMPA dataset for P1 (Chi et al. 2015 (Tissintite, EPSL))",
  "schema:description": "Auto-generated adaEMPA profile-level Dataset for publication P1: Chi et al. 2015 (Tissintite, EPSL). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p1); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes.",
  "schema:additionalType": [
    "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.PLACEHOLDER/adaempa-p1"
  },
  "schema:url": "https://astromat.org/products/adaempa-p1",
  "schema:dateModified": "2026-04-29",
  "schema:version": "0.1",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:creativeWorkStatus": "Draft",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Electron Microprobe Analysis (EMPA)",
    "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/EMPA"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-empa-p1",
      "schema:startDate": "2026-04-29",
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": [
            "nxs:BaseClass/NXinstrument",
            "ada:EMPAInstrument"
          ],
          "schema:name": "JEOL JXA-8200",
          "schema:identifier": [
            "ex:instrument-empa-001"
          ],
          "schema:manufacturer": {
            "@type": [
              "schema:Organization"
            ],
            "schema:name": "JEOL"
          }
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Caltech GPS Division Analytical Facility",
        "schema:additionalType": [
          "nxs:BaseClass/NXsource"
        ]
      },
      "schema:object": [
        {
          "@type": [
            "schema:Thing",
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalType": [
            "MaterialSample"
          ],
          "schema:name": "Sample analyzed in P1",
          "schema:identifier": [
            "igsn:10.60471/PLACEHOLDER-P1"
          ],
          "schema:description": "Sample of: Silicate minerals (tissintite, maskelynite, pigeonite, fayalite)"
        }
      ]
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "ex:adaEMPA-P1-var-Si",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Si",
      "schema:description": "Si abundance measured by EMPA WDS (K\u03b1 emission line; 20 s peak counting; 10 s background counting; calibrated against Anorthite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Si"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P1-var-Al",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Al",
      "schema:description": "Al abundance measured by EMPA WDS (K\u03b1 emission line; 20 s peak counting; 10 s background counting; calibrated against Anorthite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Al"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P1-var-Ca",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Ca",
      "schema:description": "Ca abundance measured by EMPA WDS (K\u03b1 emission line; 20 s peak counting; 10 s background counting; calibrated against Anorthite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Ca"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P1-var-Na",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Na",
      "schema:description": "Na abundance measured by EMPA WDS (K\u03b1 emission line; 20 s peak counting; 10 s background counting; calibrated against Albite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Na"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P1-var-Fe",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Fe",
      "schema:description": "Fe abundance measured by EMPA WDS (K\u03b1 emission line; 20 s peak counting; 10 s background counting; calibrated against Fayalite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Fe"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P1-var-Mg",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Mg",
      "schema:description": "Mg abundance measured by EMPA WDS (K\u03b1 emission line; 20 s peak counting; 10 s background counting; calibrated against Forsterite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Mg"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P1-var-Mn",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Mn",
      "schema:description": "Mn abundance measured by EMPA WDS (K\u03b1 emission line; 20 s peak counting; 10 s background counting; calibrated against Mn2SiO4).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Mn"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P1-var-Ti",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Ti",
      "schema:description": "Ti abundance measured by EMPA WDS (K\u03b1 emission line; 20 s peak counting; 10 s background counting; calibrated against TiO2).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Ti"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P1-var-Cr",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Cr",
      "schema:description": "Cr abundance measured by EMPA WDS (K\u03b1 emission line; 20 s peak counting; 10 s background counting; calibrated against Cr2O3).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Cr"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P1-var-K",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "K",
      "schema:description": "K abundance measured by EMPA WDS (K\u03b1 emission line; 20 s peak counting; 10 s background counting; calibrated against Microcline).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/K"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "adaEMPA-P1-archive.zip",
      "schema:description": "Archive containing tabular EMPA data for P1.",
      "schema:contentUrl": "https://astromat.org/downloads/adaempa-p1.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "0000000000000000000000000000000000000000000000000000000000000000"
      },
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 1048576,
        "schema:unitText": "byte"
      },
      "schema:hasPart": [
        {
          "@id": "ex:adaEMPA-P1-data-001",
          "@type": [
            "schema:MediaObject",
            "ada:tabularData",
            "cdi:TabularTextDataSet",
            "schema:Thing"
          ],
          "schema:name": "adaEMPA-P1-data.csv",
          "schema:description": "Per-point quantitative EMPA analyses (Chi et al. 2015 (Tissintite, EPSL)).",
          "schema:additionalType": [
            "ada:EMPAQEATabular"
          ],
          "schema:encodingFormat": [
            "text/csv"
          ],
          "cdi:isDelimited": true,
          "cdi:isFixedWidth": false,
          "csvw:delimiter": ",",
          "csvw:header": true,
          "ada:componentType": "ada:EMPAQEATabular",
          "ada:spectrometersUsed": "5x WDS",
          "ada:signalUsed": "K\u03b1 x-ray lines",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-p1"
          },
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/empaTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/acceleratingVoltage",
              "schema:name": "Default Accelerating Voltage",
              "schema:value": 15,
              "schema:unitText": "kV"
            },
            {
              "@id": "ada:parameter/empaTAPP/beamDiameter",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/beamDiameter",
              "schema:name": "Default Beam Diameter",
              "schema:value": "0 (focused)",
              "schema:unitText": "\u00b5m"
            },
            {
              "@id": "ada:parameter/empaTAPP/reportedAnalyte",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/reportedAnalyte",
              "schema:name": "Target Element",
              "schema:value": "Si|Al|Ca|Na|Fe|Mg|Mn|Ti|Cr|K"
            }
          ],
          "cdif:hasPhysicalMapping": [
            {
              "cdif:index": 0,
              "cdif:physicalDataType": "String",
              "cdi:nullSequence": "NA"
            }
          ]
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:adaEMPA-P1-metadata",
    "schema:about": {
      "@id": "ex:adaEMPA-P1"
    },
    "schema:dateModified": "2026-04-29",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaEMPA"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaProduct"
      }
    ],
    "schema:maintainer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Astromat Data Archive"
    },
    "schema:sdDatePublished": "2026-04-29T12:00:00Z"
  }
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://cdif.org/0.1/> .
@prefix csvw: <http://www.w3.org/ns/csvw#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix spdx: <http://spdx.org/rdf/terms#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://ada.astromat.org/metadata/parameter/empaTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:name "Default Accelerating Voltage" ;
    schema1:propertyID "ada:parameter/empaTAPP/acceleratingVoltage" ;
    schema1:unitText "kV" ;
    schema1:value 15 .

<https://ada.astromat.org/metadata/parameter/empaTAPP/beamDiameter> a schema1:PropertyValue ;
    schema1:name "Default Beam Diameter" ;
    schema1:propertyID "ada:parameter/empaTAPP/beamDiameter" ;
    schema1:unitText "µm" ;
    schema1:value "0 (focused)" .

<https://ada.astromat.org/metadata/parameter/empaTAPP/reportedAnalyte> a schema1:PropertyValue ;
    schema1:name "Target Element" ;
    schema1:propertyID "ada:parameter/empaTAPP/reportedAnalyte" ;
    schema1:value "Si|Al|Ca|Na|Fe|Mg|Mn|Ti|Cr|K" .

ex:adaEMPA-P1 a schema1:Dataset,
        schema1:Product ;
    schema1:additionalType "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
        "ada:DataDeliveryPackage" ;
    schema1:creativeWorkStatus "Draft" ;
    schema1:dateModified "2026-04-29" ;
    schema1:description "Auto-generated adaEMPA profile-level Dataset for publication P1: Chi et al. 2015 (Tissintite, EPSL). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p1); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes." ;
    schema1:distribution [ a schema1:DataDownload ;
            schema1:contentUrl "https://astromat.org/downloads/adaempa-p1.zip" ;
            schema1:description "Archive containing tabular EMPA data for P1." ;
            schema1:encodingFormat "application/zip" ;
            schema1:hasPart ex:adaEMPA-P1-data-001 ;
            schema1:name "adaEMPA-P1-archive.zip" ;
            schema1:size [ a schema1:QuantitativeValue ;
                    schema1:unitText "byte" ;
                    schema1:value 1048576 ] ;
            spdx:checksum [ a spdx:Checksum ;
                    spdx:algorithm "SHA256" ;
                    spdx:checksumValue "0000000000000000000000000000000000000000000000000000000000000000" ] ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://registry.identifiers.org/registry/doi" ;
            schema1:value "10.PLACEHOLDER/adaempa-p1" ] ;
    schema1:license "https://creativecommons.org/licenses/by/4.0/" ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:identifier "https://ada.astromat.org/vocabulary/techniques/EMPA" ;
            schema1:name "Electron Microprobe Analysis (EMPA)" ] ;
    schema1:name "adaEMPA dataset for P1 (Chi et al. 2015 (Tissintite, EPSL))" ;
    schema1:subjectOf ex:adaEMPA-P1-metadata ;
    schema1:url "https://astromat.org/products/adaempa-p1" ;
    schema1:variableMeasured ex:adaEMPA-P1-var-Al,
        ex:adaEMPA-P1-var-Ca,
        ex:adaEMPA-P1-var-Cr,
        ex:adaEMPA-P1-var-Fe,
        ex:adaEMPA-P1-var-K,
        ex:adaEMPA-P1-var-Mg,
        ex:adaEMPA-P1-var-Mn,
        ex:adaEMPA-P1-var-Na,
        ex:adaEMPA-P1-var-Si,
        ex:adaEMPA-P1-var-Ti ;
    schema1:version "0.1" ;
    prov:wasGeneratedBy [ a schema1:Action,
                prov:Activity ;
            schema1:identifier "session-empa-p1" ;
            schema1:location [ a schema1:Place ;
                    schema1:additionalType "nxs:BaseClass/NXsource" ;
                    schema1:name "Caltech GPS Division Analytical Facility" ] ;
            schema1:object [ a schema1:Thing,
                        <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalType "MaterialSample" ;
                    schema1:description "Sample of: Silicate minerals (tissintite, maskelynite, pigeonite, fayalite)" ;
                    schema1:identifier "igsn:10.60471/PLACEHOLDER-P1" ;
                    schema1:name "Sample analyzed in P1" ] ;
            schema1:startDate "2026-04-29" ;
            prov:used [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType "ada:EMPAInstrument",
                        "nxs:BaseClass/NXinstrument" ;
                    schema1:identifier "ex:instrument-empa-001" ;
                    schema1:manufacturer [ a schema1:Organization ;
                            schema1:name "JEOL" ] ;
                    schema1:name "JEOL JXA-8200" ] ] .

ex:adaEMPA-P1-data-001 a cdi:TabularTextDataSet,
        schema1:MediaObject,
        schema1:Thing,
        ada:tabularData ;
    cdi:isDelimited true ;
    cdi:isFixedWidth false ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/empaTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/empaTAPP/beamDiameter>,
        <https://ada.astromat.org/metadata/parameter/empaTAPP/reportedAnalyte> ;
    schema1:additionalType "ada:EMPAQEATabular" ;
    schema1:description "Per-point quantitative EMPA analyses (Chi et al. 2015 (Tissintite, EPSL))." ;
    schema1:encodingFormat "text/csv" ;
    schema1:measurementTechnique ex:empaTAPP-p1 ;
    schema1:name "adaEMPA-P1-data.csv" ;
    csvw:delimiter "," ;
    csvw:header true ;
    ada:componentType "ada:EMPAQEATabular" ;
    ada:signalUsed "Kα x-ray lines" ;
    ada:spectrometersUsed "5x WDS" ;
    cdif:hasPhysicalMapping [ cdi:nullSequence "NA" ;
            cdif:index 0 ;
            cdif:physicalDataType "String" ] .

ex:adaEMPA-P1-metadata a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.0>,
        <https://w3id.org/cdif/data_description/1.0>,
        <https://w3id.org/cdif/discovery/1.0>,
        <https://w3id.org/cdif/manifest/1.0>,
        <https://w3id.org/cdif/provenance/1.0>,
        <https://w3id.org/geochem/metadata/profiles/adaEMPA>,
        <https://w3id.org/geochem/metadata/profiles/adaProduct> ;
    schema1:about ex:adaEMPA-P1 ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:dateModified "2026-04-29" ;
    schema1:maintainer [ a schema1:Organization ;
            schema1:name "Astromat Data Archive" ] ;
    schema1:sdDatePublished "2026-04-29T12:00:00Z" .

ex:adaEMPA-P1-var-Al a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Al abundance measured by EMPA WDS (Kα emission line; 20 s peak counting; 10 s background counting; calibrated against Anorthite)." ;
    schema1:name "Al" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Al" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P1-var-Ca a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Ca abundance measured by EMPA WDS (Kα emission line; 20 s peak counting; 10 s background counting; calibrated against Anorthite)." ;
    schema1:name "Ca" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Ca" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P1-var-Cr a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Cr abundance measured by EMPA WDS (Kα emission line; 20 s peak counting; 10 s background counting; calibrated against Cr2O3)." ;
    schema1:name "Cr" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Cr" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P1-var-Fe a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Fe abundance measured by EMPA WDS (Kα emission line; 20 s peak counting; 10 s background counting; calibrated against Fayalite)." ;
    schema1:name "Fe" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Fe" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P1-var-K a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "K abundance measured by EMPA WDS (Kα emission line; 20 s peak counting; 10 s background counting; calibrated against Microcline)." ;
    schema1:name "K" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/K" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P1-var-Mg a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Mg abundance measured by EMPA WDS (Kα emission line; 20 s peak counting; 10 s background counting; calibrated against Forsterite)." ;
    schema1:name "Mg" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Mg" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P1-var-Mn a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Mn abundance measured by EMPA WDS (Kα emission line; 20 s peak counting; 10 s background counting; calibrated against Mn2SiO4)." ;
    schema1:name "Mn" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Mn" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P1-var-Na a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Na abundance measured by EMPA WDS (Kα emission line; 20 s peak counting; 10 s background counting; calibrated against Albite)." ;
    schema1:name "Na" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Na" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P1-var-Si a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Si abundance measured by EMPA WDS (Kα emission line; 20 s peak counting; 10 s background counting; calibrated against Anorthite)." ;
    schema1:name "Si" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Si" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P1-var-Ti a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Ti abundance measured by EMPA WDS (Kα emission line; 20 s peak counting; 10 s background counting; calibrated against TiO2)." ;
    schema1:name "Ti" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Ti" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .


```


### adaEMPA — P2 (Hu et al. 2020 (Coesite NWA8657, GCA))
Auto-generated adaEMPA dataset record for publication P2.
schema:variableMeasured is derived from the empaTAPP TAPP definition's
ada:defaultAnalytes; schema:hasPart carries the paired detailEMPA fields
and references the TAPP via schema:measurementTechnique. Synthetic
placeholders are used for DOI, file size, and dates.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://cdif.org/0.1/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "prov": "http://www.w3.org/ns/prov#",
    "spdx": "http://spdx.org/rdf/terms#",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "dcterms": "http://purl.org/dc/terms/",
    "ex": "https://example.org/",
    "dcat": "http://www.w3.org/ns/dcat#"
  },
  "@id": "ex:adaEMPA-P2",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "adaEMPA dataset for P2 (Hu et al. 2020 (Coesite NWA8657, GCA))",
  "schema:description": "Auto-generated adaEMPA profile-level Dataset for publication P2: Hu et al. 2020 (Coesite NWA8657, GCA). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p2); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes.",
  "schema:additionalType": [
    "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.PLACEHOLDER/adaempa-p2"
  },
  "schema:url": "https://astromat.org/products/adaempa-p2",
  "schema:dateModified": "2026-04-29",
  "schema:version": "0.1",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:creativeWorkStatus": "Draft",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Electron Microprobe Analysis (EMPA)",
    "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/EMPA"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-empa-p2",
      "schema:startDate": "2026-04-29",
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": [
            "nxs:BaseClass/NXinstrument",
            "ada:EMPAInstrument"
          ],
          "schema:name": "JEOL JXA-8100",
          "schema:identifier": [
            "ex:instrument-empa-001"
          ],
          "schema:manufacturer": {
            "@type": [
              "schema:Organization"
            ],
            "schema:name": "JEOL"
          }
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Institute of Geology and Geophysics, Chinese Academy of Sciences (IGGCAS)",
        "schema:additionalType": [
          "nxs:BaseClass/NXsource"
        ]
      },
      "schema:object": [
        {
          "@type": [
            "schema:Thing",
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalType": [
            "MaterialSample"
          ],
          "schema:name": "Sample analyzed in P2",
          "schema:identifier": [
            "igsn:10.60471/PLACEHOLDER-P2"
          ],
          "schema:description": "Sample of: Maskelynite, \nmelt inclusion glasses, \nsilica glass, \ncoesite aggregates, \nmesostasis"
        }
      ]
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "ex:adaEMPA-P2-var-Si",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Si",
      "schema:description": "Si abundance measured by EMPA WDS (calibrated against Natural kaersutite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Si"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P2-var-Mg",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Mg",
      "schema:description": "Mg abundance measured by EMPA WDS (calibrated against Natural kaersutite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Mg"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P2-var-Fe",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Fe",
      "schema:description": "Fe abundance measured by EMPA WDS (calibrated against Natural kaersutite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Fe"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P2-var-Na",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Na",
      "schema:description": "Na abundance measured by EMPA WDS (calibrated against Jadeite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Na"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P2-var-Al",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Al",
      "schema:description": "Al abundance measured by EMPA WDS (calibrated against Jadeite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Al"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P2-var-Ca",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Ca",
      "schema:description": "Ca abundance measured by EMPA WDS (calibrated against Bustamite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Ca"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P2-var-Mn",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Mn",
      "schema:description": "Mn abundance measured by EMPA WDS (calibrated against Bustamite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Mn"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P2-var-K",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "K",
      "schema:description": "K abundance measured by EMPA WDS (calibrated against K-feldspar).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/K"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P2-var-Ti",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Ti",
      "schema:description": "Ti abundance measured by EMPA WDS (calibrated against Synthetic rutile).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Ti"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P2-var-Cr",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Cr",
      "schema:description": "Cr abundance measured by EMPA WDS (calibrated against Cr2O3).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Cr"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "adaEMPA-P2-archive.zip",
      "schema:description": "Archive containing tabular EMPA data for P2.",
      "schema:contentUrl": "https://astromat.org/downloads/adaempa-p2.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "0000000000000000000000000000000000000000000000000000000000000000"
      },
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 1048576,
        "schema:unitText": "byte"
      },
      "schema:hasPart": [
        {
          "@id": "ex:adaEMPA-P2-data-001",
          "@type": [
            "schema:MediaObject",
            "ada:tabularData",
            "cdi:TabularTextDataSet",
            "schema:Thing"
          ],
          "schema:name": "adaEMPA-P2-data.csv",
          "schema:description": "Per-point quantitative EMPA analyses (Hu et al. 2020 (Coesite NWA8657, GCA)).",
          "schema:additionalType": [
            "ada:EMPAQEATabular"
          ],
          "schema:encodingFormat": [
            "text/csv"
          ],
          "cdi:isDelimited": true,
          "cdi:isFixedWidth": false,
          "csvw:delimiter": ",",
          "csvw:header": true,
          "ada:componentType": "ada:EMPAQEATabular",
          "ada:spectrometersUsed": "5x WDS",
          "ada:signalUsed": "Kα x-ray lines",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-p2"
          },
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/empaTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/acceleratingVoltage",
              "schema:name": "Default Accelerating Voltage",
              "schema:value": 15,
              "schema:unitText": "kV"
            },
            {
              "@id": "ada:parameter/empaTAPP/reportedAnalyte",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/reportedAnalyte",
              "schema:name": "Target Element",
              "schema:value": "Si|Mg|Fe|Na|Al|Ca|Mn|K|Ti|Cr"
            }
          ],
          "cdif:hasPhysicalMapping": [
            {
              "cdif:index": 0,
              "cdif:physicalDataType": "String",
              "cdi:nullSequence": "NA"
            }
          ]
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:adaEMPA-P2-metadata",
    "schema:about": {
      "@id": "ex:adaEMPA-P2"
    },
    "schema:dateModified": "2026-04-29",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaEMPA"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaProduct"
      }
    ],
    "schema:maintainer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Astromat Data Archive"
    },
    "schema:sdDatePublished": "2026-04-29T12:00:00Z"
  }
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
      "csvw": "http://www.w3.org/ns/csvw#",
      "prov": "http://www.w3.org/ns/prov#",
      "dcterms": "http://purl.org/dc/terms/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/profiles/adaProfiles/adaEMPA/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://cdif.org/0.1/",
      "csvw": "http://www.w3.org/ns/csvw#",
      "prov": "http://www.w3.org/ns/prov#",
      "spdx": "http://spdx.org/rdf/terms#",
      "nxs": "http://purl.org/nexusformat/definitions/",
      "dcterms": "http://purl.org/dc/terms/",
      "ex": "https://example.org/",
      "dcat": "http://www.w3.org/ns/dcat#"
    }
  ],
  "@id": "ex:adaEMPA-P2",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "adaEMPA dataset for P2 (Hu et al. 2020 (Coesite NWA8657, GCA))",
  "schema:description": "Auto-generated adaEMPA profile-level Dataset for publication P2: Hu et al. 2020 (Coesite NWA8657, GCA). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p2); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes.",
  "schema:additionalType": [
    "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.PLACEHOLDER/adaempa-p2"
  },
  "schema:url": "https://astromat.org/products/adaempa-p2",
  "schema:dateModified": "2026-04-29",
  "schema:version": "0.1",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:creativeWorkStatus": "Draft",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Electron Microprobe Analysis (EMPA)",
    "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/EMPA"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-empa-p2",
      "schema:startDate": "2026-04-29",
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": [
            "nxs:BaseClass/NXinstrument",
            "ada:EMPAInstrument"
          ],
          "schema:name": "JEOL JXA-8100",
          "schema:identifier": [
            "ex:instrument-empa-001"
          ],
          "schema:manufacturer": {
            "@type": [
              "schema:Organization"
            ],
            "schema:name": "JEOL"
          }
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Institute of Geology and Geophysics, Chinese Academy of Sciences (IGGCAS)",
        "schema:additionalType": [
          "nxs:BaseClass/NXsource"
        ]
      },
      "schema:object": [
        {
          "@type": [
            "schema:Thing",
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalType": [
            "MaterialSample"
          ],
          "schema:name": "Sample analyzed in P2",
          "schema:identifier": [
            "igsn:10.60471/PLACEHOLDER-P2"
          ],
          "schema:description": "Sample of: Maskelynite, \nmelt inclusion glasses, \nsilica glass, \ncoesite aggregates, \nmesostasis"
        }
      ]
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "ex:adaEMPA-P2-var-Si",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Si",
      "schema:description": "Si abundance measured by EMPA WDS (calibrated against Natural kaersutite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Si"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P2-var-Mg",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Mg",
      "schema:description": "Mg abundance measured by EMPA WDS (calibrated against Natural kaersutite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Mg"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P2-var-Fe",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Fe",
      "schema:description": "Fe abundance measured by EMPA WDS (calibrated against Natural kaersutite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Fe"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P2-var-Na",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Na",
      "schema:description": "Na abundance measured by EMPA WDS (calibrated against Jadeite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Na"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P2-var-Al",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Al",
      "schema:description": "Al abundance measured by EMPA WDS (calibrated against Jadeite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Al"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P2-var-Ca",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Ca",
      "schema:description": "Ca abundance measured by EMPA WDS (calibrated against Bustamite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Ca"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P2-var-Mn",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Mn",
      "schema:description": "Mn abundance measured by EMPA WDS (calibrated against Bustamite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Mn"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P2-var-K",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "K",
      "schema:description": "K abundance measured by EMPA WDS (calibrated against K-feldspar).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/K"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P2-var-Ti",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Ti",
      "schema:description": "Ti abundance measured by EMPA WDS (calibrated against Synthetic rutile).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Ti"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P2-var-Cr",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Cr",
      "schema:description": "Cr abundance measured by EMPA WDS (calibrated against Cr2O3).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Cr"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "adaEMPA-P2-archive.zip",
      "schema:description": "Archive containing tabular EMPA data for P2.",
      "schema:contentUrl": "https://astromat.org/downloads/adaempa-p2.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "0000000000000000000000000000000000000000000000000000000000000000"
      },
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 1048576,
        "schema:unitText": "byte"
      },
      "schema:hasPart": [
        {
          "@id": "ex:adaEMPA-P2-data-001",
          "@type": [
            "schema:MediaObject",
            "ada:tabularData",
            "cdi:TabularTextDataSet",
            "schema:Thing"
          ],
          "schema:name": "adaEMPA-P2-data.csv",
          "schema:description": "Per-point quantitative EMPA analyses (Hu et al. 2020 (Coesite NWA8657, GCA)).",
          "schema:additionalType": [
            "ada:EMPAQEATabular"
          ],
          "schema:encodingFormat": [
            "text/csv"
          ],
          "cdi:isDelimited": true,
          "cdi:isFixedWidth": false,
          "csvw:delimiter": ",",
          "csvw:header": true,
          "ada:componentType": "ada:EMPAQEATabular",
          "ada:spectrometersUsed": "5x WDS",
          "ada:signalUsed": "K\u03b1 x-ray lines",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-p2"
          },
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/empaTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/acceleratingVoltage",
              "schema:name": "Default Accelerating Voltage",
              "schema:value": 15,
              "schema:unitText": "kV"
            },
            {
              "@id": "ada:parameter/empaTAPP/reportedAnalyte",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/reportedAnalyte",
              "schema:name": "Target Element",
              "schema:value": "Si|Mg|Fe|Na|Al|Ca|Mn|K|Ti|Cr"
            }
          ],
          "cdif:hasPhysicalMapping": [
            {
              "cdif:index": 0,
              "cdif:physicalDataType": "String",
              "cdi:nullSequence": "NA"
            }
          ]
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:adaEMPA-P2-metadata",
    "schema:about": {
      "@id": "ex:adaEMPA-P2"
    },
    "schema:dateModified": "2026-04-29",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaEMPA"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaProduct"
      }
    ],
    "schema:maintainer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Astromat Data Archive"
    },
    "schema:sdDatePublished": "2026-04-29T12:00:00Z"
  }
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://cdif.org/0.1/> .
@prefix csvw: <http://www.w3.org/ns/csvw#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix spdx: <http://spdx.org/rdf/terms#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://ada.astromat.org/metadata/parameter/empaTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:name "Default Accelerating Voltage" ;
    schema1:propertyID "ada:parameter/empaTAPP/acceleratingVoltage" ;
    schema1:unitText "kV" ;
    schema1:value 15 .

<https://ada.astromat.org/metadata/parameter/empaTAPP/reportedAnalyte> a schema1:PropertyValue ;
    schema1:name "Target Element" ;
    schema1:propertyID "ada:parameter/empaTAPP/reportedAnalyte" ;
    schema1:value "Si|Mg|Fe|Na|Al|Ca|Mn|K|Ti|Cr" .

ex:adaEMPA-P2 a schema1:Dataset,
        schema1:Product ;
    schema1:additionalType "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
        "ada:DataDeliveryPackage" ;
    schema1:creativeWorkStatus "Draft" ;
    schema1:dateModified "2026-04-29" ;
    schema1:description "Auto-generated adaEMPA profile-level Dataset for publication P2: Hu et al. 2020 (Coesite NWA8657, GCA). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p2); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes." ;
    schema1:distribution [ a schema1:DataDownload ;
            schema1:contentUrl "https://astromat.org/downloads/adaempa-p2.zip" ;
            schema1:description "Archive containing tabular EMPA data for P2." ;
            schema1:encodingFormat "application/zip" ;
            schema1:hasPart ex:adaEMPA-P2-data-001 ;
            schema1:name "adaEMPA-P2-archive.zip" ;
            schema1:size [ a schema1:QuantitativeValue ;
                    schema1:unitText "byte" ;
                    schema1:value 1048576 ] ;
            spdx:checksum [ a spdx:Checksum ;
                    spdx:algorithm "SHA256" ;
                    spdx:checksumValue "0000000000000000000000000000000000000000000000000000000000000000" ] ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://registry.identifiers.org/registry/doi" ;
            schema1:value "10.PLACEHOLDER/adaempa-p2" ] ;
    schema1:license "https://creativecommons.org/licenses/by/4.0/" ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:identifier "https://ada.astromat.org/vocabulary/techniques/EMPA" ;
            schema1:name "Electron Microprobe Analysis (EMPA)" ] ;
    schema1:name "adaEMPA dataset for P2 (Hu et al. 2020 (Coesite NWA8657, GCA))" ;
    schema1:subjectOf ex:adaEMPA-P2-metadata ;
    schema1:url "https://astromat.org/products/adaempa-p2" ;
    schema1:variableMeasured ex:adaEMPA-P2-var-Al,
        ex:adaEMPA-P2-var-Ca,
        ex:adaEMPA-P2-var-Cr,
        ex:adaEMPA-P2-var-Fe,
        ex:adaEMPA-P2-var-K,
        ex:adaEMPA-P2-var-Mg,
        ex:adaEMPA-P2-var-Mn,
        ex:adaEMPA-P2-var-Na,
        ex:adaEMPA-P2-var-Si,
        ex:adaEMPA-P2-var-Ti ;
    schema1:version "0.1" ;
    prov:wasGeneratedBy [ a schema1:Action,
                prov:Activity ;
            schema1:identifier "session-empa-p2" ;
            schema1:location [ a schema1:Place ;
                    schema1:additionalType "nxs:BaseClass/NXsource" ;
                    schema1:name "Institute of Geology and Geophysics, Chinese Academy of Sciences (IGGCAS)" ] ;
            schema1:object [ a schema1:Thing,
                        <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalType "MaterialSample" ;
                    schema1:description """Sample of: Maskelynite, 
melt inclusion glasses, 
silica glass, 
coesite aggregates, 
mesostasis""" ;
                    schema1:identifier "igsn:10.60471/PLACEHOLDER-P2" ;
                    schema1:name "Sample analyzed in P2" ] ;
            schema1:startDate "2026-04-29" ;
            prov:used [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType "ada:EMPAInstrument",
                        "nxs:BaseClass/NXinstrument" ;
                    schema1:identifier "ex:instrument-empa-001" ;
                    schema1:manufacturer [ a schema1:Organization ;
                            schema1:name "JEOL" ] ;
                    schema1:name "JEOL JXA-8100" ] ] .

ex:adaEMPA-P2-data-001 a cdi:TabularTextDataSet,
        schema1:MediaObject,
        schema1:Thing,
        ada:tabularData ;
    cdi:isDelimited true ;
    cdi:isFixedWidth false ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/empaTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/empaTAPP/reportedAnalyte> ;
    schema1:additionalType "ada:EMPAQEATabular" ;
    schema1:description "Per-point quantitative EMPA analyses (Hu et al. 2020 (Coesite NWA8657, GCA))." ;
    schema1:encodingFormat "text/csv" ;
    schema1:measurementTechnique ex:empaTAPP-p2 ;
    schema1:name "adaEMPA-P2-data.csv" ;
    csvw:delimiter "," ;
    csvw:header true ;
    ada:componentType "ada:EMPAQEATabular" ;
    ada:signalUsed "Kα x-ray lines" ;
    ada:spectrometersUsed "5x WDS" ;
    cdif:hasPhysicalMapping [ cdi:nullSequence "NA" ;
            cdif:index 0 ;
            cdif:physicalDataType "String" ] .

ex:adaEMPA-P2-metadata a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.0>,
        <https://w3id.org/cdif/data_description/1.0>,
        <https://w3id.org/cdif/discovery/1.0>,
        <https://w3id.org/cdif/manifest/1.0>,
        <https://w3id.org/cdif/provenance/1.0>,
        <https://w3id.org/geochem/metadata/profiles/adaEMPA>,
        <https://w3id.org/geochem/metadata/profiles/adaProduct> ;
    schema1:about ex:adaEMPA-P2 ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:dateModified "2026-04-29" ;
    schema1:maintainer [ a schema1:Organization ;
            schema1:name "Astromat Data Archive" ] ;
    schema1:sdDatePublished "2026-04-29T12:00:00Z" .

ex:adaEMPA-P2-var-Al a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Al abundance measured by EMPA WDS (calibrated against Jadeite)." ;
    schema1:name "Al" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Al" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P2-var-Ca a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Ca abundance measured by EMPA WDS (calibrated against Bustamite)." ;
    schema1:name "Ca" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Ca" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P2-var-Cr a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Cr abundance measured by EMPA WDS (calibrated against Cr2O3)." ;
    schema1:name "Cr" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Cr" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P2-var-Fe a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Fe abundance measured by EMPA WDS (calibrated against Natural kaersutite)." ;
    schema1:name "Fe" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Fe" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P2-var-K a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "K abundance measured by EMPA WDS (calibrated against K-feldspar)." ;
    schema1:name "K" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/K" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P2-var-Mg a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Mg abundance measured by EMPA WDS (calibrated against Natural kaersutite)." ;
    schema1:name "Mg" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Mg" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P2-var-Mn a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Mn abundance measured by EMPA WDS (calibrated against Bustamite)." ;
    schema1:name "Mn" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Mn" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P2-var-Na a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Na abundance measured by EMPA WDS (calibrated against Jadeite)." ;
    schema1:name "Na" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Na" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P2-var-Si a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Si abundance measured by EMPA WDS (calibrated against Natural kaersutite)." ;
    schema1:name "Si" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Si" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P2-var-Ti a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Ti abundance measured by EMPA WDS (calibrated against Synthetic rutile)." ;
    schema1:name "Ti" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Ti" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .


```


### adaEMPA — P3sil (Liu et al. 2016 (Tissint silicate mineral chem., MAPS))
Auto-generated adaEMPA dataset record for publication P3sil.
schema:variableMeasured is derived from the empaTAPP TAPP definition's
ada:defaultAnalytes; schema:hasPart carries the paired detailEMPA fields
and references the TAPP via schema:measurementTechnique. Synthetic
placeholders are used for DOI, file size, and dates.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://cdif.org/0.1/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "prov": "http://www.w3.org/ns/prov#",
    "spdx": "http://spdx.org/rdf/terms#",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "dcterms": "http://purl.org/dc/terms/",
    "ex": "https://example.org/",
    "dcat": "http://www.w3.org/ns/dcat#"
  },
  "@id": "ex:adaEMPA-P3sil",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "adaEMPA dataset for P3sil (Liu et al. 2016 (Tissint silicate mineral chem., MAPS))",
  "schema:description": "Auto-generated adaEMPA profile-level Dataset for publication P3sil: Liu et al. 2016 (Tissint silicate mineral chem., MAPS). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p3sil); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes.",
  "schema:additionalType": [
    "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.PLACEHOLDER/adaempa-p3sil"
  },
  "schema:url": "https://astromat.org/products/adaempa-p3sil",
  "schema:dateModified": "2026-04-29",
  "schema:version": "0.1",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:creativeWorkStatus": "Draft",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Electron Microprobe Analysis (EMPA)",
    "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/EMPA"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-empa-p3sil",
      "schema:startDate": "2026-04-29",
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": [
            "nxs:BaseClass/NXinstrument",
            "ada:EMPAInstrument"
          ],
          "schema:name": "Cameca; JEOL SX100 (Univ. Tennessee); JXA-8200 (Caltech)",
          "schema:identifier": [
            "ex:instrument-empa-001"
          ],
          "schema:manufacturer": {
            "@type": [
              "schema:Organization"
            ],
            "schema:name": "Cameca; JEOL"
          }
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "University of Tennessee (Cameca SX100); Caltech (JEOL JXA-8200)",
        "schema:additionalType": [
          "nxs:BaseClass/NXsource"
        ]
      },
      "schema:object": [
        {
          "@type": [
            "schema:Thing",
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalType": [
            "MaterialSample"
          ],
          "schema:name": "Sample analyzed in P3sil",
          "schema:identifier": [
            "igsn:10.60471/PLACEHOLDER-P3sil"
          ],
          "schema:description": "Sample of: Olivine, pyroxene, Fe-Ti-Cr oxides"
        }
      ]
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "ex:adaEMPA-P3sil-var-Si",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Si",
      "schema:description": "Si abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Si"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P3sil-var-Ti",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Ti",
      "schema:description": "Ti abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Ti"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P3sil-var-Al",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Al",
      "schema:description": "Al abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Al"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P3sil-var-Mg",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Mg",
      "schema:description": "Mg abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Mg"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P3sil-var-Ca",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Ca",
      "schema:description": "Ca abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Ca"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P3sil-var-Fe",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Fe",
      "schema:description": "Fe abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Fe"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P3sil-var-Mn",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Mn",
      "schema:description": "Mn abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Mn"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P3sil-var-Cr",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Cr",
      "schema:description": "Cr abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Cr"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P3sil-var-Ni",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Ni",
      "schema:description": "Ni abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Ni"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P3sil-var-Na",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Na",
      "schema:description": "Na abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Na"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P3sil-var-K",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "K",
      "schema:description": "K abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/K"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P3sil-var-P",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "P",
      "schema:description": "P abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/P"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "adaEMPA-P3sil-archive.zip",
      "schema:description": "Archive containing tabular EMPA data for P3sil.",
      "schema:contentUrl": "https://astromat.org/downloads/adaempa-p3sil.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "0000000000000000000000000000000000000000000000000000000000000000"
      },
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 1048576,
        "schema:unitText": "byte"
      },
      "schema:hasPart": [
        {
          "@id": "ex:adaEMPA-P3sil-data-001",
          "@type": [
            "schema:MediaObject",
            "ada:tabularData",
            "cdi:TabularTextDataSet",
            "schema:Thing"
          ],
          "schema:name": "adaEMPA-P3sil-data.csv",
          "schema:description": "Per-point quantitative EMPA analyses (Liu et al. 2016 (Tissint silicate mineral chem., MAPS)).",
          "schema:additionalType": [
            "ada:EMPAQEATabular"
          ],
          "schema:encodingFormat": [
            "text/csv"
          ],
          "cdi:isDelimited": true,
          "cdi:isFixedWidth": false,
          "csvw:delimiter": ",",
          "csvw:header": true,
          "ada:componentType": "ada:EMPAQEATabular",
          "ada:spectrometersUsed": "5x WDS",
          "ada:signalUsed": "Kα x-ray lines",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-p3sil"
          },
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/empaTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/acceleratingVoltage",
              "schema:name": "Default Accelerating Voltage",
              "schema:value": 15,
              "schema:unitText": "kV"
            },
            {
              "@id": "ada:parameter/empaTAPP/beamDiameter",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/beamDiameter",
              "schema:name": "Default Beam Diameter",
              "schema:value": "1–2 µm focused",
              "schema:unitText": "µm"
            },
            {
              "@id": "ada:parameter/empaTAPP/reportedAnalyte",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/reportedAnalyte",
              "schema:name": "Target Element",
              "schema:value": "Si|Ti|Al|Mg|Ca|Fe|Mn|Cr|Ni|Na|K|P"
            }
          ],
          "cdif:hasPhysicalMapping": [
            {
              "cdif:index": 0,
              "cdif:physicalDataType": "String",
              "cdi:nullSequence": "NA"
            }
          ]
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:adaEMPA-P3sil-metadata",
    "schema:about": {
      "@id": "ex:adaEMPA-P3sil"
    },
    "schema:dateModified": "2026-04-29",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaEMPA"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaProduct"
      }
    ],
    "schema:maintainer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Astromat Data Archive"
    },
    "schema:sdDatePublished": "2026-04-29T12:00:00Z"
  }
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
      "csvw": "http://www.w3.org/ns/csvw#",
      "prov": "http://www.w3.org/ns/prov#",
      "dcterms": "http://purl.org/dc/terms/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/profiles/adaProfiles/adaEMPA/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://cdif.org/0.1/",
      "csvw": "http://www.w3.org/ns/csvw#",
      "prov": "http://www.w3.org/ns/prov#",
      "spdx": "http://spdx.org/rdf/terms#",
      "nxs": "http://purl.org/nexusformat/definitions/",
      "dcterms": "http://purl.org/dc/terms/",
      "ex": "https://example.org/",
      "dcat": "http://www.w3.org/ns/dcat#"
    }
  ],
  "@id": "ex:adaEMPA-P3sil",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "adaEMPA dataset for P3sil (Liu et al. 2016 (Tissint silicate mineral chem., MAPS))",
  "schema:description": "Auto-generated adaEMPA profile-level Dataset for publication P3sil: Liu et al. 2016 (Tissint silicate mineral chem., MAPS). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p3sil); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes.",
  "schema:additionalType": [
    "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.PLACEHOLDER/adaempa-p3sil"
  },
  "schema:url": "https://astromat.org/products/adaempa-p3sil",
  "schema:dateModified": "2026-04-29",
  "schema:version": "0.1",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:creativeWorkStatus": "Draft",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Electron Microprobe Analysis (EMPA)",
    "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/EMPA"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-empa-p3sil",
      "schema:startDate": "2026-04-29",
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": [
            "nxs:BaseClass/NXinstrument",
            "ada:EMPAInstrument"
          ],
          "schema:name": "Cameca; JEOL SX100 (Univ. Tennessee); JXA-8200 (Caltech)",
          "schema:identifier": [
            "ex:instrument-empa-001"
          ],
          "schema:manufacturer": {
            "@type": [
              "schema:Organization"
            ],
            "schema:name": "Cameca; JEOL"
          }
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "University of Tennessee (Cameca SX100); Caltech (JEOL JXA-8200)",
        "schema:additionalType": [
          "nxs:BaseClass/NXsource"
        ]
      },
      "schema:object": [
        {
          "@type": [
            "schema:Thing",
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalType": [
            "MaterialSample"
          ],
          "schema:name": "Sample analyzed in P3sil",
          "schema:identifier": [
            "igsn:10.60471/PLACEHOLDER-P3sil"
          ],
          "schema:description": "Sample of: Olivine, pyroxene, Fe-Ti-Cr oxides"
        }
      ]
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "ex:adaEMPA-P3sil-var-Si",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Si",
      "schema:description": "Si abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Si"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P3sil-var-Ti",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Ti",
      "schema:description": "Ti abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Ti"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P3sil-var-Al",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Al",
      "schema:description": "Al abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Al"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P3sil-var-Mg",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Mg",
      "schema:description": "Mg abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Mg"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P3sil-var-Ca",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Ca",
      "schema:description": "Ca abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Ca"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P3sil-var-Fe",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Fe",
      "schema:description": "Fe abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Fe"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P3sil-var-Mn",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Mn",
      "schema:description": "Mn abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Mn"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P3sil-var-Cr",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Cr",
      "schema:description": "Cr abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Cr"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P3sil-var-Ni",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Ni",
      "schema:description": "Ni abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Ni"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P3sil-var-Na",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Na",
      "schema:description": "Na abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Na"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P3sil-var-K",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "K",
      "schema:description": "K abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/K"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P3sil-var-P",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "P",
      "schema:description": "P abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/P"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "adaEMPA-P3sil-archive.zip",
      "schema:description": "Archive containing tabular EMPA data for P3sil.",
      "schema:contentUrl": "https://astromat.org/downloads/adaempa-p3sil.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "0000000000000000000000000000000000000000000000000000000000000000"
      },
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 1048576,
        "schema:unitText": "byte"
      },
      "schema:hasPart": [
        {
          "@id": "ex:adaEMPA-P3sil-data-001",
          "@type": [
            "schema:MediaObject",
            "ada:tabularData",
            "cdi:TabularTextDataSet",
            "schema:Thing"
          ],
          "schema:name": "adaEMPA-P3sil-data.csv",
          "schema:description": "Per-point quantitative EMPA analyses (Liu et al. 2016 (Tissint silicate mineral chem., MAPS)).",
          "schema:additionalType": [
            "ada:EMPAQEATabular"
          ],
          "schema:encodingFormat": [
            "text/csv"
          ],
          "cdi:isDelimited": true,
          "cdi:isFixedWidth": false,
          "csvw:delimiter": ",",
          "csvw:header": true,
          "ada:componentType": "ada:EMPAQEATabular",
          "ada:spectrometersUsed": "5x WDS",
          "ada:signalUsed": "K\u03b1 x-ray lines",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-p3sil"
          },
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/empaTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/acceleratingVoltage",
              "schema:name": "Default Accelerating Voltage",
              "schema:value": 15,
              "schema:unitText": "kV"
            },
            {
              "@id": "ada:parameter/empaTAPP/beamDiameter",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/beamDiameter",
              "schema:name": "Default Beam Diameter",
              "schema:value": "1\u20132 \u00b5m focused",
              "schema:unitText": "\u00b5m"
            },
            {
              "@id": "ada:parameter/empaTAPP/reportedAnalyte",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/reportedAnalyte",
              "schema:name": "Target Element",
              "schema:value": "Si|Ti|Al|Mg|Ca|Fe|Mn|Cr|Ni|Na|K|P"
            }
          ],
          "cdif:hasPhysicalMapping": [
            {
              "cdif:index": 0,
              "cdif:physicalDataType": "String",
              "cdi:nullSequence": "NA"
            }
          ]
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:adaEMPA-P3sil-metadata",
    "schema:about": {
      "@id": "ex:adaEMPA-P3sil"
    },
    "schema:dateModified": "2026-04-29",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaEMPA"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaProduct"
      }
    ],
    "schema:maintainer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Astromat Data Archive"
    },
    "schema:sdDatePublished": "2026-04-29T12:00:00Z"
  }
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://cdif.org/0.1/> .
@prefix csvw: <http://www.w3.org/ns/csvw#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix spdx: <http://spdx.org/rdf/terms#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://ada.astromat.org/metadata/parameter/empaTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:name "Default Accelerating Voltage" ;
    schema1:propertyID "ada:parameter/empaTAPP/acceleratingVoltage" ;
    schema1:unitText "kV" ;
    schema1:value 15 .

<https://ada.astromat.org/metadata/parameter/empaTAPP/beamDiameter> a schema1:PropertyValue ;
    schema1:name "Default Beam Diameter" ;
    schema1:propertyID "ada:parameter/empaTAPP/beamDiameter" ;
    schema1:unitText "µm" ;
    schema1:value "1–2 µm focused" .

<https://ada.astromat.org/metadata/parameter/empaTAPP/reportedAnalyte> a schema1:PropertyValue ;
    schema1:name "Target Element" ;
    schema1:propertyID "ada:parameter/empaTAPP/reportedAnalyte" ;
    schema1:value "Si|Ti|Al|Mg|Ca|Fe|Mn|Cr|Ni|Na|K|P" .

ex:adaEMPA-P3sil a schema1:Dataset,
        schema1:Product ;
    schema1:additionalType "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
        "ada:DataDeliveryPackage" ;
    schema1:creativeWorkStatus "Draft" ;
    schema1:dateModified "2026-04-29" ;
    schema1:description "Auto-generated adaEMPA profile-level Dataset for publication P3sil: Liu et al. 2016 (Tissint silicate mineral chem., MAPS). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p3sil); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes." ;
    schema1:distribution [ a schema1:DataDownload ;
            schema1:contentUrl "https://astromat.org/downloads/adaempa-p3sil.zip" ;
            schema1:description "Archive containing tabular EMPA data for P3sil." ;
            schema1:encodingFormat "application/zip" ;
            schema1:hasPart ex:adaEMPA-P3sil-data-001 ;
            schema1:name "adaEMPA-P3sil-archive.zip" ;
            schema1:size [ a schema1:QuantitativeValue ;
                    schema1:unitText "byte" ;
                    schema1:value 1048576 ] ;
            spdx:checksum [ a spdx:Checksum ;
                    spdx:algorithm "SHA256" ;
                    spdx:checksumValue "0000000000000000000000000000000000000000000000000000000000000000" ] ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://registry.identifiers.org/registry/doi" ;
            schema1:value "10.PLACEHOLDER/adaempa-p3sil" ] ;
    schema1:license "https://creativecommons.org/licenses/by/4.0/" ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:identifier "https://ada.astromat.org/vocabulary/techniques/EMPA" ;
            schema1:name "Electron Microprobe Analysis (EMPA)" ] ;
    schema1:name "adaEMPA dataset for P3sil (Liu et al. 2016 (Tissint silicate mineral chem., MAPS))" ;
    schema1:subjectOf ex:adaEMPA-P3sil-metadata ;
    schema1:url "https://astromat.org/products/adaempa-p3sil" ;
    schema1:variableMeasured ex:adaEMPA-P3sil-var-Al,
        ex:adaEMPA-P3sil-var-Ca,
        ex:adaEMPA-P3sil-var-Cr,
        ex:adaEMPA-P3sil-var-Fe,
        ex:adaEMPA-P3sil-var-K,
        ex:adaEMPA-P3sil-var-Mg,
        ex:adaEMPA-P3sil-var-Mn,
        ex:adaEMPA-P3sil-var-Na,
        ex:adaEMPA-P3sil-var-Ni,
        ex:adaEMPA-P3sil-var-P,
        ex:adaEMPA-P3sil-var-Si,
        ex:adaEMPA-P3sil-var-Ti ;
    schema1:version "0.1" ;
    prov:wasGeneratedBy [ a schema1:Action,
                prov:Activity ;
            schema1:identifier "session-empa-p3sil" ;
            schema1:location [ a schema1:Place ;
                    schema1:additionalType "nxs:BaseClass/NXsource" ;
                    schema1:name "University of Tennessee (Cameca SX100); Caltech (JEOL JXA-8200)" ] ;
            schema1:object [ a schema1:Thing,
                        <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalType "MaterialSample" ;
                    schema1:description "Sample of: Olivine, pyroxene, Fe-Ti-Cr oxides" ;
                    schema1:identifier "igsn:10.60471/PLACEHOLDER-P3sil" ;
                    schema1:name "Sample analyzed in P3sil" ] ;
            schema1:startDate "2026-04-29" ;
            prov:used [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType "ada:EMPAInstrument",
                        "nxs:BaseClass/NXinstrument" ;
                    schema1:identifier "ex:instrument-empa-001" ;
                    schema1:manufacturer [ a schema1:Organization ;
                            schema1:name "Cameca; JEOL" ] ;
                    schema1:name "Cameca; JEOL SX100 (Univ. Tennessee); JXA-8200 (Caltech)" ] ] .

ex:adaEMPA-P3sil-data-001 a cdi:TabularTextDataSet,
        schema1:MediaObject,
        schema1:Thing,
        ada:tabularData ;
    cdi:isDelimited true ;
    cdi:isFixedWidth false ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/empaTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/empaTAPP/beamDiameter>,
        <https://ada.astromat.org/metadata/parameter/empaTAPP/reportedAnalyte> ;
    schema1:additionalType "ada:EMPAQEATabular" ;
    schema1:description "Per-point quantitative EMPA analyses (Liu et al. 2016 (Tissint silicate mineral chem., MAPS))." ;
    schema1:encodingFormat "text/csv" ;
    schema1:measurementTechnique ex:empaTAPP-p3sil ;
    schema1:name "adaEMPA-P3sil-data.csv" ;
    csvw:delimiter "," ;
    csvw:header true ;
    ada:componentType "ada:EMPAQEATabular" ;
    ada:signalUsed "Kα x-ray lines" ;
    ada:spectrometersUsed "5x WDS" ;
    cdif:hasPhysicalMapping [ cdi:nullSequence "NA" ;
            cdif:index 0 ;
            cdif:physicalDataType "String" ] .

ex:adaEMPA-P3sil-metadata a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.0>,
        <https://w3id.org/cdif/data_description/1.0>,
        <https://w3id.org/cdif/discovery/1.0>,
        <https://w3id.org/cdif/manifest/1.0>,
        <https://w3id.org/cdif/provenance/1.0>,
        <https://w3id.org/geochem/metadata/profiles/adaEMPA>,
        <https://w3id.org/geochem/metadata/profiles/adaProduct> ;
    schema1:about ex:adaEMPA-P3sil ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:dateModified "2026-04-29" ;
    schema1:maintainer [ a schema1:Organization ;
            schema1:name "Astromat Data Archive" ] ;
    schema1:sdDatePublished "2026-04-29T12:00:00Z" .

ex:adaEMPA-P3sil-var-Al a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Al abundance measured by EMPA WDS." ;
    schema1:name "Al" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Al" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P3sil-var-Ca a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Ca abundance measured by EMPA WDS." ;
    schema1:name "Ca" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Ca" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P3sil-var-Cr a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Cr abundance measured by EMPA WDS." ;
    schema1:name "Cr" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Cr" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P3sil-var-Fe a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Fe abundance measured by EMPA WDS." ;
    schema1:name "Fe" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Fe" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P3sil-var-K a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "K abundance measured by EMPA WDS." ;
    schema1:name "K" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/K" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P3sil-var-Mg a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Mg abundance measured by EMPA WDS." ;
    schema1:name "Mg" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Mg" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P3sil-var-Mn a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Mn abundance measured by EMPA WDS." ;
    schema1:name "Mn" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Mn" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P3sil-var-Na a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Na abundance measured by EMPA WDS." ;
    schema1:name "Na" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Na" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P3sil-var-Ni a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Ni abundance measured by EMPA WDS." ;
    schema1:name "Ni" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Ni" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P3sil-var-P a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "P abundance measured by EMPA WDS." ;
    schema1:name "P" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/P" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P3sil-var-Si a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Si abundance measured by EMPA WDS." ;
    schema1:name "Si" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Si" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P3sil-var-Ti a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Ti abundance measured by EMPA WDS." ;
    schema1:name "Ti" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Ti" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .


```


### adaEMPA — P3phos (Liu et al. 2016 (Tissint phosphate mineral chem., MAPS))
Auto-generated adaEMPA dataset record for publication P3phos.
schema:variableMeasured is derived from the empaTAPP TAPP definition's
ada:defaultAnalytes; schema:hasPart carries the paired detailEMPA fields
and references the TAPP via schema:measurementTechnique. Synthetic
placeholders are used for DOI, file size, and dates.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://cdif.org/0.1/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "prov": "http://www.w3.org/ns/prov#",
    "spdx": "http://spdx.org/rdf/terms#",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "dcterms": "http://purl.org/dc/terms/",
    "ex": "https://example.org/",
    "dcat": "http://www.w3.org/ns/dcat#"
  },
  "@id": "ex:adaEMPA-P3phos",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "adaEMPA dataset for P3phos (Liu et al. 2016 (Tissint phosphate mineral chem., MAPS))",
  "schema:description": "Auto-generated adaEMPA profile-level Dataset for publication P3phos: Liu et al. 2016 (Tissint phosphate mineral chem., MAPS). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p3phos); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes.",
  "schema:additionalType": [
    "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.PLACEHOLDER/adaempa-p3phos"
  },
  "schema:url": "https://astromat.org/products/adaempa-p3phos",
  "schema:dateModified": "2026-04-29",
  "schema:version": "0.1",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:creativeWorkStatus": "Draft",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Electron Microprobe Analysis (EMPA)",
    "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/EMPA"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-empa-p3phos",
      "schema:startDate": "2026-04-29",
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": [
            "nxs:BaseClass/NXinstrument",
            "ada:EMPAInstrument"
          ],
          "schema:name": "Cameca; JEOL SX100 (Univ. Tennessee); JXA-8200 (Caltech)",
          "schema:identifier": [
            "ex:instrument-empa-001"
          ],
          "schema:manufacturer": {
            "@type": [
              "schema:Organization"
            ],
            "schema:name": "Cameca; JEOL"
          }
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "University of Tennessee (Cameca SX100); Caltech (JEOL JXA-8200)",
        "schema:additionalType": [
          "nxs:BaseClass/NXsource"
        ]
      },
      "schema:object": [
        {
          "@type": [
            "schema:Thing",
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalType": [
            "MaterialSample"
          ],
          "schema:name": "Sample analyzed in P3phos",
          "schema:identifier": [
            "igsn:10.60471/PLACEHOLDER-P3phos"
          ],
          "schema:description": "Sample of: maskelynite, phosphate, sulfide, glass"
        }
      ]
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "ex:adaEMPA-P3phos-var-Si",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Si",
      "schema:description": "Si abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Si"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P3phos-var-Ti",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Ti",
      "schema:description": "Ti abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Ti"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P3phos-var-Al",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Al",
      "schema:description": "Al abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Al"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P3phos-var-Mg",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Mg",
      "schema:description": "Mg abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Mg"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P3phos-var-Ca",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Ca",
      "schema:description": "Ca abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Ca"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P3phos-var-Fe",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Fe",
      "schema:description": "Fe abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Fe"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P3phos-var-Mn",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Mn",
      "schema:description": "Mn abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Mn"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P3phos-var-Cr",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Cr",
      "schema:description": "Cr abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Cr"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P3phos-var-Ni",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Ni",
      "schema:description": "Ni abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Ni"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P3phos-var-Na",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Na",
      "schema:description": "Na abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Na"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P3phos-var-K",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "K",
      "schema:description": "K abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/K"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P3phos-var-P",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "P",
      "schema:description": "P abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/P"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "adaEMPA-P3phos-archive.zip",
      "schema:description": "Archive containing tabular EMPA data for P3phos.",
      "schema:contentUrl": "https://astromat.org/downloads/adaempa-p3phos.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "0000000000000000000000000000000000000000000000000000000000000000"
      },
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 1048576,
        "schema:unitText": "byte"
      },
      "schema:hasPart": [
        {
          "@id": "ex:adaEMPA-P3phos-data-001",
          "@type": [
            "schema:MediaObject",
            "ada:tabularData",
            "cdi:TabularTextDataSet",
            "schema:Thing"
          ],
          "schema:name": "adaEMPA-P3phos-data.csv",
          "schema:description": "Per-point quantitative EMPA analyses (Liu et al. 2016 (Tissint phosphate mineral chem., MAPS)).",
          "schema:additionalType": [
            "ada:EMPAQEATabular"
          ],
          "schema:encodingFormat": [
            "text/csv"
          ],
          "cdi:isDelimited": true,
          "cdi:isFixedWidth": false,
          "csvw:delimiter": ",",
          "csvw:header": true,
          "ada:componentType": "ada:EMPAQEATabular",
          "ada:spectrometersUsed": "5x WDS",
          "ada:signalUsed": "Kα x-ray lines",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-p3phos"
          },
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/empaTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/acceleratingVoltage",
              "schema:name": "Default Accelerating Voltage",
              "schema:value": 15,
              "schema:unitText": "kV"
            },
            {
              "@id": "ada:parameter/empaTAPP/beamDiameter",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/beamDiameter",
              "schema:name": "Default Beam Diameter",
              "schema:value": "5–10 µm defocused",
              "schema:unitText": "µm"
            },
            {
              "@id": "ada:parameter/empaTAPP/reportedAnalyte",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/reportedAnalyte",
              "schema:name": "Target Element",
              "schema:value": "Si|Ti|Al|Mg|Ca|Fe|Mn|Cr|Ni|Na|K|P"
            }
          ],
          "cdif:hasPhysicalMapping": [
            {
              "cdif:index": 0,
              "cdif:physicalDataType": "String",
              "cdi:nullSequence": "NA"
            }
          ]
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:adaEMPA-P3phos-metadata",
    "schema:about": {
      "@id": "ex:adaEMPA-P3phos"
    },
    "schema:dateModified": "2026-04-29",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaEMPA"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaProduct"
      }
    ],
    "schema:maintainer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Astromat Data Archive"
    },
    "schema:sdDatePublished": "2026-04-29T12:00:00Z"
  }
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
      "csvw": "http://www.w3.org/ns/csvw#",
      "prov": "http://www.w3.org/ns/prov#",
      "dcterms": "http://purl.org/dc/terms/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/profiles/adaProfiles/adaEMPA/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://cdif.org/0.1/",
      "csvw": "http://www.w3.org/ns/csvw#",
      "prov": "http://www.w3.org/ns/prov#",
      "spdx": "http://spdx.org/rdf/terms#",
      "nxs": "http://purl.org/nexusformat/definitions/",
      "dcterms": "http://purl.org/dc/terms/",
      "ex": "https://example.org/",
      "dcat": "http://www.w3.org/ns/dcat#"
    }
  ],
  "@id": "ex:adaEMPA-P3phos",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "adaEMPA dataset for P3phos (Liu et al. 2016 (Tissint phosphate mineral chem., MAPS))",
  "schema:description": "Auto-generated adaEMPA profile-level Dataset for publication P3phos: Liu et al. 2016 (Tissint phosphate mineral chem., MAPS). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p3phos); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes.",
  "schema:additionalType": [
    "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.PLACEHOLDER/adaempa-p3phos"
  },
  "schema:url": "https://astromat.org/products/adaempa-p3phos",
  "schema:dateModified": "2026-04-29",
  "schema:version": "0.1",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:creativeWorkStatus": "Draft",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Electron Microprobe Analysis (EMPA)",
    "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/EMPA"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-empa-p3phos",
      "schema:startDate": "2026-04-29",
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": [
            "nxs:BaseClass/NXinstrument",
            "ada:EMPAInstrument"
          ],
          "schema:name": "Cameca; JEOL SX100 (Univ. Tennessee); JXA-8200 (Caltech)",
          "schema:identifier": [
            "ex:instrument-empa-001"
          ],
          "schema:manufacturer": {
            "@type": [
              "schema:Organization"
            ],
            "schema:name": "Cameca; JEOL"
          }
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "University of Tennessee (Cameca SX100); Caltech (JEOL JXA-8200)",
        "schema:additionalType": [
          "nxs:BaseClass/NXsource"
        ]
      },
      "schema:object": [
        {
          "@type": [
            "schema:Thing",
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalType": [
            "MaterialSample"
          ],
          "schema:name": "Sample analyzed in P3phos",
          "schema:identifier": [
            "igsn:10.60471/PLACEHOLDER-P3phos"
          ],
          "schema:description": "Sample of: maskelynite, phosphate, sulfide, glass"
        }
      ]
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "ex:adaEMPA-P3phos-var-Si",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Si",
      "schema:description": "Si abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Si"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P3phos-var-Ti",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Ti",
      "schema:description": "Ti abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Ti"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P3phos-var-Al",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Al",
      "schema:description": "Al abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Al"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P3phos-var-Mg",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Mg",
      "schema:description": "Mg abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Mg"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P3phos-var-Ca",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Ca",
      "schema:description": "Ca abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Ca"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P3phos-var-Fe",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Fe",
      "schema:description": "Fe abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Fe"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P3phos-var-Mn",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Mn",
      "schema:description": "Mn abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Mn"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P3phos-var-Cr",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Cr",
      "schema:description": "Cr abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Cr"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P3phos-var-Ni",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Ni",
      "schema:description": "Ni abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Ni"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P3phos-var-Na",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Na",
      "schema:description": "Na abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Na"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P3phos-var-K",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "K",
      "schema:description": "K abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/K"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P3phos-var-P",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "P",
      "schema:description": "P abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/P"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "adaEMPA-P3phos-archive.zip",
      "schema:description": "Archive containing tabular EMPA data for P3phos.",
      "schema:contentUrl": "https://astromat.org/downloads/adaempa-p3phos.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "0000000000000000000000000000000000000000000000000000000000000000"
      },
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 1048576,
        "schema:unitText": "byte"
      },
      "schema:hasPart": [
        {
          "@id": "ex:adaEMPA-P3phos-data-001",
          "@type": [
            "schema:MediaObject",
            "ada:tabularData",
            "cdi:TabularTextDataSet",
            "schema:Thing"
          ],
          "schema:name": "adaEMPA-P3phos-data.csv",
          "schema:description": "Per-point quantitative EMPA analyses (Liu et al. 2016 (Tissint phosphate mineral chem., MAPS)).",
          "schema:additionalType": [
            "ada:EMPAQEATabular"
          ],
          "schema:encodingFormat": [
            "text/csv"
          ],
          "cdi:isDelimited": true,
          "cdi:isFixedWidth": false,
          "csvw:delimiter": ",",
          "csvw:header": true,
          "ada:componentType": "ada:EMPAQEATabular",
          "ada:spectrometersUsed": "5x WDS",
          "ada:signalUsed": "K\u03b1 x-ray lines",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-p3phos"
          },
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/empaTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/acceleratingVoltage",
              "schema:name": "Default Accelerating Voltage",
              "schema:value": 15,
              "schema:unitText": "kV"
            },
            {
              "@id": "ada:parameter/empaTAPP/beamDiameter",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/beamDiameter",
              "schema:name": "Default Beam Diameter",
              "schema:value": "5\u201310 \u00b5m defocused",
              "schema:unitText": "\u00b5m"
            },
            {
              "@id": "ada:parameter/empaTAPP/reportedAnalyte",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/reportedAnalyte",
              "schema:name": "Target Element",
              "schema:value": "Si|Ti|Al|Mg|Ca|Fe|Mn|Cr|Ni|Na|K|P"
            }
          ],
          "cdif:hasPhysicalMapping": [
            {
              "cdif:index": 0,
              "cdif:physicalDataType": "String",
              "cdi:nullSequence": "NA"
            }
          ]
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:adaEMPA-P3phos-metadata",
    "schema:about": {
      "@id": "ex:adaEMPA-P3phos"
    },
    "schema:dateModified": "2026-04-29",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaEMPA"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaProduct"
      }
    ],
    "schema:maintainer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Astromat Data Archive"
    },
    "schema:sdDatePublished": "2026-04-29T12:00:00Z"
  }
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://cdif.org/0.1/> .
@prefix csvw: <http://www.w3.org/ns/csvw#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix spdx: <http://spdx.org/rdf/terms#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://ada.astromat.org/metadata/parameter/empaTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:name "Default Accelerating Voltage" ;
    schema1:propertyID "ada:parameter/empaTAPP/acceleratingVoltage" ;
    schema1:unitText "kV" ;
    schema1:value 15 .

<https://ada.astromat.org/metadata/parameter/empaTAPP/beamDiameter> a schema1:PropertyValue ;
    schema1:name "Default Beam Diameter" ;
    schema1:propertyID "ada:parameter/empaTAPP/beamDiameter" ;
    schema1:unitText "µm" ;
    schema1:value "5–10 µm defocused" .

<https://ada.astromat.org/metadata/parameter/empaTAPP/reportedAnalyte> a schema1:PropertyValue ;
    schema1:name "Target Element" ;
    schema1:propertyID "ada:parameter/empaTAPP/reportedAnalyte" ;
    schema1:value "Si|Ti|Al|Mg|Ca|Fe|Mn|Cr|Ni|Na|K|P" .

ex:adaEMPA-P3phos a schema1:Dataset,
        schema1:Product ;
    schema1:additionalType "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
        "ada:DataDeliveryPackage" ;
    schema1:creativeWorkStatus "Draft" ;
    schema1:dateModified "2026-04-29" ;
    schema1:description "Auto-generated adaEMPA profile-level Dataset for publication P3phos: Liu et al. 2016 (Tissint phosphate mineral chem., MAPS). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p3phos); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes." ;
    schema1:distribution [ a schema1:DataDownload ;
            schema1:contentUrl "https://astromat.org/downloads/adaempa-p3phos.zip" ;
            schema1:description "Archive containing tabular EMPA data for P3phos." ;
            schema1:encodingFormat "application/zip" ;
            schema1:hasPart ex:adaEMPA-P3phos-data-001 ;
            schema1:name "adaEMPA-P3phos-archive.zip" ;
            schema1:size [ a schema1:QuantitativeValue ;
                    schema1:unitText "byte" ;
                    schema1:value 1048576 ] ;
            spdx:checksum [ a spdx:Checksum ;
                    spdx:algorithm "SHA256" ;
                    spdx:checksumValue "0000000000000000000000000000000000000000000000000000000000000000" ] ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://registry.identifiers.org/registry/doi" ;
            schema1:value "10.PLACEHOLDER/adaempa-p3phos" ] ;
    schema1:license "https://creativecommons.org/licenses/by/4.0/" ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:identifier "https://ada.astromat.org/vocabulary/techniques/EMPA" ;
            schema1:name "Electron Microprobe Analysis (EMPA)" ] ;
    schema1:name "adaEMPA dataset for P3phos (Liu et al. 2016 (Tissint phosphate mineral chem., MAPS))" ;
    schema1:subjectOf ex:adaEMPA-P3phos-metadata ;
    schema1:url "https://astromat.org/products/adaempa-p3phos" ;
    schema1:variableMeasured ex:adaEMPA-P3phos-var-Al,
        ex:adaEMPA-P3phos-var-Ca,
        ex:adaEMPA-P3phos-var-Cr,
        ex:adaEMPA-P3phos-var-Fe,
        ex:adaEMPA-P3phos-var-K,
        ex:adaEMPA-P3phos-var-Mg,
        ex:adaEMPA-P3phos-var-Mn,
        ex:adaEMPA-P3phos-var-Na,
        ex:adaEMPA-P3phos-var-Ni,
        ex:adaEMPA-P3phos-var-P,
        ex:adaEMPA-P3phos-var-Si,
        ex:adaEMPA-P3phos-var-Ti ;
    schema1:version "0.1" ;
    prov:wasGeneratedBy [ a schema1:Action,
                prov:Activity ;
            schema1:identifier "session-empa-p3phos" ;
            schema1:location [ a schema1:Place ;
                    schema1:additionalType "nxs:BaseClass/NXsource" ;
                    schema1:name "University of Tennessee (Cameca SX100); Caltech (JEOL JXA-8200)" ] ;
            schema1:object [ a schema1:Thing,
                        <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalType "MaterialSample" ;
                    schema1:description "Sample of: maskelynite, phosphate, sulfide, glass" ;
                    schema1:identifier "igsn:10.60471/PLACEHOLDER-P3phos" ;
                    schema1:name "Sample analyzed in P3phos" ] ;
            schema1:startDate "2026-04-29" ;
            prov:used [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType "ada:EMPAInstrument",
                        "nxs:BaseClass/NXinstrument" ;
                    schema1:identifier "ex:instrument-empa-001" ;
                    schema1:manufacturer [ a schema1:Organization ;
                            schema1:name "Cameca; JEOL" ] ;
                    schema1:name "Cameca; JEOL SX100 (Univ. Tennessee); JXA-8200 (Caltech)" ] ] .

ex:adaEMPA-P3phos-data-001 a cdi:TabularTextDataSet,
        schema1:MediaObject,
        schema1:Thing,
        ada:tabularData ;
    cdi:isDelimited true ;
    cdi:isFixedWidth false ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/empaTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/empaTAPP/beamDiameter>,
        <https://ada.astromat.org/metadata/parameter/empaTAPP/reportedAnalyte> ;
    schema1:additionalType "ada:EMPAQEATabular" ;
    schema1:description "Per-point quantitative EMPA analyses (Liu et al. 2016 (Tissint phosphate mineral chem., MAPS))." ;
    schema1:encodingFormat "text/csv" ;
    schema1:measurementTechnique ex:empaTAPP-p3phos ;
    schema1:name "adaEMPA-P3phos-data.csv" ;
    csvw:delimiter "," ;
    csvw:header true ;
    ada:componentType "ada:EMPAQEATabular" ;
    ada:signalUsed "Kα x-ray lines" ;
    ada:spectrometersUsed "5x WDS" ;
    cdif:hasPhysicalMapping [ cdi:nullSequence "NA" ;
            cdif:index 0 ;
            cdif:physicalDataType "String" ] .

ex:adaEMPA-P3phos-metadata a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.0>,
        <https://w3id.org/cdif/data_description/1.0>,
        <https://w3id.org/cdif/discovery/1.0>,
        <https://w3id.org/cdif/manifest/1.0>,
        <https://w3id.org/cdif/provenance/1.0>,
        <https://w3id.org/geochem/metadata/profiles/adaEMPA>,
        <https://w3id.org/geochem/metadata/profiles/adaProduct> ;
    schema1:about ex:adaEMPA-P3phos ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:dateModified "2026-04-29" ;
    schema1:maintainer [ a schema1:Organization ;
            schema1:name "Astromat Data Archive" ] ;
    schema1:sdDatePublished "2026-04-29T12:00:00Z" .

ex:adaEMPA-P3phos-var-Al a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Al abundance measured by EMPA WDS." ;
    schema1:name "Al" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Al" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P3phos-var-Ca a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Ca abundance measured by EMPA WDS." ;
    schema1:name "Ca" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Ca" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P3phos-var-Cr a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Cr abundance measured by EMPA WDS." ;
    schema1:name "Cr" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Cr" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P3phos-var-Fe a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Fe abundance measured by EMPA WDS." ;
    schema1:name "Fe" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Fe" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P3phos-var-K a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "K abundance measured by EMPA WDS." ;
    schema1:name "K" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/K" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P3phos-var-Mg a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Mg abundance measured by EMPA WDS." ;
    schema1:name "Mg" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Mg" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P3phos-var-Mn a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Mn abundance measured by EMPA WDS." ;
    schema1:name "Mn" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Mn" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P3phos-var-Na a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Na abundance measured by EMPA WDS." ;
    schema1:name "Na" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Na" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P3phos-var-Ni a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Ni abundance measured by EMPA WDS." ;
    schema1:name "Ni" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Ni" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P3phos-var-P a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "P abundance measured by EMPA WDS." ;
    schema1:name "P" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/P" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P3phos-var-Si a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Si abundance measured by EMPA WDS." ;
    schema1:name "Si" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Si" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P3phos-var-Ti a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Ti abundance measured by EMPA WDS." ;
    schema1:name "Ti" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Ti" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .


```


### adaEMPA — P4 (Ma et al. 2017 (Liebermannite, MAPS))
Auto-generated adaEMPA dataset record for publication P4.
schema:variableMeasured is derived from the empaTAPP TAPP definition's
ada:defaultAnalytes; schema:hasPart carries the paired detailEMPA fields
and references the TAPP via schema:measurementTechnique. Synthetic
placeholders are used for DOI, file size, and dates.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://cdif.org/0.1/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "prov": "http://www.w3.org/ns/prov#",
    "spdx": "http://spdx.org/rdf/terms#",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "dcterms": "http://purl.org/dc/terms/",
    "ex": "https://example.org/",
    "dcat": "http://www.w3.org/ns/dcat#"
  },
  "@id": "ex:adaEMPA-P4",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "adaEMPA dataset for P4 (Ma et al. 2017 (Liebermannite, MAPS))",
  "schema:description": "Auto-generated adaEMPA profile-level Dataset for publication P4: Ma et al. 2017 (Liebermannite, MAPS). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p4); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes.",
  "schema:additionalType": [
    "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.PLACEHOLDER/adaempa-p4"
  },
  "schema:url": "https://astromat.org/products/adaempa-p4",
  "schema:dateModified": "2026-04-29",
  "schema:version": "0.1",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:creativeWorkStatus": "Draft",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Electron Microprobe Analysis (EMPA)",
    "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/EMPA"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-empa-p4",
      "schema:startDate": "2026-04-29",
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": [
            "nxs:BaseClass/NXinstrument",
            "ada:EMPAInstrument"
          ],
          "schema:name": "JEOL JXA-8200",
          "schema:identifier": [
            "ex:instrument-empa-001"
          ],
          "schema:manufacturer": {
            "@type": [
              "schema:Organization"
            ],
            "schema:name": "JEOL"
          }
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Caltech GPS Division Analytical Facility",
        "schema:additionalType": [
          "nxs:BaseClass/NXsource"
        ]
      },
      "schema:object": [
        {
          "@type": [
            "schema:Thing",
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalType": [
            "MaterialSample"
          ],
          "schema:name": "Sample analyzed in P4",
          "schema:identifier": [
            "igsn:10.60471/PLACEHOLDER-P4"
          ],
          "schema:description": "Sample of: Liebermannite, lingunite, maskelynite (K-feldspar, plagioclase high-pressure polymorphs)"
        }
      ]
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "ex:adaEMPA-P4-var-Si",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Si",
      "schema:description": "Si abundance measured by EMPA WDS (Kα emission line; 20 s peak counting; 10 s background counting; calibrated against Asbestos microcline).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Si"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P4-var-Al",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Al",
      "schema:description": "Al abundance measured by EMPA WDS (Kα emission line; 20 s peak counting; 10 s background counting; calibrated against Asbestos microcline).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Al"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P4-var-K",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "K",
      "schema:description": "K abundance measured by EMPA WDS (Kα emission line; 20 s peak counting; 10 s background counting; calibrated against Asbestos microcline).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/K"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P4-var-Ca",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Ca",
      "schema:description": "Ca abundance measured by EMPA WDS (Kα emission line; 20 s peak counting; 10 s background counting; calibrated against Synthetic anorthite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Ca"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P4-var-Na",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Na",
      "schema:description": "Na abundance measured by EMPA WDS (Kα emission line; 20 s peak counting; 10 s background counting; calibrated against Amelia albite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Na"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P4-var-Fe",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Fe",
      "schema:description": "Fe abundance measured by EMPA WDS (Kα emission line; 20 s peak counting; 10 s background counting; calibrated against Synthetic fayalite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Fe"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P4-var-Mg",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Mg",
      "schema:description": "Mg abundance measured by EMPA WDS (Kα emission line; 20 s peak counting; 10 s background counting; calibrated against Synthetic forsterite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Mg"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P4-var-Ti",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Ti",
      "schema:description": "Ti abundance measured by EMPA WDS (Kα emission line; 20 s peak counting; 10 s background counting; calibrated against Synthetic TiO2).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Ti"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P4-var-Cr",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Cr",
      "schema:description": "Cr abundance measured by EMPA WDS (Kα emission line; 20 s peak counting; 10 s background counting; calibrated against Synthetic Cr2O3).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Cr"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P4-var-Mn",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Mn",
      "schema:description": "Mn abundance measured by EMPA WDS (Kα emission line; 20 s peak counting; 10 s background counting; calibrated against Synthetic Mn-olivine).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Mn"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "adaEMPA-P4-archive.zip",
      "schema:description": "Archive containing tabular EMPA data for P4.",
      "schema:contentUrl": "https://astromat.org/downloads/adaempa-p4.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "0000000000000000000000000000000000000000000000000000000000000000"
      },
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 1048576,
        "schema:unitText": "byte"
      },
      "schema:hasPart": [
        {
          "@id": "ex:adaEMPA-P4-data-001",
          "@type": [
            "schema:MediaObject",
            "ada:tabularData",
            "cdi:TabularTextDataSet",
            "schema:Thing"
          ],
          "schema:name": "adaEMPA-P4-data.csv",
          "schema:description": "Per-point quantitative EMPA analyses (Ma et al. 2017 (Liebermannite, MAPS)).",
          "schema:additionalType": [
            "ada:EMPAQEATabular"
          ],
          "schema:encodingFormat": [
            "text/csv"
          ],
          "cdi:isDelimited": true,
          "cdi:isFixedWidth": false,
          "csvw:delimiter": ",",
          "csvw:header": true,
          "ada:componentType": "ada:EMPAQEATabular",
          "ada:spectrometersUsed": "5x WDS",
          "ada:signalUsed": "Kα x-ray lines",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-p4"
          },
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/empaTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/acceleratingVoltage",
              "schema:name": "Default Accelerating Voltage",
              "schema:value": 15,
              "schema:unitText": "kV"
            },
            {
              "@id": "ada:parameter/empaTAPP/beamDiameter",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/beamDiameter",
              "schema:name": "Default Beam Diameter",
              "schema:value": "0 (focused)",
              "schema:unitText": "µm"
            },
            {
              "@id": "ada:parameter/empaTAPP/reportedAnalyte",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/reportedAnalyte",
              "schema:name": "Target Element",
              "schema:value": "Si|Al|K|Ca|Na|Fe|Mg|Ti|Cr|Mn"
            }
          ],
          "cdif:hasPhysicalMapping": [
            {
              "cdif:index": 0,
              "cdif:physicalDataType": "String",
              "cdi:nullSequence": "NA"
            }
          ]
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:adaEMPA-P4-metadata",
    "schema:about": {
      "@id": "ex:adaEMPA-P4"
    },
    "schema:dateModified": "2026-04-29",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaEMPA"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaProduct"
      }
    ],
    "schema:maintainer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Astromat Data Archive"
    },
    "schema:sdDatePublished": "2026-04-29T12:00:00Z"
  }
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
      "csvw": "http://www.w3.org/ns/csvw#",
      "prov": "http://www.w3.org/ns/prov#",
      "dcterms": "http://purl.org/dc/terms/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/profiles/adaProfiles/adaEMPA/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://cdif.org/0.1/",
      "csvw": "http://www.w3.org/ns/csvw#",
      "prov": "http://www.w3.org/ns/prov#",
      "spdx": "http://spdx.org/rdf/terms#",
      "nxs": "http://purl.org/nexusformat/definitions/",
      "dcterms": "http://purl.org/dc/terms/",
      "ex": "https://example.org/",
      "dcat": "http://www.w3.org/ns/dcat#"
    }
  ],
  "@id": "ex:adaEMPA-P4",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "adaEMPA dataset for P4 (Ma et al. 2017 (Liebermannite, MAPS))",
  "schema:description": "Auto-generated adaEMPA profile-level Dataset for publication P4: Ma et al. 2017 (Liebermannite, MAPS). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p4); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes.",
  "schema:additionalType": [
    "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.PLACEHOLDER/adaempa-p4"
  },
  "schema:url": "https://astromat.org/products/adaempa-p4",
  "schema:dateModified": "2026-04-29",
  "schema:version": "0.1",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:creativeWorkStatus": "Draft",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Electron Microprobe Analysis (EMPA)",
    "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/EMPA"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-empa-p4",
      "schema:startDate": "2026-04-29",
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": [
            "nxs:BaseClass/NXinstrument",
            "ada:EMPAInstrument"
          ],
          "schema:name": "JEOL JXA-8200",
          "schema:identifier": [
            "ex:instrument-empa-001"
          ],
          "schema:manufacturer": {
            "@type": [
              "schema:Organization"
            ],
            "schema:name": "JEOL"
          }
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Caltech GPS Division Analytical Facility",
        "schema:additionalType": [
          "nxs:BaseClass/NXsource"
        ]
      },
      "schema:object": [
        {
          "@type": [
            "schema:Thing",
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalType": [
            "MaterialSample"
          ],
          "schema:name": "Sample analyzed in P4",
          "schema:identifier": [
            "igsn:10.60471/PLACEHOLDER-P4"
          ],
          "schema:description": "Sample of: Liebermannite, lingunite, maskelynite (K-feldspar, plagioclase high-pressure polymorphs)"
        }
      ]
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "ex:adaEMPA-P4-var-Si",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Si",
      "schema:description": "Si abundance measured by EMPA WDS (K\u03b1 emission line; 20 s peak counting; 10 s background counting; calibrated against Asbestos microcline).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Si"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P4-var-Al",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Al",
      "schema:description": "Al abundance measured by EMPA WDS (K\u03b1 emission line; 20 s peak counting; 10 s background counting; calibrated against Asbestos microcline).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Al"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P4-var-K",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "K",
      "schema:description": "K abundance measured by EMPA WDS (K\u03b1 emission line; 20 s peak counting; 10 s background counting; calibrated against Asbestos microcline).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/K"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P4-var-Ca",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Ca",
      "schema:description": "Ca abundance measured by EMPA WDS (K\u03b1 emission line; 20 s peak counting; 10 s background counting; calibrated against Synthetic anorthite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Ca"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P4-var-Na",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Na",
      "schema:description": "Na abundance measured by EMPA WDS (K\u03b1 emission line; 20 s peak counting; 10 s background counting; calibrated against Amelia albite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Na"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P4-var-Fe",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Fe",
      "schema:description": "Fe abundance measured by EMPA WDS (K\u03b1 emission line; 20 s peak counting; 10 s background counting; calibrated against Synthetic fayalite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Fe"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P4-var-Mg",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Mg",
      "schema:description": "Mg abundance measured by EMPA WDS (K\u03b1 emission line; 20 s peak counting; 10 s background counting; calibrated against Synthetic forsterite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Mg"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P4-var-Ti",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Ti",
      "schema:description": "Ti abundance measured by EMPA WDS (K\u03b1 emission line; 20 s peak counting; 10 s background counting; calibrated against Synthetic TiO2).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Ti"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P4-var-Cr",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Cr",
      "schema:description": "Cr abundance measured by EMPA WDS (K\u03b1 emission line; 20 s peak counting; 10 s background counting; calibrated against Synthetic Cr2O3).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Cr"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P4-var-Mn",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Mn",
      "schema:description": "Mn abundance measured by EMPA WDS (K\u03b1 emission line; 20 s peak counting; 10 s background counting; calibrated against Synthetic Mn-olivine).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Mn"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "adaEMPA-P4-archive.zip",
      "schema:description": "Archive containing tabular EMPA data for P4.",
      "schema:contentUrl": "https://astromat.org/downloads/adaempa-p4.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "0000000000000000000000000000000000000000000000000000000000000000"
      },
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 1048576,
        "schema:unitText": "byte"
      },
      "schema:hasPart": [
        {
          "@id": "ex:adaEMPA-P4-data-001",
          "@type": [
            "schema:MediaObject",
            "ada:tabularData",
            "cdi:TabularTextDataSet",
            "schema:Thing"
          ],
          "schema:name": "adaEMPA-P4-data.csv",
          "schema:description": "Per-point quantitative EMPA analyses (Ma et al. 2017 (Liebermannite, MAPS)).",
          "schema:additionalType": [
            "ada:EMPAQEATabular"
          ],
          "schema:encodingFormat": [
            "text/csv"
          ],
          "cdi:isDelimited": true,
          "cdi:isFixedWidth": false,
          "csvw:delimiter": ",",
          "csvw:header": true,
          "ada:componentType": "ada:EMPAQEATabular",
          "ada:spectrometersUsed": "5x WDS",
          "ada:signalUsed": "K\u03b1 x-ray lines",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-p4"
          },
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/empaTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/acceleratingVoltage",
              "schema:name": "Default Accelerating Voltage",
              "schema:value": 15,
              "schema:unitText": "kV"
            },
            {
              "@id": "ada:parameter/empaTAPP/beamDiameter",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/beamDiameter",
              "schema:name": "Default Beam Diameter",
              "schema:value": "0 (focused)",
              "schema:unitText": "\u00b5m"
            },
            {
              "@id": "ada:parameter/empaTAPP/reportedAnalyte",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/reportedAnalyte",
              "schema:name": "Target Element",
              "schema:value": "Si|Al|K|Ca|Na|Fe|Mg|Ti|Cr|Mn"
            }
          ],
          "cdif:hasPhysicalMapping": [
            {
              "cdif:index": 0,
              "cdif:physicalDataType": "String",
              "cdi:nullSequence": "NA"
            }
          ]
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:adaEMPA-P4-metadata",
    "schema:about": {
      "@id": "ex:adaEMPA-P4"
    },
    "schema:dateModified": "2026-04-29",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaEMPA"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaProduct"
      }
    ],
    "schema:maintainer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Astromat Data Archive"
    },
    "schema:sdDatePublished": "2026-04-29T12:00:00Z"
  }
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://cdif.org/0.1/> .
@prefix csvw: <http://www.w3.org/ns/csvw#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix spdx: <http://spdx.org/rdf/terms#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://ada.astromat.org/metadata/parameter/empaTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:name "Default Accelerating Voltage" ;
    schema1:propertyID "ada:parameter/empaTAPP/acceleratingVoltage" ;
    schema1:unitText "kV" ;
    schema1:value 15 .

<https://ada.astromat.org/metadata/parameter/empaTAPP/beamDiameter> a schema1:PropertyValue ;
    schema1:name "Default Beam Diameter" ;
    schema1:propertyID "ada:parameter/empaTAPP/beamDiameter" ;
    schema1:unitText "µm" ;
    schema1:value "0 (focused)" .

<https://ada.astromat.org/metadata/parameter/empaTAPP/reportedAnalyte> a schema1:PropertyValue ;
    schema1:name "Target Element" ;
    schema1:propertyID "ada:parameter/empaTAPP/reportedAnalyte" ;
    schema1:value "Si|Al|K|Ca|Na|Fe|Mg|Ti|Cr|Mn" .

ex:adaEMPA-P4 a schema1:Dataset,
        schema1:Product ;
    schema1:additionalType "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
        "ada:DataDeliveryPackage" ;
    schema1:creativeWorkStatus "Draft" ;
    schema1:dateModified "2026-04-29" ;
    schema1:description "Auto-generated adaEMPA profile-level Dataset for publication P4: Ma et al. 2017 (Liebermannite, MAPS). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p4); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes." ;
    schema1:distribution [ a schema1:DataDownload ;
            schema1:contentUrl "https://astromat.org/downloads/adaempa-p4.zip" ;
            schema1:description "Archive containing tabular EMPA data for P4." ;
            schema1:encodingFormat "application/zip" ;
            schema1:hasPart ex:adaEMPA-P4-data-001 ;
            schema1:name "adaEMPA-P4-archive.zip" ;
            schema1:size [ a schema1:QuantitativeValue ;
                    schema1:unitText "byte" ;
                    schema1:value 1048576 ] ;
            spdx:checksum [ a spdx:Checksum ;
                    spdx:algorithm "SHA256" ;
                    spdx:checksumValue "0000000000000000000000000000000000000000000000000000000000000000" ] ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://registry.identifiers.org/registry/doi" ;
            schema1:value "10.PLACEHOLDER/adaempa-p4" ] ;
    schema1:license "https://creativecommons.org/licenses/by/4.0/" ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:identifier "https://ada.astromat.org/vocabulary/techniques/EMPA" ;
            schema1:name "Electron Microprobe Analysis (EMPA)" ] ;
    schema1:name "adaEMPA dataset for P4 (Ma et al. 2017 (Liebermannite, MAPS))" ;
    schema1:subjectOf ex:adaEMPA-P4-metadata ;
    schema1:url "https://astromat.org/products/adaempa-p4" ;
    schema1:variableMeasured ex:adaEMPA-P4-var-Al,
        ex:adaEMPA-P4-var-Ca,
        ex:adaEMPA-P4-var-Cr,
        ex:adaEMPA-P4-var-Fe,
        ex:adaEMPA-P4-var-K,
        ex:adaEMPA-P4-var-Mg,
        ex:adaEMPA-P4-var-Mn,
        ex:adaEMPA-P4-var-Na,
        ex:adaEMPA-P4-var-Si,
        ex:adaEMPA-P4-var-Ti ;
    schema1:version "0.1" ;
    prov:wasGeneratedBy [ a schema1:Action,
                prov:Activity ;
            schema1:identifier "session-empa-p4" ;
            schema1:location [ a schema1:Place ;
                    schema1:additionalType "nxs:BaseClass/NXsource" ;
                    schema1:name "Caltech GPS Division Analytical Facility" ] ;
            schema1:object [ a schema1:Thing,
                        <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalType "MaterialSample" ;
                    schema1:description "Sample of: Liebermannite, lingunite, maskelynite (K-feldspar, plagioclase high-pressure polymorphs)" ;
                    schema1:identifier "igsn:10.60471/PLACEHOLDER-P4" ;
                    schema1:name "Sample analyzed in P4" ] ;
            schema1:startDate "2026-04-29" ;
            prov:used [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType "ada:EMPAInstrument",
                        "nxs:BaseClass/NXinstrument" ;
                    schema1:identifier "ex:instrument-empa-001" ;
                    schema1:manufacturer [ a schema1:Organization ;
                            schema1:name "JEOL" ] ;
                    schema1:name "JEOL JXA-8200" ] ] .

ex:adaEMPA-P4-data-001 a cdi:TabularTextDataSet,
        schema1:MediaObject,
        schema1:Thing,
        ada:tabularData ;
    cdi:isDelimited true ;
    cdi:isFixedWidth false ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/empaTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/empaTAPP/beamDiameter>,
        <https://ada.astromat.org/metadata/parameter/empaTAPP/reportedAnalyte> ;
    schema1:additionalType "ada:EMPAQEATabular" ;
    schema1:description "Per-point quantitative EMPA analyses (Ma et al. 2017 (Liebermannite, MAPS))." ;
    schema1:encodingFormat "text/csv" ;
    schema1:measurementTechnique ex:empaTAPP-p4 ;
    schema1:name "adaEMPA-P4-data.csv" ;
    csvw:delimiter "," ;
    csvw:header true ;
    ada:componentType "ada:EMPAQEATabular" ;
    ada:signalUsed "Kα x-ray lines" ;
    ada:spectrometersUsed "5x WDS" ;
    cdif:hasPhysicalMapping [ cdi:nullSequence "NA" ;
            cdif:index 0 ;
            cdif:physicalDataType "String" ] .

ex:adaEMPA-P4-metadata a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.0>,
        <https://w3id.org/cdif/data_description/1.0>,
        <https://w3id.org/cdif/discovery/1.0>,
        <https://w3id.org/cdif/manifest/1.0>,
        <https://w3id.org/cdif/provenance/1.0>,
        <https://w3id.org/geochem/metadata/profiles/adaEMPA>,
        <https://w3id.org/geochem/metadata/profiles/adaProduct> ;
    schema1:about ex:adaEMPA-P4 ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:dateModified "2026-04-29" ;
    schema1:maintainer [ a schema1:Organization ;
            schema1:name "Astromat Data Archive" ] ;
    schema1:sdDatePublished "2026-04-29T12:00:00Z" .

ex:adaEMPA-P4-var-Al a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Al abundance measured by EMPA WDS (Kα emission line; 20 s peak counting; 10 s background counting; calibrated against Asbestos microcline)." ;
    schema1:name "Al" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Al" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P4-var-Ca a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Ca abundance measured by EMPA WDS (Kα emission line; 20 s peak counting; 10 s background counting; calibrated against Synthetic anorthite)." ;
    schema1:name "Ca" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Ca" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P4-var-Cr a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Cr abundance measured by EMPA WDS (Kα emission line; 20 s peak counting; 10 s background counting; calibrated against Synthetic Cr2O3)." ;
    schema1:name "Cr" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Cr" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P4-var-Fe a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Fe abundance measured by EMPA WDS (Kα emission line; 20 s peak counting; 10 s background counting; calibrated against Synthetic fayalite)." ;
    schema1:name "Fe" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Fe" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P4-var-K a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "K abundance measured by EMPA WDS (Kα emission line; 20 s peak counting; 10 s background counting; calibrated against Asbestos microcline)." ;
    schema1:name "K" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/K" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P4-var-Mg a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Mg abundance measured by EMPA WDS (Kα emission line; 20 s peak counting; 10 s background counting; calibrated against Synthetic forsterite)." ;
    schema1:name "Mg" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Mg" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P4-var-Mn a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Mn abundance measured by EMPA WDS (Kα emission line; 20 s peak counting; 10 s background counting; calibrated against Synthetic Mn-olivine)." ;
    schema1:name "Mn" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Mn" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P4-var-Na a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Na abundance measured by EMPA WDS (Kα emission line; 20 s peak counting; 10 s background counting; calibrated against Amelia albite)." ;
    schema1:name "Na" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Na" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P4-var-Si a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Si abundance measured by EMPA WDS (Kα emission line; 20 s peak counting; 10 s background counting; calibrated against Asbestos microcline)." ;
    schema1:name "Si" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Si" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P4-var-Ti a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Ti abundance measured by EMPA WDS (Kα emission line; 20 s peak counting; 10 s background counting; calibrated against Synthetic TiO2)." ;
    schema1:name "Ti" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Ti" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .


```


### adaEMPA — P5 (Frank et al. 2023 (Ivuna CAI, MAPS))
Auto-generated adaEMPA dataset record for publication P5.
schema:variableMeasured is derived from the empaTAPP TAPP definition's
ada:defaultAnalytes; schema:hasPart carries the paired detailEMPA fields
and references the TAPP via schema:measurementTechnique. Synthetic
placeholders are used for DOI, file size, and dates.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://cdif.org/0.1/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "prov": "http://www.w3.org/ns/prov#",
    "spdx": "http://spdx.org/rdf/terms#",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "dcterms": "http://purl.org/dc/terms/",
    "ex": "https://example.org/",
    "dcat": "http://www.w3.org/ns/dcat#"
  },
  "@id": "ex:adaEMPA-P5",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "adaEMPA dataset for P5 (Frank et al. 2023 (Ivuna CAI, MAPS))",
  "schema:description": "Auto-generated adaEMPA profile-level Dataset for publication P5: Frank et al. 2023 (Ivuna CAI, MAPS). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p5); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes.",
  "schema:additionalType": [
    "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.PLACEHOLDER/adaempa-p5"
  },
  "schema:url": "https://astromat.org/products/adaempa-p5",
  "schema:dateModified": "2026-04-29",
  "schema:version": "0.1",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:creativeWorkStatus": "Draft",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Electron Microprobe Analysis (EMPA)",
    "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/EMPA"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-empa-p5",
      "schema:startDate": "2026-04-29",
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": [
            "nxs:BaseClass/NXinstrument",
            "ada:EMPAInstrument"
          ],
          "schema:name": "Cameca SX100",
          "schema:identifier": [
            "ex:instrument-empa-001"
          ],
          "schema:manufacturer": {
            "@type": [
              "schema:Organization"
            ],
            "schema:name": "Cameca"
          }
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "ARES, NASA Johnson Space Center",
        "schema:additionalType": [
          "nxs:BaseClass/NXsource"
        ]
      },
      "schema:object": [
        {
          "@type": [
            "schema:Thing",
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalType": [
            "MaterialSample"
          ],
          "schema:name": "Sample analyzed in P5",
          "schema:identifier": [
            "igsn:10.60471/PLACEHOLDER-P5"
          ],
          "schema:description": "Sample of: CAI minerals, melilite, grossmanite (Ti-Al pyroxene), spinel, hibonite, olivine, pyroxene"
        }
      ]
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "ex:adaEMPA-P5-var-Si",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Si",
      "schema:description": "Si abundance measured by EMPA WDS (10–50 s peak counting; calibrated against Kakanui kaersutite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Si"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P5-var-Al",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Al",
      "schema:description": "Al abundance measured by EMPA WDS (10–50 s peak counting; calibrated against Kakanui kaersutite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Al"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P5-var-Ti",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Ti",
      "schema:description": "Ti abundance measured by EMPA WDS (10–50 s peak counting; calibrated against Kakanui kaersutite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Ti"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P5-var-K",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "K",
      "schema:description": "K abundance measured by EMPA WDS (10–50 s peak counting; calibrated against Kakanui kaersutite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/K"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P5-var-Na",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Na",
      "schema:description": "Na abundance measured by EMPA WDS (10–50 s peak counting; calibrated against Kakanui kaersutite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Na"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P5-var-Fe",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Fe",
      "schema:description": "Fe abundance measured by EMPA WDS (10–50 s peak counting; calibrated against Kakanui kaersutite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Fe"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P5-var-Mg",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Mg",
      "schema:description": "Mg abundance measured by EMPA WDS (10–50 s peak counting; calibrated against Kakanui kaersutite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Mg"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P5-var-Ca",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Ca",
      "schema:description": "Ca abundance measured by EMPA WDS (10–50 s peak counting; calibrated against Kakanui kaersutite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Ca"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P5-var-S",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "S",
      "schema:description": "S abundance measured by EMPA WDS (10–50 s peak counting; calibrated against Canyon Diablo troilite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/S"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P5-var-Mn",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Mn",
      "schema:description": "Mn abundance measured by EMPA WDS (10–50 s peak counting; calibrated against Rhodonite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Mn"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P5-var-Cr",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Cr",
      "schema:description": "Cr abundance measured by EMPA WDS (10–50 s peak counting; calibrated against Chromium metal).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Cr"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P5-var-Ni",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Ni",
      "schema:description": "Ni abundance measured by EMPA WDS (10–50 s peak counting; calibrated against Nickel metal).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Ni"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P5-var-P",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "P",
      "schema:description": "P abundance measured by EMPA WDS (10–50 s peak counting; calibrated against Apatite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/P"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P5-var-V",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "V",
      "schema:description": "V abundance measured by EMPA WDS (10–50 s peak counting; calibrated against Vanadium metal).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/V"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "adaEMPA-P5-archive.zip",
      "schema:description": "Archive containing tabular EMPA data for P5.",
      "schema:contentUrl": "https://astromat.org/downloads/adaempa-p5.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "0000000000000000000000000000000000000000000000000000000000000000"
      },
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 1048576,
        "schema:unitText": "byte"
      },
      "schema:hasPart": [
        {
          "@id": "ex:adaEMPA-P5-data-001",
          "@type": [
            "schema:MediaObject",
            "ada:tabularData",
            "cdi:TabularTextDataSet",
            "schema:Thing"
          ],
          "schema:name": "adaEMPA-P5-data.csv",
          "schema:description": "Per-point quantitative EMPA analyses (Frank et al. 2023 (Ivuna CAI, MAPS)).",
          "schema:additionalType": [
            "ada:EMPAQEATabular"
          ],
          "schema:encodingFormat": [
            "text/csv"
          ],
          "cdi:isDelimited": true,
          "cdi:isFixedWidth": false,
          "csvw:delimiter": ",",
          "csvw:header": true,
          "ada:componentType": "ada:EMPAQEATabular",
          "ada:spectrometersUsed": "5x WDS",
          "ada:signalUsed": "Kα x-ray lines",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-p5"
          },
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/empaTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/acceleratingVoltage",
              "schema:name": "Default Accelerating Voltage",
              "schema:value": 20,
              "schema:unitText": "kV"
            },
            {
              "@id": "ada:parameter/empaTAPP/beamDiameter",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/beamDiameter",
              "schema:name": "Default Beam Diameter",
              "schema:value": "1 µm (focused)",
              "schema:unitText": "µm"
            },
            {
              "@id": "ada:parameter/empaTAPP/reportedAnalyte",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/reportedAnalyte",
              "schema:name": "Target Element",
              "schema:value": "Si|Al|Ti|K|Na|Fe|Mg|Ca|S|Mn|Cr|Ni|P|V"
            }
          ],
          "cdif:hasPhysicalMapping": [
            {
              "cdif:index": 0,
              "cdif:physicalDataType": "String",
              "cdi:nullSequence": "NA"
            }
          ]
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:adaEMPA-P5-metadata",
    "schema:about": {
      "@id": "ex:adaEMPA-P5"
    },
    "schema:dateModified": "2026-04-29",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaEMPA"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaProduct"
      }
    ],
    "schema:maintainer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Astromat Data Archive"
    },
    "schema:sdDatePublished": "2026-04-29T12:00:00Z"
  }
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
      "csvw": "http://www.w3.org/ns/csvw#",
      "prov": "http://www.w3.org/ns/prov#",
      "dcterms": "http://purl.org/dc/terms/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/profiles/adaProfiles/adaEMPA/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://cdif.org/0.1/",
      "csvw": "http://www.w3.org/ns/csvw#",
      "prov": "http://www.w3.org/ns/prov#",
      "spdx": "http://spdx.org/rdf/terms#",
      "nxs": "http://purl.org/nexusformat/definitions/",
      "dcterms": "http://purl.org/dc/terms/",
      "ex": "https://example.org/",
      "dcat": "http://www.w3.org/ns/dcat#"
    }
  ],
  "@id": "ex:adaEMPA-P5",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "adaEMPA dataset for P5 (Frank et al. 2023 (Ivuna CAI, MAPS))",
  "schema:description": "Auto-generated adaEMPA profile-level Dataset for publication P5: Frank et al. 2023 (Ivuna CAI, MAPS). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p5); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes.",
  "schema:additionalType": [
    "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.PLACEHOLDER/adaempa-p5"
  },
  "schema:url": "https://astromat.org/products/adaempa-p5",
  "schema:dateModified": "2026-04-29",
  "schema:version": "0.1",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:creativeWorkStatus": "Draft",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Electron Microprobe Analysis (EMPA)",
    "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/EMPA"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-empa-p5",
      "schema:startDate": "2026-04-29",
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": [
            "nxs:BaseClass/NXinstrument",
            "ada:EMPAInstrument"
          ],
          "schema:name": "Cameca SX100",
          "schema:identifier": [
            "ex:instrument-empa-001"
          ],
          "schema:manufacturer": {
            "@type": [
              "schema:Organization"
            ],
            "schema:name": "Cameca"
          }
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "ARES, NASA Johnson Space Center",
        "schema:additionalType": [
          "nxs:BaseClass/NXsource"
        ]
      },
      "schema:object": [
        {
          "@type": [
            "schema:Thing",
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalType": [
            "MaterialSample"
          ],
          "schema:name": "Sample analyzed in P5",
          "schema:identifier": [
            "igsn:10.60471/PLACEHOLDER-P5"
          ],
          "schema:description": "Sample of: CAI minerals, melilite, grossmanite (Ti-Al pyroxene), spinel, hibonite, olivine, pyroxene"
        }
      ]
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "ex:adaEMPA-P5-var-Si",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Si",
      "schema:description": "Si abundance measured by EMPA WDS (10\u201350 s peak counting; calibrated against Kakanui kaersutite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Si"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P5-var-Al",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Al",
      "schema:description": "Al abundance measured by EMPA WDS (10\u201350 s peak counting; calibrated against Kakanui kaersutite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Al"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P5-var-Ti",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Ti",
      "schema:description": "Ti abundance measured by EMPA WDS (10\u201350 s peak counting; calibrated against Kakanui kaersutite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Ti"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P5-var-K",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "K",
      "schema:description": "K abundance measured by EMPA WDS (10\u201350 s peak counting; calibrated against Kakanui kaersutite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/K"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P5-var-Na",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Na",
      "schema:description": "Na abundance measured by EMPA WDS (10\u201350 s peak counting; calibrated against Kakanui kaersutite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Na"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P5-var-Fe",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Fe",
      "schema:description": "Fe abundance measured by EMPA WDS (10\u201350 s peak counting; calibrated against Kakanui kaersutite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Fe"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P5-var-Mg",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Mg",
      "schema:description": "Mg abundance measured by EMPA WDS (10\u201350 s peak counting; calibrated against Kakanui kaersutite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Mg"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P5-var-Ca",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Ca",
      "schema:description": "Ca abundance measured by EMPA WDS (10\u201350 s peak counting; calibrated against Kakanui kaersutite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Ca"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P5-var-S",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "S",
      "schema:description": "S abundance measured by EMPA WDS (10\u201350 s peak counting; calibrated against Canyon Diablo troilite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/S"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P5-var-Mn",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Mn",
      "schema:description": "Mn abundance measured by EMPA WDS (10\u201350 s peak counting; calibrated against Rhodonite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Mn"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P5-var-Cr",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Cr",
      "schema:description": "Cr abundance measured by EMPA WDS (10\u201350 s peak counting; calibrated against Chromium metal).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Cr"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P5-var-Ni",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Ni",
      "schema:description": "Ni abundance measured by EMPA WDS (10\u201350 s peak counting; calibrated against Nickel metal).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Ni"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P5-var-P",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "P",
      "schema:description": "P abundance measured by EMPA WDS (10\u201350 s peak counting; calibrated against Apatite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/P"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P5-var-V",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "V",
      "schema:description": "V abundance measured by EMPA WDS (10\u201350 s peak counting; calibrated against Vanadium metal).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/V"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "adaEMPA-P5-archive.zip",
      "schema:description": "Archive containing tabular EMPA data for P5.",
      "schema:contentUrl": "https://astromat.org/downloads/adaempa-p5.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "0000000000000000000000000000000000000000000000000000000000000000"
      },
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 1048576,
        "schema:unitText": "byte"
      },
      "schema:hasPart": [
        {
          "@id": "ex:adaEMPA-P5-data-001",
          "@type": [
            "schema:MediaObject",
            "ada:tabularData",
            "cdi:TabularTextDataSet",
            "schema:Thing"
          ],
          "schema:name": "adaEMPA-P5-data.csv",
          "schema:description": "Per-point quantitative EMPA analyses (Frank et al. 2023 (Ivuna CAI, MAPS)).",
          "schema:additionalType": [
            "ada:EMPAQEATabular"
          ],
          "schema:encodingFormat": [
            "text/csv"
          ],
          "cdi:isDelimited": true,
          "cdi:isFixedWidth": false,
          "csvw:delimiter": ",",
          "csvw:header": true,
          "ada:componentType": "ada:EMPAQEATabular",
          "ada:spectrometersUsed": "5x WDS",
          "ada:signalUsed": "K\u03b1 x-ray lines",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-p5"
          },
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/empaTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/acceleratingVoltage",
              "schema:name": "Default Accelerating Voltage",
              "schema:value": 20,
              "schema:unitText": "kV"
            },
            {
              "@id": "ada:parameter/empaTAPP/beamDiameter",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/beamDiameter",
              "schema:name": "Default Beam Diameter",
              "schema:value": "1 \u00b5m (focused)",
              "schema:unitText": "\u00b5m"
            },
            {
              "@id": "ada:parameter/empaTAPP/reportedAnalyte",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/reportedAnalyte",
              "schema:name": "Target Element",
              "schema:value": "Si|Al|Ti|K|Na|Fe|Mg|Ca|S|Mn|Cr|Ni|P|V"
            }
          ],
          "cdif:hasPhysicalMapping": [
            {
              "cdif:index": 0,
              "cdif:physicalDataType": "String",
              "cdi:nullSequence": "NA"
            }
          ]
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:adaEMPA-P5-metadata",
    "schema:about": {
      "@id": "ex:adaEMPA-P5"
    },
    "schema:dateModified": "2026-04-29",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaEMPA"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaProduct"
      }
    ],
    "schema:maintainer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Astromat Data Archive"
    },
    "schema:sdDatePublished": "2026-04-29T12:00:00Z"
  }
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://cdif.org/0.1/> .
@prefix csvw: <http://www.w3.org/ns/csvw#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix spdx: <http://spdx.org/rdf/terms#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://ada.astromat.org/metadata/parameter/empaTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:name "Default Accelerating Voltage" ;
    schema1:propertyID "ada:parameter/empaTAPP/acceleratingVoltage" ;
    schema1:unitText "kV" ;
    schema1:value 20 .

<https://ada.astromat.org/metadata/parameter/empaTAPP/beamDiameter> a schema1:PropertyValue ;
    schema1:name "Default Beam Diameter" ;
    schema1:propertyID "ada:parameter/empaTAPP/beamDiameter" ;
    schema1:unitText "µm" ;
    schema1:value "1 µm (focused)" .

<https://ada.astromat.org/metadata/parameter/empaTAPP/reportedAnalyte> a schema1:PropertyValue ;
    schema1:name "Target Element" ;
    schema1:propertyID "ada:parameter/empaTAPP/reportedAnalyte" ;
    schema1:value "Si|Al|Ti|K|Na|Fe|Mg|Ca|S|Mn|Cr|Ni|P|V" .

ex:adaEMPA-P5 a schema1:Dataset,
        schema1:Product ;
    schema1:additionalType "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
        "ada:DataDeliveryPackage" ;
    schema1:creativeWorkStatus "Draft" ;
    schema1:dateModified "2026-04-29" ;
    schema1:description "Auto-generated adaEMPA profile-level Dataset for publication P5: Frank et al. 2023 (Ivuna CAI, MAPS). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p5); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes." ;
    schema1:distribution [ a schema1:DataDownload ;
            schema1:contentUrl "https://astromat.org/downloads/adaempa-p5.zip" ;
            schema1:description "Archive containing tabular EMPA data for P5." ;
            schema1:encodingFormat "application/zip" ;
            schema1:hasPart ex:adaEMPA-P5-data-001 ;
            schema1:name "adaEMPA-P5-archive.zip" ;
            schema1:size [ a schema1:QuantitativeValue ;
                    schema1:unitText "byte" ;
                    schema1:value 1048576 ] ;
            spdx:checksum [ a spdx:Checksum ;
                    spdx:algorithm "SHA256" ;
                    spdx:checksumValue "0000000000000000000000000000000000000000000000000000000000000000" ] ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://registry.identifiers.org/registry/doi" ;
            schema1:value "10.PLACEHOLDER/adaempa-p5" ] ;
    schema1:license "https://creativecommons.org/licenses/by/4.0/" ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:identifier "https://ada.astromat.org/vocabulary/techniques/EMPA" ;
            schema1:name "Electron Microprobe Analysis (EMPA)" ] ;
    schema1:name "adaEMPA dataset for P5 (Frank et al. 2023 (Ivuna CAI, MAPS))" ;
    schema1:subjectOf ex:adaEMPA-P5-metadata ;
    schema1:url "https://astromat.org/products/adaempa-p5" ;
    schema1:variableMeasured ex:adaEMPA-P5-var-Al,
        ex:adaEMPA-P5-var-Ca,
        ex:adaEMPA-P5-var-Cr,
        ex:adaEMPA-P5-var-Fe,
        ex:adaEMPA-P5-var-K,
        ex:adaEMPA-P5-var-Mg,
        ex:adaEMPA-P5-var-Mn,
        ex:adaEMPA-P5-var-Na,
        ex:adaEMPA-P5-var-Ni,
        ex:adaEMPA-P5-var-P,
        ex:adaEMPA-P5-var-S,
        ex:adaEMPA-P5-var-Si,
        ex:adaEMPA-P5-var-Ti,
        ex:adaEMPA-P5-var-V ;
    schema1:version "0.1" ;
    prov:wasGeneratedBy [ a schema1:Action,
                prov:Activity ;
            schema1:identifier "session-empa-p5" ;
            schema1:location [ a schema1:Place ;
                    schema1:additionalType "nxs:BaseClass/NXsource" ;
                    schema1:name "ARES, NASA Johnson Space Center" ] ;
            schema1:object [ a schema1:Thing,
                        <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalType "MaterialSample" ;
                    schema1:description "Sample of: CAI minerals, melilite, grossmanite (Ti-Al pyroxene), spinel, hibonite, olivine, pyroxene" ;
                    schema1:identifier "igsn:10.60471/PLACEHOLDER-P5" ;
                    schema1:name "Sample analyzed in P5" ] ;
            schema1:startDate "2026-04-29" ;
            prov:used [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType "ada:EMPAInstrument",
                        "nxs:BaseClass/NXinstrument" ;
                    schema1:identifier "ex:instrument-empa-001" ;
                    schema1:manufacturer [ a schema1:Organization ;
                            schema1:name "Cameca" ] ;
                    schema1:name "Cameca SX100" ] ] .

ex:adaEMPA-P5-data-001 a cdi:TabularTextDataSet,
        schema1:MediaObject,
        schema1:Thing,
        ada:tabularData ;
    cdi:isDelimited true ;
    cdi:isFixedWidth false ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/empaTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/empaTAPP/beamDiameter>,
        <https://ada.astromat.org/metadata/parameter/empaTAPP/reportedAnalyte> ;
    schema1:additionalType "ada:EMPAQEATabular" ;
    schema1:description "Per-point quantitative EMPA analyses (Frank et al. 2023 (Ivuna CAI, MAPS))." ;
    schema1:encodingFormat "text/csv" ;
    schema1:measurementTechnique ex:empaTAPP-p5 ;
    schema1:name "adaEMPA-P5-data.csv" ;
    csvw:delimiter "," ;
    csvw:header true ;
    ada:componentType "ada:EMPAQEATabular" ;
    ada:signalUsed "Kα x-ray lines" ;
    ada:spectrometersUsed "5x WDS" ;
    cdif:hasPhysicalMapping [ cdi:nullSequence "NA" ;
            cdif:index 0 ;
            cdif:physicalDataType "String" ] .

ex:adaEMPA-P5-metadata a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.0>,
        <https://w3id.org/cdif/data_description/1.0>,
        <https://w3id.org/cdif/discovery/1.0>,
        <https://w3id.org/cdif/manifest/1.0>,
        <https://w3id.org/cdif/provenance/1.0>,
        <https://w3id.org/geochem/metadata/profiles/adaEMPA>,
        <https://w3id.org/geochem/metadata/profiles/adaProduct> ;
    schema1:about ex:adaEMPA-P5 ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:dateModified "2026-04-29" ;
    schema1:maintainer [ a schema1:Organization ;
            schema1:name "Astromat Data Archive" ] ;
    schema1:sdDatePublished "2026-04-29T12:00:00Z" .

ex:adaEMPA-P5-var-Al a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Al abundance measured by EMPA WDS (10–50 s peak counting; calibrated against Kakanui kaersutite)." ;
    schema1:name "Al" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Al" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P5-var-Ca a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Ca abundance measured by EMPA WDS (10–50 s peak counting; calibrated against Kakanui kaersutite)." ;
    schema1:name "Ca" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Ca" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P5-var-Cr a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Cr abundance measured by EMPA WDS (10–50 s peak counting; calibrated against Chromium metal)." ;
    schema1:name "Cr" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Cr" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P5-var-Fe a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Fe abundance measured by EMPA WDS (10–50 s peak counting; calibrated against Kakanui kaersutite)." ;
    schema1:name "Fe" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Fe" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P5-var-K a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "K abundance measured by EMPA WDS (10–50 s peak counting; calibrated against Kakanui kaersutite)." ;
    schema1:name "K" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/K" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P5-var-Mg a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Mg abundance measured by EMPA WDS (10–50 s peak counting; calibrated against Kakanui kaersutite)." ;
    schema1:name "Mg" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Mg" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P5-var-Mn a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Mn abundance measured by EMPA WDS (10–50 s peak counting; calibrated against Rhodonite)." ;
    schema1:name "Mn" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Mn" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P5-var-Na a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Na abundance measured by EMPA WDS (10–50 s peak counting; calibrated against Kakanui kaersutite)." ;
    schema1:name "Na" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Na" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P5-var-Ni a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Ni abundance measured by EMPA WDS (10–50 s peak counting; calibrated against Nickel metal)." ;
    schema1:name "Ni" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Ni" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P5-var-P a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "P abundance measured by EMPA WDS (10–50 s peak counting; calibrated against Apatite)." ;
    schema1:name "P" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/P" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P5-var-S a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "S abundance measured by EMPA WDS (10–50 s peak counting; calibrated against Canyon Diablo troilite)." ;
    schema1:name "S" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/S" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P5-var-Si a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Si abundance measured by EMPA WDS (10–50 s peak counting; calibrated against Kakanui kaersutite)." ;
    schema1:name "Si" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Si" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P5-var-Ti a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Ti abundance measured by EMPA WDS (10–50 s peak counting; calibrated against Kakanui kaersutite)." ;
    schema1:name "Ti" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Ti" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P5-var-V a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "V abundance measured by EMPA WDS (10–50 s peak counting; calibrated against Vanadium metal)." ;
    schema1:name "V" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/V" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .


```


### adaEMPA — P6 (Broussard et al. 2026 (OC002 CI chondrite, MAPS))
Auto-generated adaEMPA dataset record for publication P6.
schema:variableMeasured is derived from the empaTAPP TAPP definition's
ada:defaultAnalytes; schema:hasPart carries the paired detailEMPA fields
and references the TAPP via schema:measurementTechnique. Synthetic
placeholders are used for DOI, file size, and dates.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://cdif.org/0.1/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "prov": "http://www.w3.org/ns/prov#",
    "spdx": "http://spdx.org/rdf/terms#",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "dcterms": "http://purl.org/dc/terms/",
    "ex": "https://example.org/",
    "dcat": "http://www.w3.org/ns/dcat#"
  },
  "@id": "ex:adaEMPA-P6",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "adaEMPA dataset for P6 (Broussard et al. 2026 (OC002 CI chondrite, MAPS))",
  "schema:description": "Auto-generated adaEMPA profile-level Dataset for publication P6: Broussard et al. 2026 (OC002 CI chondrite, MAPS). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p6); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes.",
  "schema:additionalType": [
    "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.PLACEHOLDER/adaempa-p6"
  },
  "schema:url": "https://astromat.org/products/adaempa-p6",
  "schema:dateModified": "2026-04-29",
  "schema:version": "0.1",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:creativeWorkStatus": "Draft",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Electron Microprobe Analysis (EMPA)",
    "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/EMPA"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-empa-p6",
      "schema:startDate": "2026-04-29",
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": [
            "nxs:BaseClass/NXinstrument",
            "ada:EMPAInstrument"
          ],
          "schema:name": "JEOL JXA-8200",
          "schema:identifier": [
            "ex:instrument-empa-001"
          ],
          "schema:manufacturer": {
            "@type": [
              "schema:Organization"
            ],
            "schema:name": "JEOL"
          }
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Washington University in St. Louis",
        "schema:additionalType": [
          "nxs:BaseClass/NXsource"
        ]
      },
      "schema:object": [
        {
          "@type": [
            "schema:Thing",
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalType": [
            "MaterialSample"
          ],
          "schema:name": "Sample analyzed in P6",
          "schema:identifier": [
            "igsn:10.60471/PLACEHOLDER-P6"
          ],
          "schema:description": "Sample of: Phyllosilicates, magnetite, dolomite, magnesite, pyrrhotite, pentlandite, apatite, fluorapatite, hydroxyapatite, ilmenite, chromite"
        }
      ]
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "ex:adaEMPA-P6-var-F",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "F",
      "schema:description": "F abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/F"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P6-var-CO2",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "CO2",
      "schema:description": "CO2 abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/CO2"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "adaEMPA-P6-archive.zip",
      "schema:description": "Archive containing tabular EMPA data for P6.",
      "schema:contentUrl": "https://astromat.org/downloads/adaempa-p6.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "0000000000000000000000000000000000000000000000000000000000000000"
      },
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 1048576,
        "schema:unitText": "byte"
      },
      "schema:hasPart": [
        {
          "@id": "ex:adaEMPA-P6-data-001",
          "@type": [
            "schema:MediaObject",
            "ada:tabularData",
            "cdi:TabularTextDataSet",
            "schema:Thing"
          ],
          "schema:name": "adaEMPA-P6-data.csv",
          "schema:description": "Per-point quantitative EMPA analyses (Broussard et al. 2026 (OC002 CI chondrite, MAPS)).",
          "schema:additionalType": [
            "ada:EMPAQEATabular"
          ],
          "schema:encodingFormat": [
            "text/csv"
          ],
          "cdi:isDelimited": true,
          "cdi:isFixedWidth": false,
          "csvw:delimiter": ",",
          "csvw:header": true,
          "ada:componentType": "ada:EMPAQEATabular",
          "ada:spectrometersUsed": "5x WDS",
          "ada:signalUsed": "Kα x-ray lines",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-p6"
          },
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/empaTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/acceleratingVoltage",
              "schema:name": "Default Accelerating Voltage",
              "schema:value": 15,
              "schema:unitText": "kV"
            },
            {
              "@id": "ada:parameter/empaTAPP/beamDiameter",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/beamDiameter",
              "schema:name": "Default Beam Diameter",
              "schema:value": "0 (focused)",
              "schema:unitText": "µm"
            },
            {
              "@id": "ada:parameter/empaTAPP/reportedAnalyte",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/reportedAnalyte",
              "schema:name": "Target Element",
              "schema:value": "F|CO2"
            }
          ],
          "cdif:hasPhysicalMapping": [
            {
              "cdif:index": 0,
              "cdif:physicalDataType": "String",
              "cdi:nullSequence": "NA"
            }
          ]
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:adaEMPA-P6-metadata",
    "schema:about": {
      "@id": "ex:adaEMPA-P6"
    },
    "schema:dateModified": "2026-04-29",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaEMPA"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaProduct"
      }
    ],
    "schema:maintainer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Astromat Data Archive"
    },
    "schema:sdDatePublished": "2026-04-29T12:00:00Z"
  }
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
      "csvw": "http://www.w3.org/ns/csvw#",
      "prov": "http://www.w3.org/ns/prov#",
      "dcterms": "http://purl.org/dc/terms/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/profiles/adaProfiles/adaEMPA/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://cdif.org/0.1/",
      "csvw": "http://www.w3.org/ns/csvw#",
      "prov": "http://www.w3.org/ns/prov#",
      "spdx": "http://spdx.org/rdf/terms#",
      "nxs": "http://purl.org/nexusformat/definitions/",
      "dcterms": "http://purl.org/dc/terms/",
      "ex": "https://example.org/",
      "dcat": "http://www.w3.org/ns/dcat#"
    }
  ],
  "@id": "ex:adaEMPA-P6",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "adaEMPA dataset for P6 (Broussard et al. 2026 (OC002 CI chondrite, MAPS))",
  "schema:description": "Auto-generated adaEMPA profile-level Dataset for publication P6: Broussard et al. 2026 (OC002 CI chondrite, MAPS). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p6); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes.",
  "schema:additionalType": [
    "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.PLACEHOLDER/adaempa-p6"
  },
  "schema:url": "https://astromat.org/products/adaempa-p6",
  "schema:dateModified": "2026-04-29",
  "schema:version": "0.1",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:creativeWorkStatus": "Draft",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Electron Microprobe Analysis (EMPA)",
    "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/EMPA"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-empa-p6",
      "schema:startDate": "2026-04-29",
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": [
            "nxs:BaseClass/NXinstrument",
            "ada:EMPAInstrument"
          ],
          "schema:name": "JEOL JXA-8200",
          "schema:identifier": [
            "ex:instrument-empa-001"
          ],
          "schema:manufacturer": {
            "@type": [
              "schema:Organization"
            ],
            "schema:name": "JEOL"
          }
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Washington University in St. Louis",
        "schema:additionalType": [
          "nxs:BaseClass/NXsource"
        ]
      },
      "schema:object": [
        {
          "@type": [
            "schema:Thing",
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalType": [
            "MaterialSample"
          ],
          "schema:name": "Sample analyzed in P6",
          "schema:identifier": [
            "igsn:10.60471/PLACEHOLDER-P6"
          ],
          "schema:description": "Sample of: Phyllosilicates, magnetite, dolomite, magnesite, pyrrhotite, pentlandite, apatite, fluorapatite, hydroxyapatite, ilmenite, chromite"
        }
      ]
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "ex:adaEMPA-P6-var-F",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "F",
      "schema:description": "F abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/F"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P6-var-CO2",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "CO2",
      "schema:description": "CO2 abundance measured by EMPA WDS.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/CO2"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "adaEMPA-P6-archive.zip",
      "schema:description": "Archive containing tabular EMPA data for P6.",
      "schema:contentUrl": "https://astromat.org/downloads/adaempa-p6.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "0000000000000000000000000000000000000000000000000000000000000000"
      },
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 1048576,
        "schema:unitText": "byte"
      },
      "schema:hasPart": [
        {
          "@id": "ex:adaEMPA-P6-data-001",
          "@type": [
            "schema:MediaObject",
            "ada:tabularData",
            "cdi:TabularTextDataSet",
            "schema:Thing"
          ],
          "schema:name": "adaEMPA-P6-data.csv",
          "schema:description": "Per-point quantitative EMPA analyses (Broussard et al. 2026 (OC002 CI chondrite, MAPS)).",
          "schema:additionalType": [
            "ada:EMPAQEATabular"
          ],
          "schema:encodingFormat": [
            "text/csv"
          ],
          "cdi:isDelimited": true,
          "cdi:isFixedWidth": false,
          "csvw:delimiter": ",",
          "csvw:header": true,
          "ada:componentType": "ada:EMPAQEATabular",
          "ada:spectrometersUsed": "5x WDS",
          "ada:signalUsed": "K\u03b1 x-ray lines",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-p6"
          },
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/empaTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/acceleratingVoltage",
              "schema:name": "Default Accelerating Voltage",
              "schema:value": 15,
              "schema:unitText": "kV"
            },
            {
              "@id": "ada:parameter/empaTAPP/beamDiameter",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/beamDiameter",
              "schema:name": "Default Beam Diameter",
              "schema:value": "0 (focused)",
              "schema:unitText": "\u00b5m"
            },
            {
              "@id": "ada:parameter/empaTAPP/reportedAnalyte",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/reportedAnalyte",
              "schema:name": "Target Element",
              "schema:value": "F|CO2"
            }
          ],
          "cdif:hasPhysicalMapping": [
            {
              "cdif:index": 0,
              "cdif:physicalDataType": "String",
              "cdi:nullSequence": "NA"
            }
          ]
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:adaEMPA-P6-metadata",
    "schema:about": {
      "@id": "ex:adaEMPA-P6"
    },
    "schema:dateModified": "2026-04-29",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaEMPA"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaProduct"
      }
    ],
    "schema:maintainer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Astromat Data Archive"
    },
    "schema:sdDatePublished": "2026-04-29T12:00:00Z"
  }
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://cdif.org/0.1/> .
@prefix csvw: <http://www.w3.org/ns/csvw#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix spdx: <http://spdx.org/rdf/terms#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://ada.astromat.org/metadata/parameter/empaTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:name "Default Accelerating Voltage" ;
    schema1:propertyID "ada:parameter/empaTAPP/acceleratingVoltage" ;
    schema1:unitText "kV" ;
    schema1:value 15 .

<https://ada.astromat.org/metadata/parameter/empaTAPP/beamDiameter> a schema1:PropertyValue ;
    schema1:name "Default Beam Diameter" ;
    schema1:propertyID "ada:parameter/empaTAPP/beamDiameter" ;
    schema1:unitText "µm" ;
    schema1:value "0 (focused)" .

<https://ada.astromat.org/metadata/parameter/empaTAPP/reportedAnalyte> a schema1:PropertyValue ;
    schema1:name "Target Element" ;
    schema1:propertyID "ada:parameter/empaTAPP/reportedAnalyte" ;
    schema1:value "F|CO2" .

ex:adaEMPA-P6 a schema1:Dataset,
        schema1:Product ;
    schema1:additionalType "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
        "ada:DataDeliveryPackage" ;
    schema1:creativeWorkStatus "Draft" ;
    schema1:dateModified "2026-04-29" ;
    schema1:description "Auto-generated adaEMPA profile-level Dataset for publication P6: Broussard et al. 2026 (OC002 CI chondrite, MAPS). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p6); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes." ;
    schema1:distribution [ a schema1:DataDownload ;
            schema1:contentUrl "https://astromat.org/downloads/adaempa-p6.zip" ;
            schema1:description "Archive containing tabular EMPA data for P6." ;
            schema1:encodingFormat "application/zip" ;
            schema1:hasPart ex:adaEMPA-P6-data-001 ;
            schema1:name "adaEMPA-P6-archive.zip" ;
            schema1:size [ a schema1:QuantitativeValue ;
                    schema1:unitText "byte" ;
                    schema1:value 1048576 ] ;
            spdx:checksum [ a spdx:Checksum ;
                    spdx:algorithm "SHA256" ;
                    spdx:checksumValue "0000000000000000000000000000000000000000000000000000000000000000" ] ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://registry.identifiers.org/registry/doi" ;
            schema1:value "10.PLACEHOLDER/adaempa-p6" ] ;
    schema1:license "https://creativecommons.org/licenses/by/4.0/" ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:identifier "https://ada.astromat.org/vocabulary/techniques/EMPA" ;
            schema1:name "Electron Microprobe Analysis (EMPA)" ] ;
    schema1:name "adaEMPA dataset for P6 (Broussard et al. 2026 (OC002 CI chondrite, MAPS))" ;
    schema1:subjectOf ex:adaEMPA-P6-metadata ;
    schema1:url "https://astromat.org/products/adaempa-p6" ;
    schema1:variableMeasured ex:adaEMPA-P6-var-CO2,
        ex:adaEMPA-P6-var-F ;
    schema1:version "0.1" ;
    prov:wasGeneratedBy [ a schema1:Action,
                prov:Activity ;
            schema1:identifier "session-empa-p6" ;
            schema1:location [ a schema1:Place ;
                    schema1:additionalType "nxs:BaseClass/NXsource" ;
                    schema1:name "Washington University in St. Louis" ] ;
            schema1:object [ a schema1:Thing,
                        <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalType "MaterialSample" ;
                    schema1:description "Sample of: Phyllosilicates, magnetite, dolomite, magnesite, pyrrhotite, pentlandite, apatite, fluorapatite, hydroxyapatite, ilmenite, chromite" ;
                    schema1:identifier "igsn:10.60471/PLACEHOLDER-P6" ;
                    schema1:name "Sample analyzed in P6" ] ;
            schema1:startDate "2026-04-29" ;
            prov:used [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType "ada:EMPAInstrument",
                        "nxs:BaseClass/NXinstrument" ;
                    schema1:identifier "ex:instrument-empa-001" ;
                    schema1:manufacturer [ a schema1:Organization ;
                            schema1:name "JEOL" ] ;
                    schema1:name "JEOL JXA-8200" ] ] .

ex:adaEMPA-P6-data-001 a cdi:TabularTextDataSet,
        schema1:MediaObject,
        schema1:Thing,
        ada:tabularData ;
    cdi:isDelimited true ;
    cdi:isFixedWidth false ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/empaTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/empaTAPP/beamDiameter>,
        <https://ada.astromat.org/metadata/parameter/empaTAPP/reportedAnalyte> ;
    schema1:additionalType "ada:EMPAQEATabular" ;
    schema1:description "Per-point quantitative EMPA analyses (Broussard et al. 2026 (OC002 CI chondrite, MAPS))." ;
    schema1:encodingFormat "text/csv" ;
    schema1:measurementTechnique ex:empaTAPP-p6 ;
    schema1:name "adaEMPA-P6-data.csv" ;
    csvw:delimiter "," ;
    csvw:header true ;
    ada:componentType "ada:EMPAQEATabular" ;
    ada:signalUsed "Kα x-ray lines" ;
    ada:spectrometersUsed "5x WDS" ;
    cdif:hasPhysicalMapping [ cdi:nullSequence "NA" ;
            cdif:index 0 ;
            cdif:physicalDataType "String" ] .

ex:adaEMPA-P6-metadata a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.0>,
        <https://w3id.org/cdif/data_description/1.0>,
        <https://w3id.org/cdif/discovery/1.0>,
        <https://w3id.org/cdif/manifest/1.0>,
        <https://w3id.org/cdif/provenance/1.0>,
        <https://w3id.org/geochem/metadata/profiles/adaEMPA>,
        <https://w3id.org/geochem/metadata/profiles/adaProduct> ;
    schema1:about ex:adaEMPA-P6 ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:dateModified "2026-04-29" ;
    schema1:maintainer [ a schema1:Organization ;
            schema1:name "Astromat Data Archive" ] ;
    schema1:sdDatePublished "2026-04-29T12:00:00Z" .

ex:adaEMPA-P6-var-CO2 a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "CO2 abundance measured by EMPA WDS." ;
    schema1:name "CO2" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/CO2" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P6-var-F a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "F abundance measured by EMPA WDS." ;
    schema1:name "F" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/F" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .


```


### adaEMPA — P7 (Seifert et al. 2026 (Bennu apatite, MAPS))
Auto-generated adaEMPA dataset record for publication P7.
schema:variableMeasured is derived from the empaTAPP TAPP definition's
ada:defaultAnalytes; schema:hasPart carries the paired detailEMPA fields
and references the TAPP via schema:measurementTechnique. Synthetic
placeholders are used for DOI, file size, and dates.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://cdif.org/0.1/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "prov": "http://www.w3.org/ns/prov#",
    "spdx": "http://spdx.org/rdf/terms#",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "dcterms": "http://purl.org/dc/terms/",
    "ex": "https://example.org/",
    "dcat": "http://www.w3.org/ns/dcat#"
  },
  "@id": "ex:adaEMPA-P7",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "adaEMPA dataset for P7 (Seifert et al. 2026 (Bennu apatite, MAPS))",
  "schema:description": "Auto-generated adaEMPA profile-level Dataset for publication P7: Seifert et al. 2026 (Bennu apatite, MAPS). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p7); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes.",
  "schema:additionalType": [
    "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.PLACEHOLDER/adaempa-p7"
  },
  "schema:url": "https://astromat.org/products/adaempa-p7",
  "schema:dateModified": "2026-04-29",
  "schema:version": "0.1",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:creativeWorkStatus": "Draft",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Electron Microprobe Analysis (EMPA)",
    "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/EMPA"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-empa-p7",
      "schema:startDate": "2026-04-29",
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": [
            "nxs:BaseClass/NXinstrument",
            "ada:EMPAInstrument"
          ],
          "schema:name": "JEOL JEOL 8530 EMPA (Field Emission)",
          "schema:identifier": [
            "ex:instrument-empa-001"
          ],
          "schema:manufacturer": {
            "@type": [
              "schema:Organization"
            ],
            "schema:name": "JEOL"
          }
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "NASA Johnson Space Center (JSC)",
        "schema:additionalType": [
          "nxs:BaseClass/NXsource"
        ]
      },
      "schema:object": [
        {
          "@type": [
            "schema:Thing",
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalType": [
            "MaterialSample"
          ],
          "schema:name": "Sample analyzed in P7",
          "schema:identifier": [
            "igsn:10.60471/PLACEHOLDER-P7"
          ],
          "schema:description": "Sample of: Apatite [Ca5(PO4)3(F,Cl,OH)]"
        }
      ]
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "ex:adaEMPA-P7-var-F",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "F",
      "schema:description": "F abundance measured by EMPA WDS (20 s peak time s peak counting; 10 s background s background counting; calibrated against SrF2).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/F"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P7-var-Na",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Na",
      "schema:description": "Na abundance measured by EMPA WDS (20 s peak time s peak counting; 10 s background s background counting; calibrated against albite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Na"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P7-var-Mg",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Mg",
      "schema:description": "Mg abundance measured by EMPA WDS (20 s peak time s peak counting; 10 s background s background counting; calibrated against SW olivine).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Mg"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P7-var-Si",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Si",
      "schema:description": "Si abundance measured by EMPA WDS (20 s peak time s peak counting; 10 s background s background counting; calibrated against quartz).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Si"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P7-var-P",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "P",
      "schema:description": "P abundance measured by EMPA WDS (20 s peak time s peak counting; 10 s background s background counting; calibrated against Wilburforce apatite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/P"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P7-var-Ca",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Ca",
      "schema:description": "Ca abundance measured by EMPA WDS (20 s peak time s peak counting; 10 s background s background counting; calibrated against Wilburforce apatite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Ca"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P7-var-S",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "S",
      "schema:description": "S abundance measured by EMPA WDS (20 s peak time s peak counting; 10 s background s background counting; calibrated against barite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/S"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P7-var-Cl",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Cl",
      "schema:description": "Cl abundance measured by EMPA WDS (20 s peak time s peak counting; 10 s background s background counting; calibrated against tugtupite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Cl"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P7-var-Mn",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Mn",
      "schema:description": "Mn abundance measured by EMPA WDS (20 s peak time s peak counting; 10 s background s background counting; calibrated against rhodonite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Mn"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P7-var-Fe",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Fe",
      "schema:description": "Fe abundance measured by EMPA WDS (20 s peak time s peak counting; 10 s background s background counting; calibrated against ilmenite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Fe"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P7-var-OH",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "OH",
      "schema:description": "OH abundance measured by EMPA WDS (20 s peak time s peak counting; 10 s background s background counting).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/OH"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "adaEMPA-P7-archive.zip",
      "schema:description": "Archive containing tabular EMPA data for P7.",
      "schema:contentUrl": "https://astromat.org/downloads/adaempa-p7.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "0000000000000000000000000000000000000000000000000000000000000000"
      },
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 1048576,
        "schema:unitText": "byte"
      },
      "schema:hasPart": [
        {
          "@id": "ex:adaEMPA-P7-data-001",
          "@type": [
            "schema:MediaObject",
            "ada:tabularData",
            "cdi:TabularTextDataSet",
            "schema:Thing"
          ],
          "schema:name": "adaEMPA-P7-data.csv",
          "schema:description": "Per-point quantitative EMPA analyses (Seifert et al. 2026 (Bennu apatite, MAPS)).",
          "schema:additionalType": [
            "ada:EMPAQEATabular"
          ],
          "schema:encodingFormat": [
            "text/csv"
          ],
          "cdi:isDelimited": true,
          "cdi:isFixedWidth": false,
          "csvw:delimiter": ",",
          "csvw:header": true,
          "ada:componentType": "ada:EMPAQEATabular",
          "ada:spectrometersUsed": "5x WDS",
          "ada:signalUsed": "Kα x-ray lines",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-p7"
          },
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/empaTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/acceleratingVoltage",
              "schema:name": "Default Accelerating Voltage",
              "schema:value": 15,
              "schema:unitText": "kV"
            },
            {
              "@id": "ada:parameter/empaTAPP/beamDiameter",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/beamDiameter",
              "schema:name": "Default Beam Diameter",
              "schema:value": "2 µm",
              "schema:unitText": "µm"
            },
            {
              "@id": "ada:parameter/empaTAPP/reportedAnalyte",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/reportedAnalyte",
              "schema:name": "Target Element",
              "schema:value": "F|Na|Mg|Si|P|Ca|S|Cl|Mn|Fe|OH"
            }
          ],
          "cdif:hasPhysicalMapping": [
            {
              "cdif:index": 0,
              "cdif:physicalDataType": "String",
              "cdi:nullSequence": "NA"
            }
          ]
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:adaEMPA-P7-metadata",
    "schema:about": {
      "@id": "ex:adaEMPA-P7"
    },
    "schema:dateModified": "2026-04-29",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaEMPA"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaProduct"
      }
    ],
    "schema:maintainer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Astromat Data Archive"
    },
    "schema:sdDatePublished": "2026-04-29T12:00:00Z"
  }
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
      "csvw": "http://www.w3.org/ns/csvw#",
      "prov": "http://www.w3.org/ns/prov#",
      "dcterms": "http://purl.org/dc/terms/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/profiles/adaProfiles/adaEMPA/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://cdif.org/0.1/",
      "csvw": "http://www.w3.org/ns/csvw#",
      "prov": "http://www.w3.org/ns/prov#",
      "spdx": "http://spdx.org/rdf/terms#",
      "nxs": "http://purl.org/nexusformat/definitions/",
      "dcterms": "http://purl.org/dc/terms/",
      "ex": "https://example.org/",
      "dcat": "http://www.w3.org/ns/dcat#"
    }
  ],
  "@id": "ex:adaEMPA-P7",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "adaEMPA dataset for P7 (Seifert et al. 2026 (Bennu apatite, MAPS))",
  "schema:description": "Auto-generated adaEMPA profile-level Dataset for publication P7: Seifert et al. 2026 (Bennu apatite, MAPS). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p7); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes.",
  "schema:additionalType": [
    "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.PLACEHOLDER/adaempa-p7"
  },
  "schema:url": "https://astromat.org/products/adaempa-p7",
  "schema:dateModified": "2026-04-29",
  "schema:version": "0.1",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:creativeWorkStatus": "Draft",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Electron Microprobe Analysis (EMPA)",
    "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/EMPA"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-empa-p7",
      "schema:startDate": "2026-04-29",
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": [
            "nxs:BaseClass/NXinstrument",
            "ada:EMPAInstrument"
          ],
          "schema:name": "JEOL JEOL 8530 EMPA (Field Emission)",
          "schema:identifier": [
            "ex:instrument-empa-001"
          ],
          "schema:manufacturer": {
            "@type": [
              "schema:Organization"
            ],
            "schema:name": "JEOL"
          }
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "NASA Johnson Space Center (JSC)",
        "schema:additionalType": [
          "nxs:BaseClass/NXsource"
        ]
      },
      "schema:object": [
        {
          "@type": [
            "schema:Thing",
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalType": [
            "MaterialSample"
          ],
          "schema:name": "Sample analyzed in P7",
          "schema:identifier": [
            "igsn:10.60471/PLACEHOLDER-P7"
          ],
          "schema:description": "Sample of: Apatite [Ca5(PO4)3(F,Cl,OH)]"
        }
      ]
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "ex:adaEMPA-P7-var-F",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "F",
      "schema:description": "F abundance measured by EMPA WDS (20 s peak time s peak counting; 10 s background s background counting; calibrated against SrF2).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/F"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P7-var-Na",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Na",
      "schema:description": "Na abundance measured by EMPA WDS (20 s peak time s peak counting; 10 s background s background counting; calibrated against albite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Na"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P7-var-Mg",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Mg",
      "schema:description": "Mg abundance measured by EMPA WDS (20 s peak time s peak counting; 10 s background s background counting; calibrated against SW olivine).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Mg"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P7-var-Si",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Si",
      "schema:description": "Si abundance measured by EMPA WDS (20 s peak time s peak counting; 10 s background s background counting; calibrated against quartz).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Si"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P7-var-P",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "P",
      "schema:description": "P abundance measured by EMPA WDS (20 s peak time s peak counting; 10 s background s background counting; calibrated against Wilburforce apatite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/P"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P7-var-Ca",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Ca",
      "schema:description": "Ca abundance measured by EMPA WDS (20 s peak time s peak counting; 10 s background s background counting; calibrated against Wilburforce apatite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Ca"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P7-var-S",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "S",
      "schema:description": "S abundance measured by EMPA WDS (20 s peak time s peak counting; 10 s background s background counting; calibrated against barite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/S"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P7-var-Cl",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Cl",
      "schema:description": "Cl abundance measured by EMPA WDS (20 s peak time s peak counting; 10 s background s background counting; calibrated against tugtupite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Cl"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P7-var-Mn",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Mn",
      "schema:description": "Mn abundance measured by EMPA WDS (20 s peak time s peak counting; 10 s background s background counting; calibrated against rhodonite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Mn"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P7-var-Fe",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Fe",
      "schema:description": "Fe abundance measured by EMPA WDS (20 s peak time s peak counting; 10 s background s background counting; calibrated against ilmenite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Fe"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P7-var-OH",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "OH",
      "schema:description": "OH abundance measured by EMPA WDS (20 s peak time s peak counting; 10 s background s background counting).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/OH"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "adaEMPA-P7-archive.zip",
      "schema:description": "Archive containing tabular EMPA data for P7.",
      "schema:contentUrl": "https://astromat.org/downloads/adaempa-p7.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "0000000000000000000000000000000000000000000000000000000000000000"
      },
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 1048576,
        "schema:unitText": "byte"
      },
      "schema:hasPart": [
        {
          "@id": "ex:adaEMPA-P7-data-001",
          "@type": [
            "schema:MediaObject",
            "ada:tabularData",
            "cdi:TabularTextDataSet",
            "schema:Thing"
          ],
          "schema:name": "adaEMPA-P7-data.csv",
          "schema:description": "Per-point quantitative EMPA analyses (Seifert et al. 2026 (Bennu apatite, MAPS)).",
          "schema:additionalType": [
            "ada:EMPAQEATabular"
          ],
          "schema:encodingFormat": [
            "text/csv"
          ],
          "cdi:isDelimited": true,
          "cdi:isFixedWidth": false,
          "csvw:delimiter": ",",
          "csvw:header": true,
          "ada:componentType": "ada:EMPAQEATabular",
          "ada:spectrometersUsed": "5x WDS",
          "ada:signalUsed": "K\u03b1 x-ray lines",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-p7"
          },
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/empaTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/acceleratingVoltage",
              "schema:name": "Default Accelerating Voltage",
              "schema:value": 15,
              "schema:unitText": "kV"
            },
            {
              "@id": "ada:parameter/empaTAPP/beamDiameter",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/beamDiameter",
              "schema:name": "Default Beam Diameter",
              "schema:value": "2 \u00b5m",
              "schema:unitText": "\u00b5m"
            },
            {
              "@id": "ada:parameter/empaTAPP/reportedAnalyte",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/reportedAnalyte",
              "schema:name": "Target Element",
              "schema:value": "F|Na|Mg|Si|P|Ca|S|Cl|Mn|Fe|OH"
            }
          ],
          "cdif:hasPhysicalMapping": [
            {
              "cdif:index": 0,
              "cdif:physicalDataType": "String",
              "cdi:nullSequence": "NA"
            }
          ]
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:adaEMPA-P7-metadata",
    "schema:about": {
      "@id": "ex:adaEMPA-P7"
    },
    "schema:dateModified": "2026-04-29",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaEMPA"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaProduct"
      }
    ],
    "schema:maintainer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Astromat Data Archive"
    },
    "schema:sdDatePublished": "2026-04-29T12:00:00Z"
  }
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://cdif.org/0.1/> .
@prefix csvw: <http://www.w3.org/ns/csvw#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix spdx: <http://spdx.org/rdf/terms#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://ada.astromat.org/metadata/parameter/empaTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:name "Default Accelerating Voltage" ;
    schema1:propertyID "ada:parameter/empaTAPP/acceleratingVoltage" ;
    schema1:unitText "kV" ;
    schema1:value 15 .

<https://ada.astromat.org/metadata/parameter/empaTAPP/beamDiameter> a schema1:PropertyValue ;
    schema1:name "Default Beam Diameter" ;
    schema1:propertyID "ada:parameter/empaTAPP/beamDiameter" ;
    schema1:unitText "µm" ;
    schema1:value "2 µm" .

<https://ada.astromat.org/metadata/parameter/empaTAPP/reportedAnalyte> a schema1:PropertyValue ;
    schema1:name "Target Element" ;
    schema1:propertyID "ada:parameter/empaTAPP/reportedAnalyte" ;
    schema1:value "F|Na|Mg|Si|P|Ca|S|Cl|Mn|Fe|OH" .

ex:adaEMPA-P7 a schema1:Dataset,
        schema1:Product ;
    schema1:additionalType "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
        "ada:DataDeliveryPackage" ;
    schema1:creativeWorkStatus "Draft" ;
    schema1:dateModified "2026-04-29" ;
    schema1:description "Auto-generated adaEMPA profile-level Dataset for publication P7: Seifert et al. 2026 (Bennu apatite, MAPS). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p7); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes." ;
    schema1:distribution [ a schema1:DataDownload ;
            schema1:contentUrl "https://astromat.org/downloads/adaempa-p7.zip" ;
            schema1:description "Archive containing tabular EMPA data for P7." ;
            schema1:encodingFormat "application/zip" ;
            schema1:hasPart ex:adaEMPA-P7-data-001 ;
            schema1:name "adaEMPA-P7-archive.zip" ;
            schema1:size [ a schema1:QuantitativeValue ;
                    schema1:unitText "byte" ;
                    schema1:value 1048576 ] ;
            spdx:checksum [ a spdx:Checksum ;
                    spdx:algorithm "SHA256" ;
                    spdx:checksumValue "0000000000000000000000000000000000000000000000000000000000000000" ] ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://registry.identifiers.org/registry/doi" ;
            schema1:value "10.PLACEHOLDER/adaempa-p7" ] ;
    schema1:license "https://creativecommons.org/licenses/by/4.0/" ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:identifier "https://ada.astromat.org/vocabulary/techniques/EMPA" ;
            schema1:name "Electron Microprobe Analysis (EMPA)" ] ;
    schema1:name "adaEMPA dataset for P7 (Seifert et al. 2026 (Bennu apatite, MAPS))" ;
    schema1:subjectOf ex:adaEMPA-P7-metadata ;
    schema1:url "https://astromat.org/products/adaempa-p7" ;
    schema1:variableMeasured ex:adaEMPA-P7-var-Ca,
        ex:adaEMPA-P7-var-Cl,
        ex:adaEMPA-P7-var-F,
        ex:adaEMPA-P7-var-Fe,
        ex:adaEMPA-P7-var-Mg,
        ex:adaEMPA-P7-var-Mn,
        ex:adaEMPA-P7-var-Na,
        ex:adaEMPA-P7-var-OH,
        ex:adaEMPA-P7-var-P,
        ex:adaEMPA-P7-var-S,
        ex:adaEMPA-P7-var-Si ;
    schema1:version "0.1" ;
    prov:wasGeneratedBy [ a schema1:Action,
                prov:Activity ;
            schema1:identifier "session-empa-p7" ;
            schema1:location [ a schema1:Place ;
                    schema1:additionalType "nxs:BaseClass/NXsource" ;
                    schema1:name "NASA Johnson Space Center (JSC)" ] ;
            schema1:object [ a schema1:Thing,
                        <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalType "MaterialSample" ;
                    schema1:description "Sample of: Apatite [Ca5(PO4)3(F,Cl,OH)]" ;
                    schema1:identifier "igsn:10.60471/PLACEHOLDER-P7" ;
                    schema1:name "Sample analyzed in P7" ] ;
            schema1:startDate "2026-04-29" ;
            prov:used [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType "ada:EMPAInstrument",
                        "nxs:BaseClass/NXinstrument" ;
                    schema1:identifier "ex:instrument-empa-001" ;
                    schema1:manufacturer [ a schema1:Organization ;
                            schema1:name "JEOL" ] ;
                    schema1:name "JEOL JEOL 8530 EMPA (Field Emission)" ] ] .

ex:adaEMPA-P7-data-001 a cdi:TabularTextDataSet,
        schema1:MediaObject,
        schema1:Thing,
        ada:tabularData ;
    cdi:isDelimited true ;
    cdi:isFixedWidth false ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/empaTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/empaTAPP/beamDiameter>,
        <https://ada.astromat.org/metadata/parameter/empaTAPP/reportedAnalyte> ;
    schema1:additionalType "ada:EMPAQEATabular" ;
    schema1:description "Per-point quantitative EMPA analyses (Seifert et al. 2026 (Bennu apatite, MAPS))." ;
    schema1:encodingFormat "text/csv" ;
    schema1:measurementTechnique ex:empaTAPP-p7 ;
    schema1:name "adaEMPA-P7-data.csv" ;
    csvw:delimiter "," ;
    csvw:header true ;
    ada:componentType "ada:EMPAQEATabular" ;
    ada:signalUsed "Kα x-ray lines" ;
    ada:spectrometersUsed "5x WDS" ;
    cdif:hasPhysicalMapping [ cdi:nullSequence "NA" ;
            cdif:index 0 ;
            cdif:physicalDataType "String" ] .

ex:adaEMPA-P7-metadata a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.0>,
        <https://w3id.org/cdif/data_description/1.0>,
        <https://w3id.org/cdif/discovery/1.0>,
        <https://w3id.org/cdif/manifest/1.0>,
        <https://w3id.org/cdif/provenance/1.0>,
        <https://w3id.org/geochem/metadata/profiles/adaEMPA>,
        <https://w3id.org/geochem/metadata/profiles/adaProduct> ;
    schema1:about ex:adaEMPA-P7 ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:dateModified "2026-04-29" ;
    schema1:maintainer [ a schema1:Organization ;
            schema1:name "Astromat Data Archive" ] ;
    schema1:sdDatePublished "2026-04-29T12:00:00Z" .

ex:adaEMPA-P7-var-Ca a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Ca abundance measured by EMPA WDS (20 s peak time s peak counting; 10 s background s background counting; calibrated against Wilburforce apatite)." ;
    schema1:name "Ca" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Ca" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P7-var-Cl a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Cl abundance measured by EMPA WDS (20 s peak time s peak counting; 10 s background s background counting; calibrated against tugtupite)." ;
    schema1:name "Cl" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Cl" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P7-var-F a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "F abundance measured by EMPA WDS (20 s peak time s peak counting; 10 s background s background counting; calibrated against SrF2)." ;
    schema1:name "F" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/F" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P7-var-Fe a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Fe abundance measured by EMPA WDS (20 s peak time s peak counting; 10 s background s background counting; calibrated against ilmenite)." ;
    schema1:name "Fe" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Fe" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P7-var-Mg a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Mg abundance measured by EMPA WDS (20 s peak time s peak counting; 10 s background s background counting; calibrated against SW olivine)." ;
    schema1:name "Mg" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Mg" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P7-var-Mn a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Mn abundance measured by EMPA WDS (20 s peak time s peak counting; 10 s background s background counting; calibrated against rhodonite)." ;
    schema1:name "Mn" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Mn" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P7-var-Na a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Na abundance measured by EMPA WDS (20 s peak time s peak counting; 10 s background s background counting; calibrated against albite)." ;
    schema1:name "Na" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Na" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P7-var-OH a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "OH abundance measured by EMPA WDS (20 s peak time s peak counting; 10 s background s background counting)." ;
    schema1:name "OH" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/OH" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P7-var-P a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "P abundance measured by EMPA WDS (20 s peak time s peak counting; 10 s background s background counting; calibrated against Wilburforce apatite)." ;
    schema1:name "P" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/P" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P7-var-S a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "S abundance measured by EMPA WDS (20 s peak time s peak counting; 10 s background s background counting; calibrated against barite)." ;
    schema1:name "S" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/S" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P7-var-Si a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Si abundance measured by EMPA WDS (20 s peak time s peak counting; 10 s background s background counting; calibrated against quartz)." ;
    schema1:name "Si" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Si" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .


```


### adaEMPA — P8sil (Zega et al. 2025 (Bennu silicates, Nat. Geosci.))
Auto-generated adaEMPA dataset record for publication P8sil.
schema:variableMeasured is derived from the empaTAPP TAPP definition's
ada:defaultAnalytes; schema:hasPart carries the paired detailEMPA fields
and references the TAPP via schema:measurementTechnique. Synthetic
placeholders are used for DOI, file size, and dates.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "prov": "http://www.w3.org/ns/prov#",
    "spdx": "http://spdx.org/rdf/terms#",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "dcterms": "http://purl.org/dc/terms/",
    "ex": "https://example.org/",
    "dcat": "http://www.w3.org/ns/dcat#"
  },
  "@id": "ex:adaEMPA-P8sil",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "adaEMPA dataset for P8sil (Zega et al. 2025 (Bennu silicates, Nat. Geosci.))",
  "schema:description": "Auto-generated adaEMPA profile-level Dataset for publication P8sil: Zega et al. 2025 (Bennu silicates, Nat. Geosci.). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p8sil); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes.",
  "schema:additionalType": [
    "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.PLACEHOLDER/adaempa-p8sil"
  },
  "schema:url": "https://astromat.org/products/adaempa-p8sil",
  "schema:dateModified": "2026-04-29",
  "schema:version": "0.1",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:creativeWorkStatus": "Draft",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Electron Microprobe Analysis (EMPA)",
    "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/EMPA"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-empa-p8sil",
      "schema:startDate": "2026-04-29",
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": [
            "nxs:BaseClass/NXinstrument",
            "ada:EMPAInstrument"
          ],
          "schema:name": "Cameca; JEOL Cameca SX-100 Ultra (U of Arizona); JEOL 7600F SEM with WDS (JSC)",
          "schema:identifier": [
            "ex:instrument-empa-001"
          ],
          "schema:manufacturer": {
            "@type": [
              "schema:Organization"
            ],
            "schema:name": "Cameca; JEOL"
          }
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "University of Arizona (K-ALFAA); NASA JSC",
        "schema:additionalType": [
          "nxs:BaseClass/NXsource"
        ]
      },
      "schema:object": [
        {
          "@type": [
            "schema:Thing",
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalType": [
            "MaterialSample"
          ],
          "schema:name": "Sample analyzed in P8sil",
          "schema:identifier": [
            "igsn:10.60471/PLACEHOLDER-P8sil"
          ],
          "schema:description": "Sample of: Sheet silicates (serpentine, saponite), sulfides (pyrrhotite, pentlandite), magnetite,"
        }
      ]
    }
  ],
  "schema:variableMeasured": [],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "adaEMPA-P8sil-archive.zip",
      "schema:description": "Archive containing tabular EMPA data for P8sil.",
      "schema:contentUrl": "https://astromat.org/downloads/adaempa-p8sil.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "0000000000000000000000000000000000000000000000000000000000000000"
      },
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 1048576,
        "schema:unitText": "byte"
      },
      "schema:hasPart": [
        {
          "@id": "ex:adaEMPA-P8sil-data-001",
          "@type": [
            "schema:MediaObject",
            "ada:tabularData",
            "cdi:TabularTextDataSet",
            "schema:Thing"
          ],
          "schema:name": "adaEMPA-P8sil-data.csv",
          "schema:description": "Per-point quantitative EMPA analyses (Zega et al. 2025 (Bennu silicates, Nat. Geosci.)).",
          "schema:additionalType": [
            "ada:EMPAQEATabular"
          ],
          "schema:encodingFormat": [
            "text/csv"
          ],
          "cdi:isDelimited": true,
          "cdi:isFixedWidth": false,
          "csvw:delimiter": ",",
          "csvw:header": true,
          "ada:componentType": "ada:EMPAQEATabular",
          "ada:spectrometersUsed": "5x WDS",
          "ada:signalUsed": "Kα x-ray lines",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-p8sil"
          },
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/empaTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/acceleratingVoltage",
              "schema:name": "Default Accelerating Voltage",
              "schema:value": 15,
              "schema:unitText": "kV"
            },
            {
              "@id": "ada:parameter/empaTAPP/beamDiameter",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/beamDiameter",
              "schema:name": "Default Beam Diameter",
              "schema:value": "~1 µm focused",
              "schema:unitText": "µm"
            }
          ],
          "cdif:hasPhysicalMapping": [
            {
              "cdif:index": 0,
              "cdif:physicalDataType": "String",
              "cdi:nullSequence": "NA"
            }
          ]
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:adaEMPA-P8sil-metadata",
    "schema:about": {
      "@id": "ex:adaEMPA-P8sil"
    },
    "schema:dateModified": "2026-04-29",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaEMPA"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaProduct"
      }
    ],
    "schema:maintainer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Astromat Data Archive"
    },
    "schema:sdDatePublished": "2026-04-29T12:00:00Z"
  }
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
      "csvw": "http://www.w3.org/ns/csvw#",
      "prov": "http://www.w3.org/ns/prov#",
      "dcterms": "http://purl.org/dc/terms/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/profiles/adaProfiles/adaEMPA/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "csvw": "http://www.w3.org/ns/csvw#",
      "prov": "http://www.w3.org/ns/prov#",
      "spdx": "http://spdx.org/rdf/terms#",
      "nxs": "http://purl.org/nexusformat/definitions/",
      "dcterms": "http://purl.org/dc/terms/",
      "ex": "https://example.org/",
      "dcat": "http://www.w3.org/ns/dcat#"
    }
  ],
  "@id": "ex:adaEMPA-P8sil",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "adaEMPA dataset for P8sil (Zega et al. 2025 (Bennu silicates, Nat. Geosci.))",
  "schema:description": "Auto-generated adaEMPA profile-level Dataset for publication P8sil: Zega et al. 2025 (Bennu silicates, Nat. Geosci.). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p8sil); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes.",
  "schema:additionalType": [
    "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.PLACEHOLDER/adaempa-p8sil"
  },
  "schema:url": "https://astromat.org/products/adaempa-p8sil",
  "schema:dateModified": "2026-04-29",
  "schema:version": "0.1",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:creativeWorkStatus": "Draft",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Electron Microprobe Analysis (EMPA)",
    "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/EMPA"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-empa-p8sil",
      "schema:startDate": "2026-04-29",
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": [
            "nxs:BaseClass/NXinstrument",
            "ada:EMPAInstrument"
          ],
          "schema:name": "Cameca; JEOL Cameca SX-100 Ultra (U of Arizona); JEOL 7600F SEM with WDS (JSC)",
          "schema:identifier": [
            "ex:instrument-empa-001"
          ],
          "schema:manufacturer": {
            "@type": [
              "schema:Organization"
            ],
            "schema:name": "Cameca; JEOL"
          }
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "University of Arizona (K-ALFAA); NASA JSC",
        "schema:additionalType": [
          "nxs:BaseClass/NXsource"
        ]
      },
      "schema:object": [
        {
          "@type": [
            "schema:Thing",
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalType": [
            "MaterialSample"
          ],
          "schema:name": "Sample analyzed in P8sil",
          "schema:identifier": [
            "igsn:10.60471/PLACEHOLDER-P8sil"
          ],
          "schema:description": "Sample of: Sheet silicates (serpentine, saponite), sulfides (pyrrhotite, pentlandite), magnetite,"
        }
      ]
    }
  ],
  "schema:variableMeasured": [],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "adaEMPA-P8sil-archive.zip",
      "schema:description": "Archive containing tabular EMPA data for P8sil.",
      "schema:contentUrl": "https://astromat.org/downloads/adaempa-p8sil.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "0000000000000000000000000000000000000000000000000000000000000000"
      },
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 1048576,
        "schema:unitText": "byte"
      },
      "schema:hasPart": [
        {
          "@id": "ex:adaEMPA-P8sil-data-001",
          "@type": [
            "schema:MediaObject",
            "ada:tabularData",
            "cdi:TabularTextDataSet",
            "schema:Thing"
          ],
          "schema:name": "adaEMPA-P8sil-data.csv",
          "schema:description": "Per-point quantitative EMPA analyses (Zega et al. 2025 (Bennu silicates, Nat. Geosci.)).",
          "schema:additionalType": [
            "ada:EMPAQEATabular"
          ],
          "schema:encodingFormat": [
            "text/csv"
          ],
          "cdi:isDelimited": true,
          "cdi:isFixedWidth": false,
          "csvw:delimiter": ",",
          "csvw:header": true,
          "ada:componentType": "ada:EMPAQEATabular",
          "ada:spectrometersUsed": "5x WDS",
          "ada:signalUsed": "K\u03b1 x-ray lines",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-p8sil"
          },
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/empaTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/acceleratingVoltage",
              "schema:name": "Default Accelerating Voltage",
              "schema:value": 15,
              "schema:unitText": "kV"
            },
            {
              "@id": "ada:parameter/empaTAPP/beamDiameter",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/beamDiameter",
              "schema:name": "Default Beam Diameter",
              "schema:value": "~1 \u00b5m focused",
              "schema:unitText": "\u00b5m"
            }
          ],
          "cdif:hasPhysicalMapping": [
            {
              "cdif:index": 0,
              "cdif:physicalDataType": "String",
              "cdi:nullSequence": "NA"
            }
          ]
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:adaEMPA-P8sil-metadata",
    "schema:about": {
      "@id": "ex:adaEMPA-P8sil"
    },
    "schema:dateModified": "2026-04-29",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaEMPA"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaProduct"
      }
    ],
    "schema:maintainer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Astromat Data Archive"
    },
    "schema:sdDatePublished": "2026-04-29T12:00:00Z"
  }
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://cdif.org/0.1/> .
@prefix csvw: <http://www.w3.org/ns/csvw#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix spdx: <http://spdx.org/rdf/terms#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://ada.astromat.org/metadata/parameter/empaTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:name "Default Accelerating Voltage" ;
    schema1:propertyID "ada:parameter/empaTAPP/acceleratingVoltage" ;
    schema1:unitText "kV" ;
    schema1:value 15 .

<https://ada.astromat.org/metadata/parameter/empaTAPP/beamDiameter> a schema1:PropertyValue ;
    schema1:name "Default Beam Diameter" ;
    schema1:propertyID "ada:parameter/empaTAPP/beamDiameter" ;
    schema1:unitText "µm" ;
    schema1:value "~1 µm focused" .

ex:adaEMPA-P8sil a schema1:Dataset,
        schema1:Product ;
    schema1:additionalType "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
        "ada:DataDeliveryPackage" ;
    schema1:creativeWorkStatus "Draft" ;
    schema1:dateModified "2026-04-29" ;
    schema1:description "Auto-generated adaEMPA profile-level Dataset for publication P8sil: Zega et al. 2025 (Bennu silicates, Nat. Geosci.). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p8sil); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes." ;
    schema1:distribution [ a schema1:DataDownload ;
            schema1:contentUrl "https://astromat.org/downloads/adaempa-p8sil.zip" ;
            schema1:description "Archive containing tabular EMPA data for P8sil." ;
            schema1:encodingFormat "application/zip" ;
            schema1:hasPart ex:adaEMPA-P8sil-data-001 ;
            schema1:name "adaEMPA-P8sil-archive.zip" ;
            schema1:size [ a schema1:QuantitativeValue ;
                    schema1:unitText "byte" ;
                    schema1:value 1048576 ] ;
            spdx:checksum [ a spdx:Checksum ;
                    spdx:algorithm "SHA256" ;
                    spdx:checksumValue "0000000000000000000000000000000000000000000000000000000000000000" ] ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://registry.identifiers.org/registry/doi" ;
            schema1:value "10.PLACEHOLDER/adaempa-p8sil" ] ;
    schema1:license "https://creativecommons.org/licenses/by/4.0/" ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:identifier "https://ada.astromat.org/vocabulary/techniques/EMPA" ;
            schema1:name "Electron Microprobe Analysis (EMPA)" ] ;
    schema1:name "adaEMPA dataset for P8sil (Zega et al. 2025 (Bennu silicates, Nat. Geosci.))" ;
    schema1:subjectOf ex:adaEMPA-P8sil-metadata ;
    schema1:url "https://astromat.org/products/adaempa-p8sil" ;
    schema1:version "0.1" ;
    prov:wasGeneratedBy [ a schema1:Action,
                prov:Activity ;
            schema1:identifier "session-empa-p8sil" ;
            schema1:location [ a schema1:Place ;
                    schema1:additionalType "nxs:BaseClass/NXsource" ;
                    schema1:name "University of Arizona (K-ALFAA); NASA JSC" ] ;
            schema1:object [ a schema1:Thing,
                        <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalType "MaterialSample" ;
                    schema1:description "Sample of: Sheet silicates (serpentine, saponite), sulfides (pyrrhotite, pentlandite), magnetite," ;
                    schema1:identifier "igsn:10.60471/PLACEHOLDER-P8sil" ;
                    schema1:name "Sample analyzed in P8sil" ] ;
            schema1:startDate "2026-04-29" ;
            prov:used [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType "ada:EMPAInstrument",
                        "nxs:BaseClass/NXinstrument" ;
                    schema1:identifier "ex:instrument-empa-001" ;
                    schema1:manufacturer [ a schema1:Organization ;
                            schema1:name "Cameca; JEOL" ] ;
                    schema1:name "Cameca; JEOL Cameca SX-100 Ultra (U of Arizona); JEOL 7600F SEM with WDS (JSC)" ] ] .

ex:adaEMPA-P8sil-data-001 a cdi:TabularTextDataSet,
        schema1:MediaObject,
        schema1:Thing,
        ada:tabularData ;
    cdi:isDelimited true ;
    cdi:isFixedWidth false ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/empaTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/empaTAPP/beamDiameter> ;
    schema1:additionalType "ada:EMPAQEATabular" ;
    schema1:description "Per-point quantitative EMPA analyses (Zega et al. 2025 (Bennu silicates, Nat. Geosci.))." ;
    schema1:encodingFormat "text/csv" ;
    schema1:measurementTechnique ex:empaTAPP-p8sil ;
    schema1:name "adaEMPA-P8sil-data.csv" ;
    csvw:delimiter "," ;
    csvw:header true ;
    ada:componentType "ada:EMPAQEATabular" ;
    ada:signalUsed "Kα x-ray lines" ;
    ada:spectrometersUsed "5x WDS" ;
    cdif:hasPhysicalMapping [ cdi:nullSequence "NA" ;
            cdif:index 0 ;
            cdif:physicalDataType "String" ] .

ex:adaEMPA-P8sil-metadata a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.0>,
        <https://w3id.org/cdif/data_description/1.0>,
        <https://w3id.org/cdif/discovery/1.0>,
        <https://w3id.org/cdif/manifest/1.0>,
        <https://w3id.org/cdif/provenance/1.0>,
        <https://w3id.org/geochem/metadata/profiles/adaEMPA>,
        <https://w3id.org/geochem/metadata/profiles/adaProduct> ;
    schema1:about ex:adaEMPA-P8sil ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:dateModified "2026-04-29" ;
    schema1:maintainer [ a schema1:Organization ;
            schema1:name "Astromat Data Archive" ] ;
    schema1:sdDatePublished "2026-04-29T12:00:00Z" .


```


### adaEMPA — P8carb (Zega et al. 2025 (Bennu carbonates, Nat. Geosci.))
Auto-generated adaEMPA dataset record for publication P8carb.
schema:variableMeasured is derived from the empaTAPP TAPP definition's
ada:defaultAnalytes; schema:hasPart carries the paired detailEMPA fields
and references the TAPP via schema:measurementTechnique. Synthetic
placeholders are used for DOI, file size, and dates.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "prov": "http://www.w3.org/ns/prov#",
    "spdx": "http://spdx.org/rdf/terms#",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "dcterms": "http://purl.org/dc/terms/",
    "ex": "https://example.org/",
    "dcat": "http://www.w3.org/ns/dcat#"
  },
  "@id": "ex:adaEMPA-P8carb",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "adaEMPA dataset for P8carb (Zega et al. 2025 (Bennu carbonates, Nat. Geosci.))",
  "schema:description": "Auto-generated adaEMPA profile-level Dataset for publication P8carb: Zega et al. 2025 (Bennu carbonates, Nat. Geosci.). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p8carb); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes.",
  "schema:additionalType": [
    "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.PLACEHOLDER/adaempa-p8carb"
  },
  "schema:url": "https://astromat.org/products/adaempa-p8carb",
  "schema:dateModified": "2026-04-29",
  "schema:version": "0.1",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:creativeWorkStatus": "Draft",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Electron Microprobe Analysis (EMPA)",
    "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/EMPA"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-empa-p8carb",
      "schema:startDate": "2026-04-29",
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": [
            "nxs:BaseClass/NXinstrument",
            "ada:EMPAInstrument"
          ],
          "schema:name": "Cameca; JEOL Cameca SX-100 Ultra (U of Arizona); JEOL 7600F SEM with WDS (JSC)",
          "schema:identifier": [
            "ex:instrument-empa-001"
          ],
          "schema:manufacturer": {
            "@type": [
              "schema:Organization"
            ],
            "schema:name": "Cameca; JEOL"
          }
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "University of Arizona (K-ALFAA); NASA JSC",
        "schema:additionalType": [
          "nxs:BaseClass/NXsource"
        ]
      },
      "schema:object": [
        {
          "@type": [
            "schema:Thing",
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalType": [
            "MaterialSample"
          ],
          "schema:name": "Sample analyzed in P8carb",
          "schema:identifier": [
            "igsn:10.60471/PLACEHOLDER-P8carb"
          ],
          "schema:description": "Sample of: carbonates (calcite, dolomite, magnesite)"
        }
      ]
    }
  ],
  "schema:variableMeasured": [],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "adaEMPA-P8carb-archive.zip",
      "schema:description": "Archive containing tabular EMPA data for P8carb.",
      "schema:contentUrl": "https://astromat.org/downloads/adaempa-p8carb.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "0000000000000000000000000000000000000000000000000000000000000000"
      },
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 1048576,
        "schema:unitText": "byte"
      },
      "schema:hasPart": [
        {
          "@id": "ex:adaEMPA-P8carb-data-001",
          "@type": [
            "schema:MediaObject",
            "ada:tabularData",
            "cdi:TabularTextDataSet",
            "schema:Thing"
          ],
          "schema:name": "adaEMPA-P8carb-data.csv",
          "schema:description": "Per-point quantitative EMPA analyses (Zega et al. 2025 (Bennu carbonates, Nat. Geosci.)).",
          "schema:additionalType": [
            "ada:EMPAQEATabular"
          ],
          "schema:encodingFormat": [
            "text/csv"
          ],
          "cdi:isDelimited": true,
          "cdi:isFixedWidth": false,
          "csvw:delimiter": ",",
          "csvw:header": true,
          "ada:componentType": "ada:EMPAQEATabular",
          "ada:spectrometersUsed": "5x WDS",
          "ada:signalUsed": "Kα x-ray lines",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-p8carb"
          },
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/empaTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/acceleratingVoltage",
              "schema:name": "Default Accelerating Voltage",
              "schema:value": 15,
              "schema:unitText": "kV"
            },
            {
              "@id": "ada:parameter/empaTAPP/beamDiameter",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/beamDiameter",
              "schema:name": "Default Beam Diameter",
              "schema:value": "variable",
              "schema:unitText": "µm"
            }
          ],
          "cdif:hasPhysicalMapping": [
            {
              "cdif:index": 0,
              "cdif:physicalDataType": "String",
              "cdi:nullSequence": "NA"
            }
          ]
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:adaEMPA-P8carb-metadata",
    "schema:about": {
      "@id": "ex:adaEMPA-P8carb"
    },
    "schema:dateModified": "2026-04-29",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaEMPA"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaProduct"
      }
    ],
    "schema:maintainer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Astromat Data Archive"
    },
    "schema:sdDatePublished": "2026-04-29T12:00:00Z"
  }
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
      "csvw": "http://www.w3.org/ns/csvw#",
      "prov": "http://www.w3.org/ns/prov#",
      "dcterms": "http://purl.org/dc/terms/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/profiles/adaProfiles/adaEMPA/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "csvw": "http://www.w3.org/ns/csvw#",
      "prov": "http://www.w3.org/ns/prov#",
      "spdx": "http://spdx.org/rdf/terms#",
      "nxs": "http://purl.org/nexusformat/definitions/",
      "dcterms": "http://purl.org/dc/terms/",
      "ex": "https://example.org/",
      "dcat": "http://www.w3.org/ns/dcat#"
    }
  ],
  "@id": "ex:adaEMPA-P8carb",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "adaEMPA dataset for P8carb (Zega et al. 2025 (Bennu carbonates, Nat. Geosci.))",
  "schema:description": "Auto-generated adaEMPA profile-level Dataset for publication P8carb: Zega et al. 2025 (Bennu carbonates, Nat. Geosci.). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p8carb); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes.",
  "schema:additionalType": [
    "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.PLACEHOLDER/adaempa-p8carb"
  },
  "schema:url": "https://astromat.org/products/adaempa-p8carb",
  "schema:dateModified": "2026-04-29",
  "schema:version": "0.1",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:creativeWorkStatus": "Draft",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Electron Microprobe Analysis (EMPA)",
    "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/EMPA"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-empa-p8carb",
      "schema:startDate": "2026-04-29",
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": [
            "nxs:BaseClass/NXinstrument",
            "ada:EMPAInstrument"
          ],
          "schema:name": "Cameca; JEOL Cameca SX-100 Ultra (U of Arizona); JEOL 7600F SEM with WDS (JSC)",
          "schema:identifier": [
            "ex:instrument-empa-001"
          ],
          "schema:manufacturer": {
            "@type": [
              "schema:Organization"
            ],
            "schema:name": "Cameca; JEOL"
          }
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "University of Arizona (K-ALFAA); NASA JSC",
        "schema:additionalType": [
          "nxs:BaseClass/NXsource"
        ]
      },
      "schema:object": [
        {
          "@type": [
            "schema:Thing",
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalType": [
            "MaterialSample"
          ],
          "schema:name": "Sample analyzed in P8carb",
          "schema:identifier": [
            "igsn:10.60471/PLACEHOLDER-P8carb"
          ],
          "schema:description": "Sample of: carbonates (calcite, dolomite, magnesite)"
        }
      ]
    }
  ],
  "schema:variableMeasured": [],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "adaEMPA-P8carb-archive.zip",
      "schema:description": "Archive containing tabular EMPA data for P8carb.",
      "schema:contentUrl": "https://astromat.org/downloads/adaempa-p8carb.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "0000000000000000000000000000000000000000000000000000000000000000"
      },
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 1048576,
        "schema:unitText": "byte"
      },
      "schema:hasPart": [
        {
          "@id": "ex:adaEMPA-P8carb-data-001",
          "@type": [
            "schema:MediaObject",
            "ada:tabularData",
            "cdi:TabularTextDataSet",
            "schema:Thing"
          ],
          "schema:name": "adaEMPA-P8carb-data.csv",
          "schema:description": "Per-point quantitative EMPA analyses (Zega et al. 2025 (Bennu carbonates, Nat. Geosci.)).",
          "schema:additionalType": [
            "ada:EMPAQEATabular"
          ],
          "schema:encodingFormat": [
            "text/csv"
          ],
          "cdi:isDelimited": true,
          "cdi:isFixedWidth": false,
          "csvw:delimiter": ",",
          "csvw:header": true,
          "ada:componentType": "ada:EMPAQEATabular",
          "ada:spectrometersUsed": "5x WDS",
          "ada:signalUsed": "K\u03b1 x-ray lines",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-p8carb"
          },
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/empaTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/acceleratingVoltage",
              "schema:name": "Default Accelerating Voltage",
              "schema:value": 15,
              "schema:unitText": "kV"
            },
            {
              "@id": "ada:parameter/empaTAPP/beamDiameter",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/beamDiameter",
              "schema:name": "Default Beam Diameter",
              "schema:value": "variable",
              "schema:unitText": "\u00b5m"
            }
          ],
          "cdif:hasPhysicalMapping": [
            {
              "cdif:index": 0,
              "cdif:physicalDataType": "String",
              "cdi:nullSequence": "NA"
            }
          ]
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:adaEMPA-P8carb-metadata",
    "schema:about": {
      "@id": "ex:adaEMPA-P8carb"
    },
    "schema:dateModified": "2026-04-29",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaEMPA"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaProduct"
      }
    ],
    "schema:maintainer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Astromat Data Archive"
    },
    "schema:sdDatePublished": "2026-04-29T12:00:00Z"
  }
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://cdif.org/0.1/> .
@prefix csvw: <http://www.w3.org/ns/csvw#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix spdx: <http://spdx.org/rdf/terms#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://ada.astromat.org/metadata/parameter/empaTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:name "Default Accelerating Voltage" ;
    schema1:propertyID "ada:parameter/empaTAPP/acceleratingVoltage" ;
    schema1:unitText "kV" ;
    schema1:value 15 .

<https://ada.astromat.org/metadata/parameter/empaTAPP/beamDiameter> a schema1:PropertyValue ;
    schema1:name "Default Beam Diameter" ;
    schema1:propertyID "ada:parameter/empaTAPP/beamDiameter" ;
    schema1:unitText "µm" ;
    schema1:value "variable" .

ex:adaEMPA-P8carb a schema1:Dataset,
        schema1:Product ;
    schema1:additionalType "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
        "ada:DataDeliveryPackage" ;
    schema1:creativeWorkStatus "Draft" ;
    schema1:dateModified "2026-04-29" ;
    schema1:description "Auto-generated adaEMPA profile-level Dataset for publication P8carb: Zega et al. 2025 (Bennu carbonates, Nat. Geosci.). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p8carb); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes." ;
    schema1:distribution [ a schema1:DataDownload ;
            schema1:contentUrl "https://astromat.org/downloads/adaempa-p8carb.zip" ;
            schema1:description "Archive containing tabular EMPA data for P8carb." ;
            schema1:encodingFormat "application/zip" ;
            schema1:hasPart ex:adaEMPA-P8carb-data-001 ;
            schema1:name "adaEMPA-P8carb-archive.zip" ;
            schema1:size [ a schema1:QuantitativeValue ;
                    schema1:unitText "byte" ;
                    schema1:value 1048576 ] ;
            spdx:checksum [ a spdx:Checksum ;
                    spdx:algorithm "SHA256" ;
                    spdx:checksumValue "0000000000000000000000000000000000000000000000000000000000000000" ] ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://registry.identifiers.org/registry/doi" ;
            schema1:value "10.PLACEHOLDER/adaempa-p8carb" ] ;
    schema1:license "https://creativecommons.org/licenses/by/4.0/" ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:identifier "https://ada.astromat.org/vocabulary/techniques/EMPA" ;
            schema1:name "Electron Microprobe Analysis (EMPA)" ] ;
    schema1:name "adaEMPA dataset for P8carb (Zega et al. 2025 (Bennu carbonates, Nat. Geosci.))" ;
    schema1:subjectOf ex:adaEMPA-P8carb-metadata ;
    schema1:url "https://astromat.org/products/adaempa-p8carb" ;
    schema1:version "0.1" ;
    prov:wasGeneratedBy [ a schema1:Action,
                prov:Activity ;
            schema1:identifier "session-empa-p8carb" ;
            schema1:location [ a schema1:Place ;
                    schema1:additionalType "nxs:BaseClass/NXsource" ;
                    schema1:name "University of Arizona (K-ALFAA); NASA JSC" ] ;
            schema1:object [ a schema1:Thing,
                        <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalType "MaterialSample" ;
                    schema1:description "Sample of: carbonates (calcite, dolomite, magnesite)" ;
                    schema1:identifier "igsn:10.60471/PLACEHOLDER-P8carb" ;
                    schema1:name "Sample analyzed in P8carb" ] ;
            schema1:startDate "2026-04-29" ;
            prov:used [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType "ada:EMPAInstrument",
                        "nxs:BaseClass/NXinstrument" ;
                    schema1:identifier "ex:instrument-empa-001" ;
                    schema1:manufacturer [ a schema1:Organization ;
                            schema1:name "Cameca; JEOL" ] ;
                    schema1:name "Cameca; JEOL Cameca SX-100 Ultra (U of Arizona); JEOL 7600F SEM with WDS (JSC)" ] ] .

ex:adaEMPA-P8carb-data-001 a cdi:TabularTextDataSet,
        schema1:MediaObject,
        schema1:Thing,
        ada:tabularData ;
    cdi:isDelimited true ;
    cdi:isFixedWidth false ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/empaTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/empaTAPP/beamDiameter> ;
    schema1:additionalType "ada:EMPAQEATabular" ;
    schema1:description "Per-point quantitative EMPA analyses (Zega et al. 2025 (Bennu carbonates, Nat. Geosci.))." ;
    schema1:encodingFormat "text/csv" ;
    schema1:measurementTechnique ex:empaTAPP-p8carb ;
    schema1:name "adaEMPA-P8carb-data.csv" ;
    csvw:delimiter "," ;
    csvw:header true ;
    ada:componentType "ada:EMPAQEATabular" ;
    ada:signalUsed "Kα x-ray lines" ;
    ada:spectrometersUsed "5x WDS" ;
    cdif:hasPhysicalMapping [ cdi:nullSequence "NA" ;
            cdif:index 0 ;
            cdif:physicalDataType "String" ] .

ex:adaEMPA-P8carb-metadata a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.0>,
        <https://w3id.org/cdif/data_description/1.0>,
        <https://w3id.org/cdif/discovery/1.0>,
        <https://w3id.org/cdif/manifest/1.0>,
        <https://w3id.org/cdif/provenance/1.0>,
        <https://w3id.org/geochem/metadata/profiles/adaEMPA>,
        <https://w3id.org/geochem/metadata/profiles/adaProduct> ;
    schema1:about ex:adaEMPA-P8carb ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:dateModified "2026-04-29" ;
    schema1:maintainer [ a schema1:Organization ;
            schema1:name "Astromat Data Archive" ] ;
    schema1:sdDatePublished "2026-04-29T12:00:00Z" .


```


### adaEMPA — P8phos (Zega et al. 2025 (Bennu phosphates, Nat. Geosci.))
Auto-generated adaEMPA dataset record for publication P8phos.
schema:variableMeasured is derived from the empaTAPP TAPP definition's
ada:defaultAnalytes; schema:hasPart carries the paired detailEMPA fields
and references the TAPP via schema:measurementTechnique. Synthetic
placeholders are used for DOI, file size, and dates.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "prov": "http://www.w3.org/ns/prov#",
    "spdx": "http://spdx.org/rdf/terms#",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "dcterms": "http://purl.org/dc/terms/",
    "ex": "https://example.org/",
    "dcat": "http://www.w3.org/ns/dcat#"
  },
  "@id": "ex:adaEMPA-P8phos",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "adaEMPA dataset for P8phos (Zega et al. 2025 (Bennu phosphates, Nat. Geosci.))",
  "schema:description": "Auto-generated adaEMPA profile-level Dataset for publication P8phos: Zega et al. 2025 (Bennu phosphates, Nat. Geosci.). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p8phos); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes.",
  "schema:additionalType": [
    "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.PLACEHOLDER/adaempa-p8phos"
  },
  "schema:url": "https://astromat.org/products/adaempa-p8phos",
  "schema:dateModified": "2026-04-29",
  "schema:version": "0.1",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:creativeWorkStatus": "Draft",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Electron Microprobe Analysis (EMPA)",
    "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/EMPA"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-empa-p8phos",
      "schema:startDate": "2026-04-29",
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": [
            "nxs:BaseClass/NXinstrument",
            "ada:EMPAInstrument"
          ],
          "schema:name": "Cameca; JEOL Cameca SX-100 Ultra (U of Arizona); JEOL 7600F SEM with WDS (JSC)",
          "schema:identifier": [
            "ex:instrument-empa-001"
          ],
          "schema:manufacturer": {
            "@type": [
              "schema:Organization"
            ],
            "schema:name": "Cameca; JEOL"
          }
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "University of Arizona (K-ALFAA); NASA JSC",
        "schema:additionalType": [
          "nxs:BaseClass/NXsource"
        ]
      },
      "schema:object": [
        {
          "@type": [
            "schema:Thing",
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalType": [
            "MaterialSample"
          ],
          "schema:name": "Sample analyzed in P8phos",
          "schema:identifier": [
            "igsn:10.60471/PLACEHOLDER-P8phos"
          ],
          "schema:description": "Sample of: phosphates"
        }
      ]
    }
  ],
  "schema:variableMeasured": [],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "adaEMPA-P8phos-archive.zip",
      "schema:description": "Archive containing tabular EMPA data for P8phos.",
      "schema:contentUrl": "https://astromat.org/downloads/adaempa-p8phos.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "0000000000000000000000000000000000000000000000000000000000000000"
      },
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 1048576,
        "schema:unitText": "byte"
      },
      "schema:hasPart": [
        {
          "@id": "ex:adaEMPA-P8phos-data-001",
          "@type": [
            "schema:MediaObject",
            "ada:tabularData",
            "cdi:TabularTextDataSet",
            "schema:Thing"
          ],
          "schema:name": "adaEMPA-P8phos-data.csv",
          "schema:description": "Per-point quantitative EMPA analyses (Zega et al. 2025 (Bennu phosphates, Nat. Geosci.)).",
          "schema:additionalType": [
            "ada:EMPAQEATabular"
          ],
          "schema:encodingFormat": [
            "text/csv"
          ],
          "cdi:isDelimited": true,
          "cdi:isFixedWidth": false,
          "csvw:delimiter": ",",
          "csvw:header": true,
          "ada:componentType": "ada:EMPAQEATabular",
          "ada:spectrometersUsed": "5x WDS",
          "ada:signalUsed": "Kα x-ray lines",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-p8phos"
          },
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/empaTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/acceleratingVoltage",
              "schema:name": "Default Accelerating Voltage",
              "schema:value": 15,
              "schema:unitText": "kV"
            },
            {
              "@id": "ada:parameter/empaTAPP/beamDiameter",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/beamDiameter",
              "schema:name": "Default Beam Diameter",
              "schema:value": "variable",
              "schema:unitText": "µm"
            }
          ],
          "cdif:hasPhysicalMapping": [
            {
              "cdif:index": 0,
              "cdif:physicalDataType": "String",
              "cdi:nullSequence": "NA"
            }
          ]
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:adaEMPA-P8phos-metadata",
    "schema:about": {
      "@id": "ex:adaEMPA-P8phos"
    },
    "schema:dateModified": "2026-04-29",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaEMPA"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaProduct"
      }
    ],
    "schema:maintainer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Astromat Data Archive"
    },
    "schema:sdDatePublished": "2026-04-29T12:00:00Z"
  }
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
      "csvw": "http://www.w3.org/ns/csvw#",
      "prov": "http://www.w3.org/ns/prov#",
      "dcterms": "http://purl.org/dc/terms/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/profiles/adaProfiles/adaEMPA/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "csvw": "http://www.w3.org/ns/csvw#",
      "prov": "http://www.w3.org/ns/prov#",
      "spdx": "http://spdx.org/rdf/terms#",
      "nxs": "http://purl.org/nexusformat/definitions/",
      "dcterms": "http://purl.org/dc/terms/",
      "ex": "https://example.org/",
      "dcat": "http://www.w3.org/ns/dcat#"
    }
  ],
  "@id": "ex:adaEMPA-P8phos",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "adaEMPA dataset for P8phos (Zega et al. 2025 (Bennu phosphates, Nat. Geosci.))",
  "schema:description": "Auto-generated adaEMPA profile-level Dataset for publication P8phos: Zega et al. 2025 (Bennu phosphates, Nat. Geosci.). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p8phos); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes.",
  "schema:additionalType": [
    "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.PLACEHOLDER/adaempa-p8phos"
  },
  "schema:url": "https://astromat.org/products/adaempa-p8phos",
  "schema:dateModified": "2026-04-29",
  "schema:version": "0.1",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:creativeWorkStatus": "Draft",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Electron Microprobe Analysis (EMPA)",
    "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/EMPA"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-empa-p8phos",
      "schema:startDate": "2026-04-29",
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": [
            "nxs:BaseClass/NXinstrument",
            "ada:EMPAInstrument"
          ],
          "schema:name": "Cameca; JEOL Cameca SX-100 Ultra (U of Arizona); JEOL 7600F SEM with WDS (JSC)",
          "schema:identifier": [
            "ex:instrument-empa-001"
          ],
          "schema:manufacturer": {
            "@type": [
              "schema:Organization"
            ],
            "schema:name": "Cameca; JEOL"
          }
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "University of Arizona (K-ALFAA); NASA JSC",
        "schema:additionalType": [
          "nxs:BaseClass/NXsource"
        ]
      },
      "schema:object": [
        {
          "@type": [
            "schema:Thing",
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalType": [
            "MaterialSample"
          ],
          "schema:name": "Sample analyzed in P8phos",
          "schema:identifier": [
            "igsn:10.60471/PLACEHOLDER-P8phos"
          ],
          "schema:description": "Sample of: phosphates"
        }
      ]
    }
  ],
  "schema:variableMeasured": [],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "adaEMPA-P8phos-archive.zip",
      "schema:description": "Archive containing tabular EMPA data for P8phos.",
      "schema:contentUrl": "https://astromat.org/downloads/adaempa-p8phos.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "0000000000000000000000000000000000000000000000000000000000000000"
      },
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 1048576,
        "schema:unitText": "byte"
      },
      "schema:hasPart": [
        {
          "@id": "ex:adaEMPA-P8phos-data-001",
          "@type": [
            "schema:MediaObject",
            "ada:tabularData",
            "cdi:TabularTextDataSet",
            "schema:Thing"
          ],
          "schema:name": "adaEMPA-P8phos-data.csv",
          "schema:description": "Per-point quantitative EMPA analyses (Zega et al. 2025 (Bennu phosphates, Nat. Geosci.)).",
          "schema:additionalType": [
            "ada:EMPAQEATabular"
          ],
          "schema:encodingFormat": [
            "text/csv"
          ],
          "cdi:isDelimited": true,
          "cdi:isFixedWidth": false,
          "csvw:delimiter": ",",
          "csvw:header": true,
          "ada:componentType": "ada:EMPAQEATabular",
          "ada:spectrometersUsed": "5x WDS",
          "ada:signalUsed": "K\u03b1 x-ray lines",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-p8phos"
          },
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/empaTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/acceleratingVoltage",
              "schema:name": "Default Accelerating Voltage",
              "schema:value": 15,
              "schema:unitText": "kV"
            },
            {
              "@id": "ada:parameter/empaTAPP/beamDiameter",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/beamDiameter",
              "schema:name": "Default Beam Diameter",
              "schema:value": "variable",
              "schema:unitText": "\u00b5m"
            }
          ],
          "cdif:hasPhysicalMapping": [
            {
              "cdif:index": 0,
              "cdif:physicalDataType": "String",
              "cdi:nullSequence": "NA"
            }
          ]
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:adaEMPA-P8phos-metadata",
    "schema:about": {
      "@id": "ex:adaEMPA-P8phos"
    },
    "schema:dateModified": "2026-04-29",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaEMPA"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaProduct"
      }
    ],
    "schema:maintainer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Astromat Data Archive"
    },
    "schema:sdDatePublished": "2026-04-29T12:00:00Z"
  }
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://cdif.org/0.1/> .
@prefix csvw: <http://www.w3.org/ns/csvw#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix spdx: <http://spdx.org/rdf/terms#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://ada.astromat.org/metadata/parameter/empaTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:name "Default Accelerating Voltage" ;
    schema1:propertyID "ada:parameter/empaTAPP/acceleratingVoltage" ;
    schema1:unitText "kV" ;
    schema1:value 15 .

<https://ada.astromat.org/metadata/parameter/empaTAPP/beamDiameter> a schema1:PropertyValue ;
    schema1:name "Default Beam Diameter" ;
    schema1:propertyID "ada:parameter/empaTAPP/beamDiameter" ;
    schema1:unitText "µm" ;
    schema1:value "variable" .

ex:adaEMPA-P8phos a schema1:Dataset,
        schema1:Product ;
    schema1:additionalType "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
        "ada:DataDeliveryPackage" ;
    schema1:creativeWorkStatus "Draft" ;
    schema1:dateModified "2026-04-29" ;
    schema1:description "Auto-generated adaEMPA profile-level Dataset for publication P8phos: Zega et al. 2025 (Bennu phosphates, Nat. Geosci.). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p8phos); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes." ;
    schema1:distribution [ a schema1:DataDownload ;
            schema1:contentUrl "https://astromat.org/downloads/adaempa-p8phos.zip" ;
            schema1:description "Archive containing tabular EMPA data for P8phos." ;
            schema1:encodingFormat "application/zip" ;
            schema1:hasPart ex:adaEMPA-P8phos-data-001 ;
            schema1:name "adaEMPA-P8phos-archive.zip" ;
            schema1:size [ a schema1:QuantitativeValue ;
                    schema1:unitText "byte" ;
                    schema1:value 1048576 ] ;
            spdx:checksum [ a spdx:Checksum ;
                    spdx:algorithm "SHA256" ;
                    spdx:checksumValue "0000000000000000000000000000000000000000000000000000000000000000" ] ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://registry.identifiers.org/registry/doi" ;
            schema1:value "10.PLACEHOLDER/adaempa-p8phos" ] ;
    schema1:license "https://creativecommons.org/licenses/by/4.0/" ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:identifier "https://ada.astromat.org/vocabulary/techniques/EMPA" ;
            schema1:name "Electron Microprobe Analysis (EMPA)" ] ;
    schema1:name "adaEMPA dataset for P8phos (Zega et al. 2025 (Bennu phosphates, Nat. Geosci.))" ;
    schema1:subjectOf ex:adaEMPA-P8phos-metadata ;
    schema1:url "https://astromat.org/products/adaempa-p8phos" ;
    schema1:version "0.1" ;
    prov:wasGeneratedBy [ a schema1:Action,
                prov:Activity ;
            schema1:identifier "session-empa-p8phos" ;
            schema1:location [ a schema1:Place ;
                    schema1:additionalType "nxs:BaseClass/NXsource" ;
                    schema1:name "University of Arizona (K-ALFAA); NASA JSC" ] ;
            schema1:object [ a schema1:Thing,
                        <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalType "MaterialSample" ;
                    schema1:description "Sample of: phosphates" ;
                    schema1:identifier "igsn:10.60471/PLACEHOLDER-P8phos" ;
                    schema1:name "Sample analyzed in P8phos" ] ;
            schema1:startDate "2026-04-29" ;
            prov:used [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType "ada:EMPAInstrument",
                        "nxs:BaseClass/NXinstrument" ;
                    schema1:identifier "ex:instrument-empa-001" ;
                    schema1:manufacturer [ a schema1:Organization ;
                            schema1:name "Cameca; JEOL" ] ;
                    schema1:name "Cameca; JEOL Cameca SX-100 Ultra (U of Arizona); JEOL 7600F SEM with WDS (JSC)" ] ] .

ex:adaEMPA-P8phos-data-001 a cdi:TabularTextDataSet,
        schema1:MediaObject,
        schema1:Thing,
        ada:tabularData ;
    cdi:isDelimited true ;
    cdi:isFixedWidth false ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/empaTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/empaTAPP/beamDiameter> ;
    schema1:additionalType "ada:EMPAQEATabular" ;
    schema1:description "Per-point quantitative EMPA analyses (Zega et al. 2025 (Bennu phosphates, Nat. Geosci.))." ;
    schema1:encodingFormat "text/csv" ;
    schema1:measurementTechnique ex:empaTAPP-p8phos ;
    schema1:name "adaEMPA-P8phos-data.csv" ;
    csvw:delimiter "," ;
    csvw:header true ;
    ada:componentType "ada:EMPAQEATabular" ;
    ada:signalUsed "Kα x-ray lines" ;
    ada:spectrometersUsed "5x WDS" ;
    cdif:hasPhysicalMapping [ cdi:nullSequence "NA" ;
            cdif:index 0 ;
            cdif:physicalDataType "String" ] .

ex:adaEMPA-P8phos-metadata a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.0>,
        <https://w3id.org/cdif/data_description/1.0>,
        <https://w3id.org/cdif/discovery/1.0>,
        <https://w3id.org/cdif/manifest/1.0>,
        <https://w3id.org/cdif/provenance/1.0>,
        <https://w3id.org/geochem/metadata/profiles/adaEMPA>,
        <https://w3id.org/geochem/metadata/profiles/adaProduct> ;
    schema1:about ex:adaEMPA-P8phos ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:dateModified "2026-04-29" ;
    schema1:maintainer [ a schema1:Organization ;
            schema1:name "Astromat Data Archive" ] ;
    schema1:sdDatePublished "2026-04-29T12:00:00Z" .


```


### adaEMPA — P9sil (McCoy et al. 2025 (Bennu silicates, Nature))
Auto-generated adaEMPA dataset record for publication P9sil.
schema:variableMeasured is derived from the empaTAPP TAPP definition's
ada:defaultAnalytes; schema:hasPart carries the paired detailEMPA fields
and references the TAPP via schema:measurementTechnique. Synthetic
placeholders are used for DOI, file size, and dates.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "prov": "http://www.w3.org/ns/prov#",
    "spdx": "http://spdx.org/rdf/terms#",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "dcterms": "http://purl.org/dc/terms/",
    "ex": "https://example.org/",
    "dcat": "http://www.w3.org/ns/dcat#"
  },
  "@id": "ex:adaEMPA-P9sil",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "adaEMPA dataset for P9sil (McCoy et al. 2025 (Bennu silicates, Nature))",
  "schema:description": "Auto-generated adaEMPA profile-level Dataset for publication P9sil: McCoy et al. 2025 (Bennu silicates, Nature). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p9sil); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes.",
  "schema:additionalType": [
    "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.PLACEHOLDER/adaempa-p9sil"
  },
  "schema:url": "https://astromat.org/products/adaempa-p9sil",
  "schema:dateModified": "2026-04-29",
  "schema:version": "0.1",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:creativeWorkStatus": "Draft",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Electron Microprobe Analysis (EMPA)",
    "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/EMPA"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-empa-p9sil",
      "schema:startDate": "2026-04-29",
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": [
            "nxs:BaseClass/NXinstrument",
            "ada:EMPAInstrument"
          ],
          "schema:name": "JEOL; Cameca JEOL 8530 F+ Hyperprobe FEG (Smithsonian)",
          "schema:identifier": [
            "ex:instrument-empa-001"
          ],
          "schema:manufacturer": {
            "@type": [
              "schema:Organization"
            ],
            "schema:name": "JEOL; Cameca"
          }
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Smithsonian Institution NMNH; University of Arizona (K-ALFAA)",
        "schema:additionalType": [
          "nxs:BaseClass/NXsource"
        ]
      },
      "schema:object": [
        {
          "@type": [
            "schema:Thing",
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalType": [
            "MaterialSample"
          ],
          "schema:name": "Sample analyzed in P9sil",
          "schema:identifier": [
            "igsn:10.60471/PLACEHOLDER-P9sil"
          ],
          "schema:description": "Sample of: Sheet silicates, pyrrhotite, pentlandite, magnetite"
        }
      ]
    }
  ],
  "schema:variableMeasured": [],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "adaEMPA-P9sil-archive.zip",
      "schema:description": "Archive containing tabular EMPA data for P9sil.",
      "schema:contentUrl": "https://astromat.org/downloads/adaempa-p9sil.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "0000000000000000000000000000000000000000000000000000000000000000"
      },
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 1048576,
        "schema:unitText": "byte"
      },
      "schema:hasPart": [
        {
          "@id": "ex:adaEMPA-P9sil-data-001",
          "@type": [
            "schema:MediaObject",
            "ada:tabularData",
            "cdi:TabularTextDataSet",
            "schema:Thing"
          ],
          "schema:name": "adaEMPA-P9sil-data.csv",
          "schema:description": "Per-point quantitative EMPA analyses (McCoy et al. 2025 (Bennu silicates, Nature)).",
          "schema:additionalType": [
            "ada:EMPAQEATabular"
          ],
          "schema:encodingFormat": [
            "text/csv"
          ],
          "cdi:isDelimited": true,
          "cdi:isFixedWidth": false,
          "csvw:delimiter": ",",
          "csvw:header": true,
          "ada:componentType": "ada:EMPAQEATabular",
          "ada:spectrometersUsed": "5x WDS",
          "ada:signalUsed": "Kα x-ray lines",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-p9sil"
          },
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/empaTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/acceleratingVoltage",
              "schema:name": "Default Accelerating Voltage",
              "schema:value": 15,
              "schema:unitText": "kV"
            },
            {
              "@id": "ada:parameter/empaTAPP/beamDiameter",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/beamDiameter",
              "schema:name": "Default Beam Diameter",
              "schema:value": "1 µm",
              "schema:unitText": "µm"
            }
          ],
          "cdif:hasPhysicalMapping": [
            {
              "cdif:index": 0,
              "cdif:physicalDataType": "String",
              "cdi:nullSequence": "NA"
            }
          ]
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:adaEMPA-P9sil-metadata",
    "schema:about": {
      "@id": "ex:adaEMPA-P9sil"
    },
    "schema:dateModified": "2026-04-29",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaEMPA"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaProduct"
      }
    ],
    "schema:maintainer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Astromat Data Archive"
    },
    "schema:sdDatePublished": "2026-04-29T12:00:00Z"
  }
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
      "csvw": "http://www.w3.org/ns/csvw#",
      "prov": "http://www.w3.org/ns/prov#",
      "dcterms": "http://purl.org/dc/terms/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/profiles/adaProfiles/adaEMPA/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "csvw": "http://www.w3.org/ns/csvw#",
      "prov": "http://www.w3.org/ns/prov#",
      "spdx": "http://spdx.org/rdf/terms#",
      "nxs": "http://purl.org/nexusformat/definitions/",
      "dcterms": "http://purl.org/dc/terms/",
      "ex": "https://example.org/",
      "dcat": "http://www.w3.org/ns/dcat#"
    }
  ],
  "@id": "ex:adaEMPA-P9sil",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "adaEMPA dataset for P9sil (McCoy et al. 2025 (Bennu silicates, Nature))",
  "schema:description": "Auto-generated adaEMPA profile-level Dataset for publication P9sil: McCoy et al. 2025 (Bennu silicates, Nature). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p9sil); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes.",
  "schema:additionalType": [
    "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.PLACEHOLDER/adaempa-p9sil"
  },
  "schema:url": "https://astromat.org/products/adaempa-p9sil",
  "schema:dateModified": "2026-04-29",
  "schema:version": "0.1",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:creativeWorkStatus": "Draft",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Electron Microprobe Analysis (EMPA)",
    "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/EMPA"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-empa-p9sil",
      "schema:startDate": "2026-04-29",
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": [
            "nxs:BaseClass/NXinstrument",
            "ada:EMPAInstrument"
          ],
          "schema:name": "JEOL; Cameca JEOL 8530 F+ Hyperprobe FEG (Smithsonian)",
          "schema:identifier": [
            "ex:instrument-empa-001"
          ],
          "schema:manufacturer": {
            "@type": [
              "schema:Organization"
            ],
            "schema:name": "JEOL; Cameca"
          }
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Smithsonian Institution NMNH; University of Arizona (K-ALFAA)",
        "schema:additionalType": [
          "nxs:BaseClass/NXsource"
        ]
      },
      "schema:object": [
        {
          "@type": [
            "schema:Thing",
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalType": [
            "MaterialSample"
          ],
          "schema:name": "Sample analyzed in P9sil",
          "schema:identifier": [
            "igsn:10.60471/PLACEHOLDER-P9sil"
          ],
          "schema:description": "Sample of: Sheet silicates, pyrrhotite, pentlandite, magnetite"
        }
      ]
    }
  ],
  "schema:variableMeasured": [],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "adaEMPA-P9sil-archive.zip",
      "schema:description": "Archive containing tabular EMPA data for P9sil.",
      "schema:contentUrl": "https://astromat.org/downloads/adaempa-p9sil.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "0000000000000000000000000000000000000000000000000000000000000000"
      },
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 1048576,
        "schema:unitText": "byte"
      },
      "schema:hasPart": [
        {
          "@id": "ex:adaEMPA-P9sil-data-001",
          "@type": [
            "schema:MediaObject",
            "ada:tabularData",
            "cdi:TabularTextDataSet",
            "schema:Thing"
          ],
          "schema:name": "adaEMPA-P9sil-data.csv",
          "schema:description": "Per-point quantitative EMPA analyses (McCoy et al. 2025 (Bennu silicates, Nature)).",
          "schema:additionalType": [
            "ada:EMPAQEATabular"
          ],
          "schema:encodingFormat": [
            "text/csv"
          ],
          "cdi:isDelimited": true,
          "cdi:isFixedWidth": false,
          "csvw:delimiter": ",",
          "csvw:header": true,
          "ada:componentType": "ada:EMPAQEATabular",
          "ada:spectrometersUsed": "5x WDS",
          "ada:signalUsed": "K\u03b1 x-ray lines",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-p9sil"
          },
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/empaTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/acceleratingVoltage",
              "schema:name": "Default Accelerating Voltage",
              "schema:value": 15,
              "schema:unitText": "kV"
            },
            {
              "@id": "ada:parameter/empaTAPP/beamDiameter",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/beamDiameter",
              "schema:name": "Default Beam Diameter",
              "schema:value": "1 \u00b5m",
              "schema:unitText": "\u00b5m"
            }
          ],
          "cdif:hasPhysicalMapping": [
            {
              "cdif:index": 0,
              "cdif:physicalDataType": "String",
              "cdi:nullSequence": "NA"
            }
          ]
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:adaEMPA-P9sil-metadata",
    "schema:about": {
      "@id": "ex:adaEMPA-P9sil"
    },
    "schema:dateModified": "2026-04-29",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaEMPA"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaProduct"
      }
    ],
    "schema:maintainer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Astromat Data Archive"
    },
    "schema:sdDatePublished": "2026-04-29T12:00:00Z"
  }
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://cdif.org/0.1/> .
@prefix csvw: <http://www.w3.org/ns/csvw#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix spdx: <http://spdx.org/rdf/terms#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://ada.astromat.org/metadata/parameter/empaTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:name "Default Accelerating Voltage" ;
    schema1:propertyID "ada:parameter/empaTAPP/acceleratingVoltage" ;
    schema1:unitText "kV" ;
    schema1:value 15 .

<https://ada.astromat.org/metadata/parameter/empaTAPP/beamDiameter> a schema1:PropertyValue ;
    schema1:name "Default Beam Diameter" ;
    schema1:propertyID "ada:parameter/empaTAPP/beamDiameter" ;
    schema1:unitText "µm" ;
    schema1:value "1 µm" .

ex:adaEMPA-P9sil a schema1:Dataset,
        schema1:Product ;
    schema1:additionalType "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
        "ada:DataDeliveryPackage" ;
    schema1:creativeWorkStatus "Draft" ;
    schema1:dateModified "2026-04-29" ;
    schema1:description "Auto-generated adaEMPA profile-level Dataset for publication P9sil: McCoy et al. 2025 (Bennu silicates, Nature). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p9sil); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes." ;
    schema1:distribution [ a schema1:DataDownload ;
            schema1:contentUrl "https://astromat.org/downloads/adaempa-p9sil.zip" ;
            schema1:description "Archive containing tabular EMPA data for P9sil." ;
            schema1:encodingFormat "application/zip" ;
            schema1:hasPart ex:adaEMPA-P9sil-data-001 ;
            schema1:name "adaEMPA-P9sil-archive.zip" ;
            schema1:size [ a schema1:QuantitativeValue ;
                    schema1:unitText "byte" ;
                    schema1:value 1048576 ] ;
            spdx:checksum [ a spdx:Checksum ;
                    spdx:algorithm "SHA256" ;
                    spdx:checksumValue "0000000000000000000000000000000000000000000000000000000000000000" ] ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://registry.identifiers.org/registry/doi" ;
            schema1:value "10.PLACEHOLDER/adaempa-p9sil" ] ;
    schema1:license "https://creativecommons.org/licenses/by/4.0/" ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:identifier "https://ada.astromat.org/vocabulary/techniques/EMPA" ;
            schema1:name "Electron Microprobe Analysis (EMPA)" ] ;
    schema1:name "adaEMPA dataset for P9sil (McCoy et al. 2025 (Bennu silicates, Nature))" ;
    schema1:subjectOf ex:adaEMPA-P9sil-metadata ;
    schema1:url "https://astromat.org/products/adaempa-p9sil" ;
    schema1:version "0.1" ;
    prov:wasGeneratedBy [ a schema1:Action,
                prov:Activity ;
            schema1:identifier "session-empa-p9sil" ;
            schema1:location [ a schema1:Place ;
                    schema1:additionalType "nxs:BaseClass/NXsource" ;
                    schema1:name "Smithsonian Institution NMNH; University of Arizona (K-ALFAA)" ] ;
            schema1:object [ a schema1:Thing,
                        <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalType "MaterialSample" ;
                    schema1:description "Sample of: Sheet silicates, pyrrhotite, pentlandite, magnetite" ;
                    schema1:identifier "igsn:10.60471/PLACEHOLDER-P9sil" ;
                    schema1:name "Sample analyzed in P9sil" ] ;
            schema1:startDate "2026-04-29" ;
            prov:used [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType "ada:EMPAInstrument",
                        "nxs:BaseClass/NXinstrument" ;
                    schema1:identifier "ex:instrument-empa-001" ;
                    schema1:manufacturer [ a schema1:Organization ;
                            schema1:name "JEOL; Cameca" ] ;
                    schema1:name "JEOL; Cameca JEOL 8530 F+ Hyperprobe FEG (Smithsonian)" ] ] .

ex:adaEMPA-P9sil-data-001 a cdi:TabularTextDataSet,
        schema1:MediaObject,
        schema1:Thing,
        ada:tabularData ;
    cdi:isDelimited true ;
    cdi:isFixedWidth false ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/empaTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/empaTAPP/beamDiameter> ;
    schema1:additionalType "ada:EMPAQEATabular" ;
    schema1:description "Per-point quantitative EMPA analyses (McCoy et al. 2025 (Bennu silicates, Nature))." ;
    schema1:encodingFormat "text/csv" ;
    schema1:measurementTechnique ex:empaTAPP-p9sil ;
    schema1:name "adaEMPA-P9sil-data.csv" ;
    csvw:delimiter "," ;
    csvw:header true ;
    ada:componentType "ada:EMPAQEATabular" ;
    ada:signalUsed "Kα x-ray lines" ;
    ada:spectrometersUsed "5x WDS" ;
    cdif:hasPhysicalMapping [ cdi:nullSequence "NA" ;
            cdif:index 0 ;
            cdif:physicalDataType "String" ] .

ex:adaEMPA-P9sil-metadata a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.0>,
        <https://w3id.org/cdif/data_description/1.0>,
        <https://w3id.org/cdif/discovery/1.0>,
        <https://w3id.org/cdif/manifest/1.0>,
        <https://w3id.org/cdif/provenance/1.0>,
        <https://w3id.org/geochem/metadata/profiles/adaEMPA>,
        <https://w3id.org/geochem/metadata/profiles/adaProduct> ;
    schema1:about ex:adaEMPA-P9sil ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:dateModified "2026-04-29" ;
    schema1:maintainer [ a schema1:Organization ;
            schema1:name "Astromat Data Archive" ] ;
    schema1:sdDatePublished "2026-04-29T12:00:00Z" .


```


### adaEMPA — P9carb (McCoy et al. 2025 (Bennu carbonates, Nature))
Auto-generated adaEMPA dataset record for publication P9carb.
schema:variableMeasured is derived from the empaTAPP TAPP definition's
ada:defaultAnalytes; schema:hasPart carries the paired detailEMPA fields
and references the TAPP via schema:measurementTechnique. Synthetic
placeholders are used for DOI, file size, and dates.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://cdif.org/0.1/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "prov": "http://www.w3.org/ns/prov#",
    "spdx": "http://spdx.org/rdf/terms#",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "dcterms": "http://purl.org/dc/terms/",
    "ex": "https://example.org/",
    "dcat": "http://www.w3.org/ns/dcat#"
  },
  "@id": "ex:adaEMPA-P9carb",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "adaEMPA dataset for P9carb (McCoy et al. 2025 (Bennu carbonates, Nature))",
  "schema:description": "Auto-generated adaEMPA profile-level Dataset for publication P9carb: McCoy et al. 2025 (Bennu carbonates, Nature). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p9carb); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes.",
  "schema:additionalType": [
    "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.PLACEHOLDER/adaempa-p9carb"
  },
  "schema:url": "https://astromat.org/products/adaempa-p9carb",
  "schema:dateModified": "2026-04-29",
  "schema:version": "0.1",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:creativeWorkStatus": "Draft",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Electron Microprobe Analysis (EMPA)",
    "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/EMPA"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-empa-p9carb",
      "schema:startDate": "2026-04-29",
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": [
            "nxs:BaseClass/NXinstrument",
            "ada:EMPAInstrument"
          ],
          "schema:name": "JEOL; Cameca Cameca SX-100 (U of Arizona)",
          "schema:identifier": [
            "ex:instrument-empa-001"
          ],
          "schema:manufacturer": {
            "@type": [
              "schema:Organization"
            ],
            "schema:name": "JEOL; Cameca"
          }
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Smithsonian Institution NMNH; University of Arizona (K-ALFAA)",
        "schema:additionalType": [
          "nxs:BaseClass/NXsource"
        ]
      },
      "schema:object": [
        {
          "@type": [
            "schema:Thing",
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalType": [
            "MaterialSample"
          ],
          "schema:name": "Sample analyzed in P9carb",
          "schema:identifier": [
            "igsn:10.60471/PLACEHOLDER-P9carb"
          ],
          "schema:description": "Sample of: calcite, dolomite, magnesite, Na carbonate"
        }
      ]
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "ex:adaEMPA-P9carb-var-Na",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Na",
      "schema:description": "Na abundance measured by EMPA WDS (calibrated against albite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Na"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P9carb-var-Si",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Si",
      "schema:description": "Si abundance measured by EMPA WDS (calibrated against Fo92 olivine).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Si"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P9carb-var-Mg",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Mg",
      "schema:description": "Mg abundance measured by EMPA WDS (calibrated against dolomite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Mg"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P9carb-var-Ca",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Ca",
      "schema:description": "Ca abundance measured by EMPA WDS (calibrated against calcite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Ca"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P9carb-var-Mn",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Mn",
      "schema:description": "Mn abundance measured by EMPA WDS (calibrated against Mn carbonate).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Mn"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P9carb-var-P",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "P",
      "schema:description": "P abundance measured by EMPA WDS (calibrated against apatite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/P"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P9carb-var-S",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "S",
      "schema:description": "S abundance measured by EMPA WDS (calibrated against baryte).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/S"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P9carb-var-Fe",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Fe",
      "schema:description": "Fe abundance measured by EMPA WDS (calibrated against fayalite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Fe"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "adaEMPA-P9carb-archive.zip",
      "schema:description": "Archive containing tabular EMPA data for P9carb.",
      "schema:contentUrl": "https://astromat.org/downloads/adaempa-p9carb.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "0000000000000000000000000000000000000000000000000000000000000000"
      },
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 1048576,
        "schema:unitText": "byte"
      },
      "schema:hasPart": [
        {
          "@id": "ex:adaEMPA-P9carb-data-001",
          "@type": [
            "schema:MediaObject",
            "ada:tabularData",
            "cdi:TabularTextDataSet",
            "schema:Thing"
          ],
          "schema:name": "adaEMPA-P9carb-data.csv",
          "schema:description": "Per-point quantitative EMPA analyses (McCoy et al. 2025 (Bennu carbonates, Nature)).",
          "schema:additionalType": [
            "ada:EMPAQEATabular"
          ],
          "schema:encodingFormat": [
            "text/csv"
          ],
          "cdi:isDelimited": true,
          "cdi:isFixedWidth": false,
          "csvw:delimiter": ",",
          "csvw:header": true,
          "ada:componentType": "ada:EMPAQEATabular",
          "ada:spectrometersUsed": "5x WDS",
          "ada:signalUsed": "Kα x-ray lines",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-p9carb"
          },
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/empaTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/acceleratingVoltage",
              "schema:name": "Default Accelerating Voltage",
              "schema:value": 15,
              "schema:unitText": "kV"
            },
            {
              "@id": "ada:parameter/empaTAPP/beamDiameter",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/beamDiameter",
              "schema:name": "Default Beam Diameter",
              "schema:value": "5 µm",
              "schema:unitText": "µm"
            },
            {
              "@id": "ada:parameter/empaTAPP/reportedAnalyte",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/reportedAnalyte",
              "schema:name": "Target Element",
              "schema:value": "Na|Si|Mg|Ca|Mn|P|S|Fe"
            }
          ],
          "cdif:hasPhysicalMapping": [
            {
              "cdif:index": 0,
              "cdif:physicalDataType": "String",
              "cdi:nullSequence": "NA"
            }
          ]
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:adaEMPA-P9carb-metadata",
    "schema:about": {
      "@id": "ex:adaEMPA-P9carb"
    },
    "schema:dateModified": "2026-04-29",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaEMPA"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaProduct"
      }
    ],
    "schema:maintainer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Astromat Data Archive"
    },
    "schema:sdDatePublished": "2026-04-29T12:00:00Z"
  }
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
      "csvw": "http://www.w3.org/ns/csvw#",
      "prov": "http://www.w3.org/ns/prov#",
      "dcterms": "http://purl.org/dc/terms/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/profiles/adaProfiles/adaEMPA/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://cdif.org/0.1/",
      "csvw": "http://www.w3.org/ns/csvw#",
      "prov": "http://www.w3.org/ns/prov#",
      "spdx": "http://spdx.org/rdf/terms#",
      "nxs": "http://purl.org/nexusformat/definitions/",
      "dcterms": "http://purl.org/dc/terms/",
      "ex": "https://example.org/",
      "dcat": "http://www.w3.org/ns/dcat#"
    }
  ],
  "@id": "ex:adaEMPA-P9carb",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "adaEMPA dataset for P9carb (McCoy et al. 2025 (Bennu carbonates, Nature))",
  "schema:description": "Auto-generated adaEMPA profile-level Dataset for publication P9carb: McCoy et al. 2025 (Bennu carbonates, Nature). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p9carb); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes.",
  "schema:additionalType": [
    "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.PLACEHOLDER/adaempa-p9carb"
  },
  "schema:url": "https://astromat.org/products/adaempa-p9carb",
  "schema:dateModified": "2026-04-29",
  "schema:version": "0.1",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:creativeWorkStatus": "Draft",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Electron Microprobe Analysis (EMPA)",
    "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/EMPA"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-empa-p9carb",
      "schema:startDate": "2026-04-29",
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": [
            "nxs:BaseClass/NXinstrument",
            "ada:EMPAInstrument"
          ],
          "schema:name": "JEOL; Cameca Cameca SX-100 (U of Arizona)",
          "schema:identifier": [
            "ex:instrument-empa-001"
          ],
          "schema:manufacturer": {
            "@type": [
              "schema:Organization"
            ],
            "schema:name": "JEOL; Cameca"
          }
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Smithsonian Institution NMNH; University of Arizona (K-ALFAA)",
        "schema:additionalType": [
          "nxs:BaseClass/NXsource"
        ]
      },
      "schema:object": [
        {
          "@type": [
            "schema:Thing",
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalType": [
            "MaterialSample"
          ],
          "schema:name": "Sample analyzed in P9carb",
          "schema:identifier": [
            "igsn:10.60471/PLACEHOLDER-P9carb"
          ],
          "schema:description": "Sample of: calcite, dolomite, magnesite, Na carbonate"
        }
      ]
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "ex:adaEMPA-P9carb-var-Na",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Na",
      "schema:description": "Na abundance measured by EMPA WDS (calibrated against albite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Na"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P9carb-var-Si",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Si",
      "schema:description": "Si abundance measured by EMPA WDS (calibrated against Fo92 olivine).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Si"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P9carb-var-Mg",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Mg",
      "schema:description": "Mg abundance measured by EMPA WDS (calibrated against dolomite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Mg"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P9carb-var-Ca",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Ca",
      "schema:description": "Ca abundance measured by EMPA WDS (calibrated against calcite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Ca"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P9carb-var-Mn",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Mn",
      "schema:description": "Mn abundance measured by EMPA WDS (calibrated against Mn carbonate).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Mn"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P9carb-var-P",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "P",
      "schema:description": "P abundance measured by EMPA WDS (calibrated against apatite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/P"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P9carb-var-S",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "S",
      "schema:description": "S abundance measured by EMPA WDS (calibrated against baryte).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/S"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P9carb-var-Fe",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Fe",
      "schema:description": "Fe abundance measured by EMPA WDS (calibrated against fayalite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Fe"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "adaEMPA-P9carb-archive.zip",
      "schema:description": "Archive containing tabular EMPA data for P9carb.",
      "schema:contentUrl": "https://astromat.org/downloads/adaempa-p9carb.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "0000000000000000000000000000000000000000000000000000000000000000"
      },
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 1048576,
        "schema:unitText": "byte"
      },
      "schema:hasPart": [
        {
          "@id": "ex:adaEMPA-P9carb-data-001",
          "@type": [
            "schema:MediaObject",
            "ada:tabularData",
            "cdi:TabularTextDataSet",
            "schema:Thing"
          ],
          "schema:name": "adaEMPA-P9carb-data.csv",
          "schema:description": "Per-point quantitative EMPA analyses (McCoy et al. 2025 (Bennu carbonates, Nature)).",
          "schema:additionalType": [
            "ada:EMPAQEATabular"
          ],
          "schema:encodingFormat": [
            "text/csv"
          ],
          "cdi:isDelimited": true,
          "cdi:isFixedWidth": false,
          "csvw:delimiter": ",",
          "csvw:header": true,
          "ada:componentType": "ada:EMPAQEATabular",
          "ada:spectrometersUsed": "5x WDS",
          "ada:signalUsed": "K\u03b1 x-ray lines",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-p9carb"
          },
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/empaTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/acceleratingVoltage",
              "schema:name": "Default Accelerating Voltage",
              "schema:value": 15,
              "schema:unitText": "kV"
            },
            {
              "@id": "ada:parameter/empaTAPP/beamDiameter",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/beamDiameter",
              "schema:name": "Default Beam Diameter",
              "schema:value": "5 \u00b5m",
              "schema:unitText": "\u00b5m"
            },
            {
              "@id": "ada:parameter/empaTAPP/reportedAnalyte",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/reportedAnalyte",
              "schema:name": "Target Element",
              "schema:value": "Na|Si|Mg|Ca|Mn|P|S|Fe"
            }
          ],
          "cdif:hasPhysicalMapping": [
            {
              "cdif:index": 0,
              "cdif:physicalDataType": "String",
              "cdi:nullSequence": "NA"
            }
          ]
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:adaEMPA-P9carb-metadata",
    "schema:about": {
      "@id": "ex:adaEMPA-P9carb"
    },
    "schema:dateModified": "2026-04-29",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaEMPA"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaProduct"
      }
    ],
    "schema:maintainer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Astromat Data Archive"
    },
    "schema:sdDatePublished": "2026-04-29T12:00:00Z"
  }
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://cdif.org/0.1/> .
@prefix csvw: <http://www.w3.org/ns/csvw#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix spdx: <http://spdx.org/rdf/terms#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://ada.astromat.org/metadata/parameter/empaTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:name "Default Accelerating Voltage" ;
    schema1:propertyID "ada:parameter/empaTAPP/acceleratingVoltage" ;
    schema1:unitText "kV" ;
    schema1:value 15 .

<https://ada.astromat.org/metadata/parameter/empaTAPP/beamDiameter> a schema1:PropertyValue ;
    schema1:name "Default Beam Diameter" ;
    schema1:propertyID "ada:parameter/empaTAPP/beamDiameter" ;
    schema1:unitText "µm" ;
    schema1:value "5 µm" .

<https://ada.astromat.org/metadata/parameter/empaTAPP/reportedAnalyte> a schema1:PropertyValue ;
    schema1:name "Target Element" ;
    schema1:propertyID "ada:parameter/empaTAPP/reportedAnalyte" ;
    schema1:value "Na|Si|Mg|Ca|Mn|P|S|Fe" .

ex:adaEMPA-P9carb a schema1:Dataset,
        schema1:Product ;
    schema1:additionalType "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
        "ada:DataDeliveryPackage" ;
    schema1:creativeWorkStatus "Draft" ;
    schema1:dateModified "2026-04-29" ;
    schema1:description "Auto-generated adaEMPA profile-level Dataset for publication P9carb: McCoy et al. 2025 (Bennu carbonates, Nature). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p9carb); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes." ;
    schema1:distribution [ a schema1:DataDownload ;
            schema1:contentUrl "https://astromat.org/downloads/adaempa-p9carb.zip" ;
            schema1:description "Archive containing tabular EMPA data for P9carb." ;
            schema1:encodingFormat "application/zip" ;
            schema1:hasPart ex:adaEMPA-P9carb-data-001 ;
            schema1:name "adaEMPA-P9carb-archive.zip" ;
            schema1:size [ a schema1:QuantitativeValue ;
                    schema1:unitText "byte" ;
                    schema1:value 1048576 ] ;
            spdx:checksum [ a spdx:Checksum ;
                    spdx:algorithm "SHA256" ;
                    spdx:checksumValue "0000000000000000000000000000000000000000000000000000000000000000" ] ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://registry.identifiers.org/registry/doi" ;
            schema1:value "10.PLACEHOLDER/adaempa-p9carb" ] ;
    schema1:license "https://creativecommons.org/licenses/by/4.0/" ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:identifier "https://ada.astromat.org/vocabulary/techniques/EMPA" ;
            schema1:name "Electron Microprobe Analysis (EMPA)" ] ;
    schema1:name "adaEMPA dataset for P9carb (McCoy et al. 2025 (Bennu carbonates, Nature))" ;
    schema1:subjectOf ex:adaEMPA-P9carb-metadata ;
    schema1:url "https://astromat.org/products/adaempa-p9carb" ;
    schema1:variableMeasured ex:adaEMPA-P9carb-var-Ca,
        ex:adaEMPA-P9carb-var-Fe,
        ex:adaEMPA-P9carb-var-Mg,
        ex:adaEMPA-P9carb-var-Mn,
        ex:adaEMPA-P9carb-var-Na,
        ex:adaEMPA-P9carb-var-P,
        ex:adaEMPA-P9carb-var-S,
        ex:adaEMPA-P9carb-var-Si ;
    schema1:version "0.1" ;
    prov:wasGeneratedBy [ a schema1:Action,
                prov:Activity ;
            schema1:identifier "session-empa-p9carb" ;
            schema1:location [ a schema1:Place ;
                    schema1:additionalType "nxs:BaseClass/NXsource" ;
                    schema1:name "Smithsonian Institution NMNH; University of Arizona (K-ALFAA)" ] ;
            schema1:object [ a schema1:Thing,
                        <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalType "MaterialSample" ;
                    schema1:description "Sample of: calcite, dolomite, magnesite, Na carbonate" ;
                    schema1:identifier "igsn:10.60471/PLACEHOLDER-P9carb" ;
                    schema1:name "Sample analyzed in P9carb" ] ;
            schema1:startDate "2026-04-29" ;
            prov:used [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType "ada:EMPAInstrument",
                        "nxs:BaseClass/NXinstrument" ;
                    schema1:identifier "ex:instrument-empa-001" ;
                    schema1:manufacturer [ a schema1:Organization ;
                            schema1:name "JEOL; Cameca" ] ;
                    schema1:name "JEOL; Cameca Cameca SX-100 (U of Arizona)" ] ] .

ex:adaEMPA-P9carb-data-001 a cdi:TabularTextDataSet,
        schema1:MediaObject,
        schema1:Thing,
        ada:tabularData ;
    cdi:isDelimited true ;
    cdi:isFixedWidth false ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/empaTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/empaTAPP/beamDiameter>,
        <https://ada.astromat.org/metadata/parameter/empaTAPP/reportedAnalyte> ;
    schema1:additionalType "ada:EMPAQEATabular" ;
    schema1:description "Per-point quantitative EMPA analyses (McCoy et al. 2025 (Bennu carbonates, Nature))." ;
    schema1:encodingFormat "text/csv" ;
    schema1:measurementTechnique ex:empaTAPP-p9carb ;
    schema1:name "adaEMPA-P9carb-data.csv" ;
    csvw:delimiter "," ;
    csvw:header true ;
    ada:componentType "ada:EMPAQEATabular" ;
    ada:signalUsed "Kα x-ray lines" ;
    ada:spectrometersUsed "5x WDS" ;
    cdif:hasPhysicalMapping [ cdi:nullSequence "NA" ;
            cdif:index 0 ;
            cdif:physicalDataType "String" ] .

ex:adaEMPA-P9carb-metadata a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.0>,
        <https://w3id.org/cdif/data_description/1.0>,
        <https://w3id.org/cdif/discovery/1.0>,
        <https://w3id.org/cdif/manifest/1.0>,
        <https://w3id.org/cdif/provenance/1.0>,
        <https://w3id.org/geochem/metadata/profiles/adaEMPA>,
        <https://w3id.org/geochem/metadata/profiles/adaProduct> ;
    schema1:about ex:adaEMPA-P9carb ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:dateModified "2026-04-29" ;
    schema1:maintainer [ a schema1:Organization ;
            schema1:name "Astromat Data Archive" ] ;
    schema1:sdDatePublished "2026-04-29T12:00:00Z" .

ex:adaEMPA-P9carb-var-Ca a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Ca abundance measured by EMPA WDS (calibrated against calcite)." ;
    schema1:name "Ca" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Ca" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P9carb-var-Fe a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Fe abundance measured by EMPA WDS (calibrated against fayalite)." ;
    schema1:name "Fe" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Fe" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P9carb-var-Mg a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Mg abundance measured by EMPA WDS (calibrated against dolomite)." ;
    schema1:name "Mg" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Mg" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P9carb-var-Mn a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Mn abundance measured by EMPA WDS (calibrated against Mn carbonate)." ;
    schema1:name "Mn" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Mn" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P9carb-var-Na a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Na abundance measured by EMPA WDS (calibrated against albite)." ;
    schema1:name "Na" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Na" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P9carb-var-P a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "P abundance measured by EMPA WDS (calibrated against apatite)." ;
    schema1:name "P" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/P" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P9carb-var-S a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "S abundance measured by EMPA WDS (calibrated against baryte)." ;
    schema1:name "S" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/S" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P9carb-var-Si a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Si abundance measured by EMPA WDS (calibrated against Fo92 olivine)." ;
    schema1:name "Si" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Si" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .


```


### adaEMPA — P9phos (McCoy et al. 2025 (Bennu phosphates, Nature))
Auto-generated adaEMPA dataset record for publication P9phos.
schema:variableMeasured is derived from the empaTAPP TAPP definition's
ada:defaultAnalytes; schema:hasPart carries the paired detailEMPA fields
and references the TAPP via schema:measurementTechnique. Synthetic
placeholders are used for DOI, file size, and dates.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://cdif.org/0.1/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "prov": "http://www.w3.org/ns/prov#",
    "spdx": "http://spdx.org/rdf/terms#",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "dcterms": "http://purl.org/dc/terms/",
    "ex": "https://example.org/",
    "dcat": "http://www.w3.org/ns/dcat#"
  },
  "@id": "ex:adaEMPA-P9phos",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "adaEMPA dataset for P9phos (McCoy et al. 2025 (Bennu phosphates, Nature))",
  "schema:description": "Auto-generated adaEMPA profile-level Dataset for publication P9phos: McCoy et al. 2025 (Bennu phosphates, Nature). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p9phos); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes.",
  "schema:additionalType": [
    "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.PLACEHOLDER/adaempa-p9phos"
  },
  "schema:url": "https://astromat.org/products/adaempa-p9phos",
  "schema:dateModified": "2026-04-29",
  "schema:version": "0.1",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:creativeWorkStatus": "Draft",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Electron Microprobe Analysis (EMPA)",
    "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/EMPA"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-empa-p9phos",
      "schema:startDate": "2026-04-29",
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": [
            "nxs:BaseClass/NXinstrument",
            "ada:EMPAInstrument"
          ],
          "schema:name": "JEOL; Cameca Cameca SX-100 (U of Arizona)",
          "schema:identifier": [
            "ex:instrument-empa-001"
          ],
          "schema:manufacturer": {
            "@type": [
              "schema:Organization"
            ],
            "schema:name": "JEOL; Cameca"
          }
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Smithsonian Institution NMNH; University of Arizona (K-ALFAA)",
        "schema:additionalType": [
          "nxs:BaseClass/NXsource"
        ]
      },
      "schema:object": [
        {
          "@type": [
            "schema:Thing",
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalType": [
            "MaterialSample"
          ],
          "schema:name": "Sample analyzed in P9phos",
          "schema:identifier": [
            "igsn:10.60471/PLACEHOLDER-P9phos"
          ],
          "schema:description": "Sample of: Mg Phosphate, Na phosphate"
        }
      ]
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "ex:adaEMPA-P9phos-var-F",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "F",
      "schema:description": "F abundance measured by EMPA WDS (calibrated against fluorapatite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/F"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P9phos-var-P",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "P",
      "schema:description": "P abundance measured by EMPA WDS (calibrated against fluorapatite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/P"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P9phos-var-Ca",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Ca",
      "schema:description": "Ca abundance measured by EMPA WDS (calibrated against fluorapatite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Ca"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P9phos-var-Si",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Si",
      "schema:description": "Si abundance measured by EMPA WDS (calibrated against Fo92 olivine).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Si"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P9phos-var-Mg",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Mg",
      "schema:description": "Mg abundance measured by EMPA WDS (calibrated against Fo92 olivine).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Mg"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P9phos-var-Mn",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Mn",
      "schema:description": "Mn abundance measured by EMPA WDS (calibrated against rhodonite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Mn"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P9phos-var-Fe",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Fe",
      "schema:description": "Fe abundance measured by EMPA WDS (calibrated against fayalite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Fe"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P9phos-var-Al",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Al",
      "schema:description": "Al abundance measured by EMPA WDS (calibrated against anorthite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Al"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P9phos-var-S",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "S",
      "schema:description": "S abundance measured by EMPA WDS (calibrated against baryte).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/S"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P9phos-var-K",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "K",
      "schema:description": "K abundance measured by EMPA WDS (calibrated against K-feldspar).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/K"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P9phos-var-Cl",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Cl",
      "schema:description": "Cl abundance measured by EMPA WDS (calibrated against scapolite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Cl"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "adaEMPA-P9phos-archive.zip",
      "schema:description": "Archive containing tabular EMPA data for P9phos.",
      "schema:contentUrl": "https://astromat.org/downloads/adaempa-p9phos.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "0000000000000000000000000000000000000000000000000000000000000000"
      },
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 1048576,
        "schema:unitText": "byte"
      },
      "schema:hasPart": [
        {
          "@id": "ex:adaEMPA-P9phos-data-001",
          "@type": [
            "schema:MediaObject",
            "ada:tabularData",
            "cdi:TabularTextDataSet",
            "schema:Thing"
          ],
          "schema:name": "adaEMPA-P9phos-data.csv",
          "schema:description": "Per-point quantitative EMPA analyses (McCoy et al. 2025 (Bennu phosphates, Nature)).",
          "schema:additionalType": [
            "ada:EMPAQEATabular"
          ],
          "schema:encodingFormat": [
            "text/csv"
          ],
          "cdi:isDelimited": true,
          "cdi:isFixedWidth": false,
          "csvw:delimiter": ",",
          "csvw:header": true,
          "ada:componentType": "ada:EMPAQEATabular",
          "ada:spectrometersUsed": "5x WDS",
          "ada:signalUsed": "Kα x-ray lines",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-p9phos"
          },
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/empaTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/acceleratingVoltage",
              "schema:name": "Default Accelerating Voltage",
              "schema:value": 15,
              "schema:unitText": "kV"
            },
            {
              "@id": "ada:parameter/empaTAPP/beamDiameter",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/beamDiameter",
              "schema:name": "Default Beam Diameter",
              "schema:value": "2 µm",
              "schema:unitText": "µm"
            },
            {
              "@id": "ada:parameter/empaTAPP/reportedAnalyte",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/reportedAnalyte",
              "schema:name": "Target Element",
              "schema:value": "F|P|Ca|Si|Mg|Mn|Fe|Al|S|K|Cl"
            }
          ],
          "cdif:hasPhysicalMapping": [
            {
              "cdif:index": 0,
              "cdif:physicalDataType": "String",
              "cdi:nullSequence": "NA"
            }
          ]
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:adaEMPA-P9phos-metadata",
    "schema:about": {
      "@id": "ex:adaEMPA-P9phos"
    },
    "schema:dateModified": "2026-04-29",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaEMPA"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaProduct"
      }
    ],
    "schema:maintainer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Astromat Data Archive"
    },
    "schema:sdDatePublished": "2026-04-29T12:00:00Z"
  }
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
      "csvw": "http://www.w3.org/ns/csvw#",
      "prov": "http://www.w3.org/ns/prov#",
      "dcterms": "http://purl.org/dc/terms/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/profiles/adaProfiles/adaEMPA/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://cdif.org/0.1/",
      "csvw": "http://www.w3.org/ns/csvw#",
      "prov": "http://www.w3.org/ns/prov#",
      "spdx": "http://spdx.org/rdf/terms#",
      "nxs": "http://purl.org/nexusformat/definitions/",
      "dcterms": "http://purl.org/dc/terms/",
      "ex": "https://example.org/",
      "dcat": "http://www.w3.org/ns/dcat#"
    }
  ],
  "@id": "ex:adaEMPA-P9phos",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "adaEMPA dataset for P9phos (McCoy et al. 2025 (Bennu phosphates, Nature))",
  "schema:description": "Auto-generated adaEMPA profile-level Dataset for publication P9phos: McCoy et al. 2025 (Bennu phosphates, Nature). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p9phos); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes.",
  "schema:additionalType": [
    "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.PLACEHOLDER/adaempa-p9phos"
  },
  "schema:url": "https://astromat.org/products/adaempa-p9phos",
  "schema:dateModified": "2026-04-29",
  "schema:version": "0.1",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:creativeWorkStatus": "Draft",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Electron Microprobe Analysis (EMPA)",
    "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/EMPA"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-empa-p9phos",
      "schema:startDate": "2026-04-29",
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": [
            "nxs:BaseClass/NXinstrument",
            "ada:EMPAInstrument"
          ],
          "schema:name": "JEOL; Cameca Cameca SX-100 (U of Arizona)",
          "schema:identifier": [
            "ex:instrument-empa-001"
          ],
          "schema:manufacturer": {
            "@type": [
              "schema:Organization"
            ],
            "schema:name": "JEOL; Cameca"
          }
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Smithsonian Institution NMNH; University of Arizona (K-ALFAA)",
        "schema:additionalType": [
          "nxs:BaseClass/NXsource"
        ]
      },
      "schema:object": [
        {
          "@type": [
            "schema:Thing",
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalType": [
            "MaterialSample"
          ],
          "schema:name": "Sample analyzed in P9phos",
          "schema:identifier": [
            "igsn:10.60471/PLACEHOLDER-P9phos"
          ],
          "schema:description": "Sample of: Mg Phosphate, Na phosphate"
        }
      ]
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "ex:adaEMPA-P9phos-var-F",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "F",
      "schema:description": "F abundance measured by EMPA WDS (calibrated against fluorapatite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/F"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P9phos-var-P",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "P",
      "schema:description": "P abundance measured by EMPA WDS (calibrated against fluorapatite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/P"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P9phos-var-Ca",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Ca",
      "schema:description": "Ca abundance measured by EMPA WDS (calibrated against fluorapatite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Ca"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P9phos-var-Si",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Si",
      "schema:description": "Si abundance measured by EMPA WDS (calibrated against Fo92 olivine).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Si"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P9phos-var-Mg",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Mg",
      "schema:description": "Mg abundance measured by EMPA WDS (calibrated against Fo92 olivine).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Mg"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P9phos-var-Mn",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Mn",
      "schema:description": "Mn abundance measured by EMPA WDS (calibrated against rhodonite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Mn"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P9phos-var-Fe",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Fe",
      "schema:description": "Fe abundance measured by EMPA WDS (calibrated against fayalite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Fe"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P9phos-var-Al",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Al",
      "schema:description": "Al abundance measured by EMPA WDS (calibrated against anorthite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Al"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P9phos-var-S",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "S",
      "schema:description": "S abundance measured by EMPA WDS (calibrated against baryte).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/S"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P9phos-var-K",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "K",
      "schema:description": "K abundance measured by EMPA WDS (calibrated against K-feldspar).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/K"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    },
    {
      "@id": "ex:adaEMPA-P9phos-var-Cl",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "Cl",
      "schema:description": "Cl abundance measured by EMPA WDS (calibrated against scapolite).",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/analytes/Cl"
      ],
      "schema:unitText": "wt%",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%",
      "cdif:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ]
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "adaEMPA-P9phos-archive.zip",
      "schema:description": "Archive containing tabular EMPA data for P9phos.",
      "schema:contentUrl": "https://astromat.org/downloads/adaempa-p9phos.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "0000000000000000000000000000000000000000000000000000000000000000"
      },
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 1048576,
        "schema:unitText": "byte"
      },
      "schema:hasPart": [
        {
          "@id": "ex:adaEMPA-P9phos-data-001",
          "@type": [
            "schema:MediaObject",
            "ada:tabularData",
            "cdi:TabularTextDataSet",
            "schema:Thing"
          ],
          "schema:name": "adaEMPA-P9phos-data.csv",
          "schema:description": "Per-point quantitative EMPA analyses (McCoy et al. 2025 (Bennu phosphates, Nature)).",
          "schema:additionalType": [
            "ada:EMPAQEATabular"
          ],
          "schema:encodingFormat": [
            "text/csv"
          ],
          "cdi:isDelimited": true,
          "cdi:isFixedWidth": false,
          "csvw:delimiter": ",",
          "csvw:header": true,
          "ada:componentType": "ada:EMPAQEATabular",
          "ada:spectrometersUsed": "5x WDS",
          "ada:signalUsed": "K\u03b1 x-ray lines",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-p9phos"
          },
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/empaTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/acceleratingVoltage",
              "schema:name": "Default Accelerating Voltage",
              "schema:value": 15,
              "schema:unitText": "kV"
            },
            {
              "@id": "ada:parameter/empaTAPP/beamDiameter",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/beamDiameter",
              "schema:name": "Default Beam Diameter",
              "schema:value": "2 \u00b5m",
              "schema:unitText": "\u00b5m"
            },
            {
              "@id": "ada:parameter/empaTAPP/reportedAnalyte",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/reportedAnalyte",
              "schema:name": "Target Element",
              "schema:value": "F|P|Ca|Si|Mg|Mn|Fe|Al|S|K|Cl"
            }
          ],
          "cdif:hasPhysicalMapping": [
            {
              "cdif:index": 0,
              "cdif:physicalDataType": "String",
              "cdi:nullSequence": "NA"
            }
          ]
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:adaEMPA-P9phos-metadata",
    "schema:about": {
      "@id": "ex:adaEMPA-P9phos"
    },
    "schema:dateModified": "2026-04-29",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaEMPA"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaProduct"
      }
    ],
    "schema:maintainer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Astromat Data Archive"
    },
    "schema:sdDatePublished": "2026-04-29T12:00:00Z"
  }
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://cdif.org/0.1/> .
@prefix csvw: <http://www.w3.org/ns/csvw#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix spdx: <http://spdx.org/rdf/terms#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://ada.astromat.org/metadata/parameter/empaTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:name "Default Accelerating Voltage" ;
    schema1:propertyID "ada:parameter/empaTAPP/acceleratingVoltage" ;
    schema1:unitText "kV" ;
    schema1:value 15 .

<https://ada.astromat.org/metadata/parameter/empaTAPP/beamDiameter> a schema1:PropertyValue ;
    schema1:name "Default Beam Diameter" ;
    schema1:propertyID "ada:parameter/empaTAPP/beamDiameter" ;
    schema1:unitText "µm" ;
    schema1:value "2 µm" .

<https://ada.astromat.org/metadata/parameter/empaTAPP/reportedAnalyte> a schema1:PropertyValue ;
    schema1:name "Target Element" ;
    schema1:propertyID "ada:parameter/empaTAPP/reportedAnalyte" ;
    schema1:value "F|P|Ca|Si|Mg|Mn|Fe|Al|S|K|Cl" .

ex:adaEMPA-P9phos a schema1:Dataset,
        schema1:Product ;
    schema1:additionalType "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
        "ada:DataDeliveryPackage" ;
    schema1:creativeWorkStatus "Draft" ;
    schema1:dateModified "2026-04-29" ;
    schema1:description "Auto-generated adaEMPA profile-level Dataset for publication P9phos: McCoy et al. 2025 (Bennu phosphates, Nature). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p9phos); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes." ;
    schema1:distribution [ a schema1:DataDownload ;
            schema1:contentUrl "https://astromat.org/downloads/adaempa-p9phos.zip" ;
            schema1:description "Archive containing tabular EMPA data for P9phos." ;
            schema1:encodingFormat "application/zip" ;
            schema1:hasPart ex:adaEMPA-P9phos-data-001 ;
            schema1:name "adaEMPA-P9phos-archive.zip" ;
            schema1:size [ a schema1:QuantitativeValue ;
                    schema1:unitText "byte" ;
                    schema1:value 1048576 ] ;
            spdx:checksum [ a spdx:Checksum ;
                    spdx:algorithm "SHA256" ;
                    spdx:checksumValue "0000000000000000000000000000000000000000000000000000000000000000" ] ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://registry.identifiers.org/registry/doi" ;
            schema1:value "10.PLACEHOLDER/adaempa-p9phos" ] ;
    schema1:license "https://creativecommons.org/licenses/by/4.0/" ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:identifier "https://ada.astromat.org/vocabulary/techniques/EMPA" ;
            schema1:name "Electron Microprobe Analysis (EMPA)" ] ;
    schema1:name "adaEMPA dataset for P9phos (McCoy et al. 2025 (Bennu phosphates, Nature))" ;
    schema1:subjectOf ex:adaEMPA-P9phos-metadata ;
    schema1:url "https://astromat.org/products/adaempa-p9phos" ;
    schema1:variableMeasured ex:adaEMPA-P9phos-var-Al,
        ex:adaEMPA-P9phos-var-Ca,
        ex:adaEMPA-P9phos-var-Cl,
        ex:adaEMPA-P9phos-var-F,
        ex:adaEMPA-P9phos-var-Fe,
        ex:adaEMPA-P9phos-var-K,
        ex:adaEMPA-P9phos-var-Mg,
        ex:adaEMPA-P9phos-var-Mn,
        ex:adaEMPA-P9phos-var-P,
        ex:adaEMPA-P9phos-var-S,
        ex:adaEMPA-P9phos-var-Si ;
    schema1:version "0.1" ;
    prov:wasGeneratedBy [ a schema1:Action,
                prov:Activity ;
            schema1:identifier "session-empa-p9phos" ;
            schema1:location [ a schema1:Place ;
                    schema1:additionalType "nxs:BaseClass/NXsource" ;
                    schema1:name "Smithsonian Institution NMNH; University of Arizona (K-ALFAA)" ] ;
            schema1:object [ a schema1:Thing,
                        <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalType "MaterialSample" ;
                    schema1:description "Sample of: Mg Phosphate, Na phosphate" ;
                    schema1:identifier "igsn:10.60471/PLACEHOLDER-P9phos" ;
                    schema1:name "Sample analyzed in P9phos" ] ;
            schema1:startDate "2026-04-29" ;
            prov:used [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType "ada:EMPAInstrument",
                        "nxs:BaseClass/NXinstrument" ;
                    schema1:identifier "ex:instrument-empa-001" ;
                    schema1:manufacturer [ a schema1:Organization ;
                            schema1:name "JEOL; Cameca" ] ;
                    schema1:name "JEOL; Cameca Cameca SX-100 (U of Arizona)" ] ] .

ex:adaEMPA-P9phos-data-001 a cdi:TabularTextDataSet,
        schema1:MediaObject,
        schema1:Thing,
        ada:tabularData ;
    cdi:isDelimited true ;
    cdi:isFixedWidth false ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/empaTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/empaTAPP/beamDiameter>,
        <https://ada.astromat.org/metadata/parameter/empaTAPP/reportedAnalyte> ;
    schema1:additionalType "ada:EMPAQEATabular" ;
    schema1:description "Per-point quantitative EMPA analyses (McCoy et al. 2025 (Bennu phosphates, Nature))." ;
    schema1:encodingFormat "text/csv" ;
    schema1:measurementTechnique ex:empaTAPP-p9phos ;
    schema1:name "adaEMPA-P9phos-data.csv" ;
    csvw:delimiter "," ;
    csvw:header true ;
    ada:componentType "ada:EMPAQEATabular" ;
    ada:signalUsed "Kα x-ray lines" ;
    ada:spectrometersUsed "5x WDS" ;
    cdif:hasPhysicalMapping [ cdi:nullSequence "NA" ;
            cdif:index 0 ;
            cdif:physicalDataType "String" ] .

ex:adaEMPA-P9phos-metadata a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.0>,
        <https://w3id.org/cdif/data_description/1.0>,
        <https://w3id.org/cdif/discovery/1.0>,
        <https://w3id.org/cdif/manifest/1.0>,
        <https://w3id.org/cdif/provenance/1.0>,
        <https://w3id.org/geochem/metadata/profiles/adaEMPA>,
        <https://w3id.org/geochem/metadata/profiles/adaProduct> ;
    schema1:about ex:adaEMPA-P9phos ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:dateModified "2026-04-29" ;
    schema1:maintainer [ a schema1:Organization ;
            schema1:name "Astromat Data Archive" ] ;
    schema1:sdDatePublished "2026-04-29T12:00:00Z" .

ex:adaEMPA-P9phos-var-Al a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Al abundance measured by EMPA WDS (calibrated against anorthite)." ;
    schema1:name "Al" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Al" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P9phos-var-Ca a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Ca abundance measured by EMPA WDS (calibrated against fluorapatite)." ;
    schema1:name "Ca" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Ca" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P9phos-var-Cl a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Cl abundance measured by EMPA WDS (calibrated against scapolite)." ;
    schema1:name "Cl" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Cl" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P9phos-var-F a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "F abundance measured by EMPA WDS (calibrated against fluorapatite)." ;
    schema1:name "F" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/F" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P9phos-var-Fe a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Fe abundance measured by EMPA WDS (calibrated against fayalite)." ;
    schema1:name "Fe" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Fe" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P9phos-var-K a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "K abundance measured by EMPA WDS (calibrated against K-feldspar)." ;
    schema1:name "K" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/K" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P9phos-var-Mg a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Mg abundance measured by EMPA WDS (calibrated against Fo92 olivine)." ;
    schema1:name "Mg" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Mg" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P9phos-var-Mn a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Mn abundance measured by EMPA WDS (calibrated against rhodonite)." ;
    schema1:name "Mn" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Mn" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P9phos-var-P a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "P abundance measured by EMPA WDS (calibrated against fluorapatite)." ;
    schema1:name "P" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/P" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P9phos-var-S a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "S abundance measured by EMPA WDS (calibrated against baryte)." ;
    schema1:name "S" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/S" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaEMPA-P9phos-var-Si a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Si abundance measured by EMPA WDS (calibrated against Fo92 olivine)." ;
    schema1:name "Si" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/analytes/Si" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .


```


### adaEMPA — P10 (Pang et al. 2016 (NWA 8003 eucrite, Sci. Rep.))
Auto-generated adaEMPA dataset record for publication P10.
schema:variableMeasured is derived from the empaTAPP TAPP definition's
ada:defaultAnalytes; schema:hasPart carries the paired detailEMPA fields
and references the TAPP via schema:measurementTechnique. Synthetic
placeholders are used for DOI, file size, and dates.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "prov": "http://www.w3.org/ns/prov#",
    "spdx": "http://spdx.org/rdf/terms#",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "dcterms": "http://purl.org/dc/terms/",
    "ex": "https://example.org/",
    "dcat": "http://www.w3.org/ns/dcat#"
  },
  "@id": "ex:adaEMPA-P10",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "adaEMPA dataset for P10 (Pang et al. 2016 (NWA 8003 eucrite, Sci. Rep.))",
  "schema:description": "Auto-generated adaEMPA profile-level Dataset for publication P10: Pang et al. 2016 (NWA 8003 eucrite, Sci. Rep.). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p10); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes.",
  "schema:additionalType": [
    "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.PLACEHOLDER/adaempa-p10"
  },
  "schema:url": "https://astromat.org/products/adaempa-p10",
  "schema:dateModified": "2026-04-29",
  "schema:version": "0.1",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:creativeWorkStatus": "Draft",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Electron Microprobe Analysis (EMPA)",
    "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/EMPA"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-empa-p10",
      "schema:startDate": "2026-04-29",
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": [
            "nxs:BaseClass/NXinstrument",
            "ada:EMPAInstrument"
          ],
          "schema:name": "JEOL JEOL 8100",
          "schema:identifier": [
            "ex:instrument-empa-001"
          ],
          "schema:manufacturer": {
            "@type": [
              "schema:Organization"
            ],
            "schema:name": "JEOL"
          }
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Nanjing University",
        "schema:additionalType": [
          "nxs:BaseClass/NXsource"
        ]
      },
      "schema:object": [
        {
          "@type": [
            "schema:Thing",
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalType": [
            "MaterialSample"
          ],
          "schema:name": "Sample analyzed in P10",
          "schema:identifier": [
            "igsn:10.60471/PLACEHOLDER-P10"
          ],
          "schema:description": "Sample of: orthopyroxene, augite,  maskelynite, garnet, clinopyroxene, silica phases"
        }
      ]
    }
  ],
  "schema:variableMeasured": [],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "adaEMPA-P10-archive.zip",
      "schema:description": "Archive containing tabular EMPA data for P10.",
      "schema:contentUrl": "https://astromat.org/downloads/adaempa-p10.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "0000000000000000000000000000000000000000000000000000000000000000"
      },
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 1048576,
        "schema:unitText": "byte"
      },
      "schema:hasPart": [
        {
          "@id": "ex:adaEMPA-P10-data-001",
          "@type": [
            "schema:MediaObject",
            "ada:tabularData",
            "cdi:TabularTextDataSet",
            "schema:Thing"
          ],
          "schema:name": "adaEMPA-P10-data.csv",
          "schema:description": "Per-point quantitative EMPA analyses (Pang et al. 2016 (NWA 8003 eucrite, Sci. Rep.)).",
          "schema:additionalType": [
            "ada:EMPAQEATabular"
          ],
          "schema:encodingFormat": [
            "text/csv"
          ],
          "cdi:isDelimited": true,
          "cdi:isFixedWidth": false,
          "csvw:delimiter": ",",
          "csvw:header": true,
          "ada:componentType": "ada:EMPAQEATabular",
          "ada:spectrometersUsed": "5x WDS",
          "ada:signalUsed": "Kα x-ray lines",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-p10"
          },
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/empaTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/acceleratingVoltage",
              "schema:name": "Default Accelerating Voltage",
              "schema:value": 15,
              "schema:unitText": "kV"
            },
            {
              "@id": "ada:parameter/empaTAPP/beamDiameter",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/beamDiameter",
              "schema:name": "Default Beam Diameter",
              "schema:value": "0 focused",
              "schema:unitText": "µm"
            }
          ],
          "cdif:hasPhysicalMapping": [
            {
              "cdif:index": 0,
              "cdif:physicalDataType": "String",
              "cdi:nullSequence": "NA"
            }
          ]
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:adaEMPA-P10-metadata",
    "schema:about": {
      "@id": "ex:adaEMPA-P10"
    },
    "schema:dateModified": "2026-04-29",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaEMPA"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaProduct"
      }
    ],
    "schema:maintainer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Astromat Data Archive"
    },
    "schema:sdDatePublished": "2026-04-29T12:00:00Z"
  }
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
      "csvw": "http://www.w3.org/ns/csvw#",
      "prov": "http://www.w3.org/ns/prov#",
      "dcterms": "http://purl.org/dc/terms/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/profiles/adaProfiles/adaEMPA/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "csvw": "http://www.w3.org/ns/csvw#",
      "prov": "http://www.w3.org/ns/prov#",
      "spdx": "http://spdx.org/rdf/terms#",
      "nxs": "http://purl.org/nexusformat/definitions/",
      "dcterms": "http://purl.org/dc/terms/",
      "ex": "https://example.org/",
      "dcat": "http://www.w3.org/ns/dcat#"
    }
  ],
  "@id": "ex:adaEMPA-P10",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "adaEMPA dataset for P10 (Pang et al. 2016 (NWA 8003 eucrite, Sci. Rep.))",
  "schema:description": "Auto-generated adaEMPA profile-level Dataset for publication P10: Pang et al. 2016 (NWA 8003 eucrite, Sci. Rep.). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p10); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes.",
  "schema:additionalType": [
    "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.PLACEHOLDER/adaempa-p10"
  },
  "schema:url": "https://astromat.org/products/adaempa-p10",
  "schema:dateModified": "2026-04-29",
  "schema:version": "0.1",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:creativeWorkStatus": "Draft",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Electron Microprobe Analysis (EMPA)",
    "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/EMPA"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-empa-p10",
      "schema:startDate": "2026-04-29",
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": [
            "nxs:BaseClass/NXinstrument",
            "ada:EMPAInstrument"
          ],
          "schema:name": "JEOL JEOL 8100",
          "schema:identifier": [
            "ex:instrument-empa-001"
          ],
          "schema:manufacturer": {
            "@type": [
              "schema:Organization"
            ],
            "schema:name": "JEOL"
          }
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Nanjing University",
        "schema:additionalType": [
          "nxs:BaseClass/NXsource"
        ]
      },
      "schema:object": [
        {
          "@type": [
            "schema:Thing",
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalType": [
            "MaterialSample"
          ],
          "schema:name": "Sample analyzed in P10",
          "schema:identifier": [
            "igsn:10.60471/PLACEHOLDER-P10"
          ],
          "schema:description": "Sample of: orthopyroxene, augite,  maskelynite, garnet, clinopyroxene, silica phases"
        }
      ]
    }
  ],
  "schema:variableMeasured": [],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "adaEMPA-P10-archive.zip",
      "schema:description": "Archive containing tabular EMPA data for P10.",
      "schema:contentUrl": "https://astromat.org/downloads/adaempa-p10.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "0000000000000000000000000000000000000000000000000000000000000000"
      },
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 1048576,
        "schema:unitText": "byte"
      },
      "schema:hasPart": [
        {
          "@id": "ex:adaEMPA-P10-data-001",
          "@type": [
            "schema:MediaObject",
            "ada:tabularData",
            "cdi:TabularTextDataSet",
            "schema:Thing"
          ],
          "schema:name": "adaEMPA-P10-data.csv",
          "schema:description": "Per-point quantitative EMPA analyses (Pang et al. 2016 (NWA 8003 eucrite, Sci. Rep.)).",
          "schema:additionalType": [
            "ada:EMPAQEATabular"
          ],
          "schema:encodingFormat": [
            "text/csv"
          ],
          "cdi:isDelimited": true,
          "cdi:isFixedWidth": false,
          "csvw:delimiter": ",",
          "csvw:header": true,
          "ada:componentType": "ada:EMPAQEATabular",
          "ada:spectrometersUsed": "5x WDS",
          "ada:signalUsed": "K\u03b1 x-ray lines",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-p10"
          },
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/empaTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/acceleratingVoltage",
              "schema:name": "Default Accelerating Voltage",
              "schema:value": 15,
              "schema:unitText": "kV"
            },
            {
              "@id": "ada:parameter/empaTAPP/beamDiameter",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/beamDiameter",
              "schema:name": "Default Beam Diameter",
              "schema:value": "0 focused",
              "schema:unitText": "\u00b5m"
            }
          ],
          "cdif:hasPhysicalMapping": [
            {
              "cdif:index": 0,
              "cdif:physicalDataType": "String",
              "cdi:nullSequence": "NA"
            }
          ]
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:adaEMPA-P10-metadata",
    "schema:about": {
      "@id": "ex:adaEMPA-P10"
    },
    "schema:dateModified": "2026-04-29",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaEMPA"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaProduct"
      }
    ],
    "schema:maintainer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Astromat Data Archive"
    },
    "schema:sdDatePublished": "2026-04-29T12:00:00Z"
  }
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://cdif.org/0.1/> .
@prefix csvw: <http://www.w3.org/ns/csvw#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix spdx: <http://spdx.org/rdf/terms#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://ada.astromat.org/metadata/parameter/empaTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:name "Default Accelerating Voltage" ;
    schema1:propertyID "ada:parameter/empaTAPP/acceleratingVoltage" ;
    schema1:unitText "kV" ;
    schema1:value 15 .

<https://ada.astromat.org/metadata/parameter/empaTAPP/beamDiameter> a schema1:PropertyValue ;
    schema1:name "Default Beam Diameter" ;
    schema1:propertyID "ada:parameter/empaTAPP/beamDiameter" ;
    schema1:unitText "µm" ;
    schema1:value "0 focused" .

ex:adaEMPA-P10 a schema1:Dataset,
        schema1:Product ;
    schema1:additionalType "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
        "ada:DataDeliveryPackage" ;
    schema1:creativeWorkStatus "Draft" ;
    schema1:dateModified "2026-04-29" ;
    schema1:description "Auto-generated adaEMPA profile-level Dataset for publication P10: Pang et al. 2016 (NWA 8003 eucrite, Sci. Rep.). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p10); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes." ;
    schema1:distribution [ a schema1:DataDownload ;
            schema1:contentUrl "https://astromat.org/downloads/adaempa-p10.zip" ;
            schema1:description "Archive containing tabular EMPA data for P10." ;
            schema1:encodingFormat "application/zip" ;
            schema1:hasPart ex:adaEMPA-P10-data-001 ;
            schema1:name "adaEMPA-P10-archive.zip" ;
            schema1:size [ a schema1:QuantitativeValue ;
                    schema1:unitText "byte" ;
                    schema1:value 1048576 ] ;
            spdx:checksum [ a spdx:Checksum ;
                    spdx:algorithm "SHA256" ;
                    spdx:checksumValue "0000000000000000000000000000000000000000000000000000000000000000" ] ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://registry.identifiers.org/registry/doi" ;
            schema1:value "10.PLACEHOLDER/adaempa-p10" ] ;
    schema1:license "https://creativecommons.org/licenses/by/4.0/" ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:identifier "https://ada.astromat.org/vocabulary/techniques/EMPA" ;
            schema1:name "Electron Microprobe Analysis (EMPA)" ] ;
    schema1:name "adaEMPA dataset for P10 (Pang et al. 2016 (NWA 8003 eucrite, Sci. Rep.))" ;
    schema1:subjectOf ex:adaEMPA-P10-metadata ;
    schema1:url "https://astromat.org/products/adaempa-p10" ;
    schema1:version "0.1" ;
    prov:wasGeneratedBy [ a schema1:Action,
                prov:Activity ;
            schema1:identifier "session-empa-p10" ;
            schema1:location [ a schema1:Place ;
                    schema1:additionalType "nxs:BaseClass/NXsource" ;
                    schema1:name "Nanjing University" ] ;
            schema1:object [ a schema1:Thing,
                        <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalType "MaterialSample" ;
                    schema1:description "Sample of: orthopyroxene, augite,  maskelynite, garnet, clinopyroxene, silica phases" ;
                    schema1:identifier "igsn:10.60471/PLACEHOLDER-P10" ;
                    schema1:name "Sample analyzed in P10" ] ;
            schema1:startDate "2026-04-29" ;
            prov:used [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType "ada:EMPAInstrument",
                        "nxs:BaseClass/NXinstrument" ;
                    schema1:identifier "ex:instrument-empa-001" ;
                    schema1:manufacturer [ a schema1:Organization ;
                            schema1:name "JEOL" ] ;
                    schema1:name "JEOL JEOL 8100" ] ] .

ex:adaEMPA-P10-data-001 a cdi:TabularTextDataSet,
        schema1:MediaObject,
        schema1:Thing,
        ada:tabularData ;
    cdi:isDelimited true ;
    cdi:isFixedWidth false ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/empaTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/empaTAPP/beamDiameter> ;
    schema1:additionalType "ada:EMPAQEATabular" ;
    schema1:description "Per-point quantitative EMPA analyses (Pang et al. 2016 (NWA 8003 eucrite, Sci. Rep.))." ;
    schema1:encodingFormat "text/csv" ;
    schema1:measurementTechnique ex:empaTAPP-p10 ;
    schema1:name "adaEMPA-P10-data.csv" ;
    csvw:delimiter "," ;
    csvw:header true ;
    ada:componentType "ada:EMPAQEATabular" ;
    ada:signalUsed "Kα x-ray lines" ;
    ada:spectrometersUsed "5x WDS" ;
    cdif:hasPhysicalMapping [ cdi:nullSequence "NA" ;
            cdif:index 0 ;
            cdif:physicalDataType "String" ] .

ex:adaEMPA-P10-metadata a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.0>,
        <https://w3id.org/cdif/data_description/1.0>,
        <https://w3id.org/cdif/discovery/1.0>,
        <https://w3id.org/cdif/manifest/1.0>,
        <https://w3id.org/cdif/provenance/1.0>,
        <https://w3id.org/geochem/metadata/profiles/adaEMPA>,
        <https://w3id.org/geochem/metadata/profiles/adaProduct> ;
    schema1:about ex:adaEMPA-P10 ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:dateModified "2026-04-29" ;
    schema1:maintainer [ a schema1:Organization ;
            schema1:name "Astromat Data Archive" ] ;
    schema1:sdDatePublished "2026-04-29T12:00:00Z" .


```


### adaEMPA — P10plag (Pang et al. 2016 (NWA 8003 eucrite plagioclase, Sci. Rep.))
Auto-generated adaEMPA dataset record for publication P10plag.
schema:variableMeasured is derived from the empaTAPP TAPP definition's
ada:defaultAnalytes; schema:hasPart carries the paired detailEMPA fields
and references the TAPP via schema:measurementTechnique. Synthetic
placeholders are used for DOI, file size, and dates.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "prov": "http://www.w3.org/ns/prov#",
    "spdx": "http://spdx.org/rdf/terms#",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "dcterms": "http://purl.org/dc/terms/",
    "ex": "https://example.org/",
    "dcat": "http://www.w3.org/ns/dcat#"
  },
  "@id": "ex:adaEMPA-P10plag",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "adaEMPA dataset for P10plag (Pang et al. 2016 (NWA 8003 eucrite plagioclase, Sci. Rep.))",
  "schema:description": "Auto-generated adaEMPA profile-level Dataset for publication P10plag: Pang et al. 2016 (NWA 8003 eucrite plagioclase, Sci. Rep.). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p10plag); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes.",
  "schema:additionalType": [
    "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.PLACEHOLDER/adaempa-p10plag"
  },
  "schema:url": "https://astromat.org/products/adaempa-p10plag",
  "schema:dateModified": "2026-04-29",
  "schema:version": "0.1",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:creativeWorkStatus": "Draft",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Electron Microprobe Analysis (EMPA)",
    "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/EMPA"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-empa-p10plag",
      "schema:startDate": "2026-04-29",
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": [
            "nxs:BaseClass/NXinstrument",
            "ada:EMPAInstrument"
          ],
          "schema:name": "JEOL JEOL 8100",
          "schema:identifier": [
            "ex:instrument-empa-001"
          ],
          "schema:manufacturer": {
            "@type": [
              "schema:Organization"
            ],
            "schema:name": "JEOL"
          }
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Nanjing University",
        "schema:additionalType": [
          "nxs:BaseClass/NXsource"
        ]
      },
      "schema:object": [
        {
          "@type": [
            "schema:Thing",
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalType": [
            "MaterialSample"
          ],
          "schema:name": "Sample analyzed in P10plag",
          "schema:identifier": [
            "igsn:10.60471/PLACEHOLDER-P10plag"
          ],
          "schema:description": "Sample of: plagioclase,  tissintite"
        }
      ]
    }
  ],
  "schema:variableMeasured": [],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "adaEMPA-P10plag-archive.zip",
      "schema:description": "Archive containing tabular EMPA data for P10plag.",
      "schema:contentUrl": "https://astromat.org/downloads/adaempa-p10plag.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "0000000000000000000000000000000000000000000000000000000000000000"
      },
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 1048576,
        "schema:unitText": "byte"
      },
      "schema:hasPart": [
        {
          "@id": "ex:adaEMPA-P10plag-data-001",
          "@type": [
            "schema:MediaObject",
            "ada:tabularData",
            "cdi:TabularTextDataSet",
            "schema:Thing"
          ],
          "schema:name": "adaEMPA-P10plag-data.csv",
          "schema:description": "Per-point quantitative EMPA analyses (Pang et al. 2016 (NWA 8003 eucrite plagioclase, Sci. Rep.)).",
          "schema:additionalType": [
            "ada:EMPAQEATabular"
          ],
          "schema:encodingFormat": [
            "text/csv"
          ],
          "cdi:isDelimited": true,
          "cdi:isFixedWidth": false,
          "csvw:delimiter": ",",
          "csvw:header": true,
          "ada:componentType": "ada:EMPAQEATabular",
          "ada:spectrometersUsed": "5x WDS",
          "ada:signalUsed": "Kα x-ray lines",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-p10plag"
          },
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/empaTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/acceleratingVoltage",
              "schema:name": "Default Accelerating Voltage",
              "schema:value": 15,
              "schema:unitText": "kV"
            },
            {
              "@id": "ada:parameter/empaTAPP/beamDiameter",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/beamDiameter",
              "schema:name": "Default Beam Diameter",
              "schema:value": "2–5 µm defocused",
              "schema:unitText": "µm"
            }
          ],
          "cdif:hasPhysicalMapping": [
            {
              "cdif:index": 0,
              "cdif:physicalDataType": "String",
              "cdi:nullSequence": "NA"
            }
          ]
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:adaEMPA-P10plag-metadata",
    "schema:about": {
      "@id": "ex:adaEMPA-P10plag"
    },
    "schema:dateModified": "2026-04-29",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaEMPA"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaProduct"
      }
    ],
    "schema:maintainer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Astromat Data Archive"
    },
    "schema:sdDatePublished": "2026-04-29T12:00:00Z"
  }
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
      "csvw": "http://www.w3.org/ns/csvw#",
      "prov": "http://www.w3.org/ns/prov#",
      "dcterms": "http://purl.org/dc/terms/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/profiles/adaProfiles/adaEMPA/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "csvw": "http://www.w3.org/ns/csvw#",
      "prov": "http://www.w3.org/ns/prov#",
      "spdx": "http://spdx.org/rdf/terms#",
      "nxs": "http://purl.org/nexusformat/definitions/",
      "dcterms": "http://purl.org/dc/terms/",
      "ex": "https://example.org/",
      "dcat": "http://www.w3.org/ns/dcat#"
    }
  ],
  "@id": "ex:adaEMPA-P10plag",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "adaEMPA dataset for P10plag (Pang et al. 2016 (NWA 8003 eucrite plagioclase, Sci. Rep.))",
  "schema:description": "Auto-generated adaEMPA profile-level Dataset for publication P10plag: Pang et al. 2016 (NWA 8003 eucrite plagioclase, Sci. Rep.). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p10plag); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes.",
  "schema:additionalType": [
    "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.PLACEHOLDER/adaempa-p10plag"
  },
  "schema:url": "https://astromat.org/products/adaempa-p10plag",
  "schema:dateModified": "2026-04-29",
  "schema:version": "0.1",
  "schema:license": [
    "https://creativecommons.org/licenses/by/4.0/"
  ],
  "schema:creativeWorkStatus": "Draft",
  "schema:measurementTechnique": {
    "@type": [
      "schema:DefinedTerm"
    ],
    "schema:name": "Electron Microprobe Analysis (EMPA)",
    "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/EMPA"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-empa-p10plag",
      "schema:startDate": "2026-04-29",
      "prov:used": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": [
            "nxs:BaseClass/NXinstrument",
            "ada:EMPAInstrument"
          ],
          "schema:name": "JEOL JEOL 8100",
          "schema:identifier": [
            "ex:instrument-empa-001"
          ],
          "schema:manufacturer": {
            "@type": [
              "schema:Organization"
            ],
            "schema:name": "JEOL"
          }
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Nanjing University",
        "schema:additionalType": [
          "nxs:BaseClass/NXsource"
        ]
      },
      "schema:object": [
        {
          "@type": [
            "schema:Thing",
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:additionalType": [
            "MaterialSample"
          ],
          "schema:name": "Sample analyzed in P10plag",
          "schema:identifier": [
            "igsn:10.60471/PLACEHOLDER-P10plag"
          ],
          "schema:description": "Sample of: plagioclase,  tissintite"
        }
      ]
    }
  ],
  "schema:variableMeasured": [],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "adaEMPA-P10plag-archive.zip",
      "schema:description": "Archive containing tabular EMPA data for P10plag.",
      "schema:contentUrl": "https://astromat.org/downloads/adaempa-p10plag.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "0000000000000000000000000000000000000000000000000000000000000000"
      },
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 1048576,
        "schema:unitText": "byte"
      },
      "schema:hasPart": [
        {
          "@id": "ex:adaEMPA-P10plag-data-001",
          "@type": [
            "schema:MediaObject",
            "ada:tabularData",
            "cdi:TabularTextDataSet",
            "schema:Thing"
          ],
          "schema:name": "adaEMPA-P10plag-data.csv",
          "schema:description": "Per-point quantitative EMPA analyses (Pang et al. 2016 (NWA 8003 eucrite plagioclase, Sci. Rep.)).",
          "schema:additionalType": [
            "ada:EMPAQEATabular"
          ],
          "schema:encodingFormat": [
            "text/csv"
          ],
          "cdi:isDelimited": true,
          "cdi:isFixedWidth": false,
          "csvw:delimiter": ",",
          "csvw:header": true,
          "ada:componentType": "ada:EMPAQEATabular",
          "ada:spectrometersUsed": "5x WDS",
          "ada:signalUsed": "K\u03b1 x-ray lines",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-p10plag"
          },
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/empaTAPP/acceleratingVoltage",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/acceleratingVoltage",
              "schema:name": "Default Accelerating Voltage",
              "schema:value": 15,
              "schema:unitText": "kV"
            },
            {
              "@id": "ada:parameter/empaTAPP/beamDiameter",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": "ada:parameter/empaTAPP/beamDiameter",
              "schema:name": "Default Beam Diameter",
              "schema:value": "2\u20135 \u00b5m defocused",
              "schema:unitText": "\u00b5m"
            }
          ],
          "cdif:hasPhysicalMapping": [
            {
              "cdif:index": 0,
              "cdif:physicalDataType": "String",
              "cdi:nullSequence": "NA"
            }
          ]
        }
      ]
    }
  ],
  "schema:subjectOf": {
    "@type": [
      "schema:Dataset"
    ],
    "schema:additionalType": [
      "dcat:CatalogRecord"
    ],
    "@id": "ex:adaEMPA-P10plag-metadata",
    "schema:about": {
      "@id": "ex:adaEMPA-P10plag"
    },
    "schema:dateModified": "2026-04-29",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.0"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.0"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaEMPA"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaProduct"
      }
    ],
    "schema:maintainer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Astromat Data Archive"
    },
    "schema:sdDatePublished": "2026-04-29T12:00:00Z"
  }
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://cdif.org/0.1/> .
@prefix csvw: <http://www.w3.org/ns/csvw#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix spdx: <http://spdx.org/rdf/terms#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<https://ada.astromat.org/metadata/parameter/empaTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:name "Default Accelerating Voltage" ;
    schema1:propertyID "ada:parameter/empaTAPP/acceleratingVoltage" ;
    schema1:unitText "kV" ;
    schema1:value 15 .

<https://ada.astromat.org/metadata/parameter/empaTAPP/beamDiameter> a schema1:PropertyValue ;
    schema1:name "Default Beam Diameter" ;
    schema1:propertyID "ada:parameter/empaTAPP/beamDiameter" ;
    schema1:unitText "µm" ;
    schema1:value "2–5 µm defocused" .

ex:adaEMPA-P10plag a schema1:Dataset,
        schema1:Product ;
    schema1:additionalType "Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)",
        "ada:DataDeliveryPackage" ;
    schema1:creativeWorkStatus "Draft" ;
    schema1:dateModified "2026-04-29" ;
    schema1:description "Auto-generated adaEMPA profile-level Dataset for publication P10plag: Pang et al. 2016 (NWA 8003 eucrite plagioclase, Sci. Rep.). The schema:hasPart entry under schema:distribution carries detailEMPA fields and points at the empaTAPP TAPP definition (ex:empaTAPP-p10plag); schema:variableMeasured is derived from the TAPP's ada:defaultAnalytes." ;
    schema1:distribution [ a schema1:DataDownload ;
            schema1:contentUrl "https://astromat.org/downloads/adaempa-p10plag.zip" ;
            schema1:description "Archive containing tabular EMPA data for P10plag." ;
            schema1:encodingFormat "application/zip" ;
            schema1:hasPart ex:adaEMPA-P10plag-data-001 ;
            schema1:name "adaEMPA-P10plag-archive.zip" ;
            schema1:size [ a schema1:QuantitativeValue ;
                    schema1:unitText "byte" ;
                    schema1:value 1048576 ] ;
            spdx:checksum [ a spdx:Checksum ;
                    spdx:algorithm "SHA256" ;
                    spdx:checksumValue "0000000000000000000000000000000000000000000000000000000000000000" ] ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://registry.identifiers.org/registry/doi" ;
            schema1:value "10.PLACEHOLDER/adaempa-p10plag" ] ;
    schema1:license "https://creativecommons.org/licenses/by/4.0/" ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:identifier "https://ada.astromat.org/vocabulary/techniques/EMPA" ;
            schema1:name "Electron Microprobe Analysis (EMPA)" ] ;
    schema1:name "adaEMPA dataset for P10plag (Pang et al. 2016 (NWA 8003 eucrite plagioclase, Sci. Rep.))" ;
    schema1:subjectOf ex:adaEMPA-P10plag-metadata ;
    schema1:url "https://astromat.org/products/adaempa-p10plag" ;
    schema1:version "0.1" ;
    prov:wasGeneratedBy [ a schema1:Action,
                prov:Activity ;
            schema1:identifier "session-empa-p10plag" ;
            schema1:location [ a schema1:Place ;
                    schema1:additionalType "nxs:BaseClass/NXsource" ;
                    schema1:name "Nanjing University" ] ;
            schema1:object [ a schema1:Thing,
                        <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalType "MaterialSample" ;
                    schema1:description "Sample of: plagioclase,  tissintite" ;
                    schema1:identifier "igsn:10.60471/PLACEHOLDER-P10plag" ;
                    schema1:name "Sample analyzed in P10plag" ] ;
            schema1:startDate "2026-04-29" ;
            prov:used [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType "ada:EMPAInstrument",
                        "nxs:BaseClass/NXinstrument" ;
                    schema1:identifier "ex:instrument-empa-001" ;
                    schema1:manufacturer [ a schema1:Organization ;
                            schema1:name "JEOL" ] ;
                    schema1:name "JEOL JEOL 8100" ] ] .

ex:adaEMPA-P10plag-data-001 a cdi:TabularTextDataSet,
        schema1:MediaObject,
        schema1:Thing,
        ada:tabularData ;
    cdi:isDelimited true ;
    cdi:isFixedWidth false ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/empaTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/empaTAPP/beamDiameter> ;
    schema1:additionalType "ada:EMPAQEATabular" ;
    schema1:description "Per-point quantitative EMPA analyses (Pang et al. 2016 (NWA 8003 eucrite plagioclase, Sci. Rep.))." ;
    schema1:encodingFormat "text/csv" ;
    schema1:measurementTechnique ex:empaTAPP-p10plag ;
    schema1:name "adaEMPA-P10plag-data.csv" ;
    csvw:delimiter "," ;
    csvw:header true ;
    ada:componentType "ada:EMPAQEATabular" ;
    ada:signalUsed "Kα x-ray lines" ;
    ada:spectrometersUsed "5x WDS" ;
    cdif:hasPhysicalMapping [ cdi:nullSequence "NA" ;
            cdif:index 0 ;
            cdif:physicalDataType "String" ] .

ex:adaEMPA-P10plag-metadata a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.0>,
        <https://w3id.org/cdif/data_description/1.0>,
        <https://w3id.org/cdif/discovery/1.0>,
        <https://w3id.org/cdif/manifest/1.0>,
        <https://w3id.org/cdif/provenance/1.0>,
        <https://w3id.org/geochem/metadata/profiles/adaEMPA>,
        <https://w3id.org/geochem/metadata/profiles/adaProduct> ;
    schema1:about ex:adaEMPA-P10plag ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:dateModified "2026-04-29" ;
    schema1:maintainer [ a schema1:Organization ;
            schema1:name "Astromat Data Archive" ] ;
    schema1:sdDatePublished "2026-04-29T12:00:00Z" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ADA EMPA Product Profile
description: Technique-specific profile for Electron Microprobe Analysis (EMPA) products.
  Extends the base ADA product profile with constraints on valid EMPA component types
  and empa_detail requirements.
allOf:
- $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/profiles/adaProfiles/adaProduct/schema.yaml
- type: object
  properties:
    schema:additionalType:
      description: Must include an EMPA product type identifier.
      contains:
        enum:
        - Electron Microprobe Analysis (EMPA) Collection
        - Electron Microprobe Analysis Image (EMPA)
        - Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)
        - Electron Microprobe Analysis (EMPA)
        - Electron microprobe analysis
      x-jsonld-id: http://schema.org/additionalType
    schema:distribution:
      description: Distribution items for adaEMPA. Each archive hasPart item must
        declare ada:componentType as a single string, drawn either from the universal
        componentType enum or from the EMPA-specific set defined by detailEMPA. EMPA-specific
        parts may also carry ada:spectrometersUsed and ada:signalUsed as siblings
        (per detailEMPA).
      type: array
      items:
        type: object
        properties:
          schema:hasPart:
            items:
              type: object
              anyOf:
              - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/profiles/adaProfiles/adaProduct/schema.yaml#/$defs/universalComponentTypeBranch
              - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/analysisSpecificDetails/detailEMPA/schema.yaml
            x-jsonld-id: http://schema.org/hasPart
      x-jsonld-id: http://schema.org/distribution
    schema:subjectOf:
      properties:
        dcterms:conformsTo:
          contains:
            type: object
            properties:
              '@id':
                const: https://w3id.org/geochem/metadata/profiles/adaEMPA
          x-jsonld-id: http://purl.org/dc/terms/conformsTo
      x-jsonld-id: http://schema.org/subjectOf
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
  csvw: http://www.w3.org/ns/csvw#
  prov: http://www.w3.org/ns/prov#
  spdx: http://spdx.org/rdf/terms#
  nxs: http://purl.org/nexusformat/definitions/
  dcterms: http://purl.org/dc/terms/
  geosparql: http://www.opengis.net/ont/geosparql#

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/profiles/adaProfiles/adaEMPA/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/profiles/adaProfiles/adaEMPA/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://cdif.org/0.1/",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "prov": "http://www.w3.org/ns/prov#",
    "ada": "https://ada.astromat.org/metadata/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "spdx": "http://spdx.org/rdf/terms#",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "geosparql": "http://www.opengis.net/ont/geosparql#",
    "xas": "https://xas.org/dictionary/",
    "bios": "https://bioschemas.org/",
    "dqv": "http://www.w3.org/ns/dqv#",
    "time": "http://www.w3.org/2006/time#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/profiles/adaProfiles/adaEMPA/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/profiles/adaProfiles/adaEMPA`

