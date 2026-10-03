
# Solution MC-ICP-MS Analysis Detail (Schema)

`ogch.techniqueProfile.geochemProfile.Solution-MC-ICPMS.detail` *v0.1*

Dataset-level analysis-instance detail for solution MC-ICP-MS, reusing CDIF/schema.org slots on the schema:Dataset root.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### detail example P0
detail instance derived from Budde+etal2016 | Neptune Plus | IfP Münster.
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
      "@id": "ex:solutionMcicpmsTAPP-P0",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Three matrix separates, six chondrule fractions (C2, C3, C4; C3m, C3i, C3n) and two bulk rock samples of Allende; BHVO-2",
  "ada:samplingUnitName": "Labelled within Allende: bulk \"MS-A\", \"MS-B\"; matrix \"M1\", \"M2\", \"M3\"; chondrules \"C1\", \"C2\", \"C3m\", \"C3n\", \"C3i\", \"C4\" (Table 1, p.3). \"C3b\" and \"C2–C4c\" in the same table are weighted means, not units. BHVO-2 by name only",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:deltaOrEpsilonValueReferenceStandard": "Mo: Alfa Aesar Mo solution standard — mean of bracketing runs",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "Mo: 0.7–1.2 ng — 'negligible, given that several hundred ng of Mo were analyzed for each sample'",
  "ada:analysisInclusionAndRejectionCriteria": "Partially — \"For samples analyzed several times, reported values represent the mean of pooled solution replicates\". No acceptance or rejection rule stated",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:combinedResults": "per-sample means where N > 1 (Table 1, 'N: number of analyses'); chondrule fraction C3 (C3m, C3n, C3i); chondrule fractions combined (C2, C3m, C3n, C3i, C4) — Table 1 and notes b, c",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "BHVO-2 [all: ±0.14 (ε97Mo) to ±0.39 (ε92Mo), 2 s.d., n = 24] — external reproducibility (§2, Table S2); Ba by TIMS ±0.13–0.31 (n = 14)",
  "ada:analyticalAccuracyAndAssessmentMethod": "BHVO-2 [all: εⁱMo indistinguishable from the Alfa Aesar standard] — §2",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock"
        }
      ],
      "schema:name": "Number of Cycles per Block",
      "schema:value": "all: 100 isotope ratio measurements, preceded by 40 baseline integrations — §2"
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio"
        }
      ],
      "schema:name": "Double-Spike Mixing Ratio",
      "schema:value": "N/A — no double spike used"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/detail/context.jsonld",
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
      "@id": "ex:solutionMcicpmsTAPP-P0",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Three matrix separates, six chondrule fractions (C2, C3, C4; C3m, C3i, C3n) and two bulk rock samples of Allende; BHVO-2",
  "ada:samplingUnitName": "Labelled within Allende: bulk \"MS-A\", \"MS-B\"; matrix \"M1\", \"M2\", \"M3\"; chondrules \"C1\", \"C2\", \"C3m\", \"C3n\", \"C3i\", \"C4\" (Table 1, p.3). \"C3b\" and \"C2\u2013C4c\" in the same table are weighted means, not units. BHVO-2 by name only",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:deltaOrEpsilonValueReferenceStandard": "Mo: Alfa Aesar Mo solution standard \u2014 mean of bracketing runs",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "Mo: 0.7\u20131.2 ng \u2014 'negligible, given that several hundred ng of Mo were analyzed for each sample'",
  "ada:analysisInclusionAndRejectionCriteria": "Partially \u2014 \"For samples analyzed several times, reported values represent the mean of pooled solution replicates\". No acceptance or rejection rule stated",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:combinedResults": "per-sample means where N > 1 (Table 1, 'N: number of analyses'); chondrule fraction C3 (C3m, C3n, C3i); chondrule fractions combined (C2, C3m, C3n, C3i, C4) \u2014 Table 1 and notes b, c",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "BHVO-2 [all: \u00b10.14 (\u03b597Mo) to \u00b10.39 (\u03b592Mo), 2 s.d., n = 24] \u2014 external reproducibility (\u00a72, Table S2); Ba by TIMS \u00b10.13\u20130.31 (n = 14)",
  "ada:analyticalAccuracyAndAssessmentMethod": "BHVO-2 [all: \u03b5\u2071Mo indistinguishable from the Alfa Aesar standard] \u2014 \u00a72",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock"
        }
      ],
      "schema:name": "Number of Cycles per Block",
      "schema:value": "all: 100 isotope ratio measurements, preceded by 40 baseline integrations \u2014 \u00a72"
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio"
        }
      ],
      "schema:name": "Double-Spike Mixing Ratio",
      "schema:value": "N/A \u2014 no double spike used"
    }
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-P0> a ada:SolutionICPMSTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio>,
        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock> ;
    schema1:measurementTechnique <ex:solutionMcicpmsTAPP-P0> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially — \"For samples analyzed several times, reported values represent the mean of pooled solution replicates\". No acceptance or rejection rule stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "BHVO-2 [all: εⁱMo indistinguishable from the Alfa Aesar standard] — §2" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "BHVO-2 [all: ±0.14 (ε97Mo) to ±0.39 (ε92Mo), 2 s.d., n = 24] — external reproducibility (§2, Table S2); Ba by TIMS ±0.13–0.31 (n = 14)" ;
    ada:combinedResults "per-sample means where N > 1 (Table 1, 'N: number of analyses'); chondrule fraction C3 (C3m, C3n, C3i); chondrule fractions combined (C2, C3m, C3n, C3i, C4) — Table 1 and notes b, c" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:deltaOrEpsilonValueReferenceStandard "Mo: Alfa Aesar Mo solution standard — mean of bracketing runs" ;
    ada:detectionLimit -9999 ;
    ada:errorCorrelationBetweenReportedQuantities -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:oxideProduction "missing" ;
    ada:peakFlatness "missing" ;
    ada:proceduralBlankLevel "Mo: 0.7–1.2 ng — 'negligible, given that several hundred ng of Mo were analyzed for each sample'" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "Three matrix separates, six chondrule fractions (C2, C3, C4; C3m, C3i, C3n) and two bulk rock samples of Allende; BHVO-2" ;
    ada:samplingUnitName "Labelled within Allende: bulk \"MS-A\", \"MS-B\"; matrix \"M1\", \"M2\", \"M3\"; chondrules \"C1\", \"C2\", \"C3m\", \"C3n\", \"C3i\", \"C4\" (Table 1, p.3). \"C3b\" and \"C2–C4c\" in the same table are weighted means, not units. BHVO-2 by name only" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<ex:solutionMcicpmsTAPP-P0> schema1:identifier "missing" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio> a schema1:PropertyValue ;
    schema1:name "Double-Spike Mixing Ratio" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio> ;
    schema1:value "N/A — no double spike used" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock> a schema1:PropertyValue ;
    schema1:name "Number of Cycles per Block" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock> ;
    schema1:value "all: 100 isotope ratio measurements, preceded by 40 baseline integrations — §2" .


```


### detail example P1
detail instance derived from Craddock+etal2008 | Thermo NEPTUNE | WHOI.
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
      "@id": "ex:solutionMcicpmsTAPP-P1",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "IAEA-S-1, S-2, S-4, NBS-123; in-house standards S_Alfa and S_Spex; anhydrite mineral standard Sch-M-2; pyrite FVG-1",
  "ada:samplingUnitName": "Sample name only — Table 3 lists \"IAEA-S-1\", \"IAEA-S-2\", \"IAEA-S-4\", \"NBS-123\" and the in-house standards Alfa and Spex (p.4); replicates are counted (\"# of replicates\"), not labelled",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:deltaOrEpsilonValueReferenceStandard": "S: V-CDT, through in-house S_Spex and S_Alfa calibrated against IAEA-S-1 (δ34S = −0.3‰) — §2.4",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "S: ~0.05% (~0.25 µg per 500 µg S) — §2.2",
  "ada:analysisInclusionAndRejectionCriteria": "Rule: data showing mass-bias drift greater than ~0.5‰ during an individual sample are discarded; no count stated — 'Data that show clear and large mass bias drift (greater than ∼0.5‰) during individual samples should be discarded'",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:combinedResults": "the reference materials and in-house standards of Table 3, each over its stated number of replicates (3–20) — Table 3",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "Alfa [δ34S: ±0.21‰, 2σ, 20–30 replicates]; Sch-M-2 [δ34S: ±0.45‰, 2σ, 12 replicates, laser] — §3.2; S_Spex ±0.18‰; δ³³S an order of magnitude worse",
  "ada:analyticalAccuracyAndAssessmentMethod": "IAEA-S-1, IAEA-S-2, IAEA-S-4, NBS-123 [δ34S: consistent with published consensus values within uncertainty] — §2.4, Table 3",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "δ34S, δ33S: two standard deviations of the replicates — Table 3 note",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock"
        }
      ],
      "schema:name": "Number of Cycles per Block",
      "schema:value": "all: 20 cycles — Table 1, §2.4"
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio"
        }
      ],
      "schema:name": "Double-Spike Mixing Ratio",
      "schema:value": "N/A — no double spike used"
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/spikeOutlierFilteringApproach",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/spikeOutlierFilteringApproach"
        }
      ],
      "schema:name": "Spike / Outlier Filtering Approach",
      "schema:value": "None, no automatic 2σ rejection of outlying cycles — 'Automatic rejection of outlying cycles (2σ outlier criterion) offered within the NEPTUNE software is not performed' (§2.4)"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/detail/context.jsonld",
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
      "@id": "ex:solutionMcicpmsTAPP-P1",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "IAEA-S-1, S-2, S-4, NBS-123; in-house standards S_Alfa and S_Spex; anhydrite mineral standard Sch-M-2; pyrite FVG-1",
  "ada:samplingUnitName": "Sample name only \u2014 Table 3 lists \"IAEA-S-1\", \"IAEA-S-2\", \"IAEA-S-4\", \"NBS-123\" and the in-house standards Alfa and Spex (p.4); replicates are counted (\"# of replicates\"), not labelled",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:deltaOrEpsilonValueReferenceStandard": "S: V-CDT, through in-house S_Spex and S_Alfa calibrated against IAEA-S-1 (\u03b434S = \u22120.3\u2030) \u2014 \u00a72.4",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "S: ~0.05% (~0.25 \u00b5g per 500 \u00b5g S) \u2014 \u00a72.2",
  "ada:analysisInclusionAndRejectionCriteria": "Rule: data showing mass-bias drift greater than ~0.5\u2030 during an individual sample are discarded; no count stated \u2014 'Data that show clear and large mass bias drift (greater than \u223c0.5\u2030) during individual samples should be discarded'",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:combinedResults": "the reference materials and in-house standards of Table 3, each over its stated number of replicates (3\u201320) \u2014 Table 3",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "Alfa [\u03b434S: \u00b10.21\u2030, 2\u03c3, 20\u201330 replicates]; Sch-M-2 [\u03b434S: \u00b10.45\u2030, 2\u03c3, 12 replicates, laser] \u2014 \u00a73.2; S_Spex \u00b10.18\u2030; \u03b4\u00b3\u00b3S an order of magnitude worse",
  "ada:analyticalAccuracyAndAssessmentMethod": "IAEA-S-1, IAEA-S-2, IAEA-S-4, NBS-123 [\u03b434S: consistent with published consensus values within uncertainty] \u2014 \u00a72.4, Table 3",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "\u03b434S, \u03b433S: two standard deviations of the replicates \u2014 Table 3 note",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock"
        }
      ],
      "schema:name": "Number of Cycles per Block",
      "schema:value": "all: 20 cycles \u2014 Table 1, \u00a72.4"
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio"
        }
      ],
      "schema:name": "Double-Spike Mixing Ratio",
      "schema:value": "N/A \u2014 no double spike used"
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/spikeOutlierFilteringApproach",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/spikeOutlierFilteringApproach"
        }
      ],
      "schema:name": "Spike / Outlier Filtering Approach",
      "schema:value": "None, no automatic 2\u03c3 rejection of outlying cycles \u2014 'Automatic rejection of outlying cycles (2\u03c3 outlier criterion) offered within the NEPTUNE software is not performed' (\u00a72.4)"
    }
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-P1> a ada:SolutionICPMSTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio>,
        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock>,
        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/spikeOutlierFilteringApproach> ;
    schema1:measurementTechnique <ex:solutionMcicpmsTAPP-P1> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Rule: data showing mass-bias drift greater than ~0.5‰ during an individual sample are discarded; no count stated — 'Data that show clear and large mass bias drift (greater than ∼0.5‰) during individual samples should be discarded'" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "IAEA-S-1, IAEA-S-2, IAEA-S-4, NBS-123 [δ34S: consistent with published consensus values within uncertainty] — §2.4, Table 3" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "Alfa [δ34S: ±0.21‰, 2σ, 20–30 replicates]; Sch-M-2 [δ34S: ±0.45‰, 2σ, 12 replicates, laser] — §3.2; S_Spex ±0.18‰; δ³³S an order of magnitude worse" ;
    ada:combinedResults "the reference materials and in-house standards of Table 3, each over its stated number of replicates (3–20) — Table 3" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:deltaOrEpsilonValueReferenceStandard "S: V-CDT, through in-house S_Spex and S_Alfa calibrated against IAEA-S-1 (δ34S = −0.3‰) — §2.4" ;
    ada:detectionLimit -9999 ;
    ada:errorCorrelationBetweenReportedQuantities -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "δ34S, δ33S: two standard deviations of the replicates — Table 3 note" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:oxideProduction "missing" ;
    ada:peakFlatness "missing" ;
    ada:proceduralBlankLevel "S: ~0.05% (~0.25 µg per 500 µg S) — §2.2" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "IAEA-S-1, S-2, S-4, NBS-123; in-house standards S_Alfa and S_Spex; anhydrite mineral standard Sch-M-2; pyrite FVG-1" ;
    ada:samplingUnitName "Sample name only — Table 3 lists \"IAEA-S-1\", \"IAEA-S-2\", \"IAEA-S-4\", \"NBS-123\" and the in-house standards Alfa and Spex (p.4); replicates are counted (\"# of replicates\"), not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<ex:solutionMcicpmsTAPP-P1> schema1:identifier "missing" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio> a schema1:PropertyValue ;
    schema1:name "Double-Spike Mixing Ratio" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio> ;
    schema1:value "N/A — no double spike used" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock> a schema1:PropertyValue ;
    schema1:name "Number of Cycles per Block" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock> ;
    schema1:value "all: 20 cycles — Table 1, §2.4" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/spikeOutlierFilteringApproach> a schema1:PropertyValue ;
    schema1:name "Spike / Outlier Filtering Approach" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/spikeOutlierFilteringApproach> ;
    schema1:value "None, no automatic 2σ rejection of outlying cycles — 'Automatic rejection of outlying cycles (2σ outlier criterion) offered within the NEPTUNE software is not performed' (§2.4)" .


```


