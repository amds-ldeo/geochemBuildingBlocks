
# DSC Instrument Detail (Schema)

`ogch.analysisSpecificDetails.detailDSC` *v0.1*

Differential Scanning Calorimetry heat tabular data. Defines properties: @type, analysisType.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# DSC Instrument Detail

Differential Scanning Calorimetry heat tabular data.

## Examples

### DSC Instrument Detail Example
Differential Scanning Calorimetry heat flow data detail.
#### json
```json
{
  "@type": ["ada:DSCHeatTabular"],
  "ada:analysisType": "heating"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/analysisSpecificDetails/detailDSC/context.jsonld"
  ],
  "@type": [
    "ada:DSCHeatTabular"
  ],
  "ada:analysisType": "heating"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .

[] a ada:DSCHeatTabular ;
    ada:analysisType "heating" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: DSC Instrument Detail
description: Differential Scanning Calorimetry heat tabular data
type: object
properties:
  ada:componentType:
    const: ada:DSCHeatTabular
    x-jsonld-id: https://ada.astromat.org/metadata/componentType
  ada:analysisType:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/analysisType
required:
- ada:componentType
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/analysisSpecificDetails/detailDSC/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/analysisSpecificDetails/detailDSC/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/analysisSpecificDetails/detailDSC/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/analysisSpecificDetails/detailDSC`

