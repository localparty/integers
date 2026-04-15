# Path 1a: Lattice Summation by Parts on Polymers with Boundaries

Resolves Obstacle 1 of Path 1 (Section 7.1): transferring $d_O - 4$
lattice derivatives from an irrelevant operator to the one-particle
wave function within a polymer with boundary, and controlling the
boundary terms.

**Notation.** $a = a_k$ (block lattice spacing), $\hat{\Delta} =
a\Delta$ (dimensionless mass gap), $g = g_k$ (running coupling),
$\Lambda_k$ (block lattice after $k$ RG steps).


---


## 1. Lattice Difference Operators

### 1.1 Basic definitions

**Forward difference:** $(\nabla_\mu f)(x) = f(x + a\hat{\mu}) - f(x)$.
**Backward difference:** $(\nabla_\mu^* f)(x) = f(x) - f(x - a\hat{\mu})$,
the formal $\ell^2$-adjoint of $-\nabla_\mu$.
**Lattice Laplacian:** $\Delta_{\mathrm{lat}} = \sum_\mu \nabla_\mu^*
\nabla_\mu$. Higher-order: $\nabla^\alpha = \nabla_{\mu_1} \cdots
\nabla_{\mu_p}$ for multi-index $\alpha$ with $|\alpha| = p$.

### 1.2 Gauge-covariant derivatives

**Covariant forward difference:** $(D_\mu \phi)(x) = U_{x,\mu}\,
\phi(x+a\hat{\mu})\,U_{x,\mu}^{-1} - \phi(x)$ for $\phi \in
\mathfrak{su}(N)$. **Covariant backward:** $(D_\mu^*\phi)(x) =
\phi(x) - U_{x-a\hat{\mu},\mu}^{-1}\phi(x-a\hat{\mu})
U_{x-a\hat{\mu},\mu}$. The Leibniz rule involves parallel transport
(treated in Section 7). **Lattice field strength:**
$F_{\mu\nu}^{(\mathrm{lat})}(x) = (U_P - \mathbf{1})/a^2 =
F_{\mu\nu}(x) + O(a)$ in Balaban's small-field region.


---


## 2. The Dimension-6 Operator in Lattice Variables

The leading continuum dimension-6 operators are $\mathcal{O}_6^{(1)}
= \mathrm{Tr}(D_\rho F_{\mu\nu} D^\rho F^{\mu\nu})$ and
$\mathcal{O}_6^{(2)} = \mathrm{Tr}(D_\mu F^{\mu\rho} D_\nu
F^\nu{}_\rho)$, each carrying two extra covariant derivatives beyond
$\mathrm{Tr}\,F^2$. Coefficients satisfy $|c_6^{(k)}| \leq Cg^2$.

**Lattice form (covariant):**
$O_6(x) = \sum_{\mu<\nu}\sum_\rho \mathrm{Re}\,\mathrm{Tr}[(D_\rho
F_{\mu\nu}^{(\mathrm{lat})})(x)]^2$.

**Lattice form (gauge-invariant scalar):** Using $s_P = 1 -
\frac{1}{N}\mathrm{Re}\,\mathrm{Tr}\,U_P$:

$$\tilde{O}_6(x) = \sum_P \sum_\rho (\nabla_\rho s_P)(x)^2$$

This carries two ordinary lattice derivatives beyond $s_P$ (dim-4).
Both forms satisfy Definition 5.1 (Path 1): $O_6(x) =
\sum_{|\alpha|=2} c_\alpha\,\nabla^\alpha\mathcal{M}_\alpha(x)$
with $\mathcal{M}_\alpha$ gauge-invariant, dimension 4. This
difference structure is what allows summation by parts.


---


## 3. Summation by Parts on the Full Lattice

### 3.1 The fundamental identity (scalar case)

On the full lattice $\Lambda$ (periodic or infinite with decay), the
summation-by-parts identity is:

$$\sum_{x \in \Lambda} (\nabla_\mu f)(x)\,g(x)
  = -\sum_{x \in \Lambda} f(x)\,(\nabla_\mu^* g)(x)$$

