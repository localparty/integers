# 3. Existence: The Eleven-Dimensional Quantum Theory

We construct a quantum Yang--Mills theory satisfying the
Osterwalder--Schrader axioms by Kaluza--Klein reduction from eleven
dimensions. This section establishes existence; the mass gap is proven
in Section 4.


## 3.1 The Euclidean Action

The starting point is the eleven-dimensional Einstein--Hilbert action
in Euclidean signature on $M^4_E \times \mathbb{CP}^2$:

$$S_{11}[g] = \frac{1}{16\pi G_{11}}
  \int_{M^4_E \times \mathbb{CP}^2}
  R_{11} \sqrt{g_{11}} \; d^{11}x$$

where $R_{11}$ is the eleven-dimensional Ricci scalar and $G_{11}$ is
the eleven-dimensional Newton constant.

For the mass gap proof, we focus on the $M^4 \times \mathbb{CP}^2$
sector. The $S^2$ and $S^1$ factors produce the $SU(2)$ and $U(1)$
sectors, which are not directly relevant to the SU(3) mass gap.

**The Euclidean path integral:**
$$Z = \int [Dg_{11}] \; e^{-S_{11}[g_{11}]}$$

The measure $[Dg_{11}]$ is over eleven-dimensional metrics on
$M^4_E \times \mathbb{CP}^2$ modulo diffeomorphisms. The compactness
of $\mathbb{CP}^2$ is crucial: it ensures the internal integration is
over a finite-volume space.


## 3.2 Kaluza--Klein Decomposition

Expand the eleven-dimensional metric in harmonics on $\mathbb{CP}^2$.
The off-diagonal components $g_{\mu a}$ (one spacetime index, one
internal index) decompose into Killing vector harmonics:

$$g_{\mu a}(x, y) = \sum_{I=1}^{8} B_\mu^I(x) \, K_I^a(y)
  + \sum_{n \geq 1} \text{(massive KK modes)}$$

The $n = 0$ sector gives 8 four-dimensional gauge fields $B_\mu^I(x)$,
one for each Killing vector of $\mathbb{CP}^2$. These are the gluon
fields.

**The reduced action.** Substituting the KK decomposition into $S_{11}$
and integrating over $\mathbb{CP}^2$:

$$S_{11} = \underbrace{\frac{1}{4g_3^2} \int_{M^4_E}
  \text{Tr}(F_{\mu\nu} F^{\mu\nu}) \sqrt{g_4} \, d^4x}_{
  \text{4D Yang--Mills action}}
  \;+\; \underbrace{S_{\text{KK}}[\text{massive modes}]}_{
  \text{massive KK corrections}}
  \;+\; \underbrace{S_{\text{grav}}[g_{\mu\nu}]}_{
  \text{4D gravity}}$$

where:
$$g_3^2 = \frac{16\pi G_{11}}{\text{Vol}(\mathbb{CP}^2)}, \quad
  F_{\mu\nu}^I = \partial_\mu B_\nu^I - \partial_\nu B_\mu^I
  + f^{IJK} B_\mu^J B_\nu^K$$

and $f^{IJK}$ are the structure constants of $SU(3)$ (determined by the
Lie brackets of the Killing vectors $K_I$).

**The zero-mode sector IS Yang--Mills.** The $n = 0$ sector of the KK
reduction is exactly the four-dimensional $SU(3)$ Yang--Mills action.
This is not an approximation --- it is the exact content of the
massless sector.


## 3.3 Why the Theory Exists

The eleven-dimensional theory on $M^4_E \times \mathbb{CP}^2$ has
properties that make it amenable to rigorous construction --- properties
absent in the direct four-dimensional approach:

**Property 1: Discrete spectrum.**
The Laplacian on $\mathbb{CP}^2$ has discrete eigenvalues
$0 = \lambda_0 < \lambda_1 \leq \lambda_2 \leq \ldots$ with
$\lambda_n \to \infty$. Every mode in the KK tower has a definite mass.
There are no continuous spectra in the internal direction.

**Property 2: Built-in UV regularization.**
The compactness of $\mathbb{CP}^2$ provides a natural ultraviolet cutoff
at the KK scale $M_{\text{KK}} = 1/r_3$. Momentum modes in the
internal direction are quantized: $p_{\text{int}} = n/r_3$ for
$n \in \mathbb{Z}$. There are no arbitrarily high momenta to integrate
over in the internal directions.

