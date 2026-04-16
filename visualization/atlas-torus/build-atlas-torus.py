#!/usr/bin/env python3
"""
build-atlas-torus.py — Parse X-RAY.md files and atlas-edges.js
to generate atlas-torus-data.js for the Atlas Torus Proof-Chain Composer.

Usage:
    cd /Users/gsix/quantum-geometry-in-5d-latex
    python3 visualization/atlas-torus/build-atlas-torus.py
"""

import os, re, json, math, sys
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
XRAY_DIR = os.path.join(ROOT, "strategy", "x-ray", "proof-chain")
EDGES_FILE = os.path.join(ROOT, "visualization", "atlas-edges.js")
OUT_FILE = os.path.join(ROOT, "visualization", "atlas-torus", "atlas-torus-data.js")

# Ordered vertex list (canonical order for torus placement)
VERTEX_ORDER = [
    "ym", "rh", "bsd", "pvnp", "hodge", "ns", "lindelof", "grh",
    "h12", "turbulence", "baum-connes", "vp-vs-vnp", "bgs",
    "katz-sarnak", "twin-primes", "cramer", "goldbach", "abc",
    "opn", "collatz", "lehmer", "sato-tate", "schanuel",
    "hilbert-6", "qg5d"
]

VERTEX_LABELS = {
    "ym": "YM", "rh": "RH", "bsd": "BSD", "pvnp": "PvNP",
    "hodge": "Hodge", "ns": "NS", "lindelof": "Lindelof", "grh": "GRH",
    "h12": "H12", "turbulence": "Turbulence", "baum-connes": "Baum-Connes",
    "vp-vs-vnp": "VP-vs-VNP", "bgs": "BGS", "katz-sarnak": "Katz-Sarnak",
    "twin-primes": "Twin Primes", "cramer": "Cramer", "goldbach": "Goldbach",
    "abc": "ABC", "opn": "OPN", "collatz": "Collatz", "lehmer": "Lehmer",
    "sato-tate": "Sato-Tate", "schanuel": "Schanuel",
    "hilbert-6": "Hilbert-6", "qg5d": "Integers"
}

# Known external / literature sources (for classification)
EXTERNAL_SOURCES = [
    "balaban", "bost-connes", "kolyvagin", "ccm", "connes",
    "deligne", "wiles", "taylor", "gross-zagier", "birch",
    "langlands", "serre", "artin", "tate", "milnor",
    "atiyah-singer", "perelman", "lindenstrauss",
    "arXiv:2511.22755", "cmp 109", "cmp 119", "cmp 95",
    "luscher", "teschl", "boegli", "davis-kahan",
    "rellich", "ax 1971", "hermite", "lindemann",
    "slepian", "hurwitz", "selberg", "montgomery",
    "rubinstein", "iwaniec", "bombieri", "helfgott",
    "goldston-pintz-yildirim", "maynard", "zhang",
    "bulatov", "zhuk", "popa", "von neumann",
    "osterwalder-schrader", "wightman", "haag",
]

# Torus geometry
R_MAJOR = 3.0
R_MINOR = 1.2

def torus_xyz(u, v):
    """Compute 3D coordinates on the torus surface."""
    x = (R_MAJOR + R_MINOR * math.cos(v)) * math.cos(u)
    y = (R_MAJOR + R_MINOR * math.cos(v)) * math.sin(u)
    z = R_MINOR * math.sin(v)
    return (round(x, 4), round(y, 4), round(z, 4))


def classify_node(status, source, vertex_id):
    """Classify a node based on its status and source."""
    status_upper = status.upper().strip()
    source_lower = source.lower() if source else ""

    # OPEN / CONJECTURED
    if any(s in status_upper for s in ["OPEN", "CONJECTURED"]):
        return "open"

    # EXTERNAL / CONDITIONAL on external
    if "CONDITIONAL" in status_upper or "EXTERNAL" in status_upper:
        return "external"

    # QED is integers-original
    if "QED" in status_upper:
        return "integers-original"

    # LITERATURE / KNOWN / ESTABLISHED / CLASSICAL
    if any(s in status_upper for s in ["LITERATURE", "KNOWN", "ESTABLISHED", "CLASSICAL"]):
        # Check if it's classical (pre-1950)
        classical_markers = [
            "hermite", "lindemann", "weierstrass", "euler",
            "gauss", "riemann 1859", "dirichlet", "hadamard",
            "poussin", "hilbert", "minkowski", "noether",
            "schur", "burnside", "sylow", "cauchy",
            "1882", "1885", "1896", "1837", "1859"
        ]
        if any(m in source_lower for m in classical_markers):
            return "classical"
        return "literature"

    # PROVED — check if integers-original
    if "PROVED" in status_upper or "THEOREM" in status_upper or "LEMMA" in status_upper:
        # Check if source references a programme paper
        paper_match = re.search(r'paper\s*(\d+)', source_lower)
        if paper_match:
            return "integers-original"
        # Check for known external sources
        for ext in EXTERNAL_SOURCES:
            if ext.lower() in source_lower:
                return "literature"
        # Default PROVED without clear external source = integers-original
        return "integers-original"

    # Fallback
    return "literature"


