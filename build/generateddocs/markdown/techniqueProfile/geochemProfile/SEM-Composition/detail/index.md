
# SEM Composition Analysis Detail (Schema)

`ogch.techniqueProfile.geochemProfile.SEM-Composition.detail` *v0.1*

Dataset-level analysis-instance detail for SEM composition (EDS/WDS), reusing CDIF/schema.org slots on the schema:Dataset root.

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
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Garvie2008"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA NNG06GE37G (LAJG); NASA NNG06GF08G (PRB)",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Garvie2008",
  "@type": [
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Garvie2008"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA NNG06GE37G (LAJG); NASA NNG06GF08G (PRB)",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Garvie2008 a ada:SEMEDSSpectrum ;
    schema1:measurementTechnique ex:semCompositionTAPP-Garvie2008 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMEDSSpectrum" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA NNG06GE37G (LAJG); NASA NNG06GF08G (PRB)" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


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
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Garvie2008-2"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA NNG06GE37G (LAJG); NASA NNG06GF08G (PRB)",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Garvie2008-2",
  "@type": [
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Garvie2008-2"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA NNG06GE37G (LAJG); NASA NNG06GF08G (PRB)",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Garvie2008-2 a ada:SEMEDSSpectrum ;
    schema1:measurementTechnique ex:semCompositionTAPP-Garvie2008-2 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMEDSSpectrum" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA NNG06GE37G (LAJG); NASA NNG06GF08G (PRB)" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


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
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Genge2025"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Genge2025",
  "@type": [
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Genge2025"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Genge2025 a ada:SEMEDSSpectrum ;
    schema1:measurementTechnique ex:semCompositionTAPP-Genge2025 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMEDSSpectrum" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


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
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Genge2025-2"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Genge2025-2",
  "@type": [
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Genge2025-2"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Genge2025-2 a ada:SEMEDSSpectrum ;
    schema1:measurementTechnique ex:semCompositionTAPP-Genge2025-2 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMEDSSpectrum" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


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
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Genge2025-3"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Genge2025-3",
  "@type": [
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Genge2025-3"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Genge2025-3 a ada:SEMEDSSpectrum ;
    schema1:measurementTechnique ex:semCompositionTAPP-Genge2025-3 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMEDSSpectrum" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


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
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Gucsik2013"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Gucsik2013",
  "@type": [
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Gucsik2013"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Gucsik2013 a ada:SEMEDSSpectrum ;
    schema1:measurementTechnique ex:semCompositionTAPP-Gucsik2013 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMEDSSpectrum" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


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
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Gucsik2013-2"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Gucsik2013-2",
  "@type": [
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Gucsik2013-2"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Gucsik2013-2 a ada:SEMEDSSpectrum ;
    schema1:measurementTechnique ex:semCompositionTAPP-Gucsik2013-2 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMEDSSpectrum" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


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
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Izawa2010"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Izawa2010",
  "@type": [
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Izawa2010"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Izawa2010 a ada:SEMEDSSpectrum ;
    schema1:measurementTechnique ex:semCompositionTAPP-Izawa2010 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMEDSSpectrum" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


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
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Izawa2010-2"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Izawa2010-2",
  "@type": [
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Izawa2010-2"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Izawa2010-2 a ada:SEMEDSSpectrum ;
    schema1:measurementTechnique ex:semCompositionTAPP-Izawa2010-2 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMEDSSpectrum" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


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
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Izawa2010-3"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "~0.5 wt% for most elements",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Izawa2010-3",
  "@type": [
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Izawa2010-3"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "~0.5 wt% for most elements",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Izawa2010-3 a ada:SEMEDSSpectrum ;
    schema1:measurementTechnique ex:semCompositionTAPP-Izawa2010-3 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMEDSSpectrum" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "~0.5 wt% for most elements" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


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
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Izawa2010-4"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Izawa2010-4",
  "@type": [
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Izawa2010-4"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Izawa2010-4 a ada:SEMEDSSpectrum ;
    schema1:measurementTechnique ex:semCompositionTAPP-Izawa2010-4 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMEDSSpectrum" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


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
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Izawa2010-5"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Izawa2010-5",
  "@type": [
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Izawa2010-5"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Izawa2010-5 a ada:SEMEDSSpectrum ;
    schema1:measurementTechnique ex:semCompositionTAPP-Izawa2010-5 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMEDSSpectrum" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


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
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Liu2017"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Liu2017",
  "@type": [
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Liu2017"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Liu2017 a ada:SEMEDSSpectrum ;
    schema1:measurementTechnique ex:semCompositionTAPP-Liu2017 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMEDSSpectrum" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


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
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Liu2017-2"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Liu2017-2",
  "@type": [
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Liu2017-2"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Liu2017-2 a ada:SEMEDSSpectrum ;
    schema1:measurementTechnique ex:semCompositionTAPP-Liu2017-2 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMEDSSpectrum" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


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
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Liu2017-3"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Liu2017-3",
  "@type": [
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Liu2017-3"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Liu2017-3 a ada:SEMEDSSpectrum ;
    schema1:measurementTechnique ex:semCompositionTAPP-Liu2017-3 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMEDSSpectrum" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


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
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Ma2017"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NSF EAR-0318518; NSF DMR-0080065 (supporting Caltech GPS Analytical Facility)",
  "ada:sampleName": "Section 126A (USNM 7908)",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Ma2017",
  "@type": [
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Ma2017"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NSF EAR-0318518; NSF DMR-0080065 (supporting Caltech GPS Analytical Facility)",
  "ada:sampleName": "Section 126A (USNM 7908)",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Ma2017 a ada:SEMEDSSpectrum ;
    schema1:measurementTechnique ex:semCompositionTAPP-Ma2017 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMEDSSpectrum" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NSF EAR-0318518; NSF DMR-0080065 (supporting Caltech GPS Analytical Facility)" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "Section 126A (USNM 7908)" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


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
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Ma2017-2"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NSF EAR-0318518; NSF DMR-0080065 (supporting Caltech GPS Analytical Facility)",
  "ada:sampleName": "Section 126A (USNM 7908)",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Ma2017-2",
  "@type": [
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Ma2017-2"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NSF EAR-0318518; NSF DMR-0080065 (supporting Caltech GPS Analytical Facility)",
  "ada:sampleName": "Section 126A (USNM 7908)",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Ma2017-2 a ada:SEMEDSSpectrum ;
    schema1:measurementTechnique ex:semCompositionTAPP-Ma2017-2 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMEDSSpectrum" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NSF EAR-0318518; NSF DMR-0080065 (supporting Caltech GPS Analytical Facility)" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "Section 126A (USNM 7908)" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


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
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Pascucci2026"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "NWA 7317",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Pascucci2026",
  "@type": [
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Pascucci2026"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "NWA 7317",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Pascucci2026 a ada:SEMEDSSpectrum ;
    schema1:measurementTechnique ex:semCompositionTAPP-Pascucci2026 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMEDSSpectrum" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "NWA 7317" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


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
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Pascucci2026-2"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "NWA 7317",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Pascucci2026-2",
  "@type": [
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Pascucci2026-2"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "NWA 7317",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Pascucci2026-2 a ada:SEMEDSSpectrum ;
    schema1:measurementTechnique ex:semCompositionTAPP-Pascucci2026-2 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMEDSSpectrum" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "NWA 7317" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


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
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Pascucci2026-3"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "NWA 7317",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": 1024,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Pascucci2026-3",
  "@type": [
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Pascucci2026-3"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "NWA 7317",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": 1024,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Pascucci2026-3 a ada:SEMEDSSpectrum ;
    schema1:measurementTechnique ex:semCompositionTAPP-Pascucci2026-3 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMEDSSpectrum" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions 1024 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "NWA 7317" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


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
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Pascucci2026-4"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "NWA 7317",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Pascucci2026-4",
  "@type": [
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Pascucci2026-4"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "NWA 7317",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Pascucci2026-4 a ada:SEMEDSSpectrum ;
    schema1:measurementTechnique ex:semCompositionTAPP-Pascucci2026-4 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMEDSSpectrum" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "NWA 7317" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


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
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Zhou2017"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "SC; HBC",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Zhou2017",
  "@type": [
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Zhou2017"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "SC; HBC",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Zhou2017 a ada:SEMEDSSpectrum ;
    schema1:measurementTechnique ex:semCompositionTAPP-Zhou2017 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMEDSSpectrum" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "SC; HBC" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


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
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Zega2025"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Zega2025",
  "@type": [
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Zega2025"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Zega2025 a ada:SEMEDSSpectrum ;
    schema1:measurementTechnique ex:semCompositionTAPP-Zega2025 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMEDSSpectrum" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


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
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Zega2025-2"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Zega2025-2",
  "@type": [
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Zega2025-2"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Zega2025-2 a ada:SEMEDSSpectrum ;
    schema1:measurementTechnique ex:semCompositionTAPP-Zega2025-2 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMEDSSpectrum" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


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
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Zega2025-3"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Zega2025-3",
  "@type": [
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Zega2025-3"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Zega2025-3 a ada:SEMEDSSpectrum ;
    schema1:measurementTechnique ex:semCompositionTAPP-Zega2025-3 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMEDSSpectrum" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


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
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Zega2025-4"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Zega2025-4",
  "@type": [
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Zega2025-4"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Zega2025-4 a ada:SEMEDSSpectrum ;
    schema1:measurementTechnique ex:semCompositionTAPP-Zega2025-4 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMEDSSpectrum" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


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
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Zega2025-5"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Zega2025-5",
  "@type": [
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Zega2025-5"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Zega2025-5 a ada:SEMEDSSpectrum ;
    schema1:measurementTechnique ex:semCompositionTAPP-Zega2025-5 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMEDSSpectrum" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


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
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Zega2025-6"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA PSEF 80NSSC23K0327; NASA Planetary Major Equipment NNX12AL47G; NSF MRI 0619599",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Zega2025-6",
  "@type": [
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Zega2025-6"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA PSEF 80NSSC23K0327; NASA Planetary Major Equipment NNX12AL47G; NSF MRI 0619599",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Zega2025-6 a ada:SEMEDSSpectrum ;
    schema1:measurementTechnique ex:semCompositionTAPP-Zega2025-6 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMEDSSpectrum" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA PSEF 80NSSC23K0327; NASA Planetary Major Equipment NNX12AL47G; NSF MRI 0619599" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


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
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Zega2025-7"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "US DOE contract DE-AC02-05CH11231 (Advanced Light Source / Molecular Foundry)",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Zega2025-7",
  "@type": [
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Zega2025-7"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "US DOE contract DE-AC02-05CH11231 (Advanced Light Source / Molecular Foundry)",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Zega2025-7 a ada:SEMEDSSpectrum ;
    schema1:measurementTechnique ex:semCompositionTAPP-Zega2025-7 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMEDSSpectrum" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "US DOE contract DE-AC02-05CH11231 (Advanced Light Source / Molecular Foundry)" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


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
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Zega2025-8"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Zega2025-8",
  "@type": [
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Zega2025-8"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Zega2025-8 a ada:SEMEDSSpectrum ;
    schema1:measurementTechnique ex:semCompositionTAPP-Zega2025-8 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMEDSSpectrum" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


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
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Zega2025-9"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Zega2025-9",
  "@type": [
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Zega2025-9"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Zega2025-9 a ada:SEMEDSSpectrum ;
    schema1:measurementTechnique ex:semCompositionTAPP-Zega2025-9 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMEDSSpectrum" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


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
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Barnes2025"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "OREX-501018-100",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Barnes2025",
  "@type": [
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Barnes2025"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "OREX-501018-100",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Barnes2025 a ada:SEMEDSSpectrum ;
    schema1:measurementTechnique ex:semCompositionTAPP-Barnes2025 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMEDSSpectrum" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "OREX-501018-100" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


```


### detail example Barnes2025-2
detail instance derived from Barnes et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | BSE Imaging (FEI Quanta 3D DualBeam + Helios DualBeam, NASA JSC).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Barnes2025-2",
  "@type": [
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Barnes2025-2"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Barnes2025-2",
  "@type": [
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Barnes2025-2"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Barnes2025-2 a ada:SEMEDSSpectrum ;
    schema1:measurementTechnique ex:semCompositionTAPP-Barnes2025-2 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMEDSSpectrum" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


```


### detail example Barnes2025-3
detail instance derived from Barnes et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | TEM Sample Preparation (FEI Helios G4 DualBeam, NASA JSC).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Barnes2025-3",
  "@type": [
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Barnes2025-3"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Barnes2025-3",
  "@type": [
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Barnes2025-3"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Barnes2025-3 a ada:SEMEDSSpectrum ;
    schema1:measurementTechnique ex:semCompositionTAPP-Barnes2025-3 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMEDSSpectrum" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


```


### detail example Barnes2025-4
detail instance derived from Barnes et al. 2025 | Bennu asteroid particles (OSIRIS-REx) | TEM Sample Preparation (FEI Helios 660 G3, NASA JSC).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Barnes2025-4",
  "@type": [
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Barnes2025-4"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Barnes2025-4",
  "@type": [
    "ada:SEMEDSSpectrum"
  ],
  "ada:componentType": "ada:SEMEDSSpectrum",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semCompositionTAPP-Barnes2025-4"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Barnes2025-4 a ada:SEMEDSSpectrum ;
    schema1:measurementTechnique ex:semCompositionTAPP-Barnes2025-4 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMEDSSpectrum" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: SEM Composition Analysis Detail
description: Dataset-level analysis-instance detail for SEM composition (EDS/WDS),
  reusing CDIF/schema.org slots on the schema:Dataset root.
allOf:
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/AnalysisIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/calibrationFactor/schema.yaml#/$defs/AnalysisIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/aggregation/schema.yaml#/$defs/AnalysisIdentification
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
                  - if:
                      properties:
                        schema:name:
                          const: Sample preparation
                      required:
                      - schema:name
                    then:
                      properties:
                        schema:description:
                          description: Method by which samples were prepared for SEM
                            analysis prior to loading in the instrument. Includes
                            mounting medium (epoxy, carbon tape, stub), polishing
                            steps (alumina, colloidal silica, argon ion mill), and
                            conductive coating type and thickness. For VP-SEM/ESEM
                            analyses, note whether an uncoated sample was used and
                            the gas type used. FIB-specific in-session operations
                            (protective coating deposition, milling conditions, lamella
                            preparation) are documented separately in Group 4.
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
                            - title: Normalization / Standards-Based Correction
                              description: Post-acquisition normalization applied
                                using secondary reference materials to correct for
                                session-to-session calibration drift.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/semCompositionTAPP/normalizationStandardsBasedCorrection
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/semCompositionTAPP/normalizationStandardsBasedCorrection
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
                              title: Normalization / Standards-Based Correction
                              description: Post-acquisition normalization applied
                                using secondary reference materials to correct for
                                session-to-session calibration drift.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/semCompositionTAPP/normalizationStandardsBasedCorrection
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/semCompositionTAPP/normalizationStandardsBasedCorrection
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
              - title: Beam Raster Dimensions
                description: "Dimensions of the small area over which the beam is
                  rastered during a single analysis point, reported as width \xD7
                  height in \xB5m. Applicable when Beam Mode = Rastered; defines the
                  effective spatial footprint of the measurement and distributes dose
                  over a larger area to reduce beam damage on sensitive phases."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semCompositionTAPP/beamRasterDimensions
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semCompositionTAPP/beamRasterDimensions
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
              - title: Beam Damage Minimization
                description: 'Describes any measures taken to reduce electron beam
                  damage to the sample during analysis. Examples: reduced accelerating
                  voltage, lowered beam current, defocused or rastered beam, cooled
                  stage, short acquisition sequences, or rotating between multiple
                  points. Particularly important for volatile-bearing phases, hydrous
                  minerals, glasses, organic materials, and biological samples.'
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semCompositionTAPP/beamDamageMinimization
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semCompositionTAPP/beamDamageMinimization
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
              - title: Drift Correction
                description: 'Describes whether and how stage or beam drift was monitored
                  and corrected during the measurement session. Examples: periodic
                  stage realignment to a fiducial marker, automated beam drift correction
                  in acquisition software, or reanalysis of a reference point at regular
                  intervals. Particularly relevant for long mapping runs and high-magnification
                  sessions where positional accuracy affects data quality.'
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semCompositionTAPP/driftCorrection
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semCompositionTAPP/driftCorrection
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
              - title: Chamber Pressure
                description: Chamber pressure and gas type during analysis. Required
                  for variable pressure (VP-SEM) and environmental SEM (ESEM) modes.
                  Report value and unit (Pa or Torr) and gas composition. Use 'None'
                  for standard high-vacuum operation.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semCompositionTAPP/chamberPressure
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semCompositionTAPP/chamberPressure
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
              - title: EDS Live Time per Point or Pixel
                description: EDS spectral acquisition live time per analysis point
                  or per pixel in seconds. Longer live time improves counting statistics
                  but increases beam damage risk and total acquisition time.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semCompositionTAPP/edsLiveTimePerPointOrPixel
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semCompositionTAPP/edsLiveTimePerPointOrPixel
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
              - title: Step Size / Pixel Size
                description: "Centre-to-centre distance between adjacent measurement
                  points (WDS mapping) or pixels (EDS mapping) in \xB5m. Defines the
                  spatial sampling interval of the map and, together with the pixel-grid
                  dimensions, determines the total mapped area. Smaller step sizes
                  increase spatial resolution but extend acquisition time."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semCompositionTAPP/stepSizePixelSize
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semCompositionTAPP/stepSizePixelSize
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
              - title: Halogen Correction on Oxygen
                description: Whether oxygen content was adjusted to account for halogen
                  substitution (F and/or Cl replacing OH) in halogen-bearing phases
                  such as apatite, amphibole, and mica, where oxygen is calculated
                  by stoichiometry.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semCompositionTAPP/halogenCorrectionOnOxygen
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semCompositionTAPP/halogenCorrectionOnOxygen
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
              - title: Detection Limit
                description: Method detection limit at 99% confidence, one per reported
                  concentration variable (one per analyte, these being the same set).
                  Include the method used and the resulting value for each.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semCompositionTAPP/detectionLimit
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semCompositionTAPP/detectionLimit
                  schema:name:
                    const: Detection Limit
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
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/targetSelection/schema.yaml#/$defs/Param_Analysis_targetSelectionCriteria
              minContains: 0
              maxContains: 1
            - contains:
                title: Beam Raster Dimensions
                description: "Dimensions of the small area over which the beam is
                  rastered during a single analysis point, reported as width \xD7
                  height in \xB5m. Applicable when Beam Mode = Rastered; defines the
                  effective spatial footprint of the measurement and distributes dose
                  over a larger area to reduce beam damage on sensitive phases."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semCompositionTAPP/beamRasterDimensions
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semCompositionTAPP/beamRasterDimensions
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
                title: Beam Damage Minimization
                description: 'Describes any measures taken to reduce electron beam
                  damage to the sample during analysis. Examples: reduced accelerating
                  voltage, lowered beam current, defocused or rastered beam, cooled
                  stage, short acquisition sequences, or rotating between multiple
                  points. Particularly important for volatile-bearing phases, hydrous
                  minerals, glasses, organic materials, and biological samples.'
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semCompositionTAPP/beamDamageMinimization
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semCompositionTAPP/beamDamageMinimization
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
                title: Drift Correction
                description: 'Describes whether and how stage or beam drift was monitored
                  and corrected during the measurement session. Examples: periodic
                  stage realignment to a fiducial marker, automated beam drift correction
                  in acquisition software, or reanalysis of a reference point at regular
                  intervals. Particularly relevant for long mapping runs and high-magnification
                  sessions where positional accuracy affects data quality.'
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semCompositionTAPP/driftCorrection
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semCompositionTAPP/driftCorrection
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
                title: Chamber Pressure
                description: Chamber pressure and gas type during analysis. Required
                  for variable pressure (VP-SEM) and environmental SEM (ESEM) modes.
                  Report value and unit (Pa or Torr) and gas composition. Use 'None'
                  for standard high-vacuum operation.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semCompositionTAPP/chamberPressure
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semCompositionTAPP/chamberPressure
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
                title: EDS Live Time per Point or Pixel
                description: EDS spectral acquisition live time per analysis point
                  or per pixel in seconds. Longer live time improves counting statistics
                  but increases beam damage risk and total acquisition time.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semCompositionTAPP/edsLiveTimePerPointOrPixel
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semCompositionTAPP/edsLiveTimePerPointOrPixel
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
                title: Step Size / Pixel Size
                description: "Centre-to-centre distance between adjacent measurement
                  points (WDS mapping) or pixels (EDS mapping) in \xB5m. Defines the
                  spatial sampling interval of the map and, together with the pixel-grid
                  dimensions, determines the total mapped area. Smaller step sizes
                  increase spatial resolution but extend acquisition time."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semCompositionTAPP/stepSizePixelSize
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semCompositionTAPP/stepSizePixelSize
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
                title: Halogen Correction on Oxygen
                description: Whether oxygen content was adjusted to account for halogen
                  substitution (F and/or Cl replacing OH) in halogen-bearing phases
                  such as apatite, amphibole, and mica, where oxygen is calculated
                  by stoichiometry.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semCompositionTAPP/halogenCorrectionOnOxygen
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semCompositionTAPP/halogenCorrectionOnOxygen
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
                title: Detection Limit
                description: Method detection limit at 99% confidence, one per reported
                  concentration variable (one per analyte, these being the same set).
                  Include the method used and the resulting value for each.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semCompositionTAPP/detectionLimit
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semCompositionTAPP/detectionLimit
                  schema:name:
                    const: Detection Limit
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
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/targetSelection/schema.yaml#/$defs/Param_Analysis_preAnalysisImagingAndScreening
                      allOf:
                      - contains:
                          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/targetSelection/schema.yaml#/$defs/Param_Analysis_preAnalysisImagingAndScreening
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
                                        in kilovolts. Affects X-ray generation depth
                                        (EDS/WDS), EBSD pattern quality, imaging resolution,
                                        and beam penetration. Low voltages (1-5 kV)
                                        improve surface sensitivity and reduce beam
                                        damage; high voltages (15-20 kV) improve X-ray
                                        generation for quantitative analysis.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/semCompositionTAPP/acceleratingVoltage
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/semCompositionTAPP/acceleratingVoltage
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
                                        (spot size) at the sample surface, in nanometres
                                        or micrometres, as set by the condenser aperture
                                        and working distance. Controls the spatial
                                        resolution and X-ray excitation volume. For
                                        mapping modes, the effective spatial sampling
                                        interval is further defined by Step Size /
                                        Pixel Size.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/semCompositionTAPP/beamDiameter
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/semCompositionTAPP/beamDiameter
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
                                    - title: Working Distance
                                      description: Distance between the objective
                                        lens pole piece and the specimen surface in
                                        millimetres. Affects spatial resolution, depth
                                        of focus, EDS X-ray take-off angle, and EBSD
                                        geometry.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/semCompositionTAPP/workingDistance
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/semCompositionTAPP/workingDistance
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
                                      title: Accelerating Voltage
                                      description: Electron beam accelerating voltage
                                        in kilovolts. Affects X-ray generation depth
                                        (EDS/WDS), EBSD pattern quality, imaging resolution,
                                        and beam penetration. Low voltages (1-5 kV)
                                        improve surface sensitivity and reduce beam
                                        damage; high voltages (15-20 kV) improve X-ray
                                        generation for quantitative analysis.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/semCompositionTAPP/acceleratingVoltage
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/semCompositionTAPP/acceleratingVoltage
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
                                        (spot size) at the sample surface, in nanometres
                                        or micrometres, as set by the condenser aperture
                                        and working distance. Controls the spatial
                                        resolution and X-ray excitation volume. For
                                        mapping modes, the effective spatial sampling
                                        interval is further defined by Step Size /
                                        Pixel Size.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/semCompositionTAPP/beamDiameter
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/semCompositionTAPP/beamDiameter
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
                                      title: Working Distance
                                      description: Distance between the objective
                                        lens pole piece and the specimen surface in
                                        millimetres. Affects spatial resolution, depth
                                        of focus, EDS X-ray take-off angle, and EBSD
                                        geometry.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/semCompositionTAPP/workingDistance
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/semCompositionTAPP/workingDistance
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
                      allOf:
                      - contains:
                          properties:
                            schema:additionalType:
                              contains:
                                const: SEM
                              schema:inDefinedTermSet: ada:vocab/instrumentType
                          required:
                          - schema:additionalType
          ada:proceduralBlankLevel:
            description: "The measured level of the analytical blank in the session,
              and \u2014 where the reported quantity is a ratio \u2014 its composition,
              since a blank subtracted from a ratio biases the result unless its own
              composition is known. Companion to the blank correction method, which
              is procedure-level: this field records what was actually measured. Follows
              the criterion-versus-measurement split the library applies wherever
              a procedure sets a threshold and an analysis reports a value against
              it."
            type: string
          ada:deadTime:
            description: "Percent dead time reported by the EDS detector during the
              session \u2014 the fraction of total acquisition time the detector spent
              processing rather than counting. EDS dead time correction is managed
              automatically by the detector electronics; this field documents the
              resulting percentage as a session QC metric. Values above ~40% indicate
              excessive count rate and may degrade spectral quality and quantitative
              accuracy. Unlike WDS dead time (see WDS Dead Time Correction), no user-selectable
              correction algorithm is required."
            anyOf:
            - type: number
            - type: string
    ada:mapDimensions:
      description: Number of pixels in the EDS map in the X and Y directions. Determined
        at analysis time based on the area of interest and selected pixel size.
      anyOf:
      - type: number
      - type: string
    schema:additionalProperty:
      type: array
      items:
        title: Map Area
        description: "Physical area covered by the map in \xB5m\xB2 or mm\xB2, calculated
          as (map width in pixels \xD7 step size) \xD7 (map height in pixels \xD7
          step size). Complements the map's pixel-grid dimensions by recording the
          physical scale of the mapped region; useful for direct comparison across
          datasets acquired with different step sizes."
        type: object
        properties:
          '@id':
            const: ada:parameter/semCompositionTAPP/mapArea
          '@type':
            const:
            - schema:PropertyValue
          schema:propertyID:
            const:
            - '@id': ada:parameter/semCompositionTAPP/mapArea
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
          description: "Physical area covered by the map in \xB5m\xB2 or mm\xB2, calculated
            as (map width in pixels \xD7 step size) \xD7 (map height in pixels \xD7
            step size). Complements the map's pixel-grid dimensions by recording the
            physical scale of the mapped region; useful for direct comparison across
            datasets acquired with different step sizes."
          type: object
          properties:
            '@id':
              const: ada:parameter/semCompositionTAPP/mapArea
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/semCompositionTAPP/mapArea
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
        - title: Normalization / Standards-Based Correction
          description: Post-acquisition normalization applied using secondary reference
            materials to correct for session-to-session calibration drift.
          type: object
          properties:
            '@id':
              const: ada:parameter/semCompositionTAPP/normalizationStandardsBasedCorrection
            '@type':
              const:
              - schema:PropertyValue
              - cdi:InstanceVariable
            schema:propertyID:
              const:
              - '@id': ada:parameter/semCompositionTAPP/normalizationStandardsBasedCorrection
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
        - title: Detection Limit
          description: Method detection limit at 99% confidence, one per reported
            concentration variable (one per analyte, these being the same set). Include
            the method used and the resulting value for each.
          type: object
          properties:
            '@id':
              const: ada:parameter/semCompositionTAPP/detectionLimit
            '@type':
              const:
              - schema:PropertyValue
              - cdi:InstanceVariable
            schema:propertyID:
              const:
              - '@id': ada:parameter/semCompositionTAPP/detectionLimit
            schema:name:
              const: Detection Limit
            schema:value:
              type: string
          required:
          - '@id'
          - '@type'
          - schema:propertyID
          - schema:name
          - schema:value
        - title: Detection Limit Method
          description: Formula or approach used to calculate detection limits.
          type: object
          properties:
            '@id':
              const: ada:parameter/semCompositionTAPP/detectionLimitMethod
            '@type':
              const:
              - schema:PropertyValue
              - cdi:InstanceVariable
            schema:propertyID:
              const:
              - '@id': ada:parameter/semCompositionTAPP/detectionLimitMethod
            schema:name:
              const: Detection Limit Method
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
          title: Normalization / Standards-Based Correction
          description: Post-acquisition normalization applied using secondary reference
            materials to correct for session-to-session calibration drift.
          type: object
          properties:
            '@id':
              const: ada:parameter/semCompositionTAPP/normalizationStandardsBasedCorrection
            '@type':
              const:
              - schema:PropertyValue
              - cdi:InstanceVariable
            schema:propertyID:
              const:
              - '@id': ada:parameter/semCompositionTAPP/normalizationStandardsBasedCorrection
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
          title: Detection Limit
          description: Method detection limit at 99% confidence, one per reported
            concentration variable (one per analyte, these being the same set). Include
            the method used and the resulting value for each.
          type: object
          properties:
            '@id':
              const: ada:parameter/semCompositionTAPP/detectionLimit
            '@type':
              const:
              - schema:PropertyValue
              - cdi:InstanceVariable
            schema:propertyID:
              const:
              - '@id': ada:parameter/semCompositionTAPP/detectionLimit
            schema:name:
              const: Detection Limit
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
          title: Detection Limit Method
          description: Formula or approach used to calculate detection limits.
          type: object
          properties:
            '@id':
              const: ada:parameter/semCompositionTAPP/detectionLimitMethod
            '@type':
              const:
              - schema:PropertyValue
              - cdi:InstanceVariable
            schema:propertyID:
              const:
              - '@id': ada:parameter/semCompositionTAPP/detectionLimitMethod
            schema:name:
              const: Detection Limit Method
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

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM-Composition/detail/context.jsonld)

## Sources

* [SEM_Composition_TAPP_v4.xlsx (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/SEM-Composition/detail`

