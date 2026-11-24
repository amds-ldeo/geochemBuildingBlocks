# Validation gates: the audit baseline, vendored remotes, the census and the counterexamples

Moved out of `CLAUDE.md` on 2026-10-25, text unchanged except where noted; `CLAUDE.md` keeps a short summary and a pointer here. Dates and counts below are as of when each passage was written; re-measure before quoting one.

**The audit is baselined, and it gates.** Until 2026-10-16 it printed
`Summary: 246 passed, 5 failed` and exited **0**, and no workflow ran it — a failure report nothing
could act on (`docs/SILENT_SUCCESS.md` #9). It now exits 1 on any issue not recorded in
`docs/audit_baseline.json`, and runs as a step of `check-schema-drift.yml`.

The baseline is EMPTY as of 2026-10-26. It held 5 accepted failures — the legacy
`geochemProfile/<TECH>/profile-ada` blocks for QRIS, RAMAN, VNMIR, XANES and XRD, each on
`No example files found` — and those blocks were retired rather than given examples: no record
derived to their `ada<TECH>Full` cids (measured over all 7,447) and each lost every detection
contest to its TAPP twin. Accepting them while they existed is what let the audit gate at all;
making it fatal outright would have built a check that can never pass.

Three things to know before touching it:

- **A deliberate change is two steps, as with the census**: fix or accept, then `--write` and commit
  `docs/audit_baseline.json` in the same PR, where the diff shows which block moved. Clearing debt
  is also a baseline change — a resolved issue left in the manifest keeps absorbing the next
  regression at that block, so a full run fails until it is removed.
- **The baseline records which `--checks` wrote it.** CI runs
  `--checks files,schema-json,shacl,coverage`: measured on `a1cb6fbdb8`, that subset and the full
  six-check audit report the SAME five failures and both exit 0 against the baseline, the subset
  takes 13.6s against the full audit's 11m25s, and the two omitted checks each duplicate a
  stricter check that already runs
  (`resolved` compares only top-level property keys, where `Regenerate and diff` byte-diffs a full
  nine-stage regeneration; `examples` is `validate_examples.py`, run by `check-examples.yml`). A run
  narrower than its manifest says so and declines to call anything resolved.
- **A vocabulary `@id` collision is fatal and NOT baselineable**; `--write` refuses it.

**Two ways a vendored upstream schema stays stale through a `--refresh-remote`.** `vendor/remote/`
plus `vendor/remote-lock.json` pin every remote `$ref` so a build cannot absorb an upstream change
unannounced, and `--refresh-remote` is the deliberate act of taking one. Neither link below is a
defect in that design; both are consequences of it that present as "the refresh did not work", and
both cost a wrong conclusion on 2026-10-22.

- **The flag re-fetches what is reached by a URL, and a relative `$ref` inside the vendored tree is
  not.** `_fetch_relative_in_cache` converts a cache path back to a URL **only when the file is
  absent**; an existing one is read off disk, so the URL is never visited and the pinned copy is
  served however many times the flag is passed. `provProperties/generatedBy` is reached exactly
  that way — `../../provProperties/generatedBy/schema.yaml` from each `cdifProfile` file — so it
  had a lock entry, a correct digest, and stale content. Force the miss: delete the vendored file,
  then re-run with `--refresh-remote`.
- **Refreshing and resolving are two jobs even in one command.** `--all` re-resolves every block and
  compares bytes, so `already current` is truthful — but it is a statement about the inputs that run
  actually had. A run that resolved while the vendored copy was still stale reports every dependent
  block current, correctly, and 24 of them did. Once the vendored file really changes, run
  `resolve_schema.py --all` AGAIN before believing any count: the second pass is what carried the
  new base into all 34 profile blocks and took `validate_examples` to 657/657.

**`constraint_census.py` answers the question `validate_examples` structurally cannot.** A
schema is a set of restrictions, so deleting one makes it more PERMISSIVE and every instance that
validated still validates — no corpus of positive examples can detect a loss, however large. The
census counts the constraints themselves (`required` names, `enum` members, `const`, `$ref`
targets, closed objects, branch counts — 1,467,862 of them across 257 blocks in the committed manifest on 2026-10-25) and compares the
counts to `docs/constraint_census.json`. Counts give magnitude and direction; a per-block digest
catches a SWAP that leaves counts equal, which a count alone cannot see.

It is NOT a stage of `regenerate.py`, deliberately — a baseline rewritten on every run agrees with
whatever just happened and records nothing, the same reasoning as `docs/modules/emitted.json`. A
deliberate constraint change is therefore two steps: regenerate, then `--write` and commit the
manifest in the same PR, where the diff shows which constraints moved. Array indices are elided
from its pointers, so `allOf`/`anyOf` reordering does not register (branch order carries no
meaning, and the upstream postprocess is known to reorder lists —
opengeospatial/bblocks-postprocess#91). It runs as a step of `check-schema-drift.yml`, after
regeneration, rather than as its own required check. `validate_counterexamples.py` and
`audit_building_blocks.py` are steps of the same job, for the same reason: a new required context is
the thing that sits pending forever, and none of the three needs a separate signal. That job is
required; `Check examples validate` is not, and a red non-required check does not delay auto-merge
at all.

**`validate_counterexamples.py` is the other half, and the two catch different bugs.** The census
sees a constraint disappear from the SCHEMA. This sees a constraint that is still there but no
longer BITES — a conditional whose `if` stopped matching, a branch moved into an `anyOf` where it
constrains nothing, a `$ref` that now resolves somewhere more permissive. 27 cases (2026-10-25) in
`docs/counterexamples.json`, each a single MUTATION of a real example (`remove`/`set`/`add` at a
JSON pointer) which must be REJECTED.

Three properties are deliberate. The mutation is applied to the LIVE example rather than stored as
an invalid document, because examples are regenerated and a stored counterexample drifts out of
shape and starts failing for an unrelated reason — which still looks like a pass. `expect` is
mandatory: the rejection must mention the named thing, or the case is reported as
failing-for-the-wrong-reason, since a case that fails for the wrong reason tells you nothing about
the constraint it was written for. And a pointer that no longer resolves is a HARD FAILURE, never
a skip — a silently skipped case is lost coverage, which is the exact failure mode the file
exists to prevent. All three are verified: dropping `schema:name` from 48 `required` lists turns
`tappdef-requires-name` red.
## A required constraint that no example and no counterexample exercises

The keyed-table families are declared far more widely than they are populated, and the gap is
invisible to every gate here. Measured 2026-10-27 over the 41 EPMA and LA-\* `tapp` examples:

| keyed family | EPMA examples | LA-\* examples |
|---|---|---|
| `ada:targetSpeciesTemplate` | 13 | 28 |
| `ada:targetMaterialTemplate` | 15 | 28 |
| `ada:monitoredPropertyTemplate` | 0 | 1 |
| `ada:reportedPropertyTemplate` | **0** | **0** |

All seven of those techniques DECLARE all four families, and each family's COLUMN array is
`required` **inside** its template object while the default-ROW array is optional. The template
itself is optional at the procedure root, which is what makes the gap possible: omitting
`ada:reportedPropertyTemplate` entirely is legal, so the `required` on
`ada:reportedPropertyColumns` never has to hold.

Repo-wide, `ada:reportedPropertyColumns` is populated by **exactly one** example —
`_sources/BaseSchema/tappDefinition/exampletappDefinition-all-properties.json` — and by **zero**
counterexamples, while **59** sidecars reference the family. No technique example exercises it at
all. So if that constraint were dropped or stopped biting, nothing in this repository would say
so: `validate_examples` cannot see a constraint that no instance reaches, and
`constraint_census.py` would record the DECREASE only if the declaration itself went, not if the
declaration survived with nothing to apply to.

No example anywhere populates all four families; the maximum is three. The richest are the
Solution-MC-ICPMS and Solution-Q-ICPMS sets (`examplesolutionQicpmsTAPP-Gao2008.json` reaches
targetSpecies 7 cols/48 rows, targetMaterial 2/14, monitoredProperty 5/3), and they are the ones
to read when the keyed shape matters.

This is the shape #232 proposes a floor for: a declared-but-unexercised constraint is not a weak
test, it is an absent one, and a pass count has no denominator in it.

## The SHACL baseline, and the one upstream rule it is holding

`docs/shacl_baseline.json` accepts SHACL violations the way `docs/audit_baseline.json` accepts
audit failures, under the same two-step rule: **fix or accept, then
`validate_examples.py --write-shacl-baseline` and commit the manifest in the SAME change.**
Accepted findings are printed and then set aside, never hidden.

Keyed by `(example, message, count)` and NOT by focus node, because a focus node is usually a
blank node whose identifier is assigned at parse time — a key containing one would match nothing
on the next run and every accepted finding would come back as new. The count is part of the key
so accepting one occurrence cannot silently cover five.

**A stale entry is fatal.** An entry the run did not encounter is reported on its own line, with
its own non-zero exit, separately from an unaccepted violation — the two call for opposite
responses: unaccepted means FIX something, stale means DELETE something. The check is scoped to
the examples a run actually visited, because `--filter` validates a subset and an unscoped check
makes a one-example run fail on every entry it never examined. It exists because 74 of this
manifest's original 77 entries went dead in a single change (#313) with nothing to say so, which
is the rot Rule B of `check_additionaltype_policy.py` already guards against for its own manifest.

### The term label floor that held 2 findings, and why it was an upstream fix

The baseline is EMPTY, and the last two entries are worth recording because the diagnosis took
two wrong measurements to get right.

Both were `A Term must have a name (label) or an identifier` on
`tappDefinition/exampletappDefinition-nmnh-spinel-oxybar-v1.json`, and the message was
misleading — **the terms DID have names.** They were the `No` member of two inline Yes/No term
sets under `ada:methodParameters[].schema:inDefinedTermSet.schema:hasDefinedTerm[]`, carrying
`schema:name` and `schema:termCode` both set to `"No"`.

What actually bit was `cdifd:termLabelProperty`, a branch of a node-level `sh:or`:

    sh:path schema:name ; sh:minCount 1 ; sh:datatype xsd:string ; sh:minLength 3 ;

`"Yes"` is three characters and passed. `"No"` is two and failed, so the name branch failed; the
terms carry no `schema:identifier`, so the other branch failed too, and the `sh:or` reported its
own generic message instead of the length one. That is why scanning the example for an unnamed
`schema:DefinedTerm` found nothing, and why `resultPath` was empty with `sh:value` equal to the
focus node itself.

**A 3-character floor on a controlled-vocabulary label is wrong in this domain**, which is what
made this an upstream repair rather than a data fix. Measured over `_sources/registry/vocab/`:
**18 labels are shorter than three characters, and every one is the canonical form** — `H2`,
`He`, `O2` (collision and reaction gases), `Ka`, `Kb`, `La`, `Lb` (Siegbahn notation for X-ray
emission lines), `On`, and `No` in six boolean-ish pick lists. `Ka` IS the name of the K-alpha
line; renaming it to clear a length check would falsify the vocabulary. **And the margin before
the floor bit again was ONE CHARACTER**: the generated technique examples emit 539
`schema:DefinedTerm` nodes across 140 distinct labels, and the shortest is exactly 3 — `SEM`,
`TEM`, `sem`, `tem`. Element symbols (`Fe`, `Mg`, `Si`) would have hit it the moment a target
species was emitted as a DefinedTerm.

That measurement is what moved the fix upstream. `sh:minLength` is now `1` in all three files —
lowered rather than dropped, matching how `cdif:physicalDataType`'s `minLength 5` was settled;
`1` still rejects `""`, and `sh:minCount 1` stays — and the message no longer recites a number.
It reached this repository as the `snapshot-2026-11-16b` pin.

**Do not "fix" a finding of this shape by lengthening labels or inventing identifiers.**
`label_defined_terms` sets a term's name from its own `schema:termCode` precisely so nothing is
asserted which the data did not carry, and a padded label would break that for the sake of a
constraint that is itself wrong.

**The misleading message is NOT fixed, and cannot be split.** Because the floor sits inside a
node-level `sh:or`, any future failure of that shape still reports "A Term must have a name
(label) or an identifier" with an empty `sh:resultPath` and `sh:value` equal to the focus node.
It cannot be separated the way `physicalDataType` was, since the `sh:or` is what makes "name OR
identifier" work at all. Read the focus node, not the message.

**A release SHACL bundle may still carry the old floor.** The fix is in the mBB source files and
in this pin; the `*Rules.shacl` bundles emitted from them by
`validation/ShaclValidation/generate_shacl_shapes.py` are published separately, and eight still
carried `minLength 3` when this landed. A consumer reading a bundle rather than pinning the
sources gets the wrong answer.

### Three shapes shared one URI, which made the constraint stricter than any of them intended

Until `snapshot-2026-11-16b`, `cdifd:CDIFDefinedTermShape` was declared in
`schemaorgProperties/{agentInRole,definedTerm,spatialExtent}/rules.shacl` as **three different
shapes under one identifier**. An earlier version of this section called them "duplicated
verbatim" and "substantively identical". That was wrong, and how it went wrong is the part worth
keeping: I compared `cdifd:termLabelProperty` — which genuinely IS byte-identical in all three —
and generalised that to the shape CONTAINING it. I verified the wrong subject. Parsed with
rdflib rather than read as text:

    agentInRole     sh:targetClass schema:DefinedTerm    2 sh:or branches   no termCode
    definedTerm     sh:target <blank node>               3 sh:or branches   termCode present
                    (a scoped SPARQLTarget)
    spatialExtent   sh:targetClass schema:DefinedTerm    2 sh:or branches   no termCode

A bundle pulling in two of those files merged both targets AND both or-lists onto the one URI and
enforced the conjunction — **stricter than any of the three authors wrote**, which is the same
class as the vocabulary `@id` collision recorded in CLAUDE.md: two files, one identifier, and
which one wins decided by what the consumer happens to load.

Upstream de-collided them in the same pin: `definedTerm` keeps the canonical name, and the other
two became `cdifd:agentInRoleDefinedTermShape` and `cdifd:spatialExtentDefinedTermShape`. For
this repository that RELAXES — we had been inheriting a constraint stricter than any single file
intended.

One finding of that episode is still untested and should not be assumed away: `definedTerm`'s
copy reported zero on these nodes because its SPARQLTarget selects only DefinedTerms in named
predicate positions and **never selected a standalone node at all**. Zero meant "not checked",
not "the termCode branch rescued it". Whether a `schema:termCode` branch satisfies such terms
remains unverified.

`validate_examples.load_shapes()` parses each file into its OWN graph, which is why a shared-URI
collision could never silently merge here — and also why a shape defined in several files reports
the same finding once per file, which is what the dedupe in #310 exists to collapse.
