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
| `/prov:wasGeneratedBy/0/schema:startDate` | EXP | earliest Analysis date across the 117 runs (03/09/2024) |
| `/prov:wasGeneratedBy/0/schema:endDate` | EXP | latest Analysis date across the 117 runs (04/09/2024); the session spans two days |
| `/prov:wasGeneratedBy/0/ada:proceduralBlankLevel` | SENT |  |
| `/prov:wasGeneratedBy/0/ada:deadTime` | SENT |  |
| `/prov:wasGeneratedBy/0/prov:used/0/schema:instrument/0` | ADA+LOG | identity from the ADA record; the collector array and which collectors carried signal from the instrument logs |
| `/prov:wasGeneratedBy/0/schema:actionProcess` | MD+EXP+LOG | prose from the method description; run counts, method files and configuration contents from the raw exports |
| `/schema:variableMeasured` | EXP | one entry per measurand column, parsed from the .exp header where each column is '<cup configuration>:<mass><element>'; the published record carried none at all |
| `/prov:wasGeneratedBy/0/schema:additionalProperty` | LOG | baseline integration time, 30 cycles per baseline |
| `/dqv:hasQualityMeasurement` | MD | the profile pins all three labels; each value says what this session actually reports |

## Rejected — would have broken validation

| JSON pointer | source | before | after |
|---|---|---|---|
| `/schema:measurementTechnique` | ADA | 1 | 3 |
| `/schema:distribution` | ADA | 1 | 3 |
| `/schema:subjectOf` | ADA | 1 | 4 |
| `/prov:wasGeneratedBy/0/schema:location` | ADA | 1 | 2 |
