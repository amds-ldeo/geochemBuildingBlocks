#!/usr/bin/env python3
"""Check sidecar placements against the tier-shape rules.

The tier pair decides SHAPE, not just requiredness, and the rules were being applied from memory —
which is how `CL Grating` ended up as a bare `ada:clGrating` on the instrument in one sidecar and a
`$Dataset.ada:clWavelengthRange` in another. Two rules are checked:

  ADVANCED / READ-ONLY   the procedure states a fixed value that the analyst cannot change, so it
                         belongs in a `schema:additionalProperty` bag, not as a first-class
                         `ada:` property.

  BASIC / EDITABLE       dual-homed. The $MethodDefinition side is the procedure default and its
                         property name carries a `Default` suffix; the $Dataset side is the
                         per-analysis value and is a `schema:additionalProperty`.

Reports violations; fixes nothing. A placement can be a deliberate exception, and only a reviewer
knows which — this exists so the exceptions are visible rather than accidental.

    python tools/check_tier_rules.py                 # every sidecar
    python tools/check_tier_rules.py empaTAPP semTAPP
"""
import os
import re
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_tapp as b
import schemapath_io

ADDL = "schema:additionalProperty"

# The tier-shape rules govern PARAMETERS. A field that maps onto a first-class CDIF / schema.org
# structure is modelled by that structure's own shape, and forcing it into an additionalProperty bag
# or renaming it to `…Default` would break the very alignment it exists for: a laboratory is a
# schema:location, an instrument component is a hasPart, a reported property is a variableMeasured.
# Exempting them is what makes the remaining violations worth reading.
FIRST_CLASS = (
    "schema:location", "schema:funding", "schema:relatedLink", "schema:creator", "schema:agent",
    "bios:computationalTool", "bios:reagent", "schema:object", "schema:identifier",
    "schema:hasPart", "schema:variableMeasured", "ada:analyteTemplate", "ada:reportedProperties",
    # keyed templates: the members carry the per-instance value, so there is no separate
    # $Dataset parameter to pair a default with
    "ada:channelTemplate", "ada:reportedPropertyTemplate",
    "dqv:hasQualityMeasurement", "schema:actionProcess", "schema:name", "schema:description",
    "schema:version", "schema:datePublished", "ada:samplingUnit",
    # A distribution's encodingFormat is a first-class CDIF slot on schema:distribution, not a
    # parameter of the procedure: the format is a fact about the file, and CDIF's dataDownload
    # already fixes its shape (an array of strings). Forcing it into an additionalProperty bag would
    # break that alignment for no gain.
    "schema:distribution", "schema:encodingFormat",
)


def first_class(path):
    return any(tok in path for tok in FIRST_CLASS)


def norm_tier(v):
    return re.sub(r"[^a-z]+", "", (v or "").lower())


def leaf_property(path):
    """The last `prefix:name` token, ignoring any [selector] and the value leaf."""
    p = re.sub(r"\[[^\]]*\]", "", path or "")
    toks = [t for t in p.split(".") if ":" in t]
    return toks[-1] if toks else ""


def check(tapp):
    b.configure(tapp)
    csv_path = schemapath_io.csv_path(b.XLSX)
    if not os.path.exists(csv_path):
        return []
    byitem = defaultdict(list)
    for r in schemapath_io.read(csv_path):
        it = (r.get("Metadata Item") or "").strip()
        p = (r.get("Schema Path") or "").strip()
        if it and p:
            byitem[it].append((p, norm_tier(r.get("Protocol Tier")),
                               norm_tier(r.get("Analysis Tier")), (r.get("Source") or "").strip()))

    out = []
    name = os.path.basename(csv_path).replace(".schemapaths.csv", "")
    for item, rows in sorted(byitem.items()):
        P, A = rows[0][1], rows[0][2]
        paths = [p for p, _, _, _ in rows]
        src = rows[0][3]

        if P == "advanced" and A == "readonly":
            bad = [p for p in paths if ADDL not in p and not first_class(p)]
            for p in bad:
                out.append((name, item, "Advanced/Read-Only", src,
                            "not a schema:additionalProperty", p))

        if P == "basic" and A == "editable":
            md = [p for p in paths if p.startswith("$MethodDefinition")]
            ds = [p for p in paths if p.startswith("$Dataset")]
            if any(first_class(p) for p in paths):
                continue
            if not md or not ds:
                out.append((name, item, "Basic/Editable", src,
                            "dual-homed tier but only the %s side is placed"
                            % ("$MethodDefinition" if md else "$Dataset"), paths[0]))
            for p in md:
                if ADDL in p:
                    continue          # a default inside an additionalProperty bag is fine
                if not leaf_property(p).endswith("Default"):
                    out.append((name, item, "Basic/Editable", src,
                                "procedure default lacks the `Default` suffix", p))
            for p in ds:
                if ADDL not in p:
                    out.append((name, item, "Basic/Editable", src,
                                "analysis value is not a schema:additionalProperty", p))
    return out


def main():
    targets = sys.argv[1:] or sorted(b.TAPP_CONFIGS)
    allv = []
    for t in targets:
        allv.extend(check(t))
    if not allv:
        print("No tier-shape violations.")
        return 0
    bysc = defaultdict(list)
    for v in allv:
        bysc[v[0]].append(v)
    for sc in sorted(bysc):
        print("\n%s  (%d)" % (sc, len(bysc[sc])))
        for _, item, tier, src, why, p in bysc[sc]:
            print("   %-44s %-18s %-9s %s" % (item[:43], tier, src, why))
            print("        %s" % p)
    print("\n%d violation(s) across %d sidecar(s)" % (len(allv), len(bysc)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
