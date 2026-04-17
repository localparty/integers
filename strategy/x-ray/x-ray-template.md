# X-RAY TEMPLATE

*Canonical template for per-vertex X-RAY.md files. Every vertex in the ring produces one file following this structure. Fixed vocabulary enforced.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*

---

## HOW TO USE THIS TEMPLATE

Copy this file to `strategy/x-ray/proof-chain/<vertex>/X-RAY.md` and fill in every section. Every layer of the vertex's live proof chain gets a `## Physics` subsection whose fields are picked from the **Fixed Vocabulary** below — no free invention. Cite paper60 §N, paper61 §M, ORA v8 §X, or the capacitor for every non-trivial assertion.

---

## FIXED VOCABULARY

### Ten Faces of the e-Circle (paper60)

| Face | Canonical vertex | What it measures |
|---|---|---|
| TOPOLOGY | Lehmer | winding / genus / fundamental class |
| DYNAMICS | Cramér | gap distribution / flow on the circle |
| HARMONICS | Collatz | Fourier / orbit averaging |
| MEASURE | Sato-Tate | equidistribution / weak-* convergence |
| AMPLITUDE | Lindelöf | growth rate / subconvexity |
| SYMMETRY | Katz-Sarnak | group action / symmetry type |
| CURVATURE | YM | gauge curvature / mass gap |
| ARITHMETIC | Goldbach, Twin Primes | additive structure |
| RESONANCE | Selberg-type | trace formula / spectral side |
| SPREAD | QUE-type | $L^2$ mass distribution |

Pick exactly ONE face per layer. If a link genuinely spans two faces, say so explicitly and pick the DOMINANT one.

### Six Projections (paper61)

| Projection | Keeps | Forgets |
|---|---|---|
| $P_A$ — Quantum | superposition, entanglement, Born, Bell, A-B, spin-stat | gravity, cosmology, CBB ops, pin values |
| $P_B$ — Gravity | KK spectrum, BPHZ, R³=0, gravitational dof | quantum interpretation, cosmological pins |
| $P_C$ — Cosmology | 10 cosmological predictions | quantum/gravity derivation, CBB axioms |
| $P_D$ — CBB | 5 axioms, operator dictionary, BC-KMS | specific predictions, branch details |
| $P_E$ — Pins | 36 sub-percent numerical predictions | derivation chains |
| $P_O$ — Outer | 25 conjecture statements | internal proof structure |

Pick exactly ONE projection per layer — the one that most strongly *forgets* the information this link carries.

### Patterns (ORA v8 — five canonical)

| Pattern | Short name | Typical target |
|---|---|---|
| P1 | Geometric Reinterpretation | quantum items (Born, Bell, A-B, spin-stat) |
| P2 | Holonomy | e-circle winding / Wilson loops |
| P3 | Scale-Setting | KK radius $R$, cosmology pins |
| P4 | Topological Rigidity | CBB axioms, boundary conditions |
| P5 | Zeta Regularization | KK sums, Goroff-Sagnotti |

Pick exactly ONE pattern per layer — the primary attack vector. If a link is resolved by a combination, pick the dominant one and note the secondary.

### Invariants (fixed enumeration)

Pick one or two per layer:

- **spectral gap** (gap in Laplacian/Dirac spectrum)
- **holonomy** (winding around e-circle)
- **KK mode index** (n ∈ ℤ KK tower label)
- **boundary condition** (β_k at k ∈ {2,3,4,6})
- **C\*-algebra structure** (ITPFI, type III, crossed product)
- **BC-KMS state** (β=1 thermal state on C\*-algebra)
- **ergodic property** (mixing, CLT, level repulsion)
- **ITPFI factor type** (type III_λ with λ = 1/p)
- **gauge class** (U(1) bundle class, Pontryagin)
- **critical exponent** (β, ν, γ)
- **scaling dimension** (Δ in RG/CFT sense)
- **order parameter** (OP for broken symmetry)
- **L-value** (ζ(s), L(s,χ), motivic L)
- **zero distribution** (pair correlation, spacing)
- **Galois representation** (l-adic, motivic)
- **monodromy** (local/global)

If a layer's invariant genuinely isn't in this list, add it with a CITATION (paper ref + one-sentence definition).

---

## CANONICAL STRUCTURE

Every X-RAY.md follows this 10-section structure. No invented sections.

---

