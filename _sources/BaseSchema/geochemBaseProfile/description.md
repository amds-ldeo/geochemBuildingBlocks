# Geochem Base Profile

The geochemistry overlay on its own. This block holds everything this repository
contributes to an analytical product record, and nothing it imports: no CDIF content, no
composition. `geochemProduct` is the composition — the CDIF profiles plus this block —
and this is the half gBB authors.

Factored out of `geochemProduct` on 2026-11-04, following the `cdifProfile` /
`cdifCompositeProfile` split upstream, where each component profile is its own block and
the composite is a thin `allOf` over them. The point is reviewability: what gBB adds can
now be read and diffed without the four imported CDIF branches around it.

## What is in here

- **Analysis events** (`prov:wasGeneratedBy`) — the instruments, computational tools and
  reagents actually used; the laboratory (`schema:location`); the samples analysed
  (`schema:object`); the session identifier and timing. `prov:used` uses the CDIF
  role-keyed wrapper model, with constraint-only `if`/`then` pins for `schema:instrument`,
  `bios:computationalTool`, `bios:reagent` and an inline-or-`@id` `ada:tappDefinition`.
- **Variables measured** (`schema:variableMeasured`) — extends `cdifInstanceVariable` with
  description, alternate names, measurement technique, units and value bounds.
- **Coverage** — `schema:spatialCoverage`, `schema:temporalCoverage`,
  `dqv:hasQualityMeasurement`.
- **Distributions** — the generic structure: `schema:DataDownload` / `schema:WebAPI`, an
  optional `cdi:isStructuredBy` data-structure description, and per-column tabular mapping
  for tabular-text files. File-classification vocabulary (e.g. ADA `ada:componentType`) is
  added by the extending profile, not here.
- **`$defs`** — `UsedComputationalTool`, `UsedReagent` and `PropertyValueEntry`, which the
  generated technique `detail/` and module blocks reference across the boundary.

## Two things it is NOT

**Not a list of properties absent from CDIF.** Most of these keys exist upstream; this
block narrows them and gives them their gBB labels. A property here may be a pure
refinement of a CDIF property, and that is the normal case rather than the exception.

**Not a standalone record schema.** On its own it constrains an object carrying the
geochem surface and says nothing about the CDIF properties a record also needs, so it
asserts far less than a record must satisfy. Compose it, or reference `geochemProduct`.
It also has no conformance class and no `conformance.json`: nothing conforms to the
overlay alone, and `build_conformance_sidecars` derives sidecars for `geochemProduct` and
`adaProduct` by name, not by walking the directory.
