
# Solution SF-ICP-MS Analysis Detail (Schema)

`ogch.techniqueProfile.geochemProfile.Solution-SF-ICPMS.detail` *v0.1*

Dataset-level analysis-instance detail for solution SF-ICP-MS, reusing CDIF/schema.org slots on the schema:Dataset root.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### detail example P0
detail instance derived from Desem+etal2022 | Nu Attom SC-SF-ICP-MS | Univ Melbourne.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-P0",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionSficpmsTAPP-P0",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "N -- \"A typical session comprised analyses of up to 50 unknowns and 15 standards\"; no session identifier stated",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Soil and rock samples from boreholes BH1, BH2 (Sunbury), BH3, BH4 (Kalkallo), BH5 (Greenvale), BH6, BH (Wallan), incl. BH3a; reference materials BCR-2, BR, AGV-2, JB-2, JB-3, NIST SRM981, and Broken Hill Main Lode galena",
  "ada:samplingUnitName": "Labelled by digestion: \"rock TD, soil TD, soil AR splits\" of each borehole sample (p.3), e.g. sample \"BH3a\" (p.2); splits are not numbered",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": 1,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "Pb: total procedural blank <100 pg — 'total procedural blanks (dissolution and/or leaching, including centrifuging) are estimated to be <100 pg'; sample/blank ratios ≥1500 (§2.3)",
  "ada:analysisInclusionAndRejectionCriteria": "Partially -- n stated per averaged result (BCR-2 n = 39, AGV-2 n = 13, BR n = 11, JB-2 n = 9, JB-3 n = 11, SRM981 n = 22 and n = 16). One documented exclusion, from the quality assessment rather than from a reported aggregate: \"Results for the pure Pb standard NIST SRM981, analysed many times with the soil samples, are not included here, because it contains no matrix and may thus not a be a good indicator of data quality for the soil samples analysed here\" [sec 3.1]. No acceptance or rejection rule, and no acquired-versus-included count, stated",
  "ada:combinedResults": "SRM981 (n = 22); SRM981 (n = 16); BCR-2 (n = 39); AGV-2 (n = 13); BR (n = 11); JB-2 (n = 9); JB-3 (n = 11)",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "206Pb/204Pb, 207Pb/204Pb: ±0.03–0.06 (±0.17–0.35%); 208Pb/204Pb: ±0.10–0.19 (±0.26–0.50%); 207Pb/206Pb: ±0.0006–0.0012 (±0.07–0.14%); 208Pb/206Pb: ±0.0020–0.0040 (0.09–0.18%) — 'Typical within-run precision (2 standards errors)' (§2.4); the ±0.001–0.002 in §2.3 is the MC-ICP-MS's",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "BCR-2, AGV-2, JB-2, BR, JB-3 [all: 2sd of repeat analyses] — Table 1; 'regular analyses of Tl-doped ~1 ppb solutions of several rock standards (unseparated)' (§2.4)",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "BCR-2, AGV-2, JB-2, BR, JB-3 [all: % deviation from published Pb isotope values] — Table 1 and §3",
  "ada:goodnessOfFitOrDispersionStatistic": "all: 2sd — '(2sd, n = 22)'; averages given with '±2sd%'"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-SF-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-P0",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionSficpmsTAPP-P0",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "N -- \"A typical session comprised analyses of up to 50 unknowns and 15 standards\"; no session identifier stated",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Soil and rock samples from boreholes BH1, BH2 (Sunbury), BH3, BH4 (Kalkallo), BH5 (Greenvale), BH6, BH (Wallan), incl. BH3a; reference materials BCR-2, BR, AGV-2, JB-2, JB-3, NIST SRM981, and Broken Hill Main Lode galena",
  "ada:samplingUnitName": "Labelled by digestion: \"rock TD, soil TD, soil AR splits\" of each borehole sample (p.3), e.g. sample \"BH3a\" (p.2); splits are not numbered",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": 1,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "Pb: total procedural blank <100 pg \u2014 'total procedural blanks (dissolution and/or leaching, including centrifuging) are estimated to be <100 pg'; sample/blank ratios \u22651500 (\u00a72.3)",
  "ada:analysisInclusionAndRejectionCriteria": "Partially -- n stated per averaged result (BCR-2 n = 39, AGV-2 n = 13, BR n = 11, JB-2 n = 9, JB-3 n = 11, SRM981 n = 22 and n = 16). One documented exclusion, from the quality assessment rather than from a reported aggregate: \"Results for the pure Pb standard NIST SRM981, analysed many times with the soil samples, are not included here, because it contains no matrix and may thus not a be a good indicator of data quality for the soil samples analysed here\" [sec 3.1]. No acceptance or rejection rule, and no acquired-versus-included count, stated",
  "ada:combinedResults": "SRM981 (n = 22); SRM981 (n = 16); BCR-2 (n = 39); AGV-2 (n = 13); BR (n = 11); JB-2 (n = 9); JB-3 (n = 11)",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "206Pb/204Pb, 207Pb/204Pb: \u00b10.03\u20130.06 (\u00b10.17\u20130.35%); 208Pb/204Pb: \u00b10.10\u20130.19 (\u00b10.26\u20130.50%); 207Pb/206Pb: \u00b10.0006\u20130.0012 (\u00b10.07\u20130.14%); 208Pb/206Pb: \u00b10.0020\u20130.0040 (0.09\u20130.18%) \u2014 'Typical within-run precision (2 standards errors)' (\u00a72.4); the \u00b10.001\u20130.002 in \u00a72.3 is the MC-ICP-MS's",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "BCR-2, AGV-2, JB-2, BR, JB-3 [all: 2sd of repeat analyses] \u2014 Table 1; 'regular analyses of Tl-doped ~1 ppb solutions of several rock standards (unseparated)' (\u00a72.4)",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "BCR-2, AGV-2, JB-2, BR, JB-3 [all: % deviation from published Pb isotope values] \u2014 Table 1 and \u00a73",
  "ada:goodnessOfFitOrDispersionStatistic": "all: 2sd \u2014 '(2sd, n = 22)'; averages given with '\u00b12sd%'"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-P0> a ada:SolutionICPMSTabular ;
    schema1:measurementTechnique <ex:solutionSficpmsTAPP-P0> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially -- n stated per averaged result (BCR-2 n = 39, AGV-2 n = 13, BR n = 11, JB-2 n = 9, JB-3 n = 11, SRM981 n = 22 and n = 16). One documented exclusion, from the quality assessment rather than from a reported aggregate: \"Results for the pure Pb standard NIST SRM981, analysed many times with the soil samples, are not included here, because it contains no matrix and may thus not a be a good indicator of data quality for the soil samples analysed here\" [sec 3.1]. No acceptance or rejection rule, and no acquired-versus-included count, stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "BCR-2, AGV-2, JB-2, BR, JB-3 [all: % deviation from published Pb isotope values] — Table 1 and §3" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:combinedResults "SRM981 (n = 22); SRM981 (n = 16); BCR-2 (n = 39); AGV-2 (n = 13); BR (n = 11); JB-2 (n = 9); JB-3 (n = 11)" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "all: 2sd — '(2sd, n = 22)'; averages given with '±2sd%'" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "206Pb/204Pb, 207Pb/204Pb: ±0.03–0.06 (±0.17–0.35%); 208Pb/204Pb: ±0.10–0.19 (±0.26–0.50%); 207Pb/206Pb: ±0.0006–0.0012 (±0.07–0.14%); 208Pb/206Pb: ±0.0020–0.0040 (0.09–0.18%) — 'Typical within-run precision (2 standards errors)' (§2.4); the ±0.001–0.002 in §2.3 is the MC-ICP-MS's" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:numberOfReplicates 1 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "Pb: total procedural blank <100 pg — 'total procedural blanks (dissolution and/or leaching, including centrifuging) are estimated to be <100 pg'; sample/blank ratios ≥1500 (§2.3)" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "Soil and rock samples from boreholes BH1, BH2 (Sunbury), BH3, BH4 (Kalkallo), BH5 (Greenvale), BH6, BH (Wallan), incl. BH3a; reference materials BCR-2, BR, AGV-2, JB-2, JB-3, NIST SRM981, and Broken Hill Main Lode galena" ;
    ada:samplingUnitName "Labelled by digestion: \"rock TD, soil TD, soil AR splits\" of each borehole sample (p.3), e.g. sample \"BH3a\" (p.2); splits are not numbered" ;
    ada:sessionIdentifier "N -- \"A typical session comprised analyses of up to 50 unknowns and 15 standards\"; no session identifier stated" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "BCR-2, AGV-2, JB-2, BR, JB-3 [all: 2sd of repeat analyses] — Table 1; 'regular analyses of Tl-doped ~1 ppb solutions of several rock standards (unseparated)' (§2.4)" .

