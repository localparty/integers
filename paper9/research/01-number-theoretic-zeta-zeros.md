# Research Memo 01 — Number-Theoretic Route: Trivial Zeros of ζ_R and the Goroff-Sagnotti Epstein Vanishing

**Route:** 01 — Number-theoretic / trivial zeros of the Riemann zeta function  
**Investigator:** Claude Sonnet 4.6 (QG5D Paper 9 agent)  
**Date:** 2026-04-07  
**Code:** `/Users/gsix/quantum-geometry-in-5d-latex/code/zeta-zeros/compute.py`  
**Results:** `/Users/gsix/quantum-geometry-in-5d-latex/code/zeta-zeros/results.txt`

---

## Summary

Paper 1 establishes that the Goroff-Sagnotti R³ counterterm vanishes in 5D KK gravity on M⁴ × S¹ via zeta regularization of the KK mode sums, with scheme-independence left as an open question. This memo asks whether that vanishing corresponds to a trivial zero of ζ_R — a number-theoretic identity independent of regularization. The answer is nuanced: **no for the leading S₀ cancellation, but yes in mechanism for the subleading Epstein zeros.** The subleading KK sums land at the Epstein zeta function evaluated at negative integers, and these zeros arise from the same pole structure of 1/Γ(s) that produces the trivial zeros of ζ_R — making them mathematically robust. However, the leading cancellation S₀ = 1 + 2ζ_R(0) = 0 uses ζ_R(0) = −1/2, which is a regularization-dependent special value rather than a trivial zero, and represents a genuine scheme-dependence gap. The route is **Promising but Partial**: the subleading zeros are defensibly scheme-independent; the leading cancellation requires a separate argument.

---

## Setup: What Paper 1 Establishes

Paper 1 (Appendices F, G, K, U) proves perturbative UV finiteness of 5D linearized gravity on M⁴ × S¹ using spectral zeta regularization of the KK mode sums. The key results:

**One loop (Appendix F):**  
The leading divergence cancels via

    S₀ = 1 + 2ζ_R(0) = 1 + 2(−1/2) = 0

The "1" is the zero-mode contribution; "2ζ_R(0) = −1" is the analytic continuation of the oscillating KK tower.

**Two loops (Appendix G and U):**  
The leading KK sum factor is S₀² = 0² = 0. The subleading terms reduce to 2D Epstein zeta functions E₂(s; Q) evaluated at negative integers:

    C_GS ∝ Σ_{n,m∈Z} [d₀ + d₂(n² + m² + (n+m)²)/R² + ...]

where d₀ × S₀² = 0 kills the leading term, and the subleading term involves E₂(−1; Q₂) with Q₂(n,m) = 2n² + 2nm + 2m².

**All loops — Theorem K.1 (Universal Epstein Vanishing):**  
For any positive-definite quadratic form Q in L variables:

    E_L(−j; Q) = 0   for all integers j ≥ 1

**Proof.** The completed Epstein zeta function is Λ(s) = π^{−s} Γ(s) E_L(s; Q), which is meromorphic with poles only at s = 0 and s = L/2. At s = −j (j ≥ 1), Λ(−j) is therefore finite. Inverting:

    E_L(s; Q) = π^s Λ(s) / Γ(s)

Since 1/Γ(−j) = 0 for all j ≥ 1 (Γ has poles at all non-positive integers), we get E_L(−j; Q) = 0. ∎

**Open question (Appendix U.2c):** Whether the vanishing under zeta regularization is scheme-independent is explicitly left unresolved. Paper 1 claims vanishing within zeta regularization, not physical scheme-independence.

---

## Main Argument: The Functional Equation Route

### Step 1: Determine s₀

The question asks: at what argument s₀ is the Epstein/Riemann zeta evaluated in the Goroff-Sagnotti diagram?

**Power-counting in 5D KK gravity:**

- 5D graviton propagator: ~1/(k² + n²/R²)
- Three-graviton vertex: ~p² (two derivatives from Einstein-Hilbert action)
- 4D loop measure per loop: d⁴k
- KK mode sum per loop: Σ_n (over Z)

At two loops, the sunset diagram has three internal graviton propagators carrying KK numbers (n, m, −(n+m)) and two independent 4D loop momenta. After performing the 4D momentum integrals in the UV, the integrand has the mass expansion:

    I_sunset(n, m) = (1/ε) × [d₀ + d₂(n² + m² + (n+m)²)/R² + O(n⁴/R⁴)]

The leading term d₀ is mass-independent (equals the 4D Goroff-Sagnotti integrand with all KK masses set to zero). The subleading term involves (n² + m² + (n+m)²)/R², which after KK summation gives:

    Σ_{n,m} (n² + m² + (n+m)²)/R² = (1/R²) × E₂(−1; Q₂)

