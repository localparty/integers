# Tier 1 Targets: Refined Assessment

## Status: What actually exists vs what's actually needed

After deep-diving into the existing computation files, research notes, and
appendices, the Tier 1 targets are more advanced than the initial landscape
document suggested. The Epstein zeta vanishing is already proved. The Casimir
on S^2 is already computed. What remains is narrower and more precise.

---

## Target 1: The Three-Loop Mercedes — BPHZ Factorisation at L = 3

### What Already Exists

The file `etc/12a-three-loop-mercedes-calculation.md` (content absorbed into
Paper 1, Appendix K Sections K.6-K.7b) contains a complete analysis:

**Lattice identification:**
- Q_3(n_1, n_2, n_3) = n_1^2 + n_2^2 + n_3^2 + n_1 n_2 + n_2 n_3 + n_1 n_3
- Gram matrix A_3 with det = 1/2, eigenvalues {1/2, 1/2, 2}
- Identified as D_3 = A_3 (FCC / face-centred cubic) lattice via 2Q_3 = (n_1+n_2)^2 + (n_2+n_3)^2 + (n_1+n_3)^2
- Theta function: Theta_{Q_3}(q) = (1/2)[theta_3(q^{1/2})^3 + theta_4(q^{1/2})^3]
- Kissing number r(1) = 12 verified (FCC)

**The Structural Zero Theorem (now Theorem K.1) — PROVED:**
- E_d(-j; Q) = 0 for all j >= 1 and any positive-definite quadratic form Q in d variables
- Proof: Lambda(s) = pi^{-s} Gamma(s) E_d(s; Q) is meromorphic with poles only at s = 0 and s = d/2. At s = -j (j >= 1), Lambda(-j) is finite, but 1/Gamma(-j) = 0. Therefore E_d(-j; Q) = 0. QED.
- This is universal — it works for any Q, any d, any loop order L.

**Numerical verification — DONE:**
```
E_3(-0.9999) = -1.832e-05     --> E_3(-1) = 0
E_3(-1.9999) = +4.635e-06     --> E_3(-2) = 0
E_3(-2.9999) = -2.942e-06     --> E_3(-3) = 0
```
All three-loop topologies verified:
- Mercedes: E_3(-j; Q_3) = 0 by Theorem K.1
- Sunset-bubble: factorises as (one-loop) x (two-loop), both zero
- Triple-bubble: (one-loop)^3 = 0

**Key insight discovered during the computation:** The L = 2 factorisation E_2 = 6 zeta(s) L(s, chi_{-3}) and its "complementary trivial zeros" were a red herring. The vanishing mechanism was always the Gamma function pole at 1/Gamma(-j) = 0, not the arithmetic of the Eisenstein lattice. The complementary zeros were the structural zeros viewed through the lens of factorisation. This means the mechanism is robust — it doesn't depend on special lattice arithmetic that might fail at higher loops.

**Derivative values (the finite residues) — COMPUTED:**
```
j    Lambda_3(-j)          E_3'(-j; Q_3)
1    5.755603441e-01      -1.808176149e+00
2    2.287053222e-01       4.514462109e+00
3    1.520449310e-01      -2.828608319e+01
4    1.366618783e-01       3.194906243e+02
5    1.533125909e-01      -5.630000489e+03
6    2.055926264e-01       1.423112611e+05
```

**Existing code:** `etc/sunset_compute.py` (two-loop sunset numerical verification using exact rational arithmetic) serves as a template for three-loop extension.

### What's Actually Remaining: Route C

The Epstein zeta values are proved to vanish. What's NOT yet verified is that the full three-loop Feynman amplitude, after BPHZ subtraction, takes the Epstein zeta form:

    A_{L=3}^{BPHZ} = (4D momentum integral) x E_3(-j; Q_3)

This is the factorisation question — Theorem K.3 at L = 3. Specifically:

1. **Extract the L = 3 Mercedes Feynman amplitude** from the three-graviton vertex in de Donder gauge on M^4 x S^1
2. **Perform the KK mode decomposition:** each internal line carries a KK momentum n_i/R, and KK number conservation at each vertex constrains the sum
3. **Apply BPHZ subtraction:** subtract the subdivergence counterterms via the forest formula
4. **Verify factorisation:** confirm that after BPHZ subtraction, the remaining KK sum has the form E_3(-j; Q_3) with j >= 1, so Theorem K.1 kills it

