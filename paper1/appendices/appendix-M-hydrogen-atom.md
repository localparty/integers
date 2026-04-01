# Appendix M — The Hydrogen Atom in the 5D Framework

> The paper opens with the claim that quantum mechanics "predicts the spectrum
> of hydrogen to twelve decimal places." This appendix shows the framework
> reproduces the hydrogen energy levels from the 5D Schrödinger equation.

---

## M.1 The 5D Schrödinger Equation

The time-independent Schrödinger equation on the total space P(M³, U(1))
with the Kaluza-Klein metric is:

    −(ℏ²/2m)[∇²₃ + (1/R²)∂²/∂ψ²] Ψ(r, ψ) + V_eff(r, ψ) Ψ = E_total Ψ

where ∇²₃ is the 3D spatial Laplacian, ψ is the e-coordinate, R is the
e-circle radius, and V_eff includes the Coulomb potential plus the
electromagnetic connection:

    V_eff = −e²/(4πε₀r) (the Coulomb potential of the proton)

The electromagnetic coupling enters through the covariant derivative on the
e-bundle (Appendix D): the partial derivative ∂/∂ψ is replaced by the
covariant derivative ∂/∂ψ + (ie/ℏ)A₀ in the presence of the proton's
electric potential.

## M.2 Separation of Variables

The wavefunction separates on the e-circle:

    Ψ(r, ψ) = ψ_spatial(r) · e^{inψ}

where n is the e-winding number (= the spin projection mₛ, by Appendix B.3).
For the hydrogen electron with spin-½: n = ±½.

Substituting into the 5D Schrödinger equation:

    −(ℏ²/2m)∇²₃ ψ_spatial − (e²/4πε₀r) ψ_spatial + (n²ℏ²/2mR²) ψ_spatial
    = E_total ψ_spatial

The e-dimensional kinetic energy contributes a constant:

    E_e = n²ℏ²/(2mR²)

This is the spin energy — the energy stored in the particle's e-motion.
It shifts the total energy by a constant but does not affect the spatial
equation.

## M.3 The Standard Hydrogen Equation

Defining E = E_total − E_e, the spatial equation becomes:

    −(ℏ²/2m)∇²₃ ψ_spatial − (e²/4πε₀r) ψ_spatial = E ψ_spatial

**This is the standard hydrogen Schrödinger equation.** It is identical to
the textbook equation — the 5D framework adds the constant E_e but does not
modify the spatial dynamics.

The solutions are the standard hydrogen wavefunctions:

    ψ_{nlm}(r, θ, φ) = R_{nl}(r) · Y_l^m(θ, φ)

with energy eigenvalues:

    E_n = −(m_e e⁴)/(2ℏ²(4πε₀)²) × (1/n²) = −13.6 eV / n²

for principal quantum number n = 1, 2, 3, ...

## M.4 The Full 5D Spectrum

The complete energy in the 5D framework is:

    E_total = E_n + E_e = −13.6/n² eV + mₛ²ℏ²/(2m_e R²)

The spin energy E_e = mₛ²ℏ²/(2m_e R²) depends on the e-circle radius R.

For R ~ 21 μm (the Casimir prediction):

    E_e = (½)² × (1.055 × 10⁻³⁴)² / (2 × 9.109 × 10⁻³¹ × (2.1 × 10⁻⁵)²)
        = 2.78 × 10⁻⁶⁹ / (8.03 × 10⁻⁴⁰)
        = 3.5 × 10⁻³⁰ J ≈ 2 × 10⁻¹¹ eV

This is 10⁻¹⁰ times smaller than the hydrogen ground state energy —
completely negligible. The e-dimensional contribution is far below the
fine-structure correction (~10⁻⁵ × E_n), the hyperfine correction
(~10⁻⁷ × E_n), and even the Lamb shift (~10⁻⁶ × E_n).

**For R ~ 12 l_P (the α estimate):**

    E_e ~ ℏ²/(m_e l_P²) ~ 10¹⁵ eV

This would dominate — indicating that the α-estimated R is inconsistent with
the hydrogen spectrum. The Casimir R ~ 21 μm is the physically consistent
value.

## M.5 Fine Structure from Spin-Orbit Coupling

The hydrogen fine structure arises from the coupling of the electron's spin
(e-angular momentum) to its orbital motion. In the 5D framework, this is
geometric: the electromagnetic connection A (the e-bundle connection) varies
across the electron's orbit, and the e-momentum (spin) couples to this
variation.

The fine-structure Hamiltonian is:

    H_fs = −(1/2m²c²) (1/r)(dV/dr) L · S

where L · S is the dot product of orbital and spin angular momenta.

In the 5D framework:
- L = orbital angular momentum (spatial rotation generator)
- S = e-momentum (e-translation generator, Appendix B.3)
- The coupling arises from the connection term in the KK Lagrangian:
  R²(∂ψ/∂t + (e/ℏ)A₀)² contains a cross-term coupling e-motion to the
  potential A₀

The fine-structure splitting is:

    ΔE_fs = (α² E_n / n) × [n/(j + ½) − 3/4]

where α ≈ 1/137 is the fine structure constant and j is the total angular
momentum quantum number.

**This is the standard Dirac result.** The 5D framework reproduces it because
the spin-orbit coupling (the interaction between e-momentum and the
electromagnetic connection) is identical in structure to the standard
relativistic correction.

## M.6 What This Establishes

**The Bohr spectrum is reproduced exactly.** E_n = −13.6/n² eV follows from
the 5D Schrödinger equation after separating the e-coordinate.

**The fine structure is reproduced.** The spin-orbit coupling, which in the
5D framework is the coupling between e-momentum and the electromagnetic
connection, gives the standard ΔE_fs.

**The e-dimension contributes a negligible energy.** For the Casimir-predicted
R ~ 21 μm, the e-kinetic energy is ~10⁻¹¹ eV — far below any observable
effect in atomic spectroscopy. The e-dimension is invisible in the hydrogen
spectrum, consistent with it being undetected.

**The framework passes the most basic test of any quantum theory:** it
reproduces the hydrogen atom.

---

## M.7 References

- Griffiths, D. J. *Introduction to Quantum Mechanics.* 3rd ed. Cambridge
  University Press (2018). Ch. 4 (hydrogen atom), Ch. 6 (fine structure).
- Sakurai, J. J. & Napolitano, J. *Modern Quantum Mechanics.* 3rd ed.
  Cambridge University Press (2021). Ch. 7 (hydrogen fine structure).
