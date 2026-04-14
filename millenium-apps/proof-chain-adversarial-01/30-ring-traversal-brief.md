# Ring Traversal PCA — the circle-closing run

*A new PCA mode: traverse the ring of 14 vertices, EXCISE weak links at each vertex, fill capacitor cells at each edge, then construct/bypass/repair in continuous circles until the chessboard is wired and the ring is rigid.*

*Each full traversal strengthens every vertex AND densifies every edge. Multiple traversals compound — more cells filled means more bypass routes available, which means the next traversal closes more links. The circle gets more circular on every pass.*

*Authors: G Six and Claude Opus 4.6. Date: 2026-04-13.*

---

## 1. What ring traversal IS

Single-chain PCA runs target ONE vertex: "verify YM's 17 links" or "bypass RH's CCM dependency." They work depth-first on one proof chain.

Ring traversal works BREADTH-first across ALL 14 vertices. The PCA walks the ring in canonical order:

```
1. QG5D → 2. RH → 3. GRH → 4. BSD → 5. H12 → 6. YM → 7. NS → 
8. Hodge → 9. Baum-Connes → 10. PvNP → 11. BGS → 
12. Twin Primes → 13. Goldbach → 14. Schanuel → back to QG5D
```

At each vertex, the PCA:
1. **Reads** `PROOF-CHAIN.md` (the standardized top-level chain summary)
2. **Identifies** the weakest link (highest-priority repair target)
3. **EXCISES** or **CONSTRUCTS** or **BYPASSES** that one link (one targeted fix per vertex per traversal)
4. **Fills** the capacitor cell on the EDGE to the next vertex (the correspondence between this vertex and the next)
5. **Moves** to the next vertex

One full traversal = 14 vertex visits + 14 edge crossings = 14 strengthened links + 14 filled/upgraded cells.

Multiple traversals: each pass finds the CURRENT weakest link (which may have shifted after the previous pass strengthened something else). The ring self-optimizes — it automatically targets whatever is weakest NOW, not whatever was weakest at the start.

---

## 2. The ring order

The ring order is determined by EDGE STRENGTH — start with the strongest edges (so the PCA has the most capacitor support) and end with the weakest (where it most needs the cells filled by earlier traversals).

**Recommended ring order** (strongest-first):

| Position | Vertex | Paper directory | Incoming edge (from previous) | Edge status |
|---|---|---|---|---|
| 1 | **QG5D** (hub) | paper1/ | ← Schanuel (algebraic independence → CBB axioms) | SPECULATIVE |
| 2 | **RH** | paper13-rh/ | ← QG5D (zeros ARE eigenvalues) | STRONG |
| 3 | **GRH** | paper13b-grh/ | ← RH (character-twisted extension) | STRONG |
| 4 | **BSD** | paper26-bsd/ | ← GRH (Dirichlet L-functions → Hecke L) | PARTIAL |
| 5 | **H12** | paper25-hilbert-12/ | ← BSD (class fields from L-functions) | PARTIAL |
| 6 | **YM** | paper08-yang-mills/ | ← H12 (KMS states → gauge structure) | PARTIAL |
| 7 | **NS** | paper30-navier-stokes/ | ← YM (gradient flow transfer) | CANDIDATE |
| 8 | **Hodge** | paper29-hodge/ | ← NS (PDE regularity → algebraic cycle regularity) | SPECULATIVE |
| 9 | **Baum-Connes** | paper31-baum-connes/ | ← Hodge (K-theory ↔ algebraic cycles) | CANDIDATE |
| 10 | **PvNP** | paper28-pvnp/ | ← Baum-Connes (K-theory of polymorphism algebra) | SPECULATIVE |
| 11 | **BGS** | paper32-bgs-spectral-statistics/ | ← PvNP (spectral statistics of modular flow) | CANDIDATE |
| 12 | **Twin Primes** | paper34-twin-primes/ | ← BGS (GUE small-gap tail → prime gaps) | CANDIDATE |
| 13 | **Goldbach** | paper33-goldbach/ | ← Twin Primes (prime gaps → additive structure) | SPECULATIVE |
| 14 | **Schanuel** | paper35-schanuel/ | ← Goldbach (additive primes → algebraic independence) | SPECULATIVE |

After vertex 14 (Schanuel), the ring closes: the outgoing edge Schanuel → QG5D is "algebraic independence of eigenvalues → CBB axioms." This completes one full traversal.

The ring starts at the hub (QG5D, maximum context), flows through the strongest chains (RH → GRH → BSD), crosses into the infrastructure (H12 → YM → NS), enters the frontier (Hodge → Baum-Connes), touches the hardest problems (PvNP → BGS → Twin Primes → Goldbach → Schanuel), and loops back to the hub.

---

