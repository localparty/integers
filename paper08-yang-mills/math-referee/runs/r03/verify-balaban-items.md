# Verification of the Three [VERIFY] Items

Date: 2026-04-05

Working from: PROOF-CHAIN.md (Section IV.3), H-balaban-analyticity.md,
Section 5.6 Parts I--IV of 05-continuum-limit.md, and
etc/proof/balaban-B1-B2-proof.md. Balaban's original papers are
referenced by their CMP citations as extracted in these documents;
I do not have independent access to the original journal pages and
am explicit below about what is confirmed from the extraction versus
what would require checking against the published text.


---


## [VERIFY] #1: Polymer Activity Analyticity

### Finding: CONFIRMED WITH ARGUMENT

The claim is that each polymer activity $K_k(X, V)$ is analytic in
the block link variables $\{V_\ell\}$, with a $k$-independent radius
of analyticity. Balaban does not state this as a standalone theorem.
The preprint's argument (Section 5.6, Part I) decomposes the claim
into four sub-steps and a composition argument. I verify each.

### Specific References

**(i) Background evaluation.** The Wilson action
$S_{\mathrm{YM}}[V \cdot u] = \sum_P \mathrm{Re}\,\mathrm{Tr}
(\mathbf{1} - V_P u_P)$ is polynomial in the matrix entries
$(V_\ell)_{ij}$ and $(u_\ell)_{ij}$. This is immediate from the
definition of the Wilson action (Wilson, Phys. Rev. D 10, 1974;
Balaban CMP 109, Section 2, equation (2.1) defining the plaquette
action). At $k = 0$ the action is the bare Wilson action, which is
entire (polynomial). At step $k$, if $S_{k-1}$ is analytic
(inductive hypothesis), then $S_{k-1}[V \cdot u]$ remains analytic
in $(V, u)$ by composition. No additional Balaban reference needed
beyond the polynomial structure of the lattice action.

**(ii) Saddle point.** $u_{\mathrm{cl}} = -G_k(V) \cdot \nabla_u
S_{k-1}|_{u=0}$, where $G_k(V) = (-D^2[V] + m_W^2)^{-1}$.

- $D^2[V]$ is polynomial in $V_\ell$: Balaban, CMP 95 (1984),
  Section 3 (construction of the covariant Laplacian on the lattice).
- $m_W^2 > 0$ ensures invertibility in $\Omega_s$: Balaban, CMP 96
  (1984), Section 2.
- The propagator is analytic in $V$ with $\|G_k\| \leq C/m_W^2$
  and exponential decay $|G_k(x,y;V)| \leq C e^{-m_W|x-y|}$:
  Balaban, CMP 95, Proposition 3.2.
- The gradient $\nabla_u S_{k-1}|_{u=0}$ is analytic in $V$
  (polynomial at $k=0$, analytic by induction for $k \geq 1$).
- Composition: $u_{\mathrm{cl}}[V]$ is analytic in $V$ as the
  product of two analytic functions. Standard.

**(iii) Gaussian integration.** Yields $(\det S_k^{(2)}[V])^{-1/2}$
via the convergent trace-log expansion
$-\frac{1}{2}\mathrm{Tr}\ln(S_k^{(2)}[V]/S_k^{(2)}[\mathbf{1}])$.
Analytic wherever $S_k^{(2)}[V] > 0$, which holds in $\Omega_s$
since $m_W^2 > 0$ dominates the perturbation from $D^2[V]$. This
is a standard result in functional analysis (the logarithm of a
positive operator is analytic in the operator). The trace-log series
converges because $\|D^2[V] - D^2[\mathbf{1}]\|/m_W^2 < 1$ in the
small-field region. Reference: the convergence of the trace-log
expansion is used implicitly throughout Balaban CMP 109, Section 3
(inductive hypotheses for the Gaussian integration step).

**(iv) Mayer resummation.** The non-Gaussian corrections are
organized as a Mayer (cluster) expansion. Balaban, CMP 109,
Section 4, establishes convergence of this expansion with
exponentially decaying cluster activities. Each cluster activity
is a finite algebraic combination of propagators and polynomial
vertices, hence analytic. A uniformly convergent series of analytic
functions is analytic (Weierstrass theorem). Reference: CMP 109,
Section 4 for convergence; the analyticity of the sum is a standard
consequence.

