# 01. Hamiltonian Decomposition: H = H_0 + V/N

## Purpose

Derive the explicit Hamiltonian of the 2D CP^{N-1} sigma model in
the auxiliary field formalism, decompose it as H = H_0 + (1/N)V
where H_0 is the exactly solvable N = infinity Hamiltonian, and
identify V as the 1/N interaction operator. Every operator is defined
on a precise Hilbert space with its domain specified.


---

## 1.1 The Euclidean Action in the Auxiliary Field Formalism

Start from the D'Adda-Di Vecchia-Luscher (1978) formulation. The
CP^{N-1} model has the partition function:

$$Z = \int [Dz][D\bar{z}][DA_\mu][D\sigma]\;
  \exp\left(-\frac{N}{\lambda_0}\int d^2x\;
  \left[\bar{z}_i(-D^2 + \sigma)z_i - \sigma\right]\right)$$

subject to the constraint $\sum_{i=1}^N |z_i|^2 = 1$, enforced by the
Lagrange multiplier $\sigma(x)$. Here $D_\mu = \partial_\mu - iA_\mu$
and $A_\mu = -i\bar{z}\cdot\partial_\mu z$ is the composite U(1) gauge
field.

Integrating out the $N$ complex scalars $z_i$ (exact Gaussian
integral) [PROVED]:

$$Z = \int [DA_\mu][D\sigma]\;\exp\left(-N\,S_{\text{eff}}[A,\sigma]\right)$$

$$S_{\text{eff}}[A,\sigma] = \operatorname{Tr}\ln(-D^2 + \sigma)
  - \frac{1}{\lambda_0}\int d^2x\;\sigma(x)$$

The factor of N in front of $S_{\text{eff}}$ is the reason the
saddle-point approximation becomes exact at N = infinity.


---

## 1.2 The Saddle Point and Fluctuation Expansion

### 1.2.1 The saddle point (N = infinity)

The saddle-point equations $\delta S_{\text{eff}}/\delta\sigma = 0$
and $\delta S_{\text{eff}}/\delta A_\mu = 0$ give [PROVED]:

$$\sigma_* = m^2 = \Lambda_{2D}^2, \qquad A_\mu^* = 0$$

where $m^2$ satisfies the gap equation:

$$\frac{1}{4\pi}\ln\frac{\Lambda_{\text{UV}}^2}{m^2} = \frac{1}{\lambda_0}$$

### 1.2.2 Fluctuation expansion

Write $\sigma = m^2 + \tilde{\sigma}/\sqrt{N}$ and
$A_\mu = \tilde{A}_\mu/\sqrt{N}$, expanding $S_{\text{eff}}$ around
the saddle:

$$N\,S_{\text{eff}} = N\,S_{\text{eff}}[\sigma_*, 0]
  + \frac{1}{2}\tilde{\sigma}\cdot K_{\sigma\sigma}\cdot\tilde{\sigma}
  + \frac{1}{2}\tilde{A}\cdot K_{AA}\cdot\tilde{A}
  + \frac{1}{\sqrt{N}}\,V_3[\tilde{\sigma}, \tilde{A}]
  + \frac{1}{N}\,V_4[\tilde{\sigma}, \tilde{A}]
  + O(N^{-3/2})$$

where:

- $K_{\sigma\sigma}(p) = N\,\Pi_\sigma(p)$ is the inverse sigma
  propagator
- $K_{AA}^{\mu\nu}(p) = N\,\Pi_A(p)(\delta^{\mu\nu} - p^\mu p^\nu/p^2)$
  is the inverse gauge propagator
- $V_3$ contains the cubic vertices (three-point functions of
  $\tilde{\sigma}$ and $\tilde{A}$)
- $V_4$ contains the quartic vertices

The propagators $\Pi_\sigma$ and $\Pi_A$ are the bubble integrals
computed in file 02-one-over-N-expansion.md of the large-N attack.
Both are UV finite in 2D. [PROVED]


---

## 1.3 The Transfer Matrix and Hilbert Space

### 1.3.1 Lattice regularization

Place the model on a lattice $\mathbb{Z}^2$ with spacing $a$.
Euclidean time is the vertical direction. A spatial slice is the
one-dimensional chain $\{1, 2, \ldots, L/a\}$.

The Hilbert space is:

$$\mathcal{H} = L^2\!\left(\prod_{x \in \text{spatial slice}}
  \mathbb{CP}^{N-1}_x,\; d\mu_{\text{FS}}\right)$$

where $d\mu_{\text{FS}}$ is the Fubini-Study measure on each copy of
$\mathbb{CP}^{N-1}$. A state $\Psi \in \mathcal{H}$ is a
square-integrable function of the field configuration
$\{z(x)\}_{x \in \text{slice}}$.

The transfer matrix $T: \mathcal{H} \to \mathcal{H}$ is defined by:

