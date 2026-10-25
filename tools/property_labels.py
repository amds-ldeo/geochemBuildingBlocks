"""Human-readable `title` labels for generated schemas.

A generator that COMPLETELY redefines a property discards whatever title the base
carried, because `resolve_schema.deep_merge` replaces rather than merges once the
overlay has a `type`, `$ref` or composition keyword. That is why `prov:wasGeneratedBy`
reached 0 of 34 technique profiles after the record-side labels landed, while
`schema:additionalType` -- redefined next to it with no `type` -- survived in all 34.

The fix is for the generator to carry the label over. The labels are NOT stated here:
`record_labels()` reads them from geochemProduct and `container_labels()` from
tappDefinition, each the block that defines the properties in question, so every
label has one home. A dict of labels in this file would be the second-home shape this
repo keeps retiring (`ada:procedureAuthorDescription`, and `ada:resultTarget` in #212).

WHICH APPLICATION MODE A PROPERTY NEEDS DEPENDS ON WHETHER ITS MEANING TRAVELS:

    meaning invariant across positions  ->  safe to label BY NAME, recursively
    meaning varies by position          ->  must be labelled BY POSITION

That distinction is the ADA metadata view session's, measured over 7,447 records, and
it is the reason for the two functions rather than one. `schema:email` is the first
kind: three populated positions -- a creator's, a contributor's, a maintainer's -- all
meaning a person's email, where the parent label already says whose. `schema:identifier`
is the second: nine positions holding a dataset DOI, a session id, an instrument code,
a lab ROR, a sample IGSN, two ORCIDs, a technique term and a maintainer id. One label
would be wrong at eight of them.

  `label_overlay`  direct properties of the root and of each top-level allOf entry --
                   the dataset-root properties, which are what end up at a consuming
                   profile's root. Deliberately NOT recursive: `schema:name` occurs 512
                   times inside the detail blocks, nearly all at nested positions where
                   the record-root label is wrong, because a sample's name is not the
                   dataset's name.

  `label_by_name`  recursive, for the invariant kind. Only `CONTAINER_KEYS` qualifies.
                   `schema:additionalProperty` is excluded on purpose: 161 nested
                   positions in the tapp sources alone, serving the procedure's
                   parameters, an instrument's properties and a workflow step's.

A label must never equal a block's own top-level title: the metadata viewer treats such
a title as a type name and drops it, because after resolution an inlined block sits AT
the property node and only the value distinguishes it. `check_label_collisions` asserts
that rather than leaving it to a reviewer.

And a label should not name an identifier SCHEME a value might not use -- "Person
Identifier" rather than "ORCID", "Laboratory Identifier" rather than "Laboratory ROR" --
or the label asserts something the data can contradict.
"""
import os

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GEOCHEM_PRODUCT = os.path.join(ROOT, "_sources", "BaseSchema", "geochemProduct", "schema.yaml")

TAPP_DEFINITION = os.path.join(ROOT, "_sources", "BaseSchema", "tappDefinition", "schema.yaml")

# WHICH procedure-side names carry one meaning wherever they appear. That is a
# structural claim, not a label, so it lives in code; the labels themselves are READ
# from tappDefinition, which declares all eleven. schema:additionalProperty is absent
# on purpose -- 161 nested positions in the tapp sources alone, serving the
# procedure's parameters, an instrument's properties and a workflow step's, so no one
# label is right for all of them.
CONTAINER_KEYS = frozenset({
    "ada:targetSpeciesColumns", "ada:monitoredPropertyColumns",
    "ada:targetMaterialColumns", "ada:reportedPropertyColumns",
    "ada:defaultTargetSpecies", "ada:defaultMonitoredProperties",
    "ada:defaultTargetMaterials", "ada:targetSpeciesTemplate",
    "ada:monitoredPropertyTemplate", "ada:targetMaterialTemplate",
    "ada:reportedPropertyTemplate",
})

_record_cache = None
_container_cache = None


