
# EMPA Geochem Profile (Schema)

`ogch.profiles.geochemProfiles.empaProfile` *v0.1*

Technique-specific dataset profile for EMPA. Extends adaProduct with constraints on schema:measurementTechnique (pointing at empaTAPP) and schema:distribution.schema:hasPart (allowing detailEMPA entries).

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### empaProfile minimal example
Smallest valid empaProfile dataset record. Demonstrates only the required
adaProduct fields plus the empaProfile-specific empaTAPP measurement-technique
@id reference and a single detailEMPA hasPart item (EMPAImageMap).
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
    "dcat": "http://www.w3.org/ns/dcat#",
    "ex": "https://example.org/"
  },
  "@id": "ex:empaProfile-minimal-001",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "Minimal empaProfile Example",
  "schema:description": "Smallest valid empaProfile dataset record. Demonstrates only the required adaProduct fields plus the empaProfile-specific empaTAPP measurement-technique reference and a single detailEMPA hasPart item.",
  "schema:additionalType": [
    "Electron Microprobe Analysis Image (EMPA)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.99999/empaprofile-minimal-001",
    "schema:url": "https://doi.org/10.99999/empaprofile-minimal-001"
  },
  "schema:dateModified": "2026-05-01",
  "schema:license": [
    "https://creativecommons.org/publicdomain/zero/1.0/"
  ],
  "schema:measurementTechnique": {
    "@id": "ex:empaTAPP-minimal"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-empa-min-001",
      "schema:startDate": "2026-05-01T09:00:00",
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
            "ex:instrument-empa-min-001"
          ]
        }
      ]
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "ex:empaProfile-minimal-var-001",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "SiO2_wt_pct",
      "schema:description": "Silicon dioxide concentration in weight percent.",
      "schema:unitText": "wt%",
      "cdi:role": "MeasureComponent"
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "empaProfile-minimal-archive.zip",
      "schema:description": "Single-file EMPA bundle for the minimal example.",
      "schema:contentUrl": "https://example.org/downloads/empaprofile-minimal-001.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "schema:hasPart": [
        {
          "@id": "ex:empaProfile-minimal-file-001",
          "@type": [
            "schema:MediaObject",
            "ada:imageMap",
            "schema:ImageObject"
          ],
          "schema:name": "minimal_EMPA_001.tif",
          "schema:description": "Minimal EMPA imageMap data file.",
          "schema:additionalType": [
            "ada:EMPAImageMap"
          ],
          "schema:encodingFormat": [
            "image/tiff"
          ],
          "ada:componentType": "ada:EMPAImageMap",
          "ada:spectrometersUsed": "WDS",
          "ada:signalUsed": "Si Kα",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-minimal"
          }
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
    "@id": "ex:empaProfile-minimal-metadata-001",
    "schema:about": {
      "@id": "ex:empaProfile-minimal-001"
    },
    "schema:dateModified": "2026-05-01",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
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
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/empaProfile"
      }
    ]
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
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/profiles/geochemProfiles/empaProfile/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "csvw": "http://www.w3.org/ns/csvw#",
      "prov": "http://www.w3.org/ns/prov#",
      "spdx": "http://spdx.org/rdf/terms#",
      "nxs": "http://purl.org/nexusformat/definitions/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#",
      "ex": "https://example.org/"
    }
  ],
  "@id": "ex:empaProfile-minimal-001",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "Minimal empaProfile Example",
  "schema:description": "Smallest valid empaProfile dataset record. Demonstrates only the required adaProduct fields plus the empaProfile-specific empaTAPP measurement-technique reference and a single detailEMPA hasPart item.",
  "schema:additionalType": [
    "Electron Microprobe Analysis Image (EMPA)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.99999/empaprofile-minimal-001",
    "schema:url": "https://doi.org/10.99999/empaprofile-minimal-001"
  },
  "schema:dateModified": "2026-05-01",
  "schema:license": [
    "https://creativecommons.org/publicdomain/zero/1.0/"
  ],
  "schema:measurementTechnique": {
    "@id": "ex:empaTAPP-minimal"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-empa-min-001",
      "schema:startDate": "2026-05-01T09:00:00",
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
            "ex:instrument-empa-min-001"
          ]
        }
      ]
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "ex:empaProfile-minimal-var-001",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "SiO2_wt_pct",
      "schema:description": "Silicon dioxide concentration in weight percent.",
      "schema:unitText": "wt%",
      "cdi:role": "MeasureComponent"
    }
  ],
  "schema:distribution": [
    {
      "@type": [
        "schema:DataDownload"
      ],
      "schema:name": "empaProfile-minimal-archive.zip",
      "schema:description": "Single-file EMPA bundle for the minimal example.",
      "schema:contentUrl": "https://example.org/downloads/empaprofile-minimal-001.zip",
      "schema:encodingFormat": [
        "application/zip"
      ],
      "schema:hasPart": [
        {
          "@id": "ex:empaProfile-minimal-file-001",
          "@type": [
            "schema:MediaObject",
            "ada:imageMap",
            "schema:ImageObject"
          ],
          "schema:name": "minimal_EMPA_001.tif",
          "schema:description": "Minimal EMPA imageMap data file.",
          "schema:additionalType": [
            "ada:EMPAImageMap"
          ],
          "schema:encodingFormat": [
            "image/tiff"
          ],
          "ada:componentType": "ada:EMPAImageMap",
          "ada:spectrometersUsed": "WDS",
          "ada:signalUsed": "Si K\u03b1",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-minimal"
          }
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
    "@id": "ex:empaProfile-minimal-metadata-001",
    "schema:about": {
      "@id": "ex:empaProfile-minimal-001"
    },
    "schema:dateModified": "2026-05-01",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
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
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/empaProfile"
      }
    ]
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
@prefix schema1: <http://schema.org/> .

ex:empaProfile-minimal-001 a schema1:Dataset,
        schema1:Product ;
    schema1:additionalType "Electron Microprobe Analysis Image (EMPA)",
        "ada:DataDeliveryPackage" ;
    schema1:dateModified "2026-05-01" ;
    schema1:description "Smallest valid empaProfile dataset record. Demonstrates only the required adaProduct fields plus the empaProfile-specific empaTAPP measurement-technique reference and a single detailEMPA hasPart item." ;
    schema1:distribution [ a schema1:DataDownload ;
            schema1:contentUrl "https://example.org/downloads/empaprofile-minimal-001.zip" ;
            schema1:description "Single-file EMPA bundle for the minimal example." ;
            schema1:encodingFormat "application/zip" ;
            schema1:hasPart ex:empaProfile-minimal-file-001 ;
            schema1:name "empaProfile-minimal-archive.zip" ] ;
    schema1:identifier [ a schema1:PropertyValue ;
            schema1:propertyID "https://registry.identifiers.org/registry/doi" ;
            schema1:url "https://doi.org/10.99999/empaprofile-minimal-001" ;
            schema1:value "10.99999/empaprofile-minimal-001" ] ;
    schema1:license "https://creativecommons.org/publicdomain/zero/1.0/" ;
    schema1:measurementTechnique ex:empaTAPP-minimal ;
    schema1:name "Minimal empaProfile Example" ;
    schema1:subjectOf ex:empaProfile-minimal-metadata-001 ;
    schema1:variableMeasured ex:empaProfile-minimal-var-001 ;
    prov:wasGeneratedBy [ a schema1:Action,
                prov:Activity ;
            schema1:identifier "session-empa-min-001" ;
            schema1:startDate "2026-05-01T09:00:00" ;
            prov:used [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType "ada:EMPAInstrument",
                        "nxs:BaseClass/NXinstrument" ;
                    schema1:identifier "ex:instrument-empa-min-001" ;
                    schema1:name "Example EMPA Instrument" ] ] .

ex:empaProfile-minimal-file-001 a schema1:ImageObject,
        schema1:MediaObject,
        ada:imageMap ;
    schema1:additionalType "ada:EMPAImageMap" ;
    schema1:description "Minimal EMPA imageMap data file." ;
    schema1:encodingFormat "image/tiff" ;
    schema1:measurementTechnique ex:empaTAPP-minimal ;
    schema1:name "minimal_EMPA_001.tif" ;
    ada:componentType "ada:EMPAImageMap" ;
    ada:signalUsed "Si Kα" ;
    ada:spectrometersUsed "WDS" .

ex:empaProfile-minimal-metadata-001 a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.0>,
        <https://w3id.org/cdif/data_description/1.0>,
        <https://w3id.org/cdif/manifest/1.0>,
        <https://w3id.org/cdif/provenance/1.0>,
        <https://w3id.org/geochem/metadata/profiles/adaProduct>,
        <https://w3id.org/geochem/metadata/profiles/empaProfile> ;
    schema1:about ex:empaProfile-minimal-001 ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:dateModified "2026-05-01" .

ex:empaProfile-minimal-var-001 a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:role "MeasureComponent" ;
    schema1:description "Silicon dioxide concentration in weight percent." ;
    schema1:name "SiO2_wt_pct" ;
    schema1:unitText "wt%" .


```


### empaProfile full example — all properties and componentTypes
Full empaProfile dataset record exercising every adaProduct field, the
empaProfile-specific empaTAPP measurement-technique @id reference, and one
hasPart per EMPA-specific componentType (EMPAImageMap, EMPAImage,
EMPAQEATabular, EMPAImageCollection, EMPAESPCTabular, EMPAESPCPlot) plus a
methodDescription document. Mock data for validation and testing.
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
    "dcat": "http://www.w3.org/ns/dcat#",
    "ex": "https://example.org/"
  },
  "@id": "ex:empaProfile-example-001",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "EMPA Analysis of Synthetic Olivine Standard (full empaProfile example)",
  "schema:description": "Full empaProfile dataset record exercising every adaProduct field, the empaProfile-specific empaTAPP measurement-technique @id reference, and one hasPart per EMPA-specific componentType (EMPAImageMap, EMPAImage, EMPAQEATabular, EMPAImageCollection, EMPAESPCTabular, EMPAESPCPlot). Mock data for validation and testing.",
  "schema:additionalType": [
    "Electron Microprobe Analysis Image (EMPA)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.99999/empaprofile-example-001",
    "schema:url": "https://doi.org/10.99999/empaprofile-example-001"
  },
  "schema:url": "https://astromat.org/products/empaprofile-example-001",
  "schema:dateModified": "2026-05-01",
  "schema:version": "1.0",
  "schema:conditionsOfAccess": [
    "Unrestricted access for research purposes"
  ],
  "schema:license": [
    "https://creativecommons.org/publicdomain/zero/1.0/"
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
    "olivine",
    "synthetic standard",
    "WDS",
    "EDS"
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
    "@id": "ex:empaTAPP-example-001"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-empa-20260501-001",
      "schema:startDate": "2026-05-01T09:30:00",
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
          "schema:name": "JEOL JXA-8200 Electron Microprobe",
          "schema:identifier": [
            "ex:instrument-empa-jxa8200"
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
          "schema:name": "Synthetic Olivine Standard SOL-1",
          "schema:identifier": [
            "igsn:10.60471/GSEEXAMPLE002"
          ],
          "schema:description": "Synthetic forsteritic olivine reference material used as in-house calibration standard."
        }
      ]
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "ex:empaProfile-var-001",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "SiO2_wt_pct",
      "schema:alternateName": [
        "Silica concentration"
      ],
      "schema:description": "Silicon dioxide concentration measured by EMPA WDS, reported in weight percent.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/variables/sio2_wt_pct"
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
      "@id": "ex:empaProfile-var-002",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "MgO_wt_pct",
      "schema:description": "Magnesium oxide concentration measured by EMPA WDS, reported in weight percent.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/variables/mgo_wt_pct"
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
      "@id": "ex:empaProfile-var-003",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "FeO_wt_pct",
      "schema:description": "Iron(II) oxide concentration measured by EMPA WDS, reported in weight percent.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/variables/feo_wt_pct"
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
      "@id": "ex:empaProfile-var-004",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "position_x",
      "schema:description": "Horizontal position coordinate on sample surface for spot analyses.",
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
      "schema:name": "empaProfile-SOL1-bundle.zip",
      "schema:description": "Archive containing all six EMPA componentType files plus method documentation.",
      "schema:contentUrl": "https://astromat.org/downloads/empaprofile-example-001.zip",
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
        "schema:value": 31457280,
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
          "@id": "ex:empaProfile-file-imageMap",
          "@type": [
            "schema:MediaObject",
            "ada:imageMap",
            "schema:ImageObject"
          ],
          "schema:name": "SOL1_EMPA_imageMap.tif",
          "schema:description": "EMPA WDS X-ray image map showing element distribution across SOL-1 thin section.",
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
          "ada:componentType": "ada:EMPAImageMap",
          "ada:spectrometersUsed": "WDS-1, WDS-2, WDS-3, WDS-4, WDS-5",
          "ada:signalUsed": "Si Kα, Mg Kα, Fe Kα, Ca Kα, Al Kα",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-example-001"
          }
        },
        {
          "@id": "ex:empaProfile-file-image",
          "@type": [
            "schema:MediaObject",
            "ada:image",
            "schema:ImageObject"
          ],
          "schema:name": "SOL1_EMPA_BSE.tif",
          "schema:description": "Backscattered electron image of SOL-1 thin section providing spatial context for spot analyses.",
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
            "schema:value": 5242880,
            "schema:unitText": "byte"
          },
          "ada:componentType": "ada:EMPAImage",
          "ada:spectrometersUsed": "BSE detector",
          "ada:signalUsed": "Backscattered electrons",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-example-001"
          }
        },
        {
          "@id": "ex:empaProfile-file-qea",
          "@type": [
            "schema:MediaObject",
            "cdi:TabularTextDataSet",
            "ada:tabularData"
          ],
          "schema:name": "SOL1_EMPA_QEA.csv",
          "schema:description": "Quantitative element analysis (QEA) results table — one row per analytical spot, columns per measured oxide.",
          "schema:additionalType": [
            "ada:EMPAQEATabular"
          ],
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
          "cdi:isDelimited": true,
          "ada:componentType": "ada:EMPAQEATabular",
          "ada:spectrometersUsed": "WDS-1 through WDS-5",
          "ada:signalUsed": "Characteristic X-rays for major elements",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-example-001"
          },
          "cdif:hasPhysicalMapping": [
            {
              "cdif:index": 0,
              "cdif:physicalDataType": "String",
              "cdi:nullSequence": "NA"
            }
          ]
        },
        {
          "@id": "ex:empaProfile-file-collection",
          "@type": [
            "schema:MediaObject",
            "ada:collection",
            "https://schema.org/Collection"
          ],
          "schema:name": "SOL1_EMPA_imagecollection",
          "schema:description": "Multi-element image collection grouping the per-element WDS X-ray maps.",
          "schema:additionalType": [
            "ada:EMPAImageCollection"
          ],
          "schema:encodingFormat": [
            "application/zip"
          ],
          "ada:componentType": "ada:EMPAImageCollection",
          "ada:spectrometersUsed": "WDS-1 through WDS-5",
          "ada:signalUsed": "Per-element X-ray characteristic lines",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-example-001"
          }
        },
        {
          "@id": "ex:empaProfile-file-espcTabular",
          "@type": [
            "schema:MediaObject",
            "cdi:TabularTextDataSet",
            "ada:tabularData"
          ],
          "schema:name": "SOL1_EMPA_ESPC.csv",
          "schema:description": "Energy-dispersive spectrometer count tabular output — wavelength/energy bins by intensity.",
          "schema:additionalType": [
            "ada:EMPAESPCTabular"
          ],
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
          "cdi:isDelimited": true,
          "ada:componentType": "ada:EMPAESPCTabular",
          "ada:spectrometersUsed": "EDS",
          "ada:signalUsed": "Continuous EDS spectrum (0–20 keV)",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-example-001"
          },
          "cdif:hasPhysicalMapping": [
            {
              "cdif:index": 0,
              "cdif:physicalDataType": "String",
              "cdi:nullSequence": "NA"
            }
          ]
        },
        {
          "@id": "ex:empaProfile-file-espcPlot",
          "@type": [
            "schema:MediaObject",
            "ada:image",
            "schema:ImageObject"
          ],
          "schema:name": "SOL1_EMPA_ESPC_plot.png",
          "schema:description": "Rendered EDS spectrum plot for visual inspection.",
          "schema:additionalType": [
            "ada:EMPAESPCPlot"
          ],
          "schema:encodingFormat": [
            "image/png"
          ],
          "ada:componentType": "ada:EMPAESPCPlot",
          "ada:spectrometersUsed": "EDS",
          "ada:signalUsed": "Continuous EDS spectrum (0–20 keV)",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-example-001"
          }
        },
        {
          "@id": "ex:empaProfile-file-methodDoc",
          "@type": [
            "schema:MediaObject",
            "ada:document",
            "schema:DigitalDocument"
          ],
          "schema:name": "SOL1_EMPA_methods.pdf",
          "schema:description": "Method description document covering instrument settings, calibration standards, and data reduction.",
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
    "@id": "ex:empaProfile-example-metadata-001",
    "schema:about": {
      "@id": "ex:empaProfile-example-001"
    },
    "schema:dateModified": "2026-05-01",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
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
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/empaProfile"
      }
    ],
    "schema:maintainer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Astromat Data Archive"
    },
    "schema:sdDatePublished": "2026-05-01T12:00:00Z",
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
      "csvw": "http://www.w3.org/ns/csvw#",
      "prov": "http://www.w3.org/ns/prov#",
      "spdx": "http://spdx.org/rdf/terms#",
      "nxs": "http://purl.org/nexusformat/definitions/",
      "dcterms": "http://purl.org/dc/terms/",
      "dcat": "http://www.w3.org/ns/dcat#"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/profiles/geochemProfiles/empaProfile/context.jsonld",
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
      "dcat": "http://www.w3.org/ns/dcat#",
      "ex": "https://example.org/"
    }
  ],
  "@id": "ex:empaProfile-example-001",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:name": "EMPA Analysis of Synthetic Olivine Standard (full empaProfile example)",
  "schema:description": "Full empaProfile dataset record exercising every adaProduct field, the empaProfile-specific empaTAPP measurement-technique @id reference, and one hasPart per EMPA-specific componentType (EMPAImageMap, EMPAImage, EMPAQEATabular, EMPAImageCollection, EMPAESPCTabular, EMPAESPCPlot). Mock data for validation and testing.",
  "schema:additionalType": [
    "Electron Microprobe Analysis Image (EMPA)",
    "ada:DataDeliveryPackage"
  ],
  "schema:identifier": {
    "@type": [
      "schema:PropertyValue"
    ],
    "schema:propertyID": "https://registry.identifiers.org/registry/doi",
    "schema:value": "10.99999/empaprofile-example-001",
    "schema:url": "https://doi.org/10.99999/empaprofile-example-001"
  },
  "schema:url": "https://astromat.org/products/empaprofile-example-001",
  "schema:dateModified": "2026-05-01",
  "schema:version": "1.0",
  "schema:conditionsOfAccess": [
    "Unrestricted access for research purposes"
  ],
  "schema:license": [
    "https://creativecommons.org/publicdomain/zero/1.0/"
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
    "olivine",
    "synthetic standard",
    "WDS",
    "EDS"
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
    "@id": "ex:empaTAPP-example-001"
  },
  "prov:wasGeneratedBy": [
    {
      "@type": [
        "prov:Activity",
        "schema:Action"
      ],
      "schema:identifier": "session-empa-20260501-001",
      "schema:startDate": "2026-05-01T09:30:00",
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
          "schema:name": "JEOL JXA-8200 Electron Microprobe",
          "schema:identifier": [
            "ex:instrument-empa-jxa8200"
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
          "schema:name": "Synthetic Olivine Standard SOL-1",
          "schema:identifier": [
            "igsn:10.60471/GSEEXAMPLE002"
          ],
          "schema:description": "Synthetic forsteritic olivine reference material used as in-house calibration standard."
        }
      ]
    }
  ],
  "schema:variableMeasured": [
    {
      "@id": "ex:empaProfile-var-001",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "SiO2_wt_pct",
      "schema:alternateName": [
        "Silica concentration"
      ],
      "schema:description": "Silicon dioxide concentration measured by EMPA WDS, reported in weight percent.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/variables/sio2_wt_pct"
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
      "@id": "ex:empaProfile-var-002",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "MgO_wt_pct",
      "schema:description": "Magnesium oxide concentration measured by EMPA WDS, reported in weight percent.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/variables/mgo_wt_pct"
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
      "@id": "ex:empaProfile-var-003",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "FeO_wt_pct",
      "schema:description": "Iron(II) oxide concentration measured by EMPA WDS, reported in weight percent.",
      "schema:propertyID": [
        "https://ada.astromat.org/vocabulary/variables/feo_wt_pct"
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
      "@id": "ex:empaProfile-var-004",
      "@type": [
        "schema:PropertyValue",
        "cdi:InstanceVariable"
      ],
      "schema:name": "position_x",
      "schema:description": "Horizontal position coordinate on sample surface for spot analyses.",
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
      "schema:name": "empaProfile-SOL1-bundle.zip",
      "schema:description": "Archive containing all six EMPA componentType files plus method documentation.",
      "schema:contentUrl": "https://astromat.org/downloads/empaprofile-example-001.zip",
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
        "schema:value": 31457280,
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
          "@id": "ex:empaProfile-file-imageMap",
          "@type": [
            "schema:MediaObject",
            "ada:imageMap",
            "schema:ImageObject"
          ],
          "schema:name": "SOL1_EMPA_imageMap.tif",
          "schema:description": "EMPA WDS X-ray image map showing element distribution across SOL-1 thin section.",
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
          "ada:componentType": "ada:EMPAImageMap",
          "ada:spectrometersUsed": "WDS-1, WDS-2, WDS-3, WDS-4, WDS-5",
          "ada:signalUsed": "Si K\u03b1, Mg K\u03b1, Fe K\u03b1, Ca K\u03b1, Al K\u03b1",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-example-001"
          }
        },
        {
          "@id": "ex:empaProfile-file-image",
          "@type": [
            "schema:MediaObject",
            "ada:image",
            "schema:ImageObject"
          ],
          "schema:name": "SOL1_EMPA_BSE.tif",
          "schema:description": "Backscattered electron image of SOL-1 thin section providing spatial context for spot analyses.",
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
            "schema:value": 5242880,
            "schema:unitText": "byte"
          },
          "ada:componentType": "ada:EMPAImage",
          "ada:spectrometersUsed": "BSE detector",
          "ada:signalUsed": "Backscattered electrons",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-example-001"
          }
        },
        {
          "@id": "ex:empaProfile-file-qea",
          "@type": [
            "schema:MediaObject",
            "cdi:TabularTextDataSet",
            "ada:tabularData"
          ],
          "schema:name": "SOL1_EMPA_QEA.csv",
          "schema:description": "Quantitative element analysis (QEA) results table \u2014 one row per analytical spot, columns per measured oxide.",
          "schema:additionalType": [
            "ada:EMPAQEATabular"
          ],
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
          "cdi:isDelimited": true,
          "ada:componentType": "ada:EMPAQEATabular",
          "ada:spectrometersUsed": "WDS-1 through WDS-5",
          "ada:signalUsed": "Characteristic X-rays for major elements",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-example-001"
          },
          "cdif:hasPhysicalMapping": [
            {
              "cdif:index": 0,
              "cdif:physicalDataType": "String",
              "cdi:nullSequence": "NA"
            }
          ]
        },
        {
          "@id": "ex:empaProfile-file-collection",
          "@type": [
            "schema:MediaObject",
            "ada:collection",
            "https://schema.org/Collection"
          ],
          "schema:name": "SOL1_EMPA_imagecollection",
          "schema:description": "Multi-element image collection grouping the per-element WDS X-ray maps.",
          "schema:additionalType": [
            "ada:EMPAImageCollection"
          ],
          "schema:encodingFormat": [
            "application/zip"
          ],
          "ada:componentType": "ada:EMPAImageCollection",
          "ada:spectrometersUsed": "WDS-1 through WDS-5",
          "ada:signalUsed": "Per-element X-ray characteristic lines",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-example-001"
          }
        },
        {
          "@id": "ex:empaProfile-file-espcTabular",
          "@type": [
            "schema:MediaObject",
            "cdi:TabularTextDataSet",
            "ada:tabularData"
          ],
          "schema:name": "SOL1_EMPA_ESPC.csv",
          "schema:description": "Energy-dispersive spectrometer count tabular output \u2014 wavelength/energy bins by intensity.",
          "schema:additionalType": [
            "ada:EMPAESPCTabular"
          ],
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
          "cdi:isDelimited": true,
          "ada:componentType": "ada:EMPAESPCTabular",
          "ada:spectrometersUsed": "EDS",
          "ada:signalUsed": "Continuous EDS spectrum (0\u201320 keV)",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-example-001"
          },
          "cdif:hasPhysicalMapping": [
            {
              "cdif:index": 0,
              "cdif:physicalDataType": "String",
              "cdi:nullSequence": "NA"
            }
          ]
        },
        {
          "@id": "ex:empaProfile-file-espcPlot",
          "@type": [
            "schema:MediaObject",
            "ada:image",
            "schema:ImageObject"
          ],
          "schema:name": "SOL1_EMPA_ESPC_plot.png",
          "schema:description": "Rendered EDS spectrum plot for visual inspection.",
          "schema:additionalType": [
            "ada:EMPAESPCPlot"
          ],
          "schema:encodingFormat": [
            "image/png"
          ],
          "ada:componentType": "ada:EMPAESPCPlot",
          "ada:spectrometersUsed": "EDS",
          "ada:signalUsed": "Continuous EDS spectrum (0\u201320 keV)",
          "schema:measurementTechnique": {
            "@id": "ex:empaTAPP-example-001"
          }
        },
        {
          "@id": "ex:empaProfile-file-methodDoc",
          "@type": [
            "schema:MediaObject",
            "ada:document",
            "schema:DigitalDocument"
          ],
          "schema:name": "SOL1_EMPA_methods.pdf",
          "schema:description": "Method description document covering instrument settings, calibration standards, and data reduction.",
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
    "@id": "ex:empaProfile-example-metadata-001",
    "schema:about": {
      "@id": "ex:empaProfile-example-001"
    },
    "schema:dateModified": "2026-05-01",
    "dcterms:conformsTo": [
      {
        "@id": "https://w3id.org/cdif/core/1.0"
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
      },
      {
        "@id": "https://w3id.org/geochem/metadata/profiles/empaProfile"
      }
    ],
    "schema:maintainer": {
      "@type": [
        "schema:Organization"
      ],
      "schema:name": "Astromat Data Archive"
    },
    "schema:sdDatePublished": "2026-05-01T12:00:00Z",
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

ex:empaProfile-example-001 a schema1:Dataset,
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
    schema1:dateModified "2026-05-01" ;
    schema1:description "Full empaProfile dataset record exercising every adaProduct field, the empaProfile-specific empaTAPP measurement-technique @id reference, and one hasPart per EMPA-specific componentType (EMPAImageMap, EMPAImage, EMPAQEATabular, EMPAImageCollection, EMPAESPCTabular, EMPAESPCPlot). Mock data for validation and testing." ;
    schema1:distribution [ a schema1:DataDownload ;
            schema1:contentUrl "https://astromat.org/downloads/empaprofile-example-001.zip" ;
            schema1:description "Archive containing all six EMPA componentType files plus method documentation." ;
            schema1:encodingFormat "application/zip" ;
            schema1:hasPart ex:empaProfile-file-collection,
                ex:empaProfile-file-espcPlot,
                ex:empaProfile-file-espcTabular,
                ex:empaProfile-file-image,
                ex:empaProfile-file-imageMap,
                ex:empaProfile-file-methodDoc,
                ex:empaProfile-file-qea ;
            schema1:name "empaProfile-SOL1-bundle.zip" ;
            schema1:provider [ a schema1:Organization ;
                    schema1:name "Astromat Data Archive" ] ;
            schema1:size [ a schema1:QuantitativeValue ;
                    schema1:unitText "byte" ;
                    schema1:value 31457280 ] ;
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
            schema1:url "https://doi.org/10.99999/empaprofile-example-001" ;
            schema1:value "10.99999/empaprofile-example-001" ] ;
    schema1:keywords [ a schema1:DefinedTerm ;
            schema1:identifier "https://ada.astromat.org/vocabulary/techniques/EMPA" ;
            schema1:inDefinedTermSet "https://ada.astromat.org/vocabulary/techniques" ;
            schema1:name "Electron Microprobe Analysis" ;
            schema1:termCode "EMPA" ],
        "EDS",
        "WDS",
        "olivine",
        "synthetic standard" ;
    schema1:license "https://creativecommons.org/publicdomain/zero/1.0/" ;
    schema1:measurementTechnique ex:empaTAPP-example-001 ;
    schema1:name "EMPA Analysis of Synthetic Olivine Standard (full empaProfile example)" ;
    schema1:subjectOf ex:empaProfile-example-metadata-001 ;
    schema1:url "https://astromat.org/products/empaprofile-example-001" ;
    schema1:variableMeasured ex:empaProfile-var-001,
        ex:empaProfile-var-002,
        ex:empaProfile-var-003,
        ex:empaProfile-var-004 ;
    schema1:version "1.0" ;
    prov:wasGeneratedBy [ a schema1:Action,
                prov:Activity ;
            schema1:identifier "session-empa-20260501-001" ;
            schema1:location [ a schema1:Place ;
                    schema1:additionalType "nxs:BaseClass/NXsource" ;
                    schema1:identifier "https://ror.org/00hx57361" ;
                    schema1:name "Analytical Sciences Laboratory" ] ;
            schema1:object [ a schema1:Thing,
                        <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:additionalType "MaterialSample" ;
                    schema1:description "Synthetic forsteritic olivine reference material used as in-house calibration standard." ;
                    schema1:identifier "igsn:10.60471/GSEEXAMPLE002" ;
                    schema1:name "Synthetic Olivine Standard SOL-1" ] ;
            schema1:startDate "2026-05-01T09:30:00" ;
            prov:used [ a schema1:Product,
                        schema1:Thing ;
                    schema1:additionalType "ada:EMPAInstrument",
                        "nxs:BaseClass/NXinstrument" ;
                    schema1:identifier "ex:instrument-empa-jxa8200" ;
                    schema1:name "JEOL JXA-8200 Electron Microprobe" ] ] .

ex:empaProfile-example-metadata-001 a schema1:Dataset ;
    dcterms:conformsTo <https://w3id.org/cdif/core/1.0>,
        <https://w3id.org/cdif/data_description/1.0>,
        <https://w3id.org/cdif/manifest/1.0>,
        <https://w3id.org/cdif/provenance/1.0>,
        <https://w3id.org/geochem/metadata/profiles/adaProduct>,
        <https://w3id.org/geochem/metadata/profiles/empaProfile> ;
    schema1:about ex:empaProfile-example-001 ;
    schema1:additionalType "dcat:CatalogRecord" ;
    schema1:dateModified "2026-05-01" ;
    schema1:includedInDataCatalog [ a schema1:DataCatalog ;
            schema1:name "Astromat Data Archive" ;
            schema1:url "https://astromat.org" ] ;
    schema1:maintainer [ a schema1:Organization ;
            schema1:name "Astromat Data Archive" ] ;
    schema1:sdDatePublished "2026-05-01T12:00:00Z" .

ex:empaProfile-file-collection a schema1:MediaObject,
        ada:collection,
        schema:Collection ;
    schema1:additionalType "ada:EMPAImageCollection" ;
    schema1:description "Multi-element image collection grouping the per-element WDS X-ray maps." ;
    schema1:encodingFormat "application/zip" ;
    schema1:measurementTechnique ex:empaTAPP-example-001 ;
    schema1:name "SOL1_EMPA_imagecollection" ;
    ada:componentType "ada:EMPAImageCollection" ;
    ada:signalUsed "Per-element X-ray characteristic lines" ;
    ada:spectrometersUsed "WDS-1 through WDS-5" .

ex:empaProfile-file-espcPlot a schema1:ImageObject,
        schema1:MediaObject,
        ada:image ;
    schema1:additionalType "ada:EMPAESPCPlot" ;
    schema1:description "Rendered EDS spectrum plot for visual inspection." ;
    schema1:encodingFormat "image/png" ;
    schema1:measurementTechnique ex:empaTAPP-example-001 ;
    schema1:name "SOL1_EMPA_ESPC_plot.png" ;
    ada:componentType "ada:EMPAESPCPlot" ;
    ada:signalUsed "Continuous EDS spectrum (0–20 keV)" ;
    ada:spectrometersUsed "EDS" .

ex:empaProfile-file-espcTabular a cdi:TabularTextDataSet,
        schema1:MediaObject,
        ada:tabularData ;
    cdi:isDelimited true ;
    schema1:additionalType "ada:EMPAESPCTabular" ;
    schema1:description "Energy-dispersive spectrometer count tabular output — wavelength/energy bins by intensity." ;
    schema1:encodingFormat "text/csv" ;
    schema1:measurementTechnique ex:empaTAPP-example-001 ;
    schema1:name "SOL1_EMPA_ESPC.csv" ;
    schema1:size [ a schema1:QuantitativeValue ;
            schema1:unitText "byte" ;
            schema1:value 16384 ] ;
    ada:componentType "ada:EMPAESPCTabular" ;
    ada:signalUsed "Continuous EDS spectrum (0–20 keV)" ;
    ada:spectrometersUsed "EDS" ;
    cdif:hasPhysicalMapping [ cdi:nullSequence "NA" ;
            cdif:index 0 ;
            cdif:physicalDataType "String" ] .

ex:empaProfile-file-image a schema1:ImageObject,
        schema1:MediaObject,
        ada:image ;
    schema1:additionalType "ada:EMPAImage" ;
    schema1:description "Backscattered electron image of SOL-1 thin section providing spatial context for spot analyses." ;
    schema1:encodingFormat "image/tiff" ;
    schema1:measurementTechnique ex:empaTAPP-example-001 ;
    schema1:name "SOL1_EMPA_BSE.tif" ;
    schema1:size [ a schema1:QuantitativeValue ;
            schema1:unitText "byte" ;
            schema1:value 5242880 ] ;
    ada:componentType "ada:EMPAImage" ;
    ada:signalUsed "Backscattered electrons" ;
    ada:spectrometersUsed "BSE detector" .

ex:empaProfile-file-imageMap a schema1:ImageObject,
        schema1:MediaObject,
        ada:imageMap ;
    schema1:additionalType "ada:EMPAImageMap" ;
    schema1:description "EMPA WDS X-ray image map showing element distribution across SOL-1 thin section." ;
    schema1:encodingFormat "image/tiff" ;
    schema1:measurementTechnique ex:empaTAPP-example-001 ;
    schema1:name "SOL1_EMPA_imageMap.tif" ;
    schema1:size [ a schema1:QuantitativeValue ;
            schema1:unitText "byte" ;
            schema1:value 10485760 ] ;
    spdx:checksum [ a spdx:Checksum ;
            spdx:algorithm "MD5" ;
            spdx:checksumValue "d41d8cd98f00b204e9800998ecf8427e" ] ;
    ada:componentType "ada:EMPAImageMap" ;
    ada:signalUsed "Si Kα, Mg Kα, Fe Kα, Ca Kα, Al Kα" ;
    ada:spectrometersUsed "WDS-1, WDS-2, WDS-3, WDS-4, WDS-5" .

ex:empaProfile-file-methodDoc a schema1:DigitalDocument,
        schema1:MediaObject,
        ada:document ;
    schema1:additionalType "ada:methodDescription" ;
    schema1:description "Method description document covering instrument settings, calibration standards, and data reduction." ;
    schema1:encodingFormat "application/pdf" ;
    schema1:name "SOL1_EMPA_methods.pdf" ;
    schema1:size [ a schema1:QuantitativeValue ;
            schema1:unitText "byte" ;
            schema1:value 524288 ] ;
    ada:componentType "ada:methodDescription" .

ex:empaProfile-file-qea a cdi:TabularTextDataSet,
        schema1:MediaObject,
        ada:tabularData ;
    cdi:isDelimited true ;
    schema1:additionalType "ada:EMPAQEATabular" ;
    schema1:description "Quantitative element analysis (QEA) results table — one row per analytical spot, columns per measured oxide." ;
    schema1:encodingFormat "text/csv" ;
    schema1:measurementTechnique ex:empaTAPP-example-001 ;
    schema1:name "SOL1_EMPA_QEA.csv" ;
    schema1:size [ a schema1:QuantitativeValue ;
            schema1:unitText "byte" ;
            schema1:value 32768 ] ;
    ada:componentType "ada:EMPAQEATabular" ;
    ada:signalUsed "Characteristic X-rays for major elements" ;
    ada:spectrometersUsed "WDS-1 through WDS-5" ;
    cdif:hasPhysicalMapping [ cdi:nullSequence "NA" ;
            cdif:index 0 ;
            cdif:physicalDataType "String" ] .

ex:empaProfile-var-001 a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:alternateName "Silica concentration" ;
    schema1:description "Silicon dioxide concentration measured by EMPA WDS, reported in weight percent." ;
    schema1:name "SiO2_wt_pct" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/variables/sio2_wt_pct" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:empaProfile-var-002 a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Magnesium oxide concentration measured by EMPA WDS, reported in weight percent." ;
    schema1:name "MgO_wt_pct" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/variables/mgo_wt_pct" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:empaProfile-var-003 a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "MeasureComponent" ;
    cdi:simpleUnitOfMeasure "wt%" ;
    schema1:description "Iron(II) oxide concentration measured by EMPA WDS, reported in weight percent." ;
    schema1:name "FeO_wt_pct" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/variables/feo_wt_pct" ;
    schema1:unitText "wt%" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#double" .

ex:empaProfile-var-004 a cdi:InstanceVariable,
        schema1:PropertyValue ;
    cdi:intendedDataType "https://www.w3.org/TR/xmlschema-2/#decimal" ;
    cdi:role "DimensionComponent" ;
    cdi:simpleUnitOfMeasure "um" ;
    schema1:description "Horizontal position coordinate on sample surface for spot analyses." ;
    schema1:name "position_x" ;
    schema1:propertyID "https://ada.astromat.org/vocabulary/variables/position_x" ;
    schema1:unitText "micrometer" ;
    cdif:physicalDataType "https://www.w3.org/TR/xmlschema-2/#float" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: EMPA Geochem Profile
description: Geochem dataset profile for EMPA. Extends adaProduct with a detailEMPA
  detail block and a schema:measurementTechnique that points at a empaTAPP TAPP definition.
allOf:
- $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/profiles/adaProfiles/adaProduct/schema.yaml
- type: object
  properties:
    schema:measurementTechnique:
      description: TAPP definition reference or inline.
      anyOf:
      - type: object
        properties:
          '@id':
            type: string
            format: uri
        required:
        - '@id'
      - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/empaTAPP/schema.yaml
    schema:distribution:
      type: array
      items:
        type: object
        properties:
          schema:hasPart:
            items:
              anyOf:
              - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/profiles/adaProfiles/adaProduct/schema.yaml#/$defs/universalComponentTypeBranch
              - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/analysisSpecificDetails/detailEMPA/schema.yaml

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/profiles/geochemProfiles/empaProfile/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/profiles/geochemProfiles/empaProfile/schema.yaml)


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
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/profiles/geochemProfiles/empaProfile/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/profiles/geochemProfiles/empaProfile`

