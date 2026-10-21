# ADA Subject — one column

`colNum` and `fieldDescription` are required: the only two keys present in **all 14** observed
item shapes across the 49 schemas carrying `columns`.

| optional key | in how many of the 14 shapes |
|---|---|
| `label` | 10 |
| `unitOfMeasure` | 9 |
| `fieldType` | 9 |
| `displayInVizTool` | 4 |
| `maxVal` | 3 |
| `minVal` | 3 |

Counts measured per SHAPE, not per schema — an earlier draft of this file hand-counted them
from a shape listing and got `label`, `unitOfMeasure` and `fieldType` wrong.

## Types declared are the dominant ones; these variants are normalisation work

Per the collection README: the schema states what a subject SHOULD look like.

| key | stored as | declared here |
|---|---|---|
| `minVal` | number 12, integer 1, **null 2** | `number` |
| `maxVal` | number 11, integer 1, null 2, `[null,number]` 1 | `number` |
| `displayInVizTool` | boolean 6, **null 1** | `boolean` |
| `fieldType` | string 26, `[null,string]` 1 | `string` |
| `colNum` | integer 49 | `integer` — no variant |

**One of these is not obviously a defect and may want a different answer.** A `null` in
`minVal`/`maxVal`/`displayInVizTool` plausibly means "not recorded" rather than a typing error,
unlike `HeaderRowCount`. If null should be permitted rather than normalised away, the fix is
`type: [number, "null"]` here and a note in the README — Stephen's call, not assumed.

**Unmapped:** `minVal`, `maxVal` (a range on an InstanceVariable, no single clean CDIF term)
and `displayInVizTool` (a viewer hint, not metadata).

**Not accepted:** `unitOfmeasure` (lowercase m), in 2 of the 14 shapes — see the README.
