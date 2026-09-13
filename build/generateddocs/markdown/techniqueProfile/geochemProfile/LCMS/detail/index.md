
# Liquid Chromatography-Mass Spectrometry Analysis Detail (Schema)

`ogch.techniqueProfile.geochemProfile.LCMS.detail` *v0.1*

Detail block for LCMS hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No LCMS-specific analysis property is defined yet.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### detail example Ultimate3000
detail instance derived from ADA n=24 | Oba, Yasuhiro | Kyushu University | Thermo Fischer Ultimate3000-QExactive.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Ultimate3000",
  "@type": [
    "ada:LCMSCollection"
  ],
  "ada:componentType": "ada:LCMSCollection",
  "schema:measurementTechnique": [
    {
      "@id": "ex:lcmsTAPP-Ultimate3000",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "20240301_lc-ms_ku_orex-800044-101_1",
  "ada:analyst": "Oba, Yasuhiro",
  "ada:analysisStartDate": "2023-11-15",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA",
  "ada:sampleName": "OREX-800044-101",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LCMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Ultimate3000",
  "@type": [
    "ada:LCMSCollection"
  ],
  "ada:componentType": "ada:LCMSCollection",
  "schema:measurementTechnique": [
    {
      "@id": "ex:lcmsTAPP-Ultimate3000",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "20240301_lc-ms_ku_orex-800044-101_1",
  "ada:analyst": "Oba, Yasuhiro",
  "ada:analysisStartDate": "2023-11-15",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA",
  "ada:sampleName": "OREX-800044-101",
  "ada:samplingUnit": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .

<ex:detail-Ultimate3000> a ada:LCMSCollection ;
    schema1:measurementTechnique <ex:lcmsTAPP-Ultimate3000> ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "2023-11-15" ;
    ada:analyst "Oba, Yasuhiro" ;
    ada:componentType "ada:LCMSCollection" ;
    ada:fundingSourceForAnalysis "NASA" ;
    ada:sampleName "OREX-800044-101" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "20240301_lc-ms_ku_orex-800044-101_1" .

<ex:lcmsTAPP-Ultimate3000> schema1:identifier "missing" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Liquid Chromatography-Mass Spectrometry Analysis Detail
description: Detail block for LCMS hasPart items, carrying the analysis-identification
  properties the Core module places on the dataset. No LCMS-specific analysis property
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

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LCMS/detail/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LCMS/detail/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LCMS/detail/context.jsonld)

## Sources

* [LCMS_TAPP_draft_v2.csv (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/LCMS/detail`

