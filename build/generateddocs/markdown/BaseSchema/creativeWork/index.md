
# Creative Work Type (Schema)

`ogch.BaseSchema.creativeWork` *v0.1*

Shell type for labeled links to creative works (schema:CreativeWork). Defines properties: @type, schema:name, schema:description, schema:url.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Creative Work Type

A shell type used mostly for labeled links to other resources. Implements `schema:CreativeWork` with name, description, and URL properties. Used in ADA metadata for license references and related resource links.

## Examples

### Creative Work Example
A labeled link to an external resource typed as schema:CreativeWork.
#### json
```json
{
  "@type": ["schema:CreativeWork"],
  "schema:name": "Analytical Methods for Geochemistry",
  "schema:description": "Reference document describing standard analytical procedures.",
  "schema:url": "https://doi.org/10.1234/example-methods"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/"
    },
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/BaseSchema/creativeWork/context.jsonld"
  ],
  "@type": [
    "schema:CreativeWork"
  ],
  "schema:name": "Analytical Methods for Geochemistry",
  "schema:description": "Reference document describing standard analytical procedures.",
  "schema:url": "https://doi.org/10.1234/example-methods"
}
```

#### ttl
```ttl
@prefix schema1: <http://schema.org/> .

[] a schema1:CreativeWork ;
    schema1:description "Reference document describing standard analytical procedures." ;
    schema1:name "Analytical Methods for Geochemistry" ;
    schema1:url "https://doi.org/10.1234/example-methods" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Creative Work Type
description: Shell type for labeled links to other resources. Any schema.org CreativeWork
  property could be included.
type: object
properties:
  '@type':
    type: array
    contains:
      const: schema:CreativeWork
    minItems: 1
  schema:name:
    type: string
    x-jsonld-id: http://schema.org/name
  schema:description:
    type: string
    x-jsonld-id: http://schema.org/description
  schema:url:
    type: string
    x-jsonld-id: http://schema.org/url
required:
- '@type'
x-jsonld-prefixes:
  schema: http://schema.org/

```

Links to the schema:

* YAML version: [schema.yaml](https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/BaseSchema/creativeWork/schema.json)
* JSON version: [schema.json](https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/BaseSchema/creativeWork/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/BaseSchema/creativeWork/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/BaseSchema/creativeWork`

