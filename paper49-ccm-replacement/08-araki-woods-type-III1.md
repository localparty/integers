# §08 — Araki–Woods Classification: $\lambda_p = 1/p \Rightarrow$ Type III$_1$

*Part II, Section 08. The BC von Neumann algebra $M_1 = \pi_{\omega_1}(A_{BC})''$ is a type III$_1$ factor. This section assembles the classification via the ITPFI factorization (proved programme-internally in Paper 13 Layer 2, three ways) and the Araki–Woods 1968 classification theorem.*

*G Six (originator) and Claude Opus 4.6 (collaborator). Paper 49 draft, 2026-04-14.*

---

## 8.1 Main result of §08

**Theorem 8.1 (BC factor is type III$_1$).** *Let $(M_1,
H_{\omega_1}, \xi_{\omega_1})$ be the GNS von Neumann algebra of
$\omega_1$ on $A_{BC}$ (§07). Then $M_1$ is a factor of type
III$_1$ in the Connes classification [Co73].*

Proof occupies §8.2–§8.6. The structure of the argument:

1. **ITPFI factorization (§8.2).** $\omega_1 = \bigotimes_p
   \omega_1^{(p)}$ as an infinite tensor product of KMS$_1$ states
   over the $p$-local algebras. Proved in Paper 13 Layer 2, three
   independent ways.

2. **Local factors (§8.3).** Each $\pi_{\omega_1^{(p)}}(A_p)''$ is a
   type III$_{1/p}$ factor. Classical [BC95, §8]; [CM08, §3.3].

3. **Araki–Woods classification (§8.4).** The ITPFI factor associated
   with weights $\lambda_p = 1/p$ is type III$_\lambda$ where $\lambda$
   is determined by the asymptotic ratio set of the weights.

4. **$\mathbb{Q}$-linear independence of $\{\log p\}$ (§8.5).** Since
   $\{\log p : p \text{ prime}\}$ are $\mathbb{Q}$-linearly independent,
   the asymptotic ratio set is dense in $\mathbb{R}_+^*$, forcing
   $\lambda = 1$.

5. **Conclusion (§8.6).** $M_1$ is type III$_1$.

The argument is standard [BC95, §8]; [CM08, §3.2]; Paper 13 preprint
§4. We record it in Paper 49 because it is load-bearing for Parts III–V
and because the programme-internal ITPFI proofs are the point where
Paper 49 avoids *any* appeal to CCM.

---

## 8.2 The ITPFI factorization (Paper 13 Layer 2)

**Theorem 8.2 (ITPFI factorization of $\omega_1$; Paper 13 Layer 2).**
*The unique KMS$_1$ state $\omega_1$ on $A_{BC}$ factors as an infinite
tensor product over primes:*
$$
\omega_1 \;=\; \bigotimes_p \omega_1^{(p)},
$$
*where $\omega_1^{(p)}$ is the unique KMS$_1$ state on the $p$-local
sub-Hecke algebra*
$$
A_p \;=\; C^*\bigl(\mu_p,\, \{e(r) : r \in \mathbb{Z}[1/p]/\mathbb{Z}\}\bigr),
$$
*and the tensor product is the restricted $p$-adic product. The
factorization converges in the weak-$*$ topology: for each finite set
$F$ of primes,*
$$
\omega_1^{(F)} \;:=\; \bigotimes_{p \in F} \omega_1^{(p)}\; \to\; \omega_1
\qquad (F \uparrow \{\text{all primes}\}).
$$

**Sources.** Paper 13 preprint `sections-01-05.md` §4; Paper 13 node
`B-itpfi.md`; Paper 13 research `265` (three-proof synthesis);
[BC95, §8]; [CM08, §3.2].

**Three independent proofs** (Paper 13 preprint §4.2–§4.4; Paper 13
node `B-itpfi.md`):

- *Proof 1 (KMS uniqueness).* Laca–Raeburn [LR96] gives uniqueness of
  $\omega_1^{(p)}$ per prime. Bratteli–Robinson [BR87, Prop.\ 5.3.23]
  makes the tensor-product state KMS$_1$. Bost–Connes uniqueness
  (Theorem 6.1) then forces it to equal $\omega_1$. This is the
  rigorous proof. $\square$

