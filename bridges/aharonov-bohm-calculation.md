# Quantitative Aharonov-Bohm Effect from the 5D Framework

> **Status:** Working draft
> **Purpose:** Derive the Aharonov-Bohm phase shift quantitatively from the 5D
> path integral. Show that the phase shift Δφ = (e/ℏ)Φ emerges from the
> holonomy of the e-connection around the solenoid, and that the flux quantum
> Φ₀ = h/e is determined by the circumference of the e-circle.
> **Prerequisites:** Section 2 (framework), Section 4.1 (AB as e-topology),
> Bridge 2 (holonomy interpretation)
> **Feeds into:** Section 4.1 of the paper (turns qualitative into quantitative)

---

## 1. Purpose

Section 4.1 of the paper derives the Aharonov-Bohm effect qualitatively from
the topology of the e-bundle and presents the formal fiber-bundle statement
(Section 4.1.6). This document provides the explicit quantitative calculation:
starting from the 5D Lagrangian, computing the propagator for an electron
traversing both sides of a solenoid, and deriving the phase shift and
interference pattern.

---

## 2. Setup

### 2.1 The Aharonov-Bohm Geometry

An infinite solenoid of radius R lies along the z-axis, carrying magnetic
flux Φ = ∫ B · dA confined entirely to its interior.

**Inside the solenoid (r < R):** B ≠ 0.

**Outside the solenoid (r > R):** B = 0 everywhere. However, the vector
potential is non-zero:

    A = (Φ / 2πr) φ̂

(in cylindrical coordinates, where φ̂ is the azimuthal unit vector). This
satisfies ∇ × A = 0 outside the solenoid (consistent with B = 0) but
∮ A · dl = Φ for any loop encircling the solenoid.

### 2.2 The Electron Paths

An electron beam is split into two coherent paths that pass on opposite
sides of the solenoid and recombine at a detector:

- **Path 1 (γ₁):** passes to the LEFT of the solenoid
- **Path 2 (γ₂):** passes to the RIGHT of the solenoid

The closed loop γ = γ₁ − γ₂ encircles the solenoid once.

### 2.3 The 5D Picture

In the 5D framework, the solenoid is a topological defect in e-space
(Section 4.1.2 of the paper). The vector potential A is the CONNECTION on
the U(1) e-bundle — it describes how the e-coordinate is parallel-transported
as the electron moves through spacetime. The solenoid's flux creates a
non-trivial holonomy: the e-coordinate does not return to its starting
value after transport around a loop encircling the solenoid.

---

## 3. The 5D Lagrangian and E-Phase Evolution

### 3.1 The Lagrangian

For an electron of mass m and charge e on the total space P(M³, U(1)) with
the Kaluza-Klein metric, the Lagrangian is (Bridge 3, Section B3.2.1):

    L = ½m[ẋ² + R_e²(φ̇ + (e/ℏ)A · ẋ)²] − V(x)

where R_e is the radius of the e-circle and we have written the coupling
explicitly: the connection on the e-bundle is (e/ℏ)A, with e being the
electron charge and ℏ the reduced Planck constant.

### 3.2 The E-Momentum

The momentum conjugate to the e-coordinate is:

    pφ = ∂L/∂φ̇ = mR_e²(φ̇ + (e/ℏ)A · ẋ)

Since the Lagrangian does not depend on φ explicitly, pφ is conserved.

### 3.3 The E-Phase Along a Path

The total e-phase accumulated along a spatial path γ from point a to point b
is:

    φ(b) − φ(a) = ∫_γ φ̇ dt = ∫_γ [pφ/(mR_e²) − (e/ℏ)A · ẋ] dt

The first term (pφ/(mR_e²))·T is the FREE e-evolution — it depends on the
e-momentum and the transit time but is the SAME for both paths (since pφ is
conserved and both paths take the same transit time in the symmetric geometry).

The second term is the CONNECTION contribution — the parallel transport of
the e-coordinate by the gauge field:

    Δφ_connection[γ] = −(e/ℏ) ∫_γ A · dl

