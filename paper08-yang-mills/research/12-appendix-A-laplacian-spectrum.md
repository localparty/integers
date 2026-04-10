# Appendix A: The Laplacian Spectrum on CP2

We collect the spectral properties of the scalar Laplacian on
$(\mathbb{CP}^2, g_{\text{FS}})$ needed for the mass gap computation.


## A.1 The Eigenvalue Formula

The scalar Laplacian $\Delta_{\mathbb{CP}^2}$ on $\mathbb{CP}^2$ with
the Fubini--Study metric (normalized so that holomorphic sectional
curvature is $4/r_3^2$) has eigenvalues:

$$\lambda_{p,q} = \frac{4}{r_3^2}\left[p(p+2) + q(q+2) + pq\right]$$

for $p, q = 0, 1, 2, \ldots$

The eigenfunctions are the harmonic polynomials on $\mathbb{CP}^2$,
which organize into irreducible representations of $SU(3)$:
- $(p, q)$ labels the $SU(3)$ representation with Dynkin indices
  $(p, q)$
- The degeneracy is $\dim(p,q) = \frac{1}{2}(p+1)(q+1)(p+q+2)$


## A.2 Low-Lying Spectrum

| $(p,q)$ | $\lambda_{p,q} \cdot r_3^2$ | Degeneracy | $SU(3)$ rep | Name |
|---------|----------------------------|------------|-------------|------|
| $(0,0)$ | 0 | 1 | $\mathbf{1}$ | Trivial (vacuum) |
| $(1,0)$ | 12 | 3 | $\mathbf{3}$ | Fundamental |
| $(0,1)$ | 12 | $\bar{3}$ | $\mathbf{\bar{3}}$ | Antifundamental |
| $(2,0)$ | 32 | 6 | $\mathbf{6}$ | Symmetric |
| $(0,2)$ | 32 | $\bar{6}$ | $\mathbf{\bar{6}}$ | Anti-symmetric |
| $(1,1)$ | 32 | 8 | $\mathbf{8}$ | Adjoint |
| $(3,0)$ | 60 | 10 | $\mathbf{10}$ | Decuplet |
| $(2,1)$ | 60 | 15 | $\mathbf{15}$ | ... |

**First non-trivial eigenvalue:**
$$\lambda_1 = \frac{12}{r_3^2}$$

This exceeds the Lichnerowicz lower bound. For $\mathbb{CP}^2$ with
$\text{Ric} = (6/r_3^2) g$:
$$\lambda_1 \geq \frac{n}{n-1} \text{Ric}_{\min}
  = \frac{4}{3} \times \frac{6}{r_3^2} = \frac{8}{r_3^2}$$

The actual value $12/r_3^2$ exceeds this bound by a factor of $3/2$,
which is expected for K\"ahler manifolds (the Lichnerowicz--Obata bound
is not tight for $\mathbb{CP}^n$).


## A.3 Gauge-Invariant States

Physical glueball states are $SU(3)$ singlets (color-singlets). The
lightest color-singlet constructed from the adjoint representation
$\mathbf{8}$ requires the product $\mathbf{8} \otimes \mathbf{8}$,
which contains a singlet:
$$\mathbf{8} \otimes \mathbf{8} = \mathbf{1} \oplus \mathbf{8}
  \oplus \mathbf{8} \oplus \mathbf{10} \oplus \overline{\mathbf{10}}
  \oplus \mathbf{27}$$

The $\mathbf{1}$ (singlet) component corresponds to the trace
$\text{Tr}(F_{\mu\nu} F^{\mu\nu})$ --- the scalar glueball operator.

**Mass of the lightest glueball from the Laplacian:**
$$m_{\text{glueball}}^2 \sim \frac{\lambda_{1,1}}{r_3^2}
  = \frac{32}{r_3^4}$$


## A.4 Weyl's Law

The asymptotic growth of eigenvalues follows Weyl's law for a
four-dimensional compact Riemannian manifold:

$$N(\lambda) = \#\{n : \lambda_n \leq \lambda\}
  \sim \frac{\text{Vol}(\mathbb{CP}^2)}{16\pi^2} \lambda^2
  = \frac{r_3^4}{6} \lambda^2$$

as $\lambda \to \infty$. This confirms that the KK tower grows as
$n^2$ in four internal dimensions, which is compatible with the zeta
regularization analysis (the relevant Epstein zeta function converges
for $\text{Re}(s) > 2$, and the regularization extends it to $s = 0$
where $\zeta(0) = -1/2$).


## A.5 Heat Kernel

The heat kernel on $\mathbb{CP}^2$ at short Euclidean time $t$:
$$K(t) = \text{Tr}\, e^{-t \Delta_{\mathbb{CP}^2}}
  = \sum_{p,q} \dim(p,q) \, e^{-t \lambda_{p,q}}$$

has the asymptotic expansion:
$$K(t) \sim \frac{\text{Vol}(\mathbb{CP}^2)}{(4\pi t)^2}
  \left(1 + \frac{R_{\text{scalar}}}{6} t
  + \mathcal{O}(t^2)\right)$$

where $R_{\text{scalar}} = 24/r_3^2$ is the scalar curvature of the
Fubini--Study metric. The heat kernel is used in the transfer matrix
construction (Section 3.4) and in the reflection positivity argument
(Section 5.4).
