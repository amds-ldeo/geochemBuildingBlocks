
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
  "ada:deltaOrEpsilonValueReferenceStandard": "Alfa Aesar solution standard",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "\"Total procedural blanks were between 0.7 and 1.2 ng and thus negligible, given that several hundred ng of Mo were analyzed for each sample\"",
  "ada:analysisInclusionAndRejectionCriteria": "Partially — \"For samples analyzed several times, reported values represent the mean of pooled solution replicates\". No acceptance or rejection rule stated",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "External reproducibility from repeated BHVO-2 measurements: ±0.14 for ε97Mo to ±0.39 for ε92Mo (2 s.d., n = 24); Ba ±0.13 for ε135Ba to ±0.31 for ε138Ba (2 s.d., n = 14)",
  "ada:analyticalAccuracyAndAssessmentMethod": "\"The εiMo values obtained for BHVO-2 are indistinguishable from the Alfa Aesar standard, demonstrating that the Mo isotopic data are accurate\"",
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
      "schema:value": 100
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
  "ada:deltaOrEpsilonValueReferenceStandard": "Alfa Aesar solution standard",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "\"Total procedural blanks were between 0.7 and 1.2 ng and thus negligible, given that several hundred ng of Mo were analyzed for each sample\"",
  "ada:analysisInclusionAndRejectionCriteria": "Partially \u2014 \"For samples analyzed several times, reported values represent the mean of pooled solution replicates\". No acceptance or rejection rule stated",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "External reproducibility from repeated BHVO-2 measurements: \u00b10.14 for \u03b597Mo to \u00b10.39 for \u03b592Mo (2 s.d., n = 24); Ba \u00b10.13 for \u03b5135Ba to \u00b10.31 for \u03b5138Ba (2 s.d., n = 14)",
  "ada:analyticalAccuracyAndAssessmentMethod": "\"The \u03b5iMo values obtained for BHVO-2 are indistinguishable from the Alfa Aesar standard, demonstrating that the Mo isotopic data are accurate\"",
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
      "schema:value": 100
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
    ada:analyticalAccuracyAndAssessmentMethod "\"The εiMo values obtained for BHVO-2 are indistinguishable from the Alfa Aesar standard, demonstrating that the Mo isotopic data are accurate\"" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "External reproducibility from repeated BHVO-2 measurements: ±0.14 for ε97Mo to ±0.39 for ε92Mo (2 s.d., n = 24); Ba ±0.13 for ε135Ba to ±0.31 for ε138Ba (2 s.d., n = 14)" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:deltaOrEpsilonValueReferenceStandard "Alfa Aesar solution standard" ;
    ada:detectionLimit -9999 ;
    ada:errorCorrelationBetweenReportedQuantities -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:oxideProduction "missing" ;
    ada:peakFlatness "missing" ;
    ada:proceduralBlankLevel "\"Total procedural blanks were between 0.7 and 1.2 ng and thus negligible, given that several hundred ng of Mo were analyzed for each sample\"" ;
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
    schema1:value 100 .


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
  "ada:deltaOrEpsilonValueReferenceStandard": "V-CDT scale via IAEA-S-1, S-2, S-4 and NBS-123",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "\"The procedural blank, resulting from chemical processing and purification is ~0.05% (~0.25 µg per 500 µg S used for column chemistry)\"",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "\"Long-term reproducibility of S isotope compositions is typically 0.20‰ and 0.45‰ (2σ) for solution and laser\"; long-term reproducibility of in-house solution standards within ±0.2‰",
  "ada:analyticalAccuracyAndAssessmentMethod": "Assessed against IAEA and NBS reference materials on the V-CDT scale and against geological reference samples with known compositions",
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
      "schema:value": 20
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
  "ada:deltaOrEpsilonValueReferenceStandard": "V-CDT scale via IAEA-S-1, S-2, S-4 and NBS-123",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "\"The procedural blank, resulting from chemical processing and purification is ~0.05% (~0.25 \u00b5g per 500 \u00b5g S used for column chemistry)\"",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "\"Long-term reproducibility of S isotope compositions is typically 0.20\u2030 and 0.45\u2030 (2\u03c3) for solution and laser\"; long-term reproducibility of in-house solution standards within \u00b10.2\u2030",
  "ada:analyticalAccuracyAndAssessmentMethod": "Assessed against IAEA and NBS reference materials on the V-CDT scale and against geological reference samples with known compositions",
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
      "schema:value": 20
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

