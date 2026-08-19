
# EA-IRMS Instrument Detail (Schema)

`ogch.techniqueProfile.adaProfile.EAIRMS.detail` *v0.1*

Elemental Analysis Isotope Ratio Mass Spectrometry collection. Defines properties: @type, massConsumed, elementType.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# EA-IRMS Instrument Detail

Elemental Analysis Isotope Ratio Mass Spectrometry collection.

## Examples

### EA-IRMS Instrument Detail Example
Elemental Analysis Isotope Ratio Mass Spectrometry collection detail.
#### json
```json
{
  "@type": ["ada:EAIRMSCollection"],
  "ada:massConsumed": "2.5 mg",
  "ada:elementType": "carbon"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/adaProfile/EAIRMS/detail/context.jsonld"
  ],
  "@type": [
    "ada:EAIRMSCollection"
  ],
  "ada:massConsumed": "2.5 mg",
  "ada:elementType": "carbon"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .

[] a ada:EAIRMSCollection ;
    ada:elementType "carbon" ;
    ada:massConsumed "2.5 mg" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: EA-IRMS Instrument Detail
description: Elemental Analysis Isotope Ratio Mass Spectrometry collection
type: object
properties:
  ada:componentType:
    const: ada:EAIRMSCollection
    x-jsonld-id: https://ada.astromat.org/metadata/componentType
  ada:massConsumed:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/massConsumed
  ada:elementType:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/elementType
required:
- ada:componentType
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/adaProfile/EAIRMS/detail/schema.json)
* JSON version: [schema.json](https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/adaProfile/EAIRMS/detail/schema.yaml)


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
[context.jsonld](https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/adaProfile/EAIRMS/detail/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/adaProfile/EAIRMS/detail`

