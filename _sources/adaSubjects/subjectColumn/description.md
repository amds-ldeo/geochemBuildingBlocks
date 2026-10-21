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

**`null` IS permitted on these three, and deliberately** (Stephen, 2026-10-21). A `null` in
`minVal`/`maxVal`/`displayInVizTool` means "not recorded" rather than a typing error, unlike
`HeaderRowCount`, so they are declared `[number, 'null']` and `[boolean, 'null']`.

The reasoning is different in kind from the lowerCamelCase decision, and the two should not be
read as one policy. A name is a TARGET the data should move to, so the schema states the target
and ADA normalises. A null is a FACT about what ADA stores today, and these fragments are
DESCRIPTIVE — so a schema forbidding null would fail real stored rows and be wrong about its own
subject. The decisive case is `187-VNMIRSpectralPoint`, whose `maxVal` is inferred
`["null","number"]`: null and real values coexist **for the same field**, so a null is an absent
value in some rows rather than a field this schema never uses. Measured over the 134 inferred
schemas: `minVal` 12 number / 2 null-only / 1 integer, `maxVal` 11 / 2 / 1 integer plus that
one `["null","number"]`, `displayInVizTool` 6 boolean / 1 null-only.

If ADA should stop storing nulls here, that is a separate data decision; until it lands, a
schema that forbids them documents a corpus that does not exist.

The `integer` variants need nothing: JSON Schema's `number` already admits integers, so
`236-GCCIRMSTabularIsotopicValues` validates against `[number, 'null']` as written.

**Unmapped:** `minVal`, `maxVal` (a range on an InstanceVariable, no single clean CDIF term)
and `displayInVizTool` (a viewer hint, not metadata).

**Not accepted:** `unitOfmeasure` (lowercase m), in 2 of the 14 shapes — see the README.
