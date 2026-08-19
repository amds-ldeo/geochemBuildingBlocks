
# String Array Type (Schema)

`ogch.geochemProperties.stringArray` *v0.1*

Simple reusable array of strings used throughout ADA metadata. Defines type: array of strings.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# String Array Type

A simple reusable array of strings used throughout ADA metadata for properties like `resultTarget`, `memberTypes`, `phaseAnalyzed`, and `isotopeAnalyzed`.

## Examples

### String Array Example
A simple array of string values, used for multi-valued text properties such as phases analyzed or isotopes tracked.
#### json
```json
["olivine", "pyroxene", "plagioclase"]

```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: String Array Type
description: Simple reusable array of strings
type: array
minItems: 0
items:
  type: string

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/geochemProperties/stringArray/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/geochemProperties/stringArray/schema.yaml)


# JSON-LD Context

```jsonld
None
```

You can find the full JSON-LD context here:
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/_sources/geochemProperties/stringArray/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/geochemProperties/stringArray`

