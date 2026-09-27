
# LA-Q-ICP-MS U-Pb Analysis Detail (Schema)

`ogch.techniqueProfile.geochemProfile.LA-Q-ICPMS-UPb.detail` *v0.1*

Dataset-level analysis-instance detail for LA-Q-ICP-MS U-Pb geochronology, reusing CDIF/schema.org slots on the schema:Dataset root.

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
    "ada:LAICPMSGeochronTabular"
  ],
  "ada:componentType": "ada:LAICPMSGeochronTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laQicpmsUPbTAPP-Nakanishi2022",
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
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially — the contributing counts are stated per grain, the reported ratios being \"the mean Re/Os abundance ratios for each of the 1–3 analytical spots measured by LA-ICP-MS\" (p.8). No acceptance or rejection rule is stated for the LA data; the 233/235 > 0.2 rejection (p.4) is a rule for the N-TIMS Os measurements, not for these spot analyses, and is not borrowed",
  "ada:radiogenicFractionOfMeasuredSignal": "missing",
  "ada:ageDatumReferenceEpoch": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "Analytical uncertainties: 2SE of individual spot measurements reported alongside data",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening"
        }
      ],
      "schema:name": "Pre-Analysis Imaging and Screening",
      "schema:value": "Secondary-electron imaging on the EPMA, used to place every spot — \"Based on the secondary electron images taken by EPMA, we selected analytical spots for LA-ICP-MS and sampling spots for micro-milling\" (p.4); the spots carry numbers (\"spot No.\" 201, 202 …) that tie the analyses back to those images (table p.6)"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS-UPb/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Nakanishi2022",
  "@type": [
    "ada:LAICPMSGeochronTabular"
  ],
  "ada:componentType": "ada:LAICPMSGeochronTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laQicpmsUPbTAPP-Nakanishi2022",
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
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially \u2014 the contributing counts are stated per grain, the reported ratios being \"the mean Re/Os abundance ratios for each of the 1\u20133 analytical spots measured by LA-ICP-MS\" (p.8). No acceptance or rejection rule is stated for the LA data; the 233/235 > 0.2 rejection (p.4) is a rule for the N-TIMS Os measurements, not for these spot analyses, and is not borrowed",
  "ada:radiogenicFractionOfMeasuredSignal": "missing",
  "ada:ageDatumReferenceEpoch": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "Analytical uncertainties: 2SE of individual spot measurements reported alongside data",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening"
        }
      ],
      "schema:name": "Pre-Analysis Imaging and Screening",
      "schema:value": "Secondary-electron imaging on the EPMA, used to place every spot \u2014 \"Based on the secondary electron images taken by EPMA, we selected analytical spots for LA-ICP-MS and sampling spots for micro-milling\" (p.4); the spots carry numbers (\"spot No.\" 201, 202 \u2026) that tie the analyses back to those images (table p.6)"
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

<ex:detail-Nakanishi2022> a ada:LAICPMSGeochronTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening> ;
    schema1:measurementTechnique <ex:laQicpmsUPbTAPP-Nakanishi2022> ;
    ada:ageDatumReferenceEpoch "missing" ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially — the contributing counts are stated per grain, the reported ratios being \"the mean Re/Os abundance ratios for each of the 1–3 analytical spots measured by LA-ICP-MS\" (p.8). No acceptance or rejection rule is stated for the LA data; the 233/235 > 0.2 rejection (p.4) is a rule for the N-TIMS Os measurements, not for these spot analyses, and is not borrowed" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "missing" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:LAICPMSGeochronTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:errorCorrelationBetweenReportedQuantities -9999 ;
    ada:fundingSourceForAnalysis "JSPS Grant-in-Aid for Scientific Research (grants 26106002, 26220713, 16H04081, 19H00715, 19H01081, 20H04609)" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:radiogenicFractionOfMeasuredSignal "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Labelled: metal grains by host chondrule within each section — e.g. \"N8_02 interior ch2-1\" with LA \"spot No.\" 201, 202; \"N8_05 margin ch1\"; isolated grain \"iso1\" (table p.6; p.4) — in the sections \"NWA801-3-8, NWA7184-29-9, and DHO1432-5-5\" (p.2)" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "Analytical uncertainties: 2SE of individual spot measurements reported alongside data" .

