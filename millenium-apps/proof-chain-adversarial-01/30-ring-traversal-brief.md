# Ring Traversal PCA — the circle-closing run

*A new PCA mode: traverse the ring of 14 vertices, EXCISE weak links at each vertex, fill capacitor cells at each edge, then construct/bypass/repair in continuous circles until the chessboard is wired and the ring is rigid.*

*Each full traversal strengthens every vertex AND densifies every edge. Multiple traversals compound — more cells filled means more bypass routes available, which means the next traversal closes more links. The circle gets more circular on every pass.*

*Authors: G Six and Claude Opus 4.6. Date: 2026-04-13.*

---

## 0. Glossary and conventions (read first)

### 0.1 Action vocabulary (EXCISE / CONSTRUCT / BYPASS)

Ring mode distinguishes three capacitor-aware moves that sit ABOVE PCA's underlying triad (verify / construct / bypass):

- **EXCISE** — attempt to replace a conditional or open link with an INDEPENDENT, already-published result. Primary mode: literature search + direct adaptation. If no independent result exists, fall through to CONSTRUCT.
- **CONSTRUCT** — build the missing proof via the capacitor toolkit. Dispatch a construct Author with access to the relevant capacitor cells + framework tools. If the construct can't close the link within a capacitor transposition, fall through to BYPASS.
- **BYPASS** — transpose to a different domain via the capacitor. The link becomes unnecessary (rather than proved directly); an alternative path reaches the downstream conclusion.

EXCISE → CONSTRUCT → BYPASS is the escalation ladder. Ring mode's naming is ADDITIVE — PCA's underlying primitives (verify/construct/bypass) still apply internally. "EXCISE" is NOT a rename of PCA's BYPASS; EXCISE precedes it in the escalation order.

When the chessboard layer §6.2 classifies a vertex as "Type B — Excision-primary," it means: try EXCISE first at this vertex, then fall through to CONSTRUCT (Type C fallback) and BYPASS (capacitor-driven) if EXCISE fails.

### 0.2 Status dictionary (cross-layer mapping)

Five partially-overlapping status taxonomies exist across the 5-layer stack. This dictionary defines the canonical ring-mode mapping.

**Link-level status** (applies to proof chain links per vertex):

| Ring-mode name | PCA equivalent (P.2) | Capacitor equivalent | Meaning |
|---|---|---|---|
| PROVED / LITERATURE | VERIFIED | ESTABLISHED | Rigorous published proof exists |
| CLOSED | VERIFIED | ESTABLISHED | Proof complete in framework |
| CONJECTURED | OPEN | CANDIDATE | Statement plausible but unproved |
| OPEN | OPEN | — | No proof attempted yet |
| CONDITIONAL | CONDITIONAL | — | Proof depends on external hypothesis |
| WEAKENED | WEAKENED | — | Existing proof has a caught gap |
| BROKEN | BROKEN | — | Existing proof has a fatal gap |
| BYPASSED | BYPASSED | ESTABLISHED (via alt. path) | Link replaced by capacitor-routed alternative |
| HONEST-STALL | HONEST-STALL | — | No viable route after EXCISE + CONSTRUCT + BYPASS all attempted |

**Edge-level status** (applies to capacitor cells between vertices):

| Ring-mode (brief §2) | Capacitor file | Meaning |
|---|---|---|
| STRONG | VERIFIED | Rigorous correspondence, computational verification |
| PARTIAL | ESTABLISHED | Published correspondence but one-sided or scope-limited |
| CANDIDATE | CANDIDATE | Plausible correspondence, not yet demonstrated |
| SPECULATIVE | (no cell or CANDIDATE) | Correspondence hypothesized but not filled |

**Cell-level status** (applies within the capacitor lookup protocol):

| Ring-mode (brief §3.3) | Capacitor | Action |
|---|---|---|
| FILLED | VERIFIED or ESTABLISHED | Upgrade with new findings if any |
| PARTIAL | CANDIDATE | Upgrade-Author dispatched to strengthen |
| EMPTY | (no cell) | Cell-Fill Author dispatched to create |

