
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
      "@id": "ex:solutionMcicpmsTAPP-P0"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Three matrix separates, six chondrule fractions (C2, C3, C4; C3m, C3i, C3n) and two bulk rock samples of Allende; BHVO-2",
  "ada:samplingUnit": "Digestion aliquot — \"All samples (0.3–0.5 g) were digested in closed Savillex beakers\"; chondrule fractions \"comprise between 155 and ~3000 chondrules each\"",
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
      "@id": "ex:solutionMcicpmsTAPP-P0"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Three matrix separates, six chondrule fractions (C2, C3, C4; C3m, C3i, C3n) and two bulk rock samples of Allende; BHVO-2",
  "ada:samplingUnit": "Digestion aliquot \u2014 \"All samples (0.3\u20130.5 g) were digested in closed Savillex beakers\"; chondrule fractions \"comprise between 155 and ~3000 chondrules each\"",
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
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-P0 a ada:SolutionICPMSTabular ;
    schema1:measurementTechnique ex:solutionMcicpmsTAPP-P0 ;
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
    ada:samplingUnit "Digestion aliquot — \"All samples (0.3–0.5 g) were digested in closed Savillex beakers\"; chondrule fractions \"comprise between 155 and ~3000 chondrules each\"" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .


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
      "@id": "ex:solutionMcicpmsTAPP-P1"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "IAEA-S-1, S-2, S-4, NBS-123; in-house standards S_Alfa and S_Spex; anhydrite mineral standard Sch-M-2; pyrite FVG-1",
  "ada:samplingUnit": "Purified solution aliquot — \"Less than 50 mg of sample was accurately weighed\"; \"A precise solution volume, corresponding to 500 µg of S\" taken for column purification",
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
      "@id": "ex:solutionMcicpmsTAPP-P1"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "IAEA-S-1, S-2, S-4, NBS-123; in-house standards S_Alfa and S_Spex; anhydrite mineral standard Sch-M-2; pyrite FVG-1",
  "ada:samplingUnit": "Purified solution aliquot \u2014 \"Less than 50 mg of sample was accurately weighed\"; \"A precise solution volume, corresponding to 500 \u00b5g of S\" taken for column purification",
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
    schema1:measurementTechnique ex:solutionMcicpmsTAPP-P1 ;
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
    ada:samplingUnit "Purified solution aliquot — \"Less than 50 mg of sample was accurately weighed\"; \"A precise solution volume, corresponding to 500 µg of S\" taken for column purification" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .


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
      "@id": "ex:solutionMcicpmsTAPP-P2"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Toluca, Gibeon, Duchesne, Skookum, Tlacotepec and 18 further iron meteorites; BHVO-2, BCR-2; IRMM-524a",
  "ada:samplingUnit": "Solution aliquot of a digestion — \"the Fe isotopic compositions were analyzed on solution aliquots (~1-2 mg Fe) of digestions\"; five meteorites cut as \"~50 mg pieces\"",
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
      "@id": "ex:solutionMcicpmsTAPP-P2"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Toluca, Gibeon, Duchesne, Skookum, Tlacotepec and 18 further iron meteorites; BHVO-2, BCR-2; IRMM-524a",
  "ada:samplingUnit": "Solution aliquot of a digestion \u2014 \"the Fe isotopic compositions were analyzed on solution aliquots (~1-2 mg Fe) of digestions\"; five meteorites cut as \"~50 mg pieces\"",
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
    schema1:measurementTechnique ex:solutionMcicpmsTAPP-P2 ;
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
    ada:samplingUnit "Solution aliquot of a digestion — \"the Fe isotopic compositions were analyzed on solution aliquots (~1-2 mg Fe) of digestions\"; five meteorites cut as \"~50 mg pieces\"" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .


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
      "@id": "ex:solutionMcicpmsTAPP-P3"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Group II CAIs including FG-FT-4, FG-FT-8 and FG-FT-9",
  "ada:samplingUnit": "Fraction of a CAI digestion — \"Approximately 30% of the matrix cut\", \"equivalent to 24% fraction of the whole CAI\"",
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
      "@id": "ex:solutionMcicpmsTAPP-P3"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Group II CAIs including FG-FT-4, FG-FT-8 and FG-FT-9",
  "ada:samplingUnit": "Fraction of a CAI digestion \u2014 \"Approximately 30% of the matrix cut\", \"equivalent to 24% fraction of the whole CAI\"",
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
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-P3 a ada:SolutionICPMSTabular ;
    schema1:measurementTechnique ex:solutionMcicpmsTAPP-P3 ;
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
    ada:samplingUnit "Fraction of a CAI digestion — \"Approximately 30% of the matrix cut\", \"equivalent to 24% fraction of the whole CAI\"" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .


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
      "@id": "ex:solutionMcicpmsTAPP-Tissot2020"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "FC-1 zircon and baddeleyite crystals; ZrNIST reference solution",
  "ada:samplingUnit": "Single crystal — \"Single zircon and baddeleyite crystals selected for analysis were individually handpicked\"; each \"individually loaded into clean PFA microcapsules\"",
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
      "@id": "ada:parameter/solutionMcicpmsTAPP/uncertaintyPropagationMethod",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/uncertaintyPropagationMethod"
        }
      ],
      "schema:name": "Uncertainty Propagation Method",
      "schema:value": "External reproducibility of the spiked ZrNIST measurements from each run adopted per determination, compared against internal counting-statistics uncertainty"
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
      "@id": "ex:solutionMcicpmsTAPP-Tissot2020"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "FC-1 zircon and baddeleyite crystals; ZrNIST reference solution",
  "ada:samplingUnit": "Single crystal \u2014 \"Single zircon and baddeleyite crystals selected for analysis were individually handpicked\"; each \"individually loaded into clean PFA microcapsules\"",
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
      "@id": "ada:parameter/solutionMcicpmsTAPP/uncertaintyPropagationMethod",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/uncertaintyPropagationMethod"
        }
      ],
      "schema:name": "Uncertainty Propagation Method",
      "schema:value": "External reproducibility of the spiked ZrNIST measurements from each run adopted per determination, compared against internal counting-statistics uncertainty"
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

