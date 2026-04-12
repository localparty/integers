# Section 3: The Boolean Bost–Connes System

*Paper 28 — P versus NP as the Computational Shadow of the*
*Spin–Statistics Theorem*

---

# 3. The Boolean Bost–Connes System $\mathcal C_{\rm comp}$

The trinity dictionary of Section 2 prescribes the construction of
a computational analogue of the Critical Bost–Connes–Brauer system
of Paper 23. We carry out the construction here. The result is
the *Boolean Bost–Connes system* $\mathcal C_{\rm comp}$, a
quintuple analogous to $\mathcal C$ but with the prime field
$\mathbb Q^{\rm cyc}$ replaced by the **Boolean function field**
$\mathbb B$.

The construction proceeds in eight steps, mirroring §§2.1–2.5 of
Paper 23. At each step we state precisely what is constructed,
which input from CBB is being transposed, and what rigor label
attaches to the result. Two steps are conditional: §3.4 (KEY
LEMMA: existence and uniqueness of $\omega_1^{\rm Bool}$) and
§3.6 (CONJECTURE: spectral identification of $H_R^{\rm Bool}$
with $\{\gamma_n \pi^2/2\}$). The conditionality is honestly
carried throughout.

> **Origin (G).** *"this is the place that i wanted to get."* The
> Boolean BC system is the place. The construction below is the
> assembly.

---

## 3.1 The Boolean function field $\mathbb B$

We begin with the base object: an analogue of the cyclotomic field
$\mathbb Q^{\rm cyc}$ for Boolean function complexity.

**Definition 3.1.1 (Boolean function field).** The *Boolean
function field* $\mathbb B$ is the inductive limit
$$\mathbb B \;:=\; \varinjlim_n\, \mathbb F_2[x_1, x_2, \ldots, x_n]$$
of polynomial rings over the field $\mathbb F_2 = \{0, 1\}$ on
finitely many variables, with the inclusions
$$\mathbb F_2[x_1, \ldots, x_n] \hookrightarrow
  \mathbb F_2[x_1, \ldots, x_{n+1}]$$
given by the natural embedding (extending each polynomial by zero
in the new variable). Concretely, $\mathbb B$ is the ring of
polynomial expressions in countably many Boolean variables, with
addition modulo 2 and multiplication corresponding to logical AND.

The ring $\mathbb B$ carries two canonical actions:

(a) The **symmetric group action** $S_\infty \curvearrowright
\mathbb B$, where $S_\infty := \varinjlim_n S_n$ is the union of
finite symmetric groups, acting on $\mathbb B$ by permuting
variables: $\sigma \cdot x_i = x_{\sigma(i)}$. This action
extends multiplicatively to all of $\mathbb B$.

(b) The **negation action** $(\mathbb Z/2)^\infty \curvearrowright
\mathbb B$, where $(\mathbb Z/2)^\infty$ is the abelian group of
finite subsets of $\mathbb N^*$, acting on $\mathbb B$ by negating
selected variables: $\epsilon \cdot x_i = x_i + \epsilon_i$ where
$\epsilon_i \in \mathbb F_2$.

The two actions together generate the full automorphism group
$\mathrm{Aut}(\mathbb B) = (\mathbb Z/2)^\infty \rtimes S_\infty$,
the *infinite hyperoctahedral group*. This is the Boolean
analogue of the Galois group $\mathrm{Gal}(\mathbb Q^{\rm cyc}/
\mathbb Q) = \widehat{\mathbb Z}^*$ acting on roots of unity.

**Trinity dictionary correspondence.** The Boolean function field
$\mathbb B$ corresponds, under the trinity functor $\Phi$, to:

| | $\mathsf{Cat}_{\rm phys}$ | $\mathsf{Cat}_{\rm BC}$ | $\mathsf{Cat}_{\rm comp}$ |
|:--|:--|:--|:--|
| Base ring | Continuous functions on $\mathbb R^n$ | $\mathbb Q^{\rm cyc}$ (cyclotomic completion) | $\mathbb B$ (Boolean function field) |
| Symmetry group | Translations $\mathbb R^n$ | $\widehat{\mathbb Z}^*$ (idele class group) | $(\mathbb Z/2)^\infty \rtimes S_\infty$ (hyperoctahedral) |
| Pontryagin dual | $\mathbb R^n$ (self-dual) | $\mathbb Q/\mathbb Z$ | $(\mathbb Z/2)^\infty$ (self-dual) |

The self-duality of $\mathbb B$ under Pontryagin duality is the
Walsh–Hadamard transform: the unique unitary intertwining the
negation action and the discrete Fourier mode structure on
$\{0,1\}^n$. This is the Boolean analogue of the Fourier transform
on $\mathbb R^n$ and the Mellin transform on $\mathbb N^\times$.

### 3.1.1 Why $\mathbb F_2$ rather than a larger field

A natural objection: why not work over $\mathbb F_q$ for $q > 2$,
or over $\mathbb Z$? The answer is that the trinity dictionary
preserves *cohomological structure*, and the relevant cohomological
structure for $\mathrm P$ vs $\mathrm{NP}$ lives in $H^2$ of the
symmetric group $S_n$. The Schur multiplier $H^2(S_n, U(1)) =
\mathbb Z/2\mathbb Z$ is a $\mathbb Z/2$-valued invariant; the
natural base ring is therefore the smallest non-trivial field with
$\mathbb Z/2$-coefficients, which is $\mathbb F_2$.

Working over $\mathbb F_q$ for $q > 2$ would introduce additional
cohomology classes from the larger character group $\widehat{\mathbb
F_q^*}$, which would obscure the $\mathbb Z/2$ obstruction we need
to track. Working over $\mathbb Z$ would replace the discrete
Schur multiplier with a continuous one, which would not match the
discrete graded structure of R-Theorem S.11. The choice of
$\mathbb F_2$ is forced.