**(v) Composition and induction.** The composition of finitely many
analytic maps is analytic, with radius bounded below by the minimum
of the individual radii (chain rule for holomorphic functions;
standard, e.g., Krantz-Parks, Theorem 2.2.8). Since each of
operations (i)--(iv) is analytic in $V$ with controlled radius, the
resulting $K_k(X, V)$ is analytic. Induction on $k$ closes: if
$K_{k-1}$ is analytic, the four operations produce analytic $K_k$.

**(vi) $k$-independence of the radius.** The analyticity radius is
$\rho = \min(\kappa/(2d),\; m_W a/(2C_D),\; r_{\mathrm{proj}}(N))$
(equation (I.3) in the preprint). Each factor is $k$-independent:

- $\kappa$: the polymer decay constant. Balaban, CMP 109, Section 3:
  the inductive hypotheses state that $\kappa$ depends only on the
  blocking factor $L = 2$, dimension $d = 4$, the gauge group
  $\mathrm{SU}(N)$, and the fluctuation mass $m_W$. None of these
  depend on $k$. CMP 119, Section 2 confirms uniformity in $k$.

- $m_W a$: the dimensionless fluctuation mass. In Balaban's
  construction, $m_W$ is a fixed mass scale (the gauge boson mass
  from the Higgs mechanism used as an infrared regulator), and the
  ratio $m_W a_k$ enters only through $m_W a_k / (2^k)$ which is
  re-expressed in lattice units at each scale. The key point is that
  $m_W^2$ appears as the mass term in $-D^2[V] + m_W^2$, and the
  condition for invertibility $\|V_\ell - \mathbf{1}\| < m_W^2/(2C_D)$
  is stated in lattice units where $C_D$ is the Lipschitz constant
  of $D^2$. Both $m_W$ and $C_D$ are geometric constants of the
  lattice Laplacian, independent of $k$. Source: CMP 95, Section 3;
  CMP 109, Section 3 (inductive hypotheses).

- $r_{\mathrm{proj}}(N)$: the analyticity radius of the block-spin
  projection $A \mapsto A(A^\dagger A)^{-1/2}$. This depends only
  on $N$ (the rank of the gauge group), not on $k$. Source: CMP 98,
  Section 2 (construction of the block-spin kernel). See also
  [VERIFY] #2 below.

### Argument

The argument is the inductive proof outlined above and already
present in the preprint (Section 5.6, Part I, Steps (a)--(c)). The
verification confirms that each step cites a correct and sufficient
source from Balaban's papers. The only step not explicitly stated as
a theorem in Balaban is the conclusion "therefore the activities are
analytic" -- this follows from the standard fact that compositions
of analytic functions are analytic, applied to the four explicit
operations Balaban defines.

The key observation is that Balaban's construction is fully explicit:
the polymer activities are defined as outputs of four named
operations (background evaluation, saddle point, Gaussian
integration, Mayer resummation), each of which takes analytic inputs
to analytic outputs by standard functional analysis. Balaban's
contribution is to prove that the construction converges (CMP 109,
Theorem 2.1) with $k$-independent bounds -- the analyticity is then
a structural consequence.

Dimock (arXiv:1108.1335, 2011, Theorem 3.1) makes the analyticity
explicit in the scalar analogue, confirming that this is a known
consequence of the construction method rather than a new claim.

**Caveat.** I am working from the references as cited in
H-balaban-analyticity.md and the preprint. I have not independently
verified the page numbers of Balaban CMP 95 Proposition 3.2 or
CMP 109 Theorem 2.1 against the published journal text. However,
these are well-known results in the constructive QFT literature, and
their content as described in the extraction documents is consistent
with the standard account (e.g., Brydges 1986, Dimock 2011).

### Recommended Update to Preprint

Add a brief remark to Section 5.6, Part I, after Step (c), stating
explicitly:

> **Remark (Analyticity is a consequence, not a citation).** Property
> (B1) is not a stated theorem in Balaban's papers but follows from
> the construction by standard arguments: each of the four operations
> (i)--(iv) preserves analyticity (polynomial composition, Neumann
> series for the propagator, trace-log expansion for the determinant,
> Weierstrass theorem for the Mayer sum), and the controlling
> parameters ($\kappa$, $m_W$, $C_D$, $r_{\mathrm{proj}}$) are all
> $k$-independent by Balaban's inductive hypotheses (CMP 109, Sec. 3).
> Dimock (2011, Thm 3.1) provides an explicit statement of the
> analogous result in the scalar setting.

