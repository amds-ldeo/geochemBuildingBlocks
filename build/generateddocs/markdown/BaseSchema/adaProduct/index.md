
# ADA Product Profile (Schema)

`ogch.BaseSchema.adaProduct` *v0.1*

Top-level ADA product metadata profile composing all ADA building blocks

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# ADA Product Profile

Top-level metadata profile for Astromat Data Archive (ADA) products. Composes all ADA building blocks into a complete product metadata schema. Each ADA product consists of one or more data files and supplemental files, each with an associated YAML metadata file.

The profile includes:
- Basic metadata (name, description, dates, status)
- Creator and contributor information
- Funding and licensing
- Measurement technique and provenance (instruments, laboratories, samples)
- Variable definitions
- Distribution with file-level metadata
- Metadata record information (subjectOf)

## Examples

### ADA Product Example
Example Astromat Data Archive (ADA) product metadata with all properties populated.
Mock data for validation and testing.
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
    "nxs": "https://manual.nexusformat.org/classes/",
    "dcterms": "http://purl.org/dc/terms/",
    "geosparql": "http://www.opengis.net/ont/geosparql#",
    "ex": "https://example.org/",
    "dcat": "http://www.w3.org/ns/dcat#"
  },
  "@id": "ex:adaProduct-example-001",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "ADA Analysis of Meteorite ALH 84001 Fragment",
  "schema:description": "Example Astromat Data Archive (ADA) product metadata demonstrating all properties defined by the adaProduct profile. Contains mock data for testing and validation.",
  "schema:additionalType": [
    "Electron Microprobe Analysis Image (EMPA)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.99999/adaproduct-example-001",
    "schema:url": "https://doi.org/10.99999/adaproduct-example-001"
  },
  "schema:url": "https://astromat.org/products/adaproduct-example-001",
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
      "schema:name": "Astromat Data Archive",
      "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/ADA",
      "schema:termCode": "ADA",
      "schema:inDefinedTermSet": "https://ada.astromat.org/vocabulary/techniques"
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
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "researcher@example.org"
        },
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "NASA Johnson Space Center"
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
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Astromat Data Archive (ADA)",
      "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/ADA"
    }
  ],
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-ada-20260110-001",
      "schema:startDate": "2026-01-10T09:30:00",
      "prov:used": [
        {
          "schema:instrument": [
            {
              "@type": [
                "schema:Thing",
                "schema:Product"
              ],
              "schema:additionalType": [
                "nxs:BaseClass/NXinstrument",
                "ada:ADAInstrument",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:name": "Example ADA Instrument",
              "schema:identifier": [
                "ex:instrument-ada-001"
              ]
            }
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
      "@id": "ex:adaProduct-var-001",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "measurement_value",
      "schema:alternateName": [
        "ADA primary measurement"
      ],
      "schema:description": "Primary measured quantity from Astromat Data Archive (ADA) analysis. This is example mock data for testing.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/variables/ada_primary"
      ],
      "schema:unitText": "counts",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "counts",
      "cdif:physicalDataType": "https://www.w3.org/TR/xmlschema-2/#double"
    },
    {
      "@id": "ex:adaProduct-var-002",
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
      "cdif:physicalDataType": "https://www.w3.org/TR/xmlschema-2/#float"
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload",
        "schema:Collection"
      ],
      "schema:name": "adaProduct-ALH84001-archive.zip",
      "schema:description": "Archive containing ADA data files and supplementary materials",
      "schema:contentUrl": "https://astromat.org/downloads/adaproduct-example-001.zip",
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
          "@id": "ex:adaProduct-file-001",
          "@type": [
            "schema:MediaObject",
            "ada:image",
            "schema:ImageObject"
          ],
          "schema:name": "ALH84001_ADA_001.tif",
          "schema:description": "ADA data file for ALH 84001 thin section",
          "schema:additionalType": [
            "ada:EMPAImage"
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
          "ada:componentType": "ada:EMPAImage"
        },
        {
          "@id": "ex:adaProduct-file-002",
          "@type": [
            "schema:MediaObject",
            "ada:document",
            "schema:DigitalDocument"
          ],
          "schema:name": "ALH84001_ADA_methods.pdf",
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
      {
        "@id": "dcat:CatalogRecord"
      }
    ],
    "@id": "ex:adaProduct-metadata-001",
    "schema:about": {
      "@id": "ex:adaProduct-example-001"
    },
    "schema:dateModified": "2026-01-15",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.1"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaProduct"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.1"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/geochemProduct"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/adaProduct/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "cdif": "https://cdif.org/0.1/",
      "csvw": "http://www.w3.org/ns/csvw#",
      "prov": "http://www.w3.org/ns/prov#",
      "spdx": "http://spdx.org/rdf/terms#",
      "nxs": "https://manual.nexusformat.org/classes/",
      "dcterms": "http://purl.org/dc/terms/",
      "geosparql": "http://www.opengis.net/ont/geosparql#",
      "ex": "https://example.org/",
      "dcat": "http://www.w3.org/ns/dcat#"
    }
  ],
  "@id": "ex:adaProduct-example-001",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "ADA Analysis of Meteorite ALH 84001 Fragment",
  "schema:description": "Example Astromat Data Archive (ADA) product metadata demonstrating all properties defined by the adaProduct profile. Contains mock data for testing and validation.",
  "schema:additionalType": [
    "Electron Microprobe Analysis Image (EMPA)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.99999/adaproduct-example-001",
    "schema:url": "https://doi.org/10.99999/adaproduct-example-001"
  },
  "schema:url": "https://astromat.org/products/adaproduct-example-001",
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
      "schema:name": "Astromat Data Archive",
      "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/ADA",
      "schema:termCode": "ADA",
      "schema:inDefinedTermSet": "https://ada.astromat.org/vocabulary/techniques"
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
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "researcher@example.org"
        },
        "schema:affiliation": {
          "@type": [
            "schema:Organization"
          ],
          "schema:name": "NASA Johnson Space Center"
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
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Astromat Data Archive (ADA)",
      "schema:identifier": "https://ada.astromat.org/vocabulary/techniques/ADA"
    }
  ],
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-ada-20260110-001",
      "schema:startDate": "2026-01-10T09:30:00",
      "prov:used": [
        {
          "schema:instrument": [
            {
              "@type": [
                "schema:Thing",
                "schema:Product"
              ],
              "schema:additionalType": [
                "nxs:BaseClass/NXinstrument",
                "ada:ADAInstrument",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:name": "Example ADA Instrument",
              "schema:identifier": [
                "ex:instrument-ada-001"
              ]
            }
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
      "@id": "ex:adaProduct-var-001",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "measurement_value",
      "schema:alternateName": [
        "ADA primary measurement"
      ],
      "schema:description": "Primary measured quantity from Astromat Data Archive (ADA) analysis. This is example mock data for testing.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/variables/ada_primary"
      ],
      "schema:unitText": "counts",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "counts",
      "cdif:physicalDataType": "https://www.w3.org/TR/xmlschema-2/#double"
    },
    {
      "@id": "ex:adaProduct-var-002",
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
      "cdif:physicalDataType": "https://www.w3.org/TR/xmlschema-2/#float"
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload",
        "schema:Collection"
      ],
      "schema:name": "adaProduct-ALH84001-archive.zip",
      "schema:description": "Archive containing ADA data files and supplementary materials",
      "schema:contentUrl": "https://astromat.org/downloads/adaproduct-example-001.zip",
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
          "@id": "ex:adaProduct-file-001",
          "@type": [
            "schema:MediaObject",
            "ada:image",
            "schema:ImageObject"
          ],
          "schema:name": "ALH84001_ADA_001.tif",
          "schema:description": "ADA data file for ALH 84001 thin section",
          "schema:additionalType": [
            "ada:EMPAImage"
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
          "ada:componentType": "ada:EMPAImage"
        },
        {
          "@id": "ex:adaProduct-file-002",
          "@type": [
            "schema:MediaObject",
            "ada:document",
            "schema:DigitalDocument"
          ],
          "schema:name": "ALH84001_ADA_methods.pdf",
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
      {
        "@id": "dcat:CatalogRecord"
      }
    ],
    "@id": "ex:adaProduct-metadata-001",
    "schema:about": {
      "@id": "ex:adaProduct-example-001"
    },
    "schema:dateModified": "2026-01-15",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/discovery/1.1"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaProduct"
      },
      {
        "@id": "https://w3id.org/cdif/data_description/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/manifest/1.1"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/geochemProduct"
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
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema1: <http://schema.org/> .
@prefix spdx: <http://spdx.org/rdf/terms#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:adaProduct-example-001 a schema1:Dataset,
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
    schema1:description "Example Astromat Data Archive (ADA) product metadata demonstrating all properties defined by the adaProduct profile. Contains mock data for testing and validation." ;
    schema1:distribution [ a schema1:Collection,
                schema1:DataDownload ;
            schema1:contentUrl "https://astromat.org/downloads/adaproduct-example-001.zip" ;
            schema1:description "Archive containing ADA data files and supplementary materials" ;
            schema1:encodingFormat "application/zip" ;
            schema1:hasPart ex:adaProduct-file-001,
                ex:adaProduct-file-002 ;
            schema1:name "adaProduct-ALH84001-archive.zip" ;
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
            schema1:url "https://doi.org/10.99999/adaproduct-example-001" ;
            schema1:value "10.99999/adaproduct-example-001" ] ;
    schema1:keywords [ a schema1:DefinedTerm ;
            schema1:identifier "https://ada.astromat.org/vocabulary/techniques/ADA" ;
            schema1:inDefinedTermSet "https://ada.astromat.org/vocabulary/techniques" ;
            schema1:name "Astromat Data Archive" ;
            schema1:termCode "ADA" ],
        "astromaterials",
        "meteorite" ;
    schema1:license "https://creativecommons.org/licenses/by/4.0/" ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:identifier "https://ada.astromat.org/vocabulary/techniques/ADA" ;
            schema1:name "Astromat Data Archive (ADA)" ] ;
    schema1:name "ADA Analysis of Meteorite ALH 84001 Fragment" ;
    schema1:subjectOf ex:adaProduct-metadata-001 ;
    schema1:url "https://astromat.org/products/adaproduct-example-001" ;
    schema1:variableMeasured ex:adaProduct-var-001,
        ex:adaProduct-var-002 ;
    schema1:version "1.0" ;
    prov:wasGeneratedBy [ a schema1:Action,
                prov:Activity ;
            schema1:identifier "session-ada-20260110-001" ;
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
            prov:used [ schema1:instrument [ a schema1:Product,
                                schema1:Thing ;
                            schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
                                "ada:ADAInstrument",
                                "nxs:BaseClass/NXinstrument" ;
                            schema1:identifier "ex:instrument-ada-001" ;
                            schema1:name "Example ADA Instrument" ] ] ] .

ex:adaProduct-file-001 a schema1:ImageObject,
        schema1:MediaObject,
        ada:image ;
    schema1:additionalType "ada:EMPAImage" ;
    schema1:description "ADA data file for ALH 84001 thin section" ;
    schema1:encodingFormat "image/tiff" ;
    schema1:name "ALH84001_ADA_001.tif" ;
    schema1:size [ a schema1:QuantitativeValue ;
            schema1:unitText "byte" ;
            schema1:value 10485760 ] ;
    spdx:checksum [ a spdx:Checksum ;
            spdx:algorithm "MD5" ;
            spdx:checksumValue "d41d8cd98f00b204e9800998ecf8427e" ] ;
    ada:componentType "ada:EMPAImage" .

ex:adaProduct-file-002 a schema1:DigitalDocument,
        schema1:MediaObject,
        ada:document ;
    schema1:additionalType "ada:methodDescription" ;
    schema1:description "Method description document for this analysis" ;
    schema1:encodingFormat "application/pdf" ;
    schema1:name "ALH84001_ADA_methods.pdf" ;
    schema1:size [ a schema1:QuantitativeValue ;
            schema1:unitText "byte" ;
            schema1:value 524288 ] ;
    ada:componentType "ada:methodDescription" .

ex:adaProduct-metadata-001 a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.1>,
        <https://w3id.org/cdif/data_description/1.1>,
        <https://w3id.org/cdif/discovery/1.1>,
        <https://w3id.org/cdif/manifest/1.1>,
        <https://w3id.org/cdif/provenance/1.1>,
        <https://w3id.org/geochem/metadata/profiles/adaProduct>,
        <https://w3id.org/geochem/metadata/profiles/geochemProduct> ;
    schema1:about ex:adaProduct-example-001 ;
    schema1:additionalType dcat:CatalogRecord ;
    schema1:dateModified "2026-01-15" ;
    schema1:includedInDataCatalog [ a schema1:DataCatalog ;
            schema1:name "Astromat Data Archive" ;
            schema1:url "https://astromat.org" ] ;
    schema1:maintainer [ a schema1:Organization ;
            schema1:name "Astromat Data Archive" ] ;
    schema1:sdDatePublished "2026-01-15T12:00:00Z" .

ex:adaProduct-var-001 a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "counts" ;
    schema1:alternateName "ADA primary measurement" ;
    schema1:description "Primary measured quantity from Astromat Data Archive (ADA) analysis. This is example mock data for testing." ;
    schema1:name "measurement_value" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/variables/ada_primary" ;
    schema1:unitText "counts" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:adaProduct-var-002 a cdi:InstanceVariable,
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

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$id: https://w3id.org/adaJSONLD/schema/3.0
title: Astromat Archive Product Metadata
description: 'Schema for JSON metadata documenting products in Astromat Data Archive
  (ADA). Extends the domain-neutral geochemProduct base with the ADA/SAMIS submission
  and delivery layer: the ADA product-type vocabulary, the SAMIS submissionType, the
  ada:componentType file-classification scheme (on monolithic distributions and on
  each bundle member), and the adaProduct profile conformance. All of the generic
  analytical surface -- analysis events (prov:wasGeneratedBy), variables measured,
  distributions, spatial / temporal / quality coverage -- is inherited unchanged from
  geochemProduct. Version 3.0 aligned with CDIF 2026.'
type: object
allOf:
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/geochemProduct/schema.yaml
- type: object
  properties:
    schema:additionalType:
      type: array
      description: Should have the ada product type and 'ada:DataDeliveryPackage'
      items:
        type: string
      contains:
        enum:
        - 40Ar/39Ar Geochronology and Thermochronology (ARGT)
        - 40Ar/39Ar geochronology and thermochronology
        - Accelerator Mass Spectrometry (AMS)
        - Accelerator Mass Spectrometry
        - Advanced Imaging and Visualization of Astromaterials (AIVA)
        - Analysis Advanced Imaging and Visualization of Astromaterials (AIVA)
        - Advanced Imaging & Visualization of Astromaterials
        - Basemap
        - Differential Scanning Calorimetry (DSC)
        - Differential Scanning Calorimetry
        - Electron Microprobe Analysis (EMPA) Collection
        - Electron Microprobe Analysis Image (EMPA)
        - Electron Microprobe Analysis Quantitative Elemental Abundances (EMPAQEA)
        - Electron Microprobe Analysis (EMPA)
        - Electron microprobe analysis
        - Elemental Analysis-Isotope Ratio Mass Spectrometry (EA-IRMS)
        - Elemental analysis - isotope ratio mass spectrometry
        - Fluorescence Microscopy (UVFM) Image
        - UV Fluorescence Microscopy
        - Fourier Transform Ion Cyclotron Resonance Mass Spectrometry (FTICRMS) Cube
        - Fourier Transform Ion Cyclotron Resonance Mass Spectrometry (FTICRMS) Tabular
        - Fourier Transform Ion Cyclotron Resonance Mass Spectrometry
        - Gas Chromatography-Mass Spectrometry (GCMS)
        - Gas Chromatography-Mass Spectrometry
        - Gas Pycnometry (GPYC) Processed
        - Gas Pycnometry (GPYC) Raw
        - Gas pycnometry
        - High-resolution Inductively Coupled Plasma Mass Spectroscopy (HRICPMS) Processed
        - High-resolution Inductively Coupled Plasma Mass Spectroscopy (HRICPMS) Raw
        - High-resolution inductively coupled plasma mass spectrometry
        - Laser Ablation Quadrupole Inductively Coupled Plasma Mass Spectrometry (LAQICPMS)
          Processed
        - Laser Ablation Quadrupole Inductively Coupled Plasma Mass Spectrometry (LAQICPMS)
          Raw
        - Laser Ablation Sector-Field Inductively Coupled Plasma Mass Spectrometry
          (LASFICPMS) Processed
        - Laser Ablation Sector-Field Inductively Coupled Plasma Mass Spectrometry
          (LASFICPMS) Raw
        - Laser Ablation Quadrupole Inductively Coupled Plasma Mass Spectrometry
        - Laser Ablation Sector-Field Inductively Coupled Plasma Mass Spectrometry
        - Inductively Coupled Plasma - Optical Emission Spectroscopy (ICPOES) Intermediate
        - Inductively Coupled Plasma - Optical Emission Spectroscopy (ICPOES) Processed
        - Inductively Coupled Plasma - Optical Emission Spectroscopy (ICPOES) Raw
        - Inductively coupled plasma - optical emission spectrometry
        - Ion Chromatography (IC)
        - Ion Chromatography
        - Laser Assisted Fluorination (LAF) Processed
        - Laser Assisted Fluorination (LAF) Raw
        - Laser Assisted Fluorination for Bulk Oxygen Isotope Ratio Measurements
        - Liquid Chromatography - Mass Spectrometry (LCMS) Collection
        - Liquid Chromatography-Mass Spectrometry
        - Lock-In Thermography (LIT) Collection
        - Lock-In Thermography (LIT) image
        - Lock-In Thermography
        - Microprobe Two-Step Laser Mass Spectrometry (L2MS)
        - Microprobe Two-Step Laser Mass Spectrometry
        - Multi-Collector Inductively Coupled Plasma Mass Spectrometry (MCICPMS) processed
        - Multi-Collector Inductively Coupled Plasma Mass Spectrometry (MCICPMS) Raw
        - Multi-Collector Inductively Coupled Plasma Mass Spectrometry
        - Nanoscale Infrared Mapping (NanoIR) Background
        - Nanoscale Infrared Mapping (NanoIR) MapCollection
        - Nanoscale Infrared Mapping (NanoIR) Point Data
        - Nanoscale Infrared Mapping
        - Nanoscale Secondary Ion Mass Spectrometry (NanoSIMS) Image
        - Nanoscale Secondary Ion Mass Spectrometry (NanoSIMS) Raw
        - Nanoscale Secondary Ion Mass Spectrometry (NanoSIMS) Tabular
        - Nanoscale secondary ion mass spectrometry
        - Noble Gas and Nitrogen Static Mass Spectrometry (NGNSMS) Raw
        - Noble Gas and Nitrogen Static Mass Spectrometry (NGNSMS) Processed
        - Noble gas and Nitrogen Static Mass Spectrometry
        - Particle Size Frequency Distribution (PSFD)
        - Particle Size Frequency Distribution
        - Quadrupole Inductively Coupled Plasma Mass Spectrometry (QICPMS) Processed
        - Quadrupole Inductively Coupled Plasma Mass Spectrometry (QICPMS) Raw
        - Quadrupole Inductively Coupled Plasma Mass Spectrometry
        - Quantitative Reflective Imaging System (QRIS)
        - Quantitative Reflective Imaging System (QRIS) Calibrated
        - Quantitative Reflectance Imaging System
        - Raman vibrational spectroscopy
        - Resonance ionization time of flight noble gas mass spectrometry (RITOFNGMS)
          Processed
        - Resonance ionization time of flight noble gas mass spectrometry (RITOFNGMS)
          Spectra
        - Resonance ionization time of flight noble gas mass spectrometry
        - Scanning Electron Microscopy (SEM) Image
        - Scanning Electron Microscopy Electron Backscatter Diffraction (SEMEBSD)
          Grain Image
        - Scanning Electron Microscopy Energy Dispersive X-ray Spectroscopy (SEMEDS)
          Point Data
        - Scanning Electron Microscopy Energy Dispersive X-ray Spectroscopy (SEMEDS)
          image
        - Scanning Electron Microscopy High Resolution Cathodoluminescence (SEMHRCL)
          image
        - Scanning electron microscopy
        - Focused ion beam-scanning electron microscopy
        - Scanning Transmission Electron Microscopy (STEM) Image
        - Scanning Transmission Electron Microscopy Electron Energy-loss Spectra (STEMEELS)
          Cube
        - Scanning Transmission Electron Microscopy Electron Energy-loss Spectra (STEMEELS)
          Tabular
        - Scanning Transmission Electron Microscopy Energy Dispersive X-ray Spectroscopy
          (STEMEDS) Cube
        - Scanning Transmission Electron Microscopy Energy Dispersive X-ray Spectroscopy
          (STEMEDS) Tabular
        - Scanning Transmission Electron Microscopy Energy Dispersive X-ray Spectroscopy
          (STEMEDS) Tomography
        - Secondary Ion Mass Spectrometry (SIMS) Tabular
        - Secondary ion mass spectrometry
        - Seismic Velocities and Rock Ultrasonic Elastic Constants (SVRUEC)
        - Seismic Velocities and Rock Ultrasonic Elastic Constants
        - Structured Light Scanning (SLS) Individual Scan Collection
        - Structured Light Scanning (SLS) Shape Model
        - Structured Light Scanning
        - Time-of-flight secondary ion mass spectrometry (TOFSIMS)
        - Time-of-Flight Secondary Ion Mass Spectrometer
        - Transmission Electron Microscopy (TEM) Image
        - Transmission Electron Microscopy (TEM) Patterns Image
        - Transmission Electron Microscopy
        - Visible Light Microscopy (VLM) Image
        - Visible Light Microscopy
        - Visible Light Microscopy Basemap
        - Visible, near-infrared, and mid-infrared Spectroscopy (VNMIR) Point
        - Visible, near-, and mid-infrared spectroscopy
        - X-ray Absorption Near Edge Structure Hyperspectral Image Stack (XANES)
        - X-ray absorption near edge structure (XANES) spectroscopy
        - X-ray Computed Tomography (XCT) Image Collection
        - X-ray computed tomography
        - X-ray Diffraction (XRD) Tabular
        - X-ray diffraction
      minItems: 2
      x-jsonld-id: http://schema.org/additionalType
    submissionType:
      type: string
    schema:distribution:
      description: 'ADA delivery view: adds the ada:componentType file-classification
        to the generic distribution structure inherited from geochemProduct. A distribution
        is EITHER a MONOLITHIC single-file dataset -- a schema:DataDownload that carries
        its own ada:componentType (and, when its structure is described, cdi:isStructuredBy
        from the base), with NO schema:hasPart -- OR a BUNDLE/archive -- a schema:DataDownload
        whose schema:hasPart lists member files, each a schema:MediaObject carrying
        its own ada:componentType (the ADA SAMIS delivery pattern).'
      type: array
      items:
        type: object
        properties:
          ada:componentType:
            type: string
            schema:inDefinedTermSet: ada:vocab/componentType
            description: ADA file-type classification for a MONOLITHIC single-file
              distribution -- it classifies the file that IS the dataset. On a bundle
              this sits on each schema:hasPart member instead, not here. Values are
              drawn from the componentType vocabulary (ada:vocab/componentType); conformance
              is advisory (annotated via schema:inDefinedTermSet), not hard-enumerated
              in JSON Schema.
            x-jsonld-id: https://ada.astromat.org/metadata/componentType
          schema:hasPart:
            items:
              allOf:
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/files/schema.yaml
              - type: object
                properties:
                  ada:componentType:
                    type: string
                    description: 'ADA file-type classification, expressed as a single
                      string drawn from a universal set or a technique-specific set.
                      Technique profiles add an anyOf at the hasPart level: one branch
                      declares the universal componentType enum; other branches $ref
                      technique-specific detail schemas (e.g. detailEMPA) that enumerate
                      technique componentType values and contribute detail-specific
                      sibling properties (e.g. ada:spectrometersUsed).'
            x-jsonld-id: http://schema.org/hasPart
      x-jsonld-id: http://schema.org/distribution
    schema:subjectOf:
      properties:
        dcterms:conformsTo:
          contains:
            type: object
            required:
            - '@id'
            additionalProperties: false
            properties:
              '@id':
                const: https://w3id.org/geochem/metadata/profiles/adaProduct
          x-jsonld-id: http://purl.org/dc/terms/conformsTo
      x-jsonld-id: http://schema.org/subjectOf
$defs:
  universalComponentTypeBranch:
    description: Wrapper for use as one branch of a profile's schema:hasPart.items.anyOf.
      Constrains ada:componentType to the universal enum and marks it required. Factored
      out of every profile to eliminate the inline boilerplate.
    properties:
      ada:componentType:
        $ref: '#/$defs/universalComponentType'
        x-jsonld-id: https://ada.astromat.org/metadata/componentType
    required:
    - ada:componentType
  universalComponentType:
    description: 'A componentType value drawn from the shared componentType vocabulary
      (ada:vocab/componentType). Not hard-enumerated here: conformance to the vocabulary
      is advisory (annotated via schema:inDefinedTermSet, SHACL-checkable) rather
      than enforced by JSON Schema, so techniques may extend the term set.'
    type: string
    schema:inDefinedTermSet: ada:vocab/componentType
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
  csvw: http://www.w3.org/ns/csvw#
  prov: http://www.w3.org/ns/prov#
  bios: https://bioschemas.org/
  spdx: http://spdx.org/rdf/terms#
  nxs: https://manual.nexusformat.org/classes/
  dcterms: http://purl.org/dc/terms/
  geosparql: http://www.opengis.net/ont/geosparql#

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/adaProduct/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/adaProduct/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://w3id.org/cdif/",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "prov": "http://www.w3.org/ns/prov#",
    "ada": "https://ada.astromat.org/metadata/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "bios": "https://bioschemas.org/",
    "spdx": "http://spdx.org/rdf/terms#",
    "nxs": "https://manual.nexusformat.org/classes/",
    "geosparql": "http://www.opengis.net/ont/geosparql#",
    "xas": "cdif:xas/",
    "wd": "https://www.wikidata.org/entity/",
    "dqv": "http://www.w3.org/ns/dqv#",
    "time": "http://www.w3.org/2006/time#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/adaProduct/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/BaseSchema/adaProduct`

