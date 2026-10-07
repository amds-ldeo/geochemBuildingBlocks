
# LA-Q-ICP-MS Analysis Detail (Schema)

`ogch.techniqueProfile.geochemProfile.LA-Q-ICPMS.detail` *v0.1*

Dataset-level analysis-instance detail for LA-Q-ICP-MS, reusing CDIF/schema.org slots on the schema:Dataset root.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### detail example Nakanishi2022
detail instance derived from Nakanishi et al. 2022 (GCA 319) CR chondrite metal (HSE) Spot analysis fs-LA-Q-ICP-MS Tokyo Institute of Technology.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Nakanishi2022",
  "@type": [
    "ada:LAICPMSTabular"
  ],
  "ada:componentType": "ada:LAICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laQicpmsTAPP-Nakanishi2022",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "JSPS Grant-in-Aid for Scientific Research (grants 26106002, 26220713, 16H04081, 19H00715, 19H01081, 20H04609)",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Labelled: metal grains by host chondrule within each section — e.g. \"N8_02 interior ch2-1\" with LA \"spot No.\" 201, 202; \"N8_05 margin ch1\"; isolated grain \"iso1\" (table p.6; p.4) — in the sections \"NWA801-3-8, NWA7184-29-9, and DHO1432-5-5\" (p.2)",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": 1,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially — the contributing counts are stated per grain, the reported ratios being \"the mean Re/Os abundance ratios for each of the 1–3 analytical spots measured by LA-ICP-MS\" (p.8). No acceptance or rejection rule is stated for the LA data; the 233/235 > 0.2 rejection (p.4) is a rule for the N-TIMS Os measurements, not for these spot analyses, and is not borrowed",
  "ada:combinedResults": "per-grain mean Re/Os ratio for each metal grain in Table 3 (1–3 spots each)",
  "ada:detectionLimit": "N — LODs not formally stated",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "all: 2SE of individual measurements — 'Analytical uncertainties accompanied with the data are 2SE of individual measurements' (p.4)",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "N — the 2SE is stated for individual measurements (p.4), not for a standard",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsTAPP/preAnalysisImagingAndScreening",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/preAnalysisImagingAndScreening"
        }
      ],
      "schema:name": "Pre-Analysis Imaging and Screening",
      "schema:value": "Secondary-electron imaging on the EPMA, used to place every spot — \"Based on the secondary electron images taken by EPMA, we selected analytical spots for LA-ICP-MS and sampling spots for micro-milling\" (p.4); the spots carry numbers (\"spot No.\" 201, 202 …) that tie the analyses back to those images (table p.6)"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/transectRateMappingRateOrStepSize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/transectRateMappingRateOrStepSize"
        }
      ],
      "schema:name": "Transect Rate, Mapping Rate or Step Size",
      "schema:value": "N/A — spot mode"
    }
  ],
  "ada:spotDiameterMeasured": -9999
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Nakanishi2022",
  "@type": [
    "ada:LAICPMSTabular"
  ],
  "ada:componentType": "ada:LAICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laQicpmsTAPP-Nakanishi2022",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "JSPS Grant-in-Aid for Scientific Research (grants 26106002, 26220713, 16H04081, 19H00715, 19H01081, 20H04609)",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Labelled: metal grains by host chondrule within each section \u2014 e.g. \"N8_02 interior ch2-1\" with LA \"spot No.\" 201, 202; \"N8_05 margin ch1\"; isolated grain \"iso1\" (table p.6; p.4) \u2014 in the sections \"NWA801-3-8, NWA7184-29-9, and DHO1432-5-5\" (p.2)",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": 1,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially \u2014 the contributing counts are stated per grain, the reported ratios being \"the mean Re/Os abundance ratios for each of the 1\u20133 analytical spots measured by LA-ICP-MS\" (p.8). No acceptance or rejection rule is stated for the LA data; the 233/235 > 0.2 rejection (p.4) is a rule for the N-TIMS Os measurements, not for these spot analyses, and is not borrowed",
  "ada:combinedResults": "per-grain mean Re/Os ratio for each metal grain in Table 3 (1\u20133 spots each)",
  "ada:detectionLimit": "N \u2014 LODs not formally stated",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "all: 2SE of individual measurements \u2014 'Analytical uncertainties accompanied with the data are 2SE of individual measurements' (p.4)",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "N \u2014 the 2SE is stated for individual measurements (p.4), not for a standard",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsTAPP/preAnalysisImagingAndScreening",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/preAnalysisImagingAndScreening"
        }
      ],
      "schema:name": "Pre-Analysis Imaging and Screening",
      "schema:value": "Secondary-electron imaging on the EPMA, used to place every spot \u2014 \"Based on the secondary electron images taken by EPMA, we selected analytical spots for LA-ICP-MS and sampling spots for micro-milling\" (p.4); the spots carry numbers (\"spot No.\" 201, 202 \u2026) that tie the analyses back to those images (table p.6)"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/transectRateMappingRateOrStepSize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/transectRateMappingRateOrStepSize"
        }
      ],
      "schema:name": "Transect Rate, Mapping Rate or Step Size",
      "schema:value": "N/A \u2014 spot mode"
    }
  ],
  "ada:spotDiameterMeasured": -9999
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Nakanishi2022> a ada:LAICPMSTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/preAnalysisImagingAndScreening>,
        <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/transectRateMappingRateOrStepSize> ;
    schema1:measurementTechnique <ex:laQicpmsTAPP-Nakanishi2022> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially — the contributing counts are stated per grain, the reported ratios being \"the mean Re/Os abundance ratios for each of the 1–3 analytical spots measured by LA-ICP-MS\" (p.8). No acceptance or rejection rule is stated for the LA data; the 233/235 > 0.2 rejection (p.4) is a rule for the N-TIMS Os measurements, not for these spot analyses, and is not borrowed" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "missing" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:combinedResults "per-grain mean Re/Os ratio for each metal grain in Table 3 (1–3 spots each)" ;
    ada:componentType "ada:LAICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "N — LODs not formally stated" ;
    ada:fundingSourceForAnalysis "JSPS Grant-in-Aid for Scientific Research (grants 26106002, 26220713, 16H04081, 19H00715, 19H01081, 20H04609)" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "all: 2SE of individual measurements — 'Analytical uncertainties accompanied with the data are 2SE of individual measurements' (p.4)" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "missing" ;
    ada:numberOfReplicates 1 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Labelled: metal grains by host chondrule within each section — e.g. \"N8_02 interior ch2-1\" with LA \"spot No.\" 201, 202; \"N8_05 margin ch1\"; isolated grain \"iso1\" (table p.6; p.4) — in the sections \"NWA801-3-8, NWA7184-29-9, and DHO1432-5-5\" (p.2)" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "N — the 2SE is stated for individual measurements (p.4), not for a standard" .

<ex:laQicpmsTAPP-Nakanishi2022> schema1:identifier "missing" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/preAnalysisImagingAndScreening> ;
    schema1:value "Secondary-electron imaging on the EPMA, used to place every spot — \"Based on the secondary electron images taken by EPMA, we selected analytical spots for LA-ICP-MS and sampling spots for micro-milling\" (p.4); the spots carry numbers (\"spot No.\" 201, 202 …) that tie the analyses back to those images (table p.6)" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/transectRateMappingRateOrStepSize> a schema1:PropertyValue ;
    schema1:name "Transect Rate, Mapping Rate or Step Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/transectRateMappingRateOrStepSize> ;
    schema1:value "N/A — spot mode" .


