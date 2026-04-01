# Bell Inequality Violation from the 5D Framework

> **Status:** Working draft
> **Purpose:** Demonstrate explicitly that the 5D geometric framework reproduces
> the quantum mechanical correlations for entangled spin-½ particles, violating
> the CHSH Bell inequality by the maximum quantum amount (Tsirelson's bound).
> This is the single most important calculation the paper needs.
> **Prerequisites:** Section 2 (framework), Section 3.2 (entanglement as
> e-conservation), Bridge 3 (spin as e-momentum)
> **Feeds into:** Section 3.2, Section 6.4, Section 7 of the paper

---

## 1. Why This Calculation Matters

The paper claims that the e-coordinate is a non-local hidden variable,
compatible with Bell's theorem. Bell's theorem (1964) proves that no LOCAL
hidden variable theory can reproduce the quantum correlations for entangled
particles. The experimental violations of Bell inequalities (Aspect et al.
1982, Hensen et al. 2015) confirm that nature is non-local.

The paper's claim is that the e-coordinate provides NON-LOCAL hidden
variables — which Bell's theorem allows. But this claim is empty without
a demonstration that the framework actually reproduces the correlations.

This document provides that demonstration. We show:

1. The Born rule follows from the 5D density and the projection postulate.
2. The singlet-state correlations E(â, b̂) = −cos θ are reproduced exactly.
3. The CHSH inequality is violated: |S| = 2√2 (Tsirelson's bound).
4. The geometric mechanism — e-conservation as non-local constraint — is
   the source of the violation.

---

## 2. The Born Rule from 5D Geometry

Before computing correlations, we establish the Born rule within the
framework. This is currently claimed but not derived in the paper
(Section 3.5).

### 2.1 The 5D Density

A particle's quantum state is described by a wavefunction ψ(x, φ) on the
5D space M³ × S¹. The 5D density is:

    ρ₅D(x, φ) = |ψ(x, φ)|²

This is the literal density of the particle's structure in 5D — how much of
the particle exists at each point (x, φ) in five-dimensional spacetime.

### 2.2 The Projection Postulate (Postulate 4)

Our observations are four-dimensional. We cannot resolve the e-coordinate
directly. When we make a measurement that is sensitive to the e-structure
(a "which-e" measurement), we sample the 5D density at a particular e-region.

For a discrete observable with eigenstates {|i⟩} corresponding to e-regions
{Ωᵢ} on the e-circle, the probability of outcome i is the fraction of the
5D density located in e-region Ωᵢ:

    P(i) = ∫_Ωᵢ ∫_{M³} |ψ(x, φ)|² dx dφ  /  ∫_{S¹} ∫_{M³} |ψ(x, φ)|² dx dφ

### 2.3 Recovery of the Standard Born Rule

Expand the wavefunction in the eigenbasis of the measured observable:

    ψ(x, φ) = Σᵢ αᵢ fᵢ(x) gᵢ(φ)

where fᵢ(x) are spatial wavefunctions, gᵢ(φ) are e-eigenstates with support
on Ωᵢ, and the {gᵢ} are orthonormal on S¹.

The 5D density integrated over e-region Ωᵢ gives:

    ∫_Ωᵢ |ψ(x, φ)|² dφ = |αᵢ|² |fᵢ(x)|²

(by orthonormality of the gᵢ — cross terms vanish because the e-eigenstates
have disjoint support on S¹).

Integrating over space:

    P(i) = |αᵢ|² ∫|fᵢ(x)|² dx / Σⱼ |αⱼ|² ∫|fⱼ(x)|² dx = |αᵢ|²

using the normalization ∫|fᵢ|² dx = 1 and Σⱼ|αⱼ|² = 1.

**Result:**

    P(i) = |αᵢ|²

This is the Born rule. It is not a separate postulate — it follows from:
(a) the identification of |ψ|² as the 5D density (Section 2.4 of the paper),
(b) the projection postulate (Postulate 4), and
(c) the orthonormality of e-eigenstates.

---

## 3. The Singlet State in the E-Dimension

### 3.1 Two Spin-½ Particles

Each particle has a two-dimensional e-Hilbert space spanned by:

    |+½⟩ ≡ |↑⟩    (e-winding n = +½, right-handed helix)
    |−½⟩ ≡ |↓⟩    (e-winding n = −½, left-handed helix)

The two-particle Hilbert space is the tensor product, spanned by:
{|↑↑⟩, |↑↓⟩, |↓↑⟩, |↓↓⟩}.

### 3.2 The Singlet State

The singlet state is:

    |Ψ⁻⟩ = (1/√2)(|↑₁↓₂⟩ − |↓₁↑₂⟩)

In the 5D framework, this state has the following geometric content:

**E-conservation constraint.** The total e-winding is zero:

    n₁ + n₂ = 0

If particle 1 has e-winding +½, particle 2 has e-winding −½, and vice versa.
The constraint is the geometric manifestation of the entanglement — it
connects the two particles through the e-dimension regardless of their
spatial separation.

**Anticorrelation of chirality.** The two particles always have OPPOSITE
helical chirality: one right-handed, one left-handed. This is the geometric
content of the singlet being a spin-zero state.

**Rotational invariance.** The singlet state is invariant under simultaneous
rotation of both particles' spin axes. In the e-dimension picture, this
means the anticorrelation holds regardless of the axis along which chirality
is assessed — the e-conservation constraint is axis-independent.

### 3.3 Spin Measurement Along an Arbitrary Axis

For a measurement axis n̂ making angle θ with the z-axis (in the xz-plane,
without loss of generality), the spin-up and spin-down eigenstates are:

    |↑_n̂⟩ = cos(θ/2)|↑⟩ + sin(θ/2)|↓⟩
    |↓_n̂⟩ = −sin(θ/2)|↑⟩ + cos(θ/2)|↓⟩

In the e-dimension picture, measuring spin along n̂ means sampling the
particle's e-structure projected onto the n̂-eigenstates. The e-winding
states |↑⟩ and |↓⟩ are defined relative to a reference axis (z). Measuring
along a DIFFERENT axis n̂ decomposes the e-state into n̂-eigenstates, with
amplitudes given by the rotation matrix above.

The probability of finding spin-up along n̂, given the particle is in state
|↑⟩ (e-winding +½ along z), is:

    P(↑_n̂ | ↑_z) = |⟨↑_n̂|↑⟩|² = cos²(θ/2)

This is the Born rule applied to the e-sampling of a spin state — the 5D
density at the ↑_n̂ e-region when the particle's e-winding is +½ along z.

---

## 4. The Correlation Function

### 4.1 Setup

Particle 1 is measured along axis â (angle α from z-axis).
Particle 2 is measured along axis b̂ (angle β from z-axis).
The angle between â and b̂ is θ = β − α.

We compute the joint probability of all four outcome combinations.

### 4.2 Joint Probabilities

The joint probability of outcome (a, b) for measurements along (â, b̂) on
the singlet state |Ψ⁻⟩ is:

    P(a, b) = |⟨a_â, b_b̂|Ψ⁻⟩|²

where a, b ∈ {↑, ↓}.

**P(↑_â, ↑_b̂):**

    ⟨↑_â, ↑_b̂|Ψ⁻⟩ = (1/√2)[⟨↑_â|↑⟩⟨↑_b̂|↓⟩ − ⟨↑_â|↓⟩⟨↑_b̂|↑⟩]

    = (1/√2)[cos(α/2) · sin(β/2) − sin(α/2) · cos(β/2)]

    = (1/√2) · sin((β − α)/2)

    = (1/√2) · sin(θ/2)

Therefore:

    P(↑_â, ↑_b̂) = ½ sin²(θ/2)

**P(↑_â, ↓_b̂):**

    ⟨↑_â, ↓_b̂|Ψ⁻⟩ = (1/√2)[cos(α/2) · cos(β/2) + sin(α/2) · sin(β/2)]

    = (1/√2) · cos((β − α)/2)

    = (1/√2) · cos(θ/2)

Therefore:

    P(↑_â, ↓_b̂) = ½ cos²(θ/2)

**By symmetry of the singlet state:**

    P(↓_â, ↑_b̂) = ½ cos²(θ/2)
    P(↓_â, ↓_b̂) = ½ sin²(θ/2)

**Verification:** P(↑↑) + P(↑↓) + P(↓↑) + P(↓↓) = sin²(θ/2) + cos²(θ/2) = 1. ✓

### 4.3 The Correlation Function

Define the correlation function as the expectation value of the product of
outcomes, with ↑ = +1 and ↓ = −1:

    E(â, b̂) = P(↑↑) + P(↓↓) − P(↑↓) − P(↓↑)

    = ½sin²(θ/2) + ½sin²(θ/2) − ½cos²(θ/2) − ½cos²(θ/2)

    = sin²(θ/2) − cos²(θ/2)

    = −cos θ

**Result:**

    E(â, b̂) = −cos θ = −â · b̂

This is the standard quantum mechanical prediction for the singlet-state
correlation. The 5D framework reproduces it exactly.

---

## 5. CHSH Inequality Violation

### 5.1 The CHSH Inequality

The Clauser-Horne-Shimony-Holt (CHSH) inequality states that for any local
hidden variable theory:

    |S| ≤ 2

where:

    S = E(â, b̂) − E(â, b̂') + E(â', b̂) + E(â', b̂')

### 5.2 Optimal Measurement Axes

Choose the measurement axes that maximize |S|:

    â at 0°,  â' at 90°,  b̂ at 45°,  b̂' at 135°

(all angles measured from the z-axis in the xz-plane).

The pairwise angles are:

    θ(â, b̂)   = 45°    → E = −cos 45°  = −√2/2
    θ(â, b̂')  = 135°   → E = −cos 135° = +√2/2
    θ(â', b̂)  = 45°    → E = −cos 45°  = −√2/2
    θ(â', b̂') = 45°    → E = −cos 45°  = −√2/2

### 5.3 The CHSH Value

    S = E(â, b̂) − E(â, b̂') + E(â', b̂) + E(â', b̂')

    = (−√2/2) − (+√2/2) + (−√2/2) + (−√2/2)

    = −4 · √2/2

    = −2√2

Therefore:

    |S| = 2√2 ≈ 2.828

### 5.4 Comparison with Bounds

| Bound | Value | Source |
|-------|-------|--------|
| Local hidden variable (CHSH) | |S| ≤ 2 | Bell (1964), CHSH (1969) |
| **5D framework prediction** | **|S| = 2√2 ≈ 2.83** | **This calculation** |
| Quantum mechanics (Tsirelson) | |S| ≤ 2√2 | Tsirelson (1980) |
| Experiment (Hensen et al.) | |S| = 2.42 ± 0.20 | Hensen et al. (2015) |

The 5D framework:
- **Violates** the CHSH inequality (2√2 > 2) ✓
- **Saturates** the Tsirelson bound (2√2 = 2√2) ✓
- **Is consistent** with experimental measurements ✓

---

## 6. The Geometric Mechanism

### 6.1 Why the Correlations Exceed the Classical Bound

In a local hidden variable theory, the correlations are limited to |S| ≤ 2
because each particle's outcome is a function only of the local hidden
variable and the local measurement axis: A(â, λ) and B(b̂, λ). The two
functions are independent — A does not depend on b̂, and B does not depend
on â.

In the 5D framework, this independence is BROKEN by the e-conservation
constraint. The mechanism:

**Step 1 — E-conservation as non-local constraint.**
The singlet state has the geometric constraint n₁ + n₂ = 0, which connects
the two particles' e-structures through the fifth dimension. The particles
are spatially separated but geometrically connected in the e-dimension.

**Step 2 — Measurement as e-sampling.**
When particle 1 is measured along â, its e-structure is sampled at the
â-eigenstates. The outcome is ↑_â with probability cos²(α/2) or ↓_â with
probability sin²(α/2) (if the particle's e-winding was +½ along z).

**Step 3 — Constraint propagation through e-space.**
The e-conservation constraint IMMEDIATELY updates particle 2's e-structure:
if particle 1 is found in state |↑_â⟩, particle 2's e-state is projected
onto the state consistent with n₁ + n₂ = 0 and the measurement result.
Specifically, particle 2 is left in the state |↓_â⟩ — spin-down along â.

This is not a signal propagating through space. It is the conservation law
revealing the pre-existing geometric relationship. The same way that
measuring one billiard ball's momentum after a collision immediately tells
you the other's — by arithmetic on a conserved quantity.

**Step 4 — Second measurement on the constrained state.**
Particle 2, now in state |↓_â⟩ (due to the constraint), is measured along
b̂. The probability of ↑_b̂ is:

    P(↑_b̂ | ↓_â) = |⟨↑_b̂|↓_â⟩|² = sin²(θ/2)

where θ is the angle between â and b̂. This depends on â — the measurement
axis used on particle 1 — through the e-conservation constraint.

**Step 5 — Non-locality produces the violation.**
The dependence of particle 2's outcome probabilities on particle 1's
measurement axis â is what produces correlations stronger than any local
model can achieve. This dependence is mediated by the e-dimension, not by
any signal through space.

### 6.2 The E-Dimension as the Source of Non-Locality

Bell's theorem rules out LOCAL hidden variables. The CHSH bound |S| ≤ 2
is the quantitative limit of local correlations.

The e-coordinate is a NON-LOCAL hidden variable: it connects particles
through a dimension orthogonal to space. The e-conservation constraint
propagates through the e-dimension, not through (x, y, z). This is why
the correlations can exceed the CHSH bound — the constraint is not limited
by spatial locality.

The geometric picture is vivid:

- In 4D (our observation): the particles are far apart, and the correlations
  seem to require faster-than-light communication.

- In 5D (the full reality): the particles are connected through the
  e-dimension. The constraint n₁ + n₂ = 0 is a geometric fact about their
  shared e-structure. No communication is needed — the correlation was
  established at creation and is revealed by measurement.

This is exactly the resolution proposed in Section 3.2 of the paper, now
demonstrated quantitatively.

---

## 7. On the Nature of This Calculation

A fair question: does this calculation do anything beyond re-deriving the
standard quantum mechanical result?

**What it does NOT do:**
It does not produce a new prediction. The correlation E = −cos θ and the
CHSH value |S| = 2√2 are the standard quantum mechanical results. The 5D
framework, in its current form, makes the same predictions as quantum
mechanics.

**What it DOES do:**

1. **Derives the Born rule.** Section 2 shows that P(i) = |αᵢ|² follows
   from the 5D density and the projection postulate. This is not a separate
   axiom in the 5D framework — it is a geometric consequence.

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
   (Section 3.2) is qualitative. This calculation makes it quantitative,
   showing that the e-conservation constraint produces EXACTLY the right
   correlations, not just approximately.

---

## 8. What This Establishes for the Paper

**For Section 3.2 (Entanglement):** The e-conservation constraint e₁ + e₂ = C
reproduces the singlet-state correlation function E(â, b̂) = −cos θ exactly.
The qualitative claim is now a quantitative result.

**For Section 3.5 (Measurement):** The Born rule P(i) = |αᵢ|² is derived from
the 5D density and the projection postulate. It is not a separate axiom.

**For Section 6.4 (Bell's Theorem):** The framework explicitly violates the
CHSH inequality: |S| = 2√2, saturating the Tsirelson bound. The violation is
sourced by the non-local e-conservation constraint. The framework is a
non-local hidden variable theory, compatible with Bell's theorem by
construction.

**For Section 7 (Philosophy):** The claim that the e-coordinate is a hidden
variable, that the framework is deterministic at the 5D level, and that the
apparent randomness is epistemic — all of these are now supported by a
concrete calculation showing the correct correlations emerge from the
geometric structure.

---

## 9. Key References

- Bell, J. S. "On the Einstein Podolsky Rosen Paradox." *Physics* 1, 195–200
  (1964).
- Clauser, J. F., Horne, M. A., Shimony, A. & Holt, R. A. "Proposed
  Experiment to Test Local Hidden-Variable Theories." *Phys. Rev. Lett.* 23,
  880–884 (1969).
- Tsirelson, B. S. "Quantum generalizations of Bell's inequality." *Lett.
  Math. Phys.* 4, 93–100 (1980).
- Aspect, A., Grangier, P. & Roger, G. "Experimental Realization of
  Einstein-Podolsky-Rosen-Bohm Gedankenexperiment." *Phys. Rev. Lett.* 49,
  91–94 (1982).
- Hensen, B. et al. "Loophole-free Bell inequality violation using electron
  spins separated by 1.3 kilometres." *Nature* 526, 682–686 (2015).

---

## 10. Summary in One Paragraph

The 5D geometric framework reproduces the quantum mechanical correlations
for entangled spin-½ particles exactly. The Born rule P(i) = |αᵢ|² is
derived from the 5D density and the projection postulate — it is a geometric
consequence, not an axiom. The singlet-state correlation function
E(â, b̂) = −cos θ follows from the e-conservation constraint (n₁ + n₂ = 0)
combined with spin measurement as e-sampling. The CHSH inequality is
violated: |S| = 2√2, saturating the Tsirelson bound. The violation is sourced
by the non-local e-conservation constraint, which connects the particles
through the fifth dimension. The e-coordinate is a non-local hidden variable
— exactly the kind Bell's theorem allows. The framework does not produce new
predictions for this experiment; it produces the same predictions as quantum
mechanics, with a geometric mechanism that explains why they take the form
they do.
