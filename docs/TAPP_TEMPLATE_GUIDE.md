# TAPP workbook → JSON guide

How to annotate a TAPP (Technique-Aligned Protocol Profile) Excel workbook so that
`tools/build_tapp.py` can generate the building-block JSON **reproducibly**. This is the
authoritative spec for the guidance fields. `docs/LA-Q_SF-ICPMS_TAPP_v3.xlsx` is the
reference model.

Generator: `python tools/build_tapp.py <tappName>` (one CLI for all techniques) +
`tools/build_<tapp>_examples.py` for the publication/synthetic examples. Routing follows the
canonical matrix in `docs/TierImplementationPatterns.xlsx`.

---

## 1. Worksheet layout

The data lives on a sheet named **`TAPP`**. Row 1 is the header. These columns are required
(detected **by header name**, so their position may vary):

| Column header | Purpose |
|---|---|
| `Metadata Item` | Human label for the field (col A). |
| `Description` / `Description / Purpose` | Field description (→ schema `description`). |
| `Procedure-Level Tier` (was `Procedure-Level Tier`) | `Basic` / `Advanced` / `N/A`. |
| `Analysis-Level Tier` | `Basic` / `Editable` / `Read-Only` / `Advanced` / `N/A`. |
| `Data Type` | e.g. `Numeric (kV)`, `Text (free)`, `Controlled list`, `Boolean`, `Integer`, `Date`, `URI`. |
| `Example/Allowed Content` | Sample value / pipe-delimited allowed values. |
| `Comments` | Free notes (not used by the generator). |
| *mode columns* (Y/N) | One column per analytical mode (see §6). Live **between `Comments` and `schema path`**. |
| `schema path` | The JSON target / role (see §3). **Authoritative for property names.** |
| `matchComment` | Optional CDIF-mapping notes. |
| `implementation notes` | Name tag + dataType + readOnly + enum (see §4). |
| `Literature Assessment` | Separator; publication columns follow it. |
| *publication columns* | One per source publication; cell = that field's value in that study. |

Tier values are case-normalised by the generator, but **use the canonical casing**
(`Basic`, `Advanced`, `Editable`, `Read-Only`, `N/A`).

---

## 2. The routing matrix (Procedure-Level × Analysis-Level)

| Protocol | Analysis | TAPP definition | Detail block (`detail<TAPP>`) |
|---|---|---|---|
| Basic | Read-Only / N/A | required `ada:<name>` (top-level) | — |
| Basic | Basic | required `ada:<name>` | required `ada:<name>` |
| Basic | Editable / Advanced | required `ada:<name>Default` | optional `ada:<name>` value |
| Advanced | Read-Only | `schema:PropertyValue` (fixed value) | — |
| Advanced | Editable / Advanced | `schema:PropertyValueSpecification` (`<name>Default`, `defaultValue`) | optional `ada:<name>` value |
| Advanced | Basic | `schema:PropertyValueSpecification` (`<name>Default`) | required `ada:<name>` |
| N/A | Basic / Editable / Advanced | — (dataset-level only) | analysis-level field |

Notes:
- **Basic = protocol property** (top-level `ada:`); **Advanced = method parameter** (an entry in
  `schema:additionalProperty[]`).
- **Advanced + Editable → `PropertyValueSpecification`** (the analyst can override; value goes in
  `schema:defaultValue`). Pinned to the `parameterTemplates` registry.
- **Advanced + Read-Only → `PropertyValue`** (fixed protocol value; value goes in `schema:value`).
  Pinned to the `parameterValues` registry.
- A Basic field that **no publication reports** (coverage 0) is emitted as **optional** rather than
  required.

---

## 3. `schema path` — role + name

The `schema path` value tells the generator the field's structural role. **For Basic/Advanced
fields the `ada:<name>` segment is the authoritative property name.**

| `schema path` pattern | Role |
|---|---|
| `$MethodDefinition.schema:name` / `.schema:creator` / `.schema:instrument…` etc. | **Inherited** base-TAPP field — not a new property. |
| `$MethodDefinition.ada:<name>` or `$.ada:<name>` | **Top-level `ada:` property** (Basic protocol). Name = `<name>`. |
| `$MethodDefinition.schema:additionalProperty['<item>'].schema:value` | **Advanced method parameter** (use this, not the legacy `$.ada:methodParameters[]`). |
| `$.ada:analyteTemplate.ada:analyteColumns[]` | **Analyte column** (per-element). |
| `$.ada:analyteTemplate.ada:defaultAnalytes[]` | **Analyte identifier** (the `Analyte` row). |
| `$.schema:description` | Maps to the protocol `schema:description`. |
| `$Dataset.…` | **Analysis-level / dataset** field → goes to the detail block, not the TAPP. |

