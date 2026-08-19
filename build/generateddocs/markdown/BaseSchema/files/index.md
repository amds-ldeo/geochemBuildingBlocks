
# Files Type (Schema)

`ogch.BaseSchema.files` *v0.1*

DataDownload with checksum, size, encoding format, and file detail. Defines properties: schema:additionalType, schema:description, schema:size, resultTarget, schema:relatedLink. Uses building blocks: dataDownload (schemaorgProperties), stringArray (geochemProperties), image (geochemProperties), imageMap (geochemProperties), tabularData (geochemProperties), collection (geochemProperties), dataCube (geochemProperties), document (geochemProperties), supDocImage (geochemProperties), otherFile (geochemProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Files Type

Describes properties for any file in an ADA product. Includes file metadata (name, description, checksum, size, encoding format), file detail classification (image, imageMap, tabularData, collection, dataCube, document, supDocImage, otherFile, or Metadata), and inter-file relationships via `schema:relatedLink`.

## Examples

### Files Type Example
An ADA product file (component within an archive) with size, encoding format,
and a link to its metadata sidecar. Files in hasPart are NOT individually
downloadable, so @type must not include schema:DataDownload and there is
no schema:contentUrl.
#### json
```json
{
  "@type": ["ada:image", "schema:MediaObject"],
  "schema:name": "ALH84001_BSE_001.tif",
  "schema:encodingFormat": ["image/tiff"],
  "schema:description": "Backscattered electron image of ALH84001 thin section",
  "schema:size": {
    "@type": ["schema:QuantitativeValue"],
    "schema:value": 4521984,
    "schema:unitText": "byte"
  },
  "schema:additionalType": ["ada:BSEImage"],
  "ada:componentType": {
    "@type": ["ada:BSEImage"]
  },
  "schema:relatedLink": [
    {
      "@type": ["schema:LinkRole"],
      "schema:linkRelationship": "metadata",
      "schema:target": {
        "@type": ["schema:EntryPoint"],
        "schema:encodingFormat": "application/json",
        "schema:name": "ALH84001_BSE_001_metadata.json"
      }
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/BaseSchema/files/context.jsonld"
  ],
  "@type": [
    "ada:image",
    "schema:MediaObject"
  ],
  "schema:name": "ALH84001_BSE_001.tif",
  "schema:encodingFormat": [
    "image/tiff"
  ],
  "schema:description": "Backscattered electron image of ALH84001 thin section",
  "schema:size": {
    "@type": [
      "schema:QuantitativeValue"
    ],
    "schema:value": 4521984,
    "schema:unitText": "byte"
  },
  "schema:additionalType": [
    "ada:BSEImage"
  ],
  "ada:componentType": {
    "@type": [
      "ada:BSEImage"
    ]
  },
  "schema:relatedLink": [
    {
      "@type": [
        "schema:LinkRole"
      ],
      "schema:linkRelationship": "metadata",
      "schema:target": {
        "@type": [
          "schema:EntryPoint"
        ],
        "schema:encodingFormat": "application/json",
        "schema:name": "ALH84001_BSE_001_metadata.json"
      }
    }
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] a schema1:MediaObject,
        ada:image ;
    schema1:additionalType "ada:BSEImage" ;
    schema1:description "Backscattered electron image of ALH84001 thin section" ;
    schema1:encodingFormat "image/tiff" ;
    schema1:name "ALH84001_BSE_001.tif" ;
    schema1:relatedLink [ a schema1:LinkRole ;
            schema1:linkRelationship "metadata" ;
            schema1:target [ a schema1:EntryPoint ;
                    schema1:encodingFormat "application/json" ;
                    schema1:name "ALH84001_BSE_001_metadata.json" ] ] ;
    schema1:size [ a schema1:QuantitativeValue ;
            schema1:unitText "byte" ;
            schema1:value 4521984 ] ;
    ada:componentType [ a ada:BSEImage ] .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Files Type
description: "Properties for any file in an ADA product distribution hasPart. These
  are component files within an archive \u2014 they are NOT individually downloadable
  (no schema:contentUrl). The @type must NOT include schema:DataDownload. GeneralType
  provides info based on broad categories of file format (tabular, image, dataCube,
  document)."
allOf:
- type: object
  description: Base properties common to all file types in hasPart
  properties:
    '@id':
      type: string
    '@type':
      type: array
      items:
        type: string
      not:
        contains:
          const: schema:DataDownload
      minItems: 1
    schema:additionalType:
      type: array
      description: Other classifiers for the file. ADA componentTypes are specified
        in the specific file type schemas attached by $refs.
      items:
        type: string
      x-jsonld-id: http://schema.org/additionalType
    schema:name:
      type: string
      description: String name of file, must be unique within the containing package.
      x-jsonld-id: http://schema.org/name
    schema:description:
      type: string
      x-jsonld-id: http://schema.org/description
    spdx:checksum:
      type: object
      properties:
        spdx:algorithm:
          type: string
          x-jsonld-id: http://spdx.org/rdf/terms#algorithm
        spdx:checksumValue:
          type: string
          x-jsonld-id: http://spdx.org/rdf/terms#checksumValue
      x-jsonld-id: http://spdx.org/rdf/terms#checksum
    schema:size:
      type: object
      properties:
        '@type':
          type: array
          contains:
            const: schema:QuantitativeValue
          minItems: 1
        schema:value:
          type: integer
          x-jsonld-id: http://schema.org/value
        schema:unitText:
          type: string
          default: byte
          x-jsonld-id: http://schema.org/unitText
      x-jsonld-id: http://schema.org/size
    schema:encodingFormat:
      type: array
      items:
        type: string
      x-jsonld-id: http://schema.org/encodingFormat
    ada:resultTarget:
      $ref: https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/BaseSchema/stringArray/schema.yaml
      x-jsonld-id: https://ada.astromat.org/metadata/resultTarget
    schema:relatedLink:
      type: array
      description: 'Links between files in the product. Use schema:name for path to
        target in product, or use #id JSON-LD links. Used to link metadata files in
        bundle to the data or supplementary files they document.'
      items:
        type: object
        properties:
          '@type':
            type: array
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
                contains:
                  const: schema:EntryPoint
                minItems: 1
              schema:encodingFormat:
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
- anyOf:
  - $ref: https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/BaseSchema/image/schema.yaml
  - $ref: https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/BaseSchema/imageMap/schema.yaml
  - $ref: https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/BaseSchema/tabularData/schema.yaml
  - $ref: https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/BaseSchema/structuredData/schema.yaml
  - $ref: https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/BaseSchema/collection/schema.yaml
  - $ref: https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/BaseSchema/dataCube/schema.yaml
  - $ref: https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/BaseSchema/document/schema.yaml
  - $ref: https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/BaseSchema/supDocImage/schema.yaml
  - $ref: https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/BaseSchema/otherFile/schema.yaml
  - type: object
    properties:
      '@type':
        type: array
        contains:
          const: Metadata
    required:
    - '@type'
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/
  spdx: http://spdx.org/rdf/terms#

```

Links to the schema:

* YAML version: [schema.yaml](https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/BaseSchema/files/schema.json)
* JSON version: [schema.json](https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/BaseSchema/files/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "spdx": "http://spdx.org/rdf/terms#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://w3id.org/cdif/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/BaseSchema/files/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/BaseSchema/files`

