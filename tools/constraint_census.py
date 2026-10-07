#!/usr/bin/env python3
"""Count what every resolved schema CONSTRAINS, and fail when a constraint disappears.

The problem this exists for is documented in docs/SILENT_SUCCESS.md section 1: a schema is a
set of restrictions, so deleting one makes the schema more PERMISSIVE and every instance that
validated before still validates. `validate_examples.py` cannot see a constraint go missing --
it has twice stayed green through real losses (nine ICP-MS schemas lost `Limit of
Quantification (LOQ) Method`; a standalone `build_pathdriven` run dropped the whole
`schema:actionProcess` subtree, 74 JSON paths, at a green 614/26).

No set of POSITIVE examples can fix that, however comprehensive: removing a restriction cannot
make a valid instance invalid. Two things can. Instances that must FAIL (see
`validate_counterexamples.py`), and counting the constraints themselves -- which is this tool,
and which needs no examples at all.

CLI:

    python tools/constraint_census.py                # check the tree against the manifest
    python tools/constraint_census.py --write        # record the current tree as the baseline
    python tools/constraint_census.py --explain BLOCK  # per-kind breakdown for one block
    python tools/constraint_census.py --verbose      # list every block, not just changed ones

Check mode exits 1 on ANY divergence, in either direction. Growth is not waved through: a
constraint that appears unannounced is as much worth a look as one that vanishes, and the
manifest is the record of what was intended. So a deliberate schema change is a two-step --
regenerate, then `--write` and commit the manifest in the same PR, where the diff shows exactly
which constraints moved. That is the whole point: a loss becomes a few reviewable lines in one
small file instead of something invisible inside 2000 regenerated ones.

It is deliberately NOT a stage of regenerate.py. A stage would rewrite the baseline on every
run, and a baseline that silently agrees with whatever just happened records nothing -- the same
reasoning as docs/modules/emitted.json, which is written only by the run that builds the modules
and never re-derived.

ARRAY INDICES ARE ELIDED from the JSON pointers (`allOf[2]/properties/x` is counted as
`allOf[]/properties/x`). Branch order carries no meaning in `allOf`/`anyOf`/`oneOf`, and the
upstream postprocess is known to reorder lists it emits (opengeospatial/bblocks-postprocess#91),
so an index-sensitive census would cry wolf on reordering and train everyone to ignore it.
Occurrences are counted as a multiset, so a branch that disappears still lowers the count.
"""

import argparse
import collections
import hashlib
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCES = os.path.join(ROOT, "_sources")
MANIFEST = os.path.join(ROOT, "docs", "constraint_census.json")

# Keywords that genuinely NARROW what validates. `properties` is not here: declaring a property
# permits it, it does not require it -- `required` is the restriction, and counting both would
# double-count one decision. `$ref` is here because losing a ref loses everything behind it,
# which is the single most consequential silent loss this repo has had.
SCALAR_KEYWORDS = (
    "const", "pattern", "format", "minimum", "maximum", "exclusiveMinimum",
    "exclusiveMaximum", "minLength", "maxLength", "minItems", "maxItems",
    "minProperties", "maxProperties", "multipleOf", "uniqueItems", "propertyNames",
)
BRANCH_KEYWORDS = ("allOf", "anyOf", "oneOf")


def _elide(ptr):
    """Pointer with array indices collapsed, so branch ORDER does not register as a change."""
    out = []
    for seg in ptr:
        out.append("[]" if isinstance(seg, int) else str(seg))
    return "/".join(out)


def _stable(value):
    """A short, order-insensitive digest of a value, for enum members and const payloads."""
    def canon(o):
        if isinstance(o, dict):
            return "{" + ",".join(f"{k}:{canon(v)}" for k, v in sorted(o.items())) + "}"
        if isinstance(o, list):
            return "[" + ",".join(sorted(canon(v) for v in o)) + "]"
        return json.dumps(o, sort_keys=True)
    return hashlib.sha256(canon(value).encode("utf-8")).hexdigest()[:12]


