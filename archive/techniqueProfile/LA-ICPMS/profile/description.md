# ADA LA-ICP-MS Profile

Technique-specific metadata profile for Laser-Ablation Inductively Coupled Plasma Mass Spectrometry (LA-ICP-MS) products in the Astromat Data Archive. LA-ICP-MS measures in-situ elemental and isotopic concentrations of solid samples by ablating material with a laser and ionizing the aerosol in an argon plasma, separating ions by mass-to-charge ratio. This profile covers LA-Q-ICP-MS (quadrupole) and LA-SF-ICP-MS (sector-field / high-resolution) variants.

## Product Types
- **LA-Q-ICP-MS Processed/Raw** - Laser-ablation quadrupole ICP-MS data
- **LA-SF-ICP-MS Processed/Raw** - Laser-ablation sector-field ICP-MS data

## Valid Component Types
Technique-specific component types are defined by the `detailLAICPMS` detail block:
- `ada:LAICPMSTabular` - LA-ICP-MS tabular data
- `ada:LAICPMSMap` - LA-ICP-MS map (2-D raster) data
- `ada:LAICPMSImage` - LA-ICP-MS image data
- `ada:LAICPMSTransect` - LA-ICP-MS transect (line-scan) data

Universal component types (e.g. `ada:methodDescription`, `ada:instrumentMetadata`, `ada:calibrationFile`) remain valid via the shared universal component-type branch.

## Detail Type
`detailLAICPMS` — carries analysis-level required properties (analyst, analysis dates, sample name, oxide production, spot coordinates, replicate count, transect length, signal integration time) plus per-dataset `schema:additionalProperty` entries and an `@id` reference to the registered laicpmsTAPP protocol.
