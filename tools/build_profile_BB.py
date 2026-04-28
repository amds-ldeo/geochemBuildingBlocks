"""Scaffold a profiles/geochemProfiles/<short>Profile/ building block referencing
the existing detail BB and TAPP definition.

Usage:
    python tools/build_profile_BB.py [TAPP_NAME]

Defaults: empaTAPP. The script derives:
    short = TAPP_NAME without the trailing "TAPP"  (e.g. "empa", "xrd")
    profile dir = _sources/profiles/geochemProfiles/<short>Profile/

Files only scaffolded when missing — re-runs are no-ops once the user starts
editing. The schema.yaml extends adaProduct with a schema:measurementTechnique
anyOf pointing at the TAPP (by @id ref or inline) plus a
schema:distribution.schema:hasPart anyOf that lets detailXXX appear.
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
                        help="TAPP name (e.g. empaTAPP, xrdTAPP). Default: empaTAPP.")
    args = parser.parse_args()
    _tapp_lib.configure(args.tapp_name)
    _tapp_lib.build_profile_BB()


if __name__ == "__main__":
    main()
