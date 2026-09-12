# ADA Geochemistry Building Blocks repository

Building blocks for Astromat Data Archive (ADA) geochemistry metadata profiles,
using the OGC Building Blocks pattern.


Modular schema components for ADA analytical technique metadata. Imports shared
schema.org and CDIF property building blocks from the CDIF Building Blocks repository.


## Building Blocks

### `ogch.BaseSchema.stringArray` — String Array Type

**Type:** schema

Simple reusable array of strings used throughout ADA metadata. Defines type: array of strings.

### `ogch.BaseSchema.creativeWork` — Creative Work Type

**Type:** schema

Shell type for labeled links to creative works (schema:CreativeWork). Defines properties: @type, schema:name, schema:description, schema:url.

### `ogch.BaseSchema.document` — Document Type

**Type:** schema

Supplemental documents for calibration, methods, and analysis info. Defines properties: @type, componentType, schema:version, schema:isBasedOn. Uses building blocks: detailARGT (geochemProperties).

### `ogch.BaseSchema.otherFile` — Other File Type

**Type:** schema

Non-standard file formats approved for ADA submission. Defines properties: @type, componentType, schema:encodingFormat, formatDescription. Uses building blocks: detailSLS (geochemProperties).

### `ogch.BaseSchema.image` — Image Type

**Type:** schema

ADA image with componentType classification for analytical images. Defines properties: @type, acquisitionTime, componentType, channel1, channel2, channel3, pixelSize, illuminationType, imageType.

### `ogch.BaseSchema.supDocImage` — Supplemental Document Image Type

**Type:** schema

Supplemental document images including analysis locations and context photos. Defines properties: @type, componentType, numPixelsX, numPixelsY, schema:isBasedOn.

### `ogch.BaseSchema.spatialRegistration` — Spatial Registration Type

**Type:** schema

Pixel coordinate system registration for images and maps. Defines properties: basemap, originX, originY, originZ, coordDef, coordUnits, pixelUnits, pixelScaleX, pixelScaleY, originLocation.

### `ogch.BaseSchema.modules.aggregation` — TAPP Composition Module: Aggregation

**Type:** schema

The shared Aggregation block of the 2026-08-11 TAPP library, composed by 13 of the sixteen delivery tables. 2 owned fields over 2 schema paths, split into the procedure and analysis halves a TAPP schema and a technique detail compose respectively. A profile over existing tappDefinition/adaProduct properties, not a new vocabulary. Generated from the module CSV and its schema-path sidecar.

### `ogch.BaseSchema.modules.blank` — TAPP Composition Module: Blank

**Type:** schema

The shared Blank block of the 2026-08-11 TAPP library, composed by 12 of the sixteen delivery tables. 1 owned fields over 0 schema paths, split into the procedure and analysis halves a TAPP schema and a technique detail compose respectively. A profile over existing tappDefinition/adaProduct properties, not a new vocabulary. Generated from the module CSV and its schema-path sidecar.

### `ogch.BaseSchema.modules.calibrationFactor` — TAPP Composition Module: CalibrationFactor

**Type:** schema

The shared CalibrationFactor block of the 2026-08-11 TAPP library, composed by 14 of the sixteen delivery tables. 1 owned fields over 2 schema paths, split into the procedure and analysis halves a TAPP schema and a technique detail compose respectively. A profile over existing tappDefinition/adaProduct properties, not a new vocabulary. Generated from the module CSV and its schema-path sidecar.

### `ogch.BaseSchema.modules.collisionCell` — TAPP Composition Module: CollisionCell

**Type:** schema

The shared CollisionCell block of the 2026-08-11 TAPP library, composed by 6 of the sixteen delivery tables. 8 owned fields over 1 schema paths, split into the procedure and analysis halves a TAPP schema and a technique detail compose respectively. A profile over existing tappDefinition/adaProduct properties, not a new vocabulary. Generated from the module CSV and its schema-path sidecar.

### `ogch.BaseSchema.modules.geochronology` — TAPP Composition Module: Geochronology

**Type:** schema

The shared Geochronology block of the 2026-08-11 TAPP library, composed by 3 of the sixteen delivery tables. 6 owned fields over 16 schema paths, split into the procedure and analysis halves a TAPP schema and a technique detail compose respectively. A profile over existing tappDefinition/adaProduct properties, not a new vocabulary. Generated from the module CSV and its schema-path sidecar.

### `ogch.BaseSchema.modules.mcIcpms` — TAPP Composition Module: MCICPMS

**Type:** schema

The shared MCICPMS block of the 2026-08-11 TAPP library, composed by 3 of the sixteen delivery tables. 15 owned fields over 3 schema paths, split into the procedure and analysis halves a TAPP schema and a technique detail compose respectively. A profile over existing tappDefinition/adaProduct properties, not a new vocabulary. Generated from the module CSV and its schema-path sidecar.

### `ogch.BaseSchema.modules.reportingCore` — TAPP Composition Module: ReportingCore

**Type:** schema

The shared ReportingCore block of the 2026-08-11 TAPP library, composed by 16 of the sixteen delivery tables. 6 owned fields over 3 schema paths, split into the procedure and analysis halves a TAPP schema and a technique detail compose respectively. A profile over existing tappDefinition/adaProduct properties, not a new vocabulary. Generated from the module CSV and its schema-path sidecar.

### `ogch.BaseSchema.modules.samplingUnitSelection` — TAPP Composition Module: SamplingUnitSelection

**Type:** schema

The shared SamplingUnitSelection block of the 2026-08-11 TAPP library, composed by 13 of the sixteen delivery tables. 2 owned fields over 1 schema paths, split into the procedure and analysis halves a TAPP schema and a technique detail compose respectively. A profile over existing tappDefinition/adaProduct properties, not a new vocabulary. Generated from the module CSV and its schema-path sidecar.

### `ogch.BaseSchema.modules.solutionIntroduction` — TAPP Composition Module: SolutionIntroduction

**Type:** schema

The shared SolutionIntroduction block of the 2026-08-11 TAPP library, composed by 3 of the sixteen delivery tables. 16 owned fields over 5 schema paths, split into the procedure and analysis halves a TAPP schema and a technique detail compose respectively. A profile over existing tappDefinition/adaProduct properties, not a new vocabulary. Generated from the module CSV and its schema-path sidecar.

### `ogch.BaseSchema.modules.uPb` — TAPP Composition Module: UPb

**Type:** schema

The shared UPb block of the 2026-08-11 TAPP library, composed by 3 of the sixteen delivery tables. 3 owned fields over 1 schema paths, split into the procedure and analysis halves a TAPP schema and a technique detail compose respectively. A profile over existing tappDefinition/adaProduct properties, not a new vocabulary. Generated from the module CSV and its schema-path sidecar.

### `ogch.registry.analyteColumns` — Analyte-Column Specification Registry

**Type:** schema

Registry of reusable schema:PropertyValueSpecification analyte-column definitions derived from technique TAPP spreadsheets. Hosts one $def per analyte-table reporting column. TAPP building blocks reference these definitions via fragment $refs so they resolve locally through the register.

### `ogch.registry.channelColumns` — Channel-Column Specification Registry

**Type:** schema

Registry of reusable schema:PropertyValueSpecification channel column definitions derived from technique TAPP workbooks. Each $def constrains one column of the channel table, a channel being an instrument selection position -- a mass, a Faraday cup, an energy-loss edge, an X-ray line -- as distinct from the analyte measured on it. TAPP building blocks reference these definitions via fragment $refs so they resolve locally through the building-block register. The root only hosts $defs; it has no instantiable properties of its own. TAPP building blocks reference these definitions via fragment $refs so they resolve locally through the register.

### `ogch.registry.parameterTemplates` — Method-Parameter Template Registry

**Type:** schema

Registry of reusable schema:PropertyValueSpecification method-parameter template definitions derived from technique TAPP spreadsheets. Hosts one $def per method-level parameter template. TAPP building blocks reference these definitions via fragment $refs so they resolve locally through the register.

### `ogch.registry.parameterValues` — Analytical Parameter Value Registry

**Type:** schema

Registry of reusable schema:PropertyValue parameter-value definitions derived from technique TAPP spreadsheets. Hosts one $def per per-dataset parameter value (e.g. acceleratingVoltage, beamDiameter, BeamRasterDimension, reportedAnalyte). Detail building blocks reference these definitions via fragment $refs so they resolve locally through the register.

### `ogch.registry.reportedPropertyColumns` — Reported-Property-Column Specification Registry

**Type:** schema

Registry of reusable schema:PropertyValueSpecification reported-property column definitions derived from technique TAPP workbooks. Each $def constrains one column of the reported-property table -- the variables a procedure REPORTS, as distinct from the analytes and channels it acquires. TAPP building blocks reference these definitions via fragment $refs so they resolve locally through the building-block register. The root only hosts $defs; it has no instantiable properties of its own. TAPP building blocks reference these definitions via fragment $refs so they resolve locally through the register.

### `ogch.techniqueProfile.adaProfile.ARGT.detail` — ARGT Instrument Detail

**Type:** schema

ARGT (Argon) document type with phase and isotope analysis. Defines properties: @type, phaseAnalyzed, isotopeType.

### `ogch.techniqueProfile.adaProfile.Basemap.detail` — Basemap Instrument Detail

**Type:** schema

Basemap images with RGB channels and pixel scaling. Defines properties: @type, schema:description, pixelUnits, pixelScaleX, pixelScaleY, channel1, channel2, channel3.

### `ogch.techniqueProfile.adaProfile.DSC.detail` — DSC Instrument Detail

**Type:** schema

Differential Scanning Calorimetry heat tabular data. Defines properties: @type, analysisType.

### `ogch.techniqueProfile.adaProfile.EAIRMS.detail` — EA-IRMS Instrument Detail

**Type:** schema

Elemental Analysis Isotope Ratio Mass Spectrometry collection. Defines properties: @type, massConsumed, elementType.

### `ogch.techniqueProfile.adaProfile.ICPOES.detail` — ICP-OES Instrument Detail

**Type:** schema

Inductively Coupled Plasma Optical Emission Spectrometry detail properties. Defines properties: @type, mass, dissolutionFactor.

### `ogch.techniqueProfile.adaProfile.L2MS.detail` — L2MS Instrument Detail

