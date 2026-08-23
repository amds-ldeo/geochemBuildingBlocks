
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
      "@id": "ex:solutionQicpmsTAPP-Gao2008"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "AGV-1 (andesite), BHVO-1 (basalt), G-2 (granite), SCO-1 (shale), GSR-5 (shale); GSR-6 and \"another eighteen international\" RMs; worldwide loess and Chinese upper-crustal composites",
  "ada:samplingUnit": "Aliquot of rock powder -- \"Fifty milligrams of sample powder were placed in a home-made PTFE-lined stainless steel bomb\"; final solution made up to 50 ml",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "Per-element blanks in ppb with standard deviation, n = 5 (e.g. B 0.39 +/- 0.26; Zn 0.80 +/- 0.56; Pb 0.043 +/- 0.020; V 0.50 +/- 0.38)",
  "ada:analysisInclusionAndRejectionCriteria": "Partially -- replicate counts stated per reference material (n = 6, 5, 7, 4, 4; blanks n = 5). No acceptance or rejection rule, and no acquired-versus-included count, stated",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "%RSD of repeated standard measurements (stated section 3.1)",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "% recovery relative to USGS/GSCA certified/consensus values (stated section 3.2, Tables 2-3)",
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
  "@id": "ex:detail-Gao2008",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionQicpmsTAPP-Gao2008"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "AGV-1 (andesite), BHVO-1 (basalt), G-2 (granite), SCO-1 (shale), GSR-5 (shale); GSR-6 and \"another eighteen international\" RMs; worldwide loess and Chinese upper-crustal composites",
  "ada:samplingUnit": "Aliquot of rock powder -- \"Fifty milligrams of sample powder were placed in a home-made PTFE-lined stainless steel bomb\"; final solution made up to 50 ml",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "Per-element blanks in ppb with standard deviation, n = 5 (e.g. B 0.39 +/- 0.26; Zn 0.80 +/- 0.56; Pb 0.043 +/- 0.020; V 0.50 +/- 0.38)",
  "ada:analysisInclusionAndRejectionCriteria": "Partially -- replicate counts stated per reference material (n = 6, 5, 7, 4, 4; blanks n = 5). No acceptance or rejection rule, and no acquired-versus-included count, stated",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "%RSD of repeated standard measurements (stated section 3.1)",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "% recovery relative to USGS/GSCA certified/consensus values (stated section 3.2, Tables 2-3)",
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Gao2008 a ada:SolutionICPMSTabular ;
    schema1:measurementTechnique ex:solutionQicpmsTAPP-Gao2008 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially -- replicate counts stated per reference material (n = 6, 5, 7, 4, 4; blanks n = 5). No acceptance or rejection rule, and no acquired-versus-included count, stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "% recovery relative to USGS/GSCA certified/consensus values (stated section 3.2, Tables 2-3)" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "Per-element blanks in ppb with standard deviation, n = 5 (e.g. B 0.39 +/- 0.26; Zn 0.80 +/- 0.56; Pb 0.043 +/- 0.020; V 0.50 +/- 0.38)" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "AGV-1 (andesite), BHVO-1 (basalt), G-2 (granite), SCO-1 (shale), GSR-5 (shale); GSR-6 and \"another eighteen international\" RMs; worldwide loess and Chinese upper-crustal composites" ;
    ada:samplingUnit "Aliquot of rock powder -- \"Fifty milligrams of sample powder were placed in a home-made PTFE-lined stainless steel bomb\"; final solution made up to 50 ml" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "%RSD of repeated standard measurements (stated section 3.1)" .


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
      "@id": "ex:solutionQicpmsTAPP-P1"
    }
  ],
  "ada:sessionIdentifier": "N -- \"a typical run (~5 hr)\" referenced; no run identifier stated",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Partially -- sample type named (\"core top Cibicidoides wuellerstorfi from the north Atlantic Ocean\"); no individual sample identifiers stated in the methods",
  "ada:samplingUnit": "Aliquot of dissolved foraminiferal calcite -- \"Ten to twenty individual foraminifera tests were handpicked\"; cleaned samples \"dissolved in 200 ul 0.075M HNO3\", then split (20 ul for [Ca] by ICP-AES, remainder for ICP-MS)",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": 6,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "Reported as blank contribution relative to typical foraminiferal test ratios: \"<1% for Ca, Mg, Sr and Li; higher blanks were observed for Cd (<2%), and U (<5%) ... and for Zn (<4%)\"; \"The B blank was substantially decreased to ~5% by the employment of a quartz spray chamber, compared with ~30% when using a glass spray chamber\"",
  "ada:analysisInclusionAndRejectionCriteria": "Partially -- number of replicate analyses stated per ratio (n = 120, 88, 32, 70, 50). No acceptance or rejection rule stated",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "Comparison with published inter-lab values for Me/Ca ratios (stated section 3)",
  "ada:goodnessOfFitOrDispersionStatistic": "N for the quantity this field defines. A calibration-curve fit statistic is reported -- \"The calibration curves determined from multiple standards are linear and R2 are usually greater than 0.999\" -- which measures the fit of the calibration, not whether scatter among contributing analyses exceeds analytical uncertainty"
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
      "@id": "ex:solutionQicpmsTAPP-P1"
    }
  ],
  "ada:sessionIdentifier": "N -- \"a typical run (~5 hr)\" referenced; no run identifier stated",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Partially -- sample type named (\"core top Cibicidoides wuellerstorfi from the north Atlantic Ocean\"); no individual sample identifiers stated in the methods",
  "ada:samplingUnit": "Aliquot of dissolved foraminiferal calcite -- \"Ten to twenty individual foraminifera tests were handpicked\"; cleaned samples \"dissolved in 200 ul 0.075M HNO3\", then split (20 ul for [Ca] by ICP-AES, remainder for ICP-MS)",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": 6,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "Reported as blank contribution relative to typical foraminiferal test ratios: \"<1% for Ca, Mg, Sr and Li; higher blanks were observed for Cd (<2%), and U (<5%) ... and for Zn (<4%)\"; \"The B blank was substantially decreased to ~5% by the employment of a quartz spray chamber, compared with ~30% when using a glass spray chamber\"",
  "ada:analysisInclusionAndRejectionCriteria": "Partially -- number of replicate analyses stated per ratio (n = 120, 88, 32, 70, 50). No acceptance or rejection rule stated",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "Comparison with published inter-lab values for Me/Ca ratios (stated section 3)",
  "ada:goodnessOfFitOrDispersionStatistic": "N for the quantity this field defines. A calibration-curve fit statistic is reported -- \"The calibration curves determined from multiple standards are linear and R2 are usually greater than 0.999\" -- which measures the fit of the calibration, not whether scatter among contributing analyses exceeds analytical uncertainty"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-P1 a ada:SolutionICPMSTabular ;
    schema1:measurementTechnique ex:solutionQicpmsTAPP-P1 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially -- number of replicate analyses stated per ratio (n = 120, 88, 32, 70, 50). No acceptance or rejection rule stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "Comparison with published inter-lab values for Me/Ca ratios (stated section 3)" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "N for the quantity this field defines. A calibration-curve fit statistic is reported -- \"The calibration curves determined from multiple standards are linear and R2 are usually greater than 0.999\" -- which measures the fit of the calibration, not whether scatter among contributing analyses exceeds analytical uncertainty" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:numberOfReplicates 6 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "Reported as blank contribution relative to typical foraminiferal test ratios: \"<1% for Ca, Mg, Sr and Li; higher blanks were observed for Cd (<2%), and U (<5%) ... and for Zn (<4%)\"; \"The B blank was substantially decreased to ~5% by the employment of a quartz spray chamber, compared with ~30% when using a glass spray chamber\"" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "Partially -- sample type named (\"core top Cibicidoides wuellerstorfi from the north Atlantic Ocean\"); no individual sample identifiers stated in the methods" ;
    ada:samplingUnit "Aliquot of dissolved foraminiferal calcite -- \"Ten to twenty individual foraminifera tests were handpicked\"; cleaned samples \"dissolved in 200 ul 0.075M HNO3\", then split (20 ul for [Ca] by ICP-AES, remainder for ICP-MS)" ;
    ada:sessionIdentifier "N -- \"a typical run (~5 hr)\" referenced; no run identifier stated" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .


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
      "@id": "ex:solutionQicpmsTAPP-Agilent7500"
    }
  ],
  "ada:sessionIdentifier": "N -- \"an average of eight sessions\" referenced; no session identifier stated",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1; NIST SRM 610, 612, 614, 616 glasses",
  "ada:samplingUnit": "Test portion / solution aliquot -- \"The amount of test portion used was 15-42 mg for basalt and andesite samples, and 30-63 mg for peridotite samples\"; NIST glasses \"a few grains totalling 8-22 mg were used in one analysis\"; \"the same sample solution aliquot\"",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "\"Total dissolution blanks for the ultrasonic bath and bomb digestions were similar at <16 pg for each element (n = 4)\"; per-element blanks Cd 16 pg, In <0.2 pg, Tl 4 pg, Bi 3 pg",
  "ada:analysisInclusionAndRejectionCriteria": "Partially -- n = 5 (evaporation test), n = 4 (dissolution blanks), \"an average of eight sessions\" for detection limits. No acceptance or rejection rule stated. 113Cd was excluded as a determination channel -- \"113Cd was not used for Cd determination, because the correction of 113In was far larger than the MoO correction\" -- which is a channel decision, not an analysis-inclusion decision",
  "ada:detectionLimit": "Analyte-specific (pg/ml level; e.g., Cd 0.04 pg/ml, In 0.5 pg/ml, Tl 0.5 pg/ml, Bi 0.6 pg/ml; stated Table 1)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "%RSD of repeated standard and RM analyses (stated section 2)",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "% recovery relative to certified/consensus values for USGS/GSJ/NIST RMs (stated section 3)",
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
  "@id": "ex:detail-Agilent7500",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionQicpmsTAPP-Agilent7500"
    }
  ],
  "ada:sessionIdentifier": "N -- \"an average of eight sessions\" referenced; no session identifier stated",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1; NIST SRM 610, 612, 614, 616 glasses",
  "ada:samplingUnit": "Test portion / solution aliquot -- \"The amount of test portion used was 15-42 mg for basalt and andesite samples, and 30-63 mg for peridotite samples\"; NIST glasses \"a few grains totalling 8-22 mg were used in one analysis\"; \"the same sample solution aliquot\"",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "\"Total dissolution blanks for the ultrasonic bath and bomb digestions were similar at <16 pg for each element (n = 4)\"; per-element blanks Cd 16 pg, In <0.2 pg, Tl 4 pg, Bi 3 pg",
  "ada:analysisInclusionAndRejectionCriteria": "Partially -- n = 5 (evaporation test), n = 4 (dissolution blanks), \"an average of eight sessions\" for detection limits. No acceptance or rejection rule stated. 113Cd was excluded as a determination channel -- \"113Cd was not used for Cd determination, because the correction of 113In was far larger than the MoO correction\" -- which is a channel decision, not an analysis-inclusion decision",
  "ada:detectionLimit": "Analyte-specific (pg/ml level; e.g., Cd 0.04 pg/ml, In 0.5 pg/ml, Tl 0.5 pg/ml, Bi 0.6 pg/ml; stated Table 1)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "%RSD of repeated standard and RM analyses (stated section 2)",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "% recovery relative to certified/consensus values for USGS/GSJ/NIST RMs (stated section 3)",
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Agilent7500 a ada:SolutionICPMSTabular ;
    schema1:measurementTechnique ex:solutionQicpmsTAPP-Agilent7500 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially -- n = 5 (evaporation test), n = 4 (dissolution blanks), \"an average of eight sessions\" for detection limits. No acceptance or rejection rule stated. 113Cd was excluded as a determination channel -- \"113Cd was not used for Cd determination, because the correction of 113In was far larger than the MoO correction\" -- which is a channel decision, not an analysis-inclusion decision" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "% recovery relative to certified/consensus values for USGS/GSJ/NIST RMs (stated section 3)" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "Analyte-specific (pg/ml level; e.g., Cd 0.04 pg/ml, In 0.5 pg/ml, Tl 0.5 pg/ml, Bi 0.6 pg/ml; stated Table 1)" ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "\"Total dissolution blanks for the ultrasonic bath and bomb digestions were similar at <16 pg for each element (n = 4)\"; per-element blanks Cd 16 pg, In <0.2 pg, Tl 4 pg, Bi 3 pg" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "JB-2, JB-3, JA-1, JA-2, JA-3, JP-1, BHVO-1, AGV-1, PCC-1, DTS-1; NIST SRM 610, 612, 614, 616 glasses" ;
    ada:samplingUnit "Test portion / solution aliquot -- \"The amount of test portion used was 15-42 mg for basalt and andesite samples, and 30-63 mg for peridotite samples\"; NIST glasses \"a few grains totalling 8-22 mg were used in one analysis\"; \"the same sample solution aliquot\"" ;
    ada:sessionIdentifier "N -- \"an average of eight sessions\" referenced; no session identifier stated" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "%RSD of repeated standard and RM analyses (stated section 2)" .


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
      "@id": "ex:solutionQicpmsTAPP-Agilent7900"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "PCA 02010, B-7904, LON 94101 and further CM/CY chondrites",
  "ada:samplingUnit": "N -- no digestion mass or aliquot stated for the elemental (Q-ICP-MS) determination; the \"approximately 35 mg of homogenized bulk powder\" in Methods belongs to the Zn-isotope MC-ICP-MS procedure",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
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
      "@id": "ex:solutionQicpmsTAPP-Agilent7900"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "PCA 02010, B-7904, LON 94101 and further CM/CY chondrites",
  "ada:samplingUnit": "N -- no digestion mass or aliquot stated for the elemental (Q-ICP-MS) determination; the \"approximately 35 mg of homogenized bulk powder\" in Methods belongs to the Zn-isotope MC-ICP-MS procedure",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
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
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Agilent7900 a ada:SolutionICPMSTabular ;
    schema1:measurementTechnique ex:solutionQicpmsTAPP-Agilent7900 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "missing" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
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
    ada:samplingUnit "N -- no digestion mass or aliquot stated for the elemental (Q-ICP-MS) determination; the \"approximately 35 mg of homogenized bulk powder\" in Methods belongs to the Zn-isotope MC-ICP-MS procedure" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .


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
      "@id": "ex:solutionQicpmsTAPP-Agilent7500-2"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1 (GSJ); BHVO-1, AGV-1, PCC-1, DTS-1 (USGS); Ivuna (CI1), Orgueil (CI1), Cold Bokkeveld (CM2), Allende (USNM 3529, Split 1, Pos. 23)",
  "ada:samplingUnit": "Weighed test portion -- \"Approximately 20 mg of basalt and andesite samples were weighed\"; \"Approximately 50 mg for peridotites and approximately 10 mg for meteorites were weighed\"; 9-18 mg for carbonaceous chondrites",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "Blanks in spike solutions (pg g-1) and total procedural blank (pg) tabulated per element; \"Blank effects for Ti, Zr, Mo, Hf and Ta from the Ca-Al-Mg solutions and the total procedure were <0.2% and negligible. The blank effects for Sn and Sb ... were 0.4-9% and 0.2-6%\" [sec 2.4]; \"Blank corrections using the values shown in Table 4 were applied to all analyses. The blank corrections were usually <1% in basalt and andesite analyses and <4% in peridotite reference materials\" [sec 3.6]",
  "ada:analysisInclusionAndRejectionCriteria": "Partially -- \"Orgueil and Allende were analyzed 4 times and twice from the sample digestion, respectively. ... As the sample amounts used were small, and the carbonaceous chondrites are heterogeneous, analytical results for each run are shown in the table\" alongside the averages. No acceptance or rejection rule stated",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "% recovery relative to USGS/GSJ certified values (stated section 3)",
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
  "@id": "ex:detail-Agilent7500-2",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionQicpmsTAPP-Agilent7500-2"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1 (GSJ); BHVO-1, AGV-1, PCC-1, DTS-1 (USGS); Ivuna (CI1), Orgueil (CI1), Cold Bokkeveld (CM2), Allende (USNM 3529, Split 1, Pos. 23)",
  "ada:samplingUnit": "Weighed test portion -- \"Approximately 20 mg of basalt and andesite samples were weighed\"; \"Approximately 50 mg for peridotites and approximately 10 mg for meteorites were weighed\"; 9-18 mg for carbonaceous chondrites",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "Blanks in spike solutions (pg g-1) and total procedural blank (pg) tabulated per element; \"Blank effects for Ti, Zr, Mo, Hf and Ta from the Ca-Al-Mg solutions and the total procedure were <0.2% and negligible. The blank effects for Sn and Sb ... were 0.4-9% and 0.2-6%\" [sec 2.4]; \"Blank corrections using the values shown in Table 4 were applied to all analyses. The blank corrections were usually <1% in basalt and andesite analyses and <4% in peridotite reference materials\" [sec 3.6]",
  "ada:analysisInclusionAndRejectionCriteria": "Partially -- \"Orgueil and Allende were analyzed 4 times and twice from the sample digestion, respectively. ... As the sample amounts used were small, and the carbonaceous chondrites are heterogeneous, analytical results for each run are shown in the table\" alongside the averages. No acceptance or rejection rule stated",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "% recovery relative to USGS/GSJ certified values (stated section 3)",
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Agilent7500-2 a ada:SolutionICPMSTabular ;
    schema1:measurementTechnique ex:solutionQicpmsTAPP-Agilent7500-2 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially -- \"Orgueil and Allende were analyzed 4 times and twice from the sample digestion, respectively. ... As the sample amounts used were small, and the carbonaceous chondrites are heterogeneous, analytical results for each run are shown in the table\" alongside the averages. No acceptance or rejection rule stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "% recovery relative to USGS/GSJ certified values (stated section 3)" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "Blanks in spike solutions (pg g-1) and total procedural blank (pg) tabulated per element; \"Blank effects for Ti, Zr, Mo, Hf and Ta from the Ca-Al-Mg solutions and the total procedure were <0.2% and negligible. The blank effects for Sn and Sb ... were 0.4-9% and 0.2-6%\" [sec 2.4]; \"Blank corrections using the values shown in Table 4 were applied to all analyses. The blank corrections were usually <1% in basalt and andesite analyses and <4% in peridotite reference materials\" [sec 3.6]" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1 (GSJ); BHVO-1, AGV-1, PCC-1, DTS-1 (USGS); Ivuna (CI1), Orgueil (CI1), Cold Bokkeveld (CM2), Allende (USNM 3529, Split 1, Pos. 23)" ;
    ada:samplingUnit "Weighed test portion -- \"Approximately 20 mg of basalt and andesite samples were weighed\"; \"Approximately 50 mg for peridotites and approximately 10 mg for meteorites were weighed\"; 9-18 mg for carbonaceous chondrites" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .


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
      "@id": "ex:solutionQicpmsTAPP-Agilent8800"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "N — SPM isotherm experiment at 1000 mg/L",
  "ada:samplingUnit": "missing",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "Recovery on NCS 73307 total digestions 94 +/- 17% (N = 3)",
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
  "@id": "ex:detail-Agilent8800",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionQicpmsTAPP-Agilent8800"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "N \u2014 SPM isotherm experiment at 1000 mg/L",
  "ada:samplingUnit": "missing",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "Recovery on NCS 73307 total digestions 94 +/- 17% (N = 3)",
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Agilent8800 a ada:SolutionICPMSTabular ;
    schema1:measurementTechnique ex:solutionQicpmsTAPP-Agilent8800 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "Recovery on NCS 73307 total digestions 94 +/- 17% (N = 3)" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
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
    ada:sampleName "N — SPM isotherm experiment at 1000 mg/L" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .


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
      "@id": "ex:solutionQicpmsTAPP-P6"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Selective extraction fractions F1-F4 and F4N; CRM NCS 73307",
  "ada:samplingUnit": "Weighed sediment aliquot — 30 mg for tri-acid digestion; 200-500 mg per selective extraction fraction",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "Three blanks run for each extraction; 126Xe contribution from 2% HNO3 analytical blanks noted",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "LOD 0.1 ng L-1 (N = 10); selective-extraction Te concentrations 5-fold (F2) to 200-fold (F4) above LOD",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "Recoveries: NIST 1643f 95 +/- 5% (N = 5) in KED mode and 89 +/- 10% (N = 5) in O2 mode; NCS 73307 99 +/- 14% (N = 4) in KED and 70 +/- 19% (N = 4) in O2 mode",
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
      "@id": "ex:solutionQicpmsTAPP-P6"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Selective extraction fractions F1-F4 and F4N; CRM NCS 73307",
  "ada:samplingUnit": "Weighed sediment aliquot \u2014 30 mg for tri-acid digestion; 200-500 mg per selective extraction fraction",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "Three blanks run for each extraction; 126Xe contribution from 2% HNO3 analytical blanks noted",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "LOD 0.1 ng L-1 (N = 10); selective-extraction Te concentrations 5-fold (F2) to 200-fold (F4) above LOD",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "Recoveries: NIST 1643f 95 +/- 5% (N = 5) in KED mode and 89 +/- 10% (N = 5) in O2 mode; NCS 73307 99 +/- 14% (N = 4) in KED and 70 +/- 19% (N = 4) in O2 mode",
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-P6 a ada:SolutionICPMSTabular ;
    schema1:measurementTechnique ex:solutionQicpmsTAPP-P6 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "Recoveries: NIST 1643f 95 +/- 5% (N = 5) in KED mode and 89 +/- 10% (N = 5) in O2 mode; NCS 73307 99 +/- 14% (N = 4) in KED and 70 +/- 19% (N = 4) in O2 mode" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "LOD 0.1 ng L-1 (N = 10); selective-extraction Te concentrations 5-fold (F2) to 200-fold (F4) above LOD" ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "Three blanks run for each extraction; 126Xe contribution from 2% HNO3 analytical blanks noted" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "Selective extraction fractions F1-F4 and F4N; CRM NCS 73307" ;
    ada:samplingUnit "Weighed sediment aliquot — 30 mg for tri-acid digestion; 200-500 mg per selective extraction fraction" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .


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
      "@id": "ex:solutionQicpmsTAPP-P7"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "N — sorption kinetics and isotherm solutions; CRMs CRM-TMDW and NIST 1643f",
  "ada:samplingUnit": "N — sub-sampled water aliquots",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "LOD 0.01 ug L-1 (N = 10)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "Recoveries 98-... % on CRM-TMDW and NIST 1643f",
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
  "@id": "ex:detail-P7",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionQicpmsTAPP-P7"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "N \u2014 sorption kinetics and isotherm solutions; CRMs CRM-TMDW and NIST 1643f",
  "ada:samplingUnit": "N \u2014 sub-sampled water aliquots",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "LOD 0.01 ug L-1 (N = 10)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "Recoveries 98-... % on CRM-TMDW and NIST 1643f",
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-P7 a ada:SolutionICPMSTabular ;
    schema1:measurementTechnique ex:solutionQicpmsTAPP-P7 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "Recoveries 98-... % on CRM-TMDW and NIST 1643f" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "LOD 0.01 ug L-1 (N = 10)" ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "N — sorption kinetics and isotherm solutions; CRMs CRM-TMDW and NIST 1643f" ;
    ada:samplingUnit "N — sub-sampled water aliquots" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .


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
      "@id": "ex:solutionQicpmsTAPP-P8"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Ryugu particles A0066, A0238, A0247, A0256, A0259, A0268, A0301, A0313; Smithsonian Allende powder",
  "ada:samplingUnit": "Individual particle, weighed: A0066 4.325 mg, A0238 1.868 mg, A0247 2.311 mg, A0256 2.378 mg, A0259 1.478 mg, A0268 1.902 mg, A0301 1.923 mg, A0313 2.012 mg; 20 mg Allende",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "N — blank data stated to be in the supplementary material; Ta and W blank contributions exceeded 30%",
  "ada:analysisInclusionAndRejectionCriteria": "Explicit rule and outcome: 'Although the abundances of Ta and W were measured, the data for these elements were excluded from the results due to high blank contributions (>30%) during the ICP-MS analysis'",
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
  "@id": "ex:detail-P8",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionQicpmsTAPP-P8"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Ryugu particles A0066, A0238, A0247, A0256, A0259, A0268, A0301, A0313; Smithsonian Allende powder",
  "ada:samplingUnit": "Individual particle, weighed: A0066 4.325 mg, A0238 1.868 mg, A0247 2.311 mg, A0256 2.378 mg, A0259 1.478 mg, A0268 1.902 mg, A0301 1.923 mg, A0313 2.012 mg; 20 mg Allende",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "N \u2014 blank data stated to be in the supplementary material; Ta and W blank contributions exceeded 30%",
  "ada:analysisInclusionAndRejectionCriteria": "Explicit rule and outcome: 'Although the abundances of Ta and W were measured, the data for these elements were excluded from the results due to high blank contributions (>30%) during the ICP-MS analysis'",
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
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-P8 a ada:SolutionICPMSTabular ;
    schema1:measurementTechnique ex:solutionQicpmsTAPP-P8 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Explicit rule and outcome: 'Although the abundances of Ta and W were measured, the data for these elements were excluded from the results due to high blank contributions (>30%) during the ICP-MS analysis'" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "missing" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
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
    ada:samplingUnit "Individual particle, weighed: A0066 4.325 mg, A0238 1.868 mg, A0247 2.311 mg, A0256 2.378 mg, A0259 1.478 mg, A0268 1.902 mg, A0301 1.923 mg, A0313 2.012 mg; 20 mg Allende" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Solution Q-ICP-MS Analysis Detail
