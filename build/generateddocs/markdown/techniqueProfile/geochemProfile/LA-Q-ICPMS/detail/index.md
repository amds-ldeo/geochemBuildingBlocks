
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
      "@id": "ex:laQicpmsTAPP-Nakanishi2022"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "JSPS Grant-in-Aid for Scientific Research (grants 26106002, 26220713, 16H04081, 19H00715, 19H01081, 20H04609)",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
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
      "@id": "ada:parameter/laQicpmsTAPP/uncertaintyPropagationMethod",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/uncertaintyPropagationMethod"
        }
      ],
      "schema:name": "Uncertainty Propagation Method",
      "schema:value": "2SE of individual spot measurements reported"
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
      "@id": "ex:laQicpmsTAPP-Nakanishi2022"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "JSPS Grant-in-Aid for Scientific Research (grants 26106002, 26220713, 16H04081, 19H00715, 19H01081, 20H04609)",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
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
      "@id": "ada:parameter/laQicpmsTAPP/uncertaintyPropagationMethod",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/uncertaintyPropagationMethod"
        }
      ],
      "schema:name": "Uncertainty Propagation Method",
      "schema:value": "2SE of individual spot measurements reported"
    }
  ],
  "ada:spotDiameterMeasured": -9999
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Nakanishi2022 a ada:LAICPMSTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/uncertaintyPropagationMethod> ;
    schema1:measurementTechnique ex:laQicpmsTAPP-Nakanishi2022 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "missing" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:LAICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:fundingSourceForAnalysis "JSPS Grant-in-Aid for Scientific Research (grants 26106002, 26220713, 16H04081, 19H00715, 19H01081, 20H04609)" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "Analytical uncertainties: 2SE of individual spot measurements reported alongside data" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/uncertaintyPropagationMethod> a schema1:PropertyValue ;
    schema1:name "Uncertainty Propagation Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/uncertaintyPropagationMethod> ;
    schema1:value "2SE of individual spot measurements reported" .


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
      "@id": "ex:laQicpmsTAPP-Liu2024"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Strategy Priority Research Program (Category B) of Chinese Academy of Sciences (XDB0710000); NSFC 42073022",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "ThO/Th = measured at <0.3%; U/Th = 0.95–1.05 (on NIST SRM 612)",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": 9,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": 45,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "LODs for 32 elements in Li-borate glass BHVO-2: 0.005–23.5 µg g⁻¹ (dilution-limited; much higher than undiluted glass LODs); LODs for NIST 610: 0.007–0.45 µg g⁻¹; LOQ = 3.3 × LOD (Pettke 2012) for most elements; LOQ for pollution elements = blank + 10SD (Gold Book IUPAC)",
  "ada:limitOfQuantificationMethod": "LOQ = 3.3 × LOD per Pettke (2012) for most elements; LOQ = blank value + 10SD per IUPAC Gold Book for pollution elements (V, Co, Zn, Ba, La, Ce, Ta, U) where blank contribution is significant",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "Analytical precision (RSD) within 10% for most of 32 trace elements in 6 silicate GRMs (verified by homogeneity index assessment across 9 spots per disk)",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "Analytical results within 10% of reference values for most of 32 trace elements in 6 GRMs (mafic to felsic); precision (RSD) within 10% for most elements; lunar basalt (NWA14526) and shergottite (NWA13190) results compared with SN-ICP-MS and found reliable",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
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
      "@id": "ex:laQicpmsTAPP-Liu2024"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Strategy Priority Research Program (Category B) of Chinese Academy of Sciences (XDB0710000); NSFC 42073022",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "ThO/Th = measured at <0.3%; U/Th = 0.95\u20131.05 (on NIST SRM 612)",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": 9,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": 45,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "LODs for 32 elements in Li-borate glass BHVO-2: 0.005\u201323.5 \u00b5g g\u207b\u00b9 (dilution-limited; much higher than undiluted glass LODs); LODs for NIST 610: 0.007\u20130.45 \u00b5g g\u207b\u00b9; LOQ = 3.3 \u00d7 LOD (Pettke 2012) for most elements; LOQ for pollution elements = blank + 10SD (Gold Book IUPAC)",
  "ada:limitOfQuantificationMethod": "LOQ = 3.3 \u00d7 LOD per Pettke (2012) for most elements; LOQ = blank value + 10SD per IUPAC Gold Book for pollution elements (V, Co, Zn, Ba, La, Ce, Ta, U) where blank contribution is significant",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "Analytical precision (RSD) within 10% for most of 32 trace elements in 6 silicate GRMs (verified by homogeneity index assessment across 9 spots per disk)",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "Analytical results within 10% of reference values for most of 32 trace elements in 6 GRMs (mafic to felsic); precision (RSD) within 10% for most elements; lunar basalt (NWA14526) and shergottite (NWA13190) results compared with SN-ICP-MS and found reliable",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:spotDiameterMeasured": -9999
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Liu2024 a ada:LAICPMSTabular ;
    schema1:measurementTechnique ex:laQicpmsTAPP-Liu2024 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "Analytical results within 10% of reference values for most of 32 trace elements in 6 GRMs (mafic to felsic); precision (RSD) within 10% for most elements; lunar basalt (NWA14526) and shergottite (NWA13190) results compared with SN-ICP-MS and found reliable" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:LAICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "LODs for 32 elements in Li-borate glass BHVO-2: 0.005–23.5 µg g⁻¹ (dilution-limited; much higher than undiluted glass LODs); LODs for NIST 610: 0.007–0.45 µg g⁻¹; LOQ = 3.3 × LOD (Pettke 2012) for most elements; LOQ for pollution elements = blank + 10SD (Gold Book IUPAC)" ;
    ada:fundingSourceForAnalysis "Strategy Priority Research Program (Category B) of Chinese Academy of Sciences (XDB0710000); NSFC 42073022" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "LOQ = 3.3 × LOD per Pettke (2012) for most elements; LOQ = blank value + 10SD per IUPAC Gold Book for pollution elements (V, Co, Zn, Ba, La, Ce, Ta, U) where blank contribution is significant" ;
    ada:mappingArea "missing" ;
    ada:numberOfReplicates 9 ;
    ada:oxideProduction "ThO/Th = measured at <0.3%; U/Th = 0.95–1.05 (on NIST SRM 612)" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime 45 ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "Analytical precision (RSD) within 10% for most of 32 trace elements in 6 silicate GRMs (verified by homogeneity index assessment across 9 spots per disk)" .


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
      "@id": "ex:laQicpmsTAPP-Liu2025"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Strategic Priority Research Program (B) of CAS (XDB0840200); NSFC 92062222, 42073057, 42250710679, 42250202, 42273023",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": "~40 s (inferred from typical CetacAnalyte HE protocol; stable signal used)",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "Detection limits for Au ~0.01 ppm; Cu ~0.1 ppm in silicate melt (stated in paper)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "Au and Cu fully dissolved in most glasses (smooth signals); Au results consistent with Au solubility trends from literature; comparison with SN-ICP-MS (solution) for two extraterrestrial samples confirms reliability",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
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
      "@id": "ex:laQicpmsTAPP-Liu2025"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Strategic Priority Research Program (B) of CAS (XDB0840200); NSFC 92062222, 42073057, 42250710679, 42250202, 42273023",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": "~40 s (inferred from typical CetacAnalyte HE protocol; stable signal used)",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "Detection limits for Au ~0.01 ppm; Cu ~0.1 ppm in silicate melt (stated in paper)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "Au and Cu fully dissolved in most glasses (smooth signals); Au results consistent with Au solubility trends from literature; comparison with SN-ICP-MS (solution) for two extraterrestrial samples confirms reliability",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:spotDiameterMeasured": -9999
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Liu2025 a ada:LAICPMSTabular ;
    schema1:measurementTechnique ex:laQicpmsTAPP-Liu2025 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "Au and Cu fully dissolved in most glasses (smooth signals); Au results consistent with Au solubility trends from literature; comparison with SN-ICP-MS (solution) for two extraterrestrial samples confirms reliability" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:LAICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "Detection limits for Au ~0.01 ppm; Cu ~0.1 ppm in silicate melt (stated in paper)" ;
    ada:fundingSourceForAnalysis "Strategic Priority Research Program (B) of CAS (XDB0840200); NSFC 92062222, 42073057, 42250710679, 42250202, 42273023" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime "~40 s (inferred from typical CetacAnalyte HE protocol; stable signal used)" ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .


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
      "@id": "ex:laQicpmsTAPP-Liu2025-2"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Strategic Priority Research Program (B) of CAS (XDB0840200); NSFC 92062222, 42073057, 42250710679, 42250202, 42273023",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": "~40 s (same)",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "Sulfide Au and Cu concentrations consistent with strong positive correlation with log fS₂ (Fig. 5A) confirming thermodynamic equilibrium; partitioning coefficients Dsulfide/melt consistent with literature (Li et al. 2019, 2021)",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
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
      "@id": "ex:laQicpmsTAPP-Liu2025-2"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Strategic Priority Research Program (B) of CAS (XDB0840200); NSFC 92062222, 42073057, 42250710679, 42250202, 42273023",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": "~40 s (same)",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "Sulfide Au and Cu concentrations consistent with strong positive correlation with log fS\u2082 (Fig. 5A) confirming thermodynamic equilibrium; partitioning coefficients Dsulfide/melt consistent with literature (Li et al. 2019, 2021)",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:spotDiameterMeasured": -9999
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Liu2025-2 a ada:LAICPMSTabular ;
    schema1:measurementTechnique ex:laQicpmsTAPP-Liu2025-2 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "Sulfide Au and Cu concentrations consistent with strong positive correlation with log fS₂ (Fig. 5A) confirming thermodynamic equilibrium; partitioning coefficients Dsulfide/melt consistent with literature (Li et al. 2019, 2021)" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:LAICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:fundingSourceForAnalysis "Strategic Priority Research Program (B) of CAS (XDB0840200); NSFC 92062222, 42073057, 42250710679, 42250202, 42273023" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime "~40 s (same)" ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .


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
      "@id": "ex:laQicpmsTAPP-Liu2016"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA Cosmochemistry grants NNX11AG58G (to L.A.T.) and NNN13D465T (to Y.L.); NSF EAR-1226270 (to P.D.A.) and EAR-1019770 (to R.J.B.); Y.L. supported by Jet Propulsion Laboratory",
  "ada:sampleName": "Tissint Martian meteorite",
  "ada:samplingUnit": "missing",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "Referenced in Table 3 and Table S1; specific values not directly stated in main text; REE in olivines below detection limits at 24–32 µm conditions",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "For silicates: oxide-sum normalization agrees within <10% with EMP-based IS method (internal cross-check, not a separate QC standard)",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
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
      "@id": "ex:laQicpmsTAPP-Liu2016"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA Cosmochemistry grants NNX11AG58G (to L.A.T.) and NNN13D465T (to Y.L.); NSF EAR-1226270 (to P.D.A.) and EAR-1019770 (to R.J.B.); Y.L. supported by Jet Propulsion Laboratory",
  "ada:sampleName": "Tissint Martian meteorite",
  "ada:samplingUnit": "missing",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "Referenced in Table 3 and Table S1; specific values not directly stated in main text; REE in olivines below detection limits at 24\u201332 \u00b5m conditions",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "For silicates: oxide-sum normalization agrees within <10% with EMP-based IS method (internal cross-check, not a separate QC standard)",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:spotDiameterMeasured": -9999
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Liu2016 a ada:LAICPMSTabular ;
    schema1:measurementTechnique ex:laQicpmsTAPP-Liu2016 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "For silicates: oxide-sum normalization agrees within <10% with EMP-based IS method (internal cross-check, not a separate QC standard)" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:LAICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "Referenced in Table 3 and Table S1; specific values not directly stated in main text; REE in olivines below detection limits at 24–32 µm conditions" ;
    ada:fundingSourceForAnalysis "NASA Cosmochemistry grants NNX11AG58G (to L.A.T.) and NNN13D465T (to Y.L.); NSF EAR-1226270 (to P.D.A.) and EAR-1019770 (to R.J.B.); Y.L. supported by Jet Propulsion Laboratory" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "Tissint Martian meteorite" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .


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
      "@id": "ex:laQicpmsTAPP-Liu2016-2"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Same as silicate protocol",
  "ada:sampleName": "Tissint Martian meteorite",
  "ada:samplingUnit": "missing",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "Referenced in Table 3 and Table S1; specific values not directly stated in main text; merrillite REE at 14–414 ppm range above detection",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
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
      "@id": "ex:laQicpmsTAPP-Liu2016-2"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Same as silicate protocol",
  "ada:sampleName": "Tissint Martian meteorite",
  "ada:samplingUnit": "missing",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "Referenced in Table 3 and Table S1; specific values not directly stated in main text; merrillite REE at 14\u2013414 ppm range above detection",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:spotDiameterMeasured": -9999
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Liu2016-2 a ada:LAICPMSTabular ;
    schema1:measurementTechnique ex:laQicpmsTAPP-Liu2016-2 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "missing" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:LAICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "Referenced in Table 3 and Table S1; specific values not directly stated in main text; merrillite REE at 14–414 ppm range above detection" ;
    ada:fundingSourceForAnalysis "Same as silicate protocol" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "Tissint Martian meteorite" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .


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
      "@id": "ex:laQicpmsTAPP-P6"
    }
  ],
  "ada:sessionIdentifier": "N — 20 analytical sessions over 3 months referenced, no identifier stated",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Xenotime XN02, MG-1, BS-1, XENOA, M1567; apatite Otter Lake, NW-1, MAP-3; two metamorphic garnets; NIST SRM 610",
  "ada:samplingUnit": "Laser spot — 246 spot analyses on XN02 alone; spot diameters 50-150 um depending on Lu and Hf contents",
  "ada:spotDiameter": 50,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Acquired and included counts both stated: 'A total of 246 spot analyses were undertaken in 20 analytical sessions over 3 months, 236 of which yielded a weighted-mean age of 515.4 +/- 1.2 Ma'. The rejection rule itself is not stated",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "Uncertainties (2SE) of single-spot ages were ~2.6%",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "Precision of common-Hf corrected single-spot ages 1.5-8.1% (xenotime) and 9.2-36.0% (apatite); isochron age uncertainties 3.5-10% for garnet",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "Accuracy of common-Hf corrected single-spot xenotime ages generally better than 1.5%, assessed against ID-TIMS U-Pb ages of the same reference materials",
  "ada:goodnessOfFitOrDispersionStatistic": "MSWD reported with each aggregate age — e.g. MSWD = 2.3 (n = 236, XN02) and MSWD = 0.6 (n = 15, weighted-mean Lu-Hf age 489.8 +/- 2.2 Ma)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsTAPP/uncertaintyPropagationMethod",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/uncertaintyPropagationMethod"
        }
      ],
      "schema:name": "Uncertainty Propagation Method",
      "schema:value": "Uncertainty propagation workflow implemented in IsoplotR"
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
  "@id": "ex:detail-P6",
  "@type": [
    "ada:LAICPMSTabular"
  ],
  "ada:componentType": "ada:LAICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laQicpmsTAPP-P6"
    }
  ],
  "ada:sessionIdentifier": "N \u2014 20 analytical sessions over 3 months referenced, no identifier stated",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Xenotime XN02, MG-1, BS-1, XENOA, M1567; apatite Otter Lake, NW-1, MAP-3; two metamorphic garnets; NIST SRM 610",
  "ada:samplingUnit": "Laser spot \u2014 246 spot analyses on XN02 alone; spot diameters 50-150 um depending on Lu and Hf contents",
  "ada:spotDiameter": 50,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Acquired and included counts both stated: 'A total of 246 spot analyses were undertaken in 20 analytical sessions over 3 months, 236 of which yielded a weighted-mean age of 515.4 +/- 1.2 Ma'. The rejection rule itself is not stated",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "Uncertainties (2SE) of single-spot ages were ~2.6%",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "Precision of common-Hf corrected single-spot ages 1.5-8.1% (xenotime) and 9.2-36.0% (apatite); isochron age uncertainties 3.5-10% for garnet",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "Accuracy of common-Hf corrected single-spot xenotime ages generally better than 1.5%, assessed against ID-TIMS U-Pb ages of the same reference materials",
  "ada:goodnessOfFitOrDispersionStatistic": "MSWD reported with each aggregate age \u2014 e.g. MSWD = 2.3 (n = 236, XN02) and MSWD = 0.6 (n = 15, weighted-mean Lu-Hf age 489.8 +/- 2.2 Ma)",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsTAPP/uncertaintyPropagationMethod",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsTAPP/uncertaintyPropagationMethod"
        }
      ],
      "schema:name": "Uncertainty Propagation Method",
      "schema:value": "Uncertainty propagation workflow implemented in IsoplotR"
    }
  ],
  "ada:spotDiameterMeasured": -9999
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-P6 a ada:LAICPMSTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/uncertaintyPropagationMethod> ;
    schema1:measurementTechnique ex:laQicpmsTAPP-P6 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Acquired and included counts both stated: 'A total of 246 spot analyses were undertaken in 20 analytical sessions over 3 months, 236 of which yielded a weighted-mean age of 515.4 +/- 1.2 Ma'. The rejection rule itself is not stated" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "Accuracy of common-Hf corrected single-spot xenotime ages generally better than 1.5%, assessed against ID-TIMS U-Pb ages of the same reference materials" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:LAICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "MSWD reported with each aggregate age — e.g. MSWD = 2.3 (n = 236, XN02) and MSWD = 0.6 (n = 15, weighted-mean Lu-Hf age 489.8 +/- 2.2 Ma)" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "Uncertainties (2SE) of single-spot ages were ~2.6%" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "Xenotime XN02, MG-1, BS-1, XENOA, M1567; apatite Otter Lake, NW-1, MAP-3; two metamorphic garnets; NIST SRM 610" ;
    ada:samplingUnit "Laser spot — 246 spot analyses on XN02 alone; spot diameters 50-150 um depending on Lu and Hf contents" ;
    ada:sessionIdentifier "N — 20 analytical sessions over 3 months referenced, no identifier stated" ;
    ada:signalIntegrationTime -9999 ;
    ada:spotDiameter 50 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "Precision of common-Hf corrected single-spot ages 1.5-8.1% (xenotime) and 9.2-36.0% (apatite); isochron age uncertainties 3.5-10% for garnet" .

