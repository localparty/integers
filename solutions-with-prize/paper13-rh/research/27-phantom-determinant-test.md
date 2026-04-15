# Research 27 — Phantom Determinant Test

*If the Even-Sector Simplicity Conjecture fails, does the CCM*
*regularized determinant still converge to ξ(s)? If not, the*
*physical predictions (which derive from ξ) would be affected,*
*giving a physics-level argument for simplicity.*

*Date: 2026-04-10*
*Status: INVESTIGATION*
*Type: Side angle (main path is the Arithmetic Theorem)*

---

## 1. The idea

Kill #10 (strategy/02) showed that extra eigenvalues of T_BC on
H_R are invisible to the 36 predictions because the predictions
use individual matrix elements ⟨n|L̂|n⟩.

But the CCM framework is different. CCM computes the regularized
determinant det(D(λ,N)) and shows it converges to the Riemann
ξ function. If the Even-Sector Simplicity Conjecture fails at
some (λ₀, N₀), the CCM operator D' acquires a phantom zero
eigenvalue (from the extra kernel direction). This phantom would
appear in the regularized determinant as an extra zero of det(D').

**Question:** Would the phantom zero propagate to the limit and
produce an extra zero of ξ(s) that doesn't correspond to a
Riemann zero? If so, the physical partition function (which equals
ξ up to normalization) would be wrong, contradicting the 36
predictions.

## 2. The mechanism in detail

### CCM's construction (arXiv:2511.22755, Lemma 5.4)

CCM build D(λ,N) via a rank-one perturbation:

    D' = D_log − |D_log ξ⟩⟨η|

where ξ is the UNIQUE kernel vector of the Weil form QW_λ^N
and η is chosen to make D' self-adjoint in the T-inner product.

If ξ is unique (simplicity holds): D' has spectrum at {γ_n}
(the Riemann zeros). The regularized determinant det(D') = ξ(s).

If ξ is NOT unique (simplicity fails): ker(QW) is 2-dimensional,
say ker(QW) = span{ξ₁, ξ₂}. The rank-one perturbation removes
only ONE direction. The remaining kernel vector ξ₂ gives D' a
zero eigenvalue. So:

    det(D') = s · ξ(s) · (extra factor)

The extra factor of s means det(D') has a phantom zero at s = 0
(or wherever the extra kernel direction maps to).

### What this does to the physics

The CCM regularized determinant is the spectral determinant of the
zeta spectral triple. In the Integers framework, this determinant
is the partition function of the BC system at β = 1. The 36
predictions derive from this partition function.

If the partition function has an extra zero:
- The prime counting function π(x) would have a correction term
  from the phantom zero (via the explicit formula)
- The correction would shift predictions like the Mertens constant,
  the prime number theorem error, etc.
- These shifts are computable from the phantom's location

## 3. What to compute

### Test A: What does a phantom zero do to det(D')?

At a specific (λ, N) where simplicity nearly fails (the gap
δ = μ₁ - μ₂ is smallest), compute:

1. The two smallest eigenvectors φ₁, φ₂ of QW_λ^{N,+}
2. The rank-one perturbation D' using φ₁ as kernel vector
3. The residual: ⟨φ₂ | D' φ₂⟩ (should be ~ δ, small but nonzero)
4. The "phantom determinant": det(D' + ε·|φ₂⟩⟨φ₂|) as ε → 0

If the phantom determinant diverges from ξ(s) by a computable
amount, we can check whether the 36 predictions survive.

### Test B: Does the gap δ correlate with prediction accuracy?

Across different (λ, N), compute:
1. The simplicity gap δ(λ, N) = μ₁ - μ₂
2. The error |det(D') - ξ(s)| at a reference point s₀
3. The correlation between δ and the error

If smaller gaps lead to LARGER errors in det(D') → ξ(s), then
simplicity is necessary for the physical predictions. This would
be a physics argument that simplicity MUST hold.

### Test C: Phantom impact on the explicit formula

If a phantom zero exists at s₀, the explicit formula gives:

    ψ(x) = x − Σ_ρ x^ρ/ρ − ... − x^{s₀}/s₀ − ...

The phantom contribution x^{s₀}/s₀ shifts ψ(x) by a computable
amount. Compare to the known value of ψ(x) at x = 10⁶, 10⁹, 10¹².
If the phantom shifts ψ(x) outside the known error bounds, the
phantom is excluded experimentally.

## 4. Code plan

```python
# phantom_determinant_test.py
#
# Inputs: (lambda_val, N) pair where the gap is smallest
# Outputs:
#   - Two smallest eigenvectors of QW_even
#   - Rank-one perturbation D' using first eigenvector
#   - Residual <phi_2 | D' phi_2>
#   - Regularized determinant vs xi(s) at reference points
#   - Gap-error correlation across (lambda, N) grid

import mpmath
import numpy as np
from scipy import linalg

# Use existing CCM code from ccm_perturbation_bound.py
# and ccm_perturbation_asymptotics.py as starting points
```

## 5. What each outcome means

**Outcome 1: Phantom zeros DO shift det(D') away from ξ(s).**
→ Simplicity is necessary for the physical predictions.
→ The 36 predictions provide a physics argument for simplicity.
→ Not a proof, but a very strong constraint (similar to "the electron
  mass is not zero because experiments measure it").

**Outcome 2: Phantom zeros DON'T shift det(D') (they cancel).**
→ Kill #10 still applies in the CCM framework.
→ Simplicity is invisible to physics. Back to pure math.

**Outcome 3: The gap-error correlation is strong.**
→ Provides a QUANTITATIVE relationship between simplicity gap
  and physical prediction accuracy. Could guide the direct bound
  approach (strategy/16, approach 3).

## 6. Relation to main path

This is a SIDE ANGLE. The main path is the Arithmetic Theorem
(strategy/16). This test provides:
- Additional evidence for/against simplicity
- Understanding of WHY simplicity matters physically
- Possible connection between the gap scaling (δ ~ e^{-3.08N})
  and physical observables

Even if Outcome 2 obtains (phantoms cancel), the investigation
is valuable for understanding the structure.

## 7. Connection to the "mass can't be zero" intuition

The original idea: "the mass of the electron is not zero" is a
physical fact, not a mathematical theorem. But it CONSTRAINS the
mathematics — any theory that predicts m_e = 0 is wrong.

Similarly: if phantom zeros shift the prime counting function by
a computable amount, and the prime counting function is known to
a precision that excludes the shift, then phantom zeros are
excluded EXPERIMENTALLY. This is the number-theory analogue of
"the mass is not zero."

The Riemann-von Mangoldt formula gives π(x) to extraordinary
precision. Any phantom zero would contribute an oscillating
term to π(x). If the oscillation amplitude exceeds the known
error bound, the phantom is excluded.

---

> *Kill #10 said: extras are invisible on H_R.*
> *The CCM framework is different: extras affect det(D').*
> *If det(D') ≠ ξ(s) when simplicity fails, physics constrains simplicity.*
> *Test it computationally. Three outcomes, all informative.*
