
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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
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
    ada:edsMapDimensions -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:mapArea -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSizeAndImageStackDimensions "missing" .


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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
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
    ada:edsMapDimensions -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:mapArea -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSizeAndImageStackDimensions "missing" .


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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
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
    ada:edsMapDimensions -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:mapArea -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSizeAndImageStackDimensions "missing" .


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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
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
    ada:edsMapDimensions -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:mapArea -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSizeAndImageStackDimensions "missing" .


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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
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
    ada:edsMapDimensions -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:mapArea -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSizeAndImageStackDimensions "missing" .


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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
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
    ada:edsMapDimensions -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:mapArea -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSizeAndImageStackDimensions "missing" .


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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
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
    ada:edsMapDimensions -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:mapArea -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSizeAndImageStackDimensions "missing" .


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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
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
    ada:edsMapDimensions -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:mapArea -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSizeAndImageStackDimensions "missing" .


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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
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
    ada:edsMapDimensions -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:mapArea -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSizeAndImageStackDimensions "missing" .


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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "~0.5 wt% for most elements",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "~0.5 wt% for most elements",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
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
    ada:edsMapDimensions -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:mapArea -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSizeAndImageStackDimensions "missing" .


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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
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
    ada:edsMapDimensions -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:mapArea -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSizeAndImageStackDimensions "missing" .


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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
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
    ada:edsMapDimensions -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:mapArea -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSizeAndImageStackDimensions "missing" .


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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "9.8 × 9.8 × 15 nm voxel size; 600 slices; 7.8 × 7.8 µm scanning area; 9.0 µm total thickness",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "9.8 \u00d7 9.8 \u00d7 15 nm voxel size; 600 slices; 7.8 \u00d7 7.8 \u00b5m scanning area; 9.0 \u00b5m total thickness",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
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
    ada:edsMapDimensions -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:mapArea -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSizeAndImageStackDimensions "9.8 × 9.8 × 15 nm voxel size; 600 slices; 7.8 × 7.8 µm scanning area; 9.0 µm total thickness" .


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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
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
    ada:edsMapDimensions -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:mapArea -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSizeAndImageStackDimensions "missing" .


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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
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
    ada:edsMapDimensions -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:mapArea -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSizeAndImageStackDimensions "missing" .


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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
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
    ada:edsMapDimensions -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:mapArea -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "Section 126A (USNM 7908)" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSizeAndImageStackDimensions "missing" .


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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": 0.3,
  "ada:ebsdIndexingRate": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": 0.3,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
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
    ada:edsMapDimensions -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:mapArea -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "Section 126A (USNM 7908)" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSizeAndImageStackDimensions "missing" .


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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
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
    ada:edsMapDimensions -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:mapArea -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "NWA 7317" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSizeAndImageStackDimensions "missing" .


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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
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
    ada:edsMapDimensions -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:mapArea -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "NWA 7317" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSizeAndImageStackDimensions "missing" .


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
  "ada:edsMapDimensions": 1024,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
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
  "ada:edsMapDimensions": 1024,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
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
    ada:edsMapDimensions 1024 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:mapArea -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "NWA 7317" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSizeAndImageStackDimensions "missing" .


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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
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
    ada:edsMapDimensions -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:mapArea -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "NWA 7317" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSizeAndImageStackDimensions "missing" .


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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "14.8×14.8 nm pixel size (XY); ~800 total slices; sub-volumes: SC=5.609×3.08×5.446 µm; HBC=4.679×3.2×4.24 µm; SEM image resolution 2.5 nm",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "14.8\u00d714.8 nm pixel size (XY); ~800 total slices; sub-volumes: SC=5.609\u00d73.08\u00d75.446 \u00b5m; HBC=4.679\u00d73.2\u00d74.24 \u00b5m; SEM image resolution 2.5 nm",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
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
    ada:edsMapDimensions -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:mapArea -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "SC; HBC" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSizeAndImageStackDimensions "14.8×14.8 nm pixel size (XY); ~800 total slices; sub-volumes: SC=5.609×3.08×5.446 µm; HBC=4.679×3.2×4.24 µm; SEM image resolution 2.5 nm" .


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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
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
    ada:edsMapDimensions -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:mapArea -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSizeAndImageStackDimensions "missing" .


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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
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
    ada:edsMapDimensions -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:mapArea -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSizeAndImageStackDimensions "missing" .


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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
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
    ada:edsMapDimensions -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:mapArea -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSizeAndImageStackDimensions "missing" .


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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
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
    ada:edsMapDimensions -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:mapArea -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSizeAndImageStackDimensions "missing" .


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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
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
    ada:edsMapDimensions -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:mapArea -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSizeAndImageStackDimensions "missing" .


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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
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
    ada:edsMapDimensions -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:mapArea -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSizeAndImageStackDimensions "missing" .


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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
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
    ada:edsMapDimensions -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:mapArea -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSizeAndImageStackDimensions "missing" .


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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
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
    ada:edsMapDimensions -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:mapArea -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSizeAndImageStackDimensions "missing" .


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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
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
    ada:edsMapDimensions -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:mapArea -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSizeAndImageStackDimensions "missing" .


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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
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
    ada:edsMapDimensions -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:mapArea -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "OREX-501018-100" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSizeAndImageStackDimensions "missing" .


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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
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
    ada:edsMapDimensions -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:mapArea -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSizeAndImageStackDimensions "missing" .


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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
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
    ada:edsMapDimensions -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:mapArea -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSizeAndImageStackDimensions "missing" .


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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
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
    "https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld",
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
  "ada:edsMapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:voxelSizeAndImageStackDimensions": "missing",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "missing",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:ebsdMeanAngularDeviation": -9999,
  "ada:ebsdIndexingRate": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "missing"
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
    ada:edsMapDimensions -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:imagePixelSize -9999 ;
    ada:mapArea -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:voxelSizeAndImageStackDimensions "missing" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: SEM Analysis Detail