**Type:** schema

Laser-2 Mass Spectrometry cube data with ionization parameters. Defines properties: @type, sampleName, ionizationTimeDelay, massGate, photoionizationWavelength, plasmaShutter, timeDelayUnits, wavelengthUnits.

### `ogch.techniqueProfile.adaProfile.LAF.detail` — LAF Instrument Detail

**Type:** schema

Laser Ablation Fluorescence processed/raw data detail properties. Defines properties: @type, elementAnalyzed, sampleMassConsumed, sampleType.

### `ogch.techniqueProfile.adaProfile.QRIS.detail` — QRIS Instrument Detail

**Type:** schema

QRIS (Raman) with calibration and illumination parameters. Defines properties: @type, calibrationFile, pipelineVersion, focalLength, illuminationColor, illuminationLevel, exposureTime, target.

### `ogch.techniqueProfile.adaProfile.SLS.detail` — SLS Instrument Detail

**Type:** schema

Structured Light Scanning shape models and partial scans. Defines properties: @type, countScans, facets, unitsOfMeasurement, version, vertices, watertight.

### `ogch.techniqueProfile.adaProfile.VNMIR.detail` — VNMIR Instrument Detail

**Type:** schema

Very-Near Mid-IR spectroscopy with detailed measurement parameters. Defines properties: @type, detector, beamsplitter, calibrationStandards, comments, numberOfScans, eMaxFitRegionMax, eMaxFitRegionMin, emissionAngle, emissivityMaximum, environmentalPressure, incidenceAngle, measurement, measurementEnvironment, phaseAngle, sampleHeated, samplePreparation, sampleTemperature, spectralRangeMax, spectralRangeMin, spectralResolution, spectralSampling, spotSize, uncertaintyNoise, vacuumExposedSample.

### `ogch.techniqueProfile.adaProfile.XRD.detail` — XRD Instrument Detail

**Type:** schema

X-ray Diffraction tabular data with geometry and wavelength. Defines properties: @type, geometry, sampleMount, stepSize, timePerStep, wavelength.

### `ogch.techniqueProfile.geochemProfile.XCT.detail-legacy` — XCT Instrument Detail

**Type:** schema

X-ray Computed Tomography images with detailed scan parameters. Defines properties: @type, beamFilterMaterial, beamFilterThickness, dataRangeLower, dataRangeUpper, detectorGain, detectorBinning, detectorSize, detectorType, imageExposure, imageFPS, imageGain, imageSize, instrumentType, nsiBeamHardening, numberOfFramesAveragedPerProjection, numberOfProjections, numberOfSlices, pixelPitch, reconstructedDataFormat, reconstructedVoxelSize, reconstructionSoftware, rotationAngle, rotationType, sourceToDetectorDistance, sourceToObjectDistance, subPixGrid, subPixShift, xraySource, xrayTargetMaterial, xrayTubeCurrent, xrayTubeEnergy, xrayTubePower.

### `ogch.BaseSchema.collection` — Collection Type

**Type:** schema

Set of related files with identical information models or composite datasets. Defines properties: @type, componentType, memberTypes, nFiles, filelist. Uses building blocks: stringArray (geochemProperties).

### `ogch.techniqueProfile.adaProfile.NanoIR.detail` — NanoIR Instrument Detail

**Type:** schema

Nano-IR spectroscopy collections with phase analysis. Defines properties: @type, phaseAnalyzed. Uses building blocks: stringArray (geochemProperties).

### `ogch.techniqueProfile.adaProfile.NanoSIMS.detail` — NanoSIMS Instrument Detail

**Type:** schema

Nano Secondary Ion Mass Spectrometry with isotope tracking. Defines properties: @type, phaseAnalyzed, isotopeAnalyzed. Uses building blocks: stringArray (geochemProperties).

### `ogch.techniqueProfile.adaProfile.PSFD.detail` — PSFD Instrument Detail

**Type:** schema

Point Spread Function Data with image names and conditions. Defines properties: @type, imageName, imageViewingConditions. Uses building blocks: stringArray (geochemProperties).

### `ogch.BaseSchema.imageMap` — Image Map Type

**Type:** schema

Spatially registered image map with pixel coordinates and component types. Defines properties: @type, acquisitionTime, componentType, channel1, channel2, channel3, illuminationType, imageType, numPixelsX, numPixelsY, spatialRegistration. Uses building blocks: detailEMPA (geochemProperties), spatialRegistration (geochemProperties).

### `ogch.BaseSchema.laboratory` — ADA Analysis Laboratory

**Type:** schema

ADA laboratory/facility building block extending core CDIF spatialExtent (schema:Place). Adds nxs:BaseClass/NXsource classification via additionalType. Inherits place name, identifier, alternateName, geo coordinates from core.

### `ogch.BaseSchema.dataCube` — Data Cube Type

**Type:** schema

CDI DimensionalDataStructure for multidimensional data. Defines properties: @type, componentType, dataComponentResource. Uses building blocks: detailL2MS (geochemProperties), cdifDataCube (cdifProperties).

### `ogch.BaseSchema.tabularData` — Tabular Data Type

**Type:** schema

CDI PhysicalDataSet for tabular/structured data files. Defines properties: @type, componentType, xCoordCol, yCoordCol, zCoordCol, coordUnits, spatialRegistration. Uses building blocks: detailDSC (geochemProperties), detailEAIRMS (geochemProperties), detailEMPA (geochemProperties), detailLAF (geochemProperties), detailNanoSIMS (geochemProperties), detailNanoIR (geochemProperties), detailPSFD (geochemProperties), detailVNMIR (geochemProperties), detailXRD (geochemProperties), spatialRegistration (geochemProperties), cdifTabularData (cdifProperties).

### `ogch.BaseSchema.instrument` — ADA Analysis Instrument

**Type:** schema

ADA analytical instrument extending the core CDIF instrument building block. Typed as schema:Thing + schema:Product with domain-specific classifications (e.g. nxs:BaseClass/NXinstrument) in schema:additionalType. Inherits hierarchical sub-components, manufacturer, model, calibration properties from core.

### `ogch.BaseSchema.structuredData` — Structured Data File Type

**Type:** schema

A container/array data file (HDF5, NeXus) in an ADA bundle whose layout is described by a CDIF DataStructure via cdi:isStructuredBy. The bundle-part analog of the monolithic single-file isStructuredBy pattern (pattern chosen by encoding, not position). Defines properties: @type, ada:componentType, cdi:isStructuredBy. Uses building blocks: cdifDataStructure (cdifProperties).

### `ogch.BaseSchema.modules.icpms` — TAPP Composition Module: ICPMS

**Type:** schema

The shared ICPMS block of the 2026-08-11 TAPP library, composed by 9 of the sixteen delivery tables. 39 owned fields over 17 schema paths, split into the procedure and analysis halves a TAPP schema and a technique detail compose respectively. A profile over existing tappDefinition/adaProduct properties, not a new vocabulary. Generated from the module CSV and its schema-path sidecar.

### `ogch.BaseSchema.modules.laserAblation` — TAPP Composition Module: LaserAblation

**Type:** schema

The shared LaserAblation block of the 2026-08-11 TAPP library, composed by 6 of the sixteen delivery tables. 29 owned fields over 22 schema paths, split into the procedure and analysis halves a TAPP schema and a technique detail compose respectively. A profile over existing tappDefinition/adaProduct properties, not a new vocabulary. Generated from the module CSV and its schema-path sidecar.

### `ogch.BaseSchema.tappDefinition` — Technique-Aligned Protocol Profile (TAPP) Definition

**Type:** schema

A registered Technique-Aligned Protocol Profile (TAPP) definition modeled as cdi:Activity + schema:Action + ada:TAPPDefinition + bios:LabProtocol. TAPP identity (name, technique, instrument, location, target material) at top level. Standard workflow encoded in schema:actionProcess as a schema:HowTo with ordered cdi:Activity + schema:Action steps. Each workflow step carries its own parameters, reagents, instruments. Uses bios:computationalTool for software, bios:reagent for reference materials, dqv:hasQualityMeasurement for quality metrics, ada:fieldScope (method/session/element) for parameter lifecycle.

### `ogch.BaseSchema.files` — Files Type

**Type:** schema

DataDownload with checksum, size, encoding format, and file detail. Defines properties: schema:additionalType, schema:description, schema:size, resultTarget, schema:relatedLink. Uses building blocks: dataDownload (schemaorgProperties), stringArray (geochemProperties), image (geochemProperties), imageMap (geochemProperties), tabularData (geochemProperties), collection (geochemProperties), dataCube (geochemProperties), document (geochemProperties), supDocImage (geochemProperties), otherFile (geochemProperties).

### `ogch.BaseSchema.geochemProduct` — Geochem Analytical Product

**Type:** schema

Generic geochemistry analytical product metadata base: composes the CDIF core, data-description, manifest, and provenance profiles with the analytical surface (analysis events, variables measured, distributions, coverage). Extended by archive-specific delivery profiles such as adaProduct.

### `ogch.BaseSchema.modules.analyte` — TAPP Composition Module: Analyte

**Type:** schema

The shared Analyte block of the 2026-08-11 TAPP library, composed by 13 of the sixteen delivery tables. 1 owned fields over 1 schema paths, split into the procedure and analysis halves a TAPP schema and a technique detail compose respectively. A profile over existing tappDefinition/adaProduct properties, not a new vocabulary. Generated from the module CSV and its schema-path sidecar.

### `ogch.BaseSchema.adaProduct` — ADA Product Profile

**Type:** schema

Top-level ADA product metadata profile composing all ADA building blocks

### `ogch.BaseSchema.modules.compositionQC` — TAPP Composition Module: CompositionQC

**Type:** schema

The shared CompositionQC block of the 2026-08-11 TAPP library, composed by 12 of the sixteen delivery tables. 6 owned fields over 10 schema paths, split into the procedure and analysis halves a TAPP schema and a technique detail compose respectively. A profile over existing tappDefinition/adaProduct properties, not a new vocabulary. Generated from the module CSV and its schema-path sidecar.

### `ogch.BaseSchema.modules.core` — TAPP Composition Module: Core

**Type:** schema

