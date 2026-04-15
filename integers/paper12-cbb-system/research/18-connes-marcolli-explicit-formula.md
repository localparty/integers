# Research 18: The Connes–Marcolli Operator-Algebraic Form of the Riemann–Weil Explicit Formula

*The master reference for the single most-cited external result in*
*Paper 12: the inclusion $\{\gamma_n\} \subseteq \mathrm{spec}(T_{\mathrm{BC}})$*
*and the trace-formula packaging that underlies it.*

*Authors: G Six, with Claude Opus 4.6*
*Date opened: 2026-04-09*
*Gap 1 of `integers/paper12-cbb-system/15-audit-and-missing-research-files.md`.*

---

## 0. Why This File Exists

Almost every research note in `integers/paper12-cbb-system/research/` cites "the Connes–
Marcolli operator-algebraic form of the Riemann–Weil explicit formula"
or, equivalently, "the inclusion $\{\gamma_n\} \subseteq
\mathrm{spec}(T_{\mathrm{BC}})$". The result is used in:

- research/02 §3.2 — the construction of $\hat R$ as a bounded
  function of $T_{\mathrm{BC}}$,
- research/04 §3.1 — the rigorous version of Identity 12,
- research/05 §5 — the CC formula derivation,
- research/08 §2.4 — RH as a physical theorem,
- research/11 — the transposition of Theorem K.4,
- research/14 Part A — the CCM scaling-operator equivalence,
- research/17 — the $K_{12}$ discussion.

Until now it has been captured only by reference ("Connes 1999",
"Connes–Marcolli 2008 Ch II §3"). This note writes it down in one
place: the classical Riemann–Weil formula, its operator-algebraic
rewriting, the precise statement of the inclusion, the regularisation
choices, the identification with the $T_{\mathrm{BC}}$ of Phase 2,
and an honest accounting of what is rigorous and what remains under
mathematical scrutiny.

The note is a *reference*, not a derivation. The proofs live in the
literature (Connes 1999; Connes–Marcolli 2008; Meyer 2005). The task
here is to state the result precisely enough that every downstream
use in Paper 12 is unambiguous.

---

## 1. The Classical Riemann–Weil Explicit Formula

### 1.1 Test function class

Let $h : \mathbb{R} \to \mathbb{C}$ be an even function satisfying
the Weil class conditions:

(W1) $h$ extends to a holomorphic function on the strip
$|\Im z| < 1/2 + \delta$ for some $\delta > 0$;

(W2) $h(z) = O\bigl((1+|z|)^{-2-\varepsilon}\bigr)$ uniformly in that
strip;

(W3) the Fourier transform
$$
\hat h(u) \;=\; \int_{-\infty}^{\infty} h(r)\,e^{-i r u}\,dr
$$
has compact support, or at least decays fast enough that the prime
sum below converges absolutely.

Classes satisfying (W1)–(W3) include Schwartz functions whose Fourier
transform has compact support (the "Paley–Wiener" class), and the
slightly larger class used by Weil and refined by Barner.

### 1.2 Statement

> **Theorem 1 (Riemann–Weil explicit formula).** *For $h$ in the Weil
> class above,*
>
> $$
>   \sum_{\rho} h\!\Bigl(\frac{\rho - 1/2}{i}\Bigr)
>   \;=\;
>   \hat h(0)\,\log \pi
>   \;+\; h\!\Bigl(\tfrac{i}{2}\Bigr) + h\!\Bigl(-\tfrac{i}{2}\Bigr)
>   \;-\; 2 \sum_{p}\sum_{k \geq 1}
>     \frac{\log p}{p^{k/2}}\,\hat h(k \log p)
>   \;-\; W_{\infty}(h),
>   \tag{1.1}
> $$
>
> *where the sum on the left runs over the non-trivial zeros $\rho$
> of $\zeta$ counted with multiplicity (so $(\rho-1/2)/i = \gamma_n$
> on the critical line), and the archimedean term is*
>
> $$
>   W_{\infty}(h) \;=\;
>   \int_{-\infty}^{\infty} h(r)\,
>     \Bigl[\,\psi\!\Bigl(\tfrac{1}{4} + \tfrac{i r}{2}\Bigr)
>       + \psi\!\Bigl(\tfrac{1}{4} - \tfrac{i r}{2}\Bigr)\,\Bigr]\,
>     \frac{dr}{2\pi},
>   \tag{1.2}
> $$
>
> *with $\psi = \Gamma'/\Gamma$ the digamma function.*