<https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/uncertaintyPropagationMethod> a schema1:PropertyValue ;
    schema1:name "Uncertainty Propagation Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsTAPP/uncertaintyPropagationMethod> ;
    schema1:value "Uncertainty propagation workflow implemented in IsoplotR" .


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
                    schema:additionalProperty:
                      type: array
                      items:
                        anyOf:
                        - title: Sample Form / Analytical Substrate
                          description: Physical form of the material as it enters
                            the ablation cell. Editable to accommodate legitimate
                            variations (e.g., thin section vs. mount) that do not
                            alter the analytical procedure.
                          type: object
                          properties:
                            '@id':
                              const: ada:parameter/laQicpmsTAPP/sampleFormAnalyticalSubstrate
                            '@type':
                              const:
                              - schema:PropertyValue
                            schema:propertyID:
                              const:
                              - '@id': ada:parameter/laQicpmsTAPP/sampleFormAnalyticalSubstrate
                            schema:name:
                              const: Sample Form / Analytical Substrate
                            schema:value:
                              type: string
                          required:
                          - '@id'
                          - '@type'
                          - schema:propertyID
                          - schema:name
                          - schema:value
                        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_mappedAreaDescription
                      allOf:
                      - contains:
                          title: Sample Form / Analytical Substrate
                          description: Physical form of the material as it enters
                            the ablation cell. Editable to accommodate legitimate
                            variations (e.g., thin section vs. mount) that do not
                            alter the analytical procedure.
                          type: object
                          properties:
                            '@id':
                              const: ada:parameter/laQicpmsTAPP/sampleFormAnalyticalSubstrate
                            '@type':
                              const:
                              - schema:PropertyValue
                            schema:propertyID:
                              const:
                              - '@id': ada:parameter/laQicpmsTAPP/sampleFormAnalyticalSubstrate
                            schema:name:
                              const: Sample Form / Analytical Substrate
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
                            - title: Fusion Flux and Dilution Ratio
                              description: For procedures using fused glass, the flux
                                type and sample:flux dilution ratio used to prepare
                                the analytical glass.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laQicpmsTAPP/fusionFluxAndDilutionRatio
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laQicpmsTAPP/fusionFluxAndDilutionRatio
                                schema:name:
                                  const: Fusion Flux and Dilution Ratio
                                schema:value:
                                  type: string
                              required:
                              - '@id'
                              - '@type'
                              - schema:propertyID
                              - schema:name
                              - schema:value
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_preAblationSurfaceTreatment
                          allOf:
                          - contains:
                              title: Fusion Flux and Dilution Ratio
                              description: For procedures using fused glass, the flux
                                type and sample:flux dilution ratio used to prepare
                                the analytical glass.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laQicpmsTAPP/fusionFluxAndDilutionRatio
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laQicpmsTAPP/fusionFluxAndDilutionRatio
                                schema:name:
                                  const: Fusion Flux and Dilution Ratio
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
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_preAblationSurfaceTreatment
                            minContains: 0
                            maxContains: 1
                        schema:description:
                          description: Description of how samples were prepared for
                            analysis (mounting, polishing, coating, fusion procedure,
                            etc.).
                          anyOf:
                          - type: string
                          - type: array
                            items:
                              type: string
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
                            - title: Signal Smoothing
                              description: 'Description of any signal smoothing device
                                or approach installed between the ablation cell and
                                the ICP-MS to reduce pulse-to-pulse signal variability.
                                Note: active signal smoothing devices (e.g., squid,
                                SCFAST) are generally incompatible with high-resolution
                                raster mapping because they degrade spatial resolution
                                by mixing aerosol from successive laser shots. For
                                mapping analyses, report "None" explicitly.'
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laQicpmsTAPP/signalSmoothing
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laQicpmsTAPP/signalSmoothing
                                schema:name:
                                  const: Signal Smoothing
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
                                  const: ada:parameter/laQicpmsTAPP/uncertaintyPropagationMethod
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laQicpmsTAPP/uncertaintyPropagationMethod
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
                            - title: Spike / Outlier Filtering Approach
                              description: Method used to identify and remove anomalous
                                signal spikes arising from micronuggets, inclusions,
                                cracks, or instrument artifacts during time-resolved
                                signal processing. Editable because the specific implementation
                                may vary between sessions while remaining within the
                                procedure framework.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laQicpmsTAPP/spikeOutlierFilteringApproach
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laQicpmsTAPP/spikeOutlierFilteringApproach
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
                                response at the transition between pulse-counting
                                and analog detector modes.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laQicpmsTAPP/pulseAnalogDetectorNonlinearityCorrection
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laQicpmsTAPP/pulseAnalogDetectorNonlinearityCorrection
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
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/calibrationFactor/schema.yaml#/$defs/Param_Analysis_calibrationFactorAndDeterminationMethod
                          allOf:
                          - contains:
                              title: Signal Smoothing
                              description: 'Description of any signal smoothing device
                                or approach installed between the ablation cell and
                                the ICP-MS to reduce pulse-to-pulse signal variability.
                                Note: active signal smoothing devices (e.g., squid,
                                SCFAST) are generally incompatible with high-resolution
                                raster mapping because they degrade spatial resolution
                                by mixing aerosol from successive laser shots. For
                                mapping analyses, report "None" explicitly.'
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laQicpmsTAPP/signalSmoothing
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laQicpmsTAPP/signalSmoothing
                                schema:name:
                                  const: Signal Smoothing
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
                                  const: ada:parameter/laQicpmsTAPP/uncertaintyPropagationMethod
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laQicpmsTAPP/uncertaintyPropagationMethod
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
                              title: Spike / Outlier Filtering Approach
                              description: Method used to identify and remove anomalous
                                signal spikes arising from micronuggets, inclusions,
                                cracks, or instrument artifacts during time-resolved
                                signal processing. Editable because the specific implementation
                                may vary between sessions while remaining within the
                                procedure framework.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laQicpmsTAPP/spikeOutlierFilteringApproach
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laQicpmsTAPP/spikeOutlierFilteringApproach
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
                                response at the transition between pulse-counting
                                and analog detector modes.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laQicpmsTAPP/pulseAnalogDetectorNonlinearityCorrection
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laQicpmsTAPP/pulseAnalogDetectorNonlinearityCorrection
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
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/calibrationFactor/schema.yaml#/$defs/Param_Analysis_calibrationFactorAndDeterminationMethod
                            minContains: 0
                            maxContains: 1
                allOf:
                - contains:
                    properties:
                      schema:name:
                        const: Sample preparation
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
              anyOf:
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/targetSelection/schema.yaml#/$defs/Param_Analysis_targetSelectionCriteria
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/targetSelection/schema.yaml#/$defs/Param_Analysis_preAnalysisImagingAndScreening
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_transectRateMappingRateOrStepSize
              - title: Carrier Gas and Flow Rate
                description: "Gas used to transport ablated aerosol from the ablation
                  cell to the ICP-MS torch, with the procedure-registered target flow
                  rate(s). Helium is standard for most UV laser systems due to superior
                  aerosol transport. Flow rates are procedure targets; actual session
                  values may be adjusted within \xB110% during tuning."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laQicpmsTAPP/carrierGasAndFlowRate
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laQicpmsTAPP/carrierGasAndFlowRate
                  schema:name:
                    const: Carrier Gas and Flow Rate
                  schema:value:
                    type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - title: Make-up Gas and Flow Rate
                description: "Supplementary gas added to the sample-carrying stream
                  between the sample introduction system and the plasma, with its
                  identity and the procedure-registered target flow rate. Argon make-up
                  is standard and maintains total gas delivery where the carrier flow
                  alone is insufficient \u2014 downstream of an ablation cell, or
                  of a desolvation system that has removed solvent load. Small nitrogen
                  or hydrogen additions are also made here to enhance sensitivity
                  for some elements; record them with their own flow, whose unit commonly
                  differs from the make-up flow. Record 'None' explicitly where no
                  supplementary gas is added, to distinguish it from not reported."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laQicpmsTAPP/makeUpGasAndFlowRate
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laQicpmsTAPP/makeUpGasAndFlowRate
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
              - title: Analysis Sequence
                description: Repeating order of primary calibration standard(s), quality
                  control standard(s), and unknown analyses within a measurement session.
                  Editable to allow minor adjustments while maintaining the bracketing
                  strategy defined in the procedure.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laQicpmsTAPP/analysisSequence
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laQicpmsTAPP/analysisSequence
                  schema:name:
                    const: Analysis Sequence
                  schema:value:
                    type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - title: Ion Counter Dead Time
                description: Dead time of each ion-counting detector channel, used
                  in the dead-time correction applied to high count rates. Distinct
                  from pulse/analog cross-calibration, which relates the two detector
                  modes rather than correcting counting losses within the pulse-counting
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
                  times. Sets the time resolution of the downhole signal, and is not
                  recoverable from Dwell Time per Mass alone because settling time
                  is not captured there. Applies to sequential (quadrupole and single-collector
                  sector-field) acquisition."
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
              - title: Background Count Time
                description: Total time spent measuring gas blank (background signal
                  with laser off or shutter closed) before each ablation event, in
                  seconds. For spot and transect analysis, a discrete background interval
                  is measured before each ablation. For mapping, background is typically
                  measured once per raster line or at the start of a map session rather
                  than before each individual pixel. Editable to allow session-specific
                  adjustment.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laQicpmsTAPP/backgroundCountTime
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laQicpmsTAPP/backgroundCountTime
                  schema:name:
                    const: Background Count Time
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
              - title: Number of Replicates
                description: Number of replicate measurements performed on the same
                  sample, or on the same nominal location where the technique is spatially
                  resolved. For spot analysis this is the number of individual spots
                  per grain or location; for transects, the number of replicate lines;
                  for mapping, the number of map acquisitions of the same area; for
                  solution work, the number of discrete replicate measurements acquired
                  per sample solution. The procedure registers an intended count where
                  it has one; the analysis records the count actually acquired.
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
              - title: Mapping Area
                description: "Total area covered by the 2D raster map, expressed as
                  width \xD7 height in \xB5m or as total area in \xB5m\xB2 or mm\xB2.
                  This is an analysis-level parameter because it depends on the size
                  of the grain or phase to be mapped. The procedure fixes scan speed,
                  line spacing, and spot size; the map area is chosen at analysis
                  time to cover the target feature."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laQicpmsTAPP/mappingArea
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laQicpmsTAPP/mappingArea
                  schema:name:
                    const: Mapping Area
                  schema:value:
                    type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - title: Signal Integration Time
                description: 'Actual integration time used for the ablation signal
                  in this analysis, in seconds. This is an analysis-level outcome
                  determined during data reduction by applying the Signal Integration
                  Interval Method to the time-resolved signal. It is equal to or shorter
                  than the Ablation Duration per Spot because the signal start and
                  end transients are typically discarded. Not applicable to mapping
                  analysis: for mapping, the equivalent concept is the per-pixel cycle
                  time, which is determined by the spectrometer dwell time settings
                  (a procedure-level field) rather than being an analysis-level outcome.'
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laQicpmsTAPP/signalIntegrationTime
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laQicpmsTAPP/signalIntegrationTime
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
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Analysis_constantsReferenceValues
            allOf:
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/targetSelection/schema.yaml#/$defs/Param_Analysis_targetSelectionCriteria
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/targetSelection/schema.yaml#/$defs/Param_Analysis_preAnalysisImagingAndScreening
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_transectRateMappingRateOrStepSize
              minContains: 0
              maxContains: 1
            - contains:
                title: Carrier Gas and Flow Rate
                description: "Gas used to transport ablated aerosol from the ablation
                  cell to the ICP-MS torch, with the procedure-registered target flow
                  rate(s). Helium is standard for most UV laser systems due to superior
                  aerosol transport. Flow rates are procedure targets; actual session
                  values may be adjusted within \xB110% during tuning."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laQicpmsTAPP/carrierGasAndFlowRate
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laQicpmsTAPP/carrierGasAndFlowRate
                  schema:name:
                    const: Carrier Gas and Flow Rate
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
                title: Make-up Gas and Flow Rate
                description: "Supplementary gas added to the sample-carrying stream
                  between the sample introduction system and the plasma, with its
                  identity and the procedure-registered target flow rate. Argon make-up
                  is standard and maintains total gas delivery where the carrier flow
                  alone is insufficient \u2014 downstream of an ablation cell, or
                  of a desolvation system that has removed solvent load. Small nitrogen
                  or hydrogen additions are also made here to enhance sensitivity
                  for some elements; record them with their own flow, whose unit commonly
                  differs from the make-up flow. Record 'None' explicitly where no
                  supplementary gas is added, to distinguish it from not reported."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laQicpmsTAPP/makeUpGasAndFlowRate
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laQicpmsTAPP/makeUpGasAndFlowRate
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
            - contains:
                title: Analysis Sequence
                description: Repeating order of primary calibration standard(s), quality
                  control standard(s), and unknown analyses within a measurement session.
                  Editable to allow minor adjustments while maintaining the bracketing
                  strategy defined in the procedure.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laQicpmsTAPP/analysisSequence
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laQicpmsTAPP/analysisSequence
                  schema:name:
                    const: Analysis Sequence
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
                description: Dead time of each ion-counting detector channel, used
                  in the dead-time correction applied to high count rates. Distinct
                  from pulse/analog cross-calibration, which relates the two detector
                  modes rather than correcting counting losses within the pulse-counting
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
                  times. Sets the time resolution of the downhole signal, and is not
                  recoverable from Dwell Time per Mass alone because settling time
                  is not captured there. Applies to sequential (quadrupole and single-collector
                  sector-field) acquisition."
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
                title: Background Count Time
                description: Total time spent measuring gas blank (background signal
                  with laser off or shutter closed) before each ablation event, in
                  seconds. For spot and transect analysis, a discrete background interval
                  is measured before each ablation. For mapping, background is typically
                  measured once per raster line or at the start of a map session rather
                  than before each individual pixel. Editable to allow session-specific
                  adjustment.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laQicpmsTAPP/backgroundCountTime
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laQicpmsTAPP/backgroundCountTime
                  schema:name:
                    const: Background Count Time
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
                title: Number of Replicates
                description: Number of replicate measurements performed on the same
                  sample, or on the same nominal location where the technique is spatially
                  resolved. For spot analysis this is the number of individual spots
                  per grain or location; for transects, the number of replicate lines;
                  for mapping, the number of map acquisitions of the same area; for
                  solution work, the number of discrete replicate measurements acquired
                  per sample solution. The procedure registers an intended count where
                  it has one; the analysis records the count actually acquired.
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
                title: Mapping Area
                description: "Total area covered by the 2D raster map, expressed as
                  width \xD7 height in \xB5m or as total area in \xB5m\xB2 or mm\xB2.
                  This is an analysis-level parameter because it depends on the size
                  of the grain or phase to be mapped. The procedure fixes scan speed,
                  line spacing, and spot size; the map area is chosen at analysis
                  time to cover the target feature."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laQicpmsTAPP/mappingArea
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laQicpmsTAPP/mappingArea
                  schema:name:
                    const: Mapping Area
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
                title: Signal Integration Time
                description: 'Actual integration time used for the ablation signal
                  in this analysis, in seconds. This is an analysis-level outcome
                  determined during data reduction by applying the Signal Integration
                  Interval Method to the time-resolved signal. It is equal to or shorter
                  than the Ablation Duration per Spot because the signal start and
                  end transients are typically discarded. Not applicable to mapping
                  analysis: for mapping, the equivalent concept is the per-pixel cycle
                  time, which is determined by the spectrometer dwell time settings
                  (a procedure-level field) rather than being an analysis-level outcome.'
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laQicpmsTAPP/signalIntegrationTime
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laQicpmsTAPP/signalIntegrationTime
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
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Analysis_constantsReferenceValues
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
                                                  const: ada:parameter/laQicpmsTAPP/torchDepth
                                                '@type':
                                                  const:
                                                  - schema:PropertyValue
                                                schema:propertyID:
                                                  const:
                                                  - '@id': ada:parameter/laQicpmsTAPP/torchDepth
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
                                                    const: ada:parameter/laQicpmsTAPP/torchDepth
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/laQicpmsTAPP/torchDepth
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
                                              - title: Coolant (Plasma) Gas Flow Rate
                                                description: Flow rate of the outer
                                                  (coolant/plasma) argon gas stream
                                                  that sustains the ICP plasma, in
                                                  L/min. Determines plasma volume
                                                  and stability. Set during initial
                                                  plasma optimisation and confirmed
                                                  at each session start.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/laQicpmsTAPP/coolantGasFlowRate
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/laQicpmsTAPP/coolantGasFlowRate
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
                                                  (auxiliary) argon gas stream that
                                                  positions the plasma relative to
                                                  the load coil, in L/min. Affects
                                                  ion extraction efficiency and oxide
                                                  production rates. Distinct from
                                                  the carrier gas (which transports
                                                  ablation aerosol) and the coolant
                                                  (plasma) gas.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/laQicpmsTAPP/auxiliaryGasFlowRate
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/laQicpmsTAPP/auxiliaryGasFlowRate
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
                                              - title: RF Power
                                                description: ICP radiofrequency forward
                                                  power in watts. Affects plasma temperature,
                                                  ionisation efficiency, oxide formation,
                                                  and whether cool or normal plasma
                                                  conditions are in effect. The procedure
                                                  registers a target value optimised
                                                  during initial setup; the analyst
                                                  confirms or fine-adjusts during
                                                  session tuning.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/laQicpmsTAPP/rfPower
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/laQicpmsTAPP/rfPower
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
                                            allOf:
                                            - contains:
                                                title: Coolant (Plasma) Gas Flow Rate
                                                description: Flow rate of the outer
                                                  (coolant/plasma) argon gas stream
                                                  that sustains the ICP plasma, in
                                                  L/min. Determines plasma volume
                                                  and stability. Set during initial
                                                  plasma optimisation and confirmed
                                                  at each session start.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/laQicpmsTAPP/coolantGasFlowRate
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/laQicpmsTAPP/coolantGasFlowRate
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
                                                  (auxiliary) argon gas stream that
                                                  positions the plasma relative to
                                                  the load coil, in L/min. Affects
                                                  ion extraction efficiency and oxide
                                                  production rates. Distinct from
                                                  the carrier gas (which transports
                                                  ablation aerosol) and the coolant
                                                  (plasma) gas.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/laQicpmsTAPP/auxiliaryGasFlowRate
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/laQicpmsTAPP/auxiliaryGasFlowRate
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
                                            - contains:
                                                title: RF Power
                                                description: ICP radiofrequency forward
                                                  power in watts. Affects plasma temperature,
                                                  ionisation efficiency, oxide formation,
                                                  and whether cool or normal plasma
                                                  conditions are in effect. The procedure
                                                  registers a target value optimised
                                                  during initial setup; the analyst
                                                  confirms or fine-adjusts during
                                                  session tuning.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/laQicpmsTAPP/rfPower
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/laQicpmsTAPP/rfPower
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
                                                  gas (typically He) introduced into
                                                  the collision/reaction cell, in
                                                  mL/min. Controls the degree of ion
                                                  thermalization and KED efficiency.
                                                  Record 'None' if the CRC is in STD
                                                  mode.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/laQicpmsTAPP/collisionGasFlowRate
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/laQicpmsTAPP/collisionGasFlowRate
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
                                                description: Bias voltage applied
                                                  at the collision/reaction cell exit
                                                  to discriminate between analyte
                                                  ions and low-energy polyatomic interferences
                                                  in KED mode, in volts (V). A negative
                                                  bias preferentially retards slow
                                                  polyatomic ions while transmitting
                                                  faster analyte ions. Record 'None'
                                                  if the CRC is in STD mode.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/laQicpmsTAPP/cellExitDiscriminationVoltage
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/laQicpmsTAPP/cellExitDiscriminationVoltage
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
                                                description: Flow rate of the reactive
                                                  gas introduced into the dynamic
                                                  reaction cell (DRC), in mL/min.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/laQicpmsTAPP/reactionGasFlowRate
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/laQicpmsTAPP/reactionGasFlowRate
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
                                                  gas (typically He) introduced into
                                                  the collision/reaction cell, in
                                                  mL/min. Controls the degree of ion
                                                  thermalization and KED efficiency.
                                                  Record 'None' if the CRC is in STD
                                                  mode.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/laQicpmsTAPP/collisionGasFlowRate
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/laQicpmsTAPP/collisionGasFlowRate
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
                                                description: Bias voltage applied
                                                  at the collision/reaction cell exit
                                                  to discriminate between analyte
                                                  ions and low-energy polyatomic interferences
                                                  in KED mode, in volts (V). A negative
                                                  bias preferentially retards slow
                                                  polyatomic ions while transmitting
                                                  faster analyte ions. Record 'None'
                                                  if the CRC is in STD mode.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/laQicpmsTAPP/cellExitDiscriminationVoltage
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/laQicpmsTAPP/cellExitDiscriminationVoltage
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
                                                description: Flow rate of the reactive
                                                  gas introduced into the dynamic
                                                  reaction cell (DRC), in mL/min.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/laQicpmsTAPP/reactionGasFlowRate
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/laQicpmsTAPP/reactionGasFlowRate
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
                                    - title: Mass Resolution Setting
                                      description: Operating mass resolution of the
                                        mass analyser. For quadrupole instruments
                                        this is fixed at unit resolution by instrument
                                        design.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/laQicpmsTAPP/massResolutionSetting
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/laQicpmsTAPP/massResolutionSetting
                                        schema:name:
                                          const: Mass Resolution Setting
                                        schema:value:
                                          type: string
                                      required:
                                      - '@id'
                                      - '@type'
                                      - schema:propertyID
                                      - schema:name
                                      - schema:value
                                    - title: ICP Tuning
                                      description: Description of the approach used
                                        to optimise ICP plasma conditions prior to
                                        analysis, including the reference material
                                        used for tuning and the acceptance criteria
                                        (e.g., oxide production threshold, sensitivity
                                        targets, mass calibration).
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/laQicpmsTAPP/icpTuning
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/laQicpmsTAPP/icpTuning
                                        schema:name:
                                          const: ICP Tuning
                                        schema:value:
                                          type: string
                                      required:
                                      - '@id'
                                      - '@type'
                                      - schema:propertyID
                                      - schema:name
                                      - schema:value
                                    - title: Doubly-Charged Species Monitor
                                      description: "The mass ratio monitored to estimate
                                        doubly-charged ion (M\xB2\u207A) formation
                                        during instrument tuning. Doubly-charged ions
                                        appear at half the mass of the parent ion
                                        and can cause isobaric interferences on analytes
                                        in that mass region. The monitor species and
                                        the mass positions monitored should be stated
                                        explicitly. Analogous to Oxide Production
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
                                        the time of instrument tuning. The procedure
                                        should specify the acceptable threshold (e.g.,
                                        <1%, <3%); the measured value for each session
                                        is recorded here. Report both the threshold
                                        and the measured value where possible.
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
                                    - title: Memory Effect Mitigation
                                      description: Procedure applied to identify and
                                        minimise memory effects from high-concentration
                                        elements in the previous sample or standard
                                        that may contaminate subsequent analyses,
                                        or from incomplete aerosol washout between
                                        adjacent pixels in raster mapping mode. For
                                        mapping, the mitigation strategy involves
                                        controlling scan speed relative to washout
                                        time to ensure each pixel signal is sufficiently
                                        free of the preceding pixel's contribution.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/laQicpmsTAPP/memoryEffectMitigation
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/laQicpmsTAPP/memoryEffectMitigation
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
                                      title: Mass Resolution Setting
                                      description: Operating mass resolution of the
                                        mass analyser. For quadrupole instruments
                                        this is fixed at unit resolution by instrument
                                        design.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/laQicpmsTAPP/massResolutionSetting
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/laQicpmsTAPP/massResolutionSetting
                                        schema:name:
                                          const: Mass Resolution Setting
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
                                      title: ICP Tuning
                                      description: Description of the approach used
                                        to optimise ICP plasma conditions prior to
                                        analysis, including the reference material
                                        used for tuning and the acceptance criteria
                                        (e.g., oxide production threshold, sensitivity
                                        targets, mass calibration).
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/laQicpmsTAPP/icpTuning
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/laQicpmsTAPP/icpTuning
                                        schema:name:
                                          const: ICP Tuning
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
                                      title: Doubly-Charged Species Monitor
                                      description: "The mass ratio monitored to estimate
                                        doubly-charged ion (M\xB2\u207A) formation
                                        during instrument tuning. Doubly-charged ions
                                        appear at half the mass of the parent ion
                                        and can cause isobaric interferences on analytes
                                        in that mass region. The monitor species and
                                        the mass positions monitored should be stated
                                        explicitly. Analogous to Oxide Production
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
                                        the time of instrument tuning. The procedure
                                        should specify the acceptable threshold (e.g.,
                                        <1%, <3%); the measured value for each session
                                        is recorded here. Report both the threshold
                                        and the measured value where possible.
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
                                      title: Memory Effect Mitigation
                                      description: Procedure applied to identify and
                                        minimise memory effects from high-concentration
                                        elements in the previous sample or standard
                                        that may contaminate subsequent analyses,
                                        or from incomplete aerosol washout between
                                        adjacent pixels in raster mapping mode. For
                                        mapping, the mitigation strategy involves
                                        controlling scan speed relative to washout
                                        time to ensure each pixel signal is sufficiently
                                        free of the preceding pixel's contribution.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/laQicpmsTAPP/memoryEffectMitigation
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/laQicpmsTAPP/memoryEffectMitigation
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
                                  description: Primary reference material(s) used
                                    to calibrate the instrument and convert raw signal
                                    intensities to concentrations or isotope ratios.
                                    Include material name, source institution, and
                                    citation for the accepted values used. Editable
                                    because the specific lot or certification vintage
                                    may differ between sessions while the material
                                    type remains the same.
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
                                  description: Quality-control reference materials
                                    analysed as unknowns alongside samples in the
                                    same session to assess accuracy and monitor drift.
                                    Include material name, source, and citation for
                                    accepted values used for comparison. Editable
                                    because selection of secondary RMs may vary across
                                    sessions.
                                  anyOf:
                                  - type: string
                                  - type: array
                                    items:
                                      type: string
                          required:
                          - ada:reagentRole
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
    "wd": "https://www.wikidata.org/entity/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "cdif": "https://w3id.org/cdif/",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcat": "http://www.w3.org/ns/dcat#",
    "dqv": "http://www.w3.org/ns/dqv#",
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

