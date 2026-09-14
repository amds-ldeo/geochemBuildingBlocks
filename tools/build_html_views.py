#!/usr/bin/env python3
"""Render a profile example as a self-contained HTML page for human readers.

One page per dataset record. The house style is the CDIF-record viewer's -- same CSS custom
properties, same light/dark handling, same sticky tabs and details/summary disclosure -- so these
pages sit beside those without looking foreign.

The page is deliberately NOT a generic JSON dumper. A record has a shape worth showing:

  banner      what the thing is -- title, identifier, abstract, and the badges that place it
              (technique, product type, status)
  Overview    citation-level fields a reader needs before anything else
  Provenance  the analysis event: when, where, on what instrument, on what sample -- and the
              PROCEDURE it followed, which is the link out to the TAPP page
  Variables   schema:variableMeasured as a table; a record can carry dozens and a disclosure
              list per variable is unreadable
  Files       the distribution and its components, likewise tabular
  Quality     dqv measurements
  Conformance which profiles the record declares

Anything not claimed by a section still renders, under "Other", so the page can never silently
drop a field the record carries -- the failure mode that matters for a metadata viewer.

    python tools/build_html_views.py --all
    python tools/build_html_views.py <example.json> -o out.html
"""
import argparse
import glob
import html
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TPROF = os.path.join(ROOT, "_sources", "techniqueProfile")
OUT = os.path.join(ROOT, "build", "htmlViews")

# A curie prefix is worth showing as a prefix, not expanded: readers recognise `schema:name`.
CURIE = re.compile(r"^([a-zA-Z][\w]*):(.+)$")


def esc(s):
    return html.escape(str(s), quote=True)


def label(key):
    """`schema:startDate` -> `startDate`, with the prefix kept as a dimmed span."""
    m = CURIE.match(key)
    if not m:
        return esc(key)
    return '<span class="curie">%s:</span>%s' % (esc(m.group(1)), esc(m.group(2)))


def is_ref(v):
    """A bare {@id} (optionally typed) is a REFERENCE, not an embedded object, and should render
    as a link rather than as a node to expand."""
    return isinstance(v, dict) and "@id" in v and not (set(v) - {"@id", "@type"})


def text_of(v):
    """A display string for a scalar-ish value, following the shapes the records actually use:
    a plain scalar, a {@value} literal, a {@id} reference, or a {schema:name} object."""
    if isinstance(v, (str, int, float, bool)):
        return esc(v)
    if isinstance(v, dict):
        if "@value" in v:
            return esc(v["@value"])
        if is_ref(v):
            i = v["@id"]
            href = i if i.startswith("http") else None
            return ('<a href="%s">%s</a>' % (esc(href), esc(i))) if href else \
                   '<span class="node-id">%s</span>' % esc(i)
        for k in ("schema:name", "skos:prefLabel", "schema:value"):
            if k in v and isinstance(v[k], (str, int, float)):
                return esc(v[k])
    return None


def render(v, depth=0):
    """Any value, as HTML. Objects become collapsible nodes; lists render their members."""
    t = text_of(v)
    if t is not None:
        return t
    if isinstance(v, list):
        if not v:
            return '<span class="empty">none</span>'
        return "".join('<div class="val">%s</div>' % render(x, depth + 1) for x in v)
    if isinstance(v, dict):
        head = None
        for k in ("schema:name", "skos:prefLabel", "@id"):
            if isinstance(v.get(k), str):
                head = v[k]
                break
        rows = "".join(
            '<div class="row"><div class="key">%s</div><div class="val">%s</div></div>'
            % (label(k), render(x, depth + 1))
            for k, x in v.items() if k not in ("@context",))
        return ('<details class="node"%s><summary><span class="node-label">%s</span></summary>'
                '<div class="node-body">%s</div></details>'
                % (" open" if depth < 1 else "", esc(head or "object"), rows))
    return '<span class="empty">none</span>'


