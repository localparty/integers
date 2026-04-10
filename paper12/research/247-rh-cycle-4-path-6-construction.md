# 247 -- RH Cycle 4, Path 6 (Distributional Closure) -- Construction

*Cycle: 4. Date: 2026-04-09. Agent: Construction (priority 1+1).*

---

## Step attempted

**Complete the Meyer Frechet-to-Hilbert gap: show that the Meyer spectral inclusion lifts from the nuclear Frechet space to the H^1 Sobolev completion.**

Per cycle 3: Path 6 closed essential self-adjointness conditional on Axiom 1. The remaining gap: construct H_R independently of the spectral realisation conjecture, starting from Meyer's nuclear-space construction.

## Attempt level: 2 (Sub-computation with mpmath)

### The mathematical structure

Meyer (2005) constructs a representation of the idele class group on a nuclear Frechet space S (essentially the Schwartz space S(R) or its adelic analog). The distributional trace of the time evolution on this space reproduces the Weil explicit formula, embedding every Riemann zero into the distributional spectrum.

The gap: S is a nuclear Frechet space, NOT a Hilbert space. The Bost-Connes C*-algebra acts on a Hilbert space H_R (Axiom 1). The question is whether S can be completed to H_R.

### Sobolev regularity computation

The Sobolev H^{-s} norm of the spectral measure is:

    ||mu||_{H^{-s}}^2 = sum_n 1/(1 + gamma_n^2)^s

**mpmath results:**

| s | sum (200 zeros) | Converges? |
|:--|:----------------|:-----------|
| 0.5 | 1.351 | Marginal (tail ~ n^0) |
| 0.6 | 0.544 | Yes |
| 0.7 | 0.228 | Yes |
| 0.8 | 0.099 | Yes |
| 1.0 | 0.021 | Yes (rapidly) |
| 1.5 | 0.00072 | Yes |
| 2.0 | 0.000037 | Yes |

The spectral measure is H^{-s} regular for all s > 1/2. This means the distributional eigenstates lie in H^{-s} for s slightly above 1/2, consistent with the zero density d(T) ~ (1/(2pi))*log(T/(2pi)) (Weyl law gives n ~ T*log(T)/(2pi), so gamma_n ~ 2pi*n/log(n), and 1/gamma_n^{2s} ~ (log n)^{2s}/n^{2s}, which converges for 2s > 1).

### Resolvent pole check

Checked the resolvent R(z) = sum_n 1/(gamma_n - z) at midpoints between all consecutive zeros gamma_n, gamma_{n+1} for n = 1, ..., 19, plus below gamma_1:

**All midpoints: R(z) finite.** No extra poles detected in the first 20 gaps.
**Below gamma_1:** z = 0, 5, 10, 12 all give finite R(z). No pole below gamma_1.

### The Frechet-to-Hilbert completion

**Theorem (nuclear space completion).** A nuclear Frechet space S with a continuous positive-definite sesquilinear form (,) can be completed to a Hilbert space H = completion of S/(ker of (,)). The natural inclusion S -> H is continuous and dense.

**Application to Meyer's construction:**

1. Meyer's space S has a natural inner product coming from the Weil inner product on adele class space: <f, g> = integral_{C_Q} f(x) g-bar(x) d*x, where C_Q = A_Q*/Q* is the idele class group.

2. The Weil inner product is positive-definite on the QUOTIENT S/ker(E), where E is the cutoff operator (Connes 1999). This is the key step: the positivity of the Weil inner product is EQUIVALENT to RH (this is Weil's classical result).

3. **Therefore:** The Frechet-to-Hilbert completion succeeds IF AND ONLY IF the Weil inner product is positive-definite, which is IF AND ONLY IF RH holds.

### Honest negative

**The Meyer Frechet-to-Hilbert gap CANNOT be closed independently of RH.** The completion of Meyer's nuclear space to a Hilbert space requires the positivity of the Weil inner product, which is equivalent to RH. This is a CIRCULAR path: we need RH to construct H_R, and we need H_R to prove RH.

This is not surprising -- it is the content of Connes's programme. The spectral realisation conjecture IS the hard part of RH, not a technical lemma that can be bypassed.

### What Path 6 can still contribute

The conditional results from cycle 3 remain valid: IF Axiom 1 holds (H_R exists), THEN T_BC is essentially self-adjoint and spec(T_BC) = {gamma_n}. The contribution of Path 6 is to show that the CONDITIONAL chain works perfectly -- the only missing input is the spectral realisation itself.

## Result: BLOCKED (honest negative)

The Meyer Frechet-to-Hilbert gap is equivalent to RH via the Weil inner product positivity. Path 6 cannot close Axiom 1 independently. The conditional closures (cycles 3-4) remain the strongest results on this path.

## Next step

Path 6 should be reclassified as a COMPLETION path (like Path 3): it provides essential infrastructure (self-adjointness) but cannot independently close the bottleneck. Future cycles should focus resources on Path 1 (Brauer-KMS), which has the only route that could bypass Axiom 1.
