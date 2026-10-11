"""Keep the productType vocabulary, adaProduct's enum and the examples in sync.

`registry/vocab/productType.json` is the source of truth and the enum is generated from it
by `apply_productType_enum.py`. Nothing in the regeneration chain runs that applier --
`check-schema-drift` runs only `resolve_schema.py --all` and `regenerate_schema_json.py` --
so a hand-edit of the enum, or a vocabulary change that was never applied, would otherwise
sit undetected. That is the same gap `check_componentType.py` exists to close for
componentType.

Checks, each a hard failure:

  A. the enum equals the vocabulary's labels exactly -- every skos:prefLabel and
     skos:altLabel is an enum member, and every enum member is one of them. A missing
     member silently rejects records; an extra one silently accepts a term the vocabulary
     does not define.
  B. the declaration annotates schema:inDefinedTermSet -> ada:vocab/productType, so a
     reader of the schema can reach the scheme.
  C. every product type used by an example is a vocabulary label. A record's
     schema:additionalType carries the product type beside 'ada:DataDeliveryPackage';
     anything else there must be a term the vocabulary knows.

Read-only. Exits non-zero on any failure, so it can gate CI.

    python tools/check_productType.py
"""
import glob
import io
import json
import os
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VOCAB = os.path.join(ROOT, "_sources", "registry", "vocab", "productType.json")
SCHEMA = os.path.join(ROOT, "_sources", "BaseSchema", "adaProduct", "schema.yaml")
SCHEME_ID = "ada:vocab/productType"
PACKAGE = "ada:DataDeliveryPackage"      # the CURIE that rides beside the product type


def vocab_labels():
    with io.open(VOCAB, encoding="utf-8") as fh:
        doc = json.load(fh)
    pref, alt = set(), set()
    for concept in doc.get("skos:hasTopConcept") or []:
        if concept.get("skos:prefLabel"):
            pref.add(concept["skos:prefLabel"])
        alts = concept.get("skos:altLabel") or []
        alt.update([alts] if isinstance(alts, str) else alts)
    return pref, alt


def declaration():
    with io.open(SCHEMA, encoding="utf-8") as fh:
        doc = yaml.safe_load(fh)
    return doc["allOf"][1]["properties"]["schema:additionalType"]


def main():
    pref, alt = vocab_labels()
    labels = pref | alt
    decl = declaration()
    enum = set(decl.get("contains", {}).get("enum") or [])
    failures = []

    print("vocabulary : %d concepts, %d labels (%d preferred + %d alternate)"
          % (len(pref), len(labels), len(pref), len(alt)))
    print("enum       : %d members" % len(enum))
    print()

    missing = sorted(labels - enum)
    extra = sorted(enum - labels)
    print("A. the enum matches the vocabulary")
    if missing or extra:
        for value in missing[:10]:
            print("   FAIL in the vocabulary but NOT the enum: %r" % value)
        for value in extra[:10]:
            print("   FAIL in the enum but NOT the vocabulary: %r" % value)
        if len(missing) + len(extra) > 20:
            print("   ... and %d more" % (len(missing) + len(extra) - 20))
        print("   run: python tools/apply_productType_enum.py --write")
        failures.append("enum out of sync (%d missing, %d extra)" % (len(missing), len(extra)))
    else:
        print("   ok -- %d labels, exactly" % len(labels))

    print("\nB. the declaration names the scheme")
    if decl.get("schema:inDefinedTermSet") == SCHEME_ID:
        print("   ok -- schema:inDefinedTermSet -> %s" % SCHEME_ID)
    else:
        print("   FAIL schema:inDefinedTermSet is %r, expected %r"
              % (decl.get("schema:inDefinedTermSet"), SCHEME_ID))
        failures.append("annotation missing or wrong")

    print("\nC. every product type an example uses is a vocabulary label")
    unknown, checked = {}, 0
    for path in glob.glob(os.path.join(ROOT, "_sources", "**", "example*.json"),
                          recursive=True):
        try:
            with io.open(path, encoding="utf-8") as fh:
                inst = json.load(fh)
        except Exception:
            continue
        values = inst.get("schema:additionalType")
        if not isinstance(values, list):
            continue
        # Scope: the enum is on adaProduct's ROOT, and what identifies an adaProduct
        # instance is ada:DataDeliveryPackage riding beside the product type. Checking every
        # example instead flags geochemProduct's own fixture, whose single value
        # "Geochemical analysis" is a geochemProduct-level label and was never governed by
        # this enum -- 110 of 112 examples carry the marker, and the other two are not
        # delivery packages.
        if not any((v.get("@id") if isinstance(v, dict) else v) == PACKAGE for v in values):
            continue
        checked += 1
        for value in values:
            if not isinstance(value, str) or value == PACKAGE:
                continue                      # {@id} forms and the package CURIE are not types
            if value not in labels:
                unknown.setdefault(value, []).append(os.path.relpath(path, ROOT))
    if unknown:
        for value, files in sorted(unknown.items(), key=lambda kv: -len(kv[1]))[:10]:
            print("   FAIL %r in %d example(s), e.g. %s"
                  % (value, len(files), files[0].replace("_sources" + os.sep, "")))
        failures.append("%d unknown product type(s) in examples" % len(unknown))
    else:
        print("   ok -- %d example(s) with a root schema:additionalType, all known" % checked)

    print("\n%s" % ("FAIL: " + "; ".join(failures) if failures else "PASS"))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
