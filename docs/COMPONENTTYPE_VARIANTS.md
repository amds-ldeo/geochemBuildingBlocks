# componentType and instrument variants (Mc/Q/Sf)

Moved out of `CLAUDE.md` on 2026-10-25, text unchanged except where noted; `CLAUDE.md` keeps a short summary and a pointer here. Dates and counts below are as of when each passage was written; re-measure before quoting one.

### One componentType per product kind — the instrument variant rides on the TAPP, not the type

**Decided 2026-10-16, and it reverses the obvious-looking alternative, so do not re-derive it.**
Mc/Q/Sf variants of a technique share one componentType: `ada:LAICPMSMap` is the map, whichever
mass spectrometer produced it. Minting `ada:LAICPMSMap.mc` / `.q` / `.sf` was considered and
refused. A future delivery proposing variant componentTypes should be refused on this basis
rather than measured again.

**The file-shape question is SETTLED on domain grounds, not open pending data.** Map and tabular
data files from MC, Q and SF are not going to be different — Steve, who owns the domain. An
earlier draft of this paragraph said it "cannot be answered today" because no ADA or TAPP example
carries a `cdif:hasPhysicalMapping`, which wrongly framed a known answer as a gap waiting on
evidence. Do not go collecting physical mappings to settle it.

**The variant distinction is real but PROCEDURE-side only.** The three LA workbooks genuinely
differ — 128 metadata items shared, `laMcicpms` unique in **15** (Collector Configuration, Faraday
Cup Amplifier Resistor Values, the three Double-Spike items, Baseline Measurement Approach),
`laQicpms` in 1 (Signal Collection Mode), `laSficpms` in 2 (E-scan Range, Triple Scanning Mode) —
and the MC items carry BOTH Procedure-Level and Analysis-Level tiers. That difference lives
entirely in what `tapp/` and `detail/` record, which is why three TAPPs exist. It never reaches
the file, and `ada:componentType` classifies the FILE.

So the discriminator for Mc/Q/Sf is the TAPP reference — `prov:used` → a TAPP definition naming
`laMcicpmsTAPP` — which is the axis the variant actually lives on.

**The precondition this section used to declare unmet IS NOW MET, and that changes what is
blocked.** It read "0 of 7,447 records carry a TAPP reference today", citing
`tools/check_migration_readiness.py`, and concluded that anything deriving the variant from
record content would be unable to "until that migration lands". **7,263 of 7,447 carry one** —
measured, and already corrected in the analytical-mode note (`docs/ANALYTICAL_MODE.md`), which says in so many words that
it "corrects an older claim that 0 records carry a TAPP reference". The correction was announced
there and never applied HERE, so a reader arriving at this section was told the discriminator did
not exist while 7,263 records carried it. That is the more dangerous half of a contradiction: the
stale claim sits exactly where someone would act on it.

**What remains true is narrower, and the distinction is the useful part.** The `@id` is an opaque
per-lab procedure URI, so **JSON Schema** still cannot use it — it cannot dereference anything,
and no `if`/`then` can read through that identifier. A consumer that CAN resolve the identifier
against a procedure registry is not blocked by the schema: it could read the referenced
definition and recover the variant. So do not cite this section as "the variant cannot be
determined" — cite it as "the variant cannot be determined BY SCHEMA".

**But do not conclude a loader could break the ICP-MS tie today, because the reference is ABSENT
on exactly the records that need it.** Measured 2026-10-24: of the 112 records claiming
`adaICPMS`, **12 carry a TAPP reference and 100 carry none** — and of the 184 records in the whole
corpus that carry no reference at all, **100 are ICP-MS**. So "7,263 of 7,447 carry one" is true
of the corpus and FALSE of this population, which is the trap: a corpus-wide figure licensed a
conclusion about a subpopulation that contradicts it. Always ask which population a reference
count was taken over.

**And the causation runs the other way from the obvious reading.** It is NOT "the cid could not
resolve, so no reference was emitted". The componentTypes do not determine the variant, so the
reference is not emitted AND the cid cannot resolve — two symptoms of one upstream cause, neither
causing the other. Reading a reference that was never written cannot break the tie. The one
ICP-MS reference that IS emitted covers 12 records whose componentTypes refine unambiguously,
and those already resolve without it.

So resolving the tie in a loader becomes worth implementing the moment an ICP-MS record carries a
reference its componentTypes cannot produce — and not before.

**Consequences for anything detecting a profile from componentType.** 21 of the 133 componentTypes
in `build_tapp.TAPP_CONFIGS` are claimed by more than one TAPP, and they are two different problems
that a priority ranking does not solve:

| group | types | handling |
|---|---|---|
| latent ICPMS families | `ada:LAICPMSImage`/`Map`/`Tabular`/`Transect`, `ada:LAICPMSGeochronTabular`, `ada:SolutionICPMSTabular` | declare an honest TIE — ranking picks a favourite and is wrong two times in three |
| live generic types | `ada:analysisLocation` (393 records), `ada:report` (210), `ada:contextPhotography` (54), `ada:quickLook` (47) | exclude from selection — they match everything and discriminate nothing |

The ICPMS six appear in **0 of 7,447 records**; the 8 LA-ICPMS records that exist carry
`ada:LAICPMSRawTabular`, `ada:logFile` and `ada:methodDescription`, none of which collide. All 657
records carrying a generic type already name their real technique in `schema:measurementTechnique`.

> **A per-profile componentType list cannot be derived from a resolved schema.** Every profile
> `$ref`s `universalComponentTypeBranch` and the base file-type blocks, so resolution inlines the
> whole sealed set: a walk over all `profile*/resolvedSchema.json` finds 238 componentTypes with
> 225 "claimed" by ~74 profiles each. That is the universal enum, not a collision. The real
> per-technique list is `build_tapp.TAPP_CONFIGS[<tapp>]["component_types"]` — 61 entries, 134
> distinct types — which is what `build_profile` emits the hasPart branches from. This follows
> from the measured fact recorded in `docs/DETAIL_BLOCK_PLACEMENT.md` that 0 of 61 geochemProfile detail blocks constrain
> `ada:componentType`:
> the per-profile narrowing was never built, so there is no validation narrowing to stay in step
> with.
