# Appendix B --- Horizon Vertex Derivation

---

## B.1 Introduction

Theorem 9.1 (Paper 3, Section 9) resolves the AMPS firewall paradox
using e-conservation at the black hole horizon. The theorem was
originally established under one explicitly acknowledged assumption:
that the e-conservation vertex factor at the horizon takes the same
form as in flat space (Section 4.3, Section 9.3.2). This appendix
derives the vertex factor from first principles, discharging that
assumption and rendering Theorem 9.1 unconditional.

The argument is structural, not computational. It rests on three
ingredients: the direct-product structure of the 5D black hole metric,
the Fourier orthogonality of S^1 modes, and the Ward identity for the
conserved e-current.

---

## B.2 Theorem Statement

**Proposition B.1 (Horizon Vertex Factor).** *Let (M^4, g_{4D}) be
any 4D Lorentzian manifold, including a Schwarzschild black hole. Let
the 5D spacetime be (M^4 x S^1, g_{4D} + R_0^2 dphi^2) with R_0
constant. Then the vertex factor for e-charge conservation at any
interaction vertex --- including vertices located at the black hole
horizon --- is:*

    V_e = delta_{sum n_in, sum n_out} = 1
    (when e-charge is conserved)

*This is identical to the flat-space result.*

**Corollary.** *Theorem 9.1 (compatibility of unitarity, no drama,
and effective field theory in 5D) is unconditional. The formerly
remaining assumption (Section 4.3, Section 9.3.2) is discharged.*

---

## B.3 Product Structure of the 5D Black Hole Metric

### B.3.1 The metric

The 5D Schwarzschild metric (Paper 3, Section 3.4) is:

    ds^2_{5D} = f(r) c^2 dt^2 - f(r)^{-1} dr^2
                - r^2 dOmega^2 + R_0^2 dphi^2

where f(r) = 1 - r_s/r and phi in [0, 2 pi R_0) is the e-coordinate.
This is a direct product metric:

    ds^2_{5D} = ds^2_{4D}(t, r, theta, varphi) + ds^2_{S^1}(phi)

No metric component couples the 4D coordinates to phi. No metric
component depends on phi. The determinant factorizes:

    sqrt{g_{5D}} = sqrt{g_{4D}} x R_0

### B.3.2 Factorization of the action

The 5D action for a scalar field Phi(x, phi) with Kaluza-Klein
expansion Phi(x, phi) = sum_n Phi_n(x) e^{in phi/R_0} decomposes as:

    S_{5D}[Phi] = (2 pi R_0) integral d^4x sqrt{g_{4D}} sum_n [
        (1/2) g^{mu nu}_{4D} partial_mu Phi_n partial_nu Phi_n^*
        + (1/2)(n/R_0)^2 |Phi_n|^2
    ]

The KK mass n/R_0 arises from the S^1 factor. The 4D dynamics
(propagation in the curved background) and the S^1 dynamics (the mode
number n, i.e., the e-charge) are separated. Interaction vertices
inherit this factorization: the phi-dependence is absorbed entirely
into the KK mode expansion, and the e-charge is carried by the mode
number n, which is determined by the S^1 geometry alone.

### B.3.3 Why the product structure is exact

The metric has the form g_{5D} = g_{4D}(x) + R_0^2 dphi^2. This is
a warped product with trivial warp factor (i.e., a direct product).
The constancy of R_0 is guaranteed by three independent results:

1. **Modulus stabilization** (Paper 1, Section 2.1): R is fixed by the
   Casimir potential. Fluctuations of R are massive (m ~ 1/R), and
   at energies below 1/R the radius is frozen.

2. **Z_2 orbifold symmetry** (Paper 1, Section 2.1): The e-circle has
   a phi -> -phi symmetry. This forbids any phi-dependent deformation
   of the 4D metric.

3. **The Killing vector** (Paper 3, Section 9.3.2): d/dphi is an
   exact Killing vector of the 5D metric. The product structure is
   exact: the 4D geometry can curve arbitrarily --- black hole,
   cosmological, or otherwise --- without affecting the S^1 factor.

---

## B.4 Kaluza-Klein Decomposition and S^1 Fourier Orthogonality

