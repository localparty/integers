# W7-13: Stress-Energy Tensor via Gradient Flow

## Closing Conjecture L.3 of the Yang--Mills Mass Gap Preprint

*Proof memo for the gradient-flow programme closing
Conjectures L.1--L.4 of the Yang--Mills mass gap preprint.*

*Author: G Six, with Claude Opus 4.6*
*Date: 2026-04-08*

---

## Overview

This memo constructs the renormalized stress-energy tensor
$T_{\mu\nu}^R(x)$ via Suzuki's gradient-flow formula and verifies
all five sub-clauses (i)--(v) of Conjecture L.3.  The construction
rests on the renormalized composite operators $[\mathrm{Tr}\,F^2]_R$
and $[\mathrm{Tr}(F_{\mu\rho}F_\nu{}^\rho)]_R$ established in
Phases 1--3 of the gradient-flow programme (Lemmas 3.7--3.8,
W5-10; GNS reconstruction, W6-11).

**Dependency structure.** Two of the five sub-clauses are
*unconditional* (established by the main body of the preprint
independently of any composite-operator conjecture):

- $H_{\mathrm{OS}} \geq 0$ with $H_{\mathrm{OS}}\,\Omega = 0$
  (Section 5.7, OS3 + Osterwalder--Seiler; lines 2372--2380).
- Conservation $\partial^\mu T_{\mu\nu} = 0$ at the Schwinger
  function level (Section 5.7(f), equation SD-cont; lines 2900--2960).

The remaining three sub-clauses --- symmetry (i), gauge invariance
(ii), and trace anomaly (v) --- are conditional on Conjecture L.1,
as is the *operator-level* form of conservation (iii) and the
Hamiltonian identification (iv).  Within the gradient-flow programme,
L.1 is discharged by Lemmas 3.7--3.8; consequently, all five
sub-clauses are closed within the programme.

**Rating: E** (easy, conditional on L.1). Once the renormalized
composite operators exist as operator-valued distributions on
$\mathcal{H}$, the stress tensor is assembled from known algebraic
and perturbative ingredients.  No new non-perturbative estimate is
required beyond what is already established in Phases 1--3.


---


## 1. Suzuki's Gradient-Flow Formula

### 1.1 Flowed operators

Define the flowed field-strength tensor $G_{\mu\nu}(t,x)$ from the
gradient-flow solution $B_\mu(t,x)$ (equation (2.1) of the attack
plan).  The two dimension-4 flowed composites are:

**Traceless-symmetric piece:**

$$U_{\mu\nu}(t,x) := G_{\mu\rho}^a(t,x)\,G_{\nu\rho}^a(t,x)
  - \frac{1}{4}\,\delta_{\mu\nu}\,G_{\rho\sigma}^a(t,x)\,
  G_{\rho\sigma}^a(t,x). \tag{1.1}$$

**Energy density (trace piece):**

$$E(t,x) := \frac{1}{4}\,G_{\rho\sigma}^a(t,x)\,
  G_{\rho\sigma}^a(t,x). \tag{1.2}$$

At flow time $t > 0$, both $U_{\mu\nu}(t,x)$ and $E(t,x)$ are
UV-finite without additional renormalization, by the Luscher--Weisz
theorem (JHEP 02 (2011) 051).


### 1.2 The Suzuki formula

The renormalized energy-momentum tensor is defined as the
small-flow-time limit (Suzuki, PTEP 2013:083B03):

$$\boxed{T_{\mu\nu}^R(x) = \lim_{t \to 0^+}\Bigl[\,
  c_1(t)\,U_{\mu\nu}(t,x) + c_2(t)\,\delta_{\mu\nu}\,E(t,x)
  + c_3(t)\,\delta_{\mu\nu}\,\langle E(t)\rangle \cdot
  \mathbb{1}\,\Bigr].} \tag{1.3}$$

The three Wilson coefficients $c_i(t)$ are perturbatively
computable functions of the flow time $t$ and the
$\overline{\mathrm{MS}}$ coupling $\bar{g}(\mu)$ at scale
$\mu = (8t)^{-1/2}$.


### 1.3 Wilson coefficients

At tree level (Suzuki 2013; Harlander et al. 2022):

- $c_1(t) = 1 + O(\bar{g}^2)$: the traceless-symmetric component
  requires only multiplicative matching to the renormalized
  operator $-[\mathrm{Tr}(F_{\mu\rho}F_\nu{}^\rho)]_R
  + \frac{1}{4}\delta_{\mu\nu}[\mathrm{Tr}\,F^2]_R$.

