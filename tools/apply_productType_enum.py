"""Regenerate adaProduct's schema:additionalType enum from the productType vocabulary.

`registry/vocab/productType.json` is the source of truth; the enum is generated. Edit the
scheme and re-run this -- never edit the enum, which is overwritten.

WHY THE ENUM SURVIVES AT ALL, rather than the vocabulary replacing it. componentType is
modelled as a vocabulary referenced by annotation ALONE, and CLAUDE.md records what that
cost: "JSON-Schema validation no longer catches componentType drift", which is why
tools/check_componentType.py had to be written to restore the enforcement. Generating the
enum keeps the JSON Schema gate AND removes the hand-maintenance, so the `contains` pin
still rejects an unknown product type at validation time.

The annotation is added too (`schema:inDefinedTermSet`), so a reader of the schema can find
the scheme, matching the convention componentType and instrumentType already use.

BOTH LABEL KINDS GO IN. A record carrying an acronym form is as valid as one carrying the
preferred form -- the corpus holds both, often for the same technique -- so every
skos:prefLabel and skos:altLabel becomes an enum member. The vocabulary records which is
preferred; the enum records what is accepted. Collapsing variants in the enum would reject
records that are merely spelled differently.

Output is ordered by prefLabel, with each concept's altLabels following it under a comment
naming the concept, so the generated block is both deterministic and readable. A generator
whose output varies by run order cannot be diffed, which forecloses the drift check.

Text surgery rather than a YAML round trip: dumping this file reflows it wholesale, and
CLAUDE.md records ruamel rewriting 63 of 69 source files on a no-op.

    python tools/apply_productType_enum.py            # dry run
    python tools/apply_productType_enum.py --write
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VOCAB = os.path.join(ROOT, "_sources", "registry", "vocab", "productType.json")
SCHEMA = os.path.join(ROOT, "_sources", "BaseSchema", "adaProduct", "schema.yaml")
SCHEME_ID = "ada:vocab/productType"


def labels_by_concept():
    """[(concept @id, prefLabel, [altLabel, ...]), ...] ordered by prefLabel."""
    with io.open(VOCAB, encoding="utf-8") as fh:
        doc = json.load(fh)
    out = []
    for concept in doc.get("skos:hasTopConcept") or []:
        pref = concept.get("skos:prefLabel")
        if not pref:
            continue
        alts = concept.get("skos:altLabel") or []
        if isinstance(alts, str):
            alts = [alts]
        out.append((concept.get("@id", ""), pref, sorted(alts)))
    return sorted(out, key=lambda row: row[1].lower())


def enum_span(lines):
    """(start, end, indent) of the enum's member lines under contains."""
    start = None
    for i, line in enumerate(lines):
        if line.strip() == "enum:" and i and "contains" in lines[i - 1]:
            start = i
            break
    if start is None:
        raise SystemExit("could not find the contains.enum block in adaProduct/schema.yaml")
    indent = len(lines[start]) - len(lines[start].lstrip())
    end = start + 1
    while end < len(lines):
        line = lines[end]
        if line.strip() and (len(line) - len(line.lstrip())) <= indent:
            break
        end += 1
    return start, end, indent


def main():
    write = "--write" in sys.argv
    concepts = labels_by_concept()
    total = sum(1 + len(alts) for _, _, alts in concepts)

    text = io.open(SCHEMA, encoding="utf-8").read()
    lines = text.splitlines(keepends=True)
    start, end, indent = enum_span(lines)
    member = " " * (indent + 2)

    block = []
    for cid, pref, alts in concepts:
        block.append("%s# %s\n" % (member, cid))
        block.append("%s- %s\n" % (member, json.dumps(pref)))
        for alt in alts:
            block.append("%s- %s\n" % (member, json.dumps(alt)))

    before = "".join(lines[start + 1:end])
    lines[start + 1:end] = block

    # The annotation goes beside THIS enum's own `contains:` -- the line immediately above
    # the enum key, whose indent is the declaration's. Searching the file for the first
    # `contains:` at some indent instead put it inside
    # schema:subjectOf.properties.dcterms:conformsTo, an unrelated declaration with a
    # `contains` of its own, where it silently annotated the wrong property.
    contains_line = start - 1
    assert lines[contains_line].strip() == "contains:", (
        "expected `contains:` directly above the enum, found %r" % lines[contains_line].strip())
    decl_indent = len(lines[contains_line]) - len(lines[contains_line].lstrip())
    if SCHEME_ID not in "".join(lines[max(0, contains_line - 25):contains_line]):
        lines.insert(contains_line,
                     "%sschema:inDefinedTermSet: %s\n" % (" " * decl_indent, SCHEME_ID))
    rebuilt = "".join(lines)

    try:
        import yaml
        doc = yaml.safe_load(rebuilt)
        got = doc["allOf"][1]["properties"]["schema:additionalType"]["contains"]["enum"]
    except Exception as exc:
        raise SystemExit("result does not parse: %s" % exc)
    if len(got) != total:
        raise SystemExit("emitted %d enum members, expected %d" % (len(got), total))

    changed = "".join(block) != before or SCHEME_ID not in text
    print("concepts            : %d" % len(concepts))
    print("enum members emitted: %d  (%d prefLabel + %d altLabel)"
          % (total, len(concepts), total - len(concepts)))
    print("annotation          : schema:inDefinedTermSet -> %s" % SCHEME_ID)
    print("state               : %s" % ("CHANGED" if changed else "already current"))
    if write:
        with io.open(SCHEMA, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(rebuilt)
        print("WRITTEN")
    else:
        print("DRY RUN -- pass --write to apply")
    return 0


if __name__ == "__main__":
    sys.exit(main())
