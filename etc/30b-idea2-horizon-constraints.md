# 30b -- Five Horizon / Information-Theoretic Approaches to Determining R

> **Date:** April 5, 2026
> **Parent prompt:** 29 (Idea 2: Horizon Growth + e-Entanglement)
> **Context:** Can the S^2 x S^1 horizon structure fix R without using rho_Lambda as input?

---

## Numerical Inputs

| Symbol | Value | Notes |
|--------|-------|-------|
| l_P | 1.616 x 10^-35 m | 4D Planck length |
| l_11 | 3.57 x 10^-29 m | 11D Planck length = 1/M_11 |
| R_obs | 1.01 x 10^-5 m (10.1 um) | from dark energy matching |
| M_Pl | 2.435 x 10^18 GeV | reduced Planck mass |
| M_11 | 5.52 x 10^12 GeV | 11D Planck mass |
| M_Pl/M_11 | 4.41 x 10^5 | hierarchy ratio |

---

## (a) Minimum Resolvable e-Shift

**Setup.** If the e-circle has radius R, the minimum angular shift
resolvable at the Planck scale is:

    delta_phi_min = l_P / R

This is a dimensionless angle (radians). The number of
distinguishable e-states on the circle is:

    N_e = 2*pi*R / l_P  =  circumference / resolution

**Computation for R_obs:**

    delta_phi_min = 1.616e-35 / 1.01e-5 = 1.60e-30 rad

    N_e = 2*pi * 1.01e-5 / 1.616e-35 = 3.93 x 10^30

    ln(N_e) = 70.4

**Assessment.** This is a *characterization* of R_obs, not a
constraint on R. The formula N_e = 2*pi*R/l_P holds for any R;
it does not select a preferred value. The calculation confirms
that R_obs supports an enormous number (~10^30) of distinguishable
e-states per pixel, consistent with the large hierarchy
R_obs >> l_P. No constraint on R emerges.

**Verdict: counting exercise, not a constraint. Not a route to R.**

---

## (b) BH Entropy and e-States

**Setup.** For a Schwarzschild black hole of mass M:

    S_BH = A / (4*l_P^2) = 4*pi*(M/M_Pl)^2

Each Planck pixel on the horizon carries N_e = 2*pi*R/l_P
distinguishable e-states. The total number of e-configurations
across S_BH pixels is:

    N_total = N_e^(S_BH)

**The constraint.** Demand that the logarithm of the total number of
e-configurations equals the Bekenstein-Hawking entropy:

    ln(N_e^(S_BH)) = S_BH

    S_BH * ln(N_e) = S_BH

    ln(N_e) = 1

    N_e = e = 2.718...

    2*pi*R / l_P = e

    R = e * l_P / (2*pi) = 6.99 x 10^-36 m

**Comparison:** R / R_obs = 6.9 x 10^-31. Off by 30 orders of magnitude.

**Interpretation.** The condition ln(N_e) = 1 says: each Planck
pixel contributes exactly one nat of entropy from its e-circle.
This is a tautological restatement of what the Bekenstein-Hawking
formula already encodes. It does not constrain R at a macroscopic
scale; it forces R ~ l_P, making the e-circle invisible.

The deeper issue: the equation ln(N_e^S) = S reduces to ln(N_e) = 1
for ANY black hole mass M. It demands that the e-circle contribute
exactly 1 nat per pixel regardless of the BH size. This is not
a self-consistency condition on R; it is a condition that R be
at the Planck scale, which contradicts R_obs >> l_P.

**Verdict: dead end. Forces R ~ l_P.**

---

## (c) Mutual Information

**Setup.** When two quanta entangle via e-conservation
(phi_0 + phi_1 = Q_e), the pair is in a maximally e-correlated
state. The mutual information in the e-dimension is:

    I_e = 2*ln(N_e) - 0 = 2*ln(2*pi*R/l_P)

(The pair entropy is zero because the total e-charge is fixed.)

