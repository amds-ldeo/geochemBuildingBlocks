#!/usr/bin/env python3
"""Assert that vocabulary references resolve, and that they do not silently disappear.

This gate exists because of a measured incident. `schema:inDefinedTermSet` is the annotation that
links a parameter or keyed-table column to the controlled vocabulary its values come from. It was
emitted exactly once in this repo's history, on four EPMA target-species columns:

    05d0bc4d4b  2026-09-14  "Rename channel -> monitoredProperty ..."   +4
    8c601ccb4f  2026-10-03  "Regenerate for the EPMA rename"            -4

One commit renamed the `$defs` and dropped the annotation in the same run, because
`build_tapp.route()` passed a literal `None` for `enum_vname` where the legacy path passed
`vocab_for(enum)`. It went unnoticed for 25 days with every required check green, and it is
structurally invisible to all of them:

  * `constraint_census.py` counts what RESTRICTS -- required names, enum members, const, pattern,
    bounds. An annotation restricts nothing, so the census cannot see one arrive or leave.
  * `validate_examples.py` only gets LOOSER when an annotation disappears, so no corpus of
    positive examples can fail.
  * `audit_building_blocks.py` checks files and schema/JSON consistency, not annotation coverage.

So this asserts the two things that cannot be inferred from any of them.

CHECK A -- NO DANGLING REFERENCE. Every `ada:vocab/...` identifier cited anywhere under
`_sources/` must resolve to a scheme actually on disk. This matters more after the 2026-10-28
consolidation than before it: the per-technique schemes `ada:vocab/<TAPP>/<field>` are gone, so
re-emitting the old form would produce an annotation pointing at nothing -- which is WORSE than the
absence, because a dangling reference looks like working wiring. A consumer resolves the @id, not
the file, so nothing else in the repo would complain.

CHECK B -- THE COUNT DOES NOT DROP. Per-file `schema:inDefinedTermSet` counts against
docs/vocab_reference_census.json. Arrival needs its own count, per artifact, exactly as the
property-title work established: an unchanged constraint census is good evidence a change is
annotation-only and is structurally unable to show the annotation is still there.

    python tools/check_vocab_references.py            # check; exit 1 on a regression
    python tools/check_vocab_references.py --write     # accept current counts as the baseline
"""
import argparse
import collections
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCES = os.path.join(ROOT, "_sources")
VOCAB = os.path.join(SOURCES, "registry", "vocab")
CENSUS = os.path.join(ROOT, "docs", "vocab_reference_census.json")

# A bare `ada:vocab/x` and `ada:vocab/x/y` are both legal: a scheme and a concept within it.
TOKEN = re.compile(r"ada:vocab/[A-Za-z0-9_/.\-]*")
ANNOTATION = "schema:inDefinedTermSet"
READ = (".yaml", ".yml", ".json", ".md")


def schemes_on_disk():
    out = {}
    for path in sorted(glob.glob(os.path.join(VOCAB, "*.json"))):
        try:
            with open(path, encoding="utf-8") as f:
                doc = json.load(f)
        except (OSError, ValueError) as e:
            print("FAIL  unreadable vocabulary: %s (%s)" % (os.path.basename(path), e))
            continue
        sid = doc.get("@id")
        if sid:
            out[sid] = {c.get("@id") for c in (doc.get("skos:hasTopConcept") or [])
                        if isinstance(c, dict)}
    return out


def scan():
    """(citations {token: [relpaths]}, annotation counts {relpath: n}), excluding registry/vocab."""
    citations = collections.defaultdict(list)
    counts = {}
    for dirpath, dirnames, filenames in os.walk(SOURCES):
        dirnames[:] = [d for d in dirnames if d != "__pycache__"]
        if os.path.normpath(dirpath) == os.path.normpath(VOCAB):
            dirnames[:] = []
            continue
        for fn in sorted(filenames):
            if not fn.endswith(READ):
                continue
            path = os.path.join(dirpath, fn)
            rel = os.path.relpath(path, ROOT).replace("\\", "/")
            try:
                text = open(path, encoding="utf-8", errors="replace").read()
            except OSError:
                continue
            for tok in TOKEN.findall(text):
                if rel not in citations[tok]:
                    citations[tok].append(rel)
            n = text.count(ANNOTATION)
            if n:
                counts[rel] = n
    return citations, counts


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--write", action="store_true",
                    help="accept the current annotation counts as the baseline")
    args = ap.parse_args()

    schemes = schemes_on_disk()
    concepts = {c for cs in schemes.values() for c in cs}
    citations, counts = scan()
    failures = []

    # --- Check A: every cited identifier resolves ---------------------------------------
    dangling = {t: f for t, f in sorted(citations.items())
                if t not in schemes and t not in concepts}
    print("CHECK A  vocabulary references resolve")
    print("  schemes on disk              : %d (%d concepts)" % (len(schemes), len(concepts)))
    print("  distinct ada:vocab/ cited    : %d" % len(citations))
    print("  DANGLING                     : %d" % len(dangling))
    for tok, files in dangling.items():
        failures.append("dangling %s (cited by %d file(s), e.g. %s)"
                        % (tok, len(files), files[0]))
        print("     %-52s <- %d file(s), e.g. %s" % (tok, len(files), files[0]))
    if not dangling:
        for tok, files in sorted(citations.items(), key=lambda kv: -len(kv[1])):
            print("     OK %-49s %5d file(s)" % (tok, len(files)))

    # --- Check B: the annotation count has not dropped ---------------------------------
    total = sum(counts.values())
    print("\nCHECK B  %s coverage" % ANNOTATION)
    print("  files carrying it            : %d" % len(counts))
    print("  occurrences                  : %d" % total)

    if args.write:
        with open(CENSUS, "w", encoding="utf-8", newline="\n") as f:
            json.dump({"$comment": [
                "Per-file schema:inDefinedTermSet counts. Asserted by "
                "tools/check_vocab_references.py because no other gate can see this annotation: "
                "the constraint census counts only what restricts, and examples get looser when "
                "an annotation disappears. Four of these vanished unnoticed for 25 days in "
                "8c601ccb4f. Regenerate, then --write and commit in the same PR."],
                "total": total, "files": counts}, f, indent=2, sort_keys=True)
            f.write("\n")
        print("  wrote baseline               : %s" % os.path.relpath(CENSUS, ROOT))
    elif not os.path.exists(CENSUS):
        print("  no baseline yet; run --write once the annotation is emitted")
    else:
        with open(CENSUS, encoding="utf-8") as f:
            base = json.load(f)
        prev = base.get("files") or {}
        lost = {k: v for k, v in sorted(prev.items()) if counts.get(k, 0) < v}
        gained = {k: v for k, v in sorted(counts.items()) if v > prev.get(k, 0)}
        print("  baseline occurrences         : %d" % base.get("total", 0))
        for k, v in lost.items():
            failures.append("%s lost annotations: %d -> %d" % (k, v, counts.get(k, 0)))
            print("     LOST   %-58s %d -> %d" % (k, v, counts.get(k, 0)))
        for k, v in gained.items():
            print("     gained %-58s %d -> %d" % (k, prev.get(k, 0), v))
        if gained and not lost:
            print("  (gains are not failures; --write to accept them)")

    print()
    if failures:
        print("FAILED (%d):" % len(failures))
        for f_ in failures:
            print("  - %s" % f_)
        return 1
    print("vocabulary references OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
