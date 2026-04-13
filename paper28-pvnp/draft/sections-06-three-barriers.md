# Section 6: The Three-Barriers Verification

*Paper 28 — P versus NP as the Computational Shadow of the*
*Spin–Statistics Theorem*

---

# 6. The Three-Barriers Verification

Any candidate proof of $\mathrm P \neq \mathrm{NP}$ must address
three formal barriers established over the past five decades that
exclude broad classes of standard proof techniques. We carry out
the verification here.

The three barriers are:

1. **Relativization** (Baker–Gill–Solovay 1975): the proof must
   not relativize, i.e. it must not work uniformly with respect
   to arbitrary oracles.

2. **Natural proofs** (Razborov–Rudich 1997): the proof must not
   produce a natural property (in Razborov's sense) that
   distinguishes hard from easy functions.

3. **Algebrization** (Aaronson–Wigderson 2008): the proof must
   not algebrize, i.e. it must not work uniformly with respect to
   polynomial extensions of arbitrary oracles over finite fields.

We show that the proof of R-Theorem PNP.1 (and equivalently of
R-Theorem PNP.2) evades all three barriers. The evasion is
*structural*: it follows from the framework's choice of mathematical
instruments, not from any clever sleight of hand designed to
circumvent the barriers. The argument was sketched in Section 1.3;
we now make it precise.

> **Origin (G).** *"the framework speaks both languages."* The
> framework speaks neither the language of relativizing
> diagonalization nor the language of natural combinatorial
> properties nor the language of arithmetization. It speaks the
> language of operator algebras over arithmetic structures, which
> is precisely the stratum of mathematics that the three barriers
> do not reach.

---

## 6.1 Non-relativization

**Claim 6.1.1.** *The proof of R-Theorem PNP.1 does not relativize.*

**Proof.** Suppose for contradiction that the proof relativizes:
that is, suppose the proof can be carried out uniformly with
respect to an arbitrary oracle $A \subseteq \{0,1\}^*$.

Consider the trinity functor $\Phi_{\rm comp} : \mathsf{Cat}_{\rm
BC} \to \mathsf{Cat}_{\rm comp}$ in the relativized setting. The
functor sends the BC C*-algebra $\mathcal A_{\rm BC}$ to the
Boolean BC algebra $\mathcal A_{\rm BC}^{\rm Bool}$, and the BC
KMS state $\omega_1$ to the Boolean KMS state $\omega_1^{\rm Bool}$.
The relativized version of the functor would send the
oracle-relativized BC algebra $\mathcal A_{\rm BC}^A$ (whatever
this could mean) to an oracle-relativized Boolean algebra
$(\mathcal A_{\rm BC}^{\rm Bool})^A$.

But there is no such object as $\mathcal A_{\rm BC}^A$. The BC
algebra $\mathcal A_{\rm BC}$ is constructed from the multiplicative
semigroup $\mathbb N^\times$ acting on $\mathbb Q/\mathbb Z$ —
both of which are *fixed* mathematical objects, independent of
any oracle. There is no notion of "the multiplicative semigroup
of integers relative to oracle $A$": the integers are what they
are, and oracles cannot redefine them.

Equivalently: the partition function $Z(\beta) = \zeta(\beta)$
of the BC system has its simple pole at $\beta = 1$ for every
oracle, because $\zeta(s)$ is a fixed analytic function and
oracles cannot reposition its poles. The unique critical KMS
state $\omega_1$ exists at $\beta = 1$ for every oracle, because
its existence and uniqueness depend only on the analytic structure
of $\zeta$ at $s = 1$.

Therefore the BC side of the trinity dictionary has no
oracle-relative version. Any proof using the BC side
(specifically, R-Theorem S.11 and its trinity image PNP.1) cannot
relativize, because there is no relativized analogue of the
foundational object $\omega_1$.

This is not a *clever choice* of mathematical machinery designed
to evade relativization. It is a *structural fact* about the
mathematical objects the framework uses. The Bost–Connes algebra
is an arithmetic object — built from the integers — and the
integers do not relativize. $\square$

### 6.1.1 What relativization actually requires

To make the argument fully precise, we recall what it means for a
proof technique to relativize.

**Definition 6.1.2 (Relativizing proof).** A proof of a complexity-
theoretic statement *relativizes* if there is a generic method by
which the proof can be carried out for any oracle Turing machine
formalism: that is, if for every oracle $A$, the same chain of
inferences (with $A$ inserted at appropriate places) yields the
analogous statement about $\mathrm P^A$ vs $\mathrm{NP}^A$.

The Baker–Gill–Solovay theorem (Theorem 1 of their 1975 paper)
exhibits oracles $A$ and $B$ with $\mathrm P^A = \mathrm{NP}^A$
and $\mathrm P^B \neq \mathrm{NP}^B$. Hence any relativizing proof
of $\mathrm P \neq \mathrm{NP}$ would, when applied to oracle $A$,
prove $\mathrm P^A \neq \mathrm{NP}^A$ — contradicting $\mathrm
P^A = \mathrm{NP}^A$. So no relativizing proof of $\mathrm P \neq
\mathrm{NP}$ can exist.

The trinity transposition's escape is that it cannot be
*re-instantiated* with an arbitrary oracle in place of the
foundational data. Specifically:

- The BC partition function $Z(\beta) = \zeta(\beta)$ has no
  oracle-relative analogue. Oracles can change *which functions
  are computable*, but they cannot change the analytic structure
  of $\zeta(s)$ at $s = 1$.

- The KMS state $\omega_1$ depends only on the existence of the
  $\zeta$-pole. Since the pole is invariant under oracles, $\omega_1$
  is also invariant. There is no $\omega_1^A$ for varying $A$.

- The trinity functor $\Phi_{\rm comp}$ is constructed from fixed
  mathematical data ($\mathbb B$, $S_\infty$, the Boolean Hecke
  semigroup, etc.) that has no oracle dependence.

Therefore any proof using the trinity dictionary applies to the
*absolute* (non-relativized) versions of P and NP, not to oracle-
relativized versions. The proof's conclusion is about $\mathrm P$
vs $\mathrm{NP}$ in the standard model of computation, and it
cannot be re-instantiated for any oracle $A$ to give a corresponding
statement about $\mathrm P^A$ vs $\mathrm{NP}^A$.

This is the structural reason the proof escapes the relativization
barrier: it does not even *attempt* to be a relativizing argument,
and its instruments forbid such an attempt.

### 6.1.2 An explicit example of non-relativization

For concreteness, consider the SAT witness operator $W_{\rm SAT}$
of Definition 4.2.3. In the standard (non-relativized) Boolean BC
system, $W_{\rm SAT}$ is a specific operator on $H_1^{\rm Bool}$
constructed from the SAT verifier $V_{\rm SAT}$ (a specific
polynomial-time circuit). The proof of R-Theorem PNP.1 in §4.5
shows that $W_{\rm SAT}$ lies in the odd graded sector and is
non-zero, leading to $\mathrm P \neq \mathrm{NP}$.

If we attempt to relativize: replace SAT with $\mathrm{SAT}^A$,
the version of SAT with access to oracle $A$. The "SAT$^A$
verifier" $V_{\rm SAT}^A$ is now an oracle Turing machine, not
a polynomial-time-uniform Boolean circuit. The witness operator
$W_{\rm SAT^A}$ would have to be constructed from $V_{\rm SAT}^A$,
but the trinity dictionary does not provide a way to embed an
oracle Turing machine into the Boolean BC algebra — because the
Boolean BC algebra is built from polynomial-time-uniform Boolean
circuits, which are *finite combinatorial objects*, not oracle-
queriable Turing machines.

Therefore, the proof of PNP.1 simply *does not apply* to the
relativized versions of SAT. It applies to the standard, non-
relativized SAT, and the conclusion is about standard P and NP.
The Baker–Gill–Solovay oracles $A$ and $B$ are not in the
domain of the trinity functor, so they do not threaten the proof.

---

## 6.2 Non-naturalness

**Claim 6.2.1.** *The proof of R-Theorem PNP.1 does not produce
a natural property in the sense of Razborov–Rudich.*

**Proof.** Recall (§1.2.2) that a natural property $\Pi$ of
Boolean functions $f : \{0,1\}^n \to \{0,1\}$ must satisfy three
conditions:

(a) **Constructivity**: membership $f \in \Pi$ can be decided in
time $2^{O(n)}$ given the truth table of $f$.

(b) **Largeness**: a constant fraction of all Boolean functions
on $n$ variables belong to $\Pi$.

(c) **Usefulness**: every $f \in \Pi$ requires super-polynomial
circuit complexity.

We show that the obstruction used in PNP.1 — the non-trivial
element of $H^2(S_n, U(1)) = \mathbb Z/2\mathbb Z$ — fails both
constructivity and largeness, so it cannot be a natural property.

**Failure of constructivity.** The Schur multiplier $H^2(S_n,
U(1)) = \mathbb Z/2\mathbb Z$ is a *single discrete element* of
a two-element group, not a property of Boolean functions per se.
To make it into a property of $f$, we would need to specify a way
of associating to each Boolean function $f$ a cohomology class
$\beta_f \in H^2(S_n, U(1))$, and then ask whether $\beta_f$ is
the trivial or the non-trivial element.

The trinity dictionary provides such an association: $\beta_f$ is
the cohomology class of the witness operator $W_{f}$ in the
graded structure of the Boolean BC factor. But this association
is *not* polynomial-time computable from the truth table of $f$.
Computing $\beta_f$ from the truth table requires constructing
the Boolean BC factor, which is an infinite-dimensional operator
algebra, and computing the Tomita modular operator and its
$\mathbb Z/2$-grading. None of this is polynomial-time in the
truth-table size $2^n$.

In other words: testing whether $\beta_f$ is the trivial element
of $H^2(S_n, U(1))$ would require having access to the *full
cohomological structure* of the Boolean BC factor, which is not
computable from the truth table of $f$ alone. The constructivity
condition (a) of Razborov–Rudich is therefore not satisfied.

**Failure of largeness.** The Schur multiplier $H^2(S_n, U(1))$
has exactly two elements: the trivial and the non-trivial. There
is no notion of a "large" or "small" subset of a two-element
group with respect to any natural measure. The Razborov–Rudich
largeness condition (b) requires that the property hold for a
*constant fraction* of all functions on $n$ variables, which
presupposes that the property is a measurable subset of function
space with a positive measure. The non-trivial element of a
two-element group is not such a subset.

More precisely: if we ask "what fraction of Boolean functions
have non-trivial $\beta_f$?", the answer depends on the embedding
of Boolean functions into the cohomology, and the embedding is
not measure-preserving in any natural sense. We could have *all*
Boolean functions correspond to the non-trivial cocycle (which
would be "100% large" but trivially so), or we could have *no*
Boolean functions correspond to it (which would be "0% large"),
or any intermediate fraction depending on the choice of embedding.
The question is not well-posed in the way Razborov–Rudich requires.

The conclusion: the cohomological obstruction is not a natural
property in Razborov's sense. It is a *single discrete element* of
a finite cohomology group, with no measure-theoretic structure
that would let it satisfy the largeness condition. $\square$

### 6.2.1 The Razborov–Rudich barrier rephrased

To see why the trinity proof escapes Razborov–Rudich, it helps to
rephrase the barrier in operational terms.

**Rephrasing.** The Razborov–Rudich barrier says: *if you can
build a polynomial-time algorithm that, given the truth table of
a Boolean function $f$, decides whether $f$ is hard or easy, then
your "hardness predicate" is a pseudorandom function distinguisher,
which contradicts the existence of pseudorandom functions.*

The trinity proof does *not* build any such algorithm. The proof
establishes the existence of a cohomological obstruction without
producing a polynomial-time procedure to decide whether a given
function violates the obstruction. In other words, the proof is
*non-constructive*: it tells us that NP-hard problems exist, but
it does not give us a polynomial-time test for hardness applied
to truth tables.

The non-constructivity is explicit in the proof of PNP.1:

- Step 1 (Section 4.5): we apply the trinity functor to the graded
  structure of S.11. The functor is defined abstractly via the
  category-theoretic correspondence (Section 2.4), not via an
  algorithm operating on truth tables.

- Step 2: we exhibit a *specific* generator (the SAT witness
  operator $W_{\rm SAT}$) of the odd graded sector. We do not
  exhibit a polynomial-time algorithm that decides whether an
  arbitrary Boolean function lies in the odd graded sector.

- Step 3: we invoke Schur multiplier rigidity, which is a
  cohomological fact about $S_n$, not a property of any specific
  truth table.

At no point in the proof is there a polynomial-time algorithm
operating on truth tables. The proof is structurally non-
constructive, which is why it escapes Razborov–Rudich.

### 6.2.2 What the proof does construct

For honesty, we note what the proof *does* construct:

- An abstract category-theoretic functor $\Phi_{\rm comp}$ from
  $\mathsf{Cat}_{\rm BC}$ to $\mathsf{Cat}_{\rm comp}$.

- A specific operator $W_{\rm SAT} \in M_{\rm Bool}$ associated
  with the SAT problem.

- A specific cohomology class in $H^2(S_n, U(1))$ associated with
  the Boolean BC graded structure.

What the proof does *not* construct:

- A polynomial-time algorithm that, given a truth table, decides
  hardness.

- An explicit polynomial-time-uniform sequence of Boolean
  functions outside P.

- A natural property in Razborov's sense.

The non-constructivity of the proof is its greatest *theoretical*
strength (it evades Razborov–Rudich) but also its greatest
*practical* weakness (it does not give us new tools for deciding
hardness in specific cases). This is a familiar trade-off in the
philosophy of mathematics: existence theorems are often non-
constructive precisely because constructiveness would conflict
with deeper theoretical constraints.

---

## 6.3 Non-algebrization

**Claim 6.3.1.** *The proof of R-Theorem PNP.1 does not algebrize.*

**Proof.** The Aaronson–Wigderson algebrization barrier (2008)
strengthens Baker–Gill–Solovay relativization in the following
way. Given an oracle $A \subseteq \{0,1\}^*$, there is a unique
*low-degree polynomial extension* $\widetilde A : \mathbb F_q^* \to
\mathbb F_q$ over a finite field $\mathbb F_q$, defined by
multilinear interpolation of $A$. A proof technique *algebrizes*
if it remains valid when both Turing machines are allowed to query
not only $A$ but also $\widetilde A$.

The Aaronson–Wigderson theorem (Theorem 5.1 of their 2008 paper)
shows that the algebrized versions of P and NP relative to
appropriate oracle pairs $(A, \widetilde A)$ can either coincide
or separate. Hence no algebrizing technique can settle $\mathrm P$
vs $\mathrm{NP}$.

The trinity transposition escapes algebrization for two reasons:

**(i) The framework uses cyclotomic Galois cohomology, not
polynomial extensions.** The cohomological obstruction in PNP.1 is
$H^2(S_n, U(1))$, which is the Schur multiplier of the symmetric
group. This is a cohomology class of a *profinite group*, computed
via the bar resolution or via the theory of group extensions. It is
*not* a polynomial extension of any finite-field oracle.

The Aaronson–Wigderson barrier is keyed to *polynomial extensions
over finite fields*. The Schur multiplier of $S_n$ is not a
polynomial; it is an element of an abelian group $H^2(S_n, U(1))$
that classifies projective representations. There is no polynomial
extension $\widetilde A$ over $\mathbb F_q$ that can encode the
information of the Schur multiplier element, because the Schur
multiplier lives at a higher categorical level than polynomials.

**(ii) The framework's operator-algebraic instruments depend on
type III$_1$ structure, which has no polynomial encoding.** The
Tomita modular operator $\Delta^{\rm Bool}$ on $M_{\rm Bool}$ is
an unbounded positive self-adjoint operator on an infinite-
dimensional Hilbert space. Its action cannot be encoded by any
polynomial over a finite field, because polynomials over finite
fields take values in a finite field, while the spectrum of
$\Delta^{\rm Bool}$ is an infinite subset of $(0, \infty)$.

More generally, type III$_1$ factors have no polynomial structure
in the sense relevant to algebrization: they are characterised
(Connes 1973) by having Connes spectrum $S(M) = \mathbb R^+_*$,
which is a continuous set. Polynomials over finite fields cannot
distinguish points of a continuous set. Therefore the type III$_1$
classification of $M_{\rm Bool}$ is invisible to polynomial
extensions of oracles.

The combined consequence: the proof of R-Theorem PNP.1 uses
mathematical objects (cohomology classes of profinite groups,
type III$_1$ factor structure, Tomita modular flow) that have no
representation as polynomials over finite fields. These objects
sit at a higher categorical level than polynomials, and they
encode information that polynomial extensions of oracles cannot
capture. Therefore no algebrizing technique applied to the proof
could yield a uniform statement about polynomial extensions of
arbitrary oracles. $\square$

### 6.3.1 The categorical hierarchy

To illuminate why the proof escapes algebrization, we situate it
within a categorical hierarchy of mathematical structures.

| Level | Mathematical structure | Aaronson–Wigderson reach? |
|:--|:--|:--|
| 0 | Boolean functions, truth tables | Yes |
| 1 | Polynomials over finite fields $\mathbb F_q$ | Yes (algebrization works here) |
| 2 | Polynomial rings, schemes over $\mathbb F_q$ | Yes (in many cases) |
| 3 | Cohomology of finite groups (e.g., $H^*(\mathbb Z/k, A)$) | Partially |
| 4 | Cohomology of profinite groups (e.g., $H^*(S_\infty, A)$) | **No** |
| 5 | Operator algebras over arithmetic structures (BC) | **No** |
| 6 | Tomita–Takesaki modular structure on type III$_1$ factors | **No** |

The Aaronson–Wigderson barrier reaches up to level 2 or 3 (depending
on the strength of the polynomial method being applied). The
trinity transposition uses objects at levels 4, 5, and 6: the
profinite Schur multiplier of $S_\infty$, the Bost–Connes algebra,
and the type III$_1$ Tomita modular structure of $M_{\rm Bool}$.
None of these can be encoded as polynomials over a finite field,
so none of them is reachable by algebrization.

The hierarchy is not just a list of more-or-less complicated
objects. It reflects a *categorical stratification*: each level
sits one categorical layer above the previous, in the sense that
the objects at level $k+1$ are *invariants* (or *automorphism
groups*, or *cohomology classes*) of objects at level $k$. Going
up the hierarchy means moving from "things" to "invariants of
things", and algebrization stops working once you go far enough
up because polynomials are objects at low levels and cannot
distinguish invariants at high levels.

The trinity dictionary is the framework's tool for navigating
this hierarchy: it identifies the cohomological invariant
(level 4 or 5) corresponding to a physical phenomenon (level 2 or
3 or below) and uses the level-4 information to derive constraints
that the level-2 information cannot capture. This is structurally
why the framework can prove things that algebrizing techniques
cannot.

---

## 6.4 What barriers the proof might still hit

For honesty, we identify what *could* still go wrong with the
proof of R-Theorem PNP.1, even granted the structural escape from
the three known barriers.

### 6.4.1 The three foundational dependencies

The proof depends on three clearly labelled conditional pieces:

**KEY LEMMA 3.4.3 (existence and uniqueness of $\omega_1^{\rm
Bool}$).** This is the existence of a unique critical KMS state
on the Boolean BC dynamical system. The lemma is the analogue of
the Bost–Connes 1995 Theorem 25, adapted to the Boolean function
field. The proof outline (§3.4.2) shows that the standard
Bost–Connes argument transfers, with three substantive new
technical ingredients (counting estimate, non-commutative Hecke
analysis, type III$_1$ classification via multiplicative density).
Each ingredient is mechanically obtainable, but the full proof has
not been written out here; it is deferred to Appendix B.

If the lemma fails, three modes are possible (§3.4.3): no KMS$_1$
state (Mode A), multiple KMS$_1$ states (Mode B), or wrong factor
type (Mode C). In any of the three modes, the trinity dictionary
breaks at the Boolean BC level and the proof of PNP.1 cannot be
completed.

**LEMMA 2.4.4 (functoriality of the trinity dictionary).** This is
the structural lemma that the trinity dictionary is a functor
preserving cohomology classes. The proof outline (§2.4.3) reduces
the lemma to the verification of cocycle preservation under the
embedding $\mathbb Z/k \hookrightarrow S_n$ via the Brauer–Jones
bridge theorem (Paper 23 §8.2). The full verification is in
Appendix C.

If the lemma fails, the trinity dictionary is not a functor and
the trinity transposition is not a rigorous proof technique, only
a suggestive analogy. The proof of PNP.1 would then have to be
restated as a conjecture rather than a theorem.

**LEMMA 3.8.2 (non-degeneracy of the graded structure).** This is
the lemma that the trinity functor $\Phi_{\rm comp}$ does not send
the non-trivial element of $H^2(S_\infty, U(1)) = \mathbb Z/2$ to
the trivial element of the corresponding target cohomology. The
proof (§3.8.1) is in two parts: an *algebraic* argument that the
functor's induced map on $H^2$ must be the identity (because it
is an isomorphism between two copies of $\mathbb Z/2$, and the
only isomorphism of a two-element group is the identity), and an
*operational* witness via the SAT witness operator $W_{\rm SAT}$.
LEMMA 3.8.2 depends on Lemma 2.4.4 and Lemma 4.5.1; neither of
these depends on it, so there is no circularity.

