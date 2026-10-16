"""Backfill `ada:submissionType` into the static examples that no pipeline regenerates.

`adaProduct` requires it as of 2026-10-16. The 38 examples that validate against adaProduct's own
layer are the STATIC category -- the BaseSchema fixtures and the `adaProfile` / `profile-ada`
examples -- and nothing regenerates them: `generate_profiles.py` is deprecated and refuses to run,
so no regeneration will ever add the field or correct a mistake in one. Same reason
`add_instrument_ids.py` exists.

So this is a one-shot written down rather than done by hand, because an unreproducible backfill
cannot be re-run when the next required property lands, and because 38 hand edits is 38 chances
to mistype a key that no generator would catch.

It does NOT touch the generated examples. Those come from `build_tapp_examples` via the schema
path emitter, and a field the emitter does not know about has to be added THERE or the next
regeneration removes it again. None of the 38 are generated -- verified by the block list below,
which is derived from what actually carries adaProduct's layer rather than from a hardcoded path
list.

The value is `BundleDelivery`, the corpus majority: 7,071 of 7,447 records against 376 `Regular`,
counted over public.json_table on 2026-10-16. These are illustrative fixtures, not records, so the
representative value is the right one; `--value` overrides it.

    python tools/add_submission_type.py            # report what would change
    python tools/add_submission_type.py --write
"""
import argparse
import glob
import io
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "_sources")
KEY = "ada:submissionType"

# adaProduct's own layer is identifiable in a resolved schema by this property. Deriving the block
# list from the resolved artifacts rather than listing directories keeps it correct when a profile
# is added or re-based: a new adaProduct-based block is picked up without editing this file.
MARKER = '"%s"' % KEY


def affected():
    for p in sorted(glob.glob(os.path.join(SRC, "**", "resolvedSchema.json"), recursive=True)):
        try:
            if MARKER not in io.open(p, encoding="utf-8").read():
                continue
        except OSError:
            continue
        d = os.path.dirname(p)
        for f in sorted(glob.glob(os.path.join(d, "example*.json"))):
            if ".provenance" not in f:
                yield f


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--value", default="BundleDelivery")
    a = ap.parse_args()

    added = present = 0
    for f in affected():
        with io.open(f, encoding="utf-8") as fh:
            doc = json.load(fh)
        if KEY in doc:
            present += 1
            continue
        # Drop the superseded unprefixed spelling if an example still carries it: two keys for one
        # fact is what the rename was for.
        doc.pop("submissionType", None)
        # Rebuilt in order so the new key sits beside schema:additionalType, which is the other
        # delivery-level claim, rather than at the end.
        out, placed = {}, False
        for k, v in doc.items():
            out[k] = v
            if k == "schema:additionalType":
                out[KEY] = a.value
                placed = True
        if not placed:
            out[KEY] = a.value
        added += 1
        print("  + %s" % os.path.relpath(f, SRC).replace(os.sep, "/"))
        if a.write:
            # indent=2 + ensure_ascii=False + trailing newline round-trips these files
            # byte-for-byte, verified before this was written, so the diff is the added line alone.
            with io.open(f, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(json.dumps(out, indent=2, ensure_ascii=False) + "\n")

    total = added + present
    print("\nexamples carrying adaProduct's layer : %d" % total)
    print("  already had %-24s : %d" % (KEY, present))
    print("  %-34s : %d" % ("added" if a.write else "would add", added))

    # A zero here means "no block carries the property" and reads identically to "all done",
    # which is this repository's most expensive failure mode. The usual cause is ORDER: the
    # marker is the NEW property name, so it appears in resolvedSchema.json only after the
    # schema edit has been regenerated. Fail rather than report a clean nothing.
    if total == 0:
        print("\nERROR: no block's resolvedSchema.json mentions %s, so this found nothing to\n"
              "check -- which is not the same as nothing to do. Either adaProduct no longer\n"
              "declares the property, or the schema edit has not been regenerated yet:\n"
              "\n    python tools/regenerate.py\n"
              "\nRun that first, then this." % KEY)
        return 1
    if added and not a.write:
        print("\nnothing written; pass --write")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
