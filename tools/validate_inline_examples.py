"""Validate the INLINE examples that validate_examples.py cannot see.

`validate_examples.py` globs `example*.json`. **46 blocks have no such file** --
their examples live as `snippets[].code` inside `examples.yaml` -- so it reports
644/644 green while those blocks' examples are never checked at all. It is not a
bug in that tool; a glob cannot reach a string inside a YAML document.

The cost of the blind spot, measured 2026-10-08: **26 of 58** inline snippets
failed their own block's schema, and had done since they were written. Among
them seven examples still carrying the retired OBJECT-FORM `ada:componentType`
that `CLAUDE.md` says must never come back, a `laboratory` example with
`schema:name` and `schema:alternateName` exactly the wrong way round, and every
one of the fourteen `adaProfile/*/detail` examples missing the required
`ada:componentType`. The OGC postprocess did see them -- it wrote a
`build/tests/**/*.validation_failed.txt` for each -- and then concluded success,
so nothing ever failed.

Validates against the committed `resolvedSchema.json`, the same target
`validate_examples.py` prefers and the file downstream validators actually read.
No network, no submodule.

A snippet whose `code` is not JSON is skipped: some are Turtle or YAML, and this
checks JSON Schema conformance only.

Exits 1 if any snippet fails, 0 otherwise. Prints the count it validated, so
"found nothing" cannot read as success -- the dead-rule failure mode this file
exists to prevent, and the one `check-examples.yml` guards with its corpus floor.

    python tools/validate_inline_examples.py
    python tools/validate_inline_examples.py --verbose

Eventually this belongs inside `validate_examples.py`, so one command covers
both shapes of example and one CI step gates them. Kept separate for now
because that tool's glob is load-bearing in several other places.
"""
import argparse
import glob
import json
import os
import sys

import yaml
from jsonschema import Draft202012Validator


def inline_blocks():
    """Blocks whose examples exist ONLY as examples.yaml snippets."""
    for path in sorted(glob.glob('_sources/**/examples.yaml', recursive=True)):
        directory = os.path.dirname(path)
        if glob.glob(os.path.join(directory, 'example*.json')):
            continue  # validate_examples.py covers these
        resolved = os.path.join(directory, 'resolvedSchema.json')
        if os.path.exists(resolved):
            yield directory, path, resolved


def snippets_of(doc):
    for entry in (doc if isinstance(doc, list) else [doc]):
        for snippet in (entry or {}).get('snippets') or []:
            code = snippet.get('code')
            if not code:
                continue
            try:
                yield json.loads(code)
            except ValueError:
                continue  # not JSON (turtle, yaml); not ours to judge


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='Print every block checked, not only the failures')
    args = parser.parse_args()

    checked = failures = blocks = 0
    for directory, yaml_path, resolved in inline_blocks():
        blocks += 1
        try:
            doc = yaml.safe_load(open(yaml_path, encoding='utf-8'))
            validator = Draft202012Validator(json.load(open(resolved, encoding='utf-8')))
        except Exception as exc:                                  # noqa: BLE001
            print('%s\n  LOAD FAILED: %s' % (directory, exc))
            failures += 1
            continue
        for instance in snippets_of(doc):
            checked += 1
            errors = sorted(validator.iter_errors(instance), key=lambda e: list(e.path))
            if not errors:
                if args.verbose:
                    print('  ok   %s' % directory)
                continue
            failures += 1
            error = errors[0]
            pointer = '/'.join(str(p) for p in error.path) or '(root)'
            print('%s\n  %s: %s' % (directory, pointer, error.message))

    print()
    print('%d inline snippet(s) in %d block(s); %d failed' % (checked, blocks, failures))
    if not checked:
        print('No inline snippets found at all. Treating that as a failure rather than a '
              'pass: this tool exists because an example nothing validates rots silently.')
        return 1
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())
