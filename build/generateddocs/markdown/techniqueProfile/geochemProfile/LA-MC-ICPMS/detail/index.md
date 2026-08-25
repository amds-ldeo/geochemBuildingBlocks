
# LA-MC-ICP-MS Analysis Detail (Schema)

`ogch.techniqueProfile.geochemProfile.LA-MC-ICPMS.detail` *v0.1*

Dataset-level analysis-instance detail for LA-MC-ICP-MS, reusing CDIF/schema.org slots on the schema:Dataset root.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### detail example Zhang2022
detail instance derived from Zhang et al. 2022 (At. Spectrosc. 43) Lunar meteorite silicates (Rb-Sr geochronology) Line scan (transect) fs-LA-MC-ICP-MS China Univ. of Geosciences.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Zhang2022",
  "@type": [
    "ada:LAICPMSTabular"
  ],
  "ada:componentType": "ada:LAICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laMcicpmsTAPP-Zhang2022"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "CNSA pre-research project D020205; NSFC 41973013; Natural Science Foundation of Hubei Province 2020CFA045; GPMR State Key Laboratory special fund MSFGPMR04 and MSFGPMR08",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": "Variable; analyses of plagioclase, pyroxene, glass in two lunar meteorites (NWA 10597 and NWA 6950); line length varies by mineral grain size",
  "ada:mappingArea": "missing",
  "ada:peakFlatness": "missing",
  "ada:signalIntegrationTime": 60,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "Standard error (USE = SE at 95% confidence) for 87Sr/86Sr and 87Rb/86Sr per individual run; dependent on signal intensity (regression shown in Fig. 3); relative errors for 87Rb/86Sr: ±3% for most reference glasses; 87Sr/86Sr relative errors: <0.2‰ for materials with 87Rb/86Sr <1",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "87Sr/86Sr relative errors <0.2‰ for reference materials with 87Rb/86Sr <1 (12 of 14 reference materials); 87Rb/86Sr relative accuracy within ±3% for 11 glasses; exceptions: NIST 610 (−2.97%), NIST 612 (+2.02%), ATHO-G (+2.89%) — all within stated ±3% criterion",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laMcicpmsTAPP/transectRateMappingRateOrStepSize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laMcicpmsTAPP/transectRateMappingRateOrStepSize"
        }
      ],
      "schema:name": "Transect Rate, Mapping Rate or Step Size",
      "schema:value": "2–6 µm s⁻¹ (varied based on Sr concentration in target minerals)"
    }
  ],
  "ada:spotDiameterMeasured": -9999
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-MC-ICPMS/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Zhang2022",
  "@type": [
    "ada:LAICPMSTabular"
  ],
  "ada:componentType": "ada:LAICPMSTabular",
  "schema:measurementTechnique": [
    {
      "@id": "ex:laMcicpmsTAPP-Zhang2022"
    }
  ],
  "ada:sessionIdentifier": "missing",
  "ada:analyst": "missing",
  "ada:analysisStartDate": "missing",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "CNSA pre-research project D020205; NSFC 41973013; Natural Science Foundation of Hubei Province 2020CFA045; GPMR State Key Laboratory special fund MSFGPMR04 and MSFGPMR08",
  "ada:sampleName": "missing",
  "ada:samplingUnit": "missing",
  "ada:spotDiameter": -9999,
  "ada:oxideProduction": "missing",
  "ada:analysisLocationSpotCoordinates": "missing",
  "ada:numberOfReplicates": -9999,
  "ada:transectLength": "Variable; analyses of plagioclase, pyroxene, glass in two lunar meteorites (NWA 10597 and NWA 6950); line length varies by mineral grain size",
  "ada:mappingArea": "missing",
  "ada:peakFlatness": "missing",
  "ada:signalIntegrationTime": 60,
  "ada:proceduralBlankLevel": "missing",
  "ada:analysisInclusionAndRejectionCriteria": "missing",
  "ada:detectionLimit": -9999,
  "ada:limitOfQuantificationMethod": "missing",
  "ada:countingStatisticsError": "missing",
  "ada:internalAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:withinSessionAnalyticalPrecisionAndAssessmentMethod": "Standard error (USE = SE at 95% confidence) for 87Sr/86Sr and 87Rb/86Sr per individual run; dependent on signal intensity (regression shown in Fig. 3); relative errors for 87Rb/86Sr: \u00b13% for most reference glasses; 87Sr/86Sr relative errors: <0.2\u2030 for materials with 87Rb/86Sr <1",
  "ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod": "missing",
  "ada:analyticalAccuracyAndAssessmentMethod": "87Sr/86Sr relative errors <0.2\u2030 for reference materials with 87Rb/86Sr <1 (12 of 14 reference materials); 87Rb/86Sr relative accuracy within \u00b13% for 11 glasses; exceptions: NIST 610 (\u22122.97%), NIST 612 (+2.02%), ATHO-G (+2.89%) \u2014 all within stated \u00b13% criterion",
  "ada:goodnessOfFitOrDispersionStatistic": "missing",
  "schema:additionalProperty": [
    {
      "@id": "ada:parameter/laMcicpmsTAPP/transectRateMappingRateOrStepSize",
      "@type": [
        "schema:PropertyValue"
      ],
      "schema:propertyID": [
        {
          "@id": "ada:parameter/laMcicpmsTAPP/transectRateMappingRateOrStepSize"
        }
      ],
      "schema:name": "Transect Rate, Mapping Rate or Step Size",
      "schema:value": "2\u20136 \u00b5m s\u207b\u00b9 (varied based on Sr concentration in target minerals)"
    }
  ],
  "ada:spotDiameterMeasured": -9999
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix ex: <https://example.org/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ex:detail-Zhang2022 a ada:LAICPMSTabular ;
    schema1:additionalProperty <https://ada.astromat.org/metadata/parameter/laMcicpmsTAPP/transectRateMappingRateOrStepSize> ;
    schema1:measurementTechnique ex:laMcicpmsTAPP-Zhang2022 ;
    ada:analysisEndDate "missing" ;
    ada:analysisInclusionAndRejectionCriteria "missing" ;
    ada:analysisLocationSpotCoordinates "missing" ;
    ada:analysisStartDate "missing" ;
    ada:analyst "missing" ;
    ada:analyticalAccuracyAndAssessmentMethod "87Sr/86Sr relative errors <0.2‰ for reference materials with 87Rb/86Sr <1 (12 of 14 reference materials); 87Rb/86Sr relative accuracy within ±3% for 11 glasses; exceptions: NIST 610 (−2.97%), NIST 612 (+2.02%), ATHO-G (+2.89%) — all within stated ±3% criterion" ;
    ada:betweenSessionAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:componentType "ada:LAICPMSTabular" ;
    ada:countingStatisticsError "missing" ;
    ada:detectionLimit -9999 ;
    ada:fundingSourceForAnalysis "CNSA pre-research project D020205; NSFC 41973013; Natural Science Foundation of Hubei Province 2020CFA045; GPMR State Key Laboratory special fund MSFGPMR04 and MSFGPMR08" ;
    ada:goodnessOfFitOrDispersionStatistic "missing" ;
    ada:internalAnalyticalPrecisionAndAssessmentMethod "missing" ;
    ada:limitOfQuantificationMethod "missing" ;
    ada:mappingArea "missing" ;
    ada:numberOfReplicates -9999 ;
    ada:oxideProduction "missing" ;
    ada:peakFlatness "missing" ;
    ada:proceduralBlankLevel "missing" ;
    ada:sampleName "missing" ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "missing" ;
    ada:signalIntegrationTime 60 ;
    ada:spotDiameter -9999 ;
    ada:spotDiameterMeasured -9999 ;
    ada:transectLength "Variable; analyses of plagioclase, pyroxene, glass in two lunar meteorites (NWA 10597 and NWA 6950); line length varies by mineral grain size" ;
    ada:withinSessionAnalyticalPrecisionAndAssessmentMethod "Standard error (USE = SE at 95% confidence) for 87Sr/86Sr and 87Rb/86Sr per individual run; dependent on signal intensity (regression shown in Fig. 3); relative errors for 87Rb/86Sr: ±3% for most reference glasses; 87Sr/86Sr relative errors: <0.2‰ for materials with 87Rb/86Sr <1" .

