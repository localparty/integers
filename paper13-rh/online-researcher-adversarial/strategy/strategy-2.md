# Strategy — Cycle 2 (tuned, Round 003)

*Strategist: ORA tuned-prompt run, 2026-04-10.*
*North star: prove RH from inside the Bost–Connes algebra.*
*Prior cycle: Cycle 1 produced 3 ADVANCED → WEAKENED, 1 BLOCKED; ledger has been updated with the 5-sub-bottleneck decomposition; Round 003 edits applied.*

---

## Reading of the ledger

**What carries over from Cycle 1.**

- **§A north star** unchanged. Chain self-grade 5/10, OPEN.
- **§C bottleneck** decomposed into five named sub-bottlenecks
  (SB-1, SB-3, SB-4, Q2-outer, precision-floor). The high-level
  framing "CCM finite→infinite transfer wall" is intact; the
  five sub-items are the load-bearing structure for Cycle 2.
- **§D toolkit** gained four new rows
  (`CCM-page-14-15-inconsistency`, `Precision-floor-rule`,
  `Ladder-tail`, `Gate-II`) plus the Min-dps column. The
  Connes-Letter-2026 and CCM-2025 rows now carry
  Min-dps = 200, matching Connes' own numerics.
- **§G live leads.** L1 at 6/10 (still strongest CCM-arc lead,
  weakened by Bögli misquote + Gate II elision + precision-floor
  yellow card). L2 at 4/10 (matrix construction bug, §6.6
  two-items-not-one). L3 at 7/10 (unexpected climb — K9
  re-entry gate robustly closed by the three-ladder witness;
  SB-4 ladder tail added). L4 at 2/10 (BLOCKED, retire).
- **§H bottleneck history** gained SB-3 (Gate II), SB-4
  (ladder tail), CCM p.14/p.15 inconsistency, precision-floor.

**What is ALIVE for Cycle 2.** The CCM arc — the combined
assembly of L1+L2+L3 into a single spectral-exactness +
simple-even + completeness chain on the CCM third space
L²([λ⁻¹,λ], d*u). Four open sub-steps (SB-1, SB-3, SB-4, Q2-outer)
and one operating discipline (precision floor).

**What is RETIRED.** L4 (BC-ITPFI → Yakaboylu orthogonal
insurance). Its purpose was to satisfy the 3/4 = 75% fan-out
rule in Cycle 1. Post-Phase-3 the L4 BLOCKED verdict stands,
and the re-entry gate ("needs a new external construction")
has not been satisfied. Archived at feasibility 2/10.

**What is DEAD.** §F's 19 killed approaches unchanged; no
new kills in Cycle 1 (3 WEAKENED + 1 BLOCKED is not a kill).

---

## Web scan findings

Queries run this cycle (≥3 per Role 1 (b)):

1. "Connes Consani Moscovici zeta spectral triples 2026 Gate II
   k_lambda theta_x approximation"
2. "Boegli discrete compactness uniform parameter 2026 spectral
   exactness non-selfadjoint"
3. "Fourier ladder eigenvalues spectral truncation tail removal
   finite rank asymptotic arXiv 2026"
4. '"Connes" "Weil quadratic form" "simple" "even eigenvector"
   prolate 2026'
5. '"prolate spheroidal" "simple eigenvalue" "even" rigorous
   proof 2025 Connes Moscovici'

**New findings.**

- **ResearchGate pub 395962447: "New eigenfunctions for the negative
  part of the Connes–Moscovici prolate spectrum" (2025).** Also the
  "A complex analytic approach of the Connes–Moscovici prolate
  spectrum" Global NCG Seminar talk (2025). These report a rigorous
  proof that the negative eigenvalues of the prolate spheroidal
  operator P W_λ — which is the "analogue of the simple-even
  property" cited in Connes-Letter §6.6 — ARE indeed negative as
  conjectured, plus an efficient computational method via complex
  analytic functions. Published in *Comptes Rendus. Mathématique*
  Vol 363 (2025). This directly sharpens CCM §8 "indication (1)":
  the prolate analogue IS now proved at higher grade. Load-bearing
  for **L6** because the Gate II analogy to the prolate case is
  exactly where CCM §8 points for evidence.

- **Bögli 2017 (arXiv:1604.07732) is still the state of the art.**
  No 2026 Q1/Q2 follow-up changes the definitions used by L1/L5.
  The pre-loaded PDF at `sources/boegli-spectral-pollution-2017.pdf`
  (moved from the WebFetch cache during Cycle 1 Phase 4) is
  sufficient. No new Bögli follow-up paper is needed; L5 just
  needs to re-quote Definition 2.5 verbatim (the Round 003
  primary-source rule).

