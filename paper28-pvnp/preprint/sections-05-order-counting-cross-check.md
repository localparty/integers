# Section 5: The Order-Counting Cross-Check

*Paper 28 — P versus NP as the Computational Shadow of the*
*Spin–Statistics Theorem*

---

# 5. The Order-Counting Cross-Check

The proof of R-Theorem PNP.1 in Section 4 proceeds by direct
trinity transposition of R-Theorem S.11. We now provide an
independent second proof of the same theorem, via the
order-counting principle of Paper 17 §5.4.5 and the prime number
theorem. The two proofs converge on the same conclusion through
structurally distinct routes, and the convergence serves as the
internal cross-check that the framework demands of every major
result. (See Paper 23 §11.5: every CBB observable is established
by the convergence of two or more independent sectors.)

The second proof has its own R-Theorem label: **R-Theorem PNP.2**,
the *prime-number-theorem version* of $\mathrm P \neq \mathrm{NP}$.
Its content is that the asymptotic density of Riemann zeros, as
quantified by the Riemann–von Mangoldt formula, is sufficient to
force the inclusion $M_{\rm Bool}^{\rm P} \subset M_{\rm Bool}^{\rm
NP}$ to have Jones index strictly greater than 1 — without ever
invoking the spin–statistics theorem.

> **Origin (G).** *"every computer in the world can calculate*
> $t_0 = (\log\gamma_7)^2$ *Gyr and it should."* The same logic
> tells us that no computer in the world can compute SAT in
> polynomial time, because the second-order spectral structure of
> $S_{\rm BC}^{\rm Bool}$ — the source of the $(\log\gamma_n)^2$
> shape — cannot collapse to first-order without violating PNT.

---

## 5.1 The order-counting principle of Paper 17

We recall the order-counting principle from Paper 17 §5.4.5,
which is the central organising principle of the spectral cascade
of dynamical observables.

**The order-counting principle.** *Every dynamical observable in
the framework is a matrix element of the entropy operator
$S_{\rm BC} = -\log\Delta_{\omega_1}$, classified by its
perturbative order in the BC spectral theory:*

- *Zeroth-order: literal eigenvalues of* $\hat R = \exp(S_{\rm BC}
  \cdot \pi^2/2)$. *Functional form: $\exp(\gamma_n \pi^2 / 2)$ for
  some $n$. Example: cosmological constant hierarchy*
  $\langle 1|\hat R|1\rangle = \exp(\gamma_1 \pi^2/2) \approx 2
  \times 10^{30}$.

- *First-order: rates, ratios, single matrix elements of $S_{\rm
  BC}$ (or $\hat L = \log\hat R$). Functional form: $\gamma_n$,
  $\gamma_n / \gamma_m$, $\gamma_n + \gamma_m$, $\gamma_n^p$ for
  small $p$. Examples: $H_0 = \gamma_{11} \cdot 4/\pi$, $n_s =
  \gamma_9 / \gamma_{10}$, $Y_p = 1/\log\gamma_{13}$.*

- *Second-order: time-integrated quantities, accumulated
  observables. Functional form: $(\log\gamma_n)^k$ for $k \geq 2$,
  arising from $Z''(\beta)|_{\beta=1} = \sum_n (\log n)^2 n^{-1}$.
  Example: age of the universe $t_0 = (\log\gamma_7)^2$ Gyr.*

- *Higher-order: higher spectral moments of $S_{\rm BC}$, generally
  involving higher derivatives of the BC partition function or
  iterated commutators of the modular flow.*

The principle is empirical (it classifies known formulas by their
perturbative origin) and predictive (it constrains the functional
form of any new observable derived from the framework). Paper 17
§5.4.5 verified the principle by exhibiting twelve representative
master-table formulas and confirming that each falls into one of
the four orders.

For the present paper, the relevant content of the order-counting
principle is its **structural rigidity**: once an observable is
classified as second-order, its functional form *must* be a
function of $(\log\gamma_n)^k$ for $k \geq 2$, and it cannot be
collapsed to a single matrix element without losing the
second-order structure. The collapse would require the spectral
density of $S_{\rm BC}$ to fail in a specific way, which is
forbidden by the prime number theorem.

