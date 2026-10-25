# Legacy profiles, profile cids, the EPMA/TEM flip and the nil token

Moved out of `CLAUDE.md` on 2026-10-25, text unchanged except where noted; `CLAUDE.md` keeps a short summary and a pointer here. Dates and counts below are as of when each passage was written; re-measure before quoting one.

### `profile-ada` and `adaProfile` are the PRE-TAPP generation, and the goal is to retire them

No generator owns them **by history, not by mystery**: they predate the TAPP pipeline. They came
from the earlier work that generated schemas for metadata describing **SAMIS** datasets (source
material lives on Google Drive under `Astromat\metadata` and
`Astromat\SpecificationDocs\AstromatDataDeliveryMetadata`), and the intent is to supersede them
with the TAPP-based collection under `techniqueProfile/geochemProfile/<TECH>/`.
`generate_profiles.py` knows them but is deprecated and refuses to run — it emits the retired
object-form `ada:componentType` — so **nothing** regenerates these and no regeneration will ever
correct a mistake in one. `adaProfile/QRIS` named a detail block in its description and
referenced it nowhere for as long as the file existed, for exactly that reason (fixed 2026-09-05,
`1db480deb`).

Where the supersession has reached: **all 9 now have a TAPP-based `profile/`** — EPMA, SEM, TEM
and XCT already did, and QRIS, RAMAN, VNMIR, XANES and XRD were generated 2026-10-07. Nothing had
been missing but a `build_profile.PROFILES` entry; all five already had `tapp/`, `detail/` and
`component_types`, and PROFILES membership is the only gate (`regenerate.py` skips
profile-1/profile-2 for a technique with no entry). Repo-wide that takes TAPP-based `profile/`
from 29 to **34 of 59** techniques.

So every `profile-ada` under `geochemProfile/` now has a replacement, and what remains before any
of them can be retired is the record-migration question below — not schema work. The 32
`adaProfile/` technique directories are a separate and larger job.

> **`addtype` is the real decision in a PROFILES entry, and it must be answered from the corpus.**
> `addtype[0]` is written into the generated example, so a profile whose head label no record
> carries rejects its own records — which is what EPMA did by holding two acronym forms and never
> its sentence-case partner. Harvest candidates from the legacy `profile-ada`, filter to values
> that exist in adaProduct's controlled list (coining one is inventing a product type), then order
> by record count. Counted over 7446 rows of `public.json_table` on 2026-10-07, the head label is
> `X-ray diffraction` (66) not `X-ray Diffraction (XRD) Tabular` (0),
> `X-ray absorption near edge structure (XANES) spectroscopy` (245) not the Image Stack form (0),
> and `Visible, near-, and mid-infrared spectroscopy` (183) not any acronym form (0) — the
> sentence-case name every time.
>
> **Give the TAPP profile a DIFFERENT `cid` from the legacy one.** These five take `ada<TECH>`
> against the legacy `ada<TECH>Full`. Two schemas claiming one `conformsTo` URI is a fork whose
> winner is read order. **All nine `geochemProfile` techniques now comply**: SEM was corrected in
> #149 and EPMA and TEM in #157, which were the last two sharing a cid between their `profile/`
> and their `profile-ada/`.
>
> A fork is not only an ambiguity for readers, it silently breaks conformance detection.
> `build_conformance_sidecars` must emit one sidecar per DISTINCT cid, so a forked cid makes it
> keep one block and discard the other — taking that block's `ada:componentType` vocabulary with
> it. For `adaTEM` the discarded twin held 7 types that no other sidecar accepted
> (`TEMPatternsImage`, `STEMEDSCube`, `TEMEDSImageCollection`, `STEMEELSCube`, `STEMEDSTabular`,
> `STEMEELSTabular`, `STEMEDSTomo`), so 257 ADA records resolved to no technique profile at all.
> EPMA lost nothing only because its TAPP block happened to cover the same types.
>
> **Five cross-tree forks remain and are harmless**: `adaQRIS`, `adaRAMAN`, `adaVNMIR`,
> `adaXANES` and `adaXRD` are each claimed by an `adaProfile/<TECH>/profile-ada` as well as the
> `geochemProfile/<TECH>/profile`. They lose nothing, because the `geochemProfile` legacy block
> already carries `ada<TECH>Full` and its sidecar keeps the vocabulary. Judge a fork by whether
> any componentType becomes unreachable, not by the fork alone.