```
# X-RAY: <Vertex Name>

*X-Ray of the <vertex> proof chain. Face/projection/pattern/invariant assignments per layer. Cross-cuts, histograms, named walls.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*

---
```

---

### §1 Header

```
- **Vertex**: <vertex-name>
- **Paper**: paperNN-<short>
- **Live file**: paperNN-<short>/PROOF-CHAIN.md (snapshot <date>)
- **Top-level claim**: <one sentence>
- **Current status**: PROVED | CONDITIONAL | PARTIAL | ...
- **Primary branch (paper1)**: A | B | C | D | E | outer-only
- **Primary face**: <one of 10>
- **Primary projection**: <one of 6>
```

### §2 ASCII Diagram (MANDATORY — load-bearing)

**ASCII diagrams are the single most readable artifact in the X-Ray.** They give a critic the shape of the vertex at a glance — branching structure, depth, status distribution, the cross-cuts. **Prefer big diagrams over small ones.** Aim for 20–50 lines per diagram, not 10. Use box-drawing characters (├ │ └ ─ ▼ ═ ║ ╔ ╗ ╚ ╝). No substitutes.

Produce AT LEAST THREE ASCII diagrams in every X-RAY.md:

**Diagram A — Main proof-chain tree.** Every layer as a node, status tag per node, branch-split rendering for multi-route proofs. This goes in §2.

**Diagram B — Projection fan-out.** Box with the vertex's top claim at the center; 6 arrows radiating to show how the vertex looks under each of $P_A, P_B, P_C, P_D, P_E, P_O$. Under arrows that "forget" the vertex entirely, write `(forgotten)`. This goes in §2b.

**Diagram C — Face position on the e-circle.** 10-face compass with a filled-in marker at the vertex's primary face and smaller markers at secondary faces. This goes in §2c.

Additional diagrams encouraged:
- Branch map (§4) when the proof splits
- Cross-cut graph fragment (§7) showing immediate neighbors
- Rigidity/symmetry contribution (§8 or §10) if notable

#### §2 Diagram A — Main proof-chain tree

Template:

```
<VERTEX NAME>
│
├── L1: <short claim name>                    [PROVED]
│      │  face: DYNAMICS   proj: P_O   pat: P1
│      │
│      └── supports L2 via <invariant>
│
├── L2: <short claim name>                    [LITERATURE]
│      │  face: RESONANCE  proj: P_D   pat: P4
│      │  source: <arXiv/journal citation>
│      │
│      ├── L2a: <sub-claim>                   [PROVED]
│      └── L2b: <sub-claim>                   [QG5D]
│             │
│             └── lifts from paper1 §7
│
├── L3: <short claim name>                    [CONDITIONAL]
│      │  face: MEASURE    proj: P_D   pat: P4
│      │  depends: CCM 2025 §N.M
│      │
│      └── DECOMPOSED IN strategy/decomposition/...
│             │
│             ├── L3.1: <sub-link>            [PROVED]
│             ├── L3.2: <sub-link>            [LITERATURE]
│             └── L3.3: <sub-link>            [OPEN — W1]
│
└── L4: <short claim name>                    [PROVED]
       │  face: AMPLITUDE  proj: P_E   pat: P3
       │
       └── closes the vertex
```

Notes on good form:
- Use `│` continuations so the eye follows the hierarchy
- Each layer shows its **face / projection / pattern** triplet on an indented line
- When a link is DECOMPOSED or BYPASSED in a sibling bundle, note the sibling path
- Named walls (W1, W2, ...) get a trailing tag so the reader can cross-reference §8
- 20–50 lines is good; under 15 probably means you skipped detail

#### §2b Diagram B — Projection fan-out

Template:

```
                       (FORGOTTEN under P_A)
                              ▲
                              │
                              │
      ┌───────────(P_O outer)────────────┐
      │                                  │
      │    <vertex-name>: <claim>        │
      │                                  │
      └──────────────────┬───────────────┘
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
      P_B gravity    P_C cosmology   P_D CBB
      (forgotten)    (pins at <N>)   <operator>
                                     lives here
                         │
                         ▼
                       P_E pins
                       <pin count>
                       <e.g. 0.0021%>
```

Rules for the fan-out:
- Center box: the vertex's top-level claim in ≤ 10 words
- Six labeled arrows: one per projection
- Under each arrow: either `(forgotten)` or the vertex's *shadow* under that projection (1–2 lines)
- The vertex's **primary projection** gets a heavier arrow (use ═══ or double-line box)