where Q₂(n,m) = 2n² + 2nm + 2m².

**Therefore: s₀ = −1.**

The Epstein zeta is evaluated at **s₀ = −1**, which is a negative *odd* integer — not a trivial zero of ζ_R.

### Step 2: Is s₀ a trivial zero of ζ_R?

No. The trivial zeros of ζ_R are at the negative *even* integers: ζ_R(−2), ζ_R(−4), ζ_R(−6), .... They arise from the sin(πs/2) = 0 factor in the functional equation

    ζ_R(s) = 2^s π^{s−1} sin(πs/2) Γ(1−s) ζ_R(1−s)

At s = −2k: sin(π·(−2k)/2) = sin(−kπ) = 0.

At s = −1 (the relevant value for the subleading GS sum), sin(π·(−1)/2) = sin(−π/2) = −1 ≠ 0. So **s₀ = −1 is not a trivial zero of ζ_R**.

### Step 3: What kind of zero is it?

The Epstein zero at s₀ = −1 is a **universal structural zero** of the Epstein zeta function, arising from a different mechanism than the ζ_R trivial zeros:

| Type | Location | Mechanism |
|------|----------|-----------|
| ζ_R trivial zeros | s = −2, −4, −6, ... (even only) | sin(πs/2) = 0 in functional equation |
| Epstein universal zeros | s = −1, −2, −3, ... (all negative integers) | 1/Γ(s) = 0 at non-positive integers |

The Epstein zeros are **strictly stronger**: they include all negative integers, not just even ones. The mechanism is the 1/Γ(s) factor.

### Step 4: Scheme independence of the Epstein zeros

**Claim:** E_L(−j; Q) = 0 for j ≥ 1 is **scheme-independent** by the same logic that makes ζ_R(−2k) = 0 scheme-independent.

The argument is:

1. Any regularization of the KK mode sum Σ_{n∈Z^L} [Q(n)]^{−s} that represents it as a meromorphic function of s with a single pole at s = L/2 will have the completed form E_L(s; Q) = π^s Λ(s)/Γ(s).

2. The identity 1/Γ(−j) = 0 is a mathematical fact about the Gamma function, independent of any regularization choice.

3. Therefore, any regularization that produces a function analytic enough to write E_L(s; Q) in the completed form will yield E_L(−j; Q) = 0.

This is analogous to the scheme-independence of ζ_R trivial zeros: the sin(πs/2) = 0 factor in the functional equation is a number-theoretic identity; any scheme consistent with the functional equation of ζ_R must reproduce the trivial zeros.

**The distinction from the leading S₀ cancellation:** The S₀ = 0 cancellation uses ζ_R(0) = −1/2, which is *not* a zero — it is a finite special value whose sign and magnitude are specific to analytic continuation. In dimensional regularization, the same sum Σ_n 1 is set to zero by a different convention (dim-reg kills scaleless integrals). Both schemes give S₀ = 0, but by different routes, and the match is not guaranteed by any overarching mathematical identity. This is where genuine scheme-dependence lurks.

### Step 5: Summary diagram

```
Goroff-Sagnotti KK sum structure:
   C_GS ~ Σ_{n,m} f(n,m)

Leading term f(n,m) = d₀ (constant):
   Σ_{n,m} d₀ = d₀ × S₀²
   S₀ = 1 + 2ζ_R(0) = 0           [uses ζ_R(0) = -1/2, scheme-sensitive]
   -> C_GS_leading = 0

First subleading f(n,m) ~ (n² + m² + (n+m)²)/R²:
   Σ_{n,m} (...)  = E₂(−1; Q₂)
   E₂(−1; Q₂) = 0                  [uses 1/Γ(−1) = 0, number-theoretic]
   -> C_GS_subleading = 0

All higher subleading terms:
   E₂(−2; Q₂) = E₂(−3; Q₂) = ... = 0    [same mechanism]
   -> C_GS_all_subleading = 0
```

---

## Numerical Results

All computations performed with `mpmath` at 50 decimal places of precision. See full output at `/Users/gsix/quantum-geometry-in-5d-latex/code/zeta-zeros/results.txt`.

### Trivial zeros confirmed

```
       s           zeta_R(s)       |zeta_R(s)|    Is zero?
  ------   ----------------   ----------------   ----------
      -2                0.0                0.0          YES
      -4                0.0                0.0          YES
      -6                0.0                0.0          YES
      -8                0.0                0.0          YES
```

### Functional equation verified (relative error ~ 10⁻⁵¹)

```
         s      direct zeta(s)       via func. eq.     rel. diff
  --------   ----------------   ----------------   -----------
      -0.5   -0.20788622498    -0.20788622498       1.61e-51
       0.5   -1.46035450881    -1.46035450881       1.83e-51
      -1.5   -0.02548520189    -0.02548520189       4.92e-51
      -3.0    0.00833333333     0.00833333333       2.51e-51
      -5.0   -0.00396825397    -0.00396825397       0.0
```

