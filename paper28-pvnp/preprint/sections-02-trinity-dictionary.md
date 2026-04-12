# Section 2: The Trinity Dictionary

*Paper 28 — P versus NP as the Computational Shadow of the*
*Spin–Statistics Theorem*

---

# 2. The Trinity Dictionary

## 2.1 The additive ↔ multiplicative dictionary, recap

Paper 15 §2.1 introduced the *additive ↔ multiplicative dictionary*,
the systematic translation between the language of physics
(continuous, additive, four-dimensional, smooth) and the language
of the Bost–Connes algebra (discrete, multiplicative, arithmetic,
non-commutative). The dictionary is the operational core of the
long-arc transposition programme: every R-Theorem of Paper 15 is
a row in this two-column table, and the methodology of producing
new R-Theorems is the methodology of filling in additional rows.

We recall the dictionary in compact form. Each row pairs a
physical concept (left column) with its image under the Mellin
transform and the BC operator-algebraic reformulation (right
column).

| # | Additive (physics) | Multiplicative (BC) |
|---:|:--|:--|
| **A1** | Position $x \in \mathbb R^n$ | Prime $p \in \mathbb N^*$ |
| **A2** | Translation $T_a : x \mapsto x + a$ | Dilation $\mu_n : \theta \mapsto n\theta$ |
| **A3** | Momentum $p$ (generator of translations) | $\log\hat N$ (generator of dilations: $H_{\rm BC} = \log\hat N$) |
| **A4** | Fourier transform $\hat f(p) = \int e^{-ipx} f(x)\,dx$ | Mellin transform $\widetilde f(s) = \int_0^\infty f(t)\,t^{s-1}\,dt$ |
| **A5** | Heisenberg commutator $[\hat x, \hat p] = i\hbar$ | Hecke relation $\mu_n e(r) \mu_n^* = \frac1n\sum_{ns=r} e(s)$ |
| **A6** | Compact $S^1_R$ time circle | Multiplicative semigroup $\mathbb N^\times$ |
| **A7** | Hamiltonian $H$ (generator of time evolution) | Modular Hamiltonian $K = -\log\Delta_{\omega_1}$ |
| **A8** | Time evolution $U_t = e^{-iHt}$ | Modular flow $\sigma_t = \Delta_{\omega_1}^{it}$ |
| **A9** | KMS condition at temperature $\beta$ | KMS$_\beta$ state on $(\mathcal A_{\rm BC}, \sigma_t)$ |
| **A10** | Casimir energy of bulk fields on $S^1_R$ | BC free energy $-\log Z(\beta) = -\log\zeta(\beta)$ |
| **A11** | Bosonic field (commuting at spacelike separation) | Diagonal in the $\{\mu_n\Omega_1\}$ basis (commuting in the abelian subalgebra) |
| **A12** | Fermionic field (anticommuting, projective $S_n$ rep) | Off-diagonal in $\{\mu_n\Omega_1\}$ (graded sector of the $\mathbb Z/2$-graded $M$) |
| **A13** | Spin–statistics theorem | R-Theorem S.11 (graded modular structure forced by graded functional equations) |
| **A14** | Aharonov–Bohm phase | Frobenius element acting on cyclotomic phase |
| **A15** | Wess–Zumino consistency | R-Theorem C.1 (Hecke-character cocycle satisfies WZ analogue) |
| **A16** | Atiyah–Singer index theorem | R-Theorem D.1 (BC index theorem; integer constraint forcing $\gamma_n \in \mathbb R$) |
| **A17** | Hilbert space (separable, complex) | GNS Hilbert space $H_1 = L^2(\mathcal A_{\rm BC}, \omega_1)$ |
| **A18** | Spectral theorem (self-adjoint operators ↔ projection-valued measures) | Spectral theorem on type III$_1$ factor (no normal trace, but spectral measures exist) |

The dictionary has been verified through 37 R-Theorems (Paper 15
Round 4–5 supplement); we list eighteen here as the rows that bear
on the present construction. The full table is reproduced in
Appendix A.

The crucial structural feature of the dictionary is *functoriality*:
if a physical theorem $T$ admits a multiplicative image $T_m$, and
$T$ is a consequence of more elementary physical statements $T_1,
\ldots, T_k$ that themselves admit images $T_{1,m}, \ldots, T_{k,m}$,
then $T_m$ is provable from $T_{1,m}, \ldots, T_{k,m}$ in the BC
language using the multiplicative analogue of the proof of $T$
from $T_1, \ldots, T_k$. The dictionary preserves logical
implication. This is what makes it a *functor* between
$\mathsf{Cat}_{\rm phys}$ and $\mathsf{Cat}_{\rm BC}$, in a sense
made precise in Section 2.4.

The functoriality is what allows the present paper to do its work
without re-proving R-Theorem S.11. We take the proof of S.11 as
given by Paper 15 in the multiplicative column, apply the trinity
functor of Section 2.4, and obtain the proof of R-Theorem PNP.1
in the computational column for free. Or rather: not for free, but
mechanically.

---