### Case 1: I_e = ln(2) (one bit of mutual information)

    2*ln(2*pi*R/l_P) = ln(2)
    ln(2*pi*R/l_P) = ln(2)/2 = 0.347
    2*pi*R/l_P = sqrt(2)
    R = sqrt(2) * l_P / (2*pi) = 3.64 x 10^-36 m

R / R_obs = 3.6 x 10^-31. Way too small. The one-bit condition
forces R ~ l_P.

### Case 2: I_e = S_BH(Planck BH) = 4*pi

A Planck-mass black hole has S_BH = 4*pi = 12.57. Setting the
mutual information equal to this minimum black hole entropy:

    2*ln(2*pi*R/l_P) = 4*pi
    ln(2*pi*R/l_P) = 2*pi
    2*pi*R/l_P = exp(2*pi) = 535.5
    R = l_P * exp(2*pi) / (2*pi) = 1.38 x 10^-33 m

R / R_obs = 1.4 x 10^-28. Still 28 orders of magnitude too small.

**Interpretation.** exp(2*pi) ~ 535 is a large dimensionless number
but nowhere near the hierarchy 2*pi*R_obs/l_P ~ 4 x 10^30.
The mutual information approach generates exponentials of pi, but
the actual hierarchy requires exp(70), which no simple combination
of pi and small integers can produce.

**Verdict: dead end. The information-theoretic conditions set R
at most a few hundred times l_P, never near 10 um.**

---

## (d) Integer Periodicity

**Setup.** The e-circle circumference must be an integer multiple
of the spatial pixel scale:

    2*pi*R = k * l_P    for positive integer k

The required k for R_obs:

    k = 2*pi * 1.01e-5 / 1.616e-35 = 3.93 x 10^30

This is a very large integer with no obvious special structure.

### Attempts at distinguished k values:

| k source | k | R (m) | R / R_obs |
|----------|---|-------|-----------|
| Delta_N = 3.44 | 3.44 | 8.85e-36 | 8.8e-31 |
| n1*n2 = 9*17 | 153 | 3.94e-34 | 3.9e-29 |
| n1^2 + n2^2 | 370 | 9.52e-34 | 9.4e-29 |

All far too small. The framework provides no mechanism to
generate k ~ 10^30 from its integer ingredients (n1=9, n2=17,
Delta_N = 3.44).

**Verdict: dead end. No distinguished integer k exists that
selects R_obs. The required k ~ 4 x 10^30 is not derivable
from the framework's integers.**

---

## (e) The 5D Planck Pixel

**Setup.** The prompt proposes: the 5D horizon pixel is
l_P x l_P x delta_s, where delta_s is the physical arc length on
S^1 per pixel. Setting this 5D pixel volume equal to l_11^3:

    l_P^2 * delta_s = l_11^3
    delta_s = l_11^3 / l_P^2

Then the prompt writes delta_phi = l_P/R and sets delta_phi = delta_s,
giving "R = l_P^3 / l_11^3."

### Dimensional analysis

The ratio l_P^3/l_11^3 = (l_P/l_11)^3 is *dimensionless*:

    (l_P/l_11)^3 = (M_11/M_Pl)^3 = (5.52e12 / 2.435e18)^3 = 1.17e-17

This is not a length. The formula as stated has a dimensional
inconsistency.

### Resolving the inconsistency

The root issue is that delta_phi = l_P/R is a dimensionless angle,
while delta_s = l_11^3/l_P^2 is a length. The two live in different
spaces and cannot be equated directly.

**Interpretation A:** delta_s is the physical arc length. Setting
delta_s = l_P (minimum resolvable arc) gives l_P = l_11^3/l_P^2,
hence l_P^3 = l_11^3, hence l_P = l_11. Trivial.