**Property 3: Zeta-regularized finiteness.**
The remaining UV divergences from the four-dimensional momentum integrals
are regulated by the Epstein zeta function of the KK tower. The leading
divergence vanishes at every loop order:
$$S_0^{(L)} = [1 + 2\zeta(0)]^L = 0$$

This is not dimensional regularization (which introduces an artificial
parameter $\epsilon$). It is a physical regularization: the compactness
of the internal space renders the theory finite.

**Property 4: Preserved symmetries.**
Unlike lattice regularization (which breaks Euclidean invariance) or
dimensional regularization (which works only perturbatively), the KK
construction preserves:
- Four-dimensional Euclidean invariance $SO(4)$
- Gauge invariance $SU(3)$ (it IS the isometry group)
- Reflection positivity (Section 5)

**Property 5: No continuum limit needed.**
In lattice gauge theory, the continuum limit $a \to 0$ is the hardest
step --- it requires controlling the theory at all scales. In the KK
construction, there is no lattice spacing. The theory is defined in the
continuum from the start. The "discretization" is in the internal
direction (the KK tower), not in spacetime.


## 3.4 The Transfer Matrix

The Hilbert space and Hamiltonian are constructed via the transfer matrix
on Euclidean time slices.

**Setup.** Slice $M^4_E$ into constant-time hypersurfaces
$\Sigma_t = \mathbb{R}^3$ at Euclidean time $t$. The full spatial slice
(including the internal space) is:
$$\hat{\Sigma}_t = \mathbb{R}^3 \times \mathbb{CP}^2$$

**The transfer matrix $T$.** For a time interval $\epsilon > 0$, the
transfer matrix is:
$$T(\epsilon) = e^{-\epsilon \hat{H}}$$

where $\hat{H}$ is the Hamiltonian on $\hat{\Sigma}$. In the path
integral:
$$\langle \phi_2 | T(\epsilon) | \phi_1 \rangle
  = \int_{\phi(0) = \phi_1}^{\phi(\epsilon) = \phi_2}
  [D\phi] \; e^{-S[\phi]}$$

where the integral is over field configurations on the slab
$[0, \epsilon] \times \hat{\Sigma}$.

**Properties of $T$:**
- $T$ is bounded (the action is bounded below on the compact internal
  space)
- $T$ is self-adjoint ($T = T^\dagger$, from time-reversal symmetry
  of the Euclidean action)
- $T$ is positive ($T \geq 0$, from reflection positivity --- see
  Section 5)

The Hilbert space $\mathcal{H}$ is the completion of the space of
field configurations on $\hat{\Sigma}$ in the inner product defined by
$T$. The Hamiltonian is $\hat{H} = -\ln T$.

**Spectral decomposition.** Because $T$ is bounded, self-adjoint, and
positive on a separable Hilbert space:
$$T = \sum_n e^{-\epsilon E_n} |n\rangle \langle n|$$

with $0 \leq E_0 \leq E_1 \leq E_2 \leq \ldots$ The vacuum $|0\rangle$
has $E_0 = 0$ (by normalization). The mass gap is
$\Delta = E_1 - E_0 = E_1$.


## 3.5 The Four-Dimensional Theory

The four-dimensional Yang--Mills theory is obtained by integrating out
all KK modes with $n \geq 1$. In terms of the transfer matrix:

$$T_{\text{4D}}(\epsilon) = \text{Tr}_{\text{KK}} \; T(\epsilon)$$

where $\text{Tr}_{\text{KK}}$ traces over the massive KK modes.

The resulting four-dimensional transfer matrix $T_{\text{4D}}$ acts on
the Hilbert space $\mathcal{H}_{\text{4D}}$ of gauge field
configurations on $\mathbb{R}^3$. Its spectral decomposition gives the
four-dimensional mass spectrum.

**Key claim (proven in Section 6).** If the eleven-dimensional theory has
a mass gap $\hat{\Delta} > 0$, then the four-dimensional theory inherits
a mass gap $\Delta \geq \hat{\Delta}$ (tracing out massive modes cannot
close a gap).

Therefore: to prove the four-dimensional mass gap, it suffices to prove
the eleven-dimensional mass gap. And in eleven dimensions, the mass gap
is topological (Section 4).
