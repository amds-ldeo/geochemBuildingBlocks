
# SEM Analysis Detail (Schema)

`ogch.techniqueProfile.geochemProfile.SEM.detail` *v0.1*

Dataset-level analysis-instance detail for SEM (superset), reusing CDIF/schema.org slots on the schema:Dataset root.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### detail example Garvie2008
detail instance derived from Garvie et al. 2008 | Tagish Lake (C2) nanoglobules | SE Imaging (FEI Nova 200 NanoLab).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Garvie2008",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Garvie2008",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA NNG06GE37G (LAJG); NASA NNG06GF08G (PRB)",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only — the Tagish Lake \"carbonaceous residue was attached to an Al-SEM stub\" (p.2); globules are identified by figure panel (\"A) Single sphere, B) three coalesced spheres, C) cluster of spheres …\", Fig. 1, p.2), not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N — an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Garvie2008",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Garvie2008",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA NNG06GE37G (LAJG); NASA NNG06GF08G (PRB)",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only \u2014 the Tagish Lake \"carbonaceous residue was attached to an Al-SEM stub\" (p.2); globules are identified by figure panel (\"A) Single sphere, B) three coalesced spheres, C) cluster of spheres \u2026\", Fig. 1, p.2), not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Garvie2008> a ada:SEMImage ;
    schema1:measurementTechnique <ex:semTAPP-Garvie2008> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA NNG06GE37G (LAJG); NASA NNG06GF08G (PRB)" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Sample name only — the Tagish Lake \"carbonaceous residue was attached to an Al-SEM stub\" (p.2); globules are identified by figure panel (\"A) Single sphere, B) three coalesced spheres, C) cluster of spheres …\", Fig. 1, p.2), not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "missing" .

<ex:semTAPP-Garvie2008> schema1:identifier "missing" .


```


### detail example Garvie2008-2
detail instance derived from Garvie et al. 2008 | Tagish Lake (C2) nanoglobules | TEM Sample Preparation (FIB, FEI Nova 200 NanoLab).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Garvie2008-2",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Garvie2008-2",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA NNG06GE37G (LAJG); NASA NNG06GF08G (PRB)",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only — the Tagish Lake carbonaceous residue on \"an Al-SEM stub\" (p.2); the globules sectioned by FIB are not given labels in the text",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N — a sample-preparation procedure produces sections rather than results to aggregate, and no selection rule for them is stated",
  "ada:combinedResults": "N — a sample-preparation procedure produces sections, not results to combine",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "N — a sample-preparation procedure produces sections, not results to combine",
  "ada:voxelSize": "missing"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Garvie2008-2",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Garvie2008-2",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA NNG06GE37G (LAJG); NASA NNG06GF08G (PRB)",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only \u2014 the Tagish Lake carbonaceous residue on \"an Al-SEM stub\" (p.2); the globules sectioned by FIB are not given labels in the text",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 a sample-preparation procedure produces sections rather than results to aggregate, and no selection rule for them is stated",
  "ada:combinedResults": "N \u2014 a sample-preparation procedure produces sections, not results to combine",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "N \u2014 a sample-preparation procedure produces sections, not results to combine",
  "ada:voxelSize": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Garvie2008-2> a ada:SEMImage ;
    schema1:measurementTechnique <ex:semTAPP-Garvie2008-2> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — a sample-preparation procedure produces sections rather than results to aggregate, and no selection rule for them is stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "N — a sample-preparation procedure produces sections, not results to combine" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA NNG06GE37G (LAJG); NASA NNG06GF08G (PRB)" ;
    ada:goodnessOfFitOrDispersionStatistic "N — a sample-preparation procedure produces sections, not results to combine" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Sample name only — the Tagish Lake carbonaceous residue on \"an Al-SEM stub\" (p.2); the globules sectioned by FIB are not given labels in the text" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "missing" .

<ex:semTAPP-Garvie2008-2> schema1:identifier "missing" .


```


### detail example Genge2025
detail instance derived from Genge et al. 2025 | Micrometeorite NG-1 (CV3-like) | BSE Imaging (ZEISS Sigma 1550VP, 10 kV).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Genge2025",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Genge2025",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only — the single particle \"micrometeorite NG-1\", analysed as \"the NG-1 section\" (p.2); regions are identified by figure panel (\"Alloy-rich regions\", Fig. 2; \"Silicate-dominated areas\", Fig. 3; pp.3–4), not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N — no count or rule is stated for this procedure. The paper's \"(n = 6)\" (p.4) is its SIMS oxygen-isotope population, not an SEM outcome",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Genge2025",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Genge2025",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only \u2014 the single particle \"micrometeorite NG-1\", analysed as \"the NG-1 section\" (p.2); regions are identified by figure panel (\"Alloy-rich regions\", Fig. 2; \"Silicate-dominated areas\", Fig. 3; pp.3\u20134), not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 no count or rule is stated for this procedure. The paper's \"(n = 6)\" (p.4) is its SIMS oxygen-isotope population, not an SEM outcome",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Genge2025> a ada:SEMImage ;
    schema1:measurementTechnique <ex:semTAPP-Genge2025> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — no count or rule is stated for this procedure. The paper's \"(n = 6)\" (p.4) is its SIMS oxygen-isotope population, not an SEM outcome" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Sample name only — the single particle \"micrometeorite NG-1\", analysed as \"the NG-1 section\" (p.2); regions are identified by figure panel (\"Alloy-rich regions\", Fig. 2; \"Silicate-dominated areas\", Fig. 3; pp.3–4), not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "missing" .

<ex:semTAPP-Genge2025> schema1:identifier "missing" .


```


### detail example Genge2025-2
detail instance derived from Genge et al. 2025 | Micrometeorite NG-1 (CV3-like) | EDS Point Analysis (ZEISS Sigma 1550VP, 10 kV).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Genge2025-2",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Genge2025-2",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only — the single particle \"micrometeorite NG-1\", analysed as \"the NG-1 section\" (p.2); regions are identified by figure panel (\"Alloy-rich regions\", Fig. 2; \"Silicate-dominated areas\", Fig. 3; pp.3–4), not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N — no count or rule is stated for this procedure. The paper's \"(n = 6)\" (p.4) is its SIMS oxygen-isotope population, not an SEM outcome",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Genge2025-2",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Genge2025-2",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only \u2014 the single particle \"micrometeorite NG-1\", analysed as \"the NG-1 section\" (p.2); regions are identified by figure panel (\"Alloy-rich regions\", Fig. 2; \"Silicate-dominated areas\", Fig. 3; pp.3\u20134), not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 no count or rule is stated for this procedure. The paper's \"(n = 6)\" (p.4) is its SIMS oxygen-isotope population, not an SEM outcome",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Genge2025-2> a ada:SEMImage ;
    schema1:measurementTechnique <ex:semTAPP-Genge2025-2> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — no count or rule is stated for this procedure. The paper's \"(n = 6)\" (p.4) is its SIMS oxygen-isotope population, not an SEM outcome" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Sample name only — the single particle \"micrometeorite NG-1\", analysed as \"the NG-1 section\" (p.2); regions are identified by figure panel (\"Alloy-rich regions\", Fig. 2; \"Silicate-dominated areas\", Fig. 3; pp.3–4), not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "missing" .

<ex:semTAPP-Genge2025-2> schema1:identifier "missing" .


```


### detail example Genge2025-3
detail instance derived from Genge et al. 2025 | Micrometeorite NG-1 (CV3-like) | EBSD (ZEISS Sigma 1550VP, 20 kV).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Genge2025-3",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Genge2025-3",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only — the single particle \"micrometeorite NG-1\", analysed as \"the NG-1 section\" (p.2); regions are identified by figure panel (\"Alloy-rich regions\", Fig. 2; \"Silicate-dominated areas\", Fig. 3; pp.3–4), not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N — no count or rule is stated for this procedure. The paper's \"(n = 6)\" (p.4) is its SIMS oxygen-isotope population, not an SEM outcome",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Genge2025-3",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Genge2025-3",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only \u2014 the single particle \"micrometeorite NG-1\", analysed as \"the NG-1 section\" (p.2); regions are identified by figure panel (\"Alloy-rich regions\", Fig. 2; \"Silicate-dominated areas\", Fig. 3; pp.3\u20134), not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 no count or rule is stated for this procedure. The paper's \"(n = 6)\" (p.4) is its SIMS oxygen-isotope population, not an SEM outcome",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Genge2025-3> a ada:SEMImage ;
    schema1:measurementTechnique <ex:semTAPP-Genge2025-3> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — no count or rule is stated for this procedure. The paper's \"(n = 6)\" (p.4) is its SIMS oxygen-isotope population, not an SEM outcome" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Sample name only — the single particle \"micrometeorite NG-1\", analysed as \"the NG-1 section\" (p.2); regions are identified by figure panel (\"Alloy-rich regions\", Fig. 2; \"Silicate-dominated areas\", Fig. 3; pp.3–4), not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "missing" .

<ex:semTAPP-Genge2025-3> schema1:identifier "missing" .


