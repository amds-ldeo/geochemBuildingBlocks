
# VNMIR Instrument Detail (Schema)

`ogch.analysisSpecificDetails.detailVNMIR` *v0.1*

Very-Near Mid-IR spectroscopy with detailed measurement parameters. Defines properties: @type, detector, beamsplitter, calibrationStandards, comments, numberOfScans, eMaxFitRegionMax, eMaxFitRegionMin, emissionAngle, emissivityMaximum, environmentalPressure, incidenceAngle, measurement, measurementEnvironment, phaseAngle, sampleHeated, samplePreparation, sampleTemperature, spectralRangeMax, spectralRangeMin, spectralResolution, spectralSampling, spotSize, uncertaintyNoise, vacuumExposedSample.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# VNMIR Instrument Detail

Very-Near Mid-IR spectroscopy with detailed measurement parameters.

## Examples

### VNMIR Instrument Detail Example
Very-Near Mid-IR spectroscopy spectral point measurement with detailed parameters.
#### json
```json
{
  "@type": ["ada:VNMIRSpectralPoint"],
  "ada:detector": "MCT",
  "ada:beamsplitter": "KBr",
  "ada:calibrationStandards": "gold mirror",
  "ada:numberOfScans": 256,
  "ada:spectralRangeMin": "400",
  "ada:spectralRangeMax": "4000",
  "ada:spectralResolution": "4 cm-1",
  "ada:spectralSampling": "2 cm-1",
  "ada:spotSize": "100 micrometer",
  "ada:measurement": "reflectance",
  "ada:measurementEnvironment": "ambient",
  "ada:environmentalPressure": 1013.25,
  "ada:sampleHeated": false,
  "ada:sampleTemperature": 25,
  "ada:vacuumExposedSample": false,
  "ada:emissionAngle": 0.0,
  "ada:incidenceAngle": 30.0,
  "ada:phaseAngle": 30.0,
  "ada:uncertaintyNoise": 0.002
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/analysisSpecificDetails/detailVNMIR/context.jsonld"
  ],
  "@type": [
    "ada:VNMIRSpectralPoint"
  ],
  "ada:detector": "MCT",
  "ada:beamsplitter": "KBr",
  "ada:calibrationStandards": "gold mirror",
  "ada:numberOfScans": 256,
  "ada:spectralRangeMin": "400",
  "ada:spectralRangeMax": "4000",
  "ada:spectralResolution": "4 cm-1",
  "ada:spectralSampling": "2 cm-1",
  "ada:spotSize": "100 micrometer",
  "ada:measurement": "reflectance",
  "ada:measurementEnvironment": "ambient",
  "ada:environmentalPressure": 1013.25,
  "ada:sampleHeated": false,
  "ada:sampleTemperature": 25,
  "ada:vacuumExposedSample": false,
  "ada:emissionAngle": 0.0,
  "ada:incidenceAngle": 30.0,
  "ada:phaseAngle": 30.0,
  "ada:uncertaintyNoise": 0.002
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] a ada:VNMIRSpectralPoint ;
    ada:beamsplitter "KBr" ;
    ada:calibrationStandards "gold mirror" ;
    ada:detector "MCT" ;
    ada:emissionAngle 0e+00 ;
    ada:environmentalPressure 1.01325e+03 ;
    ada:incidenceAngle 3e+01 ;
    ada:measurement "reflectance" ;
    ada:measurementEnvironment "ambient" ;
    ada:numberOfScans 256 ;
    ada:phaseAngle 3e+01 ;
    ada:sampleHeated false ;
    ada:sampleTemperature 25 ;
    ada:spectralRangeMax "4000" ;
    ada:spectralRangeMin "400" ;
    ada:spectralResolution "4 cm-1" ;
    ada:spectralSampling "2 cm-1" ;
    ada:spotSize "100 micrometer" ;
    ada:uncertaintyNoise 2e-03 ;
    ada:vacuumExposedSample false .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: VNMIR Instrument Detail
description: Very-Near Mid-IR spectroscopy with detailed measurement parameters
type: object
properties:
  ada:componentType:
    anyOf:
    - const: ada:VNMIRSpectralPoint
    - const: ada:VNMIROverviewImage
    - const: ada:VNMIRSpectralMap
    x-jsonld-id: https://ada.astromat.org/metadata/componentType
  ada:detector:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/detector
  ada:beamsplitter:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/beamsplitter
  ada:calibrationStandards:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/calibrationStandards
  ada:comments:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/comments
  ada:numberOfScans:
    type: integer
    x-jsonld-id: https://ada.astromat.org/metadata/numberOfScans
  ada:eMaxFitRegionMax:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/eMaxFitRegionMax
  ada:eMaxFitRegionMin:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/eMaxFitRegionMin
  ada:emissionAngle:
    type: number
    x-jsonld-id: https://ada.astromat.org/metadata/emissionAngle
  ada:emissivityMaximum:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/emissivityMaximum
  ada:environmentalPressure:
    type: number
    x-jsonld-id: https://ada.astromat.org/metadata/environmentalPressure
  ada:incidenceAngle:
    type: number
    x-jsonld-id: https://ada.astromat.org/metadata/incidenceAngle
  ada:measurement:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/measurement
  ada:measurementEnvironment:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/measurementEnvironment
  ada:phaseAngle:
    type: number
    x-jsonld-id: https://ada.astromat.org/metadata/phaseAngle
  ada:sampleHeated:
    type: boolean
    x-jsonld-id: https://ada.astromat.org/metadata/sampleHeated
  ada:samplePreparation:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/samplePreparation
  ada:sampleTemperature:
    type: integer
    x-jsonld-id: https://ada.astromat.org/metadata/sampleTemperature
  ada:spectralRangeMax:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/spectralRangeMax
  ada:spectralRangeMin:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/spectralRangeMin
  ada:spectralResolution:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/spectralResolution
  ada:spectralSampling:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/spectralSampling
  ada:spotSize:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/spotSize
  ada:uncertaintyNoise:
    type: number
    x-jsonld-id: https://ada.astromat.org/metadata/uncertaintyNoise
  ada:vacuumExposedSample:
    type: boolean
    x-jsonld-id: https://ada.astromat.org/metadata/vacuumExposedSample
required:
- ada:componentType
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/analysisSpecificDetails/detailVNMIR/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/analysisSpecificDetails/detailVNMIR/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/analysisSpecificDetails/detailVNMIR/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/analysisSpecificDetails/detailVNMIR`

