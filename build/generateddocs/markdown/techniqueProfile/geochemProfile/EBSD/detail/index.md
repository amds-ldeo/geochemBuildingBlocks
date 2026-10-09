
# Electron Backscatter Diffraction Analysis Detail (Schema)

`ogch.techniqueProfile.geochemProfile.EBSD.detail` *v0.1*

Detail block for EBSD hasPart items. The per-analysis properties are working distance, camera exposure time, map step size and indexing rate; the map step size is usually given in the source's per-sample tables rather than its prose.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### detail example P0
detail instance derived from ADA n=1354 | Nicholas E Timms | Curtin University | Tescan MIRA3 (14 method-description documents).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-P0",
  "@type": [
    "ada:SEMEBSDGrainImageMap"
  ],
  "ada:componentType": "ada:SEMEBSDGrainImageMap",
  "schema:measurementTechnique": [
    {
      "@id": "ex:ebsdTAPP-P0",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Nicholas E Timms",
  "ada:analysisStartDate": "2023-11-16",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "missing",
  "ada:workingDistance": 17.8,
  "ada:ebsdCameraExposureTime": 20,
  "ada:mapStepSize": 60,
  "ada:ebsdIndexingRate": "~45-1005 points per second"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EBSD/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-P0",
  "@type": [
    "ada:SEMEBSDGrainImageMap"
  ],
  "ada:componentType": "ada:SEMEBSDGrainImageMap",
  "schema:measurementTechnique": [
    {
      "@id": "ex:ebsdTAPP-P0",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Nicholas E Timms",
  "ada:analysisStartDate": "2023-11-16",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "missing",
  "ada:workingDistance": 17.8,
  "ada:ebsdCameraExposureTime": 20,
  "ada:mapStepSize": 60,
  "ada:ebsdIndexingRate": "~45-1005 points per second"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-P0> a ada:SEMEBSDGrainImageMap ;
    schema1:measurementTechnique <ex:ebsdTAPP-P0> ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "2023-11-16" ;
    ada:analyst "Nicholas E Timms" ;
    ada:componentType "ada:SEMEBSDGrainImageMap" ;
    ada:ebsdCameraExposureTime 20 ;
    ada:ebsdIndexingRate "~45-1005 points per second" ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:mapStepSize 60 ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:workingDistance 1.78e+01 .

<ex:ebsdTAPP-P0> schema1:identifier "missing" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Electron Backscatter Diffraction Analysis Detail
description: Detail block for EBSD hasPart items. The per-analysis properties are
  working distance, camera exposure time, map step size and indexing rate; the map
  step size is usually given in the source's per-sample tables rather than its prose.
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
              - title: EBSD Camera Exposure Time
                description: Exposure time per EBSD pattern.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/ebsdTAPP/ebsdCameraExposureTime
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/ebsdTAPP/ebsdCameraExposureTime
                  schema:name:
                    const: EBSD Camera Exposure Time
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
              - title: Hough Resolution
                description: Hough transform resolution used for band detection.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/ebsdTAPP/houghResolution
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/ebsdTAPP/houghResolution
                  schema:name:
                    const: Hough Resolution
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
              - title: Map Step Size
                description: Step size of the EBSD map.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/ebsdTAPP/mapStepSize
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/ebsdTAPP/mapStepSize
                  schema:name:
                    const: Map Step Size
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
              - title: EBSD Indexing Rate
                description: Pattern collection and indexing rate.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/ebsdTAPP/ebsdIndexingRate
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/ebsdTAPP/ebsdIndexingRate
                  schema:name:
                    const: EBSD Indexing Rate
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
              - title: EDS Channels
                description: Number of channels EDS spectra are collected on.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/ebsdTAPP/edsChannels
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/ebsdTAPP/edsChannels
                  schema:name:
                    const: EDS Channels
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
              - title: EDS Process Time
                description: AZtec process time setting for EDS.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/ebsdTAPP/edsProcessTime
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/ebsdTAPP/edsProcessTime
                  schema:name:
                    const: EDS Process Time
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
              - title: Crystal Structure File Sources
                description: Databases the match units / crystal structure files were
                  drawn from.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/ebsdTAPP/crystalStructureFileSources
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/ebsdTAPP/crystalStructureFileSources
                  schema:name:
                    const: Crystal Structure File Sources
                  schema:value:
                    type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
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
                title: EBSD Camera Exposure Time
                description: Exposure time per EBSD pattern.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/ebsdTAPP/ebsdCameraExposureTime
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/ebsdTAPP/ebsdCameraExposureTime
                  schema:name:
                    const: EBSD Camera Exposure Time
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
                title: Hough Resolution
                description: Hough transform resolution used for band detection.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/ebsdTAPP/houghResolution
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/ebsdTAPP/houghResolution
                  schema:name:
                    const: Hough Resolution
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
                title: Map Step Size
                description: Step size of the EBSD map.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/ebsdTAPP/mapStepSize
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/ebsdTAPP/mapStepSize
                  schema:name:
                    const: Map Step Size
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
                title: EBSD Indexing Rate
                description: Pattern collection and indexing rate.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/ebsdTAPP/ebsdIndexingRate
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/ebsdTAPP/ebsdIndexingRate
                  schema:name:
                    const: EBSD Indexing Rate
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
                title: EDS Channels
                description: Number of channels EDS spectra are collected on.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/ebsdTAPP/edsChannels
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/ebsdTAPP/edsChannels
                  schema:name:
                    const: EDS Channels
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
                title: EDS Process Time
                description: AZtec process time setting for EDS.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/ebsdTAPP/edsProcessTime
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/ebsdTAPP/edsProcessTime
                  schema:name:
                    const: EDS Process Time
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
                title: Crystal Structure File Sources
                description: Databases the match units / crystal structure files were
                  drawn from.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/ebsdTAPP/crystalStructureFileSources
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/ebsdTAPP/crystalStructureFileSources
                  schema:name:
                    const: Crystal Structure File Sources
                  schema:value:
                    type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
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
                                    const: SEM
                                  schema:inDefinedTermSet: ada:vocab/instrumentType
                              required:
                              - schema:additionalType
                            then:
                              properties:
                                schema:additionalProperty:
                                  type: array
                                  items:
                                    anyOf:
                                    - title: Accelerating Voltage
                                      description: Electron beam accelerating voltage.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/ebsdTAPP/acceleratingVoltage
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/ebsdTAPP/acceleratingVoltage
                                        schema:name:
                                          const: Accelerating Voltage
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
                                    - title: Beam Current
                                      description: Beam current at the sample.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/ebsdTAPP/beamCurrent
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/ebsdTAPP/beamCurrent
                                        schema:name:
                                          const: Beam Current
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
                                    - title: Working Distance
                                      description: Working distance during mapping.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/ebsdTAPP/workingDistance
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/ebsdTAPP/workingDistance
                                        schema:name:
                                          const: Working Distance
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
                                      title: Accelerating Voltage
                                      description: Electron beam accelerating voltage.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/ebsdTAPP/acceleratingVoltage
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/ebsdTAPP/acceleratingVoltage
                                        schema:name:
                                          const: Accelerating Voltage
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
                                      title: Beam Current
                                      description: Beam current at the sample.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/ebsdTAPP/beamCurrent
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/ebsdTAPP/beamCurrent
                                        schema:name:
                                          const: Beam Current
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
                                      title: Working Distance
                                      description: Working distance during mapping.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/ebsdTAPP/workingDistance
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/ebsdTAPP/workingDistance
                                        schema:name:
                                          const: Working Distance
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
                                const: SEM
                              schema:inDefinedTermSet: ada:vocab/instrumentType
                          required:
                          - schema:additionalType

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EBSD/detail/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EBSD/detail/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EBSD/detail/context.jsonld)

## Sources

* [EBSD_TAPP_draft_v2.csv (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/EBSD/detail`

