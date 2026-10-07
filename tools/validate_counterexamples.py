#!/usr/bin/env python3
"""Assert that instances which MUST fail validation still do.

`validate_examples.py` proves that valid instances validate. It cannot prove that invalid ones
do not, and that is the half where constraints go missing: deleting a restriction makes a schema
more PERMISSIVE, so every positive example keeps passing (docs/SILENT_SUCCESS.md section 1).
`constraint_census.py` catches a constraint that disappears from the SCHEMA. This catches the
other shape of the same bug -- a constraint that is still present but no longer BITES, because
something upstream of it changed: a conditional whose `if` stopped matching, a branch moved to an
`anyOf` where it constrains nothing, a `$ref` that now resolves somewhere more permissive.

Each case is a MUTATION of a real example, not a stored invalid document:

    {"id": "...", "example": "<path>", "mutate": {...}, "expect": "...", "why": "..."}

The mutation is applied in memory, the result is validated against the example's sibling
resolvedSchema.json, and the case passes only if validation FAILS. A stored invalid document
would rot -- examples are regenerated, so a hand-written counterexample drifts out of shape and
starts failing for some unrelated reason, which still looks like a pass. Mutating the live
example keeps the fixture honest: it is always the current example minus exactly one thing.

`expect` is not optional and not decoration. A case that fails for the WRONG reason is the same
trap one level down -- it reports success while telling you nothing about the constraint it was
written for. So the error must mention `expect`, in its message, its schema path or its instance
path, or the case is reported as failing-for-the-wrong-reason and the run goes red.

A mutation whose pointer no longer exists is a HARD FAILURE, never a skip. The example has
changed shape and the case is no longer testing what it claims; skipping it would quietly reduce
coverage, which is precisely the failure mode this file exists to prevent.

    python tools/validate_counterexamples.py
    python tools/validate_counterexamples.py --verbose     # show the error each case produced
    python tools/validate_counterexamples.py --id <ID>     # run one case
"""

import argparse
import copy
import json
import os
import sys

try:
    import jsonschema
except ImportError:
    print("jsonschema is required: pip install -r requirements.txt", file=sys.stderr)
    sys.exit(2)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(ROOT, "docs", "counterexamples.json")


class StaleCase(Exception):
    """The mutation could not be applied, so the case is not testing what it claims."""


def _tokens(pointer):
    if pointer in ("", "/"):
        return []
    if not pointer.startswith("/"):
        raise StaleCase(f"pointer must start with '/': {pointer!r}")
    return [t.replace("~1", "/").replace("~0", "~") for t in pointer[1:].split("/")]


def _walk(doc, tokens, pointer):
    """Return (container, final_key) for a pointer, raising StaleCase if the path is gone."""
    node = doc
    for tok in tokens[:-1]:
        if isinstance(node, list):
            try:
                node = node[int(tok)]
            except (ValueError, IndexError):
                raise StaleCase(f"{pointer}: no index {tok!r} in a {len(node)}-item array")
        elif isinstance(node, dict):
            if tok not in node:
                raise StaleCase(f"{pointer}: no key {tok!r} (has {sorted(node)[:6]})")
            node = node[tok]
        else:
            raise StaleCase(f"{pointer}: {tok!r} descends into a {type(node).__name__}")
    return node, tokens[-1]


def apply_mutation(doc, mutate):
    """remove / set / add one location. Returns the mutated copy."""
    out = copy.deepcopy(doc)
    op = mutate.get("op")
    pointer = mutate.get("pointer", "")
    tokens = _tokens(pointer)
    if not tokens:
        raise StaleCase("mutation pointer may not be the whole document")
    container, key = _walk(out, tokens, pointer)

    if op == "remove":
        if isinstance(container, list):
            try:
                container.pop(int(key))
            except (ValueError, IndexError):
                raise StaleCase(f"{pointer}: cannot remove index {key!r}")
        else:
            if key not in container:
                raise StaleCase(f"{pointer}: nothing to remove (has {sorted(container)[:6]})")
            del container[key]

    elif op == "set":
        # `set` must land on something that EXISTS, otherwise the case silently becomes an
        # `add` and stops testing the constraint it names.
        if isinstance(container, list):
            try:
                container[int(key)] = mutate["value"]
            except (ValueError, IndexError):
                raise StaleCase(f"{pointer}: no index {key!r} to set")
        else:
            if key not in container:
                raise StaleCase(f"{pointer}: no key {key!r} to set (has {sorted(container)[:6]})")
            container[key] = mutate["value"]

    elif op == "add":
        if isinstance(container, list):
            container.insert(len(container) if key == "-" else int(key), mutate["value"])
        else:
            if key in container:
                raise StaleCase(f"{pointer}: already present, use 'set'")
            container[key] = mutate["value"]

    else:
        raise StaleCase(f"unknown op {op!r} (expected remove/set/add)")

    return out


