
# Seismic Velocities and Rock Ultrasonic Elastic Constants Analysis Detail (Schema)

`ogch.techniqueProfile.geochemProfile.SVRUEC.detail` *v0.1*

Detail block for SVRUEC hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No SVRUEC-specific analysis property is defined yet.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### detail example Model5077
detail instance derived from ADA n=1 | Hanton, Lincoln | University of Calgary | Olympus Model 5077 PR with 35 MHz ultrasonic bandwidth.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Model5077",
  "@type": [
    "ada:SVRUECTabular"
  ],
  "ada:componentType": "ada:SVRUECTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:svruecTAPP-Model5077",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "20241216_sv-ruec_uca_orex-800123-0_1",
  "ada:analyst": "Hanton, Lincoln",
  "ada:analysisStartDate": "2024-12-16",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Grant 22EXPOSICA from Planetary Exploration, Space Exploration, Canadian Space Agency. This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program.",
  "ada:sampleName": "OREX-800123-0",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SVRUEC/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Model5077",
  "@type": [
    "ada:SVRUECTabular"
  ],
  "ada:componentType": "ada:SVRUECTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:svruecTAPP-Model5077",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "20241216_sv-ruec_uca_orex-800123-0_1",
  "ada:analyst": "Hanton, Lincoln",
  "ada:analysisStartDate": "2024-12-16",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Grant 22EXPOSICA from Planetary Exploration, Space Exploration, Canadian Space Agency. This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program.",
  "ada:sampleName": "OREX-800123-0",
  "ada:samplingUnit": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .

<ex:detail-Model5077> a ada:SVRUECTabular ;
    schema1:measurementTechnique <ex:svruecTAPP-Model5077> ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "2024-12-16" ;
    ada:analyst "Hanton, Lincoln" ;
    ada:componentType "ada:SVRUECTabular" ;
    ada:fundingSourceForAnalysis "Grant 22EXPOSICA from Planetary Exploration, Space Exploration, Canadian Space Agency. This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program." ;
    ada:sampleName "OREX-800123-0" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "20241216_sv-ruec_uca_orex-800123-0_1" .

<ex:svruecTAPP-Model5077> schema1:identifier "missing" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Seismic Velocities and Rock Ultrasonic Elastic Constants Analysis Detail
description: Detail block for SVRUEC hasPart items, carrying the analysis-identification
  properties the Core module places on the dataset. No SVRUEC-specific analysis property
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

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SVRUEC/detail/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SVRUEC/detail/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SVRUEC/detail/context.jsonld)

## Sources

* [SVRUEC_TAPP_draft_v2.csv (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/SVRUEC/detail`