<ex:laQicpmsUPbTAPP-Nakanishi2022> schema1:identifier "missing" .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening> ;
    schema1:value "Secondary-electron imaging on the EPMA, used to place every spot — \"Based on the secondary electron images taken by EPMA, we selected analytical spots for LA-ICP-MS and sampling spots for micro-milling\" (p.4); the spots carry numbers (\"spot No.\" 201, 202 …) that tie the analyses back to those images (table p.6)" .


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
    "ada:LAICPMSGeochronTabular"
  ],
  "ada:componentType": "ada:LAICPMSGeochronTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laQicpmsUPbTAPP-Liu2024",
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
  "ada:signalIntegrationTime": 45,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially — each reported value is the mean of a stated count, \"fs-LA-ICP-MS (n = 9 spots)\" against \"SN-ICP-MS (n = 5)\" (Table 2, p.8), with a 95% confidence interval. No acceptance or rejection rule, and no acquired-versus-included count, is stated",
  "ada:radiogenicFractionOfMeasuredSignal": "missing",
  "ada:ageDatumReferenceEpoch": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:detectionLimit": "LODs for 32 elements in Li-borate glass BHVO-2: 0.005–23.5 µg g⁻¹ (dilution-limited; much higher than undiluted glass LODs); LODs for NIST 610: 0.007–0.45 µg g⁻¹; LOQ = 3.3 × LOD (Pettke 2012) for most elements; LOQ for pollution elements = blank + 10SD (Gold Book IUPAC)",
  "ada:limitOfQuantificationMethod": "LOQ = 3.3 × LOD per Pettke (2012) for most elements; LOQ = blank value + 10SD per IUPAC Gold Book for pollution elements (V, Co, Zn, Ba, La, Ce, Ta, U) where blank contribution is significant",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "Analytical precision (RSD) within 10% for most of 32 trace elements in 6 silicate GRMs (verified by homogeneity index assessment across 9 spots per disk)",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "Analytical results within 10% of reference values for most of 32 trace elements in 6 GRMs (mafic to felsic); precision (RSD) within 10% for most elements; lunar basalt (NWA14526) and shergottite (NWA13190) results compared with SN-ICP-MS and found reliable",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening"
        }
      ],
      "schema:name": "Pre-Analysis Imaging and Screening",
      "schema:value": "N — the fused glass discs are prepared for XRF and then ablated directly; no imaging or screening step is described before the LA-ICP-MS spots, whose grid is laid out to cover the whole disc (p.5)"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS-UPb/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Liu2024",
  "@type": [
    "ada:LAICPMSGeochronTabular"
  ],
  "ada:componentType": "ada:LAICPMSGeochronTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laQicpmsUPbTAPP-Liu2024",
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
  "ada:signalIntegrationTime": 45,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially \u2014 each reported value is the mean of a stated count, \"fs-LA-ICP-MS (n = 9 spots)\" against \"SN-ICP-MS (n = 5)\" (Table 2, p.8), with a 95% confidence interval. No acceptance or rejection rule, and no acquired-versus-included count, is stated",
  "ada:radiogenicFractionOfMeasuredSignal": "missing",
  "ada:ageDatumReferenceEpoch": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:detectionLimit": "LODs for 32 elements in Li-borate glass BHVO-2: 0.005\u201323.5 \u00b5g g\u207b\u00b9 (dilution-limited; much higher than undiluted glass LODs); LODs for NIST 610: 0.007\u20130.45 \u00b5g g\u207b\u00b9; LOQ = 3.3 \u00d7 LOD (Pettke 2012) for most elements; LOQ for pollution elements = blank + 10SD (Gold Book IUPAC)",
  "ada:limitOfQuantificationMethod": "LOQ = 3.3 \u00d7 LOD per Pettke (2012) for most elements; LOQ = blank value + 10SD per IUPAC Gold Book for pollution elements (V, Co, Zn, Ba, La, Ce, Ta, U) where blank contribution is significant",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "Analytical precision (RSD) within 10% for most of 32 trace elements in 6 silicate GRMs (verified by homogeneity index assessment across 9 spots per disk)",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "Analytical results within 10% of reference values for most of 32 trace elements in 6 GRMs (mafic to felsic); precision (RSD) within 10% for most elements; lunar basalt (NWA14526) and shergottite (NWA13190) results compared with SN-ICP-MS and found reliable",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening"
        }
      ],
      "schema:name": "Pre-Analysis Imaging and Screening",
      "schema:value": "N \u2014 the fused glass discs are prepared for XRF and then ablated directly; no imaging or screening step is described before the LA-ICP-MS spots, whose grid is laid out to cover the whole disc (p.5)"
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

