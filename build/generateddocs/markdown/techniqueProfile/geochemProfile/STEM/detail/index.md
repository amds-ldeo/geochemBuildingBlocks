
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
    "ada": "https://ada.astromat.org/metadata/",
    "ex": "https://example.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/",
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@id": "ex:stemTAPP-detail-HF5000",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:instrument": [
        {
          "schema:additionalType": [
            "STEM",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/stemTAPP/magnification",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/stemTAPP/magnification"
                }
              ],
              "schema:name": "Magnification",
              "schema:value": 14000
            },
            {
              "@id": "ada:parameter/stemTAPP/cameraLength",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/stemTAPP/cameraLength"
                }
              ],
              "schema:name": "Camera Length",
              "schema:value": 37,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "37 mm"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:stemTAPP-detail-HF5000/instrument/STEM"
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/stemTAPP/dwellTimePerProbePosition",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/stemTAPP/dwellTimePerProbePosition"
            }
          ],
          "schema:name": "Dwell Time per Probe Position",
          "schema:value": 4,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "4e-06 s"
        },
        {
          "@id": "ada:parameter/stemTAPP/stageXPosition",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/stemTAPP/stageXPosition"
            }
          ],
          "schema:name": "Stage X Position",
          "schema:value": -0.1375
        },
        {
          "@id": "ada:parameter/stemTAPP/stageYPosition",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/stemTAPP/stageYPosition"
            }
          ],
          "schema:name": "Stage Y Position",
          "schema:value": -0.1776
        },
        {
          "@id": "ada:parameter/stemTAPP/stageTiltAlpha",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/stemTAPP/stageTiltAlpha"
            }
          ],
          "schema:name": "Stage Tilt Alpha",
          "schema:value": 0.0,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "0.0 deg"
        },
        {
          "@id": "ada:parameter/stemTAPP/stageTiltBeta",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/stemTAPP/stageTiltBeta"
            }
          ],
          "schema:name": "Stage Tilt Beta",
          "schema:value": 0.1,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "0.1 deg"
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "University of Arizona",
        "schema:identifier": "https://ror.org/03m2x1q45"
      },
      "schema:startTime": "2024-05-16",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier"
    }
  ],
  "schema:distribution": {
    "schema:hasPart": {
      "schema:width": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 2048,
        "schema:unitText": "pixel"
      },
      "schema:height": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 2048,
        "schema:unitText": "pixel"
      }
    }
  },
  "schema:contributor": [
    {
      "schema:roleName": "analyst",
      "schema:contributor": {
        "schema:name": "Maizey; Beau"
      }
    }
  ],
  "ada:analyticalMode": [
    "STEM"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Maizey; Beau",
  "ada:analysisStartDate": "2024-05-16",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "missing",
  "ada:imagePixelSize": 0.3696
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
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:stemTAPP-detail-HF5000",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:instrument": [
        {
          "schema:additionalType": [
            "STEM",
            {
              "@id": "https://www.wikidata.org/entity/Q3099911"
            }
          ],
          "schema:additionalProperty": [
            {
              "@id": "ada:parameter/stemTAPP/magnification",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/stemTAPP/magnification"
                }
              ],
              "schema:name": "Magnification",
              "schema:value": 14000
            },
            {
              "@id": "ada:parameter/stemTAPP/cameraLength",
              "@type": [
                "schema:PropertyValue"
              ],
              "schema:propertyID": [
                {
                  "@id": "ada:parameter/stemTAPP/cameraLength"
                }
              ],
              "schema:name": "Camera Length",
              "schema:value": 37,
              "schema:unitText": "no value available: unnamed property",
              "schema:description": "37 mm"
            }
          ],
          "@type": [
            "schema:Product",
            "schema:Thing"
          ],
          "schema:name": "no value available: schema:name",
          "@id": "ex:stemTAPP-detail-HF5000/instrument/STEM"
        }
      ],
      "schema:additionalProperty": [
        {
          "@id": "ada:parameter/stemTAPP/dwellTimePerProbePosition",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/stemTAPP/dwellTimePerProbePosition"
            }
          ],
          "schema:name": "Dwell Time per Probe Position",
          "schema:value": 4,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "4e-06 s"
        },
        {
          "@id": "ada:parameter/stemTAPP/stageXPosition",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/stemTAPP/stageXPosition"
            }
          ],
          "schema:name": "Stage X Position",
          "schema:value": -0.1375
        },
        {
          "@id": "ada:parameter/stemTAPP/stageYPosition",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/stemTAPP/stageYPosition"
            }
          ],
          "schema:name": "Stage Y Position",
          "schema:value": -0.1776
        },
        {
          "@id": "ada:parameter/stemTAPP/stageTiltAlpha",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/stemTAPP/stageTiltAlpha"
            }
          ],
          "schema:name": "Stage Tilt Alpha",
          "schema:value": 0.0,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "0.0 deg"
        },
        {
          "@id": "ada:parameter/stemTAPP/stageTiltBeta",
          "@type": [
            "schema:PropertyValue"
          ],
          "schema:propertyID": [
            {
              "@id": "ada:parameter/stemTAPP/stageTiltBeta"
            }
          ],
          "schema:name": "Stage Tilt Beta",
          "schema:value": 0.1,
          "schema:unitText": "no value available: unnamed property",
          "schema:description": "0.1 deg"
        }
      ],
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "University of Arizona",
        "schema:identifier": "https://ror.org/03m2x1q45"
      },
      "schema:startTime": "2024-05-16",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier"
    }
  ],
  "schema:distribution": {
    "schema:hasPart": {
      "schema:width": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 2048,
        "schema:unitText": "pixel"
      },
      "schema:height": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 2048,
        "schema:unitText": "pixel"
      }
    }
  },
  "schema:contributor": [
    {
      "schema:roleName": "analyst",
      "schema:contributor": {
        "schema:name": "Maizey; Beau"
      }
    }
  ],
  "ada:analyticalMode": [
    "STEM"
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Maizey; Beau",
  "ada:analysisStartDate": "2024-05-16",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "missing",
  "ada:imagePixelSize": 0.3696
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix wd: <https://www.wikidata.org/entity/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:stemTAPP-detail-HF5000 a schema1:Dataset,
        schema1:Product ;
    schema1:contributor [ schema1:contributor [ schema1:name "Maizey; Beau" ] ;
            schema1:roleName "analyst" ] ;
    schema1:distribution [ schema1:hasPart [ schema1:height [ a schema1:QuantitativeValue ;
                            schema1:unitText "pixel" ;
                            schema1:value 2048 ] ;
                    schema1:width [ a schema1:QuantitativeValue ;
                            schema1:unitText "pixel" ;
                            schema1:value 2048 ] ] ] ;
    prov:wasGeneratedBy [ schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/stemTAPP/dwellTimePerProbePosition>,
                <https://ada.astromat.org/metadata/parameter/stemTAPP/stageTiltAlpha>,
                <https://ada.astromat.org/metadata/parameter/stemTAPP/stageTiltBeta>,
                <https://ada.astromat.org/metadata/parameter/stemTAPP/stageXPosition>,
                <https://ada.astromat.org/metadata/parameter/stemTAPP/stageYPosition> ;
            schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:instrument <https://example.org/stemTAPP-detail-HF5000/instrument/STEM> ;
            schema1:location [ a schema1:Place ;
                    schema1:identifier "https://ror.org/03m2x1q45" ;
                    schema1:name "University of Arizona" ] ;
            schema1:startTime "2024-05-16" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "2024-05-16" ;
    ada:analyst "Maizey; Beau" ;
    ada:analyticalMode "STEM" ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:imagePixelSize 3.696e-01 ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "missing" ;
    ada:sessionIdentifier "missing" .

<https://example.org/stemTAPP-detail-HF5000/instrument/STEM> a schema1:Product,
        schema1:Thing ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/stemTAPP/cameraLength>,
        <https://ada.astromat.org/metadata/parameter/stemTAPP/magnification> ;
    schema1:additionalType wd:Q3099911,
        "STEM" ;
    schema1:name "no value available: schema:name" .

<https://ada.astromat.org/metadata/parameter/stemTAPP/cameraLength> a schema1:PropertyValue ;
    schema1:description "37 mm" ;
    schema1:name "Camera Length" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/stemTAPP/cameraLength> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 37 .

<https://ada.astromat.org/metadata/parameter/stemTAPP/dwellTimePerProbePosition> a schema1:PropertyValue ;
    schema1:description "4e-06 s" ;
    schema1:name "Dwell Time per Probe Position" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/stemTAPP/dwellTimePerProbePosition> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 4 .

<https://ada.astromat.org/metadata/parameter/stemTAPP/magnification> a schema1:PropertyValue ;
    schema1:name "Magnification" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/stemTAPP/magnification> ;
    schema1:value 14000 .

<https://ada.astromat.org/metadata/parameter/stemTAPP/stageTiltAlpha> a schema1:PropertyValue ;
    schema1:description "0.0 deg" ;
    schema1:name "Stage Tilt Alpha" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/stemTAPP/stageTiltAlpha> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 0e+00 .

<https://ada.astromat.org/metadata/parameter/stemTAPP/stageTiltBeta> a schema1:PropertyValue ;
    schema1:description "0.1 deg" ;
    schema1:name "Stage Tilt Beta" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/stemTAPP/stageTiltBeta> ;
    schema1:unitText "no value available: unnamed property" ;
    schema1:value 1e-01 .

<https://ada.astromat.org/metadata/parameter/stemTAPP/stageXPosition> a schema1:PropertyValue ;
    schema1:name "Stage X Position" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/stemTAPP/stageXPosition> ;
    schema1:value -1.375e-01 .

<https://ada.astromat.org/metadata/parameter/stemTAPP/stageYPosition> a schema1:PropertyValue ;
    schema1:name "Stage Y Position" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/stemTAPP/stageYPosition> ;
    schema1:value -1.776e-01 .


```


### detail example P1
detail instance derived from ADA n=694 | no named analyst | Lawrence Berkeley National Laboratory | FEI TitanX TEM (78 instrumentMetadata exports, dimensions only).
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
  "@id": "ex:stemTAPP-detail-P1",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:distribution": {
    "schema:hasPart": {
      "schema:width": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 2048,
        "schema:unitText": "pixel"
      },
      "schema:height": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 2048,
        "schema:unitText": "pixel"
      }
    }
  },
  "prov:wasGeneratedBy": [
    {
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Lawrence Berkeley National Laboratory",
        "schema:identifier": "https://ror.org/02jbv0t02"
      },
      "schema:startTime": "2023-12-07",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier"
    }
  ],
  "ada:analyticalMode": [
    "STEM"
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
  "ada:imagePixelSize": 2.2766
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
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:stemTAPP-detail-P1",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "schema:distribution": {
    "schema:hasPart": {
      "schema:width": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 2048,
        "schema:unitText": "pixel"
      },
      "schema:height": {
        "@type": [
          "schema:QuantitativeValue"
        ],
        "schema:value": 2048,
        "schema:unitText": "pixel"
      }
    }
  },
  "prov:wasGeneratedBy": [
    {
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Lawrence Berkeley National Laboratory",
        "schema:identifier": "https://ror.org/02jbv0t02"
      },
      "schema:startTime": "2023-12-07",
      "schema:endTime": "no value available: schema:endTime",
      "schema:identifier": "no value available: schema:identifier"
    }
  ],
  "ada:analyticalMode": [
    "STEM"
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
  "ada:imagePixelSize": 2.2766
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:stemTAPP-detail-P1 a schema1:Dataset,
        schema1:Product ;
    schema1:distribution [ schema1:hasPart [ schema1:height [ a schema1:QuantitativeValue ;
                            schema1:unitText "pixel" ;
                            schema1:value 2048 ] ;
                    schema1:width [ a schema1:QuantitativeValue ;
                            schema1:unitText "pixel" ;
                            schema1:value 2048 ] ] ] ;
    prov:wasGeneratedBy [ schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "no value available: schema:identifier" ;
            schema1:location [ a schema1:Place ;
                    schema1:identifier "https://ror.org/02jbv0t02" ;
                    schema1:name "Lawrence Berkeley National Laboratory" ] ;
            schema1:startTime "2023-12-07" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "2023-12-07" ;
    ada:analyst "missing" ;
    ada:analyticalMode "STEM" ;
    ada:cameraLength -9999 ;
    ada:dwellTimePerProbePosition -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:imagePixelSize 2.2766e+00 ;
    ada:magnification -9999 ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:stageTiltAlpha -9999 ;
    ada:stageTiltBeta -9999 ;
    ada:stageXPosition -9999 ;
    ada:stageYPosition -9999 .


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
          schema:instrument:
            type: array
            items:
              type: object
              allOf:
              - if:
                  $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/KindInstrument
                then:
                  $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/instrument/schema.yaml
              - if:
                  $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/KindSoftware
                then:
                  $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/geochemBaseProfile/schema.yaml#/$defs/UsedComputationalTool
              - if:
                  $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/KindReagent
                then:
                  $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/geochemBaseProfile/schema.yaml#/$defs/UsedReagent
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
      title: Analysis Events
    schema:distribution:
      type: object
      properties:
        schema:hasPart:
          type: object
          properties:
            schema:width:
              description: Image width in pixels.
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
                  type: integer
                schema:unitText:
                  type: string
            schema:height:
              description: Image height in pixels.
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
                  type: integer
                schema:unitText:
                  type: string
          required:
          - schema:height
          - schema:width
      title: Distributions
x-bblocks-metadata:
  itemIdentifier: ogch.techniqueProfile.geochemProfile.STEM.detail
  register: https://amds-ldeo.github.io/geochemBuildingBlocks/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-11'

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/STEM/detail/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/STEM/detail/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "ada": "https://ada.astromat.org/metadata/",
    "prov": "http://www.w3.org/ns/prov#",
    "schema": "http://schema.org/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "wd": "https://www.wikidata.org/entity/",
    "nxs": "https://manual.nexusformat.org/classes/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "bios": "https://bioschemas.org/",
    "spdx": "http://spdx.org/rdf/terms#",
    "dcterms": "http://purl.org/dc/terms/",
    "geosparql": "http://www.opengis.net/ont/geosparql#",
    "dqv": "http://www.w3.org/ns/dqv#",
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

