"""Aggregate the ADA parameter registries into one CDIF-codelist skos:ConceptScheme.

Reads the three cross-TAPP parameter registries —
  techniqueProtocols/parameterValues     (schema:PropertyValue, read-only session values)
  techniqueProtocols/parameterTemplates  (schema:PropertyValueSpecification, editable defaults)
  techniqueProtocols/analyteColumns      (per-analyte column definitions)
— and emits a single master vocabulary of analytical-parameter concepts at
`_sources/techniqueProtocols/vocab/adaAnalyticalParameters.json`, conformant to the
CDIF codelist profile.

Each registry $def already carries the parameter's own resolvable @id
(`ada:parameter/<tapp>/<name>` or `ada:analyteColumn/<tapp>/<name>`) — the same URI used
as `schema:propertyID` in TAPP/detail instances — plus a title (label) and description.
Those become the skos:Concept @id, skos:prefLabel, and skos:definition, so a propertyID in
any example now dereferences to a concept definition here (the geochem analog of the XAS
SKOS glossary).

Run after the per-TAPP builds (which populate the registries):
    python tools/build_parameter_codelist.py
"""
import json
import os
from collections import OrderedDict

import _tapp_lib as _L

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TP = os.path.join(ROOT, "_sources", "techniqueProtocols")
REGISTRIES = ["parameterValues", "parameterTemplates", "analyteColumns"]
SCHEME_ID = "ada:vocab/adaAnalyticalParameters"
OUT = os.path.join(TP, "vocab", "adaAnalyticalParameters.json")


def _load_defs(registry):
    path = os.path.join(TP, registry, f"{registry}Schema.json")
    with open(path, encoding="utf-8") as f:
        d = json.load(f)
    return d.get("$defs", d.get("definitions", {}))


def _concept(param_id, notation, pref_label, definition):
    c = OrderedDict([
        ("@id", param_id),
        ("@type", ["skos:Concept"]),
        ("skos:prefLabel", pref_label),
        ("skos:notation", notation),
        ("skos:inScheme", [{"@id": SCHEME_ID}]),
    ])
    if definition:
        c["skos:definition"] = definition
    return c


def main():
    concepts = []
    seen = set()
    for registry in REGISTRIES:
        for key, spec in _load_defs(registry).items():
            props = spec.get("properties", {})
            pid = props.get("@id", {}).get("const")
            if not pid or pid in seen:
                continue
            seen.add(pid)
            label = spec.get("title") or props.get("schema:name", {}).get("const") or key
            concepts.append(_concept(pid, key, label, spec.get("description")))
    concepts.sort(key=lambda c: c["@id"])

    scheme = _L.concept_scheme_obj(
        SCHEME_ID,
        "ADA Analytical Parameters",
        ("Controlled vocabulary of analytical parameters referenced by ADA TAPP definitions "
         "and analysis-specific detail blocks: protocol/session parameters (schema:PropertyValue "
         "and schema:PropertyValueSpecification) and per-analyte column definitions. Each concept "
         "@id is the parameter's schema:propertyID URI."),
        concepts,
    )
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(json.dumps(scheme, indent=2, ensure_ascii=False) + "\n")
    print(f"wrote {os.path.relpath(OUT, ROOT)} with {len(concepts)} parameter concepts")


if __name__ == "__main__":
    main()