### S₀ cancellation

```
  zeta_R(0) = -0.5  (exact, by Bernoulli formula: -B₁/1 = 1/2... 
                      mpmath convention gives -1/2)
  S₀ = 1 + 2 × (-0.5) = 0.0  (exact)
```

### Special values — Bernoulli formula confirmation

```
  zeta_R(  0): formula = -0.50000000, mpmath = -0.50000000, match=True
  zeta_R( -1): formula = -0.08333333, mpmath = -0.08333333, match=True
  zeta_R( -2): formula =  0.00000000, mpmath =  0.00000000, match=True
  zeta_R( -3): formula =  0.00833333, mpmath =  0.00833333, match=True
  zeta_R( -4): formula =  0.00000000, mpmath =  0.00000000, match=True
  zeta_R( -5): formula = -0.00396825, mpmath = -0.00396825, match=True
```

The trivial zeros ζ_R(−2k) = 0 correspond to B_{2k+1} = 0 for k ≥ 1: Bernoulli numbers with odd index ≥ 3 all vanish. This is the underlying number-theoretic fact.

### 1/Γ vanishing mechanism

```
  j=1: zeta_R(-1) = -0.083333333,  1/Gamma(-1) = 0.0
  j=2: zeta_R(-2) = 0.0,           1/Gamma(-2) = 0.0
  j=3: zeta_R(-3) =  0.0083333333, 1/Gamma(-3) = 0.0
  j=4: zeta_R(-4) = 0.0,           1/Gamma(-4) = 0.0
```

Note: ζ_R(−1) ≠ 0 but 1/Γ(−1) = 0. For the full Epstein zeta E_L(s; Q) = π^s Λ(s)/Γ(s), the factor 1/Γ(−1) = 0 forces E_L(−1; Q) = 0 for any L and any positive-definite Q. The same factor forces ζ_R(−2) = 0 because Λ(−2) is finite.

### Z₂ parity structure on S¹/Z₂

```
  zeta_R(0)      = -0.5   (exact)
  S₀ (full S¹)   =  0.0   [= 1 + 2*(-0.5)]
  S₀^even        =  0.5   [= 1 + 1*(-0.5), zero mode + positive KK modes]
  S₀^odd         = -0.5   [= 0 + 1*(-0.5), positive KK modes only]
  S₀^even + S₀^odd = 0.0  (they cancel)
```

This reveals a potential orbifold subtlety: if only Z₂-even internal loop modes contribute to a given diagram, S₀^even = 1/2 ≠ 0. The full S₀ = 0 requires summing over both Z₂-even and Z₂-odd internal modes, which is correct for the full KK loop integral but must be verified for each diagram topology on S¹/Z₂.

### Epstein zeta at s = 2 (convergent region, cross-check)

```
  E₂(2; Q₂) with Q₂(n,m) = 2n² + 2nm + 2m², direct sum (200 terms) = 1.92776310187537
```

This confirms the Epstein function is non-trivial (not identically zero) in the convergent region; the zeros at negative integers are non-trivial consequences of the analytic continuation.

---

## Gaps and Obstacles

### Gap 1 (Inherited from Paper 1): Factorization at L ≥ 3

Even accepting that E_L(−j; Q) = 0, this vanishing only kills the Goroff-Sagnotti counterterm if the full L-loop amplitude factorizes as (4D integral) × E_L(−j; Q_L). This factorization is verified explicitly at L = 1 and L = 2 but remains a conditional theorem at L ≥ 3 (Theorem K.3 in Appendix K). The Mercedes three-loop topology with overlapping subdivergences is the specific gap.

### Gap 2 (New — this memo): The leading S₀ cancellation is scheme-sensitive

The subleading Epstein zeros are defensibly scheme-independent (1/Γ argument). But the leading cancellation S₀ = 1 + 2ζ_R(0) = 0 depends on ζ_R(0) = −1/2, which is a regularization-specific value. In dim-reg, scaleless integrals vanish by a different mechanism. The two schemes both give S₀ = 0, but there is no number-theoretic identity ensuring they agree — it requires a separate scheme-comparison argument. Paper 1 identifies this explicitly in Appendix U.2c.

### Gap 3 (New — this memo): Z₂ orbifold vs. full S¹

The S₀ = 0 identity holds for the complete sum over Z (all KK modes on S¹). On S¹/Z₂, internal loop modes still run over both parities (the orbifold constrains external states, not internal loop momenta). However, if diagrams involving only Z₂-even internal modes can be isolated, their contribution is S₀^even = 1/2 ≠ 0. This requires a careful analysis of which parity combinations appear in the internal loops of the Goroff-Sagnotti diagrams on S¹/Z₂ specifically. This issue does not appear to be addressed in Paper 1.