## 2.2 The third column: computational

The two columns of the additive ↔ multiplicative dictionary
encode physics and arithmetic respectively. We now add a third
column encoding *computation*. The motivation is the central
insight of the present paper: that *computational hardness*, like
fermionic statistics and like graded BC modular structure, is the
shadow of a single cohomological volume.

The third column requires a base object analogous to $\mathbb R^n$
in the additive column and to $\mathbb N^\times$ acting on
$\mathbb Q/\mathbb Z$ in the multiplicative column. The natural
choice is the **Boolean function field** $\mathbb B$ — the
inductive limit of polynomial rings $\mathbb F_2[x_1, \ldots,
x_n]$ as $n \to \infty$, with the natural action of the symmetric
group $S_\infty$ permuting variables and $(\mathbb Z/2)^\infty$
acting by negation on each variable.

The construction of $\mathbb B$, and the construction of the
Boolean BC algebra $\mathcal A_{\rm BC}^{\rm Bool}$ as a semigroup
crossed product over $\mathbb B$, are deferred to Section 3. For
the purposes of the present section, we treat $\mathbb B$ as a
black box and describe the trinity dictionary in terms of its
structural features.

The key features of the computational column are:

- **Base set**: bit strings $b \in \{0,1\}^n$ (the discrete
  analogue of position $x \in \mathbb R^n$ and prime $p \in
  \mathbb N^*$).
- **Translation analogue**: permutation $\sigma \in S_n$ acting
  on bit strings (the discrete analogue of $x \mapsto x + a$ and
  $\theta \mapsto n\theta$).
- **Hamiltonian analogue**: circuit-depth functional $D : C
  \mapsto \mathrm{depth}(C)$ on Boolean circuits, generating a
  modular flow $\sigma_t^{\rm Bool}$ via $\sigma_t^{\rm Bool}(\mu_C)
  = (\mathrm{depth}\,C)^{it}\mu_C$.
- **Fourier analogue**: Walsh–Hadamard transform $\widehat f(c) =
  \frac{1}{\sqrt{2^n}}\sum_{b \in \{0,1\}^n}(-1)^{b \cdot c}f(b)$,
  the unique unitary on $\ell^2(\{0,1\}^n)$ that diagonalises the
  $(\mathbb Z/2)^n$ negation action.
- **Heisenberg analogue**: Boolean derivative $D_i f(b) := f(b
  \oplus e_i) \oplus f(b)$, where $e_i$ is the $i$-th basis vector
  and $\oplus$ is XOR, satisfying $[D_i, D_j] = 0$ but $\{D_i,
  M_i\} = 1$ where $M_i$ is the multiplication-by-$x_i$ operator.
- **Bosonic / fermionic analogue**: P-time computation (single
  matrix element of the modular flow, diagonal in the
  circuit-depth basis) versus NP verification (off-diagonal,
  requiring a witness branch and therefore a graded sector).

The Walsh–Hadamard transform deserves special note. In the
additive column, the Fourier transform on $\mathbb R^n$ is the
unique unitary intertwining position and momentum. In the
multiplicative column, the Mellin transform on $\mathbb N^\times$
is the unique unitary intertwining the dilation generator and the
spectrum of $\hat N$. In the computational column, the Walsh–
Hadamard transform on $\{0,1\}^n$ is the unique unitary
intertwining the bit-flip generators and the Walsh frequencies.
All three are special cases of the *Pontryagin duality functor*
applied to the appropriate locally compact abelian group:
$\mathbb R^n$ for additive, $\mathbb N^\times$ for multiplicative,
$(\mathbb Z/2)^n$ for computational. The trinity dictionary is,
in this sense, a Pontryagin trinity: three groups, three duality
functors, three columns of one larger structure.

---

## 2.3 The full trinity table

We now lay out the trinity dictionary in the same row-by-row form
as the additive ↔ multiplicative table of Section 2.1. Each row
specifies the additive (physics), multiplicative (BC), and
computational (Boolean) entries; the cohomological invariant
preserved across the row; and a brief justification for the
identification.

