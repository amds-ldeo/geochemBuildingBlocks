# ADA Subject — tabular component

| key | schemas |
|---|---|
| `countRows` | 50 |
| `countColumns` | 50 |
| `columns` | 49 |
| `headerRowCount` | 43 |

`columns` composes `subjectColumn` by `$ref` rather than restating it — the point of the
fragment split. `record_items.py:1432-1436` passes `headerRowCount`, `countRows` and
`countColumns` straight through onto the file item, which is why they map to the `cdif:` terms
of the same name.

**Normalisation pending:** `HeaderRowCount` appears in 11 schemas and is not accepted here; 4
schemas carry both spellings. One of those 11 types it as `[integer,string]`.

**Nothing is `required`.** The counts differ (50/50/49/43), so the four keys do not co-occur
across all ~50 schemas, and a fragment that required them would be unusable by the types that
omit one.
