
# LA-SF-ICP-MS U-Pb Analysis Detail (Schema)

`ogch.techniqueProfile.geochemProfile.LA-SF-ICPMS-UPb.detail` *v0.1*

Dataset-level analysis-instance detail for LA-SF-ICP-MS U-Pb geochronology, reusing CDIF/schema.org slots on the schema:Dataset root.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### detail example Zhang2022
detail instance derived from Zhang et al. 2022 (GCA 323) Iron meteorites Raster mapping + Spot (Ge) ns-LA-SF-ICP-MS Florida State University.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Zhang2022",
  "@type": [
    "ada:LAICPMSGeochronTabular"
  ],
  "ada:componentType": "ada:LAICPMSGeochronTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laSficpmsUPbTAPP-Zhang2022"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA Grants 80NSSC19K1238 (BZ), 80NSSC19K1613 (NLC), 80NSSC18K0595 (MH), NNX17AE77G (AER); NSF Cooperative Agreement DMR-1644779 and State of Florida [Acknowledgements]",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "Raster over \"a few millimeters\" of polished iron slab surface (area not precisely stated)",
  "ada:signalIntegrationTime": "N/A (mapping) / ~20 s (Ge spots: 20 s ablation at 50 Hz)",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:radiogenicFractionOfMeasuredSignal": "missing",
  "ada:ageDatumReferenceEpoch": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:detectionLimit": "LODs not formally reported; all concentrations above detection limits except noted (Cr in some irons below LOD)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "LA-ICP-MS concentrations agreed with NAA within ±40% for most elements (LA relative to NAA); within ±10% for Ni, Co, Ga; differences in W (4.39 vs 1.06 ng g⁻¹ for Cerro del Inca by LA vs INAA) and Au/As up to 30% — attributed to heterogeneous sampling scale difference between techniques",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSize"
        }
      ],
      "schema:name": "Transect Rate, Mapping Rate or Step Size",
      "schema:value": "10 µm s⁻¹ (raster scan); N/A (spot Ge)"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS-UPb/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Zhang2022",
  "@type": [
    "ada:LAICPMSGeochronTabular"
  ],
  "ada:componentType": "ada:LAICPMSGeochronTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laSficpmsUPbTAPP-Zhang2022"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA Grants 80NSSC19K1238 (BZ), 80NSSC19K1613 (NLC), 80NSSC18K0595 (MH), NNX17AE77G (AER); NSF Cooperative Agreement DMR-1644779 and State of Florida [Acknowledgements]",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "Raster over \"a few millimeters\" of polished iron slab surface (area not precisely stated)",
  "ada:signalIntegrationTime": "N/A (mapping) / ~20 s (Ge spots: 20 s ablation at 50 Hz)",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:radiogenicFractionOfMeasuredSignal": "missing",
  "ada:ageDatumReferenceEpoch": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:detectionLimit": "LODs not formally reported; all concentrations above detection limits except noted (Cr in some irons below LOD)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "LA-ICP-MS concentrations agreed with NAA within \u00b140% for most elements (LA relative to NAA); within \u00b110% for Ni, Co, Ga; differences in W (4.39 vs 1.06 ng g\u207b\u00b9 for Cerro del Inca by LA vs INAA) and Au/As up to 30% \u2014 attributed to heterogeneous sampling scale difference between techniques",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSize"
        }
      ],
      "schema:name": "Transect Rate, Mapping Rate or Step Size",
      "schema:value": "10 \u00b5m s\u207b\u00b9 (raster scan); N/A (spot Ge)"
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