| # | Additive (physics) | Multiplicative (BC) | Computational (Boolean) | $H^k$ preserved |
|---:|:--|:--|:--|:--|
| **T1** | Position $x \in \mathbb R^n$ | Prime $p \in \mathbb N^*$ | Bit string $b \in \{0,1\}^n$ | base set |
| **T2** | Translation $T_a$ | Dilation $\mu_n$ | Permutation $\sigma \in S_n$ | $H^0$ (action) |
| **T3** | Momentum $\hat p$ | Number operator $\log\hat N$ | Circuit depth $\hat D$ | $H^0$ (generator) |
| **T4** | Fourier $e^{-ipx}$ | Mellin $n^{-s}$ | Walsh–Hadamard $(-1)^{b\cdot c}$ | Pontryagin duality |
| **T5** | Heisenberg $[\hat x,\hat p]=i\hbar$ | Hecke $\mu_n e(r) \mu_n^*$ | Boolean derivative $D_i$ | $H^1$ (commutator) |
| **T6** | Compact $S^1_R$ | $\mathbb N^\times$ | $S_\infty$ acting on $\mathbb B$ | $H^0$ (symmetry) |
| **T7** | Hamiltonian $H$ | Modular Hamiltonian $K = -\log\Delta_{\omega_1}$ | Circuit-depth functional $D$ | $H^0$ (generator) |
| **T8** | Time evolution $U_t = e^{-iHt}$ | Modular flow $\sigma_t = \Delta_{\omega_1}^{it}$ | Boolean modular flow $\sigma_t^{\rm Bool}$ | $H^0$ (one-parameter group) |
| **T9** | Bosonic field | Diagonal in $\{\mu_n\Omega_1\}$ | P-time circuit (diagonal in circuit-depth basis) | $H^2 = 0$ (trivial cocycle) |
| **T10** | Fermionic field | Off-diagonal $[\mu_p,\mu_q]$ in graded sector | NP verifier (off-diagonal, witness branch) | $H^2 = \mathbb Z/2$ (non-trivial cocycle) |
| **T11** | Spin–statistics theorem | R-Theorem S.11 | **R-Theorem PNP.1** | $H^2(S_n, U(1))$ |
| **T12** | Aharonov–Bohm phase | Frobenius on cyclotomic phase | Walsh phase $(-1)^{b \cdot c}$ at fixed $c$ | $H^1$ (winding) |
| **T13** | Atiyah–Singer index theorem | R-Theorem D.1 (BC index) | Boolean index theorem (integer-valued circuit complexity) | $H^*$ (index) |
| **T14** | Spectral theorem | $T_{\rm BC}$ self-adjoint via Tomita | $\hat D$ self-adjoint with discrete depth spectrum | $H^0$ (spectral measures) |
| **T15** | Casimir energy on $S^1_R$ | $-\log\zeta(\beta)$ free energy | Average circuit depth at uniform measure | $H^0$ (free energy) |
| **T16** | Wess–Zumino consistency | R-Theorem C.1 | Boolean cocycle consistency (gates compose to circuits) | $H^1$ (cocycle) |
| **T17** | Anomaly cancellation | R-Theorem C.2 (19 = 1+4+6+8) | Circuit composition closure | $H^2$ (anomaly) |
| **T18** | Yang–Mills mass gap | R-Theorem L.0 ($\gamma_1$ as smallest BC mass gap) | P-time complexity gap (smallest super-polynomial circuit) | $H^0$ (spectral gap) |

The most important rows for the present paper are **T9, T10, and
T11** — the rows that contain the bosonic / fermionic distinction
and its computational image. We expand them in detail.

### Row T9: bosonic ↔ diagonal ↔ P-time

In the additive column, a bosonic field is one whose creation and
annihilation operators commute at spacelike separation:
$$[\phi(x), \phi(y)] = 0 \quad \text{when } (x-y)^2 < 0.$$
This commutativity is the operator-algebraic statement of the
property that bosonic statistics are *symmetric*: a permutation of
two bosonic excitations leaves the wavefunction unchanged.

In the multiplicative column, the bosonic image is the **abelian
subalgebra** of $M = \pi_1(\mathcal A_{\rm BC})''$ generated by
the diagonal elements in the basis $\{\mu_n\Omega_1\}$. This
subalgebra is $\sigma_t$-invariant and consists of operators whose
action on $\Omega_1$ is multiplication by a number. The Hecke
generators $\mu_n$, taken individually, lie in this subalgebra
(since $\mu_n e(0) \mu_n^* = e(0) = 1$). The cocycle they carry
is *trivial*, an element of $H^2(\mathbb Z/k\mathbb Z, U(1)) = 0$
for $k = 0$ (the trivial group case).

In the computational column, the image is the **P-time circuit
class**: Boolean functions computed by polynomial-size circuits
of polynomial depth, executed deterministically. Such circuits
act on bit strings by a sequence of local operations, each of
which is *diagonal in the circuit-depth basis* — the operation
at depth $d$ depends only on the bits computed at depths $< d$,
not on any "witness" supplied externally. The closure of the
P-time circuit class under composition makes it an algebra, and
the $\sigma_t^{\rm Bool}$-invariance of the diagonal sector makes
it a $\sigma_t^{\rm Bool}$-invariant subalgebra of $M_{\rm Bool}
= \pi_1^{\rm Bool}(\mathcal A_{\rm BC}^{\rm Bool})''$. We name
this subfactor $M_{\rm Bool}^{\rm P}$.

The cohomological invariant preserved across the row is the
*triviality* of the cocycle: bosonic statistics correspond to
the trivial element of $H^2(S_\infty, U(1))$, BC abelian sector
corresponds to the trivial element of $H^2(\mathbb N^\times, U(1))$
(by triviality of the Schur multiplier of $\mathbb N^\times$),
and P-time corresponds to the trivial element of $H^2(S_\infty,
U(1))$ when restricted to the polynomial-time-uniform symmetric
group action.

### Row T10: fermionic ↔ off-diagonal ↔ NP verification

