
# Fourier Transform Ion Cyclotron Resonance Mass Spectrometry Analysis Detail (Schema)

`ogch.techniqueProfile.geochemProfile.FTICRMS.detail` *v0.1*

Detail block for FTICRMS hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No FTICRMS-specific analysis property is defined yet.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### detail example P0
detail instance derived from ADA n=16 | Liss, Michael | Helmholtz University (Helmholtz Zentrum Munchen) | FTICR-MS 12 Tesla Solarix Infinity system.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-P0",
  "@type": [
    "ada:FTICRMSCube"
  ],
  "ada:componentType": "ada:FTICRMSCube",
  "schema:measurementTechnique": [
    {
      "@id": "ex:fticrmsTAPP-P0",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "20240530_fticr-ms_hmgu_orex-803006-0_1",
  "ada:analyst": "Liss, Michael",
  "ada:analysisStartDate": "2024-05-30",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program. Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) Project-ID 364653263%E2%80%94TRR 235 (CRC 235)",
  "ada:sampleName": "OREX-803006-0",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/FTICRMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-P0",
  "@type": [
    "ada:FTICRMSCube"
  ],
  "ada:componentType": "ada:FTICRMSCube",
  "schema:measurementTechnique": [
    {
      "@id": "ex:fticrmsTAPP-P0",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "20240530_fticr-ms_hmgu_orex-803006-0_1",
  "ada:analyst": "Liss, Michael",
  "ada:analysisStartDate": "2024-05-30",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program. Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) Project-ID 364653263%E2%80%94TRR 235 (CRC 235)",
  "ada:sampleName": "OREX-803006-0",
  "ada:samplingUnit": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .

<ex:detail-P0> a ada:FTICRMSCube ;
    schema1:measurementTechnique <ex:fticrmsTAPP-P0> ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "2024-05-30" ;
    ada:analyst "Liss, Michael" ;
    ada:componentType "ada:FTICRMSCube" ;
    ada:fundingSourceForAnalysis "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program. Deutsche Forschungsgemeinschaft (DFG, German Research Foundation) Project-ID 364653263%E2%80%94TRR 235 (CRC 235)" ;
    ada:sampleName "OREX-803006-0" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "20240530_fticr-ms_hmgu_orex-803006-0_1" .

<ex:fticrmsTAPP-P0> schema1:identifier "missing" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Fourier Transform Ion Cyclotron Resonance Mass Spectrometry Analysis Detail
description: Detail block for FTICRMS hasPart items, carrying the analysis-identification
  properties the Core module places on the dataset. No FTICRMS-specific analysis property
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

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/FTICRMS/detail/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/FTICRMS/detail/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/FTICRMS/detail/context.jsonld)

## Sources

* [FTICRMS_TAPP_draft_v2.csv (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/FTICRMS/detail`

