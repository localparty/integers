# Appendix I — Cassini Fifth-Force Consistency

> This appendix demonstrates that the scalar field (dilaton) arising from the
> Kaluza-Klein reduction of the 5D metric is consistent with the Cassini
> spacecraft's precision measurement of the post-Newtonian parameter gamma.
> The key result is that the Casimir-stabilized e-circle gives the scalar a
> mass of order 10 meV, suppressing its effects by a factor of exp(-7 x 10^15)
> at solar-system scales. No fine-tuning or screening mechanism is required.

---

## I.1 The Problem

The Kaluza-Klein reduction of the 5D Einstein action (Appendix D) decomposes
the 5D metric into a 4D metric g_mu_nu, a gauge field A_mu (identified with
the electromagnetic potential), and a scalar field phi(x) that encodes the
local circumference of the e-circle:

    g_AB^(5D) --> { g_mu_nu(x),  A_mu(x),  phi(x) }

The scalar phi(x) measures deviations of the extra-dimensional radius from
its stabilized value R_0. In the 4D effective theory it couples universally
to matter through the 4D gravitational sector — it is a Brans-Dicke-type
scalar. Any such scalar mediates a "fifth force" between massive bodies.

The best constraint on long-range scalar-mediated modifications of gravity
comes from the Cassini spacecraft's measurement of the Shapiro time delay
during its 2002 solar conjunction (Bertotti, Iess, & Tortora, Nature 425,
374, 2003). The result constrains the parameterized post-Newtonian (PPN)
parameter gamma:

    |gamma - 1| < 2.3 x 10^{-5}     (2 sigma)

A massless scalar field with gravitational-strength coupling predicts

    gamma = (1 + omega) / (2 + omega)

where omega is the Brans-Dicke parameter. For the canonical KK reduction,
omega = 0, giving

    gamma_BD = 1/2

This is excluded by more than four orders of magnitude. The question is
therefore unavoidable: does the scalar field in our framework violate the
Cassini bound?

The answer is no, and the reason is simple: the scalar is not massless.

---

## I.2 The Massive Scalar

The Casimir stabilization of the e-circle (Section 6.6, Appendix F) fixes
the extra-dimensional radius at a value R_0 determined by the balance between
Casimir energy and the curvature of the compactification potential. Small
fluctuations of the radius about R_0 define the physical scalar field:

    phi(x) = R(x) - R_0

These fluctuations see a potential with a nonzero second derivative — the
scalar acquires a mass:

    m_phi^2 = V''(R_0)

For the Casimir-stabilized e-circle with circumference L ~ 130 um
(R_0 = L / 2pi ~ 21 um), the characteristic energy scale is:

    m_phi = hbar c / R_0

Numerically:

    m_phi = (1.973 x 10^{-7} eV m) / (2.1 x 10^{-5} m)
          = 9.4 x 10^{-3} eV
          = 9.4 meV

The corresponding Compton wavelength — which sets the Yukawa range of the
scalar-mediated force — is:

    lambda_phi = hbar / (m_phi c) = R_0 ~ 21 um

This is the critical result. The scalar does not propagate over macroscopic
distances. Its influence is confined to a Yukawa envelope of range ~21 um,
identical to the compactification radius. At distances large compared to
lambda_phi, the scalar decouples exponentially.

---

## I.3 Solar-System Suppression

The Cassini measurement probes gravitational physics at length scales of
order the Earth-Sun distance:

    r_AU = 1 AU = 1.496 x 10^{11} m

The scalar-mediated force between two masses at separation r takes the
Yukawa form:

    F_scalar(r) = -alpha_phi (G M m / r^2) exp(-r / lambda_phi)

where alpha_phi is a dimensionless coupling of order unity (for a KK scalar,
alpha_phi ~ 1). The ratio of the scalar force to the Newtonian force is:

    F_scalar / F_Newton = alpha_phi exp(-r / lambda_phi)

At r = 1 AU:

    r / lambda_phi = (1.496 x 10^{11} m) / (2.1 x 10^{-5} m)
                   = 7.1 x 10^{15}

Therefore:

    F_scalar / F_Newton = alpha_phi x exp(-7.1 x 10^{15})

This number is not merely small — it is identically zero for all practical
purposes. To appreciate the suppression: exp(-7.1 x 10^{15}) is a number
with approximately 3.1 x 10^{15} zeros after the decimal point before the
first nonzero digit. No measurement, present or conceivable, could detect
a deviation of this magnitude.

The effective PPN parameter gamma is:

    gamma_eff = 1 - 2 alpha_phi^2 / (1 + alpha_phi^2) x exp(-r / lambda_phi)
              = 1 + O(exp(-7.1 x 10^{15}))
              = 1    (to all measurable precision)

The Cassini bound |gamma - 1| < 2.3 x 10^{-5} is satisfied by a margin of
ten trillion orders of magnitude.

---

## I.4 Where the Scalar IS Relevant

The scalar field is not inert — it is merely short-ranged. At separations
comparable to the Yukawa range:

    r ~ lambda_phi ~ 21 um

