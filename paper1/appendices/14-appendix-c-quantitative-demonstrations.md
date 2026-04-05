# Appendix C — Quantitative Demonstrations

This appendix demonstrates that the 5D framework quantitatively reproduces three canonical results of quantum mechanics: the Born rule and Bell inequality violation, the double-slit interference pattern, and the Aharonov-Bohm phase shift. Each calculation starts from the framework's postulates and derives the standard result.

---

## C.1 The Born Rule and Bell Inequality Violation

### C.1.1 The Born Rule from 5D Geometry

Before computing correlations, we establish the Born rule within the framework.

#### C.1.1.1 The 5D Density

A particle's quantum state is described by a wavefunction `ψ(x, φ)` on the
5D space `M³ × S¹`. The 5D density is:

    ρ₅D(x, φ) = |ψ(x, φ)|²

This is the literal density of the particle's structure in 5D — how much of
the particle exists at each point `(x, φ)` in five-dimensional spacetime.

#### C.1.1.2 The Projection Postulate (Postulate 4)

Our observations are four-dimensional. We cannot resolve the e-coordinate
directly. When we make a measurement that is sensitive to the e-structure
(a "which-e" measurement), we sample the 5D density at a particular e-region.

For a discrete observable with eigenstates `\{|i⟩\}` corresponding to e-regions
`\{Ωᵢ\}` on the e-circle, the probability of outcome `i` is the fraction of the
5D density located in e-region `Ωᵢ`:

    P(i) = ∫_{Ωᵢ} ∫_{M³} |ψ(x, φ)|² dx dφ  /  ∫_{S¹} ∫_{M³} |ψ(x, φ)|² dx dφ

#### C.1.1.3 Recovery of the Standard Born Rule

Expand the wavefunction in the eigenbasis of the measured observable:

    ψ(x, φ) = \sum_i αᵢ fᵢ(x) gᵢ(φ)

where `fᵢ(x)` are spatial wavefunctions, `gᵢ(φ)` are e-eigenstates with support
on `Ωᵢ`, and the `\{gᵢ\}` are orthonormal on `S¹`.

The 5D density integrated over e-region `Ωᵢ` gives:

    ∫_{Ωᵢ} |ψ(x, φ)|² dφ = |αᵢ|² |fᵢ(x)|²

(by orthonormality of the `gᵢ` — cross terms vanish because the e-eigenstates
have disjoint support on `S¹`).

Integrating over space:

    P(i) = |αᵢ|² ∫|fᵢ(x)|² dx / \sum_j |αⱼ|² ∫|fⱼ(x)|² dx = |αᵢ|²

using the normalization `∫|fᵢ|² dx = 1` and `Σⱼ|αⱼ|² = 1`.

**Result:**

    P(i) = |αᵢ|²

This is the Born rule. It is geometrically motivated and uniquely selected
by the framework, following from:
(a) the identification of `|ψ|²` as the 5D density,
(b) the Haar measure `dφ/2π` on the e-circle — the *unique*
    translation-invariant measure on `U(1)`, forced by Postulate 3
    (e-translation invariance), and
(c) the orthonormality of e-eigenstates.

Note that the Haar measure argument breaks the circularity that would
arise from simply postulating `|ψ|²` as a probability density. The
measure is not chosen to reproduce the Born rule — it is the *only*
measure consistent with the e-circle's symmetry. The Born rule is
then a theorem, not an assumption.

This result is independently supported by Torres Alegre (2026,
arXiv:2512.12636), who proves that `|⟨φ|ψ⟩|²` is the unique probability
assignment consistent with causal consistency (no superluminal
signaling) in any generalized probabilistic theory. In the 5D
framework, where causal signals propagate along the 4D base and not
along the e-fiber, this condition is geometrically enforced. See also
Brenig and Vincke (2026, arXiv:2601.12092), who derive the Born rule
from invariance properties of a "new space-like dimension" —
conceptually parallel to the e-dimension.

### C.1.2 The Singlet State in the E-Dimension

#### C.1.2.1 Two Spin-`½` Particles

Each particle has a two-dimensional e-Hilbert space spanned by:

    |+½⟩ ≡ |↑⟩    (e-winding n = +½, right-handed helix)
    |−½⟩ ≡ |↓⟩    (e-winding n = −½, left-handed helix)

The two-particle Hilbert space is the tensor product, spanned by:
`\{|↑↑⟩, |↑↓⟩, |↓↑⟩, |↓↓⟩\}`.

#### C.1.2.2 The Singlet State