<ex:detail-Liu2024> a ada:LAICPMSGeochronTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening> ;
    schema1:measurementTechnique <ex:laQicpmsUPbTAPP-Liu2024> ;
    ada:ageDatumReferenceEpoch "missing" ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially — each reported value is the mean of a stated count, \"fs-LA-ICP-MS (n = 9 spots)\" against \"SN-ICP-MS (n = 5)\" (Table 2, p.8), with a 95% confidence interval. No acceptance or rejection rule, and no acquired-versus-included count, is stated" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "Analytical results within 10% of reference values for most of 32 trace elements in 6 GRMs (mafic to felsic); precision (RSD) within 10% for most elements; lunar basalt (NWA14526) and shergottite (NWA13190) results compared with SN-ICP-MS and found reliable" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:LAICPMSGeochronTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "LODs for 32 elements in Li-borate glass BHVO-2: 0.005–23.5 µg g⁻¹ (dilution-limited; much higher than undiluted glass LODs); LODs for NIST 610: 0.007–0.45 µg g⁻¹; LOQ = 3.3 × LOD (Pettke 2012) for most elements; LOQ for pollution elements = blank + 10SD (Gold Book IUPAC)" ;
    ada:errorCorrelationBetweenReportedQuantities -9999 ;
    ada:fundingSourceForAnalysis "Strategy Priority Research Program (Category B) of Chinese Academy of Sciences (XDB0710000); NSFC 42073022" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "LOQ = 3.3 × LOD per Pettke (2012) for most elements; LOQ = blank value + 10SD per IUPAC Gold Book for pollution elements (V, Co, Zn, Ba, La, Ce, Ta, U) where blank contribution is significant" ;
    ada:mappingArea "missing" ;
    ada:numberOfReplicates 9 ;
    ada:oxideProduction "ThO/Th = measured at <0.3%; U/Th = 0.95–1.05 (on NIST SRM 612)" ;
    ada:proceduralBlankLevel "missing" ;
    ada:radiogenicFractionOfMeasuredSignal "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Sample name only — reference-material fusion glasses by name (JB-1b, GSR-3, AGV-2, AC-E, GSR-1, W-2A; BHVO-2 glass, p.3); \"Nine spot analyses ... were arranged in a grid\" per glass (p.5), unlabelled" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime 45 ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "Analytical precision (RSD) within 10% for most of 32 trace elements in 6 silicate GRMs (verified by homogeneity index assessment across 9 spots per disk)" .

<ex:laQicpmsUPbTAPP-Liu2024> schema1:identifier "missing" .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening> ;
    schema1:value "N — the fused glass discs are prepared for XRF and then ablated directly; no imaging or screening step is described before the LA-ICP-MS spots, whose grid is laid out to cover the whole disc (p.5)" .


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
    "ada:LAICPMSGeochronTabular"
  ],
  "ada:componentType": "ada:LAICPMSGeochronTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laQicpmsUPbTAPP-Liu2025",
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
  "ada:signalIntegrationTime": "~40 s (inferred from typical CetacAnalyte HE protocol; stable signal used)",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "N — no rule for admitting or rejecting individual results is stated. The one documented exclusion is at sample level and before analysis: \"Capsules that had lost significant weight were discarded\" after the leak check (p.2)",
  "ada:radiogenicFractionOfMeasuredSignal": "missing",
  "ada:ageDatumReferenceEpoch": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:detectionLimit": "Detection limits for Au ~0.01 ppm; Cu ~0.1 ppm in silicate melt (stated in paper)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "Au and Cu fully dissolved in most glasses (smooth signals); Au results consistent with Au solubility trends from literature; comparison with SN-ICP-MS (solution) for two extraterrestrial samples confirms reliability",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening"
        }
      ],
      "schema:name": "Pre-Analysis Imaging and Screening",
      "schema:value": "Optical microscopy, then EMP — \"Following examination by optical microscopy to ascertain the integrity of the experiments and the state of the oxygen buffers, the solid components of the run products were analysed for major elements, S and Cu, using a JEOL JXA-8230 electron microprobe (EMP)\" (p.2); those EMP values are then the internal standards for the LA data, \"with Si and Fe obtained from EMP analyses as the internal standards\" (p.4)"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS-UPb/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Liu2025",
  "@type": [
    "ada:LAICPMSGeochronTabular"
  ],
  "ada:componentType": "ada:LAICPMSGeochronTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laQicpmsUPbTAPP-Liu2025",
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
  "ada:signalIntegrationTime": "~40 s (inferred from typical CetacAnalyte HE protocol; stable signal used)",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 no rule for admitting or rejecting individual results is stated. The one documented exclusion is at sample level and before analysis: \"Capsules that had lost significant weight were discarded\" after the leak check (p.2)",
  "ada:radiogenicFractionOfMeasuredSignal": "missing",
  "ada:ageDatumReferenceEpoch": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:detectionLimit": "Detection limits for Au ~0.01 ppm; Cu ~0.1 ppm in silicate melt (stated in paper)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "Au and Cu fully dissolved in most glasses (smooth signals); Au results consistent with Au solubility trends from literature; comparison with SN-ICP-MS (solution) for two extraterrestrial samples confirms reliability",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening"
        }
      ],
      "schema:name": "Pre-Analysis Imaging and Screening",
      "schema:value": "Optical microscopy, then EMP \u2014 \"Following examination by optical microscopy to ascertain the integrity of the experiments and the state of the oxygen buffers, the solid components of the run products were analysed for major elements, S and Cu, using a JEOL JXA-8230 electron microprobe (EMP)\" (p.2); those EMP values are then the internal standards for the LA data, \"with Si and Fe obtained from EMP analyses as the internal standards\" (p.4)"
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

