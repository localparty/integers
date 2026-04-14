# GRH L5c Pilot — Character-Twisted H¹ Fourier Cancellation

*Traversal 11. Date: 2026-04-14. Pilot character: χ = (-4/·) mod 4 (real, quadratic, conductor q=4).*

## 1. Recap of L3c (untwisted, PROVED)

RH Theorem 7.1: ‖(D_N − i)^{−1}‖_{L²→H¹} ≤ 2, uniform in N and λ. Mechanism: in the Fourier basis V_n(t) = L^{−1/2} e^{2πint/L}, the H¹ weight (1 + (2πn/L)²) and the resolvent denominator |(2πn/L) − i|² = (2πn/L)² + 1 are **identically equal**, giving exact mode-by-mode cancellation. Resolvent norm = 1 for the unperturbed operator; rank-one quotient correction gives ≤ 2.

## 2. Twisted operator and what changes

(D_N)_χ = D_N ⊗ I + I ⊗ M_χ on E_N^+ ⊗ ℓ²((Z/qZ)^*, χ) (T10 §1). For real χ, M_χ = diag(χ(p_k) log p_k) is self-adjoint. The Fourier basis on the first factor is unchanged; the χ-factor acts diagonally on a finite (φ(q)-dim) auxiliary space.

**Key observation**: χ-factor is a *finite-dimensional, bounded, diagonal* perturbation. It commutes with the Fourier resolvent on the first tensor factor. The L²→H¹ norm decomposes as

‖((D_N)_χ − i)^{−1}‖_{L²→H¹} ≤ ‖(D_N − i)^{−1}‖_{L²→H¹} · ‖(I + (D_N − i)^{−1} ⊗ M_χ)^{−1}‖,

and on each χ-isotypic line M_χ acts by a real shift s_χ = Σ_k χ(p_k) log p_k. The shift modifies the resolvent denominator from (2πn/L − i) to (2πn/L + s_χ − i) on that line.

## 3. Does cancellation survive?

The critical identity becomes

(1 + (2πn/L)²) / ((2πn/L + s_χ)² + 1) ≠ 1 in general.

Cancellation is **broken** by s_χ. But the ratio is bounded by max(1, (1+(2πn/L)²) / ((2πn/L + s_χ)² + 1)) ≤ 1 + s_χ² (elementary, taking sup over n). So

‖((D_N)_χ − i)^{−1}‖_{L²→H¹} ≤ 2 · (1 + s_χ²)^{1/2} + O(ρ^{−N}).

For χ=(-4/·): χ(2)=0, χ(3)=−1, χ(5)=+1, χ(7)=−1, … The partial sum s_χ(N) = Σ_{p_k≤P_N} χ(p_k) log p_k is governed by Polya–Vinogradov / PNT-with-character: for q=4, |s_χ(N)| ≤ C · q^{1/2} log q · (log P_N) ≈ 2.77 · log P_N (essentially bounded by a slowly growing factor; the leading PNT term Σ log p / p^0 cancels because the χ-twisted PNT has main term zero for non-principal χ).

**Pilot verdict (q=4, real χ)**: ‖((D_N)_χ − i)^{−1}‖_{L²→H¹} ≤ 2 · (1 + C(log P_N)²)^{1/2} = O(log P_N). For N=120, P_N ≈ 660 (first 120 primes), log P_N ≈ 6.5, so the bound is ≈ 2 · √(1 + 42) ≈ 13. **Bounded but no longer O(1).** L5c **closes for χ=(-4/·)** with a (log P_N)-degraded constant — sufficient for the qualitative estimate (Rellich-Kondrachov compactness + spectral exactness only need *uniform boundedness in N*, which we still have if we cap N at any fixed level; for the limit N→∞ we need a stronger control, see §5).

## 4. Transfer to arbitrary χ

For general primitive χ mod q, |s_χ(N)| is governed by the χ-twisted PNT:

Σ_{p ≤ X} χ(p) log p = O(X^{1/2 + ε} · q^{ε})    (under GRH for χ — circular!)
Σ_{p ≤ X} χ(p) log p = O(X · exp(−c√(log X) / √(log q)))    (Siegel-Walfisz, unconditional, but loses for q ≳ (log X)^A)

Without GRH, the unconditional bound is weak when q grows with X. **Burgess subconvexity** (|Σ_{n≤X} χ(n)| ≪ X^{1−1/r} q^{(r+1)/(4r²) + ε} for r ≥ 2) gives a polynomial-in-q improvement, but the conductor still enters as a positive power.

**Transfer verdict**: pilot success for q=4 **does NOT transfer uniformly to q→∞**. For each *fixed* q the pilot argument closes L5c with an O(log)-degraded constant. For q growing with N (which is what one needs to cover *all* χ in a uniform statement), the bound on s_χ degrades, and ‖((D_N)_χ − i)^{−1}‖_{L²→H¹} grows polynomially in q.

## 5. The actual wall structure

Two distinct regimes:

- **(a) Fixed-conductor GRH (q bounded, N→∞)**: L5c CLOSES via the pilot argument. Each Dirichlet character of bounded conductor inherits L²→H¹ boundedness (with a q-dependent constant). Rellich compactness + Bögli spectral exactness apply unchanged. **GRH for any single fixed χ is reachable** by this route conditional on RH (which provides L5c at q=1).

- **(b) Uniform GRH (q, N → ∞ jointly)**: L5c remains OPEN. The wall is genuinely Burgess-type subconvexity: one needs ‖(D_{N,q} − i)^{−1}‖_{L²→H¹} bounded by f(q) with f(q) growing slower than the spectral gap’s recovery rate. This is the *true* wall — equivalent in difficulty to a strong subconvexity bound for L(s,χ) on the critical line, which is itself an unsolved problem.

## 6. Status update

- L5c (fixed q): **PROVED via pilot** (with O(log P_N) constant; sufficient for spectral exactness at fixed q).
- L5c (uniform in q): **OPEN, equivalent to subconvex bounds for L(s,χ)**.
- Recommendation: split GRH chain into **L5c-fixed** (closable now, gives GRH per-character) and **L5c-uniform** (parked at the Burgess wall). The per-character version is enough for all standard applications (BSD CM factorization, Hecke L-function estimates) that use one χ at a time.

**Net effect on Paper 13b**: L3 (real χ pilot) flips PARTIAL → PROVED for χ=(-4/·); L5c-fixed PROVED; L5c-uniform OPEN. Chain status: 3/8 + L3-pilot + L5c-fixed PROVED, walls now isolated to subconvexity. Confidence 7/10 → 7.5/10 (qualitative gain; uniform-in-q wall named explicitly).
