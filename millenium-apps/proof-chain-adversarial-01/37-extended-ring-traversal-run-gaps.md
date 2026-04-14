# Extended Ring Traversal Run — Recursive Audit & Gap Report

*Audit of `32-extended-ring-run.md` and all files in its dependency tree.*
*Auditor: Claude Opus 4.6 (1M context). Date: 2026-04-14.*

---

## 0. Scope and method

The run file `32-extended-ring-run.md` was traced recursively through every file it references, every file THOSE files reference, and every data file (PROOF-CHAIN.md) that the ring touches. The audit checks for:

- **Existence**: does every referenced file exist on disk?
- **Conflict**: do two files give contradictory instructions, numbers, or definitions?
- **Ambiguity**: is there a rule, threshold, or definition that a runner could reasonably interpret two ways?
- **Staleness**: is a file's content still calibrated for the 14-vertex ring when the run uses the 19-vertex ring?

**Files audited** (28 unique files + 19 PROOF-CHAIN.md files = 47 total):

| Layer | File | Status |
|---|---|---|
| Run file | `32-extended-ring-run.md` | read in full |
| ORA v8 base | `ora-bundle-v8/01-the-prompt.md` | read in full (~36K tokens) |
| ORA companions | `02-rationale.md`, `03-synthesis-spawn.md`, `04-closure-templates.md`, `06-anti-overfit-discipline.md`, `08-changelog.md` | read in full |
| PCA chain mode | `07-proof-chain-adversarial.md` | read in full |
| Strategic Triad | `12-prf-chain-advr-strat-triad.md` | read in full |
| Chessboard layer | `13-chessboard-layer.md` | read in full |
| Brief (delta) | `32-extended-ring-brief.md` | read in full |
| Brief (parent) | `30-ring-traversal-brief.md` | read in full |
| Toolkit | `08-framework-tools.md` | read in full |
| Capacitor | `09-capacitor-correspondence-table-v1.md` | read in full |
| North Star | `publishing/strategy.md` | read in full |
| Graph structure | `programme/25-the-graph-structure.md` | existence + edge 46 verified |
| Archival snapshot | `06-the-prompt.md` | existence confirmed |
| Output directory | `programme/ring-traversals/traversal-05` | checked (does not yet exist) |
| 19 PROOF-CHAIN.md | all 19 paper directories | read headers + link counts |

---

## 1. File existence audit

### 1.1 All referenced files exist

Every file referenced by the run file and its transitive dependencies exists on disk. All 19 PROOF-CHAIN.md files are present.

### 1.2 Output directory not yet created

`programme/ring-traversals/traversal-05` does not exist. Parent directory `programme/ring-traversals/` contains `traversal-01` through `traversal-04`. The runner will need to create `traversal-05/` at bootstrap. Brief 30 §8.2 says the caller sets the NN. **No issue** — this is expected pre-run state.

### 1.3 Wrong path reference for graph-structure file

Brief 32 line 41 references `25-the-graph-structure.md` without a full path. The actual file lives at `programme/25-the-graph-structure.md`, NOT at `paper12/research/25-the-graph-structure.md`. Edge 46 (QG5D → Hilbert 6, type STRONG) is confirmed present at line 141 of the actual file.

**Severity: MINOR.** The file exists at a different path. A runner grepping for it would find it.

---

## 2. CRITICAL — RIGIDITY formula denominator conflict

This is the most important finding of the audit.

### 2.1 The conflict

The RIGIDITY formula is defined in chessboard layer §S3 (lines 124-134):

```
RIGIDITY = (E_filled / E_total) × (L_verified / L_total) × (P_preserved / P_total) × 100

where:
  E_total    = total possible capacitor cells (276 for 24 domains)
  L_total    = total proof chain links across all 14 vertices
```

The chessboard layer explicitly defines **E_total = 276 = C(24,2) domain-pair cells**. This is the capacitor's own count — 24 mathematical domains produce 276 possible pairwise correspondences.