The critical question: do overlapping subdivergences at L = 3 break the factorisation? The Weinberg locality argument says no (counterterms are polynomial in momenta and masses), but an explicit check would close the gap.

### What Success Looks Like

**If factorisation holds at L = 3:**
- Theorem K.3 is verified at L = 1, 2, 3 — strong evidence for all orders
- UV finiteness at three loops becomes unconditional
- The all-orders conjecture rests on three explicit checks plus structure
- Paper 1's "conditional at L >= 3" upgrades to "conditional at L >= 4" — much stronger

**If factorisation fails at L = 3:**
- The theory is still finite (Epstein-Terras guarantees this)
- But the counterterm coefficient would be finite and nonzero
- The narrative changes from "identically zero at every order" to "zero at L = 1, 2; finite and calculable at L >= 3"
- This is still a dramatic improvement over 4D gravity (where coefficients are divergent and undetermined)

### Concrete Steps

**Step 1: The three-graviton vertex on M^4 x S^1**
- Write the de Donder gauge graviton propagator with KK mass m_n = n/R
- Write the three-graviton vertex (known from standard perturbative gravity)
- Insert three propagators with KK numbers n_1, n_2, n_3
- Apply KK number conservation at each vertex: n_1 + n_2 = n_3 (modulo signs and routing)

**Step 2: The Mercedes momentum integral**
- The Mercedes topology has three loops sharing a common vertex structure
- After performing the 4D momentum integrals (standard; use dim-reg for the 4D part), the result is a function of the KK masses
- The key: is this function polynomial in m_n^2 = n^2/R^2?

