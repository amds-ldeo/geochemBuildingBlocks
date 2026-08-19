
# Analytical Parameter Value Registry (Schema)

`ogch.techniqueProtocols.parameterValues` *v0.1*

Registry of reusable schema:PropertyValue parameter-value definitions derived from technique TAPP spreadsheets. Hosts one $def per per-dataset parameter value (e.g. acceleratingVoltage, beamDiameter, BeamRasterDimension, reportedAnalyte). Detail building blocks reference these definitions via fragment $refs so they resolve locally through the register.

[*Status*](http://www.opengis.net/def/status): Under development

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ADA Analytical Parameter Value Registry
description: Registry of reusable schema:PropertyValue parameter-value definitions
  derived from technique TAPP spreadsheets. Each $def constrains one per-dataset schema:PropertyValue
  entry. Detail building blocks reference these definitions via fragment $refs (schema.yaml#/$defs/<name>)
  so they resolve locally through the building-block register. The root only hosts
  $defs; it has no instantiable properties of its own.
type: object
$defs:
  acceleratingVoltage:
    title: Default Accelerating Voltage
    description: Electron beam accelerating voltage in kilovolts (kV).
    type: object
    properties:
      '@context':
        const:
          schema: http://schema.org/
          ada: https://ada.astromat.org/metadata/
      '@id':
        const: ada:parameter/empaTAPP/acceleratingVoltage
      '@type':
        const:
        - schema:PropertyValue
      schema:propertyID:
        const: ada:parameter/empaTAPP/acceleratingVoltage
      schema:name:
        const: Default Accelerating Voltage
      schema:value:
        anyOf:
        - type: number
        - type: string
      schema:unitText:
        type: string
    required:
    - '@id'
    - '@type'
    - schema:propertyID
    - schema:name
    - schema:value
    - schema:unitText
  beamDiameter:
    title: Default Beam Diameter
    description: Diameter of the focused or defocused electron beam in micrometers.
    type: object
    properties:
      '@context':
        const:
          schema: http://schema.org/
          ada: https://ada.astromat.org/metadata/
      '@id':
        const: ada:parameter/empaTAPP/beamDiameter
      '@type':
        const:
        - schema:PropertyValue
      schema:propertyID:
        const: ada:parameter/empaTAPP/beamDiameter
      schema:name:
        const: Default Beam Diameter
      schema:value:
        anyOf:
        - type: number
        - type: string
      schema:unitText:
        type: string
    required:
    - '@id'
    - '@type'
    - schema:propertyID
    - schema:name
    - schema:value
    - schema:unitText
  BeamRasterDimension:
    title: Beam Raster Dimensions
    description: "X \xD7 Y dimensions of beam raster area in micrometers, if beam
      raster mode was used."
    type: object
    properties:
      '@context':
        const:
          schema: http://schema.org/
          ada: https://ada.astromat.org/metadata/
      '@id':
        const: ada:parameter/empaTAPP/BeamRasterDimension
      '@type':
        const:
        - schema:PropertyValue
      schema:propertyID:
        const: ada:parameter/empaTAPP/BeamRasterDimension
      schema:name:
        const: Beam Raster Dimensions
      schema:value:
        anyOf:
        - type: number
        - type: string
      schema:unitText:
        type: string
    required:
    - '@id'
    - '@type'
    - schema:propertyID
    - schema:name
    - schema:value
    - schema:unitText
  reportedAnalyte:
    title: Target Element
    description: The element or oxide measured in this row of the element table.
    type: object
    properties:
      '@context':
        const:
          schema: http://schema.org/
          ada: https://ada.astromat.org/metadata/
      '@id':
        const: ada:parameter/empaTAPP/reportedAnalyte
      '@type':
        const:
        - schema:PropertyValue
      schema:propertyID:
        const: ada:parameter/empaTAPP/reportedAnalyte
      schema:name:
        const: Target Element
      schema:value:
        type: string
    required:
    - '@id'
    - '@type'
    - schema:propertyID
    - schema:name
    - schema:value

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/parameterValues/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProtocols/parameterValues/schema.yaml)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProtocols/parameterValues`