ex:detail-Tissot2020 a ada:SolutionICPMSTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/uncertaintyPropagationMethod> ;
    schema1:measurementTechnique ex:solutionMcicpmsTAPP-Tissot2020 ;
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
    ada:samplingUnit "Single crystal — \"Single zircon and baddeleyite crystals selected for analysis were individually handpicked\"; each \"individually loaded into clean PFA microcapsules\"" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "External reproducibility at 2 sigma of the spiked ZrNIST measurements from each run, adopted as the uncertainty on each determination and stated to be similar to or slightly larger than the internal counting-statistics uncertainty" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/uncertaintyPropagationMethod> a schema1:PropertyValue ;
    schema1:name "Uncertainty Propagation Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/uncertaintyPropagationMethod> ;
    schema1:value "External reproducibility of the spiked ZrNIST measurements from each run adopted per determination, compared against internal counting-statistics uncertainty" .


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
      "@id": "ex:solutionMcicpmsTAPP-Dauphas2019"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "BHVO-2, BCR-2, BE-N, W-2, AGV-2, GSR-1, GS-N, G-A, G-3; DTS-2b and PCC-1 synthetic mixes; Allende; NIST SRM984",
  "ada:samplingUnit": "Digestion aliquot — \"Samples of about 100 mg or less were digested\"",
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
      "@id": "ex:solutionMcicpmsTAPP-Dauphas2019"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "BHVO-2, BCR-2, BE-N, W-2, AGV-2, GSR-1, GS-N, G-A, G-3; DTS-2b and PCC-1 synthetic mixes; Allende; NIST SRM984",
  "ada:samplingUnit": "Digestion aliquot \u2014 \"Samples of about 100 mg or less were digested\"",
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
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Dauphas2019 a ada:SolutionICPMSTabular ;
    schema1:measurementTechnique ex:solutionMcicpmsTAPP-Dauphas2019 ;
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
    ada:samplingUnit "Digestion aliquot — \"Samples of about 100 mg or less were digested\"" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .


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
      "@id": "ex:solutionMcicpmsTAPP-P6"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "UMd, DTM, LOsST and DROsS Os isotope reference materials",
  "ada:samplingUnit": "Reference material solution aliquot — 200 ng/ml to 2.5 µg/ml Os, ~300 µl consumed per analysis",
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
      "@id": "ex:solutionMcicpmsTAPP-P6"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "UMd, DTM, LOsST and DROsS Os isotope reference materials",
  "ada:samplingUnit": "Reference material solution aliquot \u2014 200 ng/ml to 2.5 \u00b5g/ml Os, ~300 \u00b5l consumed per analysis",
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
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-P6 a ada:SolutionICPMSTabular ;
    schema1:measurementTechnique ex:solutionMcicpmsTAPP-P6 ;
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
    ada:samplingUnit "Reference material solution aliquot — 200 ng/ml to 2.5 µg/ml Os, ~300 µl consumed per analysis" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "Short-term reproducibility of standards analysed in a single analytical session, quoted as 2 standard deviations (2SD). Distinct from the within-run internal error, which the paper quotes separately as 2SE of the mean, 2SE = 2SD/n^0.5 with n = 45 for the Neptune and n = 50 for the Nu Plasma analyses" .


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
      "@id": "ex:solutionMcicpmsTAPP-P7"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "DTM and LOsST Os isotope reference materials",
  "ada:samplingUnit": "Reference material solution aliquot — ~6400 µl consumed per analysis",
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
      "@id": "ex:solutionMcicpmsTAPP-P7"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "DTM and LOsST Os isotope reference materials",
  "ada:samplingUnit": "Reference material solution aliquot \u2014 ~6400 \u00b5l consumed per analysis",
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
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-P7 a ada:SolutionICPMSTabular ;
    schema1:measurementTechnique ex:solutionMcicpmsTAPP-P7 ;
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
    ada:samplingUnit "Reference material solution aliquot — ~6400 µl consumed per analysis" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "Short-term reproducibility of standards analysed in a single analytical session, quoted as 2 standard deviations (2SD). Distinct from the within-run internal error, which the paper quotes separately as 2SE of the mean, 2SE = 2SD/n^0.5 with n = 45 for the Neptune and n = 50 for the Nu Plasma analyses" .


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
      "@id": "ex:solutionMcicpmsTAPP-Moynier2017"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "GS-N, AGV-2, BCR-2, BHVO-2, EW9309 10D, AHANEMO2 D20B; Allende (duplicate splits); NIST SRM984",
  "ada:samplingUnit": "Weighed powder aliquot — \"An aliquot of <=125 mg of powdered sample was weighed depending on the Rb concentration of the sample; masses were calculated to yield >20 ng Rb\"",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:deltaOrEpsilonValueReferenceStandard": "NIST SRM984 RbCl; the basalt geostandard BCR-2 used as an alternative bracketing standard in some sessions",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "\"any ratio outside 2σ was discarded\" — an explicit rejection rule, applied within a measurement. Reported values are \"averages of repeated measurements of each sample when multiple analyses were possible\"",
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
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/uncertaintyPropagationMethod",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/uncertaintyPropagationMethod"
        }
      ],
      "schema:name": "Uncertainty Propagation Method",
      "schema:value": "\"Errors are determined from repeated measurements\""
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
      "@id": "ex:solutionMcicpmsTAPP-Moynier2017"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "GS-N, AGV-2, BCR-2, BHVO-2, EW9309 10D, AHANEMO2 D20B; Allende (duplicate splits); NIST SRM984",
  "ada:samplingUnit": "Weighed powder aliquot \u2014 \"An aliquot of <=125 mg of powdered sample was weighed depending on the Rb concentration of the sample; masses were calculated to yield >20 ng Rb\"",
  "ada:sampleDescription": "missing",
  "ada:oxideProduction": "missing",
  "ada:peakFlatness": "missing",
  "ada:deltaOrEpsilonValueReferenceStandard": "NIST SRM984 RbCl; the basalt geostandard BCR-2 used as an alternative bracketing standard in some sessions",
  "ada:signalIntegrationTime": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "\"any ratio outside 2\u03c3 was discarded\" \u2014 an explicit rejection rule, applied within a measurement. Reported values are \"averages of repeated measurements of each sample when multiple analyses were possible\"",
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
    },
    {
      "@id": "ada:parameter/solutionMcicpmsTAPP/uncertaintyPropagationMethod",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/solutionMcicpmsTAPP/uncertaintyPropagationMethod"
        }
      ],
      "schema:name": "Uncertainty Propagation Method",
      "schema:value": "\"Errors are determined from repeated measurements\""
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