def prop(key, value, desc=None):
    d = '<div class="desc">%s</div>' % esc(desc) if desc else ""
    return ('<details class="prop" open><summary>%s</summary>%s'
            '<div class="prop-val">%s</div></details>' % (label(key), d, render(value)))


def table(rows, cols):
    """A real table for the repeating structures -- variables and file components. A record can
    carry dozens of either, and a disclosure node per member is unreadable at that count."""
    if not rows:
        return '<span class="empty">none</span>'
    head = "".join("<th>%s</th>" % esc(c[0]) for c in cols)
    body = []
    for r in rows:
        tds = []
        for _, get in cols:
            v = get(r)
            tds.append("<td>%s</td>" % (render(v) if not isinstance(v, str) else esc(v)))
        body.append("<tr>%s</tr>" % "".join(tds))
    return ('<div class="tablewrap"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>'
            % (head, "".join(body)))


def g(o, *keys, default=""):
    for k in keys:
        if isinstance(o, dict) and k in o:
            return o[k]
    return default


def first(o, key):
    v = o.get(key)
    if isinstance(v, list):
        return v[0] if v else {}
    return v or {}


def tapp_ref(doc):
    """The procedure this record followed: a prov:used entry typed ada:TAPPDefinition.

    A REFERENCE ({@id, @type}) is what we emit and what the page links to. An embedded TAPP is
    also legal, and is shown inline instead -- there is nothing to navigate to.
    """
    for act in doc.get("prov:wasGeneratedBy") or []:
        for u in act.get("prov:used") or []:
            ty = u.get("@type") or []
            if isinstance(ty, str):
                ty = [ty]
            if any("TAPPDefinition" in str(t) for t in ty):
                return u
    return None


# Keys each tab claims. Anything left over lands in "Other", so no field is silently dropped.
SECTIONS = [
    ("Overview", ["schema:name", "schema:description", "schema:identifier", "schema:url",
                  "schema:version", "schema:dateModified", "schema:datePublished",
                  "schema:creativeWorkStatus", "schema:keywords", "schema:license",
                  "schema:conditionsOfAccess", "schema:additionalType",
                  "schema:measurementTechnique"]),
    ("People & funding", ["schema:creator", "schema:contributor", "schema:funding",
                          "schema:publisher", "schema:maintainer"]),
    ("Provenance", ["prov:wasGeneratedBy"]),
    ("Variables", ["schema:variableMeasured"]),
    ("Files", ["schema:distribution"]),
    ("Quality", ["dqv:hasQualityMeasurement"]),
    ("Conformance", ["schema:subjectOf"]),
]
SKIP = {"@context", "@id", "@type"}

VAR_COLS = [("Name", lambda v: g(v, "schema:name")),
            ("Description", lambda v: g(v, "schema:description")),
            ("Unit", lambda v: g(v, "cdi:simpleUnitOfMeasure", "schema:unitText")),
            ("Type", lambda v: g(v, "ada:dataType")),
            ("Identifier", lambda v: g(v, "@id"))]

PART_COLS = [("Name", lambda p: g(p, "schema:name")),
             ("Component type", lambda p: g(p, "ada:componentType")),
             ("Format", lambda p: g(p, "schema:encodingFormat")),
             ("Size", lambda p: g(p, "schema:size")),
             ("Description", lambda p: g(p, "schema:description"))]


