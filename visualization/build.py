#!/usr/bin/env python3
"""build.py — Scan the QG5D programme and emit data.js for the visualization.

Walks `strategy/` and `paper*` directories; parses markdown for metrics;
writes a global `SHAPE_DATA` JS constant consumed by app.js under file://.

Usage:
    python3 visualization/build.py

Output:
    visualization/data.js        (generated)
    visualization/build.log      (generated)

No external deps — Python 3 stdlib only.
"""
from __future__ import annotations

import datetime as _dt
import json
import os
import re
import sys
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "visualization" / "data.js"
LOG = ROOT / "visualization" / "build.log"

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
_LOG_LINES: list[str] = []

def log(msg: str) -> None:
    _LOG_LINES.append(msg)

def flush_log() -> None:
    LOG.write_text("\n".join(_LOG_LINES) + "\n", encoding="utf-8")

# ---------------------------------------------------------------------------
# Parse helpers (robust — return defaults on missing, never raise)
# ---------------------------------------------------------------------------
def safe_read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except FileNotFoundError:
        log(f"MISS: {path.relative_to(ROOT)}")
        return ""
    except Exception as e:
        log(f"ERR  {path}: {e}")
        return ""

def count_lines(path: Path) -> int:
    txt = safe_read(path)
    if not txt:
        return 0
    return txt.count("\n") + (1 if txt and not txt.endswith("\n") else 0)

def count_theorems(path: Path) -> int:
    txt = safe_read(path)
    if not txt:
        return 0
    # Count '**Theorem N.M' or '**Theorem N' as a canonical counter.
    return len(re.findall(r"\*\*Theorem\s+\d+", txt))

def count_definitions(path: Path) -> int:
    txt = safe_read(path)
    if not txt:
        return 0
    return len(re.findall(r"\*\*Definition\s+\d+", txt))

def _clean_md(p: str, max_chars: int) -> str:
    p = re.sub(r"\*\*([^*]+)\*\*", r"\1", p)
    p = re.sub(r"\*([^*]+)\*", r"\1", p)
    p = re.sub(r"`([^`]+)`", r"\1", p)
    p = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", p)
    p = re.sub(r"\$([^$]+)\$", r"\1", p)
    p = re.sub(r"\s+", " ", p).strip()
    if len(p) > max_chars:
        p = p[: max_chars - 1].rsplit(" ", 1)[0] + "…"
    return p

def extract_first_paragraph(path: Path, max_chars: int = 600) -> str:
    """Return the first human-readable paragraph from a markdown file.

    Strategy: walk paragraphs, skip the H1 title, skip horizontal rules,
    tables, code blocks, lists, blockquotes and very-short lines (like the
    "Status: ..." metadata). An italic-wrapped paragraph is acceptable if
    it is substantial.
    """
    txt = safe_read(path)
    if not txt:
        return ""
    paragraphs = re.split(r"\n\s*\n", txt)
    for para in paragraphs:
        p = para.strip()
        if not p:
            continue
        if p.startswith("#"):
            continue
        if p.startswith(">"):
            continue
        if re.fullmatch(r"[-=_\s]+", p):
            continue
        if p.startswith("|") or p.startswith("```"):
            continue
        if p.startswith("- ") or p.startswith("* ") or re.match(r"^\d+\.\s", p):
            continue
        # Strip enclosing italic markers *...* if this is a single paragraph
        # that is entirely italic (common subtitle form).
        if p.startswith("*") and p.endswith("*") and p.count("*") == 2:
            p = p[1:-1].strip()
        cleaned = _clean_md(p, max_chars)
        # Skip lines like "Status: ..." or author tags
        if len(cleaned) < 60:
            continue
        if cleaned.lower().startswith("status"):
            continue
        if cleaned.lower().startswith("g six") or "author" in cleaned.lower()[:20]:
            continue
        return cleaned
    return ""

def find_latest_run(pac_runs_dir: Path) -> Path | None:
    """Return the run-NN directory with the highest NN (only if it contains
    a compliance-map.md). Otherwise try any run with one.
    """
    if not pac_runs_dir.exists():
        return None
    candidates = []
    for child in pac_runs_dir.iterdir():
        if not child.is_dir():
            continue
        m = re.match(r"run-(\d+)", child.name)
        if not m:
            continue
        if (child / "compliance-map.md").exists():
            candidates.append((int(m.group(1)), child))
    if not candidates:
        # Fall back to highest-numbered run, even without compliance-map.md,
        # just to confirm a run exists.
        for child in pac_runs_dir.iterdir():
            m = re.match(r"run-(\d+)", child.name)
            if m:
                candidates.append((int(m.group(1)), child))
    if not candidates:
        return None
    candidates.sort(key=lambda t: t[0], reverse=True)
    return candidates[0][1]

def parse_compliance_distribution(md_path: Path) -> dict[str, Any]:
    """Extract the aggregate verdict counts from the compliance-map.md.

    Looks for the TOTAL row in the distribution table (§2), e.g.:
        | **TOTAL (140 cells)** | **23** | **43** | **1** | **73** | 140 |
    """
    txt = safe_read(md_path)
    if not txt:
        return {}
    # Try final distribution table first (exact counts post recount).
    # Match a row containing "TOTAL" with 5 bold integer cells.
    pattern = re.compile(
        r"\*\*TOTAL[^|]*\*\*\s*\|\s*\*\*(\d+)\*\*\s*\|\s*"
        r"\*\*(\d+)\*\*\s*\|\s*\*\*(\d+)\*\*\s*\|\s*\*\*(\d+)\*\*\s*\|\s*(\d+)"
    )
    matches = list(pattern.finditer(txt))
    if matches:
        m = matches[-1]  # take last (post-recount) occurrence
        p, pa, o, s, total = (int(x) for x in m.groups())
        return {
            "PROVED": p,
            "PARTIAL": pa,
            "OPEN-BUT-ADDRESSED": o,
            "SILENT": s,
            "total": total,
        }
    # Fallback: sum the per-requirement rows of §2, ignoring Pa/Pa etc.
    return {}

def parse_matrix_size(md_path: Path) -> tuple[int, int]:
    """Return (M, N) for 'M × N' or 'M rows × N columns' or 'NxN cells'.
    Looks for patterns like '20 layers × 7 requirements' or '20 × 7 = 140 cells'.
    """
    txt = safe_read(md_path)
    if not txt:
        return (0, 0)
    m = re.search(r"(\d+)\s*(?:rows|layers)?\s*[×x]\s*(\d+)\s*(?:columns|requirements|cells)?",
                  txt, flags=re.IGNORECASE)
    if m:
        return (int(m.group(1)), int(m.group(2)))
    return (0, 0)

def parse_face_histogram(x_ray_path: Path) -> dict[str, int]:
    """Extract the face histogram from §5 of an X-RAY.md."""
    txt = safe_read(x_ray_path)
    if not txt:
        return {}
    section = re.search(r"##\s*§5[^#]+", txt)
    if not section:
        return {}
    sect_text = section.group(0)
    faces = ["TOPOLOGY", "DYNAMICS", "HARMONICS", "MEASURE", "AMPLITUDE",
             "SYMMETRY", "CURVATURE", "ARITHMETIC", "RESONANCE", "SPREAD"]
    hist = {}
    for face in faces:
        # | FACE       |   N   | ...
        m = re.search(rf"\|\s*{face}\s*\|\s*(\d+)\s*\|", sect_text)
        if m:
            hist[face] = int(m.group(1))
        else:
            hist[face] = 0
    return hist

def parse_projection_histogram(x_ray_path: Path) -> dict[str, int]:
    """Extract the projection histogram from §6 of an X-RAY.md."""
    txt = safe_read(x_ray_path)
    if not txt:
        return {}
    section = re.search(r"##\s*§6[^#]+", txt)
    if not section:
        return {}
    sect_text = section.group(0)
    projs = ["P_A", "P_B", "P_C", "P_D", "P_E", "P_O"]
    hist = {}
    for pr in projs:
        # Some tables use "$P_A$" with dollar signs. Handle both.
        m = re.search(
            rf"\|\s*\$?{re.escape(pr)}\$?\s*\|\s*(\d+)\s*\|",
            sect_text,
        )
        if m:
            hist[pr] = int(m.group(1))
        else:
            hist[pr] = 0
    return hist

def parse_cross_cut_count(x_ray_path: Path) -> int:
    """Pull the summary cross-cut edge count from an X-RAY.md."""
    txt = safe_read(x_ray_path)
    if not txt:
        return 0
    m = re.search(r"(\d+)\s+cross-cut\s+edges", txt, flags=re.IGNORECASE)
    if m:
        return int(m.group(1))
    return 0

def parse_primary_assignments(x_ray_path: Path) -> dict[str, str]:
    """Parse 'Primary face', 'Primary projection', 'Primary branch' from header."""
    txt = safe_read(x_ray_path)
    if not txt:
        return {}
    out: dict[str, str] = {}
    for key, field in [
        ("face", r"\*\*Primary face\*\*[:\s]*([^(\n.]+)"),
        ("projection", r"\*\*Primary projection\*\*[:\s]*(\$?[A-Z_]+\$?)"),
        ("branch", r"\*\*Primary branch[^*]*\*\*[:\s]*([A-E])"),
    ]:
        m = re.search(field, txt)
        if m:
            out[key] = m.group(1).strip().strip("*")
    return out

