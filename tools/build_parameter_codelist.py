"""Aggregate the ADA parameter registries into one CDIF-codelist skos:ConceptScheme.

Reads the three cross-TAPP parameter registries —
  techniqueProtocols/parameterValues     (schema:PropertyValue, read-only session values)
  techniqueProtocols/parameterTemplates  (schema:PropertyValueSpecification, editable defaults)
  techniqueProtocols/analyteColumns      (per-analyte column definitions)
— and emits a single master vocabulary of analytical-parameter concepts at
`_sources/techniqueProtocols/vocab/adaAnalyticalParameters.json`, conformant to the
CDIF codelist profile.

Each registry $def already carries the parameter's own resolvable @id
(`ada:parameter/<tapp>/<name>` or `ada:targetSpeciesColumn/<tapp>/<name>`) — the same URI used
as `schema:propertyID` in TAPP/detail instances — plus a title (label) and description.
Those become the skos:Concept @id, skos:prefLabel, and skos:definition, so a propertyID in
any example now dereferences to a concept definition here (the geochem analog of the XAS
SKOS glossary).

Run after the per-TAPP builds (which populate the registries):
    python tools/build_parameter_codelist.py
"""
import json
import os
import sys
from collections import OrderedDict

import yaml

import _tapp_lib as _L

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG = os.path.join(ROOT, "_sources", "registry")
REGISTRIES = ["parameterValues", "parameterTemplates", "targetSpeciesColumns"]
SCHEME_ID = "ada:vocab/adaAnalyticalParameters"
OUT = os.path.join(REG, "vocab", "adaAnalyticalParameters.json")


def _load_defs(registry):
    # read the registry's schema.yaml $defs (the bundled *Schema.json was removed in the reorg)
    path = os.path.join(REG, registry, "schema.yaml")
    with open(path, encoding="utf-8") as f:
        d = yaml.safe_load(f)
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
    # RETIRED GENERATOR — the layer it published belongs to the parameter register, not to
    # registry/vocab. Its output was a SKOS copy of the six parameter/column registers' $defs:
    # 1800 notations that are FIELD NAMES, not controlled values, so it was never a vocabulary of
    # allowed values at all. Measured 2026-10-28, the two copies had already drifted — 1699
    # notations overlapped, 101 existed ONLY in the SKOS copy (two superseded naming generations:
    # ~36 <technique>_samplePersistentIdentifierDefault, and ~25 bare unprefixed names including
    # elementEstimationMethod, epmaTechnique, monochromatorCrystal and wdsDetectorType), and 81
    # $defs existed only in the register, among them all 16 ebsd_* and 10 stem_*.
    #
    # Stephen retired it 2026-10-28: metadata field names are defined in the parameter register.
    # adaAnalyticalParameters.json is deleted in the same commit, and running this would recreate
    # it — the exact drift the 49 orphan deletions were about — so writing is blocked.
    # tools/draft_variable_registry.py models this layer as cdi:RepresentedVariables.
    if "--force-deprecated" not in sys.argv:
        print("ERROR: build_parameter_codelist.py is RETIRED - its 1800 notations are field names,\n"
              "       not controlled values, and the parameter register is their home.\n"
              "       registry/vocab/adaAnalyticalParameters.json has been deleted; this would\n"
              "       recreate it. See tools/draft_variable_registry.py for the layer that owns\n"
              "       them, or pass --force-deprecated to override intentionally.",
              file=sys.stderr)
        sys.exit(2)
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
