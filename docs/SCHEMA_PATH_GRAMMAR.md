# TAPP schema-path canonical grammar (v2)

The `schema path` in a TAPP workbook says **where a row's value belongs** in the JSON-LD instance
of the TAPP definition (`$MethodDefinition`, a `schema:Action`/`cdi:Activity`) or the dataset that
uses it (`$Dataset`). Human-authored paths use several inconsistent conventions; this is the single
**canonical** grammar an interpreter can parse. `tools/normalize_schema_paths.py` rewrites workbook
paths to this form (auto-fixing the mechanical cases, flagging the rest).

## Grammar

```
path      := root ( "." segment )*
root      := "$MethodDefinition" | "$Dataset"
segment   := curie [ "[]" ] [ selector ]
selector  := "[" curie "='" value "']"        # element of an array selected by key=value
curie     := ns ":" localname                 # colons only, never "." ; e.g. schema:name, ada:beamCurrent
```

### Roots and their aliases

Two canonical roots, distinguishing the reusable procedure from the analysis document:

- **`$MethodDefinition`** — the TAPP definition (a `prov:Plan`). Protocol-level and plan-scoped rows (Procedure-Level Tier = Basic/Advanced). Analyte columns are plan-level, so `$.` (self/context) is an alias for `$MethodDefinition` (e.g. `$.ada:analyteTemplate.ada:analyteColumns[]`).
- **`$Dataset`** — the technique **product document** root (the profile / analysis instance). Analysis-instance rows (Procedure-Level Tier = N/A) land here, mostly on existing cdif slots. The workbook may name the owning CDIF module instead of `$Dataset`; these are **aliases** normalized to `$Dataset`:
  - `$cdifCore` → `$Dataset` (owns `schema:contributor`, `schema:funding`, `schema:relatedLink`, `schema:creator`…)
  - `$cdifDiscovery` → `$Dataset` (owns `schema:measurementTechnique`, `dqv:hasQualityMeasurement`)
  - `$cdifProvenance`/`$cdifManifest`/`$cdifDataDescription` → `$Dataset` (module-annotated; same root)

- The **last** segment names the field the row's value sets (the *terminal*): typically
  `schema:value`, `schema:defaultValue`, `schema:description`, `schema:name`, `schema:url`,
  `schema:identifier`, `schema:termCode`. If a path ends at a selected array element with no terminal
  field, the row's value *is* that element (e.g. a tool name → a new `computationalTool`).
- Arrays are marked `[]`; a following `[key='v']` selects/creates the element where `key == v`.
- One row → one target. Rows that set multiple fields must be split into multiple rows (flagged, not
  auto-split).

## Canonical forms per family

<!-- BEGIN generated: families -->

*51 patterns across 49 families — two families are recognised by more than one shape. Generated from `tools/normalize_schema_paths.py` by `tools/gen_grammar_doc.py`; edit the recognizer, not this table.*