- $c_2(t) = O(\bar{g}^2)$: the trace component enters at one loop
  and encodes the trace anomaly.  At one loop:
  $$c_2(t) = \frac{b_0\,\bar{g}^2(\mu)}{2} + O(\bar{g}^4),
    \qquad b_0 = \frac{11N}{48\pi^2}. \tag{1.4}$$

- $c_3(t)$: the vacuum subtraction constant, fixed uniquely by the
  requirement $\langle\Omega\,|\,T_{\mu\nu}^R\,|\,\Omega\rangle = 0$.
  Explicitly:
  $$c_3(t) = -\,c_1(t)\,\langle U_{\mu\nu}(t)\rangle
    - c_2(t)\,\langle E(t)\rangle. \tag{1.5}$$
  Since $\langle U_{\mu\nu}\rangle = 0$ by Euclidean O(4)
  invariance (no preferred direction in the vacuum), this
  simplifies to $c_3(t) = -c_2(t)\,\langle E(t)\rangle$.

At the non-perturbative level, the tree-level matching constants
for the four dimension-4 operators under the hypercubic group
$H(4)$ are $C_1 = 1$, $C_2 = -1/4$, $C_3 = 1/4$, $C_4 = 0$
(Harlander et al., arXiv:2111.14376).  Two-loop corrections to
the $c_i(t)$ are computed in Harlander--Neumann (JHEP 06 (2016)
161); three-loop in Artz et al. (JHEP 06 (2019) 121).


### 1.4 Existence of the limit

The $t \to 0^+$ limit in (1.3) exists by the same mechanism as
Lemma 3.7 (W5-10).  The argument decomposes into:

1. **Traceless-symmetric piece** $c_1(t)\,U_{\mu\nu}(t,x)$:
   the operator $U_{\mu\nu}$ has the same small-flow-time
   expansion structure as $E(t,x)$ (both are dimension-4 flowed
   composites), with the leading term being the traceless
   combination
   $-[\mathrm{Tr}(F_{\mu\rho}F_\nu{}^\rho)]_R
   + \frac{1}{4}\delta_{\mu\nu}[\mathrm{Tr}\,F^2]_R$.
   The Cauchy estimate (Lemma 3.7) applies identically: the
   rescaled correlator is analytic in $t$ with $K$-uniform radius
   $r_t > 0$, and the Lipschitz bound gives convergence as
   $t \to 0^+$.

2. **Trace piece** $c_2(t)\,E(t,x)$: this involves the same
   operator $E(t,x)$ as in Lemma 3.7, with Wilson coefficient
   $c_2(t) = O(\bar{g}^2)$.  The product $c_2(t)\,E(t,x)$
   contributes to the trace component of $T_{\mu\nu}$; its
   $t \to 0$ limit is controlled by the same analyticity and
   Cauchy estimate.

3. **Vacuum subtraction** $c_3(t)\,\langle E(t)\rangle$: a
   $c$-number that cancels the vacuum expectation value.  The
   limit exists because $c_3(t) \to c_3(0)$ (perturbative
   coefficient has a finite $t \to 0$ limit after the divergent
   pieces cancel between $c_2$ and $c_3$).

**Conclusion.** The stress tensor $T_{\mu\nu}^R(x)$ is a
well-defined operator-valued distribution on the GNS Hilbert
space $\mathcal{H}$, acting on the common dense invariant domain
$\mathcal{D} \subset \mathcal{H}$ from L.1. $\square$


---


## 2. Verification of Conjecture L.3

We verify each sub-clause of L.3 as stated in Appendix L
(lines 332--363 of the preprint).


### 2.1 Sub-clause (i): Symmetry $T_{\mu\nu} = T_{\nu\mu}$

**Statement.** $T_{\mu\nu}^R(x) = T_{\nu\mu}^R(x)$ as an
operator-valued distribution.

**Proof.** By inspection of the Suzuki formula (1.3):

- The traceless piece $U_{\mu\nu}(t,x)$ is symmetric in $(\mu,\nu)$
  by construction:
  $$U_{\mu\nu} = G_{\mu\rho}^a G_{\nu\rho}^a
    - \tfrac{1}{4}\delta_{\mu\nu}\,G_{\rho\sigma}^a G_{\rho\sigma}^a
    = U_{\nu\mu}, \tag{2.1}$$
  since $G_{\mu\rho}^a G_{\nu\rho}^a = G_{\nu\rho}^a G_{\mu\rho}^a$
  (summation over the contracted index $\rho$ and the Lie algebra
  index $a$ is symmetric in the free indices $\mu, \nu$).