Brief 32 DELTA 2 redefines:

```
E_total = ~513 (171 × 3 status tiers)
```

Where 171 = C(19,2) = the number of **vertex pairs** in a 19-vertex ring, multiplied by 3 status tiers.

**These are two fundamentally different quantities:**

| | Chessboard layer / Brief 30 | Brief 32 |
|---|---|---|
| E_total counts | Domain-pair cells (24 domains) | Vertex-pair × status-tiers (19 vertices × 3) |
| E_total value | 276 | 513 |
| Unit | Capacitor cells | Ring edge-slots |
| Independent of ring size? | YES (24 domains are fixed) | NO (scales with vertex count) |

**E_filled = 48 counts domain-pair filled cells** (from the capacitor). Dividing domain-pair filled cells by vertex-pair × status-tier slots is dimensionally incoherent. The RIGIDITY ratio E_filled/E_total mixes two different counting bases.

### 2.2 The cascade

This conflict propagates into:

1. **Brief 32 RIGIDITY baseline**: reported as 6.07 (using E_total=513). Under the original formula (E_total=276), the same E_filled=48 gives RIGIDITY = (48/276) × (85/131) × 1.0 × 100 = 11.28.

2. **North Star (strategy.md) Appendix B.3**: baseline RIGIDITY = 10.63 (using E_total=276). The North Star and the brief disagree on the current RIGIDITY value by 4.56 points.

3. **North Star B.3 targets**: "RIGIDITY ≥ 15 after traversal 1" was calibrated against the 276-denominator formula. Under the 513-denominator formula, the same physical progress would show ~55% of the RIGIDITY gain. The +6-10 target (B.4) would yield 12-16 under the 276 formula but only 7-11 under the 513 formula. **The targets may be unreachable under the new denominator without recalibration.**

4. **Chessboard S3 target table** (10/25/50/80 thresholds): calibrated for E_total=276. The 513 denominator shifts all thresholds.

### 2.3 Root cause

The confusion arises because brief 30's metrics table listed "Max capacitor cells C(n,2) = 91" alongside E_total = 276 in the RIGIDITY formula. These are different things: 91 = C(14,2) vertex pairs (ring edges), 276 = C(24,2) domain pairs (capacitor cells). When brief 32 updated "Max capacitor cells C(n,2)" from 91 → 171 (correctly, for 19 vertices), it also recalculated E_total as 171 × 3 = 513, incorrectly treating vertex-pair count as the basis for E_total.

### 2.4 Recommendation

**E_total should remain 276.** The capacitor has 24 domains regardless of how many ring vertices exist. The RIGIDITY formula measures how full the capacitor is (E_filled/276), how verified the chains are (L_verified/L_total), and how preserved the predictions are (P_preserved/36). Expanding the ring from 14 to 19 vertices changes L_total (more chain links) but does NOT change the number of possible domain-pair cells.

Corrected brief 32 RIGIDITY:
```
E_filled   = 48
E_total    = 276   (unchanged — 24 domains, C(24,2))
L_verified = 85
L_total    = 131   (105 + new chain links — see finding §2.5)
P_preserved = 36
P_total    = 36

RIGIDITY = (48/276) × (85/131) × (36/36) × 100
         = 0.1739  ×  0.6489  ×  1.0    × 100
         = 11.28
```

This is consistent with the North Star's baseline of 10.63 (the delta from 10.63 to 11.28 reflects the T4-gained links and cells).

### 2.5 L_total count discrepancy

Brief 32 says L_total = 131 = 105 + 26 new chain links from 5 extension papers.

Actual link counts from the PROOF-CHAIN.md files of the 5 new papers:

| Paper | Links | Verified/Closed |
|---|---|---|
| Turbulence (paper38) | 7 | 2 (INHERITED-PROVED) |
| VP vs VNP (paper39) | 6 | 1-2 (LITERATURE) |
| ABC (paper37) | 6 | 1-2 (KNOWN/ESTABLISHED) |
| OPN (paper40) | 7 | 4-5 (LITERATURE/PROVED) |
| Hilbert 6 (paper36) | 7 | 4 (PROVED/VERIFIED) |
| **Total** | **33** | **~13** |