<ex:solutionSficpmsTAPP-P0> schema1:identifier "missing" .


```


### detail example P1
detail instance derived from Li+etal2016 | Thermo Element I | IGGCAS Beijing.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-P1",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionSficpmsTAPP-P1",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "mag_1, mag_3, mag_5, py_2, py_4; iron-formation reference material FER-2 (CCRMP, CANMET MMSL, Canada)",
  "ada:samplingUnitName": "Sample name only — \"mag_1\", \"mag_3\", \"mag_5\", \"py_2\", \"py_4\", each reported as \"Mean ± s (n = 3)\" with the replicates unlabelled (table, p.8)",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "Li: 0.026; Be: 0.008; Sc: 0.020; Cr: 0.068; Co: 0.007; Ni: 0.035; Cu: 0.089; Zn: 0.216; Ge: 0.020; Rb: 0.012; Sr: 0.010; Cs: 0.004; Ba: 0.029; other: N — ng/mL (Table 2); 'the highest blank level in Zn would contribute less than 0.01% of the amount of analyte'",
  "ada:analysisInclusionAndRejectionCriteria": "Partially -- \"The mean values and respective standard deviations (s) for three analyses were listed in Table 3\"; n = 3 throughout. No acceptance or rejection rule stated",
  "ada:combinedResults": "each reference material in Table 3 (n = 3)",
  "ada:detectionLimit": "Li: 0.024; Be: 0.006; Sc: 0.028; Cr: 0.043; Co: 0.009; Ni: 0.014; Cu: 0.052; Zn: 0.176; Ge: 0.015; Rb: 0.009; Sr: 0.008; Cs: 0.006; Ba: 0.018; other: N — method detection limits (MDL, 3 s) in ng/g (Table 2); instrumental detection limits are also given, in ng/mL",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "FER-2 [all: RSD <5%] — three analyses, Table 3 (§3)",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "FER-2 [all: most ratios to literature values within 0.9–1.1] — Fig. 7 (§3)",
  "ada:goodnessOfFitOrDispersionStatistic": "all: s, one standard deviation, and RSD — 'Mean ± 1 s (n = 3)'; 'RSD = standard deviation/mean × 100%'"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-SF-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-P1",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionSficpmsTAPP-P1",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "mag_1, mag_3, mag_5, py_2, py_4; iron-formation reference material FER-2 (CCRMP, CANMET MMSL, Canada)",
  "ada:samplingUnitName": "Sample name only \u2014 \"mag_1\", \"mag_3\", \"mag_5\", \"py_2\", \"py_4\", each reported as \"Mean \u00b1 s (n = 3)\" with the replicates unlabelled (table, p.8)",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "Li: 0.026; Be: 0.008; Sc: 0.020; Cr: 0.068; Co: 0.007; Ni: 0.035; Cu: 0.089; Zn: 0.216; Ge: 0.020; Rb: 0.012; Sr: 0.010; Cs: 0.004; Ba: 0.029; other: N \u2014 ng/mL (Table 2); 'the highest blank level in Zn would contribute less than 0.01% of the amount of analyte'",
  "ada:analysisInclusionAndRejectionCriteria": "Partially -- \"The mean values and respective standard deviations (s) for three analyses were listed in Table 3\"; n = 3 throughout. No acceptance or rejection rule stated",
  "ada:combinedResults": "each reference material in Table 3 (n = 3)",
  "ada:detectionLimit": "Li: 0.024; Be: 0.006; Sc: 0.028; Cr: 0.043; Co: 0.009; Ni: 0.014; Cu: 0.052; Zn: 0.176; Ge: 0.015; Rb: 0.009; Sr: 0.008; Cs: 0.006; Ba: 0.018; other: N \u2014 method detection limits (MDL, 3 s) in ng/g (Table 2); instrumental detection limits are also given, in ng/mL",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "FER-2 [all: RSD <5%] \u2014 three analyses, Table 3 (\u00a73)",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "FER-2 [all: most ratios to literature values within 0.9\u20131.1] \u2014 Fig. 7 (\u00a73)",
  "ada:goodnessOfFitOrDispersionStatistic": "all: s, one standard deviation, and RSD \u2014 'Mean \u00b1 1 s (n = 3)'; 'RSD = standard deviation/mean \u00d7 100%'"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-P1> a ada:SolutionICPMSTabular ;
    schema1:measurementTechnique <ex:solutionSficpmsTAPP-P1> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially -- \"The mean values and respective standard deviations (s) for three analyses were listed in Table 3\"; n = 3 throughout. No acceptance or rejection rule stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "FER-2 [all: most ratios to literature values within 0.9–1.1] — Fig. 7 (§3)" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:combinedResults "each reference material in Table 3 (n = 3)" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "Li: 0.024; Be: 0.006; Sc: 0.028; Cr: 0.043; Co: 0.009; Ni: 0.014; Cu: 0.052; Zn: 0.176; Ge: 0.015; Rb: 0.009; Sr: 0.008; Cs: 0.006; Ba: 0.018; other: N — method detection limits (MDL, 3 s) in ng/g (Table 2); instrumental detection limits are also given, in ng/mL" ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "all: s, one standard deviation, and RSD — 'Mean ± 1 s (n = 3)'; 'RSD = standard deviation/mean × 100%'" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "Li: 0.026; Be: 0.008; Sc: 0.020; Cr: 0.068; Co: 0.007; Ni: 0.035; Cu: 0.089; Zn: 0.216; Ge: 0.020; Rb: 0.012; Sr: 0.010; Cs: 0.004; Ba: 0.029; other: N — ng/mL (Table 2); 'the highest blank level in Zn would contribute less than 0.01% of the amount of analyte'" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "mag_1, mag_3, mag_5, py_2, py_4; iron-formation reference material FER-2 (CCRMP, CANMET MMSL, Canada)" ;
    ada:samplingUnitName "Sample name only — \"mag_1\", \"mag_3\", \"mag_5\", \"py_2\", \"py_4\", each reported as \"Mean ± s (n = 3)\" with the replicates unlabelled (table, p.8)" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "FER-2 [all: RSD <5%] — three analyses, Table 3 (§3)" .

<ex:solutionSficpmsTAPP-P1> schema1:identifier "missing" .


```