The shared Core block of the 2026-08-11 TAPP library, composed by 16 of the sixteen delivery tables. 31 owned fields over 35 schema paths, split into the procedure and analysis halves a TAPP schema and a technique detail compose respectively. A profile over existing tappDefinition/adaProduct properties, not a new vocabulary. Generated from the module CSV and its schema-path sidecar.

### `ogch.techniqueProfile.adaProfile.AIVA.profile-ada` — ADA AIVA Profile

**Type:** schema

Technique-specific profile for AI-driven Visual Analysis (AIVA) products

### `ogch.techniqueProfile.adaProfile.AMS.profile-ada` — ADA AMS Profile

**Type:** schema

Technique-specific profile for Accelerator Mass Spectrometry (AMS) products

### `ogch.techniqueProfile.adaProfile.ARGT.profile-ada` — ADA ARGT Profile

**Type:** schema

Technique-specific profile for Argon Geochronology and Thermochronology (ARGT) products

### `ogch.techniqueProfile.adaProfile.DSC.profile-ada` — ADA DSC Profile

**Type:** schema

Technique-specific profile for Differential Scanning Calorimetry (DSC) products

### `ogch.techniqueProfile.adaProfile.EAIRMS.profile-ada` — ADA EA-IRMS Profile

**Type:** schema

Technique-specific profile for Elemental Analysis - Isotope Ratio Mass Spectrometry (EA-IRMS) products

### `ogch.techniqueProfile.adaProfile.FTICRMS.profile-ada` — ADA FTICR-MS Profile

**Type:** schema

Technique-specific profile for Fourier Transform Ion Cyclotron Resonance Mass Spectrometry (FTICR-MS) products

### `ogch.techniqueProfile.adaProfile.GCMS.profile-ada` — ADA GC-MS Profile

**Type:** schema

Technique-specific profile for Gas Chromatography Mass Spectrometry (GC-MS) products

### `ogch.techniqueProfile.adaProfile.GPYC.profile-ada` — ADA GPYC Profile

**Type:** schema

Technique-specific profile for Gas Pycnometry (GPYC) products

### `ogch.techniqueProfile.adaProfile.IC.profile-ada` — ADA IC Profile

**Type:** schema

Technique-specific profile for Ion Chromatography (IC) products

### `ogch.techniqueProfile.adaProfile.ICPMS.profile-ada` — ADA ICP-MS Profile

**Type:** schema

Technique-specific profile for Inductively Coupled Plasma Mass Spectrometry (ICP-MS) products

### `ogch.techniqueProfile.adaProfile.ICPOES.profile-ada` — ADA ICP-OES Profile

**Type:** schema

Technique-specific profile for Inductively Coupled Plasma Optical Emission Spectrometry (ICP-OES) products

### `ogch.techniqueProfile.adaProfile.L2MS.profile-ada` — ADA L2MS Profile

**Type:** schema

Technique-specific profile for Two-Step Laser Mass Spectrometry (L2MS) products

### `ogch.techniqueProfile.adaProfile.LAF.profile-ada` — ADA LAF Profile

**Type:** schema

Technique-specific profile for Laser-Assisted Fluorination (LAF) products

### `ogch.techniqueProfile.adaProfile.LCMS.profile-ada` — ADA LC-MS Profile

**Type:** schema

Technique-specific profile for Liquid Chromatography Mass Spectrometry (LC-MS) products

### `ogch.techniqueProfile.adaProfile.LIT.profile-ada` — ADA LIT Profile

**Type:** schema

Technique-specific profile for Lock-In Thermography (LIT) products

### `ogch.techniqueProfile.adaProfile.NGNSMS.profile-ada` — ADA NG-NS-MS Profile

**Type:** schema

Technique-specific profile for Noble Gas and Nitrogen Static Mass Spectrometry (NG-NS-MS) products

### `ogch.techniqueProfile.adaProfile.NanoIR.profile-ada` — ADA NanoIR Profile

**Type:** schema

Technique-specific profile for Nano-Infrared Spectroscopy (NanoIR) products

### `ogch.techniqueProfile.adaProfile.NanoSIMS.profile-ada` — ADA NanoSIMS Profile

**Type:** schema

Technique-specific profile for Nanoscale Secondary Ion Mass Spectrometry (NanoSIMS) products

### `ogch.techniqueProfile.adaProfile.PSFD.profile-ada` — ADA PSFD Profile

**Type:** schema

Technique-specific profile for Particle Size-Frequency Distribution (PSFD) products

### `ogch.techniqueProfile.adaProfile.QRIS.profile-ada` — ADA QRIS Profile

**Type:** schema

Technique-specific profile for Quantitative Reflectance Imaging Spectroscopy (QRIS) products

### `ogch.techniqueProfile.adaProfile.RAMAN.profile-ada` — ADA RAMAN Profile

**Type:** schema

Technique-specific profile for Raman Spectroscopy (RAMAN) products

### `ogch.techniqueProfile.adaProfile.RITOFNGMS.profile-ada` — ADA RI-TOF-NGMS Profile

**Type:** schema

Technique-specific profile for Resonance Ionization Time-of-Flight Noble Gas Mass Spectrometry (RI-TOF-NGMS) products

### `ogch.techniqueProfile.adaProfile.SIMS.profile-ada` — ADA SIMS Profile

**Type:** schema

Technique-specific profile for Secondary Ion Mass Spectrometry (SIMS) products

### `ogch.techniqueProfile.adaProfile.SLS.profile-ada` — ADA SLS Profile

**Type:** schema

Technique-specific profile for Structured Light Scanning (SLS) products

### `ogch.techniqueProfile.adaProfile.SVRUEC.profile-ada` — ADA SV-RUEC Profile

**Type:** schema

Technique-specific profile for Seismic Velocities and Rock Ultrasonic Elastic Constants (SV-RUEC) products

### `ogch.techniqueProfile.adaProfile.ToFSIMS.profile-ada` — ADA ToF-SIMS Profile

**Type:** schema

Technique-specific profile for Time-of-Flight Secondary Ion Mass Spectrometry (ToF-SIMS) products

### `ogch.techniqueProfile.adaProfile.UVFM.profile-ada` — ADA UVFM Profile

**Type:** schema

Technique-specific profile for Ultraviolet Fluorescence Microscopy (UVFM) products

### `ogch.techniqueProfile.adaProfile.VLM.profile-ada` — ADA VLM Profile

**Type:** schema

Technique-specific profile for Visible Light Microscopy (VLM) products

### `ogch.techniqueProfile.adaProfile.VNMIR.profile-ada` — ADA VNMIR Profile

**Type:** schema

Technique-specific profile for Very-Near Mid-Infrared (VNMIR/FTIR) spectroscopy products

### `ogch.techniqueProfile.adaProfile.XANES.profile-ada` — ADA XANES Profile

**Type:** schema

Technique-specific profile for X-ray Absorption Near Edge Structure (XANES) products

### `ogch.techniqueProfile.adaProfile.XRD.profile-ada` — ADA XRD Profile

**Type:** schema

Technique-specific profile for X-ray Diffraction (XRD) products

### `ogch.techniqueProfile.geochemProfile.EMPA.profile-ada` — ADA EMPA Profile

**Type:** schema

Technique-specific profile for Electron Microprobe Analysis (EMPA) products

### `ogch.techniqueProfile.geochemProfile.SEM.profile-ada` — ADA SEM Profile

**Type:** schema

Technique-specific profile for Scanning Electron Microscopy (SEM) products

### `ogch.techniqueProfile.geochemProfile.TEM.profile-ada` — ADA TEM Profile

**Type:** schema

Technique-specific profile for Transmission Electron Microscopy (TEM) products

### `ogch.techniqueProfile.geochemProfile.XCT.profile-ada` — ADA XCT Profile

**Type:** schema

Technique-specific profile for X-ray Computed Tomography (XCT) products

### `ogch.techniqueProfile.geochemProfile.AIVA.detail` — Advanced Imaging & Visualization of Astromaterials Analysis Detail

**Type:** schema

Detail block for AIVA hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No AIVA-specific analysis property is defined yet.

### `ogch.techniqueProfile.geochemProfile.AIVA.tapp` — Advanced Imaging & Visualization of Astromaterials Technique-Aligned Procedure Profile (aivaTAPP)

**Type:** schema

Advanced Imaging & Visualization of Astromaterials extension of the base TAPP definition. CORE-ONLY DRAFT: the native technique layer is empty. AIVA has no ADA detail schema and no technique-specific property in any ADA record, so there was nothing to seed one from and none was invented. This registers the procedure skeleton and needs Phase 0 seed papers before it says anything AIVA-specific. Generated from draftTAPPs/AIVA_TAPP_draft_v2.csv by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.AMS.detail` — Accelerator Mass Spectrometry Analysis Detail

**Type:** schema

Detail block for AMS hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No AMS-specific analysis property is defined yet.

### `ogch.techniqueProfile.geochemProfile.AMS.tapp` — Accelerator Mass Spectrometry Technique-Aligned Procedure Profile (amsTAPP)

**Type:** schema

Accelerator Mass Spectrometry extension of the base TAPP definition. CORE-ONLY DRAFT: the native technique layer is empty. AMS has no ADA detail schema and no technique-specific property in any ADA record, so there was nothing to seed one from and none was invented. This registers the procedure skeleton and needs Phase 0 seed papers before it says anything AMS-specific. Generated from draftTAPPs/AMS_TAPP_draft_v2.csv by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.ARGT.detail` — 40Ar/39Ar geochronology and thermochronology Analysis Detail

**Type:** schema

Detail block for ARGT hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No ARGT-specific analysis property is defined yet.

### `ogch.techniqueProfile.geochemProfile.ARGT.tapp` — 40Ar/39Ar geochronology and thermochronology Technique-Aligned Procedure Profile (argtTAPP)

**Type:** schema

