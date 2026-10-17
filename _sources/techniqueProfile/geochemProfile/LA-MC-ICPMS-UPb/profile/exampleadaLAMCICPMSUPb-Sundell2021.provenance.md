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
| `/prov:wasGeneratedBy/0/schema:startDate` | SENT | no session dates are reported |
| `/prov:wasGeneratedBy/0/schema:endDate` | SENT |  |
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
