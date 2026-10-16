#!/usr/bin/env python3
"""Comprehensive audit tool for OGC Building Block repositories.

Scans a _sources/ directory and checks each building block for:
  1. File completeness (schema.yaml, bblock.json, examples, etc.)
  2. schema.yaml vs *Schema.json consistency
  3. resolvedSchema.json freshness (re-resolve and compare)
  4. Example validation against resolved schemas
  5. SHACL rules completeness relative to schema properties
  6. Example coverage of schema properties

Designed to work with any building block repository that follows the
OGC Building Blocks directory pattern.

Usage:
    python audit_building_blocks.py [_sources_dir] [options]

    # Audit current repo
    python audit_building_blocks.py

    # Audit specific repo
    python audit_building_blocks.py /path/to/repo/_sources

    # Filter to specific building blocks
    python audit_building_blocks.py --filter cdifCore

    # Output JSON report
    python audit_building_blocks.py --json -o report.json

    # Record the current failing set as the accepted baseline
    python audit_building_blocks.py --write

Exit code: 0 when the audited blocks match docs/audit_baseline.json, 1 when a
block gained an issue the baseline does not record (or, on a full run, resolved
one it does), 2 on a usage or environment error.

Until 2026-10-16 this tool printed "Summary: 246 passed, 5 failed" and exited 0,
and no workflow ran it -- so a failure report nothing was able to act on was the
only output it had. The baseline shape is borrowed from
tools/constraint_census.py for the reason that tool uses it: the repository has 5
failures it cannot clear today (the legacy profile-ada blocks for QRIS, RAMAN,
VNMIR, XANES and XRD carry no example, and no generator owns them, so the
examples must be authored or the blocks retired -- and retirement is blocked on
ADA-side record migration, not on schema work). Making the audit fatal outright
would build a check that can never pass, which CLAUDE.md warns about directly.
Recording those 5 instead makes them accepted debt whose every movement is
visible, and makes the 6th failure fatal from the moment it appears.

The baseline stores each failing block's issue strings VERBATIM and compares them
exactly, so a block that keeps failing for a DIFFERENT reason is reported rather
than absorbed -- the same reasoning behind the mandatory "expect" field in
docs/counterexamples.json. A legitimately reworded message is therefore a diff to
review, not a silent pass: re-run with --write and commit the manifest.
"""

import argparse
import json
import sys
import os
import copy
from pathlib import Path
from collections import defaultdict

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml required. Install with: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

try:
    from jsonschema import Draft202012Validator
except ImportError:
    Draft202012Validator = None

# ---------------------------------------------------------------------------
# Import resolvers: prefer schema_resolver.py SchemaResolver (correct transitive $defs),
# fall back to tools/resolve_schema.py (handles circular refs)
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent

# Tools resolver (the structured-form resolver is now the canonical artifact)
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))
try:
    import importlib.util as _ilu
    _ts = _ilu.spec_from_file_location("tools_resolve", SCRIPT_DIR / "resolve_schema.py")
    _tm = _ilu.module_from_spec(_ts)
    _ts.loader.exec_module(_tm)
    resolve_structured = _tm.resolve_structured
except Exception:
    resolve_structured = None


def _resolve_for_audit(schema_path: Path) -> dict:
    """Resolve a schema (structured form) for audit freshness checks."""
    if resolve_structured is not None:
        resolved = resolve_structured(schema_path.resolve())
        resolved.pop("$schema", None)
        return resolved
    return None


# ---------------------------------------------------------------------------
# Building block discovery
# ---------------------------------------------------------------------------

BASELINE = REPO_ROOT / "docs" / "audit_baseline.json"

# The six checks, in the order audit_building_block runs them. Recorded in the
# baseline so a run with a narrower --checks cannot claim a baselined issue is
# resolved when it simply never looked for it.
CHECK_NAMES = ["files", "schema-json", "resolved", "examples", "shacl", "coverage"]

REQUIRED_FILES = ["schema.yaml", "bblock.json"]
EXPECTED_FILES = ["description.md", "context.jsonld", "rules.shacl"]
GENERATED_FILES = ["resolvedSchema.json"]  # checked for freshness

# Directories to skip
SKIP_DIRS = {"tests", "assets", "build", ".git", "node_modules", "__pycache__"}