ex:detail-Zhang2022 a ada:LAICPMSGeochronTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSize> ;
    schema1:measurementTechnique ex:laSficpmsUPbTAPP-Zhang2022 ;
    ada:ageDatumReferenceEpoch "missing" ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "LA-ICP-MS concentrations agreed with NAA within ±40% for most elements (LA relative to NAA); within ±10% for Ni, Co, Ga; differences in W (4.39 vs 1.06 ng g⁻¹ for Cerro del Inca by LA vs INAA) and Au/As up to 30% — attributed to heterogeneous sampling scale difference between techniques" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:LAICPMSGeochronTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "LODs not formally reported; all concentrations above detection limits except noted (Cr in some irons below LOD)" ;
    ada:errorCorrelationBetweenReportedQuantities -9999 ;
    ada:fundingSourceForAnalysis "NASA Grants 80NSSC19K1238 (BZ), 80NSSC19K1613 (NLC), 80NSSC18K0595 (MH), NNX17AE77G (AER); NSF Cooperative Agreement DMR-1644779 and State of Florida [Acknowledgements]" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "Raster over \"a few millimeters\" of polished iron slab surface (area not precisely stated)" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:radiogenicFractionOfMeasuredSignal "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime "N/A (mapping) / ~20 s (Ge spots: 20 s ablation at 50 Hz)" ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSize> a schema1:PropertyValue ;
    schema1:name "Transect Rate, Mapping Rate or Step Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSize> ;
    schema1:value "10 µm s⁻¹ (raster scan); N/A (spot Ge)" .


```


### detail example Chernonozhkin2021
detail instance derived from Chernonozhkin et al. 2021 (Chem Geol 562) Pallasite olivine Raster mapping (2D) ns-LA-SF-ICP-MS Ghent University.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Chernonozhkin2021",
  "@type": [
    "ada:LAICPMSGeochronTabular"
  ],
  "ada:componentType": "ada:LAICPMSGeochronTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laSficpmsUPbTAPP-Chernonozhkin2021"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "Each map: 1450×600 µm = 870,000 µm²; total of 8 PMG olivines mapped",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:radiogenicFractionOfMeasuredSignal": "missing",
  "ada:ageDatumReferenceEpoch": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:detectionLimit": "LODs reported in Table E1 (Appendix E) for 2D mapping: average of all individual pixel LODs (Na=1, Nb=10 per Longerich et al. 1996)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "Intermediate precision for mapping: most elements at ≥10 µg g⁻¹: 5–15% RSD; elements <10 µg g⁻¹: 5–30% RSD; assessed from repeated GRM mapping in 8 sessions over 1 year (n=8 for each element)",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "No systematic bias demonstrated; MgO+FeO+SiO₂+P₂O₅ oxide sums after mapping varied 95–99 wt% (average near 100%); LA-ICP-MS Fa# values compared to EMPA values for 8 PMG (Fig. 5A shows good agreement)",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSize"
        }
      ],
      "schema:name": "Transect Rate, Mapping Rate or Step Size",
      "schema:value": "9 µm s⁻¹ (continuous raster)"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS-UPb/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Chernonozhkin2021",
  "@type": [
    "ada:LAICPMSGeochronTabular"
  ],
  "ada:componentType": "ada:LAICPMSGeochronTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laSficpmsUPbTAPP-Chernonozhkin2021"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "Each map: 1450\u00d7600 \u00b5m = 870,000 \u00b5m\u00b2; total of 8 PMG olivines mapped",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:radiogenicFractionOfMeasuredSignal": "missing",
  "ada:ageDatumReferenceEpoch": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:detectionLimit": "LODs reported in Table E1 (Appendix E) for 2D mapping: average of all individual pixel LODs (Na=1, Nb=10 per Longerich et al. 1996)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "Intermediate precision for mapping: most elements at \u226510 \u00b5g g\u207b\u00b9: 5\u201315% RSD; elements <10 \u00b5g g\u207b\u00b9: 5\u201330% RSD; assessed from repeated GRM mapping in 8 sessions over 1 year (n=8 for each element)",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "No systematic bias demonstrated; MgO+FeO+SiO\u2082+P\u2082O\u2085 oxide sums after mapping varied 95\u201399 wt% (average near 100%); LA-ICP-MS Fa# values compared to EMPA values for 8 PMG (Fig. 5A shows good agreement)",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSize"
        }
      ],
      "schema:name": "Transect Rate, Mapping Rate or Step Size",
      "schema:value": "9 \u00b5m s\u207b\u00b9 (continuous raster)"
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

ex:detail-Chernonozhkin2021 a ada:LAICPMSGeochronTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSize> ;
    schema1:measurementTechnique ex:laSficpmsUPbTAPP-Chernonozhkin2021 ;
    ada:ageDatumReferenceEpoch "missing" ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "No systematic bias demonstrated; MgO+FeO+SiO₂+P₂O₅ oxide sums after mapping varied 95–99 wt% (average near 100%); LA-ICP-MS Fa# values compared to EMPA values for 8 PMG (Fig. 5A shows good agreement)" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:LAICPMSGeochronTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "LODs reported in Table E1 (Appendix E) for 2D mapping: average of all individual pixel LODs (Na=1, Nb=10 per Longerich et al. 1996)" ;
    ada:errorCorrelationBetweenReportedQuantities -9999 ;
    ada:fundingSourceForAnalysis "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "Each map: 1450×600 µm = 870,000 µm²; total of 8 PMG olivines mapped" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:radiogenicFractionOfMeasuredSignal "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "Intermediate precision for mapping: most elements at ≥10 µg g⁻¹: 5–15% RSD; elements <10 µg g⁻¹: 5–30% RSD; assessed from repeated GRM mapping in 8 sessions over 1 year (n=8 for each element)" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSize> a schema1:PropertyValue ;
    schema1:name "Transect Rate, Mapping Rate or Step Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSize> ;
    schema1:value "9 µm s⁻¹ (continuous raster)" .


```


