# `docs/` — the schema-path sidecars and the guides around them

Two kinds of thing live here: the **`*.schemapaths.csv` sidecars**, which are hand-authored source
that the generators read, and the **`*.md` guides** that document the conventions those sidecars
follow.

Nothing here is a build output. Everything generated lands in `_sources/` (schemas, examples) or
`build/` (resolved schemas, OAS3 downcompiles, register).

## The sidecars

One `<TableName>.schemapaths.csv` per wired technique — 16 of them, named after the TAPP table they
describe — plus `modules/Module_<Name>.schemapaths.csv` for each composition module.

A TAPP table says **what** metadata a technique records. It does not say **where** that metadata
lives in a JSON-LD document. The sidecar is the missing half: one row per Metadata Item, mapping it
to a canonical **schema path**.

```
Metadata Item,Protocol Tier,Analysis Tier,Data Type,Schema Path,Source,Scope,Notes,Key by
Beam Current,Basic,Editable,Numeric (nA),$MethodDefinition.ada:beamCurrentDefault,authored,,,
```

| column | |
|---|---|
| `Metadata Item` | the table's row name — the join key back to the TAPP table |
| `Protocol Tier` / `Analysis Tier` | copied from the table; they decide requiredness and whether a leaf is `schema:value` or `schema:defaultValue` |
| `Data Type` | copied from the table; drives JSON type, unit extraction and controlled-list detection |
| `Schema Path` | **the authored decision** — where this item lands. Grammar in [SCHEMA_PATH_GRAMMAR.md](SCHEMA_PATH_GRAMMAR.md) |
| `Source` | how the path got there: `authored` (a human decided), `inferred` (the tool guessed), `keyed` (routed from `Keyed By`), `module` (a composition module owns it, so the path is blank), `flagged` (unplaced, needs a human) |
| `Scope` | `shared` / `divergent` / `module` — used when reconciling a path against the module that also places it |
| `Key by` | mirrors the table's `Keyed By`; see [KEYED_BY_GRAMMAR.md](KEYED_BY_GRAMMAR.md) |
| `Notes` | free text — provenance, open questions, why a divergence stands |

An item may have **more than one row**. A field that both the procedure defaults and the analysis
supplies is dual-homed, one row per root. A field keyed to a domain carries the keyed placement *and*
an unkeyed fallback, because which applies is a runtime condition on the instance, not a design-time
choice.

A row whose `Source` is `module` has **no** `Schema Path`: the module owns the placement, and
defining it twice would let the technique's copy silently win wherever the two differ. The row itself
stays, because migration diffs Metadata Items against the table and a deleted row returns as
"new (flagged)" at the next delivery.

## How a sidecar is created and maintained

```bash
python tools/bootstrap_schemapaths.py <table.csv>          # seed or refresh from the table
python tools/migrate_sidecar.py <tapp> --source <table>    # carry it onto a new table revision
python tools/fill_flagged.py --write                       # place what bootstrap could not
python tools/refresh_keyby.py --all --write                # re-sync Key by from the table
python tools/simplify_sidecars.py --write                  # blank rows a module already places
```

`bootstrap_schemapaths` seeds rows and infers what it can; anything it cannot place is marked
`flagged` with an empty path, and a human decides. Once a path is `authored`, later runs preserve it —
the tools fill gaps, they do not overwrite decisions.

When Ruolin issues a new table revision, **`migrate_sidecar` carries the authored paths across** and
reports what it could not match. The line to read closely is `DROPPED`: an item that looks deleted is
usually renamed beyond the mechanical rules, and its authored paths go with it. Test each drop against
the table it migrated **from** as well as the one it migrated **to** — absent from both means a stale
row, absent from only the old one means a rename that needs a `migrate_sidecar.ALIASES` entry.

Run [`intake_delivery.py`](../tools/intake_delivery.py) first: it previews all of that, plus module
conflicts and paths that no longer resolve to a grammar family, and writes nothing.

## What reads them

The sidecar is the input to the path-driven pipeline. `build_pathdriven.py` turns each path into
nested JSON Schema; `build_tapp.py` derives the registry catalogs and vocabularies;
`schema_path_example_emitter.py` uses the same paths to place values in generated examples, so schema
and example cannot disagree about where a field belongs.

```
TAPP table (tapp/ submodule)  ──┐
                                ├─→ build_tapp / build_pathdriven / build_profile ─→ _sources/…
docs/<table>.schemapaths.csv  ──┘         build_tapp_examples
```

Full walkthrough in [TAPP-schema-generation-workflow.md](TAPP-schema-generation-workflow.md); the
regeneration command sequence is in `CLAUDE.md`.

**A sidecar edit does not rebuild anything by itself.** The schema moves when you regenerate, and the
publication examples move only when `build_tapp_examples` runs — skipping it leaves them on their
previous placement, and the resulting validation failure reads as a schema bug rather than a stale
artifact.

## The guides

| file | |
|---|---|
| [SCHEMA_PATH_GRAMMAR.md](SCHEMA_PATH_GRAMMAR.md) | **the canonical grammar** — roots, productions, and the distinctions it enforces. Start here |
| [KEYED_BY_GRAMMAR.md](KEYED_BY_GRAMMAR.md) | what each `Keyed By` value means and the paths it routes to |
| [TAPP-schema-generation-workflow.md](TAPP-schema-generation-workflow.md) | end-to-end: workbook → validated schema |
| [TAPP_TEMPLATE_GUIDE.md](TAPP_TEMPLATE_GUIDE.md) | authoring guide for a new TAPP table |
| [README_TAPP_for_Schema_Generation_v2.md](README_TAPP_for_Schema_Generation_v2.md) | the table conventions the generators rely on |
| [REPORTINGCORE_BLOCKS.md](REPORTINGCORE_BLOCKS.md) | how the conditional `reportingCore` module splits into per-block `$defs` |
| [PROPOSAL-monitoredSpecies.md](PROPOSAL-monitoredSpecies.md) | **draft, not implemented** — a proposed shape for monitored species / channels |
| [upstream-requests.md](upstream-requests.md) | table problems that belong to `amds-ldeo/tapp`, not here |
| `TierImplementationPatterns.xlsx` | the canonical Protocol × Analysis tier matrix |

## Subdirectories

- **`modules/`** — sidecars for the composition modules. Same format; see
  [`_sources/BaseSchema/modules/README.md`](../_sources/BaseSchema/modules/README.md).
- **`tappDefinition-per-analyte-values/`** — worked per-analyte value sets used as reference
  material; has its own README.
- **`archive/`** — superseded sidecars and the workbooks they described. **Gitignored**: bulky and
  settled, and git history still has every version. Tools glob `docs/*.schemapaths.csv`
  non-recursively, so archived revisions are never swept in alongside live ones.
- **`experiments/`** — scratch work, untracked.

## Conventions worth knowing before editing

**An `ada:` segment must be lowerCamel.** UpperCamel is the grammar's `@type`-assertion syntax, so
`ada:IonBeamSource` sets a node's `@type` instead of navigating to a property and contributes no
schema at all — a row that passes every check while placing nothing. The parser rejects these now.

**Exactly one live sidecar per technique.** When a table is version-bumped, the old sidecar moves to
`archive/`. Two sidecars for one technique means the tools pick by filename and the loser is invisible.

**Superseded revisions are not reference material.** Deriving anything from every file in `docs/`
rather than from the *wired* sidecars picks up retired terms and double-counts techniques.
