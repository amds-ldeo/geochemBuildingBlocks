
# Method-Parameter Template Registry (Schema)

`ogch.registry.parameterTemplates` *v0.1*

Registry of reusable schema:PropertyValueSpecification method-parameter template definitions derived from technique TAPP spreadsheets. Hosts one $def per method-level parameter template. TAPP building blocks reference these definitions via fragment $refs so they resolve locally through the register.

[*Status*](http://www.opengis.net/def/status): Under development

## Schema

```yaml
$schema: https://json-schema.org/draft/2020-12/schema
title: ADA Method-Parameter Template Registry
description: Registry of reusable schema:PropertyValueSpecification method-parameter
  templates derived from technique TAPP spreadsheets. Each $def constrains one method-level
  (readOnly:true) parameter template (e.g. DriftCorrection, massAbsorptionCoefficients).
  TAPP building blocks reference these definitions via fragment $refs (schema.yaml#/$defs/<name>)
  so they resolve locally through the building-block register. The root only hosts
  $defs; it has no instantiable properties of its own.
type: object
$defs:
  empa_analyticalAccuracyDefault:
    title: Analytical Accuracy
    description: Offset between measured and accepted reference values for secondary
      standards, expressed as percent relative bias. Include reference material, reference
      value source, and the measured value.
    type: object
    properties:
      '@id':
        const: ada:parameter/empaTAPP/analyticalAccuracyDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: analyticalAccuracyDefault
      schema:name:
        const: Analytical Accuracy
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
  empa_analyticalPrecisionDefault:
    title: Analytical Precision
    description: Reproducibility of repeated measurements on the same or equivalent
      reference material, expressed as 1-sigma relative standard deviation (%). Include
      reference material name, number of analyses (n), and the measured value.
    type: object
    properties:
      '@id':
        const: ada:parameter/empaTAPP/analyticalPrecisionDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: analyticalPrecisionDefault
      schema:name:
        const: Analytical Precision
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
  empa_backgroundPositionDefault:
    title: Background Position(s)
    description: Location(s) of off-peak background measurement(s) relative to the
      peak, in mm or sin-theta, and whether on the high- or low-energy side.
    type: object
    properties:
      '@id':
        const: ada:parameter/empaTAPP/backgroundPositionDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: backgroundPositionDefault
      schema:name:
        const: Background Position(s)
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
  empa_beamDamageMinimizationDefault:
    title: Beam Damage Minimization
    description: Measures taken to minimize beam damage, particularly volatilization
      or migration of Na, K, F, and Cl in hydrous minerals, glasses, feldspars, phosphates,
      and carbonates. Document approach, beam conditions used, and phases for which
      it was applied.
    type: object
    properties:
      '@id':
        const: ada:parameter/empaTAPP/beamDamageMinimizationDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: beamDamageMinimizationDefault
      schema:name:
        const: Beam Damage Minimization
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
  empa_beamRasterDimensionsDefault:
    title: Beam Raster Dimensions
    description: "Dimensions of the small area over which the beam is rastered at
      a single analysis point, reported as width \xD7 height in \xB5m. Applicable
      when Beam Mode = Rastered; defines the effective spatial footprint of the measurement.
      Not applicable when mapping."
    type: object
    properties:
      '@id':
        const: ada:parameter/empaTAPP/beamRasterDimensionsDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: beamRasterDimensionsDefault
      schema:name:
        const: Beam Raster Dimensions
      ada:dataType:
        const: number
      ada:fieldScope:
        const: session
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:unitText:
        const: "\xB5m x \xB5m"
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - ada:fieldScope
  empa_blankCorrectionDefault:
    title: Blank Correction
    description: Method and reference material(s) used to determine and subtract blank
      signal contributions (e.g., carbon coat contribution to C signal, or background
      contamination for trace elements).
    type: object
    properties:
      '@id':
        const: ada:parameter/empaTAPP/blankCorrectionDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: blankCorrectionDefault
      schema:name:
        const: Blank Correction
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
  empa_countingStatisticsErrorDefault:
    title: Counting Statistics Error
    description: "Uncertainty predicted from counting statistics \u2014 the theoretical
      limit set by the Poisson distribution of the counts accumulated \u2014 for each
      reported quantity per analysis, with the sigma level stated. Derived from the
      counts on the analyte together with those on any background or blank subtracted
      from it. Distinct from the scatter actually observed within a measurement or
      between repeated measurements, which is recorded separately."
    type: object
    properties:
      '@id':
        const: ada:parameter/empaTAPP/countingStatisticsErrorDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: countingStatisticsErrorDefault
      schema:name:
        const: Counting Statistics Error
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
  empa_detectionLimitDefault:
    title: Detection Limit
    description: Detection limit, one per reported concentration variable (one per
      analyte, these being the same set). State the units and whether the values are
      procedure-typical estimates or session-specific measured values. The calculation
      method is recorded separately in Detection Limit Method. Record 'N/A' where
      the procedure reports no concentrations.
    type: object
    properties:
      '@id':
        const: ada:parameter/empaTAPP/detectionLimitDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: detectionLimitDefault
      schema:name:
        const: Detection Limit
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
  empa_driftCorrectionDefault:
    title: Drift Correction
    description: Method used to monitor and correct for instrument drift (beam current
      drift, spectrometer drift) during the analytical session.
    type: object
    properties:
      '@id':
        const: ada:parameter/empaTAPP/driftCorrectionDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: driftCorrectionDefault
      schema:name:
        const: Drift Correction
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
  empa_halogenCorrectionOnOxygenDefault:
    title: Halogen Correction on Oxygen
    description: Whether oxygen content was adjusted to account for halogen substitution
      (F and/or Cl replacing OH) in halogen-bearing phases such as apatite, amphibole,
      and mica, where oxygen is calculated by stoichiometry.
    type: object
    properties:
      '@id':
        const: ada:parameter/empaTAPP/halogenCorrectionOnOxygenDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: halogenCorrectionOnOxygenDefault
      schema:name:
        const: Halogen Correction on Oxygen
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
  empa_normalizationStandardsBasedCorrectionDefault:
    title: Normalization / Standards-Based Correction
    description: "Post-acquisition normalization applied to the reported data beyond
      the primary calibration \u2014 for example correction to a reference value derived
      from secondary reference materials, or correction for a systematic bias those
      materials reveal. Record 'None' if no additional normalization is applied."
    type: object
    properties:
      '@id':
        const: ada:parameter/empaTAPP/normalizationStandardsBasedCorrectionDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: normalizationStandardsBasedCorrectionDefault
      schema:name:
        const: Normalization / Standards-Based Correction
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
  empa_preAnalysisImagingAndScreeningDefault:
    title: Pre-Analysis Imaging and Screening
    description: Imaging or other characterisation performed before the measurement
      in order to select or locate the sampling unit to be analysed, including the
      technique, instrument and settings used, and how individual analyses are linked
      back to the images. Distinct from any imaging the procedure performs as its
      own measurement. Where the imaging is performed on a separate instrument, it
      should also be recorded in the Group 1 coupling fields.
    type: object
    properties:
      '@id':
        const: ada:parameter/empaTAPP/preAnalysisImagingAndScreeningDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: preAnalysisImagingAndScreeningDefault
      schema:name:
        const: Pre-Analysis Imaging and Screening
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
  empa_samplePersistentIdentifierDefault:
    title: Sample Persistent Identifier
    description: Globally unique, persistent identifier for each sample listed in
      Sample Name. IGSN (International Geo Sample Number) is the recommended standard
      for geological and cosmochemical samples, as used by Astromat, EarthChem and
      SESAR. Where a sample and its sub-samples are separately registered, record
      the identifier at the level actually analysed.
    type: object
    properties:
      '@id':
        const: ada:parameter/empaTAPP/samplePersistentIdentifierDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: samplePersistentIdentifierDefault
      schema:name:
        const: Sample Persistent Identifier
      ada:dataType:
        const: uri
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
  empa_timeDependentIntensityCorrectionDefault:
    title: Time-Dependent Intensity Correction
    description: Type of time-dependent intensity (TDI) correction applied to compensate
      for beam-induced volatilization or migration of sensitive elements (e.g., Na,
      K, F in glasses, feldspars, carbonates).
    type: object
    properties:
      '@id':
        const: ada:parameter/empaTAPP/timeDependentIntensityCorrectionDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: timeDependentIntensityCorrectionDefault
      schema:name:
        const: Time-Dependent Intensity Correction
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
  laMcicpmsUPb_ageDatumReferenceEpochDefault:
    title: Age Datum / Reference Epoch
    description: 'The zero point from which the reported age is measured, where this
      is not the present day, and the date it corresponds to. Record ''Present day''
      where the conventional datum applies. Where the datum is not the present, record
      it explicitly: year of sample collection for luminescence, end of irradiation
      for 40Ar/39Ar decay corrections.'
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsUPbTAPP/ageDatumReferenceEpochDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: ageDatumReferenceEpochDefault
      schema:name:
        const: Age Datum / Reference Epoch
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
  laMcicpmsUPb_betweenSessionAnalyticalPrecisionAndAssessmentMethodDefault:
    title: Between-Session (Long-Term) Analytical Precision and Assessment Method
    description: "Precision of measurements across multiple analytical sessions over
      weeks to months \u2014 long-term or intermediate precision \u2014 and the method
      used to assess it. Report both the assessment method and the precision values,
      specifying the reference material, the number of measurements and sessions,
      the time span covered, and the statistic reported."
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethodDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: betweenSessionAnalyticalPrecisionAndAssessmentMethodDefault
      schema:name:
        const: Between-Session (Long-Term) Analytical Precision and Assessment Method
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
  laMcicpmsUPb_collisionReactionGasMixtureRatioDefault:
    title: Collision/Reaction Gas Mixture Ratio
    description: Where the collision or reaction cell is supplied with a mixture of
      gases rather than a single gas, the identities and proportions of that mixture.
      Recorded separately from the gas identity. Record 'N/A' where a single gas is
      used.
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsUPbTAPP/collisionReactionGasMixtureRatioDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: collisionReactionGasMixtureRatioDefault
      schema:name:
        const: Collision/Reaction Gas Mixture Ratio
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
  laMcicpmsUPb_countingStatisticsErrorDefault:
    title: Counting Statistics Error
    description: "Uncertainty predicted from counting statistics \u2014 the theoretical
      limit set by the Poisson distribution of the counts accumulated \u2014 for each
      reported quantity per analysis, with the sigma level stated. Derived from the
      counts on the analyte together with those on any background or blank subtracted
      from it. Distinct from the scatter actually observed within a measurement or
      between repeated measurements, which is recorded separately."
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsUPbTAPP/countingStatisticsErrorDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: countingStatisticsErrorDefault
      schema:name:
        const: Counting Statistics Error
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
  laMcicpmsUPb_detectionLimitDefault:
    title: Detection Limit
    description: Detection limit, one per reported concentration variable (one per
      analyte, these being the same set). State the units and whether the values are
      procedure-typical estimates or session-specific measured values. The calculation
      method is recorded separately in Detection Limit Method. Record 'N/A' where
      the procedure reports no concentrations.
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsUPbTAPP/detectionLimitDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: detectionLimitDefault
      schema:name:
        const: Detection Limit
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
  laMcicpmsUPb_doubleSpikeMixingRatioDefault:
    title: Double-Spike Mixing Ratio
    description: "Target proportion of double-spike signal relative to total analyte
      signal in the spiked mixture, expressed as spike fraction (0\u20131) or spike:sample
      ratio. The optimum is analyte-system specific and is typically determined using
      the Double Spike Toolbox or equivalent. The achieved mixing ratio may deviate
      from the target within acceptable bounds (typically \xB120% of optimal); the
      double-spike inversion corrects for actual mixing ratios. Record 'N/A' where
      the procedure does not use a double spike."
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsUPbTAPP/doubleSpikeMixingRatioDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: doubleSpikeMixingRatioDefault
      schema:name:
        const: Double-Spike Mixing Ratio
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
  laMcicpmsUPb_doublyChargedSpeciesMonitorDefault:
    title: Doubly-Charged Species Monitor
    description: "The mass ratio monitored to estimate doubly-charged ion (M\xB2\u207A)
      formation during instrument tuning. The monitor species and the mass positions
      monitored should be stated explicitly. Analogous to Oxide Production Method
      and Threshold for oxide monitoring."
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsUPbTAPP/doublyChargedSpeciesMonitorDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: doublyChargedSpeciesMonitorDefault
      schema:name:
        const: Doubly-Charged Species Monitor
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
  laMcicpmsUPb_doublyChargedSpeciesProductionDefault:
    title: Doubly-Charged Species Production
    description: Measured percentage of doubly-charged ion production for the monitored
      species at the time of instrument tuning. The acceptable threshold is typically
      <1% or <3%. Record both the threshold and the measured value.
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsUPbTAPP/doublyChargedSpeciesProductionDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: doublyChargedSpeciesProductionDefault
      schema:name:
        const: Doubly-Charged Species Production
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
  laMcicpmsUPb_errorCorrelationBetweenReportedQuantitiesDefault:
    title: Error Correlation Between Reported Quantities
    description: The correlation coefficient between pairs of reported quantities
      whose uncertainties are not independent, together with the pair it applies to
      and how it was obtained.
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsUPbTAPP/errorCorrelationBetweenReportedQuantitiesDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: errorCorrelationBetweenReportedQuantitiesDefault
      schema:name:
        const: Error Correlation Between Reported Quantities
      ada:dataType:
        const: number
      ada:fieldScope:
        const: session
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:unitText:
        const: dimensionless
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - ada:fieldScope
  laMcicpmsUPb_fusionFluxAndDilutionRatioDefault:
    title: Fusion Flux and Dilution Ratio
    description: For procedures using fused glass, the flux type and sample:flux dilution
      ratio used to prepare the analytical glass.
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsUPbTAPP/fusionFluxAndDilutionRatioDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: fusionFluxAndDilutionRatioDefault
      schema:name:
        const: Fusion Flux and Dilution Ratio
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
  laMcicpmsUPb_icpTuningDefault:
    title: ICP Tuning
    description: Description of the approach used to optimise ICP plasma conditions
      prior to analysis, including the reference material used for tuning and the
      acceptance criteria (e.g., oxide production threshold, sensitivity targets,
      mass calibration).
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsUPbTAPP/icpTuningDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: icpTuningDefault
      schema:name:
        const: ICP Tuning
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
  laMcicpmsUPb_instrumentSerialNumberOrLabIdentifierDefault:
    title: Instrument Serial Number or Lab Identifier
    description: Serial number or laboratory-internal identifier for the specific
      instrument unit.
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsUPbTAPP/instrumentSerialNumberOrLabIdentifierDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: instrumentSerialNumberOrLabIdentifierDefault
      schema:name:
        const: Instrument Serial Number or Lab Identifier
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
  laMcicpmsUPb_internalAnalyticalPrecisionAndAssessmentMethodDefault:
    title: Internal (Within-Measurement) Analytical Precision and Assessment Method
    description: Precision of a single measurement, derived from the scatter of the
      cycles, sweeps or integrations that make it up, together with the method used
      to assess it. State the statistic (2SE, 2SD, 1s RSD), the number of cycles it
      is computed over, and the reported quantity it applies to. Distinct from Counting
      Statistics Error, which records the uncertainty predicted from the counts rather
      than the scatter observed; where a procedure reports both, record the observed
      value here and the predicted value there.
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsUPbTAPP/internalAnalyticalPrecisionAndAssessmentMethodDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: internalAnalyticalPrecisionAndAssessmentMethodDefault
      schema:name:
        const: Internal (Within-Measurement) Analytical Precision and Assessment Method
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
  laMcicpmsUPb_laserEnergyDefault:
    title: Laser Energy
    description: "Laser pulse energy in millijoules as set at the laser output or
      measured at the sample surface. Report only when the system displays energy
      directly. Laser fluence (J cm\u207B\xB2) is the preferred quantity and is captured
      in Laser Fluence (Energy Density)."
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsUPbTAPP/laserEnergyDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: laserEnergyDefault
      schema:name:
        const: Laser Energy
      ada:dataType:
        const: number
      ada:fieldScope:
        const: session
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:unitText:
        const: mJ
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - ada:fieldScope
  laMcicpmsUPb_limitOfQuantificationMethodDefault:
    title: Limit of Quantification (LOQ) Method
    description: 'Reference or description of the method used to calculate the limit
      of quantification (LOQ): the lowest concentration reliably measurable with acceptable
      precision and accuracy. Required when concentrations near the LOD are reported.'
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsUPbTAPP/limitOfQuantificationMethodDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: limitOfQuantificationMethodDefault
      schema:name:
        const: Limit of Quantification (LOQ) Method
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
  laMcicpmsUPb_makeUpGasAndFlowRateDefault:
    title: Make-up Gas and Flow Rate
    description: Supplementary gas added to the sample-carrying stream between the
      sample introduction system and the plasma, with its identity and the procedure-registered
      target flow rate. Record any small nitrogen or hydrogen addition with its own
      flow, whose unit commonly differs from the make-up flow. Record 'None' explicitly
      where no supplementary gas is added, to distinguish it from not reported.
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsUPbTAPP/makeUpGasAndFlowRateDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: makeUpGasAndFlowRateDefault
      schema:name:
        const: Make-up Gas and Flow Rate
      ada:dataType:
        const: number
      ada:fieldScope:
        const: session
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:unitText:
        const: L/min
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - ada:fieldScope
  laMcicpmsUPb_memoryEffectMitigationDefault:
    title: Memory Effect Mitigation
    description: Procedure applied to identify and minimise carry-over of high-concentration
      or isotopically distinct material from a preceding measurement into the current
      one. Mitigation is applied primarily at measurement time, by allowing sufficient
      washout or rinse between successive introductions. At data processing level,
      record any flagging or exclusion of measurements where the required washout
      may not have been achieved.
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsUPbTAPP/memoryEffectMitigationDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: memoryEffectMitigationDefault
      schema:name:
        const: Memory Effect Mitigation
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
  laMcicpmsUPb_normalizationStandardsBasedCorrectionDefault:
    title: Normalization / Standards-Based Correction
    description: "Post-acquisition normalization applied to the reported data beyond
      the primary calibration \u2014 for example correction to a reference value derived
      from secondary reference materials, or correction for a systematic bias those
      materials reveal. Record 'None' if no additional normalization is applied."
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsUPbTAPP/normalizationStandardsBasedCorrectionDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: normalizationStandardsBasedCorrectionDefault
      schema:name:
        const: Normalization / Standards-Based Correction
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
  laMcicpmsUPb_numberOfReplicatesDefault:
    title: Number of Replicates
    description: Number of replicate measurements performed on the same sample, or
      on the same nominal location where the technique is spatially resolved. For
      spot analysis this is the number of individual spots per grain or location;
      for transects, the number of replicate lines; for mapping, the number of map
      acquisitions of the same area; for solution work, the number of discrete replicate
      measurements acquired per sample solution.
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsUPbTAPP/numberOfReplicatesDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: numberOfReplicatesDefault
      schema:name:
        const: Number of Replicates
      ada:dataType:
        const: integer
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
  laMcicpmsUPb_preAblationSurfaceTreatmentDefault:
    title: Pre-Ablation Surface Treatment
    description: Procedure applied immediately before each analysis to remove surface
      contamination or condition the sample surface. Distinct from general sample
      preparation. For spot analysis, pre-ablation pulses are discarded before signal
      acquisition begins. For mapping, this step is typically omitted.
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsUPbTAPP/preAblationSurfaceTreatmentDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: preAblationSurfaceTreatmentDefault
      schema:name:
        const: Pre-Ablation Surface Treatment
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
  laMcicpmsUPb_preAnalysisImagingAndScreeningDefault:
    title: Pre-Analysis Imaging and Screening
    description: Imaging or other characterisation performed before the measurement
      in order to select or locate the sampling unit to be analysed, including the
      technique, instrument and settings used, and how individual analyses are linked
      back to the images. Distinct from any imaging the procedure performs as its
      own measurement. Where the imaging is performed on a separate instrument, it
      should also be recorded in the Group 1 coupling fields.
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsUPbTAPP/preAnalysisImagingAndScreeningDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: preAnalysisImagingAndScreeningDefault
      schema:name:
        const: Pre-Analysis Imaging and Screening
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
  laMcicpmsUPb_reactionGasFlowRateDefault:
    title: Reaction Gas Flow Rate
    description: Flow rate of the reactive gas introduced into the dynamic reaction
      cell (DRC), in mL/min. Record 'None' if DRC mode is not used, and 'N/A' where
      Collision/Reaction Cell (CRC) Configuration does not include DRC or the instrument
      has no cell.
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsUPbTAPP/reactionGasFlowRateDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: reactionGasFlowRateDefault
      schema:name:
        const: Reaction Gas Flow Rate
      ada:dataType:
        const: number
      ada:fieldScope:
        const: session
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:unitText:
        const: mL/min
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - ada:fieldScope
  laMcicpmsUPb_samplePersistentIdentifierDefault:
    title: Sample Persistent Identifier
    description: Globally unique, persistent identifier for each sample listed in
      Sample Name. IGSN (International Geo Sample Number) is the recommended standard
      for geological and cosmochemical samples, as used by Astromat, EarthChem and
      SESAR. Where a sample and its sub-samples are separately registered, record
      the identifier at the level actually analysed.
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsUPbTAPP/samplePersistentIdentifierDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: samplePersistentIdentifierDefault
      schema:name:
        const: Sample Persistent Identifier
      ada:dataType:
        const: uri
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
  laMcicpmsUPb_signalSmoothingDefault:
    title: Signal Smoothing
    description: Description of any signal smoothing device or approach installed
      between the ablation cell and the ICP-MS to reduce pulse-to-pulse signal variability.
      For mapping analyses, report "None" explicitly.
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsUPbTAPP/signalSmoothingDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: signalSmoothingDefault
      schema:name:
        const: Signal Smoothing
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
  laMcicpmsUPb_spikeOutlierFilteringApproachDefault:
    title: Spike / Outlier Filtering Approach
    description: Criteria used to identify and exclude anomalous data - signal spikes,
      individual cycles, or whole replicate measurements - before the reported value
      is calculated. State where in the reduction sequence the filter is applied.
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsUPbTAPP/spikeOutlierFilteringApproachDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: spikeOutlierFilteringApproachDefault
      schema:name:
        const: Spike / Outlier Filtering Approach
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
  laMcicpmsUPb_torchDepthDefault:
    title: Torch Depth
    description: Distance between the load coil and the sampling cone tip (mm), also
      called injector depth or torch position depending on the instrument manufacturer.
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsUPbTAPP/torchDepthDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: torchDepthDefault
      schema:name:
        const: Torch Depth
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
  laMcicpmsUPb_transectRateMappingRateOrStepSizeDefault:
    title: Transect Rate, Mapping Rate or Step Size
    description: "For continuous line scan (transect) and raster mapping: the stage
      translation speed in \xB5m s\u207B\xB9. For mapping, the mapping rate (mm\xB2
      h\u207B\xB9) may be reported as an alternative when scan speed is session-variable.
      For stepped line profiles: the distance between successive spot positions in
      \xB5m."
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsUPbTAPP/transectRateMappingRateOrStepSizeDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: transectRateMappingRateOrStepSizeDefault
      schema:name:
        const: Transect Rate, Mapping Rate or Step Size
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
  laMcicpmsUPb_uncertaintyPropagationMethodDefault:
    title: Uncertainty Propagation Method
    description: 'The approach used to propagate analytical uncertainty through the
      data reduction chain to the final reported value. State which sources are included
      in the propagation: counting statistics, calibration standard uncertainty, internal
      standard uncertainty, drift correction, and any systematic contributions. Distinct
      from Uncertainty Level, which states the convention at which the resulting uncertainty
      is quoted.'
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsUPbTAPP/uncertaintyPropagationMethodDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: uncertaintyPropagationMethodDefault
      schema:name:
        const: Uncertainty Propagation Method
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
  laMcicpms_betweenSessionAnalyticalPrecisionAndAssessmentMethodDefault:
    title: Between-Session (Long-Term) Analytical Precision and Assessment Method
    description: "Precision of measurements across multiple analytical sessions over
      weeks to months \u2014 long-term or intermediate precision \u2014 and the method
      used to assess it. Report both the assessment method and the precision values,
      specifying the reference material, the number of measurements and sessions,
      the time span covered, and the statistic reported."
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethodDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: betweenSessionAnalyticalPrecisionAndAssessmentMethodDefault
      schema:name:
        const: Between-Session (Long-Term) Analytical Precision and Assessment Method
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
  laMcicpms_collisionReactionGasMixtureRatioDefault:
    title: Collision/Reaction Gas Mixture Ratio
    description: Where the collision or reaction cell is supplied with a mixture of
      gases rather than a single gas, the identities and proportions of that mixture.
      Recorded separately from the gas identity. Record 'N/A' where a single gas is
      used.
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsTAPP/collisionReactionGasMixtureRatioDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: collisionReactionGasMixtureRatioDefault
      schema:name:
        const: Collision/Reaction Gas Mixture Ratio
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
  laMcicpms_countingStatisticsErrorDefault:
    title: Counting Statistics Error
    description: "Uncertainty predicted from counting statistics \u2014 the theoretical
      limit set by the Poisson distribution of the counts accumulated \u2014 for each
      reported quantity per analysis, with the sigma level stated. Derived from the
      counts on the analyte together with those on any background or blank subtracted
      from it. Distinct from the scatter actually observed within a measurement or
      between repeated measurements, which is recorded separately."
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsTAPP/countingStatisticsErrorDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: countingStatisticsErrorDefault
      schema:name:
        const: Counting Statistics Error
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
  laMcicpms_detectionLimitDefault:
    title: Detection Limit
    description: Detection limit, one per reported concentration variable (one per
      analyte, these being the same set). State the units and whether the values are
      procedure-typical estimates or session-specific measured values. The calculation
      method is recorded separately in Detection Limit Method. Record 'N/A' where
      the procedure reports no concentrations.
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsTAPP/detectionLimitDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: detectionLimitDefault
      schema:name:
        const: Detection Limit
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
  laMcicpms_doubleSpikeMixingRatioDefault:
    title: Double-Spike Mixing Ratio
    description: "Target proportion of double-spike signal relative to total analyte
      signal in the spiked mixture, expressed as spike fraction (0\u20131) or spike:sample
      ratio. The optimum is analyte-system specific and is typically determined using
      the Double Spike Toolbox or equivalent. The achieved mixing ratio may deviate
      from the target within acceptable bounds (typically \xB120% of optimal); the
      double-spike inversion corrects for actual mixing ratios. Record 'N/A' where
      the procedure does not use a double spike."
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsTAPP/doubleSpikeMixingRatioDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: doubleSpikeMixingRatioDefault
      schema:name:
        const: Double-Spike Mixing Ratio
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
  laMcicpms_doublyChargedSpeciesMonitorDefault:
    title: Doubly-Charged Species Monitor
    description: "The mass ratio monitored to estimate doubly-charged ion (M\xB2\u207A)
      formation during instrument tuning. The monitor species and the mass positions
      monitored should be stated explicitly. Analogous to Oxide Production Method
      and Threshold for oxide monitoring."
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsTAPP/doublyChargedSpeciesMonitorDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: doublyChargedSpeciesMonitorDefault
      schema:name:
        const: Doubly-Charged Species Monitor
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
  laMcicpms_doublyChargedSpeciesProductionDefault:
    title: Doubly-Charged Species Production
    description: Measured percentage of doubly-charged ion production for the monitored
      species at the time of instrument tuning. The acceptable threshold is typically
      <1% or <3%. Record both the threshold and the measured value.
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsTAPP/doublyChargedSpeciesProductionDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: doublyChargedSpeciesProductionDefault
      schema:name:
        const: Doubly-Charged Species Production
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
  laMcicpms_fusionFluxAndDilutionRatioDefault:
    title: Fusion Flux and Dilution Ratio
    description: For procedures using fused glass, the flux type and sample:flux dilution
      ratio used to prepare the analytical glass.
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsTAPP/fusionFluxAndDilutionRatioDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: fusionFluxAndDilutionRatioDefault
      schema:name:
        const: Fusion Flux and Dilution Ratio
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
  laMcicpms_icpTuningDefault:
    title: ICP Tuning
    description: Description of the approach used to optimise ICP plasma conditions
      prior to analysis, including the reference material used for tuning and the
      acceptance criteria (e.g., oxide production threshold, sensitivity targets,
      mass calibration).
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsTAPP/icpTuningDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: icpTuningDefault
      schema:name:
        const: ICP Tuning
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
  laMcicpms_instrumentSerialNumberOrLabIdentifierDefault:
    title: Instrument Serial Number or Lab Identifier
    description: Serial number or laboratory-internal identifier for the specific
      instrument unit.
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsTAPP/instrumentSerialNumberOrLabIdentifierDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: instrumentSerialNumberOrLabIdentifierDefault
      schema:name:
        const: Instrument Serial Number or Lab Identifier
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
  laMcicpms_internalAnalyticalPrecisionAndAssessmentMethodDefault:
    title: Internal (Within-Measurement) Analytical Precision and Assessment Method
    description: Precision of a single measurement, derived from the scatter of the
      cycles, sweeps or integrations that make it up, together with the method used
      to assess it. State the statistic (2SE, 2SD, 1s RSD), the number of cycles it
      is computed over, and the reported quantity it applies to. Distinct from Counting
      Statistics Error, which records the uncertainty predicted from the counts rather
      than the scatter observed; where a procedure reports both, record the observed
      value here and the predicted value there.
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethodDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: internalAnalyticalPrecisionAndAssessmentMethodDefault
      schema:name:
        const: Internal (Within-Measurement) Analytical Precision and Assessment Method
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
  laMcicpms_laserEnergyDefault:
    title: Laser Energy
    description: "Laser pulse energy in millijoules as set at the laser output or
      measured at the sample surface. Report only when the system displays energy
      directly. Laser fluence (J cm\u207B\xB2) is the preferred quantity and is captured
      in Laser Fluence (Energy Density)."
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsTAPP/laserEnergyDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: laserEnergyDefault
      schema:name:
        const: Laser Energy
      ada:dataType:
        const: number
      ada:fieldScope:
        const: session
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:unitText:
        const: mJ
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - ada:fieldScope
  laMcicpms_limitOfQuantificationMethodDefault:
    title: Limit of Quantification (LOQ) Method
    description: 'Reference or description of the method used to calculate the limit
      of quantification (LOQ): the lowest concentration reliably measurable with acceptable
      precision and accuracy. Required when concentrations near the LOD are reported.'
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsTAPP/limitOfQuantificationMethodDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: limitOfQuantificationMethodDefault
      schema:name:
        const: Limit of Quantification (LOQ) Method
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
  laMcicpms_makeUpGasAndFlowRateDefault:
    title: Make-up Gas and Flow Rate
    description: Supplementary gas added to the sample-carrying stream between the
      sample introduction system and the plasma, with its identity and the procedure-registered
      target flow rate. Record any small nitrogen or hydrogen addition with its own
      flow, whose unit commonly differs from the make-up flow. Record 'None' explicitly
      where no supplementary gas is added, to distinguish it from not reported.
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsTAPP/makeUpGasAndFlowRateDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: makeUpGasAndFlowRateDefault
      schema:name:
        const: Make-up Gas and Flow Rate
      ada:dataType:
        const: number
      ada:fieldScope:
        const: session
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:unitText:
        const: L/min
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - ada:fieldScope
  laMcicpms_memoryEffectMitigationDefault:
    title: Memory Effect Mitigation
    description: Procedure applied to identify and minimise carry-over of high-concentration
      or isotopically distinct material from a preceding measurement into the current
      one. Mitigation is applied primarily at measurement time, by allowing sufficient
      washout or rinse between successive introductions. At data processing level,
      record any flagging or exclusion of measurements where the required washout
      may not have been achieved.
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsTAPP/memoryEffectMitigationDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: memoryEffectMitigationDefault
      schema:name:
        const: Memory Effect Mitigation
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
  laMcicpms_normalizationStandardsBasedCorrectionDefault:
    title: Normalization / Standards-Based Correction
    description: "Post-acquisition normalization applied to the reported data beyond
      the primary calibration \u2014 for example correction to a reference value derived
      from secondary reference materials, or correction for a systematic bias those
      materials reveal. Record 'None' if no additional normalization is applied."
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsTAPP/normalizationStandardsBasedCorrectionDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: normalizationStandardsBasedCorrectionDefault
      schema:name:
        const: Normalization / Standards-Based Correction
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
  laMcicpms_numberOfReplicatesDefault:
    title: Number of Replicates
    description: Number of replicate measurements performed on the same sample, or
      on the same nominal location where the technique is spatially resolved. For
      spot analysis this is the number of individual spots per grain or location;
      for transects, the number of replicate lines; for mapping, the number of map
      acquisitions of the same area; for solution work, the number of discrete replicate
      measurements acquired per sample solution.
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsTAPP/numberOfReplicatesDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: numberOfReplicatesDefault
      schema:name:
        const: Number of Replicates
      ada:dataType:
        const: integer
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
  laMcicpms_preAblationSurfaceTreatmentDefault:
    title: Pre-Ablation Surface Treatment
    description: Procedure applied immediately before each analysis to remove surface
      contamination or condition the sample surface. Distinct from general sample
      preparation. For spot analysis, pre-ablation pulses are discarded before signal
      acquisition begins. For mapping, this step is typically omitted.
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsTAPP/preAblationSurfaceTreatmentDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: preAblationSurfaceTreatmentDefault
      schema:name:
        const: Pre-Ablation Surface Treatment
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
  laMcicpms_preAnalysisImagingAndScreeningDefault:
    title: Pre-Analysis Imaging and Screening
    description: Imaging or other characterisation performed before the measurement
      in order to select or locate the sampling unit to be analysed, including the
      technique, instrument and settings used, and how individual analyses are linked
      back to the images. Distinct from any imaging the procedure performs as its
      own measurement. Where the imaging is performed on a separate instrument, it
      should also be recorded in the Group 1 coupling fields.
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsTAPP/preAnalysisImagingAndScreeningDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: preAnalysisImagingAndScreeningDefault
      schema:name:
        const: Pre-Analysis Imaging and Screening
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
  laMcicpms_reactionGasFlowRateDefault:
    title: Reaction Gas Flow Rate
    description: Flow rate of the reactive gas introduced into the dynamic reaction
      cell (DRC), in mL/min. Record 'None' if DRC mode is not used, and 'N/A' where
      Collision/Reaction Cell (CRC) Configuration does not include DRC or the instrument
      has no cell.
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsTAPP/reactionGasFlowRateDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: reactionGasFlowRateDefault
      schema:name:
        const: Reaction Gas Flow Rate
      ada:dataType:
        const: number
      ada:fieldScope:
        const: session
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:unitText:
        const: mL/min
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - ada:fieldScope
  laMcicpms_samplePersistentIdentifierDefault:
    title: Sample Persistent Identifier
    description: Globally unique, persistent identifier for each sample listed in
      Sample Name. IGSN (International Geo Sample Number) is the recommended standard
      for geological and cosmochemical samples, as used by Astromat, EarthChem and
      SESAR. Where a sample and its sub-samples are separately registered, record
      the identifier at the level actually analysed.
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsTAPP/samplePersistentIdentifierDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: samplePersistentIdentifierDefault
      schema:name:
        const: Sample Persistent Identifier
      ada:dataType:
        const: uri
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
  laMcicpms_signalSmoothingDefault:
    title: Signal Smoothing
    description: Description of any signal smoothing device or approach installed
      between the ablation cell and the ICP-MS to reduce pulse-to-pulse signal variability.
      For mapping analyses, report "None" explicitly.
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsTAPP/signalSmoothingDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: signalSmoothingDefault
      schema:name:
        const: Signal Smoothing
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
  laMcicpms_spikeOutlierFilteringApproachDefault:
    title: Spike / Outlier Filtering Approach
    description: Criteria used to identify and exclude anomalous data - signal spikes,
      individual cycles, or whole replicate measurements - before the reported value
      is calculated. State where in the reduction sequence the filter is applied.
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsTAPP/spikeOutlierFilteringApproachDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: spikeOutlierFilteringApproachDefault
      schema:name:
        const: Spike / Outlier Filtering Approach
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
  laMcicpms_torchDepthDefault:
    title: Torch Depth
    description: Distance between the load coil and the sampling cone tip (mm), also
      called injector depth or torch position depending on the instrument manufacturer.
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsTAPP/torchDepthDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: torchDepthDefault
      schema:name:
        const: Torch Depth
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
  laMcicpms_transectRateMappingRateOrStepSizeDefault:
    title: Transect Rate, Mapping Rate or Step Size
    description: "For continuous line scan (transect) and raster mapping: the stage
      translation speed in \xB5m s\u207B\xB9. For mapping, the mapping rate (mm\xB2
      h\u207B\xB9) may be reported as an alternative when scan speed is session-variable.
      For stepped line profiles: the distance between successive spot positions in
      \xB5m."
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsTAPP/transectRateMappingRateOrStepSizeDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: transectRateMappingRateOrStepSizeDefault
      schema:name:
        const: Transect Rate, Mapping Rate or Step Size
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
  laMcicpms_uncertaintyPropagationMethodDefault:
    title: Uncertainty Propagation Method
    description: 'The approach used to propagate analytical uncertainty through the
      data reduction chain to the final reported value. State which sources are included
      in the propagation: counting statistics, calibration standard uncertainty, internal
      standard uncertainty, drift correction, and any systematic contributions. Distinct
      from Uncertainty Level, which states the convention at which the resulting uncertainty
      is quoted.'
    type: object
    properties:
      '@id':
        const: ada:parameter/laMcicpmsTAPP/uncertaintyPropagationMethodDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: uncertaintyPropagationMethodDefault
      schema:name:
        const: Uncertainty Propagation Method
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
  laQicpmsUPb_ageDatumReferenceEpochDefault:
    title: Age Datum / Reference Epoch
    description: 'The zero point from which the reported age is measured, where this
      is not the present day, and the date it corresponds to. Record ''Present day''
      where the conventional datum applies. Where the datum is not the present, record
      it explicitly: year of sample collection for luminescence, end of irradiation
      for 40Ar/39Ar decay corrections.'
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsUPbTAPP/ageDatumReferenceEpochDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: ageDatumReferenceEpochDefault
      schema:name:
        const: Age Datum / Reference Epoch
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
  laQicpmsUPb_betweenSessionAnalyticalPrecisionAndAssessmentMethodDefault:
    title: Between-Session (Long-Term) Analytical Precision and Assessment Method
    description: "Precision of measurements across multiple analytical sessions over
      weeks to months \u2014 long-term or intermediate precision \u2014 and the method
      used to assess it. Report both the assessment method and the precision values,
      specifying the reference material, the number of measurements and sessions,
      the time span covered, and the statistic reported."
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethodDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: betweenSessionAnalyticalPrecisionAndAssessmentMethodDefault
      schema:name:
        const: Between-Session (Long-Term) Analytical Precision and Assessment Method
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
  laQicpmsUPb_collisionReactionGasMixtureRatioDefault:
    title: Collision/Reaction Gas Mixture Ratio
    description: Where the collision or reaction cell is supplied with a mixture of
      gases rather than a single gas, the identities and proportions of that mixture.
      Recorded separately from the gas identity. Record 'N/A' where a single gas is
      used.
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsUPbTAPP/collisionReactionGasMixtureRatioDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: collisionReactionGasMixtureRatioDefault
      schema:name:
        const: Collision/Reaction Gas Mixture Ratio
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
  laQicpmsUPb_countingStatisticsErrorDefault:
    title: Counting Statistics Error
    description: "Uncertainty predicted from counting statistics \u2014 the theoretical
      limit set by the Poisson distribution of the counts accumulated \u2014 for each
      reported quantity per analysis, with the sigma level stated. Derived from the
      counts on the analyte together with those on any background or blank subtracted
      from it. Distinct from the scatter actually observed within a measurement or
      between repeated measurements, which is recorded separately."
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsUPbTAPP/countingStatisticsErrorDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: countingStatisticsErrorDefault
      schema:name:
        const: Counting Statistics Error
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
  laQicpmsUPb_detectionLimitDefault:
    title: Detection Limit
    description: Detection limit, one per reported concentration variable (one per
      analyte, these being the same set). State the units and whether the values are
      procedure-typical estimates or session-specific measured values. The calculation
      method is recorded separately in Detection Limit Method. Record 'N/A' where
      the procedure reports no concentrations.
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsUPbTAPP/detectionLimitDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: detectionLimitDefault
      schema:name:
        const: Detection Limit
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
  laQicpmsUPb_doublyChargedSpeciesMonitorDefault:
    title: Doubly-Charged Species Monitor
    description: "The mass ratio monitored to estimate doubly-charged ion (M\xB2\u207A)
      formation during instrument tuning. The monitor species and the mass positions
      monitored should be stated explicitly. Analogous to Oxide Production Method
      and Threshold for oxide monitoring."
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsUPbTAPP/doublyChargedSpeciesMonitorDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: doublyChargedSpeciesMonitorDefault
      schema:name:
        const: Doubly-Charged Species Monitor
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
  laQicpmsUPb_doublyChargedSpeciesProductionDefault:
    title: Doubly-Charged Species Production
    description: Measured percentage of doubly-charged ion production for the monitored
      species at the time of instrument tuning. The acceptable threshold is typically
      <1% or <3%. Record both the threshold and the measured value.
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsUPbTAPP/doublyChargedSpeciesProductionDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: doublyChargedSpeciesProductionDefault
      schema:name:
        const: Doubly-Charged Species Production
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
  laQicpmsUPb_errorCorrelationBetweenReportedQuantitiesDefault:
    title: Error Correlation Between Reported Quantities
    description: The correlation coefficient between pairs of reported quantities
      whose uncertainties are not independent, together with the pair it applies to
      and how it was obtained.
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsUPbTAPP/errorCorrelationBetweenReportedQuantitiesDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: errorCorrelationBetweenReportedQuantitiesDefault
      schema:name:
        const: Error Correlation Between Reported Quantities
      ada:dataType:
        const: number
      ada:fieldScope:
        const: session
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:unitText:
        const: dimensionless
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - ada:fieldScope
  laQicpmsUPb_fusionFluxAndDilutionRatioDefault:
    title: Fusion Flux and Dilution Ratio
    description: For procedures using fused glass, the flux type and sample:flux dilution
      ratio used to prepare the analytical glass.
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsUPbTAPP/fusionFluxAndDilutionRatioDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: fusionFluxAndDilutionRatioDefault
      schema:name:
        const: Fusion Flux and Dilution Ratio
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
  laQicpmsUPb_icpTuningDefault:
    title: ICP Tuning
    description: Description of the approach used to optimise ICP plasma conditions
      prior to analysis, including the reference material used for tuning and the
      acceptance criteria (e.g., oxide production threshold, sensitivity targets,
      mass calibration).
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsUPbTAPP/icpTuningDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: icpTuningDefault
      schema:name:
        const: ICP Tuning
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
  laQicpmsUPb_instrumentSerialNumberOrLabIdentifierDefault:
    title: Instrument Serial Number or Lab Identifier
    description: Serial number or laboratory-internal identifier for the specific
      instrument unit.
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsUPbTAPP/instrumentSerialNumberOrLabIdentifierDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: instrumentSerialNumberOrLabIdentifierDefault
      schema:name:
        const: Instrument Serial Number or Lab Identifier
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
  laQicpmsUPb_internalAnalyticalPrecisionAndAssessmentMethodDefault:
    title: Internal (Within-Measurement) Analytical Precision and Assessment Method
    description: Precision of a single measurement, derived from the scatter of the
      cycles, sweeps or integrations that make it up, together with the method used
      to assess it. State the statistic (2SE, 2SD, 1s RSD), the number of cycles it
      is computed over, and the reported quantity it applies to. Distinct from Counting
      Statistics Error, which records the uncertainty predicted from the counts rather
      than the scatter observed; where a procedure reports both, record the observed
      value here and the predicted value there.
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsUPbTAPP/internalAnalyticalPrecisionAndAssessmentMethodDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: internalAnalyticalPrecisionAndAssessmentMethodDefault
      schema:name:
        const: Internal (Within-Measurement) Analytical Precision and Assessment Method
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
  laQicpmsUPb_laserEnergyDefault:
    title: Laser Energy
    description: "Laser pulse energy in millijoules as set at the laser output or
      measured at the sample surface. Report only when the system displays energy
      directly. Laser fluence (J cm\u207B\xB2) is the preferred quantity and is captured
      in Laser Fluence (Energy Density)."
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsUPbTAPP/laserEnergyDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: laserEnergyDefault
      schema:name:
        const: Laser Energy
      ada:dataType:
        const: number
      ada:fieldScope:
        const: session
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:unitText:
        const: mJ
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - ada:fieldScope
  laQicpmsUPb_limitOfQuantificationMethodDefault:
    title: Limit of Quantification (LOQ) Method
    description: 'Reference or description of the method used to calculate the limit
      of quantification (LOQ): the lowest concentration reliably measurable with acceptable
      precision and accuracy. Required when concentrations near the LOD are reported.'
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsUPbTAPP/limitOfQuantificationMethodDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: limitOfQuantificationMethodDefault
      schema:name:
        const: Limit of Quantification (LOQ) Method
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
  laQicpmsUPb_makeUpGasAndFlowRateDefault:
    title: Make-up Gas and Flow Rate
    description: Supplementary gas added to the sample-carrying stream between the
      sample introduction system and the plasma, with its identity and the procedure-registered
      target flow rate. Record any small nitrogen or hydrogen addition with its own
      flow, whose unit commonly differs from the make-up flow. Record 'None' explicitly
      where no supplementary gas is added, to distinguish it from not reported.
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsUPbTAPP/makeUpGasAndFlowRateDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: makeUpGasAndFlowRateDefault
      schema:name:
        const: Make-up Gas and Flow Rate
      ada:dataType:
        const: number
      ada:fieldScope:
        const: session
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:unitText:
        const: L/min
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - ada:fieldScope
  laQicpmsUPb_memoryEffectMitigationDefault:
    title: Memory Effect Mitigation
    description: Procedure applied to identify and minimise carry-over of high-concentration
      or isotopically distinct material from a preceding measurement into the current
      one. Mitigation is applied primarily at measurement time, by allowing sufficient
      washout or rinse between successive introductions. At data processing level,
      record any flagging or exclusion of measurements where the required washout
      may not have been achieved.
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsUPbTAPP/memoryEffectMitigationDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: memoryEffectMitigationDefault
      schema:name:
        const: Memory Effect Mitigation
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
  laQicpmsUPb_normalizationStandardsBasedCorrectionDefault:
    title: Normalization / Standards-Based Correction
    description: "Post-acquisition normalization applied to the reported data beyond
      the primary calibration \u2014 for example correction to a reference value derived
      from secondary reference materials, or correction for a systematic bias those
      materials reveal. Record 'None' if no additional normalization is applied."
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsUPbTAPP/normalizationStandardsBasedCorrectionDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: normalizationStandardsBasedCorrectionDefault
      schema:name:
        const: Normalization / Standards-Based Correction
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
  laQicpmsUPb_numberOfReplicatesDefault:
    title: Number of Replicates
    description: Number of replicate measurements performed on the same sample, or
      on the same nominal location where the technique is spatially resolved. For
      spot analysis this is the number of individual spots per grain or location;
      for transects, the number of replicate lines; for mapping, the number of map
      acquisitions of the same area; for solution work, the number of discrete replicate
      measurements acquired per sample solution.
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsUPbTAPP/numberOfReplicatesDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: numberOfReplicatesDefault
      schema:name:
        const: Number of Replicates
      ada:dataType:
        const: integer
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
  laQicpmsUPb_preAblationSurfaceTreatmentDefault:
    title: Pre-Ablation Surface Treatment
    description: Procedure applied immediately before each analysis to remove surface
      contamination or condition the sample surface. Distinct from general sample
      preparation. For spot analysis, pre-ablation pulses are discarded before signal
      acquisition begins. For mapping, this step is typically omitted.
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsUPbTAPP/preAblationSurfaceTreatmentDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: preAblationSurfaceTreatmentDefault
      schema:name:
        const: Pre-Ablation Surface Treatment
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
  laQicpmsUPb_preAnalysisImagingAndScreeningDefault:
    title: Pre-Analysis Imaging and Screening
    description: Imaging or other characterisation performed before the measurement
      in order to select or locate the sampling unit to be analysed, including the
      technique, instrument and settings used, and how individual analyses are linked
      back to the images. Distinct from any imaging the procedure performs as its
      own measurement. Where the imaging is performed on a separate instrument, it
      should also be recorded in the Group 1 coupling fields.
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsUPbTAPP/preAnalysisImagingAndScreeningDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: preAnalysisImagingAndScreeningDefault
      schema:name:
        const: Pre-Analysis Imaging and Screening
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
  laQicpmsUPb_pulseAnalogDetectorNonlinearityCorrectionDefault:
    title: Pulse/Analog Detector Nonlinearity Correction
    description: Whether a correction was applied for nonlinear detector response
      at the transition between pulse-counting and analog (and Faraday, for triple-mode
      instruments) detection modes. Cross-calibration factors between detector modes
      must be confirmed, typically measured each session. Record 'Applied' and describe
      the method, the detector modes involved and the analytes affected; 'None' where
      a crossover exists on this instrument but no correction was made, giving the
      reason; and 'N/A' where the detector is pulse-counting only and no crossover
      exists.
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsUPbTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: pulseAnalogDetectorNonlinearityCorrectionDefault
      schema:name:
        const: Pulse/Analog Detector Nonlinearity Correction
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
  laQicpmsUPb_reactionGasFlowRateDefault:
    title: Reaction Gas Flow Rate
    description: Flow rate of the reactive gas introduced into the dynamic reaction
      cell (DRC), in mL/min. Record 'None' if DRC mode is not used, and 'N/A' where
      Collision/Reaction Cell (CRC) Configuration does not include DRC or the instrument
      has no cell.
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsUPbTAPP/reactionGasFlowRateDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: reactionGasFlowRateDefault
      schema:name:
        const: Reaction Gas Flow Rate
      ada:dataType:
        const: number
      ada:fieldScope:
        const: session
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:unitText:
        const: mL/min
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - ada:fieldScope
  laQicpmsUPb_samplePersistentIdentifierDefault:
    title: Sample Persistent Identifier
    description: Globally unique, persistent identifier for each sample listed in
      Sample Name. IGSN (International Geo Sample Number) is the recommended standard
      for geological and cosmochemical samples, as used by Astromat, EarthChem and
      SESAR. Where a sample and its sub-samples are separately registered, record
      the identifier at the level actually analysed.
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsUPbTAPP/samplePersistentIdentifierDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: samplePersistentIdentifierDefault
      schema:name:
        const: Sample Persistent Identifier
      ada:dataType:
        const: uri
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
  laQicpmsUPb_signalSmoothingDefault:
    title: Signal Smoothing
    description: Description of any signal smoothing device or approach installed
      between the ablation cell and the ICP-MS to reduce pulse-to-pulse signal variability.
      For mapping analyses, report "None" explicitly.
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsUPbTAPP/signalSmoothingDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: signalSmoothingDefault
      schema:name:
        const: Signal Smoothing
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
  laQicpmsUPb_spikeOutlierFilteringApproachDefault:
    title: Spike / Outlier Filtering Approach
    description: Criteria used to identify and exclude anomalous data - signal spikes,
      individual cycles, or whole replicate measurements - before the reported value
      is calculated. State where in the reduction sequence the filter is applied.
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsUPbTAPP/spikeOutlierFilteringApproachDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: spikeOutlierFilteringApproachDefault
      schema:name:
        const: Spike / Outlier Filtering Approach
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
  laQicpmsUPb_torchDepthDefault:
    title: Torch Depth
    description: Distance between the load coil and the sampling cone tip (mm), also
      called injector depth or torch position depending on the instrument manufacturer.
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsUPbTAPP/torchDepthDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: torchDepthDefault
      schema:name:
        const: Torch Depth
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
  laQicpmsUPb_transectRateMappingRateOrStepSizeDefault:
    title: Transect Rate, Mapping Rate or Step Size
    description: "For continuous line scan (transect) and raster mapping: the stage
      translation speed in \xB5m s\u207B\xB9. For mapping, the mapping rate (mm\xB2
      h\u207B\xB9) may be reported as an alternative when scan speed is session-variable.
      For stepped line profiles: the distance between successive spot positions in
      \xB5m."
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsUPbTAPP/transectRateMappingRateOrStepSizeDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: transectRateMappingRateOrStepSizeDefault
      schema:name:
        const: Transect Rate, Mapping Rate or Step Size
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
  laQicpmsUPb_uncertaintyPropagationMethodDefault:
    title: Uncertainty Propagation Method
    description: 'The approach used to propagate analytical uncertainty through the
      data reduction chain to the final reported value. State which sources are included
      in the propagation: counting statistics, calibration standard uncertainty, internal
      standard uncertainty, drift correction, and any systematic contributions. Distinct
      from Uncertainty Level, which states the convention at which the resulting uncertainty
      is quoted.'
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsUPbTAPP/uncertaintyPropagationMethodDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: uncertaintyPropagationMethodDefault
      schema:name:
        const: Uncertainty Propagation Method
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
  laQicpms_betweenSessionAnalyticalPrecisionAndAssessmentMethodDefault:
    title: Between-Session (Long-Term) Analytical Precision and Assessment Method
    description: "Precision of measurements across multiple analytical sessions over
      weeks to months \u2014 long-term or intermediate precision \u2014 and the method
      used to assess it. Report both the assessment method and the precision values,
      specifying the reference material, the number of measurements and sessions,
      the time span covered, and the statistic reported."
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethodDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: betweenSessionAnalyticalPrecisionAndAssessmentMethodDefault
      schema:name:
        const: Between-Session (Long-Term) Analytical Precision and Assessment Method
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
  laQicpms_collisionReactionGasMixtureRatioDefault:
    title: Collision/Reaction Gas Mixture Ratio
    description: Where the collision or reaction cell is supplied with a mixture of
      gases rather than a single gas, the identities and proportions of that mixture.
      Recorded separately from the gas identity. Record 'N/A' where a single gas is
      used.
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsTAPP/collisionReactionGasMixtureRatioDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: collisionReactionGasMixtureRatioDefault
      schema:name:
        const: Collision/Reaction Gas Mixture Ratio
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
  laQicpms_countingStatisticsErrorDefault:
    title: Counting Statistics Error
    description: "Uncertainty predicted from counting statistics \u2014 the theoretical
      limit set by the Poisson distribution of the counts accumulated \u2014 for each
      reported quantity per analysis, with the sigma level stated. Derived from the
      counts on the analyte together with those on any background or blank subtracted
      from it. Distinct from the scatter actually observed within a measurement or
      between repeated measurements, which is recorded separately."
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsTAPP/countingStatisticsErrorDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: countingStatisticsErrorDefault
      schema:name:
        const: Counting Statistics Error
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
  laQicpms_detectionLimitDefault:
    title: Detection Limit
    description: Detection limit, one per reported concentration variable (one per
      analyte, these being the same set). State the units and whether the values are
      procedure-typical estimates or session-specific measured values. The calculation
      method is recorded separately in Detection Limit Method. Record 'N/A' where
      the procedure reports no concentrations.
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsTAPP/detectionLimitDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: detectionLimitDefault
      schema:name:
        const: Detection Limit
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
  laQicpms_doublyChargedSpeciesMonitorDefault:
    title: Doubly-Charged Species Monitor
    description: "The mass ratio monitored to estimate doubly-charged ion (M\xB2\u207A)
      formation during instrument tuning. The monitor species and the mass positions
      monitored should be stated explicitly. Analogous to Oxide Production Method
      and Threshold for oxide monitoring."
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsTAPP/doublyChargedSpeciesMonitorDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: doublyChargedSpeciesMonitorDefault
      schema:name:
        const: Doubly-Charged Species Monitor
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
  laQicpms_doublyChargedSpeciesProductionDefault:
    title: Doubly-Charged Species Production
    description: Measured percentage of doubly-charged ion production for the monitored
      species at the time of instrument tuning. The acceptable threshold is typically
      <1% or <3%. Record both the threshold and the measured value.
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsTAPP/doublyChargedSpeciesProductionDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: doublyChargedSpeciesProductionDefault
      schema:name:
        const: Doubly-Charged Species Production
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
  laQicpms_fusionFluxAndDilutionRatioDefault:
    title: Fusion Flux and Dilution Ratio
    description: For procedures using fused glass, the flux type and sample:flux dilution
      ratio used to prepare the analytical glass.
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsTAPP/fusionFluxAndDilutionRatioDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: fusionFluxAndDilutionRatioDefault
      schema:name:
        const: Fusion Flux and Dilution Ratio
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
  laQicpms_icpTuningDefault:
    title: ICP Tuning
    description: Description of the approach used to optimise ICP plasma conditions
      prior to analysis, including the reference material used for tuning and the
      acceptance criteria (e.g., oxide production threshold, sensitivity targets,
      mass calibration).
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsTAPP/icpTuningDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: icpTuningDefault
      schema:name:
        const: ICP Tuning
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
  laQicpms_instrumentSerialNumberOrLabIdentifierDefault:
    title: Instrument Serial Number or Lab Identifier
    description: Serial number or laboratory-internal identifier for the specific
      instrument unit.
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsTAPP/instrumentSerialNumberOrLabIdentifierDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: instrumentSerialNumberOrLabIdentifierDefault
      schema:name:
        const: Instrument Serial Number or Lab Identifier
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
  laQicpms_internalAnalyticalPrecisionAndAssessmentMethodDefault:
    title: Internal (Within-Measurement) Analytical Precision and Assessment Method
    description: Precision of a single measurement, derived from the scatter of the
      cycles, sweeps or integrations that make it up, together with the method used
      to assess it. State the statistic (2SE, 2SD, 1s RSD), the number of cycles it
      is computed over, and the reported quantity it applies to. Distinct from Counting
      Statistics Error, which records the uncertainty predicted from the counts rather
      than the scatter observed; where a procedure reports both, record the observed
      value here and the predicted value there.
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethodDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: internalAnalyticalPrecisionAndAssessmentMethodDefault
      schema:name:
        const: Internal (Within-Measurement) Analytical Precision and Assessment Method
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
  laQicpms_laserEnergyDefault:
    title: Laser Energy
    description: "Laser pulse energy in millijoules as set at the laser output or
      measured at the sample surface. Report only when the system displays energy
      directly. Laser fluence (J cm\u207B\xB2) is the preferred quantity and is captured
      in Laser Fluence (Energy Density)."
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsTAPP/laserEnergyDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: laserEnergyDefault
      schema:name:
        const: Laser Energy
      ada:dataType:
        const: number
      ada:fieldScope:
        const: session
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:unitText:
        const: mJ
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - ada:fieldScope
  laQicpms_limitOfQuantificationMethodDefault:
    title: Limit of Quantification (LOQ) Method
    description: 'Reference or description of the method used to calculate the limit
      of quantification (LOQ): the lowest concentration reliably measurable with acceptable
      precision and accuracy. Required when concentrations near the LOD are reported.'
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsTAPP/limitOfQuantificationMethodDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: limitOfQuantificationMethodDefault
      schema:name:
        const: Limit of Quantification (LOQ) Method
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
  laQicpms_makeUpGasAndFlowRateDefault:
    title: Make-up Gas and Flow Rate
    description: Supplementary gas added to the sample-carrying stream between the
      sample introduction system and the plasma, with its identity and the procedure-registered
      target flow rate. Record any small nitrogen or hydrogen addition with its own
      flow, whose unit commonly differs from the make-up flow. Record 'None' explicitly
      where no supplementary gas is added, to distinguish it from not reported.
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsTAPP/makeUpGasAndFlowRateDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: makeUpGasAndFlowRateDefault
      schema:name:
        const: Make-up Gas and Flow Rate
      ada:dataType:
        const: number
      ada:fieldScope:
        const: session
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:unitText:
        const: L/min
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - ada:fieldScope
  laQicpms_memoryEffectMitigationDefault:
    title: Memory Effect Mitigation
    description: Procedure applied to identify and minimise carry-over of high-concentration
      or isotopically distinct material from a preceding measurement into the current
      one. Mitigation is applied primarily at measurement time, by allowing sufficient
      washout or rinse between successive introductions. At data processing level,
      record any flagging or exclusion of measurements where the required washout
      may not have been achieved.
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsTAPP/memoryEffectMitigationDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: memoryEffectMitigationDefault
      schema:name:
        const: Memory Effect Mitigation
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
  laQicpms_normalizationStandardsBasedCorrectionDefault:
    title: Normalization / Standards-Based Correction
    description: "Post-acquisition normalization applied to the reported data beyond
      the primary calibration \u2014 for example correction to a reference value derived
      from secondary reference materials, or correction for a systematic bias those
      materials reveal. Record 'None' if no additional normalization is applied."
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsTAPP/normalizationStandardsBasedCorrectionDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: normalizationStandardsBasedCorrectionDefault
      schema:name:
        const: Normalization / Standards-Based Correction
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
  laQicpms_numberOfReplicatesDefault:
    title: Number of Replicates
    description: Number of replicate measurements performed on the same sample, or
      on the same nominal location where the technique is spatially resolved. For
      spot analysis this is the number of individual spots per grain or location;
      for transects, the number of replicate lines; for mapping, the number of map
      acquisitions of the same area; for solution work, the number of discrete replicate
      measurements acquired per sample solution.
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsTAPP/numberOfReplicatesDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: numberOfReplicatesDefault
      schema:name:
        const: Number of Replicates
      ada:dataType:
        const: integer
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
  laQicpms_preAblationSurfaceTreatmentDefault:
    title: Pre-Ablation Surface Treatment
    description: Procedure applied immediately before each analysis to remove surface
      contamination or condition the sample surface. Distinct from general sample
      preparation. For spot analysis, pre-ablation pulses are discarded before signal
      acquisition begins. For mapping, this step is typically omitted.
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsTAPP/preAblationSurfaceTreatmentDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: preAblationSurfaceTreatmentDefault
      schema:name:
        const: Pre-Ablation Surface Treatment
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
  laQicpms_preAnalysisImagingAndScreeningDefault:
    title: Pre-Analysis Imaging and Screening
    description: Imaging or other characterisation performed before the measurement
      in order to select or locate the sampling unit to be analysed, including the
      technique, instrument and settings used, and how individual analyses are linked
      back to the images. Distinct from any imaging the procedure performs as its
      own measurement. Where the imaging is performed on a separate instrument, it
      should also be recorded in the Group 1 coupling fields.
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsTAPP/preAnalysisImagingAndScreeningDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: preAnalysisImagingAndScreeningDefault
      schema:name:
        const: Pre-Analysis Imaging and Screening
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
  laQicpms_pulseAnalogDetectorNonlinearityCorrectionDefault:
    title: Pulse/Analog Detector Nonlinearity Correction
    description: Whether a correction was applied for nonlinear detector response
      at the transition between pulse-counting and analog (and Faraday, for triple-mode
      instruments) detection modes. Cross-calibration factors between detector modes
      must be confirmed, typically measured each session. Record 'Applied' and describe
      the method, the detector modes involved and the analytes affected; 'None' where
      a crossover exists on this instrument but no correction was made, giving the
      reason; and 'N/A' where the detector is pulse-counting only and no crossover
      exists.
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: pulseAnalogDetectorNonlinearityCorrectionDefault
      schema:name:
        const: Pulse/Analog Detector Nonlinearity Correction
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
  laQicpms_reactionGasFlowRateDefault:
    title: Reaction Gas Flow Rate
    description: Flow rate of the reactive gas introduced into the dynamic reaction
      cell (DRC), in mL/min. Record 'None' if DRC mode is not used, and 'N/A' where
      Collision/Reaction Cell (CRC) Configuration does not include DRC or the instrument
      has no cell.
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsTAPP/reactionGasFlowRateDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: reactionGasFlowRateDefault
      schema:name:
        const: Reaction Gas Flow Rate
      ada:dataType:
        const: number
      ada:fieldScope:
        const: session
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:unitText:
        const: mL/min
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - ada:fieldScope
  laQicpms_samplePersistentIdentifierDefault:
    title: Sample Persistent Identifier
    description: Globally unique, persistent identifier for each sample listed in
      Sample Name. IGSN (International Geo Sample Number) is the recommended standard
      for geological and cosmochemical samples, as used by Astromat, EarthChem and
      SESAR. Where a sample and its sub-samples are separately registered, record
      the identifier at the level actually analysed.
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsTAPP/samplePersistentIdentifierDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: samplePersistentIdentifierDefault
      schema:name:
        const: Sample Persistent Identifier
      ada:dataType:
        const: uri
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
  laQicpms_signalSmoothingDefault:
    title: Signal Smoothing
    description: Description of any signal smoothing device or approach installed
      between the ablation cell and the ICP-MS to reduce pulse-to-pulse signal variability.
      For mapping analyses, report "None" explicitly.
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsTAPP/signalSmoothingDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: signalSmoothingDefault
      schema:name:
        const: Signal Smoothing
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
  laQicpms_spikeOutlierFilteringApproachDefault:
    title: Spike / Outlier Filtering Approach
    description: Criteria used to identify and exclude anomalous data - signal spikes,
      individual cycles, or whole replicate measurements - before the reported value
      is calculated. State where in the reduction sequence the filter is applied.
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsTAPP/spikeOutlierFilteringApproachDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: spikeOutlierFilteringApproachDefault
      schema:name:
        const: Spike / Outlier Filtering Approach
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
  laQicpms_torchDepthDefault:
    title: Torch Depth
    description: Distance between the load coil and the sampling cone tip (mm), also
      called injector depth or torch position depending on the instrument manufacturer.
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsTAPP/torchDepthDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: torchDepthDefault
      schema:name:
        const: Torch Depth
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
  laQicpms_transectRateMappingRateOrStepSizeDefault:
    title: Transect Rate, Mapping Rate or Step Size
    description: "For continuous line scan (transect) and raster mapping: the stage
      translation speed in \xB5m s\u207B\xB9. For mapping, the mapping rate (mm\xB2
      h\u207B\xB9) may be reported as an alternative when scan speed is session-variable.
      For stepped line profiles: the distance between successive spot positions in
      \xB5m."
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsTAPP/transectRateMappingRateOrStepSizeDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: transectRateMappingRateOrStepSizeDefault
      schema:name:
        const: Transect Rate, Mapping Rate or Step Size
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
  laQicpms_uncertaintyPropagationMethodDefault:
    title: Uncertainty Propagation Method
    description: 'The approach used to propagate analytical uncertainty through the
      data reduction chain to the final reported value. State which sources are included
      in the propagation: counting statistics, calibration standard uncertainty, internal
      standard uncertainty, drift correction, and any systematic contributions. Distinct
      from Uncertainty Level, which states the convention at which the resulting uncertainty
      is quoted.'
    type: object
    properties:
      '@id':
        const: ada:parameter/laQicpmsTAPP/uncertaintyPropagationMethodDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: uncertaintyPropagationMethodDefault
      schema:name:
        const: Uncertainty Propagation Method
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
  laSficpmsUPb_ageDatumReferenceEpochDefault:
    title: Age Datum / Reference Epoch
    description: 'The zero point from which the reported age is measured, where this
      is not the present day, and the date it corresponds to. Record ''Present day''
      where the conventional datum applies. Where the datum is not the present, record
      it explicitly: year of sample collection for luminescence, end of irradiation
      for 40Ar/39Ar decay corrections.'
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsUPbTAPP/ageDatumReferenceEpochDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: ageDatumReferenceEpochDefault
      schema:name:
        const: Age Datum / Reference Epoch
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
  laSficpmsUPb_betweenSessionAnalyticalPrecisionAndAssessmentMethodDefault:
    title: Between-Session (Long-Term) Analytical Precision and Assessment Method
    description: "Precision of measurements across multiple analytical sessions over
      weeks to months \u2014 long-term or intermediate precision \u2014 and the method
      used to assess it. Report both the assessment method and the precision values,
      specifying the reference material, the number of measurements and sessions,
      the time span covered, and the statistic reported."
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsUPbTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethodDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: betweenSessionAnalyticalPrecisionAndAssessmentMethodDefault
      schema:name:
        const: Between-Session (Long-Term) Analytical Precision and Assessment Method
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
  laSficpmsUPb_countingStatisticsErrorDefault:
    title: Counting Statistics Error
    description: "Uncertainty predicted from counting statistics \u2014 the theoretical
      limit set by the Poisson distribution of the counts accumulated \u2014 for each
      reported quantity per analysis, with the sigma level stated. Derived from the
      counts on the analyte together with those on any background or blank subtracted
      from it. Distinct from the scatter actually observed within a measurement or
      between repeated measurements, which is recorded separately."
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsUPbTAPP/countingStatisticsErrorDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: countingStatisticsErrorDefault
      schema:name:
        const: Counting Statistics Error
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
  laSficpmsUPb_detectionLimitDefault:
    title: Detection Limit
    description: Detection limit, one per reported concentration variable (one per
      analyte, these being the same set). State the units and whether the values are
      procedure-typical estimates or session-specific measured values. The calculation
      method is recorded separately in Detection Limit Method. Record 'N/A' where
      the procedure reports no concentrations.
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsUPbTAPP/detectionLimitDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: detectionLimitDefault
      schema:name:
        const: Detection Limit
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
  laSficpmsUPb_doublyChargedSpeciesMonitorDefault:
    title: Doubly-Charged Species Monitor
    description: "The mass ratio monitored to estimate doubly-charged ion (M\xB2\u207A)
      formation during instrument tuning. The monitor species and the mass positions
      monitored should be stated explicitly. Analogous to Oxide Production Method
      and Threshold for oxide monitoring."
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsUPbTAPP/doublyChargedSpeciesMonitorDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: doublyChargedSpeciesMonitorDefault
      schema:name:
        const: Doubly-Charged Species Monitor
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
  laSficpmsUPb_doublyChargedSpeciesProductionDefault:
    title: Doubly-Charged Species Production
    description: Measured percentage of doubly-charged ion production for the monitored
      species at the time of instrument tuning. The acceptable threshold is typically
      <1% or <3%. Record both the threshold and the measured value.
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsUPbTAPP/doublyChargedSpeciesProductionDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: doublyChargedSpeciesProductionDefault
      schema:name:
        const: Doubly-Charged Species Production
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
  laSficpmsUPb_errorCorrelationBetweenReportedQuantitiesDefault:
    title: Error Correlation Between Reported Quantities
    description: The correlation coefficient between pairs of reported quantities
      whose uncertainties are not independent, together with the pair it applies to
      and how it was obtained.
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsUPbTAPP/errorCorrelationBetweenReportedQuantitiesDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: errorCorrelationBetweenReportedQuantitiesDefault
      schema:name:
        const: Error Correlation Between Reported Quantities
      ada:dataType:
        const: number
      ada:fieldScope:
        const: session
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:unitText:
        const: dimensionless
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - ada:fieldScope
  laSficpmsUPb_fusionFluxAndDilutionRatioDefault:
    title: Fusion Flux and Dilution Ratio
    description: For procedures using fused glass, the flux type and sample:flux dilution
      ratio used to prepare the analytical glass.
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsUPbTAPP/fusionFluxAndDilutionRatioDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: fusionFluxAndDilutionRatioDefault
      schema:name:
        const: Fusion Flux and Dilution Ratio
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
  laSficpmsUPb_icpTuningDefault:
    title: ICP Tuning
    description: Description of the approach used to optimise ICP plasma conditions
      prior to analysis, including the reference material used for tuning and the
      acceptance criteria (e.g., oxide production threshold, sensitivity targets,
      mass calibration).
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsUPbTAPP/icpTuningDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: icpTuningDefault
      schema:name:
        const: ICP Tuning
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
  laSficpmsUPb_instrumentSerialNumberOrLabIdentifierDefault:
    title: Instrument Serial Number or Lab Identifier
    description: Serial number or laboratory-internal identifier for the specific
      instrument unit.
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsUPbTAPP/instrumentSerialNumberOrLabIdentifierDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: instrumentSerialNumberOrLabIdentifierDefault
      schema:name:
        const: Instrument Serial Number or Lab Identifier
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
  laSficpmsUPb_internalAnalyticalPrecisionAndAssessmentMethodDefault:
    title: Internal (Within-Measurement) Analytical Precision and Assessment Method
    description: Precision of a single measurement, derived from the scatter of the
      cycles, sweeps or integrations that make it up, together with the method used
      to assess it. State the statistic (2SE, 2SD, 1s RSD), the number of cycles it
      is computed over, and the reported quantity it applies to. Distinct from Counting
      Statistics Error, which records the uncertainty predicted from the counts rather
      than the scatter observed; where a procedure reports both, record the observed
      value here and the predicted value there.
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsUPbTAPP/internalAnalyticalPrecisionAndAssessmentMethodDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: internalAnalyticalPrecisionAndAssessmentMethodDefault
      schema:name:
        const: Internal (Within-Measurement) Analytical Precision and Assessment Method
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
  laSficpmsUPb_laserEnergyDefault:
    title: Laser Energy
    description: "Laser pulse energy in millijoules as set at the laser output or
      measured at the sample surface. Report only when the system displays energy
      directly. Laser fluence (J cm\u207B\xB2) is the preferred quantity and is captured
      in Laser Fluence (Energy Density)."
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsUPbTAPP/laserEnergyDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: laserEnergyDefault
      schema:name:
        const: Laser Energy
      ada:dataType:
        const: number
      ada:fieldScope:
        const: session
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:unitText:
        const: mJ
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - ada:fieldScope
  laSficpmsUPb_limitOfQuantificationMethodDefault:
    title: Limit of Quantification (LOQ) Method
    description: 'Reference or description of the method used to calculate the limit
      of quantification (LOQ): the lowest concentration reliably measurable with acceptable
      precision and accuracy. Required when concentrations near the LOD are reported.'
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsUPbTAPP/limitOfQuantificationMethodDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: limitOfQuantificationMethodDefault
      schema:name:
        const: Limit of Quantification (LOQ) Method
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
  laSficpmsUPb_makeUpGasAndFlowRateDefault:
    title: Make-up Gas and Flow Rate
    description: Supplementary gas added to the sample-carrying stream between the
      sample introduction system and the plasma, with its identity and the procedure-registered
      target flow rate. Record any small nitrogen or hydrogen addition with its own
      flow, whose unit commonly differs from the make-up flow. Record 'None' explicitly
      where no supplementary gas is added, to distinguish it from not reported.
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsUPbTAPP/makeUpGasAndFlowRateDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: makeUpGasAndFlowRateDefault
      schema:name:
        const: Make-up Gas and Flow Rate
      ada:dataType:
        const: number
      ada:fieldScope:
        const: session
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:unitText:
        const: L/min
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - ada:fieldScope
  laSficpmsUPb_memoryEffectMitigationDefault:
    title: Memory Effect Mitigation
    description: Procedure applied to identify and minimise carry-over of high-concentration
      or isotopically distinct material from a preceding measurement into the current
      one. Mitigation is applied primarily at measurement time, by allowing sufficient
      washout or rinse between successive introductions. At data processing level,
      record any flagging or exclusion of measurements where the required washout
      may not have been achieved.
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsUPbTAPP/memoryEffectMitigationDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: memoryEffectMitigationDefault
      schema:name:
        const: Memory Effect Mitigation
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
  laSficpmsUPb_normalizationStandardsBasedCorrectionDefault:
    title: Normalization / Standards-Based Correction
    description: "Post-acquisition normalization applied to the reported data beyond
      the primary calibration \u2014 for example correction to a reference value derived
      from secondary reference materials, or correction for a systematic bias those
      materials reveal. Record 'None' if no additional normalization is applied."
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsUPbTAPP/normalizationStandardsBasedCorrectionDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: normalizationStandardsBasedCorrectionDefault
      schema:name:
        const: Normalization / Standards-Based Correction
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
  laSficpmsUPb_numberOfReplicatesDefault:
    title: Number of Replicates
    description: Number of replicate measurements performed on the same sample, or
      on the same nominal location where the technique is spatially resolved. For
      spot analysis this is the number of individual spots per grain or location;
      for transects, the number of replicate lines; for mapping, the number of map
      acquisitions of the same area; for solution work, the number of discrete replicate
      measurements acquired per sample solution.
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsUPbTAPP/numberOfReplicatesDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: numberOfReplicatesDefault
      schema:name:
        const: Number of Replicates
      ada:dataType:
        const: integer
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
  laSficpmsUPb_preAblationSurfaceTreatmentDefault:
    title: Pre-Ablation Surface Treatment
    description: Procedure applied immediately before each analysis to remove surface
      contamination or condition the sample surface. Distinct from general sample
      preparation. For spot analysis, pre-ablation pulses are discarded before signal
      acquisition begins. For mapping, this step is typically omitted.
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsUPbTAPP/preAblationSurfaceTreatmentDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: preAblationSurfaceTreatmentDefault
      schema:name:
        const: Pre-Ablation Surface Treatment
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
  laSficpmsUPb_preAnalysisImagingAndScreeningDefault:
    title: Pre-Analysis Imaging and Screening
    description: Imaging or other characterisation performed before the measurement
      in order to select or locate the sampling unit to be analysed, including the
      technique, instrument and settings used, and how individual analyses are linked
      back to the images. Distinct from any imaging the procedure performs as its
      own measurement. Where the imaging is performed on a separate instrument, it
      should also be recorded in the Group 1 coupling fields.
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsUPbTAPP/preAnalysisImagingAndScreeningDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: preAnalysisImagingAndScreeningDefault
      schema:name:
        const: Pre-Analysis Imaging and Screening
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
  laSficpmsUPb_pulseAnalogDetectorNonlinearityCorrectionDefault:
    title: Pulse/Analog Detector Nonlinearity Correction
    description: Whether a correction was applied for nonlinear detector response
      at the transition between pulse-counting and analog (and Faraday, for triple-mode
      instruments) detection modes. Cross-calibration factors between detector modes
      must be confirmed, typically measured each session. Record 'Applied' and describe
      the method, the detector modes involved and the analytes affected; 'None' where
      a crossover exists on this instrument but no correction was made, giving the
      reason; and 'N/A' where the detector is pulse-counting only and no crossover
      exists.
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsUPbTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: pulseAnalogDetectorNonlinearityCorrectionDefault
      schema:name:
        const: Pulse/Analog Detector Nonlinearity Correction
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
  laSficpmsUPb_samplePersistentIdentifierDefault:
    title: Sample Persistent Identifier
    description: Globally unique, persistent identifier for each sample listed in
      Sample Name. IGSN (International Geo Sample Number) is the recommended standard
      for geological and cosmochemical samples, as used by Astromat, EarthChem and
      SESAR. Where a sample and its sub-samples are separately registered, record
      the identifier at the level actually analysed.
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsUPbTAPP/samplePersistentIdentifierDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: samplePersistentIdentifierDefault
      schema:name:
        const: Sample Persistent Identifier
      ada:dataType:
        const: uri
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
  laSficpmsUPb_signalSmoothingDefault:
    title: Signal Smoothing
    description: Description of any signal smoothing device or approach installed
      between the ablation cell and the ICP-MS to reduce pulse-to-pulse signal variability.
      For mapping analyses, report "None" explicitly.
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsUPbTAPP/signalSmoothingDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: signalSmoothingDefault
      schema:name:
        const: Signal Smoothing
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
  laSficpmsUPb_spikeOutlierFilteringApproachDefault:
    title: Spike / Outlier Filtering Approach
    description: Criteria used to identify and exclude anomalous data - signal spikes,
      individual cycles, or whole replicate measurements - before the reported value
      is calculated. State where in the reduction sequence the filter is applied.
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsUPbTAPP/spikeOutlierFilteringApproachDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: spikeOutlierFilteringApproachDefault
      schema:name:
        const: Spike / Outlier Filtering Approach
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
  laSficpmsUPb_torchDepthDefault:
    title: Torch Depth
    description: Distance between the load coil and the sampling cone tip (mm), also
      called injector depth or torch position depending on the instrument manufacturer.
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsUPbTAPP/torchDepthDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: torchDepthDefault
      schema:name:
        const: Torch Depth
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
  laSficpmsUPb_transectRateMappingRateOrStepSizeDefault:
    title: Transect Rate, Mapping Rate or Step Size
    description: "For continuous line scan (transect) and raster mapping: the stage
      translation speed in \xB5m s\u207B\xB9. For mapping, the mapping rate (mm\xB2
      h\u207B\xB9) may be reported as an alternative when scan speed is session-variable.
      For stepped line profiles: the distance between successive spot positions in
      \xB5m."
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsUPbTAPP/transectRateMappingRateOrStepSizeDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: transectRateMappingRateOrStepSizeDefault
      schema:name:
        const: Transect Rate, Mapping Rate or Step Size
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
  laSficpmsUPb_uncertaintyPropagationMethodDefault:
    title: Uncertainty Propagation Method
    description: 'The approach used to propagate analytical uncertainty through the
      data reduction chain to the final reported value. State which sources are included
      in the propagation: counting statistics, calibration standard uncertainty, internal
      standard uncertainty, drift correction, and any systematic contributions. Distinct
      from Uncertainty Level, which states the convention at which the resulting uncertainty
      is quoted.'
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsUPbTAPP/uncertaintyPropagationMethodDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: uncertaintyPropagationMethodDefault
      schema:name:
        const: Uncertainty Propagation Method
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
  laSficpms_betweenSessionAnalyticalPrecisionAndAssessmentMethodDefault:
    title: Between-Session (Long-Term) Analytical Precision and Assessment Method
    description: "Precision of measurements across multiple analytical sessions over
      weeks to months \u2014 long-term or intermediate precision \u2014 and the method
      used to assess it. Report both the assessment method and the precision values,
      specifying the reference material, the number of measurements and sessions,
      the time span covered, and the statistic reported."
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethodDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: betweenSessionAnalyticalPrecisionAndAssessmentMethodDefault
      schema:name:
        const: Between-Session (Long-Term) Analytical Precision and Assessment Method
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
  laSficpms_countingStatisticsErrorDefault:
    title: Counting Statistics Error
    description: "Uncertainty predicted from counting statistics \u2014 the theoretical
      limit set by the Poisson distribution of the counts accumulated \u2014 for each
      reported quantity per analysis, with the sigma level stated. Derived from the
      counts on the analyte together with those on any background or blank subtracted
      from it. Distinct from the scatter actually observed within a measurement or
      between repeated measurements, which is recorded separately."
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsTAPP/countingStatisticsErrorDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: countingStatisticsErrorDefault
      schema:name:
        const: Counting Statistics Error
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
  laSficpms_detectionLimitDefault:
    title: Detection Limit
    description: Detection limit, one per reported concentration variable (one per
      analyte, these being the same set). State the units and whether the values are
      procedure-typical estimates or session-specific measured values. The calculation
      method is recorded separately in Detection Limit Method. Record 'N/A' where
      the procedure reports no concentrations.
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsTAPP/detectionLimitDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: detectionLimitDefault
      schema:name:
        const: Detection Limit
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
  laSficpms_doublyChargedSpeciesMonitorDefault:
    title: Doubly-Charged Species Monitor
    description: "The mass ratio monitored to estimate doubly-charged ion (M\xB2\u207A)
      formation during instrument tuning. The monitor species and the mass positions
      monitored should be stated explicitly. Analogous to Oxide Production Method
      and Threshold for oxide monitoring."
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsTAPP/doublyChargedSpeciesMonitorDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: doublyChargedSpeciesMonitorDefault
      schema:name:
        const: Doubly-Charged Species Monitor
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
  laSficpms_doublyChargedSpeciesProductionDefault:
    title: Doubly-Charged Species Production
    description: Measured percentage of doubly-charged ion production for the monitored
      species at the time of instrument tuning. The acceptable threshold is typically
      <1% or <3%. Record both the threshold and the measured value.
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsTAPP/doublyChargedSpeciesProductionDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: doublyChargedSpeciesProductionDefault
      schema:name:
        const: Doubly-Charged Species Production
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
  laSficpms_fusionFluxAndDilutionRatioDefault:
    title: Fusion Flux and Dilution Ratio
    description: For procedures using fused glass, the flux type and sample:flux dilution
      ratio used to prepare the analytical glass.
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsTAPP/fusionFluxAndDilutionRatioDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: fusionFluxAndDilutionRatioDefault
      schema:name:
        const: Fusion Flux and Dilution Ratio
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
  laSficpms_icpTuningDefault:
    title: ICP Tuning
    description: Description of the approach used to optimise ICP plasma conditions
      prior to analysis, including the reference material used for tuning and the
      acceptance criteria (e.g., oxide production threshold, sensitivity targets,
      mass calibration).
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsTAPP/icpTuningDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: icpTuningDefault
      schema:name:
        const: ICP Tuning
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
  laSficpms_instrumentSerialNumberOrLabIdentifierDefault:
    title: Instrument Serial Number or Lab Identifier
    description: Serial number or laboratory-internal identifier for the specific
      instrument unit.
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsTAPP/instrumentSerialNumberOrLabIdentifierDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: instrumentSerialNumberOrLabIdentifierDefault
      schema:name:
        const: Instrument Serial Number or Lab Identifier
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
  laSficpms_internalAnalyticalPrecisionAndAssessmentMethodDefault:
    title: Internal (Within-Measurement) Analytical Precision and Assessment Method
    description: Precision of a single measurement, derived from the scatter of the
      cycles, sweeps or integrations that make it up, together with the method used
      to assess it. State the statistic (2SE, 2SD, 1s RSD), the number of cycles it
      is computed over, and the reported quantity it applies to. Distinct from Counting
      Statistics Error, which records the uncertainty predicted from the counts rather
      than the scatter observed; where a procedure reports both, record the observed
      value here and the predicted value there.
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethodDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: internalAnalyticalPrecisionAndAssessmentMethodDefault
      schema:name:
        const: Internal (Within-Measurement) Analytical Precision and Assessment Method
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
  laSficpms_laserEnergyDefault:
    title: Laser Energy
    description: "Laser pulse energy in millijoules as set at the laser output or
      measured at the sample surface. Report only when the system displays energy
      directly. Laser fluence (J cm\u207B\xB2) is the preferred quantity and is captured
      in Laser Fluence (Energy Density)."
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsTAPP/laserEnergyDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: laserEnergyDefault
      schema:name:
        const: Laser Energy
      ada:dataType:
        const: number
      ada:fieldScope:
        const: session
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:unitText:
        const: mJ
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - ada:fieldScope
  laSficpms_limitOfQuantificationMethodDefault:
    title: Limit of Quantification (LOQ) Method
    description: 'Reference or description of the method used to calculate the limit
      of quantification (LOQ): the lowest concentration reliably measurable with acceptable
      precision and accuracy. Required when concentrations near the LOD are reported.'
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsTAPP/limitOfQuantificationMethodDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: limitOfQuantificationMethodDefault
      schema:name:
        const: Limit of Quantification (LOQ) Method
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
  laSficpms_makeUpGasAndFlowRateDefault:
    title: Make-up Gas and Flow Rate
    description: Supplementary gas added to the sample-carrying stream between the
      sample introduction system and the plasma, with its identity and the procedure-registered
      target flow rate. Record any small nitrogen or hydrogen addition with its own
      flow, whose unit commonly differs from the make-up flow. Record 'None' explicitly
      where no supplementary gas is added, to distinguish it from not reported.
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsTAPP/makeUpGasAndFlowRateDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: makeUpGasAndFlowRateDefault
      schema:name:
        const: Make-up Gas and Flow Rate
      ada:dataType:
        const: number
      ada:fieldScope:
        const: session
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:unitText:
        const: L/min
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - ada:fieldScope
  laSficpms_memoryEffectMitigationDefault:
    title: Memory Effect Mitigation
    description: Procedure applied to identify and minimise carry-over of high-concentration
      or isotopically distinct material from a preceding measurement into the current
      one. Mitigation is applied primarily at measurement time, by allowing sufficient
      washout or rinse between successive introductions. At data processing level,
      record any flagging or exclusion of measurements where the required washout
      may not have been achieved.
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsTAPP/memoryEffectMitigationDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: memoryEffectMitigationDefault
      schema:name:
        const: Memory Effect Mitigation
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
  laSficpms_normalizationStandardsBasedCorrectionDefault:
    title: Normalization / Standards-Based Correction
    description: "Post-acquisition normalization applied to the reported data beyond
      the primary calibration \u2014 for example correction to a reference value derived
      from secondary reference materials, or correction for a systematic bias those
      materials reveal. Record 'None' if no additional normalization is applied."
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsTAPP/normalizationStandardsBasedCorrectionDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: normalizationStandardsBasedCorrectionDefault
      schema:name:
        const: Normalization / Standards-Based Correction
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
  laSficpms_numberOfReplicatesDefault:
    title: Number of Replicates
    description: Number of replicate measurements performed on the same sample, or
      on the same nominal location where the technique is spatially resolved. For
      spot analysis this is the number of individual spots per grain or location;
      for transects, the number of replicate lines; for mapping, the number of map
      acquisitions of the same area; for solution work, the number of discrete replicate
      measurements acquired per sample solution.
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsTAPP/numberOfReplicatesDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: numberOfReplicatesDefault
      schema:name:
        const: Number of Replicates
      ada:dataType:
        const: integer
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
  laSficpms_preAblationSurfaceTreatmentDefault:
    title: Pre-Ablation Surface Treatment
    description: Procedure applied immediately before each analysis to remove surface
      contamination or condition the sample surface. Distinct from general sample
      preparation. For spot analysis, pre-ablation pulses are discarded before signal
      acquisition begins. For mapping, this step is typically omitted.
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsTAPP/preAblationSurfaceTreatmentDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: preAblationSurfaceTreatmentDefault
      schema:name:
        const: Pre-Ablation Surface Treatment
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
  laSficpms_preAnalysisImagingAndScreeningDefault:
    title: Pre-Analysis Imaging and Screening
    description: Imaging or other characterisation performed before the measurement
      in order to select or locate the sampling unit to be analysed, including the
      technique, instrument and settings used, and how individual analyses are linked
      back to the images. Distinct from any imaging the procedure performs as its
      own measurement. Where the imaging is performed on a separate instrument, it
      should also be recorded in the Group 1 coupling fields.
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsTAPP/preAnalysisImagingAndScreeningDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: preAnalysisImagingAndScreeningDefault
      schema:name:
        const: Pre-Analysis Imaging and Screening
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
  laSficpms_pulseAnalogDetectorNonlinearityCorrectionDefault:
    title: Pulse/Analog Detector Nonlinearity Correction
    description: Whether a correction was applied for nonlinear detector response
      at the transition between pulse-counting and analog (and Faraday, for triple-mode
      instruments) detection modes. Cross-calibration factors between detector modes
      must be confirmed, typically measured each session. Record 'Applied' and describe
      the method, the detector modes involved and the analytes affected; 'None' where
      a crossover exists on this instrument but no correction was made, giving the
      reason; and 'N/A' where the detector is pulse-counting only and no crossover
      exists.
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: pulseAnalogDetectorNonlinearityCorrectionDefault
      schema:name:
        const: Pulse/Analog Detector Nonlinearity Correction
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
  laSficpms_samplePersistentIdentifierDefault:
    title: Sample Persistent Identifier
    description: Globally unique, persistent identifier for each sample listed in
      Sample Name. IGSN (International Geo Sample Number) is the recommended standard
      for geological and cosmochemical samples, as used by Astromat, EarthChem and
      SESAR. Where a sample and its sub-samples are separately registered, record
      the identifier at the level actually analysed.
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsTAPP/samplePersistentIdentifierDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: samplePersistentIdentifierDefault
      schema:name:
        const: Sample Persistent Identifier
      ada:dataType:
        const: uri
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
  laSficpms_signalSmoothingDefault:
    title: Signal Smoothing
    description: Description of any signal smoothing device or approach installed
      between the ablation cell and the ICP-MS to reduce pulse-to-pulse signal variability.
      For mapping analyses, report "None" explicitly.
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsTAPP/signalSmoothingDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: signalSmoothingDefault
      schema:name:
        const: Signal Smoothing
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
  laSficpms_spikeOutlierFilteringApproachDefault:
    title: Spike / Outlier Filtering Approach
    description: Criteria used to identify and exclude anomalous data - signal spikes,
      individual cycles, or whole replicate measurements - before the reported value
      is calculated. State where in the reduction sequence the filter is applied.
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsTAPP/spikeOutlierFilteringApproachDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: spikeOutlierFilteringApproachDefault
      schema:name:
        const: Spike / Outlier Filtering Approach
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
  laSficpms_torchDepthDefault:
    title: Torch Depth
    description: Distance between the load coil and the sampling cone tip (mm), also
      called injector depth or torch position depending on the instrument manufacturer.
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsTAPP/torchDepthDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: torchDepthDefault
      schema:name:
        const: Torch Depth
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
  laSficpms_transectRateMappingRateOrStepSizeDefault:
    title: Transect Rate, Mapping Rate or Step Size
    description: "For continuous line scan (transect) and raster mapping: the stage
      translation speed in \xB5m s\u207B\xB9. For mapping, the mapping rate (mm\xB2
      h\u207B\xB9) may be reported as an alternative when scan speed is session-variable.
      For stepped line profiles: the distance between successive spot positions in
      \xB5m."
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsTAPP/transectRateMappingRateOrStepSizeDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: transectRateMappingRateOrStepSizeDefault
      schema:name:
        const: Transect Rate, Mapping Rate or Step Size
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
  laSficpms_uncertaintyPropagationMethodDefault:
    title: Uncertainty Propagation Method
    description: 'The approach used to propagate analytical uncertainty through the
      data reduction chain to the final reported value. State which sources are included
      in the propagation: counting statistics, calibration standard uncertainty, internal
      standard uncertainty, drift correction, and any systematic contributions. Distinct
      from Uncertainty Level, which states the convention at which the resulting uncertainty
      is quoted.'
    type: object
    properties:
      '@id':
        const: ada:parameter/laSficpmsTAPP/uncertaintyPropagationMethodDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: uncertaintyPropagationMethodDefault
      schema:name:
        const: Uncertainty Propagation Method
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
  labxct_beamHardeningCorrectionParameterDefault:
    title: Beam Hardening Correction Parameter
    description: Numerical value or setting applied in the software beam hardening
      correction algorithm for this specific analysis. Companion to Beam Hardening
      Correction Method.
    type: object
    properties:
      '@id':
        const: ada:parameter/labxctTAPP/beamHardeningCorrectionParameterDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: beamHardeningCorrectionParameterDefault
      schema:name:
        const: Beam Hardening Correction Parameter
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
  labxct_crossValidationProcedureRequirementDefault:
    title: Cross-Validation Procedure Requirement
    description: Specification of what independent analytical validation is required
      to confirm CT segmentation results, phase identification, or quantitative measurements.
      Common approaches include BSE imaging, SEM-EDS or EPMA modal analysis, He pycnometry
      for bulk porosity, and Raman or SIMS phase mapping. Record the required validation
      method(s) and the sampling fraction (e.g., every sample, one per session, or
      a representative subset).
    type: object
    properties:
      '@id':
        const: ada:parameter/labxctTAPP/crossValidationProcedureRequirementDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: crossValidationProcedureRequirementDefault
      schema:name:
        const: Cross-Validation Procedure Requirement
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
  labxct_ctNumberCalibrationDefault:
    title: CT Number Calibration
    description: Whether the raw CT grayscale values have been calibrated to physically
      meaningful units using reference materials.
    type: object
    properties:
      '@id':
        const: ada:parameter/labxctTAPP/ctNumberCalibrationDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: ctNumberCalibrationDefault
      schema:name:
        const: CT Number Calibration
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
  labxct_detectorBinningDefault:
    title: Detector Binning
    description: "Detector pixel binning factor applied during acquisition. Binning
      combines adjacent pixels (e.g., 2\xD72 combines 4 pixels into one)."
    type: object
    properties:
      '@id':
        const: ada:parameter/labxctTAPP/detectorBinningDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: detectorBinningDefault
      schema:name:
        const: Detector Binning
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
  labxct_framesAveragedPerProjectionDefault:
    title: Frames Averaged per Projection
    description: "Number of individual detector frames acquired and averaged to produce
      each saved projection image. The effective exposure per projection = exposure
      time per frame \xD7 frames averaged."
    type: object
    properties:
      '@id':
        const: ada:parameter/labxctTAPP/framesAveragedPerProjectionDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: framesAveragedPerProjectionDefault
      schema:name:
        const: Frames Averaged per Projection
      ada:dataType:
        const: integer
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
  labxct_outputBitDepthDefault:
    title: Output Bit Depth
    description: Bit depth of the reconstructed 3D volume (number of bits used to
      encode each voxel's grayscale value). Common values are 8-bit (256 gray levels),
      16-bit (65,536 gray levels), or 32-bit floating point. A required output bit
      depth may be specified if downstream analysis workflows depend on a consistent
      grayscale range.
    type: object
    properties:
      '@id':
        const: ada:parameter/labxctTAPP/outputBitDepthDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: outputBitDepthDefault
      schema:name:
        const: Output Bit Depth
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
  labxct_partialVolumeEffectCriteriaDefault:
    title: Partial Volume Effect Criteria
    description: "Specification of how partial volume effects (PVE) are managed in
      quantitative analysis. PVE correction can be implemented via PSF-based deconvolution
      tools such as Blob3D. Record the minimum feature size criterion adopted for
      the procedure (in voxels or \xB5m), the basis for it, the treatment of boundary
      voxels in modal abundance or size distribution calculations, and whether PVE
      correction is required or optional. State whether the criterion follows the
      Withers et al. (2021) convention \u2014 a feature must span at least 3 voxels
      to be positively identified and at least 10 for reliable shape and volume characterisation
      \u2014 or is SNR-limited, PVE-limited or analyst-defined."
    type: object
    properties:
      '@id':
        const: ada:parameter/labxctTAPP/partialVolumeEffectCriteriaDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: partialVolumeEffectCriteriaDefault
      schema:name:
        const: Partial Volume Effect Criteria
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
  labxct_phaseIdentificationMethodDefault:
    title: Phase Identification Method
    description: Method used to assign reconstructed CT number ranges to specific
      mineral phases or material types. Approaches include comparison to calculated
      linear attenuation coefficients (LAC), cross-validation with independent analytical
      techniques, or empirical calibration.
    type: object
    properties:
      '@id':
        const: ada:parameter/labxctTAPP/phaseIdentificationMethodDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: phaseIdentificationMethodDefault
      schema:name:
        const: Phase Identification Method
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
  labxct_preAnalysisImagingAndScreeningDefault:
    title: Pre-Analysis Imaging and Screening
    description: Imaging or other characterisation performed before the measurement
      in order to select or locate the sampling unit to be analysed, including the
      technique, instrument and settings used, and how individual analyses are linked
      back to the images. Distinct from any imaging the procedure performs as its
      own measurement. Where the imaging is performed on a separate instrument, it
      should also be recorded in the Group 1 coupling fields.
    type: object
    properties:
      '@id':
        const: ada:parameter/labxctTAPP/preAnalysisImagingAndScreeningDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: preAnalysisImagingAndScreeningDefault
      schema:name:
        const: Pre-Analysis Imaging and Screening
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
  labxct_reconstructionConvolutionFilterDefault:
    title: Reconstruction Convolution Filter
    description: Convolution (apodization) filter kernel applied during back-projection
      reconstruction.
    type: object
    properties:
      '@id':
        const: ada:parameter/labxctTAPP/reconstructionConvolutionFilterDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: reconstructionConvolutionFilterDefault
      schema:name:
        const: Reconstruction Convolution Filter
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
  labxct_ringArtifactCorrectionMethodDefault:
    title: Ring Artifact Correction Method
    description: Procedure specification for how ring artifacts are handled. Whether
      correction was applied and its outcome are recorded separately in Group 6.
    type: object
    properties:
      '@id':
        const: ada:parameter/labxctTAPP/ringArtifactCorrectionMethodDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: ringArtifactCorrectionMethodDefault
      schema:name:
        const: Ring Artifact Correction Method
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
  labxct_rotationStepSizeDefault:
    title: Rotation Step Size
    description: Angular increment between successive projection images, in degrees.
      Equal to Rotation Range divided by Number of Projections when both are reported;
      however, some sources report step size as the primary rotation parameter without
      stating the total number of projections explicitly.
    type: object
    properties:
      '@id':
        const: ada:parameter/labxctTAPP/rotationStepSizeDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: rotationStepSizeDefault
      schema:name:
        const: Rotation Step Size
      ada:dataType:
        const: number
      ada:fieldScope:
        const: session
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:unitText:
        const: "\xB0"
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - ada:fieldScope
  labxct_sampleDimensionsDefault:
    title: "Sample Dimensions (L \xD7 W \xD7 H)"
    description: "Physical dimensions of the sample in mm, reported as length \xD7
      width \xD7 height (or equivalent three orthogonal measurements)."
    type: object
    properties:
      '@id':
        const: ada:parameter/labxctTAPP/sampleDimensionsDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: sampleDimensionsDefault
      schema:name:
        const: "Sample Dimensions (L \xD7 W \xD7 H)"
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
  labxct_sampleMountingMethodDefault:
    title: Sample Mounting Method
    description: "Method used to mount or hold the sample on the instrument rotation
      stage. Mounting material should transmit X-rays at the selected voltage without
      dominating beam attenuation. Report the holder CLASS from the list and name
      the specific vessel or material alongside it \u2014 'Tube or vial \u2014 1 cm
      plastic straw', not 'Tube or vial'. Where the sample is sealed or bagged inside
      a further holder for contamination control, record both layers. Report any adhesive,
      support material and alignment aids used."
    type: object
    properties:
      '@id':
        const: ada:parameter/labxctTAPP/sampleMountingMethodDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: sampleMountingMethodDefault
      schema:name:
        const: Sample Mounting Method
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
  labxct_samplePersistentIdentifierDefault:
    title: Sample Persistent Identifier
    description: Globally unique, persistent identifier for each sample listed in
      Sample Name. IGSN (International Geo Sample Number) is the recommended standard
      for geological and cosmochemical samples, as used by Astromat, EarthChem and
      SESAR. Where a sample and its sub-samples are separately registered, record
      the identifier at the level actually analysed.
    type: object
    properties:
      '@id':
        const: ada:parameter/labxctTAPP/samplePersistentIdentifierDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: samplePersistentIdentifierDefault
      schema:name:
        const: Sample Persistent Identifier
      ada:dataType:
        const: uri
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
  labxct_samplePreparationNotesDefault:
    title: Sample Preparation Notes
    description: Any preparation steps applied to the sample before scanning, including
      cleaning, trimming, consolidation, or drying. Note any exceptions.
    type: object
    properties:
      '@id':
        const: ada:parameter/labxctTAPP/samplePreparationNotesDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: samplePreparationNotesDefault
      schema:name:
        const: Sample Preparation Notes
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
  labxct_segmentationThresholdValuesOrCriteriaDefault:
    title: Segmentation Threshold Values or Criteria
    description: "Specific CT number range(s) or quantitative criteria used to define
      each segmented phase or feature. For LAC-calibrated datasets, report values
      in cm\u207B\xB9."
    type: object
    properties:
      '@id':
        const: ada:parameter/labxctTAPP/segmentationThresholdValuesOrCriteriaDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: segmentationThresholdValuesOrCriteriaDefault
      schema:name:
        const: Segmentation Threshold Values or Criteria
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
  labxct_sourceToDetectorDistanceDefault:
    title: Source-to-Detector Distance (SDD)
    description: "Distance from the X-ray source focal spot to the detector surface,
      in mm. Voxel size \u2248 detector pixel size / M (before binning; divide additionally
      by optical objective for Versa-class systems)."
    type: object
    properties:
      '@id':
        const: ada:parameter/labxctTAPP/sourceToDetectorDistanceDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: sourceToDetectorDistanceDefault
      schema:name:
        const: Source-to-Detector Distance (SDD)
      ada:dataType:
        const: number
      ada:fieldScope:
        const: session
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:unitText:
        const: mm
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - ada:fieldScope
  labxct_sourceToObjectDistanceDefault:
    title: Source-to-Object Distance (SOD)
    description: Distance from the X-ray source focal spot to the centre of the sample
      rotation axis, in mm.
    type: object
    properties:
      '@id':
        const: ada:parameter/labxctTAPP/sourceToObjectDistanceDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: sourceToObjectDistanceDefault
      schema:name:
        const: Source-to-Object Distance (SOD)
      ada:dataType:
        const: number
      ada:fieldScope:
        const: session
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:unitText:
        const: mm
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - ada:fieldScope
  labxct_voiSelectionCriteriaDefault:
    title: VOI Selection Criteria
    description: Rules specifying how the Volume of Interest (VOI) is to be defined
      for quantitative analysis. Common criteria exclude cone-beam artifact zones
      at sample edges, beam hardening halos near dense inclusions, and sample holder
      signal. The actual VOI applied in a specific analysis is recorded separately
      at analysis level.
    type: object
    properties:
      '@id':
        const: ada:parameter/labxctTAPP/voiSelectionCriteriaDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: voiSelectionCriteriaDefault
      schema:name:
        const: VOI Selection Criteria
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
  labxct_xRayPowerDefault:
    title: X-ray Power
    description: "X-ray tube power in watts (W). Derivable as voltage (kV) \xD7 current
      (mA) = kV \xD7 \xB5A / 1000. If power was varied across samples within the session,
      report the full range applied (e.g., 7\u201313 W)."
    type: object
    properties:
      '@id':
        const: ada:parameter/labxctTAPP/xRayPowerDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: xRayPowerDefault
      schema:name:
        const: X-ray Power
      ada:dataType:
        const: number
      ada:fieldScope:
        const: session
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:unitText:
        const: W
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - ada:fieldScope
  semComposition_analyticalAccuracyDefault:
    title: Analytical Accuracy
    description: Offset between measured and accepted reference values for secondary
      standards, expressed as percent relative bias. Include reference material, reference
      value source, and the measured value.
    type: object
    properties:
      '@id':
        const: ada:parameter/semCompositionTAPP/analyticalAccuracyDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: analyticalAccuracyDefault
      schema:name:
        const: Analytical Accuracy
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
  semComposition_analyticalPrecisionDefault:
    title: Analytical Precision
    description: Reproducibility of repeated measurements on the same or equivalent
      reference material, expressed as 1-sigma relative standard deviation (%). Include
      reference material name, number of analyses (n), and the measured value.
    type: object
    properties:
      '@id':
        const: ada:parameter/semCompositionTAPP/analyticalPrecisionDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: analyticalPrecisionDefault
      schema:name:
        const: Analytical Precision
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
  semComposition_backgroundPositionDefault:
    title: Background Position(s)
    description: Location(s) of off-peak background measurement(s) relative to the
      peak, in mm or sin-theta, and whether on the high- or low-energy side.
    type: object
    properties:
      '@id':
        const: ada:parameter/semCompositionTAPP/backgroundPositionDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: backgroundPositionDefault
      schema:name:
        const: Background Position(s)
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
  semComposition_beamDamageMinimizationDefault:
    title: Beam Damage Minimization
    description: 'Describes any measures taken to reduce electron beam damage to the
      sample during analysis. Examples: reduced accelerating voltage, lowered beam
      current, defocused or rastered beam, cooled stage, short acquisition sequences,
      or rotating between multiple points.'
    type: object
    properties:
      '@id':
        const: ada:parameter/semCompositionTAPP/beamDamageMinimizationDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: beamDamageMinimizationDefault
      schema:name:
        const: Beam Damage Minimization
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
  semComposition_beamRasterDimensionsDefault:
    title: Beam Raster Dimensions
    description: "Dimensions of the small area over which the beam is rastered at
      a single analysis point, reported as width \xD7 height in \xB5m. Applicable
      when Beam Mode = Rastered; defines the effective spatial footprint of the measurement.
      Not applicable when mapping."
    type: object
    properties:
      '@id':
        const: ada:parameter/semCompositionTAPP/beamRasterDimensionsDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: beamRasterDimensionsDefault
      schema:name:
        const: Beam Raster Dimensions
      ada:dataType:
        const: number
      ada:fieldScope:
        const: session
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:unitText:
        const: "\xB5m x \xB5m"
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - ada:fieldScope
  semComposition_blankCorrectionDefault:
    title: Blank Correction
    description: Method and reference material(s) used to determine and subtract blank
      signal contributions (e.g., carbon coat contribution to C signal, or background
      contamination for trace elements).
    type: object
    properties:
      '@id':
        const: ada:parameter/semCompositionTAPP/blankCorrectionDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: blankCorrectionDefault
      schema:name:
        const: Blank Correction
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
  semComposition_chamberPressureDefault:
    title: Chamber Pressure
    description: Chamber pressure and gas type during analysis. Required for variable
      pressure (VP-SEM) and environmental SEM (ESEM) modes. Report value and unit
      (Pa or Torr) and gas composition. Use 'None' for standard high-vacuum operation.
    type: object
    properties:
      '@id':
        const: ada:parameter/semCompositionTAPP/chamberPressureDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: chamberPressureDefault
      schema:name:
        const: Chamber Pressure
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
  semComposition_countingStatisticsErrorDefault:
    title: Counting Statistics Error
    description: "Uncertainty predicted from counting statistics \u2014 the theoretical
      limit set by the Poisson distribution of the counts accumulated \u2014 for each
      reported quantity per analysis, with the sigma level stated. Derived from the
      counts on the analyte together with those on any background or blank subtracted
      from it. Distinct from the scatter actually observed within a measurement or
      between repeated measurements, which is recorded separately."
    type: object
    properties:
      '@id':
        const: ada:parameter/semCompositionTAPP/countingStatisticsErrorDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: countingStatisticsErrorDefault
      schema:name:
        const: Counting Statistics Error
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
  semComposition_detectionLimitDefault:
    title: Detection Limit
    description: Detection limit, one per reported concentration variable (one per
      analyte, these being the same set). State the units and whether the values are
      procedure-typical estimates or session-specific measured values. The calculation
      method is recorded separately in Detection Limit Method. Record 'N/A' where
      the procedure reports no concentrations.
    type: object
    properties:
      '@id':
        const: ada:parameter/semCompositionTAPP/detectionLimitDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: detectionLimitDefault
      schema:name:
        const: Detection Limit
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
  semComposition_driftCorrectionDefault:
    title: Drift Correction
    description: 'Describes whether and how stage or beam drift was monitored and
      corrected during the measurement session. Examples: periodic stage realignment
      to a fiducial marker, automated beam drift correction in acquisition software,
      or reanalysis of a reference point at regular intervals.'
    type: object
    properties:
      '@id':
        const: ada:parameter/semCompositionTAPP/driftCorrectionDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: driftCorrectionDefault
      schema:name:
        const: Drift Correction
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
  semComposition_halogenCorrectionOnOxygenDefault:
    title: Halogen Correction on Oxygen
    description: Whether oxygen content was adjusted to account for halogen substitution
      (F and/or Cl replacing OH) in halogen-bearing phases such as apatite, amphibole,
      and mica, where oxygen is calculated by stoichiometry.
    type: object
    properties:
      '@id':
        const: ada:parameter/semCompositionTAPP/halogenCorrectionOnOxygenDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: halogenCorrectionOnOxygenDefault
      schema:name:
        const: Halogen Correction on Oxygen
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
  semComposition_normalizationStandardsBasedCorrectionDefault:
    title: Normalization / Standards-Based Correction
    description: "Post-acquisition normalization applied to the reported data beyond
      the primary calibration \u2014 for example correction to a reference value derived
      from secondary reference materials, or correction for a systematic bias those
      materials reveal. Record 'None' if no additional normalization is applied."
    type: object
    properties:
      '@id':
        const: ada:parameter/semCompositionTAPP/normalizationStandardsBasedCorrectionDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: normalizationStandardsBasedCorrectionDefault
      schema:name:
        const: Normalization / Standards-Based Correction
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
  semComposition_preAnalysisImagingAndScreeningDefault:
    title: Pre-Analysis Imaging and Screening
    description: Imaging or other characterisation performed before the measurement
      in order to select or locate the sampling unit to be analysed, including the
      technique, instrument and settings used, and how individual analyses are linked
      back to the images. Distinct from any imaging the procedure performs as its
      own measurement. Where the imaging is performed on a separate instrument, it
      should also be recorded in the Group 1 coupling fields.
    type: object
    properties:
      '@id':
        const: ada:parameter/semCompositionTAPP/preAnalysisImagingAndScreeningDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: preAnalysisImagingAndScreeningDefault
      schema:name:
        const: Pre-Analysis Imaging and Screening
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
  semComposition_samplePersistentIdentifierDefault:
    title: Sample Persistent Identifier
    description: Globally unique, persistent identifier for each sample listed in
      Sample Name. IGSN (International Geo Sample Number) is the recommended standard
      for geological and cosmochemical samples, as used by Astromat, EarthChem and
      SESAR. Where a sample and its sub-samples are separately registered, record
      the identifier at the level actually analysed.
    type: object
    properties:
      '@id':
        const: ada:parameter/semCompositionTAPP/samplePersistentIdentifierDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: samplePersistentIdentifierDefault
      schema:name:
        const: Sample Persistent Identifier
      ada:dataType:
        const: uri
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
  semComposition_timeDependentIntensityCorrectionDefault:
    title: Time-Dependent Intensity Correction
    description: Type of time-dependent intensity (TDI) correction applied to compensate
      for beam-induced volatilisation or migration of sensitive elements (e.g., Na,
      K, F in glasses, feldspars, carbonates).
    type: object
    properties:
      '@id':
        const: ada:parameter/semCompositionTAPP/timeDependentIntensityCorrectionDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: timeDependentIntensityCorrectionDefault
      schema:name:
        const: Time-Dependent Intensity Correction
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
  semFibsem_preAnalysisImagingAndScreeningDefault:
    title: Pre-Analysis Imaging and Screening
    description: Imaging or other characterisation performed before the measurement
      in order to select or locate the sampling unit to be analysed, including the
      technique, instrument and settings used, and how individual analyses are linked
      back to the images. Distinct from any imaging the procedure performs as its
      own measurement. Where the imaging is performed on a separate instrument, it
      should also be recorded in the Group 1 coupling fields.
    type: object
    properties:
      '@id':
        const: ada:parameter/semFibsemTAPP/preAnalysisImagingAndScreeningDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: preAnalysisImagingAndScreeningDefault
      schema:name:
        const: Pre-Analysis Imaging and Screening
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
  semFibsem_samplePersistentIdentifierDefault:
    title: Sample Persistent Identifier
    description: Globally unique, persistent identifier for each sample listed in
      Sample Name. IGSN (International Geo Sample Number) is the recommended standard
      for geological and cosmochemical samples, as used by Astromat, EarthChem and
      SESAR. Where a sample and its sub-samples are separately registered, record
      the identifier at the level actually analysed.
    type: object
    properties:
      '@id':
        const: ada:parameter/semFibsemTAPP/samplePersistentIdentifierDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: samplePersistentIdentifierDefault
      schema:name:
        const: Sample Persistent Identifier
      ada:dataType:
        const: uri
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
  semImaging_chamberPressureDefault:
    title: Chamber Pressure
    description: Chamber pressure and gas type during analysis. Required for variable
      pressure (VP-SEM) and environmental SEM (ESEM) modes. Report value and unit
      (Pa or Torr) and gas composition. Use 'None' for standard high-vacuum operation.
    type: object
    properties:
      '@id':
        const: ada:parameter/semImagingTAPP/chamberPressureDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: chamberPressureDefault
      schema:name:
        const: Chamber Pressure
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
  semImaging_clWavelengthCalibrationReferenceDefault:
    title: CL Wavelength Calibration Reference
    description: Reference light source or standard material used to calibrate the
      wavelength axis of the CL spectrometer. Required for quantitative spectral CL
      and hyperspectral mapping.
    type: object
    properties:
      '@id':
        const: ada:parameter/semImagingTAPP/clWavelengthCalibrationReferenceDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: clWavelengthCalibrationReferenceDefault
      schema:name:
        const: CL Wavelength Calibration Reference
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
  semImaging_ebsdFrameTimeDefault:
    title: EBSD Frame Time
    description: Acquisition time per EBSD diffraction pattern frame in milliseconds.
    type: object
    properties:
      '@id':
        const: ada:parameter/semImagingTAPP/ebsdFrameTimeDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: ebsdFrameTimeDefault
      schema:name:
        const: EBSD Frame Time
      ada:dataType:
        const: number
      ada:fieldScope:
        const: session
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:unitText:
        const: ms
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - ada:fieldScope
  semImaging_ebsdPatternQualityThresholdDefault:
    title: EBSD Pattern Quality Threshold
    description: Minimum pattern quality or confidence index threshold applied during
      EBSD data processing to exclude unreliably indexed points from orientation maps.
      Include metric name and threshold value.
    type: object
    properties:
      '@id':
        const: ada:parameter/semImagingTAPP/ebsdPatternQualityThresholdDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: ebsdPatternQualityThresholdDefault
      schema:name:
        const: EBSD Pattern Quality Threshold
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
  semImaging_imagePixelSizeDefault:
    title: Image Pixel Size
    description: "Physical size of each image pixel at the sample surface, in nm or
      \xB5m. For large-area mosaic imaging, report the pixel size of individual tiles
      and the number and arrangement of tiles."
    type: object
    properties:
      '@id':
        const: ada:parameter/semImagingTAPP/imagePixelSizeDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: imagePixelSizeDefault
      schema:name:
        const: Image Pixel Size
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
  semImaging_preAnalysisImagingAndScreeningDefault:
    title: Pre-Analysis Imaging and Screening
    description: Imaging or other characterisation performed before the measurement
      in order to select or locate the sampling unit to be analysed, including the
      technique, instrument and settings used, and how individual analyses are linked
      back to the images. Distinct from any imaging the procedure performs as its
      own measurement. Where the imaging is performed on a separate instrument, it
      should also be recorded in the Group 1 coupling fields.
    type: object
    properties:
      '@id':
        const: ada:parameter/semImagingTAPP/preAnalysisImagingAndScreeningDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: preAnalysisImagingAndScreeningDefault
      schema:name:
        const: Pre-Analysis Imaging and Screening
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
  semImaging_samplePersistentIdentifierDefault:
    title: Sample Persistent Identifier
    description: Globally unique, persistent identifier for each sample listed in
      Sample Name. IGSN (International Geo Sample Number) is the recommended standard
      for geological and cosmochemical samples, as used by Astromat, EarthChem and
      SESAR. Where a sample and its sub-samples are separately registered, record
      the identifier at the level actually analysed.
    type: object
    properties:
      '@id':
        const: ada:parameter/semImagingTAPP/samplePersistentIdentifierDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: samplePersistentIdentifierDefault
      schema:name:
        const: Sample Persistent Identifier
      ada:dataType:
        const: uri
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
  sem_analyticalAccuracyDefault:
    title: Analytical Accuracy
    description: Offset between measured and accepted reference values for secondary
      standards, expressed as percent relative bias. Include reference material, reference
      value source, and the measured value.
    type: object
    properties:
      '@id':
        const: ada:parameter/semTAPP/analyticalAccuracyDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: analyticalAccuracyDefault
      schema:name:
        const: Analytical Accuracy
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
  sem_analyticalPrecisionDefault:
    title: Analytical Precision
    description: Reproducibility of repeated measurements on the same or equivalent
      reference material, expressed as 1-sigma relative standard deviation (%). Include
      reference material name, number of analyses (n), and the measured value.
    type: object
    properties:
      '@id':
        const: ada:parameter/semTAPP/analyticalPrecisionDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: analyticalPrecisionDefault
      schema:name:
        const: Analytical Precision
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
  sem_backgroundPositionDefault:
    title: Background Position(s)
    description: Location(s) of off-peak background measurement(s) relative to the
      peak, in mm or sin-theta, and whether on the high- or low-energy side.
    type: object
    properties:
      '@id':
        const: ada:parameter/semTAPP/backgroundPositionDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: backgroundPositionDefault
      schema:name:
        const: Background Position(s)
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
  sem_beamDamageMinimizationDefault:
    title: Beam Damage Minimization
    description: 'Describes any measures taken to reduce electron beam damage to the
      sample during analysis. Examples: reduced accelerating voltage, lowered beam
      current, defocused or rastered beam, cooled stage, short acquisition sequences,
      or rotating between multiple points.'
    type: object
    properties:
      '@id':
        const: ada:parameter/semTAPP/beamDamageMinimizationDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: beamDamageMinimizationDefault
      schema:name:
        const: Beam Damage Minimization
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
  sem_beamRasterDimensionsDefault:
    title: Beam Raster Dimensions
    description: "Dimensions of the small area over which the beam is rastered at
      a single analysis point, reported as width \xD7 height in \xB5m. Applicable
      when Beam Mode = Rastered; defines the effective spatial footprint of the measurement.
      Not applicable when mapping."
    type: object
    properties:
      '@id':
        const: ada:parameter/semTAPP/beamRasterDimensionsDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: beamRasterDimensionsDefault
      schema:name:
        const: Beam Raster Dimensions
      ada:dataType:
        const: number
      ada:fieldScope:
        const: session
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:unitText:
        const: "\xB5m x \xB5m"
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - ada:fieldScope
  sem_blankCorrectionDefault:
    title: Blank Correction
    description: Method and reference material(s) used to determine and subtract blank
      signal contributions (e.g., carbon coat contribution to C signal, or background
      contamination for trace elements).
    type: object
    properties:
      '@id':
        const: ada:parameter/semTAPP/blankCorrectionDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: blankCorrectionDefault
      schema:name:
        const: Blank Correction
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
  sem_chamberPressureDefault:
    title: Chamber Pressure
    description: Chamber pressure and gas type during analysis. Required for variable
      pressure (VP-SEM) and environmental SEM (ESEM) modes. Report value and unit
      (Pa or Torr) and gas composition. Use 'None' for standard high-vacuum operation.
    type: object
    properties:
      '@id':
        const: ada:parameter/semTAPP/chamberPressureDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: chamberPressureDefault
      schema:name:
        const: Chamber Pressure
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
  sem_clWavelengthCalibrationReferenceDefault:
    title: CL Wavelength Calibration Reference
    description: Reference light source or standard material used to calibrate the
      wavelength axis of the CL spectrometer. Required for quantitative spectral CL
      and hyperspectral mapping.
    type: object
    properties:
      '@id':
        const: ada:parameter/semTAPP/clWavelengthCalibrationReferenceDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: clWavelengthCalibrationReferenceDefault
      schema:name:
        const: CL Wavelength Calibration Reference
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
  sem_countingStatisticsErrorDefault:
    title: Counting Statistics Error
    description: "Uncertainty predicted from counting statistics \u2014 the theoretical
      limit set by the Poisson distribution of the counts accumulated \u2014 for each
      reported quantity per analysis, with the sigma level stated. Derived from the
      counts on the analyte together with those on any background or blank subtracted
      from it. Distinct from the scatter actually observed within a measurement or
      between repeated measurements, which is recorded separately."
    type: object
    properties:
      '@id':
        const: ada:parameter/semTAPP/countingStatisticsErrorDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: countingStatisticsErrorDefault
      schema:name:
        const: Counting Statistics Error
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
  sem_detectionLimitDefault:
    title: Detection Limit
    description: Detection limit, one per reported concentration variable (one per
      analyte, these being the same set). State the units and whether the values are
      procedure-typical estimates or session-specific measured values. The calculation
      method is recorded separately in Detection Limit Method. Record 'N/A' where
      the procedure reports no concentrations.
    type: object
    properties:
      '@id':
        const: ada:parameter/semTAPP/detectionLimitDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: detectionLimitDefault
      schema:name:
        const: Detection Limit
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
  sem_driftCorrectionDefault:
    title: Drift Correction
    description: 'Describes whether and how stage or beam drift was monitored and
      corrected during the measurement session. Examples: periodic stage realignment
      to a fiducial marker, automated beam drift correction in acquisition software,
      or reanalysis of a reference point at regular intervals.'
    type: object
    properties:
      '@id':
        const: ada:parameter/semTAPP/driftCorrectionDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: driftCorrectionDefault
      schema:name:
        const: Drift Correction
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
  sem_ebsdFrameTimeDefault:
    title: EBSD Frame Time
    description: Acquisition time per EBSD diffraction pattern frame in milliseconds.
    type: object
    properties:
      '@id':
        const: ada:parameter/semTAPP/ebsdFrameTimeDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: ebsdFrameTimeDefault
      schema:name:
        const: EBSD Frame Time
      ada:dataType:
        const: number
      ada:fieldScope:
        const: session
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:unitText:
        const: ms
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - ada:fieldScope
  sem_ebsdPatternQualityThresholdDefault:
    title: EBSD Pattern Quality Threshold
    description: Minimum pattern quality or confidence index threshold applied during
      EBSD data processing to exclude unreliably indexed points from orientation maps.
      Include metric name and threshold value.
    type: object
    properties:
      '@id':
        const: ada:parameter/semTAPP/ebsdPatternQualityThresholdDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: ebsdPatternQualityThresholdDefault
      schema:name:
        const: EBSD Pattern Quality Threshold
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
  sem_halogenCorrectionOnOxygenDefault:
    title: Halogen Correction on Oxygen
    description: Whether oxygen content was adjusted to account for halogen substitution
      (F and/or Cl replacing OH) in halogen-bearing phases such as apatite, amphibole,
      and mica, where oxygen is calculated by stoichiometry.
    type: object
    properties:
      '@id':
        const: ada:parameter/semTAPP/halogenCorrectionOnOxygenDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: halogenCorrectionOnOxygenDefault
      schema:name:
        const: Halogen Correction on Oxygen
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
  sem_imagePixelSizeDefault:
    title: Image Pixel Size
    description: "Physical size of each image pixel at the sample surface, in nm or
      \xB5m. For large-area mosaic imaging, report the pixel size of individual tiles
      and the number and arrangement of tiles."
    type: object
    properties:
      '@id':
        const: ada:parameter/semTAPP/imagePixelSizeDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: imagePixelSizeDefault
      schema:name:
        const: Image Pixel Size
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
  sem_normalizationStandardsBasedCorrectionDefault:
    title: Normalization / Standards-Based Correction
    description: "Post-acquisition normalization applied to the reported data beyond
      the primary calibration \u2014 for example correction to a reference value derived
      from secondary reference materials, or correction for a systematic bias those
      materials reveal. Record 'None' if no additional normalization is applied."
    type: object
    properties:
      '@id':
        const: ada:parameter/semTAPP/normalizationStandardsBasedCorrectionDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: normalizationStandardsBasedCorrectionDefault
      schema:name:
        const: Normalization / Standards-Based Correction
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
  sem_preAnalysisImagingAndScreeningDefault:
    title: Pre-Analysis Imaging and Screening
    description: Imaging or other characterisation performed before the measurement
      in order to select or locate the sampling unit to be analysed, including the
      technique, instrument and settings used, and how individual analyses are linked
      back to the images. Distinct from any imaging the procedure performs as its
      own measurement. Where the imaging is performed on a separate instrument, it
      should also be recorded in the Group 1 coupling fields.
    type: object
    properties:
      '@id':
        const: ada:parameter/semTAPP/preAnalysisImagingAndScreeningDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: preAnalysisImagingAndScreeningDefault
      schema:name:
        const: Pre-Analysis Imaging and Screening
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
  sem_samplePersistentIdentifierDefault:
    title: Sample Persistent Identifier
    description: Globally unique, persistent identifier for each sample listed in
      Sample Name. IGSN (International Geo Sample Number) is the recommended standard
      for geological and cosmochemical samples, as used by Astromat, EarthChem and
      SESAR. Where a sample and its sub-samples are separately registered, record
      the identifier at the level actually analysed.
    type: object
    properties:
      '@id':
        const: ada:parameter/semTAPP/samplePersistentIdentifierDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: samplePersistentIdentifierDefault
      schema:name:
        const: Sample Persistent Identifier
      ada:dataType:
        const: uri
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
  sem_timeDependentIntensityCorrectionDefault:
    title: Time-Dependent Intensity Correction
    description: Type of time-dependent intensity (TDI) correction applied to compensate
      for beam-induced volatilisation or migration of sensitive elements (e.g., Na,
      K, F in glasses, feldspars, carbonates).
    type: object
    properties:
      '@id':
        const: ada:parameter/semTAPP/timeDependentIntensityCorrectionDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: timeDependentIntensityCorrectionDefault
      schema:name:
        const: Time-Dependent Intensity Correction
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
  solutionMcicpms_betweenSessionAnalyticalPrecisionAndAssessmentMethodDefault:
    title: Between-Session (Long-Term) Analytical Precision and Assessment Method
    description: "Precision of measurements across multiple analytical sessions over
      weeks to months \u2014 long-term or intermediate precision \u2014 and the method
      used to assess it. Report both the assessment method and the precision values,
      specifying the reference material, the number of measurements and sessions,
      the time span covered, and the statistic reported."
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionMcicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethodDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: betweenSessionAnalyticalPrecisionAndAssessmentMethodDefault
      schema:name:
        const: Between-Session (Long-Term) Analytical Precision and Assessment Method
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
  solutionMcicpms_collisionReactionGasMixtureRatioDefault:
    title: Collision/Reaction Gas Mixture Ratio
    description: Where the collision or reaction cell is supplied with a mixture of
      gases rather than a single gas, the identities and proportions of that mixture.
      Recorded separately from the gas identity. Record 'N/A' where a single gas is
      used.
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionMcicpmsTAPP/collisionReactionGasMixtureRatioDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: collisionReactionGasMixtureRatioDefault
      schema:name:
        const: Collision/Reaction Gas Mixture Ratio
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
  solutionMcicpms_countingStatisticsErrorDefault:
    title: Counting Statistics Error
    description: "Uncertainty predicted from counting statistics \u2014 the theoretical
      limit set by the Poisson distribution of the counts accumulated \u2014 for each
      reported quantity per analysis, with the sigma level stated. Derived from the
      counts on the analyte together with those on any background or blank subtracted
      from it. Distinct from the scatter actually observed within a measurement or
      between repeated measurements, which is recorded separately."
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionMcicpmsTAPP/countingStatisticsErrorDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: countingStatisticsErrorDefault
      schema:name:
        const: Counting Statistics Error
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
  solutionMcicpms_detectionLimitDefault:
    title: Detection Limit
    description: Detection limit, one per reported concentration variable (one per
      analyte, these being the same set). State the units and whether the values are
      procedure-typical estimates or session-specific measured values. The calculation
      method is recorded separately in Detection Limit Method. Record 'N/A' where
      the procedure reports no concentrations.
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionMcicpmsTAPP/detectionLimitDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: detectionLimitDefault
      schema:name:
        const: Detection Limit
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
  solutionMcicpms_doubleSpikeMixingRatioDefault:
    title: Double-Spike Mixing Ratio
    description: "Target proportion of double-spike signal relative to total analyte
      signal in the spiked mixture, expressed as spike fraction (0\u20131) or spike:sample
      ratio. The optimum is analyte-system specific and is typically determined using
      the Double Spike Toolbox or equivalent. The achieved mixing ratio may deviate
      from the target within acceptable bounds (typically \xB120% of optimal); the
      double-spike inversion corrects for actual mixing ratios. Record 'N/A' where
      the procedure does not use a double spike."
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionMcicpmsTAPP/doubleSpikeMixingRatioDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: doubleSpikeMixingRatioDefault
      schema:name:
        const: Double-Spike Mixing Ratio
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
  solutionMcicpms_errorCorrelationBetweenReportedQuantitiesDefault:
    title: Error Correlation Between Reported Quantities
    description: The correlation coefficient between pairs of reported quantities
      whose uncertainties are not independent, together with the pair it applies to
      and how it was obtained.
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionMcicpmsTAPP/errorCorrelationBetweenReportedQuantitiesDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: errorCorrelationBetweenReportedQuantitiesDefault
      schema:name:
        const: Error Correlation Between Reported Quantities
      ada:dataType:
        const: number
      ada:fieldScope:
        const: session
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:unitText:
        const: dimensionless
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - ada:fieldScope
  solutionMcicpms_icpTuningDefault:
    title: ICP Tuning
    description: Description of the approach used to optimise ICP plasma conditions
      prior to analysis, including the reference material used for tuning and the
      acceptance criteria (e.g., oxide production threshold, sensitivity targets,
      mass calibration).
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionMcicpmsTAPP/icpTuningDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: icpTuningDefault
      schema:name:
        const: ICP Tuning
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
  solutionMcicpms_instrumentSerialNumberOrLabIdentifierDefault:
    title: Instrument Serial Number or Lab Identifier
    description: Serial number or laboratory-internal identifier for the specific
      instrument unit.
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionMcicpmsTAPP/instrumentSerialNumberOrLabIdentifierDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: instrumentSerialNumberOrLabIdentifierDefault
      schema:name:
        const: Instrument Serial Number or Lab Identifier
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
  solutionMcicpms_internalAnalyticalPrecisionAndAssessmentMethodDefault:
    title: Internal (Within-Measurement) Analytical Precision and Assessment Method
    description: Precision of a single measurement, derived from the scatter of the
      cycles, sweeps or integrations that make it up, together with the method used
      to assess it. State the statistic (2SE, 2SD, 1s RSD), the number of cycles it
      is computed over, and the reported quantity it applies to. Distinct from Counting
      Statistics Error, which records the uncertainty predicted from the counts rather
      than the scatter observed; where a procedure reports both, record the observed
      value here and the predicted value there.
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionMcicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethodDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: internalAnalyticalPrecisionAndAssessmentMethodDefault
      schema:name:
        const: Internal (Within-Measurement) Analytical Precision and Assessment Method
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
  solutionMcicpms_limitOfQuantificationMethodDefault:
    title: Limit of Quantification (LOQ) Method
    description: 'Reference or description of the method used to calculate the limit
      of quantification (LOQ): the lowest concentration reliably measurable with acceptable
      precision and accuracy. Required when concentrations near the LOD are reported.'
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionMcicpmsTAPP/limitOfQuantificationMethodDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: limitOfQuantificationMethodDefault
      schema:name:
        const: Limit of Quantification (LOQ) Method
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
  solutionMcicpms_makeUpGasAndFlowRateDefault:
    title: Make-up Gas and Flow Rate
    description: Supplementary gas added to the sample-carrying stream between the
      sample introduction system and the plasma, with its identity and the procedure-registered
      target flow rate. Record any small nitrogen or hydrogen addition with its own
      flow, whose unit commonly differs from the make-up flow. Record 'None' explicitly
      where no supplementary gas is added, to distinguish it from not reported.
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionMcicpmsTAPP/makeUpGasAndFlowRateDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: makeUpGasAndFlowRateDefault
      schema:name:
        const: Make-up Gas and Flow Rate
      ada:dataType:
        const: number
      ada:fieldScope:
        const: session
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:unitText:
        const: L/min
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - ada:fieldScope
  solutionMcicpms_memoryEffectMitigationDefault:
    title: Memory Effect Mitigation
    description: Procedure applied to identify and minimise carry-over of high-concentration
      or isotopically distinct material from a preceding measurement into the current
      one. Mitigation is applied primarily at measurement time, by allowing sufficient
      washout or rinse between successive introductions. At data processing level,
      record any flagging or exclusion of measurements where the required washout
      may not have been achieved.
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionMcicpmsTAPP/memoryEffectMitigationDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: memoryEffectMitigationDefault
      schema:name:
        const: Memory Effect Mitigation
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
  solutionMcicpms_normalizationStandardsBasedCorrectionDefault:
    title: Normalization / Standards-Based Correction
    description: "Post-acquisition normalization applied to the reported data beyond
      the primary calibration \u2014 for example correction to a reference value derived
      from secondary reference materials, or correction for a systematic bias those
      materials reveal. Record 'None' if no additional normalization is applied."
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionMcicpmsTAPP/normalizationStandardsBasedCorrectionDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: normalizationStandardsBasedCorrectionDefault
      schema:name:
        const: Normalization / Standards-Based Correction
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
  solutionMcicpms_reactionGasFlowRateDefault:
    title: Reaction Gas Flow Rate
    description: Flow rate of the reactive gas introduced into the dynamic reaction
      cell (DRC), in mL/min. Record 'None' if DRC mode is not used, and 'N/A' where
      Collision/Reaction Cell (CRC) Configuration does not include DRC or the instrument
      has no cell.
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionMcicpmsTAPP/reactionGasFlowRateDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: reactionGasFlowRateDefault
      schema:name:
        const: Reaction Gas Flow Rate
      ada:dataType:
        const: number
      ada:fieldScope:
        const: session
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:unitText:
        const: mL/min
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - ada:fieldScope
  solutionMcicpms_sampleAliquotMassOrVolumeDefault:
    title: Sample Aliquot Mass or Volume
    description: Mass (mg) of solid material digested or volume (mL) of liquid taken
      for dissolution.
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionMcicpmsTAPP/sampleAliquotMassOrVolumeDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: sampleAliquotMassOrVolumeDefault
      schema:name:
        const: Sample Aliquot Mass or Volume
      ada:dataType:
        const: number
      ada:fieldScope:
        const: session
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:unitText:
        const: mg or mL
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - ada:fieldScope
  solutionMcicpms_samplePersistentIdentifierDefault:
    title: Sample Persistent Identifier
    description: Globally unique, persistent identifier for each sample listed in
      Sample Name. IGSN (International Geo Sample Number) is the recommended standard
      for geological and cosmochemical samples, as used by Astromat, EarthChem and
      SESAR. Where a sample and its sub-samples are separately registered, record
      the identifier at the level actually analysed.
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionMcicpmsTAPP/samplePersistentIdentifierDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: samplePersistentIdentifierDefault
      schema:name:
        const: Sample Persistent Identifier
      ada:dataType:
        const: uri
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
  solutionMcicpms_spikeOutlierFilteringApproachDefault:
    title: Spike / Outlier Filtering Approach
    description: Criteria used to identify and exclude anomalous data - signal spikes,
      individual cycles, or whole replicate measurements - before the reported value
      is calculated. State where in the reduction sequence the filter is applied.
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionMcicpmsTAPP/spikeOutlierFilteringApproachDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: spikeOutlierFilteringApproachDefault
      schema:name:
        const: Spike / Outlier Filtering Approach
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
  solutionMcicpms_torchDepthDefault:
    title: Torch Depth
    description: Distance between the load coil and the sampling cone tip (mm), also
      called injector depth or torch position depending on the instrument manufacturer.
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionMcicpmsTAPP/torchDepthDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: torchDepthDefault
      schema:name:
        const: Torch Depth
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
  solutionMcicpms_uncertaintyPropagationMethodDefault:
    title: Uncertainty Propagation Method
    description: 'The approach used to propagate analytical uncertainty through the
      data reduction chain to the final reported value. State which sources are included
      in the propagation: counting statistics, calibration standard uncertainty, internal
      standard uncertainty, drift correction, and any systematic contributions. Distinct
      from Uncertainty Level, which states the convention at which the resulting uncertainty
      is quoted.'
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionMcicpmsTAPP/uncertaintyPropagationMethodDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: uncertaintyPropagationMethodDefault
      schema:name:
        const: Uncertainty Propagation Method
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
  solutionQicpms_betweenSessionAnalyticalPrecisionAndAssessmentMethodDefault:
    title: Between-Session (Long-Term) Analytical Precision and Assessment Method
    description: "Precision of measurements across multiple analytical sessions over
      weeks to months \u2014 long-term or intermediate precision \u2014 and the method
      used to assess it. Report both the assessment method and the precision values,
      specifying the reference material, the number of measurements and sessions,
      the time span covered, and the statistic reported."
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionQicpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethodDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: betweenSessionAnalyticalPrecisionAndAssessmentMethodDefault
      schema:name:
        const: Between-Session (Long-Term) Analytical Precision and Assessment Method
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
  solutionQicpms_collisionReactionGasMixtureRatioDefault:
    title: Collision/Reaction Gas Mixture Ratio
    description: Where the collision or reaction cell is supplied with a mixture of
      gases rather than a single gas, the identities and proportions of that mixture.
      Recorded separately from the gas identity. Record 'N/A' where a single gas is
      used.
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionQicpmsTAPP/collisionReactionGasMixtureRatioDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: collisionReactionGasMixtureRatioDefault
      schema:name:
        const: Collision/Reaction Gas Mixture Ratio
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
  solutionQicpms_countingStatisticsErrorDefault:
    title: Counting Statistics Error
    description: "Uncertainty predicted from counting statistics \u2014 the theoretical
      limit set by the Poisson distribution of the counts accumulated \u2014 for each
      reported quantity per analysis, with the sigma level stated. Derived from the
      counts on the analyte together with those on any background or blank subtracted
      from it. Distinct from the scatter actually observed within a measurement or
      between repeated measurements, which is recorded separately."
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionQicpmsTAPP/countingStatisticsErrorDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: countingStatisticsErrorDefault
      schema:name:
        const: Counting Statistics Error
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
  solutionQicpms_detectionLimitDefault:
    title: Detection Limit
    description: Detection limit, one per reported concentration variable (one per
      analyte, these being the same set). State the units and whether the values are
      procedure-typical estimates or session-specific measured values. The calculation
      method is recorded separately in Detection Limit Method. Record 'N/A' where
      the procedure reports no concentrations.
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionQicpmsTAPP/detectionLimitDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: detectionLimitDefault
      schema:name:
        const: Detection Limit
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
  solutionQicpms_doublyChargedSpeciesMonitorDefault:
    title: Doubly-Charged Species Monitor
    description: Mass ratio monitored to estimate doubly-charged ion (M2+) formation
      during instrument tuning.
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionQicpmsTAPP/doublyChargedSpeciesMonitorDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: doublyChargedSpeciesMonitorDefault
      schema:name:
        const: Doubly-Charged Species Monitor
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
  solutionQicpms_doublyChargedSpeciesProductionDefault:
    title: Doubly-Charged Species Production
    description: Measured percentage of doubly-charged ion production for the monitored
      species at the time of instrument tuning. The acceptable threshold is typically
      <1% or <3%. Record both the threshold and the measured value.
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionQicpmsTAPP/doublyChargedSpeciesProductionDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: doublyChargedSpeciesProductionDefault
      schema:name:
        const: Doubly-Charged Species Production
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
  solutionQicpms_icpTuningDefault:
    title: ICP Tuning
    description: Description of the approach used to optimise ICP plasma conditions
      prior to analysis, including the reference material used for tuning and the
      acceptance criteria (e.g., oxide production threshold, sensitivity targets,
      mass calibration).
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionQicpmsTAPP/icpTuningDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: icpTuningDefault
      schema:name:
        const: ICP Tuning
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
  solutionQicpms_instrumentSerialNumberOrLabIdentifierDefault:
    title: Instrument Serial Number or Lab Identifier
    description: Serial number or laboratory-internal identifier for the specific
      instrument unit.
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionQicpmsTAPP/instrumentSerialNumberOrLabIdentifierDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: instrumentSerialNumberOrLabIdentifierDefault
      schema:name:
        const: Instrument Serial Number or Lab Identifier
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
  solutionQicpms_internalAnalyticalPrecisionAndAssessmentMethodDefault:
    title: Internal (Within-Measurement) Analytical Precision and Assessment Method
    description: Precision of a single measurement, derived from the scatter of the
      cycles, sweeps or integrations that make it up, together with the method used
      to assess it. State the statistic (2SE, 2SD, 1s RSD), the number of cycles it
      is computed over, and the reported quantity it applies to. Distinct from Counting
      Statistics Error, which records the uncertainty predicted from the counts rather
      than the scatter observed; where a procedure reports both, record the observed
      value here and the predicted value there.
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionQicpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethodDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: internalAnalyticalPrecisionAndAssessmentMethodDefault
      schema:name:
        const: Internal (Within-Measurement) Analytical Precision and Assessment Method
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
  solutionQicpms_limitOfQuantificationMethodDefault:
    title: Limit of Quantification (LOQ) Method
    description: 'Reference or description of the method used to calculate the limit
      of quantification (LOQ): the lowest concentration reliably measurable with acceptable
      precision and accuracy. Required when concentrations near the LOD are reported.'
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionQicpmsTAPP/limitOfQuantificationMethodDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: limitOfQuantificationMethodDefault
      schema:name:
        const: Limit of Quantification (LOQ) Method
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
  solutionQicpms_makeUpGasAndFlowRateDefault:
    title: Make-up Gas and Flow Rate
    description: Supplementary gas added to the sample-carrying stream between the
      sample introduction system and the plasma, with its identity and the procedure-registered
      target flow rate. Record any small nitrogen or hydrogen addition with its own
      flow, whose unit commonly differs from the make-up flow. Record 'None' explicitly
      where no supplementary gas is added, to distinguish it from not reported.
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionQicpmsTAPP/makeUpGasAndFlowRateDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: makeUpGasAndFlowRateDefault
      schema:name:
        const: Make-up Gas and Flow Rate
      ada:dataType:
        const: number
      ada:fieldScope:
        const: session
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:unitText:
        const: L/min
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - ada:fieldScope
  solutionQicpms_memoryEffectMitigationDefault:
    title: Memory Effect Mitigation
    description: Procedure applied to identify and minimise carry-over of high-concentration
      or isotopically distinct material from a preceding measurement into the current
      one. Mitigation is applied primarily at measurement time, by allowing sufficient
      washout or rinse between successive introductions. At data processing level,
      record any flagging or exclusion of measurements where the required washout
      may not have been achieved.
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionQicpmsTAPP/memoryEffectMitigationDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: memoryEffectMitigationDefault
      schema:name:
        const: Memory Effect Mitigation
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
  solutionQicpms_normalizationStandardsBasedCorrectionDefault:
    title: Normalization / Standards-Based Correction
    description: "Post-acquisition normalization applied to the reported data beyond
      the primary calibration \u2014 for example correction to a reference value derived
      from secondary reference materials, or correction for a systematic bias those
      materials reveal. Record 'None' if no additional normalization is applied."
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionQicpmsTAPP/normalizationStandardsBasedCorrectionDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: normalizationStandardsBasedCorrectionDefault
      schema:name:
        const: Normalization / Standards-Based Correction
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
  solutionQicpms_numberOfReplicatesDefault:
    title: Number of Replicates
    description: Number of replicate measurements performed on the same sample, or
      on the same nominal location where the technique is spatially resolved. For
      spot analysis this is the number of individual spots per grain or location;
      for transects, the number of replicate lines; for mapping, the number of map
      acquisitions of the same area; for solution work, the number of discrete replicate
      measurements acquired per sample solution.
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionQicpmsTAPP/numberOfReplicatesDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: numberOfReplicatesDefault
      schema:name:
        const: Number of Replicates
      ada:dataType:
        const: integer
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
  solutionQicpms_pulseAnalogDetectorNonlinearityCorrectionDefault:
    title: Pulse/Analog Detector Nonlinearity Correction
    description: Whether a correction was applied for nonlinear detector response
      at the transition between pulse-counting and analog (and Faraday, for triple-mode
      instruments) detection modes. Cross-calibration factors between detector modes
      must be confirmed, typically measured each session. Record 'Applied' and describe
      the method, the detector modes involved and the analytes affected; 'None' where
      a crossover exists on this instrument but no correction was made, giving the
      reason; and 'N/A' where the detector is pulse-counting only and no crossover
      exists.
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionQicpmsTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: pulseAnalogDetectorNonlinearityCorrectionDefault
      schema:name:
        const: Pulse/Analog Detector Nonlinearity Correction
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
  solutionQicpms_reactionGasFlowRateDefault:
    title: Reaction Gas Flow Rate
    description: Flow rate of the reactive gas introduced into the dynamic reaction
      cell (DRC), in mL/min. Record 'None' if DRC mode is not used, and 'N/A' where
      Collision/Reaction Cell (CRC) Configuration does not include DRC or the instrument
      has no cell.
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionQicpmsTAPP/reactionGasFlowRateDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: reactionGasFlowRateDefault
      schema:name:
        const: Reaction Gas Flow Rate
      ada:dataType:
        const: number
      ada:fieldScope:
        const: session
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:unitText:
        const: mL/min
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - ada:fieldScope
  solutionQicpms_sampleAliquotMassOrVolumeDefault:
    title: Sample Aliquot Mass or Volume
    description: Mass (mg) of solid material digested or volume (mL) of liquid taken
      for dissolution.
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionQicpmsTAPP/sampleAliquotMassOrVolumeDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: sampleAliquotMassOrVolumeDefault
      schema:name:
        const: Sample Aliquot Mass or Volume
      ada:dataType:
        const: number
      ada:fieldScope:
        const: session
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:unitText:
        const: mg or mL
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - ada:fieldScope
  solutionQicpms_samplePersistentIdentifierDefault:
    title: Sample Persistent Identifier
    description: Globally unique, persistent identifier for each sample listed in
      Sample Name. IGSN (International Geo Sample Number) is the recommended standard
      for geological and cosmochemical samples, as used by Astromat, EarthChem and
      SESAR. Where a sample and its sub-samples are separately registered, record
      the identifier at the level actually analysed.
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionQicpmsTAPP/samplePersistentIdentifierDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: samplePersistentIdentifierDefault
      schema:name:
        const: Sample Persistent Identifier
      ada:dataType:
        const: uri
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
  solutionQicpms_spikeOutlierFilteringApproachDefault:
    title: Spike / Outlier Filtering Approach
    description: Criteria used to identify and exclude anomalous data - signal spikes,
      individual cycles, or whole replicate measurements - before the reported value
      is calculated. State where in the reduction sequence the filter is applied.
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionQicpmsTAPP/spikeOutlierFilteringApproachDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: spikeOutlierFilteringApproachDefault
      schema:name:
        const: Spike / Outlier Filtering Approach
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
  solutionQicpms_torchDepthDefault:
    title: Torch Depth
    description: Distance between the load coil and the sampling cone tip (mm), also
      called injector depth or torch position depending on the instrument manufacturer.
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionQicpmsTAPP/torchDepthDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: torchDepthDefault
      schema:name:
        const: Torch Depth
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
  solutionQicpms_uncertaintyPropagationMethodDefault:
    title: Uncertainty Propagation Method
    description: 'The approach used to propagate analytical uncertainty through the
      data reduction chain to the final reported value. State which sources are included
      in the propagation: counting statistics, calibration standard uncertainty, internal
      standard uncertainty, drift correction, and any systematic contributions. Distinct
      from Uncertainty Level, which states the convention at which the resulting uncertainty
      is quoted.'
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionQicpmsTAPP/uncertaintyPropagationMethodDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: uncertaintyPropagationMethodDefault
      schema:name:
        const: Uncertainty Propagation Method
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
  solutionSficpms_betweenSessionAnalyticalPrecisionAndAssessmentMethodDefault:
    title: Between-Session (Long-Term) Analytical Precision and Assessment Method
    description: "Precision of measurements across multiple analytical sessions over
      weeks to months \u2014 long-term or intermediate precision \u2014 and the method
      used to assess it. Report both the assessment method and the precision values,
      specifying the reference material, the number of measurements and sessions,
      the time span covered, and the statistic reported."
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionSficpmsTAPP/betweenSessionAnalyticalPrecisionAndAssessmentMethodDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: betweenSessionAnalyticalPrecisionAndAssessmentMethodDefault
      schema:name:
        const: Between-Session (Long-Term) Analytical Precision and Assessment Method
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
  solutionSficpms_countingStatisticsErrorDefault:
    title: Counting Statistics Error
    description: "Uncertainty predicted from counting statistics \u2014 the theoretical
      limit set by the Poisson distribution of the counts accumulated \u2014 for each
      reported quantity per analysis, with the sigma level stated. Derived from the
      counts on the analyte together with those on any background or blank subtracted
      from it. Distinct from the scatter actually observed within a measurement or
      between repeated measurements, which is recorded separately."
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionSficpmsTAPP/countingStatisticsErrorDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: countingStatisticsErrorDefault
      schema:name:
        const: Counting Statistics Error
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
  solutionSficpms_detectionLimitDefault:
    title: Detection Limit
    description: Detection limit, one per reported concentration variable (one per
      analyte, these being the same set). State the units and whether the values are
      procedure-typical estimates or session-specific measured values. The calculation
      method is recorded separately in Detection Limit Method. Record 'N/A' where
      the procedure reports no concentrations.
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionSficpmsTAPP/detectionLimitDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: detectionLimitDefault
      schema:name:
        const: Detection Limit
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
  solutionSficpms_doublyChargedSpeciesMonitorDefault:
    title: Doubly-Charged Species Monitor
    description: Mass ratio monitored to estimate doubly-charged ion (M2+) formation
      during instrument tuning.
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionSficpmsTAPP/doublyChargedSpeciesMonitorDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: doublyChargedSpeciesMonitorDefault
      schema:name:
        const: Doubly-Charged Species Monitor
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
  solutionSficpms_doublyChargedSpeciesProductionDefault:
    title: Doubly-Charged Species Production
    description: Measured percentage of doubly-charged ion production for the monitored
      species at the time of instrument tuning. The acceptable threshold is typically
      <1% or <3%. Record both the threshold and the measured value.
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionSficpmsTAPP/doublyChargedSpeciesProductionDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: doublyChargedSpeciesProductionDefault
      schema:name:
        const: Doubly-Charged Species Production
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
  solutionSficpms_icpTuningDefault:
    title: ICP Tuning
    description: Description of the approach used to optimise ICP plasma conditions
      prior to analysis, including the reference material used for tuning and the
      acceptance criteria (e.g., oxide production threshold, sensitivity targets,
      mass calibration).
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionSficpmsTAPP/icpTuningDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: icpTuningDefault
      schema:name:
        const: ICP Tuning
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
  solutionSficpms_instrumentSerialNumberOrLabIdentifierDefault:
    title: Instrument Serial Number or Lab Identifier
    description: Serial number or laboratory-internal identifier for the specific
      instrument unit.
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionSficpmsTAPP/instrumentSerialNumberOrLabIdentifierDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: instrumentSerialNumberOrLabIdentifierDefault
      schema:name:
        const: Instrument Serial Number or Lab Identifier
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
  solutionSficpms_internalAnalyticalPrecisionAndAssessmentMethodDefault:
    title: Internal (Within-Measurement) Analytical Precision and Assessment Method
    description: Precision of a single measurement, derived from the scatter of the
      cycles, sweeps or integrations that make it up, together with the method used
      to assess it. State the statistic (2SE, 2SD, 1s RSD), the number of cycles it
      is computed over, and the reported quantity it applies to. Distinct from Counting
      Statistics Error, which records the uncertainty predicted from the counts rather
      than the scatter observed; where a procedure reports both, record the observed
      value here and the predicted value there.
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionSficpmsTAPP/internalAnalyticalPrecisionAndAssessmentMethodDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: internalAnalyticalPrecisionAndAssessmentMethodDefault
      schema:name:
        const: Internal (Within-Measurement) Analytical Precision and Assessment Method
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
  solutionSficpms_limitOfQuantificationMethodDefault:
    title: Limit of Quantification (LOQ) Method
    description: 'Reference or description of the method used to calculate the limit
      of quantification (LOQ): the lowest concentration reliably measurable with acceptable
      precision and accuracy. Required when concentrations near the LOD are reported.'
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionSficpmsTAPP/limitOfQuantificationMethodDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: limitOfQuantificationMethodDefault
      schema:name:
        const: Limit of Quantification (LOQ) Method
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
  solutionSficpms_makeUpGasAndFlowRateDefault:
    title: Make-up Gas and Flow Rate
    description: Supplementary gas added to the sample-carrying stream between the
      sample introduction system and the plasma, with its identity and the procedure-registered
      target flow rate. Record any small nitrogen or hydrogen addition with its own
      flow, whose unit commonly differs from the make-up flow. Record 'None' explicitly
      where no supplementary gas is added, to distinguish it from not reported.
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionSficpmsTAPP/makeUpGasAndFlowRateDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: makeUpGasAndFlowRateDefault
      schema:name:
        const: Make-up Gas and Flow Rate
      ada:dataType:
        const: number
      ada:fieldScope:
        const: session
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:unitText:
        const: L/min
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - ada:fieldScope
  solutionSficpms_memoryEffectMitigationDefault:
    title: Memory Effect Mitigation
    description: Procedure applied to identify and minimise carry-over of high-concentration
      or isotopically distinct material from a preceding measurement into the current
      one. Mitigation is applied primarily at measurement time, by allowing sufficient
      washout or rinse between successive introductions. At data processing level,
      record any flagging or exclusion of measurements where the required washout
      may not have been achieved.
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionSficpmsTAPP/memoryEffectMitigationDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: memoryEffectMitigationDefault
      schema:name:
        const: Memory Effect Mitigation
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
  solutionSficpms_normalizationStandardsBasedCorrectionDefault:
    title: Normalization / Standards-Based Correction
    description: "Post-acquisition normalization applied to the reported data beyond
      the primary calibration \u2014 for example correction to a reference value derived
      from secondary reference materials, or correction for a systematic bias those
      materials reveal. Record 'None' if no additional normalization is applied."
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionSficpmsTAPP/normalizationStandardsBasedCorrectionDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: normalizationStandardsBasedCorrectionDefault
      schema:name:
        const: Normalization / Standards-Based Correction
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
  solutionSficpms_numberOfReplicatesDefault:
    title: Number of Replicates
    description: Number of replicate measurements performed on the same sample, or
      on the same nominal location where the technique is spatially resolved. For
      spot analysis this is the number of individual spots per grain or location;
      for transects, the number of replicate lines; for mapping, the number of map
      acquisitions of the same area; for solution work, the number of discrete replicate
      measurements acquired per sample solution.
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionSficpmsTAPP/numberOfReplicatesDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: numberOfReplicatesDefault
      schema:name:
        const: Number of Replicates
      ada:dataType:
        const: integer
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
  solutionSficpms_pulseAnalogDetectorNonlinearityCorrectionDefault:
    title: Pulse/Analog Detector Nonlinearity Correction
    description: Whether a correction was applied for nonlinear detector response
      at the transition between pulse-counting and analog (and Faraday, for triple-mode
      instruments) detection modes. Cross-calibration factors between detector modes
      must be confirmed, typically measured each session. Record 'Applied' and describe
      the method, the detector modes involved and the analytes affected; 'None' where
      a crossover exists on this instrument but no correction was made, giving the
      reason; and 'N/A' where the detector is pulse-counting only and no crossover
      exists.
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionSficpmsTAPP/pulseAnalogDetectorNonlinearityCorrectionDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: pulseAnalogDetectorNonlinearityCorrectionDefault
      schema:name:
        const: Pulse/Analog Detector Nonlinearity Correction
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
  solutionSficpms_sampleAliquotMassOrVolumeDefault:
    title: Sample Aliquot Mass or Volume
    description: Mass (mg) of solid material digested or volume (mL) of liquid taken
      for dissolution.
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionSficpmsTAPP/sampleAliquotMassOrVolumeDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: sampleAliquotMassOrVolumeDefault
      schema:name:
        const: Sample Aliquot Mass or Volume
      ada:dataType:
        const: number
      ada:fieldScope:
        const: session
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:unitText:
        const: mg or mL
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - ada:fieldScope
  solutionSficpms_samplePersistentIdentifierDefault:
    title: Sample Persistent Identifier
    description: Globally unique, persistent identifier for each sample listed in
      Sample Name. IGSN (International Geo Sample Number) is the recommended standard
      for geological and cosmochemical samples, as used by Astromat, EarthChem and
      SESAR. Where a sample and its sub-samples are separately registered, record
      the identifier at the level actually analysed.
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionSficpmsTAPP/samplePersistentIdentifierDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: samplePersistentIdentifierDefault
      schema:name:
        const: Sample Persistent Identifier
      ada:dataType:
        const: uri
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
  solutionSficpms_spikeOutlierFilteringApproachDefault:
    title: Spike / Outlier Filtering Approach
    description: Criteria used to identify and exclude anomalous data - signal spikes,
      individual cycles, or whole replicate measurements - before the reported value
      is calculated. State where in the reduction sequence the filter is applied.
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionSficpmsTAPP/spikeOutlierFilteringApproachDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: spikeOutlierFilteringApproachDefault
      schema:name:
        const: Spike / Outlier Filtering Approach
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
  solutionSficpms_torchDepthDefault:
    title: Torch Depth
    description: Distance between the load coil and the sampling cone tip (mm), also
      called injector depth or torch position depending on the instrument manufacturer.
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionSficpmsTAPP/torchDepthDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: torchDepthDefault
      schema:name:
        const: Torch Depth
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
  solutionSficpms_uncertaintyPropagationMethodDefault:
    title: Uncertainty Propagation Method
    description: 'The approach used to propagate analytical uncertainty through the
      data reduction chain to the final reported value. State which sources are included
      in the propagation: counting statistics, calibration standard uncertainty, internal
      standard uncertainty, drift correction, and any systematic contributions. Distinct
      from Uncertainty Level, which states the convention at which the resulting uncertainty
      is quoted.'
    type: object
    properties:
      '@id':
        const: ada:parameter/solutionSficpmsTAPP/uncertaintyPropagationMethodDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: uncertaintyPropagationMethodDefault
      schema:name:
        const: Uncertainty Propagation Method
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
  tem_diffractionCalibrationReferenceDefault:
    title: Diffraction Calibration Reference
    description: "Reference material or internal standard used to calibrate the electron
      diffraction camera constant (camera length \xD7 electron wavelength), enabling
      conversion of pixel distances to d-spacings."
    type: object
    properties:
      '@id':
        const: ada:parameter/temTAPP/diffractionCalibrationReferenceDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: diffractionCalibrationReferenceDefault
      schema:name:
        const: Diffraction Calibration Reference
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
  tem_diffractionCameraLengthCalibrationMethodDefault:
    title: Diffraction Camera Length Calibration Method
    description: Method used to calibrate the camera length constant and convert pixel
      distances in diffraction patterns to d-spacings or reciprocal lattice vectors.
    type: object
    properties:
      '@id':
        const: ada:parameter/temTAPP/diffractionCameraLengthCalibrationMethodDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: diffractionCameraLengthCalibrationMethodDefault
      schema:name:
        const: Diffraction Camera Length Calibration Method
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
  tem_edsCountingStatisticsAccumulationCriterionDefault:
    title: EDS Counting Statistics / Accumulation Criterion
    description: Quality criterion used to determine when sufficient EDS signal has
      been accumulated for a given pixel or point, in lieu of or in addition to a
      fixed live time. Expressed as a target relative uncertainty on major-element
      peak counts achieved by accumulating successive scan frames (e.g., "1% counting
      statistics on major elements"; ">10% counting statistics"). Distinct from EDS
      Live Time per Point or Pixel, which records a fixed-duration setting. Record
      'N/A' where EDS is not listed in Spectroscopic Detector(s).
    type: object
    properties:
      '@id':
        const: ada:parameter/temTAPP/edsCountingStatisticsAccumulationCriterionDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: edsCountingStatisticsAccumulationCriterionDefault
      schema:name:
        const: EDS Counting Statistics / Accumulation Criterion
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
  tem_edsDetectionLimitDefault:
    title: EDS Detection Limit
    description: Estimated detection limits by EDS under this procedure's conditions,
      one per reported concentration variable (one per analyte, these being the same
      set). Record 'N/A' where EDS is not listed in Spectroscopic Detector(s).
    type: object
    properties:
      '@id':
        const: ada:parameter/temTAPP/edsDetectionLimitDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: edsDetectionLimitDefault
      schema:name:
        const: EDS Detection Limit
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
  tem_edsEnergyRangeDefault:
    title: EDS Energy Range
    description: Energy range of EDS spectrum acquisition in keV. Record 'N/A' where
      EDS is not listed in Spectroscopic Detector(s).
    type: object
    properties:
      '@id':
        const: ada:parameter/temTAPP/edsEnergyRangeDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: edsEnergyRangeDefault
      schema:name:
        const: EDS Energy Range
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
  tem_edsLiveTimePerPointOrPixelDefault:
    title: EDS Live Time per Point or Pixel
    description: EDS spectral acquisition live time per analysis point (point/line
      mode) or per pixel (spectrum image) in seconds. Also referred to as "EDS Acquisition
      Time" in EPMA and some SEM-EDS contexts, where the per-pixel distinction is
      less relevant. Record 'N/A' where EDS is not listed in Spectroscopic Detector(s).
    type: object
    properties:
      '@id':
        const: ada:parameter/temTAPP/edsLiveTimePerPointOrPixelDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: edsLiveTimePerPointOrPixelDefault
      schema:name:
        const: EDS Live Time per Point or Pixel
      ada:dataType:
        const: number
      ada:fieldScope:
        const: session
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:unitText:
        const: s
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - ada:fieldScope
  tem_eelsBackgroundSubtractionMethodDefault:
    title: EELS Background Subtraction Method
    description: Method used to subtract the background beneath the ionization edge
      of interest to extract the net edge signal. Record 'N/A' where EELS is not listed
      in Spectroscopic Detector(s).
    type: object
    properties:
      '@id':
        const: ada:parameter/temTAPP/eelsBackgroundSubtractionMethodDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: eelsBackgroundSubtractionMethodDefault
      schema:name:
        const: EELS Background Subtraction Method
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
  tem_eelsChemicalStateDeterminationMethodDefault:
    title: EELS Chemical State Determination Method
    description: Method used to determine the chemical or oxidation state of an element
      from the fine structure of its ionization edge (ELNES), together with the reference
      data or calibration the determination relies on. Name the method family and
      cite the calibration curve or reference spectra used. Record 'N/A' where no
      chemical-state determination is made.
    type: object
    properties:
      '@id':
        const: ada:parameter/temTAPP/eelsChemicalStateDeterminationMethodDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: eelsChemicalStateDeterminationMethodDefault
      schema:name:
        const: EELS Chemical State Determination Method
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
  tem_eelsDetectionLimitDefault:
    title: EELS Detection Limit
    description: Estimated detection limit or minimum detectable concentration for
      target edges under this procedure. Record 'N/A' where EELS is not listed in
      Spectroscopic Detector(s).
    type: object
    properties:
      '@id':
        const: ada:parameter/temTAPP/eelsDetectionLimitDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: eelsDetectionLimitDefault
      schema:name:
        const: EELS Detection Limit
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
  tem_eelsEnergyCalibrationDefault:
    title: EELS Energy Calibration
    description: Method and reference used to calibrate the EELS energy axis. Record
      'N/A' where EELS is not listed in Spectroscopic Detector(s).
    type: object
    properties:
      '@id':
        const: ada:parameter/temTAPP/eelsEnergyCalibrationDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: eelsEnergyCalibrationDefault
      schema:name:
        const: EELS Energy Calibration
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
  tem_eelsPluralScatteringCorrectionDefault:
    title: EELS Plural Scattering Correction
    description: Method applied to correct for multiple inelastic scattering events
      (plural scattering) that broaden edge fine structure. Record 'N/A' where EELS
      is not listed in Spectroscopic Detector(s).
    type: object
    properties:
      '@id':
        const: ada:parameter/temTAPP/eelsPluralScatteringCorrectionDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: eelsPluralScatteringCorrectionDefault
      schema:name:
        const: EELS Plural Scattering Correction
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
  tem_eftemEnergyWindowDefault:
    title: EFTEM Energy Window
    description: 'Energy window(s) used for EFTEM elemental mapping: center energy,
      width, and acquisition method (three-window or jump-ratio). Record ''N/A'' where
      EFTEM is not listed in Analytical Sub-mode.'
    type: object
    properties:
      '@id':
        const: ada:parameter/temTAPP/eftemEnergyWindowDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: eftemEnergyWindowDefault
      schema:name:
        const: EFTEM Energy Window
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
  tem_haadfCollectionAnglesDefault:
    title: HAADF Collection Angles
    description: Inner and outer collection angles of the HAADF detector in milliradians
      (mrad). Inner angle can be derived from camera length and detector geometry.
    type: object
    properties:
      '@id':
        const: ada:parameter/temTAPP/haadfCollectionAnglesDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: haadfCollectionAnglesDefault
      schema:name:
        const: HAADF Collection Angles
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
  tem_imageProcessingMethodsAppliedDefault:
    title: Image Processing Methods Applied
    description: Image processing steps applied to TEM or STEM images during or after
      acquisition. Non-linear processing steps that could affect quantitative interpretation
      should be documented explicitly.
    type: object
    properties:
      '@id':
        const: ada:parameter/temTAPP/imageProcessingMethodsAppliedDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: imageProcessingMethodsAppliedDefault
      schema:name:
        const: Image Processing Methods Applied
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
  tem_preAnalysisImagingAndScreeningDefault:
    title: Pre-Analysis Imaging and Screening
    description: Imaging or other characterisation performed before the measurement
      in order to select or locate the sampling unit to be analysed, including the
      technique, instrument and settings used, and how individual analyses are linked
      back to the images. Distinct from any imaging the procedure performs as its
      own measurement. Where the imaging is performed on a separate instrument, it
      should also be recorded in the Group 1 coupling fields.
    type: object
    properties:
      '@id':
        const: ada:parameter/temTAPP/preAnalysisImagingAndScreeningDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: preAnalysisImagingAndScreeningDefault
      schema:name:
        const: Pre-Analysis Imaging and Screening
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
  tem_precessionAngleDefault:
    title: Precession Angle
    description: Precession semi-angle in degrees for precession electron diffraction
      (PED). Not applicable to SAED, CBED, or standard 4D-STEM. Record 'N/A' where
      Precession ED is not listed in Analytical Sub-mode.
    type: object
    properties:
      '@id':
        const: ada:parameter/temTAPP/precessionAngleDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: precessionAngleDefault
      schema:name:
        const: Precession Angle
      ada:dataType:
        const: number
      ada:fieldScope:
        const: session
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:unitText:
        const: degrees
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - ada:fieldScope
  tem_saedPatternSimulationSoftwareDefault:
    title: SAED Pattern Simulation Software
    description: Software used to simulate electron diffraction patterns for comparison
      with experimental SAED patterns during phase identification (e.g., SingleCrystal,
      CrystalMaker, JEMS, DIFPACK). Complements the Acquisition Software field, which
      covers data collection; simulation software is used at the interpretation and
      data processing step.
    type: object
    properties:
      '@id':
        const: ada:parameter/temTAPP/saedPatternSimulationSoftwareDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: saedPatternSimulationSoftwareDefault
      schema:name:
        const: SAED Pattern Simulation Software
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
  tem_sampleHolderDefault:
    title: Sample Holder
    description: Type of specimen holder used.
    type: object
    properties:
      '@id':
        const: ada:parameter/temTAPP/sampleHolderDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: sampleHolderDefault
      schema:name:
        const: Sample Holder
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
  tem_samplePersistentIdentifierDefault:
    title: Sample Persistent Identifier
    description: Globally unique, persistent identifier for each sample listed in
      Sample Name. IGSN (International Geo Sample Number) is the recommended standard
      for geological and cosmochemical samples, as used by Astromat, EarthChem and
      SESAR. Where a sample and its sub-samples are separately registered, record
      the identifier at the level actually analysed.
    type: object
    properties:
      '@id':
        const: ada:parameter/temTAPP/samplePersistentIdentifierDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: samplePersistentIdentifierDefault
      schema:name:
        const: Sample Persistent Identifier
      ada:dataType:
        const: uri
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
  tem_samplePreparationDetailsDefault:
    title: Sample Preparation Details
    description: "Detailed description of section preparation conditions: FIB milling
      voltages and currents; final thinning conditions and target foil thickness;
      protective coating type and deposition method (e.g., e-beam vs. ion-beam Pt
      or C strip \u2014 e-beam deposition causes less surface damage); any post-FIB
      surface cleanup (e.g., low-energy Ar+ ion polishing in a Fischione NanoMill,
      final 0.5\u20132 kV Ga+ thinning); sample transfer and storage environment (ambient
      air, dry N\u2082 atmosphere, vacuum transfer holder, glovebox); plasma cleaning
      before loading. Includes session-specific observations and deviations from the
      procedure standard. Includes preparation artifacts noted (Ga implantation, amorphization,
      curtaining)."
    type: object
    properties:
      '@id':
        const: ada:parameter/temTAPP/samplePreparationDetailsDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: samplePreparationDetailsDefault
      schema:name:
        const: Sample Preparation Details
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
  tem_selectedAreaApertureSizeDefault:
    title: Selected-Area Aperture Size
    description: Diameter of the selected-area aperture used in SAED mode, defining
      the specimen region that contributes to the diffraction pattern.
    type: object
    properties:
      '@id':
        const: ada:parameter/temTAPP/selectedAreaApertureSizeDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: selectedAreaApertureSizeDefault
      schema:name:
        const: Selected-Area Aperture Size
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
  tem_specimenThicknessDeterminationMethodDefault:
    title: Specimen Thickness Determination Method
    description: Method used to estimate TEM foil thickness.
    type: object
    properties:
      '@id':
        const: ada:parameter/temTAPP/specimenThicknessDeterminationMethodDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: specimenThicknessDeterminationMethodDefault
      schema:name:
        const: Specimen Thickness Determination Method
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
  tem_stemDwellTimePerProbePosition4DDefault:
    title: 4D-STEM Dwell Time per Probe Position
    description: Time spent acquiring each diffraction pattern in the 4D-STEM dataset
      in milliseconds. Record 'N/A' where 4D-STEM is not listed in Analytical Sub-mode.
    type: object
    properties:
      '@id':
        const: ada:parameter/temTAPP/stemDwellTimePerProbePosition4DDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: stemDwellTimePerProbePosition4DDefault
      schema:name:
        const: 4D-STEM Dwell Time per Probe Position
      ada:dataType:
        const: number
      ada:fieldScope:
        const: session
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:unitText:
        const: ms
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - ada:fieldScope
  tem_stemFrameAveragingDefault:
    title: STEM Frame Averaging
    description: Number of frames averaged (with drift correction if applicable) to
      produce the final STEM image. Also governs STEM-EDS and STEM-EELS acquisition
      where those detectors are used.
    type: object
    properties:
      '@id':
        const: ada:parameter/temTAPP/stemFrameAveragingDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: stemFrameAveragingDefault
      schema:name:
        const: STEM Frame Averaging
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
  tem_stemProbeCurrentDefault:
    title: STEM Probe Current
    description: Probe current in picoamperes (pA) or nanoamperes (nA). Also governs
      STEM-EDS and STEM-EELS acquisition where those detectors are used.
    type: object
    properties:
      '@id':
        const: ada:parameter/temTAPP/stemProbeCurrentDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: stemProbeCurrentDefault
      schema:name:
        const: STEM Probe Current
      ada:dataType:
        const: number
      ada:fieldScope:
        const: session
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:unitText:
        const: pA or nA
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - ada:fieldScope
  tem_stemProbeDiameterDefault:
    title: STEM Probe Diameter
    description: 'Nominal or measured diameter of the focused electron probe at the
      sample, reported in nm. Related to, but distinct from, Convergence Semi-Angle:
      the two quantities are connected via aberration coefficients, defocus, and probe
      current, which are not always published. Report whichever is known; if both
      are known, report both fields. Also governs STEM-EDS and STEM-EELS acquisition
      where those detectors are used.'
    type: object
    properties:
      '@id':
        const: ada:parameter/temTAPP/stemProbeDiameterDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: stemProbeDiameterDefault
      schema:name:
        const: STEM Probe Diameter
      ada:dataType:
        const: number
      ada:fieldScope:
        const: session
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:unitText:
        const: nm
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - ada:fieldScope
  tem_stemScanDimensionsDefault:
    title: STEM Scan Dimensions
    description: "Number of pixels in the STEM scan frame (X \xD7 Y pixels). Also
      governs STEM-EDS and STEM-EELS acquisition where those detectors are used."
    type: object
    properties:
      '@id':
        const: ada:parameter/temTAPP/stemScanDimensionsDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: stemScanDimensionsDefault
      schema:name:
        const: STEM Scan Dimensions
      ada:dataType:
        const: number
      ada:fieldScope:
        const: session
      schema:readonlyValue:
        const: false
      ada:tier:
        const: R
      schema:unitText:
        const: pixels x pixels
    required:
    - '@id'
    - '@type'
    - schema:valueName
    - schema:name
    - ada:dataType
    - ada:fieldScope
  tem_stemScanGridAndArea4DDefault:
    title: 4D-STEM Scan Grid and Area
    description: "Number of probe positions in the 4D-STEM dataset (scan pixels \xD7
      scan pixels) and the physical area covered. Probe step size is the physical
      area divided by scan pixel count. Record 'N/A' where 4D-STEM is not listed in
      Analytical Sub-mode."
    type: object
    properties:
      '@id':
        const: ada:parameter/temTAPP/stemScanGridAndArea4DDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: stemScanGridAndArea4DDefault
      schema:name:
        const: 4D-STEM Scan Grid and Area
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
  tem_temObjectiveApertureDefault:
    title: TEM Objective Aperture
    description: Objective aperture diameter used to select the imaging beam condition
      in TEM mode.
    type: object
    properties:
      '@id':
        const: ada:parameter/temTAPP/temObjectiveApertureDefault
      '@type':
        const:
        - schema:PropertyValueSpecification
      schema:valueName:
        const: temObjectiveApertureDefault
      schema:name:
        const: TEM Objective Aperture
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

```

Links to the schema:

* YAML version: [schema.yaml](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/registry/parameterTemplates/schema.json)
* JSON version: [schema.json](https://amds-ldeo.github.io/geochemBuildingBlocks/build/annotated/registry/parameterTemplates/schema.yaml)

## Sources

* [ADA Metadata Schema v3](https://github.com/amds-ldeo/metadata)

# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/amds-ldeo/geochemBuildingBlocks](https://github.com/amds-ldeo/geochemBuildingBlocks)
* Path: `_sources/registry/parameterTemplates`

