
# LA-SF-ICP-MS Analysis Detail (Schema)

`ogch.techniqueProfile.geochemProfile.LA-SF-ICPMS.detail` *v0.1*

Dataset-level analysis-instance detail for LA-SF-ICP-MS, reusing CDIF/schema.org slots on the schema:Dataset root.

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
    "ada:LAICPMSTabular"
  ],
  "ada:componentType": "ada:LAICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laSficpmsTAPP-Zhang2022"
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
      "schema:name": "NASA Grants 80NSSC19K1238 (BZ), 80NSSC19K1613 (NLC), 80NSSC18K0595 (MH), NNX17AE77G (AER); NSF Cooperative Agreement DMR-1644779 and State of Florida [Acknowledgements]"
    }
  ],
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:spotDiameterMeasured": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "Raster over \"a few millimeters\" of polished iron slab surface (area not precisely stated)",
  "ada:signalIntegrationTime": "N/A (mapping) / ~20 s (Ge spots: 20 s ablation at 50 Hz)",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "LODs not formally reported; all concentrations above detection limits except noted (Cr in some irons below LOD)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "LA-ICP-MS concentrations agreed with NAA within ±40% for most elements (LA relative to NAA); within ±10% for Ni, Co, Ga; differences in W (4.39 vs 1.06 ng g⁻¹ for Cerro del Inca by LA vs INAA) and Au/As up to 30% — attributed to heterogeneous sampling scale difference between techniques",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize"
        }
      ],
      "schema:name": "Transect Rate, Mapping Rate or Step Size",
      "schema:value": "10 µm s⁻¹ (raster scan); N/A (spot Ge)"
    },
    {
      "@id": "ada:parameter/laSficpmsTAPP/uncertaintyPropagationMethod",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsTAPP/uncertaintyPropagationMethod"
        }
      ],
      "schema:name": "Uncertainty Propagation Method",
      "schema:value": "Standard deviation (SD) across individual integration cycles of raster scans; uncertainty propagation not formally described"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Zhang2022",
  "@type": [
    "ada:LAICPMSTabular"
  ],
  "ada:componentType": "ada:LAICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laSficpmsTAPP-Zhang2022"
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
      "schema:name": "NASA Grants 80NSSC19K1238 (BZ), 80NSSC19K1613 (NLC), 80NSSC18K0595 (MH), NNX17AE77G (AER); NSF Cooperative Agreement DMR-1644779 and State of Florida [Acknowledgements]"
    }
  ],
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:spotDiameterMeasured": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "Raster over \"a few millimeters\" of polished iron slab surface (area not precisely stated)",
  "ada:signalIntegrationTime": "N/A (mapping) / ~20 s (Ge spots: 20 s ablation at 50 Hz)",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "LODs not formally reported; all concentrations above detection limits except noted (Cr in some irons below LOD)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "LA-ICP-MS concentrations agreed with NAA within \u00b140% for most elements (LA relative to NAA); within \u00b110% for Ni, Co, Ga; differences in W (4.39 vs 1.06 ng g\u207b\u00b9 for Cerro del Inca by LA vs INAA) and Au/As up to 30% \u2014 attributed to heterogeneous sampling scale difference between techniques",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize"
        }
      ],
      "schema:name": "Transect Rate, Mapping Rate or Step Size",
      "schema:value": "10 \u00b5m s\u207b\u00b9 (raster scan); N/A (spot Ge)"
    },
    {
      "@id": "ada:parameter/laSficpmsTAPP/uncertaintyPropagationMethod",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsTAPP/uncertaintyPropagationMethod"
        }
      ],
      "schema:name": "Uncertainty Propagation Method",
      "schema:value": "Standard deviation (SD) across individual integration cycles of raster scans; uncertainty propagation not formally described"
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

ex:detail-Zhang2022 a ada:LAICPMSTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize>,
        <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/uncertaintyPropagationMethod> ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NASA Grants 80NSSC19K1238 (BZ), 80NSSC19K1613 (NLC), 80NSSC18K0595 (MH), NNX17AE77G (AER); NSF Cooperative Agreement DMR-1644779 and State of Florida [Acknowledgements]" ] ;
    schema1:measurementTechnique ex:laSficpmsTAPP-Zhang2022 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "LA-ICP-MS concentrations agreed with NAA within ±40% for most elements (LA relative to NAA); within ±10% for Ni, Co, Ga; differences in W (4.39 vs 1.06 ng g⁻¹ for Cerro del Inca by LA vs INAA) and Au/As up to 30% — attributed to heterogeneous sampling scale difference between techniques" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:LAICPMSTabular" ;
    ada:detectionLimit "LODs not formally reported; all concentrations above detection limits except noted (Cr in some irons below LOD)" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "Raster over \"a few millimeters\" of polished iron slab surface (area not precisely stated)" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime "N/A (mapping) / ~20 s (Ge spots: 20 s ablation at 50 Hz)" ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize> a schema1:PropertyValue ;
    schema1:name "Transect Rate, Mapping Rate or Step Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize> ;
    schema1:value "10 µm s⁻¹ (raster scan); N/A (spot Ge)" .