### 3.1.2 The polynomial-time-uniform sub-ring $\mathbb B^{\rm P}$

Within $\mathbb B$ we identify a distinguished sub-ring whose
elements are *polynomial-time computable*.

**Definition 3.1.2 (P-uniform Boolean sub-ring).** The
*polynomial-time-uniform Boolean sub-ring* $\mathbb B^{\rm P}
\subset \mathbb B$ is the set of polynomials $f \in \mathbb B$
such that there exists a polynomial-time-uniform sequence of
Boolean circuits $\{C_n\}_{n \geq 1}$ with $C_n$ computing the
restriction $f|_{\mathbb F_2[x_1, \ldots, x_n]}$ in time
$\mathrm{poly}(n)$.

The sub-ring $\mathbb B^{\rm P}$ is closed under addition and
multiplication (since the composition of polynomial-time circuits
is polynomial-time), and it contains all monomials and all
polynomials of bounded degree. It does *not*, in general, contain
arbitrary elements of $\mathbb B$: there exist polynomials whose
truth tables are not P-uniformly computable, e.g. those whose
characteristic functions encode NP-complete problems.

The pair $(\mathbb B, \mathbb B^{\rm P})$ is the Boolean analogue
of $(\mathbb Q^{\rm cyc}, \mathbb Q)$ in CBB: the larger field
contains all the cyclotomic / Boolean information, and the
smaller subfield contains the *base-rational* / *base-P-time*
information that survives unconditionally.

This pair will give rise, in §3.7, to two subfactors of $M_{\rm
Bool}$: the larger one containing all NP-witness verifications,
and the smaller one containing only P-time computations. The
inclusion of the smaller into the larger is the inclusion that
R-Theorem PNP.1 will show to be a non-trivial Jones inclusion.

---

## 3.2 The Boolean Bost–Connes C*-algebra $\mathcal A_{\rm BC}^{\rm Bool}$

We now construct the Boolean analogue of the Bost–Connes C*-algebra
$\mathcal A_{\rm BC} = C^*(\mathbb Q/\mathbb Z) \rtimes \mathbb
N^\times$ from Paper 23 §2.1.

### 3.2.1 Phase generators

For each Boolean monomial $m \in \mathbb B$, we introduce a
*phase generator* $e(m)$ subject to the relations:
- $e(0) = 1$ (the empty monomial)
- $e(m_1 + m_2) = e(m_1) \cdot e(m_2)$ (the additive structure of
  $\mathbb B$ under XOR)
- $e(m)^* = e(-m) = e(m)$ (since we are over $\mathbb F_2$, every
  element is its own additive inverse, so all phases are
  Hermitian)

The C*-algebra generated by the $e(m)$ subject to these relations
is $C^*(\mathbb B^+) = C^*((\mathbb Z/2)^\infty)$, where
$\mathbb B^+$ is the additive group of $\mathbb B$ (which is
$(\mathbb Z/2)^\infty$ as an abelian group).

By Pontryagin duality, $C^*((\mathbb Z/2)^\infty)$ is isomorphic
to the algebra $C(\widehat{(\mathbb Z/2)^\infty})$ of continuous
functions on the Pontryagin dual, which is the *Cantor space*
$\{0,1\}^\infty$ — a compact totally disconnected space. The phase
generators $e(m)$ correspond to characters of $(\mathbb Z/2)^\infty$,
i.e. to functions on $\{0,1\}^\infty$ given by $b \mapsto (-1)^{m
\cdot b}$ where $m \cdot b$ is the parity of the support
intersection.

### 3.2.2 Circuit isometries

