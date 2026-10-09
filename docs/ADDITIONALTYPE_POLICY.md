# Serialization policy for `schema:additionalType` and `schema:propertyID`

**Status: DRAFT.** Clause 1 needs a decision in `metadataBuildingBlocks`, because it makes gBB
`$ref` a CDIF-owned `$def`. Clause 2 is enforced in this repo today by
`tools/check_additionaltype_policy.py`.

## The problem this closes

CDIF's `schemaorgProperties/additionalProperty/rules.shacl` reports, at **`sh:Violation`**
severity, a value on either property that looks like a URI or CURIE but is serialized as a string
literal — because `"ada:DataDeliveryPackage"` as a string is a literal that merely *looks* like a
URI and resolves to nothing, so it does not participate in RDF entailment as a resource reference.
It was the largest single class in the build, **740 of ~2,499 violations**, and #77 cleared it:
1,542 values across 345 example files.

The same shape is equally explicit that a **free label stays a string** — it names
`'MaterialSample'` as the canonical example, twice. So the policy cannot be "always use an IRI
reference"; it has to distinguish an identifier from a label, and it does so with the shape's own
regex:

```
^[A-Za-z][A-Za-z0-9+.\-]*:[^\s"]+$
```

Anchored at both ends, with no whitespace in the local part. That is why `MaterialSample`,
`award number`, `Electron Source` and `Smithsonian catalog` are labels, and
`bios:LabProcess`, `ada:DataDeliveryPackage` and `https://registry.identifiers.org/registry/doi`
are identifiers.

## Clause 1 — a value-TYPE declaration routes through `cdifConceptOrTermOrString`

Where a schema declares what *form* a value of these properties may take, it does so by
referencing CDIF's shared shape rather than by restating one locally:

```yaml
'schema:additionalType':
  type: array
  items:
    $ref: '.../cdifDataType/cdifConceptOrTermOrString/schema.yaml'
```

That `$def` is `anyOf[string, cdifConceptOrTerm]`, and `cdifConceptOrTerm` admits `{"@id": …}`,
`schema:DefinedTerm`, or an inline `cdif:Concept`. It is strictly more permissive than the
`anyOf[string, {@id}]` this repo currently hand-writes at three sites, and it matches what the
SHACL accepts — so converging on it is adopting mBB's existing majority convention, not inventing
one.

**Where mBB and gBB stand** (parsed, counting every declaration under `_sources`; gBB at
`211afba19`):

| | mBB (20) | gBB (348 `additionalType`) |
|---|---|---|
| `$ref cdifConceptOrTermOrString` | **14** | 0 |
| local `anyOf[…{@id}]` | 5 (all `xasProperties`) | 2 |
| `type: string` only | **0** | 3 |
| `contains` pinning a bare string | 0 | **338** |

So mBB effectively has the policy already and gBB has none of it.

**The `xasProperties` entry above is not a second spelling**, and reading it as one was a
mistake worth recording. Each of those blocks carries a one-line alias:

```yaml
$defs:
  cdifConceptOrTermOrString:
    $ref: ../../cdifDataType/cdifConceptOrTermOrString/schema.yaml
```

so `items` already routes through the canonical definition; the outer `anyOf[{@id}, array]` is
a *cardinality* choice, not a restatement of the concept shape. What those sites do carry is
the hazard of gBB PR #69 — a document-local `#/$defs/…` pointer whose target is a remote `$ref`
does not survive inlining into a consumer. Latent, not currently broken.

**The `objectReference` duplication that would have undercut this policy is now fixed.** mBB
published an `objectReference` `$def` while 116 places wrote its shape out in full, so a policy
referencing a shared shape would have been enshrining one idea in two spellings. CDIF PR #51
replaced all 115 remaining copies, leaving exactly one: the definition. 63 of 63 resolved
schemas were verified to have identical constraints, so clause 1 now references a shape with a
single spelling beneath it.

