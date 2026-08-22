
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
  (`schema:object`); the session identifier and timing. `prov:used` uses the CDIF
  role-keyed wrapper model (constraint-only `if/then` pins for `schema:instrument`,
  `bios:computationalTool`, `prov:reagent`, and an inline/`@id` `tappDefinition`).
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

`UsedComputationalTool` and `UsedReagent` (the actual-tool / actual-reagent shapes used
in `prov:used`) are defined here and re-exported by `adaProduct` for backward
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
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
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
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:name": "Example ICP-MS Instrument",
              "schema:identifier": [
                "ex:instrument-001"
              ],
              "@id": "ex:instrument/nxs-BaseClass-NXinstrument"
            }
          ]
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
        "https://example.org/vocabulary/variables/concentration"
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
            "cdif:isDefinedBy_RepresentedVariable": {
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
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
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
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:name": "Example ICP-MS Instrument",
              "schema:identifier": [
                "ex:instrument-001"
              ],
              "@id": "ex:instrument/nxs-BaseClass-NXinstrument"
            }
          ]
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
        "https://example.org/vocabulary/variables/concentration"
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
            "cdif:isDefinedBy_RepresentedVariable": {
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
            schema1:propertyID "https://registry.identifiers.org/registry/doi" ;
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
            schema1:location [ a schema1:Place ;
                    schema1:identifier "https://ror.org/00hx57361" ;
                    schema1:name "Analytical Sciences Laboratory" ] ;
            schema1:object [ a schema1:Thing,
                        <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalType "MaterialSample" ;
                    schema1:description "Homogenized rock powder aliquot analysed in this session" ;
                    schema1:identifier "igsn:10.60471/GSEEXAMPLE001" ;
                    schema1:name "Example rock powder aliquot RP-123" ] ;
            schema1:startDate "2026-01-10T09:30:00" ;
            prov:used [ schema1:instrument <https://example.org/instrument/nxs-BaseClass-NXinstrument> ] ] .

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

<https://example.org/instrument/nxs-BaseClass-NXinstrument> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "nxs:BaseClass/NXinstrument" ;
    schema1:identifier "ex:instrument-001" ;
    schema1:name "Example ICP-MS Instrument" .

ex:struct-geochem-001 a cdi:DimensionalDataStructure ;
    cdi:has_DataStructureComponent [ a cdi:MeasureComponent ;
            cdif:isDefinedBy_RepresentedVariable ex:geochemProduct-var-001 ;
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
    schema1:propertyID "https://example.org/vocabulary/variables/concentration" ;
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
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifDataDescription/schema.yaml
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
- type: object
  properties:
    '@type':
      type: array
      items:
        type: string
        enum:
        - schema:Dataset
        - schema:Product
    schema:license:
      description: Legal statement of conditions for use and access
      type: array
      minItems: 0
      items:
        anyOf:
        - type: string
        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/creativeWork/schema.yaml
      x-jsonld-id: http://schema.org/license
    schema:relatedLink:
      type: array
      description: Links to related resources at the product level
      items:
        type: object
        properties:
          '@type':
            type: array
            items:
              type: string
            contains:
              const: schema:LinkRole
            minItems: 1
          schema:linkRelationship:
            type: string
            x-jsonld-id: http://schema.org/linkRelationship
          schema:target:
            type: object
            properties:
              '@type':
                type: array
                items:
                  type: string
                contains:
                  const: schema:EntryPoint
                minItems: 1
              schema:encodingFormat:
                type: array
                items:
                  type: string
                x-jsonld-id: http://schema.org/encodingFormat
              schema:name:
                type: string
                x-jsonld-id: http://schema.org/name
              schema:url:
                type: string
                x-jsonld-id: http://schema.org/url
            x-jsonld-id: http://schema.org/target
      x-jsonld-id: http://schema.org/relatedLink
    schema:creativeWorkStatus:
      type: string
      x-jsonld-id: http://schema.org/creativeWorkStatus
    schema:measurementTechnique:
      type: array
      items:
        type: object
        description: Text description of the measurement method
        properties:
          '@type':
            type: array
            items:
              type: string
            contains:
              const: schema:DefinedTerm
            minItems: 1
          schema:name:
            type: string
            x-jsonld-id: http://schema.org/name
          schema:identifier:
            type: string
            x-jsonld-id: http://schema.org/identifier
      x-jsonld-id: http://schema.org/measurementTechnique
    prov:wasGeneratedBy:
      description: 'Analysis events. Extends cdifProvActivity (from cdifProvenance)
        with the generic geochem analysis-event surface: the instruments, computational
        tools and reagents actually used; the laboratory; the samples analysed; and
        the session identifier and timing.'
      type: array
      items:
        type: object
        properties:
          prov:used:
            type: array
            description: 'Resources used in the analysis. Each item is one of: an
              instrument BB instance; a computational tool actually used (schema:SoftwareApplication);
              a reagent / reference material actually used; a tappDefinition BB instance
              (inlined); or an @id reference to a TAPP definition node defined elsewhere.
              The TAPP plan (prov:Plan / bios:LabProtocol) prescribes the generic
              instrument / computationalTool / reagent list; these prov:used entries
              record the ACTUALS used in this specific run.'
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
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/instrument/schema.yaml
                      x-jsonld-id: http://schema.org/instrument
              - if:
                  type: object
                  required:
                  - bios:computationalTool
                then:
                  properties:
                    bios:computationalTool:
                      type: array
                      minItems: 1
                      items:
                        $ref: '#/$defs/UsedComputationalTool'
                      x-jsonld-id: https://bioschemas.org/computationalTool
              - if:
                  type: object
                  required:
                  - prov:reagent
                then:
                  properties:
                    prov:reagent:
                      type: array
                      minItems: 1
                      items:
                        $ref: '#/$defs/UsedReagent'
                      x-jsonld-id: http://www.w3.org/ns/prov#reagent
              - if:
                  type: object
                  properties:
                    '@type':
                      contains:
                        const: ada:TAPPDefinition
                  required:
                  - '@type'
                then:
                  $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml
            x-jsonld-id: http://www.w3.org/ns/prov#used
          schema:location:
            $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/laboratory/schema.yaml
            x-jsonld-id: http://schema.org/location
          schema:object:
            type: array
            description: Samples analyzed
            items:
              type: object
              properties:
                '@type':
                  type: array
                  items:
                    type: string
                  allOf:
                  - contains:
                      const: schema:Thing
                  - contains:
                      const: https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample
                  minItems: 2
                schema:additionalType:
                  type: array
                  items:
                    type: string
                  x-jsonld-id: http://schema.org/additionalType
                schema:identifier:
                  type: array
                  items:
                    type: string
                  x-jsonld-id: http://schema.org/identifier
                schema:name:
                  description: Sample name/identifier as used in the lab.
                  type: string
                  x-jsonld-id: http://schema.org/name
                schema:additionalProperty:
                  description: Per-sample PropertyValue entries (e.g. analysis location);
                    technique profiles constrain these.
                  type: array
                  items:
                    type: object
                  x-jsonld-id: http://schema.org/additionalProperty
            x-jsonld-id: http://schema.org/object
          schema:identifier:
            description: The analytical session's own identifier -- the laboratory's
              run, sequence or batch identifier as generated by the instrument or
              acquisition software. Sits on the activity rather than the dataset because
              the session IS the activity.
            type: string
            x-jsonld-id: http://schema.org/identifier
          schema:startDate:
            type: string
            x-jsonld-id: http://schema.org/startDate
          schema:endDate:
            type: string
            x-jsonld-id: http://schema.org/endDate
          schema:additionalProperty:
            description: Per-analysis PropertyValue entries (replicates, transect
              length, ...); technique profiles constrain these.
            type: array
            items:
              type: object
            x-jsonld-id: http://schema.org/additionalProperty
        required:
        - prov:used
      x-jsonld-id: http://www.w3.org/ns/prov#wasGeneratedBy
    schema:variableMeasured:
      description: Variable definitions. Extends cdifInstanceVariable (from cdifDataDescription)
        with additional generic properties. Requires a description with minLength
        3.
      type: array
      items:
        type: object
        required:
        - schema:description
        properties:
          '@type':
            description: A variable is either a measured VALUE (schema:PropertyValue)
              or a SPECIFICATION of one (schema:PropertyValueSpecification); exactly
              which it is decides how a consumer reads schema:value. One of the two
              must appear. Further type URIs are welcome alongside - cdi:InstanceVariable
              is the usual companion - so the array is open.
            type: array
            items:
              type: string
            contains:
              anyOf:
              - const: schema:PropertyValue
              - const: schema:PropertyValueSpecification
          schema:description:
            type: string
            minLength: 3
            x-jsonld-id: http://schema.org/description
          schema:alternateName:
            type: array
            items:
              type: string
              description: Human intelligible name for variable that conveys semantics
            x-jsonld-id: http://schema.org/alternateName
          schema:measurementTechnique:
            type: array
            items:
              anyOf:
              - type: string
              - type: object
                required:
                - '@id'
                additionalProperties: false
                properties:
                  '@id':
                    type: string
              - type: object
                additionalProperties: false
                properties:
                  '@type':
                    type: array
                    items:
                      type: string
                    contains:
                      const: schema:DefinedTerm
                    minItems: 1
                  schema:name:
                    type: string
                    x-jsonld-id: http://schema.org/name
                required:
                - '@type'
                - schema:name
            x-jsonld-id: http://schema.org/measurementTechnique
          schema:unitText:
            type: string
            x-jsonld-id: http://schema.org/unitText
          schema:unitCode:
            anyOf:
            - type: string
            - type: object
              required:
              - '@id'
              additionalProperties: false
              properties:
                '@id':
                  type: string
            - type: object
              additionalProperties: false
              properties:
                '@type':
                  type: array
                  items:
                    type: string
                  contains:
                    const: schema:DefinedTerm
                  minItems: 1
                schema:name:
                  type: string
                  x-jsonld-id: http://schema.org/name
              required:
              - '@type'
              - schema:name
            x-jsonld-id: http://schema.org/unitCode
          schema:minValue:
            type: number
            x-jsonld-id: http://schema.org/minValue
          schema:maxValue:
            type: number
            x-jsonld-id: http://schema.org/maxValue
          schema:url:
            type: string
            format: uri
            x-jsonld-id: http://schema.org/url
      x-jsonld-id: http://schema.org/variableMeasured
    schema:spatialCoverage:
      description: Geographic extent of resource content.
      type: array
      items:
        $ref: '#/$defs/SpatialExtent'
      x-jsonld-id: http://schema.org/spatialCoverage
    schema:temporalCoverage:
      description: Temporal extent of resource content.
      type: array
      items:
        $ref: '#/$defs/TemporalExtent'
      x-jsonld-id: http://schema.org/temporalCoverage
    dqv:hasQualityMeasurement:
      description: Quality measurements reported to assess the resource.
      type: array
      items:
        $ref: '#/$defs/QualityMeasure'
    schema:additionalProperty:
      description: PropertyValue entries describing the DELIVERED DATA rather than
        the analysis that produced it (extent, dimensions, ...). Distinct from the
        per-analysis prov:wasGeneratedBy.schema:additionalProperty. Technique profiles
        constrain these.
      type: array
      items:
        type: object
      x-jsonld-id: http://schema.org/additionalProperty
    schema:distribution:
      description: Generic distribution structure. A distribution is a schema:DataDownload
        (or schema:WebAPI, inherited from cdifCore) that MAY carry a cdi:isStructuredBy
        data-structure description (for a monolithic single file that IS the dataset,
        or a structure shared across bundle parts), and MAY be a bundle whose schema:hasPart
        lists member files (typed via cdifManifest). The domain file-classification
        of a distribution / member (e.g. ADA ada:componentType) is added by the extending
        profile.
      type: array
      items:
        type: object
        properties:
          cdi:isStructuredBy:
            description: Data-structure description of a monolithic single-file distribution
              (the file is the dataset), or a structure shared across bundle parts
              and referenced from them by @id. One of the four CDIF DataStructure
              variants inline, or an @id reference. Optional.
            anyOf:
            - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifDataStructure/schema.yaml#/$defs/DataStructure
            - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifDataStructure/schema.yaml#/$defs/DimensionalDataStructure
            - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifDataStructure/schema.yaml#/$defs/LongDataStructure
            - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifDataStructure/schema.yaml#/$defs/WideDataStructure
            - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/objectReference/schema.yaml
            x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isStructuredBy
          schema:additionalType:
            description: Optional file-classification of this distribution (or, on
              a bundle, of the whole archive) drawn from the componentType vocabulary
              (ada:vocab/componentType) -- e.g. "ada:report", "ada:calibrationFile".
              Generic and OPTIONAL here; the ADA product layer (adaProduct) instead
              carries the required ada:componentType. Advisory (annotated via schema:inDefinedTermSet),
              not hard-enumerated in JSON Schema.
            type: array
            items:
              type: string
            schema:inDefinedTermSet: ada:vocab/componentType
            x-jsonld-id: http://schema.org/additionalType
        allOf:
        - if:
            properties:
              '@type':
                type: array
                contains:
                  const: cdi:TabularTextDataSet
          then:
            $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tabularData/schema.yaml
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
                const: https://w3id.org/geochem/metadata/profiles/geochemProduct
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
  UsedComputationalTool:
    type: object
    additionalProperties: false
    description: Computational tool actually used (acquisition, data reduction, or
      processing).
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: schema:SoftwareApplication
      '@id':
        type: string
      schema:name:
        type: string
        x-jsonld-id: http://schema.org/name
      schema:version:
        type: string
        x-jsonld-id: http://schema.org/version
      schema:url:
        type: string
        format: uri
        x-jsonld-id: http://schema.org/url
      schema:description:
        type: string
        x-jsonld-id: http://schema.org/description
      ada:toolRole:
        type: string
        enum:
        - acquisition
        - dataReduction
        - processing
        - visualization
        x-jsonld-id: https://ada.astromat.org/metadata/toolRole
    required:
    - '@type'
    - schema:name
  UsedReagent:
    type: object
    additionalProperties: false
    description: Reference material, calibration standard, or chemical reagent actually
      used.
    properties:
      '@type':
        type: array
        items:
          type: string
        minItems: 1
        description: What the material IS, independent of the role it plays in this
          run (that is ada:reagentRole). schema:DefinedTerm for a material identified
          by a registry entry (GeoReM, NIST SRM, USGS); schema:Product for a specific
          catalogued specimen or purchased lot; schema:ChemicalSubstance for a bulk
          chemical or coating stock.
        contains:
          enum:
          - schema:DefinedTerm
          - schema:Product
          - schema:ChemicalSubstance
      '@id':
        type: string
      schema:name:
        type: string
        x-jsonld-id: http://schema.org/name
      schema:description:
        type: string
        x-jsonld-id: http://schema.org/description
      schema:identifier:
        description: Formal identifier (IGSN, catalog number, GeoReM ID).
        anyOf:
        - type: string
        - type: object
          additionalProperties: false
          properties:
            '@type':
              type: array
              items:
                type: string
              minItems: 1
            schema:propertyID:
              type: string
              x-jsonld-id: http://schema.org/propertyID
            schema:value:
              type: string
              x-jsonld-id: http://schema.org/value
        x-jsonld-id: http://schema.org/identifier
      schema:termCode:
        type: string
        description: Registry code for the material on the schema:DefinedTerm path.
        x-jsonld-id: http://schema.org/termCode
      schema:inDefinedTermSet:
        description: The registry the schema:termCode belongs to.
        anyOf:
        - type: string
          format: uri
        - type: object
          additionalProperties: false
          properties:
            '@id':
              type: string
              format: uri
            schema:name:
              type: string
              x-jsonld-id: http://schema.org/name
        x-jsonld-id: http://schema.org/inDefinedTermSet
      ada:reagentRole:
        type: string
        enum:
        - primaryStandard
        - secondaryStandard
        - interferenceStandard
        - blankMaterial
        - coatingMaterial
        - referenceMaterial
        - reagent
        x-jsonld-id: https://ada.astromat.org/metadata/reagentRole
    required:
    - '@type'
    - schema:name
  SpatialExtent:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/spatialExtent/schema.yaml
  TemporalExtent:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/temporalExtent/schema.yaml
  QualityMeasure:
    $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/qualityProperties/qualityMeasure/schema.yaml
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

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/geochemProduct/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/geochemProduct/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/geochemProduct/context.jsonld)

## Sources

* [ADA Metadata Schema v3 (adaProduct, from which this base was factored)](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/BaseSchema/geochemProduct`