def parse_named_walls(strategy_md: Path) -> list[dict[str, str]]:
    """Extract named-walls entries from a 00-millenium-strategy.md.

    Best-effort: look for bullet or table lines that mention a W-label
    or "Named wall" or "OPEN-BUT-ADDRESSED" status.
    """
    txt = safe_read(strategy_md)
    if not txt:
        return []
    walls: list[dict[str, str]] = []
    # Pattern 1: lines like '- **W1 — H4**: ... Status: **OPEN-...**'
    for m in re.finditer(
        r"\*\*(W\d+[^*]*)\*\*[^\n]*",
        txt,
    ):
        label = m.group(1).strip()
        tail = m.group(0)
        status = ""
        for st in ["OPEN-BUT-ADDRESSED", "OPEN", "BYPASSED", "PROVED"]:
            if st in tail.upper():
                status = st
                break
        walls.append({"name": label, "status": status, "bypass": ""})
        if len(walls) >= 10:
            break
    return walls

def parse_n_requirements(strategy_md: Path) -> tuple[int, list[str]]:
    """Return the count + short list of the N requirements section."""
    txt = safe_read(strategy_md)
    if not txt:
        return (0, [])
    # Find "## §3 The N ... requirements"
    m = re.search(r"##\s*§3\s+[^#]+", txt)
    if not m:
        return (0, [])
    sect = m.group(0)
    items: list[str] = []
    for line in sect.splitlines():
        line = line.strip()
        # Match '1. **Foo** — bar' or '1. Foo: bar'
        mi = re.match(r"^(\d+)\.\s*\*\*([^*]+)\*\*", line)
        if mi:
            items.append(mi.group(2).strip())
            continue
        mi = re.match(r"^(\d+)\.\s*([^—:]+)[—:]", line)
        if mi:
            items.append(mi.group(2).strip())
    # de-duplicate in order
    seen: set[str] = set()
    uniq: list[str] = []
    for it in items:
        if it.lower() in seen:
            continue
        seen.add(it.lower())
        uniq.append(it)
    return (len(uniq), uniq)

def parse_source_type(strategy_md: Path) -> str:
    """Return 'Clay-Official' / 'Community-Standard' / 'Framework-Claim' etc.

    Heuristic: look for the phrase or for Clay-specific language in §1.
    """
    txt = safe_read(strategy_md).lower()
    if not txt:
        return ""
    if "clay" in txt[:3000] and "prize" in txt[:3000]:
        return "Clay-Official"
    if "community" in txt[:3000]:
        return "Community-Standard"
    if "framework" in txt[:3000] and ("pin" in txt[:3000] or "prediction" in txt[:3000]):
        return "Framework-Claim"
    return "Conjecture"

def count_proof_chain_layers(proof_chain_md: Path) -> int:
    """Count the number of layers/links in a PROOF-CHAIN.md.

    Looks for lines beginning with '| LN |' or 'L1:'-style entries or
    the first numeric column of a Markdown table.
    """
    txt = safe_read(proof_chain_md)
    if not txt:
        return 0
    # Find the table with the chain and count rows starting like '| 1 |' ... '| 18 |'
    rows = re.findall(r"^\|\s*(\d+)\s*\|", txt, flags=re.MULTILINE)
    # Alternative: count 'L\d+' layer labels
    ls = set(re.findall(r"\bL(\d+)\b", txt))
    return max(len(set(rows)), len(ls))

def parse_proof_chain_status(proof_chain_md: Path) -> str:
    """Grab the 'Status: ...' line."""
    txt = safe_read(proof_chain_md)
    if not txt:
        return ""
    m = re.search(r"Status[:\s]*\*{0,2}([^*\n|]+)", txt[:3000])
    if m:
        return m.group(1).strip().rstrip(".").strip()
    return ""

# ---------------------------------------------------------------------------
# Deep-dive extractors (for click-to-xray modal)
# ---------------------------------------------------------------------------
def parse_theorems_detailed(path: Path, max_items: int = 80) -> list[dict[str, str]]:
    """Extract every Theorem/Corollary/Lemma/Proposition from a bare.md.

    Returns a list of {number, kind, statement, citation} dicts. Statement
    is the first sentence (up to ~400 chars) of the theorem block.
    """
    txt = safe_read(path)
    if not txt:
        return []
    items: list[dict[str, str]] = []
    # Handle '**Theorem 2.1** (Name).' AND '### Theorem 2.1 (Name)' styles.
    pat = re.compile(
        r"(?:^|\n)(?:#{2,6}\s*)?\*{0,2}(Theorem|Corollary|Lemma|Proposition|Definition)\s+([A-Za-z0-9.]+)\*{0,2}"
        r"(?:\s*\(([^)]+)\))?[.\s]*([^\n]*(?:\n(?!\s*(?:#{1,6}\s*)?\*{0,2}(?:Theorem|Corollary|Lemma|Proposition|Definition)\s)[^\n]*){0,8})",
        flags=re.MULTILINE,
    )
    for m in pat.finditer(txt):
        kind = m.group(1)
        num = m.group(2).rstrip(".")
        name = (m.group(3) or "").strip()
        body = (m.group(4) or "").strip()
        # strip leading italics markers "*Statement.*" or "*"
        body = re.sub(r"^\*+\s*Statement\.?\s*\*+\s*", "", body, flags=re.I)
        body = re.sub(r"^Statement\.?\s*", "", body, flags=re.I)
        body = body.lstrip("*").lstrip()
        # take the first sentence (up to 400 chars)
        sentence = body.split(". ")[0].rstrip(".")
        if len(sentence) > 400:
            sentence = sentence[:400].rsplit(" ", 1)[0] + "…"
        sentence = _clean_md(sentence, 500)
        # remove stray leading asterisk
        sentence = sentence.lstrip("*").strip()
        items.append({
            "kind": kind,
            "number": num,
            "name": name,
            "statement": sentence,
        })
        if len(items) >= max_items:
            break
    return items

def parse_layers_from_proof_chain(path: Path) -> list[dict[str, str]]:
    """Parse the chain table rows from a PROOF-CHAIN.md.

    Return [{id, statement, status, depends}] for every row. Supports
    tables with variable column counts (some papers have 4, some have 6).
    """
    txt = safe_read(path)
    if not txt:
        return []
    layers: list[dict[str, str]] = []
    seen_ids: set[str] = set()
    for line in txt.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        # split on | and strip
        cells = [c.strip() for c in stripped.strip("|").split("|")]
        if len(cells) < 3:
            continue
        first = cells[0]
        # A layer-row has a short identifier in the first cell: digits or
        # things like '1b', 'S1', '3a', '10b', 'L1', etc.
        if not re.fullmatch(r"L?[\dSa-z]+(?:\.[0-9a-z]+)?", first):
            continue
        if len(first) > 6:
            continue
        # Skip header-ish rows like 'Link' or separator lines '---'
        if first.lower() in {"link", "layer", "l", "---"}:
            continue
        if set(first) <= {"-", "—"}:
            continue
        if first in seen_ids:
            continue
        statement = cells[1] if len(cells) > 1 else ""
        status = cells[2] if len(cells) > 2 else ""
        depends = cells[3] if len(cells) > 3 else ""
        # Truncate overlong statements
        statement = _clean_md(statement, 500)
        status = _clean_md(status, 120)
        depends = _clean_md(depends, 100)
        if not statement or statement == "Statement":
            continue
        layers.append({
            "id": first,
            "statement": statement,
            "status": status,
            "depends": depends,
        })
        seen_ids.add(first)
    return layers

def parse_layer_xray(xray_path: Path) -> list[dict[str, str]]:
    """Pull face/projection/pattern/invariant per layer from X-RAY.md §3.

    Parses the heading `### L1 — <title>` and the following metadata
    (Face, Projection, Pattern, Invariant, Status, Source).
    """
    txt = safe_read(xray_path)
    if not txt:
        return []
    # Carve out §3 (Layer-by-Layer X-Ray) up to the next §N header.
    m = re.search(r"##\s*§3\s+.*?(?=\n##\s*§\d|\Z)", txt, flags=re.DOTALL)
    if not m:
        return []
    sect = m.group(0)
    out: list[dict[str, str]] = []
    # Split on layer headings '### L1 — ...' / '### L1b — ...'
    parts = re.split(r"\n###\s+", sect)
    for part in parts[1:]:
        m0 = re.match(r"(L[0-9a-z_]+)\s*—\s*(.+?)\n", part)
        if not m0:
            # Try alternate: 'L_modular — ...' or just 'L1 ...'
            m0 = re.match(r"(L[\w_-]+)\s+(.+?)\n", part)
            if not m0:
                continue
        lid = m0.group(1)
        title = m0.group(2).strip()
        body = part[m0.end():]
        # Parse Face/Projection/Pattern/Status/Source
        face = _extract_kv(body, "Face")
        projection = _extract_kv(body, "Projection")
        pattern = _extract_kv(body, "Pattern")
        invariant = _extract_kv(body, "Invariant preserved") or _extract_kv(body, "Invariant")
        status = _extract_kv(body, "Status")
        source = _extract_kv(body, "Source")
        out.append({
            "id": lid,
            "title": _clean_md(title, 200),
            "face": _clean_md(face, 80),
            "projection": _clean_md(projection, 40),
            "pattern": _clean_md(pattern, 80),
            "invariant": _clean_md(invariant, 80),
            "status": _clean_md(status, 80),
            "source": _clean_md(source, 200),
        })
    return out