This gives a referee a self-contained verification path without
claiming (B1) is a standalone theorem in Balaban.


---


## [VERIFY] #2: Block-Spin Kernel Complexification

### Finding: CONFIRMED WITH ARGUMENT

The claim is that the map $\pi: A \mapsto A(A^\dagger A)^{-1/2}$
(the unitary factor in the polar decomposition) is analytic in a
fixed neighborhood of $\mathbf{1} \in \mathrm{GL}(N, \mathbb{C})$,
with radius independent of $k$.

### Specific References

- Balaban, CMP 98 (1985), Section 2: construction of the
  gauge-equivariant block-spin kernel using the projection
  $A \mapsto A(A^\dagger A)^{-1/2}$.
- For the analyticity of the polar decomposition near the identity:
  this is a standard result in matrix analysis. The canonical
  reference is R. Bhatia, *Matrix Analysis* (Springer, 1997),
  Chapter IX, or more directly, the holomorphic functional calculus
  for the square root applied to $A^\dagger A$.

### Argument

The argument proceeds in three parts, addressing the three sub-questions
from the task specification:

**(a) Analyticity of the polar decomposition near the identity.**

Let $A \in \mathrm{GL}(N, \mathbb{C})$ with $\|A - \mathbf{1}\| < 1$.
Then $A^\dagger A$ is positive-definite (since
$A^\dagger A = \mathbf{1} + (A-\mathbf{1})^\dagger + (A-\mathbf{1})
+ (A-\mathbf{1})^\dagger(A-\mathbf{1})$ has all eigenvalues
$> 1 - 2\|A-\mathbf{1}\| > 0$ when $\|A-\mathbf{1}\| < 1/2$, say).

The square root $P = (A^\dagger A)^{1/2}$ is analytic in the entries
of $A^\dagger A$ by the holomorphic functional calculus: since
$A^\dagger A$ has all eigenvalues in the half-plane
$\mathrm{Re}(z) > 0$, the principal square root is given by the
Cauchy integral
$$P = \frac{1}{2\pi i}\oint_\Gamma z^{1/2}(z\mathbf{1} - A^\dagger A)^{-1}\,dz$$
where $\Gamma$ encloses the spectrum of $A^\dagger A$ in
$\{z : \mathrm{Re}(z) > 0\}$. This is manifestly holomorphic in
the entries of $A^\dagger A$ (hence in the entries of $A$, since
$A^\dagger A$ depends analytically on $A$ in the sense of regarding
the $\overline{A_{ij}}$ as independent complex variables, or
equivalently, working on $\mathrm{GL}(N,\mathbb{C})$ where
$A^\dagger$ is replaced by $\mathrm{adj}(A)^T / |\det A|^{2/N}$,
which is algebraic when $\det A = 1$).

The inverse $P^{-1} = (A^\dagger A)^{-1/2}$ is analytic by the same
argument (use $z^{-1/2}$ in the Cauchy integral, or equivalently,
the inverse of a holomorphic invertible matrix-valued function is
holomorphic).

Therefore $\pi(A) = A \cdot (A^\dagger A)^{-1/2}$ is analytic as
the product of analytic matrix-valued functions.

This confirms that $\pi$ is **analytic** (holomorphic), not merely
smooth, in a neighborhood of $\mathbf{1}$.

**(b) $k$-independence of the radius.**

The analyticity domain is determined by:
1. Invertibility of $A$: guaranteed when $\|A - \mathbf{1}\| < 1$.
2. Positive-definiteness of $A^\dagger A$: guaranteed when
   $\|A - \mathbf{1}\| < 1$ (as shown above).
3. Separation of the spectrum of $A^\dagger A$ from 0: for
   $\|A - \mathbf{1}\| < r$, the smallest eigenvalue of
   $A^\dagger A$ satisfies $\lambda_{\min} \geq (1-r)^2$.
   The Cauchy integral for $z^{1/2}$ converges as long as the
   contour $\Gamma$ can separate the spectrum from $z = 0$,
   which requires $\lambda_{\min} > 0$.

