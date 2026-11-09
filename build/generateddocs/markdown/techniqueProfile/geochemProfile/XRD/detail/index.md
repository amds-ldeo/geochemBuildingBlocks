
# XRD Analysis Detail (Schema)

`ogch.techniqueProfile.geochemProfile.XRD.detail` *v0.1*

Detail block for XRD hasPart items, carrying the analysis-level properties supplied per scan rather than fixed by the procedure.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### detail example King2024
detail instance derived from ADA n=2 | King2024 | Natural History Museum | (NHM)Position Sensitive Detector X-ray Diffraction.
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
  "@id": "ex:xrdTAPP-detail-King2024",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Natural History Museum",
        "schema:identifier": "https://ror.org/039zvsn29"
      },
      "schema:identifier": "20241125_xrd_nhm_orex-800117-108_1 | 20240725_xrd_nhm_orex-800107-103_1",
      "schema:startTime": "2024-07-25 | 2024-11-25",
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:name": "OREX-800117-108 | OREX-800107-103"
        }
      ],
      "schema:endTime": "no value available: schema:endTime"
    }
  ],
  "schema:contributor": [
    {
      "schema:roleName": "analyst",
      "schema:contributor": {
        "schema:name": "King, Ashley"
      }
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program."
    }
  ],
  "ada:sessionIdentifier": "20241125_xrd_nhm_orex-800117-108_1 | 20240725_xrd_nhm_orex-800107-103_1",
  "ada:analyst": "King, Ashley",
  "ada:analysisStartDate": "2024-07-25 | 2024-11-25",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program.",
  "ada:sampleName": "OREX-800117-108 | OREX-800107-103",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XRD/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:xrdTAPP-detail-King2024",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Natural History Museum",
        "schema:identifier": "https://ror.org/039zvsn29"
      },
      "schema:identifier": "20241125_xrd_nhm_orex-800117-108_1 | 20240725_xrd_nhm_orex-800107-103_1",
      "schema:startTime": "2024-07-25 | 2024-11-25",
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:name": "OREX-800117-108 | OREX-800107-103"
        }
      ],
      "schema:endTime": "no value available: schema:endTime"
    }
  ],
  "schema:contributor": [
    {
      "schema:roleName": "analyst",
      "schema:contributor": {
        "schema:name": "King, Ashley"
      }
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program."
    }
  ],
  "ada:sessionIdentifier": "20241125_xrd_nhm_orex-800117-108_1 | 20240725_xrd_nhm_orex-800107-103_1",
  "ada:analyst": "King, Ashley",
  "ada:analysisStartDate": "2024-07-25 | 2024-11-25",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program.",
  "ada:sampleName": "OREX-800117-108 | OREX-800107-103",
  "ada:samplingUnitName": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .

ex:xrdTAPP-detail-King2024 a schema1:Dataset,
        schema1:Product ;
    schema1:contributor [ schema1:contributor [ schema1:name "King, Ashley" ] ;
            schema1:roleName "analyst" ] ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program." ] ;
    prov:wasGeneratedBy [ schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "20241125_xrd_nhm_orex-800117-108_1 | 20240725_xrd_nhm_orex-800107-103_1" ;
            schema1:location [ a schema1:Place ;
                    schema1:identifier "https://ror.org/039zvsn29" ;
                    schema1:name "Natural History Museum" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:name "OREX-800117-108 | OREX-800107-103" ] ;
            schema1:startTime "2024-07-25 | 2024-11-25" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "2024-07-25 | 2024-11-25" ;
    ada:analyst "King, Ashley" ;
    ada:fundingSourceForAnalysis "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program." ;
    ada:sampleName "OREX-800117-108 | OREX-800107-103" ;
    ada:samplingUnitName "missing" ;
    ada:sessionIdentifier "20241125_xrd_nhm_orex-800117-108_1 | 20240725_xrd_nhm_orex-800107-103_1" .


```


### detail example King2024-2
detail instance derived from ADA n=1 | King2024 | NASA Johnson Space Center | (JSC-ARES)Malvern PANalytical XPert Pro XRD.
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
  "@id": "ex:xrdTAPP-detail-King2024-2",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "NASA Johnson Space Center",
        "schema:identifier": "https://ror.org/04xx4z452"
      },
      "schema:identifier": "20230928_xrd_jsc-ares_orex-500005-0_1",
      "schema:startTime": "2024-01-28",
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:name": "OREX-500005-0"
        }
      ],
      "schema:endTime": "no value available: schema:endTime"
    }
  ],
  "schema:contributor": [
    {
      "schema:roleName": "analyst",
      "schema:contributor": {
        "schema:name": "King, Ashley"
      }
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program."
    }
  ],
  "ada:sessionIdentifier": "20230928_xrd_jsc-ares_orex-500005-0_1",
  "ada:analyst": "King, Ashley",
  "ada:analysisStartDate": "2024-01-28",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program.",
  "ada:sampleName": "OREX-500005-0",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XRD/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:xrdTAPP-detail-King2024-2",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "NASA Johnson Space Center",
        "schema:identifier": "https://ror.org/04xx4z452"
      },
      "schema:identifier": "20230928_xrd_jsc-ares_orex-500005-0_1",
      "schema:startTime": "2024-01-28",
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:name": "OREX-500005-0"
        }
      ],
      "schema:endTime": "no value available: schema:endTime"
    }
  ],
  "schema:contributor": [
    {
      "schema:roleName": "analyst",
      "schema:contributor": {
        "schema:name": "King, Ashley"
      }
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program."
    }
  ],
  "ada:sessionIdentifier": "20230928_xrd_jsc-ares_orex-500005-0_1",
  "ada:analyst": "King, Ashley",
  "ada:analysisStartDate": "2024-01-28",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program.",
  "ada:sampleName": "OREX-500005-0",
  "ada:samplingUnitName": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .

ex:xrdTAPP-detail-King2024-2 a schema1:Dataset,
        schema1:Product ;
    schema1:contributor [ schema1:contributor [ schema1:name "King, Ashley" ] ;
            schema1:roleName "analyst" ] ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program." ] ;
    prov:wasGeneratedBy [ schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "20230928_xrd_jsc-ares_orex-500005-0_1" ;
            schema1:location [ a schema1:Place ;
                    schema1:identifier "https://ror.org/04xx4z452" ;
                    schema1:name "NASA Johnson Space Center" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:name "OREX-500005-0" ] ;
            schema1:startTime "2024-01-28" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "2024-01-28" ;
    ada:analyst "King, Ashley" ;
    ada:fundingSourceForAnalysis "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program." ;
    ada:sampleName "OREX-500005-0" ;
    ada:samplingUnitName "missing" ;
    ada:sessionIdentifier "20230928_xrd_jsc-ares_orex-500005-0_1" .


```


### detail example King2023
detail instance derived from ADA n=1 | King2023 | Natural History Museum | Rigaku Rapid 2 Micro-XRD.
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
  "@id": "ex:xrdTAPP-detail-King2023",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Natural History Museum",
        "schema:identifier": "https://ror.org/039zvsn29"
      },
      "schema:identifier": "20231124_xrd_nhm_orex-800032-110_1",
      "schema:startTime": "2023-11-24",
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:name": "OREX-800032-110"
        }
      ],
      "schema:endTime": "no value available: schema:endTime"
    }
  ],
  "schema:contributor": [
    {
      "schema:roleName": "analyst",
      "schema:contributor": {
        "schema:name": "King, Ashley"
      }
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program."
    }
  ],
  "ada:sessionIdentifier": "20231124_xrd_nhm_orex-800032-110_1",
  "ada:analyst": "King, Ashley",
  "ada:analysisStartDate": "2023-11-24",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program.",
  "ada:sampleName": "OREX-800032-110",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XRD/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:xrdTAPP-detail-King2023",
  "@type": [
    "schema:Dataset",
    "schema:Product"
  ],
  "prov:wasGeneratedBy": [
    {
      "schema:location": {
        "@type": [
          "schema:Place"
        ],
        "schema:name": "Natural History Museum",
        "schema:identifier": "https://ror.org/039zvsn29"
      },
      "schema:identifier": "20231124_xrd_nhm_orex-800032-110_1",
      "schema:startTime": "2023-11-24",
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:name": "OREX-800032-110"
        }
      ],
      "schema:endTime": "no value available: schema:endTime"
    }
  ],
  "schema:contributor": [
    {
      "schema:roleName": "analyst",
      "schema:contributor": {
        "schema:name": "King, Ashley"
      }
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program."
    }
  ],
  "ada:sessionIdentifier": "20231124_xrd_nhm_orex-800032-110_1",
  "ada:analyst": "King, Ashley",
  "ada:analysisStartDate": "2023-11-24",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program.",
  "ada:sampleName": "OREX-800032-110",
  "ada:samplingUnitName": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .

ex:xrdTAPP-detail-King2023 a schema1:Dataset,
        schema1:Product ;
    schema1:contributor [ schema1:contributor [ schema1:name "King, Ashley" ] ;
            schema1:roleName "analyst" ] ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program." ] ;
    prov:wasGeneratedBy [ schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "20231124_xrd_nhm_orex-800032-110_1" ;
            schema1:location [ a schema1:Place ;
                    schema1:identifier "https://ror.org/039zvsn29" ;
                    schema1:name "Natural History Museum" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:name "OREX-800032-110" ] ;
            schema1:startTime "2023-11-24" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "2023-11-24" ;
    ada:analyst "King, Ashley" ;
    ada:fundingSourceForAnalysis "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program." ;
    ada:sampleName "OREX-800032-110" ;
    ada:samplingUnitName "missing" ;
    ada:sessionIdentifier "20231124_xrd_nhm_orex-800032-110_1" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: XRD Analysis Detail
description: Detail block for XRD hasPart items, carrying the analysis-level properties
  supplied per scan rather than fixed by the procedure.
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
              - title: Sample Mount
                description: The holder or mounting geometry the specimen is presented
                  in. Distinct from Sample Preparation Method, which states how the
                  material was brought to that form.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/xrdTAPP/sampleMount
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/xrdTAPP/sampleMount
                  schema:name:
                    const: Sample Mount
                  schema:value:
                    type: string
                  schema:inDefinedTermSet:
                    const:
                      '@id': ada:vocab/sample-mount
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_samplingUnitSelectionCriteria
              - title: Step Size
                description: Angular increment between recorded points.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/xrdTAPP/stepSize
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/xrdTAPP/stepSize
                  schema:name:
                    const: Step Size
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
              - title: Time per Step
                description: Counting time at each angular step.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/xrdTAPP/timePerStep
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/xrdTAPP/timePerStep
                  schema:name:
                    const: Time per Step
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
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Analysis_constantsReferenceValues
            allOf:
            - contains:
                title: Sample Mount
                description: The holder or mounting geometry the specimen is presented
                  in. Distinct from Sample Preparation Method, which states how the
                  material was brought to that form.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/xrdTAPP/sampleMount
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/xrdTAPP/sampleMount
                  schema:name:
                    const: Sample Mount
                  schema:value:
                    type: string
                  schema:inDefinedTermSet:
                    const:
                      '@id': ada:vocab/sample-mount
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_samplingUnitSelectionCriteria
              minContains: 0
              maxContains: 1
            - contains:
                title: Step Size
                description: Angular increment between recorded points.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/xrdTAPP/stepSize
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/xrdTAPP/stepSize
                  schema:name:
                    const: Step Size
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
                title: Time per Step
                description: Counting time at each angular step.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/xrdTAPP/timePerStep
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/xrdTAPP/timePerStep
                  schema:name:
                    const: Time per Step
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
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Analysis_constantsReferenceValues
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
      title: Analysis Events
x-bblocks-metadata:
  itemIdentifier: ogch.techniqueProfile.geochemProfile.XRD.detail
  register: https://amds-ldeo.github.io/geochemBuildingBlocks/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-09'

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XRD/detail/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XRD/detail/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XRD/detail/context.jsonld)

## Sources

* [XRD_TAPP_draft_v2.csv (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/XRD/detail`

