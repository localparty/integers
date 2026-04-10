# 04. One Step of the Bootstrap

## 4.1 The bootstrap hypothesis

**Inductive hypothesis at step n:**

  H(n): m(L_n) >= mu_n > 0

where L_n is the current circumference and mu_n is a certified lower
bound on the mass gap.


## 4.2 The step: from m(L_n) > 0 to m(L_n + delta) > 0

**Setup.** Suppose m(L_n) >= mu_n > 0. The cluster expansion at L = L_n
converges (by Theorem 3.4, provided mu_n > K/L_n). This gives:

(a) m(L) is real-analytic in L near L_n.
(b) We can compute m'(L_n) and higher derivatives from the convergent
    cluster expansion.
(c) The radius of analyticity R_n is bounded below by:

  R_n >= c_1 / |m'(L_n)/m(L_n)|

where c_1 is a constant from the Kotecky-Preiss theory.

**The step size.** We can take delta_n to be any value less than R_n
such that m(L_n + delta_n) > 0. The optimal choice is:

  delta_n = sup { delta > 0 : m(L_n + delta') >= mu_n/2
                  for all delta' in [0, delta] }


## 4.3 Computing the step size: what determines delta_n

The step size delta_n is controlled by two competing effects:

**(A) The analyticity radius.** From the cluster expansion, the
analyticity radius R_n is determined by the ratio of the mass gap to
the "stiffness" of the system:

  R_n ~ m(L_n) / |dm/dL|_{max}

where |dm/dL|_{max} is the maximum rate at which m can change.

**(B) The derivative dm/dL.** This is the key quantity. How fast does
the mass gap change as we vary L?


## 4.4 Estimating dm/dL

**Exact formula.** From the definition m(L) = E_1(L) - E_0(L):

  dm/dL = dE_1/dL - dE_0/dL

The Hellmann-Feynman theorem gives:

  dE_n/dL = <psi_n| dH_L/dL |psi_n>

where |psi_n> is the n-th eigenstate of H_L.

**What is dH_L/dL?** When L changes by dL, the spatial circle changes.
The Hamiltonian H_L is the generator of time translations for the sigma
model on S^1_L. Changing L changes the boundary condition (the position
of the identification) and the mode spectrum.

In the lattice formulation (N_s spatial sites of spacing a = L/N_s):
increasing L by dL = a means adding one spatial site. The Hamiltonian
changes by the insertion of one additional transfer matrix factor in the
spatial direction.

**Bound on dm/dL.** [ARGUED]

  |dm/dL| <= C_2 / L

where C_2 is a constant depending on the coupling. The reasoning:

The mass gap m(L) has dimensions of [length]^{-1}. The only length scale
in the Z_3-twisted theory (besides L itself) is 1/Lambda. Therefore:

  m(L) = Lambda x F(L Lambda)

for a dimensionless function F. Then:

  dm/dL = Lambda^2 F'(L Lambda)

and:

  |dm/dL| / m = |F'|/F x Lambda

So dm/dL is of order m x Lambda ~ m/L (up to logs) when L ~ 1/Lambda.

More rigorously, from the cluster expansion, the derivative dm/dL is
given by:

  dm/dL = -(1/L) sum_{gamma wrapping} rho'(gamma) + (non-wrapping terms)

The wrapping polymers (those that go around S^1_L) contribute a term
of order exp(-m L) x (derivative w.r.t. L). The non-wrapping polymers
contribute a term that changes smoothly with L.

**Result.** At intermediate L (L ~ 1/Lambda):

  |dm/dL| <= C_2 m(L) x max(1/L, Lambda)


## 4.5 The step size formula

From the analyticity radius bound and the derivative bound:

  delta_n >= mu_n / (2 |dm/dL|) >= mu_n / (2 C_2 mu_n / L_n) = L_n / (2 C_2)

**KEY RESULT.** [ARGUED]

  delta_n >= c_3 L_n

where c_3 = 1/(2 C_2) is a POSITIVE constant independent of n.

This means: the step size is a fixed FRACTION of the current L. Each
step increases L by a multiplicative factor:

  L_{n+1} = L_n + delta_n >= L_n (1 + c_3)

This is GEOMETRIC growth! It means:

  L_n >= L_0 (1 + c_3)^n

and L_n -> infinity as n -> infinity.


## 4.6 The detailed bootstrap step

**Input:** m(L_n) >= mu_n, cluster expansion converges at L_n.

**Step 1: Compute derivatives.**
From the convergent cluster expansion at L_n, compute:

  m'(L_n) = dm/dL |_{L=L_n}
  m''(L_n)  (and higher derivatives if needed)

These are given by convergent sums over polymers.

**Step 2: Bound the step size.**
The Taylor expansion gives:

  m(L_n + delta) = m(L_n) + m'(L_n) delta + (1/2) m''(xi) delta^2

for some xi in [L_n, L_n + delta].

We need m(L_n + delta) > 0. Using |m'| <= C_2 m/L and
|m''| <= C_3 m/L^2:

  m(L_n + delta) >= m(L_n) - C_2 (m(L_n)/L_n) delta - C_3 (m(L_n)/L_n^2) delta^2

  = m(L_n) [ 1 - C_2 delta/L_n - C_3 (delta/L_n)^2 ]

This is positive when delta/L_n < (-C_2 + sqrt(C_2^2 + 4 C_3))/(2 C_3).
Call this threshold r_0. Then:

  delta_n = r_0 L_n

works.

**Step 3: Update the lower bound.**

  mu_{n+1} = m(L_n)(1 - C_2 r_0 - C_3 r_0^2) > 0

Note: mu_{n+1}/mu_n = 1 - C_2 r_0 - C_3 r_0^2 < 1, so the lower bound
DECREASES at each step. The question is: does it decrease to zero in
finite or infinite time?


## 4.7 Evolution of the lower bound mu_n

At each step:

  mu_{n+1} >= mu_n (1 - c_4)

where c_4 = C_2 r_0 + C_3 r_0^2 < 1. After n steps:

  mu_n >= mu_0 (1 - c_4)^n = mu_0 exp(-|ln(1-c_4)| n)

This decays EXPONENTIALLY in n. But L_n grows exponentially:

  L_n = L_0 (1 + c_3)^n

So as a function of L:

  mu(L) >= mu_0 (L/L_0)^{-alpha}

where alpha = |ln(1 - c_4)| / ln(1 + c_3).

**The key question: what is alpha?**

If alpha < infinity (which it is, since c_3 > 0 and c_4 < 1), then
mu(L) >= mu_0 (L/L_0)^{-alpha} is a POWER LAW lower bound on the mass
gap. It goes to zero as L -> infinity, but it is positive for ALL
finite L.

This would prove m(L) > 0 for all L > 0 (but not m(infinity) > 0, which
requires a separate argument — see Section 05).


## 4.8 The crucial assumption: c_4 < 1

The entire bootstrap works if c_4 = C_2 r_0 + C_3 r_0^2 < 1, i.e.,
the fractional decrease in the lower bound at each step is strictly
less than 1.

**What could make c_4 >= 1?** If the mass gap m(L) can change by
O(m) when L changes by O(L), i.e., if:

  |L dm/dL| / m ~ O(1)  or larger

This would mean the mass gap is very sensitive to L — a near-critical
phenomenon.

**Physical argument against c_4 >= 1:** The Z_3 twist prevents the
theory from entering a critical phase. The twist breaks SU(3) -> U(1)^2,
and there is no continuous symmetry restoration as L varies (the twist
is imposed externally, not dynamically). Therefore, one does not expect
large fluctuations in m(L).

**Mathematical argument:** From the cluster expansion, the derivative
dm/dL is a sum over polymers. The dominant contribution comes from
polymers that wrap around S^1_L (since these are the ones sensitive to
L). The wrapping polymer contribution is of order:

  |dm/dL|_wrapping ~ m exp(-m L) x (something)

which is EXPONENTIALLY SMALL compared to m/L when mL >> 1.

So for mL >> 1 (which holds at the starting point L = L_0 when
m(L_0) ~ Lambda and L_0 ~ 1/Lambda, giving m L_0 ~ 1), the derivative
is dominated by non-wrapping terms of order m/L, giving c_4 << 1.

For mL ~ 1 (the dangerous regime where the mass gap is comparable to
the inverse circumference), the wrapping terms are O(1), and the bound
c_4 < 1 becomes a quantitative statement about the cluster expansion
coefficients.


## 4.9 The dangerous regime: m(L) ~ 1/L

If the mass gap were to approach 1/L from above, the cluster expansion
convergence condition m > K/L would be threatened.

**Scenario A (safe):** m(L) > C/L for some C > K for all L. Then
convergence holds everywhere, and the bootstrap goes through.

**Scenario B (dangerous):** m(L) decreases toward K/L as L increases.
The cluster expansion becomes marginally convergent, the step size
delta_n shrinks, and the bootstrap might stall.

**What distinguishes A from B?** The behavior of the product mL as a
function of L.

At small L: mL ~ L^2 Lambda^2 -> 0 as L -> 0 (fractional instanton
regime). But m_KK L = 2pi/3 ~ 2, so the KK modes keep mL bounded.

At L ~ 1/Lambda: mL ~ O(1). This is the crossover regime.

At large L: mL ~ m(infinity) L -> infinity. So mL grows without bound.

**The non-monotonicity of mL.** The product mL starts at O(1) (from
KK modes), may dip near L ~ 1/Lambda, then grows linearly. The
question is: HOW LOW does the dip go?

If the dip keeps mL > K, the bootstrap works. If mL dips below K at
some L*, the cluster expansion loses convergence there.


## 4.10 Status of one bootstrap step

**What is PROVED:**
- The cluster expansion converges when m > 0 and is large enough
  relative to K/L. [PROVED, standard Kotecky-Preiss theory]
- Convergence implies analyticity of m(L). [PROVED]
- Analyticity implies m(L + delta) > 0 for small enough delta. [PROVED]

**What is ARGUED:**
- The step size delta_n >= c_3 L_n (geometric growth). [ARGUED, based on
  dimensional analysis + cluster expansion bounds]
- The lower bound mu_n decays at most as a power law in L_n. [ARGUED]
- The constant c_4 < 1 (each step only costs a bounded fraction of the
  mass gap). [ARGUED, based on the Z_3 twist preventing criticality]

**What is OPEN:**
- Whether the cluster expansion convergence condition m > K/L is
  maintained for all L (i.e., whether mL stays bounded below). [OPEN]
- The precise values of C_2, C_3, and hence c_3, c_4. [OPEN,
  requires detailed computation of polymer activities]
