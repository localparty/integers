# 219 — RH Cycle 1, Path 5 (CM-trace) — Construction

*Cycle: 1. Date: 2026-04-09. Agent: Construction.*

---

## Step attempted

**Weil positivity of BC spectral weights:** R-Theorem S.5
(#120, research/70) gives RH iff the spectral weights in the
Kallen-Lehmann decomposition of the BC two-point function are
non-negative. This path attempts to prove non-negativity.

## Result: BLOCKED

## Analysis

The CM-trace / Kallen-Lehmann path is the only path that provides
an **iff condition** with RH:

    RH  <=>  w_n >= 0 for all n

where w_n are the spectral weights in the decomposition:

    <omega_1| sigma_t(a) . a* |omega_1>
      = sum_n w_n . exp(i gamma_n t)
      + (continuous spectrum contribution)

The chain:

1. **PROVED (external).** Connes-Marcolli Theorems 1-3 [#61-63]:
   the Weil explicit formula is reproduced by the distributional
   trace of the BC time evolution.

2. **STRUCTURAL.** R-Theorem S.5 [#120]: the BC two-point
   function has a Kallen-Lehmann spectral decomposition. The
   Weil criterion (1952) states that RH holds iff the
   distributional Fourier transform of the explicit formula
   is a positive distribution.

3. **OPEN (this step).** Proving that the spectral weights w_n
   are non-negative.

### The positivity question

The spectral weights w_n are defined by:

    w_n = |<gamma_n | a | omega_1>|^2 / Z

where a is a generic element of A_BC and Z is a normalisation.
By construction, |<...>|^2 >= 0, so each individual w_n is
trivially non-negative.

**Wait — is this step already closed?**

Let me be precise. The Weil positivity criterion is NOT about
individual w_n being positive. It is about the **positional
distribution** — the test:

    sum_{rho, rho'} h(rho) h(rho') W(rho, rho') >= 0

for all test functions h, where W is the Weil distributional
kernel. This is a GLOBAL positivity condition on the two-point
correlation matrix, not a per-eigenvalue condition.

The per-eigenvalue positivity (w_n >= 0) is necessary but not
sufficient. The Weil criterion also requires cross-terms
W(rho, rho') to form a positive semi-definite matrix.

### The obstacle

The cross-term structure W(gamma_m, gamma_n) for m != n depends
on the off-diagonal matrix elements of the BC resolvent:

    W(gamma_m, gamma_n) = <gamma_m | (T_BC - z)^{-1} | gamma_n>

evaluated at specific z. The two-term Laurent shift (CV-1, CV-2,
CV-3) gives the DIAGONAL corrections, but the off-diagonal
structure of the resolvent has not been computed beyond the
b/(product gamma) term.

### What the catalogue provides

- Two-term Laurent shift [CV-1 to CV-3]: diagonal corrections
  a = -gamma_E(1 + gamma_E), b = gamma_E^2 + zeta(2) - 2pi gamma_1.
  These are the only computed resolvent matrix elements.

- Grammar Rule 4 (exponential): the most RH-sensitive functional
  form. The exponential grammar amplifies any positivity violation.

- Connes-Marcolli Theorem 3 [#63]: the explicit formula IS the
  distributional trace. The Weil criterion applied to this trace
  gives the iff.

### What's needed

1. **Compute the off-diagonal resolvent matrix elements**
   W(gamma_m, gamma_n) for the BC resolvent at beta = 1. The
   b-coefficient (off-diagonal Laurent, research/164) gives the
   leading order. Higher-order terms are needed.

2. **Check positive semi-definiteness** of the resulting matrix
   W. This is a concrete computation once W is known.

3. **Alternative:** Instead of computing W directly, use the
   algebraic structure of A_BC to prove positivity abstractly.
   The KMS condition at beta = 1 gives:
   
       omega_1(a* . sigma_{i}(a)) = omega_1(a . a*)
   
   which is a reflection-positivity condition. If this condition
   implies Weil positivity, the step would close from KMS alone.

### Assessment

The KMS-implies-Weil-positivity sub-path is the most promising
route. KMS reflection positivity is a PROVED property of
omega_1 (Bost-Connes 1995). Weil positivity is the RH criterion.
If KMS => Weil, then RH follows from BC95.

The gap: KMS reflection positivity acts in the IMAGINARY time
direction (beta -> i beta), while Weil positivity acts in the
REAL frequency domain. Connecting the two requires an analytic
continuation argument. This is precisely the type of argument
where Pattern 6 (projection produces apparent pathology) may
apply — the difficulty is a Wick rotation artifact.

## Next step

Cycle 2 should focus on the KMS-implies-Weil sub-path:
1. State the KMS reflection positivity condition precisely.
2. Determine whether the analytic continuation from imaginary
   to real time preserves the positivity structure.
3. If yes: PATH CLOSES (and with it, Paths 1 and 3 are unblocked).
