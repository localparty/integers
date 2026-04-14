# §11 — Modular Operator $\Delta$ Construction

*Paper 49, Part III: Tomita-Takesaki machinery. The first of six sections
that take the type III$_1$ factor produced in Part II and run it through
Tomita-Takesaki (1970) to extract the canonical modular data $(\Delta, J)$.
This section constructs the positive self-adjoint unbounded operator $\Delta$
from the KMS$_1$ vector. The construction is entirely classical; every step
follows Takesaki Vol II §VI.*

---

## The data we inherit from Part II

Part II (§05-§10) delivered to us a quadruple
$$(M_1, \; H_{\omega_1}, \; \xi_{\omega_1}, \; P^+)$$
of the following shape:

- $M_1 = \pi_{\omega_1}(A_{BC})'' \subset B(H_{\omega_1})$ is a type III$_1$
  factor (Araki-Woods, §08).
- $H_{\omega_1}$ is the GNS Hilbert space obtained from the unique KMS$_1$
  state $\omega_1$ of the Bost-Connes system (§07).
- $\xi_{\omega_1} \in H_{\omega_1}$ is the GNS cyclic vector. It is
  *cyclic* for $M_1$ ($\overline{M_1 \xi_{\omega_1}} = H_{\omega_1}$) and
  *separating* for $M_1$ ($a \in M_1$, $a \xi_{\omega_1} = 0 \Rightarrow
  a = 0$). Cyclicity is GNS-automatic; separability follows from
  faithfulness of $\omega_1$ (Bost-Connes 1995 Thm 25).
- $P^+$ is the natural positive cone (standard form, §10).

This is a standard form for $M_1$ in the sense of Haagerup (1975). Tomita-Takesaki
theory applies without modification.

## The antilinear operator $S_0$

**Definition 11.1 (unbounded Tomita operator).** Define a map
$$S_0 : M_1 \xi_{\omega_1} \longrightarrow M_1 \xi_{\omega_1}$$
by the rule
$$S_0 \bigl( a \xi_{\omega_1} \bigr) = a^* \xi_{\omega_1}, \qquad a \in M_1.$$
The map $S_0$ is *well-defined* because $\xi_{\omega_1}$ is separating:
if $a \xi_{\omega_1} = b \xi_{\omega_1}$ then $(a-b) \xi_{\omega_1} = 0$,
hence $a = b$, hence $a^* = b^*$, hence $a^* \xi_{\omega_1} = b^*
\xi_{\omega_1}$.

$S_0$ is densely defined (cyclicity of $\xi_{\omega_1}$) and antilinear:
$S_0(\lambda a \xi_{\omega_1}) = (\lambda a)^* \xi_{\omega_1} = \bar\lambda
a^* \xi_{\omega_1} = \bar\lambda \, S_0(a \xi_{\omega_1})$ for $\lambda \in
\mathbb{C}$, $a \in M_1$.

An involution is built in: $S_0^2 = \mathrm{id}$ on the dense domain $M_1
\xi_{\omega_1}$, because $(a^*)^* = a$.

**Remark 11.2 (mirror map for the commutant).** The commutant-side mirror
$$F_0 : M_1' \xi_{\omega_1} \longrightarrow M_1' \xi_{\omega_1}, \qquad
F_0(a' \xi_{\omega_1}) = (a')^* \xi_{\omega_1}$$
is defined analogously (using separability for $M_1'$, which is equivalent
to cyclicity for $M_1$, a standard duality). $F_0$ plays the role of $S_0$
for the commutant and will turn out to be $\bar{S_0}^*$, the adjoint in
the antilinear sense.

## Closability

**Proposition 11.3.** $S_0$ is *closable*, and its closure $\bar{S}$ is an
antilinear operator on $H_{\omega_1}$ with dense domain
$$\mathrm{Dom}(\bar{S}) = \overline{M_1 \xi_{\omega_1}}^{S_0}$$
(closure taken in the graph norm). One also has $\bar{S}^2 = 1$ on
$\mathrm{Dom}(\bar{S}) \cap \bar{S}(\mathrm{Dom}(\bar{S}))$ and $\bar{S}$ is
injective with dense range.

