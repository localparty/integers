# Clay Checklist — Master Roll-Up

*Run r02, 2026-04-10. Review of Paper 13 (v2 CCM + ITPFI +
Bögli + Hurwitz).*

This is the master roll-up of the ~30 mandatory checks specified
in the referee instructions. Each line gives the check ID, its
pass criterion in brief, the finding, and the confidence.

Details for each check live in `checks/<group>/<id>.md`.
Underlying per-point analysis lives in `points/`.

---

## CCM — CCM Foundation (5 checks)

| ID | Check | Status | Conf |
|:---|:------|:-------|:-----|
| CCM1 | D_N correctly defined on E_N^+ | **WEAKENED** (even-sector compatibility not proved) | 6/10 |
| CCM2 | Self-adjointness in T-inner product | PASS on CCM authority | 7/10 |
| CCM3 | 10^{−55} at N = 6 | PASS on CCM authority | 8/10 |
| CCM4 | Two missing steps correctly stated | PASS | 9/10 |
| CCM5 | No hidden RH assumption | PASS | 9/10 |

**Group: conditional pass.** Paper 13 inherits three load-bearing
CCM results without independent verification and layers an
even-sector modification whose compatibility is asserted but not
proved.

---

## IT — ITPFI (3 checks)

| ID | Check | Status | Conf |
|:---|:------|:-------|:-----|
| IT1 | Factorization ω_1 = ⊗_p ω_1^{(p)} proved | PASS | 9/10 |
| IT2 | D_log = modular Hamiltonian identification | WEAKENED (asserted, not proved) | 6/10 |
| IT3 | Form convergence from state convergence | WEAKENED (exposition conflates entry-stab with form convergence) | 7/10 |

**Group: structurally pass, exposition issues.** Proof 1 of the
factorization is complete. The downstream "form convergence"
assertion is stronger than ITPFI alone delivers.

---

## ES — Estimates (5 checks)

| ID | Check | Status | Conf |
|:---|:------|:-------|:-----|
| ES1 | Archimedean O(1/λ) | WEAKENED (not rigorous, inherits from research/20) | 5/10 |
| ES2 | Eigenvector approximation O(1/λ) | WEAKENED (gap bound not proved, PNT-tail wrong) | 5/10 |
| ES3 | Uniform H¹ ≤ 2π/L | **PASS at λ ≤ e^π; BROKEN above** | 6/10 |
| ES4 | CF decay ρ ≥ 4.27 | PASS at N ≤ 30; asymptotic uniformity not rigorous | 7/10 |
| ES5 | Rank-one stabilization ‖Δ_N‖ ≤ C ρ^{−N} | CONDITIONAL (research/40 Lemma 1 not in preprint) | 6/10 |

**Group: multiple concrete rigor gaps.** Theorem 7.1's proof
only holds for λ ≤ e^π ≈ 23.14 — a concrete finding I
computationally verified. At the paper's numerical choice λ =
√14, the bounds hold; at any "uniform-in-λ" reading, they do
not. Several other estimates rely on internal research notes.

---

## BG — Bögli (5 checks)

| ID | Check | Status | Conf |
|:---|:------|:-------|:-----|
| BG1 | Teschl form bound a = 0 | CONDITIONAL (δ_N vs Q_∞ not disambiguated) | 6/10 |
| BG2 | KLMN closability | **WEAKENED** (argument has incorrect implication) | 5/10 |
| BG3 | Discrete compactness (H2) | PASS at fixed λ | 8/10 |
| BG4 | Bögli Theorem 2.5 applied | CONDITIONAL (gsrc vs srg, varying Hilbert spaces) | 7/10 |
| BG5 | No spectral pollution | PASS (conditional on compact resolvent) | 7/10 |

