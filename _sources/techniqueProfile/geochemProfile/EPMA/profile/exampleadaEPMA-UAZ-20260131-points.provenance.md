# Provenance of `exampleadaEPMA-UAZ-20260131-points.json`

ADA record `10.60707/an7h-fg87` -- the quantitative WDS point analyses of session `20260131_EMPA_UAZ_OREX-800150-13_1`. The sibling record `10.60707/3xec-yw98` holds the X-ray maps from the same session.

**ADA** the published record. **CAL** `..._calibrationFile_1.txt`. **INST** `..._instrumentMetadata_1.txt`, the session's own `.qtiDat` output. **SENT** no source reports it.

Skeleton `exampleadaEPMA.json` validates with 1 error(s); this instance with 0.

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
| `/schema:keywords` | ADA | from the record's sample, technique and description |
| `/schema:license` | SENT | the published ADA record carries the string 'missing' here |
| `/prov:wasGeneratedBy/0/schema:identifier` | ADA |  |
| `/prov:wasGeneratedBy/0/schema:startTime` | INST | first analysis point timestamp, Saturday January 31 2026 8:10:53 AM |
| `/prov:wasGeneratedBy/0/schema:endTime` | INST | the run's own analysis timestamps bound the session to that day; no explicit end is recorded |
| `/prov:wasGeneratedBy/0/schema:object` | ADA |  |
| `/prov:wasGeneratedBy/0/prov:used/0/schema:instrument/0` | ADA+INST | identity from the ADA record; 15 keV / 20 nA / 0 um from the instrument metadata 'Column Conditions : Cond 1 : 15 keV 20 nA' and 'Beam Size : 0 um' |
| `/prov:wasGeneratedBy/0/schema:actionProcess` | CAL+INST | calibration standards and the overlap correction from the calibration file; acquisition and reduction detail from the session's own instrument metadata |
| `/prov:wasGeneratedBy/0/ada:deadTime` | INST | ada:deadTime is EDS dead time per the TAPP; the PHA table's Dtime=3 is the WDS proportional-counter constant, which the TAPP treats as a separate field |
| `/prov:wasGeneratedBy/0/ada:proceduralBlankLevel` | SENT |  |
| `/schema:variableMeasured` | CAL+INST | one entry per monitored element, each carrying its spectrometer, crystal, X-ray line, peak and background positions, PHA settings, calibration standard and assay, peak counting time, detection limit and 1-sigma precision |
| `/prov:wasGeneratedBy/0/schema:additionalProperty` | INST | procedure parameter Beam Damage Minimization |
| `/prov:wasGeneratedBy/0/schema:additionalProperty` | SENT | procedure parameter Drift Correction |
| `/prov:wasGeneratedBy/0/schema:additionalProperty` | SENT | procedure parameter Halogen Correction on Oxygen |
| `/schema:distribution/0/schema:hasPart/0/schema:additionalProperty` | INST | analysis-level parameter EDS Spectral Processing Type |
| `/schema:distribution/0/schema:hasPart/0/schema:additionalProperty` | INST | analysis-level parameter EDS Live Time per Point or Pixel |
| `/schema:distribution/0/schema:hasPart/0/schema:additionalProperty` | INST | analysis-level parameter Stage Scan vs. Beam Scan |
| `/schema:distribution/0/schema:hasPart/0/schema:additionalProperty` | INST | analysis-level parameter Step Size / Pixel Size |
| `/schema:distribution/0/schema:hasPart/0/schema:additionalProperty` | INST | analysis-level parameter Beam Raster Dimensions |
| `/schema:distribution/0/schema:hasPart/0/schema:additionalProperty` | INST | analysis-level parameter Map Dimensions |
| `/schema:distribution/0/schema:hasPart/0/schema:additionalProperty` | INST | analysis-level parameter Map Area |
| `/dqv:hasQualityMeasurement` | INST | the profile pins the measurement label, so the label is kept and the value says what this procedure reports instead |
| `/schema:variableMeasured` | ADA+SENT | the sampling-unit identifier. ADA: the record reports one row per WDS analysis point, so the column is structurally present. SENT: no source available here gives the column's own label, so `schema:name` carries the TAPP item label, as Detection Limit and the other TAPP-labelled variables in this file do. Required by the profile from 2026-10-02, when `defines: sample > sampling unit` was routed to a data column. |

## Rejected -- kept out because they would have broken validation

Places where the published ADA record's own shape disagrees with the adaEPMA profile it declares conformance to.

| JSON pointer | source | errors before | errors after |
|---|---|---|---|
| `/schema:additionalType` | ADA | 1 | 2 |
| `/schema:measurementTechnique` | ADA | 1 | 3 |
| `/schema:distribution` | ADA | 1 | 3 |
| `/schema:subjectOf` | ADA | 1 | 2 |
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
| (UAZ)Cameca SX100 | `ex:an7h-fg87/instrument/EPMA` |

This file is SOURCE-DERIVED, so no generator rewrites it and the generator fix could not reach it;
the values were re-minted in place with the generators' own scheme
(`schema_path_example_emitter.assign_instrument_ids`), so a rebuild from scratch would produce the
same strings.

The document scope is `an7h-fg87`, this record's own `@id`.
