
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
      "@id": "ex:laSficpmsTAPP-Zhang2022",
      "schema:identifier": "test value schema:identifier"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA Grants 80NSSC19K1238 (BZ), 80NSSC19K1613 (NLC), 80NSSC18K0595 (MH), NNX17AE77G (AER); NSF Cooperative Agreement DMR-1644779 and State of Florida [Acknowledgements]",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Labelled by specimen within each meteorite: \"Cerro del Inca (museum number USNM 7062), Clark County (USNM 1304-a), Fitzwater Pass (CML 0413-6), Klamath Falls (USNM 7008-a and AMNH 4926-psl), Moonbi (USNM 1457-a), Nelson County (USNM 674-b), Oakley (iron) (USNM 780-d), and St. Genevieve County (USNM 454-a)\", plus a mount of Zinder and a thin section of NWA 1911 (p.4). Individual spots and lines \"are shown in Appendix 4\" (p.6), not in the archived PDF",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": "N — 'a set of five 150 µm spots were analyzed ... on five of the irons, including both slabs of Klamath Falls' (§2.2)",
  "ada:transectLength": -9999,
  "ada:mappingArea": "Raster over \"a few millimeters\" of polished iron slab surface (area not precisely stated)",
  "ada:signalIntegrationTime": "N — the Ge spots were ablated for 20 s (§2.2)",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially — the rule stated is one of combination rather than rejection: for Ge, Sb, Re, Os and Ir the reported value is \"calculated from the mean of the spot average (Appendix 2) and the raster average in this table\" (Table 3 note, p.4). No acceptance or rejection rule for individual results is stated. The exclusion of \"Binya and Fitzwater Pass ... from the fractional-crystallization modeling of group IIIF\" (p.5) is an interpretive exclusion downstream of the reported values, not a rule about which results make them",
  "ada:combinedResults": "raster averages for seven IIIF irons and two pallasites; spot averages — Table 3; Appendix 2",
  "ada:detectionLimit": "N — 'Concentrations below detection limits are not shown' (Table 3); the limits are not given",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "N — compared with NAA on the same irons rather than a standard: differences 'mostly ... within the range of ±40%', within ±10% for Ni, Co and Ga, up to 30% for Au and As, and W in Cerro del Inca 4.39 ng/g by LA-ICP-MS against 1.06 ng/g by INAA (§2.3)",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laSficpmsTAPP/preAnalysisImagingAndScreening",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsTAPP/preAnalysisImagingAndScreening"
        }
      ],
      "schema:name": "Pre-Analysis Imaging and Screening",
      "schema:value": "Electron-microprobe mapping, for the pallasites only — \"Quantitative analysis, mixed WDS/EDS element mapping, and characterization of the mineral phases from NWA 1911 and Zinder were performed\" on the Bruker instrument, producing Si, Al, Cr, Fe, Mg, Ca, Na, P and Ni maps \"along with backscattered electron (BSE) maps\" at 6 μm per pixel (pp.5–6); for the irons the paper states only that the rasters were \"taken on polished surfaces\" (p.5)"
    },
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
      "schema:value": "raster: 10 µm/s; Ge spots: N/A — 'scanned at 10 µm/s' (§2.2)"
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
      "@id": "ex:laSficpmsTAPP-Zhang2022",
      "schema:identifier": "test value schema:identifier"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA Grants 80NSSC19K1238 (BZ), 80NSSC19K1613 (NLC), 80NSSC18K0595 (MH), NNX17AE77G (AER); NSF Cooperative Agreement DMR-1644779 and State of Florida [Acknowledgements]",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Labelled by specimen within each meteorite: \"Cerro del Inca (museum number USNM 7062), Clark County (USNM 1304-a), Fitzwater Pass (CML 0413-6), Klamath Falls (USNM 7008-a and AMNH 4926-psl), Moonbi (USNM 1457-a), Nelson County (USNM 674-b), Oakley (iron) (USNM 780-d), and St. Genevieve County (USNM 454-a)\", plus a mount of Zinder and a thin section of NWA 1911 (p.4). Individual spots and lines \"are shown in Appendix 4\" (p.6), not in the archived PDF",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": "N \u2014 'a set of five 150 \u00b5m spots were analyzed ... on five of the irons, including both slabs of Klamath Falls' (\u00a72.2)",
  "ada:transectLength": -9999,
  "ada:mappingArea": "Raster over \"a few millimeters\" of polished iron slab surface (area not precisely stated)",
  "ada:signalIntegrationTime": "N \u2014 the Ge spots were ablated for 20 s (\u00a72.2)",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially \u2014 the rule stated is one of combination rather than rejection: for Ge, Sb, Re, Os and Ir the reported value is \"calculated from the mean of the spot average (Appendix 2) and the raster average in this table\" (Table 3 note, p.4). No acceptance or rejection rule for individual results is stated. The exclusion of \"Binya and Fitzwater Pass ... from the fractional-crystallization modeling of group IIIF\" (p.5) is an interpretive exclusion downstream of the reported values, not a rule about which results make them",
  "ada:combinedResults": "raster averages for seven IIIF irons and two pallasites; spot averages \u2014 Table 3; Appendix 2",
  "ada:detectionLimit": "N \u2014 'Concentrations below detection limits are not shown' (Table 3); the limits are not given",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "N \u2014 compared with NAA on the same irons rather than a standard: differences 'mostly ... within the range of \u00b140%', within \u00b110% for Ni, Co and Ga, up to 30% for Au and As, and W in Cerro del Inca 4.39 ng/g by LA-ICP-MS against 1.06 ng/g by INAA (\u00a72.3)",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laSficpmsTAPP/preAnalysisImagingAndScreening",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsTAPP/preAnalysisImagingAndScreening"
        }
      ],
      "schema:name": "Pre-Analysis Imaging and Screening",
      "schema:value": "Electron-microprobe mapping, for the pallasites only \u2014 \"Quantitative analysis, mixed WDS/EDS element mapping, and characterization of the mineral phases from NWA 1911 and Zinder were performed\" on the Bruker instrument, producing Si, Al, Cr, Fe, Mg, Ca, Na, P and Ni maps \"along with backscattered electron (BSE) maps\" at 6 \u03bcm per pixel (pp.5\u20136); for the irons the paper states only that the rasters were \"taken on polished surfaces\" (p.5)"
    },
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
      "schema:value": "raster: 10 \u00b5m/s; Ge spots: N/A \u2014 'scanned at 10 \u00b5m/s' (\u00a72.2)"
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