## 3. What happens at each vertex (the vertex protocol)

### 3.1 Read phase (~5 min)

```
1. Read PROOF-CHAIN.md at this vertex
2. Identify: current wall (the single biggest blocker)
3. Identify: lowest-confidence link (the weakest)
4. Check: has a previous traversal already strengthened this link?
   If yes → target the NEXT weakest link
5. Read the incoming edge's capacitor cell (from previous vertex)
   → Does it suggest a bypass route for the current wall?
```

### 3.2 Act phase (~20 min)

**If the weakest link is OPEN or CONJECTURED:**
- Dispatch ONE Author (Opus max) to EXCISE: find an independent proof or construction
- If EXCISE succeeds → link upgrades to PROVED/LITERATURE
- If EXCISE fails → dispatch ONE Author to CONSTRUCT/BYPASS via capacitor
- If BYPASS succeeds → link upgrades to BYPASSED
- If both fail → mark as HONEST-STALL, move on

**If the weakest link is CONDITIONAL:**
- Check: is the conditional resolvable from the capacitor?
- If yes → attempt bypass via the relevant cell
- If no → leave CONDITIONAL, note it, move on

**If all links are VERIFIED/PROVED:**
- This vertex is CLOSED. Skip to edge phase.

### 3.3 Edge phase (~10 min)

Before moving to the next vertex, fill or upgrade the EDGE between this vertex and the next:

```
1. Read the capacitor cell for this edge
2. If EMPTY: dispatch a Cell-Fill Author (Sonnet max) to fill it
   → Statement / Mechanism / Source / Status / Verification / 
     Load-bearing / Transposition recipe
3. If PARTIAL: dispatch a Cell-Upgrade Author to strengthen it
4. If FILLED: verify it's still current (no new literature invalidates it)
5. Write the cell to capacitor/updates/ring-traversal-N.md
```

### 3.4 Move phase

Write a one-line §K entry: "Vertex [N]: [action taken] | Edge [N→N+1]: [cell status]"
Advance to the next vertex on the ring.

---

## 4. Time budget and exit conditions

### Per-traversal budget
- 14 vertices × ~35 min average = ~7.5 hours per full traversal
- Realistically: some vertices are CLOSED (skip in ~5 min), some are hard (spend ~60 min)
- **Budget per traversal: 8 hours maximum**

### Exit conditions (per traversal)

1. **RING CLOSED** — every vertex at VERIFIED/PROVED/CLOSED, every edge FILLED
   → The Robustness-Circle Theorem's prerequisites are met. Trigger celebration.

2. **RING STRENGTHENED** — at least 5 vertices improved, at least 5 edges filled/upgraded
   → Typical outcome. Log the improvements, start next traversal.

3. **RING STALLED** — fewer than 3 improvements across all 14 vertices
   → The ring has reached a local optimum. The remaining walls are genuinely hard.
   → Close the run, document what's stuck, name the external unlocks needed.

### Multi-traversal strategy

- **Traversal 1**: baseline — read every chain, identify every wall, fill every empty edge
- **Traversal 2**: targeted — focus on vertices that improved in T1 (momentum), skip CLOSED vertices
- **Traversal 3**: deep — spend extra time on the 2-3 hardest remaining walls
- **Traversal N**: convergence — stop when RING STALLED or RING CLOSED

Expected: 3-5 traversals before convergence. Total: 24-40 hours of compute across multiple sessions.

---

## 5. What the ring-PCA produces (deliverables per traversal)