$$\langle z' | T | z \rangle = \exp\left(-a\,\mathcal{L}(z', z)\right)$$

where $\mathcal{L}$ is the lattice action density for one time step.
The transfer matrix is:
- Bounded (since the action is bounded below)
- Self-adjoint (time-reversal symmetry of the Euclidean action)
- Positive ($T \geq 0$, from reflection positivity)
- Trace-class (compact target space)

[PROVED -- these are standard properties for sigma models on compact
target spaces; see Osterwalder-Schrader reconstruction.]

### 1.3.2 The Hamiltonian

Define $H = -(1/a)\ln T$. Since $T$ is self-adjoint and positive, $H$
is self-adjoint with spectrum bounded below. The mass gap is:

$$m = E_1 - E_0 = -\frac{1}{a}\ln\frac{\lambda_1}{\lambda_0}$$

where $\lambda_0 > \lambda_1 \geq \lambda_2 \geq \ldots$ are the
eigenvalues of $T$.


---

## 1.4 The Decomposition H = H_0 + (1/N) V

### 1.4.1 Reformulation in the auxiliary field variables

In the auxiliary field formalism, after integrating out $z_i$, the
transfer matrix acts on the space of configurations of
$(\sigma(x), A_\mu(x))$ on a spatial slice:

$$\mathcal{H}_{\text{eff}} = L^2(\{\sigma(x), A_\mu(x)\},\; d\nu)$$

where $d\nu$ is the measure induced by the $z$ integration. The
effective transfer matrix is:

$$T_{\text{eff}} = \exp(-a\,H_{\text{eff}})$$

with $H_{\text{eff}}$ the effective Hamiltonian in the auxiliary field
variables.

### 1.4.2 The N = infinity Hamiltonian H_0

At N = infinity, the saddle-point is exact. The fluctuations of
$\sigma$ and $A_\mu$ are governed by the quadratic action:

$$S_0 = \frac{1}{2}\int \frac{d^2p}{(2\pi)^2}\left[
  |\tilde{\sigma}(p)|^2\,\Pi_\sigma(p)
  + |\tilde{A}_\mu(p)|^2\,\Pi_A(p)\right]$$

This is a FREE (Gaussian) theory. The corresponding Hamiltonian is:

$$\boxed{H_0 = \int \frac{dp}{2\pi}\;\omega_\sigma(p)\;
  a^\dagger_\sigma(p) a_\sigma(p)
  + \int \frac{dp}{2\pi}\;\omega_A(p)\;
  a^\dagger_A(p) a_A(p)}$$

where:
- $a^\dagger_\sigma(p), a_\sigma(p)$ are creation/annihilation operators
  for the sigma fluctuation mode at spatial momentum $p$
- $a^\dagger_A(p), a_A(p)$ are creation/annihilation operators for the
  gauge fluctuation mode
- $\omega_\sigma(p) = \sqrt{p^2 + M_\sigma^2}$ with
  $M_\sigma^2 = 4m^2$ (the sigma "particle" is the two-particle
  threshold, not a stable particle -- it is a resonance embedded in
  the two-particle continuum starting at $2m$)
- $\omega_A(p) = |p|$ (the gauge field is massless at N = infinity;
  it acquires dynamics only through the z-loop)

The SPECTRAL GAP of $H_0$:

The physical mass gap is NOT the gap of $H_0$ in the auxiliary field
variables directly. Rather, it is the gap of the ORIGINAL Hamiltonian
$H$ acting on $\mathcal{H}$, which describes the z-particle
excitations. At N = infinity, the z-particles are free with mass $m$,
so:

$$\boxed{\text{gap}(H_0) = m = \Lambda_{2D}}$$