<ex:detail-Zhang2022> a ada:LAICPMSTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/preAnalysisImagingAndScreening>,
        <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize> ;
    schema1:measurementTechnique <ex:laSficpmsTAPP-Zhang2022> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially — the rule stated is one of combination rather than rejection: for Ge, Sb, Re, Os and Ir the reported value is \"calculated from the mean of the spot average (Appendix 2) and the raster average in this table\" (Table 3 note, p.4). No acceptance or rejection rule for individual results is stated. The exclusion of \"Binya and Fitzwater Pass ... from the fractional-crystallization modeling of group IIIF\" (p.5) is an interpretive exclusion downstream of the reported values, not a rule about which results make them" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "N — compared with NAA on the same irons rather than a standard: differences 'mostly ... within the range of ±40%', within ±10% for Ni, Co and Ga, up to 30% for Au and As, and W in Cerro del Inca 4.39 ng/g by LA-ICP-MS against 1.06 ng/g by INAA (§2.3)" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:combinedResults "raster averages for seven IIIF irons and two pallasites; spot averages — Table 3; Appendix 2" ;
    ada:componentType "ada:LAICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "N — 'Concentrations below detection limits are not shown' (Table 3); the limits are not given" ;
    ada:fundingSourceForAnalysis "NASA Grants 80NSSC19K1238 (BZ), 80NSSC19K1613 (NLC), 80NSSC18K0595 (MH), NNX17AE77G (AER); NSF Cooperative Agreement DMR-1644779 and State of Florida [Acknowledgements]" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "Raster over \"a few millimeters\" of polished iron slab surface (area not precisely stated)" ;
    ada:numberOfReplicates "N — 'a set of five 150 µm spots were analyzed ... on five of the irons, including both slabs of Klamath Falls' (§2.2)" ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Labelled by specimen within each meteorite: \"Cerro del Inca (museum number USNM 7062), Clark County (USNM 1304-a), Fitzwater Pass (CML 0413-6), Klamath Falls (USNM 7008-a and AMNH 4926-psl), Moonbi (USNM 1457-a), Nelson County (USNM 674-b), Oakley (iron) (USNM 780-d), and St. Genevieve County (USNM 454-a)\", plus a mount of Zinder and a thin section of NWA 1911 (p.4). Individual spots and lines \"are shown in Appendix 4\" (p.6), not in the archived PDF" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime "N — the Ge spots were ablated for 20 s (§2.2)" ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<ex:laSficpmsTAPP-Zhang2022> schema1:identifier "test value schema:identifier" .

<https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/preAnalysisImagingAndScreening> ;
    schema1:value "Electron-microprobe mapping, for the pallasites only — \"Quantitative analysis, mixed WDS/EDS element mapping, and characterization of the mineral phases from NWA 1911 and Zinder were performed\" on the Bruker instrument, producing Si, Al, Cr, Fe, Mg, Ca, Na, P and Ni maps \"along with backscattered electron (BSE) maps\" at 6 μm per pixel (pp.5–6); for the irons the paper states only that the rasters were \"taken on polished surfaces\" (p.5)" .

<https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize> a schema1:PropertyValue ;
    schema1:name "Transect Rate, Mapping Rate or Step Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize> ;
    schema1:value "raster: 10 µm/s; Ge spots: N/A — 'scanned at 10 µm/s' (§2.2)" .


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
      "@id": "ex:laSficpmsTAPP-Chernonozhkin2021",
      "schema:identifier": "test value schema:identifier"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only — \"Springwater, ... Brenham, Brahin and Seymchan, and ... Imilac, Cumulus Peak 04071, Esquel and Fukang\" (p.2); maps and line scans are not given labels of their own in the paper",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "Each map: 1450×600 µm = 870,000 µm²; total of 8 PMG olivines mapped",
  "ada:signalIntegrationTime": "N/A — mapping",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "N — whole results are dropped, but on signal grounds: \"where significant spikes in individual transient LA-ICP-MS signals were observed (e.g. Ca in CMS 04071 and Seymchan and Ni in Brahin and Seymchan), results were not included in Table 1\" (p.6). By basis that belongs to Spike / Outlier Filtering Approach; no result-based selection rule is stated. For the maps, \"The P-rich veinlets were excluded from the maps prior to the calculation of the correlation coefficients\" (appendix C), which masks pixels within a result rather than admitting or excluding results",
  "ada:combinedResults": "'pure' olivine averages from the maps (for example Seymchan and Fukang)",
  "ada:detectionLimit": "all: per-pixel LODs, averaged over the map — Table E1 (Na = 1, Nb = 10), App. C5",
  "ada:limitOfQuantificationMethod": "all: as the LOD, with 10 SD instead of 3 SD — App. C5",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laSficpmsTAPP/preAnalysisImagingAndScreening",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsTAPP/preAnalysisImagingAndScreening"
        }
      ],
      "schema:name": "Pre-Analysis Imaging and Screening",
      "schema:value": "μXRF mapping of larger sections, on which the ablation is sited — Fe Kα intensity maps identify the mineral phases \"based on the intensities of the Kα lines of the constituent major elements (Fe, Mg, Ni, Cr, S, Ca and P)\", and the LA-ICP-MS areas correspond \"to the locations indicated on the larger μXRF maps as black rectangles\" (p.4). The instrument is a Bruker M4 Tornado with a Rh-anode source at 50 kV and 150 μA, focused to \"a 25 μm spot (measured for Mo Kα)\" (p.3)"
    },
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
      "schema:value": "all: 9 µm/s — translation speed (§2.2.2)"
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
      "@id": "ex:laSficpmsTAPP-Chernonozhkin2021",
      "schema:identifier": "test value schema:identifier"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only \u2014 \"Springwater, ... Brenham, Brahin and Seymchan, and ... Imilac, Cumulus Peak 04071, Esquel and Fukang\" (p.2); maps and line scans are not given labels of their own in the paper",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "Each map: 1450\u00d7600 \u00b5m = 870,000 \u00b5m\u00b2; total of 8 PMG olivines mapped",
  "ada:signalIntegrationTime": "N/A \u2014 mapping",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 whole results are dropped, but on signal grounds: \"where significant spikes in individual transient LA-ICP-MS signals were observed (e.g. Ca in CMS 04071 and Seymchan and Ni in Brahin and Seymchan), results were not included in Table 1\" (p.6). By basis that belongs to Spike / Outlier Filtering Approach; no result-based selection rule is stated. For the maps, \"The P-rich veinlets were excluded from the maps prior to the calculation of the correlation coefficients\" (appendix C), which masks pixels within a result rather than admitting or excluding results",
  "ada:combinedResults": "'pure' olivine averages from the maps (for example Seymchan and Fukang)",
  "ada:detectionLimit": "all: per-pixel LODs, averaged over the map \u2014 Table E1 (Na = 1, Nb = 10), App. C5",
  "ada:limitOfQuantificationMethod": "all: as the LOD, with 10 SD instead of 3 SD \u2014 App. C5",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laSficpmsTAPP/preAnalysisImagingAndScreening",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsTAPP/preAnalysisImagingAndScreening"
        }
      ],
      "schema:name": "Pre-Analysis Imaging and Screening",
      "schema:value": "\u03bcXRF mapping of larger sections, on which the ablation is sited \u2014 Fe K\u03b1 intensity maps identify the mineral phases \"based on the intensities of the K\u03b1 lines of the constituent major elements (Fe, Mg, Ni, Cr, S, Ca and P)\", and the LA-ICP-MS areas correspond \"to the locations indicated on the larger \u03bcXRF maps as black rectangles\" (p.4). The instrument is a Bruker M4 Tornado with a Rh-anode source at 50 kV and 150 \u03bcA, focused to \"a 25 \u03bcm spot (measured for Mo K\u03b1)\" (p.3)"
    },
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
      "schema:value": "all: 9 \u00b5m/s \u2014 translation speed (\u00a72.2.2)"
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

