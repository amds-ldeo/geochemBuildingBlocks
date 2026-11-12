
# Target-Material-Column Specification Registry (Schema)

`ogch.registry.targetMaterialColumns` *v0.1*

Registry of reusable schema:PropertyValueSpecification target-material-column definitions derived from technique TAPP spreadsheets. Hosts one $def per column of a per-target-material table. TAPP building blocks reference these definitions via fragment $refs so they resolve locally through the register.

[*Status*](http://www.opengis.net/def/status): Under development

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ADA Target-Material-Column Specification Registry
description: Registry of reusable schema:PropertyValueSpecification target-material-column
  definitions derived from technique TAPP spreadsheets. Each $def constrains one column
  of a technique's per-target-material table (e.g. beamCurrent, beamDiameter) - a
  field whose Keyed By column names `target material`, so its value repeats over the
  material types the procedure analyses. TAPP building blocks reference these definitions
  via fragment $refs (schema.yaml#/$defs/<name>) so they resolve locally through the
  building-block register. The root only hosts $defs; it has no instantiable properties
  of its own.
type: object
$defs:
  epma_backgroundCountingTime:
    title: Background Counting Time
    description: Total time spent counting at off-peak background position(s) in seconds,
      summed across all background positions.
    type: object
    properties:
      '@id':
        const: ada:targetMaterialColumn/epmaTAPP/backgroundCountingTime
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: backgroundCountingTime
      schema:name:
        const: Background Counting Time
      ada:dataType:
        const: number
      schema:readonlyValue:
        const: false
      ada:tier:
        const: M
      schema:defaultValue:
        anyOf:
        - type: number
        - type: string
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - schema:defaultValue
  epma_beamCurrent:
    title: Beam Current
    description: Probe current in nanoamperes (nA). Often varies by phase type or
      target species; record the procedure-standard value(s).
    type: object
    properties:
      '@id':
        const: ada:targetMaterialColumn/epmaTAPP/beamCurrent
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: beamCurrent
      schema:name:
        const: Beam Current
      ada:dataType:
        const: number
      schema:readonlyValue:
        const: false
      ada:tier:
        const: M
      schema:defaultValue:
        anyOf:
        - type: number
        - type: string
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - schema:defaultValue
  epma_beamDamageMinimization:
    title: Beam Damage Minimization
    description: Measures taken to minimize beam damage, particularly volatilization
      or migration of Na, K, F, and Cl in hydrous minerals, glasses, feldspars, phosphates,
      and carbonates. Document approach, beam conditions used, and phases for which
      it was applied.
    type: object
    properties:
      '@id':
        const: ada:targetMaterialColumn/epmaTAPP/beamDamageMinimization
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: beamDamageMinimization
      schema:name:
        const: Beam Damage Minimization
      ada:dataType:
        const: string
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:defaultValue:
        type: string
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
  epma_beamDiameter:
    title: Beam Diameter
    description: Diameter of the electron beam in micrometers. 0 indicates a fully
      focused beam. Document defocused diameter when used to minimize beam damage
      or improve spatial averaging for beam-sensitive phases.
    type: object
    properties:
      '@id':
        const: ada:targetMaterialColumn/epmaTAPP/beamDiameter
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: beamDiameter
      schema:name:
        const: Beam Diameter
      ada:dataType:
        const: number
      schema:readonlyValue:
        const: false
      ada:tier:
        const: M
      schema:defaultValue:
        anyOf:
        - type: number
        - type: string
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - schema:defaultValue
  epma_beamMode:
    title: Beam Mode
    description: Whether the electron beam was operated as a stationary focused spot,
      defocused to a specified diameter, or rastered over a small area during a single-point
      analysis. Must be consistent with the Beam Diameter and Beam Raster Dimensions
      fields. For mapping, beam scanning is controlled by Step Size / Pixel Size and
      Stage Scan vs. Beam Scan instead.
    type: object
    properties:
      '@id':
        const: ada:targetMaterialColumn/epmaTAPP/beamMode
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: beamMode
      schema:name:
        const: Beam Mode
      ada:dataType:
        const: string
      schema:readonlyValue:
        const: true
      ada:tier:
        const: M
      schema:inDefinedTermSet:
        const:
          '@id': ada:vocab/beam-mode
      schema:defaultValue:
        type: string
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - schema:defaultValue
  epma_beamRasterDimensions:
    title: Beam Raster Dimensions
    description: "Dimensions of the small area over which the beam is rastered at
      a single analysis point, reported as width \xD7 height in \xB5m. Applicable
      when Beam Mode = Rastered; defines the effective spatial footprint of the measurement.
      Not applicable when mapping."
    type: object
    properties:
      '@id':
        const: ada:targetMaterialColumn/epmaTAPP/beamRasterDimensions
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: beamRasterDimensions
      schema:name:
        const: Beam Raster Dimensions
      ada:dataType:
        const: number
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:defaultValue:
        anyOf:
        - type: number
        - type: string
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
  epma_peakCountingTime:
    title: Peak Counting Time
    description: Time spent counting X-ray intensity at the peak position, in seconds.
      Adjustments stay within procedure-defined bounds.
    type: object
    properties:
      '@id':
        const: ada:targetMaterialColumn/epmaTAPP/peakCountingTime
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: peakCountingTime
      schema:name:
        const: Peak Counting Time
      ada:dataType:
        const: number
      schema:readonlyValue:
        const: false
      ada:tier:
        const: M
      schema:defaultValue:
        anyOf:
        - type: number
        - type: string
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - schema:defaultValue
  epma_primaryCalibrationStandardName:
    title: Primary Calibration Standard Name
    description: "Name and reference material identifier of the primary reference
      material(s) against which the instrument is calibrated \u2014 converting raw
      signal intensities to concentrations, or anchoring an isotope ratio as the bracketing
      standard or zero-delta reference. Give the material name, its source or supplier,
      and a citation for the accepted values used. Where calibration instead uses
      the vendor's stored library or theoretical response factors rather than measured
      reference materials \u2014 'standardless' or 'semi-quantitative' quantification
      \u2014 record that here, naming the library or model used. 'None' means no calibration
      was performed at all, which is a different answer."
    type: object
    properties:
      '@id':
        const: ada:targetMaterialColumn/epmaTAPP/primaryCalibrationStandardName
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: primaryCalibrationStandardName
      schema:name:
        const: Primary Calibration Standard Name
      ada:dataType:
        const: string
      schema:readonlyValue:
        const: false
      ada:tier:
        const: M
      schema:defaultValue:
        type: string
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - schema:defaultValue
  laMcicpmsUPb_primaryCalibrationStandardName:
    title: Primary Calibration Standard Name
    description: "Name and reference material identifier of the primary reference
      material(s) against which the instrument is calibrated \u2014 converting raw
      signal intensities to concentrations, or anchoring an isotope ratio as the bracketing
      standard or zero-delta reference. Give the material name, its source or supplier,
      and a citation for the accepted values used. Where calibration instead uses
      the vendor's stored library or theoretical response factors rather than measured
      reference materials \u2014 'standardless' or 'semi-quantitative' quantification
      \u2014 record that here, naming the library or model used. 'None' means no calibration
      was performed at all, which is a different answer."
    type: object
    properties:
      '@id':
        const: ada:targetMaterialColumn/laMcicpmsUPbTAPP/primaryCalibrationStandardName
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: primaryCalibrationStandardName
      schema:name:
        const: Primary Calibration Standard Name
      ada:dataType:
        const: string
      schema:readonlyValue:
        const: false
      ada:tier:
        const: M
      schema:defaultValue:
        type: string
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - schema:defaultValue
  laMcicpms_primaryCalibrationStandardName:
    title: Primary Calibration Standard Name
    description: "Name and reference material identifier of the primary reference
      material(s) against which the instrument is calibrated \u2014 converting raw
      signal intensities to concentrations, or anchoring an isotope ratio as the bracketing
      standard or zero-delta reference. Give the material name, its source or supplier,
      and a citation for the accepted values used. Where calibration instead uses
      the vendor's stored library or theoretical response factors rather than measured
      reference materials \u2014 'standardless' or 'semi-quantitative' quantification
      \u2014 record that here, naming the library or model used. 'None' means no calibration
      was performed at all, which is a different answer."
    type: object
    properties:
      '@id':
        const: ada:targetMaterialColumn/laMcicpmsTAPP/primaryCalibrationStandardName
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: primaryCalibrationStandardName
      schema:name:
        const: Primary Calibration Standard Name
      ada:dataType:
        const: string
      schema:readonlyValue:
        const: false
      ada:tier:
        const: M
      schema:defaultValue:
        type: string
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - schema:defaultValue
  laQicpmsUPb_primaryCalibrationStandardName:
    title: Primary Calibration Standard Name
    description: "Name and reference material identifier of the primary reference
      material(s) against which the instrument is calibrated \u2014 converting raw
      signal intensities to concentrations, or anchoring an isotope ratio as the bracketing
      standard or zero-delta reference. Give the material name, its source or supplier,
      and a citation for the accepted values used. Where calibration instead uses
      the vendor's stored library or theoretical response factors rather than measured
      reference materials \u2014 'standardless' or 'semi-quantitative' quantification
      \u2014 record that here, naming the library or model used. 'None' means no calibration
      was performed at all, which is a different answer."
    type: object
    properties:
      '@id':
        const: ada:targetMaterialColumn/laQicpmsUPbTAPP/primaryCalibrationStandardName
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: primaryCalibrationStandardName
      schema:name:
        const: Primary Calibration Standard Name
      ada:dataType:
        const: string
      schema:readonlyValue:
        const: false
      ada:tier:
        const: M
      schema:defaultValue:
        type: string
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - schema:defaultValue
  laQicpms_primaryCalibrationStandardName:
    title: Primary Calibration Standard Name
    description: "Name and reference material identifier of the primary reference
      material(s) against which the instrument is calibrated \u2014 converting raw
      signal intensities to concentrations, or anchoring an isotope ratio as the bracketing
      standard or zero-delta reference. Give the material name, its source or supplier,
      and a citation for the accepted values used. Where calibration instead uses
      the vendor's stored library or theoretical response factors rather than measured
      reference materials \u2014 'standardless' or 'semi-quantitative' quantification
      \u2014 record that here, naming the library or model used. 'None' means no calibration
      was performed at all, which is a different answer."
    type: object
    properties:
      '@id':
        const: ada:targetMaterialColumn/laQicpmsTAPP/primaryCalibrationStandardName
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: primaryCalibrationStandardName
      schema:name:
        const: Primary Calibration Standard Name
      ada:dataType:
        const: string
      schema:readonlyValue:
        const: false
      ada:tier:
        const: M
      schema:defaultValue:
        type: string
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - schema:defaultValue
  laSficpmsUPb_primaryCalibrationStandardName:
    title: Primary Calibration Standard Name
    description: "Name and reference material identifier of the primary reference
      material(s) against which the instrument is calibrated \u2014 converting raw
      signal intensities to concentrations, or anchoring an isotope ratio as the bracketing
      standard or zero-delta reference. Give the material name, its source or supplier,
      and a citation for the accepted values used. Where calibration instead uses
      the vendor's stored library or theoretical response factors rather than measured
      reference materials \u2014 'standardless' or 'semi-quantitative' quantification
      \u2014 record that here, naming the library or model used. 'None' means no calibration
      was performed at all, which is a different answer."
    type: object
    properties:
      '@id':
        const: ada:targetMaterialColumn/laSficpmsUPbTAPP/primaryCalibrationStandardName
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: primaryCalibrationStandardName
      schema:name:
        const: Primary Calibration Standard Name
      ada:dataType:
        const: string
      schema:readonlyValue:
        const: false
      ada:tier:
        const: M
      schema:defaultValue:
        type: string
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - schema:defaultValue
  laSficpms_primaryCalibrationStandardName:
    title: Primary Calibration Standard Name
    description: "Name and reference material identifier of the primary reference
      material(s) against which the instrument is calibrated \u2014 converting raw
      signal intensities to concentrations, or anchoring an isotope ratio as the bracketing
      standard or zero-delta reference. Give the material name, its source or supplier,
      and a citation for the accepted values used. Where calibration instead uses
      the vendor's stored library or theoretical response factors rather than measured
      reference materials \u2014 'standardless' or 'semi-quantitative' quantification
      \u2014 record that here, naming the library or model used. 'None' means no calibration
      was performed at all, which is a different answer."
    type: object
    properties:
      '@id':
        const: ada:targetMaterialColumn/laSficpmsTAPP/primaryCalibrationStandardName
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: primaryCalibrationStandardName
      schema:name:
        const: Primary Calibration Standard Name
      ada:dataType:
        const: string
      schema:readonlyValue:
        const: false
      ada:tier:
        const: M
      schema:defaultValue:
        type: string
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - schema:defaultValue
  semComposition_backgroundCountingTime:
    title: Background Counting Time
    description: Total time spent counting at off-peak background position(s) in seconds,
      summed across all background positions.
    type: object
    properties:
      '@id':
        const: ada:targetMaterialColumn/semCompositionTAPP/backgroundCountingTime
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: backgroundCountingTime
      schema:name:
        const: Background Counting Time
      ada:dataType:
        const: number
      schema:readonlyValue:
        const: false
      ada:tier:
        const: M
      schema:defaultValue:
        anyOf:
        - type: number
        - type: string
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - schema:defaultValue
  semComposition_peakCountingTime:
    title: Peak Counting Time
    description: Time spent counting X-ray intensity at the peak position, in seconds.
      Adjustments stay within procedure-defined bounds.
    type: object
    properties:
      '@id':
        const: ada:targetMaterialColumn/semCompositionTAPP/peakCountingTime
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: peakCountingTime
      schema:name:
        const: Peak Counting Time
      ada:dataType:
        const: number
      schema:readonlyValue:
        const: false
      ada:tier:
        const: M
      schema:defaultValue:
        anyOf:
        - type: number
        - type: string
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - schema:defaultValue
  semComposition_primaryCalibrationStandardName:
    title: Primary Calibration Standard Name
    description: "Name and reference material identifier of the primary reference
      material(s) against which the instrument is calibrated \u2014 converting raw
      signal intensities to concentrations, or anchoring an isotope ratio as the bracketing
      standard or zero-delta reference. Give the material name, its source or supplier,
      and a citation for the accepted values used. Where calibration instead uses
      the vendor's stored library or theoretical response factors rather than measured
      reference materials \u2014 'standardless' or 'semi-quantitative' quantification
      \u2014 record that here, naming the library or model used. 'None' means no calibration
      was performed at all, which is a different answer."
    type: object
    properties:
      '@id':
        const: ada:targetMaterialColumn/semCompositionTAPP/primaryCalibrationStandardName
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: primaryCalibrationStandardName
      schema:name:
        const: Primary Calibration Standard Name
      ada:dataType:
        const: string
      schema:readonlyValue:
        const: false
      ada:tier:
        const: M
      schema:defaultValue:
        type: string
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - schema:defaultValue
  sem_backgroundCountingTime:
    title: Background Counting Time
    description: Total time spent counting at off-peak background position(s) in seconds,
      summed across all background positions.
    type: object
    properties:
      '@id':
        const: ada:targetMaterialColumn/semTAPP/backgroundCountingTime
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: backgroundCountingTime
      schema:name:
        const: Background Counting Time
      ada:dataType:
        const: number
      schema:readonlyValue:
        const: false
      ada:tier:
        const: M
      schema:defaultValue:
        anyOf:
        - type: number
        - type: string
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - schema:defaultValue
  sem_peakCountingTime:
    title: Peak Counting Time
    description: Time spent counting X-ray intensity at the peak position, in seconds.
      Adjustments stay within procedure-defined bounds.
    type: object
    properties:
      '@id':
        const: ada:targetMaterialColumn/semTAPP/peakCountingTime
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: peakCountingTime
      schema:name:
        const: Peak Counting Time
      ada:dataType:
        const: number
      schema:readonlyValue:
        const: false
      ada:tier:
        const: M
      schema:defaultValue:
        anyOf:
        - type: number
        - type: string
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - schema:defaultValue
  sem_primaryCalibrationStandardName:
    title: Primary Calibration Standard Name
    description: "Name and reference material identifier of the primary reference
      material(s) against which the instrument is calibrated \u2014 converting raw
      signal intensities to concentrations, or anchoring an isotope ratio as the bracketing
      standard or zero-delta reference. Give the material name, its source or supplier,
      and a citation for the accepted values used. Where calibration instead uses
      the vendor's stored library or theoretical response factors rather than measured
      reference materials \u2014 'standardless' or 'semi-quantitative' quantification
      \u2014 record that here, naming the library or model used. 'None' means no calibration
      was performed at all, which is a different answer."
    type: object
    properties:
      '@id':
        const: ada:targetMaterialColumn/semTAPP/primaryCalibrationStandardName
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: primaryCalibrationStandardName
      schema:name:
        const: Primary Calibration Standard Name
      ada:dataType:
        const: string
      schema:readonlyValue:
        const: false
      ada:tier:
        const: M
      schema:defaultValue:
        type: string
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - schema:defaultValue
  solutionMcicpms_primaryCalibrationStandardName:
    title: Primary Calibration Standard Name
    description: "Name and reference material identifier of the primary reference
      material(s) against which the instrument is calibrated \u2014 converting raw
      signal intensities to concentrations, or anchoring an isotope ratio as the bracketing
      standard or zero-delta reference. Give the material name, its source or supplier,
      and a citation for the accepted values used. Where calibration instead uses
      the vendor's stored library or theoretical response factors rather than measured
      reference materials \u2014 'standardless' or 'semi-quantitative' quantification
      \u2014 record that here, naming the library or model used. 'None' means no calibration
      was performed at all, which is a different answer."
    type: object
    properties:
      '@id':
        const: ada:targetMaterialColumn/solutionMcicpmsTAPP/primaryCalibrationStandardName
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: primaryCalibrationStandardName
      schema:name:
        const: Primary Calibration Standard Name
      ada:dataType:
        const: string
      schema:readonlyValue:
        const: false
      ada:tier:
        const: M
      schema:defaultValue:
        type: string
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - schema:defaultValue
  solutionQicpms_primaryCalibrationStandardName:
    title: Primary Calibration Standard Name
    description: "Name and reference material identifier of the primary reference
      material(s) against which the instrument is calibrated \u2014 converting raw
      signal intensities to concentrations, or anchoring an isotope ratio as the bracketing
      standard or zero-delta reference. Give the material name, its source or supplier,
      and a citation for the accepted values used. Where calibration instead uses
      the vendor's stored library or theoretical response factors rather than measured
      reference materials \u2014 'standardless' or 'semi-quantitative' quantification
      \u2014 record that here, naming the library or model used. 'None' means no calibration
      was performed at all, which is a different answer."
    type: object
    properties:
      '@id':
        const: ada:targetMaterialColumn/solutionQicpmsTAPP/primaryCalibrationStandardName
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: primaryCalibrationStandardName
      schema:name:
        const: Primary Calibration Standard Name
      ada:dataType:
        const: string
      schema:readonlyValue:
        const: false
      ada:tier:
        const: M
      schema:defaultValue:
        type: string
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - schema:defaultValue
  solutionSficpms_primaryCalibrationStandardName:
    title: Primary Calibration Standard Name
    description: "Name and reference material identifier of the primary reference
      material(s) against which the instrument is calibrated \u2014 converting raw
      signal intensities to concentrations, or anchoring an isotope ratio as the bracketing
      standard or zero-delta reference. Give the material name, its source or supplier,
      and a citation for the accepted values used. Where calibration instead uses
      the vendor's stored library or theoretical response factors rather than measured
      reference materials \u2014 'standardless' or 'semi-quantitative' quantification
      \u2014 record that here, naming the library or model used. 'None' means no calibration
      was performed at all, which is a different answer."
    type: object
    properties:
      '@id':
        const: ada:targetMaterialColumn/solutionSficpmsTAPP/primaryCalibrationStandardName
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: primaryCalibrationStandardName
      schema:name:
        const: Primary Calibration Standard Name
      ada:dataType:
        const: string
      schema:readonlyValue:
        const: false
      ada:tier:
        const: M
      schema:defaultValue:
        type: string
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - schema:defaultValue
x-bblocks-metadata:
  itemIdentifier: ogch.registry.targetMaterialColumns
  register: https://amds-ldeo.github.io/geochemBuildingBlocks/build/register.json
  version: '0.1'
  dateOfLastChange: '2026-11-12'

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/registry/targetMaterialColumns/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/registry/targetMaterialColumns/schema.yaml)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/registry/targetMaterialColumns`