def parse_xray(vertex_id):
    """Parse a single X-RAY.md file and extract layers + cross-cuts."""
    filepath = os.path.join(XRAY_DIR, vertex_id, "X-RAY.md")
    if not os.path.exists(filepath):
        print(f"  WARNING: {filepath} not found, skipping {vertex_id}")
        return [], [], None

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    layers = []
    cross_cuts = []
    primary_face = None

    # Extract primary face from §1 Header
    # Handle both **Primary face**: CURVATURE and **Primary face**: **SYMMETRY**
    face_match = re.search(r'\*\*Primary face\*\*:\s*\**(\w+)\**', content)
    if face_match:
        primary_face = face_match.group(1).upper()

    # ---- Parse layers from §3 (Layer-by-Layer) and §2 (ASCII diagram) ----
    # Strategy: parse the ASCII diagram in §2 for layer entries, then
    # enrich with §3 detailed sections.

    # First, extract from the ASCII diagram (most reliable for layer IDs + status)
    diagram_match = re.search(r'## §2 ASCII Diagram.*?```(.*?)```', content, re.DOTALL)
    diagram_layers = {}
    if diagram_match:
        diagram_text = diagram_match.group(1)
        # Match lines like: ├── L1: description  [STATUS]
        # or: └── L18: description [CONDITIONAL on H4 — W1]
        # or: ├── S1: description  [PROVED]
        # or: ├── T1: ... [PROVED]  (qg5d uses T_k for root theorems)
        layer_pattern = re.compile(
            r'[├└─│\s]*(?:──\s+)?(L\d+[a-z]?|S\d+|T\d+|CP-\d+|W_\w+)\s*[:]\s*(.*?)\s*\[(.*?)\]',
            re.IGNORECASE
        )
        for m in layer_pattern.finditer(diagram_text):
            lid = m.group(1).strip()
            name = m.group(2).strip()
            status = m.group(3).strip()
            # Clean up name
            name = re.sub(r'\s+', ' ', name)
            if len(name) > 80:
                name = name[:77] + "..."
            diagram_layers[lid] = {"name": name, "status": status}

    # Now parse §3 sections for detailed metadata
    # Look for ### L1 — ... or ### T1 — ... or #### A.1 — ... or #### D.B1 — ... pattern
    # Uses #{3,4} to match both ### and #### heading levels
    # Layer ID patterns: L1, L1b, S1, T1, A.1, B.10, B.KK-gap, B.grad, D.B1, C.13, etc.
    section_pattern = re.compile(
        r'#{3,4}\s+(L\d+[a-z]?|S\d+|T\d+|[A-D]\.\d+|[A-D]\.\w[\w-]*|[A-D]\.B\d+)\s*(?:—|–|-)\s*(.*?)(?:\n)(.*?)(?=\n#{3,4}\s+(?:L\d|S\d|T\d|[A-D]\.|Branch)|\n## §|\n---\n|\Z)',
        re.DOTALL
    )

    for m in section_pattern.finditer(content):
        lid = m.group(1).strip()
        section_name = m.group(2).strip()
        section_body = m.group(3)

        # Extract fields from the section body
        status_match = re.search(r'\*\*Status\*\*:\s*(.*?)(?:\n|\*)', section_body)
        source_match = re.search(r'\*\*Source\*\*:\s*(.*?)(?:\n\n|\n\*\*|\n####)', section_body, re.DOTALL)
        face_match2 = re.search(r'\*\*Face\*\*:\s*(\w+)', section_body)
        proj_match = re.search(r'\*\*Projection\*\*:\s*\$?(P_\w+)\$?', section_body)
        pattern_match = re.search(r'\*\*Pattern\*\*:\s*(P\d+)', section_body)
        invariant_match = re.search(r'\*\*Invariant preserved\*\*:\s*(.*?)(?:\n|$)', section_body)
        crosscut_match = re.search(r'\*\*Cross-cuts\*\*:\s*(.*?)(?:\n|$)', section_body)

        status = status_match.group(1).strip() if status_match else ""
        source = source_match.group(1).strip().replace('\n', ' ') if source_match else ""
        face = face_match2.group(1).upper() if face_match2 else ""
        projection = proj_match.group(1) if proj_match else ""
        pattern = pattern_match.group(1) if pattern_match else ""
        invariant_raw = invariant_match.group(1).strip() if invariant_match else ""
        # Take first invariant (before comma or parenthetical)
        invariant = re.split(r'[,(]', invariant_raw)[0].strip() if invariant_raw else ""

        # Simplify status
        status_simple = status.upper()
        for tag in ["PROVED", "LITERATURE", "EXTERNAL", "CONDITIONAL", "OPEN",
                     "CONJECTURED", "KNOWN", "ESTABLISHED", "CLASSICAL", "QED"]:
            if tag in status_simple:
                status_simple = tag
                break
        else:
            # Check diagram layers for fallback
            if lid in diagram_layers:
                ds = diagram_layers[lid]["status"].upper()
                for tag in ["PROVED", "LITERATURE", "EXTERNAL", "CONDITIONAL", "OPEN",
                            "CONJECTURED", "KNOWN", "ESTABLISHED", "CLASSICAL", "QED"]:
                    if tag in ds:
                        status_simple = tag
                        break

        # Use diagram name if section name is too short
        name = section_name
        if lid in diagram_layers and len(diagram_layers[lid]["name"]) > len(name):
            name = diagram_layers[lid]["name"]
        if not name and lid in diagram_layers:
            name = diagram_layers[lid]["name"]

        # Source citation (compact)
        source_cite = source
        if len(source_cite) > 100:
            source_cite = source_cite[:97] + "..."

        classification = classify_node(status_simple, source, vertex_id)

        layers.append({
            "layer": lid,
            "name": name,
            "status": status_simple,
            "face": face,
            "projection": projection,
            "pattern": pattern,
            "invariant": invariant,
            "source": source_cite,
            "classification": classification,
        })

    # If §3 parsing found nothing, fall back to diagram layers
    if not layers and diagram_layers:
        for lid, info in diagram_layers.items():
            status_simple = info["status"].upper()
            for tag in ["PROVED", "LITERATURE", "EXTERNAL", "CONDITIONAL", "OPEN",
                        "CONJECTURED", "KNOWN", "ESTABLISHED", "CLASSICAL", "QED"]:
                if tag in status_simple:
                    status_simple = tag
                    break
            classification = classify_node(status_simple, "", vertex_id)
            layers.append({
                "layer": lid,
                "name": info["name"],
                "status": status_simple,
                "face": "",
                "projection": "",
                "pattern": "",
                "invariant": "",
                "source": "",
                "classification": classification,
            })

    # ---- Parse cross-cuts from §7 ----
    crosscut_section = re.search(r'## §7 Cross-Cut Map(.*?)(?=\n## §|\Z)', content, re.DOTALL)
    if crosscut_section:
        body = crosscut_section.group(1)
        # Look for bullet entries like: - **L1 ↔ qg5d:Branch B** — shared spectral gap.
        # or: - **L1 ↔ pvnp:L_gap** — shared spectral gap.
        cc_pattern = re.compile(
            r'-\s*\*\*(L\d+[a-z]?|S\d+)\s*(?:↔|<->|to)\s*(\w[\w-]*):?(\w*)\*\*\s*(?:—|–|-)\s*(?:shared\s+)?(.*?)(?:\n\s*-\s*Reason|\n\s*-\s*Trans|\n\n|\n-\s*\*\*)',
            re.DOTALL
        )
        for m in cc_pattern.finditer(body):
            from_layer = m.group(1).strip()
            to_vertex = m.group(2).strip()
            to_layer = m.group(3).strip() if m.group(3) else ""
            shared = m.group(4).strip().rstrip('.')
            if len(shared) > 80:
                shared = shared[:77] + "..."

            from_id = f"{vertex_id}-{from_layer}"
            to_id = f"{to_vertex}-{to_layer}" if to_layer else to_vertex

            cross_cuts.append({
                "from": from_id,
                "to": to_id,
                "shared": shared,
                "type": "cross-cut"
            })

    return layers, cross_cuts, primary_face