<ex:detail-Chernonozhkin2021> a ada:LAICPMSTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/preAnalysisImagingAndScreening>,
        <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize> ;
    schema1:measurementTechnique <ex:laSficpmsTAPP-Chernonozhkin2021> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — whole results are dropped, but on signal grounds: \"where significant spikes in individual transient LA-ICP-MS signals were observed (e.g. Ca in CMS 04071 and Seymchan and Ni in Brahin and Seymchan), results were not included in Table 1\" (p.6). By basis that belongs to Spike / Outlier Filtering Approach; no result-based selection rule is stated. For the maps, \"The P-rich veinlets were excluded from the maps prior to the calculation of the correlation coefficients\" (appendix C), which masks pixels within a result rather than admitting or excluding results" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "missing" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:combinedResults "'pure' olivine averages from the maps (for example Seymchan and Fukang)" ;
    ada:componentType "ada:LAICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "all: per-pixel LODs, averaged over the map — Table E1 (Na = 1, Nb = 10), App. C5" ;
    ada:fundingSourceForAnalysis "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "all: as the LOD, with 10 SD instead of 3 SD — App. C5" ;
    ada:mappingArea "Each map: 1450×600 µm = 870,000 µm²; total of 8 PMG olivines mapped" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Sample name only — \"Springwater, ... Brenham, Brahin and Seymchan, and ... Imilac, Cumulus Peak 04071, Esquel and Fukang\" (p.2); maps and line scans are not given labels of their own in the paper" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime "N/A — mapping" ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<ex:laSficpmsTAPP-Chernonozhkin2021> schema1:identifier "test value schema:identifier" .

<https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/preAnalysisImagingAndScreening> ;
    schema1:value "μXRF mapping of larger sections, on which the ablation is sited — Fe Kα intensity maps identify the mineral phases \"based on the intensities of the Kα lines of the constituent major elements (Fe, Mg, Ni, Cr, S, Ca and P)\", and the LA-ICP-MS areas correspond \"to the locations indicated on the larger μXRF maps as black rectangles\" (p.4). The instrument is a Bruker M4 Tornado with a Rh-anode source at 50 kV and 150 μA, focused to \"a 25 μm spot (measured for Mo Kα)\" (p.3)" .

<https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize> a schema1:PropertyValue ;
    schema1:name "Transect Rate, Mapping Rate or Step Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize> ;
    schema1:value "all: 9 µm/s — translation speed (§2.2.2)" .


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
      "@id": "ex:laSficpmsTAPP-Chernonozhkin2021-2",
      "schema:identifier": "test value schema:identifier"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only — \"Springwater, ... Brenham, Brahin and Seymchan, and ... Imilac, Cumulus Peak 04071, Esquel and Fukang\" (p.2); maps and line scans are not given labels of their own in the paper",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": 3,
  "ada:transectLength": "Line scan length: 400 µm (runs 1 and 2; 34 runs adjusted to measure 400 µm line + blank + washout)",
  "ada:mappingArea": "N/A — line scan + spot; not 2D raster",
  "ada:signalIntegrationTime": "N — 50 s of sample ablation per line (Table B1); the integration window is not stated",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "N — whole results are dropped, but on signal grounds: \"where significant spikes in individual transient LA-ICP-MS signals were observed (e.g. Ca in CMS 04071 and Seymchan and Ni in Brahin and Seymchan), results were not included in Table 1\" (p.6). By basis that belongs to Spike / Outlier Filtering Approach; no result-based selection rule is stated",
  "ada:combinedResults": "each main-group pallasite olivine in Table 1 (3 replicates each)",
  "ada:detectionLimit": "Cu: 0.28 ng/g; Cs: 4.9 ng/g; Ba: 16 ng/g; W: 5.4 ng/g; Re: 0.42 ng/g; Ir: 0.95 ng/g; Pt: 0.73 ng/g; Au: 1.8 ng/g; Nb: 0.61 ng/g; other: Table 1 — stated in §3.3; LODs averaged over analyses (Na = 24, Nb = 5). §3.3 also gives 33 ng/g for Sr, which is not among the measured nuclides",
  "ada:limitOfQuantificationMethod": "all: as the LOD, with 10 SD instead of 3 SD — App. C5",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "all: 1 standard deviation — Table 1: 'the uncertainty corresponds to 1 standard deviation'",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laSficpmsTAPP/preAnalysisImagingAndScreening",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsTAPP/preAnalysisImagingAndScreening"
        }
      ],
      "schema:name": "Pre-Analysis Imaging and Screening",
      "schema:value": "μXRF mapping of larger sections, on which the ablation is sited — Fe Kα intensity maps identify the mineral phases \"based on the intensities of the Kα lines of the constituent major elements (Fe, Mg, Ni, Cr, S, Ca and P)\", and the LA-ICP-MS areas correspond \"to the locations indicated on the larger μXRF maps as black rectangles\" (p.4). The instrument is a Bruker M4 Tornado with a Rh-anode source at 50 kV and 150 μA, focused to \"a 25 μm spot (measured for Mo Kα)\" (p.3)"
    },
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
      "schema:value": "run 1: 10 µm/s; run 2: 10 µm/s"
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
      "@id": "ex:laSficpmsTAPP-Chernonozhkin2021-2",
      "schema:identifier": "test value schema:identifier"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only \u2014 \"Springwater, ... Brenham, Brahin and Seymchan, and ... Imilac, Cumulus Peak 04071, Esquel and Fukang\" (p.2); maps and line scans are not given labels of their own in the paper",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": 3,
  "ada:transectLength": "Line scan length: 400 \u00b5m (runs 1 and 2; 34 runs adjusted to measure 400 \u00b5m line + blank + washout)",
  "ada:mappingArea": "N/A \u2014 line scan + spot; not 2D raster",
  "ada:signalIntegrationTime": "N \u2014 50 s of sample ablation per line (Table B1); the integration window is not stated",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 whole results are dropped, but on signal grounds: \"where significant spikes in individual transient LA-ICP-MS signals were observed (e.g. Ca in CMS 04071 and Seymchan and Ni in Brahin and Seymchan), results were not included in Table 1\" (p.6). By basis that belongs to Spike / Outlier Filtering Approach; no result-based selection rule is stated",
  "ada:combinedResults": "each main-group pallasite olivine in Table 1 (3 replicates each)",
  "ada:detectionLimit": "Cu: 0.28 ng/g; Cs: 4.9 ng/g; Ba: 16 ng/g; W: 5.4 ng/g; Re: 0.42 ng/g; Ir: 0.95 ng/g; Pt: 0.73 ng/g; Au: 1.8 ng/g; Nb: 0.61 ng/g; other: Table 1 \u2014 stated in \u00a73.3; LODs averaged over analyses (Na = 24, Nb = 5). \u00a73.3 also gives 33 ng/g for Sr, which is not among the measured nuclides",
  "ada:limitOfQuantificationMethod": "all: as the LOD, with 10 SD instead of 3 SD \u2014 App. C5",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "all: 1 standard deviation \u2014 Table 1: 'the uncertainty corresponds to 1 standard deviation'",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laSficpmsTAPP/preAnalysisImagingAndScreening",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsTAPP/preAnalysisImagingAndScreening"
        }
      ],
      "schema:name": "Pre-Analysis Imaging and Screening",
      "schema:value": "\u03bcXRF mapping of larger sections, on which the ablation is sited \u2014 Fe K\u03b1 intensity maps identify the mineral phases \"based on the intensities of the K\u03b1 lines of the constituent major elements (Fe, Mg, Ni, Cr, S, Ca and P)\", and the LA-ICP-MS areas correspond \"to the locations indicated on the larger \u03bcXRF maps as black rectangles\" (p.4). The instrument is a Bruker M4 Tornado with a Rh-anode source at 50 kV and 150 \u03bcA, focused to \"a 25 \u03bcm spot (measured for Mo K\u03b1)\" (p.3)"
    },
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
      "schema:value": "run 1: 10 \u00b5m/s; run 2: 10 \u00b5m/s"
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