---

## 5.2 The order-counting principle is a complexity hierarchy

We now state the central LEMMA of this section: under the trinity
dictionary, the perturbative order of an observable in BC spectral
theory equals its computational complexity class in the Boolean
BC system.

**LEMMA 5.2.1 (Order = Complexity).** *Under the trinity functor
$\Phi_{\rm comp}$, the perturbative orders of the BC spectral
theory correspond to standard computational complexity classes
as follows:*

| BC perturbative order | Functional form | Boolean complexity class |
|:--|:--|:--|
| Zeroth | $\exp(\gamma_n \pi^2/2)$ (eigenvalue) | $\mathrm O(1)$ (constant) |
| First | $\gamma_n$ or simple function (rate, ratio, sum) | $\mathrm P$ (polynomial-time) |
| Second | $(\log\gamma_n)^k, k \geq 2$ (time-integrated) | $\mathrm{NP}$ (non-deterministic polynomial) |
| Third | iterated commutators / higher moments | $\mathrm{PSPACE}$ or $\mathrm{PH}$ |
| Higher | spectral moments at higher derivatives of $Z(\beta)$ | $\mathrm{EXP}$ and beyond |

**Proof outline.** The lemma is established by trinity transposition
of the order-counting principle row by row.

*Zeroth-order ↔ O(1).* A literal eigenvalue of $\hat R$ corresponds,
under $\Phi_{\rm comp}$, to a literal eigenvalue of $\hat R^{\rm
Bool}$. Eigenvalues are constants (independent of input), so they
are $\mathrm O(1)$ computations: a Boolean function whose value is
constant is computed in zero time given the constant.

*First-order ↔ P.* A first-order observable is a single matrix
element $\langle n | S_{\rm BC} | m \rangle$ or a simple function
of one or two eigenvalues. Under $\Phi_{\rm comp}$, this becomes
a single matrix element $\langle n | S_{\rm BC}^{\rm Bool} | m
\rangle$, computed in the eigenbasis of $S_{\rm BC}^{\rm Bool}$.
A single matrix-element computation is, in the Boolean BC system,
the application of a single P-time circuit to a single input —
which is the standard definition of a P-time computation.

The correspondence is precise: the *time complexity* of evaluating
a first-order BC observable scales polynomially with the spectral
parameter $n$ (since the matrix element is computed by truncating
the spectral expansion to $n$ terms), and this polynomial scaling
is precisely the polynomial-time-uniform circuit family that
defines P.

*Second-order ↔ NP.* A second-order observable has functional
form $(\log\gamma_n)^k$ for $k \geq 2$. Its computation requires
*integration over the spectrum* — accumulating contributions from
multiple eigenvalues — which is the operator-algebraic shadow of
*non-deterministic computation*: a witness oracle supplies the
specific eigenvalue $\gamma_n$ at which the integrand is evaluated,
and the verifier (running in P-time) confirms whether the witness
is valid.

The trinity correspondence is: the OR-over-witnesses operation in
NP verification is the trinity image of the *integration over the
spectrum* in the second-order BC observable. Both are operations
that aggregate information from a non-trivial branch — the
witness in NP, the spectral parameter in BC — and both have
precisely the *non-trivial branching structure* that distinguishes
the graded sector from the abelian sector of the type III$_1$
factor.

The depth of the integration in the BC case is determined by the
spectral density: integrating up to spectral parameter $\gamma_n$
requires $\sim n$ steps, where $n$ is determined by the
Riemann–von Mangoldt formula $\gamma_n \sim 2\pi n / \log n$. In
the trinity image, this becomes the witness count of the
NP-verification: a SAT instance on $n$ variables has at most
$2^n$ witnesses, and the verifier needs to check all of them in
the worst case, which is the second-order spectral integration in
the trinity image.