<ex:detail-Liu2025> a ada:LAICPMSGeochronTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening> ;
    schema1:measurementTechnique <ex:laQicpmsUPbTAPP-Liu2025> ;
    ada:ageDatumReferenceEpoch "missing" ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — no rule for admitting or rejecting individual results is stated. The one documented exclusion is at sample level and before analysis: \"Capsules that had lost significant weight were discarded\" after the leak check (p.2)" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "Au and Cu fully dissolved in most glasses (smooth signals); Au results consistent with Au solubility trends from literature; comparison with SN-ICP-MS (solution) for two extraterrestrial samples confirms reliability" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:LAICPMSGeochronTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "Detection limits for Au ~0.01 ppm; Cu ~0.1 ppm in silicate melt (stated in paper)" ;
    ada:errorCorrelationBetweenReportedQuantities -9999 ;
    ada:fundingSourceForAnalysis "Strategic Priority Research Program (B) of CAS (XDB0840200); NSFC 92062222, 42073057, 42250710679, 42250202, 42273023" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:radiogenicFractionOfMeasuredSignal "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Sample name only — experimental run products by run number, e.g. \"D-2\", \"D-4\", \"D-34\", \"D-46\" (Table 1, p.3) and \"DAC-41\" (p.4); spots within a run are not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime "~40 s (inferred from typical CetacAnalyte HE protocol; stable signal used)" ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<ex:laQicpmsUPbTAPP-Liu2025> schema1:identifier "missing" .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening> ;
    schema1:value "Optical microscopy, then EMP — \"Following examination by optical microscopy to ascertain the integrity of the experiments and the state of the oxygen buffers, the solid components of the run products were analysed for major elements, S and Cu, using a JEOL JXA-8230 electron microprobe (EMP)\" (p.2); those EMP values are then the internal standards for the LA data, \"with Si and Fe obtained from EMP analyses as the internal standards\" (p.4)" .


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
    "ada:LAICPMSGeochronTabular"
  ],
  "ada:componentType": "ada:LAICPMSGeochronTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laQicpmsUPbTAPP-Liu2025-2",
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
  "ada:signalIntegrationTime": "~40 s (same)",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "N — no rule for admitting or rejecting individual results is stated. The one documented exclusion is at sample level and before analysis: \"Capsules that had lost significant weight were discarded\" after the leak check (p.2)",
  "ada:radiogenicFractionOfMeasuredSignal": "missing",
  "ada:ageDatumReferenceEpoch": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "Sulfide Au and Cu concentrations consistent with strong positive correlation with log fS₂ (Fig. 5A) confirming thermodynamic equilibrium; partitioning coefficients Dsulfide/melt consistent with literature (Li et al. 2019, 2021)",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening"
        }
      ],
      "schema:name": "Pre-Analysis Imaging and Screening",
      "schema:value": "Optical microscopy, then EMP — \"Following examination by optical microscopy to ascertain the integrity of the experiments and the state of the oxygen buffers, the solid components of the run products were analysed for major elements, S and Cu, using a JEOL JXA-8230 electron microprobe (EMP)\" (p.2); those EMP values are then the internal standards for the LA data, \"with Si and Fe obtained from EMP analyses as the internal standards\" (p.4)"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS-UPb/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Liu2025-2",
  "@type": [
    "ada:LAICPMSGeochronTabular"
  ],
  "ada:componentType": "ada:LAICPMSGeochronTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laQicpmsUPbTAPP-Liu2025-2",
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
  "ada:signalIntegrationTime": "~40 s (same)",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 no rule for admitting or rejecting individual results is stated. The one documented exclusion is at sample level and before analysis: \"Capsules that had lost significant weight were discarded\" after the leak check (p.2)",
  "ada:radiogenicFractionOfMeasuredSignal": "missing",
  "ada:ageDatumReferenceEpoch": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "Sulfide Au and Cu concentrations consistent with strong positive correlation with log fS\u2082 (Fig. 5A) confirming thermodynamic equilibrium; partitioning coefficients Dsulfide/melt consistent with literature (Li et al. 2019, 2021)",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening"
        }
      ],
      "schema:name": "Pre-Analysis Imaging and Screening",
      "schema:value": "Optical microscopy, then EMP \u2014 \"Following examination by optical microscopy to ascertain the integrity of the experiments and the state of the oxygen buffers, the solid components of the run products were analysed for major elements, S and Cu, using a JEOL JXA-8230 electron microprobe (EMP)\" (p.2); those EMP values are then the internal standards for the LA data, \"with Si and Fe obtained from EMP analyses as the internal standards\" (p.4)"
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