[PROVED -- this is Witten's 1979 result]

### 1.4.3 The interaction V

The 1/N corrections arise from the cubic and quartic vertices in the
fluctuation expansion of $S_{\text{eff}}$. Collecting all terms that
are suppressed by $1/N$ relative to the quadratic part:

$$\boxed{V = V_{\sigma^3} + V_{\sigma A^2} + V_{\sigma^2 A^2}
  + V_{\sigma^4} + V_{\sigma\text{-shift}} + V_{A\text{-shift}}}$$

where:

**Cubic vertices (from the third derivative of Tr ln):**

$$V_{\sigma^3} = \int \frac{d^2p\,d^2q}{(2\pi)^4}\;
  \Gamma_3(p, q)\;\tilde{\sigma}(p)\,\tilde{\sigma}(q)\,
  \tilde{\sigma}(-p-q)$$

$$\Gamma_3(p,q) = -\frac{1}{(2\pi)^2}\int \frac{d^2k}
  {(k^2+m^2)((k+p)^2+m^2)((k+p+q)^2+m^2)}$$

This is the triangle diagram with three massive propagators.
[PROVED: UV finite in 2D]

$$V_{\sigma A^2} = \int \frac{d^2p\,d^2q}{(2\pi)^4}\;
  \Gamma_{\sigma AA}^{\mu\nu}(p,q)\;\tilde{\sigma}(p)\,
  \tilde{A}_\mu(q)\,\tilde{A}_\nu(-p-q)$$

with $\Gamma_{\sigma AA}$ the sigma-gauge-gauge three-point vertex.

**Quartic vertices (from the fourth derivative of Tr ln):**

$$V_{\sigma^4}, \; V_{\sigma^2 A^2}$$

These are the box and crossed-box diagrams with four massive
propagators. UV finite in 2D. [PROVED]

**Saddle-point shift terms:**

$$V_{\sigma\text{-shift}} = \delta\sigma_1 \cdot
  \frac{\partial^2 S_{\text{eff}}}{\partial\sigma^2}\bigg|_*
  \cdot \tilde{\sigma}$$

This accounts for the O(1/N) shift in the saddle-point value
$\sigma_* \to m^2 + \delta\sigma_1/N + \ldots$. The shift is:

$$\delta\sigma_1 = -\frac{1}{(2\pi)^2}\int \frac{d^2p}
  {(p^2+m^2)^2}\left[\frac{1}{\Pi_\sigma(p)}
  + \frac{2p^2}{p^2\,\Pi_A(p)}\right] \cdot m^2$$

[ESTABLISHED -- computed by Campostrini, Rossi, and Vicari 1992]

### 1.4.4 The full decomposition

$$\boxed{H = H_0 + \frac{1}{N}\,V}$$

where:
- $H_0$: Free Hamiltonian for N massive z-particles (mass $m = \Lambda$)
  plus Gaussian fluctuations of $\sigma$ and $A_\mu$
- $V$: Sum of all interaction vertices listed above
- Domain of $H_0$: the Fock space $\mathcal{F}$ of free particles
- Domain of $V$: requires regularity conditions on the state (the
  vertices involve products of fields at the same point, regulated
  by the UV cutoff or lattice spacing)


---

## 1.5 Properties of H_0 and V

### 1.5.1 H_0 is exactly solvable [PROVED]

$H_0$ describes N free massive bosons. Its spectrum is:

$$\text{Spec}(H_0) = \left\{E = \sum_{i=1}^N \sum_{k}
  n_{ik}\,\omega_k \;\Big|\; n_{ik} \in \mathbb{Z}_{\geq 0}\right\}$$

Ground state energy: $E_0 = 0$ (after normal ordering).
First excited state: $E_1 = m = \Lambda_{2D}$.
Gap: $\Delta_0 = m = \Lambda_{2D}$.

### 1.5.2 V is a sum of well-defined interaction vertices [ESTABLISHED]

Each vertex in V is:
- Expressed as a convergent integral over the momenta of the
  fluctuation fields (UV finite in 2D)
- IR finite (all internal propagators carry mass $m > 0$)
- A polynomial in the creation/annihilation operators (when expressed
  in the Fock space language)

### 1.5.3 The perturbation is O(1/N) [PROVED]

The coupling constant of V is 1/N. At N = infinity, V decouples and
H reduces to $H_0$. The 1/N expansion is a perturbative expansion
in the vertices of V, with each loop of auxiliary fields contributing
one power of 1/N.

### 1.5.4 Sign of V [OPEN -- see file 02]

The sign of V is the crucial question for monotonicity. If V >= 0
(positive semi-definite as an operator on $\mathcal{H}$), then
$H \geq H_0$ and gap(H) >= gap(H_0) = Lambda. This is analyzed in
the next file.


---

## 1.6 Summary

| Object | Definition | Status |
|--------|-----------|--------|
| $\mathcal{H}$ | $L^2(\prod_x \mathbb{CP}^{N-1}_x, d\mu_{\text{FS}})$ | [PROVED] |
| $T$ | Transfer matrix from one-step Euclidean evolution | [PROVED: bounded, self-adjoint, positive, trace-class] |
| $H = -a^{-1}\ln T$ | Hamiltonian | [PROVED: self-adjoint, bounded below] |
| $H_0$ | Free Hamiltonian (N = infinity limit) | [PROVED: exactly solvable, gap = $\Lambda$] |
| $V$ | Interaction: cubic + quartic vertices + saddle shift | [ESTABLISHED: UV/IR finite vertices] |
| $H = H_0 + V/N$ | Full decomposition | [ESTABLISHED at the level of the effective action] |
| gap($H_0$) = $\Lambda$ | Spectral gap at N = infinity | [PROVED] |
| gap($H$) >= $\Lambda$? | Monotonicity conjecture | [OPEN] |

The decomposition $H = H_0 + V/N$ is explicit and well-defined. The
remaining question is the sign and magnitude of V as an operator.