### detail example Chernonozhkin2021-2
detail instance derived from Chernonozhkin et al. 2021 (Chem Geol 562) Pallasite olivine Line scan (Run 1: major) + Spot (Run 2: trace) [Multi-run] ns-LA-SF-ICP-MS Ghent University.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Chernonozhkin2021-2",
  "@type": [
    "ada:LAICPMSGeochronTabular"
  ],
  "ada:componentType": "ada:LAICPMSGeochronTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laSficpmsUPbTAPP-Chernonozhkin2021-2"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": 3,
  "ada:transectLength": "Line scan length: 400 µm (runs 1 and 2; 34 runs adjusted to measure 400 µm line + blank + washout)",
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": "Run 1: ~50 s (34 runs covering 400 µm line + 10 s blank + washout); Run 2: same structure; actual integrated signal window within run not separately stated",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:radiogenicFractionOfMeasuredSignal": "missing",
  "ada:ageDatumReferenceEpoch": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:detectionLimit": "LODs reported in Table 1 for line scan + spot trace elements: Na=24, Nb=5 per Longerich et al. 1996; LOQ = 10SD criterion",
  "ada:limitOfQuantificationMethod": "LOQ = 10SD of background counts (10σ criterion; Chernonozhkin et al. 2021)",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "LOD calculated per analysis (Na=24, Nb=5); precision not formally reported as separate metric",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "Trace element accuracy verified against literature INAA and EPMA data; major elements verified by comparison with EMPA results from same section",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSize"
        }
      ],
      "schema:name": "Transect Rate, Mapping Rate or Step Size",
      "schema:value": "10 µm s⁻¹ (line scan run 1); spot mode (run 2)"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS-UPb/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Chernonozhkin2021-2",
  "@type": [
    "ada:LAICPMSGeochronTabular"
  ],
  "ada:componentType": "ada:LAICPMSGeochronTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laSficpmsUPbTAPP-Chernonozhkin2021-2"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": 3,
  "ada:transectLength": "Line scan length: 400 \u00b5m (runs 1 and 2; 34 runs adjusted to measure 400 \u00b5m line + blank + washout)",
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": "Run 1: ~50 s (34 runs covering 400 \u00b5m line + 10 s blank + washout); Run 2: same structure; actual integrated signal window within run not separately stated",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:radiogenicFractionOfMeasuredSignal": "missing",
  "ada:ageDatumReferenceEpoch": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:detectionLimit": "LODs reported in Table 1 for line scan + spot trace elements: Na=24, Nb=5 per Longerich et al. 1996; LOQ = 10SD criterion",
  "ada:limitOfQuantificationMethod": "LOQ = 10SD of background counts (10\u03c3 criterion; Chernonozhkin et al. 2021)",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "LOD calculated per analysis (Na=24, Nb=5); precision not formally reported as separate metric",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "Trace element accuracy verified against literature INAA and EPMA data; major elements verified by comparison with EMPA results from same section",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSize"
        }
      ],
      "schema:name": "Transect Rate, Mapping Rate or Step Size",
      "schema:value": "10 \u00b5m s\u207b\u00b9 (line scan run 1); spot mode (run 2)"
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

