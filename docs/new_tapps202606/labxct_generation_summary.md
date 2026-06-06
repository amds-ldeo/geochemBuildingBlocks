# Lab-XCT TAPP generation summary (2026-06-04)

Generated the **labxctTAPP** protocol-definition BB + **detailLABXCT** analysis-detail BB and their
catalog/vocab contributions, from `docs/Lab-XCT_TAPP_v8.xlsx` (TAPP worksheet). First TAPP built
from Ruolin's new workbooks (which lack the `[schema path, matchComment, impl notes]` guidance
columns), so routing is driven purely by the two tier columns.

## Generators (reproducible, committed)
- `tools/build_labxct_from_spreadsheet.py` — routing → schemas + catalog `$defs` + vocab.
- `tools/build_labxct_examples.py` — representative validating example instances + `examples.yaml`.
- Routing precomputed in `labxct_routing.json`; gen index in `labxct_gen_index.json`.

## What was produced
| artifact | count | notes |
|---|---|---|
| `_sources/techniqueProtocols/labxctTAPP/` | 1 BB | extends `tappDefinition`; ~21 new `ada:` top-level props + `ada:methodParameters` |
| `_sources/analysisSpecificDetails/detailLABXCT/` | 1 BB | discriminates `ada:componentType`; 8 required analysis props + `schema:additionalProperty` anyOf |
| parameterTemplates `$defs` (appended) | 27 | `labxct_*`, Advanced-protocol params, `@id ada:parameter/labxctTAPP/<name>` |
| parameterValues `$defs` (appended) | 50 | `labxct_*`, Editable/Advanced-analysis values |
| `vocab/labxct_*.json` | 17 | `schema:DefinedTermSet` reference vocabularies |
| analyteColumns | 0 | XCT has no per-element analyte axis |

## Routing rules applied (per spec)
- **Protocol-Level Tier**: Basic → TAPP top-level property (`…Default` suffix if editable at analysis);
  Advanced → `ada:methodParameters` template.
- **Analysis-Level Tier**: Basic → required detail property; Read-Only → lives on TAPP;
  Editable/Advanced → `schema:additionalProperty` anyOf branch (parameterValues registry).
- Identity rows (name, technique, author, lab, dates, funding, target material, CT model, refs, DOI)
  populate **inherited** base-TAPP fields, not new `ada:` properties.
- Multi-volume-only detail fields (`ada:numberOfSubVolumes`, `ada:subVolumeOverlap`) are present but
  not globally required → single-volume datasets validate.

## Validation
- `examplelabxctTAPP-P0.json` and `exampledetailLABXCT-P0.json` both **PASS**
  `Draft202012Validator` against their locally-resolved `resolvedSchema.json`.
- `audit_building_blocks.py`: `[PASS] detailLABXCT` (+ `detailEMPA` unaffected; all profiles/properties pass).
- Both BBs carry the full required file set (bblock.json, schema.yaml, description.md, rules.shacl,
  examples.yaml, example JSON, resolvedSchema.json, *Schema.json; detail also context.jsonld).

## Follow-ups (NOT done — flag for decision)
1. **componentType consts** — detailLABXCT pins `ada:componentType` to PROPOSED values
   (`ada:XCTVolume`, `ada:XCTProjectionImageSet`, `ada:XCTSegmentationVolume`, `ada:XCTRenderedImage`,
   `ada:XCTQuantitativeTabular`). To wire into profile-level validation these must be added to the
   **Components worksheet** + the base file-type BB enums (image/dataCube/tabularData/…).
2. **labxctProfile** geochemProfile not generated (not requested) — needed to make instance docs
   reference labxctTAPP via `schema:measurementTechnique` and gate detailLABXCT fields.
3. **Pre-existing stubs**: `detailXCT` + `adaXCT` are older generic XCT placeholders that coexist.
4. **CI** (bblocks postprocess / annotate) is the only full check for registration + dangling-ref
   resolution — local green ≠ CI green.
5. Two cosmetic label variants in other new workbooks (Description vs Description / Purpose; Example
   spacing) — the generator reads exact header text, so normalize before running on LA-Q_SF-ICPMS.