| family | canonical shape |
|---|---|
| `direct-ada` | `$MethodDefinition.ada:<name>[]?` |
| `dataset-scalar` | `$Dataset.ada:<name>[]?` |
| `analyte-template` | `$MethodDefinition.ada:analyteTemplate.ada:analyteColumns[]` |
| `analyte-identifier` | `$MethodDefinition.ada:analyteTemplate.ada:defaultAnalytes[]` |
| `reported-property-template` | `$MethodDefinition.ada:reportedPropertyTemplate.ada:reportedPropertyColumns[]` |
| `reported-property-identifier` | `$MethodDefinition.ada:reportedPropertyTemplate.ada:defaultReportedProperties[]` |
| `channel-template` | `$MethodDefinition.ada:channelTemplate.ada:channelColumns[]` |
| `channel-identifier` | `$MethodDefinition.ada:channelTemplate.ada:defaultChannels[]` |
| `method-variable-measured` | `$MethodDefinition.schema:variableMeasured[(schema:name='<value>')?](.schema:(name|description|unitText|propertyID|value|defaultValue))?` |
| `dataset-variable-measured` | `$Dataset.schema:variableMeasured[(schema:name='<value>')?](.schema:(name|description|unitText|propertyID|value))?` |
| `protocol-description` | `$MethodDefinition.schema:description` |
| `method-parameter` | `$MethodDefinition.schema:additionalProperty[schema:name='<value>'].schema:(value|defaultValue)` |
| `computational-tool` | `$MethodDefinition.bios:computationalTool[(schema:name|ada:toolRole)='<value>'](.schema:(name|description))?` |
| `computational-tool-list` | `$MethodDefinition.bios:computationalTool[]` |
| `related-link` | `$MethodDefinition.schema:relatedLink[schema:linkRelationship='<value>'].schema:target(.schema:(name|description|url))?` |
| `workflow-step` | `$MethodDefinition.schema:actionProcess.schema:step[schema:(name|additionalType)='<value>'](.schema:(name|description))?` |
| `workflow-step-ada` | `$MethodDefinition.schema:actionProcess.schema:step[schema:(name|additionalType)='<value>'].ada:<name>[]?` |
| `workflow-step-parameter` | `$MethodDefinition.schema:actionProcess.schema:step[schema:(name|additionalType)='<value>'].schema:additionalProperty[schema:name='<value>'].schema:(value|defaultValue)` |
| `workflow-step-reagent` | `$MethodDefinition.schema:actionProcess.schema:step[schema:(name|additionalType)='<value>'].bios:reagent[](.schema:(name|identifier))?` |
| `inherited-identity` | `$MethodDefinition.schema:(name|identifier|datePublished)` |
| `protocol-derived-from` | `$MethodDefinition.prov:wasDerivedFrom` |
| `protocol-sample-parameter` | `$MethodDefinition.schema:object[@type='<value>'].schema:additionalProperty[schema:name='<value>'].schema:(value|defaultValue)[]?` |
| `instrument-identity` | `$MethodDefinition.schema:instrument[schema:additionalType='<value>'].schema:(model|manufacturer)(.schema:[A-Z][A-Za-z]*)?.schema:name` |
| `instrument-identity` | `$MethodDefinition.schema:instrument[schema:additionalType='<value>'].schema:(name|identifier|additionalType|description)` |
| `instrument-direct-ada` | `$MethodDefinition.schema:instrument[schema:additionalType='<value>'].ada:<name>[]?` |
| `instrument-parameter` | `$MethodDefinition.schema:instrument[schema:additionalType='<value>'].schema:additionalProperty[schema:name='<value>'].schema:(value|defaultValue)` |
| `instrument-component` | `$MethodDefinition.schema:instrument[schema:additionalType='<value>'].schema:hasPart[schema:additionalType='<value>'].schema:(name|identifier|description)` |
| `instrument-component-ada` | `$MethodDefinition.schema:instrument[schema:additionalType='<value>'].schema:hasPart[schema:additionalType='<value>'].ada:<name>[]?` |
| `instrument-component-parameter` | `$MethodDefinition.schema:instrument[schema:additionalType='<value>'].schema:hasPart[schema:additionalType='<value>'].schema:additionalProperty[schema:name='<value>'].schema:(value|defaultValue)` |
| `inherited-identity` | `$MethodDefinition.schema:(creator|location|measurementTechnique|object|funding)\b.*` |
| `dataset-contributor` | `$Dataset.schema:contributor[schema:roleName='<value>'](.schema:(name|identifier))?` |
| `dataset-measurement-technique` | `$Dataset.schema:measurementTechnique(.schema:DefinedTerm)?.schema:identifier` |
| `dataset-provenance` | `$Dataset.prov:wasGeneratedBy.schema:(startDate|endDate|identifier)` |
| `dataset-prov-parameter` | `$Dataset.prov:wasGeneratedBy.schema:additionalProperty[schema:name='<value>'].schema:value` |
| `dataset-parameter` | `$Dataset.schema:additionalProperty[schema:name='<value>'].schema:value` |
| `dataset-step-parameter` | `$Dataset.prov:wasGeneratedBy.schema:actionProcess.schema:step[schema:(name|additionalType)='<value>'].schema:additionalProperty[schema:name='<value>'].schema:value` |
| `dataset-step` | `$Dataset.prov:wasGeneratedBy.schema:actionProcess.schema:step[schema:(name|additionalType)='<value>'](.schema:(name|description))?` |
| `dataset-activity-ada` | `$Dataset.prov:wasGeneratedBy.ada:<name>[]?` |
| `dataset-activity-description` | `$Dataset.prov:wasGeneratedBy.schema:description` |
| `dataset-location` | `$Dataset.prov:wasGeneratedBy.schema:location.schema:Place[schema:additionalType='<value>'].schema:(name|identifier)` |
| `dataset-used-identity` | `$Dataset.prov:wasGeneratedBy.prov:used.(?:schema:instrument|bios:computationalTool|prov:reagent)[(schema:additionalType|ada:<name>)='<value>'].schema:(name|identifier|description)` |
| `dataset-distribution` | `$Dataset.schema:distribution[].schema:encodingFormat[]` |
| `dataset-instrument-ada` | `$Dataset.prov:wasGeneratedBy.prov:used.schema:instrument[schema:additionalType='<value>'].ada:<name>[]?` |
| `dataset-instrument-parameter` | `$Dataset.prov:wasGeneratedBy.prov:used.schema:instrument[schema:additionalType='<value>'].schema:additionalProperty[schema:name='<value>'].schema:value` |
| `dataset-instrument-component-parameter` | `$Dataset.prov:wasGeneratedBy.prov:used.schema:instrument[schema:additionalType='<value>'].schema:hasPart[schema:additionalType='<value>'].schema:additionalProperty[schema:name='<value>'].schema:value` |
| `dataset-instrument-component-ada` | `$Dataset.prov:wasGeneratedBy.prov:used.schema:instrument[schema:additionalType='<value>'].schema:hasPart[schema:additionalType='<value>'].ada:<name>[]?` |
| `dataset-sample` | `$Dataset.prov:wasGeneratedBy.schema:object[@type='<value>'].schema:(name|identifier|description)` |
| `dataset-sample-parameter` | `$Dataset.prov:wasGeneratedBy.schema:object[@type='<value>'].schema:additionalProperty[schema:name='<value>'].schema:value` |
| `dataset-funding` | `$Dataset.schema:funding` |
| `dataset-related-link` | `$Dataset.schema:relatedLink[schema:linkRelationship='<value>'].schema:target(.schema:(name|url|description))?` |
| `dataset-quality` | `$Dataset.dqv:hasQualityMeasurement[dqv:isMeasurementOf='<value>'].dqv:value` |

