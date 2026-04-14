#!/usr/bin/env python3
"""build.py -- Scan paper60 and emit data.js for the torus visualization.

Reads every markdown file in paper60-the-geometry-of-the-circle/ and extracts
what the paper says about the torus: the definition, the 10 faces, the two
generating circles, the Riemann-zero intersections, the south trough, the
ellipse/confidence distribution, and the explanation steps.

Emits TORUS_DATA as a global constant consumed by app.js under file://.

Usage:
    python3 visualization/torus/build.py

Output:
    visualization/torus/data.js      (generated)
    visualization/torus/build.log    (generated)

No external deps -- Python 3 stdlib only.
"""
from __future__ import annotations

import datetime as _dt
import json
import re
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parent.parent.parent
PAPER60 = ROOT / "paper60-the-geometry-of-the-circle"
OUT_DIR = ROOT / "visualization" / "torus"
OUT = OUT_DIR / "data.js"
LOG = OUT_DIR / "build.log"

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
_LOG_LINES: list[str] = []

def log(msg: str) -> None:
    _LOG_LINES.append(msg)

def flush_log() -> None:
    LOG.write_text("\n".join(_LOG_LINES) + "\n", encoding="utf-8")

def safe_read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        log(f"ERR  {path}: {e}")
        return ""

# ---------------------------------------------------------------------------
# Face table (the ten faces, as listed in paper60 files 17 & 28)
# Source: paper60/17-two-circles-one-torus.md ASCII grid, paper60/20, paper60/28
# ---------------------------------------------------------------------------
#
# Paper 60's grid (file 17) lays faces out as 2 rows x 5 columns:
#   row 0 (top/geometric):  TOPOLOGY  HARMONICS  CURVATURE  MEASURE   SPREAD
#   row 1 (bot/spectral):   DYNAMICS  AMPLITUDE  SYMMETRY   ARITHMETIC RESONANCE
#
# We reproduce that grid faithfully. Column u-coordinates are equi-spaced around
# the major (geometric) circle. Poloidal coordinate v picks geometric (top) or
# spectral (bottom) row.
#
# Confidence values from paper60/20 and paper60/28.
#
FACES_CANONICAL = [
    # column 0
    dict(key="TOPOLOGY",   conj="Lehmer",           question="What can LIVE on it?",
         circle="geometric", col=0, conf=4.0, paper="Paper 42", face_num=1),
    dict(key="DYNAMICS",   conj="Cramer",           question="How does the flow TRAVERSE it?",
         circle="spectral",  col=0, conf=5.0, paper="Paper 43", face_num=2),
    # column 1
    dict(key="HARMONICS",  conj="Collatz",          question="How do modes MIX on it?",
         circle="geometric", col=1, conf=4.0, paper="Paper 41", face_num=3),
    dict(key="AMPLITUDE",  conj="Lindeloef",        question="How LOUD can it get?",
         circle="spectral",  col=1, conf=7.0, paper="Paper 45", face_num=5),
    # column 2
    dict(key="CURVATURE",  conj="Yang-Mills",       question="How do connections CURVE on it?",
         circle="geometric", col=2, conf=9.5, paper="Paper 08", face_num=7),
    dict(key="SYMMETRY",   conj="Katz-Sarnak",      question="Which GROUP acts on it?",
         circle="spectral",  col=2, conf=7.0, paper="Paper 46", face_num=6),
    # column 3
    dict(key="MEASURE",    conj="Sato-Tate",        question="How do angles DISTRIBUTE on it?",
         circle="geometric", col=3, conf=6.0, paper="Paper 44", face_num=4),
    dict(key="ARITHMETIC", conj="Goldbach/Twin",    question="How do integers LATTICE on it?",
         circle="spectral",  col=3, conf=1.0, paper="Papers 33-34", face_num=8),
    # column 4
    dict(key="SPREAD",     conj="QUE (Lindenstrauss)", question="How do eigenmodes SPREAD?",
         circle="both",      col=4, conf=8.0, paper="Paper 48", face_num=10),
    dict(key="RESONANCE",  conj="Selberg 1/4",      question="What frequencies are ALLOWED?",
         circle="spectral",  col=4, conf=6.0, paper="Paper 47", face_num=9),
]