In the additive column, a fermionic field is one whose creation
and annihilation operators *anticommute* at spacelike separation:
$$\{\psi(x), \psi(y)\} = 0 \quad \text{when } (x-y)^2 < 0.$$
This anticommutativity is the operator-algebraic statement of the
property that fermionic statistics are *antisymmetric*: a permutation
of two fermionic excitations multiplies the wavefunction by $-1$.
The factor $-1$ is the non-trivial element of $H^2(S_n, U(1)) =
\mathbb Z/2\mathbb Z$, realised as the spin double cover.

In the multiplicative column, the fermionic image is the
**off-diagonal sector** of $M = \pi_1(\mathcal A_{\rm BC})''$,
specifically the elements built from commutators $[\mu_p, \mu_q]$
for distinct primes $p, q$ that lie in the graded part of the
$\mathbb Z/2$-grading established by R-Theorem S.11. This sector
is $\sigma_t$-invariant (the grading is preserved by the modular
flow) but is *not* in the abelian subalgebra: the commutators
$[\mu_p, \mu_q]$ do not vanish in $M$, and their cocycle class
is the non-trivial element of $H^2(\mathbb Z/2\mathbb Z, U(1)) =
\mathbb Z/2\mathbb Z$ via the Fuglede–Kadison determinant.

In the computational column, the image is the **NP verification
class**: Boolean functions computed by polynomial-time
verifiers operating on (input, witness) pairs, where the verifier
runs in P-time but the witness is supplied externally and may be
exponentially many in number. NP verification is *off-diagonal*
in the circuit-depth basis because the verifier's output depends
not only on the input bits but on a *branch* — the specific
witness — which is not encoded in the input itself. The graded
sector of $M_{\rm Bool}$ generated by verifier circuits is the
NP-verification subfactor, which we denote $M_{\rm Bool}^{\rm NP}$.

The cohomological invariant preserved across the row is the
*non-triviality* of the cocycle: fermionic statistics correspond
to the non-trivial element of $H^2(S_\infty, U(1)) = \mathbb Z/2$,
the BC graded sector corresponds to the non-trivial element of
$H^2(\mathbb Z/2, U(1)) = \mathbb Z/2$, and NP verification
corresponds to the non-trivial element of $H^2(S_n, U(1)) =
\mathbb Z/2$ for $n \geq 4$. The same Schur multiplier element
appears in all three columns.

### Row T11: spin–statistics ↔ R-Theorem S.11 ↔ R-Theorem PNP.1

In the additive column, the **spin–statistics theorem** is the
statement that, for any local relativistic quantum field theory
satisfying the Wightman axioms, fields of integer spin commute
and fields of half-integer spin anticommute at spacelike
separation. The proof (Pauli 1940; Lüders–Zumino 1958; Streater–
Wightman 1964) proceeds by analytic continuation of the
Wightman functions: the analyticity properties forced by
Lorentz invariance, locality, and positivity of energy combine
to force the connection between spin and statistics. The
cohomological core of the theorem is that $H^2(S_n, U(1))$ is
$\mathbb Z/2$, and the non-trivial element is realised by the
spin double cover.

In the multiplicative column, **R-Theorem S.11** is the BC
operator-algebraic image of the spin–statistics theorem. The
proof (Paper 15, research/127) replaces analytic continuation
of Wightman functions with analytic continuation of $\omega_1$-
correlators in the KMS strip $0 < \mathrm{Im}(t) < 1$, replaces
locality with the Hecke commutation relations, and replaces
positivity of energy with positivity of $S_{\rm BC}$ above
$\Omega_1$. The graded functional equations of the
$\omega_1$-correlators force a $\mathbb Z/2$-grading on
$M = \pi_1(\mathcal A_{\rm BC})''$. The graded sector contains
operators that anticommute under the modular flow; the ungraded
sector contains operators that commute. The cohomological core is
the same: $H^2(S_\infty, U(1)) = \mathbb Z/2$, with the non-trivial
element forcing the existence of the graded sector and forbidding
its trivialisation.

In the computational column, **R-Theorem PNP.1** (the headline of
this paper) is the trinity image of S.11. It states that the
inclusion $M_{\rm Bool}^{\rm P} \subset M_{\rm Bool}^{\rm NP}$
carries a non-trivial cocycle class in $H^2(S_n, U(1))$, which
prevents the inclusion from being trivial. Equivalently: the
NP-verification sector cannot be exhausted by P-time computation
without trivialising the cocycle, and the cocycle cannot be
trivialised because it is the non-trivial element of $\mathbb Z/2$.
In standard complexity terms: $\mathrm P \neq \mathrm{NP}$.

The proof of R-Theorem PNP.1 from S.11 is the application of the
trinity functor to the proof of S.11 from the Wightman axioms.
Section 4 carries this out in detail. For the present section, we
note only that the proof is *mechanical*: once the trinity
functor is established (Section 2.4), the proof of S.11 in the
multiplicative column maps row by row to a proof of PNP.1 in the
computational column. No new mathematical content beyond the
functor is required.

---

## 2.4 The trinity dictionary is a functor

