# LA-ICP-MS Analysis Detail (Dataset-level)

Analysis-instance metadata for a Laser-Ablation ICP-MS dataset (`detailLAICPMS`). Expressed on the
`schema:Dataset` root and combined with the base ADA product via `allOf: [adaProduct, detailLAICPMS]`
in the LA-ICPMS profile.

Rather than inventing `ada:` properties, it reuses existing CDIF / schema.org slots:

- **Analyst** → `schema:contributor[schema:roleName='analyst']`
- **Analysis dates** → `prov:wasGeneratedBy.schema:startDate` / `schema:endDate`
- **Analysed sample** (name, persistent identifier, spot/location) →
  `prov:wasGeneratedBy.schema:object[…materialsample…]` (`schema:name`, `schema:identifier`,
  `schema:additionalProperty`)
- **Per-analysis parameters** (replicates, transect length, mapping area, signal integration time) →
  `prov:wasGeneratedBy.schema:additionalProperty[]` `schema:PropertyValue` entries, `$ref`-constrained
  to the [parameterValues](../../techniqueProtocols/parameterValues/) registry
- **Protocol identifier** → `schema:measurementTechnique` (`@id`, the laicpmsTAPP DOI)
- **Coupled protocols/datasets** → `schema:relatedLink`
- **Funding for the analysis** → `schema:funding`
- **Oxide production** → `dqv:hasQualityMeasurement`

Per-file classification (`ada:componentType`) is **not** here — it lives on the profile's
`schema:distribution` / `schema:DataDownload` `hasPart` items.

Generated from the LA-Q_SF-ICPMS TAPP `schema path` column by the path-driven emitter
(`tools/schema_path_emitter.py`).
