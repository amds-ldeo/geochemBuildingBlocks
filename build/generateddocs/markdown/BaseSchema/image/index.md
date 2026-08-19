
# Image Type (Schema)

`ogch.BaseSchema.image` *v0.1*

ADA image with componentType classification for analytical images. Defines properties: @type, acquisitionTime, componentType, channel1, channel2, channel3, pixelSize, illuminationType, imageType.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Image Type

Describes image objects in ADA metadata with acquisition details and component type classification. Typed as `ada:image` and `schema:ImageObject`. Supports various analytical image types including EMPA, SEM, TEM, STEM, and spectroscopic images.

## Examples

### Image Type Example
An SEM backscattered electron image with component type and acquisition details.
#### json
```json
{
  "@type": ["ada:image", "schema:ImageObject"],
  "ada:componentType": {
    "@type": "ada:SEMImageCollection"
  },
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/BaseSchema/image/context.jsonld"
  ],
  "@type": [
    "ada:image",
    "schema:ImageObject"
  ],
  "ada:componentType": {
    "@type": "ada:SEMImageCollection"
  },
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
    ada:componentType [ a ada:SEMImageCollection ] ;
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
    - ada:EMPAESPCPlot
    - ada:EMPAImage
    - ada:GCMSChromatogram
    - ada:GCMSSpectraPlot
    - ada:L2MSOverviewImage
    - ada:L2MSSpectraPlot
    - ada:LCMSChromatogram
    - ada:LCMSVisualization
    - ada:LITImage
    - ada:NanoIRBackground
    - ada:NanoSIMSImage
    - ada:PSFDContextImage
    - ada:QRISCalibratedImage
    - ada:QRISFlatFieldImage
    - ada:QRISRawImage
    - ada:SEMEDSPointSpectraPlot
    - ada:SEMHRCLimage
    - ada:SEMImage
    - ada:SLSShapeModelImage
    - ada:STEMEDSSpectraPlot
    - ada:STEMEELSSpectraPlot
    - ada:STEMImage
    - ada:SVRUECWaveformPlot
    - ada:TEMImage
    - ada:TEMPatternsImage
    - ada:TOFSIMSIonImages
    - ada:TOFSIMSMassSpectrumPlot
    - ada:UVFMImage
    - ada:VLMImage
    - ada:VNMIRSpectraPlot
    - ada:XANESImageStack
    - ada:XANESStackOverviewImage
    - ada:XRDDiffractionPattern
    - ada:XRDIndexedImage
    - ada:plot
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
required:
- '@type'
- ada:componentType
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/BaseSchema/image/schema.json)
* JSON version: [schema.json](https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/BaseSchema/image/schema.yaml)


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
[context.jsonld](https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/BaseSchema/image/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/BaseSchema/image`