### detail example P2
detail instance derived from Hopp+etal2021 | Neptune (Plus spec) | Univ Chicago.
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
      "@id": "ex:solutionMcicpmsTAPP-P2",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Toluca, Gibeon, Duchesne, Skookum, Tlacotepec and 18 further iron meteorites; BHVO-2, BCR-2; IRMM-524a",
  "ada:samplingUnitName": "Sample name only — meteorites by name, e.g. \"Toluca, Gibeon, Duchesne, Skookum, Tlacotepec\" (p.5); the digestion aliquots and ~50 mg pieces carry no labels of their own",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:deltaOrEpsilonValueReferenceStandard": "Fe: IRMM-524a — 'that has an identical isotopic composition to IRMM-014' (§2.3)",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "Fe: ~70 ng — 'negligible considering that 1-2 mg Fe was purified for each sample' (§2.2)",
  "ada:analysisInclusionAndRejectionCriteria": "Rule: samples with ε196Pt(8/5) > 0.16 are left out of the low-exposure group averages; four samples excluded — 'we, therefore, excluded four samples that have ε196Pt(8/5) >0.16 to calculate low-exposure averages' (p.9); Table 1 note g",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:combinedResults": "per-sample averages (n = 10–35 each); IC low-exposure weighted average; IC intercept; IIAB low-exposure weighted average; IIAB intercept; IIC weighted average; IID low-exposure weighted average; IIIAB weighted average; IVA weighted average; IVB weighted average — Table 1",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "BHVO-2, BCR-2 [\"μ54Fe(7/6)\": average 2 ± 2 (95% c.i.); \"μ58Fe(7/6)\": average 4 ± 6 (95% c.i.); other: normal within uncertainties] — §3; agreeing with Schiller et al. (2020)",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock"
        }
      ],
      "schema:name": "Number of Cycles per Block",
      "schema:value": "HR: 25 cycles; MR: 50 cycles — §2.3"
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio"
        }
      ],
      "schema:name": "Double-Spike Mixing Ratio",
      "schema:value": "N/A — no double spike used"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/detail/context.jsonld",
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
      "@id": "ex:solutionMcicpmsTAPP-P2",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Toluca, Gibeon, Duchesne, Skookum, Tlacotepec and 18 further iron meteorites; BHVO-2, BCR-2; IRMM-524a",
  "ada:samplingUnitName": "Sample name only \u2014 meteorites by name, e.g. \"Toluca, Gibeon, Duchesne, Skookum, Tlacotepec\" (p.5); the digestion aliquots and ~50 mg pieces carry no labels of their own",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:deltaOrEpsilonValueReferenceStandard": "Fe: IRMM-524a \u2014 'that has an identical isotopic composition to IRMM-014' (\u00a72.3)",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "Fe: ~70 ng \u2014 'negligible considering that 1-2 mg Fe was purified for each sample' (\u00a72.2)",
  "ada:analysisInclusionAndRejectionCriteria": "Rule: samples with \u03b5196Pt(8/5) > 0.16 are left out of the low-exposure group averages; four samples excluded \u2014 'we, therefore, excluded four samples that have \u03b5196Pt(8/5) >0.16 to calculate low-exposure averages' (p.9); Table 1 note g",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:combinedResults": "per-sample averages (n = 10\u201335 each); IC low-exposure weighted average; IC intercept; IIAB low-exposure weighted average; IIAB intercept; IIC weighted average; IID low-exposure weighted average; IIIAB weighted average; IVA weighted average; IVB weighted average \u2014 Table 1",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "BHVO-2, BCR-2 [\"\u03bc54Fe(7/6)\": average 2 \u00b1 2 (95% c.i.); \"\u03bc58Fe(7/6)\": average 4 \u00b1 6 (95% c.i.); other: normal within uncertainties] \u2014 \u00a73; agreeing with Schiller et al. (2020)",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock"
        }
      ],
      "schema:name": "Number of Cycles per Block",
      "schema:value": "HR: 25 cycles; MR: 50 cycles \u2014 \u00a72.3"
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio"
        }
      ],
      "schema:name": "Double-Spike Mixing Ratio",
      "schema:value": "N/A \u2014 no double spike used"
    }
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-P2> a ada:SolutionICPMSTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio>,
        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock> ;
    schema1:measurementTechnique <ex:solutionMcicpmsTAPP-P2> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Rule: samples with ε196Pt(8/5) > 0.16 are left out of the low-exposure group averages; four samples excluded — 'we, therefore, excluded four samples that have ε196Pt(8/5) >0.16 to calculate low-exposure averages' (p.9); Table 1 note g" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "BHVO-2, BCR-2 [\"μ54Fe(7/6)\": average 2 ± 2 (95% c.i.); \"μ58Fe(7/6)\": average 4 ± 6 (95% c.i.); other: normal within uncertainties] — §3; agreeing with Schiller et al. (2020)" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:combinedResults "per-sample averages (n = 10–35 each); IC low-exposure weighted average; IC intercept; IIAB low-exposure weighted average; IIAB intercept; IIC weighted average; IID low-exposure weighted average; IIIAB weighted average; IVA weighted average; IVB weighted average — Table 1" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:deltaOrEpsilonValueReferenceStandard "Fe: IRMM-524a — 'that has an identical isotopic composition to IRMM-014' (§2.3)" ;
    ada:detectionLimit -9999 ;
    ada:errorCorrelationBetweenReportedQuantities -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:oxideProduction "missing" ;
    ada:peakFlatness "missing" ;
    ada:proceduralBlankLevel "Fe: ~70 ng — 'negligible considering that 1-2 mg Fe was purified for each sample' (§2.2)" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "Toluca, Gibeon, Duchesne, Skookum, Tlacotepec and 18 further iron meteorites; BHVO-2, BCR-2; IRMM-524a" ;
    ada:samplingUnitName "Sample name only — meteorites by name, e.g. \"Toluca, Gibeon, Duchesne, Skookum, Tlacotepec\" (p.5); the digestion aliquots and ~50 mg pieces carry no labels of their own" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<ex:solutionMcicpmsTAPP-P2> schema1:identifier "missing" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio> a schema1:PropertyValue ;
    schema1:name "Double-Spike Mixing Ratio" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio> ;
    schema1:value "N/A — no double spike used" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock> a schema1:PropertyValue ;
    schema1:name "Number of Cycles per Block" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock> ;
    schema1:value "HR: 25 cycles; MR: 50 cycles — §2.3" .


```


### detail example P3
detail instance derived from Hu+etal2022 | Neptune Plus | Univ Chicago.
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
      "@id": "ex:solutionMcicpmsTAPP-P3",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Group II CAIs including FG-FT-4, FG-FT-8 and FG-FT-9",
  "ada:samplingUnitName": "Labelled: each CAI by name under its specimen number — Table 1's \"Sample\" and \"CAI name\" columns give e.g. ME-3364-25.2 \"FG-FT-3\", ME-2639-16.2 \"FG-FT-4\", AL3S5 \"FG-FT-8\", AL4S6 \"FG-FT-9\", AL8S2 \"FG-FT-10\" (p.3); † marks a second analysis of FG-FT-4, -8 and -9. BCR-2 by name only",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:deltaOrEpsilonValueReferenceStandard": "Ce, Nd, Sm, Eu, Gd, Dy, Er, Yb: OL-REE series — prepared in-house from high-purity ESPI oxide powders",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "Ce, Nd, Sm, Eu, Gd, Dy, Er, Yb: < 0.25 ng — 'negligible compared to the amounts of REEs in the samples'",
  "ada:analysisInclusionAndRejectionCriteria": "Partially — \"On average, LREEs were measured nine times\"; replicate matrix cuts were measured but \"are not used, however, for data interpretation to avoid unnecessary influence of stable isotopic fractionation potentially induced by Mo chemistry\" — an explicit exclusion, on chemical rather than statistical grounds",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:combinedResults": "per-CAI values (1 to 12 bracketings each); mean of the seven CAIs — Table 1; Fig. 1",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "BCR-2 [all: zero within error bars, typically < 0.05‰/amu] — Assessment of data accuracy; replicates from the Mo-chemistry matrix cut agree, with LREEs shifted ~0.1‰/amu",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock"
        }
      ],
      "schema:name": "Number of Cycles per Block",
      "schema:value": "main configuration: 40 cycles; subconfiguration: 2, measured at the beginning — Materials and Methods"
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio"
        }
      ],
      "schema:name": "Double-Spike Mixing Ratio",
      "schema:value": "N/A — no double spike used"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/detail/context.jsonld",
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
      "@id": "ex:solutionMcicpmsTAPP-P3",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Group II CAIs including FG-FT-4, FG-FT-8 and FG-FT-9",
  "ada:samplingUnitName": "Labelled: each CAI by name under its specimen number \u2014 Table 1's \"Sample\" and \"CAI name\" columns give e.g. ME-3364-25.2 \"FG-FT-3\", ME-2639-16.2 \"FG-FT-4\", AL3S5 \"FG-FT-8\", AL4S6 \"FG-FT-9\", AL8S2 \"FG-FT-10\" (p.3); \u2020 marks a second analysis of FG-FT-4, -8 and -9. BCR-2 by name only",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:deltaOrEpsilonValueReferenceStandard": "Ce, Nd, Sm, Eu, Gd, Dy, Er, Yb: OL-REE series \u2014 prepared in-house from high-purity ESPI oxide powders",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "Ce, Nd, Sm, Eu, Gd, Dy, Er, Yb: < 0.25 ng \u2014 'negligible compared to the amounts of REEs in the samples'",
  "ada:analysisInclusionAndRejectionCriteria": "Partially \u2014 \"On average, LREEs were measured nine times\"; replicate matrix cuts were measured but \"are not used, however, for data interpretation to avoid unnecessary influence of stable isotopic fractionation potentially induced by Mo chemistry\" \u2014 an explicit exclusion, on chemical rather than statistical grounds",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:combinedResults": "per-CAI values (1 to 12 bracketings each); mean of the seven CAIs \u2014 Table 1; Fig. 1",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "BCR-2 [all: zero within error bars, typically < 0.05\u2030/amu] \u2014 Assessment of data accuracy; replicates from the Mo-chemistry matrix cut agree, with LREEs shifted ~0.1\u2030/amu",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock"
        }
      ],
      "schema:name": "Number of Cycles per Block",
      "schema:value": "main configuration: 40 cycles; subconfiguration: 2, measured at the beginning \u2014 Materials and Methods"
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio"
        }
      ],
      "schema:name": "Double-Spike Mixing Ratio",
      "schema:value": "N/A \u2014 no double spike used"
    }
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-P3> a ada:SolutionICPMSTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio>,
        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock> ;
    schema1:measurementTechnique <ex:solutionMcicpmsTAPP-P3> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially — \"On average, LREEs were measured nine times\"; replicate matrix cuts were measured but \"are not used, however, for data interpretation to avoid unnecessary influence of stable isotopic fractionation potentially induced by Mo chemistry\" — an explicit exclusion, on chemical rather than statistical grounds" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "BCR-2 [all: zero within error bars, typically < 0.05‰/amu] — Assessment of data accuracy; replicates from the Mo-chemistry matrix cut agree, with LREEs shifted ~0.1‰/amu" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:combinedResults "per-CAI values (1 to 12 bracketings each); mean of the seven CAIs — Table 1; Fig. 1" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:deltaOrEpsilonValueReferenceStandard "Ce, Nd, Sm, Eu, Gd, Dy, Er, Yb: OL-REE series — prepared in-house from high-purity ESPI oxide powders" ;
    ada:detectionLimit -9999 ;
    ada:errorCorrelationBetweenReportedQuantities -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:oxideProduction "missing" ;
    ada:peakFlatness "missing" ;
    ada:proceduralBlankLevel "Ce, Nd, Sm, Eu, Gd, Dy, Er, Yb: < 0.25 ng — 'negligible compared to the amounts of REEs in the samples'" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "Group II CAIs including FG-FT-4, FG-FT-8 and FG-FT-9" ;
    ada:samplingUnitName "Labelled: each CAI by name under its specimen number — Table 1's \"Sample\" and \"CAI name\" columns give e.g. ME-3364-25.2 \"FG-FT-3\", ME-2639-16.2 \"FG-FT-4\", AL3S5 \"FG-FT-8\", AL4S6 \"FG-FT-9\", AL8S2 \"FG-FT-10\" (p.3); † marks a second analysis of FG-FT-4, -8 and -9. BCR-2 by name only" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<ex:solutionMcicpmsTAPP-P3> schema1:identifier "missing" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio> a schema1:PropertyValue ;
    schema1:name "Double-Spike Mixing Ratio" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio> ;
    schema1:value "N/A — no double spike used" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock> a schema1:PropertyValue ;
    schema1:name "Number of Cycles per Block" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock> ;
    schema1:value "main configuration: 40 cycles; subconfiguration: 2, measured at the beginning — Materials and Methods" .


```


### detail example Tissot2020
detail instance derived from IbanezMejia+Tissot2020 | Nu Plasma II | MIT.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Tissot2020",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionMcicpmsTAPP-Tissot2020",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "FC-1 zircon and baddeleyite crystals; ZrNIST reference solution",
  "ada:samplingUnitName": "Labelled: single crystals of FC-1 — zircons \"z1\"–\"z16\" with \"3_z…\" and \"4_z…\" series (e.g. \"4_z15R\", \"4_z17\"), baddeleyites \"b1\"–\"b8\" with \"3_b…\" and \"4_b…\" series, and bulk rock \"WR1\" (Table 1, pp.4–6); \"CA\"/\"Untr.\" beside each label marks chemical abrasion, not identity",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:deltaOrEpsilonValueReferenceStandard": "Zr: ZrNIST — a NIST gravimetric Zr solution being calibrated as an isotopic reference material",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "N — the blank comparison stated concerns non-radiogenic Pb in the U-Pb work",
  "ada:analysisInclusionAndRejectionCriteria": "Partially — Table 1 records \"Number of times the same purified Zr solution was measured independently in the MC-ICP-MS\" and \"Reported values are weighted means of all replicate\" analyses. No rejection rule stated",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:combinedResults": "each FC-1 zircon and baddeleyite fraction, over its replicates — Table 1, 'Replicates': 'Number of times the same purified Zr solution was measured independently'",
  "ada:countingStatisticsError": "N — the internal counting-statistics uncertainty is used for comparison but not tabulated",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "all: internal uncertainty from counting statistics — similar in magnitude to or slightly smaller than the external reproducibility assigned to each determination",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "ZrNIST [all: 2σ external reproducibility of the spiked ZrNIST measurements in each run]",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock"
        }
      ],
      "schema:name": "Number of Cycles per Block",
      "schema:value": "all: 50 cycles"
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio"
        }
      ],
      "schema:name": "Double-Spike Mixing Ratio",
      "schema:value": "0.43:0.57 spike-to-sample Zr mass ratio, described as optimal"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Tissot2020",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionMcicpmsTAPP-Tissot2020",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "FC-1 zircon and baddeleyite crystals; ZrNIST reference solution",
  "ada:samplingUnitName": "Labelled: single crystals of FC-1 \u2014 zircons \"z1\"\u2013\"z16\" with \"3_z\u2026\" and \"4_z\u2026\" series (e.g. \"4_z15R\", \"4_z17\"), baddeleyites \"b1\"\u2013\"b8\" with \"3_b\u2026\" and \"4_b\u2026\" series, and bulk rock \"WR1\" (Table 1, pp.4\u20136); \"CA\"/\"Untr.\" beside each label marks chemical abrasion, not identity",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:deltaOrEpsilonValueReferenceStandard": "Zr: ZrNIST \u2014 a NIST gravimetric Zr solution being calibrated as an isotopic reference material",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "N \u2014 the blank comparison stated concerns non-radiogenic Pb in the U-Pb work",
  "ada:analysisInclusionAndRejectionCriteria": "Partially \u2014 Table 1 records \"Number of times the same purified Zr solution was measured independently in the MC-ICP-MS\" and \"Reported values are weighted means of all replicate\" analyses. No rejection rule stated",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:combinedResults": "each FC-1 zircon and baddeleyite fraction, over its replicates \u2014 Table 1, 'Replicates': 'Number of times the same purified Zr solution was measured independently'",
  "ada:countingStatisticsError": "N \u2014 the internal counting-statistics uncertainty is used for comparison but not tabulated",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "all: internal uncertainty from counting statistics \u2014 similar in magnitude to or slightly smaller than the external reproducibility assigned to each determination",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "ZrNIST [all: 2\u03c3 external reproducibility of the spiked ZrNIST measurements in each run]",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock"
        }
      ],
      "schema:name": "Number of Cycles per Block",
      "schema:value": "all: 50 cycles"
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio"
        }
      ],
      "schema:name": "Double-Spike Mixing Ratio",
      "schema:value": "0.43:0.57 spike-to-sample Zr mass ratio, described as optimal"
    }
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Tissot2020> a ada:SolutionICPMSTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio>,
        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock> ;
    schema1:measurementTechnique <ex:solutionMcicpmsTAPP-Tissot2020> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially — Table 1 records \"Number of times the same purified Zr solution was measured independently in the MC-ICP-MS\" and \"Reported values are weighted means of all replicate\" analyses. No rejection rule stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "missing" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:combinedResults "each FC-1 zircon and baddeleyite fraction, over its replicates — Table 1, 'Replicates': 'Number of times the same purified Zr solution was measured independently'" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "N — the internal counting-statistics uncertainty is used for comparison but not tabulated" ;
    ada:deltaOrEpsilonValueReferenceStandard "Zr: ZrNIST — a NIST gravimetric Zr solution being calibrated as an isotopic reference material" ;
    ada:detectionLimit -9999 ;
    ada:errorCorrelationBetweenReportedQuantities -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "all: internal uncertainty from counting statistics — similar in magnitude to or slightly smaller than the external reproducibility assigned to each determination" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:oxideProduction "missing" ;
    ada:peakFlatness "missing" ;
    ada:proceduralBlankLevel "N — the blank comparison stated concerns non-radiogenic Pb in the U-Pb work" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "FC-1 zircon and baddeleyite crystals; ZrNIST reference solution" ;
    ada:samplingUnitName "Labelled: single crystals of FC-1 — zircons \"z1\"–\"z16\" with \"3_z…\" and \"4_z…\" series (e.g. \"4_z15R\", \"4_z17\"), baddeleyites \"b1\"–\"b8\" with \"3_b…\" and \"4_b…\" series, and bulk rock \"WR1\" (Table 1, pp.4–6); \"CA\"/\"Untr.\" beside each label marks chemical abrasion, not identity" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "ZrNIST [all: 2σ external reproducibility of the spiked ZrNIST measurements in each run]" .