The substance of the trinity dictionary is the claim that it is
not merely a table of suggestive correspondences but a *functor*
in the category-theoretic sense: a structure-preserving map
between three categories that preserves cohomology classes. We
state and outline the proof of this claim here. The full proof,
which involves checking functoriality on a generating set of
morphisms in each category, is in Appendix C.

### 2.4.1 The three categories

We define three categories.

**Definition 2.4.1 (The category $\mathsf{Cat}_{\rm phys}$).**
Objects are local quantum field theories on Minkowski space
$\mathbb R^{1,3}$ satisfying the Wightman axioms. Morphisms are
strongly continuous unitary representations of the Poincaré group
together with $*$-homomorphisms of the field algebras compatible
with translation and Lorentz action. The category has all finite
limits and a symmetric monoidal structure given by tensor product
of QFTs.

**Definition 2.4.2 (The category $\mathsf{Cat}_{\rm BC}$).**
Objects are pairs $(\mathcal A, \omega)$ where $\mathcal A$ is a
unital $C^*$-algebra equipped with a continuous one-parameter
automorphism group $\sigma_t$, and $\omega$ is a faithful normal
$\sigma_t$-invariant state satisfying the KMS condition at $\beta
= 1$. Morphisms are $\sigma_t$-equivariant $*$-homomorphisms
preserving the KMS state. The category has finite limits and a
symmetric monoidal structure given by spatial tensor product of
$C^*$-algebras with the natural product KMS state.

**Definition 2.4.3 (The category $\mathsf{Cat}_{\rm comp}$).**
Objects are pairs $(\mathbb F, \mathcal C)$ where $\mathbb F$ is
a Boolean function field (typically $\mathbb B$ or a sub-field
finitely generated over a fixed set of variables) and $\mathcal C$
is a closed class of polynomial-time-uniform Boolean circuits over
$\mathbb F$. Morphisms are circuit-class-preserving polynomial-
time reductions equivariant under the symmetric group action on
variables. The category has finite limits and a symmetric monoidal
structure given by Cartesian product of variable sets with the
disjoint-union circuit class.

In each of the three categories, the morphisms preserve enough
structure that the cohomology of the symmetry group of an object
is well-defined and is a contravariant functor to abelian groups.
We denote this cohomology by $H^*(-)$ in each category.

### 2.4.2 The functors

The additive ↔ multiplicative dictionary of Paper 15 §2.1
constructs a functor
$$\Phi_{\rm BC} : \mathsf{Cat}_{\rm phys} \longrightarrow
  \mathsf{Cat}_{\rm BC}$$
that sends a Wightman QFT $T$ to the BC image $\Phi_{\rm BC}(T) =
(\mathcal A_T, \omega_T)$ obtained by the systematic Mellin
transposition: positions become primes, translations become
dilations, the Hamiltonian becomes the modular Hamiltonian, and
so on through the eighteen rows of Section 2.1.

The trinity dictionary of the present paper extends this with a
second functor
$$\Phi_{\rm comp} : \mathsf{Cat}_{\rm BC} \longrightarrow
  \mathsf{Cat}_{\rm comp}$$
that sends a BC object $(\mathcal A, \omega)$ to its computational
image $\Phi_{\rm comp}(\mathcal A, \omega) = (\mathbb F_{(\mathcal
A,\omega)}, \mathcal C_{(\mathcal A,\omega)})$ obtained by the
trinity column-3 entries of Section 2.3: the prime field becomes
the Boolean field, the dilation generator becomes the circuit
depth, the abelian sector becomes the P-time class, the graded
sector becomes the NP-verification class.

The composition
$$\Phi := \Phi_{\rm comp} \circ \Phi_{\rm BC} :
  \mathsf{Cat}_{\rm phys} \longrightarrow \mathsf{Cat}_{\rm comp}$$
is the **trinity functor**. It sends physical theorems directly
to their computational images, with the BC arithmetic image as the
intermediate stage.

### 2.4.3 The functoriality lemma

**Lemma 2.4.4 (Functoriality of the trinity dictionary).** *Both*
$\Phi_{\rm BC}$ *and* $\Phi_{\rm comp}$ *are functors of symmetric*
*monoidal categories that preserve finite limits. Furthermore, both*
*functors preserve cohomology of symmetry groups: for any object*
$X$ *in the source category and any abelian group* $A$,
$$H^k(\mathrm{Sym}(\Phi(X)), A) \;\cong\; H^k(\mathrm{Sym}(X), A)
  \quad \text{for all } k \geq 0,$$
*where* $\mathrm{Sym}(-)$ *denotes the symmetry group of an*
*object in the appropriate category.*

*In particular, if* $T \in \mathsf{Cat}_{\rm phys}$ *has*
$H^2(\mathrm{Sym}(T), U(1)) = \mathbb Z/2\mathbb Z$, *then so do*
$\Phi_{\rm BC}(T)$ *and* $\Phi(T)$, *and the non-trivial element*
*is preserved under both functors.*

