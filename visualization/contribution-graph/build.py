#!/usr/bin/env python3
"""build.py -- Scan strategy/ and emit data.js for the contribution-graph viz.

For every vertex directory under strategy/ this script tries to extract:

  Pillar A (COMPLY)       <vertex>-comply-bare.md  (or -clay-bare.md)
  Pillar B (INDEPENDENT)  <vertex>-independence-bare.md
  Pillar C (CONTRIBUTE)   <vertex>-harden-bare.md
  Bonus    (BEYOND)       <vertex>-beyond-bare.md

  + run-02 compliance-map.md   (verdict counts P/Pa/O/S)
  + run-05 primitive-log.md    (Pillar B primitive counts BYP/DEC/EXC/TRP)
  + run-06 commit-memo.md      (Pillar C externals list)
  + cross-cut edges from strategy/x-ray/pac-output/runs/run-01/cross-cut-edges.md

For vertices missing files we still emit the slot ("AUDIT PENDING") so the
ring renders with all 25 + framework slots.

Output: data.js, build.log.  No external deps -- Python 3 stdlib only.
"""
from __future__ import annotations

import datetime as _dt
import json
import math
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent.parent
STRATEGY = ROOT / "strategy"
OUT_DIR = ROOT / "visualization" / "contribution-graph"
OUT = OUT_DIR / "data.js"
LOG = OUT_DIR / "build.log"

# Six Millennium vertices have full deliverables today.
MILL_VERTICES = {"ym", "rh", "bsd", "pvnp", "hodge", "ns"}

# Canonical 25-vertex ring order matches the torus visualization for visual
# continuity across the three viewers.  Names use lowercase strategy-dir keys.
RING_ORDER = [
    "qg5d",        # 0  NORTH
    "ym",          # 1  NORTH
    "rh",          # 2  NORTH
    "lindelof",    # 3  EAST
    "grh",         # 4  EAST
    "bgs-spectral-statistics",  # 5  EAST
    "bsd",         # 6  NORTH
    "pvnp",        # 7  EAST
    "hilbert-6",   # 8  WEST
    "hilbert-12",  # 9  SOUTH
    "cramer",      # 10 EAST
    "ns",          # 11 EAST
    "hodge",       # 12 WEST
    "turbulence",  # 13 SOUTH
    "katz-sarnak", # 14 EAST
    "sato-tate",   # 15 WEST
    "twin-primes", # 16 SOUTH
    "goldbach",    # 17 SOUTH
    "schanuel",    # 18 SOUTH
    "odd-perfect", # 19 WEST
    "collatz",     # 20 WEST
    "lehmer",      # 21 WEST
    "abc",         # 22 SOUTH
    "baum-connes", # 23 WEST
    "vp-vs-vnp",   # 24 SOUTH
]

ZONE_BY_INDEX = {
    0: "NORTH", 1: "NORTH", 2: "NORTH", 6: "NORTH",
    3: "EAST", 4: "EAST", 5: "EAST", 7: "EAST", 10: "EAST", 11: "EAST", 14: "EAST",
    8: "WEST", 12: "WEST", 15: "WEST", 19: "WEST", 20: "WEST", 21: "WEST", 23: "WEST",
    9: "SOUTH", 13: "SOUTH", 16: "SOUTH", 17: "SOUTH", 18: "SOUTH", 22: "SOUTH", 24: "SOUTH",
}

# Pretty display name for each vertex slot.
DISPLAY_NAME = {
    "qg5d": "QG5D",
    "ym": "YM",
    "rh": "RH",
    "lindelof": "Lindelöf",
    "grh": "GRH",
    "bgs-spectral-statistics": "BGS",
    "bsd": "BSD",
    "pvnp": "P vs NP",
    "hilbert-6": "H6",
    "hilbert-12": "H12",
    "cramer": "Cramér",
    "ns": "NS",
    "hodge": "Hodge",
    "turbulence": "Turb",
    "katz-sarnak": "Katz-Sarnak",
    "sato-tate": "Sato-Tate",
    "twin-primes": "Twin Primes",
    "goldbach": "Goldbach",
    "schanuel": "Schanuel",
    "odd-perfect": "OPN",
    "collatz": "Collatz",
    "lehmer": "Lehmer",
    "abc": "ABC",
    "baum-connes": "Baum-Connes",
    "vp-vs-vnp": "VP vs VNP",
}

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
_LOG: list[str] = []

def log(msg: str) -> None:
    _LOG.append(msg)

def flush_log() -> None:
    LOG.write_text("\n".join(_LOG) + "\n", encoding="utf-8")

