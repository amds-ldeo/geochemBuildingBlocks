
# ADA Analysis Instrument (Schema)

`ogch.BaseSchema.instrument` *v0.1*

ADA analytical instrument extending the core CDIF instrument building block. Typed as schema:Thing + schema:Product with domain-specific classifications (e.g. nxs:BaseClass/NXinstrument) in schema:additionalType. Inherits hierarchical sub-components, manufacturer, model, calibration properties from core.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# ADA Analysis Instrument

Extends the core CDIF [instrument](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/schemaorgProperties/instrument/) building block for ADA analytical instruments. Instruments are typed as `schema:Thing` + `schema:Product` (from core) with domain-specific classifications in `schema:additionalType` (e.g. `nxs:BaseClass/NXinstrument`, `ada:AMSInstrument`).

Inherits all core instrument properties: hierarchical sub-components via `schema:hasPart`, manufacturer, model, ownership, calibration properties, and linked resources.

## Examples

### ADA Analysis Instrument Example
An analytical instrument extending the core CDIF instrument building block.
Typed as schema:Thing + schema:Product with NeXus and technique-specific
classifications in additionalType.
#### json
```json
{
  "@type": ["schema:Thing", "schema:Product"],
  "schema:name": "JEOL JXA-8530F Electron Microprobe",
  "schema:description": "Field-emission electron probe microanalyzer with 5 wavelength-dispersive spectrometers",
  "schema:identifier": "https://www.wikidata.org/wiki/Q116917974",
  "schema:additionalType": ["nxs:BaseClass/NXinstrument", "https://gcmd.earthdata.nasa.gov/kms/concept/76a947a3-4529-4fb7-87a7-f4b3a0a0de48"]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "nxs": "https://manual.nexusformat.org/classes/"
    },
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/instrument/context.jsonld"
  ],
  "@type": [
    "schema:Thing",
    "schema:Product"
  ],
  "schema:name": "JEOL JXA-8530F Electron Microprobe",
  "schema:description": "Field-emission electron probe microanalyzer with 5 wavelength-dispersive spectrometers",
  "schema:identifier": "https://www.wikidata.org/wiki/Q116917974",
  "schema:additionalType": [
    "nxs:BaseClass/NXinstrument",
    "https://gcmd.earthdata.nasa.gov/kms/concept/76a947a3-4529-4fb7-87a7-f4b3a0a0de48"
  ]
}
```

#### ttl
```ttl
@prefix schema1: <http://schema.org/> .

[] a schema1:Product,
        schema1:Thing ;
    schema1:additionalType "https://gcmd.earthdata.nasa.gov/kms/concept/76a947a3-4529-4fb7-87a7-f4b3a0a0de48",
        "nxs:BaseClass/NXinstrument" ;
    schema1:description "Field-emission electron probe microanalyzer with 5 wavelength-dispersive spectrometers" ;
    schema1:identifier "https://www.wikidata.org/wiki/Q116917974" ;
    schema1:name "JEOL JXA-8530F Electron Microprobe" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ADA Analysis Instrument
description: ADA analytical instrument building block. Extends the core CDIF instrument
  building block with NeXus NXinstrument classification via additionalType. Instruments
  are typed as schema:Thing + schema:Product (from core) with domain-specific types
  (e.g. nxs:BaseClass/NXinstrument, ada:AMSInstrument) in additionalType.
allOf:
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/instrument/schema.yaml
- type: object
  properties:
    schema:additionalType:
      description: 'Domain-specific instrument type classifications. Should include
        a NeXus base class (e.g. nxs:BaseClass/NXinstrument) and/or technique-specific
        identifier (e.g. ada:AMSInstrument, GCMD instrument identifier). URI-shape
        values MUST be serialized as JSON-LD IRI references ({"@id":"..."}); free-label
        strings remain valid. Every instrument additionally carries the Wikidata "measuring
        instrument" type, which is invariant across techniques: the technique-specific
        entry says what KIND of instrument this is and varies by profile, while the
        Wikidata term says that it is an instrument at all, and gives a consumer one
        term to select on without knowing the ADA vocabulary.'
      type: array
      items:
        anyOf:
        - type: string
        - type: object
          additionalProperties: false
          required:
          - '@id'
          properties:
            '@id':
              type: string
      minItems: 1
      contains:
        type: object
        properties:
          '@id':
            const: https://www.wikidata.org/wiki/Q3099911
        required:
        - '@id'
      x-jsonld-id: http://schema.org/additionalType
    schema:hasPart:
      description: 'Sub-components of this instrument system (a torch, an ICP source,
        a collision/reaction cell, a spectrometer). A component IS an instrument --
        same @type (schema:Product + schema:Thing), same Wikidata term, and its own
        schema:additionalType token saying which kind of component it is. The shape
        is restated rather than written as `$ref: ''#''`, because resolve_schema replaces
        a circular ref with an empty stub -- it would read as "a part is an instrument"
        and enforce nothing. Upstream types a component more loosely (schema:Thing
        alone, no Wikidata); this narrows it, and the two compose because allOf intersects.'
      type: array
      items:
        anyOf:
        - type: object
          required:
          - '@type'
          - schema:name
          - schema:additionalType
          properties:
            '@type':
              type: array
              items:
                type: string
              minItems: 2
              allOf:
              - contains:
                  const: schema:Product
              - contains:
                  const: schema:Thing
            schema:name:
              type: string
              x-jsonld-id: http://schema.org/name
            schema:additionalType:
              type: array
              minItems: 1
              contains:
                type: object
                required:
                - '@id'
                properties:
                  '@id':
                    const: https://www.wikidata.org/wiki/Q3099911
              x-jsonld-id: http://schema.org/additionalType
        - type: object
          additionalProperties: false
          description: Reference by node @id to a component described elsewhere.
          required:
          - '@id'
          properties:
            '@id':
              type: string
      x-jsonld-id: http://schema.org/hasPart
  required:
  - schema:additionalType
x-jsonld-prefixes:
  schema: http://schema.org/
  nxs: https://manual.nexusformat.org/classes/

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/instrument/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/instrument/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "wd": "https://www.wikidata.org/entity/",
    "nxs": "https://manual.nexusformat.org/classes/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://w3id.org/cdif/",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/instrument/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/BaseSchema/instrument`

