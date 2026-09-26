
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
      "@id": "ex:empaTAPP-JEOL8200",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Chi Ma",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Tissint Mars meteorite",
  "ada:samplingUnitName": "Labelled at section level only: tissintite \"was identified in sections UT1, UT2 and UT3\" (p.2); Table 1 groups the point analyses by phase and setting (\"Wormy type tissintite\", \"Rimming tissintite\", \"Maskelynite away from melt pockets\" …) with counts (n = 6, 9, 17 …), not labels (p.5)",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially — the contributing counts are stated per aggregate, each Table 1 column being the mean of n point analyses of one phase and textural setting (n = 6, 6, 6, 9, 17, 7 and 5; p.5), with one standard deviation of the mean. No acceptance or rejection rule, and no acquired-versus-included count, is stated",
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
      "@id": "ex:empaTAPP-JEOL8200",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Chi Ma",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Tissint Mars meteorite",
  "ada:samplingUnitName": "Labelled at section level only: tissintite \"was identified in sections UT1, UT2 and UT3\" (p.2); Table 1 groups the point analyses by phase and setting (\"Wormy type tissintite\", \"Rimming tissintite\", \"Maskelynite away from melt pockets\" \u2026) with counts (n = 6, 9, 17 \u2026), not labels (p.5)",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially \u2014 the contributing counts are stated per aggregate, each Table 1 column being the mean of n point analyses of one phase and textural setting (n = 6, 6, 6, 9, 17, 7 and 5; p.5), with one standard deviation of the mean. No acceptance or rejection rule, and no acquired-versus-included count, is stated",
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
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-JEOL8200> a ada:EMPAImage ;
    schema1:measurementTechnique <ex:empaTAPP-JEOL8200> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially — the contributing counts are stated per aggregate, each Table 1 column being the mean of n point analyses of one phase and textural setting (n = 6, 6, 6, 9, 17, 7 and 5; p.5), with one standard deviation of the mean. No acceptance or rejection rule, and no acquired-versus-included count, is stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "Chi Ma" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:EMPAImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "K: 0.02 wt%; Cr: 0.05 wt%; Mn: 0.06 wt% (Table 1 footnote; other elements N)" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "Tissint Mars meteorite" ;
    ada:samplingUnitName "Labelled at section level only: tissintite \"was identified in sections UT1, UT2 and UT3\" (p.2); Table 1 groups the point analyses by phase and setting (\"Wormy type tissintite\", \"Rimming tissintite\", \"Maskelynite away from melt pockets\" …) with counts (n = 6, 9, 17 …), not labels (p.5)" ;
    ada:sessionIdentifier "missing" .

<ex:empaTAPP-JEOL8200> schema1:identifier "missing" .


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
      "@id": "ex:empaTAPP-P1",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Sen Hu",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "NWA 8657 shergottite",
  "ada:samplingUnitName": "Sample name only — \"a polished thick section of the martian meteorite NWA 8657\" (p.2), not otherwise labelled; analyses are grouped by phase (\"maskelynite, melt inclusion glasses, silica glasses, coesite aggregates, and mesostasis\", p.2)",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "N — analyses are reported by phase with no contributing count and no acceptance or rejection rule stated",
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
      "@id": "ex:empaTAPP-P1",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Sen Hu",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "NWA 8657 shergottite",
  "ada:samplingUnitName": "Sample name only \u2014 \"a polished thick section of the martian meteorite NWA 8657\" (p.2), not otherwise labelled; analyses are grouped by phase (\"maskelynite, melt inclusion glasses, silica glasses, coesite aggregates, and mesostasis\", p.2)",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 analyses are reported by phase with no contributing count and no acceptance or rejection rule stated",
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
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-P1> a ada:EMPAImage ;
    schema1:measurementTechnique <ex:empaTAPP-P1> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — analyses are reported by phase with no contributing count and no acceptance or rejection rule stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "Sen Hu" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:EMPAImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "K2O: 0.01 wt% (lowest); MnO: 0.06 wt% (highest); full per-element values stated in paper" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "NWA 8657 shergottite" ;
    ada:samplingUnitName "Sample name only — \"a polished thick section of the martian meteorite NWA 8657\" (p.2), not otherwise labelled; analyses are grouped by phase (\"maskelynite, melt inclusion glasses, silica glasses, coesite aggregates, and mesostasis\", p.2)" ;
    ada:sessionIdentifier "missing" .