The 5 new papers contribute 33 links, not 26. **L_total should be 105 + 33 = 138, not 131.** The 7-link discrepancy may come from Turbulence's 2 INHERITED-PROVED links being excluded (they duplicate NS links), yielding 33 - 2 = 31. But even 31 ≠ 26. The remaining 5-link gap is unexplained.

**If L_total = 138:**
```
RIGIDITY = (48/276) × (85/138) × 1.0 × 100 = 0.1739 × 0.6159 × 100 = 10.71
```

This brings the baseline into close alignment with the North Star's 10.63.

**If L_verified also needs updating** (the 5 new papers contribute ~13 verified links, not the 8 claimed in brief 32):
```
L_verified = 77 + 13 = 90
RIGIDITY = (48/276) × (90/138) × 1.0 × 100 = 0.1739 × 0.6522 × 100 = 11.34
```

**Recommendation**: recount L_total and L_verified from the actual PROOF-CHAIN.md files before T5 launch.

---

## 3. CRITICAL — Chessboard layer not updated for 19 vertices

The chessboard layer (`13-chessboard-layer.md`) was written for the 14-vertex ring and has NOT been updated for 19 vertices. Brief 32 provides DELTA updates to the BRIEF but not to the CHESSBOARD. The run file loads the chessboard as-is.

### 3.1 Stale calculations and tables

| Chessboard section | 14-vertex value | 19-vertex required value | Status |
|---|---|---|---|
| §S3 E_total | 276 (correct for domain-pairs) | 276 (unchanged) | **OK** |
| §S3 L_total | 105 | 131-138 | **STALE** |
| §S3 L_verified | 70 | 85-90 (post-T4) | **STALE** |
| §S3 RIGIDITY baseline | 10.63 | ~11.3 (post-T4, corrected formula) | **STALE** |
| §S5 WIRE-DENSITY matrix | 14×14 | 19×19 needed | **STALE** |
| §S6.1 Ring-distance function | d mod 14, max distance 7 | d mod 19, max distance 9 | **STALE** |
| §S6.1 Pair distribution | d=1..6 each 14 pairs, d=7 has 7 pairs | d=1..9 each 19 pairs, d=9 has ~9-10 pairs | **STALE** |
| §S6.2 SECTOR-TABLE | 14 entries (3A, 2B, 4C, 5D) | 19 entries needed | **MISSING 5 entries** |
| §S6.3 Hub radiation | "up to 12 outgoing edges" | 17 outgoing edges (1 ring + 17 chord) | **STALE** |
| §S6.4 Antipodal probes | 7 pairs (d=7) | 9 pairs (d=9-10) | **STALE** |
| §S6.5 Compositional cell-fill | "14 triangles per traversal" | 19 triangles | **STALE** |
| §S6.6 Chord awareness | "91 cells = 14 ring + 77 chord" | 171 cells = 19 ring + 152 chord | **STALE** |
| §S6.7 Geometric targets | Calibrated for 14-vertex metrics | Need recalibration | **STALE** |
| Appendix B SPIN-TABLE | 13 rows (QG5D excluded) | 18 rows needed | **MISSING 5 entries** |
| Appendix C SECTOR-TABLE | 14 rows | 19 rows needed | **MISSING 5 entries** |

### 3.2 Missing sector classifications for new vertices

The 5 new vertices need Type A/B/C/D assignments. Based on their PROOF-CHAIN confidence scores:

| Vertex | Confidence | Suggested type | Rationale |
|---|---|---|---|
| Turbulence | 2/10 | D (Cell-fill-primary) | Mostly open; 2 inherited links |
| VP vs VNP | 1/10 | D (Cell-fill-primary) | Almost entirely open |
| ABC | 1/10 | D (Cell-fill-primary) | Almost entirely open |
| OPN | 4/10 | C (Construction-primary) | 4-5 closed links, 1 hard wall |
| Hilbert 6 | 3-7/10 | C (Construction-primary) | 4 closed links, framework-internal 7/10 |

