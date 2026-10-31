# Provenance of `exampleadaLAMCICPMSUPb-Sundell2021.json`

Sundell K.E., Gehrels G.E. and Pecha M.E. (2021) *Rapid U-Pb Geochronology by Laser Ablation Multi-Collector ICP-MS.* Geostandards and Geoanalytical Research **45**(1), 37-57. doi:10.1111/ggr.12355

**LIT** transcribed from the paper's Methods and Table 1. **SENT** the paper does not report it.

Skeleton validates with 1 error(s); this instance with 0.

## Accepted

| JSON pointer | source | note |
|---|---|---|
| `/@id` | LIT | the paper's own DOI |
| `/schema:name` | LIT |  |
| `/schema:description` | LIT |  |
| `/schema:identifier` | LIT |  |
| `/schema:url` | LIT |  |
| `/schema:datePublished` | LIT |  |
| `/schema:creator` | LIT |  |
| `/schema:keywords` | LIT |  |
| `/schema:license` | SENT |  |
| `/prov:wasGeneratedBy/0/schema:identifier` | LIT | eight measurement sessions, four acquisition rates, two sessions each |
| `/prov:wasGeneratedBy/0/schema:startTime` | SENT | no session dates are reported |
| `/prov:wasGeneratedBy/0/schema:endTime` | SENT |  |
| `/prov:wasGeneratedBy/0/schema:location` | LIT |  |
| `/prov:wasGeneratedBy/0/ada:proceduralBlankLevel` | SENT |  |
| `/prov:wasGeneratedBy/0/ada:deadTime` | SENT |  |
| `/prov:wasGeneratedBy/0/prov:used/0/schema:instrument` | LIT | laser and mass spectrometer from the Methods and Table 1 |
| `/prov:wasGeneratedBy/0/schema:actionProcess` | LIT |  |
| `/schema:variableMeasured` | LIT | Table 1, 'Collector configuration - mass': the paper states which mass is measured on which named cup, which is the join ADA's own MC-ICP-MS deposits do not carry |
| `/dqv:hasQualityMeasurement` | LIT | the profile pins all three labels; only Goodness-of-Fit is reported |
| `/schema:variableMeasured` | ADA+SENTINEL | the sampling-unit identifier. the session reports one row per ablation spot, so the column is structurally present; no source available here gives its own label, so `schema:name` carries the TAPP item label as the other TAPP-labelled variables here do. Required by the profile from 2026-10-02, when `defines: sample > sampling unit` was routed to a data column. |

## Rejected

| JSON pointer | source | before | after |
|---|---|---|---|

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

## 2026-10-30 — the laser and the mass spectrometer were ONE JSON-LD node

Both instruments under `/prov:wasGeneratedBy/0/prov:used/0/schema:instrument` carried
`"@id": "ex:instrument/nxs-BaseClass-NXinstrument"` and `schema:identifier`
`["ex:instrument-ada-001"]`. A repeated `@id` inside one array is not a cosmetic collision: in
JSON-LD those members are the SAME node, so this record asserted that one instrument is both a
Photon Machines Analyte G2 laser and a Nu Plasma HR multi-collector.

The shared id is the NeXus base class, which `build_tapp_examples.py:170` uses as its FALLBACK
token when a schema path carries no `[additionalType=...]` selector. It is universal, so it is not
an identity — all 68 instrument members across the generated `geochemProfile/*/profile` examples
carry it. Derived here from the model name instead, which is what distinguishes the two in the
paper's Table 1:

| JSON pointer | source | before | after |
|---|---|---|---|
| `/prov:wasGeneratedBy/0/prov:used/0/schema:instrument/0/@id` | LIT | `ex:instrument/nxs-BaseClass-NXinstrument` | `ex:instrument/Analyte-G2` |
| `/prov:wasGeneratedBy/0/prov:used/0/schema:instrument/1/@id` | LIT | `ex:instrument/nxs-BaseClass-NXinstrument` | `ex:instrument/Nu-Plasma-HR` |
| `/prov:wasGeneratedBy/0/prov:used/0/schema:instrument/1/schema:identifier/0` | LIT | `ex:instrument-ada-001` | `ex:instrument-ada-002` |

Edited in this file rather than fixed in a generator because the example is SOURCE-DERIVED, and
safe to edit here because `schema_path_example_emitter.normalize_instrument_tree` only supplies an
`@id` when the node does not already carry a string one — an authored id is preserved.

Not changed, and worth a look by someone with the paper: both instruments carry the SAME
`schema:additionalType`, `["ICPMS", "Laser Ablation System", ...]`, so each claims to be both
kinds of device. That is content this edit has no basis to decide.

The duplicate `ex:adaProduct-var-001` ids in this file's `schema:variableMeasured` were a
DIFFERENT defect with a different cause — `build_profile._add_required_variables` cloning
`vm[0]` without re-minting its id — and were fixed in that generator, which does own those
appended members even in a source-derived file.

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
| Photon Machines Analyte G2 | `ex:ggr-12355/instrument/Analyte-G2` |
| Nu Instruments HR Multi-collector | `ex:ggr-12355/instrument/Nu-Plasma-HR` |

This file is SOURCE-DERIVED, so no generator rewrites it and the generator fix could not reach it;
the values were re-minted in place with the generators' own scheme
(`schema_path_example_emitter.assign_instrument_ids`), so a rebuild from scratch would produce the
same strings.

The document scope is `ggr-12355`, this record's own `@id`.

`Analyte-G2` and `Nu-Plasma-HR` are kept as the local parts. Both instruments carry the same
`schema:additionalType` tokens, so deriving from the type would have replaced two names the paper
identifies (Table 1) with `ICPMS` and `ICPMS-2`; an authored local part names the actual device and
is preserved.
