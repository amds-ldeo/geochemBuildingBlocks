
# Geochem Analytical Product (Schema)

`ogch.BaseSchema.geochemProduct` *v0.1*

Generic geochemistry analytical product metadata base: composes the CDIF core, data-description, manifest, and provenance profiles with the analytical surface (analysis events, variables measured, distributions, coverage). Extended by archive-specific delivery profiles such as adaProduct.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Geochem Analytical Product

Domain-neutral base profile for metadata documenting an analytical product from a
geochemistry (or related analytical) laboratory workflow. It was factored out of
`adaProduct` so that the generic analytical surface can be reused by any archive,
with archive-specific submission/delivery layers extending it.

It composes the CDIF profiles and adds the generic geochem surface:

- **Composition** — CDIF `cdifCore`, `cdifDataDescription`, `cdifManifest` (bundle,
  applied only when a distribution is a `schema:Collection`), and `cdifProvenance`.
- **Analysis events** (`prov:wasGeneratedBy`) — the instruments, computational tools,
  and reagents actually used; the laboratory (`schema:location`); the samples analysed
  (`schema:object`); the session identifier and timing. What was used is
  `schema:instrument`, one array told apart by Wikidata kind term (constraint-only
  `if/then` pins per kind), and the TAPP followed is `schema:actionProcess {"@id"}`
  (or `schema:isBasedOn` on the activity's own workflow).
- **Variables measured** (`schema:variableMeasured`) — extends `cdifInstanceVariable`
  with description, alternate names, measurement technique, units, and value bounds.
- **Coverage** — `schema:spatialCoverage`, `schema:temporalCoverage`,
  `dqv:hasQualityMeasurement`.
- **Distributions** — the generic structure: `schema:DataDownload` / `schema:WebAPI`,
  an optional `cdi:isStructuredBy` data-structure description, and per-column tabular
  mapping for tabular-text files. File-classification vocabulary (e.g. ADA
  `ada:componentType`) is added by the extending profile.

A record declares conformance to `https://w3id.org/geochem/metadata/profiles/geochemProduct`
(alongside the CDIF profile URIs). Extending profiles add their own conformance URI, so
a record self-declares the full profile chain.

## Shared `$defs`

`UsedComputationalTool` and `UsedReagent` (the actual-tool / actual-reagent shapes of
the software and reagent items of an activity's `schema:instrument`) are defined here and re-exported by `adaProduct` for backward
compatibility with technique profiles that reference them.

## Examples

### Geochem Analytical Product Example
A minimal generic geochemistry analytical product: a dataset with one analysis
event (instrument + sample), one measured variable, and one distribution. Declares
conformance to the geochemProduct profile chain. Domain archives extend this with
their delivery-packaging vocabulary (see adaProduct).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
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
  "@id": "ex:geochemProduct-example-001",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "Generic geochemistry analytical product — single tabular dataset",
  "schema:description": "Minimal generic geochemistry analytical product: one analysis event (instrument, laboratory, sample), one measured variable, and one monolithic distribution with an inline data structure. Domain archives extend this base (see adaProduct) with delivery-packaging vocabulary. Example mock data for testing.",
  "schema:additionalType": [
    "Geochemical analysis"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": {
      "@id": "https://registry.identifiers.org/registry/doi"
    },
    "schema:value": "10.99999/geochemproduct-example-001",
    "schema:url": "https://doi.org/10.99999/geochemproduct-example-001"
  },
  "schema:url": "https://example.org/products/geochemproduct-example-001",
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
    "geochemistry",
    "analytical data"
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
          "schema:name": "Example Geoscience Institute"
        },
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "analytica@example.org"
        }
      }
    ]
  },
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Inductively coupled plasma mass spectrometry",
      "schema:identifier": "https://example.org/vocabulary/techniques/ICPMS"
    }
  ],
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-geochem-20260110-001",
      "schema:startTime": "2026-01-10T09:30:00",
      "schema:instrument": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": [
            {
              "@id": "nxs:base_classes/NXinstrument.html"
            },
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:name": "Example ICP-MS Instrument",
          "schema:identifier": [
            "ex:instrument-001"
          ],
          "@id": "ex:geochemProduct-example-001/instrument/instrument"
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Analytical Sciences Laboratory",
        "schema:identifier": "https://ror.org/00hx57361"
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
          "schema:name": "Example rock powder aliquot RP-123",
          "schema:identifier": [
            "igsn:10.60471/GSEEXAMPLE001"
          ],
          "schema:description": "Homogenized rock powder aliquot analysed in this session"
        }
      ]
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "ex:geochemProduct-var-001",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "concentration",
      "schema:alternateName": [
        "element concentration"
      ],
      "schema:description": "Measured element concentration from the analysis. Example mock data for testing.",
      "schema:propertyID": [
        {
          "@id": "https://example.org/vocabulary/variables/concentration"
        }
      ],
      "schema:unitText": "ppm",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "ppm",
      "cdif:physicalDataType": "https://www.w3.org/TR/xmlschema-2/#double"
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload",
        "cdi:PhysicalDataSet"
      ],
      "schema:name": "geochem_results.nxs",
      "schema:description": "Single NeXus (HDF5) file containing the full analysis.",
      "schema:contentUrl": "https://example.org/downloads/geochemproduct-001.nxs",
      "schema:encodingFormat": [
        "application/x-hdf5"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3"
      },
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 1048576,
        "schema:unitText": "byte"
      },
      "cdi:isStructuredBy": {
        "@id": "ex:struct-geochem-001",
        "@type": [
          "cdi:DimensionalDataStructure"
        ],
        "schema:name": "Analysis result data structure",
        "schema:description": "Dimensional structure: one measure over the analysis.",
        "cdi:has_DataStructureComponent": [
          {
            "@type": [
              "cdi:MeasureComponent"
            ],
            "cdif:name": [
              "concentration"
            ],
            "cdif:isDefinedBy_Variable": {
              "@id": "ex:geochemProduct-var-001"
            }
          }
        ]
      }
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
    "@id": "ex:geochemProduct-metadata-001",
    "schema:about": {
      "@id": "ex:geochemProduct-example-001"
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
        "@id": "https://w3id.org/cdif/data_description/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/data_structure/1.1"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/geochemProduct"
      }
    ],
    "schema:maintainer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Example Geoscience Institute"
    },
    "schema:sdDatePublished": "2026-01-15T12:00:00Z"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/geochemProduct/context.jsonld",
    {
      "schema": "http://schema.org/",
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
  "@id": "ex:geochemProduct-example-001",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "Generic geochemistry analytical product \u2014 single tabular dataset",
  "schema:description": "Minimal generic geochemistry analytical product: one analysis event (instrument, laboratory, sample), one measured variable, and one monolithic distribution with an inline data structure. Domain archives extend this base (see adaProduct) with delivery-packaging vocabulary. Example mock data for testing.",
  "schema:additionalType": [
    "Geochemical analysis"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": {
      "@id": "https://registry.identifiers.org/registry/doi"
    },
    "schema:value": "10.99999/geochemproduct-example-001",
    "schema:url": "https://doi.org/10.99999/geochemproduct-example-001"
  },
  "schema:url": "https://example.org/products/geochemproduct-example-001",
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
    "geochemistry",
    "analytical data"
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
          "schema:name": "Example Geoscience Institute"
        },
        "schema:contactPoint": {
          "@type": [
            "schema:ContactPoint"
          ],
          "schema:email": "analytica@example.org"
        }
      }
    ]
  },
  "schema:measurementTechnique": [
    {
      "@type": [
        "schema:DefinedTerm"
      ],
      "schema:name": "Inductively coupled plasma mass spectrometry",
      "schema:identifier": "https://example.org/vocabulary/techniques/ICPMS"
    }
  ],
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-geochem-20260110-001",
      "schema:startTime": "2026-01-10T09:30:00",
      "schema:instrument": [
        {
          "@type": [
            "schema:Thing",
            "schema:Product"
          ],
          "schema:additionalType": [
            {
              "@id": "nxs:base_classes/NXinstrument.html"
            },
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:name": "Example ICP-MS Instrument",
          "schema:identifier": [
            "ex:instrument-001"
          ],
          "@id": "ex:geochemProduct-example-001/instrument/instrument"
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Analytical Sciences Laboratory",
        "schema:identifier": "https://ror.org/00hx57361"
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
          "schema:name": "Example rock powder aliquot RP-123",
          "schema:identifier": [
            "igsn:10.60471/GSEEXAMPLE001"
          ],
          "schema:description": "Homogenized rock powder aliquot analysed in this session"
        }
      ]
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "ex:geochemProduct-var-001",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "concentration",
      "schema:alternateName": [
        "element concentration"
      ],
      "schema:description": "Measured element concentration from the analysis. Example mock data for testing.",
      "schema:propertyID": [
        {
          "@id": "https://example.org/vocabulary/variables/concentration"
        }
      ],
      "schema:unitText": "ppm",
      "cdi:intendedDataType": "https://www.w3.org/TR/xmlschema-2/#decimal",
      "cdi:role": "MeasureComponent",
      "cdi:simpleUnitOfMeasure": "ppm",
      "cdif:physicalDataType": "https://www.w3.org/TR/xmlschema-2/#double"
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload",
        "cdi:PhysicalDataSet"
      ],
      "schema:name": "geochem_results.nxs",
      "schema:description": "Single NeXus (HDF5) file containing the full analysis.",
      "schema:contentUrl": "https://example.org/downloads/geochemproduct-001.nxs",
      "schema:encodingFormat": [
        "application/x-hdf5"
      ],
      "spdx:checksum": {
        "@type": [
          "spdx:Checksum"
        ],
        "spdx:algorithm": "SHA256",
        "spdx:checksumValue": "b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3"
      },
      "schema:size": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 1048576,
        "schema:unitText": "byte"
      },
      "cdi:isStructuredBy": {
        "@id": "ex:struct-geochem-001",
        "@type": [
          "cdi:DimensionalDataStructure"
        ],
        "schema:name": "Analysis result data structure",
        "schema:description": "Dimensional structure: one measure over the analysis.",
        "cdi:has_DataStructureComponent": [
          {
            "@type": [
              "cdi:MeasureComponent"
            ],
            "cdif:name": [
              "concentration"
            ],
            "cdif:isDefinedBy_Variable": {
              "@id": "ex:geochemProduct-var-001"
            }
          }
        ]
      }
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
    "@id": "ex:geochemProduct-metadata-001",
    "schema:about": {
      "@id": "ex:geochemProduct-example-001"
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
        "@id": "https://w3id.org/cdif/data_description/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/provenance/1.1"
      },
      {
        "@id": "https://w3id.org/cdif/data_structure/1.1"
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/geochemProduct"
      }
    ],
    "schema:maintainer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Example Geoscience Institute"
    },
    "schema:sdDatePublished": "2026-01-15T12:00:00Z"
  }
}
```

#### ttl
```ttl
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://cdif.org/0.1/> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix schema1: <http://schema.org/> .
@prefix spdx: <http://spdx.org/rdf/terms#> .
@prefix wd: <https://www.wikidata.org/entity/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:geochemProduct-example-001 a schema1:Dataset,
        schema1:Product ;
    schema1:additionalType "Geochemical analysis" ;
    schema1:conditionsOfAccess "Unrestricted access for research purposes" ;
    schema1:creativeWorkStatus "Published" ;
    schema1:creator ( [ a schema1:Person ;
                schema1:affiliation [ a schema1:Organization ;
                        schema1:name "Example Geoscience Institute" ] ;
                schema1:contactPoint [ a schema1:ContactPoint ;
                        schema1:email "analytica@example.org" ] ;
                schema1:identifier "https://orcid.org/0000-0001-2345-6789" ;
                schema1:name "Analytica, Maria" ] ) ;
    schema1:dateModified "2026-01-15" ;
    schema1:description "Minimal generic geochemistry analytical product: one analysis event (instrument, laboratory, sample), one measured variable, and one monolithic distribution with an inline data structure. Domain archives extend this base (see adaProduct) with delivery-packaging vocabulary. Example mock data for testing." ;
    schema1:distribution [ a cdi:PhysicalDataSet,
                schema1:DataDownload ;
            cdi:isStructuredBy ex:struct-geochem-001 ;
            schema1:contentUrl "https://example.org/downloads/geochemproduct-001.nxs" ;
            schema1:description "Single NeXus (HDF5) file containing the full analysis." ;
            schema1:encodingFormat "application/x-hdf5" ;
            schema1:name "geochem_results.nxs" ;
            schema1:size [ a schema1:QuantitativeValue ;
                    schema1:unitText "byte" ;
                    schema1:value 1048576 ] ;
            spdx:checksum [ a spdx:Checksum ;
                    spdx:algorithm "SHA256" ;
                    spdx:checksumValue "b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3" ] ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID <https://registry.identifiers.org/registry/doi> ;
            schema1:url "https://doi.org/10.99999/geochemproduct-example-001" ;
            schema1:value "10.99999/geochemproduct-example-001" ] ;
    schema1:keywords "analytical data",
        "geochemistry" ;
    schema1:license "https://creativecommons.org/licenses/by/4.0/" ;
    schema1:measurementTechnique [ a schema1:DefinedTerm ;
            schema1:identifier "https://example.org/vocabulary/techniques/ICPMS" ;
            schema1:name "Inductively coupled plasma mass spectrometry" ] ;
    schema1:name "Generic geochemistry analytical product — single tabular dataset" ;
    schema1:subjectOf ex:geochemProduct-metadata-001 ;
    schema1:url "https://example.org/products/geochemproduct-example-001" ;
    schema1:variableMeasured ex:geochemProduct-var-001 ;
    schema1:version "1.0" ;
    prov:wasGeneratedBy [ a schema1:Action,
                prov:Activity ;
            schema1:identifier "session-geochem-20260110-001" ;
            schema1:instrument <https://example.org/geochemProduct-example-001/instrument/instrument> ;
            schema1:location [ a schema1:Place ;
                    schema1:identifier "https://ror.org/00hx57361" ;
                    schema1:name "Analytical Sciences Laboratory" ] ;
            schema1:object [ a schema1:Thing,
                        <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalType "MaterialSample" ;
                    schema1:description "Homogenized rock powder aliquot analysed in this session" ;
                    schema1:identifier "igsn:10.60471/GSEEXAMPLE001" ;
                    schema1:name "Example rock powder aliquot RP-123" ] ;
            schema1:startTime "2026-01-10T09:30:00" ] .

