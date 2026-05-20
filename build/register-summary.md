# ADA Geochemistry Building Blocks repository

Building blocks for Astromat Data Archive (ADA) geochemistry metadata profiles,
using the OGC Building Blocks pattern.


Modular schema components for ADA analytical technique metadata. Imports shared
schema.org and CDIF property building blocks from the CDIF Building Blocks repository.


## Building Blocks

### `ogch.analysisSpecificDetails.detailARGT` — ARGT Instrument Detail

**Type:** schema

ARGT (Argon) document type with phase and isotope analysis. Defines properties: @type, phaseAnalyzed, isotopeType.

### `ogch.analysisSpecificDetails.detailBasemap` — Basemap Instrument Detail

**Type:** schema

Basemap images with RGB channels and pixel scaling. Defines properties: @type, schema:description, pixelUnits, pixelScaleX, pixelScaleY, channel1, channel2, channel3.

### `ogch.analysisSpecificDetails.detailDSC` — DSC Instrument Detail

**Type:** schema

Differential Scanning Calorimetry heat tabular data. Defines properties: @type, analysisType.

### `ogch.analysisSpecificDetails.detailEAIRMS` — EA-IRMS Instrument Detail

**Type:** schema

Elemental Analysis Isotope Ratio Mass Spectrometry collection. Defines properties: @type, massConsumed, elementType.

### `ogch.techniqueProtocols.parameterValues` — Analytical Parameter Value Registry

**Type:** schema

Registry of reusable schema:PropertyValue parameter-value definitions derived from technique TAPP spreadsheets. Hosts one $def per per-dataset parameter value (e.g. acceleratingVoltage, beamDiameter, BeamRasterDimension, reportedAnalyte). Detail building blocks reference these definitions via fragment $refs so they resolve locally through the register.

### `ogch.analysisSpecificDetails.detailICPOES` — ICP-OES Instrument Detail

**Type:** schema

Inductively Coupled Plasma Optical Emission Spectrometry detail properties. Defines properties: @type, mass, dissolutionFactor.

### `ogch.analysisSpecificDetails.detailL2MS` — L2MS Instrument Detail

**Type:** schema

Laser-2 Mass Spectrometry cube data with ionization parameters. Defines properties: @type, sampleName, ionizationTimeDelay, massGate, photoionizationWavelength, plasmaShutter, timeDelayUnits, wavelengthUnits.

### `ogch.analysisSpecificDetails.detailLAF` — LAF Instrument Detail

**Type:** schema

Laser Ablation Fluorescence processed/raw data detail properties. Defines properties: @type, elementAnalyzed, sampleMassConsumed, sampleType.

### `ogch.geochemProperties.stringArray` — String Array Type

**Type:** schema

Simple reusable array of strings used throughout ADA metadata. Defines type: array of strings.

### `ogch.analysisSpecificDetails.detailQRIS` — QRIS Instrument Detail

**Type:** schema

QRIS (Raman) with calibration and illumination parameters. Defines properties: @type, calibrationFile, pipelineVersion, focalLength, illuminationColor, illuminationLevel, exposureTime, target.

### `ogch.analysisSpecificDetails.detailSLS` — SLS Instrument Detail

**Type:** schema

Structured Light Scanning shape models and partial scans. Defines properties: @type, countScans, facets, unitsOfMeasurement, version, vertices, watertight.

### `ogch.analysisSpecificDetails.detailVNMIR` — VNMIR Instrument Detail

**Type:** schema

Very-Near Mid-IR spectroscopy with detailed measurement parameters. Defines properties: @type, detector, beamsplitter, calibrationStandards, comments, numberOfScans, eMaxFitRegionMax, eMaxFitRegionMin, emissionAngle, emissivityMaximum, environmentalPressure, incidenceAngle, measurement, measurementEnvironment, phaseAngle, sampleHeated, samplePreparation, sampleTemperature, spectralRangeMax, spectralRangeMin, spectralResolution, spectralSampling, spotSize, uncertaintyNoise, vacuumExposedSample.

### `ogch.analysisSpecificDetails.detailXCT` — XCT Instrument Detail

**Type:** schema