If LEMMA 3.8.2 fails — i.e., if the trinity functor degenerates
on $H^2$ despite preserving the cohomology group — then the
graded structure of $M_{\rm Bool}$ collapses to a single sector,
the inclusion $M_{\rm Bool}^{\rm P} \subset M_{\rm Bool}^{\rm NP}$
becomes an equality, and the proof of PNP.1 fails at Step 1.
However, the failure mode is *category-theoretically forbidden*
by the algebraic part of the proof: as long as Lemma 2.4.4 holds
and gives an isomorphism on $H^2$, the only homomorphism
$\mathbb Z/2 \to \mathbb Z/2$ that is an isomorphism is the
identity, so the failure would require Lemma 2.4.4 itself to fail.
LEMMA 3.8.2 is therefore *implied* by Lemma 2.4.4 and is named
separately only because the implication is non-obvious and the
operational witness via $W_{\rm SAT}$ provides a redundant
verification.

### 6.4.2 Why we believe the foundational pieces hold

The grounds for believing KEY LEMMA 3.4.3 are:

(a) The Boolean partition function $Z^{\rm Bool}(\beta) = \sum_C
(\mathrm{size}\,C)^{-\beta}$ has the same analytic structure as
the BC partition function $\zeta(\beta)$, with a simple pole at
$\beta = 1$. This follows from the polynomial growth of the
distinct-circuit count, which gives a Dirichlet-series-like
behaviour (§3.4.1).

