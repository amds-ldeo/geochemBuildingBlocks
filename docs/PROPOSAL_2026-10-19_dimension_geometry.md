# Dimension geometry for gridded products — research record and implementation brief

**Status: DEFERRED.** Not scheduled work. The recommendation this records is a *standing*
recommendation at CDIF ([profile-datastructure#10](https://github.com/Cross-Domain-Interoperability-Framework/profile-datastructure/issues/10),
open), and the gBB implementation is deferred as a deeper problem with wider ramifications
than it first appears. This document exists so that whoever picks it up does not have to
redo the research, and does not re-litigate decisions that were already settled with
evidence.

Written 2026-10-19.

---

# Part 1 — The question and the answer

**The question.** Should a dimension's size (extent) be specified in the
`dimensionComponent`, or is it part of the valueDomain definition for the instance or
represented variable? And how is it represented in DDI-CDI?

**The answer: neither, and not as a "size" at all.** In DDI-CDI it has no representation.
`cdi:DimensionComponent` is a keying role — "the variable acts as a field in the compound
identifier (the key structure) to disambiguate the cells in the multi-dimensional 'cube'"
— and `cdi:ValueDomain` is a "set of permissible values". A count belongs to neither by
definition, not merely by omission.

The reason it belongs nowhere is that **the thing wanted is not a scalar.** A dimension's
domain takes one of three forms, and in all three the count is already entailed:

| the dimension is | described by | count follows from |
|---|---|---|
| categorical | the existing enumeration / codelist | the item scheme |
| continuous, regularly sampled | start, increment, optional end | those three |
| continuous, irregularly sampled | the enumerated coordinates | the coordinate array |

So a `dimensionSize` property would be redundant in every case and sufficient in none — a
second source of truth that can disagree with the data. What is missing is not size but
**axis geometry**.

**The recommendation** (full text in #10, six points, abridged here):

1. Do not mint a `size` or `dimensionSize` property.
2. Describe the domain and let the extent follow. The selector already exists:
   `cdi:ValueAndConceptDescription.classificationLevel`, typed `CategoryRelationCode` —
   "nominal, ordinal, interval, ratio, or **continuous**."
3. Align with SDMX 3.0's facet set rather than designing one: `isSequence`, `startValue`,
   `interval`, `endValue`, with `timeInterval` / `startTime` / `endTime` for a temporal
   axis, and an enumerated representation for the other two cases.
4. Take the increment's **value type** from ISO 19115-1, not SDMX:
   `MD_Dimension.resolution` is a `Measure` and carries a unit; SDMX's `interval` does
   not. For a physical axis — micrometres per slice — the unit is not optional. **This is
   the only place CDIF has to make a choice.**
5. Keep `endValue` optional and treat its absence as meaningful: per SDMX, "if an end
   value is not given, then the sequence continues indefinitely."
6. Place it at the **physical** layer, beside `cdi:locator` / `cdif:LocatorMapping`, not
   on `DimensionComponent` or `ValueDomain`.

---

# Part 2 — How that was arrived at

Recorded because the conclusions are only as good as the survey, and because two of them
were wrong on the way and were corrected.

## 2.1 What each standard actually does

| standard | size / extent | resolution / spacing |
|---|---|---|
| **ISO 19115-1 `MD_Dimension`** | `dimensionSize` — Integer, **mandatory**, "number of elements along the axis" | **`resolution`** — `Measure`, optional |
| **SDMX 3.0** | none, and none needed | **`interval`** — "the permitted interval (increment) in a sequence" |
| **DAP4** | `<Dimension name="n" size="s"/>` — explicit, positive integer | **none** |
| **W3C Data Cube (QB)** | none | none |
| **DDI-CDI** | 1-D only — `PhysicalDataSet.recordCount` | none |
| **science-on-schema.org** | none — explicitly deferred | none — explicitly deferred |

**DDI-CDI**, verified against `ddi-cdi_ea15.2026.March` (281 classes, 368 distinct
attributes): `DimensionComponent` has exactly one attribute, `categoricalAdditivity`.
`ValueAndConceptDescription` has `classificationLevel`, min/max inclusive and exclusive,
`formatPattern`, `logicalExpression`, `regularExpression`. `EnumerationDomain` has
identifier/name/purpose and no member count. `DescriptorValueDomain` and
`SubstantiveValueDomain` have no attributes at all. No class in the model mentions grid,
array, axis, raster, cube or tensor. The only cardinality anywhere is
`PhysicalDataSet.recordCount`, which is 1-D and physical.

**DAP4 splits the question cleanly.** The dimension declaration holds "only a name and a
size… not coordinate values, resolution, or spacing"; coordinate values come from separate
rank-one variables linked by `<Map>`, needed to complete "the sampling of" the domain. So
DAP4 handles size and not resolution — which reconciles an apparent contradiction with
[science-on-schema.org#209](https://github.com/ESIPFed/science-on-schema.org/issues/209),
where OPeNDAP v4 is said not to handle this case: that issue is titled about *resolution*.

**SDMX 3.0 carries the whole regular-axis geometry**, and is the closest fit of anything
surveyed. From Section 2's Facet Type table:

- `isSequence` — "indicates whether the values are intended to be ordered… If this
  attribute holds a value of true, a start value or time and a numeric or time interval
  **must** be supplied. If an end value is not given, then the sequence continues
  indefinitely."
- `interval` — "specifies the permitted interval (increment) in a sequence."
- `startValue` — "indicates the starting point… **mandatory** for a numeric sequence."
- `endValue` — "that ending point (if any)."
- `timeInterval` / `startTime` / `endTime` — the same three for a time axis.
- plus `minValue` / `maxValue`, `minLength` / `maxLength`, `decimals`, `pattern`.

And because a Representation is either *enumerated* (`Codelist` / `ValueList` /
`GeoCodelist`) or *non-enumerated* (Facets), SDMX covers all three cases of §1 — with no
size facet, because in each one the count is entailed. That is a stronger argument against
minting a size than the derivability reasoning above: it is a mature standard's realised
design rather than an inference.

**science-on-schema.org** uses `additionalType` `qudt:MultiDimensionalDataFormat` with
dimensions as `variableMeasured` `PropertyValue`s keyed `qb#measureDimension`, and says
plainly that it does not propose "how to represent the sampling points along the various
dimension" and that "the details of the sample spacing along each dimension are not
described in this scheme", deferring to OPeNDAP DMR or W3C DataCube.

## 2.2 The real decision: two standards disagree about which fact is primitive

This is the sharpest framing of the problem, and the one a CDIF decision actually turns on.

| | SDMX 3.0 facets | ISO 19115 `MD_Dimension` |
|---|---|---|
| primitive | the **generator**: start + interval | the **count**: `dimensionSize` |
| count | entailed, never stated | stated, mandatory |
| unbounded axis | expressible (omit `endValue`) | not expressible |
| unit on the spacing | no — `interval` carries none | yes — `resolution` is a `Measure` |
| failure mode | none obvious | a stated size can contradict the data |

So the question is not "does a term exist" — two standards have one — but **which design
to adopt**. The recommendation's answer is a synthesis of two realised designs rather than
an invention: **SDMX's facet names with ISO's unit-bearing value type.** SDMX has the right
structure and no unit; ISO has the unit and the wrong primitive. That is the gap, precisely
identified, and it is the only part CDIF has to decide for itself.

Note also that `ValueAndConceptDescription`'s min/max map onto SDMX's
`minValue`/`maxValue`, so "generalise DDI-CDI's existing bounds into geometry" and "adopt
the SDMX sequence facets" are **one request seen from two sides** — and since QB derives
from SDMX, DDI-CDI would be aligning rather than extending alone.

## 2.3 Evidence from a real record

A NOAA ERDDAP ISO 19115 record (`ncdcOisst21Agg.iso19115`) carries four `MD_Dimension`
blocks. All four carry a `dimensionSize` **value** (1440, 720, 1, ~15273 — the temporal
axis grows between fetches, it is a live aggregation). What is nil'd is the spacing:

```xml
<gmd:resolution gco:nilReason="inapplicable"/>
```

on the `zlev` axis. **The count was consistently available; the spacing was not.** Two
consequences: a design that depends on reading spacing from a container will more often
find nothing, and this is a point for ISO's primitive rather than against it.

The same record carries a second, better finding: the `zlev` axis has
`dimensionName codeListValue="unknown"`. A depth axis could not be named from
`MD_DimensionNameTypeCode` (row, column, vertical, track, crossTrack, line, sample, time).
That is a live instance of the point made in science-on-schema.org#209 — and it bears on
design, not just on ISO's quality: **any scheme keyed on an ISO-style dimension-name
codelist inherits that failure.**

## 2.4 Corrections made during the research

Recorded deliberately, because each was asserted before being checked and the record is
more useful with them than without.

1. **"SDMX has no size and no resolution" was wrong.** The first survey recorded SDMX as
   "no / no" on the strength of the 2.1 information model, flagging 3.0's representation
   facets as unexamined. SDMX 3.0 in fact carries the entire regular-axis geometry (§2.1).
   This was the one row that changed the recommendation, and it was corrected in #10 by a
   follow-up comment rather than by editing, so both the error and the fix stay legible.
2. **"ISO carries it too, so the premise was wrong twice" was wrong.** ISO was in the
   original survey table as carrying both, and was called "the only one carrying both".
   Only the SDMX row was in error.
3. **"Real ISO records nil `dimensionSize` despite it being mandatory" was unsupported.**
   Offered as evidence that the scalar is not always knowable; the record checked shows the
   opposite (§2.3). The claim originated in a search engine's characterisation of an
   unnamed record, repeated as though the record had been read. Not in play unless someone
   produces a record that actually shows it.

## 2.5 Method notes

- **The DDI-CDI XMI export does not carry class-level documentation** — only
  attribute-level. A naive read hands you the *first attribute's* description as the
  class's (`EnumerationDomain` appears to mean "Identifier for objects requiring short- or
  long-lasting referencing and management", which is its `identifier` attribute's prose).
  Use the **XMI** (`cdif-umlmodel/xmiModels/ddi-cdi_ea15.2026.March.xml`) for structure and
  enumeration — all 281 classes at once — and the **EA bridge**
  (`mcp__ea-sparx__find_elements_by_name`) for class definitions. The failure modes are
  opposite: XMI misattributes prose; the EA bridge makes you walk classes one at a time and
  tempts you to stop early, which is how the physical layer was missed on a first pass.
  Neither alone is sufficient. Note the XMI is `windows-1252` and the doc tag is
  `description`, not `documentation`.
- **The SDMX 3.0 Section 2 PDF is Flate-compressed**, so fetching it returns raw PDF
  syntax rather than text. `pypdf` `extract_text()` across all 163 pages, then grep, is
  what worked. The Facet Type table is at pages 44–46.

---

# Part 3 — Implementation brief for gBB

## 3.1 The single most important thing: this is not greenfield

`_sources/BaseSchema/spatialRegistration/schema.yaml` **already implements the
recommendation**, narrowly, for two or three spatial axes:

| gBB today | #10 / SDMX equivalent |
|---|---|
| `ada:originX` / `ada:originY` / `ada:originZ` | `startValue` |
| `ada:pixelScaleX` / `ada:pixelScaleY` (in `$defs/Scaling`) | `interval` |
| `ada:pixelUnits` (in `$defs/Scaling`) | the unit on the increment — point 4, **already done** |
| `ada:pixelRotationX/Y`, `ada:coordDef`, `ada:coordUnits`, `ada:originLocation`, `ada:worldFile` | beyond #10's scope (affine registration) |

In use: `ada:pixelScaleX` 759 occurrences, `ada:pixelScaleY` 592, `ada:pixelUnits` 552.

**So the task is to generalise an existing gBB pattern, not to invent one** — from two or
three hardcoded spatial axes to *n* named axes of any kind. That is the same move #10 asks
CDIF to make; gBB already made it for the spatial case. Framing it this way matters twice:
the design is already validated against a real corpus, and the work must not build a
second, parallel way to say the same thing.

What `Scaling` lacks and the work must add:

- an **end / bound** (`endValue`), with its absence kept meaningful (point 5)
- an explicit **ordered-sequence flag** (`isSequence`), which is what makes start+interval
  well-formed rather than incidental
- **generalisation beyond spatial axes** — no time, composition, pressure or temperature
  axis is expressible today
- **per-axis structure** rather than `X`/`Y`/`Z` baked into property names
- the **irregular case** — an enumerated coordinate array. Nothing in gBB expresses it.

**First decision, from which the rest follows:** does the new geometry *supersede*
`Scaling` — with `pixelScaleX/Y` retired onto it, as `ada:numPixelsX/Y` were retired onto
`schema:width`/`schema:height` in #107 — or sit *beside* it for the spatial case? Retiring
is cleaner but touches ~1900 occurrences. See §3.5.

## 3.2 State of dimension modelling in gBB

Verified, not assumed:

- **No gBB source schema declares `cdi:DimensionComponent`.** Zero `schema.yaml` files.
  Dimensions are not modelled here at all today.
- `_sources/BaseSchema/dataCube/schema.yaml` is **58 lines**: an `@type` pin (`ada:dataCube`
  + `cdi:StructuredDataSet`) and an `ada:componentType` enum of cube kinds
  (`ada:FTICRMSCube`, `ada:STEMEDSCube`, `ada:STEMEDSTomo`, `ada:VNMIRSpectralMap`, …). It
  says *what kind* of cube and nothing about its axes. **The obvious host block.**
- Axis-ish properties that exist but are not a dimension model: `ada:imageStackDimensions`
  (43 occurrences), `ada:numberOfSlices` (6). Both are candidates to be expressed by the
  new geometry and then retired.
- `ada:numPixelsX` / `ada:numPixelsY` are **already retired** (#107) onto `schema:width` /
  `schema:height` as `schema:QuantitativeValue` objects, and survive only in
  `PixelDimension`'s explanatory prose in `image/schema.yaml`. Do not re-add them; do read
  that prose, which records why a pixel *count* and a pixel *size* are different
  properties — a distinction this work must preserve.

## 3.3 Where it attaches

```
geochemProduct  --$ref-->  cdifDataStructure#/$defs/DimensionalDataStructure
                             cdi:has_DataStructureComponent: [ anyOf
                               IdentifierComponent | MeasureComponent |
                               AttributeComponent | DimensionComponent | ... ]
```

and in metadataBuildingBlocks, `cdifDataType/cdifDataStructureComponent#/$defs/DimensionComponent`
declares exactly `@type`, `@id`, `cdif:isDefinedBy_Variable` (required: `@type`,
`cdif:isDefinedBy_Variable`).

Per point 6 the geometry does **not** go on `DimensionComponent` — it is a keying role. But
that is where an axis's *identity* lives, so the physical geometry must key to it, either
to the component's `@id` or to the variable in its `cdif:isDefinedBy_Variable`. **Second
decision: pick one and write down why.** It determines whether geometry is addressable per
axis or only per cube.

The physical layer in gBB is reached via `cdif:hasPhysicalMapping` (used in
`structuredData`, `tabularData`, referenced from `geochemProduct/schema.yaml:548`).
`cdi:locator` appears in gBB only in *resolved* artifacts, inherited from mBB — not in any
gBB source. So "beside `cdi:locator`" means beside gBB's `cdif:hasPhysicalMapping` usage,
not adding a `cdi:locator` of its own.

## 3.4 Gates it must pass

Run the full pipeline, then all of these — they are CI-enforced:

```
python tools/regenerate.py
python tools/validate_examples.py              # expect "N passed, 0 failed"
python tools/check_additionaltype_policy.py
python tools/validate_inline_examples.py
python tools/validate_counterexamples.py
python tools/constraint_census.py              # then --write, attributing every line
python tools/check_data_type_agreement.py --self-test --emitters --strict
python tools/check_step_names.py
```

**`check_additionaltype_policy.py` will bite if a new pinned value is an identifier.**
Rule A has no allowlist and gates CI: a value matching
`^[A-Za-z][A-Za-z0-9+.\-]*:[^\s"]+$` must be serialized as an IRI reference, not a bare
string; a free label stays a string. For a selector token pinned on
`schema:additionalType` or `schema:propertyID`, `schema_path_emitter._token_const` already
emits the required string-or-`{"@id"}` pair — and it is **scoped to those two keys**,
deliberately, because `@type` members are bare IRI strings and the dual form is wrong
there. Do not widen that scoping; its comment records the measurement (661
`additionalType` selector occurrences, none identifier-shaped; 127 `@type`, all of them).

**`constraint_census.py` refuses growth as well as loss.** Adding properties will move it.
Attribute every changed line *before* `--write`, and check specifically for **decreases** —
a lost constraint only makes a schema more permissive, so every example that passed still
passes.

## 3.5 Precedent for the retirement, if `Scaling` is superseded

#107 retired `ada:pixelSize`, `ada:numPixelsX` and `ada:numPixelsY`; #109 then corrected
it. Two lessons, both worth not repeating:

1. **`ada:pixelSize` was retired onto the wrong replacement.** It is a physical pixel
   *size*, not a *count*, so `schema:width`/`schema:height` could not express it; the
   correct supersession was `ada:spatialRegistration.ada:pixelScaleX/Y` with
   `ada:pixelUnits`. A retirement note naming the wrong successor is worse than none.
2. **Retiring a property breaks downstream emitters, not just schemas.** #107 did not check
   writers; the `amds-ldeo/metadata` forms app was still emitting the retired names, and
   the method-definition editor (`static/js/method_definition_editor.js`,
   `templates/core/method_definition_edit.html`) was missed even by the first fix sweep
   there. **If you retire anything, grep `amds-ldeo/metadata`** — `loaders/`,
   `ada_metadata_forms/`, `adaMetadataViews/` — and tell that project.

## 3.6 Suggested sequence

1. Decide: supersede `Scaling` or sit beside it (§3.1). Everything follows from this.
2. Decide: geometry keys to `DimensionComponent.@id` or to `cdif:isDefinedBy_Variable` (§3.3).
3. Add the geometry `$defs` to `dataCube` (or a new block it `$ref`s), covering the three forms.
4. Express `ada:imageStackDimensions` and `ada:numberOfSlices` with it; retire them if it works.
5. One example per form — regular, irregular, categorical — and a `tests/*-fail.json` per
   form that fails for the constraint its filename names.
6. Full pipeline and all gates (§3.4), census attributed before `--write`.
7. Report back to #10. It is a standing recommendation, and implementation experience is
   the thing most likely to change it.

---

# Part 4 — Still open

[profile-datastructure#11](https://github.com/Cross-Domain-Interoperability-Framework/profile-datastructure/issues/11)
— when a container already carries the geometry, does CDIF restate it or point at it?

**This does not block the Astromat case.** XCT products are image stacks and the container
carries no axis geometry, so for those the record must state it. #11 governs only the
self-describing case (NetCDF, HDF5), where both standards' arguments apply: a
self-describing format is authoritative about its own shape, but a record that defers to it
is useless for the discovery decision metadata exists to support. Build for the
non-self-describing case and do not bake in an assumption that restating is always correct.

---

# Part 5 — Traps

- **DDI-CDI has three names that look like answers and are not**: `extent` (an attribute of
  `PairedControlledVocabularyEntry`), `StructureExtent` (the type of
  `PhysicalDataSetStructure.totality` — a coverage-completeness flag), and `Step` (`script`
  + `scriptingLanguage` — a *process* step, not an axis step).
- **SDMX's change history is misleading.** "Removed interval and enumeration from Facet"
  refers to the UML *attributes* of the `Facet` class — in 3.0 a Facet is `facetType` +
  `facetValue` + `facetValueType`, so `interval` became a facetType *value*. The facet is
  alive and documented nine pages later in the same specification.
- **ISO's `dimensionName` is a codelist and does not generalise** (§2.3).
- **The XMI export lacks class-level documentation** (§2.5).
- **gBB is a shared checkout.** Other sessions work in it; `main` moves on its own via CI
  auto-commits ("Building blocks postprocessing"). `git fetch` and check the current branch
  before committing.

---

# Sources

- [profile-datastructure#10](https://github.com/Cross-Domain-Interoperability-Framework/profile-datastructure/issues/10) — the recommendation and the full survey, in three comments
- [profile-datastructure#11](https://github.com/Cross-Domain-Interoperability-Framework/profile-datastructure/issues/11) — the open duplication-policy question
- [science-on-schema.org#209](https://github.com/ESIPFed/science-on-schema.org/issues/209) — the equivalent question for schema.org, open since 2022
- [DAP4 specification](https://opendap.github.io/dap4-specification/DAP4.html), section 1.5.9
- [science-on-schema.org Experimental.md](https://github.com/ESIPFed/science-on-schema.org/blob/main/guides/Experimental.md#array-gridded-or-coverage-data), "Array, Gridded or Coverage Data"
- [SDMX 3.0 Section 2 — Information Model](https://sdmx.org/wp-content/uploads/SDMX_3-0-0_SECTION_2_FINAL-1_0.pdf), Facet Type table at pp. 44–46
- [GeoAPI `Dimension`](https://www.geoapi.org/snapshot/javadoc/org.opengis.geoapi/org/opengis/metadata/spatial/Dimension.html) for `MD_Dimension` members
- DDI-CDI UML: `cdif-umlmodel/xmiModels/ddi-cdi_ea15.2026.March.xml`