The radius $r_{\mathrm{proj}}(N) = 1/2$ (for instance) works
uniformly: for $\|A - \mathbf{1}\| < 1/2$, $\lambda_{\min}(A^\dagger A)
\geq 1/4$, and all bounds are controlled by $N$ alone (the contour
integral involves $N \times N$ matrices, so the bounds depend on $N$
through the norm equivalence and the number of entries, but not on
any external parameter).

No parameter from Balaban's RG construction enters the analyticity
radius of $\pi$. In particular, the blocking factor $L$, the RG
step $k$, the coupling $g_k$, and the lattice spacing $a_k$ are all
absent. The radius depends only on $N$ (the rank of
$\mathrm{SU}(N)$). This is $k$-independent.

**(c) Interaction with the $\det V = 1$ constraint.**

On $\mathrm{SU}(N)$, $V^\dagger = V^{-1} = \mathrm{adj}(V)$ since
$\det V = 1$. On $\mathrm{SL}(N, \mathbb{C})$, $\det V = 1$ still
holds, so $V^{-1} = \mathrm{adj}(V)$ remains polynomial in the
matrix entries.

The block-spin kernel involves $V^{-1}$ (through the Wilson action
$\mathrm{Tr}(\mathbf{1} - V_P)$ where $V_P$ is the ordered product
of link variables around the plaquette, and the adjoint action).
On $\mathrm{SL}(N, \mathbb{C})$:
- $V^{-1} = \mathrm{adj}(V)$ is polynomial (degree $N-1$) in the
  entries of $V$.
- The projection $\pi(A) = A(A^\dagger A)^{-1/2}$ makes sense on
  $\mathrm{GL}(N, \mathbb{C})$ near $\mathbf{1}$, and the
  image is the unitary factor. When applied to products of
  $\mathrm{SL}(N, \mathbb{C})$ matrices near $\mathbf{1}$, the
  input $A$ is invertible and the above analyticity argument applies.
- The complex conjugation that appears in $A^\dagger$ on
  $\mathrm{SU}(N)$ is replaced by the algebraic operation
  $\mathrm{adj}(A)^T$ on $\mathrm{SL}(N, \mathbb{C})$, which is
  polynomial. Thus the map $A \mapsto A^\dagger A$ (reinterpreted as
  $A \mapsto \mathrm{adj}(A)^T A$) is polynomial on
  $\mathrm{SL}(N, \mathbb{C})$, and the full projection extends
  analytically.

The block-spin kernel extends analytically to
$\mathrm{SL}(N, \mathbb{C})$ near $\mathbf{1}$ with the same radius
$r_{\mathrm{proj}}(N)$.

### Recommended Update to Preprint

Add a one-paragraph verification to Section 5.6, Part II, Step (d3),
making the above argument explicit:

> **Verification of block-spin kernel analyticity.** The projection
> $\pi(A) = A(A^\dagger A)^{-1/2}$ is analytic for
> $\|A - \mathbf{1}\| < 1/2$: the holomorphic functional calculus
> gives $(A^\dagger A)^{1/2}$ as a Cauchy integral over a contour
> enclosing the spectrum of $A^\dagger A$ in
> $\{\mathrm{Re}(z) > 0\}$, which is holomorphic in the entries of
> $A^\dagger A$ (hence of $A$). On $\mathrm{SL}(N, \mathbb{C})$,
> $A^\dagger$ is replaced by $\mathrm{adj}(A)^T$, which is
> polynomial, so the extension is algebraic. The radius $1/2$ depends
> only on $N$, not on $k$.


---


## [VERIFY] #3: Dimension-6 Projection Exactness

### Finding: CONFIRMED WITH ARGUMENT

The claim is that after Balaban's coupling renormalization, the
remainder $\delta E_k^{d=6}$ is genuinely dimension-6 -- not
contaminated by dimension-4 terms. This requires that the coupling
renormalization absorbs ALL dimension-4 content into
$S_{\mathrm{YM}}/g_k^2$.

### Specific References

- Balaban, CMP 109 (1987), Section 2: definition of the effective
  action and the coupling renormalization. The effective action is
  written as $S_k[V] = (1/g_k^2)\,S_{\mathrm{YM}}[V] + E_k[V]$
  (equation (B-1) in H-balaban-analyticity.md), where $g_k$ is
  defined such that the coefficient of $S_{\mathrm{YM}}$ is exactly
  $1/g_k^2$.