ex:detail-Chernonozhkin2021-2 a ada:LAICPMSGeochronTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSize> ;
    schema1:measurementTechnique ex:laSficpmsUPbTAPP-Chernonozhkin2021-2 ;
    ada:ageDatumReferenceEpoch "missing" ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "Trace element accuracy verified against literature INAA and EPMA data; major elements verified by comparison with EMPA results from same section" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:LAICPMSGeochronTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "LODs reported in Table 1 for line scan + spot trace elements: Na=24, Nb=5 per Longerich et al. 1996; LOQ = 10SD criterion" ;
    ada:errorCorrelationBetweenReportedQuantities -9999 ;
    ada:fundingSourceForAnalysis "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "LOQ = 10SD of background counts (10σ criterion; Chernonozhkin et al. 2021)" ;
    ada:mappingArea "missing" ;
    ada:numberOfReplicates 3 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:radiogenicFractionOfMeasuredSignal "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime "Run 1: ~50 s (34 runs covering 400 µm line + 10 s blank + washout); Run 2: same structure; actual integrated signal window within run not separately stated" ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength "Line scan length: 400 µm (runs 1 and 2; 34 runs adjusted to measure 400 µm line + blank + washout)" ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "LOD calculated per analysis (Na=24, Nb=5); precision not formally reported as separate metric" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSize> a schema1:PropertyValue ;
    schema1:name "Transect Rate, Mapping Rate or Step Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSize> ;
    schema1:value "10 µm s⁻¹ (line scan run 1); spot mode (run 2)" .


```


### detail example Chernonozhkin2021-3
detail instance derived from Chernonozhkin et al. 2021 (Chem Geol 562) Pallasite phosphate Spot analysis ns-LA-SF-ICP-MS Ghent University.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Chernonozhkin2021-3",
  "@type": [
    "ada:LAICPMSGeochronTabular"
  ],
  "ada:componentType": "ada:LAICPMSGeochronTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laSficpmsUPbTAPP-Chernonozhkin2021-3"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": "Multiple phosphate grains per meteorite; number varies by section",
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": 20,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:radiogenicFractionOfMeasuredSignal": "missing",
  "ada:ageDatumReferenceEpoch": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:detectionLimit": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS-UPb/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Chernonozhkin2021-3",
  "@type": [
    "ada:LAICPMSGeochronTabular"
  ],
  "ada:componentType": "ada:LAICPMSGeochronTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laSficpmsUPbTAPP-Chernonozhkin2021-3"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": "Multiple phosphate grains per meteorite; number varies by section",
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": 20,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:radiogenicFractionOfMeasuredSignal": "missing",
  "ada:ageDatumReferenceEpoch": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:detectionLimit": -9999,
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

ex:detail-Chernonozhkin2021-3 a ada:LAICPMSGeochronTabular ;
    schema1:measurementTechnique ex:laSficpmsUPbTAPP-Chernonozhkin2021-3 ;
    ada:ageDatumReferenceEpoch "missing" ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "missing" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:LAICPMSGeochronTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:errorCorrelationBetweenReportedQuantities -9999 ;
    ada:fundingSourceForAnalysis "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "missing" ;
    ada:numberOfReplicates "Multiple phosphate grains per meteorite; number varies by section" ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:radiogenicFractionOfMeasuredSignal "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime 20 ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .


```