This is the term that differs between the two paths and produces the AB effect.

---

## 4. The Phase Shift Calculation

### 4.1 E-Phase Along Each Path

**Path 1 (left of solenoid):**

    Δφ₁ = (pφ/(mR_e²))T − (e/ℏ) ∫_{γ₁} A · dl

**Path 2 (right of solenoid):**

    Δφ₂ = (pφ/(mR_e²))T − (e/ℏ) ∫_{γ₂} A · dl

The free evolution terms are identical (same pφ, same T). They cancel in the
phase difference.

### 4.2 The Phase Difference

    Δφ = Δφ₁ − Δφ₂ = −(e/ℏ)[∫_{γ₁} A · dl − ∫_{γ₂} A · dl]

The quantity in brackets is the line integral of A around the closed loop
γ = γ₁ − γ₂ (traversing γ₁ forward and γ₂ backward):

    ∫_{γ₁} A · dl − ∫_{γ₂} A · dl = ∮_{γ₁ − γ₂} A · dl

By Stokes' theorem, this equals the flux of B through any surface bounded
by the loop:

    ∮_γ A · dl = ∫_Σ (∇ × A) · dA = ∫_Σ B · dA = Φ

Note: outside the solenoid, B = 0. But the surface Σ bounded by the loop
necessarily crosses the solenoid interior (where B ≠ 0). The flux through
Σ is the total solenoid flux Φ, regardless of the specific shape of the
loop or the surface.

Therefore:

    **Δφ = −(e/ℏ) · Φ**

This is the Aharonov-Bohm phase shift. Its magnitude is:

    |Δφ| = (e/ℏ) · Φ = (e/ℏ) · Φ

### 4.3 The 5D Interpretation

The phase shift is the HOLONOMY of the e-connection around the closed loop
encircling the solenoid:

    Hol_γ(A_e) = exp(i(e/ℏ)Φ)

In the e-dimension picture:
- The electron's e-coordinate is parallel-transported along each path by the
  connection (e/ℏ)A.
- Outside the solenoid, the connection is non-zero (A ≠ 0) even though the
  curvature vanishes (B = 0).
- The two paths accumulate different e-phases because the connection is not
  exact — its line integral around the solenoid is non-zero.
- The phase difference is a topological invariant: it depends only on the
  enclosed flux, not on the specific paths taken.

This is the same holonomy mechanism that produces the exchange phase in
Bridge 2. The solenoid AB effect and the spin-statistics exchange phase are
both holonomies of the e-connection — one around an external topological
defect, the other around the exchange loop in configuration space.

---

## 5. The Interference Pattern

### 5.1 Amplitude at the Detector

The wavefunction at the detector is the sum of amplitudes from both paths:

    ψ(y) = ψ₁(y) + ψ₂(y)

where ψ₁ and ψ₂ include both the spatial propagation phase and the AB
e-phase shift:

    ψ₁(y) = (A₁/r₁) · exp(ikr₁ − i(e/ℏ)∫_{γ₁} A · dl)
    ψ₂(y) = (A₂/r₂) · exp(ikr₂ − i(e/ℏ)∫_{γ₂} A · dl)

### 5.2 Intensity Pattern

For a symmetric geometry (A₁ ≈ A₂ ≈ A, r₁ ≈ r₂ ≈ r):

    I(y) = |ψ₁ + ψ₂|²

    = (2A²/r²)[1 + cos(k·Δr_spatial + (e/ℏ)Φ)]

where Δr_spatial = r₂ − r₁ ≈ d sin θ is the geometric path difference
(as in the standard double-slit) and (e/ℏ)Φ is the AB phase shift.

Rewriting:

    I(y, Φ) = I₀ · cos²(πd sin θ/λ + eΦ/2ℏ)

### 5.3 The Observable Effect

The AB phase shift (e/ℏ)Φ shifts the entire interference pattern laterally.
The fringe maxima move from:

    d sin θ = nλ    (Φ = 0)