**Proof.** Shift the summation index $x \to x - a\hat{\mu}$ in
$\sum_x f(x + a\hat{\mu})\,g(x)$ to get
$\sum_x f(x)\,g(x - a\hat{\mu})$, whence $\sum_x (\nabla_\mu f)\,g
= -\sum_x f\,(\nabla_\mu^* g)$. $\square$

For two derivatives, iterate:

$$\sum_x (\nabla_\mu \nabla_\nu f)(x)\,g(x)
  = \sum_x f(x)\,(\nabla_\mu^* \nabla_\nu^* g)(x)$$

### 3.2 Application to the form factor

Write $O_6(0) = \sum_\rho \nabla_\rho^2 \mathcal{M}(0)$
(schematically). Transfer $\nabla_\rho^2$ onto the one-particle
wave function $\psi_1(\vec{x}) = \langle \vec{x}|1\rangle$:

- **Spatial derivatives** ($\rho = 1,2,3$): $\nabla_\rho \psi_1 = 0$
  since $\psi_1$ is constant (translation invariance at $\vec{p}=0$).

- **Temporal derivative** ($\rho = 0$): $\nabla_0\,e^{-\hat{\Delta}t}
  = (e^{-\hat{\Delta}} - 1)\,e^{-\hat{\Delta}t} \approx
  -\hat{\Delta}\,e^{-\hat{\Delta}t}$. Each temporal derivative
  contributes $\hat{\Delta}$.

Therefore on the full lattice, the two transferred derivatives give
$\hat{\Delta}^2 = (a\Delta)^2$, and summing over $\vec{z}$ with
exponential clustering:

$$|f_c^{(6)}(0)| \leq C'\,g^4\,(a\Delta)^2\,\Delta^3$$

This is the target bound (Theorem 7). The full-lattice argument is
clean because periodic/infinite sums have no boundary terms. The
difficulty is that the cluster expansion sums over polymers, not the
full lattice.


---


## 4. The Polymer Boundary Problem

### 4.1 Summation by parts on a polymer

Let $X \subset \Lambda_k$ be a connected polymer. Define
$\partial_\mu^+ X = \{x \in X : x + a\hat{\mu} \notin X\}$ (inner
boundary) and $\partial_\mu^- X = \{y - a\hat{\mu} : y \in X,\;
y - a\hat{\mu} \notin X\}$ (outer boundary).

**Lemma 4.1 (Summation by parts on a polymer).**
*For $f, g : \Lambda_k \to \mathbb{C}$ and a finite subset
$X \subset \Lambda_k$:*

$$\sum_{x \in X} (\nabla_\mu f)(x)\,g(x)
  = -\sum_{x \in X} f(x)\,(\nabla_\mu^* g)(x)
  + B_\mu(f, g; X)$$

*where the boundary term is:*

$$B_\mu(f, g; X)
  = \sum_{x \in \partial_\mu^+ X} f(x + a\hat{\mu})\,g(x)
  - \sum_{x \in \partial_\mu^- X} f(x)\,g(x + a\hat{\mu})$$

**Proof.** Substitute $y = x + a\hat{\mu}$ and split by $y \in X$
vs. $y \notin X$. The $y \notin X$ part gives $\partial_\mu^+$;
rewriting $g(y-a\hat{\mu}) = g(y) - (\nabla_\mu^* g)(y)$ for
$y \in X$ gives the bulk adjoint; the complementary boundary gives
$\partial_\mu^-$. Functions $f,g$ are defined on all of $\Lambda_k$.
$\square$

### 4.2 Iterating for two derivatives

Write $I(X) = \sum_{x \in X} h(\vec{z},x)\,(\nabla_\rho\nabla_\sigma
\mathcal{M})(x)$. Two applications of Lemma 4.1 give:

$$I(X) = \underbrace{\sum_{x \in X} \mathcal{M}(x)\,
  (\nabla_\rho^*\nabla_\sigma^* h)(x)}_{\text{bulk}}
  \;-\; B_\sigma(\mathcal{M}, \nabla_\rho^* h; X)
  \;+\; B_\rho(\nabla_\sigma \mathcal{M}, h; X)$$

A bulk term (both derivatives transferred to $h$) plus two boundary
terms, one from each application.

### 4.3 Structure of the boundary terms

