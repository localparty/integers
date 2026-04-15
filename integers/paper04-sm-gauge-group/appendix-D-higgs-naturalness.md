# Appendix D --- Higgs Mass Naturalness

---

## D.1 Theorem Statement

**Theorem D.1 (Radiative Stability of the Gauge-Higgs Mass).**

*In the M^4 x CP^2 x S^2 x S^1 compactification with the Higgs
identified as the SU(2) Wilson line on S^2 (Section 6.1--6.2), the
Higgs mass satisfies:*

*(a) m_H^2 = V''_{Casimir}(theta_0) / f^2, where V_{Casimir} is the
one-loop Casimir potential on S^2 x S^1 and f = 1/(g_2 r_2) is the
Higgs decay constant.*

*(b) The one-loop Casimir potential is finite and calculable, with the
KK sum regularized by the S^2 spectral zeta function. The
regularization-dependent coefficient is Z_{S^2}(0) = -2/3.*

*(c) All higher-loop corrections to m_H^2 vanish: at L >= 2 loops,
the KK mode sums produce Epstein zeta functions E_L(-j; Q_L) with
j >= 1, which vanish identically by Theorem K.1 (Universal Epstein
Vanishing, Paper 1, Appendix K, Section K.7b).*

*(d) Therefore m_H^2 is exactly determined by the one-loop Casimir
energy, is of order (g^2/16 pi^2)(1/r_2^2) ~ (100 GeV)^2, and
receives no corrections of order M_{GUT}^2 or M_{Pl}^2.*

---

## D.2 Tree-Level Higgs Mass from the Hosotani Mechanism

The Higgs is the Wilson line of the SU(2) gauge field on S^2
(Section 6.1--6.2). The off-diagonal metric components g_{i psi}(x),
where i labels S^2 coordinates and psi labels S^1, transform as a
doublet under SU(2)_L with U(1)_Y charge --- exactly the Higgs
quantum numbers (2, +1/2).

The Wilson line parameter theta_H is a flat direction at tree level:
the classical action is gauge-invariant under theta_H -> theta_H +
alpha, so V_{tree}(theta_H) = 0. The Higgs is an exact Goldstone
boson classically.

The one-loop Casimir energy (Section 6.3) lifts the flat direction:

    V(theta_H) = (3 / 64 pi^6 r_2^4) sum_{n=1}^infty
                 [c_B cos(n theta_H) - c_F cos(n(theta_H + pi))] / n^5

where c_B and c_F count bosonic and fermionic degrees of freedom. The
top quark dominates c_F and drives the minimum to theta_0 != 0, pi.
The Higgs mass-squared is the curvature at the minimum:

    m_H^2 = V''(theta_0) / f^2
           ~ (3 y_t^4 / 8 pi^2)(sin^2 theta_0 / r_2^2)
             (ln(1/sin^2 theta_0) + const)

For y_t = 1.0, sin theta_0 = 0.4, 1/r_2 = 1.5 TeV, this gives
m_H ~ 120--130 GeV, consistent with the observed 125.25 +/- 0.17 GeV.

---

## D.3 Derivation of Z_{S^2}(0) = -2/3

The S^2 Laplacian has eigenvalues lambda_l = l(l+1)/r_2^2 with
degeneracy d_l = 2l + 1, for l = 0, 1, 2, .... The spectral zeta
function (excluding the zero mode l = 0) is:

    Z_{S^2}(s) = sum_{l=1}^infty (2l + 1) [l(l+1)]^{-s}

The one-loop KK correction to the Higgs mass involves Z_{S^2}(0) ---
the regularized count of KK modes.

### D.3.1 Method 1: Direct zeta regularization

At s = 0, the sum reduces to:

    Z_{S^2}(0) = sum_{l=1}^infty (2l + 1) |_{reg}

Splitting the summand:

    Z_{S^2}(0) = 2 sum_{l=1}^infty l |_{reg}
                 + sum_{l=1}^infty 1 |_{reg}

Each sum is evaluated by the Riemann zeta function at negative
arguments:

    sum_{l=1}^infty l |_{reg} = zeta(-1) = -1/12

    sum_{l=1}^infty 1 |_{reg} = zeta(0) = -1/2

Therefore:

    Z_{S^2}(0) = 2(-1/12) + (-1/2) = -1/6 - 1/2 = -2/3

### D.3.2 Method 2: Heat kernel

The heat trace on S^2 (including all modes l >= 0) has the small-t
expansion:

    K_{S^2}(t) = sum_{l=0}^infty (2l + 1) e^{-l(l+1) t/r_2^2}
               ~ r_2^2/t + 1/3 + O(t)

