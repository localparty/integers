## 8. Bekenstein-Hawking Entropy — Why S = A/4 in 5D


### 8.1 The Entropy from Entanglement

The Bekenstein-Hawking entropy measures the entanglement between the
black hole interior and exterior across the horizon (Bombelli et al.
1986, Srednicki 1993). In the 5D framework, this entanglement
includes the KK modes on the e-circle.

For `N_eff` field species, the entanglement entropy across a surface
of area `A` is (Srednicki 1993):

    S_ent = α × N_eff × A / ε²

where `α ∼ 1/(360π)` is a numerical coefficient and `ε` is the UV
cutoff. In the 5D framework, the UV cutoff is the Planck area:

    ε² = l_P²

The effective number of species includes the KK tower:

    N_eff = N_0 + Σ_{n=1}^{n_max} N_n × f(m_n/T_H)

where `f(m/T)` is the thermal suppression factor for modes heavier
than the Hawking temperature.

### 8.2 The Species Problem and Its Resolution

The naive entropy counting with all KK modes gives:

    S_naive = N_eff × α × A / l_P,bare²

which overshoots `S_BH = A/(4l_P²)` by a factor of `N_eff` — the
species problem (Susskind & Uglum 1994).

The resolution is standard: the Newton's constant `G` in the
Bekenstein-Hawking formula is the *renormalized* constant, which
already incorporates the contribution of all species (Jacobson 1994):

    1/G_ren = 1/G_bare + (loop contributions from all species)

The entanglement entropy of all species is:

    S = N_eff × α × A / l_P,bare²

But the physical Planck area `l_P,phys² = G_ren ℏ/c³` absorbs the
species factor through the renormalization of `G`:

    S = A / (4 l_P,phys²)

**The Bekenstein-Hawking entropy is recovered exactly** after
renormalization of Newton's constant.

### 8.3 The Geometric Interpretation

In the e-dimension framework, the black hole entropy has a
specific geometric meaning beyond the standard calculation:

**The entropy counts independent e-circle configurations on the
horizon surface.**

Each Planck-area cell on the horizon supports an e-circle with
`d_e = L/l_P` distinguishable positions. But these positions are not
independent — the e-coordinates of adjacent cells are correlated
through the e-conservation constraint. The Bekenstein-Hawking
entropy `S = A/(4l_P²)` counts the number of Planck cells — which,
after accounting for the e-circle correlations, is the number of
INDEPENDENT e-circle configurations.

The e-dimension provides the microstates. The conservation
constraint provides the correlation. The entropy counts the
independent degrees of freedom.

### 8.4 Why Area, Not Volume

The reason entropy scales with area rather than volume is now
transparent: **information is on the surface because the surface
is where the e-encoding happens.** Matter does not enter the
interior — the horizon grows to meet it (Section 4.2). All
information is surface information, encoded in the e-coordinates
of Planck pixels. Entropy counting surface e-states naturally
gives `S ∝ A`.

### 8.5 No Free Parameters

Unlike loop quantum gravity (which requires the Immirzi parameter
`γ`), the e-dimension entropy calculation has no free parameters.
The e-circle radius `R` is fixed by the Casimir dark energy
prediction (Paper 1, Section 6.6), and the entropy follows from
the standard entanglement entropy formula with renormalization of
`G` — a procedure that is independent of `R`.

---