<ex:empaTAPP-P1> schema1:identifier "missing" .


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
      "@id": "ex:empaTAPP-P2",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Tissint thin sections UT1, UT2, UT3; Tata-1-C1 to C3; Tata-2-C1 to C3; Tata-3-C1 to C3; Tissint-B",
  "ada:samplingUnitName": "Labelled at section level: X-ray maps are placed by thin section, e.g. an olivine megacryst \"in Tata-2-C3\" whose \"Red box outlines the area of X-ray maps\" (Fig. 3 caption, p.7); the sections are \"UT1 to UT3\" and \"Tata-1-C1 to C3, Tata-2-C1 to C3, and Tata-3-C1 to C3\" (pp.2–3). Map areas carry no labels of their own",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "N — the modal fractions use every pixel of the mapped section (\"the number of pixels attributed to each mineral was divided by the total number of pixels in the whole section\", p.3); nothing is admitted or excluded",
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
      "@id": "ex:empaTAPP-P2",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Tissint thin sections UT1, UT2, UT3; Tata-1-C1 to C3; Tata-2-C1 to C3; Tata-3-C1 to C3; Tissint-B",
  "ada:samplingUnitName": "Labelled at section level: X-ray maps are placed by thin section, e.g. an olivine megacryst \"in Tata-2-C3\" whose \"Red box outlines the area of X-ray maps\" (Fig. 3 caption, p.7); the sections are \"UT1 to UT3\" and \"Tata-1-C1 to C3, Tata-2-C1 to C3, and Tata-3-C1 to C3\" (pp.2\u20133). Map areas carry no labels of their own",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 the modal fractions use every pixel of the mapped section (\"the number of pixels attributed to each mineral was divided by the total number of pixels in the whole section\", p.3); nothing is admitted or excluded",
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
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-P2> a ada:EMPAImage ;
    schema1:measurementTechnique <ex:empaTAPP-P2> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — the modal fractions use every pixel of the mapped section (\"the number of pixels attributed to each mineral was divided by the total number of pixels in the whole section\", p.3); nothing is admitted or excluded" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:EMPAImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "<0.03 wt% for SiO2, TiO2, Al2O3, MgO, CaO; <0.05-0.1 wt% for FeO, MnO, Cr2O3, NiO, Na2O, K2O, P2O5 (stated as \"typical\")" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "Tissint thin sections UT1, UT2, UT3; Tata-1-C1 to C3; Tata-2-C1 to C3; Tata-3-C1 to C3; Tissint-B" ;
    ada:samplingUnitName "Labelled at section level: X-ray maps are placed by thin section, e.g. an olivine megacryst \"in Tata-2-C3\" whose \"Red box outlines the area of X-ray maps\" (Fig. 3 caption, p.7); the sections are \"UT1 to UT3\" and \"Tata-1-C1 to C3, Tata-2-C1 to C3, and Tata-3-C1 to C3\" (pp.2–3). Map areas carry no labels of their own" ;
    ada:sessionIdentifier "missing" .

<ex:empaTAPP-P2> schema1:identifier "missing" .


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
      "@id": "ex:empaTAPP-P3",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Tissint thin sections UT1, UT2, UT3; Tata-1-C1 to C3; Tata-2-C1 to C3; Tata-3-C1 to C3; Tissint-B",
  "ada:samplingUnitName": "Labelled: thin sections \"UT1 to UT3\" and \"Tata-1-C1 to C3, Tata-2-C1 to C3, and Tata-3-C1 to C3\" (pp.2–3), and pyroxene grains within a section, e.g. \"T-3-C2 px1\" to \"T-3-C2 px5\" (Fig. 8, p.12); individual point analyses are not labelled",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially — contributing counts are stated for the glass aggregates (\"EMP avg (n = 73)\" and \"avg (n = 14)\", Table 3, p.9) and for the mineral means (n = 7, n = 13, table p.9). No acceptance or rejection rule is stated; the plateau-region screening of each spot is a signal-based step recorded under Spike / Outlier Filtering Approach",
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
      "@id": "ex:empaTAPP-P3",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Tissint thin sections UT1, UT2, UT3; Tata-1-C1 to C3; Tata-2-C1 to C3; Tata-3-C1 to C3; Tissint-B",
  "ada:samplingUnitName": "Labelled: thin sections \"UT1 to UT3\" and \"Tata-1-C1 to C3, Tata-2-C1 to C3, and Tata-3-C1 to C3\" (pp.2\u20133), and pyroxene grains within a section, e.g. \"T-3-C2 px1\" to \"T-3-C2 px5\" (Fig. 8, p.12); individual point analyses are not labelled",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially \u2014 contributing counts are stated for the glass aggregates (\"EMP avg (n = 73)\" and \"avg (n = 14)\", Table 3, p.9) and for the mineral means (n = 7, n = 13, table p.9). No acceptance or rejection rule is stated; the plateau-region screening of each spot is a signal-based step recorded under Spike / Outlier Filtering Approach",
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
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-P3> a ada:EMPAImage ;
    schema1:measurementTechnique <ex:empaTAPP-P3> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially — contributing counts are stated for the glass aggregates (\"EMP avg (n = 73)\" and \"avg (n = 14)\", Table 3, p.9) and for the mineral means (n = 7, n = 13, table p.9). No acceptance or rejection rule is stated; the plateau-region screening of each spot is a signal-based step recorded under Spike / Outlier Filtering Approach" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:EMPAImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "<0.03 wt% for SiO2, TiO2, Al2O3, MgO, CaO; <0.05-0.1 wt% for FeO, MnO, Cr2O3, NiO, Na2O, K2O, P2O5 (stated as shared conditions with UT)" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "Tissint thin sections UT1, UT2, UT3; Tata-1-C1 to C3; Tata-2-C1 to C3; Tata-3-C1 to C3; Tissint-B" ;
    ada:samplingUnitName "Labelled: thin sections \"UT1 to UT3\" and \"Tata-1-C1 to C3, Tata-2-C1 to C3, and Tata-3-C1 to C3\" (pp.2–3), and pyroxene grains within a section, e.g. \"T-3-C2 px1\" to \"T-3-C2 px5\" (Fig. 8, p.12); individual point analyses are not labelled" ;
    ada:sessionIdentifier "missing" .

<ex:empaTAPP-P3> schema1:identifier "missing" .


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
      "@id": "ex:empaTAPP-JEOL8200-2",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Chi Ma",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Zagami USNM 7619",
  "ada:samplingUnitName": "Labelled at section level only: \"The Zagami thin section (USNM 7619)\" (p.3); occurrences are identified by figure panel (\"First occurrence of liebermannite\", Fig. 1, p.2), not by label",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially — each Table 1 column is the mean of n point analyses of one occurrence (n = 6, 2, 3, 3, 5 and 4; p.3), with one standard deviation of the mean. No acceptance or rejection rule is stated",
  "ada:detectionLimit": 0.05,
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
      "@id": "ex:empaTAPP-JEOL8200-2",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Chi Ma",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Zagami USNM 7619",
  "ada:samplingUnitName": "Labelled at section level only: \"The Zagami thin section (USNM 7619)\" (p.3); occurrences are identified by figure panel (\"First occurrence of liebermannite\", Fig. 1, p.2), not by label",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially \u2014 each Table 1 column is the mean of n point analyses of one occurrence (n = 6, 2, 3, 3, 5 and 4; p.3), with one standard deviation of the mean. No acceptance or rejection rule is stated",
  "ada:detectionLimit": 0.05,
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
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-JEOL8200-2> a ada:EMPAImage ;
    schema1:measurementTechnique <ex:empaTAPP-JEOL8200-2> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially — each Table 1 column is the mean of n point analyses of one occurrence (n = 6, 2, 3, 3, 5 and 4; p.3), with one standard deviation of the mean. No acceptance or rejection rule is stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "Chi Ma" ;
    ada:analyticalAccuracy "1-2% for Si, Al, Ca, Na, and K (based on feldspar standards run as unknowns)" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:EMPAImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit 5e-02 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "Zagami USNM 7619" ;
    ada:samplingUnitName "Labelled at section level only: \"The Zagami thin section (USNM 7619)\" (p.3); occurrences are identified by figure panel (\"First occurrence of liebermannite\", Fig. 1, p.2), not by label" ;
    ada:sessionIdentifier "missing" .

<ex:empaTAPP-JEOL8200-2> schema1:identifier "missing" .


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
      "@id": "ex:empaTAPP-P5",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "David R. Frank",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Ivuna CI chondrite, section MZ2",
  "ada:samplingUnitName": "Labelled at section level: the CAI \"in Ivuna section MZ2\" (p.3), in \"polished mount 'Ivuna MZ2'\" (p.14); the single CAI and its analysis points carry no labels",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "N — the microprobe analyses are reported as \"Representative electron-microprobe measurements\" (p.5) with no contributing count and no selection rule. The counts on p.8 (n = 9, n = 7) are SIMS standard populations, not microprobe aggregates",
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
      "@id": "ex:empaTAPP-P5",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "David R. Frank",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Ivuna CI chondrite, section MZ2",
  "ada:samplingUnitName": "Labelled at section level: the CAI \"in Ivuna section MZ2\" (p.3), in \"polished mount 'Ivuna MZ2'\" (p.14); the single CAI and its analysis points carry no labels",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 the microprobe analyses are reported as \"Representative electron-microprobe measurements\" (p.5) with no contributing count and no selection rule. The counts on p.8 (n = 9, n = 7) are SIMS standard populations, not microprobe aggregates",
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
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-P5> a ada:EMPAImage ;
    schema1:measurementTechnique <ex:empaTAPP-P5> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — the microprobe analyses are reported as \"Representative electron-microprobe measurements\" (p.5) with no contributing count and no selection rule. The counts on p.8 (n = 9, n = 7) are SIMS standard populations, not microprobe aggregates" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "David R. Frank" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:EMPAImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "Al2O3, K2O, CaO: 0.03-0.04 wt%; Na2O, MgO, SiO2, FeO, MnO: 0.05 wt%; P2O5, SO2, TiO2, V2O3, Cr2O3, NiO: 0.06-0.09 wt% (stated as \"typically\")" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "Ivuna CI chondrite, section MZ2" ;
    ada:samplingUnitName "Labelled at section level: the CAI \"in Ivuna section MZ2\" (p.3), in \"polished mount 'Ivuna MZ2'\" (p.14); the single CAI and its analysis points carry no labels" ;
    ada:sessionIdentifier "missing" .

<ex:empaTAPP-P5> schema1:identifier "missing" .


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
      "@id": "ex:empaTAPP-P6",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "OC002 LAB24-2 (10-11 fragments of Oued Chebeika 002)",
  "ada:samplingUnitName": "Labelled: \"OC002 LAB24-2 fragment 1\" and \"fragment 2\" (Figs 3–4, pp.6–7), and within fragment 1 \"lithic clast LC1\" (Figure S3 caption, p.17); map areas are otherwise unlabelled",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially — the carbonate compositions are means of stated counts (\"Dolomite contains 2.0 ± 0.4 wt% Fe and 3.0 ± 0.9 wt% Mn (n = 37)\"; \"Magnesite contains 14.5 ± 2.7 wt% Fe and 4.6 ± 2.5 wt % Mn (n = 23)\", p.5). No acceptance or rejection rule is stated",
  "ada:detectionLimit": -9999,
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
      "@id": "ex:empaTAPP-P6",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "OC002 LAB24-2 (10-11 fragments of Oued Chebeika 002)",
  "ada:samplingUnitName": "Labelled: \"OC002 LAB24-2 fragment 1\" and \"fragment 2\" (Figs 3\u20134, pp.6\u20137), and within fragment 1 \"lithic clast LC1\" (Figure S3 caption, p.17); map areas are otherwise unlabelled",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially \u2014 the carbonate compositions are means of stated counts (\"Dolomite contains 2.0 \u00b1 0.4 wt% Fe and 3.0 \u00b1 0.9 wt% Mn (n = 37)\"; \"Magnesite contains 14.5 \u00b1 2.7 wt% Fe and 4.6 \u00b1 2.5 wt % Mn (n = 23)\", p.5). No acceptance or rejection rule is stated",
  "ada:detectionLimit": -9999,
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
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-P6> a ada:EMPAImage ;
    schema1:measurementTechnique <ex:empaTAPP-P6> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially — the carbonate compositions are means of stated counts (\"Dolomite contains 2.0 ± 0.4 wt% Fe and 3.0 ± 0.9 wt% Mn (n = 37)\"; \"Magnesite contains 14.5 ± 2.7 wt% Fe and 4.6 ± 2.5 wt % Mn (n = 23)\", p.5). No acceptance or rejection rule is stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:EMPAImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "OC002 LAB24-2 (10-11 fragments of Oued Chebeika 002)" ;
    ada:samplingUnitName "Labelled: \"OC002 LAB24-2 fragment 1\" and \"fragment 2\" (Figs 3–4, pp.6–7), and within fragment 1 \"lithic clast LC1\" (Figure S3 caption, p.17); map areas are otherwise unlabelled" ;
    ada:sessionIdentifier "missing" .

<ex:empaTAPP-P6> schema1:identifier "missing" .


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
      "@id": "ex:empaTAPP-JEOL8530",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Logan B. Seifert",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "OREX-803079-0 and OREX-803080-0 (Bennu OSIRIS-REx samples)",
  "ada:samplingUnitName": "Labelled: apatite grains numbered within each particle — \"OREX-803166-0 … Ap. #1 Ap. #2 Ap. #3 Ap. #4\" (Table 1, p.7) — in particles \"OREX-803166-0, OREX-803169-0, and OREX-803173-0\" (p.3) from the mounts \"OREX-803079-0 and OREX-803080-0\" (p.2)",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "N — Table 1 reports one column per named apatite grain rather than an aggregate over results, and no acceptance or rejection rule is stated",
  "ada:detectionLimit": -9999,
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
      "@id": "ex:empaTAPP-JEOL8530",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Logan B. Seifert",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "OREX-803079-0 and OREX-803080-0 (Bennu OSIRIS-REx samples)",
  "ada:samplingUnitName": "Labelled: apatite grains numbered within each particle \u2014 \"OREX-803166-0 \u2026 Ap. #1 Ap. #2 Ap. #3 Ap. #4\" (Table 1, p.7) \u2014 in particles \"OREX-803166-0, OREX-803169-0, and OREX-803173-0\" (p.3) from the mounts \"OREX-803079-0 and OREX-803080-0\" (p.2)",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 Table 1 reports one column per named apatite grain rather than an aggregate over results, and no acceptance or rejection rule is stated",
  "ada:detectionLimit": -9999,
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
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-JEOL8530> a ada:EMPAImage ;
    schema1:measurementTechnique <ex:empaTAPP-JEOL8530> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — Table 1 reports one column per named apatite grain rather than an aggregate over results, and no acceptance or rejection rule is stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "Logan B. Seifert" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:EMPAImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "OREX-803079-0 and OREX-803080-0 (Bennu OSIRIS-REx samples)" ;
    ada:samplingUnitName "Labelled: apatite grains numbered within each particle — \"OREX-803166-0 … Ap. #1 Ap. #2 Ap. #3 Ap. #4\" (Table 1, p.7) — in particles \"OREX-803166-0, OREX-803169-0, and OREX-803173-0\" (p.3) from the mounts \"OREX-803079-0 and OREX-803080-0\" (p.2)" ;
    ada:sessionIdentifier "missing" .

<ex:empaTAPP-JEOL8530> schema1:identifier "missing" .


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
      "@id": "ex:empaTAPP-P8",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "NWA 8003 eucrite",
  "ada:samplingUnitName": "Sample name only — NWA 8003; grains are identified by setting (\"garnet grains within the eclogitic mineral assemblage\", p.4), and the point analyses are in \"Supplementary Table 4\" (p.4), not in the archived PDF",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially — the reported averages state their contributing counts (\"based on 12 analyses\" for orthopyroxene, and \"14 analyses\" for augite, p.2; \"based on 13 analyses\" and \"34 ± 7 mol% on average; 19 analyses\" for the Ca-Eskola component, p.4). No acceptance or rejection rule is stated",
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
      "@id": "ex:empaTAPP-P8",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "NWA 8003 eucrite",
  "ada:samplingUnitName": "Sample name only \u2014 NWA 8003; grains are identified by setting (\"garnet grains within the eclogitic mineral assemblage\", p.4), and the point analyses are in \"Supplementary Table 4\" (p.4), not in the archived PDF",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "Partially \u2014 the reported averages state their contributing counts (\"based on 12 analyses\" for orthopyroxene, and \"14 analyses\" for augite, p.2; \"based on 13 analyses\" and \"34 \u00b1 7 mol% on average; 19 analyses\" for the Ca-Eskola component, p.4). No acceptance or rejection rule is stated",
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
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-P8> a ada:EMPAImage ;
    schema1:measurementTechnique <ex:empaTAPP-P8> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially — the reported averages state their contributing counts (\"based on 12 analyses\" for orthopyroxene, and \"14 analyses\" for augite, p.2; \"based on 13 analyses\" and \"34 ± 7 mol% on average; 19 analyses\" for the Ca-Eskola component, p.4). No acceptance or rejection rule is stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:EMPAImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "Better than 0.02 wt% (as stated in paper)" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "NWA 8003 eucrite" ;
    ada:samplingUnitName "Sample name only — NWA 8003; grains are identified by setting (\"garnet grains within the eclogitic mineral assemblage\", p.4), and the point analyses are in \"Supplementary Table 4\" (p.4), not in the archived PDF" ;
    ada:sessionIdentifier "missing" .

<ex:empaTAPP-P8> schema1:identifier "missing" .


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
      "@id": "ex:empaTAPP-JEOL8530-2",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Bennu OSIRIS-REx samples (OREX-8#####-###)",
  "ada:samplingUnitName": "N — the Smithsonian microprobe passage names no specimens (\"conducted on Ir-coated specimens\", p.7); the paper's OREX numbers identify figure images, not microprobe analyses",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "N — compositions are reported by phase with no contributing count and no selection rule stated",
  "ada:detectionLimit": -9999,
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
      "@id": "ex:empaTAPP-JEOL8530-2",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Bennu OSIRIS-REx samples (OREX-8#####-###)",
  "ada:samplingUnitName": "N \u2014 the Smithsonian microprobe passage names no specimens (\"conducted on Ir-coated specimens\", p.7); the paper's OREX numbers identify figure images, not microprobe analyses",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 compositions are reported by phase with no contributing count and no selection rule stated",
  "ada:detectionLimit": -9999,
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
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-JEOL8530-2> a ada:EMPAImage ;
    schema1:measurementTechnique <ex:empaTAPP-JEOL8530-2> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — compositions are reported by phase with no contributing count and no selection rule stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:EMPAImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "Bennu OSIRIS-REx samples (OREX-8#####-###)" ;
    ada:samplingUnitName "N — the Smithsonian microprobe passage names no specimens (\"conducted on Ir-coated specimens\", p.7); the paper's OREX numbers identify figure images, not microprobe analyses" ;
    ada:sessionIdentifier "missing" .

<ex:empaTAPP-JEOL8530-2> schema1:identifier "missing" .


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
      "@id": "ex:empaTAPP-P10",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Bennu OSIRIS-REx samples (OREX-8#####-###)",
  "ada:samplingUnitName": "N — the Arizona microprobe passage names no specimen (\"the section was coated with a thin film of carbon\", p.7); the paper's OREX numbers identify figure images, not microprobe analyses",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "N — compositions are reported by phase with no contributing count and no selection rule stated",
  "ada:detectionLimit": -9999,
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
      "@id": "ex:empaTAPP-P10",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Bennu OSIRIS-REx samples (OREX-8#####-###)",
  "ada:samplingUnitName": "N \u2014 the Arizona microprobe passage names no specimen (\"the section was coated with a thin film of carbon\", p.7); the paper's OREX numbers identify figure images, not microprobe analyses",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 compositions are reported by phase with no contributing count and no selection rule stated",
  "ada:detectionLimit": -9999,
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
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-P10> a ada:EMPAImage ;
    schema1:measurementTechnique <ex:empaTAPP-P10> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — compositions are reported by phase with no contributing count and no selection rule stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:EMPAImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "Bennu OSIRIS-REx samples (OREX-8#####-###)" ;
    ada:samplingUnitName "N — the Arizona microprobe passage names no specimen (\"the section was coated with a thin film of carbon\", p.7); the paper's OREX numbers identify figure images, not microprobe analyses" ;
    ada:sessionIdentifier "missing" .

<ex:empaTAPP-P10> schema1:identifier "missing" .


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
      "@id": "ex:empaTAPP-P11",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Bennu OSIRIS-REx samples (OREX-5/8#####-###)",
  "ada:samplingUnitName": "Labelled by curation number per particle: \"EMPA data from Bennu particles\" (Fig. 1) cites \"OREX-803095-0\" and \"OREX-803096-0\", and sulfide compositions \"in samples OREX-803095-0, OREX-803096-0, OREX-803066-0, OREX-803067-0 and OREX-803070-0\" (p.2); points within particles are not labelled",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "N — no contributing count and no acceptance or rejection rule is stated for the microprobe analyses; the modal abundances come from classified phase-map pixels rather than from admitting or excluding results (p.9)",
  "ada:detectionLimit": -9999,
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
      "@id": "ex:empaTAPP-P11",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "Bennu OSIRIS-REx samples (OREX-5/8#####-###)",
  "ada:samplingUnitName": "Labelled by curation number per particle: \"EMPA data from Bennu particles\" (Fig. 1) cites \"OREX-803095-0\" and \"OREX-803096-0\", and sulfide compositions \"in samples OREX-803095-0, OREX-803096-0, OREX-803066-0, OREX-803067-0 and OREX-803070-0\" (p.2); points within particles are not labelled",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 no contributing count and no acceptance or rejection rule is stated for the microprobe analyses; the modal abundances come from classified phase-map pixels rather than from admitting or excluding results (p.9)",
  "ada:detectionLimit": -9999,
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
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-P11> a ada:EMPAImage ;
    schema1:measurementTechnique <ex:empaTAPP-P11> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — no contributing count and no acceptance or rejection rule is stated for the microprobe analyses; the modal abundances come from classified phase-map pixels rather than from admitting or excluding results (p.9)" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:EMPAImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "Bennu OSIRIS-REx samples (OREX-5/8#####-###)" ;
    ada:samplingUnitName "Labelled by curation number per particle: \"EMPA data from Bennu particles\" (Fig. 1) cites \"OREX-803095-0\" and \"OREX-803096-0\", and sulfide compositions \"in samples OREX-803095-0, OREX-803096-0, OREX-803066-0, OREX-803067-0 and OREX-803070-0\" (p.2); points within particles are not labelled" ;
    ada:sessionIdentifier "missing" .

<ex:empaTAPP-P11> schema1:identifier "missing" .


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
      "@id": "ex:empaTAPP-P12",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "OREX-800045-103 and OREX-800045-107",
  "ada:samplingUnitName": "Labelled at split level: \"Samples OREX-800045-103 and OREX-800045-107 ... Aggregate particles (<1 mm) were mounted in epoxy\" (p.11); particles and points are not labelled, and the data are \"compiled in Supplementary Table 14\" (p.11), not in the archived PDF",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "N — the analyses are \"compiled in Supplementary Table 14\" (p.11), not in the archived PDF, and no count or selection rule is stated in the text. The \"Bennu (n = 58)\" population (Fig. 5, p.6) is the SIMS oxygen-isotope dataset, not this procedure's",
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
      "@id": "ex:empaTAPP-P12",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "OREX-800045-103 and OREX-800045-107",
  "ada:samplingUnitName": "Labelled at split level: \"Samples OREX-800045-103 and OREX-800045-107 ... Aggregate particles (<1 mm) were mounted in epoxy\" (p.11); particles and points are not labelled, and the data are \"compiled in Supplementary Table 14\" (p.11), not in the archived PDF",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 the analyses are \"compiled in Supplementary Table 14\" (p.11), not in the archived PDF, and no count or selection rule is stated in the text. The \"Bennu (n = 58)\" population (Fig. 5, p.6) is the SIMS oxygen-isotope dataset, not this procedure's",
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
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-P12> a ada:EMPAImage ;
    schema1:measurementTechnique <ex:empaTAPP-P12> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — the analyses are \"compiled in Supplementary Table 14\" (p.11), not in the archived PDF, and no count or selection rule is stated in the text. The \"Bennu (n = 58)\" population (Fig. 5, p.6) is the SIMS oxygen-isotope dataset, not this procedure's" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:EMPAImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "Mg: 0.025 wt%; Fe: 0.025 wt%; Si: 0.05 wt%; K: 0.05 wt%; Na: 0.05 wt%; Ca: 0.005 wt%; Al: 0.02 wt%; Ti: 0.005 wt%; Cr: 0.015 wt%; Mn: 0.008 wt%" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "OREX-800045-103 and OREX-800045-107" ;
    ada:samplingUnitName "Labelled at split level: \"Samples OREX-800045-103 and OREX-800045-107 ... Aggregate particles (<1 mm) were mounted in epoxy\" (p.11); particles and points are not labelled, and the data are \"compiled in Supplementary Table 14\" (p.11), not in the archived PDF" ;
    ada:sessionIdentifier "missing" .

<ex:empaTAPP-P12> schema1:identifier "missing" .


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
      "@id": "ex:empaTAPP-P13",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "OREX-501054-0 and OREX-501059-0 (particles P1, P2)",
  "ada:samplingUnitName": "Labelled: \"The samples OREX-501054-0 and OREX-501059-0 ... fragmented into particles, identified as P1 and P2\" (p.13); the olivine and pyroxene grains within them are not labelled",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "N — no contributing count and no acceptance or rejection rule is stated for the olivine and pyroxene analyses",
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
      "@id": "ex:empaTAPP-P13",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "OREX-501054-0 and OREX-501059-0 (particles P1, P2)",
  "ada:samplingUnitName": "Labelled: \"The samples OREX-501054-0 and OREX-501059-0 ... fragmented into particles, identified as P1 and P2\" (p.13); the olivine and pyroxene grains within them are not labelled",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 no contributing count and no acceptance or rejection rule is stated for the olivine and pyroxene analyses",
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
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-P13> a ada:EMPAImage ;
    schema1:measurementTechnique <ex:empaTAPP-P13> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — no contributing count and no acceptance or rejection rule is stated for the olivine and pyroxene analyses" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:EMPAImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "Transition metals: ~250 ppm (stated as \"typical\")" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "OREX-501054-0 and OREX-501059-0 (particles P1, P2)" ;
    ada:samplingUnitName "Labelled: \"The samples OREX-501054-0 and OREX-501059-0 ... fragmented into particles, identified as P1 and P2\" (p.13); the olivine and pyroxene grains within them are not labelled" ;
    ada:sessionIdentifier "missing" .

<ex:empaTAPP-P13> schema1:identifier "missing" .


```


### detail example P14
detail instance derived from Neuman+2025 | WashU St. Louis | WDS Mapping (JEOL JXA-8200).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-P14",
  "@type": [
    "ada:EMPAImage"
  ],
  "ada:componentType": "ada:EMPAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:empaTAPP-P14",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "73001,6014-73001,6021",
  "ada:samplingUnitName": "Labelled at thin-section level: \"The 73001,6014–73001,6021 samples are 50 × 25 mm continuous thin sections\" (p.6), e.g. the \"73001,6019\" X-ray map (p.11); every map pixel is an analysis, so the section — the acquisition area — is the unit named",
  "ada:mapDimensions": 1,
  "ada:mapArea": "N - not stated directly (1,024 pixels at 9.5 um step corresponds to ~9.7 mm per side)",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": 0.1,
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
  "@id": "ex:detail-P14",
  "@type": [
    "ada:EMPAImage"
  ],
  "ada:componentType": "ada:EMPAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:empaTAPP-P14",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "missing",
  "ada:sampleName": "73001,6014-73001,6021",
  "ada:samplingUnitName": "Labelled at thin-section level: \"The 73001,6014\u201373001,6021 samples are 50 \u00d7 25 mm continuous thin sections\" (p.6), e.g. the \"73001,6019\" X-ray map (p.11); every map pixel is an analysis, so the section \u2014 the acquisition area \u2014 is the unit named",
  "ada:mapDimensions": 1,
  "ada:mapArea": "N - not stated directly (1,024 pixels at 9.5 um step corresponds to ~9.7 mm per side)",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": 0.1,
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
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-P14> a ada:EMPAImage ;
    schema1:measurementTechnique <ex:empaTAPP-P14> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:componentType "ada:EMPAImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit 1e-01 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "missing" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea "N - not stated directly (1,024 pixels at 9.5 um step corresponds to ~9.7 mm per side)" ;
    ada:mapDimensions 1 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "73001,6014-73001,6021" ;
    ada:samplingUnitName "Labelled at thin-section level: \"The 73001,6014–73001,6021 samples are 50 × 25 mm continuous thin sections\" (p.6), e.g. the \"73001,6019\" X-ray map (p.11); every map pixel is an analysis, so the section — the acquisition area — is the unit named" ;
    ada:sessionIdentifier "missing" .

<ex:empaTAPP-P14> schema1:identifier "missing" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: EPMA/EMPA Analysis Detail
description: Dataset-level analysis-instance detail for EPMA/EMPA, reusing CDIF/schema.org
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
                                        in kilovolts (kV). Justify any deviation from
                                        the standard operating voltage.
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
                                        in kilovolts (kV). Justify any deviation from
                                        the standard operating voltage.
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
                              schema:inDefinedTermSet: ada:vocab/instrumentType
                          required:
                          - schema:additionalType
          schema:additionalProperty:
            type: array
            items:
              anyOf:
              - title: Beam Damage Minimization
                description: Measures taken to minimize beam damage, particularly
                  volatilization or migration of Na, K, F, and Cl in hydrous minerals,
                  glasses, feldspars, phosphates, and carbonates. Document approach,
                  beam conditions used, and phases for which it was applied.
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
                description: "Dimensions of the small area over which the beam is
                  rastered at a single analysis point, reported as width \xD7 height
                  in \xB5m. Applicable when Beam Mode = Rastered; defines the effective
                  spatial footprint of the measurement. Not applicable when mapping."
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
              - title: EDS Live Time per Point or Pixel
                description: EDS spectral acquisition live time per analysis point
                  in seconds. Previously referred to as "EDS Acquisition Time" in
                  this TAPP and commonly used under that name in EPMA and SEM-EDS
                  contexts. Renamed to align with TEM-EDS usage, where the per-point
                  vs. per-pixel distinction (point/line mode vs. spectrum image) is
                  explicit. In EPMA, acquisition is always per point.
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
                  such as apatite, amphibole, and mica, where oxygen is calculated
                  by stoichiometry.
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
                  map in micrometers, defining the spatial resolution. Report both
                  X and Y step if they differ.
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
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_samplingUnitSelectionCriteria
            allOf:
            - contains:
                title: Beam Damage Minimization
                description: Measures taken to minimize beam damage, particularly
                  volatilization or migration of Na, K, F, and Cl in hydrous minerals,
                  glasses, feldspars, phosphates, and carbonates. Document approach,
                  beam conditions used, and phases for which it was applied.
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
                description: "Dimensions of the small area over which the beam is
                  rastered at a single analysis point, reported as width \xD7 height
                  in \xB5m. Applicable when Beam Mode = Rastered; defines the effective
                  spatial footprint of the measurement. Not applicable when mapping."
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
                title: EDS Live Time per Point or Pixel
                description: EDS spectral acquisition live time per analysis point
                  in seconds. Previously referred to as "EDS Acquisition Time" in
                  this TAPP and commonly used under that name in EPMA and SEM-EDS
                  contexts. Renamed to align with TEM-EDS usage, where the per-point
                  vs. per-pixel distinction (point/line mode vs. spectrum image) is
                  explicit. In EPMA, acquisition is always per point.
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
                  such as apatite, amphibole, and mica, where oxygen is calculated
                  by stoichiometry.
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
                  map in micrometers, defining the spatial resolution. Report both
                  X and Y step if they differ.
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
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_samplingUnitSelectionCriteria
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
                        $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_preAnalysisImagingAndScreening
                      allOf:
                      - contains:
                          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_preAnalysisImagingAndScreening
                        minContains: 0
                        maxContains: 1
          ada:deadTime:
            description: "Percent dead time reported by the EDS detector during the
              session \u2014 the fraction of total acquisition time the detector spent
              processing rather than counting. This field documents the resulting
              percentage as a session QC metric. Unlike WDS dead time (see WDS Dead
              Time Correction), no user-selectable correction algorithm is required."
            anyOf:
            - type: number
            - type: string
          ada:proceduralBlankLevel:
            description: "The measured level of the analytical blank in the session,
              and \u2014 where the reported quantity is a ratio \u2014 its composition,
              since a blank subtracted from a ratio biases the result unless its own
              composition is known. Companion to the blank correction method."
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
                          const: Data reduction
                      required:
                      - schema:name
                    then:
                      properties:
                        schema:additionalProperty:
                          type: array
                          items:
                            $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Analysis_constantsReferenceValues
                          allOf:
                          - contains:
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Analysis_constantsReferenceValues
                            minContains: 0
                            maxContains: 1
                allOf:
                - contains:
                    properties:
                      schema:name:
                        const: Data reduction
                    required:
                    - schema:name
        required:
        - ada:deadTime
        - ada:proceduralBlankLevel
        - schema:actionProcess
    schema:additionalProperty:
      type: array
      items:
        anyOf:
        - title: Map Area
          description: "Physical extent of the mapped region, given either as width
            \xD7 height in \xB5m or as a total area in \xB5m\xB2 or mm\xB2, and equal
            to (map width in pixels \xD7 step size) \xD7 (map height in pixels \xD7
            step size). Complements the map's pixel-grid dimensions by recording the
            physical scale of the mapped region."
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
            Based on the area of interest and selected step size.
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
          description: "Physical extent of the mapped region, given either as width
            \xD7 height in \xB5m or as a total area in \xB5m\xB2 or mm\xB2, and equal
            to (map width in pixels \xD7 step size) \xD7 (map height in pixels \xD7
            step size). Complements the map's pixel-grid dimensions by recording the
            physical scale of the mapped region."
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
            Based on the area of interest and selected step size.
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

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EMPA/detail/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EMPA/detail/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EMPA/detail/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/EMPA/detail`

