
# Scanning Transmission Electron Microscopy Analysis Detail (Schema)

`ogch.techniqueProfile.geochemProfile.STEM.detail` *v0.1*

Detail block for STEM hasPart items. Image pixel size and image dimensions are the only properties both laboratories record, and the pixel size appears in m, nm and um, so it needs normalising before values are compared.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### detail example HF5000
detail instance derived from ADA n=365 | Maizey, Beau | University of Arizona | Hitachi HF5000 (25 instrumentMetadata exports).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-HF5000",
  "@type": [
    "ada:STEMImage"
  ],
  "ada:componentType": "ada:STEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:stemTAPP-HF5000",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Maizey; Beau",
  "ada:analysisStartDate": "2024-05-16",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "missing",
  "ada:magnification": 14000,
  "ada:dwellTimePerProbePosition": 4,
  "ada:cameraLength": 37,
  "ada:stageXPosition": -0.1375,
  "ada:stageYPosition": -0.1776,
  "ada:stageTiltAlpha": 0.0,
  "ada:stageTiltBeta": 0.1,
  "ada:imagePixelSize": 0.3696,
  "ada:imageWidth": 2048,
  "ada:imageHeight": 2048,
  "schema:distribution": {
    "schema:hasPart": {
      "schema:height": -9999,
      "schema:width": -9999
    }
  }
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/STEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-HF5000",
  "@type": [
    "ada:STEMImage"
  ],
  "ada:componentType": "ada:STEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:stemTAPP-HF5000",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Maizey; Beau",
  "ada:analysisStartDate": "2024-05-16",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "missing",
  "ada:magnification": 14000,
  "ada:dwellTimePerProbePosition": 4,
  "ada:cameraLength": 37,
  "ada:stageXPosition": -0.1375,
  "ada:stageYPosition": -0.1776,
  "ada:stageTiltAlpha": 0.0,
  "ada:stageTiltBeta": 0.1,
  "ada:imagePixelSize": 0.3696,
  "ada:imageWidth": 2048,
  "ada:imageHeight": 2048,
  "schema:distribution": {
    "schema:hasPart": {
      "schema:height": -9999,
      "schema:width": -9999
    }
  }
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-HF5000> a ada:STEMImage ;
    schema1:distribution [ schema1:hasPart [ schema1:height -9999 ;
                    schema1:width -9999 ] ] ;
    schema1:measurementTechnique <ex:stemTAPP-HF5000> ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "2024-05-16" ;
    ada:analyst "Maizey; Beau" ;
    ada:cameraLength 37 ;
    ada:componentType "ada:STEMImage" ;
    ada:dwellTimePerProbePosition 4 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:imageHeight 2048 ;
    ada:imagePixelSize 3.696e-01 ;
    ada:imageWidth 2048 ;
    ada:magnification 14000 ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:stageTiltAlpha 0e+00 ;
    ada:stageTiltBeta 1e-01 ;
    ada:stageXPosition -1.375e-01 ;
    ada:stageYPosition -1.776e-01 .

<ex:stemTAPP-HF5000> schema1:identifier "missing" .


