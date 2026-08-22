
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
      "@id": "ex:laQicpmsUPbTAPP-Nakanishi2022"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "JSPS Grant-in-Aid for Scientific Research (grants 26106002, 26220713, 16H04081, 19H00715, 19H01081, 20H04609)"
    }
  ],
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:spotDiameterMeasured": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:radiogenicFractionOfMeasuredSignal": "missing",
  "ada:ageDatumReferenceEpoch": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "Analytical uncertainties: 2SE of individual spot measurements reported alongside data",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsUPbTAPP/uncertaintyPropagationMethod",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsUPbTAPP/uncertaintyPropagationMethod"
        }
      ],
      "schema:name": "Uncertainty Propagation Method",
      "schema:value": "2SE of individual spot measurements reported"
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
      "@id": "ex:laQicpmsUPbTAPP-Nakanishi2022"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "JSPS Grant-in-Aid for Scientific Research (grants 26106002, 26220713, 16H04081, 19H00715, 19H01081, 20H04609)"
    }
  ],
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:spotDiameterMeasured": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:radiogenicFractionOfMeasuredSignal": "missing",
  "ada:ageDatumReferenceEpoch": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "Analytical uncertainties: 2SE of individual spot measurements reported alongside data",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laQicpmsUPbTAPP/uncertaintyPropagationMethod",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laQicpmsUPbTAPP/uncertaintyPropagationMethod"
        }
      ],
      "schema:name": "Uncertainty Propagation Method",
      "schema:value": "2SE of individual spot measurements reported"
    }
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Nakanishi2022 a ada:LAICPMSGeochronTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/uncertaintyPropagationMethod> ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "JSPS Grant-in-Aid for Scientific Research (grants 26106002, 26220713, 16H04081, 19H00715, 19H01081, 20H04609)" ] ;
    schema1:measurementTechnique ex:laQicpmsUPbTAPP-Nakanishi2022 ;
    ada:ageDatumReferenceEpoch "missing" ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "missing" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:LAICPMSGeochronTabular" ;
    ada:detectionLimit -9999 ;
    ada:errorCorrelationBetweenReportedQuantities -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:radiogenicFractionOfMeasuredSignal "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "Analytical uncertainties: 2SE of individual spot measurements reported alongside data" .

<https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/uncertaintyPropagationMethod> a schema1:PropertyValue ;
    schema1:name "Uncertainty Propagation Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laQicpmsUPbTAPP/uncertaintyPropagationMethod> ;
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
    "ada:LAICPMSGeochronTabular"
  ],
  "ada:componentType": "ada:LAICPMSGeochronTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laQicpmsUPbTAPP-Liu2024"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "Strategy Priority Research Program (Category B) of Chinese Academy of Sciences (XDB0710000); NSFC 42073022"
    }
  ],
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:spotDiameterMeasured": -9999,
  "ada:oxideProduction": "ThO/Th = measured at <0.3%; U/Th = 0.95–1.05 (on NIST SRM 612)",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": 9,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": 45,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:radiogenicFractionOfMeasuredSignal": "missing",
  "ada:ageDatumReferenceEpoch": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:detectionLimit": "LODs for 32 elements in Li-borate glass BHVO-2: 0.005–23.5 µg g⁻¹ (dilution-limited; much higher than undiluted glass LODs); LODs for NIST 610: 0.007–0.45 µg g⁻¹; LOQ = 3.3 × LOD (Pettke 2012) for most elements; LOQ for pollution elements = blank + 10SD (Gold Book IUPAC)",
  "ada:limitOfQuantificationMethod": "LOQ = 3.3 × LOD per Pettke (2012) for most elements; LOQ = blank value + 10SD per IUPAC Gold Book for pollution elements (V, Co, Zn, Ba, La, Ce, Ta, U) where blank contribution is significant",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "Analytical precision (RSD) within 10% for most of 32 trace elements in 6 silicate GRMs (verified by homogeneity index assessment across 9 spots per disk)",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "Analytical results within 10% of reference values for most of 32 trace elements in 6 GRMs (mafic to felsic); precision (RSD) within 10% for most elements; lunar basalt (NWA14526) and shergottite (NWA13190) results compared with SN-ICP-MS and found reliable",
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
      "@id": "ex:laQicpmsUPbTAPP-Liu2024"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "Strategy Priority Research Program (Category B) of Chinese Academy of Sciences (XDB0710000); NSFC 42073022"
    }
  ],
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:spotDiameterMeasured": -9999,
  "ada:oxideProduction": "ThO/Th = measured at <0.3%; U/Th = 0.95\u20131.05 (on NIST SRM 612)",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": 9,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": 45,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:radiogenicFractionOfMeasuredSignal": "missing",
  "ada:ageDatumReferenceEpoch": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:detectionLimit": "LODs for 32 elements in Li-borate glass BHVO-2: 0.005\u201323.5 \u00b5g g\u207b\u00b9 (dilution-limited; much higher than undiluted glass LODs); LODs for NIST 610: 0.007\u20130.45 \u00b5g g\u207b\u00b9; LOQ = 3.3 \u00d7 LOD (Pettke 2012) for most elements; LOQ for pollution elements = blank + 10SD (Gold Book IUPAC)",
  "ada:limitOfQuantificationMethod": "LOQ = 3.3 \u00d7 LOD per Pettke (2012) for most elements; LOQ = blank value + 10SD per IUPAC Gold Book for pollution elements (V, Co, Zn, Ba, La, Ce, Ta, U) where blank contribution is significant",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "Analytical precision (RSD) within 10% for most of 32 trace elements in 6 silicate GRMs (verified by homogeneity index assessment across 9 spots per disk)",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "Analytical results within 10% of reference values for most of 32 trace elements in 6 GRMs (mafic to felsic); precision (RSD) within 10% for most elements; lunar basalt (NWA14526) and shergottite (NWA13190) results compared with SN-ICP-MS and found reliable",
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Liu2024 a ada:LAICPMSGeochronTabular ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "Strategy Priority Research Program (Category B) of Chinese Academy of Sciences (XDB0710000); NSFC 42073022" ] ;
    schema1:measurementTechnique ex:laQicpmsUPbTAPP-Liu2024 ;
    ada:ageDatumReferenceEpoch "missing" ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "Analytical results within 10% of reference values for most of 32 trace elements in 6 GRMs (mafic to felsic); precision (RSD) within 10% for most elements; lunar basalt (NWA14526) and shergottite (NWA13190) results compared with SN-ICP-MS and found reliable" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:LAICPMSGeochronTabular" ;
    ada:detectionLimit "LODs for 32 elements in Li-borate glass BHVO-2: 0.005–23.5 µg g⁻¹ (dilution-limited; much higher than undiluted glass LODs); LODs for NIST 610: 0.007–0.45 µg g⁻¹; LOQ = 3.3 × LOD (Pettke 2012) for most elements; LOQ for pollution elements = blank + 10SD (Gold Book IUPAC)" ;
    ada:errorCorrelationBetweenReportedQuantities -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:limitOfQuantificationMethod "LOQ = 3.3 × LOD per Pettke (2012) for most elements; LOQ = blank value + 10SD per IUPAC Gold Book for pollution elements (V, Co, Zn, Ba, La, Ce, Ta, U) where blank contribution is significant" ;
    ada:mappingArea "missing" ;
    ada:numberOfReplicates 9 ;
    ada:oxideProduction "ThO/Th = measured at <0.3%; U/Th = 0.95–1.05 (on NIST SRM 612)" ;
    ada:proceduralBlankLevel "missing" ;
    ada:radiogenicFractionOfMeasuredSignal "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime 45 ;
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
    "ada:LAICPMSGeochronTabular"
  ],
  "ada:componentType": "ada:LAICPMSGeochronTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laQicpmsUPbTAPP-Liu2025"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "Strategic Priority Research Program (B) of CAS (XDB0840200); NSFC 92062222, 42073057, 42250710679, 42250202, 42273023"
    }
  ],
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:spotDiameterMeasured": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": "~40 s (inferred from typical CetacAnalyte HE protocol; stable signal used)",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:radiogenicFractionOfMeasuredSignal": "missing",
  "ada:ageDatumReferenceEpoch": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:detectionLimit": "Detection limits for Au ~0.01 ppm; Cu ~0.1 ppm in silicate melt (stated in paper)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "Au and Cu fully dissolved in most glasses (smooth signals); Au results consistent with Au solubility trends from literature; comparison with SN-ICP-MS (solution) for two extraterrestrial samples confirms reliability",
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
      "@id": "ex:laQicpmsUPbTAPP-Liu2025"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "Strategic Priority Research Program (B) of CAS (XDB0840200); NSFC 92062222, 42073057, 42250710679, 42250202, 42273023"
    }
  ],
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:spotDiameterMeasured": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": "~40 s (inferred from typical CetacAnalyte HE protocol; stable signal used)",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:radiogenicFractionOfMeasuredSignal": "missing",
  "ada:ageDatumReferenceEpoch": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:detectionLimit": "Detection limits for Au ~0.01 ppm; Cu ~0.1 ppm in silicate melt (stated in paper)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "Au and Cu fully dissolved in most glasses (smooth signals); Au results consistent with Au solubility trends from literature; comparison with SN-ICP-MS (solution) for two extraterrestrial samples confirms reliability",
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Liu2025 a ada:LAICPMSGeochronTabular ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "Strategic Priority Research Program (B) of CAS (XDB0840200); NSFC 92062222, 42073057, 42250710679, 42250202, 42273023" ] ;
    schema1:measurementTechnique ex:laQicpmsUPbTAPP-Liu2025 ;
    ada:ageDatumReferenceEpoch "missing" ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "Au and Cu fully dissolved in most glasses (smooth signals); Au results consistent with Au solubility trends from literature; comparison with SN-ICP-MS (solution) for two extraterrestrial samples confirms reliability" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:LAICPMSGeochronTabular" ;
    ada:detectionLimit "Detection limits for Au ~0.01 ppm; Cu ~0.1 ppm in silicate melt (stated in paper)" ;
    ada:errorCorrelationBetweenReportedQuantities -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:radiogenicFractionOfMeasuredSignal "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime "~40 s (inferred from typical CetacAnalyte HE protocol; stable signal used)" ;
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
    "ada:LAICPMSGeochronTabular"
  ],
  "ada:componentType": "ada:LAICPMSGeochronTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laQicpmsUPbTAPP-Liu2025-2"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "Strategic Priority Research Program (B) of CAS (XDB0840200); NSFC 92062222, 42073057, 42250710679, 42250202, 42273023"
    }
  ],
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:spotDiameterMeasured": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": "~40 s (same)",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:radiogenicFractionOfMeasuredSignal": "missing",
  "ada:ageDatumReferenceEpoch": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "Sulfide Au and Cu concentrations consistent with strong positive correlation with log fS₂ (Fig. 5A) confirming thermodynamic equilibrium; partitioning coefficients Dsulfide/melt consistent with literature (Li et al. 2019, 2021)",
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
      "@id": "ex:laQicpmsUPbTAPP-Liu2025-2"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "Strategic Priority Research Program (B) of CAS (XDB0840200); NSFC 92062222, 42073057, 42250710679, 42250202, 42273023"
    }
  ],
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:spotDiameterMeasured": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": "~40 s (same)",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:radiogenicFractionOfMeasuredSignal": "missing",
  "ada:ageDatumReferenceEpoch": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "Sulfide Au and Cu concentrations consistent with strong positive correlation with log fS\u2082 (Fig. 5A) confirming thermodynamic equilibrium; partitioning coefficients Dsulfide/melt consistent with literature (Li et al. 2019, 2021)",
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Liu2025-2 a ada:LAICPMSGeochronTabular ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "Strategic Priority Research Program (B) of CAS (XDB0840200); NSFC 92062222, 42073057, 42250710679, 42250202, 42273023" ] ;
    schema1:measurementTechnique ex:laQicpmsUPbTAPP-Liu2025-2 ;
    ada:ageDatumReferenceEpoch "missing" ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "Sulfide Au and Cu concentrations consistent with strong positive correlation with log fS₂ (Fig. 5A) confirming thermodynamic equilibrium; partitioning coefficients Dsulfide/melt consistent with literature (Li et al. 2019, 2021)" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:LAICPMSGeochronTabular" ;
    ada:detectionLimit -9999 ;
    ada:errorCorrelationBetweenReportedQuantities -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:radiogenicFractionOfMeasuredSignal "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime "~40 s (same)" ;
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
    "ada:LAICPMSGeochronTabular"
  ],
  "ada:componentType": "ada:LAICPMSGeochronTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laQicpmsUPbTAPP-Liu2016"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA Cosmochemistry grants NNX11AG58G (to L.A.T.) and NNN13D465T (to Y.L.); NSF EAR-1226270 (to P.D.A.) and EAR-1019770 (to R.J.B.); Y.L. supported by Jet Propulsion Laboratory"
    }
  ],
  "ada:sampleName": "Tissint Martian meteorite",
  "ada:samplingUnit": "missing",
  "ada:spotDiameterMeasured": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:radiogenicFractionOfMeasuredSignal": "missing",
  "ada:ageDatumReferenceEpoch": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:detectionLimit": "Referenced in Table 3 and Table S1; specific values not directly stated in main text; REE in olivines below detection limits at 24–32 µm conditions",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "For silicates: oxide-sum normalization agrees within <10% with EMP-based IS method (internal cross-check, not a separate QC standard)",
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
      "@id": "ex:laQicpmsUPbTAPP-Liu2016"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "NASA Cosmochemistry grants NNX11AG58G (to L.A.T.) and NNN13D465T (to Y.L.); NSF EAR-1226270 (to P.D.A.) and EAR-1019770 (to R.J.B.); Y.L. supported by Jet Propulsion Laboratory"
    }
  ],
  "ada:sampleName": "Tissint Martian meteorite",
  "ada:samplingUnit": "missing",
  "ada:spotDiameterMeasured": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:radiogenicFractionOfMeasuredSignal": "missing",
  "ada:ageDatumReferenceEpoch": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:detectionLimit": "Referenced in Table 3 and Table S1; specific values not directly stated in main text; REE in olivines below detection limits at 24\u201332 \u00b5m conditions",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "For silicates: oxide-sum normalization agrees within <10% with EMP-based IS method (internal cross-check, not a separate QC standard)",
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Liu2016 a ada:LAICPMSGeochronTabular ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NASA Cosmochemistry grants NNX11AG58G (to L.A.T.) and NNN13D465T (to Y.L.); NSF EAR-1226270 (to P.D.A.) and EAR-1019770 (to R.J.B.); Y.L. supported by Jet Propulsion Laboratory" ] ;
    schema1:measurementTechnique ex:laQicpmsUPbTAPP-Liu2016 ;
    ada:ageDatumReferenceEpoch "missing" ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "For silicates: oxide-sum normalization agrees within <10% with EMP-based IS method (internal cross-check, not a separate QC standard)" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:LAICPMSGeochronTabular" ;
    ada:detectionLimit "Referenced in Table 3 and Table S1; specific values not directly stated in main text; REE in olivines below detection limits at 24–32 µm conditions" ;
    ada:errorCorrelationBetweenReportedQuantities -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:radiogenicFractionOfMeasuredSignal "missing" ;
    ada:sampleName "Tissint Martian meteorite" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
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
    "ada:LAICPMSGeochronTabular"
  ],
  "ada:componentType": "ada:LAICPMSGeochronTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laQicpmsUPbTAPP-Liu2016-2"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "Same as silicate protocol"
    }
  ],
  "ada:sampleName": "Tissint Martian meteorite",
  "ada:samplingUnit": "missing",
  "ada:spotDiameterMeasured": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:radiogenicFractionOfMeasuredSignal": "missing",
  "ada:ageDatumReferenceEpoch": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:detectionLimit": "Referenced in Table 3 and Table S1; specific values not directly stated in main text; merrillite REE at 14–414 ppm range above detection",
  "ada:limitOfQuantificationMethod": "missing",
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
      "@id": "ex:laQicpmsUPbTAPP-Liu2016-2"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "schema:funding": [
    {
      "@type": [
        "schema:MonetaryGrant"
      ],
      "schema:name": "Same as silicate protocol"
    }
  ],
  "ada:sampleName": "Tissint Martian meteorite",
  "ada:samplingUnit": "missing",
  "ada:spotDiameterMeasured": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:radiogenicFractionOfMeasuredSignal": "missing",
  "ada:ageDatumReferenceEpoch": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:detectionLimit": "Referenced in Table 3 and Table S1; specific values not directly stated in main text; merrillite REE at 14\u2013414 ppm range above detection",
  "ada:limitOfQuantificationMethod": "missing",
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

