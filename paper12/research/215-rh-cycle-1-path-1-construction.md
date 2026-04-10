# 215 — RH Cycle 1, Path 1 (Brauer-KMS) — Construction

*Cycle: 1. Date: 2026-04-09. Agent: Construction.*

---

## Step attempted

**Spectral density irrationality:** Show that the spectral density
factor f(gamma) in Paper 25 §5.4 — the accumulated phase shift
from a hypothetical off-line zero — is generically irrational
(or at least not an integer multiple of k), so that the continuous
perturbation delta cannot be absorbed into the discrete Brauer
class beta_k in H^2(Z/kZ, U(1)).

## Result: BLOCKED

## Analysis

The Brauer-KMS path (Conjecture 2, Critical 1 in the catalogue
[210: 25.C2]) has the following chain:

1. **PROVED.** Bridge theorem at k=3: Brauer class = 1/3 mod Z
   = Fuglede-Kadison class [24.1, research/162].

2. **STRUCTURAL.** The contradiction argument (Compendium §C.2):
   off-line zero with Re(s) = 1/2 + delta produces a continuous
   phase shift delta_c ~ exp(2 pi i delta f(gamma) / k) to the
   obstruction class. Since the Brauer class is discrete (element
   of Z/kZ), the perturbation must vanish => delta = 0.

3. **OPEN (this step).** The argument requires f(gamma) to NOT be
   an integer multiple of k (otherwise the continuous perturbation
   would map to the identity in Z/kZ and no contradiction arises).

### Why this step is blocked

The function f(gamma) is defined as a spectral density integral
over the zeta zeros:

    f(gamma) = integral of rho(t) . K(gamma, t) dt

where rho(t) is the spectral density of the Riemann zeros and
K is a kernel from the V-coupling commutator [log R-hat, Pi_chi].

To prove f(gamma) is irrational (or not a multiple of k), we need:

1. **An explicit formula for f(gamma).** The V-coupling operator
   V = lambda . tau_1 . [log R-hat, Pi_chi] is defined
   (Conjecture 5 / Critical 8 [210: 25.C5]), but the spectral
   density factor arising from an off-line zero's contribution to
   the commutator has not been computed in closed form.

2. **An irrationality result for that formula.** Even if f(gamma)
   were computed, showing it is irrational requires either:
   - (a) Identifying f(gamma) with a known irrational (e.g., a
     transcendental function of gamma_n), or
   - (b) Proving irrationality from scratch for the specific
     spectral density integral.

### What's available from the catalogue

- **Operator dictionary closure** [Critical 6, CV-6]: the
  dictionary is closed under sum/product/ratio/power/log/exp.
  This means f(gamma) should be expressible in terms of the
  dictionary's building blocks {gamma_n, pi, zeta(2), gamma_E, e}.
  These are generically transcendental, which is promising.

- **Grammar Rule 4** (exponential): exp(gamma_n pi^2/2) is the
  most RH-sensitive functional form. If f(gamma) involves an
  exponential, irrationality follows from Lindemann-Weierstrass
  (e^alpha is transcendental for algebraic nonzero alpha).

- **Pattern 4** (topological rigidity): the discrete invariant
  (Brauer class) cannot absorb a continuous perturbation. This is
  the META-PRINCIPLE, but making it rigorous requires the
  irrationality step.

### What's needed to close this step

1. **Compute f(gamma) explicitly** from the V-coupling definition
   and the off-line zero contribution. This requires working through
   the commutator [log R-hat, Pi_chi] with an off-line eigenvalue
   present.

2. **Prove f(gamma) is not a k-integer.** Once computed, establish
   that f(gamma) is irrational or at least not in (1/k)Z for any
   of the bridge indices k in {3, 4, 6}.

### Alternative sub-path

Instead of proving irrationality of f(gamma), one could:
- Show that f(gamma) depends continuously on delta (the off-line
  displacement), so that for GENERIC delta, f is not a k-integer.
  Then the set of delta values that evade the contradiction has
  measure zero, and by analyticity of zeta(s), a zero cannot sit
  at a measure-zero set of delta values unless it is at delta = 0.

This "genericity + analyticity" approach may be more tractable
than a direct irrationality proof.

## Next step

Cycle 2 should:
1. Write out the explicit commutator [log R-hat, Pi_chi] with an
   off-line zero eigenvalue lambda_extra present.
2. Compute the resulting phase shift delta_c as a function of
   delta and gamma.
3. Determine whether the "genericity + analyticity" sub-path
   closes the irrationality gap.
