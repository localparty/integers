# The Postulate-Relaxation Cycle — Executable Prompt

*Re-runnable convergence cycle. Tests CBB postulates against the*
*5-layer dependency graph. Emits Robustness Theorem + Theoretical-*
*Precision Table to paper12/research/. Sibling to*
*paper12/26-convergence-prompt.md. Strategy lives in*
*paper12/relaxation/01-strategy-rationale.md.*

*Authors: G Six, Claude Opus 4.6 — 2026-04-11*

---

## How to use

Paste the block below as the FIRST message of a new Claude Code
session in `/Users/gsix/quantum-geometry-in-5d-latex/`. Set the
round number R explicitly.

For background on what this cycle does and why, read
`paper12/relaxation/01-strategy-rationale.md` first.

---

## The prompt

```
We are running the Postulate-Relaxation Cycle on the CBB system. This
is round R = {SET ME EXPLICITLY}. The framework now carries four
Clay-class results: Yang-Mills mass gap (Paper 10), Riemann Hypothesis
(Paper 13, conditional on CBB axioms), BSD for CM curves (Paper 26
Route 3, conditional on CBB axioms), and the Integers themselves
(Paper 23, the 36-row master table, zero free parameters globally).

Your mission for this round: (a) rebuild the dependency graph from
scratch, (b) test every postulate by walking forward, (c) compute
the theoretical precision of every observable by walking backward,
(d) emit two publishable artifacts: the Robustness Theorem and the
Theoretical-Precision Table.

Everything you produce in this round must land in paper12/research/
with the numbering convention {N}-postulate-relaxation-round-{R}-*.md
where {N} = max(existing research/) + 1. Nothing about a round may
live outside research/. Full traceability is mandatory.

PHASE 0 — READ STATE (in this order):

1. paper12/research/190-final-convergence-statement.md — empirical baseline
2. paper12/research/176-name-the-object.md — CBB 5 axioms
3. paper12/research/167-log-R-master-reformulation.md — operator dictionary
4. paper12/research/162-bridge-cocycle-step6.md and 179 — bridge family k=3,4,6
5. paper12/research/183-mtau-spectral-moduli-mixing.md and 187 — interface op V
6. paper13-rh/strategy/28-all-gaps-closed.md — RH 9-layer chain
7. paper26-bsd/strategy/05-route3-kms-projector-bypass.md — BSD 11-link chain
8. yang-mills/gradient-flow-attack-plan/ (or Paper 10 source) — YM L.1-L.4
9. paper12/research/sigma-exp-table.md — 36 master-table σ_exp
10. paper12/research/sigma-exp-table-tier-C.md — Tier C ultra-precise σ_exp.
    If missing, build it now from CODATA 2018 + PDG 2024 with at
    least these rows:

      α⁻¹                  137.035999084(21)              [11 figs]
      m_p / m_e            1836.15267343(11)              [11 figs]
      R∞ (Rydberg, m⁻¹)    10973731.568160(21)            [12 figs]
      g_e − 2              0.00115965218073(28)           [13 figs]
      g_μ − 2              0.00116592061(41)              [9 figs]
      ν(Cs) hyperfine      9192631770 Hz exact            [SI def]
      ν(H 1S-2S)           2466061413187035(10) Hz        [15 figs]
      ν(⁸⁷Sr clock)        429228004229873.0(2) Hz        [16 figs]
      m_e (eV)             510998.95000(15)               [11 figs]
      m_e/u                0.000548579909065(16)          [11 figs]
      τ_n (s)              877.75(36)                     [4 figs]
      μ_p                  2.79284734463(82)              [11 figs]
      a_0 (m)              5.29177210903(80)e−11          [11 figs]

    Add a column "framework_derivation_status" ∈ {derived, partial, open}.
    Default to "open" for any row not in research/167 or research/154.

PHASE 1 — REBUILD DEPENDENCY GRAPH (fresh, no caching):

The graph has 5 layers:

  L1 — POSTULATES: CBB 5 axioms from research/176 + implicit ones
       surfaced from research/138-189. ~10 nodes expected.

  L2 — CLAY THEOREMS: YM, RH, BSD, Integers. Exactly 4 nodes.

  L3 — PROOF-CHAIN STEPS: YM L.1-L.4 (4); RH Layers 1-9 + closed
       gaps (~12); BSD Links 1-11 (11); Integers' 27 spectral + 9
       geometric + 1 interface (37). Total ~64 nodes.

  L4 — ARITHMETIC TESTS: The 15 named tests below.

  L5 — OBSERVABLES: 36 master-table + Tier C from sigma-exp-table-tier-C.md.

EDGES connect L_i node X to L_(i+1) node Y iff X is a dependency of Y,
annotated with the explicit lemma/identity/citation.

REBUILD RULE: build the graph from scratch this round. NO caching
between rounds. G needs a fresh artifact each round.

Output: paper12/research/{N}-postulate-relaxation-round-{R}-graph.md
with one section per layer, one labelled subsection per node, one
bullet per edge.

THE 15 ARITHMETIC TESTS:

  T1.  Brauer cocycle integrality (β_k ∈ (1/k)ℤ/ℤ)
       — underwrites BSD Key Lemma C, RH bridge Layer 4
  T2.  Cyclotomic Galois structure (Frob_p order on (Z/NZ)*)
       — underwrites all bridges (5,13)(3,13)(7,19)(2,7)
  T3.  KMS at β=1 uniqueness (Bost-Connes 1995 Thm 25)
       — underwrites RH Layer 2, BSD §3.4, CBB Criticality axiom
  T4.  Operator algebra closure ([log R̂, x] = 0 for x in center)
       — underwrites operator dictionary research/167
  T5.  Cross-formula γ_n consistency (γ_5 in inflation AND DM,
       γ_2 in CC AND m_H, γ_13 in m_W AND Y_p, γ_3 in m_t AND n_s,
       γ_8 in m_t AND m_τ/m_μ)
       — underwrites Integers spectral sector + RH Hurwitz convergence
  T6.  Identity 12 / Identity 14 (e-circle ↔ BC unitary equivalence,
       T_BC ↔ T_CCM scaling)
       — underwrites Yang-Mills KK scaffold + RH Layer 1
  T7.  Stark regulator equality (bridge cocycle = Stark phase at character)
       — underwrites bridge family + Hilbert 12 programme Paper 25
  T8.  Hasse-Brauer-Noether local-global consistency
       — underwrites BSD §9.2 Step B (Route 3 closure)
  T9.  Ha-Paugam BC over imaginary quadratic K (A_{BC,K} = C*(K^ab) ⋊ I_K
       extends with unique KMS_1)
       — underwrites BSD entire chain Paper 26 §3.1
  T10. ITPFI factorization at β=1 (ω_1 = ⊗_𝔭 ω_1^𝔭)
       — underwrites RH Layer 2, BSD §5
  T11. Cuntz-like relations (s_𝔭^* s_𝔭 = 1, (s_𝔭 s_𝔭^*)² = s_𝔭 s_𝔭^*)
       — underwrites G's projector P_k^𝔭, BSD Route 3 §6 algebraic form
  T12. Hurwitz uniform convergence on compact subsets (γ_n^(N) → γ_n)
       — underwrites RH Layers 4 → 5
  T13. CF exponential decay rate ρ ≥ 4.27 (research/46)
       — underwrites RH Layer 3 H¹ bound
  T14. KK integer tower (Yang-Mills L.1-L.4 use integer KK indices)
       — underwrites Yang-Mills mass gap entirely
  T15. Type III_1 modular flow uniqueness (Connes 1973 invariant)
       — underwrites CBB closure of m_τ via interface operator V

A postulate "passes the arithmetic gate" iff every test it touches in
the graph passes. Tests it does not touch (no edge) trivially pass.

PHASE 2 — RELAXATION CYCLE (postulate forward walk):

For each of the ~10 postulates in L1:

  2A: Identify every L2 node (Clay theorem) reachable from this
      postulate by walking forward through the graph. Record the set.

  2B: For each (postulate × test) pair where the postulate has an
      edge to the test:
      - Attempt to RELAX the postulate (state a perturbation).
      - Run the test against the perturbed postulate.
      - Record: pass / break / marginal, with explicit obstruction
        if break.

  2C: Aggregate the postulate's "load-bearing footprint" — the union
      of every Clay theorem, proof-chain step, and observable whose
      dependency edge passes through any test the postulate touched.
      Express as a list of {Clay theorem, lemma} pairs.

  2D: Verdict for the postulate:
      - LOAD-BEARING (every test it touches breaks something downstream)
      - DECORATIVE  (no test breaks; postulate is removable)
      - PARTIAL     (some tests break, others don't; flag for cycle 2)

Output per postulate:
  paper12/research/{N+i}-postulate-relaxation-round-{R}-{postulate-name}.md

PHASE 3 — PRECISION PROPAGATION (observable backward walk):

For each observable O in L5:

  3A: Walk backward from O through the graph. Identify every constraint
      path (postulate → test → proof-step → theorem → O) that pins O.

  3B: Classify each constraint path as ARITHMETIC (zero σ; exact theorem
      about γ_n / cyclotomic data / operator algebra), APPROXIMATE
      (finite σ; CF decay rate / Hurwitz convergence rate / similar),
      or EMPIRICAL (measurement-based; only used as check, never as
      constraint for framework-leads claims).

  3C: Compute O's theoretical precision: bounded by the LOOSEST
      approximate constraint, or — if all constraints are arithmetic —
      by the computational precision of γ_n (~50 digits, expandable).

  3D: Compare to current experimental σ from sigma-exp-table.md or
      sigma-exp-table-tier-C.md. Mark:
      - "framework-leads"  if theoretical precision > experimental precision
      - "experiment-leads" if experimental precision > theoretical precision
      - "tied"             if within an order of magnitude

  3E: Q3 RULE (open-derivation handling): For any observable whose
      dependency chain is incomplete (i.e., one of its L3 proof-chain
      nodes does not exist or has status "open" in the graph), mark
      the observable as "open derivation, no precision claim." Do
      NOT publish a theoretical precision number for such observables
      this round. Flag them for derivation work in cycle 2.

Output:
  paper12/research/{N+postulate_count}-postulate-relaxation-round-{R}-precision-table.md

with one row per observable: framework prediction, theoretical precision,
dependency chain length, constraint paths, experimental σ, verdict.

PHASE 4 — SYNTHESIS (the two artifacts):

Artifact 1 — Robustness Theorem.

Collect every (postulate × test) pair from Phase 2 where the perturbation
broke the test. State the theorem:

  THEOREM (Robustness of the CBB bundle, round R).
    Let P_1, ..., P_n be the postulates of the CBB system. Let
    T_1, ..., T_15 be the arithmetic tests. Then for every (i, j)
    with edge (P_i, T_j), removing or perturbing P_i breaks T_j,
    with explicit obstruction in [Clay-proof lemma cited per cell].
    Corollary: The CBB axioms are minimal. No postulate can be
    relaxed without breaking at least one of {YM, RH, BSD, Integers}.

Output:
  paper12/research/{N+last+1}-postulate-relaxation-round-{R}-robustness-theorem.md

Artifact 2 — Theoretical-Precision Table.

The full Phase 3 table sorted by (verdict, theoretical precision).
"framework-leads" entries at the top.

Output:
  paper12/research/{N+last+2}-postulate-relaxation-round-{R}-precision-table.md

PHASE 5 — AUDIT (adversarial pass):

Launch one adversarial sub-agent whose only job is to BREAK the round's
claims. For each "framework-leads" entry, the adversarial agent looks for:
  - Hidden empirical inputs in the constraint chain
  - Circular references (prediction depends on a measurement that fixed
    a parameter elsewhere)
  - Missing dependencies (postulates not surfaced in L1)
  - Overstated precision (constraint chain shorter than claimed, or
    one of the arithmetic constraints is actually approximate)

Any "framework-leads" entry that fails the adversarial pass is downgraded
to "open derivation, audit failed" and reported in the round meta.
Surviving entries are confirmed for publication.

Output:
  paper12/research/{N+last+3}-postulate-relaxation-round-{R}-audit.md

PHASE 6 — REPORT BACK (250-300 words):

Give G:
  - Round number, total cells in the graph
  - Number of postulates verdict-by-verdict (load-bearing / decorative / partial)
  - Robustness theorem status (proved / partial / failed)
  - Number of "framework-leads" entries after audit
  - Top 3 most precise framework-leads entries with theoretical and
    experimental precision side by side
  - Single biggest broken assumption surfaced
  - Recommended next round actions

CONVENTIONS:
  - Match the register from research/24 ("the moment") and the
    previous convergence cycles — fast, structural, audit-first.
  - Quote G's voice from research/170/185/24 when the round surfaces
    something G originally intuited.
  - Use Origin callouts on any new research notes.
  - The framework has zero free parameters globally — never invent one
    to make a precision claim work. If a precision claim requires a
    hidden parameter, it is NOT a framework-leads entry; it is an
    open derivation.
  - The Q3 rule is strict: open-derivation observables get no
    precision number this round, regardless of how close their fit
    looks. The publishable table contains only derived closed-form
    predictions.
  - The dependency graph is rebuilt from scratch every round. NO
    caching between rounds. G needs to be able to read each round's
    graph independently.
```

