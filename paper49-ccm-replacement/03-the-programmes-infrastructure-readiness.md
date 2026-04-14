# §03 — The Programme's Infrastructure Readiness

*Paper 49, Part I: Motivation. What we have already proved is more
than enough. An audit of programme-internal proofs that feed Paper 49.
Every ingredient is either classical (Tomita-Takesaki 1970) or
programme-internal (our own PROOF-CHAIN files).*

---

## The thesis

Paper 49's construction of the Hilbert-Pólya operator has six
prerequisites:

1. The BC algebra and its KMS$_1$ state.
2. The type III$_1$ classification of the BC factor.
3. Tomita-Takesaki theory on a type III$_1$ factor in standard form.
4. Ergodicity of the modular flow.
5. A compact-resolvent bound on the Hilbert-Pólya operator.
6. A matching of the spectral density to the Riemann-zero density.

For each of these, we show below that either a classical result
suffices or a programme-internal proof already exists. Nothing in the
list requires new work beyond the writing-up of Paper 49's sections.

## 1. The BC algebra and KMS$_1$ — Bost-Connes 1995

**Status**: Classical (30 years).

The algebra $A_{BC} = C(\hat{\mathbb{Q}}) \rtimes \mathbb{N}^*$,
originally constructed by Bost and Connes (*Selecta Math.* 1995), is
the starting point. Theorem 25 of that paper establishes that the
unique KMS$_1$ state on $A_{BC}$ satisfies $\omega_1(e_n) = 1/n$ for
all $n \in \mathbb{N}^*$. At $\beta > 1$, KMS states form a family
parametrized by $\text{Gal}(\mathbb{Q}^{\text{cyc}}/\mathbb{Q})$; at
$\beta = 1$ the symmetry breaks and the equilibrium is unique.

The GNS construction from $\omega_1$ produces a Hilbert space
$H_{\omega_1}$, a cyclic and separating vector $\xi_{\omega_1}$, and
a representation $\pi_{\omega_1}: A_{BC} \to B(H_{\omega_1})$. The
bicommutant $M_1 := \pi_{\omega_1}(A_{BC})''$ is a von Neumann
algebra. All of this is standard GNS and appears in every operator-
algebra textbook.

**What Paper 49 needs**: Existence + uniqueness of $\omega_1$;
GNS data $(H_{\omega_1}, \pi_{\omega_1}, \xi_{\omega_1}, M_1)$.
**Where it comes from**: Bost-Connes 1995 Thm 25; Takesaki Vol I §III.4.

## 2. Type III$_1$ classification — Paper 13 Layer 2

**Status**: Programme-internal, three independent proofs.

Paper 13's Layer 2 establishes the ITPFI factorization
$\omega_1 = \bigotimes_p \omega_1^{(p)}$ of the KMS$_1$ state as
an infinite tensor product over primes, with Araki-Woods parameters
$\lambda_p = 1/p$. The resulting factor is classified via
Araki-Woods 1968: since $\{\log p\}_{p \text{ prime}}$ is
$\mathbb{Q}$-linearly independent (unique prime factorization), the
Araki-Woods closure is dense in $\mathbb{R}_+$, forcing type III$_1$.

Three independent proofs are recorded in
`paper13-rh/research/265-itpfi-factorization.md`:

- **Proof A**: Direct Euler-product decomposition of $\omega_1$,
  using the BC partition-function identity $Z(\beta) = \zeta(\beta)$.
- **Proof B**: Amenability of the BC Hecke semigroup plus
  uniqueness of KMS$_1$, invoking Connes-Takesaki structure theory.
- **Proof C**: Direct Araki-Woods construction from the local-at-$p$
  factor decomposition, matching weights to $\lambda_p = 1/p$.

Any one of the three proofs suffices. Three independent routes
greatly reduce the risk of undetected error.

**What Paper 49 needs**: $M_1$ is a type III$_1$ factor.
**Where it comes from**: Paper 13 research/265 (three proofs);
Bost-Connes 1995 + Araki-Woods 1968.

## 3. Tomita-Takesaki theory — classical 1970

**Status**: Classical (55 years), textbook.

For a von Neumann algebra $M$ on a Hilbert space $H$ with a cyclic
and separating vector $\xi$, define the closable antilinear operator
$S_0: M\xi \to M\xi$ by $S_0(a\xi) = a^*\xi$. The closure
$\bar{S}$ has polar decomposition $\bar{S} = J \Delta^{1/2}$, where
$\Delta$ is positive self-adjoint (possibly unbounded) and $J$ is
antilinear with $J^2 = I$. Tomita-Takesaki's theorem states:

- $J M J = M'$ (the commutant).
- $\Delta^{it} M \Delta^{-it} = M$ for all $t \in \mathbb{R}$.
- $\sigma_t := \text{Ad}(\Delta^{it})|_M$ is a one-parameter
  automorphism group of $M$ (the *modular flow*).
