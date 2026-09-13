# Provenance of `exampleadaEMPA-UAZ-20260131.json`

Session `20260131_EMPA_UAZ_OREX-800150-13_1`, DOI `10.60707/3xec-yw98`.

**ADA** the published ADA record. **MD** that session's own method description. **LIT:<column>** a literature column of `EPMA_TAPP_v68.csv`; `Zega+2025_UA` and `McCoy+2025_UA` are the same laboratory (K-ALFAA, U. Arizona) on the same instrument (Cameca SX-100). **SENTINEL** no source reports it.

Skeleton `exampleadaEMPA.json` validates with 1 error(s); this instance validates with 0.

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
| `/prov:wasGeneratedBy/0/schema:startDate` | ADA |  |
| `/prov:wasGeneratedBy/0/schema:endDate` | SENTINEL | ADA records a start but no end |
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

## Rejected — kept out because they would have broken validation

These are places where the published ADA record's own shape disagrees with the adaEMPA profile it declares conformance to.

| JSON pointer | source | errors before | errors after |
|---|---|---|---|
| `/schema:additionalType` | ADA | 1 | 2 |
| `/schema:measurementTechnique` | ADA | 1 | 3 |
| `/schema:distribution` | ADA | 1 | 3 |
| `/schema:subjectOf` | ADA | 1 | 3 |
| `/prov:wasGeneratedBy/0/schema:location` | ADA | 1 | 2 |
| `/prov:wasGeneratedBy/0/schema:additionalProperty` | MD | 0 | 1 |
| `/prov:wasGeneratedBy/0/schema:additionalProperty` | MD | 0 | 1 |
