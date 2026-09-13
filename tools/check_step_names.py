#!/usr/bin/env python3
"""Assert every schema:actionProcess step name is one its technique actually recognises.

JSON Schema validation does NOT catch a mis-named step, and it fails in the worst way:
silently. A profile attaches per-step constraints with

    if   {schema:name: {const: "Data acquisition"}}
    then {schema:additionalProperty: {...}}

so a step named anything else does not match the `if`, no `then` applies, and the step
accepts arbitrary content. Where a profile ALSO requires the step by name via `contains`,
that requirement can itself sit under an outer conditional the record never triggers -- one
keyed on an ada:TAPPDefinition in prov:used, say -- so nothing fails at all.

Measured 2026-09-13: exampleadaSolutionMCICPMS-ETHZ-20240903.json named its acquisition step
"Acquisition" rather than the pinned "Data acquisition" and validated with ZERO errors while
every conditional block keyed off that name was skipped.

Findings are graded, because "not pinned" does not mean "wrong" -- a profile may simply not
constrain a step:

  SENTINEL   the step name IS a sentinel ('missing', -9999). Always a bug: a placeholder
             leaked into a structural position and took the step's constraints with it.
  NEAR-MISS  a recognised name is a substring of it or vice versa ("Acquisition" vs "Data
             acquisition"). Almost certainly a typo, and silently ignored.
  novel      recognised nowhere in the technique. Reported as a count, not a failure; it
             may be a deliberate extra step the profile does not constrain.

    python tools/check_step_names.py            # report; fails on SENTINEL
    python tools/check_step_names.py -v         # also list every novel name
    python tools/check_step_names.py --strict   # fail on NEAR-MISS too

Exit non-zero on failure so it can gate CI beside check_componentType.py.
"""
import argparse
import collections
import glob
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TPROF = os.path.join(ROOT, "_sources", "techniqueProfile")
SENTINELS = {"missing", "nil:missing", "-9999", "n/a", "none", ""}


def _const_name(node):
    """The schema:name const of a step subschema, if it pins one."""
    if not isinstance(node, dict):
        return None
    n = ((node.get("properties") or {}).get("schema:name") or {}).get("const")
    return n if isinstance(n, str) else None


def step_names(schema):
    """(required, recognised) step names a schema pins.

    Scoped deliberately to the `schema:step` ARRAY subschema. Parameter names such as
    'Guard Electrode' also appear as schema:name consts, but nested inside a step's
    schema:additionalProperty items -- they are not step names and must not be collected.
    """
    required, recognised = set(), set()

    def scan_array(x):
        cands = [x.get("contains")]
        cands += [b.get("contains") for b in x.get("allOf", []) if isinstance(b, dict)]
        for c in cands:
            n = _const_name(c)
            if n:
                required.add(n)
                recognised.add(n)
        for b in (x.get("items") or {}).get("allOf", []) or []:
            if isinstance(b, dict):
                n = _const_name(b.get("if"))
                if n:
                    recognised.add(n)

    def walk(n, depth=0):
        if depth > 24:
            return
        if isinstance(n, dict):
            s = (n.get("properties") or {}).get("schema:step")
            if isinstance(s, dict):
                scan_array(s)
            for v in n.values():
                walk(v, depth + 1)
        elif isinstance(n, list):
            for v in n:
                walk(v, depth + 1)

    walk(schema)
    return required, recognised


def used_names(doc):
    """Every schema:step name in an instance, with the JSON pointer it sits at."""
    out = []

    def walk(n, path=""):
        if isinstance(n, dict):
            s = n.get("schema:step")
            if isinstance(s, list):
                for i, st in enumerate(s):
                    if isinstance(st, dict) and isinstance(st.get("schema:name"), str):
                        out.append(("%s/schema:step/%d" % (path, i), st["schema:name"]))
            for k, v in n.items():
                walk(v, path + "/" + k)
        elif isinstance(n, list):
            for i, v in enumerate(n):
                walk(v, "%s/%d" % (path, i))

    walk(doc)
    return out


def _squash(x):
    return "".join(x.lower().split())


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("-v", "--verbose", action="store_true",
                    help="also list every novel step name")
    ap.add_argument("--strict", action="store_true",
                    help="fail on near-misses too, not only sentinels")
    a = ap.parse_args()

    # A technique's blocks (tapp / detail / profile / profile-ada) constrain different
    # slices of one record, so a name pinned by ANY of them is a name the technique knows.
    # Judging a tapp example against the tapp block alone reports every "Data reduction" in
    # the corpus -- 33 of them -- which is noise rather than signal.
    tech_ok, blocks = collections.defaultdict(set), 0
    for res in sorted(glob.glob(os.path.join(TPROF, "*", "*", "*", "resolvedSchema.json"))):
        tech = "/".join(os.path.relpath(res, TPROF).replace("\\", "/").split("/")[:2])
        try:
            _, ok = step_names(json.load(open(res, encoding="utf-8")))
        except Exception as e:
            print("  UNREADABLE %s: %s" % (res, e))
            continue
        if ok:
            blocks += 1
        tech_ok[tech] |= ok

    sentinel, nearmiss, novel, checked = [], [], [], 0
    for res in sorted(glob.glob(os.path.join(TPROF, "*", "*", "*", "resolvedSchema.json"))):
        blk = os.path.dirname(res)
        tech = "/".join(os.path.relpath(res, TPROF).replace("\\", "/").split("/")[:2])
        ok = tech_ok.get(tech) or set()
        if not ok:
            continue
        for ex in sorted(glob.glob(os.path.join(blk, "example*.json"))):
            try:
                doc = json.load(open(ex, encoding="utf-8"))
            except Exception:
                continue
            checked += 1
            rel = os.path.relpath(ex, ROOT).replace("\\", "/")
            for ptr, name in used_names(doc):
                if name in ok:
                    continue
                row = (rel, ptr, name, sorted(ok))
                if name.strip().lower() in SENTINELS:
                    sentinel.append(row)
                elif any(_squash(x) in _squash(name) or _squash(name) in _squash(x) for x in ok):
                    nearmiss.append(row)
                else:
                    novel.append(row)

    print("")
    print("%d block(s) pin step names across %d technique(s) | %d example(s) checked"
          % (blocks, len(tech_ok), checked))

    def show(rows, head):
        print("")
        print("%s (%d)" % (head, len(rows)))
        for f, ptr, name, ok in rows:
            print("  %s" % f)
            print("      %s = %r" % (ptr, name))
            print("      recognised: %s" % ", ".join(repr(x) for x in ok))

    if sentinel:
        show(sentinel, "SENTINEL as a step name -- the step is silently unconstrained")
    if nearmiss:
        show(nearmiss, "NEAR-MISS of a recognised name -- almost certainly a typo, and "
                       "validation will NOT catch it")
    if novel:
        if a.verbose:
            show(novel, "novel step names -- unconstrained, but may be deliberate")
        else:
            agg = collections.Counter(n for _, _, n, _ in novel)
            print("")
            print("%d novel step name(s) over %d use(s); -v to list. Most common: %s"
                  % (len(agg), len(novel), ", ".join("%r x%d" % kv for kv in agg.most_common(4))))

    if not sentinel and not nearmiss:
        print("")
        print("no sentinel or near-miss step names.")
    return 1 if (sentinel or (nearmiss and a.strict)) else 0


if __name__ == "__main__":
    sys.exit(main())
