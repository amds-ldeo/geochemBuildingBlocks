# exampledetailXRD-identifierOnlySample.json

**This example is NOT generated, and it must never gain `schema:name` on its sample.** It is the
positive half of the `schema:name` -> `schema:identifier` substitute line; the negative half is
`docs/counterexamples.json`'s `sample-needs-name-or-identifier`, which points at
`exampledetailXRD-P0.json` in this same directory.

## What it is for

`tools/schema_path_emitter.py`'s `SUBSTITUTES` / `_require()` let an analysed sample satisfy
`schema:name` with `schema:identifier`, scoped to `schema:object`, because ADA records identify the
sample by `schema:identifier` ("OREX-803031-101") and carry no separate laboratory name -- for
XANES, XRD, QRIS and RAMAN (322 records) it was the only thing they failed on. The relaxation
reaches every `detail/` and `profile/` block through `BaseSchema/modules/core`'s
`AnalysisIdentification` `$def`.

The scoping is carried by a `scope` argument threaded through `to_schema`'s recursive call sites.
Lose that threading -- a plausible merge resolution, and what nearly happened resolving PR #123 --
and `_require` gets `scope=None`, `SUBSTITUTES.get(None)` misses, and the relaxation silently
disappears. **Nothing caught that before this file existed**, because the loss makes the schema
STRICTER:

- every positive example still validated, so `validate_examples` stayed green;
- `sample-needs-name-or-identifier` sets the sample to a bare typed object carrying NEITHER name
  nor identifier, so it is rejected whether or not the substitute is honoured;
- `constraint_census.py` saw counts RISE (a removed `anyOf` becomes a firm `required`), which is
  not a decrease and so read as benign.

Only real ADA records would have failed, and nothing in gBB reads ADA records. See
`docs/SILENT_SUCCESS.md` #8.

## The measurement

**Measured 2026-10-16 on `143824ace1`** (main, after PR #123, which modified this same emitter but
touches neither `to_schema`'s signature, the `scope` argument, `SUBSTITUTES` nor `_require`). Cited
with its commit because the reverted lines shift whenever the emitter is edited, and a reader
reproducing it needs to know which generator was measured.

Revert the `scope` threading on `to_schema`'s three recursive call sites, rebuild the modules stage
(`build_module_bb.py --write`), re-resolve this block:

```
core AnalysisIdentification `then`      required: [schema:name]      <- anyOf gone
exampledetailXRD-identifierOnlySample   FAIL  'schema:name' is a required property
exampledetailXRD-P0                     PASS  <- the control
```

Restoring the threading returns both to PASS.

**The control is the point, not a footnote.** That `exampledetailXRD-P0` is green in BOTH states is
what establishes the gap: the pre-existing corpus cannot distinguish the two generators, so the
relaxation could be lost without any check going red. A counterexample alone shows the floor still
holds; a positive example alone shows the relaxation works; only the pair *plus* a green control
shows the pair is load-bearing. If a future reader re-runs this, keep `-P0` in the comparison.

A full nine-stage `python tools/regenerate.py` was also run against a populated `tapp/` submodule:
`git status --porcelain -- _sources` afterwards listed these two files and nothing else, so the
pipeline leaves this example untouched rather than merely being expected to.

## Neither half of the line catches the other's regression -- keep both

This file and `sample-needs-name-or-identifier` are not redundant, and deleting either leaves a
blind spot:

- a tightening that re-required `schema:name` outright fails THIS file and leaves the
  counterexample green;
- a relaxation that let an anonymous sample through fails the COUNTEREXAMPLE and leaves this file
  green.

**The scoping is the load-bearing part.** `schema:name` is still required outright at ~48 other
nodes -- a TAPP definition, a person, an instrument, a step parameter -- where an identifier is
NOT an acceptable substitute, and `tappdef-requires-name` and `step-parameter-requires-name` hold
that line. Do not let this example drift toward demonstrating the relaxation at one of those
nodes: it would then be asserting something false.

## Why it is static, and how to rebuild it

Every other example in this directory is generated -- `exampledetailXRD-P0.json` by
`build_pathdriven`, `exampledetail-<Pub>.json` by `build_tapp_examples`. Neither generator emits an
identifier-only sample, and the `-P0` emitter fills both `schema:name` and `schema:identifier` from
their sidecar rows, so the case cannot be had from a generated file.

Its filename is deliberately outside both generators' namespaces: `build_tapp_examples._prune()`
globs `exampledetail-*.json` in this directory and `build_pathdriven` writes exactly
`exampledetailXRD-P0.json`.

It is a byte-faithful derivative of `exampledetailXRD-P0.json` apart from its identity and the
sample, so when the XRD detail schema moves and this file goes stale, rebuild it rather than
repairing it by hand:

```
python - <<'PY'
import collections, json
src = '_sources/techniqueProfile/geochemProfile/XRD/detail/exampledetailXRD-P0.json'
out = '_sources/techniqueProfile/geochemProfile/XRD/detail/exampledetailXRD-identifierOnlySample.json'
ex = json.load(open(src, encoding='utf-8'), object_pairs_hook=collections.OrderedDict)
smp = ex['prov:wasGeneratedBy'][0]['schema:object'][0]
del smp['schema:name']
smp['schema:identifier'] = 'OREX-803031-101'
ex['@id'] = 'ex:detailXRD-identifierOnlySample'
with open(out, 'w', encoding='utf-8', newline='\n') as f:
    json.dump(ex, f, indent=2, ensure_ascii=False)
    f.write('\n')
PY
```

Rebuilding is the only sanctioned repair. Adding `schema:name` back would make the file validate
again while removing the coverage it exists for, which is the same silent success the file guards
against.
