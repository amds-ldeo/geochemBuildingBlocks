
# Structured Data File Type (Schema)

`ogch.BaseSchema.structuredData` *v0.1*

A container/array data file (HDF5, NeXus) in an ADA bundle whose layout is described by a CDIF DataStructure via cdi:isStructuredBy. The bundle-part analog of the monolithic single-file isStructuredBy pattern (pattern chosen by encoding, not position). Defines properties: @type, ada:componentType, cdi:isStructuredBy. Uses building blocks: cdifDataStructure (cdifProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Structured Data File Type

Describes a container/array data file (e.g. HDF5, NeXus) that is a member of an ADA
product bundle (`schema:distribution.hasPart`) and whose internal layout is described
by a CDIF DataStructure via `cdi:isStructuredBy`. Typed as `ada:structuredData` and
`cdi:PhysicalDataSet`.

This is the **bundle-part analog of the monolithic single-file `cdi:isStructuredBy`
pattern**: the structure-description pattern is chosen by the file's *encoding*, not by
its position in the distribution.

- **Tabular text** files (CSV, fixed-width) use `tabularData` — CSVW/DDI-CDI layout plus
  per-column `cdif:hasPhysicalMapping`.
- **Container/array** files (HDF5, NeXus) use `structuredData` — a `cdi:DataStructure`
  (Dimensional / Long / Wide / DataStructure) attached with `cdi:isStructuredBy`, whose
  components carry their own physical mappings (LocatorMapping).

The structure may be stated inline, or referenced by `@id` from a structure declared once
and shared across several parts of the same layout.

## Examples

### Structured Data File Type Example
An HDF5 container part in an ADA bundle whose layout is described by a CDIF
DimensionalDataStructure via cdi:isStructuredBy (chosen because the file is a
container, not tabular text).
#### json
```json
{
  "@id": "ex:file-map-cube-001",
  "@type": ["schema:MediaObject", "ada:structuredData", "cdi:PhysicalDataSet"],
  "schema:name": "elemental_map_cube.h5",
  "schema:encodingFormat": ["application/x-hdf5"],
  "ada:componentType": "ada:other",
  "cdi:isStructuredBy": {
    "@id": "ex:struct-map-cube-001",
    "@type": ["cdi:DimensionalDataStructure"],
    "schema:name": "Elemental map cube structure",
    "cdi:has_DataStructureComponent": [
      {"@type": ["cdi:MeasureComponent"], "cdif:name": ["intensity"]},
      {"@type": ["cdi:DimensionComponent"], "cdif:name": ["x"]},
      {"@type": ["cdi:DimensionComponent"], "cdif:name": ["y"]}
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
      "cdif": "https://cdif.org/0.1/"
    },
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/BaseSchema/structuredData/context.jsonld"
  ],
  "@id": "ex:file-map-cube-001",
  "@type": [
    "schema:MediaObject",
    "ada:structuredData",
    "cdi:PhysicalDataSet"
  ],
  "schema:name": "elemental_map_cube.h5",
  "schema:encodingFormat": [
    "application/x-hdf5"
  ],
  "ada:componentType": "ada:other",
  "cdi:isStructuredBy": {
    "@id": "ex:struct-map-cube-001",
    "@type": [
      "cdi:DimensionalDataStructure"
    ],
    "schema:name": "Elemental map cube structure",
    "cdi:has_DataStructureComponent": [
      {
        "@type": [
          "cdi:MeasureComponent"
        ],
        "cdif:name": [
          "intensity"
        ]
      },
      {
        "@type": [
          "cdi:DimensionComponent"
        ],
        "cdif:name": [
          "x"
        ]
      },
      {
        "@type": [
          "cdi:DimensionComponent"
        ],
        "cdif:name": [
          "y"
        ]
      }
    ]
  }
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix cdif: <https://cdif.org/0.1/> .
@prefix schema1: <http://schema.org/> .

<ex:file-map-cube-001> a cdi:PhysicalDataSet,
        schema1:MediaObject,
        ada:structuredData ;
    cdi:isStructuredBy <ex:struct-map-cube-001> ;
    schema1:encodingFormat "application/x-hdf5" ;
    schema1:name "elemental_map_cube.h5" ;
    ada:componentType "ada:other" .

<ex:struct-map-cube-001> a cdi:DimensionalDataStructure ;
    cdi:has_DataStructureComponent [ a cdi:DimensionComponent ;
            cdif:name "y" ],
        [ a cdi:DimensionComponent ;
            cdif:name "x" ],
        [ a cdi:MeasureComponent ;
            cdif:name "intensity" ] ;
    schema1:name "Elemental map cube structure" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Structured Data File Type
description: 'A container/array data file (e.g. HDF5, NeXus) within an ADA bundle
  whose layout is described by a CDIF DataStructure via cdi:isStructuredBy, rather
  than the flat CSVW layout + per-column cdif:hasPhysicalMapping of a tabular text
  file (tabularData) or the locator mappings of a dataCube. This is the bundle-part
  analog of the monolithic single-file cdi:isStructuredBy pattern: the pattern is
  chosen by the file''s encoding, not its position. Typed as ada:structuredData and
  cdi:PhysicalDataSet.'
type: object
properties:
  '@type':
    type: array
    items:
      type: string
    minItems: 2
    allOf:
    - contains:
        const: ada:structuredData
    - contains:
        const: cdi:PhysicalDataSet
  ada:componentType:
    type: string
    description: ADA componentType for a structured container file, as a single string.
      Allowed values are constrained at the technique-profile level.
    x-jsonld-id: https://ada.astromat.org/metadata/componentType
  cdi:isStructuredBy:
    description: "The data structure of this container file \u2014 one of the four
      CDIF DataStructure variants (DataStructure, Dimensional, Long, Wide) inline,
      or an @id reference to a structure declared elsewhere in the document (e.g.
      shared across parts)."
    anyOf:
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifDataStructure/schema.yaml#/$defs/DataStructure
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifDataStructure/schema.yaml#/$defs/DimensionalDataStructure
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifDataStructure/schema.yaml#/$defs/LongDataStructure
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/profiles/cdifProfile/cdifDataStructure/schema.yaml#/$defs/WideDataStructure
    - $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/cdifDataType/objectReference/schema.yaml
    x-jsonld-id: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/isStructuredBy
required:
- '@type'
- ada:componentType
- cdi:isStructuredBy
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/
  cdi: http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/
  cdif: https://cdif.org/0.1/

```

Links to the schema:

* YAML version: [schema.yaml](https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/BaseSchema/structuredData/schema.json)
* JSON version: [schema.json](https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/BaseSchema/structuredData/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://cdif.org/0.1/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/BaseSchema/structuredData/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/BaseSchema/structuredData`