X-ray Computed Tomography images with detailed scan parameters. Defines properties: @type, beamFilterMaterial, beamFilterThickness, dataRangeLower, dataRangeUpper, detectorGain, detectorBinning, detectorSize, detectorType, imageExposure, imageFPS, imageGain, imageSize, instrumentType, nsiBeamHardening, numberOfFramesAveragedPerProjection, numberOfProjections, numberOfSlices, pixelPitch, reconstructedDataFormat, reconstructedVoxelSize, reconstructionSoftware, rotationAngle, rotationType, sourceToDetectorDistance, sourceToObjectDistance, subPixGrid, subPixShift, xraySource, xrayTargetMaterial, xrayTubeCurrent, xrayTubeEnergy, xrayTubePower.

### `ogch.analysisSpecificDetails.detailXRD` — XRD Instrument Detail

**Type:** schema

X-ray Diffraction tabular data with geometry and wavelength. Defines properties: @type, geometry, sampleMount, stepSize, timePerStep, wavelength.

### `ogch.geochemProperties.creativeWork` — Creative Work Type

**Type:** schema

Shell type for labeled links to creative works (schema:CreativeWork). Defines properties: @type, schema:name, schema:description, schema:url.

### `ogch.geochemProperties.document` — Document Type

**Type:** schema

Supplemental documents for calibration, methods, and analysis info. Defines properties: @type, componentType, schema:version, schema:isBasedOn. Uses building blocks: detailARGT (geochemProperties).

### `ogch.geochemProperties.image` — Image Type

**Type:** schema

ADA image with componentType classification for analytical images. Defines properties: @type, acquisitionTime, componentType, channel1, channel2, channel3, pixelSize, illuminationType, imageType.

### `ogch.geochemProperties.otherFile` — Other File Type

**Type:** schema

Non-standard file formats approved for ADA submission. Defines properties: @type, componentType, schema:encodingFormat, formatDescription. Uses building blocks: detailSLS (geochemProperties).

### `ogch.geochemProperties.supDocImage` — Supplemental Document Image Type

**Type:** schema

Supplemental document images including analysis locations and context photos. Defines properties: @type, componentType, numPixelsX, numPixelsY, schema:isBasedOn.

### `ogch.geochemProperties.spatialRegistration` — Spatial Registration Type

**Type:** schema

Pixel coordinate system registration for images and maps. Defines properties: basemap, originX, originY, originZ, coordDef, coordUnits, pixelUnits, pixelScaleX, pixelScaleY, originLocation.

### `ogch.techniqueProtocols.analyteColumns` — Analyte-Column Specification Registry

**Type:** schema

Registry of reusable schema:PropertyValueSpecification analyte-column definitions derived from technique TAPP spreadsheets. Hosts one $def per analyte-table reporting column. TAPP building blocks reference these definitions via fragment $refs so they resolve locally through the register.

### `ogch.techniqueProtocols.parameterTemplates` — Method-Parameter Template Registry

**Type:** schema

Registry of reusable schema:PropertyValueSpecification method-parameter template definitions derived from technique TAPP spreadsheets. Hosts one $def per method-level parameter template. TAPP building blocks reference these definitions via fragment $refs so they resolve locally through the register.

### `ogch.analysisSpecificDetails.detailEMPA` — EMPA Instrument Detail

**Type:** schema

Electron Microprobe Analysis instrument-specific detail properties. Defines properties: @type, spectrometersUsed, signalUsed.

### `ogch.analysisSpecificDetails.detailNanoIR` — NanoIR Instrument Detail

**Type:** schema

Nano-IR spectroscopy collections with phase analysis. Defines properties: @type, phaseAnalyzed. Uses building blocks: stringArray (geochemProperties).

### `ogch.analysisSpecificDetails.detailNanoSIMS` — NanoSIMS Instrument Detail

**Type:** schema

Nano Secondary Ion Mass Spectrometry with isotope tracking. Defines properties: @type, phaseAnalyzed, isotopeAnalyzed. Uses building blocks: stringArray (geochemProperties).

### `ogch.analysisSpecificDetails.detailPSFD` — PSFD Instrument Detail

**Type:** schema

