# Detail-block placement: measurements

Moved out of `CLAUDE.md` on 2026-10-25, text unchanged except where noted; `CLAUDE.md` keeps a short summary and a pointer here. Dates and counts below are as of when each passage was written; re-measure before quoting one.

Measure before relocating one of these `$ref`s. Moving the twelve `adaProfile` hasPart-item blocks
to the top level was tried on a copy on 2026-09-05 and failed **all 218** records of the affected
profiles on a missing `ada:componentType` — the reasoning that motivated it (EPMA's description
says "Dataset-level analysis-instance detail ... on the schema:Dataset root") generalised from the
wrong family.

This mismatch is the NORM, not four exceptions. Measured 2026-10-06, after this paragraph claimed
TEM, XCT, SEM-FIBSEM and SEM-Imaging were the only inconsistent ones:

  34 of 34  `profile/` schemas compose `../detail/schema.yaml` as a top-level `allOf` entry,
            i.e. on the `schema:Dataset` root
  49 of 61  detail blocks describe themselves as "Detail block for <TECH> hasPart items"
   0 of 61  GEOCHEMPROFILE detail blocks CONSTRAIN `ada:componentType` anywhere — in XCT's it
            appears only in its own description, and EPMA's does not mention it at all
  13 of 14  adaProfile detail blocks DO constrain it, almost all as a bare `const` — the
            asymmetry is real and load-bearing, see below
  34 of 34  `profile/` descriptions say they constrain "valid component types on
            schema:distribution.hasPart", and NONE of them constrains `schema:hasPart` at all —
            in XCT's profile the word appears once, in that sentence
   0 of 61  geochemProfile detail blocks constrain anything at the hasPart level either, so
            nothing in a technique profile reaches a component. The sealed componentType enums
            live in the base file-type BBs (image, imageMap, tabularData, …), layer 1 of the componentType architecture in `CLAUDE.md`

**Counts measured 2026-10-18**, over 61 techniques and 34 TAPP profiles.

**The `0 of 61` applies to `geochemProfile` ONLY, and the adaProfile row is why that matters.**
`build_conformance_sidecars` reads a profile's componentTypes from three unioned sources, and for
the legacy `adaProfile` blocks the DETAIL block is the authoritative one — its `profile-ada`
reaches components through `$ref: ../detail/schema.yaml` rather than an inline enum. Those detail
blocks pin `ada:componentType` as a bare `const`, a shape the sidecar generator did not read
until 2026-10-18, which made ICPOES, LAF, PSFD and L2MS look like profiles with nothing to
distinguish them. Reading this section as "no detail block anywhere constrains componentType" is
what hid that for weeks.

Reproduce
with: parse each `profile/schema.yaml`, check whether any `allOf` entry `$ref`s `../detail/schema.yaml`;
then dump each `detail/schema.yaml` with its `description` and `title` removed and grep for
`componentType`. Do NOT grep the file whole — the description says the word, which is exactly how
this went unnoticed.

The consequence is scope, not failure: a `$Dataset.schema:distribution…` path in a detail block
constrains EVERY distribution item of a conforming dataset rather than only the components whose
`ada:componentType` the block names. Nothing is invalid today, because no record exercises the
narrowing that was never built.

Measure before relocating any of it. The twelve `adaProfile` hasPart-item blocks were moved to the
top level on a copy on 2026-09-05 and failed all 218 records of the affected profiles; the reverse
move is equally capable of surprising, and it would now touch 49 blocks rather than four. *(Was "47"; corrected 2026-10-25 to the 49 of 61 measured above.)*