def provenance_panel(doc, tapp_href):
    """The analysis event, with the procedure promoted to the top: it is the question a reader
    most often arrives with, and the one link off this page."""
    out = []
    ref = tapp_ref(doc)
    if ref and is_ref(ref):
        tid = ref.get("@id", "")
        link = ('<a class="procedure-link" href="%s">%s</a>' % (esc(tapp_href), esc(tid))
                if tapp_href else '<span class="node-id">%s</span>' % esc(tid))
        out.append('<div class="group">Procedure</div>'
                   '<p class="lead">This dataset was produced by following the analytical '
                   'procedure below. %s</p><div class="procedure">%s</div>'
                   % ("Open it to see the parameters it fixes."
                      if tapp_href else "The procedure is referenced but not resolvable here.", link))
    elif ref:
        out.append('<div class="group">Procedure (embedded)</div>%s' % render(ref))
    else:
        out.append('<div class="group">Procedure</div>'
                   '<p class="note">This record does not name the procedure it followed.</p>')
    for act in doc.get("prov:wasGeneratedBy") or []:
        rest = {k: v for k, v in act.items() if k != "prov:used"}
        out.append('<div class="group">Analysis event</div>%s' % render(rest))
        insts = [i for u in (act.get("prov:used") or []) for i in (u.get("schema:instrument") or [])]
        if insts:
            out.append('<div class="group">Instrument</div>%s' % render(insts))
    return "".join(out)


def badges(doc):
    out = []
    for t in (doc.get("schema:additionalType") or []):
        s = t.get("@id") if isinstance(t, dict) else t
        if s:
            out.append('<span class="badge">%s</span>' % esc(s))
    st = doc.get("schema:creativeWorkStatus")
    if st:
        out.append('<span class="badge">%s</span>' % esc(st))
    for m in (doc.get("schema:measurementTechnique") or []):
        s = m.get("schema:name") if isinstance(m, dict) else m
        if s:
            out.append('<span class="badge">%s</span>' % esc(s))
    return "".join(out)


def build_page(doc, css, tapp_href=None, title=None):
    name = doc.get("schema:name") or doc.get("@id") or "ADA record"
    did = doc.get("@id", "")
    url = doc.get("schema:url")
    ids = esc(did)
    if url:
        ids += ' &middot; <a href="%s">%s</a>' % (esc(url), esc(url))
    panels, tabs, claimed = [], [], set(SKIP)
    for i, (tab, keys) in enumerate(SECTIONS):
        present = [k for k in keys if k in doc]
        claimed.update(keys)
        if not present and tab != "Provenance":
            continue
        if tab == "Provenance":
            body = provenance_panel(doc, tapp_href)
            count = len(doc.get("prov:wasGeneratedBy") or [])
        elif tab == "Variables":
            body = table(doc.get("schema:variableMeasured") or [], VAR_COLS)
            count = len(doc.get("schema:variableMeasured") or [])
        elif tab == "Files":
            body = ""
            dists = doc.get("schema:distribution") or []
            for dist in dists:
                meta = {k: v for k, v in dist.items() if k != "schema:hasPart"}
                body += '<div class="group">Distribution</div>%s' % render(meta)
                parts = dist.get("schema:hasPart") or []
                if parts:
                    body += ('<div class="group">Components <span class="count">%d</span></div>%s'
                             % (len(parts), table(parts, PART_COLS)))
            count = sum(len(d.get("schema:hasPart") or []) for d in dists)
        else:
            body = "".join(prop(k, doc[k]) for k in present)
            count = len(present)
        tabs.append('<button role="tab" aria-selected="%s" aria-controls="p%d">%s'
                    '<span class="count">%d</span></button>'
                    % ("true" if not panels else "false", i, esc(tab), count))
        panels.append('<div class="panel" id="p%d" role="tabpanel"%s>%s</div>'
                      % (i, "" if not panels else " hidden", body))
    leftover = [k for k in doc if k not in claimed]
    if leftover:
        tabs.append('<button role="tab" aria-selected="false" aria-controls="pX">Other'
                    '<span class="count">%d</span></button>' % len(leftover))
        panels.append('<div class="panel" id="pX" role="tabpanel" hidden>'
                      '<p class="lead">Fields this record carries that no section above claims. '
                      'Shown so nothing is silently dropped.</p>%s</div>'
                      % "".join(prop(k, doc[k]) for k in leftover))
    return PAGE % {"title": esc(title or name), "css": css, "name": esc(name), "ids": ids,
                   "badges": badges(doc),
                   "abstract": esc(doc.get("schema:description") or ""),
                   "tabs": "".join(tabs), "panels": "".join(panels)}