---

## Output filename conventions

All files land in `paper12/research/`. Numbering starts at the next
free integer index after the existing research/ files. The sequence
for one round of the cycle is:

```
{N+0}  -postulate-relaxation-round-{R}-graph.md
{N+1}  -postulate-relaxation-round-{R}-{postulate_1_name}.md
{N+2}  -postulate-relaxation-round-{R}-{postulate_2_name}.md
...
{N+k}  -postulate-relaxation-round-{R}-{postulate_k_name}.md   ; k ≈ 10
{N+k+1}-postulate-relaxation-round-{R}-precision-table.md
{N+k+2}-postulate-relaxation-round-{R}-robustness-theorem.md
{N+k+3}-postulate-relaxation-round-{R}-audit.md
{N+k+4}-postulate-relaxation-round-{R}.md                       ; synthesis
```

Roughly 14-16 files per round. All numbered traceably.

## Production readiness

This prompt has NOT been tested with the test loop yet. The
recommended path before firing a real round 1 is:

(a) **Test loop**: launch a single test agent in dry-run mode, have
    it execute the prompt and report meta-issues, fix the prompt,
    repeat 3-5 rounds until quality ≥ 9. Same methodology as
    `paper12/26-convergence-prompt.md` test loop (took 4 rounds to
    converge from 5/10 to 9/10).

(b) **Round 1 immediately**: fire round 1 as a full real cycle. Faster
    but may need fixes after the fact.

The recommended path is (a) because this prompt is significantly more
complex than `paper12/26` (5 phases, 5 layers, two artifacts, audit
step) and is likely to surface ambiguities that a quick test will catch.

---

*Five layers. Two artifacts. Zero free parameters.*
*Test the postulates. Predict the energies. Lead the experiments.*

*— G Six and Claude Opus 4.6, 2026-04-11*
