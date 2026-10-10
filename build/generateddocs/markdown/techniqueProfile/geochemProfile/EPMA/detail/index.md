
# EPMA Instrument Detail (Schema)

`ogch.techniqueProfile.geochemProfile.EPMA.detail` *v0.1*

Electron Microprobe Analysis instrument-specific detail properties. Defines properties: @type, spectrometersUsed, signalUsed.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### detail example Ma2015
detail instance derived from Ma+2015 | Caltech GPS | WDS Point Analysis (JEOL 8200).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Ma2015",
  "@type": [
    "ada:EPMAImage"
  ],
  "ada:componentType": "ada:EPMAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:epmaTAPP-Ma2015",
      "schema:identifier": "test value schema:identifier"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Chi Ma",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "DOE Cooperative Agreement DE-NA0001982; NSF EAR 322082; NASA NNN13D465T; NASA Cosmochemistry NNX11AG58G and NNX12AH63G; NSF EAR 1344942 and 1440005 — acknowledged author by author for the study as a whole; none is attributed to the microprobe work",
  "ada:sampleName": "Tissint Mars meteorite",
  "ada:samplingUnitName": "Labelled at section level only: tissintite \"was identified in sections UT1, UT2 and UT3\" (p.2); Table 1 groups the point analyses by phase and setting (\"Wormy type tissintite\", \"Rimming tissintite\", \"Maskelynite away from melt pockets\" …) with counts (n = 6, 9, 17 …), not labels (p.5)",
  "ada:targetMaterialOfSamplingUnit": "each unit is named by its material: tissintite (wormy, rimming), maskelynite (three settings), pigeonite, fayalite — Table 1",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "Partially — the contributing counts are stated per aggregate, each Table 1 column being the mean of n point analyses of one phase and textural setting (n = 6, 6, 6, 9, 17, 7 and 5; p.5), with one standard deviation of the mean. No acceptance or rejection rule, and no acquired-versus-included count, is stated",
  "ada:combinedResults": "wormy type tissintite (n = 6); maskelynite associated with wormy tissintite (n = 6); rimming tissintite (n = 6); maskelynite associated with rimming tissintite (n = 9); maskelynite away from melt pockets (n = 17); pigeonite surrounding tissintite (n = 7); fayalite surrounding tissintite (n = 5) — the columns of Table 1",
  "ada:detectionLimit": "K2O: 0.02 wt% K; Cr2O3: 0.05 wt% Cr; MnO: 0.06 wt% Mn; other: N — Table 1 footnote c, attached to the b.d. entries of the K2O, Cr2O3 and MnO rows: 'b.d. = below detection limit: 0.02 wt% K, 0.05 wt% Cr, 0.06 wt% Mn'",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "SiO2, TiO2, Al2O3, FeO, MgO, CaO, Na2O, K2O, Cr2O3, MnO: one standard deviation of the mean; other: N — Table 1 note b: 'Errors given inside parentheses are one standard deviation of the mean based on all of the analyses'"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Ma2015",
  "@type": [
    "ada:EPMAImage"
  ],
  "ada:componentType": "ada:EPMAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:epmaTAPP-Ma2015",
      "schema:identifier": "test value schema:identifier"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Chi Ma",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "DOE Cooperative Agreement DE-NA0001982; NSF EAR 322082; NASA NNN13D465T; NASA Cosmochemistry NNX11AG58G and NNX12AH63G; NSF EAR 1344942 and 1440005 \u2014 acknowledged author by author for the study as a whole; none is attributed to the microprobe work",
  "ada:sampleName": "Tissint Mars meteorite",
  "ada:samplingUnitName": "Labelled at section level only: tissintite \"was identified in sections UT1, UT2 and UT3\" (p.2); Table 1 groups the point analyses by phase and setting (\"Wormy type tissintite\", \"Rimming tissintite\", \"Maskelynite away from melt pockets\" \u2026) with counts (n = 6, 9, 17 \u2026), not labels (p.5)",
  "ada:targetMaterialOfSamplingUnit": "each unit is named by its material: tissintite (wormy, rimming), maskelynite (three settings), pigeonite, fayalite \u2014 Table 1",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "Partially \u2014 the contributing counts are stated per aggregate, each Table 1 column being the mean of n point analyses of one phase and textural setting (n = 6, 6, 6, 9, 17, 7 and 5; p.5), with one standard deviation of the mean. No acceptance or rejection rule, and no acquired-versus-included count, is stated",
  "ada:combinedResults": "wormy type tissintite (n = 6); maskelynite associated with wormy tissintite (n = 6); rimming tissintite (n = 6); maskelynite associated with rimming tissintite (n = 9); maskelynite away from melt pockets (n = 17); pigeonite surrounding tissintite (n = 7); fayalite surrounding tissintite (n = 5) \u2014 the columns of Table 1",
  "ada:detectionLimit": "K2O: 0.02 wt% K; Cr2O3: 0.05 wt% Cr; MnO: 0.06 wt% Mn; other: N \u2014 Table 1 footnote c, attached to the b.d. entries of the K2O, Cr2O3 and MnO rows: 'b.d. = below detection limit: 0.02 wt% K, 0.05 wt% Cr, 0.06 wt% Mn'",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "SiO2, TiO2, Al2O3, FeO, MgO, CaO, Na2O, K2O, Cr2O3, MnO: one standard deviation of the mean; other: N \u2014 Table 1 note b: 'Errors given inside parentheses are one standard deviation of the mean based on all of the analyses'"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Ma2015> a ada:EPMAImage ;
    schema1:measurementTechnique <ex:epmaTAPP-Ma2015> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially — the contributing counts are stated per aggregate, each Table 1 column being the mean of n point analyses of one phase and textural setting (n = 6, 6, 6, 9, 17, 7 and 5; p.5), with one standard deviation of the mean. No acceptance or rejection rule, and no acquired-versus-included count, is stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "Chi Ma" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "wormy type tissintite (n = 6); maskelynite associated with wormy tissintite (n = 6); rimming tissintite (n = 6); maskelynite associated with rimming tissintite (n = 9); maskelynite away from melt pockets (n = 17); pigeonite surrounding tissintite (n = 7); fayalite surrounding tissintite (n = 5) — the columns of Table 1" ;
    ada:componentType "ada:EPMAImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "K2O: 0.02 wt% K; Cr2O3: 0.05 wt% Cr; MnO: 0.06 wt% Mn; other: N — Table 1 footnote c, attached to the b.d. entries of the K2O, Cr2O3 and MnO rows: 'b.d. = below detection limit: 0.02 wt% K, 0.05 wt% Cr, 0.06 wt% Mn'" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "DOE Cooperative Agreement DE-NA0001982; NSF EAR 322082; NASA NNN13D465T; NASA Cosmochemistry NNX11AG58G and NNX12AH63G; NSF EAR 1344942 and 1440005 — acknowledged author by author for the study as a whole; none is attributed to the microprobe work" ;
    ada:goodnessOfFitOrDispersionStatistic "SiO2, TiO2, Al2O3, FeO, MgO, CaO, Na2O, K2O, Cr2O3, MnO: one standard deviation of the mean; other: N — Table 1 note b: 'Errors given inside parentheses are one standard deviation of the mean based on all of the analyses'" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "Tissint Mars meteorite" ;
    ada:samplingUnitName "Labelled at section level only: tissintite \"was identified in sections UT1, UT2 and UT3\" (p.2); Table 1 groups the point analyses by phase and setting (\"Wormy type tissintite\", \"Rimming tissintite\", \"Maskelynite away from melt pockets\" …) with counts (n = 6, 9, 17 …), not labels (p.5)" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "each unit is named by its material: tissintite (wormy, rimming), maskelynite (three settings), pigeonite, fayalite — Table 1" .

<ex:epmaTAPP-Ma2015> schema1:identifier "test value schema:identifier" .