### detail example P2
detail instance derived from Lu+etal2007 | Finnigan ELEMENT | PML Okayama.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-P2",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionSficpmsTAPP-P2",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1 (GSJ); BHVO-1, AGV-1, PCC-1, DTS-1 (USGS); Ivuna (CI1), Orgueil (CI1), Cold Bokkeveld (CM2), Allende (USNM 3529, Split 1, Pos. 23)",
  "ada:samplingUnitName": "Sample name only, except the Allende powder: \"the Smithsonian reference Allende powder (USNM 3529, Split 1, Pos. 23)\" (p.5). Solutions \"#1\"–\"#8\" (p.7) are synthetic yield-test solutions, not samples",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially -- \"Orgueil and Allende were analyzed 4 times and twice from the sample digestion, respectively ... analytical results for each run are shown in the table\" alongside the averages. No acceptance or rejection rule stated",
  "ada:combinedResults": "Orgueil average (4 runs); Allende average (2 runs) — Table 3",
  "ada:detectionLimit": "Ti: 4 µg/g; other: N — 3σ in rock; 21 ng/g in solution (Table 2b)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "all [Ti: RSD 3.6% (2.3–5.4%)] — TTi/93Nb RSD% (Table 2b)",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1 [all: consistent with previous studies] — abstract; Tables 5 and 6",
  "ada:goodnessOfFitOrDispersionStatistic": "all: RSD% — 'Averages of the reproducibility (RSD %)'"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-SF-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-P2",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionSficpmsTAPP-P2",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1 (GSJ); BHVO-1, AGV-1, PCC-1, DTS-1 (USGS); Ivuna (CI1), Orgueil (CI1), Cold Bokkeveld (CM2), Allende (USNM 3529, Split 1, Pos. 23)",
  "ada:samplingUnitName": "Sample name only, except the Allende powder: \"the Smithsonian reference Allende powder (USNM 3529, Split 1, Pos. 23)\" (p.5). Solutions \"#1\"\u2013\"#8\" (p.7) are synthetic yield-test solutions, not samples",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially -- \"Orgueil and Allende were analyzed 4 times and twice from the sample digestion, respectively ... analytical results for each run are shown in the table\" alongside the averages. No acceptance or rejection rule stated",
  "ada:combinedResults": "Orgueil average (4 runs); Allende average (2 runs) \u2014 Table 3",
  "ada:detectionLimit": "Ti: 4 \u00b5g/g; other: N \u2014 3\u03c3 in rock; 21 ng/g in solution (Table 2b)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "all [Ti: RSD 3.6% (2.3\u20135.4%)] \u2014 TTi/93Nb RSD% (Table 2b)",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1 [all: consistent with previous studies] \u2014 abstract; Tables 5 and 6",
  "ada:goodnessOfFitOrDispersionStatistic": "all: RSD% \u2014 'Averages of the reproducibility (RSD %)'"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-P2> a ada:SolutionICPMSTabular ;
    schema1:measurementTechnique <ex:solutionSficpmsTAPP-P2> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially -- \"Orgueil and Allende were analyzed 4 times and twice from the sample digestion, respectively ... analytical results for each run are shown in the table\" alongside the averages. No acceptance or rejection rule stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1 [all: consistent with previous studies] — abstract; Tables 5 and 6" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:combinedResults "Orgueil average (4 runs); Allende average (2 runs) — Table 3" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "Ti: 4 µg/g; other: N — 3σ in rock; 21 ng/g in solution (Table 2b)" ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "all: RSD% — 'Averages of the reproducibility (RSD %)'" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1 (GSJ); BHVO-1, AGV-1, PCC-1, DTS-1 (USGS); Ivuna (CI1), Orgueil (CI1), Cold Bokkeveld (CM2), Allende (USNM 3529, Split 1, Pos. 23)" ;
    ada:samplingUnitName "Sample name only, except the Allende powder: \"the Smithsonian reference Allende powder (USNM 3529, Split 1, Pos. 23)\" (p.5). Solutions \"#1\"–\"#8\" (p.7) are synthetic yield-test solutions, not samples" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "all [Ti: RSD 3.6% (2.3–5.4%)] — TTi/93Nb RSD% (Table 2b)" .

<ex:solutionSficpmsTAPP-P2> schema1:identifier "missing" .