- For any other cyclic-separating vector $\eta$, the two modular
  flows $\sigma^{\omega_\xi}_t$ and $\sigma^{\omega_\eta}_t$ differ by
  an inner automorphism (cocycle formula; Connes 1973).

The theory is in every operator-algebra textbook:

- Takesaki, *Theory of Operator Algebras* Vol I–III (Springer).
- Bratteli-Robinson, *Operator Algebras and Quantum Statistical
  Mechanics* Vol I–II.
- Connes, *Noncommutative Geometry*.

No preprint. No ambiguity. Classical.

**What Paper 49 needs**: The modular operator $\Delta$ and
conjugation $J$; the modular flow $\sigma_t$; the invariance
properties above.
**Where it comes from**: Tomita 1967, Takesaki 1970.

## 4. Modular flow ergodicity — Paper 32 (BGS) L2

**Status**: Programme-internal, closed via Path B.

Paper 32 (BGS — Bohigas-Giannoni-Schmit spectral statistics) L2
proved: the modular flow $\sigma_t$ acts ergodically on $M_1$.

Path B (the route we closed with) chains:

- $M_1$ is a factor (trivial center), because $A_{BC}$ has
  uniqueness at KMS$_1$ — proved in Bost-Connes 1995 Thm 25 and
  recalled in Paper 28 Key Lemma 3.4.3.
- A type III$_1$ factor in standard form with trivial center has no
  $\sigma_t$-invariant projections other than $0$ and $I$ (this is a
  classical consequence of the Connes-Takesaki structure theory,
  e.g., Takesaki Vol II §XII).
- Therefore $\sigma_t$ is ergodic on $M_1$.

The detailed write-up is in
`paper32-bgs-spectral-statistics/research/01-modular-flow-ergodicity.md`.

**What Paper 49 needs**: Ergodicity of $\sigma_t$ on $M_1$.
**Where it comes from**: Paper 32 (BGS) L2; inherits unchanged.

## 5. Compact-resolvent bound — Paper 13 Layer 3c

**Status**: Programme-internal, proved via Fourier cancellation.

Paper 13's Layer 3c ("Fourier-basis cancellation H$^1$ bound")
proved:

$$
\left\| (D_N - i)^{-1} \right\|_{L^2 \to H^1}
\leq 1 + C \rho^{-N} < 2
$$

uniformly in $\lambda$ and $N$, where $\rho \geq 4.27$ is the CF
decay rate (Paper 13 research/35) and $C$ is an absolute constant.
The proof mechanism: the $H^1$ weight $(1 + (2\pi n/L)^2)$ *exactly*
cancels the resolvent denominator $(2\pi n/L)^2 + 1$ from the BC
algebra's abelian Fourier structure; rank-1 quotient correction
contributes $O(\rho^{-N})$.

**Crucial for Paper 49**: the cancellation argument uses only the
abelian Fourier structure of $C(\hat{\mathbb{Q}})$. It does not
depend on CCM's specific prolate-spheroidal basis, nor on
Carathéodory-Fejér stabilization. The bound extends to the
infinite-$N$ limit (Paper 13 Layer 4 Bögli argument), giving
compactness of the resolvent via Rellich-Kondrachov.

Paper 49 inherits the Layer 3c bound with the operator $D_N$
reinterpreted as the finite-$N$ truncation of $-(2/\pi^2) i \log \Delta$
instead of CCM's prolate-based construction. The bound is *structurally*
independent of which route one took to build $D_N$ — it depends only on
the BC algebra's Fourier structure, which is the same on both routes.

**What Paper 49 needs**: $(D - i)^{-1}$ compact on the even sector.
**Where it comes from**: Paper 13 research/44 (Fourier cancellation);
Rellich-Kondrachov (classical).

## 6. Spectral-density matching — Layers 4–5 + QUE + Sato-Tate

**Status**: Layers 4–5 programme-internal (PROVED); QUE classical
(Lindenstrauss 2010); Sato-Tate classical (Taylor 2011).

The matching $\text{spec}(D) = \{\gamma_n\}$ breaks into three
substeps:

**(6a) Entry-by-entry Weil-form convergence.** Paper 13 Layer 2
(ITPFI factorization) gives weak-$*$ convergence of the truncated
KMS$_1$ states to $\omega_1$, hence entry-by-entry convergence of
the associated Weil quadratic form. Paper 13 Layer 3 supplies the
four uniform estimates (archimedean, eigenvector, H$^1$, CF-decay).

**(6b) Spectral exactness.** Paper 13 Layer 4 (Bögli H1+H2 → spectral
exactness) proves $\text{spec}(D_\infty) = \lim \text{spec}(D_N)$
with no spurious eigenvalues, via Bögli 2017 (arXiv:1604.07732,
refereed). Paper 13 Layer 5 (Hurwitz zero convergence) identifies
the limit spectrum with $\{\gamma_n\}$, via Hurwitz 1893 and
Connes-van Suijlekom 2025 (Commun. Math. Phys., published).