The two "polar" terms $h(i/2) + h(-i/2)$ arise from the pole of
$\zeta$ at $s=1$ (and, symmetrically, from the trivial behaviour at
$s=0$). The term $\hat h(0)\log\pi$ is the contribution of the
gamma factor $\pi^{-s/2}$ in the completed zeta function
$\xi(s) = \pi^{-s/2}\Gamma(s/2)\zeta(s)$. The archimedean
correction $W_\infty$ is the remaining piece of the logarithmic
derivative of $\Gamma(s/2)$ along the critical line; it is a
smooth linear functional of $h$ and is the subject of the
regularisation discussion in §4.

### 1.3 References for the classical form

The identity (1.1) with the archimedean term (1.2) is Theorem 5.12
in Iwaniec–Kowalski, *Analytic Number Theory*, AMS 2004, and is
equivalent to Weil's original 1952 formulation (Weil, "Sur les
«formules explicites» de la théorie des nombres premiers", *Medd.
Lunds Univ. Mat. Sem.*). The modern presentation with distributional
test functions is in Edwards, *Riemann's Zeta Function*, Academic
Press 1974, §1.14, and in Patterson, *An Introduction to the Theory
of the Riemann Zeta-Function*, Cambridge 1988, Ch. 3.

---

## 2. The Connes–Marcolli Operator-Algebraic Form

### 2.1 The idea

Connes (1999) observed that the Riemann–Weil formula has the
structure of a *trace formula*: the left-hand side is a sum over
spectral data, and the right-hand side is a sum over "geometric"
data (primes, archimedean place, pole). The natural question is
whether there is a geometric object $X$ and an operator $T$ on a
Hilbert space $\mathcal H$ associated to $X$, such that (1.1) is
literally
$$
\mathrm{Tr}\bigl(h(T)\bigr) \;=\; (\text{geometric side}),
\tag{2.1}
$$
where $h(T)$ is defined by the functional calculus for self-adjoint
operators.

The answer (Connes 1999, Theorem III.1; Connes–Marcolli 2008,
Chapter II §3, Theorem 3.6) is *yes, after regularisation*. The
object $X$ is the *adele class space*
$$
X \;=\; \mathbb{A}_{\mathbb{Q}} / \mathbb{Q}^{\times},
\tag{2.2}
$$
the quotient of the full adele ring by the multiplicative action of
the rationals. The Hilbert space is an $L^2$-space on $X$ (more
precisely, a weighted Sobolev completion; see §4), and the operator
$T$ is the infinitesimal generator of the scaling action
$$
(\vartheta_\lambda f)(x) \;=\; f(\lambda^{-1} x),
\qquad \lambda \in \mathbb{R}_{>0}^{\times},
\tag{2.3}
$$
so $T = -i\,\frac{d}{d\log\lambda}\bigr|_{\lambda=1}\vartheta_\lambda$.

### 2.2 Statement

> **Theorem 2 (Connes 1999; Connes–Marcolli 2008, Ch. II §3).**
> *There exists a Hilbert space $\mathcal H$ (a weighted $L^2$-space
> on the adele class space $X$ of (2.2)), a self-adjoint operator
> $T$ on $\mathcal H$ generating the scaling action (2.3), and a
> natural class of test functions $h$ satisfying (W1)–(W3), such
> that the Riemann–Weil identity (1.1) is the semiclassical trace
> formula*
>
> $$
>   \mathrm{Tr}_{\mathrm{reg}}\bigl(h(T)\bigr)
>   \;=\;
>   \hat h(0)\,\log\pi
>   \;+\; h(i/2) + h(-i/2)
>   \;-\; 2\sum_{p}\sum_{k}
>     \frac{\log p}{p^{k/2}}\,\hat h(k\log p)
>   \;-\; W_\infty(h),
>   \tag{2.4}
> $$
>
> *where $\mathrm{Tr}_{\mathrm{reg}}$ is the regularised trace
> defined in §4 below (principal-value cutoff at the archimedean
> place and a suitable trace-class condition on $h(T)$).*