```


### detail example P3
detail instance derived from Milne+etal2010 | Thermo Finnigan Element I | FSU NHMFL.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-P3",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionSficpmsTAPP-P3",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "N -- \"Each analytical session would begin and end with the analysis of a series of Mo standards (1-100 nM)\"; \"an analysis sequence\"; \"1 day's analysis\"; \"three separate days of analyses\". No session or sequence identifier stated",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Open-ocean seawater reference materials SAFe S1, SAFe D2 and NASS-5; GEOTRACES inter-calibration samples GS (surface) and GD (deep); depth-profile samples from the BATS station, 31 deg 45' N, 64 deg 05' W, 23 June 2008",
  "ada:samplingUnitName": "Sample name only — seawater samples by name (SAFe S1, SAFe D2, NASS-5; GEOTRACES \"(GS)\" and \"(GD)\", p.4); the 12 mL sub-samples are not labelled",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "Mn: 0.433 ± 0.026; Fe: 2.791 ± 0.083; Co: 0.078 ± 0.006; Ni: 0.457 ± 0.104; Cu: 0.184 ± 0.027; Zn: 3.044 ± 0.018; Cd: 0.045 ± 0.003; Pb: 0.017 ± 0.001 — pmol, mean reagent blank ± 1 SD from one day's analysis, elution acid plus ammonium acetate buffer (Table 5)",
  "ada:analysisInclusionAndRejectionCriteria": "Partially -- \"The blank solutions were analysed at least three times on the ICP-MS\"; \"parallel triplicate samples\"; n = 3 for reference materials and n = 5 for the GEOTRACES samples. No acceptance or rejection rule stated",
  "ada:combinedResults": "blank means; Co and Mn average standard-addition slopes; reference materials (n = 3); GEOTRACES samples (n = 5)",
  "ada:detectionLimit": "Mn: 0.007; Fe: 0.021; Co: 0.002; Ni: 0.026; Cu: 0.007; Zn: 0.005; Cd: 0.0006; Pb: 0.0002 — nM, 3 SD, for the extraction of a 12 mL sample (Table 5)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "NASS-5, SAFe S1, SAFe D2 [all: 95% confidence limit, n = 3] — Table 6",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "NASS-5, SAFe S1, SAFe D2 [all: agreement with the NASS-5 certified and SAFe consensus values] — Table 6",
  "ada:goodnessOfFitOrDispersionStatistic": "all: %RSD, with 1 S.D. for blanks — 'The precision is calculated as the percent relative standard deviation (% RSD)'; 'Mean blank ± 1S.D.'"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-SF-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-P3",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionSficpmsTAPP-P3",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "N -- \"Each analytical session would begin and end with the analysis of a series of Mo standards (1-100 nM)\"; \"an analysis sequence\"; \"1 day's analysis\"; \"three separate days of analyses\". No session or sequence identifier stated",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Open-ocean seawater reference materials SAFe S1, SAFe D2 and NASS-5; GEOTRACES inter-calibration samples GS (surface) and GD (deep); depth-profile samples from the BATS station, 31 deg 45' N, 64 deg 05' W, 23 June 2008",
  "ada:samplingUnitName": "Sample name only \u2014 seawater samples by name (SAFe S1, SAFe D2, NASS-5; GEOTRACES \"(GS)\" and \"(GD)\", p.4); the 12 mL sub-samples are not labelled",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "Mn: 0.433 \u00b1 0.026; Fe: 2.791 \u00b1 0.083; Co: 0.078 \u00b1 0.006; Ni: 0.457 \u00b1 0.104; Cu: 0.184 \u00b1 0.027; Zn: 3.044 \u00b1 0.018; Cd: 0.045 \u00b1 0.003; Pb: 0.017 \u00b1 0.001 \u2014 pmol, mean reagent blank \u00b1 1 SD from one day's analysis, elution acid plus ammonium acetate buffer (Table 5)",
  "ada:analysisInclusionAndRejectionCriteria": "Partially -- \"The blank solutions were analysed at least three times on the ICP-MS\"; \"parallel triplicate samples\"; n = 3 for reference materials and n = 5 for the GEOTRACES samples. No acceptance or rejection rule stated",
  "ada:combinedResults": "blank means; Co and Mn average standard-addition slopes; reference materials (n = 3); GEOTRACES samples (n = 5)",
  "ada:detectionLimit": "Mn: 0.007; Fe: 0.021; Co: 0.002; Ni: 0.026; Cu: 0.007; Zn: 0.005; Cd: 0.0006; Pb: 0.0002 \u2014 nM, 3 SD, for the extraction of a 12 mL sample (Table 5)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "NASS-5, SAFe S1, SAFe D2 [all: 95% confidence limit, n = 3] \u2014 Table 6",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "NASS-5, SAFe S1, SAFe D2 [all: agreement with the NASS-5 certified and SAFe consensus values] \u2014 Table 6",
  "ada:goodnessOfFitOrDispersionStatistic": "all: %RSD, with 1 S.D. for blanks \u2014 'The precision is calculated as the percent relative standard deviation (% RSD)'; 'Mean blank \u00b1 1S.D.'"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-P3> a ada:SolutionICPMSTabular ;
    schema1:measurementTechnique <ex:solutionSficpmsTAPP-P3> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially -- \"The blank solutions were analysed at least three times on the ICP-MS\"; \"parallel triplicate samples\"; n = 3 for reference materials and n = 5 for the GEOTRACES samples. No acceptance or rejection rule stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "NASS-5, SAFe S1, SAFe D2 [all: agreement with the NASS-5 certified and SAFe consensus values] — Table 6" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:combinedResults "blank means; Co and Mn average standard-addition slopes; reference materials (n = 3); GEOTRACES samples (n = 5)" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "Mn: 0.007; Fe: 0.021; Co: 0.002; Ni: 0.026; Cu: 0.007; Zn: 0.005; Cd: 0.0006; Pb: 0.0002 — nM, 3 SD, for the extraction of a 12 mL sample (Table 5)" ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "all: %RSD, with 1 S.D. for blanks — 'The precision is calculated as the percent relative standard deviation (% RSD)'; 'Mean blank ± 1S.D.'" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "Mn: 0.433 ± 0.026; Fe: 2.791 ± 0.083; Co: 0.078 ± 0.006; Ni: 0.457 ± 0.104; Cu: 0.184 ± 0.027; Zn: 3.044 ± 0.018; Cd: 0.045 ± 0.003; Pb: 0.017 ± 0.001 — pmol, mean reagent blank ± 1 SD from one day's analysis, elution acid plus ammonium acetate buffer (Table 5)" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "Open-ocean seawater reference materials SAFe S1, SAFe D2 and NASS-5; GEOTRACES inter-calibration samples GS (surface) and GD (deep); depth-profile samples from the BATS station, 31 deg 45' N, 64 deg 05' W, 23 June 2008" ;
    ada:samplingUnitName "Sample name only — seawater samples by name (SAFe S1, SAFe D2, NASS-5; GEOTRACES \"(GS)\" and \"(GD)\", p.4); the 12 mL sub-samples are not labelled" ;
    ada:sessionIdentifier "N -- \"Each analytical session would begin and end with the analysis of a series of Mo standards (1-100 nM)\"; \"an analysis sequence\"; \"1 day's analysis\"; \"three separate days of analyses\". No session or sequence identifier stated" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "NASS-5, SAFe S1, SAFe D2 [all: 95% confidence limit, n = 3] — Table 6" .

<ex:solutionSficpmsTAPP-P3> schema1:identifier "missing" .


```