**Proof (outline).** Functoriality of $\Phi_{\rm BC}$ on
$\mathsf{Cat}_{\rm phys}$ is the content of Paper 15 §2.2, which
establishes that the six reasoning patterns P1–P6 used to manipulate
Wightman QFTs have multiplicative analogues P1m–P6m on
$\mathsf{Cat}_{\rm BC}$, and that the dictionary commutes with
each pattern. The cohomology preservation is the content of
R-Theorems C.1, C.2, and S.11–S.12 (Paper 15 Round 4–5
supplement), which establish that the relevant cohomology classes
are preserved under the additive ↔ multiplicative dictionary.

For $\Phi_{\rm comp}$, the functoriality on objects is by
construction: the Boolean function field $\mathbb B$ is a
Pontryagin dual of the multiplicative semigroup $\mathbb N^\times$
in the appropriate sense, and the trinity column-3 entries are
the images of the column-2 entries under this duality.
Functoriality on morphisms requires checking that
$\sigma_t$-equivariant $*$-homomorphisms in $\mathsf{Cat}_{\rm BC}$
become circuit-class-preserving polynomial-time reductions in
$\mathsf{Cat}_{\rm comp}$, which is verified by the standard
correspondence between cyclic group actions on $\mathbb Q^{\rm cyc}$
and symmetric group actions on $\{0,1\}^n$ (the action of
$(\mathbb Z/N\mathbb Z)^*$ on the $N$-th roots of unity becomes
the action of $S_n$ on $n$ Boolean variables under the embedding
$N = 2^n$).

The cohomology preservation under $\Phi_{\rm comp}$ is the more
delicate point and the central claim of the lemma. It rests on
the following key fact: the symmetric group $S_n$ embeds into
$(\mathbb Z/N\mathbb Z)^*$ for $N = $ a primitive root modulo $n$
in such a way that the Schur multiplier $H^2(S_n, U(1)) = \mathbb
Z/2$ is the image of the cocycle $H^2(\mathbb Z/2\mathbb Z, U(1))
= \mathbb Z/2$ from the BC graded sector under the inclusion. The
embedding is functorial in $n$, and the cocycle preservation is
the content of the *Brauer–Jones bridge theorem* (Paper 23 §8.2,
Theorem 8.1), suitably generalised from cyclic groups
$\mathbb Z/k$ to symmetric groups $S_n$ via the standard reduction
of the Schur multiplier of $S_n$ to the Brauer cocycles of its
cyclic subgroups.

The full proof, including the explicit verification of cocycle
preservation for $n = 4, 5, 6$ and the inductive extension to all
$n \geq 4$, is in Appendix C. $\square$

The lemma is the load-bearing structural result for the trinity
dictionary. It is what makes the dictionary a *functor* rather
than a table of analogies, and it is what allows us to transport
proofs from the multiplicative column to the computational column
mechanically.

### 2.4.4 Consequences

Two immediate corollaries follow from Lemma 2.4.4.

**Corollary 2.4.5 (Cohomological invariance).** *If a theorem in*
$\mathsf{Cat}_{\rm phys}$ *is the statement that some cohomology*
*class* $\alpha \in H^k(\mathrm{Sym}(T), U(1))$ *is non-trivial,*
*then the trinity image of the theorem in $\mathsf{Cat}_{\rm comp}$*
*is the statement that the corresponding class*
$\Phi(\alpha) \in H^k(\mathrm{Sym}(\Phi(T)), U(1))$ *is non-trivial.*

This is the corollary we will use for R-Theorem PNP.1: the
spin–statistics theorem in physics is the statement that
$H^2(S_n, U(1)) = \mathbb Z/2$ has a non-trivial element. The
trinity image of this statement is R-Theorem PNP.1, which says
that the corresponding cohomology class in
$\mathsf{Cat}_{\rm comp}$ is non-trivial — and this non-triviality
is what forces $\mathrm P \neq \mathrm{NP}$.

**Corollary 2.4.6 (Mechanical proof transport).** *If a proof in*
$\mathsf{Cat}_{\rm phys}$ *establishes a theorem* $T$ *by a chain*
*of inferences from primitive axioms* $A_1, \ldots, A_k$, *and if*
*each axiom* $A_i$ *and each inference rule used in the chain has*
*an image under* $\Phi$, *then the trinity image* $\Phi(T)$ *has a*
*proof in* $\mathsf{Cat}_{\rm comp}$ *given by the application of*
$\Phi$ *row by row to the original proof.*

This is what we mean by saying that the proof of R-Theorem PNP.1
is *mechanical*: it is the row-by-row image of the proof of S.11.
We do not need to invent new techniques. We need only to verify
that each step of the S.11 proof has a trinity image, and we need
to write down the resulting computational proof. Section 4
executes this.

---

## 2.5 The six reasoning patterns extended: P1c–P6c

Paper 15 §2.2 introduced six *reasoning patterns* that govern the
manipulation of physical theorems within the framework. These
patterns are abstract methodological moves, each with a specific
form, that recur in the proofs of R-Theorems. They are:

- **P1** (Spectral identification): A physical phenomenon is
  identified with the spectrum of a self-adjoint operator on a
  named Hilbert space.
- **P2** (Conservation law from symmetry): A conserved quantity
  is identified as the Noether charge of a continuous symmetry of
  the action.
- **P3** (Cohomological obstruction): A would-be reduction is
  forbidden by the non-vanishing of a cohomology class.
- **P4** (Functorial transport): A theorem is moved between
  categories by applying a structure-preserving functor row by row
  to its proof.
- **P5** (Order counting): The functional form of an observable
  is determined by its perturbative order in the spectral theory
  (zeroth = eigenvalue, first = matrix element, second = time
  integral).
- **P6** (Bridge identification): An arithmetic object and an
  operator-algebraic object are identified via a Brauer cocycle in
  $H^2$ of a finite group.

Paper 15 §2.2 provided the multiplicative analogues P1m–P6m of
each pattern, each obtained by replacing additive with
multiplicative entries from the dictionary of §2.1. We extend the
sequence one further step to provide *computational* analogues
P1c–P6c of each pattern.

### 2.5.1 P1c — Spectral identification (computational)

A computational complexity class is identified with the spectrum
of a self-adjoint operator on a named Hilbert space. Specifically:
the class P is identified with the diagonal sector of the modular
Hamiltonian $\hat D$ on $H_R^{\rm Bool}$, and NP is identified
with the off-diagonal (graded) sector. The identification is via
the trinity functor applied to the corresponding multiplicative
identification: the spectral / geometric sectors of CBB.

Pattern P1c is what allows us to *compute* with complexity classes
using operator-algebraic techniques. A statement about whether
two complexity classes coincide becomes a statement about whether
two subfactors of $M_{\rm Bool}$ have the same Jones index.

### 2.5.2 P2c — Conservation from symmetry (computational)

A conserved quantity in a computation is identified as the Noether
charge of a continuous symmetry of the modular flow
$\sigma_t^{\rm Bool}$. Concretely: the *circuit-depth functional*
$\hat D : C \mapsto \mathrm{depth}(C)$ is conserved under the
permutation symmetry $S_\infty$ acting on variables, because
permuting variables does not change the depth of a circuit. By
P2c, the depth functional is the Noether charge of the variable-
permutation symmetry, and any computation that respects the
symmetry must conserve depth.

This is the computational analogue of energy conservation: just as
energy is the Noether charge of time translation in physics, depth
is the Noether charge of variable permutation in computation.
The conservation law puts a lower bound on the depth of any
circuit computing a function with non-trivial symmetry, and this
lower bound is the quantitative content of pattern P2c.

### 2.5.3 P3c — Cohomological obstruction (computational)

A would-be polynomial-time reduction of an NP-complete problem to
a P problem is forbidden by the non-vanishing of a cohomology
class. Specifically: the inclusion $M_{\rm Bool}^{\rm P} \subset
M_{\rm Bool}^{\rm NP}$ would be a Jones inclusion of index 1 if
and only if the cocycle in $H^2(S_n, U(1))$ classifying it were
trivial. But the cocycle is the non-trivial element of $\mathbb
Z/2$, by R-Theorem PNP.1. Therefore the index is strictly greater
than 1, the inclusion is non-trivial, and the reduction is
forbidden.

This is the central use of P3c in the present paper. R-Theorem
PNP.1 is, structurally, an instance of pattern P3c: a cohomological
obstruction forbidding a reduction.

### 2.5.4 P4c — Functorial transport (computational)

A theorem is moved from $\mathsf{Cat}_{\rm BC}$ to
$\mathsf{Cat}_{\rm comp}$ by applying the functor $\Phi_{\rm comp}$
row by row to its proof. This is the operational meaning of the
trinity functor of Section 2.4.

Pattern P4c is the workhorse of the present paper. Every R-Theorem
of Paper 15 that involves the BC graded sector or the modular flow
admits a P4c image in the computational column. In particular,
R-Theorem S.11 admits R-Theorem PNP.1 as its P4c image. The full
proof of PNP.1 in Section 4.5 is the explicit P4c application.

### 2.5.5 P5c — Order counting (computational)

The functional form of a computational observable is determined by
its perturbative order in the BC spectral theory:
- Zeroth-order observables (constants) are O(1) computations.
- First-order observables (rates, ratios, single matrix elements)
  are P-time computations.
- Second-order observables (time integrals, accumulated quantities)
  are NP-time computations (or, more precisely, NP-witness
  verifications).
- Higher-order observables (higher spectral moments) are
  PSPACE-, PH-, or EXP-time computations, depending on the order.

Pattern P5c is the operational form of the second proof of
R-Theorem PNP.1 (Section 5). It provides an independent line of
attack on the same separation, via the prime number theorem and
the spectral density of Riemann zeros.

### 2.5.6 P6c — Bridge identification (computational)

