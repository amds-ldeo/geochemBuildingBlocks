
# EMPA Instrument Detail (Schema)

`ada.bbr.metadata.geochemProperties.detailEMPA` *v0.1*

Electron Microprobe Analysis instrument-specific detail properties. Defines properties: @type, spectrometersUsed, signalUsed.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# EMPA Instrument Detail

Electron Microprobe Analysis with spectrometer and signal details.

## Examples

### EMPA Instrument Detail Example
Electron Microprobe Analysis detail with spectrometer and signal information.
#### json
```json
{
  "@type": ["ada:EMPAQEATabular"],
  "ada:spectrometersUsed": "WDS 1-5",
  "ada:signalUsed": "characteristic X-rays"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailEMPA/context.jsonld"
  ],
  "@type": [
    "ada:EMPAQEATabular"
  ],
  "ada:spectrometersUsed": "WDS 1-5",
  "ada:signalUsed": "characteristic X-rays"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .

[] a ada:EMPAQEATabular ;
    ada:signalUsed "characteristic X-rays" ;
    ada:spectrometersUsed "WDS 1-5" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: EMPA Instrument Detail
description: Detail block for Electron Microprobe Analysis hasPart items. Discriminates
  on ada:componentType (string) and contributes ada:spectrometersUsed and ada:signalUsed
  as sibling properties on the hasPart item.
type: object
properties:
  ada:componentType:
    anyOf:
    - const: ada:EMPAImage
    - const: ada:EMPAImageMap
    - const: ada:EMPAQEATabular
    - const: ada:EMPAImageCollection
    - const: ada:EMPAESPCTabular
    - const: ada:EMPAESPCPlot
  ada:spectrometersUsed:
    type: string
    description: Spectrometers used in analysis
  ada:signalUsed:
    type: string
required:
- ada:componentType
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailEMPA/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailEMPA/schema.yaml)


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
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/bbr/metadata/geochemProperties/detailEMPA/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/geochemProperties/detailEMPA`