The KK expansion on S^1 relies on the orthonormality of Fourier modes:

    integral_0^{2 pi R_0} e^{i(n-m) phi / R_0} dphi
        = 2 pi R_0  delta_{nm}

This identity depends only on the S^1 geometry --- the circumference
2 pi R_0 and the topological quantization of the mode numbers n, m
in Z. It does not reference the 4D metric g_{4D}(x) in any way.

The identity is *topological*: it follows from the compactness of S^1
and the single-valuedness of the mode functions. No metric deformation
of M^4 --- including a black hole singularity --- can modify the S^1
orthogonality integral.

---

## B.5 Ward Identity Factorization

### B.5.1 The Ward identity in 5D

The U(1) e-translation symmetry phi -> phi + alpha is an exact
symmetry of S_{5D}. By Noether's theorem (Paper 1, Theorem 2.1), the
associated current is covariantly conserved:

    nabla_mu J^mu_e = 0

In the quantum theory, this becomes the Ward-Takahashi identity: for
any correlator involving the e-current and n fields,

    partial_{x^mu} <J^mu_e(x) Phi_1(y_1) ... Phi_n(y_n)>
        = sum_i q_i delta(x - y_i)
          <Phi_1(y_1) ... Phi_n(y_n)>

where q_i is the e-charge of field Phi_i.

### B.5.2 Why the factorization holds in the black hole background

The vertex factor for e-charge conservation at an interaction point is
the matrix element of the e-charge operator Q_e at the vertex. In the
KK decomposition:

    <n_out | V_e | n_in> = delta_{n_out, n_in}

This Kronecker delta was derived using only:

(a) The KK expansion, which requires the product structure
g_{5D} = g_{4D} + R_0^2 dphi^2. **Established in Section B.3.**

(b) The orthonormality of S^1 modes (Section B.4). This depends only
on the S^1 geometry, not on g_{4D}.

(c) The e-symmetry of the action, which is exact because S_{5D} is
phi-independent. **Established in Section B.3.2.**

None of these ingredients reference the 4D metric. Specifically:
- (a) holds for *any* g_{4D}, including Schwarzschild
- (b) is a property of S^1 alone
- (c) follows from the product structure

Therefore the vertex factor for e-charge conservation is independent
of the 4D geometry.

---

## B.6 Proof of Proposition B.1

**Step A (KK decomposition).** The product metric ensures that the 5D
field decomposes as:

    Phi(x, phi) = (1/sqrt{2 pi R_0}) sum_n Phi_n(x) e^{in phi/R_0}

with each Phi_n(x) satisfying a 4D equation of motion on (M^4, g_{4D})
with mass m_n^2 = n^2/R_0^2 plus the 4D curvature coupling. The
decomposition is exact because the 5D Laplacian separates:

    Box_{5D} = Box_{4D} + (1/R_0^2) partial^2/partial phi^2

and the S^1 eigenfunctions diagonalize the second term regardless of
g_{4D}.

**Step B (Vertex structure).** Any interaction vertex in the 5D theory
(cubic, quartic, or higher) contains a phi-integral:

    integral_0^{2 pi R_0} dphi  e^{i(n_1 + n_2 + ... + n_k) phi/R_0}
        = 2 pi R_0  delta_{n_1 + n_2 + ... + n_k, 0}

This is the KK selection rule --- an exact identity from the Fourier
orthogonality on S^1. It holds for any vertex, at any spacetime point
x in M^4, regardless of the local curvature.

**Step C (Independence from g_{4D}).** The Kronecker delta in Step B
depends on the S^1 circumference 2 pi R_0 (constant) and the mode
numbers n_i (integers, topologically quantized). It does not depend
on the metric g_{4D}(x), the curvature R_{mu nu} at the horizon, or
whether the vertex is in flat space, near a singularity, or on the
horizon. The vertex factor is determined by the S^1 topology alone.

**Step D (Ward identity protection).** The Ward identity for the
e-current in the product spacetime reads (after phi integration):

    partial_mu (sqrt{g_{4D}} J^mu_{e,4D}(x)) = 0

This constrains the vertex factor to be exactly 1 (for
charge-conserving vertices) at all orders in perturbation theory:

1. *Tree level:* vertex = 1 by the classical Noether theorem.