**Proof (sketch).** Closability is equivalent to $F_0 \subseteq S_0^*$
in the antilinear sense: for $a \in M_1$, $a' \in M_1'$,
$$\langle F_0(a' \xi_{\omega_1}), \, a \xi_{\omega_1} \rangle =
\langle (a')^* \xi_{\omega_1}, \, a \xi_{\omega_1} \rangle =
\overline{\omega_1(a a')} = \overline{\omega_1(a' a)} =
\langle \xi_{\omega_1}, \, a^* (a')^* \xi_{\omega_1} \rangle^*$$
(the last equality uses faithfulness of $\omega_1$ and the fact that $a \in
M_1$, $a' \in M_1'$ commute). A careful antilinear-adjoint bookkeeping
(Takesaki Vol II §VI.1, Lemma 1.4) shows that $F_0$ is contained in the
antilinear adjoint of $S_0$, which implies closability. QED.

The closure $\bar{S}$ is the operator Tomita called *the* modular
involution. It is antilinear, densely defined, closed, and satisfies
$\bar{S}^2 \subseteq 1$ (involutive on its domain).

## Polar decomposition

**Theorem 11.4 (Tomita-Takesaki, polar decomposition).** The closed
antilinear operator $\bar{S}$ admits a unique polar decomposition
$$\bar{S} = J \, \Delta^{1/2}$$
in which:

(i) $\Delta$ is a positive self-adjoint (generally unbounded, and here
*genuinely* unbounded because $M_1$ is type III$_1$, hence no finite
trace) linear operator on $H_{\omega_1}$ with $\mathrm{Dom}(\Delta^{1/2}) =
\mathrm{Dom}(\bar{S})$;

(ii) $J$ is an antiunitary involution: antilinear, $\|J\xi\| = \|\xi\|$
for all $\xi \in H_{\omega_1}$, and $J^2 = I$;

(iii) $J$ and $\Delta$ commute in the sense $J \Delta^{1/2} J = \Delta^{-1/2}$,
equivalently $J \Delta = \Delta^{-1} J$;

(iv) $\ker \Delta = \{0\}$ (hence $\log \Delta$ is defined as a self-adjoint
operator on a dense domain via Borel functional calculus).

**Proof.** Apply Tomita's theorem (Tomita 1967; formalized in Takesaki
1970). The construction is: first observe that $\bar{S}^* \bar{S}$ is a
positive self-adjoint operator in the standard sense on
$\mathrm{Dom}(\bar{S})$; call it $\Delta$. Then define $J$ as the
antiunitary given by uniqueness of polar decomposition of a closed
antilinear map: $J := \bar{S} \, \Delta^{-1/2}$ on the appropriate domain,
extended by continuity. The relations (ii), (iii) are then structural
consequences of $\bar{S}^2 = 1$ and the structure of antilinear polar
decomposition. Non-triviality of $\ker \Delta$ would violate the
cyclicity-separability balance between $\xi_{\omega_1}$ and $M_1$, hence
(iv). QED.

Detailed exposition in Takesaki Vol II §VI.1 (Theorem 1.5 and Corollary
1.6); a self-contained treatment in Bratteli-Robinson Vol I §2.5.

## What $\Delta$ means

The operator $\Delta$ is the *modular operator* of the state $\omega_1$.
Intuitively: $\Delta$ measures the *lack of tracial property* of the
state. If $\omega_1$ were a trace (which it is not, since $M_1$ is type
III — no finite trace at all), one would have $\omega_1(ab) = \omega_1(ba)$
and $\Delta = I$. The departure from $\Delta = I$ measures exactly how much
$\omega_1$ fails to commute with the algebra product.

Formally:
$$\omega_1(ab) = \langle \Delta^{1/2} a^* \xi_{\omega_1}, \, b^*
\xi_{\omega_1} \rangle, \qquad a, b \in M_1$$
(Takesaki Vol II §VI.1, Lemma 1.4). When $\omega_1$ is a trace this
reduces to the identity; the genuine $\Delta > 0$ (nontrivial) encodes
the KMS anomaly.

For a type III$_1$ factor, $\Delta$ has *continuous spectrum* equal to
$[0, \infty)$ — in fact, the Connes spectrum $\mathrm{Sd}(M_1) =
\mathbb{R}$ (see §16) is by definition the spectrum of $\log \Delta$
after intersection over all cyclic-separating vectors. For the BC
factor this intersection is already attained at $\xi_{\omega_1}$:
$\mathrm{spec}(\log \Delta) = \mathbb{R}$ on $H_{\omega_1} \ominus
\mathbb{C} \xi_{\omega_1}$.

## Uniqueness

**Proposition 11.5 (uniqueness of modular data).** Let $\xi$ be any
cyclic-separating vector for $M_1$. The associated modular operator
$\Delta_\xi$ and modular conjugation $J_\xi$ are determined by $\xi$ up
to a specified cocycle. Specifically: if $\xi' = u \xi$ for a unitary
$u \in M_1$, then $\Delta_{\xi'} = u \Delta_\xi u^*$ and $J_{\xi'} = u
J_\xi u^*$ (conjugation by the same unitary).

**Proof.** Direct from the definition $S_{\xi'}(a u \xi) = (au)^* \xi =
u^* a^* \xi$, rewritten as $S_{\xi'} = u^* S_\xi u$ on the appropriate
domain. Polar decomposition intertwines as stated. QED.

For Paper 49 we *fix* $\xi = \xi_{\omega_1}$ (the canonical KMS$_1$
vector). All subsequent modular structure is then canonical with respect
to the unique KMS$_1$ state — the only degree of freedom remaining is an
overall phase on $\xi_{\omega_1}$, which does not affect $\Delta$ or $J$
as operators.

## Basic properties we will use

The modular operator $\Delta$ and its associated modular group $\sigma_t
= \mathrm{Ad}(\Delta^{it})$ (§14) enjoy the following properties, all
proven in Takesaki Vol II Ch VI-IX and recorded here for reference:

(P1) $\Delta \xi_{\omega_1} = \xi_{\omega_1}$ (the KMS$_1$ vector is fixed
by $\Delta$, hence is the unique ground state of $\log \Delta$
on its cyclic component).

(P2) $\Delta^{it}$ is a strongly continuous one-parameter group of unitary
operators on $H_{\omega_1}$ for $t \in \mathbb{R}$.

(P3) $\Delta^{it} M_1 \Delta^{-it} = M_1$ for all $t \in \mathbb{R}$
(the modular group preserves the algebra).

(P4) $J M_1 J = M_1'$ (the modular conjugation carries the algebra to its
commutant; see §12).

(P5) The *modular flow* on states — $\omega_1 \circ \sigma_t$ — satisfies
a KMS condition at $\beta = 1$ that is equivalent to the analytic
condition of Kubo, Martin and Schwinger; this is the content of §13.

Properties (P1)-(P4) are the structural content of Tomita-Takesaki
theory. Property (P5) is the *reason* the construction matters for
Paper 49: it links the modular flow to the physical time evolution of
the BC system, and thence (via Link 3 of the chain) to the Weil explicit
formula side (Part V).

## Summary

The unique KMS$_1$ vector $\xi_{\omega_1}$ is cyclic and separating for
$M_1$. The antilinear map $S_0(a \xi_{\omega_1}) = a^* \xi_{\omega_1}$ is
closable; its closure $\bar{S}$ has polar decomposition $\bar{S} = J
\Delta^{1/2}$ with $\Delta > 0$ positive self-adjoint unbounded and $J$
antiunitary. The pair $(\Delta, J)$ is canonical with respect to $\omega_1$
(up to a conjugation in $M_1$) and exhibits the defining properties
(P1)-(P4) above.

This is the raw material for the Hilbert-Pólya operator $D$ of Part IV.

---

*Next: §12 — the modular conjugation $J$, where Tomita-Takesaki theory
meets the functional equation $\xi(s) = \xi(1-s)$. The hinge point of
the paper.*

---

**Primary references.**
Tomita 1967, *Standard forms of von Neumann algebras* (unpublished notes,
Kyushu).
Takesaki 1970, *Tomita's theory of modular Hilbert algebras and its
applications*, Lecture Notes in Math. 128, Springer.
Takesaki, *Theory of Operator Algebras II*, Springer 2003, Chapters VI-IX
(our master reference for the classical machinery).
Bratteli-Robinson, *Operator Algebras and Quantum Statistical Mechanics
I*, §2.5 (self-contained exposition of Tomita-Takesaki).
Haagerup 1975, *The standard form of von Neumann algebras*, Math. Scand.
37.