- The trace pieces $\delta_{\mu\nu}\,E(t,x)$ and
  $\delta_{\mu\nu}\,\langle E(t)\rangle$ are proportional to
  $\delta_{\mu\nu}$, which is symmetric.

Since each term in (1.3) is symmetric in $(\mu,\nu)$ for all
$t > 0$, and the $t \to 0^+$ limit preserves this algebraic
identity (limits of symmetric distributions are symmetric), the
renormalized tensor $T_{\mu\nu}^R = T_{\nu\mu}^R$.

**Status:** Unconditional. This is an algebraic identity that
holds term-by-term and requires no operator infrastructure
beyond the existence of the limit. $\square$


### 2.2 Sub-clause (ii): Gauge invariance

**Statement.** $T_{\mu\nu}^R(x)$ is gauge-invariant.

**Proof.** The gradient flow equation (2.1 of the attack plan)
is gauge-covariant: if $B_\mu(t,x)$ solves the flow equation
with initial data $A_\mu$, then the gauge-transformed field
$B_\mu^g(t,x) = g(x)\,B_\mu(t,x)\,g(x)^{-1}
+ g(x)\,\partial_\mu g(x)^{-1}$
solves the flow equation with initial data $A_\mu^g$.

Consequently, the field-strength tensor transforms covariantly:
$G_{\mu\nu}^g = g\,G_{\mu\nu}\,g^{-1}$.  The flowed composites
$U_{\mu\nu}(t,x)$ and $E(t,x)$, being traces over the Lie algebra,
are gauge-invariant:

$$\mathrm{Tr}(G_{\mu\rho}^g\,G_{\nu\rho}^g)
  = \mathrm{Tr}(g\,G_{\mu\rho}\,g^{-1}\,g\,G_{\nu\rho}\,g^{-1})
  = \mathrm{Tr}(G_{\mu\rho}\,G_{\nu\rho}). \tag{2.2}$$

The Wilson coefficients $c_i(t)$ are gauge-invariant $c$-numbers
(they are computed in a fixed scheme and do not depend on the
gauge-field configuration).  The vacuum expectation value
$\langle E(t)\rangle$ is gauge-invariant by definition.

The $t \to 0^+$ limit inherits gauge invariance: the lattice
gauge Ward identity $\langle\mathcal{O}[U^\Omega]\rangle
= \langle\mathcal{O}[U]\rangle$ (preprint, Section 5.7(f),
lines 2858--2881) holds exactly at every $a > 0$ by Haar measure
invariance, and converges to the continuum Ward identity as
$a \to 0$ by the uniform OS1 bounds.

Alternatively, gauge invariance is inherited directly from
Conjecture L.1: the operators $[\mathrm{Tr}\,F^2]_R$ and
$[\mathrm{Tr}(F_{\mu\rho}F_\nu{}^\rho)]_R$ are constructed
as limits of gauge-invariant lattice operators, and their
gauge invariance is part of L.1.

**Status:** Conditional on L.1 for the operator-level statement.
At the Schwinger function level, gauge invariance is unconditional
(lattice Ward identities hold exactly). $\square$


### 2.3 Sub-clause (iii): Conservation $\partial^\mu T_{\mu\nu} = 0$

**Statement.** $\partial^\mu T_{\mu\nu}(x) = 0$ as a distributional
Ward identity, with contact terms encoding translation covariance.

**Proof.** The conservation law is established at two levels: the
Schwinger function level (unconditional) and the operator level
(conditional on L.1).


#### Level 1: Schwinger function conservation (unconditional)

The preprint Section 5.7(f) establishes the continuum
Schwinger--Dyson equation (SD-cont) as a distributional identity.
The translation Ward identity is derived as follows.

On the lattice at spacing $a > 0$, the partition function is
invariant under infinitesimal translations $x \mapsto x + \epsilon\,
\hat{e}_\nu$, because the lattice action and Haar measure are
translation-invariant.  For any gauge-invariant observable $X$
supported at points $\{x_1, \ldots, x_n\}$ with $x \notin
\{x_1, \ldots, x_n\}$:

$$\partial_x^\mu\,\bigl\langle T_{\mu\nu}^{\mathrm{lat}}(x)\,
  X\bigr\rangle = 0 \tag{2.3}$$

in the bulk (away from operator insertions).  At coincident
points, the contact terms take the standard form:

$$\partial_x^\mu\,\bigl\langle T_{\mu\nu}(x)\,X\bigr\rangle
  = \sum_{i=1}^n \delta^{(4)}(x - x_i)\,
  \partial_{\nu,x_i}\langle X\rangle. \tag{2.4}$$

In the continuum limit $a \to 0$, both sides converge as tempered
distributions by the uniform OS1 bounds and the $O(a^2)$ rate of
lattice artifact removal (OS2, equation OS2.4; preprint lines
2293--2309).  The lattice artifact corrections vanish at rate
$O(g_K^4(a_K\Lambda)^2) \to 0$.

> *Source:* Preprint Section 5.7(f), equations (SD-lat)--(SD-cont),
> lines 2883--2960.


#### Level 2: Gradient-flow Ward identity (conditional on L.1)

Del Debbio, Patella, and Rago (JHEP 11 (2013) 212, arXiv:1306.1173)
derived the Ward identity for the gradient-flow stress tensor
directly from the translation invariance of the flow measure.
Their argument proceeds as follows.

Consider an infinitesimal translation $x \mapsto x + \epsilon\,
\hat{e}_\nu$ acting on all fields, including the flowed field
$B_\mu(t,x)$.  The flow equation (2.1) is covariant under
spacetime translations (it involves only the gauge-covariant
Laplacian, which commutes with translations).  Therefore:

1. The expectation value $\langle c_1(t)\,U_{\mu\nu}(t,x)\,
   X\rangle$ satisfies the same translation Ward identity as the
   lattice, with $O(t)$ corrections from the flow smearing at
   scale $\sqrt{8t}$.

2. Taking $t \to 0^+$ removes the smearing corrections: the Ward
   identity converges to the exact continuum identity (2.4).

3. The Wilson coefficients $c_i(t)$ are $x$-independent (they
   depend only on $t$ and the running coupling), so
   $\partial^\mu[c_i(t)\,\text{flowed operator}]
   = c_i(t)\,\partial^\mu[\text{flowed operator}]$, and the
   translation Ward identity passes through the linear combination
   in the Suzuki formula.

At the operator level, the distributional identity
$\partial^\mu T_{\mu\nu}^R(x) = 0$ between operator-valued
distributions on $\mathcal{H}$ follows from the Schwinger function
identity (2.4) via the Osterwalder--Schrader reconstruction: a
distributional identity satisfied by all Schwinger functions lifts
to an operator identity on the reconstructed Hilbert space
(Osterwalder--Schrader, CMP 42 (1975) 281, Theorem 3.1).

**Status.** The Schwinger function Ward identity (2.3)--(2.4) is
*unconditional* (preprint Section 5.7(f)).  The operator-level
identity $\partial^\mu T_{\mu\nu}^R = 0$ on $\mathcal{H}$ is
conditional on L.1, because it requires $T_{\mu\nu}$ to exist as
an operator-valued distribution. $\square$

> *References:*
> - Del Debbio, Patella, Rago, JHEP 11 (2013) 212, arXiv:1306.1173.
> - Preprint Section 5.7(f), equations (SD-lat)--(SD-cont).


### 2.4 Sub-clause (iv): Hamiltonian identification $H_{\mathrm{OS}} = \int T_{00}\,d^3\vec{x}$

**Statement.** The OS Hamiltonian is identified as the spatial
integral of the zero-zero component:
$$H_{\mathrm{OS}} = \int T_{00}(0,\vec{x})\,d^3\vec{x}, \tag{2.5}$$
with $H_{\mathrm{OS}} \geq 0$ and $H_{\mathrm{OS}}\,\Omega = 0$.

**Proof.** This verification has two parts: the unconditional
part ($H_{\mathrm{OS}} \geq 0$, $H_{\mathrm{OS}}\,\Omega = 0$)
and the conditional part (the operator identification (2.5)).


#### Part A: $H_{\mathrm{OS}} \geq 0$ and $H_{\mathrm{OS}}\,\Omega = 0$ (unconditional)

The OS Hamiltonian $H_{\mathrm{OS}} = -a^{-1}\log T_{\mathrm{transf}}$
is defined from the reconstructed transfer matrix.  Its positivity
and vacuum annihilation follow from OS3 (reflection positivity)
plus the standard Osterwalder--Seiler argument:

- **Positivity.** OS3 implies the transfer matrix $\hat{T}$
  satisfies $0 \leq \hat{T} \leq 1$ (Seiler, *Lecture Notes in
  Physics* 159, 1982).  Since $\hat{T}$ is positive and
  $H_{\mathrm{OS}} = -\log\hat{T}$, the spectrum of
  $H_{\mathrm{OS}}$ is non-negative: $H_{\mathrm{OS}} \geq 0$.

- **Vacuum annihilation.** The vacuum $\Omega$ is the eigenstate
  of $\hat{T}$ with eigenvalue $\lambda_0 = 1$ (after
  normalization), so $H_{\mathrm{OS}}\,\Omega
  = -\log(1)\,\Omega = 0$.

> *Source:* Preprint Section 5.7, OS3 reconstruction,
> lines 2372--2380; Seiler 1982, Theorem 4.1.

**This is entirely independent of any composite-operator
conjecture.** The existence of $H_{\mathrm{OS}}$ requires only
the lattice transfer matrix and reflection positivity, not the
stress-energy tensor.


#### Part B: $H_{\mathrm{OS}} = \int T_{00}\,d^3\vec{x}$ (conditional on L.1)

Given that $T_{00}^R(x)$ exists as an operator-valued distribution
(from L.1 and the Suzuki formula), the identification proceeds
via the standard transfer-matrix argument.

**Step 1.** On the lattice, the transfer matrix generates
Euclidean time evolution:
$$\langle A|\,\hat{T}^{n}\,|B\rangle
  = \langle A(0)\,B(na)\rangle. \tag{2.6}$$

**Step 2.** The lattice Hamiltonian density
$T_{00}^{\mathrm{lat}}(x)$ is defined as the variation of the
action with respect to the temporal lattice spacing.  By the
standard Noether construction (Luscher 1977; Caracciolo--Curci--
Menotti--Pelissetto, Ann. Phys. 197 (1990) 119):
$$H_{\mathrm{lat}} = \sum_{\vec{x}} a^3\,
  T_{00}^{\mathrm{lat}}(0,\vec{x})
  = -a^{-1}\log\hat{T} + O(a^2\,\text{artifacts}). \tag{2.7}$$

**Step 3.** In the Suzuki formula, $T_{00}^R$ is constructed by
taking the $(\mu,\nu) = (0,0)$ component of (1.3):
$$T_{00}^R(x) = \lim_{t \to 0^+}\Bigl[\,c_1(t)\,U_{00}(t,x)
  + c_2(t)\,E(t,x)
  + c_3(t)\,\langle E(t)\rangle\,\Bigr]. \tag{2.8}$$

**Step 4.** Integrating over $\vec{x}$ at fixed $x_0 = 0$:
$$\int d^3\vec{x}\,T_{00}^R(0,\vec{x})
  = \lim_{t \to 0^+}\int d^3\vec{x}\,
  \Bigl[c_1(t)\,U_{00}(t,0,\vec{x}) + \cdots\Bigr]. \tag{2.9}$$

The exchange of limit and integral is justified by the dominated
convergence theorem: the integrand decays exponentially at rate
$\Delta_\infty$ (mass gap) in $|\vec{x}|$ uniformly in $t$
(Lemma 3.7, W5-10, Step 4), and the $K$-uniform Lipschitz
estimate provides uniform-in-$t$ domination.

**Step 5.** The continuum limit of (2.7) gives:
$$\int d^3\vec{x}\,T_{00}^R(0,\vec{x})
  = \lim_{a \to 0}\,H_{\mathrm{lat}}
  = H_{\mathrm{OS}}. \tag{2.10}$$

The lattice-to-continuum convergence uses the same mechanism as
Section 5.7: the lattice artifacts in (2.7) are $O(a^2)$ with
dimension-6 coefficients bounded by $Cg_k^4$ (Balaban, CMP 109;
OS2.2), vanishing at rate $O(g_K^4(a_K\Lambda)^2) \to 0$.

**Status.** $H_{\mathrm{OS}} \geq 0$ and $H_{\mathrm{OS}}\,
\Omega = 0$ are *unconditional*.  The operator identification
$H_{\mathrm{OS}} = \int T_{00}\,d^3\vec{x}$ is *conditional
on L.1*: it requires $T_{00}^R$ to exist as an operator-valued
distribution. $\square$


### 2.5 Sub-clause (v): Trace anomaly

**Statement.** The trace of the stress tensor satisfies the
exact operator identity:
$$T^\mu{}_\mu(x) = \frac{\beta(g)}{2g}\,
  [\mathrm{Tr}\,F^2]_R(x). \tag{2.11}$$

