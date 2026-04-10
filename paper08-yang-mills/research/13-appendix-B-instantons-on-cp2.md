# Appendix B: Instantons on CP2

We derive the Bogomolny bound and describe the instanton solutions on
$\mathbb{CP}^2$ used in Section 4.


## B.1 Self-Duality on Four-Manifolds

On any oriented Riemannian four-manifold $(X, g)$, the Hodge star
operator $*: \Omega^2(X) \to \Omega^2(X)$ satisfies $*^2 = 1$ on
two-forms. This gives the eigenspace decomposition:
$$\Omega^2(X) = \Omega^+(X) \oplus \Omega^-(X)$$

where $\Omega^{\pm}$ are the $\pm 1$ eigenspaces (self-dual and
anti-self-dual two-forms).

For a gauge field with curvature $F \in \Omega^2(X, \text{ad}\,P)$:
$$F = F^+ + F^-, \quad *F^{\pm} = \pm F^{\pm}$$


## B.2 The Bogomolny Bound

**Theorem (Bogomolny bound on compact 4-manifolds).** Let $(X, g)$ be a
compact oriented Riemannian four-manifold and $P \to X$ a principal
$G$-bundle with $G$ compact semisimple. For any connection $A$ on $P$:

$$S_{\text{YM}}[A] = \frac{1}{2g^2} \int_X \text{Tr}(F \wedge *F)
  \;\geq\; \frac{8\pi^2}{g^2} |k|$$

where $k = c_2(P) = \frac{1}{8\pi^2} \int_X \text{Tr}(F \wedge F)$.

*Proof.* Write:
$$\int_X \text{Tr}(F \wedge *F) = \|F^+\|^2 + \|F^-\|^2$$
$$\int_X \text{Tr}(F \wedge F) = \|F^+\|^2 - \|F^-\|^2 = 8\pi^2 k$$

Since $\|F^{\pm}\|^2 \geq 0$:

For $k \geq 0$: $\|F^+\|^2 = 8\pi^2 k + \|F^-\|^2 \geq 8\pi^2 k$,
so $\|F^+\|^2 + \|F^-\|^2 \geq 8\pi^2 k + 2\|F^-\|^2 \geq 8\pi^2 k$.
Actually, more directly:
$$\|F^+\|^2 + \|F^-\|^2 \geq |\|F^+\|^2 - \|F^-\|^2| = 8\pi^2|k|$$

Equality when $F^- = 0$ ($k > 0$, self-dual) or $F^+ = 0$ ($k < 0$,
anti-self-dual). $\square$


## B.3 Instantons on CP2

$\mathbb{CP}^2$ is a compact oriented four-manifold, so the Bogomolny
bound applies directly.

**The canonical line bundle instanton.** The simplest instanton on
$\mathbb{CP}^2$ is the curvature of the canonical (or anti-canonical)
line bundle. In homogeneous coordinates $[Z_0 : Z_1 : Z_2]$:

The Fubini--Study K\"ahler form $\omega_{\text{FS}}$ is self-dual
($*\omega_{\text{FS}} = \omega_{\text{FS}}$) and satisfies:
$$\int_{\mathbb{CP}^2} \omega_{\text{FS}} \wedge \omega_{\text{FS}}
  = \int_{\mathbb{CP}^2} \frac{r_3^4}{(1+|z|^2)^4}
  \, d^4z = \frac{8\pi^2 r_3^4}{3} \times \frac{1}{r_3^4} = \frac{8\pi^2}{3}$$

Wait --- let us be more careful with the normalization. For the
Fubini--Study metric on $\mathbb{CP}^2$ with $\int_{\mathbb{CP}^1}
\omega = 1$:
$$\int_{\mathbb{CP}^2} \omega \wedge \omega = 1$$

This is the intersection number $\mathbb{CP}^1 \cdot \mathbb{CP}^1 = 1$.

**SU(2) instanton.** For $SU(2)$ gauge theory, the $k = 1$ instanton on
$\mathbb{CP}^2$ was constructed by Charap and Duff (1977). The
connection is:
$$A = \frac{1}{2} \text{Im}\left(\frac{\bar{z}_i \, dz_i}{1+|z|^2}
  \right) \sigma_3
  + \frac{1}{2}\frac{dz_1 \, \sigma_+ + d\bar{z}_1 \, \sigma_-}
  {1 + |z|^2}$$

with curvature:
$$F = \frac{\sigma_3}{2} \frac{dz_1 \wedge d\bar{z}_1
  + dz_2 \wedge d\bar{z}_2}{(1+|z|^2)^2}
  + \text{(off-diagonal terms)}$$

This is self-dual: $F = *F$, so the Bogomolny bound is saturated.

**SU(3) instanton.** For the physical case $G = SU(3)$, instantons on
$\mathbb{CP}^2$ are constructed by embedding the $SU(2)$ instanton
into an $SU(2) \subset SU(3)$ subgroup. The $k = 1$ $SU(3)$ instanton
has moduli space of dimension $\dim \mathcal{M}_{3,1} = 4 \times 3
\times 1 - 9 + 1 = 4$.


## B.4 The Energy of the k = 1 Sector

For any connection on the $k = 1$ $SU(3)$ bundle over $\mathbb{CP}^2$:
$$E[A] \geq \frac{8\pi^2}{g_3^2}$$

The instanton saturates this bound:
$$E_{\text{instanton}} = \frac{8\pi^2}{g_3^2}$$

Using $g_3^2 = 16\pi G_{11}/\text{Vol}(\mathbb{CP}^2)$:
$$E_{\text{instanton}} = \frac{8\pi^2 \text{Vol}(\mathbb{CP}^2)}{16\pi G_{11}}
  = \frac{\pi \text{Vol}(\mathbb{CP}^2)}{2 G_{11}}$$

This is a purely geometric quantity --- the product of the volume of
$\mathbb{CP}^2$ and the eleven-dimensional gravitational coupling.


## B.5 Higher Topological Sectors

For $|k| = n > 1$, the Bogomolny bound gives:
$$E[A] \geq \frac{8\pi^2 n}{g_3^2}$$

The energy grows linearly with the topological charge. Multi-instanton
configurations exist for all $n$ and can be described using the ADHM
construction adapted to $\mathbb{CP}^2$ (Buchdahl 1988).

The spectrum of topological energies is:
$$E_k = \frac{8\pi^2 |k|}{g_3^2}, \quad k \in \mathbb{Z}$$

This is a discrete spectrum with uniform spacing $8\pi^2/g_3^2$.
The gap between $k = 0$ (vacuum) and $k = \pm 1$ (lightest topological
excitation) is the mass gap $\Delta$.
