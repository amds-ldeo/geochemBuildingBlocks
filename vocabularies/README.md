# Geochemistry vocabularies

SKOS vocabularies published under `https://w3id.org/geochem/vocabulary/` (redirect rules in
w3id.org `ids/geochem/vocabulary/.htaccess`, served from this folder on GitHub Pages).

## activityTypes

`activityTypes.jsonld`: laboratory activity types used in ADA / geochemistry analytical procedures
(TAPP workflow steps). Scheme `https://w3id.org/geochem/vocabulary/activityTypes`; concepts
`https://w3id.org/geochem/vocabulary/<localName>`:

| concept | broader | `skos:broadMatch` (CDIF provenance activity) |
|---|---|---|
| samplePreparation | | |
| sampleDigestion | samplePreparation | |
| ionMilling | samplePreparation | |
| instrumentTuning | | Configuration |
| instrumentCalibration | | Calibration |
| dataAcquisition | | Measurement |
| dataProcessing | | DataTransformation |
| qualityControl | | QualityControl |

These moved here from the deprecated CDIF activity-type vocabulary
(`https://w3id.org/cdif/provenance/activityType/`), whose concepts now carry `dcterms:isReplacedBy`
pointing here; each concept here records the old IRI with `dcterms:replaces`.

`activityTypes.jsonld` is the only file to edit. `activityTypes.ttl` and the per-concept files in
`activityType/` are generated from it with profile-provenance's build script:

```bash
python <profile-provenance>/tools/buildVocabularyFiles.py vocabularies/activityTypes.jsonld --concept-dir vocabularies/activityType
```

Each concept's `skos:notation` must equal its IRI's last segment. Validate against the CDIF
concept-scheme profile (`profile-conceptscheme`'s `FrameAndValidate.py -v` and pyshacl with
`conceptSchemeRules.shacl`).