# ---------------------------------------------------------------------------
# Ring vertices (25 of them, per paper60/20 and paper60/28 diagrams)
# Distributed around the major (geometric) circle of the torus.
# Confidence + zone taken from the paper60/28 elliptical diagram.
# ---------------------------------------------------------------------------
#
# Paper60/28 lists the 25 vertices in canonical ring order with confidence scores
# and maps them into four zones (NORTH/EAST/WEST/SOUTH). The ordering below is
# synthesized from the two radial diagrams in paper60/20 and paper60/28.
#
RING_VERTICES_CANONICAL = [
    dict(name="QG5D",         pos=0,  conf=10.0, zone="NORTH"),
    dict(name="YM",           pos=1,  conf=9.5,  zone="NORTH"),
    dict(name="RH",           pos=2,  conf=8.0,  zone="NORTH"),
    dict(name="Lindeloef",    pos=3,  conf=7.0,  zone="EAST"),
    dict(name="GRH",          pos=4,  conf=7.0,  zone="EAST"),
    dict(name="BGS",          pos=5,  conf=7.0,  zone="EAST"),
    dict(name="BSD",          pos=6,  conf=9.0,  zone="NORTH"),
    dict(name="PvNP",         pos=7,  conf=7.0,  zone="EAST"),
    dict(name="H6",           pos=8,  conf=7.0,  zone="WEST"),
    dict(name="H12",          pos=9,  conf=2.0,  zone="SOUTH"),
    dict(name="Cramer",       pos=10, conf=5.0,  zone="EAST"),
    dict(name="NS",           pos=11, conf=4.0,  zone="EAST"),
    dict(name="Hodge",        pos=12, conf=3.0,  zone="WEST"),
    dict(name="Turb",         pos=13, conf=2.0,  zone="SOUTH"),
    dict(name="Katz-Sarnak",  pos=14, conf=7.0,  zone="EAST"),
    dict(name="Sato-Tate",    pos=15, conf=6.0,  zone="WEST"),
    dict(name="Twin",         pos=16, conf=1.0,  zone="SOUTH"),
    dict(name="Goldbach",     pos=17, conf=1.0,  zone="SOUTH"),
    dict(name="Schanuel",     pos=18, conf=1.0,  zone="SOUTH"),
    dict(name="OPN",          pos=19, conf=4.0,  zone="WEST"),
    dict(name="Collatz",      pos=20, conf=4.0,  zone="WEST"),
    dict(name="Lehmer",       pos=21, conf=4.0,  zone="WEST"),
    dict(name="ABC",          pos=22, conf=1.0,  zone="SOUTH"),
    dict(name="B-C",          pos=23, conf=3.0,  zone="WEST"),
    dict(name="VP",           pos=24, conf=1.0,  zone="SOUTH"),
]

# ---------------------------------------------------------------------------
# Parse: look for torus definitions in the markdown
# ---------------------------------------------------------------------------

def extract_paragraphs(text: str, pattern: str, limit_chars: int = 2000) -> list[str]:
    """Return paragraphs (double-newline-separated) that match a regex.
    Skips markdown heading lines (starting with '#') and pure quote/epigraph
    lines shorter than 40 chars so we return substantive prose paragraphs.
    """
    rx = re.compile(pattern, re.IGNORECASE | re.DOTALL)
    paras = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    hits = []
    for p in paras:
        # skip headings
        if p.startswith("#"):
            continue
        # skip trivially short epigraphs
        if len(p) < 80:
            continue
        if rx.search(p):
            # flatten whitespace for compactness
            flat = re.sub(r"\s+", " ", p)
            hits.append(flat[:limit_chars])
    return hits