def fingerprints(node, ptr=()):
    """Every constraint in `node`, as (elided pointer, kind, detail) triples."""
    if isinstance(node, dict):
        here = _elide(ptr)

        if isinstance(node.get("required"), list):
            for name in node["required"]:
                if isinstance(name, str):
                    yield (here, "required", name)

        if isinstance(node.get("enum"), list):
            # One fingerprint per MEMBER, so dropping a term from a controlled list registers.
            for member in node["enum"]:
                yield (here, "enum", _stable(member))

        if "type" in node:
            tv = node["type"]
            for t in (tv if isinstance(tv, list) else [tv]):
                if isinstance(t, str):
                    yield (here, "type", t)

        if node.get("additionalProperties") is False:
            yield (here, "closed", "additionalProperties")

        if isinstance(node.get("dependentRequired"), dict):
            for k, v in node["dependentRequired"].items():
                for name in (v if isinstance(v, list) else []):
                    yield (here, "dependentRequired", f"{k}->{name}")

        for kw in SCALAR_KEYWORDS:
            if kw in node:
                yield (here, kw, _stable(node[kw]))

        if "$ref" in node and isinstance(node["$ref"], str):
            yield (here, "ref", node["$ref"])

        if "not" in node:
            yield (here, "not", "present")

        for kw in BRANCH_KEYWORDS:
            if isinstance(node.get(kw), list):
                yield (here, kw, str(len(node[kw])))

        if "if" in node:
            # A conditional is only a constraint if it has a consequent.
            for side in ("then", "else"):
                if side in node:
                    yield (here, "conditional", side)

        for key, value in node.items():
            yield from fingerprints(value, ptr + (key,))

    elif isinstance(node, list):
        for i, value in enumerate(node):
            yield from fingerprints(value, ptr + (i,))


def census_file(path):
    """counts-by-kind and a digest of the whole fingerprint multiset for one resolved schema."""
    with open(path, encoding="utf-8") as fh:
        doc = json.load(fh)
    fps = list(fingerprints(doc))
    counts = collections.Counter(kind for _p, kind, _d in fps)
    lines = sorted(f"{p}|{k}|{d}" for p, k, d in fps)
    return {
        "counts": dict(sorted(counts.items())),
        "total": len(fps),
        # The counts catch magnitude and direction; the digest catches a SWAP that leaves the
        # counts equal -- one required property traded for another is invisible to a count.
        "digest": hashlib.sha256("\n".join(lines).encode("utf-8")).hexdigest()[:16],
    }


def blocks():
    """{block key: resolvedSchema.json path}, keyed by directory relative to _sources/."""
    found = {}
    for dirpath, _dirs, files in os.walk(SOURCES):
        if "resolvedSchema.json" in files:
            key = os.path.relpath(dirpath, SOURCES).replace(os.sep, "/")
            found[key] = os.path.join(dirpath, "resolvedSchema.json")
    return dict(sorted(found.items()))


def build():
    out, bad = {}, []
    for key, path in blocks().items():
        try:
            out[key] = census_file(path)
        except (OSError, ValueError) as exc:
            bad.append((key, str(exc)))
    return out, bad


