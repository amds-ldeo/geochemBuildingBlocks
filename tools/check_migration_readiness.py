"""Per technique: could the TAPP profile replace the legacy profile its records declare?

Every ADA record declares its profiles at `schema:subjectOf.dcterms:conformsTo` -- 7,447 of
7,447, 36 distinct cids. A *cid* is the conformance-class identifier, the last segment of a
profile URI: a record asserting `https://w3id.org/geochem/metadata/profiles/adaSEM` declares the
cid `adaSEM`. It is the same string a block pins in its `contains` const and the same one
`build_profile.PROFILES` carries as `cid=`, so one cid is meant to name exactly one schema.

Of the 36, two (`adaProduct`, `geochemProduct`) are base products every record declares, and the
other 34 name a LEGACY `*/profile-ada` block. Only 8 of those 34 have a TAPP-based
`geochemProfile/<TECH>/profile` to be superseded BY; the remaining 26, all under `adaProfile/`
and covering 965 records, have no replacement at all, so for them the question cannot yet be
asked. That is itself the answer for them, and the report lists them.

Measured 2026-10-15 over `ada_subjects`, for the 8 that do have a replacement: 100% of records
validate against the profile they declare and 0% against the replacement. The cause is NOT a
missing TAPP reference -- `prov:used` is present on these records, carrying the instrument. It
is required properties the records do not have, and the gap divides sharply:

  XANES, XRD, QRIS, RAMAN  `schema:variableMeasured` is an empty array and the profile
                           requires it to contain a matching variable. That is genuinely
                           absent content -- which variables were measured -- not a
                           labelling mismatch, so it cannot be relaxed away.
  SEM, TEM, EPMA, VNMIR    that, plus per-analysis detail a SAMIS-era submission never
                           supplied: `ada:edsDeadTime`, `ada:proceduralBlankLevel`,
                           `schema:actionProcess`, `ada:mapDimensions`, `ada:voxelSize`.

A ninth blocker was removed rather than reported: all 8 also failed on
`prov:wasGeneratedBy[].schema:object[].schema:name`, and for the first four that was the ONLY
failure. The records name the sample with `schema:identifier` ("OREX-803031-101") and carry no
separate laboratory name, so the information was present under another key. `schema_path_emitter
.SUBSTITUTES` now lets the identifier satisfy the name, scoped to `schema:object`.

So a legacy declaration is not redundant today; it is the only profile those records satisfy.
The decision recorded alongside this tool is to KEEP BOTH until the records are enriched, per
technique, from method descriptions and instrument metadata.

This is therefore a REPORT, not a gate: it always exits 0 and is not wired into CI. It cannot
be -- it needs a database, and psycopg2 is kept in requirements-db.txt precisely so schema work
never depends on a driver. Run it when you want to know whether a technique has become
migratable.

A technique reads READY when the TAPP profile accepts every sampled record that declares its
legacy partner. Then, and only then, is dropping the legacy declaration safe for that technique.

    python tools/check_migration_readiness.py                  # all techniques, 40 records each
    python tools/check_migration_readiness.py --cap 200        # more records per technique
    python tools/check_migration_readiness.py --tech SEM TEM   # just these
"""
import argparse
import collections
import glob
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "_sources")
sys.path.insert(0, os.path.join(ROOT, "tools"))

CID = re.compile(r"https://w3id\.org/geochem/metadata/profiles/([A-Za-z0-9_-]+)")


def cid_to_blocks():
    """{cid: {block, ...}} read from the sources, so nothing is hardcoded."""
    out = collections.defaultdict(set)
    for path in glob.glob(os.path.join(SRC, "**", "schema.yaml"), recursive=True):
        try:
            text = io.open(path, encoding="utf-8").read()
        except Exception:
            continue
        block = os.path.relpath(os.path.dirname(path), SRC).replace(os.sep, "/")
        for cid in set(CID.findall(text)):
            out[cid].add(block)
    return out


def tapp_sibling(block):
    """The TAPP `profile/` for a legacy block's technique, if one exists.

    Both legacy families -- geochemProfile/<TECH>/profile-ada and
    adaProfile/<TECH>/profile-ada -- are superseded by the same
    geochemProfile/<TECH>/profile, so the technique name is what connects them, not the family.
    """
    if not block.endswith("/profile-ada"):
        return None
    tech = block.rsplit("/", 2)[-2]
    cand = "techniqueProfile/geochemProfile/%s/profile" % tech
    return cand if os.path.isdir(os.path.join(SRC, cand.replace("/", os.sep))) else None


