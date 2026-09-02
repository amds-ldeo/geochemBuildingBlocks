"""Keep the schema, examples and componentType vocabulary in sync.

componentType is modelled as a controlled *vocabulary* referenced by annotation
(schema:inDefinedTermSet -> ada:vocab/componentType), NOT as a hard JSON-Schema enum,
so JSON-Schema validation no longer catches componentType drift. This checker restores
that enforcement across the four places componentType lives:

  1. registry/vocab/componentType.json   the UNIVERSAL (cross-technique) term set (SKOS)
  2. tools/componentType_enum_cache.json  the FULL per-file-type-BB term set, cached from
                                          the Components worksheet (apply_componentType_enums.py)
  3. BaseSchema/{geochemProduct,adaProduct}/schema.yaml
                                          must annotate schema:inDefinedTermSet -> the vocab
  4. every _sources/**/example*.json      ada:componentType values actually used

Checks (each a hard failure unless noted):
  A. universal vocab terms are all present in the enum cache (the authoritative source)
  B. base schemas reference the vocab @id via schema:inDefinedTermSet
  C. every ada:componentType value used in an example is a known term
     (universal vocab UNION enum-cache) -- otherwise it is drift

Exit non-zero if any check fails, so it can gate CI. Read-only; prints a report.

    python tools/check_componentType.py
"""
import json
import glob
import os
import sys
import apply_componentType_enums as ace

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VOCAB = os.path.join(ROOT, "_sources", "registry", "vocab", "componentType.json")
CACHE = os.path.join(ROOT, "tools", "componentType_enum_cache.json")
VOCAB_ID = "ada:vocab/componentType"
BASE_SCHEMAS = ["_sources/BaseSchema/geochemProduct/schema.yaml",
                "_sources/BaseSchema/adaProduct/schema.yaml"]


def vocab_terms():
    d = json.load(open(VOCAB, encoding="utf-8"))
    return {c.get("skos:notation") for c in d.get("skos:hasTopConcept", [])}


def cache_terms():
    d = json.load(open(CACHE, encoding="utf-8"))
    out = set()
    for vals in d.values():
        out.update(vals)
    return out


def example_componentTypes():
    """{value -> [example files using it]} for every ada:componentType string in examples."""
    used = {}

    def walk(o, path):
        if isinstance(o, dict):
            for k, v in o.items():
                if k == "ada:componentType" and isinstance(v, str):
                    used.setdefault(v, set()).add(path)
                walk(v, path)
        elif isinstance(o, list):
            for x in o:
                walk(x, path)

    for ex in glob.glob(os.path.join(ROOT, "_sources", "**", "example*.json"), recursive=True):
        try:
            walk(json.load(open(ex, encoding="utf-8")), os.path.relpath(ex, ROOT))
        except Exception:
            pass
    return used


def schema_refs_vocab(path):
    """True if the schema annotates schema:inDefinedTermSet -> the vocab @id anywhere."""
    txt = open(os.path.join(ROOT, path), encoding="utf-8").read()
    return "schema:inDefinedTermSet" in txt and VOCAB_ID in txt


def schema_enum_componentTypes():
    """Technique-specific ada:componentType values enumerated by profile/detail resolvedSchemas.
    These are enforced by JSON Schema per technique, so they are known terms, not drift."""
    out = set()

    def walk(node):
        if isinstance(node, dict):
            ct = node.get("properties", {}).get("ada:componentType") if isinstance(node.get("properties"), dict) else None
            if isinstance(ct, dict):
                for en in _enums(ct):
                    out.update(en)
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for x in node:
                walk(x)

    def _enums(sch):
        # yield any enum list reachable from a componentType subschema (direct, or under anyOf/const)
        if isinstance(sch, dict):
            if isinstance(sch.get("enum"), list):
                yield sch["enum"]
            if isinstance(sch.get("const"), str):
                yield [sch["const"]]
            for key in ("anyOf", "oneOf", "allOf"):
                for sub in sch.get(key, []):
                    yield from _enums(sub)

    for rs in glob.glob(os.path.join(ROOT, "_sources", "techniqueProfile", "**", "resolvedSchema.json"), recursive=True):
        try:
            walk(json.load(open(rs, encoding="utf-8")))
        except Exception:
            pass
    return out


def main():
    vocab = vocab_terms()
    cache = cache_terms()
    tech = schema_enum_componentTypes()
    known = vocab | cache | tech
    used = example_componentTypes()
    failures = []

    print(f"vocab (universal): {len(vocab)} terms | enum cache: {len(cache)} terms | "
          f"technique-schema enums: {len(tech)} terms | examples use {len(used)} distinct componentTypes\n")

    # A. universal vocab ⊆ enum cache, EXCEPT the OGC nil reason.
    #
    # The cache is the Components worksheet, cached; `nil:missing` is deliberately not a
    # worksheet row -- a nil reason applies to every file type, so apply_componentType_enums
    # appends it to each base BB's enum directly (see NIL_MISSING there). Adding it to the
    # cache would satisfy this check and then be dropped by the next `--refresh`, which is a
    # worse failure than the one it silences: the term would vanish from the enums with the
    # cache still claiming it. Exempted here, and imported rather than restated so the two
    # cannot drift apart.
    missing = sorted(vocab - cache - {ace.NIL_MISSING})
    if missing:
        failures.append(f"[A] {len(missing)} universal vocab term(s) absent from the enum cache "
                        f"(refresh apply_componentType_enums --refresh, or drop from the vocab): {missing}")

    # B. base schemas annotate the vocab
    for s in BASE_SCHEMAS:
        if not schema_refs_vocab(s):
            failures.append(f"[B] {s} does not annotate schema:inDefinedTermSet -> {VOCAB_ID}")

    # C. every used componentType is a known term
    drift = sorted(v for v in used if v not in known)
    if drift:
        for v in drift:
            exs = sorted(used[v])
            failures.append(f"[C] componentType '{v}' used in {len(exs)} example(s) is in neither the "
                            f"universal vocab nor the enum cache: e.g. {exs[0]}")

    if failures:
        print(f"COMPONENTTYPE DRIFT — {len(failures)} issue(s):")
        for f in failures:
            print("  -", f)
        sys.exit(1)
    print("componentType is in sync across vocab, enum cache, base schemas, and examples.")


if __name__ == "__main__":
    main()