```


### detail example Hu2020
detail instance derived from Hu+2020 | IGGCAS | WDS Point Analysis (JEOL JXA-8100).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Hu2020",
  "@type": [
    "ada:EPMAImage"
  ],
  "ada:componentType": "ada:EPMAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:epmaTAPP-Hu2020",
      "schema:identifier": "test value schema:identifier"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Sen Hu",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NSFC 41573057, 41430105 and 41973062; China Scholarship Council 201804910284; IGGCAS key research program IGGCAS-201905 — 'This study was financially supported by ...'",
  "ada:sampleName": "NWA 8657 shergottite",
  "ada:samplingUnitName": "Sample name only — \"a polished thick section of the martian meteorite NWA 8657\" (p.2), not otherwise labelled; analyses are grouped by phase (\"maskelynite, melt inclusion glasses, silica glasses, coesite aggregates, and mesostasis\", p.2)",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N — analyses are reported by phase with no contributing count and no acceptance or rejection rule stated",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": "K2O: 0.01 wt%; SiO2, Al2O3, MgO, CaO, Na2O: 0.02 wt%; TiO2, Cr2O3: 0.03 wt%; FeO: 0.05 wt%; MnO: 0.06 wt% — p.2",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Hu2020",
  "@type": [
    "ada:EPMAImage"
  ],
  "ada:componentType": "ada:EPMAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:epmaTAPP-Hu2020",
      "schema:identifier": "test value schema:identifier"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Sen Hu",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NSFC 41573057, 41430105 and 41973062; China Scholarship Council 201804910284; IGGCAS key research program IGGCAS-201905 \u2014 'This study was financially supported by ...'",
  "ada:sampleName": "NWA 8657 shergottite",
  "ada:samplingUnitName": "Sample name only \u2014 \"a polished thick section of the martian meteorite NWA 8657\" (p.2), not otherwise labelled; analyses are grouped by phase (\"maskelynite, melt inclusion glasses, silica glasses, coesite aggregates, and mesostasis\", p.2)",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 analyses are reported by phase with no contributing count and no acceptance or rejection rule stated",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": "K2O: 0.01 wt%; SiO2, Al2O3, MgO, CaO, Na2O: 0.02 wt%; TiO2, Cr2O3: 0.03 wt%; FeO: 0.05 wt%; MnO: 0.06 wt% \u2014 p.2",
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

<ex:detail-Hu2020> a ada:EPMAImage ;
    schema1:measurementTechnique <ex:epmaTAPP-Hu2020> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — analyses are reported by phase with no contributing count and no acceptance or rejection rule stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "Sen Hu" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "missing" ;
    ada:componentType "ada:EPMAImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "K2O: 0.01 wt%; SiO2, Al2O3, MgO, CaO, Na2O: 0.02 wt%; TiO2, Cr2O3: 0.03 wt%; FeO: 0.05 wt%; MnO: 0.06 wt% — p.2" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NSFC 41573057, 41430105 and 41973062; China Scholarship Council 201804910284; IGGCAS key research program IGGCAS-201905 — 'This study was financially supported by ...'" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "NWA 8657 shergottite" ;
    ada:samplingUnitName "Sample name only — \"a polished thick section of the martian meteorite NWA 8657\" (p.2), not otherwise labelled; analyses are grouped by phase (\"maskelynite, melt inclusion glasses, silica glasses, coesite aggregates, and mesostasis\", p.2)" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" .

<ex:epmaTAPP-Hu2020> schema1:identifier "test value schema:identifier" .


```