```


### detail example P1
detail instance derived from ADA n=694 | no named analyst | Lawrence Berkeley National Laboratory | FEI TitanX TEM (78 instrumentMetadata exports, dimensions only).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-P1",
  "@type": [
    "ada:STEMImage"
  ],
  "ada:componentType": "ada:STEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:stemTAPP-P1",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "2023-12-07",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "missing",
  "ada:magnification": -9999,
  "ada:dwellTimePerProbePosition": -9999,
  "ada:cameraLength": -9999,
  "ada:stageXPosition": -9999,
  "ada:stageYPosition": -9999,
  "ada:stageTiltAlpha": -9999,
  "ada:stageTiltBeta": -9999,
  "ada:imagePixelSize": 2.2766,
  "ada:imageWidth": 2048,
  "ada:imageHeight": 2048,
  "schema:distribution": {
    "schema:hasPart": {
      "schema:height": -9999,
      "schema:width": -9999
    }
  }
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/STEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-P1",
  "@type": [
    "ada:STEMImage"
  ],
  "ada:componentType": "ada:STEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:stemTAPP-P1",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "2023-12-07",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "missing",
  "ada:magnification": -9999,
  "ada:dwellTimePerProbePosition": -9999,
  "ada:cameraLength": -9999,
  "ada:stageXPosition": -9999,
  "ada:stageYPosition": -9999,
  "ada:stageTiltAlpha": -9999,
  "ada:stageTiltBeta": -9999,
  "ada:imagePixelSize": 2.2766,
  "ada:imageWidth": 2048,
  "ada:imageHeight": 2048,
  "schema:distribution": {
    "schema:hasPart": {
      "schema:height": -9999,
      "schema:width": -9999
    }
  }
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-P1> a ada:STEMImage ;
    schema1:distribution [ schema1:hasPart [ schema1:height -9999 ;
                    schema1:width -9999 ] ] ;
    schema1:measurementTechnique <ex:stemTAPP-P1> ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "2023-12-07" ;
    ada:analyst "missing" ;
    ada:cameraLength -9999 ;
    ada:componentType "ada:STEMImage" ;
    ada:dwellTimePerProbePosition -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:imageHeight 2048 ;
    ada:imagePixelSize 2.2766e+00 ;
    ada:imageWidth 2048 ;
    ada:magnification -9999 ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:stageTiltAlpha -9999 ;
    ada:stageTiltBeta -9999 ;
    ada:stageXPosition -9999 ;
    ada:stageYPosition -9999 .

<ex:stemTAPP-P1> schema1:identifier "missing" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Scanning Transmission Electron Microscopy Analysis Detail
description: Detail block for STEM hasPart items. Image pixel size and image dimensions
  are the only properties both laboratories record, and the pixel size appears in
  m, nm and um, so it needs normalising before values are compared.
allOf:
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/AnalysisIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/calibrationFactor/schema.yaml#/$defs/AnalysisIdentification
- type: object
  properties:
    prov:wasGeneratedBy:
      type: array
      items:
        type: object
        properties:
          schema:additionalProperty:
            type: array
            items:
              anyOf:
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_samplingUnitSelectionCriteria
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Analysis_constantsReferenceValues
              - title: Dwell Time per Probe Position
                description: Dwell time per scanned probe position.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/stemTAPP/dwellTimePerProbePosition
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/stemTAPP/dwellTimePerProbePosition
                  schema:name:
                    const: Dwell Time per Probe Position
                  schema:value:
                    anyOf:
                    - type: number
                    - type: string
                  schema:unitText:
                    type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
                - schema:unitText
              - title: Stage X Position
                description: Stage X position.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/stemTAPP/stageXPosition
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/stemTAPP/stageXPosition
                  schema:name:
                    const: Stage X Position
                  schema:value:
                    anyOf:
                    - type: number
                    - type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - title: Stage Y Position
                description: Stage Y position.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/stemTAPP/stageYPosition
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/stemTAPP/stageYPosition
                  schema:name:
                    const: Stage Y Position
                  schema:value:
                    anyOf:
                    - type: number
                    - type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - title: Stage Tilt Alpha
                description: Primary stage tilt.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/stemTAPP/stageTiltAlpha
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/stemTAPP/stageTiltAlpha
                  schema:name:
                    const: Stage Tilt Alpha
                  schema:value:
                    anyOf:
                    - type: number
                    - type: string
                  schema:unitText:
                    type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
                - schema:unitText
              - title: Stage Tilt Beta
                description: Secondary stage tilt.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/stemTAPP/stageTiltBeta
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/stemTAPP/stageTiltBeta
                  schema:name:
                    const: Stage Tilt Beta
                  schema:value:
                    anyOf:
                    - type: number
                    - type: string
                  schema:unitText:
                    type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
                - schema:unitText
            allOf:
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_samplingUnitSelectionCriteria
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Analysis_constantsReferenceValues
              minContains: 0
              maxContains: 1
            - contains:
                title: Dwell Time per Probe Position
                description: Dwell time per scanned probe position.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/stemTAPP/dwellTimePerProbePosition
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/stemTAPP/dwellTimePerProbePosition
                  schema:name:
                    const: Dwell Time per Probe Position
                  schema:value:
                    anyOf:
                    - type: number
                    - type: string
                  schema:unitText:
                    type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
                - schema:unitText
              minContains: 0
              maxContains: 1
            - contains:
                title: Stage X Position
                description: Stage X position.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/stemTAPP/stageXPosition
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/stemTAPP/stageXPosition
                  schema:name:
                    const: Stage X Position
                  schema:value:
                    anyOf:
                    - type: number
                    - type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              minContains: 0
              maxContains: 1
            - contains:
                title: Stage Y Position
                description: Stage Y position.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/stemTAPP/stageYPosition
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/stemTAPP/stageYPosition
                  schema:name:
                    const: Stage Y Position
                  schema:value:
                    anyOf:
                    - type: number
                    - type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              minContains: 0
              maxContains: 1
            - contains:
                title: Stage Tilt Alpha
                description: Primary stage tilt.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/stemTAPP/stageTiltAlpha
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/stemTAPP/stageTiltAlpha
                  schema:name:
                    const: Stage Tilt Alpha
                  schema:value:
                    anyOf:
                    - type: number
                    - type: string
                  schema:unitText:
                    type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
                - schema:unitText
              minContains: 0
              maxContains: 1
            - contains:
                title: Stage Tilt Beta
                description: Secondary stage tilt.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/stemTAPP/stageTiltBeta
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/stemTAPP/stageTiltBeta
                  schema:name:
                    const: Stage Tilt Beta
                  schema:value:
                    anyOf:
                    - type: number
                    - type: string
                  schema:unitText:
                    type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
                - schema:unitText
              minContains: 0
              maxContains: 1
          schema:object:
            type: array
            items:
              type: object
              allOf:
              - if:
                  properties:
                    '@type':
                      contains:
                        const: https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample
                  required:
                  - '@type'
                then:
                  properties:
                    schema:additionalProperty:
                      type: array
                      items:
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_preAnalysisImagingAndScreening
                      allOf:
                      - contains:
                          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_preAnalysisImagingAndScreening
                        minContains: 0
                        maxContains: 1
          prov:used:
            type: array
            items:
              type: object
              allOf:
              - if:
                  required:
                  - schema:instrument
                then:
                  properties:
                    schema:instrument:
                      type: array
                      items:
                        allOf:
                        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/instrument/schema.yaml
                        - type: object
                          allOf:
                          - if:
                              properties:
                                schema:additionalType:
                                  contains:
                                    const: STEM
                              required:
                              - schema:additionalType
                            then:
                              properties:
                                schema:additionalProperty:
                                  type: array
                                  items:
                                    anyOf:
                                    - title: Magnification
                                      description: Nominal magnification.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/stemTAPP/magnification
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/stemTAPP/magnification
                                        schema:name:
                                          const: Magnification
                                        schema:value:
                                          anyOf:
                                          - type: number
                                          - type: string
                                      required:
                                      - '@id'
                                      - '@type'
                                      - schema:propertyID
                                      - schema:name
                                      - schema:value
                                    - title: Camera Length
                                      description: Camera length.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/stemTAPP/cameraLength
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/stemTAPP/cameraLength
                                        schema:name:
                                          const: Camera Length
                                        schema:value:
                                          anyOf:
                                          - type: number
                                          - type: string
                                        schema:unitText:
                                          type: string
                                      required:
                                      - '@id'
                                      - '@type'
                                      - schema:propertyID
                                      - schema:name
                                      - schema:value
                                      - schema:unitText
                                  allOf:
                                  - contains:
                                      title: Magnification
                                      description: Nominal magnification.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/stemTAPP/magnification
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/stemTAPP/magnification
                                        schema:name:
                                          const: Magnification
                                        schema:value:
                                          anyOf:
                                          - type: number
                                          - type: string
                                      required:
                                      - '@id'
                                      - '@type'
                                      - schema:propertyID
                                      - schema:name
                                      - schema:value
                                    minContains: 0
                                    maxContains: 1
                                  - contains:
                                      title: Camera Length
                                      description: Camera length.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/stemTAPP/cameraLength
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/stemTAPP/cameraLength
                                        schema:name:
                                          const: Camera Length
                                        schema:value:
                                          anyOf:
                                          - type: number
                                          - type: string
                                        schema:unitText:
                                          type: string
                                      required:
                                      - '@id'
                                      - '@type'
                                      - schema:propertyID
                                      - schema:name
                                      - schema:value
                                      - schema:unitText
                                    minContains: 0
                                    maxContains: 1
                      allOf:
                      - contains:
                          properties:
                            schema:additionalType:
                              contains:
                                const: STEM
                          required:
                          - schema:additionalType
    schema:distribution:
      type: object
      properties:
        schema:hasPart:
          type: object
          properties:
            schema:width:
              description: Image width in pixels.
              anyOf:
              - type: integer
              - type: string
            schema:height:
              description: Image height in pixels.
              anyOf:
              - type: integer
              - type: string
          required:
          - schema:height
          - schema:width
      required:
      - schema:hasPart
  required:
  - schema:distribution

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/STEM/detail/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/STEM/detail/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "ada": "https://ada.astromat.org/metadata/",
    "bios": "https://bioschemas.org/",
    "prov": "http://www.w3.org/ns/prov#",
    "schema": "http://schema.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "spdx": "http://spdx.org/rdf/terms#",
    "nxs": "https://manual.nexusformat.org/classes/",
    "dcterms": "http://purl.org/dc/terms/",
    "geosparql": "http://www.opengis.net/ont/geosparql#",
    "dqv": "http://www.w3.org/ns/dqv#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "wd": "https://www.wikidata.org/entity/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/STEM/detail/context.jsonld)

## Sources

* [STEM_TAPP_draft_v2.csv (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/STEM/detail`