```


### detail example Liu2024
detail instance derived from Liu et al. 2024 (JAAS 39) Extraterrestrial samples (Li-borate flux glass) Spot analysis fs-LA-Q-ICP-MS Chinese Academy of Sciences.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Liu2024",
  "@type": [
    "ada:LAICPMSTabular"
  ],
  "ada:componentType": "ada:LAICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laQicpmsTAPP-Liu2024",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Strategy Priority Research Program (Category B) of Chinese Academy of Sciences (XDB0710000); NSFC 42073022",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only — reference-material fusion glasses by name (JB-1b, GSR-3, AGV-2, AC-E, GSR-1, W-2A; BHVO-2 glass, p.3); \"Nine spot analyses ... were arranged in a grid\" per glass (p.5), unlabelled",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "ThO/Th = measured at <0.3%; U/Th = 0.95–1.05 (on NIST SRM 612)",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": 9,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": "N — ablation lasted 45 s (§2.2); the integration interval is not stated",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially — each reported value is the mean of a stated count, \"fs-LA-ICP-MS (n = 9 spots)\" against \"SN-ICP-MS (n = 5)\" (Table 2, p.8), with a 95% confidence interval. No acceptance or rejection rule, and no acquired-versus-included count, is stated",
  "ada:combinedResults": "each sample in Table 2 (n = 9 spots)",
  "ada:detectionLimit": "all: 0.005–23.5 µg g⁻¹ — LODs of 32 elements in lithium borate glass BHVO-2 (Table S2); 0.007–0.45 µg g⁻¹ calculated for NIST 610 (§3.2)",
  "ada:limitOfQuantificationMethod": "V, Co, Zn, Ba, La, Ce, Ta, U: blank value + 10SD (IUPAC Gold Book); other: 3.3 × LOD — §3.2",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "AC-E, GSR-1, JB-1b, GSR-3, AGV-2, W-2A [all: RSD better than 10% for most elements] — §3.5, Fig. 5b; higher RSDs for Zn in GSR-1, Tm, Yb and Lu in GSR-3, Lu in AGV-2, and Ta and U in W-2A",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "AC-E, GSR-1, JB-1b, GSR-3, AGV-2, W-2A [all: within 10% of the GeoReM reference values for most trace elements] — §3.5, Fig. 5a; discrepancies >15% for Co in AGV-2, JB-1b and W-2A, Ni in JB-1b, Cu in AGV-2 and JB-1b, Zn and Hf in GSR-1",
  "ada:goodnessOfFitOrDispersionStatistic": "all: relative standard deviation — 'relative standard deviations are reported as the precision measure'",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsTAPP/preAnalysisImagingAndScreening",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/preAnalysisImagingAndScreening"
        }
      ],
      "schema:name": "Pre-Analysis Imaging and Screening",
      "schema:value": "N — the fused glass discs are prepared for XRF and then ablated directly; no imaging or screening step is described before the LA-ICP-MS spots, whose grid is laid out to cover the whole disc (p.5)"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/transectRateMappingRateOrStepSize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/transectRateMappingRateOrStepSize"
        }
      ],
      "schema:name": "Transect Rate, Mapping Rate or Step Size",
      "schema:value": "N/A — spot mode"
    }
  ],
  "ada:spotDiameterMeasured": -9999
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Liu2024",
  "@type": [
    "ada:LAICPMSTabular"
  ],
  "ada:componentType": "ada:LAICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laQicpmsTAPP-Liu2024",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Strategy Priority Research Program (Category B) of Chinese Academy of Sciences (XDB0710000); NSFC 42073022",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only \u2014 reference-material fusion glasses by name (JB-1b, GSR-3, AGV-2, AC-E, GSR-1, W-2A; BHVO-2 glass, p.3); \"Nine spot analyses ... were arranged in a grid\" per glass (p.5), unlabelled",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "ThO/Th = measured at <0.3%; U/Th = 0.95\u20131.05 (on NIST SRM 612)",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": 9,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": "N \u2014 ablation lasted 45 s (\u00a72.2); the integration interval is not stated",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially \u2014 each reported value is the mean of a stated count, \"fs-LA-ICP-MS (n = 9 spots)\" against \"SN-ICP-MS (n = 5)\" (Table 2, p.8), with a 95% confidence interval. No acceptance or rejection rule, and no acquired-versus-included count, is stated",
  "ada:combinedResults": "each sample in Table 2 (n = 9 spots)",
  "ada:detectionLimit": "all: 0.005\u201323.5 \u00b5g g\u207b\u00b9 \u2014 LODs of 32 elements in lithium borate glass BHVO-2 (Table S2); 0.007\u20130.45 \u00b5g g\u207b\u00b9 calculated for NIST 610 (\u00a73.2)",
  "ada:limitOfQuantificationMethod": "V, Co, Zn, Ba, La, Ce, Ta, U: blank value + 10SD (IUPAC Gold Book); other: 3.3 \u00d7 LOD \u2014 \u00a73.2",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "AC-E, GSR-1, JB-1b, GSR-3, AGV-2, W-2A [all: RSD better than 10% for most elements] \u2014 \u00a73.5, Fig. 5b; higher RSDs for Zn in GSR-1, Tm, Yb and Lu in GSR-3, Lu in AGV-2, and Ta and U in W-2A",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "AC-E, GSR-1, JB-1b, GSR-3, AGV-2, W-2A [all: within 10% of the GeoReM reference values for most trace elements] \u2014 \u00a73.5, Fig. 5a; discrepancies >15% for Co in AGV-2, JB-1b and W-2A, Ni in JB-1b, Cu in AGV-2 and JB-1b, Zn and Hf in GSR-1",
  "ada:goodnessOfFitOrDispersionStatistic": "all: relative standard deviation \u2014 'relative standard deviations are reported as the precision measure'",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsTAPP/preAnalysisImagingAndScreening",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/preAnalysisImagingAndScreening"
        }
      ],
      "schema:name": "Pre-Analysis Imaging and Screening",
      "schema:value": "N \u2014 the fused glass discs are prepared for XRF and then ablated directly; no imaging or screening step is described before the LA-ICP-MS spots, whose grid is laid out to cover the whole disc (p.5)"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/transectRateMappingRateOrStepSize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/transectRateMappingRateOrStepSize"
        }
      ],
      "schema:name": "Transect Rate, Mapping Rate or Step Size",
      "schema:value": "N/A \u2014 spot mode"
    }
  ],
  "ada:spotDiameterMeasured": -9999
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Liu2024> a ada:LAICPMSTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/preAnalysisImagingAndScreening>,
        <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/transectRateMappingRateOrStepSize> ;
    schema1:measurementTechnique <ex:laQicpmsTAPP-Liu2024> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially — each reported value is the mean of a stated count, \"fs-LA-ICP-MS (n = 9 spots)\" against \"SN-ICP-MS (n = 5)\" (Table 2, p.8), with a 95% confidence interval. No acceptance or rejection rule, and no acquired-versus-included count, is stated" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "AC-E, GSR-1, JB-1b, GSR-3, AGV-2, W-2A [all: within 10% of the GeoReM reference values for most trace elements] — §3.5, Fig. 5a; discrepancies >15% for Co in AGV-2, JB-1b and W-2A, Ni in JB-1b, Cu in AGV-2 and JB-1b, Zn and Hf in GSR-1" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:combinedResults "each sample in Table 2 (n = 9 spots)" ;
    ada:componentType "ada:LAICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "all: 0.005–23.5 µg g⁻¹ — LODs of 32 elements in lithium borate glass BHVO-2 (Table S2); 0.007–0.45 µg g⁻¹ calculated for NIST 610 (§3.2)" ;
    ada:fundingSourceForAnalysis "Strategy Priority Research Program (Category B) of Chinese Academy of Sciences (XDB0710000); NSFC 42073022" ;
    ada:goodnessOfFitOrDispersionStatistic "all: relative standard deviation — 'relative standard deviations are reported as the precision measure'" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "V, Co, Zn, Ba, La, Ce, Ta, U: blank value + 10SD (IUPAC Gold Book); other: 3.3 × LOD — §3.2" ;
    ada:mappingArea "missing" ;
    ada:numberOfReplicates 9 ;
    ada:oxideProduction "ThO/Th = measured at <0.3%; U/Th = 0.95–1.05 (on NIST SRM 612)" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Sample name only — reference-material fusion glasses by name (JB-1b, GSR-3, AGV-2, AC-E, GSR-1, W-2A; BHVO-2 glass, p.3); \"Nine spot analyses ... were arranged in a grid\" per glass (p.5), unlabelled" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime "N — ablation lasted 45 s (§2.2); the integration interval is not stated" ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "AC-E, GSR-1, JB-1b, GSR-3, AGV-2, W-2A [all: RSD better than 10% for most elements] — §3.5, Fig. 5b; higher RSDs for Zn in GSR-1, Tm, Yb and Lu in GSR-3, Lu in AGV-2, and Ta and U in W-2A" .

<ex:laQicpmsTAPP-Liu2024> schema1:identifier "missing" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/preAnalysisImagingAndScreening> ;
    schema1:value "N — the fused glass discs are prepared for XRF and then ablated directly; no imaging or screening step is described before the LA-ICP-MS spots, whose grid is laid out to cover the whole disc (p.5)" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/transectRateMappingRateOrStepSize> a schema1:PropertyValue ;
    schema1:name "Transect Rate, Mapping Rate or Step Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/transectRateMappingRateOrStepSize> ;
    schema1:value "N/A — spot mode" .


```