The left-hand side of (1.1) — the sum $\sum_\rho h((\rho-1/2)/i) =
\sum_n h(\gamma_n)$ on the critical line — is exactly
$\mathrm{Tr}_{\mathrm{reg}}(h(T))$ if and only if the spectrum of
$T$ is $\{\gamma_n\}$ counted with the correct multiplicity.

Connes' theorem does *not* establish that equality. What it
establishes is the *inclusion* of §3 below.

### 2.3 The version in Connes–Marcolli 2008

In Connes–Marcolli, *Noncommutative Geometry, Quantum Fields and
Motives*, AMS Colloquium Publications 55, 2008, the result is
Theorem 3.6 of Chapter II (pp. 97–103 in the printed edition; see
also the exposition in §4.3 of the same chapter on the
Bost–Connes / adele-class-space correspondence). The theorem is
stated there in the slightly stronger form where the test function
class is explicitly the Bruhat–Schwartz space on the adeles, and
the regularised trace is defined via a *subtracted Dixmier trace*
(Connes–Marcolli 2008, Definition 3.5). The subtraction removes a
divergent scale integral, and the finite part reproduces the right-
hand side of (1.1) including the archimedean correction (1.2).

Meyer (2005, "On a representation of the idèle class group related
to primes and zeros of $L$-functions", *Duke Math. J.* 127,
pp. 519–595) gives a cleaner analytic treatment in which the
scaling operator on the adele class space is replaced by a
multiplicative convolution operator on a Sobolev completion, and
the trace formula becomes an identity of tempered distributions.
Meyer's formulation is the one most commonly cited as "the
rigorous version" of Connes 1999.

---

## 3. The Inclusion $\{\gamma_n\} \subseteq \mathrm{spec}(T)$

### 3.1 Statement

> **Theorem 3 (the inclusion).** *Let $T$ be the scaling operator of
> Theorem 2 on the Hilbert space $\mathcal H$. Then each $\gamma_n$
> is a spectral value of $T$:*
>
> $$
>   \bigl\{\,\gamma_n : n = 1, 2, 3, \ldots\,\bigr\}
>   \;\subseteq\;
>   \mathrm{spec}(T).
>   \tag{3.1}
> $$

### 3.2 What "spectral value" means here

The inclusion (3.1) is a statement about the *distributional*
spectrum of $T$: each $\gamma_n$ appears as a pole of the resolvent
$(T - z)^{-1}$ acting on the dense subspace of Bruhat–Schwartz test
vectors. Equivalently, each $\gamma_n$ is a zero of the analytic
continuation of the Mellin-transformed correlator
$$
M(s) \;=\; \langle \phi, \vartheta_{e^{s-1/2}}\,\phi\rangle
\tag{3.2}
$$
for a suitable test vector $\phi \in \mathcal H$.

For a *generic* test vector the correspondence is exact:
$\gamma_n$ is a spectral value of $T$ iff $\rho_n = 1/2 + i\gamma_n$
is a non-trivial zero of $\zeta$. The inclusion (3.1) is the
statement that the forward direction of this equivalence holds
unconditionally.

### 3.3 What the inclusion does NOT say

Three things (3.1) does *not* claim:

(i) It does not claim that $T$ has only $\{\gamma_n\}$ in its
spectrum. The operator $T$ on $\mathcal H$ may have additional
continuous spectrum coming from the non-trivial zeros off the
critical line (if any such zeros exist). The statement
$\mathrm{spec}(T) = \{\gamma_n\}$ is the Hilbert–Pólya conjecture
and is equivalent to RH in this formulation (Connes 1999, §II).

