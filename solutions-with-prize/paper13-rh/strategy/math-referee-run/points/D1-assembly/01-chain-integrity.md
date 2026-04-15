# D1.01 — Chain Integrity

## Walking the chain

| Step | Layer | What is needed | Status (from A1-C2) |
|:-----|:------|:---------------|:--------------------|
| D_N self-adjoint, real spectrum | 1 | CCM Thm 4.2 | PASS (on CCM authority) |
| D_N on E_N^+ (even-sector) | 1 | CCM + even-sector modification | WEAKENED (A1.01) |
| Zeros of ξ̂_N = spec(D_N) | 1 | CCM Thm 5.10(iii) | PASS (on CCM authority) |
| ξ̂_N has only real zeros in ℂ | 1/5 | implicit from above | IMPLICIT, not stated |
| ITPFI factorization of ω_1 | 2 | Laca-Raeburn + BR + BC | PASS |
| ω_1^{≤P_N} → ω_1 weak-* | 2 | direct from ITPFI | PASS |
| Entry-by-entry Q_N stabilization | 2 | direct from ITPFI | PASS |
| Archimedean O(1/λ) | 3 | Proposition 5.1 | WEAKENED (B1) |
| Eigenvector O(1/λ) via ITPFI triangle | 3 | Theorem 6.4 | WEAKENED (B2) |
| Uniform H¹ bound ≤ 2π/L | 3 | Theorem 7.1 | PASS at λ ≤ e^π; BROKEN above |
| CF decay ρ ≥ 4.27 uniform in N | 3 | Proposition 8.1 | VERIFIED at N ≤ 30; asymptotic uniformity NOT rigorous |
| Teschl form bound a = 0 | 4 | Theorem 9.3 | CONDITIONAL |
| KLMN closability of Q_∞ | 4 | Corollary 9.6 | WEAKENED (B3.04) |
| gsrc = Bögli H1 | 4 | Corollary 9.5 | CONDITIONAL (Teschl applicability) |
| Discrete compactness = Bögli H2 | 4 | Corollary 9.8 | PASS (at fixed λ) |
| Bögli exactness: spec(D_∞) = lim spec(D_N) | 4 | Theorem 9.9 | CONDITIONAL |
| ξ̂_N → Ξ uniformly on compacts | 5 | Theorem 10.1 | CONDITIONAL (λ vs N) |
| Hurwitz gives zero convergence | 5 | Theorem 10.2 | PASS in principle |
| spec(D_∞) = {γ_n} | 5/6 | Theorem 10.3 Step 1-2 | CONDITIONAL |
| D_∞ self-adjoint → spec ⊂ ℝ | 6 | standard | PASS if D_∞ exists |
| **"γ_n ∈ ℝ hence RH"** (as written) | 6 | Section 10.4 Step 4 | **TAUTOLOGICAL** |
| Hurwitz-in-complex-plane + real-zero property (correct) | 6 | reconstructed | WORKS but NOT EXPLICIT |

## The weakest links (in order)

1. **The final exposition (Section 10.4 Step 4)** is
   tautological as written. The correct argument (Hurwitz in ℂ +
   real-zero property of ξ̂_N) is not explicit. This is a
   **fixable exposition issue** but a serious one.

2. **Theorem 7.1 proof** only valid for λ ≤ e^π ≈ 23.14. At
   the paper's fixed λ = √14 this holds; any "uniform in λ"
   reading breaks. Paper does not clarify the intended regime.

3. **KLMN closability** of Q_∞ is argued via an incorrect
   implication (positivity ⇒ closability). Fixable with correct
   citations.

4. **AE simplicity for N > 20** is not rigorously established.
   The Slepian-limit argument is heuristic. Fixable with a
   dedicated convergence theorem.

5. **Eigenvector approximation Theorem 6.4** has:
   - a divergent PNT-tail estimate (Σ log p / √p) as written,
   - a gap lower bound gap(T_0) ≥ C''·λ that is not proved,
   - an unproven "ξ_0 → E(h)" claim.

6. **The λ vs N conflation** throughout Sections 5–10 masks
   whether the convergence rate is in λ, in N, or in a joint
   coupling.

7. **External dependence on CCM preprint** — unverifiable until
   refereed.

8. **External dependence on research/40 Lemma 1** — not in the
   preprint at all.

## Is every link rigorous?

No. Several links (7.1 proof, KLMN closability, Slepian limit,
the final exposition) are not rigorous. Several others
(archimedean, eigenvector approximation) rely on internal
research notes not included in the preprint.

## Does the chain hold modulo these issues?

If all the flagged items are fixed (which is plausible, since
none is definitively fatal), the chain would hold **conditional
on CCM being correct**. That is the 8/10 self-assessment the
paper makes.

## Verdict on this subpoint

The chain's structure is sound. Individual links have rigor
gaps of varying severity. The weakest are in Layer 4 (Teschl-
Bögli synthesis) and in the final deduction (Section 10.4).
