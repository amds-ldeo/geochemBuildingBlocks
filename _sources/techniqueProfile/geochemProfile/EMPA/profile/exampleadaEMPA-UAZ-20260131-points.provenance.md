# Provenance of `exampleadaEMPA-UAZ-20260131-points.json`

ADA record `10.60707/an7h-fg87` -- the quantitative WDS point analyses of session `20260131_EMPA_UAZ_OREX-800150-13_1`. The sibling record `10.60707/3xec-yw98` holds the X-ray maps from the same session.

**ADA** the published record. **CAL** `..._calibrationFile_1.txt`. **INST** `..._instrumentMetadata_1.txt`, the session's own `.qtiDat` output. **SENT** no source reports it.

Skeleton `exampleadaEMPA.json` validates with 1 error(s); this instance with 0.

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
| `/prov:wasGeneratedBy/0/schema:startDate` | INST | first analysis point timestamp, Saturday January 31 2026 8:10:53 AM |
| `/prov:wasGeneratedBy/0/schema:endDate` | INST | the run's own analysis timestamps bound the session to that day; no explicit end is recorded |
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

## Rejected -- kept out because they would have broken validation

Places where the published ADA record's own shape disagrees with the adaEMPA profile it declares conformance to.

| JSON pointer | source | errors before | errors after |
|---|---|---|---|
| `/schema:additionalType` | ADA | 1 | 2 |
| `/schema:measurementTechnique` | ADA | 1 | 3 |
| `/schema:distribution` | ADA | 1 | 3 |
| `/schema:subjectOf` | ADA | 1 | 2 |
| `/prov:wasGeneratedBy/0/schema:location` | ADA | 1 | 2 |
