# TAPP issue draft: are the analytical-quality labels using the right term?

For filing in [amds-ldeo/tapp](https://github.com/amds-ldeo/tapp). Not yet filed.
Raised by Stephen, 2026-10-23.

## The observation

Six labels across the workbooks describe analytical quality. Four are named **precision**,
two **accuracy**, and **none** is named reproducibility, repeatability, trueness or bias.
But several define themselves with a term other than the one in their name:

| label | defs | defs whose Purpose text says "reproducibility" |
|---|---|---|
| `Analytical Precision` | 6 | **6 of 6** |
| `Between-Session (Long-Term) Analytical Precision and Assessment Method` | 18 | 1 |
| `Within-Session Analytical Precision and Assessment Method` | 9 | 1 |
| `Internal (Within-Measurement) Analytical Precision and Assessment Method` | 18 | 0 |
| `Analytical Accuracy and Assessment Method` | 9 | 0 (uses "percent relative bias") |
| `Analytical Precision` / `Analytical Accuracy` (the two 6-def pairs) | 12 | — |

`Analytical Precision` is the clearest case: all six of its defs open
"Reproducibility of repeated measurements on the same or equivalent reference material,
expressed as 1-sigma relative…". The label and the definition name different quantities.

## Why it matters

These are distinct, standardised concepts (ISO 5725-1; VIM 3rd ed.), and they answer
different questions about a dataset:

- **precision** — closeness of agreement among repeated measurements. Says nothing about
  whether the values are right.
- **trueness / accuracy** — closeness to a true or accepted value. ISO 5725 reserves
  *accuracy* for the combination of trueness and precision; VIM allows the looser usage.
- **repeatability** — precision under *unchanged* conditions: same operator, instrument,
  short interval.
- **reproducibility** — precision under *changed* conditions: different operator,
  instrument, laboratory, or time.

Under those definitions the existing labels already carry the repeatability /
reproducibility axis in their names — `Within-Session` is repeatability-like and
`Between-Session (Long-Term)` is reproducibility-like — which is arguably why the
`laMcicpms` texts reached for "reproducibility". So the structure may be right and only
the wording inconsistent.

## The question

Is each label naming the quantity intended? Specifically:

1. Does `Analytical Precision` mean precision, or reproducibility, as all six of its own
   definitions state?
2. Should the session-scoped labels say repeatability / reproducibility explicitly, given
   that is what "within-session" and "between-session" already encode?
3. Is `Analytical Accuracy` meant in the ISO sense (trueness + precision) or the looser
   sense (trueness alone)? Its text reports "percent relative bias", which is trueness.

## Options

1. **Keep the names, align the definitions.** Smallest change: reword the texts that say
   "reproducibility" to say "precision", since the scope word already carries the axis.
2. **Rename to the standard terms** — `Within-Session Repeatability`,
   `Between-Session Reproducibility`, `Analytical Trueness` — and align the texts.
   Clearest to a metrologist, but renames fields many techniques populate.
3. **Keep both**, naming the standard term in the text as a parenthetical: "Precision
   under changed conditions (reproducibility, ISO 5725)". No rename, no ambiguity.
4. **Leave as is.** Cheapest, and it keeps a label whose name and definition disagree.

Option 3 is the recommendation if renaming is unattractive: it makes the intent citable
without touching any field name. Option 1 alone would resolve the inconsistency but leave
the reader to infer which axis each label means.

## Status in geochemBuildingBlocks

Nothing is blocked. The variable-registry prototype resolves
`Between-Session (Long-Term) Analytical Precision and Assessment Method` and
`Analytical Accuracy and Assessment Method` to one variable each (both accepted,
`docs/variable_registry_decisions.json`) — the conflicts there were wording, not this
question. Whichever way this is answered changes the definitions, not the variable count.
