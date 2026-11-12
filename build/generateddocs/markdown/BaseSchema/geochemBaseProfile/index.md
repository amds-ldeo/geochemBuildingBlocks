
# Geochem Base Profile (Schema)

`ogch.BaseSchema.geochemBaseProfile` *v0.1*

The geochemistry overlay on its own: the analytical surface this repository adds to, and refines on top of, the CDIF profiles -- analysis events, variables measured, distributions and parts, coverage, and the product-level declarations. geochemProduct is the composition of the CDIF profiles with this block; this block composes nothing and is not a standalone record schema.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Geochem Base Profile

The geochemistry overlay on its own. This block holds everything this repository
contributes to an analytical product record, and nothing it imports: no CDIF content, no
composition. `geochemProduct` is the composition — the CDIF profiles plus this block —
and this is the half gBB authors.

Factored out of `geochemProduct` on 2026-11-04, following the `cdifProfile` /
`cdifCompositeProfile` split upstream, where each component profile is its own block and
the composite is a thin `allOf` over them. The point is reviewability: what gBB adds can
now be read and diffed without the four imported CDIF branches around it.

## What is in here

- **Analysis events** (`prov:wasGeneratedBy`) — the instruments, computational tools and
  reagents actually used; the laboratory (`schema:location`); the samples analysed
  (`schema:object`); the session identifier and timing; and the TAPP followed. What was
  used is `schema:instrument`: one array of instruments, computational tools and reagents,
  told apart by the Wikidata kind term in `schema:additionalType`, with a constraint-only
  `if`/`then` pin per kind. The TAPP link is `schema:actionProcess {"@id"}`, or
  `schema:isBasedOn` on the activity's own inline workflow. The superseded `prov:used`
  role-keyed wrappers are closed off by name.
- **Variables measured** (`schema:variableMeasured`) — extends `cdifInstanceVariable` with
  description, alternate names, measurement technique, units and value bounds.
- **Coverage** — `schema:spatialCoverage`, `schema:temporalCoverage`,
  `dqv:hasQualityMeasurement`.
- **Distributions** — the generic structure: `schema:DataDownload` / `schema:WebAPI`, an
  optional `cdi:isStructuredBy` data-structure description, and per-column tabular mapping
  for tabular-text files. File-classification vocabulary (e.g. ADA `ada:componentType`) is
  added by the extending profile, not here.
- **`$defs`** — `UsedComputationalTool`, `UsedReagent` and `PropertyValueEntry`, which the
  generated technique `detail/` and module blocks reference across the boundary.

## Two things it is NOT

**Not a list of properties absent from CDIF.** Most of these keys exist upstream; this
block narrows them and gives them their gBB labels. A property here may be a pure
refinement of a CDIF property, and that is the normal case rather than the exception.

**Not a standalone record schema.** On its own it constrains an object carrying the
geochem surface and says nothing about the CDIF properties a record also needs, so it
asserts far less than a record must satisfy. Compose it, or reference `geochemProduct`.
It also has no conformance class and no `conformance.json`: nothing conforms to the
overlay alone, and `build_conformance_sidecars` derives sidecars for `geochemProduct` and
`adaProduct` by name, not by walking the directory.

## Examples

### Geochem Base Profile Example
The geochem overlay alone: one analysis event (instrument plus sample), one measured
variable, one distribution, and the product-level declarations. It is the same content
as the geochemProduct example minus nothing -- every key that example carries is one
this overlay defines or refines -- but it is validated against the overlay by itself,
which is what pins the overlay's own shape rather than the composition's.