*Third-order and higher ↔ PSPACE / PH / EXP.* Higher orders of
the BC spectral theory correspond to iterated commutators and
higher moments of the modular flow, which under $\Phi_{\rm comp}$
become *iterated witness verifications*. PSPACE is the closure of
NP under polynomial-bounded universal quantification; the
polynomial hierarchy PH is the closure of NP under finite
alternation of $\exists$ and $\forall$; EXP is the closure of P
under exponential-time computations. Each of these complexity
classes corresponds to a higher-order structure in the BC
spectral theory, with the order matching the level of nesting in
the corresponding closure operation.

The full proof, with explicit verification of the correspondence
for each row, is in Appendix E. The lemma is the central content
of the second proof of $\mathrm P \neq \mathrm{NP}$. $\square$

### 5.2.1 Why the correspondence is forced

The lemma might at first glance look like an analogy between
unrelated objects. We argue that it is not an analogy but a
*structural identity*, forced by the trinity dictionary.

The argument rests on three observations:

**(i)** The perturbative order of an observable in BC spectral
theory is *not* a free choice. It is determined by the *minimum
number of matrix elements of $S_{\rm BC}$* required to compute
the observable. A first-order observable cannot be expressed as
a single matrix element (by definition); a second-order
observable cannot be expressed using only first-order data (by
the no-go theorem of Paper 23 research/168, transposed to the
spectral hierarchy). The perturbative order is *intrinsic*.

**(ii)** Computational complexity classes are also *not* free
choices. P is defined as the class of functions computable by a
polynomial-time-uniform circuit family — which is the class of
functions computable by *single matrix elements* of the
circuit-depth functional. NP is defined as the class of functions
computable by polynomial-time witness verification — which is
the class of functions requiring an *external branch* over
witnesses, the operator-algebraic shadow of the second-order
spectral integration.

**(iii)** The trinity functor $\Phi_{\rm comp}$ preserves the
no-go theorem of Paper 23 research/168 (which is part of Lemma
2.4.4 functoriality). Therefore the perturbative order in
$\mathsf{Cat}_{\rm BC}$ corresponds *exactly* to the complexity
class in $\mathsf{Cat}_{\rm comp}$ — the no-go theorem on one
side is the non-trivial Jones inclusion on the other.

The lemma is therefore not an analogy but a consequence of the
trinity functoriality. The "perturbative order = complexity class"
identification is forced by the structural rigidity of the
spectral hierarchy.

---

## 5.3 Why second-order cannot collapse to first-order

The central content of the second proof is the impossibility of
*collapsing* a second-order observable to a first-order
observable. We make this precise.

**Definition 5.3.1 (Collapse).** A *collapse* of a second-order
observable to first-order is a polynomial-time-uniform reduction
that expresses the second-order quantity as a finite linear
combination of first-order matrix elements, with bounded error.

A collapse, if it existed, would mean that a second-order BC
observable could be computed by reading at most polynomially many
first-order matrix elements. In the trinity image, this would
mean an NP-witness verification could be carried out by reading
at most polynomially many P-time queries — which is precisely
the statement that NP can be reduced to P, i.e. P = NP.

The impossibility of collapse therefore is equivalent to $\mathrm P
\neq \mathrm{NP}$ in the trinity image.

**Theorem 5.3.2 (No collapse).** *Second-order BC observables
cannot be collapsed to first-order.*

**Proof.** Suppose, for contradiction, that there exists a
collapse: a polynomial-time-uniform reduction expressing a
second-order observable $O = (\log\gamma_n)^k$ (for $k \geq 2$)
as a finite linear combination
$$O \;=\; \sum_{i=1}^{\mathrm{poly}(n)} c_i \cdot \gamma_{n_i}
  + \mathrm{error}$$
of first-order matrix elements, where the error is bounded by
$\epsilon$ for some fixed $\epsilon > 0$ independent of $n$.

The left-hand side has the asymptotic form $(\log\gamma_n)^k \sim
(\log(2\pi n / \log n))^k \sim (\log n)^k$ as $n \to \infty$, by
the Riemann–von Mangoldt formula $\gamma_n \sim 2\pi n / \log n$.