def _extract_kv(body: str, key: str) -> str:
    """Extract `- **Key**: value` or `**Key**: value` on a single line."""
    m = re.search(
        rf"^\s*-?\s*\*\*{re.escape(key)}\*\*\s*:\s*([^\n]+)",
        body, flags=re.MULTILINE,
    )
    if m:
        return m.group(1).strip()
    return ""

def parse_named_walls_detailed(strategy_md: Path, bare_md: Path | None = None) -> list[dict[str, str]]:
    """Extract full disclosure fields for each named wall.

    Looks in both strategy md (for overview) and the bare.md (for the
    DELTA-10 field table: Name, Location, Statement, Status, Bypass route,
    Confidence, Audit pending, Effects).
    """
    walls: list[dict[str, str]] = []
    # Try bare.md first — has the full DELTA-10 table
    if bare_md and bare_md.exists():
        txt = safe_read(bare_md)
        if txt:
            # Find every 'NAMED WALL W\d+' heading or tagged block
            # Match '### NAMED WALL W1 — H4' and then the adjacent table
            for m in re.finditer(
                r"(?:###\s*|#### W\d+\s*|### §15\.\d+\s*|W\d+\s+—\s*)NAMED\s+WALL\s+(W\d+)\s*—?\s*([^\n]*)",
                txt,
            ):
                w_name = m.group(1).strip()
                w_topic = m.group(2).strip().rstrip("—").strip()
                start = m.end()
                # Look for a | Field | Value | table in the next ~3000 chars
                block = txt[start:start+3000]
                fields = _parse_wall_fields(block)
                fields["name"] = w_name
                if w_topic:
                    fields["topic"] = w_topic
                walls.append(fields)
            # Alternative: detect `### §15.1 W1 — H4` style
            if not walls:
                for m in re.finditer(
                    r"###\s*§15\.\d+\s+(W\d+)\s*—\s*([^\n]*)",
                    txt,
                ):
                    w_name = m.group(1).strip()
                    w_topic = m.group(2).strip()
                    start = m.end()
                    block = txt[start:start+2000]
                    fields = _parse_wall_fields(block)
                    fields["name"] = w_name
                    fields["topic"] = w_topic
                    walls.append(fields)
    # Fallback to overview-level parsing from strategy md (if no bare walls)
    if not walls and strategy_md and strategy_md.exists():
        txt = safe_read(strategy_md)
        for m in re.finditer(
            r"\*\*(W\d+)(?:\s*[—-]\s*|\s+)([^*\n]{0,60})\*\*\s*\(?([^\)]*)?\)?",
            txt,
        ):
            w_name = m.group(1).strip()
            w_topic = m.group(2).strip() if m.group(2) else ""
            tail = txt[m.end():m.end()+400]
            status = ""
            for st in ["OPEN-BUT-ADDRESSED", "BYPASSED", "PROVED", "OPEN", "CLOSED"]:
                if st in tail.upper():
                    status = st
                    break
            walls.append({
                "name": w_name,
                "topic": w_topic,
                "status": status,
            })
            if len(walls) >= 10:
                break
    return walls

def _parse_wall_fields(block: str) -> dict[str, str]:
    """Parse a DELTA-10 table | Field | Value | from a wall block."""
    fields: dict[str, str] = {}
    for line in block.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 2:
            continue
        k = cells[0].strip("* ").lower()
        v = cells[1].strip()
        if not k or k in {"field", "---", "—"}:
            continue
        if set(k) <= {"-", "—", " "}:
            continue
        if k in {"name", "location in chain", "location in programme", "statement",
                 "status", "bypass route", "bypass citation", "aggregate confidence",
                 "audit pending", "effect if l.3.7 passes", "effect if l.3.7 fails",
                 "independent standing"}:
            # Normalize key
            short = {
                "location in chain": "chain_location",
                "location in programme": "programme_location",
                "bypass route": "bypass",
                "bypass citation": "bypass_citation",
                "aggregate confidence": "confidence",
                "audit pending": "audit_pending",
                "effect if l.3.7 passes": "effect_pass",
                "effect if l.3.7 fails": "effect_fail",
                "independent standing": "independent_standing",
            }.get(k, k)
            fields[short] = _clean_md(v, 500)
    return fields

def parse_cross_cuts_for_vertex(vertex: str) -> list[dict[str, str]]:
    """Filter cross-cut-edges.md for edges mentioning this vertex."""
    cross_cut_md = ROOT / "strategy" / "x-ray" / "pac-output" / "runs" / "run-01" / "cross-cut-edges.md"
    txt = safe_read(cross_cut_md)
    if not txt:
        return []
    edges: list[dict[str, str]] = []
    for line in txt.splitlines():
        if not line.lstrip().startswith("-"):
            continue
        # Match '- ym:L1 ↔ qg5d:Branch B — shared <invariant> — <reason>'
        # Also handle cases with no reason.
        m = re.match(
            r"^\s*-\s*([\w\-/]+):([\w_\s]+?)\s*↔\s*([\w\-/]+)(?::([\w_\s]+?))?\s*—\s*(?:shared|face-only)\s+([^—]+?)(?:\s*—\s*(.+))?$",
            line,
        )
        if not m:
            continue
        a = m.group(1).strip()
        a_layer = m.group(2).strip()
        b = m.group(3).strip()
        b_layer = (m.group(4) or "").strip()
        shared = m.group(5).strip()
        reason = (m.group(6) or "").strip()
        if a != vertex and b != vertex:
            continue
        edges.append({
            "from": a,
            "from_layer": a_layer,
            "to": b,
            "to_layer": b_layer,
            "shared": shared,
            "reason": reason,
        })
    return edges

def parse_all_cross_cuts() -> list[dict[str, str]]:
    """Return every cross-cut edge from the run-01 file."""
    cross_cut_md = ROOT / "strategy" / "x-ray" / "pac-output" / "runs" / "run-01" / "cross-cut-edges.md"
    txt = safe_read(cross_cut_md)
    if not txt:
        return []
    edges: list[dict[str, str]] = []
    for line in txt.splitlines():
        if not line.lstrip().startswith("-"):
            continue
        m = re.match(
            r"^\s*-\s*([\w\-/]+):([\w_\s]+?)\s*↔\s*([\w\-/]+)(?::([\w_\s]+?))?\s*—\s*(?:shared|face-only)\s+([^—]+?)(?:\s*—\s*(.+))?$",
            line,
        )
        if not m:
            continue
        edges.append({
            "from": m.group(1).strip(),
            "from_layer": m.group(2).strip(),
            "to": m.group(3).strip(),
            "to_layer": (m.group(4) or "").strip(),
            "shared": m.group(5).strip(),
            "reason": (m.group(6) or "").strip(),
        })
    return edges

def parse_numbers_table(bare_md: Path) -> list[dict[str, str]]:
    """Extract the Numbers Table (§16) from a bare.md."""
    txt = safe_read(bare_md)
    if not txt:
        return []
    # Find '## §N Numbers Table' header then read up to the next '## ' header
    m = re.search(r"(?:^|\n)##\s*§?\s*\d*\s*Numbers?\s+Table[^\n]*\n(.*?)(?=\n##\s|\Z)",
                  txt, flags=re.DOTALL | re.IGNORECASE)
    if not m:
        return []
    sect = m.group(1)
    rows: list[dict[str, str]] = []
    for line in sect.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 3:
            continue
        if cells[0] in {"#", "---", ""} or re.fullmatch(r"-+", cells[0]):
            continue
        # Skip header row
        if cells[0].lower() in {"#", "num"}:
            continue
        # Skip separator
        if all(re.fullmatch(r"-+|:-+:?|-+:", c) for c in cells):
            continue
        idx = cells[0]
        if not re.match(r"^\d+[a-z]?$", idx):
            continue
        quantity = _clean_md(cells[1] if len(cells) > 1 else "", 250)
        value = _clean_md(cells[2] if len(cells) > 2 else "", 250)
        citation = _clean_md(cells[3] if len(cells) > 3 else "", 250)
        rows.append({
            "n": idx,
            "quantity": quantity,
            "value": value,
            "citation": citation,
        })
    return rows

def parse_n_requirements_detailed(strategy_md: Path) -> list[dict[str, str]]:
    """Return the full §3 N requirements with descriptions."""
    txt = safe_read(strategy_md)
    if not txt:
        return []
    m = re.search(r"##\s*§3[^#]+", txt)
    if not m:
        return []
    sect = m.group(0)
    items: list[dict[str, str]] = []
    seen = set()
    for line in sect.splitlines():
        stripped = line.strip()
        mi = re.match(r"^(\d+)\.\s*\*\*([^*]+)\*\*\s*(?:—|:)?\s*(.*)$", stripped)
        if not mi:
            mi = re.match(r"^(\d+)\.\s*([^—:]+)[—:]\s*(.*)$", stripped)
        if mi:
            n = mi.group(1).strip()
            label = mi.group(2).strip()
            desc = mi.group(3).strip() if mi.lastindex and mi.lastindex >= 3 else ""
            key = (n, label.lower())
            if key in seen:
                continue
            seen.add(key)
            items.append({
                "n": n,
                "label": _clean_md(label, 100),
                "description": _clean_md(desc, 300),
            })
    return items