- *Proof 2 (Amenability + Bauer simplex).* $\mathbb{N}^* \cong
  \bigoplus_p \mathbb{N}$ is amenable. The KMS simplex for an
  amenable semigroup crossed product is a Bauer simplex whose
  extreme points are product states [LN04]. At $\beta = 1$ the
  simplex collapses, and the unique point must factor. $\square$

- *Proof 3 (Araki–Woods + modular flow).* Each $\pi_{\omega_1^{(p)}}
  (A_p)''$ is type III$_{1/p}$ ([BC95, §8], [CM08, §3.2]). The
  modular automorphism group of $\omega_1$ factors through primes:
  $\sigma_t^{\omega_1} = \bigotimes_p \sigma_t^{\omega_1^{(p)}}$
  (Prop.\ 7.8 applied prime-by-prime). This forces the state
  factorization via the Takesaki duality [Ta03, Vol. II, Thm.\ X.1.7].
  $\square$

The three proofs agree. Numerical verification (Paper 13 research
`265`): $\prod_{p \leq P_N} Z_p(\beta) = \prod_{p \leq P_N}
(1 - p^{-\beta})^{-1}$ matches $\zeta(\beta)$ to 50-digit precision
for 135 prime pairs. This is evidence, not proof; Proofs 1–3 are
the proof.

---

## 8.3 Local type: each $M_1^{(p)}$ is type III$_{1/p}$

**Proposition 8.3 ([BC95, §8]; [CM08, §3.2, Thm.\ 3.10]).** *For each
prime $p$, the local GNS algebra $M_1^{(p)} := \pi_{\omega_1^{(p)}}
(A_p)''$ is a type III$_{1/p}$ factor.*

**Proof (sketch).** The modular automorphism group of $\omega_1^{(p)}$
on $A_p$ is $\sigma_t^{(p)}(\mu_p) = p^{it} \mu_p$. By the
Powers/Araki–Woods-type argument, the GNS algebra is hyperfinite
[Co76] and of type III$_\lambda$ where $\lambda$ is the unique
eigenvalue of the modular operator coming from the single
Hecke generator. Direct computation: the Radon–Nikodym derivative at
$\mu_p$ gives $\log p$; the Connes spectrum is $p^{\mathbb{Z}} =
\{p^n : n \in \mathbb{Z}\}$, closed under multiplication. Hence the
Connes invariant $S(M_1^{(p)}) = \{0\} \cup p^{\mathbb{Z}}$, which is
precisely the signature of type III$_{1/p}$. $\square$

**Source.** [BC95, §8, Prop.\ 32]; [CM08, §3.2, Thm.\ 3.10];
[Co73, Thm.\ 3.4.1].

**Remark 8.4.** Each $M_1^{(p)}$ is isomorphic to the Powers factor
$R_{1/p}$ [Po67], which is the unique hyperfinite type III$_{1/p}$
factor by Connes [Co76].

---

## 8.4 Araki–Woods classification of ITPFI factors