<ex:solutionMcicpmsTAPP-Tissot2020> schema1:identifier "missing" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio> a schema1:PropertyValue ;
    schema1:name "Double-Spike Mixing Ratio" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio> ;
    schema1:value "0.43:0.57 spike-to-sample Zr mass ratio, described as optimal" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock> a schema1:PropertyValue ;
    schema1:name "Number of Cycles per Block" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock> ;
    schema1:value "all: 50 cycles" .


```


### detail example Dauphas2019
detail instance derived from Nie+Dauphas2019 | Neptune | Univ Chicago.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Dauphas2019",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionMcicpmsTAPP-Dauphas2019",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "BHVO-2, BCR-2, BE-N, W-2, AGV-2, GSR-1, GS-N, G-A, G-3; DTS-2b and PCC-1 synthetic mixes; Allende; NIST SRM984",
  "ada:samplingUnitName": "Labelled for the lunar rocks by Apollo sample and split number: \"12002.613\", \"12018.301\", \"12052.353\", \"10017.413\", \"74275.361\", \"77215.276\" (Table 1, p.2), the last a \"white-colored fragment\"; terrestrial rocks by name only (BCR-2, BHVO-2 …)",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:deltaOrEpsilonValueReferenceStandard": "Rb: NIST SRM984",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "Rb: ~0.14 ng — less than 0.5% of the Rb of a typical sample (40 ng)",
  "ada:analysisInclusionAndRejectionCriteria": "Rule: the norite is left out of the bulk-Moon regression for its very light Rb isotopic composition — Fig. 1 caption: 'excluded from the regression due to its very light Rb isotopic composition (this sample is heterogeneous ...)'",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:combinedResults": "per-sample averages (5–12 measurements each); bulk Moon δ87Rb (+0.03 ± 0.03‰); bulk Earth δ87Rb (−0.13 ± 0.01‰) — Table 1; Fig. 1 caption",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "SRM984 as a sample, DTS-2b + SRM984, PCC-1 + SRM984 [δ87Rb: zero within error]; BHVO-2, BCR-2, BE-N, W-2, AGV-2, GSR-1, GS-N, G-A, G-3, Allende [δ87Rb: reproducible, agree with published results] — A.4, Fig. 8",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfBlocksPerMeasurement",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfBlocksPerMeasurement"
        }
      ],
      "schema:name": "Number of Blocks per Measurement",
      "schema:value": "A single block"
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock"
        }
      ],
      "schema:name": "Number of Cycles per Block",
      "schema:value": "all: 25 cycles — a single block"
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio"
        }
      ],
      "schema:name": "Double-Spike Mixing Ratio",
      "schema:value": "N/A — no double spike used"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Dauphas2019",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionMcicpmsTAPP-Dauphas2019",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "BHVO-2, BCR-2, BE-N, W-2, AGV-2, GSR-1, GS-N, G-A, G-3; DTS-2b and PCC-1 synthetic mixes; Allende; NIST SRM984",
  "ada:samplingUnitName": "Labelled for the lunar rocks by Apollo sample and split number: \"12002.613\", \"12018.301\", \"12052.353\", \"10017.413\", \"74275.361\", \"77215.276\" (Table 1, p.2), the last a \"white-colored fragment\"; terrestrial rocks by name only (BCR-2, BHVO-2 \u2026)",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:deltaOrEpsilonValueReferenceStandard": "Rb: NIST SRM984",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "Rb: ~0.14 ng \u2014 less than 0.5% of the Rb of a typical sample (40 ng)",
  "ada:analysisInclusionAndRejectionCriteria": "Rule: the norite is left out of the bulk-Moon regression for its very light Rb isotopic composition \u2014 Fig. 1 caption: 'excluded from the regression due to its very light Rb isotopic composition (this sample is heterogeneous ...)'",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:combinedResults": "per-sample averages (5\u201312 measurements each); bulk Moon \u03b487Rb (+0.03 \u00b1 0.03\u2030); bulk Earth \u03b487Rb (\u22120.13 \u00b1 0.01\u2030) \u2014 Table 1; Fig. 1 caption",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "SRM984 as a sample, DTS-2b + SRM984, PCC-1 + SRM984 [\u03b487Rb: zero within error]; BHVO-2, BCR-2, BE-N, W-2, AGV-2, GSR-1, GS-N, G-A, G-3, Allende [\u03b487Rb: reproducible, agree with published results] \u2014 A.4, Fig. 8",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfBlocksPerMeasurement",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfBlocksPerMeasurement"
        }
      ],
      "schema:name": "Number of Blocks per Measurement",
      "schema:value": "A single block"
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock"
        }
      ],
      "schema:name": "Number of Cycles per Block",
      "schema:value": "all: 25 cycles \u2014 a single block"
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio"
        }
      ],
      "schema:name": "Double-Spike Mixing Ratio",
      "schema:value": "N/A \u2014 no double spike used"
    }
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Dauphas2019> a ada:SolutionICPMSTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio>,
        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfBlocksPerMeasurement>,
        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock> ;
    schema1:measurementTechnique <ex:solutionMcicpmsTAPP-Dauphas2019> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Rule: the norite is left out of the bulk-Moon regression for its very light Rb isotopic composition — Fig. 1 caption: 'excluded from the regression due to its very light Rb isotopic composition (this sample is heterogeneous ...)'" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "SRM984 as a sample, DTS-2b + SRM984, PCC-1 + SRM984 [δ87Rb: zero within error]; BHVO-2, BCR-2, BE-N, W-2, AGV-2, GSR-1, GS-N, G-A, G-3, Allende [δ87Rb: reproducible, agree with published results] — A.4, Fig. 8" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:combinedResults "per-sample averages (5–12 measurements each); bulk Moon δ87Rb (+0.03 ± 0.03‰); bulk Earth δ87Rb (−0.13 ± 0.01‰) — Table 1; Fig. 1 caption" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:deltaOrEpsilonValueReferenceStandard "Rb: NIST SRM984" ;
    ada:detectionLimit -9999 ;
    ada:errorCorrelationBetweenReportedQuantities -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:oxideProduction "missing" ;
    ada:peakFlatness "missing" ;
    ada:proceduralBlankLevel "Rb: ~0.14 ng — less than 0.5% of the Rb of a typical sample (40 ng)" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "BHVO-2, BCR-2, BE-N, W-2, AGV-2, GSR-1, GS-N, G-A, G-3; DTS-2b and PCC-1 synthetic mixes; Allende; NIST SRM984" ;
    ada:samplingUnitName "Labelled for the lunar rocks by Apollo sample and split number: \"12002.613\", \"12018.301\", \"12052.353\", \"10017.413\", \"74275.361\", \"77215.276\" (Table 1, p.2), the last a \"white-colored fragment\"; terrestrial rocks by name only (BCR-2, BHVO-2 …)" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<ex:solutionMcicpmsTAPP-Dauphas2019> schema1:identifier "missing" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio> a schema1:PropertyValue ;
    schema1:name "Double-Spike Mixing Ratio" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio> ;
    schema1:value "N/A — no double spike used" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfBlocksPerMeasurement> a schema1:PropertyValue ;
    schema1:name "Number of Blocks per Measurement" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfBlocksPerMeasurement> ;
    schema1:value "A single block" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock> a schema1:PropertyValue ;
    schema1:name "Number of Cycles per Block" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock> ;
    schema1:value "all: 25 cycles — a single block" .


```


