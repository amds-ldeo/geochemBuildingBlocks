
# VNMIR Analysis Detail (Schema)

`ogch.techniqueProfile.geochemProfile.VNMIR.detail` *v0.1*

Detail block for VNMIR hasPart items. Discriminates on ada:componentType and carries the analysis-level properties - viewing geometry, sample state and per-measurement results - that are supplied per measurement rather than fixed by the procedure.

[*Status*](http://www.opengis.net/def/status): Under development

## Examples

### detail example Hiroi2023
detail instance derived from ADA n=19 | Hiroi2023 | Brown U. | Thermo/Nicolet Nexus 870 FTIR.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Hiroi2023",
  "@type": [
    "ada:VNMIRSpectralPoint"
  ],
  "ada:componentType": "ada:VNMIRSpectralPoint",
  "schema:measurementTechnique": [
    {
      "@id": "ex:vnmirTAPP-Hiroi2023",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "20240514_vnmir_brown_orex-803124-0_1 | 20240918_vnmir_brown_orex-803119-100_1 | (+8 more)",
  "ada:analyst": "Hiroi, Takahiro",
  "ada:analysisStartDate": "2023-11-14 | 2024-03-28 | (+7 more)",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "This material is supported by NASA PSEF grant. | NASA PSEF | (+1 more)",
  "ada:sampleName": "OREX-803124-0 | OREX-803119-100 | OREX-800029-0 | (+4 more)",
  "ada:samplingUnit": "missing",
  "ada:sampleHeated": "missing",
  "ada:vacuumExposedSample": "missing",
  "ada:incidenceAngle": -9999,
  "ada:emissionAngle": -9999,
  "ada:sampleTemperature": -9999
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/VNMIR/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Hiroi2023",
  "@type": [
    "ada:VNMIRSpectralPoint"
  ],
  "ada:componentType": "ada:VNMIRSpectralPoint",
  "schema:measurementTechnique": [
    {
      "@id": "ex:vnmirTAPP-Hiroi2023",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "20240514_vnmir_brown_orex-803124-0_1 | 20240918_vnmir_brown_orex-803119-100_1 | (+8 more)",
  "ada:analyst": "Hiroi, Takahiro",
  "ada:analysisStartDate": "2023-11-14 | 2024-03-28 | (+7 more)",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "This material is supported by NASA PSEF grant. | NASA PSEF | (+1 more)",
  "ada:sampleName": "OREX-803124-0 | OREX-803119-100 | OREX-800029-0 | (+4 more)",
  "ada:samplingUnit": "missing",
  "ada:sampleHeated": "missing",
  "ada:vacuumExposedSample": "missing",
  "ada:incidenceAngle": -9999,
  "ada:emissionAngle": -9999,
  "ada:sampleTemperature": -9999
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Hiroi2023> a ada:VNMIRSpectralPoint ;
    schema1:measurementTechnique <ex:vnmirTAPP-Hiroi2023> ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "2023-11-14 | 2024-03-28 | (+7 more)" ;
    ada:analyst "Hiroi, Takahiro" ;
    ada:componentType "ada:VNMIRSpectralPoint" ;
    ada:emissionAngle -9999 ;
    ada:fundingSourceForAnalysis "This material is supported by NASA PSEF grant. | NASA PSEF | (+1 more)" ;
    ada:incidenceAngle -9999 ;
    ada:sampleHeated "missing" ;
    ada:sampleName "OREX-803124-0 | OREX-803119-100 | OREX-800029-0 | (+4 more)" ;
    ada:sampleTemperature -9999 ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "20240514_vnmir_brown_orex-803124-0_1 | 20240918_vnmir_brown_orex-803119-100_1 | (+8 more)" ;
    ada:vacuumExposedSample "missing" .

<ex:vnmirTAPP-Hiroi2023> schema1:identifier "missing" .


```


### detail example Hiroi2023-2
detail instance derived from ADA n=13 | Hiroi2023 | Brown U. | Custom bi-directional.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Hiroi2023-2",
  "@type": [
    "ada:VNMIRSpectralPoint"
  ],
  "ada:componentType": "ada:VNMIRSpectralPoint",
  "schema:measurementTechnique": [
    {
      "@id": "ex:vnmirTAPP-Hiroi2023-2",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "20240917_vnmir_brown_orex-803119-102_1 | 20240916_vnmir_brown_orex-803119-100_1 | (+6 more)",
  "ada:analyst": "Hiroi, Takahiro",
  "ada:analysisStartDate": "2023-11-14 | 2024-09-16 | (+4 more)",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "This material is supported by NASA PSEF grant. | This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program and NASA Planetary Science Enabling Facilities program 80NSSC23K0198. | (+1 more)",
  "ada:sampleName": "OREX-803119-102 | OREX-803119-100 | OREX-800098-0 | (+4 more)",
  "ada:samplingUnit": "missing",
  "ada:sampleHeated": "missing",
  "ada:vacuumExposedSample": "missing",
  "ada:incidenceAngle": -9999,
  "ada:emissionAngle": -9999,
  "ada:sampleTemperature": -9999
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/VNMIR/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Hiroi2023-2",
  "@type": [
    "ada:VNMIRSpectralPoint"
  ],
  "ada:componentType": "ada:VNMIRSpectralPoint",
  "schema:measurementTechnique": [
    {
      "@id": "ex:vnmirTAPP-Hiroi2023-2",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "20240917_vnmir_brown_orex-803119-102_1 | 20240916_vnmir_brown_orex-803119-100_1 | (+6 more)",
  "ada:analyst": "Hiroi, Takahiro",
  "ada:analysisStartDate": "2023-11-14 | 2024-09-16 | (+4 more)",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "This material is supported by NASA PSEF grant. | This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program and NASA Planetary Science Enabling Facilities program 80NSSC23K0198. | (+1 more)",
  "ada:sampleName": "OREX-803119-102 | OREX-803119-100 | OREX-800098-0 | (+4 more)",
  "ada:samplingUnit": "missing",
  "ada:sampleHeated": "missing",
  "ada:vacuumExposedSample": "missing",
  "ada:incidenceAngle": -9999,
  "ada:emissionAngle": -9999,
  "ada:sampleTemperature": -9999
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Hiroi2023-2> a ada:VNMIRSpectralPoint ;
    schema1:measurementTechnique <ex:vnmirTAPP-Hiroi2023-2> ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "2023-11-14 | 2024-09-16 | (+4 more)" ;
    ada:analyst "Hiroi, Takahiro" ;
    ada:componentType "ada:VNMIRSpectralPoint" ;
    ada:emissionAngle -9999 ;
    ada:fundingSourceForAnalysis "This material is supported by NASA PSEF grant. | This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program and NASA Planetary Science Enabling Facilities program 80NSSC23K0198. | (+1 more)" ;
    ada:incidenceAngle -9999 ;
    ada:sampleHeated "missing" ;
    ada:sampleName "OREX-803119-102 | OREX-803119-100 | OREX-800098-0 | (+4 more)" ;
    ada:sampleTemperature -9999 ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "20240917_vnmir_brown_orex-803119-102_1 | 20240916_vnmir_brown_orex-803119-100_1 | (+6 more)" ;
    ada:vacuumExposedSample "missing" .

<ex:vnmirTAPP-Hiroi2023-2> schema1:identifier "missing" .


```


### detail example Milliken2024
detail instance derived from ADA n=2 | Milliken2024 | Brown U. | Bruker LUMOS FTIR microscope.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Milliken2024",
  "@type": [
    "ada:VNMIRSpectralPoint"
  ],
  "ada:componentType": "ada:VNMIRSpectralPoint",
  "schema:measurementTechnique": [
    {
      "@id": "ex:vnmirTAPP-Milliken2024",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "20231113_vnmir_brown_orex-800029-0_1",
  "ada:analyst": "Milliken, Ralph",
  "ada:analysisStartDate": "2024-01-19",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program.",
  "ada:sampleName": "OREX-800029-0",
  "ada:samplingUnit": "missing",
  "ada:sampleHeated": "missing",
  "ada:vacuumExposedSample": "missing",
  "ada:incidenceAngle": -9999,
  "ada:emissionAngle": -9999,
  "ada:sampleTemperature": -9999
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/VNMIR/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Milliken2024",
  "@type": [
    "ada:VNMIRSpectralPoint"
  ],
  "ada:componentType": "ada:VNMIRSpectralPoint",
  "schema:measurementTechnique": [
    {
      "@id": "ex:vnmirTAPP-Milliken2024",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "20231113_vnmir_brown_orex-800029-0_1",
  "ada:analyst": "Milliken, Ralph",
  "ada:analysisStartDate": "2024-01-19",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program.",
  "ada:sampleName": "OREX-800029-0",
  "ada:samplingUnit": "missing",
  "ada:sampleHeated": "missing",
  "ada:vacuumExposedSample": "missing",
  "ada:incidenceAngle": -9999,
  "ada:emissionAngle": -9999,
  "ada:sampleTemperature": -9999
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Milliken2024> a ada:VNMIRSpectralPoint ;
    schema1:measurementTechnique <ex:vnmirTAPP-Milliken2024> ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "2024-01-19" ;
    ada:analyst "Milliken, Ralph" ;
    ada:componentType "ada:VNMIRSpectralPoint" ;
    ada:emissionAngle -9999 ;
    ada:fundingSourceForAnalysis "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program." ;
    ada:incidenceAngle -9999 ;
    ada:sampleHeated "missing" ;
    ada:sampleName "OREX-800029-0" ;
    ada:sampleTemperature -9999 ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "20231113_vnmir_brown_orex-800029-0_1" ;
    ada:vacuumExposedSample "missing" .

<ex:vnmirTAPP-Milliken2024> schema1:identifier "missing" .


```


### detail example Keller2024
detail instance derived from ADA n=1 | Keller2024 | NASA Johnson Space Center | JEOL 2500SE.
#### json
```json
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/"
  },
  "@id": "ex:detail-Keller2024",
  "@type": [
    "ada:VNMIRSpectralPoint"
  ],
  "ada:componentType": "ada:VNMIRSpectralPoint",
  "schema:measurementTechnique": [
    {
      "@id": "ex:vnmirTAPP-Keller2024",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "20230929_vnmir_jsc-ares_orex-501006-0_1",
  "ada:analyst": "Keller, Lindsay",
  "ada:analysisStartDate": "2024-04-17",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program.",
  "ada:sampleName": "OREX-501006-0",
  "ada:samplingUnit": "missing",
  "ada:sampleHeated": "missing",
  "ada:vacuumExposedSample": "missing",
  "ada:incidenceAngle": -9999,
  "ada:emissionAngle": -9999,
  "ada:sampleTemperature": -9999
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
    "https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/VNMIR/detail/context.jsonld",
    {
      "schema": "http://schema.org/",
      "ada": "https://ada.astromat.org/metadata/"
    }
  ],
  "@id": "ex:detail-Keller2024",
  "@type": [
    "ada:VNMIRSpectralPoint"
  ],
  "ada:componentType": "ada:VNMIRSpectralPoint",
  "schema:measurementTechnique": [
    {
      "@id": "ex:vnmirTAPP-Keller2024",
      "schema:identifier": "missing"
    }
  ],
  "ada:sessionIdentifier": "20230929_vnmir_jsc-ares_orex-501006-0_1",
  "ada:analyst": "Keller, Lindsay",
  "ada:analysisStartDate": "2024-04-17",
  "ada:analysisEndDate": "missing",
  "ada:fundingSourceForAnalysis": "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program.",
  "ada:sampleName": "OREX-501006-0",
  "ada:samplingUnit": "missing",
  "ada:sampleHeated": "missing",
  "ada:vacuumExposedSample": "missing",
  "ada:incidenceAngle": -9999,
  "ada:emissionAngle": -9999,
  "ada:sampleTemperature": -9999
}
```

#### ttl
```ttl
@prefix ada: <https://ada.astromat.org/metadata/> .
@prefix schema1: <http://schema.org/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<ex:detail-Keller2024> a ada:VNMIRSpectralPoint ;
    schema1:measurementTechnique <ex:vnmirTAPP-Keller2024> ;
    ada:analysisEndDate "missing" ;
    ada:analysisStartDate "2024-04-17" ;
    ada:analyst "Keller, Lindsay" ;
    ada:componentType "ada:VNMIRSpectralPoint" ;
    ada:emissionAngle -9999 ;
    ada:fundingSourceForAnalysis "This material is supported by NASA under contract NNM10AA11C issued through the New Frontiers program." ;
    ada:incidenceAngle -9999 ;
    ada:sampleHeated "missing" ;
    ada:sampleName "OREX-501006-0" ;
    ada:sampleTemperature -9999 ;
    ada:samplingUnit "missing" ;
    ada:sessionIdentifier "20230929_vnmir_jsc-ares_orex-501006-0_1" ;
    ada:vacuumExposedSample "missing" .

<ex:vnmirTAPP-Keller2024> schema1:identifier "missing" .


```

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: VNMIR Analysis Detail
description: Detail block for VNMIR hasPart items. Discriminates on ada:componentType
  and carries the analysis-level properties - viewing geometry, sample state and per-measurement
  results - that are supplied per measurement rather than fixed by the procedure.
allOf:
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/AnalysisIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/calibrationFactor/schema.yaml#/$defs/AnalysisIdentification
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
                        - title: Sample Heated
                          description: Whether the sample was heated during measurement.
                            Record 'N/A' where the procedure does not control sample
                            temperature.
                          type: object
                          properties:
                            '@id':
                              const: ada:parameter/vnmirTAPP/sampleHeated
                            '@type':
                              const:
                              - schema:PropertyValue
                            schema:propertyID:
                              const:
                              - '@id': ada:parameter/vnmirTAPP/sampleHeated
                            schema:name:
                              const: Sample Heated
                            schema:value:
                              type: string
                          required:
                          - '@id'
                          - '@type'
                          - schema:propertyID
                          - schema:name
                          - schema:value
                        - title: Vacuum Exposed Sample
                          description: Whether this sample was exposed to vacuum before
                            or during measurement, which alters adsorbed water and
                            therefore the spectrum.
                          type: object
                          properties:
                            '@id':
                              const: ada:parameter/vnmirTAPP/vacuumExposedSample
                            '@type':
                              const:
                              - schema:PropertyValue
                            schema:propertyID:
                              const:
                              - '@id': ada:parameter/vnmirTAPP/vacuumExposedSample
                            schema:name:
                              const: Vacuum Exposed Sample
                            schema:value:
                              type: string
                          required:
                          - '@id'
                          - '@type'
                          - schema:propertyID
                          - schema:name
                          - schema:value
                        - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_preAnalysisImagingAndScreening
                      allOf:
                      - contains:
                          title: Sample Heated
                          description: Whether the sample was heated during measurement.
                            Record 'N/A' where the procedure does not control sample
                            temperature.
                          type: object
                          properties:
                            '@id':
                              const: ada:parameter/vnmirTAPP/sampleHeated
                            '@type':
                              const:
                              - schema:PropertyValue
                            schema:propertyID:
                              const:
                              - '@id': ada:parameter/vnmirTAPP/sampleHeated
                            schema:name:
                              const: Sample Heated
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
                          title: Vacuum Exposed Sample
                          description: Whether this sample was exposed to vacuum before
                            or during measurement, which alters adsorbed water and
                            therefore the spectrum.
                          type: object
                          properties:
                            '@id':
                              const: ada:parameter/vnmirTAPP/vacuumExposedSample
                            '@type':
                              const:
                              - schema:PropertyValue
                            schema:propertyID:
                              const:
                              - '@id': ada:parameter/vnmirTAPP/vacuumExposedSample
                            schema:name:
                              const: Vacuum Exposed Sample
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
                          $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_preAnalysisImagingAndScreening
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
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_samplingUnitSelectionCriteria
              - title: Spectral Resolution
                description: Instrumental spectral resolution the procedure operates
                  at.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/vnmirTAPP/spectralResolution
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/vnmirTAPP/spectralResolution
                  schema:name:
                    const: Spectral Resolution
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
              - title: Measurement Environment
                description: Atmosphere the measurement chamber is held in.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/vnmirTAPP/measurementEnvironment
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/vnmirTAPP/measurementEnvironment
                  schema:name:
                    const: Measurement Environment
                  schema:value:
                    type: string
                required:
                - '@id'
                - '@type'
                - schema:propertyID
                - schema:name
                - schema:value
              - title: Spot Size
                description: Diameter of the analysed area for a point measurement,
                  or the pixel footprint for a map.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/vnmirTAPP/spotSize
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/vnmirTAPP/spotSize
                  schema:name:
                    const: Spot Size
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
              - title: Number of Scans
                description: Interferograms co-added per reported spectrum.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/vnmirTAPP/numberOfScans
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/vnmirTAPP/numberOfScans
                  schema:name:
                    const: Number of Scans
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
              - title: Emissivity Maximum Fit Region Minimum
                description: Short-wavelength limit of the window over which the emissivity
                  maximum is fitted. Record 'N/A' where Measurement Type is not Emissivity.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/vnmirTAPP/emissivityMaximumFitRegionMinimum
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/vnmirTAPP/emissivityMaximumFitRegionMinimum
                  schema:name:
                    const: Emissivity Maximum Fit Region Minimum
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
              - title: Emissivity Maximum Fit Region Maximum
                description: Long-wavelength limit of the window over which the emissivity
                  maximum is fitted. Record 'N/A' where Measurement Type is not Emissivity.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/vnmirTAPP/emissivityMaximumFitRegionMaximum
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/vnmirTAPP/emissivityMaximumFitRegionMaximum
                  schema:name:
                    const: Emissivity Maximum Fit Region Maximum
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
              - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Analysis_constantsReferenceValues
              - title: Calibration Standards
                description: Reference materials measured to calibrate the reported
                  quantity, with source.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/vnmirTAPP/calibrationStandards
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/vnmirTAPP/calibrationStandards
                  schema:name:
                    const: Calibration Standards
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
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Analysis_samplingUnitSelectionCriteria
              minContains: 0
              maxContains: 1
            - contains:
                title: Spectral Resolution
                description: Instrumental spectral resolution the procedure operates
                  at.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/vnmirTAPP/spectralResolution
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/vnmirTAPP/spectralResolution
                  schema:name:
                    const: Spectral Resolution
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
                title: Measurement Environment
                description: Atmosphere the measurement chamber is held in.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/vnmirTAPP/measurementEnvironment
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/vnmirTAPP/measurementEnvironment
                  schema:name:
                    const: Measurement Environment
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
                title: Spot Size
                description: Diameter of the analysed area for a point measurement,
                  or the pixel footprint for a map.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/vnmirTAPP/spotSize
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/vnmirTAPP/spotSize
                  schema:name:
                    const: Spot Size
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
                title: Number of Scans
                description: Interferograms co-added per reported spectrum.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/vnmirTAPP/numberOfScans
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/vnmirTAPP/numberOfScans
                  schema:name:
                    const: Number of Scans
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
                title: Emissivity Maximum Fit Region Minimum
                description: Short-wavelength limit of the window over which the emissivity
                  maximum is fitted. Record 'N/A' where Measurement Type is not Emissivity.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/vnmirTAPP/emissivityMaximumFitRegionMinimum
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/vnmirTAPP/emissivityMaximumFitRegionMinimum
                  schema:name:
                    const: Emissivity Maximum Fit Region Minimum
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
                title: Emissivity Maximum Fit Region Maximum
                description: Long-wavelength limit of the window over which the emissivity
                  maximum is fitted. Record 'N/A' where Measurement Type is not Emissivity.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/vnmirTAPP/emissivityMaximumFitRegionMaximum
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/vnmirTAPP/emissivityMaximumFitRegionMaximum
                  schema:name:
                    const: Emissivity Maximum Fit Region Maximum
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
                $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/Param_Analysis_constantsReferenceValues
              minContains: 0
              maxContains: 1
            - contains:
                title: Calibration Standards
                description: Reference materials measured to calibrate the reported
                  quantity, with source.
                type: object
                properties:
                  '@id':
                    const: ada:parameter/vnmirTAPP/calibrationStandards
                  '@type':
                    const:
                    - schema:PropertyValue
                  schema:propertyID:
                    const:
                    - '@id': ada:parameter/vnmirTAPP/calibrationStandards
                  schema:name:
                    const: Calibration Standards
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
          ada:incidenceAngle:
            description: Angle of the illumination source from the sample surface
              normal, for this measurement.
            anyOf:
            - type: number
            - type: string
          ada:emissionAngle:
            description: Angle of the detector from the sample surface normal, for
              this measurement.
            anyOf:
            - type: number
            - type: string
          ada:phaseAngle:
            description: Angle between illumination and detection directions, for
              this measurement.
            anyOf:
            - type: number
            - type: string
          ada:sampleTemperature:
            description: Sample temperature during this measurement.
            anyOf:
            - type: number
            - type: string
          ada:environmentalPressure:
            description: Chamber pressure during the session.
            anyOf:
            - type: number
            - type: string
        required:
        - ada:emissionAngle
        - ada:incidenceAngle
        - ada:sampleTemperature
    schema:additionalProperty:
      type: array
      items:
        title: Emissivity Maximum
        description: Fitted maximum emissivity (Christiansen feature) for this measurement.
          Record 'N/A' where Measurement Type is not Emissivity.
        type: object
        properties:
          '@id':
            const: ada:parameter/vnmirTAPP/emissivityMaximum
          '@type':
            const:
            - schema:PropertyValue
          schema:propertyID:
            const:
            - '@id': ada:parameter/vnmirTAPP/emissivityMaximum
          schema:name:
            const: Emissivity Maximum
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
          title: Emissivity Maximum
          description: Fitted maximum emissivity (Christiansen feature) for this measurement.
            Record 'N/A' where Measurement Type is not Emissivity.
          type: object
          properties:
            '@id':
              const: ada:parameter/vnmirTAPP/emissivityMaximum
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/vnmirTAPP/emissivityMaximum
            schema:name:
              const: Emissivity Maximum
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
                const: Noise Uncertainty
            required:
            - dqv:isMeasurementOf
          then:
            properties:
              dqv:value:
                description: Noise-equivalent uncertainty on the reported spectrum
                  for this measurement.
                anyOf:
                - type: number
                - type: string

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/VNMIR/detail/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/VNMIR/detail/schema.yaml)


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
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/VNMIR/detail/context.jsonld)

## Sources

* [VNMIR_TAPP_draft_v2.csv (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/VNMIR/detail`

