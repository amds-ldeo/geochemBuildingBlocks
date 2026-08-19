# Structured Data File Type

Describes a container/array data file (e.g. HDF5, NeXus) that is a member of an ADA
product bundle (`schema:distribution.hasPart`) and whose internal layout is described
by a CDIF DataStructure via `cdi:isStructuredBy`. Typed as `ada:structuredData` and
`cdi:PhysicalDataSet`.

This is the **bundle-part analog of the monolithic single-file `cdi:isStructuredBy`
pattern**: the structure-description pattern is chosen by the file's *encoding*, not by
its position in the distribution.

- **Tabular text** files (CSV, fixed-width) use `tabularData` — CSVW/DDI-CDI layout plus
  per-column `cdif:hasPhysicalMapping`.
- **Container/array** files (HDF5, NeXus) use `structuredData` — a `cdi:DataStructure`
  (Dimensional / Long / Wide / DataStructure) attached with `cdi:isStructuredBy`, whose
  components carry their own physical mappings (LocatorMapping).

The structure may be stated inline, or referenced by `@id` from a structure declared once
and shared across several parts of the same layout.