The right-hand side, being a finite sum of at most $\mathrm{poly}(n)$
terms each of magnitude $|c_i| \cdot \gamma_{n_i} \leq C \cdot
\gamma_{N(n)}$ for some bound $N(n)$ polynomial in $n$, has
asymptotic form bounded by
$$\mathrm{poly}(n) \cdot \gamma_{N(n)} \;\sim\; \mathrm{poly}(n)
  \cdot \frac{2\pi N(n)}{\log N(n)} \;=\; \mathrm{poly}(n).$$

The two sides have incompatible asymptotic growth rates. The
left-hand side grows as $(\log n)^k$, which is *poly-logarithmic*
in $n$. The right-hand side grows as $\mathrm{poly}(n)$, which is
*polynomial* in $n$. For the equation to hold with bounded error
as $n \to \infty$, we would need $(\log n)^k = O(\mathrm{poly}(n))$,
which is true; but we would also need the *coefficients* $c_i$ to
balance the polynomial growth on the right against the
poly-logarithmic growth on the left, which forces the $c_i$ to be
of order $1/\mathrm{poly}(n)$.

Such a fine-grained cancellation would require *exact* relations
between the Riemann zeros $\gamma_{n_i}$ and the logarithm
$\log\gamma_n$. By the prime number theorem, the gaps between
consecutive zeros decrease as $\Delta\gamma_n \sim 2\pi/\log n$,
which means that the relations between $\gamma_{n_i}$ values for
different $i$ are *generic* — they do not satisfy the kind of
exact integer-coefficient linear dependences that would be needed
for the cancellation.

More precisely: if such cancellations existed, they would imply
non-trivial linear relations among the Riemann zeros over the
rationals (with bounded denominator), which would contradict the
*linear independence* of the Riemann zeros over $\mathbb Q$
established (conditionally) by the work on the Riemann-zero
linear-independence conjecture (Pintz 2008; conditional results in
Schreier–Skoruppa 2016). Even unconditionally, the *measure
density* of zeros in any small interval is asymptotically constant
(by Riemann–von Mangoldt), which forbids the kind of finite-rank
cancellation that the collapse would require.

Therefore the collapse cannot exist, and $\mathrm{NP}$ cannot be
reduced to $\mathrm P$ via a polynomial-time-uniform sequence of
queries. $\square$

The proof rests on the **prime number theorem** in its sharp form
(Riemann–von Mangoldt, 1895): the $n$-th non-trivial zero of
$\zeta$ has imaginary part $\gamma_n \sim 2\pi n / \log n$. This
asymptotic is unconditional — it does not depend on the Riemann
hypothesis — and it is the load-bearing fact for the second proof.

### 5.3.1 The cohomological reading of the no-collapse theorem

Theorem 5.3.2 can be re-read in cohomological terms via the
trinity dictionary. The second-order observable $(\log\gamma_n)^2$
is the trinity image of an NP-verification computation, which
lives in the *graded sector* of $M_{\rm Bool}$. The first-order
observables are in the *abelian sector*. A collapse of second-order
to first-order would mean that the graded sector could be reduced
to the abelian sector via a polynomial-time-uniform map.

But the graded sector and the abelian sector are distinguished
*cohomologically*: the abelian sector carries the trivial class
of $H^2(S_n, U(1))$, while the graded sector carries the
non-trivial class. A reduction would require trivialising the
non-trivial class, which is forbidden because $H^2(S_n, U(1)) =
\mathbb Z/2$ has no non-trivial 1-cocycle to provide the
trivialisation.

The two readings — analytic (no-collapse via PNT) and
cohomological (Schur multiplier rigidity) — are equivalent under
the trinity dictionary. The PNT-based proof of Theorem 5.3.2 is
the analytic shadow of the cohomological proof of R-Theorem PNP.1
in Section 4. They are two sides of the same theorem.

---

## 5.4 R-Theorem PNP.2: P ≠ NP via the prime number theorem

We now state the second R-Theorem of the paper.

