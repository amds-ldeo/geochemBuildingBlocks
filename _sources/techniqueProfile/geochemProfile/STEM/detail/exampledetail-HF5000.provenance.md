# Provenance: `exampledetail-HF5000.json`

**Source-derived.** Assembled from primary sources, not rendered from a TAPP workbook column, and
kept because a generator cannot invent its content.

## Where the content came from

**HyperSpy metadata exported from a Hitachi HF5000 at the University of Arizona.** All 25 exports
carry a full `Acquisition_instrument` block, which is what makes a native layer possible for this
laboratory at all.

This is one of **two** STEM laboratory instances, and the split is on the laboratory boundary rather
than at random -- the metadata available differs by lab, not by record. The LBNL instance
(`*-P1`) is deliberately left empty of these values: declaring 200 kV technique-wide would assert
Arizona's instrument for Berkeley's records.

First use 2024-05-16.

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
this example carries. See `CLAUDE.md` and #65.

## Commits

- `28020f247` seeded `stemTAPP` and `ebsdTAPP` from ADA's own supplementary documents
- `bd17888f5` recorded the analysts and first-use dates on all three instances
- `f1cab9f27` added the creator attribution and pathed the identity rows
- `f9e5b6fbf` recorded the constraint census for the four new blocks
