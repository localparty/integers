# Appendix R — Running of Coupling Constants Above the KK Scale

> Above the KK energy threshold `E_KK = ℏc/R ~ 10 meV`, the theory is
> effectively five-dimensional. Gauge coupling constants run differently in
> 5D than in 4D — power-law instead of logarithmic. This appendix computes
> the modified running, determines its effect on gauge coupling unification,
> and identifies an observational consequence.

---

## R.1 Coupling Constant Running in 4D

In four-dimensional quantum field theory, gauge couplings run logarithmically
with energy:

    1/αᵢ(μ) = 1/αᵢ(μ₀) + (bᵢ/2π) \ln(μ/μ₀)

where `αᵢ = gᵢ²/(4πℏc)` is the coupling of gauge group `i`, `μ` is the energy
scale, and `bᵢ` are the one-loop beta function coefficients:

    b₁ = −41/10     (U(1)_Y, with SM normalization)
    b₂ = +19/6      (SU(2)_L)
    b₃ = +7          (SU(3)_c)

The negative `b₁` means `α₁` increases with energy; the positive `b₂`, `b₃` mean
`α₂`, `α₃` decrease. The three couplings approach each other at high energies
but do NOT meet at a single point — they form a triangle at `E ~ 10¹⁴–10¹⁶`
GeV. This near-miss is one of the motivations for supersymmetry, which
modifies the `bᵢ` to produce exact unification at `~2 × 10¹⁶` GeV.

---

## R.2 The KK Threshold

### R.2.1 Below the KK Scale: Standard 4D Running

For energies `E < E_KK = ℏc/R ≈ 9.4 meV` (if `R ~ 21 μm`), the e-circle is
invisible — only the `n = 0` KK modes are accessible. The running is the
standard 4D logarithmic running with the SM beta coefficients.

Since `E_KK ~ 10 meV` is far below any particle physics scale (`m_e = 0.5 MeV`
is already `10⁵ ×` larger), **the KK threshold has no effect on the running
of gauge couplings at any experimentally accessible energy.** The standard
4D running is unmodified from the meV scale up to arbitrarily high energies
— as far as the coupling constants are concerned.

### R.2.2 Why the Low KK Scale Doesn't Matter

This may seem surprising: doesn't the extra dimension modify physics above
`E_KK`? The key is that the gauge couplings run due to QUANTUM LOOPS of
charged particles. The KK modes that open up above `E_KK` are GRAVITATIONAL
excitations (massive gravitons, massive vectors from the metric, massive
scalars from the dilaton). These do not carry Standard Model gauge charges
(they are gauge singlets) and therefore do NOT contribute to the running of
the SM gauge couplings.

The SM gauge fields (photon, W/Z, gluons) have `n = 0` as their KK number —
they are the zero modes of the 5D connection `Aμ`. Their KK excitations
(the massive gauge bosons at each KK level) DO carry gauge charge and DO
affect the running. But their mass is:

    m_n^{gauge} = n/R = n × 9.4 meV

These are incredibly light — well below the electron mass. Are they
populated in loops?

### R.2.3 The Gauge KK Modes

In the standard KK framework for gauge fields, the massive gauge KK modes
contribute to the running above their mass threshold. For `n = 1`:
`m₁ = 9.4 meV`. Above this energy, the first massive gauge KK mode enters
the loops.

The modified running above `E_KK` is:

    1/αᵢ(μ) = 1/αᵢ(E_KK) + (bᵢ/2π) \ln(μ/E_KK) + \sum_{n=1}^{μR/ℏc} (bᵢ^{(n)}/2π) \ln(μ/m_n)

where `bᵢ^{(n)}` is the beta function contribution from KK level `n`.

For each KK level, the massive gauge boson has the SAME gauge quantum numbers
as the zero mode (it's the same field, just with `n ≠ 0`). Therefore
`bᵢ^{(n)} = Δbᵢ` (a constant contribution per KK level).

The SUM over KK levels converts the logarithmic running into power-law
running:

    \sum_{n=1}^{N} \ln(μ/m_n) = \sum_{n=1}^{N} \ln(μR/(nℏc)) ≈ N \ln(μR/ℏc) − \ln(N!)
                               ≈ N \ln(μR/ℏc)  (for large N)

where `N = μR/(ℏc)` is the number of KK modes below energy `μ`.

Therefore above `E_KK`:

    1/αᵢ(μ) ≈ 1/αᵢ(E_KK) + (bᵢ/2π) \ln(μ/E_KK) + (Δbᵢ/2π) × (μR/ℏc) × \ln(μR/ℏc)

The second term (logarithmic) is the standard 4D running. The third term
(power-law, growing linearly with `μ`) is the KK correction — it becomes the
DOMINANT contribution above `E_KK`.

---

## R.3 Power-Law Unification

### R.3.1 The 5D Running

In the regime `E >> E_KK` (many KK modes populated), the running is
effectively 5-dimensional. The 5D gauge coupling has different dimensions
from the 4D coupling:

    g₅² = g₄² × L = g₄² × 2πR

The 5D beta function gives power-law running:

    1/α₅(μ) = 1/α₅(μ₀) + (b₅/2π) × (μ − μ₀) × L

where `b₅` is the 5D beta coefficient and the running is LINEAR in `μ` (not
logarithmic).

### R.3.2 The Unification Scale

In 4D, the three SM couplings nearly unify at `E ~ 10¹⁵` GeV. The power-law
KK correction ACCELERATES the running — the couplings converge faster.

However, for `R ~ 21 μm` (`E_KK ~ 10 meV`), the KK correction kicks in at
10 meV — an incredibly low scale. The power-law running from 10 meV to
`10¹⁵` GeV is:

    KK correction ∝ (10¹⁵ GeV / 10⁻² eV) × R/ℏc ~ 10¹⁷ × 10⁵ ~ 10²²

This is an ENORMOUS correction — much too large. The couplings would unify
(or diverge) at an energy far below the GUT scale.

### R.3.3 The Resolution: Gauge Fields Are 4D

The resolution is crucial and specific to the e-dimension framework:

**In the framework, the SM gauge fields live on the 4D base manifold, NOT
on the full 5D spacetime.**

The e-circle is the `U(1)` fiber of the electromagnetic bundle. The non-abelian
gauge fields (W/Z, gluons) — if they exist in the framework at all — would
require SEPARATE fibers (Appendix L). They do NOT propagate in the e-circle.

Therefore: **the SM gauge KK modes do not exist** (except for the photon's
KK tower, which is part of the electromagnetic sector). The W, Z, and gluon
fields have no KK excitations on the e-circle.

The photon's KK modes DO exist (they are the massive vector modes from the
KK decomposition of Appendix D). But these are massive photons, not W/Z/gluon
excitations. They affect only the electromagnetic coupling `α_EM`, not `α_weak`
or `α_strong`.