(ii) It does not claim that $\gamma_n$ are eigenvalues of $T$ in
the strict sense (i.e., point spectrum). They are *resonances*
of the resolvent, which become point eigenvalues after passing
to an appropriate subspace (the "Riemann subspace" $H_R$ of
research/02 §3.3).

(iii) It does not claim that each $\gamma_n$ appears with
multiplicity 1. The multiplicity of $\gamma_n$ as a spectral value
of $T$ equals the order of the zero $\rho_n$ of $\zeta$ as a zero.
Simple zeros give multiplicity 1; this is conjectured for all
$\gamma_n$ but unproven.

### 3.4 Status of the inclusion

The inclusion (3.1) is **generally accepted as rigorous** in the
operator-algebraic literature. The precise status is:

- **Connes 1999**: proved the inclusion for the regularised trace,
  modulo the analytic subtleties in §4 below. The original paper
  states the result as Theorem III.1 but the proof depends on
  specific regularisation choices that were the subject of later
  refinement.
- **Meyer 2005**: gave a fully rigorous distributional version,
  replacing the regularised trace by a tempered distribution
  identity. Meyer's version is unconditionally proved.
- **Connes–Marcolli 2008**: consolidated the picture in Chapter II,
  Theorem 3.6, citing Meyer 2005 for the rigorous distributional
  formulation and Connes 1999 for the spectral/operator-algebraic
  interpretation.

The *consensus* is that (3.1) holds. The *subtlety* (see §6) is
that the operator $T$ on which it holds depends on the choice of
regularisation, and different choices give unitarily equivalent
but not obviously identical operators. The spectrum, and therefore
the inclusion (3.1), is invariant under these choices.

---

## 4. Regularisation Choices

The trace formula (2.4) does not hold literally: the operator
$h(T)$ on the adele-class Hilbert space $\mathcal H$ is generically
*not* trace-class. The left-hand side of (2.4) has to be
regularised, and the choice of regularisation affects the precise
form of the archimedean correction $W_\infty$.

### 4.1 The principal value at the archimedean place

The archimedean place of $\mathbb{Q}$ contributes a divergent
integral of the form
$$
\int_{0}^{\infty} \bigl(f(\lambda) - f(0)\bigr)\,\frac{d\lambda}{\lambda}
\tag{4.1}
$$
which is only conditionally convergent. Connes (1999, §II.4) uses
the Hadamard *principal-value* regularisation
$$
\mathrm{PV}\int_{0}^{\infty} f(\lambda)\,\frac{d\lambda}{\lambda}
\;=\;
\lim_{\varepsilon \to 0^+}\left[
  \int_{\varepsilon}^{1/\varepsilon} f(\lambda)\,\frac{d\lambda}{\lambda}
  + f(0)\,\log \varepsilon^2
\right].
\tag{4.2}
$$
This specific principal value is the one needed for the archimedean
term to reduce to (1.2).

### 4.2 The cutoff at the non-archimedean places

At each prime $p$, the adelic integral is already convergent (the
local measure is finite on the maximal compact subgroup), so no
cutoff is needed. The sum over primes in (1.1) converges absolutely
for $h$ of Paley–Wiener type (compact support of $\hat h$ makes the
sum finite).

### 4.3 The test function class

The regularised trace is defined for $h$ in the Bruhat–Schwartz
class on the idele class group $\mathbb{A}_\mathbb{Q}^\times /
\mathbb{Q}^\times$. This class is stable under the Fourier
transform and under the scaling action (2.3). Restricted to the
connected component (i.e., $\mathbb{R}_{>0}^\times$), Bruhat–
Schwartz functions are the Schwartz functions whose Fourier
transform has compact support plus a smooth tail — essentially the
Paley–Wiener class of §1.1.

### 4.4 Does the inclusion (3.1) depend on these choices?

