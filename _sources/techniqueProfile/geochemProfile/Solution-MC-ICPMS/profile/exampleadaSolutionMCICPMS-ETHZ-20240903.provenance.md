# Provenance of `exampleadaSolutionMCICPMS-ETHZ-20240903.json`

ADA record `10.60707/9q7s-5533` — ETHZ mass-independent Ti isotope session, 3–4 September 2024, Thermo Neptune Plus.

**ADA** the published record. **EXP** the 117 Neptune `.exp` Analysis Data Reports. **LOG** the 117 instrument `.log` files. **MD** the session's methodDescription. **SENT** no source reports it.

The published record carries `schema:variableMeasured: []`. Everything below identity is recovered from the raw-data collection ADA already holds.

**Not asserted:** which collector carries which mass. That join lives in `Titan_Miriam.ccf`, named by the logs and not deposited.

Skeleton validates with 1 error(s); this instance with 0.

## Accepted

| JSON pointer | source | note |
|---|---|---|
| `/@id` | ADA |  |
| `/schema:name` | ADA |  |
| `/schema:description` | ADA |  |
| `/schema:identifier` | ADA |  |
| `/schema:url` | ADA |  |
| `/schema:creator` | ADA |  |
| `/schema:funding` | ADA |  |
| `/schema:dateModified` | ADA |  |
| `/schema:datePublished` | ADA |  |
| `/schema:additionalType` | ADA |  |
| `/schema:keywords` | ADA | from the record's own title and description |
| `/schema:license` | SENT |  |
| `/prov:wasGeneratedBy/0/schema:identifier` | ADA |  |
| `/prov:wasGeneratedBy/0/schema:startTime` | EXP | earliest Analysis date across the 117 runs (03/09/2024) |
| `/prov:wasGeneratedBy/0/schema:endTime` | EXP | latest Analysis date across the 117 runs (04/09/2024); the session spans two days |
| `/prov:wasGeneratedBy/0/ada:proceduralBlankLevel` | SENT |  |
| `/prov:wasGeneratedBy/0/ada:deadTime` | SENT |  |
| `/prov:wasGeneratedBy/0/prov:used/0/schema:instrument/0` | ADA+LOG | identity from the ADA record; the collector array and which collectors carried signal from the instrument logs |
| `/prov:wasGeneratedBy/0/schema:actionProcess` | MD+EXP+LOG | prose from the method description; run counts, method files and configuration contents from the raw exports |
| `/schema:variableMeasured` | EXP | one entry per measurand column, parsed from the .exp header where each column is '<cup configuration>:<mass><element>'; the published record carried none at all |
| `/prov:wasGeneratedBy/0/schema:additionalProperty` | LOG | baseline integration time, 30 cycles per baseline |
| `/dqv:hasQualityMeasurement` | MD | the profile pins all three labels; each value says what this session actually reports |
| `/schema:variableMeasured` | ADA+SENTINEL | the sampling-unit identifier. the deposited Neptune run reports one row per analysis, so the column is structurally present; no source available here gives its own label, so `schema:name` carries the TAPP item label as the other TAPP-labelled variables here do. Required by the profile from 2026-10-02, when `defines: sample > sampling unit` was routed to a data column. |

## Rejected — would have broken validation

| JSON pointer | source | before | after |
|---|---|---|---|
| `/schema:measurementTechnique` | ADA | 1 | 3 |
| `/schema:distribution` | ADA | 1 | 3 |
| `/schema:subjectOf` | ADA | 1 | 4 |
| `/prov:wasGeneratedBy/0/schema:location` | ADA | 1 | 2 |

## 2026-10-16 — `ada:submissionType` added

This example declares `adaProduct` in `dcterms:conformsTo` but carried no `ada:submissionType`,
which adaProduct has required since gBB #136. It was one of only four examples in the
`geochemProfile/*/profile` blocks missing it; the other 68 all carry it.

The field never reached this file because the example is SOURCE-DERIVED and therefore never
regenerated — the generator fills it for its generated siblings — and because
`tools/add_submission_type.py` targets blocks whose `resolvedSchema.json` mentions the property,
which these geochemProduct-based blocks do not.

`BundleDelivery` matches all 68 siblings and the corpus majority (7,071 of 7,447). It is a
DELIVERY fact about the submission, not a measurement fact, so it is not an invention of content
this example's sources do not support — the distinction the rest of this file turns on.

Found by stage-2 conformance detection, whose adaProduct presence test requires the ADA marker:
detection from CONTENT asked a question validation never asked of this file, because its block
composes geochemProduct and so never enforced adaProduct's requirements.

## 2026-10-30 — two co-authors were identified as the dataset itself

`/schema:creator/@list/1` and `/2` (Ruefenacht, Fehr) each carried `"@id": ""` and
`"schema:identifier": ""`, copied from the ADA record, which holds an empty string where an author
has no ORCID. An empty `@id` is not an absent one: in JSON-LD it resolves to the BASE IRI, so both
co-authors were asserted to be the dataset document — and, being equal, to be each other.

| JSON pointer | source | before | after |
|---|---|---|---|
| `/schema:creator/@list/1/@id` | ADA | `""` | *(removed)* |
| `/schema:creator/@list/1/schema:identifier` | ADA | `""` | *(removed)* |
| `/schema:creator/@list/2/@id` | ADA | `""` | *(removed)* |
| `/schema:creator/@list/2/schema:identifier` | ADA | `""` | *(removed)* |

Removed rather than filled. With no `@id` they are blank nodes: distinct, unnamed persons, which
is exactly what the sources support — `schema:name` and `schema:email` still carry the identity
that exists, and the first author keeps the ORCID they do have. A nil token is the resolution for
a property a schema PINS; nothing requires `@id` on a person here, so omission states the absence
and invents nothing.

The duplicate `ex:adaProduct-var-001` ids in this file's `schema:variableMeasured` were a separate
defect, fixed in `build_profile._add_required_variables`, which owns those appended members even
in a source-derived file.

## 2026-10-30 — instrument identifiers scoped to this document

`schema:instrument[].@id` was `ex:instrument/<type token>`, derived from the instrument's TYPE.
A type is not an identity: `ex:instrument/nxs-BaseClass-NXinstrument` -- the NeXus BASE CLASS, a
type URI standing in for an identifier -- was the `@id` of one JSON-LD node in 113 documents, and
`ex:instrument/SEM` in 85, each giving that one node a different manufacturer, model and name.

The identifiers below are now scoped by this document's own `@id`, so the instrument this record
describes is its own node. Nothing referenced the old values -- every occurrence of an instrument
identifier in the repository is the `@id` declaration itself, so no pointer moved.

| instrument | `@id` |
|---|---|
| NeptunePlus | `ex:9q7s-5533/instrument/ICPMS` |

This file is SOURCE-DERIVED, so no generator rewrites it and the generator fix could not reach it;
the values were re-minted in place with the generators' own scheme
(`schema_path_example_emitter.assign_instrument_ids`), so a rebuild from scratch would produce the
same strings.

The document scope is `9q7s-5533`, this record's own `@id`.