description: Dataset-level analysis-instance detail for solution Q-ICP-MS, reusing
  CDIF/schema.org slots on the schema:Dataset root.
allOf:
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/AnalysisIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/aggregation/schema.yaml#/$defs/AnalysisIdentification
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
                            - title: Spike / Outlier Filtering Approach
                              description: Criteria used to identify and exclude anomalous
                                replicate measurements or data points from the calculated
                                mean.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionQicpmsTAPP/spikeOutlierFilteringApproach
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionQicpmsTAPP/spikeOutlierFilteringApproach
                                schema:name:
                                  const: Spike / Outlier Filtering Approach
                                schema:value:
                                  type: string
                              required:
                              - '@id'
                              - '@type'
                              - schema:propertyID
                              - schema:name
                              - schema:value
                            - title: Pulse/Analog Detector Nonlinearity Correction
                              description: Whether a correction was applied for nonlinear
                                detector response at the transition between pulse-counting
                                and analog detection modes. For Q-ICP-MS instruments
                                with dual-mode SEM detectors, a cross-calibration
                                factor is measured and applied at the pulse-to-analog
                                crossover threshold. Accurate cross-calibration is
                                critical for analytes spanning a wide concentration
                                range in the same session.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionQicpmsTAPP/pulseAnalogDetectorNonlinearityCorrection
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionQicpmsTAPP/pulseAnalogDetectorNonlinearityCorrection
                                schema:name:
                                  const: Pulse/Analog Detector Nonlinearity Correction
                                schema:value:
                                  type: string
                              required:
                              - '@id'
                              - '@type'
                              - schema:propertyID
                              - schema:name
                              - schema:value
                            - title: Uncertainty Propagation Method
                              description: 'The approach used to propagate analytical
                                uncertainty through the data reduction chain to the
                                final reported value. State which sources are included
                                in the propagation: counting statistics, calibration
                                standard uncertainty, internal standard uncertainty,
                                drift correction, and any systematic contributions.
                                Distinct from Uncertainty Level, which states the
                                convention at which the resulting uncertainty is quoted.'
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionQicpmsTAPP/uncertaintyPropagationMethod
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionQicpmsTAPP/uncertaintyPropagationMethod
                                schema:name:
                                  const: Uncertainty Propagation Method
                                schema:value:
                                  type: string
                              required:
                              - '@id'
                              - '@type'
                              - schema:propertyID
                              - schema:name
                              - schema:value
                            - title: Normalization / Standards-Based Correction
                              description: Post-acquisition normalization applied
                                to output concentrations relative to a reference value
                                (e.g., correction to a monitor element's certified
                                value in the calibration standard).
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionQicpmsTAPP/normalizationStandardsBasedCorrection
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionQicpmsTAPP/normalizationStandardsBasedCorrection
                                schema:name:
                                  const: Normalization / Standards-Based Correction
                                schema:value:
                                  type: string
                              required:
                              - '@id'
                              - '@type'
                              - schema:propertyID
                              - schema:name
                              - schema:value
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Analysis_constantsReferenceValues
                          allOf:
                          - contains:
                              title: Spike / Outlier Filtering Approach
                              description: Criteria used to identify and exclude anomalous
                                replicate measurements or data points from the calculated
                                mean.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionQicpmsTAPP/spikeOutlierFilteringApproach
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionQicpmsTAPP/spikeOutlierFilteringApproach
                                schema:name:
                                  const: Spike / Outlier Filtering Approach
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
                              title: Pulse/Analog Detector Nonlinearity Correction
                              description: Whether a correction was applied for nonlinear
                                detector response at the transition between pulse-counting
                                and analog detection modes. For Q-ICP-MS instruments
                                with dual-mode SEM detectors, a cross-calibration
                                factor is measured and applied at the pulse-to-analog
                                crossover threshold. Accurate cross-calibration is
                                critical for analytes spanning a wide concentration
                                range in the same session.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionQicpmsTAPP/pulseAnalogDetectorNonlinearityCorrection
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionQicpmsTAPP/pulseAnalogDetectorNonlinearityCorrection
                                schema:name:
                                  const: Pulse/Analog Detector Nonlinearity Correction
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
                              title: Uncertainty Propagation Method
                              description: 'The approach used to propagate analytical
                                uncertainty through the data reduction chain to the
                                final reported value. State which sources are included
                                in the propagation: counting statistics, calibration
                                standard uncertainty, internal standard uncertainty,
                                drift correction, and any systematic contributions.
                                Distinct from Uncertainty Level, which states the
                                convention at which the resulting uncertainty is quoted.'
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionQicpmsTAPP/uncertaintyPropagationMethod
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionQicpmsTAPP/uncertaintyPropagationMethod
                                schema:name:
                                  const: Uncertainty Propagation Method
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
                              title: Normalization / Standards-Based Correction
                              description: Post-acquisition normalization applied
                                to output concentrations relative to a reference value
                                (e.g., correction to a monitor element's certified
                                value in the calibration standard).
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionQicpmsTAPP/normalizationStandardsBasedCorrection
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionQicpmsTAPP/normalizationStandardsBasedCorrection
                                schema:name:
                                  const: Normalization / Standards-Based Correction
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
                                schema:identifier:
                                  description: Serial number or laboratory-internal
                                    identifier for the specific instrument unit. Supports
                                    traceability to instrument service records.
                                  anyOf:
                                  - type: string
                                  - type: array
                                    items:
                                      type: string
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
                                              title: Torch Depth
                                              description: Distance between the load
                                                coil and the sampling cone tip (mm),
                                                also called injector depth or torch
                                                position depending on the instrument
                                                manufacturer. Affects ion transmission
                                                efficiency, oxide formation, and doubly-charged
                                                species production. The procedure
                                                specifies a target value optimised
                                                during initial setup; the analyst
                                                confirms or fine-adjusts during session
                                                tuning.
                                              type: object
                                              properties:
                                                '@id':
                                                  const: ada:parameter/solutionQicpmsTAPP/torchDepth
                                                '@type':
                                                  const:
                                                  - schema:PropertyValue
                                                schema:propertyID:
                                                  const:
                                                  - '@id': ada:parameter/solutionQicpmsTAPP/torchDepth
                                                schema:name:
                                                  const: Torch Depth
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
                                                title: Torch Depth
                                                description: Distance between the
                                                  load coil and the sampling cone
                                                  tip (mm), also called injector depth
                                                  or torch position depending on the
                                                  instrument manufacturer. Affects
                                                  ion transmission efficiency, oxide
                                                  formation, and doubly-charged species
                                                  production. The procedure specifies
                                                  a target value optimised during
                                                  initial setup; the analyst confirms
                                                  or fine-adjusts during session tuning.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/solutionQicpmsTAPP/torchDepth
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/solutionQicpmsTAPP/torchDepth
                                                  schema:name:
                                                    const: Torch Depth
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
                                              - title: Make-up Gas and Flow Rate
                                                description: "Supplementary gas added
                                                  to the sample-carrying stream between
                                                  the sample introduction system and
                                                  the plasma, with its identity and
                                                  the procedure-registered target
                                                  flow rate. Argon make-up is standard
                                                  and maintains total gas delivery
                                                  where the carrier flow alone is
                                                  insufficient \u2014 downstream of
                                                  an ablation cell, or of a desolvation
                                                  system that has removed solvent
                                                  load. Small nitrogen or hydrogen
                                                  additions are also made here to
                                                  enhance sensitivity for some elements;
                                                  record them with their own flow,
                                                  whose unit commonly differs from
                                                  the make-up flow. Record 'None'
                                                  explicitly where no supplementary
                                                  gas is added, to distinguish it
                                                  from not reported."
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/solutionQicpmsTAPP/makeUpGasAndFlowRate
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/solutionQicpmsTAPP/makeUpGasAndFlowRate
                                                  schema:name:
                                                    const: Make-up Gas and Flow Rate
                                                  schema:value:
                                                    anyOf:
                                                    - type: number
                                                    - type: string
                                                  schema:unitText:
                                                    type: string
                                                required:
                                                - '@id'
                                                - '@type'
                                                - schema:propertyID
                                                - schema:name
                                                - schema:value
                                                - schema:unitText
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
                                                title: Make-up Gas and Flow Rate
                                                description: "Supplementary gas added
                                                  to the sample-carrying stream between
                                                  the sample introduction system and
                                                  the plasma, with its identity and
                                                  the procedure-registered target
                                                  flow rate. Argon make-up is standard
                                                  and maintains total gas delivery
                                                  where the carrier flow alone is
                                                  insufficient \u2014 downstream of
                                                  an ablation cell, or of a desolvation
                                                  system that has removed solvent
                                                  load. Small nitrogen or hydrogen
                                                  additions are also made here to
                                                  enhance sensitivity for some elements;
                                                  record them with their own flow,
                                                  whose unit commonly differs from
                                                  the make-up flow. Record 'None'
                                                  explicitly where no supplementary
                                                  gas is added, to distinguish it
                                                  from not reported."
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/solutionQicpmsTAPP/makeUpGasAndFlowRate
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/solutionQicpmsTAPP/makeUpGasAndFlowRate
                                                  schema:name:
                                                    const: Make-up Gas and Flow Rate
                                                  schema:value:
                                                    anyOf:
                                                    - type: number
                                                    - type: string
                                                  schema:unitText:
                                                    type: string
                                                required:
                                                - '@id'
                                                - '@type'
                                                - schema:propertyID
                                                - schema:name
                                                - schema:value
                                                - schema:unitText
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
                                              - title: RF Power
                                                description: Radiofrequency forward
                                                  power applied to the plasma (W).
                                                  Controls ionization efficiency and
                                                  oxide production rates.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/solutionQicpmsTAPP/rfPower
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/solutionQicpmsTAPP/rfPower
                                                  schema:name:
                                                    const: RF Power
                                                  schema:value:
                                                    anyOf:
                                                    - type: number
                                                    - type: string
                                                  schema:unitText:
                                                    type: string
                                                required:
                                                - '@id'
                                                - '@type'
                                                - schema:propertyID
                                                - schema:name
                                                - schema:value
                                                - schema:unitText
                                              - title: Coolant (Plasma) Gas Flow Rate
                                                description: Flow rate of the outer
                                                  (coolant) argon gas stream (L/min).
                                                  Influences plasma temperature and
                                                  oxide ion formation.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/solutionQicpmsTAPP/coolantGasFlowRate
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/solutionQicpmsTAPP/coolantGasFlowRate
                                                  schema:name:
                                                    const: Coolant (Plasma) Gas Flow
                                                      Rate
                                                  schema:value:
                                                    anyOf:
                                                    - type: number
                                                    - type: string
                                                  schema:unitText:
                                                    type: string
                                                required:
                                                - '@id'
                                                - '@type'
                                                - schema:propertyID
                                                - schema:name
                                                - schema:value
                                                - schema:unitText
                                              - title: Auxiliary Gas Flow Rate
                                                description: Flow rate of the intermediate
                                                  (auxiliary) argon gas stream between
                                                  torch body and injector tube (L/min).
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/solutionQicpmsTAPP/auxiliaryGasFlowRate
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/solutionQicpmsTAPP/auxiliaryGasFlowRate
                                                  schema:name:
                                                    const: Auxiliary Gas Flow Rate
                                                  schema:value:
                                                    anyOf:
                                                    - type: number
                                                    - type: string
                                                  schema:unitText:
                                                    type: string
                                                required:
                                                - '@id'
                                                - '@type'
                                                - schema:propertyID
                                                - schema:name
                                                - schema:value
                                                - schema:unitText
                                            allOf:
                                            - contains:
                                                title: RF Power
                                                description: Radiofrequency forward
                                                  power applied to the plasma (W).
                                                  Controls ionization efficiency and
                                                  oxide production rates.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/solutionQicpmsTAPP/rfPower
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/solutionQicpmsTAPP/rfPower
                                                  schema:name:
                                                    const: RF Power
                                                  schema:value:
                                                    anyOf:
                                                    - type: number
                                                    - type: string
                                                  schema:unitText:
                                                    type: string
                                                required:
                                                - '@id'
                                                - '@type'
                                                - schema:propertyID
                                                - schema:name
                                                - schema:value
                                                - schema:unitText
                                              minContains: 0
                                              maxContains: 1
                                            - contains:
                                                title: Coolant (Plasma) Gas Flow Rate
                                                description: Flow rate of the outer
                                                  (coolant) argon gas stream (L/min).
                                                  Influences plasma temperature and
                                                  oxide ion formation.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/solutionQicpmsTAPP/coolantGasFlowRate
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/solutionQicpmsTAPP/coolantGasFlowRate
                                                  schema:name:
                                                    const: Coolant (Plasma) Gas Flow
                                                      Rate
                                                  schema:value:
                                                    anyOf:
                                                    - type: number
                                                    - type: string
                                                  schema:unitText:
                                                    type: string
                                                required:
                                                - '@id'
                                                - '@type'
                                                - schema:propertyID
                                                - schema:name
                                                - schema:value
                                                - schema:unitText
                                              minContains: 0
                                              maxContains: 1
                                            - contains:
                                                title: Auxiliary Gas Flow Rate
                                                description: Flow rate of the intermediate
                                                  (auxiliary) argon gas stream between
                                                  torch body and injector tube (L/min).
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/solutionQicpmsTAPP/auxiliaryGasFlowRate
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/solutionQicpmsTAPP/auxiliaryGasFlowRate
                                                  schema:name:
                                                    const: Auxiliary Gas Flow Rate
                                                  schema:value:
                                                    anyOf:
                                                    - type: number
                                                    - type: string
                                                  schema:unitText:
                                                    type: string
                                                required:
                                                - '@id'
                                                - '@type'
                                                - schema:propertyID
                                                - schema:name
                                                - schema:value
                                                - schema:unitText
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
                                              - title: Collision Gas Flow Rate
                                                description: Flow rate of the collision
                                                  gas in KED mode (mL/min). Higher
                                                  flow rates provide greater interference
                                                  suppression at the cost of analyte
                                                  sensitivity. Record 'N/A' if KED
                                                  mode is not used. Record 'N/A' where
                                                  Collision/Reaction Cell (CRC) Configuration
                                                  does not include KED.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/solutionQicpmsTAPP/collisionGasFlowRate
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/solutionQicpmsTAPP/collisionGasFlowRate
                                                  schema:name:
                                                    const: Collision Gas Flow Rate
                                                  schema:value:
                                                    anyOf:
                                                    - type: number
                                                    - type: string
                                                  schema:unitText:
                                                    type: string
                                                required:
                                                - '@id'
                                                - '@type'
                                                - schema:propertyID
                                                - schema:name
                                                - schema:value
                                                - schema:unitText
                                              - title: Cell Exit Discrimination Voltage
                                                description: Kinetic energy discrimination
                                                  offset voltage applied at the exit
                                                  of the collision cell (V). Controls
                                                  the degree of polyatomic ion suppression.
                                                  Record 'N/A' if KED mode is not
                                                  used. Record 'N/A' where Collision/Reaction
                                                  Cell (CRC) Configuration does not
                                                  include KED.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/solutionQicpmsTAPP/cellExitDiscriminationVoltage
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/solutionQicpmsTAPP/cellExitDiscriminationVoltage
                                                  schema:name:
                                                    const: Cell Exit Discrimination
                                                      Voltage
                                                  schema:value:
                                                    anyOf:
                                                    - type: number
                                                    - type: string
                                                  schema:unitText:
                                                    type: string
                                                required:
                                                - '@id'
                                                - '@type'
                                                - schema:propertyID
                                                - schema:name
                                                - schema:value
                                                - schema:unitText
                                              - title: Reaction Gas Flow Rate
                                                description: Flow rate of the reaction
                                                  gas in DRC mode (mL/min). Record
                                                  'N/A' if DRC mode is not used. Record
                                                  'N/A' where Collision/Reaction Cell
                                                  (CRC) Configuration does not include
                                                  DRC.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/solutionQicpmsTAPP/reactionGasFlowRate
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/solutionQicpmsTAPP/reactionGasFlowRate
                                                  schema:name:
                                                    const: Reaction Gas Flow Rate
                                                  schema:value:
                                                    anyOf:
                                                    - type: number
                                                    - type: string
                                                  schema:unitText:
                                                    type: string
                                                required:
                                                - '@id'
                                                - '@type'
                                                - schema:propertyID
                                                - schema:name
                                                - schema:value
                                                - schema:unitText
                                            allOf:
                                            - contains:
                                                title: Collision Gas Flow Rate
                                                description: Flow rate of the collision
                                                  gas in KED mode (mL/min). Higher
                                                  flow rates provide greater interference
                                                  suppression at the cost of analyte
                                                  sensitivity. Record 'N/A' if KED
                                                  mode is not used. Record 'N/A' where
                                                  Collision/Reaction Cell (CRC) Configuration
                                                  does not include KED.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/solutionQicpmsTAPP/collisionGasFlowRate
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/solutionQicpmsTAPP/collisionGasFlowRate
                                                  schema:name:
                                                    const: Collision Gas Flow Rate
                                                  schema:value:
                                                    anyOf:
                                                    - type: number
                                                    - type: string
                                                  schema:unitText:
                                                    type: string
                                                required:
                                                - '@id'
                                                - '@type'
                                                - schema:propertyID
                                                - schema:name
                                                - schema:value
                                                - schema:unitText
                                              minContains: 0
                                              maxContains: 1
                                            - contains:
                                                title: Cell Exit Discrimination Voltage
                                                description: Kinetic energy discrimination
                                                  offset voltage applied at the exit
                                                  of the collision cell (V). Controls
                                                  the degree of polyatomic ion suppression.
                                                  Record 'N/A' if KED mode is not
                                                  used. Record 'N/A' where Collision/Reaction
                                                  Cell (CRC) Configuration does not
                                                  include KED.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/solutionQicpmsTAPP/cellExitDiscriminationVoltage
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/solutionQicpmsTAPP/cellExitDiscriminationVoltage
                                                  schema:name:
                                                    const: Cell Exit Discrimination
                                                      Voltage
                                                  schema:value:
                                                    anyOf:
                                                    - type: number
                                                    - type: string
                                                  schema:unitText:
                                                    type: string
                                                required:
                                                - '@id'
                                                - '@type'
                                                - schema:propertyID
                                                - schema:name
                                                - schema:value
                                                - schema:unitText
                                              minContains: 0
                                              maxContains: 1
                                            - contains:
                                                title: Reaction Gas Flow Rate
                                                description: Flow rate of the reaction
                                                  gas in DRC mode (mL/min). Record
                                                  'N/A' if DRC mode is not used. Record
                                                  'N/A' where Collision/Reaction Cell
                                                  (CRC) Configuration does not include
                                                  DRC.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/solutionQicpmsTAPP/reactionGasFlowRate
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/solutionQicpmsTAPP/reactionGasFlowRate
                                                  schema:name:
                                                    const: Reaction Gas Flow Rate
                                                  schema:value:
                                                    anyOf:
                                                    - type: number
                                                    - type: string
                                                  schema:unitText:
                                                    type: string
                                                required:
                                                - '@id'
                                                - '@type'
                                                - schema:propertyID
                                                - schema:name
                                                - schema:value
                                                - schema:unitText
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
                                      description: Mass ratio monitored to estimate
                                        doubly-charged ion (M2+) formation during
                                        instrument tuning. Doubly-charged ions appear
                                        at half the nominal mass of the parent ion
                                        and can interfere with lighter analyte masses.
                                        Ba2+/Ba+ (m/z 69/138) and Ce2+/Ce+ (m/z 70/140)
                                        are the most common proxies for solution ICP-MS.
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
                                        the time of instrument tuning. Record both
                                        the acceptance threshold and the measured
                                        value. Elevated doubly-charged production
                                        indicates incomplete ionization and potential
                                        interference on elements at approximately
                                        half the mass of abundant matrix components.
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
                                    - title: Memory Effect Mitigation
                                      description: Procedure applied to identify and
                                        minimize carry-over of high-concentration
                                        elements between successive sample introductions.
                                        For solution ICP-MS, mitigation is implemented
                                        primarily at measurement time through extended
                                        rinse periods (see Wash Time Between Samples,
                                        Group 4). At data processing level, documents
                                        any flagging or exclusion of measurements
                                        preceded by high-concentration samples or
                                        standards where the required washout time
                                        may not have been achieved.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/solutionQicpmsTAPP/memoryEffectMitigation
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/solutionQicpmsTAPP/memoryEffectMitigation
                                        schema:name:
                                          const: Memory Effect Mitigation
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
                                      title: Doubly-Charged Species Monitor
                                      description: Mass ratio monitored to estimate
                                        doubly-charged ion (M2+) formation during
                                        instrument tuning. Doubly-charged ions appear
                                        at half the nominal mass of the parent ion
                                        and can interfere with lighter analyte masses.
                                        Ba2+/Ba+ (m/z 69/138) and Ce2+/Ce+ (m/z 70/140)
                                        are the most common proxies for solution ICP-MS.
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
                                        the time of instrument tuning. Record both
                                        the acceptance threshold and the measured
                                        value. Elevated doubly-charged production
                                        indicates incomplete ionization and potential
                                        interference on elements at approximately
                                        half the mass of abundant matrix components.
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
                                      title: Memory Effect Mitigation
                                      description: Procedure applied to identify and
                                        minimize carry-over of high-concentration
                                        elements between successive sample introductions.
                                        For solution ICP-MS, mitigation is implemented
                                        primarily at measurement time through extended
                                        rinse periods (see Wash Time Between Samples,
                                        Group 4). At data processing level, documents
                                        any flagging or exclusion of measurements
                                        preceded by high-concentration samples or
                                        standards where the required washout time
                                        may not have been achieved.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/solutionQicpmsTAPP/memoryEffectMitigation
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/solutionQicpmsTAPP/memoryEffectMitigation
                                        schema:name:
                                          const: Memory Effect Mitigation
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
                      allOf:
                      - contains:
                          properties:
                            schema:additionalType:
                              contains:
                                const: ICPMS
                              schema:inDefinedTermSet: ada:vocab/instrumentType
                          required:
                          - schema:additionalType
              - if:
                  required:
                  - prov:reagent
                then:
                  properties:
                    prov:reagent:
                      type: array
                      items:
                        allOf:
                        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/geochemProduct/schema.yaml#/$defs/UsedReagent
                        - type: object
                          allOf:
                          - if:
                              properties:
                                ada:reagentRole:
                                  const: primaryStandard
                              required:
                              - ada:reagentRole
                            then:
                              properties:
                                schema:name:
                                  description: Name and reference material identifier
                                    of the external calibration standard used to convert
                                    signal intensities to elemental concentrations.
                                    Include the material name, its source or supplier,
                                    and a citation for the accepted values used, since
                                    results calibrated against different published
                                    values for the same material are not directly
                                    comparable.
                                  anyOf:
                                  - type: string
                                  - type: array
                                    items:
                                      type: string
                          - if:
                              properties:
                                ada:reagentRole:
                                  const: referenceMaterial
                              required:
                              - ada:reagentRole
                            then:
                              properties:
                                schema:name:
                                  description: Reference material(s) measured as unknowns
                                    to independently assess analytical accuracy. Specify
                                    material name and expected-value source.
                                  anyOf:
                                  - type: string
                                  - type: array
                                    items:
                                      type: string
                          required:
                          - ada:reagentRole
          schema:additionalProperty:
            type: array
            items:
              anyOf:
              - title: Signal Integration Time
                description: Total integration time per analyte per replicate (s).
                  Determined at analysis time from the actual acquisition.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/solutionQicpmsTAPP/signalIntegrationTime
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/solutionQicpmsTAPP/signalIntegrationTime
                  schema:name:
                    const: Signal Integration Time
                  schema:value:
                    anyOf:
                    - type: number
                    - type: string
                  schema:unitText:
                    type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
                - schema:unitText
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/blank/schema.yaml#/$defs/Param_Analysis_proceduralBlankLevel
            allOf:
            - contains:
                title: Signal Integration Time
                description: Total integration time per analyte per replicate (s).
                  Determined at analysis time from the actual acquisition.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/solutionQicpmsTAPP/signalIntegrationTime
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/solutionQicpmsTAPP/signalIntegrationTime
                  schema:name:
                    const: Signal Integration Time
                  schema:value:
                    anyOf:
                    - type: number
                    - type: string
                  schema:unitText:
                    type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
                - schema:unitText
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/blank/schema.yaml#/$defs/Param_Analysis_proceduralBlankLevel
              minContains: 0
              maxContains: 1
    dqv:hasQualityMeasurement:
      type: array
      items:
        type: object
        allOf:
        - if:
            properties:
              dqv:isMeasurementOf:
                const: Oxide production ratio
            required:
            - dqv:isMeasurementOf
          then:
            properties:
              dqv:value:
                description: Measured oxide production ratio obtained during session-start
                  tuning, for the proxy specified in Oxide Production Method and Threshold.
                  Record the measured value and confirm whether the procedure threshold
                  was met.
                anyOf:
                - type: string
                - type: array
                  items:
                    type: string
      allOf:
      - contains:
          properties:
            dqv:isMeasurementOf:
              const: Oxide production ratio
          required:
          - dqv:isMeasurementOf

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
    "wd": "https://www.wikidata.org/entity/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "cdif": "https://w3id.org/cdif/",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
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

