
# Solution Q-ICP-MS Analysis Detail (Schema)

`ogch.techniqueProfile.geochemProfile.Solution-Q-ICPMS.detail` *v0.1*

Dataset-level analysis-instance detail for solution Q-ICP-MS, reusing CDIF/schema.org slots on the schema:Dataset root.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### detail example Gao2008
detail instance derived from Hu+Gao2008 | PerkinElmer ELAN 6100 DRC | NWU Xi'an.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Gao2008",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionQicpmsTAPP-Gao2008",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "AGV-1 (andesite), BHVO-1 (basalt), G-2 (granite), SCO-1 (shale), GSR-5 (shale); GSR-6 and \"another eighteen international\" RMs; worldwide loess and Chinese upper-crustal composites",
  "ada:samplingUnitName": "Sample name only — Table 2 reports \"AGV-1\", \"BHVO-1\", \"G-2\", \"SCO-1\", \"GSR-5\" with replicate counts (n = 6, 5, 7, 4, 4) and no replicate labels (p.4)",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "Li: 0.036 ± 0.028; Be: 0.00091 ± 0.00049; B: 0.39 ± 0.26; Sc: 0.033 ± 0.011; V: 0.50 ± 0.38; Cr: 0.53 ± 0.16; Co: 0.0046 ± 0.0032; Ni: 0.065 ± 0.037; Cu: 0.072 ± 0.022; Zn: 0.80 ± 0.56; Ga: 0.0037 ± 0.0020; Ge: 0.0081 ± 0.0040; As: 0.021 ± 0.009; Rb: 0.11 ± 0.05; Sr: 0.018 ± 0.018; Y: 0.0018 ± 0.0017; Zr: 0.0030 ± 0.0015; Nb: 0.0012 ± 0.0012; Mo: 0.035 ± 0.030; Cd: 0.0026 ± 0.0015; In: 0.00016 ± 0.00004; Sn: 0.0083 ± 0.0016; Sb: 0.010 ± 0.006; Te: 0.00097 ± 0.00014; Cs: 0.00060 ± 0.00034; Ba: 0.075 ± 0.063; La: 0.0025 ± 0.0020; Ce: 0.0028 ± 0.0016; Pr: 0.00056 ± 0.00042; Nd: 0.0019 ± 0.0017; Sm: 0.00079 ± 0.00036; Eu: 0.00023 ± 0.00014; Gd: 0.00063 ± 0.00054; Tb: 0.00013 ± 0.00005; Dy: 0.00058 ± 0.00038; Ho: 0.00013 ± 0.00008; Er: 0.00027 ± 0.00020; Tm: 0.00011 ± 0.00003; Yb: 0.00043 ± 0.00025; Lu: 0.00015 ± 0.00007; Hf: 0.0010 ± 0.0012; Ta: 0.00017 ± 0.00009; W: 0.023 ± 0.010; Tl: 0.0026 ± 0.0009; Pb: 0.043 ± 0.020; Bi: 0.00049 ± 0.00028; Th: 0.00062 ± 0.00050; U: 0.00027 ± 0.00025 — ppb, mean ± STD of n = 5 blanks (Table 2)",
  "ada:analysisInclusionAndRejectionCriteria": "Partially -- replicate counts stated per reference material (n = 6, 5, 7, 4, 4; blanks n = 5). No acceptance or rejection rule, and no acquired-versus-included count, stated",
  "ada:combinedResults": "AGV-1 (n = 6); BHVO-1 (n = 5); G-2 (n = 7); GSR-5 (n = 4); SCO-1 (n = 4); blank (n = 5) — Table 2",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "AGV-1, BHVO-1, G-2, GSR-5, SCO-1 [all: RSD of n = 4–7 analyses, usually <8%] — Table 2 and §3.4; whether the replicates share a session is not stated",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "AGV-1, BHVO-1, G-2, GSR-5, SCO-1 [all: agreement with GeoReM preferred values (AGV-1, BHVO-1) and Govindaraju 1994 (G-2, GSR-5, SCO-1), better than 8% for most elements]; JP-1, DTS-1, BHVO-2, BIR-1, JB-3, GSR-3, DNC-1, W-2, AGV-2, BCR-2, JA-3, GSR-2, JG-3, GSR-1, RGM-1, GSR-4, SGR-1, GSR-6 [Mo, Cd, In, Sn, Sb, W, Tl, Bi, As, Te: reasonable agreement with Govindaraju 1994 and GeoReM] — Tables 2 and 3, §3.4",
  "ada:goodnessOfFitOrDispersionStatistic": "all: RSD, relative standard deviation in percent — Table 2: 'The RSD is the relative standard deviation in percent'"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-Q-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Gao2008",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionQicpmsTAPP-Gao2008",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "AGV-1 (andesite), BHVO-1 (basalt), G-2 (granite), SCO-1 (shale), GSR-5 (shale); GSR-6 and \"another eighteen international\" RMs; worldwide loess and Chinese upper-crustal composites",
  "ada:samplingUnitName": "Sample name only \u2014 Table 2 reports \"AGV-1\", \"BHVO-1\", \"G-2\", \"SCO-1\", \"GSR-5\" with replicate counts (n = 6, 5, 7, 4, 4) and no replicate labels (p.4)",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "Li: 0.036 \u00b1 0.028; Be: 0.00091 \u00b1 0.00049; B: 0.39 \u00b1 0.26; Sc: 0.033 \u00b1 0.011; V: 0.50 \u00b1 0.38; Cr: 0.53 \u00b1 0.16; Co: 0.0046 \u00b1 0.0032; Ni: 0.065 \u00b1 0.037; Cu: 0.072 \u00b1 0.022; Zn: 0.80 \u00b1 0.56; Ga: 0.0037 \u00b1 0.0020; Ge: 0.0081 \u00b1 0.0040; As: 0.021 \u00b1 0.009; Rb: 0.11 \u00b1 0.05; Sr: 0.018 \u00b1 0.018; Y: 0.0018 \u00b1 0.0017; Zr: 0.0030 \u00b1 0.0015; Nb: 0.0012 \u00b1 0.0012; Mo: 0.035 \u00b1 0.030; Cd: 0.0026 \u00b1 0.0015; In: 0.00016 \u00b1 0.00004; Sn: 0.0083 \u00b1 0.0016; Sb: 0.010 \u00b1 0.006; Te: 0.00097 \u00b1 0.00014; Cs: 0.00060 \u00b1 0.00034; Ba: 0.075 \u00b1 0.063; La: 0.0025 \u00b1 0.0020; Ce: 0.0028 \u00b1 0.0016; Pr: 0.00056 \u00b1 0.00042; Nd: 0.0019 \u00b1 0.0017; Sm: 0.00079 \u00b1 0.00036; Eu: 0.00023 \u00b1 0.00014; Gd: 0.00063 \u00b1 0.00054; Tb: 0.00013 \u00b1 0.00005; Dy: 0.00058 \u00b1 0.00038; Ho: 0.00013 \u00b1 0.00008; Er: 0.00027 \u00b1 0.00020; Tm: 0.00011 \u00b1 0.00003; Yb: 0.00043 \u00b1 0.00025; Lu: 0.00015 \u00b1 0.00007; Hf: 0.0010 \u00b1 0.0012; Ta: 0.00017 \u00b1 0.00009; W: 0.023 \u00b1 0.010; Tl: 0.0026 \u00b1 0.0009; Pb: 0.043 \u00b1 0.020; Bi: 0.00049 \u00b1 0.00028; Th: 0.00062 \u00b1 0.00050; U: 0.00027 \u00b1 0.00025 \u2014 ppb, mean \u00b1 STD of n = 5 blanks (Table 2)",
  "ada:analysisInclusionAndRejectionCriteria": "Partially -- replicate counts stated per reference material (n = 6, 5, 7, 4, 4; blanks n = 5). No acceptance or rejection rule, and no acquired-versus-included count, stated",
  "ada:combinedResults": "AGV-1 (n = 6); BHVO-1 (n = 5); G-2 (n = 7); GSR-5 (n = 4); SCO-1 (n = 4); blank (n = 5) \u2014 Table 2",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "AGV-1, BHVO-1, G-2, GSR-5, SCO-1 [all: RSD of n = 4\u20137 analyses, usually <8%] \u2014 Table 2 and \u00a73.4; whether the replicates share a session is not stated",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "AGV-1, BHVO-1, G-2, GSR-5, SCO-1 [all: agreement with GeoReM preferred values (AGV-1, BHVO-1) and Govindaraju 1994 (G-2, GSR-5, SCO-1), better than 8% for most elements]; JP-1, DTS-1, BHVO-2, BIR-1, JB-3, GSR-3, DNC-1, W-2, AGV-2, BCR-2, JA-3, GSR-2, JG-3, GSR-1, RGM-1, GSR-4, SGR-1, GSR-6 [Mo, Cd, In, Sn, Sb, W, Tl, Bi, As, Te: reasonable agreement with Govindaraju 1994 and GeoReM] \u2014 Tables 2 and 3, \u00a73.4",
  "ada:goodnessOfFitOrDispersionStatistic": "all: RSD, relative standard deviation in percent \u2014 Table 2: 'The RSD is the relative standard deviation in percent'"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Gao2008> a ada:SolutionICPMSTabular ;
    schema1:measurementTechnique <ex:solutionQicpmsTAPP-Gao2008> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially -- replicate counts stated per reference material (n = 6, 5, 7, 4, 4; blanks n = 5). No acceptance or rejection rule, and no acquired-versus-included count, stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "AGV-1, BHVO-1, G-2, GSR-5, SCO-1 [all: agreement with GeoReM preferred values (AGV-1, BHVO-1) and Govindaraju 1994 (G-2, GSR-5, SCO-1), better than 8% for most elements]; JP-1, DTS-1, BHVO-2, BIR-1, JB-3, GSR-3, DNC-1, W-2, AGV-2, BCR-2, JA-3, GSR-2, JG-3, GSR-1, RGM-1, GSR-4, SGR-1, GSR-6 [Mo, Cd, In, Sn, Sb, W, Tl, Bi, As, Te: reasonable agreement with Govindaraju 1994 and GeoReM] — Tables 2 and 3, §3.4" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:combinedResults "AGV-1 (n = 6); BHVO-1 (n = 5); G-2 (n = 7); GSR-5 (n = 4); SCO-1 (n = 4); blank (n = 5) — Table 2" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "all: RSD, relative standard deviation in percent — Table 2: 'The RSD is the relative standard deviation in percent'" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "Li: 0.036 ± 0.028; Be: 0.00091 ± 0.00049; B: 0.39 ± 0.26; Sc: 0.033 ± 0.011; V: 0.50 ± 0.38; Cr: 0.53 ± 0.16; Co: 0.0046 ± 0.0032; Ni: 0.065 ± 0.037; Cu: 0.072 ± 0.022; Zn: 0.80 ± 0.56; Ga: 0.0037 ± 0.0020; Ge: 0.0081 ± 0.0040; As: 0.021 ± 0.009; Rb: 0.11 ± 0.05; Sr: 0.018 ± 0.018; Y: 0.0018 ± 0.0017; Zr: 0.0030 ± 0.0015; Nb: 0.0012 ± 0.0012; Mo: 0.035 ± 0.030; Cd: 0.0026 ± 0.0015; In: 0.00016 ± 0.00004; Sn: 0.0083 ± 0.0016; Sb: 0.010 ± 0.006; Te: 0.00097 ± 0.00014; Cs: 0.00060 ± 0.00034; Ba: 0.075 ± 0.063; La: 0.0025 ± 0.0020; Ce: 0.0028 ± 0.0016; Pr: 0.00056 ± 0.00042; Nd: 0.0019 ± 0.0017; Sm: 0.00079 ± 0.00036; Eu: 0.00023 ± 0.00014; Gd: 0.00063 ± 0.00054; Tb: 0.00013 ± 0.00005; Dy: 0.00058 ± 0.00038; Ho: 0.00013 ± 0.00008; Er: 0.00027 ± 0.00020; Tm: 0.00011 ± 0.00003; Yb: 0.00043 ± 0.00025; Lu: 0.00015 ± 0.00007; Hf: 0.0010 ± 0.0012; Ta: 0.00017 ± 0.00009; W: 0.023 ± 0.010; Tl: 0.0026 ± 0.0009; Pb: 0.043 ± 0.020; Bi: 0.00049 ± 0.00028; Th: 0.00062 ± 0.00050; U: 0.00027 ± 0.00025 — ppb, mean ± STD of n = 5 blanks (Table 2)" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "AGV-1 (andesite), BHVO-1 (basalt), G-2 (granite), SCO-1 (shale), GSR-5 (shale); GSR-6 and \"another eighteen international\" RMs; worldwide loess and Chinese upper-crustal composites" ;
    ada:samplingUnitName "Sample name only — Table 2 reports \"AGV-1\", \"BHVO-1\", \"G-2\", \"SCO-1\", \"GSR-5\" with replicate counts (n = 6, 5, 7, 4, 4) and no replicate labels (p.4)" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "AGV-1, BHVO-1, G-2, GSR-5, SCO-1 [all: RSD of n = 4–7 analyses, usually <8%] — Table 2 and §3.4; whether the replicates share a session is not stated" .