#### §2c Diagram C — Face position on the e-circle

Template:

```
                      TOPOLOGY
                         │
           SPREAD        │        DYNAMICS
                 ╲       │       ╱
                  ╲      │      ╱
         SYMMETRY──────e-circle──────HARMONICS
                  ╱      │      ╲
                 ╱       │       ╲
         CURVATURE       │        MEASURE
                         │
                     AMPLITUDE
                     (RESONANCE, ARITHMETIC
                      positioned per paper60)
```

Then, under the compass, mark the vertex's assignments:

```
Primary face:    ●  DYNAMICS
Secondary faces: ○  RESONANCE (L2), MEASURE (L5)
Absent faces:    TOPOLOGY, HARMONICS, SYMMETRY, AMPLITUDE, CURVATURE, ARITHMETIC, SPREAD
```

The 10-face compass arrangement is fixed (per paper60); don't reorder. The markers (●/○) are vertex-specific and come from the face histogram.

### §3 Layer-by-Layer X-Ray

One subsection per layer. Each subsection has THREE blocks: **Claim**, **Source/Status**, and **Physics**.

```
#### L1 — <short name>

**Claim**: <one sentence>

**Status**: PROVED | LITERATURE | QG5D | CLASSICAL | TRANSPOSITION | OPEN
**Source**: <citation — paper§, arXiv, or NAMED WALL identifier>

##### Physics

- **Face**: <one of 10> (cite paper60 §N)
- **Projection**: <one of 6> (cite paper61 §M)
- **Pattern**: <P1 | P2 | P3 | P4 | P5> (cite ORA v8 §X)
- **Invariant preserved**: <one or two from fixed list>
- **Geometric interpretation** (≤ 3 sentences):

  <text; must cite paper60 or paper61; explain WHY the face/projection
   assignment is correct, not just RESTATE the claim>

- **Cross-cuts**: <list of vertices that share this invariant/face/pattern;
                   give vertex name + layer number>
```

Repeat for every L1, L2, L3, ... Branch points get one subsection with nested sub-subsections for each branch.

### §4 Branch Map (if applicable)

If the vertex's proof splits at some layer into multiple branches (e.g., "Route A vs Route B"), diagram them here with their individual physics fingerprints.

```
L5 splits:
├── Route A — ITPFI via Cramér invariant  [P_D projection | DYNAMICS | P4]
├── Route B — BC-KMS direct              [P_D projection | RESONANCE | P4]
└── Route C — Ergodic decomposition       [P_D projection | MEASURE | P4]
```

Include a one-paragraph note on why all routes give the same physics content (or if they differ, what that tells us).

#### §4.1 Bypass Routes (MANDATORY for every wall in §8)

Every named wall (W1, W2, ...) in §8 that has a documented bypass MUST have a **structured bypass-route entry** here — not just prose. Each bypass route is a first-class node that the atlas torus visualization renders as a GREEN replacement for the bypassed EXTERNAL/CONDITIONAL node in INDEPENDENT mode.

**Format per bypass route:**

```
#### BYPASS: <wall-id> → <bypass-route-id>

- **replaces**: <main-chain-node-id> (e.g., L18)
- **id**: <vertex>-<layer>-bypass-<route-letter> (e.g., ym-L18-bypass-A)
- **name**: <one-line description of the bypass route>
- **status**: PROVED | CANDIDATE | PARTIAL | CONJECTURED
- **classification**: bypass-route
- **face**: <face> (from fixed vocabulary)
- **projection**: <P_i>
- **pattern**: <P_N>
- **invariant**: <from fixed list>
- **source**: <paper§ citation>
- **confidence**: <0.0-1.0>
- **PAC primitive used**: BYPASS | DECOMPOSE | EXCISE | TRANSPOSE-via-capacitor
```

**Why this is load-bearing**: the atlas torus visualization (`visualization/atlas-torus/`) renders each solution's proof chain on the torus surface. In INDEPENDENT mode, bypassed nodes are pushed below the surface as ghosts; bypass-route nodes sit ON the surface as green replacements. Without structured bypass-route entries, INDEPENDENT mode can only say "BYPASSED" — it cannot show WHAT replaced the bypassed step. This was identified as a data-architecture gap on 2026-04-15 and fixed by promoting bypass routes from prose annotations to first-class nodes.