The generator derives a property name as: clean `ada:<name>` segment of `schema path` (trailing
`Default` stripped) → impl-notes tag name → `camelCase(MetadataItem)`. Keep `schema path` and
`implementation notes` names in agreement.

---

## 4. `implementation notes` — tag format

One tag per role, lowerCamelCase name:

```
property: <name>        dataType: <type>   readOnly: <true|false>   enum: {A | B | C}
parameter: <name>       dataType: <type>   readOnly: <true|false>
analyteColumn: <name>   dataType: <type>   readOnly: <true|false>   enum: {…}
```

- A row may carry **multiple `analyteColumn:` tags** (one source row → several columns).
- `enum: {A | B | C}` generates a `schema:DefinedTermSet` vocabulary and wires it to the field.
- `dataType` values: `string`, `number`, `integer`, `boolean`, `date`, `uri`.

---

## 5. Naming rules

- **lowerCamelCase** (`beamCurrent`, not `BeamCurrent` or `beam_current`).
- **Do NOT bake `Default` into the name.** The generator appends `Default` automatically for
  Basic+Editable / Advanced+dual fields. Write the **base** name (`beamCurrent`, not
  `beamCurrentDefault`).
- A technique prefix is added only on a cross-technique **collision** with an incompatible
  definition; otherwise reuse the bare name (shared catalogs).

---

## 6. Mode columns + `ada:analyticalMode`

- The **mode columns** are the Y/N boolean columns between `Comments` and `schema path` (e.g.
  `Spot`/`Transect`/`Mapping`, `Single-volume`/`Multi-volume stitching`). A `Y` marks that a field
  applies in that mode.
- Their **headers are the `ada:analyticalMode` enum options**.
- Include an **`Analytical Mode`** row (`schema path` = `$MethodDefinition.ada:analyticalMode`).
  `ada:analyticalMode` is always emitted as a **list of strings** (an array) constrained to the mode
  options. Imaging techniques with no per-element axis still use modes (e.g. SEM, XCT).

---

## 7. `Analyte` row → `defaultAnalytes`

- The `Analyte` row's per-publication value is a **comma-delimited list** (e.g. `³¹P, ⁵¹V, ⁵³Cr`).
- Each value becomes one element of `ada:analyteTemplate.ada:defaultAnalytes`, carrying the required
  `analyte` key (mass numbers normalised, e.g. `31P`) plus any per-analyte values from the
  `analyteColumn` rows.
- Techniques with no per-element analyte axis (imaging: SEM, XCT) omit the `Analyte` row and the
  `analyteTemplate`.

---

## 8. Generating + adding a new TAPP

```
python tools/build_tapp.py <tappName>          # TAPP + detail + shared catalogs + vocab
python tools/build_<tapp>_examples.py           # publication / synthetic examples
```

To add a technique: register a `TAPP_CONFIGS` entry in `tools/build_tapp.py` (xlsx path,
`component_types`, identity `base_items`, `title`/`description`). The shared catalogs
(`analyteColumns`, `parameterTemplates`, `parameterValues`, `vocab`) are populated automatically
from the workbook. Validate with `python tools/validate_examples.py`.

---

## 9. Common problems to avoid (seen in review)

- Names with stray capitals (`AblationSpotDuration`) — must be lowerCamelCase.
- `Default` baked into the name (`spotGeometryDefault`) — write the base name.
- Copy-paste errors where the impl name belongs to another row (`property: cameraLength` on an
  EDS-mode row).
- `schema path` and `implementation notes` names disagreeing — reconcile to one authoritative name.
- Legacy `$.ada:methodParameters[]` schema paths — use `schema:additionalProperty` (the
  `ada:methodParameters` property was retired repo-wide).
- Typos in names (`elementalFractionalCorretion`, `nonlineraResponseCorrection`).
- Malformed tags (`property--`, `property : ada:<name>`) — use `property: <name>`.