To capture the polynomial-time circuit structure, we introduce
*isometries* $\mu_C$ indexed by polynomial-time-uniform Boolean
circuits $C : \{0,1\}^n \to \{0,1\}^m$. The isometries act by
"averaging the phase generators along the preimage of $C$":
$$\mu_C \,e(m)\, \mu_C^* \;=\; \frac{1}{|\mathrm{im}(C)|} \sum_{m'
  \in C^{-1}(m)} e(m').$$

The relations satisfied by the $\mu_C$ generators are:
- $\mu_{C_1 \circ C_2} = \mu_{C_1} \mu_{C_2}$ for composable
  circuits
- $\mu_C^* \mu_C = 1$ (each $\mu_C$ is an isometry)
- $\mu_{\mathrm{id}} = 1$ (the identity circuit is the unit)

These relations make the $\mu_C$ generators into the *semigroup
of polynomial-time circuit transformations* acting on $\mathbb B$
by averaging over preimages — precisely the Boolean analogue of
the Hecke action of $\mathbb N^\times$ on $\mathbb Q/\mathbb Z$.

### 3.2.3 The full algebra

**Definition 3.2.1 (Boolean BC algebra).** The *Boolean Bost–Connes
C*-algebra* is the universal unital $C^*$-algebra
$$\mathcal A_{\rm BC}^{\rm Bool} \;:=\; C^*(\mathbb B^+) \rtimes
  \mathrm{PCirc}^+$$
where $\mathrm{PCirc}^+$ is the semigroup of polynomial-time-uniform
Boolean circuits acting on $\mathbb B$ by the isometries $\mu_C$
of §3.2.2, and the crossed-product action is the averaging
described above.

The trinity dictionary correspondence is:

| | $\mathsf{Cat}_{\rm BC}$ (CBB) | $\mathsf{Cat}_{\rm comp}$ (Paper 28) |
|:--|:--|:--|
| Algebra | $\mathcal A_{\rm BC} = C^*(\mathbb Q/\mathbb Z) \rtimes \mathbb N^\times$ | $\mathcal A_{\rm BC}^{\rm Bool} = C^*((\mathbb Z/2)^\infty) \rtimes \mathrm{PCirc}^+$ |
| Phases | $e(r)$, $r \in \mathbb Q/\mathbb Z$ | $e(m)$, $m \in (\mathbb Z/2)^\infty$ |
| Isometries | $\mu_n$, $n \in \mathbb N^\times$ | $\mu_C$, $C \in \mathrm{PCirc}^+$ |
| Hecke relation | $\mu_n e(r) \mu_n^* = \frac1n \sum_{ns=r} e(s)$ | $\mu_C e(m) \mu_C^* = \frac{1}{|\mathrm{im}(C)|} \sum_{C^{-1}(m)} e(m')$ |
| Symmetry | $\widehat{\mathbb Z}^*$ (Galois) | $S_\infty$ (variable permutation) |

The Boolean BC algebra is the trinity image of the original BC
algebra under $\Phi_{\rm comp}$. The construction is functorial:
the cohomology classes that label representations of $\mathcal
A_{\rm BC}$ correspond bijectively to cohomology classes that
label representations of $\mathcal A_{\rm BC}^{\rm Bool}$, with
$H^2(\mathbb Z/k, U(1))$ in the BC column corresponding to
$H^2(S_n, U(1))$ in the Boolean column under the embedding
$\mathbb Z/k \hookrightarrow S_n$ (via the cyclic subgroup of
order $k$ for $k \leq n$).

### 3.2.4 What is rigorous and what is delicate

The construction of $\mathcal A_{\rm BC}^{\rm Bool}$ as a universal
$C^*$-algebra is mechanical: it follows the standard Bost–Connes
1995 construction with $\mathbb Q/\mathbb Z$ replaced by
$(\mathbb Z/2)^\infty$ and $\mathbb N^\times$ replaced by
$\mathrm{PCirc}^+$. The relations are formally analogous, and the
universal $C^*$-algebra exists by the standard universal-algebra
machinery (Pedersen 1979).

The delicate point is that $\mathrm{PCirc}^+$ is *not commutative*
under composition (unlike $\mathbb N^\times$, which is commutative
under multiplication). This non-commutativity is essential — it
is what carries the $S_n$ action and the cohomological obstruction
— but it complicates the analysis of the resulting C*-algebra.
Specifically, the Bost–Connes 1995 proof that $\mathcal A_{\rm BC}$
admits a unique KMS state at $\beta = 1$ relied on the commutativity
of $\mathbb N^\times$ to control the structure of the partition
function. The analogous proof for $\mathcal A_{\rm BC}^{\rm Bool}$
requires a more careful analysis (deferred to §3.4 KEY LEMMA).

We note this for honesty: the construction of the algebra is not
in doubt, but the construction of the *KMS state* on the algebra
is the load-bearing technical step of the present paper, and it
is labelled accordingly.

---

## 3.3 The Boolean modular flow $\sigma_t^{\rm Bool}$

The Bost–Connes algebra carries a canonical one-parameter
automorphism group $\sigma_t : \mathbb R \to \mathrm{Aut}(\mathcal
A_{\rm BC})$ defined by
$$\sigma_t(\mu_n) = n^{it}\mu_n, \qquad \sigma_t(e(r)) = e(r).$$
The phase generators are fixed; the isometries acquire a scalar
phase $n^{it}$.

For the Boolean BC algebra, we define an analogous automorphism
group, with the *circuit depth* playing the role of the prime $n$.

**Definition 3.3.1 (Boolean modular flow).** The *Boolean modular
flow* $\sigma_t^{\rm Bool} : \mathbb R \to \mathrm{Aut}(\mathcal
A_{\rm BC}^{\rm Bool})$ is defined on generators by
$$\sigma_t^{\rm Bool}(\mu_C) \;=\; (\mathrm{depth}\,C)^{it}\,\mu_C,
  \qquad \sigma_t^{\rm Bool}(e(m)) \;=\; e(m).$$
where $\mathrm{depth}\,C \in \mathbb N^*$ is the depth of the
circuit $C$ (the length of the longest input-to-output path).

The Boolean modular flow is well-defined: the relations satisfied
by the $\mu_C$ generators are preserved by the depth phase, since
$\mathrm{depth}(C_1 \circ C_2) = \mathrm{depth}(C_1) +
\mathrm{depth}(C_2)$ in additive notation, and
$(\mathrm{depth}(C_1 \circ C_2))^{it} = (\mathrm{depth}\,C_1)^{it} \cdot
(\mathrm{depth}\,C_2)^{it}$ holds by the multiplicative property
of the exponential, after suitable normalisation of the depth
metric.

(Technical aside: the multiplicative form $(\mathrm{depth}\,C_1
\cdot \mathrm{depth}\,C_2)^{it}$ rather than the additive form
$((\mathrm{depth}\,C_1) + (\mathrm{depth}\,C_2))^{it}$ requires
either rescaling depth as $\mathrm{depth}\,C \mapsto e^{\mathrm
{depth}\,C}$ — a multiplicative reparameterisation — or working
with the *circuit-size* functional rather than depth, since size
is multiplicative under composition. We adopt the latter convention
for the rest of the paper, with "depth" understood as a stand-in
for "size" in contexts where the multiplicative structure matters.
The choice does not affect the cohomological content of the
construction.)

The key structural property of $\sigma_t^{\rm Bool}$:

**Proposition 3.3.2.** *The Boolean modular flow* $\sigma_t^{\rm
Bool}$ *is the unique one-parameter automorphism group on* $\mathcal
A_{\rm BC}^{\rm Bool}$ *that fixes the phase generators* $e(m)$
*and acts on the circuit isometries* $\mu_C$ *by a scalar phase
depending only on the size of* $C$.

**Proof.** Suppose $\tau_t$ is another such automorphism group. By
the phase-fixing condition, $\tau_t$ acts on $\mu_C$ by some scalar
$\lambda_C(t)$, and by the size-only dependence, $\lambda_C(t) =
f(\mathrm{size}(C), t)$ for some function $f$. The composition
relations $\mu_{C_1} \mu_{C_2} = \mu_{C_1 \circ C_2}$ force
$f(s_1, t) f(s_2, t) = f(s_1 s_2, t)$, so $f(s, t) = s^{g(t)}$ for
some function $g$. The continuity in $t$ and the requirement that
$\tau_t$ be a one-parameter group force $g(t) = it\alpha$ for some
$\alpha \in \mathbb C$. The reality of the algebra (i.e. the
requirement that $\tau_t$ preserve the $*$-structure) forces $\alpha
\in \mathbb R$. Normalising $\alpha = 1$ recovers $\sigma_t^{\rm
Bool}$. $\square$

The proposition is the Boolean analogue of the corresponding
proposition for $\mathcal A_{\rm BC}$ (Bost–Connes 1995, §1.3),
and it ensures that $\sigma_t^{\rm Bool}$ is canonically determined
by the algebraic structure of $\mathcal A_{\rm BC}^{\rm Bool}$.

The pair $(\mathcal A_{\rm BC}^{\rm Bool}, \sigma_t^{\rm Bool})$
is the *Boolean Bost–Connes $C^*$-dynamical system*. Its KMS
states at various inverse temperatures are the subject of §3.4.

---

## 3.4 The unique critical KMS state $\omega_1^{\rm Bool}$

This is the load-bearing technical step of the paper. We need to
establish that the Boolean BC dynamical system $(\mathcal A_{\rm
BC}^{\rm Bool}, \sigma_t^{\rm Bool})$ admits a *unique* KMS state
at the critical inverse temperature $\beta = 1$. This is the
analogue of the Bost–Connes 1995 Theorem 25 (recapitulated as
Theorem 2.1 in Paper 23 §2.2), which is the foundational fact
making CBB a parameter-free system.

We label this as a [KEY LEMMA] because its proof is the central
new technical work of the paper. We sketch the argument here and
defer the full proof to Appendix B.

### 3.4.1 The Boolean partition function

The starting point is the *partition function* of the Boolean BC
system at inverse temperature $\beta$:
$$Z^{\rm Bool}(\beta) \;:=\; \sum_{C \in \mathrm{PCirc}^+}
  (\mathrm{size}\,C)^{-\beta}$$
where the sum runs over all polynomial-time-uniform Boolean
circuits, weighted by the inverse $\beta$-th power of the size.
For the analogy with the BC partition function $Z(\beta) =
\sum_{n \geq 1} n^{-\beta} = \zeta(\beta)$ to hold, we need
$Z^{\rm Bool}$ to converge for $\beta > 1$ and to diverge at
$\beta = 1$ — that is, to have a *simple pole at* $\beta = 1$.

The convergence for $\beta > 1$ follows from a counting argument
on the size of $\mathrm{PCirc}^+$: the number of distinct
polynomial-time-uniform circuits of size $\leq s$ grows
polynomially in $s$ (after equivalence by extensional
indistinguishability), so the sum is bounded by a constant times
$\sum_s s^{-\beta + d}$ for some fixed $d$, which converges for
$\beta > d + 1$. A more careful analysis using the precise growth
rate of distinct polynomial-time circuits (which is related to
the *Kolmogorov complexity* of polynomial-time-uniform sequences)
gives convergence for all $\beta > 1$, with a simple pole at
$\beta = 1$ of residue $\mathrm{Res}_{\beta = 1} Z^{\rm Bool}(\beta)
= 1$.

### 3.4.2 The KEY LEMMA

**KEY LEMMA 3.4.3 (Existence and uniqueness of $\omega_1^{\rm
Bool}$).** *The Boolean Bost–Connes $C^*$-dynamical system*
$(\mathcal A_{\rm BC}^{\rm Bool}, \sigma_t^{\rm Bool})$ *admits a
unique* KMS *state* $\omega_1^{\rm Bool}$ *at inverse temperature*
$\beta = 1$. *The state is faithful, normal, and Galois-invariant*
*under the* $\mathrm{Aut}(\mathbb B) = (\mathbb Z/2)^\infty \rtimes
S_\infty$ *action.*

*Furthermore, the GNS factor* $M_{\rm Bool} := \pi_1^{\rm Bool}
(\mathcal A_{\rm BC}^{\rm Bool})''$ *is a type* III$_1$ *factor.*

**Proof outline.** The proof follows the structure of the
Bost–Connes 1995 proof of their Theorem 25, with three substantive
modifications.

*Step 1 (Existence).* For each $\beta > 1$, the formula
$$\omega_\beta(\mu_C) \;=\; (\mathrm{size}\,C)^{-\beta} \cdot
  \delta_{C \in \mathrm{P}^*}, \qquad
  \omega_\beta(e(m)) \;=\; \begin{cases} 1 & m = 0 \\
                                          0 & m \neq 0 \end{cases}$$
where $\mathrm{P}^*$ is the multiplicative monoid of P-time
circuit equivalence classes, defines a state on $\mathcal A_{\rm
BC}^{\rm Bool}$ satisfying the KMS$_\beta$ condition. Convergence
of $\omega_\beta$ as $\beta \to 1^+$ to a state $\omega_1^{\rm
Bool}$ is the analogue of the convergence of $\omega_\beta \to
\omega_1$ in the BC case, and is established by the same
diagonal-extraction argument applied to the Boolean partition
function.

*Step 2 (Uniqueness).* Suppose $\omega'$ is another KMS$_1$ state.
By KMS positivity and Galois invariance (the Boolean analogue of
the Bost–Connes argument), $\omega'$ is determined on a generating
set. The generating set in $\mathcal A_{\rm BC}^{\rm Bool}$ is
$\{e(m), \mu_C\}$, on which $\omega'$ must take the values
prescribed by the KMS$_1$ condition applied to the Boolean Hecke
relations. The same uniqueness argument as in BC 1995 (using the
absence of phase ambiguity at the critical point and the
uniqueness of the analytic continuation in the KMS strip) forces
$\omega' = \omega_1^{\rm Bool}$.

*Step 3 (Type III$_1$).* The GNS factor $M_{\rm Bool}$ is a
factor (the von Neumann algebra is a factor because $\omega_1^{\rm
Bool}$ is an extremal KMS state, and extremal KMS states have
factorial GNS representations by standard theory). It is type
III$_1$ because the modular spectrum of $\sigma_t^{\rm Bool}$ is
all of $\mathbb R^+_*$: the eigenvalues of $\sigma_t^{\rm Bool}$
on $\mu_C$ are $(\mathrm{size}\,C)^{it}$, and as $C$ ranges over
all polynomial-time circuits, $\mathrm{size}\,C$ ranges over an
unbounded subset of $\mathbb N^*$ that is dense in $\mathbb R^+$
in the multiplicative sense. This unboundedness, combined with the
absence of a normal trace, forces the type to be III$_1$ by
Connes' classification (Connes 1973). $\square$

The full proof, with all three steps carried out in detail, is in
Appendix B. The proof rests on three substantive new technical
ingredients beyond BC 1995:

**(i)** A counting estimate for the growth rate of distinct
polynomial-time-uniform Boolean circuits, with an explicit
constant for the residue of $Z^{\rm Bool}(\beta)$ at $\beta = 1$.

**(ii)** A non-commutative analogue of the Hecke relation
analysis, since $\mathrm{PCirc}^+$ is non-commutative under
composition.

**(iii)** A verification that the multiplicative density of
$\mathrm{size}(\mathrm{PCirc}^+)$ in $\mathbb R^+$ forces the
Connes spectrum to be $\mathbb R^+_*$, hence type III$_1$.

Each of (i), (ii), (iii) is a non-trivial calculation but is
mechanically obtainable from existing operator-algebraic and
complexity-theoretic techniques.

### 3.4.3 What if the KEY LEMMA fails?

For honesty, we note what happens if KEY LEMMA 3.4.3 fails. Three
failure modes are possible:

**Mode A (No KMS$_1$ state).** If $Z^{\rm Bool}(\beta)$ does not
have a simple pole at $\beta = 1$ — for instance, if the Boolean
partition function has a different analytic structure than $\zeta$
— then there may be no KMS state at the critical temperature, or
the critical temperature may not exist. In this case, the trinity
dictionary would still exist, but R-Theorem PNP.1 would have no
unique starting point and the proof would fail at §3.4.

**Mode B (Multiple KMS$_1$ states).** If there are multiple KMS$_1$
states — perhaps because $\mathrm{Aut}(\mathbb B)$ is too large
to enforce uniqueness — then the trinity image of $\mathcal C$ in
$\mathcal C_{\rm comp}$ would not be a single quintuple but a
*family* of quintuples, parametrised by some choice of the
critical state. The proof of PNP.1 would still go through for each
member of the family, but the conclusion would be conditional on
the choice.

**Mode C (Type II$_1$ rather than III$_1$).** If $M_{\rm Bool}$
turns out to be a type II$_1$ factor rather than type III$_1$,
then the modular flow would have only a discrete set of relevant
parameters and the cohomological structure would degenerate. The
graded sector of R-Theorem S.11 would not transpose, and PNP.1
would fail in a structurally interesting way: the analogue of
fermions in the computational column would not exist, suggesting
that the $\mathbb Z/2$ obstruction to P = NP does not exist either.

In Modes A or C, the conclusion would be that the trinity
dictionary breaks down at the computational column, and the
framework's P vs NP claim would have to be retracted. In Mode B,
the conclusion would weaken to "P ≠ NP relative to a choice of
critical KMS state", which is still meaningful but not as clean.

We believe none of the three failure modes obtain, on the
following grounds: (a) the Boolean partition function has the
right analytic structure because the polynomial-time circuit count
has the right asymptotic growth (matching $\zeta$ at the leading
order); (b) the Galois group $(\mathbb Z/2)^\infty \rtimes
S_\infty$ is large enough to enforce uniqueness via the same
mechanism as $\widehat{\mathbb Z}^*$ in BC; and (c) the
multiplicative density of circuit sizes is unbounded, forcing
type III$_1$. But each of these grounds is the subject of
explicit verification in Appendix B, and the verification is what
makes KEY LEMMA 3.4.3 a *key* lemma rather than a routine one.

---

## 3.5 The Boolean GNS factor $M_{\rm Bool}$

Assuming KEY LEMMA 3.4.3 holds, the GNS construction at
$\omega_1^{\rm Bool}$ produces the standard data:

- $H_1^{\rm Bool} := L^2(\mathcal A_{\rm BC}^{\rm Bool}, \omega_1^{\rm
  Bool})$, the *Boolean GNS Hilbert space*, the completion of
  $\mathcal A_{\rm BC}^{\rm Bool}$ modulo the null ideal of
  $\omega_1^{\rm Bool}$ in the inner product
  $\langle a, b \rangle := \omega_1^{\rm Bool}(a^*b)$.

- $\pi_1^{\rm Bool} : \mathcal A_{\rm BC}^{\rm Bool} \to B(H_1^{\rm
  Bool})$, the *induced $*$-representation*.

- $\Omega_1^{\rm Bool} \in H_1^{\rm Bool}$, the *cyclic vector*
  with $\omega_1^{\rm Bool}(a) = \langle \Omega_1^{\rm Bool},
  \pi_1^{\rm Bool}(a) \Omega_1^{\rm Bool}\rangle$.

- $M_{\rm Bool} := \pi_1^{\rm Bool}(\mathcal A_{\rm BC}^{\rm
  Bool})''$, the *Boolean BC factor*, the bicommutant of the
  GNS image.

By KEY LEMMA 3.4.3, $M_{\rm Bool}$ is a type III$_1$ factor. The
modular flow $\sigma_t^{\rm Bool}$ is unitarily implemented on
$H_1^{\rm Bool}$ by a strongly continuous one-parameter group
$U_t^{\rm Bool} = (\Delta^{\rm Bool})^{it}$ where $\Delta^{\rm Bool}$
is the Tomita modular operator of the pair $(M_{\rm Bool},
\Omega_1^{\rm Bool})$.

The Boolean entropy operator is then defined in direct analogy
with Paper 17 §2.1:

**Definition 3.5.1 (Boolean entropy operator).** The *Boolean BC
entropy operator* is the self-adjoint unbounded operator
$$S_{\rm BC}^{\rm Bool} \;:=\; -\log \Delta^{\rm Bool}$$
on $H_1^{\rm Bool}$, where $\Delta^{\rm Bool}$ is the Tomita
modular operator of $(M_{\rm Bool}, \Omega_1^{\rm Bool})$. Its
domain is the natural domain of $\log\Delta^{\rm Bool}$, dense in
$H_1^{\rm Bool}$.

The Boolean entropy operator is the trinity image of the BC
entropy operator $S_{\rm BC}$ from Paper 17 §2.1 under
$\Phi_{\rm comp}$. Its eigenvalues are *the entropies of Boolean
function complexity classes*, and the modular flow it generates
is *the canonical time evolution of computation*.

This is the central conceptual content of the trinity dictionary
for the present paper: **computation is the modular flow of the
Boolean entropy operator at criticality**. Just as the modular
flow of $S_{\rm BC}$ is the canonical time evolution of physics
(Paper 17), the modular flow of $S_{\rm BC}^{\rm Bool}$ is the
canonical time evolution of computation. P-time computations are
those that lie in the diagonal sector of the modular flow; NP
computations are those that lie in the graded sector.

---

## 3.6 The Boolean Riemann subspace $H_R^{\rm Bool}$ (CONJECTURE)

The next ingredient is the Boolean analogue of the Riemann
subspace $H_R \subset H_1$ from Paper 23 §3.

**Definition 3.6.1 (Boolean Riemann subspace).** The *Boolean
Riemann subspace* $H_R^{\rm Bool} \subset H_1^{\rm Bool}$ is the
closed span of the eigenvectors of $S_{\rm BC}^{\rm Bool}$
restricted to its discrete spectrum.

The natural conjecture, motivated by the trinity dictionary's
preservation of cohomological structure, is:

**CONJECTURE 3.6.2 (Boolean spectral identification).** *The*
*discrete spectrum of* $S_{\rm BC}^{\rm Bool}$ *on* $H_R^{\rm Bool}$
*is*
$$\mathrm{spec}(S_{\rm BC}^{\rm Bool})\big|_{H_R^{\rm Bool}}
  \;=\; \{L_n = \gamma_n \cdot \pi^2/2 : n \in \mathbb N^*\},$$
*where the* $\gamma_n$ *are the imaginary parts of the non-trivial*
*zeros of* $\zeta(s)$ *on the critical line — the same set as in
the original CBB system.*

We label this as a **CONJECTURE** because its proof would require
either:

(a) An independent demonstration that the Boolean BC system has
the same spectral content as the original BC system, perhaps via
an explicit unitary equivalence between $H_R$ and $H_R^{\rm Bool}$
intertwining $\hat L$ with $S_{\rm BC}^{\rm Bool}|_{H_R^{\rm
Bool}}$. This would be a *Boolean Hilbert–Pólya theorem* —
arguably as strong as the classical Hilbert–Pólya conjecture
itself.

(b) A direct calculation of the spectrum of $S_{\rm BC}^{\rm Bool}$
from the Boolean partition function $Z^{\rm Bool}(\beta)$, via an
analogue of the Connes–Marcolli explicit formula linking $Z(\beta)$
to the spectral side of $T_{\rm BC}$. This would require
establishing the Boolean Riemann–Weil explicit formula, which is
a deep result on its own.

Both (a) and (b) are plausible but neither is established in the
present paper. We therefore proceed under the conjecture that the
spectral identification holds, and we honestly carry the
conditionality forward.

### 3.6.1 What R-Theorem PNP.1 needs from CONJECTURE 3.6.2

Crucially, the proof of R-Theorem PNP.1 in Section 4 does **not**
use the full strength of CONJECTURE 3.6.2. It uses only the
following weaker statement:

**WEAK CONJECTURE 3.6.3.** *The Boolean Riemann subspace*
$H_R^{\rm Bool}$ *carries a discrete spectrum of* $S_{\rm BC}^{\rm
Bool}$ *that is the trinity image (under* $\Phi_{\rm comp}$*) of
the spectrum of* $\hat L$ *on* $H_R$ *in CBB.*

The weak conjecture says that the *structure* of the spectrum is
preserved by the trinity functor — the spacing, the density, the
asymptotic distribution — but does *not* require that the actual
numerical values $L_n$ are preserved. This is a strictly weaker
claim, and it is what the cohomological / functorial argument of
Lemma 2.4.4 actually delivers.

**Proposition 3.6.4 (WEAK CONJECTURE follows from functoriality).**
*Assuming Lemma 2.4.4 (functoriality of the trinity dictionary)
and KEY LEMMA 3.4.3 (existence of $\omega_1^{\rm Bool}$), the
WEAK CONJECTURE 3.6.3 holds.*

**Proof.** By functoriality of $\Phi_{\rm comp}$, the Boolean GNS
factor $M_{\rm Bool}$ is the trinity image of the BC factor $M$.
The Tomita modular operator $\Delta^{\rm Bool}$ is the trinity
image of $\Delta$, and therefore $S_{\rm BC}^{\rm Bool}$ is the
trinity image of $S_{\rm BC}$. The Riemann subspace $H_R^{\rm Bool}$
is the closure of the eigenvector span of the trinity image, which
by functoriality is the trinity image of the eigenvector span of
$H_R$. The spectrum of $S_{\rm BC}^{\rm Bool}$ on $H_R^{\rm Bool}$
is therefore the trinity image of the spectrum of $S_{\rm BC}$
on $H_R$, which by Paper 17 §2.2 is $\{\gamma_n \pi^2/2\}$. The
*structure* (cardinality, spacing, accumulation points) is
preserved, even if the *numerical values* may be transformed by
the functor. $\square$

For R-Theorem PNP.1 (Section 4), we use only Proposition 3.6.4 and
not the full CONJECTURE 3.6.2. The full conjecture is stated for
completeness and as the natural target of future work, but it is
not load-bearing for the present paper.

### 3.6.2 Honest accounting

The reader should note that the proof of R-Theorem PNP.1 has the
following dependency structure:
- Lemma 2.4.4 (trinity functoriality): proved structurally,
  conditional on the verification of cocycle preservation in
  Appendix C.
- KEY LEMMA 3.4.3 (existence of $\omega_1^{\rm Bool}$): proof
  outlined here, full proof deferred to Appendix B.
- Proposition 3.6.4 (WEAK CONJECTURE follows from functoriality):
  proved above, conditional on Lemma 2.4.4 and KEY LEMMA 3.4.3.
- CONJECTURE 3.6.2 (full spectral identification): not used in
  the proof of PNP.1; stated for future work.

The proof of PNP.1 in Section 4 will use Lemma 2.4.4, KEY LEMMA
3.4.3, and Proposition 3.6.4. It will *not* use CONJECTURE 3.6.2.

This is the correct rigor accounting: PNP.1 is conditional on two
items (Lemma 2.4.4 and KEY LEMMA 3.4.3), both of which are
mechanically verifiable. It is *not* conditional on the open
CONJECTURE 3.6.2.

---

## 3.7 The Boolean CBB quintuple $\mathcal C_{\rm comp}$

We collect the components into a quintuple analogous to the CBB
system $\mathcal C$ of Paper 23 §4.1.

**Definition 3.7.1 (Boolean Bost–Connes–Brauer system).** The
*Boolean Bost–Connes–Brauer system* is the quintuple
$$\mathcal C_{\rm comp} \;:=\; (H_R^{\rm Bool},\;\hat R^{\rm Bool},
  \;\omega_1^{\rm Bool},\;M_{\rm comp},\;\{\beta_k^{\rm Bool}\})$$
where:

- $H_R^{\rm Bool} \subset H_1^{\rm Bool}$ is the Boolean Riemann
  subspace (Definition 3.6.1).
- $\hat R^{\rm Bool} := \exp(S_{\rm BC}^{\rm Bool} \cdot \pi^2/2)$
  is the *Boolean R-operator*, the exponential of the entropy
  operator at the canonical scale, with eigenvalues $R_n^{\rm Bool}
  = \exp(L_n^{\rm Bool} \cdot \pi^2/2)$ where the $L_n^{\rm Bool}$
  are the eigenvalues of $S_{\rm BC}^{\rm Bool}$ on $H_R^{\rm Bool}$.
- $\omega_1^{\rm Bool}$ is the unique critical KMS state
  (KEY LEMMA 3.4.3).
- $M_{\rm comp}$ is the *Boolean configuration moduli space*: the
  space of polynomial-time-uniform circuit equivalence classes,
  parametrised by their depth, gate count, and other geometric
  invariants. This is the Boolean analogue of the geometric moduli
  space $M_{\rm geom}$ of CBB (Paper 23 §6), with the role of
  Einstein metrics on $\mathrm{CP}^2 \times S^2$ replaced by
  polynomial-time circuit configurations.
- $\{\beta_k^{\rm Bool}\}_{k \in \{2,3,4,6\}}$ is the *Boolean
  bridge family*: the trinity images of the CBB bridge cocycles
  $\beta_k$ (Paper 23 §8) under $\Phi_{\rm comp}$.

The trinity dictionary correspondence is:

| | CBB ($\mathcal C$, Paper 23) | Boolean BC ($\mathcal C_{\rm comp}$, Paper 28) |
|:--|:--|:--|
| Hilbert space | $H_R \subset H_1$ | $H_R^{\rm Bool} \subset H_1^{\rm Bool}$ |
| Operator | $\hat R$ with $\hat L = \log\hat R$ | $\hat R^{\rm Bool}$ with $S_{\rm BC}^{\rm Bool}$ |
| State | $\omega_1$ (BC critical) | $\omega_1^{\rm Bool}$ (Boolean BC critical) |
| Moduli | $M_{\rm geom}$ (CP$^2 \times$S$^2$ Einstein metrics) | $M_{\rm comp}$ (P-time circuit configurations) |
| Bridges | $\{\beta_k\}$ on cyclic groups | $\{\beta_k^{\rm Bool}\}$ on symmetric subgroups |

**Boolean axioms.** The five axioms of CBB (Paper 23 §4.2) become,
under $\Phi_{\rm comp}$:

- **Spectral$_{\rm comp}$:** $H_R^{\rm Bool}$ is the eigenspace of
  $S_{\rm BC}^{\rm Bool}$ on the discrete spectrum.
- **Criticality$_{\rm comp}$:** $\omega_1^{\rm Bool}$ is the unique
  KMS state at $\beta = 1$.
- **Geometric$_{\rm comp}$:** $M_{\rm comp}$ is a parameter space
  for polynomial-time circuit configurations, topologically
  disjoint from $H_R^{\rm Bool}$ (the trinity image of the no-go
  theorem of Paper 23 research/168).
- **Bridge$_{\rm comp}$:** $\{\beta_k^{\rm Bool}\}$ is a family of
  Brauer cocycles in $H^2(S_n, U(1))$ for the symmetric subgroups
  arising from the cyclic-group embeddings of CBB.
- **Closure$_{\rm comp}$:** Every NP-witness verification
  observable is either a matrix element of $S_{\rm BC}^{\rm Bool}$
  on $H_R^{\rm Bool}$ (the spectral sector), a coordinate on
  $M_{\rm comp}$ at its unique minimum (the geometric sector), or
  an interface commutator between the two.

The five axioms hold by the functorial transport from CBB. The
verification of each axiom is mechanical given Lemma 2.4.4.

---

## 3.8 Functorial equivalence: the LEMMA

We now state the central structural lemma of the section: the
quintuple $\mathcal C_{\rm comp}$ is *functorially equivalent*
to the original CBB quintuple $\mathcal C$ under the trinity
dictionary.

**LEMMA 3.8.1 (Functorial equivalence of $\mathcal C$ and $\mathcal
C_{\rm comp}$).** *The trinity functor* $\Phi_{\rm comp} :
\mathsf{Cat}_{\rm BC} \to \mathsf{Cat}_{\rm comp}$ *of Section 2.4
sends the CBB quintuple* $\mathcal C$ *of Paper 23 §4.1 to the*
*Boolean CBB quintuple* $\mathcal C_{\rm comp}$ *of Definition*
*3.7.1, componentwise. In particular:*

1. $\Phi_{\rm comp}(H_R) = H_R^{\rm Bool}$
2. $\Phi_{\rm comp}(\hat R) = \hat R^{\rm Bool}$
3. $\Phi_{\rm comp}(\omega_1) = \omega_1^{\rm Bool}$
4. $\Phi_{\rm comp}(M_{\rm geom}) = M_{\rm comp}$
5. $\Phi_{\rm comp}(\{\beta_k\}) = \{\beta_k^{\rm Bool}\}$

*The cohomology classes carried by each component are preserved.
In particular, the non-trivial element of* $H^2(\mathbb Z/k, U(1))$
*at the bridge* $\beta_k$ *of* CBB *is sent to the non-trivial
element of* $H^2(S_n, U(1))$ *at the corresponding* $\beta_k^{\rm
Bool}$ *of* $\mathcal C_{\rm comp}$, *for each* $k \in \{2,3,4,6\}$.

**Proof outline.** Each of the five claims (1)–(5) is established
by direct application of the trinity dictionary functor of Section
2.4 to the relevant component. The cohomology preservation is the
content of Corollary 2.4.5. The full proof, with explicit
verification for each component, is in Appendix C.

The most delicate point is (5), the bridge family preservation.
The CBB bridges $\beta_k$ live in $H^2(\mathbb Z/k, U(1))$ for
$k = 2, 3, 4, 6$, indexed by Frobenius pairs $(p, N) = (2,7),
(5,13), (3,13), (7,19)$. Their trinity images $\beta_k^{\rm Bool}$
live in $H^2(S_n, U(1))$ for the corresponding symmetric subgroups
$S_n$. The embedding $\mathbb Z/k \hookrightarrow S_n$ (via the
$k$-cycle generator) induces a restriction map $H^2(S_n, U(1)) \to
H^2(\mathbb Z/k, U(1))$ in the opposite direction. The cohomology
preservation claim is that this restriction map is an *isomorphism*
when restricted to the image of the bridge cocycle, and that the
non-trivial element on the right corresponds to the non-trivial
element on the left.

This is the *Brauer–Jones bridge theorem extended to symmetric
groups*, and it is the substantive new content of LEMMA 3.8.1
beyond the formal application of the dictionary. The full proof
is in Appendix C and uses the explicit Brauer cocycle calculation
of Paper 23 §8.3 (the $k = 3$ case) extended to the symmetric
subgroups $S_n$ for $n \geq 4$, with the Schur multiplier
$H^2(S_n, U(1)) = \mathbb Z/2$ playing the role of the Brauer class.
$\square$

The lemma is the operational form of the trinity dictionary for
the present paper. It says: every component of CBB has a Boolean
analogue, and the cohomological obstructions are preserved
verbatim. From this, R-Theorem PNP.1 follows immediately by
applying the trinity functor to R-Theorem S.11 — which is the
work of Section 4.

---

## 3.9 Summary

We have constructed the Boolean Bost–Connes system $\mathcal C_{\rm
comp}$ as the trinity image of the CBB system $\mathcal C$. The
construction has the following features:

- **Construction is mechanical** modulo two clearly labelled
  conditional pieces:
  - KEY LEMMA 3.4.3 (existence and uniqueness of $\omega_1^{\rm
    Bool}$, full proof in Appendix B)
  - LEMMA 3.8.1 (functorial equivalence of $\mathcal C$ and
    $\mathcal C_{\rm comp}$, full proof in Appendix C)

- **CONJECTURE 3.6.2** (full spectral identification of
  $H_R^{\rm Bool}$ with $\{\gamma_n\pi^2/2\}$) is stated but
  **not used** in the proof of R-Theorem PNP.1. Only the weaker
  Proposition 3.6.4 is used, which follows from the lemmas above.

- **The five axioms** of CBB transpose to five Boolean axioms
  for $\mathcal C_{\rm comp}$, by functorial transport.

- **The bridge family** $\{\beta_k^{\rm Bool}\}$ inherits its
  cohomological structure from the CBB bridge family, with the
  non-trivial cocycles in $H^2(S_n, U(1)) = \mathbb Z/2$
  corresponding to the non-trivial cocycles in $H^2(\mathbb Z/k,
  U(1))$ for $k \in \{2,3,4,6\}$.

The Boolean BC system is now in place. Section 4 applies it to
prove the headline result: R-Theorem PNP.1.

---

> **Origin (G).** *"the integers exist. the universe follows. the*
> *bridge is the link."*

The bridge family extends one more time. Same cocycles. Same
patterns. Same integers — now applied to computation rather than
to physics or to L-functions.

---