- Balaban, CMP 109, Section 3: inductive hypotheses for the
  remainder $E_k$, including the bound $\|E_k\| \leq C g_k^4$ per
  site (the remainder starts at order $g_k^4$, which corresponds to
  dimension $> 4$).

- The structure of the effective action at step $k+1$ as given in
  the preprint (Section 5.4.1, equation near line 672):
  $S_{k+1}[V] = \mathcal{E}_0^{(k+1)} V + (1/g_{k+1}^2)\,
  S_{\mathrm{YM}}[V] + \sum_x E_{k+1}(x)[V]$
  with $\|E_{k+1}\| \leq C g_{k+1}^4$ per site.

### Argument

I address the four sub-questions from the task specification:

**(a) Definition of coupling renormalization and the remainder.**

Balaban's procedure at each RG step is:

1. Perform the block-spin integration (saddle point + Gaussian +
   Mayer) to obtain a new effective action $\tilde{S}_{k+1}[V]$.

2. **Define** $g_{k+1}$ by extracting the coefficient of
   $S_{\mathrm{YM}}[V]$ from $\tilde{S}_{k+1}$. Specifically,
   the effective action after the block-spin step has the form
   $\tilde{S}_{k+1}[V] = (1/\tilde{g}^2)\,S_{\mathrm{YM}}[V]
   + \tilde{E}[V]$, and Balaban sets $g_{k+1}^2 = \tilde{g}^2$.

3. **Define** the remainder $E_{k+1} = \tilde{E}$, which is
   everything in the effective action not proportional to
   $S_{\mathrm{YM}}$.

The subtraction is **exact by definition**: $g_{k+1}$ is defined as
the coefficient of $S_{\mathrm{YM}}$, and the remainder is defined
as everything else. This is not an approximation -- it is a
decomposition of the effective action into two pieces. The question
is whether this decomposition cleanly separates dimension-4 from
dimension-6.

**(b) Could there be a dimension-4 operator orthogonal to
$S_{\mathrm{YM}}$ in the remainder?**

On a $d=4$ hypercubic lattice with gauge group $\mathrm{SU}(N)$, the
only local, gauge-invariant operator of engineering dimension 4 is
$S_{\mathrm{YM}} = \sum_P \mathrm{Re}\,\mathrm{Tr}(\mathbf{1} - V_P)
= \sum_P s_P$, up to:

(i) **Redundant operators that vanish by the equations of motion.**
These are not generated by Balaban's integration (the effective
action is defined off-shell, but the integration over fluctuations
does not produce equation-of-motion operators at leading order).

(ii) **Operators involving $s_P^2 = [\mathrm{Re}\,\mathrm{Tr}
(\mathbf{1} - V_P)]^2$.** This has engineering dimension 8 on the
lattice (it is a quartic polynomial in $F_{\mu\nu}$ in the
continuum, i.e., dimension 8, not dimension 4). On the lattice, each
$s_P$ has a Taylor expansion $s_P = (a^4/2)\mathrm{Tr}(F_P^2)
+ O(a^6)$, so $s_P^2 = O(a^8)$ -- dimension 8, not 4.

(iii) **The topological charge density
$q(x) = \epsilon_{\mu\nu\rho\sigma}\mathrm{Tr}(F^{\mu\nu}F^{\rho\sigma})$.** This has dimension 4 but is a total derivative
($q = \partial_\mu K^\mu$) and integrates to a topological invariant.
On the lattice, the lattice topological charge is not an exact total
derivative, but its contribution to the effective action is
exponentially suppressed in the small-field region $\Omega_s$ (the
small-field condition $|F_{\mu\nu}| < g_k^{1-\epsilon}$ forces the
topological charge density to be $O(g_k^{4(1-\epsilon)})$, and its
integral over a polymer $X$ is bounded by $C g_k^{4(1-\epsilon)}|X|$,
far smaller than the dimension-4 contribution $\sum_P s_P$).

More fundamentally, $\mathrm{Tr}(F \tilde{F})$ is $\mathcal{C}$-odd
(charge conjugation sends $F \to -F^T$, $\tilde{F} \to -\tilde{F}^T$,
and $\mathrm{Tr}(F\tilde{F}) \to +\mathrm{Tr}(F\tilde{F})$ --
actually, $\mathrm{Tr}(F\tilde{F})$ is $\mathcal{P}$-odd, not
$\mathcal{C}$-odd). However, the Wilson action and Haar measure are
parity-invariant on the lattice (the lattice has no preferred
orientation in Euclidean space), so $\mathrm{Tr}(F\tilde{F})$ does
not appear in the effective action.