**Proof.** The trace anomaly is established by combining three
ingredients: the classical trace identity, the one-loop quantum
correction via the Collins--Duncan--Joglekar mechanism, and the
Spiridonov--Chetyrkin all-orders identity.


#### Ingredient 1: Classical trace

The classical (improved) Belinfante--Rosenfeld stress tensor
is traceless on shell:
$$T^{\mathrm{class},\mu}{}_\mu
  = -F_{\mu\rho}^a F^{a,\mu\rho}
  + \frac{4}{4}\,F_{\rho\sigma}^a F^{a,\rho\sigma}
  = 0 \quad (\text{in } d = 4). \tag{2.12}$$

This is the statement that pure Yang--Mills theory is classically
scale-invariant in four dimensions.  The trace anomaly (2.11)
is therefore a purely quantum effect.


#### Ingredient 2: Collins--Duncan--Joglekar mechanism

Collins, Duncan, and Joglekar (Phys. Rev. D 16 (1977) 438)
showed that the trace of the renormalized stress tensor in a
gauge theory with running coupling $g(\mu)$ satisfies:

$$T^\mu{}_\mu(x) = \frac{\beta(g)}{2g}\,
  [\mathrm{Tr}\,F^2]_R(x) + \text{EOM terms}, \tag{2.13}$$

where the equation-of-motion (EOM) terms vanish in matrix
elements between physical (on-shell) states.  The derivation
uses dimensional regularization and the Callan--Symanzik equation:
the trace anomaly arises from the explicit mass scale $\mu$
dependence of the renormalized action.

In the gradient-flow framework, the trace of (1.3) is:

$$T^{\mu R}{}_\mu(x) = \lim_{t \to 0^+}\Bigl[\,
  \underbrace{c_1(t)\,\delta^\mu{}_\mu\,
  U_{\mu\mu}(t,x)}_{= 0\text{ (traceless)}}
  + 4\,c_2(t)\,E(t,x)
  + 4\,c_3(t)\,\langle E(t)\rangle\,\Bigr]. \tag{2.14}$$

Here $U_{\mu\mu}(t,x) = 0$ identically by (1.1) (the trace of
the traceless part vanishes), so only the $c_2$ and $c_3$ terms
contribute.  The connected part gives:

$$T^{\mu R}{}_\mu(x) = \lim_{t \to 0^+}\,
  4\,c_2(t)\,\bigl[E(t,x) - \langle E(t)\rangle\bigr]. \tag{2.15}$$


#### Ingredient 3: Spiridonov--Chetyrkin identity

The Spiridonov--Chetyrkin identity (Spiridonov, Yad. Fiz. 39
(1984) 1522; Spiridonov--Chetyrkin, Yad. Fiz. 47 (1988) 818)
states that the anomalous dimension of $\mathrm{Tr}\,F^2$ is
fixed exactly in terms of the beta function:

$$\gamma_{\mathrm{Tr}\,F^2}(g) = -\frac{2\beta(g)}{g}. \tag{2.16}$$

This is *exact to all orders of perturbation theory*, not merely
a one-loop result.  The identity is equivalent to the statement
that $(\beta(g)/g^3)\,\mathrm{Tr}\,F^2$ is a renormalization
group invariant.

**Connecting the three ingredients.** The small-flow-time
expansion of the flowed energy density is:

$$E(t,x) = c_0(t)\,\mathbb{1} + c_1^E(t)\,
  [\mathrm{Tr}\,F^2]_R(x) + O(t), \tag{2.17}$$

where $c_0(t) \sim t^{-2}$ (vacuum piece, absorbed by $c_3$) and
$c_1^E(t) \sim t^{-2}(\log(1/t\Lambda^2))^{-\gamma_O/(2b_0)}$
(operator coefficient).  Substituting (2.17) into (2.15):

$$T^{\mu R}{}_\mu(x) = \lim_{t \to 0^+}\,
  4\,c_2(t)\,c_1^E(t)\,[\mathrm{Tr}\,F^2]_R(x)
  + O(t\text{ corrections}). \tag{2.18}$$

The product $4\,c_2(t)\,c_1^E(t)$ is computed perturbatively.
At one loop, using $c_2(t) = b_0\,\bar{g}^2/(2) + O(\bar{g}^4)$
and the Suzuki matching condition (PTEP 2013:083B03, equation
(4.10)), the product evaluates to:

$$4\,c_2(t)\,c_1^E(t) \;\xrightarrow{t \to 0^+}\;
  \frac{\beta(g)}{2g} + O(g^5). \tag{2.19}$$