### detail example P6
detail instance derived from Nowell+etal2008 | Neptune | Durham AHIGL.
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
      "@id": "ex:solutionMcicpmsTAPP-P6",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "UMd, DTM, LOsST and DROsS Os isotope reference materials",
  "ada:samplingUnitName": "Labelled for LOsST only: \"LOsST 17-03-06 (Aliq 1)\" (Table 8b, p.22) — the Neptune and Nu Plasma runs \"were made on two different aliquots of the LOsST RM\" (p.24); UMd, DTM and DROsS by name and session date",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:deltaOrEpsilonValueReferenceStandard": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially — n = 45 per analysis. No rejection rule stated",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:combinedResults": "UMd and DTM per-session averages; UMd average (94 analyses); DTM average (121 analyses); stable Os ratio averages (215 analyses); LOsST and DROsS averages — Tables 7a and 8a",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "all: 2SE = 2SD/n^0.5, n = 45 cycles — within-run errors (§3)",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "UMd, DTM [all: 2SD of the analyses in each session] — Table 7a",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "UMd [187Os/188Os: 0.113795 ± 25 (2SD, n = 94)]; DTM [187Os/188Os: 0.173923 ± 26 (2SD, n = 121)] — 9 sessions over 11 months (Table 7a)",
  "ada:analyticalAccuracyAndAssessmentMethod": "UMd [187Os/188Os: +26 ppm; 186Os/188Os: −125 ppm]; DTM [187Os/188Os: −12 ppm; 186Os/188Os: −108 ppm] — offset from Durham N-TIMS (Table 7a)",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "all: 2SD — Table 7a: 'All quoted errors are 2SD'",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfBlocksPerMeasurement",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfBlocksPerMeasurement"
        }
      ],
      "schema:name": "Number of Blocks per Measurement",
      "schema:value": 9
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock"
        }
      ],
      "schema:name": "Number of Cycles per Block",
      "schema:value": "all: 5 cycles — 9 blocks (§3.1)"
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio"
        }
      ],
      "schema:name": "Double-Spike Mixing Ratio",
      "schema:value": "N/A — no double spike used"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/detail/context.jsonld",
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
      "@id": "ex:solutionMcicpmsTAPP-P6",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "UMd, DTM, LOsST and DROsS Os isotope reference materials",
  "ada:samplingUnitName": "Labelled for LOsST only: \"LOsST 17-03-06 (Aliq 1)\" (Table 8b, p.22) \u2014 the Neptune and Nu Plasma runs \"were made on two different aliquots of the LOsST RM\" (p.24); UMd, DTM and DROsS by name and session date",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:deltaOrEpsilonValueReferenceStandard": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially \u2014 n = 45 per analysis. No rejection rule stated",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:combinedResults": "UMd and DTM per-session averages; UMd average (94 analyses); DTM average (121 analyses); stable Os ratio averages (215 analyses); LOsST and DROsS averages \u2014 Tables 7a and 8a",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "all: 2SE = 2SD/n^0.5, n = 45 cycles \u2014 within-run errors (\u00a73)",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "UMd, DTM [all: 2SD of the analyses in each session] \u2014 Table 7a",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "UMd [187Os/188Os: 0.113795 \u00b1 25 (2SD, n = 94)]; DTM [187Os/188Os: 0.173923 \u00b1 26 (2SD, n = 121)] \u2014 9 sessions over 11 months (Table 7a)",
  "ada:analyticalAccuracyAndAssessmentMethod": "UMd [187Os/188Os: +26 ppm; 186Os/188Os: \u2212125 ppm]; DTM [187Os/188Os: \u221212 ppm; 186Os/188Os: \u2212108 ppm] \u2014 offset from Durham N-TIMS (Table 7a)",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "all: 2SD \u2014 Table 7a: 'All quoted errors are 2SD'",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfBlocksPerMeasurement",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfBlocksPerMeasurement"
        }
      ],
      "schema:name": "Number of Blocks per Measurement",
      "schema:value": 9
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock"
        }
      ],
      "schema:name": "Number of Cycles per Block",
      "schema:value": "all: 5 cycles \u2014 9 blocks (\u00a73.1)"
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio"
        }
      ],
      "schema:name": "Double-Spike Mixing Ratio",
      "schema:value": "N/A \u2014 no double spike used"
    }
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-P6> a ada:SolutionICPMSTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio>,
        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfBlocksPerMeasurement>,
        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock> ;
    schema1:measurementTechnique <ex:solutionMcicpmsTAPP-P6> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially — n = 45 per analysis. No rejection rule stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "UMd [187Os/188Os: +26 ppm; 186Os/188Os: −125 ppm]; DTM [187Os/188Os: −12 ppm; 186Os/188Os: −108 ppm] — offset from Durham N-TIMS (Table 7a)" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "UMd [187Os/188Os: 0.113795 ± 25 (2SD, n = 94)]; DTM [187Os/188Os: 0.173923 ± 26 (2SD, n = 121)] — 9 sessions over 11 months (Table 7a)" ;
    ada:combinedResults "UMd and DTM per-session averages; UMd average (94 analyses); DTM average (121 analyses); stable Os ratio averages (215 analyses); LOsST and DROsS averages — Tables 7a and 8a" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:deltaOrEpsilonValueReferenceStandard "missing" ;
    ada:detectionLimit -9999 ;
    ada:errorCorrelationBetweenReportedQuantities -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "all: 2SD — Table 7a: 'All quoted errors are 2SD'" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "all: 2SE = 2SD/n^0.5, n = 45 cycles — within-run errors (§3)" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:oxideProduction "missing" ;
    ada:peakFlatness "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "UMd, DTM, LOsST and DROsS Os isotope reference materials" ;
    ada:samplingUnitName "Labelled for LOsST only: \"LOsST 17-03-06 (Aliq 1)\" (Table 8b, p.22) — the Neptune and Nu Plasma runs \"were made on two different aliquots of the LOsST RM\" (p.24); UMd, DTM and DROsS by name and session date" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "UMd, DTM [all: 2SD of the analyses in each session] — Table 7a" .

