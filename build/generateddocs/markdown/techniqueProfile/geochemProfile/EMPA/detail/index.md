
# EMPA Instrument Detail (Schema)

`ogch.techniqueProfile.geochemProfile.EMPA.detail` *v0.1*

Electron Microprobe Analysis instrument-specific detail properties. Defines properties: @type, spectrometersUsed, signalUsed.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### detail example JEOL8200
detail instance derived from Ma+2015 | Caltech GPS | WDS Point Analysis (JEOL 8200).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-JEOL8200",
  "@type": [
    "ada:EMPAImage"
  ],
  "ada:componentType": "ada:EMPAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:empaTAPP-JEOL8200"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Chi Ma",
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
  "ada:sampleName": "Tissint Mars meteorite",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "K: 0.02 wt%; Cr: 0.05 wt%; Mn: 0.06 wt% (Table 1 footnote; other elements N)",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EMPA/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-JEOL8200",
  "@type": [
    "ada:EMPAImage"
  ],
  "ada:componentType": "ada:EMPAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:empaTAPP-JEOL8200"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Chi Ma",
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
  "ada:sampleName": "Tissint Mars meteorite",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "K: 0.02 wt%; Cr: 0.05 wt%; Mn: 0.06 wt% (Table 1 footnote; other elements N)",
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

ex:detail-JEOL8200 a ada:EMPAImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:empaTAPP-JEOL8200 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "Chi Ma" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:EMPAImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "K: 0.02 wt%; Cr: 0.05 wt%; Mn: 0.06 wt% (Table 1 footnote; other elements N)" ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "Tissint Mars meteorite" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


```


### detail example P1
detail instance derived from Hu+2020 | IGGCAS | WDS Point Analysis (JEOL JXA-8100).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-P1",
  "@type": [
    "ada:EMPAImage"
  ],
  "ada:componentType": "ada:EMPAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:empaTAPP-P1"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Sen Hu",
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
  "ada:sampleName": "NWA 8657 shergottite",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "K2O: 0.01 wt% (lowest); MnO: 0.06 wt% (highest); full per-element values stated in paper",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EMPA/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-P1",
  "@type": [
    "ada:EMPAImage"
  ],
  "ada:componentType": "ada:EMPAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:empaTAPP-P1"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Sen Hu",
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
  "ada:sampleName": "NWA 8657 shergottite",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "K2O: 0.01 wt% (lowest); MnO: 0.06 wt% (highest); full per-element values stated in paper",
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

ex:detail-P1 a ada:EMPAImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:empaTAPP-P1 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "Sen Hu" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:EMPAImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "K2O: 0.01 wt% (lowest); MnO: 0.06 wt% (highest); full per-element values stated in paper" ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "NWA 8657 shergottite" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


```


### detail example P2
detail instance derived from Liu+2016_UT | Cameca SX100 | WDS Mapping (U.Tennessee).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-P2",
  "@type": [
    "ada:EMPAImage"
  ],
  "ada:componentType": "ada:EMPAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:empaTAPP-P2"
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
  "ada:sampleName": "Tissint thin sections UT1, UT2, UT3; Tata-1-C1 to C3; Tata-2-C1 to C3; Tata-3-C1 to C3; Tissint-B",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "<0.03 wt% for SiO2, TiO2, Al2O3, MgO, CaO; <0.05-0.1 wt% for FeO, MnO, Cr2O3, NiO, Na2O, K2O, P2O5 (stated as \"typical\")",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EMPA/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-P2",
  "@type": [
    "ada:EMPAImage"
  ],
  "ada:componentType": "ada:EMPAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:empaTAPP-P2"
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
  "ada:sampleName": "Tissint thin sections UT1, UT2, UT3; Tata-1-C1 to C3; Tata-2-C1 to C3; Tata-3-C1 to C3; Tissint-B",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "<0.03 wt% for SiO2, TiO2, Al2O3, MgO, CaO; <0.05-0.1 wt% for FeO, MnO, Cr2O3, NiO, Na2O, K2O, P2O5 (stated as \"typical\")",
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

ex:detail-P2 a ada:EMPAImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:empaTAPP-P2 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:EMPAImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "<0.03 wt% for SiO2, TiO2, Al2O3, MgO, CaO; <0.05-0.1 wt% for FeO, MnO, Cr2O3, NiO, Na2O, K2O, P2O5 (stated as \"typical\")" ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "Tissint thin sections UT1, UT2, UT3; Tata-1-C1 to C3; Tata-2-C1 to C3; Tata-3-C1 to C3; Tissint-B" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


