#!/usr/bin/env python3
"""Regenerate the family table in docs/SCHEMA_PATH_GRAMMAR.md from the recognizer itself.

The table was hand-maintained and drifted: two weeks after it was written the code had 47 families
and the doc described 23. A reference that documents half the grammar is worse than one that admits
it is generated, so the list now comes from `normalize_schema_paths.recognize()` — the same source
the pipeline enforces — and the prose around it stays hand-written.

Each family's regex is rendered as a readable SHAPE rather than printed raw: `[^']*` becomes
`<value>`, `[a-z][A-Za-z0-9]*` becomes `<name>`, alternations stay as they are. The comment sitting
above a family in the source is its explanation, so that is carried across too.

    python tools/gen_grammar_doc.py            # print the table
    python tools/gen_grammar_doc.py --write    # splice it into the doc
"""
import argparse
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "tools", "normalize_schema_paths.py")
DOC = os.path.join(ROOT, "docs", "SCHEMA_PATH_GRAMMAR.md")
BEGIN = "<!-- BEGIN generated: families -->"
END = "<!-- END generated: families -->"

# regex -> readable shape, most specific first
SHAPE = [
    (r"\(\?<!Default\)", ""),
    (r"\[\^'\]\*", "<value>"),
    (r"\[a-z\]\[A-Za-z0-9\]\*", "<name>"),
    (r"\[A-Za-z\]\[A-Za-z0-9\]\*", "<name>"),
    (r"\[A-Za-z0-9\]\+", "<name>"),
    (r"\\\$", "$"),
    (r"\\\.", "."),
    (r"\\\[", "["),
    (r"\\\]", "]"),
    (r"\\\(", "("),
    (r"\\\)", ")"),
]


def shape(rx):
    s = rx
    for pat, rep in SHAPE:
        s = re.sub(pat, rep, s)
    s = s.lstrip("^").rstrip("$")
    s = s.replace("([])?", "[]?").replace("()?", "")
    return s.strip()


def families():
    """[(name, shape, comment)] in source order."""
    src = io.open(SRC, encoding="utf-8").read()
    i = src.index("    fams = [")
    j = src.index("\n    ]", i)
    body = src[i:j]
    out, pending = [], []
    for line in body.splitlines():
        st = line.strip()
        if st.startswith("#"):
            pending.append(st.lstrip("# ").rstrip())
            continue
        m = re.search(r'\(r"(.+)",\s*"([a-z][a-z0-9-]*)"\)', st)
        if not m:
            m2 = re.search(r'\(r"(.+)",$', st)
            if m2:
                pending.append("\x00" + m2.group(1))   # regex continued on the next line
            else:
                m3 = re.search(r'^"([a-z][a-z0-9-]*)"\)', st)
                if m3 and pending and pending[-1].startswith("\x00"):
                    rx = pending.pop()[1:]
                    out.append((m3.group(1), shape(rx), " ".join(pending)))
                    pending = []
            continue
        out.append((m.group(2), shape(m.group(1)), " ".join(p for p in pending if not p.startswith("\x00"))))
        pending = []
    return out


def table(fams):
    distinct = len({n for n, _, _ in fams})
    lines = [BEGIN,
             "",
             f"*{len(fams)} patterns across {distinct} families — two families are recognised by "
             "more than one shape. Generated from `tools/normalize_schema_paths.py` by "
             "`tools/gen_grammar_doc.py`; edit the recognizer, not this table.*",
             "",
             "| family | canonical shape |",
             "|---|---|"]
    for name, sh, comment in fams:
        lines.append(f"| `{name}` | `{sh}` |")
    lines += ["", END]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args()
    fams = families()
    t = table(fams)
    if not a.write:
        print(t)
        return 0
    doc = io.open(DOC, encoding="utf-8").read()
    if BEGIN in doc and END in doc:
        pre = doc[:doc.index(BEGIN)]
        post = doc[doc.index(END) + len(END):]
        doc = pre + t + post
    else:
        raise SystemExit(f"markers not found in {DOC}; add {BEGIN} / {END} where the table belongs")
    io.open(DOC, "w", encoding="utf-8", newline="\n").write(doc)
    print(f"wrote {len(fams)} families into {os.path.relpath(DOC, ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
