# EMPA → EPMA: full rename scope

**Decision (2026-10-03):** standardise on **EPMA** everywhere, retiring the legacy `EMPA`
spelling — identifiers, derived names, directories and filenames. This supersedes the earlier
"EPMA for new things only" position.

**Owner:** the gBB work belongs to the **TAPPS** session (it owns
`C:\GithubC\amds-ldeo\geochemBuildingBlocks`, knows the generator, and has to run the
regeneration). The `metadata`-side follow-up is listed at the end and waits on gBB republishing.

**Why this is durable:** `empaTAPP` appears **zero times** in the upstream `tapp/` delivery. The
workbook is already EPMA (`TAPP_EPMA_filled.xlsx`, `EPMA_TAPP_v87.schemapaths.csv`). The legacy
spelling is gBB's own identifier choice, so renaming it will not be reverted by the next intake.

---

## Inventory (gBB, excluding `build/`)

| spelling | files | occurrences |
|---|---|---|
| `EMPA` (all forms) | 589 | 3541 |
| `empaTAPP` | 122 | 1834 |
| `empa_` (vocab filenames and ids) | 31 | 408 |
| `detailEMPA` | 57 | 88 |
| `adaEMPA` | 26 | 76 |
| `exampleempaTAPP` | 7 | 25 |

## What has to change together

1. **Identifier** `empaTAPP` → `epmaTAPP`. It is a *configuration key*, not a derived string.
   The live one is **`TAPP_CONFIGS` in `tools/build_tapp.py`** (the `"empaTAPP": {...}` entry, and
   the `{"empaTAPP": "EMPA", ...}` id→directory map above it) — which is also the file CLAUDE.md
   names for this ("edit build_tapp.TAPP_CONFIGS"). `tools/_tapp_lib.py` carries a SECOND id→
   directory map and a docstring describing a `_build_empaTAPP.py` entry point that no longer
   exists; it is legacy and must be changed too, but it is not where the configuration lives.
   ~20 tools reference the key.
2. **Derived detail name** `detailEMPA` → `detailEPMA`. Derived as strip-`TAPP` + uppercase
   (`'empaTAPP' → 'detailEMPA'`), so it follows the id automatically — but `DETAIL_NAME` and the
   hardcoded `detailEMPA` strings (88 occurrences) do not.
3. **Profile name** `adaEMPA` → `adaEPMA`. This appears in each schema's
   `schema:subjectOf.dcterms:conformsTo` const, which is what the forms app builds its profile
   index from. Renaming it is a breaking change for that index — see the metadata section.
4. **Technique directory** `_sources/techniqueProfile/geochemProfile/EMPA/` → `EPMA/`, with its
   `tapp/`, `detail/`, `profile/` and `profile-ada/` children.

   **The directory and the example filenames are driven by different identifiers, so renaming the
   folder does not rename the examples.** Example files are written as
   `f"example{tapp}-{code}.json"` and `f"example{detail_name}-{code}.json"`
   (`build_tapp_examples.py:1450,1470`), so `exampleempaTAPP-*.json` follows item 1 (`empaTAPP` →
   `epmaTAPP`) and `exampledetailEMPA-*.json` follows item 2 (`detailEMPA` → `detailEPMA`). Rename
   the folder alone and you get `EPMA/tapp/exampleempaTAPP-P1.json` — consistent with nothing. The
   three renames have to land together.
5. **26 vocab files** `_sources/registry/vocab/empa_*.json` → `epma_*.json`, their `@id`s
   `ada:vocab/empaTAPP/*` → `ada:vocab/epmaTAPP/*`, and the term URIs nested under each (20 terms
   in `diffractingCrystal` alone).
6. **Registry column and parameter URIs**: `ada:targetSpeciesColumn/empaTAPP/*`,
   `ada:monitoredPropertyColumn/empaTAPP/*`, `ada:targetMaterialColumn/empaTAPP/*`,
   `ada:parameter/empaTAPP/*`.
7. **Product-type enum labels** in `_sources/BaseSchema/adaProduct/schema.yaml` — four members:
   `Electron Microprobe Analysis (EMPA)`, `… (EMPA) Collection`, `… Image (EMPA)`,
   `… Quantitative Elemental Abundances (EMPAQEA)`.
8. **Tool filename** `tools/build_adaEMPA_examples.py`.
9. **Full regeneration** to propagate into 241 `resolvedSchema.json`, the examples and the mirrors.
10. **`build/`, which the inventory above excludes but which is tracked** — 5005 files, **183 of
    them under `build/annotated/techniqueProfile/geochemProfile/EMPA/`** — and
    `build/register.json`, whose entries embed the spelling in *published* identifiers
    (`ogch.techniqueProfile.geochemProfile.EMPA.detail`,
    `ogch.techniqueProfile.geochemProfile.EMPA.profile-ada`). Those identifiers are
    consumer-facing, so this is not only internal churn.

    CI's reusable postprocess regenerates `build/` and commits it (`8d46c08d7` touched 3301 files
    there), so it should follow the source rename without hand editing. What is NOT established is
    whether the postprocess DELETES a directory that has gone away or only adds the new one. If it
    only adds, both spellings will sit in `build/` indefinitely. Check after it runs, rather than
    assuming either way.