**These profiles are not CITED — their URI is DERIVED from record content.** Corrected
2026-10-20, and two earlier versions of this paragraph were both wrong. The first said no record
declares `dcterms:conformsTo` at all (0 of 7446), which had been measured at the record ROOT
only. The second said records "cite" these profiles and that citation and content-detection
disagree for 4,217 records. **There is no citation route at all.** The loader ASSIGNS
`schema:subjectOf.dcterms:conformsTo` from content — `record_items.py:715`,
`base_conformance_uris(...)` — so a count of that field is a count of DERIVATIONS, and a derived
field cannot preserve a stale label across a re-run. Every record carries one, 7,447 of 7,447,
at that nested path.

**35 distinct profile cids are derived.** Re-measured 2026-10-24, AFTER the EPMA and TEM flip —
the three `Full` rows below moved, so read the date before quoting any of them:

| cid | records | holder |
|---|---|---|
| `geochemProduct`, `adaProduct` | 7,447 each | the base products |
| `adaSEMFull` | **2,918** | the LEGACY `geochemProfile/SEM/profile-ada` — NOT flipped |
| `adaTEM` | **870** | the TAPP `geochemProfile/TEM/profile` — flipped 2026-10-24 |
| `adaEPMA` | **436** | the TAPP `geochemProfile/EPMA/profile` — flipped 2026-10-24 |
| `adaTEMFull`, `adaEPMAFull` | **0 each** | the LEGACY blocks, now reached by no record |
| `adaSEM`, `adaSEMComposition`, `adaXCT`, `adaLabXCT` | **0 each** | the TAPP `profile/` blocks — reached by NO record |
| `adaXANES` 245, `adaVNMIR` 183, `adaXRD` 66 | | `adaProfile/*/profile-ada` — legacy |
| `adaLIT` 137, `adaICPMS` 112, `adaARGT` 97, `adaFTICRMS` 89, `adaLCMS`/`adaGCMS` 75 … | | all legacy |

**#149 was a SWAP, not a rename, and the records followed the BLOCK rather than the label.**
`SEM/profile` went `adaSEMFull` -> `adaSEM` and `SEM/profile-ada` took the reverse
(`ccb49db80f`, 2026-10-17); #157 un-forked EPMA and TEM the same way (`e6f2772c43`, 2026-10-18).
An earlier table here recorded `adaSEM` 2,912 / `adaTEM` 870 / `adaEPMA` 435, measured
2026-10-15 — those were CORRECT derivations against the cid assignment of that day, when each
bare `ada<TECH>` was the legacy block's label. Because the field is derived, re-derivation moved
the same records onto the `Full` labels. Do not read the old counts as a disagreement that needs
reconciling; there was never a stale citation to disagree with.

**THE FLIP HAS LANDED for EPMA and TEM (2026-10-24).** Decided by Stephen, built by the ADA
loader, measured over all 7,447 records:

| cid | records | | cid | records |
|---|---|---|---|---|
| `adaEPMA` | **436** | | `adaEPMAFull` | 0 |
| `adaTEM` | **870** | | `adaTEMFull` | 0 |
| `adaSEM` | **0** | | `adaSEMFull` | **2,918** — untouched, out of scope |

All **1,306 went from failing to passing** — measured, not the predicted figure. Validation
7,447 success / 0 failed, with the one long-standing baseline failure unchanged. Determinism:
two full regenerations, 0 DOIs present in only one run, 0 whose output differs.

**The disagreement between the loader's static path and the CDIF engine is DELIBERATE and
load-bearing — not an open question.** The earlier text here said it was open; it is not, and
reading it that way invites exactly the wrong repair. The mechanism lives with the code that
owns it: **`metadata/AGENTS.md`, section "Which technique profile a record claims, and the one
default holding it there"**. Read that section, not a restatement here, because a restatement
drifts from the code. In outline: the loader swaps the cid in its STATIC SEED and then runs
`detect_and_apply` with `technique_profiles="preserve"`, which keeps whatever the static path
wrote.