**Group: Layer 4 is the weakest link.** The Teschl–Bögli synthesis
is novel and the interface checks are informal. KLMN closability
is argued via an incorrect general implication ("positivity ⇒
closability", which is false in general).

---

## HZ — Hurwitz (4 checks)

| ID | Check | Status | Conf |
|:---|:------|:-------|:-----|
| HZ1 | ξ̂_N → Ξ uniformly on compacts | CONDITIONAL (λ vs N conflation) | 7/10 |
| HZ2 | Hurwitz theorem correctly applied | PASS in principle | 8/10 |
| HZ3 | Zeros of ξ̂_N = eigenvalues of D_N | PASS on CCM authority | 7/10 |
| HZ4 | Zeros of Ξ = {γ_n} | PASS | 10/10 |

**Group: structurally correct, exposition issues.** The Hurwitz
step itself is the right tool, and it would give RH if applied
correctly. **The final deduction in Section 10.4 is tautological
as written**; the intended argument (Hurwitz + real-zero
property of ξ̂_N) is implicit but never explicit.

---

## AE — AE Simplicity (4 checks)

| ID | Check | Status | Conf |
|:---|:------|:-------|:-----|
| AE1 | Overlap real-analytic in λ | PASS | 9/10 |
| AE2 | Certified nonzero at N ≤ 20 | PASS (120-digit) | 9/10 |
| AE3 | Even-sector handles parity | WEAKENED (via CCM1) | 6/10 |
| AE4 | AE suffices (identity theorem) | WEAKENED at N > 20 (heuristic extension) | 6/10 |

**Group: rigorous at N ≤ 20; heuristic above.** The certification
at N ≤ 20 is a genuine contribution; the Slepian-limit extension
to all N is a plausibility argument, not a theorem.

---

## CL — Clay Compliance (4 checks)

| ID | Check | Status | Conf |
|:---|:------|:-------|:-----|
| CL1 | All non-trivial zeros covered | PASS in principle | 7/10 |
| CL2 | Unconditional (or clearly conditional) | **MIXED** — unconditional in Theorem 1.1, conditional in Sec 13.6 | 5/10 |
| CL3 | Rigorous mathematics throughout | **NOT MET** — 8+ concrete rigor gaps | 4/10 |
| CL4 | Addresses Bombieri's questions | PARTIAL (core engaged, L-functions not) | 6/10 |

**Group: Clay compliance is NOT met.** The proof has multiple
rigor gaps (CL3), the theorem statement is over-stated relative
to what is actually proved (CL2), and it does not qualify as a
"published in a qualifying outlet" result (Clay rules §6).

---

## Aggregate

**Total checks:** 30.

**By status:**
- PASS or PASS in principle: 10
- PASS on CCM authority (conditional on preprint): 4
- CONDITIONAL (technical gaps, fixable): 5
- WEAKENED (significant but fixable issues): 8
- BROKEN or NOT MET: 3 (ES3 at λ > e^π, BG2 KLMN, CL3 rigor)

**Overall grade:** see summary.md for the closing verdict.

**The three most critical specific issues:**

1. **Section 10.4 Step 4 is tautological as written.** The correct
   argument (Hurwitz in the complex plane applied to the real-zero
   property of ξ̂_N) is implicit but never explicit. Without a
   rewrite, the proof does not actually prove RH.

2. **Theorem 7.1 proof step (7.5) only holds for λ ≤ e^π ≈
   23.14.** The paper uses λ = √14 in numerics, so the bound
   holds at that value. But the theorem is stated "uniform in N"
   with no restriction on λ. This is a concrete technical gap.

3. **KLMN closability (Corollary 9.6) uses the incorrect
   implication "lower-bounded ⇒ closable".** This is false in
   general (Reed–Simon II Example X.3.1 is a counterexample).
   The fix is to cite the correct result from Reed–Simon II
   Chapter X.

These three are supplemented by the CCM preprint dependence
(Layer 1 rests on unrefereed Connes-Consani-Moscovici 2025) and
several internal-research-note dependencies (research/20, 24,
35, 40, 42) that are not included in the preprint.