def parse_bonus_theorems(beyond_bare: Path, max_items: int = 40) -> list[dict[str, str]]:
    """Theorems from *-beyond-bare.md (bonus content)."""
    return parse_theorems_detailed(beyond_bare, max_items=max_items)

# ---------------------------------------------------------------------------
# Artifact reader (for mode-toggle buttons)
# ---------------------------------------------------------------------------
def read_artifact(path: Path, max_chars: int = 120000) -> dict[str, Any] | None:
    """Read a markdown artifact for inline modal display.

    Returns {path, size, lines, content} or None if missing.
    Content is truncated at max_chars with a trailing marker.
    """
    if not path.exists():
        return None
    txt = safe_read(path)
    if not txt:
        return None
    size = len(txt)
    lines = txt.count("\n") + 1
    if len(txt) > max_chars:
        txt = txt[:max_chars] + f"\n\n… [truncated; full file: {size} chars]"
    return {
        "path": str(path.relative_to(ROOT)),
        "size": size,
        "lines": lines,
        "content": txt,
    }

# ---------------------------------------------------------------------------
# Progress ladder (13 rungs)
# ---------------------------------------------------------------------------
LADDER_NAMES = [
    "Strategy exists",
    "Brief exists",
    "X-Ray done",
    "Compliance locked",
    "Bare locked",
    "Full composed",
    "Full locked",
    "Zenodo published",
    "arXiv published",
    "Journal published",
    "Community accepted",
    "PROVED",
    "UNIVERSALLY PROVED",
]

def compute_ladder(vertex: str, paper_dir: str,
                   strategy_dirname: str | None) -> tuple[list[bool], dict[str, str]]:
    """Compute the 13-rung ladder state for a vertex.

    Returns (ladder, detection_files). detection_files maps each reached
    rung's 1-based index (as string) to the file path that triggered it.
    """
    rungs = [False] * 13
    det: dict[str, str] = {}
    if not strategy_dirname:
        # no bundle; still check PROOF-CHAIN.md OPEN-walls for rung 12
        pc = ROOT / paper_dir / "PROOF-CHAIN.md"
        if pc.exists():
            txt = safe_read(pc)
            has_open_wall = bool(re.search(r"\b(OPEN-BUT-ADDRESSED|\bOPEN\b)", txt or ""))
            if txt and not has_open_wall:
                # if the chain claims completed (all PROVED/QED), rung 12 ON
                # conservative: only if text mentions '/N PROVED' with N == N
                pass
        return rungs, det
    strat_dir = ROOT / "strategy" / strategy_dirname
    # Rung 1: strategy file
    for candidate in ("00-millenium-strategy.md", "00-audit-strategy.md"):
        p = strat_dir / candidate
        if p.exists():
            rungs[0] = True
            det["1"] = str(p.relative_to(ROOT))
            break
    # Rung 2: brief file
    for candidate in [f"{vertex}-millenium-brief.md", f"{vertex}-audit-brief.md",
                      f"{strategy_dirname}-millenium-brief.md"]:
        p = strat_dir / candidate
        if p.exists():
            rungs[1] = True
            det["2"] = str(p.relative_to(ROOT))
            break
    # Rung 3: X-Ray
    xr = ROOT / "strategy" / "x-ray" / "proof-chain" / vertex / "X-RAY.md"
    if xr.exists():
        rungs[2] = True
        det["3"] = str(xr.relative_to(ROOT))
    # Rung 4: Compliance locked = any commit-memo.md with LOCKED
    runs_dir = strat_dir / "pac-output" / "runs"
    locked_run = None
    if runs_dir.exists():
        for child in sorted(runs_dir.iterdir()):
            cm = child / "commit-memo.md"
            if cm.exists():
                cm_txt = safe_read(cm)
                if "LOCKED" in cm_txt:
                    locked_run = cm
                    break
    if locked_run is not None:
        rungs[3] = True
        det["4"] = str(locked_run.relative_to(ROOT))
    # Rung 5: both -bare.md and -beyond-bare.md
    deliv = strat_dir / "deliverables"
    bare_path = None
    beyond_path = None
    if deliv.exists():
        for f in deliv.iterdir():
            n = f.name
            if n.endswith("-bare.md") and not n.endswith("-beyond-bare.md"):
                bare_path = f
            if n.endswith("-beyond-bare.md"):
                beyond_path = f
    if bare_path and beyond_path:
        rungs[4] = True
        det["5"] = str(bare_path.relative_to(ROOT))
    # Rung 6: full composed = -full.md or -beyond-full.md exists
    full_path = None
    if deliv.exists():
        for f in deliv.iterdir():
            n = f.name
            if n.endswith("-full.md") or n.endswith("-beyond-full.md"):
                full_path = f
                break
    if full_path is not None:
        rungs[5] = True
        det["6"] = str(full_path.relative_to(ROOT))
    # Rung 7: full locked = full composed + PUBLISH-READY in any commit-memo
    if full_path is not None and runs_dir.exists():
        for child in sorted(runs_dir.iterdir()):
            cm = child / "commit-memo.md"
            if cm.exists():
                cm_txt = safe_read(cm)
                if "PUBLISH-READY" in cm_txt:
                    rungs[6] = True
                    det["7"] = str(cm.relative_to(ROOT))
                    break
    # Rung 8/9/10/11: future placeholders — detect manifest files if any
    # (none today; left as always false)
    zenodo = strat_dir / "zenodo-manifest.md"
    if zenodo.exists():
        rungs[7] = True
        det["8"] = str(zenodo.relative_to(ROOT))
    arxiv = strat_dir / "arxiv-manifest.md"
    if arxiv.exists():
        rungs[8] = True
        det["9"] = str(arxiv.relative_to(ROOT))
    journal = strat_dir / "journal-manifest.md"
    if journal.exists():
        rungs[9] = True
        det["10"] = str(journal.relative_to(ROOT))
    accepted = strat_dir / "community-accepted.md"
    if accepted.exists():
        rungs[10] = True
        det["11"] = str(accepted.relative_to(ROOT))
    # Rung 12: PROVED = no OPEN tags in live PROOF-CHAIN
    pc = ROOT / paper_dir / "PROOF-CHAIN.md"
    if pc.exists():
        txt = safe_read(pc)
        # Consider PROVED if no OPEN/OPEN-BUT-ADDRESSED and no CONDITIONAL
        open_count = len(re.findall(r"\bOPEN(?:-BUT-ADDRESSED)?\b", txt))
        cond_count = len(re.findall(r"\bCONDITIONAL\b", txt))
        if txt and open_count == 0 and cond_count == 0:
            rungs[11] = True
            det["12"] = str(pc.relative_to(ROOT))
    # Rung 13: UNIVERSALLY PROVED — future, always false today
    return rungs, det

# ---------------------------------------------------------------------------
# Ring-vertex bundle extractor
# ---------------------------------------------------------------------------
RING_VERTEX_DIRS = {
    "ym": ("ym", "paper08-yang-mills"),
    "rh": ("rh", "paper13-rh"),
    "bsd": ("bsd", "paper26-bsd"),
    "ns": ("ns", "paper30-navier-stokes"),
    "hodge": ("hodge", "paper29-hodge"),
    "pvnp": ("pvnp", "paper28-pvnp"),
}