<ex:detail-Liu2025-2> a ada:LAICPMSGeochronTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening> ;
    schema1:measurementTechnique <ex:laQicpmsUPbTAPP-Liu2025-2> ;
    ada:ageDatumReferenceEpoch "missing" ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — no rule for admitting or rejecting individual results is stated. The one documented exclusion is at sample level and before analysis: \"Capsules that had lost significant weight were discarded\" after the leak check (p.2)" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "Sulfide Au and Cu concentrations consistent with strong positive correlation with log fS₂ (Fig. 5A) confirming thermodynamic equilibrium; partitioning coefficients Dsulfide/melt consistent with literature (Li et al. 2019, 2021)" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:LAICPMSGeochronTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:errorCorrelationBetweenReportedQuantities -9999 ;
    ada:fundingSourceForAnalysis "Strategic Priority Research Program (B) of CAS (XDB0840200); NSFC 92062222, 42073057, 42250710679, 42250202, 42273023" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:radiogenicFractionOfMeasuredSignal "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Sample name only — experimental run products by run number, e.g. \"D-2\", \"D-4\", \"D-34\", \"D-46\" (Table 1, p.3) and \"DAC-41\" (p.4); spots within a run are not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime "~40 s (same)" ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<ex:laQicpmsUPbTAPP-Liu2025-2> schema1:identifier "missing" .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening> ;
    schema1:value "Optical microscopy, then EMP — \"Following examination by optical microscopy to ascertain the integrity of the experiments and the state of the oxygen buffers, the solid components of the run products were analysed for major elements, S and Cu, using a JEOL JXA-8230 electron microprobe (EMP)\" (p.2); those EMP values are then the internal standards for the LA data, \"with Si and Fe obtained from EMP analyses as the internal standards\" (p.4)" .


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
    "ada:LAICPMSGeochronTabular"
  ],
  "ada:componentType": "ada:LAICPMSGeochronTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laQicpmsUPbTAPP-Liu2016",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA Cosmochemistry grants NNX11AG58G (to L.A.T.) and NNN13D465T (to Y.L.); NSF EAR-1226270 (to P.D.A.) and EAR-1019770 (to R.J.B.); Y.L. supported by Jet Propulsion Laboratory",
  "ada:sampleName": "Tissint Martian meteorite",
  "ada:samplingUnitName": "Labelled sections: \"UT1 to UT3 (formerly referred to as MT-1, MT-2, MT-3)\" (p.3). LA-ICP-MS results are averages (\"n = 7\", \"n = 13\", table p.9); individual analyses are in \"Table S1 in supporting information\" (p.7), not in the archived PDF",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially — the reported values are means of stated counts (\"n = 7\", \"n = 13\", table p.9). No acceptance or rejection rule is stated; the plateau-region screening of each spot is signal-based and is recorded under Spike / Outlier Filtering Approach",
  "ada:radiogenicFractionOfMeasuredSignal": "missing",
  "ada:ageDatumReferenceEpoch": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:detectionLimit": "Referenced in Table 3 and Table S1; specific values not directly stated in main text; REE in olivines below detection limits at 24–32 µm conditions",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "For silicates: oxide-sum normalization agrees within <10% with EMP-based IS method (internal cross-check, not a separate QC standard)",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening"
        }
      ],
      "schema:name": "Pre-Analysis Imaging and Screening",
      "schema:value": "Petrographic microscopy, SEM and EMP — \"The petrography of these sections was examined using a petrographic microscope and a scanning electron microscope\", followed by BSE images and element maps (p.3); the EMP results then serve as internal standards for the ablation data, which are normalised using \"EMP CaO or MgO values\" for silicates and \"40Ca counts to CaO concentrations from the EMP analysis\" for phosphate (p.4)"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS-UPb/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Liu2016",
  "@type": [
    "ada:LAICPMSGeochronTabular"
  ],
  "ada:componentType": "ada:LAICPMSGeochronTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laQicpmsUPbTAPP-Liu2016",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA Cosmochemistry grants NNX11AG58G (to L.A.T.) and NNN13D465T (to Y.L.); NSF EAR-1226270 (to P.D.A.) and EAR-1019770 (to R.J.B.); Y.L. supported by Jet Propulsion Laboratory",
  "ada:sampleName": "Tissint Martian meteorite",
  "ada:samplingUnitName": "Labelled sections: \"UT1 to UT3 (formerly referred to as MT-1, MT-2, MT-3)\" (p.3). LA-ICP-MS results are averages (\"n = 7\", \"n = 13\", table p.9); individual analyses are in \"Table S1 in supporting information\" (p.7), not in the archived PDF",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially \u2014 the reported values are means of stated counts (\"n = 7\", \"n = 13\", table p.9). No acceptance or rejection rule is stated; the plateau-region screening of each spot is signal-based and is recorded under Spike / Outlier Filtering Approach",
  "ada:radiogenicFractionOfMeasuredSignal": "missing",
  "ada:ageDatumReferenceEpoch": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:detectionLimit": "Referenced in Table 3 and Table S1; specific values not directly stated in main text; REE in olivines below detection limits at 24\u201332 \u00b5m conditions",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "For silicates: oxide-sum normalization agrees within <10% with EMP-based IS method (internal cross-check, not a separate QC standard)",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening"
        }
      ],
      "schema:name": "Pre-Analysis Imaging and Screening",
      "schema:value": "Petrographic microscopy, SEM and EMP \u2014 \"The petrography of these sections was examined using a petrographic microscope and a scanning electron microscope\", followed by BSE images and element maps (p.3); the EMP results then serve as internal standards for the ablation data, which are normalised using \"EMP CaO or MgO values\" for silicates and \"40Ca counts to CaO concentrations from the EMP analysis\" for phosphate (p.4)"
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

