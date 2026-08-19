
# XCT Instrument Detail (Schema)

`ogch.techniqueProfile.geochemProfile.XCT.detail-legacy` *v0.1*

X-ray Computed Tomography images with detailed scan parameters. Defines properties: @type, beamFilterMaterial, beamFilterThickness, dataRangeLower, dataRangeUpper, detectorGain, detectorBinning, detectorSize, detectorType, imageExposure, imageFPS, imageGain, imageSize, instrumentType, nsiBeamHardening, numberOfFramesAveragedPerProjection, numberOfProjections, numberOfSlices, pixelPitch, reconstructedDataFormat, reconstructedVoxelSize, reconstructionSoftware, rotationAngle, rotationType, sourceToDetectorDistance, sourceToObjectDistance, subPixGrid, subPixShift, xraySource, xrayTargetMaterial, xrayTubeCurrent, xrayTubeEnergy, xrayTubePower.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# XCT Instrument Detail

X-ray Computed Tomography images with detailed scan parameters. (Extension type, not in v3 source schema.)

## Examples

### XCT Instrument Detail Example
X-ray Computed Tomography image collection with detailed scan parameters.
#### json
```json
{
  "@type": ["ada:XCTImageCollection"],
  "ada:instrumentType": "micro-CT",
  "ada:xraySource": "sealed tube",
  "ada:xrayTargetMaterial": "tungsten",
  "ada:xrayTubeEnergy": 120.0,
  "ada:xrayTubeCurrent": 0.1,
  "ada:xrayTubePower": 12.0,
  "ada:beamFilterMaterial": "copper",
  "ada:beamFilterThickness": 0.5,
  "ada:sourceToDetectorDistance": "500 mm",
  "ada:sourceToObjectDistance": 200.0,
  "ada:detectorType": "flat panel",
  "ada:detectorSize": "2048x2048",
  "ada:detectorBinning": "1x1",
  "ada:numberOfProjections": 1440,
  "ada:numberOfSlices": 2000,
  "ada:numberOfFramesAveragedPerProjection": 4,
  "ada:rotationAngle": "360 degrees",
  "ada:rotationType": "step-and-shoot",
  "ada:imageExposure": 0.5,
  "ada:imageSize": "2048x2048",
  "ada:reconstructedVoxelSize": "5.0 micrometer",
  "ada:reconstructedDataFormat": "16-bit TIFF",
  "ada:reconstructionSoftware": "Nikon CT Pro 3D"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/XCT/detail-legacy/context.jsonld"
  ],
  "@type": [
    "ada:XCTImageCollection"
  ],
  "ada:instrumentType": "micro-CT",
  "ada:xraySource": "sealed tube",
  "ada:xrayTargetMaterial": "tungsten",
  "ada:xrayTubeEnergy": 120.0,
  "ada:xrayTubeCurrent": 0.1,
  "ada:xrayTubePower": 12.0,
  "ada:beamFilterMaterial": "copper",
  "ada:beamFilterThickness": 0.5,
  "ada:sourceToDetectorDistance": "500 mm",
  "ada:sourceToObjectDistance": 200.0,
  "ada:detectorType": "flat panel",
  "ada:detectorSize": "2048x2048",
  "ada:detectorBinning": "1x1",
  "ada:numberOfProjections": 1440,
  "ada:numberOfSlices": 2000,
  "ada:numberOfFramesAveragedPerProjection": 4,
  "ada:rotationAngle": "360 degrees",
  "ada:rotationType": "step-and-shoot",
  "ada:imageExposure": 0.5,
  "ada:imageSize": "2048x2048",
  "ada:reconstructedVoxelSize": "5.0 micrometer",
  "ada:reconstructedDataFormat": "16-bit TIFF",
  "ada:reconstructionSoftware": "Nikon CT Pro 3D"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

[] a ada:XCTImageCollection ;
    ada:beamFilterMaterial "copper" ;
    ada:beamFilterThickness 5e-01 ;
    ada:detectorBinning "1x1" ;
    ada:detectorSize "2048x2048" ;
    ada:detectorType "flat panel" ;
    ada:imageExposure 5e-01 ;
    ada:imageSize "2048x2048" ;
    ada:instrumentType "micro-CT" ;
    ada:numberOfFramesAveragedPerProjection 4 ;
    ada:numberOfProjections 1440 ;
    ada:numberOfSlices 2000 ;
    ada:reconstructedDataFormat "16-bit TIFF" ;
    ada:reconstructedVoxelSize "5.0 micrometer" ;
    ada:reconstructionSoftware "Nikon CT Pro 3D" ;
    ada:rotationAngle "360 degrees" ;
    ada:rotationType "step-and-shoot" ;
    ada:sourceToDetectorDistance "500 mm" ;
    ada:sourceToObjectDistance 2e+02 ;
    ada:xraySource "sealed tube" ;
    ada:xrayTargetMaterial "tungsten" ;
    ada:xrayTubeCurrent 1e-01 ;
    ada:xrayTubeEnergy 1.2e+02 ;
    ada:xrayTubePower 1.2e+01 .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: XCT Instrument Detail
description: X-ray Computed Tomography images with detailed scan parameters. (Extension
  type, not in v3 source schema.)
type: object
properties:
  ada:componentType:
    const: ada:XCTImageCollection
    x-jsonld-id: https://ada.astromat.org/metadata/componentType
  ada:beamFilterMaterial:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/beamFilterMaterial
  ada:beamFilterThickness:
    type: number
    x-jsonld-id: https://ada.astromat.org/metadata/beamFilterThickness
  ada:dataRangeLower:
    type: integer
    x-jsonld-id: https://ada.astromat.org/metadata/dataRangeLower
  ada:dataRangeUpper:
    type: integer
    x-jsonld-id: https://ada.astromat.org/metadata/dataRangeUpper
  ada:detectorGain:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/detectorGain
  ada:detectorBinning:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/detectorBinning
  ada:detectorSize:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/detectorSize
  ada:detectorType:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/detectorType
  ada:imageExposure:
    type: number
    x-jsonld-id: https://ada.astromat.org/metadata/imageExposure
  ada:imageFPS:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/imageFPS
  ada:imageGain:
    type: number
    x-jsonld-id: https://ada.astromat.org/metadata/imageGain
  ada:imageSize:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/imageSize
  ada:instrumentType:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/instrumentType
  ada:nsiBeamHardening:
    type: number
    x-jsonld-id: https://ada.astromat.org/metadata/nsiBeamHardening
  ada:numberOfFramesAveragedPerProjection:
    type: integer
    x-jsonld-id: https://ada.astromat.org/metadata/numberOfFramesAveragedPerProjection
  ada:numberOfProjections:
    type: integer
    x-jsonld-id: https://ada.astromat.org/metadata/numberOfProjections
  ada:numberOfSlices:
    type: integer
    x-jsonld-id: https://ada.astromat.org/metadata/numberOfSlices
  ada:pixelPitch:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/pixelPitch
  ada:reconstructedDataFormat:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/reconstructedDataFormat
  ada:reconstructedVoxelSize:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/reconstructedVoxelSize
  ada:reconstructionSoftware:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/reconstructionSoftware
  ada:rotationAngle:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/rotationAngle
  ada:rotationType:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/rotationType
  ada:sourceToDetectorDistance:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/sourceToDetectorDistance
  ada:sourceToObjectDistance:
    type: number
    x-jsonld-id: https://ada.astromat.org/metadata/sourceToObjectDistance
  ada:subPixGrid:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/subPixGrid
  ada:subPixShift:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/subPixShift
  ada:xraySource:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/xraySource
  ada:xrayTargetMaterial:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/xrayTargetMaterial
  ada:xrayTubeCurrent:
    type: number
    x-jsonld-id: https://ada.astromat.org/metadata/xrayTubeCurrent
  ada:xrayTubeEnergy:
    type: number
    x-jsonld-id: https://ada.astromat.org/metadata/xrayTubeEnergy
  ada:xrayTubePower:
    type: number
    x-jsonld-id: https://ada.astromat.org/metadata/xrayTubePower
required:
- ada:componentType
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/XCT/detail-legacy/schema.json)
* JSON version: [schema.json](https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/XCT/detail-legacy/schema.yaml)


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
[context.jsonld](https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/XCT/detail-legacy/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/XCT/detail-legacy`