```


### detail example Gucsik2013
detail instance derived from Gucsik et al. 2013 | Forsterite, Kaba meteorite (CV3) | CL Mapping (JEOL JSM-5410LV).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Gucsik2013",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Gucsik2013",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Labelled: \"seven representative grains (designated as B-1 through B-7)\" of \"a Kaba thin section\" (p.2), shown as the \"analyzed areas\" in Fig. 1 (p.2)",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N — the seven grains are chosen before analysis (recorded under Sampling Unit Selection Criteria), not admitted to or excluded from an aggregate; no contributing count or rejection rule is stated",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Gucsik2013",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Gucsik2013",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Labelled: \"seven representative grains (designated as B-1 through B-7)\" of \"a Kaba thin section\" (p.2), shown as the \"analyzed areas\" in Fig. 1 (p.2)",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 the seven grains are chosen before analysis (recorded under Sampling Unit Selection Criteria), not admitted to or excluded from an aggregate; no contributing count or rejection rule is stated",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Gucsik2013> a ada:SEMImage ;
    schema1:measurementTechnique <ex:semTAPP-Gucsik2013> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — the seven grains are chosen before analysis (recorded under Sampling Unit Selection Criteria), not admitted to or excluded from an aggregate; no contributing count or rejection rule is stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Labelled: \"seven representative grains (designated as B-1 through B-7)\" of \"a Kaba thin section\" (p.2), shown as the \"analyzed areas\" in Fig. 1 (p.2)" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "missing" .

<ex:semTAPP-Gucsik2013> schema1:identifier "missing" .


```


### detail example Gucsik2013-2
detail instance derived from Gucsik et al. 2013 | Forsterite, Kaba meteorite (CV3) | EDS Point Analysis (JEOL JSM-5410LV).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Gucsik2013-2",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Gucsik2013-2",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Labelled: \"seven representative grains (designated as B-1 through B-7)\" of \"a Kaba thin section\" (p.2), shown as the \"analyzed areas\" in Fig. 1 (p.2)",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N — no contributing count and no acceptance or rejection rule is stated; the grain selection is recorded under Sampling Unit Selection Criteria",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Gucsik2013-2",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Gucsik2013-2",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Labelled: \"seven representative grains (designated as B-1 through B-7)\" of \"a Kaba thin section\" (p.2), shown as the \"analyzed areas\" in Fig. 1 (p.2)",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 no contributing count and no acceptance or rejection rule is stated; the grain selection is recorded under Sampling Unit Selection Criteria",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Gucsik2013-2> a ada:SEMImage ;
    schema1:measurementTechnique <ex:semTAPP-Gucsik2013-2> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — no contributing count and no acceptance or rejection rule is stated; the grain selection is recorded under Sampling Unit Selection Criteria" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Labelled: \"seven representative grains (designated as B-1 through B-7)\" of \"a Kaba thin section\" (p.2), shown as the \"analyzed areas\" in Fig. 1 (p.2)" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "missing" .

<ex:semTAPP-Gucsik2013-2> schema1:identifier "missing" .


```


### detail example Izawa2010
detail instance derived from Izawa et al. 2010 | Tagish Lake (C2) meteorite | CL Mapping (Hitachi S-2500C).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Izawa2010",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Izawa2010",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only — \"polished thin sections\" of Tagish Lake (p.2), not individually labelled; the numbered points of Table 1 and Fig. 1 (e.g. \"point #1\", \"spot 34\") are μXRD spots, not SEM-CL",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N — an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Izawa2010",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Izawa2010",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only \u2014 \"polished thin sections\" of Tagish Lake (p.2), not individually labelled; the numbered points of Table 1 and Fig. 1 (e.g. \"point #1\", \"spot 34\") are \u03bcXRD spots, not SEM-CL",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Izawa2010> a ada:SEMImage ;
    schema1:measurementTechnique <ex:semTAPP-Izawa2010> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Sample name only — \"polished thin sections\" of Tagish Lake (p.2), not individually labelled; the numbered points of Table 1 and Fig. 1 (e.g. \"point #1\", \"spot 34\") are μXRD spots, not SEM-CL" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "missing" .

<ex:semTAPP-Izawa2010> schema1:identifier "missing" .


```


### detail example Izawa2010-2
detail instance derived from Izawa et al. 2010 | Tagish Lake (C2) meteorite | BSE Imaging (Leo 440).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Izawa2010-2",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Izawa2010-2",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only — \"the Tagish Lake sections\" (p.3), not individually labelled; the numbered points of Table 1 and Fig. 1 (e.g. \"point #1\", \"spot 34\") are μXRD spots, not SEM analyses",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N — an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Izawa2010-2",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Izawa2010-2",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only \u2014 \"the Tagish Lake sections\" (p.3), not individually labelled; the numbered points of Table 1 and Fig. 1 (e.g. \"point #1\", \"spot 34\") are \u03bcXRD spots, not SEM analyses",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Izawa2010-2> a ada:SEMImage ;
    schema1:measurementTechnique <ex:semTAPP-Izawa2010-2> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Sample name only — \"the Tagish Lake sections\" (p.3), not individually labelled; the numbered points of Table 1 and Fig. 1 (e.g. \"point #1\", \"spot 34\") are μXRD spots, not SEM analyses" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "missing" .

<ex:semTAPP-Izawa2010-2> schema1:identifier "missing" .


```


### detail example Izawa2010-3
detail instance derived from Izawa et al. 2010 | Tagish Lake (C2) meteorite | EDS Mapping (Leo 440).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Izawa2010-3",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Izawa2010-3",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only — \"the Tagish Lake sections\" (p.3), not individually labelled; the numbered points of Table 1 and Fig. 1 (e.g. \"point #1\", \"spot 34\") are μXRD spots, not SEM analyses",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N — an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": "all: 0.5 wt% — 'with a detection limit of 0.5 wt% for most elements' (p.3), a capability of the Quartz XOne system",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Izawa2010-3",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Izawa2010-3",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only \u2014 \"the Tagish Lake sections\" (p.3), not individually labelled; the numbered points of Table 1 and Fig. 1 (e.g. \"point #1\", \"spot 34\") are \u03bcXRD spots, not SEM analyses",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": "all: 0.5 wt% \u2014 'with a detection limit of 0.5 wt% for most elements' (p.3), a capability of the Quartz XOne system",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Izawa2010-3> a ada:SEMImage ;
    schema1:measurementTechnique <ex:semTAPP-Izawa2010-3> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "all: 0.5 wt% — 'with a detection limit of 0.5 wt% for most elements' (p.3), a capability of the Quartz XOne system" ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Sample name only — \"the Tagish Lake sections\" (p.3), not individually labelled; the numbered points of Table 1 and Fig. 1 (e.g. \"point #1\", \"spot 34\") are μXRD spots, not SEM analyses" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "missing" .

<ex:semTAPP-Izawa2010-3> schema1:identifier "missing" .


```


### detail example Izawa2010-4
detail instance derived from Izawa et al. 2010 | Tagish Lake (C2) meteorite | BSE Imaging (Leo 1540 FIB/SEM CrossBeam).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Izawa2010-4",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Izawa2010-4",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only — \"the Tagish Lake sections\" (p.3), not individually labelled; the numbered points of Table 1 and Fig. 1 (e.g. \"point #1\", \"spot 34\") are μXRD spots, not SEM analyses",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N — an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Izawa2010-4",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Izawa2010-4",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only \u2014 \"the Tagish Lake sections\" (p.3), not individually labelled; the numbered points of Table 1 and Fig. 1 (e.g. \"point #1\", \"spot 34\") are \u03bcXRD spots, not SEM analyses",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Izawa2010-4> a ada:SEMImage ;
    schema1:measurementTechnique <ex:semTAPP-Izawa2010-4> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Sample name only — \"the Tagish Lake sections\" (p.3), not individually labelled; the numbered points of Table 1 and Fig. 1 (e.g. \"point #1\", \"spot 34\") are μXRD spots, not SEM analyses" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "missing" .

<ex:semTAPP-Izawa2010-4> schema1:identifier "missing" .


```


### detail example Izawa2010-5
detail instance derived from Izawa et al. 2010 | Tagish Lake (C2) meteorite | EDS Point Analysis (Leo 1540 FIB/SEM CrossBeam).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Izawa2010-5",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Izawa2010-5",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only — \"the Tagish Lake sections\" (p.3), not individually labelled; the numbered points of Table 1 and Fig. 1 (e.g. \"point #1\", \"spot 34\") are μXRD spots, not SEM analyses",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N — compositions are reported by phase with no contributing count and no acceptance or rejection rule stated",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Izawa2010-5",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Izawa2010-5",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Sample name only \u2014 \"the Tagish Lake sections\" (p.3), not individually labelled; the numbered points of Table 1 and Fig. 1 (e.g. \"point #1\", \"spot 34\") are \u03bcXRD spots, not SEM analyses",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 compositions are reported by phase with no contributing count and no acceptance or rejection rule stated",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Izawa2010-5> a ada:SEMImage ;
    schema1:measurementTechnique <ex:semTAPP-Izawa2010-5> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — compositions are reported by phase with no contributing count and no acceptance or rejection rule stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Sample name only — \"the Tagish Lake sections\" (p.3), not individually labelled; the numbered points of Table 1 and Fig. 1 (e.g. \"point #1\", \"spot 34\") are μXRD spots, not SEM analyses" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "missing" .

<ex:semTAPP-Izawa2010-5> schema1:identifier "missing" .


```