<ex:detail-Chernonozhkin2021-2> a ada:LAICPMSTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/preAnalysisImagingAndScreening>,
        <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize> ;
    schema1:measurementTechnique <ex:laSficpmsTAPP-Chernonozhkin2021-2> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — whole results are dropped, but on signal grounds: \"where significant spikes in individual transient LA-ICP-MS signals were observed (e.g. Ca in CMS 04071 and Seymchan and Ni in Brahin and Seymchan), results were not included in Table 1\" (p.6). By basis that belongs to Spike / Outlier Filtering Approach; no result-based selection rule is stated" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "missing" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:combinedResults "each main-group pallasite olivine in Table 1 (3 replicates each)" ;
    ada:componentType "ada:LAICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "Cu: 0.28 ng/g; Cs: 4.9 ng/g; Ba: 16 ng/g; W: 5.4 ng/g; Re: 0.42 ng/g; Ir: 0.95 ng/g; Pt: 0.73 ng/g; Au: 1.8 ng/g; Nb: 0.61 ng/g; other: Table 1 — stated in §3.3; LODs averaged over analyses (Na = 24, Nb = 5). §3.3 also gives 33 ng/g for Sr, which is not among the measured nuclides" ;
    ada:fundingSourceForAnalysis "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent" ;
    ada:goodnessOfFitOrDispersionStatistic "all: 1 standard deviation — Table 1: 'the uncertainty corresponds to 1 standard deviation'" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "all: as the LOD, with 10 SD instead of 3 SD — App. C5" ;
    ada:mappingArea "N/A — line scan + spot; not 2D raster" ;
    ada:numberOfReplicates 3 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Sample name only — \"Springwater, ... Brenham, Brahin and Seymchan, and ... Imilac, Cumulus Peak 04071, Esquel and Fukang\" (p.2); maps and line scans are not given labels of their own in the paper" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime "N — 50 s of sample ablation per line (Table B1); the integration window is not stated" ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength "Line scan length: 400 µm (runs 1 and 2; 34 runs adjusted to measure 400 µm line + blank + washout)" ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<ex:laSficpmsTAPP-Chernonozhkin2021-2> schema1:identifier "test value schema:identifier" .

<https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/preAnalysisImagingAndScreening> ;
    schema1:value "μXRF mapping of larger sections, on which the ablation is sited — Fe Kα intensity maps identify the mineral phases \"based on the intensities of the Kα lines of the constituent major elements (Fe, Mg, Ni, Cr, S, Ca and P)\", and the LA-ICP-MS areas correspond \"to the locations indicated on the larger μXRF maps as black rectangles\" (p.4). The instrument is a Bruker M4 Tornado with a Rh-anode source at 50 kV and 150 μA, focused to \"a 25 μm spot (measured for Mo Kα)\" (p.3)" .