def safe_read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        log(f"ERR  {path}: {e}")
        return ""

# ---------------------------------------------------------------------------
# Per-pillar parsers
# ---------------------------------------------------------------------------

def _count_theorems(text: str) -> int:
    """Heuristic: count occurrences of bold 'Theorem' or 'Proposition'."""
    return len(re.findall(r"\*\*(Theorem|Proposition|Lemma|Corollary)\b", text, re.IGNORECASE))

def _count_sections(text: str) -> int:
    return len(re.findall(r"^##\s+", text, re.MULTILINE))

def _count_layers(text: str) -> int:
    """Programme proof-chain layer references (L1, L2, ...)."""
    return len(set(re.findall(r"\bL\d+[a-z]?\b", text)))

def _extract_named_walls(text: str) -> list[str]:
    """Pull explicit named walls referenced in the deliverable.

    Walls usually appear as W1, W2, ..., or W1^Pillar-A.
    """
    walls: list[str] = []
    for m in re.finditer(r"W_?(\d+)(?:\s*=\s*([A-Za-z0-9.\-\/_§ ]{2,40}))?", text):
        token = f"W{m.group(1)}"
        rhs = (m.group(2) or "").strip().strip(",.;:")
        if rhs and len(rhs) < 60:
            label = f"{token} = {rhs}"
        else:
            label = token
        if label not in walls:
            walls.append(label)
    return walls[:5]

def _extract_externals(harden_text: str, commit_memo_text: str) -> list[dict]:
    """Pull external citations from the harden-bare table (E1..E12) plus
    an ALL-attribution back-stop from the commit memo.
    """
    externals: list[dict] = []
    # Primary parse: harden-bare master table rows with format
    #  | E1 | Balaban multi-scale RG | Bałaban CMP 95-119 (1982-89) | ...
    for m in re.finditer(
        r"\|\s*(E\d{1,2})\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", harden_text):
        eid, name, refs = m.group(1), m.group(2).strip(), m.group(3).strip()
        if name.lower().startswith("external"):
            continue  # skip header row
        if eid in {e["id"] for e in externals}:
            continue
        externals.append({
            "id": eid,
            "name": name[:120],
            "authors": refs[:160],
        })
    return externals

def _count_primitives(prim_log_text: str) -> dict[str, int]:
    counts = {"BYPASS": 0, "DECOMPOSE": 0, "EXCISE": 0, "TRANSPOSE": 0}
    if not prim_log_text:
        return counts
    # Match table rows where the 'Primitive' column is one of BYP/DEC/EXC/TRP.
    for m in re.finditer(r"\|\s*(BYP|DEC|EXC|TRP)\b[^|]*\|", prim_log_text):
        code = m.group(1)
        if code == "BYP":  counts["BYPASS"]    += 1
        if code == "DEC":  counts["DECOMPOSE"] += 1
        if code == "EXC":  counts["EXCISE"]    += 1
        if code == "TRP":  counts["TRANSPOSE"] += 1
    return counts

def _count_verdicts(compl_map_text: str) -> dict[str, int]:
    """Heuristic count over | ... | cells of P / Pa / O / S verdict tokens."""
    counts = {"PROVED": 0, "PARTIAL": 0, "OPEN_BUT_ADDRESSED": 0, "SILENT": 0}
    if not compl_map_text:
        return counts
    # Restrict to the table rows: lines starting with '|' and containing token.
    for line in compl_map_text.splitlines():
        if not line.startswith("|"):
            continue
        # Each cell is between |...|.  We look at first-token of cell content.
        for cell in line.split("|")[1:-1]:
            token = cell.strip().split()[0:1]
            if not token:
                continue
            t = token[0].rstrip(".,;:()*")
            if t == "P":   counts["PROVED"]              += 1
            elif t == "Pa":counts["PARTIAL"]             += 1
            elif t == "O": counts["OPEN_BUT_ADDRESSED"]  += 1
            elif t == "S": counts["SILENT"]              += 1
    return counts

def _extract_acknowledgments(landscape_text: str) -> list[str]:
    """Pull author names from a landscape file's Acknowledgment Suggestions."""
    if not landscape_text:
        return []
    # Find a section with 'Acknowledgment'.
    m = re.search(r"##\s*[^\n]*Acknowledgment[^\n]*\n([\s\S]+?)(?:\n##\s|\Z)",
                  landscape_text, re.IGNORECASE)
    if not m:
        return []
    block = m.group(1)
    names: list[str] = []
    for line in block.splitlines():
        line = line.strip()
        if line.startswith(("- ", "* ")):
            entry = line[2:].split(" — ")[0].split(" - ")[0].split(":")[0]
            entry = entry.strip("*_ ")
            if 3 < len(entry) < 80:
                names.append(entry)
    # de-dup preserving order
    seen = set()
    out = []
    for n in names:
        if n not in seen:
            seen.add(n)
            out.append(n)
    return out[:12]

