# Provenance: `exampledetail-P1.json`

**Source-derived.** Assembled from primary sources, not rendered from a TAPP workbook column, and
kept because a generator cannot invent its content.

## Where the content came from

**`.ser` files from an FEI TitanX at Lawrence Berkeley.** All 78 carry image dimensions and nothing
else, so the native layer here is **deliberately empty** of acquisition parameters. That emptiness
is a decision, not a gap: the other STEM instance (`*-HF5000`, University of Arizona) has a full
`Acquisition_instrument` block, and carrying its 200 kV across to Berkeley would assert Arizona's
instrument for Berkeley's records.

Image pixel size and image dimensions are the only properties both laboratories record, and the
pixel size appears in m, nm and um, so it needs normalising before values are compared.

First use 2023-12-07.

## Do NOT fix this block by regenerating it

This block is **not reproducible from its sidecar**. Measured 2026-10-08, running the sanctioned
`python tools/regenerate.py --tapp stemTAPP` against a clean tree:

```
STEM/tapp/schema.yaml        41 paths LOST, including ada:acceleratingVoltage
                             and ada:analyticalMode (119 generic paths gained)
examplestemTAPP-HF5000.json  2 paths LOST: ada:acceleratingVoltage, ada:analyticalMode
```

The lost paths are the protocol-level constants seeded from the sources above. A generator cannot
invent them -- they were read out of method-description documents and instrument exports -- so
regeneration replaces real content with generic scaffolding and `validate_examples` stays green
through it, because losing content only makes an instance smaller and more permissively valid.

If this block needs changing, change it here and keep this record current. If it ever needs to
become generator-owned, the values above have to reach the generator first -- through the draft
table in `draftTAPPs/`, the sidecar, or a tool -- and the loss measurement above has to come back
clean before anyone trusts a regen.

## Attribution

`schema:creator` is `"Claude assisted"`, with a description recording that the parameter values and
tier assignments were derived by machine from ADA records and the attached documents, under human
review -- not authored by the laboratory. That attribution is load-bearing rather than a formality:
naming the analyst as creator would claim they wrote a TAPP they did not write. See `f1cab9f27`.

Note `ada:procedureAuthorDescription` is **deprecated** -- that statement lives at
`$MethodDefinition.schema:creator.schema:description`, which is what the sidecar paths and what
this example carries. See `CLAUDE.md` and #66.

## Commits

- `28020f247` seeded `stemTAPP` and `ebsdTAPP` from ADA's own supplementary documents
- `bd17888f5` recorded the analysts and first-use dates on all three instances
- `f1cab9f27` added the creator attribution and pathed the identity rows
- `f9e5b6fbf` recorded the constraint census for the four new blocks