<ex:solutionQicpmsTAPP-Gao2008> schema1:identifier "missing" .


```


### detail example P1
detail instance derived from Yu+etal2005 | PerkinElmer ELAN DRC II | Univ Cambridge.
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
      "@id": "ex:solutionQicpmsTAPP-P1",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "N -- \"a typical run (~5 hr)\" referenced; no run identifier stated",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Partially -- sample type named (\"core top Cibicidoides wuellerstorfi from the north Atlantic Ocean\"); no individual sample identifiers stated in the methods",
  "ada:samplingUnitName": "N — only the sample type is named (core-top Cibicidoides wuellerstorfi); no sample or aliquot identifiers are stated",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": 6,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "Li, Mg, Sr: <1%; Cd: <2%; Zn: <4%; U: <5%; B: 5%; other: N — relative to typical foraminiferal ratios; Ca also <1%; B was 30% with a glass spray chamber (§3.2)",
  "ada:analysisInclusionAndRejectionCriteria": "Partially -- number of replicate analyses stated per ratio (n = 120, 88, 32, 70, 50). No acceptance or rejection rule stated",
  "ada:combinedResults": "each element/Ca ratio of the consistency standards, over its replicates (n = 120, 88, 32, 70, 50) — Tables 2 and 3",
  "ada:detectionLimit": "Li/Ca: 0.5; B/Ca: 15; Mg/Ca: 0.03; Al/Ca: 0.05; Mn/Ca: 0.3; Zn/Ca: 0.05; Sr/Ca: 0.02; Cd/Ca: 0.005; U/Ca: 0.5 — in the units of the ratio (Table 2)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "all [Li/Ca: 2.42%; B/Ca: 4.17%; Mg/Ca: 1.39%; Al/Ca: 14.06%; Mn/Ca: 0.93%; Zn/Ca: 2.83% (1.2–7.8), 5.05% (0.5–1.2); Sr/Ca: 0.92%; Cd/Ca: 2.37% (0.07–0.24), 4.80% (0.01–0.07); U/Ca: 2.54%] — RSD of external standards over three months, n = 120 except Zn/Ca 88 and 32, Cd/Ca 50 and 70 (Table 2, §3.6)",
  "ada:analyticalAccuracyAndAssessmentMethod": "all [Li/Ca: 0.39%; B/Ca: 2.57%; Mg/Ca: 0.61%; Al/Ca: 9.30%; Mn/Ca: 0.23%; Zn/Ca: 0.82% (1.2–7.8), 1.69% (0.5–1.2); Sr/Ca: 0.34%; Cd/Ca: 0.93% (0.07–0.24), 0.80% (0.01–0.07); U/Ca: 1.09%] — Acc.% = (average measured − true)/true × 100 on external standards (Table 2)",
  "ada:goodnessOfFitOrDispersionStatistic": "all: RSD% = SD of measurements / average ratio × 100 — table notes"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-Q-ICPMS/detail/context.jsonld",
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
      "@id": "ex:solutionQicpmsTAPP-P1",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "N -- \"a typical run (~5 hr)\" referenced; no run identifier stated",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Partially -- sample type named (\"core top Cibicidoides wuellerstorfi from the north Atlantic Ocean\"); no individual sample identifiers stated in the methods",
  "ada:samplingUnitName": "N \u2014 only the sample type is named (core-top Cibicidoides wuellerstorfi); no sample or aliquot identifiers are stated",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": 6,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "Li, Mg, Sr: <1%; Cd: <2%; Zn: <4%; U: <5%; B: 5%; other: N \u2014 relative to typical foraminiferal ratios; Ca also <1%; B was 30% with a glass spray chamber (\u00a73.2)",
  "ada:analysisInclusionAndRejectionCriteria": "Partially -- number of replicate analyses stated per ratio (n = 120, 88, 32, 70, 50). No acceptance or rejection rule stated",
  "ada:combinedResults": "each element/Ca ratio of the consistency standards, over its replicates (n = 120, 88, 32, 70, 50) \u2014 Tables 2 and 3",
  "ada:detectionLimit": "Li/Ca: 0.5; B/Ca: 15; Mg/Ca: 0.03; Al/Ca: 0.05; Mn/Ca: 0.3; Zn/Ca: 0.05; Sr/Ca: 0.02; Cd/Ca: 0.005; U/Ca: 0.5 \u2014 in the units of the ratio (Table 2)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "all [Li/Ca: 2.42%; B/Ca: 4.17%; Mg/Ca: 1.39%; Al/Ca: 14.06%; Mn/Ca: 0.93%; Zn/Ca: 2.83% (1.2\u20137.8), 5.05% (0.5\u20131.2); Sr/Ca: 0.92%; Cd/Ca: 2.37% (0.07\u20130.24), 4.80% (0.01\u20130.07); U/Ca: 2.54%] \u2014 RSD of external standards over three months, n = 120 except Zn/Ca 88 and 32, Cd/Ca 50 and 70 (Table 2, \u00a73.6)",
  "ada:analyticalAccuracyAndAssessmentMethod": "all [Li/Ca: 0.39%; B/Ca: 2.57%; Mg/Ca: 0.61%; Al/Ca: 9.30%; Mn/Ca: 0.23%; Zn/Ca: 0.82% (1.2\u20137.8), 1.69% (0.5\u20131.2); Sr/Ca: 0.34%; Cd/Ca: 0.93% (0.07\u20130.24), 0.80% (0.01\u20130.07); U/Ca: 1.09%] \u2014 Acc.% = (average measured \u2212 true)/true \u00d7 100 on external standards (Table 2)",
  "ada:goodnessOfFitOrDispersionStatistic": "all: RSD% = SD of measurements / average ratio \u00d7 100 \u2014 table notes"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-P1> a ada:SolutionICPMSTabular ;
    schema1:measurementTechnique <ex:solutionQicpmsTAPP-P1> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially -- number of replicate analyses stated per ratio (n = 120, 88, 32, 70, 50). No acceptance or rejection rule stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "all [Li/Ca: 0.39%; B/Ca: 2.57%; Mg/Ca: 0.61%; Al/Ca: 9.30%; Mn/Ca: 0.23%; Zn/Ca: 0.82% (1.2–7.8), 1.69% (0.5–1.2); Sr/Ca: 0.34%; Cd/Ca: 0.93% (0.07–0.24), 0.80% (0.01–0.07); U/Ca: 1.09%] — Acc.% = (average measured − true)/true × 100 on external standards (Table 2)" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "all [Li/Ca: 2.42%; B/Ca: 4.17%; Mg/Ca: 1.39%; Al/Ca: 14.06%; Mn/Ca: 0.93%; Zn/Ca: 2.83% (1.2–7.8), 5.05% (0.5–1.2); Sr/Ca: 0.92%; Cd/Ca: 2.37% (0.07–0.24), 4.80% (0.01–0.07); U/Ca: 2.54%] — RSD of external standards over three months, n = 120 except Zn/Ca 88 and 32, Cd/Ca 50 and 70 (Table 2, §3.6)" ;
    ada:combinedResults "each element/Ca ratio of the consistency standards, over its replicates (n = 120, 88, 32, 70, 50) — Tables 2 and 3" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "Li/Ca: 0.5; B/Ca: 15; Mg/Ca: 0.03; Al/Ca: 0.05; Mn/Ca: 0.3; Zn/Ca: 0.05; Sr/Ca: 0.02; Cd/Ca: 0.005; U/Ca: 0.5 — in the units of the ratio (Table 2)" ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "all: RSD% = SD of measurements / average ratio × 100 — table notes" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:numberOfReplicates 6 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "Li, Mg, Sr: <1%; Cd: <2%; Zn: <4%; U: <5%; B: 5%; other: N — relative to typical foraminiferal ratios; Ca also <1%; B was 30% with a glass spray chamber (§3.2)" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "Partially -- sample type named (\"core top Cibicidoides wuellerstorfi from the north Atlantic Ocean\"); no individual sample identifiers stated in the methods" ;
    ada:samplingUnitName "N — only the sample type is named (core-top Cibicidoides wuellerstorfi); no sample or aliquot identifiers are stated" ;
    ada:sessionIdentifier "N -- \"a typical run (~5 hr)\" referenced; no run identifier stated" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<ex:solutionQicpmsTAPP-P1> schema1:identifier "missing" .


```