Point Spread Function Data with image names and conditions. Defines properties: @type, imageName, imageViewingConditions. Uses building blocks: stringArray (geochemProperties).

### `ogch.geochemProperties.collection` — Collection Type

**Type:** schema

Set of related files with identical information models or composite datasets. Defines properties: @type, componentType, memberTypes, nFiles, filelist. Uses building blocks: stringArray (geochemProperties).

### `ogch.geochemProperties.imageMap` — Image Map Type

**Type:** schema

Spatially registered image map with pixel coordinates and component types. Defines properties: @type, acquisitionTime, componentType, channel1, channel2, channel3, illuminationType, imageType, numPixelsX, numPixelsY, spatialRegistration. Uses building blocks: detailEMPA (geochemProperties), spatialRegistration (geochemProperties).

### `ogch.geochemProperties.dataCube` — Data Cube Type

**Type:** schema

CDI DimensionalDataStructure for multidimensional data. Defines properties: @type, componentType, dataComponentResource. Uses building blocks: detailL2MS (geochemProperties), cdifDataCube (cdifProperties).

### `ogch.geochemProperties.tabularData` — Tabular Data Type

**Type:** schema

CDI PhysicalDataSet for tabular/structured data files. Defines properties: @type, componentType, xCoordCol, yCoordCol, zCoordCol, coordUnits, spatialRegistration. Uses building blocks: detailDSC (geochemProperties), detailEAIRMS (geochemProperties), detailEMPA (geochemProperties), detailLAF (geochemProperties), detailNanoSIMS (geochemProperties), detailNanoIR (geochemProperties), detailPSFD (geochemProperties), detailVNMIR (geochemProperties), detailXRD (geochemProperties), spatialRegistration (geochemProperties), cdifTabularData (cdifProperties).

### `ogch.geochemProperties.laboratory` — ADA Analysis Laboratory

**Type:** schema

ADA laboratory/facility building block extending core CDIF spatialExtent (schema:Place). Adds nxs:BaseClass/NXsource classification via additionalType. Inherits place name, identifier, alternateName, geo coordinates from core.

### `ogch.geochemProperties.files` — Files Type

**Type:** schema

DataDownload with checksum, size, encoding format, and file detail. Defines properties: schema:additionalType, schema:description, schema:size, resultTarget, schema:relatedLink. Uses building blocks: dataDownload (schemaorgProperties), stringArray (geochemProperties), image (geochemProperties), imageMap (geochemProperties), tabularData (geochemProperties), collection (geochemProperties), dataCube (geochemProperties), document (geochemProperties), supDocImage (geochemProperties), otherFile (geochemProperties).

### `ogch.geochemProperties.instrument` — ADA Analysis Instrument

**Type:** schema

ADA analytical instrument extending the core CDIF instrument building block. Typed as schema:Thing + schema:Product with domain-specific classifications (e.g. nxs:BaseClass/NXinstrument) in schema:additionalType. Inherits hierarchical sub-components, manufacturer, model, calibration properties from core.

### `ogch.techniqueProtocols.tappDefinition` — Technique-Aligned Protocol Profile (TAPP) Definition

**Type:** schema

A registered Technique-Aligned Protocol Profile (TAPP) definition modeled as cdi:Activity + schema:Action + ada:TAPPDefinition + bios:LabProtocol. TAPP identity (name, technique, instrument, location, target material) at top level. Standard workflow encoded in schema:actionProcess as a schema:HowTo with ordered cdi:Activity + schema:Action steps. Each workflow step carries its own parameters, reagents, instruments. Uses bios:computationalTool for software, bios:reagent for reference materials, dqv:hasQualityMeasurement for quality metrics, ada:fieldScope (method/session/element) for parameter lifecycle.

### `ogch.profiles.adaProfiles.adaProduct` — ADA Product Profile

**Type:** schema

Top-level ADA product metadata profile composing all ADA building blocks

### `ogch.techniqueProtocols.empaTAPP` — EMPA Technique-Aligned Protocol Profile (empaTAPP)

**Type:** schema

EMPA-specific extension of the base TAPP definition. Adds EPMA top-level properties (beam mode, accelerating voltage, matrix correction method), a parameter vocabulary, and an analyte-column template covering EPMA per-element acquisition and reporting fields. Vocabularies, parameter templates, and analyte-column templates ship as separate JSON files under vocab/, parameters/, and analyteColumns/ for maintainability.

