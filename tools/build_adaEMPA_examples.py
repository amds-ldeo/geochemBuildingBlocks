"""Build adaEMPA profile-level dataset examples from paired empaTAPP+detailEMPA
example files.

For each publication with both an exampleempaTAPP-<pub>.json and an
exampledetailEMPA-<pub>.json on disk, emits exampleadaEMPA-<pub>.json under
_sources/profiles/adaProfiles/adaEMPA/. The resulting Dataset:

  - derives schema:variableMeasured from the TAPP's ada:defaultAnalytes
  - carries the detailEMPA fields on a single tabular hasPart
  - references the TAPP definition via schema:measurementTechnique on that
    hasPart (@id reference, not inline)
  - inserts synthetic placeholders (DOI, file size, checksum, dates) that
    authors can override per-pub when ready to publish

Run from repo root:
    python tools/build_adaEMPA_examples.py            # all pubs with paired files
    python tools/build_adaEMPA_examples.py --pub P1 --pub P5  # specific pubs
"""
from __future__ import annotations
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _tapp_lib as L


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--tapp", default="empaTAPP", help="TAPP name (default empaTAPP)")
    p.add_argument("--xlsx", default=None, help="Path to TAPP spreadsheet (informational)")
    p.add_argument("--pub", action="append", default=None,
                   help="Restrict to specific pub code(s); repeat for multiple")
    args = p.parse_args()

    L.configure(args.tapp, args.xlsx)
    counts = L.build_profile_examples(pub_filter=args.pub)
    print(f"adaEMPA profile examples: wrote {counts['written']}, skipped {counts['skipped']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