<https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize> a schema1:PropertyValue ;
    schema1:name "Transect Rate, Mapping Rate or Step Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize> ;
    schema1:value "run 1: 10 µm/s; run 2: 10 µm/s" .


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
      "@id": "ex:laSficpmsTAPP-Chernonozhkin2021-3",
      "schema:identifier": "test value schema:identifier"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Labelled: phosphate grains per pallasite, \"Ph1\", \"Ph2\", \"Ph3\", \"Ph4\" with mineral (\"stanf\", \"merr\"), and each \"single parallel measurement\" numbered (Table 2, p.10) — for Brahin, CMS 04071, Esquel and Seymchan",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": "N — Table 2 lists each 'single parallel measurement' per grain; 'Parallel analyses of single phosphate grains are highly reproducible' (§3.4)",
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": "N — 20 s of spot ablation (§2.2.4)",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "N — whole results are dropped, but on signal grounds: \"where significant spikes in individual transient LA-ICP-MS signals were observed (e.g. Ca in CMS 04071 and Seymchan and Ni in Brahin and Seymchan), results were not included in Table 1\" (p.6). By basis that belongs to Spike / Outlier Filtering Approach; no result-based selection rule is stated",
  "ada:combinedResults": "missing",
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
      "@id": "ada:parameter/laSficpmsTAPP/preAnalysisImagingAndScreening",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsTAPP/preAnalysisImagingAndScreening"
        }
      ],
      "schema:name": "Pre-Analysis Imaging and Screening",
      "schema:value": "μXRF mapping of larger sections, on which the ablation is sited — Fe Kα intensity maps identify the mineral phases \"based on the intensities of the Kα lines of the constituent major elements (Fe, Mg, Ni, Cr, S, Ca and P)\", and the LA-ICP-MS areas correspond \"to the locations indicated on the larger μXRF maps as black rectangles\" (p.4). The instrument is a Bruker M4 Tornado with a Rh-anode source at 50 kV and 150 μA, focused to \"a 25 μm spot (measured for Mo Kα)\" (p.3)"
    },
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
      "@id": "ex:laSficpmsTAPP-Chernonozhkin2021-3",
      "schema:identifier": "test value schema:identifier"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Labelled: phosphate grains per pallasite, \"Ph1\", \"Ph2\", \"Ph3\", \"Ph4\" with mineral (\"stanf\", \"merr\"), and each \"single parallel measurement\" numbered (Table 2, p.10) \u2014 for Brahin, CMS 04071, Esquel and Seymchan",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": "N \u2014 Table 2 lists each 'single parallel measurement' per grain; 'Parallel analyses of single phosphate grains are highly reproducible' (\u00a73.4)",
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": "N \u2014 20 s of spot ablation (\u00a72.2.4)",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 whole results are dropped, but on signal grounds: \"where significant spikes in individual transient LA-ICP-MS signals were observed (e.g. Ca in CMS 04071 and Seymchan and Ni in Brahin and Seymchan), results were not included in Table 1\" (p.6). By basis that belongs to Spike / Outlier Filtering Approach; no result-based selection rule is stated",
  "ada:combinedResults": "missing",
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
      "@id": "ada:parameter/laSficpmsTAPP/preAnalysisImagingAndScreening",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsTAPP/preAnalysisImagingAndScreening"
        }
      ],
      "schema:name": "Pre-Analysis Imaging and Screening",
      "schema:value": "\u03bcXRF mapping of larger sections, on which the ablation is sited \u2014 Fe K\u03b1 intensity maps identify the mineral phases \"based on the intensities of the K\u03b1 lines of the constituent major elements (Fe, Mg, Ni, Cr, S, Ca and P)\", and the LA-ICP-MS areas correspond \"to the locations indicated on the larger \u03bcXRF maps as black rectangles\" (p.4). The instrument is a Bruker M4 Tornado with a Rh-anode source at 50 kV and 150 \u03bcA, focused to \"a 25 \u03bcm spot (measured for Mo K\u03b1)\" (p.3)"
    },
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

<ex:detail-Chernonozhkin2021-3> a ada:LAICPMSTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/preAnalysisImagingAndScreening>,
        <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize> ;
    schema1:measurementTechnique <ex:laSficpmsTAPP-Chernonozhkin2021-3> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — whole results are dropped, but on signal grounds: \"where significant spikes in individual transient LA-ICP-MS signals were observed (e.g. Ca in CMS 04071 and Seymchan and Ni in Brahin and Seymchan), results were not included in Table 1\" (p.6). By basis that belongs to Spike / Outlier Filtering Approach; no result-based selection rule is stated" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "missing" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:combinedResults "missing" ;
    ada:componentType "ada:LAICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:fundingSourceForAnalysis "Planet Topers (BELSPO); FWO; Alexander von Humboldt Foundation; FWO/BOF-UGent" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "missing" ;
    ada:numberOfReplicates "N — Table 2 lists each 'single parallel measurement' per grain; 'Parallel analyses of single phosphate grains are highly reproducible' (§3.4)" ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Labelled: phosphate grains per pallasite, \"Ph1\", \"Ph2\", \"Ph3\", \"Ph4\" with mineral (\"stanf\", \"merr\"), and each \"single parallel measurement\" numbered (Table 2, p.10) — for Brahin, CMS 04071, Esquel and Seymchan" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime "N — 20 s of spot ablation (§2.2.4)" ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<ex:laSficpmsTAPP-Chernonozhkin2021-3> schema1:identifier "test value schema:identifier" .

<https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/preAnalysisImagingAndScreening> ;
    schema1:value "μXRF mapping of larger sections, on which the ablation is sited — Fe Kα intensity maps identify the mineral phases \"based on the intensities of the Kα lines of the constituent major elements (Fe, Mg, Ni, Cr, S, Ca and P)\", and the LA-ICP-MS areas correspond \"to the locations indicated on the larger μXRF maps as black rectangles\" (p.4). The instrument is a Bruker M4 Tornado with a Rh-anode source at 50 kV and 150 μA, focused to \"a 25 μm spot (measured for Mo Kα)\" (p.3)" .