```


### detail example P3
detail instance derived from Liu+2016_Cal | JEOL JXA-8200 | WDS Point Analysis (Caltech GPS).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-P3",
  "@type": [
    "ada:EMPAImage"
  ],
  "ada:componentType": "ada:EMPAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:empaTAPP-P3"
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
  "ada:sampleName": "Tissint thin sections UT1, UT2, UT3; Tata-1-C1 to C3; Tata-2-C1 to C3; Tata-3-C1 to C3; Tissint-B",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "<0.03 wt% for SiO2, TiO2, Al2O3, MgO, CaO; <0.05-0.1 wt% for FeO, MnO, Cr2O3, NiO, Na2O, K2O, P2O5 (stated as shared conditions with UT)",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EMPA/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-P3",
  "@type": [
    "ada:EMPAImage"
  ],
  "ada:componentType": "ada:EMPAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:empaTAPP-P3"
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
  "ada:sampleName": "Tissint thin sections UT1, UT2, UT3; Tata-1-C1 to C3; Tata-2-C1 to C3; Tata-3-C1 to C3; Tissint-B",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "<0.03 wt% for SiO2, TiO2, Al2O3, MgO, CaO; <0.05-0.1 wt% for FeO, MnO, Cr2O3, NiO, Na2O, K2O, P2O5 (stated as shared conditions with UT)",
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

ex:detail-P3 a ada:EMPAImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:empaTAPP-P3 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:EMPAImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "<0.03 wt% for SiO2, TiO2, Al2O3, MgO, CaO; <0.05-0.1 wt% for FeO, MnO, Cr2O3, NiO, Na2O, K2O, P2O5 (stated as shared conditions with UT)" ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "Tissint thin sections UT1, UT2, UT3; Tata-1-C1 to C3; Tata-2-C1 to C3; Tata-3-C1 to C3; Tissint-B" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


```


### detail example JEOL8200-2
detail instance derived from Ma+2017 | JEOL 8200 | WDS Point Analysis (Caltech GPS Analytical Facility).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-JEOL8200-2",
  "@type": [
    "ada:EMPAImage"
  ],
  "ada:componentType": "ada:EMPAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:empaTAPP-JEOL8200-2"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Chi Ma",
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
  "ada:sampleName": "Zagami USNM 7619",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "0.05 Si, 0.04 Ti, 0.06 Al, 0.06 Fe, 0.02 Mg, 0.02 Ca, 0.03 Na, 0.02 K, 0.05 Cr, 0.06 Mn (all wt%)",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "1-2% for Si, Al, Ca, Na, and K (based on feldspar standards run as unknowns)",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EMPA/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-JEOL8200-2",
  "@type": [
    "ada:EMPAImage"
  ],
  "ada:componentType": "ada:EMPAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:empaTAPP-JEOL8200-2"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Chi Ma",
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
  "ada:sampleName": "Zagami USNM 7619",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "0.05 Si, 0.04 Ti, 0.06 Al, 0.06 Fe, 0.02 Mg, 0.02 Ca, 0.03 Na, 0.02 K, 0.05 Cr, 0.06 Mn (all wt%)",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "1-2% for Si, Al, Ca, Na, and K (based on feldspar standards run as unknowns)",
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

ex:detail-JEOL8200-2 a ada:EMPAImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:empaTAPP-JEOL8200-2 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "Chi Ma" ;
    ada:analyticalAccuracy "1-2% for Si, Al, Ca, Na, and K (based on feldspar standards run as unknowns)" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:EMPAImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "0.05 Si, 0.04 Ti, 0.06 Al, 0.06 Fe, 0.02 Mg, 0.02 Ca, 0.03 Na, 0.02 K, 0.05 Cr, 0.06 Mn (all wt%)" ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "Zagami USNM 7619" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