### detail example Liu2017
detail instance derived from Liu et al. 2017 | High-rank coal (Qinshui basin) | 3D Tomography (Carl Zeiss Crossbeam 540).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Liu2017",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Liu2017",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Labelled: coal samples \"#1\" (Bofang Mine) and \"#2\" (Yuwu Mine) (Table 1, p.2); the 3D pore-network model \"only focuses on the coal sample #1\" (p.8)",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "9.8 × 9.8 × 15 nm voxel size; 600 slices; 7.8 × 7.8 µm scanning area; 9.0 µm total thickness",
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N — the pore statistics integrate the whole segmented volume rather than admitting or excluding results; the only stated restriction is of scope, the model focusing \"only ... on the coal sample #1\" (p.8)",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Liu2017",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Liu2017",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Labelled: coal samples \"#1\" (Bofang Mine) and \"#2\" (Yuwu Mine) (Table 1, p.2); the 3D pore-network model \"only focuses on the coal sample #1\" (p.8)",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "9.8 \u00d7 9.8 \u00d7 15 nm voxel size; 600 slices; 7.8 \u00d7 7.8 \u00b5m scanning area; 9.0 \u00b5m total thickness",
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 the pore statistics integrate the whole segmented volume rather than admitting or excluding results; the only stated restriction is of scope, the model focusing \"only ... on the coal sample #1\" (p.8)",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Liu2017> a ada:SEMImage ;
    schema1:measurementTechnique <ex:semTAPP-Liu2017> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — the pore statistics integrate the whole segmented volume rather than admitting or excluding results; the only stated restriction is of scope, the model focusing \"only ... on the coal sample #1\" (p.8)" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "9.8 × 9.8 × 15 nm voxel size; 600 slices; 7.8 × 7.8 µm scanning area; 9.0 µm total thickness" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Labelled: coal samples \"#1\" (Bofang Mine) and \"#2\" (Yuwu Mine) (Table 1, p.2); the 3D pore-network model \"only focuses on the coal sample #1\" (p.8)" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "missing" .

<ex:semTAPP-Liu2017> schema1:identifier "missing" .


```


### detail example Liu2017-2
detail instance derived from Liu et al. 2017 | High-rank coal (Qinshui basin) | SE Imaging (ESEM Quanta 250).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Liu2017-2",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Liu2017-2",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Labelled: coal samples \"#1\" (Bofang Mine) and \"#2\" (Yuwu Mine) (Table 1, p.2); imaged areas are not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N — an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Liu2017-2",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Liu2017-2",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Labelled: coal samples \"#1\" (Bofang Mine) and \"#2\" (Yuwu Mine) (Table 1, p.2); imaged areas are not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Liu2017-2> a ada:SEMImage ;
    schema1:measurementTechnique <ex:semTAPP-Liu2017-2> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Labelled: coal samples \"#1\" (Bofang Mine) and \"#2\" (Yuwu Mine) (Table 1, p.2); imaged areas are not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "missing" .

<ex:semTAPP-Liu2017-2> schema1:identifier "missing" .


```


### detail example Liu2017-3
detail instance derived from Liu et al. 2017 | High-rank coal (Qinshui basin) | SE Imaging (FESEM SUPRA 55).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Liu2017-3",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Liu2017-3",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Labelled: coal samples \"#1\" (Bofang Mine) and \"#2\" (Yuwu Mine) (Table 1, p.2); imaged areas are not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N — an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Liu2017-3",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Liu2017-3",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "Labelled: coal samples \"#1\" (Bofang Mine) and \"#2\" (Yuwu Mine) (Table 1, p.2); imaged areas are not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Liu2017-3> a ada:SEMImage ;
    schema1:measurementTechnique <ex:semTAPP-Liu2017-3> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "Labelled: coal samples \"#1\" (Bofang Mine) and \"#2\" (Yuwu Mine) (Table 1, p.2); imaged areas are not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "missing" .

<ex:semTAPP-Liu2017-3> schema1:identifier "missing" .


```


### detail example Ma2017
detail instance derived from Ma et al. 2017 | Khatyrka CV3 chondrite (metal phases) | BSE Imaging (ZEISS 1550VP FE-SEM).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Ma2017",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Ma2017",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NSF EAR-0318518; NSF DMR-0080065 (supporting Caltech GPS Analytical Facility)",
  "ada:sampleName": "Section 126A (USNM 7908)",
  "ada:samplingUnitName": "Labelled: \"section 126A of USNM 7908\" (p.1), \"prepared from a larger Grain 126\" (p.2); the three mineral locations are \"marked by rectangles\" in Fig. 1 (p.2), not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N — no count or rule is stated for the SEM work. The contributing counts in this paper (\"n = 4\", \"n = 8\", \"n = 15\", \"n = 65\", \"n = 3\"; Table 1, p.2) belong to its EPMA analyses and are not borrowed",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Ma2017",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Ma2017",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NSF EAR-0318518; NSF DMR-0080065 (supporting Caltech GPS Analytical Facility)",
  "ada:sampleName": "Section 126A (USNM 7908)",
  "ada:samplingUnitName": "Labelled: \"section 126A of USNM 7908\" (p.1), \"prepared from a larger Grain 126\" (p.2); the three mineral locations are \"marked by rectangles\" in Fig. 1 (p.2), not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 no count or rule is stated for the SEM work. The contributing counts in this paper (\"n = 4\", \"n = 8\", \"n = 15\", \"n = 65\", \"n = 3\"; Table 1, p.2) belong to its EPMA analyses and are not borrowed",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Ma2017> a ada:SEMImage ;
    schema1:measurementTechnique <ex:semTAPP-Ma2017> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — no count or rule is stated for the SEM work. The contributing counts in this paper (\"n = 4\", \"n = 8\", \"n = 15\", \"n = 65\", \"n = 3\"; Table 1, p.2) belong to its EPMA analyses and are not borrowed" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NSF EAR-0318518; NSF DMR-0080065 (supporting Caltech GPS Analytical Facility)" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "Section 126A (USNM 7908)" ;
    ada:samplingUnitName "Labelled: \"section 126A of USNM 7908\" (p.1), \"prepared from a larger Grain 126\" (p.2); the three mineral locations are \"marked by rectangles\" in Fig. 1 (p.2), not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "missing" .

<ex:semTAPP-Ma2017> schema1:identifier "missing" .


```