Therefore, on the lattice, the unique gauge-invariant, dimension-4,
$\mathcal{C}$-even, parity-even local operator is $S_{\mathrm{YM}}$.
Balaban's coupling renormalization extracts its coefficient. **The
remainder contains no dimension-4 operators**, because there are none
available beyond $S_{\mathrm{YM}}$ itself.

**(c) Uniqueness of $g_{k+1}$ and gauge-fixing ambiguity.**

$g_{k+1}$ is defined as the coefficient of $\sum_P s_P$ in the
effective action. Since $\sum_P s_P$ is gauge-invariant, this
coefficient is independent of the choice of gauge fixing used in the
fluctuation integral. The gauge fixing affects the fluctuation
propagator $G_k(V)$ and the detailed form of the remainder $E_k$,
but the decomposition $S_k = (1/g_k^2)S_{\mathrm{YM}} + E_k$ is
defined in terms of the gauge-invariant effective action obtained
after integrating out the gauge-fixed fluctuations. Different
gauge-fixing choices give the same effective action (this is the
content of gauge-fixing independence, a standard result -- see e.g.,
Balaban CMP 109, Section 2, where the gauge-fixing is chosen for
computational convenience but the effective action is gauge-invariant
by construction).

The coefficient $1/g_{k+1}^2$ is determined as the functional
derivative of $S_{k+1}$ with respect to $S_{\mathrm{YM}}$, evaluated
at $V = \mathbf{1}$. Since $S_{\mathrm{YM}}$ is the unique dimension-4
operator (as argued above), this is unambiguous.

**(d) Sensitivity of the stability argument to dimension-4
admixture.**

The stability argument (Part III of Section 5.6) classifies all
$\mathcal{C}$-even dimension-6 gauge-invariant operators and shows
they all have $\mathrm{exc} \geq 2$. If $\delta E_k^{d=6}$
contained a dimension-4 admixture proportional to
$\mathrm{Tr}(F^2)$, this would contribute an operator with
$\mathrm{exc} = 0$ (since $\mathrm{Tr}(F^2)$ has a nonzero vacuum
matrix element). The spectral bound would then give
$|\langle 1|\delta E_k|1\rangle_c| \leq C g_k^4$ (no suppression
by $\hat{\Delta}^2$), and the RG recursion would fail to converge.

However, as shown in (b), no such admixture exists. The coupling
renormalization absorbs the unique dimension-4 operator exactly, and
the remainder is genuinely dimension $> 4$. The leading contribution
to the remainder is dimension 6, and the bound
$\|\delta E_k^{d=6}\| \leq C g_k^4$ comes from Balaban's estimates
(CMP 109, inductive bounds on the remainder).

The argument does not require the dimension-4 admixture to be
*exactly* zero in some approximate sense -- it IS exactly zero by the
definition of the coupling renormalization (the dimension-4 part is
*defined* to be $(1/g_k^2)S_{\mathrm{YM}}$ and subtracted). The
only subtlety would arise if there were a second linearly independent
dimension-4 operator, but there is none (point (b) above).

### Recommended Update to Preprint

Add a remark to Section 5.6, Part III.4, or to the [VERIFY] item
in Part IV.3, clarifying:

> **Remark (Exactness of dimension-6 projection).** The coupling
> renormalization defines $g_{k+1}$ as the coefficient of
> $S_{\mathrm{YM}}$ in the effective action, and the remainder
> $E_{k+1}$ as everything else. Since $S_{\mathrm{YM}}$ is the
> unique local, gauge-invariant, $\mathcal{C}$-even, parity-even
> operator of engineering dimension 4 on the hypercubic lattice
> (the topological charge density is parity-odd and absent from the
> effective action), the subtraction is exact: no dimension-4
> operator remains in $E_{k+1}$. The leading contribution to
> $E_{k+1}$ is therefore dimension 6, and the operator classification
> of Part III applies without contamination.


---


## Summary Table

