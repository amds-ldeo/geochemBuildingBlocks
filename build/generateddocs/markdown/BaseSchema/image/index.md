
# Image Type (Schema)

`ogch.BaseSchema.image` *v0.1*

ADA image with componentType classification for analytical images. Defines properties: @type, acquisitionTime, componentType, channel1, channel2, channel3, pixelSize, illuminationType, imageType.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Image Type

Describes image objects in ADA metadata with acquisition details and component type classification. Typed as `ada:image` and `schema:ImageObject`. Supports various analytical image types including EPMA, SEM, TEM, STEM, and spectroscopic images.

## Examples

### Image Type Example
An SEM backscattered electron image with component type and acquisition details.
#### json
```json
{
  "@type": ["ada:image", "schema:ImageObject"],
  "ada:componentType": "ada:SEMImage",
  "ada:acquisitionTime": "2024-03-15T14:30:00Z",
  "ada:channel1": "BSE",
  "ada:pixelSize": "0.5 micrometer",
  "ada:illuminationType": "Electron beam",
  "ada:imageType": "Backscattered electron"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/image/context.jsonld"
  ],
  "@type": [
    "ada:image",
    "schema:ImageObject"
  ],
  "ada:componentType": "ada:SEMImage",
  "ada:acquisitionTime": "2024-03-15T14:30:00Z",
  "ada:channel1": "BSE",
  "ada:pixelSize": "0.5 micrometer",
  "ada:illuminationType": "Electron beam",
  "ada:imageType": "Backscattered electron"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .

[] a schema1:ImageObject,
        ada:image ;
    ada:acquisitionTime "2024-03-15T14:30:00Z" ;
    ada:channel1 "BSE" ;
    ada:componentType "ada:SEMImage" ;
    ada:illuminationType "Electron beam" ;
    ada:imageType "Backscattered electron" ;
    ada:pixelSize "0.5 micrometer" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Image Type
description: Image objects with acquisition details and component type classification.
  Typed as ada:image and schema:ImageObject.
type: object
properties:
  '@type':
    type: array
    items:
      type: string
    minItems: 2
    allOf:
    - contains:
        const: ada:image
    - contains:
        const: schema:ImageObject
    description: GeneralType for images
  ada:acquisitionTime:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/acquisitionTime
  ada:componentType:
    type: string
    enum:
    - ada:AIVAImage
    - ada:BSEImage
    - ada:CLImage
    - ada:CPDImage
    - ada:EPMAESPCPlot
    - ada:EPMAImage
    - ada:FIBSEMImage
    - ada:GCMSChromatogram
    - ada:GCMSSpectraPlot
    - ada:L2MSOverviewImage
    - ada:L2MSSpectraPlot
    - ada:LAICPMSImage
    - ada:LCMSChromatogram
    - ada:LCMSVisualization
    - ada:LITImage
    - ada:NanoIRBackground
    - ada:NanoSIMSImage
    - ada:PSFDContextImage
    - ada:QRISCalibrated
    - ada:QRISCalibratedImage
    - ada:QRISFlatFieldImage
    - ada:QRISRaw
    - ada:QRISRawImage
    - ada:SEMEDSPointSpectraPlot
    - ada:SEMFIBIonImage
    - ada:SEMHRCLimage
    - ada:SEMImage
    - ada:SIMSProcessedImage
    - ada:SLSShapeModelImage
    - ada:STEMEDSSpectraPlot
    - ada:STEMEELSSpectraPlot
    - ada:STEMImage
    - ada:SVRUECWaveformPlot
    - ada:SXRF2DImage
    - ada:TEMDiffractionPattern
    - ada:TEMImage
    - ada:TEMPatternsImage
    - ada:TOFSIMSIonImages
    - ada:TOFSIMSMassSpectrumPlot
    - ada:UVFMImage
    - ada:VLMImage
    - ada:VNMIROverviewImage
    - ada:VNMIRSpectraPlot
    - ada:XANESImageStack
    - ada:XANESStackOverviewImage
    - ada:XRDDiffractionPattern
    - ada:XRDIndexedImage
    - ada:plot
    - ada:analysisLocation
    - ada:annotatedImage
    - ada:areaOfInterest
    - ada:basemap
    - ada:calibrationFile
    - ada:code
    - ada:contextPhotography
    - ada:contextVideo
    - ada:inputFile
    - ada:instrumentMetadata
    - ada:logFile
    - ada:methodDescription
    - ada:other
    - ada:processingMethod
    - ada:quickLook
    - ada:report
    - ada:samplePreparation
    - ada:shapefile
    - ada:supplementalBasemap
    - ada:supplementaryImage
    - ada:worldFile
    - nil:missing
    description: ADA componentType for an image, as a single string. Allowed values
      are constrained at the technique-profile level.
    x-jsonld-id: https://ada.astromat.org/metadata/componentType
  ada:channel1:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/channel1
  ada:channel2:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/channel2
  ada:channel3:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/channel3
  ada:pixelSize:
    type: string
    x-jsonld-id: https://ada.astromat.org/metadata/pixelSize
  ada:illuminationType:
    type: string
    description: Type of illumination used to create the image. Examples include Visible
      light, Cross-polarized visible light, ultraviolet light, Electron beam, X-ray.
    x-jsonld-id: https://ada.astromat.org/metadata/illuminationType
  ada:imageType:
    type: string
    description: Specifies the nature of the sample's response to the illumination
      that was detected and measured.
    x-jsonld-id: https://ada.astromat.org/metadata/imageType
  ada:spatialRegistration:
    description: 'Pixel size and its units. SCALING ONLY -- the half of a spatial
      registration an unregistered image can state. A plain image has a pixel size,
      and ada:pixelScaleX on an ada:EPMAImage is a well-formed statement, but an image
      does not say where it sits on the sample or how its axes relate to the sample
      axes. The imageMap block references the full shape, which adds the origin, the
      origin corner, the coordinate definition and the two rotation terms, and whose
      required list demands them.

      Same property NAME on both branches on purpose: a placement path such as schema:hasPart[@type=ada:image|ada:imageMap].ada:spatialRegistration.ada:pixelScaleX
      then resolves through either, which is what the subject-key register and the
      TAPP sidecars both target. Before this, the image branch declared no spatialRegistration
      at all -- not because a pixel scale is meaningless on an image, but because
      the only available shape required an origin and a corner, so an image could
      not use it without asserting a registration it does not have.'
    $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/spatialRegistration/schema.yaml#/$defs/Scaling
    x-jsonld-id: https://ada.astromat.org/metadata/spatialRegistration
required:
- '@type'
- ada:componentType
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/image/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/image/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/image/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/BaseSchema/image`