### detail example Agilent7500
detail instance derived from Makishima+etal2011 | Agilent 7500cs | PML Okayama.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Agilent7500",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionQicpmsTAPP-Agilent7500",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "N -- \"an average of eight sessions\" referenced; no session identifier stated",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1; NIST SRM 610, 612, 614, 616 glasses",
  "ada:samplingUnitName": "Labelled for the meteorites: \"Orgueil #1\", \"Orgueil #2\", \"Murchison #1\", \"Murchison #2\", \"Allende #1\", \"Allende #2\" (table, p.9) — \"Two powder aliquots were used for each meteorite\" (p.9); geostandards by name only",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "Cd: 16 pg; In: <0.2 pg; Tl: 4 pg; Bi: 3 pg — total dissolution blanks, similar for the ultrasonic and bomb digestions, n = 4 (Table 1)",
  "ada:analysisInclusionAndRejectionCriteria": "Partially -- n = 5 (evaporation test), n = 4 (dissolution blanks), \"an average of eight sessions\" for detection limits. No acceptance or rejection rule for individual results is stated. The 113Cd decision is a mass-selection decision, not an aggregation one, and is recorded under Monitored Masses",
  "ada:combinedResults": "evaporation-test ratios (n = 5); detection limits (average of eight sessions) — Tables 1 and 2",
  "ada:detectionLimit": "Cd: 0.8; In: 0.2; Tl: 0.9; Bi: 0.2 — 3s, in pg/ml in solution and in ng/g in silicates at DF 1000 (Table 1)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "all [Cd: 2.0%; In, Tl, Bi: 1.6%] — RPD of X/¹⁴⁹Sm between neighbouring calibrator runs (Table 1)",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "JB-2, JB-3, JA-1, JA-2, JA-3, BHVO-1, AGV-1 [Cd: 3–10%]; JP-1, PCC-1, DTS-1 [Cd: 7–16%]; NIST SRM 610, NIST SRM 612, NIST SRM 614, NIST SRM 616 [Cd: 2–3%; In: 0.7–3%; Tl: 6–12%; Bi: 1–4%] — intermediate precision, RSD of n = 4–8 separate decompositions (Tables 3 and 4)",
  "ada:analyticalAccuracyAndAssessmentMethod": "JB-2, JB-3, JA-1, JA-2, JA-3 [Cd: broadly similar to the reference values of Govindaraju (1994) and Imai et al. (1995)]; BHVO-1, AGV-1 [Cd: differ from those reference values] — Table 3; In, Tl and Bi compared with previous studies",
  "ada:goodnessOfFitOrDispersionStatistic": "all: RSD — 'The normalised ratios after evaporation together with the RSD (n = 5)'"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-Q-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Agilent7500",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionQicpmsTAPP-Agilent7500",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "N -- \"an average of eight sessions\" referenced; no session identifier stated",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1; NIST SRM 610, 612, 614, 616 glasses",
  "ada:samplingUnitName": "Labelled for the meteorites: \"Orgueil #1\", \"Orgueil #2\", \"Murchison #1\", \"Murchison #2\", \"Allende #1\", \"Allende #2\" (table, p.9) \u2014 \"Two powder aliquots were used for each meteorite\" (p.9); geostandards by name only",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "Cd: 16 pg; In: <0.2 pg; Tl: 4 pg; Bi: 3 pg \u2014 total dissolution blanks, similar for the ultrasonic and bomb digestions, n = 4 (Table 1)",
  "ada:analysisInclusionAndRejectionCriteria": "Partially -- n = 5 (evaporation test), n = 4 (dissolution blanks), \"an average of eight sessions\" for detection limits. No acceptance or rejection rule for individual results is stated. The 113Cd decision is a mass-selection decision, not an aggregation one, and is recorded under Monitored Masses",
  "ada:combinedResults": "evaporation-test ratios (n = 5); detection limits (average of eight sessions) \u2014 Tables 1 and 2",
  "ada:detectionLimit": "Cd: 0.8; In: 0.2; Tl: 0.9; Bi: 0.2 \u2014 3s, in pg/ml in solution and in ng/g in silicates at DF 1000 (Table 1)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "all [Cd: 2.0%; In, Tl, Bi: 1.6%] \u2014 RPD of X/\u00b9\u2074\u2079Sm between neighbouring calibrator runs (Table 1)",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "JB-2, JB-3, JA-1, JA-2, JA-3, BHVO-1, AGV-1 [Cd: 3\u201310%]; JP-1, PCC-1, DTS-1 [Cd: 7\u201316%]; NIST SRM 610, NIST SRM 612, NIST SRM 614, NIST SRM 616 [Cd: 2\u20133%; In: 0.7\u20133%; Tl: 6\u201312%; Bi: 1\u20134%] \u2014 intermediate precision, RSD of n = 4\u20138 separate decompositions (Tables 3 and 4)",
  "ada:analyticalAccuracyAndAssessmentMethod": "JB-2, JB-3, JA-1, JA-2, JA-3 [Cd: broadly similar to the reference values of Govindaraju (1994) and Imai et al. (1995)]; BHVO-1, AGV-1 [Cd: differ from those reference values] \u2014 Table 3; In, Tl and Bi compared with previous studies",
  "ada:goodnessOfFitOrDispersionStatistic": "all: RSD \u2014 'The normalised ratios after evaporation together with the RSD (n = 5)'"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Agilent7500> a ada:SolutionICPMSTabular ;
    schema1:measurementTechnique <ex:solutionQicpmsTAPP-Agilent7500> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially -- n = 5 (evaporation test), n = 4 (dissolution blanks), \"an average of eight sessions\" for detection limits. No acceptance or rejection rule for individual results is stated. The 113Cd decision is a mass-selection decision, not an aggregation one, and is recorded under Monitored Masses" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "JB-2, JB-3, JA-1, JA-2, JA-3 [Cd: broadly similar to the reference values of Govindaraju (1994) and Imai et al. (1995)]; BHVO-1, AGV-1 [Cd: differ from those reference values] — Table 3; In, Tl and Bi compared with previous studies" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "JB-2, JB-3, JA-1, JA-2, JA-3, BHVO-1, AGV-1 [Cd: 3–10%]; JP-1, PCC-1, DTS-1 [Cd: 7–16%]; NIST SRM 610, NIST SRM 612, NIST SRM 614, NIST SRM 616 [Cd: 2–3%; In: 0.7–3%; Tl: 6–12%; Bi: 1–4%] — intermediate precision, RSD of n = 4–8 separate decompositions (Tables 3 and 4)" ;
    ada:combinedResults "evaporation-test ratios (n = 5); detection limits (average of eight sessions) — Tables 1 and 2" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "Cd: 0.8; In: 0.2; Tl: 0.9; Bi: 0.2 — 3s, in pg/ml in solution and in ng/g in silicates at DF 1000 (Table 1)" ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "all: RSD — 'The normalised ratios after evaporation together with the RSD (n = 5)'" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "Cd: 16 pg; In: <0.2 pg; Tl: 4 pg; Bi: 3 pg — total dissolution blanks, similar for the ultrasonic and bomb digestions, n = 4 (Table 1)" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1; NIST SRM 610, 612, 614, 616 glasses" ;
    ada:samplingUnitName "Labelled for the meteorites: \"Orgueil #1\", \"Orgueil #2\", \"Murchison #1\", \"Murchison #2\", \"Allende #1\", \"Allende #2\" (table, p.9) — \"Two powder aliquots were used for each meteorite\" (p.9); geostandards by name only" ;
    ada:sessionIdentifier "N -- \"an average of eight sessions\" referenced; no session identifier stated" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "all [Cd: 2.0%; In, Tl, Bi: 1.6%] — RPD of X/¹⁴⁹Sm between neighbouring calibrator runs (Table 1)" .