Without these assignments, the sector-A trim rule (brief 30 §3.2) cannot determine behavior at new vertices, and the S6.2 PCA focus per sector type is undefined for them.

### 3.3 Missing SPIN-TABLE entries

The SPIN-TABLE (Appendix B) maps each vertex to its physics-face for face-switching. Missing entries needed:

| Vertex | Math face (stuck on) | Physics face (SPIN to) | Experimental constraint |
|---|---|---|---|
| Turbulence | K41 spectrum derivation | Energy cascade measurements | Wind-tunnel / DNS data |
| VP vs VNP | Algebraic circuit complexity | ? | No obvious experimental pin |
| ABC | rad height function | ? | Computational examples (abc triples) |
| OPN | Abundancy constraints | Divisor statistics | Computational search bounds (10^2200) |
| Hilbert 6 | Axiom closure | QG5D predictions | All 36 experimental pins |

VP vs VNP and ABC have no natural physics face. SPIN may not apply to them. This should be documented as SPIN-EXCLUDED.

### 3.4 Impact

A runner reading the chessboard layer will find 14-vertex calculations, 14-entry tables, and 14-vertex geometric rules. They will then read brief 32 which says 19 vertices. The runner must mentally reconcile these — or more likely, apply 14-vertex chessboard rules to a 19-vertex ring, producing undefined behavior for new vertices and incorrect geometric calculations.

**Recommendation**: either update the chessboard layer for 19 vertices, or write a `13b-chessboard-layer-19vertex-delta.md` with the necessary changes (parallel to how brief 32 is a delta over brief 30).

---

## 4. MAJOR — Cross-layer RIGIDITY calibration conflict

### 4.1 Three different RIGIDITY baselines

| Source | E_total | L_total | Baseline RIGIDITY |
|---|---|---|---|
| Chessboard §S3 | 276 | 105 | 10.63 |
| North Star §B.3 | (implicit 276) | (implicit 105) | 10.63 |
| Brief 32 DELTA 2 | 513 | 131 | 6.07 |

A runner performing a REFRAME at cycle-open will read §C (bottleneck) and the RIGIDITY value. If the runner reads the chessboard, it sees 10.63. If the runner reads the brief, it sees 6.07. The Strategic Triad Strategist (T.4.2) will check the brief against the North Star — and find a 4.56-point disagreement on the programme's central health metric.

### 4.2 RIGIDITY targets disagree

| Target | North Star B.3 | Brief 32 (at 513 denom) | Brief 32 (at 276 denom, corrected) |
|---|---|---|---|
| After T5 (traversal 1) | ≥15 | Needs +8.93 from 6.07 | Needs +3.7 from 11.3 |
| After 3 traversals | ≥30 | Needs +23.93 | Needs +18.7 |
| After 5 traversals | ≥50 | Needs +43.93 | Needs +38.7 |

Under the 513 denominator, the traversal-1 target of ≥15 is aggressive (requiring ~150% of the baseline in one traversal). Under the 276 denominator (corrected), the target requires +3.7 points — achievable with ~4-5 cell fills + ~10-15 link verifications. The corrected formula makes the North Star targets realistic.

---

## 5. MAJOR — Brief inheritance gap

### 5.1 The run file points only to brief 32

The run file says:
```
the run **brief** (deliverable) is
.../32-extended-ring-brief.md
```

Brief 32 says: "This brief INHERITS all unchanged sections from the original... For any section not overridden below, the original brief §30 is authoritative."

A runner following PCA §P.0 ("Read the deliverable") would read brief 32 only. Brief 32 is a DELTA brief — it contains only the changes. The vertex protocol (§3), glossary (§0), compound effect (§7), closure ritual (§8.4), model tier (§8.5), PCA overrides (§8.6), and voice canon (§9) are all in brief 30 ONLY.