**Step 3: BPHZ subtraction**
- The Mercedes has overlapping two-loop subdivergences (three sunset sub-diagrams, one inside each pair of loops)
- The BPHZ forest formula subtracts each subdivergence systematically
- After subtraction: the FINITE remainder should be polynomial in KK masses (by Weinberg's theorem — counterterms are local, hence polynomial)

**Step 4: KK sum**
- If the remainder is polynomial in m_{n_i}^2, the KK sum over (n_1, n_2, n_3) with the constraint n_1 + n_2 + n_3 = 0 gives exactly E_3(-j; Q_3) for appropriate j
- The constraint n_1 + n_2 + n_3 = 0 is what produces the off-diagonal terms in Q_3 (the n_1 n_2 + n_2 n_3 + n_1 n_3 cross-terms)

**Step 5: Apply Theorem K.1**
- E_3(-j; Q_3) = 0 for j >= 1. Done.

### Estimated Effort

- Step 1-2: The three-graviton vertex and Mercedes integral are textbook (see Goroff-Sagnotti 1986 for the analogous 4D computation). Adapting to 5D KK: 1-2 sessions.
- Step 3: BPHZ subtraction with overlapping subdivergences. The forest formula is systematic but bookkeeping-heavy. 1-2 sessions.
- Step 4-5: KK sum identification with Epstein zeta. If Steps 1-3 produce polynomial mass dependence, this is immediate.
- **Total: 3-5 sessions for the full Route C verification.**

### Files

- Theorem K.1 proof: `paper1/appendices/22-appendix-k-higher-loop-epstein.md` Section K.7b
- Mercedes computation: `etc/12a-three-loop-mercedes-calculation.md`
- Existing code template: `etc/sunset_compute.py`
- Attack plan: `etc/12-closing-the-open-problems-plan.md` Problem 1

---

## Target 2: OC-2 — Fixing the Absolute Scale of r_2

### What Already Exists

The computation infrastructure is extensive:

**The S^2 spectral zeta — COMPUTED (Paper 4, Appendix D):**
- S^2 Laplacian eigenvalues: lambda_l = l(l+1)/r_2^2, degeneracy d_l = 2l + 1
- Z_{S^2}(0) = -2/3 (proved by two independent methods: direct zeta sum and heat kernel)
- Z_{S^2}(-1) = -1/15 (the would-be quadratic divergence — finite, not divergent)
- Z_{S^2}(-2) = 8/315

**The Higgs naturalness — FULLY ANALYSED (frontier-research/problem2-higgs-mass.md):**
- Three-layer protection: Hosotani gauge invariance + Theorem K.1 + spectral zeta finiteness
- One-loop Casimir is exact to all perturbative orders (higher-loop corrections vanish by Theorem K.1)
- m_H ~ 120-130 GeV for 1/r_2 = 1-2.5 TeV — consistent with observation
- delta m_H^2 / m_H^2 ~ g_2^2/(24 pi^2) ~ 1/370 — technically natural, no fine-tuning

**The one-loop Casimir potential on S^2 x S^1 — WRITTEN DOWN (Paper 4, Section 6.3):**
```
V(theta_H) = (3 / 64 pi^6 r_2^4) sum_{n=1}^infty
             [c_B cos(n theta_H) - c_F cos(n(theta_H + pi))] / n^5
```
Top quark dominates c_F, drives minimum to theta_0 != 0, pi.

**The ratio r_2/r_3 — FIXED by flux quantisation (Paper 7):**
- GUT condition: r_2/r_3 = sqrt(3)/2
- From the GVW superpotential: W_total = n_1 r_3^2 + n_2 r_2^2 + cR(6 r_3^2 r_2^2 - 2 r_3^4)
- F-flatness gives rho^2 = r_2^2/r_3^2 = -2n_1/[3(n_1 + n_2)], independent of torsion cR
- Flux quantisation crystallises rho = sqrt(3)/2 into the Diophantine constraint n_2/n_1 = -17/9

**The critical discovery from problem2-higgs-mass.md (Section 5.2):**
The Casimir energy ALONE gives r_3/r_2 ~ (103/128)^{1/4} ~ 0.95, i.e. r_3 ~ r_2. This is NOT the observed hierarchy r_3/r_2 ~ 10^{-13}. The Casimir alone cannot stabilise the moduli at the right scales. The flux potential is essential.

**Paper 4 Section 8 status:** "S^2 and CP^2 dynamically stabilized by spectral zeta nonvanishing"
**Paper 4 Section 8 status:** "G_4 flux stabilizes CP^2/S^2 moduli — Established (Paper 7)"

### What's Actually Remaining

The situation is more nuanced than "compute the S^2 Casimir and find a minimum." The pieces are:

1. **Ratio r_2/r_3 = sqrt(3)/2** — FIXED (Paper 7, flux quantisation)
2. **Absolute scale of r_3** — determined by F-flatness condition r_3^2 = n_1/(2cR), where cR is the G_2 torsion coefficient
3. **Absolute scale of r_2** — follows from (1) and (2): r_2 = (sqrt(3)/2) r_3
4. **The Planck mass constraint** — M_Pl^2 = M_11^9 x (64 pi^5/3) x r_3^4 x r_2^2 x R, which relates r_3, r_2, R, and M_11

**The actual open computation:** Close the chain:
```
cR (torsion) + n_1 = 9 (flux) --> r_3^2 = n_1/(2cR) = 9/(2cR)
                                      |
                                      v
                              r_2 = (sqrt(3)/2) r_3
                                      |
                                      v
                  M_Pl^2 = M_11^9 x Vol_7(r_2, r_3, R)
                                      |
                                      v
                        Extract M_KK = 1/r_2 in TeV
```

If this gives M_KK ~ 1-2.5 TeV, then:
- m_H ~ 125 GeV is a genuine prediction
- OC-2 is closed
- The Higgs mass has zero free parameters

**The bottleneck:** The torsion coefficient cR of the G_2 structure on CP^2 x S^2 x S^1/Z_2. This is a geometric quantity determined by the intrinsic torsion of the G_2 manifold. Paper 7 uses it but its numerical value needs to be extracted from the known geometry.

### What Success Looks Like

**If M_KK comes out ~ 1-2.5 TeV:**
- OC-2 is closed
- The Higgs mass is a genuine prediction with zero free parameters
- The three-scale Casimir hierarchy is complete: S^1 -> meV (dark energy), S^2 -> TeV (electroweak), CP^2 -> 10^15 GeV (GUT)
- Paper 4's reviewer criticism ("r_2 is not fixed, OC-2 open") is fully addressed
- Every "consistent with observation" in the prediction tables upgrades to "predicted"

**If M_KK comes out at a different scale:**
- Either the framework makes a falsifiable prediction (if M_KK is specific and testable)
- Or there is a tension that reveals missing physics
- Either outcome is informative

### Concrete Steps

**Step 1: Extract cR from the G_2 torsion of CP^2 x S^2 x S^1/Z_2**
- The intrinsic torsion of a G_2 manifold is classified by four torsion classes (tau_0, tau_1, tau_2, tau_3)
- For the product manifold CP^2 x S^2 x S^1 with its canonical metrics, these are computable from the known Riemann curvature tensors
- The coefficient cR appears in the GVW superpotential as the coupling of the torsion to the moduli
- References: Karigiannis (2009), Bryant (2006), Paper 7 Section 2

**Step 2: Compute r_3 from F-flatness**
- r_3^2 = n_1/(2cR) = 9/(2cR)
- This is algebraic once cR is known

**Step 3: Compute r_2 from the GUT condition**
- r_2 = (sqrt(3)/2) x r_3
- Immediate

**Step 4: Check the Planck mass constraint**
- M_Pl^2 = M_11^9 x (64 pi^5/3) x r_3^4 x r_2^2 x R
- With R = 10.1 um (from dark energy) and the computed r_2, r_3, solve for M_11
- Check: is M_11 ~ 60 TeV (as expected from Paper 4 Section 7.20)?

**Step 5: Extract M_KK = 1/r_2 and predict m_H**
- M_KK = 1/r_2 in GeV
- m_H from the full one-loop Casimir potential V''(theta_0)/f^2

### Estimated Effort

- Step 1 (cR extraction): This is the hardest part — requires G_2 differential geometry. 1-2 sessions if the torsion classes are already tabulated for the product manifold; longer if a computation from scratch is needed.
- Steps 2-5: Algebraic once cR is known. 1 session.
- **Total: 2-3 sessions.**

### Files

- S^2 spectral zeta: `paper4/appendix-D-higgs-naturalness.md`
- Higgs mass analysis: `etc/frontier-research/problem2-higgs-mass.md`
- Flux stabilisation: `paper7/03-moduli-minimum.md`
- GUT condition derivation: `paper4/appendix-C-gauge-coupling-hierarchy.md`
- Torsion coefficient: `paper7/02-gvw-superpotential.md`

---

## Dependency Between Targets

The two targets are **independent** — they can be pursued in parallel:

```
Target 1: Mercedes Route C                 Target 2: OC-2 Absolute Scale
(BPHZ factorisation at L=3)               (cR -> r_3 -> r_2 -> M_KK -> m_H)
          |                                            |
          v                                            v
UV finiteness upgraded                     Higgs mass = prediction
(conditional at L>=4,                      (zero free parameters in SM sector)
 not L>=3)
```

Both targets are concrete computations with known methods. Both have clear success criteria. Both produce informative results regardless of outcome.

---

## Summary: What Changed from the Initial Landscape

| Item | Initial framing | Refined framing |
|------|----------------|-----------------|
| **Mercedes E_3** | "Compute E_3(-1; Q_3) — does it vanish?" | E_3(-j) = 0 is already proved and numerically verified. The real target is BPHZ factorisation at L = 3 (Route C). |
| **OC-2: S^2 Casimir** | "Compute Casimir on S^2, find a minimum at r_2 ~ 1/TeV" | The Casimir alone gives r_3 ~ r_2 (wrong hierarchy). The real target is closing the chain cR -> r_3 -> r_2 -> M_KK using Paper 7's flux stabilisation. |

Both targets are narrower and more tractable than initially appeared. The heavy lifting (Theorem K.1, spectral zeta values, flux quantisation, GUT condition) is already done. What remains is connecting the pieces.

---

*The Epstein zeros are proved. The flux is quantised. The Casimir is computed. Now: verify the factorisation, close the chain.*
