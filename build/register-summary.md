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

### `ogch.BaseSchema.supDocImage` — Supplemental Document Image Type

**Type:** schema

Supplemental document images including analysis locations and context photos. Defines properties: @type, componentType, numPixelsX, numPixelsY, schema:isBasedOn.

### `ogch.BaseSchema.image` — Image Type

**Type:** schema

ADA image with componentType classification for analytical images. Defines properties: @type, acquisitionTime, componentType, channel1, channel2, channel3, pixelSize, illuminationType, imageType.

### `ogch.BaseSchema.otherFile` — Other File Type

**Type:** schema

Non-standard file formats approved for ADA submission. Defines properties: @type, componentType, schema:encodingFormat, formatDescription. Uses building blocks: detailSLS (geochemProperties).

### `ogch.BaseSchema.spatialRegistration` — Spatial Registration Type

**Type:** schema

Pixel coordinate system registration for images and maps. Defines properties: basemap, originX, originY, originZ, coordDef, coordUnits, pixelUnits, pixelScaleX, pixelScaleY, originLocation.

### `ogch.BaseSchema.modules.geochronology` — TAPP Composition Module: Geochronology

**Type:** schema

The shared Geochronology block of the 2026-08-11 TAPP library, composed by 3 of the sixteen delivery tables. 6 owned fields over 3 schema paths, split into the procedure and analysis halves a TAPP schema and a technique detail compose respectively. A profile over existing tappDefinition/adaProduct properties, not a new vocabulary. Generated from the module CSV and its schema-path sidecar.

### `ogch.BaseSchema.modules.group1` — TAPP Composition Module: Group1

**Type:** schema

The shared Group1 block of the 2026-08-11 TAPP library, composed by 16 of the sixteen delivery tables. 18 owned fields over 22 schema paths, split into the procedure and analysis halves a TAPP schema and a technique detail compose respectively. A profile over existing tappDefinition/adaProduct properties, not a new vocabulary. Generated from the module CSV and its schema-path sidecar.

### `ogch.BaseSchema.modules.mcIcpms` — TAPP Composition Module: MCICPMS

**Type:** schema

The shared MCICPMS block of the 2026-08-11 TAPP library, composed by 3 of the sixteen delivery tables. 15 owned fields over 3 schema paths, split into the procedure and analysis halves a TAPP schema and a technique detail compose respectively. A profile over existing tappDefinition/adaProduct properties, not a new vocabulary. Generated from the module CSV and its schema-path sidecar.

### `ogch.BaseSchema.modules.reportingCore` — TAPP Composition Module: ReportingCore

**Type:** schema

The shared ReportingCore block of the 2026-08-11 TAPP library, composed by 16 of the sixteen delivery tables. 6 owned fields over 3 schema paths, split into the procedure and analysis halves a TAPP schema and a technique detail compose respectively. A profile over existing tappDefinition/adaProduct properties, not a new vocabulary. Generated from the module CSV and its schema-path sidecar.

### `ogch.BaseSchema.modules.solutionIntroduction` — TAPP Composition Module: SolutionIntroduction

**Type:** schema

The shared SolutionIntroduction block of the 2026-08-11 TAPP library, composed by 3 of the sixteen delivery tables. 16 owned fields over 21 schema paths, split into the procedure and analysis halves a TAPP schema and a technique detail compose respectively. A profile over existing tappDefinition/adaProduct properties, not a new vocabulary. Generated from the module CSV and its schema-path sidecar.

### `ogch.BaseSchema.modules.uPb` — TAPP Composition Module: UPb

**Type:** schema

The shared UPb block of the 2026-08-11 TAPP library, composed by 3 of the sixteen delivery tables. 3 owned fields over 3 schema paths, split into the procedure and analysis halves a TAPP schema and a technique detail compose respectively. A profile over existing tappDefinition/adaProduct properties, not a new vocabulary. Generated from the module CSV and its schema-path sidecar.

### `ogch.registry.analyteColumns` — Analyte-Column Specification Registry

**Type:** schema

Registry of reusable schema:PropertyValueSpecification analyte-column definitions derived from technique TAPP spreadsheets. Hosts one $def per analyte-table reporting column. TAPP building blocks reference these definitions via fragment $refs so they resolve locally through the register.

### `ogch.registry.parameterTemplates` — Method-Parameter Template Registry

**Type:** schema

