# Geochem Analytical Product

Domain-neutral base profile for metadata documenting an analytical product from a
geochemistry (or related analytical) laboratory workflow. It was factored out of
`adaProduct` so that the generic analytical surface can be reused by any archive,
with archive-specific submission/delivery layers extending it.

It composes the CDIF profiles and adds the generic geochem surface:

- **Composition** — CDIF `cdifCore`, `cdifDataDescription`, `cdifManifest` (bundle,
  applied only when a distribution is a `schema:Collection`), and `cdifProvenance`.
- **Analysis events** (`prov:wasGeneratedBy`) — the instruments, computational tools,
  and reagents actually used; the laboratory (`schema:location`); the samples analysed
  (`schema:object`); the session identifier and timing. `prov:used` uses the CDIF
  role-keyed wrapper model (constraint-only `if/then` pins for `schema:instrument`,
  `bios:computationalTool`, `prov:reagent`, and an inline/`@id` `tappDefinition`).
- **Variables measured** (`schema:variableMeasured`) — extends `cdifInstanceVariable`
  with description, alternate names, measurement technique, units, and value bounds.
- **Coverage** — `schema:spatialCoverage`, `schema:temporalCoverage`,
  `dqv:hasQualityMeasurement`.
- **Distributions** — the generic structure: `schema:DataDownload` / `schema:WebAPI`,
  an optional `cdi:isStructuredBy` data-structure description, and per-column tabular
  mapping for tabular-text files. File-classification vocabulary (e.g. ADA
  `ada:componentType`) is added by the extending profile.

A record declares conformance to `https://w3id.org/geochem/metadata/profiles/geochemProduct`
(alongside the CDIF profile URIs). Extending profiles add their own conformance URI, so
a record self-declares the full profile chain.

## Shared `$defs`

`UsedComputationalTool` and `UsedReagent` (the actual-tool / actual-reagent shapes used
in `prov:used`) are defined here and re-exported by `adaProduct` for backward
compatibility with technique profiles that reference them.