40Ar/39Ar geochronology and thermochronology extension of the base TAPP definition. CORE-ONLY DRAFT: the native technique layer is empty. ARGT has no ADA detail schema and no technique-specific property in any ADA record, so there was nothing to seed one from and none was invented. This registers the procedure skeleton and needs Phase 0 seed papers before it says anything ARGT-specific. Generated from draftTAPPs/ARGT_TAPP_draft_v2.csv by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.CAPD.detail` — Capacitance Dilatometry Analysis Detail

**Type:** schema

Detail block for CAPD hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No CAPD-specific analysis property is defined yet.

### `ogch.techniqueProfile.geochemProfile.CAPD.tapp` — Capacitance Dilatometry Technique-Aligned Procedure Profile (capdTAPP)

**Type:** schema

Capacitance Dilatometry extension of the base TAPP definition. CORE-ONLY DRAFT: the native technique layer is empty. CAPD has no ADA detail schema and no technique-specific property in any ADA record, so there was nothing to seed one from and none was invented. This registers the procedure skeleton and needs Phase 0 seed papers before it says anything CAPD-specific. Generated from draftTAPPs/CAPD_TAPP_draft_v2.csv by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.CPD.detail` — Curation Photo-Documentation Analysis Detail

**Type:** schema

Detail block for CPD hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No CPD-specific analysis property is defined yet.

### `ogch.techniqueProfile.geochemProfile.CPD.tapp` — Curation Photo-Documentation Technique-Aligned Procedure Profile (cpdTAPP)

**Type:** schema

Curation Photo-Documentation extension of the base TAPP definition. CORE-ONLY DRAFT: the native technique layer is empty. CPD has no ADA detail schema and no technique-specific property in any ADA record, so there was nothing to seed one from and none was invented. This registers the procedure skeleton and needs Phase 0 seed papers before it says anything CPD-specific. Generated from draftTAPPs/CPD_TAPP_draft_v2.csv by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.DSC.detail` — Differential Scanning Calorimetry Analysis Detail

**Type:** schema

Detail block for DSC hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No DSC-specific analysis property is defined yet.

### `ogch.techniqueProfile.geochemProfile.DSC.tapp` — Differential Scanning Calorimetry Technique-Aligned Procedure Profile (dscTAPP)

**Type:** schema

Differential Scanning Calorimetry extension of the base TAPP definition. CORE-ONLY DRAFT: the native technique layer is empty. DSC has no ADA detail schema and no technique-specific property in any ADA record, so there was nothing to seed one from and none was invented. This registers the procedure skeleton and needs Phase 0 seed papers before it says anything DSC-specific. Generated from draftTAPPs/DSC_TAPP_draft_v2.csv by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.DSSM.detail` — Direct Shear Strength Measurement Analysis Detail

**Type:** schema

Detail block for DSSM hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No DSSM-specific analysis property is defined yet.

### `ogch.techniqueProfile.geochemProfile.DSSM.tapp` — Direct Shear Strength Measurement Technique-Aligned Procedure Profile (dssmTAPP)

**Type:** schema

Direct Shear Strength Measurement extension of the base TAPP definition. CORE-ONLY DRAFT: the native technique layer is empty. DSSM has no ADA detail schema and no technique-specific property in any ADA record, so there was nothing to seed one from and none was invented. This registers the procedure skeleton and needs Phase 0 seed papers before it says anything DSSM-specific. Generated from draftTAPPs/DSSM_TAPP_draft_v2.csv by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.EAIRMS.detail` — Elemental analysis - isotope ratio mass spectrometry Analysis Detail

**Type:** schema

Detail block for EAIRMS hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No EAIRMS-specific analysis property is defined yet.

### `ogch.techniqueProfile.geochemProfile.EAIRMS.tapp` — Elemental analysis - isotope ratio mass spectrometry Technique-Aligned Procedure Profile (eairmsTAPP)

**Type:** schema

Elemental analysis - isotope ratio mass spectrometry extension of the base TAPP definition. CORE-ONLY DRAFT: the native technique layer is empty. EAIRMS has no ADA detail schema and no technique-specific property in any ADA record, so there was nothing to seed one from and none was invented. This registers the procedure skeleton and needs Phase 0 seed papers before it says anything EAIRMS-specific. Generated from draftTAPPs/EAIRMS_TAPP_draft_v2.csv by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.EMPA.detail` — EMPA Instrument Detail

**Type:** schema

Electron Microprobe Analysis instrument-specific detail properties. Defines properties: @type, spectrometersUsed, signalUsed.

### `ogch.techniqueProfile.geochemProfile.EMPA.tapp` — EMPA Technique-Aligned Protocol Profile (empaTAPP)

**Type:** schema

EMPA-specific extension of the base TAPP definition. Adds EPMA top-level properties (beam mode, accelerating voltage, matrix correction method), a parameter vocabulary, and an analyte-column template covering EPMA per-element acquisition and reporting fields. Vocabularies, parameter templates, and analyte-column templates ship as separate JSON files under vocab/, parameters/, and analyteColumns/ for maintainability.

### `ogch.techniqueProfile.geochemProfile.FINESSE.detail` — Stepped Heating Carbon and Nitrogen Isotopic Compositions Analysis Detail

**Type:** schema

Detail block for FINESSE hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No FINESSE-specific analysis property is defined yet.

### `ogch.techniqueProfile.geochemProfile.FINESSE.tapp` — Stepped Heating Carbon and Nitrogen Isotopic Compositions Technique-Aligned Procedure Profile (finesseTAPP)

**Type:** schema

Stepped Heating Carbon and Nitrogen Isotopic Compositions extension of the base TAPP definition. CORE-ONLY DRAFT: the native technique layer is empty. FINESSE has no ADA detail schema and no technique-specific property in any ADA record, so there was nothing to seed one from and none was invented. This registers the procedure skeleton and needs Phase 0 seed papers before it says anything FINESSE-specific. Generated from draftTAPPs/FINESSE_TAPP_draft_v2.csv by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.FTICRMS.detail` — Fourier Transform Ion Cyclotron Resonance Mass Spectrometry Analysis Detail

**Type:** schema

Detail block for FTICRMS hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No FTICRMS-specific analysis property is defined yet.

### `ogch.techniqueProfile.geochemProfile.FTICRMS.tapp` — Fourier Transform Ion Cyclotron Resonance Mass Spectrometry Technique-Aligned Procedure Profile (fticrmsTAPP)

**Type:** schema

Fourier Transform Ion Cyclotron Resonance Mass Spectrometry extension of the base TAPP definition. CORE-ONLY DRAFT: the native technique layer is empty. FTICRMS has no ADA detail schema and no technique-specific property in any ADA record, so there was nothing to seed one from and none was invented. This registers the procedure skeleton and needs Phase 0 seed papers before it says anything FTICRMS-specific. Generated from draftTAPPs/FTICRMS_TAPP_draft_v2.csv by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.GC-C-IRMS.detail` — Gas Chromatography-Combustion-Isotopic Ratio Mass Spectromet Analysis Detail

**Type:** schema

Detail block for GC-C-IRMS hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No GC-C-IRMS-specific analysis property is defined yet.

### `ogch.techniqueProfile.geochemProfile.GC-C-IRMS.tapp` — Gas Chromatography-Combustion-Isotopic Ratio Mass Spectromet Technique-Aligned Procedure Profile (gcCIrmsTAPP)

**Type:** schema

Gas Chromatography-Combustion-Isotopic Ratio Mass Spectrometry extension of the base TAPP definition. CORE-ONLY DRAFT: the native technique layer is empty. GC-C-IRMS has no ADA detail schema and no technique-specific property in any ADA record, so there was nothing to seed one from and none was invented. This registers the procedure skeleton and needs Phase 0 seed papers before it says anything GC-C-IRMS-specific. Generated from draftTAPPs/GC-C-IRMS_TAPP_draft_v2.csv by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.GCMS.detail` — Gas Chromatography-Mass Spectrometry Analysis Detail

**Type:** schema

Detail block for GCMS hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No GCMS-specific analysis property is defined yet.

### `ogch.techniqueProfile.geochemProfile.GCMS.tapp` — Gas Chromatography-Mass Spectrometry Technique-Aligned Procedure Profile (gcmsTAPP)

**Type:** schema

Gas Chromatography-Mass Spectrometry extension of the base TAPP definition. CORE-ONLY DRAFT: the native technique layer is empty. GCMS has no ADA detail schema and no technique-specific property in any ADA record, so there was nothing to seed one from and none was invented. This registers the procedure skeleton and needs Phase 0 seed papers before it says anything GCMS-specific. Generated from draftTAPPs/GCMS_TAPP_draft_v2.csv by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.GPYC.detail` — Gas pycnometry Analysis Detail

**Type:** schema

Detail block for GPYC hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No GPYC-specific analysis property is defined yet.

### `ogch.techniqueProfile.geochemProfile.GPYC.tapp` — Gas pycnometry Technique-Aligned Procedure Profile (gpycTAPP)

**Type:** schema

Gas pycnometry extension of the base TAPP definition. CORE-ONLY DRAFT: the native technique layer is empty. GPYC has no ADA detail schema and no technique-specific property in any ADA record, so there was nothing to seed one from and none was invented. This registers the procedure skeleton and needs Phase 0 seed papers before it says anything GPYC-specific. Generated from draftTAPPs/GPYC_TAPP_draft_v2.csv by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.IC.detail` — Ion Chromatography Analysis Detail

**Type:** schema

Detail block for IC hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No IC-specific analysis property is defined yet.

### `ogch.techniqueProfile.geochemProfile.IC.tapp` — Ion Chromatography Technique-Aligned Procedure Profile (icTAPP)

**Type:** schema

Ion Chromatography extension of the base TAPP definition. CORE-ONLY DRAFT: the native technique layer is empty. IC has no ADA detail schema and no technique-specific property in any ADA record, so there was nothing to seed one from and none was invented. This registers the procedure skeleton and needs Phase 0 seed papers before it says anything IC-specific. Generated from draftTAPPs/IC_TAPP_draft_v2.csv by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.IC-MS.detail` — Ion Chromatography-Mass Spectrometry Analysis Detail

**Type:** schema

Detail block for IC-MS hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No IC-MS-specific analysis property is defined yet.

### `ogch.techniqueProfile.geochemProfile.IC-MS.tapp` — Ion Chromatography-Mass Spectrometry Technique-Aligned Procedure Profile (icMsTAPP)

**Type:** schema

