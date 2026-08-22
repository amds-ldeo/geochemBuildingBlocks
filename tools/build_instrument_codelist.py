#!/usr/bin/env python3
"""Derive the ADA instrument-type and instrument-component-type code lists from the sidecars.

The schema paths select an instrument by a short token —
`schema:instrument[schema:additionalType='SEM']` — and the generated schema turns that token into a
hard `contains` const on schema:additionalType. Until now those tokens were backed by NO controlled
vocabulary (only "EPMA" appeared in any vocab file), so the schema required a literal string that
nothing defined and no lab would know to write. The examples validated only because the generator
emitted the same invented token it then demanded.

This mints the scheme those consts refer to, EMPIRICALLY: the terms are exactly the tokens the
sidecars use, so the vocabulary cannot drift from the paths that depend on it. Re-run it after any
sidecar change that adds or renames an instrument selector.

    python tools/build_instrument_codelist.py            # report
    python tools/build_instrument_codelist.py --write
"""
import argparse
import glob
import json
import os
import re
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VOCAB = os.path.join(ROOT, "_sources", "registry", "vocab")
CODELIST_SCHEMA = ("https://cross-domain-interoperability-framework.github.io/"
                   "metadataBuildingBlocks/_sources/profiles/cdifProfile/cdifCodelist/schema.yaml")
CONTEXT = {"skos": "http://www.w3.org/2004/02/skos/core#",
           "schema": "http://schema.org/",
           "dcterms": "http://purl.org/dc/terms/",
           "ada": "https://ada.astromat.org/metadata/"}

INSTRUMENT = re.compile(r"schema:instrument\[schema:additionalType='([^']*)'\]")
COMPONENT = re.compile(r"schema:instrument\[schema:additionalType='([^']*)'\]"
                       r"\.schema:hasPart\[schema:additionalType='([^']*)'\]")

# skos:notation is the CODE the schema pins; skos:prefLabel is the human-readable preferred label.
# Tokens that are already a readable label (Torch, Collector, Laser Ablation System) keep themselves
# as prefLabel; the split still earns its keep there, because notation preserves the exact token -
# including its warts, e.g. notation "Electron source" with prefLabel "Electron Source".
PREF_LABEL = {
    "SEM": "Scanning Electron Microscope",
    "TEM": "Transmission Electron Microscope",
    "EPMA": "Electron Probe Microanalyser",
    "ICPMS": "Inductively Coupled Plasma Mass Spectrometer",
    "XCT": "X-ray Computed Tomography Scanner",
    "FIBSEM": "Focused Ion Beam Scanning Electron Microscope",
    "EDSDetector": "Energy Dispersive X-ray Spectroscopy Detector",
    "WDSSpectrometer": "Wavelength Dispersive X-ray Spectrometer",
    "BSEDetector": "Backscattered Electron Detector",
    "SEDetector": "Secondary Electron Detector",
    "EELSSpectrometer": "Electron Energy Loss Spectrometer",
    "4DSTEMDetector": "Four-Dimensional Scanning Transmission Electron Microscopy Detector",
    "AberrationCorrector": "Aberration Corrector",
    "ImagingDetector": "Imaging Detector",
    "Electron source": "Electron Source",
    "xrayLine": "X-ray Line",
}


def pref_label(token):
    """The preferred label for a token: a curated expansion, else the token split on CamelCase."""
    if token in PREF_LABEL:
        return PREF_LABEL[token]
    if " " not in token and not token.isupper():
        spaced = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", token)
        if spaced != token:
            return spaced
    return token


def scan():
    """(instrument -> {sidecar}, component -> {sidecar}, component -> {host instrument})"""
    inst, comp, hosts = defaultdict(set), defaultdict(set), defaultdict(set)
    for f in sorted(glob.glob(os.path.join(ROOT, "docs", "*.schemapaths.csv"))
                    + glob.glob(os.path.join(ROOT, "docs", "modules", "*.schemapaths.csv"))):
        tag = os.path.basename(f).replace(".schemapaths.csv", "")
        txt = open(f, encoding="utf-8-sig").read()
        for m in INSTRUMENT.finditer(txt):
            inst[m.group(1)].add(tag)
        for m in COMPONENT.finditer(txt):
            comp[m.group(2)].add(tag)
            hosts[m.group(2)].add(m.group(1))
    return inst, comp, hosts


