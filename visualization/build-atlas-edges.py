#!/usr/bin/env python3
"""Parse atlas cross-cut edges from X-RAY.md files and emit atlas-edges.js."""

import os
import re
import sys
from collections import defaultdict
from datetime import date

ROOT = "/Users/gsix/quantum-geometry-in-5d-latex/strategy/x-ray/proof-chain"
OUTPUT = "/Users/gsix/quantum-geometry-in-5d-latex/visualization/atlas-edges.js"

VERTICES = [
    "qg5d", "ym", "rh", "bsd", "pvnp", "hodge", "ns", "grh", "bgs",
    "baum-connes", "katz-sarnak", "goldbach", "twin-primes", "cramer",
    "lindelof", "h12", "turbulence", "vp-vs-vnp", "abc", "opn",
    "collatz", "lehmer", "sato-tate", "schanuel", "hilbert-6",
]
VERTEX_SET = set(VERTICES)

# Aliases/normalizations for references found in the text.
ALIAS = {
    "paper13-rh": "rh",
    "paper08-yang-mills": "ym",
    "paper26-bsd": "bsd",
    "paper28-pvnp": "pvnp",
    "paper29-hodge": "hodge",
    "paper30-navier-stokes": "ns",
    "paper30-ns": "ns",
    "paper30": "ns",
    "paper31-baum-connes": "baum-connes",
    "paper32-bgs": "bgs",
    "paper32-bgs-spectral-statistics": "bgs",
    "paper33-goldbach": "goldbach",
    "paper34-twin-primes": "twin-primes",
    "paper35-schanuel": "schanuel",
    "paper36-hilbert-6": "hilbert-6",
    "paper37-abc": "abc",
    "paper38-turbulence": "turbulence",
    "paper39-vp-vs-vnp": "vp-vs-vnp",
    "paper40-odd-perfect": "opn",
    "paper40-opn": "opn",
    "paper41-collatz": "collatz",
    "paper42-lehmer": "lehmer",
    "paper43-cramer": "cramer",
    "paper44-sato-tate": "sato-tate",
    "paper45-lindelof": "lindelof",
    "paper46-katz-sarnak": "katz-sarnak",
    "paper25-hilbert-12": "h12",
    "paper13b-grh": "grh",
    "paper13b": "grh",
    "paper08": "ym",
    "paper13": "rh",
    "paper26": "bsd",
    "paper28": "pvnp",
    "paper29": "hodge",
    "paper31": "baum-connes",
    "paper32": "bgs",
    "paper33": "goldbach",
    "paper34": "twin-primes",
    "paper35": "schanuel",
    "paper36": "hilbert-6",
    "paper37": "abc",
    "paper38": "turbulence",
    "paper39": "vp-vs-vnp",
    "paper40": "opn",
    "paper41": "collatz",
    "paper42": "lehmer",
    "paper43": "cramer",
    "paper44": "sato-tate",
    "paper45": "lindelof",
    "paper46": "katz-sarnak",
    "paper25": "h12",
    "hilbert6": "hilbert-6",
    "hilbert-12": "h12",
    "hilbert12": "h12",
    "baum_connes": "baum-connes",
    "baumconnes": "baum-connes",
    "katz_sarnak": "katz-sarnak",
    "katzsarnak": "katz-sarnak",
    "satotate": "sato-tate",
    "sato_tate": "sato-tate",
    "twinprimes": "twin-primes",
    "twin_primes": "twin-primes",
    "vpvsvnp": "vp-vs-vnp",
    "vp_vs_vnp": "vp-vs-vnp",
    "odd-perfect": "opn",
    "oddperfect": "opn",
    "odd_perfect": "opn",
    "navier-stokes": "ns",
    "navierstokes": "ns",
    "lindeloef": "lindelof",
    "lindeloef": "lindelof",
    "lindelöf": "lindelof",
    "cramér": "cramer",
    "riemann": "rh",
    "bsd-for-cm-curves": "bsd",
    "hub": "qg5d",
}

# Non-ring / drop targets (substrings to ignore when tokenizing references).
DROP_PATTERNS = [
    r"^branch\s+[a-e]\b",
    r"^branch[a-e]\b",
    r"^literature",
    r"^selberg",
    r"^speculative$",
    r"^open$",
    r"^kk$",
    r"^ccm$",
    r"^boegli",
    r"^bögli",
    r"^connes",
    r"^rmt$",
    r"^weitzenb",
    r"^popa",
    r"^taylor",
    r"^ha-paugam",
    r"^bratteli",
    r"^laca",
    r"^kolyvagin",
    r"^deligne",
    r"^hecke$",
    r"^gaitsgory",
    r"^kapustin",
    r"^bulatov",
    r"^schaefer",
    r"^marrakchi",
    r"^feldman",
    r"^houdayer",
    r"^hilbert(?:'s)?\s*\d+",  # Hilbert's <n> in prose, not our vertex id
]
DROP_RE = [re.compile(p, re.I) for p in DROP_PATTERNS]


