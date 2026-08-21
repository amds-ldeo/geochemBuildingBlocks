
# LAF Instrument Detail (Schema)

`ogch.techniqueProfile.adaProfile.LAF.detail` *v0.1*

Laser Ablation Fluorescence processed/raw data detail properties. Defines properties: @type, elementAnalyzed, sampleMassConsumed, sampleType.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# LAF Instrument Detail

Laser Ablation Fluorescence processed/raw data. elementAnalyzed goes in resultTarget.

## Examples

### LAF Instrument Detail Example
Laser Ablation Fluorescence processed data with element and mass details.
#### json
```json
{
  "@type": ["ada:LAFProcessed"],
  "ada:elementAnalyzed": "U",
  "ada:sampleMassConsumed": "0.3 mg",
  "ada:sampleType": "zircon grain mount"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/adaProfile/LAF/detail/context.jsonld"
  ],
  "@type": [
    "ada:LAFProcessed"
  ],
  "ada:elementAnalyzed": "U",
  "ada:sampleMassConsumed": "0.3 mg",
  "ada:sampleType": "zircon grain mount"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .

[] a ada:LAFProcessed ;
    ada:elementAnalyzed "U" ;
    ada:sampleMassConsumed "0.3 mg" ;
    ada:sampleType "zircon grain mount" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: LAF Instrument Detail
description: Laser Ablation Fluorescence processed/raw data. elementAnalyzed goes
  in resultTarget.
type: object
properties:
  ada:componentType:
    anyOf:
    - const: ada:LAFProcessed
    - const: ada:LAFRaw
    x-jsonld-id: https://ada.astromat.org/metadata/componentType
  ada:elementAnalyzed:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/elementAnalyzed
  ada:sampleMassConsumed:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/sampleMassConsumed
  ada:sampleType:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/sampleType
required:
- ada:componentType
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/adaProfile/LAF/detail/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/adaProfile/LAF/detail/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/adaProfile/LAF/detail/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/adaProfile/LAF/detail`

