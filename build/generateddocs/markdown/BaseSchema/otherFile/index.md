
# Other File Type (Schema)

`ogch.BaseSchema.otherFile` *v0.1*

Non-standard file formats approved for ADA submission. Defines properties: @type, componentType, schema:encodingFormat, formatDescription. Uses building blocks: detailSLS (geochemProperties).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Other File Type

Describes files in non-standard formats that have been approved for submission to the Astromat Archive. Supports EMSA spectral data, OBJ 3D models, STL files, XLSX workbooks, and Neptune Plus exports.

## Examples

### Other File Type Example
A 3D shape model in OBJ format from structured light scanning.
#### json
```json
{
  "@type": ["ada:otherFileType"],
  "ada:componentType": {
    "@type": "ada:other"
  },
  "schema:encodingFormat": "model/obj",
  "ada:formatDescription": "Wavefront OBJ 3D model file"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/otherFile/context.jsonld"
  ],
  "@type": [
    "ada:otherFileType"
  ],
  "ada:componentType": {
    "@type": "ada:other"
  },
  "schema:encodingFormat": "model/obj",
  "ada:formatDescription": "Wavefront OBJ 3D model file"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .

[] a ada:otherFileType ;
    schema1:encodingFormat "model/obj" ;
    ada:componentType [ a ada:other ] ;
    ada:formatDescription "Wavefront OBJ 3D model file" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Other File Type
description: Files in other widely-used formats approved for submission to the Astromat
  Archive. Includes EMSA, OBJ, STL, XLSX, and Neptune Plus export formats.
type: object
properties:
  '@type':
    type: array
    items:
      type: string
    minItems: 1
    contains:
      const: ada:otherFileType
  ada:componentType:
    type: string
    enum:
    - ada:VLMVideo
    - ada:XCTVideo
    - ada:contextVideo
    - ada:other
    - nil:missing
    description: ADA componentType for an other-format file, as a single string. Allowed
      values are constrained at the technique-profile level.
    x-jsonld-id: https://ada.astromat.org/metadata/componentType
  schema:encodingFormat:
    description: 'One of the approved non-standard file formats: ''Spectral Data Exchange
      File (.emsa)''-->text/plain; ''3D model file (.obj)''-->model/obj; ''Standard
      Triangle Language (.stl)''-->model/stl; ''Open XML workbook (.xlsx)''-->application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;
      ''Neptune Plus export (.exp)''-->application/octet-stream'
    type: array
    items:
      enum:
      - text/plain
      - model/obj
      - model/stl
      - application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
      - application/octet-stream
      - application/zip
      - video/mp4
      - video/x-m4v
      - video/quicktime
    x-jsonld-id: http://schema.org/encodingFormat
  ada:formatDescription:
    type: string
    description: Free text explanation of file format, or a link to a publicly accessible
      specification for the format.
    x-jsonld-id: https://ada.astromat.org/metadata/formatDescription
required:
- '@type'
- ada:componentType
x-jsonld-prefixes:
  schema: http://schema.org/
  ada: https://ada.astromat.org/metadata/

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/otherFile/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/otherFile/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/otherFile/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/BaseSchema/otherFile`