def concept(scheme_id, token, sidecars, hosts=None):
    label = pref_label(token)
    c = {
        "@id": f"{scheme_id}/{token}",
        "@type": ["skos:Concept"],
        "skos:prefLabel": label,
        "skos:notation": token,
        "skos:inScheme": [{"@id": scheme_id}],
    }
    if label != token:
        c["skos:altLabel"] = [token]      # the code is also a usable label in practice
    if hosts:
        # The instrument(s) this component is a part of, as observed in the sidecars. Recorded as
        # skos:related pointing into the instrument-type scheme, so the part/whole pairing a TAPP
        # asserts through its schema paths is available as data rather than only as prose.
        # (SKOS reserves skos:relatedMatch for cross-scheme associations; skos:related is used here
        # as asked, and the two schemes are siblings of one ADA vocabulary rather than independent
        # published thesauri.)
        c["skos:related"] = [{"@id": "ada:vocab/instrumentType/%s" % h} for h in sorted(hosts)]
    c["skos:scopeNote"] = "Used by %d sidecar(s): %s." % (len(sidecars), ", ".join(sorted(sidecars)[:6]))
    return c


def scheme(scheme_id, label, definition, terms, sidecars, hosts=None):
    return {
        "$schema": CODELIST_SCHEMA,
        "@context": CONTEXT,
        "@id": scheme_id,
        "@type": ["skos:ConceptScheme"],
        "skos:prefLabel": label,
        "skos:definition": definition,
        "schema:identifier": scheme_id,
        "schema:license": ["https://creativecommons.org/licenses/by/4.0/"],
        "skos:hasTopConcept": [
            concept(scheme_id, t, sidecars[t], (hosts or {}).get(t)) for t in sorted(terms)
        ],
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()

    inst, comp, hosts = scan()
    schemes = [
        ("adaInstrumentType.json",
         scheme("ada:vocab/instrumentType", "ADA Instrument Type",
                "The instrument a TAPP schema path selects, as used in "
                "schema:instrument[schema:additionalType='…']. Derived from the schema-path "
                "sidecars, so the vocabulary and the generated consts cannot diverge.",
                inst, inst)),
        ("adaInstrumentComponentType.json",
         scheme("ada:vocab/instrumentComponentType", "ADA Instrument Component Type",
                "A part of an instrument, as used in schema:hasPart[schema:additionalType='…']. "
                "Derived from the schema-path sidecars.",
                comp, comp, hosts)),
    ]
    for fn, doc in schemes:
        n = len(doc["skos:hasTopConcept"])
        print("%-36s %2d concepts" % (fn, n))
        for c in doc["skos:hasTopConcept"]:
            print("     %-28s %s" % (c["skos:notation"], c["skos:scopeNote"][:70]))
        if a.write:
            p = os.path.join(VOCAB, fn)
            with open(p, "w", encoding="utf-8", newline="\n") as f:
                json.dump(doc, f, indent=2, ensure_ascii=False)
                f.write("\n")
            print("     wrote %s" % os.path.relpath(p, ROOT))

    # anomalies worth a human decision rather than silent blessing in a controlled vocabulary
    odd = [t for t in comp if not re.match(r"^[A-Z0-9]", t)]
    mixed = [t for t in list(inst) + list(comp) if " " in t] , [t for t in list(inst) + list(comp) if " " not in t and not t.isupper()]
    print("\nANOMALIES (empirical, not corrected here):")
    if odd:
        print("  lowercase-initial component token(s): %s" % ", ".join(sorted(odd)))
        print("    -> 'xrayLine' is a spectral feature, not hardware; it is the known "
              "'X-ray Line as instrument part' defect.")
    print("  token style is inconsistent: Title Case with spaces (%s) vs CamelCase (%s)"
          % (", ".join(sorted(mixed[0])[:3]), ", ".join(sorted(mixed[1])[:3])))
    if not a.write:
        print("\n(dry run — pass --write)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
