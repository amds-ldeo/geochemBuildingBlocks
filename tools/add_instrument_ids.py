#!/usr/bin/env python3
"""Add the @id that the instrument building block now requires, in the ex: namespace.

@id became REQUIRED on an instrument and on an INLINE instrument component: a monitored species has
to be able to name the device or the part that reports it, and an anonymous object cannot be
referenced. Every example predating that change lacks one.

The generators emit identifiers for what they build, but not every example is regenerated -- the
adaProfile profile-ada examples and the static BaseSchema examples are not produced by the
technique pipeline. This fills those in, with the same scheme the generators use so the two agree:

    ex:<document>/instrument/<AdditionalTypeToken>
    ex:<document>/instrument/<AdditionalTypeToken>/part/<ComponentToken>

Identifiers are document-scoped, derived from the type token, and de-duplicated with a numeric
suffix where one document carries two instruments of the same kind. Deriving them keeps them stable
across re-runs; a random or sequential id would churn every example on every invocation.

The DOCUMENT scope is not decoration. This file used to mint `ex:instrument/<Type>`, which its own
docstring already called document-scoped and which was not: a type is shared by every example of a
technique, so `ex:instrument/SEM` was one JSON-LD node in 85 documents and the NeXus base class
`ex:instrument/nxs-BaseClass-NXinstrument` was one node in 113. The scheme itself now lives in
schema_path_example_emitter (doc_scope / instrument_id), so there is one implementation of it.

    python tools/add_instrument_ids.py            # report
    python tools/add_instrument_ids.py --write
"""
import argparse
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import schema_path_example_emitter as spe  # noqa: E402


def slug(v, fallback):
    s = re.sub(r"[^A-Za-z0-9]+", "-", str(v or "")).strip("-")
    return s or fallback


def token_of(node, fallback):
    """The instrument/component type token: the first plain string in schema:additionalType.

    Falls back to the node's schema:name, which a static example usually carries and a generated one
    does not -- the generators' own _type_token has no such fallback because at the point they mint,
    the name may still be the "missing" sentinel.
    """
    for x in (node.get("schema:additionalType") or []):
        if isinstance(x, str):
            return slug(x, fallback)
    return slug(node.get("schema:name"), fallback)


def fix(doc):
    """Add @id where missing. Returns (instruments_fixed, parts_fixed).

    Only where MISSING: an @id already in the file was decided by whoever wrote the file, and a
    source-derived example names its instruments after the models its sources identify. Migrating an
    existing identifier is a separate, deliberate act.
    """
    scope = spe.doc_scope(doc)
    if scope is None:
        return (0, 0)          # nothing to scope an identifier by; leave the document alone
    used = set()

    def unique(base):
        cand, n = base, 2
        while cand in used:
            cand, n = "%s-%d" % (base, n), n + 1
        used.add(cand)
        return cand

    counts = [0, 0]

    def collect(n):
        if isinstance(n, dict):
            if isinstance(n.get("@id"), str):
                used.add(n["@id"])
            for v in n.values():
                collect(v)
        elif isinstance(n, list):
            for v in n:
                collect(v)

    collect(doc)

    def walk(n):
        if isinstance(n, dict):
            for k, v in n.items():
                if k == "schema:instrument":
                    for i in (v if isinstance(v, list) else [v]):
                        if not isinstance(i, dict):
                            continue
                        if not isinstance(i.get("@id"), str):
                            i["@id"] = unique(spe.instrument_id(token_of(i, "instrument"), scope))
                            counts[0] += 1
                        for p in (i.get("schema:hasPart") or []):
                            # the by-reference form is a bare {"@id": ...}; only INLINE components
                            # (which carry their own description) need one minted
                            if isinstance(p, dict) and not isinstance(p.get("@id"), str):
                                p["@id"] = unique("%s/part/%s" % (i["@id"], token_of(p, "component")))
                                counts[1] += 1
                walk(v)
        elif isinstance(n, list):
            for v in n:
                walk(v)

    walk(doc)
    return tuple(counts)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    files = sorted(glob.glob(os.path.join(ROOT, "_sources", "**", "example*.json"), recursive=True))
    ti = tp = nf = 0
    for f in files:
        try:
            doc = json.load(open(f, encoding="utf-8"))
        except Exception:
            continue
        i, p = fix(doc)
        if not (i or p):
            continue
        nf += 1
        ti += i
        tp += p
        if a.write:
            with open(f, "w", encoding="utf-8", newline="\n") as fh:
                json.dump(doc, fh, indent=2, ensure_ascii=False)
                fh.write("\n")
    print("%d file(s): %d instrument @id, %d component @id%s"
          % (nf, ti, tp, "" if a.write else "   (dry run - pass --write)"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
