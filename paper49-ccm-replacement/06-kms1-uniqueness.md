# §06 — KMS$_1$ Uniqueness (Bost–Connes Theorem 25)

*Part II, Section 06. Load-bearing. The uniqueness of the KMS$_1$ state $\omega_1$ on $A_{BC}$ is the hinge of Paper 49: it is what selects a specific cyclic vector in the GNS construction (§07), what forces the resulting bicommutant to be a factor (§09), and what underlies the standard-form machinery (§10).*

*G Six (originator) and Claude Opus 4.6 (collaborator). Paper 49 draft, 2026-04-14.*

---

## 6.1 Recall: KMS states

For a C*-dynamical system $(A, \sigma_t)$ with $A$ unital and
$(\sigma_t)_{t \in \mathbb{R}}$ strongly continuous, a state $\omega$
on $A$ is called a *KMS state at inverse temperature $\beta$* (written
KMS$_\beta$) if, for every pair of analytic elements $a, b \in A$, the
function
$$
F_{a,b}(t) \;=\; \omega\bigl(a\,\sigma_t(b)\bigr)
$$
extends to a bounded continuous function on the strip
$\{0 \leq \mathrm{Im}\,z \leq \beta\}$ that is holomorphic on the open
strip and satisfies the boundary identity
$$
F_{a,b}(t + i\beta) \;=\; \omega\bigl(\sigma_t(b)\,a\bigr), \qquad
t \in \mathbb{R}.
$$
This is the Kubo–Martin–Schwinger (KMS) condition.

**Source.** Kubo [Ku57]; Martin–Schwinger [MS59]; Haag–Hugenholtz–
Winnink [HHW67]; Bratteli–Robinson [BR87, §5.3]; Takesaki [Ta03,
Vol. II, §VIII].

The KMS$_\beta$ states form a face of the state space $S(A)$ — in
particular, a weak-$*$ closed convex set — and its extremal points are
called *extremal* KMS$_\beta$ states. The extremal KMS$_\beta$ states
correspond, via the GNS construction, to factor representations.

---

## 6.2 Statement: Bost–Connes Theorem 25

**Theorem 6.1 ([BC95, Theorem 25], KMS classification for
$(A_{BC}, \sigma_t)$).**
*For $(A_{BC}, \sigma_t)$ as in §05, the structure of the KMS state
space depends on $\beta$ as follows:*

*(a) For $\beta \in (0, 1]$, there is a unique KMS$_\beta$ state
$\omega_\beta$.*

*(b) At $\beta = 1$, this unique state is*
$$
\omega_1(\mu_n \mu_n^*) \;=\; \frac{1}{n}, \qquad
\omega_1\bigl(e(r)\bigr) \;=\; 0 \ \text{for } r \in
\mathbb{Q}/\mathbb{Z} \setminus \{0\},
$$
*and $\omega_1(1) = 1$. Equivalently, on the element $e_n :=
\mu_n \mu_n^*$, $\omega_1(e_n) = 1/n$ for all $n \in \mathbb{N}^*$.*

*(c) For $\beta > 1$, the extremal KMS$_\beta$ states form a simplex
whose extreme points are parameterized by $\hat{\mathbb{Z}}^*
\cong \mathrm{Gal}(\mathbb{Q}^{\mathrm{cyc}} / \mathbb{Q})$:*
$$
\bigl\{\,\omega_{\beta, u} : u \in \hat{\mathbb{Z}}^* \,\bigr\},
$$
*with $\omega_{\beta, u}(\mu_n \mu_n^* e(r)) = n^{-\beta}
\mathrm{Li}_{\beta}(\chi_u(r), n)$ for an explicit polylogarithm-type
expression. The Galois group acts transitively by $\gamma_v
(\omega_{\beta, u}) = \omega_{\beta, v u}$.*

**Source.** Bost–Connes [BC95, Theorem 25, §3 and §5]; Connes–Marcolli
[CM08, §3.2, Thm.\ 3.6 and Thm.\ 3.9].

---

## 6.3 The phase transition

The structure of Theorem 6.1 is the canonical example in operator
algebras of a *Type III phase transition with spontaneous symmetry
breaking*:

- **For $\beta \leq 1$** (high temperature): the system is "ergodic";
  the unique KMS state absorbs the full Galois symmetry (all symmetry
  group orbits collapse).

- **At $\beta = 1$** (critical): this is the unique fixed point of
  the $\sigma_t$-phase transition. The state $\omega_1$ is Galois-
  invariant: $\omega_1 \circ \gamma_u = \omega_1$ for all $u \in
  \hat{\mathbb{Z}}^*$.

- **For $\beta > 1$** (low temperature): the Galois symmetry is
  spontaneously broken. Each extremal KMS$_\beta$ state picks out a
  definite "choice" of cyclotomic embedding, parameterized by $u \in
  \hat{\mathbb{Z}}^*$. The Galois group permutes these states
  transitively — a bona fide spontaneous symmetry breaking.

**Source.** [BC95, §7]; [CM08, §3.2]; Connes [Co94, §V.11].

