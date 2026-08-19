
# NanoSIMS Instrument Detail (Schema)

`ogch.techniqueProfile.adaProfile.NanoSIMS.detail` *v0.1*

Nano Secondary Ion Mass Spectrometry with isotope tracking. Defines properties: @type, phaseAnalyzed, isotopeAnalyzed. Uses building blocks: stringArray (geochemProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# NanoSIMS Instrument Detail

Nano Secondary Ion Mass Spectrometry with isotope tracking.

## Examples

### NanoSIMS Instrument Detail Example
NanoSIMS detail with isotope and phase tracking for presolar grain analysis.
#### json
```json
{
  "@type": ["ada:NanoSIMSTabular"],
  "ada:phaseAnalyzed": ["presolar SiC", "presolar graphite"],
  "ada:isotopeAnalyzed": ["12C", "13C", "28Si", "29Si"]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/adaProfile/NanoSIMS/detail/context.jsonld"
  ],
  "@type": [
    "ada:NanoSIMSTabular"
  ],
  "ada:phaseAnalyzed": [
    "presolar SiC",
    "presolar graphite"
  ],
  "ada:isotopeAnalyzed": [
    "12C",
    "13C",
    "28Si",
    "29Si"
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .

[] a ada:NanoSIMSTabular ;
    ada:isotopeAnalyzed "12C",
        "13C",
        "28Si",
        "29Si" ;
    ada:phaseAnalyzed "presolar SiC",
        "presolar graphite" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: NanoSIMS Instrument Detail
description: Nano Secondary Ion Mass Spectrometry with isotope tracking
type: object
properties:
  ada:componentType:
    anyOf:
    - const: ada:NanoSIMSCollection
    - const: ada:NanoSIMSImageCollection
    - const: ada:NanoSIMSTabular
    - const: ada:NanoSIMSMap
    x-jsonld-id: https://ada.astromat.org/metadata/componentType
  ada:phaseAnalyzed:
    $ref: https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/BaseSchema/stringArray/schema.yaml
    x-jsonld-id: https://ada.astromat.org/metadata/phaseAnalyzed
  ada:isotopeAnalyzed:
    $ref: https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/BaseSchema/stringArray/schema.yaml
    x-jsonld-id: https://ada.astromat.org/metadata/isotopeAnalyzed
required:
- ada:componentType
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/adaProfile/NanoSIMS/detail/schema.json)
* JSON version: [schema.json](https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/adaProfile/NanoSIMS/detail/schema.yaml)


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
[context.jsonld](https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/adaProfile/NanoSIMS/detail/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/adaProfile/NanoSIMS/detail`