### detail example P4
detail instance derived from Misra+etal2014 | Thermo Element XR | Univ Cambridge.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-P4",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionSficpmsTAPP-P4",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "N -- \"a single instrument session\" referenced; no session identifier stated",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "In-house consistency standards CAM-wuellerstorfi, CAM-Uvig-1, CAM-Uvig-2 and CAM-Mix; Globigerinoides sacculifer specimens of the 300-355 um size fraction",
  "ada:samplingUnitName": "Sample name only — consistency standards \"CAM-Uvig-1\", \"CAM-Uvig-2\", \"CAM-wuellerstorfi\", \"CAM-Mix\" (p.6); in the cleaning test each core-top sample was \"split into three fractions\" identified only by cleaning sequence (p.4)",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": 3,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "B: 2.0 ± 1.0 µmol/mol (as B/Ca); other: N — abstract",
  "ada:analysisInclusionAndRejectionCriteria": "Partially -- \"Open symbols represent an average of 10 measurements acquired during a single instrument session. The solid symbols represent the average of the open symbols\"; and for a second figure \"which is a total of 15 measurements\"; acquisition structured as 3 runs x 15 passes (low resolution) or 3 x 5 (medium). No acceptance or rejection rule stated",
  "ada:combinedResults": "session averages of the consistency standards (10 measurements each); overall averages of the session averages — figures",
  "ada:detectionLimit": "B/Ca: 2 µmol/mol; other: N — 'We report a B/Ca detection limit of 2 µmol/mol' (abstract)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "B/Ca: 1.0%; other: N — abstract",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "all [B/Ca: 4.0% (2σ), average within-run external precision] — abstract",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "CAM-wuellerstorfi, CAM-Uvig-1, CAM-Uvig-2, CAM-Mix [all: ±2σ of repeat analyses over 8 months] — Table 4; n = 180, 130, 100 and 150",
  "ada:analyticalAccuracyAndAssessmentMethod": "CAM-wuellerstorfi, CAM-Uvig-1, CAM-Uvig-2, CAM-Mix [B/Ca: across degrees of sample dilution] — Fig. 2",
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-SF-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-P4",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionSficpmsTAPP-P4",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "N -- \"a single instrument session\" referenced; no session identifier stated",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "In-house consistency standards CAM-wuellerstorfi, CAM-Uvig-1, CAM-Uvig-2 and CAM-Mix; Globigerinoides sacculifer specimens of the 300-355 um size fraction",
  "ada:samplingUnitName": "Sample name only \u2014 consistency standards \"CAM-Uvig-1\", \"CAM-Uvig-2\", \"CAM-wuellerstorfi\", \"CAM-Mix\" (p.6); in the cleaning test each core-top sample was \"split into three fractions\" identified only by cleaning sequence (p.4)",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": 3,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "B: 2.0 \u00b1 1.0 \u00b5mol/mol (as B/Ca); other: N \u2014 abstract",
  "ada:analysisInclusionAndRejectionCriteria": "Partially -- \"Open symbols represent an average of 10 measurements acquired during a single instrument session. The solid symbols represent the average of the open symbols\"; and for a second figure \"which is a total of 15 measurements\"; acquisition structured as 3 runs x 15 passes (low resolution) or 3 x 5 (medium). No acceptance or rejection rule stated",
  "ada:combinedResults": "session averages of the consistency standards (10 measurements each); overall averages of the session averages \u2014 figures",
  "ada:detectionLimit": "B/Ca: 2 \u00b5mol/mol; other: N \u2014 'We report a B/Ca detection limit of 2 \u00b5mol/mol' (abstract)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "B/Ca: 1.0%; other: N \u2014 abstract",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "all [B/Ca: 4.0% (2\u03c3), average within-run external precision] \u2014 abstract",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "CAM-wuellerstorfi, CAM-Uvig-1, CAM-Uvig-2, CAM-Mix [all: \u00b12\u03c3 of repeat analyses over 8 months] \u2014 Table 4; n = 180, 130, 100 and 150",
  "ada:analyticalAccuracyAndAssessmentMethod": "CAM-wuellerstorfi, CAM-Uvig-1, CAM-Uvig-2, CAM-Mix [B/Ca: across degrees of sample dilution] \u2014 Fig. 2",
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-P4> a ada:SolutionICPMSTabular ;
    schema1:measurementTechnique <ex:solutionSficpmsTAPP-P4> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially -- \"Open symbols represent an average of 10 measurements acquired during a single instrument session. The solid symbols represent the average of the open symbols\"; and for a second figure \"which is a total of 15 measurements\"; acquisition structured as 3 runs x 15 passes (low resolution) or 3 x 5 (medium). No acceptance or rejection rule stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "CAM-wuellerstorfi, CAM-Uvig-1, CAM-Uvig-2, CAM-Mix [B/Ca: across degrees of sample dilution] — Fig. 2" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "CAM-wuellerstorfi, CAM-Uvig-1, CAM-Uvig-2, CAM-Mix [all: ±2σ of repeat analyses over 8 months] — Table 4; n = 180, 130, 100 and 150" ;
    ada:combinedResults "session averages of the consistency standards (10 measurements each); overall averages of the session averages — figures" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "B/Ca: 2 µmol/mol; other: N — 'We report a B/Ca detection limit of 2 µmol/mol' (abstract)" ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "B/Ca: 1.0%; other: N — abstract" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:numberOfReplicates 3 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "B: 2.0 ± 1.0 µmol/mol (as B/Ca); other: N — abstract" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "In-house consistency standards CAM-wuellerstorfi, CAM-Uvig-1, CAM-Uvig-2 and CAM-Mix; Globigerinoides sacculifer specimens of the 300-355 um size fraction" ;
    ada:samplingUnitName "Sample name only — consistency standards \"CAM-Uvig-1\", \"CAM-Uvig-2\", \"CAM-wuellerstorfi\", \"CAM-Mix\" (p.6); in the cleaning test each core-top sample was \"split into three fractions\" identified only by cleaning sequence (p.4)" ;
    ada:sessionIdentifier "N -- \"a single instrument session\" referenced; no session identifier stated" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "all [B/Ca: 4.0% (2σ), average within-run external precision] — abstract" .

<ex:solutionSficpmsTAPP-P4> schema1:identifier "missing" .


