
# ADA Solution SF-ICP-MS Product Profile (Schema)

`ogch.techniqueProfile.geochemProfile.Solution-SF-ICPMS.profile` *v0.1*

Path-driven ADA product profile for ADA Solution SF-ICP-MS Product Profile.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### ADA Solution SF-ICP-MS Product Profile Example
Example path-driven SOLUTIONSFICPMS product record with dataset-level analysis detail
and technique component types on the archive distribution. Mock data for validation.
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
  "@id": "ex:adaSolutionSFICPMS-example-001",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "ADA Solution SF-ICP-MS Example Product",
  "schema:description": "Example path-driven SOLUTIONSFICPMS product record: dataset-level analysis detail plus technique component types on distribution.hasPart. Mock data.",
  "schema:additionalType": [
    "High-resolution Inductively Coupled Plasma Mass Spectroscopy (HRICPMS) Processed",
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
      "schema:roleName": "analyst",
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
                "ICPMS",
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
            "ada:SolutionICPMSTabular"
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
          "ada:componentType": "ada:SolutionICPMSTabular"
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
            "ada:SolutionICPMSTabular"
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
          "ada:componentType": "ada:SolutionICPMSTabular"
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
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/adaSolutionSFICPMS"
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
  },
  "dqv:hasQualityMeasurement": [
    {
      "dqv:isMeasurementOf": "Oxide production ratio",
      "dqv:value": "example oxideProduction"
    },
    {
      "dqv:isMeasurementOf": "Dispersion Statistic",
      "dqv:value": "example goodnessOfFitOrDispersionStatistic"
    },
    {
      "dqv:isMeasurementOf": "Goodness-of-Fit",
      "dqv:value": "example goodnessOfFitOrDispersionStatistic"
    }
  ]
}

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ADA Solution SF-ICP-MS Product Profile
description: Path-driven technique-specific profile for ADA Solution SF-ICP-MS Product
  Profile. Extends the base ADA product profile with the SOLUTIONSFICPMS analysis-instance
  detail on the schema:Dataset root, narrows prov:used to the solutionSficpmsTAPP
  protocol, and constrains valid component types on schema:distribution.hasPart.
allOf:
- $ref: https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/BaseSchema/geochemProduct/schema.yaml
- $ref: https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/Solution-SF-ICPMS/detail/schema.yaml
- type: object
  properties:
    prov:wasGeneratedBy:
      description: 'Pin the solutionSficpmsTAPP definition and the instrument where
        prov:used carries them. Constraint-only if/then, never a narrowed anyOf: prov:used
        items are role-keyed wrappers, and an anyOf here would allOf-merge with the
        base union and exclude item shapes the base allows.'
      type: array
      items:
        type: object
        properties:
          prov:used:
            type: array
            items:
              allOf:
              - if:
                  type: object
                  required:
                  - schema:instrument
                then:
                  properties:
                    schema:instrument:
                      type: array
                      minItems: 1
                      items:
                        $ref: https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/BaseSchema/instrument/schema.yaml
              - if:
                  type: object
                  properties:
                    '@type':
                      contains:
                        const: ada:TAPPDefinition
                  required:
                  - '@type'
                then:
                  $ref: https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/Solution-SF-ICPMS/tapp/schema.yaml
    schema:additionalType:
      description: Must include a SOLUTIONSFICPMS product type identifier.
      contains:
        enum:
        - High-resolution Inductively Coupled Plasma Mass Spectroscopy (HRICPMS) Processed
        - High-resolution inductively coupled plasma mass spectrometry
    schema:distribution:
      description: Each distribution item is EITHER a monolithic single-file dataset
        whose ada:componentType is a SOLUTIONSFICPMS-specific or universal value (and
        may carry cdi:isStructuredBy), OR a bundle whose schema:hasPart members each
        carry such a componentType (the ADA/SAMIS archive form).
      type: array
      items:
        anyOf:
        - type: object
          required:
          - ada:componentType
          properties:
            ada:componentType:
              type: string
              anyOf:
              - $ref: https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/BaseSchema/geochemProduct/schema.yaml#/$defs/universalComponentType
              - enum:
                - ada:SolutionICPMSTabular
        - type: object
          required:
          - schema:hasPart
          properties:
            schema:hasPart:
              items:
                type: object
                anyOf:
                - $ref: https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/BaseSchema/geochemProduct/schema.yaml#/$defs/universalComponentTypeBranch
                - properties:
                    ada:componentType:
                      type: string
                      enum:
                      - ada:SolutionICPMSTabular
                  required:
                  - ada:componentType
    schema:subjectOf:
      properties:
        dcterms:conformsTo:
          contains:
            type: object
            properties:
              '@id':
                const: https://w3id.org/geochem/metadata/profiles/adaSolutionSFICPMS

```

Links to the schema:

* YAML version: [schema.yaml](https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/Solution-SF-ICPMS/profile/schema.json)
* JSON version: [schema.json](https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/Solution-SF-ICPMS/profile/schema.yaml)


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
[context.jsonld](https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/Solution-SF-ICPMS/profile/context.jsonld)


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/Solution-SF-ICPMS/profile`

