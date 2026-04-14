# §09 — Factoriality of $M_1$

*Part II, Section 09. $M_1 = \pi_{\omega_1}(A_{BC})''$ is a factor: its center is trivial, $Z(M_1) = \mathbb{C} \cdot 1$. This follows from KMS$_1$ uniqueness (§06) via an ergodic argument. The result is required both by the type III$_1$ classification (§08 implicitly) and by the Tomita–Takesaki standard-form machinery (§10).*

*G Six (originator) and Claude Opus 4.6 (collaborator). Paper 49 draft, 2026-04-14.*

---

## 9.1 Statement

**Theorem 9.1 (Factoriality of $M_1$).** *The von Neumann algebra*
$$
M_1 \;=\; \pi_{\omega_1}(A_{BC})'' \;\subset\; B(H_{\omega_1})
$$
*is a factor: $Z(M_1) := M_1 \cap M_1' = \mathbb{C} \cdot 1$.*

This is strictly stronger than what §08 gives, since the type III$_1$
classification applies to factors. §08 implicitly assumed
factoriality; this section supplies the proof.

---

## 9.2 The ergodic argument: uniqueness of $\omega_1$ forces factoriality

**Proof of Theorem 9.1.** Suppose, for contradiction, that $M_1$ is
not a factor. Then there exists a central projection $P \in Z(M_1)$
with $P \neq 0, 1$. We shall derive a contradiction to Bost–Connes
Theorem 25 (Theorem 6.1).

**Step 1 (Decomposition of $\omega_1$).** Since $P$ is central and
$P \in M_1$, both $P$ and $1 - P$ define restriction maps. Set
$$
\omega^+ \;:=\; \frac{1}{\omega_1(P)}\,\omega_1(P \cdot P),
\qquad
\omega^- \;:=\; \frac{1}{\omega_1(1-P)}\,\omega_1\bigl((1-P) \cdot
(1-P)\bigr),
$$
viewed as states on $A_{BC}$ via pullback through $\pi_{\omega_1}$.
Since $\omega_1$ is faithful (Remark 7.4) and $P \neq 0, 1$, both
$\omega_1(P) \in (0, 1)$ and $\omega_1(1 - P) \in (0, 1)$ are strictly
positive. Hence $\omega^+$ and $\omega^-$ are well-defined states.

We have the convex decomposition
$$
\omega_1 \;=\; \omega_1(P) \cdot \omega^+ \;+\; \omega_1(1-P)
\cdot \omega^-,
$$
a non-trivial convex combination (both coefficients strictly positive,
and $\omega^+ \neq \omega^-$ because $P$ and $1 - P$ cut out distinct
subrepresentations).

**Step 2 ($\omega^\pm$ are KMS$_1$).** We claim that both $\omega^+$
and $\omega^-$ are KMS$_1$ states. Since $P$ is central in $M_1$,
$P$ commutes with the modular automorphism group $\sigma_t^{\omega_1}$:
if $u_t := \Delta^{it}$ implements $\sigma_t^{\omega_1}$, then $u_t P
u_t^* = P$ because $\sigma_t^{\omega_1}(Z(M_1)) = Z(M_1)$ and
$\sigma_t^{\omega_1}$ restricted to the abelian center is trivial on
each central projection (by the classification of $\sigma_t$-invariant
projections; see [Ta03, Vol. II, Lemma VIII.1.3]). Hence $P$ is
$\sigma_t^{\omega_1}$-invariant.

Given that $P$ is $\sigma_t^{\omega_1}$-invariant, the KMS condition
restricts: for $a, b \in A_{BC}$ analytic,
$$
\omega^+(a \sigma_t(b))\;=\;\frac{\omega_1(P a \sigma_t(b))}{\omega_1(P)}
\;=\;\frac{\omega_1(P a P \sigma_t(P b P))}{\omega_1(P)},
$$
and analytic continuation in $t$ of the function $F_{a,b}^+$ satisfies
the KMS$_1$ boundary identity
$F_{a,b}^+(t + i) = \omega^+(\sigma_t(b) a)$ because $\omega_1$ does
and the cut-down by $P$ preserves analyticity. Hence $\omega^+$ is
KMS$_1$. The same argument shows $\omega^-$ is KMS$_1$.

**Step 3 (Contradiction).** By Step 2, both $\omega^+$ and $\omega^-$
are KMS$_1$ states on $A_{BC}$. By Step 1, $\omega^+ \neq \omega^-$.
But Bost–Connes Theorem 25 (Theorem 6.1) says the KMS$_1$ state is
*unique*. Contradiction.

Hence the assumption "$M_1$ is not a factor" is false. $Z(M_1) =
\mathbb{C} \cdot 1$. $\square$