Registry of reusable schema:PropertyValueSpecification method-parameter template definitions derived from technique TAPP spreadsheets. Hosts one $def per method-level parameter template. TAPP building blocks reference these definitions via fragment $refs so they resolve locally through the register.

### `ogch.registry.parameterValues` — Analytical Parameter Value Registry

**Type:** schema

Registry of reusable schema:PropertyValue parameter-value definitions derived from technique TAPP spreadsheets. Hosts one $def per per-dataset parameter value (e.g. acceleratingVoltage, beamDiameter, BeamRasterDimension, reportedAnalyte). Detail building blocks reference these definitions via fragment $refs so they resolve locally through the register.

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

### `ogch.BaseSchema.structuredData` — Structured Data File Type

**Type:** schema

A container/array data file (HDF5, NeXus) in an ADA bundle whose layout is described by a CDIF DataStructure via cdi:isStructuredBy. The bundle-part analog of the monolithic single-file isStructuredBy pattern (pattern chosen by encoding, not position). Defines properties: @type, ada:componentType, cdi:isStructuredBy. Uses building blocks: cdifDataStructure (cdifProperties).

### `ogch.BaseSchema.instrument` — ADA Analysis Instrument

**Type:** schema

ADA analytical instrument extending the core CDIF instrument building block. Typed as schema:Thing + schema:Product with domain-specific classifications (e.g. nxs:BaseClass/NXinstrument) in schema:additionalType. Inherits hierarchical sub-components, manufacturer, model, calibration properties from core.

### `ogch.BaseSchema.files` — Files Type

**Type:** schema

DataDownload with checksum, size, encoding format, and file detail. Defines properties: schema:additionalType, schema:description, schema:size, resultTarget, schema:relatedLink. Uses building blocks: dataDownload (schemaorgProperties), stringArray (geochemProperties), image (geochemProperties), imageMap (geochemProperties), tabularData (geochemProperties), collection (geochemProperties), dataCube (geochemProperties), document (geochemProperties), supDocImage (geochemProperties), otherFile (geochemProperties).

### `ogch.BaseSchema.modules.laserAblation` — TAPP Composition Module: LaserAblation

**Type:** schema

The shared LaserAblation block of the 2026-08-11 TAPP library, composed by 6 of the sixteen delivery tables. 18 owned fields over 17 schema paths, split into the procedure and analysis halves a TAPP schema and a technique detail compose respectively. A profile over existing tappDefinition/adaProduct properties, not a new vocabulary. Generated from the module CSV and its schema-path sidecar.

### `ogch.BaseSchema.tappDefinition` — Technique-Aligned Protocol Profile (TAPP) Definition

**Type:** schema

A registered Technique-Aligned Protocol Profile (TAPP) definition modeled as cdi:Activity + schema:Action + ada:TAPPDefinition + bios:LabProtocol. TAPP identity (name, technique, instrument, location, target material) at top level. Standard workflow encoded in schema:actionProcess as a schema:HowTo with ordered cdi:Activity + schema:Action steps. Each workflow step carries its own parameters, reagents, instruments. Uses bios:computationalTool for software, bios:reagent for reference materials, dqv:hasQualityMeasurement for quality metrics, ada:fieldScope (method/session/element) for parameter lifecycle.

### `ogch.BaseSchema.geochemProduct` — Geochem Analytical Product

**Type:** schema

Generic geochemistry analytical product metadata base: composes the CDIF core, data-description, manifest, and provenance profiles with the analytical surface (analysis events, variables measured, distributions, coverage). Extended by archive-specific delivery profiles such as adaProduct.

### `ogch.techniqueProfile.geochemProfile.EMPA.tapp` — EMPA Technique-Aligned Protocol Profile (empaTAPP)

**Type:** schema

EMPA-specific extension of the base TAPP definition. Adds EPMA top-level properties (beam mode, accelerating voltage, matrix correction method), a parameter vocabulary, and an analyte-column template covering EPMA per-element acquisition and reporting fields. Vocabularies, parameter templates, and analyte-column templates ship as separate JSON files under vocab/, parameters/, and analyteColumns/ for maintainability.

### `ogch.techniqueProfile.geochemProfile.LA-MC-ICPMS.tapp` — LA-MC-ICP-MS Technique-Aligned Procedure Profile (laMcicpmsTAPP)

**Type:** schema