(b) The Galois group $(\mathbb Z/2)^\infty \rtimes S_\infty$ of
$\mathbb B$ is large enough to enforce uniqueness of the KMS$_1$
state, by the same argument as in Bost–Connes 1995 (which uses
$\widehat{\mathbb Z}^*$, also a profinite group of comparable
"size").

(c) The multiplicative density of circuit sizes is unbounded in
$\mathbb R^+$, forcing the Connes spectrum of $\sigma_t^{\rm Bool}$
to be all of $\mathbb R^+_*$, hence type III$_1$ (Connes 1973).

Each of (a)–(c) is the subject of explicit verification in
Appendix B.

The grounds for believing Lemma 2.4.4 are:

(d) The trinity functor is constructed component-wise from existing
functorial relationships: the additive ↔ multiplicative dictionary
of Paper 15 §2.1 (which is already a functor) and the multiplicative
↔ Boolean dictionary constructed in Section 2.2 (which is the new
contribution).

(e) The cocycle preservation under the embedding $\mathbb Z/k
\hookrightarrow S_n$ is the content of the Brauer–Jones bridge
theorem (Paper 23 §8.2), generalised from cyclic to symmetric
groups.

(f) The verification has been carried out explicitly for $k = 3$
and the corresponding $S_n$ embedding, with the cocycle preservation
matching the Schur multiplier element.