def parse_atlas_edges():
    """Parse atlas-edges.js to extract vertex-level edges."""
    if not os.path.exists(EDGES_FILE):
        print(f"  WARNING: {EDGES_FILE} not found, skipping atlas edges")
        return []

    with open(EDGES_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    edges = []
    pattern = re.compile(
        r'\{from:"([\w-]+)",\s*to:"([\w-]+)",\s*shared:"(.*?)"\}'
    )
    for m in pattern.finditer(content):
        edges.append({
            "from": m.group(1),
            "to": m.group(2),
            "shared": m.group(3),
        })
    return edges


def main():
    print("=== Atlas Torus Data Builder ===")
    print(f"Root: {ROOT}")
    print(f"X-RAY dir: {XRAY_DIR}")
    print()

    all_nodes = []
    all_edges = []
    all_vertices = []
    warnings = []

    vertex_count = len(VERTEX_ORDER)

    for vi, vertex_id in enumerate(VERTEX_ORDER):
        print(f"Parsing {vertex_id}...")
        try:
            layers, cross_cuts, primary_face = parse_xray(vertex_id)
        except Exception as e:
            warnings.append(f"{vertex_id}: parse error: {e}")
            print(f"  ERROR: {e}")
            layers, cross_cuts, primary_face = [], [], None

        if not layers:
            warnings.append(f"{vertex_id}: no layers extracted")
            print(f"  WARNING: no layers extracted for {vertex_id}")
            # Create a placeholder node
            u_val = vi / vertex_count * 2 * math.pi
            x, y, z = torus_xyz(u_val, 0)
            all_nodes.append({
                "id": f"{vertex_id}-L0",
                "vertex": vertex_id,
                "layer": "L0",
                "name": f"{VERTEX_LABELS.get(vertex_id, vertex_id)} (no data)",
                "status": "OPEN",
                "face": primary_face or "",
                "projection": "",
                "pattern": "",
                "invariant": "",
                "source": "",
                "classification": "open",
                "u": round(u_val, 4),
                "v": 0,
                "x": x, "y": y, "z": z
            })
            all_vertices.append({
                "id": vertex_id,
                "label": VERTEX_LABELS.get(vertex_id, vertex_id),
                "layers": ["L0"],
                "u": round(u_val, 4),
                "primaryFace": primary_face or ""
            })
            continue

        # Compute torus coordinates
        u_val = vi / vertex_count * 2 * math.pi
        layer_count = len(layers)
        layer_ids = []

        for li, layer in enumerate(layers):
            v_val = li / max(layer_count, 1) * 2 * math.pi
            x, y, z = torus_xyz(u_val, v_val)

            node_id = f"{vertex_id}-{layer['layer']}"
            layer_ids.append(layer['layer'])

            all_nodes.append({
                "id": node_id,
                "vertex": vertex_id,
                "layer": layer["layer"],
                "name": layer["name"],
                "status": layer["status"],
                "face": layer["face"],
                "projection": layer["projection"],
                "pattern": layer["pattern"],
                "invariant": layer["invariant"],
                "source": layer["source"],
                "classification": layer["classification"],
                "u": round(u_val, 4),
                "v": round(v_val, 4),
                "x": x, "y": y, "z": z
            })

        # Intra-chain edges (sequential layers)
        for li in range(len(layers) - 1):
            from_id = f"{vertex_id}-{layers[li]['layer']}"
            to_id = f"{vertex_id}-{layers[li+1]['layer']}"
            all_edges.append({
                "from": from_id,
                "to": to_id,
                "shared": "intra-chain",
                "type": "intra-chain"
            })

        # Cross-cut edges
        all_edges.extend(cross_cuts)

        all_vertices.append({
            "id": vertex_id,
            "label": VERTEX_LABELS.get(vertex_id, vertex_id),
            "layers": layer_ids,
            "u": round(u_val, 4),
            "primaryFace": primary_face or ""
        })

        print(f"  {len(layers)} layers, {len(cross_cuts)} cross-cuts, face={primary_face}")

    # Parse atlas edges (vertex-level supplementary)
    atlas_edges = parse_atlas_edges()
    print(f"\nAtlas edges loaded: {len(atlas_edges)} vertex-level edges")

    # Deduplicate edges
    edge_set = set()
    unique_edges = []
    for e in all_edges:
        key = (e["from"], e["to"], e.get("type", ""))
        rkey = (e["to"], e["from"], e.get("type", ""))
        if key not in edge_set and rkey not in edge_set:
            edge_set.add(key)
            unique_edges.append(e)
    all_edges = unique_edges

    # Count classifications
    counts = {}
    for n in all_nodes:
        c = n["classification"]
        counts[c] = counts.get(c, 0) + 1

    meta = {
        "nodeCount": len(all_nodes),
        "edgeCount": len(all_edges),
        "integersOriginalCount": counts.get("integers-original", 0),
        "literatureCount": counts.get("literature", 0),
        "externalCount": counts.get("external", 0),
        "classicalCount": counts.get("classical", 0),
        "openCount": counts.get("open", 0),
        "vertexCount": len(all_vertices),
        "atlasEdgeCount": len(atlas_edges),
        "buildTimestamp": datetime.now(timezone.utc).isoformat(),
    }

    # ---- Emit JS ----
    def js_str(s):
        """Escape string for JS."""
        return s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ")

    lines = []
    lines.append("// Atlas Torus Data — generated from strategy/x-ray/proof-chain/*/X-RAY.md")
    lines.append("// Build: python3 visualization/atlas-torus/build-atlas-torus.py")
    lines.append(f"// Generated: {meta['buildTimestamp']}")
    lines.append("")

    # TORUS_NODES
    lines.append("const TORUS_NODES = [")
    for n in all_nodes:
        lines.append('  {' + ', '.join([
            f'id:"{js_str(n["id"])}"',
            f'vertex:"{js_str(n["vertex"])}"',
            f'layer:"{js_str(n["layer"])}"',
            f'name:"{js_str(n["name"])}"',
            f'status:"{js_str(n["status"])}"',
            f'face:"{js_str(n["face"])}"',
            f'projection:"{js_str(n["projection"])}"',
            f'pattern:"{js_str(n["pattern"])}"',
            f'invariant:"{js_str(n["invariant"])}"',
            f'source:"{js_str(n["source"])}"',
            f'classification:"{js_str(n["classification"])}"',
            f'u:{n["u"]}',
            f'v:{n["v"]}',
            f'x:{n["x"]}',
            f'y:{n["y"]}',
            f'z:{n["z"]}',
        ]) + '},')
    lines.append("];")
    lines.append("")

    # TORUS_EDGES
    lines.append("const TORUS_EDGES = [")
    for e in all_edges:
        lines.append('  {' + ', '.join([
            f'from:"{js_str(e["from"])}"',
            f'to:"{js_str(e["to"])}"',
            f'shared:"{js_str(e["shared"])}"',
            f'type:"{js_str(e.get("type", "cross-cut"))}"',
        ]) + '},')
    lines.append("];")
    lines.append("")

    # ATLAS_VERTEX_EDGES (vertex-level from atlas-edges.js)
    lines.append("const ATLAS_VERTEX_EDGES = [")
    for e in atlas_edges:
        lines.append('  {' + ', '.join([
            f'from:"{js_str(e["from"])}"',
            f'to:"{js_str(e["to"])}"',
            f'shared:"{js_str(e["shared"])}"',
        ]) + '},')
    lines.append("];")
    lines.append("")

    # TORUS_VERTICES
    lines.append("const TORUS_VERTICES = [")
    for v in all_vertices:
        layers_str = "[" + ",".join(f'"{l}"' for l in v["layers"]) + "]"
        lines.append('  {' + ', '.join([
            f'id:"{js_str(v["id"])}"',
            f'label:"{js_str(v["label"])}"',
            f'layers:{layers_str}',
            f'u:{v["u"]}',
            f'primaryFace:"{js_str(v["primaryFace"])}"',
        ]) + '},')
    lines.append("];")
    lines.append("")

    # TORUS_META
    lines.append("const TORUS_META = {")
    for k, val in meta.items():
        if isinstance(val, str):
            lines.append(f'  {k}: "{js_str(val)}",')
        else:
            lines.append(f'  {k}: {val},')
    lines.append("};")

    output = "\n".join(lines) + "\n"

    os.makedirs(os.path.dirname(OUT_FILE), exist_ok=True)
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write(output)

    print(f"\n=== BUILD COMPLETE ===")
    print(f"Output: {OUT_FILE}")
    print(f"Nodes: {meta['nodeCount']}")
    print(f"Edges: {meta['edgeCount']}")
    print(f"Vertices: {meta['vertexCount']}")
    print(f"Integers-original: {meta['integersOriginalCount']}")
    print(f"Literature: {meta['literatureCount']}")
    print(f"External: {meta['externalCount']}")
    print(f"Classical: {meta.get('classicalCount', 0)}")
    print(f"Open: {meta['openCount']}")
    print(f"Atlas vertex-level edges: {meta['atlasEdgeCount']}")
    if warnings:
        print(f"\nWarnings ({len(warnings)}):")
        for w in warnings:
            print(f"  - {w}")


if __name__ == "__main__":
    main()
