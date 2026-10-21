# ADA Subject — supporting document component

| key | schemas | subjects |
|---|---|---|
| `associatedFiles` | 27 | ~13,800 across the group |
| `supDocType` | 20 | |
| `originalName` | 15 (stored as `OriginalName`) | |

## This block names a key the data does not yet use

`OriginalName` has **no lowerCamel form anywhere in the 133 schemas**, so unlike
`HeaderRowCount` this is not a tie-break between two spellings — it is a rename the data has
not had. Every one of those 15 types therefore fails this block until ADA normalises. That is
the intended consequence of Stephen's 2026-10-20 decision, recorded in the README.

## `associatedFiles` has a type variant that matters

Array in 24 schemas, **plain string in 3** — a bare filename where the others hold a list.
Declared as an array of strings here. Its items carry no properties in any schema, so they are
scalars, not objects.

`supDocType` is `report`/`document_type`-style vocabulary; `record_items.py:522` records that
`report` / `supDocType` / `document_type` are the same axis under three names, which is its
own normalisation question and not one this block can settle.