### `ogch.techniqueProtocols.laicpmsTAPP` — LA-ICPMS Technique-Aligned Protocol Profile (laicpmsTAPP)

**Type:** schema

LA-ICPMS-specific extension of the base TAPP definition. Adds laser-ablation top-level properties (spot geometry, ablation mode, laser fluence, ablation spot duration), a parameter vocabulary, and an analyte-column template covering LA-ICPMS per-element acquisition and reporting fields (detection limits, reproducibility, isobaric interference corrections). Vocabularies, parameter templates, and analyte-column templates ship as separate JSON files under the shared vocab/, parameterTemplates/, and analyteColumns/ catalogs for maintainability.

### `ogch.profiles.adaProfiles.adaAIVA` — ADA AIVA Profile

**Type:** schema

Technique-specific profile for AI-driven Visual Analysis (AIVA) products

### `ogch.profiles.adaProfiles.adaAMS` — ADA AMS Profile

**Type:** schema

Technique-specific profile for Accelerator Mass Spectrometry (AMS) products

### `ogch.profiles.adaProfiles.adaARGT` — ADA ARGT Profile

**Type:** schema

Technique-specific profile for Argon Geochronology and Thermochronology (ARGT) products

### `ogch.profiles.adaProfiles.adaDSC` — ADA DSC Profile

**Type:** schema

Technique-specific profile for Differential Scanning Calorimetry (DSC) products

### `ogch.profiles.adaProfiles.adaEAIRMS` — ADA EA-IRMS Profile

**Type:** schema

Technique-specific profile for Elemental Analysis - Isotope Ratio Mass Spectrometry (EA-IRMS) products

### `ogch.profiles.adaProfiles.adaEMPA` — ADA EMPA Profile

**Type:** schema

Technique-specific profile for Electron Microprobe Analysis (EMPA) products

### `ogch.profiles.adaProfiles.adaFTICRMS` — ADA FTICR-MS Profile

**Type:** schema

Technique-specific profile for Fourier Transform Ion Cyclotron Resonance Mass Spectrometry (FTICR-MS) products

### `ogch.profiles.adaProfiles.adaGCMS` — ADA GC-MS Profile

**Type:** schema

Technique-specific profile for Gas Chromatography Mass Spectrometry (GC-MS) products

### `ogch.profiles.adaProfiles.adaGPYC` — ADA GPYC Profile

**Type:** schema

Technique-specific profile for Gas Pycnometry (GPYC) products

### `ogch.profiles.adaProfiles.adaIC` — ADA IC Profile

**Type:** schema

Technique-specific profile for Ion Chromatography (IC) products

### `ogch.profiles.adaProfiles.adaICPMS` — ADA ICP-MS Profile

**Type:** schema

Technique-specific profile for Inductively Coupled Plasma Mass Spectrometry (ICP-MS) products

### `ogch.profiles.adaProfiles.adaICPOES` — ADA ICP-OES Profile

**Type:** schema

Technique-specific profile for Inductively Coupled Plasma Optical Emission Spectrometry (ICP-OES) products

### `ogch.profiles.adaProfiles.adaL2MS` — ADA L2MS Profile

**Type:** schema

Technique-specific profile for Two-Step Laser Mass Spectrometry (L2MS) products

### `ogch.profiles.adaProfiles.adaLAF` — ADA LAF Profile

**Type:** schema

Technique-specific profile for Laser-Assisted Fluorination (LAF) products

### `ogch.profiles.adaProfiles.adaLCMS` — ADA LC-MS Profile

**Type:** schema

Technique-specific profile for Liquid Chromatography Mass Spectrometry (LC-MS) products

### `ogch.profiles.adaProfiles.adaLIT` — ADA LIT Profile

**Type:** schema

Technique-specific profile for Lock-In Thermography (LIT) products

### `ogch.profiles.adaProfiles.adaNGNSMS` — ADA NG-NS-MS Profile

**Type:** schema

Technique-specific profile for Noble Gas and Nitrogen Static Mass Spectrometry (NG-NS-MS) products