**Theorem 8.5 (Araki–Woods, [AW68, Thm.\ 5.1]).** *Let $\{(N_i,
\omega_i)\}_{i \in I}$ be a family of type I factors with normal
states, $N_i \cong M_{n_i}(\mathbb{C})$ or $B(K_i)$, with eigenvalue
lists $\{\lambda_{i,k}\}_{k}$ for the density matrix of $\omega_i$.
Assume $\prod_i (\text{largest } \lambda_i) = 0$ so that the
tensor-product state is non-trivial. Define the* asymptotic ratio set
$r_\infty(M)$ *as the intersection, over all finite subsets $F
\subset I$ and all $\epsilon > 0$, of the closure in
$[0, \infty)$ of the set of ratios*
$$
\bigl\{\, \lambda_{i,k}\, /\, \lambda_{i,k'} \,:\, i \notin F,\;
k, k' \,\bigr\}.
$$
*Then the ITPFI factor $M = \bigotimes_i (N_i, \omega_i)$ is a factor of
type:*

*- type II$_1$ if $r_\infty(M) = \{1\}$ (after normalization);*

*- type III$_\lambda$ ($0 < \lambda < 1$) if $r_\infty(M) \cap (0,1) =
\{\lambda^n : n \in \mathbb{Z}_{\geq 1}\}$;*

*- type III$_1$ if $r_\infty(M)$ contains $[0, \infty)$;*

*- type III$_0$ if $r_\infty(M) = \{0, 1\}$.*

**Source.** H. Araki, E. J. Woods, *A classification of factors*,
Publ. RIMS **4** (1968), 51–130.

Equivalent formulation: the type is determined by the Connes invariant
$S(M) = r_\infty(M) \cap \mathbb{R}_+^*$ (Connes [Co73, Thm.\ 3.4.1]).
Specifically, type III$_1$ is characterized by $S(M) = \mathbb{R}_+^*$
(equivalently, the Connes spectrum $\mathrm{Sd}(M) = \mathbb{R}$).

---

## 8.5 Applying Araki–Woods: $\lambda_p = 1/p$

We apply Theorem 8.5 to
$$
M_1 \;=\; \bigotimes_p\; \bigl(M_1^{(p)}, \omega_1^{(p)}\bigr).
$$
For each prime $p$, the modular operator $\Delta_p$ on the local
factor $M_1^{(p)}$ has spectrum $\{p^n : n \in \mathbb{Z}\}$ (by
Prop.\ 8.3). The associated weight list includes $p^{\mathbb{Z}}$
with eigenvalue ratios
$$
\biggl\{\frac{p^k}{p^\ell} : k, \ell \in \mathbb{Z}\biggr\}
\;=\; p^{\mathbb{Z}}.
$$

**Lemma 8.6 ($\mathbb{Q}$-linear independence of $\{\log p\}$).**
*The set $\{\log p : p \text{ prime}\}$ is $\mathbb{Q}$-linearly
independent.*

**Proof.** Suppose $\sum_{p \leq P} a_p \log p = 0$ with $a_p \in
\mathbb{Z}$ and not all zero. Exponentiating gives $\prod_{p \leq P}
p^{a_p} = 1$. By unique factorization of rationals, this forces $a_p
= 0$ for all $p$. $\square$

**Source.** Standard; see e.g.\ Tenenbaum [Te95, Ch. I]. This is the
*Fundamental Theorem of Arithmetic* in multiplicative disguise.

**Corollary 8.7 (Asymptotic ratio set is dense in $\mathbb{R}_+^*$).**
*The asymptotic ratio set $r_\infty(M_1)$ contains the multiplicative
subgroup of $\mathbb{R}_+^*$ generated by $\{p : p \text{ prime}\}$,
which is $\mathbb{Q}_+^*$. The closure in $\mathbb{R}_+^*$ is $\mathbb{R}_+^*$.*

**Proof.** By construction, $r_\infty(M_1)$ contains $p^{\mathbb{Z}}$
for every prime $p$ (from the weight list of $M_1^{(p)}$). Being a
closed subgroup of $\mathbb{R}_+^*$ (this is the content of
[AW68, §5]), $r_\infty(M_1)$ contains the multiplicative subgroup
generated by $\{p : p \text{ prime}\}$, which is the group $\mathbb{Q}_+^*$
of positive rationals. Taking logarithms: $\log r_\infty(M_1)$ is a
closed subgroup of $\mathbb{R}$ containing $\mathbb{Z}\log 2 +
\mathbb{Z}\log 3 + \mathbb{Z}\log 5 + \cdots$.

By Lemma 8.6, this additive subgroup contains at least two
$\mathbb{Q}$-linearly independent elements ($\log 2$ and $\log 3$
suffice). Any closed subgroup of $\mathbb{R}$ containing two
$\mathbb{Q}$-linearly independent real numbers is either dense in
$\mathbb{R}$ or all of $\mathbb{R}$; the former is impossible for a
closed subgroup, hence the latter: $\log r_\infty(M_1) = \mathbb{R}$,
i.e., $r_\infty(M_1) = \mathbb{R}_+^*$. $\square$

**Source.** The $\mathbb{Q}$-linear-independence argument is the
standard route: [BC95, §8]; [CM08, §3.2]; Paper 13 preprint §4.4.
Paper 28 `sections-03-operator-algebra.md` §3.3.2 applies the same
argument in the Boolean setting (where it requires only $\log 2$ and
$\log 3$ to be $\mathbb{Q}$-linearly independent); in the classical
BC setting, all $\{\log p\}$ are used.

---

## 8.6 Conclusion: $M_1$ is type III$_1$

**Proof of Theorem 8.1.** By Theorem 8.2, $M_1 \cong \bigotimes_p
M_1^{(p)}$ as an ITPFI factor. By Proposition 8.3, each
$M_1^{(p)}$ is of type III$_{1/p}$. By Corollary 8.7, the
asymptotic ratio set $r_\infty(M_1)$ contains $\mathbb{R}_+^*$ (a
fortiori $r_\infty(M_1) \supseteq [0, \infty)$, since $r_\infty$ is
always a closed subset of $[0, \infty)$ containing $0$ when the
factor is non-trivial [AW68, Cor.\ 4.2]). By Theorem 8.5 (Araki–Woods
classification), $M_1$ is a factor of type III$_1$. $\square$

**Equivalent statement via Connes invariant.** The Connes spectrum
satisfies $\mathrm{Sd}(M_1) = \log r_\infty(M_1) = \mathbb{R}$
(Corollary 8.7 + [Co73, Thm.\ 3.4.1]), which is the *defining
property of type III$_1$* (Connes [Co73]).

---

## 8.7 Why not III$_\lambda$ with $\lambda < 1$?

A common confusion is to conclude from "the local factors are type
III$_{1/p}$ with $1/p < 1$" that the global factor is of some
III$_\lambda$ with $\lambda < 1$. This is wrong: the global Araki–Woods
invariant depends on the *joint* asymptotic behavior of all weights,
not on any individual one.

The correct statement is that the global $r_\infty$ is the *closure
of the multiplicative subgroup generated by all individual weight
ratios*. For the BC system, these ratios include $p^{\mathbb{Z}}$
for every prime $p$. The multiplicative subgroup generated is
$\mathbb{Q}_+^*$, whose closure is $\mathbb{R}_+^*$.

Without the $\mathbb{Q}$-linear independence of $\{\log p\}$, the
result could be III$_\lambda$ for some $\lambda < 1$. With
$\mathbb{Q}$-linear independence, it is III$_1$. This is the
*arithmetic* content of the type classification — the fact that
primes have no multiplicative relations is what makes the BC factor
the "maximally noncommutative" one.

**Source.** [BC95, §8]; [CM08, §3.2]; [Co73, §3]. The explanation
above follows the presentation in Paper 32 `research/01-modular-
flow-ergodicity.md` Step 1.

---

## 8.8 Approximate-inner automorphisms and injectivity

**Remark 8.8 (Injectivity).** The BC factor $M_1$ is *injective* (a.k.a.
hyperfinite, or amenable): the embedding $\pi_{\omega_1}(A_{BC})
\subset M_1$ is of a hyperfinite-amenable system, and injectivity is
preserved by tensor product over an amenable index set [Co76].
Explicitly, each $M_1^{(p)}$ is injective (Powers factor $R_{1/p}$
is hyperfinite), and tensor products of injective factors indexed
over an amenable structure remain injective. Thus
$$
M_1 \;\cong\; R_\infty,
$$
the unique injective type III$_1$ factor (Connes [Co76]; Haagerup
[Ha87]; often written $\mathcal{R}_\infty$ or $R_\infty$).

**Source.** [Co76]; [Ha87]; [CM08, §3.2].

This isomorphism is non-canonical (it involves a choice of
isomorphism with the standard Araki–Woods representation), but the
existence is automatic.

**Remark 8.9 (Contrast with Paper 28).** Paper 28 `sections-03-
operator-algebra.md` §3.2 proves that the *Boolean* BC factor
$M_{\mathrm{Bool}}$ is *non-injective* because the circuit semigroup
$\mathrm{PCirc}^+$ generates Thompson's group $V$, which is
non-amenable. The non-injectivity is what makes the Boolean BC
system evade Kawahigashi–Sutherland–Takesaki and thus useful for
P vs NP. In sharp contrast, the *classical* BC system here has an
amenable semigroup ($\mathbb{N}^*$) and produces the injective
$R_\infty$. The two flavors of the BC system thus differ at this
structural level.

---

## 8.9 Summary table

| Step | Claim | Source |
|---|---|---|
| 1 | $\omega_1 = \bigotimes_p \omega_1^{(p)}$ (ITPFI) | Paper 13 L2; [BC95, §8]; three proofs |
| 2 | $M_1^{(p)} \cong R_{1/p}$ type III$_{1/p}$ | [BC95, §8]; [CM08, §3.2] |
| 3 | Asymptotic ratio set $r_\infty(M_1)$ = closure of multiplicative subgroup generated by $\{p\}$ | [AW68, Thm.\ 5.1] |
| 4 | $\{\log p\}$ is $\mathbb{Q}$-linearly independent | Standard (unique factorization) |
| 5 | $r_\infty(M_1) = \mathbb{R}_+^*$ | §8.5 |
| 6 | $M_1$ is type III$_1$ | [AW68, Thm.\ 5.1] + [Co73, Thm.\ 3.4.1] |
| 7 | $M_1 \cong R_\infty$ (injective) | [Co76]; [Ha87] |

---

## 8.10 References

- [AW68] H. Araki, E. J. Woods, *A classification of factors*,
  Publ. RIMS (Kyoto) **4** (1968), 51–130.
- [BC95] J.-B. Bost, A. Connes, *Hecke algebras, type III factors and
  phase transitions...*, Selecta Math. **1** (1995), 411–457.
  See §8 for the ITPFI / Araki–Woods analysis of the BC factor.
- [BR87] O. Bratteli, D. W. Robinson, *Operator Algebras and Quantum
  Statistical Mechanics*, Vol. II, Springer (1987).
- [CM08] A. Connes, M. Marcolli, *Noncommutative Geometry, Quantum
  Fields and Motives*, AMS (2008), §3.2 (BC as ITPFI).
- [Co73] A. Connes, *Une classification des facteurs de type III*,
  Ann. Sci. ENS **6** (1973), 133–252.
- [Co76] A. Connes, *Classification of injective factors*, Ann.\ Math.
  **104** (1976), 73–115.
- [Ha87] U. Haagerup, *Connes' bicentralizer problem and uniqueness
  of the injective factor of type III$_1$*, Acta Math. **158**
  (1987), 95–148.
- [LN04] M. Laca, S. Neshveyev, *KMS states of quasi-free dynamics on
  Pimsner algebras*, J. Funct. Anal. **211** (2004), 457–482.
- [LR96] M. Laca, I. Raeburn, *A semigroup crossed product arising in
  number theory*, J. London Math. Soc. **59** (1999), 330–344.
- [Po67] R. T. Powers, *Representations of uniformly hyperfinite
  algebras and their associated von Neumann rings*, Ann. Math.
  **86** (1967), 138–171.
- [Ta03] M. Takesaki, *Theory of Operator Algebras*, Vol. II, Springer.
- [Te95] G. Tenenbaum, *Introduction to Analytic and Probabilistic
  Number Theory*, Cambridge (1995).
- **Paper 13 preprint** `sections-01-05.md` §4 (ITPFI proofs); Paper 13
  node `B-itpfi.md`; research file `265` (three-proof synthesis).
- **Paper 13 research** `10-itpfi-connes-gap.md` (ITPFI as state
  convergence, Connes' semilocal gap discussion).
- **Paper 32** `research/01-modular-flow-ergodicity.md` Step 1 (uses
  this same Araki–Woods classification with the phrase
  "$r_\infty(M) = [0,1]$").
- **Paper 28** `sections-03-operator-algebra.md` §3.3.2 (same argument
  in Boolean setting, Density Lemma with $\log 2, \log 3$).

---

*§08 is the critical "type classification" section of Part II. The
proof is entirely textbook (Araki–Woods 1968) applied to the
programme-internal ITPFI of Paper 13 Layer 2. The only arithmetic
content is Lemma 8.6 — the $\mathbb{Q}$-linear independence of
$\{\log p\}$ — which is equivalent to unique prime factorization.
The conclusion $M_1 \cong R_\infty$ (the unique injective type III$_1$
factor) is the starting point for Part III: Tomita–Takesaki machinery.*