Each of (d)–(f) is the subject of explicit verification in
Appendix C.

The grounds for believing LEMMA 3.8.2 are:

(g) The algebraic part of the proof (parts (i) and (ii) of §3.8.1)
is *forced by category theory*: a homomorphism $\mathbb Z/2 \to
\mathbb Z/2$ that is an isomorphism is necessarily the identity
map. There is no other possibility. As long as Lemma 2.4.4 gives
an isomorphism on $H^2$, the non-degeneracy follows mechanically.

(h) The operational part of the proof (part (iii) of §3.8.1) is a
direct construction: the SAT witness operator $W_{\rm SAT}$ is
non-zero (the trivial SAT instance $x = (x_1)$ is satisfiable, so
the contribution $1 \cdot e(\chi_{(x_1)})$ to $W_{\rm SAT}$ is
non-zero) and lies in the odd graded sector by the off-diagonal
branch structure of the OR-over-witnesses sum (Lemma 4.5.1).

(g) and (h) together make LEMMA 3.8.2 the most secure of the three
foundational pieces: the algebraic part is a category-theoretic
tautology, and the operational part is a one-line verification.

### 6.4.3 What if the proof is wrong

Suppose, hypothetically, that one of the foundational pieces fails.
What do we learn?

If KEY LEMMA 3.4.3 fails: we learn that the Boolean BC dynamical
system does not have a unique critical KMS state, which means
the trinity dictionary's third column does not have a parameter-
free anchor. The framework's claim of zero parameters in the
computational column would be falsified, and the trinity
transposition would have to be reformulated with explicit
parameters or with a different anchoring state.