def normalize_vertex(tok: str) -> str | None:
    """Map a raw token to a canonical vertex id, or return None if not a ring vertex."""
    if not tok:
        return None
    t = tok.strip().lower()
    t = t.replace("ö", "o").replace("é", "e")
    # Strip trailing punctuation / parens
    t = t.strip(" :;,.()[]{}\"'/")
    # Strip markdown emphasis
    t = t.replace("**", "").replace("*", "").replace("`", "").strip()
    # Strip latex
    t = re.sub(r"\$[^$]*\$", "", t)
    t = t.strip(" :;,.()[]{}\"'/")
    if not t:
        return None
    if t in VERTEX_SET:
        return t
    if t in ALIAS:
        return ALIAS[t]
    # try without trailing 's', etc
    if t.endswith("s") and t[:-1] in VERTEX_SET:
        return t[:-1]
    for pat in DROP_RE:
        if pat.search(t):
            return None
    return None


def parse_layer_label(layer_token: str) -> str | None:
    """Take a snippet like 'L3' or 'L_BC' or 'CP-1' or 'S1' or 'L14' and return it as-is (cleaned)."""
    if not layer_token:
        return None
    t = layer_token.strip()
    t = t.strip(" :;,.()[]{}\"'/")
    # Keep only leading alphanumeric + dashes/underscores
    m = re.match(r"^[A-Za-z0-9_\-]{1,40}", t)
    if not m:
        return None
    return m.group(0)


def extract_shared_from_em(source_layer: str, body: str) -> str:
    """Extract the shared-invariant phrase from the em-dash body of a bullet edge."""
    # Expected pattern: "— shared X, Y (Z)." possibly followed by hints.
    body = body.strip()
    # Strip leading em or hyphen
    body = body.lstrip("—-– ").strip()
    # Take up to first sentence delimiter
    m = re.match(r"([^.;]+)", body)
    return (m.group(1) if m else body).strip()


def collect_edges_bullet(text: str, src: str) -> list:
    """Parse YM-style bullet format:
       - **L1 ↔ rh:L3** — shared X, Y (extra).
       - **L1 ↔ lehmer:L_top** — shared face-only ...
       Also multi-target like 'ym:L16, ym:L17' or 'goldbach:L_Euler / twin-primes:L_Euler'.
    """
    edges = []
    # Match bullets that start with **<left> ↔ <right>** — <body>
    # Accept either a plain `- **...**` or a `- **...** —` (sometimes dash is outside bold).
    bullet_re = re.compile(
        r"^-\s+\*\*([^*]+?)\*\*\s*(?:—|-)?\s*(.*?)(?=\n-\s|\n\n|\Z)",
        re.S | re.M,
    )
    for m in bullet_re.finditer(text):
        head = m.group(1).strip()
        body = m.group(2).strip()
        if "↔" not in head:
            continue
        # Split head on ↔
        parts = head.split("↔")
        if len(parts) != 2:
            continue
        left_raw = parts[0].strip()
        right_raw = parts[1].strip()
        # LEFT side: could be "L1" or "CP-1" or "L1, L1b" etc. Left side = source layer(s) in the current file.
        left_layer = parse_layer_label(left_raw.split()[0]) if left_raw else None
        # RIGHT side: targets. Parse out `<vertex>:<layer>` pairs, possibly separated by /, ,, ;, or "and"
        # Also parse "vertex:LabelA, vertex:LabelB".
        # Tokenize: find all runs of <word>:<layer> OR just <word> (vertex-only).
        # Also accept "vertex (annotation)" as a vertex-only reference.
        targets = []
        # First, strip any parenthetical note at end of right_raw.
        right_stripped = re.sub(r"\([^)]*\)\s*$", "", right_raw).strip()
        # Split on / , ;  — these commonly separate multiple targets in the same head.
        # But keep ":" intact.
        sub_parts = re.split(r"\s*[/,;]\s*|\s+or\s+", right_stripped)
        for sub in sub_parts:
            sub = sub.strip()
            if not sub:
                continue
            # Remove leading labels like "ym " or "rh " when colon-syntax is used
            # Pattern: vertex[:layer]
            mv = re.match(r"^([A-Za-z][A-Za-z0-9_\-]*)\s*(?::\s*([A-Za-z0-9_\-]+))?", sub)
            if not mv:
                continue
            tgt = normalize_vertex(mv.group(1))
            tgt_layer = mv.group(2) if mv.lastindex and mv.lastindex >= 2 else None
            if tgt:
                targets.append((tgt, tgt_layer))
        if not targets:
            continue
        shared = extract_shared_from_em(left_layer or "", body)
        # Clean shared of markdown, remove leading "shared "
        shared = re.sub(r"^\s*shared\s+", "", shared, flags=re.I)
        shared = re.sub(r"\s*\(PRIMARY.*?\)\s*$", "", shared, flags=re.I)
        shared = re.sub(r"\s*\(load-bearing.*?\)\s*$", "", shared, flags=re.I)
        shared = shared.strip(" .,;")
        for tgt, _ in targets:
            if tgt == src:
                continue
            edges.append({"from": src, "to": tgt, "shared": shared, "src_layer": left_layer})
    return edges