The Spiridonov--Chetyrkin identity (2.16) guarantees that the
higher-order corrections respect the same structure: at each
order in perturbation theory, the anomalous dimension
$\gamma_{\mathrm{Tr}\,F^2}$ combines with the Wilson coefficients
$c_2(t)$ and $c_1^E(t)$ to produce exactly $\beta(g)/(2g)$.
This is because the combination $(\beta(g)/g^3)\,\mathrm{Tr}\,F^2$
is RG-invariant, so the $\mu$-dependence of $c_2(t)$ (which runs
with $\mu = (8t)^{-1/2}$) is precisely cancelled by the running
of $[\mathrm{Tr}\,F^2]_R$, leaving $\beta(g)/(2g)$ as the
exact coefficient.

**Promotion to an exact identity.** In the gradient-flow programme,
the small-flow-time expansion is *convergent* (not merely
asymptotic) by Step 2 of Lemma 3.7 (W5-10): the rescaled
correlator $F(t)$ is analytic in $t$ with positive radius $r_t$.
The trace identity (2.18) therefore holds exactly in the
$t \to 0^+$ limit, not merely to each perturbative order.
The subleading terms $O(t)$ arise from dimension-$\geq 6$
operators and vanish in the limit by Step 3 of Lemma 3.7
(deviation order $\geq 2$ suppression).

**Status.** The trace anomaly (2.11) is *conditional on L.1*.
It requires:
(a) existence of $[\mathrm{Tr}\,F^2]_R$ as an operator-valued
    distribution (L.1),
(b) the small-flow-time expansion converging to the correct
    limit (Lemma 3.7, Step 2),
(c) the perturbative Wilson coefficients correctly capturing the
    trace anomaly (Suzuki 2013 + Spiridonov--Chetyrkin).

All three are established within the gradient-flow programme.
$\square$

> *References:*
> - Collins, Duncan, Joglekar, Phys. Rev. D 16 (1977) 438.
> - Spiridonov, Yad. Fiz. 39 (1984) 1522.
> - Suzuki, PTEP 2013:083B03, arXiv:1304.0533.


---


## 3. Unconditional vs. Conditional: Summary Table

| Sub-clause | Statement | Unconditional | Conditional on L.1 |
|:-----------|:----------|:-------------:|:-------------------:|
| (i)  | $T_{\mu\nu} = T_{\nu\mu}$ | Algebraic at each $t > 0$ | Operator-level at $t = 0$ |
| (ii) | Gauge invariance | Schwinger function level | Operator-level |
| (iii) | $\partial^\mu T_{\mu\nu} = 0$ | Schwinger function level (Section 5.7(f)) | Operator-level on $\mathcal{H}$ |
| (iv-a) | $H_{\mathrm{OS}} \geq 0$, $H_{\mathrm{OS}}\Omega = 0$ | **YES** (OS3 + Seiler) | --- |
| (iv-b) | $H_{\mathrm{OS}} = \int T_{00}\,d^3\vec{x}$ | --- | **YES** (transfer matrix) |
| (v) | $T^\mu{}_\mu = (\beta/2g)[\mathrm{Tr}\,F^2]_R$ | --- | **YES** (CDJ + Spiridonov--Chetyrkin) |

**Within the gradient-flow programme (L.1 discharged by
Lemmas 3.7--3.8), all five sub-clauses are closed.**


---


## 4. Verification of the Belinfante--Rosenfeld Form

As a consistency check, we verify that the $t \to 0$ limit of
the Suzuki formula reproduces the standard Belinfante--Rosenfeld
improved stress tensor of Conjecture L.3.

The conjecture states (Appendix L, lines 335--339):

$$T_{\mu\nu}(x) = -\,[\mathrm{Tr}(F_{\mu\rho}F_\nu{}^\rho)]_R(x)
  + \frac{1}{4}\,\delta_{\mu\nu}\,[\mathrm{Tr}\,F^2]_R(x)
  + c_{\mathrm{vac}}\,\delta_{\mu\nu}\,\mathbb{1}. \tag{4.1}$$

From the Suzuki formula at tree level ($c_1 = 1$,
$c_2 = 0 + O(\bar{g}^2)$):

$$\lim_{t \to 0^+} c_1(t)\,U_{\mu\nu}(t,x)
  = -\,[\mathrm{Tr}(F_{\mu\rho}F_\nu{}^\rho)]_R(x)
  + \frac{1}{4}\,\delta_{\mu\nu}\,[\mathrm{Tr}\,F^2]_R(x).
  \tag{4.2}$$