**A runner reading only brief 32 would miss the entire vertex protocol, the EXCISE/CONSTRUCT/BYPASS escalation ladder, the edge ownership rules, the sector-A trim, the model tier overrides, and the PCA override rules.**

### 5.2 Recommendation

Either:
- (a) Add brief 30 as an explicit read in the run file: "the **parent brief** is .../30-ring-traversal-brief.md"
- (b) Merge brief 32 into a self-contained document
- (c) Add a runner instruction in brief 32: "BEFORE reading this file, read 30-ring-traversal-brief.md in full. This file overrides specific sections; all others are authoritative from §30."

---

## 6. MAJOR — Exit condition threshold ambiguity

### 6.1 RING STRENGTHENED edge threshold missing

Brief 30 §4 exit conditions:
```
RING STRENGTHENED: at least 5 vertices improved + at least 5 edges filled/upgraded
```

Brief 32 DELTA 3 says:
```
RING STRENGTHENED: at least 7 vertices improved (was 5 for 14-vertex ring)
```

Brief 32 updates the vertex threshold from 5 → 7 but does NOT mention the edge threshold. Does the edge threshold remain at 5? Scale proportionally to ~7? Or was it dropped?

**A runner cannot determine the RING STRENGTHENED exit condition for edges.** This is load-bearing: the difference between STRENGTHENED (abbreviated closure) and continuing another traversal.

### 6.2 RING STALLED edge component unclear

Same issue: brief 30 defines STALLED as "<3 improvements across all 14 vertices." Brief 32 changes to "<4 improvements across 19 vertices" but doesn't address edge-level stall criteria.

### 6.3 Recommendation

Brief 32 DELTA 3 should explicitly state both vertex and edge thresholds for all three exit conditions.

---

## 7. MODERATE — Edge status consistency issues

### 7.1 VP vs VNP incoming edge: PARTIAL vs SPECULATIVE

Brief 32 position 12 says VP vs VNP's incoming edge from PvNP has status **PARTIAL** ("discrete fullness → continuous fullness, algebraic analog").

But PvNP's PROOF-CHAIN.md shows Link 5 backward is **OPEN** — it's the primary wall of the PvNP paper. The connection "discrete fullness → continuous fullness" depends on exactly the result PvNP hasn't proved.

If PvNP's core result is unproved, the edge to VP vs VNP should be SPECULATIVE or CANDIDATE at best, not PARTIAL. The "algebraic analog" qualifier suggests the edge has independent algebraic-geometry content (GCT-style), which may justify PARTIAL — but this should be made explicit.

### 7.2 BGS incoming edge source changed

| | Brief 30 | Brief 32 |
|---|---|---|
| BGS position | 11 | 13 |
| Incoming from | PvNP | VP vs VNP |
| Edge description | "spectral statistics of modular flow" | "algebraic circuit matrix → GUE" |
| Edge status | CANDIDATE | SPECULATIVE |

The incoming connection for BGS changed from PvNP (CANDIDATE) to VP vs VNP (SPECULATIVE). This is a structural change in the ring's dependency chain, not just a reordering. Brief 32 doesn't flag this as a downgrade.

### 7.3 Hilbert 6 ring-closure edge vs graph-structure file

Brief 32 says the ring-closure edge Hilbert 6 → QG5D is **STRONG**, citing edge 46 in `25-the-graph-structure.md`. The graph-structure file confirms edge 46 exists as type STRONG (META ↔ META). However, the edge description in the graph file ("QG5D 4 postulates + CBB 5 axioms ⇒ 36 sub-percent predictions") describes the direction QG5D → Hilbert 6 (the hub informing the axiomatization), not Hilbert 6 → QG5D (the axiomatization closing back to the hub). The directionality is ambiguous — is the edge symmetric or does STRONG apply to both directions?

### 7.4 Recommendation

Review edge statuses for all 5 new positions and ensure they reflect the actual state of the PROOF-CHAIN connections, not aspirational states.