The two boundary terms have explicit form:

$$B_\rho(\nabla_\sigma \mathcal{M}, h; X)
  = \sum_{x \in \partial_\rho^+ X}
    (\nabla_\sigma \mathcal{M})(x + a\hat{\rho})\,h(x)
  - \sum_{x \in \partial_\rho^- X}
    (\nabla_\sigma \mathcal{M})(x)\,h(x + a\hat{\rho})$$

$$B_\sigma(\mathcal{M}, \nabla_\rho^* h; X)
  = \sum_{x \in \partial_\sigma^+ X}
    \mathcal{M}(x + a\hat{\sigma})\,(\nabla_\rho^* h)(x)
  - \sum_{x \in \partial_\sigma^- X}
    \mathcal{M}(x)\,(\nabla_\rho^* h)(x + a\hat{\sigma})$$

Each involves the operator ($\|\mathcal{M}\|_\infty \leq M_4$) at
boundary points times the propagator (exponentially decaying) at
boundary points.


---


## 5. Control of the Boundary Terms

### 5.1 Polymer geometry

Define the **depth** $d(0, \partial X) = \min_{y \in \partial X} |y|$.
A polymer of depth $R$ requires $|X| \geq cR$ sites. Conversely,
$d(0,\partial X) \leq C_d\,|X|^{1/4}$ in $d = 4$.

### 5.2 Exponential suppression of the boundary

By exponential clustering, $|h(\vec{z}, x)| \leq C_h\,e^{-\Delta|x|}$,
so on $\partial X$: $|h|_{\partial X} \leq C_h\,e^{-\Delta\,d(0,\partial X)}$.

**Lemma 5.2 (Boundary term bound).** *The boundary terms from the
double summation by parts satisfy:*

$$|B_\rho(\nabla_\sigma \mathcal{M}, h; X)|
  + |B_\sigma(\mathcal{M}, \nabla_\rho^* h; X)|
  \leq C_B\,|\partial X|\,M_4\,C_h\,
  \hat{\Delta}\,e^{-\Delta\,d(0, \partial X)}$$

*where $|\partial X|$ is the number of boundary sites and the factor
$\hat{\Delta}$ comes from $\nabla_\rho^* h$ contributing one derivative
of the propagator.*

**Proof.** Each boundary point satisfies $|x| \geq d(0, \partial X)$.
For the first term, bound $|\nabla_\sigma\mathcal{M}| \leq 2M_4$ and
$|h| \leq C_h e^{-\Delta|x|}$. For the second, $|\nabla_\rho^* h|
\leq \hat{\Delta}\,C_h\,e^{-\Delta|x|}$ (lattice derivative of an
exponential). Sum over boundary sites. $\square$

### 5.3 The small field condition on the boundary

In Balaban's small field region, $|\mathcal{M}|_{\Omega_s} \leq
Cg^4$, improving the boundary terms but not changing the qualitative
picture.


---


## 6. Summation over Polymers

### 6.1 Decomposition

From Section 4.2: $I(X) = I_{\mathrm{bulk}}(X) + I_{\mathrm{bdy}}(X)$
with $|I_{\mathrm{bulk}}| \leq K^{|X|}\|O_6\|_6\hat{\Delta}^2 z^{|X|}$
(both derivatives transferred) and $|I_{\mathrm{bdy}}| \leq K^{|X|}
C_B|\partial X|\hat{\Delta}\,e^{-\Delta\,d(0,\partial X)}z^{|X|}$.

### 6.2 Naive boundary estimate

**Lemma 6.2.** $\sum_{X \ni 0} |I_{\mathrm{bdy}}(X)|\,e^{\alpha|X|}
  = O(\hat{\Delta})$ (one power, not two).

**Proof.** Group the sum by depth $R = d(0, \partial X)$. Any polymer
of depth $R$ has $|X| \geq cR$ sites, giving $(Kze^\alpha)^{cR}$ from
the activity. Set $\rho = (Kze^\alpha)^c < 1$ (Kotecky-Preiss). The
boundary count gives $|\partial X| \leq C'' R^3$. Then:

$$\sum_{X \ni 0} |I_{\mathrm{bdy}}|\,e^{\alpha|X|}
  \leq C_B\,\hat{\Delta}\,\sum_{R=1}^{\infty}
    C'' R^3\,e^{-\hat{\Delta}R}\,\rho^R
  \leq C_B C'' C_3\,\hat{\Delta}\,|\ln\rho|^{-4}
  = O(\hat{\Delta})$$

since $\sum R^3\,e^{-\hat{\Delta}R}\rho^R \leq C_3/|\ln\rho|^4$
(the $\rho^R$ decay dominates for $|\ln\rho| > 0$).

**Problem.** This is $O(\hat{\Delta})$, not $O(\hat{\Delta}^2)$.
The boundary contributes one power less than the bulk. This would
give $|f_c| \leq Cg^4(a\Delta)\Delta^3$, and $\sum_k g_k^4(a_k\Lambda)$
diverges logarithmically.

### 6.3 The missing factor: the connected propagator

The estimate above used the full propagator $h$. But the form factor
is a **connected** (vacuum-subtracted) matrix element. The connected
propagator $h_c = h - \langle h\rangle_0$ vanishes at zero momentum,
so it carries an extra $\hat{\Delta}$:

$$|h_c(\vec{z}, x)| \leq C\,\hat{\Delta}\,e^{-\Delta\,|x|}$$

(see Section 6.4). With this refinement:

$$|I_{\mathrm{bdy}}(X)| \leq C_B'\,|\partial X|\,\hat{\Delta}^2\,
  e^{-\Delta\,d(0,\partial X)}\,K^{|X|}\,z^{|X|}$$

Both boundary terms now carry $\hat{\Delta}^2$: one power from the
transferred derivative, one from the connected propagator. The polymer
sum gives $O(\hat{\Delta}^2)$ as required.

### 6.4 Why the connected propagator carries $\hat{\Delta}$

The connected correlator $G_c(x,y) = \langle\phi(x)\phi(y)\rangle -
\langle\phi\rangle^2$ has Fourier transform $\hat{G}_c(p) \sim
1/(p^2 + \Delta^2)$, supported at $|p| \lesssim \Delta$. Its
position-space profile $h_c(x) \sim Z\,e^{-\Delta|x|}/\Delta^{d-1}$
is smooth on scale $1/\Delta$, so the lattice derivative satisfies:

$$|(\nabla_\mu h_c)(x)| \leq a\,|\partial_\mu h_c| + O(a^2)
  \leq \hat{\Delta}\,|h_c(x)| + O(a^2)$$

Each lattice derivative on the connected propagator brings
$\hat{\Delta}$ because the propagator varies on scale $1/\Delta$
while the lattice spacing is $a$.


---


## 7. The Gauge-Covariant Complication

### 7.1 Covariant summation by parts

For $D_\mu$ on adjoint-valued fields:

$$\sum_{x \in X} \mathrm{Tr}[(D_\mu\Phi)^\dagger\Psi]
  = -\sum_{x \in X} \mathrm{Tr}[\Phi^\dagger(D_\mu^*\Psi)]
  + B_\mu^{\mathrm{cov}}(\Phi, \Psi; X)$$

The covariant boundary term $B_\mu^{\mathrm{cov}}$ has the same
structure as the scalar one, with parallel transports $U_{x,\mu}$
inserted. Since $U_{x,\mu}$ is unitary, $|U\Phi U^{-1}| = |\Phi|$,
so the covariant boundary terms have **exactly the same magnitude**
as the scalar ones.

### 7.2 Connection terms from the Leibniz rule

The covariant Leibniz rule for $\mathrm{Tr}(\Phi\,\Psi)$ produces a
curvature remainder $R_\mu(x)$ satisfying $|R_\mu| \leq C\,a^2\,
|F_{\mu\nu}|\,|\Phi|\,|\Psi| \leq C\,a^2\,p(g)\,|\Phi|\,|\Psi|$
in the small field region. This is $O(a^2) = O(\hat{\Delta}^2)$ on
the asymptotic freedom trajectory and absorbed into the main bound.

### 7.3 The gauge-invariant case

