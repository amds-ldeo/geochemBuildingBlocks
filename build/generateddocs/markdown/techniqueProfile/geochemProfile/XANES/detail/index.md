
# XANES Analysis Detail (Schema)

`ogch.techniqueProfile.geochemProfile.XANES.detail` *v0.1*

Detail block for XANES hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No XANES-specific analysis property is defined yet.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### detail example Gainsforth2023
detail instance derived from ADA n=241 | Gainsforth2023 | Advanced Light Source at Lawrence Berkeley National Laboratory | ALS STXM beamline 5.3.2.2.
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
  "@id": "ex:xanesTAPP-detail-Gainsforth2023",
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
        "schema:name": "Advanced Light Source at Lawrence Berkeley National Laboratory",
        "schema:identifier": "https://ror.org/00319zh75"
      },
      "schema:identifier": "20231211_xanes_als_orex-803030-100_1 | 20241027_xanes_als_orex-800055-125_1 | (+6 more)",
      "schema:startTime": "2023-11-12 | 2023-12-06 | (+4 more)",
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:name": "OREX-803030-100 | OREX-800055-125 | OREX-501005-101 | (+3 more)"
        }
      ],
      "schema:endTime": "no value available: schema:endTime"
    }
  ],
  "schema:contributor": [
    {
      "schema:roleName": "analyst",
      "schema:contributor": {
        "schema:name": "Gainsforth, Zack"
      }
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA"
    }
  ],
  "ada:sessionIdentifier": "20231211_xanes_als_orex-803030-100_1 | 20241027_xanes_als_orex-800055-125_1 | (+6 more)",
  "ada:analyst": "Gainsforth, Zack",
  "ada:analysisStartDate": "2023-11-12 | 2023-12-06 | (+4 more)",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA",
  "ada:sampleName": "OREX-803030-100 | OREX-800055-125 | OREX-501005-101 | (+3 more)",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XANES/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:xanesTAPP-detail-Gainsforth2023",
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
        "schema:name": "Advanced Light Source at Lawrence Berkeley National Laboratory",
        "schema:identifier": "https://ror.org/00319zh75"
      },
      "schema:identifier": "20231211_xanes_als_orex-803030-100_1 | 20241027_xanes_als_orex-800055-125_1 | (+6 more)",
      "schema:startTime": "2023-11-12 | 2023-12-06 | (+4 more)",
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:name": "OREX-803030-100 | OREX-800055-125 | OREX-501005-101 | (+3 more)"
        }
      ],
      "schema:endTime": "no value available: schema:endTime"
    }
  ],
  "schema:contributor": [
    {
      "schema:roleName": "analyst",
      "schema:contributor": {
        "schema:name": "Gainsforth, Zack"
      }
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA"
    }
  ],
  "ada:sessionIdentifier": "20231211_xanes_als_orex-803030-100_1 | 20241027_xanes_als_orex-800055-125_1 | (+6 more)",
  "ada:analyst": "Gainsforth, Zack",
  "ada:analysisStartDate": "2023-11-12 | 2023-12-06 | (+4 more)",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA",
  "ada:sampleName": "OREX-803030-100 | OREX-800055-125 | OREX-501005-101 | (+3 more)",
  "ada:samplingUnitName": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .

ex:xanesTAPP-detail-Gainsforth2023 a schema1:Dataset,
        schema1:Product ;
    schema1:contributor [ schema1:contributor [ schema1:name "Gainsforth, Zack" ] ;
            schema1:roleName "analyst" ] ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NASA" ] ;
    prov:wasGeneratedBy [ schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "20231211_xanes_als_orex-803030-100_1 | 20241027_xanes_als_orex-800055-125_1 | (+6 more)" ;
            schema1:location [ a schema1:Place ;
                    schema1:identifier "https://ror.org/00319zh75" ;
                    schema1:name "Advanced Light Source at Lawrence Berkeley National Laboratory" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:name "OREX-803030-100 | OREX-800055-125 | OREX-501005-101 | (+3 more)" ] ;
            schema1:startTime "2023-11-12 | 2023-12-06 | (+4 more)" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "2023-11-12 | 2023-12-06 | (+4 more)" ;
    ada:analyst "Gainsforth, Zack" ;
    ada:fundingSourceForAnalysis "NASA" ;
    ada:sampleName "OREX-803030-100 | OREX-800055-125 | OREX-501005-101 | (+3 more)" ;
    ada:samplingUnitName "missing" ;
    ada:sessionIdentifier "20231211_xanes_als_orex-803030-100_1 | 20241027_xanes_als_orex-800055-125_1 | (+6 more)" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: XANES Analysis Detail
description: Detail block for XANES hasPart items, carrying the analysis-identification
  properties the Core module places on the dataset. No XANES-specific analysis property
  is defined yet.
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
            allOf:
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_samplingUnitSelectionCriteria
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
  itemIdentifier: ogch.techniqueProfile.geochemProfile.XANES.detail
  register: https://amds-ldeo.github.io/geochemBuildingBlocks/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-11'

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XANES/detail/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XANES/detail/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XANES/detail/context.jsonld)

## Sources

* [XANES_TAPP_draft_v2.csv (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/XANES/detail`