## Hazards, each with evidence

- **`TAPP_NAME = "empaTAPP"` is the module default.** `_tapp_lib.py` says so outright: "Default
  behavior is empaTAPP, so existing …". A tool that never calls `configure()` silently targets this
  technique, so the default has to stay coherent through the rename rather than be left pointing at
  a key that no longer exists.
- **The directory rename is narrower than it looks — but it breaks the forms app's TAPP index.**
  Measured: **no `$ref` in `_sources/` contains `EMPA`** (refs are relative and point upward, e.g.
  `../../../registry/parameterValues/schema.yaml#/$defs/…`), so the usual
  "`$ref` silently stops being inlined" hazard does **not** apply to this rename. Inside gBB the
  directory name is held in just two places: `build_profile.PROFILES["empaTAPP"]` —
  `dict(dir="EMPA", short="EMPA", cid="adaEMPA", …)`, one line carrying the directory, the short
  code *and* the profile id — and the `{"empaTAPP": "EMPA", …}` map in `_tapp_lib.py`. The rest is
  documentation.

  The real coupling is **downstream**: `schema_registry._build_tapp_index()` keys its index on the
  *directory* name (`technique = schema_yaml.parent.parent.name`, normalised). Rename the folder and
  the key becomes `EPMA`, at which point the existing alias `{"EPMA": "EMPA"}` maps a correct input
  to a key that no longer exists and TAPP lookup for this technique fails. So the alias inversion
  below is not tidying — it is **required in the same change** as the directory rename.
- **Two vocab files already mix both spellings**: `empa_epmaTechniquePerAnalyte.json` and
  `empa_epmaTechniquePerTargetSpecies.json` — legacy prefix, standard spelling inside. Do not
  assume the file prefix and the content agree anywhere.
- **`adaProduct`'s enums are sealed.** Per the forms app's own notes, a label mismatch alone was
  enough to fail every record of this technique on the profile's `contains`. The enum and whatever
  produces the label have to move in one step.
- **The 5 `profile-ada` Phase-0 holds are QRIS, RAMAN, VNMIR, XANES, XRD** — none is EMPA, so the
  expected audit result is unchanged at 237/242. A sixth failure after this work means something
  real broke.
- **Cost:** a full `regenerate.py` is now ~144 minutes (resolve alone 107, measured 2026-10-02) and
  **does not fit a two-hour window**. A run cut off mid-`resolve` leaves a half-resolved tree that
  can still validate green, because `validate_examples.py` reads whatever `resolvedSchema.json` is
  on disk. `resolve_schema.py --all` takes repeatable `--only <substring>` to resume.

  Partly mitigated since this was written: `regenerate.py` now STREAMS the resolve stage rather
  than capturing it (gBB `d299a3101`). `run()` printed a stage's output only on failure, so both
  runs that died at the cap had printed nothing at all from resolve and a run in progress could not
  be told from a stalled one. Streaming does not make it faster — splitting the pipeline (stages up
  to `profile-1`, then `resolve_schema.py` directly, then `--from profile-2`) is still what fits it
  into the window.

## Also in scope: the publication example codes (`short_code`)

Fold this in, because fixing it renames 14 of EPMA's 16 `tapp/` example files and there is no sense
renaming them twice.

`tools/build_tapp_examples.py` names each publication example from its workbook column header:

```python
def short_code(header, idx):
    m = re.search(r"([A-Z][A-Za-z]+)\s*(?:et al\.?)?\s*\(?(\d{4})", header)
    return (m.group(1) + m.group(2)) if m else f"P{idx}"
```

**EPMA is the only one of the sixteen that writes `Author+Year`.** SEM v84 writes
`Garvie et al. 2008`, which matches, giving `Garvie2008`. EPMA v87 writes `Ma+2015`, where the `+`
is not covered by `\s*(?:et al\.?)?\s*\(?`, so the author never matches — and `re.search` then
continues along the header and matches an **instrument model** instead. Three columns carry a bare
`JEOL <4 digits>`; the other twelve carry `JXA-8100`, `SX-100` or `SX100`, where the hyphen or the
missing space blocks it, so they fall through to the positional `P{idx}`.

That is the whole explanation for EPMA's "missing" P4, P7 and P9. All 15 publication columns do
produce an example; three are just named after a microprobe:

| expected | actual file | source column |
|---|---|---|
| `P4` | `exampleempaTAPP-JEOL8200-2.json` | `Ma+2017 \| JEOL 8200 \| WDS Point Analysis` |
| `P7` | `exampleempaTAPP-JEOL8530.json` | `Seifert+2026 \| JEOL 8530 \| WDS Point Analysis` |
| `P9` | `exampleempaTAPP-JEOL8530-2.json` | `McCoy+2025_SI \| JEOL 8530F+ \| WDS Point Analysis` |

Two faults, not one cosmetic issue:

- **`P0` collision.** Column `idx=0` (`Ma+2015 | Caltech GPS | … (JEOL 8200)`) would fall back to
  `P0`, which is the reserved code for the **synthetic** example every block carries and which is
  not a publication at all. It escapes today only because `JEOL 8200` matches first. Remove that
  model from the first column's header and column 0 collides with the synthetic example; the de-dup
  loop renames whichever it reaches second, so which file wins depends on write order.
- **Positional instability.** `P{idx}` is the column position, so inserting or deleting a
  publication column silently renumbers every `P` code after it and repoints those filenames at
  different papers. The three instrument-named files are immune, which makes the instability
  inconsistent within one workbook.

Suggested fix: widen the separator to `[\s+,]*` so `Ma+2015` matches the author, and anchor the
search to the **first pipe-delimited segment** of the header so an instrument model can never win.
Consider also making the fallback something that cannot collide with the reserved synthetic code —
`Pcol{idx}`, or the column letter — and deriving it from the header rather than the position.

Expect this to show up in CI's **Regenerate and diff** as 14 EPMA renames. The example *count*
stays 628: these are renames, not additions.

## Suggested shape

A fresh branch off `main`, with sources in one commit and regenerated output in a second, so the
reviewable diff is separable from the 100k-line regeneration.

## Verification

```
python tools/validate_examples.py          # expect 628 of 628
python tools/audit_building_blocks.py      # expect 237 of 242, same 5 profile-ada holds
python tools/intake_delivery.py --checks-only
python tools/check_componentType.py
```

```
git ls-files build/ | grep EMPA     # expect nothing once the postprocess has run
```

Plus CI's **Validate and annotate** (the only thing that catches dangling-`$ref` breakage — local
validation structurally cannot) and **Regenerate and diff** (proves the committed artifacts are
reproducible, which is what a directory rename most risks).

---

## Follow-up in `metadata`, after gBB republishes

1. **`core/services/schema_registry.py` — `_TECHNIQUE_ALIASES` must invert.** It currently reads
   `{"EPMA": "EMPA", "EMP": "EMPA"}`, normalising the *standard* spelling to the legacy one. It
   becomes `{"EMPA": "EPMA", "EMP": "EPMA"}`. Its comment, which cites the EPMA-workbook /
   EMPA-directory split as the reason, stops being true once the directory is renamed.
2. **`adaEMPA` → `adaEPMA`** in `core/management/commands/load_json_table.py`,
   `validate_json_table.py`, `bundle_ingestion/services/yaml_to_jsonld.py`,
   `adaMetadataViews/viewapp/views.py`, and the docs.
3. **Re-run `sync_registries`** from the new commit. The `epmaTAPP` rows are created and the **145**
   `empaTAPP` rows (46 analyte + 10 monitored-property + 1 target-material + 13 parameter-template +
   44 parameter-value + 31 vocabulary) are unpublished automatically by `--retire-absent`.
4. **The ADA database needs no change.** `records.specific_type` holds
   `"Electron microprobe analysis"` for **436** records, and **no** row contains the string `EMPA`
   or `EPMA` — the acronym lives only in the derived label. What changes is the mapping in
   `core/services/record_items.py` and `schema_registry.py`. (Note: those files' comments say "346
   EMPA records"; the current count on `specific_type` is 436. The discrepancy is unexplained and
   worth resolving rather than propagating.)
5. **Do not edit migrations `0006`, `0016`, `0017`.** They mention `empaTAPP` only in `help_text`
   examples. Cosmetic, and if changed at all it is through a new migration.

## Bonus: this closes the OneGeochemistry vocabulary gap

The mismatch that prompted this — 89 method definitions referencing
`https://vocab.onegeochemistry.org/epma/...` against a registry keyed `ada:vocab/empaTAPP/...` —
largely dissolves. The external path segment `/epma/` is the technique scope, so after the rename it
maps directly onto `ada:vocab/epmaTAPP/...` with no alias at all.

Four resolve by a kebab→camel, plural→singular transform once the spelling agrees:

| external | local |
|---|---|
| `epma/diffracting-crystals` | `epmaTAPP/diffractingCrystal` |
| `epma/xray-lines` | `epmaTAPP/xRayLine` |
| `epma/beam-modes` | `epmaTAPP/beamMode` |
| `epma/matrix-correction` | `epmaTAPP/matrixCorrectionMethod` |

Four still need decisions, independent of this rename:

- `epma/background-methods` — ambiguous between `backgroundCorrectionMethod` and
  `xRayBackgroundCorrectionMethod`
- `epma/matrix-correction-models` — no `models` vocabulary; may collapse onto `matrix-correction`
- `epma/beam-damage-methods` — **no counterpart exists**; terms would need authoring
- `laicpms/spot-geometries` — `/laicpms/` is ambiguous across `laMcicpms`, `laQicpms`, `laSficpms`
  and their UPb twins, and no spot-geometry vocabulary exists under any of them

`/techniques` (all 89 definitions) and `/materials` (5) have no technique segment and are global
community lists; the local `epmaTechnique` and per-TAPP material vocabularies are not equivalents.