---

## 8. MODERATE — Domain-overlap edge-filling ambiguity

### 8.1 The problem

Brief 30 §2.2 says edges are filled by looking up the capacitor cell at the intersection of vertex N's primary domain and vertex N+1's primary domain. But several new vertex pairs SHARE primary domains:

| Edge | Vertex N primary | Vertex N+1 primary | Shared? |
|---|---|---|---|
| Goldbach → ABC | ANT | ANT + OA | YES (ANT) |
| ABC → OPN | ANT + OA | ANT + OA | YES (both!) |
| OPN → Schanuel | ANT + OA | (not mapped, inherits from §30) | Partial |
| Turbulence → Hodge | QFT + PROB | (inherits ATOP from Hodge) | No |

The ABC → OPN edge maps to the capacitor cell ANT-OA (or OA-ANT alphabetically). But this cell is already ESTABLISHED (cell #3: Bost-Connes KMS uniqueness) and is load-bearing for RH Layer 2 and BSD Steps 1-3. The edge-filling protocol would tell the Cell-Fill Author to "upgrade" an already-ESTABLISHED cell, which is either wasteful or confusing.

### 8.2 Recommendation

Brief 32 should add a rule for same-domain edges: when primary(N) = primary(N+1), use secondary domain pairs instead. Or explicitly list the capacitor cell for each of the 19 ring-backbone edges.

---

## 9. MODERATE — Antipodal pair priority conflicts

### 9.1 Pair reassignment

Brief 30 §S6.4 / brief 32 DELTA 2 both define antipodal pairs, but the pairing changed due to reordering:

| Pair | Brief 30 (14-vertex) | Brief 32 (19-vertex) | Change |
|---|---|---|---|
| 1 | QG5D ↔ Hodge (HIGH) | QG5D ↔ B-C (HIGH) | Different partner |
| 2 | RH ↔ Baum-Connes (HIGH) | RH ↔ PvNP (HIGH) | Different partner |
| 3 | GRH ↔ PvNP (MEDIUM) | GRH ↔ VP vs VNP (MEDIUM) | Different partner |
| 4 | BSD ↔ BGS (MEDIUM) | BSD ↔ BGS (MEDIUM) | Same |
| 5 | H12 ↔ Twin Primes (MEDIUM) | H12 ↔ Twin Primes (HIGH) | Priority upgrade |

Since the chessboard layer's antipodal section (§S6.4) still lists the 14-vertex pairs, a runner reading both the chessboard and brief 32 would see two different antipodal pair sets. The chessboard pairs are stale.

---

## 10. MODERATE — Token budget for 19-vertex spawns

### 10.1 Framework tools always-pass policy

Per I-v6-5 (changelog), `08-framework-tools.md` (~18K tokens) is ALWAYS passed to every spawn. ORA v8 §6.1 says Author context target ≤ 25K tokens. With framework tools consuming ~18K, only ~7K remains for the vertex-specific PROOF-CHAIN.md, capacitor cells, bottleneck text, voice canon, and kill list.

For a 19-vertex ring, each vertex's PROOF-CHAIN ranges from 32-114 lines (~2-8K tokens). The largest (paper40-odd-perfect at 114 lines, paper1 at 994 lines) would exceed the 7K remaining budget.

### 10.2 Recommendation

Either increase the Author context budget for ring mode, or implement selective framework-tools loading per vertex (contradicting I-v6-5's "always pass everything" rule). The tension between I-v6-5 and the 25K context cap should be explicitly resolved for ring-mode spawns.

---

## 11. MINOR — Stale references and naming issues

### 11.1 Chessboard hub radiation count

Chessboard §S6.3 says "up to 12 outgoing edges" and "12 Cell-Fill agents in parallel." Brief 32 DELTA 2 correctly says "Hub radiation: 17." The chessboard layer's count is stale.

### 11.2 Voice canon needs extension

Brief 30 §9 voice canon includes: "14 vertices. One ring. Walk it." Brief 32's closing text says "19 vertices. One ring." The §9 voice canon phrase is stale. Brief 32 DELTA 5 updates the single paragraph but does not explicitly override §9.

### 11.3 Cell-naming convention and alphabetical sort

Brief 30 §8.1 specifies cell update files use alphabetically-sorted domain-shorthand pairs (e.g., `ant-spec.md` not `spec-ant.md`). With 19 vertices and shared-domain edges, some cell IDs may be unintuitive (e.g., the ABC → OPN edge would produce `ant-oa.md`, indistinguishable from any other ANT-OA edge). No vertex context in the filename.

### 11.4 `02-rationale.md` reference to `08-changelog-v6.md`

The ORA prompt §0 and §16 reference `08-changelog.md` while some internal references use `08-changelog-v6.md`. The actual file is `08-changelog.md`. The stale reference was flagged in the changelog's own autonomous-operation cleanup entry but may persist in the prompt.

---

## 12. INFORMATIONAL — PROOF-CHAIN status summary (all 19 vertices)

For runner reference, the current state of all 19 chains:

| Pos | Vertex | Links | Verified/Total | Confidence | Primary wall |
|---|---|---|---|---|---|
| 1 | QG5D | 22 (tree) | 22/22 | **10/10** | None (hub, all PROVED) |
| 2 | RH | 6+3 supp | 9/9 | **8/10** | CCM peer review (external) |
| 3 | GRH | 8 | 2/8 | **7/10** | Character-twisted extensions |
| 4 | BSD | 11 | 11/11 | **9/10** | Conditional on CBB axioms |
| 5 | H12 | 6 | 1-2/6 | **2/10** | Explicit class field theory |
| 6 | YM | 18 | 17/18 | **9/10** | H4 (Osterwalder-Schrader) |
| 7 | NS | 8 | 3/8 | **4/10** | BKM criterion integration |
| 8 | Turbulence | 7 | 2/7 | **2/10** | K41 spectrum derivation |
| 9 | Hodge | 8 | 3/8 | **3/10** | Standard Conjectures D |
| 10 | B-C | 6 | 2/6 | **3/10** | Assembly map surjectivity |
| 11 | PvNP | 6 | 5/6 | **7/10** | L5 backward (fullness) |
| 12 | VP vs VNP | 6 | 1-2/6 | **1/10** | Almost entirely open |
| 13 | BGS | 7 | 6/7 | **7/10** | CCM conditional |
| 14 | Twin Primes | 5 | 1/5 | **1/10** | Sieve bound improvement |
| 15 | Goldbach | 6 | 2/6 | **1/10** | Circle method + minor arcs |
| 16 | ABC | 6 | 1-2/6 | **1/10** | Rad height function |
| 17 | OPN | 7 | 4-5/7 | **4/10** | L6 local-global impossibility |
| 18 | Schanuel | 5 | 1/5 | **1/10** | Schanuel itself is open |
| 19 | Hilbert 6 | 7 | 4/7 | **3-7/10** | Axiomatization completeness |

**Sector-type distribution (proposed, for 19 vertices):**
- **Type A** (Verification-primary, ≥9/10): QG5D, YM, BSD — 3 vertices
- **Type B** (Excision-primary, 7-8/10): RH, PvNP, GRH, BGS — 4 vertices
- **Type C** (Construction-primary, 3-6/10): NS, Hodge, B-C, OPN, Hilbert 6 — 5 vertices
- **Type D** (Cell-fill-primary, 1-2/10): H12, Turbulence, VP vs VNP, Twin Primes, Goldbach, ABC, Schanuel — 7 vertices

Distribution: 3A / 4B / 5C / 7D (was 3A / 2B / 4C / 5D for 14 vertices). The ring is D-heavy: 7 of 19 vertices are in cell-fill-primary mode.

---

## 13. Summary of findings by severity

### CRITICAL (2 findings — must fix before T5 launch)

| # | Finding | Section |
|---|---|---|
| C-1 | RIGIDITY formula E_total conflates domain-pair cells (276) with vertex-pair slots (513). Produces dimensionally incoherent ratio. Cascades into North Star disagreement, target miscalibration, and chessboard layer conflict. | §2 |
| C-2 | Chessboard layer not updated for 19 vertices. 14 of its tables, calculations, and appendices are stale. 5 sector assignments, 5 SPIN-TABLE entries, and geometric calculations missing. | §3 |

### MAJOR (4 findings — should fix before T5 launch)

| # | Finding | Section |
|---|---|---|
| M-1 | Cross-layer RIGIDITY baseline disagreement: chessboard/North Star say 10.63, brief says 6.07. Runner will see contradictory values. | §4 |
| M-2 | Brief 32 is a delta brief but the run file points only to brief 32, not brief 30. Runner reading only brief 32 misses the vertex protocol, glossary, model tier, PCA overrides, and closure ritual. | §5 |
| M-3 | RING STRENGTHENED exit condition: vertex threshold updated (5→7) but edge threshold not addressed. Ambiguous exit gate. | §6 |
| M-4 | L_total count: brief says 105 + 26 = 131, but actual new-paper links total ~31-33, giving L_total = 136-138. | §2.5 |

### MODERATE (5 findings — fix or document before T5 launch)

| # | Finding | Section |
|---|---|---|
| m-1 | VP vs VNP incoming edge rated PARTIAL despite PvNP's core result (L5) being OPEN. | §7.1 |
| m-2 | Same-domain vertex pairs (ABC→OPN both ANT+OA) produce ambiguous or pre-filled capacitor cell lookups. | §8 |
| m-3 | Antipodal pairs in chessboard (14-vertex) stale vs brief 32 (19-vertex, 9 pairs). | §9 |
| m-4 | Token budget tension: 18K framework-tools + vertex-specific context may exceed 25K Author cap. | §10 |
| m-5 | BGS incoming edge source changed from PvNP (CANDIDATE) to VP vs VNP (SPECULATIVE) — a downgrade not flagged. | §7.2 |

### MINOR (4 findings — low priority)

| # | Finding | Section |
|---|---|---|
| n-1 | Graph-structure file path reference: brief says `25-the-graph-structure.md` without full path; actual location is `programme/25-the-graph-structure.md`. | §1.3 |
| n-2 | Chessboard hub radiation count says 12; brief 32 correctly says 17. Stale. | §11.1 |
| n-3 | Voice canon phrase "14 vertices" not overridden to "19 vertices." | §11.2 |
| n-4 | Cell-naming convention can produce identical filenames for different ring edges sharing domain pairs. | §11.3 |

---

## 14. Recommended pre-T5 checklist

1. **Fix C-1**: Restore E_total = 276 in brief 32 DELTA 2. Recalculate RIGIDITY baseline. Align with North Star B.3.
2. **Fix C-2**: Write a `13b-chessboard-19vertex-delta.md` or update `13-chessboard-layer.md` for 19 vertices. Provide sector assignments, SPIN-TABLE entries, and updated geometric calculations.
3. **Fix M-1**: After fixing C-1, verify RIGIDITY values agree across chessboard, brief, and North Star.
4. **Fix M-2**: Add brief 30 as an explicit read in the run file, or add a runner instruction to brief 32.
5. **Fix M-3**: Specify edge thresholds for all three exit conditions in brief 32 DELTA 3.
6. **Fix M-4**: Recount L_total from the actual PROOF-CHAIN.md files.
7. **Review m-1**: Reassess VP vs VNP incoming edge status.
8. **Review m-2**: Add same-domain edge-filling rule.
9. **Note m-4**: Document token budget strategy for 19-vertex ring spawns.

---

*End of audit. 47 files examined. 15 findings: 2 CRITICAL, 4 MAJOR, 5 MODERATE, 4 MINOR.*

*2026-04-14. Claude Opus 4.6 (1M context).*