### `ogch.profiles.adaProfiles.adaNanoIR` — ADA NanoIR Profile

**Type:** schema

Technique-specific profile for Nano-Infrared Spectroscopy (NanoIR) products

### `ogch.profiles.adaProfiles.adaNanoSIMS` — ADA NanoSIMS Profile

**Type:** schema

Technique-specific profile for Nanoscale Secondary Ion Mass Spectrometry (NanoSIMS) products

### `ogch.profiles.adaProfiles.adaPSFD` — ADA PSFD Profile

**Type:** schema

Technique-specific profile for Particle Size-Frequency Distribution (PSFD) products

### `ogch.profiles.adaProfiles.adaQRIS` — ADA QRIS Profile

**Type:** schema

Technique-specific profile for Quantitative Reflectance Imaging Spectroscopy (QRIS) products

### `ogch.profiles.adaProfiles.adaRAMAN` — ADA RAMAN Profile

**Type:** schema

Technique-specific profile for Raman Spectroscopy (RAMAN) products

### `ogch.profiles.adaProfiles.adaRITOFNGMS` — ADA RI-TOF-NGMS Profile

**Type:** schema

Technique-specific profile for Resonance Ionization Time-of-Flight Noble Gas Mass Spectrometry (RI-TOF-NGMS) products

### `ogch.profiles.adaProfiles.adaSEM` — ADA SEM Profile

**Type:** schema

Technique-specific profile for Scanning Electron Microscopy (SEM) products

### `ogch.profiles.adaProfiles.adaSIMS` — ADA SIMS Profile

**Type:** schema

Technique-specific profile for Secondary Ion Mass Spectrometry (SIMS) products

### `ogch.profiles.adaProfiles.adaSLS` — ADA SLS Profile

**Type:** schema

Technique-specific profile for Structured Light Scanning (SLS) products

### `ogch.profiles.adaProfiles.adaSVRUEC` — ADA SV-RUEC Profile

**Type:** schema

Technique-specific profile for Seismic Velocities and Rock Ultrasonic Elastic Constants (SV-RUEC) products

### `ogch.profiles.adaProfiles.adaTEM` — ADA TEM Profile

**Type:** schema

Technique-specific profile for Transmission Electron Microscopy (TEM) products

### `ogch.profiles.adaProfiles.adaToFSIMS` — ADA ToF-SIMS Profile

**Type:** schema

Technique-specific profile for Time-of-Flight Secondary Ion Mass Spectrometry (ToF-SIMS) products

### `ogch.profiles.adaProfiles.adaUVFM` — ADA UVFM Profile

**Type:** schema

Technique-specific profile for Ultraviolet Fluorescence Microscopy (UVFM) products

### `ogch.profiles.adaProfiles.adaVLM` — ADA VLM Profile

**Type:** schema

Technique-specific profile for Visible Light Microscopy (VLM) products

### `ogch.profiles.adaProfiles.adaVNMIR` — ADA VNMIR Profile

**Type:** schema

Technique-specific profile for Very-Near Mid-Infrared (VNMIR/FTIR) spectroscopy products

### `ogch.profiles.adaProfiles.adaXANES` — ADA XANES Profile

**Type:** schema

Technique-specific profile for X-ray Absorption Near Edge Structure (XANES) products

### `ogch.profiles.adaProfiles.adaXCT` — ADA XCT Profile

**Type:** schema

Technique-specific profile for X-ray Computed Tomography (XCT) products

### `ogch.profiles.adaProfiles.adaXRD` — ADA XRD Profile

**Type:** schema

Technique-specific profile for X-ray Diffraction (XRD) products

### `ogch.profiles.geochemProfiles.empaProfile` — EMPA Geochem Profile

**Type:** schema

Technique-specific dataset profile for EMPA. Extends adaProduct with constraints on schema:measurementTechnique (pointing at empaTAPP) and schema:distribution.schema:hasPart (allowing detailEMPA entries).

### `ogch.profiles.geochemProfiles.LA-ICPMS` — ADA ICP-MS Profile

**Type:** schema

Technique-specific profile for Inductively Coupled Plasma Mass Spectrometry (ICP-MS) products