<https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/uncertaintyPropagationMethod> a schema1:PropertyValue ;
    schema1:name "Uncertainty Propagation Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/uncertaintyPropagationMethod> ;
    schema1:value "Standard deviation (SD) across individual integration cycles of raster scans; uncertainty propagation not formally described" .


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
    "ada:LAICPMSTabular"
  ],
  "ada:componentType": "ada:LAICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laSficpmsTAPP-Chernonozhkin2021"
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
      "schema:name": "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent"
    }
  ],
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:spotDiameterMeasured": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "Each map: 1450×600 µm = 870,000 µm²; total of 8 PMG olivines mapped",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "LODs reported in Table E1 (Appendix E) for 2D mapping: average of all individual pixel LODs (Na=1, Nb=10 per Longerich et al. 1996)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "Intermediate precision for mapping: most elements at ≥10 µg g⁻¹: 5–15% RSD; elements <10 µg g⁻¹: 5–30% RSD; assessed from repeated GRM mapping in 8 sessions over 1 year (n=8 for each element)",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "No systematic bias demonstrated; MgO+FeO+SiO₂+P₂O₅ oxide sums after mapping varied 95–99 wt% (average near 100%); LA-ICP-MS Fa# values compared to EMPA values for 8 PMG (Fig. 5A shows good agreement)",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize"
        }
      ],
      "schema:name": "Transect Rate, Mapping Rate or Step Size",
      "schema:value": "9 µm s⁻¹ (continuous raster)"
    },
    {
      "@id": "ada:parameter/laSficpmsTAPP/uncertaintyPropagationMethod",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsTAPP/uncertaintyPropagationMethod"
        }
      ],
      "schema:name": "Uncertainty Propagation Method",
      "schema:value": "Longerich et al. (1996) equation (3SD/S × √(1/Nb + 1/Na))"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Chernonozhkin2021",
  "@type": [
    "ada:LAICPMSTabular"
  ],
  "ada:componentType": "ada:LAICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laSficpmsTAPP-Chernonozhkin2021"
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
      "schema:name": "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent"
    }
  ],
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:spotDiameterMeasured": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "Each map: 1450\u00d7600 \u00b5m = 870,000 \u00b5m\u00b2; total of 8 PMG olivines mapped",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "LODs reported in Table E1 (Appendix E) for 2D mapping: average of all individual pixel LODs (Na=1, Nb=10 per Longerich et al. 1996)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "Intermediate precision for mapping: most elements at \u226510 \u00b5g g\u207b\u00b9: 5\u201315% RSD; elements <10 \u00b5g g\u207b\u00b9: 5\u201330% RSD; assessed from repeated GRM mapping in 8 sessions over 1 year (n=8 for each element)",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "No systematic bias demonstrated; MgO+FeO+SiO\u2082+P\u2082O\u2085 oxide sums after mapping varied 95\u201399 wt% (average near 100%); LA-ICP-MS Fa# values compared to EMPA values for 8 PMG (Fig. 5A shows good agreement)",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize"
        }
      ],
      "schema:name": "Transect Rate, Mapping Rate or Step Size",
      "schema:value": "9 \u00b5m s\u207b\u00b9 (continuous raster)"
    },
    {
      "@id": "ada:parameter/laSficpmsTAPP/uncertaintyPropagationMethod",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsTAPP/uncertaintyPropagationMethod"
        }
      ],
      "schema:name": "Uncertainty Propagation Method",
      "schema:value": "Longerich et al. (1996) equation (3SD/S \u00d7 \u221a(1/Nb + 1/Na))"
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

ex:detail-Chernonozhkin2021 a ada:LAICPMSTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize>,
        <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/uncertaintyPropagationMethod> ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent" ] ;
    schema1:measurementTechnique ex:laSficpmsTAPP-Chernonozhkin2021 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "No systematic bias demonstrated; MgO+FeO+SiO₂+P₂O₅ oxide sums after mapping varied 95–99 wt% (average near 100%); LA-ICP-MS Fa# values compared to EMPA values for 8 PMG (Fig. 5A shows good agreement)" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:LAICPMSTabular" ;
    ada:detectionLimit "LODs reported in Table E1 (Appendix E) for 2D mapping: average of all individual pixel LODs (Na=1, Nb=10 per Longerich et al. 1996)" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "Each map: 1450×600 µm = 870,000 µm²; total of 8 PMG olivines mapped" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "Intermediate precision for mapping: most elements at ≥10 µg g⁻¹: 5–15% RSD; elements <10 µg g⁻¹: 5–30% RSD; assessed from repeated GRM mapping in 8 sessions over 1 year (n=8 for each element)" .

<https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize> a schema1:PropertyValue ;
    schema1:name "Transect Rate, Mapping Rate or Step Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize> ;
    schema1:value "9 µm s⁻¹ (continuous raster)" .

<https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/uncertaintyPropagationMethod> a schema1:PropertyValue ;
    schema1:name "Uncertainty Propagation Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/uncertaintyPropagationMethod> ;
    schema1:value "Longerich et al. (1996) equation (3SD/S × √(1/Nb + 1/Na))" .


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
    "ada:LAICPMSTabular"
  ],
  "ada:componentType": "ada:LAICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laSficpmsTAPP-Chernonozhkin2021-2"
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
      "schema:name": "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent"
    }
  ],
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:spotDiameterMeasured": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": 3,
  "ada:transectLength": "Line scan length: 400 µm (runs 1 and 2; 34 runs adjusted to measure 400 µm line + blank + washout)",
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": "Run 1: ~50 s (34 runs covering 400 µm line + 10 s blank + washout); Run 2: same structure; actual integrated signal window within run not separately stated",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "LODs reported in Table 1 for line scan + spot trace elements: Na=24, Nb=5 per Longerich et al. 1996; LOQ = 10SD criterion",
  "ada:limitOfQuantificationMethod": "LOQ = 10SD of background counts (10σ criterion; Chernonozhkin et al. 2021)",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "LOD calculated per analysis (Na=24, Nb=5); precision not formally reported as separate metric",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "Trace element accuracy verified against literature INAA and EPMA data; major elements verified by comparison with EMPA results from same section",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize"
        }
      ],
      "schema:name": "Transect Rate, Mapping Rate or Step Size",
      "schema:value": "10 µm s⁻¹ (line scan run 1); spot mode (run 2)"
    },
    {
      "@id": "ada:parameter/laSficpmsTAPP/uncertaintyPropagationMethod",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsTAPP/uncertaintyPropagationMethod"
        }
      ],
      "schema:name": "Uncertainty Propagation Method",
      "schema:value": "Longerich et al. (1996) for LOD; uncertainty for concentrations not formally described"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Chernonozhkin2021-2",
  "@type": [
    "ada:LAICPMSTabular"
  ],
  "ada:componentType": "ada:LAICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laSficpmsTAPP-Chernonozhkin2021-2"
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
      "schema:name": "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent"
    }
  ],
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:spotDiameterMeasured": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": 3,
  "ada:transectLength": "Line scan length: 400 \u00b5m (runs 1 and 2; 34 runs adjusted to measure 400 \u00b5m line + blank + washout)",
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": "Run 1: ~50 s (34 runs covering 400 \u00b5m line + 10 s blank + washout); Run 2: same structure; actual integrated signal window within run not separately stated",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "LODs reported in Table 1 for line scan + spot trace elements: Na=24, Nb=5 per Longerich et al. 1996; LOQ = 10SD criterion",
  "ada:limitOfQuantificationMethod": "LOQ = 10SD of background counts (10\u03c3 criterion; Chernonozhkin et al. 2021)",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "LOD calculated per analysis (Na=24, Nb=5); precision not formally reported as separate metric",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "Trace element accuracy verified against literature INAA and EPMA data; major elements verified by comparison with EMPA results from same section",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize"
        }
      ],
      "schema:name": "Transect Rate, Mapping Rate or Step Size",
      "schema:value": "10 \u00b5m s\u207b\u00b9 (line scan run 1); spot mode (run 2)"
    },
    {
      "@id": "ada:parameter/laSficpmsTAPP/uncertaintyPropagationMethod",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsTAPP/uncertaintyPropagationMethod"
        }
      ],
      "schema:name": "Uncertainty Propagation Method",
      "schema:value": "Longerich et al. (1996) for LOD; uncertainty for concentrations not formally described"
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