def discover_building_blocks(sources_dir):
    """Find all building block directories under sources_dir.

    A building block directory contains at least schema.yaml.
    Returns list of (category, name, path) tuples sorted by path.
    """
    bbs = []
    for schema_path in sorted(sources_dir.rglob("schema.yaml")):
        bb_dir = schema_path.parent
        # Skip nested dirs (tests/, assets/, etc.)
        if any(part in SKIP_DIRS for part in bb_dir.parts):
            continue
        # Derive category and name from path relative to sources_dir
        rel = bb_dir.relative_to(sources_dir)
        parts = rel.parts
        if len(parts) >= 2:
            category = parts[0]
            name = parts[-1]
        elif len(parts) == 1:
            category = ""
            name = parts[0]
        else:
            continue
        bbs.append((category, name, bb_dir))
    return bbs


# ---------------------------------------------------------------------------
# Check 1: File completeness
# ---------------------------------------------------------------------------

def check_files(bb_dir, name, is_type_library=False):
    """Check for required, expected, and generated files.

    isTypeLibrary BBs have no instantiable root class (they only host reusable
    $defs referenced by fragment $refs), so the standalone-example requirement
    does not apply — a missing example is downgraded to info for them."""
    issues = []
    info = []

    for f in REQUIRED_FILES:
        if not (bb_dir / f).exists():
            issues.append(f"MISSING required file: {f}")

    for f in EXPECTED_FILES:
        if not (bb_dir / f).exists():
            info.append(f"Missing optional file: {f}")

    # Check for examples
    examples = list(bb_dir.glob("example*.json"))
    if not examples:
        # Check examples.yaml for inline examples
        if (bb_dir / "examples.yaml").exists():
            info.append("Has examples.yaml but no standalone example*.json files")
        elif is_type_library:
            info.append("No example files (isTypeLibrary: $defs library has no instantiable root)")
        else:
            issues.append("No example files found (example*.json or examples.yaml)")
    else:
        info.append(f"Found {len(examples)} example file(s)")

    # Check for generated schema files
    for f in GENERATED_FILES:
        if not (bb_dir / f).exists():
            issues.append(f"MISSING generated file: {f}")

    # Check for *Schema.json
    schema_jsons = list(bb_dir.glob("*Schema.json"))
    if not schema_jsons:
        issues.append("MISSING *Schema.json (run regenerate_schema_json.py)")

    return issues, info


# ---------------------------------------------------------------------------
# Check 2: schema.yaml vs *Schema.json consistency
# ---------------------------------------------------------------------------