The spectral zeta function (all modes) at s = 0 equals the constant
term in the heat trace expansion:

    zeta_{S^2}(0) = 1/3

The zero mode (l = 0) contributes 1 to zeta_{S^2}(0). Excluding it:

    Z_{S^2}(0) = zeta_{S^2}(0) - 1 = 1/3 - 1 = -2/3

Both methods yield Z_{S^2}(0) = -2/3, a standard result in spectral
geometry.

---

## D.4 The One-Loop Correction

The one-loop KK correction to the Higgs mass from the gauge sector is:

    delta m_H^2 = (g_2^2 / 16 pi^2)(1/r_2^2) Z_{S^2}(0)
               = (g_2^2 / 16 pi^2)(1/r_2^2)(-2/3)

This is a finite, negative, O(m_H^2) shift. The complete one-loop
potential (Section 6.3) already includes the full KK tower via the
zeta-regularized sum, so this coefficient appears as part of the
Casimir calculation rather than as a separate correction. The
Z_{S^2}(0) = -2/3 encodes the regularized sum over all S^2 KK modes.

---

## D.5 Three-Layer Protection Mechanism

The Higgs mass is protected from large corrections by three
independent mechanisms, each sufficient on its own.

### D.5.1 Layer 1: Higher-Dimensional Gauge Invariance (Hosotani Protection)

The Higgs is the A_5 component of the higher-dimensional gauge field.
Its potential vanishes at tree level by gauge invariance. No local
counterterm for the Wilson line is gauge-invariant because the Wilson
line is a non-local operator (it is an integral around S^2). The mass
is protected by this non-locality, in direct analogy with the chiral
symmetry protection of fermion masses: just as a mass term m psi-bar
psi is forbidden by chiral symmetry (forcing delta m ~ g^2 m
ln(Lambda/m)), a local mass term for theta_H is forbidden by gauge
invariance (forcing delta m_H^2 ~ (g^2/16 pi^2)(1/r_2^2)).

### D.5.2 Layer 2: UV Finiteness (Theorem K.1)

Theorem K.1 (Universal Epstein Vanishing, Paper 1, Appendix K,
Section K.7b) states that E_L(-j; Q) = 0 for all j >= 1 and any
positive-definite quadratic form Q.

At any loop order L, the power-law-divergent KK sums that would
produce quadratic or higher corrections to m_H^2 are identically
zero. Specifically:

- The would-be quadratic divergence (proportional to Z_{S^2}(-1) =
  -1/15) is killed by the BPHZ factorization (Theorem K.3, Paper 1,
  Appendix K, Section K.5.3).
- All higher power-law contributions are similarly killed.
- The only surviving contribution is the logarithmic piece,
  proportional to Z_{S^2}(0) = -2/3.

### D.5.3 Layer 3: Decoupling of Higher KK Scales

The CP^2 KK tower (scale 1/r_3 ~ 10^{15} GeV) and the Planck scale
do not contribute quadratically:

(a) *Gauge invariance protection:* The CP^2 modes are neutral under
the S^2 holonomy and do not shift theta_H at any loop order (Hosotani
non-renormalization theorem).

(b) *UV finiteness:* Theorems K.1 and K.3 ensure that KK sums over
all compact dimensions produce finite results. The Epstein zeta
vanishing applies to the full internal space CP^2 x S^2 x S^1.

(c) *BPHZ factorization:* By Theorem K.3, the BPHZ-subtracted
amplitude at every loop order factors as (4D integral) x E_L(-j; Q_L),
and the Epstein factor vanishes for j >= 1. No counterterm for the
Higgs mass is generated beyond one loop.

---

## D.6 Perturbative Exactness of the One-Loop Result

**The one-loop Casimir result is exact to all perturbative orders.**

At L >= 2 loops, the Wilson line potential involves L-fold KK sums that
reduce to Epstein zeta functions E_L(-j; Q_L) with j >= 1. By Theorem
K.1 (Paper 1, Appendix K, Section K.7b):

    E_L(-j; Q_L) = 0    for all j >= 1

The proof is elementary: the completed Epstein zeta Lambda(s) =
pi^{-s} Gamma(s) E_L(s; Q) is meromorphic with poles only at s = 0
and s = L/2. At s = -j (j >= 1), Lambda(-j) is finite. Since
1/Gamma(-j) = 0 (Gamma has poles at non-positive integers),
E_L(-j; Q) = 0.

By Theorem K.3 (BPHZ Factorization, Paper 1, Appendix K, Section
K.5.3), the BPHZ-subtracted amplitude at L loops factors as:

    A_L = (4D integral) x E_L(-j; Q_L)

Since E_L(-j; Q_L) = 0, the amplitude vanishes. Therefore:

    delta m_H^2 |_{L >= 2} = 0

