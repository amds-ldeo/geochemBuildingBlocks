
# EMPA Instrument Detail (Schema)

`ogch.analysisSpecificDetails.detailEMPA` *v0.1*

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
    "https://usgin.github.io/geochemBuildingBlocks/build/annotated/analysisSpecificDetails/detailEMPA/context.jsonld"
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
  as sibling properties on the hasPart item. Per-dataset schema:additionalProperty
  entries are constrained inline via $refs to the parameterValues registry (one schema:PropertyValue
  branch per readOnly:false empaTAPP parameter, plus a catch-all). schema:measurementTechnique
  is an @id reference to a registered empaTAPP TAPP definition.
allOf:
- type: object
  properties:
    ada:componentType:
      anyOf:
      - const: ada:EMPAImage
      - const: ada:EMPAImageMap
      - const: ada:EMPAQEATabular
      - const: ada:EMPAImageCollection
      - const: ada:EMPAESPCTabular
      - const: ada:EMPAESPCPlot
      x-jsonld-id: https://ada.astromat.org/metadata/componentType
    ada:spectrometersUsed:
      type: string
      description: Spectrometers used in analysis
      x-jsonld-id: https://ada.astromat.org/metadata/spectrometersUsed
    ada:signalUsed:
      type: string
      x-jsonld-id: https://ada.astromat.org/metadata/signalUsed
    schema:measurementTechnique:
      type: object
      description: '@id reference to a registered empaTAPP TAPP definition.'
      properties:
        '@id':
          type: string
          format: uri
      required:
      - '@id'
      x-jsonld-id: http://schema.org/measurementTechnique
  required:
  - ada:componentType
- type: object
  properties:
    schema:additionalProperty:
      type: array
      description: "Per-dataset schema:PropertyValue entries for this EMPA dataset.
        Each item is any of the empaTAPP-derived parameter types or (via the catch-all
        branch) any other PropertyValue. All entries are optional \u2014 include only
        the parameters you have values for."
      items:
        anyOf:
        - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/parameterValues/schema.yaml#/$defs/acceleratingVoltage
        - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/parameterValues/schema.yaml#/$defs/beamDiameter
        - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/parameterValues/schema.yaml#/$defs/BeamRasterDimension
        - $ref: https://usgin.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/parameterValues/schema.yaml#/$defs/reportedAnalyte
        - type: object
          description: Catch-all for additional schema:PropertyValue entries beyond
            those enumerated in the empaTAPP-derived catalog above.
          properties:
            '@type':
              type: array
              items:
                type: string
              contains:
                const: schema:PropertyValue
            schema:propertyID:
              type: string
              not:
                enum:
                - ada:parameter/empaTAPP/BeamRasterDimension
                - ada:parameter/empaTAPP/acceleratingVoltage
                - ada:parameter/empaTAPP/beamDiameter
                - ada:parameter/empaTAPP/reportedAnalyte
              x-jsonld-id: http://schema.org/propertyID
          required:
          - '@type'
          - schema:propertyID
      x-jsonld-id: http://schema.org/additionalProperty
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://usgin.github.io/geochemBuildingBlocks/build/annotated/analysisSpecificDetails/detailEMPA/schema.json)
* JSON version: [schema.json](https://usgin.github.io/geochemBuildingBlocks/build/annotated/analysisSpecificDetails/detailEMPA/schema.yaml)


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
[context.jsonld](https://usgin.github.io/geochemBuildingBlocks/build/annotated/analysisSpecificDetails/detailEMPA/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/usgin/geochemBuildingBlocks](https://github.com/usgin/geochemBuildingBlocks)
* Path: `_sources/analysisSpecificDetails/detailEMPA`