### detail example Liu2025
detail instance derived from Liu et al. 2025 (GCA 393) Experimental silicate glass Spot analysis ns-LA-Q-ICP-MS Guangzhou Inst. Geochemistry.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Liu2025",
  "@type": [
    "ada:LAICPMSTabular"
  ],
  "ada:componentType": "ada:LAICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laQicpmsTAPP-Liu2025",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Strategic Priority Research Program (B) of CAS (XDB0840200); NSFC 92062222, 42073057, 42250710679, 42250202, 42273023",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only — experimental run products by run number, e.g. \"D-2\", \"D-4\", \"D-34\", \"D-46\" (Table 1, p.3) and \"DAC-41\" (p.4); spots within a run are not labelled",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "N — no rule for admitting or rejecting individual results is stated. The one documented exclusion is at sample level and before analysis: \"Capsules that had lost significant weight were discarded\" after the leak check (p.2)",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": "Au: ~0.01 ppm; Cu: ~0.1 ppm — 'Detection limits for Au and Cu in silicate melts were ~ 0.01 ppm and ~ 0.1 ppm, respectively' (§2.2.2)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "N — data from the two laboratories 'exhibited good agreement, any differences being below 10 %' (§2.2.2)",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsTAPP/preAnalysisImagingAndScreening",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/preAnalysisImagingAndScreening"
        }
      ],
      "schema:name": "Pre-Analysis Imaging and Screening",
      "schema:value": "Optical microscopy, then EMP — \"Following examination by optical microscopy to ascertain the integrity of the experiments and the state of the oxygen buffers, the solid components of the run products were analysed for major elements, S and Cu, using a JEOL JXA-8230 electron microprobe (EMP)\" (p.2); those EMP values are then the internal standards for the LA data, \"with Si and Fe obtained from EMP analyses as the internal standards\" (p.4)"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/transectRateMappingRateOrStepSize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/transectRateMappingRateOrStepSize"
        }
      ],
      "schema:name": "Transect Rate, Mapping Rate or Step Size",
      "schema:value": "N/A — spot mode"
    }
  ],
  "ada:spotDiameterMeasured": -9999
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Liu2025",
  "@type": [
    "ada:LAICPMSTabular"
  ],
  "ada:componentType": "ada:LAICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laQicpmsTAPP-Liu2025",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Strategic Priority Research Program (B) of CAS (XDB0840200); NSFC 92062222, 42073057, 42250710679, 42250202, 42273023",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only \u2014 experimental run products by run number, e.g. \"D-2\", \"D-4\", \"D-34\", \"D-46\" (Table 1, p.3) and \"DAC-41\" (p.4); spots within a run are not labelled",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 no rule for admitting or rejecting individual results is stated. The one documented exclusion is at sample level and before analysis: \"Capsules that had lost significant weight were discarded\" after the leak check (p.2)",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": "Au: ~0.01 ppm; Cu: ~0.1 ppm \u2014 'Detection limits for Au and Cu in silicate melts were ~ 0.01 ppm and ~ 0.1 ppm, respectively' (\u00a72.2.2)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "N \u2014 data from the two laboratories 'exhibited good agreement, any differences being below 10 %' (\u00a72.2.2)",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsTAPP/preAnalysisImagingAndScreening",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/preAnalysisImagingAndScreening"
        }
      ],
      "schema:name": "Pre-Analysis Imaging and Screening",
      "schema:value": "Optical microscopy, then EMP \u2014 \"Following examination by optical microscopy to ascertain the integrity of the experiments and the state of the oxygen buffers, the solid components of the run products were analysed for major elements, S and Cu, using a JEOL JXA-8230 electron microprobe (EMP)\" (p.2); those EMP values are then the internal standards for the LA data, \"with Si and Fe obtained from EMP analyses as the internal standards\" (p.4)"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/transectRateMappingRateOrStepSize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/transectRateMappingRateOrStepSize"
        }
      ],
      "schema:name": "Transect Rate, Mapping Rate or Step Size",
      "schema:value": "N/A \u2014 spot mode"
    }
  ],
  "ada:spotDiameterMeasured": -9999
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Liu2025> a ada:LAICPMSTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/preAnalysisImagingAndScreening>,
        <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/transectRateMappingRateOrStepSize> ;
    schema1:measurementTechnique <ex:laQicpmsTAPP-Liu2025> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — no rule for admitting or rejecting individual results is stated. The one documented exclusion is at sample level and before analysis: \"Capsules that had lost significant weight were discarded\" after the leak check (p.2)" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "N — data from the two laboratories 'exhibited good agreement, any differences being below 10 %' (§2.2.2)" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:combinedResults "missing" ;
    ada:componentType "ada:LAICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "Au: ~0.01 ppm; Cu: ~0.1 ppm — 'Detection limits for Au and Cu in silicate melts were ~ 0.01 ppm and ~ 0.1 ppm, respectively' (§2.2.2)" ;
    ada:fundingSourceForAnalysis "Strategic Priority Research Program (B) of CAS (XDB0840200); NSFC 92062222, 42073057, 42250710679, 42250202, 42273023" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Sample name only — experimental run products by run number, e.g. \"D-2\", \"D-4\", \"D-34\", \"D-46\" (Table 1, p.3) and \"DAC-41\" (p.4); spots within a run are not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<ex:laQicpmsTAPP-Liu2025> schema1:identifier "missing" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/preAnalysisImagingAndScreening> ;
    schema1:value "Optical microscopy, then EMP — \"Following examination by optical microscopy to ascertain the integrity of the experiments and the state of the oxygen buffers, the solid components of the run products were analysed for major elements, S and Cu, using a JEOL JXA-8230 electron microprobe (EMP)\" (p.2); those EMP values are then the internal standards for the LA data, \"with Si and Fe obtained from EMP analyses as the internal standards\" (p.4)" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/transectRateMappingRateOrStepSize> a schema1:PropertyValue ;
    schema1:name "Transect Rate, Mapping Rate or Step Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/transectRateMappingRateOrStepSize> ;
    schema1:value "N/A — spot mode" .


