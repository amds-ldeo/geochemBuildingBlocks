
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
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Gainsforth2023",
  "@type": [
    "ada:XANESCollection"
  ],
  "ada:componentType": "ada:XANESCollection",
  "schema:measurementTechnique": [
    {
      "@id": "ex:xanesTAPP-Gainsforth2023",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "20231211_xanes_als_orex-803030-100_1 | 20241027_xanes_als_orex-800055-125_1 | (+6 more)",
  "ada:analyst": "Gainsforth, Zack",
  "ada:analysisStartDate": "2023-11-12 | 2023-12-06 | (+4 more)",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA",
  "ada:sampleName": "OREX-803030-100 | OREX-800055-125 | OREX-501005-101 | (+3 more)",
  "ada:samplingUnit": "missing"
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
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Gainsforth2023",
  "@type": [
    "ada:XANESCollection"
  ],
  "ada:componentType": "ada:XANESCollection",
  "schema:measurementTechnique": [
    {
      "@id": "ex:xanesTAPP-Gainsforth2023",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "20231211_xanes_als_orex-803030-100_1 | 20241027_xanes_als_orex-800055-125_1 | (+6 more)",
  "ada:analyst": "Gainsforth, Zack",
  "ada:analysisStartDate": "2023-11-12 | 2023-12-06 | (+4 more)",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA",
  "ada:sampleName": "OREX-803030-100 | OREX-800055-125 | OREX-501005-101 | (+3 more)",
  "ada:samplingUnit": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .

<ex:detail-Gainsforth2023> a ada:XANESCollection ;
    schema1:measurementTechnique <ex:xanesTAPP-Gainsforth2023> ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "2023-11-12 | 2023-12-06 | (+4 more)" ;
    ada:analyst "Gainsforth, Zack" ;
    ada:componentType "ada:XANESCollection" ;
    ada:fundingSourceForAnalysis "NASA" ;
    ada:sampleName "OREX-803030-100 | OREX-800055-125 | OREX-501005-101 | (+3 more)" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "20231211_xanes_als_orex-803030-100_1 | 20241027_xanes_als_orex-800055-125_1 | (+6 more)" .

<ex:xanesTAPP-Gainsforth2023> schema1:identifier "missing" .


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

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XANES/detail/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XANES/detail/schema.yaml)


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

