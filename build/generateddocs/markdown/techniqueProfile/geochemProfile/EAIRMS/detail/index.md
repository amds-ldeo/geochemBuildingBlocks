
# Elemental analysis - isotope ratio mass spectrometry Analysis Detail (Schema)

`ogch.techniqueProfile.geochemProfile.EAIRMS.detail` *v0.1*

Detail block for EAIRMS hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No EAIRMS-specific analysis property is defined yet.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### detail example P0
detail instance derived from ADA n=16 | Foustoukos, Dionysis | Carnegie Institution for Science | Thermo Scientific Delta VPlus.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-P0",
  "@type": [
    "ada:EAIRMSCollection"
  ],
  "ada:componentType": "ada:EAIRMSCollection",
  "schema:measurementTechnique": [
    {
      "@id": "ex:eairmsTAPP-P0",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "20231209_ea-irms_cis_multisample_1",
  "ada:analyst": "Foustoukos, Dionysis",
  "ada:analysisStartDate": "2023-10-04",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "his material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program and CIW",
  "ada:sampleName": "OREX-800107-177",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EAIRMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-P0",
  "@type": [
    "ada:EAIRMSCollection"
  ],
  "ada:componentType": "ada:EAIRMSCollection",
  "schema:measurementTechnique": [
    {
      "@id": "ex:eairmsTAPP-P0",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "20231209_ea-irms_cis_multisample_1",
  "ada:analyst": "Foustoukos, Dionysis",
  "ada:analysisStartDate": "2023-10-04",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "his material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program and CIW",
  "ada:sampleName": "OREX-800107-177",
  "ada:samplingUnit": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .

<ex:detail-P0> a ada:EAIRMSCollection ;
    schema1:measurementTechnique <ex:eairmsTAPP-P0> ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "2023-10-04" ;
    ada:analyst "Foustoukos, Dionysis" ;
    ada:componentType "ada:EAIRMSCollection" ;
    ada:fundingSourceForAnalysis "his material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program and CIW" ;
    ada:sampleName "OREX-800107-177" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "20231209_ea-irms_cis_multisample_1" .

<ex:eairmsTAPP-P0> schema1:identifier "missing" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Elemental analysis - isotope ratio mass spectrometry Analysis Detail
description: Detail block for EAIRMS hasPart items, carrying the analysis-identification
  properties the Core module places on the dataset. No EAIRMS-specific analysis property
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

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EAIRMS/detail/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EAIRMS/detail/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EAIRMS/detail/context.jsonld)

## Sources

* [EAIRMS_TAPP_draft_v2.csv (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/EAIRMS/detail`