the scalar force is unsuppressed and contributes a Yukawa modification to
gravity with coupling strength of order unity. This is precisely the regime
probed by the submillimeter gravity experiments discussed in Appendix H,
Prediction 1.

The scalar therefore plays a dual role in the framework:

1. **At r >> lambda_phi (solar-system scales):** The scalar decouples
   exponentially. Gravity is described by pure 4D GR to extraordinary
   precision. All solar-system tests — Shapiro delay, perihelion precession,
   Nordtvedt effect, lunar laser ranging — are satisfied trivially.

2. **At r ~ lambda_phi (submillimeter scales):** The scalar contributes a
   detectable Yukawa correction. This is the regime of Prediction 1 and
   the target of current short-range gravity experiments (Adelberger et al.,
   Lee et al.).

This separation of scales is not arranged by hand. It is a direct
consequence of the Casimir stabilization: the same mechanism that fixes the
e-circle radius and produces the observed dark energy density (Section 6.6)
also determines the scalar mass. The consistency is automatic.

---

## I.5 Comparison with Other Scalar-Tensor Theories

The following table compares our framework's scalar with other well-known
theories containing gravitational scalars.

    +----------------------------+----------+-----------+-------------+---------------------+
    | Theory                     | Scalar   | Solar     | Mechanism   | Status              |
    |                            | mass     | system    |             |                     |
    +----------------------------+----------+-----------+-------------+---------------------+
    | Brans-Dicke (omega ~ 1)    | 0        | gamma=1/2 | None        | Ruled out           |
    +----------------------------+----------+-----------+-------------+---------------------+
    | Brans-Dicke (omega > 40000)| 0        | gamma ~ 1 | Large omega | Viable but          |
    |                            |          |           |             | fine-tuned           |
    +----------------------------+----------+-----------+-------------+---------------------+
    | f(R) gravity               | Variable | gamma ~ 1 | Chameleon   | Viable with         |
    |                            |          |           | screening   | tuning              |
    +----------------------------+----------+-----------+-------------+---------------------+
    | String moduli              | Model-   | Model-    | Model-      | Model-dependent     |
    |                            | dep.     | dep.      | dep.        |                     |
    +----------------------------+----------+-----------+-------------+---------------------+
    | Large extra dimensions     | ~ 1/R    | Depends   | Yukawa      | Depends on R;       |
    | (ADD)                      |          | on R      | suppression | R > 44 um excluded  |
    +----------------------------+----------+-----------+-------------+---------------------+
    | This framework             | 9.4 meV  | gamma = 1 | Yukawa      | Trivially           |
    | (5D e-circle, Casimir-     | (= hbar  | to all    | suppression | consistent;         |
    | stabilized)                | c / R)   | precision | (natural)   | predictive at       |
    |                            |          |           |             | r ~ 21 um           |
    +----------------------------+----------+-----------+-------------+---------------------+

Key observations:

- **Brans-Dicke:** A massless scalar requires omega > 40,000 to satisfy
  Cassini. This is a fine-tuning problem — nothing in the theory explains
  why omega should be so large.

- **f(R) gravity:** The scalar (scalaron) is effectively massless in vacuum
  but acquires an environment-dependent mass through the chameleon mechanism.
  This is a viable but elaborate screening construction that requires careful
  tuning of the f(R) function.

- **String moduli:** Generically produce massless or very light scalars.
  Stabilizing them (e.g., via flux compactification in the KKLT scenario)
  is one of the central challenges of string phenomenology. The moduli
  problem is a major open issue.

- **ADD (large extra dimensions):** The scenario of Arkani-Hamed, Dimopoulos,
  and Dvali places the extra-dimensional radius at scales testable by
  submillimeter gravity experiments. Current bounds (Kapner et al. 2007)
  exclude modifications to gravity above ~44 um at 95% confidence. Our
  predicted scale of ~21 um lies below this bound.

- **This framework:** The scalar mass is set by the same Casimir
  stabilization that determines the dark energy density. There is no
  free parameter to tune. Solar-system consistency is a consequence, not
  a constraint.

---

## I.6 The Key Advantage: Naturally Massive Scalar

The central point of this appendix deserves emphasis. In most theories
with extra dimensions or gravitational scalars, consistency with solar-
system tests requires one of the following:

1. **Fine-tuning a coupling constant** (Brans-Dicke with large omega).
2. **Invoking a screening mechanism** (chameleon, symmetron, Vainshtein).
3. **Assuming moduli stabilization** from unspecified UV physics (string
   compactifications).

Our framework requires none of these. The scalar field acquires its mass
from the same Casimir energy that:

- Stabilizes the e-circle (preventing decompactification),
- Predicts the dark energy density within observational bounds (Section 6.6),
- Determines the scale of submillimeter gravity modifications (Appendix H).

The mass is not an additional input. It is a derived quantity:

    m_phi = hbar c / R_0   where R_0 is fixed by Lambda_obs