Authors and Critics should use the RING-MODE names in their outputs; the runner's reconciliation pass at cycle-close translates to PCA/capacitor native names for the respective state files.

### 0.3 Canonical paper locations

The 14 ring vertices point to canonical paper directories under `/Users/gsix/quantum-geometry-in-5d-latex/`. NOTE: older directories `paper27-hodge/` and `paper27-navier/` exist and contain historical research — they are NOT canonical. The ring uses `paper29-hodge/` and `paper30-navier-stokes/` (the scaffolds built in this session). If a Glob surfaces `paper27-*/`, treat those as archive only; do not update them.

### 0.4 Ring mode is CONTINUOUS-RUN

Ring traversals take hours. The invocation is structurally async — no interactive user presence is assumed between cycle-opens. Triad proposals do NOT block dispatch (they land in `triad/traversal-N/mediator-proposal.md` and the runner continues). The user applies approved edits BETWEEN traversals. See §8.3.

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

### 2.1 Edge ownership (disambiguation)

**Ring edges (14 total)** are owned by exactly ONE vertex — the **predecessor** (the vertex you're leaving). That vertex fills the ring edge during its EDGE PHASE (§3.3) as its LAST action before moving on. The successor vertex does NOT re-fill the edge — it inherits the filled edge as its "incoming context" (§3.1 READ phase).

**Ring-closure boundary condition (T1)**: on traversal 1, when QG5D (position 1) is visited FIRST, the incoming edge Schanuel → QG5D has not yet been filled (Schanuel at position 14 hasn't run yet). Interpretation: **pre-traversal capacitor state IS the incoming context for T1's position-1 vertex.** QG5D reads whatever cell currently exists for Schanuel → QG5D (EMPTY/SPECULATIVE pre-T1) and proceeds without waiting. Schanuel fills its outgoing edge to QG5D at T1's position 14 AFTER QG5D has already been visited. Subsequent traversals (T2+) inherit what Schanuel wrote in the prior traversal as their incoming context at position 1. T1 is a "prime-the-pump" traversal for the ring-closing edge.

**Ring edges are TRANSPOSITION CHALLENGES, not acknowledgments of natural programme-graph dependencies.** Each ring edge forces a connection between two vertices that may not have a direct link in either vertex's `PROOF-CHAIN.md` "Programme graph edges" section (e.g., H12 → YM does not appear in either H12's or YM's own edge list). The Cell-Fill Author dispatched to fill a ring edge is expected to CREATE the connection via capacitor domain-pair lookup (§2.2) + transposition recipe (§0.1), not cite an existing one. A ring edge labeled SPECULATIVE in §2 is a discovery target — closing it is a structural contribution that both vertices' future work will inherit. The ring's discipline is to FORCE cross-vertex transpositions that the natural programme graph doesn't express; this is a feature, not a bug.

**Chord edges (77 total — non-adjacent vertex pairs)** have NO single-owner rule. They are filled via three distinct mechanisms, all on the chessboard layer:
- **Hub radiation (chessboard §6.3)**: QG5D fills up to 12 chord edges (QG5D → every non-ring-adjacent vertex) in parallel during its edge phase
- **Antipodal probe (chessboard §6.4)**: 7 chord edges (the antipodal pairs) get probed at traversal start
- **Compositional cell-fill (chessboard §6.5)**: when triangle (A, B, C) has A↔B and B↔C filled, the chord A↔C is proposed

Before dispatching any chord-fill action, the runner checks WIRE-DENSITY (chessboard §5) to avoid duplicate work. If a chord is already FILLED, the runner SKIPS the fill (or upgrades if new findings warrant). Ring edges (owned by predecessor) and chord edges (owned by nobody, filled by mechanisms) do NOT conflict — they're distinct subsets of the 91-cell capacitor.

Concretely, for traversal T:
- Vertex N's edge phase fills edge `N → N+1` (exactly once).
- Vertex N+1's read phase consults edge `N → N+1` (filled by N) as incoming context.
- Vertex N+1's edge phase fills edge `N+1 → N+2` (exactly once).
- Over the full traversal, all 14 edges are filled exactly once. No double-filling. No skipping.

The §2 table's "Incoming edge (from previous)" column is DESCRIPTIVE (what the vertex inherits). §3.3 EDGE PHASE is PRESCRIPTIVE (what the vertex writes).

### 2.2 Vertex-to-domain mapping (capacitor lookup)

Each ring vertex maps to one or more domains in the capacitor's **24-domain index** (defined in `09-capacitor-correspondence-table-v1.md §"Domain index"`). This table uses ONLY the capacitor's actual domain codes (D1-D24) — no invented codes.

| Position | Vertex | Primary domain(s) | Secondary domains (triangulation) |
|---|---|---|---|
| 1 | QG5D | **D2 GEOM** | ALL (hub — every domain connects to QG5D) |
| 2 | RH | **D1 SPEC** + **D5 ANT** | D3 OA, D13 LANG |
| 3 | GRH | **D1 SPEC** + **D5 ANT** | D20 REP, D13 LANG, D11 ECFT |
| 4 | BSD | **D5 ANT** + **D8 AG** | D3 OA, D13 LANG |
| 5 | H12 | **D5 ANT** + **D11 ECFT** | D3 OA, D13 LANG, D8 AG |
| 6 | YM | **D7 QFT** | D1 SPEC, D2 GEOM |
| 7 | NS | **D7 QFT** + **D2 GEOM** | D17 MICRO, D9 PROB |
| 8 | Hodge | **D8 AG** + **D21 HOM** | D13 LANG, D24 NCG |
| 9 | Baum-Connes | **D6 ATOP** + **D3 OA** | D19 DTOP, D24 NCG |
| 10 | PvNP | **D4 INFO** + **D3 OA** | D22 MOD (Fagin's theorem), D18 CODE |
| 11 | BGS | **D9 PROB** + **D23 ERG** | D1 SPEC, D3 OA |
| 12 | Twin Primes | **D9 PROB** + **D5 ANT** | D1 SPEC |
| 13 | Goldbach | **D5 ANT** + **D9 PROB** | D10 THERMO (partition function ζ(β) → prime density) |
| 14 | Schanuel | **D5 ANT** + **D22 MOD** | D24 NCG (model-theoretic transcendence) |

**Domain codes used** (all exist in capacitor v1 §Domain index): D1 SPEC, D2 GEOM, D3 OA, D4 INFO, D5 ANT, D6 ATOP, D7 QFT, D8 AG, D9 PROB, D10 THERMO, D11 ECFT, D13 LANG, D17 MICRO, D18 CODE, D19 DTOP, D20 REP, D21 HOM, D22 MOD, D23 ERG, D24 NCG.

Edge `N → N+1` is filled by looking up the capacitor cell at the intersection of N's primary domain(s) and N+1's primary domain(s). If multiple primary-domain pairs exist (because a vertex has two primary domains), the runner picks the pair with the STRONGEST existing cell status (FILLED > PARTIAL > CANDIDATE > EMPTY). If all primary pairs are EMPTY, fall back to primary×secondary and secondary×secondary pairs in that order. If ALL pairs are EMPTY → new cell must be filled; start from the canonical correspondence recipe in the vertices' PROOF-CHAIN.md "Programme graph edges" sections.

**Example** (edge 2 → 3, RH → GRH):
- RH primary: {D1 SPEC, D5 ANT}
- GRH primary: {D1 SPEC, D5 ANT}
- Pairs to check: (SPEC, SPEC), (SPEC, ANT), (ANT, SPEC), (ANT, ANT)
- The SPEC↔SPEC cell is the diagonal (same-domain upgrade); treat as "internal deepening" rather than a capacitor cell fill.
- The SPEC↔ANT and ANT↔SPEC are the same off-diagonal cell (undirected). This is the canonical "spectral realization of zeros" cell — already FILLED at Tier 1 status.
- Upgrade: add any new findings from RH's Phase 1 bypass run + the character-modulation extension in GRH's chain.

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

**If all links are VERIFIED/PROVED** (per §0.2 status dictionary):
- **Traversal 1 (baseline): run a lightweight re-verification pass.** Dispatch ONE Sonnet Critic to spot-check the 2-3 highest-confidence PROVED links against current capacitor state + any literature added since the last verification. If all SOUND → mark vertex CLOSED-AND-VERIFIED for this ring, skip to edge phase. If a WEAKEN → downgrade and route through the normal EXCISE → CONSTRUCT → BYPASS ladder.
- **Traversals 2+**: trust the PROOF-CHAIN.md status from traversal 1 unless an explicit trigger fires (§8.3 triad §T.3 triggers, or user-written §K note flagging re-verification needed). Skip directly to edge phase. This policy amortizes the baseline verification cost across all subsequent traversals.

**PCA §P.3.1 override**: PCA mandates "verify ALL links simultaneously" (not serialized). Ring mode overrides this for efficiency: at any single vertex visit, the runner verifies ONE link (the weakest) deeply and spot-checks 2-3 others shallowly. The ring as a whole verifies ALL 14 vertices × ~3-5 links each = ~50+ link verifications per traversal, but only the weakest link at each vertex gets the full CONSTRUCT/BYPASS treatment.

### 3.3 Edge phase (~10 min)

**Edge ownership**: the current vertex owns its OUTGOING edge (to the next vertex). It fills exactly this one edge during the edge phase, then moves on. It does NOT touch the incoming edge — that was filled by the previous vertex.

Before moving to the next vertex, fill or upgrade the OUTGOING EDGE per §2.2 vertex-to-domain mapping:

```
1. Determine the target domain pair: (current vertex's primary domain, next vertex's primary domain)
2. Look up the capacitor cell at that domain pair (consult §2.2 table)
3. If EMPTY: dispatch a Cell-Fill Author (Sonnet max) to fill it
   → Statement / Mechanism / Source / Status / Verification / 
     Load-bearing / Transposition recipe
4. If PARTIAL: dispatch a Cell-Upgrade Author to strengthen it with 
   any new findings from the current vertex's act phase
5. If FILLED: verify it's still current (no new literature invalidates it);
   append a "traversal-T confirmation note" rather than re-filling
6. Write the cell update to capacitor/updates/ring-traversal-N.md
```

**Critical**: each of the 14 edges is filled EXACTLY ONCE per traversal. The predecessor vertex owns the edge. No double-filling by the successor.

### 3.4 Move phase

Write a one-line §K entry: "Vertex [N]: [action taken] | Edge [N→N+1]: [cell status]"
Advance to the next vertex on the ring.

---

## 4. Time budget and exit conditions

### Per-traversal budget

- **Traversal 1 (baseline): 10 hours maximum.** Elevated because of one-time setup costs:
  - Antipodal probes (§6.4 chessboard): 7 probes × ~10 min = ~70 min raw; **T1 skips the 2 LOW-priority pairs** (YM↔Goldbach, NS↔Schanuel) → 5 × 10 = ~50 min actual
  - Hub radiation (§6.3 chessboard): ~10 min at QG5D's edge phase
  - Compositional cell-fill (§6.5): ~5 min × 14 = ~70 min
  - VERIFY spot-checks: **SKIPPED ENTIRELY on T1** — the 14 PROOF-CHAIN.md files were just refreshed for the W1/W2 cascade (2026-04-14) and are authoritative at T1 start. VERIFY spot-checks resume on T2+ unless explicit §K trigger fires in T1.
  - Core vertex+edge work: 14 × ~35 min = ~490 min, minus skip-sector-A for confidence ≥ 9/10 (QG5D, BSD, YM) = ~30 min saved → ~460 min
  - Total estimate post-trims: 50 + 10 + 70 + 0 + 460 = **~590 min ≈ 9.8 h** ✓ fits 10 h ceiling
  - Restore policy: VERIFY spot-checks on T2+ (at baseline, the refresh is stale). LOW antipodal probes on T2+ if HIGH/MEDIUM closed or fully probed.
- **Traversals 2+: 8 hours maximum.** Antipodal probes done, hub radiated, sector classification cached. Only core vertex+edge work + DUAL-CHECK/PIN-PRESERVATION firings remain active per cycle.
- Realistically: some vertices are CLOSED (skip in ~5 min), some are hard (spend ~60 min). The budget is per-traversal, not per-vertex — the runner balances across vertices.

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
- RIGIDITY-SCORE (per the chessboard layer `13-chessboard-layer.md` §3, the canonical formula):
  ```
  RIGIDITY = (E_filled / E_total) × (L_verified / L_total) × (P_preserved / P_total) × 100
  ```
  where E_filled/E_total is filled capacitor cells over 276, L_verified/L_total is verified links over 83, and P_preserved/P_total is experimental pins preserved over 36. Current baseline: 9.03.

### The chessboard metaphor in practice
Every filled cell = a wire through the board. Every verified link = a pin through both faces. Every traversal adds wires and pins. The board gets more rigid. The conditionals get more forced. The circle gets more circular. **The chessboard layer (loaded via `13-chessboard-layer.md`) provides the DUAL-CHECK, SPIN, PIN-PRESERVATION, and WIRE-DENSITY primitives used throughout this brief** — the runner reads that extension at bootstrap and applies its primitives during every vertex visit.

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

**The canonical invocation is `30-ring-traversal-run.md`** in this same directory. It loads the 5-layer stack (ORA base + PCA chain mode + strategic triad + chessboard layer + north star) plus the toolkit, capacitor, and output path. The base prompt lives at `online-researcher-adversarial/ora-bundle-v8/01-the-prompt.md` (NOT the archival snapshot at `06-the-prompt.md`) so all its internal references resolve natively. See the run file for the exact paths; update the `traversal-NN` output directory manually for T2/T3/... per §8.2.

Every traversal reuses the same run file with only the output-directory NN incremented. The brief is the deliverable; the run file is the executable invocation. Do NOT copy the invocation template into the brief — it drifts. The brief tells the runner WHAT to do; the run file tells the runner WHICH files to read.

The key difference from single-chain runs: the brief tells the runner to traverse ALL 14 PROOF-CHAIN.md files in ring order, not just one. The runner hops between paper directories, reading each top-level PROOF-CHAIN.md, acting on the weakest link, filling the outgoing edge, and moving on.

### 8.1 State management (ring-mode override of 07-proof-chain-adversarial.md §P.2)

The PCA chain-mode extension (`07-proof-chain-adversarial.md`) assumes SINGLE chain and mandates ONE `chain/chain-state.md` file. Ring mode overrides this. In ring mode:

- **No unified chain-state file is created.** The runner does NOT write a single ring-wide chain-state.md.
- **14 in-situ PROOF-CHAIN.md files are the source of truth** — one per vertex, at `paperNN-xxx/PROOF-CHAIN.md`. The runner UPDATES these in place as each vertex is visited (status columns, confidence scores, "last traversal" timestamps).
- **Per-traversal log at `programme/ring-traversal-log.md`** — the runner APPENDS one entry per traversal to this file (traversal number, RIGIDITY before/after, per-vertex actions, per-edge fills, kills added, exit condition).
- **Per-vertex blackboards at `${output-directory}/vertices/<vertex-name>.md`** — the runner creates these for each vertex visit, capturing the blackboard §A-§O state DURING the visit. These are ephemeral working state, not authoritative.
- **Per-cell updates at `${output-directory}/capacitor/updates/<cell-id>.md`** — one file per cell filled or upgraded during the traversal.

At every cycle-close, the runner reconciles: in-situ PROOF-CHAIN.md files = CANONICAL STATE; log file = HISTORICAL RECORD; per-vertex blackboards = WORKING SCRATCH. If an Author returns work that changes a vertex's chain, the update goes to BOTH the in-situ PROOF-CHAIN.md (canonical) AND the per-vertex blackboard (working).

This multi-file architecture replaces the single chain-state.md of ordinary PCA runs. The runner MUST NOT create `chain/chain-state.md` in ring mode — it would be misleading (state lives in 14 places, not one).

### 8.2 Output directory numbering

The output directory is `programme/ring-traversals/traversal-NN/` where NN is the current traversal number (zero-padded 2-digit).

Before invoking, the caller MUST set NN correctly. The invocation file (`30-ring-traversal-run.md`) hardcodes `traversal-01` — for traversal 2, change to `traversal-02`; for traversal 3, `traversal-03`; and so on. The runner checks `programme/ring-traversals/` at bootstrap and WARNS if the target directory already exists (unless explicitly resuming).

**Resume semantics**: if `traversal-NN/` exists AND contains a `vertices/` subdirectory with partial work, the runner treats this as a RESUME of an interrupted traversal. It reads what was completed and continues from the next vertex. No work is lost.

### 8.3 Strategic triad handling in ring mode (override of `12-prf-chain-advr-strat-triad.md` §T.3 and §T.6)

The strategic triad layer is LOADED in ring mode (per §8's invoke template), but its firing semantics are modified:

**§T.3 triggers fire PER-TRAVERSAL, not per-vertex.** At traversal-close (after all 14 vertices visited), the runner checks the 6 triad triggers against the traversal's AGGREGATE findings. The triad does NOT fire after each individual vertex visit — that would produce 14× user-approval requests per traversal, overwhelming the user-out-of-loop budget.

**§T.6 approval gates are NON-BLOCKING in ring mode** (ring mode is CONTINUOUS-RUN per §0.4). Triad proposals land in `${output-directory}/triad/traversal-N/mediator-proposal.md` and the runner CONTINUES to the next traversal. The user applies approved edits to the brief/chessboard/capacitor BETWEEN traversals, not during. Traversal N+1 picks up whatever edits are in place at its bootstrap — the triad proposal from traversal N is either applied (incorporated) or deferred (still in queue).

**§T.10 backward-compat**: if the user wants a pure-PCA ring run without the triad layer, they can invoke by REMOVING the `strategic triad` line from `30-ring-traversal-run.md`. The runner detects the omission and proceeds without triad. This is the recommended FALLBACK if the triad is producing noise-level proposals early in the programme.

**Expected triad activity per traversal**:
- Traversal 1: few triggers (baseline; most findings are NEW, nothing to compare to)
- Traversals 2-3: moderate triggers (cell-fills plateauing, rigidity delta stabilizing, one-liner brief edits proposed)
- Traversals 4+: rare triggers (either the ring is converging smoothly, or it has stalled — triad should name which)

### 8.4 Closure ritual on ring exit (override of ORA §13.3 and PCA §P.9)

The three exit conditions from §4 trigger different closure protocols:

- **RING STRENGTHENED (typical outcome)**: ABBREVIATED ritual.
  - Append a `programme/ring-traversal-log.md` entry with before/after RIGIDITY, per-vertex actions, per-edge fills, kills added
  - Write a commit memo to `${output-directory}/commit-memo.md`
  - Do NOT spawn a final-adversarial-pass or referee — the next traversal performs that role implicitly
  - Total ritual cost: ~15 min

- **RING CLOSED (dream outcome, rare until convergence)**: FULL 5-FILE ritual per ORA §13.3 + PCA §P.9.
  - `lockdown.md` — freeze the current state
  - `final-adversarial-pass.md` — a dedicated Critic sweep across all 14 vertices
  - `referee.md` — formal referee-style review of the ring as a whole
  - `closure.md` — per-vertex + per-edge closure summaries
  - `backup.md` + commit memo
  - Trigger the Robustness-Circle Theorem draft pass (§27 in programme document)
  - Total ritual cost: ~4-6 hours (within the 8-hour traversal budget if RING CLOSED emerges mid-traversal)

- **RING STALLED (honest-named outcome)**: MEDIUM ritual.
  - Append to `programme/ring-traversal-log.md` with explicit stall diagnosis
  - Write `${output-directory}/stall-diagnosis.md` naming: which walls resisted, which external unlocks are needed, what the capacitor would need to fill before resuming
  - Do NOT spawn final-adversarial-pass (premature), but DO spawn a referee-style summary for the stall report
  - Total ritual cost: ~60-90 min

The ritual choice is determined at cycle-close by comparing RIGIDITY-SCORE delta + per-vertex improvement counts against the §4 exit-condition thresholds.

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