def collect_edges_inline_crosscuts(text: str, src: str) -> list:
    """Parse hodge/ns-style inline per-layer 'Cross-cuts: A (r1), B (r2), ...' bullets."""
    edges = []
    line_re = re.compile(
        r"^- \*\*Cross-cuts\*\*:\s*(.+?)(?=\n(?:-\s\*\*|\n|###|##)|\Z)",
        re.M | re.S,
    )
    for m in line_re.finditer(text):
        body = m.group(1).strip()
        # Split at commas that sit at paren-depth 0
        items = []
        depth = 0
        buf = []
        for ch in body:
            if ch in "([{":
                depth += 1
                buf.append(ch)
            elif ch in ")]}":
                depth = max(0, depth - 1)
                buf.append(ch)
            elif ch == "," and depth == 0:
                items.append("".join(buf).strip())
                buf = []
            else:
                buf.append(ch)
        if buf:
            items.append("".join(buf).strip())

        for itm in items:
            # Each item: "<vertex>[:<layer>] (<reason>)" or just "<vertex>"
            itm = itm.strip().strip(".")
            if not itm:
                continue
            mv = re.match(r"^([A-Za-z][A-Za-z0-9_\-]*)(?::\s*([A-Za-z0-9_\-/]+))?(?:\s*\(([^)]*)\))?", itm)
            if not mv:
                continue
            tgt = normalize_vertex(mv.group(1))
            reason = mv.group(3) or ""
            if not tgt or tgt == src:
                continue
            # Clean reason
            reason = reason.strip()
            shared = reason[:80] if reason else "(unspecified)"
            edges.append({"from": src, "to": tgt, "shared": shared})
    return edges


def collect_edges_qg5d_outbound(text: str, src: str) -> list:
    """Parse qg5d's **[N] to: <vertex>** style outbound section.

    Format:
      **[1] to: ym (Paper 8 — Yang-Mills Mass Gap)**
      - via-projection: ...
      - shared-invariant: ...
    One edge per target (24 expected); shared-invariant is the combined list.
    """
    edges = []
    hdr_re = re.compile(
        r"^\*\*\[\d+\]\s+to:\s+([A-Za-z0-9\-]+)[^\n]*\*\*\s*\n(.*?)(?=^\*\*\[\d+\]\s+to:|^---|\Z)",
        re.S | re.M,
    )
    for m in hdr_re.finditer(text):
        raw_tgt = m.group(1)
        tgt = normalize_vertex(raw_tgt)
        block = m.group(2)
        if not tgt or tgt == src:
            continue
        sh_m = re.search(r"^\s*-\s+shared-invariant:\s*(.+?)$", block, re.M)
        if sh_m:
            shared_line = sh_m.group(1).strip()
            # Clean load-bearing / background parentheticals
            shared_line = re.sub(r"\s*\(load-bearing[^)]*\)", "", shared_line, flags=re.I)
            shared_line = re.sub(r"\s*\(background[^)]*\)", "", shared_line, flags=re.I)
            # Truncate overly long
            shared_line = shared_line.strip(" .;,")
            edges.append({"from": src, "to": tgt, "shared": shared_line})
        else:
            edges.append({"from": src, "to": tgt, "shared": "(outbound)"})
    return edges


def canonicalize(edge):
    a, b = edge["from"], edge["to"]
    if a > b:
        a, b = b, a
    return (a, b, edge.get("shared", "").lower())


