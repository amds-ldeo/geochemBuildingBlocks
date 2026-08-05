"""Locate a building-block directory by its (pre-reorg) identity name under the group-by-technique
_sources layout.

The reorg renamed the per-technique BB dirs to roles (techniqueProfile/<tech>/{tapp,detail,profile,
profile-ada}), so a lookup by the old identity name (empaTAPP, detailLAICPMS, adaEMPA, empaProfile…)
no longer matches a directory name. This resolver maps those names to their new location:

  - identity-named BBs (adaProduct, tappDefinition, registry catalogs, BaseSchema helpers): exact search
  - <x>TAPP        -> techniqueProfile/<tech>/tapp
  - detail<X>      -> techniqueProfile/<tech>/detail   (detailXCT -> .../detail-legacy)
  - ada<X> generic -> techniqueProfile/<tech>/profile-ada
  - <geochem name> -> techniqueProfile/<tech>/profile   (empaProfile, LA-ICPMS, Geochron, SEM-Imaging…)
"""
from pathlib import Path

# lowercased technique token -> technique directory name under techniqueProfile/
_ALIAS = {
    "empa": "EMPA", "geochron": "Geochron", "laicpms": "LA-ICPMS", "icpms": "ICPMS",
    "labxct": "XCT", "xct": "XCT", "sem": "SEM", "semimaging": "SEM-Imaging",
    "semfibsem": "SEM-FIBSEM", "semcomposition": "SEM-Composition",
    "solutionqicpms": "Solution-Q-ICPMS", "solutionsficpms": "Solution-SF-ICPMS",
    "tem": "TEM", "argt": "ARGT", "dsc": "DSC", "eairms": "EAIRMS", "icpoes": "ICPOES",
    "l2ms": "L2MS", "laf": "LAF", "nanoir": "NanoIR", "nanosims": "NanoSIMS", "psfd": "PSFD",
    "qris": "QRIS", "sls": "SLS", "vnmir": "VNMIR", "xrd": "XRD", "basemap": "Basemap",
    "aiva": "AIVA", "ams": "AMS", "fticrms": "FTICRMS", "gcms": "GCMS", "gpyc": "GPYC",
    "ic": "IC", "lcms": "LCMS", "lit": "LIT", "ngnsms": "NGNSMS", "raman": "RAMAN",
    "ritofngms": "RITOFNGMS", "sims": "SIMS", "svruec": "SVRUEC", "tofsims": "ToFSIMS",
    "uvfm": "UVFM", "vlm": "VLM", "xanes": "XANES",
    # geochemProfile dir names (path-driven product profiles)
    "empaprofile": "EMPA", "la-icpms": "LA-ICPMS", "lab-xct": "XCT",
    "sem-imaging": "SEM-Imaging", "sem-fibsem": "SEM-FIBSEM", "sem-composition": "SEM-Composition",
    "solution-q-icpms": "Solution-Q-ICPMS", "solution-sf-icpms": "Solution-SF-ICPMS",
}


def _tech(token: str) -> str:
    return _ALIAS.get(token.lower(), token)


def find_bb_dir(name: str, sources) -> Path | None:
    """Return the BB directory for `name` under `sources` (the _sources root), or None."""
    sources = Path(sources)
    tp = sources / "techniqueProfile"

    def ok(d: Path):
        return d if d.is_dir() and (d / "schema.yaml").exists() else None

    # 1. identity-named BB anywhere (adaProduct, tappDefinition, registry catalogs, BaseSchema helpers)
    for cand in sources.rglob(name):
        if (hit := ok(cand)):
            return hit
    # 2. <x>TAPP
    if name.endswith("TAPP"):
        if (hit := ok(tp / _tech(name[:-4]) / "tapp")):
            return hit
    # 3. detail<X>  (old detailXCT stub lives under detail-legacy)
    if name.startswith("detail"):
        role = "detail-legacy" if name == "detailXCT" else "detail"
        if (hit := ok(tp / _tech(name[len("detail"):]) / role)):
            return hit
    # 4. generic ada<X> profile
    if name.startswith("ada"):
        if (hit := ok(tp / _tech(name[3:]) / "profile-ada")):
            return hit
    # 5. path-driven geochem product profile (by dir/technique name)
    if (hit := ok(tp / _tech(name) / "profile")):
        return hit
    return None