Ion Chromatography-Mass Spectrometry extension of the base TAPP definition. CORE-ONLY DRAFT: the native technique layer is empty. IC-MS has no ADA detail schema and no technique-specific property in any ADA record, so there was nothing to seed one from and none was invented. This registers the procedure skeleton and needs Phase 0 seed papers before it says anything IC-MS-specific. Generated from draftTAPPs/IC-MS_TAPP_draft_v2.csv by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.ICPOES.detail` — Inductively coupled plasma - optical emission spectrometry Analysis Detail

**Type:** schema

Detail block for ICPOES hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No ICPOES-specific analysis property is defined yet.

### `ogch.techniqueProfile.geochemProfile.ICPOES.tapp` — Inductively coupled plasma - optical emission spectrometry Technique-Aligned Procedure Profile (icpoesTAPP)

**Type:** schema

Inductively coupled plasma - optical emission spectrometry extension of the base TAPP definition. CORE-ONLY DRAFT: the native technique layer is empty. ICPOES has no ADA detail schema and no technique-specific property in any ADA record, so there was nothing to seed one from and none was invented. This registers the procedure skeleton and needs Phase 0 seed papers before it says anything ICPOES-specific. Generated from draftTAPPs/ICPOES_TAPP_draft_v2.csv by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.L2MS.detail` — Microprobe Two-Step Laser Mass Spectrometry Analysis Detail

**Type:** schema

Detail block for L2MS hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No L2MS-specific analysis property is defined yet.

### `ogch.techniqueProfile.geochemProfile.L2MS.tapp` — Microprobe Two-Step Laser Mass Spectrometry Technique-Aligned Procedure Profile (l2msTAPP)

**Type:** schema

Microprobe Two-Step Laser Mass Spectrometry extension of the base TAPP definition. CORE-ONLY DRAFT: the native technique layer is empty. L2MS has no ADA detail schema and no technique-specific property in any ADA record, so there was nothing to seed one from and none was invented. This registers the procedure skeleton and needs Phase 0 seed papers before it says anything L2MS-specific. Generated from draftTAPPs/L2MS_TAPP_draft_v2.csv by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.LA-MC-ICPMS.detail` — LA-MC-ICP-MS Analysis Detail

**Type:** schema

Dataset-level analysis-instance detail for LA-MC-ICP-MS, reusing CDIF/schema.org slots on the schema:Dataset root.

### `ogch.techniqueProfile.geochemProfile.LA-MC-ICPMS.tapp` — LA-MC-ICP-MS Technique-Aligned Procedure Profile (laMcicpmsTAPP)

**Type:** schema

Laser-ablation multi-collector ICP-MS extension of the base TAPP definition, generated from TAPPS20260813/Current TAPPs/LA-MC-ICPMS_TAPP_v13.csv via the path-driven pipeline.

### `ogch.techniqueProfile.geochemProfile.LA-MC-ICPMS-UPb.detail` — LA-MC-ICP-MS U-Pb Analysis Detail

**Type:** schema

Dataset-level analysis-instance detail for LA-MC-ICP-MS U-Pb geochronology, reusing CDIF/schema.org slots on the schema:Dataset root.

### `ogch.techniqueProfile.geochemProfile.LA-MC-ICPMS-UPb.tapp` — LA-MC-ICP-MS U-Pb Geochronology TAPP (laMcicpmsUPbTAPP)

**Type:** schema

Laser-ablation multi-collector ICP-MS U-Pb geochronology extension of the base TAPP definition, generated from TAPPS20260813/Current TAPPs/LA-MC-ICPMS_UPb_TAPP_v13.csv via the path-driven pipeline.

### `ogch.techniqueProfile.geochemProfile.LA-Q-ICPMS.detail` — LA-Q-ICP-MS Analysis Detail

**Type:** schema

Dataset-level analysis-instance detail for LA-Q-ICP-MS, reusing CDIF/schema.org slots on the schema:Dataset root.

### `ogch.techniqueProfile.geochemProfile.LA-Q-ICPMS.tapp` — LA-Q-ICP-MS Technique-Aligned Procedure Profile (laQicpmsTAPP)

**Type:** schema

Laser-ablation quadrupole ICP-MS extension of the base TAPP definition, generated from TAPPS20260813/Current TAPPs/LA-Q-ICP-MS_TAPP_v15.csv via the path-driven pipeline (bootstrap_schemapaths.py + build_pathdriven.py).

### `ogch.techniqueProfile.geochemProfile.LA-Q-ICPMS-UPb.detail` — LA-Q-ICP-MS U-Pb Analysis Detail

**Type:** schema

Dataset-level analysis-instance detail for LA-Q-ICP-MS U-Pb geochronology, reusing CDIF/schema.org slots on the schema:Dataset root.

### `ogch.techniqueProfile.geochemProfile.LA-Q-ICPMS-UPb.tapp` — LA-Q-ICP-MS U-Pb Geochronology TAPP (laQicpmsUPbTAPP)

**Type:** schema

Laser-ablation quadrupole ICP-MS U-Pb geochronology extension of the base TAPP definition, generated from TAPPS20260813/Current TAPPs/LA-Q-ICP-MS_UPb_TAPP_v16.csv via the path-driven pipeline.

### `ogch.techniqueProfile.geochemProfile.LA-SF-ICPMS.detail` — LA-SF-ICP-MS Analysis Detail

**Type:** schema

Dataset-level analysis-instance detail for LA-SF-ICP-MS, reusing CDIF/schema.org slots on the schema:Dataset root.

### `ogch.techniqueProfile.geochemProfile.LA-SF-ICPMS.tapp` — LA-SF-ICP-MS Technique-Aligned Procedure Profile (laSficpmsTAPP)

**Type:** schema

Laser-ablation sector-field (high-resolution) ICP-MS extension of the base TAPP definition, generated from TAPPS20260813/Current TAPPs/LA-SF-ICP-MS_TAPP_v16.csv via the path-driven pipeline.

### `ogch.techniqueProfile.geochemProfile.LA-SF-ICPMS-UPb.detail` — LA-SF-ICP-MS U-Pb Analysis Detail

**Type:** schema

Dataset-level analysis-instance detail for LA-SF-ICP-MS U-Pb geochronology, reusing CDIF/schema.org slots on the schema:Dataset root.

### `ogch.techniqueProfile.geochemProfile.LA-SF-ICPMS-UPb.tapp` — LA-SF-ICP-MS U-Pb Geochronology TAPP (laSficpmsUPbTAPP)

**Type:** schema

Laser-ablation sector-field ICP-MS U-Pb geochronology extension of the base TAPP definition, generated from TAPPS20260813/Current TAPPs/LA-SF-ICP-MS_UPb_TAPP_v17.csv via the path-driven pipeline.

### `ogch.techniqueProfile.geochemProfile.LAF.detail` — Laser Assisted Fluorination for Bulk Oxygen Isotope Ratio Me Analysis Detail

**Type:** schema

Detail block for LAF hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No LAF-specific analysis property is defined yet.

### `ogch.techniqueProfile.geochemProfile.LAF.tapp` — Laser Assisted Fluorination for Bulk Oxygen Isotope Ratio Me Technique-Aligned Procedure Profile (lafTAPP)

**Type:** schema

Laser Assisted Fluorination for Bulk Oxygen Isotope Ratio Measurements extension of the base TAPP definition. CORE-ONLY DRAFT: the native technique layer is empty. LAF has no ADA detail schema and no technique-specific property in any ADA record, so there was nothing to seed one from and none was invented. This registers the procedure skeleton and needs Phase 0 seed papers before it says anything LAF-specific. Generated from draftTAPPs/LAF_TAPP_draft_v2.csv by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.LCMS.detail` — Liquid Chromatography-Mass Spectrometry Analysis Detail

**Type:** schema

Detail block for LCMS hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No LCMS-specific analysis property is defined yet.

### `ogch.techniqueProfile.geochemProfile.LCMS.tapp` — Liquid Chromatography-Mass Spectrometry Technique-Aligned Procedure Profile (lcmsTAPP)

**Type:** schema

Liquid Chromatography-Mass Spectrometry extension of the base TAPP definition. CORE-ONLY DRAFT: the native technique layer is empty. LCMS has no ADA detail schema and no technique-specific property in any ADA record, so there was nothing to seed one from and none was invented. This registers the procedure skeleton and needs Phase 0 seed papers before it says anything LCMS-specific. Generated from draftTAPPs/LCMS_TAPP_draft_v2.csv by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.LIT.detail` — Lock-In Thermography Analysis Detail

**Type:** schema

Detail block for LIT hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No LIT-specific analysis property is defined yet.

### `ogch.techniqueProfile.geochemProfile.LIT.tapp` — Lock-In Thermography Technique-Aligned Procedure Profile (litTAPP)

**Type:** schema

Lock-In Thermography extension of the base TAPP definition. CORE-ONLY DRAFT: the native technique layer is empty. LIT has no ADA detail schema and no technique-specific property in any ADA record, so there was nothing to seed one from and none was invented. This registers the procedure skeleton and needs Phase 0 seed papers before it says anything LIT-specific. Generated from draftTAPPs/LIT_TAPP_draft_v2.csv by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.NGNSMS.detail` — Noble gas and Nitrogen Static Mass Spectrometry Analysis Detail

**Type:** schema

Detail block for NGNSMS hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No NGNSMS-specific analysis property is defined yet.

### `ogch.techniqueProfile.geochemProfile.NGNSMS.tapp` — Noble gas and Nitrogen Static Mass Spectrometry Technique-Aligned Procedure Profile (ngnsmsTAPP)

**Type:** schema

Noble gas and Nitrogen Static Mass Spectrometry extension of the base TAPP definition. CORE-ONLY DRAFT: the native technique layer is empty. NGNSMS has no ADA detail schema and no technique-specific property in any ADA record, so there was nothing to seed one from and none was invented. This registers the procedure skeleton and needs Phase 0 seed papers before it says anything NGNSMS-specific. Generated from draftTAPPs/NGNSMS_TAPP_draft_v2.csv by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.NI-MI.detail` — Nanoindentation and Microindentation Analysis Detail

**Type:** schema

Detail block for NI-MI hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No NI-MI-specific analysis property is defined yet.

### `ogch.techniqueProfile.geochemProfile.NI-MI.tapp` — Nanoindentation and Microindentation Technique-Aligned Procedure Profile (niMiTAPP)

**Type:** schema

Nanoindentation and Microindentation extension of the base TAPP definition. CORE-ONLY DRAFT: the native technique layer is empty. NI-MI has no ADA detail schema and no technique-specific property in any ADA record, so there was nothing to seed one from and none was invented. This registers the procedure skeleton and needs Phase 0 seed papers before it says anything NI-MI-specific. Generated from draftTAPPs/NI-MI_TAPP_draft_v2.csv by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.NanoIR.detail` — Nanoscale Infrared Mapping Analysis Detail

