# ADA EPMA Profile

Technique-specific metadata profile for Electron Microprobe Analysis (EPMA) products in the Astromat Data Archive. EPMA uses focused electron beams to determine chemical composition of small volumes of solid materials through characteristic X-ray emission.

## Product Types
- **EPMA Image** - Backscattered electron or secondary electron images
- **EPMA Collection** - Sets of EPMA images or maps
- **EPMA QEA** - Quantitative elemental analysis tabular data
- **EPMA SPC** - Spectral data from electron microprobe

## Valid Component Types
- `ada:EPMAImageMap` - Image maps with spectrometer and signal detail (epma_detail)
- `ada:EPMAImage` - Individual EPMA images
- `ada:EPMAQEATabular` - Quantitative elemental analysis tables (epma_detail)
- `ada:EPMAImageCollection` - Collections of EPMA images
- `ada:analysisLocation` - Supplemental analysis location images
- `ada:supplementaryImage` - Supplementary visual materials
- `ada:calibrationFile` - Calibration documents
- `ada:methodDescription` - Method description documents
- `ada:instrumentMetadata` - Instrument metadata documents

## Detail Type
`epma_detail` with properties: `spectrometersUsed`, `signalUsed`