def extract_ring_vertex(vertex_key: str, paper_dir: str,
                        strategy_dirname: str | None = None) -> dict[str, Any]:
    """Pull all ring-vertex data for the given vertex key.

    `strategy_dirname` — the folder under `strategy/` (e.g. 'ym'); may be None
    if no bundle exists for this vertex yet (then we do graceful fallback).
    """
    d: dict[str, Any] = {"paper": paper_dir}
    paper_dir_path = ROOT / paper_dir

    bare_path: Path | None = None
    beyond_path: Path | None = None
    strat_md_used: Path | None = None
    full_path: Path | None = None

    # 1) PROOF-CHAIN.md on the paper itself
    pc = paper_dir_path / "PROOF-CHAIN.md"
    if pc.exists():
        d["proofChainStatus"] = parse_proof_chain_status(pc)
        d["proofChainLayers"] = count_proof_chain_layers(pc)
        d["proofChainDescription"] = extract_first_paragraph(pc, max_chars=500)
        d["proofChainPath"] = str(pc.relative_to(ROOT))
        d["chainLayers"] = parse_layers_from_proof_chain(pc)

    # 2) Strategy bundle (may not exist for most vertices)
    bundle_name = strategy_dirname
    if bundle_name and (ROOT / "strategy" / bundle_name).exists():
        strat_dir = ROOT / "strategy" / bundle_name
        d["strategyDir"] = f"strategy/{bundle_name}"

        # millennium strategy file
        for candidate in ("00-millenium-strategy.md", "00-audit-strategy.md"):
            strat_md = strat_dir / candidate
            if strat_md.exists():
                strat_md_used = strat_md
                d["sourceType"] = parse_source_type(strat_md)
                n_count, n_items = parse_n_requirements(strat_md)
                d["nRequirements"] = n_count
                d["nItems"] = n_items[:10]  # short form for existing UI
                d["requirementsDetailed"] = parse_n_requirements_detailed(strat_md)
                break

        # pac-output/runs/run-NN compliance map
        latest_run = find_latest_run(strat_dir / "pac-output" / "runs")
        if latest_run is not None:
            d["latestRun"] = latest_run.name
            cm = latest_run / "compliance-map.md"
            if cm.exists():
                d["verdictDist"] = parse_compliance_distribution(cm)
                mm, nn = parse_matrix_size(cm)
                if mm and nn:
                    d["matrixM"] = mm
                    d["matrixN"] = nn

        # deliverables
        deliv = strat_dir / "deliverables"
        if deliv.exists():
            for fname in deliv.iterdir():
                n = fname.name
                if n.endswith("-beyond-bare.md"):
                    beyond_path = fname
                    d["beyondLineCount"] = count_lines(fname)
                    d["beyondTheoremCount"] = count_theorems(fname)
                elif n.endswith("-bare.md") or n.endswith("-clay-bare.md"):
                    bare_path = fname
                    d["bareLineCount"] = count_lines(fname)
                    d["bareTheoremCount"] = count_theorems(fname)
                    d["bareDefinitionCount"] = count_definitions(fname)
                if n.endswith("-full.md") or n.endswith("-beyond-full.md"):
                    full_path = fname

    # Parse walls (bare.md has the DELTA-10 table; strategy md is fallback)
    d["namedWalls"] = parse_named_walls_detailed(
        strat_md_used if strat_md_used else (paper_dir_path / "PROOF-CHAIN.md"),
        bare_path,
    )

    # Bare deep-dives
    if bare_path is not None:
        d["barePath"] = str(bare_path.relative_to(ROOT))
        d["theoremsDetailed"] = parse_theorems_detailed(bare_path)
        d["numbersTable"] = parse_numbers_table(bare_path)
    if beyond_path is not None:
        d["beyondBarePath"] = str(beyond_path.relative_to(ROOT))
        d["bonusTheorems"] = parse_bonus_theorems(beyond_path)

    # Cross-cuts touching this vertex
    ccs = parse_cross_cuts_for_vertex(vertex_key)
    if ccs:
        d["crossCutsDetailed"] = ccs

    # 3) X-RAY file (under strategy/x-ray/proof-chain/<vertex>/X-RAY.md)
    xr = ROOT / "strategy" / "x-ray" / "proof-chain" / vertex_key / "X-RAY.md"
    if xr.exists():
        d["xRayPath"] = f"strategy/x-ray/proof-chain/{vertex_key}/X-RAY.md"
        d["faceHistogram"] = parse_face_histogram(xr)
        d["projectionHistogram"] = parse_projection_histogram(xr)
        d["crossCutCount"] = parse_cross_cut_count(xr)
        d["primary"] = parse_primary_assignments(xr)
        d["layerXray"] = parse_layer_xray(xr)

    # 4) Ladder (13 rungs)
    ladder, det = compute_ladder(vertex_key, paper_dir, strategy_dirname)
    d["ladder"] = ladder
    d["ladderDetections"] = det

    # 5) Artifact registry (for mode toggle buttons)
    artifacts: dict[str, str] = {}
    if bare_path is not None:
        artifacts["bare"] = str(bare_path.relative_to(ROOT))
    if beyond_path is not None:
        artifacts["beyond-bare"] = str(beyond_path.relative_to(ROOT))
    if strat_md_used is not None:
        artifacts["strategy"] = str(strat_md_used.relative_to(ROOT))
    if xr.exists():
        artifacts["x-ray"] = str(xr.relative_to(ROOT))
    if full_path is not None:
        artifacts["full"] = str(full_path.relative_to(ROOT))
        # If 'beyond-full' is also in deliv, add it
    if strategy_dirname:
        deliv = ROOT / "strategy" / strategy_dirname / "deliverables"
        if deliv.exists():
            for f in deliv.iterdir():
                if f.name.endswith("-beyond-full.md"):
                    artifacts["beyond-full"] = str(f.relative_to(ROOT))
    # Compliance = latest commit-memo.md (has verdict-map summary)
    if strategy_dirname:
        runs_dir = ROOT / "strategy" / strategy_dirname / "pac-output" / "runs"
        latest = find_latest_run(runs_dir)
        if latest is not None:
            cm = latest / "commit-memo.md"
            if cm.exists():
                artifacts["compliance"] = str(cm.relative_to(ROOT))
    d["artifacts"] = artifacts

    return d

# ---------------------------------------------------------------------------
# Shape inventory (43 positions — the slider)
# ---------------------------------------------------------------------------
# Each entry: dict with at minimum name/class/paper; some provide 'vertex' and
# 'strategy_dir' for ring vertices. Classes drive SVG rendering in app.js.

SHAPE_SPEC: list[dict[str, Any]] = [
    # Row 1 — Foundational
    {"name": "e-circle",
     "class": "e-circle",
     "paper": "paper60-the-geometry-of-the-circle",
     "label": "S¹ — e-circle, R ≈ 10.10 μm"},
    {"name": "Bouquet topology",
     "class": "bouquet",
     "paper": "paper61-projections-of-the-5d-geometry",
     "label": "6-ring wedge sum ⋁_QG5D"},
    {"name": "Core QG5D",
     "class": "core",
     "paper": "paper1",
     "label": "M⁵ = M⁴ × S¹ — 22 theorems"},

    # Row 2 — Inner rings
    {"name": "Branch A — Quantum",
     "class": "inner-ring",
     "paper": "paper1",
     "innerRing": "branch-a-quantum",
     "itemCount": 9,
     "label": "9 quantum items — P_A projection"},
    {"name": "Branch B — Gravity",
     "class": "inner-ring",
     "paper": "paper1",
     "innerRing": "branch-b-gravity",
     "itemCount": 4,
     "label": "4 gravity items — KK reduction, UV finite, BPHZ, Goroff-Sagnotti"},
    {"name": "Branch C — Cosmology",
     "class": "inner-ring",
     "paper": "paper2",
     "innerRing": "branch-c-cosmology",
     "itemCount": 10,
     "label": "10 cosmology items — H_0, N_eff, t_0, S_8, BBN, dark energy…"},
    {"name": "Branch D — CBB",
     "class": "inner-ring",
     "paper": "paper12",
     "innerRing": "branch-d-cbb",
     "itemCount": 5,
     "label": "5 CBB axioms + operator dictionary (L̂ = log R̂)"},
    {"name": "Branch E — 36 Pins",
     "class": "inner-ring",
     "paper": "paper12",
     "innerRing": "branch-e-pins",
     "itemCount": 36,
     "label": "36 sub-percent predictions — 27 spectral, 9 geometric"},

    # Row 3 — Projection operators
    {"name": "P_A Quantum projection",
     "class": "projection-operator",
     "paper": "paper61-projections-of-the-5d-geometry",
     "projector": "P_A",
     "label": "5D → 4D quantum: forgets KK gap"},
    {"name": "P_B Gravity projection",
     "class": "projection-operator",
     "paper": "paper61-projections-of-the-5d-geometry",
     "projector": "P_B",
     "label": "5D → 4D gauge bundle: preserves KK gap"},
    {"name": "P_C Cosmology projection",
     "class": "projection-operator",
     "paper": "paper61-projections-of-the-5d-geometry",
     "projector": "P_C",
     "label": "5D → 4D cosmological: preserves horizon pins"},
    {"name": "P_D CBB projection",
     "class": "projection-operator",
     "paper": "paper61-projections-of-the-5d-geometry",
     "projector": "P_D",
     "label": "5D → 4D operator-algebra: modular flow"},
    {"name": "P_E Pins projection",
     "class": "projection-operator",
     "paper": "paper61-projections-of-the-5d-geometry",
     "projector": "P_E",
     "label": "5D → 4D spectral: Riemann zeros as pin rays"},
    {"name": "P_O Outer projection",
     "class": "projection-operator",
     "paper": "paper61-projections-of-the-5d-geometry",
     "projector": "P_O",
     "label": "5D → 4D conjecture-grade boundary"},

    # Row 4 — 24 outer-ring vertices
    {"name": "YM",
     "class": "ring-vertex", "vertex": "ym", "paper": "paper08-yang-mills",
     "strategyDir": "ym", "millennium": True},
    {"name": "RH",
     "class": "ring-vertex", "vertex": "rh", "paper": "paper13-rh",
     "strategyDir": "rh", "millennium": True},
    {"name": "GRH",
     "class": "ring-vertex", "vertex": "grh", "paper": "paper13b-grh",
     "strategyDir": None},
    {"name": "Lindelöf",
     "class": "ring-vertex", "vertex": "lindelof", "paper": "paper45-lindelof",
     "strategyDir": None},
    {"name": "BSD",
     "class": "ring-vertex", "vertex": "bsd", "paper": "paper26-bsd",
     "strategyDir": "bsd", "millennium": True},
    {"name": "H12",
     "class": "ring-vertex", "vertex": "h12", "paper": "paper25-hilbert-12",
     "strategyDir": None},
    {"name": "NS",
     "class": "ring-vertex", "vertex": "ns", "paper": "paper30-navier-stokes",
     "strategyDir": "ns", "millennium": True},
    {"name": "Turbulence",
     "class": "ring-vertex", "vertex": "turbulence", "paper": "paper38-turbulence",
     "strategyDir": None},
    {"name": "Hodge",
     "class": "ring-vertex", "vertex": "hodge", "paper": "paper29-hodge",
     "strategyDir": "hodge", "millennium": True},
    {"name": "Baum-Connes",
     "class": "ring-vertex", "vertex": "baum-connes", "paper": "paper31-baum-connes",
     "strategyDir": None},
    {"name": "PvNP",
     "class": "ring-vertex", "vertex": "pvnp", "paper": "paper28-pvnp",
     "strategyDir": "pvnp", "millennium": True},
    {"name": "VP-vs-VNP",
     "class": "ring-vertex", "vertex": "vp-vs-vnp", "paper": "paper39-vp-vs-vnp",
     "strategyDir": None},
    {"name": "BGS",
     "class": "ring-vertex", "vertex": "bgs", "paper": "paper32-bgs-spectral-statistics",
     "strategyDir": None},
    {"name": "Katz-Sarnak",
     "class": "ring-vertex", "vertex": "katz-sarnak", "paper": "paper46-katz-sarnak",
     "strategyDir": None},
    {"name": "Twin Primes",
     "class": "ring-vertex", "vertex": "twin-primes", "paper": "paper34-twin-primes",
     "strategyDir": None},
    {"name": "Cramér",
     "class": "ring-vertex", "vertex": "cramer", "paper": "paper43-cramer",
     "strategyDir": None},
    {"name": "Goldbach",
     "class": "ring-vertex", "vertex": "goldbach", "paper": "paper33-goldbach",
     "strategyDir": None},
    {"name": "ABC",
     "class": "ring-vertex", "vertex": "abc", "paper": "paper37-abc",
     "strategyDir": None},
    {"name": "OPN",
     "class": "ring-vertex", "vertex": "opn", "paper": "paper40-odd-perfect",
     "strategyDir": None},
    {"name": "Collatz",
     "class": "ring-vertex", "vertex": "collatz", "paper": "paper41-collatz",
     "strategyDir": None},
    {"name": "Lehmer",
     "class": "ring-vertex", "vertex": "lehmer", "paper": "paper42-lehmer",
     "strategyDir": None},
    {"name": "Sato-Tate",
     "class": "ring-vertex", "vertex": "sato-tate", "paper": "paper44-sato-tate",
     "strategyDir": None},
    {"name": "Schanuel",
     "class": "ring-vertex", "vertex": "schanuel", "paper": "paper35-schanuel",
     "strategyDir": None},
    {"name": "Hilbert 6",
     "class": "ring-vertex", "vertex": "hilbert-6", "paper": "paper36-hilbert-6",
     "strategyDir": None},

    # Row 5 — Composite shapes
    {"name": "36-pin circle",
     "class": "36-pin",
     "paper": "paper12",
     "pinTableRef": "paper12/research/23-framework-predictions-master-table.md",
     "label": "36 pins — 27 spectral + 9 geometric"},
    {"name": "Chord graph",
     "class": "chord-graph",
     "paper": "strategy/x-ray",
     "crossCutRef": "strategy/x-ray/pac-output/runs/run-01/cross-cut-edges.md",
     "label": "25 vertices, cross-cut chords"},
    {"name": "Face graph",
     "class": "face-graph",
     "paper": "paper60-the-geometry-of-the-circle",
     "label": "10 faces — TOPOLOGY / DYNAMICS / HARMONICS / MEASURE / AMPLITUDE / SYMMETRY / CURVATURE / ARITHMETIC / RESONANCE / SPREAD"},
    {"name": "South trough / ellipse",
     "class": "south-trough",
     "paper": "paper60-the-geometry-of-the-circle",
     "sectionRef": "paper60-the-geometry-of-the-circle/28-the-south-trough-needs-lifting.md",
     "label": "Loopsidedness diagnostic — ring as ellipse, north pole complete, south trough unthickened"},
    {"name": "Outer ring as whole",
     "class": "outer-ring-whole",
     "paper": "strategy/x-ray",
     "label": "25-vertex ring + chord overlay"},
]