```


### detail example Willbold2005
detail instance derived from Willbold2005 | ThermoFinnigan ELEMENT2 | MPI Mainz.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Willbold2005",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionSficpmsTAPP-Willbold2005",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "AGV-1, AGV-2, BCR-1, BCR-2, BCR-2G, BIR-1, BIR-1G, BHVO-1, BHVO-2, BHVO-2G, G-2, JR-1, KL2-G, ML3B-G, NIST SRM 612, OU-6, PCC-1 -- tabulated with issuing organisation and split/position numbers (e.g. BHVO-1 Split 15 Pos 26; G-2 Split 58 Pos 23)",
  "ada:samplingUnitName": "Labelled for BHVO-1: digestions \"BHVO-1 (1)\" to \"BHVO-1 (5)\", each with determinations \"1 2 3\" (Table 4, pp.8–9); the other reference materials by name with their issuing split and position (e.g. AGV-1 Split 35 Pos 13; Table 2, p.6)",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": 3,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "N — the total procedural blanks enter only through the LOD",
  "ada:analysisInclusionAndRejectionCriteria": "Partially, and the most complete of the six -- \"Five independent analyses (different spikings/digestions) of BHVO-1 were carried out over a time period of 4 months. Triplicate determinations were performed for each digestion\"; \"the results of three to four independent analyses of sixteen other RMs\"; \"Only one digestion was prepared for the USGS reference glasses BCR-2G, BHVO-2G and BIR-1G, and NIST SRM 612 respectively and were measured in triplicate\". No acceptance or rejection rule stated",
  "ada:combinedResults": "BHVO-1 (five digestions, triplicate each); sixteen other RMs (three to four analyses each); BCR-2G, BHVO-2G, BIR-1G and NIST SRM 612 (one digestion, triplicate) — Tables 4 and 5",
  "ada:detectionLimit": "all: about 0.1 to 10 ng/g sample equivalent for most elements — Figure 2",
  "ada:limitOfQuantificationMethod": "all: RSD better than 10% on the low-concentration RM PCC-1, ca. 10 to 900 ng/g — 'about 10 to 20 times the LOD for most elements'",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "BHVO-1 [all: RSD of triplicate determinations on one digestion, generally better than 1%] — Table 4",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "BHVO-1 [all: RSD of five independent digestions over 4 months, 1–3%] — abstract and Table 4; the sixteen other RMs by RSD of three to four independent analyses (Table 5)",
  "ada:analyticalAccuracyAndAssessmentMethod": "BHVO-1 [all: within 1–2% of published ID data and 2–3% of all published data]; AGV-1, AGV-2, BCR-1, BCR-2, BCR-2G, BIR-1, BIR-1G, BHVO-2, BHVO-2G, G-2, JR-1, KL2-G, ML3B-G, NIST SRM 612, OU-6, PCC-1 [all: most within 3–4% of published data] — abstract; Table 5",
  "ada:goodnessOfFitOrDispersionStatistic": "all: RSD — Tables 4 and 5",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/solutionSficpmsTAPP/spikeOutlierFilteringApproach",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionSficpmsTAPP/spikeOutlierFilteringApproach"
        }
      ],
      "schema:name": "Spike / Outlier Filtering Approach",
      "schema:value": "Dixon outlier test on each block of ten ratios — 'Generally, less than one ratio had to be excluded from the whole data set'"
    }
  ]
}

```

