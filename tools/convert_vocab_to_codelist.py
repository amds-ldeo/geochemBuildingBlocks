"""In-place migration: convert any legacy schema:DefinedTermSet vocab file to a
CDIF-codelist-conformant skos:ConceptScheme.

The TAPP generator (tools/build_tapp.py via _tapp_lib.vocab_obj) now emits ConceptScheme
directly, so a freshly regenerated vocab is already conformant. This pass catches files a
current workbook no longer regenerates (orphans from renamed/retired rows) so that the whole
`_sources/techniqueProtocols/vocab/` directory is uniform. Idempotent: files already typed
skos:ConceptScheme are left untouched. The scheme @id is preserved, so every
`schema:inDefinedTermSet` reference keeps resolving.

    python tools/convert_vocab_to_codelist.py [--dry-run]
"""
import glob
import json
import os
import sys
from collections import OrderedDict

import _tapp_lib as _L

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VOCAB_DIR = os.path.join(ROOT, "_sources", "registry", "vocab")


def _terms(doc: dict):
    """Yield (notation, prefLabel, definition) from either a legacy
    schema:DefinedTermSet or an existing skos:ConceptScheme, so the pass both
    migrates old files and re-normalizes already-converted ones to the current
    concept shape."""
    for term in doc.get("schema:hasDefinedTerm", []):
        code = term.get("schema:termCode") or term.get("schema:name")
        yield code, term.get("schema:name") or code, term.get("schema:description")
    for c in doc.get("skos:hasTopConcept", []):
        notation = c.get("skos:notation")
        if isinstance(notation, list):
            notation = notation[0] if notation else None
        code = notation or c.get("skos:prefLabel")
        yield code, c.get("skos:prefLabel") or code, c.get("skos:definition")


def convert(doc: dict) -> "OrderedDict":
    scheme_id = doc["@id"]
    label = doc.get("schema:name") or doc.get("skos:prefLabel") or scheme_id.rsplit("/", 1)[-1]
    desc = doc.get("schema:description") or doc.get("skos:definition") or ""
    concepts = [_L.concept_obj(scheme_id, code, pref, defn)
                for code, pref, defn in _terms(doc)
                if code and code not in ("N/A", "None")]
    return _L.concept_scheme_obj(scheme_id, label, desc, concepts)


# Empty since 2026-10-28. Its one entry was adaAnalyticalParameters.json, which was skipped
# because build_parameter_codelist.py owned it and its concept @ids were parameter propertyID
# URIs rather than scheme-scoped. Both the file and that generator are retired — field names
# belong to the parameter register, not to a vocabulary — so there is nothing to exclude. The
# mechanism is kept for the next codelist another generator owns.
SKIP_FILES = set()


def main():
    dry = "--dry-run" in sys.argv
    converted = skipped = 0
    for path in sorted(glob.glob(os.path.join(VOCAB_DIR, "*.json"))):
        if os.path.basename(path) in SKIP_FILES:
            skipped += 1
            continue
        with open(path, encoding="utf-8") as f:
            doc = json.load(f)
        types = doc.get("@type", [])
        if "schema:DefinedTermSet" not in types and "skos:ConceptScheme" not in types:
            print(f"  SKIP (unexpected @type): {os.path.basename(path)}")
            skipped += 1
            continue
        new = convert(doc)
        rel = os.path.relpath(path, ROOT)
        if dry:
            print(f"  would normalize {rel} ({len(new['skos:hasTopConcept'])} concepts)")
        else:
            with open(path, "w", encoding="utf-8") as f:
                f.write(json.dumps(new, indent=2, ensure_ascii=False) + "\n")
        converted += 1
    print(f"{'would normalize' if dry else 'normalized'} {converted}; {skipped} skipped")


if __name__ == "__main__":
    main()
