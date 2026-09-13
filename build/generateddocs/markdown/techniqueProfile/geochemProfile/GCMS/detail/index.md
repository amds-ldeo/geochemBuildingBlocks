
# Gas Chromatography-Mass Spectrometry Analysis Detail (Schema)

`ogch.techniqueProfile.geochemProfile.GCMS.detail` *v0.1*

Detail block for GCMS hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No GCMS-specific analysis property is defined yet.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### detail example Agilent5977
detail instance derived from ADA n=26 | Sako, Sunami | Tohoku University | Agilent 5977B GCMSD.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Agilent5977",
  "@type": [
    "ada:GCMSCollection"
  ],
  "ada:componentType": "ada:GCMSCollection",
  "schema:measurementTechnique": [
    {
      "@id": "ex:gcmsTAPP-Agilent5977",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "20241121_gc-ms_tu_orex-800107-108_1",
  "ada:analyst": "Sako, Sunami",
  "ada:analysisStartDate": "2023-10-03",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program. This analysis is supported by JSPS Kakenhi 18H03728 and 22H00165 to Yoshihiro Furukawa.",
  "ada:sampleName": "OREX-800107-108",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/GCMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Agilent5977",
  "@type": [
    "ada:GCMSCollection"
  ],
  "ada:componentType": "ada:GCMSCollection",
  "schema:measurementTechnique": [
    {
      "@id": "ex:gcmsTAPP-Agilent5977",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "20241121_gc-ms_tu_orex-800107-108_1",
  "ada:analyst": "Sako, Sunami",
  "ada:analysisStartDate": "2023-10-03",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program. This analysis is supported by JSPS Kakenhi 18H03728 and 22H00165 to Yoshihiro Furukawa.",
  "ada:sampleName": "OREX-800107-108",
  "ada:samplingUnit": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .

<ex:detail-Agilent5977> a ada:GCMSCollection ;
    schema1:measurementTechnique <ex:gcmsTAPP-Agilent5977> ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "2023-10-03" ;
    ada:analyst "Sako, Sunami" ;
    ada:componentType "ada:GCMSCollection" ;
    ada:fundingSourceForAnalysis "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program. This analysis is supported by JSPS Kakenhi 18H03728 and 22H00165 to Yoshihiro Furukawa." ;
    ada:sampleName "OREX-800107-108" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "20241121_gc-ms_tu_orex-800107-108_1" .

<ex:gcmsTAPP-Agilent5977> schema1:identifier "missing" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Gas Chromatography-Mass Spectrometry Analysis Detail
description: Detail block for GCMS hasPart items, carrying the analysis-identification
  properties the Core module places on the dataset. No GCMS-specific analysis property
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

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/GCMS/detail/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/GCMS/detail/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/GCMS/detail/context.jsonld)

## Sources

* [GCMS_TAPP_draft_v2.csv (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/GCMS/detail`