# ---------------------------------------------------------------------------
# Enrich each shape
# ---------------------------------------------------------------------------
def enrich_e_circle(entry: dict[str, Any]) -> dict[str, Any]:
    entry["description"] = extract_first_paragraph(
        ROOT / "paper60-the-geometry-of-the-circle" / "00-table-of-contents.md"
    ) or "The e-circle (S¹, R ≈ 10.10 μm) is the fifth dimension. Ten faces encode every outer-ring conjecture as a question about the circle."
    entry["radiusMicrons"] = 10.10
    entry["faces"] = ["TOPOLOGY", "DYNAMICS", "HARMONICS", "MEASURE",
                      "AMPLITUDE", "SYMMETRY", "CURVATURE", "ARITHMETIC",
                      "RESONANCE", "SPREAD"]
    entry["faceConjectures"] = {
        "TOPOLOGY": "Lehmer",
        "DYNAMICS": "Cramér",
        "HARMONICS": "Collatz",
        "MEASURE": "Sato-Tate",
        "AMPLITUDE": "Lindelöf",
        "SYMMETRY": "Katz-Sarnak",
        "CURVATURE": "Yang-Mills",
        "ARITHMETIC": "Goldbach / Twin Primes",
        "RESONANCE": "Selberg ¼",
        "SPREAD": "QUE (Lindenstrauss)",
    }
    return entry

def enrich_bouquet(entry: dict[str, Any]) -> dict[str, Any]:
    # Try paper61 sections
    toc = ROOT / "paper61-projections-of-the-5d-geometry" / "table-of-contents.md"
    entry["description"] = extract_first_paragraph(toc) or \
        "Every observed mathematical shape is a projection of the 5D geometry M⁵ = M⁴ × S¹ into 4D. The bouquet displays all projections as a wedge sum of six subspaces at the shared basepoint QG5D."
    entry["rings"] = ["Outer ring", "Branch A — Quantum", "Branch B — Gravity",
                      "Branch C — Cosmology", "Branch D — CBB",
                      "Branch E — 36 Pins"]
    return entry

def enrich_core(entry: dict[str, Any]) -> dict[str, Any]:
    pc = ROOT / "paper1" / "PROOF-CHAIN.md"
    entry["description"] = extract_first_paragraph(pc) or "QG5D foundation: four postulates on M⁴ × S¹ generate 22 theorems."
    entry["theoremCount"] = 22
    entry["status"] = parse_proof_chain_status(pc)
    entry["predictionCount"] = 36
    return entry

def enrich_inner_ring(entry: dict[str, Any]) -> dict[str, Any]:
    # Check if ring bundle exists
    inner = ROOT / "strategy" / "inner-rings" / entry["innerRing"]
    if inner.exists():
        pac = inner / "pac-output"
        pc_dir = inner / "proof-chain"
        has_content = any(pac.iterdir()) if pac.exists() else False
        has_pc = any(pc_dir.iterdir()) if pc_dir.exists() else False
        if not has_content and not has_pc:
            entry["status"] = "AUDIT PENDING"
            log(f"AUDIT PENDING: inner-ring {entry['innerRing']}")
    else:
        entry["status"] = "AUDIT PENDING"
        log(f"MISS: inner-ring {entry['innerRing']}")
    # Borrow description from paper1 PROOF-CHAIN tree
    entry["description"] = {
        "branch-a-quantum": "Branch A: 5 interpretations + 3 derivations + 1 measurement problem = 9 quantum items, all geometric consequences of the 5D projection (Paper 1 §3, §4).",
        "branch-b-gravity": "Branch B: KK reduction (Thm K), perturbative UV finiteness (K.1), BPHZ (K.3), Goroff-Sagnotti R³ = 0. Four gravity items (Paper 1 §6, §7).",
        "branch-c-cosmology": "Branch C: H_0, N_eff, t_0, S_8, BBN, dark energy, and four more cosmological observables, all predicted at sub-percent precision (Paper 2).",
        "branch-d-cbb": "Branch D: five CBB axioms + operator dictionary L̂ = log R̂, with 3 sectors + bridge family {β_k} (Paper 12).",
        "branch-e-pins": "Branch E: 36 sub-percent predictions form the pin registry — 27 spectral + 9 geometric + 1 interface. Zero free parameters. All predictions match experiment (Papers 11, 12, 23, 24).",
    }.get(entry["innerRing"], "")
    return entry

def enrich_projection_op(entry: dict[str, Any]) -> dict[str, Any]:
    projector = entry["projector"]
    entry["description"] = {
        "P_A": "P_A projects M⁵ to the quantum subalgebra, forgetting the KK spectral gap and retaining observables of 4D quantum mechanics (paper61 §07).",
        "P_B": "P_B projects M⁵ to the gauge-bundle subspace over M⁴. The KK spectral gap survives as the Yang-Mills mass gap (paper61 §08).",
        "P_C": "P_C projects M⁵ to the cosmological sector: Hubble rate, dark-matter abundance, horizon pins (paper61 §09).",
        "P_D": "P_D projects M⁵ to the CBB operator-algebra sector. Modular flow, KMS states, type III₁ ergodicity (paper61 §10).",
        "P_E": "P_E projects M⁵ to the spectral registry: 36 pins as matrix elements of the CBB operator dictionary, Riemann zeros as rays (paper61 §11).",
        "P_O": "P_O is the outer-ring (conjecture-grade) projection. Each of the 25 outer-ring vertices is a projection of one face of M⁵ to a famous conjecture (paper61 §12).",
    }.get(projector, "")
    return entry