### detail example Mittlefehldt2024
detail instance derived from Mittlefehldt 2024 Appendix A Pallasite olivine Spot analysis ns-LA-SF-ICP-MS Johnson Space Center.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Mittlefehldt2024",
  "@type": [
    "ada:LAICPMSGeochronTabular"
  ],
  "ada:componentType": "ada:LAICPMSGeochronTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laSficpmsUPbTAPP-Mittlefehldt2024"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
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
  "ada:radiogenicFractionOfMeasuredSignal": "missing",
  "ada:ageDatumReferenceEpoch": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "Theoretical 1 sigma analytical precision from counting statistics plus propagation of uncertainties, ~0.6% on the Fe/Mn ratio of pallasite olivine; the observed standard deviations per meteorite range from 0.6 to 4.0%",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "Sc: good agreement with Davis (1977) INAA values within measurement scatter; overall accuracy verified by comparison with literature INAA and SIMS data; Marjalahti used as in-session control (Mn deviation from reference value noted as 4.2% above Ryder 1984)",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS-UPb/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Mittlefehldt2024",
  "@type": [
    "ada:LAICPMSGeochronTabular"
  ],
  "ada:componentType": "ada:LAICPMSGeochronTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laSficpmsUPbTAPP-Mittlefehldt2024"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
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
  "ada:radiogenicFractionOfMeasuredSignal": "missing",
  "ada:ageDatumReferenceEpoch": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "Theoretical 1 sigma analytical precision from counting statistics plus propagation of uncertainties, ~0.6% on the Fe/Mn ratio of pallasite olivine; the observed standard deviations per meteorite range from 0.6 to 4.0%",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "Sc: good agreement with Davis (1977) INAA values within measurement scatter; overall accuracy verified by comparison with literature INAA and SIMS data; Marjalahti used as in-session control (Mn deviation from reference value noted as 4.2% above Ryder 1984)",
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

ex:detail-Mittlefehldt2024 a ada:LAICPMSGeochronTabular ;
    schema1:measurementTechnique ex:laSficpmsUPbTAPP-Mittlefehldt2024 ;
    ada:ageDatumReferenceEpoch "missing" ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "Sc: good agreement with Davis (1977) INAA values within measurement scatter; overall accuracy verified by comparison with literature INAA and SIMS data; Marjalahti used as in-session control (Mn deviation from reference value noted as 4.2% above Ryder 1984)" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:LAICPMSGeochronTabular" ;
    ada:countingStatisticsError "Theoretical 1 sigma analytical precision from counting statistics plus propagation of uncertainties, ~0.6% on the Fe/Mn ratio of pallasite olivine; the observed standard deviations per meteorite range from 0.6 to 4.0%" ;
    ada:detectionLimit -9999 ;
    ada:errorCorrelationBetweenReportedQuantities -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
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
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .


```


### detail example Navarro2024
detail instance derived from Navarro et al. 2024 (ACS ESC 8) Iron meteorites Spot analysis ns-LA-SF-ICP-MS University of Campinas.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Navarro2024",
  "@type": [
    "ada:LAICPMSGeochronTabular"
  ],
  "ada:componentType": "ada:LAICPMSGeochronTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laSficpmsUPbTAPP-Navarro2024"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "M.S.N.: Educorp (Unicamp) and International Association of Geoanalysts for Geoanalysis 2022 presentation; J.E.: CNPq grant 316191/2021-3",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": 20,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": 40,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:radiogenicFractionOfMeasuredSignal": "missing",
  "ada:ageDatumReferenceEpoch": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:detectionLimit": "LODs in µg g⁻¹ (median from Table 3): As 2, Au 0.1, Co 2, Cr 19, Cu 0.8, Fe 5300, Ga 0.1, Ge 0.2, Ir 0.04, Ni 60, Os 0.09, Pd 0.06, Pt 0.4, Re 0.02, Rh 0.05, Ru 0.3, W 0.09; calculated per Longerich et al. (1996) in iolite 4",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "RSD <15% for most elements in Arraias meteorite under repeatability conditions (n=20 spot analyses); Cr: 20%, Ir: 16%, Os: 20% RSD; assessed by repeated analysis of same meteorite in one session",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "Intermediate precision: RSD ≤20% for most elements assessed over multiple days on North Chile iron meteorite measured as unknown (n multiple days over 4 months)",
  "ada:analyticalAccuracyAndAssessmentMethod": "Results for 9 known iron meteorites: >75% of published values within LA-ICP-MS result ± 2s (two standard deviations); relative differences mostly within ±20% (Fig. 2); specific discrepancies: Ir in Arraias +40%, Ir in Nossa Senhora +64%, Co and Ga in Campo del Cielo (heterogeneity issues); trend lines slope 0.87–1.17 with R² = 0.97–1.0",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS-UPb/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Navarro2024",
  "@type": [
    "ada:LAICPMSGeochronTabular"
  ],
  "ada:componentType": "ada:LAICPMSGeochronTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laSficpmsUPbTAPP-Navarro2024"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "M.S.N.: Educorp (Unicamp) and International Association of Geoanalysts for Geoanalysis 2022 presentation; J.E.: CNPq grant 316191/2021-3",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": 20,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": 40,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:radiogenicFractionOfMeasuredSignal": "missing",
  "ada:ageDatumReferenceEpoch": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:detectionLimit": "LODs in \u00b5g g\u207b\u00b9 (median from Table 3): As 2, Au 0.1, Co 2, Cr 19, Cu 0.8, Fe 5300, Ga 0.1, Ge 0.2, Ir 0.04, Ni 60, Os 0.09, Pd 0.06, Pt 0.4, Re 0.02, Rh 0.05, Ru 0.3, W 0.09; calculated per Longerich et al. (1996) in iolite 4",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "RSD <15% for most elements in Arraias meteorite under repeatability conditions (n=20 spot analyses); Cr: 20%, Ir: 16%, Os: 20% RSD; assessed by repeated analysis of same meteorite in one session",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "Intermediate precision: RSD \u226420% for most elements assessed over multiple days on North Chile iron meteorite measured as unknown (n multiple days over 4 months)",
  "ada:analyticalAccuracyAndAssessmentMethod": "Results for 9 known iron meteorites: >75% of published values within LA-ICP-MS result \u00b1 2s (two standard deviations); relative differences mostly within \u00b120% (Fig. 2); specific discrepancies: Ir in Arraias +40%, Ir in Nossa Senhora +64%, Co and Ga in Campo del Cielo (heterogeneity issues); trend lines slope 0.87\u20131.17 with R\u00b2 = 0.97\u20131.0",
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

ex:detail-Navarro2024 a ada:LAICPMSGeochronTabular ;
    schema1:measurementTechnique ex:laSficpmsUPbTAPP-Navarro2024 ;
    ada:ageDatumReferenceEpoch "missing" ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "Results for 9 known iron meteorites: >75% of published values within LA-ICP-MS result ± 2s (two standard deviations); relative differences mostly within ±20% (Fig. 2); specific discrepancies: Ir in Arraias +40%, Ir in Nossa Senhora +64%, Co and Ga in Campo del Cielo (heterogeneity issues); trend lines slope 0.87–1.17 with R² = 0.97–1.0" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "Intermediate precision: RSD ≤20% for most elements assessed over multiple days on North Chile iron meteorite measured as unknown (n multiple days over 4 months)" ;
    ada:componentType "ada:LAICPMSGeochronTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "LODs in µg g⁻¹ (median from Table 3): As 2, Au 0.1, Co 2, Cr 19, Cu 0.8, Fe 5300, Ga 0.1, Ge 0.2, Ir 0.04, Ni 60, Os 0.09, Pd 0.06, Pt 0.4, Re 0.02, Rh 0.05, Ru 0.3, W 0.09; calculated per Longerich et al. (1996) in iolite 4" ;
    ada:errorCorrelationBetweenReportedQuantities -9999 ;
    ada:fundingSourceForAnalysis "M.S.N.: Educorp (Unicamp) and International Association of Geoanalysts for Geoanalysis 2022 presentation; J.E.: CNPq grant 316191/2021-3" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "missing" ;
    ada:numberOfReplicates 20 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:radiogenicFractionOfMeasuredSignal "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime 40 ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "RSD <15% for most elements in Arraias meteorite under repeatability conditions (n=20 spot analyses); Cr: 20%, Ir: 16%, Os: 20% RSD; assessed by repeated analysis of same meteorite in one session" .


```