description: Dataset-level analysis-instance detail for SEM (superset), reusing CDIF/schema.org
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
        schema:startDate:
          description: 'Date on which the analytical session began. For sessions spanning
            multiple days, use the date of the first session. Format: YYYY-MM-DD.'
          type: string
        schema:endDate:
          description: 'Date on which the analytical session ended. May equal Analysis
            Start Date for single-day sessions. Format: YYYY-MM-DD.'
          type: string
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
                          analysis prior to loading in the instrument. Includes mounting
                          medium (epoxy, carbon tape, stub), polishing steps (alumina,
                          colloidal silica, argon ion mill), and conductive coating
                          type and thickness. For VP-SEM/ESEM analyses, note whether
                          an uncoated sample was used and the gas type used. FIB-specific
                          in-session operations (protective coating deposition, milling
                          conditions, lamella preparation) are documented separately
                          in Group 4.
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
                          title: Constants and Reference Values Used
                          description: Physical constants and reference values used
                            in data reduction to calculate the final reported quantity
                            (e.g., decay constants for age calculation, standard isotope
                            ratios, or other citable reference values used in a correction
                            or calculation), together with their source. Distinct
                            from the Group 6 reference-material fields, which document
                            accepted values for specific calibration/validation materials
                            rather than universal physical constants. Record "None"
                            if no citable, revisable physical constants feed into
                            this procedure's data reduction.
                          type: object
                          properties:
                            '@id':
                              const: ada:parameter/semTAPP/constantsAndReferenceValuesUsed
                            '@type':
                              const:
                              - schema:PropertyValue
                            schema:propertyID:
                              const:
                              - '@id': ada:parameter/semTAPP/constantsAndReferenceValuesUsed
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
                            title: Constants and Reference Values Used
                            description: Physical constants and reference values used
                              in data reduction to calculate the final reported quantity
                              (e.g., decay constants for age calculation, standard
                              isotope ratios, or other citable reference values used
                              in a correction or calculation), together with their
                              source. Distinct from the Group 6 reference-material
                              fields, which document accepted values for specific
                              calibration/validation materials rather than universal
                              physical constants. Record "None" if no citable, revisable
                              physical constants feed into this procedure's data reduction.
                            type: object
                            properties:
                              '@id':
                                const: ada:parameter/semTAPP/constantsAndReferenceValuesUsed
                              '@type':
                                const:
                                - schema:PropertyValue
                              schema:propertyID:
                                const:
                                - '@id': ada:parameter/semTAPP/constantsAndReferenceValuesUsed
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
                  schema:additionalProperty:
                    type: array
                    items:
                      anyOf:
                      - title: Sample Persistent Identifier
                        description: Globally unique, persistent identifier for each
                          sample listed in Sample Name. IGSN (International Geo Sample
                          Number) is the recommended standard for geological and cosmochemical
                          samples, as used by Astromat, EarthChem and SESAR. Where
                          a sample and its sub-samples are separately registered,
                          record the identifier at the level actually analysed.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/semTAPP/samplePersistentIdentifier
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/semTAPP/samplePersistentIdentifier
                          schema:name:
                            const: Sample Persistent Identifier
                          schema:value:
                            type: string
                        required:
                        - '@id'
                        - '@type'
                        - schema:propertyID
                        - schema:name
                        - schema:value
                      - title: Pre-Analysis Imaging and Screening
                        description: Imaging or other characterisation performed before
                          the measurement in order to select or locate the analysed
                          target, including the technique, instrument and settings
                          used, and how individual analyses are linked back to the
                          images. Distinct from any imaging the procedure performs
                          as its own measurement. Where the imaging is performed on
                          a separate instrument, it should also be recorded in the
                          Group 1 coupling fields.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/semTAPP/preAnalysisImagingAndScreening
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/semTAPP/preAnalysisImagingAndScreening
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
                    allOf:
                    - contains:
                        title: Sample Persistent Identifier
                        description: Globally unique, persistent identifier for each
                          sample listed in Sample Name. IGSN (International Geo Sample
                          Number) is the recommended standard for geological and cosmochemical
                          samples, as used by Astromat, EarthChem and SESAR. Where
                          a sample and its sub-samples are separately registered,
                          record the identifier at the level actually analysed.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/semTAPP/samplePersistentIdentifier
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/semTAPP/samplePersistentIdentifier
                          schema:name:
                            const: Sample Persistent Identifier
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
                        description: Imaging or other characterisation performed before
                          the measurement in order to select or locate the analysed
                          target, including the technique, instrument and settings
                          used, and how individual analyses are linked back to the
                          images. Distinct from any imaging the procedure performs
                          as its own measurement. Where the imaging is performed on
                          a separate instrument, it should also be recorded in the
                          Group 1 coupling fields.
                        type: object
                        properties:
                          '@id':
                            const: ada:parameter/semTAPP/preAnalysisImagingAndScreening
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/semTAPP/preAnalysisImagingAndScreening
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
          allOf:
          - contains:
              properties:
                '@type':
                  contains:
                    const: https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample
              required:
              - '@type'
        prov:used:
          type: array
          items:
            type: object
            allOf:
            - if:
                required:
                - bios:computationalTool
              then:
                properties:
                  bios:computationalTool:
                    type: array
                    items:
                      allOf:
                      - $ref: https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/BaseSchema/geochemProduct/schema.yaml#/$defs/UsedComputationalTool
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
                                description: Software used to control the SEM and
                                  acquire data, including version number. For FIB-SEM
                                  3D tomography, include the automated slice-and-view
                                  module name and version.
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
                                description: Software used for post-acquisition data
                                  reduction and analysis. List all packages with version
                                  numbers.
                                anyOf:
                                - type: string
                                - type: array
                                  items:
                                    type: string
                        required:
                        - ada:toolRole
            - if:
                required:
                - schema:instrument
              then:
                properties:
                  schema:instrument:
                    type: array
                    items:
                      allOf:
                      - $ref: https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/BaseSchema/instrument/schema.yaml
                      - type: object
                        allOf:
                        - if:
                            properties:
                              schema:additionalType:
                                contains:
                                  const: SEM
                            required:
                            - schema:additionalType
                          then:
                            properties:
                              ada:acceleratingVoltage:
                                description: Electron beam accelerating voltage in
                                  kilovolts. Affects X-ray generation depth (EDS/WDS),
                                  EBSD pattern quality, imaging resolution, and beam
                                  penetration. Low voltages (1-5 kV) improve surface
                                  sensitivity and reduce beam damage; high voltages
                                  (15-20 kV) improve X-ray generation for quantitative
                                  analysis.
                                anyOf:
                                - type: number
                                - type: string
                              ada:beamDiameter:
                                description: Nominal electron beam diameter (spot
                                  size) at the sample surface, in nanometres or micrometres,
                                  as set by the condenser aperture and working distance.
                                  Controls the spatial resolution and X-ray excitation
                                  volume. For mapping modes, the effective spatial
                                  sampling interval is further defined by Step Size
                                  / Pixel Size.
                                anyOf:
                                - type: number
                                - type: string
                    allOf:
                    - contains:
                        properties:
                          schema:additionalType:
                            contains:
                              const: SEM
                        required:
                        - schema:additionalType
        schema:additionalProperty:
          type: array
          items:
            anyOf:
            - title: Beam Raster Dimensions
              description: "Dimensions of the small area over which the beam is rastered
                during a single analysis point, reported as width \xD7 height in \xB5m.
                Applicable when Beam Mode = Rastered; defines the effective spatial
                footprint of the measurement and distributes dose over a larger area
                to reduce beam damage on sensitive phases."
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
              required:
              - '@id'
              - '@type'
              - schema:propertyID
              - schema:name
              - schema:value
            - title: Beam Damage Minimization
              description: 'Describes any measures taken to reduce electron beam damage
                to the sample during analysis. Examples: reduced accelerating voltage,
                lowered beam current, defocused or rastered beam, cooled stage, short
                acquisition sequences, or rotating between multiple points. Particularly
                important for volatile-bearing phases, hydrous minerals, glasses,
                organic materials, and biological samples.'
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
            - title: Drift Correction
              description: 'Describes whether and how stage or beam drift was monitored
                and corrected during the measurement session. Examples: periodic stage
                realignment to a fiducial marker, automated beam drift correction
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
            - title: Dwell Time per Pixel
              description: Time the electron beam dwells on each pixel during raster
                scanning (imaging modes) or on each step position during compositional
                mapping (EDS and WDS mapping modes), in microseconds or milliseconds.
                Longer dwell time improves signal-to-noise and counting statistics
                but increases total dose and can cause beam damage or contamination
                on sensitive materials. For WDS mapping, the dwell time is per spectrometer
                per pixel.
              type: object
              properties:
                '@id':
                  const: ada:parameter/semTAPP/dwellTimePerPixel
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/semTAPP/dwellTimePerPixel
                schema:name:
                  const: Dwell Time per Pixel
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
            - title: Step Size / Pixel Size
              description: "Centre-to-centre distance between adjacent measurement
                points (WDS mapping) or pixels (EDS mapping) in \xB5m. Defines the
                spatial sampling interval of the map and, together with the pixel-grid
                dimensions, determines the total mapped area. Smaller step sizes increase
                spatial resolution but extend acquisition time."
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
              required:
              - '@id'
              - '@type'
              - schema:propertyID
              - schema:name
              - schema:value
            - title: Halogen Correction on Oxygen
              description: Whether oxygen content was adjusted to account for halogen
                substitution (F and/or Cl replacing OH) in halogen-bearing phases
                such as apatite, amphibole, and mica, where oxygen is calculated by
                stoichiometry.
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
                  const: ada:parameter/semTAPP/proceduralBlankLevel
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/semTAPP/proceduralBlankLevel
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
            - title: EDS Dead Time
              description: "Percent dead time reported by the EDS detector during
                the session \u2014 the fraction of total acquisition time the detector
                spent processing rather than counting. EDS dead time correction is
                managed automatically by the detector electronics; this field documents
                the resulting percentage as a session QC metric. Values above ~40%
                indicate excessive count rate and may degrade spectral quality and
                quantitative accuracy. Unlike WDS dead time (see WDS Dead Time Correction),
                no user-selectable correction algorithm is required."
              type: object
              properties:
                '@id':
                  const: ada:parameter/semTAPP/edsDeadTime
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/semTAPP/edsDeadTime
                schema:name:
                  const: EDS Dead Time
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
              title: Beam Raster Dimensions
              description: "Dimensions of the small area over which the beam is rastered
                during a single analysis point, reported as width \xD7 height in \xB5m.
                Applicable when Beam Mode = Rastered; defines the effective spatial
                footprint of the measurement and distributes dose over a larger area
                to reduce beam damage on sensitive phases."
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
              description: 'Describes any measures taken to reduce electron beam damage
                to the sample during analysis. Examples: reduced accelerating voltage,
                lowered beam current, defocused or rastered beam, cooled stage, short
                acquisition sequences, or rotating between multiple points. Particularly
                important for volatile-bearing phases, hydrous minerals, glasses,
                organic materials, and biological samples.'
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
              title: Drift Correction
              description: 'Describes whether and how stage or beam drift was monitored
                and corrected during the measurement session. Examples: periodic stage
                realignment to a fiducial marker, automated beam drift correction
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
              title: Dwell Time per Pixel
              description: Time the electron beam dwells on each pixel during raster
                scanning (imaging modes) or on each step position during compositional
                mapping (EDS and WDS mapping modes), in microseconds or milliseconds.
                Longer dwell time improves signal-to-noise and counting statistics
                but increases total dose and can cause beam damage or contamination
                on sensitive materials. For WDS mapping, the dwell time is per spectrometer
                per pixel.
              type: object
              properties:
                '@id':
                  const: ada:parameter/semTAPP/dwellTimePerPixel
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/semTAPP/dwellTimePerPixel
                schema:name:
                  const: Dwell Time per Pixel
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
              title: Step Size / Pixel Size
              description: "Centre-to-centre distance between adjacent measurement
                points (WDS mapping) or pixels (EDS mapping) in \xB5m. Defines the
                spatial sampling interval of the map and, together with the pixel-grid
                dimensions, determines the total mapped area. Smaller step sizes increase
                spatial resolution but extend acquisition time."
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
              required:
              - '@id'
              - '@type'
              - schema:propertyID
              - schema:name
              - schema:value
            minContains: 0
            maxContains: 1
          - contains:
              title: Halogen Correction on Oxygen
              description: Whether oxygen content was adjusted to account for halogen
                substitution (F and/or Cl replacing OH) in halogen-bearing phases
                such as apatite, amphibole, and mica, where oxygen is calculated by
                stoichiometry.
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
                  const: ada:parameter/semTAPP/proceduralBlankLevel
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/semTAPP/proceduralBlankLevel
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
              title: EDS Dead Time
              description: "Percent dead time reported by the EDS detector during
                the session \u2014 the fraction of total acquisition time the detector
                spent processing rather than counting. EDS dead time correction is
                managed automatically by the detector electronics; this field documents
                the resulting percentage as a session QC metric. Values above ~40%
                indicate excessive count rate and may degrade spectral quality and
                quantitative accuracy. Unlike WDS dead time (see WDS Dead Time Correction),
                no user-selectable correction algorithm is required."
              type: object
              properties:
                '@id':
                  const: ada:parameter/semTAPP/edsDeadTime
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/semTAPP/edsDeadTime
                schema:name:
                  const: EDS Dead Time
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
        ada:edsLiveTimePerPointOrPixel:
          description: EDS spectral acquisition live time per analysis point or per
            pixel in seconds. Longer live time improves counting statistics but increases
            beam damage risk and total acquisition time.
          anyOf:
          - type: number
          - type: string
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
          description: DOI or unique persistent identifier for the registered procedure
            used in this analysis, generated upon procedure submission to a data repository.
            This field is mandatory when submitting analytical data, to encourage
            formal procedure registration and ensure traceability. If a DOI has been
            applied for but not yet minted, enter "pending".
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
                    - EPMA; NanoSIMS
                    - XCT (pre-SEM overview)
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
                  description: Registered procedure DOI for the coupled technique
                    named above. Provides a stable, citable link to the companion
                    method independent of whether a dataset has been deposited. If
                    the coupled procedure has not yet been registered, enter the DOI
                    of a publication describing the coupled method, or "pending".
                    Enter "None" if no coupling is planned.
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
  schema:additionalProperty:
    type: array
    items:
      title: Map Area
      description: "Physical area covered by the map in \xB5m\xB2 or mm\xB2, calculated
        as (map width in pixels \xD7 step size) \xD7 (map height in pixels \xD7 step
        size). Complements the map's pixel-grid dimensions by recording the physical
        scale of the mapped region; useful for direct comparison across datasets acquired
        with different step sizes."
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
      required:
      - '@id'
      - '@type'
      - schema:propertyID
      - schema:name
      - schema:value
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
        required:
        - '@id'
        - '@type'
        - schema:propertyID
        - schema:name
        - schema:value
      minContains: 0
      maxContains: 1
  schema:variableMeasured:
    type: array
    items:
      anyOf:
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
      - title: Calibration Factor and Determination Method
        description: 'An externally-calibrated factor that converts the measured quantity
          into the reported quantity, how it was determined, and its uncertainty.
          Applies where the conversion depends on a factor calibrated against a reference
          of independently known value, rather than on the instrument response alone.
          Distinct from the fields that name the calibration material and that state
          which approach applies to which analyte, where the technique has them: this
          field records the resulting factor itself.'
        type: object
        properties:
          '@id':
            const: ada:parameter/semTAPP/calibrationFactorAndDeterminationMethod
          '@type':
            const:
            - schema:PropertyValue
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
        description: Method detection limit at 99% confidence, one per reported concentration
          variable (one per analyte, these being the same set). Include the method
          used and the resulting value for each.
        type: object
        properties:
          '@id':
            const: ada:parameter/semTAPP/detectionLimit
          '@type':
            const:
            - schema:PropertyValue
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
      - title: Goodness-of-Fit or Dispersion Statistic
        description: The statistic reported to show whether scatter among the contributing
          analyses exceeds what analytical uncertainty alone predicts, together with
          its value. Answers whether a reported aggregate is defensible as a single
          population. Procedure-level tier is N/A because the value cannot be known
          before the analysis; the procedure may still state an acceptance threshold,
          which belongs with the inclusion criteria.
        type: object
        properties:
          '@id':
            const: ada:parameter/semTAPP/goodnessOfFitOrDispersionStatistic
          '@type':
            const:
            - schema:PropertyValue
          schema:propertyID:
            const:
            - '@id': ada:parameter/semTAPP/goodnessOfFitOrDispersionStatistic
          schema:name:
            const: Goodness-of-Fit or Dispersion Statistic
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
            const: ada:parameter/semTAPP/normalizationStandardsBasedCorrection
          '@type':
            const:
            - schema:PropertyValue
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
    - contains:
        title: Calibration Factor and Determination Method
        description: 'An externally-calibrated factor that converts the measured quantity
          into the reported quantity, how it was determined, and its uncertainty.
          Applies where the conversion depends on a factor calibrated against a reference
          of independently known value, rather than on the instrument response alone.
          Distinct from the fields that name the calibration material and that state
          which approach applies to which analyte, where the technique has them: this
          field records the resulting factor itself.'
        type: object
        properties:
          '@id':
            const: ada:parameter/semTAPP/calibrationFactorAndDeterminationMethod
          '@type':
            const:
            - schema:PropertyValue
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
        description: Method detection limit at 99% confidence, one per reported concentration
          variable (one per analyte, these being the same set). Include the method
          used and the resulting value for each.
        type: object
        properties:
          '@id':
            const: ada:parameter/semTAPP/detectionLimit
          '@type':
            const:
            - schema:PropertyValue
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
        title: Goodness-of-Fit or Dispersion Statistic
        description: The statistic reported to show whether scatter among the contributing
          analyses exceeds what analytical uncertainty alone predicts, together with
          its value. Answers whether a reported aggregate is defensible as a single
          population. Procedure-level tier is N/A because the value cannot be known
          before the analysis; the procedure may still state an acceptance threshold,
          which belongs with the inclusion criteria.
        type: object
        properties:
          '@id':
            const: ada:parameter/semTAPP/goodnessOfFitOrDispersionStatistic
          '@type':
            const:
            - schema:PropertyValue
          schema:propertyID:
            const:
            - '@id': ada:parameter/semTAPP/goodnessOfFitOrDispersionStatistic
          schema:name:
            const: Goodness-of-Fit or Dispersion Statistic
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
- schema:funding

```

Links to the schema:

* YAML version: [schema.yaml](https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/detail/schema.json)
* JSON version: [schema.json](https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/detail/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "csvw": "http://www.w3.org/ns/csvw#",
    "prov": "http://www.w3.org/ns/prov#",
    "bios": "https://bioschemas.org/",
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
[context.jsonld](https://raw.githubusercontent.com/amds-ldeo/geochemBuildingBlocks/undefined/build/annotated/techniqueProfile/geochemProfile/SEM/detail/context.jsonld)

## Sources

* [SEM_TAPP_v4.xlsx (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/SEM/detail`