<https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize> a schema1:PropertyValue ;
    schema1:name "Transect Rate, Mapping Rate or Step Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize> ;
    schema1:value "N/A — spot mode" .


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
      "@id": "ex:laSficpmsTAPP-Mittlefehldt2024",
      "schema:identifier": "test value schema:identifier"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "N — no funding section in this appendix document; funding would be in the parent paper which was not assessed",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Labelled: samples within each pallasite, e.g. \"Ac-1\", \"Ad-1\", \"Ah-1\", \"Ah-2\", \"Ah-3\", \"Al-1\", \"Br-1\" (Table S1, p.14); laser spots carry labels such as \"laser spot 059-Pa-1\" (p.8)",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": "N — variable number of spots per sample",
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": "N — parameters lost",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially — the reported values are averages per meteorite (Table E4 of the data file), with the complete set of analyses also released (p.6); trace-element chromatograms were \"scrutinized for unanticipated interferences, improperly chosen backgrounds or other problems\" (p.5). No acceptance or rejection rule is stated for the LA data. The paper's detailed filters — analysis sums 100 ± 2%, stoichiometry limits, Grubb's test rejecting at p<0.01 and tagging at p<0.05, an FeO ceiling of 17.5 wt% for Phillips County, and a zoning profile excluded from that mean — are stated for the EMPA data (p.3) and are not borrowed here",
  "ada:combinedResults": "per-split averages (Table L2); per-meteorite weighted means (Table L3)",
  "ada:detectionLimit": "N — LODs not stated; concentrations reported for all nuclides above background",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "N — the ~0.6% precision on Fe/Mn is for the EMPA (§3.1)",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "N — within-session precision not formally assessed",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "N — LA-ICP-MS Sc agrees with INAA 'with scatter of roughly ±0.5 µg/g'; Cr scatters more (§6.1)",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laSficpmsTAPP/preAnalysisImagingAndScreening",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsTAPP/preAnalysisImagingAndScreening"
        }
      ],
      "schema:name": "Pre-Analysis Imaging and Screening",
      "schema:value": "SEM imaging of the grain mounts, used to place the spots — \"The grains were first imaged using a scanning electron microscope (SEM) to locate regions for analysis. Regions containing surface inclusions were avoided for analysis\" (p.5); the grains are the same mounts already used for EMPA (p.5)"
    },
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
      "@id": "ex:laSficpmsTAPP-Mittlefehldt2024",
      "schema:identifier": "test value schema:identifier"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "N \u2014 no funding section in this appendix document; funding would be in the parent paper which was not assessed",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Labelled: samples within each pallasite, e.g. \"Ac-1\", \"Ad-1\", \"Ah-1\", \"Ah-2\", \"Ah-3\", \"Al-1\", \"Br-1\" (Table S1, p.14); laser spots carry labels such as \"laser spot 059-Pa-1\" (p.8)",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": "N \u2014 variable number of spots per sample",
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": "N \u2014 parameters lost",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially \u2014 the reported values are averages per meteorite (Table E4 of the data file), with the complete set of analyses also released (p.6); trace-element chromatograms were \"scrutinized for unanticipated interferences, improperly chosen backgrounds or other problems\" (p.5). No acceptance or rejection rule is stated for the LA data. The paper's detailed filters \u2014 analysis sums 100 \u00b1 2%, stoichiometry limits, Grubb's test rejecting at p<0.01 and tagging at p<0.05, an FeO ceiling of 17.5 wt% for Phillips County, and a zoning profile excluded from that mean \u2014 are stated for the EMPA data (p.3) and are not borrowed here",
  "ada:combinedResults": "per-split averages (Table L2); per-meteorite weighted means (Table L3)",
  "ada:detectionLimit": "N \u2014 LODs not stated; concentrations reported for all nuclides above background",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "N \u2014 the ~0.6% precision on Fe/Mn is for the EMPA (\u00a73.1)",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "N \u2014 within-session precision not formally assessed",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "N \u2014 LA-ICP-MS Sc agrees with INAA 'with scatter of roughly \u00b10.5 \u00b5g/g'; Cr scatters more (\u00a76.1)",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laSficpmsTAPP/preAnalysisImagingAndScreening",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsTAPP/preAnalysisImagingAndScreening"
        }
      ],
      "schema:name": "Pre-Analysis Imaging and Screening",
      "schema:value": "SEM imaging of the grain mounts, used to place the spots \u2014 \"The grains were first imaged using a scanning electron microscope (SEM) to locate regions for analysis. Regions containing surface inclusions were avoided for analysis\" (p.5); the grains are the same mounts already used for EMPA (p.5)"
    },
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

<ex:detail-Mittlefehldt2024> a ada:LAICPMSTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/preAnalysisImagingAndScreening>,
        <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize> ;
    schema1:measurementTechnique <ex:laSficpmsTAPP-Mittlefehldt2024> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially — the reported values are averages per meteorite (Table E4 of the data file), with the complete set of analyses also released (p.6); trace-element chromatograms were \"scrutinized for unanticipated interferences, improperly chosen backgrounds or other problems\" (p.5). No acceptance or rejection rule is stated for the LA data. The paper's detailed filters — analysis sums 100 ± 2%, stoichiometry limits, Grubb's test rejecting at p<0.01 and tagging at p<0.05, an FeO ceiling of 17.5 wt% for Phillips County, and a zoning profile excluded from that mean — are stated for the EMPA data (p.3) and are not borrowed here" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "N — LA-ICP-MS Sc agrees with INAA 'with scatter of roughly ±0.5 µg/g'; Cr scatters more (§6.1)" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:combinedResults "per-split averages (Table L2); per-meteorite weighted means (Table L3)" ;
    ada:componentType "ada:LAICPMSTabular" ;
    ada:countingStatisticsError "N — the ~0.6% precision on Fe/Mn is for the EMPA (§3.1)" ;
    ada:detectionLimit "N — LODs not stated; concentrations reported for all nuclides above background" ;
    ada:fundingSourceForAnalysis "N — no funding section in this appendix document; funding would be in the parent paper which was not assessed" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "missing" ;
    ada:numberOfReplicates "N — variable number of spots per sample" ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Labelled: samples within each pallasite, e.g. \"Ac-1\", \"Ad-1\", \"Ah-1\", \"Ah-2\", \"Ah-3\", \"Al-1\", \"Br-1\" (Table S1, p.14); laser spots carry labels such as \"laser spot 059-Pa-1\" (p.8)" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime "N — parameters lost" ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "N — within-session precision not formally assessed" .

<ex:laSficpmsTAPP-Mittlefehldt2024> schema1:identifier "test value schema:identifier" .

<https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/preAnalysisImagingAndScreening> ;
    schema1:value "SEM imaging of the grain mounts, used to place the spots — \"The grains were first imaged using a scanning electron microscope (SEM) to locate regions for analysis. Regions containing surface inclusions were avoided for analysis\" (p.5); the grains are the same mounts already used for EMPA (p.5)" .

