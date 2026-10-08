# Provenance: `exampledetail-P0.json`

**Source-derived.** Assembled from primary sources, not rendered from a TAPP workbook column, and
kept because a generator cannot invent its content.

## Where the content came from

**14 distinct method-description documents, behind 4,305 references in ADA.** All are from
**Curtin University**, on a Tescan MIRA3 with an Oxford Instruments AZtec v5.1 Symmetry EBSD-EDS
system -- one laboratory instance, because the sources do not vary. Seeded from those documents
rather than from ADA subject fields, which carry no EBSD-specific property at all: the 1,354
records hold only `channel1`-`channel3` and `imageType`.

Constant across all 14 documents and therefore recorded at protocol level:

| value | |
|---|---|
| stage tilt | 70 degrees |
| camera gain | 2 |
| maximum mean angular deviation | 1.2 degrees |
| detector | XMax 150 mm SDD |

**Analyst:** Timms, who authored the method descriptions. First use 2023-11-16.

## Do NOT fix this block by regenerating it

This block is **not reproducible from its sidecar**. Measured 2026-10-08, running the sanctioned
`python tools/regenerate.py --tapp ebsdTAPP` against a clean tree:

```
exampleebsdTAPP-P0.json      15 JSON paths LOST, including ada:ebsdCameraGain,
                             ada:beamCurrentDefault, ada:crystalStructureFileSourcesDefault
                             and ada:dataProcessingSoftwareDefault
EBSD/tapp/schema.yaml        81 paths LOST (119 generic paths gained)
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