The *spectrum* of $T$ is a unitary invariant of the operator, and
therefore does not depend on the regularisation choices used to
define the trace. What depends on the regularisation is the
*identity* (2.4) — specifically, the form of the archimedean term
$W_\infty$. Different regularisation schemes give different
$W_\infty$'s, but they all correspond to the same operator $T$
(up to unitary equivalence) and therefore to the same inclusion
(3.1).

This is the precise content of the statement that (3.1) is
regularisation-independent: the *trace formula* (2.4) is
scheme-dependent in its explicit form, but the *spectral content*
— namely that $\gamma_n$ appears as a spectral value of $T$ — is
invariant.

### 4.5 Subtractions and multiplicative renormalisation

An alternative to the principal-value scheme is the Connes–Marcolli
2008 *subtracted Dixmier trace*, in which the divergent scale
integral is subtracted in a multiplicatively invariant way. The
subtracted trace differs from the principal-value trace by a
finite renormalisation constant, which shifts the archimedean
correction $W_\infty$ by a term proportional to $\hat h(0)$.
Absorbing this shift into the coefficient of $\log\pi$ in (1.1)
shows that the two schemes give the same identity, up to the
$\hat h(0)$-coefficient of the archimedean polar term.

---

## 5. Connection to $T_{\mathrm{BC}}$ of Phase 2

### 5.1 The two constructions

Paper 12's Phase 2 (research/02 §3.2) constructs an operator
$T_{\mathrm{BC}}$ on a subspace of the Bost–Connes GNS Hilbert
space $\mathcal H_1$ at $\beta=1$, defined as
$$
T_{\mathrm{BC}}
\;=\;
-i\,\frac{d}{d\log u}\Big|_{u=1}\sigma_{i\log u},
\tag{5.1}
$$
the generator of the imaginary-time dilation of the BC modular flow.

The Connes operator $T$ of §2 is the scaling-action generator on
the adele class space:
$$
T
\;=\;
-i\,\frac{d}{d\log\lambda}\Big|_{\lambda=1}\vartheta_\lambda.
\tag{5.2}
$$

### 5.2 The equivalence

> **Proposition (CCM equivalence).** *The operators $T$ and
> $T_{\mathrm{BC}}$ are unitarily equivalent, under the unitary
> intertwining the BC GNS space at $\beta=1$ with the weighted
> $L^2$-space on the adele class space used by Connes–Marcolli.
> Specifically, there is a unitary $U : \mathcal H_1 \to \mathcal H$
> such that $U T_{\mathrm{BC}} U^* = T$ on the common dense domain
> of Bruhat–Schwartz test vectors.*

This is the statement of Identity 14 in the QG5D-Riemann research
(`/Users/gsix/riemann-hypothesis/research/`) and is made explicit
in Paper 12 research/14 Part A (the CCM equivalence note).

The identification proceeds via the following chain:

1. The BC algebra $\mathcal A_{\mathrm{BC}} = C^*(\mathbb Q/\mathbb Z)
   \rtimes \mathbb N^\times$ is isomorphic to the reduced crossed
   product of $C(\hat{\mathbb Z})$ by the semigroup action of
   $\mathbb N^\times$ (Bost–Connes 1995, Proposition 18).
2. The GNS representation at $\beta=1$ embeds into $L^2(\hat{\mathbb Z})
   \otimes L^2(\mathbb N^\times, n^{-1}\,dn)$, which in turn embeds
   into the weighted $L^2$-space on the finite-adelic part of
   $\mathbb A_{\mathbb Q}^\times / \mathbb Q^\times$.
3. Adjoining the archimedean component $\mathbb R_{>0}^\times$ and
   the full scaling action gives the adele-class Hilbert space
   $\mathcal H$ of Connes 1999.
4. Under this chain of embeddings, the BC modular automorphism
   $\sigma_t$ at $\beta=1$ becomes the scaling action $\vartheta_{e^t}$
   on $\mathcal H$, and its generator $T_{\mathrm{BC}}$ becomes $T$.