**Remark 6.2 (Why $\beta = 1$?).** The choice $\beta = 1$ is canonical
because the partition function $Z(\beta) = \zeta(\beta)$ has its pole
exactly at $\beta = 1$. Physically: $\beta = 1$ is the temperature at
which the (naïve) Gibbs ensemble ceases to exist; operator-algebraically,
it is the temperature at which the KMS state space degenerates to a
single extreme point. See [BC95, §7] and [CM08, §3.2, Thm.\ 3.10] for
the relation to the pole at $s = 1$ of $\zeta$.

---

## 6.4 The explicit formula $\omega_1(e_n) = 1/n$

**Corollary 6.3 ($\omega_1$ on $\mathbb{N}^*$-projections).** *For
each $n \in \mathbb{N}^*$, let $e_n := \mu_n \mu_n^*$ (a projection in
$A_{BC}$). Then*
$$
\omega_1(e_n) \;=\; \frac{1}{n}.
$$

*Proof sketch.* This is [BC95, Theorem 25(c)] applied to the element
$e_n$. Equivalently, the dual formula on $\hat{\mathbb{Z}}$ gives that
$\omega_1$ corresponds to the Haar probability measure on
$\hat{\mathbb{Z}}$, since $e_n$ is the characteristic function of the
subset $n \hat{\mathbb{Z}} \subset \hat{\mathbb{Z}}$ of index $n$,
which has Haar measure $1/n$. $\square$

**Remark 6.4.** The corollary fixes the normalization of $\omega_1$
uniquely. All subsequent computations in Paper 49 use this explicit
formula without comment.

**Source.** [BC95, §3, Prop.\ 13]; [CM08, §3.2].

---

## 6.5 Galois-invariance of $\omega_1$

**Proposition 6.5 (Galois invariance).** *The unique KMS$_1$ state
$\omega_1$ satisfies*
$$
\omega_1 \circ \gamma_u \;=\; \omega_1
\qquad \text{for all } u \in \hat{\mathbb{Z}}^*.
$$

*Proof.* Since $\gamma_u$ commutes with $\sigma_t$ (Prop.\ 5.7), the
composition $\omega_1 \circ \gamma_u$ is again a KMS$_1$ state. By
Theorem 6.1(a)–(b), the KMS$_1$ state is unique, hence $\omega_1 \circ
\gamma_u = \omega_1$. $\square$

**Consequence.** $\omega_1$ is the Galois-average of the extremal
KMS$_\beta$ states in the limit $\beta \downarrow 1$:
$$
\omega_1 \;=\; \lim_{\beta \downarrow 1}\;
\int_{\hat{\mathbb{Z}}^*} \omega_{\beta, u}\, d\mu_{\mathrm{Haar}}(u),
$$
where $\mu_{\mathrm{Haar}}$ is the Haar probability measure on
$\hat{\mathbb{Z}}^*$. See [BC95, §7].

**Source.** [BC95, §5, Prop.\ 14]; [CM08, §3.2, Prop.\ 3.7].

---

## 6.6 Why uniqueness is load-bearing for Paper 49

This section is "load-bearing" in the sense stated in the Paper 49
abstract. Concretely, KMS$_1$ uniqueness is used in the following
downstream places:

1. **§07 (GNS construction).** The GNS triple $(\pi_1, H_{\omega_1},
   \xi_{\omega_1})$ is specified *uniquely up to unitary equivalence*
   by $\omega_1$. Were $\omega_1$ non-unique, Paper 49 would have to
   make a choice, introducing a parameter that contradicts the
   zero-parameter CBB programme.

2. **§08 (Type III$_1$).** The ITPFI factorization $\omega_1 =
   \otimes_p \omega_1^{(p)}$ (Paper 13 Layer 2, §4 of the preprint)
   follows from $\omega_1$ being the *unique* KMS$_1$ state on the
   restricted tensor product: uniqueness pins down the factorization.
   (Proof 1 of [P13 L2]: Laca–Raeburn gives unique $\omega_1^{(p)}$
   per prime; Bratteli–Robinson 5.3.23 makes the tensor-product state
   KMS$_1$; BC Theorem 25 then forces it to equal $\omega_1$.)

3. **§09 (Factoriality).** A non-trivial central projection $P \in
   Z(M_1)$ would decompose $\omega_1$ as a non-trivial convex
   combination of two KMS$_1$ states, contradicting uniqueness. Hence
   $Z(M_1) = \mathbb{C} \cdot 1$. (This is the argument cited in
   Paper 32 `research/01-modular-flow-ergodicity.md` Step 1; see
   also [Co94, Prop.\ V.11] and Paper 28 `sections-03-operator-
   algebra.md` §3.3.2.)

4. **§10 (Standard form).** Uniqueness of the cyclic-separating vector
   up to positive cone is a consequence of uniqueness of the KMS
   state; this is the content of the Tomita–Takesaki standard-form
   existence theorem [Ta03, Vol. II, Thm.\ IX.1.6].