ex:detail-Chernonozhkin2021-2 a ada:LAICPMSTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize>,
        <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/uncertaintyPropagationMethod> ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent" ] ;
    schema1:measurementTechnique ex:laSficpmsTAPP-Chernonozhkin2021-2 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "Trace element accuracy verified against literature INAA and EPMA data; major elements verified by comparison with EMPA results from same section" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:LAICPMSTabular" ;
    ada:detectionLimit "LODs reported in Table 1 for line scan + spot trace elements: Na=24, Nb=5 per Longerich et al. 1996; LOQ = 10SD criterion" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:limitOfQuantificationMethod "LOQ = 10SD of background counts (10σ criterion; Chernonozhkin et al. 2021)" ;
    ada:mappingArea "missing" ;
    ada:numberOfReplicates 3 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime "Run 1: ~50 s (34 runs covering 400 µm line + 10 s blank + washout); Run 2: same structure; actual integrated signal window within run not separately stated" ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength "Line scan length: 400 µm (runs 1 and 2; 34 runs adjusted to measure 400 µm line + blank + washout)" ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "LOD calculated per analysis (Na=24, Nb=5); precision not formally reported as separate metric" .

<https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize> a schema1:PropertyValue ;
    schema1:name "Transect Rate, Mapping Rate or Step Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize> ;
    schema1:value "10 µm s⁻¹ (line scan run 1); spot mode (run 2)" .

<https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/uncertaintyPropagationMethod> a schema1:PropertyValue ;
    schema1:name "Uncertainty Propagation Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/uncertaintyPropagationMethod> ;
    schema1:value "Longerich et al. (1996) for LOD; uncertainty for concentrations not formally described" .


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
    "ada:LAICPMSTabular"
  ],
  "ada:componentType": "ada:LAICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laSficpmsTAPP-Chernonozhkin2021-3"
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
      "schema:name": "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent"
    }
  ],
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:spotDiameterMeasured": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": "Multiple phosphate grains per meteorite; number varies by section",
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": 20,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laSficpmsTAPP/uncertaintyPropagationMethod",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsTAPP/uncertaintyPropagationMethod"
        }
      ],
      "schema:name": "Uncertainty Propagation Method",
      "schema:value": "Longerich et al. (1996) for LOD; uncertainty not formally described"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Chernonozhkin2021-3",
  "@type": [
    "ada:LAICPMSTabular"
  ],
  "ada:componentType": "ada:LAICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laSficpmsTAPP-Chernonozhkin2021-3"
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
      "schema:name": "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent"
    }
  ],
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:spotDiameterMeasured": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": "Multiple phosphate grains per meteorite; number varies by section",
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": 20,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laSficpmsTAPP/uncertaintyPropagationMethod",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsTAPP/uncertaintyPropagationMethod"
        }
      ],
      "schema:name": "Uncertainty Propagation Method",
      "schema:value": "Longerich et al. (1996) for LOD; uncertainty not formally described"
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