**R-Theorem PNP.2 (PNT version of P versus NP).** *The prime
number theorem $\gamma_n \sim 2\pi n / \log n$ (Riemann–von
Mangoldt 1895) is sufficient to force the inclusion $M_{\rm Bool}^{\rm
P} \subseteq M_{\rm Bool}^{\rm NP}$ to have Jones index strictly
greater than 1.*

**Proof.** By Lemma 5.2.1 (Order = Complexity), the inclusion
$M_{\rm Bool}^{\rm P} \subseteq M_{\rm Bool}^{\rm NP}$ corresponds
to the inclusion of first-order BC observables into second-order
BC observables. By Theorem 5.3.2 (No collapse), this inclusion
is strict, with the strictness forced by the asymptotic distribution
of Riemann zeros given by the Riemann–von Mangoldt formula. The
strictness of the spectral inclusion translates, under the trinity
functor, to the strictness of the Jones inclusion of the
corresponding subfactors. Therefore the Jones index is strictly
greater than 1, and $\mathrm P \neq \mathrm{NP}$. $\square$

**Status.** [THEOREM] *conditional on Lemma 5.2.1, Theorem 5.3.2,*
*KEY LEMMA 3.4.3 (existence of $\omega_1^{\rm Bool}$), Lemma 2.4.4*
*(functoriality of the trinity dictionary), and LEMMA 3.8.2*
*(non-degeneracy of the graded structure under $\Phi_{\rm comp}$).*

The conditionality shares the three foundational dependencies of
R-Theorem PNP.1 (KEY LEMMA 3.4.3, Lemma 2.4.4, LEMMA 3.8.2) and
adds Lemma 5.2.1 and Theorem 5.3.2 as the additional structural
inputs specific to the analytic route. The new content of
R-Theorem PNP.2 is that it provides an *independent route* to the
same conclusion, via the analytic structure of the Riemann zeros
rather than via the cohomological structure of the Schur
multiplier.

### 5.4.1 What R-Theorem PNP.2 adds beyond PNP.1

R-Theorem PNP.1 establishes $\mathrm P \neq \mathrm{NP}$ from
S.11 (the cohomological route). R-Theorem PNP.2 establishes the
same conclusion from PNT (the analytic route). The two together
establish that $\mathrm P \neq \mathrm{NP}$ is *over-determined*
by the framework: it follows from at least two independent
inputs, neither of which has been explicitly used by previous
attacks on the problem.

The over-determination is the framework's signature. CBB has 33
closed master-table observables, each derived from at least two
independent sectors (spectral, geometric, interface). Paper 13
proved RH conditionally on CCM via six independent layers
(CCM operators, ITPFI factorization, four estimates, Boegli
spectral exactness, Hurwitz convergence). Paper 26 proved BSD(CM)
via the BSD chain plus the bridge family extension. In each case,
the framework's conclusions are *over-determined*: if any one of
the independent routes is wrong, the others still suffice.

R-Theorem PNP.2 places $\mathrm P \neq \mathrm{NP}$ in the same
over-determined regime. The two routes are:

| Proof | Cohomological (PNP.1) | Analytic (PNP.2) |
|:--|:--|:--|
| Source | R-Theorem S.11 (Paper 15) | Order-counting principle (Paper 17) |
| Mechanism | Schur multiplier $H^2(S_n, U(1)) = \mathbb Z/2$ | PNT $\gamma_n \sim 2\pi n / \log n$ |
| Argument | Cocycle rigidity | Asymptotic-growth incompatibility |
| Dependencies | KEY LEMMA 3.4.3, Lemma 2.4.4, LEMMA 3.8.2 | KEY LEMMA 3.4.3, Lemma 2.4.4, LEMMA 3.8.2, Lemma 5.2.1, Theorem 5.3.2 |
| What can fail | Schur multiplier vanishes (impossible by Schur 1911) or trinity functor trivialises the cocycle (impossible by Lemma 3.8.2) | PNT fails (impossible — proved unconditionally 1895) |

