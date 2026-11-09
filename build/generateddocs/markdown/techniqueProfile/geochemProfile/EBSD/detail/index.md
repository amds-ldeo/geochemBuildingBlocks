
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
    "ada": "https://ada.astromat.org/metadata/",
    "ex": "https://example.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/",
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@id": "ex:ebsdTAPP-detail-P0",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "SEM",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/ebsdTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/ebsdTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 20,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "20 kV"
                },
                {
                  "@id": "ada:parameter/ebsdTAPP/beamCurrent",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/ebsdTAPP/beamCurrent"
                    }
                  ],
                  "schema:name": "Beam Current",
                  "schema:value": 1.5,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "~1.5 nA"
                },
                {
                  "@id": "ada:parameter/ebsdTAPP/workingDistance",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/ebsdTAPP/workingDistance"
                    }
                  ],
                  "schema:name": "Working Distance",
                  "schema:value": 17.8,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "17.8-18.3 mm"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:ebsdTAPP-detail-P0/instrument/SEM"
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "acquisition",
              "schema:name": "Oxford Instruments AZtec v5.1 Symmetry",
              "@type": [
                "schema:SoftwareApplication"
              ]
            },
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "AZtecCrystal",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/ebsdTAPP/ebsdCameraExposureTime",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/ebsdTAPP/ebsdCameraExposureTime"
            }
          ],
          "schema:name": "EBSD Camera Exposure Time",
          "schema:value": 20,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "20-25 ms"
        },
        {
          "@id": "ada:parameter/ebsdTAPP/houghResolution",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/ebsdTAPP/houghResolution"
            }
          ],
          "schema:name": "Hough Resolution",
          "schema:value": 60
        },
        {
          "@id": "ada:parameter/ebsdTAPP/mapStepSize",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/ebsdTAPP/mapStepSize"
            }
          ],
          "schema:name": "Map Step Size",
          "schema:value": 60,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "60-600 nm"
        },
        {
          "@id": "ada:parameter/ebsdTAPP/ebsdIndexingRate",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/ebsdTAPP/ebsdIndexingRate"
            }
          ],
          "schema:name": "EBSD Indexing Rate",
          "schema:value": 45,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "~45-1005 points per second"
        },
        {
          "@id": "ada:parameter/ebsdTAPP/edsChannels",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/ebsdTAPP/edsChannels"
            }
          ],
          "schema:name": "EDS Channels",
          "schema:value": 2024
        },
        {
          "@id": "ada:parameter/ebsdTAPP/edsProcessTime",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/ebsdTAPP/edsProcessTime"
            }
          ],
          "schema:name": "EDS Process Time",
          "schema:value": 5
        },
        {
          "@id": "ada:parameter/ebsdTAPP/crystalStructureFileSources",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/ebsdTAPP/crystalStructureFileSources"
            }
          ],
          "schema:name": "Crystal Structure File Sources",
          "schema:value": "HKL; ICSD; American Mineralogist"
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Curtin University",
        "schema:identifier": "https://ror.org/02n415q13"
      },
      "schema:startTime": "2023-11-16",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "FIB-milled (Tescan LYRA3); 5 nm evaporative carbon coat",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier"
    }
  ],
  "schema:contributor": [
    {
      "schema:roleName": "analyst",
      "schema:contributor": {
        "schema:name": "Nicholas E Timms"
      }
    }
  ],
  "ada:analyticalMode": [
    "Simultaneous EBSD-EDS mapping"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Nicholas E Timms",
  "ada:analysisStartDate": "2023-11-16",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "missing"
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
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:ebsdTAPP-detail-P0",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "prov:used": [
        {
          "schema:instrument": [
            {
              "schema:additionalType": [
                "SEM",
                {
                  "@id": "https://www.wikidata.org/wiki/Q3099911"
                }
              ],
              "schema:additionalProperty": [
                {
                  "@id": "ada:parameter/ebsdTAPP/acceleratingVoltage",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/ebsdTAPP/acceleratingVoltage"
                    }
                  ],
                  "schema:name": "Accelerating Voltage",
                  "schema:value": 20,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "20 kV"
                },
                {
                  "@id": "ada:parameter/ebsdTAPP/beamCurrent",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/ebsdTAPP/beamCurrent"
                    }
                  ],
                  "schema:name": "Beam Current",
                  "schema:value": 1.5,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "~1.5 nA"
                },
                {
                  "@id": "ada:parameter/ebsdTAPP/workingDistance",
                  "@type": [
                    "schema:PropertyValue"
                  ],
                  "schema:propertyID": [
                    {
                      "@id": "ada:parameter/ebsdTAPP/workingDistance"
                    }
                  ],
                  "schema:name": "Working Distance",
                  "schema:value": 17.8,
                  "schema:unitText": "no value available: unnamed property",
                  "schema:description": "17.8-18.3 mm"
                }
              ],
              "@type": [
                "schema:Product",
                "schema:Thing"
              ],
              "schema:name": "no value available: schema:name",
              "@id": "ex:ebsdTAPP-detail-P0/instrument/SEM"
            }
          ]
        },
        {
          "bios:computationalTool": [
            {
              "ada:toolRole": "acquisition",
              "schema:name": "Oxford Instruments AZtec v5.1 Symmetry",
              "@type": [
                "schema:SoftwareApplication"
              ]
            },
            {
              "ada:toolRole": "dataReduction",
              "schema:name": "AZtecCrystal",
              "@type": [
                "schema:SoftwareApplication"
              ]
            }
          ]
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/ebsdTAPP/ebsdCameraExposureTime",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/ebsdTAPP/ebsdCameraExposureTime"
            }
          ],
          "schema:name": "EBSD Camera Exposure Time",
          "schema:value": 20,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "20-25 ms"
        },
        {
          "@id": "ada:parameter/ebsdTAPP/houghResolution",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/ebsdTAPP/houghResolution"
            }
          ],
          "schema:name": "Hough Resolution",
          "schema:value": 60
        },
        {
          "@id": "ada:parameter/ebsdTAPP/mapStepSize",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/ebsdTAPP/mapStepSize"
            }
          ],
          "schema:name": "Map Step Size",
          "schema:value": 60,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "60-600 nm"
        },
        {
          "@id": "ada:parameter/ebsdTAPP/ebsdIndexingRate",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/ebsdTAPP/ebsdIndexingRate"
            }
          ],
          "schema:name": "EBSD Indexing Rate",
          "schema:value": 45,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "~45-1005 points per second"
        },
        {
          "@id": "ada:parameter/ebsdTAPP/edsChannels",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/ebsdTAPP/edsChannels"
            }
          ],
          "schema:name": "EDS Channels",
          "schema:value": 2024
        },
        {
          "@id": "ada:parameter/ebsdTAPP/edsProcessTime",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/ebsdTAPP/edsProcessTime"
            }
          ],
          "schema:name": "EDS Process Time",
          "schema:value": 5
        },
        {
          "@id": "ada:parameter/ebsdTAPP/crystalStructureFileSources",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/ebsdTAPP/crystalStructureFileSources"
            }
          ],
          "schema:name": "Crystal Structure File Sources",
          "schema:value": "HKL; ICSD; American Mineralogist"
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Curtin University",
        "schema:identifier": "https://ror.org/02n415q13"
      },
      "schema:startTime": "2023-11-16",
      "schema:actionProcess": {
        "schema:step": [
          {
            "schema:name": "Sample preparation",
            "schema:description": "FIB-milled (Tescan LYRA3); 5 nm evaporative carbon coat",
            "@type": [
              "cdi:Activity",
              "schema:Action",
              "schema:HowToStep"
            ],
            "schema:position": 1
          }
        ]
      },
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier"
    }
  ],
  "schema:contributor": [
    {
      "schema:roleName": "analyst",
      "schema:contributor": {
        "schema:name": "Nicholas E Timms"
      }
    }
  ],
  "ada:analyticalMode": [
    "Simultaneous EBSD-EDS mapping"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Nicholas E Timms",
  "ada:analysisStartDate": "2023-11-16",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix bios: <https://bioschemas.org/> .
@prefix cdi: <http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:ebsdTAPP-detail-P0 a schema1:Dataset,
        schema1:Product ;
    schema1:contributor [ schema1:contributor [ schema1:name "Nicholas E Timms" ] ;
            schema1:roleName "analyst" ] ;
    prov:wasGeneratedBy [ schema1:actionProcess [ schema1:step [ a cdi:Activity,
                                schema1:Action,
                                schema1:HowToStep ;
                            schema1:description "FIB-milled (Tescan LYRA3); 5 nm evaporative carbon coat" ;
                            schema1:name "Sample preparation" ;
                            schema1:position 1 ] ] ;
            schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/ebsdTAPP/crystalStructureFileSources>,
                <https://ada.astromat.org/metadata/parameter/ebsdTAPP/ebsdCameraExposureTime>,
                <https://ada.astromat.org/metadata/parameter/ebsdTAPP/ebsdIndexingRate>,
                <https://ada.astromat.org/metadata/parameter/ebsdTAPP/edsChannels>,
                <https://ada.astromat.org/metadata/parameter/ebsdTAPP/edsProcessTime>,
                <https://ada.astromat.org/metadata/parameter/ebsdTAPP/houghResolution>,
                <https://ada.astromat.org/metadata/parameter/ebsdTAPP/mapStepSize> ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:identifier "https://ror.org/02n415q13" ;
                    schema1:name "Curtin University" ] ;
            schema1:startTime "2023-11-16" ;
            prov:used [ schema1:instrument <https://example.org/ebsdTAPP-detail-P0/instrument/SEM> ],
                [ bios:computationalTool [ a schema1:SoftwareApplication ;
                            schema1:name "AZtecCrystal" ;
                            ada:toolRole "dataReduction" ],
                        [ a schema1:SoftwareApplication ;
                            schema1:name "Oxford Instruments AZtec v5.1 Symmetry" ;
                            ada:toolRole "acquisition" ] ] ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "2023-11-16" ;
    ada:analyst "Nicholas E Timms" ;
    ada:analyticalMode "Simultaneous EBSD-EDS mapping" ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "missing" ;
    ada:sessionIdentifier "missing" .

<https://example.org/ebsdTAPP-detail-P0/instrument/SEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/ebsdTAPP/acceleratingVoltage>,
        <https://ada.astromat.org/metadata/parameter/ebsdTAPP/beamCurrent>,
        <https://ada.astromat.org/metadata/parameter/ebsdTAPP/workingDistance> ;
    schema1:additionalType <https://www.wikidata.org/wiki/Q3099911>,
        "SEM" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/ebsdTAPP/acceleratingVoltage> a schema1:PropertyValue ;
    schema1:description "20 kV" ;
    schema1:name "Accelerating Voltage" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/ebsdTAPP/acceleratingVoltage> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 20 .

<https://ada.astromat.org/metadata/parameter/ebsdTAPP/beamCurrent> a schema1:PropertyValue ;
    schema1:description "~1.5 nA" ;
    schema1:name "Beam Current" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/ebsdTAPP/beamCurrent> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1.5e+00 .

<https://ada.astromat.org/metadata/parameter/ebsdTAPP/crystalStructureFileSources> a schema1:PropertyValue ;
    schema1:name "Crystal Structure File Sources" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/ebsdTAPP/crystalStructureFileSources> ;
    schema1:value "HKL; ICSD; American Mineralogist" .

<https://ada.astromat.org/metadata/parameter/ebsdTAPP/ebsdCameraExposureTime> a schema1:PropertyValue ;
    schema1:description "20-25 ms" ;
    schema1:name "EBSD Camera Exposure Time" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/ebsdTAPP/ebsdCameraExposureTime> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 20 .

<https://ada.astromat.org/metadata/parameter/ebsdTAPP/ebsdIndexingRate> a schema1:PropertyValue ;
    schema1:description "~45-1005 points per second" ;
    schema1:name "EBSD Indexing Rate" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/ebsdTAPP/ebsdIndexingRate> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 45 .

<https://ada.astromat.org/metadata/parameter/ebsdTAPP/edsChannels> a schema1:PropertyValue ;
    schema1:name "EDS Channels" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/ebsdTAPP/edsChannels> ;
    schema1:value 2024 .

<https://ada.astromat.org/metadata/parameter/ebsdTAPP/edsProcessTime> a schema1:PropertyValue ;
    schema1:name "EDS Process Time" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/ebsdTAPP/edsProcessTime> ;
    schema1:value 5 .

<https://ada.astromat.org/metadata/parameter/ebsdTAPP/houghResolution> a schema1:PropertyValue ;
    schema1:name "Hough Resolution" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/ebsdTAPP/houghResolution> ;
    schema1:value 60 .

<https://ada.astromat.org/metadata/parameter/ebsdTAPP/mapStepSize> a schema1:PropertyValue ;
    schema1:description "60-600 nm" ;
    schema1:name "Map Step Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/ebsdTAPP/mapStepSize> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 60 .

<https://ada.astromat.org/metadata/parameter/ebsdTAPP/workingDistance> a schema1:PropertyValue ;
    schema1:description "17.8-18.3 mm" ;
    schema1:name "Working Distance" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/ebsdTAPP/workingDistance> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1.78e+01 .


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
      title: Analysis Events
x-bblocks-metadata:
  itemIdentifier: ogch.techniqueProfile.geochemProfile.EBSD.detail
  register: https://amds-ldeo.github.io/geochemBuildingBlocks/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-09'

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

