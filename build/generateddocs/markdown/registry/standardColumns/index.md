
# Standard-Column Specification Registry (Schema)

`ogch.registry.standardColumns` *v0.1*

Registry of reusable schema:PropertyValueSpecification standard column definitions derived from technique TAPP workbooks. Each $def constrains one column of the standards table -- the reference materials a procedure calibrates against. A row of that table is a standard BY the thing it standardizes, so one standard appears once per target and the identifier column is not unique per row. TAPP building blocks reference these definitions via fragment $refs so they resolve locally through the building-block register. The root only hosts $defs; it has no instantiable properties of its own.

[*Status*](http://www.opengis.net/def/status): Under development

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/registry/standardColumns`