- **No 2026 Q1/Q2 paper surfaces that addresses the Fourier-ladder
  tail elimination at the SB-4 level.** The CCM Theorem 5.10 proof
  itself (CCM-2025 page 24) already contains the factorization
  det_reg(D^(λ,N)_log − z) = Det(D^(λ,N)_log|_{E_N'} − z) ·
  det_reg(D^(λ)_log|_{E_N^⊥} − z), and the ladder tail {2πj/L :
  j ∈ ℤ, |j|>N} is identified as the zero set of the SECOND factor.
  This is a structural handle that L7 can use: the ladder tail
  is a separate factor from the "useful" E_N' block, and the
  question is whether the E_N^⊥ factor's contribution stays
  isolated from the Riemann-zero identification when N → ∞.
  No external paper is needed for this; the handle is in CCM-2025
  itself.

**Pre-loaded sources covering the five sub-bottlenecks.**

| Sub-bottleneck | Pre-loaded source covering it | New source needed? |
|:--|:--|:--|
| SB-1 (simple-even on QW^N_λ) | CCM-2025 §3-5, Connes-Letter-2026 §6.6, CCM-2025 §8 indications | No |
| SB-3 (Gate II k_λ ≈ θ_x ≈ ξ̂) | Connes-Letter-2026 §6.4–§6.5, CCM-2025 §7 + Lemma 7.3, CCM-2025 §8 | No (plus ResearchGate 2025 prolate item added as cross-reference, not downloaded) |
| SB-4 (ladder tail) | CCM-2025 Theorem 5.10 proof page 24 (the E_N' / E_N^⊥ factorization itself names the tail) | No |
| Q2-outer (uniform discrete compactness in λ) | Bögli 2017, Teschl-gsrc-2026, CCM-2025 Lemma 7.3 | No |
| Precision floor | Internal discipline row | N/A |

**Decision:** no new downloads this cycle. All five
sub-bottlenecks are covered by existing `sources/` or by
passages already identified inside pre-loaded PDFs. Per Round
002 "download only if genuinely new" rule, the ResearchGate
prolate-negativity paper is flagged for Cycle 3 if L6 collapses
and we need to upgrade the prolate-analogue citation to a
post-2024 rigorous source; for now L6 cites CCM-2025 §8
indication (1) + Connes-Letter §6.6's own "the analogue of
this property is known for the prolate wave operator."

---

## Current bottleneck (refined)

The five sub-bottlenecks from §C are load-bearing for the
Cycle 2 fan-out exception; I am NOT collapsing them. I am
making two small refinements to the wording, both of which
sharpen the target without changing the structure:

**SB-1 (refined):** simple-even property of the smallest
eigenvalue of the CORRECT CCM QW^N_λ matrix (per eq 3.10
assembled with the `wL` form of γ_L per `CCM-page-14-15-inconsistency`),
verified numerically at dps ≥ 200 (to stay strictly above the
precision floor observed in Cycle 1 reconciliation),
AND extended to a uniformity claim that supports the λ→∞
limit of the simple-even property on QW_λ. Connes-Letter
Theorem 6.1's hypothesis is for the LIMIT form QW_λ, not for
QW^N_λ; the finite-N verification is evidence for the limit
hypothesis, not a discharge.

**SB-3 (refined):** Gate II has TWO sub-items, which are the
two items of Connes-Letter §6.6 "Remaining steps":
 - **SB-3a:** show that kλ is a sufficiently good approximation of θ_x,
   λ = √x. [§6.6 item (ii); CCM §8 item (2).]
 - **SB-3b:** (already partially available as Fact 6.4 /
   CCM Lemma 7.3) kbλ → Ξ uniformly on closed substrips of
   |ℑ(z)|<1/2. This is *already a theorem* in Connes-Letter
   §6.5 and CCM-2025 Lemma 7.3.
 - The remaining open piece is SB-3a, i.e. the approximation
   of θ_x by kλ itself, not of Ξ by kbλ. **This is the item
   that needs the Archimedean-1/λ + CCM Lemma 7.3 route.**

**SB-4 (refined):** per CCM-2025 Theorem 5.10 proof (page 24),
the regularized determinant factorizes as
det_reg(D^(λ,N)_log − z) = Det(D^(λ,N)_log|_{E_N'} − z)
· det_reg(D^(λ)_log|_{E_N^⊥} − z),
and the ladder {2πj/L : j ∈ ℤ, |j|>N} is the zero set of the
second factor — structurally SEPARATE from the Weil-quadratic-form
block. The open question is whether the second factor can be
isolated in the λ, N → ∞ limit so that the identification
"zeros of ξ̂ = γ_n" is not contaminated by ladder-tail zeros.

**Q2-outer** and **precision floor** unchanged.

---

## Leads for this cycle

### Lead 5 — Fix L1 + re-verify at dps ≥ 200

- **Pattern/toolkit**: `CCM-2025`, `Teschl-gsrc-2026`, `Boegli-2017`,
  `Hurwitz-1893`, `CCM-page-14-15-inconsistency`,
  `Precision-floor-rule`, `Gate-II`.
- **Feasibility**: **6/10** (L1 inherited, with the documented
  fixes).
- **Engages bottleneck**: crosses (same as L1).
- **Rationale**: L1 was WEAKENED in Phase 3 for four specific
  reasons: (a) Bögli Definition 2.5 misquote, (b) Teschl
  Lemma 2.7 hypothesis list hand-waved, (c) Theorem 5.10(iii)
  narrative drift onto Connes-Letter 6.1, (d) Gate II elided in
  the Hurwitz closure. Plus a γ_L diagonal bug (−1.38832·I
  shift) that does not affect eigenvalue gaps but DOES affect
  literal matrix entries and any future computation comparing
  matrices directly. The reconciliation note
  (`research/01-reconciliation-L1-L2-matrix.md`) gives the
  one-line fix for γ_L. Additionally, the Cycle 1 headline
  |γ₁−eig₁| = 1.78×10⁻⁴⁹ at (λ=4, N=30) was observed at
  dps=60, which is below the precision floor observed in
  reconciliation (dps ≥ 150 for simplicity-gap work). The
  re-verification at dps ≥ 200 puts the headline number
  outside the precision-floor discipline zone and meets
  Connes-Letter-2026's operating convention.
- **Treat as OPEN sub-steps**: SB-3 (the Hurwitz closure
  gate) and Q2-outer (the uniform-in-λ discrete compactness)
  are explicitly left as "sub-bottleneck pointers, NOT discharged
  by this lead". L5 does not attempt to close SB-3 (L6 does)
  or SB-4 (L7 does). L5's job is to put the L1 chain on firm
  citation + precision footing.
- **Would close if**: all four fixes land, the chain is
  rewritten as conditional on SB-3 + SB-4 (explicitly, not
  eliding them), the script re-runs at dps ≥ 200 and the
  headline gap/agreement numbers either reproduce at the same
  precision or the lead is DOWNGRADED honestly to reflect the
  true precision-floor situation.
- **Would kill if**: the γ_L fix reveals a SECOND structural
  mistake not caught in reconciliation (e.g., the α_L/β_L
  formulas are ALSO affected by the p.14/p.15 inconsistency);
  the re-run at dps=200 shows that the alleged 10⁻⁴⁹
  agreement is a precision-floor artifact of dps=60 and the
  true agreement is orders of magnitude worse; any of the
  five hypothesis conditions of Teschl Lemma 2.7 fails on
  explicit verification.

### Lead 6 — Attack SB-3 (Gate II) via Archimedean-1/λ + CCM Lemma 7.3

- **Pattern/toolkit**: `CCM-2025` (§7, Lemma 7.3, §8 item 2),
  `Connes-Letter-2026` (§6.4–6.5, §6.6 item ii), `Archimedean-1/λ`,
  `Hurwitz-1893`, `Gate-II`.
- **Feasibility**: **5/10** (structural step, two adversaries
  confirmed its realness, but the reduction is not mechanical).
- **Engages bottleneck**: crosses — directly attacks SB-3.
- **Rationale**: The two adversaries in Cycle 1 (L1 and L2)
  converged on Gate II from different directions:
  L1 Adversary identified it as the missing uniform
  k_λ ≈ ξ̂_{λ,N} step in the Hurwitz closure; L2 Adversary
  identified it as the second item of Connes-Letter §6.6. After
  verbatim re-read of §6.6 I can now state the exact split:
  > "In order to apply Theorem 6.1 one needs to show that
  > the smallest eigenvalue of the Weil quadratic form QW_λ is
  > simple with even eigenvector. The analogue of this property
  > is known for the prolate wave operator. Moreover it still
  > remains to show that k_λ is a sufficiently good approximation
  > of θ_x, λ = √x." (Connes-Letter-2026 §6.6, page 30, verbatim)
  The FIRST item of §6.6 is SB-1 (simple-even on the LIMIT
  QW_λ). The SECOND item is SB-3a (k_λ ≈ θ_x). Fact 6.4 /
  CCM Lemma 7.3 already gives kbλ → Ξ uniformly on closed
  substrips (this is SB-3b in my decomposition and is a
  theorem, not an open step). What is open is that kλ itself
  approximates θ_x before taking Fourier transforms — and the
  operator-side linking of "spec D^(λ,N)_log" to the γ_n via
  Hurwitz needs this direct approximation.
  
  L6's attack: use `Archimedean-1/λ` (the bound
  ‖τ^{(R)}‖ / ‖Σ_p τ^{(p)}‖ = O(1/λ)) plus CCM Lemma 7.3
  (uniform convergence of kbλ to Ξ on compact substrips) to
  derive a quantitative bound on ‖kλ − θ_x‖ (measured in an
  L² or sup norm on [λ⁻¹, λ]) as λ→∞.
- **Investigate**:
  1. What norm does "sufficiently good approximation" mean in
     §6.6 item (ii)? (L² on [λ⁻¹, λ]? Sup on compacts? Weight
     adapted to d*u?)
  2. Can Archimedean-1/λ be transformed into a direct bound on
     ‖kλ − θ_x‖ in that norm?
  3. Does Fact 6.4 + Poisson summation give ‖kλ − θ_x‖ as the
     Fourier-inverse image of an already-bounded quantity?
  4. What role does the prolate-wave approximation (kλ =
     E(hλ), with hλ a combination of h_{0,λ}, h_{4,λ}) play —
     is the approximation exact at the prolate level and only
     approximate at the zeta level?
  5. Is the bound uniform in a compact subset of (strip, λ) or
     does it degenerate at either endpoint?
- **Would close if**: an explicit lemma
  "‖kλ − θ_x‖_{L²([λ⁻¹,λ],d*u)} ≤ C / λ^α for some α > 0,
  uniform on compact substrips |ℑ(z)|<r < 1/2", citing
  Archimedean-1/λ and Fact 6.4 as the two inputs.
- **Would kill if**: the norm in §6.6 item (ii) turns out to
  be a mode that Archimedean-1/λ cannot bound (e.g. a
  Sobolev norm of order > 0); or the approximation is only
  conjectured in §6.4 and no rate is available; or the
  prolate E(hλ) construction has a built-in obstruction that
  makes ‖kλ − θ_x‖ bounded below by an O(1) constant in the
  required norm.

### Lead 7 — Attack SB-4 (ladder-truncation tail)

- **Pattern/toolkit**: `CCM-2025` (Theorem 5.10 proof page 24
  with the det_reg factorization),
  `Ladder-tail` (§D toolkit row), `Precision-floor-rule`.
- **Feasibility**: **6/10** (the structural handle is sitting
  inside CCM Theorem 5.10's proof — the ladder tail is the
  zero set of a SEPARATE factor in the determinantal
  factorization, not interspersed with the useful block).
- **Engages bottleneck**: crosses — directly attacks SB-4.
- **Rationale**: L3 Adversary discovered that at T > 2πN/L
  the count N_op(T) exceeds N(T) by up to +38 at T=100. The
  operator-level interpretation (per CCM 5.10(iii) proof,
  page 24) is that `D^(λ,N)_log` genuinely has ladder-tail
  eigenvalues {2πj/L : j ∈ ℤ, |j|>N}, which appear as the zero
  set of the complementary factor
  det_reg(D^(λ)_log|_{E_N^⊥} − z). These are NOT noise; they
  are real operator eigenvalues that just happen not to match
  any γ_n. L7's job is to prove that in the N→∞ limit the
  ladder-tail factor DECOUPLES from the "useful" factor
  Det(D^(λ,N)_log|_{E_N'} − z) in a way that keeps the
  identification "zeros of Ξ = γ_n" clean. Two possible
  routes:
  
  (a) **Factor-separation route.** The det_reg factorization
      is a product; if we can show that the ladder-tail factor
      contributes a known entire function (sin-like, say
      sin(zL/2) / ∏_{|j|≤N}(1 − z·2π j/L)) whose zeros are
      explicitly at 2πj/L and move to ∞ (or to the full
      2πZ/L lattice) as N→∞, then only the useful-block
      zeros are candidates for γ_n identification. This is a
      clean analytic argument on a known entire function.
  
  (b) **Rescaling route.** For T in a window [0, T_N] with
      T_N → ∞ slower than 2πN/L, the ladder tail is strictly
      above the counting window, so the count on [0, T_N]
      is unaffected. Quantify the required growth rate
      N/T_N → ∞ that makes the "on-window" count exact.
- **Investigate**:
  1. Write down the explicit form of det_reg(D^(λ)_log|_{E_N^⊥} − z).
     Is it a finite product or an infinite one? Does it have
     a known closed form in terms of sin or Gamma?
  2. Does the proof of Theorem 5.10 (page 24) give enough to
     identify this factor as an explicit entire function, so
     that its zeros are *exactly* {2πj/L : |j|>N} and no
     interference occurs with the main block's zeros?
  3. What is the relationship N(T_N) ~ T_N / 2π · log(T_N/2πe) vs
     the ladder-tail onset at 2π(N+1)/L? For completeness
     we need N(T_N) to fit inside [0, 2π(N+1)/L], i.e. T_N ≲
     2π(N+1)/L which gives an asymptotic L N(T_N)/(2π) ≲ N+1.
     With L = 2 log λ, this is a joint condition on (λ, N).
  4. Can the rescaling route be made unconditional, or does it
     require a specific relation (λ, N) → ∞?
- **Would close if**: a lemma "the zeros of the E_N^⊥ factor
  converge, in Hausdorff distance on compact subsets of ℂ, to
  the full lattice 2πZ/L as N→∞, and the zeros of the E_N'
  factor converge to the γ_n" — then Hurwitz on each factor
  separately closes the identification.
- **Would kill if**: the ladder-tail factor is not cleanly
  separable from the main block (e.g. the factorization in
  CCM 5.10 proof is only formal and not a product of two
  well-defined entire functions); or the rescaling route
  requires a growth relation between λ and N that
  is incompatible with the Archimedean-1/λ decay rate needed
  by L6/L5.

### Lead 8 — Rebuild L2 from scratch per reconciliation

- **Pattern/toolkit**: `Connes-Letter-2026`, `CCM-2025` (Prop 4.3,
  Lemma 5.1, Def 5.3, §8 item 2), `AE-simp-N≤20`, `CF-ρ≥4.27`,
  `CCM-page-14-15-inconsistency`, `Precision-floor-rule`,
  `Gate-II`, `γ_E-elim`.
- **Feasibility**: **4/10** (L2 was at 4/10 post-Phase 3
  WEAKENED; the rebuild restores confidence but the underlying
  question — discharging the simple-even hypothesis
  unconditionally — is intrinsically harder than the finite-N
  check L2 performed in Cycle 1).
- **Engages bottleneck**: crosses — attacks SB-1 directly, and
  SB-3a as a cross-reference to L6.
- **Rationale**: L2 was weakened by (a) a γ_L shift bug
  (+0.61496·I) AND a W_R sign bug (/(m−n) vs paper's /(n−m)),
  per reconciliation §3; (b) §6.6 two-items-not-one (executor
  flagged only SB-1, missed SB-3a); (c) the elided
  "zeros on Re=1/2 at every finite cutoff" conflation
  (Theorem 6.1 gives "zeros of η̂ are real", not "zeros of η̂
  equal γ_n"); (d) running at dps=60 instead of dps=150–200.
  L8 rebuilds the matrix construction per reconciliation §3's
  two-line fix, bumps precision to dps ≥ 200 (matching
  Connes), addresses BOTH items of §6.6, and reports
  simplicity/evenness as evidence rather than as a
  bottleneck-cross.
- **Cross-reference to L6**: SB-3a = §6.6 item (ii) is the
  SAME step as L6's target. L6 attacks it from the
  Archimedean-1/λ + Lemma 7.3 angle; L8 acknowledges it as
  a sub-step needed for the "zeros = γ_n" identification
  and DOES NOT attempt to discharge it. Both leads name
  `Gate-II` as their toolkit row. **This cross-reference is
  legitimate because L6 and L8 attack the same open step from
  different angles** (L6 from the approximation side, L8 from
  the CF-simplicity side).
- **Investigate**:
  1. Apply reconciliation §3 fixes: (i) replace the γ_L block
     with `wL(L) = (1/2)(γ_E + log(4π)) − (1/2) log((e^L+1)/(e^L−1))`
     only (no c(L) term); (ii) correct the W_R off-diagonal
     sign from `/(m−n)` to `/(n−m)`. The fixes are at
     `code/lead-2-verify-cf-even-simple.py` lines 159–161 and
     line 167. Cross-check against the direct-from-eq(4.4)
     quadrature `W_R(V_n,V_n) = (γ_E + log(4π(e^L−1)/(e^L+1))) +
     ∫₀^L [e^(x/2) · 2(1−x/L) cos(2πnx/L) − 2]/(e^x − e^(−x)) dx`
     (reconciliation §3 "direct reference" formula).
  2. Bump mp.dps to 200 and re-verify simplicity/evenness at
     (λ, N) ∈ {(2,10), (2,20), (4,15), (4,20), (4,30), (8,30)}.
  3. Record the true simple-even gap at dps=200. Compare to
     the cascade μ_0 ~ 10⁻⁵³, μ_1 − μ_0 ~ 3.78×10⁻⁵⁰, μ_2 − μ_0
     ~ 5.34×10⁻⁴⁷ observed in reconciliation at dps=50. Is the
     gap structure stable at dps=200 or does it collapse further?
  4. Quote Theorem 6.1 and §6.6 verbatim (Round 003 e.1 rule);
     quote item (ii) of §6.6 verbatim and name it SB-3a.
  5. Explicitly state "Theorem 6.1 gives zeros of η̂ on the
     real line — not equal to γ_n at finite N" and route the
     γ_n identification through SB-3a (→ L6).
- **Would close if**: the rebuild passes simplicity/evenness
  at dps ≥ 200 across the full (λ, N) grid AND Theorem 6.1's
  "real zeros of η̂" is cleanly bridged to "γ_n" via SB-3a
  (conditional on L6 landing), with no remaining citation drift.
- **Would kill if**: the rebuild exposes a third independent
  matrix error (e.g. the α_L or β_L formulas are also affected
  by CCM p.14/p.15 inconsistency); simplicity fails at
  dps = 200 for any tested (λ, N); or Theorem 6.1's hypothesis
  list includes a condition that the CCM A_λ does not satisfy
  (e.g. the specific normalization of the Hilbert space
  L²([−L/2, L/2]) vs L²([λ⁻¹, λ], d*u) — the Prop 3.2 isometry
  κ needs to be checked).

---

## Fan-out exception

**Invoked.** All four leads (L5, L6, L7, L8) sit on the CCM
arc. By the integer rule in Role 1 item (f), 4/4 = 100% on a
single construction is a HARD FAIL and should trigger an
orthogonal-insurance spawn before Phase 1.5.

**I am invoking the exception clause in Role 1 item (f):**

> "Exception: after a bottleneck has been crossed and the chain
>  is in assembly mode, convergence to one path is correct and
>  this rule is suspended for that cycle."

The invocation rests on three claims, each of which I can
cite explicitly:

1. **The H₁-vs-H_R wall IS crossed.** Cycle 1 L3's Adversary
   closed the K9 re-entry gate with a clean witness: under
   precision-floor breakdown, the spurious artifacts cluster
   around a THIRD ladder {2πk/L}, geometrically distinct from
   both H₁'s {log n} and the target {γ_n}. This is the cleanest
   possible proof that the CCM third space is not secretly H₁.
   The ledger §H row "H₁-vs-H_R wall (18 kills all reduce
   here)" is marked "Crossed by CCM's third space L²([λ⁻¹,λ])
   per L3's ladder-of-noise witness."

2. **The CCM arc IS the assembly mode.** The programme has a
   single load-bearing path (CCM 2025 + Connes-Letter 2026 +
   Teschl-gsrc 2026 + Bögli 2017 + Hurwitz 1893 + Archimedean-1/λ +
   internal CF-ρ and AE-simp toolkit). The fan-out in Cycle 1
   was 3/4 on the CCM arc (75%, within the soft-warning zone,
   the fourth lead L4 being the orthogonal spawn). Cycle 1
   retired L4 as BLOCKED (orthogonal insurance purpose served).
   With the bottleneck crossed, the path forward is to ASSEMBLE
   the CCM chain's open sub-steps, not to spawn a fresh
   structurally-disjoint route.

3. **The five sub-bottlenecks are sub-steps of ONE named
   bottleneck.** §C is already decomposed into SB-1, SB-3,
   SB-4, Q2-outer, precision-floor. Each of L5, L6, L7, L8
   targets a different sub-bottleneck. Collectively the four
   leads parallelize the assembly work. They are independently
   workable by separate executors — the key test in Role 1
   item (f) — because the sub-bottlenecks are on different
   analytic pieces: L5 on the numerical verification +
   citation discipline, L6 on the Archimedean approximation
   bound, L7 on the determinantal-factor separation, L8 on
   the CF-matrix construction.

**Why this is NOT over-investment.** If all four leads shared
the same toolkit piece and the same analytic object, a single
failure would take them all out. But L5 uses
Teschl-gsrc-2026 + Bögli-2017; L6 uses Archimedean-1/λ +
CCM Lemma 7.3; L7 uses the CCM Theorem 5.10 proof
factorization and the Hurwitz machinery; L8 uses
Connes-Letter Theorem 6.1 + CCM Prop 4.3 + internal
AE-simp-N≤20 / CF-ρ≥4.27. Each lead can fail without
zeroing the others. This is fan-out INSIDE one bottleneck,
not over-clustering on one toolkit row.

**Orthogonal insurance is explicitly DEFERRED.** If Cycle 2
does not make substantive progress on at least two of the
five sub-bottlenecks, Cycle 3 should reopen L4 under a new
re-entry gate (e.g. spawn a Majorana-Rindler side-lead, or a
SUSY-embedding-2025 lead, per the Cycle 1 "What I deliberately
rejected" section).

---

## What I deliberately rejected

1. **Reviving L4 (BC-ITPFI → Yakaboylu) as a Cycle 2 lead.**
   L4 was BLOCKED in Cycle 1 because ω₁ is a state and Ŵ is an
   operator — any BC → Ŵ intertwiner reintroduces K6
   (Weil/Li positivity with the wrong sign) and runs into the
   same wrong-space category error that killed the earlier
   BC-side attempts. The re-entry gate is "needs a new
   external construction"; none has appeared. L4 stays
   archived. Reviving it would squander Cycle 2's
   fan-out budget on a 2/10 lead.

2. **A Majorana-Rindler side-lead (arXiv:2503.09644).** The
   Majorana-Rindler 2025 paper proposes an independent
   spectral realisation of the zeros via deficiency-index /
   boundary-triplet / Krein extension on a (1+1)D Rindler
   space. It is a genuine alternative Hilbert-Pólya route,
   but (a) its relation to the Bost-Connes algebra is
   unclear — it is a competing realisation, not a
   BC-internal route, violating SP1; (b) the Cycle 1
   strategist already flagged it and deferred it; (c)
   spawning it would re-break the fan-out exception by
   splitting the cycle's attention across two disjoint
   arcs just when the CCM arc is in assembly mode. Defer.

3. **A SUSY-embedding-2025 lead.** The SUSY-embedding idea
   reframes Hilbert-Pólya as "zeros are a sparse subsequence
   of a Hamiltonian's spectrum, not the whole spectrum." This
   is structurally orthogonal to the "all zeros are
   eigenvalues" stance of CCM, and attractive for resolving
   the "no spurious eigenvalues" half of the wall by converting
   it into an explicit selection question. But the source
   (ScienceDirect S3050475925008978) is a variational /
   Gaussian-trial-state argument, not a proved operator
   identity — it is a "spectral selection principle to be
   discovered", in its own authors' framing. Too under-developed
   to be a Cycle 2 lead.

4. **A fresh external search for a different spectral
   realization.** Tempting because the CCM arc has five open
   sub-bottlenecks and any alternative realization that
   bypasses one of them would be a straight win. But every
   alternative realization I have surveyed (Majorana-Rindler,
   SUSY-embedding, PW_λ prolate, Meyer, ...) leaves the
   "zeros = γ_n identification" as either an open conjecture
   or a numerical observation, and none of them has the
   property CCM has uniquely: the operator can be WRITTEN
   DOWN in closed form from primes ≤ λ², and the eigenvalues
   have been numerically verified to 50 zeros at 10⁻⁵⁵. This
   is not the moment to change horses.

---

## Precision discipline reminder

**Cycle 2 executors MUST run CCM CF-matrix work at mp.dps ≥ 200.**

The §D `Precision-floor-rule` row records the dps ≥ 1.86·N + 30
rule, AND the higher dps ≥ 150 floor for simplicity-gap
verification (because the cascade of near-zero eigenvalues
μ_0, μ_1 − μ_0, μ_2 − μ_0 observed in reconciliation was
3.78×10⁻⁵⁰, 5.34×10⁻⁴⁷ respectively, below dps=60 = 10⁻⁶⁰
in linear scaling but close enough that second-level
precision artifacts were being reported as gaps). Connes
uses dps = 200 himself; the Min-dps column on
`Connes-Letter-2026` and `CCM-2025` is 200.

**Executors for L5 and L8:** bump mp.dps to 200 and report
the resulting gaps at the new precision. If the true
simplicity gap turns out to be below 10⁻¹⁰⁰ even at dps=200,
declare the simple-even verification "inconclusive at
available precision" and escalate to Strategist for a
Cycle 3 discussion of dps = 400+ feasibility on available
compute. Do NOT report a gap that is within 3 orders of
magnitude of the precision floor (Round 003 e.3 rule).

**Executor for L6:** the Archimedean-1/λ decay rate lives
far above the precision floor, so dps=50 is sufficient for
any numerics. Stay at the default.

**Executor for L7:** the ladder tail is at the operator level,
not the gap level; dps=100 is sufficient for locating ladder
zeros at known positions 2πj/L, and dps=200 is needed only if
L7 computes determinants of the E_N^⊥ factor explicitly.

---

## Next phase handoff

**For the Phase 2 executors:**

### L5 executor
- Start by READING `research/01-reconciliation-L1-L2-matrix.md` in
  full. Apply the one-line γ_L fix per §3 (L1 block: replace
  the `c_plus_w` block with `wL` alone). Verify the fix against
  the direct-from-eq(4.4) quadrature formula in reconciliation §3.
- Re-run `code/lead-1-verify-ccm-convergence.py` at mp.dps = 200.
  Report the headline |γ_1 − eig_1| at the new precision. If the
  agreement is no longer at 10⁻⁴⁹ but at a weaker number, report
  the true number honestly.
- Re-quote Bögli 2017 Definition 2.5 VERBATIM from the PDF at
  `sources/boegli-spectral-pollution-2017.pdf`. The executor L1
  had an operator-insertion error ("A_n x_n" vs Bögli's "x_n");
  fix this.
- Make Teschl Lemma 2.7's hypothesis list EXPLICIT: list the
  five conditions (bounded below A_n; A ≥ γ; J_n Q(A) ⊆ Q(A_n);
  |q_A(ψ) − q_{A_n}(J_n ψ)| ≤ a_n q_{A−γ}(ψ) + b_n ‖ψ‖²;
  a_n, b_n → 0) and verify each one against the CCM E_N → E
  convergence, in writing, at the chain level (not hand-waving).
- Route the Hurwitz closure through Gate II EXPLICITLY
  (NOT through Theorem 5.10(iii), which is self-contained at
  finite N). SB-3 and Q2-outer are NOT discharged by L5; flag
  them as cross-references to L6 and as open sub-steps
  respectively.
- Pattern check against §F must re-verify K9 and K19 safety
  with the corrected construction.

### L6 executor
- READ Connes-Letter-2026 §6.4, §6.5, §6.6, and CCM-2025 §7 +
  §8 "missing steps" BEFORE touching the problem. Quote §6.6
  item (ii) VERBATIM (primary-source rule).
- Write a formal statement: "Target Lemma (SB-3a): ‖kλ − θ_x‖_Ω
  ≤ C/λ^α as λ → ∞, in norm Ω on compact subsets of the
  strip |ℑ(z)| < 1/2, for some α > 0." Identify the correct Ω
  from §6.4 context (almost certainly L²([λ⁻¹, λ], d*u) or a
  weighted sup norm).
- Attempt the derivation:
  (i) use Fact 6.4 / Lemma 7.3 for kbλ → Ξ;
  (ii) invert the Fourier transform (via Poisson summation in
       §6.4) to get kλ − θ_x;
  (iii) use Archimedean-1/λ to bound the remainder in the
       relevant norm.
- If the derivation goes through, the result is a NEW §D
  toolkit row. Propose a canonical name (e.g.,
  `Gate-II-closure`) and a one-line statement.
- If the derivation fails, identify WHICH step fails
  (approximation not in the right norm / rate not O(1/λ^α) /
  prolate approximation residual doesn't vanish) and report
  the failure cleanly.
- Computational kill/advance: if possible, verify a numerical
  proxy — compute ‖kλ − θ_x‖ in a discretized norm at
  λ ∈ {2, 4, 8, 16, 32} and fit a power law. If the fit is not
  O(1/λ^α) with α > 0, the lead is a candidate for KILL.
- Pattern check: Gate II is NOT a shadow of any K-row, but
  the lead must verify that the approximation argument is
  NOT a re-dressed K11 circularity (i.e., do not define kλ in
  a way that secretly uses {γ_n}).

### L7 executor
- READ CCM-2025 Theorem 5.10 proof (pages 23–24) VERBATIM.
  Quote the factorization block and the ladder-tail
  identification block.
- Identify the E_N^⊥ factor det_reg(D^(λ)_log|_{E_N^⊥} − z).
  Is it a finite or infinite product? Does it have a
  closed form?
- Two parallel approaches:
  (a) FACTOR-SEPARATION: prove the E_N^⊥ factor is an explicit
      entire function whose zeros are exactly {2πj/L : |j|>N}
      and whose contribution to "zeros of det_reg = γ_n"
      is disjoint (in the limit) from the E_N' factor's
      contribution. Use Hurwitz on each factor separately.
  (b) RESCALING: find a growth relation N = N(T) such that
      T < 2π(N+1)/L for all T in the counting window, so the
      ladder tail stays above the window and the count is
      "local in T" but asymptotically correct. Quantify the
      minimum rate N(T)/T → ∞.
- Decide which of (a) or (b) is more tractable. (a) is the
  stronger conclusion; (b) is a weaker but possibly-easier
  fallback.
- Computational kill/advance: at (λ, N) = (16, 60), (32, 70),
  (64, 75), compute the spectrum of D^(λ,N)_log at dps = 250
  and verify that the ladder eigenvalues appear EXACTLY at
  2πj/L for |j|>N (no drift). If they drift, the factor
  separation is not clean and the lead is weakened. If they
  sit exactly at 2πj/L, the factor separation is numerically
  confirmed.
- Pattern check: the lead is NOT a shadow of any K-row. K9
  (operator-side Weyl counting on H₁) is explicitly closed by
  the three-ladder witness from Cycle 1.

### L8 executor
- READ `research/01-reconciliation-L1-L2-matrix.md` §3 in full.
  Apply BOTH fixes to `code/lead-2-verify-cf-even-simple.py`:
  (a) replace `gamma_L_int` with the `wL`-only form (drop the
  `cL` block); (b) correct line 167 sign from `/(m−n)` to
  `/(n−m)`.
- Cross-check the corrected matrix against the direct-from-eq(4.4)
  quadrature W_R(V_n, V_n) formula in reconciliation §3 at n=0,1,2,3.
  Must agree to ≥ 40 digits.
- Bump mp.dps to 200 and re-verify simplicity/evenness at
  (λ, N) ∈ {(2,10), (2,20), (4,15), (4,20), (4,30), (8,30)}.
- Report the TRUE simplicity gap at dps=200. The reconciliation
  note's computed cascade (μ_0 ~ 10⁻⁵³, μ_1−μ_0 ~ 3.78×10⁻⁵⁰,
  μ_2−μ_0 ~ 5.34×10⁻⁴⁷) was at dps=50 — it is likely that at
  dps=200 the gaps are still at this magnitude (because the CF
  decay rate is uniform), in which case the simple-even property
  is validly *verifiable* at dps=200.
- Quote Theorem 6.1 AND §6.6 items (i) and (ii) VERBATIM. State
  that Theorem 6.1 alone gives "zeros of η̂ real", NOT "zeros
  of η̂ = γ_n"; the γ_n identification route goes through
  SB-3a (the second item of §6.6), which is L6's target.
- Cross-reference L6 explicitly in the L8 chain: "simple-even
  (this lead) + k_λ ≈ θ_x (L6) → Theorem 6.1 + Hurwitz closure
  → zeros of η̂ = γ_n." The two leads are complementary
  sub-steps of a joint SB-1 + SB-3a closure.
- Pattern check: confirm K6, K2, K10, K16 all cleared (per
  L2's Cycle 1 pattern check, which was correct).

**Cross-lead consistency check** (per Role 3 item d.2):
- L5 and L8 BOTH cite CCM-2025 Prop 4.3 / Lemma 5.1 / Def 5.3.
  After corrections, L5's matrix (corrected L1 matrix) and
  L8's matrix (corrected L2 matrix) should be IDENTICAL up to
  basis conventions. Adversaries must run a byte-for-byte
  cross-lead matrix check at (λ, N) = (4, 30), dps = 200.
- L5 and L6 BOTH cite Archimedean-1/λ. Any quantitative use of
  the O(1/λ) decay by L5 (as a yellow-card for the K9 re-entry
  gate) must be consistent with L6's direct use of it as the
  Gate II approximation rate. Adversaries must check.
- L5, L6, L7, L8 all cite CCM-2025. Adversaries must ensure
  no two leads rely on the SAME theorem number in contradictory
  ways.

**Notation freeze** (from §D). D(λ,N) = D^(λ,N)_log,
QW^N_λ, α_L, β_L, γ_L (per reconciliation, use the `wL`-only
form), W_R (per Prop 4.3, sign `/(n−m)`), ξ, η̂, k_λ, θ_x, Ξ,
ε_N, μ_0, μ_1. Use these names exactly. Do not re-derive.

---

*End of strategy-2.md. Phase 1.5 premise checks are appended to
each lead file directly.*