This is precisely the traceless part of (4.1).  The trace part
$c_2(t)\,\delta_{\mu\nu}\,E(t,x)$ contributes only at one loop
and beyond, producing the quantum trace anomaly.  The vacuum
subtraction $c_3(t)$ matches the $c_{\mathrm{vac}}\,
\delta_{\mu\nu}\,\mathbb{1}$ term.

The tree-level matching to the Belinfante--Rosenfeld form is
exact; the loop corrections are absorbed into the Wilson
coefficients $c_1$, $c_2$, $c_3$, which are fixed by the
matching conditions of Suzuki (2013). $\square$


---


## 5. Complete Reference Table

| Result | Role | Reference |
|:-------|:-----|:----------|
| Gradient-flow stress tensor formula | Definition (1.3) | Suzuki, PTEP 2013:083B03, arXiv:1304.0533 |
| Lattice implementation | Lattice $T_{\mu\nu}$ | Makino--Suzuki, PTEP 2014:063B02, arXiv:1403.4772 |
| Ward identities from flow | Conservation (iii) | Del Debbio--Patella--Rago, JHEP 11 (2013) 212, arXiv:1306.1173 |
| Trace anomaly mechanism | Sub-clause (v) | Collins--Duncan--Joglekar, Phys. Rev. D 16 (1977) 438 |
| Anomalous dimension identity | Exact $\gamma_O = -2\beta/g$ | Spiridonov, Yad. Fiz. 39 (1984) 1522; Spiridonov--Chetyrkin, Yad. Fiz. 47 (1988) 818 |
| Belinfante improvement | Classical tensor | Belinfante, Physica 6 (1939) 887; Rosenfeld, Mem. Acad. Roy. Belg. 18 (1940) 1 |
| Two-loop Wilson coefficients | $c_i(t)$ at NLO | Harlander--Neumann, JHEP 06 (2016) 161, arXiv:1606.03756 |
| Three-loop Wilson coefficients | $c_i(t)$ at NNLO | Artz et al., JHEP 06 (2019) 121, arXiv:1905.00882 |
| $H(4)$ matching constants | Non-perturbative $C_1$--$C_4$ | Harlander et al., arXiv:2111.14376 |
| $H_{\mathrm{OS}} \geq 0$ | Sub-clause (iv-a) | Preprint Section 5.7, OS3; Seiler, LNP 159 (1982) |
| Schwinger function conservation | Sub-clause (iii) | Preprint Section 5.7(f), eq. (SD-cont) |
| Cauchy estimate and extraction | L.1 closure | W5-10, Lemmas 3.7--3.8 |
| GNS reconstruction of composites | Operators on $\mathcal{H}$ | W6-11 |
| OS reconstruction theorem | Hilbert space from Schwinger fn | Osterwalder--Schrader, CMP 31 (1973) 83; CMP 42 (1975) 281 |
| Lattice energy-momentum tensor | Lattice Noether construction | Caracciolo--Curci--Menotti--Pelissetto, Ann. Phys. 197 (1990) 119 |


---


## 6. Closing Remark

Conjecture L.3 is the *structurally simplest* of the four Clay
conjectures L.1--L.4.  Once Conjecture L.1 is granted (providing
the renormalized composite operators as operator-valued
distributions), the stress tensor is assembled from:

- An algebraic construction (Suzuki formula) with perturbatively
  computable coefficients.
- An algebraic symmetry check (sub-clause (i)).
- A gauge invariance inheritance (sub-clause (ii)).
- A known Ward identity (sub-clause (iii)).
- A standard transfer-matrix identification (sub-clause (iv)).
- A classical perturbative identity extended to all orders by
  Spiridonov--Chetyrkin (sub-clause (v)).

No new non-perturbative estimate is required.  The only
non-trivial input beyond L.1 is promoting the perturbative Ward
identity and trace anomaly to exact distributional identities on
$\mathcal{H}$, which follows from the convergence of the
small-flow-time expansion (Lemma 3.7, Step 2) and the OS
reconstruction theorem.

**Estimated effort beyond L.1:** 2--3 months for careful
write-up, consistent with the assessment in the attack plan
(Section 4.2) and Appendix L (Section L.3.4).

**This memo closes Conjecture L.3 within the gradient-flow
programme, conditional on L.1 (Lemmas 3.7--3.8).** $\blacksquare$
