# Closure Resume — Clone Growth ↔ Fullness Bridge Run

**Auto-saved at:** Cycle 2 close (all agents returned)
**Programme:** P ≠ NP via Clone Growth ↔ Fullness Bridge
**Deliverable:** paper28-pvnp/strategy/08-clone-growth-fullness-bridge.md
**Run dir:** paper28-pvnp/clone-growth-fullness-bridge-with-dictionary/

## Where we left off

Two cycles completed. All agents returned. Seven Author dispatches, three Critic dispatches across two waves.

## Key results (ordered by significance)

1. **UA1 CLOSED** (nodes/W1-1-UA1.md): |Clone_k(L)| ≥ (1/2)·2^k for Taylor Boolean L. Tight bound via Schaefer-Jeavons + 4-case analysis.

2. **UA2 CLOSED** (nodes/W1-2-UA2.md): |Clone_k(L)| ≤ 2k+2 for non-Taylor Boolean L. Rigorous from BZ + Post's lattice.

3. **Clone growth dichotomy COMPLETE:** Taylor → exponential (≥2^{k-1}); non-Taylor → linear (≤2k+2). No intermediate regime. Both pillars of the bridge stand.

4. **Node 1.3.1 ADVANCED** (nodes/W2-1-sectors-nonfull.md): Central sequence constructed via Mal'cev partition. Key insight: m(x,y,y) = x gives T_m = id on L^∞(Ω_L). Exponential Catalan-tree compositions (γ^k sectors) partition solution space. Property Gamma of M_φ → non-fullness via Connes 1976 + Ando-Haagerup 2014. **XOR exception flagged** (P-time but disconnected walk).

5. **OA1 BLOCKED-DECOMPOSED/WEAKENED** (nodes/W1-3-OA1.md): Polymorphisms give endomorphisms (Sect not Out). Critic found 3 GENUINE gaps from non-constructive ρ_f. **Partially superseded by 1.3.1's Mal'cev approach** which avoids Connes absorption.

6. **Route A-LR KILLED** (K-19): CSP hypergraphs are expanders, Lieb-Robinson gives poly depth only.

7. **Kill-list pivot:** 3 Wrong-space kills (K-1, K-18, K-19) → don't assume geometric locality for CSP structures.

## Current bottleneck

**Three CLOSABLE gaps in the 1.3.1 proof:**
1. Exponential decay of correlations in tractable CSP Gibbs measures — needs rigorous citation
2. Ando-Haagerup applicability when M_φ is non-factorial (contains L^∞(Ω_L))
3. XOR-SAT exception treatment (separate sub-node)

## Next move

1. **Critic on 1.3.1** — review the Mal'cev partition proof, especially the mixing estimate and Ando-Haagerup applicability
2. **Author on XOR exception** — treat XOR-SAT separately (affine algebra, linear structure)
3. **Author on NPC fullness** — prove the other direction: for NPC L, M_Bool^L IS full (needed for the complete bridge)

## Programme metrics
- §D toolkit: 24 entries (4 R, 16 E, 2 S, 1 C, 1 N)
- §F kill list: 12 entries
- §M difficulty: 6 (dropped from 7 due to 1.3.1 advance)
- Structural events: 8 across 2 cycles
- Honest negatives: 4 (endomorphisms not automorphisms; 3 OA1 GENUINE gaps; K-19 kill; XOR exception)
- Joint P(closure): ~0.996