```


### detail example P5
detail instance derived from Frank+2023 | Cameca SX100 | WDS Point Analysis (ARES JSC).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-P5",
  "@type": [
    "ada:EMPAImage"
  ],
  "ada:componentType": "ada:EMPAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:empaTAPP-P5"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "David R. Frank",
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
  "ada:sampleName": "Ivuna CI chondrite, section MZ2",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "Al2O3, K2O, CaO: 0.03-0.04 wt%; Na2O, MgO, SiO2, FeO, MnO: 0.05 wt%; P2O5, SO2, TiO2, V2O3, Cr2O3, NiO: 0.06-0.09 wt% (stated as \"typically\")",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EMPA/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-P5",
  "@type": [
    "ada:EMPAImage"
  ],
  "ada:componentType": "ada:EMPAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:empaTAPP-P5"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "David R. Frank",
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
  "ada:sampleName": "Ivuna CI chondrite, section MZ2",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "Al2O3, K2O, CaO: 0.03-0.04 wt%; Na2O, MgO, SiO2, FeO, MnO: 0.05 wt%; P2O5, SO2, TiO2, V2O3, Cr2O3, NiO: 0.06-0.09 wt% (stated as \"typically\")",
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

ex:detail-P5 a ada:EMPAImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:empaTAPP-P5 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "David R. Frank" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:EMPAImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "Al2O3, K2O, CaO: 0.03-0.04 wt%; Na2O, MgO, SiO2, FeO, MnO: 0.05 wt%; P2O5, SO2, TiO2, V2O3, Cr2O3, NiO: 0.06-0.09 wt% (stated as \"typically\")" ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "Ivuna CI chondrite, section MZ2" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


```


### detail example P6
detail instance derived from Broussard+2026 | JEOL JXA-8200 | WDS Mapping (WashU).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-P6",
  "@type": [
    "ada:EMPAImage"
  ],
  "ada:componentType": "ada:EMPAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:empaTAPP-P6"
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
  "ada:sampleName": "OC002 LAB24-2 (10-11 fragments of Oued Chebeika 002)",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EMPA/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-P6",
  "@type": [
    "ada:EMPAImage"
  ],
  "ada:componentType": "ada:EMPAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:empaTAPP-P6"
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
  "ada:sampleName": "OC002 LAB24-2 (10-11 fragments of Oued Chebeika 002)",
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

ex:detail-P6 a ada:EMPAImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:empaTAPP-P6 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:EMPAImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "OC002 LAB24-2 (10-11 fragments of Oued Chebeika 002)" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


```


### detail example JEOL8530
detail instance derived from Seifert+2026 | JEOL 8530 | WDS Point Analysis (ARES JSC).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-JEOL8530",
  "@type": [
    "ada:EMPAImage"
  ],
  "ada:componentType": "ada:EMPAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:empaTAPP-JEOL8530"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Logan B. Seifert",
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
  "ada:sampleName": "OREX-803079-0 and OREX-803080-0 (Bennu OSIRIS-REx samples)",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EMPA/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-JEOL8530",
  "@type": [
    "ada:EMPAImage"
  ],
  "ada:componentType": "ada:EMPAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:empaTAPP-JEOL8530"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Logan B. Seifert",
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
  "ada:sampleName": "OREX-803079-0 and OREX-803080-0 (Bennu OSIRIS-REx samples)",
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

ex:detail-JEOL8530 a ada:EMPAImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:empaTAPP-JEOL8530 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "Logan B. Seifert" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:EMPAImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "OREX-803079-0 and OREX-803080-0 (Bennu OSIRIS-REx samples)" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


```


### detail example P8
detail instance derived from Pang+2016 | JEOL JXA-8100 | WDS Point Analysis (Nanjing U.).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-P8",
  "@type": [
    "ada:EMPAImage"
  ],
  "ada:componentType": "ada:EMPAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:empaTAPP-P8"
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
  "ada:sampleName": "NWA 8003 eucrite",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "Better than 0.02 wt% (as stated in paper)",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EMPA/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-P8",
  "@type": [
    "ada:EMPAImage"
  ],
  "ada:componentType": "ada:EMPAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:empaTAPP-P8"
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
  "ada:sampleName": "NWA 8003 eucrite",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "Better than 0.02 wt% (as stated in paper)",
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

ex:detail-P8 a ada:EMPAImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:empaTAPP-P8 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:EMPAImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "Better than 0.02 wt% (as stated in paper)" ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "NWA 8003 eucrite" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


```


### detail example JEOL8530-2
detail instance derived from McCoy+2025_SI | JEOL 8530F+ | WDS Point Analysis (Smithsonian).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-JEOL8530-2",
  "@type": [
    "ada:EMPAImage"
  ],
  "ada:componentType": "ada:EMPAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:empaTAPP-JEOL8530-2"
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
  "ada:sampleName": "Bennu OSIRIS-REx samples (OREX-8#####-###)",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EMPA/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-JEOL8530-2",
  "@type": [
    "ada:EMPAImage"
  ],
  "ada:componentType": "ada:EMPAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:empaTAPP-JEOL8530-2"
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
  "ada:sampleName": "Bennu OSIRIS-REx samples (OREX-8#####-###)",
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

ex:detail-JEOL8530-2 a ada:EMPAImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:empaTAPP-JEOL8530-2 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:EMPAImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "Bennu OSIRIS-REx samples (OREX-8#####-###)" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


```