The singlet state is:

    |Ψ⁻⟩ = (1/\sqrt{2})(|↑₁↓₂⟩ − |↓₁↑₂⟩)

In the 5D framework, this state has the following geometric content:

**E-conservation constraint.** The total e-winding is zero:

    n₁ + n₂ = 0

If particle 1 has e-winding `+½`, particle 2 has e-winding `−½`, and vice versa.
The constraint is the geometric manifestation of the entanglement — it
connects the two particles through the e-dimension regardless of their
spatial separation.

**Anticorrelation of chirality.** The two particles always have opposite
helical chirality: one right-handed, one left-handed. This is the geometric
content of the singlet being a spin-zero state.

**Rotational invariance.** The singlet state is invariant under simultaneous
rotation of both particles' spin axes. In the e-dimension picture, this
means the anticorrelation holds regardless of the axis along which chirality
is assessed — the e-conservation constraint is axis-independent.

#### C.1.2.3 Spin Measurement Along an Arbitrary Axis

For a measurement axis `n̂` making angle `θ` with the z-axis (in the xz-plane,
without loss of generality), the spin-up and spin-down eigenstates are:

    |↑_n̂⟩ = \cos(θ/2)|↑⟩ + \sin(θ/2)|↓⟩
    |↓_n̂⟩ = -\sin(θ/2)|↑⟩ + \cos(θ/2)|↓⟩

In the e-dimension picture, measuring spin along `n̂` means sampling the
particle's e-structure projected onto the `n̂`-eigenstates. The e-winding
states `|↑⟩` and `|↓⟩` are defined relative to a reference axis (z). Measuring
along a different axis `n̂` decomposes the e-state into `n̂`-eigenstates, with
amplitudes given by the rotation matrix above.

The probability of finding spin-up along `n̂`, given the particle is in state
`|↑⟩` (e-winding `+½` along z), is:

    P(↑_n̂ | ↑_z) = |⟨↑_n̂|↑⟩|² = \cos^2(θ/2)

This is the Born rule applied to the e-sampling of a spin state — the 5D
density at the `↑_n̂` e-region when the particle's e-winding is `+½` along z.

### C.1.3 The Correlation Function

#### C.1.3.1 Setup

Particle 1 is measured along axis `â` (angle `α` from z-axis).
Particle 2 is measured along axis `b̂` (angle `β` from z-axis).
The angle between `â` and `b̂` is `θ = β − α`.

We compute the joint probability of all four outcome combinations.

#### C.1.3.2 Joint Probabilities

The joint probability of outcome `(a, b)` for measurements along `(â, b̂)` on
the singlet state `|Ψ⁻⟩` is:

    P(a, b) = |⟨a_â, b_b̂|Ψ⁻⟩|²

where `a, b ∈ \{↑, ↓\}`.

**`P(↑_â, ↑_b̂)`:**

    ⟨↑_â, ↑_b̂|Ψ⁻⟩ = (1/\sqrt{2})[⟨↑_â|↑⟩⟨↑_b̂|↓⟩ − ⟨↑_â|↓⟩⟨↑_b̂|↑⟩]

    = (1/\sqrt{2})[\cos(α/2) · \sin(β/2) − \sin(α/2) · \cos(β/2)]

    = (1/\sqrt{2}) · \sin((β − α)/2)

    = (1/\sqrt{2}) · \sin(θ/2)

Therefore:

    P(↑_â, ↑_b̂) = ½ \sin^2(θ/2)

**`P(↑_â, ↓_b̂)`:**

    ⟨↑_â, ↓_b̂|Ψ⁻⟩ = (1/\sqrt{2})[\cos(α/2) · \cos(β/2) + \sin(α/2) · \sin(β/2)]

    = (1/\sqrt{2}) · \cos((β − α)/2)

    = (1/\sqrt{2}) · \cos(θ/2)

Therefore:

    P(↑_â, ↓_b̂) = ½ \cos^2(θ/2)

**By symmetry of the singlet state:**

    P(↓_â, ↑_b̂) = ½ \cos^2(θ/2)
    P(↓_â, ↓_b̂) = ½ \sin^2(θ/2)

**Verification:** `P(↑↑) + P(↑↓) + P(↓↑) + P(↓↓) = sin²(θ/2) + cos²(θ/2) = 1`. `✓`

#### C.1.3.3 The Correlation Function

