"""Build the register of what EXISTS, from Ruolin's planning table.

Original columns are preserved verbatim and in order, so a PR back to the TAPP repo is a
clean diff. Four columns are appended:

  TAPP key        the machine key (empaTAPP). PRE-FILLED ONLY ON AN EXACT ACRONYM MATCH
                  against the technique directory -- anything less is left blank, because
                  fuzzy matching produced confident errors (it scored SNMS -> simsTAPP at
                  0.87 and offered xanesTAPP only as a runner-up for XANES).
  Technique dir   from build_tapp.TECH_DIR, once a key is filled in
  TAPP table      the source table TAPP_CONFIGS reads, or "draft"
  Geochem profile built / template (addtype not authored) / none

Rows for TAPPs that EXIST but have no planning row are appended at the end, flagged, since
a register of what exists must account for them.
"""
import csv, io, os, re, sys
sys.path.insert(0, "tools")
import build_tapp as b, build_profile as bp

SRC = r"tapp/Project Files/Registers & Planning/TAPP_Planning_Table.csv"
OUT = r"docs/registers/TAPP_Register.csv"
NEW = ["TAPP key", "Technique dir", "TAPP table", "Geochem profile"]

def squash(s):
    return re.sub(r"[^A-Za-z0-9]", "", s or "").upper()

# exact acronym -> tapp key, high precision only
by_dir = {squash(b.TECH_DIR[t]): t for t in b.TAPP_CONFIGS}
def exact_key(name):
    cands = set()
    for grp in re.findall(r"\(([^)]*)\)", name or ""):
        for part in re.split(r"[/&,]|–|-see-", grp):
            k = by_dir.get(squash(part))
            if k:
                cands.add(k)
    k = by_dir.get(squash(name))
    if k:
        cands.add(k)
    return cands.pop() if len(cands) == 1 else ""

def profile_state(t):
    c = bp.PROFILES.get(t)
    if not c:
        return "none"
    return "built" if c.get("addtype") else "template (addtype not authored)"

def table_of(t):
    x = str(b.TAPP_CONFIGS[t].get("xlsx", ""))
    return os.path.basename(x) if x.startswith("tapp/") else "draft"

if os.path.exists(OUT) and "--force" not in sys.argv:
    raise SystemExit(
        f"{OUT} already exists.\n"
        "This file is CURATED once generated -- the TAPP key column is authored by hand, and\n"
        "regenerating would discard that work. Re-run with --force only if you mean to start\n"
        "over, and commit first so the curation is recoverable."
    )

f = io.open(SRC, encoding="utf-8-sig", newline="")
banner = f.readline().rstrip("\r\n")
rd = csv.DictReader(f)
cols = list(rd.fieldnames)
rows = list(rd)

used, filled = set(), 0
for r in rows:
    name = (r.get("Proposed TAPP Name") or "").strip()
    k = exact_key(name) if name else ""
    if k:
        used.add(k); filled += 1
    r["TAPP key"] = k
    r["Technique dir"] = b.TECH_DIR.get(k, "") if k else ""
    r["TAPP table"] = table_of(k) if k else ""
    r["Geochem profile"] = profile_state(k) if k else ""

extra = sorted(set(b.TAPP_CONFIGS) - used, key=lambda t: b.TECH_DIR.get(t, t))
for t in extra:
    r = {c: "" for c in cols}
    r["#"] = "—"
    r["Proposed TAPP Name"] = f"(exists, no planning row) {b.TECH_DIR.get(t, t)}"
    r["Status"] = "IN REPO, NOT IN PLANNING TABLE"
    r["TAPP key"] = t
    r["Technique dir"] = b.TECH_DIR.get(t, "")
    r["TAPP table"] = table_of(t)
    r["Geochem profile"] = profile_state(t)
    rows.append(r)

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with io.open(OUT, "w", encoding="utf-8-sig", newline="") as g:
    g.write(banner + "," * len(NEW) + "\r\n")
    w = csv.DictWriter(g, fieldnames=cols + NEW)
    w.writeheader()
    w.writerows(rows)

print(f"planning rows            : {len(rows) - len(extra)}")
print(f"  TAPP key pre-filled    : {filled}   (exact acronym match only)")
print(f"  left blank for you     : {len(rows) - len(extra) - filled}")
print(f"appended (exist, unlisted): {len(extra)}")
print(f"  {' '.join(b.TECH_DIR.get(t, t) for t in extra)}")
print(f"\nwrote {OUT}  ({len(rows)} rows, {len(cols) + len(NEW)} columns)")