2. *Loop level:* The Ward identity forbids radiative corrections to
   the vertex that would modify e-charge conservation. This is the
   standard non-renormalization of a conserved current vertex (the
   analog of Z_1 = Z_2 in QED).

3. *Non-perturbatively:* The gauge symmetry phi -> phi + alpha cannot
   be broken (Paper 3, Section 9.3.2), so the Ward identity holds
   exactly.

**QED.** The vertex factor is identically 1 in the black hole
background.

---

## B.7 The 4D Vertex Carries No e-Charge Dependence

The factorization produces a 4D vertex factor V_{4D} describing the
dynamics of the KK modes Phi_n(x) in the curved 4D background. This
V_{4D} depends on g_{4D}, on the masses m_n = n/R_0, and on the 4D
coupling constants. But it carries no e-charge selection rule --- that
selection rule resides entirely in the S^1 Kronecker delta.

Formally: V_{4D} is a 4D observable constructed from g_{4D} and the
4D fields Phi_n. By the superselection property (Paper 3, Section
9.3.1, Property 2):

    [Q_e, O_{4D}] = 0

the 4D vertex commutes with Q_e and therefore cannot generate or
absorb e-charge. All e-charge dynamics reside in the S^1 factor, which
is topology-determined and g_{4D}-independent.

---

## B.8 Note on the Planck-Scale Regime

For an evaporating black hole at very late times (M -> M_Pl), the
semi-classical description breaks down in the 4D sector. The vertex
factor derivation (Steps B--C) depends only on the S^1 sector, not
on g_{4D}. Even if g_{4D} is singular, the S^1 orthogonality integral
remains well-defined. The vertex factor delta_{n,m} is a topological
statement about the S^1 fiber and survives even when the base manifold
M^4 degenerates.

However, the physical interpretation of the vertex (an infalling
quantum absorbed by the horizon) relies on the semi-classical horizon
picture. At M ~ M_Pl, the horizon itself is not well-defined
classically. The mathematical result (vertex = 1) is unconditional;
the physical application to the information paradox requires M >> M_Pl,
which is the regime where the AMPS argument itself is stated.

---

## B.9 Proof Chain

| # | Statement | Status | Source |
|---|-----------|--------|--------|
| B.1 | In flat 5D: e-conservation vertex = 1 (exact) | **Proved** | Paper 1, Theorem 2.1 (Noether) |
| B.2 | 5D BH metric is M^4 x S^1 with R_0 constant | **Proved** | Paper 3, Section 3.4; modulus stabilization (Paper 1) |
| B.3 | d/dphi is exact Killing vector of 5D BH metric | **Proved** | Paper 3, Section 9.3.2 |
| B.4 | Covariant conservation nabla_mu J^mu_e = 0 in BH background | **Proved** | Killing vector theorem (Paper 3, Section 9.3.2) |
| B.5 | Q_e is superselection charge: [Q_e, O_{4D}] = 0 | **Proved** | Paper 3, Section 9.3.1 |
| B.6 | 5D action factorizes into 4D and S^1 sectors | **Proved** | Product metric structure (Section B.3) |
| B.7 | Ward identity factorizes: vertex = V_{4D} x V_{S^1} | **Proved** | From B.6 (Section B.5) |
| B.8 | V_{S^1} = 1 identically (S^1 unaffected by BH) | **Proved** | From B.2 + Fourier orthogonality (Section B.4) |
| B.9 | V_{4D} carries no e-charge dependence | **Proved** | From B.5 (Section B.7) |
| B.10 | Horizon vertex factor = 1 in BH background | **Derived** | Steps A--D (Section B.6) |
| B.11 | Theorem 9.1 is unconditional | **Derived** | B.10 closes the remaining assumption |

---

## B.10 References

- Almheiri, A., Marolf, D., Polchinski, J. & Sully, J. "Black holes:
  complementarity vs. firewalls." *JHEP* 02, 062 (2013). --- The AMPS
  argument.
- Noether, E. "Invariante Variationsprobleme." *Nachr. Ges. Wiss.
  Goettingen* 235--257 (1918). --- Conservation law from symmetry.
- Peskin, M. E. & Schroeder, D. V. *An Introduction to Quantum Field
  Theory.* Westview Press (1995). --- Ward-Takahashi identity and
  Z_1 = Z_2.