Laser-ablation multi-collector ICP-MS extension of the base TAPP definition, generated from TAPPS20260813/Current TAPPs/LA-MC-ICPMS_TAPP_v13.csv via the path-driven pipeline.

### `ogch.techniqueProfile.geochemProfile.LA-MC-ICPMS-UPb.tapp` — LA-MC-ICP-MS U-Pb Geochronology TAPP (laMcicpmsUPbTAPP)

**Type:** schema

Laser-ablation multi-collector ICP-MS U-Pb geochronology extension of the base TAPP definition, generated from TAPPS20260813/Current TAPPs/LA-MC-ICPMS_UPb_TAPP_v13.csv via the path-driven pipeline.

### `ogch.techniqueProfile.geochemProfile.LA-Q-ICPMS.tapp` — LA-Q-ICP-MS Technique-Aligned Procedure Profile (laQicpmsTAPP)

**Type:** schema

Laser-ablation quadrupole ICP-MS extension of the base TAPP definition, generated from TAPPS20260813/Current TAPPs/LA-Q-ICP-MS_TAPP_v15.csv via the path-driven pipeline (bootstrap_schemapaths.py + build_pathdriven.py).

### `ogch.techniqueProfile.geochemProfile.LA-Q-ICPMS-UPb.tapp` — LA-Q-ICP-MS U-Pb Geochronology TAPP (laQicpmsUPbTAPP)

**Type:** schema

Laser-ablation quadrupole ICP-MS U-Pb geochronology extension of the base TAPP definition, generated from TAPPS20260813/Current TAPPs/LA-Q-ICP-MS_UPb_TAPP_v16.csv via the path-driven pipeline.

### `ogch.techniqueProfile.geochemProfile.LA-SF-ICPMS.tapp` — LA-SF-ICP-MS Technique-Aligned Procedure Profile (laSficpmsTAPP)

**Type:** schema

Laser-ablation sector-field (high-resolution) ICP-MS extension of the base TAPP definition, generated from TAPPS20260813/Current TAPPs/LA-SF-ICP-MS_TAPP_v16.csv via the path-driven pipeline.

### `ogch.techniqueProfile.geochemProfile.LA-SF-ICPMS-UPb.tapp` — LA-SF-ICP-MS U-Pb Geochronology TAPP (laSficpmsUPbTAPP)

**Type:** schema

Laser-ablation sector-field ICP-MS U-Pb geochronology extension of the base TAPP definition, generated from TAPPS20260813/Current TAPPs/LA-SF-ICP-MS_UPb_TAPP_v17.csv via the path-driven pipeline.

### `ogch.techniqueProfile.geochemProfile.SEM.tapp` — SEM Technique-Aligned Protocol Profile (semTAPP)

**Type:** schema

Scanning electron microscopy superset (imaging + EDS/WDS composition + EBSD + FIB-SEM) extension of the base TAPP definition, generated from docs/SEM_TAPP_v4.xlsx via the path-driven pipeline.

### `ogch.techniqueProfile.geochemProfile.SEM-Composition.tapp` — SEM Composition (EDS/WDS) Technique-Aligned Protocol Profile (semCompositionTAPP)

**Type:** schema

Scanning electron microscopy compositional microanalysis (EDS/WDS) extension of the base TAPP definition, generated from docs/SEM_Composition_TAPP_v4.xlsx via the path-driven pipeline (bootstrap_schemapaths.py + build_pathdriven.py).

### `ogch.techniqueProfile.geochemProfile.SEM-FIBSEM.tapp` — FIB-SEM Technique-Aligned Protocol Profile (semFibsemTAPP)

**Type:** schema

Focused-ion-beam SEM (FIB-SEM tomography, TEM lamella prep) extension of the base TAPP definition. Basic protocol-tier fields are required top-level ada: properties; Advanced protocol-tier fields are schema:additionalProperty[] entries. No ada:analyteTemplate. Generated from docs/SEM_FIBSEM_TAPP_v4.xlsx by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.SEM-Imaging.tapp` — SEM Imaging Technique-Aligned Protocol Profile (semImagingTAPP)

**Type:** schema

Scanning electron microscopy imaging (SE/BSE/CL/EBSD) extension of the base TAPP definition. Basic protocol-tier fields are required top-level ada: properties; Advanced protocol-tier fields are schema:additionalProperty[] entries. No ada:analyteTemplate (imaging has no per-element analyte axis). Generated from docs/SEM_Imaging_TAPP_v4.xlsx by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.Solution-MC-ICPMS.tapp` — Solution MC-ICP-MS Technique-Aligned Procedure Profile (solutionMcicpmsTAPP)

