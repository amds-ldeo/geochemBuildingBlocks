#!/usr/bin/env python3
"""Read a TAPP source table, whichever format it is in.

The library moved from xlsx to CSV with the 2026-08-11 delivery, and the delivery README is
explicit that the CSV is the source of truth and the xlsx a generated artifact that should not be
parsed for content. The path-driven pipeline had three separate readers, each opening the workbook
with openpyxl and re-deriving the header layout — so switching source format meant changing the
same logic three times, in three slightly different forms.

This is the one primitive they all actually wanted: the TAPP sheet as a list of row tuples, header
first. Everything above it — locating columns, skipping group headers, finding the mode block —
stays where it was.

CSV rows are normalised to look exactly like openpyxl's: padded to the header width, and empty
cells returned as None rather than ''. Callers already treat both as absent (build_tapp.norm maps
each to ""), but matching openpyxl exactly means a reader cannot behave differently on one format
than the other.

Encoding is utf-8-sig: the library's CSVs carry a BOM, and their content includes superscripts and
Greek that must survive (²⁰⁶Pb/²³⁸U, δ⁵⁶Fe, J cm⁻²).
"""
import csv
import os
import sys


def rows(path):
    """The TAPP table as a list of row tuples, header first. Accepts .csv or .xlsx."""
    if str(path).lower().endswith(".csv"):
        with open(path, newline="", encoding="utf-8-sig") as f:
            raw = [list(r) for r in csv.reader(f)]
        if not raw:
            return []
        width = len(raw[0])
        return [tuple((c if c != "" else None) for c in (r + [""] * (width - len(r)))[:width])
                for r in raw]

    import openpyxl
    wb = openpyxl.load_workbook(path, data_only=True, read_only=True)
    sheet = "TAPP" if "TAPP" in wb.sheetnames else wb.sheetnames[0]
    out = list(wb[sheet].iter_rows(values_only=True))
    wb.close()
    return out


def exists(path):
    return bool(path) and os.path.exists(path)


_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# The canonical TAPP source library is the `tapp/` git submodule (amds-ldeo/tapp), whose root holds
# the delivery contents directly (Current TAPPs/, Claude Skills for TAPP/, composed_tapps.json) —
# no TAPPS<date>/ wrapper. The older inline TAPPS<date>/ drops are kept only as a fallback, and
# reaching one is now a REFUSAL rather than a quiet substitution -- see require_delivery().
_TAPP_SUBMODULE = os.path.join(_ROOT, "tapp")


def _is_delivery(path):
    """True if `path` looks like a TAPP delivery (has the tables and/or the manifest)."""
    return os.path.isdir(os.path.join(path, "Current TAPPs")) or \
        os.path.exists(os.path.join(path, "composed_tapps.json"))


#: Deliberate override for the refusal below, mirroring resolve_schema.py's --allow-unresolved.
ESCAPE_VAR = "ADA_ALLOW_STALE_TAPP_DROP"

_STALE_MSG = """\
The `tapp/` submodule is EMPTY, so the TAPP source would fall back to the superseded inline
drop {drop}/ and everything built in this run would come from a STALE table.

Nothing downstream can tell you that happened. Building from the wrong source only changes
CONTENT, and a schema with less in it is more permissive rather than invalid -- so
validate_examples stays green over it. The module stages are the dangerous ones: {drop}/ ships
Module_ArAr and Module_Group1, both retired upstream, and simplify_sidecars BLANKS a technique
row when it decides a module covers the field.

.gitmodules sets `update = none` for this submodule, so a fresh clone AND a fresh git worktree
both leave it registered but empty. Populate it:

    git submodule update --init --checkout tapp

The `--checkout` is required: `--recursive` and actions/checkout's `submodules: true` both honour
`update = none` and leave it empty. `update = none` is itself load-bearing -- it stops OGC's
postprocess from running `git submodule update --remote` and COMMITTING a bumped pointer, as it
did in c0194f7e4.

To build from the inline drop deliberately anyway, set {escape}=1."""