### detail example Navarro2024-2
detail instance derived from Navarro et al. 2024 (ACS ESC 8) Iron meteorites Raster mapping (2D) ns-LA-SF-ICP-MS University of Campinas.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Navarro2024-2",
  "@type": [
    "ada:LAICPMSGeochronTabular"
  ],
  "ada:componentType": "ada:LAICPMSGeochronTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laSficpmsUPbTAPP-Navarro2024-2"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "M.S.N.: Educorp (Unicamp) and International Association of Geoanalysts; J.E.: CNPq grant 316191/2021-3",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": 1,
  "ada:transectLength": -9999,
  "ada:mappingArea": "Augusto Pestana: 30 min mapping session (area not explicitly stated; 150 µm spot at 10 µm s⁻¹)",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:radiogenicFractionOfMeasuredSignal": "missing",
  "ada:ageDatumReferenceEpoch": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSize"
        }
      ],
      "schema:name": "Transect Rate, Mapping Rate or Step Size",
      "schema:value": "10 µm s⁻¹ (continuous raster scan)"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS-UPb/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Navarro2024-2",
  "@type": [
    "ada:LAICPMSGeochronTabular"
  ],
  "ada:componentType": "ada:LAICPMSGeochronTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laSficpmsUPbTAPP-Navarro2024-2"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "M.S.N.: Educorp (Unicamp) and International Association of Geoanalysts; J.E.: CNPq grant 316191/2021-3",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": 1,
  "ada:transectLength": -9999,
  "ada:mappingArea": "Augusto Pestana: 30 min mapping session (area not explicitly stated; 150 \u00b5m spot at 10 \u00b5m s\u207b\u00b9)",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:radiogenicFractionOfMeasuredSignal": "missing",
  "ada:ageDatumReferenceEpoch": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSize"
        }
      ],
      "schema:name": "Transect Rate, Mapping Rate or Step Size",
      "schema:value": "10 \u00b5m s\u207b\u00b9 (continuous raster scan)"
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

ex:detail-Navarro2024-2 a ada:LAICPMSGeochronTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSize> ;
    schema1:measurementTechnique ex:laSficpmsUPbTAPP-Navarro2024-2 ;
    ada:ageDatumReferenceEpoch "missing" ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "missing" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:LAICPMSGeochronTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:errorCorrelationBetweenReportedQuantities -9999 ;
    ada:fundingSourceForAnalysis "M.S.N.: Educorp (Unicamp) and International Association of Geoanalysts; J.E.: CNPq grant 316191/2021-3" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "Augusto Pestana: 30 min mapping session (area not explicitly stated; 150 µm spot at 10 µm s⁻¹)" ;
    ada:numberOfReplicates 1 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:radiogenicFractionOfMeasuredSignal "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSize> a schema1:PropertyValue ;
    schema1:name "Transect Rate, Mapping Rate or Step Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSize> ;
    schema1:value "10 µm s⁻¹ (continuous raster scan)" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: LA-SF-ICP-MS U-Pb Analysis Detail
