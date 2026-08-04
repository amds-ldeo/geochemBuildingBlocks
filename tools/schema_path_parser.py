"""Phase 1 of the nested-interpreter work: PARSER.

Turns a *canonical* TAPP schema path (as produced by tools/normalize_schema_paths.py into
docs/<workbook>.schemapaths.json) into a structured tree that the schema/example emitters
(Phase 2/3) walk. Input must already be canonical per docs/SCHEMA_PATH_GRAMMAR.md; this module
parses and validates that grammar, it does NOT normalize (that is the normalizer's job).

Grammar (canonical):
    path      := root ( "." segment )*
    root      := "$MethodDefinition" | "$Dataset"
    segment   := curie [ "[]" ] [ "[" curie "='" value "']" ]
    curie     := ns ":" localname

A segment's localname case carries meaning (schema.org convention):
    lowerCamel  -> a PROPERTY (navigate into it)      e.g. schema:name, schema:measurementTechnique
    UpperCamel  -> a TYPE assertion (@type of node)   e.g. schema:DefinedTerm, schema:Person

    python tools/schema_path_parser.py            # self-test over every schemapaths.json
    python tools/schema_path_parser.py '<path>'   # parse one path, print the tree
"""
import glob
import json
import os
import re
import sys
from dataclasses import dataclass, field
from typing import List, Optional, Tuple

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_CURIE = r"[A-Za-z][A-Za-z0-9]*:[A-Za-z][A-Za-z0-9]*"


class SchemaPathError(ValueError):
    """Raised when a path does not conform to the canonical grammar."""


@dataclass
class Segment:
    prop: str                                   # the curie, e.g. "schema:additionalProperty"
    is_array: bool = False                       # True if "[]" or a selector is present
    selector: Optional[Tuple[str, str]] = None   # (key_curie, value) for [key='value'], else None

    @property
    def localname(self) -> str:
        return self.prop.split(":", 1)[1]

    @property
    def is_type(self) -> bool:
        # schema.org convention: UpperCamel localname = a @type assertion, not a property nav
        return self.localname[:1].isupper()

    def to_dict(self):
        d = {"prop": self.prop}
        if self.is_type:
            d["type"] = True
        if self.is_array:
            d["array"] = True
        if self.selector:
            d["selector"] = {"key": self.selector[0], "value": self.selector[1]}
        return d


@dataclass
class ParsedPath:
    root: str                      # "MethodDefinition" | "Dataset"
    segments: List[Segment] = field(default_factory=list)

    @property
    def artifact(self) -> str:
        """Which artifact the row targets: the reusable protocol vs the analysis document."""
        return "tapp" if self.root == "MethodDefinition" else "dataset"

    @property
    def leaf(self) -> Segment:
        return self.segments[-1]

    @property
    def terminal_field(self) -> Optional[Segment]:
        """The scalar property the row's value sets (last segment when it is a plain field:
        not an array, not a selector, not a @type). None when the value IS an array element."""
        s = self.leaf
        return s if (not s.is_array and s.selector is None and not s.is_type) else None

    @property
    def leaf_is_element(self) -> bool:
        """True when the path ends at an array (append or selected element) with no terminal
        field — i.e. the row's value is (or populates) that element itself."""
        s = self.leaf
        return s.is_array or s.selector is not None

    def to_dict(self):
        return {"root": self.root, "artifact": self.artifact,
                "segments": [s.to_dict() for s in self.segments]}


def _split_top(s: str, sep: str = ".") -> List[str]:
    """Split on `sep` at bracket/quote depth 0."""
    parts, buf, depth, inq = [], [], 0, False
    for ch in s:
        if ch == "'":
            inq = not inq; buf.append(ch)
        elif inq:
            buf.append(ch)
        elif ch == "[":
            depth += 1; buf.append(ch)
        elif ch == "]":
            depth -= 1; buf.append(ch)
        elif ch == sep and depth == 0:
            parts.append("".join(buf)); buf = []
        else:
            buf.append(ch)
    if depth != 0 or inq:
        raise SchemaPathError(f"unbalanced brackets/quotes: {s!r}")
    if buf:
        parts.append("".join(buf))
    return parts