def load_manifest():
    try:
        with open(MANIFEST, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return None


def save_manifest(data):
    totals = collections.Counter()
    for entry in data.values():
        totals.update(entry["counts"])
    payload = {
        "_comment": "Written by tools/constraint_census.py --write. Never hand-edit. See the "
                    "module docstring and docs/SILENT_SUCCESS.md section 1.",
        "_totals": dict(sorted(totals.items())),
        "_blocks": len(data),
        "_constraints": sum(e["total"] for e in data.values()),
        "blocks": data,
    }
    os.makedirs(os.path.dirname(MANIFEST), exist_ok=True)
    with open(MANIFEST, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(payload, fh, indent=2, sort_keys=True)
        fh.write("\n")
    return payload


def compare(now, before):
    """(lost, gained, changed, added_blocks, removed_blocks) -- lost/gained are per-kind deltas."""
    lost, gained, changed = [], [], []
    added = sorted(set(now) - set(before))
    removed = sorted(set(before) - set(now))
    for key in sorted(set(now) & set(before)):
        a, b = now[key], before[key]
        if a["digest"] == b["digest"]:
            continue
        kinds = sorted(set(a["counts"]) | set(b["counts"]))
        deltas = [(k, b["counts"].get(k, 0), a["counts"].get(k, 0)) for k in kinds
                  if a["counts"].get(k, 0) != b["counts"].get(k, 0)]
        for k, was, isnow in deltas:
            (lost if isnow < was else gained).append((key, k, was, isnow))
        if not deltas:
            # Same counts, different digest: constraints were SWAPPED, not added or removed.
            changed.append(key)
    return lost, gained, changed, added, removed


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--write", action="store_true",
                    help="record the current tree as the baseline")
    ap.add_argument("--explain", metavar="BLOCK",
                    help="per-kind breakdown for one block, then exit")
    ap.add_argument("--verbose", action="store_true", help="list every block")
    args = ap.parse_args()

    if args.explain:
        found = blocks()
        matches = [k for k in found if args.explain in k]
        if not matches:
            print(f"no block matching {args.explain!r}", file=sys.stderr)
            return 2
        for key in matches:
            entry = census_file(found[key])
            print(f"{key}  ({entry['total']} constraints, digest {entry['digest']})")
            for kind, n in sorted(entry["counts"].items(), key=lambda kv: -kv[1]):
                print(f"    {n:6d}  {kind}")
        return 0

    now, bad = build()
    for key, err in bad:
        print(f"UNREADABLE {key}: {err}", file=sys.stderr)
    if bad:
        return 2

    if args.write:
        payload = save_manifest(now)
        print(f"wrote {os.path.relpath(MANIFEST, ROOT)}: "
              f"{payload['_blocks']} blocks, {payload['_constraints']} constraints")
        for kind, n in sorted(payload["_totals"].items(), key=lambda kv: -kv[1]):
            print(f"  {n:7d}  {kind}")
        return 0

    manifest = load_manifest()
    if manifest is None:
        print("no baseline at docs/constraint_census.json -- run with --write to create it",
              file=sys.stderr)
        return 2

    before = manifest.get("blocks", {})
    lost, gained, changed, added, removed = compare(now, before)

    if args.verbose:
        for key, entry in now.items():
            print(f"  {entry['total']:6d}  {key}")

    if not (lost or gained or changed or added or removed):
        print(f"constraint census unchanged: {len(now)} blocks, "
              f"{sum(e['total'] for e in now.values())} constraints")
        return 0

    # Losses first, and loudest: that is the failure this tool exists to make visible.
    if lost:
        print(f"\nCONSTRAINTS LOST ({len(lost)} kind(s) across "
              f"{len({k for k, *_ in lost})} block(s)):")
        for key, kind, was, isnow in lost:
            print(f"  -{was - isnow:<5d} {kind:20s} {was} -> {isnow}   {key}")
    if removed:
        print(f"\nBLOCKS GONE ({len(removed)}):")
        for key in removed:
            print(f"  - {key}  (was {before[key]['total']} constraints)")
    if changed:
        print(f"\nCONSTRAINTS SWAPPED, counts unchanged ({len(changed)} block(s)) -- "
              f"one constraint traded for another, which a count alone cannot see:")
        for key in changed:
            print(f"  ~ {key}")
    if gained:
        print(f"\nconstraints gained ({len(gained)} kind(s)):")
        for key, kind, was, isnow in gained:
            print(f"  +{isnow - was:<5d} {kind:20s} {was} -> {isnow}   {key}")
    if added:
        print(f"\nnew blocks ({len(added)}):")
        for key in added:
            print(f"  + {key}  ({now[key]['total']} constraints)")

    print("\nThe tree no longer matches docs/constraint_census.json.")
    print("If every line above is intended, re-run with --write and commit the manifest in the")
    print("same change, so the diff records which constraints moved and why.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