```


### detail example Liu2025-2
detail instance derived from Liu et al. 2025 (GCA 393) Experimental sulfide Spot analysis ns-LA-Q-ICP-MS Guangzhou Inst. Geochemistry.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Liu2025-2",
  "@type": [
    "ada:LAICPMSTabular"
  ],
  "ada:componentType": "ada:LAICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laQicpmsTAPP-Liu2025-2",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Strategic Priority Research Program (B) of CAS (XDB0840200); NSFC 92062222, 42073057, 42250710679, 42250202, 42273023",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only — experimental run products by run number, e.g. \"D-2\", \"D-4\", \"D-34\", \"D-46\" (Table 1, p.3) and \"DAC-41\" (p.4); spots within a run are not labelled",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "N — no rule for admitting or rejecting individual results is stated. The one documented exclusion is at sample level and before analysis: \"Capsules that had lost significant weight were discarded\" after the leak check (p.2)",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": "N — detection limits are stated for silicate melts only (§2.2.2)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "N — data from the two laboratories 'exhibited good agreement, any differences being below 10 %' (§2.2.2)",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsTAPP/preAnalysisImagingAndScreening",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/preAnalysisImagingAndScreening"
        }
      ],
      "schema:name": "Pre-Analysis Imaging and Screening",
      "schema:value": "Optical microscopy, then EMP — \"Following examination by optical microscopy to ascertain the integrity of the experiments and the state of the oxygen buffers, the solid components of the run products were analysed for major elements, S and Cu, using a JEOL JXA-8230 electron microprobe (EMP)\" (p.2); those EMP values are then the internal standards for the LA data, \"with Si and Fe obtained from EMP analyses as the internal standards\" (p.4)"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/transectRateMappingRateOrStepSize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/transectRateMappingRateOrStepSize"
        }
      ],
      "schema:name": "Transect Rate, Mapping Rate or Step Size",
      "schema:value": "N/A — spot mode"
    }
  ],
  "ada:spotDiameterMeasured": -9999
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Liu2025-2",
  "@type": [
    "ada:LAICPMSTabular"
  ],
  "ada:componentType": "ada:LAICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laQicpmsTAPP-Liu2025-2",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Strategic Priority Research Program (B) of CAS (XDB0840200); NSFC 92062222, 42073057, 42250710679, 42250202, 42273023",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only \u2014 experimental run products by run number, e.g. \"D-2\", \"D-4\", \"D-34\", \"D-46\" (Table 1, p.3) and \"DAC-41\" (p.4); spots within a run are not labelled",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 no rule for admitting or rejecting individual results is stated. The one documented exclusion is at sample level and before analysis: \"Capsules that had lost significant weight were discarded\" after the leak check (p.2)",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": "N \u2014 detection limits are stated for silicate melts only (\u00a72.2.2)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "N \u2014 data from the two laboratories 'exhibited good agreement, any differences being below 10 %' (\u00a72.2.2)",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsTAPP/preAnalysisImagingAndScreening",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/preAnalysisImagingAndScreening"
        }
      ],
      "schema:name": "Pre-Analysis Imaging and Screening",
      "schema:value": "Optical microscopy, then EMP \u2014 \"Following examination by optical microscopy to ascertain the integrity of the experiments and the state of the oxygen buffers, the solid components of the run products were analysed for major elements, S and Cu, using a JEOL JXA-8230 electron microprobe (EMP)\" (p.2); those EMP values are then the internal standards for the LA data, \"with Si and Fe obtained from EMP analyses as the internal standards\" (p.4)"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/transectRateMappingRateOrStepSize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/transectRateMappingRateOrStepSize"
        }
      ],
      "schema:name": "Transect Rate, Mapping Rate or Step Size",
      "schema:value": "N/A \u2014 spot mode"
    }
  ],
  "ada:spotDiameterMeasured": -9999
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Liu2025-2> a ada:LAICPMSTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/preAnalysisImagingAndScreening>,
        <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/transectRateMappingRateOrStepSize> ;
    schema1:measurementTechnique <ex:laQicpmsTAPP-Liu2025-2> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — no rule for admitting or rejecting individual results is stated. The one documented exclusion is at sample level and before analysis: \"Capsules that had lost significant weight were discarded\" after the leak check (p.2)" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "N — data from the two laboratories 'exhibited good agreement, any differences being below 10 %' (§2.2.2)" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:combinedResults "missing" ;
    ada:componentType "ada:LAICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "N — detection limits are stated for silicate melts only (§2.2.2)" ;
    ada:fundingSourceForAnalysis "Strategic Priority Research Program (B) of CAS (XDB0840200); NSFC 92062222, 42073057, 42250710679, 42250202, 42273023" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Sample name only — experimental run products by run number, e.g. \"D-2\", \"D-4\", \"D-34\", \"D-46\" (Table 1, p.3) and \"DAC-41\" (p.4); spots within a run are not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<ex:laQicpmsTAPP-Liu2025-2> schema1:identifier "missing" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/preAnalysisImagingAndScreening> ;
    schema1:value "Optical microscopy, then EMP — \"Following examination by optical microscopy to ascertain the integrity of the experiments and the state of the oxygen buffers, the solid components of the run products were analysed for major elements, S and Cu, using a JEOL JXA-8230 electron microprobe (EMP)\" (p.2); those EMP values are then the internal standards for the LA data, \"with Si and Fe obtained from EMP analyses as the internal standards\" (p.4)" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/transectRateMappingRateOrStepSize> a schema1:PropertyValue ;
    schema1:name "Transect Rate, Mapping Rate or Step Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/transectRateMappingRateOrStepSize> ;
    schema1:value "N/A — spot mode" .


```