**What is gBB's half, and it is the half that is ours to change.** `detect_domain_conformance`
genuinely resolves these records to the TAPP cid — the legacy and TAPP cids share one
`exclusiveGroup` and the TAPP priority outranks LEGACY 3, with no fall-back. That preference is
**live and correct**, and the loader's `preserve` **overrides it deliberately**. Do NOT describe
these priorities as inert or vestigial and do not tidy them away: they are the thing the override
overrides, and removing them would break the mechanism silently, here, where nothing would fail.

**The cost of switching `preserve` to `detect` is measured, not argued.** That one word hands
every technique to these priorities at once:

    adaSEM      priority 5    65 schema:variableMeasured `contains` pins
    adaSEMFull  priority 3     1 pin

So 2,918 SEM records would move onto a profile 65 pins deep with no nil tokens built for any of
them. Nothing raises at the moment of the change; the records simply start failing afterwards, in
a different repository from the change. **"Complete the rollout" and "flip SEM" are the same
action under `detect`.** SEM needs its own measurement and token pass first — and do not assume
its failing pins match EPMA's or TEM's, which brings us to:

**The flip is a REVALIDATION, not a relabelling**, and the pin names are per-technique. Measured:

    EPMA   ada:deadTime, ada:proceduralBlankLevel, `Sampling Unit Name`, `Detection Limit`
    TEM    ada:deadTime,                           `Sampling Unit Name`, `EELS Detection Limit`

`ada:proceduralBlankLevel` is EPMA-only — TEM's profile does not require it, and emitting it there
would assert a reading nobody asked for. And TEM's second name is **not** `Detection Limit`:
until #201 it was the stale token `sensitivityDetectionLimit`, and two separate handoff notes
carried `Detection Limit` for both techniques. Building from that would have left all 870 TEM
records failing while looking like the token SHAPE was wrong rather than the name. Do not treat
the rollout as a labelling change, and do not carry one technique's pin names to another.

**Those two are the pins the CORPUS FAILS, not the pins that exist, and the difference is two
orders of magnitude.** Measured 2026-10-23 on the resolved schemas: `EPMA/profile` pins **46**
`variableMeasured` names through `contains` and `TEM/profile` pins **50**, against **1** in each
`profile-ada` (`Sample preparation`). So the flip's constraint SURFACE is 45 and 49 newly pinned
names; the claim behind the "two" is that every other one is already satisfied by real record
content. Read as "only two pins exist" it badly understates what a flipped record must carry —
a mistake made once from this paragraph's earlier wording. Before building nil-token members,
RE-MEASURE which pins the corpus fails rather than reusing the figure: it was taken against the
schema of 2026-10-20, and building for two when the real set is larger ships records that still
fail. Derive the lists from the resolved schema, by walking every `contains` for a
`properties.schema:name.const`.