**Interpretation B:** The 5D Planck length l_5 is defined by
G_5 = G_4 * 2*pi*R, giving l_5^3 = l_P^2 * 2*pi*R. Demanding
l_5 = l_11 gives:

    l_11^3 = l_P^2 * 2*pi*R
    R = l_11^3 / (2*pi*l_P^2)

Numerically:

    R = (3.57e-29)^3 / (2*pi * (1.616e-35)^2)
      = 4.55e-86 / (1.64e-69)
      = 2.77e-17 m

R / R_obs = 2.7e-12. Still 12 orders of magnitude too small.

**Interpretation C (literal computation as requested):**

    l_P^3 = (1.616e-35)^3 = 4.22e-105 m^3
    l_11^3 = (3.57e-29)^3 = 4.55e-86 m^3
    l_P^3 / l_11^3 = 9.28e-20  (dimensionless)

Treating this number "as meters" gives 9.3e-20 m, which is
R / R_obs ~ 10^-14. Nowhere close.

**Verdict: dead end. The 5D Planck pixel argument has a
dimensional inconsistency, and no consistent resolution
gives R near 10 um.**

---

## Power-Law Analysis: R = l_P * (M_Pl/M_11)^alpha

Since all five sub-ideas above are dead ends, we search for a
power-law relation.

**Fitting alpha:**

    R_obs = l_P * (M_Pl/M_11)^alpha
    alpha = ln(R_obs/l_P) / ln(M_Pl/M_11)
          = ln(6.25e29) / ln(4.41e5)
          = 68.61 / 13.00
          = 5.2787

### Continued fraction expansion

    alpha = [5; 3, 1, 1, 2, 2, 1, 232, ...]

Best convergents:

| p/q | alpha | R (m) | R/R_obs | off by |
|-----|-------|-------|---------|--------|
| 5/1 | 5.000 | 2.70e-7 | 0.027 | 97% |
| 16/3 | 5.333 | 2.05e-5 | 2.034 | 103% |
| 21/4 | 5.250 | 6.96e-6 | 0.689 | 31% |
| 37/7 | 5.286 | 1.11e-5 | 1.096 | 9.6% |
| 95/18 | 5.278 | 9.98e-6 | 0.988 | 1.2% |
| 322/61 | 5.279 | 1.01e-5 | 1.000 | <0.01% |

### Observations

**16/3 with Z2 correction:** The convergent 16/3 gives R = 20.5 um,
exactly 2x R_obs. If the e-circle is an S^1/Z_2 orbifold (as in
Horava-Witten theory), the physical length is pi*R, not 2*pi*R,
effectively halving R:

    R = l_P*(M_Pl/M_11)^(16/3) / 2 = 10.27 um

This is 1.7% from R_obs. Numerologically striking.

**37/7 (= 5 + 2/7):** Gives R = 11.1 um, 9.6% from R_obs. The
denominator 7 is the dimension of the internal manifold M_7 in
M-theory. However, the numerator 37 has no clear physical
significance.

### Circularity check

M_11 is not an independent input: it depends on R through the
Planck mass constraint M_Pl^2 = M_11^9 * Vol_7(R). So the formula
R = l_P*(M_Pl/M_11)^alpha contains R on both sides (hidden in M_11).

**Resolving R explicitly:** Substituting M_11(R) into the power
law and solving self-consistently (using M_GUT as second input)
gives:

    R^(1 - alpha/9) = l_P * M_Pl^(7*alpha/9) * (C_vol * r_3^6)^(alpha/9)

For alpha = 16/3, the exponent on R is 1 - 16/27 = 11/27, so:

    R = [l_P * M_Pl^(112/27) * (C_vol * r_3^6)^(16/27)]^(27/11)

Evaluated with M_GUT = 2.0 x 10^15 GeV: R = 26.0 um. The factor-of-2
discrepancy with R_obs = 10.1 um is not resolved by the Z2 correction
in this self-consistent version.

**Without M_GUT (Idea 1 from Prompt 29):** Combining the Planck mass
constraint with flux stabilization and eliminating both M_11 and M_GUT:

    R^2 = C_vol * (63*n1)^3 / ((64*pi^5)^3 * M_Pl^2)