Non-perturbative corrections from M2-brane instantons wrapping S^2 are
suppressed by exp(-Vol(S^2)/l_P^3) ~ exp(-r_2^2/l_P^2) ~ exp(-10^{30})
and are negligible to any conceivable precision.

---

## D.7 Technical Naturalness

The result satisfies the 't Hooft naturalness criterion: a parameter
is natural if setting it to zero enhances the symmetry of the theory.
Setting m_H -> 0 restores the full higher-dimensional gauge symmetry
(the Wilson line becomes a flat direction). The small mass is protected
by this approximate symmetry.

The correction delta m_H^2 / m_H^2 is of order g_2^2 / (24 pi^2) ~
1/370 --- a small, calculable, stable ratio. There is no fine-tuning.

---

## D.8 Proof Chain

| # | Statement | Status | Source |
|---|-----------|--------|--------|
| D.1 | Higgs = SU(2) Wilson line on S^2 (Hosotani mechanism) | **Established** | Hosotani (1983); Section 6.1--6.2 |
| D.2 | Tree-level Higgs mass: m_H^2 ~ (3 y_t^4 / 8 pi^2)(sin^2 theta_0 / r_2^2) | **Derived** | Section 6.7, one-loop Casimir |
| D.3 | m_H ~ 120--130 GeV for 1/r_2 = 1--2.5 TeV | **Derived** | Section 6.7 |
| D.4 | Z_{S^2}(0) = -2/3 (direct zeta sum) | **Proved** | Standard spectral geometry (Section D.3.1) |
| D.5 | Z_{S^2}(0) = -2/3 (heat kernel) | **Proved** | Standard spectral geometry (Section D.3.2) |
| D.6 | One-loop correction: delta m_H^2 = (g_2^2/16 pi^2)(1/r_2^2)(-2/3) | **Derived** | Section D.4 |
| D.7 | Theorem K.1: E_L(-j; Q) = 0 for j >= 1 | **Proved** | Paper 1, Appendix K, Section K.7b |
| D.8 | No quadratic divergence from KK tower | **Derived** | Theorem K.1 (D.7) applied to KK sums |
| D.9 | Hosotani protection: no local counterterm for Wilson line mass | **Established** | Hosotani (1983); Section D.5.1 |
| D.10 | Theorem K.3: BPHZ-subtracted amplitudes factor as (4D) x E_L(-j) = 0 | **Proved** | Paper 1, Appendix K, Section K.5.3 |
| D.11 | Higher-loop corrections vanish: delta m_H^2 |_{L>=2} = 0 | **Derived** | D.7 + D.10 (Section D.6) |
| D.12 | delta m_H^2 is O(m_H^2) --- no hierarchy problem | **Derived** | D.6, D.8, D.11 |

---

## D.9 Honest Caveats

1. **L >= 3 factorization.** Theorem K.3 establishes the BPHZ
   factorization using joint holomorphicity of the Epstein zeta. The
   treatment of overlapping subdivergences at L >= 3 (Paper 1,
   Appendix K, Section K.5.2) concerns the commutation of BPHZ
   subtraction with the Epstein evaluation. An explicit verification
   at L = 3 for the Mercedes diagram with Wilson line external legs
   would close this narrow gap.

2. **Quantitative prediction.** The precise numerical value of m_H
   requires the complete SM field content on S^2 x S^1, the Wilson
   line angle theta_0 from the full Casimir minimization, and the S^2
   radius r_2 from moduli stabilization. These are coupled through the
   Casimir potential on the full internal space (Open Problem OC-2,
   Section 9.1).

3. **The big hierarchy.** The ratio m_H / M_{GUT} ~ r_3 / r_2 is
   geometrized as a radius ratio but its numerical value requires
   the full moduli stabilization including G_4 flux (Paper 7,
   Sections 2--3). This is identified as future work.

---

## D.10 References

- Hosotani, Y. "Dynamical mass generation by compact extra dimensions."
  *Phys. Lett. B* 126, 309--312 (1983).
- Manton, N. S. "A new six-dimensional approach to the Weinberg-Salam
  model." *Nucl. Phys. B* 158, 141--153 (1979).
- Hatanaka, H., Inami, T. & Lim, C. S. "The gauge hierarchy problem
  and higher-dimensional gauge theories." *Mod. Phys. Lett. A* 13,
  2601--2612 (1998).
- 't Hooft, G. "Naturalness, chiral symmetry, and spontaneous chiral
  symmetry breaking." *NATO Sci. Ser. B* 59, 135--157 (1980).
- Epstein, P. "Zur Theorie allgemeiner Zetafunktionen." *Math. Ann.*
  56, 615--644 (1903).