### detail example Liu2016
detail instance derived from Liu+2016_UT | Cameca SX100 | WDS Mapping (U.Tennessee).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Liu2016",
  "@type": [
    "ada:EPMAImage"
  ],
  "ada:componentType": "ada:EPMAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:epmaTAPP-Liu2016",
      "schema:identifier": "test value schema:identifier"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA Cosmochemistry NNX11AG58G and NNN13D465T; NSF EAR-1226270; NSF EAR-1019770 — 'We acknowledge partial support by ...'",
  "ada:sampleName": "Tissint thin sections UT1, UT2, UT3; Tata-1-C1 to C3; Tata-2-C1 to C3; Tata-3-C1 to C3; Tissint-B",
  "ada:samplingUnitName": "Labelled at section level: X-ray maps are placed by thin section, e.g. an olivine megacryst \"in Tata-2-C3\" whose \"Red box outlines the area of X-ray maps\" (Fig. 3 caption, p.7); the sections are \"UT1 to UT3\" and \"Tata-1-C1 to C3, Tata-2-C1 to C3, and Tata-3-C1 to C3\" (pp.2–3). Map areas carry no labels of their own",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N — the modal fractions use every pixel of the mapped section (\"the number of pixels attributed to each mineral was divided by the total number of pixels in the whole section\", p.3); nothing is admitted or excluded",
  "ada:combinedResults": "glass inclusion average (n = 73); impact-melt glass average (n = 14) — Table 3: 'Glass inclusion EMP avg (n = 73) 1σ' and the impact-melt 'avg (n = 14) 1σ', whose average 'only included the glassy regions of the impact melt pockets'",
  "ada:detectionLimit": "SiO2, TiO2, Al2O3, MgO, CaO: <0.03 wt%; FeO, MnO, Cr2O3, NiO, Na2O, K2O, P2O5: <0.05–0.1 wt%; other: N — 'Detection limits are typically <0.03 wt% for SiO2, TiO2, Al2O3, MgO, and CaO; <0.05–0.1 wt% for FeO, MnO, Cr2O3, NiO, Na2O, K2O, and P2O5' (p.3)",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "SiO2, TiO2, Al2O3, Cr2O3, MgO, CaO, MnO, FeO, NiO, Na2O, K2O, P2O5: 1σ, one standard deviation of the average; other: N — Table 3 note b: '1σ is 1 standard deviation of the average'"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Liu2016",
  "@type": [
    "ada:EPMAImage"
  ],
  "ada:componentType": "ada:EPMAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:epmaTAPP-Liu2016",
      "schema:identifier": "test value schema:identifier"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA Cosmochemistry NNX11AG58G and NNN13D465T; NSF EAR-1226270; NSF EAR-1019770 \u2014 'We acknowledge partial support by ...'",
  "ada:sampleName": "Tissint thin sections UT1, UT2, UT3; Tata-1-C1 to C3; Tata-2-C1 to C3; Tata-3-C1 to C3; Tissint-B",
  "ada:samplingUnitName": "Labelled at section level: X-ray maps are placed by thin section, e.g. an olivine megacryst \"in Tata-2-C3\" whose \"Red box outlines the area of X-ray maps\" (Fig. 3 caption, p.7); the sections are \"UT1 to UT3\" and \"Tata-1-C1 to C3, Tata-2-C1 to C3, and Tata-3-C1 to C3\" (pp.2\u20133). Map areas carry no labels of their own",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 the modal fractions use every pixel of the mapped section (\"the number of pixels attributed to each mineral was divided by the total number of pixels in the whole section\", p.3); nothing is admitted or excluded",
  "ada:combinedResults": "glass inclusion average (n = 73); impact-melt glass average (n = 14) \u2014 Table 3: 'Glass inclusion EMP avg (n = 73) 1\u03c3' and the impact-melt 'avg (n = 14) 1\u03c3', whose average 'only included the glassy regions of the impact melt pockets'",
  "ada:detectionLimit": "SiO2, TiO2, Al2O3, MgO, CaO: <0.03 wt%; FeO, MnO, Cr2O3, NiO, Na2O, K2O, P2O5: <0.05\u20130.1 wt%; other: N \u2014 'Detection limits are typically <0.03 wt% for SiO2, TiO2, Al2O3, MgO, and CaO; <0.05\u20130.1 wt% for FeO, MnO, Cr2O3, NiO, Na2O, K2O, and P2O5' (p.3)",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "SiO2, TiO2, Al2O3, Cr2O3, MgO, CaO, MnO, FeO, NiO, Na2O, K2O, P2O5: 1\u03c3, one standard deviation of the average; other: N \u2014 Table 3 note b: '1\u03c3 is 1 standard deviation of the average'"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Liu2016> a ada:EPMAImage ;
    schema1:measurementTechnique <ex:epmaTAPP-Liu2016> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — the modal fractions use every pixel of the mapped section (\"the number of pixels attributed to each mineral was divided by the total number of pixels in the whole section\", p.3); nothing is admitted or excluded" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "glass inclusion average (n = 73); impact-melt glass average (n = 14) — Table 3: 'Glass inclusion EMP avg (n = 73) 1σ' and the impact-melt 'avg (n = 14) 1σ', whose average 'only included the glassy regions of the impact melt pockets'" ;
    ada:componentType "ada:EPMAImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "SiO2, TiO2, Al2O3, MgO, CaO: <0.03 wt%; FeO, MnO, Cr2O3, NiO, Na2O, K2O, P2O5: <0.05–0.1 wt%; other: N — 'Detection limits are typically <0.03 wt% for SiO2, TiO2, Al2O3, MgO, and CaO; <0.05–0.1 wt% for FeO, MnO, Cr2O3, NiO, Na2O, K2O, and P2O5' (p.3)" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA Cosmochemistry NNX11AG58G and NNN13D465T; NSF EAR-1226270; NSF EAR-1019770 — 'We acknowledge partial support by ...'" ;
    ada:goodnessOfFitOrDispersionStatistic "SiO2, TiO2, Al2O3, Cr2O3, MgO, CaO, MnO, FeO, NiO, Na2O, K2O, P2O5: 1σ, one standard deviation of the average; other: N — Table 3 note b: '1σ is 1 standard deviation of the average'" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "Tissint thin sections UT1, UT2, UT3; Tata-1-C1 to C3; Tata-2-C1 to C3; Tata-3-C1 to C3; Tissint-B" ;
    ada:samplingUnitName "Labelled at section level: X-ray maps are placed by thin section, e.g. an olivine megacryst \"in Tata-2-C3\" whose \"Red box outlines the area of X-ray maps\" (Fig. 3 caption, p.7); the sections are \"UT1 to UT3\" and \"Tata-1-C1 to C3, Tata-2-C1 to C3, and Tata-3-C1 to C3\" (pp.2–3). Map areas carry no labels of their own" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" .

<ex:epmaTAPP-Liu2016> schema1:identifier "test value schema:identifier" .


```


### detail example Liu2016-2
detail instance derived from Liu+2016_Cal | JEOL JXA-8200 | WDS Point Analysis (Caltech GPS).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Liu2016-2",
  "@type": [
    "ada:EPMAImage"
  ],
  "ada:componentType": "ada:EPMAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:epmaTAPP-Liu2016-2",
      "schema:identifier": "test value schema:identifier"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA Cosmochemistry NNX11AG58G and NNN13D465T; NSF EAR-1226270; NSF EAR-1019770 — 'We acknowledge partial support by ...'",
  "ada:sampleName": "Tissint thin sections UT1, UT2, UT3; Tata-1-C1 to C3; Tata-2-C1 to C3; Tata-3-C1 to C3; Tissint-B",
  "ada:samplingUnitName": "Labelled: thin sections \"UT1 to UT3\" and \"Tata-1-C1 to C3, Tata-2-C1 to C3, and Tata-3-C1 to C3\" (pp.2–3), and pyroxene grains within a section, e.g. \"T-3-C2 px1\" to \"T-3-C2 px5\" (Fig. 8, p.12); individual point analyses are not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "Partially — contributing counts are stated for the glass averages ('EMP avg (n = 73)' and 'avg (n = 14)', Table 3, p.9). No acceptance or rejection rule is stated. The table's n = 7 and n = 13 are LA-ICP-MS averages, not microprobe ones",
  "ada:combinedResults": "glass inclusion average (n = 73); impact-melt glass average (n = 14) — Table 3: 'Glass inclusion EMP avg (n = 73) 1σ' and the impact-melt 'avg (n = 14) 1σ', whose average 'only included the glassy regions of the impact melt pockets'",
  "ada:detectionLimit": "SiO2, TiO2, Al2O3, MgO, CaO: <0.03 wt%; FeO, MnO, Cr2O3, NiO, Na2O, K2O, P2O5: <0.05–0.1 wt%; other: N — 'Detection limits are typically <0.03 wt% for SiO2, TiO2, Al2O3, MgO, and CaO; <0.05–0.1 wt% for FeO, MnO, Cr2O3, NiO, Na2O, K2O, and P2O5' (p.3)",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "SiO2, TiO2, Al2O3, Cr2O3, MgO, CaO, MnO, FeO, NiO, Na2O, K2O, P2O5: 1σ, one standard deviation of the average; other: N — Table 3 note b"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Liu2016-2",
  "@type": [
    "ada:EPMAImage"
  ],
  "ada:componentType": "ada:EPMAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:epmaTAPP-Liu2016-2",
      "schema:identifier": "test value schema:identifier"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA Cosmochemistry NNX11AG58G and NNN13D465T; NSF EAR-1226270; NSF EAR-1019770 \u2014 'We acknowledge partial support by ...'",
  "ada:sampleName": "Tissint thin sections UT1, UT2, UT3; Tata-1-C1 to C3; Tata-2-C1 to C3; Tata-3-C1 to C3; Tissint-B",
  "ada:samplingUnitName": "Labelled: thin sections \"UT1 to UT3\" and \"Tata-1-C1 to C3, Tata-2-C1 to C3, and Tata-3-C1 to C3\" (pp.2\u20133), and pyroxene grains within a section, e.g. \"T-3-C2 px1\" to \"T-3-C2 px5\" (Fig. 8, p.12); individual point analyses are not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "Partially \u2014 contributing counts are stated for the glass averages ('EMP avg (n = 73)' and 'avg (n = 14)', Table 3, p.9). No acceptance or rejection rule is stated. The table's n = 7 and n = 13 are LA-ICP-MS averages, not microprobe ones",
  "ada:combinedResults": "glass inclusion average (n = 73); impact-melt glass average (n = 14) \u2014 Table 3: 'Glass inclusion EMP avg (n = 73) 1\u03c3' and the impact-melt 'avg (n = 14) 1\u03c3', whose average 'only included the glassy regions of the impact melt pockets'",
  "ada:detectionLimit": "SiO2, TiO2, Al2O3, MgO, CaO: <0.03 wt%; FeO, MnO, Cr2O3, NiO, Na2O, K2O, P2O5: <0.05\u20130.1 wt%; other: N \u2014 'Detection limits are typically <0.03 wt% for SiO2, TiO2, Al2O3, MgO, and CaO; <0.05\u20130.1 wt% for FeO, MnO, Cr2O3, NiO, Na2O, K2O, and P2O5' (p.3)",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "SiO2, TiO2, Al2O3, Cr2O3, MgO, CaO, MnO, FeO, NiO, Na2O, K2O, P2O5: 1\u03c3, one standard deviation of the average; other: N \u2014 Table 3 note b"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Liu2016-2> a ada:EPMAImage ;
    schema1:measurementTechnique <ex:epmaTAPP-Liu2016-2> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially — contributing counts are stated for the glass averages ('EMP avg (n = 73)' and 'avg (n = 14)', Table 3, p.9). No acceptance or rejection rule is stated. The table's n = 7 and n = 13 are LA-ICP-MS averages, not microprobe ones" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "glass inclusion average (n = 73); impact-melt glass average (n = 14) — Table 3: 'Glass inclusion EMP avg (n = 73) 1σ' and the impact-melt 'avg (n = 14) 1σ', whose average 'only included the glassy regions of the impact melt pockets'" ;
    ada:componentType "ada:EPMAImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "SiO2, TiO2, Al2O3, MgO, CaO: <0.03 wt%; FeO, MnO, Cr2O3, NiO, Na2O, K2O, P2O5: <0.05–0.1 wt%; other: N — 'Detection limits are typically <0.03 wt% for SiO2, TiO2, Al2O3, MgO, and CaO; <0.05–0.1 wt% for FeO, MnO, Cr2O3, NiO, Na2O, K2O, and P2O5' (p.3)" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA Cosmochemistry NNX11AG58G and NNN13D465T; NSF EAR-1226270; NSF EAR-1019770 — 'We acknowledge partial support by ...'" ;
    ada:goodnessOfFitOrDispersionStatistic "SiO2, TiO2, Al2O3, Cr2O3, MgO, CaO, MnO, FeO, NiO, Na2O, K2O, P2O5: 1σ, one standard deviation of the average; other: N — Table 3 note b" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "Tissint thin sections UT1, UT2, UT3; Tata-1-C1 to C3; Tata-2-C1 to C3; Tata-3-C1 to C3; Tissint-B" ;
    ada:samplingUnitName "Labelled: thin sections \"UT1 to UT3\" and \"Tata-1-C1 to C3, Tata-2-C1 to C3, and Tata-3-C1 to C3\" (pp.2–3), and pyroxene grains within a section, e.g. \"T-3-C2 px1\" to \"T-3-C2 px5\" (Fig. 8, p.12); individual point analyses are not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" .

<ex:epmaTAPP-Liu2016-2> schema1:identifier "test value schema:identifier" .


```


### detail example Ma2017
detail instance derived from Ma+2017 | JEOL 8200 | WDS Point Analysis (Caltech GPS Analytical Facility).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Ma2017",
  "@type": [
    "ada:EPMAImage"
  ],
  "ada:componentType": "ada:EPMAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:epmaTAPP-Ma2017",
      "schema:identifier": "test value schema:identifier"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Chi Ma",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NNSA Stewardship Science Academic Alliances, DOE Cooperative Agreements DE-NA0001982 and DESC0005278; NASA NNX12AJ01G — 'This work was supported in part by ...'",
  "ada:sampleName": "Zagami USNM 7619",
  "ada:samplingUnitName": "Labelled at section level only: \"The Zagami thin section (USNM 7619)\" (p.3); occurrences are identified by figure panel (\"First occurrence of liebermannite\", Fig. 1, p.2), not by label",
  "ada:targetMaterialOfSamplingUnit": "liebermannite (type, second and third occurrences); lingunite (next to type liebermannite); maskelynite (near type and near second liebermannite) — Table 1",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "Partially — each Table 1 column is the mean of n point analyses of one occurrence (n = 6, 2, 3, 3, 5 and 4; p.3), with one standard deviation of the mean. No acceptance or rejection rule is stated",
  "ada:combinedResults": "type liebermannite (n = 6); the second liebermannite (n = 2); the third liebermannite (n = 3); lingunite next to type liebermannite (n = 3); maskelynite near type liebermannite (n = 5); maskelynite near the 2nd liebermannite (n = 4) — the columns of Table 1, where the paper prints 'Maskeleyite'",
  "ada:detectionLimit": "Si: 0.05 wt%; Ti: 0.04 wt%; Al: 0.06 wt%; Fe: 0.06 wt%; Mg: 0.02 wt%; Ca: 0.02 wt%; Na: 0.03 wt%; K: 0.02 wt%; Cr: 0.05 wt%; Mn: 0.06 wt% — 'The detection limits (wt%) are 0.05 Si, 0.04 Ti, ...' (p.2) — stated per element, while Table 1 reports oxides",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "feldspar standards [Si, Al, Ca, Na, K: 1–2%; other: N] — 'The accuracy is 1–2% for Si, Al, Ca, Na, and K, based on analysis of feldspar standards as unknowns' — per element, while Table 1 reports oxides",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "SiO2, TiO2, Al2O3, FeO, CaO, Na2O, K2O: one standard deviation of the mean; other: N — Table 1 note c, same wording"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Ma2017",
  "@type": [
    "ada:EPMAImage"
  ],
  "ada:componentType": "ada:EPMAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:epmaTAPP-Ma2017",
      "schema:identifier": "test value schema:identifier"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Chi Ma",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NNSA Stewardship Science Academic Alliances, DOE Cooperative Agreements DE-NA0001982 and DESC0005278; NASA NNX12AJ01G \u2014 'This work was supported in part by ...'",
  "ada:sampleName": "Zagami USNM 7619",
  "ada:samplingUnitName": "Labelled at section level only: \"The Zagami thin section (USNM 7619)\" (p.3); occurrences are identified by figure panel (\"First occurrence of liebermannite\", Fig. 1, p.2), not by label",
  "ada:targetMaterialOfSamplingUnit": "liebermannite (type, second and third occurrences); lingunite (next to type liebermannite); maskelynite (near type and near second liebermannite) \u2014 Table 1",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "Partially \u2014 each Table 1 column is the mean of n point analyses of one occurrence (n = 6, 2, 3, 3, 5 and 4; p.3), with one standard deviation of the mean. No acceptance or rejection rule is stated",
  "ada:combinedResults": "type liebermannite (n = 6); the second liebermannite (n = 2); the third liebermannite (n = 3); lingunite next to type liebermannite (n = 3); maskelynite near type liebermannite (n = 5); maskelynite near the 2nd liebermannite (n = 4) \u2014 the columns of Table 1, where the paper prints 'Maskeleyite'",
  "ada:detectionLimit": "Si: 0.05 wt%; Ti: 0.04 wt%; Al: 0.06 wt%; Fe: 0.06 wt%; Mg: 0.02 wt%; Ca: 0.02 wt%; Na: 0.03 wt%; K: 0.02 wt%; Cr: 0.05 wt%; Mn: 0.06 wt% \u2014 'The detection limits (wt%) are 0.05 Si, 0.04 Ti, ...' (p.2) \u2014 stated per element, while Table 1 reports oxides",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "feldspar standards [Si, Al, Ca, Na, K: 1\u20132%; other: N] \u2014 'The accuracy is 1\u20132% for Si, Al, Ca, Na, and K, based on analysis of feldspar standards as unknowns' \u2014 per element, while Table 1 reports oxides",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "SiO2, TiO2, Al2O3, FeO, CaO, Na2O, K2O: one standard deviation of the mean; other: N \u2014 Table 1 note c, same wording"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Ma2017> a ada:EPMAImage ;
    schema1:measurementTechnique <ex:epmaTAPP-Ma2017> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially — each Table 1 column is the mean of n point analyses of one occurrence (n = 6, 2, 3, 3, 5 and 4; p.3), with one standard deviation of the mean. No acceptance or rejection rule is stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "Chi Ma" ;
    ada:analyticalAccuracy "feldspar standards [Si, Al, Ca, Na, K: 1–2%; other: N] — 'The accuracy is 1–2% for Si, Al, Ca, Na, and K, based on analysis of feldspar standards as unknowns' — per element, while Table 1 reports oxides" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "type liebermannite (n = 6); the second liebermannite (n = 2); the third liebermannite (n = 3); lingunite next to type liebermannite (n = 3); maskelynite near type liebermannite (n = 5); maskelynite near the 2nd liebermannite (n = 4) — the columns of Table 1, where the paper prints 'Maskeleyite'" ;
    ada:componentType "ada:EPMAImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "Si: 0.05 wt%; Ti: 0.04 wt%; Al: 0.06 wt%; Fe: 0.06 wt%; Mg: 0.02 wt%; Ca: 0.02 wt%; Na: 0.03 wt%; K: 0.02 wt%; Cr: 0.05 wt%; Mn: 0.06 wt% — 'The detection limits (wt%) are 0.05 Si, 0.04 Ti, ...' (p.2) — stated per element, while Table 1 reports oxides" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NNSA Stewardship Science Academic Alliances, DOE Cooperative Agreements DE-NA0001982 and DESC0005278; NASA NNX12AJ01G — 'This work was supported in part by ...'" ;
    ada:goodnessOfFitOrDispersionStatistic "SiO2, TiO2, Al2O3, FeO, CaO, Na2O, K2O: one standard deviation of the mean; other: N — Table 1 note c, same wording" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "Zagami USNM 7619" ;
    ada:samplingUnitName "Labelled at section level only: \"The Zagami thin section (USNM 7619)\" (p.3); occurrences are identified by figure panel (\"First occurrence of liebermannite\", Fig. 1, p.2), not by label" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "liebermannite (type, second and third occurrences); lingunite (next to type liebermannite); maskelynite (near type and near second liebermannite) — Table 1" .

<ex:epmaTAPP-Ma2017> schema1:identifier "test value schema:identifier" .


```


### detail example Frank2023
detail instance derived from Frank+2023 | Cameca SX100 | WDS Point Analysis (ARES JSC).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Frank2023",
  "@type": [
    "ada:EPMAImage"
  ],
  "ada:componentType": "ada:EPMAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:epmaTAPP-Frank2023",
      "schema:identifier": "test value schema:identifier"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "David R. Frank",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA NNX11AG78G, 13-COS13-0026, NNX14AI19G and 80NSSC18K0586; NASA Cosmochemistry and Emerging Worlds Programs — 'This work was supported by ...'",
  "ada:sampleName": "Ivuna CI chondrite, section MZ2",
  "ada:samplingUnitName": "Labelled at section level: the CAI \"in Ivuna section MZ2\" (p.3), in \"polished mount 'Ivuna MZ2'\" (p.14); the single CAI and its analysis points carry no labels",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N — the microprobe analyses are reported as \"Representative electron-microprobe measurements\" (p.5) with no contributing count and no selection rule. The counts on p.8 (n = 9, n = 7) are SIMS standard populations, not microprobe aggregates",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": "Al2O3, K2O, CaO: 0.03–0.04 wt%; Na2O, MgO, SiO2, FeO, MnO: 0.05 wt%; P2O5, SO2, TiO2, V2O3, Cr2O3, NiO: 0.06–0.09 wt% — 'typically' (p.4)",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Frank2023",
  "@type": [
    "ada:EPMAImage"
  ],
  "ada:componentType": "ada:EPMAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:epmaTAPP-Frank2023",
      "schema:identifier": "test value schema:identifier"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "David R. Frank",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA NNX11AG78G, 13-COS13-0026, NNX14AI19G and 80NSSC18K0586; NASA Cosmochemistry and Emerging Worlds Programs \u2014 'This work was supported by ...'",
  "ada:sampleName": "Ivuna CI chondrite, section MZ2",
  "ada:samplingUnitName": "Labelled at section level: the CAI \"in Ivuna section MZ2\" (p.3), in \"polished mount 'Ivuna MZ2'\" (p.14); the single CAI and its analysis points carry no labels",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 the microprobe analyses are reported as \"Representative electron-microprobe measurements\" (p.5) with no contributing count and no selection rule. The counts on p.8 (n = 9, n = 7) are SIMS standard populations, not microprobe aggregates",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": "Al2O3, K2O, CaO: 0.03\u20130.04 wt%; Na2O, MgO, SiO2, FeO, MnO: 0.05 wt%; P2O5, SO2, TiO2, V2O3, Cr2O3, NiO: 0.06\u20130.09 wt% \u2014 'typically' (p.4)",
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

<ex:detail-Frank2023> a ada:EPMAImage ;
    schema1:measurementTechnique <ex:epmaTAPP-Frank2023> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — the microprobe analyses are reported as \"Representative electron-microprobe measurements\" (p.5) with no contributing count and no selection rule. The counts on p.8 (n = 9, n = 7) are SIMS standard populations, not microprobe aggregates" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "David R. Frank" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "missing" ;
    ada:componentType "ada:EPMAImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "Al2O3, K2O, CaO: 0.03–0.04 wt%; Na2O, MgO, SiO2, FeO, MnO: 0.05 wt%; P2O5, SO2, TiO2, V2O3, Cr2O3, NiO: 0.06–0.09 wt% — 'typically' (p.4)" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA NNX11AG78G, 13-COS13-0026, NNX14AI19G and 80NSSC18K0586; NASA Cosmochemistry and Emerging Worlds Programs — 'This work was supported by ...'" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "Ivuna CI chondrite, section MZ2" ;
    ada:samplingUnitName "Labelled at section level: the CAI \"in Ivuna section MZ2\" (p.3), in \"polished mount 'Ivuna MZ2'\" (p.14); the single CAI and its analysis points carry no labels" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" .

<ex:epmaTAPP-Frank2023> schema1:identifier "test value schema:identifier" .


```


### detail example Broussard2026
detail instance derived from Broussard+2026 | JEOL JXA-8200 | WDS Mapping (WashU).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Broussard2026",
  "@type": [
    "ada:EPMAImage"
  ],
  "ada:componentType": "ada:EPMAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:epmaTAPP-Broussard2026",
      "schema:identifier": "test value schema:identifier"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA 80NSSC22K1689; NASA 80NSSC24K1284; McDonnell Center for the Space Sciences — 'Individual funding was provided by ...'",
  "ada:sampleName": "OC002 LAB24-2 (10-11 fragments of Oued Chebeika 002)",
  "ada:samplingUnitName": "Labelled: \"OC002 LAB24-2 fragment 1\" and \"fragment 2\" (Figs 3–4, pp.6–7), and within fragment 1 \"lithic clast LC1\" (Figure S3 caption, p.17); map areas are otherwise unlabelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "Partially — the carbonate compositions are means of stated counts (\"Dolomite contains 2.0 ± 0.4 wt% Fe and 3.0 ± 0.9 wt% Mn (n = 37)\"; \"Magnesite contains 14.5 ± 2.7 wt% Fe and 4.6 ± 2.5 wt % Mn (n = 23)\", p.5). No acceptance or rejection rule is stated",
  "ada:combinedResults": "dolomite (n = 37); magnesite (n = 23) — 'Dolomite contains 2.0 ± 0.4 wt% Fe and 3.0 ± 0.9 wt% Mn (n = 37)'; 'Magnesite contains 14.5 ± 2.7 wt% Fe and 4.6 ± 2.5 wt % Mn (n = 23)'",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "N — the carbonate means are given as '±' values ('2.0 ± 0.4 wt% Fe') without naming the statistic"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Broussard2026",
  "@type": [
    "ada:EPMAImage"
  ],
  "ada:componentType": "ada:EPMAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:epmaTAPP-Broussard2026",
      "schema:identifier": "test value schema:identifier"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA 80NSSC22K1689; NASA 80NSSC24K1284; McDonnell Center for the Space Sciences \u2014 'Individual funding was provided by ...'",
  "ada:sampleName": "OC002 LAB24-2 (10-11 fragments of Oued Chebeika 002)",
  "ada:samplingUnitName": "Labelled: \"OC002 LAB24-2 fragment 1\" and \"fragment 2\" (Figs 3\u20134, pp.6\u20137), and within fragment 1 \"lithic clast LC1\" (Figure S3 caption, p.17); map areas are otherwise unlabelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "Partially \u2014 the carbonate compositions are means of stated counts (\"Dolomite contains 2.0 \u00b1 0.4 wt% Fe and 3.0 \u00b1 0.9 wt% Mn (n = 37)\"; \"Magnesite contains 14.5 \u00b1 2.7 wt% Fe and 4.6 \u00b1 2.5 wt % Mn (n = 23)\", p.5). No acceptance or rejection rule is stated",
  "ada:combinedResults": "dolomite (n = 37); magnesite (n = 23) \u2014 'Dolomite contains 2.0 \u00b1 0.4 wt% Fe and 3.0 \u00b1 0.9 wt% Mn (n = 37)'; 'Magnesite contains 14.5 \u00b1 2.7 wt% Fe and 4.6 \u00b1 2.5 wt % Mn (n = 23)'",
  "ada:detectionLimit": -9999,
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "N \u2014 the carbonate means are given as '\u00b1' values ('2.0 \u00b1 0.4 wt% Fe') without naming the statistic"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Broussard2026> a ada:EPMAImage ;
    schema1:measurementTechnique <ex:epmaTAPP-Broussard2026> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially — the carbonate compositions are means of stated counts (\"Dolomite contains 2.0 ± 0.4 wt% Fe and 3.0 ± 0.9 wt% Mn (n = 37)\"; \"Magnesite contains 14.5 ± 2.7 wt% Fe and 4.6 ± 2.5 wt % Mn (n = 23)\", p.5). No acceptance or rejection rule is stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "dolomite (n = 37); magnesite (n = 23) — 'Dolomite contains 2.0 ± 0.4 wt% Fe and 3.0 ± 0.9 wt% Mn (n = 37)'; 'Magnesite contains 14.5 ± 2.7 wt% Fe and 4.6 ± 2.5 wt % Mn (n = 23)'" ;
    ada:componentType "ada:EPMAImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA 80NSSC22K1689; NASA 80NSSC24K1284; McDonnell Center for the Space Sciences — 'Individual funding was provided by ...'" ;
    ada:goodnessOfFitOrDispersionStatistic "N — the carbonate means are given as '±' values ('2.0 ± 0.4 wt% Fe') without naming the statistic" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "OC002 LAB24-2 (10-11 fragments of Oued Chebeika 002)" ;
    ada:samplingUnitName "Labelled: \"OC002 LAB24-2 fragment 1\" and \"fragment 2\" (Figs 3–4, pp.6–7), and within fragment 1 \"lithic clast LC1\" (Figure S3 caption, p.17); map areas are otherwise unlabelled" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" .

<ex:epmaTAPP-Broussard2026> schema1:identifier "test value schema:identifier" .


```


### detail example Seifert2026
detail instance derived from Seifert+2026 | JEOL 8530 | WDS Point Analysis (ARES JSC).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Seifert2026",
  "@type": [
    "ada:EPMAImage"
  ],
  "ada:componentType": "ada:EPMAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:epmaTAPP-Seifert2026",
      "schema:identifier": "test value schema:identifier"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Logan B. Seifert",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program); NASA Postdoctoral Program — acknowledgements",
  "ada:sampleName": "OREX-803079-0 and OREX-803080-0 (Bennu OSIRIS-REx samples)",
  "ada:samplingUnitName": "Labelled: apatite grains numbered within each particle — \"OREX-803166-0 … Ap. #1 Ap. #2 Ap. #3 Ap. #4\" (Table 1, p.7) — in particles \"OREX-803166-0, OREX-803169-0, and OREX-803173-0\" (p.3) from the mounts \"OREX-803079-0 and OREX-803080-0\" (p.2)",
  "ada:targetMaterialOfSamplingUnit": "Phosphate (apatite) for every grain, Ap. #1 onward — Table 1",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N — Table 1 reports one column per named apatite grain rather than an aggregate over results, and no acceptance or rejection rule is stated",
  "ada:combinedResults": "N — Table 1 reports one column per apatite grain; no combined value is stated",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Seifert2026",
  "@type": [
    "ada:EPMAImage"
  ],
  "ada:componentType": "ada:EPMAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:epmaTAPP-Seifert2026",
      "schema:identifier": "test value schema:identifier"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "Logan B. Seifert",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program); NASA Postdoctoral Program \u2014 acknowledgements",
  "ada:sampleName": "OREX-803079-0 and OREX-803080-0 (Bennu OSIRIS-REx samples)",
  "ada:samplingUnitName": "Labelled: apatite grains numbered within each particle \u2014 \"OREX-803166-0 \u2026 Ap. #1 Ap. #2 Ap. #3 Ap. #4\" (Table 1, p.7) \u2014 in particles \"OREX-803166-0, OREX-803169-0, and OREX-803173-0\" (p.3) from the mounts \"OREX-803079-0 and OREX-803080-0\" (p.2)",
  "ada:targetMaterialOfSamplingUnit": "Phosphate (apatite) for every grain, Ap. #1 onward \u2014 Table 1",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 Table 1 reports one column per named apatite grain rather than an aggregate over results, and no acceptance or rejection rule is stated",
  "ada:combinedResults": "N \u2014 Table 1 reports one column per apatite grain; no combined value is stated",
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

<ex:detail-Seifert2026> a ada:EPMAImage ;
    schema1:measurementTechnique <ex:epmaTAPP-Seifert2026> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — Table 1 reports one column per named apatite grain rather than an aggregate over results, and no acceptance or rejection rule is stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "Logan B. Seifert" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "N — Table 1 reports one column per apatite grain; no combined value is stated" ;
    ada:componentType "ada:EPMAImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program); NASA Postdoctoral Program — acknowledgements" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "OREX-803079-0 and OREX-803080-0 (Bennu OSIRIS-REx samples)" ;
    ada:samplingUnitName "Labelled: apatite grains numbered within each particle — \"OREX-803166-0 … Ap. #1 Ap. #2 Ap. #3 Ap. #4\" (Table 1, p.7) — in particles \"OREX-803166-0, OREX-803169-0, and OREX-803173-0\" (p.3) from the mounts \"OREX-803079-0 and OREX-803080-0\" (p.2)" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "Phosphate (apatite) for every grain, Ap. #1 onward — Table 1" .

<ex:epmaTAPP-Seifert2026> schema1:identifier "test value schema:identifier" .


```


### detail example Pang2016
detail instance derived from Pang+2016 | JEOL JXA-8100 | WDS Point Analysis (Nanjing U.).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Pang2016",
  "@type": [
    "ada:EPMAImage"
  ],
  "ada:componentType": "ada:EPMAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:epmaTAPP-Pang2016",
      "schema:identifier": "test value schema:identifier"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NSFC 41373065; State Key Laboratory for Mineral Deposits Research ZZKT-201322; Fundamental Research Funds for the Central Universities — 'This study was supported by grants from ...'",
  "ada:sampleName": "NWA 8003 eucrite",
  "ada:samplingUnitName": "Sample name only — NWA 8003; grains are identified by setting (\"garnet grains within the eclogitic mineral assemblage\", p.4), and the point analyses are in \"Supplementary Table 4\" (p.4), not in the archived PDF",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "Partially — the reported averages state their contributing counts (\"based on 12 analyses\" for orthopyroxene, and \"14 analyses\" for augite, p.2; \"based on 13 analyses\" and \"34 ± 7 mol% on average; 19 analyses\" for the Ca-Eskola component, p.4). No acceptance or rejection rule is stated",
  "ada:combinedResults": "orthopyroxene (n = 12); augite (n = 14); clinopyroxene in the eclogitic assemblage of zoned veins (n = 13); clinopyroxene in thin melt veins and edge zones (n = 19) — 'based on 12 analyses', '14 analyses' (p.2); Ca-Esk components '41 ± 8 mol% on average; based on 13 analyses' in the former, '34 ± 7 mol% on average; 19 analyses' in the latter (p.4)",
  "ada:detectionLimit": "all: better than 0.02 wt% (typical) — 'Typical detection limits for oxides of most elements were better than 0.02 wt%'",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "N — the averages are given as '±' values ('41 ± 8 mol%') without naming the statistic"
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Pang2016",
  "@type": [
    "ada:EPMAImage"
  ],
  "ada:componentType": "ada:EPMAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:epmaTAPP-Pang2016",
      "schema:identifier": "test value schema:identifier"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NSFC 41373065; State Key Laboratory for Mineral Deposits Research ZZKT-201322; Fundamental Research Funds for the Central Universities \u2014 'This study was supported by grants from ...'",
  "ada:sampleName": "NWA 8003 eucrite",
  "ada:samplingUnitName": "Sample name only \u2014 NWA 8003; grains are identified by setting (\"garnet grains within the eclogitic mineral assemblage\", p.4), and the point analyses are in \"Supplementary Table 4\" (p.4), not in the archived PDF",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "Partially \u2014 the reported averages state their contributing counts (\"based on 12 analyses\" for orthopyroxene, and \"14 analyses\" for augite, p.2; \"based on 13 analyses\" and \"34 \u00b1 7 mol% on average; 19 analyses\" for the Ca-Eskola component, p.4). No acceptance or rejection rule is stated",
  "ada:combinedResults": "orthopyroxene (n = 12); augite (n = 14); clinopyroxene in the eclogitic assemblage of zoned veins (n = 13); clinopyroxene in thin melt veins and edge zones (n = 19) \u2014 'based on 12 analyses', '14 analyses' (p.2); Ca-Esk components '41 \u00b1 8 mol% on average; based on 13 analyses' in the former, '34 \u00b1 7 mol% on average; 19 analyses' in the latter (p.4)",
  "ada:detectionLimit": "all: better than 0.02 wt% (typical) \u2014 'Typical detection limits for oxides of most elements were better than 0.02 wt%'",
  "ada:analyticalPrecision": "missing",
  "ada:analyticalAccuracy": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:edsDeadTime": -9999,
  "ada:goodnessOfFitOrDispersionStatistic": "N \u2014 the averages are given as '\u00b1' values ('41 \u00b1 8 mol%') without naming the statistic"
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Pang2016> a ada:EPMAImage ;
    schema1:measurementTechnique <ex:epmaTAPP-Pang2016> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "Partially — the reported averages state their contributing counts (\"based on 12 analyses\" for orthopyroxene, and \"14 analyses\" for augite, p.2; \"based on 13 analyses\" and \"34 ± 7 mol% on average; 19 analyses\" for the Ca-Eskola component, p.4). No acceptance or rejection rule is stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "orthopyroxene (n = 12); augite (n = 14); clinopyroxene in the eclogitic assemblage of zoned veins (n = 13); clinopyroxene in thin melt veins and edge zones (n = 19) — 'based on 12 analyses', '14 analyses' (p.2); Ca-Esk components '41 ± 8 mol% on average; based on 13 analyses' in the former, '34 ± 7 mol% on average; 19 analyses' in the latter (p.4)" ;
    ada:componentType "ada:EPMAImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "all: better than 0.02 wt% (typical) — 'Typical detection limits for oxides of most elements were better than 0.02 wt%'" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NSFC 41373065; State Key Laboratory for Mineral Deposits Research ZZKT-201322; Fundamental Research Funds for the Central Universities — 'This study was supported by grants from ...'" ;
    ada:goodnessOfFitOrDispersionStatistic "N — the averages are given as '±' values ('41 ± 8 mol%') without naming the statistic" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "NWA 8003 eucrite" ;
    ada:samplingUnitName "Sample name only — NWA 8003; grains are identified by setting (\"garnet grains within the eclogitic mineral assemblage\", p.4), and the point analyses are in \"Supplementary Table 4\" (p.4), not in the archived PDF" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" .

<ex:epmaTAPP-Pang2016> schema1:identifier "test value schema:identifier" .


```


### detail example McCoy2025
detail instance derived from McCoy+2025_SI | JEOL 8530F+ | WDS Point Analysis (Smithsonian).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-McCoy2025",
  "@type": [
    "ada:EPMAImage"
  ],
  "ada:componentType": "ada:EPMAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:epmaTAPP-McCoy2025",
      "schema:identifier": "test value schema:identifier"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) — 'This material is based on work supported by ...'; individual grants are also listed by person (80NSSC22K1692, MR/T020261/1, ST/V000675/1, 22EXPOSITO)",
  "ada:sampleName": "Bennu OSIRIS-REx samples (OREX-8#####-###)",
  "ada:samplingUnitName": "N — the Smithsonian microprobe passage names no specimens (\"conducted on Ir-coated specimens\", p.7); the paper's OREX numbers identify figure images, not microprobe analyses",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N — compositions are reported by phase with no contributing count and no selection rule stated",
  "ada:combinedResults": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-McCoy2025",
  "@type": [
    "ada:EPMAImage"
  ],
  "ada:componentType": "ada:EPMAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:epmaTAPP-McCoy2025",
      "schema:identifier": "test value schema:identifier"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) \u2014 'This material is based on work supported by ...'; individual grants are also listed by person (80NSSC22K1692, MR/T020261/1, ST/V000675/1, 22EXPOSITO)",
  "ada:sampleName": "Bennu OSIRIS-REx samples (OREX-8#####-###)",
  "ada:samplingUnitName": "N \u2014 the Smithsonian microprobe passage names no specimens (\"conducted on Ir-coated specimens\", p.7); the paper's OREX numbers identify figure images, not microprobe analyses",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 compositions are reported by phase with no contributing count and no selection rule stated",
  "ada:combinedResults": "missing",
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

<ex:detail-McCoy2025> a ada:EPMAImage ;
    schema1:measurementTechnique <ex:epmaTAPP-McCoy2025> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — compositions are reported by phase with no contributing count and no selection rule stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "missing" ;
    ada:componentType "ada:EPMAImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) — 'This material is based on work supported by ...'; individual grants are also listed by person (80NSSC22K1692, MR/T020261/1, ST/V000675/1, 22EXPOSITO)" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "Bennu OSIRIS-REx samples (OREX-8#####-###)" ;
    ada:samplingUnitName "N — the Smithsonian microprobe passage names no specimens (\"conducted on Ir-coated specimens\", p.7); the paper's OREX numbers identify figure images, not microprobe analyses" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" .

<ex:epmaTAPP-McCoy2025> schema1:identifier "test value schema:identifier" .


```


### detail example McCoy2025-2
detail instance derived from McCoy+2025_UA | Cameca SX-100 | WDS Point Analysis (K-ALFAA U.Arizona).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-McCoy2025-2",
  "@type": [
    "ada:EPMAImage"
  ],
  "ada:componentType": "ada:EPMAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:epmaTAPP-McCoy2025-2",
      "schema:identifier": "test value schema:identifier"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) — 'This material is based on work supported by ...'; individual grants are also listed by person (80NSSC22K1692, MR/T020261/1, ST/V000675/1, 22EXPOSITO)",
  "ada:sampleName": "Bennu OSIRIS-REx samples (OREX-8#####-###)",
  "ada:samplingUnitName": "N — the Arizona microprobe passage names no specimen (\"the section was coated with a thin film of carbon\", p.7); the paper's OREX numbers identify figure images, not microprobe analyses",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N — compositions are reported by phase with no contributing count and no selection rule stated",
  "ada:combinedResults": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-McCoy2025-2",
  "@type": [
    "ada:EPMAImage"
  ],
  "ada:componentType": "ada:EPMAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:epmaTAPP-McCoy2025-2",
      "schema:identifier": "test value schema:identifier"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) \u2014 'This material is based on work supported by ...'; individual grants are also listed by person (80NSSC22K1692, MR/T020261/1, ST/V000675/1, 22EXPOSITO)",
  "ada:sampleName": "Bennu OSIRIS-REx samples (OREX-8#####-###)",
  "ada:samplingUnitName": "N \u2014 the Arizona microprobe passage names no specimen (\"the section was coated with a thin film of carbon\", p.7); the paper's OREX numbers identify figure images, not microprobe analyses",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 compositions are reported by phase with no contributing count and no selection rule stated",
  "ada:combinedResults": "missing",
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

<ex:detail-McCoy2025-2> a ada:EPMAImage ;
    schema1:measurementTechnique <ex:epmaTAPP-McCoy2025-2> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — compositions are reported by phase with no contributing count and no selection rule stated" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "missing" ;
    ada:componentType "ada:EPMAImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) — 'This material is based on work supported by ...'; individual grants are also listed by person (80NSSC22K1692, MR/T020261/1, ST/V000675/1, 22EXPOSITO)" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "Bennu OSIRIS-REx samples (OREX-8#####-###)" ;
    ada:samplingUnitName "N — the Arizona microprobe passage names no specimen (\"the section was coated with a thin film of carbon\", p.7); the paper's OREX numbers identify figure images, not microprobe analyses" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" .

<ex:epmaTAPP-McCoy2025-2> schema1:identifier "test value schema:identifier" .


```


### detail example Zega2025
detail instance derived from Zega+2025 | Cameca SX-100 Ultra | WDS Point Analysis (K-ALFAA U.Arizona).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Zega2025",
  "@type": [
    "ada:EPMAImage"
  ],
  "ada:componentType": "ada:EPMAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:epmaTAPP-Zega2025",
      "schema:identifier": "test value schema:identifier"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) — 'This material is based upon work supported by ...'; the K-ALFAA facility and instrumentation support is under Funding Source for Procedure Development",
  "ada:sampleName": "Bennu OSIRIS-REx samples (OREX-5/8#####-###)",
  "ada:samplingUnitName": "Labelled by curation number per particle: \"EMPA data from Bennu particles\" (Fig. 1) cites \"OREX-803095-0\" and \"OREX-803096-0\", and sulfide compositions \"in samples OREX-803095-0, OREX-803096-0, OREX-803066-0, OREX-803067-0 and OREX-803070-0\" (p.2); points within particles are not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N — no contributing count and no acceptance or rejection rule is stated for the microprobe analyses; the modal abundances come from classified phase-map pixels rather than from admitting or excluding results (p.9)",
  "ada:combinedResults": "missing",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Zega2025",
  "@type": [
    "ada:EPMAImage"
  ],
  "ada:componentType": "ada:EPMAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:epmaTAPP-Zega2025",
      "schema:identifier": "test value schema:identifier"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) \u2014 'This material is based upon work supported by ...'; the K-ALFAA facility and instrumentation support is under Funding Source for Procedure Development",
  "ada:sampleName": "Bennu OSIRIS-REx samples (OREX-5/8#####-###)",
  "ada:samplingUnitName": "Labelled by curation number per particle: \"EMPA data from Bennu particles\" (Fig. 1) cites \"OREX-803095-0\" and \"OREX-803096-0\", and sulfide compositions \"in samples OREX-803095-0, OREX-803096-0, OREX-803066-0, OREX-803067-0 and OREX-803070-0\" (p.2); points within particles are not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 no contributing count and no acceptance or rejection rule is stated for the microprobe analyses; the modal abundances come from classified phase-map pixels rather than from admitting or excluding results (p.9)",
  "ada:combinedResults": "missing",
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

<ex:detail-Zega2025> a ada:EPMAImage ;
    schema1:measurementTechnique <ex:epmaTAPP-Zega2025> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — no contributing count and no acceptance or rejection rule is stated for the microprobe analyses; the modal abundances come from classified phase-map pixels rather than from admitting or excluding results (p.9)" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "missing" ;
    ada:componentType "ada:EPMAImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) — 'This material is based upon work supported by ...'; the K-ALFAA facility and instrumentation support is under Funding Source for Procedure Development" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "Bennu OSIRIS-REx samples (OREX-5/8#####-###)" ;
    ada:samplingUnitName "Labelled by curation number per particle: \"EMPA data from Bennu particles\" (Fig. 1) cites \"OREX-803095-0\" and \"OREX-803096-0\", and sulfide compositions \"in samples OREX-803095-0, OREX-803096-0, OREX-803066-0, OREX-803067-0 and OREX-803070-0\" (p.2); points within particles are not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" .

<ex:epmaTAPP-Zega2025> schema1:identifier "test value schema:identifier" .


```


### detail example Barnes2025
detail instance derived from Barnes+2025 | JEOL JXA-8230 | WDS Point Analysis (CRPG Nancy).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Barnes2025",
  "@type": [
    "ada:EPMAImage"
  ],
  "ada:componentType": "ada:EPMAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:epmaTAPP-Barnes2025",
      "schema:identifier": "test value schema:identifier"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) — acknowledged with the named authors; further grants are listed by person across many laboratories, and none is attributed to the microprobe work",
  "ada:sampleName": "OREX-800045-103 and OREX-800045-107",
  "ada:samplingUnitName": "Labelled at split level: \"Samples OREX-800045-103 and OREX-800045-107 ... Aggregate particles (<1 mm) were mounted in epoxy\" (p.11); particles and points are not labelled, and the data are \"compiled in Supplementary Table 14\" (p.11), not in the archived PDF",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N — the analyses are \"compiled in Supplementary Table 14\" (p.11), not in the archived PDF, and no count or selection rule is stated in the text. The \"Bennu (n = 58)\" population (Fig. 5, p.6) is the SIMS oxygen-isotope dataset, not this procedure's",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": "Mg: 0.025 wt%; Fe: 0.025 wt%; Si, K, Na: 0.05 wt%; Ca: 0.005 wt%; Al: 0.02 wt%; Ti: 0.005 wt%; Cr: 0.015 wt%; Mn: 0.008 wt%; other: N — p.11",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Barnes2025",
  "@type": [
    "ada:EPMAImage"
  ],
  "ada:componentType": "ada:EPMAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:epmaTAPP-Barnes2025",
      "schema:identifier": "test value schema:identifier"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) \u2014 acknowledged with the named authors; further grants are listed by person across many laboratories, and none is attributed to the microprobe work",
  "ada:sampleName": "OREX-800045-103 and OREX-800045-107",
  "ada:samplingUnitName": "Labelled at split level: \"Samples OREX-800045-103 and OREX-800045-107 ... Aggregate particles (<1 mm) were mounted in epoxy\" (p.11); particles and points are not labelled, and the data are \"compiled in Supplementary Table 14\" (p.11), not in the archived PDF",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 the analyses are \"compiled in Supplementary Table 14\" (p.11), not in the archived PDF, and no count or selection rule is stated in the text. The \"Bennu (n = 58)\" population (Fig. 5, p.6) is the SIMS oxygen-isotope dataset, not this procedure's",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": "Mg: 0.025 wt%; Fe: 0.025 wt%; Si, K, Na: 0.05 wt%; Ca: 0.005 wt%; Al: 0.02 wt%; Ti: 0.005 wt%; Cr: 0.015 wt%; Mn: 0.008 wt%; other: N \u2014 p.11",
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

<ex:detail-Barnes2025> a ada:EPMAImage ;
    schema1:measurementTechnique <ex:epmaTAPP-Barnes2025> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — the analyses are \"compiled in Supplementary Table 14\" (p.11), not in the archived PDF, and no count or selection rule is stated in the text. The \"Bennu (n = 58)\" population (Fig. 5, p.6) is the SIMS oxygen-isotope dataset, not this procedure's" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "missing" ;
    ada:componentType "ada:EPMAImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "Mg: 0.025 wt%; Fe: 0.025 wt%; Si, K, Na: 0.05 wt%; Ca: 0.005 wt%; Al: 0.02 wt%; Ti: 0.005 wt%; Cr: 0.015 wt%; Mn: 0.008 wt%; other: N — p.11" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) — acknowledged with the named authors; further grants are listed by person across many laboratories, and none is attributed to the microprobe work" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "OREX-800045-103 and OREX-800045-107" ;
    ada:samplingUnitName "Labelled at split level: \"Samples OREX-800045-103 and OREX-800045-107 ... Aggregate particles (<1 mm) were mounted in epoxy\" (p.11); particles and points are not labelled, and the data are \"compiled in Supplementary Table 14\" (p.11), not in the archived PDF" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" .

<ex:epmaTAPP-Barnes2025> schema1:identifier "test value schema:identifier" .


```


### detail example Barnes2025-2
detail instance derived from Barnes+2025 | Cameca SX100 | WDS Point Analysis (NHM London).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Barnes2025-2",
  "@type": [
    "ada:EPMAImage"
  ],
  "ada:componentType": "ada:EPMAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:epmaTAPP-Barnes2025-2",
      "schema:identifier": "test value schema:identifier"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) — acknowledged with the named authors; further grants are listed by person across many laboratories, and none is attributed to the microprobe work",
  "ada:sampleName": "OREX-501054-0 and OREX-501059-0 (particles P1, P2)",
  "ada:samplingUnitName": "Labelled: \"The samples OREX-501054-0 and OREX-501059-0 ... fragmented into particles, identified as P1 and P2\" (p.13); the olivine and pyroxene grains within them are not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "N/A — no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N — no contributing count and no acceptance or rejection rule is stated for the olivine and pyroxene analyses",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": "N — 'Typical detection limits for transition metals were around 250 ppm'; the elements are not named",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Barnes2025-2",
  "@type": [
    "ada:EPMAImage"
  ],
  "ada:componentType": "ada:EPMAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:epmaTAPP-Barnes2025-2",
      "schema:identifier": "test value schema:identifier"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) \u2014 acknowledged with the named authors; further grants are listed by person across many laboratories, and none is attributed to the microprobe work",
  "ada:sampleName": "OREX-501054-0 and OREX-501059-0 (particles P1, P2)",
  "ada:samplingUnitName": "Labelled: \"The samples OREX-501054-0 and OREX-501059-0 ... fragmented into particles, identified as P1 and P2\" (p.13); the olivine and pyroxene grains within them are not labelled",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": -9999,
  "ada:mapArea": -9999,
  "ada:proceduralBlankLevel": "N/A \u2014 no chemical separation, so there is no procedural blank",
  "ada:analysisInclusionAndRejectionCriteria": "N \u2014 no contributing count and no acceptance or rejection rule is stated for the olivine and pyroxene analyses",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": "N \u2014 'Typical detection limits for transition metals were around 250 ppm'; the elements are not named",
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

<ex:detail-Barnes2025-2> a ada:EPMAImage ;
    schema1:measurementTechnique <ex:epmaTAPP-Barnes2025-2> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "N — no contributing count and no acceptance or rejection rule is stated for the olivine and pyroxene analyses" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "missing" ;
    ada:componentType "ada:EPMAImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "N — 'Typical detection limits for transition metals were around 250 ppm'; the elements are not named" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA NNH09ZDA007O under contract NNM10AA11C (New Frontiers Program) — acknowledged with the named authors; further grants are listed by person across many laboratories, and none is attributed to the microprobe work" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea -9999 ;
    ada:mapDimensions -9999 ;
    ada:proceduralBlankLevel "N/A — no chemical separation, so there is no procedural blank" ;
    ada:sampleName "OREX-501054-0 and OREX-501059-0 (particles P1, P2)" ;
    ada:samplingUnitName "Labelled: \"The samples OREX-501054-0 and OREX-501059-0 ... fragmented into particles, identified as P1 and P2\" (p.13); the olivine and pyroxene grains within them are not labelled" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" .

<ex:epmaTAPP-Barnes2025-2> schema1:identifier "test value schema:identifier" .


```


### detail example Neuman2025
detail instance derived from Neuman+2025 | WashU St. Louis | WDS Mapping (JEOL JXA-8200).
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Neuman2025",
  "@type": [
    "ada:EPMAImage"
  ],
  "ada:componentType": "ada:EPMAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:epmaTAPP-Neuman2025",
      "schema:identifier": "test value schema:identifier"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA ANGSA program 80NSSC19K0958 — 'We thank NASA for support of the ANGSA program (Grant 80NSSC19K0958)'",
  "ada:sampleName": "73001,6014-73001,6021",
  "ada:samplingUnitName": "Labelled at thin-section level: \"The 73001,6014–73001,6021 samples are 50 × 25 mm continuous thin sections\" (p.6), e.g. the \"73001,6019\" X-ray map (p.11); every map pixel is an analysis, so the section — the acquisition area — is the unit named",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": 1,
  "ada:mapArea": "N - not stated directly (1,024 pixels at 9.5 um step corresponds to ~9.7 mm per side)",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": "all: 0.1–0.2 element wt% — 'for all elements in this map set'",
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Neuman2025",
  "@type": [
    "ada:EPMAImage"
  ],
  "ada:componentType": "ada:EPMAImage",
  "schema:measurementTechnique": [
    {
      "@id": "ex:epmaTAPP-Neuman2025",
      "schema:identifier": "test value schema:identifier"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "NASA ANGSA program 80NSSC19K0958 \u2014 'We thank NASA for support of the ANGSA program (Grant 80NSSC19K0958)'",
  "ada:sampleName": "73001,6014-73001,6021",
  "ada:samplingUnitName": "Labelled at thin-section level: \"The 73001,6014\u201373001,6021 samples are 50 \u00d7 25 mm continuous thin sections\" (p.6), e.g. the \"73001,6019\" X-ray map (p.11); every map pixel is an analysis, so the section \u2014 the acquisition area \u2014 is the unit named",
  "ada:targetMaterialOfSamplingUnit": "missing",
  "ada:mapDimensions": 1,
  "ada:mapArea": "N - not stated directly (1,024 pixels at 9.5 um step corresponds to ~9.7 mm per side)",
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:combinedResults": "missing",
  "ada:detectionLimit": "all: 0.1\u20130.2 element wt% \u2014 'for all elements in this map set'",
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

<ex:detail-Neuman2025> a ada:EPMAImage ;
    schema1:measurementTechnique <ex:epmaTAPP-Neuman2025> ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracy "missing" ;
    ada:analyticalPrecision "missing" ;
    ada:combinedResults "missing" ;
    ada:componentType "ada:EPMAImage" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit "all: 0.1–0.2 element wt% — 'for all elements in this map set'" ;
    ada:edsDeadTime -9999 ;
    ada:fundingSourceForAnalysis "NASA ANGSA program 80NSSC19K0958 — 'We thank NASA for support of the ANGSA program (Grant 80NSSC19K0958)'" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:mapArea "N - not stated directly (1,024 pixels at 9.5 um step corresponds to ~9.7 mm per side)" ;
    ada:mapDimensions 1 ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "73001,6014-73001,6021" ;
    ada:samplingUnitName "Labelled at thin-section level: \"The 73001,6014–73001,6021 samples are 50 × 25 mm continuous thin sections\" (p.6), e.g. the \"73001,6019\" X-ray map (p.11); every map pixel is an analysis, so the section — the acquisition area — is the unit named" ;
    ada:sessionIdentifier "missing" ;
    ada:targetMaterialOfSamplingUnit "missing" .

<ex:epmaTAPP-Neuman2025> schema1:identifier "test value schema:identifier" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: EPMA/EPMA Analysis Detail
description: Dataset-level analysis-instance detail for EPMA/EPMA, reusing CDIF/schema.org
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
                                          const: ada:parameter/epmaTAPP/acceleratingVoltage
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/epmaTAPP/acceleratingVoltage
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
                                          const: ada:parameter/epmaTAPP/beamDiameter
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/epmaTAPP/beamDiameter
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
                                      description: Probe current in nanoamperes (nA)
                                        used during X-ray mapping.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/epmaTAPP/mappingBeamCurrent
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/epmaTAPP/mappingBeamCurrent
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
                                          const: ada:parameter/epmaTAPP/mappingBeamDiameter
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/epmaTAPP/mappingBeamDiameter
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
                                        in kilovolts (kV). Justify any deviation from
                                        the standard operating voltage.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/epmaTAPP/acceleratingVoltage
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/epmaTAPP/acceleratingVoltage
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
                                          const: ada:parameter/epmaTAPP/beamDiameter
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/epmaTAPP/beamDiameter
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
                                      description: Probe current in nanoamperes (nA)
                                        used during X-ray mapping.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/epmaTAPP/mappingBeamCurrent
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/epmaTAPP/mappingBeamCurrent
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
                                          const: ada:parameter/epmaTAPP/mappingBeamDiameter
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/epmaTAPP/mappingBeamDiameter
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
                    const: ada:parameter/epmaTAPP/beamDamageMinimization
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/epmaTAPP/beamDamageMinimization
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
                    const: ada:parameter/epmaTAPP/beamRasterDimensions
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/epmaTAPP/beamRasterDimensions
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
                    const: ada:parameter/epmaTAPP/driftCorrection
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/epmaTAPP/driftCorrection
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
                    const: ada:parameter/epmaTAPP/edsLiveTimePerPointOrPixel
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/epmaTAPP/edsLiveTimePerPointOrPixel
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
                    const: ada:parameter/epmaTAPP/halogenCorrectionOnOxygen
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/epmaTAPP/halogenCorrectionOnOxygen
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
                    const: ada:parameter/epmaTAPP/stepSizePixelSize
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/epmaTAPP/stepSizePixelSize
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
                    const: ada:parameter/epmaTAPP/beamDamageMinimization
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/epmaTAPP/beamDamageMinimization
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
                    const: ada:parameter/epmaTAPP/beamRasterDimensions
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/epmaTAPP/beamRasterDimensions
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
                    const: ada:parameter/epmaTAPP/driftCorrection
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/epmaTAPP/driftCorrection
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
                    const: ada:parameter/epmaTAPP/edsLiveTimePerPointOrPixel
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/epmaTAPP/edsLiveTimePerPointOrPixel
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
                    const: ada:parameter/epmaTAPP/halogenCorrectionOnOxygen
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/epmaTAPP/halogenCorrectionOnOxygen
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
                    const: ada:parameter/epmaTAPP/stepSizePixelSize
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/epmaTAPP/stepSizePixelSize
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
                  - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml#/$defs/WorkflowStep
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
              const: ada:parameter/epmaTAPP/mapArea
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/epmaTAPP/mapArea
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
              const: ada:parameter/epmaTAPP/mapDimensions
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/epmaTAPP/mapDimensions
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
              const: ada:parameter/epmaTAPP/mapArea
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/epmaTAPP/mapArea
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
              const: ada:parameter/epmaTAPP/mapDimensions
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/epmaTAPP/mapDimensions
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
              const: ada:parameter/epmaTAPP/targetMaterialOfSamplingUnit
            '@type':
              const:
              - schema:PropertyValue
              - cdi:InstanceVariable
            schema:propertyID:
              const:
              - '@id': ada:parameter/epmaTAPP/targetMaterialOfSamplingUnit
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
              const: ada:parameter/epmaTAPP/targetMaterialOfSamplingUnit
            '@type':
              const:
              - schema:PropertyValue
              - cdi:InstanceVariable
            schema:propertyID:
              const:
              - '@id': ada:parameter/epmaTAPP/targetMaterialOfSamplingUnit
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

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/detail/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/detail/schema.yaml)


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
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/EPMA/detail/context.jsonld)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/EPMA/detail`