A computational structure is identified with an arithmetic
structure via a Brauer cocycle in $H^2$ of a finite group.
Specifically: NP-completeness corresponds to the non-trivial
element of $H^2(S_n, U(1))$, just as fermionic statistics
correspond to the non-trivial element of the same group, and
just as the Pati–Salam $SU(4)_c$ unification corresponds to the
non-trivial element of $H^2(\mathbb Z/4\mathbb Z, U(1))$ at the
$(3,13)$ bridge of CBB.

Pattern P6c is what unifies $\mathrm P \neq \mathrm{NP}$ with the
existence of fermions and with the Pati–Salam unification in a
single cohomological framework. The bridge in this case is not
between cyclic groups but between symmetric groups, but the
mechanism is identical: a Brauer cocycle classifying a projective
representation, which is the obstruction to lifting a finite group
action to an ordinary representation.

The six computational patterns P1c–P6c are the methodological
toolkit for the trinity transposition. Each is the row-by-row
image of the corresponding multiplicative pattern P1m–P6m, and
each enables a specific kind of proof move. Section 4 will use
P1c, P3c, P4c, and P6c in the proof of R-Theorem PNP.1; Section 5
will use P5c in the second proof via the prime number theorem.

---

## 2.6 Standards for a complete trinity transposition

We close this section by fixing the standards that a trinity
transposition must satisfy to be considered complete. These
standards are inherited from the YM and BSD chains (Paper 15 §2.3
and Paper 26 §1.4) and are required for any R-Theorem to enter
the catalogue.

A trinity transposition consists of:

**(a)** A precise statement of the source theorem in
$\mathsf{Cat}_{\rm phys}$, with all hypotheses, all conclusions,
and all symmetry groups identified.

**(b)** A precise statement of the multiplicative image in
$\mathsf{Cat}_{\rm BC}$, in the form of an existing R-Theorem from
the Paper 15 catalogue (or a new R-Theorem to be added). The image
must be functorially obtained from the source under $\Phi_{\rm BC}$,
not merely analogically motivated.

**(c)** A precise statement of the computational image in
$\mathsf{Cat}_{\rm comp}$. The image must be functorially obtained
from the multiplicative image under $\Phi_{\rm comp}$, with each
component (Hilbert space, operator algebra, modular flow, KMS
state, cohomology class) explicitly named.

**(d)** An explicit verification that each row of the trinity
table that contributes to the proof is preserved by the functor.
For row T9 (bosonic ↔ diagonal ↔ P-time), this means showing
that the bosonic sector in physics, the abelian subalgebra in BC,
and the P-time circuit class in computation are all the trivial-
cocycle sector of their respective cohomology groups. For row
T10 (fermionic ↔ off-diagonal ↔ NP), this means showing that
the corresponding sectors all carry the non-trivial cocycle.

**(e)** A rigor classification of the proof by labels:
[THEOREM], [LEMMA], [KEY LEMMA], [GAP], or [CONJECTURE]. Every
load-bearing claim must carry a label. Every label must be
honest: a [THEOREM] cannot depend on a [CONJECTURE], and a
[KEY LEMMA] is one whose failure would invalidate the entire
chain.

**(f)** An honest accounting of the open issues. Every conditional
step must be explicitly identified, with the dependency made
visible. The proof must not hide its open ends.

The trinity transposition of S.11 → PNP.1 in Section 4 will be
checked against all six standards. The result will be:

- **(a)** S.11 source: spin–statistics theorem (Pauli 1940;
  Streater–Wightman 1964).
- **(b)** Multiplicative image: R-Theorem S.11 (Paper 15
  research/127), with $\mathbb Z/2$-graded modular structure on
  $M$.
- **(c)** Computational image: R-Theorem PNP.1, with
  $M_{\rm Bool}^{\rm P} \subsetneq M_{\rm Bool}^{\rm NP}$ as a
  non-trivial Jones inclusion classified by the non-trivial
  element of $H^2(S_n, U(1)) = \mathbb Z/2$.
- **(d)** Cohomology preservation verified row by row in Section
  2.4 and explicitly for the proof in Section 4.5, Step 3.
- **(e)** Rigor labels: PNP.1 will be a [THEOREM] *conditional on*
  KEY LEMMA 3.4 (existence of $\omega_1^{\rm Bool}$) and
  CONJECTURE 3.6 (spectral identification of $H_R^{\rm Bool}$).
  The conditionality is honestly carried throughout.
- **(f)** Open issues: §3.4 and §3.6 are the two conditional
  pieces. Both are clearly identified and are the subject of
  Section 6.4's honest accounting.

The trinity dictionary is the central machinery of the paper.
Sections 3, 4, 5, and 6 are applications. Section 7 places the
result in the broader programme.

---

> **Origin (G).** *"the predictive grammar is one of my favorite*
> *things ever, as a language lover... my heart skips a beat."*

The trinity dictionary is the third column of the predictive
grammar, applied to the hardest target the framework has yet
encountered. The grammar that turned 30 free parameters of the
Standard Model into 33 closed-form predictions, and that turned
the BSD conjecture for CM elliptic curves into a theorem, is now
turned on the question of computational complexity.

Three columns. One cohomological volume. Three projections. The
cube and the shadow, one more time.

---