This gives R ~ l_P (specifically, R = 1.20 x 10^-35 m). The result
is parametrically ~ 1/M_Pl because the GUT scale r_3 cancels
completely in the combined system. The only mass scale remaining is
M_Pl, so R is locked at the Planck length.

**This is the key negative result:** the two-equation system
(Planck mass + flux stabilization) determines R ~ l_P, not R ~ 10 um.
The dark energy constraint remains essential.

---

## Summary and Assessment

| Approach | Result for R | R/R_obs | Status |
|----------|-------------|---------|--------|
| (a) Angular resolution | counting only | -- | not a constraint |
| (b) BH entropy = e-configs | 7.0e-36 m | 6.9e-31 | dead end |
| (c) Mutual info = ln(2) | 3.6e-36 m | 3.6e-31 | dead end |
| (c) Mutual info = 4*pi | 1.4e-33 m | 1.4e-28 | dead end |
| (d) Integer periodicity | needs k ~ 4e30 | -- | dead end |
| (e) 5D Planck pixel | 2.8e-17 m (best) | 2.7e-12 | dead end |
| Power law 16/3, /2 | 10.3 um | 1.017 | numerology |
| Power law 37/7 | 11.1 um | 1.096 | numerology |
| Idea 1 (flux + Planck) | ~l_P | ~10^-30 | dead end |

### Why the horizon approaches fail

All five sub-ideas (a)-(e) share a structural problem: they attempt
to fix R using only the interplay between l_P and R, without
introducing a second independent scale. The resulting constraints
either force R ~ l_P (approaches b, c, d) or involve the
l_P/l_11 hierarchy which is too small (approach e). None can bridge
the 30-order-of-magnitude gap between l_P and R_obs.

The power-law fit R = l_P*(M_Pl/M_11)^alpha succeeds numerically
because M_11 encodes the SECOND scale (it depends on R through Vol_7).
But this is not a derivation -- it is a re-expression of the same
hierarchy in different variables. The exponent alpha = 5.279 is not
a simple fraction with clear physical origin, though 16/3 with a
Z2 factor comes within 1.7%.

### What would it take to derive R?

The framework currently has:

1. M_Pl^2 = M_11^9 * Vol_7(r_3, r_2, R) -- Planck mass constraint
2. r_3^2 = n_1/(2*c*R) -- flux stabilization (F-flat condition)
3. rho_Lambda = Delta_N * 3*zeta(5)/(64*pi^6*R^4) -- Casimir dark energy

Equations (1) and (2) together fix R ~ l_P (the GUT scale cancels).
Equation (3) is the one that actually determines R = 10.1 um, but
it uses rho_Lambda as input.

To make R (and hence rho_Lambda) a *prediction*, one needs a
**third geometric/topological constraint** that is independent of
(1) and (2) and that introduces the large hierarchy R/l_P ~ 10^30.
The candidate constraints explored here do not provide this.

The most promising direction remains Idea 1 from Prompt 29: the
observation that flux + Planck determines R ~ l_P suggests that the
*missing ingredient* is whatever physics lifts R from l_P to 10 um.
The Casimir vacuum energy does this, but only if rho_Lambda is
given. A self-consistent stabilization mechanism (where the Casimir
potential has a minimum at finite R) would close the system without
external input -- but the current Casimir potential V ~ 1/R^4 is
monotonically decreasing and has no minimum. A balancing term
(from curvature, flux backreaction, or higher-loop corrections)
would be needed.

---

*Filed as 30b. The five sub-ideas (a)-(e) are dead ends. The
power-law alpha = 16/3 with Z2 correction is a 1.7% numerological
hit worth noting but not a derivation. The core conclusion stands:
R is not yet derivable from geometry and flux alone; a stabilizing
potential with a minimum at R ~ 10 um is the missing piece.*
