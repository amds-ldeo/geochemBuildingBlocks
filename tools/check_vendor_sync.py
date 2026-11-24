"""Fail when the vendored upstream copies disagree with their locks, or with each other.

Two directories hold copies of someone else's files:

    vendor/remote/   CDIF's schemas, pinned by vendor/remote-lock.json
                     (refreshed by resolve_schema.py --all --refresh-remote)
    vendor/shapes/   CDIF's rules.shacl, pinned by vendor/shapes-lock.json
                     (refreshed by validate_examples.py --refresh-shapes)

Both pin by URL, and the URLs name an immutable git TAG, so there is no silent upstream
drift: re-fetching the same tag is a no-op by definition. The hazards are the other two.

ONE. The two locks are refreshed by DIFFERENT COMMANDS, so nothing stops one being bumped
to a newer snapshot and the other left behind. You would then validate examples against one
revision's shapes and another revision's schemas, and no check in this repository would
notice: `regenerate.py` does not touch `vendor/`, so `Regenerate and diff` -- the gate that
catches every other stale artifact -- is structurally blind to it.

TWO. Nothing verifies a vendored file still matches the sha256 its lock recorded. Only a
re-fetch compares them, and a re-fetch needs the network, so a hand-edit or a half-finished
refresh survives indefinitely. CLAUDE.md already records the related trap for schemas: a
relative $ref INSIDE vendor/remote is read off disk and never re-fetched, so a vendored file
can stay stale through --refresh-remote and you have to delete it to force the miss.

Both checks are offline and take under a second, which is why they can sit in a required
workflow.

    python tools/check_vendor_sync.py
"""
import hashlib
import io
import json
import os
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

REPO_ROOT = Path(__file__).resolve().parent.parent
VENDOR = REPO_ROOT / "vendor"

# (lock file, directory its URLs were written into, what refreshes it)
PAIRS = [
    (VENDOR / "remote-lock.json", VENDOR / "remote",
     "resolve_schema.py --all --refresh-remote"),
    (VENDOR / "shapes-lock.json", VENDOR / "shapes",
     "validate_examples.py --refresh-shapes"),
]

# .../<org>/<repo>/refs/tags/<tag>/...  or  .../refs/heads/<branch>/...
REVISION = re.compile(r"/refs/(tags|heads)/([^/]+)/")


def revision_of(url):
    m = REVISION.search(url)
    return "%s/%s" % (m.group(1), m.group(2)) if m else None


def local_path(root, url):
    parsed = urlparse(url)
    return root / parsed.netloc / parsed.path.strip("/")


def opener(path):
    r"""`path` in a form Windows will actually open.

    The vendored tree nests the netloc, the org, the repo, `refs/tags/<tag>` and the
    upstream `_sources/...` path under vendor/, and the longest of those reaches EXACTLY
    260 characters -- Windows MAX_PATH. Python's os.stat then reports the file as absent
    while Git Bash lists it happily, so a present file reads as missing:

        vendor/remote/.../cdifConceptOrTermOrString/cdifConceptOrTermOrStringSchema.json
        len 260, exists() False, 598 bytes on disk

    The `\\?\` prefix opts out of MAX_PATH per call, which works regardless of the
    machine's LongPathsEnabled setting. CI runs on ubuntu-latest and never sees this, so a
    check that omits it passes in CI and fails only on a maintainer's Windows box -- the
    worst split for a gate to have.
    """
    s = str(path)
    if os.name == "nt" and not s.startswith("\\\\?\\"):
        return "\\\\?\\" + os.path.abspath(s)
    return s


def main():
    problems = []
    revisions = {}
    present = 0

    for lock_path, root, refresher in PAIRS:
        label = lock_path.name
        if not lock_path.exists():
            # Not an error. vendor/shapes-lock.json is absent until someone vendors the
            # shapes, and validate_examples says so on its own line every run.
            print("  %-20s absent (nothing vendored; refresh with %s)"
                  % (label, refresher))
            continue
        try:
            lock = json.loads(lock_path.read_text(encoding="utf-8"))
        except ValueError as ex:
            problems.append("%s is not valid JSON: %s" % (label, ex))
            continue

        revs, missing, mismatched = set(), 0, 0
        for url, meta in sorted(lock.items()):
            rev = revision_of(url)
            if rev is None:
                problems.append("%s: %s names no refs/tags/ or refs/heads/ revision, so "
                                "what it is pinned to cannot be established" % (label, url))
            else:
                revs.add(rev)
            path = local_path(root, url)
            if not os.path.exists(opener(path)):
                missing += 1
                problems.append("%s: %s is in the lock but not on disk (re-run %s)"
                                % (label, path.relative_to(REPO_ROOT), refresher))
                continue
            present += 1
            blob = io.open(opener(path), "rb").read()
            want = meta.get("sha256")
            if want and hashlib.sha256(blob).hexdigest() != want:
                mismatched += 1
                problems.append(
                    "%s: %s does not match its recorded sha256. It was hand-edited, or a "
                    "refresh did not finish. Re-run %s"
                    % (label, path.relative_to(REPO_ROOT), refresher))
            elif meta.get("bytes") is not None and len(blob) != meta["bytes"]:
                mismatched += 1
                problems.append("%s: %s is %d bytes, lock says %d"
                                % (label, path.relative_to(REPO_ROOT), len(blob),
                                   meta["bytes"]))

        if len(revs) > 1:
            problems.append("%s pins MORE THAN ONE upstream revision: %s. A single lock "
                            "must name one snapshot, or what the vendored copies represent "
                            "is undefined" % (label, ", ".join(sorted(revs))))
        if revs:
            revisions[label] = revs
        print("  %-20s %4d url(s), %d on disk verified, revision %s"
              % (label, len(lock), len(lock) - missing - mismatched,
                 ", ".join(sorted(revs)) or "?"))

    # The cross-lock check: every lock that pins anything must pin the SAME revision.
    all_revs = set()
    for revs in revisions.values():
        all_revs |= revs
    if len(all_revs) > 1:
        detail = "; ".join("%s -> %s" % (k, ", ".join(sorted(v)))
                           for k, v in sorted(revisions.items()))
        problems.append(
            "the vendor locks pin DIFFERENT upstream revisions (%s). The schemas and the "
            "shapes would then come from different snapshots, which nothing else here can "
            "see: regenerate.py does not touch vendor/, so Regenerate and diff cannot "
            "catch it. Bump both, or neither." % detail)

    print()
    if problems:
        print("FAIL: %d problem(s)" % len(problems), file=sys.stderr)
        for p in problems:
            print("  - %s" % p, file=sys.stderr)
        return 1
    if not revisions:
        print("nothing vendored, so nothing to check.")
        return 0
    print("vendored copies agree with their locks, and both locks pin %s."
          % ", ".join(sorted(all_revs)))
    print("%d file(s) verified by sha256." % present)
    return 0


if __name__ == "__main__":
    sys.exit(main())