def enrich_ring_vertex(entry: dict[str, Any]) -> dict[str, Any]:
    vertex = entry.get("vertex", "")
    paper_dir = entry.get("paper", "")
    strat_dir = entry.get("strategyDir")
    data = extract_ring_vertex(vertex, paper_dir, strat_dir)
    entry.update(data)
    # Mark AUDIT PENDING if no proof chain and no strategy bundle
    if not data.get("proofChainStatus") and not data.get("strategyDir"):
        entry["status"] = "AUDIT PENDING"
        log(f"AUDIT PENDING: ring-vertex {vertex}")
    return entry

def enrich_36_pin(entry: dict[str, Any]) -> dict[str, Any]:
    pin_md = ROOT / "paper12" / "research" / "23-framework-predictions-master-table.md"
    txt = safe_read(pin_md)
    # Count table rows (rough)
    if txt:
        entry["description"] = (
            "34 sub-percent fits consolidated from preprints and research notes — the programme's pin registry. All 15 first non-trivial Riemann zeros appear in at least one fitted formula."
        )
    entry["pinCount"] = 36
    # Classify by domain
    entry["pinDomains"] = {
        "Cosmology": 10,
        "QCD / flavour": 8,
        "CKM / PMNS": 9,
        "GUT / interface": 4,
        "Other": 5,
    }
    return entry

def enrich_chord_graph(entry: dict[str, Any]) -> dict[str, Any]:
    cross_cut_md = ROOT / "strategy" / "x-ray" / "pac-output" / "runs" / "run-01" / "cross-cut-edges.md"
    txt = safe_read(cross_cut_md)
    edges: list[dict[str, str]] = []
    # Match 'ym:L1 ↔ qg5d:Branch B — shared <..>' etc. Vertex names may
    # include slashes (e.g. 'selberg-1/4') and digits; layer labels may be
    # multi-word ('Branch B', 'L_top').
    for line in txt.splitlines():
        m = re.match(
            r"^-\s*([\w\-/]+):([\w_]+)\s*[↔<>-]+\s*([\w\-/]+):([\w\s_]+?)\s*—\s*(?:shared|face-only)\s*([^—]+)",
            line,
        )
        if m:
            edges.append({
                "from": m.group(1).strip(),
                "fromLayer": m.group(2).strip(),
                "to": m.group(3).strip(),
                "toLayer": m.group(4).strip(),
                "shared": m.group(5).strip(),
            })
    entry["edges"] = edges
    entry["edgeCount"] = len(edges)
    entry["description"] = (
        f"Cross-cut chord graph — {len(edges)} edges extracted from the atlas "
        "(run-01). Each chord is a shared invariant / face / projection "
        "between two vertices."
    )
    return entry

def enrich_face_graph(entry: dict[str, Any]) -> dict[str, Any]:
    entry["faces"] = ["TOPOLOGY", "DYNAMICS", "HARMONICS", "MEASURE",
                      "AMPLITUDE", "SYMMETRY", "CURVATURE", "ARITHMETIC",
                      "RESONANCE", "SPREAD"]
    entry["description"] = (
        "The 10 faces of the e-circle. Each face asks one question about S¹ "
        "and answers it with the associated outer-ring conjecture. Adjacency "
        "structure comes from the paper60 §13 table; paper61 projections "
        "glue face → vertex."
    )
    # Build adjacency as a dict of pairs (canonical paper60 §13 ordering cycle)
    entry["adjacency"] = [
        ["TOPOLOGY", "DYNAMICS"],
        ["DYNAMICS", "HARMONICS"],
        ["HARMONICS", "MEASURE"],
        ["MEASURE", "AMPLITUDE"],
        ["AMPLITUDE", "SYMMETRY"],
        ["SYMMETRY", "CURVATURE"],
        ["CURVATURE", "ARITHMETIC"],
        ["ARITHMETIC", "RESONANCE"],
        ["RESONANCE", "SPREAD"],
        ["SPREAD", "TOPOLOGY"],
    ]
    return entry

def enrich_south_trough(entry: dict[str, Any]) -> dict[str, Any]:
    md = ROOT / "paper60-the-geometry-of-the-circle" / "28-the-south-trough-needs-lifting.md"
    entry["description"] = extract_first_paragraph(md) or \
        "The ring is an ellipse, not a circle. The north pole is complete work (YM, RH, BSD). The south trough is the unthickened frontier. The lopsidedness is itself the x-ray — it tells us where to excise, bypass, and repair."
    # Assign rough "latitude" scores for 25 vertices (north high, south low)
    entry["northVertices"] = ["ym", "rh", "bsd", "ns", "hodge", "pvnp"]
    entry["southVertices"] = ["schanuel", "hilbert-6", "abc", "collatz", "lehmer", "opn"]
    return entry

def enrich_outer_ring_whole(entry: dict[str, Any]) -> dict[str, Any]:
    # All 25 vertices; inject names in ring order
    entry["vertexOrder"] = [
        "qg5d", "ym", "rh", "grh", "lindelof", "bsd", "h12", "ns",
        "turbulence", "hodge", "baum-connes", "pvnp", "vp-vs-vnp",
        "bgs", "katz-sarnak", "twin-primes", "cramer", "goldbach",
        "abc", "opn", "collatz", "lehmer", "sato-tate", "schanuel",
        "hilbert-6",
    ]
    entry["description"] = (
        "The outer ring (25 vertices) with chord structure overlaid. "
        "qg5d is the hub and bouquet basepoint; the remaining 24 are "
        "outer-ring conjectures. Chord edges are cross-cut invariants "
        "between vertices, extracted from x-ray atlas run-01."
    )
    return entry

# ---------------------------------------------------------------------------
# Ring aggregation — populates `aggregated_*` fields for connecting shapes
# ---------------------------------------------------------------------------
def _find_shape(shapes: list[dict[str, Any]], name_or_vertex: str) -> dict[str, Any] | None:
    lo = name_or_vertex.lower()
    for s in shapes:
        if s.get("vertex", "").lower() == lo:
            return s
        if s.get("name", "").lower() == lo:
            return s
        if s.get("innerRing", "").lower() == lo:
            return s
    return None

def _aggregate_from_nodes(nodes: list[dict[str, Any]], field: str) -> list[Any]:
    """Collect entries from `field` across each connected node, tagging
    with source vertex/name for the modal UI."""
    out: list[Any] = []
    for node in nodes:
        if not node:
            continue
        items = node.get(field, []) or []
        src = node.get("vertex") or node.get("name") or ""
        for it in items:
            if isinstance(it, dict):
                copy = dict(it)
                copy.setdefault("_source", src)
                out.append(copy)
            else:
                out.append({"_source": src, "value": it})
    return out