### detail example P10
detail instance derived from McCoy+2025_UA | Cameca SX-100 | WDS Point Analysis (K-ALFAA U.Arizona).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-P10",
  "@type": [
    "ada:EMPAImage"
  ],
  "ada:componentType": "ada:EMPAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:empaTAPP-P10"
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
  "ada:sampleName": "Bennu OSIRIS-REx samples (OREX-8#####-###)",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EMPA/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-P10",
  "@type": [
    "ada:EMPAImage"
  ],
  "ada:componentType": "ada:EMPAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:empaTAPP-P10"
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
  "ada:sampleName": "Bennu OSIRIS-REx samples (OREX-8#####-###)",
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

ex:detail-P10 a ada:EMPAImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:empaTAPP-P10 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:EMPAImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "Bennu OSIRIS-REx samples (OREX-8#####-###)" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


```


### detail example P11
detail instance derived from Zega+2025 | Cameca SX-100 Ultra | WDS Point Analysis (K-ALFAA U.Arizona).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-P11",
  "@type": [
    "ada:EMPAImage"
  ],
  "ada:componentType": "ada:EMPAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:empaTAPP-P11"
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
  "ada:sampleName": "Bennu OSIRIS-REx samples (OREX-5/8#####-###)",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EMPA/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-P11",
  "@type": [
    "ada:EMPAImage"
  ],
  "ada:componentType": "ada:EMPAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:empaTAPP-P11"
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
  "ada:sampleName": "Bennu OSIRIS-REx samples (OREX-5/8#####-###)",
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

ex:detail-P11 a ada:EMPAImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:empaTAPP-P11 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:EMPAImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "missing" ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "Bennu OSIRIS-REx samples (OREX-5/8#####-###)" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


```


### detail example P12
detail instance derived from Barnes+2025 | JEOL JXA-8230 | WDS Point Analysis (CRPG Nancy).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-P12",
  "@type": [
    "ada:EMPAImage"
  ],
  "ada:componentType": "ada:EMPAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:empaTAPP-P12"
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
  "ada:sampleName": "OREX-800045-103 and OREX-800045-107",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "Mg: 0.025 wt%; Fe: 0.025 wt%; Si: 0.05 wt%; K: 0.05 wt%; Na: 0.05 wt%; Ca: 0.005 wt%; Al: 0.02 wt%; Ti: 0.005 wt%; Cr: 0.015 wt%; Mn: 0.008 wt%",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EMPA/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-P12",
  "@type": [
    "ada:EMPAImage"
  ],
  "ada:componentType": "ada:EMPAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:empaTAPP-P12"
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
  "ada:sampleName": "OREX-800045-103 and OREX-800045-107",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "Mg: 0.025 wt%; Fe: 0.025 wt%; Si: 0.05 wt%; K: 0.05 wt%; Na: 0.05 wt%; Ca: 0.005 wt%; Al: 0.02 wt%; Ti: 0.005 wt%; Cr: 0.015 wt%; Mn: 0.008 wt%",
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

ex:detail-P12 a ada:EMPAImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:empaTAPP-P12 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:EMPAImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "Mg: 0.025 wt%; Fe: 0.025 wt%; Si: 0.05 wt%; K: 0.05 wt%; Na: 0.05 wt%; Ca: 0.005 wt%; Al: 0.02 wt%; Ti: 0.005 wt%; Cr: 0.015 wt%; Mn: 0.008 wt%" ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "OREX-800045-103 and OREX-800045-107" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