---

## 9.3 Source check

The argument above is the standard "KMS uniqueness $\Rightarrow$
factoriality" route in operator algebras. Specifically:

- The general principle (that a unique KMS state on a C*-dynamical
  system gives a factorial GNS representation) is [BR87, Vol. II,
  Theorem 5.3.30(3)]: *If $\omega$ is an extremal KMS$_\beta$ state,
  then $\pi_\omega(A)''$ is a factor.* The KMS$_1$ state $\omega_1$
  is automatically extremal because it is unique (the KMS$_\beta$
  state space is a face of $S(A)$, so uniqueness implies
  extremality).

- The explicit statement for the BC algebra appears in Bost–Connes
  [BC95, Theorem 25]: the KMS$_1$ state is unique, and the
  corresponding GNS factor is of type III$_1$ (so in particular is
  a factor).

- Paper 32 `research/01-modular-flow-ergodicity.md` Step 1 gives
  exactly this argument: "*That $M$ is a factor ($Z(M) = \mathbb{C}
  \cdot 1$) follows from uniqueness of KMS$_1$: a non-trivial central
  projection would decompose $\omega_1$ as a non-trivial convex
  combination of KMS$_1$ states, contradicting uniqueness*."

- Paper 28 `sections-03-operator-algebra.md` §3.3.2 Step 4: "*If
  $\omega_1^{\mathrm{Bool}}$ is extremal among KMS$_1$ states, then
  $M_{\mathrm{Bool}}$ is a factor by Bratteli–Robinson II,
  Theorem 5.3.30.*"

- [Co94, Prop.\ V.11]: the same principle, stated for general
  C*-dynamical systems.

All four sources give the same argument. Paper 49 inherits it
directly.

---

## 9.4 Extremality via uniqueness

**Proposition 9.2 (Uniqueness $\Rightarrow$ extremality).** *In a
convex face of a weak-$*$ compact convex set $K$, a unique point is
automatically extremal. In particular, the KMS$_1$ state $\omega_1$ on
$A_{BC}$ is an extremal KMS$_1$ state.*

**Proof.** The set of KMS$_\beta$ states on $A$ is a weak-$*$ compact
convex face of the state space $S(A)$ [BR87, Prop.\ 5.3.23]. If the
KMS$_\beta$ state space is a single point $\{\omega_0\}$, then
$\omega_0$ is trivially extremal in that singleton (any "decomposition"
of $\omega_0$ must be trivial). $\square$

**Source.** Standard; [BR87, Vol. II, §5.3].

**Consequence.** The hypothesis of [BR87, Thm.\ 5.3.30(3)] is met:
$\omega_1$ is extremal KMS$_1$. Hence $M_1$ is a factor, as claimed.

---

## 9.5 Consequence: $\xi_{\omega_1}$ is cyclic and separating

**Corollary 9.3 (Separating property of $\xi_{\omega_1}$).** *The
vector $\xi_{\omega_1} \in H_{\omega_1}$ is both cyclic and separating
for $M_1$:*

*(a) Cyclic: $\overline{M_1 \xi_{\omega_1}} = H_{\omega_1}$ (Prop.\ 7.10).*

*(b) Separating: for $x \in M_1$, $x \xi_{\omega_1} = 0$ implies $x =
0$.*

**Proof.** Cyclicity is Proposition 7.10. For the separating property:
the vector state $\omega_1(x) = \langle \xi_{\omega_1}, x \xi_{\omega_1}
\rangle$ is faithful on $M_1$ (Prop.\ 7.7: faithfulness of the normal
extension). If $x \xi_{\omega_1} = 0$, then $\omega_1(x^* x) =
\langle x \xi_{\omega_1}, x \xi_{\omega_1} \rangle = 0$, so by
faithfulness $x^* x = 0$, hence $x = 0$. $\square$

**Source.** Standard; [Ta03, Vol. II, Lemma VI.1.5]: a faithful normal
state has a cyclic and separating GNS representing vector for the
GNS von Neumann algebra. The factor property is what makes
faithfulness of the *vector state* hold; the cyclic-separating
property then follows.

**Remark 9.4.** Without factoriality, $\xi_{\omega_1}$ would still be
cyclic for $M_1$ but might fail to be separating. The combination
"cyclic AND separating" is what Tomita–Takesaki theory requires (Part
III of Paper 49). Corollary 9.3 is therefore load-bearing for §10 and
for the construction of the modular operator in §11.

---

## 9.6 Bypass: factoriality without Tomita–Takesaki

