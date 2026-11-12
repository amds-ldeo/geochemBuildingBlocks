
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
    "ada": "https://ada.astromat.org/metadata/",
    "ex": "https://example.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/",
    "prov": "http://www.w3.org/ns/prov#"
  },
  "@id": "ex:ritofngmsTAPP-detail-P0",
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
        "schema:name": "University of Manchester"
      },
      "schema:identifier": "20240116_ri-tof-ngms_uom_orex-803060-0_1",
      "schema:startTime": "2024-01-16",
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:name": "OREX-803060-0"
        }
      ],
      "schema:endTime": "no value available: schema:endTime"
    }
  ],
  "schema:contributor": [
    {
      "schema:roleName": "analyst",
      "schema:contributor": {
        "schema:name": "Crowther, Sarah"
      }
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "Science and Technology Facilities Council (UK) ST/V000675/1 and ST/Y002369/1"
    }
  ],
  "ada:sessionIdentifier": "20240116_ri-tof-ngms_uom_orex-803060-0_1",
  "ada:analyst": "Crowther, Sarah",
  "ada:analysisStartDate": "2024-01-16",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Science and Technology Facilities Council (UK) ST/V000675/1 and ST/Y002369/1",
  "ada:sampleName": "OREX-803060-0",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/RITOFNGMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/",
      "ex": "https://example.org/",
      "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
      "bios": "https://bioschemas.org/",
      "prov": "http://www.w3.org/ns/prov#"
    }
  ],
  "@id": "ex:ritofngmsTAPP-detail-P0",
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
        "schema:name": "University of Manchester"
      },
      "schema:identifier": "20240116_ri-tof-ngms_uom_orex-803060-0_1",
      "schema:startTime": "2024-01-16",
      "schema:object": [
        {
          "@type": [
            "https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample"
          ],
          "schema:name": "OREX-803060-0"
        }
      ],
      "schema:endTime": "no value available: schema:endTime"
    }
  ],
  "schema:contributor": [
    {
      "schema:roleName": "analyst",
      "schema:contributor": {
        "schema:name": "Crowther, Sarah"
      }
    }
  ],
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "Science and Technology Facilities Council (UK) ST/V000675/1 and ST/Y002369/1"
    }
  ],
  "ada:sessionIdentifier": "20240116_ri-tof-ngms_uom_orex-803060-0_1",
  "ada:analyst": "Crowther, Sarah",
  "ada:analysisStartDate": "2024-01-16",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Science and Technology Facilities Council (UK) ST/V000675/1 and ST/Y002369/1",
  "ada:sampleName": "OREX-803060-0",
  "ada:samplingUnitName": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix schema1: <http://schema.org/> .

ex:ritofngmsTAPP-detail-P0 a schema1:Dataset,
        schema1:Product ;
    schema1:contributor [ schema1:contributor [ schema1:name "Crowther, Sarah" ] ;
            schema1:roleName "analyst" ] ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "Science and Technology Facilities Council (UK) ST/V000675/1 and ST/Y002369/1" ] ;
    prov:wasGeneratedBy [ schema1:endTime "no value available: schema:endTime" ;
            schema1:identifier "20240116_ri-tof-ngms_uom_orex-803060-0_1" ;
            schema1:location [ a schema1:Place ;
                    schema1:name "University of Manchester" ] ;
            schema1:object [ a <https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample> ;
                    schema1:name "OREX-803060-0" ] ;
            schema1:startTime "2024-01-16" ] ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "2024-01-16" ;
    ada:analyst "Crowther, Sarah" ;
    ada:fundingSourceForAnalysis "Science and Technology Facilities Council (UK) ST/V000675/1 and ST/Y002369/1" ;
    ada:sampleName "OREX-803060-0" ;
    ada:samplingUnitName "missing" ;
    ada:sessionIdentifier "20240116_ri-tof-ngms_uom_orex-803060-0_1" .


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
      title: Analysis Events
x-bblocks-metadata:
  itemIdentifier: ogch.techniqueProfile.geochemProfile.RITOFNGMS.detail
  register: https://amds-ldeo.github.io/geochemBuildingBlocks/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-11'

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/RITOFNGMS/detail/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/RITOFNGMS/detail/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/RITOFNGMS/detail/context.jsonld)

## Sources

* [RITOFNGMS_TAPP_draft_v2.csv (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/RITOFNGMS/detail`

