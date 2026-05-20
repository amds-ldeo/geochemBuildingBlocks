"""Generate the per-dataset PropertyValue parameter registry for a detail<XXX>
building block from a TAPP_<technique>_filled.xlsx spreadsheet.

Usage:
    python tools/build_detail_BB.py [TAPP_NAME] [XLSX_PATH]

Defaults: empaTAPP / docs/TAPP_EPMA_filled.xlsx → writes the registered
parameterValues collection BB at
_sources/techniqueProtocols/parameterValues/schema.yaml (one $def per
readOnly:false parameter, keyed by name) plus its bblock.json.

The detail BB's own schema.yaml is hand-authored (componentType enum,
spectrometersUsed, signalUsed, schema:measurementTechnique anyOf-link to the
TAPP definition) and is NOT regenerated here. Its allOf carries the per-dataset
schema:additionalProperty constraint INLINE, referencing the parameterValues
registry $defs via fragment $refs
(../../techniqueProtocols/parameterValues/schema.yaml#/$defs/<name>) so they
resolve locally through the building-block register. This tool also cleans up
the legacy generated parametersConstraint.yaml if a stale copy remains.
"""
from __future__ import annotations
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _tapp_lib  # noqa: E402


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n", 1)[0])
    parser.add_argument("tapp_name", nargs="?", default="empaTAPP",
                        help="TAPP name (e.g. empaTAPP). Default: empaTAPP.")
    parser.add_argument("xlsx", nargs="?", default="docs/TAPP_EPMA_filled.xlsx",
                        help="Path to the filled TAPP spreadsheet. Default: docs/TAPP_EPMA_filled.xlsx.")
    parser.add_argument("--pub", action="append",
                        help="Only regen examples for these publication codes (e.g. --pub P0). "
                             "Repeat for multiple. Schema/catalog artifacts always rebuild.")
    args = parser.parse_args()
    _tapp_lib.configure(args.tapp_name, args.xlsx)
    _tapp_lib.build_detail_artifacts(pub_filter=args.pub)


if __name__ == "__main__":
    main()