<https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize> a schema1:PropertyValue ;
    schema1:name "Transect Rate, Mapping Rate or Step Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize> ;
    schema1:value "N/A — spot mode" .


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
      "@id": "ex:laSficpmsTAPP-Navarro2024",
      "schema:identifier": "test value schema:identifier"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "M.S.N.: Educorp (Unicamp) and International Association of Geoanalysts for Geoanalysis 2022 presentation; J.E.: CNPq grant 316191/2021-3",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only — iron meteorites by name (Table 1, p.2), each analysed as \"fragments about 1 cm\" (p.3); spots and mapped areas are counted (\"points 176\", p.12), not labelled",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": 20,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": 40,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially — contributing counts are stated ('n: number of replicates'; 'the mean value of 20 spot measurements in the Arraias meteorite'); no acceptance or rejection rule is stated",
  "ada:combinedResults": "per-meteorite averages (Table 3 and the data table for Figs 2 and 3), for example Arraias (20 spots)",
  "ada:detectionLimit": "As: 2; Au: 0.1; Co: 2; Cr: 19; Cu: 0.8; Fe: 60; Ga: 0.3; Ge: 3; Ir: 0.2; Ni: 36; Os: 0.2; Pd: 0.5; Pt: 0.3; Re: 0.1; Rh: 0.1; Ru: 1; W: 1 — µg/g, median values (Table 3 'LOD')",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "N — precision is stated for samples: RSD <15% for 20 spots in Arraias except Cr (20%), Ir (16%) and Os (20%), and better than 20% for the other meteorites",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "North Chile [all: RSD 20% at worst] — measured as an unknown over four months; its RSD represents 'the laboratory reproducibility or intermediate precision conditions'",
  "ada:analyticalAccuracyAndAssessmentMethod": "N — assessed on eight known iron meteorites, not a standard: 'More than 75% of published values are within the respective LA-ICP-MS result ±2s'; relative differences 'almost always within ±20%' (Fig. 2)",
  "ada:goodnessOfFitOrDispersionStatistic": "all: s, standard deviation of n measured values, and RSD — data table for Figs 2 and 3",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laSficpmsTAPP/preAnalysisImagingAndScreening",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsTAPP/preAnalysisImagingAndScreening"
        }
      ],
      "schema:name": "Pre-Analysis Imaging and Screening",
      "schema:value": "N — the preparation is stated without an imaging step: \"Before analyses, fragments about 1 cm were mounted in epoxy resin, polished, and cleaned with ultrapure water\" (p.3). The meteorites' structural classes were known beforehand (Table 1, p.2) but no screening of this material is described"
    },
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
      "@id": "ex:laSficpmsTAPP-Navarro2024",
      "schema:identifier": "test value schema:identifier"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "M.S.N.: Educorp (Unicamp) and International Association of Geoanalysts for Geoanalysis 2022 presentation; J.E.: CNPq grant 316191/2021-3",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only \u2014 iron meteorites by name (Table 1, p.2), each analysed as \"fragments about 1 cm\" (p.3); spots and mapped areas are counted (\"points 176\", p.12), not labelled",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": 20,
  "ada:transectLength": -9999,
  "ada:mappingArea": "missing",
  "ada:signalIntegrationTime": 40,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially \u2014 contributing counts are stated ('n: number of replicates'; 'the mean value of 20 spot measurements in the Arraias meteorite'); no acceptance or rejection rule is stated",
  "ada:combinedResults": "per-meteorite averages (Table 3 and the data table for Figs 2 and 3), for example Arraias (20 spots)",
  "ada:detectionLimit": "As: 2; Au: 0.1; Co: 2; Cr: 19; Cu: 0.8; Fe: 60; Ga: 0.3; Ge: 3; Ir: 0.2; Ni: 36; Os: 0.2; Pd: 0.5; Pt: 0.3; Re: 0.1; Rh: 0.1; Ru: 1; W: 1 \u2014 \u00b5g/g, median values (Table 3 'LOD')",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "N \u2014 precision is stated for samples: RSD <15% for 20 spots in Arraias except Cr (20%), Ir (16%) and Os (20%), and better than 20% for the other meteorites",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "North Chile [all: RSD 20% at worst] \u2014 measured as an unknown over four months; its RSD represents 'the laboratory reproducibility or intermediate precision conditions'",
  "ada:analyticalAccuracyAndAssessmentMethod": "N \u2014 assessed on eight known iron meteorites, not a standard: 'More than 75% of published values are within the respective LA-ICP-MS result \u00b12s'; relative differences 'almost always within \u00b120%' (Fig. 2)",
  "ada:goodnessOfFitOrDispersionStatistic": "all: s, standard deviation of n measured values, and RSD \u2014 data table for Figs 2 and 3",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laSficpmsTAPP/preAnalysisImagingAndScreening",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsTAPP/preAnalysisImagingAndScreening"
        }
      ],
      "schema:name": "Pre-Analysis Imaging and Screening",
      "schema:value": "N \u2014 the preparation is stated without an imaging step: \"Before analyses, fragments about 1 cm were mounted in epoxy resin, polished, and cleaned with ultrapure water\" (p.3). The meteorites' structural classes were known beforehand (Table 1, p.2) but no screening of this material is described"
    },
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

<ex:detail-Navarro2024> a ada:LAICPMSTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/preAnalysisImagingAndScreening>,
        <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize> ;
    schema1:measurementTechnique <ex:laSficpmsTAPP-Navarro2024> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially — contributing counts are stated ('n: number of replicates'; 'the mean value of 20 spot measurements in the Arraias meteorite'); no acceptance or rejection rule is stated" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "N — assessed on eight known iron meteorites, not a standard: 'More than 75% of published values are within the respective LA-ICP-MS result ±2s'; relative differences 'almost always within ±20%' (Fig. 2)" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "North Chile [all: RSD 20% at worst] — measured as an unknown over four months; its RSD represents 'the laboratory reproducibility or intermediate precision conditions'" ;
    ada:combinedResults "per-meteorite averages (Table 3 and the data table for Figs 2 and 3), for example Arraias (20 spots)" ;
    ada:componentType "ada:LAICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "As: 2; Au: 0.1; Co: 2; Cr: 19; Cu: 0.8; Fe: 60; Ga: 0.3; Ge: 3; Ir: 0.2; Ni: 36; Os: 0.2; Pd: 0.5; Pt: 0.3; Re: 0.1; Rh: 0.1; Ru: 1; W: 1 — µg/g, median values (Table 3 'LOD')" ;
    ada:fundingSourceForAnalysis "M.S.N.: Educorp (Unicamp) and International Association of Geoanalysts for Geoanalysis 2022 presentation; J.E.: CNPq grant 316191/2021-3" ;
    ada:goodnessOfFitOrDispersionStatistic "all: s, standard deviation of n measured values, and RSD — data table for Figs 2 and 3" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "missing" ;
    ada:numberOfReplicates 20 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Sample name only — iron meteorites by name (Table 1, p.2), each analysed as \"fragments about 1 cm\" (p.3); spots and mapped areas are counted (\"points 176\", p.12), not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime 40 ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "N — precision is stated for samples: RSD <15% for 20 spots in Arraias except Cr (20%), Ir (16%) and Os (20%), and better than 20% for the other meteorites" .

<ex:laSficpmsTAPP-Navarro2024> schema1:identifier "test value schema:identifier" .

<https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/preAnalysisImagingAndScreening> ;
    schema1:value "N — the preparation is stated without an imaging step: \"Before analyses, fragments about 1 cm were mounted in epoxy resin, polished, and cleaned with ultrapure water\" (p.3). The meteorites' structural classes were known beforehand (Table 1, p.2) but no screening of this material is described" .