<ex:solutionMcicpmsTAPP-P6> schema1:identifier "missing" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio> a schema1:PropertyValue ;
    schema1:name "Double-Spike Mixing Ratio" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio> ;
    schema1:value "N/A — no double spike used" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfBlocksPerMeasurement> a schema1:PropertyValue ;
    schema1:name "Number of Blocks per Measurement" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfBlocksPerMeasurement> ;
    schema1:value 9 .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock> a schema1:PropertyValue ;
    schema1:name "Number of Cycles per Block" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock> ;
    schema1:value "all: 5 cycles — 9 blocks (§3.1)" .


```


### detail example P7
detail instance derived from Nowell+etal2008 | Nu Plasma | NIGL.
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
      "@id": "ex:solutionMcicpmsTAPP-P7",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "DTM and LOsST Os isotope reference materials",
  "ada:samplingUnitName": "Labelled for LOsST only: \"23-05-06NIGL (Aliq 2)\" (Table 8b, p.22), the second of the \"two different aliquots of the LOsST RM\" (p.24); DTM by name only",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:deltaOrEpsilonValueReferenceStandard": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially — n = 50 per analysis. No rejection rule stated",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:combinedResults": "DTM average; LOsST average — Tables 7b and 8b",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "all: 2SE = 2SD/n^0.5, n = 50 cycles — within-run errors (§3)",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "DTM [187Os/188Os: 0.173910 ± 21 (2SD, n = 9)] — session 23-05-06 (Table 7a)",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "DTM [187Os/188Os: compared with Durham N-TIMS 0.173927 ± 5] — Table 7a",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "all: 2SD — 'Reported errors are 2SD unless otherwise stated'",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfBlocksPerMeasurement",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfBlocksPerMeasurement"
        }
      ],
      "schema:name": "Number of Blocks per Measurement",
      "schema:value": 1
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock"
        }
      ],
      "schema:name": "Number of Cycles per Block",
      "schema:value": "all: 50 cycles — 1 block"
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio"
        }
      ],
      "schema:name": "Double-Spike Mixing Ratio",
      "schema:value": "N/A — no double spike used"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/detail/context.jsonld",
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
      "@id": "ex:solutionMcicpmsTAPP-P7",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "DTM and LOsST Os isotope reference materials",
  "ada:samplingUnitName": "Labelled for LOsST only: \"23-05-06NIGL (Aliq 2)\" (Table 8b, p.22), the second of the \"two different aliquots of the LOsST RM\" (p.24); DTM by name only",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:deltaOrEpsilonValueReferenceStandard": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially \u2014 n = 50 per analysis. No rejection rule stated",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:combinedResults": "DTM average; LOsST average \u2014 Tables 7b and 8b",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "all: 2SE = 2SD/n^0.5, n = 50 cycles \u2014 within-run errors (\u00a73)",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "DTM [187Os/188Os: 0.173910 \u00b1 21 (2SD, n = 9)] \u2014 session 23-05-06 (Table 7a)",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "DTM [187Os/188Os: compared with Durham N-TIMS 0.173927 \u00b1 5] \u2014 Table 7a",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "all: 2SD \u2014 'Reported errors are 2SD unless otherwise stated'",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfBlocksPerMeasurement",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfBlocksPerMeasurement"
        }
      ],
      "schema:name": "Number of Blocks per Measurement",
      "schema:value": 1
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock"
        }
      ],
      "schema:name": "Number of Cycles per Block",
      "schema:value": "all: 50 cycles \u2014 1 block"
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio"
        }
      ],
      "schema:name": "Double-Spike Mixing Ratio",
      "schema:value": "N/A \u2014 no double spike used"
    }
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-P7> a ada:SolutionICPMSTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio>,
        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfBlocksPerMeasurement>,
        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock> ;
    schema1:measurementTechnique <ex:solutionMcicpmsTAPP-P7> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially — n = 50 per analysis. No rejection rule stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "DTM [187Os/188Os: compared with Durham N-TIMS 0.173927 ± 5] — Table 7a" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:combinedResults "DTM average; LOsST average — Tables 7b and 8b" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:deltaOrEpsilonValueReferenceStandard "missing" ;
    ada:detectionLimit -9999 ;
    ada:errorCorrelationBetweenReportedQuantities -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "all: 2SD — 'Reported errors are 2SD unless otherwise stated'" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "all: 2SE = 2SD/n^0.5, n = 50 cycles — within-run errors (§3)" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:oxideProduction "missing" ;
    ada:peakFlatness "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "DTM and LOsST Os isotope reference materials" ;
    ada:samplingUnitName "Labelled for LOsST only: \"23-05-06NIGL (Aliq 2)\" (Table 8b, p.22), the second of the \"two different aliquots of the LOsST RM\" (p.24); DTM by name only" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "DTM [187Os/188Os: 0.173910 ± 21 (2SD, n = 9)] — session 23-05-06 (Table 7a)" .

<ex:solutionMcicpmsTAPP-P7> schema1:identifier "missing" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio> a schema1:PropertyValue ;
    schema1:name "Double-Spike Mixing Ratio" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio> ;
    schema1:value "N/A — no double spike used" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfBlocksPerMeasurement> a schema1:PropertyValue ;
    schema1:name "Number of Blocks per Measurement" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfBlocksPerMeasurement> ;
    schema1:value 1 .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock> a schema1:PropertyValue ;
    schema1:name "Number of Cycles per Block" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock> ;
    schema1:value "all: 50 cycles — 1 block" .


```


### detail example Moynier2017
detail instance derived from Pringle+Moynier2017 | Neptune Plus | IPGP.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Moynier2017",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionMcicpmsTAPP-Moynier2017",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "GS-N, AGV-2, BCR-2, BHVO-2, EW9309 10D, AHANEMO2 D20B; Allende (duplicate splits); NIST SRM984",
  "ada:samplingUnitName": "Labelled for the one duplicated sample: \"Allende I\" and \"Allende II\" (Table 1, p.4), \"duplicate splits from the same powder aliquot\" (p.3); every other sample by name only",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:deltaOrEpsilonValueReferenceStandard": "Rb: NIST SRM984 RbCl — BCR-2 as the bracketing standard in some sessions",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "N — no result-level rule is stated. Reported values are \"averages of repeated measurements of each sample when multiple analyses were possible\", with no criterion for admitting or rejecting a measurement; the \"any ratio outside 2σ was discarded\" rule acts within a measurement and is recorded under Spike / Outlier Filtering Approach",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:combinedResults": "per-sample averages; terrestrial average; low-Ti and high-Ti lunar averages; lunar average; Allende average; carbonaceous chondrite average; enstatite chondrite average — Table 1",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "pure Rb ICP-MS solution [δ87Rb: ±0.01‰ (n = 40)] — run as an external standard each session",
  "ada:analyticalAccuracyAndAssessmentMethod": "SRM984 through chemistry [δ87Rb: 0.00 ± 0.03‰]; Allende [δ87Rb: duplicate splits 0.12 ± 0.02‰ and 0.14 ± 0.04‰] — §2.3",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfBlocksPerMeasurement",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfBlocksPerMeasurement"
        }
      ],
      "schema:name": "Number of Blocks per Measurement",
      "schema:value": "N — 'blocks of 20 cycles'"
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock"
        }
      ],
      "schema:name": "Number of Cycles per Block",
      "schema:value": "all: 20 cycles"
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio"
        }
      ],
      "schema:name": "Double-Spike Mixing Ratio",
      "schema:value": "N/A — no double spike used"
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/spikeOutlierFilteringApproach",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/spikeOutlierFilteringApproach"
        }
      ],
      "schema:name": "Spike / Outlier Filtering Approach",
      "schema:value": "\"any ratio outside 2σ was discarded\""
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Moynier2017",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionMcicpmsTAPP-Moynier2017",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "GS-N, AGV-2, BCR-2, BHVO-2, EW9309 10D, AHANEMO2 D20B; Allende (duplicate splits); NIST SRM984",
  "ada:samplingUnitName": "Labelled for the one duplicated sample: \"Allende I\" and \"Allende II\" (Table 1, p.4), \"duplicate splits from the same powder aliquot\" (p.3); every other sample by name only",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:deltaOrEpsilonValueReferenceStandard": "Rb: NIST SRM984 RbCl \u2014 BCR-2 as the bracketing standard in some sessions",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 no result-level rule is stated. Reported values are \"averages of repeated measurements of each sample when multiple analyses were possible\", with no criterion for admitting or rejecting a measurement; the \"any ratio outside 2\u03c3 was discarded\" rule acts within a measurement and is recorded under Spike / Outlier Filtering Approach",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:combinedResults": "per-sample averages; terrestrial average; low-Ti and high-Ti lunar averages; lunar average; Allende average; carbonaceous chondrite average; enstatite chondrite average \u2014 Table 1",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "pure Rb ICP-MS solution [\u03b487Rb: \u00b10.01\u2030 (n = 40)] \u2014 run as an external standard each session",
  "ada:analyticalAccuracyAndAssessmentMethod": "SRM984 through chemistry [\u03b487Rb: 0.00 \u00b1 0.03\u2030]; Allende [\u03b487Rb: duplicate splits 0.12 \u00b1 0.02\u2030 and 0.14 \u00b1 0.04\u2030] \u2014 \u00a72.3",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfBlocksPerMeasurement",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfBlocksPerMeasurement"
        }
      ],
      "schema:name": "Number of Blocks per Measurement",
      "schema:value": "N \u2014 'blocks of 20 cycles'"
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock"
        }
      ],
      "schema:name": "Number of Cycles per Block",
      "schema:value": "all: 20 cycles"
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio"
        }
      ],
      "schema:name": "Double-Spike Mixing Ratio",
      "schema:value": "N/A \u2014 no double spike used"
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/spikeOutlierFilteringApproach",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/spikeOutlierFilteringApproach"
        }
      ],
      "schema:name": "Spike / Outlier Filtering Approach",
      "schema:value": "\"any ratio outside 2\u03c3 was discarded\""
    }
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Moynier2017> a ada:SolutionICPMSTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio>,
        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfBlocksPerMeasurement>,
        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock>,
        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/spikeOutlierFilteringApproach> ;
    schema1:measurementTechnique <ex:solutionMcicpmsTAPP-Moynier2017> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — no result-level rule is stated. Reported values are \"averages of repeated measurements of each sample when multiple analyses were possible\", with no criterion for admitting or rejecting a measurement; the \"any ratio outside 2σ was discarded\" rule acts within a measurement and is recorded under Spike / Outlier Filtering Approach" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "SRM984 through chemistry [δ87Rb: 0.00 ± 0.03‰]; Allende [δ87Rb: duplicate splits 0.12 ± 0.02‰ and 0.14 ± 0.04‰] — §2.3" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "pure Rb ICP-MS solution [δ87Rb: ±0.01‰ (n = 40)] — run as an external standard each session" ;
    ada:combinedResults "per-sample averages; terrestrial average; low-Ti and high-Ti lunar averages; lunar average; Allende average; carbonaceous chondrite average; enstatite chondrite average — Table 1" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:deltaOrEpsilonValueReferenceStandard "Rb: NIST SRM984 RbCl — BCR-2 as the bracketing standard in some sessions" ;
    ada:detectionLimit -9999 ;
    ada:errorCorrelationBetweenReportedQuantities -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:oxideProduction "missing" ;
    ada:peakFlatness "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "GS-N, AGV-2, BCR-2, BHVO-2, EW9309 10D, AHANEMO2 D20B; Allende (duplicate splits); NIST SRM984" ;
    ada:samplingUnitName "Labelled for the one duplicated sample: \"Allende I\" and \"Allende II\" (Table 1, p.4), \"duplicate splits from the same powder aliquot\" (p.3); every other sample by name only" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<ex:solutionMcicpmsTAPP-Moynier2017> schema1:identifier "missing" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio> a schema1:PropertyValue ;
    schema1:name "Double-Spike Mixing Ratio" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio> ;
    schema1:value "N/A — no double spike used" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfBlocksPerMeasurement> a schema1:PropertyValue ;
    schema1:name "Number of Blocks per Measurement" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfBlocksPerMeasurement> ;
    schema1:value "N — 'blocks of 20 cycles'" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock> a schema1:PropertyValue ;
    schema1:name "Number of Cycles per Block" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock> ;
    schema1:value "all: 20 cycles" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/spikeOutlierFilteringApproach> a schema1:PropertyValue ;
    schema1:name "Spike / Outlier Filtering Approach" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/spikeOutlierFilteringApproach> ;
    schema1:value "\"any ratio outside 2σ was discarded\"" .