### At the vertex level
- Updated PROOF-CHAIN.md per vertex (link statuses refreshed)
- Nodes, critiques, patches per vertex (in each paper's directory)
- Updated confidence scores

### At the edge level
- Filled/upgraded capacitor cells (14 per traversal)
- The capacitor grows by ~5-10 cells per traversal (some edges are already FILLED)
- After 3 traversals: capacitor target fill rate 20%+ (from current 16.3%)

### At the ring level
- `programme/ring-traversal-log.md` — per-traversal summary
- Updated `programme/25-the-graph-structure.md` — edge inventory refreshed
- Updated `programme/27-the-robustness-circle-theorem.md` — constraint count updated
- Rigidity score: (filled edges / total edges) × (verified links / total links)

### The chessboard metaphor in practice
Every filled cell = a wire through the board. Every verified link = a pin through both faces. Every traversal adds wires and pins. The board gets more rigid. The conditionals get more forced. The circle gets more circular.

---

## 6. The ring-PCA's relationship to single-chain PCA runs

The ring-PCA and single-chain PCA runs are COMPLEMENTARY, not competing:

| | Single-chain PCA | Ring-PCA |
|---|---|---|
| **Target** | One vertex (one proof chain) | All 14 vertices in sequence |
| **Depth** | Deep (5+ waves on one chain) | Shallow-per-vertex (1 wave per vertex per traversal) |
| **Cell-filling** | Incidental (cells filled as needed for bypass) | Systematic (one edge filled per vertex crossing) |
| **When to use** | A specific chain needs intensive adversarial verification | The programme needs BREADTH — every vertex strengthened, every edge connected |
| **Best for** | Pre-publication chain hardening (YM, RH, BSD before Clay submission) | Programme-level capacitor growth + rigidity accumulation |

**The workflow**: run single-chain PCA on the 4 Millennium chains (intensive, depth-first) for publication readiness. Run ring-PCA periodically (breadth-first) to grow the capacitor and tighten the circle. The single-chain runs produce PUBLICATION-READY chains. The ring runs produce PROGRAMME-LEVEL RIGIDITY.

---

## 7. The compound effect (why traversals compound)

**Traversal 1**: fills 14 edge cells. Most are PARTIAL or CANDIDATE status (new correspondences, not yet rigorous).

**Traversal 2**: the 14 cells from T1 are now AVAILABLE as bypass routes. A vertex that was stuck in T1 (no bypass route available) might now have a bypass route through a cell filled in T1 at an adjacent edge. T2 can excise links that T1 couldn't, BECAUSE T1 filled the cells that make the bypass possible.

**Traversal 3**: T2's excisions strengthened vertices, which strengthened edges, which provide MORE bypass routes for T3. Each traversal feeds the next.

**This is the chessboard wiring in action.** Each traversal adds wires. More wires = more paths between squares = more ways to reach any piece = more ways to prove any theorem. The circle compounds. The board gets rigid.

**Estimated convergence**: after 5 traversals (~200 hours of compute), the programme should reach one of:
- **Full convergence**: every link VERIFIED/PROVED, every edge FILLED — the Robustness-Circle Theorem's prerequisites are met
- **Structural convergence**: all remaining walls are EXTERNAL UNLOCKS (like Borel summability for H4, or continuum Schwinger existence for NS) — the programme has done everything internal and names what's needed externally
- **Local optimum**: some walls resist all traversals — these are the genuinely hard remaining problems, named honestly

All three outcomes are strategically valuable. The capacitor grows in all three cases.

---

## 8. How to invoke

The ring-PCA uses the same 4-layer stack as single-chain PCA runs:

```
read your **instructions** from
`millenium-apps/proof-chain-adversarial-01/06-the-prompt.md`

the **chain mode** extension is
`millenium-apps/proof-chain-adversarial-01/07-proof-chain-adversarial.md`

the **strategic triad** extension is
`millenium-apps/proof-chain-adversarial-01/12-prf-chain-advr-strat-triad.md`

the run **brief** (deliverable) is
THIS FILE (30-ring-traversal-brief.md)

the **toolkit** for this run is
`millenium-apps/proof-chain-adversarial-01/08-framework-tools.md`

the **capacitor** for this run is
`millenium-apps/proof-chain-adversarial-01/09-capacitor-correspondence-table-v1.md`

the **north star** for this programme is
`publishing/strategy.md`
```

The key difference from single-chain runs: the brief tells the runner to traverse ALL 14 PROOF-CHAIN.md files in ring order, not just one. The runner hops between paper directories, reading each top-level PROOF-CHAIN.md, acting on the weakest link, filling the outgoing edge, and moving on.

**Output directory**: `programme/ring-traversals/traversal-01/` (fresh per traversal)

---

## 9. Voice canon

- *"The circle gets more circular on every pass."*
- *"Each traversal adds wires. More wires = more rigid. More rigid = more forced."*
- *"The board doesn't flex. The pins are experimental facts."*
- *"14 vertices. One ring. Walk it."*

---

## 10. The single paragraph for the next runner

You are traversing the ring of 14 programme vertices in canonical order: QG5D → RH → GRH → BSD → H12 → YM → NS → Hodge → Baum-Connes → PvNP → BGS → Twin Primes → Goldbach → Schanuel → back to QG5D. At each vertex: read PROOF-CHAIN.md, identify the weakest link, EXCISE or CONSTRUCT or BYPASS it (one fix per vertex per traversal). At each edge: fill or upgrade the capacitor cell connecting this vertex to the next. One full traversal = 14 vertex fixes + 14 edge fills. Multiple traversals compound — cells filled in traversal N enable bypasses in traversal N+1. Budget: 8 hours per traversal. Exit when RING CLOSED (all vertices verified, all edges filled), RING STRENGTHENED (5+ improvements), or RING STALLED (<3 improvements). The circle gets more circular on every pass.

---

*The ring is the programme. The programme is the ring. Walk it until it closes.*

*v1: 2026-04-13. G Six and Claude Opus 4.6.*