<https://example.org/geochemProduct-example-001/instrument/instrument> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://manual.nexusformat.org/classes/base_classes/NXinstrument.html>,
        wd:Q3099911 ;
    schema1:identifier "ex:instrument-001" ;
    schema1:name "Example ICP-MS Instrument" .

ex:geochemProduct-metadata-001 a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.1>,
        <https://w3id.org/cdif/data_description/1.1>,
        <https://w3id.org/cdif/data_structure/1.1>,
        <https://w3id.org/cdif/discovery/1.1>,
        <https://w3id.org/cdif/provenance/1.1>,
        <https://w3id.org/geochem/metadata/profiles/geochemProduct> ;
    schema1:about ex:geochemProduct-example-001 ;
    schema1:additionalType dcat:CatalogRecord ;
    schema1:dateModified "2026-01-15" ;
    schema1:maintainer [ a schema1:Organization ;
            schema1:name "Example Geoscience Institute" ] ;
    schema1:sdDatePublished "2026-01-15T12:00:00Z" .

ex:struct-geochem-001 a cdi:DimensionalDataStructure ;
    cdi:has_DataStructureComponent [ a cdi:MeasureComponent ;
            cdif:isDefinedBy_Variable ex:geochemProduct-var-001 ;
            cdif:name "concentration" ] ;
    schema1:description "Dimensional structure: one measure over the analysis." ;
    schema1:name "Analysis result data structure" .