**Type:** schema

Solution multi-collector ICP-MS extension of the base TAPP definition, generated from TAPPS20260813/Current TAPPs/Solution_MC-ICP-MS_TAPP_v16.csv via the path-driven pipeline.

### `ogch.techniqueProfile.geochemProfile.Solution-Q-ICPMS.tapp` — Solution Q-ICP-MS Technique-Aligned Protocol Profile (solutionQicpmsTAPP)

**Type:** schema

Solution quadrupole ICP-MS extension of the base TAPP definition, generated from docs/Solution_Q-ICP-MS_TAPP_v5.xlsx via the path-driven pipeline.

### `ogch.techniqueProfile.geochemProfile.Solution-SF-ICPMS.tapp` — Solution SF-ICP-MS Technique-Aligned Protocol Profile (solutionSficpmsTAPP)

**Type:** schema

Solution sector-field (high-resolution) ICP-MS extension of the base TAPP definition, generated from docs/Solution_SF-ICP-MS_TAPP_v5.xlsx via the path-driven pipeline.

### `ogch.techniqueProfile.geochemProfile.TEM.tapp` — TEM Technique-Aligned Protocol Profile (temTAPP)

**Type:** schema

Transmission electron microscopy (TEM/STEM, incl. EDS/EELS) extension of the base TAPP definition. Basic protocol-tier fields are required top-level ada: properties; Advanced protocol-tier fields are schema:additionalProperty[] entries; an ada:analyteTemplate carries per-element columns. Generated from docs/TEM_TAPP_v7.xlsx by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.XCT.tapp` — Lab-XCT Technique-Aligned Protocol Profile (labxctTAPP)

**Type:** schema

Laboratory X-ray computed tomography (polychromatic cone-beam) extension of the base TAPP definition. Adds XCT protocol-level acquisition/processing defaults as top-level ada: properties and an ada:methodParameters vocabulary of session-adjustable parameter templates. XCT has no per-element analyte axis, so no analyteTemplate is defined. Vocabularies and parameter templates ship as separate files under vocab/ and parameterTemplates/.

### `ogch.BaseSchema.adaProduct` — ADA Product Profile

**Type:** schema

Top-level ADA product metadata profile composing all ADA building blocks

### `ogch.techniqueProfile.geochemProfile.EMPA.detail` — EMPA Instrument Detail

**Type:** schema

Electron Microprobe Analysis instrument-specific detail properties. Defines properties: @type, spectrometersUsed, signalUsed.

### `ogch.techniqueProfile.geochemProfile.LA-MC-ICPMS.detail` — LA-MC-ICP-MS Analysis Detail

**Type:** schema

Dataset-level analysis-instance detail for LA-MC-ICP-MS, reusing CDIF/schema.org slots on the schema:Dataset root.

### `ogch.techniqueProfile.geochemProfile.LA-MC-ICPMS-UPb.detail` — LA-MC-ICP-MS U-Pb Analysis Detail

**Type:** schema

Dataset-level analysis-instance detail for LA-MC-ICP-MS U-Pb geochronology, reusing CDIF/schema.org slots on the schema:Dataset root.

### `ogch.techniqueProfile.geochemProfile.LA-Q-ICPMS.detail` — LA-Q-ICP-MS Analysis Detail

**Type:** schema

Dataset-level analysis-instance detail for LA-Q-ICP-MS, reusing CDIF/schema.org slots on the schema:Dataset root.

### `ogch.techniqueProfile.geochemProfile.LA-Q-ICPMS-UPb.detail` — LA-Q-ICP-MS U-Pb Analysis Detail

**Type:** schema

Dataset-level analysis-instance detail for LA-Q-ICP-MS U-Pb geochronology, reusing CDIF/schema.org slots on the schema:Dataset root.

### `ogch.techniqueProfile.geochemProfile.LA-SF-ICPMS.detail` — LA-SF-ICP-MS Analysis Detail

**Type:** schema

Dataset-level analysis-instance detail for LA-SF-ICP-MS, reusing CDIF/schema.org slots on the schema:Dataset root.

### `ogch.techniqueProfile.geochemProfile.LA-SF-ICPMS-UPb.detail` — LA-SF-ICP-MS U-Pb Analysis Detail

**Type:** schema

Dataset-level analysis-instance detail for LA-SF-ICP-MS U-Pb geochronology, reusing CDIF/schema.org slots on the schema:Dataset root.

### `ogch.techniqueProfile.geochemProfile.SEM.detail` — SEM Analysis Detail

**Type:** schema

Dataset-level analysis-instance detail for SEM (superset), reusing CDIF/schema.org slots on the schema:Dataset root.

### `ogch.techniqueProfile.geochemProfile.SEM-Composition.detail` — SEM Composition Analysis Detail

**Type:** schema

Dataset-level analysis-instance detail for SEM composition (EDS/WDS), reusing CDIF/schema.org slots on the schema:Dataset root.

### `ogch.techniqueProfile.geochemProfile.SEM-FIBSEM.detail` — FIB-SEM Analysis Detail

**Type:** schema

Detail block for FIB-SEM hasPart items. Discriminates on ada:componentType, carries analysis-level required properties and an @id reference to a registered semFibsemTAPP definition, and per-dataset schema:additionalProperty entries constrained via $refs to the parameterValues registry plus a catch-all. Generated by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.SEM-Imaging.detail` — SEM Imaging Analysis Detail

