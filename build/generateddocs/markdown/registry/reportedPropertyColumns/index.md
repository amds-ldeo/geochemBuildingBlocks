
# Reported-Property-Column Specification Registry (Schema)

`ogch.registry.reportedPropertyColumns` *v0.1*

Registry of reusable schema:PropertyValueSpecification reported-property column definitions derived from technique TAPP workbooks. Each $def constrains one column of the reported-property table -- the variables a procedure REPORTS, as distinct from the analytes and channels it acquires. TAPP building blocks reference these definitions via fragment $refs so they resolve locally through the building-block register. The root only hosts $defs; it has no instantiable properties of its own. TAPP building blocks reference these definitions via fragment $refs so they resolve locally through the register.

[*Status*](http://www.opengis.net/def/status): Under development

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ADA Reported-Property Column Specification Registry
description: Registry of reusable schema:PropertyValueSpecification reported-property
  column definitions derived from technique TAPP workbooks. Each $def constrains one
  column of the reported-property table -- the variables a procedure REPORTS, as distinct
  from the analytes and channels it acquires. TAPP building blocks reference these
  definitions via fragment $refs so they resolve locally through the building-block
  register. The root only hosts $defs; it has no instantiable properties of its own.
type: object
$defs:
  laMcicpms_detectionLimitMethod:
    title: Detection Limit Method
    description: Reference or description of the method used to calculate session
      detection limits. Mandatory at analysis level. Must be consistent with the method
      applied to generate the Detection Limit values reported above.
    type: object
    properties:
      '@id':
        const: ada:reportedPropertyColumn/laMcicpmsTAPP/detectionLimitMethod
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: detectionLimitMethod
      schema:name:
        const: Detection Limit Method
      ada:dataType:
        const: uri
      schema:readonlyValue:
        const: true
      ada:tier:
        const: M
      schema:defaultValue:
        type: string
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - schema:defaultValue

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/registry/reportedPropertyColumns/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/registry/reportedPropertyColumns/schema.yaml)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/registry/reportedPropertyColumns`

