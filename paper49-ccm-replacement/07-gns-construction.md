# §07 — GNS Construction from $\omega_1$

*Part II, Section 07. The Gelfand–Naimark–Segal construction converts the state $\omega_1$ into a Hilbert-space representation. This is standard material; the only programme-specific content is the observation that uniqueness of $\omega_1$ (§06) makes the construction canonical.*

*G Six (originator) and Claude Opus 4.6 (collaborator). Paper 49 draft, 2026-04-14.*

---

## 7.1 The GNS theorem

**Theorem 7.1 (Gelfand–Naimark–Segal, [Ta03, Vol. I, Thm.\ I.9.14]).**
*Let $A$ be a unital C*-algebra and $\omega$ a state on $A$. Then
there exists a triple $(\pi_\omega, H_\omega, \xi_\omega)$ consisting
of*

*(i) a Hilbert space $H_\omega$,*

*(ii) a cyclic vector $\xi_\omega \in H_\omega$ with $\|\xi_\omega\| = 1$,*

*(iii) a *-representation $\pi_\omega : A \to B(H_\omega)$,*

*such that $\pi_\omega(A) \xi_\omega$ is dense in $H_\omega$ and*
$$
\omega(a) \;=\; \bigl\langle\, \xi_\omega,\, \pi_\omega(a)\, \xi_\omega
\,\bigr\rangle, \qquad a \in A.
$$
*The triple is unique up to unitary equivalence.*

**Source.** Gelfand–Naimark 1943; Segal 1947; Takesaki [Ta03, Vol. I,
§I.9]; Bratteli–Robinson [BR87, Vol. I, §2.3.3].

---

## 7.2 Application to $\omega_1$

Apply Theorem 7.1 to $A = A_{BC}$ (the Bost–Connes C*-algebra, §05)
and $\omega = \omega_1$ (the unique KMS$_1$ state, §06). We obtain:

**Definition 7.2 (Canonical GNS data).** The *canonical GNS triple*
of the Bost–Connes system at KMS$_1$ is
$$
\bigl(\pi_{\omega_1},\; H_{\omega_1},\; \xi_{\omega_1}\bigr),
$$
with:

- $H_{\omega_1}$: the GNS Hilbert space, a separable or
  non-separable Hilbert space (see Rem.\ 7.3 below).
- $\xi_{\omega_1} \in H_{\omega_1}$: the canonical cyclic vector,
  $\|\xi_{\omega_1}\| = 1$.
- $\pi_{\omega_1} : A_{BC} \to B(H_{\omega_1})$: a *-representation
  with $\overline{\pi_{\omega_1}(A_{BC}) \xi_{\omega_1}} =
  H_{\omega_1}$.

By KMS$_1$ uniqueness (§06, Theorem 6.1), this triple is unique up to
unitary equivalence. The construction is therefore *canonical*.

**Remark 7.3 (Separability).** The separability of $H_{\omega_1}$
depends on the presentation of $A_{BC}$. If one takes $A_{BC}$ in its
separable norm-closure presentation, $H_{\omega_1}$ is separable. If
one works with the *multiplier* algebra or with the full non-separable
C*-algebra $C(\hat{\mathbb{Z}}) \rtimes \mathbb{N}^*$, the GNS
Hilbert space may be non-separable. Paper 32 L2
(`paper32-bgs-spectral-statistics/research/01-modular-flow-
ergodicity.md`, Remark after Step 2) explicitly notes the
non-separability of the predual and circumvents it. Paper 49 uses
whichever presentation is convenient and tracks separability where it
matters (e.g., in the classification of type III factors, §08).

---

## 7.3 Explicit construction

For transparency we recall the construction. Define a sesquilinear form
on $A_{BC}$ by
$$
\langle a, b \rangle_{\omega_1} \;:=\; \omega_1(a^* b), \qquad
a, b \in A_{BC}.
$$
The associated semi-norm $\|a\|_{\omega_1} = \omega_1(a^* a)^{1/2}$
defines a subspace
$$
N_{\omega_1} \;=\; \{a \in A_{BC} : \omega_1(a^* a) = 0\}
$$
(the *Gelfand kernel*), which is a left ideal of $A_{BC}$. The quotient
$A_{BC} / N_{\omega_1}$ is a pre-Hilbert space; its completion is
$H_{\omega_1}$.

- $\xi_{\omega_1}$ is the image of $1 \in A_{BC}$ under the quotient
  map $A_{BC} \to A_{BC} / N_{\omega_1} \hookrightarrow H_{\omega_1}$.
- $\pi_{\omega_1}(a)$ acts by left multiplication: $\pi_{\omega_1}(a)
  [b] := [ab]$, where $[b] \in A_{BC}/N_{\omega_1}$.