<!-- END generated: families -->

## Normalization rules (what the normalizer auto-applies)

1. `scheme:` → `schema:`; `additiional` → `additional`; known property-name typos repaired
   (`measuremntTechnique`→`measurementTechnique`, `phaseIdentificatonMethod`→`phaseIdentificationMethod`,
   `meanAngularDeviaton`→`meanAngularDeviation`).
2. Dot-before-field → colon: `schema.name`→`schema:name`, `schema.value`→`schema:value`,
   `schema.description`, `schema.defaultValue`, `schema.object` (outside quoted literals).
3. Selector unification to `[curie='value']`:
   - `['X']` (bare literal on additionalProperty/hasPart) → `[schema:name='X']`
   - `[].schema:name:'X'` and `[].schema:name='X'` → `[schema:name='X']`
   - `[X]` (unquoted) → `[schema:name='X']`
   - `[name = 'X']` on `linkRelationship` → hoisted to `relatedLink[schema:linkRelationship='X']`
   - whitespace inside brackets collapsed.
4. `relatedLink[].schema:linkRelationship[name='X'].schema:target…` restructured to
   `relatedLink[schema:linkRelationship='X'].schema:target…`.
5. Doubled separators collapsed: `$MethodDefinition..schema:actionProcess` → `…​.schema:actionProcess`
   (outside quoted literals, where `..` may be part of a name).
6. `prov:used.<kind>[sel]` → `prov:used[sel]`, for `schema:instrument`, `bios:computationalTool` and
   `bios:reagent`. `adaProduct` defines `prov:used` as an array whose items **are** the instrument,
   tool or reagent, discriminated by their own selector key — there is no property to navigate into.
   Authors write the kind because it mirrors the `$MethodDefinition` path and reads better.

## Distinctions the grammar enforces, and why

**An `ada:` segment must be lowerCamel.** UpperCamel is the parser's `@type`-assertion syntax — it
is how `schema:DefinedTerm` and `schema:Place` work — so `ada:ReportedDateType` parses as a *type*
and emits **nothing**, while a looser recognizer happily calls it `direct-ada`. A path could
therefore pass every check and contribute no schema at all. UpperCamel `ada:` segments are now
rejected rather than silently dropped.

**`$Dataset.schema:additionalProperty[…]` and
`$Dataset.prov:wasGeneratedBy.schema:additionalProperty[…]` are different things.** The first
(`dataset-parameter`) is a property of the delivered DATA — the area a map covers, the dimensions of
a reconstructed volume. The second (`dataset-prov-parameter`) is a parameter of the SESSION — how
the instrument was configured. One session can yield products of differing extent, and a product
keeps its dimensions whether or not its provenance is described, so both spellings are legal and
**nothing normalizes one into the other**.

Related: a `$Dataset` path never carries a `Default`. The analysis records what was used; the
default lives on the procedure. Several families encode that with a negative lookbehind rather than
trusting authors to remember.

**A reported property (`schema:variableMeasured`) is dual-homed like a parameter, not like an
identity field.** `schema:variableMeasured[]` with no selector (or with identity terminals
`schema:name`/`description`/`unitText`/`propertyID`) *registers* a reported variable. But the
variable's value is dual-homed exactly as a `schema:additionalProperty` parameter is:
`variableMeasured[schema:name='X'].defaultValue` on `$MethodDefinition` is the procedure's registered
default, and `variableMeasured[schema:name='X'].value` on `$Dataset` is the value the analysis
reported. `method-variable-measured` and `dataset-variable-measured` carry the two homes; the
`value`/`defaultValue` split follows the same rule as every other parameter.

**A direct `ada:` property can sit on an instrument COMPONENT, not just the instrument.** An ICP-MS
Collector's `ada:collectorConfiguration` (its channel table) or `ada:defaultChannels` hangs off
`schema:instrument[…].schema:hasPart[…].ada:<name>[]` — the hasPart-level analogue of
`instrument-direct-ada`. `instrument-component-ada` (and its `$Dataset` partner
`dataset-instrument-component-ada`) recognize it.

## What the normalizer FLAGS for human review (does not guess)

- multi-target paths (`, ` / `|` / `and` joining several fields or properties)
- malformed: unbalanced brackets, trailing `.`, `"special handling"`, missing terminal
- the complex/inconsistent instrument `hasPart`/`additionalType` variants (several incompatible forms)
- any path that matches no family after auto-fixing

**A clean sweep here is necessary but not sufficient.** Recognition proves a path is well-formed,
not that it produces anything: confirm newly authored paths actually emit a property. The
UpperCamel case above is exactly this failure, and it went unnoticed for a whole delivery.