<ex:solutionQicpmsTAPP-Agilent7500> schema1:identifier "missing" .


```


### detail example Agilent7900
detail instance derived from Long+etal2025 | Agilent 7900 | IPGP France.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Agilent7900",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionQicpmsTAPP-Agilent7900",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "PCA 02010, B-7904, LON 94101 and further CM/CY chondrites",
  "ada:samplingUnitName": "Sample name only — meteorites by name (e.g. PCA 02010, PCA 02012); PCA 02010's \"Two separate fragments\" are distinguished by their values, not by labels (p.2)",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-Q-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Agilent7900",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionQicpmsTAPP-Agilent7900",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "PCA 02010, B-7904, LON 94101 and further CM/CY chondrites",
  "ada:samplingUnitName": "Sample name only \u2014 meteorites by name (e.g. PCA 02010, PCA 02012); PCA 02010's \"Two separate fragments\" are distinguished by their values, not by labels (p.2)",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Agilent7900> a ada:SolutionICPMSTabular ;
    schema1:measurementTechnique <ex:solutionQicpmsTAPP-Agilent7900> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "missing" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:combinedResults "missing" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "PCA 02010, B-7904, LON 94101 and further CM/CY chondrites" ;
    ada:samplingUnitName "Sample name only — meteorites by name (e.g. PCA 02010, PCA 02012); PCA 02010's \"Two separate fragments\" are distinguished by their values, not by labels (p.2)" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<ex:solutionQicpmsTAPP-Agilent7900> schema1:identifier "missing" .


```