to:

    d sin θ = nλ − λeΦ/(2πℏ) = nλ − eΦ/(hc · d)... 

More directly: the fringe shift (in units of fringe spacing) is:

    Δn = (e/ℏ)Φ / (2π) = eΦ/h = Φ/Φ₀

where Φ₀ = h/e is the magnetic flux quantum.

**For Φ = Φ₀/2 = h/(2e):** The pattern shifts by half a fringe — bright
fringes become dark and vice versa. This is the maximally detectable shift.

**For Φ = Φ₀ = h/e:** The pattern shifts by one full fringe — returning to
its original appearance. The effect is periodic in the flux with period Φ₀.

---

## 6. Flux Quantization from E-Geometry

### 6.1 The Flux Quantum

The periodicity of the interference pattern with period Φ₀ = h/e has a
clean geometric origin in the 5D framework.

The e-dimension is a circle of circumference 2π (in the natural angular
parameterization). One full revolution of the e-coordinate is Δφ = 2π. The
AB phase shift for enclosed flux Φ is:

    Δφ = (e/ℏ)Φ

Setting Δφ = 2π (one full e-revolution):

    (e/ℏ)Φ₀ = 2π    →    Φ₀ = 2πℏ/e = h/e

**The flux quantum is the amount of magnetic flux needed to wind the
e-coordinate through one complete revolution of the e-circle.**

This is not an independent experimental fact to be memorized. It is
determined by two geometric quantities:
- The circumference of the e-circle (2π in natural units)
- The coupling strength between the electromagnetic connection and the
  e-coordinate (e/ℏ)

The ratio h/e emerges from the geometry.

### 6.2 Superconducting Flux Quantization

In superconductors, the flux quantum is Φ₀^SC = h/(2e) — half the
single-electron value. This is because superconducting charge carriers are
Cooper pairs with charge 2e. In the 5D framework:

    Δφ = (2e/ℏ)Φ = 2π    →    Φ₀^SC = 2πℏ/(2e) = h/(2e)

The Cooper pair winds the e-circle twice as fast per unit flux (due to
double the charge), so it completes a full revolution at half the flux.
The factor of 2 is geometric — it reflects the charge of the carrier, which
determines the coupling strength to the e-connection.

---

## 7. The 5D Path Integral

### 7.1 Formulation

The 5D propagator for an electron in the AB geometry is:

    K(r', φ'; r, φ; T) = ∫ D[r(t)] D[φ(t)] exp(iS₅D/ℏ)

with the action:

    S₅D = ∫₀ᵀ ½m[ẋ² + R_e²(φ̇ + (e/ℏ)A · ẋ)²] dt

### 7.2 Separation of Spatial and E-Sectors

The action separates into spatial and e-contributions:

    S₅D = S_spatial + S_e + S_coupling

where:
- S_spatial = ∫ ½mẋ² dt (free spatial propagation)
- S_e = ∫ ½mR_e²φ̇² dt (free e-propagation)
- S_coupling = ∫ mR_e²φ̇(e/ℏ)A·ẋ dt + ∫ ½mR_e²((e/ℏ)A·ẋ)² dt

The coupling term is what produces the AB effect. For paths outside the
solenoid (where B = 0 and A is pure gauge), the coupling simplifies.

### 7.3 The Topological Phase

For any path γ from a to b outside the solenoid, the coupling contribution
to the action is:

    S_coupling[γ] = mR_e² · (e/ℏ) · ⟨φ̇⟩ · ∫_γ A · dl + ...

The key term is the line integral ∫_γ A · dl, which depends on the
TOPOLOGY of the path relative to the solenoid.

For paths in the same homotopy class (not encircling the solenoid), this
integral is gauge-dependent and can be set to zero by a gauge choice.

For paths in DIFFERENT homotopy classes (one encircling the solenoid, one
not), the DIFFERENCE in line integrals is gauge-INDEPENDENT and equals the
enclosed flux Φ.

