#!/usr/bin/env python3
"""Prototype the proposed cdifCore change and test it against real ADA records.

PROPOSAL (reviewer's, encoded)

  "contentUrl is required if a DataDownload. If the distribution is a Collection, then
   contentUrl is not required if there is a Dataset/schema:url."

Encoding note. The second clause cannot be written inside the distribution ITEM subschema:
JSON Schema has no parent reference, so an item cannot see the Dataset's schema:url. It is
therefore written as the equivalent implication at Dataset scope, which is expressible:

  part 1 (item scope)     schema:distribution items gain a THIRD anyOf branch, a bundle
                          Collection: @type contains schema:Collection, schema:hasPart
                          required, schema:contentUrl NOT required.

  part 2 (dataset scope)  IF any distribution item is a Collection carrying no
                          schema:contentUrl, THEN schema:url is required on the Dataset.

Part 2 carries the same truth as "not required if there is a Dataset/schema:url" while
being checkable, and it makes the landing page mandatory exactly when it is the only
address the record publishes -- which is what cdifCore's own prose asks for:

    schema:url  "...If a direct link is available to get the data, put in
                 distribution/contentUrl"
    distribution "...If user must access data through a landing page, provide link to
                 landing page in the 'url' property for the dataset"
"""
import json
import copy
import os
from jsonschema import Draft202012Validator as V

S = os.path.dirname(os.path.abspath(__file__))
GBB = r"C:\GithubC\amds-ldeo\geochemBuildingBlocks"
PROF = os.path.join(GBB, "_sources", "techniqueProfile", "geochemProfile", "EMPA", "profile",
                    "resolvedSchema.json")

BUNDLE_BRANCH = {
    "type": "object",
    "description": ("A bundle distribution: an archive or package that enumerates its "
                    "component files in schema:hasPart and is retrieved by a route "
                    "published separately (a WebAPI distribution entry, or the dataset's "
                    "landing page in schema:url). It has no direct href of its own, so "
                    "schema:contentUrl is not required."),
    "properties": {
        "@type": {"type": "array", "items": {"type": "string"},
                  "contains": {"const": "schema:Collection"}, "minItems": 1},
        "schema:hasPart": {"type": "array", "minItems": 1},
    },
    "required": ["@type", "schema:hasPart"],
}

DATASET_RULE = {
    "description": ("If a bundle Collection publishes no schema:contentUrl, the dataset "
                    "must publish a landing page in schema:url -- otherwise the record "
                    "states no way to reach the data at all."),
    "if": {
        "properties": {
            "schema:distribution": {
                "type": "array",
                "contains": {
                    "type": "object",
                    "properties": {"@type": {"type": "array",
                                             "contains": {"const": "schema:Collection"}}},
                    "required": ["@type"],
                    "not": {"required": ["schema:contentUrl"]},
                },
            }
        },
        "required": ["schema:distribution"],
    },
    "then": {"required": ["schema:url"]},
}


def patched(schema):
    d = copy.deepcopy(schema)
    d["properties"]["schema:distribution"]["items"]["allOf"][0]["anyOf"].append(
        copy.deepcopy(BUNDLE_BRANCH))
    d.setdefault("allOf", []).append(copy.deepcopy(DATASET_RULE))
    return d


if __name__ == "__main__":
    base = json.load(open(PROF, encoding="utf-8"))
    prop = patched(base)
    vb, vp = V(base), V(prop)

    def errs(v, doc):
        return [e for e in v.iter_errors(doc)]

    def dist_errs(v, doc):
        return [e for e in v.iter_errors(doc)
                if list(e.absolute_path)[:1] == ["schema:distribution"]]

    for doi in ("an7h-fg87", "3xec-yw98"):
        rec = json.load(open(os.path.join(S, "ada_record_%s.json" % doi), encoding="utf-8"))
        print("%-12s  total %2d -> %2d   distribution %d -> %d"
              % (doi, len(errs(vb, rec)), len(errs(vp, rec)),
                 len(dist_errs(vb, rec)), len(dist_errs(vp, rec))))

    # negative control: the branch must NOT let a bundle through with no address at all
    rec = json.load(open(os.path.join(S, "ada_record_an7h-fg87.json"), encoding="utf-8"))
    bad = copy.deepcopy(rec)
    bad.pop("schema:url", None)
    print("\nnegative control - bundle with NO schema:url and no contentUrl:")
    print("   under the proposal: %d error(s) %s"
          % (len(errs(vp, bad)),
             "-- REJECTED, as intended" if len(errs(vp, bad)) > len(errs(vp, rec))
             else "-- NOT rejected, rule is too weak"))
    # second control: a non-Collection DataDownload must still need contentUrl
    bad2 = copy.deepcopy(rec)
    bad2["schema:distribution"][0]["@type"] = ["schema:DataDownload"]
    print("negative control - plain DataDownload, no contentUrl:")
    print("   under the proposal: distribution errors %d %s"
          % (len(dist_errs(vp, bad2)),
             "-- still required, as intended" if dist_errs(vp, bad2)
             else "-- LEAK: contentUrl no longer enforced"))