#### jsonld
```jsonld
{
  "@context": [
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    },
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-SF-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Willbold2005",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionSficpmsTAPP-Willbold2005",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "AGV-1, AGV-2, BCR-1, BCR-2, BCR-2G, BIR-1, BIR-1G, BHVO-1, BHVO-2, BHVO-2G, G-2, JR-1, KL2-G, ML3B-G, NIST SRM 612, OU-6, PCC-1 -- tabulated with issuing organisation and split/position numbers (e.g. BHVO-1 Split 15 Pos 26; G-2 Split 58 Pos 23)",
  "ada:samplingUnitName": "Labelled for BHVO-1: digestions \"BHVO-1 (1)\" to \"BHVO-1 (5)\", each with determinations \"1 2 3\" (Table 4, pp.8\u20139); the other reference materials by name with their issuing split and position (e.g. AGV-1 Split 35 Pos 13; Table 2, p.6)",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": 3,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "N \u2014 the total procedural blanks enter only through the LOD",
  "ada:analysisInclusionAndRejectionCriteria": "Partially, and the most complete of the six -- \"Five independent analyses (different spikings/digestions) of BHVO-1 were carried out over a time period of 4 months. Triplicate determinations were performed for each digestion\"; \"the results of three to four independent analyses of sixteen other RMs\"; \"Only one digestion was prepared for the USGS reference glasses BCR-2G, BHVO-2G and BIR-1G, and NIST SRM 612 respectively and were measured in triplicate\". No acceptance or rejection rule stated",
  "ada:combinedResults": "BHVO-1 (five digestions, triplicate each); sixteen other RMs (three to four analyses each); BCR-2G, BHVO-2G, BIR-1G and NIST SRM 612 (one digestion, triplicate) \u2014 Tables 4 and 5",
  "ada:detectionLimit": "all: about 0.1 to 10 ng/g sample equivalent for most elements \u2014 Figure 2",
  "ada:limitOfQuantificationMethod": "all: RSD better than 10% on the low-concentration RM PCC-1, ca. 10 to 900 ng/g \u2014 'about 10 to 20 times the LOD for most elements'",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "BHVO-1 [all: RSD of triplicate determinations on one digestion, generally better than 1%] \u2014 Table 4",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "BHVO-1 [all: RSD of five independent digestions over 4 months, 1\u20133%] \u2014 abstract and Table 4; the sixteen other RMs by RSD of three to four independent analyses (Table 5)",
  "ada:analyticalAccuracyAndAssessmentMethod": "BHVO-1 [all: within 1\u20132% of published ID data and 2\u20133% of all published data]; AGV-1, AGV-2, BCR-1, BCR-2, BCR-2G, BIR-1, BIR-1G, BHVO-2, BHVO-2G, G-2, JR-1, KL2-G, ML3B-G, NIST SRM 612, OU-6, PCC-1 [all: most within 3\u20134% of published data] \u2014 abstract; Table 5",
  "ada:goodnessOfFitOrDispersionStatistic": "all: RSD \u2014 Tables 4 and 5",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/solutionSficpmsTAPP/spikeOutlierFilteringApproach",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionSficpmsTAPP/spikeOutlierFilteringApproach"
        }
      ],
      "schema:name": "Spike / Outlier Filtering Approach",
      "schema:value": "Dixon outlier test on each block of ten ratios \u2014 'Generally, less than one ratio had to be excluded from the whole data set'"
    }
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Willbold2005> a ada:SolutionICPMSTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/spikeOutlierFilteringApproach> ;
    schema1:measurementTechnique <ex:solutionSficpmsTAPP-Willbold2005> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially, and the most complete of the six -- \"Five independent analyses (different spikings/digestions) of BHVO-1 were carried out over a time period of 4 months. Triplicate determinations were performed for each digestion\"; \"the results of three to four independent analyses of sixteen other RMs\"; \"Only one digestion was prepared for the USGS reference glasses BCR-2G, BHVO-2G and BIR-1G, and NIST SRM 612 respectively and were measured in triplicate\". No acceptance or rejection rule stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "BHVO-1 [all: within 1–2% of published ID data and 2–3% of all published data]; AGV-1, AGV-2, BCR-1, BCR-2, BCR-2G, BIR-1, BIR-1G, BHVO-2, BHVO-2G, G-2, JR-1, KL2-G, ML3B-G, NIST SRM 612, OU-6, PCC-1 [all: most within 3–4% of published data] — abstract; Table 5" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "BHVO-1 [all: RSD of five independent digestions over 4 months, 1–3%] — abstract and Table 4; the sixteen other RMs by RSD of three to four independent analyses (Table 5)" ;
    ada:combinedResults "BHVO-1 (five digestions, triplicate each); sixteen other RMs (three to four analyses each); BCR-2G, BHVO-2G, BIR-1G and NIST SRM 612 (one digestion, triplicate) — Tables 4 and 5" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "all: about 0.1 to 10 ng/g sample equivalent for most elements — Figure 2" ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "all: RSD — Tables 4 and 5" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "all: RSD better than 10% on the low-concentration RM PCC-1, ca. 10 to 900 ng/g — 'about 10 to 20 times the LOD for most elements'" ;
    ada:numberOfReplicates 3 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "N — the total procedural blanks enter only through the LOD" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "AGV-1, AGV-2, BCR-1, BCR-2, BCR-2G, BIR-1, BIR-1G, BHVO-1, BHVO-2, BHVO-2G, G-2, JR-1, KL2-G, ML3B-G, NIST SRM 612, OU-6, PCC-1 -- tabulated with issuing organisation and split/position numbers (e.g. BHVO-1 Split 15 Pos 26; G-2 Split 58 Pos 23)" ;
    ada:samplingUnitName "Labelled for BHVO-1: digestions \"BHVO-1 (1)\" to \"BHVO-1 (5)\", each with determinations \"1 2 3\" (Table 4, pp.8–9); the other reference materials by name with their issuing split and position (e.g. AGV-1 Split 35 Pos 13; Table 2, p.6)" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "BHVO-1 [all: RSD of triplicate determinations on one digestion, generally better than 1%] — Table 4" .

<ex:solutionSficpmsTAPP-Willbold2005> schema1:identifier "missing" .

<https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/spikeOutlierFilteringApproach> a schema1:PropertyValue ;
    schema1:name "Spike / Outlier Filtering Approach" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionSficpmsTAPP/spikeOutlierFilteringApproach> ;
    schema1:value "Dixon outlier test on each block of ten ratios — 'Generally, less than one ratio had to be excluded from the whole data set'" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Solution SF-ICP-MS Analysis Detail
description: Dataset-level analysis-instance detail for solution SF-ICP-MS, reusing
  CDIF/schema.org slots on the schema:Dataset root.
allOf:
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/AnalysisIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/calibrationFactor/schema.yaml#/$defs/AnalysisIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/aggregation/schema.yaml#/$defs/AnalysisIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/AnalysisIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/compositionQC/schema.yaml#/$defs/AnalysisIdentification
- type: object
  properties:
    prov:wasGeneratedBy:
      type: array
      items:
        type: object
        properties:
          prov:used:
            type: array
            items:
              type: object
              allOf:
              - if:
                  required:
                  - schema:instrument
                then:
                  properties:
                    schema:instrument:
                      type: array
                      items:
                        allOf:
                        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/instrument/schema.yaml
                        - type: object
                          allOf:
                          - if:
                              properties:
                                schema:additionalType:
                                  contains:
                                    const: ICPMS
                                  schema:inDefinedTermSet: ada:vocab/instrumentType
                              required:
                              - schema:additionalType
                            then:
                              properties:
                                schema:hasPart:
                                  type: array
                                  items:
                                    type: object
                                    allOf:
                                    - if:
                                        properties:
                                          schema:additionalType:
                                            contains:
                                              const: ICP Source
                                            schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                                        required:
                                        - schema:additionalType
                                      then:
                                        properties:
                                          schema:additionalProperty:
                                            type: array
                                            items:
                                              anyOf:
                                              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_auxiliaryGasFlowRate
                                              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_coolantPlasmaGasFlowRate
                                              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_rfPower
                                            allOf:
                                            - contains:
                                                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_auxiliaryGasFlowRate
                                              minContains: 0
                                              maxContains: 1
                                            - contains:
                                                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_coolantPlasmaGasFlowRate
                                              minContains: 0
                                              maxContains: 1
                                            - contains:
                                                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_rfPower
                                              minContains: 0
                                              maxContains: 1
                                    - if:
                                        properties:
                                          schema:additionalType:
                                            contains:
                                              const: Sample Introduction System
                                            schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                                        required:
                                        - schema:additionalType
                                      then:
                                        properties:
                                          schema:additionalProperty:
                                            type: array
                                            items:
                                              anyOf:
                                              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_makeUpGasAndFlowRate
                                              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Analysis_nebulizerGasFlowRate
                                              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Analysis_sampleUptakeRate
                                            allOf:
                                            - contains:
                                                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_makeUpGasAndFlowRate
                                              minContains: 0
                                              maxContains: 1
                                            - contains:
                                                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Analysis_nebulizerGasFlowRate
                                              minContains: 0
                                              maxContains: 1
                                            - contains:
                                                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Analysis_sampleUptakeRate
                                              minContains: 0
                                              maxContains: 1
                                    - if:
                                        properties:
                                          schema:additionalType:
                                            contains:
                                              const: Torch
                                            schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                                        required:
                                        - schema:additionalType
                                      then:
                                        properties:
                                          schema:additionalProperty:
                                            type: array
                                            items:
                                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_torchDepth
                                            allOf:
                                            - contains:
                                                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_torchDepth
                                              minContains: 0
                                              maxContains: 1
                                  allOf:
                                  - contains:
                                      properties:
                                        schema:additionalType:
                                          contains:
                                            const: ICP Source
                                          schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                                      required:
                                      - schema:additionalType
                                  - contains:
                                      properties:
                                        schema:additionalType:
                                          contains:
                                            const: Sample Introduction System
                                          schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                                      required:
                                      - schema:additionalType
                                schema:additionalProperty:
                                  type: array
                                  items:
                                    anyOf:
                                    - title: Doubly-Charged Species Monitor
                                      description: "The mass ratio monitored to estimate
                                        doubly-charged ion (M\xB2\u207A) formation
                                        during instrument tuning. The monitor species
                                        and the mass positions monitored should be
                                        stated explicitly. Analogous to Oxide Production
                                        Method and Threshold for oxide monitoring."
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/solutionSficpmsTAPP/doublyChargedSpeciesMonitor
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/solutionSficpmsTAPP/doublyChargedSpeciesMonitor
                                        schema:name:
                                          const: Doubly-Charged Species Monitor
                                        schema:value:
                                          type: string
                                      required:
                                      - '@id'
                                      - '@type'
                                      - schema:propertyID
                                      - schema:name
                                      - schema:value
                                    - title: Doubly-Charged Species Production
                                      description: Measured percentage of doubly-charged
                                        ion production for the monitored species at
                                        the time of instrument tuning. The acceptable
                                        threshold is typically <1% or <3%. Record
                                        both the threshold and the measured value.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/solutionSficpmsTAPP/doublyChargedSpeciesProduction
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/solutionSficpmsTAPP/doublyChargedSpeciesProduction
                                        schema:name:
                                          const: Doubly-Charged Species Production
                                        schema:value:
                                          type: string
                                      required:
                                      - '@id'
                                      - '@type'
                                      - schema:propertyID
                                      - schema:name
                                      - schema:value
                                    - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_massResolutionSetting
                                    - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_memoryEffectMitigation
                                    - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_icpTuning
                                  allOf:
                                  - contains:
                                      title: Doubly-Charged Species Monitor
                                      description: "The mass ratio monitored to estimate
                                        doubly-charged ion (M\xB2\u207A) formation
                                        during instrument tuning. The monitor species
                                        and the mass positions monitored should be
                                        stated explicitly. Analogous to Oxide Production
                                        Method and Threshold for oxide monitoring."
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/solutionSficpmsTAPP/doublyChargedSpeciesMonitor
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/solutionSficpmsTAPP/doublyChargedSpeciesMonitor
                                        schema:name:
                                          const: Doubly-Charged Species Monitor
                                        schema:value:
                                          type: string
                                      required:
                                      - '@id'
                                      - '@type'
                                      - schema:propertyID
                                      - schema:name
                                      - schema:value
                                    minContains: 0
                                    maxContains: 1
                                  - contains:
                                      title: Doubly-Charged Species Production
                                      description: Measured percentage of doubly-charged
                                        ion production for the monitored species at
                                        the time of instrument tuning. The acceptable
                                        threshold is typically <1% or <3%. Record
                                        both the threshold and the measured value.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/solutionSficpmsTAPP/doublyChargedSpeciesProduction
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/solutionSficpmsTAPP/doublyChargedSpeciesProduction
                                        schema:name:
                                          const: Doubly-Charged Species Production
                                        schema:value:
                                          type: string
                                      required:
                                      - '@id'
                                      - '@type'
                                      - schema:propertyID
                                      - schema:name
                                      - schema:value
                                    minContains: 0
                                    maxContains: 1
                                  - contains:
                                      $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_massResolutionSetting
                                    minContains: 0
                                    maxContains: 1
                                  - contains:
                                      $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_memoryEffectMitigation
                                    minContains: 0
                                    maxContains: 1
                                  - contains:
                                      $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_icpTuning
                                    minContains: 0
                                    maxContains: 1
                      allOf:
                      - contains:
                          properties:
                            schema:additionalType:
                              contains:
                                const: ICPMS
                              schema:inDefinedTermSet: ada:vocab/instrumentType
                          required:
                          - schema:additionalType
          schema:object:
            type: array
            items:
              type: object
              allOf:
              - if:
                  properties:
                    '@type':
                      contains:
                        const: https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample
                  required:
                  - '@type'
                then:
                  properties:
                    schema:description:
                      description: Brief description of sample provenance, form, or
                        preparation state relevant to this analysis.
                      anyOf:
                      - type: string
                      - type: array
                        items:
                          type: string
                    schema:additionalProperty:
                      type: array
                      items:
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Analysis_sampleAliquotMassOrVolume
                      allOf:
                      - contains:
                          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Analysis_sampleAliquotMassOrVolume
                        minContains: 0
                        maxContains: 1
                  required:
                  - schema:description
            allOf:
            - contains:
                properties:
                  '@type':
                    contains:
                      const: https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample
                required:
                - '@type'
          schema:actionProcess:
            type: object
            properties:
              schema:step:
                type: array
                items:
                  type: object
                  allOf:
                  - if:
                      properties:
                        schema:name:
                          const: Sample digestion
                      required:
                      - schema:name
                    then:
                      properties:
                        schema:additionalProperty:
                          type: array
                          items:
                            anyOf:
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Analysis_digestionDuration
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Analysis_digestionTemperature
                          allOf:
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Analysis_digestionDuration
                            minContains: 0
                            maxContains: 1
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Analysis_digestionTemperature
                            minContains: 0
                            maxContains: 1
                  - if:
                      properties:
                        schema:name:
                          const: Data reduction
                      required:
                      - schema:name
                    then:
                      properties:
                        schema:additionalProperty:
                          type: array
                          items:
                            anyOf:
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/singleCollector/schema.yaml#/$defs/Param_Analysis_pulseAnalogDetectorNonlinearityCorrection
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_filteringApproach
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Analysis_constantsReferenceValues
                          allOf:
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/singleCollector/schema.yaml#/$defs/Param_Analysis_pulseAnalogDetectorNonlinearityCorrection
                            minContains: 0
                            maxContains: 1
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_filteringApproach
                            minContains: 0
                            maxContains: 1
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Analysis_constantsReferenceValues
                            minContains: 0
                            maxContains: 1
                allOf:
                - contains:
                    properties:
                      schema:name:
                        const: Sample digestion
                    required:
                    - schema:name
                - contains:
                    properties:
                      schema:name:
                        const: Data reduction
                    required:
                    - schema:name
          schema:additionalProperty:
            type: array
            items:
              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_signalIntegrationTime
            allOf:
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_signalIntegrationTime
              minContains: 0
              maxContains: 1
          ada:proceduralBlankLevel:
            description: "The measured level of the analytical blank in the session,
              and \u2014 where the reported quantity is a ratio \u2014 its composition,
              since a blank subtracted from a ratio biases the result unless its own
              composition is known. Companion to the blank correction method."
            type: string
        required:
        - ada:proceduralBlankLevel
        - schema:actionProcess

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-SF-ICPMS/detail/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-SF-ICPMS/detail/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "ada": "https://ada.astromat.org/metadata/",
    "bios": "https://bioschemas.org/",
    "prov": "http://www.w3.org/ns/prov#",
    "schema": "http://schema.org/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "spdx": "http://spdx.org/rdf/terms#",
    "nxs": "https://manual.nexusformat.org/classes/",
    "dcterms": "http://purl.org/dc/terms/",
    "geosparql": "http://www.opengis.net/ont/geosparql#",
    "dqv": "http://www.w3.org/ns/dqv#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "wd": "https://www.wikidata.org/entity/",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-SF-ICPMS/detail/context.jsonld)

## Sources

* [Solution_SF-ICP-MS_TAPP_v5.xlsx (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/Solution-SF-ICPMS/detail`

