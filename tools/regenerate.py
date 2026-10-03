#!/usr/bin/env python3
"""Regenerate the pipeline in dependency order. One entrypoint, because the order is load-bearing.

    python tools/regenerate.py                 # everything
    python tools/regenerate.py --tapp semTAPP  # one technique (modules/simplify still run;
                                               #   resolve is scoped to that technique)
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
      and misses whatever the composition just added — 16 profile examples failed
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
import build_profile as bprof  # noqa: E402  — PROFILES, for the profile-stage filter

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


def run(cmd, dry, attempts=3, stream=False):
    """Run one stage. Retries ONLY an Errno 22 write fault, never a real build failure.

    Windows intermittently refuses `open(path, "w")` with `OSError: [Errno 22] Invalid argument`
    when something else is momentarily holding the file -- an indexer, antivirus, an open workbook.
    It is not a build error and it does not repeat on the same file twice in a row, but a single
    occurrence used to fail its technique and leave the run's later stages reasoning over a
    half-written registry. On 2026-09-25 one such window took out a dozen consecutive techniques
    in the `tapp` stage and wrecked a 30-minute run.

    The condition is deliberately narrow: the output must actually name Errno 22. A genuine failure
    still fails on the first attempt, because retrying a real error three times only delays it and
    buries the traceback under duplicates.

    stream=True hands the child our stdout and stderr instead of capturing them, for a stage long
    enough that silence is indistinguishable from a stall. Capture is what makes the Errno 22
    retry possible -- it has to read the output to recognise one -- so a streamed stage cannot be
    retried, and that is asserted rather than assumed.
    """
    printable = " ".join(x if " " not in x else f'"{x}"' for x in cmd[1:])
    if dry:
        print(f"      would run: python {printable}")
        return 0
    if stream:
        assert attempts == 1, "a streamed stage cannot be retried: capture is what finds Errno 22"
        r = subprocess.run([sys.executable] + cmd[1:], cwd=ROOT)
        if r.returncode:
            # its output is already on the terminal, so there is no tail worth repeating
            print(f"      FAILED: python {printable}", flush=True)
        return r.returncode

    for attempt in range(1, attempts + 1):
        r = subprocess.run([sys.executable] + cmd[1:], cwd=ROOT, capture_output=True,
                           text=True, encoding="utf-8", errors="replace")
        if not r.returncode:
            if attempt > 1:
                print(f"      recovered on attempt {attempt}: python {printable}", flush=True)
            return 0
        out = (r.stderr or "") + (r.stdout or "")
        if "Errno 22" in out and attempt < attempts:
            print(f"      Errno 22 (transient write lock), retrying {attempt + 1}/{attempts}: "
                  f"python {printable}", flush=True)
            time.sleep(2 * attempt)
            continue
        print(f"      FAILED: python {printable}", flush=True)
        print(out[-2000:])
        return r.returncode


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tapp", action="append", default=[],
                    help="limit the per-technique stages to these (repeatable). module, simplify "
                         "and mirrors still run over everything because they are shared; resolve is "
                         "SCOPED to these techniques plus every shared schema")
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
            # Scope resolve to the techniques being rebuilt. Without this a --tapp run still
            # resolved all 206 schemas -- 190 of them techniques it was not touching -- and that
            # stage dominates the wall clock. Shared schemas (BaseSchema/, registry/) are always
            # resolved by resolve_schema itself: the module and registry stages rebuild them every
            # run, so scoping those out would leave a stale resolvedSchema poisoning every
            # technique that composes it.
            cmd = ["", os.path.join(TOOLS, "resolve_schema.py"), "--all"]
            if a.tapp:
                for t in a.tapp:
                    cmd += ["--only", b.TECH_DIR.get(t, t)]
            # attempts=1: no Errno 22 retry here, unlike every other stage. run() re-runs the
            # whole command, and this one command is the better part of an hour, so a lock in its
            # last minute costs another full pass from the start -- three of which do not fit in
            # the time a run gets. On 2026-10-02 that killed a run at its two-hour limit on
            # attempt 2, with profile-2, examples and mirrors never reached.
            #
            # It is also the stage that needs the retry least: resolve_schema writes only files
            # whose bytes changed and refuses to write one whose refs did not resolve, so the next
            # ordinary run repairs whatever a lock cost. Re-run the stage, do not retry inside it.
            # stream=True: an hour-long stage must show progress, or a stalled run
            # cannot be told from a slow one. See run() for why this needs attempts=1.
            fail += [(stage, "")] if run(cmd, a.dry_run, attempts=1,
                                         stream=True) else []
        elif stage == "mirrors":
            fail += [(stage, "")] if run(["", os.path.join(TOOLS, "regenerate_schema_json.py")],
                                         a.dry_run) else []
        else:
            script = {"tapp": "build_tapp.py", "pathdriven": "build_pathdriven.py",
                      "profile-1": "build_profile.py", "profile-2": "build_profile.py",
                      "examples": "build_tapp_examples.py"}[stage]
            todo = tapps
            if stage in ("profile-1", "profile-2"):
                # Only the released TAPPs have a profile; the drafts carry tapp/ and detail/ only.
                # Unfiltered, build_profile raises KeyError: PROFILES[tapp] for every draft — 43
                # tracebacks on a full run that all mean "this technique has no profile", which is
                # the correct state. The cost is not the noise: a REAL profile failure on one of
                # the sixteen prints the same FAILED line in the same wall of text, so the signal
                # the FAILURES list is supposed to carry is buried in expected output.
                #
                # The test is PROFILES membership, not whether profile/ exists on disk:
                # build_profile CREATES that directory (os.makedirs, build_profile.py:465), so a
                # directory test would skip a newly configured profile on the one run that was
                # meant to create it, and every run after.
                todo = [t for t in tapps if t in bprof.PROFILES]
                if len(todo) != len(tapps):
                    print(f"      {len(tapps) - len(todo)} technique(s) skipped — no profile "
                          f"configured in build_profile.PROFILES", flush=True)
            for t in todo:
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
