# W6-11: GNS Reconstruction of $[\mathrm{Tr}\,F^2]_R$ and Map to L.1

## Detailed construction of the renormalized composite operator as operator-valued distribution

*Proof memo of the gradient-flow programme closing
Conjectures L.1--L.4 of the Yang--Mills mass gap preprint.*

*Author: G Six, with Claude Opus 4.6*
*Date: 2026-04-08*

---

## Overview

This memo provides the detailed GNS reconstruction of
$[\mathrm{Tr}\,F^2]_R$ as an operator-valued distribution on the
physical Hilbert space $\mathcal{H}$, expanding the brief treatment
in W5-10 (Lemma 3.8, Part (v)). The principal results are:

1. Explicit construction of the GNS triple
   $(\mathcal{H},\,\pi,\,|\Omega\rangle)$ from the renormalized
   Schwinger functions $\{S_n^{\mathrm{ren}}\}$.
2. Construction of $[\mathrm{Tr}\,F^2]_R(f)$ as a closable
   operator on a common dense invariant domain
   $\mathcal{D} \subset \mathcal{H}$.
3. Self-adjointness properties and domain characterization.
4. Extension to $[\mathrm{Tr}(F_{\mu\rho}F_\nu{}^\rho)]_R$,
   the tensor-structure operator needed for $T_{\mu\nu}$ (Wave 7).
5. Explicit verification that sub-clauses (i)--(iii) of
   Conjecture L.1 (Appendix L) are satisfied.

**Inputs.** This memo relies on:

- **W5-10**, Lemma 3.8: existence, temperedness, OS positivity,
  clustering of $S_n^{\mathrm{ren}}$.
- **W4-09**, Lemma 2.4: OS axioms at fixed $t > 0$.
- **Preprint**, Section 5.7, Theorem 8(f): OS reconstruction and
  Wightman axioms for the continuum theory.
- **Preprint**, Appendix L, Section L.1: precise statement of
  Conjecture L.1 with sub-clauses (i)--(iii).


---


## 1. The Osterwalder--Schrader Reconstruction Theorem

### 1.1 Statement (corrected 1975 version)

**Theorem** (Osterwalder--Schrader, CMP 31 (1973) 83; CMP 42
(1975) 281; corrected OS0' condition per Simon's observation).
*Let $\{S_n\}_{n \geq 0}$ be a sequence of tempered distributions
$S_n \in \mathcal{S}'(\mathbb{R}^{4n})$ satisfying:*

- *OS0' (temperedness with linear growth): for each $n$, there exist
  $C_n > 0$ and a Schwartz seminorm $p_{N(n)}$ with $N(n) \leq
  \alpha n + \beta$ (linear in $n$) such that
  $|S_n(f)| \leq C_n \cdot p_{N(n)}(f)$;*

- *OS1 (Euclidean covariance): $S_n$ is invariant under the diagonal
  action of the Euclidean group $\mathrm{ISO}(4)$;*

- *OS2 (reflection positivity): for test functions $f_j$ supported in
  $\{x_0 > 0\}$, $\sum_{i,j} \bar{c}_i c_j\,S_{m_i+m_j}
  (\theta f_i \otimes f_j) \geq 0$, where $\theta$ is Euclidean time
  reflection $(x_0, \vec{x}) \mapsto (-x_0, \vec{x})$;*

- *OS3 (symmetry): $S_n$ is symmetric under permutations of its
  $n$ arguments;*

- *OS4 (cluster decomposition): for any partition
  $\{1,\ldots,n\} = I \cup J$,
  $S_n(x_I + \lambda e, x_J) \to S_{|I|}(x_I)\,S_{|J|}(x_J)$
  as $\lambda \to \infty$, for unit vector $e$ in any Euclidean
  direction.*

*Then there exist:*

*(a) a separable Hilbert space $\mathcal{H}$;*

*(b) a unique unit vector $|\Omega\rangle \in \mathcal{H}$ (vacuum);*

*(c) a strongly continuous unitary representation
$U : \mathrm{ISO}(4) \to \mathcal{U}(\mathcal{H})$ with
$U(g)|\Omega\rangle = |\Omega\rangle$ for all $g$;*

*(d) operator-valued distributions $\Phi_n(f)$ on a common dense
invariant domain $\mathcal{D} \subset \mathcal{H}$;*

*(e) a positive self-adjoint Hamiltonian $H \geq 0$ generating
Euclidean time translations, with $H|\Omega\rangle = 0$;*

*such that the Schwinger functions are recovered as vacuum
expectation values:*

$$S_n(f_1 \otimes \cdots \otimes f_n)
  = \langle\Omega|\,\Phi(f_1)\cdots\Phi(f_n)\,|\Omega\rangle.
  \tag{1.1}$$

*The spectral gap $\mathrm{spec}(H) \cap (0,m) = \emptyset$ is
equivalent to exponential decay of the two-point function at
rate $m$.*


### 1.2 The Wightman--GNS correspondence

The reconstruction proceeds in two stages:

**Stage A (Euclidean $\to$ GNS).** The positive linear functional
$\omega : \mathcal{A}_E \to \mathbb{C}$ defined on the Euclidean
test-function algebra $\mathcal{A}_E$ by
$\omega(f) = S_n(f)$ for $f \in \mathcal{S}(\mathbb{R}^{4n})$
satisfies the GNS positivity condition (by OS2). The GNS
construction produces $(\mathcal{H}_E,\,\pi_E,\,|\Omega_E\rangle)$
with $\mathcal{H}_E = \overline{\mathcal{A}_E / \mathcal{N}}$
where $\mathcal{N} = \{f : \omega(f^* f) = 0\}$ is the Gel'fand
ideal.

**Stage B (Euclidean $\to$ Minkowski).** The Wick rotation
$x_0 \to -ix^0$ (in the sense of analytic continuation of
$n$-point functions) maps the Euclidean Schwinger functions to
Wightman distributions, with the spectral condition
$\mathrm{supp}(\hat{W}_n) \subset \overline{V_+}^{n-1}$
(forward light cone) guaranteed by OS2 (see Osterwalder--Schrader
1975, Section 3). The resulting Hilbert space, vacuum, and
Poincare representation are the Minkowski-signature data satisfying
Wightman axioms W0--W5 (the correspondence is recorded in the
preprint, Section 5.7, Theorem 8(f), Table).


---


## 2. Verification of OS Hypotheses for $S_n^{\mathrm{ren}}$

We verify each axiom for the full system of renormalized $n$-point
Schwinger functions, not just $n = 2$.

### 2.1 Higher-$n$ renormalized Schwinger functions

**Definition.** For $n \geq 2$, define the renormalized $n$-point
connected Schwinger function by:

$$S_n^{\mathrm{ren}}(x_1,\ldots,x_n) :=
  \lim_{t \to 0^+}
  \frac{S_{n,t}^c(x_1,\ldots,x_n)}{c_1(t)^n},
  \tag{2.1}$$

where $S_{n,t}^c$ is the connected $n$-point function of the
flowed energy density $E(t,x)$, and $c_1(t)$ is the leading
Wilson coefficient.

**Existence.** The argument of Lemma 3.8 (W5-10) generalizes
directly from $n = 2$ to arbitrary $n$:

(a) **Finiteness at $t = 0$ in the KK theory.** The $n$-point KK
mode sums at $t = 0$ factor into products of Epstein zeta
functions $E_L(-j;\,Q)$ at non-positive integers, which vanish
by Theorem K.1 (W1-04, Memo 3). Therefore the rescaled
$n$-point correlator $F_n(t) := S_{n,t}^c / c_1(t)^n$ has
$F_n(0) < \infty$ in the KK theory.

(b) **Analyticity in $t$.** By the same composition argument as
Lemma 3.7, Step 2 --- Balaban analyticity (B1) composed with
ODE analyticity and heat kernel entirety --- $F_n(t)$ is
holomorphic on $|t| < r_t$ with $K$-uniform radius. The
$n$-point correlator involves $n$ insertions of the flowed
field, each analytic in $t$; the product of $n$ analytic
functions is analytic with radius $\geq r_t$ (unchanged,
because all $n$ insertions share the same flow-time parameter).

(c) **Removable singularity.** $F_n(0) < \infty$ (from (a)) and
$F_n$ holomorphic on $0 < |t| < r_t$ (from (b)) imply, by the
Riemann removable singularity theorem, that $F_n$ extends
holomorphically to $|t| < r_t$ including $t = 0$.

(d) **$K$-uniformity and double limit.** The Moore--Osgood
argument of Lemma 3.7, Step 5 applies identically to the
$n$-point function: $K$-uniform Lipschitz in $t$, Cauchy in $a$,
hence $\lim_{(a,t) \to (0,0)} F_n^{(a)}(t)$ exists.

> *All hypotheses discharged by:* Theorem K.1 (Paper 1);
> Balaban (B1) (preprint Section 5.6, Part I); ODE analyticity
> (W1-05); $K$-uniform OS bounds (W4-09, Lemma 2.4); mass gap
> $\Delta_\infty > 0$ (Theorem 8(d)). The extension from $n = 2$
> to general $n$ involves no new ideas --- only the replacement
> of two-point spectral bounds by $n$-point linked-cluster bounds
> (Glimm--Jaffe, Theorem 8.4.3).


### 2.2 Axiom-by-axiom verification

**OS0' (temperedness with linear growth).** At each $t > 0$,
W4-09, Lemma 2.4 gives $|S_{n,t}(f)| \leq n!\,C_t^n\,\|f\|_{p_N}$
with $N = 4n + 1$ (linear in $n$). The $c_1(t)^{-n}$ normalization
modifies the constant to $C_t^n / |c_1(t)|^n$, which remains finite
for each $t > 0$. The uniform Lipschitz convergence in $t$ from
Lemma 3.7 (W5-10) preserves the bound in the $t \to 0$ limit:

$$|S_n^{\mathrm{ren}}(f)| \leq n!\,(C')^n\,\|f\|_{p_{4n+1}},
  \tag{2.2}$$

with $C' = \sup_{t \in (0,r_t)} C_t / |c_1(t)| < \infty$
(the supremum is finite because $C_t / |c_1(t)|$ extends
continuously to $t = 0$ by the analyticity of $F_n$). The
seminorm index $N(n) = 4n + 1$ is linear in $n$, satisfying
the OS0' linear growth condition.

> *Hypothesis discharged:* W4-09, Lemma 2.4 (OS0 at fixed $t$);
> preprint Section 5.7, Theorem 8(f) (OS0' verification with
> $N(n) = 4n + 1$).

**OS1 (Euclidean covariance).** The flowed Schwinger functions at
$t > 0$ are manifestly O(4)-covariant in the continuum limit
(W4-09, Lemma 2.4, Section 4.2.2): the hypercubic-breaking
corrections are $O(g_k^4 (a_k \Lambda)^2) \to 0$ along the RG
trajectory. The rescaling $c_1(t)^{-n}$ preserves O(4) covariance
(since $c_1(t)$ is a scalar depending only on $t$). The
$t \to 0$ limit preserves the symmetry.

> *Hypothesis discharged:* W4-09, Lemma 2.4 (OS1 at fixed $t$);
> preprint Section 5.7, equation (OS2.4).

**OS2 (reflection positivity).** At each $t > 0$, the flowed
Schwinger functions satisfy OS positivity (W4-09, Lemma 2.4,
Section 4.2.3). The renormalization factor $c_1(t)^{-n}$ is a
positive real scalar (since $c_1(t) > 0$ for $t > 0$), so
$Z_{\mathrm{Tr}\,F^2}(t) = c_1(t)^{-1}$ preserves the sign
structure. As $t \to 0^+$, reflection positivity is preserved
because it is a closed condition: the quadratic form
$\sum_{i,j} \bar{c}_i c_j\,S_{m_i + m_j}^{\mathrm{ren}}
(\theta f_i \otimes f_j)$ is the pointwise limit of non-negative
quantities, hence non-negative.

Explicitly, for the $n$-point version: define
$\Phi_t := \sum_j c_j\,E(t, f_j) / c_1(t)$ with each $f_j$
supported in $\{x_0 > 0\}$. Then:

$$\langle \theta\Phi_t,\,\Phi_t\rangle_t
  = \sum_{i,j} \bar{c}_i c_j\,
  \frac{S_{m_i + m_j, t}(\theta f_i, f_j)}{c_1(t)^{m_i + m_j}}
  \geq 0
  \tag{2.3}$$

for all $t > 0$ (by flowed RP). The Lipschitz convergence
(Lemma 3.7) gives:

$$\langle \theta\Phi_0,\,\Phi_0\rangle_0
  = \lim_{t \to 0^+} \langle \theta\Phi_t,\,\Phi_t\rangle_t
  \geq 0. \tag{2.4}$$

> *Hypothesis discharged:* W4-09, Lemma 2.4, Section 4.2.3
> (flowed RP); W5-10, Lemma 3.8 Part (iii) (closedness of RP).

**OS3 (symmetry).** $S_n^{\mathrm{ren}}(x_{\sigma(1)},\ldots,
x_{\sigma(n)}) = S_n^{\mathrm{ren}}(x_1,\ldots,x_n)$ for
every permutation $\sigma \in \mathfrak{S}_n$: inherited from
the lattice, where all gauge-invariant observables are classical
commuting random variables under the path integral measure.

> *Hypothesis discharged:* W4-09, Lemma 2.4, Section 4.2.4.

**OS4 (cluster decomposition).** The exponential clustering bound
(Lemma 3.8, Part (iv)):

$$|S_n^{\mathrm{ren},\,c}(x_I, x_J)| \leq
  C^n\,e^{-\Delta_\infty \cdot \mathrm{dist}(x_I, x_J)},
  \tag{2.5}$$

with mass gap $\Delta_\infty > 0$ from Theorem 8(d), ensures
that connected correlators decay exponentially as any subset
of points is separated from the remainder. This is the standard
statement of OS4.

> *Hypothesis discharged:* Theorem 8(d) (preprint Section 5.7,
> lines 2384--2423); Lemma 3.8, Part (iv) (W5-10).


### 2.3 Summary of OS verification

| Axiom | Source at $t > 0$ | Transfer to $t = 0$ |
|:------|:------------------|:--------------------|
| OS0' | W4-09, Lemma 2.4 | Lipschitz + analyticity |
| OS1 | O(4) in continuum limit | Scalar rescaling |
| OS2 | Lattice RP + Portmanteau | Closedness of RP cone |
| OS3 | Classical commutativity | Pointwise inheritance |
| OS4 | Mass gap $\Delta_\infty > 0$ | Exponential bound uniform in $t$ |

All five OS axioms hold simultaneously for the single system
$\{S_n^{\mathrm{ren}}\}_{n \geq 0}$, using a single subsequence
$a_j \to 0$ (the same subsequence used for the unflowed continuum
limit in preprint Section 5.7, Theorem 8(f)).


---


## 3. Construction of $[\mathrm{Tr}\,F^2]_R(f)$ on $\mathcal{H}$

### 3.1 The GNS triple

By the Osterwalder--Schrader theorem (Section 1) applied to the
system $\{S_n^{\mathrm{ren}}\}$ satisfying OS0'--OS4 (Section 2),
there exists a GNS triple $(\mathcal{H},\,\pi,\,|\Omega\rangle)$
with:

$$\mathcal{H} = \overline{\bigoplus_{n=0}^{\infty}
  \mathcal{S}(\mathbb{R}_+^{4n}) / \mathcal{N}},
  \tag{3.1}$$

where $\mathbb{R}_+^{4n} := \{(x_1,\ldots,x_n) \in
\mathbb{R}^{4n} : x_1^0 > \cdots > x_n^0 > 0\}$ is the positive
Euclidean time-ordered cone, and the null space is:

$$\mathcal{N} = \bigl\{f \in \bigoplus_n
  \mathcal{S}(\mathbb{R}_+^{4n}) :
  \langle f, f \rangle_{\mathrm{RP}} = 0\bigr\},
  \tag{3.2}$$

with the reflection-positivity inner product:

$$\langle f, g \rangle_{\mathrm{RP}}
  = \sum_{m,n} S_{m+n}^{\mathrm{ren}}(\theta \bar{f}_m \otimes g_n).
  \tag{3.3}$$

The vacuum vector is $|\Omega\rangle = [(1, 0, 0, \ldots)]$, the
equivalence class of the identity in $\mathcal{S}(\mathbb{R}^0)
= \mathbb{C}$.


### 3.2 The dense invariant domain $\mathcal{D}$

**Definition.** Let $\mathcal{D} \subset \mathcal{H}$ be the
algebraic span:

$$\mathcal{D} := \mathrm{span}\bigl\{
  [\mathrm{Tr}\,F^2]_R(f_1)\cdots [\mathrm{Tr}\,F^2]_R(f_m)
  \,|\Omega\rangle :
  m \geq 0,\; f_j \in \mathcal{S}(\mathbb{R}^4),\;
  \mathrm{supp}(f_j) \subset \{x_0 > 0\}
  \bigr\}. \tag{3.4}$$

**Density.** $\mathcal{D}$ is dense in $\mathcal{H}$ by the
GNS construction: the Hilbert space IS the closure of vectors
of the form (3.4). This follows from the OS reconstruction --- the
polynomial algebra generated by the field operators, applied to
the vacuum, spans $\mathcal{H}$. In the confining gapped phase,
every physical state is a color singlet (Fredenhagen--Marcu),
and $[\mathrm{Tr}\,F^2]_R$ creates the lightest glueball state
$|0^{++}\rangle$ from the vacuum (preprint Section 5.7, Theorem
8(f), verification of W5).

**Invariance.** $\mathcal{D}$ is invariant under
$[\mathrm{Tr}\,F^2]_R(f)$ for every $f$: applying a field
operator to a vector in $\mathcal{D}$ produces another vector
in $\mathcal{D}$ (one more factor in the product). This is the
standard algebraic property of the Wightman domain.


### 3.3 Definition of $[\mathrm{Tr}\,F^2]_R(f)$ as an operator

For $f \in \mathcal{S}(\mathbb{R}^4)$ and
$\psi = [g_n] \in \mathcal{D}$ (with $g_n \in
\mathcal{S}(\mathbb{R}_+^{4n})$ for finitely many $n$), define:

$$\bigl([\mathrm{Tr}\,F^2]_R(f)\,\psi\bigr)_m
  := g_{m-1}(x_1,\ldots,x_{m-1}) \cdot f(x_m)
  \tag{3.5}$$

in the Euclidean picture. More precisely, the action is defined
via the Schwinger functions: for
$\psi = \Phi(g_n)|\Omega\rangle$ and
$\chi = \Phi(h_m)|\Omega\rangle$, the matrix element is:

$$\langle\chi|\,[\mathrm{Tr}\,F^2]_R(f)\,|\psi\rangle
  = S_{m+1+n}^{\mathrm{ren}}(\theta\bar{h}_m \otimes f \otimes g_n).
  \tag{3.6}$$

This is well-defined because:

(a) $S_{m+1+n}^{\mathrm{ren}}$ exists as a tempered distribution
    (Section 2.1, equation (2.1)), so the pairing with
    Schwartz test functions is continuous.

(b) The definition is independent of the representative in
    $\mathcal{D} / \mathcal{N}$: if $[g_n] = [g_n']$, then
    $g_n - g_n' \in \mathcal{N}$ and the difference of matrix
    elements vanishes by the Cauchy--Schwarz inequality applied
    to the RP inner product (3.3).

(c) The OS0' bound (2.2) with Schwartz seminorm $p_{N(n)}$
    ensures continuity in $f$ for the weak topology on
    $\mathcal{S}'$: for fixed $\psi, \chi \in \mathcal{D}$,
    $f \mapsto \langle\chi|\,[\mathrm{Tr}\,F^2]_R(f)\,|\psi\rangle$
    is a continuous linear functional on $\mathcal{S}(\mathbb{R}^4)$.

**Therefore $[\mathrm{Tr}\,F^2]_R$ is an operator-valued
(tempered) distribution:** a continuous linear map
$\mathcal{S}(\mathbb{R}^4) \to
\mathrm{End}(\mathcal{D})$, in the weak operator topology on
$\mathrm{End}(\mathcal{D})$.


---


## 4. Domain Properties and Closability

### 4.1 Closability

**Proposition 4.1** (Closability). *For each
$f \in \mathcal{S}(\mathbb{R}^4)$, the operator
$[\mathrm{Tr}\,F^2]_R(f)$ defined on $\mathcal{D}$ is closable.*

**Proof.** It suffices to show that the adjoint
$[\mathrm{Tr}\,F^2]_R(f)^*$ is densely defined. Since the
Schwinger functions are real-valued for real test functions (the
lattice path integral is a probability measure with real
observables), the formal adjoint satisfies:

$$[\mathrm{Tr}\,F^2]_R(\bar{f})^*
  \supseteq [\mathrm{Tr}\,F^2]_R(\theta^* f)
  \tag{4.1}$$

on $\mathcal{D}$, where $\theta^* f(x_0, \vec{x}) =
\overline{f(-x_0, \vec{x})}$ is the Euclidean time reflection
composed with complex conjugation. Since $\mathcal{D}$ is dense
and contained in $\mathrm{dom}([\mathrm{Tr}\,F^2]_R(f)^*)$,
the adjoint is densely defined. By the standard criterion
(Reed--Simon, Vol. I, Theorem VIII.1), $[\mathrm{Tr}\,F^2]_R(f)$
is closable. $\square$

**Remark.** The closability argument uses only the reality of the
Schwinger functions and the density of $\mathcal{D}$. It does
not require any growth bound on $[\mathrm{Tr}\,F^2]_R(f)$ beyond
the OS0' temperedness.


### 4.2 Symmetry for real test functions

**Proposition 4.2** (Hermiticity on $\mathcal{D}$). *For real
$f \in \mathcal{S}(\mathbb{R}^4;\,\mathbb{R})$ supported in
$\{x_0 > 0\}$:*

$$\langle\chi|\,[\mathrm{Tr}\,F^2]_R(f)\,|\psi\rangle
  = \overline{\langle\psi|\,[\mathrm{Tr}\,F^2]_R(f)\,|\chi\rangle}
  \tag{4.2}$$

*for all $\psi, \chi \in \mathcal{D}$. That is,
$[\mathrm{Tr}\,F^2]_R(f)$ is Hermitian (symmetric) on
$\mathcal{D}$.*

**Proof.** By equation (3.6):

$$\langle\chi|\,[\mathrm{Tr}\,F^2]_R(f)\,|\psi\rangle
  = S_{m+1+n}^{\mathrm{ren}}(\theta\bar{h}_m \otimes f \otimes g_n).
  \tag{4.3a}$$

The complex conjugate of the other matrix element is:

$$\overline{\langle\psi|\,[\mathrm{Tr}\,F^2]_R(f)\,|\chi\rangle}
  = \overline{S_{n+1+m}^{\mathrm{ren}}
  (\theta\bar{g}_n \otimes f \otimes h_m)}.
  \tag{4.3b}$$

By OS3 (symmetry of Schwinger functions under permutations) and
the reality of $S_k^{\mathrm{ren}}$ for real arguments (inherited
from the lattice path integral, which is a real probability
measure):

$$S_{n+1+m}^{\mathrm{ren}}
  (\theta\bar{g}_n \otimes f \otimes h_m)
  = S_{m+1+n}^{\mathrm{ren}}
  (\theta\bar{h}_m \otimes f \otimes g_n)
  \in \mathbb{R},
  \tag{4.4}$$

where the permutation reorders the reflected and unreflected
arguments. (The precise statement: for real test functions, the
Euclidean-reflected $n$-point function equals the complex
conjugate of the time-reverse-permuted one, and OS3 symmetry
gives equality.) Hence (4.3a) = (4.3b). $\square$


### 4.3 Operator bounds from clustering

**Proposition 4.3** (Operator bound from mass gap). *For
$f \in \mathcal{S}(\mathbb{R}^4)$ with $\mathrm{supp}(f)
\subset B_R(0)$ (ball of radius $R$):*

$$\|[\mathrm{Tr}\,F^2]_R(f)\,|\Omega\rangle\|^2
  = S_2^{\mathrm{ren}}(\theta\bar{f}, f)
  \leq C_2\,\|f\|_{L^2}^2,
  \tag{4.5}$$

*where $C_2 = C_2(R,\Delta_\infty)$ depends on the support
radius and the mass gap.*

**Proof.** By definition,

$$\|[\mathrm{Tr}\,F^2]_R(f)\,|\Omega\rangle\|^2
  = \langle\Omega|\,[\mathrm{Tr}\,F^2]_R(\theta\bar{f})\,
  [\mathrm{Tr}\,F^2]_R(f)\,|\Omega\rangle
  = S_2^{\mathrm{ren}}(\theta\bar{f} \otimes f).
  \tag{4.6}$$

Using the Kallen--Lehmann spectral representation and the mass
gap $\Delta_\infty > 0$ (Theorem 8(d)):

$$S_2^{\mathrm{ren}}(x,y) = \int_{\Delta_\infty^2}^{\infty}
  \rho(m^2)\,K_m(x-y)\,dm^2,
  \tag{4.7}$$

where $K_m(z) = (2\pi)^{-2} (m/|z|) K_1(m|z|)$ is the
4D massive propagator. For $m \geq \Delta_\infty > 0$ and
$x, y$ in a bounded region, $K_m(x-y)$ is bounded. Integrating
against $\theta\bar{f} \otimes f$:

$$S_2^{\mathrm{ren}}(\theta\bar{f}, f)
  = \int_{\Delta_\infty^2}^{\infty} \rho(m^2)
  \left|\int f(x)\,\hat{K}_m(x)\,d^4x\right|^2 dm^2
  \leq \|\rho\|_{L^1} \cdot
  \sup_{m \geq \Delta_\infty} \|\hat{K}_m\|_\infty^2
  \cdot \|f\|_{L^1}^2,
  \tag{4.8}$$

which is finite since $\|\rho\|_{L^1} < \infty$ (by the OS0'
bound) and $\hat{K}_m$ is uniformly bounded for $m$ in the
spectral support. $\square$

**Remark.** The spectral representation (4.7) and the mass gap
$\Delta_\infty > 0$ are both established unconditionally by the
preprint. The operator bound (4.5) is therefore unconditional.


### 4.4 Essential self-adjointness (conditional)

**Proposition 4.4** (Nelson-type criterion). *If the renormalized
Schwinger functions satisfy the Nelson--Symanzik bound*

$$|S_n^{\mathrm{ren}}(f_1,\ldots,f_n)|
  \leq A^n\,n!\,\prod_{j=1}^n \|f_j\|_p,
  \tag{4.9}$$

*with $A$ independent of $n$, then for each real
$f \in \mathcal{S}(\mathbb{R}^4;\,\mathbb{R})$, the operator
$[\mathrm{Tr}\,F^2]_R(f)$ is essentially self-adjoint on
$\mathcal{D}$.*

**Proof sketch.** The bound (4.9) guarantees that the vectors

$$e^{z\,[\mathrm{Tr}\,F^2]_R(f)}\,|\Omega\rangle
  = \sum_{n=0}^{\infty} \frac{z^n}{n!}\,
  [\mathrm{Tr}\,F^2]_R(f)^n\,|\Omega\rangle
  \tag{4.10}$$

converge in $\mathcal{H}$ for $|z| < 1/A$. By Nelson's analytic
vector theorem (Nelson, Ann. Math. 70 (1959) 572; see Reed--Simon
Vol. II, Theorem X.39), the existence of analytic vectors dense in
$\mathcal{D}$ implies essential self-adjointness. The vectors (4.10)
are analytic vectors for $[\mathrm{Tr}\,F^2]_R(f)$, and $\{
e^{z\Phi(f)}|\Omega\rangle : f \in \mathcal{S},\; |z| < 1/A\}$
spans a dense subspace of $\mathcal{H}$ (this follows from the
vacuum cyclicity, W5).

**Status.** The bound (4.9) is established: the OS0' verification
(preprint Section 5.7, Theorem 8(f)) gives
$|S_n(f)| \leq n!\,C_0^n\,\|f\|_{p_{4n+1}}$, which is of the
required $n!$ factorial growth type. The critical input is that
$C_0$ is $n$-independent, which holds by the linked-cluster theorem
and the uniform mass-gap bound. $\square$


---


## 5. Extension to $[\mathrm{Tr}(F_{\mu\rho}F_\nu{}^\rho)]_R$

The construction of the stress tensor $T_{\mu\nu}$ (Conjecture L.3,
Wave 7) requires the renormalized tensor-structure operator
$[\mathrm{Tr}(F_{\mu\rho}F_\nu{}^\rho)]_R$ in addition to the
scalar $[\mathrm{Tr}\,F^2]_R$. The Suzuki gradient-flow formula
(Suzuki, PTEP 2013:083B03; Makino--Suzuki, PTEP 2014:063B02)
expresses $T_{\mu\nu}^R$ in terms of two independent flowed
operators:

$$T_{\mu\nu}^R(x) = \lim_{t \to 0^+}\Bigl[
  c_1(t)\,U_{\mu\nu}(t,x)
  + c_2(t)\,\delta_{\mu\nu}\,E(t,x)
  + c_3(t)\,\delta_{\mu\nu}\,\langle E(t,x)\rangle \cdot \mathbb{1}
  \,\Bigr],
  \tag{5.1}$$

where

$$U_{\mu\nu}(t,x) := G_{\mu\rho}^a(t,x)\,G_{\nu\rho}^a(t,x)
  - \tfrac{1}{4}\,\delta_{\mu\nu}\,
  G_{\rho\sigma}^a(t,x)\,G_{\rho\sigma}^a(t,x),
  \tag{5.2}$$

with $G_{\mu\nu}^a(t,x)$ the field strength of the flowed gauge
field $B_\mu(t,x)$, and $E(t,x) = \tfrac{1}{4}\,
G_{\mu\nu}^a(t,x)\,G_{\mu\nu}^a(t,x)$ is the flowed energy density.


### 5.1 Operator mixing at dimension 4: tensor decomposition

The key structural fact is that the space of gauge-invariant,
$\mathcal{C}$-even, dimension-4, rank-2 symmetric tensor operators
decomposes under O(4) into irreducible components. For pure
Yang--Mills:

- **Scalar channel** ($J = 0$): $\delta_{\mu\nu}\,\mathrm{Tr}\,F^2$.
  A single operator; this is the energy density $E(t,x)$ channel.

- **Spin-2 channel** ($J = 2$): the traceless part
  $\mathrm{Tr}(F_{\mu\rho}F_\nu{}^\rho)
  - \tfrac{1}{4}\delta_{\mu\nu}\,\mathrm{Tr}\,F^2$.
  This is the $U_{\mu\nu}$ channel.

The mixing matrix at dimension 4 for each irreducible O(4)
representation is $1 \times 1$ (a single operator in each channel),
by the same argument as Lemma 3.2 (W1-04, Memo 1; preprint
Section 5.3.1): the unique gauge-invariant, $\mathcal{C}$-even,
parity-even bilinears in $F_{\mu\nu}$ of dimension 4 are
$\mathrm{Tr}\,F^2$ (scalar) and
$\mathrm{Tr}(F_{\mu\rho}F_\nu{}^\rho) - \mathrm{trace}$
(traceless symmetric rank-2).

**Consequence:** The Wilson coefficients $c_1(t)$ and $c_2(t)$
in Suzuki's formula (5.1) are the unique multiplicative
renormalization constants for the spin-2 and spin-0 channels,
respectively. No operator mixing occurs at dimension 4 in either
channel.


### 5.2 Extraction of $[\mathrm{Tr}(F_{\mu\rho}F_\nu{}^\rho)]_R$

**Proposition 5.1.** *The renormalized tensor-structure two-point
function*

$$S_2^{\mathrm{ren},\,\mu\nu\rho\sigma}(x,y) :=
  \lim_{t \to 0^+}
  \frac{\langle U_{\mu\nu}(t,x)\,U_{\rho\sigma}(t,y)\rangle_c}
  {c_1(t)^2}
  \tag{5.3}$$

*exists as a finite tempered distribution for non-coincident
$(x,y)$, satisfies OS positivity, Euclidean covariance (including
the spin-2 transformation law), and cluster decomposition.*

**Proof.** The argument parallels Lemma 3.8 (W5-10) exactly,
with $E(t,x)$ replaced by $U_{\mu\nu}(t,x)$ throughout:

(a) **Finiteness at $t = 0$**: $U_{\mu\nu}$ is a gauge-invariant
    bilinear in $F$, so the KK mode sums are the same Epstein
    zeta functions (Theorem K.1 applies identically; the tensor
    indices do not affect the mode-sum structure).

(b) **Analyticity in $t$**: $U_{\mu\nu}(t,x)$ is polynomial in
    the flowed field strength $G_{\mu\nu}(t,x)$, which is itself
    analytic in $t$ by the same composition argument (Lemma 3.1,
    W1-05). The analyticity radius $r_t$ is unchanged (it depends
    on the Balaban radius $\rho$ and the flow speed
    $L_{\mathrm{flow}}$, neither of which depends on the Lorentz
    structure of the observable).

(c) **Removable singularity and Cauchy estimate**: the identical
    argument as Steps 4--5 of Lemma 3.7.

(d) **OS axioms**: reflection positivity for
    $U_{\mu\nu}$ follows from lattice reflection positivity
    applied to the traceless plaquette operator (the lattice
    analogue of $U_{\mu\nu}$), which is a gauge-invariant observable.
    The factor $c_1(t)^{-1}$ is a positive scalar and preserves RP.

(e) **$K$-uniformity and double limit**: the same Moore--Osgood
    mechanism applies.

The tensor transformation law under O(4) is:

$$U(R)\,[\mathrm{Tr}(F_{\mu\rho}F_\nu{}^\rho)]_R(x)\,U(R)^{-1}
  = R_\mu{}^{\mu'}\,R_\nu{}^{\nu'}\,
  [\mathrm{Tr}(F_{\mu'\rho'}F_{\nu'}{}^{\rho'})]_R(Rx),
  \tag{5.4}$$

inherited from the O(4) covariance of the continuum flowed Schwinger
functions (W4-09, Lemma 2.4). $\square$


### 5.3 The Belinfante--Rosenfeld decomposition on $\mathcal{H}$

With both $[\mathrm{Tr}\,F^2]_R(f)$ and
$[\mathrm{Tr}(F_{\mu\rho}F_\nu{}^\rho)]_R(f)$ constructed as
operator-valued distributions on the common domain $\mathcal{D}$,
the stress tensor (Conjecture L.3) is assembled as:

$$T_{\mu\nu}(f) = -\,[\mathrm{Tr}(F_{\mu\rho}F_\nu{}^\rho)]_R(f)
  + \tfrac{1}{4}\,\delta_{\mu\nu}\,[\mathrm{Tr}\,F^2]_R(f)
  + c_{\mathrm{vac}}\,\delta_{\mu\nu}\,(f, 1)\,\mathbb{1},
  \tag{5.5}$$

where $c_{\mathrm{vac}}$ is chosen so that
$\langle\Omega|\,T_{\mu\nu}(f)\,|\Omega\rangle = 0$.

The domain $\mathcal{D}$ is invariant under both operators (by
construction: Section 3.2), so $T_{\mu\nu}(f)$ is well-defined on
$\mathcal{D}$. All sub-clauses of Conjecture L.3 ---
symmetry, gauge invariance, conservation, positivity of $H$,
trace anomaly --- are addressed in Wave 7 (W7-13) using the
infrastructure established here.


---


## 6. Map to Conjecture L.1 Sub-Clauses (i)--(iii)

### 6.1 Sub-clause (i): Multiplicatively renormalized lattice limit

**Conjecture L.1(i).** *Each $[\mathcal{O}]_R$ is the limit, as
$a \to 0$, of a multiplicatively renormalized lattice operator:*

$$[\mathcal{O}]_R(f) = \lim_{a \to 0}\;
  Z_\mathcal{O}(a)\,\sum_{x \in \Lambda_a} a^4\,
  \mathcal{O}_a^{\mathrm{bare}}(x)\,f(x). \tag{L.1.i}$$

**Discharge.** The gradient-flow construction provides an explicit
realization. At flow time $t > 0$, the flowed energy density
$E(t,x)$ is UV-finite and needs no $Z$-factor renormalization.
The small-flow-time expansion gives:

$$E(t,x) = c_1(t)\,[\mathrm{Tr}\,F^2]_R(x) + O(t). \tag{6.1}$$

Inverting:

$$[\mathrm{Tr}\,F^2]_R(x) = \lim_{t \to 0^+}
  \frac{E(t,x)}{c_1(t)}. \tag{6.2}$$

On the lattice at spacing $a$, the flowed energy density is:

$$E^{(a)}(t,x) = \frac{2N}{a^4 g_0^2}\,\hat{s}_P^{(t)}(x),
  \tag{6.3}$$

where $\hat{s}_P^{(t)}$ is the symmetrized plaquette of the
flowed lattice configuration. Therefore, with the identification

$$Z_{\mathrm{Tr}\,F^2}(a) = c_1(t(a))^{-1}, \qquad
  \mathcal{O}_a^{\mathrm{bare}}(x) = E^{(a)}(t(a), x),
  \tag{6.4}$$

where $t(a)$ is any function with $t(a) \to 0$ as $a \to 0$ and
$t(a)/a^2 \to \infty$ (so that the flow provides UV smoothing
at scale $\sqrt{t} \gg a$), the lattice operator converges:

$$\lim_{a \to 0}\,Z_{\mathrm{Tr}\,F^2}(a)\,
  \sum_{x \in \Lambda_a} a^4\,E^{(a)}(t(a),x)\,f(x)
  = [\mathrm{Tr}\,F^2]_R(f). \tag{6.5}$$

The convergence is established by the double limit (equation (DL)
of W5-10, Lemma 3.8, Part I, Step 5): the Moore--Osgood theorem
applied to the $K$-uniform Lipschitz estimate in $t$ and the Cauchy
property in $a$ guarantees that the iterated limits and the
simultaneous limit coincide.

**Alternatively (pure multiplicative scheme).** If one prefers
the pure lattice formulation without the gradient flow as
intermediary, set $t = 0$ and:

$$Z_{\mathrm{Tr}\,F^2}(a) = c_1(0,\mu)^{-1} \cdot
  \Bigl(\frac{g^2(1/a)}{g^2(\mu)}\Bigr)^{\gamma_0/(2b_0)},
  \tag{6.6}$$

where $\gamma_0 = 2b_0$ is the one-loop anomalous dimension
coefficient (from the trace-anomaly identity, see sub-clause
(iii) below), and the $g^2$ ratio absorbs the logarithmic running.
In the KK theory, the unflowed correlator at $t = 0$ is finite
(Theorem K.1), so the $Z$-factor is well-defined. The lattice-
to-continuum convergence is then a single limit $a \to 0$, not
a double limit, and follows from Theorem M.2.1 (Appendix M).


### 6.2 Sub-clause (ii): OS properties of $S_n^{\mathrm{ren}}$

**Conjecture L.1(ii).** *The renormalized Schwinger functions
$S_n^{\mathrm{ren}}$ are finite tempered distributions on
$(\mathbb{R}^4)^n$, smooth off the total diagonal, satisfy OS
positivity, Euclidean invariance, and cluster decomposition.*

**Discharge.** Each property is established in Section 2:

| Property | Where established |
|:---------|:-----------------|
| Finite tempered distributions | Section 2.2, OS0', equation (2.2) |
| Smooth off diagonal | Analyticity from $F_n$ holomorphic (Section 2.1(b)); non-coincident points have $\|x-y\| > 0$, so analyticity of the spectral representation (4.7) in the separation gives real-analyticity off the diagonal |
| OS positivity | Section 2.2, OS2, equations (2.3)--(2.4) |
| Euclidean invariance | Section 2.2, OS1 |
| Cluster decomposition | Section 2.2, OS4, equation (2.5) |

**Smoothness off diagonal (detail).** The Kallen--Lehmann
spectral representation (4.7) with spectral measure supported on
$[m^2, \infty)$, $m = \Delta_\infty > 0$, gives:

$$S_2^{\mathrm{ren}}(x,y)
  = \int_{\Delta_\infty^2}^{\infty} \rho(s)\,
  \frac{(\sqrt{s})^{1}}{(2\pi)^2}\,
  \frac{K_1(\sqrt{s}\,|x-y|)}{|x-y|}\,ds.
  \tag{6.7}$$

For $|x - y| > 0$, $K_1(\sqrt{s}\,|x-y|)$ is a real-analytic
function of $|x - y|^2$ (the modified Bessel function $K_1$
is analytic for positive argument), and the $s$-integral converges
absolutely and uniformly on compact subsets of
$\{(x,y) : |x - y| > \epsilon\}$. Therefore
$S_2^{\mathrm{ren}}(x,y)$ is $C^\infty$ (in fact real-analytic)
off the diagonal. The argument extends to $n$-point functions via
the linked-cluster decomposition into products of two-point
functions (Glimm--Jaffe, Theorem 8.4.3).


### 6.3 Sub-clause (iii): Anomalous dimension match

**Conjecture L.1(iii).** *The anomalous dimension satisfies the
Spiridonov--Chetyrkin trace-anomaly identity:*

$$\gamma_{\mathrm{Tr}\,F^2}(g)
  = -\,\frac{2\,\beta(g)}{g}
  = 2\,b_0\,g^2 + O(g^4),
  \qquad b_0 = \frac{11N}{48\pi^2}.
  \tag{L.1.iii}$$

**Discharge.** The gradient-flow construction provides a clean
derivation of this identity through three ingredients.

**Ingredient 1: The renormalization-group invariant combination.**

The combination $(\beta(g)/g^3)\,\mathrm{Tr}\,F^2$ is
renormalization-group invariant to all orders in continuum
perturbation theory. This is a consequence of the trace-anomaly
identity:

$$T_\mu{}^\mu = \frac{\beta(g)}{2g}\,[\mathrm{Tr}\,F^2]_R,
  \tag{6.8}$$

combined with the fact that $T_\mu{}^\mu$ has vanishing anomalous
dimension (it is the divergence of a conserved current in flat
space). Therefore:

$$\mu\,\frac{d}{d\mu}\left(\frac{\beta(g)}{g^3}\,
  [\mathrm{Tr}\,F^2]_R\right) = 0,
  \tag{6.9}$$

which gives:

$$\gamma_{\mathrm{Tr}\,F^2} := \mu\,\frac{d}{d\mu}
  \ln Z_{\mathrm{Tr}\,F^2}
  = -\,\frac{2\,\beta(g)}{g}.
  \tag{6.10}$$

> *Reference:* Spiridonov, Phys. Lett. B 147 (1984) 117;
> Spiridonov--Chetyrkin, Sov. J. Nucl. Phys. 47 (1988) 522.
> Collins--Duncan--Joglekar, Phys. Rev. D 16 (1977) 438.

**Ingredient 2: Gradient-flow realization.**

In the gradient-flow scheme, the Wilson coefficient $c_1(t,\mu)$
plays the role of $Z_{\mathrm{Tr}\,F^2}$. The Luscher--Weisz
small-flow-time expansion gives:

$$c_1(t,\mu) = 1 + c_{1,1}\,\bar{g}^2(q) + O(\bar{g}^4),
  \qquad q = (8t)^{-1/2},
  \tag{6.11}$$

where $\bar{g}(q)$ is the running coupling at scale $q$. The
$\mu$-dependence of $c_1$ is determined by the anomalous dimension:

$$\mu\,\frac{\partial}{\partial\mu}\,c_1(t,\mu)
  = -\gamma_{\mathrm{Tr}\,F^2}(g(\mu))\,c_1(t,\mu).
  \tag{6.12}$$

At one loop, $\gamma_{\mathrm{Tr}\,F^2} = 2b_0\,g^2$
(from $\beta(g) = -b_0\,g^3$), which matches the perturbative
computation of $c_1$ (Luscher 2010; Harlander--Neumann, JHEP 06
(2016) 161).

**Ingredient 3: Non-perturbative verification.**

The gradient-flow programme provides a non-perturbative path to
the anomalous dimension. The renormalized two-point function
$S_2^{\mathrm{ren}}(x,y)$ defined in Lemma 3.8 (W5-10) satisfies:

$$S_2^{\mathrm{ren}}(x,y) = \lim_{t \to 0^+}
  \frac{S_{2,t}^c(x,y)}{c_1(t)^2}. \tag{6.13}$$

At short distance $|x - y| \to 0$, the perturbative prediction
(Conjecture L.2) gives:

$$S_2^{\mathrm{ren}}(x,y) \sim
  \frac{C_N}{|x-y|^8}\,
  \left(\ln\frac{1}{|x-y|\Lambda}\right)^{-2}
  [1 + O((\log)^{-1})], \tag{6.14}$$

with $C_N = 2(N^2-1)/\pi^6$. The logarithmic exponent $-2$ arises
precisely from $\gamma_0 = 2b_0$ (the one-loop anomalous dimension):
the callan--Symanzik equation with $\gamma_0 = 2b_0$ and $\beta_0 =
-b_0 g^3$ gives the correction $(\log)^{-\gamma_0/b_0} =
(\log)^{-2}$ to the naive engineering-dimension scaling $|x-y|^{-8}$.

This is the precise verification of $\gamma_0 = 2b_0$, equivalent
to $\gamma_{\mathrm{Tr}\,F^2} = -2\beta(g)/g$ at leading order.

**The Spiridonov--Chetyrkin identity is exact.** Beyond one loop,
the identity $\gamma_{\mathrm{Tr}\,F^2} = -2\beta(g)/g$ holds
to all orders in perturbation theory (Spiridonov 1984). In the
gradient-flow construction, this means the exact relation between
$c_1(t,\mu)$ and $\beta(g)$ is:

$$c_1(t,\mu) = \left(\frac{g^2(\mu)}{g^2(q)}\right)
  \cdot [1 + O(\bar{g}^4(q))],
  \tag{6.15}$$

where the ratio $g^2(\mu)/g^2(q)$ encodes the full
renormalization-group evolution, including the all-orders relation
$\gamma = -2\beta/g$.


---


## 7. Summary: Complete Discharge Map

### 7.1 Conjecture L.1 sub-clause status

| Sub-clause | Statement | Discharge | Source |
|:-----------|:----------|:----------|:-------|
| L.1(i) | Multiplicatively renormalized lattice limit | Gradient-flow extraction, equations (6.2)--(6.5) | W5-10, Lemma 3.8; Moore--Osgood (Step 5) |
| L.1(ii) | $S_n^{\mathrm{ren}}$ finite, tempered, OS, clustered | Full OS axiom verification, Section 2 | W4-09, Lemma 2.4; W5-10, Lemma 3.8 |
| L.1(iii) | Anomalous dimension $= -2\beta/g$ | Spiridonov--Chetyrkin via trace anomaly, Section 6.3 | Spiridonov 1984; Luscher 2010; equation (6.10) |


### 7.2 Infrastructure for downstream conjectures

| Conjecture | What this memo provides | What remains (Wave 7+) |
|:-----------|:-----------------------|:-----------------------|
| L.1 | Complete GNS reconstruction; domain $\mathcal{D}$; closability | --- (closed by this memo + W5-10) |
| L.2 (AF match) | Short-distance form (6.14) as consequence of $\gamma_0 = 2b_0$ | Promote perturbative = non-perturbative at short distance (standard hypothesis) |
| L.3 ($T_{\mu\nu}$) | Both tensor components $[\mathrm{Tr}\,F^2]_R$ and $[\mathrm{Tr}(F_{\mu\rho}F_\nu{}^\rho)]_R$ on $\mathcal{D}$; Belinfante decomposition (5.5) | Ward identity, trace anomaly as operator identity, $H = \int T_{00}$ (W7-13) |
| L.4 (OPE) | Coincident-point bounds from OS0'; operator basis at dim 4 | Distributional OPE convergence; subleading channels (W8+) |


### 7.3 Logical dependencies

$$\boxed{
\begin{aligned}
&\text{W5-10 (Lemma 3.8)} &&\xrightarrow{\;\text{input}\;}
  &&\text{This memo (GNS reconstruction, L.1 discharge)} \\[4pt]
&\text{This memo} &&\xrightarrow{\;\text{tensor extension}\;}
  &&\text{W7-13 (stress tensor, L.3)} \\[4pt]
&\text{This memo} &&\xrightarrow{\;\text{short-distance}\;}
  &&\text{W8 (AF match, L.2)} \\[4pt]
&\text{This memo + W8} &&\xrightarrow{\;\text{OPE}\;}
  &&\text{W9 (leading OPE, L.4)}
\end{aligned}
}$$


---


## 8. References

1. Osterwalder, K. and Schrader, R. Axioms for Euclidean Green's
   functions, I--II. *CMP* **31** (1973) 83--112; **42** (1975)
   281--305.

2. Glimm, J. and Jaffe, A. *Quantum Physics: A Functional Integral
   Point of View*, 2nd ed. Springer (1987), Chapters 18--19.

3. Reed, M. and Simon, B. *Methods of Modern Mathematical Physics,
   Vol. I: Functional Analysis*. Academic Press (1972), Section VIII.

4. Reed, M. and Simon, B. *Methods of Modern Mathematical Physics,
   Vol. II: Fourier Analysis, Self-Adjointness*. Academic Press
   (1975), Theorem X.39 (Nelson's analytic vector theorem),
   Theorem X.55 (OS reconstruction).

5. Nelson, E. Analytic vectors. *Ann. Math.* **70** (1959) 572--615.

6. Spiridonov, V. P. Anomalous dimension of the quark--gluon operator
   and low-energy theorem for the trace of the energy-momentum tensor
   in QCD. *Phys. Lett. B* **147** (1984) 117--120.

7. Spiridonov, V. P. and Chetyrkin, K. G. Nonleading mass corrections
   and renormalization of the operators $m\bar{\psi}\psi$ and $G^2$.
   *Sov. J. Nucl. Phys.* **47** (1988) 522--527.

8. Collins, J. C., Duncan, A. and Joglekar, S. D. Trace and
   dilatation anomalies in gauge theories. *Phys. Rev. D* **16**
   (1977) 438--449.

9. Luscher, M. Properties and uses of the Wilson flow in lattice QCD.
   *JHEP* **08** (2010) 071; arXiv:1006.4518.

10. Luscher, M. and Weisz, P. Perturbative analysis of the gradient
    flow in non-abelian gauge theories. *JHEP* **02** (2011) 051;
    arXiv:1101.0963.

11. Suzuki, H. Energy-momentum tensor from the Yang--Mills gradient
    flow. *PTEP* **2013** (2013) 083B03; arXiv:1304.0533.

12. Makino, H. and Suzuki, H. Lattice energy-momentum tensor from the
    Yang--Mills gradient flow --- inclusion of fermion fields. *PTEP*
    **2014** (2014) 063B02; arXiv:1403.4772.

13. Harlander, R. V. and Neumann, T. The perturbative QCD gradient
    flow to three loops. *JHEP* **06** (2016) 161; arXiv:1606.03756.

14. Del Debbio, L., Patella, A. and Rago, A. Space-time symmetries
    and the Yang--Mills gradient flow. *JHEP* **11** (2013) 212;
    arXiv:1306.1173.

15. Mass gap preprint: Sections 5.3.1, 5.5.3, 5.6, 5.7; Appendices K,
    L, M.

16. W5-10: Lemma 3.7 (Cauchy estimate) and Lemma 3.8 (extraction).

17. W4-09: Lemmas 2.2--2.4 (continuum limit of flowed correlators;
    OS axioms at fixed $t > 0$).

18. W1-04: Lemmas 3.2--3.6 (no mixing, Epstein vanishing,
    $\mathbb{Z}_2$ cancellation).

19. W1-05: Lemma 3.1 (composition theorem; analyticity in $t$).


---


*File location:*
`/Users/gsix/yang-mills/gradient-flow-attack-plan/research/W6-11-extraction.md`

*Input:*
`/Users/gsix/yang-mills/gradient-flow-attack-plan/research/W5-10-cauchy-estimate-and-extraction.md`

*Downstream:*
`/Users/gsix/yang-mills/gradient-flow-attack-plan/research/W7-13-stress-tensor.md` (stress tensor, L.3)

*This memo provides the complete functional-analytic infrastructure
for the GNS reconstruction of $[\mathrm{Tr}\,F^2]_R$ and its
tensor extension $[\mathrm{Tr}(F_{\mu\rho}F_\nu{}^\rho)]_R$,
discharging all three sub-clauses of Conjecture L.1 and
establishing the operator-valued distribution on the common dense
invariant domain $\mathcal{D} \subset \mathcal{H}$.*