### detail example Agilent7500-2
detail instance derived from Lu+etal2007 | Agilent 7500cs | PML Okayama.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Agilent7500-2",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionQicpmsTAPP-Agilent7500-2",
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
  "ada:proceduralBlankLevel": "B: 13–185 pg (ultrasonic); Zr: 0.9–29, 55; Nb: 2–5, 3; Mo: 0.2–10, ~134; Sn: ~323, ~276; Sb: 0.7–9, ~60; Hf: <12, <8; Ta: 0.6–7, 0.6–2 — total procedural blank in pg, ultrasonic then bomb method (Table 4)",
  "ada:analysisInclusionAndRejectionCriteria": "Partially -- \"Orgueil and Allende were analyzed 4 times and twice from the sample digestion, respectively. ... As the sample amounts used were small, and the carbonaceous chondrites are heterogeneous, analytical results for each run are shown in the table\" alongside the averages. No acceptance or rejection rule stated",
  "ada:combinedResults": "Orgueil average (4 runs); Allende average (2 runs); bomb-method yields (average of two tests) — Tables 3 and 5",
  "ada:detectionLimit": "B: 45 (10B), 11 (11B); Zr: 13 (90Zr), 43 (91Zr); Nb: 1; Mo: 2 (95Mo), 14 (97Mo); Sn: 3 (118Sn), 5 (119Sn); Sb: 2 (121Sb), 0.7 (123Sb); Hf: 0.7 (178Hf), 1 (179Hf); Ta: 0.3 — ng/g in rock, 3σ (Table 2a); in solution, in pg/g",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "B: 2.4% (11B/10B); Zr: 3.2% (91Zr/90Zr); Nb: 3.1% (93Nb/91Zr), 0.8% (93Nb/97Mo); Mo: 1.0% (97Mo/95Mo); Sn: 0.7% (119Sn/118Sn); Sb: 0.6% (121Sb/123Sb); Hf: 0.5% (179Hf/178Hf); Ta: 2.4% (181Ta/97Mo), 0.5% (181Ta/179Hf) — RSD% of each ratio measurement, ranges in Table 2a",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1 [all: average reproducibility 1.0–4.6% RSD] — §3.7, Tables 5–6; Mo in JB-1 (15%) excluded as heterogeneous",
  "ada:analyticalAccuracyAndAssessmentMethod": "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1 [all: compared with reference values (Govindaraju 1994, Imai et al. 1995 and others)] — Tables 5–6; 'a significant difference exists for B in JA-2'",
  "ada:goodnessOfFitOrDispersionStatistic": "all: RSD% — Tables 5 and 6; 'Averages of the reproducibility (RSD %)'"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-Q-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Agilent7500-2",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionQicpmsTAPP-Agilent7500-2",
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
  "ada:proceduralBlankLevel": "B: 13\u2013185 pg (ultrasonic); Zr: 0.9\u201329, 55; Nb: 2\u20135, 3; Mo: 0.2\u201310, ~134; Sn: ~323, ~276; Sb: 0.7\u20139, ~60; Hf: <12, <8; Ta: 0.6\u20137, 0.6\u20132 \u2014 total procedural blank in pg, ultrasonic then bomb method (Table 4)",
  "ada:analysisInclusionAndRejectionCriteria": "Partially -- \"Orgueil and Allende were analyzed 4 times and twice from the sample digestion, respectively. ... As the sample amounts used were small, and the carbonaceous chondrites are heterogeneous, analytical results for each run are shown in the table\" alongside the averages. No acceptance or rejection rule stated",
  "ada:combinedResults": "Orgueil average (4 runs); Allende average (2 runs); bomb-method yields (average of two tests) \u2014 Tables 3 and 5",
  "ada:detectionLimit": "B: 45 (10B), 11 (11B); Zr: 13 (90Zr), 43 (91Zr); Nb: 1; Mo: 2 (95Mo), 14 (97Mo); Sn: 3 (118Sn), 5 (119Sn); Sb: 2 (121Sb), 0.7 (123Sb); Hf: 0.7 (178Hf), 1 (179Hf); Ta: 0.3 \u2014 ng/g in rock, 3\u03c3 (Table 2a); in solution, in pg/g",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "B: 2.4% (11B/10B); Zr: 3.2% (91Zr/90Zr); Nb: 3.1% (93Nb/91Zr), 0.8% (93Nb/97Mo); Mo: 1.0% (97Mo/95Mo); Sn: 0.7% (119Sn/118Sn); Sb: 0.6% (121Sb/123Sb); Hf: 0.5% (179Hf/178Hf); Ta: 2.4% (181Ta/97Mo), 0.5% (181Ta/179Hf) \u2014 RSD% of each ratio measurement, ranges in Table 2a",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1 [all: average reproducibility 1.0\u20134.6% RSD] \u2014 \u00a73.7, Tables 5\u20136; Mo in JB-1 (15%) excluded as heterogeneous",
  "ada:analyticalAccuracyAndAssessmentMethod": "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1 [all: compared with reference values (Govindaraju 1994, Imai et al. 1995 and others)] \u2014 Tables 5\u20136; 'a significant difference exists for B in JA-2'",
  "ada:goodnessOfFitOrDispersionStatistic": "all: RSD% \u2014 Tables 5 and 6; 'Averages of the reproducibility (RSD %)'"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Agilent7500-2> a ada:SolutionICPMSTabular ;
    schema1:measurementTechnique <ex:solutionQicpmsTAPP-Agilent7500-2> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially -- \"Orgueil and Allende were analyzed 4 times and twice from the sample digestion, respectively. ... As the sample amounts used were small, and the carbonaceous chondrites are heterogeneous, analytical results for each run are shown in the table\" alongside the averages. No acceptance or rejection rule stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1 [all: compared with reference values (Govindaraju 1994, Imai et al. 1995 and others)] — Tables 5–6; 'a significant difference exists for B in JA-2'" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1 [all: average reproducibility 1.0–4.6% RSD] — §3.7, Tables 5–6; Mo in JB-1 (15%) excluded as heterogeneous" ;
    ada:combinedResults "Orgueil average (4 runs); Allende average (2 runs); bomb-method yields (average of two tests) — Tables 3 and 5" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "B: 45 (10B), 11 (11B); Zr: 13 (90Zr), 43 (91Zr); Nb: 1; Mo: 2 (95Mo), 14 (97Mo); Sn: 3 (118Sn), 5 (119Sn); Sb: 2 (121Sb), 0.7 (123Sb); Hf: 0.7 (178Hf), 1 (179Hf); Ta: 0.3 — ng/g in rock, 3σ (Table 2a); in solution, in pg/g" ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "all: RSD% — Tables 5 and 6; 'Averages of the reproducibility (RSD %)'" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "B: 2.4% (11B/10B); Zr: 3.2% (91Zr/90Zr); Nb: 3.1% (93Nb/91Zr), 0.8% (93Nb/97Mo); Mo: 1.0% (97Mo/95Mo); Sn: 0.7% (119Sn/118Sn); Sb: 0.6% (121Sb/123Sb); Hf: 0.5% (179Hf/178Hf); Ta: 2.4% (181Ta/97Mo), 0.5% (181Ta/179Hf) — RSD% of each ratio measurement, ranges in Table 2a" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "B: 13–185 pg (ultrasonic); Zr: 0.9–29, 55; Nb: 2–5, 3; Mo: 0.2–10, ~134; Sn: ~323, ~276; Sb: 0.7–9, ~60; Hf: <12, <8; Ta: 0.6–7, 0.6–2 — total procedural blank in pg, ultrasonic then bomb method (Table 4)" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1 (GSJ); BHVO-1, AGV-1, PCC-1, DTS-1 (USGS); Ivuna (CI1), Orgueil (CI1), Cold Bokkeveld (CM2), Allende (USNM 3529, Split 1, Pos. 23)" ;
    ada:samplingUnitName "Sample name only, except the Allende powder: \"the Smithsonian reference Allende powder (USNM 3529, Split 1, Pos. 23)\" (p.5). Solutions \"#1\"–\"#8\" (p.7) are synthetic yield-test solutions, not samples" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<ex:solutionQicpmsTAPP-Agilent7500-2> schema1:identifier "missing" .