ex:detail-Liu2016-2 a ada:LAICPMSGeochronTabular ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "Same as silicate protocol" ] ;
    schema1:measurementTechnique ex:laQicpmsUPbTAPP-Liu2016-2 ;
    ada:ageDatumReferenceEpoch "missing" ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "missing" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:LAICPMSGeochronTabular" ;
    ada:detectionLimit "Referenced in Table 3 and Table S1; specific values not directly stated in main text; merrillite REE at 14–414 ppm range above detection" ;
    ada:errorCorrelationBetweenReportedQuantities -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:radiogenicFractionOfMeasuredSignal "missing" ;
    ada:sampleName "Tissint Martian meteorite" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: LA-Q-ICP-MS U-Pb Analysis Detail
description: Dataset-level analysis-instance detail for LA-Q-ICP-MS U-Pb geochronology,
  reusing CDIF/schema.org slots on the schema:Dataset root.
type: object
properties:
  prov:wasGeneratedBy:
    type: array
    items:
      type: object
      properties:
        schema:location:
          type: object
          properties:
            schema:name:
              description: Name of the laboratory or institution hosting the instrument.
              type: string
            schema:identifier:
              description: Persistent identifier for the laboratory (e.g., ROR ID).
              type: string
        schema:identifier:
          description: "Identifier for the analytical session this record describes
            \u2014 the laboratory's own run, sequence or batch identifier as generated
            by the instrument or acquisition software. The analysis record corresponds
            to one session, which may cover several samples, and this is the link
            back to the raw instrument files. Distinct from any persistent identifier
            a repository mints on submission."
          type: string
        schema:startDate:
          description: 'Date on which the analytical session began. For sessions spanning
            multiple days, use the date of the first session. Format: YYYY-MM-DD.'
          type: string
        schema:endDate:
          description: 'Date on which the analytical session ended. May equal Analysis
            Start Date for single-day sessions. Format: YYYY-MM-DD.'
          type: string
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
                        description: Physical form of the material as it enters the
                          ablation cell. Editable to accommodate legitimate variations
                          (e.g., thin section vs. mount) that do not alter the analytical
                          procedure.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/laQicpmsUPbTAPP/sampleFormAnalyticalSubstrate
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/laQicpmsUPbTAPP/sampleFormAnalyticalSubstrate
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
                      - title: Analysis Location/Spot Coordinates
                        description: "Location of the analysis on the sample surface.
                          For spot and transect analysis: stage coordinates (X, Y
                          in \xB5m) or a description relative to a named reference
                          feature (e.g., mineral rim, inclusion boundary). For mapping:
                          coordinates of the map corner(s) or centre, plus map dimensions.
                          Enables spatial reconstruction and co-registration with
                          other analytical images."
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/laQicpmsUPbTAPP/analysisLocationSpotCoordinates
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/laQicpmsUPbTAPP/analysisLocationSpotCoordinates
                          schema:name:
                            const: Analysis Location/Spot Coordinates
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
                        title: Sample Form / Analytical Substrate
                        description: Physical form of the material as it enters the
                          ablation cell. Editable to accommodate legitimate variations
                          (e.g., thin section vs. mount) that do not alter the analytical
                          procedure.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/laQicpmsUPbTAPP/sampleFormAnalyticalSubstrate
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/laQicpmsUPbTAPP/sampleFormAnalyticalSubstrate
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
                        title: Analysis Location/Spot Coordinates
                        description: "Location of the analysis on the sample surface.
                          For spot and transect analysis: stage coordinates (X, Y
                          in \xB5m) or a description relative to a named reference
                          feature (e.g., mineral rim, inclusion boundary). For mapping:
                          coordinates of the map corner(s) or centre, plus map dimensions.
                          Enables spatial reconstruction and co-registration with
                          other analytical images."
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/laQicpmsUPbTAPP/analysisLocationSpotCoordinates
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/laQicpmsUPbTAPP/analysisLocationSpotCoordinates
                          schema:name:
                            const: Analysis Location/Spot Coordinates
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
                  schema:name:
                    description: "Name or identifier of each sample analysed in this
                      session, as used in the laboratory \u2014 a sample mount, section
                      or aliquot counts as one entry where that is what the laboratory
                      tracks. The analysis record corresponds to one session and may
                      cover several samples; fields whose Keyed By column declares
                      'sample' take one value per entry. Should match the identifier
                      used in associated publications or data tables."
                    anyOf:
                    - type: string
                    - type: array
                      items:
                        type: string
                  schema:identifier:
                    description: Globally unique, persistent identifier for each sample
                      listed in Sample Name. IGSN (International Geo Sample Number)
                      is the recommended standard for geological and cosmochemical
                      samples, as used by Astromat, EarthChem and SESAR. Where a sample
                      and its sub-samples are separately registered, record the identifier
                      at the level actually analysed.
                    anyOf:
                    - type: string
                    - type: array
                      items:
                        type: string
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
                                const: ada:parameter/laQicpmsUPbTAPP/fusionFluxAndDilutionRatio
                              '@type':
                                const:
                                - schema:PropertyValue
                              schema:propertyID:
                                const:
                                - '@id': ada:parameter/laQicpmsUPbTAPP/fusionFluxAndDilutionRatio
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
                          - title: Pre-Ablation Surface Treatment
                            description: Procedure applied immediately before each
                              analysis to remove surface contamination or condition
                              the sample surface. Distinct from general sample preparation.
                              For spot analysis, pre-ablation pulses are discarded
                              before signal acquisition begins. For mapping, this
                              step is typically omitted as the large area ablated
                              averages out surface effects.
                            type: object
                            properties:
                              '@id':
                                const: ada:parameter/laQicpmsUPbTAPP/preAblationSurfaceTreatment
                              '@type':
                                const:
                                - schema:PropertyValue
                              schema:propertyID:
                                const:
                                - '@id': ada:parameter/laQicpmsUPbTAPP/preAblationSurfaceTreatment
                              schema:name:
                                const: Pre-Ablation Surface Treatment
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
                            title: Fusion Flux and Dilution Ratio
                            description: For procedures using fused glass, the flux
                              type and sample:flux dilution ratio used to prepare
                              the analytical glass.
                            type: object
                            properties:
                              '@id':
                                const: ada:parameter/laQicpmsUPbTAPP/fusionFluxAndDilutionRatio
                              '@type':
                                const:
                                - schema:PropertyValue
                              schema:propertyID:
                                const:
                                - '@id': ada:parameter/laQicpmsUPbTAPP/fusionFluxAndDilutionRatio
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
                            title: Pre-Ablation Surface Treatment
                            description: Procedure applied immediately before each
                              analysis to remove surface contamination or condition
                              the sample surface. Distinct from general sample preparation.
                              For spot analysis, pre-ablation pulses are discarded
                              before signal acquisition begins. For mapping, this
                              step is typically omitted as the large area ablated
                              averages out surface effects.
                            type: object
                            properties:
                              '@id':
                                const: ada:parameter/laQicpmsUPbTAPP/preAblationSurfaceTreatment
                              '@type':
                                const:
                                - schema:PropertyValue
                              schema:propertyID:
                                const:
                                - '@id': ada:parameter/laQicpmsUPbTAPP/preAblationSurfaceTreatment
                              schema:name:
                                const: Pre-Ablation Surface Treatment
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
                              by mixing aerosol from successive laser shots. For mapping
                              analyses, report "None" explicitly.'
                            type: object
                            properties:
                              '@id':
                                const: ada:parameter/laQicpmsUPbTAPP/signalSmoothing
                              '@type':
                                const:
                                - schema:PropertyValue
                              schema:propertyID:
                                const:
                                - '@id': ada:parameter/laQicpmsUPbTAPP/signalSmoothing
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
                              Distinct from Uncertainty Level, which states the convention
                              at which the resulting uncertainty is quoted.'
                            type: object
                            properties:
                              '@id':
                                const: ada:parameter/laQicpmsUPbTAPP/uncertaintyPropagationMethod
                              '@type':
                                const:
                                - schema:PropertyValue
                              schema:propertyID:
                                const:
                                - '@id': ada:parameter/laQicpmsUPbTAPP/uncertaintyPropagationMethod
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
                                const: ada:parameter/laQicpmsUPbTAPP/spikeOutlierFilteringApproach
                              '@type':
                                const:
                                - schema:PropertyValue
                              schema:propertyID:
                                const:
                                - '@id': ada:parameter/laQicpmsUPbTAPP/spikeOutlierFilteringApproach
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
                              response at the transition between pulse-counting and
                              analog detector modes.
                            type: object
                            properties:
                              '@id':
                                const: ada:parameter/laQicpmsUPbTAPP/pulseAnalogDetectorNonlinearityCorrection
                              '@type':
                                const:
                                - schema:PropertyValue
                              schema:propertyID:
                                const:
                                - '@id': ada:parameter/laQicpmsUPbTAPP/pulseAnalogDetectorNonlinearityCorrection
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
                          - title: Calibration Factor and Determination Method
                            description: 'An externally-calibrated factor that converts
                              the measured quantity into the reported quantity, how
                              it was determined, and its uncertainty. Applies where
                              the conversion depends on a factor calibrated against
                              a reference of independently known value, rather than
                              on the instrument response alone. Distinct from the
                              fields that name the calibration material and that state
                              which approach applies to which analyte, where the technique
                              has them: this field records the resulting factor itself.'
                            type: object
                            properties:
                              '@id':
                                const: ada:parameter/laQicpmsUPbTAPP/calibrationFactorAndDeterminationMethod
                              '@type':
                                const:
                                - schema:PropertyValue
                              schema:propertyID:
                                const:
                                - '@id': ada:parameter/laQicpmsUPbTAPP/calibrationFactorAndDeterminationMethod
                              schema:name:
                                const: Calibration Factor and Determination Method
                              schema:value:
                                type: string
                            required:
                            - '@id'
                            - '@type'
                            - schema:propertyID
                            - schema:name
                            - schema:value
                          - title: Constants and Reference Values Used
                            description: Physical constants and reference values used
                              in data reduction to calculate the final reported quantity
                              (e.g., decay constants for age calculation, standard
                              isotope ratios, or other citable reference values used
                              in a correction or calculation), together with their
                              source. Distinct from the Group 6 reference-material
                              fields, which document accepted values for specific
                              calibration/validation materials rather than universal
                              physical constants. Record "None" if no citable, revisable
                              physical constants feed into this procedure's data reduction.
                            type: object
                            properties:
                              '@id':
                                const: ada:parameter/laQicpmsUPbTAPP/constantsAndReferenceValuesUsed
                              '@type':
                                const:
                                - schema:PropertyValue
                              schema:propertyID:
                                const:
                                - '@id': ada:parameter/laQicpmsUPbTAPP/constantsAndReferenceValuesUsed
                              schema:name:
                                const: Constants and Reference Values Used
                              schema:value:
                                type: string
                            required:
                            - '@id'
                            - '@type'
                            - schema:propertyID
                            - schema:name
                            - schema:value
                          - title: Normalization/Standards-Based Correction
                            description: ''
                            type: object
                            properties:
                              '@id':
                                const: ada:parameter/laQicpmsUPbTAPP/normalizationStandardsBasedCorrection
                              '@type':
                                const:
                                - schema:PropertyValue
                              schema:propertyID:
                                const:
                                - '@id': ada:parameter/laQicpmsUPbTAPP/normalizationStandardsBasedCorrection
                              schema:name:
                                const: Normalization/Standards-Based Correction
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
                            title: Signal Smoothing
                            description: 'Description of any signal smoothing device
                              or approach installed between the ablation cell and
                              the ICP-MS to reduce pulse-to-pulse signal variability.
                              Note: active signal smoothing devices (e.g., squid,
                              SCFAST) are generally incompatible with high-resolution
                              raster mapping because they degrade spatial resolution
                              by mixing aerosol from successive laser shots. For mapping
                              analyses, report "None" explicitly.'
                            type: object
                            properties:
                              '@id':
                                const: ada:parameter/laQicpmsUPbTAPP/signalSmoothing
                              '@type':
                                const:
                                - schema:PropertyValue
                              schema:propertyID:
                                const:
                                - '@id': ada:parameter/laQicpmsUPbTAPP/signalSmoothing
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
                              Distinct from Uncertainty Level, which states the convention
                              at which the resulting uncertainty is quoted.'
                            type: object
                            properties:
                              '@id':
                                const: ada:parameter/laQicpmsUPbTAPP/uncertaintyPropagationMethod
                              '@type':
                                const:
                                - schema:PropertyValue
                              schema:propertyID:
                                const:
                                - '@id': ada:parameter/laQicpmsUPbTAPP/uncertaintyPropagationMethod
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
                                const: ada:parameter/laQicpmsUPbTAPP/spikeOutlierFilteringApproach
                              '@type':
                                const:
                                - schema:PropertyValue
                              schema:propertyID:
                                const:
                                - '@id': ada:parameter/laQicpmsUPbTAPP/spikeOutlierFilteringApproach
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
                              response at the transition between pulse-counting and
                              analog detector modes.
                            type: object
                            properties:
                              '@id':
                                const: ada:parameter/laQicpmsUPbTAPP/pulseAnalogDetectorNonlinearityCorrection
                              '@type':
                                const:
                                - schema:PropertyValue
                              schema:propertyID:
                                const:
                                - '@id': ada:parameter/laQicpmsUPbTAPP/pulseAnalogDetectorNonlinearityCorrection
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
                            title: Calibration Factor and Determination Method
                            description: 'An externally-calibrated factor that converts
                              the measured quantity into the reported quantity, how
                              it was determined, and its uncertainty. Applies where
                              the conversion depends on a factor calibrated against
                              a reference of independently known value, rather than
                              on the instrument response alone. Distinct from the
                              fields that name the calibration material and that state
                              which approach applies to which analyte, where the technique
                              has them: this field records the resulting factor itself.'
                            type: object
                            properties:
                              '@id':
                                const: ada:parameter/laQicpmsUPbTAPP/calibrationFactorAndDeterminationMethod
                              '@type':
                                const:
                                - schema:PropertyValue
                              schema:propertyID:
                                const:
                                - '@id': ada:parameter/laQicpmsUPbTAPP/calibrationFactorAndDeterminationMethod
                              schema:name:
                                const: Calibration Factor and Determination Method
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
                            title: Constants and Reference Values Used
                            description: Physical constants and reference values used
                              in data reduction to calculate the final reported quantity
                              (e.g., decay constants for age calculation, standard
                              isotope ratios, or other citable reference values used
                              in a correction or calculation), together with their
                              source. Distinct from the Group 6 reference-material
                              fields, which document accepted values for specific
                              calibration/validation materials rather than universal
                              physical constants. Record "None" if no citable, revisable
                              physical constants feed into this procedure's data reduction.
                            type: object
                            properties:
                              '@id':
                                const: ada:parameter/laQicpmsUPbTAPP/constantsAndReferenceValuesUsed
                              '@type':
                                const:
                                - schema:PropertyValue
                              schema:propertyID:
                                const:
                                - '@id': ada:parameter/laQicpmsUPbTAPP/constantsAndReferenceValuesUsed
                              schema:name:
                                const: Constants and Reference Values Used
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
                            title: Normalization/Standards-Based Correction
                            description: ''
                            type: object
                            properties:
                              '@id':
                                const: ada:parameter/laQicpmsUPbTAPP/normalizationStandardsBasedCorrection
                              '@type':
                                const:
                                - schema:PropertyValue
                              schema:propertyID:
                                const:
                                - '@id': ada:parameter/laQicpmsUPbTAPP/normalizationStandardsBasedCorrection
                              schema:name:
                                const: Normalization/Standards-Based Correction
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
            - title: Target Selection Criteria
              description: "The rules governing which part of the sample is analysed,
                and why. Covers the criteria applied when choosing grains, aliquots,
                spots, or a region of interest \u2014 size, morphology, clarity, freedom
                from inclusions or alteration, phase identity, or spatial position.
                Distinct from Target Material, which states the material type the
                procedure is designed for: this field states how, within such a sample,
                the analysed portion is picked out."
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/targetSelectionCriteria
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/targetSelectionCriteria
                schema:name:
                  const: Target Selection Criteria
                schema:value:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:propertyID
              - schema:name
              - schema:value
            - title: Pre-Analysis Imaging and Screening
              description: Imaging or other characterisation performed before the
                measurement in order to select or locate the analysed target, including
                the technique, instrument and settings used, and how individual analyses
                are linked back to the images. Distinct from any imaging the procedure
                performs as its own measurement. Where the imaging is performed on
                a separate instrument, it should also be recorded in the Group 1 coupling
                fields.
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening
                schema:name:
                  const: Pre-Analysis Imaging and Screening
                schema:value:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:propertyID
              - schema:name
              - schema:value
            - title: Ablation Duration per Spot
              description: 'Total on-sample ablation (signal acquisition) time per
                individual spot in seconds, as set in the acquisition method. This
                is a procedure-level parameter for spot analysis: it reflects the
                deliberate trade-off between signal accumulation (longer = lower LOD),
                sample consumption, and session throughput. For transect analysis,
                the equivalent procedure-level parameter is scan speed (captured in
                Transect Rate, Mapping Rate or Step Size). For mapping analysis, total
                acquisition time is sample-area-dependent and therefore analysis-level,
                not captured here.'
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/ablationDurationPerSpot
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/ablationDurationPerSpot
                schema:name:
                  const: Ablation Duration per Spot
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
            - title: Ablation Pit Depth and Ablation Rate
              description: Depth of the ablation pit produced under the registered
                laser conditions, the method used to measure it, and the resulting
                per-pulse ablation rate. Sets the achievable depth resolution and
                governs downhole elemental fractionation. For transect and mapping
                the equivalent quantity is trench depth under the same conditions.
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/ablationPitDepthAndAblationRate
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/ablationPitDepthAndAblationRate
                schema:name:
                  const: Ablation Pit Depth and Ablation Rate
                schema:value:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:propertyID
              - schema:name
              - schema:value
            - title: Transect Rate, Mapping Rate or Step Size
              description: "For continuous line scan (transect) and raster mapping:
                the stage translation speed in \xB5m s\u207B\xB9. This is the procedure-level
                parameter that, together with spot size and repetition rate, determines
                spatial resolution along the scan direction. For mapping, the mapping
                rate (mm\xB2 h\u207B\xB9) may be reported as an alternative when scan
                speed is session-variable. For stepped line profiles: the distance
                between successive spot positions in \xB5m."
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/transectRateMappingRateOrStepSize
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/transectRateMappingRateOrStepSize
                schema:name:
                  const: Transect Rate, Mapping Rate or Step Size
                schema:value:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:propertyID
              - schema:name
              - schema:value
            - title: Raster Line Spacing (Mapping Only)
              description: Distance between adjacent raster lines in a 2D elemental
                map, measured perpendicular to the scan direction, in micrometres.
                Together with spot size, this determines whether adjacent lines are
                contiguous (line spacing = spot size), overlapping (line spacing <
                spot size), or have gaps (line spacing > spot size). Applies to raster
                mapping only.
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/rasterLineSpacing
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/rasterLineSpacing
                schema:name:
                  const: Raster Line Spacing (Mapping Only)
                schema:value:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:propertyID
              - schema:name
              - schema:value
            - title: Carrier Gas and Flow Rate
              description: "Gas used to transport ablated aerosol from the ablation
                cell to the ICP-MS torch, with the procedure-registered target flow
                rate(s). Helium is standard for most UV laser systems due to superior
                aerosol transport. Flow rates are procedure targets; actual session
                values may be adjusted within \xB110% during tuning."
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/carrierGasAndFlowRate
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/carrierGasAndFlowRate
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
            - title: Plasma / Make-up Gas Addition
              description: "Additional gas(es) mixed into the carrier stream downstream
                of the ablation cell, with the procedure-registered target flow rate.
                Ar make-up gas is standard. Small N\u2082 additions can enhance sensitivity
                for some elements. If N\u2082 is not added, state \"None\" explicitly
                to distinguish from not reported."
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/plasmaMakeUpGasAddition
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/plasmaMakeUpGasAddition
                schema:name:
                  const: Plasma / Make-up Gas Addition
                schema:value:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:propertyID
              - schema:name
              - schema:value
            - title: Analysis Sequence
              description: Repeating order of primary calibration standard(s), quality
                control standard(s), and unknown analyses within a measurement session.
                Editable to allow minor adjustments while maintaining the bracketing
                strategy defined in the procedure.
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/analysisSequence
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/analysisSequence
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
              description: Dead time of each ion-counting detector channel, used in
                the dead-time correction applied to high count rates. Distinct from
                pulse/analog cross-calibration, which relates the two detector modes
                rather than correcting counting losses within the pulse-counting mode.
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
            - title: Background Count Time
              description: Total time spent measuring gas blank (background signal
                with laser off or shutter closed) before each ablation event, in seconds.
                For spot and transect analysis, a discrete background interval is
                measured before each ablation. For mapping, background is typically
                measured once per raster line or at the start of a map session rather
                than before each individual pixel. Editable to allow session-specific
                adjustment.
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/backgroundCountTime
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/backgroundCountTime
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
              description: 'Number of replicate analyses performed on the same sample
                (or same nominal location for spot analysis) in this session. For
                spot analysis: number of individual spot analyses per grain or location.
                For transect: number of replicate transect lines. For mapping: number
                of map acquisitions of the same area (usually 1).'
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
            - title: Transect Length
              description: Total length of the transect line analysed in micrometres.
                This is an analysis-level parameter because it depends on the size
                of the feature of interest rather than being fixed in the procedure.
                The procedure fixes scan speed (captured in Transect Rate, Mapping
                Rate or Step Size); transect length is determined at analysis time
                based on grain or feature size.
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/transectLength
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/transectLength
                schema:name:
                  const: Transect Length
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
            - title: Mapping Area
              description: "Total area covered by the 2D raster map, expressed as
                width \xD7 height in \xB5m or as total area in \xB5m\xB2 or mm\xB2.
                This is an analysis-level parameter because it depends on the size
                of the grain or phase to be mapped. The procedure fixes scan speed,
                line spacing, and spot size; the map area is chosen at analysis time
                to cover the target feature."
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/mappingArea
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/mappingArea
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
              description: 'Actual integration time used for the ablation signal in
                this analysis, in seconds. This is an analysis-level outcome determined
                during data reduction by applying the Signal Integration Interval
                Method to the time-resolved signal. It is equal to or shorter than
                the Ablation Duration per Spot because the signal start and end transients
                are typically discarded. Not applicable to mapping analysis: for mapping,
                the equivalent concept is the per-pixel cycle time, which is determined
                by the spectrometer dwell time settings (a procedure-level field)
                rather than being an analysis-level outcome.'
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/signalIntegrationTime
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/signalIntegrationTime
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
            - title: Procedural Blank Level
              description: "The measured level of the analytical blank in the session,
                and \u2014 where the reported quantity is a ratio \u2014 its composition,
                since a blank subtracted from a ratio biases the result unless its
                own composition is known. Companion to the blank correction method,
                which is procedure-level: this field records what was actually measured.
                Follows the criterion-versus-measurement split the library applies
                wherever a procedure sets a threshold and an analysis reports a value
                against it."
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/proceduralBlankLevel
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/proceduralBlankLevel
                schema:name:
                  const: Procedural Blank Level
                schema:value:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:propertyID
              - schema:name
              - schema:value
            - title: Reported Date Type
              description: The kind of date or age the procedure reports. Most dating
                systems derive several different date types from the same measurements,
                so a reported age is ambiguous without this. Where more than one type
                is reported, list all, separated by semicolons. Kohn et al. (2024)
                carry this as a named required item ("fission-track age type"); the
                equivalent distinction is required by all five other standards surveyed.
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/reportedDateType
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/reportedDateType
                schema:name:
                  const: Reported Date Type
                schema:value:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:propertyID
              - schema:name
              - schema:value
            - title: Inherited or Initial Signal Correction
              description: 'How any non-radiogenic, inherited or pre-existing component
                of the measured signal was accounted for, including the composition
                assumed, its source, and its uncertainty. Record ''None'' where the
                measured quantity accumulates from zero and no such component exists.
                Applies to five of the six dating systems surveyed; fission track
                is the sole genuine exception, as tracks accumulate from zero. D=Editable
                rather than Read-Only: the procedure registers the correction method
                and any default composition, but the value actually applied is frequently
                sample-specific (a two-stage model composition is evaluated at the
                interpreted age) or session-derived (a trapped composition solved
                from an isochron intercept), and a revision to the assumed composition
                should not require registering a new procedure. Same reasoning as
                Rule 5''s Constants and Reference Values Used.'
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/inheritedOrInitialSignalCorrection
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/inheritedOrInitialSignalCorrection
                schema:name:
                  const: Inherited or Initial Signal Correction
                schema:value:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:propertyID
              - schema:name
              - schema:value
            - title: Age Model
              description: "The statistical model used to combine individual analyses
                into a single reported age, including any criteria governing which
                model is applied. This is a methodological choice that changes the
                result: a Model-1 and a Model-3 regression of the same data yield
                different ages and different uncertainties. Record the model only
                \u2014 the software implementing it belongs in Data Reduction Software
                (Group 3), whose scope already extends to age calculation; where reduction
                and age regression use different packages, list both there. Required
                in some form by all six geochronology reporting standards surveyed."
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/ageModel
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/ageModel
                schema:name:
                  const: Age Model
                schema:value:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:propertyID
              - schema:name
              - schema:value
            - title: Age Datum / Reference Epoch
              description: 'The zero point from which the reported age is measured,
                where this is not the present day, and the date it corresponds to.
                Record ''Present day'' where the conventional datum applies. Explicitly
                required wherever the datum is not the present: year of sample collection
                for luminescence (Mahan et al. 2023), end of irradiation for 40Ar/39Ar
                decay corrections (Schaen et al. 2021).'
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/ageDatumReferenceEpoch
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/ageDatumReferenceEpoch
                schema:name:
                  const: Age Datum / Reference Epoch
                schema:value:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:propertyID
              - schema:name
              - schema:value
            - title: Error Correlation Between Reported Quantities
              description: The correlation coefficient between pairs of reported quantities
                whose uncertainties are not independent, together with the pair it
                applies to and how it was obtained. Concordia and isochron regressions
                cannot be reconstructed without it.
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
            - title: Imaging
              description: ''
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/imaging
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/imaging
                schema:name:
                  const: Imaging
                schema:value:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:propertyID
              - schema:name
              - schema:value
            - title: Spot Diameter
              description: ''
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/spotDiameter
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/spotDiameter
                schema:name:
                  const: Spot Diameter
                schema:value:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:propertyID
              - schema:name
              - schema:value
            - title: Ablation Pit Depth/Ablation Rate
              description: ''
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/ablationPitDepthAblationRate
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/ablationPitDepthAblationRate
                schema:name:
                  const: Ablation Pit Depth/Ablation Rate
                schema:value:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:propertyID
              - schema:name
              - schema:value
            - title: "Make-up Gas Flow (L min\u207B\xB9)"
              description: ''
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/makeUpGasFlow
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/makeUpGasFlow
                schema:name:
                  const: "Make-up Gas Flow (L min\u207B\xB9)"
                schema:value:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:propertyID
              - schema:name
              - schema:value
            - title: Masses Measured
              description: ''
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/massesMeasured
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/massesMeasured
                schema:name:
                  const: Masses Measured
                schema:value:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:propertyID
              - schema:name
              - schema:value
            - title: Integration Time per Peak/Dwell Times; Quadrupole Settling Time
                Between Mass Jumps
              description: ''
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/integrationTimePerPeakDwellTimesQuadrupoleSettlingTimeBetweenMassJumps
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/integrationTimePerPeakDwellTimesQuadrupoleSettlingTimeBetweenMassJumps
                schema:name:
                  const: Integration Time per Peak/Dwell Times; Quadrupole Settling
                    Time Between Mass Jumps
                schema:value:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:propertyID
              - schema:name
              - schema:value
            - title: Total Integration Time per Output Data Point
              description: "Total duty-cycle time for one complete mass-scan sweep
                \u2014 the sum of all per-isotope dwell times plus inter-mass settling
                times. Sets the time resolution of the downhole signal, and is not
                recoverable from Dwell Time per Mass alone because settling time is
                not captured there. Applies to sequential (quadrupole and single-collector
                sector-field) acquisition."
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
            - title: Number of Blocks per Measurement
              description: ''
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/numberOfBlocksPerMeasurement
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/numberOfBlocksPerMeasurement
                schema:name:
                  const: Number of Blocks per Measurement
                schema:value:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:propertyID
              - schema:name
              - schema:value
            - title: Number of Cycles per Block
              description: ''
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/numberOfCyclesPerBlock
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/numberOfCyclesPerBlock
                schema:name:
                  const: Number of Cycles per Block
                schema:value:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:propertyID
              - schema:name
              - schema:value
            - title: Integration Time per Cycle
              description: ''
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/integrationTimePerCycle
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/integrationTimePerCycle
                schema:name:
                  const: Integration Time per Cycle
                schema:value:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:propertyID
              - schema:name
              - schema:value
            - title: IC Dead Time (ns)
              description: ''
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/icDeadTime
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/icDeadTime
                schema:name:
                  const: IC Dead Time (ns)
                schema:value:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:propertyID
              - schema:name
              - schema:value
            - title: Other Information
              description: ''
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/otherInformation
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/otherInformation
                schema:name:
                  const: Other Information
                schema:value:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:propertyID
              - schema:name
              - schema:value
            - title: Uncertainty Level and Propagation
              description: ''
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/uncertaintyLevelAndPropagation
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/uncertaintyLevelAndPropagation
                schema:name:
                  const: Uncertainty Level and Propagation
                schema:value:
                  type: string
              required:
              - '@id'
              - '@type'
              - schema:propertyID
              - schema:name
              - schema:value
            - title: Double-Spike Mixing Ratio
              description: ''
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/doubleSpikeMixingRatio
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/doubleSpikeMixingRatio
                schema:name:
                  const: Double-Spike Mixing Ratio
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
              title: Target Selection Criteria
              description: "The rules governing which part of the sample is analysed,
                and why. Covers the criteria applied when choosing grains, aliquots,
                spots, or a region of interest \u2014 size, morphology, clarity, freedom
                from inclusions or alteration, phase identity, or spatial position.
                Distinct from Target Material, which states the material type the
                procedure is designed for: this field states how, within such a sample,
                the analysed portion is picked out."
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/targetSelectionCriteria
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/targetSelectionCriteria
                schema:name:
                  const: Target Selection Criteria
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
              title: Pre-Analysis Imaging and Screening
              description: Imaging or other characterisation performed before the
                measurement in order to select or locate the analysed target, including
                the technique, instrument and settings used, and how individual analyses
                are linked back to the images. Distinct from any imaging the procedure
                performs as its own measurement. Where the imaging is performed on
                a separate instrument, it should also be recorded in the Group 1 coupling
                fields.
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreening
                schema:name:
                  const: Pre-Analysis Imaging and Screening
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
              title: Ablation Duration per Spot
              description: 'Total on-sample ablation (signal acquisition) time per
                individual spot in seconds, as set in the acquisition method. This
                is a procedure-level parameter for spot analysis: it reflects the
                deliberate trade-off between signal accumulation (longer = lower LOD),
                sample consumption, and session throughput. For transect analysis,
                the equivalent procedure-level parameter is scan speed (captured in
                Transect Rate, Mapping Rate or Step Size). For mapping analysis, total
                acquisition time is sample-area-dependent and therefore analysis-level,
                not captured here.'
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/ablationDurationPerSpot
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/ablationDurationPerSpot
                schema:name:
                  const: Ablation Duration per Spot
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
              title: Ablation Pit Depth and Ablation Rate
              description: Depth of the ablation pit produced under the registered
                laser conditions, the method used to measure it, and the resulting
                per-pulse ablation rate. Sets the achievable depth resolution and
                governs downhole elemental fractionation. For transect and mapping
                the equivalent quantity is trench depth under the same conditions.
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/ablationPitDepthAndAblationRate
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/ablationPitDepthAndAblationRate
                schema:name:
                  const: Ablation Pit Depth and Ablation Rate
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
              title: Transect Rate, Mapping Rate or Step Size
              description: "For continuous line scan (transect) and raster mapping:
                the stage translation speed in \xB5m s\u207B\xB9. This is the procedure-level
                parameter that, together with spot size and repetition rate, determines
                spatial resolution along the scan direction. For mapping, the mapping
                rate (mm\xB2 h\u207B\xB9) may be reported as an alternative when scan
                speed is session-variable. For stepped line profiles: the distance
                between successive spot positions in \xB5m."
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/transectRateMappingRateOrStepSize
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/transectRateMappingRateOrStepSize
                schema:name:
                  const: Transect Rate, Mapping Rate or Step Size
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
              title: Raster Line Spacing (Mapping Only)
              description: Distance between adjacent raster lines in a 2D elemental
                map, measured perpendicular to the scan direction, in micrometres.
                Together with spot size, this determines whether adjacent lines are
                contiguous (line spacing = spot size), overlapping (line spacing <
                spot size), or have gaps (line spacing > spot size). Applies to raster
                mapping only.
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/rasterLineSpacing
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/rasterLineSpacing
                schema:name:
                  const: Raster Line Spacing (Mapping Only)
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
              title: Carrier Gas and Flow Rate
              description: "Gas used to transport ablated aerosol from the ablation
                cell to the ICP-MS torch, with the procedure-registered target flow
                rate(s). Helium is standard for most UV laser systems due to superior
                aerosol transport. Flow rates are procedure targets; actual session
                values may be adjusted within \xB110% during tuning."
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/carrierGasAndFlowRate
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/carrierGasAndFlowRate
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
              title: Plasma / Make-up Gas Addition
              description: "Additional gas(es) mixed into the carrier stream downstream
                of the ablation cell, with the procedure-registered target flow rate.
                Ar make-up gas is standard. Small N\u2082 additions can enhance sensitivity
                for some elements. If N\u2082 is not added, state \"None\" explicitly
                to distinguish from not reported."
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/plasmaMakeUpGasAddition
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/plasmaMakeUpGasAddition
                schema:name:
                  const: Plasma / Make-up Gas Addition
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
              title: Analysis Sequence
              description: Repeating order of primary calibration standard(s), quality
                control standard(s), and unknown analyses within a measurement session.
                Editable to allow minor adjustments while maintaining the bracketing
                strategy defined in the procedure.
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/analysisSequence
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/analysisSequence
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
              description: Dead time of each ion-counting detector channel, used in
                the dead-time correction applied to high count rates. Distinct from
                pulse/analog cross-calibration, which relates the two detector modes
                rather than correcting counting losses within the pulse-counting mode.
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
              title: Background Count Time
              description: Total time spent measuring gas blank (background signal
                with laser off or shutter closed) before each ablation event, in seconds.
                For spot and transect analysis, a discrete background interval is
                measured before each ablation. For mapping, background is typically
                measured once per raster line or at the start of a map session rather
                than before each individual pixel. Editable to allow session-specific
                adjustment.
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/backgroundCountTime
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/backgroundCountTime
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
              description: 'Number of replicate analyses performed on the same sample
                (or same nominal location for spot analysis) in this session. For
                spot analysis: number of individual spot analyses per grain or location.
                For transect: number of replicate transect lines. For mapping: number
                of map acquisitions of the same area (usually 1).'
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
              title: Transect Length
              description: Total length of the transect line analysed in micrometres.
                This is an analysis-level parameter because it depends on the size
                of the feature of interest rather than being fixed in the procedure.
                The procedure fixes scan speed (captured in Transect Rate, Mapping
                Rate or Step Size); transect length is determined at analysis time
                based on grain or feature size.
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/transectLength
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/transectLength
                schema:name:
                  const: Transect Length
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
              title: Mapping Area
              description: "Total area covered by the 2D raster map, expressed as
                width \xD7 height in \xB5m or as total area in \xB5m\xB2 or mm\xB2.
                This is an analysis-level parameter because it depends on the size
                of the grain or phase to be mapped. The procedure fixes scan speed,
                line spacing, and spot size; the map area is chosen at analysis time
                to cover the target feature."
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/mappingArea
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/mappingArea
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
              description: 'Actual integration time used for the ablation signal in
                this analysis, in seconds. This is an analysis-level outcome determined
                during data reduction by applying the Signal Integration Interval
                Method to the time-resolved signal. It is equal to or shorter than
                the Ablation Duration per Spot because the signal start and end transients
                are typically discarded. Not applicable to mapping analysis: for mapping,
                the equivalent concept is the per-pixel cycle time, which is determined
                by the spectrometer dwell time settings (a procedure-level field)
                rather than being an analysis-level outcome.'
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/signalIntegrationTime
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/signalIntegrationTime
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
              title: Procedural Blank Level
              description: "The measured level of the analytical blank in the session,
                and \u2014 where the reported quantity is a ratio \u2014 its composition,
                since a blank subtracted from a ratio biases the result unless its
                own composition is known. Companion to the blank correction method,
                which is procedure-level: this field records what was actually measured.
                Follows the criterion-versus-measurement split the library applies
                wherever a procedure sets a threshold and an analysis reports a value
                against it."
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/proceduralBlankLevel
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/proceduralBlankLevel
                schema:name:
                  const: Procedural Blank Level
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
              title: Reported Date Type
              description: The kind of date or age the procedure reports. Most dating
                systems derive several different date types from the same measurements,
                so a reported age is ambiguous without this. Where more than one type
                is reported, list all, separated by semicolons. Kohn et al. (2024)
                carry this as a named required item ("fission-track age type"); the
                equivalent distinction is required by all five other standards surveyed.
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/reportedDateType
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/reportedDateType
                schema:name:
                  const: Reported Date Type
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
              title: Inherited or Initial Signal Correction
              description: 'How any non-radiogenic, inherited or pre-existing component
                of the measured signal was accounted for, including the composition
                assumed, its source, and its uncertainty. Record ''None'' where the
                measured quantity accumulates from zero and no such component exists.
                Applies to five of the six dating systems surveyed; fission track
                is the sole genuine exception, as tracks accumulate from zero. D=Editable
                rather than Read-Only: the procedure registers the correction method
                and any default composition, but the value actually applied is frequently
                sample-specific (a two-stage model composition is evaluated at the
                interpreted age) or session-derived (a trapped composition solved
                from an isochron intercept), and a revision to the assumed composition
                should not require registering a new procedure. Same reasoning as
                Rule 5''s Constants and Reference Values Used.'
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/inheritedOrInitialSignalCorrection
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/inheritedOrInitialSignalCorrection
                schema:name:
                  const: Inherited or Initial Signal Correction
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
              title: Age Model
              description: "The statistical model used to combine individual analyses
                into a single reported age, including any criteria governing which
                model is applied. This is a methodological choice that changes the
                result: a Model-1 and a Model-3 regression of the same data yield
                different ages and different uncertainties. Record the model only
                \u2014 the software implementing it belongs in Data Reduction Software
                (Group 3), whose scope already extends to age calculation; where reduction
                and age regression use different packages, list both there. Required
                in some form by all six geochronology reporting standards surveyed."
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/ageModel
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/ageModel
                schema:name:
                  const: Age Model
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
              title: Age Datum / Reference Epoch
              description: 'The zero point from which the reported age is measured,
                where this is not the present day, and the date it corresponds to.
                Record ''Present day'' where the conventional datum applies. Explicitly
                required wherever the datum is not the present: year of sample collection
                for luminescence (Mahan et al. 2023), end of irradiation for 40Ar/39Ar
                decay corrections (Schaen et al. 2021).'
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/ageDatumReferenceEpoch
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/ageDatumReferenceEpoch
                schema:name:
                  const: Age Datum / Reference Epoch
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
              title: Error Correlation Between Reported Quantities
              description: The correlation coefficient between pairs of reported quantities
                whose uncertainties are not independent, together with the pair it
                applies to and how it was obtained. Concordia and isochron regressions
                cannot be reconstructed without it.
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
              title: Imaging
              description: ''
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/imaging
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/imaging
                schema:name:
                  const: Imaging
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
              title: Spot Diameter
              description: ''
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/spotDiameter
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/spotDiameter
                schema:name:
                  const: Spot Diameter
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
              title: Ablation Pit Depth/Ablation Rate
              description: ''
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/ablationPitDepthAblationRate
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/ablationPitDepthAblationRate
                schema:name:
                  const: Ablation Pit Depth/Ablation Rate
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
              title: "Make-up Gas Flow (L min\u207B\xB9)"
              description: ''
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/makeUpGasFlow
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/makeUpGasFlow
                schema:name:
                  const: "Make-up Gas Flow (L min\u207B\xB9)"
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
              title: Masses Measured
              description: ''
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/massesMeasured
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/massesMeasured
                schema:name:
                  const: Masses Measured
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
              title: Integration Time per Peak/Dwell Times; Quadrupole Settling Time
                Between Mass Jumps
              description: ''
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/integrationTimePerPeakDwellTimesQuadrupoleSettlingTimeBetweenMassJumps
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/integrationTimePerPeakDwellTimesQuadrupoleSettlingTimeBetweenMassJumps
                schema:name:
                  const: Integration Time per Peak/Dwell Times; Quadrupole Settling
                    Time Between Mass Jumps
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
              title: Total Integration Time per Output Data Point
              description: "Total duty-cycle time for one complete mass-scan sweep
                \u2014 the sum of all per-isotope dwell times plus inter-mass settling
                times. Sets the time resolution of the downhole signal, and is not
                recoverable from Dwell Time per Mass alone because settling time is
                not captured there. Applies to sequential (quadrupole and single-collector
                sector-field) acquisition."
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
              title: Number of Blocks per Measurement
              description: ''
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/numberOfBlocksPerMeasurement
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/numberOfBlocksPerMeasurement
                schema:name:
                  const: Number of Blocks per Measurement
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
              title: Number of Cycles per Block
              description: ''
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/numberOfCyclesPerBlock
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/numberOfCyclesPerBlock
                schema:name:
                  const: Number of Cycles per Block
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
              title: Integration Time per Cycle
              description: ''
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/integrationTimePerCycle
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/integrationTimePerCycle
                schema:name:
                  const: Integration Time per Cycle
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
              title: IC Dead Time (ns)
              description: ''
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/icDeadTime
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/icDeadTime
                schema:name:
                  const: IC Dead Time (ns)
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
              title: Other Information
              description: ''
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/otherInformation
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/otherInformation
                schema:name:
                  const: Other Information
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
              title: Uncertainty Level and Propagation
              description: ''
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/uncertaintyLevelAndPropagation
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/uncertaintyLevelAndPropagation
                schema:name:
                  const: Uncertainty Level and Propagation
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
              title: Double-Spike Mixing Ratio
              description: ''
              type: object
              properties:
                '@id':
                  const: ada:parameter/laQicpmsUPbTAPP/doubleSpikeMixingRatio
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laQicpmsUPbTAPP/doubleSpikeMixingRatio
                schema:name:
                  const: Double-Spike Mixing Ratio
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
                                              species production. The procedure specifies
                                              a target value optimised during initial
                                              setup; the analyst confirms or fine-adjusts
                                              during session tuning.
                                            type: object
                                            properties:
                                              '@id':
                                                const: ada:parameter/laQicpmsUPbTAPP/torchDepth
                                              '@type':
                                                const:
                                                - schema:PropertyValue
                                              schema:propertyID:
                                                const:
                                                - '@id': ada:parameter/laQicpmsUPbTAPP/torchDepth
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
                                                  const: ada:parameter/laQicpmsUPbTAPP/torchDepth
                                                '@type':
                                                  const:
                                                  - schema:PropertyValue
                                                schema:propertyID:
                                                  const:
                                                  - '@id': ada:parameter/laQicpmsUPbTAPP/torchDepth
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
                                                that sustains the ICP plasma, in L/min.
                                                Determines plasma volume and stability.
                                                Set during initial plasma optimisation
                                                and confirmed at each session start.
                                              type: object
                                              properties:
                                                '@id':
                                                  const: ada:parameter/laQicpmsUPbTAPP/coolantGasFlowRate
                                                '@type':
                                                  const:
                                                  - schema:PropertyValue
                                                schema:propertyID:
                                                  const:
                                                  - '@id': ada:parameter/laQicpmsUPbTAPP/coolantGasFlowRate
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
                                                positions the plasma relative to the
                                                load coil, in L/min. Affects ion extraction
                                                efficiency and oxide production rates.
                                                Distinct from the carrier gas (which
                                                transports ablation aerosol) and the
                                                coolant (plasma) gas.
                                              type: object
                                              properties:
                                                '@id':
                                                  const: ada:parameter/laQicpmsUPbTAPP/auxiliaryGasFlowRate
                                                '@type':
                                                  const:
                                                  - schema:PropertyValue
                                                schema:propertyID:
                                                  const:
                                                  - '@id': ada:parameter/laQicpmsUPbTAPP/auxiliaryGasFlowRate
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
                                                confirms or fine-adjusts during session
                                                tuning.
                                              type: object
                                              properties:
                                                '@id':
                                                  const: ada:parameter/laQicpmsUPbTAPP/rfPower
                                                '@type':
                                                  const:
                                                  - schema:PropertyValue
                                                schema:propertyID:
                                                  const:
                                                  - '@id': ada:parameter/laQicpmsUPbTAPP/rfPower
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
                                                that sustains the ICP plasma, in L/min.
                                                Determines plasma volume and stability.
                                                Set during initial plasma optimisation
                                                and confirmed at each session start.
                                              type: object
                                              properties:
                                                '@id':
                                                  const: ada:parameter/laQicpmsUPbTAPP/coolantGasFlowRate
                                                '@type':
                                                  const:
                                                  - schema:PropertyValue
                                                schema:propertyID:
                                                  const:
                                                  - '@id': ada:parameter/laQicpmsUPbTAPP/coolantGasFlowRate
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
                                                positions the plasma relative to the
                                                load coil, in L/min. Affects ion extraction
                                                efficiency and oxide production rates.
                                                Distinct from the carrier gas (which
                                                transports ablation aerosol) and the
                                                coolant (plasma) gas.
                                              type: object
                                              properties:
                                                '@id':
                                                  const: ada:parameter/laQicpmsUPbTAPP/auxiliaryGasFlowRate
                                                '@type':
                                                  const:
                                                  - schema:PropertyValue
                                                schema:propertyID:
                                                  const:
                                                  - '@id': ada:parameter/laQicpmsUPbTAPP/auxiliaryGasFlowRate
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
                                                confirms or fine-adjusts during session
                                                tuning.
                                              type: object
                                              properties:
                                                '@id':
                                                  const: ada:parameter/laQicpmsUPbTAPP/rfPower
                                                '@type':
                                                  const:
                                                  - schema:PropertyValue
                                                schema:propertyID:
                                                  const:
                                                  - '@id': ada:parameter/laQicpmsUPbTAPP/rfPower
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
                                                the collision/reaction cell, in mL/min.
                                                Controls the degree of ion thermalization
                                                and KED efficiency. Record 'None'
                                                if the CRC is in STD mode.
                                              type: object
                                              properties:
                                                '@id':
                                                  const: ada:parameter/laQicpmsUPbTAPP/collisionGasFlowRate
                                                '@type':
                                                  const:
                                                  - schema:PropertyValue
                                                schema:propertyID:
                                                  const:
                                                  - '@id': ada:parameter/laQicpmsUPbTAPP/collisionGasFlowRate
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
                                              description: Bias voltage applied at
                                                the collision/reaction cell exit to
                                                discriminate between analyte ions
                                                and low-energy polyatomic interferences
                                                in KED mode, in volts (V). A negative
                                                bias preferentially retards slow polyatomic
                                                ions while transmitting faster analyte
                                                ions. Record 'None' if the CRC is
                                                in STD mode.
                                              type: object
                                              properties:
                                                '@id':
                                                  const: ada:parameter/laQicpmsUPbTAPP/cellExitDiscriminationVoltage
                                                '@type':
                                                  const:
                                                  - schema:PropertyValue
                                                schema:propertyID:
                                                  const:
                                                  - '@id': ada:parameter/laQicpmsUPbTAPP/cellExitDiscriminationVoltage
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
                                                gas introduced into the dynamic reaction
                                                cell (DRC), in mL/min.
                                              type: object
                                              properties:
                                                '@id':
                                                  const: ada:parameter/laQicpmsUPbTAPP/reactionGasFlowRate
                                                '@type':
                                                  const:
                                                  - schema:PropertyValue
                                                schema:propertyID:
                                                  const:
                                                  - '@id': ada:parameter/laQicpmsUPbTAPP/reactionGasFlowRate
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
                                                the collision/reaction cell, in mL/min.
                                                Controls the degree of ion thermalization
                                                and KED efficiency. Record 'None'
                                                if the CRC is in STD mode.
                                              type: object
                                              properties:
                                                '@id':
                                                  const: ada:parameter/laQicpmsUPbTAPP/collisionGasFlowRate
                                                '@type':
                                                  const:
                                                  - schema:PropertyValue
                                                schema:propertyID:
                                                  const:
                                                  - '@id': ada:parameter/laQicpmsUPbTAPP/collisionGasFlowRate
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
                                              description: Bias voltage applied at
                                                the collision/reaction cell exit to
                                                discriminate between analyte ions
                                                and low-energy polyatomic interferences
                                                in KED mode, in volts (V). A negative
                                                bias preferentially retards slow polyatomic
                                                ions while transmitting faster analyte
                                                ions. Record 'None' if the CRC is
                                                in STD mode.
                                              type: object
                                              properties:
                                                '@id':
                                                  const: ada:parameter/laQicpmsUPbTAPP/cellExitDiscriminationVoltage
                                                '@type':
                                                  const:
                                                  - schema:PropertyValue
                                                schema:propertyID:
                                                  const:
                                                  - '@id': ada:parameter/laQicpmsUPbTAPP/cellExitDiscriminationVoltage
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
                                                gas introduced into the dynamic reaction
                                                cell (DRC), in mL/min.
                                              type: object
                                              properties:
                                                '@id':
                                                  const: ada:parameter/laQicpmsUPbTAPP/reactionGasFlowRate
                                                '@type':
                                                  const:
                                                  - schema:PropertyValue
                                                schema:propertyID:
                                                  const:
                                                  - '@id': ada:parameter/laQicpmsUPbTAPP/reactionGasFlowRate
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
                                      mass analyser. For quadrupole instruments this
                                      is fixed at unit resolution by instrument design.
                                    type: object
                                    properties:
                                      '@id':
                                        const: ada:parameter/laQicpmsUPbTAPP/massResolutionSetting
                                      '@type':
                                        const:
                                        - schema:PropertyValue
                                      schema:propertyID:
                                        const:
                                        - '@id': ada:parameter/laQicpmsUPbTAPP/massResolutionSetting
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
                                      to optimise ICP plasma conditions prior to analysis,
                                      including the reference material used for tuning
                                      and the acceptance criteria (e.g., oxide production
                                      threshold, sensitivity targets, mass calibration).
                                    type: object
                                    properties:
                                      '@id':
                                        const: ada:parameter/laQicpmsUPbTAPP/icpTuning
                                      '@type':
                                        const:
                                        - schema:PropertyValue
                                      schema:propertyID:
                                        const:
                                        - '@id': ada:parameter/laQicpmsUPbTAPP/icpTuning
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
                                      doubly-charged ion (M\xB2\u207A) formation during
                                      instrument tuning. Doubly-charged ions appear
                                      at half the mass of the parent ion and can cause
                                      isobaric interferences on analytes in that mass
                                      region. The monitor species and the mass positions
                                      monitored should be stated explicitly. Analogous
                                      to Oxide Production Method and Threshold for
                                      oxide monitoring."
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
                                      the time of instrument tuning. The procedure
                                      should specify the acceptable threshold (e.g.,
                                      <1%, <3%); the measured value for each session
                                      is recorded here. Report both the threshold
                                      and the measured value where possible.
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
                                  - title: Memory Effect Mitigation
                                    description: Procedure applied to identify and
                                      minimise memory effects from high-concentration
                                      elements in the previous sample or standard
                                      that may contaminate subsequent analyses, or
                                      from incomplete aerosol washout between adjacent
                                      pixels in raster mapping mode. For mapping,
                                      the mitigation strategy involves controlling
                                      scan speed relative to washout time to ensure
                                      each pixel signal is sufficiently free of the
                                      preceding pixel's contribution.
                                    type: object
                                    properties:
                                      '@id':
                                        const: ada:parameter/laQicpmsUPbTAPP/memoryEffectMitigation
                                      '@type':
                                        const:
                                        - schema:PropertyValue
                                      schema:propertyID:
                                        const:
                                        - '@id': ada:parameter/laQicpmsUPbTAPP/memoryEffectMitigation
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
                                      mass analyser. For quadrupole instruments this
                                      is fixed at unit resolution by instrument design.
                                    type: object
                                    properties:
                                      '@id':
                                        const: ada:parameter/laQicpmsUPbTAPP/massResolutionSetting
                                      '@type':
                                        const:
                                        - schema:PropertyValue
                                      schema:propertyID:
                                        const:
                                        - '@id': ada:parameter/laQicpmsUPbTAPP/massResolutionSetting
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
                                      to optimise ICP plasma conditions prior to analysis,
                                      including the reference material used for tuning
                                      and the acceptance criteria (e.g., oxide production
                                      threshold, sensitivity targets, mass calibration).
                                    type: object
                                    properties:
                                      '@id':
                                        const: ada:parameter/laQicpmsUPbTAPP/icpTuning
                                      '@type':
                                        const:
                                        - schema:PropertyValue
                                      schema:propertyID:
                                        const:
                                        - '@id': ada:parameter/laQicpmsUPbTAPP/icpTuning
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
                                      doubly-charged ion (M\xB2\u207A) formation during
                                      instrument tuning. Doubly-charged ions appear
                                      at half the mass of the parent ion and can cause
                                      isobaric interferences on analytes in that mass
                                      region. The monitor species and the mass positions
                                      monitored should be stated explicitly. Analogous
                                      to Oxide Production Method and Threshold for
                                      oxide monitoring."
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
                                      the time of instrument tuning. The procedure
                                      should specify the acceptable threshold (e.g.,
                                      <1%, <3%); the measured value for each session
                                      is recorded here. Report both the threshold
                                      and the measured value where possible.
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
                                    title: Memory Effect Mitigation
                                    description: Procedure applied to identify and
                                      minimise memory effects from high-concentration
                                      elements in the previous sample or standard
                                      that may contaminate subsequent analyses, or
                                      from incomplete aerosol washout between adjacent
                                      pixels in raster mapping mode. For mapping,
                                      the mitigation strategy involves controlling
                                      scan speed relative to washout time to ensure
                                      each pixel signal is sufficiently free of the
                                      preceding pixel's contribution.
                                    type: object
                                    properties:
                                      '@id':
                                        const: ada:parameter/laQicpmsUPbTAPP/memoryEffectMitigation
                                      '@type':
                                        const:
                                        - schema:PropertyValue
                                      schema:propertyID:
                                        const:
                                        - '@id': ada:parameter/laQicpmsUPbTAPP/memoryEffectMitigation
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
                              ada:laserSpotGeometry:
                                description: "Shape and dimensions of the laser ablation
                                  spot in micrometres registered by the procedure.
                                  For circular spots, report diameter; for square
                                  or rectangular spots, report width \xD7 length.
                                  The procedure registers the typical geometry; analysts
                                  may adjust within procedure-allowed range."
                                anyOf:
                                - type: string
                                - type: array
                                  items:
                                    type: string
                              schema:additionalProperty:
                                type: array
                                items:
                                  title: Laser Energy
                                  description: "Laser pulse energy in millijoules
                                    as set at the laser output or measured at the
                                    sample surface. Less commonly reported than fluence
                                    because it does not account for spot area. Report
                                    only when the system displays energy directly.
                                    Laser fluence (J cm\u207B\xB2) is the preferred
                                    quantity and is captured in Default Laser Fluence."
                                  type: object
                                  properties:
                                    '@id':
                                      const: ada:parameter/laQicpmsUPbTAPP/laserEnergy
                                    '@type':
                                      const:
                                      - schema:PropertyValue
                                    schema:propertyID:
                                      const:
                                      - '@id': ada:parameter/laQicpmsUPbTAPP/laserEnergy
                                    schema:name:
                                      const: Laser Energy
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
                                    title: Laser Energy
                                    description: "Laser pulse energy in millijoules
                                      as set at the laser output or measured at the
                                      sample surface. Less commonly reported than
                                      fluence because it does not account for spot
                                      area. Report only when the system displays energy
                                      directly. Laser fluence (J cm\u207B\xB2) is
                                      the preferred quantity and is captured in Default
                                      Laser Fluence."
                                    type: object
                                    properties:
                                      '@id':
                                        const: ada:parameter/laQicpmsUPbTAPP/laserEnergy
                                      '@type':
                                        const:
                                        - schema:PropertyValue
                                      schema:propertyID:
                                        const:
                                        - '@id': ada:parameter/laQicpmsUPbTAPP/laserEnergy
                                      schema:name:
                                        const: Laser Energy
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
                              ada:laserFluence:
                                description: "Laser pulse energy per unit area at
                                  the sample surface in J cm\u207B\xB2, as registered
                                  by the procedure. Fluence is the physically meaningful
                                  quantity controlling ablation rate, crater morphology,
                                  elemental fractionation, and particle size distribution.
                                  If the system reports only as % of maximum output,
                                  include that value and note the system maximum where
                                  known."
                                anyOf:
                                - type: number
                                - type: string
                              ada:laserRepetitionRate:
                                description: Laser pulse repetition rate in hertz
                                  registered by the procedure. For mapping methods,
                                  repetition rate together with scan speed and spot
                                  size determines pixel size and spatial resolution.
                                  Analysts may adjust within procedure-allowed bounds.
                                anyOf:
                                - type: number
                                - type: string
                    allOf:
                    - contains:
                        properties:
                          schema:additionalType:
                            contains:
                              const: ICPMS
                            schema:inDefinedTermSet: ada:vocab/instrumentType
                        required:
                        - schema:additionalType
                    - contains:
                        properties:
                          schema:additionalType:
                            contains:
                              const: Laser Ablation System
                            schema:inDefinedTermSet: ada:vocab/instrumentType
                        required:
                        - schema:additionalType
            - if:
                required:
                - bios:computationalTool
              then:
                properties:
                  bios:computationalTool:
                    type: array
                    items:
                      allOf:
                      - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/geochemProduct/schema.yaml#/$defs/UsedComputationalTool
                      - type: object
                        allOf:
                        - if:
                            properties:
                              ada:toolRole:
                                const: acquisition
                            required:
                            - ada:toolRole
                          then:
                            properties:
                              schema:name:
                                description: Instrument control and data acquisition
                                  software used to collect raw signal data, including
                                  version number. Separate from data reduction software.
                                anyOf:
                                - type: string
                                - type: array
                                  items:
                                    type: string
                        - if:
                            properties:
                              ada:toolRole:
                                const: dataReduction
                            required:
                            - ada:toolRole
                          then:
                            properties:
                              schema:name:
                                description: Software used for signal processing,
                                  background subtraction, and concentration calculation,
                                  including version number.
                                anyOf:
                                - type: string
                                - type: array
                                  items:
                                    type: string
                        required:
                        - ada:toolRole
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
                                description: Primary reference material(s) used to
                                  calibrate the instrument and convert raw signal
                                  intensities to concentrations or isotope ratios.
                                  Include material name, source institution, and citation
                                  for the accepted values used. Editable because the
                                  specific lot or certification vintage may differ
                                  between sessions while the material type remains
                                  the same.
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
                                description: Quality-control reference materials analysed
                                  as unknowns alongside samples in the same session
                                  to assess accuracy and monitor drift. Include material
                                  name, source, and citation for accepted values used
                                  for comparison. Editable because selection of secondary
                                  RMs may vary across sessions.
                                anyOf:
                                - type: string
                                - type: array
                                  items:
                                    type: string
                        required:
                        - ada:reagentRole
        schema:description:
          description: "Any procedure- or analysis-specific information not captured
            by a structured field anywhere in this TAPP \u2014 including anomalies,
            deviations from the registered procedure, instrument modifications, and
            supplementary context. Scope is the whole document, not Group 6: this
            is the last field of the TAPP and covers all six groups. Use sparingly;
            a structured field is preferred for anything that can be formally categorised."
          type: string
  schema:measurementTechnique:
    type: array
    items:
      type: object
      properties:
        schema:identifier:
          type: string
  schema:contributor:
    type: array
    items:
      type: object
      allOf:
      - if:
          properties:
            schema:roleName:
              const: analyst
          required:
          - schema:roleName
        then:
          properties:
            schema:name:
              description: Name(s) of the analyst(s) who performed the analysis session.
                ORCID is recommended for persistent identification.
              anyOf:
              - type: string
              - type: array
                items:
                  type: string
    allOf:
    - contains:
        properties:
          schema:roleName:
            const: analyst
        required:
        - schema:roleName
  schema:funding:
    type: array
  schema:relatedLink:
    type: array
    items:
      type: object
      allOf:
      - if:
          properties:
            schema:linkRelationship:
              const: coupledTechnique
          required:
          - schema:linkRelationship
        then:
          properties:
            schema:target:
              type: object
              properties:
                schema:name:
                  description: "Other analytical techniques applied to the same sample(s)
                    whose results are intended to be interpreted together with data
                    from this procedure. Document coupling with any technique whose
                    results are functionally linked to this dataset \u2014 providing
                    calibration inputs, complementary spatial context, or required
                    companion measurements. Use the same controlled vocabulary as
                    the Technique field. Enter \"None\" if no coupling is intended."
                  anyOf:
                  - type: string
                    enum:
                    - EPMA
                    - SIMS
                    - ICP-MS (solution)
                    - Noble Gas MS
                    - None
                    - N/A
                    - missing
                  - type: string
                schema:description:
                  description: "Description of how this procedure is coupled with
                    the technique(s) listed above. Include: (1) the functional relationship
                    \u2014 what data or context flows between techniques, or how results
                    are combined (e.g. which output from the coupled technique serves
                    as input to data reduction for this technique); and (2) the analytical
                    sequence \u2014 which technique is performed first and why (e.g.
                    non-destructive before destructive). Required when Coupled Technique(s)
                    is not \"None\"."
                  type: string
      - if:
          properties:
            schema:linkRelationship:
              const: coupledProcedure
          required:
          - schema:linkRelationship
        then:
          properties:
            schema:target:
              type: object
              properties:
                schema:url:
                  type: string
      - if:
          properties:
            schema:linkRelationship:
              const: coupledDataset
          required:
          - schema:linkRelationship
        then:
          properties:
            schema:target:
              description: 'DOI or other persistent identifier for the co-registered
                dataset or publication where both datasets are reported together.
                Accepts: a dedicated dataset DOI (if separately deposited), a shared
                dataset DOI (if co-submitted in the same package), or a publication
                DOI. Use "same submission" if the coupled dataset is included in this
                data package, or "pending" if not yet assigned. If coupling is documented
                through a shared sample identifier only, that information is already
                captured in Sample Persistent Identifier (Group 2).'
              anyOf:
              - type: string
              - type: array
                items:
                  type: string
  ada:spotDiameterMeasured:
    description: 'Diameter of the laser spot as independently measured on the sample
      or on a test material, distinct from the nominal value the procedure registers.
      Measured companion to Laser Spot Geometry: nominal and delivered spot size can
      differ appreciably with optics condition and focus.'
    anyOf:
    - type: number
    - type: string
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
      - if:
          properties:
            dqv:isMeasurementOf:
              const: Dispersion Statistic
          required:
          - dqv:isMeasurementOf
        then:
          properties:
            dqv:value:
              description: The statistic reported to show whether scatter among the
                contributing analyses exceeds what analytical uncertainty alone predicts,
                together with its value. Answers whether a reported aggregate is defensible
                as a single population. Procedure-level tier is N/A because the value
                cannot be known before the analysis; the procedure may still state
                an acceptance threshold, which belongs with the inclusion criteria.
              anyOf:
              - type: string
              - type: array
                items:
                  type: string
      - if:
          properties:
            dqv:isMeasurementOf:
              const: Goodness-of-Fit
          required:
          - dqv:isMeasurementOf
        then:
          properties:
            dqv:value:
              description: The statistic reported to show whether scatter among the
                contributing analyses exceeds what analytical uncertainty alone predicts,
                together with its value. Answers whether a reported aggregate is defensible
                as a single population. Procedure-level tier is N/A because the value
                cannot be known before the analysis; the procedure may still state
                an acceptance threshold, which belongs with the inclusion criteria.
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
    - contains:
        properties:
          dqv:isMeasurementOf:
            const: Dispersion Statistic
        required:
        - dqv:isMeasurementOf
    - contains:
        properties:
          dqv:isMeasurementOf:
            const: Goodness-of-Fit
        required:
        - dqv:isMeasurementOf
  ada:sensitivityYield:
    type: string
required:
- schema:funding
- ada:spotDiameterMeasured

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS-UPb/detail/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-Q-ICPMS-UPb/detail/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "wd": "https://www.wikidata.org/entity/",
    "nxs": "https://manual.nexusformat.org/classes/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "cdif": "https://w3id.org/cdif/",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "ada": "https://ada.astromat.org/metadata/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "prov": "http://www.w3.org/ns/prov#",
    "bios": "https://bioschemas.org/",
    "spdx": "http://spdx.org/rdf/terms#",
    "geosparql": "http://www.opengis.net/ont/geosparql#",
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