ex:detail-Chernonozhkin2021-3 a ada:LAICPMSTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/uncertaintyPropagationMethod> ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent" ] ;
    schema1:measurementTechnique ex:laSficpmsTAPP-Chernonozhkin2021-3 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "missing" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:LAICPMSTabular" ;
    ada:detectionLimit -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "missing" ;
    ada:numberOfReplicates "Multiple phosphate grains per meteorite; number varies by section" ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime 20 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/uncertaintyPropagationMethod> a schema1:PropertyValue ;
    schema1:name "Uncertainty Propagation Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/uncertaintyPropagationMethod> ;
    schema1:value "Longerich et al. (1996) for LOD; uncertainty not formally described" .


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
    "ada:LAICPMSTabular"
  ],
  "ada:componentType": "ada:LAICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laSficpmsTAPP-Mittlefehldt2024"
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
      "schema:name": "missing"
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
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "Sc: good agreement with Davis (1977) INAA values within measurement scatter; overall accuracy verified by comparison with literature INAA and SIMS data; Marjalahti used as in-session control (Mn deviation from reference value noted as 4.2% above Ryder 1984)",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Mittlefehldt2024",
  "@type": [
    "ada:LAICPMSTabular"
  ],
  "ada:componentType": "ada:LAICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laSficpmsTAPP-Mittlefehldt2024"
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
      "schema:name": "missing"
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
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "Sc: good agreement with Davis (1977) INAA values within measurement scatter; overall accuracy verified by comparison with literature INAA and SIMS data; Marjalahti used as in-session control (Mn deviation from reference value noted as 4.2% above Ryder 1984)",
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Mittlefehldt2024 a ada:LAICPMSTabular ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:laSficpmsTAPP-Mittlefehldt2024 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "Sc: good agreement with Davis (1977) INAA values within measurement scatter; overall accuracy verified by comparison with literature INAA and SIMS data; Marjalahti used as in-session control (Mn deviation from reference value noted as 4.2% above Ryder 1984)" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:LAICPMSTabular" ;
    ada:detectionLimit -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
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
    "ada:LAICPMSTabular"
  ],
  "ada:componentType": "ada:LAICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laSficpmsTAPP-Navarro2024"
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
      "schema:name": "M.S.N.: Educorp (Unicamp) and International Association of Geoanalysts for Geoanalysis 2022 presentation; J.E.: CNPq grant 316191/2021-3"
    }
  ],
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:spotDiameterMeasured": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": 20,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": 40,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "LODs in µg g⁻¹ (median from Table 3): As 2, Au 0.1, Co 2, Cr 19, Cu 0.8, Fe 5300, Ga 0.1, Ge 0.2, Ir 0.04, Ni 60, Os 0.09, Pd 0.06, Pt 0.4, Re 0.02, Rh 0.05, Ru 0.3, W 0.09; calculated per Longerich et al. (1996) in iolite 4",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "RSD <15% for most elements in Arraias meteorite under repeatability conditions (n=20 spot analyses); Cr: 20%, Ir: 16%, Os: 20% RSD; assessed by repeated analysis of same meteorite in one session",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "Intermediate precision: RSD ≤20% for most elements assessed over multiple days on North Chile iron meteorite measured as unknown (n multiple days over 4 months)",
  "ada:analyticalAccuracyAndAssessmentMethod": "Results for 9 known iron meteorites: >75% of published values within LA-ICP-MS result ± 2s (two standard deviations); relative differences mostly within ±20% (Fig. 2); specific discrepancies: Ir in Arraias +40%, Ir in Nossa Senhora +64%, Co and Ga in Campo del Cielo (heterogeneity issues); trend lines slope 0.87–1.17 with R² = 0.97–1.0",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Navarro2024",
  "@type": [
    "ada:LAICPMSTabular"
  ],
  "ada:componentType": "ada:LAICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laSficpmsTAPP-Navarro2024"
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
      "schema:name": "M.S.N.: Educorp (Unicamp) and International Association of Geoanalysts for Geoanalysis 2022 presentation; J.E.: CNPq grant 316191/2021-3"
    }
  ],
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:spotDiameterMeasured": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": 20,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": 40,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "LODs in \u00b5g g\u207b\u00b9 (median from Table 3): As 2, Au 0.1, Co 2, Cr 19, Cu 0.8, Fe 5300, Ga 0.1, Ge 0.2, Ir 0.04, Ni 60, Os 0.09, Pd 0.06, Pt 0.4, Re 0.02, Rh 0.05, Ru 0.3, W 0.09; calculated per Longerich et al. (1996) in iolite 4",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "RSD <15% for most elements in Arraias meteorite under repeatability conditions (n=20 spot analyses); Cr: 20%, Ir: 16%, Os: 20% RSD; assessed by repeated analysis of same meteorite in one session",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "Intermediate precision: RSD \u226420% for most elements assessed over multiple days on North Chile iron meteorite measured as unknown (n multiple days over 4 months)",
  "ada:analyticalAccuracyAndAssessmentMethod": "Results for 9 known iron meteorites: >75% of published values within LA-ICP-MS result \u00b1 2s (two standard deviations); relative differences mostly within \u00b120% (Fig. 2); specific discrepancies: Ir in Arraias +40%, Ir in Nossa Senhora +64%, Co and Ga in Campo del Cielo (heterogeneity issues); trend lines slope 0.87\u20131.17 with R\u00b2 = 0.97\u20131.0",
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Navarro2024 a ada:LAICPMSTabular ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "M.S.N.: Educorp (Unicamp) and International Association of Geoanalysts for Geoanalysis 2022 presentation; J.E.: CNPq grant 316191/2021-3" ] ;
    schema1:measurementTechnique ex:laSficpmsTAPP-Navarro2024 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "Results for 9 known iron meteorites: >75% of published values within LA-ICP-MS result ± 2s (two standard deviations); relative differences mostly within ±20% (Fig. 2); specific discrepancies: Ir in Arraias +40%, Ir in Nossa Senhora +64%, Co and Ga in Campo del Cielo (heterogeneity issues); trend lines slope 0.87–1.17 with R² = 0.97–1.0" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "Intermediate precision: RSD ≤20% for most elements assessed over multiple days on North Chile iron meteorite measured as unknown (n multiple days over 4 months)" ;
    ada:componentType "ada:LAICPMSTabular" ;
    ada:detectionLimit "LODs in µg g⁻¹ (median from Table 3): As 2, Au 0.1, Co 2, Cr 19, Cu 0.8, Fe 5300, Ga 0.1, Ge 0.2, Ir 0.04, Ni 60, Os 0.09, Pd 0.06, Pt 0.4, Re 0.02, Rh 0.05, Ru 0.3, W 0.09; calculated per Longerich et al. (1996) in iolite 4" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "missing" ;
    ada:numberOfReplicates 20 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime 40 ;
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
    "ada:LAICPMSTabular"
  ],
  "ada:componentType": "ada:LAICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laSficpmsTAPP-Navarro2024-2"
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
      "schema:name": "M.S.N.: Educorp (Unicamp) and International Association of Geoanalysts; J.E.: CNPq grant 316191/2021-3"
    }
  ],
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:spotDiameterMeasured": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": 1,
  "ada:transectLength": -9999,
  "ada:mappingArea": "Augusto Pestana: 30 min mapping session (area not explicitly stated; 150 µm spot at 10 µm s⁻¹)",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize"
        }
      ],
      "schema:name": "Transect Rate, Mapping Rate or Step Size",
      "schema:value": "10 µm s⁻¹ (continuous raster scan)"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Navarro2024-2",
  "@type": [
    "ada:LAICPMSTabular"
  ],
  "ada:componentType": "ada:LAICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laSficpmsTAPP-Navarro2024-2"
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
      "schema:name": "M.S.N.: Educorp (Unicamp) and International Association of Geoanalysts; J.E.: CNPq grant 316191/2021-3"
    }
  ],
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:spotDiameterMeasured": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": 1,
  "ada:transectLength": -9999,
  "ada:mappingArea": "Augusto Pestana: 30 min mapping session (area not explicitly stated; 150 \u00b5m spot at 10 \u00b5m s\u207b\u00b9)",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize"
        }
      ],
      "schema:name": "Transect Rate, Mapping Rate or Step Size",
      "schema:value": "10 \u00b5m s\u207b\u00b9 (continuous raster scan)"
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