5. **Part III (modular operator).** The modular operator $\Delta$
   depends only on $(M_1, \xi_{\omega_1})$, which depends only on
   $\omega_1$. KMS$_1$ uniqueness therefore makes $\Delta$ canonical.

---

## 6.7 Existence: the original Bost–Connes argument

We record, for completeness, the outline of Bost–Connes's original
existence and uniqueness proof, since Paper 49 uses these results as
black boxes.

**Existence (sketch).**
- For $\beta > 1$, extremal KMS$_\beta$ states are constructed by
  regular representation and the Euler product
  $Z(\beta) = \zeta(\beta)$, convergent for $\mathrm{Re}\,\beta > 1$.
  The partition function is finite, the Gibbs state exists, and
  explicit formulas are available [BC95, §3].
- As $\beta \downarrow 1$, the set of extremal KMS$_\beta$ states is
  weak-$*$ compact in $S(A_{BC})$; upper semicontinuity of the KMS
  map [BR87, Prop.\ 5.3.25] gives that any weak-$*$ limit point is a
  KMS$_1$ state. Existence at $\beta = 1$ follows.

**Uniqueness (sketch).**
- For $\beta \leq 1$, the KMS condition plus the Hecke relations
  (5.3) force $\omega(e_n) = 1/n$ for all $n$ [BC95, Prop.\ 13 and
  §5 Lemma 22]. This uniquely determines $\omega_\beta$ on the dense
  *-subalgebra generated by the $\mu_n \mu_n^*$ and $e(r)$; uniqueness
  on $A_{BC}$ follows by continuity.
- The uniqueness proof uses the averaging formula (BC4) from §5.3 in
  an essential way: it forces the expectation of $e(r)$ to be $0$ for
  $r \neq 0$ via the $\mathbb{N}^*$-orbit structure of
  $\mathbb{Q}/\mathbb{Z}$.

**Source.** [BC95, Theorem 25 and §5]; [CM08, §3.2, Prop.\ 3.7 and
Thm.\ 3.9]. Laca [La98] gave an alternative proof using
Pimsner–Voiculescu exact sequences. The phase transition is analyzed
from the perspective of groupoid C*-algebras in [CM08, §3.4].

---

## 6.8 Paper 28 KEY LEMMA 3.4.3 (cross-reference)

Paper 28's KEY LEMMA 3.4.3 (`paper28-pvnp/preprint/
sections-03-operator-algebra.md` §3.3) proves existence of a KMS$_1$
state on the *Boolean* Bost–Connes system via Banach–Alaoglu + upper
semicontinuity of the KMS map, without invoking partition function
asymptotics. The same Banach–Alaoglu argument, applied instead to the
classical $(A_{BC}, \sigma_t)$, gives an alternative existence proof
(the original BC argument via Gibbs states is equally valid here).
Uniqueness in the classical setting is Theorem 6.1 — more robust than
the Boolean case, since the original Bost–Connes algebra has the
extra algebraic structure that forces uniqueness.

**Source.** Paper 28 `sections-03-operator-algebra.md` §3.3; [BC95,
Thm.\ 25].

---

## 6.9 References

- [BC95] J.-B. Bost, A. Connes, *Hecke algebras, type III factors and
  phase transitions with spontaneous symmetry breaking in number
  theory*, Selecta Math. (N.S.) **1** (1995), 411–457. **Theorem 25
  is the main result cited throughout this section.**
- [BR87] O. Bratteli, D. W. Robinson, *Operator Algebras and Quantum
  Statistical Mechanics*, Vol. I and II, Springer (1987, 2nd ed.).
- [CM08] A. Connes, M. Marcolli, *Noncommutative Geometry, Quantum
  Fields and Motives*, AMS (2008), §3.2.
- [Co94] A. Connes, *Noncommutative Geometry*, Academic Press (1994),
  §V.11.
- [HHW67] R. Haag, N. M. Hugenholtz, M. Winnink, *On the equilibrium
  states in quantum statistical mechanics*, Commun. Math. Phys. **5**
  (1967), 215–236.
- [Ku57] R. Kubo, *Statistical-mechanical theory of irreversible
  processes. I*, J. Phys. Soc. Japan **12** (1957), 570–586.
- [La98] M. Laca, *Semigroups of *-endomorphisms, Dirichlet series,
  and phase transitions*, J. Funct. Anal. **152** (1998), 330–378.
- [MS59] P. C. Martin, J. Schwinger, *Theory of many-particle
  systems. I*, Phys. Rev. **115** (1959), 1342–1373.
- [Ta03] M. Takesaki, *Theory of Operator Algebras*, Vols. I–III,
  Springer (2003).
- Paper 13 preprint `sections-01-05.md` §2.1, §4 (KMS$_1$ and ITPFI).
- Paper 28 `sections-03-operator-algebra.md` §3.3 (alternative
  existence argument via Banach–Alaoglu).
- Paper 32 `research/01-modular-flow-ergodicity.md` (uniqueness used
  for factoriality).

---

*§06 contains no original results: everything is either classical
(Bost–Connes 1995) or a programme-internal cross-reference. The
load-bearing function is that §07–§10 and all of Part III use
uniqueness as a black box.*