It is NOT a complete record: composed into geochemProduct it would also have to satisfy
the CDIF core, provenance and (conditionally) data-description and manifest profiles.
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
    "dcat": "http://www.w3.org/ns/dcat#",
    "bios": "https://bioschemas.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "dqv": "http://www.w3.org/ns/dqv#"
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
      "schema:actionProcess": {
        "@type": [
          "schema:HowTo"
        ],
        "schema:name": "Synthetic solution ICP-MS trace-element workflow",
        "schema:isBasedOn": {
          "@id": "ex:solutionQicpmsTAPP-P0"
        },
        "schema:step": [
          {
            "@id": "ex:geochemProduct-example-001/step/digestion",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:name": "Sample digestion",
            "schema:position": 1,
            "schema:description": "Synthetic step. 100 mg of rock powder digested in HF-HNO3 on a hotplate, dried down and taken up in 2% HNO3.",
            "schema:additionalType": [
              {
                "@id": "bios:LabProcess"
              }
            ],
            "schema:agent": {
              "@type": [
                "schema:Person"
              ],
              "schema:name": "Example Analyst"
            },
            "schema:startTime": "2026-01-08T09:00:00",
            "schema:endTime": "2026-01-09T16:00:00",
            "schema:location": {
              "@type": [
                "schema:Place"
              ],
              "schema:name": "Clean laboratory, Analytical Sciences Laboratory"
            },
            "schema:object": {
              "@id": "ex:geochemProduct-example-001/sample/RP-123"
            },
            "schema:result": {
              "@id": "ex:geochemProduct-example-001/digest/RP-123"
            },
            "schema:instrument": [
              {
                "@type": [
                  "schema:ChemicalSubstance"
                ],
                "schema:name": "Concentrated HF, trace-metal grade",
                "ada:reagentRole": "reagent",
                "schema:additionalType": [
                  {
                    "@id": "https://www.wikidata.org/entity/Q2356542"
                  }
                ]
              },
              {
                "@type": [
                  "schema:ChemicalSubstance"
                ],
                "schema:name": "Concentrated HNO3, trace-metal grade",
                "ada:reagentRole": "reagent",
                "schema:additionalType": [
                  {
                    "@id": "https://www.wikidata.org/entity/Q2356542"
                  }
                ]
              }
            ]
          },
          {
            "@id": "ex:geochemProduct-example-001/step/tuning",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:name": "Instrument tuning",
            "schema:position": 2,
            "schema:description": "Synthetic step. ICP-MS tuned on a multi-element tuning solution for sensitivity and low oxide formation.",
            "schema:instrument": [
              {
                "@id": "ex:geochemProduct-example-001/instrument/instrument"
              },
              {
                "@type": [
                  "schema:ChemicalSubstance"
                ],
                "schema:name": "Multi-element tuning solution, 1 ug/L",
                "ada:reagentRole": "referenceMaterial",
                "schema:additionalType": [
                  {
                    "@id": "https://www.wikidata.org/entity/Q2356542"
                  }
                ]
              }
            ],
            "schema:additionalProperty": [
              {
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:name": "RF power",
                "schema:value": 1550,
                "schema:unitText": "W"
              },
              {
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:name": "Nebulizer gas flow",
                "schema:value": 1.05,
                "schema:unitText": "L/min"
              }
            ],
            "schema:actionStatus": "schema:CompletedActionStatus",
            "dqv:hasQualityMeasurement": [
              {
                "@type": [
                  "dqv:QualityMeasurement"
                ],
                "dqv:isMeasurementOf": "CeO+/Ce+ oxide ratio",
                "dqv:value": "1.2%"
              }
            ]
          },
          {
            "@id": "ex:geochemProduct-example-001/step/acquisition-1",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:name": "Data acquisition, first attempt",
            "schema:position": 3,
            "schema:description": "Synthetic step. First acquisition run, stopped when the drift monitor failed.",
            "schema:instrument": [
              {
                "@id": "ex:geochemProduct-example-001/instrument/instrument"
              }
            ],
            "schema:object": {
              "@id": "ex:geochemProduct-example-001/digest/RP-123"
            },
            "schema:startTime": "2026-01-10T09:30:00",
            "schema:endTime": "2026-01-10T10:05:00",
            "schema:actionStatus": "schema:FailedActionStatus",
            "schema:error": "Internal-standard (In) recovery fell below 80% after the third sample; run aborted and the cones cleaned."
          },
          {
            "@id": "ex:geochemProduct-example-001/step/acquisition-2",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:name": "Data acquisition",
            "schema:position": 4,
            "schema:description": "Synthetic step. Calibration standards, the digest and the secondary standard measured, with In as internal standard.",
            "schema:instrument": [
              {
                "@id": "ex:geochemProduct-example-001/instrument/instrument"
              },
              {
                "@type": [
                  "schema:DefinedTerm"
                ],
                "schema:name": "BHVO-2 basalt reference material",
                "schema:termCode": "BHVO-2",
                "schema:inDefinedTermSet": "http://georem.mpch-mainz.gwdg.de/",
                "ada:reagentRole": "primaryStandard",
                "schema:additionalType": [
                  {
                    "@id": "https://www.wikidata.org/entity/Q2356542"
                  }
                ]
              },
              {
                "@type": [
                  "schema:DefinedTerm"
                ],
                "schema:name": "BCR-2 basalt reference material",
                "schema:termCode": "BCR-2",
                "schema:inDefinedTermSet": "http://georem.mpch-mainz.gwdg.de/",
                "ada:reagentRole": "secondaryStandard",
                "schema:additionalType": [
                  {
                    "@id": "https://www.wikidata.org/entity/Q2356542"
                  }
                ]
              },
              {
                "@type": [
                  "schema:ChemicalSubstance"
                ],
                "schema:name": "2% HNO3 procedural blank",
                "ada:reagentRole": "blankMaterial",
                "schema:additionalType": [
                  {
                    "@id": "https://www.wikidata.org/entity/Q2356542"
                  }
                ]
              }
            ],
            "schema:participant": [
              {
                "@type": [
                  "schema:Person"
                ],
                "schema:name": "Example Laboratory Technician"
              }
            ],
            "schema:object": {
              "@id": "ex:geochemProduct-example-001/digest/RP-123"
            },
            "schema:startTime": "2026-01-10T11:00:00",
            "schema:endTime": "2026-01-10T14:30:00",
            "schema:actionStatus": "schema:CompletedActionStatus",
            "schema:result": {
              "@id": "ex:geochemProduct-example-001/data/RP-123-counts"
            }
          },
          {
            "@id": "ex:geochemProduct-example-001/step/reduction",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:name": "Data reduction",
            "schema:position": 5,
            "schema:description": "Synthetic step. Blank subtraction, internal-standard and drift correction, and calibration to concentrations.",
            "schema:additionalProperty": [
              {
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:name": "Internal standard",
                "schema:value": "115In"
              }
            ],
            "schema:object": {
              "@id": "ex:geochemProduct-example-001/data/RP-123-counts"
            },
            "schema:result": {
              "@id": "ex:geochemProduct-example-001/data/RP-123-concentrations"
            },
            "dqv:hasQualityMeasurement": [
              {
                "@type": [
                  "dqv:QualityMeasurement"
                ],
                "dqv:isMeasurementOf": "BCR-2 accuracy (mean deviation from certified values)",
                "dqv:value": "within 5%"
              }
            ],
            "schema:instrument": [
              {
                "@type": [
                  "schema:SoftwareApplication"
                ],
                "schema:name": "Example ICP-MS reduction software",
                "schema:version": "2.1",
                "ada:toolRole": "dataReduction",
                "schema:additionalType": [
                  {
                    "@id": "https://www.wikidata.org/entity/Q7397"
                  }
                ]
              }
            ]
          }
        ]
      },
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
          "@id": "ex:geochemProduct-example-001/sample/RP-123",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/geochemBaseProfile/context.jsonld",
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
      "dcat": "http://www.w3.org/ns/dcat#",
      "bios": "https://bioschemas.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "dqv": "http://www.w3.org/ns/dqv#"
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
      "schema:actionProcess": {
        "@type": [
          "schema:HowTo"
        ],
        "schema:name": "Synthetic solution ICP-MS trace-element workflow",
        "schema:isBasedOn": {
          "@id": "ex:solutionQicpmsTAPP-P0"
        },
        "schema:step": [
          {
            "@id": "ex:geochemProduct-example-001/step/digestion",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:name": "Sample digestion",
            "schema:position": 1,
            "schema:description": "Synthetic step. 100 mg of rock powder digested in HF-HNO3 on a hotplate, dried down and taken up in 2% HNO3.",
            "schema:additionalType": [
              {
                "@id": "bios:LabProcess"
              }
            ],
            "schema:agent": {
              "@type": [
                "schema:Person"
              ],
              "schema:name": "Example Analyst"
            },
            "schema:startTime": "2026-01-08T09:00:00",
            "schema:endTime": "2026-01-09T16:00:00",
            "schema:location": {
              "@type": [
                "schema:Place"
              ],
              "schema:name": "Clean laboratory, Analytical Sciences Laboratory"
            },
            "schema:object": {
              "@id": "ex:geochemProduct-example-001/sample/RP-123"
            },
            "schema:result": {
              "@id": "ex:geochemProduct-example-001/digest/RP-123"
            },
            "schema:instrument": [
              {
                "@type": [
                  "schema:ChemicalSubstance"
                ],
                "schema:name": "Concentrated HF, trace-metal grade",
                "ada:reagentRole": "reagent",
                "schema:additionalType": [
                  {
                    "@id": "https://www.wikidata.org/entity/Q2356542"
                  }
                ]
              },
              {
                "@type": [
                  "schema:ChemicalSubstance"
                ],
                "schema:name": "Concentrated HNO3, trace-metal grade",
                "ada:reagentRole": "reagent",
                "schema:additionalType": [
                  {
                    "@id": "https://www.wikidata.org/entity/Q2356542"
                  }
                ]
              }
            ]
          },
          {
            "@id": "ex:geochemProduct-example-001/step/tuning",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:name": "Instrument tuning",
            "schema:position": 2,
            "schema:description": "Synthetic step. ICP-MS tuned on a multi-element tuning solution for sensitivity and low oxide formation.",
            "schema:instrument": [
              {
                "@id": "ex:geochemProduct-example-001/instrument/instrument"
              },
              {
                "@type": [
                  "schema:ChemicalSubstance"
                ],
                "schema:name": "Multi-element tuning solution, 1 ug/L",
                "ada:reagentRole": "referenceMaterial",
                "schema:additionalType": [
                  {
                    "@id": "https://www.wikidata.org/entity/Q2356542"
                  }
                ]
              }
            ],
            "schema:additionalProperty": [
              {
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:name": "RF power",
                "schema:value": 1550,
                "schema:unitText": "W"
              },
              {
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:name": "Nebulizer gas flow",
                "schema:value": 1.05,
                "schema:unitText": "L/min"
              }
            ],
            "schema:actionStatus": "schema:CompletedActionStatus",
            "dqv:hasQualityMeasurement": [
              {
                "@type": [
                  "dqv:QualityMeasurement"
                ],
                "dqv:isMeasurementOf": "CeO+/Ce+ oxide ratio",
                "dqv:value": "1.2%"
              }
            ]
          },
          {
            "@id": "ex:geochemProduct-example-001/step/acquisition-1",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:name": "Data acquisition, first attempt",
            "schema:position": 3,
            "schema:description": "Synthetic step. First acquisition run, stopped when the drift monitor failed.",
            "schema:instrument": [
              {
                "@id": "ex:geochemProduct-example-001/instrument/instrument"
              }
            ],
            "schema:object": {
              "@id": "ex:geochemProduct-example-001/digest/RP-123"
            },
            "schema:startTime": "2026-01-10T09:30:00",
            "schema:endTime": "2026-01-10T10:05:00",
            "schema:actionStatus": "schema:FailedActionStatus",
            "schema:error": "Internal-standard (In) recovery fell below 80% after the third sample; run aborted and the cones cleaned."
          },
          {
            "@id": "ex:geochemProduct-example-001/step/acquisition-2",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:name": "Data acquisition",
            "schema:position": 4,
            "schema:description": "Synthetic step. Calibration standards, the digest and the secondary standard measured, with In as internal standard.",
            "schema:instrument": [
              {
                "@id": "ex:geochemProduct-example-001/instrument/instrument"
              },
              {
                "@type": [
                  "schema:DefinedTerm"
                ],
                "schema:name": "BHVO-2 basalt reference material",
                "schema:termCode": "BHVO-2",
                "schema:inDefinedTermSet": "http://georem.mpch-mainz.gwdg.de/",
                "ada:reagentRole": "primaryStandard",
                "schema:additionalType": [
                  {
                    "@id": "https://www.wikidata.org/entity/Q2356542"
                  }
                ]
              },
              {
                "@type": [
                  "schema:DefinedTerm"
                ],
                "schema:name": "BCR-2 basalt reference material",
                "schema:termCode": "BCR-2",
                "schema:inDefinedTermSet": "http://georem.mpch-mainz.gwdg.de/",
                "ada:reagentRole": "secondaryStandard",
                "schema:additionalType": [
                  {
                    "@id": "https://www.wikidata.org/entity/Q2356542"
                  }
                ]
              },
              {
                "@type": [
                  "schema:ChemicalSubstance"
                ],
                "schema:name": "2% HNO3 procedural blank",
                "ada:reagentRole": "blankMaterial",
                "schema:additionalType": [
                  {
                    "@id": "https://www.wikidata.org/entity/Q2356542"
                  }
                ]
              }
            ],
            "schema:participant": [
              {
                "@type": [
                  "schema:Person"
                ],
                "schema:name": "Example Laboratory Technician"
              }
            ],
            "schema:object": {
              "@id": "ex:geochemProduct-example-001/digest/RP-123"
            },
            "schema:startTime": "2026-01-10T11:00:00",
            "schema:endTime": "2026-01-10T14:30:00",
            "schema:actionStatus": "schema:CompletedActionStatus",
            "schema:result": {
              "@id": "ex:geochemProduct-example-001/data/RP-123-counts"
            }
          },
          {
            "@id": "ex:geochemProduct-example-001/step/reduction",
            "@type": [
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:name": "Data reduction",
            "schema:position": 5,
            "schema:description": "Synthetic step. Blank subtraction, internal-standard and drift correction, and calibration to concentrations.",
            "schema:additionalProperty": [
              {
                "@type": [
                  "schema:PropertyValue"
                ],
                "schema:name": "Internal standard",
                "schema:value": "115In"
              }
            ],
            "schema:object": {
              "@id": "ex:geochemProduct-example-001/data/RP-123-counts"
            },
            "schema:result": {
              "@id": "ex:geochemProduct-example-001/data/RP-123-concentrations"
            },
            "dqv:hasQualityMeasurement": [
              {
                "@type": [
                  "dqv:QualityMeasurement"
                ],
                "dqv:isMeasurementOf": "BCR-2 accuracy (mean deviation from certified values)",
                "dqv:value": "within 5%"
              }
            ],
            "schema:instrument": [
              {
                "@type": [
                  "schema:SoftwareApplication"
                ],
                "schema:name": "Example ICP-MS reduction software",
                "schema:version": "2.1",
                "ada:toolRole": "dataReduction",
                "schema:additionalType": [
                  {
                    "@id": "https://www.wikidata.org/entity/Q7397"
                  }
                ]
              }
            ]
          }
        ]
      },
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
          "@id": "ex:geochemProduct-example-001/sample/RP-123",
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
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://cdif.org/0.1/> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix dqv: <http://www.w3.org/ns/dqv#> .
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
            schema1:actionProcess [ a schema1:HowTo ;
                    schema1:isBasedOn ex:solutionQicpmsTAPP-P0 ;
                    schema1:name "Synthetic solution ICP-MS trace-element workflow" ;
                    schema1:step <https://example.org/geochemProduct-example-001/step/acquisition-1>,
                        <https://example.org/geochemProduct-example-001/step/acquisition-2>,
                        <https://example.org/geochemProduct-example-001/step/digestion>,
                        <https://example.org/geochemProduct-example-001/step/reduction>,
                        <https://example.org/geochemProduct-example-001/step/tuning> ] ;
            schema1:identifier "session-geochem-20260110-001" ;
            schema1:instrument <https://example.org/geochemProduct-example-001/instrument/instrument> ;
            schema1:location [ a schema1:Place ;
                    schema1:identifier "https://ror.org/00hx57361" ;
                    schema1:name "Analytical Sciences Laboratory" ] ;
            schema1:object <https://example.org/geochemProduct-example-001/sample/RP-123> ;
            schema1:startTime "2026-01-10T09:30:00" ] .

<https://example.org/geochemProduct-example-001/step/acquisition-1> a schema1:Action,
        schema1:HowToStep ;
    schema1:actionStatus "schema:FailedActionStatus" ;
    schema1:description "Synthetic step. First acquisition run, stopped when the drift monitor failed." ;
    schema1:endTime "2026-01-10T10:05:00" ;
    schema1:error "Internal-standard (In) recovery fell below 80% after the third sample; run aborted and the cones cleaned." ;
    schema1:instrument <https://example.org/geochemProduct-example-001/instrument/instrument> ;
    schema1:name "Data acquisition, first attempt" ;
    schema1:object <https://example.org/geochemProduct-example-001/digest/RP-123> ;
    schema1:position 3 ;
    schema1:startTime "2026-01-10T09:30:00" .

<https://example.org/geochemProduct-example-001/step/acquisition-2> a schema1:Action,
        schema1:HowToStep ;
    schema1:actionStatus "schema:CompletedActionStatus" ;
    schema1:description "Synthetic step. Calibration standards, the digest and the secondary standard measured, with In as internal standard." ;
    schema1:endTime "2026-01-10T14:30:00" ;
    schema1:instrument [ a schema1:DefinedTerm ;
            schema1:additionalType wd:Q2356542 ;
            schema1:inDefinedTermSet "http://georem.mpch-mainz.gwdg.de/" ;
            schema1:name "BCR-2 basalt reference material" ;
            schema1:termCode "BCR-2" ;
            ada:reagentRole "secondaryStandard" ],
        [ a schema1:ChemicalSubstance ;
            schema1:additionalType wd:Q2356542 ;
            schema1:name "2% HNO3 procedural blank" ;
            ada:reagentRole "blankMaterial" ],
        [ a schema1:DefinedTerm ;
            schema1:additionalType wd:Q2356542 ;
            schema1:inDefinedTermSet "http://georem.mpch-mainz.gwdg.de/" ;
            schema1:name "BHVO-2 basalt reference material" ;
            schema1:termCode "BHVO-2" ;
            ada:reagentRole "primaryStandard" ],
        <https://example.org/geochemProduct-example-001/instrument/instrument> ;
    schema1:name "Data acquisition" ;
    schema1:object <https://example.org/geochemProduct-example-001/digest/RP-123> ;
    schema1:participant [ a schema1:Person ;
            schema1:name "Example Laboratory Technician" ] ;
    schema1:position 4 ;
    schema1:result <https://example.org/geochemProduct-example-001/data/RP-123-counts> ;
    schema1:startTime "2026-01-10T11:00:00" .

<https://example.org/geochemProduct-example-001/step/digestion> a schema1:Action,
        schema1:HowToStep ;
    schema1:additionalType bios:LabProcess ;
    schema1:agent [ a schema1:Person ;
            schema1:name "Example Analyst" ] ;
    schema1:description "Synthetic step. 100 mg of rock powder digested in HF-HNO3 on a hotplate, dried down and taken up in 2% HNO3." ;
    schema1:endTime "2026-01-09T16:00:00" ;
    schema1:instrument [ a schema1:ChemicalSubstance ;
            schema1:additionalType wd:Q2356542 ;
            schema1:name "Concentrated HF, trace-metal grade" ;
            ada:reagentRole "reagent" ],
        [ a schema1:ChemicalSubstance ;
            schema1:additionalType wd:Q2356542 ;
            schema1:name "Concentrated HNO3, trace-metal grade" ;
            ada:reagentRole "reagent" ] ;
    schema1:location [ a schema1:Place ;
            schema1:name "Clean laboratory, Analytical Sciences Laboratory" ] ;
    schema1:name "Sample digestion" ;
    schema1:object <https://example.org/geochemProduct-example-001/sample/RP-123> ;
    schema1:position 1 ;
    schema1:result <https://example.org/geochemProduct-example-001/digest/RP-123> ;
    schema1:startTime "2026-01-08T09:00:00" .

<https://example.org/geochemProduct-example-001/step/reduction> a schema1:Action,
        schema1:HowToStep ;
    schema1:additionalProperty [ a schema1:PropertyValue ;
            schema1:name "Internal standard" ;
            schema1:value "115In" ] ;
    schema1:description "Synthetic step. Blank subtraction, internal-standard and drift correction, and calibration to concentrations." ;
    schema1:instrument [ a schema1:SoftwareApplication ;
            schema1:additionalType wd:Q7397 ;
            schema1:name "Example ICP-MS reduction software" ;
            schema1:version "2.1" ;
            ada:toolRole "dataReduction" ] ;
    schema1:name "Data reduction" ;
    schema1:object <https://example.org/geochemProduct-example-001/data/RP-123-counts> ;
    schema1:position 5 ;
    schema1:result <https://example.org/geochemProduct-example-001/data/RP-123-concentrations> ;
    dqv:hasQualityMeasurement [ a dqv:QualityMeasurement ;
            dqv:isMeasurementOf "BCR-2 accuracy (mean deviation from certified values)" ;
            dqv:value "within 5%" ] .

<https://example.org/geochemProduct-example-001/step/tuning> a schema1:Action,
        schema1:HowToStep ;
    schema1:actionStatus "schema:CompletedActionStatus" ;
    schema1:additionalProperty [ a schema1:PropertyValue ;
            schema1:name "RF power" ;
            schema1:unitText "W" ;
            schema1:value 1550 ],
        [ a schema1:PropertyValue ;
            schema1:name "Nebulizer gas flow" ;
            schema1:unitText "L/min" ;
            schema1:value 1.05e+00 ] ;
    schema1:description "Synthetic step. ICP-MS tuned on a multi-element tuning solution for sensitivity and low oxide formation." ;
    schema1:instrument [ a schema1:ChemicalSubstance ;
            schema1:additionalType wd:Q2356542 ;
            schema1:name "Multi-element tuning solution, 1 ug/L" ;
            ada:reagentRole "referenceMaterial" ],
        <https://example.org/geochemProduct-example-001/instrument/instrument> ;
    schema1:name "Instrument tuning" ;
    schema1:position 2 ;
    dqv:hasQualityMeasurement [ a dqv:QualityMeasurement ;
            dqv:isMeasurementOf "CeO+/Ce+ oxide ratio" ;
            dqv:value "1.2%" ] .

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

<https://example.org/geochemProduct-example-001/sample/RP-123> a schema1:Thing,
        <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
    schema1:additionalType "MaterialSample" ;
    schema1:description "Homogenized rock powder aliquot analysed in this session" ;
    schema1:identifier "igsn:10.60471/GSEEXAMPLE001" ;
    schema1:name "Example rock powder aliquot RP-123" .

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

<https://example.org/geochemProduct-example-001/instrument/instrument> a schema1:Product,
        schema1:Thing ;
    schema1:additionalType <https://manual.nexusformat.org/classes/base_classes/NXinstrument.html>,
        wd:Q3099911 ;
    schema1:identifier "ex:instrument-001" ;
    schema1:name "Example ICP-MS Instrument" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
$id: https://w3id.org/geochem/schema/geochemBaseProfile/1.0
title: Geochem Base Profile
description: 'The geochemistry overlay on its own: the analytical surface this repository
  contributes on top of the CDIF profiles. The analysis events that produced a product
  (instruments, computational tools, reagents, laboratory, samples analysed), the
  product-type and licence declarations, the distributions and their parts, and the
  geochem-specific variable, parameter and coverage shapes.

  It imports no CDIF schema and composes nothing. geochemProduct is the composition
  -- the CDIF core, data-description, manifest and provenance profiles together with
  this overlay -- and this file is the half of that which gBB authors. Factored out
  2026-11-04, following the cdifProfile / cdifCompositeProfile split upstream, so
  that what gBB contributes can be read, diffed and reviewed without the imported
  profiles around it.

  "Overlay" rather than "additions", deliberately: most of these keys exist upstream
  and this block narrows them and carries their gBB labels. A pure refinement of a
  CDIF property is the normal case here, not the exception.

  Not a standalone record schema: on its own it constrains an object that carries
  the geochem surface and says nothing about the CDIF properties a record also needs.
  Compose it, or reference geochemProduct.'
type: object
properties:
  '@type':
    title: Record Type
    type: array
    items:
      type: string
      enum:
      - schema:Dataset
      - schema:Product
  schema:license:
    title: License
    description: Legal statement of conditions for use and access
    type: array
    minItems: 0
    items:
      anyOf:
      - type: string
      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/creativeWork/schema.yaml
    x-jsonld-id: http://schema.org/license
  schema:relatedLink:
    title: Related Links
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
    title: Status
    type: string
    x-jsonld-id: http://schema.org/creativeWorkStatus
  schema:measurementTechnique:
    title: Measurement Technique
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
          title: Technique Identifier
          type: string
          x-jsonld-id: http://schema.org/identifier
    x-jsonld-id: http://schema.org/measurementTechnique
  prov:wasGeneratedBy:
    title: Analysis Events
    description: 'Analysis events. Extends cdifProvActivity (from cdifProvenance)
      with the generic geochem analysis-event surface: the instruments, computational
      tools and reagents actually used (schema:instrument); the laboratory; the samples
      analysed (schema:object); the TAPP the analysis followed (schema:actionProcess);
      and the session identifier and timing.'
    type: array
    items:
      type: object
      properties:
        schema:actionProcess:
          description: 'The TAPP this analysis event followed, or the workflow as
            it was performed.

            Two forms, after the CDIF plan link (cdifProvActivity; option A of the
            2026-11-11 activity-used-resources proposal). A bare {"@id": ...} is the
            link to the TAPP definition, which is typed schema:HowTo for exactly this
            reason. An inline schema:HowTo is the workflow as performed; when the
            event also followed a TAPP, that HowTo names it with schema:isBasedOn.
            One path finds the TAPP either way: prov:wasGeneratedBy/schema:actionProcess/schema:isBasedOn?.
            The TAPP link used to be the role-keyed prov:used wrapper {"ada:tappDefinition":
            {...}}, which is closed off below. Inline TAPPs are not accepted here:
            none existed in ada2 or ada_subjects when the link moved (measured 2026-11-11),
            so the reference is the only form.

            The reference is SEALED, as the ada:tappDefinition reference was, and
            so is schema:isBasedOn: a TAPP link names the plan and says nothing else
            about it.

            The base cdifProvActivity already supplies a schema:HowTo here, but its
            step shape carries only @type / name / description / position / url. A
            geochem analysis event needs the same step surface the TAPP plan uses
            -- per-step instruments, computational tools and reagents (schema:instrument),
            inputs (schema:object), result, parameters and sub-workflow -- so the
            step items are pinned to tappDefinition''s WorkflowStep. Both apply: the
            base and this intersect under allOf, and neither the base HowTo nor its
            step is a closed object, so the richer shape adds to it rather than conflicting.

            WorkflowStep, NOT WorkflowHowTo, is deliberate. The requirement for exactly
            one "Sample preparation" step carrying bios:LabProcess lives on WorkflowHowTo,
            and it belongs to the TAPP plan -- a protocol must say how the sample
            was prepared. An analysis EVENT records what was done and may legitimately
            describe only part of a workflow, so referencing the step shape alone
            brings the structure without that requirement.'
          anyOf:
          - type: string
          - description: The link to the TAPP definition this analysis followed.
            type: object
            additionalProperties: false
            required:
            - '@id'
            properties:
              '@id':
                type: string
          - description: The workflow as performed, as a schema:HowTo.
            type: object
            required:
            - '@type'
            properties:
              '@type':
                type: array
                contains:
                  const: schema:HowTo
          properties:
            schema:isBasedOn:
              description: The TAPP definition this workflow was based on, by reference.
              type: object
              additionalProperties: false
              required:
              - '@id'
              properties:
                '@id':
                  type: string
              x-jsonld-id: http://schema.org/isBasedOn
            schema:step:
              type: array
              items:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/WorkflowStep
              x-jsonld-id: http://schema.org/step
          x-jsonld-id: http://schema.org/actionProcess
        schema:instrument:
          title: Resources Used
          type: array
          description: 'What the analysis used, other than its samples: the instruments,
            the computational tools actually used (acquisition, reduction, processing)
            and the reagents and reference materials actually used. One array, the
            kinds told apart by the Wikidata term each item carries in schema:additionalType
            -- Q3099911 (measuring instrument), Q7397 (software), Q2356542 (chemical
            reagent) -- which is the CDIF cdifProvActivity rule. Each item is one
            of those, or a sealed {@id} reference (the CDIF base admits both, and
            requires exactly one kind term on an item described in place). The TAPP
            plan prescribes the generic instruments, tools and reagents; these record
            the ACTUALS used in this specific run.'
          items:
            allOf:
            - if:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/KindInstrument
              then:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/instrument/schema.yaml
            - if:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/KindSoftware
              then:
                $ref: '#/$defs/UsedComputationalTool'
            - if:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/KindReagent
              then:
                $ref: '#/$defs/UsedReagent'
          x-jsonld-id: http://schema.org/instrument
        prov:used:
          description: 'Not where this profile records what an analysis used: instruments,
            tools and reagents are schema:instrument, samples are schema:object, and
            the TAPP link is schema:actionProcess. A prov:used that passes the CDIF
            core shape (strings and @id references) is accepted and checked by nothing
            more.

            The superseded spellings are CLOSED OFF, so a writer that regressed to
            one fails, naming the key, instead of passing silently. The role-keyed
            wrappers carry no @id and the CDIF core rejects them already; these close
            them off by name, and close off the one old form that does carry an @id
            -- an item typed ada:TAPPDefinition. Same sequence as the earlier close-offs:
            the records move first (the ADA stores are migrated before this is published),
            then the schema.'
          type: array
          items:
            properties:
              schema:instrument:
                description: 'Superseded wrapper: an instrument is an item of the
                  activity''s own schema:instrument.'
                not: {}
                x-jsonld-id: http://schema.org/instrument
              bios:computationalTool:
                description: 'Superseded wrapper: a computational tool is a schema:instrument
                  item of the software kind (Wikidata Q7397).'
                not: {}
                x-jsonld-id: https://bioschemas.org/computationalTool
              bios:reagent:
                description: 'Superseded wrapper: a reagent is a schema:instrument
                  item of the reagent kind (Wikidata Q2356542).'
                not: {}
                x-jsonld-id: https://bioschemas.org/reagent
              prov:reagent:
                description: 'Superseded twice over (prov:reagent, then bios:reagent):
                  a reagent is a schema:instrument item of the reagent kind.'
                not: {}
                x-jsonld-id: http://www.w3.org/ns/prov#reagent
              ada:tappDefinition:
                description: 'Superseded wrapper: the TAPP link is schema:actionProcess
                  {"@id": ...}, or schema:isBasedOn on the event''s inline workflow.'
                not: {}
                x-jsonld-id: https://ada.astromat.org/metadata/tappDefinition
            allOf:
            - if:
                type: object
                required:
                - '@type'
                properties:
                  '@type':
                    contains:
                      const: ada:TAPPDefinition
              then:
                description: 'A TAPP is not a prov:used entity: link it with schema:actionProcess
                  {"@id": ...}, or with schema:isBasedOn on the event''s inline workflow.'
                properties:
                  '@type':
                    not:
                      contains:
                        const: ada:TAPPDefinition
          x-jsonld-id: http://www.w3.org/ns/prov#used
        schema:location:
          title: Laboratory
          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/laboratory/schema.yaml
          x-jsonld-id: http://schema.org/location
        schema:object:
          title: Samples Analyzed
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
                  $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifConceptOrTermOrString/schema.yaml
                x-jsonld-id: http://schema.org/additionalType
              schema:identifier:
                title: Sample Identifier
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
                  $ref: '#/$defs/PropertyValueEntry'
                x-jsonld-id: http://schema.org/additionalProperty
              ada:spatialRegistration:
                title: Spatial Registration
                description: 'The coordinate system defined ON the sample -- typically
                  a planar thin section -- that image pixel coordinates are registered
                  to. Distinct from the ada:spatialRegistration on an image or imageMap
                  part, which maps pixel coordinates WITHIN one file: this one is
                  the frame those are registered to, and is what lets two images of
                  the same section be compared. Optional, and no record carries it
                  yet.'
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/spatialRegistration/schema.yaml
                x-jsonld-id: https://ada.astromat.org/metadata/spatialRegistration
          x-jsonld-id: http://schema.org/object
        schema:identifier:
          title: Session Identifier
          description: The analytical session's own identifier -- the laboratory's
            run, sequence or batch identifier as generated by the instrument or acquisition
            software. Sits on the activity rather than the dataset because the session
            IS the activity.
          type: string
          x-jsonld-id: http://schema.org/identifier
        schema:startTime:
          title: Start Time
          type: string
          x-jsonld-id: http://schema.org/startTime
        schema:endTime:
          title: End Time
          type: string
          x-jsonld-id: http://schema.org/endTime
        schema:startDate:
          description: 'Superseded: the analysis start is schema:startTime. Rename
            the key.'
          not: {}
          x-jsonld-id: http://schema.org/startDate
        schema:endDate:
          description: 'Superseded: the analysis end is schema:endTime. Rename the
            key.'
          not: {}
          x-jsonld-id: http://schema.org/endDate
        schema:additionalProperty:
          description: Per-analysis PropertyValue entries (replicates, transect length,
            ...); technique profiles constrain these.
          type: array
          items:
            $ref: '#/$defs/PropertyValueEntry'
          x-jsonld-id: http://schema.org/additionalProperty
        ada:combinedResults:
          description: 'The reported values this session obtained by averaging or
            otherwise combining several individual results -- the ROWS of the combined-result
            table, and the domain that `defines: combined result` enumerates (Rule
            7; see the Legends sheet of any delivered TAPP). One entry per combined
            value, each naming what it combines: "Olivine, sample A, 8 points", "Zircon
            weighted-mean date, sample B, 236 of 246 spots", "Isochron, sample C,
            36 runs".

            On the ACTIVITY rather than on a sample, because a combined result names
            its own sample and need not belong to exactly one -- an isochron over
            36 runs is the case in hand.

            It is METADATA, unlike a sampling unit, and the difference is worth being
            clear about because an earlier design got it wrong. A combined result
            is a statement the record makes about its own contents, so it belongs
            here. An individual sampling unit is not: the procedure and the analysis
            can state only the KIND of unit (ada:samplingUnitType), while a particular
            unit''s identifier is a schema:variableMeasured naming a COLUMN in one
            of the distributions, and the binding from that unit to its target material
            exists only in the instance data table beside the results. There is therefore
            no array of sampling-unit objects here; one was added on 2026-09-25 and
            removed on 2026-10-01 once that was settled.

            Analysis-side only: the procedure can say HOW results will be combined
            (Combination Method, keyed by reported property) but not WHICH were, so
            there is no ada:combinedResults counterpart in tappDefinition.

            Fields keyed `combined result x reported property` -- Goodness-of-Fit
            or Dispersion Statistic, and Other Statistics -- ride on these rows as
            per-reported- property values, keyed by the valueName of the column that
            declared them.'
          type: array
          items:
            type: object
            required:
            - schema:name
            properties:
              '@id':
                description: Optional identifier for this combined result.
                type: string
              schema:name:
                description: What this combined value is and what it combines. Required,
                  because a combined result nothing can name gives a field keyed by
                  combined result no row to attach its value to.
                type: string
                x-jsonld-id: http://schema.org/name
          x-jsonld-id: https://ada.astromat.org/metadata/combinedResults
      required:
      - schema:location
    x-jsonld-id: http://www.w3.org/ns/prov#wasGeneratedBy
  schema:variableMeasured:
    title: Measured Variables
    description: Variable definitions. Extends cdifInstanceVariable (from cdifDataDescription)
      with additional generic properties. Requires a description with minLength 3.
    type: array
    items:
      type: object
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
          title: Alternate Name
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
      required:
      - schema:description
      - '@type'
    x-jsonld-id: http://schema.org/variableMeasured
  schema:spatialCoverage:
    title: Spatial Coverage
    description: Geographic extent of resource content.
    type: array
    items:
      $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/spatialExtent/schema.yaml
    x-jsonld-id: http://schema.org/spatialCoverage
  schema:temporalCoverage:
    title: Temporal Coverage
    description: Temporal extent of resource content.
    type: array
    items:
      $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/temporalExtent/schema.yaml
    x-jsonld-id: http://schema.org/temporalCoverage
  dqv:hasQualityMeasurement:
    title: Quality Measurements
    description: Quality measurements reported to assess the resource.
    type: array
    items:
      $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/qualityProperties/qualityMeasure/schema.yaml
  schema:additionalProperty:
    title: Additional Properties
    description: PropertyValue entries describing the DELIVERED DATA rather than the
      analysis that produced it (extent, dimensions, ...). Distinct from the per-analysis
      prov:wasGeneratedBy.schema:additionalProperty. Technique profiles constrain
      these.
    type: array
    items:
      $ref: '#/$defs/PropertyValueEntry'
    x-jsonld-id: http://schema.org/additionalProperty
  schema:distribution:
    title: Distributions
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
            (the file is the dataset), or a structure shared across bundle parts and
            referenced from them by @id. One of the four CDIF DataStructure variants
            inline, or an @id reference. Optional.
          anyOf:
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifDataStructure/schema.yaml#/$defs/DataStructure
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifDataStructure/schema.yaml#/$defs/DimensionalDataStructure
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifDataStructure/schema.yaml#/$defs/LongDataStructure
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifDataStructure/schema.yaml#/$defs/WideDataStructure
          - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/objectReference/schema.yaml
          x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isStructuredBy
        schema:additionalType:
          description: Optional file-classification of this distribution (or, on a
            bundle, of the whole archive) drawn from the componentType vocabulary
            (ada:vocab/componentType) -- e.g. "ada:report", "ada:calibrationFile".
            Generic and OPTIONAL here; the ADA product layer (adaProduct) instead
            carries the required ada:componentType. Advisory (annotated via schema:inDefinedTermSet),
            not hard-enumerated in JSON Schema.
          type: array
          items:
            $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifConceptOrTermOrString/schema.yaml
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
    title: About This Record
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
  schema:name:
    title: Dataset Name
    x-jsonld-id: http://schema.org/name
  schema:description:
    title: Description
    x-jsonld-id: http://schema.org/description
  schema:identifier:
    title: Primary Identifier
    x-jsonld-id: http://schema.org/identifier
  schema:sameAs:
    title: Other Identifiers
    x-jsonld-id: http://schema.org/sameAs
  schema:url:
    title: Landing Page
    x-jsonld-id: http://schema.org/url
  schema:version:
    title: Version
    x-jsonld-id: http://schema.org/version
  schema:creator:
    title: Authors
    x-jsonld-id: http://schema.org/creator
  schema:contributor:
    title: Contributors
    x-jsonld-id: http://schema.org/contributor
  schema:publisher:
    title: Publisher
    x-jsonld-id: http://schema.org/publisher
  schema:provider:
    title: Provider
    x-jsonld-id: http://schema.org/provider
  schema:funding:
    title: Funding Source
    x-jsonld-id: http://schema.org/funding
  schema:conditionsOfAccess:
    title: Access Conditions
    x-jsonld-id: http://schema.org/conditionsOfAccess
  schema:publishingPrinciples:
    title: Publishing Principles
    x-jsonld-id: http://schema.org/publishingPrinciples
  schema:dateModified:
    title: Date Modified
    x-jsonld-id: http://schema.org/dateModified
  schema:datePublished:
    title: Date Published
    x-jsonld-id: http://schema.org/datePublished
  schema:inLanguage:
    title: Language
    x-jsonld-id: http://schema.org/inLanguage
  schema:keywords:
    title: Keywords
    x-jsonld-id: http://schema.org/keywords
  schema:additionalType:
    title: Product Type
    x-jsonld-id: http://schema.org/additionalType
  prov:wasDerivedFrom:
    title: Derived From
    x-jsonld-id: http://www.w3.org/ns/prov#wasDerivedFrom
  '@id':
    title: Record IRI
$defs:
  UsedComputationalTool:
    type: object
    additionalProperties: false
    description: 'Computational tool actually used (acquisition, data reduction, or
      processing): a schema:instrument item of the software kind.'
    properties:
      schema:additionalType:
        description: 'Carries the Wikidata kind term, https://www.wikidata.org/entity/Q7397
          (software), as {"@id": ...}: what makes this a software item of the activity''s
          schema:instrument.'
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifConceptOrTermOrString/schema.yaml
        x-jsonld-id: http://schema.org/additionalType
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
    description: 'Reference material, calibration standard, or chemical reagent actually
      used: a schema:instrument item of the reagent kind.'
    properties:
      schema:additionalType:
        description: 'Carries the Wikidata kind term, https://www.wikidata.org/entity/Q2356542
          (chemical reagent), as {"@id": ...}: what makes this a reagent item of the
          activity''s schema:instrument.'
        type: array
        items:
          $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifConceptOrTermOrString/schema.yaml
        x-jsonld-id: http://schema.org/additionalType
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
              $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/cdifConceptOrTermOrString/schema.yaml
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
  PropertyValueEntry:
    description: 'One entry of a schema:additionalProperty array: a named value carried
      on the dataset, on an analysis, or on a sample. The three sites above delegate
      their per-technique CONTENT to the technique profiles -- which property names
      are allowed, and with what values -- and this def supplies only the ENTRY SHAPE
      those names are carried in, so that a placement path such as `schema:additionalProperty[schema:name=''Map
      Area''].schema:value` names something the schema has heard of.

      Measured across all 2047 additionalProperty entries in this repository''s examples
      (2026-10-08): every one carries both ''@type'' and ''schema:name'', and none
      carries a property outside the set below, so the two required keys are measured
      rather than assumed. ''@type'' is always a one-element array.

      DELIBERATELY NOT SEALED. additionalProperties is left open so a technique profile
      can add a property without every consumer of this block having to learn about
      it first -- the same reason the sites delegate in the first place. The consequence
      is that a MISSPELLED property here still validates; what this def buys is that
      the register''s path checker (amds-ldeo/metadata, loaders/map_subject_keys.py)
      can now tell a real typo from a node that simply declares nothing. Before it
      existed, those two were the same report, and 18 correct paths were indistinguishable
      from a wrong one.'
    type: object
    properties:
      '@id':
        description: Identifier for this entry, so it can be referenced -- typically
          the CURIE of the parameter it instantiates, e.g. ada:parameter/labxctTAPP/xrayEnergy.
          Not a resolvable URL, so no format assertion.
        type: string
      '@type':
        type: array
        minItems: 1
        items:
          type: string
        contains:
          enum:
          - schema:PropertyValue
          - schema:PropertyValueSpecification
      schema:name:
        description: Human-readable label, matching the TAPP Metadata Item where one
          exists.
        type: string
        minLength: 1
        x-jsonld-id: http://schema.org/name
      schema:value:
        description: 'The value. Left untyped on purpose: measured as string, integer
          and number across the examples, and a technique profile is the right place
          to pin one.'
        x-jsonld-id: http://schema.org/value
      schema:propertyID:
        description: URI(s) identifying this property in a vocabulary. Always an array
          of IRI-reference objects where present; left unconstrained here because
          the profiles that care already constrain it.
        x-jsonld-id: http://schema.org/propertyID
      schema:unitText:
        description: Unit the value is expressed in, as written.
        type: string
        x-jsonld-id: http://schema.org/unitText
      schema:description:
        type: string
        x-jsonld-id: http://schema.org/description
      schema:valueName:
        description: Machine-readable name, for serialization and form binding.
        type: string
        x-jsonld-id: http://schema.org/valueName
      schema:defaultValue:
        description: Value carried into an analysis from the procedure, where the
          entry is a spec.
        x-jsonld-id: http://schema.org/defaultValue
      ada:dataType:
        type: string
        x-jsonld-id: https://ada.astromat.org/metadata/dataType
      ada:fieldScope:
        type: string
        x-jsonld-id: https://ada.astromat.org/metadata/fieldScope
    required:
    - '@type'
    - schema:name
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
  itemIdentifier: ogch.BaseSchema.geochemBaseProfile
  register: https://amds-ldeo.github.io/geochemBuildingBlocks/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-12'

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/geochemBaseProfile/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/geochemBaseProfile/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "prov": "http://www.w3.org/ns/prov#",
    "bios": "https://bioschemas.org/",
    "spdx": "http://spdx.org/rdf/terms#",
    "nxs": "https://manual.nexusformat.org/classes/",
    "dcterms": "http://purl.org/dc/terms/",
    "geosparql": "http://www.opengis.net/ont/geosparql#",
    "dqv": "http://www.w3.org/ns/dqv#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "wd": "https://www.wikidata.org/entity/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "time": "http://www.w3.org/2006/time#",
    "cdif": "https://w3id.org/cdif/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "xas": "cdif:xas/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/geochemBaseProfile/context.jsonld)

## Sources

* [Factored out of geochemProduct, following the cdifProfile / cdifCompositeProfile split](https://github.com/Cross-Domain-Interoperability-Framework/metadataBuildingBlocks)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/BaseSchema/geochemBaseProfile`

