
# Inductively coupled plasma - optical emission spectrometry Analysis Detail (Schema)

`ogch.techniqueProfile.geochemProfile.ICPOES.detail` *v0.1*

Detail block for ICPOES hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No ICPOES-specific analysis property is defined yet.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### detail example CAP6300
detail instance derived from ADA n=12 | Welten, Kees | University of California, Berkeley | Thermo Fisher Scientific iCAP 6300 duo.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-CAP6300",
  "@type": [
    "ada:ICPOESRawTabular"
  ],
  "ada:componentType": "ada:ICPOESRawTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:icpoesTAPP-CAP6300",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "20231219_icp-oes_ucb_multisample_1",
  "ada:analyst": "Welten, Kees",
  "ada:analysisStartDate": "2023-12-13",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program. This study is supported by NASA grant 80NSSC22K1693 through the OREX Participating Scientist Program.",
  "ada:sampleName": "OREX-803047-101",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/ICPOES/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-CAP6300",
  "@type": [
    "ada:ICPOESRawTabular"
  ],
  "ada:componentType": "ada:ICPOESRawTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:icpoesTAPP-CAP6300",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "20231219_icp-oes_ucb_multisample_1",
  "ada:analyst": "Welten, Kees",
  "ada:analysisStartDate": "2023-12-13",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program. This study is supported by NASA grant 80NSSC22K1693 through the OREX Participating Scientist Program.",
  "ada:sampleName": "OREX-803047-101",
  "ada:samplingUnit": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .

<ex:detail-CAP6300> a ada:ICPOESRawTabular ;
    schema1:measurementTechnique <ex:icpoesTAPP-CAP6300> ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "2023-12-13" ;
    ada:analyst "Welten, Kees" ;
    ada:componentType "ada:ICPOESRawTabular" ;
    ada:fundingSourceForAnalysis "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program. This study is supported by NASA grant 80NSSC22K1693 through the OREX Participating Scientist Program." ;
    ada:sampleName "OREX-803047-101" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "20231219_icp-oes_ucb_multisample_1" .

<ex:icpoesTAPP-CAP6300> schema1:identifier "missing" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Inductively coupled plasma - optical emission spectrometry Analysis Detail
description: Detail block for ICPOES hasPart items, carrying the analysis-identification
  properties the Core module places on the dataset. No ICPOES-specific analysis property
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

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/ICPOES/detail/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/ICPOES/detail/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/ICPOES/detail/context.jsonld)

## Sources

* [ICPOES_TAPP_draft_v2.csv (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/ICPOES/detail`