```


### detail example P9
detail instance derived from Schönbächler+etal2025 | Neptune Plus | ETH Zurich.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-P9",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionMcicpmsTAPP-P9",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Ryugu A0106, A0106-A0107 and C0108; Tagish Lake, Tarda, Ivuna (PB and high PT), Orgueil, Murchison, Colony; eucrites Bouvante and Bereba; BHVO-2, BCR-2, AGV-1, SCo-1; NIST SRM 3169",
  "ada:samplingUnitName": "Labelled by digestion where a sample was digested more than one way: \"Ivuna PB\" and \"Ivuna high PT\", \"30 mg Tagish Lake (labeled high PT)\" and \"90 mg Tarda (high PT)\" (p.4); Ryugu A0106, A0106-A0107 and C0108 and the other samples by name only",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:deltaOrEpsilonValueReferenceStandard": "Zr: NIST SRM 3169",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "Zr: 0.08–0.24 ng — 0.08 and 0.24 ng with Tarda and Tagish Lake, 0.09 and 0.13 ng with Ivuna",
  "ada:analysisInclusionAndRejectionCriteria": "Rule: data outside the 2SD uncertainty are rejected as outliers; n stated per sample (n = 13–99 for terrestrial RMs; n = 17–38 for eucrites and Colony) — Table 1 note: 'An outlier rejection was carried out with rejection of data that falls outside the 2SD uncertainty'",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:combinedResults": "per-sample averages (n = number of measurements); BHVO-2 average of two digestions; Ryugu average (all); Ryugu average (samples); Allende average — Table 1",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "all [ε91Zr: 0.35; ε92Zr: 0.21; ε96Zr: 1.00] — 2SD of NIST SRM 3169 for an average session at 30 ppb (n = 32)",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "BHVO-2, BCR-2, AGV-1, SCo-1, Bouvante, Bereba, Colony [ε91Zr: 0.3; ε92Zr: 0.2; ε96Zr: 1.0] — average 2SD over 10 months, n = 13–99 (eucrites and Colony n = 17–38)",
  "ada:analyticalAccuracyAndAssessmentMethod": "BHVO-2, BCR-2, AGV-1, SCo-1, Bouvante, Bereba, Colony [all: measured repeatedly to verify data quality] — doping tests with Ti, V, Cr, Mo, Hf and W 'have no effect on the accuracy of the Zr isotope data'",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "all: 2SD of the individual measurements — Fig. 1: 'the 2 sd calculated from the individual sample measurements'",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock"
        }
      ],
      "schema:name": "Number of Cycles per Block",
      "schema:value": "all: 60 ratios — static collection"
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio"
        }
      ],
      "schema:name": "Double-Spike Mixing Ratio",
      "schema:value": "N/A — no double spike used"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-P9",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionMcicpmsTAPP-P9",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Ryugu A0106, A0106-A0107 and C0108; Tagish Lake, Tarda, Ivuna (PB and high PT), Orgueil, Murchison, Colony; eucrites Bouvante and Bereba; BHVO-2, BCR-2, AGV-1, SCo-1; NIST SRM 3169",
  "ada:samplingUnitName": "Labelled by digestion where a sample was digested more than one way: \"Ivuna PB\" and \"Ivuna high PT\", \"30 mg Tagish Lake (labeled high PT)\" and \"90 mg Tarda (high PT)\" (p.4); Ryugu A0106, A0106-A0107 and C0108 and the other samples by name only",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:deltaOrEpsilonValueReferenceStandard": "Zr: NIST SRM 3169",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "Zr: 0.08\u20130.24 ng \u2014 0.08 and 0.24 ng with Tarda and Tagish Lake, 0.09 and 0.13 ng with Ivuna",
  "ada:analysisInclusionAndRejectionCriteria": "Rule: data outside the 2SD uncertainty are rejected as outliers; n stated per sample (n = 13\u201399 for terrestrial RMs; n = 17\u201338 for eucrites and Colony) \u2014 Table 1 note: 'An outlier rejection was carried out with rejection of data that falls outside the 2SD uncertainty'",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:combinedResults": "per-sample averages (n = number of measurements); BHVO-2 average of two digestions; Ryugu average (all); Ryugu average (samples); Allende average \u2014 Table 1",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "all [\u03b591Zr: 0.35; \u03b592Zr: 0.21; \u03b596Zr: 1.00] \u2014 2SD of NIST SRM 3169 for an average session at 30 ppb (n = 32)",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "BHVO-2, BCR-2, AGV-1, SCo-1, Bouvante, Bereba, Colony [\u03b591Zr: 0.3; \u03b592Zr: 0.2; \u03b596Zr: 1.0] \u2014 average 2SD over 10 months, n = 13\u201399 (eucrites and Colony n = 17\u201338)",
  "ada:analyticalAccuracyAndAssessmentMethod": "BHVO-2, BCR-2, AGV-1, SCo-1, Bouvante, Bereba, Colony [all: measured repeatedly to verify data quality] \u2014 doping tests with Ti, V, Cr, Mo, Hf and W 'have no effect on the accuracy of the Zr isotope data'",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "all: 2SD of the individual measurements \u2014 Fig. 1: 'the 2 sd calculated from the individual sample measurements'",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock"
        }
      ],
      "schema:name": "Number of Cycles per Block",
      "schema:value": "all: 60 ratios \u2014 static collection"
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio"
        }
      ],
      "schema:name": "Double-Spike Mixing Ratio",
      "schema:value": "N/A \u2014 no double spike used"
    }
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-P9> a ada:SolutionICPMSTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio>,
        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock> ;
    schema1:measurementTechnique <ex:solutionMcicpmsTAPP-P9> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Rule: data outside the 2SD uncertainty are rejected as outliers; n stated per sample (n = 13–99 for terrestrial RMs; n = 17–38 for eucrites and Colony) — Table 1 note: 'An outlier rejection was carried out with rejection of data that falls outside the 2SD uncertainty'" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "BHVO-2, BCR-2, AGV-1, SCo-1, Bouvante, Bereba, Colony [all: measured repeatedly to verify data quality] — doping tests with Ti, V, Cr, Mo, Hf and W 'have no effect on the accuracy of the Zr isotope data'" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "BHVO-2, BCR-2, AGV-1, SCo-1, Bouvante, Bereba, Colony [ε91Zr: 0.3; ε92Zr: 0.2; ε96Zr: 1.0] — average 2SD over 10 months, n = 13–99 (eucrites and Colony n = 17–38)" ;
    ada:combinedResults "per-sample averages (n = number of measurements); BHVO-2 average of two digestions; Ryugu average (all); Ryugu average (samples); Allende average — Table 1" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:deltaOrEpsilonValueReferenceStandard "Zr: NIST SRM 3169" ;
    ada:detectionLimit -9999 ;
    ada:errorCorrelationBetweenReportedQuantities -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "all: 2SD of the individual measurements — Fig. 1: 'the 2 sd calculated from the individual sample measurements'" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:oxideProduction "missing" ;
    ada:peakFlatness "missing" ;
    ada:proceduralBlankLevel "Zr: 0.08–0.24 ng — 0.08 and 0.24 ng with Tarda and Tagish Lake, 0.09 and 0.13 ng with Ivuna" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "Ryugu A0106, A0106-A0107 and C0108; Tagish Lake, Tarda, Ivuna (PB and high PT), Orgueil, Murchison, Colony; eucrites Bouvante and Bereba; BHVO-2, BCR-2, AGV-1, SCo-1; NIST SRM 3169" ;
    ada:samplingUnitName "Labelled by digestion where a sample was digested more than one way: \"Ivuna PB\" and \"Ivuna high PT\", \"30 mg Tagish Lake (labeled high PT)\" and \"90 mg Tarda (high PT)\" (p.4); Ryugu A0106, A0106-A0107 and C0108 and the other samples by name only" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "all [ε91Zr: 0.35; ε92Zr: 0.21; ε96Zr: 1.00] — 2SD of NIST SRM 3169 for an average session at 30 ppb (n = 32)" .

<ex:solutionMcicpmsTAPP-P9> schema1:identifier "missing" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio> a schema1:PropertyValue ;
    schema1:name "Double-Spike Mixing Ratio" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio> ;
    schema1:value "N/A — no double spike used" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock> a schema1:PropertyValue ;
    schema1:name "Number of Cycles per Block" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock> ;
    schema1:value "all: 60 ratios — static collection" .


```


