# The collector: a string, a table, and the N=1 fallback (E1)

Moved out of `CLAUDE.md` on 2026-10-25, text unchanged except where noted; `CLAUDE.md` keeps a short summary and a pointer here. Dates and counts below are as of when each passage was written; re-measure before quoting one.

### The collector: a string, a table, and the N=1 fallback (E1)

`schema:instrument.schema:hasPart[additionalType 'Collector']` carries two properties, defined on
the **instrument** building block so every technique with a Collector part inherits them. They come
from our instrument representation, not from a delivered TAPP table — Ruolin's E1 answer says so
explicitly — which is why they are not generated from a sidecar row.

  `ada:collectorConfiguration`  the assignment as the SOURCE states it, free text
  `ada:collectors`              the collector table, `schema:name` the referenceable label

They are not the same information twice: the string is the claim, the table is the reading of it.

**The table follows Decision 6 (`TAPP-keyed-values-design.md` §1.1), not a second fallback shape.**
"Rather than admit two shapes, always emit the table: a declaration that does not parse into members
yields a one-row table whose row key is the text as written. The fallback is then not a separate
branch but N=1." So: one member per position when the string parses; ONE member carrying the text
when it does not, with the source fields riding in `schema:additionalProperty` as name/value pairs.
A consumer reads one shape either way. Parsing these strings to individual collectors is not
tractable in general — they are written for a person — so **N=1 is the expected case**.

**An N=1 member names no cup, so it makes no per-cup claim.** That is deliberate and load-bearing:
the resistor values are attested per MASS (`Proposal_Monitored_Property_2026-09-10` §10), and a
fallback that quietly moved them onto the collector axis would undo the withdrawal §10 argued for.

**`ada:collectorConfiguration` is NOT a keyed table, and was until 2026-09-27.** It was registered in
`KEYED_TABLES` as the monitored-property column array itself, which made one property the container
for eight unrelated items — each emitted as a `PropertyValueSpecification` column with a pinned
`schema:valueName` — while its own sidecar row declared it `Text (free)`. Declared type and emitted
shape contradicted each other from the start. The seven other items are now ordinary
`schema:additionalProperty` entries on the Collector, `@type` `schema:PropertyValue`: a column
DEFINITION specifies, a property on a part RECORDS.
