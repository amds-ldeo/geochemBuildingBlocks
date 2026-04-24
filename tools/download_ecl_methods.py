#!/usr/bin/env python3
"""
Download analytical method Excel workbooks from the EarthChem Library.

Reads the methods list CSV (exported from Google Sheets), fetches each
ECL record page to discover the download filename, then POSTs to dl_multi.php
to retrieve the actual Excel file.

Usage:
    python tools/download_ecl_methods.py
    python tools/download_ecl_methods.py --output-dir /some/other/path
    python tools/download_ecl_methods.py --dry-run
"""

import argparse
import csv
import os
import re
import sys
import time
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from urllib.error import URLError, HTTPError

ECL_VIEW_URL = "https://ecl.earthchem.org/view.php?id={id}"
ECL_DOWNLOAD_URL = "https://ecl.earthchem.org/dl_multi.php"
SPREADSHEET_CSV_URL = (
    "https://docs.google.com/spreadsheets/d/"
    "1TwWgk2_gNANyjpRoVRHtdB6BS2q7fHeWLIg0CQU051Q/export?format=csv"
)

DEFAULT_OUTPUT_DIR = Path("G:/My Drive/OneGeochemistry/AnalyticalMethodTemplates")


def fetch_csv_rows(url: str) -> list[dict]:
    """Fetch the Google Sheets CSV and return rows as dicts."""
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(req, timeout=30) as resp:
        text = resp.read().decode("utf-8")
    reader = csv.DictReader(text.splitlines())
    return [row for row in reader if row.get("ID", "").strip()]


def get_filenames_from_page(ecl_id: str) -> list[str]:
    """Scrape the ECL view page to find download filenames."""
    url = ECL_VIEW_URL.format(id=ecl_id)
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urlopen(req, timeout=30) as resp:
            html = resp.read().decode("utf-8", errors="replace")
    except (URLError, HTTPError) as e:
        print(f"  WARNING: Could not fetch page for ID {ecl_id}: {e}", file=sys.stderr)
        return []

    if "non-existent or not yet approved" in html:
        return []

    # Extract filenames from hidden input fields
    return re.findall(r'name="filename"\s+value="([^"]+)"', html)


def download_file(ecl_id: str, filename: str, output_dir: Path) -> bool:
    """POST to dl_multi.php to download a file. Returns True on success."""
    data = urlencode({
        "id": ecl_id,
        "verifySubmit": "yes",
        "system": "ec",
        "filename": filename,
        "dlFormat": "single",
    }).encode("utf-8")

    req = Request(
        ECL_DOWNLOAD_URL,
        data=data,
        headers={
            "User-Agent": "Mozilla/5.0",
            "Content-Type": "application/x-www-form-urlencoded",
        },
    )

    try:
        with urlopen(req, timeout=60) as resp:
            content = resp.read()
            if len(content) < 100:
                print(f"  WARNING: Suspiciously small file ({len(content)} bytes) for {filename}")
                return False

            out_path = output_dir / filename
            out_path.write_bytes(content)
            print(f"  OK: {filename} ({len(content):,} bytes)")
            return True
    except (URLError, HTTPError) as e:
        print(f"  ERROR downloading {filename}: {e}", file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(description="Download ECL method workbooks")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--dry-run", action="store_true", help="List files without downloading")
    parser.add_argument("--delay", type=float, default=1.0, help="Seconds between requests")
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)

    print("Fetching methods list from Google Sheets...")
    rows = fetch_csv_rows(SPREADSHEET_CSV_URL)
    # Filter out any header-like rows
    rows = [r for r in rows if r.get("ID", "").strip().isdigit()]
    print(f"Found {len(rows)} method entries\n")

    downloaded = 0
    skipped = 0
    failed = 0
    not_approved = 0

    for row in rows:
        ecl_id = row["ID"].strip()
        title = row.get("MethodTitle", row.get("title", "")).strip()
        print(f"[{ecl_id}] {title[:80]}")

        # Check if already downloaded
        existing = list(args.output_dir.glob(f"{ecl_id}-*"))
        if existing:
            print(f"  SKIP: already have {existing[0].name}")
            skipped += 1
            continue

        filenames = get_filenames_from_page(ecl_id)
        if not filenames:
            print(f"  SKIP: not approved or no files found")
            not_approved += 1
            continue

        if args.dry_run:
            for fn in filenames:
                print(f"  WOULD DOWNLOAD: {fn}")
            continue

        for fn in filenames:
            if download_file(ecl_id, fn, args.output_dir):
                downloaded += 1
            else:
                failed += 1

        time.sleep(args.delay)

    print(f"\nDone: {downloaded} downloaded, {skipped} skipped (existing), "
          f"{not_approved} not approved, {failed} failed")


if __name__ == "__main__":
    main()