def mentions(err, needle):
    """Does this error implicate `needle`, in its message or either path?"""
    low = needle.lower()
    if low in str(err.message).lower():
        return True
    for path in (err.absolute_schema_path, err.absolute_path):
        if any(low in str(p).lower() for p in path):
            return True
    # A failing composite reports its branch errors underneath, where the real detail sits.
    return any(mentions(sub, needle) for sub in err.context or [])


def run_case(case, verbose=False):
    """(ok, detail). ok is False when the constraint no longer bites, or bites wrongly."""
    ex_rel = case["example"]
    ex_path = os.path.join(ROOT, ex_rel)
    schema_path = os.path.join(os.path.dirname(ex_path), "resolvedSchema.json")
    if not os.path.exists(ex_path):
        return False, f"example is gone: {ex_rel}"
    if not os.path.exists(schema_path):
        return False, f"no sibling resolvedSchema.json for {ex_rel}"

    with open(ex_path, encoding="utf-8") as fh:
        example = json.load(fh)
    with open(schema_path, encoding="utf-8") as fh:
        schema = json.load(fh)

    validator = jsonschema.Draft202012Validator(schema)

    # The unmutated example must be VALID, or the case proves nothing: an already-invalid
    # example would "fail" after mutation no matter what the schema says about the mutation.
    baseline = list(validator.iter_errors(example))
    if baseline:
        return False, (f"the example is already invalid before mutation "
                       f"({len(baseline)} error(s), first: {baseline[0].message[:120]}) -- "
                       f"fix that first, this case cannot test anything")

    try:
        mutated = apply_mutation(example, case["mutate"])
    except StaleCase as exc:
        return False, f"STALE: {exc}"

    errors = list(validator.iter_errors(mutated))
    if not errors:
        return False, ("the mutated instance VALIDATES -- the constraint no longer bites. "
                       "This is the loss this check exists to catch.")

    expect = case["expect"]
    if not any(mentions(e, expect) for e in errors):
        msgs = "; ".join(e.message[:90] for e in errors[:3])
        return False, (f"fails, but not for {expect!r} -- so this case is no longer testing "
                       f"what it claims. Errors: {msgs}")

    detail = f"rejected ({len(errors)} error(s))"
    if verbose:
        detail += f": {errors[0].message[:140]}"
    return True, detail


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--verbose", action="store_true", help="show the error each case produced")
    ap.add_argument("--id", help="run only this case")
    args = ap.parse_args()

    if not os.path.exists(MANIFEST):
        print(f"no manifest at {os.path.relpath(MANIFEST, ROOT)}", file=sys.stderr)
        return 2
    with open(MANIFEST, encoding="utf-8") as fh:
        cases = json.load(fh)["cases"]

    if args.id:
        cases = [c for c in cases if c["id"] == args.id]
        if not cases:
            print(f"no case with id {args.id!r}", file=sys.stderr)
            return 2

    failures = []
    for case in cases:
        ok, detail = run_case(case, args.verbose)
        print(f"  {'ok  ' if ok else 'FAIL'}  {case['id']:44s} {detail}")
        if not ok:
            failures.append((case, detail))

    print()
    if failures:
        print(f"{len(failures)} of {len(cases)} counterexample(s) did not behave as required:\n")
        for case, detail in failures:
            print(f"  {case['id']}")
            print(f"    why this case exists: {case['why']}")
            print(f"    what happened:        {detail}\n")
        return 1

    print(f"all {len(cases)} counterexamples correctly rejected")
    return 0


if __name__ == "__main__":
    sys.exit(main())