**Type:** schema

Detail block for NanoIR hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No NanoIR-specific analysis property is defined yet.

### `ogch.techniqueProfile.geochemProfile.NanoIR.tapp` — Nanoscale Infrared Mapping Technique-Aligned Procedure Profile (nanoirTAPP)

**Type:** schema

Nanoscale Infrared Mapping extension of the base TAPP definition. CORE-ONLY DRAFT: the native technique layer is empty. NanoIR has no ADA detail schema and no technique-specific property in any ADA record, so there was nothing to seed one from and none was invented. This registers the procedure skeleton and needs Phase 0 seed papers before it says anything NanoIR-specific. Generated from draftTAPPs/NanoIR_TAPP_draft_v2.csv by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.NanoSIMS.detail` — Nanoscale secondary ion mass spectrometry Analysis Detail

**Type:** schema

Detail block for NanoSIMS hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No NanoSIMS-specific analysis property is defined yet.

### `ogch.techniqueProfile.geochemProfile.NanoSIMS.tapp` — Nanoscale secondary ion mass spectrometry Technique-Aligned Procedure Profile (nanosimsTAPP)

**Type:** schema

Nanoscale secondary ion mass spectrometry extension of the base TAPP definition. CORE-ONLY DRAFT: the native technique layer is empty. NanoSIMS has no ADA detail schema and no technique-specific property in any ADA record, so there was nothing to seed one from and none was invented. This registers the procedure skeleton and needs Phase 0 seed papers before it says anything NanoSIMS-specific. Generated from draftTAPPs/NanoSIMS_TAPP_draft_v2.csv by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.PCD-AFM.detail` — Particle cohesion determination with AFM Analysis Detail

**Type:** schema

Detail block for PCD-AFM hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No PCD-AFM-specific analysis property is defined yet.

### `ogch.techniqueProfile.geochemProfile.PCD-AFM.tapp` — Particle cohesion determination with AFM Technique-Aligned Procedure Profile (pcdAfmTAPP)

**Type:** schema

Particle cohesion determination with AFM extension of the base TAPP definition. CORE-ONLY DRAFT: the native technique layer is empty. PCD-AFM has no ADA detail schema and no technique-specific property in any ADA record, so there was nothing to seed one from and none was invented. This registers the procedure skeleton and needs Phase 0 seed papers before it says anything PCD-AFM-specific. Generated from draftTAPPs/PCD-AFM_TAPP_draft_v2.csv by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.PSFD.detail` — Particle Size Frequency Distribution Analysis Detail

**Type:** schema

Detail block for PSFD hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No PSFD-specific analysis property is defined yet.

### `ogch.techniqueProfile.geochemProfile.PSFD.tapp` — Particle Size Frequency Distribution Technique-Aligned Procedure Profile (psfdTAPP)

**Type:** schema

Particle Size Frequency Distribution extension of the base TAPP definition. CORE-ONLY DRAFT: the native technique layer is empty. PSFD has no ADA detail schema and no technique-specific property in any ADA record, so there was nothing to seed one from and none was invented. This registers the procedure skeleton and needs Phase 0 seed papers before it says anything PSFD-specific. Generated from draftTAPPs/PSFD_TAPP_draft_v2.csv by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.QRIS.detail` — QRIS Analysis Detail

**Type:** schema

Detail block for QRIS hasPart items, carrying the analysis-level properties supplied per imaging session rather than fixed by the procedure.

### `ogch.techniqueProfile.geochemProfile.QRIS.tapp` — QRIS Technique-Aligned Procedure Profile (qrisTAPP)

**Type:** schema

Quantitative Reflectance Imaging System extension of the base TAPP definition. QRIS has no per-element analyte axis, so no ada:analyteTemplate is defined, and no mode-flag columns: its ADA componentTypes are pipeline stages of one acquisition, not modes. DRAFT - generated from draftTAPPs/QRIS_TAPP_draft_v2.csv by tools/build_tapp.py; the source table has not been through Phase 0 review.

### `ogch.techniqueProfile.geochemProfile.RAMAN.detail` — Raman Analysis Detail

**Type:** schema

Detail block for Raman hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No Raman-specific analysis property is defined yet.

### `ogch.techniqueProfile.geochemProfile.RAMAN.tapp` — Raman Technique-Aligned Procedure Profile (ramanTAPP)

**Type:** schema

Raman vibrational spectroscopy extension of the base TAPP definition. CORE-ONLY DRAFT: the native technique layer is empty. Raman has no ADA detail schema and no technique property in any ADA record, so there was nothing to seed one from and none was invented - no laser wavelength, grating or objective appears here. This registers the procedure skeleton and needs Phase 0 seed papers before it says anything Raman-specific. Generated from draftTAPPs/RAMAN_TAPP_draft_v2.csv by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.RITOFNGMS.detail` — Resonance ionization time of flight noble gas mass spectrome Analysis Detail

**Type:** schema

Detail block for RITOFNGMS hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No RITOFNGMS-specific analysis property is defined yet.

### `ogch.techniqueProfile.geochemProfile.RITOFNGMS.tapp` — Resonance ionization time of flight noble gas mass spectrome Technique-Aligned Procedure Profile (ritofngmsTAPP)

**Type:** schema

Resonance ionization time of flight noble gas mass spectrometry extension of the base TAPP definition. CORE-ONLY DRAFT: the native technique layer is empty. RITOFNGMS has no ADA detail schema and no technique-specific property in any ADA record, so there was nothing to seed one from and none was invented. This registers the procedure skeleton and needs Phase 0 seed papers before it says anything RITOFNGMS-specific. Generated from draftTAPPs/RITOFNGMS_TAPP_draft_v2.csv by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.S-XRF.detail` — Synchrotron-based X-ray Fluorescence Spectroscopy Analysis Detail

**Type:** schema

Detail block for S-XRF hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No S-XRF-specific analysis property is defined yet.

### `ogch.techniqueProfile.geochemProfile.S-XRF.tapp` — Synchrotron-based X-ray Fluorescence Spectroscopy Technique-Aligned Procedure Profile (sXrfTAPP)

**Type:** schema

Synchrotron-based X-ray Fluorescence Spectroscopy extension of the base TAPP definition. CORE-ONLY DRAFT: the native technique layer is empty. S-XRF has no ADA detail schema and no technique-specific property in any ADA record, so there was nothing to seed one from and none was invented. This registers the procedure skeleton and needs Phase 0 seed papers before it says anything S-XRF-specific. Generated from draftTAPPs/S-XRF_TAPP_draft_v2.csv by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.SEM.detail` — SEM Analysis Detail

**Type:** schema

Dataset-level analysis-instance detail for SEM (superset), reusing CDIF/schema.org slots on the schema:Dataset root.

### `ogch.techniqueProfile.geochemProfile.SEM.tapp` — SEM Technique-Aligned Protocol Profile (semTAPP)

**Type:** schema

Scanning electron microscopy superset (imaging + EDS/WDS composition + EBSD + FIB-SEM) extension of the base TAPP definition, generated from docs/SEM_TAPP_v4.xlsx via the path-driven pipeline.

### `ogch.techniqueProfile.geochemProfile.SEM-CL.detail` — SEM Cathodoluminescence Spectroscopy Analysis Detail

**Type:** schema

Detail block for SEM-CL hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No SEM-CL-specific analysis property is defined yet.

### `ogch.techniqueProfile.geochemProfile.SEM-CL.tapp` — SEM Cathodoluminescence Spectroscopy Technique-Aligned Procedure Profile (semClTAPP)

**Type:** schema

SEM Cathodoluminescence Spectroscopy extension of the base TAPP definition. CORE-ONLY DRAFT: the native technique layer is empty. SEM-CL has no ADA detail schema and no technique-specific property in any ADA record, so there was nothing to seed one from and none was invented. This registers the procedure skeleton and needs Phase 0 seed papers before it says anything SEM-CL-specific. Generated from draftTAPPs/SEM-CL_TAPP_draft_v2.csv by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.SEM-Composition.detail` — SEM Composition Analysis Detail

**Type:** schema

Dataset-level analysis-instance detail for SEM composition (EDS/WDS), reusing CDIF/schema.org slots on the schema:Dataset root.

### `ogch.techniqueProfile.geochemProfile.SEM-Composition.tapp` — SEM Composition (EDS/WDS) Technique-Aligned Protocol Profile (semCompositionTAPP)

**Type:** schema

Scanning electron microscopy compositional microanalysis (EDS/WDS) extension of the base TAPP definition, generated from docs/SEM_Composition_TAPP_v4.xlsx via the path-driven pipeline (bootstrap_schemapaths.py + build_pathdriven.py).

### `ogch.techniqueProfile.geochemProfile.SEM-FIBSEM.detail` — FIB-SEM Analysis Detail

**Type:** schema

Detail block for FIB-SEM hasPart items. Discriminates on ada:componentType, carries analysis-level required properties and an @id reference to a registered semFibsemTAPP definition, and per-dataset schema:additionalProperty entries constrained via $refs to the parameterValues registry plus a catch-all. Generated by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.SEM-FIBSEM.tapp` — FIB-SEM Technique-Aligned Protocol Profile (semFibsemTAPP)

**Type:** schema

Focused-ion-beam SEM (FIB-SEM tomography, TEM lamella prep) extension of the base TAPP definition. Basic protocol-tier fields are required top-level ada: properties; Advanced protocol-tier fields are schema:additionalProperty[] entries. No ada:analyteTemplate. Generated from docs/SEM_FIBSEM_TAPP_v4.xlsx by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.SEM-Imaging.detail` — SEM Imaging Analysis Detail

**Type:** schema