```


### detail example Agilent8800
detail instance derived from GilDiaz+etal2020 | Agilent 8800 QQQ | FHNW Basel.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Agilent8800",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionQicpmsTAPP-Agilent8800",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "N — SPM isotherm experiment at 1000 mg/L",
  "ada:samplingUnitName": "N — the sorption-isotherm solutions carry no sample or unit identifiers",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:combinedResults": "NCS 73307 recovery (N = 3)",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "NCS 73307 [Te: 94 ± 17% recovery (N = 3); Se: 70–134% recovery (N = 3)] — §2.3, §2.4",
  "ada:goodnessOfFitOrDispersionStatistic": "all: SD — 'mean ± SD recovery values of 94 ± 17% (N = 3)'"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-Q-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Agilent8800",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionQicpmsTAPP-Agilent8800",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "N \u2014 SPM isotherm experiment at 1000 mg/L",
  "ada:samplingUnitName": "N \u2014 the sorption-isotherm solutions carry no sample or unit identifiers",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:combinedResults": "NCS 73307 recovery (N = 3)",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "NCS 73307 [Te: 94 \u00b1 17% recovery (N = 3); Se: 70\u2013134% recovery (N = 3)] \u2014 \u00a72.3, \u00a72.4",
  "ada:goodnessOfFitOrDispersionStatistic": "all: SD \u2014 'mean \u00b1 SD recovery values of 94 \u00b1 17% (N = 3)'"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Agilent8800> a ada:SolutionICPMSTabular ;
    schema1:measurementTechnique <ex:solutionQicpmsTAPP-Agilent8800> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "NCS 73307 [Te: 94 ± 17% recovery (N = 3); Se: 70–134% recovery (N = 3)] — §2.3, §2.4" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:combinedResults "NCS 73307 recovery (N = 3)" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "all: SD — 'mean ± SD recovery values of 94 ± 17% (N = 3)'" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "N — SPM isotherm experiment at 1000 mg/L" ;
    ada:samplingUnitName "N — the sorption-isotherm solutions carry no sample or unit identifiers" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<ex:solutionQicpmsTAPP-Agilent8800> schema1:identifier "missing" .


```


