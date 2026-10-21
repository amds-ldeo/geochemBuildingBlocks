# ADA Subject — dimensions

Three item shapes observed, all subsets of `{dimension, fieldDescription, unitOfMeasure,
fieldResource}`; `dimension` and `fieldDescription` are in all three.

`fieldResource` was **not** in the handover brief's list — it came out of the measurement.

The mapping is the one `record_items.py:1313-1324` actually performs: each dimension becomes a
`cdi:DimensionComponent` with `dimension`→`name`, `fieldDescription`→`description`,
`colNum`→`index`. Note `colNum` is a *column* key, not a dimension key, which is why it is
absent here.

**Unmapped:** `fieldResource` — it names an external resource for the dimension's values and
has no settled CDIF term.
