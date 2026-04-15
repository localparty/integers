# Strategy 21 — Boegli's Discrete Compactness: The Last Condition

*Boegli's spectral exactness theorem applies to CCM. One condition*
*remains: discrete compactness of the resolvent sequence. This*
*reduces to CF-controlled Sobolev regularity. Rated 7/10.*

*Date: 2026-04-10*

---

## 1. The single remaining condition

> **Discrete compactness:** Every bounded sequence
> {(D_N − z)⁻¹ f_N} with f_N ∈ H_N, ‖f_N‖ ≤ 1 has a
> convergent subsequence in the limit space.

This is equivalent to: the resolvent images have UNIFORM
Sobolev regularity (eigenvector Fourier coefficients decay
fast enough, uniformly in N).

## 2. Why CF gives Sobolev regularity

The Carathéodory-Fejér mechanism in CCM's construction provides
EXPONENTIAL decay of eigenvector Fourier coefficients. CF
optimization is the reason CCM get 10⁻⁵⁵ precision with 6 primes.

Exponential decay of Fourier coefficients = ANALYTIC regularity
(stronger than any Sobolev regularity). If the CF decay rate is
UNIFORM in N → discrete compactness follows.

## 3. The proof chain

1. ITPFI: ω₁^{≤P} → ω₁ in weak-* (PROVED)
2. Weil form QW^{N,+} entries converge (follows from ITPFI)
3. Generalized strong resolvent convergence (H1): PLAUSIBLE
   (ITPFI + self-adjointness → automatic resolvent bounds)
4. CF exponential decay of Fourier coefficients: STRUCTURAL
   (from CCM's Carathéodory-Fejér construction)
5. CF decay UNIFORM in N: NEEDS VERIFICATION
6. Uniform CF → discrete compactness (H2): FOLLOWS
7. H1 + H2 → Boegli spectral exactness → spec(D_∞) = lim spec(D_N)
8. CCM numerics + Lemma 7.3: lim spec(D_N) = {γ_n}
9. **RH**

## 4. The verification needed

> **Is the CF decay rate uniform in N?**
>
> At each N, CF gives exponential decay of eigenvector Fourier
> coefficients: |ξ̂_N(k)| ≤ C_N · ρ_N^{-k} for some C_N, ρ_N > 1.
>
> Uniform: C_N ≤ C and ρ_N ≥ ρ > 1 for all N.
>
> If uniform → discrete compactness → Boegli → RH.