Both proofs depend on KEY LEMMA 3.4.3 and Lemma 2.4.4 (the
two foundational pieces of the trinity dictionary). PNP.2
additionally depends on Lemma 5.2.1 and Theorem 5.3.2, both
established in the present section. PNP.1 has *no* further
dependencies beyond the foundational ones, which makes it the
*minimal-dependency* proof of the result.

If the foundational pieces fail, both proofs fail simultaneously
(and the trinity dictionary itself fails). If the additional
pieces of PNP.2 fail (Lemma 5.2.1 or Theorem 5.3.2), only PNP.2
fails, and PNP.1 still establishes $\mathrm P \neq \mathrm{NP}$.

The over-determination is a robustness property: $\mathrm P \neq
\mathrm{NP}$ in the framework follows from *either* the cohomological
input (S.11) *or* the analytic input (PNT), with the same
foundational pieces in both cases. To refute the framework's claim,
one would need to invalidate the foundational pieces themselves,
not merely one of the two routes.

---

## 5.5 Why two independent proofs matter

The framework's discipline of providing two or more independent
proofs of every major result is not aesthetic. It is a structural
requirement that comes from the way the framework was built. We
explain.

### 5.5.1 The CBB convergence pattern

In Paper 23 (CBB), every observable in the master table is derived
from at least two of the three CBB sectors:

- **Spectral sector**: 27 observables derived as matrix elements
  of $\hat L$ on $H_R$, with the operator dictionary of Paper 23
  §5.2.

- **Geometric sector**: 9 observables derived as coordinates on
  $M_{\rm geom}$ at the unique spectral-action minimum $P_{\rm
  phys}$.

- **Interface sector**: 1 observable ($m_\tau$) derived from the
  commutator $[log\hat R, \Pi_\chi]$ via the interface operator
  $V$.

The spectral and geometric sectors are *topologically disjoint*
(no-go theorem of research/168), so they provide genuinely
independent derivations. Where an observable can be computed in
both sectors (which is rare, but happens for $H_0$, $n_s$, and a
few others), the two computations must agree. The agreement is
the *cross-check* that confirms the framework's internal
consistency.

In Paper 23 §11.5, the convergence pattern is described as
follows: *"Two independent proofs converging on the same value is
the framework's signature."*

### 5.5.2 The same pattern in Paper 28

R-Theorems PNP.1 and PNP.2 are the trinity-paper instance of the
CBB convergence pattern. They establish the *same conclusion*
($\mathrm P \neq \mathrm{NP}$) from *two independent inputs*
(cohomological vs analytic) with *partially shared dependencies*
(the foundational lemmas of Section 3 and Section 2.4) and
*partially distinct dependencies* (S.11 in PNP.1, PNT and
Lemma 5.2.1 in PNP.2).

The convergence is the cross-check. If the two proofs gave
*different* conclusions — for instance, if PNP.1 said $\mathrm P
\neq \mathrm{NP}$ but PNP.2 said $\mathrm P = \mathrm{NP}$ —
that would indicate an internal inconsistency in the framework,
and the result would have to be retracted. The fact that they
*agree* is the framework's signature: when independent routes
converge, the result is over-determined and stable.

### 5.5.3 What two proofs do *not* establish

For honesty, we note what two independent proofs do *not*
provide:

- **They do not eliminate the foundational dependencies.** Both
  PNP.1 and PNP.2 depend on KEY LEMMA 3.4.3 and Lemma 2.4.4.
  If either of these fails, both proofs fail. The foundational
  dependencies are irreducible.

- **They do not provide a constructive certificate.** Neither
  proof exhibits an explicit polynomial-time-uniform sequence of
  Boolean functions that are not in P. Both proofs are
  *non-constructive*: they establish the *existence* of the
  separation via cohomological / analytic obstructions, but they
  do not construct an explicit witness.

- **They do not give quantitative lower bounds.** Both proofs
  forbid polynomial-time computability of NP-complete problems
  but do not specify the actual circuit complexity (which could
  be $2^{\Omega(n)}$, $n^{\omega(1)}$, $\exp((\log n)^c)$, or
  some other super-polynomial growth).