ex:detail-Navarro2024-2 a ada:LAICPMSTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize> ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "M.S.N.: Educorp (Unicamp) and International Association of Geoanalysts; J.E.: CNPq grant 316191/2021-3" ] ;
    schema1:measurementTechnique ex:laSficpmsTAPP-Navarro2024-2 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "missing" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:LAICPMSTabular" ;
    ada:detectionLimit -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "Augusto Pestana: 30 min mapping session (area not explicitly stated; 150 µm spot at 10 µm s⁻¹)" ;
    ada:numberOfReplicates 1 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize> a schema1:PropertyValue ;
    schema1:name "Transect Rate, Mapping Rate or Step Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize> ;
    schema1:value "10 µm s⁻¹ (continuous raster scan)" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: LA-SF-ICP-MS Analysis Detail
description: Dataset-level analysis-instance detail for LA-SF-ICP-MS, reusing CDIF/schema.org
  slots on the schema:Dataset root.
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
                            const: ada:parameter/laSficpmsTAPP/sampleFormAnalyticalSubstrate
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/laSficpmsTAPP/sampleFormAnalyticalSubstrate
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
                            const: ada:parameter/laSficpmsTAPP/analysisLocationSpotCoordinates
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/laSficpmsTAPP/analysisLocationSpotCoordinates
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
                            const: ada:parameter/laSficpmsTAPP/sampleFormAnalyticalSubstrate
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/laSficpmsTAPP/sampleFormAnalyticalSubstrate
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
                            const: ada:parameter/laSficpmsTAPP/analysisLocationSpotCoordinates
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/laSficpmsTAPP/analysisLocationSpotCoordinates
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
                                const: ada:parameter/laSficpmsTAPP/fusionFluxAndDilutionRatio
                              '@type':
                                const:
                                - schema:PropertyValue
                              schema:propertyID:
                                const:
                                - '@id': ada:parameter/laSficpmsTAPP/fusionFluxAndDilutionRatio
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
                                const: ada:parameter/laSficpmsTAPP/preAblationSurfaceTreatment
                              '@type':
                                const:
                                - schema:PropertyValue
                              schema:propertyID:
                                const:
                                - '@id': ada:parameter/laSficpmsTAPP/preAblationSurfaceTreatment
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
                                const: ada:parameter/laSficpmsTAPP/fusionFluxAndDilutionRatio
                              '@type':
                                const:
                                - schema:PropertyValue
                              schema:propertyID:
                                const:
                                - '@id': ada:parameter/laSficpmsTAPP/fusionFluxAndDilutionRatio
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
                                const: ada:parameter/laSficpmsTAPP/preAblationSurfaceTreatment
                              '@type':
                                const:
                                - schema:PropertyValue
                              schema:propertyID:
                                const:
                                - '@id': ada:parameter/laSficpmsTAPP/preAblationSurfaceTreatment
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
                                const: ada:parameter/laSficpmsTAPP/signalSmoothing
                              '@type':
                                const:
                                - schema:PropertyValue
                              schema:propertyID:
                                const:
                                - '@id': ada:parameter/laSficpmsTAPP/signalSmoothing
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
                                const: ada:parameter/laSficpmsTAPP/uncertaintyPropagationMethod
                              '@type':
                                const:
                                - schema:PropertyValue
                              schema:propertyID:
                                const:
                                - '@id': ada:parameter/laSficpmsTAPP/uncertaintyPropagationMethod
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
                                const: ada:parameter/laSficpmsTAPP/spikeOutlierFilteringApproach
                              '@type':
                                const:
                                - schema:PropertyValue
                              schema:propertyID:
                                const:
                                - '@id': ada:parameter/laSficpmsTAPP/spikeOutlierFilteringApproach
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
                                const: ada:parameter/laSficpmsTAPP/pulseAnalogDetectorNonlinearityCorrection
                              '@type':
                                const:
                                - schema:PropertyValue
                              schema:propertyID:
                                const:
                                - '@id': ada:parameter/laSficpmsTAPP/pulseAnalogDetectorNonlinearityCorrection
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
                                const: ada:parameter/laSficpmsTAPP/calibrationFactorAndDeterminationMethod
                              '@type':
                                const:
                                - schema:PropertyValue
                              schema:propertyID:
                                const:
                                - '@id': ada:parameter/laSficpmsTAPP/calibrationFactorAndDeterminationMethod
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
                                const: ada:parameter/laSficpmsTAPP/signalSmoothing
                              '@type':
                                const:
                                - schema:PropertyValue
                              schema:propertyID:
                                const:
                                - '@id': ada:parameter/laSficpmsTAPP/signalSmoothing
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
                                const: ada:parameter/laSficpmsTAPP/uncertaintyPropagationMethod
                              '@type':
                                const:
                                - schema:PropertyValue
                              schema:propertyID:
                                const:
                                - '@id': ada:parameter/laSficpmsTAPP/uncertaintyPropagationMethod
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
                                const: ada:parameter/laSficpmsTAPP/spikeOutlierFilteringApproach
                              '@type':
                                const:
                                - schema:PropertyValue
                              schema:propertyID:
                                const:
                                - '@id': ada:parameter/laSficpmsTAPP/spikeOutlierFilteringApproach
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
                                const: ada:parameter/laSficpmsTAPP/pulseAnalogDetectorNonlinearityCorrection
                              '@type':
                                const:
                                - schema:PropertyValue
                              schema:propertyID:
                                const:
                                - '@id': ada:parameter/laSficpmsTAPP/pulseAnalogDetectorNonlinearityCorrection
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
                                const: ada:parameter/laSficpmsTAPP/calibrationFactorAndDeterminationMethod
                              '@type':
                                const:
                                - schema:PropertyValue
                              schema:propertyID:
                                const:
                                - '@id': ada:parameter/laSficpmsTAPP/calibrationFactorAndDeterminationMethod
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
                  const: ada:parameter/laSficpmsTAPP/targetSelectionCriteria
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laSficpmsTAPP/targetSelectionCriteria
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
                  const: ada:parameter/laSficpmsTAPP/preAnalysisImagingAndScreening
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laSficpmsTAPP/preAnalysisImagingAndScreening
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
                  const: ada:parameter/laSficpmsTAPP/ablationDurationPerSpot
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laSficpmsTAPP/ablationDurationPerSpot
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
                  const: ada:parameter/laSficpmsTAPP/ablationPitDepthAndAblationRate
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laSficpmsTAPP/ablationPitDepthAndAblationRate
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
                  const: ada:parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize
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
                  const: ada:parameter/laSficpmsTAPP/rasterLineSpacing
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laSficpmsTAPP/rasterLineSpacing
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
                  const: ada:parameter/laSficpmsTAPP/carrierGasAndFlowRate
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laSficpmsTAPP/carrierGasAndFlowRate
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
                  const: ada:parameter/laSficpmsTAPP/plasmaMakeUpGasAddition
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laSficpmsTAPP/plasmaMakeUpGasAddition
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
                  const: ada:parameter/laSficpmsTAPP/analysisSequence
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laSficpmsTAPP/analysisSequence
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
                  const: ada:parameter/laSficpmsTAPP/ionCounterDeadTime
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laSficpmsTAPP/ionCounterDeadTime
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
                recoverable from Dwell Time per Mass alone because settling time is
                not captured there. Applies to sequential (quadrupole and single-collector
                sector-field) acquisition."
              type: object
              properties:
                '@id':
                  const: ada:parameter/laSficpmsTAPP/totalIntegrationTimePerOutputDataPoint
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laSficpmsTAPP/totalIntegrationTimePerOutputDataPoint
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
                with laser off or shutter closed) before each ablation event, in seconds.
                For spot and transect analysis, a discrete background interval is
                measured before each ablation. For mapping, background is typically
                measured once per raster line or at the start of a map session rather
                than before each individual pixel. Editable to allow session-specific
                adjustment.
              type: object
              properties:
                '@id':
                  const: ada:parameter/laSficpmsTAPP/backgroundCountTime
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laSficpmsTAPP/backgroundCountTime
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
                  const: ada:parameter/laSficpmsTAPP/numberOfReplicates
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laSficpmsTAPP/numberOfReplicates
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
                  const: ada:parameter/laSficpmsTAPP/transectLength
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laSficpmsTAPP/transectLength
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
                  const: ada:parameter/laSficpmsTAPP/mappingArea
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laSficpmsTAPP/mappingArea
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
                  const: ada:parameter/laSficpmsTAPP/signalIntegrationTime
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laSficpmsTAPP/signalIntegrationTime
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
                  const: ada:parameter/laSficpmsTAPP/proceduralBlankLevel
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laSficpmsTAPP/proceduralBlankLevel
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
            - title: Constants and Reference Values Used
              description: Physical constants and reference values used in data reduction
                to calculate the final reported quantity (e.g., decay constants for
                age calculation, standard isotope ratios, or other citable reference
                values used in a correction or calculation), together with their source.
                Distinct from the Group 6 reference-material fields, which document
                accepted values for specific calibration/validation materials rather
                than universal physical constants. Record "None" if no citable, revisable
                physical constants feed into this procedure's data reduction.
              type: object
              properties:
                '@id':
                  const: ada:parameter/laSficpmsTAPP/constantsAndReferenceValuesUsed
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laSficpmsTAPP/constantsAndReferenceValuesUsed
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
                  const: ada:parameter/laSficpmsTAPP/targetSelectionCriteria
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laSficpmsTAPP/targetSelectionCriteria
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
                  const: ada:parameter/laSficpmsTAPP/preAnalysisImagingAndScreening
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laSficpmsTAPP/preAnalysisImagingAndScreening
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
                  const: ada:parameter/laSficpmsTAPP/ablationDurationPerSpot
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laSficpmsTAPP/ablationDurationPerSpot
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
                  const: ada:parameter/laSficpmsTAPP/ablationPitDepthAndAblationRate
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laSficpmsTAPP/ablationPitDepthAndAblationRate
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
                  const: ada:parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize
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
                  const: ada:parameter/laSficpmsTAPP/rasterLineSpacing
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laSficpmsTAPP/rasterLineSpacing
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
                  const: ada:parameter/laSficpmsTAPP/carrierGasAndFlowRate
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laSficpmsTAPP/carrierGasAndFlowRate
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
                  const: ada:parameter/laSficpmsTAPP/plasmaMakeUpGasAddition
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laSficpmsTAPP/plasmaMakeUpGasAddition
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
                  const: ada:parameter/laSficpmsTAPP/analysisSequence
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laSficpmsTAPP/analysisSequence
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
                  const: ada:parameter/laSficpmsTAPP/ionCounterDeadTime
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laSficpmsTAPP/ionCounterDeadTime
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
                recoverable from Dwell Time per Mass alone because settling time is
                not captured there. Applies to sequential (quadrupole and single-collector
                sector-field) acquisition."
              type: object
              properties:
                '@id':
                  const: ada:parameter/laSficpmsTAPP/totalIntegrationTimePerOutputDataPoint
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laSficpmsTAPP/totalIntegrationTimePerOutputDataPoint
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
                with laser off or shutter closed) before each ablation event, in seconds.
                For spot and transect analysis, a discrete background interval is
                measured before each ablation. For mapping, background is typically
                measured once per raster line or at the start of a map session rather
                than before each individual pixel. Editable to allow session-specific
                adjustment.
              type: object
              properties:
                '@id':
                  const: ada:parameter/laSficpmsTAPP/backgroundCountTime
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laSficpmsTAPP/backgroundCountTime
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
                  const: ada:parameter/laSficpmsTAPP/numberOfReplicates
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laSficpmsTAPP/numberOfReplicates
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
                  const: ada:parameter/laSficpmsTAPP/transectLength
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laSficpmsTAPP/transectLength
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
                  const: ada:parameter/laSficpmsTAPP/mappingArea
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laSficpmsTAPP/mappingArea
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
                  const: ada:parameter/laSficpmsTAPP/signalIntegrationTime
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laSficpmsTAPP/signalIntegrationTime
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
                  const: ada:parameter/laSficpmsTAPP/proceduralBlankLevel
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laSficpmsTAPP/proceduralBlankLevel
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
              title: Constants and Reference Values Used
              description: Physical constants and reference values used in data reduction
                to calculate the final reported quantity (e.g., decay constants for
                age calculation, standard isotope ratios, or other citable reference
                values used in a correction or calculation), together with their source.
                Distinct from the Group 6 reference-material fields, which document
                accepted values for specific calibration/validation materials rather
                than universal physical constants. Record "None" if no citable, revisable
                physical constants feed into this procedure's data reduction.
              type: object
              properties:
                '@id':
                  const: ada:parameter/laSficpmsTAPP/constantsAndReferenceValuesUsed
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/laSficpmsTAPP/constantsAndReferenceValuesUsed
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
                                                const: ada:parameter/laSficpmsTAPP/torchDepth
                                              '@type':
                                                const:
                                                - schema:PropertyValue
                                              schema:propertyID:
                                                const:
                                                - '@id': ada:parameter/laSficpmsTAPP/torchDepth
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
                                                  const: ada:parameter/laSficpmsTAPP/torchDepth
                                                '@type':
                                                  const:
                                                  - schema:PropertyValue
                                                schema:propertyID:
                                                  const:
                                                  - '@id': ada:parameter/laSficpmsTAPP/torchDepth
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
                                                  const: ada:parameter/laSficpmsTAPP/coolantGasFlowRate
                                                '@type':
                                                  const:
                                                  - schema:PropertyValue
                                                schema:propertyID:
                                                  const:
                                                  - '@id': ada:parameter/laSficpmsTAPP/coolantGasFlowRate
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
                                                  const: ada:parameter/laSficpmsTAPP/auxiliaryGasFlowRate
                                                '@type':
                                                  const:
                                                  - schema:PropertyValue
                                                schema:propertyID:
                                                  const:
                                                  - '@id': ada:parameter/laSficpmsTAPP/auxiliaryGasFlowRate
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
                                                  const: ada:parameter/laSficpmsTAPP/rfPower
                                                '@type':
                                                  const:
                                                  - schema:PropertyValue
                                                schema:propertyID:
                                                  const:
                                                  - '@id': ada:parameter/laSficpmsTAPP/rfPower
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
                                                  const: ada:parameter/laSficpmsTAPP/coolantGasFlowRate
                                                '@type':
                                                  const:
                                                  - schema:PropertyValue
                                                schema:propertyID:
                                                  const:
                                                  - '@id': ada:parameter/laSficpmsTAPP/coolantGasFlowRate
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
                                                  const: ada:parameter/laSficpmsTAPP/auxiliaryGasFlowRate
                                                '@type':
                                                  const:
                                                  - schema:PropertyValue
                                                schema:propertyID:
                                                  const:
                                                  - '@id': ada:parameter/laSficpmsTAPP/auxiliaryGasFlowRate
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
                                                  const: ada:parameter/laSficpmsTAPP/rfPower
                                                '@type':
                                                  const:
                                                  - schema:PropertyValue
                                                schema:propertyID:
                                                  const:
                                                  - '@id': ada:parameter/laSficpmsTAPP/rfPower
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
                                              description: ''
                                              type: object
                                              properties:
                                                '@id':
                                                  const: ada:parameter/laSficpmsTAPP/collisionGasFlowRate
                                                '@type':
                                                  const:
                                                  - schema:PropertyValue
                                                schema:propertyID:
                                                  const:
                                                  - '@id': ada:parameter/laSficpmsTAPP/collisionGasFlowRate
                                                schema:name:
                                                  const: Collision Gas Flow Rate
                                                schema:value:
                                                  type: string
                                              required:
                                              - '@id'
                                              - '@type'
                                              - schema:propertyID
                                              - schema:name
                                              - schema:value
                                            - title: Cell Exit Discrimination Voltage
                                              description: ''
                                              type: object
                                              properties:
                                                '@id':
                                                  const: ada:parameter/laSficpmsTAPP/cellExitDiscriminationVoltage
                                                '@type':
                                                  const:
                                                  - schema:PropertyValue
                                                schema:propertyID:
                                                  const:
                                                  - '@id': ada:parameter/laSficpmsTAPP/cellExitDiscriminationVoltage
                                                schema:name:
                                                  const: Cell Exit Discrimination
                                                    Voltage
                                                schema:value:
                                                  type: string
                                              required:
                                              - '@id'
                                              - '@type'
                                              - schema:propertyID
                                              - schema:name
                                              - schema:value
                                            - title: Reaction Gas Flow Rate
                                              description: ''
                                              type: object
                                              properties:
                                                '@id':
                                                  const: ada:parameter/laSficpmsTAPP/reactionGasFlowRate
                                                '@type':
                                                  const:
                                                  - schema:PropertyValue
                                                schema:propertyID:
                                                  const:
                                                  - '@id': ada:parameter/laSficpmsTAPP/reactionGasFlowRate
                                                schema:name:
                                                  const: Reaction Gas Flow Rate
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
                                              title: Collision Gas Flow Rate
                                              description: ''
                                              type: object
                                              properties:
                                                '@id':
                                                  const: ada:parameter/laSficpmsTAPP/collisionGasFlowRate
                                                '@type':
                                                  const:
                                                  - schema:PropertyValue
                                                schema:propertyID:
                                                  const:
                                                  - '@id': ada:parameter/laSficpmsTAPP/collisionGasFlowRate
                                                schema:name:
                                                  const: Collision Gas Flow Rate
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
                                              title: Cell Exit Discrimination Voltage
                                              description: ''
                                              type: object
                                              properties:
                                                '@id':
                                                  const: ada:parameter/laSficpmsTAPP/cellExitDiscriminationVoltage
                                                '@type':
                                                  const:
                                                  - schema:PropertyValue
                                                schema:propertyID:
                                                  const:
                                                  - '@id': ada:parameter/laSficpmsTAPP/cellExitDiscriminationVoltage
                                                schema:name:
                                                  const: Cell Exit Discrimination
                                                    Voltage
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
                                              title: Reaction Gas Flow Rate
                                              description: ''
                                              type: object
                                              properties:
                                                '@id':
                                                  const: ada:parameter/laSficpmsTAPP/reactionGasFlowRate
                                                '@type':
                                                  const:
                                                  - schema:PropertyValue
                                                schema:propertyID:
                                                  const:
                                                  - '@id': ada:parameter/laSficpmsTAPP/reactionGasFlowRate
                                                schema:name:
                                                  const: Reaction Gas Flow Rate
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
                                          const: ICP Source
                                        schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                                    required:
                                    - schema:additionalType
                              schema:additionalProperty:
                                type: array
                                items:
                                  anyOf:
                                  - title: Mass Resolution Setting
                                    description: Operating mass resolution of the
                                      mass analyser. The analyst selects low, medium,
                                      or high resolution to balance sensitivity against
                                      spectral interference suppression.
                                    type: object
                                    properties:
                                      '@id':
                                        const: ada:parameter/laSficpmsTAPP/massResolutionSetting
                                      '@type':
                                        const:
                                        - schema:PropertyValue
                                      schema:propertyID:
                                        const:
                                        - '@id': ada:parameter/laSficpmsTAPP/massResolutionSetting
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
                                        const: ada:parameter/laSficpmsTAPP/icpTuning
                                      '@type':
                                        const:
                                        - schema:PropertyValue
                                      schema:propertyID:
                                        const:
                                        - '@id': ada:parameter/laSficpmsTAPP/icpTuning
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
                                        const: ada:parameter/laSficpmsTAPP/doublyChargedSpeciesMonitor
                                      '@type':
                                        const:
                                        - schema:PropertyValue
                                      schema:propertyID:
                                        const:
                                        - '@id': ada:parameter/laSficpmsTAPP/doublyChargedSpeciesMonitor
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
                                        const: ada:parameter/laSficpmsTAPP/doublyChargedSpeciesProduction
                                      '@type':
                                        const:
                                        - schema:PropertyValue
                                      schema:propertyID:
                                        const:
                                        - '@id': ada:parameter/laSficpmsTAPP/doublyChargedSpeciesProduction
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
                                        const: ada:parameter/laSficpmsTAPP/memoryEffectMitigation
                                      '@type':
                                        const:
                                        - schema:PropertyValue
                                      schema:propertyID:
                                        const:
                                        - '@id': ada:parameter/laSficpmsTAPP/memoryEffectMitigation
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
                                      mass analyser. The analyst selects low, medium,
                                      or high resolution to balance sensitivity against
                                      spectral interference suppression.
                                    type: object
                                    properties:
                                      '@id':
                                        const: ada:parameter/laSficpmsTAPP/massResolutionSetting
                                      '@type':
                                        const:
                                        - schema:PropertyValue
                                      schema:propertyID:
                                        const:
                                        - '@id': ada:parameter/laSficpmsTAPP/massResolutionSetting
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
                                        const: ada:parameter/laSficpmsTAPP/icpTuning
                                      '@type':
                                        const:
                                        - schema:PropertyValue
                                      schema:propertyID:
                                        const:
                                        - '@id': ada:parameter/laSficpmsTAPP/icpTuning
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
                                        const: ada:parameter/laSficpmsTAPP/doublyChargedSpeciesMonitor
                                      '@type':
                                        const:
                                        - schema:PropertyValue
                                      schema:propertyID:
                                        const:
                                        - '@id': ada:parameter/laSficpmsTAPP/doublyChargedSpeciesMonitor
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
                                        const: ada:parameter/laSficpmsTAPP/doublyChargedSpeciesProduction
                                      '@type':
                                        const:
                                        - schema:PropertyValue
                                      schema:propertyID:
                                        const:
                                        - '@id': ada:parameter/laSficpmsTAPP/doublyChargedSpeciesProduction
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
                                        const: ada:parameter/laSficpmsTAPP/memoryEffectMitigation
                                      '@type':
                                        const:
                                        - schema:PropertyValue
                                      schema:propertyID:
                                        const:
                                        - '@id': ada:parameter/laSficpmsTAPP/memoryEffectMitigation
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
                                      const: ada:parameter/laSficpmsTAPP/laserEnergy
                                    '@type':
                                      const:
                                      - schema:PropertyValue
                                    schema:propertyID:
                                      const:
                                      - '@id': ada:parameter/laSficpmsTAPP/laserEnergy
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
                                        const: ada:parameter/laSficpmsTAPP/laserEnergy
                                      '@type':
                                        const:
                                        - schema:PropertyValue
                                      schema:propertyID:
                                        const:
                                        - '@id': ada:parameter/laSficpmsTAPP/laserEnergy
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
required:
- schema:funding
- ada:spotDiameterMeasured

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS/detail/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS/detail/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS/detail/context.jsonld)

## Sources

* [LA-SF-ICP-MS_TAPP_v16.csv (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/LA-SF-ICPMS/detail`