def load_yaml(path):
    """Load YAML file."""
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_json(path):
    """Load JSON file."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def normalize_ref(ref_str):
    """Normalize $ref for comparison.

    The *Schema.json files rewrite refs from 'dir/schema.yaml' to
    'dir/dirNameSchema.json'; the same translation applies to HTTP
    refs in cross-repo $refs (CDIF, schemaorg upstream BBs). For both
    relative and HTTP refs, when the basename matches the
    'schema.yaml' or '<dirname>Schema.json' convention, we normalize
    to the directory path so the two forms compare equal.

    Fragment-only refs (#/$defs/X) are compared as-is.
    """
    if not ref_str:
        return ref_str
    if ref_str.startswith("#"):
        return ref_str
    import posixpath
    # Split fragment if present (e.g. .../schema.yaml#/$defs/X)
    base, _, frag = ref_str.partition("#")
    dirname = posixpath.dirname(base)
    basename = posixpath.basename(base)
    last_dir = posixpath.basename(dirname)
    is_yaml_source = basename == "schema.yaml"
    is_json_derivative = basename == f"{last_dir}Schema.json"
    if is_yaml_source or is_json_derivative:
        # Both forms point to the same building block: collapse to dir + frag
        normalized = dirname
    else:
        normalized = base
    return normalized + (("#" + frag) if frag else "")


def compare_schemas(yaml_schema, json_schema, path=""):
    """Compare YAML source schema with generated JSON schema.

    Returns list of difference descriptions. Ignores $ref extension
    differences (.yaml vs .json).
    """
    diffs = []
    if type(yaml_schema) != type(json_schema):
        diffs.append(f"{path}: type mismatch: {type(yaml_schema).__name__} vs {type(json_schema).__name__}")
        return diffs

    if isinstance(yaml_schema, dict):
        yaml_keys = set(yaml_schema.keys())
        json_keys = set(json_schema.keys())

        for k in yaml_keys - json_keys:
            diffs.append(f"{path}.{k}: missing from JSON schema")
        for k in json_keys - yaml_keys:
            diffs.append(f"{path}.{k}: extra in JSON schema")

        for k in yaml_keys & json_keys:
            if k == "$ref":
                # $ref extension differences (.yaml vs .json) are expected
                if normalize_ref(yaml_schema[k]) != normalize_ref(json_schema[k]):
                    diffs.append(f"{path}.$ref: {yaml_schema[k]} vs {json_schema[k]}")
            elif k == "$schema":
                # $schema differences are OK
                pass
            else:
                diffs.extend(compare_schemas(yaml_schema[k], json_schema[k], f"{path}.{k}"))

    elif isinstance(yaml_schema, list):
        if len(yaml_schema) != len(json_schema):
            diffs.append(f"{path}: array length {len(yaml_schema)} vs {len(json_schema)}")
        else:
            for i, (a, b) in enumerate(zip(yaml_schema, json_schema)):
                diffs.extend(compare_schemas(a, b, f"{path}[{i}]"))

    else:
        if yaml_schema != json_schema:
            diffs.append(f"{path}: value {yaml_schema!r} vs {json_schema!r}")

    return diffs


def check_schema_json_consistency(bb_dir, name):
    """Compare schema.yaml with *Schema.json."""
    issues = []
    schema_yaml_path = bb_dir / "schema.yaml"
    if not schema_yaml_path.exists():
        return issues

    yaml_data = load_yaml(schema_yaml_path)

    # Find *Schema.json
    schema_jsons = list(bb_dir.glob("*Schema.json"))
    # Exclude resolved and structured
    schema_jsons = [p for p in schema_jsons
                    if "resolved" not in p.name.lower()
                    and "structured" not in p.name.lower()]
    if not schema_jsons:
        return issues

    json_data = load_json(schema_jsons[0])
    diffs = compare_schemas(yaml_data, json_data)
    for d in diffs[:5]:  # limit to first 5
        issues.append(f"schema.yaml vs {schema_jsons[0].name}: {d}")
    if len(diffs) > 5:
        issues.append(f"  ... and {len(diffs) - 5} more differences")

    return issues


# ---------------------------------------------------------------------------
# Check 3: resolvedSchema.json freshness
# ---------------------------------------------------------------------------

def check_resolved_schema(bb_dir, name):
    """Re-resolve schema.yaml and compare with existing resolvedSchema.json."""
    issues = []
    resolved_path = bb_dir / "resolvedSchema.json"
    schema_path = bb_dir / "schema.yaml"

    if not schema_path.exists() or not resolved_path.exists():
        return issues

    if resolve_structured is None:
        issues.append("Cannot check resolvedSchema freshness (resolve_schema not importable)")
        return issues

    try:
        fresh = _resolve_for_audit(schema_path)
        if fresh is None:
            issues.append("Cannot check resolvedSchema freshness (resolution failed)")
            return issues
        existing = load_json(resolved_path)

        # Compare top-level property keys as a quick freshness check
        fresh_props = set(fresh.get("properties", {}).keys())
        existing_props = set(existing.get("properties", {}).keys())

        missing = fresh_props - existing_props
        extra = existing_props - fresh_props

        if missing:
            issues.append(f"resolvedSchema.json STALE — missing properties: {', '.join(sorted(missing))}")
        if extra:
            issues.append(f"resolvedSchema.json STALE — extra properties: {', '.join(sorted(extra))}")

    except Exception as e:
        issues.append(f"resolvedSchema.json check error: {e}")

    return issues


# ---------------------------------------------------------------------------
# Check 4: Example validation
# ---------------------------------------------------------------------------

def check_example_validation(bb_dir, name):
    """Validate all example*.json against resolved schema."""
    issues = []
    info = []

    if Draft202012Validator is None:
        issues.append("Cannot validate examples (jsonschema not installed)")
        return issues, info

    schema_path = bb_dir / "schema.yaml"
    if not schema_path.exists():
        return issues, info

    examples = sorted(bb_dir.glob("example*.json"))
    if not examples:
        return issues, info

    # Prefer existing resolvedSchema.json (CI-generated, handles allOf correctly)
    # Fall back to re-resolving from source
    resolved_path = bb_dir / "resolvedSchema.json"
    resolved = None
    if resolved_path.exists():
        try:
            resolved = load_json(resolved_path)
        except Exception:
            pass

    if resolved is None:
        try:
            resolved = _resolve_for_audit(schema_path)
        except Exception as e:
            issues.append(f"Schema resolution failed: {e}")
            return issues, info
        if resolved is None:
            issues.append("Cannot validate examples (no resolvedSchema.json and resolve_schema not importable)")
            return issues, info

    # Try validating with the resolved schema; if it has dangling $ref links
    # (from inline optimization), re-resolve with the audit resolver
    try:
        validator = Draft202012Validator(resolved)
        # Quick test to surface PointerToNowhere early
        validator.check_schema(resolved)
    except Exception:
        audit_resolved = _resolve_for_audit(schema_path)
        if audit_resolved is not None:
            resolved = audit_resolved
        validator = Draft202012Validator(resolved)

    for ex_path in examples:
        try:
            example = load_json(ex_path)
        except Exception as e:
            issues.append(f"{ex_path.name}: JSON parse error: {e}")
            continue

        try:
            errors = list(validator.iter_errors(example))
        except RecursionError:
            issues.append(f"{ex_path.name}: RecursionError during validation")
            continue
        except Exception as exc:
            # Dangling $ref in pre-built resolvedSchema.json — retry with
            # live resolution from the audit resolver
            try:
                audit_resolved = _resolve_for_audit(schema_path)
                if audit_resolved is not None:
                    retry_validator = Draft202012Validator(audit_resolved)
                    errors = list(retry_validator.iter_errors(example))
                else:
                    issues.append(f"{ex_path.name}: {type(exc).__name__} during validation")
                    continue
            except Exception as exc2:
                issues.append(f"{ex_path.name}: {type(exc2).__name__} during validation (retry)")
                continue
        if errors:
            for err in errors[:3]:
                path_str = "/".join(str(p) for p in err.absolute_path) if err.absolute_path else "(root)"
                issues.append(f"{ex_path.name}: {path_str}: {err.message[:120]}")
            if len(errors) > 3:
                issues.append(f"{ex_path.name}: ... and {len(errors) - 3} more errors")
        else:
            info.append(f"{ex_path.name}: PASS")

    return issues, info


# ---------------------------------------------------------------------------
# Check 5: SHACL completeness relative to schema
# ---------------------------------------------------------------------------

def extract_schema_properties(schema, prefix=""):
    """Extract property paths from a JSON schema."""
    props = set()
    if not isinstance(schema, dict):
        return props

    for key, val in schema.get("properties", {}).items():
        if key.startswith("@"):
            continue
        full = f"{prefix}{key}" if not prefix else f"{prefix}.{key}"
        props.add(full)
        if isinstance(val, dict):
            props |= extract_schema_properties(val, full)

    # Walk allOf, anyOf, oneOf
    for keyword in ("allOf", "anyOf", "oneOf"):
        for item in schema.get(keyword, []):
            props |= extract_schema_properties(item, prefix)

    # Walk items
    items = schema.get("items", {})
    if isinstance(items, dict):
        props |= extract_schema_properties(items, prefix)

    return props


def check_shacl_completeness(bb_dir, name, is_type_library=False):
    """Check if SHACL rules exist and cover key schema properties."""
    issues = []
    info = []

    shacl_path = bb_dir / "rules.shacl"
    schema_path = bb_dir / "schema.yaml"

    if not schema_path.exists():
        return issues, info

    if not shacl_path.exists():
        # Not all BBs need SHACL
        info.append("No rules.shacl file")
        return issues, info

    try:
        shacl_text = shacl_path.read_text(encoding="utf-8")
    except Exception as e:
        issues.append(f"Cannot read rules.shacl: {e}")
        return issues, info

    # Extract schema properties
    try:
        schema = load_yaml(schema_path)
        schema_props = extract_schema_properties(schema)
    except Exception:
        schema_props = set()

    # Check for sh:NodeShape definitions
    if "sh:NodeShape" not in shacl_text:
        if is_type_library:
            # Type libraries have no instantiable root class (e.g. a literal
            # array, or an anyOf umbrella that delegates to other BBs), so a
            # NodeShape is not applicable; rules.shacl is an intentional placeholder.
            info.append("rules.shacl has no sh:NodeShape (isTypeLibrary: SHACL not applicable)")
        elif "SHACL-NOT-APPLICABLE:" in shacl_text:
            # An instantiable BB can still have nothing to assert. geochemProduct is the case:
            # its schema.yaml carries NO root `required` at all — it is a permissive base that
            # profiles narrow (adaProduct adds the real shapes) — so any NodeShape written here
            # would invent constraints the JSON Schema does not make, which is worse than the
            # empty file. The declaration has to be MACHINE-READABLE and carry a reason, so a
            # genuinely missing shape still fails; a prose comment alone would let every BB
            # silently opt out.
            why = next((ln.split("SHACL-NOT-APPLICABLE:", 1)[1].strip()
                        for ln in shacl_text.splitlines() if "SHACL-NOT-APPLICABLE:" in ln), "")
            info.append(f"rules.shacl has no sh:NodeShape (declared not applicable: {why})")
        else:
            issues.append("rules.shacl has no sh:NodeShape definitions")
    else:
        # Count shapes
        shape_count = shacl_text.count("sh:NodeShape")
        prop_shape_count = shacl_text.count("sh:PropertyShape")
        info.append(f"SHACL: {shape_count} NodeShape(s), {prop_shape_count} PropertyShape(s)")

    # Check which schema properties are referenced in SHACL
    # Simple heuristic: look for property path URIs in the SHACL text
    covered = set()
    uncovered = set()
    for prop in schema_props:
        # Normalize: schema:name → schema:name
        local_name = prop.split(".")[-1]  # innermost property
        if ":" in local_name:
            prefix, local = local_name.split(":", 1)
            # Check if the property appears in SHACL
            if local in shacl_text or local_name in shacl_text:
                covered.add(prop)
            else:
                uncovered.add(prop)

    if covered:
        info.append(f"SHACL covers {len(covered)}/{len(covered) + len(uncovered)} schema properties")

    return issues, info


# ---------------------------------------------------------------------------
# Check 6: Example property coverage
# ---------------------------------------------------------------------------

def extract_example_properties(data, prefix=""):
    """Extract property paths used in an example JSON."""
    props = set()
    if isinstance(data, dict):
        for key, val in data.items():
            if key.startswith("@"):
                continue
            full = f"{prefix}{key}" if not prefix else f"{prefix}.{key}"
            props.add(full)
            if isinstance(val, dict):
                props |= extract_example_properties(val, full)
            elif isinstance(val, list):
                for item in val:
                    props |= extract_example_properties(item, full)
    return props


def check_example_coverage(bb_dir, name):
    """Check whether examples exercise all schema properties."""
    issues = []
    info = []

    schema_path = bb_dir / "schema.yaml"
    if not schema_path.exists():
        return issues, info

    try:
        schema = load_yaml(schema_path)
        schema_props = extract_schema_properties(schema)
    except Exception:
        return issues, info

    # Collect all properties used across all examples
    all_example_props = set()
    examples = sorted(bb_dir.glob("example*.json"))
    for ex_path in examples:
        try:
            data = load_json(ex_path)
            all_example_props |= extract_example_properties(data)
        except Exception:
            continue

    if not examples:
        return issues, info

    # Find schema properties not exercised by any example
    # Only check top-level domain properties (schema:X, prov:X, etc.)
    domain_props = {p for p in schema_props if ":" in p.split(".")[-1]}
    exercised = set()
    for sp in domain_props:
        leaf = sp.split(".")[-1]
        if any(leaf in ep for ep in all_example_props):
            exercised.add(sp)

    missing = domain_props - exercised
    if missing and len(missing) <= 10:
        for m in sorted(missing):
            info.append(f"Property not exercised in examples: {m}")
    elif missing:
        info.append(f"{len(missing)} schema properties not exercised in examples")

    if exercised:
        info.append(f"Examples cover {len(exercised)}/{len(domain_props)} domain properties")

    return issues, info


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------

class AuditResult:
    def __init__(self, category, name, bb_dir):
        self.category = category
        self.name = name
        self.bb_dir = str(bb_dir)
        # Path relative to _sources/, set by main(). This -- not `name` -- is the
        # baseline key, because `name` is not unique: 41 blocks are called
        # "profile-ada", and both adaProfile/QRIS/profile-ada and
        # geochemProfile/QRIS/profile-ada are among them. Keying on the name would
        # let one block's accepted debt excuse another block's failure.
        self.key = str(bb_dir)
        self.issues = []
        self.info = []
        self.status = "PASS"

    def add_issues(self, issues):
        self.issues.extend(issues)
        if issues:
            self.status = "FAIL"

    def add_info(self, info):
        self.info.extend(info)

    def to_dict(self):
        return {
            "category": self.category,
            "name": self.name,
            "key": self.key,
            "status": self.status,
            "issues": self.issues,
            "info": self.info,
        }


# ---------------------------------------------------------------------------
# Accepted-failure baseline
# ---------------------------------------------------------------------------

def load_baseline():
    try:
        with open(BASELINE, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return None


def save_baseline(results, checks):
    """Record every currently failing block. Passing blocks are NOT recorded.

    A manifest of all 251 blocks would churn on any change to a block's info
    messages and would say nothing about what is accepted; absence from this
    file therefore means "must have no issues at all"."""
    blocks = {r.key: list(r.issues)
              for r in sorted(results, key=lambda r: r.key) if r.issues}
    payload = {
        "_comment": "Written by tools/audit_building_blocks.py --write. Never hand-edit. "
                    "Lists the building blocks whose audit failures are ACCEPTED: the audit "
                    "exits non-zero on any issue not recorded here. A block absent from "
                    "'blocks' must have no issues. See the module docstring and "
                    "docs/SILENT_SUCCESS.md section 9.",
        "_blocks": len(blocks),
        "_issues": sum(len(v) for v in blocks.values()),
        "_checks": sorted(checks),
        "blocks": blocks,
    }
    BASELINE.parent.mkdir(parents=True, exist_ok=True)
    with open(BASELINE, "w", encoding="utf-8", newline="\n") as fh:
        json.dump(payload, fh, indent=2, sort_keys=True)
        fh.write("\n")
    return payload


def compare_baseline(results, before):
    """(gained, lost) as lists of (block_key, issue).

    Only blocks that were actually audited are compared, so --filter and
    --checks cannot make an unexamined block look fixed."""
    now = {r.key: list(r.issues) for r in results if r.issues}
    audited = {r.key for r in results}
    gained, lost = [], []
    for key in sorted(set(now) | (set(before) & audited)):
        a = now.get(key, [])
        b = before.get(key, [])
        gained.extend((key, i) for i in a if i not in b)
        lost.extend((key, i) for i in b if i not in a)
    return gained, lost


def print_report(results, verbose=False, baseline=None):
    """Print human-readable audit report."""
    baseline = baseline or {}
    total = len(results)
    passed = sum(1 for r in results if r.status == "PASS")
    failed = total - passed
    accepted = sum(1 for r in results
                   if r.issues and all(i in baseline.get(r.key, []) for i in r.issues))

    print(f"\n{'=' * 70}")
    print(f"Building Block Audit Report")
    print(f"{'=' * 70}")

    # Group by category
    by_category = defaultdict(list)
    for r in results:
        by_category[r.category].append(r)

    for category in sorted(by_category.keys()):
        cat_results = by_category[category]
        cat_pass = sum(1 for r in cat_results if r.status == "PASS")
        print(f"\n--- {category or '(root)'} ({cat_pass}/{len(cat_results)} pass) ---")

        for r in cat_results:
            known = baseline.get(r.key, [])
            if r.status == "PASS":
                marker = "PASS"
            elif all(i in known for i in r.issues):
                marker = "KNOWN"
            else:
                marker = "FAIL"
            label = r.name if r.key == r.name else f"{r.name}  ({r.key})"
            print(f"  [{marker}] {label}")

            if r.issues:
                for issue in r.issues:
                    tag = "known" if issue in known else "ERROR"
                    print(f"    {tag}: {issue}")

            if verbose and r.info:
                for info in r.info:
                    print(f"    info: {info}")

    print(f"\n{'=' * 70}")
    print(f"Summary: {passed} passed, {failed} failed (of {total} building blocks)")
    if failed:
        print(f"         {accepted} of the {failed} are accepted in "
              f"{os.path.relpath(BASELINE, REPO_ROOT)}; {failed - accepted} are not.")
    print(f"{'=' * 70}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def audit_building_block(category, name, bb_dir, checks=None):
    """Run all audit checks on a single building block."""
    result = AuditResult(category, name, bb_dir)

    # Read opt-out flags from bblock.json. isTypeLibrary marks BBs with no
    # instantiable root class (reusable type defs, anyOf umbrellas); the SHACL
    # NodeShape requirement does not apply to them.
    is_type_library = False
    bblock_path = bb_dir / "bblock.json"
    if bblock_path.exists():
        try:
            with open(bblock_path, encoding="utf-8") as _f:
                is_type_library = bool(json.load(_f).get("isTypeLibrary", False))
        except Exception:
            pass

    # Check 1: File completeness
    if not checks or "files" in checks:
        issues, info = check_files(bb_dir, name, is_type_library=is_type_library)
        result.add_issues(issues)
        result.add_info(info)

    # Check 2: schema.yaml vs *Schema.json
    if not checks or "schema-json" in checks:
        issues = check_schema_json_consistency(bb_dir, name)
        result.add_issues(issues)

    # Check 3: resolvedSchema freshness
    if not checks or "resolved" in checks:
        issues = check_resolved_schema(bb_dir, name)
        result.add_issues(issues)

    # Check 4: Example validation
    if not checks or "examples" in checks:
        issues, info = check_example_validation(bb_dir, name)
        result.add_issues(issues)
        result.add_info(info)

    # Check 5: SHACL completeness
    if not checks or "shacl" in checks:
        issues, info = check_shacl_completeness(bb_dir, name, is_type_library=is_type_library)
        result.add_issues(issues)
        result.add_info(info)

    # Check 6: Example coverage
    if not checks or "coverage" in checks:
        issues, info = check_example_coverage(bb_dir, name)
        result.add_issues(issues)
        result.add_info(info)

    return result


def check_vocab_identifier_collisions(sources_dir):
    """Every vocabulary file must own its @id.

    registry/vocab is a plain catalog: nothing $refs a vocabulary FILE, consumers
    resolve the @id. So two files carrying one @id are not a duplicate -- they are
    a fork, and which one a consumer sees is decided by whatever order it happened
    to read the directory in.

    That is not hypothetical. The 2026-09 generator changed the filename convention
    to <tapp>_<name>.json and did not remove the bare <name>.json it superseded, so
    seven epmaTAPP vocabularies existed twice with DIFFERENT terms (Raster vs
    Rastered; a matrixCorrectionMethod list missing ZAF, CITZAF and Bence-Albee).
    The ADA forms app ingests this directory sorted by filename and upserts on @id,
    so the alphabetically last file won: four of the seven resolved to the stale
    fork and the registry served picklists the current TAPP does not allow.

    Returns (ok, [message, ...]).
    """
    vocab_dir = Path(sources_dir) / "registry" / "vocab"
    if not vocab_dir.is_dir():
        return True, []
    by_id = {}
    for path in sorted(vocab_dir.glob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            return False, [f"{path.name}: unreadable ({exc})"]
        ident = data.get("@id") or data.get("$id")
        if not ident:
            continue
        by_id.setdefault(ident, []).append(path.name)
    problems = []
    for ident, files in sorted(by_id.items()):
        if len(files) > 1:
            problems.append(f"{ident} is claimed by {len(files)} files: {', '.join(files)}")
    return (not problems), problems


def main():
    parser = argparse.ArgumentParser(
        description="Comprehensive audit of OGC Building Block repositories"
    )
    parser.add_argument(
        "sources_dir",
        nargs="?",
        default=None,
        help="Path to _sources/ directory (default: auto-detect)"
    )
    parser.add_argument(
        "--filter", "-f",
        type=str,
        default=None,
        help="Only audit BBs whose name contains this string"
    )
    parser.add_argument(
        "--checks", "-c",
        type=str,
        default=None,
        help="Comma-separated list of checks to run: files,schema-json,resolved,examples,shacl,coverage"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show info messages in addition to errors"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        dest="json_output",
        help="Output report as JSON"
    )
    parser.add_argument(
        "-o", "--output",
        type=str,
        default=None,
        help="Output file (default: stdout)"
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="record the currently failing blocks as the accepted baseline "
             "(docs/audit_baseline.json)"
    )
    args = parser.parse_args()

    # Find sources directory
    if args.sources_dir:
        sources_dir = Path(args.sources_dir)
    else:
        # Auto-detect: look for _sources/ relative to CWD or script
        candidates = [
            Path.cwd() / "_sources",
            SCRIPT_DIR.parent / "_sources",
        ]
        sources_dir = None
        for c in candidates:
            if c.is_dir():
                sources_dir = c
                break
        if sources_dir is None:
            print("ERROR: Cannot find _sources/ directory. Provide path as argument.",
                  file=sys.stderr)
            sys.exit(1)

    print(f"Auditing: {sources_dir}")

    # Parse checks. `checks` stays None for "run everything" (audit_building_block
    # reads it that way); run_checks is the resolved set, for the baseline.
    checks = None
    if args.checks:
        checks = set(args.checks.split(","))
        unknown = sorted(checks - set(CHECK_NAMES))
        if unknown:
            print(f"ERROR: unknown check(s): {', '.join(unknown)}. "
                  f"Known: {', '.join(CHECK_NAMES)}", file=sys.stderr)
            return 2
    run_checks = set(checks) if checks else set(CHECK_NAMES)

    # Discover building blocks
    bbs = discover_building_blocks(sources_dir)
    if args.filter:
        bbs = [(c, n, p) for c, n, p in bbs if args.filter.lower() in n.lower()]

    print(f"Found {len(bbs)} building blocks\n")

    # Run audit
    results = []
    for category, name, bb_dir in bbs:
        result = audit_building_block(category, name, bb_dir, checks)
        result.key = bb_dir.relative_to(sources_dir).as_posix()
        results.append(result)
        # Progress indicator
        marker = "." if result.status == "PASS" else "F"
        print(marker, end="", flush=True)
    print()

    # Catalog-wide, not per building block: a collision is a relationship BETWEEN
    # files, so no single-block check can see it.
    vocab_ok, vocab_problems = check_vocab_identifier_collisions(sources_dir)
    if not vocab_ok:
        print(chr(10) + "FAIL  registry/vocab: %d identifier collision(s)" % len(vocab_problems))
        for msg in vocab_problems:
            print("        " + msg)
        print("      Nothing $refs a vocabulary file; consumers resolve the @id, so which")
        print("      of these a consumer sees depends on its directory read order.")

    if args.write:
        payload = save_baseline(results, run_checks)
        print(f"\nwrote {os.path.relpath(BASELINE, REPO_ROOT)}: "
              f"{payload['_blocks']} block(s) with {payload['_issues']} accepted issue(s)")
        for key, issues in sorted(payload["blocks"].items()):
            print(f"  {key}")
            for issue in issues:
                print(f"      {issue}")
        # A vocabulary @id collision is never acceptable debt, so --write must not
        # look like a way to accept one: see the comment on the verdict below.
        return 0 if vocab_ok else 1

    baseline = load_baseline()
    if baseline is None:
        print(f"no baseline at {os.path.relpath(BASELINE, REPO_ROOT)} -- "
              f"run with --write to create it", file=sys.stderr)
        return 2
    before = baseline.get("blocks", {})
    gained, lost = compare_baseline(results, before)

    # A run that examines a subset cannot tell "fixed" from "not looked for", so
    # only a run that covered at least everything the manifest was written with --
    # and that filtered nothing out -- may call a baselined issue resolved. A
    # NEW issue is fatal from any run, because finding one is positive evidence
    # either way.
    baseline_checks = set(baseline.get("_checks") or CHECK_NAMES)
    narrower = sorted(baseline_checks - run_checks)
    authoritative = not args.filter and not narrower

    # Output
    if args.json_output:
        report = {
            "sources_dir": str(sources_dir),
            "total": len(results),
            "passed": sum(1 for r in results if r.status == "PASS"),
            "failed": sum(1 for r in results if r.status == "FAIL"),
            "baseline": os.path.relpath(BASELINE, REPO_ROOT),
            "new_issues": [{"block": k, "issue": i} for k, i in gained],
            "resolved_issues": [{"block": k, "issue": i} for k, i in lost],
            "vocab_collisions": vocab_problems,
            "results": [r.to_dict() for r in results],
        }
        output = json.dumps(report, indent=2)
        if args.output:
            with open(args.output, "w", encoding="utf-8") as f:
                f.write(output)
            print(f"\nJSON report written to {args.output}")
        else:
            print(output)
    else:
        print_report(results, verbose=args.verbose, baseline=before)

    if narrower:
        print(f"\nNote: this run skipped {', '.join(narrower)}, which "
              f"{os.path.relpath(BASELINE, REPO_ROOT)} was written with, so it cannot")
        print("      tell a resolved issue from one it did not look for. New issues are "
              "still fatal.")
    if gained:
        print(f"\nNEW ISSUES ({len(gained)}), not recorded in "
              f"{os.path.relpath(BASELINE, REPO_ROOT)}:")
        for key, issue in gained:
            print(f"  + {key}")
            print(f"      {issue}")
    if lost:
        verb = "RESOLVED" if authoritative else "not reported by this narrower run"
        print(f"\n{len(lost)} baselined issue(s) {verb}:")
        for key, issue in lost:
            print(f"  - {key}")
            print(f"      {issue}")

    # The verdict. Three separate reasons to fail, deliberately not collapsed:
    #
    #   gained    a block has an issue nobody accepted. This is the check.
    #   lost      from an authoritative run only: debt that has been cleared must
    #             be removed from the manifest in the same change, or the baseline
    #             keeps permitting a failure that is no longer there -- and the
    #             next regression at that block is absorbed by the stale entry.
    #   vocab     a vocabulary @id claimed by two files is a fork whose winner is
    #             read order. It is a catalog-level defect, not a per-block one,
    #             and it is never accepted debt, so it is not baselineable.
    status = 0
    if gained:
        status = 1
    if lost and authoritative:
        status = 1
    if not vocab_ok:
        status = 1

    if status == 0:
        n = sum(1 for r in results if r.issues)
        print(f"\naudit matches {os.path.relpath(BASELINE, REPO_ROOT)}"
              + (f" ({n} accepted failure(s))" if n else ""))
        return status

    if not vocab_ok:
        print(f"\nA vocabulary @id claimed by two files is not baselineable: --write will")
        print("not accept it. Remove the file the convention superseded.")
    if gained or (lost and authoritative):
        print("\nThe audit no longer matches "
              f"{os.path.relpath(BASELINE, REPO_ROOT)}.")
        print("Fix the block, or -- if every line above is intended -- re-run with --write")
        print("and commit the manifest in the same change, so the diff records what moved.")
    return status


if __name__ == "__main__":
    sys.exit(main())
