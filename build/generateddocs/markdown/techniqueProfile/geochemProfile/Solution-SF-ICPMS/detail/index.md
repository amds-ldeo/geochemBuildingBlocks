
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
      "@id": "ex:solutionSficpmsTAPP-P0"
    }
  ],
  "ada:sessionIdentifier": "N -- \"A typical session comprised analyses of up to 50 unknowns and 15 standards\"; no session identifier stated",
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
  "ada:sampleName": "Soil and rock samples from boreholes BH1, BH2 (Sunbury), BH3, BH4 (Kalkallo), BH5 (Greenvale), BH6, BH (Wallan), incl. BH3a; reference materials BCR-2, BR, AGV-2, JB-2, JB-3, NIST SRM981, and Broken Hill Main Lode galena",
  "ada:samplingUnit": "Weighed split of a digest or leachate -- rock chips 0.05-0.24 g, soils 1-2.3 g; \"weighed splits taken for trace element and high-precision Pb isotope analysis by MC-ICPMS. At least 50% of each solution was retained for Pb isotope analysis by SC-SF-ICP-MS and Q-ICP-MS\"; \"Small splits of the soil samples (TD, AR) were used for Pb isotope analysis on a Nu Instruments Attom\"",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": 1,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "\"Typical column blanks were <20 pg Pb, while total procedural blanks (dissolution and/or leaching, including centrifuging) are estimated to be <100 pg\"; \"sample/blank ratios were >=1500, rendering blank corrections negligible\". Per-acquisition instrumental blank on the Attom: \"Each sample acquisition was preceded by a blank determination (average 900cps on 208Pb, equivalent to 1.8 ppt Pb in solution)\" [sec 2.4]",
  "ada:analysisInclusionAndRejectionCriteria": "Partially -- n stated per averaged result (BCR-2 n = 39, AGV-2 n = 13, BR n = 11, JB-2 n = 9, JB-3 n = 11, SRM981 n = 22 and n = 16). One documented exclusion, from the quality assessment rather than from a reported aggregate: \"Results for the pure Pb standard NIST SRM981, analysed many times with the soil samples, are not included here, because it contains no matrix and may thus not a be a good indicator of data quality for the soil samples analysed here\" [sec 3.1]. No acceptance or rejection rule, and no acquired-versus-included count, stated",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "A single analysis of 30-40 10-s integrations gives typical internal precision (2SE) of +/-0.001-0.002 for 206Pb/204Pb and +/-0.003-0.005 for 208Pb/204Pb",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "2 sigma uncertainty of 30-set Pb isotope ratios per sample (stated section 2.3)",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "% deviation from published Pb isotope values for geological RMs (BCR-2, AGV-2, JB-2, BR, JB-3; stated section 3)",
  "ada:goodnessOfFitOrDispersionStatistic": "N for the quantity this field defines. A regression statistic is reported for the measured-versus-nominal comparison -- \"The data distributions around the nominal compositions (Fig. 2) have slopes near 1 (with correlation coefficients of 0.75-0.85)\" -- which is not a test of whether scatter among contributing analyses exceeds analytical uncertainty"
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
      "@id": "ex:solutionSficpmsTAPP-P0"
    }
  ],
  "ada:sessionIdentifier": "N -- \"A typical session comprised analyses of up to 50 unknowns and 15 standards\"; no session identifier stated",
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
  "ada:sampleName": "Soil and rock samples from boreholes BH1, BH2 (Sunbury), BH3, BH4 (Kalkallo), BH5 (Greenvale), BH6, BH (Wallan), incl. BH3a; reference materials BCR-2, BR, AGV-2, JB-2, JB-3, NIST SRM981, and Broken Hill Main Lode galena",
  "ada:samplingUnit": "Weighed split of a digest or leachate -- rock chips 0.05-0.24 g, soils 1-2.3 g; \"weighed splits taken for trace element and high-precision Pb isotope analysis by MC-ICPMS. At least 50% of each solution was retained for Pb isotope analysis by SC-SF-ICP-MS and Q-ICP-MS\"; \"Small splits of the soil samples (TD, AR) were used for Pb isotope analysis on a Nu Instruments Attom\"",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": 1,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "\"Typical column blanks were <20 pg Pb, while total procedural blanks (dissolution and/or leaching, including centrifuging) are estimated to be <100 pg\"; \"sample/blank ratios were >=1500, rendering blank corrections negligible\". Per-acquisition instrumental blank on the Attom: \"Each sample acquisition was preceded by a blank determination (average 900cps on 208Pb, equivalent to 1.8 ppt Pb in solution)\" [sec 2.4]",
  "ada:analysisInclusionAndRejectionCriteria": "Partially -- n stated per averaged result (BCR-2 n = 39, AGV-2 n = 13, BR n = 11, JB-2 n = 9, JB-3 n = 11, SRM981 n = 22 and n = 16). One documented exclusion, from the quality assessment rather than from a reported aggregate: \"Results for the pure Pb standard NIST SRM981, analysed many times with the soil samples, are not included here, because it contains no matrix and may thus not a be a good indicator of data quality for the soil samples analysed here\" [sec 3.1]. No acceptance or rejection rule, and no acquired-versus-included count, stated",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "A single analysis of 30-40 10-s integrations gives typical internal precision (2SE) of +/-0.001-0.002 for 206Pb/204Pb and +/-0.003-0.005 for 208Pb/204Pb",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "2 sigma uncertainty of 30-set Pb isotope ratios per sample (stated section 2.3)",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "% deviation from published Pb isotope values for geological RMs (BCR-2, AGV-2, JB-2, BR, JB-3; stated section 3)",
  "ada:goodnessOfFitOrDispersionStatistic": "N for the quantity this field defines. A regression statistic is reported for the measured-versus-nominal comparison -- \"The data distributions around the nominal compositions (Fig. 2) have slopes near 1 (with correlation coefficients of 0.75-0.85)\" -- which is not a test of whether scatter among contributing analyses exceeds analytical uncertainty"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-P0 a ada:SolutionICPMSTabular ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:solutionSficpmsTAPP-P0 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially -- n stated per averaged result (BCR-2 n = 39, AGV-2 n = 13, BR n = 11, JB-2 n = 9, JB-3 n = 11, SRM981 n = 22 and n = 16). One documented exclusion, from the quality assessment rather than from a reported aggregate: \"Results for the pure Pb standard NIST SRM981, analysed many times with the soil samples, are not included here, because it contains no matrix and may thus not a be a good indicator of data quality for the soil samples analysed here\" [sec 3.1]. No acceptance or rejection rule, and no acquired-versus-included count, stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "% deviation from published Pb isotope values for geological RMs (BCR-2, AGV-2, JB-2, BR, JB-3; stated section 3)" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "N for the quantity this field defines. A regression statistic is reported for the measured-versus-nominal comparison -- \"The data distributions around the nominal compositions (Fig. 2) have slopes near 1 (with correlation coefficients of 0.75-0.85)\" -- which is not a test of whether scatter among contributing analyses exceeds analytical uncertainty" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "A single analysis of 30-40 10-s integrations gives typical internal precision (2SE) of +/-0.001-0.002 for 206Pb/204Pb and +/-0.003-0.005 for 208Pb/204Pb" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:numberOfReplicates 1 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "\"Typical column blanks were <20 pg Pb, while total procedural blanks (dissolution and/or leaching, including centrifuging) are estimated to be <100 pg\"; \"sample/blank ratios were >=1500, rendering blank corrections negligible\". Per-acquisition instrumental blank on the Attom: \"Each sample acquisition was preceded by a blank determination (average 900cps on 208Pb, equivalent to 1.8 ppt Pb in solution)\" [sec 2.4]" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "Soil and rock samples from boreholes BH1, BH2 (Sunbury), BH3, BH4 (Kalkallo), BH5 (Greenvale), BH6, BH (Wallan), incl. BH3a; reference materials BCR-2, BR, AGV-2, JB-2, JB-3, NIST SRM981, and Broken Hill Main Lode galena" ;
    ada:samplingUnit "Weighed split of a digest or leachate -- rock chips 0.05-0.24 g, soils 1-2.3 g; \"weighed splits taken for trace element and high-precision Pb isotope analysis by MC-ICPMS. At least 50% of each solution was retained for Pb isotope analysis by SC-SF-ICP-MS and Q-ICP-MS\"; \"Small splits of the soil samples (TD, AR) were used for Pb isotope analysis on a Nu Instruments Attom\"" ;
    ada:sessionIdentifier "N -- \"A typical session comprised analyses of up to 50 unknowns and 15 standards\"; no session identifier stated" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "2 sigma uncertainty of 30-set Pb isotope ratios per sample (stated section 2.3)" .


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
      "@id": "ex:solutionSficpmsTAPP-P1"
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
  "ada:sampleName": "mag_1, mag_3, mag_5, py_2, py_4; iron-formation reference material FER-2 (CCRMP, CANMET MMSL, Canada)",
  "ada:samplingUnit": "Aliquot of the digest solution -- 50 mg FER-2 and \"approximately 100 mg of the studied mineral samples\" digested; \"a small aliquot sample solution was taken for column separation\", \"7.2 mg Fe in 10% aliquot of magnetite solution\"; \"A 1.8 g sample solution (in 2 g of 10 M HCl) was weighed and loaded\"",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "\"The concentration of elements in the procedural blank ranged from 0.004 ng mL-1 (Cs) to 0.216 ng mL-1 (Zn)\"; \"the highest blank level in Zn would contribute less than 0.01% of the amount of analyte\"",
  "ada:analysisInclusionAndRejectionCriteria": "Partially -- \"The mean values and respective standard deviations (s) for three analyses were listed in Table 3\"; n = 3 throughout. No acceptance or rejection rule stated",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "%RSD of replicate analyses (stated Table 5)",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "% recovery relative to certified/consensus values for geological RMs (stated Table 5)",
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
  "@id": "ex:detail-P1",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionSficpmsTAPP-P1"
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
  "ada:sampleName": "mag_1, mag_3, mag_5, py_2, py_4; iron-formation reference material FER-2 (CCRMP, CANMET MMSL, Canada)",
  "ada:samplingUnit": "Aliquot of the digest solution -- 50 mg FER-2 and \"approximately 100 mg of the studied mineral samples\" digested; \"a small aliquot sample solution was taken for column separation\", \"7.2 mg Fe in 10% aliquot of magnetite solution\"; \"A 1.8 g sample solution (in 2 g of 10 M HCl) was weighed and loaded\"",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "\"The concentration of elements in the procedural blank ranged from 0.004 ng mL-1 (Cs) to 0.216 ng mL-1 (Zn)\"; \"the highest blank level in Zn would contribute less than 0.01% of the amount of analyte\"",
  "ada:analysisInclusionAndRejectionCriteria": "Partially -- \"The mean values and respective standard deviations (s) for three analyses were listed in Table 3\"; n = 3 throughout. No acceptance or rejection rule stated",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "%RSD of replicate analyses (stated Table 5)",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "% recovery relative to certified/consensus values for geological RMs (stated Table 5)",
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-P1 a ada:SolutionICPMSTabular ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:solutionSficpmsTAPP-P1 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially -- \"The mean values and respective standard deviations (s) for three analyses were listed in Table 3\"; n = 3 throughout. No acceptance or rejection rule stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "% recovery relative to certified/consensus values for geological RMs (stated Table 5)" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "\"The concentration of elements in the procedural blank ranged from 0.004 ng mL-1 (Cs) to 0.216 ng mL-1 (Zn)\"; \"the highest blank level in Zn would contribute less than 0.01% of the amount of analyte\"" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "mag_1, mag_3, mag_5, py_2, py_4; iron-formation reference material FER-2 (CCRMP, CANMET MMSL, Canada)" ;
    ada:samplingUnit "Aliquot of the digest solution -- 50 mg FER-2 and \"approximately 100 mg of the studied mineral samples\" digested; \"a small aliquot sample solution was taken for column separation\", \"7.2 mg Fe in 10% aliquot of magnetite solution\"; \"A 1.8 g sample solution (in 2 g of 10 M HCl) was weighed and loaded\"" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "%RSD of replicate analyses (stated Table 5)" .


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
      "@id": "ex:solutionSficpmsTAPP-P2"
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
  "ada:sampleName": "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1 (GSJ); BHVO-1, AGV-1, PCC-1, DTS-1 (USGS); Ivuna (CI1), Orgueil (CI1), Cold Bokkeveld (CM2), Allende (USNM 3529, Split 1, Pos. 23)",
  "ada:samplingUnit": "Weighed test portion -- \"Approximately 20 mg of basalt and andesite samples were weighed\"; \"Approximately 50 mg for peridotites and approximately 10 mg for meteorites\"; 9-18 mg for carbonaceous chondrites",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "Blanks in spike solutions (pg g-1) and total procedural blank (pg) tabulated per element; \"The blank corrections were usually <1% in basalt and andesite analyses and <4% in peridotite reference materials\"; \"Total Sn blank levels are ~300 pg in both the ultrasonic and the bomb methods\" [sec 3.6]",
  "ada:analysisInclusionAndRejectionCriteria": "Partially -- \"Orgueil and Allende were analyzed 4 times and twice from the sample digestion, respectively ... analytical results for each run are shown in the table\" alongside the averages. No acceptance or rejection rule stated",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "% recovery relative to certified/consensus values for USGS/GSJ RMs and chondrites (stated section 3)",
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
  "@id": "ex:detail-P2",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionSficpmsTAPP-P2"
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
  "ada:sampleName": "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1 (GSJ); BHVO-1, AGV-1, PCC-1, DTS-1 (USGS); Ivuna (CI1), Orgueil (CI1), Cold Bokkeveld (CM2), Allende (USNM 3529, Split 1, Pos. 23)",
  "ada:samplingUnit": "Weighed test portion -- \"Approximately 20 mg of basalt and andesite samples were weighed\"; \"Approximately 50 mg for peridotites and approximately 10 mg for meteorites\"; 9-18 mg for carbonaceous chondrites",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "Blanks in spike solutions (pg g-1) and total procedural blank (pg) tabulated per element; \"The blank corrections were usually <1% in basalt and andesite analyses and <4% in peridotite reference materials\"; \"Total Sn blank levels are ~300 pg in both the ultrasonic and the bomb methods\" [sec 3.6]",
  "ada:analysisInclusionAndRejectionCriteria": "Partially -- \"Orgueil and Allende were analyzed 4 times and twice from the sample digestion, respectively ... analytical results for each run are shown in the table\" alongside the averages. No acceptance or rejection rule stated",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "% recovery relative to certified/consensus values for USGS/GSJ RMs and chondrites (stated section 3)",
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-P2 a ada:SolutionICPMSTabular ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:solutionSficpmsTAPP-P2 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially -- \"Orgueil and Allende were analyzed 4 times and twice from the sample digestion, respectively ... analytical results for each run are shown in the table\" alongside the averages. No acceptance or rejection rule stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "% recovery relative to certified/consensus values for USGS/GSJ RMs and chondrites (stated section 3)" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "Blanks in spike solutions (pg g-1) and total procedural blank (pg) tabulated per element; \"The blank corrections were usually <1% in basalt and andesite analyses and <4% in peridotite reference materials\"; \"Total Sn blank levels are ~300 pg in both the ultrasonic and the bomb methods\" [sec 3.6]" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "JB-1, JB-2, JB-3, JA-1, JA-2, JA-3, JP-1 (GSJ); BHVO-1, AGV-1, PCC-1, DTS-1 (USGS); Ivuna (CI1), Orgueil (CI1), Cold Bokkeveld (CM2), Allende (USNM 3529, Split 1, Pos. 23)" ;
    ada:samplingUnit "Weighed test portion -- \"Approximately 20 mg of basalt and andesite samples were weighed\"; \"Approximately 50 mg for peridotites and approximately 10 mg for meteorites\"; 9-18 mg for carbonaceous chondrites" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .


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
      "@id": "ex:solutionSficpmsTAPP-P3"
    }
  ],
  "ada:sessionIdentifier": "N -- \"Each analytical session would begin and end with the analysis of a series of Mo standards (1-100 nM)\"; \"an analysis sequence\"; \"1 day's analysis\"; \"three separate days of analyses\". No session or sequence identifier stated",
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
  "ada:sampleName": "Open-ocean seawater reference materials SAFe S1, SAFe D2 and NASS-5; GEOTRACES inter-calibration samples GS (surface) and GD (deep); depth-profile samples from the BATS station, 31 deg 45' N, 64 deg 05' W, 23 June 2008",
  "ada:samplingUnit": "12 mL sub-sample (aliquot) of an acidified seawater sample -- \"Acidified seawater samples ... were sub-sampled (12 mL) into clean 30 mL FEP Teflon bottles. The 12 mL aliquots were spiked\"; \"standard additions ... were added to individual 12 mL sub-samples of the same sample\"; \"Standard additions of Co and Mn were performed on a further four aliquots (1 mL) of the elution acid\"",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "Per-element reagent blank with 1 S.D. in pmoles, broken down into elution acid and ammonium acetate buffer contributions (Mn 0.433 +/- 0.026; Fe 2.791 +/- 0.083; Co 0.078 +/- 0.006; Ni 0.457 +/- 0.104; Cu 0.184 +/- 0.027; Zn 3.044 +/- 0.018; Cd 0.045 +/- 0.003; Pb 0.017 +/- 0.001)",
  "ada:analysisInclusionAndRejectionCriteria": "Partially -- \"The blank solutions were analysed at least three times on the ICP-MS\"; \"parallel triplicate samples\"; n = 3 for reference materials and n = 5 for the GEOTRACES samples. No acceptance or rejection rule stated",
  "ada:detectionLimit": "Analyte-specific (pg/kg to pM level; e.g., Fe 0.01 nM in seawater; stated Table 1)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "%RSD of replicate measurements (stated section 2.4)",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "Comparison with SAFe consensus values and NASS-5 certified values (stated section 2.4)",
  "ada:goodnessOfFitOrDispersionStatistic": "N -- standard-addition regressions are reported with average slope, SD and %RSD, but no fit statistic"
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
      "@id": "ex:solutionSficpmsTAPP-P3"
    }
  ],
  "ada:sessionIdentifier": "N -- \"Each analytical session would begin and end with the analysis of a series of Mo standards (1-100 nM)\"; \"an analysis sequence\"; \"1 day's analysis\"; \"three separate days of analyses\". No session or sequence identifier stated",
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
  "ada:sampleName": "Open-ocean seawater reference materials SAFe S1, SAFe D2 and NASS-5; GEOTRACES inter-calibration samples GS (surface) and GD (deep); depth-profile samples from the BATS station, 31 deg 45' N, 64 deg 05' W, 23 June 2008",
  "ada:samplingUnit": "12 mL sub-sample (aliquot) of an acidified seawater sample -- \"Acidified seawater samples ... were sub-sampled (12 mL) into clean 30 mL FEP Teflon bottles. The 12 mL aliquots were spiked\"; \"standard additions ... were added to individual 12 mL sub-samples of the same sample\"; \"Standard additions of Co and Mn were performed on a further four aliquots (1 mL) of the elution acid\"",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "Per-element reagent blank with 1 S.D. in pmoles, broken down into elution acid and ammonium acetate buffer contributions (Mn 0.433 +/- 0.026; Fe 2.791 +/- 0.083; Co 0.078 +/- 0.006; Ni 0.457 +/- 0.104; Cu 0.184 +/- 0.027; Zn 3.044 +/- 0.018; Cd 0.045 +/- 0.003; Pb 0.017 +/- 0.001)",
  "ada:analysisInclusionAndRejectionCriteria": "Partially -- \"The blank solutions were analysed at least three times on the ICP-MS\"; \"parallel triplicate samples\"; n = 3 for reference materials and n = 5 for the GEOTRACES samples. No acceptance or rejection rule stated",
  "ada:detectionLimit": "Analyte-specific (pg/kg to pM level; e.g., Fe 0.01 nM in seawater; stated Table 1)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "%RSD of replicate measurements (stated section 2.4)",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "Comparison with SAFe consensus values and NASS-5 certified values (stated section 2.4)",
  "ada:goodnessOfFitOrDispersionStatistic": "N -- standard-addition regressions are reported with average slope, SD and %RSD, but no fit statistic"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-P3 a ada:SolutionICPMSTabular ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:solutionSficpmsTAPP-P3 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially -- \"The blank solutions were analysed at least three times on the ICP-MS\"; \"parallel triplicate samples\"; n = 3 for reference materials and n = 5 for the GEOTRACES samples. No acceptance or rejection rule stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "Comparison with SAFe consensus values and NASS-5 certified values (stated section 2.4)" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "Analyte-specific (pg/kg to pM level; e.g., Fe 0.01 nM in seawater; stated Table 1)" ;
    ada:goodnessOfFitOrDispersionStatistic "N -- standard-addition regressions are reported with average slope, SD and %RSD, but no fit statistic" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "Per-element reagent blank with 1 S.D. in pmoles, broken down into elution acid and ammonium acetate buffer contributions (Mn 0.433 +/- 0.026; Fe 2.791 +/- 0.083; Co 0.078 +/- 0.006; Ni 0.457 +/- 0.104; Cu 0.184 +/- 0.027; Zn 3.044 +/- 0.018; Cd 0.045 +/- 0.003; Pb 0.017 +/- 0.001)" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "Open-ocean seawater reference materials SAFe S1, SAFe D2 and NASS-5; GEOTRACES inter-calibration samples GS (surface) and GD (deep); depth-profile samples from the BATS station, 31 deg 45' N, 64 deg 05' W, 23 June 2008" ;
    ada:samplingUnit "12 mL sub-sample (aliquot) of an acidified seawater sample -- \"Acidified seawater samples ... were sub-sampled (12 mL) into clean 30 mL FEP Teflon bottles. The 12 mL aliquots were spiked\"; \"standard additions ... were added to individual 12 mL sub-samples of the same sample\"; \"Standard additions of Co and Mn were performed on a further four aliquots (1 mL) of the elution acid\"" ;
    ada:sessionIdentifier "N -- \"Each analytical session would begin and end with the analysis of a series of Mo standards (1-100 nM)\"; \"an analysis sequence\"; \"1 day's analysis\"; \"three separate days of analyses\". No session or sequence identifier stated" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "%RSD of replicate measurements (stated section 2.4)" .


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
      "@id": "ex:solutionSficpmsTAPP-P4"
    }
  ],
  "ada:sessionIdentifier": "N -- \"a single instrument session\" referenced; no session identifier stated",
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
  "ada:sampleName": "In-house consistency standards CAM-wuellerstorfi, CAM-Uvig-1, CAM-Uvig-2 and CAM-Mix; Globigerinoides sacculifer specimens of the 300-355 um size fraction",
  "ada:samplingUnit": "Dissolved foraminiferal test aliquot -- \"capable of analyzing small masses of calcite (5-10 mg), including single foraminifera specimens\"; \"Leached samples were dissolved in a minimum volume of 1 M HNO3 (40-60 uL) ... centrifuged for 2 min at 10,000 rpm and the supernatant was used for Me/Ca analysis. A 5 uL aliquot ...\"",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": 3,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "\"Our procedural B/Ca blank of 2.0 +/- 1.0 umol/mol\"; instrumental 11B blank in cps tabulated against spray chamber material, injector material and acid matrix (2011-19,750 cps) [Table 2]",
  "ada:analysisInclusionAndRejectionCriteria": "Partially -- \"Open symbols represent an average of 10 measurements acquired during a single instrument session. The solid symbols represent the average of the open symbols\"; and for a second figure \"which is a total of 15 measurements\"; acquisition structured as 3 runs x 15 passes (low resolution) or 3 x 5 (medium). No acceptance or rejection rule stated",
  "ada:detectionLimit": "~2 umol/mol B/Ca procedural blank (stated abstract)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "%RSD of repeated consistency standard analyses (stated section 2.3.1)",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "% bias relative to published foraminifera inter-lab consensus values (stated section 2.3.1)",
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
      "@id": "ex:solutionSficpmsTAPP-P4"
    }
  ],
  "ada:sessionIdentifier": "N -- \"a single instrument session\" referenced; no session identifier stated",
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
  "ada:sampleName": "In-house consistency standards CAM-wuellerstorfi, CAM-Uvig-1, CAM-Uvig-2 and CAM-Mix; Globigerinoides sacculifer specimens of the 300-355 um size fraction",
  "ada:samplingUnit": "Dissolved foraminiferal test aliquot -- \"capable of analyzing small masses of calcite (5-10 mg), including single foraminifera specimens\"; \"Leached samples were dissolved in a minimum volume of 1 M HNO3 (40-60 uL) ... centrifuged for 2 min at 10,000 rpm and the supernatant was used for Me/Ca analysis. A 5 uL aliquot ...\"",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": 3,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "\"Our procedural B/Ca blank of 2.0 +/- 1.0 umol/mol\"; instrumental 11B blank in cps tabulated against spray chamber material, injector material and acid matrix (2011-19,750 cps) [Table 2]",
  "ada:analysisInclusionAndRejectionCriteria": "Partially -- \"Open symbols represent an average of 10 measurements acquired during a single instrument session. The solid symbols represent the average of the open symbols\"; and for a second figure \"which is a total of 15 measurements\"; acquisition structured as 3 runs x 15 passes (low resolution) or 3 x 5 (medium). No acceptance or rejection rule stated",
  "ada:detectionLimit": "~2 umol/mol B/Ca procedural blank (stated abstract)",
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "%RSD of repeated consistency standard analyses (stated section 2.3.1)",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "% bias relative to published foraminifera inter-lab consensus values (stated section 2.3.1)",
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-P4 a ada:SolutionICPMSTabular ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:solutionSficpmsTAPP-P4 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially -- \"Open symbols represent an average of 10 measurements acquired during a single instrument session. The solid symbols represent the average of the open symbols\"; and for a second figure \"which is a total of 15 measurements\"; acquisition structured as 3 runs x 15 passes (low resolution) or 3 x 5 (medium). No acceptance or rejection rule stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "% bias relative to published foraminifera inter-lab consensus values (stated section 2.3.1)" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "~2 umol/mol B/Ca procedural blank (stated abstract)" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:numberOfReplicates 3 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "\"Our procedural B/Ca blank of 2.0 +/- 1.0 umol/mol\"; instrumental 11B blank in cps tabulated against spray chamber material, injector material and acid matrix (2011-19,750 cps) [Table 2]" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "In-house consistency standards CAM-wuellerstorfi, CAM-Uvig-1, CAM-Uvig-2 and CAM-Mix; Globigerinoides sacculifer specimens of the 300-355 um size fraction" ;
    ada:samplingUnit "Dissolved foraminiferal test aliquot -- \"capable of analyzing small masses of calcite (5-10 mg), including single foraminifera specimens\"; \"Leached samples were dissolved in a minimum volume of 1 M HNO3 (40-60 uL) ... centrifuged for 2 min at 10,000 rpm and the supernatant was used for Me/Ca analysis. A 5 uL aliquot ...\"" ;
    ada:sessionIdentifier "N -- \"a single instrument session\" referenced; no session identifier stated" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "%RSD of repeated consistency standard analyses (stated section 2.3.1)" .


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
      "@id": "ex:solutionSficpmsTAPP-Willbold2005"
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
  "ada:sampleName": "AGV-1, AGV-2, BCR-1, BCR-2, BCR-2G, BIR-1, BIR-1G, BHVO-1, BHVO-2, BHVO-2G, G-2, JR-1, KL2-G, ML3B-G, NIST SRM 612, OU-6, PCC-1 -- tabulated with issuing organisation and split/position numbers (e.g. BHVO-1 Split 15 Pos 26; G-2 Split 58 Pos 23)",
  "ada:samplingUnit": "Digestion, with determinations nested inside it -- \"Five independent analyses (different spikings/digestions) of BHVO-1 were carried out over a time period of 4 months. Triplicate determinations were performed for each digestion\"; \"Only one digestion was prepared for the USGS reference glasses ... and were measured in triplicate\"",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "Partially -- \"Limits of detection (LOD) were calculated according to the 3s criterion on a data set of fifty measurements in LR mode and twenty measurements in HR mode of total procedural blanks (including spiking)\"; LODs \"ranged between about 0.1 and 10 ng g-1 sample equivalents for most elements\". The blank levels themselves are not tabulated",
  "ada:analysisInclusionAndRejectionCriteria": "Partially, and the most complete of the six -- \"Five independent analyses (different spikings/digestions) of BHVO-1 were carried out over a time period of 4 months. Triplicate determinations were performed for each digestion\"; \"the results of three to four independent analyses of sixteen other RMs\"; \"Only one digestion was prepared for the USGS reference glasses BCR-2G, BHVO-2G and BIR-1G, and NIST SRM 612 respectively and were measured in triplicate\". No acceptance or rejection rule stated",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "%RSD of repeated RM analyses within session (stated Table 5)",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "% recovery relative to published consensus values for geological RMs (stated Table 5)",
  "ada:goodnessOfFitOrDispersionStatistic": "N -- a power law is fitted to the calculated mass fractionation factors, but no fit statistic is reported"
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
      "@id": "ex:solutionSficpmsTAPP-Willbold2005"
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
  "ada:sampleName": "AGV-1, AGV-2, BCR-1, BCR-2, BCR-2G, BIR-1, BIR-1G, BHVO-1, BHVO-2, BHVO-2G, G-2, JR-1, KL2-G, ML3B-G, NIST SRM 612, OU-6, PCC-1 -- tabulated with issuing organisation and split/position numbers (e.g. BHVO-1 Split 15 Pos 26; G-2 Split 58 Pos 23)",
  "ada:samplingUnit": "Digestion, with determinations nested inside it -- \"Five independent analyses (different spikings/digestions) of BHVO-1 were carried out over a time period of 4 months. Triplicate determinations were performed for each digestion\"; \"Only one digestion was prepared for the USGS reference glasses ... and were measured in triplicate\"",
  "ada:sampleDescription": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:oxideProduction": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "Partially -- \"Limits of detection (LOD) were calculated according to the 3s criterion on a data set of fifty measurements in LR mode and twenty measurements in HR mode of total procedural blanks (including spiking)\"; LODs \"ranged between about 0.1 and 10 ng g-1 sample equivalents for most elements\". The blank levels themselves are not tabulated",
  "ada:analysisInclusionAndRejectionCriteria": "Partially, and the most complete of the six -- \"Five independent analyses (different spikings/digestions) of BHVO-1 were carried out over a time period of 4 months. Triplicate determinations were performed for each digestion\"; \"the results of three to four independent analyses of sixteen other RMs\"; \"Only one digestion was prepared for the USGS reference glasses BCR-2G, BHVO-2G and BIR-1G, and NIST SRM 612 respectively and were measured in triplicate\". No acceptance or rejection rule stated",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "%RSD of repeated RM analyses within session (stated Table 5)",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "% recovery relative to published consensus values for geological RMs (stated Table 5)",
  "ada:goodnessOfFitOrDispersionStatistic": "N -- a power law is fitted to the calculated mass fractionation factors, but no fit statistic is reported"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Willbold2005 a ada:SolutionICPMSTabular ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:solutionSficpmsTAPP-Willbold2005 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially, and the most complete of the six -- \"Five independent analyses (different spikings/digestions) of BHVO-1 were carried out over a time period of 4 months. Triplicate determinations were performed for each digestion\"; \"the results of three to four independent analyses of sixteen other RMs\"; \"Only one digestion was prepared for the USGS reference glasses BCR-2G, BHVO-2G and BIR-1G, and NIST SRM 612 respectively and were measured in triplicate\". No acceptance or rejection rule stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "% recovery relative to published consensus values for geological RMs (stated Table 5)" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "N -- a power law is fitted to the calculated mass fractionation factors, but no fit statistic is reported" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:proceduralBlankLevel "Partially -- \"Limits of detection (LOD) were calculated according to the 3s criterion on a data set of fifty measurements in LR mode and twenty measurements in HR mode of total procedural blanks (including spiking)\"; LODs \"ranged between about 0.1 and 10 ng g-1 sample equivalents for most elements\". The blank levels themselves are not tabulated" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "AGV-1, AGV-2, BCR-1, BCR-2, BCR-2G, BIR-1, BIR-1G, BHVO-1, BHVO-2, BHVO-2G, G-2, JR-1, KL2-G, ML3B-G, NIST SRM 612, OU-6, PCC-1 -- tabulated with issuing organisation and split/position numbers (e.g. BHVO-1 Split 15 Pos 26; G-2 Split 58 Pos 23)" ;
    ada:samplingUnit "Digestion, with determinations nested inside it -- \"Five independent analyses (different spikings/digestions) of BHVO-1 were carried out over a time period of 4 months. Triplicate determinations were performed for each digestion\"; \"Only one digestion was prepared for the USGS reference glasses ... and were measured in triplicate\"" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "%RSD of repeated RM analyses within session (stated Table 5)" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Solution SF-ICP-MS Analysis Detail
