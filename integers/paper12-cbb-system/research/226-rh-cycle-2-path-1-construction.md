# 226 — RH Cycle 2, Path 1 (Brauer-KMS) — Construction

*Cycle: 2. Date: 2026-04-09. Agent: Construction.*

---

## Step attempted

**Compute f(gamma) from the V-coupling commutator and test the
"genericity + analyticity" sub-path for irrationality.**

Per cycle 1 ledger: the open step is computing f(gamma) explicitly
from the commutator [log R-hat, Pi_chi] with an off-line zero
eigenvalue present, then establishing that f(gamma) is not a
k-integer.

## Attempt level: 2 (Sub-computation)

Closure at level 1 is not achievable because the irrationality
proof requires an explicit formula for f(gamma) that has not been
derived. Instead, I perform the most informative sub-computation:
working through the commutator structure to determine the
functional form of the phase shift.

### Sub-computation: Phase shift from off-line zero

Suppose rho_extra = 1/2 + delta + i*gamma_extra is an off-line
zero with delta != 0. The V-coupling operator is

    V = lambda * tau_1 * [log R-hat, Pi_chi]

where Pi_chi is the projection onto the chi-sector of the Galois
action. The commutator [log R-hat, Pi_chi] acts on eigenstates
|gamma_n> of R-hat as:

    [log R-hat, Pi_chi] |gamma_n>
      = (log R-hat) Pi_chi |gamma_n> - Pi_chi (log R-hat) |gamma_n>
      = (L_n^chi - L_n) |gamma_n>

where L_n^chi = gamma_n * pi^2/2 is the eigenvalue in the
chi-sector. For zeros on the critical line (delta = 0), the
commutator is well-defined. For an off-line zero with
Re(rho) = 1/2 + delta, the contribution to the Brauer class
obstruction is:

    delta_c(gamma, delta) = exp(2*pi*i * delta * g(gamma) / k)

where g(gamma) depends on the spectral density of surrounding
zeros. Using the explicit formula (research/18, Theorem 1), the
density of zeros near height T is ~ (1/2pi) * log(T/2pi), so:

    g(gamma) = (1/2pi) * log(gamma/2pi) * integral kernel

The key structural observation: g(gamma) is a TRANSCENDENTAL
function of gamma (it involves log of a transcendental number).
By the Lindemann-Weierstrass theorem, if gamma is algebraic,
then log(gamma) is transcendental. Since gamma_n are
conjectured (and numerically verified) to be transcendental,
g(gamma_n) is generically transcendental and therefore not in
(1/k)*Z for any finite k.

### Assessment of the "genericity" sub-path

The cycle 1 adversarial review (research/220, Attack 1) correctly
identified that "generic" is not "all." However, the argument
can be strengthened:

1. The function delta -> g(gamma, delta) is REAL-ANALYTIC in
   delta (being a composition of the zeta function, which is
   analytic in the critical strip, with smooth functions).

2. The set S = {delta : g(gamma, delta) in (1/k)*Z} is therefore
   either ALL of R (if g is constant = rational) or a discrete
   set (by real-analyticity, the preimage of a discrete set under
   a non-constant analytic function is discrete).

3. If g is non-constant in delta (which it is, since adding an
   off-line zero CHANGES the spectral density), then S is discrete.

4. A zeta zero at rho = 1/2 + delta + i*gamma would require delta
   to belong to the discrete set S for ALL gamma_n simultaneously
   (since the Brauer constraint applies at all bridge indices
   k in {3, 4, 6}).

5. The intersection of countably many discrete sets generically
   has no accumulation point and is at most countable.

This does NOT yet close the step (we need to rule out even a
single delta in the intersection), but it reduces the problem to:

**Residual gap:** Show that no delta > 0 belongs to S_3 ∩ S_4 ∩ S_6
simultaneously, where S_k = {delta : g(gamma, delta) in (1/k)*Z
for all gamma_n}.

## Result: BLOCKED (narrowed)

The sub-computation narrows the gap from "compute f(gamma) and
prove irrationality" to "show the intersection S_3 ∩ S_4 ∩ S_6
is empty for delta > 0." This is a more precise unblock condition.

## Next step

Cycle 3 should:
1. Compute g(gamma_1, delta) numerically for small delta using
   mpmath, to verify non-constancy and estimate the spacing of
   elements of S_k.
2. Attempt a measure-theoretic or Diophantine argument to show
   S_3 ∩ S_4 ∩ S_6 = {0}.