def validator(block):
    import jsonschema
    path = os.path.join(SRC, block.replace("/", os.sep), "resolvedSchema.json")
    with io.open(path, encoding="utf-8") as fh:
        return jsonschema.Draft202012Validator(json.load(fh))


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cap", type=int, default=40,
                    help="records validated per technique (default 40)")
    ap.add_argument("--tech", nargs="*", help="limit to these technique directory names")
    args = ap.parse_args()

    try:
        import build_html_views as bhv        # its ada_records() owns the DB convention
    except ImportError as exc:                # pragma: no cover
        print("cannot read the ADA database: %s" % exc)
        return 0

    # Reading the database name back is not decoration: an ambient ADA_NAME overrides a .env,
    # because load_dotenv does not replace a variable that is already set, so a run can silently
    # answer from production instead of the copy you meant.
    print("database: %s @ %s" % (os.environ.get("ADA_NAME") or "(unset)",
                                 os.environ.get("DB_2024_HOST") or "localhost"))

    blocks = cid_to_blocks()
    records = collections.defaultdict(list)
    total = 0
    try:
        rows = list(bhv.ada_records())
    except SystemExit as exc:
        # ada_records' own message names build_html_views' --source flag, which is not a flag
        # of this tool; keep the actionable part and re-label it.
        print("cannot read the ADA database: %s"
              % str(exc).replace("--source ada2 needs", "this report needs"))
        return 0
    for name, doc in rows:
        total += 1
        for cid in set(CID.findall(json.dumps(doc))):
            records[cid].append(doc)
    print("records read: %d" % total)
    print()

    rows, unmigratable = [], []
    for cid, docs in sorted(records.items(), key=lambda kv: -len(kv[1])):
        legacy = sorted(b for b in (blocks.get(cid) or set()) if b.endswith("/profile-ada"))
        if not legacy:
            continue
        lb = legacy[0]
        tech = lb.rsplit("/", 2)[-2]
        if args.tech and tech not in args.tech:
            continue
        tb = tapp_sibling(lb)
        if not tb:
            unmigratable.append((cid, len(docs), lb))
            continue
        sample = docs[:args.cap]
        lv, tv = validator(lb), validator(tb)
        lok = sum(1 for d in sample if not next(lv.iter_errors(d), None))
        tok, blocking = 0, collections.Counter()
        for d in sample:
            errs = list(tv.iter_errors(d))
            if not errs:
                tok += 1
            for e in errs:
                # EVERY error, not only the required-property ones. Reporting just those once
                # made this tool print a technique at 0/60 with nothing listed beneath it, which
                # reads as "it fails for no reason": the records had stopped failing on a missing
                # property and started failing on `schema:variableMeasured: []` not containing a
                # matching item. A report that is silent about the blocker it cannot phrase is
                # worse than a verbose one.
                #
                # Key on the PATH as well as the message. The property name alone is ambiguous --
                # schema:name is required at a dozen nodes -- and list indices are elided so
                # wasGeneratedBy/0 and /1 are one finding rather than two.
                where = "/".join("[]" if isinstance(x, int) else str(x) for x in e.path) or "(root)"
                m = re.match(r"'([^']+)' is a required property", e.message or "")
                what = "requires %s" % m.group(1) if m else (e.message or "")[:88]
                blocking["%s :: %s" % (where, what)] += 1
        rows.append((tech, cid, len(docs), len(sample), lok, tok, tb, blocking))

    print("%-9s %-14s %6s %9s %9s %-9s" % ("technique", "declared cid", "recs",
                                           "legacy ok", "TAPP ok", "verdict"))
    print("-" * 78)
    for tech, cid, n, s, lok, tok, tb, blocking in rows:
        verdict = "READY" if tok == s else ("partial" if tok else "not ready")
        print("%-9s %-14s %6d %9s %9s %-9s" % (tech, cid, n, "%d/%d" % (lok, s),
                                               "%d/%d" % (tok, s), verdict))
    if rows:
        print()
        print("=== where the TAPP profile rejects these records ===")
        for tech, cid, n, s, lok, tok, tb, blocking in rows:
            if blocking:
                print("  %s (%s)" % (tech, cid))
                for what, n in blocking.most_common(8):
                    print("      %4d  %s" % (n, what))
    if unmigratable:
        print()
        print("=== no TAPP profile exists for these, so migration cannot be assessed ===")
        for cid, n, lb in sorted(unmigratable, key=lambda r: -r[1]):
            print("  %-16s %5d record(s)   %s" % (cid, n, lb.replace("techniqueProfile/", "")))
    print()
    ready = [r[0] for r in rows if r[5] == r[3]]
    print("READY to drop the legacy declaration: %s" % (", ".join(ready) if ready else "none"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