def _extract_main_theorem(comply_text: str) -> str:
    """Grab the first Theorem statement from the comply-bare deliverable."""
    if not comply_text:
        return ""
    m = re.search(r"\*\*(Theorem [0-9.]+\s*\([^)]+\))\.\*\*\s*\*([^*]{20,400})", comply_text)
    if m:
        return f"{m.group(1)} {m.group(2).strip()}"[:400]
    # Fallback: any first bold heading in §2.
    m = re.search(r"##\s*§?2[^\n]*\n+([\s\S]{40,400}?)(?:\n##\s|\n\n\*Proof|$)", comply_text)
    if m:
        return re.sub(r"\s+", " ", m.group(1)).strip()[:400]
    return ""

# ---------------------------------------------------------------------------
# Per-vertex extractor
# ---------------------------------------------------------------------------

def find_deliverable(vertex_dir: Path, vertex_key: str, suffix: str) -> Path | None:
    """Look for a deliverable file under <vertex_dir>/deliverables/.

    suffix in {'comply', 'independence', 'harden', 'beyond'}.
    Tries the canonical name first, then the legacy 'clay' alias for comply.
    """
    deliv_dir = vertex_dir / "deliverables"
    if not deliv_dir.exists():
        return None
    candidates = [
        f"{vertex_key}-{suffix}-bare.md",
        f"{vertex_key}-{suffix}-math.md",
    ]
    if suffix == "comply":
        # Legacy: ym-clay-bare.md
        candidates.append(f"{vertex_key}-clay-bare.md")
    if suffix == "independence":
        candidates.append(f"{vertex_key}-independent-bare.md")
    if suffix == "harden":
        candidates.append(f"{vertex_key}-contribute-bare.md")
    for name in candidates:
        p = deliv_dir / name
        if p.exists():
            return p
    return None


def find_pac_run(vertex_dir: Path, run: str, name: str) -> Path | None:
    p = vertex_dir / "pac-output" / "runs" / run / name
    return p if p.exists() else None