def aggregate_ring_shapes(shapes: list[dict[str, Any]]) -> None:
    """For each 'connecting' shape (bouquet, outer-ring, chord, face, inner,
    projection operators, 36-pin), populate aggregated_* fields by
    unioning content from the connected vertices / inner rings."""
    # Map vertex -> shape
    by_vertex: dict[str, dict[str, Any]] = {}
    for s in shapes:
        v = s.get("vertex")
        if v:
            by_vertex[v] = s

    # All ring-vertex shapes
    ring_vertices = [s for s in shapes if s.get("class") == "ring-vertex"]

    def set_agg(shape: dict[str, Any], nodes: list[dict[str, Any]]) -> None:
        shape["connectedNodes"] = [
            {"name": n.get("name"), "vertex": n.get("vertex"), "position": n.get("position"),
             "class": n.get("class")}
            for n in nodes if n
        ]
        shape["aggregatedTheorems"] = _aggregate_from_nodes(nodes, "theoremsDetailed")
        shape["aggregatedRequirements"] = _aggregate_from_nodes(nodes, "requirementsDetailed")
        shape["aggregatedLayers"] = _aggregate_from_nodes(nodes, "chainLayers")
        shape["aggregatedWalls"] = _aggregate_from_nodes(nodes, "namedWalls")
        shape["aggregatedCrossCuts"] = _aggregate_from_nodes(nodes, "crossCutsDetailed")
        shape["aggregatedBonus"] = _aggregate_from_nodes(nodes, "bonusTheorems")
        shape["aggregatedNumbers"] = _aggregate_from_nodes(nodes, "numbersTable")

    for shape in shapes:
        cls = shape.get("class")
        if cls == "bouquet":
            # QG5D + inner rings + outer ring vertices + projection ops
            nodes = []
            core = _find_shape(shapes, "Core QG5D")
            if core:
                nodes.append(core)
            for s in shapes:
                if s.get("class") in {"inner-ring", "projection-operator", "ring-vertex"}:
                    nodes.append(s)
            set_agg(shape, nodes)

        elif cls == "outer-ring-whole":
            # All 25 vertices (24 ring-vertex + core qg5d)
            nodes = []
            core = _find_shape(shapes, "Core QG5D")
            if core:
                nodes.append(core)
            nodes.extend(ring_vertices)
            set_agg(shape, nodes)

        elif cls == "chord-graph":
            # All cross-cut edges + content of their endpoints
            all_ccs = parse_all_cross_cuts()
            shape["aggregatedCrossCutsAll"] = all_ccs
            touched = set()
            for e in all_ccs:
                touched.add(e.get("from", ""))
                touched.add(e.get("to", ""))
            nodes = [by_vertex[v] for v in touched if v in by_vertex]
            set_agg(shape, nodes)

        elif cls == "face-graph":
            # Face → canonical conjecture (from paper60 §13 mapping)
            face_map = {
                "TOPOLOGY": ["lehmer"],
                "DYNAMICS": ["cramer"],
                "HARMONICS": ["collatz"],
                "MEASURE": ["sato-tate"],
                "AMPLITUDE": ["lindelof"],
                "SYMMETRY": ["katz-sarnak"],
                "CURVATURE": ["ym"],
                "ARITHMETIC": ["goldbach", "twin-primes"],
                "RESONANCE": ["rh"],  # Selberg 1/4 ↔ RH in this programme
                "SPREAD": ["bgs"],  # QUE-class ↔ spectral statistics
            }
            # Also pull vertices whose primary face matches
            face_to_vertices: dict[str, list[str]] = {k: list(v) for k, v in face_map.items()}
            for v, s in by_vertex.items():
                pf = (s.get("primary") or {}).get("face", "")
                if pf and pf in face_to_vertices:
                    if v not in face_to_vertices[pf]:
                        face_to_vertices[pf].append(v)
            shape["faceVertices"] = face_to_vertices
            nodes = []
            seen: set[str] = set()
            for vs in face_to_vertices.values():
                for v in vs:
                    if v in by_vertex and v not in seen:
                        nodes.append(by_vertex[v])
                        seen.add(v)
            set_agg(shape, nodes)

        elif cls == "inner-ring":
            # Inner ring content = the items in that branch
            # For now we point to the structural description and any
            # branch-level PROOF-CHAIN artifact if present.
            shape["connectedNodes"] = []
            shape["aggregatedTheorems"] = []
            shape["aggregatedRequirements"] = []
            shape["aggregatedLayers"] = []
            shape["aggregatedWalls"] = []
            shape["aggregatedCrossCuts"] = []
            shape["aggregatedBonus"] = []
            shape["aggregatedNumbers"] = []

        elif cls == "projection-operator":
            # P_X's vertices = those whose primary projection is P_X
            px = shape.get("projector", "")
            nodes = []
            for v, s in by_vertex.items():
                pp = (s.get("primary") or {}).get("projection", "")
                pp_clean = pp.replace("$", "").strip()
                if pp_clean == px:
                    nodes.append(s)
            # Fallback: programme-level mapping if xray data is sparse
            if not nodes:
                programme_map = {
                    "P_A": [],
                    "P_B": ["ym"],
                    "P_C": [],
                    "P_D": [],
                    "P_E": [],
                    "P_O": ["rh", "bsd", "pvnp", "ns", "hodge"],
                }
                nodes = [by_vertex[v] for v in programme_map.get(px, []) if v in by_vertex]
            set_agg(shape, nodes)

        elif cls == "36-pin":
            # All 36 pins + (optionally) union of vertices citing them
            pin_md = ROOT / "paper12" / "research" / "23-framework-predictions-master-table.md"
            shape["aggregatedPins"] = parse_pin_master_table(pin_md)
            shape["connectedNodes"] = []
            shape["aggregatedTheorems"] = []
            shape["aggregatedRequirements"] = []
            shape["aggregatedLayers"] = []
            shape["aggregatedWalls"] = []
            shape["aggregatedCrossCuts"] = []
            shape["aggregatedBonus"] = []
            shape["aggregatedNumbers"] = []

def parse_pin_master_table(path: Path, max_pins: int = 50) -> list[dict[str, str]]:
    """Extract pin rows from the master predictions table."""
    txt = safe_read(path)
    if not txt:
        return []
    pins: list[dict[str, str]] = []
    for line in txt.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 3:
            continue
        if set(cells[0]) <= {"-", ":", " "}:
            continue
        if cells[0].lower() in {"parameter", "pin", "#", "num"}:
            continue
        param = _clean_md(cells[0], 120)
        if not param or len(param) < 2:
            continue
        measured = _clean_md(cells[1] if len(cells) > 1 else "", 120)
        formula = _clean_md(cells[2] if len(cells) > 2 else "", 180)
        err = _clean_md(cells[3] if len(cells) > 3 else "", 40)
        gammas = _clean_md(cells[4] if len(cells) > 4 else "", 80)
        pins.append({
            "parameter": param,
            "measured": measured,
            "formula": formula,
            "error": err,
            "gammas": gammas,
        })
        if len(pins) >= max_pins:
            break
    return pins

# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------
def build_shape(pos: int, spec: dict[str, Any]) -> dict[str, Any]:
    entry: dict[str, Any] = {
        "position": pos,
        "name": spec["name"],
        "class": spec["class"],
        "paper": spec.get("paper", ""),
    }
    # Copy through known fields without mutating spec
    for k in ("label", "innerRing", "itemCount", "projector", "vertex",
              "strategyDir", "millennium", "pinTableRef", "crossCutRef",
              "sectionRef"):
        if k in spec:
            entry[k] = spec[k]

    # Dispatch enrichers
    cls = spec["class"]
    if cls == "e-circle":
        return enrich_e_circle(entry)
    if cls == "bouquet":
        return enrich_bouquet(entry)
    if cls == "core":
        return enrich_core(entry)
    if cls == "inner-ring":
        return enrich_inner_ring(entry)
    if cls == "projection-operator":
        return enrich_projection_op(entry)
    if cls == "ring-vertex":
        return enrich_ring_vertex(entry)
    if cls == "36-pin":
        return enrich_36_pin(entry)
    if cls == "chord-graph":
        return enrich_chord_graph(entry)
    if cls == "face-graph":
        return enrich_face_graph(entry)
    if cls == "south-trough":
        return enrich_south_trough(entry)
    if cls == "outer-ring-whole":
        return enrich_outer_ring_whole(entry)
    return entry

def main() -> int:
    log(f"build.py start {_dt.datetime.now().isoformat()}")
    log(f"ROOT={ROOT}")
    log(f"specs={len(SHAPE_SPEC)}")
    shapes: list[dict[str, Any]] = []
    for i, spec in enumerate(SHAPE_SPEC, 1):
        try:
            shape = build_shape(i, spec)
            shapes.append(shape)
        except Exception as e:
            log(f"ERR  shape {i} {spec.get('name')}: {e}")
            shapes.append({
                "position": i,
                "name": spec.get("name", "?"),
                "class": spec.get("class", "unknown"),
                "paper": spec.get("paper", ""),
                "status": "AUDIT PENDING",
                "errorMessage": str(e),
            })

    # Aggregate connecting shapes (bouquet, outer ring, chord, face, inner,
    # projections, 36-pin) — must happen AFTER all ring-vertex enrichers run.
    try:
        aggregate_ring_shapes(shapes)
    except Exception as e:
        log(f"ERR  aggregation: {e}")

    # Ladder distribution diagnostic
    ladder_count: dict[int, int] = {}
    for s in shapes:
        if s.get("class") != "ring-vertex":
            continue
        l = s.get("ladder") or []
        highest = 0
        for i, on in enumerate(l, 1):
            if on:
                highest = i
        ladder_count[highest] = ladder_count.get(highest, 0) + 1
    if ladder_count:
        log(f"LADDER ring-vertex distribution: {dict(sorted(ladder_count.items()))}")

    # Audit-pending count
    pending = sum(1 for s in shapes if s.get("status") == "AUDIT PENDING")
    log(f"AUDIT PENDING count: {pending}")
    log(f"total shapes: {len(shapes)}")

    # Collect artifact bodies for mode-toggle panels
    artifact_bodies: dict[str, dict[str, Any]] = {}
    collected = set()
    for s in shapes:
        arts = s.get("artifacts") or {}
        for _k, rel in arts.items():
            if rel in collected:
                continue
            collected.add(rel)
            abs_path = ROOT / rel
            body_data = read_artifact(abs_path)
            if body_data:
                artifact_bodies[rel] = body_data

    log(f"artifact bodies collected: {len(artifact_bodies)}")

    # Emit data.js
    ts = _dt.datetime.now().isoformat(timespec="seconds")
    body = json.dumps(shapes, indent=2, ensure_ascii=False)
    arts_body = json.dumps(artifact_bodies, indent=2, ensure_ascii=False)
    ladder_names_body = json.dumps(LADDER_NAMES, ensure_ascii=False)
    OUT.write_text(
        "// Auto-generated by build.py — do not edit\n"
        "// Regenerate: python3 visualization/build.py\n\n"
        f"const SHAPE_DATA = {body};\n"
        f"const ARTIFACT_BODIES = {arts_body};\n"
        f"const LADDER_NAMES = {ladder_names_body};\n"
        f"const BUILD_TIMESTAMP = {json.dumps(ts)};\n"
        f"const SHAPE_COUNT = {len(shapes)};\n"
        f"const AUDIT_PENDING_COUNT = {pending};\n",
        encoding="utf-8",
    )
    log(f"wrote {OUT.relative_to(ROOT)} ({OUT.stat().st_size} bytes)")
    flush_log()
    print(f"OK  {len(shapes)} shapes, {pending} AUDIT PENDING "
          f"— wrote {OUT.relative_to(ROOT)}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