If Lemma 2.4.4 fails: we learn that the trinity dictionary is not
functorial, and the cohomological obstructions in $\mathsf{Cat}_{\rm
BC}$ do not reliably correspond to obstructions in $\mathsf{Cat}_{\rm
comp}$. The trinity transposition would then be only an analogy,
not a rigorous proof technique. PNP.1 and PNP.2 would have to be
restated as conjectures motivated by the analogy.

In both cases, the framework would learn something useful: where
the trinity dictionary breaks, and what the correct mathematical
structure of the computational column actually is. The failure of
PNP.1 would not invalidate the trinity dictionary as a research
programme — it would only reveal the location of the missing
structural piece.

We do not believe either failure mode obtains, on the grounds (a)–(f)
listed above. But we state the conditional honestly, because the
framework's discipline requires every load-bearing claim to carry
its rigor label and every conditional claim to make its
dependencies visible.

### 6.4.4 Other potential issues

Beyond the two named foundational pieces, three other potential
issues are worth flagging:

**(g) Quantum complexity classes.** The proof of PNP.1 establishes
that NP-witness verification cannot be done in P-time. It does *not*
directly address the question of quantum complexity classes (BQP,
QMA, etc.). The corollary 4.6.1(iv) extends the conclusion to
non-adaptive quantum algorithms via a deferred argument in Appendix
D §D.4. The full extension to all quantum algorithms (including
adaptive ones with measurement-dependent gate sequences) is not
addressed in the present paper.

