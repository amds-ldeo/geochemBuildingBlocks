
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
  "ada:componentType": "ada:XCTImageCollection",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XCT/detail-legacy/context.jsonld"
  ],
  "@type": [
    "ada:XCTImageCollection"
  ],
  "ada:componentType": "ada:XCTImageCollection",
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
    ada:componentType "ada:XCTImageCollection" ;
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
    if:
      type: object
    then:
      $ref: '#/$defs/QuantitativeValue'
    else:
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
    if:
      type: object
    then:
      $ref: '#/$defs/QuantitativeValue'
    else:
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
    if:
      type: object
    then:
      $ref: '#/$defs/QuantitativeValue'
    else:
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
  ada:xrayEnergy:
    description: Accelerating energy of the X-ray source. This block did not declare
      it at all, while 257 XCTImageCollection subjects carry it -- with its unit in
      a SEPARATE ada:energyUnit key. Emitted as a QuantitativeValue the two fold into
      one node, which is why ada:energyUnit is not declared beside it; the block is
      open, so a record still carrying the split pair is not rejected.
    if:
      type: object
    then:
      $ref: '#/$defs/QuantitativeValue'
    else:
      type: number
    x-jsonld-id: https://ada.astromat.org/metadata/xrayEnergy
  ada:xrayTubeCurrent:
    if:
      type: object
    then:
      $ref: '#/$defs/QuantitativeValue'
    else:
      type: number
    x-jsonld-id: https://ada.astromat.org/metadata/xrayTubeCurrent
  ada:xrayTubeEnergy:
    if:
      type: object
    then:
      $ref: '#/$defs/QuantitativeValue'
    else:
      type: number
    x-jsonld-id: https://ada.astromat.org/metadata/xrayTubeEnergy
  ada:xrayTubePower:
    if:
      type: object
    then:
      $ref: '#/$defs/QuantitativeValue'
    else:
      type: number
    x-jsonld-id: https://ada.astromat.org/metadata/xrayTubePower
required:
- ada:componentType
$defs:
  QuantitativeValue:
    title: Quantitative value with its unit
    description: 'A measured value carrying its unit, for the XCT parameters that
      ADA stores BOTH ways. Of the ~700 XCTImageCollection subjects, roughly 360 hold
      each of these as text with the unit inside it ("90 kV", "11.50844 mm", "33 uA")
      and roughly 76 as a bare number, so about 2,212 values could not be emitted
      at all without discarding the unit.

      DEFINED HERE rather than reused, after looking. The SHAPE is settled and consistent
      across five places -- BaseSchema/image, BaseSchema/files, STEM/detail, and CDIF''s
      cdifManifest and dataDownload -- but none of them offers a general reusable
      $def: image/schema.yaml#/$defs/PixelDimension is the only named one and it types
      schema:value as an INTEGER for pixel counts, which rejects 11.50844. CDIF''s
      is number-valued but inline. So this is a local $def with one consumer. If a
      second block needs it, promote it to a shared one rather than copying -- which
      is the argument PixelDimension''s own description already makes, having been
      written after two blocks declared one property two ways.

      IF/THEN/ELSE RATHER THAN ANYOF, and the reason is diagnostics, not taste. Both
      admit the same two forms, but an anyOf collapses every failure to "is not valid
      under any of the given schemas" naming no property -- measured. With if/then
      an object missing its number reports ''schema:value'' is a required property,
      and a value still stored as the text "90 kV" reports is not of type ''number''
      instead. That matters twice: the counterexample can assert the real cause, and
      ADA sees a message that says what to fix. It also follows this repo''s standing
      preference for if/then over a narrowed anyOf.

      schema:value AND schema:unitText are both REQUIRED. The whole purpose of this
      branch is to carry the unit, so a QuantitativeValue missing either is not a
      weaker statement of the same fact, it is a malformed one -- and the plain-number
      branch is already there for a value with no unit. docs/counterexamples.json
      pins the schema:value half.

      "N/A mm" IS NOT EXPRESSIBLE HERE, deliberately. It appears among the stored
      values and has a unit but no measurement, so it is an ABSENT reading rather
      than a quantity. Omit the property instead; the only required property of this
      block is ada:componentType. Encoding it as a unit-only QuantitativeValue would
      assert that something was measured in millimetres when nothing was.

      schema:unitCode is OPTIONAL and unused today. Allowed because schema.org defines
      it for exactly this, and it lets ADA add a QUDT or UCUM code later without a
      schema change; not required, because none of the 2,212 stored values carries
      one and requiring it would reject every record.'
    type: object
    properties:
      '@type':
        type: array
        items:
          type: string
        contains:
          const: schema:QuantitativeValue
        minItems: 1
      schema:value:
        type: number
        x-jsonld-id: http://schema.org/value
      schema:unitText:
        type: string
        x-jsonld-id: http://schema.org/unitText
      schema:unitCode:
        type: string
        x-jsonld-id: http://schema.org/unitCode
    required:
    - '@type'
    - schema:value
    - schema:unitText
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/
x-bblocks-metadata:
  itemIdentifier: ogch.techniqueProfile.geochemProfile.XCT.detail-legacy
  register: https://amds-ldeo.github.io/geochemBuildingBlocks/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-10-23'

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XCT/detail-legacy/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XCT/detail-legacy/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XCT/detail-legacy/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/XCT/detail-legacy`

