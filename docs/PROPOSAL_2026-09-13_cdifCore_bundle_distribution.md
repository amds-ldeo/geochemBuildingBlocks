# Proposal to cdifCore: a distribution branch for a bundle reached through its landing page

**13 September 2026.** For `cdifProfile/cdifCore`. Raised by a consumer that hits it on every
record it publishes.

---

## 1. The prose and the schema disagree

`cdifCore/schema.yaml` says, of `schema:url`:

> Web Location of a page describing the dataset (landing page), typically providing links or
> instructions to get the actual resource content; analogous to dcat:accessURL. **If a direct
> link is available to get the data, put in distribution/contentUrl**

and of `schema:distribution`:

> **If user must access data through a landing page, provide link to landing page in the 'url'
> property for the dataset**

That is a clear rule, and it describes a real and common delivery shape: there is no direct
href, so the landing page carries the address.

The JSON Schema does not implement it. `schema:distribution.items` is

```yaml
items:
  anyOf:
    - $ref: '#/$defs/DataDownload'
    - $ref: '#/$defs/WebAPI'
```

and `schemaorgProperties/dataDownload/schema.yaml` ends

```yaml
required:
- 'schema:contentUrl'
```

So every distribution item must either publish a direct href or be a web service. **The
landing-page case the prose describes has no branch, and is rejected.**

`cdifManifest` does not relieve it, by its own statement:

> The base `schema:distribution` anyOf [DataDownload, WebAPI] contributed by cdifCore is
> preserved — this BB only adds property constraints, no new anyOf branch.

Nor can a downstream profile relieve it: JSON Schema `allOf` composition only ever narrows, so
no extending profile can widen an inherited `anyOf`. It has to change here.

## 2. The consumer

Astromat Data Archive (ADA), 7,446 published records. Each declares
`https://w3id.org/cdif/manifest/1.1` in `schema:subjectOf` → `dcterms:conformsTo`.

A record's data is a zip bundle. It is typed `["schema:DataDownload", "schema:Collection"]` and
enumerates its component files in `schema:hasPart`, which is the manifest bundle pattern. It has
no `schema:contentUrl`, and deliberately so: the bundle is fetched through a separate endpoint
that returns `{"downloadUrl": "<presigned S3 URL>"}` rather than the bytes, and the presigned
URL expires, so there is no href that can be published. The record's address is its landing page
in `schema:url` — exactly what the prose prescribes.

**Every one of those records fails this constraint.** It is not a data-quality problem; it is
the prose and the schema disagreeing.

## 3. Proposed change

Two parts. The second cannot be written inside the distribution item, because JSON Schema has no
parent reference and an item cannot see the dataset's `schema:url`; it is therefore written at
dataset scope as the equivalent implication.

### 3.1 A third branch on `schema:distribution.items` (item scope)

```yaml
items:
  anyOf:
    - $ref: '#/$defs/DataDownload'
    - $ref: '#/$defs/WebAPI'
    - $ref: '#/$defs/BundleCollection'      # NEW
```

```yaml
$defs:
  BundleCollection:
    type: object
    description: >-
      A bundle distribution: an archive or package that enumerates its component files in
      schema:hasPart and is retrieved by a route published separately -- a WebAPI distribution
      entry, or the dataset's landing page in schema:url. It has no direct href of its own, so
      schema:contentUrl is not required.
    properties:
      '@type':
        type: array
        items: {type: string}
        contains: {const: 'schema:Collection'}
        minItems: 1
      'schema:hasPart':
        type: array
        minItems: 1
    required: ['@type', 'schema:hasPart']
```

The branch is narrow on purpose. It admits only something positively typed `schema:Collection`
that actually enumerates its parts. A plain `DataDownload` still requires `contentUrl`.

### 3.2 The landing page becomes mandatory when it is the only address (dataset scope)

```yaml
- description: >-
    If a bundle Collection publishes no schema:contentUrl, the dataset must publish a landing
    page in schema:url -- otherwise the record states no way to reach the data at all.
  if:
    required: ['schema:distribution']
    properties:
      'schema:distribution':
        type: array
        contains:
          type: object
          required: ['@type']
          properties:
            '@type': {type: array, contains: {const: 'schema:Collection'}}
          not: {required: ['schema:contentUrl']}
  then:
    required: ['schema:url']
```

This carries the same truth as "contentUrl is not required if there is a Dataset/schema:url",
in the direction JSON Schema can check, and it makes the rule strictly stronger than today for
the case it admits: a bundle may omit `contentUrl` **only** if the record says where to go
instead.

## 4. Tested

Against two published ADA records, `10.60707/an7h-fg87` and `10.60707/3xec-yw98`, using the
resolved adaEMPA profile schema (which composes cdifCore, cdifDataDescription, cdifManifest and
cdifProvenance). Prototype in `scratchpad/proto_cdif_collection_branch.py`.

| | distribution errors before | after |
|---|---:|---:|
| `10.60707/an7h-fg87` | 2 | 1 |
| `10.60707/3xec-yw98` | 2 | 1 |

The remaining error was **not** a CDIF defect: ADA's WebAPI entry was missing
`schema:potentialAction` and `schema:termsOfService`, both of which cdifCore's WebAPI branch
requires and both of which describe the endpoint truthfully. With that entry completed on the
consumer side, **distribution errors go to 0**.

Two negative controls, both behaving as intended:

- a bundle Collection with no `contentUrl` **and** no `schema:url` → rejected;
- a plain `DataDownload` with no `contentUrl` → still rejected.

## 5. What this does not ask for

No change to `cdifManifest`, whose hasPart rules already describe this shape correctly. No
relaxation of `contentUrl` for ordinary downloads. No new vocabulary.