We record a second route to factoriality, independent of the argument
in §9.2, for robustness. The type III$_1$ classification of §08
implicitly gives factoriality: the ITPFI factor associated with any
non-trivial ratio set is always a factor [AW68, Thm.\ 5.1].

**Proposition 9.5 (Factoriality via ITPFI, [AW68, Thm.\ 5.1]).** *An
ITPFI factor $M = \bigotimes_i (N_i, \omega_i)$ of type I factors with
at least one non-trivial state is a factor of some type
(II$_1$, II$_\infty$, III$_\lambda$, III$_0$, or III$_1$).*

Applying this to §08: $M_1 \cong \bigotimes_p (M_1^{(p)},
\omega_1^{(p)})$ is an ITPFI factor in the Araki–Woods sense, hence
*automatically a factor* by [AW68, Thm.\ 5.1]. We do not need the
ergodic argument of §9.2 for factoriality itself; we need it only to
*identify* the factor as the BC GNS algebra (which the ITPFI
factorization of §08 does).

**Summary.** Factoriality has two proofs:

- **Proof A (ergodic, §9.2):** KMS$_1$ uniqueness + central projection
  decomposition.
- **Proof B (ITPFI, §9.6):** Araki–Woods "ITPFI $\Rightarrow$ factor".

Both are clean. Proof A is needed for Paper 28's setting (where the
Boolean BC system's ITPFI classification is not always available); in
the classical case, Proof B is simpler. Paper 49 uses Proof A as
primary because it is closer to the overall narrative (Paper 32's
BGS L2 also uses Proof A).

---

## 9.7 Cross-reference to Paper 28 KEY LEMMA 3.4.3

Paper 28's KEY LEMMA 3.4.3 (`sections-03-operator-algebra.md` §3.3)
proves existence + type III$_1$ classification for the *Boolean* BC
system. The *factoriality* claim there (Step 4 of §3.3.2) reads:
"*If $\omega_1^{\mathrm{Bool}}$ is extremal among KMS$_1$ states, then
$M_{\mathrm{Bool}}$ is a factor by Bratteli–Robinson II,
Theorem 5.3.30. If $\omega_1^{\mathrm{Bool}}$ is not extremal,
decompose into extremal components; each component gives a type
III$_1$ factor by the same Connes spectrum argument.*"

Paper 28's setting is harder than Paper 49's because KMS$_1$
uniqueness for the Boolean BC system is *conjectural* (Paper 28
Conjecture 3.3.1). Paper 49's setting is easier because uniqueness is
*proved* (Bost–Connes Theorem 25), so we are in the "extremal" branch
of Paper 28's argument, and the conclusion is unconditional.

**Source.** Paper 28 `sections-03-operator-algebra.md` §3.3.2, Step 4;
[BR87, Thm.\ 5.3.30(3)]; [BC95, Thm.\ 25].

---

## 9.8 References

- [AW68] H. Araki, E. J. Woods, *A classification of factors*,
  Publ. RIMS **4** (1968), 51–130. Theorem 5.1 (an ITPFI factor is
  a factor).
- [BC95] J.-B. Bost, A. Connes, *Hecke algebras, type III factors...*,
  Selecta Math. **1** (1995), 411–457. Theorem 25 (KMS$_1$
  uniqueness).
- [BR87] O. Bratteli, D. W. Robinson, *Operator Algebras and Quantum
  Statistical Mechanics*, Vol. II, Springer (1987). Theorem 5.3.30(3)
  (extremal KMS $\Rightarrow$ factorial GNS).
- [Co73] A. Connes, *Une classification des facteurs de type III*,
  Ann. Sci. ENS **6** (1973), 133–252.
- [Co94] A. Connes, *Noncommutative Geometry*, Academic Press (1994),
  Prop.\ V.11.
- [Ta03] M. Takesaki, *Theory of Operator Algebras*, Vol. II, Springer
  (2003). Lemma VI.1.5 (faithful normal state $\Rightarrow$ cyclic
  and separating vector).
- Paper 28 `sections-03-operator-algebra.md` §3.3.2, Step 4.
- Paper 32 `research/01-modular-flow-ergodicity.md` Step 1.

---

*§09 closes the factoriality gap that §08 assumed. The argument is
two sentences long modulo the KMS machinery: unique KMS$_1$ state
(Bost–Connes) $\Rightarrow$ extremal KMS$_1$ state (trivially)
$\Rightarrow$ factorial GNS ([BR87, Thm.\ 5.3.30(3)]). The alternative
ITPFI proof (§9.6) gives the same conclusion via Araki–Woods. The
consequence — cyclic and separating $\xi_{\omega_1}$ (Cor.\ 9.3) — is
the hypothesis of Tomita–Takesaki standard-form theory in §10.*