Detail block for SEM imaging hasPart items. Discriminates on ada:componentType, carries analysis-level required properties and an @id reference to a registered semImagingTAPP definition, and per-dataset schema:additionalProperty entries constrained via $refs to the parameterValues registry plus a catch-all. Generated by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.SEM-Imaging.tapp` — SEM Imaging Technique-Aligned Protocol Profile (semImagingTAPP)

**Type:** schema

Scanning electron microscopy imaging (SE/BSE/CL/EBSD) extension of the base TAPP definition. Basic protocol-tier fields are required top-level ada: properties; Advanced protocol-tier fields are schema:additionalProperty[] entries. No ada:analyteTemplate (imaging has no per-element analyte axis). Generated from docs/SEM_Imaging_TAPP_v4.xlsx by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.SIMS.detail` — Secondary ion mass spectrometry Analysis Detail

**Type:** schema

Detail block for SIMS hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No SIMS-specific analysis property is defined yet.

### `ogch.techniqueProfile.geochemProfile.SIMS.tapp` — Secondary ion mass spectrometry Technique-Aligned Procedure Profile (simsTAPP)

**Type:** schema

Secondary ion mass spectrometry extension of the base TAPP definition. CORE-ONLY DRAFT: the native technique layer is empty. SIMS has no ADA detail schema and no technique-specific property in any ADA record, so there was nothing to seed one from and none was invented. This registers the procedure skeleton and needs Phase 0 seed papers before it says anything SIMS-specific. Generated from draftTAPPs/SIMS_TAPP_draft_v2.csv by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.SLS.detail` — Structured Light Scanning Analysis Detail

**Type:** schema

Detail block for SLS hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No SLS-specific analysis property is defined yet.

### `ogch.techniqueProfile.geochemProfile.SLS.tapp` — Structured Light Scanning Technique-Aligned Procedure Profile (slsTAPP)

**Type:** schema

Structured Light Scanning extension of the base TAPP definition. CORE-ONLY DRAFT: the native technique layer is empty. SLS has no ADA detail schema and no technique-specific property in any ADA record, so there was nothing to seed one from and none was invented. This registers the procedure skeleton and needs Phase 0 seed papers before it says anything SLS-specific. Generated from draftTAPPs/SLS_TAPP_draft_v2.csv by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.STHM-AFM.detail` — Scanning Thermal Microscopy with AFM Analysis Detail

**Type:** schema

Detail block for STHM-AFM hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No STHM-AFM-specific analysis property is defined yet.

### `ogch.techniqueProfile.geochemProfile.STHM-AFM.tapp` — Scanning Thermal Microscopy with AFM Technique-Aligned Procedure Profile (sthmAfmTAPP)

**Type:** schema

Scanning Thermal Microscopy with AFM extension of the base TAPP definition. CORE-ONLY DRAFT: the native technique layer is empty. STHM-AFM has no ADA detail schema and no technique-specific property in any ADA record, so there was nothing to seed one from and none was invented. This registers the procedure skeleton and needs Phase 0 seed papers before it says anything STHM-AFM-specific. Generated from draftTAPPs/STHM-AFM_TAPP_draft_v2.csv by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.SVRUEC.detail` — Seismic Velocities and Rock Ultrasonic Elastic Constants Analysis Detail

**Type:** schema

Detail block for SVRUEC hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No SVRUEC-specific analysis property is defined yet.

### `ogch.techniqueProfile.geochemProfile.SVRUEC.tapp` — Seismic Velocities and Rock Ultrasonic Elastic Constants Technique-Aligned Procedure Profile (svruecTAPP)

**Type:** schema

Seismic Velocities and Rock Ultrasonic Elastic Constants extension of the base TAPP definition. CORE-ONLY DRAFT: the native technique layer is empty. SVRUEC has no ADA detail schema and no technique-specific property in any ADA record, so there was nothing to seed one from and none was invented. This registers the procedure skeleton and needs Phase 0 seed papers before it says anything SVRUEC-specific. Generated from draftTAPPs/SVRUEC_TAPP_draft_v2.csv by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.Solution-MC-ICPMS.detail` — Solution MC-ICP-MS Analysis Detail

**Type:** schema

Dataset-level analysis-instance detail for solution MC-ICP-MS, reusing CDIF/schema.org slots on the schema:Dataset root.

### `ogch.techniqueProfile.geochemProfile.Solution-MC-ICPMS.tapp` — Solution MC-ICP-MS Technique-Aligned Procedure Profile (solutionMcicpmsTAPP)

**Type:** schema

Solution multi-collector ICP-MS extension of the base TAPP definition, generated from TAPPS20260813/Current TAPPs/Solution_MC-ICP-MS_TAPP_v16.csv via the path-driven pipeline.

### `ogch.techniqueProfile.geochemProfile.Solution-Q-ICPMS.detail` — Solution Q-ICP-MS Analysis Detail

**Type:** schema

Dataset-level analysis-instance detail for solution Q-ICP-MS, reusing CDIF/schema.org slots on the schema:Dataset root.

### `ogch.techniqueProfile.geochemProfile.Solution-Q-ICPMS.tapp` — Solution Q-ICP-MS Technique-Aligned Protocol Profile (solutionQicpmsTAPP)

**Type:** schema

Solution quadrupole ICP-MS extension of the base TAPP definition, generated from docs/Solution_Q-ICP-MS_TAPP_v5.xlsx via the path-driven pipeline.

### `ogch.techniqueProfile.geochemProfile.Solution-SF-ICPMS.detail` — Solution SF-ICP-MS Analysis Detail

**Type:** schema

Dataset-level analysis-instance detail for solution SF-ICP-MS, reusing CDIF/schema.org slots on the schema:Dataset root.

### `ogch.techniqueProfile.geochemProfile.Solution-SF-ICPMS.tapp` — Solution SF-ICP-MS Technique-Aligned Protocol Profile (solutionSficpmsTAPP)

**Type:** schema

Solution sector-field (high-resolution) ICP-MS extension of the base TAPP definition, generated from docs/Solution_SF-ICP-MS_TAPP_v5.xlsx via the path-driven pipeline.

### `ogch.techniqueProfile.geochemProfile.TDM.detail` — Temperature-Dependent Magnetization Analysis Detail

**Type:** schema

Detail block for TDM hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No TDM-specific analysis property is defined yet.

### `ogch.techniqueProfile.geochemProfile.TDM.tapp` — Temperature-Dependent Magnetization Technique-Aligned Procedure Profile (tdmTAPP)

**Type:** schema

Temperature-Dependent Magnetization extension of the base TAPP definition. CORE-ONLY DRAFT: the native technique layer is empty. TDM has no ADA detail schema and no technique-specific property in any ADA record, so there was nothing to seed one from and none was invented. This registers the procedure skeleton and needs Phase 0 seed papers before it says anything TDM-specific. Generated from draftTAPPs/TDM_TAPP_draft_v2.csv by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.TEM.detail` — TEM Analysis Detail

**Type:** schema

Detail block for TEM hasPart items. Discriminates on ada:componentType, carries analysis-level required properties and an @id reference to a registered temTAPP definition, and per-dataset schema:additionalProperty entries constrained via $refs to the parameterValues registry plus a catch-all. Generated by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.TEM.tapp` — TEM Technique-Aligned Protocol Profile (temTAPP)

**Type:** schema

Transmission electron microscopy (TEM/STEM, incl. EDS/EELS) extension of the base TAPP definition. Basic protocol-tier fields are required top-level ada: properties; Advanced protocol-tier fields are schema:additionalProperty[] entries; an ada:analyteTemplate carries per-element columns. Generated from docs/TEM_TAPP_v7.xlsx by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.TIMS.detail` — Thermal ionization mass spectrometry Analysis Detail

**Type:** schema

Detail block for TIMS hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No TIMS-specific analysis property is defined yet.

### `ogch.techniqueProfile.geochemProfile.TIMS.tapp` — Thermal ionization mass spectrometry Technique-Aligned Procedure Profile (timsTAPP)

**Type:** schema

Thermal ionization mass spectrometry extension of the base TAPP definition. CORE-ONLY DRAFT: the native technique layer is empty. TIMS has no ADA detail schema and no technique-specific property in any ADA record, so there was nothing to seed one from and none was invented. This registers the procedure skeleton and needs Phase 0 seed papers before it says anything TIMS-specific. Generated from draftTAPPs/TIMS_TAPP_draft_v2.csv by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.ToFSIMS.detail` — Time-of-Flight Secondary Ion Mass Spectrometer Analysis Detail

**Type:** schema

Detail block for ToFSIMS hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No ToFSIMS-specific analysis property is defined yet.

### `ogch.techniqueProfile.geochemProfile.ToFSIMS.tapp` — Time-of-Flight Secondary Ion Mass Spectrometer Technique-Aligned Procedure Profile (tofsimsTAPP)

**Type:** schema

Time-of-Flight Secondary Ion Mass Spectrometer extension of the base TAPP definition. CORE-ONLY DRAFT: the native technique layer is empty. ToFSIMS has no ADA detail schema and no technique-specific property in any ADA record, so there was nothing to seed one from and none was invented. This registers the procedure skeleton and needs Phase 0 seed papers before it says anything ToFSIMS-specific. Generated from draftTAPPs/ToFSIMS_TAPP_draft_v2.csv by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.UVFM.detail` — UV Fluorescence Microscopy Analysis Detail

**Type:** schema

Detail block for UVFM hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No UVFM-specific analysis property is defined yet.

### `ogch.techniqueProfile.geochemProfile.UVFM.tapp` — UV Fluorescence Microscopy Technique-Aligned Procedure Profile (uvfmTAPP)

**Type:** schema

UV Fluorescence Microscopy extension of the base TAPP definition. CORE-ONLY DRAFT: the native technique layer is empty. UVFM has no ADA detail schema and no technique-specific property in any ADA record, so there was nothing to seed one from and none was invented. This registers the procedure skeleton and needs Phase 0 seed papers before it says anything UVFM-specific. Generated from draftTAPPs/UVFM_TAPP_draft_v2.csv by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.VLM.detail` — Visible Light Microscopy Analysis Detail

**Type:** schema

Detail block for VLM hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No VLM-specific analysis property is defined yet.

### `ogch.techniqueProfile.geochemProfile.VLM.tapp` — Visible Light Microscopy Technique-Aligned Procedure Profile (vlmTAPP)

