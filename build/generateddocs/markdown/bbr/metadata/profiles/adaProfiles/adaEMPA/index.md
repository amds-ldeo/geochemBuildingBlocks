
# ADA EMPA Profile (Schema)

`ada.bbr.metadata.profiles.adaProfiles.adaEMPA` *v0.1*

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
Example Electron Microprobe Analysis (EMPA) product metadata with all properties populated.
Mock data for validation and testing.
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
      "cdi:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ],
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "counts"
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
      "cdi:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#float"
      ],
      "cdi:role": "DimensionComponent",
      "cdi:simpleUnitOfMeasure": "um"
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
            "ada:document",
            "schema:DigitalDocument",
            "schema:MediaObject"
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
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaEMPA/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
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
      "cdi:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ],
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "counts"
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
      "cdi:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#float"
      ],
      "cdi:role": "DimensionComponent",
      "cdi:simpleUnitOfMeasure": "um"
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
            "ada:document",
            "schema:DigitalDocument",
            "schema:MediaObject"
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
    cdi:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "counts" ;
    schema1:alternateName "EMPA primary measurement" ;
    schema1:description "Primary measured quantity from Electron Microprobe Analysis (EMPA) analysis. This is example mock data for testing." ;
    schema1:name "measurement_value" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/variables/empa_primary" ;
    schema1:unitText "counts" .

ex:adaEMPA-var-002 a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:physicalDataType "https://www.w3.org/TR/xmlschema-2/#float" ;
    cdi:role "DimensionComponent" ;
    cdi:simpleUnitOfMeasure "um" ;
    schema1:alternateName "X coordinate" ;
    schema1:description "Horizontal position coordinate on sample surface." ;
    schema1:name "position_x" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/variables/position_x" ;
    schema1:unitText "micrometer" .


```


### EMPA Bundle — All Six componentTypes
Comprehensive example of an EMPA ZIP bundle distribution with one hasPart per
EMPA-specific ada:componentType (EMPAImageMap, EMPAImage, EMPAQEATabular,
EMPAImageCollection, EMPAESPCTabular, EMPAESPCPlot). Exercises the
componentType-nested detailEMPA pattern (spectrometersUsed, signalUsed)
on parts whose underlying file-shape schemas wire detailEMPA.
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
      "cdi:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ],
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%"
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
      "cdi:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#float"
      ],
      "cdi:role": "DimensionComponent",
      "cdi:simpleUnitOfMeasure": "um"
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
          "ada:signalUsed": "Characteristic X-rays: Si Kα, Ti Kα, Al Kα, Fe Kα, Mn Kα, Mg Kα, Ca Kα, Na Kα, K Kα, Cr Kα"
        },
        {
          "@id": "ex:adaEMPA-part-imagecollection",
          "@type": [
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
          "ada:signalUsed": "Full X-ray spectrum, 0–20 keV, 10 eV channel width"
        },
        {
          "@id": "ex:adaEMPA-part-espcplot",
          "@type": [
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
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaEMPA/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
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
      "cdi:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#double"
      ],
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "wt%"
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
      "cdi:physicalDataType": [
        "https://www.w3.org/TR/xmlschema-2/#float"
      ],
      "cdi:role": "DimensionComponent",
      "cdi:simpleUnitOfMeasure": "um"
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
          "ada:signalUsed": "Characteristic X-rays: Si K\u03b1, Ti K\u03b1, Al K\u03b1, Fe K\u03b1, Mn K\u03b1, Mg K\u03b1, Ca K\u03b1, Na K\u03b1, K K\u03b1, Cr K\u03b1"
        },
        {
          "@id": "ex:adaEMPA-part-imagecollection",
          "@type": [
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
          "ada:signalUsed": "Full X-ray spectrum, 0\u201320 keV, 10 eV channel width"
        },
        {
          "@id": "ex:adaEMPA-part-espcplot",
          "@type": [
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
    ada:spectrometersUsed "Energy-dispersive Si(Li) detector" .

ex:adaEMPA-part-image a schema1:ImageObject,
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

ex:adaEMPA-part-imagecollection a ada:collection,
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
    ada:yCoordCol "position_y_um" .

ex:adaEMPA-var-mg a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:alternateName "MgO (weight percent)" ;
    schema1:description "Magnesium oxide weight percent derived from electron microprobe analysis with ZAF matrix correction." ;
    schema1:maxValue 100 ;
    schema1:minValue 0 ;
    schema1:name "MgO_wt_pct" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/variables/MgO_wt_pct" ;
    schema1:unitText "wt%" .

ex:adaEMPA-var-x a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:physicalDataType "https://www.w3.org/TR/xmlschema-2/#float" ;
    cdi:role "DimensionComponent" ;
    cdi:simpleUnitOfMeasure "um" ;
    schema1:alternateName "Stage X coordinate" ;
    schema1:description "Horizontal position coordinate on sample surface referenced to stage origin." ;
    schema1:name "position_x" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/variables/position_x" ;
    schema1:unitText "micrometer" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ADA EMPA Product Profile
description: Technique-specific profile for Electron Microprobe Analysis (EMPA) products.
  Extends the base ADA product profile with constraints on valid EMPA component types
  and empa_detail requirements.
allOf:
- $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaProduct/schema.yaml
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
              - properties:
                  ada:componentType:
                    $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaProduct/schema.yaml#/$defs/universalComponentType
                required:
                - ada:componentType
              - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailEMPA/schema.yaml
    schema:subjectOf:
      properties:
        dcterms:conformsTo:
          contains:
            type: object
            properties:
              '@id':
                const: https://w3id.org/geochem/metadata/profiles/adaEMPA
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

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaEMPA/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaEMPA/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "prov": "http://www.w3.org/ns/prov#",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "spdx": "http://spdx.org/rdf/terms#",
    "nxs": "http://purl.org/nexusformat/definitions/",
    "geosparql": "http://www.opengis.net/ont/geosparql#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xas": "https://xas.org/dictionary/",
    "time": "http://www.w3.org/2006/time#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/profiles/adaProfiles/adaEMPA/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/profiles/adaProfiles/adaEMPA`

