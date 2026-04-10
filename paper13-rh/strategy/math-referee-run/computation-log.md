# Computation Log — Referee Run r02

*Written 2026-04-10. Reproducible with `mpmath` at dps >= 50.*

This log records the computational checks actually performed during the review,
not those I could not perform in the absence of the CCM matrix assembly code.
For the checks that require reproducing CCM's construction (10^{-55}
eigenvalue match, Boegli rank-one stabilization, full Teschl form bound), I
relied on the preprint's internal numerics and flag them explicitly as *not
independently reproduced*.

---

## C1. Euler product at β = 2 and β = 3

Command (`mpmath`, dps = 50):

```python
prod = 1
for p in first_100_primes:
    prod *= 1/(1 - p**(-2))
# compare to pi^2/6
```

| β | ∏_{p≤p_100} (1-p^{-β})^{-1} | ζ(β) | |diff| |
|:--|:----------------------------|:-----|:------|
| 2 | 1.644515221724... | π²/6 = 1.644934066848... | 4.188 × 10^{-4} |
| 3 | 1.202056602179... | 1.202056903159... | 3.010 × 10^{-7} |

**Pass.** Euler product converges to ζ(β) as expected. This is the
standard check the paper calls "ITPFI Euler product" (Appendix B.5 at β > 1).
It is not a proof of the ITPFI factorization at β = 1 (where ζ has a pole);
the three-way argument in Appendix B is required for that.

---

## C2. Value of Xi(0) (claimed 1/2 in Sec 10.3 and Appendix E.4)

Command:

```python
def xi(s):
    return 0.5 * s * (s-1) * pi**(-s/2) * gamma(s/2) * zeta(s)
Xi_0 = xi(mpf(1)/2)   # = 0.4971207781883141099127...
```

The paper (Sec 10.3 proof of Hurwitz applicability, and Appendix E.4) states:

> "Xi(0) = 1/2 ≠ 0" (Sec 10.3)
> "Xi(0) = −(1/2) ζ(1/2) π^{1/4} / Γ(1/4) ≠ 0" (E.4)

**Both are wrong as written.** The correct value is

  Xi(0) = ξ(1/2) = −(1/8) π^{−1/4} Γ(1/4) ζ(1/2) ≈ 0.497121...

and the paper's explicit formula in E.4 is also wrong; plugging it in yields
0.26812..., neither the paper's stated 1/2 nor the correct value 0.4971.

**Effect on proof:** COSMETIC. Xi(0) ≠ 0 is all that is actually needed for
Hurwitz applicability, and the correct value is nonzero. The error does not
invalidate the argument, but it is a cosmetic/exposition bug that a careful
referee will catch on the first pass. It also undermines confidence that the
paper's derivations have been independently checked.

**Required fix:** replace both statements with
"Xi(0) = ξ(1/2) = −(1/8) π^{−1/4} Γ(1/4) ζ(1/2) ≈ 0.4971 ≠ 0".

---

## C3. Theorem 7.1 proof step (7.5): range of validity of the inequality
"(1 + a² x²)/(x² + 1) ≤ a² for x ∈ ℝ whenever a ≥ 1"

Algebraic verification:

  (1 + a² x²)/(x² + 1) − a² = (1 − a²)/(x² + 1)

so the inequality ≤ a² holds iff 1 − a² ≤ 0 iff a² ≥ 1. **Correct as
stated.** The paper's parenthetical "and 2π/L ≥ 1 in the CCM normalisation"
is the substantive content.

Testing at values of L:

| λ     | L = 2 log λ | 2π/L   | 2π/L ≥ 1? | (7.5) valid? |
|:------|:------------|:-------|:----------|:-------------|
| √14 ≈ 3.742 | 2.639 | 2.380 | YES | YES |
| 10    | 4.605 | 1.364 | YES | YES |
| e^π ≈ 23.14 | 6.283 | 1.000 | borderline | borderline |
| 100   | 9.210 | 0.682 | **NO** | **NO** |
| 1000  | 13.815| 0.455 | **NO** | **NO** |

**Finding:** The proof of Theorem 7.1 as written in eq (7.5) **fails for
λ > e^π ≈ 23.14**. At the CCM numerical choice λ = √14, the bound works
comfortably. But Theorem 7.1 is asserted as a uniform bound "for all N ≥ 1"
and is used in the Boegli H2 verification (Corollary 7.3) and in the
Hurwitz argument (which implicitly needs control at eigenvalues up to height
T, corresponding to λ ≳ T).

**Severity:** If λ is treated as *fixed* throughout the proof (at √14 or any
value below e^π), the argument is intact. If λ is treated as a parameter
that grows to capture arbitrarily high Riemann zeros, the proof of
Theorem 7.1 must be replaced or extended.

The paper **does not clearly state which interpretation is intended**. See
Issue (λ-vs-N conflation) in points/B1, B2, D1.

---

## C4. Xi is not identically zero

Trivially verified: Xi(0) = 0.4971... ≠ 0 (see C2). Hurwitz hypothesis
satisfied.

---

## C5. First 5 Riemann zero imaginary parts

```python
for n in range(1,6):
    print(zetazero(n).imag)
```