### detail example Ma2017-2
detail instance derived from Ma et al. 2017 | Khatyrka CV3 chondrite (metal phases) | EBSD (ZEISS 1550VP FE-SEM, HKL system, 20 kV).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Ma2017-2",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Ma2017-2",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NSF EAR-0318518; NSF DMR-0080065 (supporting Caltech GPS Analytical Facility)",
  "ada:sampleName": "Section 126A (USNM 7908)",
  "ada:samplingUnitName": "Labelled: \"section 126A of USNM 7908\" (p.1), \"prepared from a larger Grain 126\" (p.2); the three mineral locations are \"marked by rectangles\" in Fig. 1 (p.2), not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N — no count or rule is stated for the SEM work. The contributing counts in this paper (\"n = 4\", \"n = 8\", \"n = 15\", \"n = 65\", \"n = 3\"; Table 1, p.2) belong to its EPMA analyses and are not borrowed",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": 0.3,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Ma2017-2",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Ma2017-2",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NSF EAR-0318518; NSF DMR-0080065 (supporting Caltech GPS Analytical Facility)",
  "ada:sampleName": "Section 126A (USNM 7908)",
  "ada:samplingUnitName": "Labelled: \"section 126A of USNM 7908\" (p.1), \"prepared from a larger Grain 126\" (p.2); the three mineral locations are \"marked by rectangles\" in Fig. 1 (p.2), not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 no count or rule is stated for the SEM work. The contributing counts in this paper (\"n = 4\", \"n = 8\", \"n = 15\", \"n = 65\", \"n = 3\"; Table 1, p.2) belong to its EPMA analyses and are not borrowed",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": 0.3,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Ma2017-2> a ada:SEMImage ;
    schema1:measurementTechnique <ex:semTAPP-Ma2017-2> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — no count or rule is stated for the SEM work. The contributing counts in this paper (\"n = 4\", \"n = 8\", \"n = 15\", \"n = 65\", \"n = 3\"; Table 1, p.2) belong to its EPMA analyses and are not borrowed" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation 3e-01 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NSF EAR-0318518; NSF DMR-0080065 (supporting Caltech GPS Analytical Facility)" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "Section 126A (USNM 7908)" ;
    ada:samplingUnitName "Labelled: \"section 126A of USNM 7908\" (p.1), \"prepared from a larger Grain 126\" (p.2); the three mineral locations are \"marked by rectangles\" in Fig. 1 (p.2), not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "missing" .

<ex:semTAPP-Ma2017-2> schema1:identifier "missing" .


```


### detail example Pascucci2026
detail instance derived from Pascucci et al. 2026 | NWA 7317 CR6 chondrite | BSE Imaging (Zeiss Supra 40 FE-SEM, 20 kV).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Pascucci2026",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Pascucci2026",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "NWA 7317",
  "ada:samplingUnitName": "Sample name only — \"the NWA 7317 slab\" (p.3), imaged on \"almost the same portion of the VIS-IR SPIM images\" (p.4); imaged fields and analysis points are not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N — an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Pascucci2026",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Pascucci2026",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "NWA 7317",
  "ada:samplingUnitName": "Sample name only \u2014 \"the NWA 7317 slab\" (p.3), imaged on \"almost the same portion of the VIS-IR SPIM images\" (p.4); imaged fields and analysis points are not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Pascucci2026> a ada:SEMImage ;
    schema1:measurementTechnique <ex:semTAPP-Pascucci2026> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "NWA 7317" ;
    ada:samplingUnitName "Sample name only — \"the NWA 7317 slab\" (p.3), imaged on \"almost the same portion of the VIS-IR SPIM images\" (p.4); imaged fields and analysis points are not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "missing" .

<ex:semTAPP-Pascucci2026> schema1:identifier "missing" .


```


### detail example Pascucci2026-2
detail instance derived from Pascucci et al. 2026 | NWA 7317 CR6 chondrite | EDS Point Analysis (Zeiss Supra 40 FE-SEM, 20 kV).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Pascucci2026-2",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Pascucci2026-2",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "NWA 7317",
  "ada:samplingUnitName": "Sample name only — \"the NWA 7317 slab\" (p.3), imaged on \"almost the same portion of the VIS-IR SPIM images\" (p.4); imaged fields and analysis points are not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N — compositions are reported by phase with no contributing count and no acceptance or rejection rule stated",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Pascucci2026-2",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Pascucci2026-2",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "NWA 7317",
  "ada:samplingUnitName": "Sample name only \u2014 \"the NWA 7317 slab\" (p.3), imaged on \"almost the same portion of the VIS-IR SPIM images\" (p.4); imaged fields and analysis points are not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 compositions are reported by phase with no contributing count and no acceptance or rejection rule stated",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Pascucci2026-2> a ada:SEMImage ;
    schema1:measurementTechnique <ex:semTAPP-Pascucci2026-2> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — compositions are reported by phase with no contributing count and no acceptance or rejection rule stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "NWA 7317" ;
    ada:samplingUnitName "Sample name only — \"the NWA 7317 slab\" (p.3), imaged on \"almost the same portion of the VIS-IR SPIM images\" (p.4); imaged fields and analysis points are not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "missing" .

<ex:semTAPP-Pascucci2026-2> schema1:identifier "missing" .


```


### detail example Pascucci2026-3
detail instance derived from Pascucci et al. 2026 | NWA 7317 CR6 chondrite | EDS Mapping (Zeiss Supra 40 FE-SEM, 20 kV).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Pascucci2026-3",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Pascucci2026-3",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "NWA 7317",
  "ada:samplingUnitName": "Sample name only — \"the NWA 7317 slab\" (p.3), imaged on \"almost the same portion of the VIS-IR SPIM images\" (p.4); imaged fields and analysis points are not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": 1024,
  "ada:mapArea": 10.5,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N — an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Pascucci2026-3",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Pascucci2026-3",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "NWA 7317",
  "ada:samplingUnitName": "Sample name only \u2014 \"the NWA 7317 slab\" (p.3), imaged on \"almost the same portion of the VIS-IR SPIM images\" (p.4); imaged fields and analysis points are not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": 1024,
  "ada:mapArea": 10.5,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Pascucci2026-3> a ada:SEMImage ;
    schema1:measurementTechnique <ex:semTAPP-Pascucci2026-3> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea 1.05e+01 ;
    ada:mapDimensions 1024 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "NWA 7317" ;
    ada:samplingUnitName "Sample name only — \"the NWA 7317 slab\" (p.3), imaged on \"almost the same portion of the VIS-IR SPIM images\" (p.4); imaged fields and analysis points are not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "missing" .

<ex:semTAPP-Pascucci2026-3> schema1:identifier "missing" .


```


### detail example Pascucci2026-4
detail instance derived from Pascucci et al. 2026 | NWA 7317 CR6 chondrite | SE Imaging (Zeiss Supra 40 FE-SEM).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Pascucci2026-4",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Pascucci2026-4",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "NWA 7317",
  "ada:samplingUnitName": "Sample name only — \"the NWA 7317 slab\" (p.3), imaged on \"almost the same portion of the VIS-IR SPIM images\" (p.4); imaged fields and analysis points are not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N — an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Pascucci2026-4",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Pascucci2026-4",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "NWA 7317",
  "ada:samplingUnitName": "Sample name only \u2014 \"the NWA 7317 slab\" (p.3), imaged on \"almost the same portion of the VIS-IR SPIM images\" (p.4); imaged fields and analysis points are not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Pascucci2026-4> a ada:SEMImage ;
    schema1:measurementTechnique <ex:semTAPP-Pascucci2026-4> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "NWA 7317" ;
    ada:samplingUnitName "Sample name only — \"the NWA 7317 slab\" (p.3), imaged on \"almost the same portion of the VIS-IR SPIM images\" (p.4); imaged fields and analysis points are not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "missing" .

<ex:semTAPP-Pascucci2026-4> schema1:identifier "missing" .


```


### detail example Zhou2017
detail instance derived from Zhou et al. 2017 | Coal (SC + HBC, Junggar Basin) | 3D Tomography (FEI Helios NanoLab 650).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Zhou2017",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Zhou2017",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "SC; HBC",
  "ada:samplingUnitName": "Sample name only — \"subbituminous coal (SC) and high-volatile bituminous coal (HBC)\" (p.1), one FIB-SEM volume each; the numbered images (e.g. \"1st\", \"300th\" of sample SC, p.2) are slices, not units",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "14.8×14.8 nm pixel size (XY); ~800 total slices; sub-volumes: SC=5.609×3.08×5.446 µm; HBC=4.679×3.2×4.24 µm; SEM image resolution 2.5 nm",
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N — no results are admitted or excluded; the volume's adequacy is assessed instead, under \"evaluation of representative volumes\" (§2.3, p.4), and the reported statistics integrate all ~800 slices",
  "ada:combinedResults": "SC pore diameter; HBC pore diameter; SC throat size (516 throats); HBC throat size (715 throats); SC throat length per size class; HBC throat length per size class — Conclusions and Table 5; the number of pores averaged is not stated",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Zhou2017",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Zhou2017",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "SC; HBC",
  "ada:samplingUnitName": "Sample name only \u2014 \"subbituminous coal (SC) and high-volatile bituminous coal (HBC)\" (p.1), one FIB-SEM volume each; the numbered images (e.g. \"1st\", \"300th\" of sample SC, p.2) are slices, not units",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "14.8\u00d714.8 nm pixel size (XY); ~800 total slices; sub-volumes: SC=5.609\u00d73.08\u00d75.446 \u00b5m; HBC=4.679\u00d73.2\u00d74.24 \u00b5m; SEM image resolution 2.5 nm",
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 no results are admitted or excluded; the volume's adequacy is assessed instead, under \"evaluation of representative volumes\" (\u00a72.3, p.4), and the reported statistics integrate all ~800 slices",
  "ada:combinedResults": "SC pore diameter; HBC pore diameter; SC throat size (516 throats); HBC throat size (715 throats); SC throat length per size class; HBC throat length per size class \u2014 Conclusions and Table 5; the number of pores averaged is not stated",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Zhou2017> a ada:SEMImage ;
    schema1:measurementTechnique <ex:semTAPP-Zhou2017> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — no results are admitted or excluded; the volume's adequacy is assessed instead, under \"evaluation of representative volumes\" (§2.3, p.4), and the reported statistics integrate all ~800 slices" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "SC pore diameter; HBC pore diameter; SC throat size (516 throats); HBC throat size (715 throats); SC throat length per size class; HBC throat length per size class — Conclusions and Table 5; the number of pores averaged is not stated" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "14.8×14.8 nm pixel size (XY); ~800 total slices; sub-volumes: SC=5.609×3.08×5.446 µm; HBC=4.679×3.2×4.24 µm; SEM image resolution 2.5 nm" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "SC; HBC" ;
    ada:samplingUnitName "Sample name only — \"subbituminous coal (SC) and high-volatile bituminous coal (HBC)\" (p.1), one FIB-SEM volume each; the numbered images (e.g. \"1st\", \"300th\" of sample SC, p.2) are slices, not units" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "missing" .

<ex:semTAPP-Zhou2017> schema1:identifier "missing" .


```


### detail example Zega2025
detail instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | BSE Imaging (JEOL 7600F, NASA JSC, 15 kV).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Zega2025",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Zega2025",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "N — the JSC SEM passage names no specimen (\"The particle was attached to an Al cylinder SEM mount\"; \"regions of interest\", p.9); the paper's OREX numbers identify figures, not this laboratory's analyses",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N — an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Zega2025",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Zega2025",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "N \u2014 the JSC SEM passage names no specimen (\"The particle was attached to an Al cylinder SEM mount\"; \"regions of interest\", p.9); the paper's OREX numbers identify figures, not this laboratory's analyses",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Zega2025> a ada:SEMImage ;
    schema1:measurementTechnique <ex:semTAPP-Zega2025> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "N — the JSC SEM passage names no specimen (\"The particle was attached to an Al cylinder SEM mount\"; \"regions of interest\", p.9); the paper's OREX numbers identify figures, not this laboratory's analyses" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "missing" .

<ex:semTAPP-Zega2025> schema1:identifier "missing" .


```


### detail example Zega2025-2
detail instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | EDS Point Analysis (JEOL 7600F, NASA JSC, 15 kV).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Zega2025-2",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Zega2025-2",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "N — the JSC SEM passage names no specimen (\"The particle was attached to an Al cylinder SEM mount\"; \"regions of interest\", p.9); the paper's OREX numbers identify figures, not this laboratory's analyses",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N — compositions are reported by phase with no contributing count and no acceptance or rejection rule stated",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Zega2025-2",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Zega2025-2",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "N \u2014 the JSC SEM passage names no specimen (\"The particle was attached to an Al cylinder SEM mount\"; \"regions of interest\", p.9); the paper's OREX numbers identify figures, not this laboratory's analyses",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 compositions are reported by phase with no contributing count and no acceptance or rejection rule stated",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Zega2025-2> a ada:SEMImage ;
    schema1:measurementTechnique <ex:semTAPP-Zega2025-2> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — compositions are reported by phase with no contributing count and no acceptance or rejection rule stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "N — the JSC SEM passage names no specimen (\"The particle was attached to an Al cylinder SEM mount\"; \"regions of interest\", p.9); the paper's OREX numbers identify figures, not this laboratory's analyses" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "missing" .

<ex:semTAPP-Zega2025-2> schema1:identifier "missing" .


```


### detail example Zega2025-3
detail instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | SE Imaging (Hitachi S-4800, U Arizona).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Zega2025-3",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Zega2025-3",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "N — the Arizona SEM passage names no specimen (\"Polished sections were coated with a thin layer ... of carbon\", p.9); the paper's OREX numbers identify figures, not this laboratory's analyses",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N — an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Zega2025-3",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Zega2025-3",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "N \u2014 the Arizona SEM passage names no specimen (\"Polished sections were coated with a thin layer ... of carbon\", p.9); the paper's OREX numbers identify figures, not this laboratory's analyses",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Zega2025-3> a ada:SEMImage ;
    schema1:measurementTechnique <ex:semTAPP-Zega2025-3> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "N — the Arizona SEM passage names no specimen (\"Polished sections were coated with a thin layer ... of carbon\", p.9); the paper's OREX numbers identify figures, not this laboratory's analyses" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "missing" .

<ex:semTAPP-Zega2025-3> schema1:identifier "missing" .


```


### detail example Zega2025-4
detail instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | BSE Imaging (Hitachi S-4800, U Arizona).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Zega2025-4",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Zega2025-4",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "N — the Arizona SEM passage names no specimen (\"Polished sections were coated with a thin layer ... of carbon\", p.9); the paper's OREX numbers identify figures, not this laboratory's analyses",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N — an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Zega2025-4",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Zega2025-4",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "N \u2014 the Arizona SEM passage names no specimen (\"Polished sections were coated with a thin layer ... of carbon\", p.9); the paper's OREX numbers identify figures, not this laboratory's analyses",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Zega2025-4> a ada:SEMImage ;
    schema1:measurementTechnique <ex:semTAPP-Zega2025-4> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "N — the Arizona SEM passage names no specimen (\"Polished sections were coated with a thin layer ... of carbon\", p.9); the paper's OREX numbers identify figures, not this laboratory's analyses" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "missing" .

<ex:semTAPP-Zega2025-4> schema1:identifier "missing" .


```


### detail example Zega2025-5
detail instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | EDS Mapping (Hitachi S-4800, U Arizona).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Zega2025-5",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Zega2025-5",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "N — the Arizona SEM passage names no specimen (\"Polished sections were coated with a thin layer ... of carbon\", p.9); the paper's OREX numbers identify figures, not this laboratory's analyses",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N — an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Zega2025-5",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Zega2025-5",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "N \u2014 the Arizona SEM passage names no specimen (\"Polished sections were coated with a thin layer ... of carbon\", p.9); the paper's OREX numbers identify figures, not this laboratory's analyses",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Zega2025-5> a ada:SEMImage ;
    schema1:measurementTechnique <ex:semTAPP-Zega2025-5> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "N — the Arizona SEM passage names no specimen (\"Polished sections were coated with a thin layer ... of carbon\", p.9); the paper's OREX numbers identify figures, not this laboratory's analyses" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "missing" .

<ex:semTAPP-Zega2025-5> schema1:identifier "missing" .


```


### detail example Zega2025-6
detail instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | TEM Sample Preparation (Helios G3, U Arizona).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Zega2025-6",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Zega2025-6",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA PSEF 80NSSC23K0327; NASA Planetary Major Equipment NNX12AL47G; NSF MRI 0619599",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "N — \"All sections were extracted from varied regions of matrix within the particles\" (p.9), none named; the paper labels FIB sections (e.g. OREX-803095-100, OREX-501005-100, OREX-803031-101; Figs 2–4) without attributing them to a laboratory",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N — a sample-preparation procedure produces sections rather than results to aggregate (p.9)",
  "ada:combinedResults": "N — a sample-preparation procedure produces sections, not results to combine",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "N — a sample-preparation procedure produces sections, not results to combine",
  "ada:voxelSize": "missing"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Zega2025-6",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Zega2025-6",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA PSEF 80NSSC23K0327; NASA Planetary Major Equipment NNX12AL47G; NSF MRI 0619599",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "N \u2014 \"All sections were extracted from varied regions of matrix within the particles\" (p.9), none named; the paper labels FIB sections (e.g. OREX-803095-100, OREX-501005-100, OREX-803031-101; Figs 2\u20134) without attributing them to a laboratory",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 a sample-preparation procedure produces sections rather than results to aggregate (p.9)",
  "ada:combinedResults": "N \u2014 a sample-preparation procedure produces sections, not results to combine",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "N \u2014 a sample-preparation procedure produces sections, not results to combine",
  "ada:voxelSize": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Zega2025-6> a ada:SEMImage ;
    schema1:measurementTechnique <ex:semTAPP-Zega2025-6> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — a sample-preparation procedure produces sections rather than results to aggregate (p.9)" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "N — a sample-preparation procedure produces sections, not results to combine" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA PSEF 80NSSC23K0327; NASA Planetary Major Equipment NNX12AL47G; NSF MRI 0619599" ;
    ada:goodnessOfFitOrDispersionStatistic "N — a sample-preparation procedure produces sections, not results to combine" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "N — \"All sections were extracted from varied regions of matrix within the particles\" (p.9), none named; the paper labels FIB sections (e.g. OREX-803095-100, OREX-501005-100, OREX-803031-101; Figs 2–4) without attributing them to a laboratory" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "missing" .

<ex:semTAPP-Zega2025-6> schema1:identifier "missing" .


```


### detail example Zega2025-7
detail instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | TEM Sample Preparation (Helios G4 UX, UC Berkeley).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Zega2025-7",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Zega2025-7",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "US DOE contract DE-AC02-05CH11231 (Advanced Light Source / Molecular Foundry)",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "N — \"Bennu particles were placed on PELCO carbon conductive tabs\" (p.9), none named; the paper labels FIB sections (e.g. OREX-803095-100, OREX-501005-100, OREX-803031-101; Figs 2–4) without attributing them to a laboratory",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N — a sample-preparation procedure produces sections rather than results to aggregate (p.9)",
  "ada:combinedResults": "N — a sample-preparation procedure produces sections, not results to combine",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "N — a sample-preparation procedure produces sections, not results to combine",
  "ada:voxelSize": "missing"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Zega2025-7",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Zega2025-7",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "US DOE contract DE-AC02-05CH11231 (Advanced Light Source / Molecular Foundry)",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "N \u2014 \"Bennu particles were placed on PELCO carbon conductive tabs\" (p.9), none named; the paper labels FIB sections (e.g. OREX-803095-100, OREX-501005-100, OREX-803031-101; Figs 2\u20134) without attributing them to a laboratory",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 a sample-preparation procedure produces sections rather than results to aggregate (p.9)",
  "ada:combinedResults": "N \u2014 a sample-preparation procedure produces sections, not results to combine",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "N \u2014 a sample-preparation procedure produces sections, not results to combine",
  "ada:voxelSize": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Zega2025-7> a ada:SEMImage ;
    schema1:measurementTechnique <ex:semTAPP-Zega2025-7> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — a sample-preparation procedure produces sections rather than results to aggregate (p.9)" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "N — a sample-preparation procedure produces sections, not results to combine" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "US DOE contract DE-AC02-05CH11231 (Advanced Light Source / Molecular Foundry)" ;
    ada:goodnessOfFitOrDispersionStatistic "N — a sample-preparation procedure produces sections, not results to combine" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "N — \"Bennu particles were placed on PELCO carbon conductive tabs\" (p.9), none named; the paper labels FIB sections (e.g. OREX-803095-100, OREX-501005-100, OREX-803031-101; Figs 2–4) without attributing them to a laboratory" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "missing" .

<ex:semTAPP-Zega2025-7> schema1:identifier "missing" .


```


### detail example Zega2025-8
detail instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | TEM Sample Preparation (Quanta3D600, NASA JSC).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Zega2025-8",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Zega2025-8",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "N — \"FIB sections were prepared from particles dispersed on conductive carbon dots on Al SEM pin mounts\" (p.10), none named; the paper labels FIB sections (e.g. OREX-803095-100, OREX-501005-100, OREX-803031-101; Figs 2–4) without attributing them to a laboratory",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N — a sample-preparation procedure produces sections rather than results to aggregate (p.10)",
  "ada:combinedResults": "N — a sample-preparation procedure produces sections, not results to combine",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "N — a sample-preparation procedure produces sections, not results to combine",
  "ada:voxelSize": "missing"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Zega2025-8",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Zega2025-8",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "N \u2014 \"FIB sections were prepared from particles dispersed on conductive carbon dots on Al SEM pin mounts\" (p.10), none named; the paper labels FIB sections (e.g. OREX-803095-100, OREX-501005-100, OREX-803031-101; Figs 2\u20134) without attributing them to a laboratory",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 a sample-preparation procedure produces sections rather than results to aggregate (p.10)",
  "ada:combinedResults": "N \u2014 a sample-preparation procedure produces sections, not results to combine",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "N \u2014 a sample-preparation procedure produces sections, not results to combine",
  "ada:voxelSize": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Zega2025-8> a ada:SEMImage ;
    schema1:measurementTechnique <ex:semTAPP-Zega2025-8> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — a sample-preparation procedure produces sections rather than results to aggregate (p.10)" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "N — a sample-preparation procedure produces sections, not results to combine" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)" ;
    ada:goodnessOfFitOrDispersionStatistic "N — a sample-preparation procedure produces sections, not results to combine" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "N — \"FIB sections were prepared from particles dispersed on conductive carbon dots on Al SEM pin mounts\" (p.10), none named; the paper labels FIB sections (e.g. OREX-803095-100, OREX-501005-100, OREX-803031-101; Figs 2–4) without attributing them to a laboratory" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "missing" .

<ex:semTAPP-Zega2025-8> schema1:identifier "missing" .


```


### detail example Zega2025-9
detail instance derived from Zega et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | CL Mapping (JEOL JSM-7000F, Universite Cote d'Azur, 5 keV).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Zega2025-9",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Zega2025-9",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "N — the cathodoluminescence passage names no specimen (p.9)",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N — an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Zega2025-9",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Zega2025-9",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnitName": "N \u2014 the cathodoluminescence passage names no specimen (p.9)",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Zega2025-9> a ada:SEMImage ;
    schema1:measurementTechnique <ex:semTAPP-Zega2025-9> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — an imaging procedure reports no aggregate over individual results, and no acceptance or rejection rule is stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "missing" ;
    ada:samplingUnitName "N — the cathodoluminescence passage names no specimen (p.9)" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "missing" .

<ex:semTAPP-Zega2025-9> schema1:identifier "missing" .


```


### detail example Barnes2025
detail instance derived from Barnes et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | EDS Mapping (JEOL 7600F, NASA JSC, 15 kV).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Barnes2025",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Barnes2025",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "OREX-501018-100",
  "ada:samplingUnitName": "Labelled: \"Bennu sample OREX-501018-100\" (Extended Data Fig. 8 caption, p.27), \"aggregate QL material pressed onto a gold (Au) foil mount\" (p.10); the presolar-grain regions are not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N — this procedure analyses \"Two O-rich presolar grains\" individually to confirm their phase (p.11), with no aggregate over results. The >5σ anomaly criterion and the requirement that an anomaly persist \"in multiple consecutive frames\" (p.11) select grains from the NanoSIMS imaging, and belong to that procedure",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Barnes2025",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Barnes2025",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "OREX-501018-100",
  "ada:samplingUnitName": "Labelled: \"Bennu sample OREX-501018-100\" (Extended Data Fig. 8 caption, p.27), \"aggregate QL material pressed onto a gold (Au) foil mount\" (p.10); the presolar-grain regions are not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 this procedure analyses \"Two O-rich presolar grains\" individually to confirm their phase (p.11), with no aggregate over results. The >5\u03c3 anomaly criterion and the requirement that an anomaly persist \"in multiple consecutive frames\" (p.11) select grains from the NanoSIMS imaging, and belong to that procedure",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "ada:voxelSize": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Barnes2025> a ada:SEMImage ;
    schema1:measurementTechnique <ex:semTAPP-Barnes2025> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — this procedure analyses \"Two O-rich presolar grains\" individually to confirm their phase (p.11), with no aggregate over results. The >5σ anomaly criterion and the requirement that an anomaly persist \"in multiple consecutive frames\" (p.11) select grains from the NanoSIMS imaging, and belong to that procedure" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "OREX-501018-100" ;
    ada:samplingUnitName "Labelled: \"Bennu sample OREX-501018-100\" (Extended Data Fig. 8 caption, p.27), \"aggregate QL material pressed onto a gold (Au) foil mount\" (p.10); the presolar-grain regions are not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" ;
    ada:voxelSize "missing" .

<ex:semTAPP-Barnes2025> schema1:identifier "missing" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: SEM Analysis Detail
description: Dataset-level analysis-instance detail for SEM (superset), reusing CDIF/schema.org
  slots on the schema:Dataset root.
allOf:
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/AnalysisIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/calibrationFactor/schema.yaml#/$defs/AnalysisIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/aggregation/schema.yaml#/$defs/AnalysisIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/compositionQC/schema.yaml#/$defs/AnalysisIdentification
- type: object
  properties:
    prov:wasGeneratedBy:
      type: array
      items:
        type: object
        properties:
          schema:additionalProperty:
            type: array
            items:
              anyOf:
              - title: 3D Image Registration
                description: Method used to align consecutive SEM image slices in
                  the 3D stack to correct for drift, vibration, and curtaining artifacts.
                  Include software used.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/imageRegistration3D
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/imageRegistration3D
                  schema:name:
                    const: 3D Image Registration
                  schema:value:
                    type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - title: Segmentation Method
                description: Method and software used to separate distinct phases
                  or features in the reconstructed 3D volume, turning the grayscale
                  volume into labelled regions.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/segmentationMethod
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/segmentationMethod
                  schema:name:
                    const: Segmentation Method
                  schema:value:
                    type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - title: Beam Damage Minimization
                description: 'Describes any measures taken to reduce electron beam
                  damage to the sample during analysis. Examples: reduced accelerating
                  voltage, lowered beam current, defocused or rastered beam, cooled
                  stage, short acquisition sequences, or rotating between multiple
                  points.'
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/beamDamageMinimization
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/beamDamageMinimization
                  schema:name:
                    const: Beam Damage Minimization
                  schema:value:
                    type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - title: Beam Raster Dimensions
                description: "Dimensions of the small area over which the beam is
                  rastered at a single analysis point, reported as width \xD7 height
                  in \xB5m. Applicable when Beam Mode = Rastered; defines the effective
                  spatial footprint of the measurement. Not applicable when mapping."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/beamRasterDimensions
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/beamRasterDimensions
                  schema:name:
                    const: Beam Raster Dimensions
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
              - title: Chamber Pressure
                description: Chamber pressure and gas type during analysis. Required
                  for variable pressure (VP-SEM) and environmental SEM (ESEM) modes.
                  Report value and unit (Pa or Torr) and gas composition. Use 'None'
                  for standard high-vacuum operation.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/chamberPressure
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/chamberPressure
                  schema:name:
                    const: Chamber Pressure
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
              - title: CL Integration Time
                description: Acquisition time per pixel (hyperspectral map mode) or
                  per spectrum (spectral point mode), in ms or s.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/clIntegrationTime
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/clIntegrationTime
                  schema:name:
                    const: CL Integration Time
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
              - title: CL Wavelength Calibration Reference
                description: Reference light source or standard material used to calibrate
                  the wavelength axis of the CL spectrometer. Required for quantitative
                  spectral CL and hyperspectral mapping.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/clWavelengthCalibrationReference
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/clWavelengthCalibrationReference
                  schema:name:
                    const: CL Wavelength Calibration Reference
                  schema:value:
                    type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - title: Drift Correction
                description: 'Describes whether and how stage or beam drift was monitored
                  and corrected during the measurement session. Examples: periodic
                  stage realignment to a fiducial marker, automated beam drift correction
                  in acquisition software, or reanalysis of a reference point at regular
                  intervals.'
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/driftCorrection
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/driftCorrection
                  schema:name:
                    const: Drift Correction
                  schema:value:
                    type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - title: EBSD Frame Time
                description: Acquisition time per EBSD diffraction pattern frame in
                  milliseconds.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/ebsdFrameTime
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/ebsdFrameTime
                  schema:name:
                    const: EBSD Frame Time
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
              - title: EBSD Phase List
                description: Mineral phases included in the EBSD reference pattern
                  library for this procedure. Phases may be added for specific sample
                  compositions beyond the expected suite for the target material.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/ebsdPhaseList
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/ebsdPhaseList
                  schema:name:
                    const: EBSD Phase List
                  schema:value:
                    type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - title: EBSD Step Size
                description: "Distance between adjacent EBSD measurement points in
                  the map in nm or \xB5m. Must be smaller than the smallest grain
                  of interest."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/ebsdStepSize
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/ebsdStepSize
                  schema:name:
                    const: EBSD Step Size
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
              - title: EDS Live Time per Point or Pixel
                description: EDS spectral acquisition live time per analysis point
                  or per pixel in seconds.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/edsLiveTimePerPointOrPixel
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/edsLiveTimePerPointOrPixel
                  schema:name:
                    const: EDS Live Time per Point or Pixel
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
              - title: Halogen Correction on Oxygen
                description: Whether oxygen content was adjusted to account for halogen
                  substitution (F and/or Cl replacing OH) in halogen-bearing phases
                  such as apatite, amphibole, and mica, where oxygen is calculated
                  by stoichiometry.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/halogenCorrectionOnOxygen
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/halogenCorrectionOnOxygen
                  schema:name:
                    const: Halogen Correction on Oxygen
                  schema:value:
                    type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - title: Image Pixel Size
                description: "Physical size of each image pixel at the sample surface,
                  in nm or \xB5m. For large-area mosaic imaging, report the pixel
                  size of individual tiles and the number and arrangement of tiles."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/imagePixelSize
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/imagePixelSize
                  schema:name:
                    const: Image Pixel Size
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
              - title: Step Size / Pixel Size
                description: "Centre-to-centre distance between adjacent measurement
                  points (WDS mapping) or pixels (EDS mapping) in \xB5m."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/stepSizePixelSize
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/stepSizePixelSize
                  schema:name:
                    const: Step Size / Pixel Size
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
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_samplingUnitSelectionCriteria
              - title: Working Distance
                description: Distance between the objective lens pole piece and the
                  specimen surface in millimetres.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/workingDistance
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/workingDistance
                  schema:name:
                    const: Working Distance
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
                title: 3D Image Registration
                description: Method used to align consecutive SEM image slices in
                  the 3D stack to correct for drift, vibration, and curtaining artifacts.
                  Include software used.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/imageRegistration3D
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/imageRegistration3D
                  schema:name:
                    const: 3D Image Registration
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
                title: Segmentation Method
                description: Method and software used to separate distinct phases
                  or features in the reconstructed 3D volume, turning the grayscale
                  volume into labelled regions.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/segmentationMethod
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/segmentationMethod
                  schema:name:
                    const: Segmentation Method
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
                title: Beam Damage Minimization
                description: 'Describes any measures taken to reduce electron beam
                  damage to the sample during analysis. Examples: reduced accelerating
                  voltage, lowered beam current, defocused or rastered beam, cooled
                  stage, short acquisition sequences, or rotating between multiple
                  points.'
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/beamDamageMinimization
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/beamDamageMinimization
                  schema:name:
                    const: Beam Damage Minimization
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
                title: Beam Raster Dimensions
                description: "Dimensions of the small area over which the beam is
                  rastered at a single analysis point, reported as width \xD7 height
                  in \xB5m. Applicable when Beam Mode = Rastered; defines the effective
                  spatial footprint of the measurement. Not applicable when mapping."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/beamRasterDimensions
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/beamRasterDimensions
                  schema:name:
                    const: Beam Raster Dimensions
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
                title: Chamber Pressure
                description: Chamber pressure and gas type during analysis. Required
                  for variable pressure (VP-SEM) and environmental SEM (ESEM) modes.
                  Report value and unit (Pa or Torr) and gas composition. Use 'None'
                  for standard high-vacuum operation.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/chamberPressure
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/chamberPressure
                  schema:name:
                    const: Chamber Pressure
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
                title: CL Integration Time
                description: Acquisition time per pixel (hyperspectral map mode) or
                  per spectrum (spectral point mode), in ms or s.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/clIntegrationTime
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/clIntegrationTime
                  schema:name:
                    const: CL Integration Time
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
                title: CL Wavelength Calibration Reference
                description: Reference light source or standard material used to calibrate
                  the wavelength axis of the CL spectrometer. Required for quantitative
                  spectral CL and hyperspectral mapping.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/clWavelengthCalibrationReference
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/clWavelengthCalibrationReference
                  schema:name:
                    const: CL Wavelength Calibration Reference
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
                title: Drift Correction
                description: 'Describes whether and how stage or beam drift was monitored
                  and corrected during the measurement session. Examples: periodic
                  stage realignment to a fiducial marker, automated beam drift correction
                  in acquisition software, or reanalysis of a reference point at regular
                  intervals.'
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/driftCorrection
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/driftCorrection
                  schema:name:
                    const: Drift Correction
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
                title: EBSD Frame Time
                description: Acquisition time per EBSD diffraction pattern frame in
                  milliseconds.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/ebsdFrameTime
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/ebsdFrameTime
                  schema:name:
                    const: EBSD Frame Time
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
                title: EBSD Phase List
                description: Mineral phases included in the EBSD reference pattern
                  library for this procedure. Phases may be added for specific sample
                  compositions beyond the expected suite for the target material.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/ebsdPhaseList
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/ebsdPhaseList
                  schema:name:
                    const: EBSD Phase List
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
                title: EBSD Step Size
                description: "Distance between adjacent EBSD measurement points in
                  the map in nm or \xB5m. Must be smaller than the smallest grain
                  of interest."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/ebsdStepSize
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/ebsdStepSize
                  schema:name:
                    const: EBSD Step Size
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
                title: EDS Live Time per Point or Pixel
                description: EDS spectral acquisition live time per analysis point
                  or per pixel in seconds.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/edsLiveTimePerPointOrPixel
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/edsLiveTimePerPointOrPixel
                  schema:name:
                    const: EDS Live Time per Point or Pixel
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
                title: Halogen Correction on Oxygen
                description: Whether oxygen content was adjusted to account for halogen
                  substitution (F and/or Cl replacing OH) in halogen-bearing phases
                  such as apatite, amphibole, and mica, where oxygen is calculated
                  by stoichiometry.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/halogenCorrectionOnOxygen
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/halogenCorrectionOnOxygen
                  schema:name:
                    const: Halogen Correction on Oxygen
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
                title: Image Pixel Size
                description: "Physical size of each image pixel at the sample surface,
                  in nm or \xB5m. For large-area mosaic imaging, report the pixel
                  size of individual tiles and the number and arrangement of tiles."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/imagePixelSize
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/imagePixelSize
                  schema:name:
                    const: Image Pixel Size
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
                title: Step Size / Pixel Size
                description: "Centre-to-centre distance between adjacent measurement
                  points (WDS mapping) or pixels (EDS mapping) in \xB5m."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/stepSizePixelSize
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/stepSizePixelSize
                  schema:name:
                    const: Step Size / Pixel Size
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
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_samplingUnitSelectionCriteria
              minContains: 0
              maxContains: 1
            - contains:
                title: Working Distance
                description: Distance between the objective lens pole piece and the
                  specimen surface in millimetres.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/workingDistance
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/workingDistance
                  schema:name:
                    const: Working Distance
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
                                    const: SEM
                                  schema:inDefinedTermSet: ada:vocab/instrumentType
                              required:
                              - schema:additionalType
                            then:
                              properties:
                                schema:additionalProperty:
                                  type: array
                                  items:
                                    anyOf:
                                    - title: Accelerating Voltage
                                      description: Electron beam accelerating voltage
                                        in kilovolts.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/semTAPP/acceleratingVoltage
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/semTAPP/acceleratingVoltage
                                        schema:name:
                                          const: Accelerating Voltage
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
                                    - title: Beam Diameter
                                      description: Nominal electron beam diameter
                                        (spot size) at the sample surface for point
                                        analysis, in nanometres or micrometres, as
                                        set by the condenser aperture and working
                                        distance. The beam used for mapping is recorded
                                        under Mapping Beam Diameter.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/semTAPP/beamDiameter
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/semTAPP/beamDiameter
                                        schema:name:
                                          const: Beam Diameter
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
                                    - title: Mapping Beam Current
                                      description: 'Electron beam probe current used
                                        while the beam scans an area: an X-ray or
                                        CL map, an EBSD map, or an SE or BSE image,
                                        including images taken during FIB-SEM work.
                                        For sub-nA values use decimal notation (e.g.,
                                        0.4 nA). Ion-beam currents used for milling
                                        belong in the milling condition fields.'
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/semTAPP/mappingBeamCurrent
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/semTAPP/mappingBeamCurrent
                                        schema:name:
                                          const: Mapping Beam Current
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
                                    - title: Mapping Beam Diameter
                                      description: Diameter of the electron beam in
                                        micrometres during X-ray mapping. 0 indicates
                                        a fully focused beam.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/semTAPP/mappingBeamDiameter
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/semTAPP/mappingBeamDiameter
                                        schema:name:
                                          const: Mapping Beam Diameter
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
                                      title: Accelerating Voltage
                                      description: Electron beam accelerating voltage
                                        in kilovolts.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/semTAPP/acceleratingVoltage
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/semTAPP/acceleratingVoltage
                                        schema:name:
                                          const: Accelerating Voltage
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
                                      title: Beam Diameter
                                      description: Nominal electron beam diameter
                                        (spot size) at the sample surface for point
                                        analysis, in nanometres or micrometres, as
                                        set by the condenser aperture and working
                                        distance. The beam used for mapping is recorded
                                        under Mapping Beam Diameter.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/semTAPP/beamDiameter
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/semTAPP/beamDiameter
                                        schema:name:
                                          const: Beam Diameter
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
                                      title: Mapping Beam Current
                                      description: 'Electron beam probe current used
                                        while the beam scans an area: an X-ray or
                                        CL map, an EBSD map, or an SE or BSE image,
                                        including images taken during FIB-SEM work.
                                        For sub-nA values use decimal notation (e.g.,
                                        0.4 nA). Ion-beam currents used for milling
                                        belong in the milling condition fields.'
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/semTAPP/mappingBeamCurrent
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/semTAPP/mappingBeamCurrent
                                        schema:name:
                                          const: Mapping Beam Current
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
                                      title: Mapping Beam Diameter
                                      description: Diameter of the electron beam in
                                        micrometres during X-ray mapping. 0 indicates
                                        a fully focused beam.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/semTAPP/mappingBeamDiameter
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/semTAPP/mappingBeamDiameter
                                        schema:name:
                                          const: Mapping Beam Diameter
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
                                const: SEM
                              schema:inDefinedTermSet: ada:vocab/instrumentType
                          required:
                          - schema:additionalType
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
                            - title: Coarse Milling Conditions
                              description: 'Ion beam voltage and current used for
                                bulk material removal during FIB milling. For TEM
                                specimen preparation: bulk trenching to isolate the
                                lamella and intermediate thinning. For 3D tomography:
                                face preparation and initial slice removal.'
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/semTAPP/coarseMillingConditions
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/semTAPP/coarseMillingConditions
                                schema:name:
                                  const: Coarse Milling Conditions
                                schema:value:
                                  type: string
                              required:
                              - '@id'
                              - '@type'
                              - schema:propertyID
                              - schema:name
                              - schema:value
                            - title: Fine Polishing Conditions
                              description: Ion beam voltage and current for final
                                thinning and surface polishing of the TEM lamella.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/semTAPP/finePolishingConditions
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/semTAPP/finePolishingConditions
                                schema:name:
                                  const: Fine Polishing Conditions
                                schema:value:
                                  type: string
                              required:
                              - '@id'
                              - '@type'
                              - schema:propertyID
                              - schema:name
                              - schema:value
                            - title: Protective Coating Deposition
                              description: 'Type and deposition conditions of the
                                protective coating applied to the sample surface before
                                FIB milling. E-beam deposition should be applied as
                                the initial layer. Typical coatings: platinum (Pt)
                                or carbon (C). State material, deposition method,
                                beam conditions, and approximate thickness.'
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/semTAPP/protectiveCoatingDeposition
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/semTAPP/protectiveCoatingDeposition
                                schema:name:
                                  const: Protective Coating Deposition
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
                              title: Coarse Milling Conditions
                              description: 'Ion beam voltage and current used for
                                bulk material removal during FIB milling. For TEM
                                specimen preparation: bulk trenching to isolate the
                                lamella and intermediate thinning. For 3D tomography:
                                face preparation and initial slice removal.'
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/semTAPP/coarseMillingConditions
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/semTAPP/coarseMillingConditions
                                schema:name:
                                  const: Coarse Milling Conditions
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
                              title: Fine Polishing Conditions
                              description: Ion beam voltage and current for final
                                thinning and surface polishing of the TEM lamella.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/semTAPP/finePolishingConditions
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/semTAPP/finePolishingConditions
                                schema:name:
                                  const: Fine Polishing Conditions
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
                              title: Protective Coating Deposition
                              description: 'Type and deposition conditions of the
                                protective coating applied to the sample surface before
                                FIB milling. E-beam deposition should be applied as
                                the initial layer. Typical coatings: platinum (Pt)
                                or carbon (C). State material, deposition method,
                                beam conditions, and approximate thickness.'
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/semTAPP/protectiveCoatingDeposition
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/semTAPP/protectiveCoatingDeposition
                                schema:name:
                                  const: Protective Coating Deposition
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
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Analysis_constantsReferenceValues
                            - title: Crystal Structure Database
                              description: Crystal structure database used for EBSD
                                phase identification and Kikuchi pattern simulation.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/semTAPP/crystalStructureDatabase
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/semTAPP/crystalStructureDatabase
                                schema:name:
                                  const: Crystal Structure Database
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
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Analysis_constantsReferenceValues
                            minContains: 0
                            maxContains: 1
                          - contains:
                              title: Crystal Structure Database
                              description: Crystal structure database used for EBSD
                                phase identification and Kikuchi pattern simulation.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/semTAPP/crystalStructureDatabase
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/semTAPP/crystalStructureDatabase
                                schema:name:
                                  const: Crystal Structure Database
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
                        schema:name:
                          const: Ion milling
                      required:
                      - schema:name
                    then:
                      properties:
                        schema:description:
                          description: Ion beam voltage and current used to mill each
                            slice during FIB-SEM serial sectioning.
                          anyOf:
                          - type: string
                          - type: array
                            items:
                              type: string
                      required:
                      - schema:description
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
                - contains:
                    properties:
                      schema:name:
                        const: Ion milling
                    required:
                    - schema:name
          ada:edsDeadTime:
            description: "Percent dead time reported by the EDS detector during the
              session \u2014 the fraction of total acquisition time the detector spent
              processing rather than counting. This field documents the resulting
              percentage as a session QC metric. Unlike WDS dead time (see WDS Dead
              Time Correction), no user-selectable correction algorithm is required."
            anyOf:
            - type: number
            - type: string
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
                        - title: Foil Thickness
                          description: Target thickness of the electron-transparent
                            TEM lamella after final FIB polishing, in nanometres.
                            Actual thickness may differ from target.
                          type: object
                          properties:
                            '@id':
                              const: ada:parameter/semTAPP/foilThickness
                            '@type':
                              const:
                              - schema:PropertyValue
                            schema:propertyID:
                              const:
                              - '@id': ada:parameter/semTAPP/foilThickness
                            schema:name:
                              const: Foil Thickness
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
                        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_preAnalysisImagingAndScreening
                        - title: Slice Thickness
                          description: Thickness of each FIB-milled slice during serial
                            sectioning in nanometres.
                          type: object
                          properties:
                            '@id':
                              const: ada:parameter/semTAPP/sliceThickness
                            '@type':
                              const:
                              - schema:PropertyValue
                            schema:propertyID:
                              const:
                              - '@id': ada:parameter/semTAPP/sliceThickness
                            schema:name:
                              const: Slice Thickness
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
                          title: Foil Thickness
                          description: Target thickness of the electron-transparent
                            TEM lamella after final FIB polishing, in nanometres.
                            Actual thickness may differ from target.
                          type: object
                          properties:
                            '@id':
                              const: ada:parameter/semTAPP/foilThickness
                            '@type':
                              const:
                              - schema:PropertyValue
                            schema:propertyID:
                              const:
                              - '@id': ada:parameter/semTAPP/foilThickness
                            schema:name:
                              const: Foil Thickness
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
                          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_preAnalysisImagingAndScreening
                        minContains: 0
                        maxContains: 1
                      - contains:
                          title: Slice Thickness
                          description: Thickness of each FIB-milled slice during serial
                            sectioning in nanometres.
                          type: object
                          properties:
                            '@id':
                              const: ada:parameter/semTAPP/sliceThickness
                            '@type':
                              const:
                              - schema:PropertyValue
                            schema:propertyID:
                              const:
                              - '@id': ada:parameter/semTAPP/sliceThickness
                            schema:name:
                              const: Slice Thickness
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
        - ada:edsDeadTime
        - ada:proceduralBlankLevel
        - schema:actionProcess
    dqv:hasQualityMeasurement:
      type: array
      items:
        type: object
        allOf:
        - if:
            properties:
              dqv:isMeasurementOf:
                const: EBSD Indexing Rate
            required:
            - dqv:isMeasurementOf
          then:
            properties:
              dqv:value:
                description: Fraction of EBSD map points successfully indexed, expressed
                  as a percentage of total map points.
                anyOf:
                - type: number
                - type: string
            required:
            - dqv:value
        - if:
            properties:
              dqv:isMeasurementOf:
                const: EBSD Mean Angular Deviation
            required:
            - dqv:isMeasurementOf
          then:
            properties:
              dqv:value:
                description: Mean angular deviation (MAD) of the EBSD pattern indexing
                  solution in degrees. MAD quantifies the misfit between experimental
                  Kikuchi band positions and the best-fit crystal orientation.
                anyOf:
                - type: number
                - type: string
            required:
            - dqv:value
        - if:
            properties:
              dqv:isMeasurementOf:
                const: EBSD Pattern Quality Threshold
            required:
            - dqv:isMeasurementOf
          then:
            properties:
              dqv:value:
                description: Minimum pattern quality or confidence index threshold
                  applied during EBSD data processing to exclude unreliably indexed
                  points from orientation maps. Include metric name and threshold
                  value.
                anyOf:
                - type: string
                - type: array
                  items:
                    type: string
      allOf:
      - contains:
          properties:
            dqv:isMeasurementOf:
              const: EBSD Indexing Rate
          required:
          - dqv:isMeasurementOf
      - contains:
          properties:
            dqv:isMeasurementOf:
              const: EBSD Mean Angular Deviation
          required:
          - dqv:isMeasurementOf
    ada:mapDimensions:
      description: Number of pixels in the EDS map in the X and Y directions. Based
        on the area of interest and selected pixel size.
      anyOf:
      - type: number
      - type: string
    schema:additionalProperty:
      type: array
      items:
        title: Map Area
        description: "Physical extent of the mapped region, given either as width
          \xD7 height in \xB5m or as a total area in \xB5m\xB2 or mm\xB2, and equal
          to (map width in pixels \xD7 step size) \xD7 (map height in pixels \xD7
          step size). Complements the map's pixel-grid dimensions by recording the
          physical scale of the mapped region."
        type: object
        properties:
          '@id':
            const: ada:parameter/semTAPP/mapArea
          '@type':
            const:
            - schema:PropertyValue
          schema:propertyID:
            const:
            - '@id': ada:parameter/semTAPP/mapArea
          schema:name:
            const: Map Area
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
          title: Map Area
          description: "Physical extent of the mapped region, given either as width
            \xD7 height in \xB5m or as a total area in \xB5m\xB2 or mm\xB2, and equal
            to (map width in pixels \xD7 step size) \xD7 (map height in pixels \xD7
            step size). Complements the map's pixel-grid dimensions by recording the
            physical scale of the mapped region."
          type: object
          properties:
            '@id':
              const: ada:parameter/semTAPP/mapArea
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/semTAPP/mapArea
            schema:name:
              const: Map Area
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
    ada:voxelSize:
      description: X, Y, Z dimensions of the reconstructed 3D voxel in nanometres
        (X-Y pixel size from SEM image calibration; Z from slice thickness), and the
        total number of slices in the stack.
      type: string
    ada:imageStackDimenstions:
      description: X, Y, Z dimensions of the reconstructed 3D voxel in nanometres
        (X-Y pixel size from SEM image calibration; Z from slice thickness), and the
        total number of slices in the stack.
      type: string
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
        - title: Target Material of Sampling Unit
          description: The entry in Target Material that the sampling unit belongs
            to, which links the unit to the point-analysis conditions registered for
            that material.
          type: object
          properties:
            '@id':
              const: ada:parameter/semTAPP/targetMaterialOfSamplingUnit
            '@type':
              const:
              - schema:PropertyValue
              - cdi:InstanceVariable
            schema:propertyID:
              const:
              - '@id': ada:parameter/semTAPP/targetMaterialOfSamplingUnit
            schema:name:
              const: Target Material of Sampling Unit
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
          title: Target Material of Sampling Unit
          description: The entry in Target Material that the sampling unit belongs
            to, which links the unit to the point-analysis conditions registered for
            that material.
          type: object
          properties:
            '@id':
              const: ada:parameter/semTAPP/targetMaterialOfSamplingUnit
            '@type':
              const:
              - schema:PropertyValue
              - cdi:InstanceVariable
            schema:propertyID:
              const:
              - '@id': ada:parameter/semTAPP/targetMaterialOfSamplingUnit
            schema:name:
              const: Target Material of Sampling Unit
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
  required:
  - ada:mapDimensions
  - ada:voxelSize
  - ada:imageStackDimenstions

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld)

## Sources

* [SEM_TAPP_v4.xlsx (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/SEM/detail`