Define the correlation function as the expectation value of the product of
outcomes, with `↑ = +1` and `↓ = −1`:

    E(â, b̂) = P(↑↑) + P(↓↓) − P(↑↓) − P(↓↑)

    = ½\sin^2(θ/2) + ½\sin^2(θ/2) − ½\cos^2(θ/2) − ½\cos^2(θ/2)

    = \sin^2(θ/2) − \cos^2(θ/2)

    = -\cos θ

**Result:**

    E(â, b̂) = -\cos θ = -â · b̂

This is the standard quantum mechanical prediction for the singlet-state
correlation. The 5D framework reproduces it exactly.

### C.1.4 CHSH Inequality Violation

#### C.1.4.1 The CHSH Inequality

The Clauser-Horne-Shimony-Holt (CHSH) inequality states that for any local
hidden variable theory:

    |S| ≤ 2

where:

    S = E(â, b̂) − E(â, b̂') + E(â', b̂) + E(â', b̂')

#### C.1.4.2 Optimal Measurement Axes

Choose the measurement axes that maximize `|S|`:

    â at 0°,  â' at 90°,  b̂ at 45°,  b̂' at 135°

(all angles measured from the z-axis in the xz-plane).

The pairwise angles are:

    θ(â, b̂)   = 45°    → E = -\cos 45°  = -\sqrt{2}/2
    θ(â, b̂')  = 135°   → E = -\cos 135° = +\sqrt{2}/2
    θ(â', b̂)  = 45°    → E = -\cos 45°  = -\sqrt{2}/2
    θ(â', b̂') = 45°    → E = -\cos 45°  = -\sqrt{2}/2

#### C.1.4.3 The CHSH Value

    S = E(â, b̂) − E(â, b̂') + E(â', b̂) + E(â', b̂')

    = (-\sqrt{2}/2) − (+\sqrt{2}/2) + (-\sqrt{2}/2) + (-\sqrt{2}/2)

    = -4 · \sqrt{2}/2

    = -2\sqrt{2}

Therefore:

    |S| = 2\sqrt{2} ≈ 2.828

#### C.1.4.4 Comparison with Bounds

| Bound | Value | Source |
|-------|-------|--------|
| Local hidden variable (CHSH) | `\lvert S \rvert ≤ 2` | Bell (1964), CHSH (1969) |
| **5D framework prediction** | **`\lvert S \rvert = 2√2 ≈ 2.83`** | **This calculation** |
| Quantum mechanics (Tsirelson) | `\lvert S \rvert ≤ 2√2` | Tsirelson (1980) |
| Experiment (Hensen et al.) | `\lvert S \rvert = 2.42 ± 0.20` | Hensen et al. (2015) |

The 5D framework:
- **Violates** the CHSH inequality (`2√2 > 2`)
- **Saturates** the Tsirelson bound (`2√2 = 2√2`)
- **Is consistent** with experimental measurements

### C.1.5 The Geometric Mechanism

#### C.1.5.1 Why the Correlations Exceed the Classical Bound

In a local hidden variable theory, the correlations are limited to `|S| ≤ 2`
because each particle's outcome is a function only of the local hidden
variable and the local measurement axis: `A(â, λ)` and `B(b̂, λ)`. The two
functions are independent — `A` does not depend on `b̂`, and `B` does not depend
on `â`.

In the 5D framework, this independence is broken by the e-conservation
constraint. The mechanism proceeds in five steps.

**Step 1 — E-conservation as non-local constraint.**
The singlet state has the geometric constraint `n₁ + n₂ = 0`, which connects
the two particles' e-structures through the fifth dimension. The particles
are spatially separated but geometrically connected in the e-dimension.

**Step 2 — Measurement as e-sampling.**
When particle 1 is measured along `â`, its e-structure is sampled at the
`â`-eigenstates. The outcome is `↑_â` with probability `cos²(α/2)` or `↓_â` with
probability `sin²(α/2)` (if the particle's e-winding was `+½` along z).

**Step 3 — Constraint propagation through e-space.**
The e-conservation constraint immediately updates particle 2's e-structure:
if particle 1 is found in state `|↑_â⟩`, particle 2's e-state is projected
onto the state consistent with `n₁ + n₂ = 0` and the measurement result.
Specifically, particle 2 is left in the state `|↓_â⟩` — spin-down along `â`.

This is not a signal propagating through space. It is the conservation law
revealing the pre-existing geometric relationship. The same way that
measuring one billiard ball's momentum after a collision immediately tells
you the other's — by arithmetic on a conserved quantity.

**Step 4 — Second measurement on the constrained state.**
Particle 2, now in state `|↓_â⟩` (due to the constraint), is measured along
`b̂`. The probability of `↑_b̂` is:

    P(↑_b̂ | ↓_â) = |⟨↑_b̂|↓_â⟩|² = \sin^2(θ/2)

where `θ` is the angle between `â` and `b̂`. This depends on `â` — the measurement
axis used on particle 1 — through the e-conservation constraint.

**Step 5 — Non-locality produces the violation.**
The dependence of particle 2's outcome probabilities on particle 1's
measurement axis `â` is what produces correlations stronger than any local
model can achieve. This dependence is mediated by the e-dimension, not by
any signal through space.

#### C.1.5.2 The E-Dimension as the Source of Non-Locality

Bell's theorem rules out local hidden variables. The CHSH bound `|S| ≤ 2`
is the quantitative limit of local correlations.

The e-coordinate is a non-local hidden variable: it connects particles
through a dimension orthogonal to space. The e-conservation constraint
propagates through the e-dimension, not through `(x, y, z)`. This is why
the correlations can exceed the CHSH bound — the constraint is not limited
by spatial locality.

The geometric picture is as follows:

- In 4D (our observation): the particles are far apart, and the correlations
  seem to require faster-than-light communication.

- In 5D (the full reality): the particles are connected through the
  e-dimension. The constraint `n₁ + n₂ = 0` is a geometric fact about their
  shared e-structure. No communication is needed — the correlation was
  established at creation and is revealed by measurement.

### C.1.6 Honest Assessment

A fair question: does this calculation do anything beyond re-deriving the
standard quantum mechanical result?

**What it does not do.**
It does not produce a new prediction. The correlation `E = −cos θ` and the
CHSH value `|S| = 2√2` are the standard quantum mechanical results. The 5D
framework, in its current form, makes the same predictions as quantum
mechanics.

**What it does do.**

The calculation demonstrates that the 5D framework REPRODUCES the standard
quantum mechanical result for entangled spin-`½` particles; it does not
derive it from purely geometric axioms independent of the QM formalism.
The Born rule derivation (C.1.1) is a re-derivation within the framework
using the e-density postulate, not an independent derivation from geometry
alone. With this caveat:

1. **Re-derives the Born rule.** Section C.1.1 shows that `P(i) = |αᵢ|²`
   follows from the 5D density and the projection postulate. This is not a
   separate axiom in the 5D framework — it is a geometric consequence of
   the e-density postulate.

2. **Provides the geometric mechanism.** The correlations arise from the
   e-conservation constraint (a Noether conservation law from e-translation
   invariance) combined with e-sampling (the projection postulate). Every
   step has a geometric meaning.

3. **Demonstrates compatibility with Bell's theorem.** The framework is
   explicitly non-local — the e-conservation constraint connects spatially
   separated particles through the fifth dimension — and this non-locality
   is what allows the CHSH bound to be exceeded. The framework satisfies
   Bell's constraint exactly: it is a non-local hidden variable theory, which
   Bell's theorem allows.

4. **Closes the quantitative gap.** The paper's entanglement discussion
   is qualitative. This calculation makes it quantitative,
   showing that the e-conservation constraint produces exactly the right
   correlations, not just approximately.

---

## C.2 Double-Slit Interference

### C.2.1 The E-Phase Along Each Path

#### C.2.1.1 Path Lengths

From slit 1 (at `y = +d/2`) to detection point `y` on the far screen:

    r₁ = \sqrt{L² + (y − d/2)²}

From slit 2 (at `y = −d/2`) to detection point `y`:

    r₂ = \sqrt{L² + (y + d/2)²}

In the far-field (Fraunhofer) approximation (`L >> d, y`):

    r₁ ≈ r − (d/2) \sin θ
    r₂ ≈ r + (d/2) \sin θ

where `r = \sqrt{L² + y²} ≈ L` and `sin θ ≈ y/L`.

The path difference is:

    Δr = r₂ − r₁ ≈ d \sin θ

#### C.2.1.2 E-Phase Accumulation

As the particle's 5D structure propagates from slit to detector, the
e-coordinate advances along each path:

**Path through slit 1:**

    φ₁ = k · r₁ = (p/ℏ) · r₁

**Path through slit 2:**

    φ₂ = k · r₂ = (p/ℏ) · r₂

These are not abstract phases — they are the literal e-coordinates of the
particle's helical structure at the detector, having arrived via each slit.
The particle's 5D structure at the detection point `y` has two e-components:
one at e-value `φ₁` (from slit 1) and one at e-value `φ₂` (from slit 2).

#### C.2.1.3 The E-Phase Difference

    Δφ = φ₂ − φ₁ = k(r₂ − r₁) = k · d \sin θ = (2π/λ) · d \sin θ

This is the difference in e-coordinates between the two components of the
particle's 5D structure at the detector. It depends on the detection angle
`θ` — different points on the detector screen receive e-components with
different phase relationships.

### C.2.2 The Interference Pattern

#### C.2.2.1 Amplitude at the Detector

The wavefunction at detection point `y` is the sum of contributions from both
slits (both e-components arriving at the same spatial point):

    ψ(y) = ψ₁(y) + ψ₂(y)

For equal-amplitude slits in the far field:

    ψ₁(y) ≈ (A/r) · e^{ikr₁} = (A/r) · \exp[ik(r − d \sin θ/2)]
    ψ₂(y) ≈ (A/r) · e^{ikr₂} = (A/r) · \exp[ik(r + d \sin θ/2)]

Factoring out the common phase:

    ψ(y) = (A/r) · e^{ikr} · [e^{-ikd \sin θ/2} + e^{+ikd \sin θ/2}]
          = (2A/r) · e^{ikr} · \cos(kd \sin θ/2)

#### C.2.2.2 Intensity

The 4D observable is the intensity — the 5D density integrated over the
e-dimension and projected onto position:

    I(y) = |ψ(y)|²

    = (4A²/r²) · \cos^2(kd \sin θ/2)

    = (4A²/r²) · \cos^2(πd \sin θ / λ)

This is the standard double-slit interference pattern.

#### C.2.2.3 Fringe Properties

**Bright fringes** (constructive interference) occur where:

    Δφ = 2nπ    →    d \sin θ = nλ    (n = 0, ±1, ±2, ...)

In the 5D picture: the two e-components arrive at the same e-coordinate
(modulo `2π`). The 5D densities add — the particle's structure from both
slits overlaps constructively in e-space.

**Dark fringes** (destructive interference) occur where:

    Δφ = (2n+1)π    →    d \sin θ = (n + ½)λ

In the 5D picture: the two e-components arrive at opposite points on the
e-circle (separated by `π`). The 5D densities cancel — the particle's structure
from the two slits is anti-aligned in e-space, producing zero projected
density.

**Fringe spacing** on the detector:

    Δy = λL/d

This is set entirely by the geometry: the helix pitch (`λ = h/p`), the
propagation distance (`L`), and the slit separation (`d`).

### C.2.3 Single-Slit Diffraction Envelope

For slits of finite width `a`, each slit acts as a distributed source. The
e-phase varies continuously across the slit width, producing a diffraction
envelope:

    I_{single}(θ) = I₀ · \operatorname{sinc}^2(πa \sin θ / λ)

where `sinc(x) = sin(x)/x`.

The full double-slit pattern including the envelope is:

    I(θ) = I₀ · \cos^2(πd \sin θ / λ) · \operatorname{sinc}^2(πa \sin θ / λ)

In the 5D picture, the `sinc²` envelope arises because different e-components
within a single slit accumulate slightly different phases across the slit
width `a`. The `cos²` modulation arises from the phase difference between the
two slits separated by `d`. Both effects are geometric — they are the
e-structure of the particle, shaped by the slit geometry, projected onto 4D.

### C.2.4 Which-Path Measurement and Decoherence

The double-slit experiment is most striking when a which-path detector is
introduced. If we determine which slit the particle went through, the
interference pattern disappears.

In the 5D framework:

**Without which-path measurement:** The particle's 5D structure passes
through both slits coherently. Both e-components arrive at the detector
with a definite phase relationship. Interference occurs.

**With which-path measurement:** The which-path detector interacts with the
particle's e-coordinate, entangling it with the detector's e-coordinate.
This entanglement scrambles the phase relationship between the two
e-components — the relative e-phase `Δφ` is no longer definite but is spread
across all values by the entanglement with the detector.

When the relative e-phase is scrambled, the `cos²(Δφ/2)` factor averages to
`½` over all `Δφ` values:

    ⟨\cos^2(Δφ/2)⟩_Δφ = ½

The interference term vanishes, and the intensity becomes:

    I(y) = I₁(y) + I₂(y)

— the classical sum of intensities from each slit, with no fringes. This
is decoherence: the loss of e-phase coherence through entanglement with
the measuring apparatus.

**The complementarity principle is geometric:** Determining which slit
(spatial information) requires interacting with the e-coordinate (coupling
to the which-path detector), which destroys the e-phase coherence needed
for interference. Position information and phase information cannot coexist
because they compete for the same e-structure.

---

## C.3 Quantitative Aharonov-Bohm Effect

### C.3.1 The 5D Lagrangian and E-Phase Evolution

#### C.3.1.1 The Lagrangian

For an electron of mass `m` and charge `e` on the total space `P(M³, U(1))` with
the Kaluza-Klein metric, the Lagrangian is:

    L = ½m[ẋ² + R_e²(φ̇ + (e/ℏ)A · ẋ)²] − V(x)

where `R_e` is the radius of the e-circle and the coupling is written
explicitly: the connection on the e-bundle is `(e/ℏ)A`, with `e` being the
electron charge and `ℏ` the reduced Planck constant.

#### C.3.1.2 The E-Momentum

The momentum conjugate to the e-coordinate is:

    pφ = ∂L/∂φ̇ = mR_e²(φ̇ + (e/ℏ)A · ẋ)

Since the Lagrangian does not depend on `φ` explicitly, `pφ` is conserved.

#### C.3.1.3 The E-Phase Along a Path

The total e-phase accumulated along a spatial path `γ` from point a to point b
is:

    φ(b) − φ(a) = ∫_γ φ̇ dt = ∫_γ [pφ/(mR_e²) − (e/ℏ)A · ẋ] dt

The first term `(pφ/(mR_e²))·T` is the free e-evolution — it depends on the
e-momentum and the transit time but is the same for both paths (since `pφ` is
conserved and both paths take the same transit time in the symmetric geometry).

The second term is the connection contribution — the parallel transport of
the e-coordinate by the gauge field:

    Δφ_{connection}[γ] = −(e/ℏ) ∫_γ A · dl

This is the term that differs between the two paths and produces the AB effect.

### C.3.2 The Phase Shift Calculation

#### C.3.2.1 E-Phase Along Each Path

**Path 1 (left of solenoid):**

    Δφ₁ = (pφ/(mR_e²))T − (e/ℏ) ∫_{γ₁} A · dl

**Path 2 (right of solenoid):**

    Δφ₂ = (pφ/(mR_e²))T − (e/ℏ) ∫_{γ₂} A · dl

The free evolution terms are identical (same `pφ`, same `T`). They cancel in the
phase difference.

#### C.3.2.2 The Phase Difference

    Δφ = Δφ₁ − Δφ₂ = −(e/ℏ)[∫_{γ₁} A · dl − ∫_{γ₂} A · dl]

The quantity in brackets is the line integral of `A` around the closed loop
`γ = γ₁ − γ₂` (traversing `γ₁` forward and `γ₂` backward):

    ∫_{γ₁} A · dl − ∫_{γ₂} A · dl = ∮_{γ₁ − γ₂} A · dl

By Stokes' theorem, this equals the flux of `B` through any surface bounded
by the loop:

    ∮_γ A · dl = ∫_Σ (∇ × A) · dA = ∫_Σ B · dA = Φ

Note: outside the solenoid, `B = 0`. But the surface `Σ` bounded by the loop
necessarily crosses the solenoid interior (where `B ≠ 0`). The flux through
`Σ` is the total solenoid flux `Φ`, regardless of the specific shape of the
loop or the surface.

Therefore:

    **Δφ = −(e/ℏ) · Φ**

This is the Aharonov-Bohm phase shift. Its magnitude is:

    |Δφ| = (e/ℏ) · Φ

#### C.3.2.3 The 5D Interpretation

The phase shift is the holonomy of the e-connection around the closed loop
encircling the solenoid:

    Hol_γ(A_e) = \exp(i(e/ℏ)Φ)

In the e-dimension picture:
- The electron's e-coordinate is parallel-transported along each path by the
  connection `(e/ℏ)A`.
- Outside the solenoid, the connection is non-zero (`A ≠ 0`) even though the
  curvature vanishes (`B = 0`).
- The two paths accumulate different e-phases because the connection is not
  exact — its line integral around the solenoid is non-zero.
- The phase difference is a topological invariant: it depends only on the
  enclosed flux, not on the specific paths taken.

### C.3.3 Interference Pattern with AB Shift

#### C.3.3.1 Amplitude at the Detector

The wavefunction at the detector is the sum of amplitudes from both paths:

    ψ(y) = ψ₁(y) + ψ₂(y)

where `ψ₁` and `ψ₂` include both the spatial propagation phase and the AB
e-phase shift:

    ψ₁(y) = (A₁/r₁) · \exp(ikr₁ − i(e/ℏ)∫_{γ₁} A · dl)
    ψ₂(y) = (A₂/r₂) · \exp(ikr₂ − i(e/ℏ)∫_{γ₂} A · dl)

#### C.3.3.2 Intensity Pattern

For a symmetric geometry (`A₁ ≈ A₂ ≈ A`, `r₁ ≈ r₂ ≈ r`):

    I(y) = |ψ₁ + ψ₂|²

    = (2A²/r²)[1 + \cos(k·Δr_{spatial} + (e/ℏ)Φ)]

where `Δr_{spatial} = r₂ − r₁ ≈ d \sin θ` is the geometric path difference
(as in the standard double-slit) and `(e/ℏ)Φ` is the AB phase shift.

Rewriting:

    I(y, Φ) = I₀ · \cos^2(πd \sin θ/λ + eΦ/2ℏ)

#### C.3.3.3 The Observable Effect

The AB phase shift `(e/ℏ)Φ` shifts the entire interference pattern laterally.
The fringe shift (in units of fringe spacing) is:

    Δn = (e/ℏ)Φ / (2π) = eΦ/h = Φ/Φ₀

where `Φ₀ = h/e` is the magnetic flux quantum.

**For `Φ` = `Φ₀/2` = h/(2e):** The pattern shifts by half a fringe — bright
fringes become dark and vice versa. This is the maximally detectable shift.

**For `Φ` = `Φ₀` = h/e:** The pattern shifts by one full fringe — returning to
its original appearance. The effect is periodic in the flux with period `Φ₀`.

### C.3.4 Flux Quantization from E-Geometry

#### C.3.4.1 The Flux Quantum

The periodicity of the interference pattern with period `Φ₀` = h/e has a
clean geometric origin in the 5D framework.

The e-dimension is a circle of circumference `2π` (in the natural angular
parameterization). One full revolution of the e-coordinate is `Δφ` = `2π`. The
AB phase shift for enclosed flux `Φ` is:

    Δφ = (e/ℏ)Φ

Setting `Δφ` = `2π` (one full e-revolution):

    (e/ℏ)Φ₀ = 2π    →    Φ₀ = 2πℏ/e = h/e

**The flux quantum is the amount of magnetic flux needed to wind the
e-coordinate through one complete revolution of the e-circle.**

This is not an independent experimental fact to be memorized. It is
determined by two geometric quantities:
- The circumference of the e-circle (`2π` in natural units)
- The coupling strength between the electromagnetic connection and the
  e-coordinate (`e/ℏ`)

The ratio h/e emerges from the geometry.

#### C.3.4.2 Superconducting Flux Quantization

In superconductors, the flux quantum is `Φ₀^{SC}` = h/(2e) — half the
single-electron value. This is because superconducting charge carriers are
Cooper pairs with charge 2e. In the 5D framework:

    Δφ = (2e/ℏ)Φ = 2π    →    Φ₀^{SC} = 2πℏ/(2e) = h/(2e)

The Cooper pair winds the e-circle twice as fast per unit flux (due to
double the charge), so it completes a full revolution at half the flux.
The factor of 2 is geometric — it reflects the charge of the carrier, which
determines the coupling strength to the e-connection.

### C.3.5 The 5D Path Integral

#### C.3.5.1 Formulation

The 5D propagator for an electron in the AB geometry is:

    K(r', φ'; r, φ; T) = ∫ D[r(t)] D[φ(t)] \exp(iS_{5D}/ℏ)

with the action:

    S_{5D} = ∫₀ᵀ ½m[ẋ² + R_e²(φ̇ + (e/ℏ)A · ẋ)²] dt

#### C.3.5.2 Separation of Spatial and E-Sectors

The action separates into spatial and e-contributions:

    S_{5D} = S_{spatial} + S_e + S_{coupling}

where:
- `S_{spatial}` = ∫ `½mẋ²` dt (free spatial propagation)
- `S_e` = ∫ `½mR_e²φ̇²` dt (free e-propagation)
- `S_{coupling}` = ∫ `mR_e²φ̇(e/ℏ)A·ẋ` dt + ∫ `½mR_e²((e/ℏ)A·ẋ)²` dt

The coupling term is what produces the AB effect. For paths outside the
solenoid (where B = 0 and A is pure gauge), the coupling simplifies.

#### C.3.5.3 The Topological Phase

For any path `γ` from a to b outside the solenoid, the coupling contribution
to the action is:

    S_{coupling}[γ] = mR_e² · (e/ℏ) · ⟨φ̇⟩ · ∫_γ A · dl + ...

The key term is the line integral `∫_γ A · dl`, which depends on the
topology of the path relative to the solenoid.

For paths in the same homotopy class (not encircling the solenoid), this
integral is gauge-dependent and can be set to zero by a gauge choice.

For paths in different homotopy classes (one encircling the solenoid, one
not), the difference in line integrals is gauge-independent and equals the
enclosed flux `Φ`.

In the path integral, the propagator sums over all paths. Paths that
encircle the solenoid n times contribute with an additional phase factor:

    \exp(in(e/ℏ)Φ)

relative to paths that do not encircle it. This topological phase is the
AB effect.

#### C.3.5.4 The Full Propagator

The propagator from source to detector, summing over both paths (left and
right of solenoid), is:

    K_{total} = K_{left} · \exp(-i(e/ℏ)∫_{γ_L} A · dl) + K_{right} · \exp(-i(e/ℏ)∫_{γ_R} A · dl)

The spatial propagators `K_{left}` and `K_{right}` give the standard double-slit
amplitudes. The exponential factors are the e-phase shifts from parallel
transport along each path.

The intensity is:

    I(y) = |K_{total}|² = |K_L|² + |K_R|² + 2\operatorname{Re}[K_L^* K_R · \exp(i(e/ℏ)Φ)]

The interference term oscillates with the AB phase `(e/ℏ)Φ`, producing the
fringe shift described in Section C.3.3.

### C.3.6 Comparison of Standard and 5D Derivations

| Step | Standard QM derivation | 5D framework derivation |
|------|----------------------|------------------------|
| Vector potential | Mathematical object, gauge-ambiguous | Connection on the e-bundle, physically real |
| Phase shift origin | "The potential is physical" (asserted) | Holonomy of e-connection (derived from geometry) |
| Why B = 0 yet effect occurs | Potential has physical content beyond field | Locally flat but globally twisted e-bundle |
| Flux quantization | Experimental fact | Circumference of the e-circle: `Φ₀` = `2πℏ/e` |
| Path independence | Gauge invariance of the phase difference | Holonomy is a topological invariant |
| Connection to spin-statistics | None apparent | Same mechanism: holonomy of e-connection |

The 5D derivation reproduces every quantitative result of the standard
treatment. What it adds is the geometric reason: the vector potential is
the connection on a physical fifth dimension, the phase shift is the
holonomy of this connection, and the flux quantum is set by the geometry
of the e-circle.

---

## C.4 References

- Aharonov, Y. & Bohm, D. "Significance of Electromagnetic Potentials in
  the Quantum Theory." *Phys. Rev.* 115, 485--491 (1959).
- Aspect, A., Grangier, P. & Roger, G. "Experimental Realization of
  Einstein-Podolsky-Rosen-Bohm Gedankenexperiment." *Phys. Rev. Lett.* 49,
  91--94 (1982).
- Bell, J. S. "On the Einstein Podolsky Rosen Paradox." *Physics* 1,
  195--200 (1964).
- Chambers, R. G. "Shift of an Electron Interference Pattern by Enclosed
  Magnetic Flux." *Phys. Rev. Lett.* 5, 3--5 (1960).
- Clauser, J. F., Horne, M. A., Shimony, A. & Holt, R. A. "Proposed
  Experiment to Test Local Hidden-Variable Theories." *Phys. Rev. Lett.* 23,
  880--884 (1969).
- Feynman, R. P., Leighton, R. B. & Sands, M. *The Feynman Lectures on
  Physics*, Vol. III, Ch. 1 (1965).
- Hensen, B. et al. "Loophole-free Bell inequality violation using electron
  spins separated by 1.3 kilometres." *Nature* 526, 682--686 (2015).
- Peshkin, M. & Tonomura, A. *The Aharonov-Bohm Effect.* Springer LNP 340
  (1989).
- Tonomura, A. et al. "Demonstration of single-electron buildup of an
  interference pattern." *Am. J. Phys.* 57, 117--120 (1989).
- Tonomura, A. et al. "Evidence for Aharonov-Bohm effect with magnetic
  field completely shielded from electron wave." *Phys. Rev. Lett.* 56,
  792--795 (1986).
- Tsirelson, B. S. "Quantum generalizations of Bell's inequality." *Lett.
  Math. Phys.* 4, 93--100 (1980).
- Wu, T. T. & Yang, C. N. "Concept of Nonintegrable Phase Factors and
  Global Formulation of Gauge Fields." *Phys. Rev. D* 12, 3845--3857 (1975).
- Zurek, W. H. "Decoherence, einselection, and the quantum origins of the
  classical." *Rev. Mod. Phys.* 75, 715--775 (2003).