<ex:detail-P1> a ada:SolutionICPMSTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio>,
        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock> ;
    schema1:measurementTechnique <ex:solutionMcicpmsTAPP-P1> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "Assessed against IAEA and NBS reference materials on the V-CDT scale and against geological reference samples with known compositions" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "\"Long-term reproducibility of S isotope compositions is typically 0.20‰ and 0.45‰ (2σ) for solution and laser\"; long-term reproducibility of in-house solution standards within ±0.2‰" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:deltaOrEpsilonValueReferenceStandard "V-CDT scale via IAEA-S-1, S-2, S-4 and NBS-123" ;
    ada:detectionLimit -9999 ;
    ada:errorCorrelationBetweenReportedQuantities -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:oxideProduction "missing" ;
    ada:peakFlatness "missing" ;
    ada:proceduralBlankLevel "\"The procedural blank, resulting from chemical processing and purification is ~0.05% (~0.25 µg per 500 µg S used for column chemistry)\"" ;
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
    schema1:value 20 .


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
  "ada:deltaOrEpsilonValueReferenceStandard": "IRMM-524a, \"that has an identical isotopic composition to IRMM-014\"",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "\"the total procedural blank is ~70 ng and thus negligible considering that 1-2 mg Fe was purified for each sample\"",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
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
      "schema:value": 25
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
  "ada:deltaOrEpsilonValueReferenceStandard": "IRMM-524a, \"that has an identical isotopic composition to IRMM-014\"",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "\"the total procedural blank is ~70 ng and thus negligible considering that 1-2 mg Fe was purified for each sample\"",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
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
      "schema:value": 25
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
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "missing" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:deltaOrEpsilonValueReferenceStandard "IRMM-524a, \"that has an identical isotopic composition to IRMM-014\"" ;
    ada:detectionLimit -9999 ;
    ada:errorCorrelationBetweenReportedQuantities -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:oxideProduction "missing" ;
    ada:peakFlatness "missing" ;
    ada:proceduralBlankLevel "\"the total procedural blank is ~70 ng and thus negligible considering that 1-2 mg Fe was purified for each sample\"" ;
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
    schema1:value 25 .


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
  "ada:deltaOrEpsilonValueReferenceStandard": "OL-REE series, prepared in-house from high-purity ESPI oxide powder",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially — \"On average, LREEs were measured nine times\"; replicate matrix cuts were measured but \"are not used, however, for data interpretation to avoid unnecessary influence of stable isotopic fractionation potentially induced by Mo chemistry\" — an explicit exclusion, on chemical rather than statistical grounds",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "Assessed in a dedicated \"Assessment of data accuracy\" section, using replicate matrix cuts and a processed geostandard",
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
      "schema:value": 40
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
  "ada:deltaOrEpsilonValueReferenceStandard": "OL-REE series, prepared in-house from high-purity ESPI oxide powder",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially \u2014 \"On average, LREEs were measured nine times\"; replicate matrix cuts were measured but \"are not used, however, for data interpretation to avoid unnecessary influence of stable isotopic fractionation potentially induced by Mo chemistry\" \u2014 an explicit exclusion, on chemical rather than statistical grounds",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "Assessed in a dedicated \"Assessment of data accuracy\" section, using replicate matrix cuts and a processed geostandard",
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
      "schema:value": 40
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
    ada:analyticalAccuracyAndAssessmentMethod "Assessed in a dedicated \"Assessment of data accuracy\" section, using replicate matrix cuts and a processed geostandard" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:deltaOrEpsilonValueReferenceStandard "OL-REE series, prepared in-house from high-purity ESPI oxide powder" ;
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
    schema1:value 40 .


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
  "ada:deltaOrEpsilonValueReferenceStandard": "ZrNIST",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "\"The total mass of non-radiogenic Pb measured in our FC-1 zircon and baddeleyite fractions is indistinguishable from the range of Pb determined in total procedural blanks\"",
  "ada:analysisInclusionAndRejectionCriteria": "Partially — Table 1 records \"Number of times the same purified Zr solution was measured independently in the MC-ICP-MS\" and \"Reported values are weighted means of all replicate\" analyses. No rejection rule stated",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:countingStatisticsError": "Internal uncertainty determined from counting statistics, used as the comparison against the external reproducibility adopted per determination; value not tabulated",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "Internal uncertainty determined from counting statistics; stated to be similar in magnitude to or slightly smaller than the external reproducibility adopted per determination",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "External reproducibility at 2 sigma of the spiked ZrNIST measurements from each run, adopted as the uncertainty on each determination and stated to be similar to or slightly larger than the internal counting-statistics uncertainty",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "External reproducibility at 2σ of the spiked ZrNIST measurements from each run",
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
      "schema:value": 50
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
  "ada:deltaOrEpsilonValueReferenceStandard": "ZrNIST",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "\"The total mass of non-radiogenic Pb measured in our FC-1 zircon and baddeleyite fractions is indistinguishable from the range of Pb determined in total procedural blanks\"",
  "ada:analysisInclusionAndRejectionCriteria": "Partially \u2014 Table 1 records \"Number of times the same purified Zr solution was measured independently in the MC-ICP-MS\" and \"Reported values are weighted means of all replicate\" analyses. No rejection rule stated",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:countingStatisticsError": "Internal uncertainty determined from counting statistics, used as the comparison against the external reproducibility adopted per determination; value not tabulated",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "Internal uncertainty determined from counting statistics; stated to be similar in magnitude to or slightly smaller than the external reproducibility adopted per determination",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "External reproducibility at 2 sigma of the spiked ZrNIST measurements from each run, adopted as the uncertainty on each determination and stated to be similar to or slightly larger than the internal counting-statistics uncertainty",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "External reproducibility at 2\u03c3 of the spiked ZrNIST measurements from each run",
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
      "schema:value": 50
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
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "External reproducibility at 2σ of the spiked ZrNIST measurements from each run" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "Internal uncertainty determined from counting statistics, used as the comparison against the external reproducibility adopted per determination; value not tabulated" ;
    ada:deltaOrEpsilonValueReferenceStandard "ZrNIST" ;
    ada:detectionLimit -9999 ;
    ada:errorCorrelationBetweenReportedQuantities -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "Internal uncertainty determined from counting statistics; stated to be similar in magnitude to or slightly smaller than the external reproducibility adopted per determination" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:oxideProduction "missing" ;
    ada:peakFlatness "missing" ;
    ada:proceduralBlankLevel "\"The total mass of non-radiogenic Pb measured in our FC-1 zircon and baddeleyite fractions is indistinguishable from the range of Pb determined in total procedural blanks\"" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "FC-1 zircon and baddeleyite crystals; ZrNIST reference solution" ;
    ada:samplingUnitName "Labelled: single crystals of FC-1 — zircons \"z1\"–\"z16\" with \"3_z…\" and \"4_z…\" series (e.g. \"4_z15R\", \"4_z17\"), baddeleyites \"b1\"–\"b8\" with \"3_b…\" and \"4_b…\" series, and bulk rock \"WR1\" (Table 1, pp.4–6); \"CA\"/\"Untr.\" beside each label marks chemical abrasion, not identity" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "External reproducibility at 2 sigma of the spiked ZrNIST measurements from each run, adopted as the uncertainty on each determination and stated to be similar to or slightly larger than the internal counting-statistics uncertainty" .