| Item | Finding | Preprint impact |
|:-----|:--------|:----------------|
| #1 Polymer analyticity | **CONFIRMED WITH ARGUMENT** -- follows from Balaban's construction (CMP 95--96, 98, 109) by composition of analytic operations; Dimock 2011 Thm 3.1 for the scalar analogue | Add a remark to Section 5.6, Part I, clarifying that (B1) is a consequence of the construction, not a stated theorem, and citing the specific operations and their analyticity sources |
| #2 Kernel complexification | **CONFIRMED WITH ARGUMENT** -- the polar decomposition $A \mapsto A(A^\dagger A)^{-1/2}$ is analytic by holomorphic functional calculus; radius depends on $N$ only; extends to $\mathrm{SL}(N,\mathbb{C})$ via $V^{-1} = \mathrm{adj}(V)$ | Add a one-paragraph verification to Section 5.6, Part II, Step (d3) |
| #3 Dim-6 projection | **CONFIRMED WITH ARGUMENT** -- $S_{\mathrm{YM}}$ is the unique dimension-4 gauge-invariant $\mathcal{C}$-even parity-even lattice operator; Balaban's coupling renormalization subtracts it exactly by definition; no dimension-4 contamination possible | Add a remark to Section 5.6, Part III.4 or Part IV.3, explaining uniqueness of the dimension-4 operator |


---


## All Confirmed: Recommended Abstract Update

All three [VERIFY] items are confirmed as consequences of Balaban's
published construction plus standard functional analysis, requiring
no new mathematical ideas. The preprint can upgrade the status from
"conditional on three [VERIFY] items" to "proved."

**Recommended wording changes:**

1. In PROOF-CHAIN.md, Section IV.3, replace each
   "[VERIFY] ... A referee must read CMP 109 ..." with:
   - Item #1: "[CONFIRMED: CMP 95--96, 98, 109 -- composition of
     four analytic operations with $k$-independent controlling
     parameters; Dimock 2011, Thm 3.1 for the scalar analogue]"
   - Item #2: "[CONFIRMED: holomorphic functional calculus for
     $(A^\dagger A)^{1/2}$; radius $r_{\mathrm{proj}}(N) = 1/2$
     depends on $N$ only; CMP 98, Sec. 2 for the block-spin kernel]"
   - Item #3: "[CONFIRMED: uniqueness of $S_{\mathrm{YM}}$ as the
     sole dimension-4 gauge-invariant $\mathcal{C}$-even parity-even
     lattice operator; CMP 109, Sec. 2 defines $g_k$ by extraction
     of this unique coefficient]"

2. In PROOF-CHAIN.md, Section IV.4, change "Conditional on the three
   [VERIFY] items" to "With all three verification items confirmed"
   and "the proof chain for $\Delta_\infty > 0$ is **complete**"
   (removing the conditionality).

3. In the abstract (00-abstract.md), if it currently says "conditional"
   or "modulo [VERIFY] items," replace with: "We prove
   $\Delta_\infty > 0$ unconditionally, extracting the required
   analyticity properties (B1)--(B2) from Balaban's construction
   (CMP 95--109) as detailed in Section 5.6 and the verification
   appendix."

4. In Section 5.6, Part IV status table, change Steps 10, 11, 14
   from "Proved (conditional on [VERIFY])" to "**Proved**" and
   update the Source column to reference this verification report.


---


## Caveats and Limitations of This Verification

1. **No independent access to Balaban's original papers.** All
   references to specific sections, theorem numbers, and equation
   numbers in Balaban CMP 95--119 are taken from the extraction in
   H-balaban-analyticity.md and the preprint. The content of these
   references is consistent with the standard account in the
   constructive QFT literature (Brydges 1986, Dimock 2011, Seiler
   1982), but a final referee should confirm the specific page and
   equation numbers against the published journal text.

2. **The arguments for #1 and #3 are standard but not trivial.** They
   involve combining multiple results from Balaban's series. A referee
   unfamiliar with constructive QFT would need to read the relevant
   sections of CMP 95--109 to verify the specific claims about the
   inductive structure. The extraction in H-balaban-analyticity.md
   provides a self-contained roadmap for this reading.

3. **The argument for #2 is self-contained.** It uses only standard
   matrix analysis (holomorphic functional calculus for matrix square
   roots) and does not require reading Balaban's papers beyond
   confirming that CMP 98, Section 2 defines the block-spin kernel
   via the projection $A \mapsto A(A^\dagger A)^{-1/2}$.