<https://ada.astromat.org/metadata/parameter/laMcicpmsTAPP/transectRateMappingRateOrStepSize> a schema1:PropertyValue ;
    schema1:name "Transect Rate, Mapping Rate or Step Size" ;
    schema1:propertyID <https://ada.astromat.org/metadata/parameter/laMcicpmsTAPP/transectRateMappingRateOrStepSize> ;
    schema1:value "2–6 µm s⁻¹ (varied based on Sr concentration in target minerals)" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: LA-MC-ICP-MS Analysis Detail
description: Dataset-level analysis-instance detail for LA-MC-ICP-MS, reusing CDIF/schema.org
  slots on the schema:Dataset root.
allOf:
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/AnalysisIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/AnalysisIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/AnalysisIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/calibrationFactor/schema.yaml#/$defs/AnalysisIdentification
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
                    schema:additionalProperty:
                      type: array
                      items:
                        anyOf:
                        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_mappedAreaDescription
                        - title: Sample Form / Analytical Substrate
                          description: Physical form of the material as it enters
                            the ablation cell. Editable to accommodate legitimate
                            variations (e.g., thin section vs. mount) that do not
                            alter the analytical procedure.
                          type: object
                          properties:
                            '@id':
                              const: ada:parameter/laMcicpmsTAPP/sampleFormAnalyticalSubstrate
                            '@type':
                              const:
                              - schema:PropertyValue
                            schema:propertyID:
                              const:
                              - '@id': ada:parameter/laMcicpmsTAPP/sampleFormAnalyticalSubstrate
                            schema:name:
                              const: Sample Form / Analytical Substrate
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
                          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_mappedAreaDescription
                        minContains: 0
                        maxContains: 1
                      - contains:
                          title: Sample Form / Analytical Substrate
                          description: Physical form of the material as it enters
                            the ablation cell. Editable to accommodate legitimate
                            variations (e.g., thin section vs. mount) that do not
                            alter the analytical procedure.
                          type: object
                          properties:
                            '@id':
                              const: ada:parameter/laMcicpmsTAPP/sampleFormAnalyticalSubstrate
                            '@type':
                              const:
                              - schema:PropertyValue
                            schema:propertyID:
                              const:
                              - '@id': ada:parameter/laMcicpmsTAPP/sampleFormAnalyticalSubstrate
                            schema:name:
                              const: Sample Form / Analytical Substrate
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
          schema:additionalProperty:
            type: array
            items:
              anyOf:
              - title: Analysis Sequence
                description: Repeating order of primary calibration standard(s), quality
                  control standard(s), and unknown analyses within a measurement session.
                  Editable to allow minor adjustments while maintaining the bracketing
                  strategy defined in the procedure.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laMcicpmsTAPP/analysisSequence
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laMcicpmsTAPP/analysisSequence
                  schema:name:
                    const: Analysis Sequence
                  schema:value:
                    type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - title: Background Count Time
                description: Total time spent measuring gas blank (background signal
                  with laser off or shutter closed) before each ablation event, in
                  seconds. For spot and transect analysis, a discrete background interval
                  is measured before each ablation. For mapping, background is typically
                  measured once per raster line or at the start of a map session rather
                  than before each individual pixel. Editable to allow session-specific
                  adjustment.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laMcicpmsTAPP/backgroundCountTime
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laMcicpmsTAPP/backgroundCountTime
                  schema:name:
                    const: Background Count Time
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
              - title: Carrier Gas and Flow Rate
                description: "Gas used to transport ablated aerosol from the ablation
                  cell to the ICP-MS torch, with the procedure-registered target flow
                  rate(s). Helium is standard for most UV laser systems due to superior
                  aerosol transport. Flow rates are procedure targets; actual session
                  values may be adjusted within \xB110% during tuning."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laMcicpmsTAPP/carrierGasAndFlowRate
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laMcicpmsTAPP/carrierGasAndFlowRate
                  schema:name:
                    const: Carrier Gas and Flow Rate
                  schema:value:
                    type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Analysis_constantsReferenceValues
              - title: Detection Limit
                description: "Session detection limit, one per reported concentration
                  variable (one per analyte, these being the same set), expressed
                  in \xB5g g\u207B\xB9, ng g\u207B\xB9, or wt% as appropriate. Mandatory
                  at analysis level to demonstrate the reliability of reported near-detection-limit
                  concentrations. The calculation method is captured separately in
                  Detection Limit Method."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laMcicpmsTAPP/detectionLimit
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laMcicpmsTAPP/detectionLimit
                  schema:name:
                    const: Detection Limit
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
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Analysis_doubleSpikeMixingRatio
              - title: Mapping Area
                description: "Total area covered by the 2D raster map, expressed as
                  width \xD7 height in \xB5m or as total area in \xB5m\xB2 or mm\xB2.
                  This is an analysis-level parameter because it depends on the size
                  of the grain or phase to be mapped. The procedure fixes scan speed,
                  line spacing, and spot size; the map area is chosen at analysis
                  time to cover the target feature."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laMcicpmsTAPP/mappingArea
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laMcicpmsTAPP/mappingArea
                  schema:name:
                    const: Mapping Area
                  schema:value:
                    type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Analysis_numberOfBlocksPerMeasurement
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Analysis_numberOfCyclesPerBlock
              - title: Number of Replicates
                description: Number of replicate measurements performed on the same
                  sample, or on the same nominal location where the technique is spatially
                  resolved. For spot analysis this is the number of individual spots
                  per grain or location; for transects, the number of replicate lines;
                  for mapping, the number of map acquisitions of the same area; for
                  solution work, the number of discrete replicate measurements acquired
                  per sample solution. The procedure registers an intended count where
                  it has one; the analysis records the count actually acquired.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laMcicpmsTAPP/numberOfReplicates
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laMcicpmsTAPP/numberOfReplicates
                  schema:name:
                    const: Number of Replicates
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
              - title: Make-up Gas and Flow Rate
                description: "Supplementary gas added to the sample-carrying stream
                  between the sample introduction system and the plasma, with its
                  identity and the procedure-registered target flow rate. Argon make-up
                  is standard and maintains total gas delivery where the carrier flow
                  alone is insufficient \u2014 downstream of an ablation cell, or
                  of a desolvation system that has removed solvent load. Small nitrogen
                  or hydrogen additions are also made here to enhance sensitivity
                  for some elements; record them with their own flow, whose unit commonly
                  differs from the make-up flow. Record 'None' explicitly where no
                  supplementary gas is added, to distinguish it from not reported."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laMcicpmsTAPP/makeUpGasAndFlowRate
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laMcicpmsTAPP/makeUpGasAndFlowRate
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
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/targetSelection/schema.yaml#/$defs/Param_Analysis_preAnalysisImagingAndScreening
              - title: Signal Integration Time
                description: 'Actual integration time used for the ablation signal
                  in this analysis, in seconds. This is an analysis-level outcome
                  determined during data reduction by applying the Signal Integration
                  Interval Method to the time-resolved signal. It is equal to or shorter
                  than the Ablation Duration per Spot because the signal start and
                  end transients are typically discarded. Not applicable to mapping
                  analysis: for mapping, the equivalent concept is the per-pixel cycle
                  time, which is determined by the spectrometer dwell time settings
                  (a procedure-level field) rather than being an analysis-level outcome.'
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laMcicpmsTAPP/signalIntegrationTime
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laMcicpmsTAPP/signalIntegrationTime
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
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/targetSelection/schema.yaml#/$defs/Param_Analysis_targetSelectionCriteria
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_transectLength
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_transectRateMappingRateOrStepSize
            allOf:
            - contains:
                title: Analysis Sequence
                description: Repeating order of primary calibration standard(s), quality
                  control standard(s), and unknown analyses within a measurement session.
                  Editable to allow minor adjustments while maintaining the bracketing
                  strategy defined in the procedure.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laMcicpmsTAPP/analysisSequence
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laMcicpmsTAPP/analysisSequence
                  schema:name:
                    const: Analysis Sequence
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
                title: Background Count Time
                description: Total time spent measuring gas blank (background signal
                  with laser off or shutter closed) before each ablation event, in
                  seconds. For spot and transect analysis, a discrete background interval
                  is measured before each ablation. For mapping, background is typically
                  measured once per raster line or at the start of a map session rather
                  than before each individual pixel. Editable to allow session-specific
                  adjustment.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laMcicpmsTAPP/backgroundCountTime
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laMcicpmsTAPP/backgroundCountTime
                  schema:name:
                    const: Background Count Time
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
                title: Carrier Gas and Flow Rate
                description: "Gas used to transport ablated aerosol from the ablation
                  cell to the ICP-MS torch, with the procedure-registered target flow
                  rate(s). Helium is standard for most UV laser systems due to superior
                  aerosol transport. Flow rates are procedure targets; actual session
                  values may be adjusted within \xB110% during tuning."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laMcicpmsTAPP/carrierGasAndFlowRate
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laMcicpmsTAPP/carrierGasAndFlowRate
                  schema:name:
                    const: Carrier Gas and Flow Rate
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
            - contains:
                title: Detection Limit
                description: "Session detection limit, one per reported concentration
                  variable (one per analyte, these being the same set), expressed
                  in \xB5g g\u207B\xB9, ng g\u207B\xB9, or wt% as appropriate. Mandatory
                  at analysis level to demonstrate the reliability of reported near-detection-limit
                  concentrations. The calculation method is captured separately in
                  Detection Limit Method."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laMcicpmsTAPP/detectionLimit
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laMcicpmsTAPP/detectionLimit
                  schema:name:
                    const: Detection Limit
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
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Analysis_doubleSpikeMixingRatio
              minContains: 0
              maxContains: 1
            - contains:
                title: Mapping Area
                description: "Total area covered by the 2D raster map, expressed as
                  width \xD7 height in \xB5m or as total area in \xB5m\xB2 or mm\xB2.
                  This is an analysis-level parameter because it depends on the size
                  of the grain or phase to be mapped. The procedure fixes scan speed,
                  line spacing, and spot size; the map area is chosen at analysis
                  time to cover the target feature."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laMcicpmsTAPP/mappingArea
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laMcicpmsTAPP/mappingArea
                  schema:name:
                    const: Mapping Area
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
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Analysis_numberOfBlocksPerMeasurement
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/mcIcpms/schema.yaml#/$defs/Param_Analysis_numberOfCyclesPerBlock
              minContains: 0
              maxContains: 1
            - contains:
                title: Number of Replicates
                description: Number of replicate measurements performed on the same
                  sample, or on the same nominal location where the technique is spatially
                  resolved. For spot analysis this is the number of individual spots
                  per grain or location; for transects, the number of replicate lines;
                  for mapping, the number of map acquisitions of the same area; for
                  solution work, the number of discrete replicate measurements acquired
                  per sample solution. The procedure registers an intended count where
                  it has one; the analysis records the count actually acquired.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laMcicpmsTAPP/numberOfReplicates
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laMcicpmsTAPP/numberOfReplicates
                  schema:name:
                    const: Number of Replicates
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
                title: Make-up Gas and Flow Rate
                description: "Supplementary gas added to the sample-carrying stream
                  between the sample introduction system and the plasma, with its
                  identity and the procedure-registered target flow rate. Argon make-up
                  is standard and maintains total gas delivery where the carrier flow
                  alone is insufficient \u2014 downstream of an ablation cell, or
                  of a desolvation system that has removed solvent load. Small nitrogen
                  or hydrogen additions are also made here to enhance sensitivity
                  for some elements; record them with their own flow, whose unit commonly
                  differs from the make-up flow. Record 'None' explicitly where no
                  supplementary gas is added, to distinguish it from not reported."
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laMcicpmsTAPP/makeUpGasAndFlowRate
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laMcicpmsTAPP/makeUpGasAndFlowRate
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
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/targetSelection/schema.yaml#/$defs/Param_Analysis_preAnalysisImagingAndScreening
              minContains: 0
              maxContains: 1
            - contains:
                title: Signal Integration Time
                description: 'Actual integration time used for the ablation signal
                  in this analysis, in seconds. This is an analysis-level outcome
                  determined during data reduction by applying the Signal Integration
                  Interval Method to the time-resolved signal. It is equal to or shorter
                  than the Ablation Duration per Spot because the signal start and
                  end transients are typically discarded. Not applicable to mapping
                  analysis: for mapping, the equivalent concept is the per-pixel cycle
                  time, which is determined by the spectrometer dwell time settings
                  (a procedure-level field) rather than being an analysis-level outcome.'
                type: object
                properties:
                  '@id':
                    const: ada:parameter/laMcicpmsTAPP/signalIntegrationTime
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/laMcicpmsTAPP/signalIntegrationTime
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
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/targetSelection/schema.yaml#/$defs/Param_Analysis_targetSelectionCriteria
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_transectLength
              minContains: 0
              maxContains: 1
            - contains:
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_transectRateMappingRateOrStepSize
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
                                              - title: Auxiliary Gas Flow Rate
                                                description: Flow rate of the intermediate
                                                  (auxiliary) argon gas stream that
                                                  positions the plasma relative to
                                                  the load coil, in L/min. Affects
                                                  ion extraction efficiency and oxide
                                                  production rates. Distinct from
                                                  the carrier gas (which transports
                                                  ablation aerosol) and the coolant
                                                  (plasma) gas.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/laMcicpmsTAPP/auxiliaryGasFlowRate
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/laMcicpmsTAPP/auxiliaryGasFlowRate
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
                                              - title: Coolant (Plasma) Gas Flow Rate
                                                description: Flow rate of the outer
                                                  (coolant/plasma) argon gas stream
                                                  that sustains the ICP plasma, in
                                                  L/min. Determines plasma volume
                                                  and stability. Set during initial
                                                  plasma optimisation and confirmed
                                                  at each session start.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/laMcicpmsTAPP/coolantGasFlowRate
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/laMcicpmsTAPP/coolantGasFlowRate
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
                                              - title: RF Power
                                                description: ICP radiofrequency forward
                                                  power in watts. Affects plasma temperature,
                                                  ionisation efficiency, oxide formation,
                                                  and whether cool or normal plasma
                                                  conditions are in effect. The procedure
                                                  registers a target value optimised
                                                  during initial setup; the analyst
                                                  confirms or fine-adjusts during
                                                  session tuning.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/laMcicpmsTAPP/rfPower
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/laMcicpmsTAPP/rfPower
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
                                            allOf:
                                            - contains:
                                                title: Auxiliary Gas Flow Rate
                                                description: Flow rate of the intermediate
                                                  (auxiliary) argon gas stream that
                                                  positions the plasma relative to
                                                  the load coil, in L/min. Affects
                                                  ion extraction efficiency and oxide
                                                  production rates. Distinct from
                                                  the carrier gas (which transports
                                                  ablation aerosol) and the coolant
                                                  (plasma) gas.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/laMcicpmsTAPP/auxiliaryGasFlowRate
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/laMcicpmsTAPP/auxiliaryGasFlowRate
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
                                            - contains:
                                                title: Coolant (Plasma) Gas Flow Rate
                                                description: Flow rate of the outer
                                                  (coolant/plasma) argon gas stream
                                                  that sustains the ICP plasma, in
                                                  L/min. Determines plasma volume
                                                  and stability. Set during initial
                                                  plasma optimisation and confirmed
                                                  at each session start.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/laMcicpmsTAPP/coolantGasFlowRate
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/laMcicpmsTAPP/coolantGasFlowRate
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
                                                title: RF Power
                                                description: ICP radiofrequency forward
                                                  power in watts. Affects plasma temperature,
                                                  ionisation efficiency, oxide formation,
                                                  and whether cool or normal plasma
                                                  conditions are in effect. The procedure
                                                  registers a target value optimised
                                                  during initial setup; the analyst
                                                  confirms or fine-adjusts during
                                                  session tuning.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/laMcicpmsTAPP/rfPower
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/laMcicpmsTAPP/rfPower
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
                                              - title: Cell Exit Discrimination Voltage
                                                description: Bias voltage applied
                                                  at the collision/reaction cell exit
                                                  to discriminate between analyte
                                                  ions and low-energy polyatomic interferences
                                                  in KED mode, in volts (V). A negative
                                                  bias preferentially retards slow
                                                  polyatomic ions while transmitting
                                                  faster analyte ions. Record 'None'
                                                  if the CRC is in STD mode. Record
                                                  'N/A' where Collision/Reaction Cell
                                                  (CRC) Configuration does not include
                                                  KED.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/laMcicpmsTAPP/cellExitDiscriminationVoltage
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/laMcicpmsTAPP/cellExitDiscriminationVoltage
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
                                              - title: Collision Gas Flow Rate
                                                description: Flow rate of the collision
                                                  gas (typically He) introduced into
                                                  the collision/reaction cell, in
                                                  mL/min. Controls the degree of ion
                                                  thermalization and KED efficiency.
                                                  Record 'None' if the CRC is in STD
                                                  mode. Record 'N/A' where Collision/Reaction
                                                  Cell (CRC) Configuration does not
                                                  include KED.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/laMcicpmsTAPP/collisionGasFlowRate
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/laMcicpmsTAPP/collisionGasFlowRate
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
                                              - title: Reaction Gas Flow Rate
                                                description: Flow rate of the reactive
                                                  gas introduced into the dynamic
                                                  reaction cell (DRC), in mL/min.
                                                  Record 'N/A' where Collision/Reaction
                                                  Cell (CRC) Configuration does not
                                                  include DRC.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/laMcicpmsTAPP/reactionGasFlowRate
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/laMcicpmsTAPP/reactionGasFlowRate
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
                                                title: Cell Exit Discrimination Voltage
                                                description: Bias voltage applied
                                                  at the collision/reaction cell exit
                                                  to discriminate between analyte
                                                  ions and low-energy polyatomic interferences
                                                  in KED mode, in volts (V). A negative
                                                  bias preferentially retards slow
                                                  polyatomic ions while transmitting
                                                  faster analyte ions. Record 'None'
                                                  if the CRC is in STD mode. Record
                                                  'N/A' where Collision/Reaction Cell
                                                  (CRC) Configuration does not include
                                                  KED.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/laMcicpmsTAPP/cellExitDiscriminationVoltage
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/laMcicpmsTAPP/cellExitDiscriminationVoltage
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
                                                title: Collision Gas Flow Rate
                                                description: Flow rate of the collision
                                                  gas (typically He) introduced into
                                                  the collision/reaction cell, in
                                                  mL/min. Controls the degree of ion
                                                  thermalization and KED efficiency.
                                                  Record 'None' if the CRC is in STD
                                                  mode. Record 'N/A' where Collision/Reaction
                                                  Cell (CRC) Configuration does not
                                                  include KED.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/laMcicpmsTAPP/collisionGasFlowRate
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/laMcicpmsTAPP/collisionGasFlowRate
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
                                                title: Reaction Gas Flow Rate
                                                description: Flow rate of the reactive
                                                  gas introduced into the dynamic
                                                  reaction cell (DRC), in mL/min.
                                                  Record 'N/A' where Collision/Reaction
                                                  Cell (CRC) Configuration does not
                                                  include DRC.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:parameter/laMcicpmsTAPP/reactionGasFlowRate
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/laMcicpmsTAPP/reactionGasFlowRate
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
                                    - if:
                                        properties:
                                          schema:additionalType:
                                            contains:
                                              const: Collector
                                            schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                                        required:
                                        - schema:additionalType
                                      then:
                                        properties:
                                          ada:collectorConfiguration:
                                            type: array
                                            items:
                                              anyOf:
                                              - title: Integration Time per Cycle
                                                description: "Duration of signal integration
                                                  per measurement cycle (seconds).
                                                  Determines counting statistics per
                                                  cycle. Longer integration times
                                                  improve shot-noise precision but
                                                  increase the impact of signal drift
                                                  within the integration window. For
                                                  high-gain (10\xB9\xB2 or 10\xB9\xB3
                                                  \u03A9) amplifier channels, longer
                                                  integration times are often required
                                                  to accumulate sufficient charge.
                                                  Procedure specifies the standard
                                                  integration time; analyst may confirm
                                                  or adjust within procedure bounds.
                                                  Where different isotope channels
                                                  use different integration schemes,
                                                  record the time for each channel."
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:channelColumn/laMcicpmsTAPP/integrationTimePerCycle
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:channelColumn/laMcicpmsTAPP/integrationTimePerCycle
                                                  schema:name:
                                                    const: Integration Time per Cycle
                                                  ada:dataType:
                                                    const: number
                                                  ada:tier:
                                                    const: M
                                                  schema:value:
                                                    anyOf:
                                                    - anyOf:
                                                      - type: number
                                                      - type: string
                                                    - type: array
                                                      items:
                                                        anyOf:
                                                        - type: number
                                                        - type: string
                                                required:
                                                - '@id'
                                                - '@type'
                                                - schema:propertyID
                                                - schema:name
                                                - ada:dataType
                                                - schema:value
                                              - title: Ion Counter Dead Time
                                                description: Dead time of each ion-counting
                                                  detector channel, used in the dead-time
                                                  correction applied to high count
                                                  rates. Distinct from pulse/analog
                                                  cross-calibration, which relates
                                                  the two detector modes rather than
                                                  correcting counting losses within
                                                  the pulse-counting mode.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:channelColumn/laMcicpmsTAPP/ionCounterDeadTime
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:channelColumn/laMcicpmsTAPP/ionCounterDeadTime
                                                  schema:name:
                                                    const: Ion Counter Dead Time
                                                  ada:dataType:
                                                    const: number
                                                  ada:tier:
                                                    const: M
                                                  schema:value:
                                                    anyOf:
                                                    - anyOf:
                                                      - type: number
                                                      - type: string
                                                    - type: array
                                                      items:
                                                        anyOf:
                                                        - type: number
                                                        - type: string
                                                required:
                                                - '@id'
                                                - '@type'
                                                - schema:propertyID
                                                - schema:name
                                                - ada:dataType
                                                - schema:value
                                            allOf:
                                            - contains:
                                                title: Integration Time per Cycle
                                                description: "Duration of signal integration
                                                  per measurement cycle (seconds).
                                                  Determines counting statistics per
                                                  cycle. Longer integration times
                                                  improve shot-noise precision but
                                                  increase the impact of signal drift
                                                  within the integration window. For
                                                  high-gain (10\xB9\xB2 or 10\xB9\xB3
                                                  \u03A9) amplifier channels, longer
                                                  integration times are often required
                                                  to accumulate sufficient charge.
                                                  Procedure specifies the standard
                                                  integration time; analyst may confirm
                                                  or adjust within procedure bounds.
                                                  Where different isotope channels
                                                  use different integration schemes,
                                                  record the time for each channel."
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:channelColumn/laMcicpmsTAPP/integrationTimePerCycle
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:channelColumn/laMcicpmsTAPP/integrationTimePerCycle
                                                  schema:name:
                                                    const: Integration Time per Cycle
                                                  ada:dataType:
                                                    const: number
                                                  ada:tier:
                                                    const: M
                                                  schema:value:
                                                    anyOf:
                                                    - anyOf:
                                                      - type: number
                                                      - type: string
                                                    - type: array
                                                      items:
                                                        anyOf:
                                                        - type: number
                                                        - type: string
                                                required:
                                                - '@id'
                                                - '@type'
                                                - schema:propertyID
                                                - schema:name
                                                - ada:dataType
                                                - schema:value
                                              minContains: 0
                                              maxContains: 1
                                            - contains:
                                                title: Ion Counter Dead Time
                                                description: Dead time of each ion-counting
                                                  detector channel, used in the dead-time
                                                  correction applied to high count
                                                  rates. Distinct from pulse/analog
                                                  cross-calibration, which relates
                                                  the two detector modes rather than
                                                  correcting counting losses within
                                                  the pulse-counting mode.
                                                type: object
                                                properties:
                                                  '@id':
                                                    const: ada:channelColumn/laMcicpmsTAPP/ionCounterDeadTime
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:channelColumn/laMcicpmsTAPP/ionCounterDeadTime
                                                  schema:name:
                                                    const: Ion Counter Dead Time
                                                  ada:dataType:
                                                    const: number
                                                  ada:tier:
                                                    const: M
                                                  schema:value:
                                                    anyOf:
                                                    - anyOf:
                                                      - type: number
                                                      - type: string
                                                    - type: array
                                                      items:
                                                        anyOf:
                                                        - type: number
                                                        - type: string
                                                required:
                                                - '@id'
                                                - '@type'
                                                - schema:propertyID
                                                - schema:name
                                                - ada:dataType
                                                - schema:value
                                              minContains: 0
                                              maxContains: 1
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
                                                  const: ada:parameter/laMcicpmsTAPP/torchDepth
                                                '@type':
                                                  const:
                                                  - schema:PropertyValue
                                                schema:propertyID:
                                                  const:
                                                  - '@id': ada:parameter/laMcicpmsTAPP/torchDepth
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
                                                    const: ada:parameter/laMcicpmsTAPP/torchDepth
                                                  '@type':
                                                    const:
                                                    - schema:PropertyValue
                                                  schema:propertyID:
                                                    const:
                                                    - '@id': ada:parameter/laMcicpmsTAPP/torchDepth
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
                                  allOf:
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
                                  - contains:
                                      properties:
                                        schema:additionalType:
                                          contains:
                                            const: Collector
                                          schema:inDefinedTermSet: ada:vocab/instrumentComponentType
                                      required:
                                      - schema:additionalType
                                schema:additionalProperty:
                                  type: array
                                  items:
                                    anyOf:
                                    - title: Doubly-Charged Species Monitor
                                      description: "The mass ratio monitored to estimate
                                        doubly-charged ion (M\xB2\u207A) formation
                                        during instrument tuning. Doubly-charged ions
                                        appear at half the mass of the parent ion
                                        and can cause isobaric interferences on analytes
                                        in that mass region. The monitor species and
                                        the mass positions monitored should be stated
                                        explicitly. Analogous to Oxide Production
                                        Method and Threshold for oxide monitoring."
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/laMcicpmsTAPP/doublyChargedSpeciesMonitor
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/laMcicpmsTAPP/doublyChargedSpeciesMonitor
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
                                        the time of instrument tuning. The procedure
                                        should specify the acceptable threshold (e.g.,
                                        <1%, <3%); the measured value for each session
                                        is recorded here. Report both the threshold
                                        and the measured value where possible.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/laMcicpmsTAPP/doublyChargedSpeciesProduction
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/laMcicpmsTAPP/doublyChargedSpeciesProduction
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
                                    - title: ICP Tuning
                                      description: Description of the approach used
                                        to optimise ICP plasma conditions prior to
                                        analysis, including the reference material
                                        used for tuning and the acceptance criteria
                                        (e.g., oxide production threshold, sensitivity
                                        targets, mass calibration).
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/laMcicpmsTAPP/icpTuning
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/laMcicpmsTAPP/icpTuning
                                        schema:name:
                                          const: ICP Tuning
                                        schema:value:
                                          type: string
                                      required:
                                      - '@id'
                                      - '@type'
                                      - schema:propertyID
                                      - schema:name
                                      - schema:value
                                    - title: Mass Resolution Setting
                                      description: Operating mass resolution of the
                                        mass analyser. For quadrupole instruments
                                        this is fixed at unit resolution by instrument
                                        design. For sector-field instruments the analyst
                                        selects low, medium, or high resolution to
                                        balance sensitivity against spectral interference
                                        suppression.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/laMcicpmsTAPP/massResolutionSetting
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/laMcicpmsTAPP/massResolutionSetting
                                        schema:name:
                                          const: Mass Resolution Setting
                                        schema:value:
                                          type: string
                                      required:
                                      - '@id'
                                      - '@type'
                                      - schema:propertyID
                                      - schema:name
                                      - schema:value
                                    - title: Memory Effect Mitigation
                                      description: Procedure applied to identify and
                                        minimise memory effects from high-concentration
                                        elements in the previous sample or standard
                                        that may contaminate subsequent analyses,
                                        or from incomplete aerosol washout between
                                        adjacent pixels in raster mapping mode. For
                                        mapping, the mitigation strategy involves
                                        controlling scan speed relative to washout
                                        time to ensure each pixel signal is sufficiently
                                        free of the preceding pixel's contribution.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/laMcicpmsTAPP/memoryEffectMitigation
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/laMcicpmsTAPP/memoryEffectMitigation
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
                                      title: Doubly-Charged Species Monitor
                                      description: "The mass ratio monitored to estimate
                                        doubly-charged ion (M\xB2\u207A) formation
                                        during instrument tuning. Doubly-charged ions
                                        appear at half the mass of the parent ion
                                        and can cause isobaric interferences on analytes
                                        in that mass region. The monitor species and
                                        the mass positions monitored should be stated
                                        explicitly. Analogous to Oxide Production
                                        Method and Threshold for oxide monitoring."
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/laMcicpmsTAPP/doublyChargedSpeciesMonitor
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/laMcicpmsTAPP/doublyChargedSpeciesMonitor
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
                                        the time of instrument tuning. The procedure
                                        should specify the acceptable threshold (e.g.,
                                        <1%, <3%); the measured value for each session
                                        is recorded here. Report both the threshold
                                        and the measured value where possible.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/laMcicpmsTAPP/doublyChargedSpeciesProduction
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/laMcicpmsTAPP/doublyChargedSpeciesProduction
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
                                  - contains:
                                      title: ICP Tuning
                                      description: Description of the approach used
                                        to optimise ICP plasma conditions prior to
                                        analysis, including the reference material
                                        used for tuning and the acceptance criteria
                                        (e.g., oxide production threshold, sensitivity
                                        targets, mass calibration).
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/laMcicpmsTAPP/icpTuning
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/laMcicpmsTAPP/icpTuning
                                        schema:name:
                                          const: ICP Tuning
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
                                      title: Mass Resolution Setting
                                      description: Operating mass resolution of the
                                        mass analyser. For quadrupole instruments
                                        this is fixed at unit resolution by instrument
                                        design. For sector-field instruments the analyst
                                        selects low, medium, or high resolution to
                                        balance sensitivity against spectral interference
                                        suppression.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/laMcicpmsTAPP/massResolutionSetting
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/laMcicpmsTAPP/massResolutionSetting
                                        schema:name:
                                          const: Mass Resolution Setting
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
                                      title: Memory Effect Mitigation
                                      description: Procedure applied to identify and
                                        minimise memory effects from high-concentration
                                        elements in the previous sample or standard
                                        that may contaminate subsequent analyses,
                                        or from incomplete aerosol washout between
                                        adjacent pixels in raster mapping mode. For
                                        mapping, the mitigation strategy involves
                                        controlling scan speed relative to washout
                                        time to ensure each pixel signal is sufficiently
                                        free of the preceding pixel's contribution.
                                      type: object
                                      properties:
                                        '@id':
                                          const: ada:parameter/laMcicpmsTAPP/memoryEffectMitigation
                                        '@type':
                                          const:
                                          - schema:PropertyValue
                                        schema:propertyID:
                                          const:
                                          - '@id': ada:parameter/laMcicpmsTAPP/memoryEffectMitigation
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
                                schema:identifier:
                                  description: Serial number or laboratory-internal
                                    identifier for the specific instrument unit. Supports
                                    traceability to instrument service records.
                                  anyOf:
                                  - type: string
                                  - type: array
                                    items:
                                      type: string
                          - if:
                              properties:
                                schema:additionalType:
                                  contains:
                                    const: Laser Ablation System
                                  schema:inDefinedTermSet: ada:vocab/instrumentType
                              required:
                              - schema:additionalType
                            then:
                              properties:
                                schema:additionalProperty:
                                  type: array
                                  items:
                                    $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_laserEnergy
                                  allOf:
                                  - contains:
                                      $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_laserEnergy
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
                                  description: Primary reference material(s) used
                                    to calibrate the instrument and convert raw signal
                                    intensities to concentrations or isotope ratios.
                                    Include material name, source institution, and
                                    citation for the accepted values used. Editable
                                    because the specific lot or certification vintage
                                    may differ between sessions while the material
                                    type remains the same.
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
                                  description: Quality-control reference materials
                                    analysed as unknowns alongside samples in the
                                    same session to assess accuracy and monitor drift.
                                    Include material name, source, and citation for
                                    accepted values used for comparison. Editable
                                    because selection of secondary RMs may vary across
                                    sessions.
                                  anyOf:
                                  - type: string
                                  - type: array
                                    items:
                                      type: string
                          required:
                          - ada:reagentRole
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
                            - title: Fusion Flux and Dilution Ratio
                              description: For procedures using fused glass, the flux
                                type and sample:flux dilution ratio used to prepare
                                the analytical glass.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laMcicpmsTAPP/fusionFluxAndDilutionRatio
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laMcicpmsTAPP/fusionFluxAndDilutionRatio
                                schema:name:
                                  const: Fusion Flux and Dilution Ratio
                                schema:value:
                                  type: string
                              required:
                              - '@id'
                              - '@type'
                              - schema:propertyID
                              - schema:name
                              - schema:value
                            - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_preAblationSurfaceTreatment
                          allOf:
                          - contains:
                              title: Fusion Flux and Dilution Ratio
                              description: For procedures using fused glass, the flux
                                type and sample:flux dilution ratio used to prepare
                                the analytical glass.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laMcicpmsTAPP/fusionFluxAndDilutionRatio
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laMcicpmsTAPP/fusionFluxAndDilutionRatio
                                schema:name:
                                  const: Fusion Flux and Dilution Ratio
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
                              $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/laserAblation/schema.yaml#/$defs/Param_Analysis_preAblationSurfaceTreatment
                            minContains: 0
                            maxContains: 1
                        schema:description:
                          description: Description of how samples were prepared for
                            analysis (mounting, polishing, coating, fusion procedure,
                            etc.).
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
                              description: Any post-acquisition normalization applied
                                to correct for systematic biases identified from secondary
                                reference materials, or stoichiometric normalization
                                applied per pixel in mapping. Distinct from the primary
                                internal standard approach captured in Internal Standard
                                Approach.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laMcicpmsTAPP/normalizationStandardsBasedCorrection
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laMcicpmsTAPP/normalizationStandardsBasedCorrection
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
                            - title: Signal Smoothing
                              description: 'Description of any signal smoothing device
                                or approach installed between the ablation cell and
                                the ICP-MS to reduce pulse-to-pulse signal variability.
                                Note: active signal smoothing devices (e.g., squid,
                                SCFAST) are generally incompatible with high-resolution
                                raster mapping because they degrade spatial resolution
                                by mixing aerosol from successive laser shots. For
                                mapping analyses, report "None" explicitly.'
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laMcicpmsTAPP/signalSmoothing
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laMcicpmsTAPP/signalSmoothing
                                schema:name:
                                  const: Signal Smoothing
                                schema:value:
                                  type: string
                              required:
                              - '@id'
                              - '@type'
                              - schema:propertyID
                              - schema:name
                              - schema:value
                            - title: Spike / Outlier Filtering Approach
                              description: Method used to identify and remove anomalous
                                signal spikes arising from micronuggets, inclusions,
                                cracks, or instrument artifacts during time-resolved
                                signal processing. Editable because the specific implementation
                                may vary between sessions while remaining within the
                                procedure framework.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laMcicpmsTAPP/spikeOutlierFilteringApproach
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laMcicpmsTAPP/spikeOutlierFilteringApproach
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
                                  const: ada:parameter/laMcicpmsTAPP/uncertaintyPropagationMethod
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laMcicpmsTAPP/uncertaintyPropagationMethod
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
                          allOf:
                          - contains:
                              title: Normalization / Standards-Based Correction
                              description: Any post-acquisition normalization applied
                                to correct for systematic biases identified from secondary
                                reference materials, or stoichiometric normalization
                                applied per pixel in mapping. Distinct from the primary
                                internal standard approach captured in Internal Standard
                                Approach.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laMcicpmsTAPP/normalizationStandardsBasedCorrection
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laMcicpmsTAPP/normalizationStandardsBasedCorrection
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
                              title: Signal Smoothing
                              description: 'Description of any signal smoothing device
                                or approach installed between the ablation cell and
                                the ICP-MS to reduce pulse-to-pulse signal variability.
                                Note: active signal smoothing devices (e.g., squid,
                                SCFAST) are generally incompatible with high-resolution
                                raster mapping because they degrade spatial resolution
                                by mixing aerosol from successive laser shots. For
                                mapping analyses, report "None" explicitly.'
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laMcicpmsTAPP/signalSmoothing
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laMcicpmsTAPP/signalSmoothing
                                schema:name:
                                  const: Signal Smoothing
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
                              title: Spike / Outlier Filtering Approach
                              description: Method used to identify and remove anomalous
                                signal spikes arising from micronuggets, inclusions,
                                cracks, or instrument artifacts during time-resolved
                                signal processing. Editable because the specific implementation
                                may vary between sessions while remaining within the
                                procedure framework.
                              type: object
                              properties:
                                '@id':
                                  const: ada:parameter/laMcicpmsTAPP/spikeOutlierFilteringApproach
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laMcicpmsTAPP/spikeOutlierFilteringApproach
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
                                  const: ada:parameter/laMcicpmsTAPP/uncertaintyPropagationMethod
                                '@type':
                                  const:
                                  - schema:PropertyValue
                                schema:propertyID:
                                  const:
                                  - '@id': ada:parameter/laMcicpmsTAPP/uncertaintyPropagationMethod
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
                allOf:
                - contains:
                    properties:
                      schema:name:
                        const: Sample preparation
                    required:
                    - schema:name
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
        - title: Detection Limit
          description: "Session detection limit, one per reported concentration variable
            (one per analyte, these being the same set), expressed in \xB5g g\u207B\xB9,
            ng g\u207B\xB9, or wt% as appropriate. Mandatory at analysis level to
            demonstrate the reliability of reported near-detection-limit concentrations.
            The calculation method is captured separately in Detection Limit Method."
          type: object
          properties:
            '@id':
              const: ada:parameter/laMcicpmsTAPP/detectionLimit
            '@type':
              const:
              - schema:PropertyValue
              - cdi:InstanceVariable
            schema:propertyID:
              const:
              - '@id': ada:parameter/laMcicpmsTAPP/detectionLimit
            schema:name:
              const: Detection Limit
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
        - title: Detection Limit Method
          description: Reference or description of the method used to calculate session
            detection limits. Mandatory at analysis level. Must be consistent with
            the method applied to generate the Detection Limit values reported above.
          type: object
          properties:
            '@id':
              const: ada:parameter/laMcicpmsTAPP/detectionLimitMethod
            '@type':
              const:
              - schema:PropertyValue
              - cdi:InstanceVariable
            schema:propertyID:
              const:
              - '@id': ada:parameter/laMcicpmsTAPP/detectionLimitMethod
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
        - title: Limit of Quantification (LOQ) Method
          description: 'Reference or description of the method used to calculate the
            limit of quantification (LOQ): the lowest concentration reliably measurable
            with acceptable precision and accuracy. Mandatory at analysis level when
            concentrations near the LOD are reported. Concentrations between LOD and
            LOQ are detectable but not reliably quantifiable.'
          type: object
          properties:
            '@id':
              const: ada:parameter/laMcicpmsTAPP/limitOfQuantificationMethod
            '@type':
              const:
              - schema:PropertyValue
              - cdi:InstanceVariable
            schema:propertyID:
              const:
              - '@id': ada:parameter/laMcicpmsTAPP/limitOfQuantificationMethod
            schema:name:
              const: Limit of Quantification (LOQ) Method
            schema:value:
              type: string
          required:
          - '@id'
          - '@type'
          - schema:propertyID
          - schema:name
          - schema:value
        - title: Normalization / Standards-Based Correction
          description: Any post-acquisition normalization applied to correct for systematic
            biases identified from secondary reference materials, or stoichiometric
            normalization applied per pixel in mapping. Distinct from the primary
            internal standard approach captured in Internal Standard Approach.
          type: object
          properties:
            '@id':
              const: ada:parameter/laMcicpmsTAPP/normalizationStandardsBasedCorrection
            '@type':
              const:
              - schema:PropertyValue
              - cdi:InstanceVariable
            schema:propertyID:
              const:
              - '@id': ada:parameter/laMcicpmsTAPP/normalizationStandardsBasedCorrection
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
        - title: Uncertainty Propagation Method
          description: 'The approach used to propagate analytical uncertainty through
            the data reduction chain to the final reported value. State which sources
            are included in the propagation: counting statistics, calibration standard
            uncertainty, internal standard uncertainty, drift correction, and any
            systematic contributions. Distinct from Uncertainty Level, which states
            the convention at which the resulting uncertainty is quoted.'
          type: object
          properties:
            '@id':
              const: ada:parameter/laMcicpmsTAPP/uncertaintyPropagationMethod
            '@type':
              const:
              - schema:PropertyValue
              - cdi:InstanceVariable
            schema:propertyID:
              const:
              - '@id': ada:parameter/laMcicpmsTAPP/uncertaintyPropagationMethod
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
      allOf:
      - contains:
          title: Detection Limit
          description: "Session detection limit, one per reported concentration variable
            (one per analyte, these being the same set), expressed in \xB5g g\u207B\xB9,
            ng g\u207B\xB9, or wt% as appropriate. Mandatory at analysis level to
            demonstrate the reliability of reported near-detection-limit concentrations.
            The calculation method is captured separately in Detection Limit Method."
          type: object
          properties:
            '@id':
              const: ada:parameter/laMcicpmsTAPP/detectionLimit
            '@type':
              const:
              - schema:PropertyValue
              - cdi:InstanceVariable
            schema:propertyID:
              const:
              - '@id': ada:parameter/laMcicpmsTAPP/detectionLimit
            schema:name:
              const: Detection Limit
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
          title: Detection Limit Method
          description: Reference or description of the method used to calculate session
            detection limits. Mandatory at analysis level. Must be consistent with
            the method applied to generate the Detection Limit values reported above.
          type: object
          properties:
            '@id':
              const: ada:parameter/laMcicpmsTAPP/detectionLimitMethod
            '@type':
              const:
              - schema:PropertyValue
              - cdi:InstanceVariable
            schema:propertyID:
              const:
              - '@id': ada:parameter/laMcicpmsTAPP/detectionLimitMethod
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
          title: Limit of Quantification (LOQ) Method
          description: 'Reference or description of the method used to calculate the
            limit of quantification (LOQ): the lowest concentration reliably measurable
            with acceptable precision and accuracy. Mandatory at analysis level when
            concentrations near the LOD are reported. Concentrations between LOD and
            LOQ are detectable but not reliably quantifiable.'
          type: object
          properties:
            '@id':
              const: ada:parameter/laMcicpmsTAPP/limitOfQuantificationMethod
            '@type':
              const:
              - schema:PropertyValue
              - cdi:InstanceVariable
            schema:propertyID:
              const:
              - '@id': ada:parameter/laMcicpmsTAPP/limitOfQuantificationMethod
            schema:name:
              const: Limit of Quantification (LOQ) Method
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
          description: Any post-acquisition normalization applied to correct for systematic
            biases identified from secondary reference materials, or stoichiometric
            normalization applied per pixel in mapping. Distinct from the primary
            internal standard approach captured in Internal Standard Approach.
          type: object
          properties:
            '@id':
              const: ada:parameter/laMcicpmsTAPP/normalizationStandardsBasedCorrection
            '@type':
              const:
              - schema:PropertyValue
              - cdi:InstanceVariable
            schema:propertyID:
              const:
              - '@id': ada:parameter/laMcicpmsTAPP/normalizationStandardsBasedCorrection
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
          title: Uncertainty Propagation Method
          description: 'The approach used to propagate analytical uncertainty through
            the data reduction chain to the final reported value. State which sources
            are included in the propagation: counting statistics, calibration standard
            uncertainty, internal standard uncertainty, drift correction, and any
            systematic contributions. Distinct from Uncertainty Level, which states
            the convention at which the resulting uncertainty is quoted.'
          type: object
          properties:
            '@id':
              const: ada:parameter/laMcicpmsTAPP/uncertaintyPropagationMethod
            '@type':
              const:
              - schema:PropertyValue
              - cdi:InstanceVariable
            schema:propertyID:
              const:
              - '@id': ada:parameter/laMcicpmsTAPP/uncertaintyPropagationMethod
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

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-MC-ICPMS/detail/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-MC-ICPMS/detail/schema.yaml)


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
    "dqv": "http://www.w3.org/ns/dqv#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/LA-MC-ICPMS/detail/context.jsonld)

## Sources

* [LA-MC-ICPMS_TAPP_v13.csv (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/LA-MC-ICPMS/detail`