### detail example P10
detail instance derived from vanKooten+etal2026 | Thermo Neoma | Univ Copenhagen.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-P10",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionMcicpmsTAPP-P10",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "BHVO2 and DTS-2b processed alongside the samples",
  "ada:samplingUnitName": "Labelled where a meteorite was analysed twice: \"NWA 16569 (1)\", \"NWA 16569 (2)\", \"NWA 16554 (1)\", \"NWA 16554 (2)\" (Table 1, p.2); the other chondrites by name only",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:deltaOrEpsilonValueReferenceStandard": "Fe: IRMM-014; Cr: SRM979; Mg: DTS-2b",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially — \"the mean ... of ten individual standard-bracketed sample analyses\"; \"Samples were typically analysed two to four times\". No rejection rule stated",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:combinedResults": "per-sample means (ten analyses each); CL grouplet weighted mean; CT grouplet weighted mean; CO average; CM-an average; CT average — Methods; Figs 2 and 4",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "N — BHVO2 and DTS-2b results are in Supplementary Dataset 2",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock"
        }
      ],
      "schema:name": "Number of Cycles per Block",
      "schema:value": "Fe: 200 cycles; Cr: 100 cycles; Mg: 100 cycles"
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio"
        }
      ],
      "schema:name": "Double-Spike Mixing Ratio",
      "schema:value": "N/A — no double spike used"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-P10",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionMcicpmsTAPP-P10",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "BHVO2 and DTS-2b processed alongside the samples",
  "ada:samplingUnitName": "Labelled where a meteorite was analysed twice: \"NWA 16569 (1)\", \"NWA 16569 (2)\", \"NWA 16554 (1)\", \"NWA 16554 (2)\" (Table 1, p.2); the other chondrites by name only",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:deltaOrEpsilonValueReferenceStandard": "Fe: IRMM-014; Cr: SRM979; Mg: DTS-2b",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially \u2014 \"the mean ... of ten individual standard-bracketed sample analyses\"; \"Samples were typically analysed two to four times\". No rejection rule stated",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:combinedResults": "per-sample means (ten analyses each); CL grouplet weighted mean; CT grouplet weighted mean; CO average; CM-an average; CT average \u2014 Methods; Figs 2 and 4",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "N \u2014 BHVO2 and DTS-2b results are in Supplementary Dataset 2",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock"
        }
      ],
      "schema:name": "Number of Cycles per Block",
      "schema:value": "Fe: 200 cycles; Cr: 100 cycles; Mg: 100 cycles"
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio"
        }
      ],
      "schema:name": "Double-Spike Mixing Ratio",
      "schema:value": "N/A \u2014 no double spike used"
    }
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-P10> a ada:SolutionICPMSTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio>,
        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock> ;
    schema1:measurementTechnique <ex:solutionMcicpmsTAPP-P10> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially — \"the mean ... of ten individual standard-bracketed sample analyses\"; \"Samples were typically analysed two to four times\". No rejection rule stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "N — BHVO2 and DTS-2b results are in Supplementary Dataset 2" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:combinedResults "per-sample means (ten analyses each); CL grouplet weighted mean; CT grouplet weighted mean; CO average; CM-an average; CT average — Methods; Figs 2 and 4" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:deltaOrEpsilonValueReferenceStandard "Fe: IRMM-014; Cr: SRM979; Mg: DTS-2b" ;
    ada:detectionLimit -9999 ;
    ada:errorCorrelationBetweenReportedQuantities -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:oxideProduction "missing" ;
    ada:peakFlatness "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "BHVO2 and DTS-2b processed alongside the samples" ;
    ada:samplingUnitName "Labelled where a meteorite was analysed twice: \"NWA 16569 (1)\", \"NWA 16569 (2)\", \"NWA 16554 (1)\", \"NWA 16554 (2)\" (Table 1, p.2); the other chondrites by name only" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<ex:solutionMcicpmsTAPP-P10> schema1:identifier "missing" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio> a schema1:PropertyValue ;
    schema1:name "Double-Spike Mixing Ratio" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio> ;
    schema1:value "N/A — no double spike used" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock> a schema1:PropertyValue ;
    schema1:name "Number of Cycles per Block" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock> ;
    schema1:value "Fe: 200 cycles; Cr: 100 cycles; Mg: 100 cycles" .


```


### detail example P11
detail instance derived from Broussard+etal2026 | Neptune Plus | WUSTL.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-P11",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionMcicpmsTAPP-P11",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Oued Chebeika 002; geostandard BHVO-2; NIST SRM 3141a",
  "ada:samplingUnitName": "Labelled: two solutions of the OC002 fragment — \"Approximately 7 mg of sample from the LAB24-2 OC002A and OC002B solutions ... were used for potassium stable isotope analysis\" (p.3)",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:deltaOrEpsilonValueReferenceStandard": "K: NIST SRM 3141a",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially — \"Each sample was measured approximately 20 times\". No rejection rule stated",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:combinedResults": "BHVO-2 δ41K average — p.4; whether the sample values average the ~20 measurements is not stated",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "BHVO-2 [δ41K: −0.448 ± 0.027‰, within error of reported values such as −0.46 ± 0.09‰ (Wang et al. 2021)]",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock"
        }
      ],
      "schema:name": "Number of Cycles per Block",
      "schema:value": "N — 'Each sample was measured approximately 20 times'"
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio"
        }
      ],
      "schema:name": "Double-Spike Mixing Ratio",
      "schema:value": "N/A — no double spike used"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-P11",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionMcicpmsTAPP-P11",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Oued Chebeika 002; geostandard BHVO-2; NIST SRM 3141a",
  "ada:samplingUnitName": "Labelled: two solutions of the OC002 fragment \u2014 \"Approximately 7 mg of sample from the LAB24-2 OC002A and OC002B solutions ... were used for potassium stable isotope analysis\" (p.3)",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:deltaOrEpsilonValueReferenceStandard": "K: NIST SRM 3141a",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially \u2014 \"Each sample was measured approximately 20 times\". No rejection rule stated",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:combinedResults": "BHVO-2 \u03b441K average \u2014 p.4; whether the sample values average the ~20 measurements is not stated",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "BHVO-2 [\u03b441K: \u22120.448 \u00b1 0.027\u2030, within error of reported values such as \u22120.46 \u00b1 0.09\u2030 (Wang et al. 2021)]",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock"
        }
      ],
      "schema:name": "Number of Cycles per Block",
      "schema:value": "N \u2014 'Each sample was measured approximately 20 times'"
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio"
        }
      ],
      "schema:name": "Double-Spike Mixing Ratio",
      "schema:value": "N/A \u2014 no double spike used"
    }
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-P11> a ada:SolutionICPMSTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio>,
        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock> ;
    schema1:measurementTechnique <ex:solutionMcicpmsTAPP-P11> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially — \"Each sample was measured approximately 20 times\". No rejection rule stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "BHVO-2 [δ41K: −0.448 ± 0.027‰, within error of reported values such as −0.46 ± 0.09‰ (Wang et al. 2021)]" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:combinedResults "BHVO-2 δ41K average — p.4; whether the sample values average the ~20 measurements is not stated" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:deltaOrEpsilonValueReferenceStandard "K: NIST SRM 3141a" ;
    ada:detectionLimit -9999 ;
    ada:errorCorrelationBetweenReportedQuantities -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:oxideProduction "missing" ;
    ada:peakFlatness "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "Oued Chebeika 002; geostandard BHVO-2; NIST SRM 3141a" ;
    ada:samplingUnitName "Labelled: two solutions of the OC002 fragment — \"Approximately 7 mg of sample from the LAB24-2 OC002A and OC002B solutions ... were used for potassium stable isotope analysis\" (p.3)" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<ex:solutionMcicpmsTAPP-P11> schema1:identifier "missing" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio> a schema1:PropertyValue ;
    schema1:name "Double-Spike Mixing Ratio" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio> ;
    schema1:value "N/A — no double spike used" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock> a schema1:PropertyValue ;
    schema1:name "Number of Cycles per Block" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock> ;
    schema1:value "N — 'Each sample was measured approximately 20 times'" .


```


### detail example P12
detail instance derived from Barnes+etal2025 | Neptune Plus | WUSTL.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-P12",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionMcicpmsTAPP-P12",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "OREX-803015-101 (LLNL split) and OREX-803015-100 (ETH split) of Bennu aggregate; BHVO-2",
  "ada:samplingUnitName": "Labelled: split \"OREX-803015-0\" — \"An ~20.66 mg split of Bennu aggregate (OREX-803015-0) was dissolved at WUSTL\" (p.7); the half of the solution kept at WUSTL is given no identifier of its own. The paper states its scheme: splits take \"suffixes of -100, -101, -102\" on the parent's number (p.7)",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:deltaOrEpsilonValueReferenceStandard": "K: NIST-SRM 3141a; Cu: NIST-SRM 976; Zn: JMC-Lyon",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:combinedResults": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "N — 'the geostandard BHVO-2 was analysed alongside all sample analyses'; results in Supplementary Table 9",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio"
        }
      ],
      "schema:name": "Double-Spike Mixing Ratio",
      "schema:value": "N/A — no double spike used"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-P12",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionMcicpmsTAPP-P12",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "OREX-803015-101 (LLNL split) and OREX-803015-100 (ETH split) of Bennu aggregate; BHVO-2",
  "ada:samplingUnitName": "Labelled: split \"OREX-803015-0\" \u2014 \"An ~20.66 mg split of Bennu aggregate (OREX-803015-0) was dissolved at WUSTL\" (p.7); the half of the solution kept at WUSTL is given no identifier of its own. The paper states its scheme: splits take \"suffixes of -100, -101, -102\" on the parent's number (p.7)",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:deltaOrEpsilonValueReferenceStandard": "K: NIST-SRM 3141a; Cu: NIST-SRM 976; Zn: JMC-Lyon",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:combinedResults": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "N \u2014 'the geostandard BHVO-2 was analysed alongside all sample analyses'; results in Supplementary Table 9",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio"
        }
      ],
      "schema:name": "Double-Spike Mixing Ratio",
      "schema:value": "N/A \u2014 no double spike used"
    }
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-P12> a ada:SolutionICPMSTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio> ;
    schema1:measurementTechnique <ex:solutionMcicpmsTAPP-P12> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "N — 'the geostandard BHVO-2 was analysed alongside all sample analyses'; results in Supplementary Table 9" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:combinedResults "missing" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:deltaOrEpsilonValueReferenceStandard "K: NIST-SRM 3141a; Cu: NIST-SRM 976; Zn: JMC-Lyon" ;
    ada:detectionLimit -9999 ;
    ada:errorCorrelationBetweenReportedQuantities -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:oxideProduction "missing" ;
    ada:peakFlatness "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "OREX-803015-101 (LLNL split) and OREX-803015-100 (ETH split) of Bennu aggregate; BHVO-2" ;
    ada:samplingUnitName "Labelled: split \"OREX-803015-0\" — \"An ~20.66 mg split of Bennu aggregate (OREX-803015-0) was dissolved at WUSTL\" (p.7); the half of the solution kept at WUSTL is given no identifier of its own. The paper states its scheme: splits take \"suffixes of -100, -101, -102\" on the parent's number (p.7)" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<ex:solutionMcicpmsTAPP-P12> schema1:identifier "missing" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio> a schema1:PropertyValue ;
    schema1:name "Double-Spike Mixing Ratio" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio> ;
    schema1:value "N/A — no double spike used" .