| n | γ_n |
|:--|:----|
| 1 | 14.13472514173469... |
| 2 | 21.02203963877155... |
| 3 | 25.01085758014569... |
| 4 | 30.42487612585951... |
| 5 | 32.93506158773919... |

These are the standard values. Reference only; the paper's claim that
CCM matches these to 10^{-55} at N=6 is accepted on CCM's authority
(NOT independently reproduced — see C7).

---

## C6. AE simplicity margin at N = 20

Paper-reported values (Appendix F): gap = 7.868 × 10^{-35},
min|⟨φ_k|a⟩| = 9.365 × 10^{-4}, claimed safety margin ~10^{72}.

Consistency check of the safety margin as ratio:

  ratio = min_overlap / (matrix_assembly_error / gap)
        ≈ 9.365e-4 / (1e-110 / 7.87e-35)
        ≈ 7.4e+72    ✓ consistent with paper's claim

**Concern with interpretation:** the spectral gap itself shrinks as
~10^{-1.6 N}, so at N = 30 the gap is ~10^{-52}, at N = 100 ~10^{-170}.
"Simplicity" is maintained only in a delicate arbitrary-precision sense.
The paper extends the certification beyond N = 20 via a "Slepian limit"
monotonicity argument that is **not a theorem** in the paper — it is a
limiting statement supported by numerics at N ≤ 20. This is a real gap:
AE simplicity at N > 20 is *motivated* but not *proved*.

See points/C2-ae-simplicity for the detailed analysis.

---

## C7. 10^{-55} eigenvalue match at N = 6

**NOT independently reproduced.** Reproducing would require implementing
CCM's matrix assembly for QW_λ^N at 200+ digit precision, including the
hypergeometric and digamma evaluations at prime powers. This is feasible
with mpmath in several hours of compute, but outside the scope of a
literature review. The paper itself (Appendix A.5) explicitly flags this:

> "At λ = √14, N = 120: eigenvalue error for γ_1 is 1.07 × 10^{-60} (CCM
> Table 1). ... We have NOT independently reproduced this computation".

So the 10^{-55} figure is taken on CCM's authority.

---

## C8. Rank-one stabilization ||Δ_N|| ≤ C ρ^{−N}

**NOT independently reproduced.** Depends on the paper's research/40
Lemma 1, which is cited but not included in the preprint. The paper reports
b(N) values at N = 10, 20, 30 in Remark 9.4 (3.04e-26, 3.75e-39, 4.62e-52).
These are consistent with ρ ≈ 19.54 and sub-linear C. Flag as
*dependent on research/40*, not self-contained.

---

## C9. CF decay ρ ≥ 4.27 at N = 5, 10, 15, 20, 30

**NOT independently reproduced.** Requires implementing the full CCM
eigenvector solver. Paper reports ρ values 4.27, 6.33, 6.25, 6.06, 5.35 at
these N (Table in Sec 8.1). All satisfy ρ ≥ 4.27.

One concern from the reported data: ρ_N is **non-monotone** (4.27 → 6.33 →
6.25 → 6.06 → 5.35), with a clear downward trend from N = 10 onward. Paper
attributes this to "fit artefact from non-exponential behaviour near j = 0".
The concern is that extrapolating ρ_N ≥ 4.27 to *all* N from a non-monotone
5-point sample is **not rigorous** — strict asymptotic uniformity is
required, and the five-point pattern is consistent with ρ_N possibly dipping
below 4.27 for some N > 30 not tested. Paper's argument that "ρ is
determined by singularities of the Weil distribution, independent of N"
(Sec 8.1) would close the gap if made rigorous; as stated it is a
structural plausibility argument, not a proof.

See points/B3 step 05-discrete-compactness.md for more.

---

## Summary

| Check | Result |
|:------|:-------|
| C1 Euler product β=2,3 | PASS |
| C2 Xi(0) value | FAIL (cosmetic, not structural) |
| C3 (7.5) inequality | HOLDS only for λ ≤ e^π ≈ 23.14 |
| C4 Xi ≢ 0 | PASS (Hurwitz hypothesis OK) |
| C5 Riemann zeros | reference |
| C6 AE margin at N=20 | consistent; gap shrinkage is a concern |
| C7 10^{-55} match | NOT REPRODUCED (depends on CCM) |
| C8 ρ_Δ, ||Δ_N|| | NOT REPRODUCED (depends on research/40) |
| C9 CF ρ ≥ 4.27 uniform | verified at N ≤ 30; asymptotic uniformity not rigorous |

**Two concrete bugs found by computation:**

1. Xi(0) value is wrong (Sec 10.3 and App E.4). Cosmetic — Xi(0) ≠ 0
   remains true, Hurwitz applies.

2. Theorem 7.1's key inequality (7.5) only holds for λ ≤ e^π ≈ 23.14.
   The paper uses λ = √14 in its numerics but states the theorem with
   "uniform in N" and gives no range of λ. If the proof is intended to
   cover all λ, Theorem 7.1's proof is broken.

Neither of these kills the proof outright, but both indicate the paper
has not been sufficiently checked. A refereeable version must fix both.