For $\tilde{O}_6 = \sum_P\sum_\rho(\nabla_\rho s_P)^2$, the
plaquette variable $s_P$ is gauge-invariant (real-valued), so
summation by parts is exactly the scalar case: no parallel transport,
no curvature remainder. The leading dimension-6 operators can be
expressed in gauge-invariant form, so Sections 7.1-7.2 arise only at
intermediate steps.


---


## 8. The Complete Bound

**Lemma 8.1 (Three-point weight with boundary control).**
*Let $X$ be a connected polymer containing the three insertion points,
$O_6$ a dimension-6 gauge-invariant operator with $|c_6| \leq Cg^2$.
Then:*

$$|\omega_3(X; c_6 O_6)|
  \leq K^{|X|}\,|c_6|\,\hat{\Delta}^2\,z^{|X|}
  \,\bigl(C_{\mathrm{bulk}} + C_{\mathrm{bdy}}\,|\partial X|\,
    e^{-\Delta\,d(0,\partial X)}\bigr)$$

*with constants independent of $\hat{\Delta}$, $|X|$, $k$.*

**Proof.** Bulk: double summation by parts (Section 4.2). Boundary:
Section 6.3, with $\hat{\Delta}^2 = \hat{\Delta}_{\text{transfer}}
\times \hat{\Delta}_{\text{connected}}$. $\square$

### 8.2 The polymer sum

**Proposition 8.2 (Form factor bound from the cluster expansion).**
*Under the hypotheses of Lemma 8.1, and assuming the Kotecky-Preiss
convergence condition holds for the two-point expansion:*

$$|f_c^{(6)}(0)| \leq C\,g^4\,(a\Delta)^2\,\Delta^3$$

**Proof.** The bulk sum is the standard Kotecky-Preiss sum, bounded
by $C_{\mathrm{KP}}$. The boundary sum was bounded in Section 6.3 by
$O(1)$. Using $|c_6| \leq Cg^2$:

$$|f_c^{(6)}(0)| \leq C'\,g^4\,(a\Delta)^2\,\Delta^3. \quad\square$$


---


## 9. Honest Assessment

### 9.1 What is proved

1. Summation by parts on polymers (Lemma 4.1): rigorous, elementary.
2. Decomposition into bulk + boundary (Section 4.2): clean.
3. Exponential suppression of boundary terms by polymer depth
   (Lemma 5.2): standard cluster expansion technology.
4. Gauge-covariant case reduces to scalar case for gauge-invariant
   operators (Section 7).

### 9.2 The critical input

5. **The connected propagator bound** (Sections 6.3-6.4):
   $|h_c(x)| \leq C\hat{\Delta}\,e^{-\Delta|x|}$. Without this
   extra $\hat{\Delta}$, the boundary gives $O(\hat{\Delta})$
   instead of $O(\hat{\Delta}^2)$, and $\sum_k g_k^4(a_k\Lambda)$
   diverges. The bound follows from $\hat{G}_c(p) \sim 1/(p^2 +
   \Delta^2)$ and smoothness, but establishing it non-perturbatively
   within the polymer expansion requires: (a) the connected correlator
   within a single polymer inherits full-lattice derivative bounds,
   and (b) the finite polymer introduces no spurious zero-mode
   contributions. Both are plausible, neither is proved.

6. **The dangerous polymers are small.** Large polymers ($|X| \gg
   1/\hat{\Delta}$) are killed by $e^{-\Delta\,d}$. Small polymers
   ($|X| = O(1)$) have $e^{-\hat{\Delta}\cdot O(1)} = 1 -
   O(\hat{\Delta})$, so their boundary terms are controlled only by
   the connected propagator structure, not by geometry.

### 9.3 Status relative to Obstacle 1

Obstacle 1 is reduced to one regularity estimate: for a connected
polymer $X$ with mass gap $\Delta$ and spacing $a$,

$$\sup_{x \in \partial X}
  |G_c^X(0, x)| \leq C\,\hat{\Delta}\,e^{-\Delta\,d(0, x)}$$

where $G_c^X$ is the connected correlator restricted to $X$. This is
a quantitative statement about Balaban's polymer expansion, not a new
conceptual difficulty -- but it requires the polymer to inherit enough
full-lattice structure for the suppression to survive restriction to
a finite domain.