In the path integral, the propagator sums over all paths. Paths that
encircle the solenoid n times contribute with an additional phase factor:

    exp(in(e/ℏ)Φ)

relative to paths that do not encircle it. This topological phase is the
AB effect.

### 7.4 The Full Propagator

The propagator from source to detector, summing over both paths (left and
right of solenoid), is:

    K_total = K_left · exp(−i(e/ℏ)∫_{γ_L} A · dl) + K_right · exp(−i(e/ℏ)∫_{γ_R} A · dl)

The spatial propagators K_left and K_right give the standard double-slit
amplitudes. The exponential factors are the e-phase shifts from parallel
transport along each path.

The intensity is:

    I(y) = |K_total|² = |K_L|² + |K_R|² + 2Re[K_L* K_R · exp(i(e/ℏ)Φ)]

The interference term oscillates with the AB phase (e/ℏ)Φ, producing the
fringe shift described in Section 5.

---

## 8. Comparison with Standard Derivation

| Step | Standard QM derivation | 5D framework derivation |
|------|----------------------|------------------------|
| Vector potential | Mathematical object, gauge-ambiguous | Connection on the e-bundle, physically real |
| Phase shift origin | "The potential is physical" (asserted) | Holonomy of e-connection (derived from geometry) |
| Why B = 0 yet effect occurs | Potential has physical content beyond field | Locally flat but globally twisted e-bundle |
| Flux quantization | Experimental fact | Circumference of the e-circle: Φ₀ = 2πℏ/e |
| Path independence | Gauge invariance of the phase difference | Holonomy is a topological invariant |
| Connection to spin-statistics | None apparent | Same mechanism: holonomy of e-connection |

The 5D derivation reproduces every quantitative result of the standard
treatment. What it adds is the geometric reason: the vector potential is
the connection on a physical fifth dimension, the phase shift is the
holonomy of this connection, and the flux quantum is set by the geometry
of the e-circle.

---

## 9. What This Establishes

**The Aharonov-Bohm phase shift is derived quantitatively.** The result
Δφ = (e/ℏ)Φ follows from the 5D path integral with the e-connection
(e/ℏ)A. The standard experimental predictions are reproduced exactly.

**The vector potential is physically real.** In the 5D framework, A is the
connection on the e-bundle — a geometric object with direct physical content.
Its physical reality is not an awkward conclusion forced by the AB experiment;
it is a prediction of the framework.

**Flux quantization is geometric.** The flux quantum Φ₀ = h/e is the flux
required to wind the e-coordinate through one full revolution. It is
determined by the circumference of the e-circle and the charge coupling
constant. The superconducting flux quantum Φ₀/2 follows from the doubled
charge of Cooper pairs.

**The AB effect and spin-statistics are unified.** Both are holonomies of
the e-connection: the AB holonomy around a solenoid, the exchange holonomy
around identical particles. The 5D framework reveals them as the same
geometric mechanism.

---

## 10. Key References

- Aharonov, Y. & Bohm, D. "Significance of Electromagnetic Potentials in
  the Quantum Theory." *Phys. Rev.* 115, 485–491 (1959).
- Chambers, R. G. "Shift of an Electron Interference Pattern by Enclosed
  Magnetic Flux." *Phys. Rev. Lett.* 5, 3–5 (1960).
- Tonomura, A. et al. "Evidence for Aharonov-Bohm effect with magnetic
  field completely shielded from electron wave." *Phys. Rev. Lett.* 56,
  792–795 (1986). — Definitive experimental confirmation.
- Wu, T. T. & Yang, C. N. "Concept of Nonintegrable Phase Factors and
  Global Formulation of Gauge Fields." *Phys. Rev. D* 12, 3845–3857 (1975).
  — Fiber bundle formulation of electromagnetism; closest mathematical
  precursor to the 5D interpretation.
- Peshkin, M. & Tonomura, A. *The Aharonov-Bohm Effect.* Springer LNP 340
  (1989). — Comprehensive monograph.
