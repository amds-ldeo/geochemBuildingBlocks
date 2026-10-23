# TAPP issue draft: Purpose texts cite sections by bare number

For filing in [amds-ldeo/tapp](https://github.com/amds-ldeo/tapp). Not yet filed.
Raised 2026-10-23. Separate from `tapp-dangling-cross-references.md`: these references all
**resolve**, they are just unreadable away from the workbook.

## The observation

252 Purpose texts point the reader at another part of the workbook by section number —
"also recorded in the **Group 1** coupling fields", "documented in **Group 3** and
**Group 4**". The numbers refer to the workbooks' own section header rows, which carry a
string in `Metadata Item` and nothing else:

| | |
|---|---|
| 1. Procedure Identification | 4. Measurement Information |
| 2. Samples | 5. Data Processing |
| 3. Instrument & Software | 6. Quality Control & Uncertainty |

Measured across all 61 workbooks: **sections 1–6 are identical in every one.** Section 7
exists in exactly two (`EBSD Acquisition and Indexing`, `STEM Acquisition`) and is
technique-specific — but no Purpose text cites a Group 7, or a Group 5, so all 252
references resolve against the universal six.

Distribution: Group 1 ×116, Group 2 ×61, Group 6 ×63, Group 3 ×10, Group 4 ×2. Three
labels account for most of it — `Pre-Analysis Imaging and Screening` (116),
`Constants and Reference Values Used` (61) and
`Coupled Dataset or Publication Reference` (61).

## Why it is worth fixing at source

A bare number means nothing to a reader who does not have the workbook in front of them,
and the Purpose texts are the definitions these fields carry everywhere downstream — into
generated schema descriptions, into the ADA registry, and into any variable registry built
from them. "Recorded in the Group 1 coupling fields" tells such a reader only that
something exists somewhere.

The section names are stable enough to rely on, which is what makes substitution safe:
identical across 61 workbooks for every number actually cited.

## Options

1. **Substitute the section name in the Purpose text** — "also recorded in the Procedure
   Identification coupling fields". Self-describing, no structural change, and the numbers
   stay in the header rows where they belong. Recommended.
2. **Name the section and keep the number** — "in Procedure Identification (Group 1)".
   Preserves the shorthand for anyone navigating the sheet.
3. **Cite the FIELD rather than the section**, where one specific field is meant. Most
   precise, but several of these references genuinely mean "that group of fields" rather
   than one row, so it will not always apply.
4. **Leave as is.** The references resolve for anyone with the workbook; everyone else
   reads a dead number.

Option 1 unless the shorthand is actively used when editing, in which case option 2.

## Status in geochemBuildingBlocks

Already handled downstream, so nothing is blocked: `tools/draft_variable_registry.py`
substitutes the section name when it loads a definition
(`resolve_group_refs`, `_SECTIONS` derived from the workbooks), and 0 `Group N` strings
remain in the emitted draft. That fix lives in the consumer, though — the workbook text
still carries bare numbers for every other reader.