ex:detail-Moynier2017 a ada:SolutionICPMSTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/spikeOutlierFilteringApproach>,
        <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/uncertaintyPropagationMethod> ;
    schema1:measurementTechnique ex:solutionMcicpmsTAPP-Moynier2017 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "\"any ratio outside 2σ was discarded\" — an explicit rejection rule, applied within a measurement. Reported values are \"averages of repeated measurements of each sample when multiple analyses were possible\"" ;
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
    ada:samplingUnit "Weighed powder aliquot — \"An aliquot of <=125 mg of powdered sample was weighed depending on the Rb concentration of the sample; masses were calculated to yield >20 ng Rb\"" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/spikeOutlierFilteringApproach> a schema1:PropertyValue ;
    schema1:name "Spike / Outlier Filtering Approach" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/spikeOutlierFilteringApproach> ;
    schema1:value "\"any ratio outside 2σ was discarded\"" .

<https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/uncertaintyPropagationMethod> a schema1:PropertyValue ;
    schema1:name "Uncertainty Propagation Method" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/solutionMcicpmsTAPP/uncertaintyPropagationMethod> ;
    schema1:value "\"Errors are determined from repeated measurements\"" .


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
      "@id": "ex:solutionMcicpmsTAPP-P9"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Ryugu A0106, A0106-A0107 and C0108; Tagish Lake, Tarda, Ivuna (PB and high PT), Orgueil, Murchison, Colony; eucrites Bouvante and Bereba; BHVO-2, BCR-2, AGV-1, SCo-1; NIST SRM 3169",
  "ada:samplingUnit": "Digestion aliquot — Ryugu \"aliquots of <25 mg were analyzed with ~40 to 70 ng Zr\"; Tagish Lake 30 mg, Tarda 90 mg, Ivuna 40 and 44 mg \"from a larger homogenized powder (550 mg)\"",
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
      "@id": "ex:solutionMcicpmsTAPP-P9"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Ryugu A0106, A0106-A0107 and C0108; Tagish Lake, Tarda, Ivuna (PB and high PT), Orgueil, Murchison, Colony; eucrites Bouvante and Bereba; BHVO-2, BCR-2, AGV-1, SCo-1; NIST SRM 3169",
  "ada:samplingUnit": "Digestion aliquot \u2014 Ryugu \"aliquots of <25 mg were analyzed with ~40 to 70 ng Zr\"; Tagish Lake 30 mg, Tarda 90 mg, Ivuna 40 and 44 mg \"from a larger homogenized powder (550 mg)\"",
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
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-P9 a ada:SolutionICPMSTabular ;
    schema1:measurementTechnique ex:solutionMcicpmsTAPP-P9 ;
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
    ada:samplingUnit "Digestion aliquot — Ryugu \"aliquots of <25 mg were analyzed with ~40 to 70 ng Zr\"; Tagish Lake 30 mg, Tarda 90 mg, Ivuna 40 and 44 mg \"from a larger homogenized powder (550 mg)\"" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .


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
      "@id": "ex:solutionMcicpmsTAPP-P10"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "BHVO2 and DTS-2b processed alongside the samples",
  "ada:samplingUnit": "Fraction of a bulk digestion — \"Another 5% fraction was used to determine Al/Mg ratios by multi-collector (MC)-ICPMS\"",
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
      "@id": "ex:solutionMcicpmsTAPP-P10"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "BHVO2 and DTS-2b processed alongside the samples",
  "ada:samplingUnit": "Fraction of a bulk digestion \u2014 \"Another 5% fraction was used to determine Al/Mg ratios by multi-collector (MC)-ICPMS\"",
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
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-P10 a ada:SolutionICPMSTabular ;
    schema1:measurementTechnique ex:solutionMcicpmsTAPP-P10 ;
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
    ada:samplingUnit "Fraction of a bulk digestion — \"Another 5% fraction was used to determine Al/Mg ratios by multi-collector (MC)-ICPMS\"" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .


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
      "@id": "ex:solutionMcicpmsTAPP-P11"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Oued Chebeika 002; geostandard BHVO-2; NIST SRM 3141a",
  "ada:samplingUnit": "missing",
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
      "@id": "ex:solutionMcicpmsTAPP-P11"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Oued Chebeika 002; geostandard BHVO-2; NIST SRM 3141a",
  "ada:samplingUnit": "missing",
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
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-P11 a ada:SolutionICPMSTabular ;
    schema1:measurementTechnique ex:solutionMcicpmsTAPP-P11 ;
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
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .


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
      "@id": "ex:solutionMcicpmsTAPP-P12"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "OREX-803015-101 (LLNL split) and OREX-803015-100 (ETH split) of Bennu aggregate; BHVO-2",
  "ada:samplingUnit": "Split of a single digest — \"The solution was then split two ways: about half stayed at WUSTL and half was sent to Lawrence Livermore National Laboratory ... the aliquot was further split into two aliquots\"",
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
      "@id": "ex:solutionMcicpmsTAPP-P12"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "OREX-803015-101 (LLNL split) and OREX-803015-100 (ETH split) of Bennu aggregate; BHVO-2",
  "ada:samplingUnit": "Split of a single digest \u2014 \"The solution was then split two ways: about half stayed at WUSTL and half was sent to Lawrence Livermore National Laboratory ... the aliquot was further split into two aliquots\"",
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
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-P12 a ada:SolutionICPMSTabular ;
    schema1:measurementTechnique ex:solutionMcicpmsTAPP-P12 ;
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
    ada:samplingUnit "Split of a single digest — \"The solution was then split two ways: about half stayed at WUSTL and half was sent to Lawrence Livermore National Laboratory ... the aliquot was further split into two aliquots\"" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .


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
      "@id": "ex:solutionMcicpmsTAPP-P13"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "OREX-803015-100, a 5.2 mg aliquot of Bennu aggregate",
  "ada:samplingUnit": "A 5.2 mg aliquot of Bennu aggregate",
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
  "ada:analyticalAccuracyAndAssessmentMethod": "Reproducibility verified against measurements made \"under conditions similar to the methods used\", quoted as ±0.16 and ±0.26 ε50Ti (2 s.d.)",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
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
      "@id": "ex:solutionMcicpmsTAPP-P13"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "OREX-803015-100, a 5.2 mg aliquot of Bennu aggregate",
  "ada:samplingUnit": "A 5.2 mg aliquot of Bennu aggregate",
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
  "ada:analyticalAccuracyAndAssessmentMethod": "Reproducibility verified against measurements made \"under conditions similar to the methods used\", quoted as \u00b10.16 and \u00b10.26 \u03b550Ti (2 s.d.)",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-P13 a ada:SolutionICPMSTabular ;
    schema1:measurementTechnique ex:solutionMcicpmsTAPP-P13 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "Reproducibility verified against measurements made \"under conditions similar to the methods used\", quoted as ±0.16 and ±0.26 ε50Ti (2 s.d.)" ;
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
    ada:samplingUnit "A 5.2 mg aliquot of Bennu aggregate" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime -9999 ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "missing" .


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
                            - title: Spike / Outlier Filtering Approach
                              description: Criteria used to identify and exclude anomalous
                                cycles or replicate measurements from the calculated
                                isotope ratio mean. Filtering is applied after baseline
                                subtraction and before mass bias correction.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionMcicpmsTAPP/spikeOutlierFilteringApproach
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionMcicpmsTAPP/spikeOutlierFilteringApproach
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
                                  const: ada:parameter/solutionMcicpmsTAPP/uncertaintyPropagationMethod
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionMcicpmsTAPP/uncertaintyPropagationMethod
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
                            - title: Normalization / Standards-Based Correction
                              description: "Post-acquisition normalization applied
                                to output isotope ratio data beyond the primary mass
                                bias correction. Examples: correction of \u03B4 values
                                for decay of enriched spike isotopes between calibration
                                and use date (double-spike procedures); age correction
                                of \u03B4238U for secular disequilibrium. Record 'None'
                                if no additional normalization is applied."
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionMcicpmsTAPP/normalizationStandardsBasedCorrection
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionMcicpmsTAPP/normalizationStandardsBasedCorrection
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
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Analysis_constantsReferenceValues
                          allOf:
                          - contains:
                              title: Spike / Outlier Filtering Approach
                              description: Criteria used to identify and exclude anomalous
                                cycles or replicate measurements from the calculated
                                isotope ratio mean. Filtering is applied after baseline
                                subtraction and before mass bias correction.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionMcicpmsTAPP/spikeOutlierFilteringApproach
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionMcicpmsTAPP/spikeOutlierFilteringApproach
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
                                  const: ada:parameter/solutionMcicpmsTAPP/uncertaintyPropagationMethod
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionMcicpmsTAPP/uncertaintyPropagationMethod
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
                              title: Normalization / Standards-Based Correction
                              description: "Post-acquisition normalization applied
                                to output isotope ratio data beyond the primary mass
                                bias correction. Examples: correction of \u03B4 values
                                for decay of enriched spike isotopes between calibration
                                and use date (double-spike procedures); age correction
                                of \u03B4238U for secular disequilibrium. Record 'None'
                                if no additional normalization is applied."
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/solutionMcicpmsTAPP/normalizationStandardsBasedCorrection
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/solutionMcicpmsTAPP/normalizationStandardsBasedCorrection
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
                                                  const: ada:parameter/solutionMcicpmsTAPP/torchDepth
                                                '@type':
                                                  const:
                                                  - schema:PropertyValue
                                                schema:propertyID:
                                                  const:
                                                  - '@id': ada:parameter/solutionMcicpmsTAPP/torchDepth
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
                                                    const: ada:parameter/solutionMcicpmsTAPP/torchDepth
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/solutionMcicpmsTAPP/torchDepth
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
                                                    const: ada:parameter/solutionMcicpmsTAPP/makeUpGasAndFlowRate
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/solutionMcicpmsTAPP/makeUpGasAndFlowRate
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
                                                    const: ada:parameter/solutionMcicpmsTAPP/makeUpGasAndFlowRate
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/solutionMcicpmsTAPP/makeUpGasAndFlowRate
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
                                              - title: RF Power
                                                description: Radiofrequency forward
                                                  power applied to the plasma (W).
                                                  Controls ionization efficiency and
                                                  oxide production rates.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/solutionMcicpmsTAPP/rfPower
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/solutionMcicpmsTAPP/rfPower
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
                                              - title: Coolant (Plasma) Gas Flow Rate
                                                description: Flow rate of the outer
                                                  (coolant) argon gas stream (L/min).
                                                  Influences plasma temperature and
                                                  oxide ion formation.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/solutionMcicpmsTAPP/coolantGasFlowRate
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/solutionMcicpmsTAPP/coolantGasFlowRate
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
                                                  (auxiliary) argon gas stream between
                                                  torch body and injector tube (L/min).
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/solutionMcicpmsTAPP/auxiliaryGasFlowRate
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/solutionMcicpmsTAPP/auxiliaryGasFlowRate
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
                                            allOf:
                                            - contains:
                                                title: RF Power
                                                description: Radiofrequency forward
                                                  power applied to the plasma (W).
                                                  Controls ionization efficiency and
                                                  oxide production rates.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/solutionMcicpmsTAPP/rfPower
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/solutionMcicpmsTAPP/rfPower
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
                                            - contains:
                                                title: Coolant (Plasma) Gas Flow Rate
                                                description: Flow rate of the outer
                                                  (coolant) argon gas stream (L/min).
                                                  Influences plasma temperature and
                                                  oxide ion formation.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/solutionMcicpmsTAPP/coolantGasFlowRate
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/solutionMcicpmsTAPP/coolantGasFlowRate
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
                                                  (auxiliary) argon gas stream between
                                                  torch body and injector tube (L/min).
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/solutionMcicpmsTAPP/auxiliaryGasFlowRate
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/solutionMcicpmsTAPP/auxiliaryGasFlowRate
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
                                                  gas in KED mode (mL/min), on collision/reaction-cell-equipped
                                                  MC-ICP-MS instruments. Higher flow
                                                  rates provide greater interference
                                                  suppression at the cost of analyte
                                                  sensitivity. Record 'N/A' if the
                                                  instrument has no cell or KED mode
                                                  is not used. Record 'N/A' where
                                                  Collision/Reaction Cell (CRC) Configuration
                                                  does not include KED.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/solutionMcicpmsTAPP/collisionGasFlowRate
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/solutionMcicpmsTAPP/collisionGasFlowRate
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
                                                description: Kinetic energy discrimination
                                                  offset voltage applied at the exit
                                                  of the collision cell (V), on collision/reaction-cell-equipped
                                                  MC-ICP-MS instruments. Controls
                                                  the degree of polyatomic ion suppression.
                                                  Record 'N/A' if the instrument has
                                                  no cell or KED mode is not used.
                                                  Record 'N/A' where Collision/Reaction
                                                  Cell (CRC) Configuration does not
                                                  include KED.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/solutionMcicpmsTAPP/cellExitDiscriminationVoltage
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/solutionMcicpmsTAPP/cellExitDiscriminationVoltage
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
                                                description: Flow rate of the reaction
                                                  gas in DRC mode (mL/min), on collision/reaction-cell-equipped
                                                  MC-ICP-MS instruments. Record 'N/A'
                                                  if the instrument has no cell or
                                                  DRC mode is not used. Record 'N/A'
                                                  where Collision/Reaction Cell (CRC)
                                                  Configuration does not include DRC.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/solutionMcicpmsTAPP/reactionGasFlowRate
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/solutionMcicpmsTAPP/reactionGasFlowRate
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
                                                  gas in KED mode (mL/min), on collision/reaction-cell-equipped
                                                  MC-ICP-MS instruments. Higher flow
                                                  rates provide greater interference
                                                  suppression at the cost of analyte
                                                  sensitivity. Record 'N/A' if the
                                                  instrument has no cell or KED mode
                                                  is not used. Record 'N/A' where
                                                  Collision/Reaction Cell (CRC) Configuration
                                                  does not include KED.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/solutionMcicpmsTAPP/collisionGasFlowRate
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/solutionMcicpmsTAPP/collisionGasFlowRate
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
                                                description: Kinetic energy discrimination
                                                  offset voltage applied at the exit
                                                  of the collision cell (V), on collision/reaction-cell-equipped
                                                  MC-ICP-MS instruments. Controls
                                                  the degree of polyatomic ion suppression.
                                                  Record 'N/A' if the instrument has
                                                  no cell or KED mode is not used.
                                                  Record 'N/A' where Collision/Reaction
                                                  Cell (CRC) Configuration does not
                                                  include KED.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/solutionMcicpmsTAPP/cellExitDiscriminationVoltage
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/solutionMcicpmsTAPP/cellExitDiscriminationVoltage
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
                                                description: Flow rate of the reaction
                                                  gas in DRC mode (mL/min), on collision/reaction-cell-equipped
                                                  MC-ICP-MS instruments. Record 'N/A'
                                                  if the instrument has no cell or
                                                  DRC mode is not used. Record 'N/A'
                                                  where Collision/Reaction Cell (CRC)
                                                  Configuration does not include DRC.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/solutionMcicpmsTAPP/reactionGasFlowRate
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/solutionMcicpmsTAPP/reactionGasFlowRate
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
                                    title: Memory Effect Mitigation
                                    description: Procedure applied to minimize carryover
                                      of analyte isotopes between successive sample
                                      introductions. In MC-ICP-MS, extended rinse
                                      periods with the same acid matrix as samples
                                      (see Wash Time Between Samples) are the primary
                                      mitigation. At data processing level, documents
                                      any flagging or exclusion of measurements preceded
                                      by samples with significantly different isotopic
                                      compositions where carryover may be suspected.
                                    type: object
                                    properties:
                                      '@id':
                                        const: ada:parameter/solutionMcicpmsTAPP/memoryEffectMitigation
                                      '@type':
                                        const:
                                        - schema:PropertyValue
                                      schema:propertyID:
                                        const:
                                        - '@id': ada:parameter/solutionMcicpmsTAPP/memoryEffectMitigation
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
                                      title: Memory Effect Mitigation
                                      description: Procedure applied to minimize carryover
                                        of analyte isotopes between successive sample
                                        introductions. In MC-ICP-MS, extended rinse
                                        periods with the same acid matrix as samples
                                        (see Wash Time Between Samples) are the primary
                                        mitigation. At data processing level, documents
                                        any flagging or exclusion of measurements
                                        preceded by samples with significantly different
                                        isotopic compositions where carryover may
                                        be suspected.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/solutionMcicpmsTAPP/memoryEffectMitigation
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/solutionMcicpmsTAPP/memoryEffectMitigation
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
                                  description: "Name and reference material identifier
                                    of the isotopic reference standard used as the
                                    bracketing standard (SSB) or zero-delta anchor.
                                    This is an isotopic composition standard (not
                                    a concentration standard): it defines the isotopic
                                    composition against which all sample \u03B4 or
                                    \u03B5 values are normalized. Must be a pure,
                                    homogeneous, internationally distributed material
                                    with well-characterized isotopic composition.
                                    For double-spike procedures, also used for spike
                                    calibration. Include the material name, its source
                                    or supplier, and a citation for the accepted values
                                    used, since results calibrated against different
                                    published values for the same material are not
                                    directly comparable."
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
                                    material name and the isotopic composition reference
                                    source (certified value, consensus value, or literature
                                    compilation). For isotope ratio procedures, secondary
                                    RMs are geological materials with published isotopic
                                    compositions (e.g., BHVO-2 for Fe isotopes) or
                                    pure isotopic standards of certified composition.
                                  anyOf:
                                  - type: string
                                  - type: array
                                    items:
                                      type: string
                          required:
                          - ada:reagentRole
          schema:additionalProperty:
            type: array
            items:
              anyOf:
              - title: Signal Integration Time
                description: "Total integration time per sample solution (s). Calculated
                  from blocks \xD7 cycles per block \xD7 integration time per cycle.
                  Recorded at analysis level as the actual total time used."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/solutionMcicpmsTAPP/signalIntegrationTime
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/solutionMcicpmsTAPP/signalIntegrationTime
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
                description: "Total integration time per sample solution (s). Calculated
                  from blocks \xD7 cycles per block \xD7 integration time per cycle.
                  Recorded at analysis level as the actual total time used."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/solutionMcicpmsTAPP/signalIntegrationTime
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/solutionMcicpmsTAPP/signalIntegrationTime
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
    "cdif": "https://w3id.org/cdif/",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcat": "http://www.w3.org/ns/dcat#",
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