ex:geochemProduct-var-001 a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "ppm" ;
    schema1:alternateName "element concentration" ;
    schema1:description "Measured element concentration from the analysis. Example mock data for testing." ;
    schema1:name "concentration" ;
    schema1:propertyID <https://example.org/vocabulary/variables/concentration> ;
    schema1:unitText "ppm" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$id: https://w3id.org/geochem/schema/geochemProduct/1.0
title: Geochemistry Analytical Product Metadata
description: 'Generic schema for JSON-LD metadata documenting an analytical product
  from a geochemistry (or related analytical) laboratory workflow. It describes the
  dataset and its distributions, the analysis events that produced it (instruments,
  computational tools, reagents, laboratory, samples analysed), the variables measured,
  and spatial / temporal / quality coverage. It composes the CDIF core, data-description,
  manifest (bundle), and provenance profiles.

  This is the domain-neutral base. Archive-specific submission/delivery layers (e.g.
  ADA/SAMIS via adaProduct) extend it with their product-type vocabulary, file-classification
  (componentType) scheme, and delivery-packaging rules.'
type: object
allOf:
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifCore/schema.yaml
- if:
    anyOf:
    - properties:
        schema:variableMeasured:
          type: array
          minItems: 1
      required:
      - schema:variableMeasured
    - properties:
        schema:distribution:
          type: array
          contains:
            type: object
            anyOf:
            - properties:
                '@type':
                  type: array
                  contains:
                    const: cdi:TabularTextDataSet
              required:
              - '@type'
            - properties:
                schema:hasPart:
                  type: array
                  contains:
                    type: object
                    properties:
                      '@type':
                        type: array
                        contains:
                          const: cdi:TabularTextDataSet
                    required:
                    - '@type'
              required:
              - schema:hasPart
      required:
      - schema:distribution
  then:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifDataDescription/schema.yaml
- if:
    properties:
      schema:distribution:
        type: array
        contains:
          type: object
          properties:
            '@type':
              type: array
              contains:
                const: schema:Collection
          required:
          - '@type'
  then:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifManifest/schema.yaml
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifProvenance/schema.yaml
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/geochemBaseProfile/schema.yaml
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
x-bblocks-metadata:
  itemIdentifier: ogch.BaseSchema.geochemProduct
  register: https://amds-ldeo.github.io/geochemBuildingBlocks/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-11'

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/geochemProduct/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/geochemProduct/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "cdif": "https://w3id.org/cdif/",
    "prov": "http://www.w3.org/ns/prov#",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/geochemProduct/context.jsonld)

## Sources

* [ADA Metadata Schema v3 (adaProduct, from which this base was factored)](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/BaseSchema/geochemProduct`