def _bracket_groups(s: str) -> List[str]:
    """Return the inner contents of each top-level [...] group in `s` (the tail after the curie).
    Rejects any non-space text between/around groups."""
    groups, buf, depth = [], [], 0
    for ch in s:
        if ch == "[":
            if depth == 0:
                buf = []
            else:
                buf.append(ch)
            depth += 1
        elif ch == "]":
            depth -= 1
            if depth == 0:
                groups.append("".join(buf))
            elif depth < 0:
                raise SchemaPathError(f"unbalanced brackets: {s!r}")
            else:
                buf.append(ch)
        else:
            if depth > 0:
                buf.append(ch)
            elif ch.strip():
                raise SchemaPathError(f"unexpected text outside selector: {s!r}")
    if depth != 0:
        raise SchemaPathError(f"unbalanced brackets: {s!r}")
    return groups


_SELECTOR_RE = re.compile(r"^(@type|" + _CURIE + r")='(.*)'$")   # @type membership selector allowed


def _parse_segment(seg: str) -> Segment:
    i = seg.find("[")
    curie = seg if i == -1 else seg[:i]
    if not re.fullmatch(_CURIE, curie):
        raise SchemaPathError(f"bad curie {curie!r} in segment {seg!r}")
    is_array, selector = False, None
    for b in ([] if i == -1 else _bracket_groups(seg[i:])):
        if b == "":
            is_array = True
        else:
            m = _SELECTOR_RE.match(b)
            if not m:
                raise SchemaPathError(f"bad selector [{b}] in segment {seg!r}")
            if selector is not None:
                raise SchemaPathError(f"multiple selectors in segment {seg!r}")
            selector = (m.group(1), m.group(2))
            is_array = True
    return Segment(curie, is_array, selector)


_ROOT_RE = re.compile(r"^\$(MethodDefinition|Dataset)(?:\.|$)")


def parse(path: str) -> ParsedPath:
    """Parse a canonical schema path into a ParsedPath. Raises SchemaPathError on non-canonical input."""
    path = path.strip()
    m = _ROOT_RE.match(path)
    if not m:
        raise SchemaPathError(f"path must start with $MethodDefinition or $Dataset: {path!r}")
    root = m.group(1)
    rest = path[len(m.group(0)):] if m.group(0).endswith(".") else path[m.end():]
    segments = [_parse_segment(seg) for seg in _split_top(rest) if seg]
    if not segments:
        raise SchemaPathError(f"path has a root but no segments: {path!r}")
    return ParsedPath(root, segments)


def _self_test():
    files = sorted(glob.glob(os.path.join(ROOT, "docs", "*.schemapaths.json")))
    total = ok = 0
    failures, by_family = [], {}
    for fp in files:
        spec = json.load(open(fp, encoding="utf-8"))
        for item, rec in spec.items():
            total += 1
            fam = rec.get("family", "?")
            try:
                p = parse(rec["path"])
                ok += 1
                by_family.setdefault(fam, []).append(p)
            except SchemaPathError as e:
                failures.append((os.path.basename(fp), item, rec["path"], str(e)))
    print(f"parsed {ok}/{total} canonical paths across {len(files)} schemapaths.json files\n")
    print("families seen:")
    for fam in sorted(by_family):
        print(f"  {fam:28} {len(by_family[fam]):3}")
    if failures:
        print(f"\nFAILURES ({len(failures)}):")
        for f, item, path, err in failures:
            print(f"  [{f}] {item}: {path}\n      -> {err}")
        return 1
    print("\nALL canonical paths parsed cleanly.")
    # show a couple of structured examples
    print("\n--- sample parses ---")
    for sample in ["$MethodDefinition.schema:additionalProperty[schema:name='Torch Depth'].schema:value",
                   "$Dataset.prov:wasGeneratedBy.schema:object[schema:additionalType='materialsample'].schema:name",
                   "$Dataset.schema:measurementTechnique.schema:DefinedTerm.schema:identifier"]:
        print(f"{sample}\n   {json.dumps(parse(sample).to_dict())}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(json.dumps(parse(sys.argv[1]).to_dict(), indent=2))
    else:
        sys.exit(_self_test())
