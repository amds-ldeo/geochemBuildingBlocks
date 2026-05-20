
# XRD Instrument Detail (Schema)

`ogch.analysisSpecificDetails.detailXRD` *v0.1*

X-ray Diffraction tabular data with geometry and wavelength. Defines properties: @type, geometry, sampleMount, stepSize, timePerStep, wavelength.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# XRD Instrument Detail

X-ray Diffraction tabular data with geometry and wavelength.

## Examples

### XRD Instrument Detail Example
X-ray Diffraction tabular data with geometry and wavelength parameters.
#### json
```json
{
  "@type": ["ada:XRDTabular"],
  "ada:geometry": "Bragg-Brentano",
  "ada:sampleMount": "flat plate",
  "ada:stepSize": 0.02,
  "ada:timePerStep": 1.0,
  "ada:wavelength": 1.5406
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/analysisSpecificDetails/detailXRD/context.jsonld"
  ],
  "@type": [
    "ada:XRDTabular"
  ],
  "ada:geometry": "Bragg-Brentano",
  "ada:sampleMount": "flat plate",
  "ada:stepSize": 0.02,
  "ada:timePerStep": 1.0,
  "ada:wavelength": 1.5406
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] a ada:XRDTabular ;
    ada:geometry "Bragg-Brentano" ;
    ada:sampleMount "flat plate" ;
    ada:stepSize 2e-02 ;
    ada:timePerStep 1e+00 ;
    ada:wavelength 1.5406e+00 .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: XRD Instrument Detail
description: X-ray Diffraction tabular data with geometry and wavelength
type: object
properties:
  ada:componentType:
    const: ada:XRDTabular
    x-jsonld-id: https://ada.astromat.org/metadata/componentType
  ada:geometry:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/geometry
  ada:sampleMount:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/sampleMount
  ada:stepSize:
    type: number
    x-jsonld-id: https://ada.astromat.org/metadata/stepSize
  ada:timePerStep:
    type: number
    x-jsonld-id: https://ada.astromat.org/metadata/timePerStep
  ada:wavelength:
    type: number
    x-jsonld-id: https://ada.astromat.org/metadata/wavelength
required:
- ada:componentType
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/analysisSpecificDetails/detailXRD/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/analysisSpecificDetails/detailXRD/schema.yaml)


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
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/analysisSpecificDetails/detailXRD/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/analysisSpecificDetails/detailXRD`