**Cost to weigh:** this adds a cross-repo `$ref` from gBB into CDIF for a shared `$def`, which
makes gBB regeneration depend on CDIF publishing it. That dependency has repeatedly bitten this
ecosystem through stale `gh-pages`. It is currently clear, and `targeted_resolve_acceleration`
records how to resolve against a local unpublished mBB block if it is not.

## Clause 2 — a pinned identifier must be expressed as an IRI reference

This is the half that actually broke, and it is **not** the same as clause 1.

338 of gBB's 348 `additionalType` declarations are not type declarations at all. They are
discriminators that pin a required member, with `items` left unconstrained:

```yaml
'schema:additionalType':
  contains: {const: 'Collision Reaction Cell'}
  schema:inDefinedTermSet: ada:vocab/instrumentType
```

Because `items` is unconstrained, `{"@id": X}` is admitted as a *value*. But `contains` demands a
member equal to the literal string `X`, so the array **stops satisfying `contains`** the moment
that value is converted. The constraint is still present and still bites — it just stops matching
what it was written for, which is the failure mode `CLAUDE.md` describes as a conditional that is
too narrow: its constraints are silently absent and the record validates clean.

> **A pin may name a free label as a bare string. A pin that names a CURIE or URI must also admit
> the IRI-reference form.**

```yaml
contains:
  anyOf:
  - const: bios:LabProcess
  - type: object
    required: ['@id']
    properties:
      '@id': {const: bios:LabProcess}
```

Each branch pins the const, so the discriminator still discriminates — widening it to
`{type: object}` would match *any* step and silently satisfy the requirement, which is worse than
the narrow form because it fails nothing.

`bios:LabProcess` was the **one** pin of the 339 keying on a CURIE, which is why it was the one
that needed #79. The other 338 pin free labels — `ICPMS`, `Electron Source`, `Torch`, and
adaProduct's 114 product names — and are correct exactly as they are. **The rule keys on the
value, not on the presence of a pin.**

The clause covers `const` and `enum` as well as `contains`, because all three freeze a literal the
same way. The parameter `$defs` already satisfy it: they pin
`schema:propertyID: {const: [{"@id": "ada:parameter/…"}]}`.

## What is out of scope

- **Free labels.** They stay strings. Converting one would mint a bogus IRI.
- **Whether a given value *ought* to be an identifier.** `MaterialSample` and
  `Smithsonian catalog` are content questions for CDIF and ADA respectively, not serialization
  ones.
- **The example corpus.** It is generated. `build_tapp_examples.idify_uri_values()` serializes
  these values and is idempotent; fix a generator, never an example.

## Enforcement

```
python tools/check_additionaltype_policy.py          # both clauses; exits non-zero on failure
python tools/check_additionaltype_policy.py --list   # every declaration, by shape
```

Clause 2 carries **no allowlist** — it is green today, so any violation is a regression. Verified
to bite in both directions: collapsing #79's dual-form discriminator back to `const:
bios:LabProcess` turns it red, and restoring it turns it green. A check that has never been
observed failing is not known to work.

Clause 1 has known open debt, so it compares against `docs/additionaltype_policy_open.json`. A
violation **not** in that manifest fails, and a manifest entry that **no longer** violates also
fails — a manifest that may silently rot is the failure mode `docs/SILENT_SUCCESS.md` exists to
prevent. The five recorded entries are #77's unwidened sites.

## Why a check and not just a convention

A schema is a set of restrictions, so this class is invisible to the example corpus in both
directions. Dropping a constraint only makes a schema more permissive, so no number of passing
examples can detect it (`constraint_census.py` exists for that reason). And a pin that stops
matching makes instances *more* likely to validate, not less. The violation surfaced at all only
because #67 fixed five unparseable module `rules.shacl` files — until then no shape was evaluated.
Neither `validate_examples` nor `check-schema-drift` can see either half of this.