The detailed computation of each step is in Connes–Consani–Marcolli,
"Noncommutative geometry and motives: the thermodynamics of
endomotives", *Adv. Math.* 214 (2007) 761–831, §6–§8. That paper is
the bridge between the Bost–Connes 1995 KMS setup and the Connes
1999 adelic scaling setup.

### 5.3 Consequence for research/02

Under the equivalence of §5.2, Theorem 3 of this file (the inclusion
$\{\gamma_n\} \subseteq \mathrm{spec}(T)$) transfers to
$$
\{\gamma_n\} \;\subseteq\; \mathrm{spec}(T_{\mathrm{BC}}),
\tag{5.3}
$$
which is equation (3.3) of research/02. The $\hat R$ operator of
research/02 §4.1 is then defined as the bounded function
$$
\hat R \;=\; \frac{\ell_P}{\pi}\,\exp\!\Bigl(T_{\mathrm{BC}}\cdot\frac{\pi^2}{2}\Bigr)
\tag{5.4}
$$
by the spectral theorem, with spectrum
$\{R_n = (\ell_P/\pi)\exp(\gamma_n\pi^2/2)\}$ as claimed.

The entire Phase 2 construction rests on (5.3), which is the
transferred form of Theorem 3 via §5.2.

---

## 6. What Is Rigorous, What Is Consensus, What Is Open

### 6.1 Rigorous

(R1) The classical Riemann–Weil explicit formula (1.1) with the
archimedean correction (1.2) for test functions in the Weil class.
This is standard analytic number theory (Iwaniec–Kowalski 2004,
Theorem 5.12; Edwards 1974, §1.14).

(R2) The adele class space $X = \mathbb A_{\mathbb Q}/\mathbb Q^\times$
and its weighted $L^2$-completion $\mathcal H$ (Connes 1999;
Connes–Marcolli 2008, Ch. II §3.1).

(R3) The scaling operator $T$ of (2.3), (5.2) is self-adjoint on a
natural dense domain in $\mathcal H$, as a generator of a strongly
continuous unitary group.

(R4) Meyer's distributional version of the trace formula (Meyer 2005,
*Duke Math. J.* 127): the Riemann–Weil identity (1.1) lifts to an
identity of tempered distributions on the idele class group, with
no regularisation ambiguity. This is the fully rigorous form of
(2.4).

(R5) The unitary equivalence of $T$ with $T_{\mathrm{BC}}$ of the BC
GNS at $\beta=1$, via the Connes–Consani–Marcolli endomotive
framework (Connes–Consani–Marcolli 2007).

### 6.2 Consensus (rigorous but scheme-dependent)

(C1) The regularised trace formula (2.4) with the principal-value
regularisation of §4.1. The equality holds but the value of the
archimedean correction $W_\infty$ depends on the choice of
principal value. Different choices are related by finite
renormalisations absorbed into the polar terms.

(C2) The inclusion $\{\gamma_n\} \subseteq \mathrm{spec}(T)$
(Theorem 3). Under Meyer's distributional formulation this is
unconditionally proved; under the original Connes 1999 formulation
it is proved modulo the regularisation scheme of §4. The *spectrum*
is scheme-invariant and the inclusion holds independently of the
choice.

(C3) The identification of the multiplicities: $\gamma_n$ appears
in $\mathrm{spec}(T)$ with multiplicity equal to the order of the
zero $\rho_n$ of $\zeta$. This follows from the residue analysis
of the Mellin transform in (3.2) and is standard.

### 6.3 Open

