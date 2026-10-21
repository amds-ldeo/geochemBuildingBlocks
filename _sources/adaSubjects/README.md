# `adaSubjects` — schemas describing ADA's STORED record_subjects

This collection describes **ADA's stored input**, not the published product. Everything under
`BaseSchema/` and `techniqueProfile/` says what a conforming ADA metadata record looks like;
these say what the rows of `record_subjects` in `ada_subjects` actually contain, so that a
loader can validate them before composing anything.

Mixing the two is what produced the defect this collection answers. ADA's own
`subject_schemas` table is supposed to describe subjects and does not: 147 of its 160
`json_schema` values are CDIF **output** fragments, and 11% of 111,963 subjects share no key
with their assigned schema. Schema 169 (`STEMEDSCube`) declares `dataComponentResource` and
`cdif:hasPhysicalMapping` while its subjects carry `dataComponentType`, `description` and
`dimensions[]`. They validate only vacuously. See `metadata/docs/ada-subject-factoring.md`.

## NOT REGISTER BLOCKS, and the mechanism is the absence of `bblock.json`

There is no exclusion switch in `bblocks-config.yaml`. Measured: **251 directories hold a
`schema.yaml`, 251 hold a `bblock.json`, and `build/register.json` has 251 entries** — exactly
1:1, no exceptions. So `bblock.json` IS the register boundary, and a directory without one is
not published.

Every block here therefore has **no `bblock.json`**, deliberately. Do not add one to "make the
audit happy": that publishes it.

What still applies, because those tools discover by `schema.yaml` or `example*.json`:

| tool | sees this collection? |
|---|---|
| `resolve_schema.py` | yes — `rglob("schema.yaml")`, so `resolvedSchema.json` is generated and committed |
| `validate_examples.py` | yes — `rglob("example*.json")`, so the examples below are validated |
| `constraint_census.py` | yes — the blocks are counted |
| `audit_building_blocks.py` | yes, but `bblock.json` is NOT required here — see `NON_REGISTER_COLLECTIONS` |
| the OGC postprocess / register | **no** |

## Derived, not invented

Every property, type and `required` list comes from
`metadata/subject_schemas/inferred/*.json` — 133 schemas inferred from the stored subjects by
`metadata/loaders/infer_subject_schemas.py`, against which all 111,963 subjects validate.

**Pinned input: metadata commits `040f461` (the schemas) and `26ac25e` (the generator).** If
those are regenerated, the fragments here can drift silently — re-derive rather than assume.

## Property names are lowerCamelCase, and the data is not yet

Stephen's decision, 2026-10-20: **the schemas use lowerCamelCase and ADA normalises the data**,
rather than the schemas accepting both spellings. So these schemas legitimately REJECT some
stored subjects until that normalisation lands, and a rejection is not a schema bug.

Seven renames are outstanding ADA-side. The first four were known; `unitOfmeasure` and `Doi`
were found by a case-insensitive sweep after an initial capital-letter-only scan missed them,
and `OriginalName` has no lowerCamel form in the data at all:

| stored | should be | schemas | note |
|---|---|---|---|
| `OriginalName` | `originalName` | 15 | no lowerCamel form exists yet |
| `HeaderRowCount` | `headerRowCount` | 11 | 4 schemas carry BOTH |
| `Instrument` | `instrument` | 2 | |
| `Laboratory` | `laboratory` | 2 | |
| `unitOfmeasure` | `unitOfMeasure` | 2 | medial case; 1 schema carries both |
| `Format` | `format` | 1 | |
| `Doi` | `doi` | 1 | initialism lowercased; see the note below on the separate modelling question |

**`Doi` carries a second question that is NOT a rename, and the two were deliberately split**
(Stephen, 2026-10-21). The casing fix is free: `Doi` appears in exactly one schema
(`166-SIMSTabular`) as a plain string, and lowercase `doi` appears in **none**, so there is no
collision and no tie to break. But a DOI is an IDENTIFIER, and this repo's convention is
`schema:identifier` carrying a `propertyID` rather than a bare string under a type-named key —
so `Doi` is arguably mis-modelled as well as mis-cased. Remodelling it is a content change ADA
would make across its SIMS records; renaming it is a key change in a descriptive fragment.
Bundling them would have stalled the free fix behind a real migration, so `doi` lands now and
the identifier modelling is logged as an upstream question.

**Two decisions of 2026-10-21 close the other open items**, both resting on the rule in the
section above — the schema states the intended shape, ADA normalises:

- `imageType` is declared `array`, not `[array, string]`. An even 4/4 split cannot be decided
  by counting, so it is decided by the rule; accepting both would oblige every consumer to
  handle a scalar and a list forever. See `subjectRaster/description.md`.
- **`null` IS permitted** on `minVal`, `maxVal` and `displayInVizTool`, and this one does NOT
  rest on that rule — it is the exception to it. A name is a target the data should move to; a
  null is a fact about what ADA stores, and these fragments are descriptive, so forbidding null
  would fail real rows. See `subjectColumn/description.md` for the measurement that decided it.

## Type inconsistencies, same treatment

The schemas declare the DOMINANT type; the variants below are normalisation work, not accepted
unions. Listed rather than silently widened:

| key | stored as | note |
|---|---|---|
| `associatedFiles` | array in 24 schemas, **string in 3** | sometimes a bare filename |
| `imageType` | array in 4, `[array,string]` in 4 | |
| `channel2`, `channel3` | `string`, `null`, or `[null,string]` | null-vs-absent |
| `pixelScaleX`, `pixelScaleY` | number in 9, `[array,number]` in 1 | |
| `HeaderRowCount` | integer in 10, `[integer,string]` in 1 | |

## `context.jsonld` maps only terms that exist

Checked against `metadata/ada_metadata_forms/core/services/record_items.py:1313-1324`, which
maps `dimension`→`name`, `fieldDescription`→`description`, `colNum`→`index` on a
`cdi:DimensionComponent`. Where no clean CDIF/schema.org term exists the key is left unmapped
and listed in that block's `description.md` — inventing a term is how the mislabelling started.