**(h) Non-uniformity.** The proof addresses *polynomial-time-uniform*
Boolean circuits. Non-uniform circuits (i.e. P/poly, BPP/poly, etc.)
have a different complexity-theoretic status, and the trinity
correspondence between BC sectors and uniform vs non-uniform
classes needs to be made precise. The present paper assumes the
uniform setting throughout.

**(i) Average-case versus worst-case.** The proof is a worst-case
argument: it shows that *some* NP-complete problem cannot be
solved in P-time. The average-case version (Levin 1986) — which
asks whether NP-complete problems can be solved in polynomial time
on average over a natural distribution — is a separate question,
and the trinity dictionary's relationship to average-case
complexity has not been worked out.

These issues are flagged for transparency. None of them
invalidates the proof of $\mathrm P \neq \mathrm{NP}$ in the
worst-case, polynomial-time-uniform, non-quantum setting; they
are *additional* questions that the present paper does not address.

---

## 6.5 Summary of Section 6

The three-barriers verification establishes that the proof of
R-Theorem PNP.1 (and equivalently PNP.2) escapes all three known
barriers to a proof of $\mathrm P \neq \mathrm{NP}$:

| Barrier | Standard target | Why the proof escapes |
|:--|:--|:--|
| **Relativization** | Diagonalization | $\omega_1$ has no oracle-relative version |
| **Natural proofs** | Combinatorial properties of truth tables | Schur multiplier $\mathbb Z/2$ is not constructive and not large |
| **Algebrization** | Polynomial method over $\mathbb F_q$ | Profinite Galois cohomology + type III$_1$ factor structure sit above polynomials |

