
# VNMIR Technique-Aligned Procedure Profile (vnmirTAPP) (Schema)

`ogch.techniqueProfile.geochemProfile.VNMIR.tapp` *v0.1*

Visible, near- and mid-infrared reflectance/emissivity spectroscopy extension of the base TAPP definition. Basic procedure-tier fields are required top-level ada: properties; Advanced procedure-tier fields are schema:additionalProperty[] PropertyValueSpecification entries. VNMIR has no per-element analyte axis, so no ada:analyteTemplate is defined. DRAFT - generated from draftTAPPs/VNMIR_TAPP_draft_v2.csv by tools/build_tapp.py; the source table has not been through Phase 0 review.

[*Status*](http://www.opengis.net/def/status): Under development

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: VNMIR Technique-Aligned Procedure Profile (vnmirTAPP)
description: 'Visible, near- and mid-infrared reflectance/emissivity spectroscopy
  extension of the base TAPP definition. Basic procedure-tier fields are required
  top-level ada: properties; Advanced procedure-tier fields are schema:additionalProperty[]
  PropertyValueSpecification entries. VNMIR has no per-element analyte axis, so no
  ada:analyteTemplate is defined. DRAFT - generated from draftTAPPs/VNMIR_TAPP_draft_v2.csv
  by tools/build_tapp.py; the source table has not been through Phase 0 review.'
allOf:
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/tappDefinition/schema.yaml
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/core/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/ProcedureIdentification
- $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/calibrationFactor/schema.yaml#/$defs/ProcedureIdentification
- type: object
  properties:
    ada:targetMaterial:
      description: General description of the material type(s) this procedure is designed
        to analyse.
      anyOf:
      - type: string
        enum:
        - Silicate mineral
        - Silicate glass
        - Oxide
        - Sulfide
        - Carbonate
        - Phosphate
        - Metal or alloy
        - Organic matter
        - Bulk regolith or soil
        - Meteorite (bulk)
        - Ice or hydrate
        - Synthetic analogue
        - N/A
        - None
        - missing
      - type: string
      readOnly: true
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
                      Record 'N/A' where the procedure does not control sample temperature.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/vnmirTAPP/sampleHeatedDefault
                      '@type':
                        const:
                        - schema:PropertyValueSpecification
                      schema:valueName:
                        const: sampleHeatedDefault
                      schema:name:
                        const: Sample Heated
                      ada:dataType:
                        const: string
                      ada:fieldScope:
                        const: session
                      schema:readonlyValue:
                        const: false
                      ada:tier:
                        const: R
                    required:
                    - '@id'
                    - '@type'
                    - schema:valueName
                    - schema:name
                    - ada:dataType
                    - ada:fieldScope
                  - title: Vacuum Exposed Sample
                    description: Whether this sample was exposed to vacuum before
                      or during measurement, which alters adsorbed water and therefore
                      the spectrum.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/vnmirTAPP/vacuumExposedSampleDefault
                      '@type':
                        const:
                        - schema:PropertyValueSpecification
                      schema:valueName:
                        const: vacuumExposedSampleDefault
                      schema:name:
                        const: Vacuum Exposed Sample
                      ada:dataType:
                        const: string
                      ada:fieldScope:
                        const: session
                      schema:readonlyValue:
                        const: false
                      ada:tier:
                        const: R
                    required:
                    - '@id'
                    - '@type'
                    - schema:valueName
                    - schema:name
                    - ada:dataType
                    - ada:fieldScope
                  - $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Procedure_preAnalysisImagingAndScreening
                allOf:
                - contains:
                    title: Sample Heated
                    description: Whether the sample was heated during measurement.
                      Record 'N/A' where the procedure does not control sample temperature.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/vnmirTAPP/sampleHeatedDefault
                      '@type':
                        const:
                        - schema:PropertyValueSpecification
                      schema:valueName:
                        const: sampleHeatedDefault
                      schema:name:
                        const: Sample Heated
                      ada:dataType:
                        const: string
                      ada:fieldScope:
                        const: session
                      schema:readonlyValue:
                        const: false
                      ada:tier:
                        const: R
                    required:
                    - '@id'
                    - '@type'
                    - schema:valueName
                    - schema:name
                    - ada:dataType
                    - ada:fieldScope
                  minContains: 0
                  maxContains: 1
                - contains:
                    title: Vacuum Exposed Sample
                    description: Whether this sample was exposed to vacuum before
                      or during measurement, which alters adsorbed water and therefore
                      the spectrum.
                    type: object
                    properties:
                      '@id':
                        const: ada:parameter/vnmirTAPP/vacuumExposedSampleDefault
                      '@type':
                        const:
                        - schema:PropertyValueSpecification
                      schema:valueName:
                        const: vacuumExposedSampleDefault
                      schema:name:
                        const: Vacuum Exposed Sample
                      ada:dataType:
                        const: string
                      ada:fieldScope:
                        const: session
                      schema:readonlyValue:
                        const: false
                      ada:tier:
                        const: R
                    required:
                    - '@id'
                    - '@type'
                    - schema:valueName
                    - schema:name
                    - ada:dataType
                    - ada:fieldScope
                  minContains: 0
                  maxContains: 1
                - contains:
                    $ref: https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/BaseSchema/modules/samplingUnitSelection/schema.yaml#/$defs/Param_Procedure_preAnalysisImagingAndScreening
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
    ada:instrumentManufacturer:
      description: Manufacturer of the instrument that performs the measurement, recorded
        as a controlled value. Where a procedure couples a sample-introduction system
        to an analysing instrument, this records the analysing instrument. Instrument
        Model gives the specific designation.
      type: string
      enum:
      - Thermo Fisher Scientific (Nicolet)
      - Bruker
      - ASD / Malvern Panalytical
      - Agilent
      - PerkinElmer
      - Shimadzu
      - Analytik Jena
      - Custom-built
      - Unknown
      - N/A
      - None
      - missing
      readOnly: true
    ada:instrumentModel:
      description: Model designation of the instrument that performs the measurement,
        including any generation or configuration suffix. Conventionally written with
        the manufacturer name included; Instrument Manufacturer records the vendor
        separately, as a controlled value, so that procedures remain findable by vendor.
      type: string
      readOnly: true
    ada:detector:
      description: Detector fitted to the spectrometer for this procedure.
      anyOf:
      - type: string
        enum:
        - MCT/A
        - MCT/B
        - DTGS
        - InSb
        - Si photodiode
        - Microbolometer
        - N/A
        - None
        - missing
      - type: string
      readOnly: true
    ada:beamsplitter:
      description: Beamsplitter fitted for this procedure; it sets the accessible
        spectral range. Record 'N/A' where the procedure uses no interferometer.
      anyOf:
      - type: string
        enum:
        - KBr
        - CaF2
        - ZnSe
        - Mylar
        - Quartz
        - N/A
        - None
        - missing
      - type: string
      readOnly: true
    ada:spectralRangeMinimum:
      description: Short-wavelength (or low-wavenumber) limit the procedure acquires.
      anyOf:
      - type: number
      - type: string
      readOnly: true
    ada:spectralRangeMaximum:
      description: Long-wavelength (or high-wavenumber) limit the procedure acquires.
      anyOf:
      - type: number
      - type: string
      readOnly: true
    ada:spectralResolutionDefault:
      description: Instrumental spectral resolution the procedure operates at.
      anyOf:
      - type: number
      - type: string
    schema:additionalProperty:
      type: array
      items:
        anyOf:
        - title: Spectral Sampling
          description: 'Spacing between adjacent recorded spectral points. Distinct
            from resolution: sampling may oversample the instrumental resolution.'
          type: object
          properties:
            '@id':
              const: ada:parameter/vnmirTAPP/spectralSampling
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/vnmirTAPP/spectralSampling
            schema:name:
              const: Spectral Sampling
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
          readOnly: true
        - title: Emissivity Maximum Fit Region Minimum
          description: Short-wavelength limit of the window over which the emissivity
            maximum is fitted. Record 'N/A' where Measurement Type is not Emissivity.
          type: object
          properties:
            '@id':
              const: ada:parameter/vnmirTAPP/emissivityMaximumFitRegionMinimumDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: emissivityMaximumFitRegionMinimumDefault
            schema:name:
              const: Emissivity Maximum Fit Region Minimum
            ada:dataType:
              const: number
            ada:fieldScope:
              const: session
            schema:readonlyValue:
              const: false
            ada:tier:
              const: R
            schema:unitText:
              type: string
          required:
          - '@id'
          - '@type'
          - schema:valueName
          - schema:name
          - ada:dataType
          - ada:fieldScope
        - title: Emissivity Maximum Fit Region Maximum
          description: Long-wavelength limit of the window over which the emissivity
            maximum is fitted. Record 'N/A' where Measurement Type is not Emissivity.
          type: object
          properties:
            '@id':
              const: ada:parameter/vnmirTAPP/emissivityMaximumFitRegionMaximumDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: emissivityMaximumFitRegionMaximumDefault
            schema:name:
              const: Emissivity Maximum Fit Region Maximum
            ada:dataType:
              const: number
            ada:fieldScope:
              const: session
            schema:readonlyValue:
              const: false
            ada:tier:
              const: R
            schema:unitText:
              type: string
          required:
          - '@id'
          - '@type'
          - schema:valueName
          - schema:name
          - ada:dataType
          - ada:fieldScope
      allOf:
      - contains:
          title: Spectral Sampling
          description: 'Spacing between adjacent recorded spectral points. Distinct
            from resolution: sampling may oversample the instrumental resolution.'
          type: object
          properties:
            '@id':
              const: ada:parameter/vnmirTAPP/spectralSampling
            '@type':
              const:
              - schema:PropertyValue
            schema:propertyID:
              const:
              - '@id': ada:parameter/vnmirTAPP/spectralSampling
            schema:name:
              const: Spectral Sampling
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
          readOnly: true
        minContains: 0
        maxContains: 1
      - contains:
          title: Emissivity Maximum Fit Region Minimum
          description: Short-wavelength limit of the window over which the emissivity
            maximum is fitted. Record 'N/A' where Measurement Type is not Emissivity.
          type: object
          properties:
            '@id':
              const: ada:parameter/vnmirTAPP/emissivityMaximumFitRegionMinimumDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: emissivityMaximumFitRegionMinimumDefault
            schema:name:
              const: Emissivity Maximum Fit Region Minimum
            ada:dataType:
              const: number
            ada:fieldScope:
              const: session
            schema:readonlyValue:
              const: false
            ada:tier:
              const: R
            schema:unitText:
              type: string
          required:
          - '@id'
          - '@type'
          - schema:valueName
          - schema:name
          - ada:dataType
          - ada:fieldScope
        minContains: 0
        maxContains: 1
      - contains:
          title: Emissivity Maximum Fit Region Maximum
          description: Long-wavelength limit of the window over which the emissivity
            maximum is fitted. Record 'N/A' where Measurement Type is not Emissivity.
          type: object
          properties:
            '@id':
              const: ada:parameter/vnmirTAPP/emissivityMaximumFitRegionMaximumDefault
            '@type':
              const:
              - schema:PropertyValueSpecification
            schema:valueName:
              const: emissivityMaximumFitRegionMaximumDefault
            schema:name:
              const: Emissivity Maximum Fit Region Maximum
            ada:dataType:
              const: number
            ada:fieldScope:
              const: session
            schema:readonlyValue:
              const: false
            ada:tier:
              const: R
            schema:unitText:
              type: string
          required:
          - '@id'
          - '@type'
          - schema:valueName
          - schema:name
          - ada:dataType
          - ada:fieldScope
        minContains: 0
        maxContains: 1
    ada:measurementType:
      description: Radiometric quantity the procedure reports.
      anyOf:
      - type: string
        enum:
        - Reflectance (bidirectional)
        - Reflectance (biconical)
        - Reflectance (hemispherical)
        - Emissivity
        - Transmittance
        - Absorbance
        - N/A
        - None
        - missing
      - type: string
      readOnly: true
    ada:measurementEnvironmentDefault:
      description: Atmosphere the measurement chamber is held in.
      anyOf:
      - type: string
        enum:
        - Ambient air
        - Purged (dry N2)
        - Purged (dry air)
        - Vacuum
        - Simulated planetary
        - N/A
        - None
        - missing
      - type: string
    ada:spotSizeDefault:
      description: Diameter of the analysed area for a point measurement, or the pixel
        footprint for a map.
      anyOf:
      - type: number
      - type: string
    ada:numberOfScansDefault:
      description: Interferograms co-added per reported spectrum.
      anyOf:
      - type: integer
      - type: string
    ada:constantsAndReferenceValuesUsedDefault:
      description: Physical constants and reference values used in data reduction
        to calculate the final reported quantity (e.g., decay constants for age calculation,
        standard isotope ratios, or other citable reference values used in a correction
        or calculation), together with their source. Distinct from the Group 6 reference-material
        fields, which document accepted values for specific calibration/validation
        materials rather than universal physical constants. Record "None" if no citable,
        revisable physical constants feed into this procedure's data reduction.
      type: string
    ada:calibrationStandardsDefault:
      description: Reference materials measured to calibrate the reported quantity,
        with source.
      type: string
    ada:analyticalMode:
      type: array
      items:
        type: string
        enum:
        - Spectral Point
        - Overview Image
        - Spectral Map
  required:
  - ada:targetMaterial
  - ada:instrumentManufacturer
  - ada:instrumentModel
  - ada:detector
  - ada:beamsplitter
  - ada:spectralRangeMinimum
  - ada:spectralRangeMaximum
  - ada:spectralResolutionDefault
  - ada:measurementType
  - ada:measurementEnvironmentDefault
  - ada:spotSizeDefault
  - ada:numberOfScansDefault
  - ada:constantsAndReferenceValuesUsedDefault
  - ada:calibrationStandardsDefault

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/VNMIR/tapp/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/VNMIR/tapp/schema.yaml)


# JSON-LD Context

```jsonld
{
  "@context": {
    "schema": "http://schema.org/",
    "ada": "https://ada.astromat.org/metadata/",
    "prov": "http://www.w3.org/ns/prov#",
    "cdi": "http://ddialliance.org/Specification/DDI-CDI/1.0/RDF/",
    "bios": "https://bioschemas.org/",
    "nxs": "https://manual.nexusformat.org/classes/",
    "dqv": "http://www.w3.org/ns/dqv#",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "wd": "https://www.wikidata.org/entity/",
    "cdif": "https://w3id.org/cdif/",
    "ex": "https://example.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "dcat": "http://www.w3.org/ns/dcat#",
    "@version": 1.1
  }
}
```

You can find the full JSON-LD context here:
[context.jsonld](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/techniqueProfile/geochemProfile/VNMIR/tapp/context.jsonld)

## Sources

* [VNMIR_TAPP_draft_v2.csv (TAPP worksheet)](https://github.com/amds-ldeo/geochemBuildingBlocks/tree/main/docs)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/techniqueProfile/geochemProfile/VNMIR/tapp`