<ex:solutionMcicpmsTAPP-Tissot2020> schema1:identifier "missing" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio> a schema1:PropertyValue ;
    schema1:name "Double-Spike Mixing Ratio" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio> ;
    schema1:value "0.43:0.57 spike-to-sample Zr mass ratio, described as optimal" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock> a schema1:PropertyValue ;
    schema1:name "Number of Cycles per Block" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock> ;
    schema1:value 50 .


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
  "ada:deltaOrEpsilonValueReferenceStandard": "NIST SRM984",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "\"The Rb blank of the procedure (digestion and column chemistry) is ~0.14 ng, which accounts for less than 0.5% of total Rb from a typical sample (40 ng)\"",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "NIST SRM984 treated as a sample, plus synthetic DTS-2b+SRM984 and PCC-1+SRM984 mixes, \"gave δ87Rb values of zero within error\"; geostandards and Allende \"yielded reproducible results that agree with literature data\"",
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
      "schema:value": 25
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
  "ada:deltaOrEpsilonValueReferenceStandard": "NIST SRM984",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "\"The Rb blank of the procedure (digestion and column chemistry) is ~0.14 ng, which accounts for less than 0.5% of total Rb from a typical sample (40 ng)\"",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "NIST SRM984 treated as a sample, plus synthetic DTS-2b+SRM984 and PCC-1+SRM984 mixes, \"gave \u03b487Rb values of zero within error\"; geostandards and Allende \"yielded reproducible results that agree with literature data\"",
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
      "schema:value": 25
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
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "NIST SRM984 treated as a sample, plus synthetic DTS-2b+SRM984 and PCC-1+SRM984 mixes, \"gave δ87Rb values of zero within error\"; geostandards and Allende \"yielded reproducible results that agree with literature data\"" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:deltaOrEpsilonValueReferenceStandard "NIST SRM984" ;
    ada:detectionLimit -9999 ;
    ada:errorCorrelationBetweenReportedQuantities -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:oxideProduction "missing" ;
    ada:peakFlatness "missing" ;
    ada:proceduralBlankLevel "\"The Rb blank of the procedure (digestion and column chemistry) is ~0.14 ng, which accounts for less than 0.5% of total Rb from a typical sample (40 ng)\"" ;
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
    schema1:value 25 .


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
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "Within-run errors for individual analyses quoted as 2 standard errors of the mean, 2SE = 2SD/n^0.5, with n = 45 cycles",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "Short-term reproducibility of standards analysed in a single analytical session, quoted as 2 standard deviations (2SD). Distinct from the within-run internal error, which the paper quotes separately as 2SE of the mean, 2SE = 2SD/n^0.5 with n = 45 for the Neptune and n = 50 for the Nu Plasma analyses",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
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
      "schema:value": 5
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
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "Within-run errors for individual analyses quoted as 2 standard errors of the mean, 2SE = 2SD/n^0.5, with n = 45 cycles",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "Short-term reproducibility of standards analysed in a single analytical session, quoted as 2 standard deviations (2SD). Distinct from the within-run internal error, which the paper quotes separately as 2SE of the mean, 2SE = 2SD/n^0.5 with n = 45 for the Neptune and n = 50 for the Nu Plasma analyses",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
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
      "schema:value": 5
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
    ada:analyticalAccuracyAndAssessmentMethod "missing" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:deltaOrEpsilonValueReferenceStandard "missing" ;
    ada:detectionLimit -9999 ;
    ada:errorCorrelationBetweenReportedQuantities -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "Within-run errors for individual analyses quoted as 2 standard errors of the mean, 2SE = 2SD/n^0.5, with n = 45 cycles" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:oxideProduction "missing" ;
    ada:peakFlatness "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "UMd, DTM, LOsST and DROsS Os isotope reference materials" ;
    ada:samplingUnitName "Labelled for LOsST only: \"LOsST 17-03-06 (Aliq 1)\" (Table 8b, p.22) — the Neptune and Nu Plasma runs \"were made on two different aliquots of the LOsST RM\" (p.24); UMd, DTM and DROsS by name and session date" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "Short-term reproducibility of standards analysed in a single analytical session, quoted as 2 standard deviations (2SD). Distinct from the within-run internal error, which the paper quotes separately as 2SE of the mean, 2SE = 2SD/n^0.5 with n = 45 for the Neptune and n = 50 for the Nu Plasma analyses" .

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
    schema1:value 5 .


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
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "Within-run errors for individual analyses quoted as 2 standard errors of the mean, 2SE = 2SD/n^0.5, with n = 50 cycles",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "Short-term reproducibility of standards analysed in a single analytical session, quoted as 2 standard deviations (2SD). Distinct from the within-run internal error, which the paper quotes separately as 2SE of the mean, 2SE = 2SD/n^0.5 with n = 45 for the Neptune and n = 50 for the Nu Plasma analyses",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
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
      "schema:value": 50
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
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "Within-run errors for individual analyses quoted as 2 standard errors of the mean, 2SE = 2SD/n^0.5, with n = 50 cycles",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "Short-term reproducibility of standards analysed in a single analytical session, quoted as 2 standard deviations (2SD). Distinct from the within-run internal error, which the paper quotes separately as 2SE of the mean, 2SE = 2SD/n^0.5 with n = 45 for the Neptune and n = 50 for the Nu Plasma analyses",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "missing",
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
      "schema:value": 50
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
    ada:analyticalAccuracyAndAssessmentMethod "missing" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:deltaOrEpsilonValueReferenceStandard "missing" ;
    ada:detectionLimit -9999 ;
    ada:errorCorrelationBetweenReportedQuantities -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "Within-run errors for individual analyses quoted as 2 standard errors of the mean, 2SE = 2SD/n^0.5, with n = 50 cycles" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:oxideProduction "missing" ;
    ada:peakFlatness "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "DTM and LOsST Os isotope reference materials" ;
    ada:samplingUnitName "Labelled for LOsST only: \"23-05-06NIGL (Aliq 2)\" (Table 8b, p.22), the second of the \"two different aliquots of the LOsST RM\" (p.24); DTM by name only" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "Short-term reproducibility of standards analysed in a single analytical session, quoted as 2 standard deviations (2SD). Distinct from the within-run internal error, which the paper quotes separately as 2SE of the mean, 2SE = 2SD/n^0.5 with n = 45 for the Neptune and n = 50 for the Nu Plasma analyses" .

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
    schema1:value 50 .


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
  "ada:deltaOrEpsilonValueReferenceStandard": "NIST SRM984 RbCl; the basalt geostandard BCR-2 used as an alternative bracketing standard in some sessions",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "N — no result-level rule is stated. Reported values are \"averages of repeated measurements of each sample when multiple analyses were possible\", with no criterion for admitting or rejecting a measurement; the \"any ratio outside 2σ was discarded\" rule acts within a measurement and is recorded under Spike / Outlier Filtering Approach",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "\"the long-term reproducibility was ±0.01‰ (n = 40)\" from a pure Rb ICP-MS solution run as an external standard each session",
  "ada:analyticalAccuracyAndAssessmentMethod": "An aliquot of SRM984 passed through the full chemistry gave δ87Rb = 0.00 ± 0.03‰, \"confirming that no isotope fractionation is caused by the Rb purification procedure\"; Allende duplicate splits agreed at 0.12 ± 0.02‰ and 0.14 ± 0.04‰",
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
      "schema:value": "Blocks of 20 cycles"
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
      "schema:value": 20
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
  "ada:deltaOrEpsilonValueReferenceStandard": "NIST SRM984 RbCl; the basalt geostandard BCR-2 used as an alternative bracketing standard in some sessions",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 no result-level rule is stated. Reported values are \"averages of repeated measurements of each sample when multiple analyses were possible\", with no criterion for admitting or rejecting a measurement; the \"any ratio outside 2\u03c3 was discarded\" rule acts within a measurement and is recorded under Spike / Outlier Filtering Approach",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "\"the long-term reproducibility was \u00b10.01\u2030 (n = 40)\" from a pure Rb ICP-MS solution run as an external standard each session",
  "ada:analyticalAccuracyAndAssessmentMethod": "An aliquot of SRM984 passed through the full chemistry gave \u03b487Rb = 0.00 \u00b1 0.03\u2030, \"confirming that no isotope fractionation is caused by the Rb purification procedure\"; Allende duplicate splits agreed at 0.12 \u00b1 0.02\u2030 and 0.14 \u00b1 0.04\u2030",
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
      "schema:value": "Blocks of 20 cycles"
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
      "schema:value": 20
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
    ada:analyticalAccuracyAndAssessmentMethod "An aliquot of SRM984 passed through the full chemistry gave δ87Rb = 0.00 ± 0.03‰, \"confirming that no isotope fractionation is caused by the Rb purification procedure\"; Allende duplicate splits agreed at 0.12 ± 0.02‰ and 0.14 ± 0.04‰" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "\"the long-term reproducibility was ±0.01‰ (n = 40)\" from a pure Rb ICP-MS solution run as an external standard each session" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:deltaOrEpsilonValueReferenceStandard "NIST SRM984 RbCl; the basalt geostandard BCR-2 used as an alternative bracketing standard in some sessions" ;
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
    schema1:value "Blocks of 20 cycles" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock> a schema1:PropertyValue ;
    schema1:name "Number of Cycles per Block" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock> ;
    schema1:value 20 .

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
  "ada:deltaOrEpsilonValueReferenceStandard": "NIST SRM 3169",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "\"Total procedural blanks prepared together with Tarda and Tagish Lake contained 0.08 and 0.24 ng Zr, while total blanks treated alongside Ivuna were 0.09 and 0.13 ng Zr\"",
  "ada:analysisInclusionAndRejectionCriteria": "Partially — n stated per reference material (n = 13–99 for terrestrial RMs over 10 months; n = 17–38 for eucrites and Colony; n = 32 and n = 37 for standard sessions). No rejection rule stated",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "Terrestrial RMs measured over 10 months (n = 13–99) give average 2SD of 0.3, 0.2 and 1.0 for ε91Zr, ε92Zr and ε96Zr; \"The external precision estimated from the geological sample measurements integrates the uncertainty introduced by the chemical separation procedure and mass spectrometry\"",
  "ada:analyticalAccuracyAndAssessmentMethod": "Terrestrial and meteorite reference materials measured repeatedly to verify data quality; doping tests with Ti, V, Cr, Mo, Hf and W showed \"the observed trace levels have no effect on the accuracy of the Zr isotope data\"",
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
      "schema:value": 60
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
  "ada:deltaOrEpsilonValueReferenceStandard": "NIST SRM 3169",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "\"Total procedural blanks prepared together with Tarda and Tagish Lake contained 0.08 and 0.24 ng Zr, while total blanks treated alongside Ivuna were 0.09 and 0.13 ng Zr\"",
  "ada:analysisInclusionAndRejectionCriteria": "Partially \u2014 n stated per reference material (n = 13\u201399 for terrestrial RMs over 10 months; n = 17\u201338 for eucrites and Colony; n = 32 and n = 37 for standard sessions). No rejection rule stated",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "Terrestrial RMs measured over 10 months (n = 13\u201399) give average 2SD of 0.3, 0.2 and 1.0 for \u03b591Zr, \u03b592Zr and \u03b596Zr; \"The external precision estimated from the geological sample measurements integrates the uncertainty introduced by the chemical separation procedure and mass spectrometry\"",
  "ada:analyticalAccuracyAndAssessmentMethod": "Terrestrial and meteorite reference materials measured repeatedly to verify data quality; doping tests with Ti, V, Cr, Mo, Hf and W showed \"the observed trace levels have no effect on the accuracy of the Zr isotope data\"",
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
      "schema:value": 60
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
    ada:analysisInclusionAndRejectionCriteria "Partially — n stated per reference material (n = 13–99 for terrestrial RMs over 10 months; n = 17–38 for eucrites and Colony; n = 32 and n = 37 for standard sessions). No rejection rule stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "Terrestrial and meteorite reference materials measured repeatedly to verify data quality; doping tests with Ti, V, Cr, Mo, Hf and W showed \"the observed trace levels have no effect on the accuracy of the Zr isotope data\"" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "Terrestrial RMs measured over 10 months (n = 13–99) give average 2SD of 0.3, 0.2 and 1.0 for ε91Zr, ε92Zr and ε96Zr; \"The external precision estimated from the geological sample measurements integrates the uncertainty introduced by the chemical separation procedure and mass spectrometry\"" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:deltaOrEpsilonValueReferenceStandard "NIST SRM 3169" ;
    ada:detectionLimit -9999 ;
    ada:errorCorrelationBetweenReportedQuantities -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:oxideProduction "missing" ;
    ada:peakFlatness "missing" ;
    ada:proceduralBlankLevel "\"Total procedural blanks prepared together with Tarda and Tagish Lake contained 0.08 and 0.24 ng Zr, while total blanks treated alongside Ivuna were 0.09 and 0.13 ng Zr\"" ;
    ada:sampleDescription "missing" ;
    ada:sampleName "Ryugu A0106, A0106-A0107 and C0108; Tagish Lake, Tarda, Ivuna (PB and high PT), Orgueil, Murchison, Colony; eucrites Bouvante and Bereba; BHVO-2, BCR-2, AGV-1, SCo-1; NIST SRM 3169" ;
    ada:samplingUnitName "Labelled by digestion where a sample was digested more than one way: \"Ivuna PB\" and \"Ivuna high PT\", \"30 mg Tagish Lake (labeled high PT)\" and \"90 mg Tarda (high PT)\" (p.4); Ryugu A0106, A0106-A0107 and C0108 and the other samples by name only" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<ex:solutionMcicpmsTAPP-P9> schema1:identifier "missing" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio> a schema1:PropertyValue ;
    schema1:name "Double-Spike Mixing Ratio" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatio> ;
    schema1:value "N/A — no double spike used" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock> a schema1:PropertyValue ;
    schema1:name "Number of Cycles per Block" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/numberOfCyclesPerBlock> ;
    schema1:value 60 .


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
  "ada:deltaOrEpsilonValueReferenceStandard": "IRMM-014 (Fe), SRM979 (Cr), DTS-2b (Mg)",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially — \"the mean ... of ten individual standard-bracketed sample analyses\"; \"Samples were typically analysed two to four times\". No rejection rule stated",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "BHVO2 and DTS-2b processed alongside the samples",
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
      "schema:value": "Fe 200 cycles; Cr 100 cycles; Mg 100 cycles"
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
  "ada:deltaOrEpsilonValueReferenceStandard": "IRMM-014 (Fe), SRM979 (Cr), DTS-2b (Mg)",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially \u2014 \"the mean ... of ten individual standard-bracketed sample analyses\"; \"Samples were typically analysed two to four times\". No rejection rule stated",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "BHVO2 and DTS-2b processed alongside the samples",
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
      "schema:value": "Fe 200 cycles; Cr 100 cycles; Mg 100 cycles"
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
    ada:analyticalAccuracyAndAssessmentMethod "BHVO2 and DTS-2b processed alongside the samples" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:deltaOrEpsilonValueReferenceStandard "IRMM-014 (Fe), SRM979 (Cr), DTS-2b (Mg)" ;
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
    schema1:value "Fe 200 cycles; Cr 100 cycles; Mg 100 cycles" .


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
  "ada:deltaOrEpsilonValueReferenceStandard": "NIST SRM 3141a",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially — \"Each sample was measured approximately 20 times\". No rejection rule stated",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "\"The average d41K value for BHVO-2 was −0.448 ± 0.027‰ which is within error of its previously reported values, for example, −0.46 ± 0.09‰ (Wang et al., 2021)\"",
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
      "schema:value": "\"Each sample was measured approximately 20 times\""
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
  "ada:deltaOrEpsilonValueReferenceStandard": "NIST SRM 3141a",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially \u2014 \"Each sample was measured approximately 20 times\". No rejection rule stated",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "\"The average d41K value for BHVO-2 was \u22120.448 \u00b1 0.027\u2030 which is within error of its previously reported values, for example, \u22120.46 \u00b1 0.09\u2030 (Wang et al., 2021)\"",
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
      "schema:value": "\"Each sample was measured approximately 20 times\""
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
    ada:analyticalAccuracyAndAssessmentMethod "\"The average d41K value for BHVO-2 was −0.448 ± 0.027‰ which is within error of its previously reported values, for example, −0.46 ± 0.09‰ (Wang et al., 2021)\"" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:deltaOrEpsilonValueReferenceStandard "NIST SRM 3141a" ;
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
    schema1:value "\"Each sample was measured approximately 20 times\"" .


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
  "ada:deltaOrEpsilonValueReferenceStandard": "NIST-SRM 3141a (K), NIST-SRM 976 (Cu), JMC-Lyon (Zn)",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "\"To monitor data quality, the geostandard BHVO-2 was analysed alongside all sample analyses\"",
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
  "ada:deltaOrEpsilonValueReferenceStandard": "NIST-SRM 3141a (K), NIST-SRM 976 (Cu), JMC-Lyon (Zn)",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "\"To monitor data quality, the geostandard BHVO-2 was analysed alongside all sample analyses\"",
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
    ada:analyticalAccuracyAndAssessmentMethod "\"To monitor data quality, the geostandard BHVO-2 was analysed alongside all sample analyses\"" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:deltaOrEpsilonValueReferenceStandard "NIST-SRM 3141a (K), NIST-SRM 976 (Cu), JMC-Lyon (Zn)" ;
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
  "ada:deltaOrEpsilonValueReferenceStandard": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "\"The total procedural blank for Ti was 3.7 ng, resulting in a maximum blank contribution of 0.18% for Ti\"",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "BHVO-2 and the Agua Zarcas (CM2) chondrite analysed alongside Bennu — \"To verify the accuracy and reproducibility of these measurements, the terrestrial rock standard BHVO-2 and the Agua Zarcas (CM2) chondrite were analysed alongside the Bennu sample. The analytical uncertainties of 9 analyses of BHVO-2 are ±0.17 ε46Ti, ±0.09 ε48Ti and ±0.16 ε50Ti (2 s.d.)\" (p.8). No accepted values or offsets are stated. The ±0.26 ε50Ti in the same paper is the LLNL procedure's (16 analyses of BCR-2 and BHVO-2, p.8), not this one",
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
      "schema:value": 40
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
  "ada:deltaOrEpsilonValueReferenceStandard": "missing",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "\"The total procedural blank for Ti was 3.7 ng, resulting in a maximum blank contribution of 0.18% for Ti\"",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:errorCorrelationBetweenReportedQuantities": -9999,
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "BHVO-2 and the Agua Zarcas (CM2) chondrite analysed alongside Bennu \u2014 \"To verify the accuracy and reproducibility of these measurements, the terrestrial rock standard BHVO-2 and the Agua Zarcas (CM2) chondrite were analysed alongside the Bennu sample. The analytical uncertainties of 9 analyses of BHVO-2 are \u00b10.17 \u03b546Ti, \u00b10.09 \u03b548Ti and \u00b10.16 \u03b550Ti (2 s.d.)\" (p.8). No accepted values or offsets are stated. The \u00b10.26 \u03b550Ti in the same paper is the LLNL procedure's (16 analyses of BCR-2 and BHVO-2, p.8), not this one",
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
      "schema:value": 40
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
    ada:analyticalAccuracyAndAssessmentMethod "BHVO-2 and the Agua Zarcas (CM2) chondrite analysed alongside Bennu — \"To verify the accuracy and reproducibility of these measurements, the terrestrial rock standard BHVO-2 and the Agua Zarcas (CM2) chondrite were analysed alongside the Bennu sample. The analytical uncertainties of 9 analyses of BHVO-2 are ±0.17 ε46Ti, ±0.09 ε48Ti and ±0.16 ε50Ti (2 s.d.)\" (p.8). No accepted values or offsets are stated. The ±0.26 ε50Ti in the same paper is the LLNL procedure's (16 analyses of BCR-2 and BHVO-2, p.8), not this one" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:SolutionICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:deltaOrEpsilonValueReferenceStandard "missing" ;
    ada:detectionLimit -9999 ;
    ada:errorCorrelationBetweenReportedQuantities -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:oxideProduction "missing" ;
    ada:peakFlatness "missing" ;
    ada:proceduralBlankLevel "\"The total procedural blank for Ti was 3.7 ng, resulting in a maximum blank contribution of 0.18% for Ti\"" ;
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
    schema1:value 40 .


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
    "wd": "https://www.wikidata.org/entity/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
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