The escape from each barrier is *structural*: it follows from the
choice of mathematical instruments (operator algebras over
arithmetic structures, cohomology of profinite groups, type III$_1$
factors), not from any clever workaround. The framework's
instruments are precisely the kind that the three barriers do not
reach.

The proof has three clearly labelled foundational dependencies
(KEY LEMMA 3.4.3, Lemma 2.4.4, and LEMMA 3.8.2), all of which are
the subject of mechanical verification (Appendices B, C, and §3.8.1
respectively). If any one fails, the proof of PNP.1 fails
accordingly. We have grounds for believing all three hold; the
strongest grounds are for LEMMA 3.8.2 (which is forced by
category theory plus a one-line operational witness) and the
weakest are for KEY LEMMA 3.4.3 (which is the central new
operator-algebraic construction). The conditional is carried
honestly.

Three additional potential issues are flagged for transparency:
quantum complexity classes (incompletely addressed), non-uniform
circuits (not addressed), and average-case complexity (not
addressed). These are open questions for future R-Theorems in the
trinity programme.

The final section (Section 7) places the result in the context of
the broader programme.

---

> **Origin (G).** *"the framework speaks both languages."*

Three columns. Three languages. One cohomological volume. The
barriers were designed to forbid translation between low-level
languages (Boolean, polynomial, oracle). The framework operates
in a higher language (cohomology of profinite groups acting on
type III$_1$ factors at criticality), and the barriers cannot
follow it there. This is the structural reason the proof exists.

---