### detail example Liu2016
detail instance derived from Liu et al. 2016 (M&PS 51) Tissint martian meteorite Silicates, oxides & glass Spot analysis LA-Q-ICP-MS Virginia Tech.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Liu2016",
  "@type": [
    "ada:LAICPMSTabular"
  ],
  "ada:componentType": "ada:LAICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laQicpmsTAPP-Liu2016",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA Cosmochemistry NNX11AG58G and NNN13D465T; NSF EAR-1226270 and EAR-1019770 — acknowledgements; Y.L. was also supported by the Jet Propulsion Laboratory",
  "ada:sampleName": "Tissint Martian meteorite",
  "ada:samplingUnitName": "Labelled sections: \"UT1 to UT3 (formerly referred to as MT-1, MT-2, MT-3)\" (p.3). LA-ICP-MS results are averages (\"n = 7\", \"n = 13\", table p.9); individual analyses are in \"Table S1 in supporting information\" (p.7), not in the archived PDF",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "N — not stated",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": "N — not stated",
  "ada:transectLength": "N/A — spot analysis",
  "ada:mappingArea": "N/A — spot analysis",
  "ada:signalIntegrationTime": "N — not stated",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially — the reported values are means of stated counts (\"n = 7\", \"n = 13\", table p.9). No acceptance or rejection rule is stated; the plateau-region screening of each spot is signal-based and is recorded under Spike / Outlier Filtering Approach",
  "ada:combinedResults": "glass-inclusion average (n = 7); impact-melt glass average (n = 13) — Table 3",
  "ada:detectionLimit": "K: 16.7; Ti: 1.12; V: 3; Mn: 4.54; Zn: 0.69; Sr: 0.147; Nb: 0.103; Ba: 0.049; La: 0.113; Ce: 1.102; Pr: 0.580; Nd: 0.129; Sm: 0.457; Eu: 0.228; Gd: 0.453; Tb: 0.079; Dy: 0.222; Ho: 0.135; Er: 0.353; Tm: 0.630; Yb: 0.364; Lu: 0.117; Hf: 0.365; Ta: 0.333; W: 0.254; other: N — ppm; Table 3 'LOD' column, beside a single glass-inclusion analysis (n = 1)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "N — oxide-total normalization 'generally agrees within <10% with the method using EMP CaO or MgO values as internal standards' (Methods, p.4)",
  "ada:goodnessOfFitOrDispersionStatistic": "all: 1σ, one standard deviation of the average — Table 3 note b: '1σ is 1 standard deviation of the average'",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsTAPP/preAnalysisImagingAndScreening",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/preAnalysisImagingAndScreening"
        }
      ],
      "schema:name": "Pre-Analysis Imaging and Screening",
      "schema:value": "Petrographic microscopy, SEM and EMP — \"The petrography of these sections was examined using a petrographic microscope and a scanning electron microscope\", followed by BSE images and element maps (p.3); the EMP results then serve as internal standards for the ablation data, which are normalised using \"EMP CaO or MgO values\" for silicates and \"40Ca counts to CaO concentrations from the EMP analysis\" for phosphate (p.4)"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/transectRateMappingRateOrStepSize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/transectRateMappingRateOrStepSize"
        }
      ],
      "schema:name": "Transect Rate, Mapping Rate or Step Size",
      "schema:value": "N/A — spot analysis"
    }
  ],
  "ada:spotDiameterMeasured": -9999
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Liu2016",
  "@type": [
    "ada:LAICPMSTabular"
  ],
  "ada:componentType": "ada:LAICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laQicpmsTAPP-Liu2016",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA Cosmochemistry NNX11AG58G and NNN13D465T; NSF EAR-1226270 and EAR-1019770 \u2014 acknowledgements; Y.L. was also supported by the Jet Propulsion Laboratory",
  "ada:sampleName": "Tissint Martian meteorite",
  "ada:samplingUnitName": "Labelled sections: \"UT1 to UT3 (formerly referred to as MT-1, MT-2, MT-3)\" (p.3). LA-ICP-MS results are averages (\"n = 7\", \"n = 13\", table p.9); individual analyses are in \"Table S1 in supporting information\" (p.7), not in the archived PDF",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "N \u2014 not stated",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": "N \u2014 not stated",
  "ada:transectLength": "N/A \u2014 spot analysis",
  "ada:mappingArea": "N/A \u2014 spot analysis",
  "ada:signalIntegrationTime": "N \u2014 not stated",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially \u2014 the reported values are means of stated counts (\"n = 7\", \"n = 13\", table p.9). No acceptance or rejection rule is stated; the plateau-region screening of each spot is signal-based and is recorded under Spike / Outlier Filtering Approach",
  "ada:combinedResults": "glass-inclusion average (n = 7); impact-melt glass average (n = 13) \u2014 Table 3",
  "ada:detectionLimit": "K: 16.7; Ti: 1.12; V: 3; Mn: 4.54; Zn: 0.69; Sr: 0.147; Nb: 0.103; Ba: 0.049; La: 0.113; Ce: 1.102; Pr: 0.580; Nd: 0.129; Sm: 0.457; Eu: 0.228; Gd: 0.453; Tb: 0.079; Dy: 0.222; Ho: 0.135; Er: 0.353; Tm: 0.630; Yb: 0.364; Lu: 0.117; Hf: 0.365; Ta: 0.333; W: 0.254; other: N \u2014 ppm; Table 3 'LOD' column, beside a single glass-inclusion analysis (n = 1)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "N \u2014 oxide-total normalization 'generally agrees within <10% with the method using EMP CaO or MgO values as internal standards' (Methods, p.4)",
  "ada:goodnessOfFitOrDispersionStatistic": "all: 1\u03c3, one standard deviation of the average \u2014 Table 3 note b: '1\u03c3 is 1 standard deviation of the average'",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsTAPP/preAnalysisImagingAndScreening",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/preAnalysisImagingAndScreening"
        }
      ],
      "schema:name": "Pre-Analysis Imaging and Screening",
      "schema:value": "Petrographic microscopy, SEM and EMP \u2014 \"The petrography of these sections was examined using a petrographic microscope and a scanning electron microscope\", followed by BSE images and element maps (p.3); the EMP results then serve as internal standards for the ablation data, which are normalised using \"EMP CaO or MgO values\" for silicates and \"40Ca counts to CaO concentrations from the EMP analysis\" for phosphate (p.4)"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/transectRateMappingRateOrStepSize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/transectRateMappingRateOrStepSize"
        }
      ],
      "schema:name": "Transect Rate, Mapping Rate or Step Size",
      "schema:value": "N/A \u2014 spot analysis"
    }
  ],
  "ada:spotDiameterMeasured": -9999
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Liu2016> a ada:LAICPMSTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/preAnalysisImagingAndScreening>,
        <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/transectRateMappingRateOrStepSize> ;
    schema1:measurementTechnique <ex:laQicpmsTAPP-Liu2016> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially — the reported values are means of stated counts (\"n = 7\", \"n = 13\", table p.9). No acceptance or rejection rule is stated; the plateau-region screening of each spot is signal-based and is recorded under Spike / Outlier Filtering Approach" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "N — oxide-total normalization 'generally agrees within <10% with the method using EMP CaO or MgO values as internal standards' (Methods, p.4)" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:combinedResults "glass-inclusion average (n = 7); impact-melt glass average (n = 13) — Table 3" ;
    ada:componentType "ada:LAICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "K: 16.7; Ti: 1.12; V: 3; Mn: 4.54; Zn: 0.69; Sr: 0.147; Nb: 0.103; Ba: 0.049; La: 0.113; Ce: 1.102; Pr: 0.580; Nd: 0.129; Sm: 0.457; Eu: 0.228; Gd: 0.453; Tb: 0.079; Dy: 0.222; Ho: 0.135; Er: 0.353; Tm: 0.630; Yb: 0.364; Lu: 0.117; Hf: 0.365; Ta: 0.333; W: 0.254; other: N — ppm; Table 3 'LOD' column, beside a single glass-inclusion analysis (n = 1)" ;
    ada:fundingSourceForAnalysis "NASA Cosmochemistry NNX11AG58G and NNN13D465T; NSF EAR-1226270 and EAR-1019770 — acknowledgements; Y.L. was also supported by the Jet Propulsion Laboratory" ;
    ada:goodnessOfFitOrDispersionStatistic "all: 1σ, one standard deviation of the average — Table 3 note b: '1σ is 1 standard deviation of the average'" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "N/A — spot analysis" ;
    ada:numberOfReplicates "N — not stated" ;
    ada:oxideProduction "N — not stated" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "Tissint Martian meteorite" ;
    ada:samplingUnitName "Labelled sections: \"UT1 to UT3 (formerly referred to as MT-1, MT-2, MT-3)\" (p.3). LA-ICP-MS results are averages (\"n = 7\", \"n = 13\", table p.9); individual analyses are in \"Table S1 in supporting information\" (p.7), not in the archived PDF" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime "N — not stated" ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength "N/A — spot analysis" ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<ex:laQicpmsTAPP-Liu2016> schema1:identifier "missing" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/preAnalysisImagingAndScreening> ;
    schema1:value "Petrographic microscopy, SEM and EMP — \"The petrography of these sections was examined using a petrographic microscope and a scanning electron microscope\", followed by BSE images and element maps (p.3); the EMP results then serve as internal standards for the ablation data, which are normalised using \"EMP CaO or MgO values\" for silicates and \"40Ca counts to CaO concentrations from the EMP analysis\" for phosphate (p.4)" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/transectRateMappingRateOrStepSize> a schema1:PropertyValue ;
    schema1:name "Transect Rate, Mapping Rate or Step Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/transectRateMappingRateOrStepSize> ;
    schema1:value "N/A — spot analysis" .


```


### detail example Liu2016-2
detail instance derived from Liu et al. 2016 (M&PS 51) Tissint martian meteorite Phosphate (merrillite) Spot analysis LA-Q-ICP-MS Virginia Tech.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Liu2016-2",
  "@type": [
    "ada:LAICPMSTabular"
  ],
  "ada:componentType": "ada:LAICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laQicpmsTAPP-Liu2016-2",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA Cosmochemistry NNX11AG58G and NNN13D465T; NSF EAR-1226270 and EAR-1019770 — acknowledgements; Y.L. was also supported by the Jet Propulsion Laboratory",
  "ada:sampleName": "Tissint Martian meteorite",
  "ada:samplingUnitName": "Labelled sections: \"UT1 to UT3 (formerly referred to as MT-1, MT-2, MT-3)\" (p.3). LA-ICP-MS results are averages (\"n = 7\", \"n = 13\", table p.9); individual analyses are in \"Table S1 in supporting information\" (p.7), not in the archived PDF",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "N — not stated",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": "N — not stated",
  "ada:transectLength": "N/A — spot analysis",
  "ada:mappingArea": "N/A — spot analysis",
  "ada:signalIntegrationTime": "N — not stated",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "N — the counts 'n = 7' and 'n = 13' (Table 3) are the two glass averages, not merrillite; no contributing count or rule is stated for the merrillite analyses",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": "N — Table 3's LODs are for the glasses",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsTAPP/preAnalysisImagingAndScreening",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/preAnalysisImagingAndScreening"
        }
      ],
      "schema:name": "Pre-Analysis Imaging and Screening",
      "schema:value": "Petrographic microscopy, SEM and EMP — \"The petrography of these sections was examined using a petrographic microscope and a scanning electron microscope\", followed by BSE images and element maps (p.3); the EMP results then serve as internal standards for the ablation data, which are normalised using \"EMP CaO or MgO values\" for silicates and \"40Ca counts to CaO concentrations from the EMP analysis\" for phosphate (p.4)"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/transectRateMappingRateOrStepSize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/transectRateMappingRateOrStepSize"
        }
      ],
      "schema:name": "Transect Rate, Mapping Rate or Step Size",
      "schema:value": "N/A — spot analysis"
    }
  ],
  "ada:spotDiameterMeasured": -9999
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Liu2016-2",
  "@type": [
    "ada:LAICPMSTabular"
  ],
  "ada:componentType": "ada:LAICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laQicpmsTAPP-Liu2016-2",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA Cosmochemistry NNX11AG58G and NNN13D465T; NSF EAR-1226270 and EAR-1019770 \u2014 acknowledgements; Y.L. was also supported by the Jet Propulsion Laboratory",
  "ada:sampleName": "Tissint Martian meteorite",
  "ada:samplingUnitName": "Labelled sections: \"UT1 to UT3 (formerly referred to as MT-1, MT-2, MT-3)\" (p.3). LA-ICP-MS results are averages (\"n = 7\", \"n = 13\", table p.9); individual analyses are in \"Table S1 in supporting information\" (p.7), not in the archived PDF",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "N \u2014 not stated",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": "N \u2014 not stated",
  "ada:transectLength": "N/A \u2014 spot analysis",
  "ada:mappingArea": "N/A \u2014 spot analysis",
  "ada:signalIntegrationTime": "N \u2014 not stated",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 the counts 'n = 7' and 'n = 13' (Table 3) are the two glass averages, not merrillite; no contributing count or rule is stated for the merrillite analyses",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": "N \u2014 Table 3's LODs are for the glasses",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsTAPP/preAnalysisImagingAndScreening",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/preAnalysisImagingAndScreening"
        }
      ],
      "schema:name": "Pre-Analysis Imaging and Screening",
      "schema:value": "Petrographic microscopy, SEM and EMP \u2014 \"The petrography of these sections was examined using a petrographic microscope and a scanning electron microscope\", followed by BSE images and element maps (p.3); the EMP results then serve as internal standards for the ablation data, which are normalised using \"EMP CaO or MgO values\" for silicates and \"40Ca counts to CaO concentrations from the EMP analysis\" for phosphate (p.4)"
    },
    {
      "@id": "ada:parameter/laQicpmsTAPP/transectRateMappingRateOrStepSize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/transectRateMappingRateOrStepSize"
        }
      ],
      "schema:name": "Transect Rate, Mapping Rate or Step Size",
      "schema:value": "N/A \u2014 spot analysis"
    }
  ],
  "ada:spotDiameterMeasured": -9999
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Liu2016-2> a ada:LAICPMSTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/preAnalysisImagingAndScreening>,
        <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/transectRateMappingRateOrStepSize> ;
    schema1:measurementTechnique <ex:laQicpmsTAPP-Liu2016-2> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — the counts 'n = 7' and 'n = 13' (Table 3) are the two glass averages, not merrillite; no contributing count or rule is stated for the merrillite analyses" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "missing" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:combinedResults "missing" ;
    ada:componentType "ada:LAICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "N — Table 3's LODs are for the glasses" ;
    ada:fundingSourceForAnalysis "NASA Cosmochemistry NNX11AG58G and NNN13D465T; NSF EAR-1226270 and EAR-1019770 — acknowledgements; Y.L. was also supported by the Jet Propulsion Laboratory" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "N/A — spot analysis" ;
    ada:numberOfReplicates "N — not stated" ;
    ada:oxideProduction "N — not stated" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "Tissint Martian meteorite" ;
    ada:samplingUnitName "Labelled sections: \"UT1 to UT3 (formerly referred to as MT-1, MT-2, MT-3)\" (p.3). LA-ICP-MS results are averages (\"n = 7\", \"n = 13\", table p.9); individual analyses are in \"Table S1 in supporting information\" (p.7), not in the archived PDF" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime "N — not stated" ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength "N/A — spot analysis" ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<ex:laQicpmsTAPP-Liu2016-2> schema1:identifier "missing" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/preAnalysisImagingAndScreening> ;
    schema1:value "Petrographic microscopy, SEM and EMP — \"The petrography of these sections was examined using a petrographic microscope and a scanning electron microscope\", followed by BSE images and element maps (p.3); the EMP results then serve as internal standards for the ablation data, which are normalised using \"EMP CaO or MgO values\" for silicates and \"40Ca counts to CaO concentrations from the EMP analysis\" for phosphate (p.4)" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/transectRateMappingRateOrStepSize> a schema1:PropertyValue ;
    schema1:name "Transect Rate, Mapping Rate or Step Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/transectRateMappingRateOrStepSize> ;
    schema1:value "N/A — spot analysis" .


```


### detail example P6
detail instance derived from Wu+etal2023 | Analyte G2 + iCAP TQ ICP-MS/MS | IGGCAS.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-P6",
  "@type": [
    "ada:LAICPMSTabular"
  ],
  "ada:componentType": "ada:LAICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laQicpmsTAPP-P6",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "N — 20 analytical sessions over 3 months referenced, no identifier stated",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Xenotime XN02, MG-1, BS-1, XENOA, M1567; apatite Otter Lake, NW-1, MAP-3; two metamorphic garnets; NIST SRM 610",
  "ada:samplingUnitName": "Sample name only — \"Xenotime samples included BS-1, MG-1, XN02, XENOA and M1567; apatite samples included Otter Lake, NW-1 and MAP-3; and garnet samples included 14SA36 and 12QL59\" (p.9); spots are counted per sample, not labelled",
  "ada:spotDiameter": 50,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Acquired and included counts both stated: 'A total of 246 spot analyses were undertaken in 20 analytical sessions over 3 months, 236 of which yielded a weighted-mean age of 515.4 +/- 1.2 Ma'. The rejection rule itself is not stated",
  "ada:combinedResults": "the weighted-mean and isochron ages of each sample in Figs 8–10, for example the XN02 weighted-mean age (236 of 246 spots) and the weighted mean of 15 session ages (n = 15)",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "common-Hf-corrected single-spot age: 2SE, ~2.6%; other: N",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "MG-1, BS-1, XENOA, M1567 [common-Hf-corrected single-spot age: 1.5–8.1%]; Otter Lake, NW-1, MAP-3 [common-Hf-corrected single-spot age: 9.2–36.0%] — isochron age uncertainties of 3.5–10% for the garnet samples",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "MG-1, BS-1, XENOA, M1567 [common-Hf-corrected single-spot age: generally better than 1.5%] — against ID-TIMS U–Pb ages of the same reference materials",
  "ada:goodnessOfFitOrDispersionStatistic": "Lu-Hf isochron age, Lu-Hf weighted-mean age: MSWD; other: N — e.g. MSWD = 2.3 (n = 236, XN02) and MSWD = 0.6 (n = 15, weighted-mean Lu-Hf age 489.8 ± 2.2 Ma)",
  "ada:spotDiameterMeasured": -9999
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-P6",
  "@type": [
    "ada:LAICPMSTabular"
  ],
  "ada:componentType": "ada:LAICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laQicpmsTAPP-P6",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "N \u2014 20 analytical sessions over 3 months referenced, no identifier stated",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Xenotime XN02, MG-1, BS-1, XENOA, M1567; apatite Otter Lake, NW-1, MAP-3; two metamorphic garnets; NIST SRM 610",
  "ada:samplingUnitName": "Sample name only \u2014 \"Xenotime samples included BS-1, MG-1, XN02, XENOA and M1567; apatite samples included Otter Lake, NW-1 and MAP-3; and garnet samples included 14SA36 and 12QL59\" (p.9); spots are counted per sample, not labelled",
  "ada:spotDiameter": 50,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Acquired and included counts both stated: 'A total of 246 spot analyses were undertaken in 20 analytical sessions over 3 months, 236 of which yielded a weighted-mean age of 515.4 +/- 1.2 Ma'. The rejection rule itself is not stated",
  "ada:combinedResults": "the weighted-mean and isochron ages of each sample in Figs 8\u201310, for example the XN02 weighted-mean age (236 of 246 spots) and the weighted mean of 15 session ages (n = 15)",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "common-Hf-corrected single-spot age: 2SE, ~2.6%; other: N",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "MG-1, BS-1, XENOA, M1567 [common-Hf-corrected single-spot age: 1.5\u20138.1%]; Otter Lake, NW-1, MAP-3 [common-Hf-corrected single-spot age: 9.2\u201336.0%] \u2014 isochron age uncertainties of 3.5\u201310% for the garnet samples",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "MG-1, BS-1, XENOA, M1567 [common-Hf-corrected single-spot age: generally better than 1.5%] \u2014 against ID-TIMS U\u2013Pb ages of the same reference materials",
  "ada:goodnessOfFitOrDispersionStatistic": "Lu-Hf isochron age, Lu-Hf weighted-mean age: MSWD; other: N \u2014 e.g. MSWD = 2.3 (n = 236, XN02) and MSWD = 0.6 (n = 15, weighted-mean Lu-Hf age 489.8 \u00b1 2.2 Ma)",
  "ada:spotDiameterMeasured": -9999
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-P6> a ada:LAICPMSTabular ;
    schema1:measurementTechnique <ex:laQicpmsTAPP-P6> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Acquired and included counts both stated: 'A total of 246 spot analyses were undertaken in 20 analytical sessions over 3 months, 236 of which yielded a weighted-mean age of 515.4 +/- 1.2 Ma'. The rejection rule itself is not stated" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "MG-1, BS-1, XENOA, M1567 [common-Hf-corrected single-spot age: generally better than 1.5%] — against ID-TIMS U–Pb ages of the same reference materials" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:combinedResults "the weighted-mean and isochron ages of each sample in Figs 8–10, for example the XN02 weighted-mean age (236 of 246 spots) and the weighted mean of 15 session ages (n = 15)" ;
    ada:componentType "ada:LAICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "Lu-Hf isochron age, Lu-Hf weighted-mean age: MSWD; other: N — e.g. MSWD = 2.3 (n = 236, XN02) and MSWD = 0.6 (n = 15, weighted-mean Lu-Hf age 489.8 ± 2.2 Ma)" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "common-Hf-corrected single-spot age: 2SE, ~2.6%; other: N" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "Xenotime XN02, MG-1, BS-1, XENOA, M1567; apatite Otter Lake, NW-1, MAP-3; two metamorphic garnets; NIST SRM 610" ;
    ada:samplingUnitName "Sample name only — \"Xenotime samples included BS-1, MG-1, XN02, XENOA and M1567; apatite samples included Otter Lake, NW-1 and MAP-3; and garnet samples included 14SA36 and 12QL59\" (p.9); spots are counted per sample, not labelled" ;
    ada:sessionIdentifier "N — 20 analytical sessions over 3 months referenced, no identifier stated" ;
    ada:signalIntegrationTime -9999 ;
    ada:spotDiameter 50 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "MG-1, BS-1, XENOA, M1567 [common-Hf-corrected single-spot age: 1.5–8.1%]; Otter Lake, NW-1, MAP-3 [common-Hf-corrected single-spot age: 9.2–36.0%] — isochron age uncertainties of 3.5–10% for the garnet samples" .

<ex:laQicpmsTAPP-P6> schema1:identifier "missing" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: LA-Q-ICP-MS Analysis Detail
description: Dataset-level analysis-instance detail for LA-Q-ICP-MS, reusing CDIF/schema.org
  slots on the schema:Dataset root.
allOf:
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/AnalysisIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/AnalysisIdentification
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
                          const: Sample preparation
                      required:
                      - schema:name
                    then:
                      properties:
                        schema:additionalProperty:
                          type: array
                          items:
                            anyOf:
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_fusionFluxAndDilutionRatio
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_preAblationSurfaceTreatment
                          allOf:
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_fusionFluxAndDilutionRatio
                            minContains: 0
                            maxContains: 1
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_preAblationSurfaceTreatment
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
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_signalSmoothing
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_filteringApproach
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/singleCollector/schema.yaml#/$defs/Param_Analysis_pulseAnalogDetectorNonlinearityCorrection
                          allOf:
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_signalSmoothing
                            minContains: 0
                            maxContains: 1
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_filteringApproach
                            minContains: 0
                            maxContains: 1
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/singleCollector/schema.yaml#/$defs/Param_Analysis_pulseAnalogDetectorNonlinearityCorrection
                            minContains: 0
                            maxContains: 1
          schema:additionalProperty:
            type: array
            items:
              anyOf:
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_samplingUnitSelectionCriteria
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_preAnalysisImagingAndScreening
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_transectRateMappingRateOrStepSize
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_carrierGasAndFlowRate
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_makeUpGasAndFlowRate
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_analysisSequence
              - title: Ion Counter Dead Time
                description: Dead time of the ion-counting detector(s), used in the
                  dead-time correction applied to high count rates. Distinct from
                  pulse/analog cross-calibration, which relates the two detector modes
                  rather than correcting counting losses within the pulse-counting
                  mode.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laQicpmsTAPP/ionCounterDeadTime
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laQicpmsTAPP/ionCounterDeadTime
                  schema:name:
                    const: Ion Counter Dead Time
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
              - title: Total Integration Time per Output Data Point
                description: "Total duty-cycle time for one complete mass-scan sweep
                  \u2014 the sum of all per-isotope dwell times plus inter-mass settling
                  times. Not recoverable from Dwell Time per Mass alone, because settling
                  time is not captured there. Applies to sequential (quadrupole and
                  single-collector sector-field) acquisition."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laQicpmsTAPP/totalIntegrationTimePerOutputDataPoint
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laQicpmsTAPP/totalIntegrationTimePerOutputDataPoint
                  schema:name:
                    const: Total Integration Time per Output Data Point
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
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_backgroundCountTime
              - title: Number of Replicates
                description: Number of replicate measurements performed on the same
                  sample, or on the same nominal location where the technique is spatially
                  resolved. For spot analysis this is the number of individual spots
                  per grain or location; for transects, the number of replicate lines;
                  for mapping, the number of map acquisitions of the same area; for
                  solution work, the number of discrete replicate measurements acquired
                  per sample solution.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laQicpmsTAPP/numberOfReplicates
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laQicpmsTAPP/numberOfReplicates
                  schema:name:
                    const: Number of Replicates
                  schema:value:
                    anyOf:
                    - type: number
                    - type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_transectLength
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_mappingArea
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_signalIntegrationTime
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Analysis_constantsReferenceValues
              - title: Collision/Reaction Gas Mixture Ratio
                description: Where the collision or reaction cell is supplied with
                  a mixture of gases rather than a single gas, the identities and
                  proportions of that mixture. Recorded separately from the gas identity.
                  Record 'N/A' where a single gas is used.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laQicpmsTAPP/collisionReactionGasMixtureRatio
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laQicpmsTAPP/collisionReactionGasMixtureRatio
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
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_samplingUnitSelectionCriteria
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_preAnalysisImagingAndScreening
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_transectRateMappingRateOrStepSize
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_carrierGasAndFlowRate
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_makeUpGasAndFlowRate
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_analysisSequence
              minContains: 0
              maxContains: 1
            - contains:
                title: Ion Counter Dead Time
                description: Dead time of the ion-counting detector(s), used in the
                  dead-time correction applied to high count rates. Distinct from
                  pulse/analog cross-calibration, which relates the two detector modes
                  rather than correcting counting losses within the pulse-counting
                  mode.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laQicpmsTAPP/ionCounterDeadTime
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laQicpmsTAPP/ionCounterDeadTime
                  schema:name:
                    const: Ion Counter Dead Time
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
                title: Total Integration Time per Output Data Point
                description: "Total duty-cycle time for one complete mass-scan sweep
                  \u2014 the sum of all per-isotope dwell times plus inter-mass settling
                  times. Not recoverable from Dwell Time per Mass alone, because settling
                  time is not captured there. Applies to sequential (quadrupole and
                  single-collector sector-field) acquisition."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laQicpmsTAPP/totalIntegrationTimePerOutputDataPoint
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laQicpmsTAPP/totalIntegrationTimePerOutputDataPoint
                  schema:name:
                    const: Total Integration Time per Output Data Point
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
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_backgroundCountTime
              minContains: 0
              maxContains: 1
            - contains:
                title: Number of Replicates
                description: Number of replicate measurements performed on the same
                  sample, or on the same nominal location where the technique is spatially
                  resolved. For spot analysis this is the number of individual spots
                  per grain or location; for transects, the number of replicate lines;
                  for mapping, the number of map acquisitions of the same area; for
                  solution work, the number of discrete replicate measurements acquired
                  per sample solution.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laQicpmsTAPP/numberOfReplicates
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laQicpmsTAPP/numberOfReplicates
                  schema:name:
                    const: Number of Replicates
                  schema:value:
                    anyOf:
                    - type: number
                    - type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_transectLength
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_mappingArea
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_signalIntegrationTime
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Analysis_constantsReferenceValues
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
                    const: ada:parameter/laQicpmsTAPP/collisionReactionGasMixtureRatio
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laQicpmsTAPP/collisionReactionGasMixtureRatio
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
                                              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_coolantPlasmaGasFlowRate
                                              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_auxiliaryGasFlowRate
                                              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_rfPower
                                            allOf:
                                            - contains:
                                                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_coolantPlasmaGasFlowRate
                                              minContains: 0
                                              maxContains: 1
                                            - contains:
                                                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_auxiliaryGasFlowRate
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
                                    - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_massResolutionSetting
                                    - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_icpTuning
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
                                          const: ada:parameter/laQicpmsTAPP/doublyChargedSpeciesMonitor
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/laQicpmsTAPP/doublyChargedSpeciesMonitor
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
                                          const: ada:parameter/laQicpmsTAPP/doublyChargedSpeciesProduction
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/laQicpmsTAPP/doublyChargedSpeciesProduction
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
                                  allOf:
                                  - contains:
                                      $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_massResolutionSetting
                                    minContains: 0
                                    maxContains: 1
                                  - contains:
                                      $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_icpTuning
                                    minContains: 0
                                    maxContains: 1
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
                                          const: ada:parameter/laQicpmsTAPP/doublyChargedSpeciesMonitor
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/laQicpmsTAPP/doublyChargedSpeciesMonitor
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
                                          const: ada:parameter/laQicpmsTAPP/doublyChargedSpeciesProduction
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/laQicpmsTAPP/doublyChargedSpeciesProduction
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
                          - if:
                              properties:
                                schema:additionalType:
                                  contains:
                                    const: Laser Ablation System
                                  schema:inDefinedTermSet: ada:vocab/instrumentType
                              required:
                              - schema:additionalType
                            then:
                              properties:
                                schema:additionalProperty:
                                  type: array
                                  items:
                                    $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_laserEnergy
                                  allOf:
                                  - contains:
                                      $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_laserEnergy
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
                    schema:additionalProperty:
                      type: array
                      items:
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_mappedAreaDescription
                      allOf:
                      - contains:
                          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_mappedAreaDescription
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
          ada:proceduralBlankLevel:
            description: "The measured level of the analytical blank in the session,
              and \u2014 where the reported quantity is a ratio \u2014 its composition,
              since a blank subtracted from a ratio biases the result unless its own
              composition is known. Companion to the blank correction method."
            type: string
        required:
        - ada:proceduralBlankLevel

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS/detail/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS/detail/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS/detail/context.jsonld)

## Sources

* [LA-Q-ICP-MS_TAPP_v15.csv (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/LA-Q-ICPMS/detail`