description: Dataset-level analysis-instance detail for LA-SF-ICP-MS U-Pb geochronology,
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
                            - title: Pulse/Analog Detector Nonlinearity Correction
                              description: Whether a correction was applied for nonlinear
                                detector response at the transition between pulse-counting
                                and analog (and Faraday, for triple-mode instruments)
                                detection modes. Cross-calibration factors between
                                detector modes must be confirmed, typically measured
                                each session. Record 'Applied' and describe the method,
                                the detector modes involved and the analytes affected;
                                'None' where a crossover exists on this instrument
                                but no correction was made, giving the reason; and
                                'N/A' where the detector is pulse-counting only and
                                no crossover exists.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laSficpmsUPbTAPP/pulseAnalogDetectorNonlinearityCorrection
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laSficpmsUPbTAPP/pulseAnalogDetectorNonlinearityCorrection
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
                              title: Pulse/Analog Detector Nonlinearity Correction
                              description: Whether a correction was applied for nonlinear
                                detector response at the transition between pulse-counting
                                and analog (and Faraday, for triple-mode instruments)
                                detection modes. Cross-calibration factors between
                                detector modes must be confirmed, typically measured
                                each session. Record 'Applied' and describe the method,
                                the detector modes involved and the analytes affected;
                                'None' where a crossover exists on this instrument
                                but no correction was made, giving the reason; and
                                'N/A' where the detector is pulse-counting only and
                                no crossover exists.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laSficpmsUPbTAPP/pulseAnalogDetectorNonlinearityCorrection
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laSficpmsUPbTAPP/pulseAnalogDetectorNonlinearityCorrection
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
                  by the analyte element they serve where they serve one. Covers atomic
                  isotopes and, where a reaction cell shifts an analyte onto a different
                  mass, the product mass actually measured. Includes interference-monitor
                  and internal-standard masses, which serve no analyte and so have
                  no parent element. The analyte list is given by the Analyte field
                  and is never inferred from the element symbols appearing here.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laSficpmsUPbTAPP/monitoredMasses
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laSficpmsUPbTAPP/monitoredMasses
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
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_ionCounterDeadTime
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
                    const: ada:parameter/laSficpmsUPbTAPP/numberOfReplicates
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laSficpmsUPbTAPP/numberOfReplicates
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
                    const: ada:parameter/laSficpmsUPbTAPP/errorCorrelationBetweenReportedQuantities
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laSficpmsUPbTAPP/errorCorrelationBetweenReportedQuantities
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
                    const: ada:parameter/laSficpmsUPbTAPP/totalIntegrationTimePerOutputDataPoint
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laSficpmsUPbTAPP/totalIntegrationTimePerOutputDataPoint
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
                  by the analyte element they serve where they serve one. Covers atomic
                  isotopes and, where a reaction cell shifts an analyte onto a different
                  mass, the product mass actually measured. Includes interference-monitor
                  and internal-standard masses, which serve no analyte and so have
                  no parent element. The analyte list is given by the Analyte field
                  and is never inferred from the element symbols appearing here.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laSficpmsUPbTAPP/monitoredMasses
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laSficpmsUPbTAPP/monitoredMasses
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
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_ionCounterDeadTime
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
                    const: ada:parameter/laSficpmsUPbTAPP/numberOfReplicates
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laSficpmsUPbTAPP/numberOfReplicates
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
                    const: ada:parameter/laSficpmsUPbTAPP/errorCorrelationBetweenReportedQuantities
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laSficpmsUPbTAPP/errorCorrelationBetweenReportedQuantities
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
                    const: ada:parameter/laSficpmsUPbTAPP/totalIntegrationTimePerOutputDataPoint
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laSficpmsUPbTAPP/totalIntegrationTimePerOutputDataPoint
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
                                  allOf:
                                  - contains:
                                      properties:
                                        schema:additionalType:
                                          contains:
                                            const: ICP Source
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
                                          const: ada:parameter/laSficpmsUPbTAPP/doublyChargedSpeciesMonitor
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/laSficpmsUPbTAPP/doublyChargedSpeciesMonitor
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
                                          const: ada:parameter/laSficpmsUPbTAPP/doublyChargedSpeciesProduction
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/laSficpmsUPbTAPP/doublyChargedSpeciesProduction
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
                                          const: ada:parameter/laSficpmsUPbTAPP/doublyChargedSpeciesMonitor
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/laSficpmsUPbTAPP/doublyChargedSpeciesMonitor
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
                                          const: ada:parameter/laSficpmsUPbTAPP/doublyChargedSpeciesProduction
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/laSficpmsUPbTAPP/doublyChargedSpeciesProduction
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

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS-UPb/detail/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS-UPb/detail/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS-UPb/detail/context.jsonld)

## Sources

* [LA-SF-ICP-MS_UPb_TAPP_v17.csv (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/LA-SF-ICPMS-UPb/detail`