def main():
    all_edges = []
    per_vertex_raw = defaultdict(int)
    failed = []

    for v in VERTICES:
        path = os.path.join(ROOT, v, "X-RAY.md")
        if not os.path.exists(path):
            failed.append((v, "missing"))
            continue
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        edges_here = []
        if v == "qg5d":
            edges_here = collect_edges_qg5d_outbound(text, v)
        else:
            e1 = collect_edges_bullet(text, v)
            # If the bullet list yielded substantial edges, don't also parse per-layer inline
            # Cross-cuts (which are largely redundant with the §7 Cross-Cut Map bullets).
            # Only fall back to inline parsing if bullet parse produced very few edges.
            if len(e1) >= 10:
                edges_here = e1
            else:
                e2 = collect_edges_inline_crosscuts(text, v)
                edges_here = e1 + e2
        per_vertex_raw[v] = len(edges_here)
        all_edges.extend(edges_here)
        if len(edges_here) == 0:
            failed.append((v, "no edges parsed"))

    # Deduplicate: canonicalize endpoints alphabetically; drop exact dups of (A,B,shared).
    # Per user spec: "If multiple edges exist between the same pair with different
    # invariants, keep them all as distinct entries." So we preserve multiplicity.
    # But we also normalize 'shared' phrases a bit to merge near-duplicates.
    def normalize_shared(s: str) -> str:
        s = (s or "").strip()
        s = re.sub(r"\s+", " ", s)
        # Strip trailing parenthetical hints ("(PRIMARY EDGE)", etc.)
        s = re.sub(r"\s*\(\s*PRIMARY[^)]*\)\s*$", "", s, flags=re.I)
        s = re.sub(r"\s*\(\s*load-bearing[^)]*\)", "", s, flags=re.I)
        s = re.sub(r"\s*\(\s*background[^)]*\)", "", s, flags=re.I)
        s = s.strip(" .,;")
        return s

    seen_triples = set()
    unique = []
    counts = defaultdict(int)
    for e in all_edges:
        a, b = e["from"], e["to"]
        if a not in VERTEX_SET or b not in VERTEX_SET:
            continue
        if a == b:
            continue
        if a > b:
            a, b = b, a
        shared = normalize_shared(e.get("shared", ""))
        key = (a, b, shared.lower())
        if key in seen_triples:
            continue
        seen_triples.add(key)
        unique.append({"from": a, "to": b, "shared": shared})
        counts[a] += 1
        counts[b] += 1
    # Stable sort for diff-friendly output
    unique.sort(key=lambda e: (e["from"], e["to"], e["shared"]))

    distinct_pairs = defaultdict(set)
    for e in unique:
        distinct_pairs[e["from"]].add(e["to"])
        distinct_pairs[e["to"]].add(e["from"])

    # Emit JS
    today = date.today().isoformat()
    lines = []
    lines.append("// Atlas cross-cut edges — aggregated from all 25 X-RAY.md files + qg5d hub.")
    lines.append(f"// Generated {today} from strategy/x-ray/proof-chain/*/X-RAY.md §4/§7 enumerations.")
    lines.append("// Format: [{from, to, shared}]")
    lines.append("// Edge orientation is alphabetical-low→alphabetical-high; (A,B) == (B,A) in the chord graph.")
    lines.append("")
    lines.append(f"// Stats: {len(unique)} unique edges across {len(VERTICES)} vertices.")
    lines.append("")
    lines.append("const ATLAS_EDGES = [")
    for e in unique:
        shared = (e["shared"] or "").replace("\\", "\\\\").replace('"', '\\"')
        # Trim shared to something readable
        if len(shared) > 140:
            shared = shared[:137] + "..."
        lines.append(f'  {{from:"{e["from"]}", to:"{e["to"]}", shared:"{shared}"}},')
    lines.append("];")
    lines.append("")
    lines.append("// Per-vertex cross-cut counts (unique edge endpoints, counted once per edge).")
    lines.append("const ATLAS_COUNTS = {")
    for v in VERTICES:
        lines.append(f'  "{v}": {counts.get(v, 0)},')
    lines.append("};")
    lines.append("")
    lines.append("// Per-vertex distinct neighbour counts.")
    lines.append("const ATLAS_NEIGHBOURS = {")
    for v in VERTICES:
        lines.append(f'  "{v}": {len(distinct_pairs.get(v, set()))},')
    lines.append("};")
    lines.append("")
    lines.append("if (typeof window !== 'undefined') {")
    lines.append("  window.ATLAS_EDGES = ATLAS_EDGES;")
    lines.append("  window.ATLAS_COUNTS = ATLAS_COUNTS;")
    lines.append("  window.ATLAS_NEIGHBOURS = ATLAS_NEIGHBOURS;")
    lines.append("}")
    lines.append("")

    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    # Report
    print(f"Wrote {OUTPUT}")
    print(f"Files parsed: {len(VERTICES) - len([f for f in failed if f[1] == 'missing'])}/{len(VERTICES)}")
    print(f"Raw edges extracted: {len(all_edges)}")
    print(f"Unique edges after dedup: {len(unique)}")
    print()
    print("Per-vertex raw edges found:")
    for v in VERTICES:
        print(f"  {v:15s} {per_vertex_raw.get(v, 0):3d} raw")
    print()
    print("Top 10 highest-connectivity vertices (by endpoint count in unique set):")
    top = sorted(counts.items(), key=lambda x: -x[1])[:10]
    for v, c in top:
        print(f"  {v:15s} {c:3d}")
    print()
    if failed:
        print("Failed / empty:")
        for v, why in failed:
            print(f"  {v}: {why}")


if __name__ == "__main__":
    main()