**Type:** schema

Detail block for SEM imaging hasPart items. Discriminates on ada:componentType, carries analysis-level required properties and an @id reference to a registered semImagingTAPP definition, and per-dataset schema:additionalProperty entries constrained via $refs to the parameterValues registry plus a catch-all. Generated by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.Solution-MC-ICPMS.detail` — Solution MC-ICP-MS Analysis Detail

**Type:** schema

Dataset-level analysis-instance detail for solution MC-ICP-MS, reusing CDIF/schema.org slots on the schema:Dataset root.

### `ogch.techniqueProfile.geochemProfile.Solution-Q-ICPMS.detail` — Solution Q-ICP-MS Analysis Detail

**Type:** schema

Dataset-level analysis-instance detail for solution Q-ICP-MS, reusing CDIF/schema.org slots on the schema:Dataset root.

### `ogch.techniqueProfile.geochemProfile.Solution-SF-ICPMS.detail` — Solution SF-ICP-MS Analysis Detail

**Type:** schema

Dataset-level analysis-instance detail for solution SF-ICP-MS, reusing CDIF/schema.org slots on the schema:Dataset root.

### `ogch.techniqueProfile.geochemProfile.TEM.detail` — TEM Analysis Detail

**Type:** schema

Detail block for TEM hasPart items. Discriminates on ada:componentType, carries analysis-level required properties and an @id reference to a registered temTAPP definition, and per-dataset schema:additionalProperty entries constrained via $refs to the parameterValues registry plus a catch-all. Generated by tools/build_tapp.py.

### `ogch.techniqueProfile.geochemProfile.XCT.detail` — Lab-XCT Analysis Detail

**Type:** schema

Laboratory X-ray computed tomography analysis-specific detail properties. Discriminates on ada:componentType (XCTVolume, XCTProjectionImageSet, XCTSegmentationVolume, XCTRenderedImage, XCTQuantitativeTabular), carries analysis-level required properties (analyst, dates, sample, VOI) and per-dataset schema:additionalProperty values referencing the labxctTAPP parameterValues registry.

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

### `ogch.techniqueProfile.geochemProfile.EMPA.profile` — EMPA Geochem Profile

**Type:** schema

Technique-specific dataset profile for EMPA. Extends adaProduct with constraints on schema:measurementTechnique (pointing at empaTAPP) and schema:distribution.schema:hasPart (allowing detailEMPA entries).

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

### `ogch.techniqueProfile.geochemProfile.Solution-Q-ICPMS.profile` — ADA Solution Q-ICP-MS Product Profile

**Type:** schema

Path-driven ADA product profile for ADA Solution Q-ICP-MS Product Profile.

### `ogch.techniqueProfile.geochemProfile.Solution-SF-ICPMS.profile` — ADA Solution SF-ICP-MS Product Profile

**Type:** schema

Path-driven ADA product profile for ADA Solution SF-ICP-MS Product Profile.

### `ogch.techniqueProfile.geochemProfile.XCT.profile` — ADA Lab-XCT Product Profile

**Type:** schema

Path-driven ADA product profile for ADA Lab-XCT Product Profile.