<ex:detail-Liu2016> a ada:LAICPMSGeochronTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening> ;
    schema1:measurementTechnique <ex:laQicpmsUPbTAPP-Liu2016> ;
    ada:ageDatumReferenceEpoch "missing" ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially — the reported values are means of stated counts (\"n = 7\", \"n = 13\", table p.9). No acceptance or rejection rule is stated; the plateau-region screening of each spot is signal-based and is recorded under Spike / Outlier Filtering Approach" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "For silicates: oxide-sum normalization agrees within <10% with EMP-based IS method (internal cross-check, not a separate QC standard)" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:LAICPMSGeochronTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "Referenced in Table 3 and Table S1; specific values not directly stated in main text; REE in olivines below detection limits at 24–32 µm conditions" ;
    ada:errorCorrelationBetweenReportedQuantities -9999 ;
    ada:fundingSourceForAnalysis "NASA Cosmochemistry grants NNX11AG58G (to L.A.T.) and NNN13D465T (to Y.L.); NSF EAR-1226270 (to P.D.A.) and EAR-1019770 (to R.J.B.); Y.L. supported by Jet Propulsion Laboratory" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:radiogenicFractionOfMeasuredSignal "missing" ;
    ada:sampleName "Tissint Martian meteorite" ;
    ada:samplingUnitName "Labelled sections: \"UT1 to UT3 (formerly referred to as MT-1, MT-2, MT-3)\" (p.3). LA-ICP-MS results are averages (\"n = 7\", \"n = 13\", table p.9); individual analyses are in \"Table S1 in supporting information\" (p.7), not in the archived PDF" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<ex:laQicpmsUPbTAPP-Liu2016> schema1:identifier "missing" .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening> ;
    schema1:value "Petrographic microscopy, SEM and EMP — \"The petrography of these sections was examined using a petrographic microscope and a scanning electron microscope\", followed by BSE images and element maps (p.3); the EMP results then serve as internal standards for the ablation data, which are normalised using \"EMP CaO or MgO values\" for silicates and \"40Ca counts to CaO concentrations from the EMP analysis\" for phosphate (p.4)" .


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
    "ada:LAICPMSGeochronTabular"
  ],
  "ada:componentType": "ada:LAICPMSGeochronTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laQicpmsUPbTAPP-Liu2016-2",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Same as silicate protocol",
  "ada:sampleName": "Tissint Martian meteorite",
  "ada:samplingUnitName": "Labelled sections: \"UT1 to UT3 (formerly referred to as MT-1, MT-2, MT-3)\" (p.3). LA-ICP-MS results are averages (\"n = 7\", \"n = 13\", table p.9); individual analyses are in \"Table S1 in supporting information\" (p.7), not in the archived PDF",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially — the reported values are means of stated counts (\"n = 7\", \"n = 13\", table p.9). No acceptance or rejection rule is stated; the plateau-region screening of each spot is signal-based and is recorded under Spike / Outlier Filtering Approach",
  "ada:radiogenicFractionOfMeasuredSignal": "missing",
  "ada:ageDatumReferenceEpoch": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:detectionLimit": "Referenced in Table 3 and Table S1; specific values not directly stated in main text; merrillite REE at 14–414 ppm range above detection",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening"
        }
      ],
      "schema:name": "Pre-Analysis Imaging and Screening",
      "schema:value": "Petrographic microscopy, SEM and EMP — \"The petrography of these sections was examined using a petrographic microscope and a scanning electron microscope\", followed by BSE images and element maps (p.3); the EMP results then serve as internal standards for the ablation data, which are normalised using \"EMP CaO or MgO values\" for silicates and \"40Ca counts to CaO concentrations from the EMP analysis\" for phosphate (p.4)"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS-UPb/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Liu2016-2",
  "@type": [
    "ada:LAICPMSGeochronTabular"
  ],
  "ada:componentType": "ada:LAICPMSGeochronTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laQicpmsUPbTAPP-Liu2016-2",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Same as silicate protocol",
  "ada:sampleName": "Tissint Martian meteorite",
  "ada:samplingUnitName": "Labelled sections: \"UT1 to UT3 (formerly referred to as MT-1, MT-2, MT-3)\" (p.3). LA-ICP-MS results are averages (\"n = 7\", \"n = 13\", table p.9); individual analyses are in \"Table S1 in supporting information\" (p.7), not in the archived PDF",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially \u2014 the reported values are means of stated counts (\"n = 7\", \"n = 13\", table p.9). No acceptance or rejection rule is stated; the plateau-region screening of each spot is signal-based and is recorded under Spike / Outlier Filtering Approach",
  "ada:radiogenicFractionOfMeasuredSignal": "missing",
  "ada:ageDatumReferenceEpoch": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:detectionLimit": "Referenced in Table 3 and Table S1; specific values not directly stated in main text; merrillite REE at 14\u2013414 ppm range above detection",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening"
        }
      ],
      "schema:name": "Pre-Analysis Imaging and Screening",
      "schema:value": "Petrographic microscopy, SEM and EMP \u2014 \"The petrography of these sections was examined using a petrographic microscope and a scanning electron microscope\", followed by BSE images and element maps (p.3); the EMP results then serve as internal standards for the ablation data, which are normalised using \"EMP CaO or MgO values\" for silicates and \"40Ca counts to CaO concentrations from the EMP analysis\" for phosphate (p.4)"
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