def extract_vertex(vertex_key: str) -> dict[str, Any]:
    vertex_dir = STRATEGY / vertex_key
    record: dict[str, Any] = {
        "key": vertex_key,
        "name": DISPLAY_NAME.get(vertex_key, vertex_key.upper()),
        "is_millennium": vertex_key in MILL_VERTICES,
        "status": "AUDIT PENDING",
        "comply": {"present": False, "lines": 0, "theorems": 0, "sections": 0,
                   "layers": 0, "named_walls": [], "main_theorem": ""},
        "independent": {"present": False, "lines": 0, "theorems": 0, "sections": 0,
                        "primitives": {"BYPASS": 0, "DECOMPOSE": 0, "EXCISE": 0, "TRANSPOSE": 0},
                        "named_walls": []},
        "contribute": {"present": False, "lines": 0, "theorems": 0, "sections": 0,
                       "externals": [], "named_walls": []},
        "beyond": {"present": False, "lines": 0, "theorems": 0, "sections": 0},
        "compliance": {"PROVED": 0, "PARTIAL": 0, "OPEN_BUT_ADDRESSED": 0, "SILENT": 0},
        "acknowledgments": [],
    }

    if not vertex_dir.exists():
        log(f"  vertex dir missing: {vertex_key}")
        return record

    # Pillar A
    p = find_deliverable(vertex_dir, vertex_key, "comply")
    if p:
        text = safe_read(p)
        record["comply"] = {
            "present": True,
            "file": str(p.relative_to(ROOT)),
            "lines": len(text.splitlines()),
            "theorems": _count_theorems(text),
            "sections": _count_sections(text),
            "layers": _count_layers(text),
            "named_walls": _extract_named_walls(text),
            "main_theorem": _extract_main_theorem(text),
        }

    # Pillar B
    p = find_deliverable(vertex_dir, vertex_key, "independence")
    indep_text = ""
    if p:
        indep_text = safe_read(p)
        record["independent"] = {
            "present": True,
            "file": str(p.relative_to(ROOT)),
            "lines": len(indep_text.splitlines()),
            "theorems": _count_theorems(indep_text),
            "sections": _count_sections(indep_text),
            "primitives": {"BYPASS": 0, "DECOMPOSE": 0, "EXCISE": 0, "TRANSPOSE": 0},
            "named_walls": _extract_named_walls(indep_text),
        }

    # Pillar C
    p = find_deliverable(vertex_dir, vertex_key, "harden")
    harden_text = ""
    if p:
        harden_text = safe_read(p)
        record["contribute"] = {
            "present": True,
            "file": str(p.relative_to(ROOT)),
            "lines": len(harden_text.splitlines()),
            "theorems": _count_theorems(harden_text),
            "sections": _count_sections(harden_text),
            "externals": [],
            "named_walls": _extract_named_walls(harden_text),
        }

    # Beyond
    p = find_deliverable(vertex_dir, vertex_key, "beyond")
    if p:
        text = safe_read(p)
        record["beyond"] = {
            "present": True,
            "file": str(p.relative_to(ROOT)),
            "lines": len(text.splitlines()),
            "theorems": _count_theorems(text),
            "sections": _count_sections(text),
        }

    # PAC primitive counts (run-05)
    prim = find_pac_run(vertex_dir, "run-05", "primitive-log.md")
    if prim:
        prim_text = safe_read(prim)
        record["independent"]["primitives"] = _count_primitives(prim_text)

    # Compliance map verdicts (run-02)
    cmap = find_pac_run(vertex_dir, "run-02", "compliance-map.md")
    if cmap:
        record["compliance"] = _count_verdicts(safe_read(cmap))

    # Externals from commit-memo run-06 + harden-bare table parse
    commit = find_pac_run(vertex_dir, "run-06", "commit-memo.md")
    commit_text = safe_read(commit) if commit else ""
    if record["contribute"]["present"]:
        record["contribute"]["externals"] = _extract_externals(harden_text, commit_text)

    # Landscape acknowledgments
    landscape = STRATEGY / "_research" / vertex_key / "landscape.md"
    if landscape.exists():
        record["acknowledgments"] = _extract_acknowledgments(safe_read(landscape))

    # Status flag
    full = (record["comply"]["present"] and record["independent"]["present"]
            and record["contribute"]["present"] and record["beyond"]["present"])
    if full:
        record["status"] = "FULL"
    elif record["comply"]["present"] or record["independent"]["present"] or record["contribute"]["present"]:
        record["status"] = "PARTIAL"
    else:
        record["status"] = "AUDIT PENDING"

    return record

# ---------------------------------------------------------------------------
# Edges
# ---------------------------------------------------------------------------

def parse_cross_cut_edges() -> list[dict[str, Any]]:
    path = STRATEGY / "x-ray" / "pac-output" / "runs" / "run-01" / "cross-cut-edges.md"
    if not path.exists():
        log(f"cross-cut-edges.md not found at {path}")
        return []
    text = safe_read(path)
    edges: list[dict[str, Any]] = []
    # Lines look like:
    # - ym:L1 ↔ qg5d:Branch B — shared spectral gap — paper61 §08 ...
    line_re = re.compile(
        r"^- ([a-z0-9_-]+):([A-Za-z0-9_./ -]+?)\s*↔\s*([a-z0-9_-]+):?([A-Za-z0-9_./ -]*?)\s*[—–-]\s*([^—–-]+?)\s*[—–-]\s*(.+)$"
    )
    section_status = "verified"
    for raw in text.splitlines():
        line = raw.rstrip()
        ls = line.lstrip()
        if ls.startswith("###"):
            if "Verified" in ls:
                section_status = "verified"
            elif "Speculative" in ls:
                section_status = "speculative"
            continue
        if not line.startswith("- "):
            continue
        m = line_re.match(line)
        if not m:
            continue
        src, src_layer, dst, dst_layer, shared, reason = m.groups()
        edges.append({
            "src": src.strip().lower(),
            "src_layer": src_layer.strip(),
            "dst": dst.strip().lower(),
            "dst_layer": dst_layer.strip(),
            "shared": shared.strip(),
            "reason": reason.strip()[:240],
            "status": section_status,
        })
    return edges

# ---------------------------------------------------------------------------
# Ring layout
# ---------------------------------------------------------------------------

