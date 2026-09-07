
# ADA XANES Profile (TAPP-linked) (Schema)

`ogch.techniqueProfile.geochemProfile.XANES.profile-ada` *v0.1*

Profile for an ADA metadata document describing X-ray absorption near edge structure spectroscopy products generated under a registered xanesTAPP procedure. Adds the XANES analysis detail on the schema:Dataset root and pins prov:used to the xanesTAPP definition, on top of the ADA XANES component-type constraints. DRAFT - the source table has not been through Phase 0 review.

[*Status*](http://www.opengis.net/def/status): Under development

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ADA XANES Product Profile (TAPP-linked)
description: Profile for an ADA metadata document describing data generated under
  a registered xanesTAPP procedure. Extends the base ADA product profile with the
  XANES analysis-instance detail on the schema:Dataset root, pins prov:used to the
  xanesTAPP definition and the instrument building block, and constrains valid XANES
  component types on both the monolithic and bundle forms of schema:distribution.
  Distinct from adaProfile/XANES, which is the generic (adaProduct-only) XANES profile
  and carries no TAPP linkage - a record conforming here additionally asserts which
  registered procedure produced it. DRAFT - the xanesTAPP source table has not been
  through Phase 0 review.
allOf:
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/adaProduct/schema.yaml
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XANES/detail/schema.yaml
- type: object
  properties:
    prov:wasGeneratedBy:
      description: 'Pin the xanesTAPP definition and the instrument where prov:used
        carries them. Constraint-only if/then, never a narrowed anyOf: prov:used items
        are role-keyed wrappers, and an anyOf here would allOf-merge with the base
        union and exclude item shapes the base allows.'
      type: array
      items:
        type: object
        properties:
          prov:used:
            type: array
            items:
              allOf:
              - if:
                  type: object
                  required:
                  - schema:instrument
                then:
                  properties:
                    schema:instrument:
                      type: array
                      minItems: 1
                      items:
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/instrument/schema.yaml
              - if:
                  type: object
                  properties:
                    '@type':
                      contains:
                        const: ada:TAPPDefinition
                  required:
                  - '@type'
                then:
                  $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XANES/tapp/schema.yaml
    schema:additionalType:
      description: Must include a XANES product type identifier.
      contains:
        enum:
        - X-ray Absorption Near Edge Structure Hyperspectral Image Stack (XANES)
        - X-ray absorption near edge structure (XANES) spectroscopy
    schema:distribution:
      description: Each distribution item is EITHER a monolithic single-file dataset
        whose ada:componentType is a XANES-specific or universal value (and may carry
        cdi:isStructuredBy), OR a bundle whose schema:hasPart members each carry such
        a componentType (the ADA/SAMIS archive form).
      type: array
      items:
        anyOf:
        - type: object
          required:
          - ada:componentType
          properties:
            ada:componentType:
              type: string
              anyOf:
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/adaProduct/schema.yaml#/$defs/universalComponentType
              - enum:
                - ada:XANESCollection
                - ada:XANESImageStack
                - ada:XANESProcessedTabular
                - ada:XANESRawTabular
                - ada:XANESStackOverviewImage
                - ada:XANESimage
        - type: object
          required:
          - schema:hasPart
          properties:
            schema:hasPart:
              items:
                type: object
                anyOf:
                - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/adaProduct/schema.yaml#/$defs/universalComponentTypeBranch
                - properties:
                    ada:componentType:
                      type: string
                      enum:
                      - ada:XANESCollection
                      - ada:XANESImageStack
                      - ada:XANESProcessedTabular
                      - ada:XANESRawTabular
                      - ada:XANESStackOverviewImage
                      - ada:XANESimage
                  required:
                  - ada:componentType
    schema:subjectOf:
      properties:
        dcterms:conformsTo:
          contains:
            type: object
            required:
            - '@id'
            additionalProperties: false
            properties:
              '@id':
                const: https://w3id.org/geochem/metadata/profiles/adaXANESFull

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XANES/profile-ada/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XANES/profile-ada/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://w3id.org/cdif/",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "prov": "http://www.w3.org/ns/prov#",
    "ada": "https://ada.astromat.org/metadata/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "bios": "https://bioschemas.org/",
    "spdx": "http://spdx.org/rdf/terms#",
    "nxs": "https://manual.nexusformat.org/classes/",
    "geosparql": "http://www.opengis.net/ont/geosparql#",
    "xas": "cdif:xas/",
    "wd": "https://www.wikidata.org/entity/",
    "dqv": "http://www.w3.org/ns/dqv#",
    "time": "http://www.w3.org/2006/time#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/XANES/profile-ada/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/XANES/profile-ada`

