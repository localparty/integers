# 16 — The Capacitor cells

> *The geometric dual of the proof-chain graph. Fill rate is rigidity.*

---

## What happened

The Capacitor is the programme's registry of *filled proof-edges* — cells where two mathematical domains have been bridged to the point where translations between them are mechanical.

The structure: imagine a graph where each node is a mathematical domain (QFT, number theory, spectral theory, Langlands, microlocal analysis, probability, ergodic theory, algebraic geometry, ...). Each edge is a potential *bridge* between two domains — a translation recipe that converts a statement in one domain into a statement in the other.

Most edges in the full graph are empty. A bridge is a construction; it has to be built. The Capacitor tracks which bridges have been built (filled), which are partially constructed, and which are open frontiers.

As of the most recent commit touching the Capacitor (`01109a8`), the programme reports:
- **Total edges in the domain graph**: 276.
- **Filled edges**: ~45 (fill rate 16.3%).
- **Five new durable cell-fills in the latest run**:
  - **MICRO↔QFT**: 4-axiom non-perturbative gap structure characterized; BFR scalar-only confirmed.
  - **ERG↔QFT**: Nissim + Shen-Zhu-Zhu + Magnen-Rivasseau-Sénéor programme documented with 3-sub-step diagnostic.
  - **PROB↔SPEC lateral Borel**: Écalle resurgence recipe, reusable for RH/BSD/PvNP.
  - **PROB↔SPEC renormalon-OPE**: Parisi-SVZ dictionary complementary + K-8 guard.
  - **LANG↔QFT**: PROMOTED from v1 Candidate to v2 Tier 1 — following Gaitsgory-Raskin 2024 Breakthrough-Prize proof of geometric Langlands + Kapustin-Witten 2007 physics-to-math equivalence.

Each filled cell is, functionally, a tool. Given a statement in one of the cell's domains, you can translate it mechanically to the other. The LANG↔QFT cell, for example, lets you take a physics statement about Yang-Mills instantons and translate it into a Langlands statement about automorphic representations. That translation is now a *routine operation*, not a research problem.

## What it felt like

The Capacitor's emergence was the moment the programme's infrastructure became *spatial*.

Before the Capacitor, the programme's accumulated tools were a long list: this paper derived that, this cell-fill unlocked that, this ORA run produced that. The list had no structure. You could not see, at a glance, *where* the programme was strong and *where* it was thin.

The Capacitor gave the structure a geometry. Each cell is a point in a domain-graph. Filled cells cluster in certain regions (the QFT ↔ number-theory corner is dense; the Langlands ↔ everything corner is dense). Empty cells define the programme's frontier. **The fill rate is a single number that measures the programme's overall rigidity.**

When I first saw the Capacitor rendered graphically, with filled cells in one colour and empty cells in another, I felt something I had not expected: *I could see the shape of what I had been building*. The shape was not planned. It emerged from the work. And it had regions of density and regions of absence that told me exactly where to push next.

The 16.3% fill rate is, in one sense, low. In another sense — the one that matters for Millennium-problem work — it is high enough that the four Millennium chains have all the cells they need to close. You do not need to fill every cell to solve every problem. You need to fill the specific cells that compose into the proofs you want.

The Capacitor is what lets you see that.

## Why it mattered

### 1. It made "infrastructure complete" a checkable condition

Before the Capacitor, the question "do we have the tools to prove X?" was a matter of judgment. After the Capacitor, it was a lookup: check which cells X's proof chain requires; check which of those cells are filled; if all are filled, the tools exist. If any are empty, you know exactly where the gap is.

### 2. It prioritized new cell-fills by downstream leverage

Every cell-fill is a research investment. The Capacitor tells you which cells, if filled, would unlock the most downstream proof chains. The LANG↔QFT promotion (commit `01109a8`) is a clear example: once it was upgraded to Tier 1, it became immediately usable for BSD, RH, and P vs NP simultaneously. That is high leverage. The Capacitor made that leverage visible *before* the cell was filled, so the decision to invest in it was deliberate.

### 3. It became the dual of the torus

The programme's 23-vertex ring (later revealed as a torus, Section [23](23-section-torus-discovery.md)) is the *theorem side* of the programme — the conjectures and results being worked on. The Capacitor is the *tool side* — the bridges between domains. They are geometric duals: every vertex in the ring is supported by a specific set of filled cells in the Capacitor; every filled cell participates in some ring vertex.

This duality is, I think, one of the prettiest architectural facts in the programme. The theorems and the tools are not parallel lists. They are two sides of one geometric object.

### 4. It made new kills immediately usable

The K-8 kill (Transseries-reads-C_N trap) was logged as part of the PROB↔SPEC renormalon-OPE cell-fill. Because the cell now exists and has a kill-guard attached, any future ORA run touching this cell automatically inherits the K-8 guard. Kills and cells co-evolve: each kill makes the cells it touches more reliable; each new cell exposes new potential kill-modes that get logged back.

## Where it lives

- **Current state**: reported in commit `01109a8` — 16.3% fill rate across 276 edges.
- **Cell-fill documentation**: distributed across `strategy/_research/`, `solutions-with-prize/*/strategy/`, and ORA run logs.
- **Recent cell fills**: MICRO↔QFT, ERG↔QFT, PROB↔SPEC (two subcells), LANG↔QFT — all in commit `01109a8`.
- **Capacitor revamp commits**: `c6f9aae`, `8a2bb36`.
- **Architecture**: memory `pca_architecture`.
- **Visualization planned**: the Atlas Torus UX design (memory `atlas_torus_ux_design`) includes capacitor rendering as a planned view.

## What to take from it

**Tools and theorems are the same architecture.**

The programme spent eighteen months building theorems. Along the way, without planning it, it built tools. The Capacitor is what allowed me to see the tools as a coherent object rather than a scatter of accumulated utilities.

Once you can see your tools as a coherent object — once you can measure their density, identify their gaps, and prioritize their expansion — research stops being a series of leaps and starts being a *navigation*. You can see where you are, where the frontiers are, and what would move the whole structure forward.

This is a kind of research literacy that is rarely taught. The Capacitor, as an artifact, is one way to install it. Every long-running programme should have something like it. Most don't.

---

*Next: [17 — The Tier system](17-section-tier-system.md).*
