# TAPP schema-path canonical grammar (v1)

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

Two canonical roots, distinguishing the reusable protocol from the analysis document:

- **`$MethodDefinition`** — the TAPP definition (a `prov:Plan`). Protocol-level and plan-scoped rows (Protocol-Level Tier = Basic/Advanced). Analyte columns are plan-level, so `$.` (self/context) is an alias for `$MethodDefinition` (e.g. `$.ada:analyteTemplate.ada:analyteColumns[]`).
- **`$Dataset`** — the technique **product document** root (the profile / analysis instance). Analysis-instance rows (Protocol-Level Tier = N/A) land here, mostly on existing cdif slots. The workbook may name the owning CDIF module instead of `$Dataset`; these are **aliases** normalized to `$Dataset`:
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

| family | canonical path |
|---|---|
| analyte identifier column | `$MethodDefinition.ada:analyteTemplate.ada:defaultAnalytes[]` |
| direct protocol property | `$MethodDefinition.ada:<name>` (append `[]` if list-valued) |
| protocol method parameter | `$MethodDefinition.schema:additionalProperty[schema:name='<Item>'].schema:value` (or `.schema:defaultValue`) |
| inherited identity field | `$MethodDefinition.schema:<name\|creator\|instrument\|location\|object\|funding\|datePublished\|identifier\|measurementTechnique>[…]` |
| computational tool (whole) | `$MethodDefinition.bios:computationalTool[<schema:name\|ada:toolRole>='<sel>']` — selected by role (`acquisition`, `dataReduction`) where the tool's NAME is the recorded value |
| computational tool field | `$MethodDefinition.bios:computationalTool[<schema:name\|ada:toolRole>='<sel>'].schema:<name\|description>` |
| related link target | `$MethodDefinition.schema:relatedLink[schema:linkRelationship='<rel>'].schema:target.<field>` |
| workflow step (whole/field) | `$MethodDefinition.schema:actionProcess.schema:step[schema:name='<step>'](.<field>)?` |
| workflow-step reagent | `$MethodDefinition.schema:actionProcess.schema:step[schema:name='<step>'].bios:reagent[](.schema:<name\|identifier>)?` |
| workflow-step parameter | `$MethodDefinition.schema:actionProcess.schema:step[schema:name='<step>'].schema:additionalProperty[schema:name='<param>'].schema:<value\|defaultValue>` |
| instrument identity | `$MethodDefinition.schema:instrument[schema:additionalType='<type>'].schema:<model\|manufacturer>.schema:name` (or `.schema:<name\|identifier\|additionalType\|description>`) |
| instrument direct property | `$MethodDefinition.schema:instrument[schema:additionalType='<type>'].ada:<name>` |
| instrument parameter | `$MethodDefinition.schema:instrument[schema:additionalType='<type>'].schema:additionalProperty[schema:name='<param>'].schema:<value\|defaultValue>` |
| instrument component | `$MethodDefinition.schema:instrument[schema:additionalType='<type>'].schema:hasPart[schema:additionalType='<component>'].schema:<name\|identifier\|description>` |
| instrument component parameter | `…schema:hasPart[schema:additionalType='<component>'].schema:additionalProperty[schema:name='<param>'].schema:<value\|defaultValue>` |
| dataset scalar | `$Dataset.ada:<name>` |
| dataset provenance | `$Dataset.prov:wasGeneratedBy.<schema:startDate\|schema:endDate>` |
| dataset prov parameter | `$Dataset.prov:wasGeneratedBy.schema:additionalProperty[schema:name='<param>'].schema:value` |
| dataset step parameter | `$Dataset.prov:wasGeneratedBy.schema:actionProcess.schema:step[schema:name='<step>'].schema:additionalProperty[schema:name='<param>'].schema:value` — analysis-tier half of a dual-homed step parameter. `value` only: a dataset records what was used, never a default |
| dataset sample | `$Dataset.prov:wasGeneratedBy.schema:object[schema:additionalType='materialsample'].schema:<name\|identifier\|description>` |
| dataset contributor | `$Dataset.schema:contributor[schema:roleName='<role>'](.schema:<name\|identifier>)?` |
| dataset funding | `$Dataset.schema:funding` |
| dataset measurement technique | `$Dataset.schema:measurementTechnique(.schema:DefinedTerm)?.schema:identifier` |
| dataset related link | `$Dataset.schema:relatedLink[schema:linkRelationship='<rel>'].schema:target(.schema:<name\|url\|description>)?` |
| dataset quality | `$Dataset.dqv:hasQualityMeasurement[dqv:isMeasurementOf='<measure>'].dqv:value` |

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

## What the normalizer FLAGS for human review (does not guess)

- multi-target paths (`, ` / `|` / `and` joining several fields or properties)
- malformed: unbalanced brackets, trailing `.`, `"special handling"`, missing terminal
- the complex/inconsistent instrument `hasPart`/`additionalType` variants (several incompatible forms)
- any path that matches no family after auto-fixing