**Type:** schema

Visible Light Microscopy extension of the base TAPP definition. CORE-ONLY DRAFT: the native technique layer is empty. VLM has no ADA detail schema and no technique-specific property in any ADA record, so there was nothing to seed one from and none was invented. This registers the procedure skeleton and needs Phase 0 seed papers before it says anything VLM-specific. Generated from draftTAPPs/VLM_TAPP_draft_v2.csv by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.VNMIR.detail` — VNMIR Analysis Detail

**Type:** schema

Detail block for VNMIR hasPart items. Discriminates on ada:componentType and carries the analysis-level properties - viewing geometry, sample state and per-measurement results - that are supplied per measurement rather than fixed by the procedure.

### `ogch.techniqueProfile.geochemProfile.VNMIR.tapp` — VNMIR Technique-Aligned Procedure Profile (vnmirTAPP)

**Type:** schema

Visible, near- and mid-infrared reflectance/emissivity spectroscopy extension of the base TAPP definition. Basic procedure-tier fields are required top-level ada: properties; Advanced procedure-tier fields are schema:additionalProperty[] PropertyValueSpecification entries. VNMIR has no per-element analyte axis, so no ada:analyteTemplate is defined. DRAFT - generated from draftTAPPs/VNMIR_TAPP_draft_v2.csv by tools/build_tapp.py; the source table has not been through Phase 0 review.

### `ogch.techniqueProfile.geochemProfile.XANES.detail` — XANES Analysis Detail

**Type:** schema

Detail block for XANES hasPart items, carrying the analysis-identification properties the Core module places on the dataset. No XANES-specific analysis property is defined yet.

### `ogch.techniqueProfile.geochemProfile.XANES.tapp` — XANES Technique-Aligned Procedure Profile (xanesTAPP)

**Type:** schema

X-ray absorption near edge structure spectroscopy extension of the base TAPP definition. CORE-ONLY DRAFT: the native technique layer is empty. XANES has no ADA detail schema and no technique property in any of its 241 ADA records, so there was nothing to seed one from and none was invented - no beamline energy range, monochromator or dwell time appears here. This registers the procedure skeleton and needs Phase 0 seed papers before it says anything XANES-specific. Generated from draftTAPPs/XANES_TAPP_draft_v2.csv by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.XCT.detail` — Lab-XCT Analysis Detail

**Type:** schema

Laboratory X-ray computed tomography analysis-specific detail properties. Discriminates on ada:componentType (XCTVolume, XCTProjectionImageSet, XCTSegmentationVolume, XCTRenderedImage, XCTQuantitativeTabular), carries analysis-level required properties (analyst, dates, sample, VOI) and per-dataset schema:additionalProperty values referencing the labxctTAPP parameterValues registry.

### `ogch.techniqueProfile.geochemProfile.XCT.tapp` — Lab-XCT Technique-Aligned Protocol Profile (labxctTAPP)

**Type:** schema

Laboratory X-ray computed tomography (polychromatic cone-beam) extension of the base TAPP definition. Adds XCT protocol-level acquisition/processing defaults as top-level ada: properties and an ada:methodParameters vocabulary of session-adjustable parameter templates. XCT has no per-element analyte axis, so no analyteTemplate is defined. Vocabularies and parameter templates ship as separate files under vocab/ and parameterTemplates/.

### `ogch.techniqueProfile.geochemProfile.XRD.detail` — XRD Analysis Detail

**Type:** schema

Detail block for XRD hasPart items, carrying the analysis-level properties supplied per scan rather than fixed by the procedure.

### `ogch.techniqueProfile.geochemProfile.XRD.tapp` — XRD Technique-Aligned Procedure Profile (xrdTAPP)

**Type:** schema

X-ray diffraction extension of the base TAPP definition. XRD reports phases rather than per-element concentrations, so no ada:analyteTemplate is defined; no mode-flag columns, since it delivers a single technique componentType. DRAFT - generated from draftTAPPs/XRD_TAPP_draft_v2.csv by tools/build_tapp.py; the source table has not been through Phase 0 review.

### `ogch.techniqueProfile.geochemProfile.EMPA.profile` — ADA EMPA Product Profile

**Type:** schema

Path-driven ADA product profile for ADA EMPA Product Profile.

### `ogch.techniqueProfile.geochemProfile.LA-MC-ICPMS.profile` — ADA LA-MC-ICP-MS Product Profile

**Type:** schema

Path-driven ADA product profile for ADA LA-MC-ICP-MS Product Profile.

### `ogch.techniqueProfile.geochemProfile.LA-MC-ICPMS-UPb.profile` — ADA LA-MC-ICP-MS U-Pb Geochronology Product Profile

**Type:** schema

Path-driven ADA product profile for ADA LA-MC-ICP-MS U-Pb Geochronology Product Profile.

### `ogch.techniqueProfile.geochemProfile.LA-Q-ICPMS.profile` — ADA LA-Q-ICP-MS Product Profile

**Type:** schema

Path-driven ADA product profile for ADA LA-Q-ICP-MS Product Profile.

### `ogch.techniqueProfile.geochemProfile.LA-Q-ICPMS-UPb.profile` — ADA LA-Q-ICP-MS U-Pb Geochronology Product Profile

**Type:** schema

Path-driven ADA product profile for ADA LA-Q-ICP-MS U-Pb Geochronology Product Profile.

### `ogch.techniqueProfile.geochemProfile.LA-SF-ICPMS.profile` — ADA LA-SF-ICP-MS Product Profile

**Type:** schema

Path-driven ADA product profile for ADA LA-SF-ICP-MS Product Profile.

### `ogch.techniqueProfile.geochemProfile.LA-SF-ICPMS-UPb.profile` — ADA LA-SF-ICP-MS U-Pb Geochronology Product Profile

**Type:** schema

Path-driven ADA product profile for ADA LA-SF-ICP-MS U-Pb Geochronology Product Profile.

### `ogch.techniqueProfile.geochemProfile.QRIS.profile-ada` — ADA QRIS Profile (TAPP-linked)

**Type:** schema

Profile for an ADA metadata document describing Quantitative Reflectance Imaging System products generated under a registered qrisTAPP procedure. Adds the QRIS analysis detail on the schema:Dataset root and pins prov:used to the qrisTAPP definition, on top of the ADA QRIS component-type constraints. DRAFT - the source table has not been through Phase 0 review.

### `ogch.techniqueProfile.geochemProfile.RAMAN.profile-ada` — ADA RAMAN Profile (TAPP-linked)

**Type:** schema

Profile for an ADA metadata document describing Raman vibrational spectroscopy products generated under a registered ramanTAPP procedure. Adds the RAMAN analysis detail on the schema:Dataset root and pins prov:used to the ramanTAPP definition, on top of the ADA RAMAN component-type constraints. DRAFT - the source table has not been through Phase 0 review.

### `ogch.techniqueProfile.geochemProfile.SEM.profile` — ADA SEM (superset) Product Profile

**Type:** schema

Path-driven ADA product profile for ADA SEM (superset) Product Profile.

### `ogch.techniqueProfile.geochemProfile.SEM-Composition.profile` — ADA SEM Composition (EDS/WDS) Product Profile

**Type:** schema

Path-driven ADA product profile for ADA SEM Composition (EDS/WDS) Product Profile.

### `ogch.techniqueProfile.geochemProfile.SEM-FIBSEM.profile` — ADA FIB-SEM Product Profile

**Type:** schema

Path-driven ADA product profile for ADA FIB-SEM Product Profile.

### `ogch.techniqueProfile.geochemProfile.SEM-Imaging.profile` — ADA SEM Imaging Product Profile

**Type:** schema

Path-driven ADA product profile for ADA SEM Imaging Product Profile.

### `ogch.techniqueProfile.geochemProfile.Solution-MC-ICPMS.profile` — ADA Solution MC-ICP-MS Product Profile

**Type:** schema

Path-driven ADA product profile for ADA Solution MC-ICP-MS Product Profile.

### `ogch.techniqueProfile.geochemProfile.Solution-Q-ICPMS.profile` — ADA Solution Q-ICP-MS Product Profile

**Type:** schema

Path-driven ADA product profile for ADA Solution Q-ICP-MS Product Profile.

### `ogch.techniqueProfile.geochemProfile.Solution-SF-ICPMS.profile` — ADA Solution SF-ICP-MS Product Profile

**Type:** schema

Path-driven ADA product profile for ADA Solution SF-ICP-MS Product Profile.

### `ogch.techniqueProfile.geochemProfile.TEM.profile` — ADA TEM Product Profile

**Type:** schema

Path-driven ADA product profile for ADA TEM Product Profile.

### `ogch.techniqueProfile.geochemProfile.VNMIR.profile-ada` — ADA VNMIR Profile (TAPP-linked)

**Type:** schema

Profile for an ADA metadata document describing data generated under a registered vnmirTAPP procedure. Adds the VNMIR analysis detail on the schema:Dataset root and pins prov:used to the vnmirTAPP definition, on top of the ADA VNMIR component-type constraints. DRAFT - the vnmirTAPP source table has not been through Phase 0 review.

### `ogch.techniqueProfile.geochemProfile.XANES.profile-ada` — ADA XANES Profile (TAPP-linked)

**Type:** schema

Profile for an ADA metadata document describing X-ray absorption near edge structure spectroscopy products generated under a registered xanesTAPP procedure. Adds the XANES analysis detail on the schema:Dataset root and pins prov:used to the xanesTAPP definition, on top of the ADA XANES component-type constraints. DRAFT - the source table has not been through Phase 0 review.

### `ogch.techniqueProfile.geochemProfile.XCT.profile` — ADA Lab-XCT Product Profile

**Type:** schema

Path-driven ADA product profile for ADA Lab-XCT Product Profile.

### `ogch.techniqueProfile.geochemProfile.XRD.profile-ada` — ADA XRD Profile (TAPP-linked)

**Type:** schema

Profile for an ADA metadata document describing X-ray diffraction products generated under a registered xrdTAPP procedure. Adds the XRD analysis detail on the schema:Dataset root and pins prov:used to the xrdTAPP definition, on top of the ADA XRD component-type constraints. DRAFT - the source table has not been through Phase 0 review.