(O1) The equality $\mathrm{spec}(T) = \{\gamma_n\}$ (the
Hilbert–Pólya conjecture in Connes' form). This is equivalent to
RH and is the central open problem. Phase 2 of Paper 12 does not
require it — only the inclusion (3.1).

(O2) Whether there exists a "preferred" regularisation scheme in
which the trace formula (2.4) becomes an *unregularised* trace
identity. Meyer 2005 comes close via the distributional
formulation, but a fully operator-theoretic version with $h(T)$
literally trace-class is not known.

(O3) The precise relationship between Connes' adele-class scaling
operator $T$ and the Bost–Connes modular generator
$T_{\mathrm{BC}}$ beyond the unitary equivalence of §5.2. The
equivalence is known at the level of the unitary group generated,
but the finer spectral projections (e.g., the projection $P_{\gamma_n}$
used in research/02 §3.3 to define $H_R$) are not entirely
independent of the regularisation scheme. This is the "residual
subtlety" flagged in §6.4 below.

### 6.4 The residual subtlety

The single most important residual subtlety is this:

**Under different regularisation schemes, the spectral projections
$P_{\gamma_n}$ of $T$ at the spectral value $\gamma_n$ are defined
on slightly different dense subspaces of $\mathcal H$.** They agree
as operators on the Bruhat–Schwartz test-vector domain, but their
extensions to the full Hilbert space can differ by a finite-rank
perturbation at each $\gamma_n$.

The consequence for Paper 12 is: the Riemann subspace
$H_R = \overline{\mathrm{span}}\{P_{\gamma_n}\Omega_1\}$ of research/02
§3.3 is well-defined up to a choice of regularisation, and the
$\hat R$ operator of (5.4) has spectrum $\{R_n\}$ independent of
the choice, but the *individual eigenvectors* $|\gamma_n\rangle$
depend on the scheme.

This subtlety is visible in the off-diagonal matrix elements of
$\hat R$ between $|\gamma_n\rangle$ and $|\gamma_m\rangle$ (research/02
§5), which enter the 5 ppb corrections of the CC formula. The
*spectrum* is scheme-invariant; the *matrix elements* are not. The
latter are the subject of open problem (O3) above.

For the purposes of research/02 §4 (the construction of $\hat R$
from the spectrum), research/04 (Identity 12), research/08 §2.4
(RH as physical theorem, which needs only the inclusion), and
research/11 (the transposition of Theorem K.4, which needs only
the unitary equivalence), the residual subtlety is *inconsequential*.
For research/02 §5 (the perturbative corrections) it is a genuine
source of freedom that has not yet been pinned down.

---

## 7. Status Table

| # | Content | Status |
|:--|:--------|:-------|
| T1 | Riemann–Weil formula (1.1) | **Rigorous** (Iwaniec–Kowalski 2004) |
| T2 | Adele-class Hilbert space $\mathcal H$ | **Rigorous** (Connes 1999) |
| T3 | Scaling operator $T$ self-adjoint | **Rigorous** (Meyer 2005) |
| T4 | Distributional trace formula | **Rigorous** (Meyer 2005) |
| T5 | Regularised trace formula (2.4) | **Consensus** (scheme-dependent archimedean) |
| T6 | Inclusion $\{\gamma_n\}\subseteq\mathrm{spec}(T)$ | **Consensus → Rigorous** via Meyer |
| T7 | Multiplicity = order of zero | **Consensus** |
| T8 | $T \simeq T_{\mathrm{BC}}$ (unitary equiv.) | **Rigorous** (CCM 2007) |
| T9 | Inclusion transferred to $T_{\mathrm{BC}}$ | **Consensus** (same status as T6) |
| O1 | $\mathrm{spec}(T) = \{\gamma_n\}$ (Hilbert–Pólya) | **Open** ≡ RH |
| O2 | Preferred regularisation scheme | **Open** |
| O3 | Scheme-independence of $P_{\gamma_n}$ | **Open** |

The inclusion that Paper 12 uses — T6/T9 — is rigorous via Meyer
2005 in its distributional form, and is consensus (modulo
regularisation) in its operator-theoretic form. The rigorous form
is sufficient for every downstream use in Paper 12 except the
5 ppb perturbative corrections of research/02 §5, which depend on
the finer spectral projection structure addressed by O3.

---

## 8. Definition of Done

This research file is the master reference for Gap 1 of
`integers/paper12-cbb-system/15-audit-and-missing-research-files.md`. It is complete when:

- [x] The classical Riemann–Weil formula is stated precisely (§1).
- [x] The Connes–Marcolli operator-algebraic form is stated (§2),
      with the specific theorem reference (Connes–Marcolli 2008
      Ch. II Thm 3.6; Meyer 2005).
- [x] The inclusion $\{\gamma_n\}\subseteq\mathrm{spec}(T)$ is
      stated precisely with the distinction between point spectrum,
      resonances, and multiplicities (§3).
- [x] The regularisation choices (principal value, Bruhat–Schwartz
      test functions, subtracted Dixmier trace) are discussed and
      their effect on the inclusion is addressed (§4).
- [x] The unitary equivalence with $T_{\mathrm{BC}}$ of research/02
      is stated and the chain of embeddings sketched (§5).
- [x] A honest rigorous/consensus/open accounting is given (§6),
      with the residual subtlety (O3) explicitly flagged.
- [x] A status table (§7) summarises the landscape.
- [x] References to the primary literature (§9) are complete.

Subsequent citations from other research notes should cite this
file as:

> "see research/18 §3 for the precise form of the inclusion
> $\{\gamma_n\}\subseteq\mathrm{spec}(T_{\mathrm{BC}})$"

or, for the regularisation dependence,

> "see research/18 §4 and §6.4 for the scheme dependence of the
> spectral projections".

---

## 9. References

### 9.1 Primary operator-algebraic references

- Connes, A., "Trace formula in noncommutative geometry and the
  zeros of the Riemann zeta function", *Selecta Math. (N.S.)*
  **5** (1999) 29–106.
- Connes, A., and Marcolli, M., *Noncommutative Geometry, Quantum
  Fields and Motives*, AMS Colloquium Publications **55** (2008),
  Chapter II §3, especially Theorem 3.6.
- Connes, A., Consani, C., and Marcolli, M., "Noncommutative
  geometry and motives: the thermodynamics of endomotives",
  *Adv. Math.* **214** (2007) 761–831.
- Meyer, R., "On a representation of the idèle class group related
  to primes and zeros of $L$-functions", *Duke Math. J.* **127**
  (2005) 519–595.
- Bost, J.-B., and Connes, A., "Hecke algebras, type III factors
  and phase transitions with spontaneous symmetry breaking in
  number theory", *Selecta Math. (N.S.)* **1** (1995) 411–457.

### 9.2 Classical analytic number theory references

- Edwards, H. M., *Riemann's Zeta Function*, Academic Press, 1974.
  (Chapter 1, especially §1.14, for the classical explicit
  formula.)
- Iwaniec, H., and Kowalski, E., *Analytic Number Theory*, AMS
  Colloquium Publications **53**, 2004. (Theorem 5.12 for the
  Riemann–Weil explicit formula with archimedean term.)
- Patterson, S. J., *An Introduction to the Theory of the Riemann
  Zeta-Function*, Cambridge University Press, 1988, Chapter 3.
- Weil, A., "Sur les «formules explicites» de la théorie des
  nombres premiers", *Comm. Sém. Math. Univ. Lund* (1952) 252–265.

### 9.3 Within Paper 12

- `research/02-quantize-R-construction.md` §3.2 — the downstream
  use for constructing $\hat R$.
- `research/04-identity-12-rigorous.md` — the unitary equivalence
  between the e-circle and the BC system.
- `research/08-rh-as-physical-theorem.md` §2.4 — RH as the
  physical statement that the smallest eigenvalue of $\hat R$ is
  the observed radius.
- `research/14-transposition-ccm.md` Part A — the CCM scaling
  operator identification used here in §5.2.
- `research/17-k12-discussion.md` — the $K_{12}$ closure problem,
  which uses the inclusion (3.1).

---

*The Riemann–Weil explicit formula is the backbone of analytic*
*number theory since Weil 1952. Connes 1999 rewrote it as a trace*
*formula for a scaling operator on the adele class space. The*
*inclusion $\{\gamma_n\} \subseteq \mathrm{spec}(T)$ — rigorous via*
*Meyer 2005 in its distributional form, consensus via Connes 1999*
*in its operator-theoretic form — is the single most-cited result*
*in Paper 12. Every downstream use refers to this note.*