# Added to the inherited house CSS: the record pages need tables (variables, components) and a
# prominent procedure link, neither of which the CDIF-record viewer had.
EXTRA_CSS = """
.tablewrap{overflow-x:auto;margin:.25rem 0 1rem}
table{border-collapse:collapse;width:100%;font-size:.88rem}
th,td{border:1px solid var(--line);padding:.35rem .5rem;text-align:left;vertical-align:top}
th{background:var(--card);font-weight:600;white-space:nowrap}
tbody tr:nth-child(even){background:var(--card)}
.count{color:var(--muted);font-weight:400;font-size:.8em;margin-left:.35rem}
.procedure{margin:.25rem 0 1rem}
a.procedure-link{display:inline-block;background:var(--badge);border:1px solid var(--line);
  border-radius:4px;padding:.4rem .7rem;font-weight:600;text-decoration:none}
a.procedure-link:hover{border-color:var(--accent)}
.note{color:var(--warn);background:var(--warnbg);border-radius:4px;padding:.4rem .6rem;
  max-width:80ch;font-size:.87rem;margin:.2rem 0 .8rem}
table.grid th{vertical-align:bottom;font-size:.82rem;max-width:14rem;white-space:normal}
table.grid td.rowhead,table.grid th.rowhead{background:var(--card);font-weight:600;
  white-space:nowrap;position:sticky;left:0}
table.grid .coldefault{font-weight:400;color:var(--muted);font-size:.78rem;margin-top:.2rem;
  border-top:1px dotted var(--line);padding-top:.15rem}
table.grid tbody td:empty::after{content:'4';color:var(--line)}
"""

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%(title)s</title>
<style>%(css)s</style>
</head>
<body>
<div class="wrap">
<header class="banner">
<h1>%(name)s</h1>
<div class="ids">%(ids)s</div>
<div>%(badges)s</div>
<div class="abstract">%(abstract)s</div>
</header>
<nav class="tabs" role="tablist">%(tabs)s</nav>
%(panels)s
</div>
<script>
document.querySelectorAll('nav.tabs button').forEach(function(b){
  b.addEventListener('click',function(){
    document.querySelectorAll('nav.tabs button').forEach(function(x){
      x.setAttribute('aria-selected', x===b ? 'true' : 'false');});
    document.querySelectorAll('.panel').forEach(function(p){
      p.hidden = (p.id !== b.getAttribute('aria-controls'));});
  });
});
</script>
</body>
</html>
"""


def house_css():
    """Reuse the CDIF-record viewer's stylesheet when it is available, so the pages match; fall
    back to the minimum needed to be readable when it is not."""
    for cand in [os.path.join(ROOT, "..", "metadata", "htmlViews", "index.html")]:
        try:
            t = open(cand, encoding="utf-8").read()
            return t[t.index("<style>") + 7:t.index("</style>")] + EXTRA_CSS
        except Exception:
            pass
    return FALLBACK_CSS + EXTRA_CSS


FALLBACK_CSS = """
:root{--bg:#fff;--fg:#1c1f24;--muted:#5b6472;--line:#dde2e8;--accent:#1c5d8c;
      --card:#f7f9fb;--badge:#e6eef5;--warn:#8a5a00;--warnbg:#fdf6e3}
@media (prefers-color-scheme:dark){
 :root{--bg:#14171b;--fg:#e6e9ee;--muted:#98a2b3;--line:#2b3138;--accent:#7fb6dd;
       --card:#1b1f25;--badge:#243039;--warn:#e0b661;--warnbg:#2a2416}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);
 font:15px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
.wrap{max-width:1100px;margin:0 auto;padding:1.5rem 1.25rem 4rem}
a{color:var(--accent)}
header.banner{border-bottom:2px solid var(--line);padding-bottom:1rem}
header.banner h1{margin:.1rem 0 .5rem;font-size:1.55rem}
.ids{color:var(--muted);font-size:.83rem;word-break:break-all;margin-bottom:.5rem}
.abstract{margin:.5rem 0 0;max-width:80ch}
.badge{display:inline-block;background:var(--badge);border-radius:3px;padding:.05rem .4rem;
 font-size:.75rem;margin-right:.3rem}
nav.tabs{display:flex;flex-wrap:wrap;gap:.25rem;border-bottom:1px solid var(--line);
 margin:1.25rem 0;position:sticky;top:0;background:var(--bg);z-index:5;padding-top:.5rem}
nav.tabs button{border:1px solid transparent;border-bottom:none;background:none;color:var(--muted);
 font:inherit;font-size:.9rem;padding:.45rem .8rem;cursor:pointer;border-radius:5px 5px 0 0}
nav.tabs button[aria-selected=true]{color:var(--fg);font-weight:600;background:var(--card);
 border-color:var(--line)}
.panel[hidden]{display:none}
.panel>p.lead{color:var(--muted);margin:0 0 1.25rem;max-width:80ch}
.group{font-size:.78rem;text-transform:uppercase;letter-spacing:.06em;color:var(--muted);
 margin:1.6rem 0 .7rem;padding-bottom:.25rem;border-bottom:1px solid var(--line);font-weight:600}
.prop{margin:0 0 1.4rem}
.prop>summary{font-size:1rem;font-weight:600;cursor:pointer;border-bottom:1px solid var(--line);
 padding:0 0 .2rem 0}
.desc{color:var(--muted);font-size:.86rem;margin:.2rem 0}
.row{display:flex;gap:.6rem;padding:.15rem 0}
.key{flex:0 0 15rem;color:var(--muted);font-size:.86rem}
.val{min-width:0;overflow-wrap:anywhere}
details.node>summary{cursor:pointer}
.node-body{border-left:2px solid var(--line);padding-left:.7rem;margin:.2rem 0 .2rem .2rem}
.node-id,.curie{color:var(--muted)}
.empty{color:var(--muted);font-style:italic}
"""


# A keyed table: the `defines: <keyset>` member list is the ROWS, the properties keyed to that
# set are the COLUMNS. Template key -> (row key, column key, what the rows are).
KEYED_TABLES = [
    ("ada:targetSpeciesTemplate",     "ada:defaultTargetSpecies",     "ada:targetSpeciesColumns",
     "target species"),
    ("ada:monitoredPropertyTemplate", "ada:defaultMonitoredProperties", "ada:monitoredPropertyColumns",
     "monitored property"),
    ("ada:reportedPropertyTemplate",  "ada:defaultReportedProperties", "ada:reportedPropertyColumns",
     "reported property"),
]


def _col_value(col):
    return col.get("schema:defaultValue", col.get("schema:value"))


def keyed_grid(rows, cols, domain):
    """Render one keyed table.

    The honest part. A column carries ONE schema:defaultValue for the whole column, not a value
    per member, so a 14x10 table has real axes and no cell data. Repeating the column default
    down every row would assert something the record does not say -- that each member has that
    value. Instead the default is shown once, under the column name, and the member cells are
    left empty with the reason stated. When a column's value IS a per-member list of the right
    length (the shape the branch 2/3 design targets), it is used per row and the cells fill in.
    """
    named = [c for c in cols if isinstance(c, dict)]
    if not rows and not named:
        return ""
    per_member = {}
    for i, c in enumerate(named):
        v = _col_value(c)
        if isinstance(v, list) and len(v) == len(rows) and rows:
            per_member[i] = v
    head = ['<th class="rowhead">%s</th>' % esc(domain)]
    for c in named:
        nm = esc(c.get("schema:name") or c.get("schema:valueName") or "?")
        v = _col_value(c)
        dflt = ("" if (isinstance(v, list) or v is None)
                else '<div class="coldefault">default: %s</div>' % esc(v))
        head.append("<th>%s%s</th>" % (nm, dflt))
    body = []
    for r_i, r in enumerate(rows):
        tds = ['<td class="rowhead">%s</td>' % esc(r if isinstance(r, str) else text_of(r) or "")]
        for c_i, _ in enumerate(named):
            cell = per_member.get(c_i, [None] * len(rows))[r_i] if c_i in per_member else None
            tds.append("<td>%s</td>" % (esc(cell) if cell is not None else ""))
        body.append("<tr>%s</tr>" % "".join(tds))
    if not body:
        body.append('<tr><td class="rowhead"><span class="empty">no members listed</span></td>'
                    '%s</tr>' % ("<td></td>" * len(named)))
    note = ""
    if named and not per_member:
        note = ('<p class="note">The columns carry one default each, shown in the header. '
                'Per-member values are not carried by the record yet, so the member cells are '
                'empty rather than repeating a column default as if it were per-member.</p>')
    return ('%s<div class="tablewrap"><table class="grid"><thead><tr>%s</tr></thead>'
            '<tbody>%s</tbody></table></div>' % (note, "".join(head), "".join(body)))


def collector_grid(doc):
    """ada:collectorConfiguration is the same idea without a template: it sits on an instrument
    part and IS the column array directly, one entry per collector."""
    out = []
    for inst in doc.get("schema:instrument") or []:
        for part in inst.get("schema:hasPart") or []:
            cc = part.get("ada:collectorConfiguration")
            if cc:
                out.append('<div class="group">Collector configuration <span class="count">%d</span>'
                           "</div>%s" % (len(cc), keyed_grid([], cc, "collector")))
    return "".join(out)


def tapp_page_name(ref_id):
    """`ex:finesseTAPP-P0` -> the filename the TAPP page will be written as. Kept in one place so
    the two generators cannot drift apart on naming."""
    return "tapp_%s.html" % re.sub(r"[^A-Za-z0-9._-]", "_", (ref_id or "").split(":")[-1])


TAPP_SECTIONS = [
    ("Overview", ["schema:name", "schema:description", "schema:measurementTechnique",
                  "ada:analyticalMode", "ada:targetMaterial", "schema:creator", "schema:location",
                  "schema:datePublished", "schema:funding", "schema:citation"]),
    ("Procedure", ["schema:actionProcess"]),
    ("Instrument", ["schema:instrument", "ada:instrumentManufacturer", "ada:instrumentModel"]),
]
TAPP_KEYED_KEYS = {k for t in KEYED_TABLES for k in t[:3]}


def build_tapp_page(doc, css, back_href=None):
    """The TAPP page. Same chrome as the dataset page; the difference is the Keyed values tab,
    where a `defines: <keyset>` member list becomes the rows of a grid and the properties keyed to
    that set become its columns."""
    name = doc.get("schema:name") or doc.get("@id") or "TAPP definition"
    ids = esc(doc.get("@id", ""))
    panels, tabs, claimed = [], [], set(SKIP) | TAPP_KEYED_KEYS
    for i, (tab, keys) in enumerate(TAPP_SECTIONS):
        present = [k for k in keys if k in doc]
        claimed.update(keys)
        if not present:
            continue
        body = "".join(prop(k, doc[k]) for k in present)
        if tab == "Instrument":
            body += collector_grid(doc)
        tabs.append('<button role="tab" aria-selected="%s" aria-controls="t%d">%s'
                    '<span class="count">%d</span></button>'
                    % ("true" if not panels else "false", i, esc(tab), len(present)))
        panels.append('<div class="panel" id="t%d" role="tabpanel"%s>%s</div>'
                      % (i, "" if not panels else " hidden", body))
    # Keyed values
    grids, ngrid = [], 0
    for tkey, rkey, ckey, domain in KEYED_TABLES:
        tpl = doc.get(tkey)
        if not isinstance(tpl, dict):
            continue
        rows, cols = tpl.get(rkey) or [], tpl.get(ckey) or []
        if not rows and not cols:
            continue
        ngrid += 1
        grids.append('<div class="group">%s <span class="count">%d x %d</span></div>%s'
                     % (esc(domain), len(rows), len(cols), keyed_grid(rows, cols, domain)))
    if grids:
        tabs.append('<button role="tab" aria-selected="%s" aria-controls="tK">Keyed values'
                    '<span class="count">%d</span></button>'
                    % ("true" if not panels else "false", ngrid))
        panels.append('<div class="panel" id="tK" role="tabpanel"%s>'
                      '<p class="lead">Each grid is one keyed set: the rows are the members the '
                      'procedure defines, the columns the properties keyed to that set.</p>%s</div>'
                      % ("" if not panels else " hidden", "".join(grids)))
    leftover = [k for k in doc if k not in claimed]
    if leftover:
        tabs.append('<button role="tab" aria-selected="false" aria-controls="tX">Parameters'
                    '<span class="count">%d</span></button>' % len(leftover))
        panels.append('<div class="panel" id="tX" role="tabpanel" hidden>'
                      '<p class="lead">Everything else the procedure fixes.</p>%s</div>'
                      % "".join(prop(k, doc[k]) for k in leftover))
    back = ('<div class="ids"><a href="%s">&larr; back to the dataset</a></div>' % esc(back_href)
            if back_href else "")
    return PAGE % {"title": esc(name), "css": css, "name": esc(name),
                   "ids": ids + back, "badges": badges(doc),
                   "abstract": esc(doc.get("schema:description") or ""),
                   "tabs": "".join(tabs), "panels": "".join(panels)}


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("example", nargs="?", help="a profile example*.json")
    ap.add_argument("--all", action="store_true", help="every profile example")
    ap.add_argument("-o", "--out", help="output file (single-example mode)")
    ap.add_argument("--outdir", default=OUT)
    a = ap.parse_args()

    files = []
    if a.all:
        files = sorted(glob.glob(os.path.join(TPROF, "*", "*", "profile*", "example*.json")))
        tapps = sorted(glob.glob(os.path.join(TPROF, "*", "*", "tapp", "example*.json")))
    elif a.example:
        files = [a.example]
    else:
        ap.error("give an example, or --all")

    css = house_css()
    os.makedirs(a.outdir, exist_ok=True)
    n = nolink = 0
    for f in files:
        try:
            doc = json.loads(open(f, "rb").read().decode("utf-8"))
        except Exception as e:
            print("  UNREADABLE %s: %s" % (f, e))
            continue
        ref = tapp_ref(doc)
        href = tapp_page_name(ref.get("@id")) if (ref and is_ref(ref)) else None
        if href is None:
            nolink += 1
        page = build_page(doc, css, tapp_href=href)
        dest = a.out if (a.out and not a.all) else os.path.join(
            a.outdir, os.path.splitext(os.path.basename(f))[0] + ".html")
        with open(dest, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(page)
        n += 1
        if not a.all:
            print("wrote %s" % dest)
    if a.all:
        nt = 0
        for f in tapps:
            try:
                doc = json.loads(open(f, "rb").read().decode("utf-8"))
            except Exception as e:
                print("  UNREADABLE %s: %s" % (f, e))
                continue
            dest = os.path.join(a.outdir, tapp_page_name(doc.get("@id") or
                                os.path.splitext(os.path.basename(f))[0]))
            with open(dest, "w", encoding="utf-8", newline="\n") as fh:
                fh.write(build_tapp_page(doc, css))
            nt += 1
        print("wrote %d dataset page(s) and %d TAPP page(s) to %s" % (n, nt, a.outdir))
        if nolink:
            print("  %d of them name no procedure -- prov:used carries no ada:TAPPDefinition "
                  "reference yet, so those pages have no link to a TAPP." % nolink)
    return 0


if __name__ == "__main__":
    sys.exit(main())