Left multiplication extends to a bounded operator on $H_{\omega_1}$
because $\omega_1$ is a positive, normalized functional on $A_{BC}$
with $\|\pi_{\omega_1}(a)\| \leq \|a\|$.

**Source.** [Ta03, Vol. I, Thm.\ I.9.14]; [BR87, Vol. I, §2.3.3].

**Remark 7.4 (Faithfulness).** $\omega_1$ is a *faithful* state on
$A_{BC}$: $\omega_1(a^* a) = 0 \Rightarrow a = 0$. This follows from
the fact that the restriction of $\omega_1$ to $C(\hat{\mathbb{Z}}) \subset
A_{BC}$ is the Haar probability measure on $\hat{\mathbb{Z}}$, which is
faithful on $C(\hat{\mathbb{Z}})$; together with the Hecke relations
(5.3), this propagates to faithfulness on $A_{BC}$. Equivalently,
the Gelfand kernel is trivial: $N_{\omega_1} = \{0\}$. Consequently
$A_{BC}$ embeds isometrically into $H_{\omega_1}$ via the GNS map
[BC95, §3]; [CM08, §3.2].

---

## 7.4 The bicommutant $M_1 = \pi_{\omega_1}(A_{BC})''$

**Definition 7.5 (Von Neumann algebra $M_1$).**
$$
M_1 \;:=\; \pi_{\omega_1}(A_{BC})''
\;\subset\; B(H_{\omega_1}),
$$
the *bicommutant* of $\pi_{\omega_1}(A_{BC})$ inside the bounded-
operator algebra on $H_{\omega_1}$.

By von Neumann's bicommutant theorem [vN29] (see [Ta03, Vol. I,
Thm.\ II.3.9]), $M_1$ is the weak-operator (equivalently $\sigma$-weak,
strong-operator, or $\sigma$-strong) closure of $\pi_{\omega_1}(A_{BC})$
in $B(H_{\omega_1})$, and it is a von Neumann algebra.

**Remark 7.6 (Notation).** We write $M_1$ for this von Neumann
algebra because it is the KMS$_1$ object (distinguishing from the
$M_\beta$ that would arise from KMS$_\beta$ states for $\beta \neq 1$).
Throughout Parts III–V of Paper 49, $M_1$ refers exclusively to this
object.

---

## 7.5 Extension of $\omega_1$ to a normal state on $M_1$

**Proposition 7.7 (Normal extension of $\omega_1$).** *The state
$\omega_1$ extends to a faithful normal state $\tilde{\omega}_1$ on
$M_1$, given by*
$$
\tilde{\omega}_1(x) \;=\; \bigl\langle \xi_{\omega_1}, x\,
\xi_{\omega_1} \bigr\rangle, \qquad x \in M_1.
$$

**Proof.** The formula defines a normal state on $B(H_{\omega_1})$
(vector states are normal). Its restriction to $M_1$ extends
$\omega_1$: for $a \in A_{BC}$,
$$
\tilde{\omega}_1(\pi_{\omega_1}(a)) = \bigl\langle \xi_{\omega_1},
\pi_{\omega_1}(a) \xi_{\omega_1} \bigr\rangle = \omega_1(a)
$$
by the GNS relation. Faithfulness follows from faithfulness of
$\omega_1$ on $A_{BC}$ (Rem.\ 7.4) and density of
$\pi_{\omega_1}(A_{BC})$ in $M_1$. $\square$

**Convention.** Throughout Paper 49 we drop the tilde and write
$\omega_1$ for both the original state on $A_{BC}$ and its normal
extension to $M_1$, since the two are the same on the dense
subalgebra $\pi_{\omega_1}(A_{BC})$.

**Source.** [Ta03, Vol. II, §VI.1]; [BR87, Vol. I, §2.4].

---

## 7.6 The modular automorphism group

**Proposition 7.8 (Modular automorphism group of $\omega_1$).** *The
one-parameter automorphism group $\sigma_t$ of $A_{BC}$ (Def.\ 5.5)
extends to a $\sigma$-weakly continuous one-parameter automorphism
group $\sigma_t^{\omega_1}$ of $M_1$, given on $\pi_{\omega_1}(A_{BC})$
by*
$$
\sigma_t^{\omega_1}\bigl(\pi_{\omega_1}(a)\bigr) \;=\;
\pi_{\omega_1}\bigl(\sigma_t(a)\bigr), \qquad a \in A_{BC}.
$$

**Proof.** The KMS condition for $\omega_1$ with respect to $\sigma_t$
lifts to the normal extension on $M_1$ [BR87, Vol. II, Prop.\ 5.3.10].
Specifically, the group $\{\sigma_t^{\omega_1}\}$ is the *modular
automorphism group* of $\omega_1$ on $M_1$ in the Tomita–Takesaki
sense (Part III of Paper 49). For now we take the statement of
Prop.\ 7.8 as a black box; its connection to the modular operator
$\Delta$ is §14. $\square$

