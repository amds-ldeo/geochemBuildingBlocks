# Analytical mode and the per-field mode flags

Moved out of `CLAUDE.md` on 2026-10-25, text unchanged except where noted; `CLAUDE.md` keeps a short summary and a pointer here. Dates and counts below are as of when each passage was written; re-measure before quoting one.

## Analytical mode and the per-field mode flags: designed upstream, UNUSABLE today

The TAPP workbooks carry a complete conditional design that gBB does not act on, and the reason
is not a missing generator — it is missing data. Measured 2026-10-21; do not re-derive it.

**What the workbooks declare.** Every workbook has mode-flag columns (`EDS Point Analysis`,
`WDS Mapping`, `SE Imaging`, `Transect`, `Electron Diffraction`, …) whose values are `Y`/`N` per
FIELD, plus an `Analytical Mode` row whose allowed content IS the set of those column headers.
Ruolin's own Purpose cell states the split: *"the procedure-level declaration of measurement
type, distinct from the mode flag columns, which state per-field applicability."* So
`EDS Dead Time` is `Y` for the two EDS modes and `N` for both WDS modes.

**What gBB does with that: nothing.** No tool reads the mode-flag columns. Consequently **284
field rows across 14 techniques have mixed `Y`/`N` applicability**, and they sit at a tier the
emitter turns into an unconditional `required` — so those properties are demanded of records the
workbook says they do not apply to. `semTAPP` alone has 84, `temTAPP` 46, `semCompositionTAPP` 30,
`epmaTAPP` 29.

**And the FIRST question is whether a technique's mode gates anything at all.** Only **14 of 61**
techniques have mode-flag columns between `Purpose` and `Literature Assessment`. For the other
**47** the `Analytical Mode` is **INFORMATIONAL**: reported on an analysis, gating no constraint.
Solution Q/SF/MC-ICP-MS are the clear case — they declare
`Solution nebulisation (continuous) | Flow injection` and no field's applicability varies between
them. Determining a mode there buys nothing, so any effort to derive one belongs to the 14.

> Corrected 2026-10-22. This section first said "213 rows across 11 workbooks", from a header
> regex written here rather than from `build_tapp.mode_columns()`, which is what the generator
> uses. That undercount missed `vnmirTAPP` and `semFibsemTAPP` entirely. Use
> `tools/infer_analytical_mode.py`, which derives both figures from that function.

**Why the conditional cannot be built, measured on the live corpus:**

| | |
|---|---|
| `ada:analyticalMode` in the 7,447 records | **0**, at the dataset root or anywhere else |
| any key containing "mode" in 111,963 `record_subjects` | **0** — there is no SOURCE field |
| `componentType` naming EDS | 502 records, all SEM/STEM/TEM |
| `componentType` naming WDS | **0** |
| EPMA records with any EDS signal in `componentType` | **0 of 436** |

So this is not "the loader does not emit a mode yet". **ADA records no acquisition mode and no
detector anywhere**, so a mode would have to be DERIVED, and for EPMA — the case that motivated
the whole exercise — there is nothing to derive it from. A conditional in any polarity leaves
those 436 records exactly as they are. **The blocker is upstream of both repositories**: ADA does
not record which detector was used. That is a question for ADA and its submitters, not a schema
change, and not a TAPP change either.

**Three anchors were tried and all three are dead.** Do not retry them:

  instrument components   `schema:instrument.schema:hasPart[].schema:additionalType` -- 0 of 7,447
                          records carry ANY instrument part. `adaInstrumentComponentType` has the
                          right terms (`EDS Detector`, `WDS Spectrometer`) and gBB's own generated
                          examples populate them (78 / 56), but gBB examples are generated from
                          workbooks and say nothing about ADA's holdings.
  instrument additionalType  present on all 7,447 and useless: ONE distinct value,
                          `nxs:base_classes/NXinstrument.html`.
  the TAPP reference      7,263 of 7,447 DO carry `prov:used` -> `{@id, @type}` typed
                          `ada:TAPPDefinition`, so the variant's real axis is referenced -- but the
                          `@id` is an opaque per-lab procedure URI and JSON Schema cannot
                          dereference it. (This also corrects an older claim that 0 records carry a
                          TAPP reference; see the note on the `schema:name` guard in `CLAUDE.md`'s recurring bug patterns.)

**What DID land, and it is worth keeping.** `$Dataset.ada:analyticalMode[]`, one row in
`docs/modules/Module_Core.schemapaths.csv` (`7b0488060e`). The procedure side already declared the
modes a procedure PERMITS; this is the analysis side declaring the mode(s) actually USED, which is
the only place a JSON Schema conditional could read. Deliberately **optional** — the tier
arithmetic gives that for free, since `require = (A == "Basic")` on a `$Dataset` path and the
Analysis tier is `Read-Only`. Census: +188, all `type`, **0 decreases**, 657 examples passing.

**If a mode is ever emitted, write the conditionals in POSITIVE polarity** (Stephen, 2026-10-21):

    dead time is NOT required by default
      if analyticalMode contains 'EDS Point Analysis' or 'EDS Mapping' -> require it

not "required by default, excused when WDS". The inverted form needs the anchor to be MANDATORY: an
absent mode fires no `if`, nothing is excused, and the requirement stands against a record whose
mode cannot be determined. Positive polarity degrades to optional when the anchor is absent, which
is the only safe direction and the general rule here — **a conditional you cannot evaluate must
degrade to optional, never to required.**

**And design it per `schema:hasPart`, not at the dataset root.** 264 records have MIXED EDS and
non-EDS parts in one distribution, so a dataset-root mode genuinely cannot describe them. That
makes the per-part reading correct rather than hypothetical — but note the three-levels rule in `CLAUDE.md`:
`hasPart` exists only for a collection, so the monolithic case needs the mode at the dataset root
or on the distribution, and a mixed-mode monolithic dataset is unsayable by construction.

**The interim answer for the motivating case is the nil token, not a conditional.** EPMA's 436
records carry `http://www.opengis.net/def/nil/OGC/0/unknown` for `ada:deadTime`, which these
measurements make literally true: ADA holds no record of a dead time that does not exist, only of
one nobody sent. The conditionals were an attempt to avoid the placeholder; the placeholder is the
honest answer while the information is absent.

### A related emitter defect, real and NOT fixed

`schema_path_emitter.insert()`'s bare-`[]` terminal branch returns without recording requiredness,
and `build_module_bb.py:207` excludes `is_array` from its own required list to MIRROR that
condition — so it inherited the same omission. Measured: **9 fields, 178 declarations, 0
requirements**, every one carrying a `Basic` tier, `ada:analyticalMode` and `ada:reportedProperties`
among them. `build_module_bb` also ASSIGNS its required list over `to_schema()`'s rather than
merging, which silently drops the tree's ancestor requirements the moment its own list is non-empty.

All three are genuine. **An attempt to fix them was reverted** — see `docs/SILENT_SUCCESS.md` #13 —
because the change destroyed 257,052 constraints across 161 blocks while every example gate stayed
green. Redo it one defect at a time, with `constraint_census.py` read LINE BY LINE as the primary
gate and a committed baseline between steps. The saved diff is not in the repo; re-derive from the
line references above.