<https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize> a schema1:PropertyValue ;
    schema1:name "Transect Rate, Mapping Rate or Step Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize> ;
    schema1:value "N/A — spot mode" .


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
      "@id": "ex:laSficpmsTAPP-Navarro2024-2",
      "schema:identifier": "test value schema:identifier"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "M.S.N.: Educorp (Unicamp) and International Association of Geoanalysts; J.E.: CNPq grant 316191/2021-3",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only — iron meteorites by name (Table 1, p.2), each analysed as \"fragments about 1 cm\" (p.3); spots and mapped areas are counted (\"points 176\", p.12), not labelled",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "Augusto Pestana: 30 min mapping session (area not explicitly stated; 150 µm spot at 10 µm s⁻¹)",
  "ada:signalIntegrationTime": "N/A — mapping",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially — the reported values integrate a stated number of points per phase, \"176 kamacite points (211,060 µm2) and 1,173 plessite points (1,712,297 µm2)\" (Table 5, p.12). The points are assigned to a phase rather than admitted or rejected, and no rejection rule is stated",
  "ada:combinedResults": "kamacite (176 points, 211,060 µm2); plessite (1,173 points, 1,712,297 µm2) — Table 5",
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
      "@id": "ada:parameter/laSficpmsTAPP/preAnalysisImagingAndScreening",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsTAPP/preAnalysisImagingAndScreening"
        }
      ],
      "schema:name": "Pre-Analysis Imaging and Screening",
      "schema:value": "Chemical etching to reveal the phases before mapping — \"For the mapping experiment, the polished surface of the Augusto Pestana sample was etched with freshly prepared Nital solution (2% v/v HNO3 ... in 99.5% absolute ethanol) to reveal the presence of different phases (in this case, kamacite and plessite)\" (p.3). Not imaging, but the screening step that sites the map"
    },
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
      "schema:value": "all: 10 µm/s — 'scanning at a speed of 10 μm s−1'"
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
      "@id": "ex:laSficpmsTAPP-Navarro2024-2",
      "schema:identifier": "test value schema:identifier"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "M.S.N.: Educorp (Unicamp) and International Association of Geoanalysts; J.E.: CNPq grant 316191/2021-3",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only \u2014 iron meteorites by name (Table 1, p.2), each analysed as \"fragments about 1 cm\" (p.3); spots and mapped areas are counted (\"points 176\", p.12), not labelled",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": -9999,
  "ada:mappingArea": "Augusto Pestana: 30 min mapping session (area not explicitly stated; 150 \u00b5m spot at 10 \u00b5m s\u207b\u00b9)",
  "ada:signalIntegrationTime": "N/A \u2014 mapping",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially \u2014 the reported values integrate a stated number of points per phase, \"176 kamacite points (211,060 \u00b5m2) and 1,173 plessite points (1,712,297 \u00b5m2)\" (Table 5, p.12). The points are assigned to a phase rather than admitted or rejected, and no rejection rule is stated",
  "ada:combinedResults": "kamacite (176 points, 211,060 \u00b5m2); plessite (1,173 points, 1,712,297 \u00b5m2) \u2014 Table 5",
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
      "@id": "ada:parameter/laSficpmsTAPP/preAnalysisImagingAndScreening",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laSficpmsTAPP/preAnalysisImagingAndScreening"
        }
      ],
      "schema:name": "Pre-Analysis Imaging and Screening",
      "schema:value": "Chemical etching to reveal the phases before mapping \u2014 \"For the mapping experiment, the polished surface of the Augusto Pestana sample was etched with freshly prepared Nital solution (2% v/v HNO3 ... in 99.5% absolute ethanol) to reveal the presence of different phases (in this case, kamacite and plessite)\" (p.3). Not imaging, but the screening step that sites the map"
    },
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
      "schema:value": "all: 10 \u00b5m/s \u2014 'scanning at a speed of 10 \u03bcm s\u22121'"
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

<ex:detail-Navarro2024-2> a ada:LAICPMSTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/preAnalysisImagingAndScreening>,
        <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize> ;
    schema1:measurementTechnique <ex:laSficpmsTAPP-Navarro2024-2> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially — the reported values integrate a stated number of points per phase, \"176 kamacite points (211,060 µm2) and 1,173 plessite points (1,712,297 µm2)\" (Table 5, p.12). The points are assigned to a phase rather than admitted or rejected, and no rejection rule is stated" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "missing" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:combinedResults "kamacite (176 points, 211,060 µm2); plessite (1,173 points, 1,712,297 µm2) — Table 5" ;
    ada:componentType "ada:LAICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:fundingSourceForAnalysis "M.S.N.: Educorp (Unicamp) and International Association of Geoanalysts; J.E.: CNPq grant 316191/2021-3" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "Augusto Pestana: 30 min mapping session (area not explicitly stated; 150 µm spot at 10 µm s⁻¹)" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Sample name only — iron meteorites by name (Table 1, p.2), each analysed as \"fragments about 1 cm\" (p.3); spots and mapped areas are counted (\"points 176\", p.12), not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime "N/A — mapping" ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<ex:laSficpmsTAPP-Navarro2024-2> schema1:identifier "test value schema:identifier" .

<https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/preAnalysisImagingAndScreening> a schema1:PropertyValue ;
    schema1:name "Pre-Analysis Imaging and Screening" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/preAnalysisImagingAndScreening> ;
    schema1:value "Chemical etching to reveal the phases before mapping — \"For the mapping experiment, the polished surface of the Augusto Pestana sample was etched with freshly prepared Nital solution (2% v/v HNO3 ... in 99.5% absolute ethanol) to reveal the presence of different phases (in this case, kamacite and plessite)\" (p.3). Not imaging, but the screening step that sites the map" .

<https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize> a schema1:PropertyValue ;
    schema1:name "Transect Rate, Mapping Rate or Step Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laSficpmsTAPP/transectRateMappingRateOrStepSize> ;
    schema1:value "all: 10 µm/s — 'scanning at a speed of 10 μm s−1'" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: LA-SF-ICP-MS Analysis Detail
description: Dataset-level analysis-instance detail for LA-SF-ICP-MS, reusing CDIF/schema.org
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
                  times. Not recoverable from Dwell Time per Mass alone, because settling
                  time is not captured there. Applies to sequential (quadrupole and
                  single-collector sector-field) acquisition."
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
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_transectLength
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_mappingArea
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_signalIntegrationTime
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Analysis_constantsReferenceValues
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
                  times. Not recoverable from Dwell Time per Mass alone, because settling
                  time is not captured there. Applies to sequential (quadrupole and
                  single-collector sector-field) acquisition."
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
                                        the time of instrument tuning. The acceptable
                                        threshold is typically <1% or <3%. Record
                                        both the threshold and the measured value.
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
                                        the time of instrument tuning. The acceptable
                                        threshold is typically <1% or <3%. Record
                                        both the threshold and the measured value.
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

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS/detail/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS/detail/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-SF-ICPMS/detail/context.jsonld)

## Sources

* [LA-SF-ICP-MS_TAPP_v16.csv (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/LA-SF-ICPMS/detail`

