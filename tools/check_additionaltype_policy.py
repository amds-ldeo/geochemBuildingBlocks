"""Enforce the serialization policy for schema:additionalType / schema:propertyID.

CDIF's schemaorgProperties/additionalProperty SHACL reports, at sh:Violation severity, a
value that LOOKS like a URI or CURIE but is serialized as a string literal -- while
explicitly permitting a free label such as 'MaterialSample' to stay a string. #77 cleared
1,542 such values out of the corpus. This checker stops the class coming back, and it is
split in two because the two halves fail for different reasons.

  A. A `contains` PIN that names a CURIE or URI must also admit the IRI-reference form.

     This is the half that actually broke. 326 of this repo's 336 additionalType
     declarations are discriminators: `contains: {const: X}` with `items` left
     unconstrained. An {"@id": X} member is admitted as a VALUE, but the array stops
     satisfying `contains` the moment X is converted -- the constraint is still present and
     still bites, it just stops matching what it was written for. bios:LabProcess was the
     one pin of the 326 keying on a CURIE, and it took #79 to make it dual-form. The other
     325 pin free labels (ICPMS, Electron Source, adaProduct's 114 product names) and are
     correct as a bare string, which is why this rule keys on the SHAPE'S OWN REGEX rather
     than on the presence of a pin.

  B. A value-TYPE declaration must admit the IRI-reference form.

     A declaration that says `type: string` and nothing else forbids {"@id": ...} outright,
     so an emitter cannot serialize an identifier there however correct that would be. This
     is what #77's eight sites were about; five are still open, recorded in OPEN_MANIFEST.

Rule A carries no allowlist -- it is green today and any new violation is a regression.
Rule B has known open debt, so it compares against a recorded manifest: a violation NOT in
the manifest fails, and a manifest entry that NO LONGER violates also fails, because a
manifest that may silently rot is the failure mode docs/SILENT_SUCCESS.md exists to
prevent. Shrinking the manifest is the point; it must be edited deliberately.

Read-only. Exits non-zero on any failure, so it can gate CI.

    python tools/check_additionaltype_policy.py
    python tools/check_additionaltype_policy.py --list   # every declaration, by shape
"""
import glob
import json
import os
import re
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OPEN_MANIFEST = os.path.join(ROOT, "docs", "additionaltype_policy_open.json")
PROPS = ("schema:additionalType", "schema:propertyID")

# Verbatim from metadataBuildingBlocks/_sources/schemaorgProperties/additionalProperty/
# rules.shacl (cdifd:AdditionalTypeUriShouldBeIRIShape / PropertyIDUriShouldBeIRIShape).
# Anchored at both ends, and no whitespace in the local part -- which is exactly why
# 'Smithsonian catalog' and 'synthetic schema:propertyID' are NOT identifiers.
IRI_LIKE = re.compile(r'^[A-Za-z][A-Za-z0-9+.\-]*:[^\s"]+$')


def admits_iri_ref(node):
    """Does this subschema admit {"@id": "..."}?

    Unconstrained is permissive, so it admits one. An object branch requiring @id admits
    one. A $ref is assumed to (cdifConceptOrTermOrString and cdifConceptOrTerm both do);
    resolving every remote ref here would make a read-only checker fetch the network.

    A `const` or `enum` is decided by its VALUE, not by its presence. The parameter $defs
    pin `schema:propertyID: {const: [{"@id": "ada:parameter/..."}]}` -- already the IRI
    form, and already required. Reading the keyword alone and concluding string-only
    reported 1,806 of them as violations.
    """
    if not isinstance(node, dict) or not node:
        return True
    if "$ref" in node:
        return True
    for branch in (node.get("anyOf") or node.get("oneOf") or []):
        if admits_iri_ref(branch):
            return True
    if "@id" in (node.get("properties") or {}):
        return True
    if "const" in node or "enum" in node:
        literals = [node["const"]] if "const" in node else []
        literals += list(node.get("enum", []))
        return any(uses_iri_form(v) for v in literals)
    declared = node.get("type")
    types = declared if isinstance(declared, list) else [declared] if declared else []
    if not types:
        return True
    return "object" in types


def uses_iri_form(value):
    """Is this literal already serialized as an IRI reference (or a wrapper of one)?"""
    if isinstance(value, dict):
        return "@id" in value
    if isinstance(value, list):
        return any(uses_iri_form(v) for v in value)
    return False


def literal_strings(value):
    """Every bare string inside a pinned literal, however it is nested."""
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [s for v in value for s in literal_strings(v)]
    return []


