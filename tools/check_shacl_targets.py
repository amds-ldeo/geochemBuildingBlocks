"""Fail when a SHACL SPARQLTarget cannot select anything, so a shape cannot pass vacuously.

A SHACL shape whose target selects NO focus node reports conformance. Not "skipped", not
"0 of 0" -- conformance, indistinguishable from a shape that ran and found nothing wrong. That
is the same shape of failure as a `contains` over an empty array or a grep whose command never
ran, and it cost this repository 35 inert shapes.

THE INCIDENT (2026-10-16). Every technique profile's rules.shacl targeted

    ?meta schema:additionalType "dcat:CatalogRecord" .

a STRING LITERAL. ADA records and all 111 of this repository's own examples carry
`{"@id": "dcat:CatalogRecord"}`, which is an IRI node, and in SPARQL an IRI does not equal a
literal of the same spelling. Measured with rdflib against record 10.60707/09k9-j686: the literal
target selected 0 focus nodes, the IRI form selected 1. So all 35 shapes had been reporting
conformance over an empty focus set since commit 6341393bf0 moved the examples to `@id` form.

They are not dead code -- the OGC postprocess runs them and records SHACL as a passing test item
in build/tests/**/_report.json. A green SHACL result was being produced by shapes that examined
nothing.

The giveaway was that conformance ALONE could not tell the two apart: the real XRD example
conformed under both the broken and the fixed target. Only mutating it to carry no valid product
type separated them -- the broken target still conformed, the fixed one failed. A check that
cannot fail is this repository's most expensive defect, so what this tool asserts is that the
target SELECTS, not that validation passed.

TWO MODES, and the split is deliberate.

The default is a dependency-free text lint, suitable for CI: `rdflib` and `pyshacl` are not in
requirements.txt (nothing in tools/ imports them -- audit_building_blocks.py only checks that a
rules.shacl exists and mentions sh:NodeShape), and adding a pinned dependency to run shapes in CI
is a larger decision than this fix. The lint catches the exact regression: a CURIE written as a
string literal where an IRI is meant.

`--execute` is the real check and needs rdflib. It runs each SPARQLTarget against the examples
beside it and fails on any that selects nothing. It REFUSES rather than skipping when rdflib is
absent, because a check that quietly does not run is the thing this file exists to prevent.

    python tools/check_shacl_targets.py             # lint (CI)
    python tools/check_shacl_targets.py --execute   # run the targets (needs rdflib)
"""
import argparse
import glob
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "_sources")

# A CURIE-shaped string literal compared against a property that carries IRIs. `schema:additionalType`
# is the one that bit; the pattern is written to catch the family, not just that property.
CURIE_LITERAL = re.compile(r'(schema:additionalType|dcterms:conformsTo)\s+"([A-Za-z][\w.-]*:[^"\s]+)"')

TARGET_BLOCK = re.compile(r'sh:select\s+"""(.*?)"""', re.DOTALL)


def shacl_files():
    return sorted(glob.glob(os.path.join(SRC, "**", "rules.shacl"), recursive=True))


def lint(paths):
    bad = []
    for p in paths:
        text = io.open(p, encoding="utf-8").read()
        for m in CURIE_LITERAL.finditer(text):
            line = text[:m.start()].count("\n") + 1
            bad.append((p, line, m.group(1), m.group(2)))
    return bad


def execute(paths):
    try:
        import rdflib
    except ImportError:
        print("ERROR: --execute needs rdflib, which is not pinned in requirements.txt.\n"
              "Refusing rather than skipping: a check that quietly does not run is the defect\n"
              "this tool exists to catch.\n\n    pip install rdflib", file=sys.stderr)
        raise SystemExit(2)

    # Parse the shapes rather than regexing every sh:select, because the two kinds of query mean
    # OPPOSITE things. A sh:SPARQLTarget select names the focus nodes, so selecting nothing makes
    # the shape vacuous. A sh:sparql CONSTRAINT select returns violations, so selecting nothing is
    # a pass. The first draft of this tool regexed both and reported tappDefinition's two
    # duplicate-step constraints -- which correctly find no duplicates -- as inert targets.
    SH = rdflib.Namespace("http://www.w3.org/ns/shacl#")
    empty, ok, untested = [], 0, 0
    for p in paths:
        text = io.open(p, encoding="utf-8").read()
        try:
            sg = rdflib.Graph()
            sg.parse(data=text, format="turtle")
        except Exception as exc:
            print("  WARNING: %s did not parse as turtle (%s)"
                  % (os.path.relpath(p, ROOT).replace(os.sep, "/"), type(exc).__name__))
            continue
        targets = [str(q) for t in sg.subjects(rdflib.RDF.type, SH.SPARQLTarget)
                   for q in sg.objects(t, SH.select)]
        if not targets:
            continue
        d = os.path.dirname(p)
        examples = [e for e in sorted(glob.glob(os.path.join(d, "example*.json")))
                    if ".provenance" not in e]
        if not examples:
            untested += 1
            continue
        for sel in targets:
            selected_somewhere = False
            for e in examples:
                g = rdflib.Graph()
                try:
                    g.parse(data=io.open(e, encoding="utf-8").read(), format="json-ld")
                except Exception:
                    continue
                if len(list(g.query(sel))) > 0:
                    selected_somewhere = True
                    break
            if selected_somewhere:
                ok += 1
            else:
                empty.append((p, len(examples)))
    return empty, ok, untested


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--execute", action="store_true",
                    help="run each SPARQLTarget against its examples (needs rdflib)")
    a = ap.parse_args()

    paths = shacl_files()
    if not paths:
        print("ERROR: no rules.shacl found under _sources, so this checked nothing.",
              file=sys.stderr)
        return 1
    print("mode: %s | %d rules.shacl" % ("execute" if a.execute else "lint (text only)", len(paths)))

    bad = lint(paths)
    for p, line, prop, val in bad:
        print("  %s:%d  %s matched against the string literal %r"
              % (os.path.relpath(p, ROOT).replace(os.sep, "/"), line, prop, val))
    if bad:
        print("\nERROR: %d target(s) compare a CURIE-shaped STRING LITERAL against a property whose\n"
              "values are IRIs. In SPARQL an IRI never equals a literal of the same spelling, so\n"
              "the target selects nothing and the shape reports conformance having examined no\n"
              "focus node. Write the IRI instead, e.g.\n"
              "    <http://www.w3.org/ns/dcat#CatalogRecord>" % len(bad))
        return 1
    print("  no CURIE-shaped string literals in a target.")

    if a.execute:
        empty, ok, untested = execute(paths)
        print("\n  targets that select a focus node : %d" % ok)
        print("  blocks with no example to test   : %d" % untested)
        if empty:
            print("\nERROR: %d target(s) selected NOTHING against their own examples:" % len(empty))
            for p, n in empty:
                print("  %s  (%d example(s))" % (os.path.relpath(p, ROOT).replace(os.sep, "/"), n))
            return 1
        print("  every target with an example selects at least one focus node.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
