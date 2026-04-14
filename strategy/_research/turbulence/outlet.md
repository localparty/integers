# Turbulence / Kolmogorov K41 — Outlet Report

## 1. Official outlet

- **Scholarpedia (authoritative review):** http://www.scholarpedia.org/article/Turbulence
- **Original paper:** Kolmogorov, A. N. (1941). "The local structure of turbulence in incompressible viscous fluid for very large Reynolds numbers." *Dokl. Akad. Nauk SSSR* 30, 301–305. English: https://www.ams.jhu.edu/~eyink/Turbulence/classics/Kolmogorov41a.pdf
- **Related problem (Clay-prized):** Clay Navier-Stokes existence and smoothness: https://www.claymath.org/millennium/navier-stokes-equation/
- **Key monograph:** Frisch, U. (1995). *Turbulence: The Legacy of A. N. Kolmogorov*. Cambridge University Press.

**K41 itself is not a prized problem — it is a phenomenological theory/framework.** The associated rigorous problems (Onsager conjecture, K41 spectrum derivation from NS) straddle the Clay NS problem.

## 2. Problem statement

**K41 hypotheses (verbatim-ish, Kolmogorov 1941):**

Under the assumption of statistical homogeneity, isotropy, and infinite Reynolds number, the ensemble-averaged longitudinal velocity structure function satisfies
S_p(ℓ) = ⟨ (δu_∥(ℓ))^p ⟩ = C_p · (ε ℓ)^{p/3}
in the inertial range η ≪ ℓ ≪ L, where ε is the mean energy dissipation rate, η is the Kolmogorov dissipation scale, and L is the integral scale.

**Energy spectrum (Kolmogorov-Obukhov):** E(k) = C_K · ε^{2/3} · k^{-5/3}, C_K the Kolmogorov constant (≈ 1.5 experimentally).

**Two fundamental postulates (Frisch's rendering of K41):**
- **H1:** as viscosity ν → 0, the energy dissipation rate ε tends to a finite, non-vanishing limit.
- **H2:** statistical scale invariance holds in the inertial range.

**Open problem:** Rigorously derive K41 (or a corrected version) from the Navier–Stokes or Euler equations.

## 3. Prize

**No direct prize.** However, the *closely related* Clay Navier-Stokes Millennium Problem (US $1,000,000) covers existence/smoothness; K41 derivation is widely understood as a deeper question logically related to NS.

The Clay Mathematics Institute explicitly identifies "understanding turbulence" as a motivation for the NS problem, though the Clay statement itself is about regularity, not K41.

## 4. Publication expectation

Expected journals in descending prestige:

- **Annals of Mathematics** — regularity/singularity breakthroughs (e.g., Terry Tao's blowup conditional work).
- **Communications in Mathematical Physics (CMP)** — most rigorous turbulence/fluid math.
- **Inventiones Mathematicae**
- **Acta Mathematica**
- **Publications Mathématiques de l'IHES**
- **Journal of the AMS**
- **Duke Mathematical Journal**
- **Archive for Rational Mechanics and Analysis (ARMA)** — fluid PDE specialty.
- **Communications on Pure and Applied Mathematics (CPAM)**
- **Analysis & PDE**

Physics-facing results:
- *Physical Review Letters* (phenomenology)
- *Physical Review Fluids*
- *Journal of Fluid Mechanics*
- *Physica D*

## 5. Formulation variants

- **K41 (original, 1941):** structure-function scaling S_p(ℓ) ∝ ℓ^{p/3}; 4/5 law S_3(ℓ) = -(4/5) ε ℓ exact.
- **K62 (Kolmogorov 1962):** refined similarity hypothesis accounting for intermittency; log-normal correction.
- **Onsager conjecture (1949; proven):** weak Euler solutions with Hölder regularity < 1/3 may dissipate energy (anomalous dissipation). Proved by Isett (2018, *Annals Math.*); rigidity by Constantin-E-Titi (1994).
- **4/5 law (Kolmogorov):** ⟨(δu_∥)^3⟩ = -(4/5) ε ℓ — a rigorous consequence given K41 hypotheses.
- **Kraichnan direct cascade (2D):** enstrophy cascade, k^{-3} spectrum.
- **Intermittency corrections (multifractal):** Parisi–Frisch, She–Lévêque.
- **Rigorous K41 from NS:** OPEN.

## 6. Known partial results + named walls

**Proven:**
- **Onsager conjecture (flexible part):** Isett, P. (2018). "A proof of Onsager's conjecture." *Annals of Math.* 188, 871–963. — shows energy-dissipating Hölder-1/3 Euler solutions exist.
- **Rigidity half:** Constantin, E & Titi (1994) *CMP* — Hölder > 1/3 implies conservation.
- **Non-uniqueness (2019):** Buckmaster–Vicol non-uniqueness of NS solutions in critical spaces (*Annals of Math.*, 2019).
- **Bedrossian–Blumenthal–Punshon-Smith (2019+):** anomalous dissipation for stochastic NS; matches K41 4/5 law structure for stochastically-forced scalar advection.
- **Numerical verification:** DNS at Re up to ~10⁵; K41 scaling approximately confirmed with intermittency corrections.

**Named walls:**
- *Anomalous dissipation wall* — proving ε(ν) → ε₀ > 0 for deterministic NS as ν → 0 is open (even in 3D).
- *Regularity wall* — Clay NS problem; sits underneath everything.
- *Intermittency wall* — exact exponents ζ_p diverging from p/3 defy rigorous derivation.
- *Ensemble-mean wall* — statistical homogeneity is assumed; justifying it from generic initial data is open.

## 7. Key references

**Original:**
- Kolmogorov, A. N. (1941). *Dokl. Akad. Nauk SSSR* 30, 301–305 + 32, 16–18 (the 4/5 law).
- Onsager, L. (1949). "Statistical hydrodynamics." *Nuovo Cimento* 6, 279–287.

**Best modern surveys:**
- Frisch, U. (1995). *Turbulence: The Legacy of A. N. Kolmogorov*. Cambridge University Press. — canonical.
- Foias, C., Manley, O., Rosa, R., Temam, R. (2001). *Navier-Stokes Equations and Turbulence*. Cambridge.
- Eyink, G. L. (2018). *Scholarpedia* article on Turbulence.
- Tao, T. Blog posts on NS regularity and turbulence (terrytao.wordpress.com).

## Status: OPEN. No direct monetary prize; Clay NS $1M related but separate. Target journal: Annals of Math / CMP / CPAM.
