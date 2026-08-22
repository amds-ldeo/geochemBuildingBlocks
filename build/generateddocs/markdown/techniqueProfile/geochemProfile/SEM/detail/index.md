
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
      "@id": "ex:semTAPP-Garvie2008"
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
      "schema:name": "NASA NNG06GE37G (LAJG); NASA NNG06GF08G (PRB)"
    }
  ],
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
      "@id": "ex:semTAPP-Garvie2008"
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
      "schema:name": "NASA NNG06GE37G (LAJG); NASA NNG06GF08G (PRB)"
    }
  ],
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Garvie2008 a ada:SEMImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NASA NNG06GE37G (LAJG); NASA NNG06GF08G (PRB)" ] ;
    schema1:measurementTechnique ex:semTAPP-Garvie2008 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSize "missing" .


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
      "@id": "ex:semTAPP-Garvie2008-2"
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
      "schema:name": "NASA NNG06GE37G (LAJG); NASA NNG06GF08G (PRB)"
    }
  ],
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
  "@id": "ex:detail-Garvie2008-2",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Garvie2008-2"
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
      "schema:name": "NASA NNG06GE37G (LAJG); NASA NNG06GF08G (PRB)"
    }
  ],
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Garvie2008-2 a ada:SEMImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NASA NNG06GE37G (LAJG); NASA NNG06GF08G (PRB)" ] ;
    schema1:measurementTechnique ex:semTAPP-Garvie2008-2 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSize "missing" .


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
      "@id": "ex:semTAPP-Genge2025"
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
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
      "@id": "ex:semTAPP-Genge2025"
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
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Genge2025 a ada:SEMImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:semTAPP-Genge2025 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSize "missing" .


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
      "@id": "ex:semTAPP-Genge2025-2"
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
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
      "@id": "ex:semTAPP-Genge2025-2"
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
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Genge2025-2 a ada:SEMImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:semTAPP-Genge2025-2 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSize "missing" .


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
      "@id": "ex:semTAPP-Genge2025-3"
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
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
      "@id": "ex:semTAPP-Genge2025-3"
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
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Genge2025-3 a ada:SEMImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:semTAPP-Genge2025-3 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSize "missing" .


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
      "@id": "ex:semTAPP-Gucsik2013"
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
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
      "@id": "ex:semTAPP-Gucsik2013"
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
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Gucsik2013 a ada:SEMImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:semTAPP-Gucsik2013 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSize "missing" .


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
      "@id": "ex:semTAPP-Gucsik2013-2"
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
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
      "@id": "ex:semTAPP-Gucsik2013-2"
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
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Gucsik2013-2 a ada:SEMImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:semTAPP-Gucsik2013-2 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSize "missing" .


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
      "@id": "ex:semTAPP-Izawa2010"
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
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
      "@id": "ex:semTAPP-Izawa2010"
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
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Izawa2010 a ada:SEMImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:semTAPP-Izawa2010 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSize "missing" .


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
      "@id": "ex:semTAPP-Izawa2010-2"
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
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
      "@id": "ex:semTAPP-Izawa2010-2"
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
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Izawa2010-2 a ada:SEMImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:semTAPP-Izawa2010-2 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSize "missing" .


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
      "@id": "ex:semTAPP-Izawa2010-3"
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
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "~0.5 wt% for most elements",
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
      "@id": "ex:semTAPP-Izawa2010-3"
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
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "~0.5 wt% for most elements",
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
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Izawa2010-3 a ada:SEMImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:semTAPP-Izawa2010-3 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "~0.5 wt% for most elements" ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSize "missing" .


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
      "@id": "ex:semTAPP-Izawa2010-4"
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
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
      "@id": "ex:semTAPP-Izawa2010-4"
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
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Izawa2010-4 a ada:SEMImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:semTAPP-Izawa2010-4 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSize "missing" .


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
      "@id": "ex:semTAPP-Izawa2010-5"
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
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
      "@id": "ex:semTAPP-Izawa2010-5"
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
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Izawa2010-5 a ada:SEMImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:semTAPP-Izawa2010-5 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSize "missing" .


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
      "@id": "ex:semTAPP-Liu2017"
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
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "9.8 × 9.8 × 15 nm voxel size; 600 slices; 7.8 × 7.8 µm scanning area; 9.0 µm total thickness",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
      "@id": "ex:semTAPP-Liu2017"
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
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "9.8 \u00d7 9.8 \u00d7 15 nm voxel size; 600 slices; 7.8 \u00d7 7.8 \u00b5m scanning area; 9.0 \u00b5m total thickness",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Liu2017 a ada:SEMImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:semTAPP-Liu2017 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "9.8 × 9.8 × 15 nm voxel size; 600 slices; 7.8 × 7.8 µm scanning area; 9.0 µm total thickness" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSize "missing" .


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
      "@id": "ex:semTAPP-Liu2017-2"
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
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
      "@id": "ex:semTAPP-Liu2017-2"
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
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Liu2017-2 a ada:SEMImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:semTAPP-Liu2017-2 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSize "missing" .


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
      "@id": "ex:semTAPP-Liu2017-3"
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
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
      "@id": "ex:semTAPP-Liu2017-3"
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
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Liu2017-3 a ada:SEMImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:semTAPP-Liu2017-3 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSize "missing" .


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
      "@id": "ex:semTAPP-Ma2017"
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
      "schema:name": "NSF EAR-0318518; NSF DMR-0080065 (supporting Caltech GPS Analytical Facility)"
    }
  ],
  "ada:sampleName": "Section 126A (USNM 7908)",
  "ada:samplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
      "@id": "ex:semTAPP-Ma2017"
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
      "schema:name": "NSF EAR-0318518; NSF DMR-0080065 (supporting Caltech GPS Analytical Facility)"
    }
  ],
  "ada:sampleName": "Section 126A (USNM 7908)",
  "ada:samplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Ma2017 a ada:SEMImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NSF EAR-0318518; NSF DMR-0080065 (supporting Caltech GPS Analytical Facility)" ] ;
    schema1:measurementTechnique ex:semTAPP-Ma2017 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "Section 126A (USNM 7908)" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSize "missing" .


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
      "@id": "ex:semTAPP-Ma2017-2"
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
      "schema:name": "NSF EAR-0318518; NSF DMR-0080065 (supporting Caltech GPS Analytical Facility)"
    }
  ],
  "ada:sampleName": "Section 126A (USNM 7908)",
  "ada:samplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
      "@id": "ex:semTAPP-Ma2017-2"
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
      "schema:name": "NSF EAR-0318518; NSF DMR-0080065 (supporting Caltech GPS Analytical Facility)"
    }
  ],
  "ada:sampleName": "Section 126A (USNM 7908)",
  "ada:samplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Ma2017-2 a ada:SEMImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NSF EAR-0318518; NSF DMR-0080065 (supporting Caltech GPS Analytical Facility)" ] ;
    schema1:measurementTechnique ex:semTAPP-Ma2017-2 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation 3e-01 ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "Section 126A (USNM 7908)" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSize "missing" .


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
      "@id": "ex:semTAPP-Pascucci2026"
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
  "ada:sampleName": "NWA 7317",
  "ada:samplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
      "@id": "ex:semTAPP-Pascucci2026"
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
  "ada:sampleName": "NWA 7317",
  "ada:samplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Pascucci2026 a ada:SEMImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:semTAPP-Pascucci2026 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "NWA 7317" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSize "missing" .


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
      "@id": "ex:semTAPP-Pascucci2026-2"
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
  "ada:sampleName": "NWA 7317",
  "ada:samplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
      "@id": "ex:semTAPP-Pascucci2026-2"
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
  "ada:sampleName": "NWA 7317",
  "ada:samplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Pascucci2026-2 a ada:SEMImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:semTAPP-Pascucci2026-2 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "NWA 7317" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSize "missing" .


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
      "@id": "ex:semTAPP-Pascucci2026-3"
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
  "ada:sampleName": "NWA 7317",
  "ada:samplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": 1024,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
      "@id": "ex:semTAPP-Pascucci2026-3"
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
  "ada:sampleName": "NWA 7317",
  "ada:samplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": 1024,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Pascucci2026-3 a ada:SEMImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:semTAPP-Pascucci2026-3 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions 1024 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "NWA 7317" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSize "missing" .


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
      "@id": "ex:semTAPP-Pascucci2026-4"
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
  "ada:sampleName": "NWA 7317",
  "ada:samplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
      "@id": "ex:semTAPP-Pascucci2026-4"
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
  "ada:sampleName": "NWA 7317",
  "ada:samplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Pascucci2026-4 a ada:SEMImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:semTAPP-Pascucci2026-4 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "NWA 7317" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSize "missing" .


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
      "@id": "ex:semTAPP-Zhou2017"
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
  "ada:sampleName": "SC; HBC",
  "ada:samplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "14.8×14.8 nm pixel size (XY); ~800 total slices; sub-volumes: SC=5.609×3.08×5.446 µm; HBC=4.679×3.2×4.24 µm; SEM image resolution 2.5 nm",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
      "@id": "ex:semTAPP-Zhou2017"
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
  "ada:sampleName": "SC; HBC",
  "ada:samplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "14.8\u00d714.8 nm pixel size (XY); ~800 total slices; sub-volumes: SC=5.609\u00d73.08\u00d75.446 \u00b5m; HBC=4.679\u00d73.2\u00d74.24 \u00b5m; SEM image resolution 2.5 nm",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Zhou2017 a ada:SEMImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:semTAPP-Zhou2017 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "14.8×14.8 nm pixel size (XY); ~800 total slices; sub-volumes: SC=5.609×3.08×5.446 µm; HBC=4.679×3.2×4.24 µm; SEM image resolution 2.5 nm" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "SC; HBC" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSize "missing" .


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
      "@id": "ex:semTAPP-Zega2025"
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
      "schema:name": "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)"
    }
  ],
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
      "@id": "ex:semTAPP-Zega2025"
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
      "schema:name": "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)"
    }
  ],
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Zega2025 a ada:SEMImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)" ] ;
    schema1:measurementTechnique ex:semTAPP-Zega2025 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSize "missing" .


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
      "@id": "ex:semTAPP-Zega2025-2"
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
      "schema:name": "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)"
    }
  ],
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
      "@id": "ex:semTAPP-Zega2025-2"
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
      "schema:name": "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)"
    }
  ],
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Zega2025-2 a ada:SEMImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)" ] ;
    schema1:measurementTechnique ex:semTAPP-Zega2025-2 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSize "missing" .


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
      "@id": "ex:semTAPP-Zega2025-3"
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
      "schema:name": "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599"
    }
  ],
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
      "@id": "ex:semTAPP-Zega2025-3"
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
      "schema:name": "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599"
    }
  ],
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Zega2025-3 a ada:SEMImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599" ] ;
    schema1:measurementTechnique ex:semTAPP-Zega2025-3 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSize "missing" .


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
      "@id": "ex:semTAPP-Zega2025-4"
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
      "schema:name": "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599"
    }
  ],
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
      "@id": "ex:semTAPP-Zega2025-4"
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
      "schema:name": "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599"
    }
  ],
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Zega2025-4 a ada:SEMImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599" ] ;
    schema1:measurementTechnique ex:semTAPP-Zega2025-4 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSize "missing" .


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
      "@id": "ex:semTAPP-Zega2025-5"
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
      "schema:name": "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599"
    }
  ],
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
      "@id": "ex:semTAPP-Zega2025-5"
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
      "schema:name": "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599"
    }
  ],
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Zega2025-5 a ada:SEMImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NASA PSEF 80NSSC23K0327; NSF MRI 1531243 and 0619599" ] ;
    schema1:measurementTechnique ex:semTAPP-Zega2025-5 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSize "missing" .


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
      "@id": "ex:semTAPP-Zega2025-6"
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
      "schema:name": "NASA PSEF 80NSSC23K0327; NASA Planetary Major Equipment NNX12AL47G; NSF MRI 0619599"
    }
  ],
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
  "@id": "ex:detail-Zega2025-6",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Zega2025-6"
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
      "schema:name": "NASA PSEF 80NSSC23K0327; NASA Planetary Major Equipment NNX12AL47G; NSF MRI 0619599"
    }
  ],
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Zega2025-6 a ada:SEMImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NASA PSEF 80NSSC23K0327; NASA Planetary Major Equipment NNX12AL47G; NSF MRI 0619599" ] ;
    schema1:measurementTechnique ex:semTAPP-Zega2025-6 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSize "missing" .


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
      "@id": "ex:semTAPP-Zega2025-7"
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
      "schema:name": "US DOE contract DE-AC02-05CH11231 (Advanced Light Source / Molecular Foundry)"
    }
  ],
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
  "@id": "ex:detail-Zega2025-7",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Zega2025-7"
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
      "schema:name": "US DOE contract DE-AC02-05CH11231 (Advanced Light Source / Molecular Foundry)"
    }
  ],
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Zega2025-7 a ada:SEMImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "US DOE contract DE-AC02-05CH11231 (Advanced Light Source / Molecular Foundry)" ] ;
    schema1:measurementTechnique ex:semTAPP-Zega2025-7 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSize "missing" .


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
      "@id": "ex:semTAPP-Zega2025-8"
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
      "schema:name": "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)"
    }
  ],
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
  "@id": "ex:detail-Zega2025-8",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Zega2025-8"
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
      "schema:name": "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)"
    }
  ],
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Zega2025-8 a ada:SEMImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "NASA award NNH09ZDA007O; contract NNM10AA11C (OSIRIS-REx New Frontiers)" ] ;
    schema1:measurementTechnique ex:semTAPP-Zega2025-8 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSize "missing" .


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
      "@id": "ex:semTAPP-Zega2025-9"
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
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
      "@id": "ex:semTAPP-Zega2025-9"
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
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Zega2025-9 a ada:SEMImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:semTAPP-Zega2025-9 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSize "missing" .


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
      "@id": "ex:semTAPP-Barnes2025"
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
  "ada:sampleName": "OREX-501018-100",
  "ada:samplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
      "@id": "ex:semTAPP-Barnes2025"
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
  "ada:sampleName": "OREX-501018-100",
  "ada:samplingUnit": "missing",
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Barnes2025 a ada:SEMImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:semTAPP-Barnes2025 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "OREX-501018-100" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSize "missing" .


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
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Barnes2025-2"
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
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
  "@id": "ex:detail-Barnes2025-2",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Barnes2025-2"
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
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Barnes2025-2 a ada:SEMImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:semTAPP-Barnes2025-2 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSize "missing" .


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
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Barnes2025-3"
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
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
  "@id": "ex:detail-Barnes2025-3",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Barnes2025-3"
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
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Barnes2025-3 a ada:SEMImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:semTAPP-Barnes2025-3 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSize "missing" .


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
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Barnes2025-4"
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
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
  "@id": "ex:detail-Barnes2025-4",
  "@type": [
    "ada:SEMImage"
  ],
  "ada:componentType": "ada:SEMImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:semTAPP-Barnes2025-4"
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
  "ada:imagePixelSize": -9999,
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:imageStackDimenstions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
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
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Barnes2025-4 a ada:SEMImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:semTAPP-Barnes2025-4 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:SEMImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:ebsdIndexingRate -9999 ;
    ada:ebsdMeanAngularDeviation -9999 ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:imageStackDimenstions "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSize "missing" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: SEM Analysis Detail