### Gap 4: Does dim-reg reproduce the Epstein vanishing?

The 1/Γ argument shows the Epstein zeros are mathematically robust. But in dimensional regularization, the KK sums are regulated by a different method (analytic continuation in D, not in the KK summation variable s). To confirm scheme-independence, one would need to show that dim-reg KK sums evaluated at the relevant orders also vanish. This is non-trivial because dim-reg acts on the 4D momentum dimension, not the KK index lattice.

---

## Assessment

| Component | Status |
|-----------|--------|
| s₀ determination | Complete: s₀ = −1 for leading subleading GS term |
| Is s₀ a trivial zero of ζ_R? | No — it is a negative odd integer |
| Is the vanishing number-theoretic? | Partially: same 1/Γ mechanism as trivial zeros, but broader class |
| Subleading Epstein zeros — scheme independence | Strongly supported: 1/Γ(−j) = 0 is mathematical identity |
| Leading S₀ cancellation — scheme independence | Open gap (inherited from Paper 1) |
| Orbifold Z₂ parity analysis | Partial: new subtlety identified, needs diagram-level analysis |
| Explicit dim-reg comparison | Not done; open |

**Status: Promising / Partial**

The number-theoretic route provides a genuine strengthening of the scheme-independence argument for the *subleading* Epstein zeros. These zeros arise from the same 1/Γ pole mechanism as the ζ_R trivial zeros — making them defensibly scheme-independent in the sense that any analytic continuation scheme consistent with the gamma function poles must reproduce them. However, this route does not resolve the scheme-independence of the leading S₀ = 0 cancellation, and it reveals a new subtlety about the Z₂ orbifold structure.

---

## Proposed Next Steps

**Highest priority:** Analyze the Z₂ parity of internal loop modes in the Goroff-Sagnotti diagrams on M⁴ × S¹/Z₂ explicitly. Determine whether the full sum (both parities) or only Z₂-even modes run in each diagram topology. This could either confirm S₀ = 0 or reveal a new gap.

**Second priority:** Attempt a dim-reg computation of the leading KK mode sum Σ_n 1 in the 5D KK theory. If dim-reg also gives 0 (e.g., by the argument that scaleless sums vanish), this would close the leading-term scheme-independence gap by a direct comparison rather than by appeal to an abstract equivalence theorem.

**Third priority:** Investigate whether the Epstein functional equation (the multi-dimensional analogue of the ζ_R functional equation) provides a stronger scheme-independence argument — specifically whether it forces E_L(−j; Q) = 0 in any scheme consistent with the functional equation, by the same logic as ζ_R trivial zeros.

---

## Key Code Snippet

```python
# The 1/Gamma mechanism — core of the number-theoretic argument
import mpmath
from mpmath import mp, mpf, zeta, gamma

mp.dps = 50

# Reciprocal gamma (avoids pole exceptions)
for j in [1, 2, 3, 4]:
    s_val = mpf(-j)
    z_val = zeta(s_val)
    one_over_gamma = mpmath.rgamma(s_val)
    print(f"j={j}: zeta_R({-j}) = {z_val},  1/Gamma({-j}) = {one_over_gamma}")

# Output:
#   j=1: zeta_R(-1) = -0.083333333,  1/Gamma(-1) = 0.0
#   j=2: zeta_R(-2) = 0.0,           1/Gamma(-2) = 0.0
#   j=3: zeta_R(-3) =  0.0083333333, 1/Gamma(-3) = 0.0
#   j=4: zeta_R(-4) = 0.0,           1/Gamma(-4) = 0.0
```

Note: `zeta_R(−1) ≠ 0` but `1/Gamma(−1) = 0`. For the Epstein function
`E_L(s; Q) = π^s Λ(s)/Γ(s)`, the factor `1/Γ(−1) = 0` forces `E_L(−1; Q) = 0`
regardless of the form Q or loop order L. This is the number-theoretic
content: the universal Epstein vanishing is a consequence of the gamma
function's poles, not of the specific quadratic form.

---

## References

- Paper 1 Appendix K (§K.7b): Theorem K.1 (Universal Epstein Vanishing), proof via 1/Γ poles
- Paper 1 Appendix U (§U.2c): Scheme-independence problem, explicit statement of the open question
- Epstein, P. "Zur Theorie allgemeiner Zetafunktionen." *Math. Ann.* 56, 615-644 (1903)
- Terras, A. *Harmonic Analysis on Symmetric Spaces and Applications.* Vol. I, Springer (1985)
- Goroff, M. H. & Sagnotti, A. *Nucl. Phys. B* 266, 709-736 (1986)