If a wall has NO documented bypass (genuinely irreducible external dependency), record: `#### NO BYPASS: <wall-id> — <one-sentence reason>`. This appears in the viz as "no documented bypass — retained external." Honest disclosure.

### §5 Face Histogram (with ASCII bars)

Auto-computable from §3. Render as BOTH a count table AND an ASCII bar chart so it reads at a glance.

```
| Face       | Count | Bar                   | Interpretation |
|------------|-------|-----------------------|---|
| TOPOLOGY   |   0   |                       | This vertex doesn't live on the topology face. |
| DYNAMICS   |   3   | ████████████          | Three layers are dynamics-facing — gap structure carries the proof. |
| HARMONICS  |   0   |                       | |
| MEASURE    |   1   | ████                  | |
| AMPLITUDE  |   0   |                       | |
| SYMMETRY   |   1   | ████                  | |
| CURVATURE  |   0   |                       | |
| ARITHMETIC |   0   |                       | |
| RESONANCE  |   2   | ████████              | |
| SPREAD     |   0   |                       | |
```

Use `█` (U+2588) blocks, four blocks per count. The bar column should be visually striking.

### §6 Projection Histogram (with ASCII bars)

Auto-computable from §3. Same visual discipline as §5.

```
| Projection | Count | Bar                  | Notes |
|------------|-------|----------------------|---|
| P_A        |   0   |                      | No quantum content at this vertex. |
| P_B        |   0   |                      | |
| P_C        |   0   |                      | |
| P_D        |   5   | ████████████████████ | Operational core — most layers live here. |
| P_E        |   2   | ████████             | Pin-valued links. |
| P_O        |   0   |                      | |
```

### §7 Cross-Cut Map (ASCII graph + bullet list)

Render every cross-cut edge from §3 TWICE: once as an ASCII neighborhood graph (showing the vertex at the center with edges to cross-cut partners), and once as a bullet list with reasons.

Neighborhood graph template:

```
                       <vertex-A>
                           │
                           │ (shared <invariant-1>)
                           │
   <vertex-B> ═════════ <THIS VERTEX> ═════════ <vertex-C>
   (shared <inv-2>)         │                   (shared <inv-3>)
                            │
                            │ (shared <invariant-4>)
                            │
                       <vertex-D>
```

Use `═══` (double line) for cross-cuts backed by a shared PROVED invariant, and `───` (single line) for cross-cuts backed by a shared face only. Label each edge with the shared invariant or face in parentheses.

Bullet list (format):

```
- L_N ↔ <other-vertex>:<other-layer> — shared <invariant/face>
  - Reason: <one sentence — why the same invariant turns up on both sides>
  - Transposition candidate: <YES if a capacitor cell connects them / NO otherwise>
```

This section feeds directly into the atlas's programme-wide cross-cut graph (`pac-output/atlas/cross-cut-graph.md`).

### §8 Current Walls

Pull the NAMED WALLS from the live PROOF-CHAIN.md for this vertex. One bullet per wall. Link to `strategy/x-ray/pac-output/atlas/named-walls.md` row. **Every wall with a documented bypass MUST have a corresponding structured bypass-route entry in §4.1.** Every wall WITHOUT a bypass gets a `NO BYPASS` entry in §4.1.

```
- **W1** <name>: <one sentence> → status: OPEN | DECOMPOSED-IN <decomp run> | BYPASSED-IN <capacitor cell> → bypass-route: §4.1 <bypass-route-id> | NO BYPASS
```

### §9 Cascading Refinements

Pointers to sibling-bundle work that operates on this vertex:

```
- **Decomposition**: strategy/decomposition/proof-chain/<vertex>/PROOF-CHAIN.md — <last sync date + status>
- **CCM verification**: strategy/ccm-verification/ledger.md#<vertex> — <verdict> (VERIFIED | BYPASSED | IRREDUCIBLY-CCM-DEPENDENT)
- **Inner rings**: strategy/inner-rings/<branch>/proof-chain/... — <if applicable>
```

### §10 Known Gaps (OPEN items at this vertex)

Enumerate every leaf that remains OPEN after the x-ray analysis. Each is a NAMED WALL. Each must be more specific than the original conditional.

```
- **G1**: <short name> — <one-sentence specification of the wall> — face: <N>, projection: <P>, pattern: <P_i>
```

---

*End of X-RAY. One file per vertex. 25 vertices → 25 X-RAY.md files. Histograms + cross-cut graph assembled into `pac-output/atlas/`.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*