### detail example P6
detail instance derived from GilDiaz+etal2020 | Thermo iCAP-TQ | lab not stated.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-P6",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionQicpmsTAPP-P6",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Selective extraction fractions F1-F4 and F4N; CRM NCS 73307",
  "ada:samplingUnitName": "Labelled by extraction: fractions \"F1\", \"F2\", \"F3\", \"F4\" and \"F4N\" of the equilibrated sediment, \"two replicates per extraction mode\" (p.2); replicates not labelled",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "Te: ~35 µg/L in the F3 extraction blanks; other: N — three blanks of each extraction; the F3 contamination is attributed to the H2O2 or ammonium acetate (§2.2)",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": "Te: 0.1 ng/L; other: N — N = 10; natural Te in the extractions 5-fold (F2) to 200-fold (F4) above the LOD",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "NIST 1643f [Te: 95 ± 5% (KED), 89 ± 10% (O2), N = 5; Se: 95 ± 3%]; NCS 73307 [Te: 99 ± 14% (KED), 70 ± 19% (O2), N = 4]; NIST 1640a [Se: 85 ± 2%] — recoveries (§2.3, §2.4)",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-Q-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-P6",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionQicpmsTAPP-P6",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Selective extraction fractions F1-F4 and F4N; CRM NCS 73307",
  "ada:samplingUnitName": "Labelled by extraction: fractions \"F1\", \"F2\", \"F3\", \"F4\" and \"F4N\" of the equilibrated sediment, \"two replicates per extraction mode\" (p.2); replicates not labelled",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "Te: ~35 \u00b5g/L in the F3 extraction blanks; other: N \u2014 three blanks of each extraction; the F3 contamination is attributed to the H2O2 or ammonium acetate (\u00a72.2)",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": "Te: 0.1 ng/L; other: N \u2014 N = 10; natural Te in the extractions 5-fold (F2) to 200-fold (F4) above the LOD",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "NIST 1643f [Te: 95 \u00b1 5% (KED), 89 \u00b1 10% (O2), N = 5; Se: 95 \u00b1 3%]; NCS 73307 [Te: 99 \u00b1 14% (KED), 70 \u00b1 19% (O2), N = 4]; NIST 1640a [Se: 85 \u00b1 2%] \u2014 recoveries (\u00a72.3, \u00a72.4)",
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-P6> a ada:SolutionICPMSTabular ;
    schema1:measurementTechnique <ex:solutionQicpmsTAPP-P6> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "NIST 1643f [Te: 95 ± 5% (KED), 89 ± 10% (O2), N = 5; Se: 95 ± 3%]; NCS 73307 [Te: 99 ± 14% (KED), 70 ± 19% (O2), N = 4]; NIST 1640a [Se: 85 ± 2%] — recoveries (§2.3, §2.4)" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:combinedResults "missing" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "Te: 0.1 ng/L; other: N — N = 10; natural Te in the extractions 5-fold (F2) to 200-fold (F4) above the LOD" ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "Te: ~35 µg/L in the F3 extraction blanks; other: N — three blanks of each extraction; the F3 contamination is attributed to the H2O2 or ammonium acetate (§2.2)" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "Selective extraction fractions F1-F4 and F4N; CRM NCS 73307" ;
    ada:samplingUnitName "Labelled by extraction: fractions \"F1\", \"F2\", \"F3\", \"F4\" and \"F4N\" of the equilibrated sediment, \"two replicates per extraction mode\" (p.2); replicates not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<ex:solutionQicpmsTAPP-P6> schema1:identifier "missing" .


```


### detail example P7
detail instance derived from GilDiaz+etal2020 | Thermo XSeries 2 | KIT Karlsruhe.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-P7",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionQicpmsTAPP-P7",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "N — sorption kinetics and isotherm solutions; CRMs CRM-TMDW and NIST 1643f",
  "ada:samplingUnitName": "N — the sorption-kinetics and isotherm solutions carry no sample or unit identifiers",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:combinedResults": "Se sorption at each sampling time and condition (N = 3); sorption isotherm points (N = 2) — Fig. 2",
  "ada:detectionLimit": "Te: 0.01 µg/L; Se: 0.06 µg/L — N = 10 (§2.3, §2.4)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "CRM-TMDW [Se: 98–106% recovery (N = 16)]; NIST 1643f [Se: 100–102% (N = 16); Te: 85–91% (N = 4)] — §2.3, §2.4",
  "ada:goodnessOfFitOrDispersionStatistic": "Te, Se: SD — Figs 1–2"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-Q-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-P7",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionQicpmsTAPP-P7",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "N \u2014 sorption kinetics and isotherm solutions; CRMs CRM-TMDW and NIST 1643f",
  "ada:samplingUnitName": "N \u2014 the sorption-kinetics and isotherm solutions carry no sample or unit identifiers",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:combinedResults": "Se sorption at each sampling time and condition (N = 3); sorption isotherm points (N = 2) \u2014 Fig. 2",
  "ada:detectionLimit": "Te: 0.01 \u00b5g/L; Se: 0.06 \u00b5g/L \u2014 N = 10 (\u00a72.3, \u00a72.4)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "CRM-TMDW [Se: 98\u2013106% recovery (N = 16)]; NIST 1643f [Se: 100\u2013102% (N = 16); Te: 85\u201391% (N = 4)] \u2014 \u00a72.3, \u00a72.4",
  "ada:goodnessOfFitOrDispersionStatistic": "Te, Se: SD \u2014 Figs 1\u20132"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-P7> a ada:SolutionICPMSTabular ;
    schema1:measurementTechnique <ex:solutionQicpmsTAPP-P7> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "CRM-TMDW [Se: 98–106% recovery (N = 16)]; NIST 1643f [Se: 100–102% (N = 16); Te: 85–91% (N = 4)] — §2.3, §2.4" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:combinedResults "Se sorption at each sampling time and condition (N = 3); sorption isotherm points (N = 2) — Fig. 2" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "Te: 0.01 µg/L; Se: 0.06 µg/L — N = 10 (§2.3, §2.4)" ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "Te, Se: SD — Figs 1–2" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "N — sorption kinetics and isotherm solutions; CRMs CRM-TMDW and NIST 1643f" ;
    ada:samplingUnitName "N — the sorption-kinetics and isotherm solutions carry no sample or unit identifiers" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<ex:solutionQicpmsTAPP-P7> schema1:identifier "missing" .


```


### detail example P8
detail instance derived from LopezGarcia+etal2026 | Thermo iCAP TQ | Institute of Science Tokyo.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-P8",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionQicpmsTAPP-P8",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Ryugu particles A0066, A0238, A0247, A0256, A0259, A0268, A0301, A0313; Smithsonian Allende powder",
  "ada:samplingUnitName": "Sample name only — each Ryugu particle was \"individually weighed\" and digested whole, so it is its own unit: \"A0066, A0238, A0247, A0256, A0259, A0268, A0301, and A0313\" (p.3)",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "N — blank data stated to be in the supplementary material; Ta and W blank contributions exceeded 30%",
  "ada:analysisInclusionAndRejectionCriteria": "N — no rule for admitting or rejecting individual results is stated. The exclusion of Ta and W is a decision about which elements are reported, not about which results enter an aggregate, and is recorded under Reported Variables and Units",
  "ada:combinedResults": "Allende replicate average (n = 5); average of the eight Ryugu particles — supplementary data; Fig. 2",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "N — the Allende replicate averages and uncertainties are in the supplementary materials",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-Q-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-P8",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionQicpmsTAPP-P8",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Ryugu particles A0066, A0238, A0247, A0256, A0259, A0268, A0301, A0313; Smithsonian Allende powder",
  "ada:samplingUnitName": "Sample name only \u2014 each Ryugu particle was \"individually weighed\" and digested whole, so it is its own unit: \"A0066, A0238, A0247, A0256, A0259, A0268, A0301, and A0313\" (p.3)",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "N \u2014 blank data stated to be in the supplementary material; Ta and W blank contributions exceeded 30%",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 no rule for admitting or rejecting individual results is stated. The exclusion of Ta and W is a decision about which elements are reported, not about which results enter an aggregate, and is recorded under Reported Variables and Units",
  "ada:combinedResults": "Allende replicate average (n = 5); average of the eight Ryugu particles \u2014 supplementary data; Fig. 2",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "N \u2014 the Allende replicate averages and uncertainties are in the supplementary materials",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-P8> a ada:SolutionICPMSTabular ;
    schema1:measurementTechnique <ex:solutionQicpmsTAPP-P8> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — no rule for admitting or rejecting individual results is stated. The exclusion of Ta and W is a decision about which elements are reported, not about which results enter an aggregate, and is recorded under Reported Variables and Units" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "missing" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "N — the Allende replicate averages and uncertainties are in the supplementary materials" ;
    ada:combinedResults "Allende replicate average (n = 5); average of the eight Ryugu particles — supplementary data; Fig. 2" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "N — blank data stated to be in the supplementary material; Ta and W blank contributions exceeded 30%" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "Ryugu particles A0066, A0238, A0247, A0256, A0259, A0268, A0301, A0313; Smithsonian Allende powder" ;
    ada:samplingUnitName "Sample name only — each Ryugu particle was \"individually weighed\" and digested whole, so it is its own unit: \"A0066, A0238, A0247, A0256, A0259, A0268, A0301, and A0313\" (p.3)" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<ex:solutionQicpmsTAPP-P8> schema1:identifier "missing" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Solution Q-ICP-MS Analysis Detail