def assign_ring_positions(vertices: list[dict[str, Any]]) -> list[dict[str, Any]]:
    n = len(vertices)
    # Place each vertex at angle theta = 2*pi*i/n, with 12 o'clock = top (theta = -pi/2).
    for i, v in enumerate(vertices):
        theta = -math.pi / 2 + 2 * math.pi * i / n
        v["index"] = i
        v["theta"] = theta
        v["zone"] = ZONE_BY_INDEX.get(i, "EAST")
    return vertices

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    log(f"build.py starting at {_dt.datetime.now().isoformat(timespec='seconds')}")
    log(f"ROOT = {ROOT}")
    log(f"STRATEGY = {STRATEGY}")

    if not STRATEGY.exists():
        log(f"FATAL: strategy/ not found at {STRATEGY}")
        flush_log()
        raise SystemExit(1)

    vertices: list[dict[str, Any]] = []
    for key in RING_ORDER:
        log(f"extracting vertex: {key}")
        try:
            v = extract_vertex(key)
        except Exception as e:
            log(f"  EXC {key}: {e}")
            v = {
                "key": key, "name": DISPLAY_NAME.get(key, key.upper()),
                "is_millennium": key in MILL_VERTICES,
                "status": "ERROR",
                "comply": {"present": False}, "independent": {"present": False},
                "contribute": {"present": False}, "beyond": {"present": False},
                "compliance": {"PROVED":0,"PARTIAL":0,"OPEN_BUT_ADDRESSED":0,"SILENT":0},
                "acknowledgments": [],
            }
        vertices.append(v)
        log(f"  status: {v.get('status', '?')}")

    vertices = assign_ring_positions(vertices)

    log("parsing cross-cut edges")
    edges = parse_cross_cut_edges()
    log(f"  {len(edges)} edges")

    # Filter edges to only those whose endpoints are in our ring.
    keys = {v["key"] for v in vertices}
    # Some edges name vertices the ring lists differently (e.g., 'twin-primes'
    # vs 'twin'); accept either spelling.
    alias = {
        "twin": "twin-primes",
        "selberg-1/4": None,         # not in ring
        "selberg-1": None,
        "lehmer": "lehmer",
        "lindelof": "lindelof",
        "katz-sarnak": "katz-sarnak",
        "sato-tate": "sato-tate",
        "h6": "hilbert-6",
        "h12": "hilbert-12",
        "vp": "vp-vs-vnp",
        "bgs": "bgs-spectral-statistics",
        "baum-connes": "baum-connes",
        "bc": "baum-connes",
    }
    def normalize(k: str) -> str | None:
        k = k.strip().lower()
        if k in keys:
            return k
        if k in alias:
            return alias[k]
        return None
    kept_edges: list[dict[str, Any]] = []
    skipped = 0
    for e in edges:
        s = normalize(e["src"]); d = normalize(e["dst"])
        if not s or not d or s == d:
            skipped += 1
            continue
        e2 = dict(e)
        e2["src"] = s
        e2["dst"] = d
        kept_edges.append(e2)
    log(f"  kept {len(kept_edges)} edges, skipped {skipped}")

    # Aggregate stats
    counts = {
        "vertices": len(vertices),
        "fully_authored": sum(1 for v in vertices if v["status"] == "FULL"),
        "partially_authored": sum(1 for v in vertices if v["status"] == "PARTIAL"),
        "audit_pending": sum(1 for v in vertices if v["status"] == "AUDIT PENDING"),
        "edges": len(kept_edges),
    }
    log(f"summary: {counts}")

    data = {
        "generated_at": _dt.datetime.now().isoformat(timespec="seconds"),
        "generator": "visualization/contribution-graph/build.py",
        "vertices": vertices,
        "edges": kept_edges,
        "counts": counts,
        "legend": {
            "COMPLY":      "slate — what the prize requires (Pillar A)",
            "INDEPENDENT": "amber — we lifted (Pillar B, PAC primitives)",
            "CONTRIBUTE":  "cyan — we gave back to the field (Pillar C)",
            "BEYOND":      "violet — beyond-bonus (cross-Clay, fair attribution)",
        },
        "primitives": {
            "BYPASS":    "drop the unprovable; route around it",
            "DECOMPOSE": "split a partial into a proved conjunction",
            "EXCISE":    "remove an unnecessary external dependency",
            "TRANSPOSE": "move a cell into a verified capacitor cell",
        },
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(data, indent=2)
    OUT.write_text(
        "// Auto-generated by visualization/contribution-graph/build.py\n"
        f"// Generated {data['generated_at']}\n"
        "// Regenerate: python3 visualization/contribution-graph/build.py\n\n"
        f"const CONTRIBUTION_DATA = {payload};\n",
        encoding="utf-8",
    )
    log(f"wrote {OUT} ({OUT.stat().st_size} bytes)")

    flush_log()
    print(f"wrote {OUT}")
    print(f"wrote {LOG}")
    print(f"summary: {json.dumps(counts)}")


if __name__ == "__main__":
    main()
