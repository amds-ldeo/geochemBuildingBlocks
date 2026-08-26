
# ADA Analysis Laboratory (Schema)

`ogch.BaseSchema.laboratory` *v0.1*

ADA laboratory/facility building block extending core CDIF spatialExtent (schema:Place). Adds nxs:BaseClass/NXsource classification via additionalType. Inherits place name, identifier, alternateName, geo coordinates from core.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# ADA Analysis Laboratory

Extends the core CDIF [spatialExtent](https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/_sources/schemaorgProperties/spatialExtent/) building block for ADA laboratory/facility descriptions. Adds `nxs:BaseClass/NXsource` classification via `schema:additionalType`. Inherits place name, identifier, alternateName, geo coordinates, and GeoSPARQL geometry from core spatialExtent.

## Examples

### ADA Analysis Laboratory Example
A laboratory facility extending core spatialExtent (schema:Place) with
NeXus NXsource classification in additionalType.
#### json
```json
{
  "@type": ["schema:Place"],
  "schema:additionalType": ["nxs:BaseClass/NXsource"],
  "schema:name": ["Lunar and Planetary Laboratory Electron Microprobe Facility"],
  "schema:alternateName": "LPL EMPA Lab",
  "schema:identifier": "https://ror.org/03m2x1q45"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/laboratory/context.jsonld"
  ],
  "@type": [
    "schema:Place"
  ],
  "schema:additionalType": [
    "nxs:BaseClass/NXsource"
  ],
  "schema:name": [
    "Lunar and Planetary Laboratory Electron Microprobe Facility"
  ],
  "schema:alternateName": "LPL EMPA Lab",
  "schema:identifier": "https://ror.org/03m2x1q45"
}
```

#### ttl
```ttl
@prefix schema1: <http://schema.org/> .

[] a schema1:Place ;
    schema1:additionalType "nxs:BaseClass/NXsource" ;
    schema1:alternateName "LPL EMPA Lab" ;
    schema1:identifier "https://ror.org/03m2x1q45" ;
    schema1:name "Lunar and Planetary Laboratory Electron Microprobe Facility" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ADA Analysis Laboratory
description: ADA laboratory or facility building block. Extends the core CDIF spatialExtent
  (schema:Place) with NeXus NXsource classification via additionalType. Inherits place
  name, identifier, alternateName, geo coordinates, and geosparql geometry from spatialExtent.
allOf:
- $ref: https://cross-domain-interoperability-framework.github.io/metadataBuildingBlocks/build/annotated/bbr/metadata/schemaorgProperties/spatialExtent/schema.yaml
- type: object
  properties:
    schema:additionalType:
      description: 'Must classify the place as a NeXus NXsource. The value is a sealed
        reference ({"@id": ...}) so JSON-LD expands it to a real IRI; written as a
        bare string it stays a literal that looks like a URI and resolves to nothing.
        The two-segment path is the form that actually resolves -- .../classes/BaseClass/NXsource
        is a 404, .../classes/base_classes/NXsource.html is not.'
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
      contains:
        type: object
        additionalProperties: false
        required:
        - '@id'
        properties:
          '@id':
            const: nxs:base_classes/NXsource.html
      x-jsonld-id: http://schema.org/additionalType
x-jsonld-prefixes:
  schema: http://schema.org/
  nxs: https://manual.nexusformat.org/classes/

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/laboratory/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/laboratory/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "nxs": "https://manual.nexusformat.org/classes/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/laboratory/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/BaseSchema/laboratory`

