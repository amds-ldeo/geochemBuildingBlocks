# Provenance of `exampleadaEPMA-UAZ-20260131.json`

Session `20260131_EMPA_UAZ_OREX-800150-13_1`, DOI `10.60707/3xec-yw98`.

**ADA** the published ADA record. **MD** that session's own method description. **LIT:<column>** a literature column of `EPMA_TAPP_v68.csv`; `Zega+2025_UA` and `McCoy+2025_UA` are the same laboratory (K-ALFAA, U. Arizona) on the same instrument (Cameca SX-100). **SENTINEL** no source reports it.

Skeleton `exampleadaEPMA.json` validates with 1 error(s); this instance validates with 0.

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
| `/schema:keywords` | ADA | from the record's sample and technique |
| `/schema:license` | SENTINEL | the published ADA record carries the string 'missing' in this field |
| `/prov:wasGeneratedBy/0/schema:identifier` | ADA |  |
| `/prov:wasGeneratedBy/0/schema:startTime` | ADA |  |
| `/prov:wasGeneratedBy/0/schema:endTime` | SENTINEL | ADA records a start but no end |
| `/prov:wasGeneratedBy/0/schema:object` | ADA |  |
| `/prov:wasGeneratedBy/0/prov:used/0/schema:instrument/0` | ADA+MD | identity from the ADA record; voltage, current and beam size from the method description |
| `/prov:wasGeneratedBy/0/schema:actionProcess` | MD | the two passes become the ordered HowTo steps; this also repairs the stub that makes both shipped profile examples fail |
| `/prov:wasGeneratedBy/0/ada:deadTime` | SENTINEL | numeric sentinel |
| `/prov:wasGeneratedBy/0/ada:proceduralBlankLevel` | SENTINEL |  |
| `/schema:variableMeasured` | MD | one entry per spectrometer channel per pass, plus BSE Z; the skeleton's remaining variables are retained because the profile pins them with `contains` |
| `/prov:wasGeneratedBy/0/schema:additionalProperty` | LIT:Zega+2025_UA | procedure-level parameter Beam Damage Minimization |
| `/prov:wasGeneratedBy/0/schema:additionalProperty` | SENTINEL | procedure-level parameter Drift Correction |
| `/prov:wasGeneratedBy/0/schema:additionalProperty` | SENTINEL | procedure-level parameter Halogen Correction on Oxygen |
| `/schema:distribution/0/schema:hasPart/0/schema:additionalProperty` | MD | analysis-level parameter Map Dimensions |
| `/schema:distribution/0/schema:hasPart/0/schema:additionalProperty` | SENTINEL | analysis-level parameter Map Area |
| `/schema:distribution/0/schema:hasPart/0/schema:additionalProperty` | SENTINEL | analysis-level parameter Stage Scan vs. Beam Scan |
| `/schema:distribution/0/schema:hasPart/0/schema:additionalProperty` | SENTINEL | analysis-level parameter Step Size / Pixel Size |
| `/schema:distribution/0/schema:hasPart/0/schema:additionalProperty` | SENTINEL | analysis-level parameter Beam Raster Dimensions |
| `/schema:distribution/0/schema:hasPart/0/schema:additionalProperty` | MD | analysis-level parameter EDS Spectral Processing Type |
| `/schema:distribution/0/schema:hasPart/0/schema:additionalProperty` | MD | analysis-level parameter EDS Live Time per Point or Pixel |
| `/dqv:hasQualityMeasurement` | SENTINEL | Goodness-of-Fit is empty in all 15 literature columns |
| `/schema:variableMeasured` | ADA+SENTINEL | the sampling-unit identifier. ADA: the session reports per analysis point across two spectrometer passes, so the column is structurally present. SENTINEL: no source gives the column's own label, so `schema:name` carries the TAPP item label, as Detection Limit and the other TAPP-labelled variables in this file do. Required by the profile from 2026-10-02, when `defines: sample > sampling unit` was routed to a data column. |

## Rejected — kept out because they would have broken validation

These are places where the published ADA record's own shape disagrees with the adaEPMA profile it declares conformance to.

| JSON pointer | source | errors before | errors after |
|---|---|---|---|
| `/schema:additionalType` | ADA | 1 | 2 |
| `/schema:measurementTechnique` | ADA | 1 | 3 |
| `/schema:distribution` | ADA | 1 | 3 |
| `/schema:subjectOf` | ADA | 1 | 3 |
| `/prov:wasGeneratedBy/0/schema:location` | ADA | 1 | 2 |
| `/prov:wasGeneratedBy/0/schema:additionalProperty` | MD | 0 | 1 |
| `/prov:wasGeneratedBy/0/schema:additionalProperty` | MD | 0 | 1 |

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
| (UAZ)Cameca SX100 | `ex:3xec-yw98/instrument/EPMA` |

This file is SOURCE-DERIVED, so no generator rewrites it and the generator fix could not reach it;
the values were re-minted in place with the generators' own scheme
(`schema_path_example_emitter.assign_instrument_ids`), so a rebuild from scratch would produce the
same strings.

The document scope is `3xec-yw98`, this record's own `@id`.