description: Dataset-level analysis-instance detail for SEM (superset), reusing CDIF/schema.org
  slots on the schema:Dataset root.
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
              - title: 3D Segmentation Method
                description: Method and software used to segment phases and features
                  in the aligned 3D image stack, transforming the grayscale stack
                  into labelled 3D regions (pores, mineral phases, grain boundaries,
                  organic matter).
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/segmentationMethod3D
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/segmentationMethod3D
                  schema:name:
                    const: 3D Segmentation Method
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
                  points. Particularly important for volatile-bearing phases, hydrous
                  minerals, glasses, organic materials, and biological samples.'
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
                  rastered during a single analysis point, reported as width \xD7
                  height in \xB5m. Applicable when Beam Mode = Rastered; defines the
                  effective spatial footprint of the measurement and distributes dose
                  over a larger area to reduce beam damage on sensitive phases."
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
                  per spectrum (spectral point mode), in ms or s. Longer integration
                  improves signal-to-noise but increases beam dose and acquisition
                  time.
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
                  intervals. Particularly relevant for long mapping runs and high-magnification
                  sessions where positional accuracy affects data quality.'
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
                  milliseconds. Longer frame time improves pattern quality and indexing
                  rate but increases total acquisition time.
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
                  library for this procedure. The procedure specifies the expected
                  phase suite for the target material; analysts may add phases for
                  specific sample compositions.
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
                  of interest to resolve grain boundary positions and intragrain orientation
                  gradients."
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
                  or per pixel in seconds. Longer live time improves counting statistics
                  but increases beam damage risk and total acquisition time.
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
                  in nm or \xB5m. Defines spatial sampling of SE or BSE images. For
                  large-area mosaic imaging, report the pixel size of individual tiles
                  and the number and arrangement of tiles."
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
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/blank/schema.yaml#/$defs/Param_Analysis_proceduralBlankLevel
              - title: Step Size / Pixel Size
                description: "Centre-to-centre distance between adjacent measurement
                  points (WDS mapping) or pixels (EDS mapping) in \xB5m. Defines the
                  spatial sampling interval of the map and, together with the pixel-grid
                  dimensions, determines the total mapped area. Smaller step sizes
                  increase spatial resolution but extend acquisition time."
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
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/targetSelection/schema.yaml#/$defs/Param_Analysis_targetSelectionCriteria
              - title: Working Distance
                description: Distance between the objective lens pole piece and the
                  specimen surface in millimetres. Affects spatial resolution, depth
                  of focus, EDS X-ray take-off angle, and EBSD geometry.
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
                title: 3D Segmentation Method
                description: Method and software used to segment phases and features
                  in the aligned 3D image stack, transforming the grayscale stack
                  into labelled 3D regions (pores, mineral phases, grain boundaries,
                  organic matter).
                type: object
                properties:
                  '@id':
                    const: ada:parameter/semTAPP/segmentationMethod3D
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/semTAPP/segmentationMethod3D
                  schema:name:
                    const: 3D Segmentation Method
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
                  points. Particularly important for volatile-bearing phases, hydrous
                  minerals, glasses, organic materials, and biological samples.'
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
                  rastered during a single analysis point, reported as width \xD7
                  height in \xB5m. Applicable when Beam Mode = Rastered; defines the
                  effective spatial footprint of the measurement and distributes dose
                  over a larger area to reduce beam damage on sensitive phases."
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
                  per spectrum (spectral point mode), in ms or s. Longer integration
                  improves signal-to-noise but increases beam dose and acquisition
                  time.
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
                  intervals. Particularly relevant for long mapping runs and high-magnification
                  sessions where positional accuracy affects data quality.'
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
                  milliseconds. Longer frame time improves pattern quality and indexing
                  rate but increases total acquisition time.
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
                  library for this procedure. The procedure specifies the expected
                  phase suite for the target material; analysts may add phases for
                  specific sample compositions.
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
                  of interest to resolve grain boundary positions and intragrain orientation
                  gradients."
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
                  or per pixel in seconds. Longer live time improves counting statistics
                  but increases beam damage risk and total acquisition time.
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
                  in nm or \xB5m. Defines spatial sampling of SE or BSE images. For
                  large-area mosaic imaging, report the pixel size of individual tiles
                  and the number and arrangement of tiles."
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
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/blank/schema.yaml#/$defs/Param_Analysis_proceduralBlankLevel
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
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/targetSelection/schema.yaml#/$defs/Param_Analysis_targetSelectionCriteria
              minContains: 0
              maxContains: 1
            - contains:
                title: Working Distance
                description: Distance between the objective lens pole piece and the
                  specimen surface in millimetres. Affects spatial resolution, depth
                  of focus, EDS X-ray take-off angle, and EBSD geometry.
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
                                        in kilovolts. Affects X-ray generation depth
                                        (EDS/WDS), EBSD pattern quality, imaging resolution,
                                        and beam penetration. Low voltages (1-5 kV)
                                        improve surface sensitivity and reduce beam
                                        damage; high voltages (15-20 kV) improve X-ray
                                        generation for quantitative analysis.
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
                                Low-voltage polishing (2 kV or below) minimises Ga
                                implantation depth, surface amorphisation, and curtaining
                                artifacts.
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
                                FIB milling. E-beam deposition causes less surface
                                damage than ion-beam deposition and should be applied
                                as the initial layer. Typical coatings: platinum (Pt)
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
                                Low-voltage polishing (2 kV or below) minimises Ga
                                implantation depth, surface amorphisation, and curtaining
                                artifacts.
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
                                FIB milling. E-beam deposition causes less surface
                                damage than ion-beam deposition and should be applied
                                as the initial layer. Typical coatings: platinum (Pt)
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
                          const: Ion Milling
                      required:
                      - schema:name
                    then:
                      properties:
                        schema:description:
                          description: Ion beam voltage and current used to mill each
                            slice during FIB-SEM serial sectioning. These parameters
                            determine material removal rate per slice and exposed
                            surface quality.
                          anyOf:
                          - type: string
                          - type: array
                            items:
                              type: string
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
                        const: Ion Milling
                    required:
                    - schema:name
          ada:ebsdIndexingRate:
            description: Fraction of EBSD map points successfully indexed, expressed
              as a percentage of total map points. Low indexing rate may indicate
              surface damage, amorphisation, severe deformation, or phase misidentification.
            anyOf:
            - type: number
            - type: string
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
                          description: 'Target thickness of the electron-transparent
                            TEM lamella after final FIB polishing, in nanometres.
                            Actual thickness may differ from target. Typical range:
                            50-150 nm for standard TEM/STEM; 200-600 nm for XANES
                            or tomography sections.'
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
                        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/targetSelection/schema.yaml#/$defs/Param_Analysis_preAnalysisImagingAndScreening
                        - title: Slice Thickness
                          description: Thickness of each FIB-milled slice during serial
                            sectioning in nanometres. Controls the Z-axis resolution
                            of the 3D reconstruction.
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
                          description: 'Target thickness of the electron-transparent
                            TEM lamella after final FIB polishing, in nanometres.
                            Actual thickness may differ from target. Typical range:
                            50-150 nm for standard TEM/STEM; 200-600 nm for XANES
                            or tomography sections.'
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
                          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/targetSelection/schema.yaml#/$defs/Param_Analysis_preAnalysisImagingAndScreening
                        minContains: 0
                        maxContains: 1
                      - contains:
                          title: Slice Thickness
                          description: Thickness of each FIB-milled slice during serial
                            sectioning in nanometres. Controls the Z-axis resolution
                            of the 3D reconstruction.
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
        - title: Calibration Factor and Determination Method
          description: 'An externally-calibrated factor that converts the measured
            quantity into the reported quantity, how it was determined, and its uncertainty.
            Applies where the conversion depends on a factor calibrated against a
            reference of independently known value, rather than on the instrument
            response alone. Distinct from the fields that name the calibration material
            and that state which approach applies to which analyte, where the technique
            has them: this field records the resulting factor itself.'
          type: object
          properties:
            '@id':
              const: ada:parameter/semTAPP/calibrationFactorAndDeterminationMethod
            '@type':
              const:
              - schema:PropertyValue
              - cdi:InstanceVariable
            schema:propertyID:
              const:
              - '@id': ada:parameter/semTAPP/calibrationFactorAndDeterminationMethod
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
        - title: Detection Limit
          description: Method detection limit at 99% confidence, one per reported
            concentration variable (one per analyte, these being the same set). Include
            the method used and the resulting value for each.
          type: object
          properties:
            '@id':
              const: ada:parameter/semTAPP/detectionLimit
            '@type':
              const:
              - schema:PropertyValue
              - cdi:InstanceVariable
            schema:propertyID:
              const:
              - '@id': ada:parameter/semTAPP/detectionLimit
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
              const: ada:parameter/semTAPP/detectionLimitMethod
            '@type':
              const:
              - schema:PropertyValue
              - cdi:InstanceVariable
            schema:propertyID:
              const:
              - '@id': ada:parameter/semTAPP/detectionLimitMethod
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
        - title: Normalization / Standards-Based Correction
          description: Post-acquisition normalization applied using secondary reference
            materials to correct for session-to-session calibration drift.
          type: object
          properties:
            '@id':
              const: ada:parameter/semTAPP/normalizationStandardsBasedCorrection
            '@type':
              const:
              - schema:PropertyValue
              - cdi:InstanceVariable
            schema:propertyID:
              const:
              - '@id': ada:parameter/semTAPP/normalizationStandardsBasedCorrection
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
      allOf:
      - contains:
          title: Calibration Factor and Determination Method
          description: 'An externally-calibrated factor that converts the measured
            quantity into the reported quantity, how it was determined, and its uncertainty.
            Applies where the conversion depends on a factor calibrated against a
            reference of independently known value, rather than on the instrument
            response alone. Distinct from the fields that name the calibration material
            and that state which approach applies to which analyte, where the technique
            has them: this field records the resulting factor itself.'
          type: object
          properties:
            '@id':
              const: ada:parameter/semTAPP/calibrationFactorAndDeterminationMethod
            '@type':
              const:
              - schema:PropertyValue
              - cdi:InstanceVariable
            schema:propertyID:
              const:
              - '@id': ada:parameter/semTAPP/calibrationFactorAndDeterminationMethod
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
          title: Detection Limit
          description: Method detection limit at 99% confidence, one per reported
            concentration variable (one per analyte, these being the same set). Include
            the method used and the resulting value for each.
          type: object
          properties:
            '@id':
              const: ada:parameter/semTAPP/detectionLimit
            '@type':
              const:
              - schema:PropertyValue
              - cdi:InstanceVariable
            schema:propertyID:
              const:
              - '@id': ada:parameter/semTAPP/detectionLimit
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
              const: ada:parameter/semTAPP/detectionLimitMethod
            '@type':
              const:
              - schema:PropertyValue
              - cdi:InstanceVariable
            schema:propertyID:
              const:
              - '@id': ada:parameter/semTAPP/detectionLimitMethod
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
      - contains:
          title: Normalization / Standards-Based Correction
          description: Post-acquisition normalization applied using secondary reference
            materials to correct for session-to-session calibration drift.
          type: object
          properties:
            '@id':
              const: ada:parameter/semTAPP/normalizationStandardsBasedCorrection
            '@type':
              const:
              - schema:PropertyValue
              - cdi:InstanceVariable
            schema:propertyID:
              const:
              - '@id': ada:parameter/semTAPP/normalizationStandardsBasedCorrection
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
    dqv:hasQualityMeasurement:
      type: array
      items:
        type: object
        allOf:
        - if:
            properties:
              dqv:isMeasurementOf:
                const: EBSD Mean Angular Deviation
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
              const: EBSD Mean Angular Deviation
          required:
          - dqv:isMeasurementOf
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
          description: "Physical area covered by the map in \xB5m\xB2 or mm\xB2, calculated
            as (map width in pixels \xD7 step size) \xD7 (map height in pixels \xD7
            step size). Complements the map's pixel-grid dimensions by recording the
            physical scale of the mapped region; useful for direct comparison across
            datasets acquired with different step sizes."
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
        total number of slices in the stack. Determined at analysis time.
      type: string
    ada:imageStackDimenstions:
      description: X, Y, Z dimensions of the reconstructed 3D voxel in nanometres
        (X-Y pixel size from SEM image calibration; Z from slice thickness), and the
        total number of slices in the stack. Determined at analysis time.
      type: string
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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld)

## Sources

* [SEM_TAPP_v4.xlsx (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/SEM/detail`