_WARNED = False


def _inline_drops():
    return sorted(d for d in os.listdir(_ROOT)
                  if d.startswith("TAPPS") and os.path.isdir(os.path.join(_ROOT, d)))


class StaleDeliveryError(RuntimeError):
    """The submodule is unpopulated and the only alternative is a superseded inline drop."""


def require_delivery():
    """Refuse to resolve the TAPP source to a superseded inline drop.

    The fallback below was silent, and on 2026-10-15 a fresh `.claude/worktrees/` worktree on main
    held 0 files under `tapp/Current TAPPs/` while `current_delivery()` happily returned
    `TAPPS20260813`. A regeneration from there would have been built from the wrong tables and
    reported 647/647 examples valid, for the reason in docs/SILENT_SUCCESS.md #1.

    Silent only when there is nothing stale to fall into: with no inline drop at all the caller's
    own missing-file error names the exact table and is clearer than this one.
    """
    global _WARNED
    if _is_delivery(_TAPP_SUBMODULE):
        return
    drops = _inline_drops()
    if not drops:
        return
    if os.environ.get(ESCAPE_VAR):
        if not _WARNED:
            _WARNED = True
            print(f"WARNING: {ESCAPE_VAR} is set, so the TAPP source is the superseded inline "
                  f"drop {drops[-1]}/ and not the pinned `tapp/` submodule.", file=sys.stderr)
        return
    raise StaleDeliveryError(_STALE_MSG.format(drop=drops[-1], escape=ESCAPE_VAR))


def current_delivery():
    """The TAPP source library.

    Prefers the `tapp/` submodule (amds-ldeo/tapp) — the canonical source going forward, version
    pinned by the submodule commit. Falls back to the newest inline TAPPS<date>/ folder for a repo
    that still carries a drop inline (deliveries are dated, so the latest name is the latest drop).

    Derived rather than hard-coded because three separate tools once pinned TAPPS20260811 in their
    own constants and silently read a superseded delivery after the next drop.

    RAISES StaleDeliveryError rather than taking that fallback when the submodule is unpopulated,
    because an unpopulated submodule is the normal state of a fresh clone or worktree and the
    substitution was invisible. `ADA_ALLOW_STALE_TAPP_DROP=1` takes it deliberately.
    """
    if _is_delivery(_TAPP_SUBMODULE):
        return _TAPP_SUBMODULE
    require_delivery()
    ds = _inline_drops()
    return os.path.join(_ROOT, ds[-1]) if ds else _ROOT


def manifest_path():
    """The composed_tapps.json to use, or None.

    Prefers the submodule's manifest, then the newest across any inline TAPPS<date>/ folders. Not
    simply `current_delivery()/composed_tapps.json`: some drops shipped without a manifest, so
    anything that assumed the current delivery has one crashed outright. The composition declaration
    changes far less often than the tables, so falling back to the most recent one is better than
    failing — as long as the caller says which delivery it came from.
    """
    sub = os.path.join(_TAPP_SUBMODULE, "composed_tapps.json")
    if os.path.exists(sub):
        return sub
    # Its own scan, so it needs the refusal in its own right -- reaching an inline manifest while
    # the submodule is empty is the same stale-source bug as current_delivery()'s fallback.
    require_delivery()
    for d in sorted((x for x in os.listdir(_ROOT) if x.startswith("TAPPS")), reverse=True):
        p = os.path.join(_ROOT, d, "composed_tapps.json")
        if os.path.exists(p):
            return p
    return None


def modules_dir():
    """The authoritative modules folder: <newest delivery>/Claude Skills for TAPP/modules.

    Confirmed by Stephen as the source of truth for both the module CSVs and their sidecars — the
    2026-08-13 drop also ships copies under references/modules/, which are NOT authoritative.
    """
    return os.path.join(current_delivery(), "Claude Skills for TAPP", "modules")