Given the observed dark energy density Lambda_obs ~ 10^{-122} M_Pl^4, the
Casimir calculation yields R_0 ~ 21 um, which gives m_phi ~ 9.4 meV, which
gives a Yukawa range of ~21 um, which is exponentially smaller than any
solar-system scale. The chain of reasoning is:

    Lambda_obs --> R_0 --> m_phi --> lambda_phi << 1 AU --> gamma = 1

Every link is determined. There is no freedom to adjust. The framework
either passes the Cassini test or it does not — and it passes, by an
absurd margin.

---

## I.7 Formal Derivation of gamma_eff

For completeness, we sketch the derivation of the effective PPN parameter
in the presence of a massive scalar.

Starting from the 4D effective action after KK reduction (Appendix D):

    S = integral d^4x sqrt(-g) [ (1/16piG) R - (1/2)(d phi)^2
        - (1/2) m_phi^2 phi^2 + L_matter(g_mu_nu, phi) ]

The linearized field equations around flat space (g_mu_nu = eta_mu_nu + h_mu_nu,
phi = phi_0 + delta_phi) give, for a static point source of mass M:

    h_00 = 2GM/r + 2 alpha_phi^2 (GM/r) exp(-m_phi r)
    h_ij = delta_ij [ 2GM/r - 2 alpha_phi^2 (GM/r) exp(-m_phi r) ]

where alpha_phi characterizes the scalar-matter coupling strength
(alpha_phi ~ 1 for a KK scalar).

The PPN parameter gamma is defined by the ratio of spatial curvature to
time curvature in the metric of a point mass:

    gamma = - h_ij / (delta_ij h_00)

For a massless scalar (m_phi = 0):

    gamma = (1 - alpha_phi^2) / (1 + alpha_phi^2) = 1/2   (alpha_phi = 1)

For a massive scalar at r >> 1/m_phi:

    gamma_eff = [1 - alpha_phi^2 exp(-m_phi r)] / [1 + alpha_phi^2 exp(-m_phi r)]
              --> 1   as   m_phi r --> infinity

At r = 1 AU:

    m_phi r = r / lambda_phi = 7.1 x 10^{15}

and gamma_eff = 1 to all digits that could ever be measured.

---

## I.8 Additional Solar-System Tests

The Cassini bound is the tightest constraint on gamma, but it is not the
only solar-system test. We briefly confirm consistency with other tests.

**Perihelion precession of Mercury.** The anomalous precession depends on
the PPN parameters beta and gamma. A massive scalar with m_phi r >> 1
contributes zero correction to both. The framework predicts the standard
GR value of 42.98 arcsec/century.

**Nordtvedt effect.** Lunar laser ranging constrains violations of the
strong equivalence principle via the Nordtvedt parameter eta = 4(beta - 1)
- (gamma - 1). With gamma = beta = 1, eta = 0 identically.

**Gravitational redshift.** Tested by Gravity Probe A and atomic clock
comparisons. The scalar does not modify the redshift at distances r >> lambda_phi.

**Frame dragging.** Measured by Gravity Probe B and LAGEOS/LARES. These
probe the gravitomagnetic sector, which is controlled by the vector part
of the KK decomposition (the gauge field A_mu), not the scalar. The scalar
mass is irrelevant here.

In every case, the exponential suppression exp(-m_phi r) renders the scalar
undetectable at solar-system scales. The framework is consistent with the
full suite of precision gravitational tests.

---

## I.9 References

1. B. Bertotti, L. Iess, and P. Tortora, "A test of general relativity
   using radio links with the Cassini spacecraft," Nature **425**, 374
   (2003).

2. C. M. Will, "The confrontation between general relativity and
   experiment," Living Rev. Rel. **17**, 4 (2014). [arXiv:1403.7377]

3. E. G. Adelberger, B. R. Heckel, and A. E. Nelson, "Tests of the
   gravitational inverse-square law," Ann. Rev. Nucl. Part. Sci. **53**,
   77 (2003).

4. E. G. Adelberger et al., "Torsion balance experiments: A low-energy
   frontier of particle physics," Prog. Part. Nucl. Phys. **62**, 102
   (2009).

5. D. J. Kapner et al., "Tests of the gravitational inverse-square law
   below the dark-energy length scale," Phys. Rev. Lett. **98**, 021101
   (2007).

6. T. Damour and A. M. Polyakov, "The string dilaton and a least coupling
   principle," Nucl. Phys. B **423**, 532 (1994). [arXiv:hep-th/9401069]

7. J. Khoury and A. Weltman, "Chameleon fields: Awaiting surprises for
   tests of gravity in space," Phys. Rev. Lett. **93**, 171104 (2004).
   [arXiv:astro-ph/0309300]

---

*This appendix confirms that the 5D e-circle framework is trivially
consistent with the most precise solar-system test of gravity. The scalar
field is naturally massive, with a Yukawa range of ~21 um set by the
Casimir stabilization. At solar-system scales, its effects are suppressed
by a factor of exp(-7 x 10^{15}), which is zero to any conceivable
measurement precision. The framework passes the Cassini test — and every
other solar-system test — without fine-tuning, screening mechanisms, or
additional assumptions.*
