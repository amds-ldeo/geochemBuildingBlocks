
# PSFD Instrument Detail (Schema)

`ogch.techniqueProfile.adaProfile.PSFD.detail` *v0.1*

Point Spread Function Data with image names and conditions. Defines properties: @type, imageName, imageViewingConditions. Uses building blocks: stringArray (geochemProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# PSFD Instrument Detail

Point Spread Function Data with image names and conditions.

## Examples

### PSFD Instrument Detail Example
Point Spread Function Data detail with image names and viewing conditions.
#### json
```json
{
  "@type": ["ada:PSFDTabular"],
  "ada:imageName": ["crater_overview_001.tif", "crater_overview_002.tif"],
  "ada:imageViewingConditions": "nadir, 50m altitude"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/adaProfile/PSFD/detail/context.jsonld"
  ],
  "@type": [
    "ada:PSFDTabular"
  ],
  "ada:imageName": [
    "crater_overview_001.tif",
    "crater_overview_002.tif"
  ],
  "ada:imageViewingConditions": "nadir, 50m altitude"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .

[] a ada:PSFDTabular ;
    ada:imageName "crater_overview_001.tif",
        "crater_overview_002.tif" ;
    ada:imageViewingConditions "nadir, 50m altitude" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: PSFD Instrument Detail
description: Point Spread Function Data with image names and conditions
type: object
properties:
  ada:componentType:
    const: ada:PSFDTabular
    x-jsonld-id: https://ada.astromat.org/metadata/componentType
  ada:imageName:
    $ref: https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/BaseSchema/stringArray/schema.yaml
    x-jsonld-id: https://ada.astromat.org/metadata/imageName
  ada:imageViewingConditions:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/imageViewingConditions
required:
- ada:componentType
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/adaProfile/PSFD/detail/schema.json)
* JSON version: [schema.json](https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/adaProfile/PSFD/detail/schema.yaml)


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
[context.jsonld](https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/adaProfile/PSFD/detail/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/adaProfile/PSFD/detail`

