# ADA Subject — common keys

`dataComponentType` (101 of 133 inferred schemas) and `description` (122).

**Neither is `required` in this fragment, deliberately.** 11 of the 133 types omit
`description` and 32 omit `dataComponentType`, so requiring either here would make the
fragment unusable by the types that do not carry it. A consuming type block adds them to its
own `required` where its own subjects all have them.

`dataComponentType` maps to `ada:componentType` — the same string the published product puts
on a `schema:hasPart` item, which is the one place these two worlds genuinely share a term.