```


### detail example P13
detail instance derived from Barnes+etal2025 | Neptune Plus | ETH Zurich.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-P13",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionMcicpmsTAPP-P13",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "OREX-803015-100, a 5.2 mg aliquot of Bennu aggregate",
  "ada:samplingUnitName": "Labelled: aliquot \"OREX-803015-100\" — \"a 5.2 mg aliquot of Bennu aggregate (OREX-803015-100)\" (p.7)",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:deltaOrEpsilonValueReferenceStandard": "Ti: in-house Alfa Aesar Ti wire standard",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "Ti: 3.7 ng — a maximum blank contribution of 0.18%",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:combinedResults": "Bennu ε46Ti, ε48Ti and ε50Ti average (four repetitions) — p.2 and Methods",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "BHVO-2 [ε46Ti: ±0.17; ε48Ti: ±0.09; ε50Ti: ±0.16] — 2 s.d. of 9 analyses",
  "ada:analyticalAccuracyAndAssessmentMethod": "BHVO-2, Agua Zarcas [all: analysed alongside Bennu to verify accuracy and reproducibility]",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock"
        }
      ],
      "schema:name": "Number of Cycles per Block",
      "schema:value": "all: 40 cycles"
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio"
        }
      ],
      "schema:name": "Double-Spike Mixing Ratio",
      "schema:value": "N/A — no double spike used"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-P13",
  "@type": [
    "ada:SolutionICPMSTabular"
  ],
  "ada:componentType": "ada:SolutionICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:solutionMcicpmsTAPP-P13",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "OREX-803015-100, a 5.2 mg aliquot of Bennu aggregate",
  "ada:samplingUnitName": "Labelled: aliquot \"OREX-803015-100\" \u2014 \"a 5.2 mg aliquot of Bennu aggregate (OREX-803015-100)\" (p.7)",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:deltaOrEpsilonValueReferenceStandard": "Ti: in-house Alfa Aesar Ti wire standard",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "Ti: 3.7 ng \u2014 a maximum blank contribution of 0.18%",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:combinedResults": "Bennu \u03b546Ti, \u03b548Ti and \u03b550Ti average (four repetitions) \u2014 p.2 and Methods",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "BHVO-2 [\u03b546Ti: \u00b10.17; \u03b548Ti: \u00b10.09; \u03b550Ti: \u00b10.16] \u2014 2 s.d. of 9 analyses",
  "ada:analyticalAccuracyAndAssessmentMethod": "BHVO-2, Agua Zarcas [all: analysed alongside Bennu to verify accuracy and reproducibility]",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock"
        }
      ],
      "schema:name": "Number of Cycles per Block",
      "schema:value": "all: 40 cycles"
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio"
        }
      ],
      "schema:name": "Double-Spike Mixing Ratio",
      "schema:value": "N/A \u2014 no double spike used"
    }
  ]
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-P13> a ada:SolutionICPMSTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio>,
        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock> ;
    schema1:measurementTechnique <ex:solutionMcicpmsTAPP-P13> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "BHVO-2, Agua Zarcas [all: analysed alongside Bennu to verify accuracy and reproducibility]" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "BHVO-2 [ε46Ti: ±0.17; ε48Ti: ±0.09; ε50Ti: ±0.16] — 2 s.d. of 9 analyses" ;
    ada:combinedResults "Bennu ε46Ti, ε48Ti and ε50Ti average (four repetitions) — p.2 and Methods" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:deltaOrEpsilonValueReferenceStandard "Ti: in-house Alfa Aesar Ti wire standard" ;
    ada:detectionLimit -9999 ;
    ada:errorCorrelationBetweenReportedQuantities -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:oxideProduction "missing" ;
    ada:peakFlatness "missing" ;
    ada:proceduralBlankLevel "Ti: 3.7 ng — a maximum blank contribution of 0.18%" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "OREX-803015-100, a 5.2 mg aliquot of Bennu aggregate" ;
    ada:samplingUnitName "Labelled: aliquot \"OREX-803015-100\" — \"a 5.2 mg aliquot of Bennu aggregate (OREX-803015-100)\" (p.7)" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<ex:solutionMcicpmsTAPP-P13> schema1:identifier "missing" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio> a schema1:PropertyValue ;
    schema1:name "Double-Spike Mixing Ratio" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio> ;
    schema1:value "N/A — no double spike used" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock> a schema1:PropertyValue ;
    schema1:name "Number of Cycles per Block" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock> ;
    schema1:value "all: 40 cycles" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: Solution MC-ICP-MS Analysis Detail
description: Dataset-level analysis-instance detail for solution MC-ICP-MS, reusing
  CDIF/schema.org slots on the schema:Dataset root.
allOf:
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/AnalysisIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/AnalysisIdentification
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
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Analysis_constantsReferenceValues
                          allOf:
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_filteringApproach
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
                                    - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_memoryEffectMitigation
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
                                          const: ada:parameter/solutionMcicpmsTAPP/doublyChargedSpeciesMonitor
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/solutionMcicpmsTAPP/doublyChargedSpeciesMonitor
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
                                          const: ada:parameter/solutionMcicpmsTAPP/doublyChargedSpeciesProduction
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/solutionMcicpmsTAPP/doublyChargedSpeciesProduction
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
                                  allOf:
                                  - contains:
                                      $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/icpms/schema.yaml#/$defs/Param_Analysis_memoryEffectMitigation
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
                                          const: ada:parameter/solutionMcicpmsTAPP/doublyChargedSpeciesMonitor
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/solutionMcicpmsTAPP/doublyChargedSpeciesMonitor
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
                                          const: ada:parameter/solutionMcicpmsTAPP/doublyChargedSpeciesProduction
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/solutionMcicpmsTAPP/doublyChargedSpeciesProduction
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
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Analysis_numberOfBlocksPerMeasurement
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Analysis_numberOfCyclesPerBlock
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Analysis_integrationTimePerCycle
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Analysis_doubleSpikeMixingRatio
              - title: Error Correlation Between Reported Quantities
                description: The correlation coefficient between pairs of reported
                  quantities whose uncertainties are not independent, together with
                  the pair it applies to and how it was obtained.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/solutionMcicpmsTAPP/errorCorrelationBetweenReportedQuantities
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/solutionMcicpmsTAPP/errorCorrelationBetweenReportedQuantities
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
              - title: Collision/Reaction Gas Mixture Ratio
                description: Where the collision or reaction cell is supplied with
                  a mixture of gases rather than a single gas, the identities and
                  proportions of that mixture. Recorded separately from the gas identity.
                  Record 'N/A' where a single gas is used.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/solutionMcicpmsTAPP/collisionReactionGasMixtureRatio
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/solutionMcicpmsTAPP/collisionReactionGasMixtureRatio
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
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Analysis_numberOfBlocksPerMeasurement
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Analysis_numberOfCyclesPerBlock
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Analysis_integrationTimePerCycle
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Analysis_doubleSpikeMixingRatio
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
                    const: ada:parameter/solutionMcicpmsTAPP/errorCorrelationBetweenReportedQuantities
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/solutionMcicpmsTAPP/errorCorrelationBetweenReportedQuantities
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
                title: Collision/Reaction Gas Mixture Ratio
                description: Where the collision or reaction cell is supplied with
                  a mixture of gases rather than a single gas, the identities and
                  proportions of that mixture. Recorded separately from the gas identity.
                  Record 'N/A' where a single gas is used.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/solutionMcicpmsTAPP/collisionReactionGasMixtureRatio
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/solutionMcicpmsTAPP/collisionReactionGasMixtureRatio
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
          ada:deltaOrEpsilonValueReferenceStandard:
            description: "International or community-accepted isotopic reference standard
              used as the zero-delta anchor for expressing isotopic compositions in
              delta (\u03B4, per mil) or epsilon (\u03B5, per ten thousand) notation:
              \u03B4\u2071X = [(\u2071X/\u02B2X)sample / (\u2071X/\u02B2X)reference
              \u2212 1] \xD7 1000\u2030. The reporting reference is a per-study or
              per-publication decision. Specify the standard name, lot or batch number
              where applicable, and the certified or consensus isotope ratio used
              for normalization."
            type: string
        required:
        - ada:deltaOrEpsilonValueReferenceStandard
        - ada:proceduralBlankLevel
        - schema:actionProcess
    schema:variableMeasured:
      type: array
      items:
        anyOf:
        - title: Dataset variable
          description: A measured variable of this dataset that is not one of the
            procedure's declared reported properties. schema:variableMeasured carries
            the dataset's actual variables; the reported-property branches above are
            permitted members of it, not the whole of it.
          type: object
          required:
          - '@type'
          properties:
            '@type':
              type: array
              contains:
                enum:
                - cdi:InstanceVariable
                - schema:PropertyValue
        - title: Isotope Ratio Reported
          description: Specific isotope ratio pair(s) reported as primary data output.
            The denominator isotope is typically the reference mass used in the delta
            notation (e.g., 54Fe for Fe isotopes, 235U for U isotopes). Report all
            ratio pairs routinely calculated and reported.
          type: object
          properties:
            '@id':
              const: ada:parameter/solutionMcicpmsTAPP/isotopeRatioReported
            '@type':
              const:
              - schema:PropertyValue
              - cdi:InstanceVariable
            schema:propertyID:
              const:
              - '@id': ada:parameter/solutionMcicpmsTAPP/isotopeRatioReported
            schema:name:
              const: Isotope Ratio Reported
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
          title: Isotope Ratio Reported
          description: Specific isotope ratio pair(s) reported as primary data output.
            The denominator isotope is typically the reference mass used in the delta
            notation (e.g., 54Fe for Fe isotopes, 235U for U isotopes). Report all
            ratio pairs routinely calculated and reported.
          type: object
          properties:
            '@id':
              const: ada:parameter/solutionMcicpmsTAPP/isotopeRatioReported
            '@type':
              const:
              - schema:PropertyValue
              - cdi:InstanceVariable
            schema:propertyID:
              const:
              - '@id': ada:parameter/solutionMcicpmsTAPP/isotopeRatioReported
            schema:name:
              const: Isotope Ratio Reported
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

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/detail/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/detail/schema.yaml)


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
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/Solution-MC-ICPMS/detail/context.jsonld)

## Sources

* [Solution_MC-ICP-MS_TAPP_v16.csv (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/Solution-MC-ICPMS/detail`