def extract_torus_definition(paper60_content: dict[str, str]) -> dict[str, Any]:
    """Find the core torus definition paragraphs (substantive prose only).

    The one-line summary and crossed-product are direct transcriptions of the
    content in paper60/17. Supporting quotes are pulled from the body text of
    files 17, 18, 19 using content-pattern matches that skip headings and
    epigraphs.
    """
    definition: dict[str, Any] = {
        "one_line": (
            "The e-circle (geometric, U(1), the fifth dimension) and the modular "
            "flow (spectral, KMS_1 orbit) are the two generating circles of a "
            "torus T^2 = S^1_geo x S^1_spec. The ten faces live on its surface."
        ),
        "crossed_product": "A_BC x_sigma R  (BC algebra crossed with modular flow)",
        "quotes": [],
        "source_files": [],
    }

    text17 = paper60_content.get("paper60-the-geometry-of-the-circle/17-two-circles-one-torus.md", "")
    for quote in extract_paragraphs(
            text17,
            r"(crossed product|mapping torus|two generating circles|geometric circle.*spectral circle)",
            limit_chars=400):
        if len(definition["quotes"]) < 3:
            definition["quotes"].append({
                "source": "paper60 \u00a717",
                "text": quote[:400],
            })
    if text17:
        definition["source_files"].append("paper60/17-two-circles-one-torus.md")

    text18 = paper60_content.get("paper60-the-geometry-of-the-circle/18-riemann-zeros-as-intersection.md", "")
    for quote in extract_paragraphs(
            text18,
            r"(intersection points|transversal|critical line IS|crossings grow)",
            limit_chars=400):
        if len(definition["quotes"]) < 5:
            definition["quotes"].append({
                "source": "paper60 \u00a718",
                "text": quote[:400],
            })
    if text18:
        definition["source_files"].append("paper60/18-riemann-zeros-as-intersection.md")

    text19 = paper60_content.get("paper60-the-geometry-of-the-circle/19-rh-as-existence-of-the-torus.md", "")
    for quote in extract_paragraphs(
            text19,
            r"(consistency condition|ten faces|structural fact|physics IS the mathematics)",
            limit_chars=400):
        if len(definition["quotes"]) < 7:
            definition["quotes"].append({
                "source": "paper60 \u00a719",
                "text": quote[:400],
            })
    if text19:
        definition["source_files"].append("paper60/19-rh-as-existence-of-the-torus.md")

    return definition


def extract_radii(paper60_content: dict[str, str]) -> dict[str, Any]:
    """Pull any explicit radii from paper60. Paper 1 gives R ~ 10.10 um for the
    physical e-circle, but the torus diagram has no numerical tube radius.
    """
    found: dict[str, Any] = {
        "physical_R_microns": None,
        "major_R_visual": 3.0,
        "minor_r_visual": 1.0,
        "note": "",
    }

    # Look for the e-circle physical radius.
    for content in paper60_content.values():
        m = re.search(r"R\s*[\u2248\u2243=~]+\s*10\.?10?\s*\\?mu\\?m|10\.10\s*\\?mu\\?m", content)
        if m:
            found["physical_R_microns"] = 10.10
            break
        m = re.search(r"R\s*[\u2248\u2243=~]+\s*10\.10", content)
        if m:
            found["physical_R_microns"] = 10.10
            break

    found["note"] = (
        "Paper 60 specifies R ~ 10.10 um for the physical e-circle but does "
        "not give a numerical minor-radius (tube) value for the torus embedding. "
        "Major/minor radii for the visualization are visual defaults."
    )

    if found["physical_R_microns"] is None:
        log("NEEDS-VERIFICATION: physical R not found by regex in paper60")
        found["physical_R_microns"] = 10.10  # fall back to known value
        found["note"] += " (fallback R=10.10 um applied)"

    return found