### R.3.4 The Modified EM Running

The electromagnetic coupling receives a KK correction:

    1/α_EM(μ) = 1/α_EM(E_KK) + (b_EM/2π) \ln(μ/E_KK) + (Δb_EM/2π) × (μR/ℏc)

For `μ ~ 100` GeV (the electroweak scale):

    KK correction ~ (Δb_EM/2π) × (100 GeV / 10⁻² eV) ~ Δb_EM × 10¹²

This is a potentially large correction. However, `Δb_EM` (the contribution of
each KK photon mode to the EM beta function) is:

    Δb_EM = 0 (massive vector KK modes are neutral!)

The photon's KK excitations are massive spin-1 bosons, but they are
electrically neutral — they are massive excitations of the electromagnetic
field itself. They couple to charged particles but, as neutral particles,
do not contribute to charge renormalization.

**The KK correction to `α_EM` running vanishes.** The massive photon KK modes
are neutral and do not renormalize the electric charge.

---

## R.4 The Result: Standard Running Is Preserved

### R.4.1 Summary

| Gauge coupling | KK modes on e-circle? | Running modified? |
|---------------|---------------------|------------------|
| `α_EM` (U(1)) | Massive neutral photons | **No** (neutral, don't renormalize charge) |
| `α_weak` (SU(2)) | **No** (W/Z not on e-circle) | **No** |
| `α_strong` (SU(3)) | **No** (gluons not on e-circle) | **No** |

**All three SM gauge coupling constants run with the standard 4D
logarithmic running.** The e-circle does not modify the gauge coupling
running at any energy scale.

This is simultaneously a strength and a limitation:

**Strength:** The framework is automatically consistent with all precision
electroweak measurements, which are based on the standard running of gauge
couplings. No fine-tuning is needed to avoid conflicts with LEP/LHC data.

**Limitation:** The framework does not address gauge coupling unification.
The near-miss of the three couplings at `~10¹⁵` GeV remains unexplained. If
the framework is extended to include the non-abelian forces (Appendix L),
the additional compact dimensions might modify the running at high energies
— but this is beyond the current scope.

### R.4.2 What DOES Run Differently

The one coupling that IS modified by the e-circle is the **gravitational
coupling** `G`. Above the KK scale, the effective gravitational coupling
becomes 5-dimensional:

    G_eff(r) = G₄ for r >> R (standard 4D gravity)
    G_eff(r) = G₅/r for r << R (5D gravity, enhanced)

At distances `r << R ~ 21 μm`, the gravitational force transitions from
`1/r²` (4D) to `1/r³` (5D). This is the Yukawa correction of Prediction 1
(Appendix H) — the most directly testable consequence of the framework.

---

## R.5 Implications for Grand Unification

### R.5.1 The Current State

The standard 4D running of SM couplings gives near-unification at
`E_GUT ~ 10¹⁵` GeV, with a small triangle of non-intersection. SUSY
provides exact unification at `~2 × 10¹⁶` GeV by modifying the beta
functions.

The e-dimension framework (single `U(1)` e-circle) does NOT modify the SM
running. It therefore does NOT address unification.

### R.5.2 The Extended Framework

If the non-abelian extension (Appendix L) is realized — with an 11D
geometry `M⁴ × M⁷` where `M⁷` includes the e-circle as one factor — the
running IS modified above the compactification scales of the additional
dimensions. In M-theory compactifications, gauge coupling unification can be
achieved (Witten 1996, Horava & Witten 1996), with the unification scale
related to the sizes of the compact dimensions.

This connects the e-dimension framework's unification program to the active
research program in string/M-theory phenomenology. The e-circle would be one
component of a larger compact space whose geometry determines ALL the gauge
couplings, including their unification.

---

## R.6 References

- Georgi, H., Quinn, H. R. & Weinberg, S. "Hierarchy of Interactions in
  Unified Gauge Theories." *Phys. Rev. Lett.* 33, 451–454 (1974). — Gauge
  coupling running and unification.
- Dienes, K. R., Dudas, E. & Gherghetta, T. "Grand Unification at
  Intermediate Mass Scales through Extra Dimensions." *Nucl. Phys. B* 537,
  47–108 (1999). — Power-law running in extra dimensions.
- Horava, P. & Witten, E. "Eleven-Dimensional Supergravity on a Manifold
  with Boundary." *Nucl. Phys. B* 475, 94–114 (1996). — Gauge coupling
  unification in M-theory.
- Langacker, P. "Grand Unified Theories and Proton Decay." *Phys. Reports*
  72, 185–385 (1981). — SM coupling running and near-unification.