> **The resolution is a NIL TOKEN, not a relaxed constraint** (Steve, 2026-10-20). The TAPP
> workbooks are Ruolin's and the ADA corpus predates TAPP generation, so the pins stay and the
> records DECLARE the absence. The agreed token is the OGC nil reason `unknown`, written as the
> **expanded IRI, as a string**:
>
>     http://www.opengis.net/def/nil/OGC/0/unknown
>
> Expanded rather than the compact `nil:unknown` because nothing guarantees a consumer applies
> ADA's `adaJSONLD.json` context (which does bind `nil:`) before reading a scalar. `unknown`
> rather than `missing` because ADA holds no record of a value that does not exist, only of one
> no submitter sent. Where a field accepts a REFERENCE the object form `{"@id": "nil:unknown"}`
> remains correct and is already in use for `cdif:physicalDataType`; the string form is only for
> the scalar-typed fields.
>
> **No gBB constraint changes, and that is the point.** `ada:deadTime` is
> `anyOf: [{number}, {string}]` and `ada:proceduralBlankLevel` is `{type: string}`, so an IRI
> string already validates; the two FAILING `variableMeasured` `contains` pins (two of 46 and 50 —
> see the correction above) require `schema:name` ALONE, so the member must exist and be named
> exactly, with the token as its `schema:value`.
> An `{"@id": …}` OBJECT does **not** work in the scalar fields — it fails both — which is why
> the string form was chosen over the object form the question was first asked about.
>
> **The member needs FOUR properties, not three — `schema:description` is also required.**
> Corrected 2026-10-21, after the forms session tested the three-property shape this section
> first specified and found it BREAKS a record that currently validates. The requirement is
> record-side and unconditional in both generations, which is why it bites immediately rather
> than only after a flip:
>
>     EPMA/profile       /properties/schema:variableMeasured/items/allOf[0]
>     EPMA/profile-ada   /allOf[0]/allOf[4]/properties/schema:variableMeasured/items
>
> So the member is `{"@type": […], "schema:name": "<the pinned name>",
> "schema:description": "<text>", "schema:value": "<the nil IRI>"}`. Note the legacy path: a
> check of the ROOT `properties.schema:variableMeasured.items` alone finds the TAPP requirement
> and misses the legacy one, which sits two `allOf` levels down — the same top-level-only
> mistake that `CLAUDE.md` warns about for counts.
>
> **The four-property member is CONFIRMED, and there is no third blocker.** An earlier version of
> this note carried residual `dcterms:conformsTo` `contains` errors as an unresolved risk. They
> were an artifact of the trial method: patching a STORED document and revalidating skips
> `detect_and_apply`, and `conformsTo` is DERIVED, so the added members obliged a CDIF module
> that detection would have supplied. Run properly — four-property member, then detect-and-apply
> to re-derive `conformsTo`, then validate — a real EPMA record gives **0 errors** against
> `adaEPMA`. **The general rule: a trial that mutates a stored document is not a valid test of
> anything DERIVED from that document's content.** Regenerate; do not patch JSON.
>
> **NOW MEASURED over the full corpus (2026-10-24), and it passed.** All 1,306 EPMA and TEM
> records went from failing to passing: `ada:deadTime` on 1,306, `ada:proceduralBlankLevel` on the
> 436 EPMA only, `Sampling Unit Name` on 1,306, `Detection Limit` on the 436 and
> `EELS Detection Limit` on the 870. Validation 7,447 success / 0 failed with the one
> long-standing baseline failure unchanged, and two full regenerations byte-identical.
>
> **The scope blocker is RESOLVED.** It read "the convention is not buildable until it resolves"
> — the token must only go on records whose technique profile requires it, and the requiring
> profiles were the TAPP variants while records resolved to the `Full` ones. The flip settled
> that: the scope is now EPMA and TEM, enforced by the loader, and the tokens are built and
> measured against exactly those. SEM is deliberately out — see the flip section above for what
> switching `preserve` to `detect` would cost.
>
> **Verified end-to-end, not predicted.** A real flipped EPMA record carrying the token as a
> string in both properties, and a named `variableMeasured` member carrying it in `schema:value`
> for each pin, validates against `EPMA/profile/resolvedSchema.json` with **0 errors** — measured
> by the Validation session 2026-10-20, against the schema as authored. The object form's failure
> in those same fields was confirmed independently on the same record.
>
> **`ada:analyticalMode` takes `unknown`, as a STRING, on the dataset side only** (Stephen,
> 2026-10-22). Distinct from the gated fields above and easy to conflate with them:
>
>   the mode PROPERTY     `unknown` -- every analysis HAS a mode; ADA does not record which
>   a GATED FIELD         `inapplicable` where the implied mode excludes it, else `unknown`
>
> `inapplicable` on the mode itself would assert the analysis had no mode, which is false for
> every record. The form is a string element carrying the expanded IRI, because the schema asks
> for one: `detail/` places the property with `items: {type: string}` and no enum, so a nil IRI
> validates, while `tapp/` constrains items to the technique's mode enum for the 14 gating
> techniques and a nil IRI would VIOLATE it there. That asymmetry is correct rather than an
> oversight -- a record may not know its mode, but a procedure that cannot say which modes it runs
> is not a procedure. No schema widening is needed, and the object form
> `{"@id": "nil:unknown"}` would NOT validate here.
>
> Nothing demands the value today: `ada:analyticalMode` is declared and optional everywhere, 0
> required sites repo-wide, because of the bare-`[]` requiredness defect (`docs/ANALYTICAL_MODE.md`). **And a correct
> fix for that emits `required` AND `minItems: 1`, not `required` alone** -- `required` by itself
> is satisfied by an empty array, which asserts nothing. Measured across the `tapp` blocks, 2,135
> required array properties already carry `minItems` and 279 do not, so the pairing is the
> established convention and the 279 are the anomaly.
>
> `tools/build_mode_applicability.py` carries all of this as `mode_property` in
> `docs/mode_applicability.json`, so the loader reads it rather than re-deriving it.