<ex:detail-Liu2016-2> a ada:LAICPMSGeochronTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening> ;
    schema1:measurementTechnique <ex:laQicpmsUPbTAPP-Liu2016-2> ;
    ada:ageDatumReferenceEpoch "missing" ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially — the reported values are means of stated counts (\"n = 7\", \"n = 13\", table p.9). No acceptance or rejection rule is stated; the plateau-region screening of each spot is signal-based and is recorded under Spike / Outlier Filtering Approach" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "missing" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:LAICPMSGeochronTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "Referenced in Table 3 and Table S1; specific values not directly stated in main text; merrillite REE at 14–414 ppm range above detection" ;
    ada:errorCorrelationBetweenReportedQuantities -9999 ;
    ada:fundingSourceForAnalysis "Same as silicate protocol" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:radiogenicFractionOfMeasuredSignal "missing" ;
    ada:sampleName "Tissint Martian meteorite" ;
    ada:samplingUnitName "Labelled sections: \"UT1 to UT3 (formerly referred to as MT-1, MT-2, MT-3)\" (p.3). LA-ICP-MS results are averages (\"n = 7\", \"n = 13\", table p.9); individual analyses are in \"Table S1 in supporting information\" (p.7), not in the archived PDF" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<ex:laQicpmsUPbTAPP-Liu2016-2> schema1:identifier "missing" .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening> ;
    schema1:value "Petrographic microscopy, SEM and EMP — \"The petrography of these sections was examined using a petrographic microscope and a scanning electron microscope\", followed by BSE images and element maps (p.3); the EMP results then serve as internal standards for the ablation data, which are normalised using \"EMP CaO or MgO values\" for silicates and \"40Ca counts to CaO concentrations from the EMP analysis\" for phosphate (p.4)" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: LA-Q-ICP-MS U-Pb Analysis Detail
description: Dataset-level analysis-instance detail for LA-Q-ICP-MS U-Pb geochronology,
  reusing CDIF/schema.org slots on the schema:Dataset root.
allOf:
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/AnalysisIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/AnalysisIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/calibrationFactor/schema.yaml#/$defs/AnalysisIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/aggregation/schema.yaml#/$defs/AnalysisIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/geochronology/schema.yaml#/$defs/AnalysisIdentification
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
                    schema:additionalProperty:
                      type: array
                      items:
                        anyOf:
                        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_sampleFormAnalyticalSubstrate
                        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_mappedAreaDescription
                      allOf:
                      - contains:
                          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_sampleFormAnalyticalSubstrate
                        minContains: 0
                        maxContains: 1
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
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Analysis_constantsReferenceValues
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
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Analysis_constantsReferenceValues
                            minContains: 0
                            maxContains: 1
                allOf:
                - contains:
                    properties:
                      schema:name:
                        const: Data reduction
                    required:
                    - schema:name
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
              - title: Monitored Masses
                description: Specific masses monitored in this procedure, grouped
                  by the target species element they serve where they serve one. Covers
                  atomic isotopes and, where a reaction cell shifts an target species
                  onto a different mass, the product mass actually measured. Includes
                  interference-monitor and internal-standard masses, which serve no
                  target species and so have no parent element. The target species
                  list is given by the Target Species field and is never inferred
                  from the element symbols appearing here.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laQicpmsUPbTAPP/monitoredMasses
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laQicpmsUPbTAPP/monitoredMasses
                  schema:name:
                    const: Monitored Masses
                  schema:value:
                    type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - title: Ion Counter Dead Time
                description: Dead time of the ion-counting detector(s), used in the
                  dead-time correction applied to high count rates. Distinct from
                  pulse/analog cross-calibration, which relates the two detector modes
                  rather than correcting counting losses within the pulse-counting
                  mode.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laQicpmsUPbTAPP/ionCounterDeadTime
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laQicpmsUPbTAPP/ionCounterDeadTime
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
                    const: ada:parameter/laQicpmsUPbTAPP/numberOfReplicates
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laQicpmsUPbTAPP/numberOfReplicates
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
              - title: Error Correlation Between Reported Quantities
                description: The correlation coefficient between pairs of reported
                  quantities whose uncertainties are not independent, together with
                  the pair it applies to and how it was obtained.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laQicpmsUPbTAPP/errorCorrelationBetweenReportedQuantities
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laQicpmsUPbTAPP/errorCorrelationBetweenReportedQuantities
                  schema:name:
                    const: Error Correlation Between Reported Quantities
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
                    const: ada:parameter/laQicpmsUPbTAPP/totalIntegrationTimePerOutputDataPoint
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laQicpmsUPbTAPP/totalIntegrationTimePerOutputDataPoint
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
              - title: Collision/Reaction Gas Mixture Ratio
                description: Where the collision or reaction cell is supplied with
                  a mixture of gases rather than a single gas, the identities and
                  proportions of that mixture. Recorded separately from the gas identity.
                  Record 'N/A' where a single gas is used.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laQicpmsUPbTAPP/collisionReactionGasMixtureRatio
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laQicpmsUPbTAPP/collisionReactionGasMixtureRatio
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
                title: Monitored Masses
                description: Specific masses monitored in this procedure, grouped
                  by the target species element they serve where they serve one. Covers
                  atomic isotopes and, where a reaction cell shifts an target species
                  onto a different mass, the product mass actually measured. Includes
                  interference-monitor and internal-standard masses, which serve no
                  target species and so have no parent element. The target species
                  list is given by the Target Species field and is never inferred
                  from the element symbols appearing here.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laQicpmsUPbTAPP/monitoredMasses
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laQicpmsUPbTAPP/monitoredMasses
                  schema:name:
                    const: Monitored Masses
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
                title: Ion Counter Dead Time
                description: Dead time of the ion-counting detector(s), used in the
                  dead-time correction applied to high count rates. Distinct from
                  pulse/analog cross-calibration, which relates the two detector modes
                  rather than correcting counting losses within the pulse-counting
                  mode.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laQicpmsUPbTAPP/ionCounterDeadTime
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laQicpmsUPbTAPP/ionCounterDeadTime
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
                    const: ada:parameter/laQicpmsUPbTAPP/numberOfReplicates
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laQicpmsUPbTAPP/numberOfReplicates
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
                title: Error Correlation Between Reported Quantities
                description: The correlation coefficient between pairs of reported
                  quantities whose uncertainties are not independent, together with
                  the pair it applies to and how it was obtained.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laQicpmsUPbTAPP/errorCorrelationBetweenReportedQuantities
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laQicpmsUPbTAPP/errorCorrelationBetweenReportedQuantities
                  schema:name:
                    const: Error Correlation Between Reported Quantities
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
                    const: ada:parameter/laQicpmsUPbTAPP/totalIntegrationTimePerOutputDataPoint
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laQicpmsUPbTAPP/totalIntegrationTimePerOutputDataPoint
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
                title: Collision/Reaction Gas Mixture Ratio
                description: Where the collision or reaction cell is supplied with
                  a mixture of gases rather than a single gas, the identities and
                  proportions of that mixture. Recorded separately from the gas identity.
                  Record 'N/A' where a single gas is used.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laQicpmsUPbTAPP/collisionReactionGasMixtureRatio
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laQicpmsUPbTAPP/collisionReactionGasMixtureRatio
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
                                          const: ada:parameter/laQicpmsUPbTAPP/doublyChargedSpeciesMonitor
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/laQicpmsUPbTAPP/doublyChargedSpeciesMonitor
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
                                          const: ada:parameter/laQicpmsUPbTAPP/doublyChargedSpeciesProduction
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/laQicpmsUPbTAPP/doublyChargedSpeciesProduction
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
                                          const: ada:parameter/laQicpmsUPbTAPP/doublyChargedSpeciesMonitor
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/laQicpmsUPbTAPP/doublyChargedSpeciesMonitor
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
                                          const: ada:parameter/laQicpmsUPbTAPP/doublyChargedSpeciesProduction
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/laQicpmsUPbTAPP/doublyChargedSpeciesProduction
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

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS-UPb/detail/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS-UPb/detail/schema.yaml)


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
    "wd": "https://www.wikidata.org/entity/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "dqv": "http://www.w3.org/ns/dqv#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS-UPb/detail/context.jsonld)

## Sources

* [LA-Q-ICP-MS_UPb_TAPP_v16.csv (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/LA-Q-ICPMS-UPb/detail`