def pinned_literals(node):
    """Every literal this subschema DEMANDS, from contains / const / enum alike.

    Yields (literal, branch_admits_iri). A pin is where an identifier gets frozen as a
    string: `contains: {const: 'bios:LabProcess'}` kept the constraint present and biting
    while no longer matching the converted value (#79). const and enum freeze it the same
    way, so all three are read here rather than only `contains`.
    """
    out = []
    if not isinstance(node, dict):
        return out
    for key in ("contains", "const", "enum"):
        if key not in node:
            continue
        if key == "contains":
            out.extend(pinned_literals(node["contains"]))
            continue
        values = [node["const"]] if key == "const" else list(node["enum"])
        dual = any(uses_iri_form(v) for v in values)
        for value in values:
            for text in literal_strings(value):
                out.append((text, dual))
    for branch in (node.get("anyOf") or node.get("oneOf") or []):
        inner = pinned_literals(branch)
        if any(admits_iri_ref(b) for b in (node.get("anyOf") or node.get("oneOf"))):
            inner = [(lit, True) for lit, _ in inner]
        out.extend(inner)
    return out


def declarations():
    """Every schema:additionalType / schema:propertyID declaration under _sources."""
    for path in sorted(glob.glob(os.path.join(ROOT, "_sources", "**", "schema.yaml"),
                                 recursive=True)):
        try:
            doc = yaml.safe_load(open(path, encoding="utf-8"))
        except Exception as exc:                      # a broken file is another check's job
            print("  !! %s: %s" % (os.path.relpath(path, ROOT), exc))
            continue
        rel = os.path.relpath(path, ROOT).replace(os.sep, "/")

        def walk(node, ptr):
            if isinstance(node, dict):
                for key, value in node.items():
                    if key in PROPS and isinstance(value, dict):
                        yield rel, ptr + "/" + key, value
                    for item in walk(value, ptr + "/" + str(key)):
                        yield item
            elif isinstance(node, list):
                for index, value in enumerate(node):
                    for item in walk(value, ptr + "/" + str(index)):
                        yield item

        for item in walk(doc, ""):
            yield item


def value_node(decl):
    """The subschema governing an individual VALUE (arrays unwrapped to items)."""
    if decl.get("type") == "array" or "items" in decl:
        return decl.get("items") or {}
    return decl


def main():
    decls = list(declarations())

    if "--list" in sys.argv:
        for rel, ptr, decl in decls:
            node = value_node(decl)
            print("%-5s %-46s %s" % ("@id" if admits_iri_ref(node) else "STR",
                                     rel.replace("_sources/", "")[:46], ptr[:84]))
        print("\n%d declarations" % len(decls))
        return 0

    a_fail, b_fail, pins = [], [], 0
    for rel, ptr, decl in decls:
        for literal, dual in pinned_literals(decl):
            pins += 1
            if IRI_LIKE.match(literal) and not dual:
                a_fail.append((rel, ptr, literal))
        if not admits_iri_ref(value_node(decl)):
            b_fail.append((rel, ptr))

    print("declarations examined          : %d" % len(decls))
    print("pinned literals (contains/const/enum) : %d" % pins)
    print()

    print("A. a pinned CURIE/URI must be expressed as an IRI reference")
    if a_fail:
        for rel, ptr, literal in a_fail:
            print("   FAIL %s" % rel.replace("_sources/", ""))
            print("        %s" % ptr)
            print("        pins %r as a bare string only" % literal)
    else:
        print("   ok -- no pin names a CURIE or URI in string-only form")

    recorded = {}
    if os.path.exists(OPEN_MANIFEST):
        with open(OPEN_MANIFEST, encoding="utf-8") as handle:
            recorded = {(e["file"], e["pointer"]): e.get("reason", "")
                        for e in json.load(handle)["open"]}
    found = set(b_fail)
    new = sorted(found - set(recorded))
    stale = sorted(set(recorded) - found)

    print("\nB. a value-type declaration must admit the IRI-reference form")
    print("   recorded open : %d" % len(recorded))
    print("   found         : %d" % len(found))
    for rel, ptr in new:
        print("   FAIL (new) %s" % rel.replace("_sources/", ""))
        print("        %s" % ptr)
    for rel, ptr in stale:
        print("   FAIL (stale manifest entry -- now compliant, remove it)")
        print("        %s  %s" % (rel.replace("_sources/", ""), ptr))
    if not new and not stale:
        print("   ok -- every open site is recorded debt, and all of it is still open")

    bad = len(a_fail) + len(new) + len(stale)
    print("\n%s" % ("FAIL: %d problem(s)" % bad if bad else "PASS"))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