> **Recorded as a deliberate trade, not a fix.** A required pin satisfied by a placeholder passes
> while conveying no measurement — the vacuous-validation shape `docs/SILENT_SUCCESS.md` and the
> `adaSubjects` work both circle. It is accepted because an explicit machine-readable `unknown`
> lets a consumer distinguish *declared absent* from *present*, which nothing can do today, and
> because the alternative was loosening authored workbooks to fit legacy data. Do not cite it as
> precedent for relaxing a TAPP constraint, and do not add a second sentinel beside it — the
> examples already carry 1,090+ `"no value available: X"` strings from the generators, and a
> third convention would make absence unreadable. The loader emits this; no gBB generator does.

Do NOT read this table as "the legacy profile owns the records" any more. Ask which block pins
the cid today — `grep -rlE "profiles/<cid>([^A-Za-z0-9]|$)" --include=schema.yaml _sources/` —
because the answer moved twice in two days. **Anchor that pattern.** An unanchored
`profiles/adaSEM` also matches `adaSEMFull`, silently merging a cid with its legacy twin, which
is exactly the distinction that matters here; a first pass without the anchor reported zero
forks repo-wide against the five that exist.

So retiring or renaming a legacy profile moves every record that derives to it, and nothing in
gBB would notice: no gBB check reads ADA records. But it does not ORPHAN them, and the earlier
wording here said it did. Because the field is derived rather than stored, a renamed cid is
simply re-derived on the next loader run — which is exactly what #149's swap did to 2,918 SEM
records without touching one of them. What a rename changes is which SCHEMA those records are
then judged against, so sequence it as: decide the cids, confirm the new target ACCEPTS the
records, then deprecate. Judge the move by validation, not by citation.

`adaTEM` and `adaEPMA` were **ambiguous** URIs until #157, each claimed by two schemas. They now
resolve to one block apiece — the TAPP `profile/` — so the ambiguity is gone, and the question
that used to sit here is CLOSED: as of 2026-10-24 the loader derives the TAPP cid for these
records and all 1,306 pass it, carrying the nil token. See the flip section above. The records
no longer "fail the TAPP schema if flipped" — they are flipped, and they pass.

The risk compounds through a second route. The ADA loader **derives** `conformsTo` from record
CONTENT (via the CDIF validation repo's `detect_conformance`), so a record is matched to a
profile by what it carries, not by what it cites — and the matched profile's constraints then
have to accept it. That is why relocating the twelve `adaProfile` hasPart-item detail blocks to
the top level, tried on a copy on 2026-09-05, failed **all 218** records of the affected profiles
on a missing `ada:componentType`: those records never mentioned the profile, they were matched
into it. So there are TWO questions to ask before retiring a profile, and the correction above
means the first one is about DERIVATION, not citation: **"which cid does the loader derive for
these records today?"** — measured per cid at `schema:subjectOf.dcterms:conformsTo`, which is
`adaSEMFull` 2,918 and `adaSEM` **zero** — and **"what would `detect_conformance` match here
instead, and would that schema accept these records?"** For SEM the two answers still DIFFER,
and that difference is now the deliberate override described in the flip section, not an open
divergence. For EPMA and TEM they agree as of 2026-10-24: the loader derives the TAPP cid, and
the TAPP schema accepts the records. SEM is the live case, which is why it is the example here.