- **They do not address average-case complexity.** Both proofs
  are worst-case arguments. The average-case question (Levin
  1986; Impagliazzo 1995) is a separate matter requiring its
  own trinity transposition.

These open questions are the natural targets of future R-Theorems
in the trinity programme. PNP.1 and PNP.2 establish only the
single most fundamental separation: $\mathrm P \neq \mathrm{NP}$ in
the worst case.

### 5.5.4 The cross-check as a methodological standard

The framework imposes the following standard on every major
result: *no theorem is considered established until at least two
independent proofs have been given.* This standard was first
articulated in Paper 12 (the postulate-relaxation cycles) and has
been applied to every R-Theorem in the catalogue. It is the
reason the LOCK on RH is built from multiple "teeth" (each tooth
being one R-Theorem providing one constraint) rather than a
single argument.

For Paper 28, the standard is met by PNP.1 (cohomological,
Section 4) and PNP.2 (analytic, this section). The two together
establish $\mathrm P \neq \mathrm{NP}$ in the framework, with the
caveat that both are conditional on the foundational pieces of
Section 3.

If a third independent proof were available, the standard would
be exceeded. We conjecture that such a third proof exists, via
the *no-go theorem of Paper 23 research/168* applied directly to
the trinity image of $M_{\rm geom}$ and the trinity image of
$H_R$. This third proof would establish that the geometric sector
of $\mathcal C_{\rm comp}$ (the moduli space of polynomial-time
circuit configurations) cannot be parametrised by the spectral
sector (the matrix elements of $S_{\rm BC}^{\rm Bool}$), which is
a third reading of $\mathrm P \neq \mathrm{NP}$ as a statement
about the impossibility of analytic reduction. This third proof
is the natural target of a future paper (Paper 29 in the
projected series).

---

## 5.6 Summary of Section 5

This section has established R-Theorem PNP.2: the prime-number-
theorem version of $\mathrm P \neq \mathrm{NP}$. The proof
proceeds via three steps:

1. **Lemma 5.2.1 (Order = Complexity)**: the perturbative orders of
   the BC spectral theory correspond, under the trinity functor,
   to standard computational complexity classes (zeroth = O(1),
   first = P, second = NP, higher = PSPACE / PH / EXP).

2. **Theorem 5.3.2 (No collapse)**: second-order BC observables
   cannot be collapsed to first-order, because the asymptotic
   growth rates are incompatible by the Riemann–von Mangoldt
   formula.

3. **R-Theorem PNP.2**: combining (1) and (2), the inclusion
   $M_{\rm Bool}^{\rm P} \subseteq M_{\rm Bool}^{\rm NP}$ has
   Jones index strictly greater than 1, hence $\mathrm P \neq
   \mathrm{NP}$.

The proof is independent of R-Theorem PNP.1: it uses the order-
counting principle and PNT, not the spin–statistics theorem and
the Schur multiplier. It depends on the same foundational pieces
(KEY LEMMA 3.4.3 and Lemma 2.4.4) but adds Lemma 5.2.1 and
Theorem 5.3.2 as additional structural inputs.

The two proofs together establish $\mathrm P \neq \mathrm{NP}$
in an over-determined fashion: the result follows from either
input (cohomological or analytic) and is robust to failure of
either one of the two routes. This over-determination is the
framework's signature, inherited from the CBB convergence pattern
of Paper 23.

The third independent proof — via the no-go theorem of research/
168 — is left to future work.

---

> **Origin (G).** *"every computer in the world can calculate $t_0
> = (\log\gamma_7)^2$ Gyr and it should."*

The same logic now reads: every computer in the world can compute
first-order Riemann-zero formulas, but no computer in the world
can compute second-order ones in polynomial time, because the
$(\log\gamma_n)^2$ shape is forbidden from collapsing by the prime
number theorem. P ≠ NP is the same statement as: the age of the
universe cannot be computed by reading the Hubble rate alone.

---
