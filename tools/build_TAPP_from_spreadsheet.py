"""Generate a TAPP building block (and its shared analyteColumns/parameterTemplates/
vocab catalog entries) from a TAPP_<technique>_filled.xlsx spreadsheet.

Usage:
    python tools/build_TAPP_from_spreadsheet.py [TAPP_NAME] [XLSX_PATH]

Defaults: empaTAPP / docs/TAPP_EPMA_filled.xlsx (matches the legacy behaviour
of build_empaTAPP_from_spreadsheet.py).

For a new TAPP (e.g. xrdTAPP), clone the spreadsheet template, fill it in,
and run:
    python tools/build_TAPP_from_spreadsheet.py xrdTAPP docs/TAPP_XRD_filled.xlsx

The script writes catalog files into the shared dirs at
_sources/techniqueProtocols/{analyteColumns,parameterTemplates,vocab}/ — if a
catalog file already exists with content owned by another TAPP, this script
shares (no-op when content matches) or errors (when content conflicts) per
the share_or_write_catalog rules in tools/_tapp_lib.py. Use
tools/build_detail_BB.py to generate the corresponding detail BB and
parameterValues entries.
"""
from __future__ import annotations
import argparse
import sys
from pathlib import Path

# Allow running from repo root or anywhere — make sibling import work.
sys.path.insert(0, str(Path(__file__).resolve().parent))
import _tapp_lib  # noqa: E402


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n", 1)[0])
    parser.add_argument("tapp_name", nargs="?", default="empaTAPP",
                        help="TAPP name (e.g. empaTAPP, xrdTAPP). Default: empaTAPP.")
    parser.add_argument("xlsx", nargs="?", default="docs/TAPP_EPMA_filled.xlsx",
                        help="Path to the filled TAPP spreadsheet (relative to repo root or absolute). Default: docs/TAPP_EPMA_filled.xlsx.")
    args = parser.parse_args()
    _tapp_lib.configure(args.tapp_name, args.xlsx)
    _tapp_lib.build_tapp_artifacts()


if __name__ == "__main__":
    main()