description: Dataset-level analysis-instance detail for solution Q-ICP-MS, reusing
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
                  - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/WorkflowStep
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
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Analysis_digestionTemperature
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Analysis_digestionDuration
                          allOf:
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Analysis_digestionTemperature
                            minContains: 0
                            maxContains: 1
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Analysis_digestionDuration
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
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_filteringApproach
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/singleCollector/schema.yaml#/$defs/Param_Analysis_pulseAnalogDetectorNonlinearityCorrection
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Analysis_constantsReferenceValues
                          allOf:
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_filteringApproach
                            minContains: 0
                            maxContains: 1
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/singleCollector/schema.yaml#/$defs/Param_Analysis_pulseAnalogDetectorNonlinearityCorrection
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
                                              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Analysis_sampleUptakeRate
                                              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Analysis_nebulizerGasFlowRate
                                              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_makeUpGasAndFlowRate
                                            allOf:
                                            - contains:
                                                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Analysis_sampleUptakeRate
                                              minContains: 0
                                              maxContains: 1
                                            - contains:
                                                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Analysis_nebulizerGasFlowRate
                                              minContains: 0
                                              maxContains: 1
                                            - contains:
                                                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_makeUpGasAndFlowRate
                                              minContains: 0
                                              maxContains: 1
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
                                              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_rfPower
                                              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_coolantPlasmaGasFlowRate
                                              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_auxiliaryGasFlowRate
                                            allOf:
                                            - contains:
                                                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_rfPower
                                              minContains: 0
                                              maxContains: 1
                                            - contains:
                                                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_coolantPlasmaGasFlowRate
                                              minContains: 0
                                              maxContains: 1
                                            - contains:
                                                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_auxiliaryGasFlowRate
                                              minContains: 0
                                              maxContains: 1
                                    - if:
                                        properties:
                                          schema:additionalType:
                                            contains:
                                              const: Collision Reaction Cell
                                            schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                                        required:
                                        - schema:additionalType
                                      then:
                                        properties:
                                          schema:additionalProperty:
                                            type: array
                                            items:
                                              anyOf:
                                              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/collisionCell/schema.yaml#/$defs/Param_Analysis_gasFlowRate
                                              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/collisionCell/schema.yaml#/$defs/Param_Analysis_cellExitDiscriminationVoltage
                                              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/collisionCell/schema.yaml#/$defs/Param_Analysis_reactionGasFlowRate
                                            allOf:
                                            - contains:
                                                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/collisionCell/schema.yaml#/$defs/Param_Analysis_gasFlowRate
                                              minContains: 0
                                              maxContains: 1
                                            - contains:
                                                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/collisionCell/schema.yaml#/$defs/Param_Analysis_cellExitDiscriminationVoltage
                                              minContains: 0
                                              maxContains: 1
                                            - contains:
                                                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/collisionCell/schema.yaml#/$defs/Param_Analysis_reactionGasFlowRate
                                              minContains: 0
                                              maxContains: 1
                                  allOf:
                                  - contains:
                                      properties:
                                        schema:additionalType:
                                          contains:
                                            const: Sample Introduction System
                                          schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                                      required:
                                      - schema:additionalType
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
                                            const: Collision Reaction Cell
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
                                          const: ada:parameter/solutionQicpmsTAPP/doublyChargedSpeciesMonitor
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/solutionQicpmsTAPP/doublyChargedSpeciesMonitor
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
                                          const: ada:parameter/solutionQicpmsTAPP/doublyChargedSpeciesProduction
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/solutionQicpmsTAPP/doublyChargedSpeciesProduction
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
                                          const: ada:parameter/solutionQicpmsTAPP/doublyChargedSpeciesMonitor
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/solutionQicpmsTAPP/doublyChargedSpeciesMonitor
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
                                          const: ada:parameter/solutionQicpmsTAPP/doublyChargedSpeciesProduction
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/solutionQicpmsTAPP/doublyChargedSpeciesProduction
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
          schema:additionalProperty:
            type: array
            items:
              anyOf:
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_signalIntegrationTime
              - title: Collision/Reaction Gas Mixture Ratio
                description: Where the collision or reaction cell is supplied with
                  a mixture of gases rather than a single gas, the identities and
                  proportions of that mixture. Recorded separately from the gas identity.
                  Record 'N/A' where a single gas is used.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/solutionQicpmsTAPP/collisionReactionGasMixtureRatio
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/solutionQicpmsTAPP/collisionReactionGasMixtureRatio
                  schema:name:
                    const: Collision/Reaction Gas Mixture Ratio
                  schema:value:
                    type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
            allOf:
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_signalIntegrationTime
              minContains: 0
              maxContains: 1
            - contains:
                title: Collision/Reaction Gas Mixture Ratio
                description: Where the collision or reaction cell is supplied with
                  a mixture of gases rather than a single gas, the identities and
                  proportions of that mixture. Recorded separately from the gas identity.
                  Record 'N/A' where a single gas is used.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/solutionQicpmsTAPP/collisionReactionGasMixtureRatio
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/solutionQicpmsTAPP/collisionReactionGasMixtureRatio
                  schema:name:
                    const: Collision/Reaction Gas Mixture Ratio
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

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-Q-ICPMS/detail/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-Q-ICPMS/detail/schema.yaml)


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
    "dcat": "http://www.w3.org/ns/dcat#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-Q-ICPMS/detail/context.jsonld)

## Sources

* [Solution_Q-ICP-MS_TAPP_v5.xlsx (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/Solution-Q-ICPMS/detail`

