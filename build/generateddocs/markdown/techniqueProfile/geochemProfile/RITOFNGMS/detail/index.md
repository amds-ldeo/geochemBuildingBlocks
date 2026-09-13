
# Resonance ionization time of flight noble gas mass spectrome Analysis Detail (Schema)

`ogch.techniqueProfile.geochemProfile.RITOFNGMS.detail` *v0.1*

Detail block for RITOFNGMS hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No RITOFNGMS-specific analysis property is defined yet.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### detail example P0
detail instance derived from ADA n=2 | Crowther, Sarah | University of Manchester | RELAX.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-P0",
  "@type": [
    "ada:RITOFNGMSCollection"
  ],
  "ada:componentType": "ada:RITOFNGMSCollection",
  "schema:measurementTechnique": [
    {
      "@id": "ex:ritofngmsTAPP-P0",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "20240116_ri-tof-ngms_uom_orex-803060-0_1",
  "ada:analyst": "Crowther, Sarah",
  "ada:analysisStartDate": "2024-01-16",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Science and Technology Facilities Council (UK) ST/V000675/1 and ST/Y002369/1",
  "ada:sampleName": "OREX-803060-0",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/RITOFNGMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-P0",
  "@type": [
    "ada:RITOFNGMSCollection"
  ],
  "ada:componentType": "ada:RITOFNGMSCollection",
  "schema:measurementTechnique": [
    {
      "@id": "ex:ritofngmsTAPP-P0",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "20240116_ri-tof-ngms_uom_orex-803060-0_1",
  "ada:analyst": "Crowther, Sarah",
  "ada:analysisStartDate": "2024-01-16",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Science and Technology Facilities Council (UK) ST/V000675/1 and ST/Y002369/1",
  "ada:sampleName": "OREX-803060-0",
  "ada:samplingUnit": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .

<ex:detail-P0> a ada:RITOFNGMSCollection ;
    schema1:measurementTechnique <ex:ritofngmsTAPP-P0> ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "2024-01-16" ;
    ada:analyst "Crowther, Sarah" ;
    ada:componentType "ada:RITOFNGMSCollection" ;
    ada:fundingSourceForAnalysis "Science and Technology Facilities Council (UK) ST/V000675/1 and ST/Y002369/1" ;
    ada:sampleName "OREX-803060-0" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "20240116_ri-tof-ngms_uom_orex-803060-0_1" .

<ex:ritofngmsTAPP-P0> schema1:identifier "missing" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Resonance ionization time of flight noble gas mass spectrome Analysis Detail
description: Detail block for RITOFNGMS hasPart items, carrying the analysis-identification
  properties the Core module places on the dataset. No RITOFNGMS-specific analysis
  property is defined yet.
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

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/RITOFNGMS/detail/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/RITOFNGMS/detail/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/RITOFNGMS/detail/context.jsonld)

## Sources

* [RITOFNGMS_TAPP_draft_v2.csv (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/RITOFNGMS/detail`