```


### detail example P13
detail instance derived from Barnes+2025 | Cameca SX100 | WDS Point Analysis (NHM London).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-P13",
  "@type": [
    "ada:EMPAImage"
  ],
  "ada:componentType": "ada:EMPAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:empaTAPP-P13"
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
  "ada:sampleName": "OREX-501054-0 and OREX-501059-0 (particles P1, P2)",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "Transition metals: ~250 ppm (stated as \"typical\")",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EMPA/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-P13",
  "@type": [
    "ada:EMPAImage"
  ],
  "ada:componentType": "ada:EMPAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:empaTAPP-P13"
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
  "ada:sampleName": "OREX-501054-0 and OREX-501059-0 (particles P1, P2)",
  "ada:samplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": "Transition metals: ~250 ppm (stated as \"typical\")",
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

ex:detail-P13 a ada:EMPAImage ;
    schema1:funding [ a schema1:MonetaryGrant ;
            schema1:name "missing" ] ;
    schema1:measurementTechnique ex:empaTAPP-P13 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:EMPAImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "Transition metals: ~250 ppm (stated as \"typical\")" ;
    ada:edsDeadTime -9999 ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "OREX-501054-0 and OREX-501059-0 (particles P1, P2)" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: EPMA/EMPA Analysis Detail
description: Dataset-level analysis-instance detail for EPMA/EMPA, reusing CDIF/schema.org
  slots on the schema:Dataset root.
type: object
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
                                  const: EPMA
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
                                      in kilovolts (kV). The procedure specifies the
                                      standard operating voltage; analysts record
                                      and justify any deviations.
                                    type: object
                                    properties:
                                      '@id':
                                        const: ada:parameter/empaTAPP/acceleratingVoltage
                                      '@type':
                                        const:
                                        - schema:PropertyValue
                                      schema:propertyID:
                                        const:
                                        - '@id': ada:parameter/empaTAPP/acceleratingVoltage
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
                                    description: Diameter of the electron beam in
                                      micrometers. 0 indicates a fully focused beam.
                                      Document defocused diameter when used to minimize
                                      beam damage or improve spatial averaging for
                                      beam-sensitive phases.
                                    type: object
                                    properties:
                                      '@id':
                                        const: ada:parameter/empaTAPP/beamDiameter
                                      '@type':
                                        const:
                                        - schema:PropertyValue
                                      schema:propertyID:
                                        const:
                                        - '@id': ada:parameter/empaTAPP/beamDiameter
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
                                      in kilovolts (kV). The procedure specifies the
                                      standard operating voltage; analysts record
                                      and justify any deviations.
                                    type: object
                                    properties:
                                      '@id':
                                        const: ada:parameter/empaTAPP/acceleratingVoltage
                                      '@type':
                                        const:
                                        - schema:PropertyValue
                                      schema:propertyID:
                                        const:
                                        - '@id': ada:parameter/empaTAPP/acceleratingVoltage
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
                                    description: Diameter of the electron beam in
                                      micrometers. 0 indicates a fully focused beam.
                                      Document defocused diameter when used to minimize
                                      beam damage or improve spatial averaging for
                                      beam-sensitive phases.
                                    type: object
                                    properties:
                                      '@id':
                                        const: ada:parameter/empaTAPP/beamDiameter
                                      '@type':
                                        const:
                                        - schema:PropertyValue
                                      schema:propertyID:
                                        const:
                                        - '@id': ada:parameter/empaTAPP/beamDiameter
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
                              const: EPMA
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
                                description: Instrument control, automation and data
                                  acquisition software used to collect the raw data,
                                  including version number. Distinct from Data Processing
                                  Software(s), which covers everything applied to
                                  the data after acquisition.
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
                                description: All software applied to the data after
                                  acquisition in order to produce the reported quantities,
                                  including version numbers. List every package used.
                                  Distinct from Acquisition Software, which controls
                                  the instrument and collects the raw data.
                                anyOf:
                                - type: string
                                - type: array
                                  items:
                                    type: string
                        required:
                        - ada:toolRole
        schema:description:
          description: "Any procedure- or analysis-specific information not captured
            by a structured field anywhere in this TAPP \u2014 including anomalies,
            deviations from the registered procedure, instrument modifications, and
            supplementary context. Scope is the whole document, not Group 6: this
            is the last field of the TAPP and covers all six groups. Use sparingly;
            a structured field is preferred for anything that can be formally categorised."
          type: string
        schema:endDate:
          description: 'Date on which the analytical session ended. May equal Analysis
            Start Date for single-day sessions. Format: YYYY-MM-DD.'
          type: string
        schema:startDate:
          description: 'Date on which the analytical session began. For sessions spanning
            multiple days, use the date of the first session. Format: YYYY-MM-DD.'
          type: string
        schema:additionalProperty:
          type: array
          items:
            anyOf:
            - title: Beam Damage Minimization
              description: Measures taken to minimize beam damage, particularly volatilization
                or migration of Na, K, F, and Cl in hydrous minerals, glasses, feldspars,
                phosphates, and carbonates. Document approach, beam conditions used,
                and phases for which it was applied.
              type: object
              properties:
                '@id':
                  const: ada:parameter/empaTAPP/beamDamageMinimization
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/empaTAPP/beamDamageMinimization
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
              description: X x Y dimensions of a small beam raster used at a single
                analysis point to average a coarse-grained or beam-sensitive phase.
                Different from X-ray mapping mode; not applicable when mapping.
              type: object
              properties:
                '@id':
                  const: ada:parameter/empaTAPP/beamRasterDimensions
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/empaTAPP/beamRasterDimensions
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
            - title: Drift Correction
              description: Method used to monitor and correct for instrument drift
                (beam current drift, spectrometer drift) during the analytical session.
              type: object
              properties:
                '@id':
                  const: ada:parameter/empaTAPP/driftCorrection
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/empaTAPP/driftCorrection
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
              description: 'Time spent acquiring X-ray signal at each pixel during
                X-ray mapping, in milliseconds. For WDS: one value per spectrometer
                assignment per pixel. For EDS: total live-time per spectrum per pixel,
                a single value.'
              type: object
              properties:
                '@id':
                  const: ada:parameter/empaTAPP/dwellTimePerPixel
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/empaTAPP/dwellTimePerPixel
                schema:name:
                  const: Dwell Time per Pixel
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
              description: EDS spectral acquisition live time per analysis point in
                seconds. Previously referred to as "EDS Acquisition Time" in this
                TAPP and commonly used under that name in EPMA and SEM-EDS contexts.
                Renamed to align with TEM-EDS usage, where the per-point vs. per-pixel
                distinction (point/line mode vs. spectrum image) is explicit. In EPMA,
                acquisition is always per point.
              type: object
              properties:
                '@id':
                  const: ada:parameter/empaTAPP/edsLiveTimePerPointOrPixel
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/empaTAPP/edsLiveTimePerPointOrPixel
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
                such as apatite, amphibole, and mica, where oxygen is calculated by
                stoichiometry.
              type: object
              properties:
                '@id':
                  const: ada:parameter/empaTAPP/halogenCorrectionOnOxygen
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/empaTAPP/halogenCorrectionOnOxygen
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
            - title: Step Size / Pixel Size
              description: Distance between adjacent measurement points in the X-ray
                map in micrometers, defining the spatial resolution. Report both X
                and Y step if they differ.
              type: object
              properties:
                '@id':
                  const: ada:parameter/empaTAPP/stepSizePixelSize
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/empaTAPP/stepSizePixelSize
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
                  const: ada:parameter/empaTAPP/targetSelectionCriteria
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/empaTAPP/targetSelectionCriteria
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
                  const: ada:parameter/empaTAPP/proceduralBlankLevel
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/empaTAPP/proceduralBlankLevel
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
          allOf:
          - contains:
              title: Beam Damage Minimization
              description: Measures taken to minimize beam damage, particularly volatilization
                or migration of Na, K, F, and Cl in hydrous minerals, glasses, feldspars,
                phosphates, and carbonates. Document approach, beam conditions used,
                and phases for which it was applied.
              type: object
              properties:
                '@id':
                  const: ada:parameter/empaTAPP/beamDamageMinimization
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/empaTAPP/beamDamageMinimization
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
              description: X x Y dimensions of a small beam raster used at a single
                analysis point to average a coarse-grained or beam-sensitive phase.
                Different from X-ray mapping mode; not applicable when mapping.
              type: object
              properties:
                '@id':
                  const: ada:parameter/empaTAPP/beamRasterDimensions
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/empaTAPP/beamRasterDimensions
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
              title: Drift Correction
              description: Method used to monitor and correct for instrument drift
                (beam current drift, spectrometer drift) during the analytical session.
              type: object
              properties:
                '@id':
                  const: ada:parameter/empaTAPP/driftCorrection
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/empaTAPP/driftCorrection
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
              description: 'Time spent acquiring X-ray signal at each pixel during
                X-ray mapping, in milliseconds. For WDS: one value per spectrometer
                assignment per pixel. For EDS: total live-time per spectrum per pixel,
                a single value.'
              type: object
              properties:
                '@id':
                  const: ada:parameter/empaTAPP/dwellTimePerPixel
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/empaTAPP/dwellTimePerPixel
                schema:name:
                  const: Dwell Time per Pixel
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
              description: EDS spectral acquisition live time per analysis point in
                seconds. Previously referred to as "EDS Acquisition Time" in this
                TAPP and commonly used under that name in EPMA and SEM-EDS contexts.
                Renamed to align with TEM-EDS usage, where the per-point vs. per-pixel
                distinction (point/line mode vs. spectrum image) is explicit. In EPMA,
                acquisition is always per point.
              type: object
              properties:
                '@id':
                  const: ada:parameter/empaTAPP/edsLiveTimePerPointOrPixel
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/empaTAPP/edsLiveTimePerPointOrPixel
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
                such as apatite, amphibole, and mica, where oxygen is calculated by
                stoichiometry.
              type: object
              properties:
                '@id':
                  const: ada:parameter/empaTAPP/halogenCorrectionOnOxygen
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/empaTAPP/halogenCorrectionOnOxygen
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
              title: Step Size / Pixel Size
              description: Distance between adjacent measurement points in the X-ray
                map in micrometers, defining the spatial resolution. Report both X
                and Y step if they differ.
              type: object
              properties:
                '@id':
                  const: ada:parameter/empaTAPP/stepSizePixelSize
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/empaTAPP/stepSizePixelSize
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
                  const: ada:parameter/empaTAPP/targetSelectionCriteria
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/empaTAPP/targetSelectionCriteria
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
                  const: ada:parameter/empaTAPP/proceduralBlankLevel
                '@type':
                  const:
                  - schema:PropertyValue
                schema:propertyID:
                  const:
                  - '@id': ada:parameter/empaTAPP/proceduralBlankLevel
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
                      title: Pre-Analysis Imaging and Screening
                      description: Imaging or other characterisation performed before
                        the measurement in order to select or locate the analysed
                        target, including the technique, instrument and settings used,
                        and how individual analyses are linked back to the images.
                        Distinct from any imaging the procedure performs as its own
                        measurement. Where the imaging is performed on a separate
                        instrument, it should also be recorded in the Group 1 coupling
                        fields.
                      type: object
                      properties:
                        '@id':
                          const: ada:parameter/empaTAPP/preAnalysisImagingAndScreening
                        '@type':
                          const:
                          - schema:PropertyValue
                        schema:propertyID:
                          const:
                          - '@id': ada:parameter/empaTAPP/preAnalysisImagingAndScreening
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
                            const: ada:parameter/empaTAPP/preAnalysisImagingAndScreening
                          '@type':
                            const:
                            - schema:PropertyValue
                          schema:propertyID:
                            const:
                            - '@id': ada:parameter/empaTAPP/preAnalysisImagingAndScreening
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
        schema:location:
          type: object
          properties:
            schema:name:
              description: Name of the laboratory or institution hosting the instrument.
              type: string
            schema:identifier:
              description: Persistent identifier for the laboratory (e.g., ROR ID).
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
                        description: Description of how samples were prepared for
                          analysis under this procedure (mounting, polishing, coating).
                          Analysts may document session-specific variations from the
                          procedure standard.
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
                                const: ada:parameter/empaTAPP/calibrationFactorAndDeterminationMethod
                              '@type':
                                const:
                                - schema:PropertyValue
                              schema:propertyID:
                                const:
                                - '@id': ada:parameter/empaTAPP/calibrationFactorAndDeterminationMethod
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
                          - title: Constants and Reference Values Used
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
                                const: ada:parameter/empaTAPP/constantsAndReferenceValuesUsed
                              '@type':
                                const:
                                - schema:PropertyValue
                              schema:propertyID:
                                const:
                                - '@id': ada:parameter/empaTAPP/constantsAndReferenceValuesUsed
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
                                const: ada:parameter/empaTAPP/calibrationFactorAndDeterminationMethod
                              '@type':
                                const:
                                - schema:PropertyValue
                              schema:propertyID:
                                const:
                                - '@id': ada:parameter/empaTAPP/calibrationFactorAndDeterminationMethod
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
                                const: ada:parameter/empaTAPP/constantsAndReferenceValuesUsed
                              '@type':
                                const:
                                - schema:PropertyValue
                              schema:propertyID:
                                const:
                                - '@id': ada:parameter/empaTAPP/constantsAndReferenceValuesUsed
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
        ada:deadTime:
          description: "Percent dead time reported by the EDS detector during the
            session \u2014 the fraction of total acquisition time the detector spent
            processing rather than counting. EDS dead time correction is managed automatically
            by the detector electronics; this field documents the resulting percentage
            as a session QC metric. Values above ~40% indicate excessive count rate
            and may degrade spectral quality and quantitative accuracy. Unlike WDS
            dead time (see WDS Dead Time Correction), no user-selectable correction
            algorithm is required."
          anyOf:
          - type: number
          - type: string
        schema:identifier:
          description: "Identifier for the analytical session this record describes
            \u2014 the laboratory's own run, sequence or batch identifier as generated
            by the instrument or acquisition software. The analysis record corresponds
            to one session, which may cover several samples, and this is the link
            back to the raw instrument files. Distinct from any persistent identifier
            a repository mints on submission."
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
  schema:relatedLink:
    type: array
    items:
      type: object
      allOf:
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
                    - EBSD
                    - SEM-EDS
                    - NanoSIMS
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
  schema:funding:
    type: array
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
            const: ada:parameter/empaTAPP/normalizationStandardsBasedCorrection
          '@type':
            const:
            - schema:PropertyValue
          schema:propertyID:
            const:
            - '@id': ada:parameter/empaTAPP/normalizationStandardsBasedCorrection
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
            const: ada:parameter/empaTAPP/calibrationFactorAndDeterminationMethod
          '@type':
            const:
            - schema:PropertyValue
          schema:propertyID:
            const:
            - '@id': ada:parameter/empaTAPP/calibrationFactorAndDeterminationMethod
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
            const: ada:parameter/empaTAPP/goodnessOfFitOrDispersionStatistic
          '@type':
            const:
            - schema:PropertyValue
          schema:propertyID:
            const:
            - '@id': ada:parameter/empaTAPP/goodnessOfFitOrDispersionStatistic
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
            const: ada:parameter/empaTAPP/normalizationStandardsBasedCorrection
          '@type':
            const:
            - schema:PropertyValue
          schema:propertyID:
            const:
            - '@id': ada:parameter/empaTAPP/normalizationStandardsBasedCorrection
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
            const: ada:parameter/empaTAPP/calibrationFactorAndDeterminationMethod
          '@type':
            const:
            - schema:PropertyValue
          schema:propertyID:
            const:
            - '@id': ada:parameter/empaTAPP/calibrationFactorAndDeterminationMethod
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
            const: ada:parameter/empaTAPP/goodnessOfFitOrDispersionStatistic
          '@type':
            const:
            - schema:PropertyValue
          schema:propertyID:
            const:
            - '@id': ada:parameter/empaTAPP/goodnessOfFitOrDispersionStatistic
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
  schema:additionalProperty:
    type: array
    items:
      anyOf:
      - title: Map Area
        description: Physical dimensions of the mapped region in micrometers (X x
          Y). Determined at analysis time based on the sample feature or region of
          interest.
        type: object
        properties:
          '@id':
            const: ada:parameter/empaTAPP/mapArea
          '@type':
            const:
            - schema:PropertyValue
          schema:propertyID:
            const:
            - '@id': ada:parameter/empaTAPP/mapArea
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
      - title: Map Dimensions
        description: Number of pixels in the X-ray map in the X and Y directions.
          Determined at analysis time based on the area of interest and selected step
          size.
        type: object
        properties:
          '@id':
            const: ada:parameter/empaTAPP/mapDimensions
          '@type':
            const:
            - schema:PropertyValue
          schema:propertyID:
            const:
            - '@id': ada:parameter/empaTAPP/mapDimensions
          schema:name:
            const: Map Dimensions
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
        description: Physical dimensions of the mapped region in micrometers (X x
          Y). Determined at analysis time based on the sample feature or region of
          interest.
        type: object
        properties:
          '@id':
            const: ada:parameter/empaTAPP/mapArea
          '@type':
            const:
            - schema:PropertyValue
          schema:propertyID:
            const:
            - '@id': ada:parameter/empaTAPP/mapArea
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
    - contains:
        title: Map Dimensions
        description: Number of pixels in the X-ray map in the X and Y directions.
          Determined at analysis time based on the area of interest and selected step
          size.
        type: object
        properties:
          '@id':
            const: ada:parameter/empaTAPP/mapDimensions
          '@type':
            const:
            - schema:PropertyValue
          schema:propertyID:
            const:
            - '@id': ada:parameter/empaTAPP/mapDimensions
          schema:name:
            const: Map Dimensions
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
  dqv:hasQualityMeasurement:
    type: array
    items:
      type: object
      allOf:
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
            const: Goodness-of-Fit
        required:
        - dqv:isMeasurementOf
required:
- schema:funding

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EMPA/detail/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EMPA/detail/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EMPA/detail/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/EMPA/detail`