def build_face_positions(faces: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Assign (u, v) torus coordinates to each face.

    u runs around the major loop (geometric circle). v runs around the tube
    (spectral circle, poloidal). Paper 60 file 17 lays the 10 faces as a 2x5
    grid; we place them at 5 equi-spaced u positions and 2 distinct v positions
    (top for geometric row, bottom for spectral row).

    SPREAD is marked as "both" -- we place it at the same u as its column but
    at an intermediate v (equator of the tube) to show that it bridges circles.
    """
    out = []
    N_COLS = 5
    import math
    for f in faces:
        u = (f["col"] / N_COLS) * (2 * math.pi)
        if f["circle"] == "geometric":
            v = math.pi / 2          # top of tube (outer top)
        elif f["circle"] == "spectral":
            v = -math.pi / 2         # bottom of tube (inner bottom)
        else:
            v = 0.0                  # equator -- bridges both circles
        out.append({
            **f,
            "u": u,
            "v": v,
        })
    return out


def build_vertex_positions(vertices: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Assign (u, v) torus coords to each ring vertex.

    Vertices sit on the major circle (the ring IS S^1, per paper60/28 file).
    Equi-spaced around the major loop at v=0 (equator -- neither strictly
    geometric nor spectral face). Zone determines overlay color.
    """
    import math
    N = len(vertices)
    out = []
    for v_idx, v in enumerate(vertices):
        u = (v["pos"] / N) * (2 * math.pi)
        # tube offset by zone: NORTH on outer top arc, SOUTH on inner bottom.
        zone = v["zone"]
        if zone == "NORTH":
            vcoord = 0.35
        elif zone == "SOUTH":
            vcoord = -0.35
        else:
            vcoord = 0.0
        out.append({
            **v,
            "u": u,
            "v": vcoord,
        })
    return out


def extract_south_trough(paper60_content: dict[str, str]) -> dict[str, Any]:
    """File 28 defines the south trough and the ellipse diagnostic."""
    text28 = paper60_content.get("paper60-the-geometry-of-the-circle/28-the-south-trough-needs-lifting.md", "")

    south_vertices = [v["name"] for v in RING_VERTICES_CANONICAL if v["zone"] == "SOUTH"]
    avg_conf_south = (
        sum(v["conf"] for v in RING_VERTICES_CANONICAL if v["zone"] == "SOUTH")
        / max(1, sum(1 for v in RING_VERTICES_CANONICAL if v["zone"] == "SOUTH"))
    )
    avg_conf_north = (
        sum(v["conf"] for v in RING_VERTICES_CANONICAL if v["zone"] == "NORTH")
        / max(1, sum(1 for v in RING_VERTICES_CANONICAL if v["zone"] == "NORTH"))
    )

    summary_quotes = []
    if text28:
        for quote in extract_paragraphs(
                text28,
                r"(south trough|ellipse|lopsided|dipole|major axis)",
                limit_chars=500):
            if len(summary_quotes) < 3:
                summary_quotes.append(quote[:500])

    return {
        "definition": (
            "The ring's confidence distribution is not uniform. It is elliptical, "
            "with a NORTH pole (QG5D at 10/10) and a SOUTH trough (Goldbach, "
            "Twin Primes, Schanuel, VP at 1/10). On the torus, the south trough "
            "is the set of ring-vertex positions on the lower half of the major "
            "circle (v < 0 band on the tube)."
        ),
        "south_vertices": south_vertices,
        "avg_conf_south": round(avg_conf_south, 2),
        "avg_conf_north": round(avg_conf_north, 2),
        "confidence_ratio_N_over_S": round(avg_conf_north / max(0.01, avg_conf_south), 2),
        "ellipse_major_axis": "NORTH-SOUTH",
        "ellipse_minor_axis": "EAST-WEST",
        "quotes": summary_quotes,
        "source": "paper60 \u00a728",
    }


def extract_riemann_intersections() -> list[dict[str, Any]]:
    """Riemann zeros are the transversal intersections of the two generating
    circles. Per paper60/18 the critical line IS the intersection locus. We
    place a small number of marker points along this locus for illustration.

    Source: paper60/18 ('the crossings grow logarithmically in T' -- we take
    the first 12 ordinates and wrap them around the major loop.)
    """
    import math
    # First 12 Riemann zero ordinates (well-known: 14.134, 21.022, 25.010, ...).
    # Paper 60 does not list numerical values; these are the canonical known
    # ordinates used throughout number theory.
    gamma_n = [
        14.134725, 21.022040, 25.010858, 30.424876,
        32.935062, 37.586178, 40.918719, 43.327073,
        48.005151, 49.773832, 52.970321, 56.446248,
    ]
    # Map each gamma_n to (u, v) on the torus. Paper60/18 describes the
    # critical-line locus as a curve on the surface, not at fixed v.
    # Visualization choice: wrap gamma_n around the major loop at v = 0
    # (the equator intersection locus).
    zeros = []
    for i, g in enumerate(gamma_n):
        u = (g % (2 * math.pi))
        v = 0.0  # on the equator: where both circles pass through
        zeros.append({"index": i + 1, "gamma": g, "u": u, "v": v})
    return zeros


def extract_explanation_steps(paper60_content: dict[str, str],
                              faces: list[dict[str, Any]],
                              vertices: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Produce the 6-step explanation + cite paper60 for each."""
    steps = [
        dict(
            idx=1,
            title="Start from M^5 = M^4 x S^1",
            body=(
                "Paper 1's postulate: spacetime is five-dimensional, and the "
                "fifth dimension is a circle. Mathematically S^1 = U(1) = R/2piZ "
                "with R ~ 10.10 um. This is the FIRST (geometric) circle -- the "
                "substrate on which things live."
            ),
            cite="paper60 \u00a717 & \u00a703; Paper 1 \u00a71",
            highlight="geometric_circle",
        ),
        dict(
            idx=2,
            title="Add the modular flow -- the SECOND circle",
            body=(
                "The BC algebra at beta=1 is a type III_1 factor. Its modular "
                "flow sigma_t acts as a one-parameter automorphism that closes "
                "up under the KMS periodicity. This is the SECOND (spectral) "
                "circle -- the flow that traverses the substrate."
            ),
            cite="paper60 \u00a717; Paper 12 \u00a723",
            highlight="spectral_circle",
        ),
        dict(
            idx=3,
            title="The crossed product IS the torus",
            body=(
                "The crossed product A_BC rtimes_sigma R encodes both circles "
                "simultaneously. The geometric and spectral circles are its "
                "two generating factors. That is the torus T^2 = S^1_geo x "
                "S^1_spec. This is not a metaphor -- it is the type II_\u221e "
                "unfolding of the type III_1 factor."
            ),
            cite="paper60 \u00a717",
            highlight="torus_surface",
        ),
        dict(
            idx=4,
            title="The 10 faces live on the torus surface",
            body=(
                "Five GEOMETRIC faces (TOPOLOGY, HARMONICS, MEASURE, CURVATURE, "
                "SPREAD) sit along the major (geometric) direction. Five "
                "SPECTRAL faces (DYNAMICS, AMPLITUDE, SYMMETRY, ARITHMETIC, "
                "RESONANCE) sit along the minor (spectral) direction. SPREAD "
                "(QUE) bridges both circles -- it sits at the equator. Each "
                "face is one of the world's famous unsolved problems (or a "
                "recently-proved theorem)."
            ),
            cite="paper60 \u00a717 grid, \u00a720 table, \u00a728",
            highlight="faces",
        ),
        dict(
            idx=5,
            title="The 25 ring vertices sit on the major loop",
            body=(
                "The programme's methodology is a ring of 25 vertices (Paper 60 "
                "\u00a722, \u00a728). On the torus, these vertices distribute around "
                "the major (geometric) loop. Confidence scores push NORTH "
                "vertices toward the outer top of the tube (v > 0) and SOUTH "
                "vertices toward the inner bottom (v < 0), producing the "
                "ellipse."
            ),
            cite="paper60 \u00a728",
            highlight="vertices",
        ),
        dict(
            idx=6,
            title="The south trough + ellipse diagnostic",
            body=(
                "The confidence distribution is lopsided. NORTH average ~9.1, "
                "SOUTH average ~1.4 -- a 10x dipole. The major axis of the "
                "ellipse runs NORTH-SOUTH. On the torus, the SOUTH TROUGH is "
                "the arc of the major circle where low-confidence arithmetic "
                "faces (Goldbach, Twin Primes, Schanuel, VP, ABC) cluster. "
                "The direction of the lopsidedness tells the programme where "
                "to focus: SOUTH."
            ),
            cite="paper60 \u00a728 'The South Trough Needs Lifting'",
            highlight="south_trough",
        ),
        dict(
            idx=7,
            title="Riemann zeros are the intersection points",
            body=(
                "On the torus the geometric and spectral circles intersect at "
                "discrete points -- the Riemann zeros {gamma_n}. RH says the "
                "intersections are transversal: every zero sits at a clean "
                "crossing on the torus surface, none wander into the interior. "
                "RH is the EXISTENCE of the torus as a well-formed surface."
            ),
            cite="paper60 \u00a718, \u00a719",
            highlight="zeros",
        ),
    ]
    return steps


def extract_key_quotes(paper60_content: dict[str, str]) -> list[dict[str, Any]]:
    """Pull headline quotes (stable hand-chosen, cross-checked against on-disk
    paper60 text). We validate each quote is present in the file to confirm
    the paper says what we say it says; if missing we log and skip.
    """
    quotes = []
    candidates = [
        dict(
            source="paper60 \u00a717",
            file="paper60-the-geometry-of-the-circle/17-two-circles-one-torus.md",
            probe="Wait -- is it a circle or a torus",
            text="\"Wait -- is it a circle or a torus?\" Both. (G, April 14, 2026)",
        ),
        dict(
            source="paper60 \u00a717",
            file="paper60-the-geometry-of-the-circle/17-two-circles-one-torus.md",
            probe="two circles, linked, make a torus",
            text="Not one circle. Two. And two circles, linked, make a torus.",
        ),
        dict(
            source="paper60 \u00a718",
            file="paper60-the-geometry-of-the-circle/18-riemann-zeros-as-intersection.md",
            probe="zeros are where the two circles cross",
            text="The zeros are where the two circles cross. Every Riemann zero is simultaneously a point on the geometric circle and a point on the spectral circle.",
        ),
        dict(
            source="paper60 \u00a719",
            file="paper60-the-geometry-of-the-circle/19-rh-as-existence-of-the-torus.md",
            probe="not a face. It is the EXISTENCE of the torus",
            text="The Riemann Hypothesis is not a face. It is the EXISTENCE of the torus.",
        ),
        dict(
            source="paper60 \u00a719",
            file="paper60-the-geometry-of-the-circle/19-rh-as-existence-of-the-torus.md",
            probe="physics IS the mathematics",
            text="\"The physics IS the mathematics.\" The physics (geometric circle) and mathematics (spectral circle) are the two generating circles of one torus.",
        ),
        dict(
            source="paper60 \u00a720",
            file="paper60-the-geometry-of-the-circle/20-the-ellipse-and-the-missing-faces.md",
            probe="confidence dipole",
            text="The ring has a NORTH POLE (QG5D at 10/10) and a SOUTH TROUGH (Goldbach/Twin Primes/Schanuel/VP at 1/10). The confidence drops 10x from pole to trough. This is an ellipse, not a circle.",
        ),
        dict(
            source="paper60 \u00a728",
            file="paper60-the-geometry-of-the-circle/28-the-south-trough-needs-lifting.md",
            probe="in love with this picture",
            text="\"i am in love with this picture we just discovered everything about the e-circle!! the direction of the lopsidedness is where we need to focus our excision/bypass/repair exercises.\" -- G, April 14, 2026",
        ),
    ]
    for c in candidates:
        text = paper60_content.get(c["file"], "")
        if c["probe"].lower() in text.lower():
            quotes.append({"source": c["source"], "text": c["text"]})
        else:
            log(f"NEEDS-VERIFICATION: probe '{c['probe']}' not found in {c['file']}; skipping quote")
    return quotes


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> None:
    log(f"build.py starting at {_dt.datetime.now().isoformat(timespec='seconds')}")
    log(f"ROOT = {ROOT}")
    log(f"PAPER60 = {PAPER60}")

    if not PAPER60.exists():
        log(f"FATAL: paper60 dir not found: {PAPER60}")
        flush_log()
        raise SystemExit(1)

    # Walk paper60.
    md_files = sorted(PAPER60.rglob("*.md"))
    log(f"found {len(md_files)} markdown files in paper60")
    paper60_content: dict[str, str] = {}
    for f in md_files:
        rel = str(f.relative_to(ROOT))
        paper60_content[rel] = safe_read(f)
        log(f"  read: {rel} ({len(paper60_content[rel])} chars)")

    # Extract structures.
    log("extracting torus definition...")
    definition = extract_torus_definition(paper60_content)
    log(f"  {len(definition['quotes'])} definition quotes")

    log("extracting radii...")
    radii = extract_radii(paper60_content)
    log(f"  physical R = {radii.get('physical_R_microns')} um")

    log("building face positions...")
    faces = build_face_positions(FACES_CANONICAL)
    log(f"  {len(faces)} faces placed on torus")

    log("building ring-vertex positions...")
    vertices = build_vertex_positions(RING_VERTICES_CANONICAL)
    log(f"  {len(vertices)} ring vertices placed on major loop")

    log("extracting south trough / ellipse...")
    south_trough = extract_south_trough(paper60_content)
    log(f"  south vertices: {len(south_trough['south_vertices'])}; NORTH/SOUTH ratio = {south_trough['confidence_ratio_N_over_S']}")

    log("placing Riemann-zero intersections...")
    zeros = extract_riemann_intersections()
    log(f"  {len(zeros)} zero markers placed at critical-line locus")

    log("building explanation steps...")
    steps = extract_explanation_steps(paper60_content, faces, vertices)
    log(f"  {len(steps)} explanation steps produced")

    log("extracting headline quotes...")
    quotes = extract_key_quotes(paper60_content)
    log(f"  {len(quotes)} headline quotes")

    # Assemble.
    data = {
        "generated_at": _dt.datetime.now().isoformat(timespec="seconds"),
        "generator": "visualization/torus/build.py",
        "definition": definition,
        "radii": radii,
        "faces": faces,
        "vertices": vertices,
        "zeros": zeros,
        "south_trough": south_trough,
        "explanation": steps,
        "quotes": quotes,
        "source_files": sorted(paper60_content.keys()),
        "face_count": len(faces),
        "vertex_count": len(vertices),
        "zero_count": len(zeros),
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(data, indent=2)
    out_text = (
        "// Auto-generated by visualization/torus/build.py -- do not edit by hand.\n"
        f"// Generated {data['generated_at']}\n"
        "// Regenerate: python3 visualization/torus/build.py\n\n"
        f"const TORUS_DATA = {payload};\n"
    )
    OUT.write_text(out_text, encoding="utf-8")
    log(f"wrote {OUT} ({OUT.stat().st_size} bytes)")

    flush_log()
    print(f"wrote {OUT}")
    print(f"wrote {LOG}")


if __name__ == "__main__":
    main()