**Source.** [BR87, Vol. II, §5.3]; [Ta03, Vol. II, §VIII.1].

**Remark 7.9.** In Takesaki's formulation, the KMS condition is
equivalent to the statement that $\sigma_t^{\omega_1}$ is the modular
automorphism group of $\omega_1$ [Ta03, Vol. II, Thm.\ VIII.1.2].
This equivalence is the bridge between statistical mechanics (KMS) and
operator algebras (Tomita–Takesaki).

---

## 7.7 Cyclicity of $\xi_{\omega_1}$ for $M_1$

**Proposition 7.10 (Cyclicity).** *The vector $\xi_{\omega_1}$ is
cyclic for $M_1$ in $H_{\omega_1}$, i.e.,*
$$
\overline{M_1 \xi_{\omega_1}} \;=\; H_{\omega_1}.
$$

**Proof.** By construction, $\pi_{\omega_1}(A_{BC}) \xi_{\omega_1}$ is
dense in $H_{\omega_1}$. Since $M_1 \supseteq \pi_{\omega_1}(A_{BC})$,
we have $M_1 \xi_{\omega_1} \supseteq \pi_{\omega_1}(A_{BC})
\xi_{\omega_1}$, hence $\overline{M_1 \xi_{\omega_1}} = H_{\omega_1}$.
$\square$

Separating-ness of $\xi_{\omega_1}$ is non-trivial and follows from
the fact that $M_1$ is a type III factor (cf. §08). We postpone the
proof of separating-ness to §09–§10.

**Source.** [Ta03, Vol. II, Lemma VI.1.5 and Prop.\ IX.1.3].

---

## 7.8 Summary: output of §07

We have extracted, from the unique KMS$_1$ state $\omega_1$ of §06, the
following canonical data:

| Object | Symbol | Origin |
|---|---|---|
| GNS Hilbert space | $H_{\omega_1}$ | §07.2 |
| GNS cyclic vector | $\xi_{\omega_1}$, $\|\xi_{\omega_1}\| = 1$ | §07.2 |
| GNS representation | $\pi_{\omega_1} : A_{BC} \to B(H_{\omega_1})$ | §07.2 |
| BC von Neumann algebra | $M_1 = \pi_{\omega_1}(A_{BC})''$ | §07.4 |
| Normal extension | $\omega_1 : M_1 \to \mathbb{C}$ | §07.5 |
| Modular automorphisms | $\sigma_t^{\omega_1} : M_1 \to M_1$ | §07.6 |

All of this is uniquely determined by $(A_{BC}, \sigma_t, \omega_1)$
up to unitary equivalence, hence canonical.

**Outlook.** In §08 we classify $M_1$ as a type III$_1$ factor. In
§09 we prove $M_1$ is a factor (trivial center). In §10 we put
$M_1$ in standard form $(M_1, H_{\omega_1}, J, P^+)$. Part III then
constructs the Tomita–Takesaki data $(\Delta, J)$ that carry the
Hilbert–Pólya operator.

---

## 7.9 References

- [BR87] O. Bratteli, D. W. Robinson, *Operator Algebras and Quantum
  Statistical Mechanics*, Vol. I and II, Springer (1987).
- [BC95] J.-B. Bost, A. Connes, *Hecke algebras, type III factors and
  phase transitions...*, Selecta Math. **1** (1995), 411–457.
- [CM08] A. Connes, M. Marcolli, *Noncommutative Geometry, Quantum
  Fields and Motives*, AMS (2008).
- [Ta03] M. Takesaki, *Theory of Operator Algebras*, Vols. I–III,
  Springer (2003). Vol. I §I.9 for GNS; Vol. II §VI for modular
  theory.
- [vN29] J. von Neumann, *Zur Algebra der Funktionaloperationen und
  Theorie der normalen Operatoren*, Math. Ann. **102** (1929),
  370–427. (Bicommutant theorem.)
- Paper 13 preprint `sections-01-05.md` §2.1 (GNS triple
  $(H_1, \pi_1, \Omega_1)$, equivalent notation).
- Paper 32 `research/01-modular-flow-ergodicity.md` (non-separability
  discussion).
- Paper 28 `sections-03-operator-algebra.md` §3.2 (classical-vs-
  Boolean GNS discussion, for contrast).

---

*§07 is entirely textbook material (GNS + bicommutant). The only
programme-specific item is Prop.\ 7.8, which uses KMS$_1$ from §06
to promote the BC time evolution to the modular automorphism group
on $M_1$ — the starting point for Part III.*