def record_labels():
    """{property: title} as authored in geochemProduct's own overlay.

    Read, never restated, so the labels have one home. Returns {} rather than raising
    if the file cannot be read: a missing label is a raw key in a viewer, which is
    recoverable, where a failed regeneration is not.
    """
    global _record_cache
    if _record_cache is not None:
        return _record_cache
    labels = {}
    try:
        with open(GEOCHEM_PRODUCT, encoding="utf-8") as fh:
            doc = yaml.safe_load(fh)
    except Exception:
        _record_cache = {}
        return _record_cache
    for entry in [doc] + list((doc or {}).get("allOf") or []):
        if not isinstance(entry, dict):
            continue
        for key, node in (entry.get("properties") or {}).items():
            if isinstance(node, dict) and isinstance(node.get("title"), str):
                labels.setdefault(key, node["title"])
    _record_cache = labels
    return labels


def container_labels():
    """{container: title} for CONTAINER_KEYS, as authored in tappDefinition.

    tappDefinition is the defining block for all eleven, so labelling them there
    covers every consumer through the $ref; this pass exists for a technique overlay
    that completely redefines one and would otherwise discard the base title.
    """
    global _container_cache
    if _container_cache is not None:
        return _container_cache
    labels = {}
    try:
        with open(TAPP_DEFINITION, encoding="utf-8") as fh:
            doc = yaml.safe_load(fh)
    except Exception:
        _container_cache = {}
        return _container_cache
    stack = [doc]
    while stack:
        node = stack.pop()
        if isinstance(node, dict):
            for key, child in (node.get("properties") or {}).items():
                if (key in CONTAINER_KEYS and isinstance(child, dict)
                        and isinstance(child.get("title"), str)):
                    labels.setdefault(key, child["title"])
            stack.extend(node.values())
        elif isinstance(node, list):
            stack.extend(node)
    _container_cache = labels
    return labels


def _block_titles():
    """Every block's own top-level title, from both source trees."""
    titles = set()
    for sub in ("_sources", os.path.join("vendor", "remote")):
        base = os.path.join(ROOT, sub)
        if not os.path.isdir(base):
            continue
        for dirpath, _dirnames, filenames in os.walk(base):
            if "schema.yaml" not in filenames:
                continue
            try:
                with open(os.path.join(dirpath, "schema.yaml"), encoding="utf-8") as fh:
                    doc = yaml.safe_load(fh)
            except Exception:
                continue
            if isinstance(doc, dict) and isinstance(doc.get("title"), str):
                titles.add(doc["title"])
    return titles


def check_label_collisions(labels):
    """Return the labels that equal a block title, and would therefore be dropped."""
    return sorted(set(labels.values()) & _block_titles())


def _apply(props, labels):
    n = 0
    for key, node in (props or {}).items():
        if not isinstance(node, dict) or key not in labels:
            continue
        if isinstance(node.get("title"), str):
            continue          # an authored or already-carried title wins
        node["title"] = labels[key]
        n += 1
    return n


def label_overlay(schema, labels=None):
    """Label the dataset-root properties: the root's own, and each top-level allOf
    entry's own. NOT recursive -- see this module's docstring for why."""
    labels = record_labels() if labels is None else labels
    if not isinstance(schema, dict):
        return 0
    n = _apply(schema.get("properties"), labels)
    for entry in schema.get("allOf") or []:
        if isinstance(entry, dict):
            n += _apply(entry.get("properties"), labels)
    return n


def label_by_name(schema, labels=None):
    """Label every occurrence of these property names, at any depth. Only for names
    that carry one meaning wherever they appear."""
    labels = container_labels() if labels is None else labels
    n = 0
    stack = [schema]
    while stack:
        node = stack.pop()
        if isinstance(node, dict):
            n += _apply(node.get("properties"), labels)
            stack.extend(node.values())
        elif isinstance(node, list):
            stack.extend(node)
    return n
