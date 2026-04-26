
# Collection Type (Schema)

`ada.bbr.metadata.geochemProperties.collection` *v0.1*

Set of related files with identical information models or composite datasets. Defines properties: @type, componentType, memberTypes, nFiles, filelist. Uses building blocks: stringArray (geochemProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Collection Type

Describes a collection of related files in ADA metadata. Can represent a set of files with identical information models and serialization (a collection), or a heterogeneous set of files constituting a composite dataset. Typed as `ada:collection` and `schema:Collection`.

## Examples

### Collection Type Example
A collection of SEM-EDS elemental map images with file listing.
#### json
```json
{
  "@type": ["ada:collection", "https://schema.org/Collection"],
  "ada:componentType": {
    "@type": "ada:SEMEDSElementalMaps"
  },
  "ada:memberTypes": ["ada:SEMEDSElementalMap"],
  "ada:nFiles": 5,
  "ada:filelist": [
    {
      "ada:fileName": "map_Fe_Ka.tif",
      "ada:componentType": "ada:SEMEDSElementalMap",
      "schema:encodingFormat": "image/tiff"
    },
    {
      "ada:fileName": "map_Si_Ka.tif",
      "ada:componentType": "ada:SEMEDSElementalMap",
      "schema:encodingFormat": "image/tiff"
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
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/collection/context.jsonld"
  ],
  "@type": [
    "ada:collection",
    "https://schema.org/Collection"
  ],
  "ada:componentType": {
    "@type": "ada:SEMEDSElementalMaps"
  },
  "ada:memberTypes": [
    "ada:SEMEDSElementalMap"
  ],
  "ada:nFiles": 5,
  "ada:filelist": [
    {
      "ada:fileName": "map_Fe_Ka.tif",
      "ada:componentType": "ada:SEMEDSElementalMap",
      "schema:encodingFormat": "image/tiff"
    },
    {
      "ada:fileName": "map_Si_Ka.tif",
      "ada:componentType": "ada:SEMEDSElementalMap",
      "schema:encodingFormat": "image/tiff"
    }
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema: <https://schema.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] a ada:collection,
        schema:Collection ;
    ada:componentType [ a ada:SEMEDSElementalMaps ] ;
    ada:filelist [ schema1:encodingFormat "image/tiff" ;
            ada:componentType "ada:SEMEDSElementalMap" ;
            ada:fileName "map_Si_Ka.tif" ],
        [ schema1:encodingFormat "image/tiff" ;
            ada:componentType "ada:SEMEDSElementalMap" ;
            ada:fileName "map_Fe_Ka.tif" ] ;
    ada:memberTypes "ada:SEMEDSElementalMap" ;
    ada:nFiles 5 .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Collection Type
description: A collection can be a set of files with identical information model and
  serialization/formatting, or a heterogeneous set of files that together constitute
  a dataset (a composite dataset).
type: object
properties:
  '@type':
    type: array
    items:
      type: string
    minItems: 2
    allOf:
    - contains:
        const: ada:collection
    - contains:
        const: https://schema.org/Collection
    description: GeneralType for collections
  ada:componentType:
    type: string
    enum:
    - ada:EMPAImageCollection
    - ada:PSFDShapeFile
    - ada:XCTImageCollection
    - ada:shapefile
    description: ADA componentType for a collection, as a single string. Allowed values
      are constrained by the technique profile (via its hasPart anyOf), which either
      lists universal componentTypes inline or $refs a detail schema enumerating technique-specific
      collection componentTypes.
  ada:memberTypes:
    description: List of the component types in the collection
    $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/stringArray/schema.yaml
  ada:nFiles:
    type: integer
    description: Number of files in the collection, including metadata files
  ada:filelist:
    type: array
    items:
      type: object
      properties:
        ada:fileName:
          type: string
          description: Full path to file in container object
        ada:fileNamePattern:
          type: string
          description: Pattern for collection members with differentiating suffix
            at '*'
        ada:componentType:
          type: string
          description: componentType of an individual file within the collection.
            Not constrained to the collection-level enum, since a collection holds
            heterogeneous files (each carrying its own file-type componentType).
        schema:encodingFormat:
          type: string
          description: MIME type with extension
      oneOf:
      - required:
        - ada:fileName
      - required:
        - ada:fileNamePattern
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/collection/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/collection/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/collection/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/geochemProperties/collection`