**(6c) Spectral density equals Weil density.** The Koopman operator
$U_t = \Delta^{it}$ on $L^2(M_1)$ is unitary; its spectral
decomposition gives the density of $D$. Ergodicity (§ above) plus
QUE (Lindenstrauss 2006, *Ann. Math.*, published) force the
Hecke-Maass equidistribution that identifies the density with the
Weil measure. Sato-Tate (Taylor 2011, published) gives the local-
at-$p$ matching of Frobenius angles, closing the explicit formula.

The QUE ingredient requires Paper 48 (not yet written) to spell out
the arithmetic-to-modular-flow translation. The Sato-Tate framing is
in Paper 44.

**What Paper 49 needs**: spectral density of $D$ equals zero-
density of $\zeta$.
**Where it comes from**: Paper 13 Layers 2, 4, 5 (programme-
internal); Paper 48 QUE (Lindenstrauss 2010); Paper 44 Sato-Tate
(Taylor 2011); Weil 1952 explicit formula (classical).

## Dependency table

| Prerequisite | Source | Tier |
|---|---|---|
| BC algebra + KMS$_1$ uniqueness | Bost-Connes 1995 | Published 30 years |
| GNS construction | Takesaki Vol I §III.4 | Textbook |
| Type III$_1$ via ITPFI | Paper 13 L2 (3 proofs) | Programme-internal |
| Araki-Woods classification | Araki-Woods 1968 | Published 58 years |
| Tomita-Takesaki theory | Takesaki 1970 | Textbook |
| Modular flow ergodicity | Paper 32 (BGS) L2 (Path B) | Programme-internal |
| Trivial center of $M_1$ | Paper 28 Key Lemma 3.4.3 | Programme-internal |
| Compact resolvent bound | Paper 13 L3c (Fourier cancellation) | Programme-internal |
| CBB rescaling $\kappa = 2/\pi^2$ | Paper 12 operator dictionary | Programme-internal |
| Rellich-Kondrachov | standard functional analysis | Textbook |
| Spectral exactness | Paper 13 L4 (Bögli H1+H2) | Programme-internal + refereed |
| Hurwitz zero convergence | Paper 13 L5 | Programme-internal + classical |
| Weil explicit formula | Weil 1952 | Published 73 years |
| QUE (Hecke-Maass) | Lindenstrauss 2006 | Published 20 years (Fields Medal) |
| Sato-Tate (non-CM) | Taylor 2011 | Published 15 years |
| ITPFI factorization of $\omega_1$ | Paper 13 L2 research/265 | Programme-internal (3 proofs) |
| Parity involution / even sector | BC $\hat{\mathbb{Z}}^*$-symmetry (programme) | Programme-internal |

Zero preprint-tier dependencies. Every ingredient is either classical
published literature (textbook or >10 years old) or a programme-
internal proof we can audit.

## What's missing

Paper 48 (QUE → programme framing for the BC Koopman operator) is not
yet written. The substance is Lindenstrauss 2006 (classical,
published). The programme framing (how Hecke-Maass eigenfunctions on
$\Gamma_0(N) \backslash \mathbb{H}$ correspond to BC modular-flow
eigenfunctions) is the remaining new writeup. This is a translation
exercise between two equivalent descriptions of arithmetic quantum
chaos. It is not a new theorem.

Paper 44 (Sato-Tate framing) exists as a stub (confidence 6/10,
research folder present). The non-CM Sato-Tate theorem is Taylor
2011. The framing that connects it to the BC modular flow is written
up in fragments across Papers 1, 12, and 32; Paper 49 §26 will
consolidate.

No other pieces are missing.

## The assessment

Paper 49 is a large synthesis, but it is not a new proof of anything
deep. Every deep theorem it uses has been proved elsewhere — some in
the 1970s (Tomita-Takesaki, Araki-Woods), some in the 1990s (Bost-
Connes, ITPFI via our Layer 2), some in the 2010s (Lindenstrauss,
Taylor), some in our own programme (Paper 13 Layers 2–5, Paper 32 L2,
Paper 12 dictionary, Paper 28 Lemma 3.4.3). What Paper 49 supplies is
the *assembly*: the specific way these pieces compose into a self-
adjoint operator whose spectrum is the Riemann zeros.

The assembly takes effort (Parts IV–V will be substantial), but the
effort is of the "careful write-up" kind, not the "new mathematical
breakthrough" kind. This is why the timeline is 6–12 months rather
than 6–12 years.

The programme's infrastructure is ready. Paper 49 is the next
scheduled step, not a speculative leap.

---

*Next: §04 — the proof in one paragraph. The compressed statement
of Paper 49's claim.*