description: Dataset-level analysis-instance detail for solution SF-ICP-MS, reusing
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
                                              - title: Auxiliary Gas Flow Rate
                                                description: Flow rate of the intermediate
                                                  (auxiliary) argon gas stream between
                                                  torch body and injector tube (L/min).
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/solutionSficpmsTAPP/auxiliaryGasFlowRate
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/solutionSficpmsTAPP/auxiliaryGasFlowRate
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
                                              - title: Coolant (Plasma) Gas Flow Rate
                                                description: Flow rate of the outer
                                                  (coolant) argon gas stream (L/min).
                                                  Influences plasma temperature and
                                                  oxide ion formation.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/solutionSficpmsTAPP/coolantGasFlowRate
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/solutionSficpmsTAPP/coolantGasFlowRate
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
                                              - title: RF Power
                                                description: Radiofrequency forward
                                                  power applied to the plasma (W).
                                                  Controls ionization efficiency and
                                                  oxide production rates.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/solutionSficpmsTAPP/rfPower
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/solutionSficpmsTAPP/rfPower
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
                                                title: Auxiliary Gas Flow Rate
                                                description: Flow rate of the intermediate
                                                  (auxiliary) argon gas stream between
                                                  torch body and injector tube (L/min).
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/solutionSficpmsTAPP/auxiliaryGasFlowRate
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/solutionSficpmsTAPP/auxiliaryGasFlowRate
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
                                                title: Coolant (Plasma) Gas Flow Rate
                                                description: Flow rate of the outer
                                                  (coolant) argon gas stream (L/min).
                                                  Influences plasma temperature and
                                                  oxide ion formation.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/solutionSficpmsTAPP/coolantGasFlowRate
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/solutionSficpmsTAPP/coolantGasFlowRate
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
                                                title: RF Power
                                                description: Radiofrequency forward
                                                  power applied to the plasma (W).
                                                  Controls ionization efficiency and
                                                  oxide production rates.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/solutionSficpmsTAPP/rfPower
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/solutionSficpmsTAPP/rfPower
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
                                                    const: ada:parameter/solutionSficpmsTAPP/makeUpGasAndFlowRate
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/solutionSficpmsTAPP/makeUpGasAndFlowRate
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
                                              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Analysis_nebulizerGasFlowRate
                                              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/solutionIntroduction/schema.yaml#/$defs/Param_Analysis_sampleUptakeRate
                                            allOf:
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
                                                    const: ada:parameter/solutionSficpmsTAPP/makeUpGasAndFlowRate
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/solutionSficpmsTAPP/makeUpGasAndFlowRate
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
                                                  const: ada:parameter/solutionSficpmsTAPP/torchDepth
                                                '@type':
                                                  const:
                                                  - schema:PropertyValue
                                                schema:propertyID:
                                                  const:
                                                  - '@id': ada:parameter/solutionSficpmsTAPP/torchDepth
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
                                                    const: ada:parameter/solutionSficpmsTAPP/torchDepth
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/solutionSficpmsTAPP/torchDepth
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
                                      description: Mass ratio monitored to estimate
                                        doubly-charged ion (M2+) formation during
                                        instrument tuning. Doubly-charged ions appear
                                        at half the nominal mass of the parent ion
                                        and can interfere with lighter analyte masses.
                                        In SF-ICP-MS, doubly-charged species are not
                                        suppressed by collision cells and require
                                        monitoring through plasma tuning. Ba2+/Ba+
                                        (m/z 69/138) is the most common proxy.
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
                                        the time of instrument tuning. Record both
                                        the acceptance threshold and the measured
                                        value. Elevated doubly-charged production
                                        indicates incomplete ionization and potential
                                        interference on elements at approximately
                                        half the mass of abundant matrix components.
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
                                    - title: Mass Resolution Setting
                                      description: "Mass resolution mode(s) used in
                                        this procedure. Sector-field instruments allow
                                        selection of low resolution (LR; m/\u0394m
                                        \u2248 300\u2013400), medium resolution (MR;
                                        m/\u0394m \u2248 2500\u20135000), or high
                                        resolution (HR; m/\u0394m \u2248 10,000).
                                        Multi-resolution procedures assign individual
                                        analytes to specific modes (documented in
                                        Group 4 under Mass Resolution Assignment).
                                        Procedure registers the mode(s) in use; analyst
                                        confirms at session start."
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/solutionSficpmsTAPP/massResolutionSetting
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/solutionSficpmsTAPP/massResolutionSetting
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
                                          const: ada:parameter/solutionSficpmsTAPP/memoryEffectMitigation
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/solutionSficpmsTAPP/memoryEffectMitigation
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
                                        In SF-ICP-MS, doubly-charged species are not
                                        suppressed by collision cells and require
                                        monitoring through plasma tuning. Ba2+/Ba+
                                        (m/z 69/138) is the most common proxy.
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
                                        the time of instrument tuning. Record both
                                        the acceptance threshold and the measured
                                        value. Elevated doubly-charged production
                                        indicates incomplete ionization and potential
                                        interference on elements at approximately
                                        half the mass of abundant matrix components.
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
                                      title: Mass Resolution Setting
                                      description: "Mass resolution mode(s) used in
                                        this procedure. Sector-field instruments allow
                                        selection of low resolution (LR; m/\u0394m
                                        \u2248 300\u2013400), medium resolution (MR;
                                        m/\u0394m \u2248 2500\u20135000), or high
                                        resolution (HR; m/\u0394m \u2248 10,000).
                                        Multi-resolution procedures assign individual
                                        analytes to specific modes (documented in
                                        Group 4 under Mass Resolution Assignment).
                                        Procedure registers the mode(s) in use; analyst
                                        confirms at session start."
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/solutionSficpmsTAPP/massResolutionSetting
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/solutionSficpmsTAPP/massResolutionSetting
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
                                          const: ada:parameter/solutionSficpmsTAPP/memoryEffectMitigation
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/solutionSficpmsTAPP/memoryEffectMitigation
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
                                schema:identifier:
                                  description: Serial number or laboratory-internal
                                    identifier for the specific instrument unit. Supports
                                    traceability to instrument service records.
                                  anyOf:
                                  - type: string
                                  - type: array
                                    items:
                                      type: string
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
                            - title: Normalization / Standards-Based Correction
                              description: Post-acquisition normalization applied
                                to output concentrations relative to a reference value
                                (e.g., correction to a BHVO-2 working value).
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionSficpmsTAPP/normalizationStandardsBasedCorrection
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionSficpmsTAPP/normalizationStandardsBasedCorrection
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
                            - title: Pulse/Analog Detector Nonlinearity Correction
                              description: Whether a correction was applied for nonlinear
                                detector response at the transition between pulse-counting
                                and analog (and Faraday, for triple-mode instruments)
                                detection modes. For SF-ICP-MS instruments, the signal
                                transitions between pulse counting (low concentrations)
                                and analog detection (high concentrations). For triple-mode
                                instruments (e.g., Thermo Element XR), an additional
                                transition to Faraday cup detection occurs at the
                                highest signal intensities. Cross-calibration factors
                                between detector modes must be confirmed, typically
                                measured each session.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionSficpmsTAPP/pulseAnalogDetectorNonlinearityCorrection
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionSficpmsTAPP/pulseAnalogDetectorNonlinearityCorrection
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
                            - title: Spike / Outlier Filtering Approach
                              description: Criteria used to identify and exclude anomalous
                                replicate measurements or data points from the calculated
                                mean.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionSficpmsTAPP/spikeOutlierFilteringApproach
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionSficpmsTAPP/spikeOutlierFilteringApproach
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
                                  const: ada:parameter/solutionSficpmsTAPP/uncertaintyPropagationMethod
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionSficpmsTAPP/uncertaintyPropagationMethod
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
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Analysis_constantsReferenceValues
                          allOf:
                          - contains:
                              title: Normalization / Standards-Based Correction
                              description: Post-acquisition normalization applied
                                to output concentrations relative to a reference value
                                (e.g., correction to a BHVO-2 working value).
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionSficpmsTAPP/normalizationStandardsBasedCorrection
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionSficpmsTAPP/normalizationStandardsBasedCorrection
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
                              title: Pulse/Analog Detector Nonlinearity Correction
                              description: Whether a correction was applied for nonlinear
                                detector response at the transition between pulse-counting
                                and analog (and Faraday, for triple-mode instruments)
                                detection modes. For SF-ICP-MS instruments, the signal
                                transitions between pulse counting (low concentrations)
                                and analog detection (high concentrations). For triple-mode
                                instruments (e.g., Thermo Element XR), an additional
                                transition to Faraday cup detection occurs at the
                                highest signal intensities. Cross-calibration factors
                                between detector modes must be confirmed, typically
                                measured each session.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionSficpmsTAPP/pulseAnalogDetectorNonlinearityCorrection
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionSficpmsTAPP/pulseAnalogDetectorNonlinearityCorrection
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
                              title: Spike / Outlier Filtering Approach
                              description: Criteria used to identify and exclude anomalous
                                replicate measurements or data points from the calculated
                                mean.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionSficpmsTAPP/spikeOutlierFilteringApproach
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionSficpmsTAPP/spikeOutlierFilteringApproach
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
                                  const: ada:parameter/solutionSficpmsTAPP/uncertaintyPropagationMethod
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionSficpmsTAPP/uncertaintyPropagationMethod
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
              anyOf:
              - title: Signal Integration Time
                description: Total integration time per analyte per replicate (s).
                  Determined at analysis time from the actual acquisition.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/solutionSficpmsTAPP/signalIntegrationTime
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/solutionSficpmsTAPP/signalIntegrationTime
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
                    const: ada:parameter/solutionSficpmsTAPP/signalIntegrationTime
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/solutionSficpmsTAPP/signalIntegrationTime
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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-SF-ICPMS/detail/context.jsonld)

## Sources

* [Solution_SF-ICP-MS_TAPP_v5.xlsx (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/Solution-SF-ICPMS/detail`

