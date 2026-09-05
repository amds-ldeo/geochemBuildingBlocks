#!/usr/bin/env python3
"""Regenerate the pipeline in dependency order. One entrypoint, because the order is load-bearing.

    python tools/regenerate.py                 # everything
    python tools/regenerate.py --tapp semTAPP  # one technique (modules and resolve still run)
    python tools/regenerate.py --dry-run       # print the plan, run nothing
    python tools/regenerate.py --from profile  # resume at a stage, after fixing something

The stages below are not a checklist, they are a dependency chain, and running them out of order
fails SILENTLY. Two instances on 2026-09-03, both of which produced a green validate_examples:

  modules before simplify.  simplify_sidecars blanks a technique row when a module covers the
      field. Deciding that against module BBs which had not been rebuilt since their sidecars
      changed deleted `Limit of Quantification (LOQ) Method` from nine ICP-MS schemas. The planner
      now reads docs/modules/emitted.json so it fails closed, but the BBs still have to be built
      before anything reasons about what they cover.

  resolve before build_profile.  build_profile backfills the variableMeasured entries its examples
      need by reading profile/resolvedSchema.json to see which variables the COMPOSED schema pins
      with a `contains`. Run in the same pass that produces that file, it reads the previous one
      and misses whatever the composition just added — 16 hand-authored profile examples failed
      until it was re-run against current resolved schemas.

Neither is visible to validate_examples: dropping a constraint only makes a schema more
permissive, so every example still passes. The order is the guard.
"""
import argparse
import os
import subprocess
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_tapp as b  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(ROOT, "tools")

# (stage, description, per-technique?)  in dependency order
STAGES = [
    ("modules", "build the module BBs and docs/modules/emitted.json from the module sidecars",
     False),
    ("simplify", "blank technique rows a module now covers (reads emitted.json)", False),
    ("tapp", "registry catalogs + vocab, per technique", True),
    ("pathdriven", "tapp/ and detail/ schemas from the sidecar, per technique", True),
    ("profile-1", "profile/ schema, per technique", True),
    ("resolve", "resolvedSchema.json everywhere", False),
    ("profile-2", "profile/ again: backfill example variables now that resolve has run", True),
    ("examples", "publication-derived example*.json, per technique", True),
    ("mirrors", "*Schema.json from schema.yaml", False),
]


def run(cmd, dry):
    printable = " ".join(x if " " not in x else f'"{x}"' for x in cmd[1:])
    if dry:
        print(f"      would run: python {printable}")
        return 0
    r = subprocess.run([sys.executable] + cmd[1:], cwd=ROOT, capture_output=True,
                       text=True, encoding="utf-8", errors="replace")
    if r.returncode:
        print(f"      FAILED: python {printable}", flush=True)
        print((r.stderr or r.stdout or "")[-2000:])
    return r.returncode


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tapp", action="append", default=[],
                    help="limit the per-technique stages to these (repeatable); the module, "
                         "simplify, resolve and mirror stages always run over everything, "
                         "because they are shared")
    ap.add_argument("--from", dest="start", choices=[s for s, _, _ in STAGES],
                    help="resume at this stage")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    tapps = a.tapp or sorted(b.TAPP_CONFIGS)
    unknown = [t for t in tapps if t not in b.TAPP_CONFIGS]
    if unknown:
        raise SystemExit(f"unknown TAPP(s): {', '.join(unknown)}")

    stages = STAGES
    if a.start:
        i = [s for s, _, _ in STAGES].index(a.start)
        stages = STAGES[i:]
        print(f"resuming at '{a.start}' — {len(STAGES) - len(stages)} earlier stage(s) skipped\n")

    fail = []
    for stage, why, per_tapp in stages:
        t0 = time.time()
        print(f"[{stage}] {why}", flush=True)
        if stage == "modules":
            fail += [(stage, "")] if run(["", os.path.join(TOOLS, "build_module_bb.py"),
                                          "--write"], a.dry_run) else []
        elif stage == "simplify":
            fail += [(stage, "")] if run(["", os.path.join(TOOLS, "simplify_sidecars.py"),
                                          "--write"], a.dry_run) else []
        elif stage == "resolve":
            fail += [(stage, "")] if run(["", os.path.join(TOOLS, "resolve_schema.py"),
                                          "--all"], a.dry_run) else []
        elif stage == "mirrors":
            fail += [(stage, "")] if run(["", os.path.join(TOOLS, "regenerate_schema_json.py")],
                                         a.dry_run) else []
        else:
            script = {"tapp": "build_tapp.py", "pathdriven": "build_pathdriven.py",
                      "profile-1": "build_profile.py", "profile-2": "build_profile.py",
                      "examples": "build_tapp_examples.py"}[stage]
            for t in tapps:
                if run(["", os.path.join(TOOLS, script), t], a.dry_run):
                    fail.append((stage, t))
        print(f"      {time.time() - t0:.0f}s\n" if not a.dry_run else "", flush=True)

    if fail:
        print("FAILURES:")
        for s, t in fail:
            print(f"   {s} {t}")
        return 1
    if not a.dry_run:
        print("Regeneration complete. Now verify — the pipeline cannot tell you a field went "
              "missing:\n"
              "   python tools/validate_examples.py\n"
              "   python tools/audit_building_blocks.py\n"
              "   python tools/intake_delivery.py --checks-only\n"
              "   python tools/check_componentType.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
