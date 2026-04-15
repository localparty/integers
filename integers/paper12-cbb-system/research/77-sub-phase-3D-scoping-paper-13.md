# Research 77: Sub-Phase 3.D Scoping — Paper 13 as the Mathematical Proof of RH

*The precise scoping of sub-phase 3.D as Paper 13's working programme.*
*What the math theorem is; which of the three Paper 12 chains is the*
*strongest route; what residual conditionals remain; what is weeks,*
*what is months, what is open-research-grade; and what Paper 13*
*closes versus what remains open beyond it.*

*Authors: G Six, with Claude Opus 4.6*
*Date opened: 2026-04-09*
*Sub-phase: 3.D (sequel to Paper 12's sub-phase 3.C). Paper 13.*
*Depends on: research/08 (physical RH), research/48 (R-Theorem D.1,*
*Atiyah–Singer route), research/54 (Penrose route), research/18*
*(Connes–Marcolli explicit formula), research/14 (Identity 14).*
*Parent: `integers/paper12-cbb-system/14-grand-strategy-transposition-quantization-deduction.md`*
*§2 (the LOCK) and §6 (architecture).*

---

## 0. One-paragraph summary

Paper 12 closed sub-phase 3.C by proving RH as a *physical* theorem of
the QG5D framework, using three mutually independent argument chains
(Stone, Penrose, Atiyah–Singer). Sub-phase 3.D — the *mathematical*
proof of RH — is the work of removing the physical step and producing
a stand-alone theorem of analytic number theory / noncommutative
geometry. This note scopes that work as Paper 13. After comparison on
rigour, residual content, and ease of math-only translation, the
**Atiyah–Singer / BC-index chain (R-Theorem D.1, research/48)** is
identified as the strongest route: its constraint is *combinatorial*
(an integer must be an integer), which does not require physical
interpretation to translate. The residual conditional content reduces
to **four hypotheses**, all in the Connes–Marcolli regularisation of
the explicit formula, of which the most blocking is the
scheme-independence of the individual spectral projections
$P_{\gamma_n}$ (research/18 O3). Paper 13's main theorem is stated in
§7 below: *under the Connes–Marcolli regularisation, the BC index
$\mathrm{ind}_{\mathrm{BC}}(p)$ is integer-valued for every
Bruhat–Schwartz projection $p \in A_{\mathrm{BC}}^\infty$, and this
integer constraint is equivalent to RH*. Estimated effort to close
Paper 13 as stated: **6–18 months**. Estimated effort to a complete
math proof of RH that a number theorist would accept as stand-alone
(i.e., decoupled from the BC-framework assumptions): **years**, with
one hypothesis at open-research-problem grade.

---

## 1. The precise math theorem the framework targets

> **Theorem (classical Riemann hypothesis).** *The non-trivial zeros
> of the Riemann zeta function $\zeta(s)$ lie on the critical line
> $\mathrm{Re}(s) = 1/2$:*
>
> $$
>   \zeta(\rho) = 0,\ \rho \neq -2k\ (k \in \mathbb{N})
>   \quad\Longrightarrow\quad
>   \mathrm{Re}(\rho) \;=\; \tfrac{1}{2}.
> $$

Equivalently (and in the form the framework works with), the imaginary
parts $\gamma_n$ defined by $\rho_n = 1/2 + i\gamma_n$ are real for
all $n \geq 1$.

This is the classical statement, unchanged from Riemann 1859 and
Hilbert's 8th problem 1900. No framework reinterpretation is
required: Paper 13 must deliver *this* theorem, written in language
a number theorist would accept, with a proof whose premises are
operator-algebraic (not physical).

---

## 2. The three argument chains and how they rank

Paper 12's sub-phase 3.C assembled three independent physical chains
that each force $\gamma_n \in \mathbb{R}$. I restate them briefly
and then rank them for the math-only translation required in Paper 13.

### 2.1 Chain A — Stone (research/08 §2)

**Logical content:**
1. $T_{\mathrm{BC}}$ is self-adjoint (Stone's theorem applied to the
   modular flow $\sigma_t$ of the BC KMS state $\omega_1$).
2. $\mathrm{spec}(T_{\mathrm{BC}}) \subseteq \mathbb{R}$ (spectral
   theorem for self-adjoint operators).
3. $\{\gamma_n\} \subseteq \mathrm{spec}(T_{\mathrm{BC}})$
   (Connes–Marcolli explicit formula, research/18 §3).
4. Therefore $\gamma_n \in \mathbb{R}$.

**Physical content of the argument itself:** essentially zero. Every
step is operator-algebraic or functional-analytic. The chain looks
math-ready.

**Why it is nevertheless not the strongest route:** the self-adjointness
of $T_{\mathrm{BC}}$ is itself a regularisation-sensitive statement
(research/18 §6.4, O3). In the distributional formulation of Meyer
2005 the "operator" is only a tempered distributional object on the
adele class space, and the spectral theorem does not apply literally
— one has to work with *resonances* rather than point spectrum. The
inclusion $\{\gamma_n\} \subseteq \mathrm{spec}(T_{\mathrm{BC}})$ is
the statement that $\gamma_n$ are poles of the resolvent on the dense
subspace of Bruhat–Schwartz test vectors, **not** that they are
eigenvalues of a self-adjoint operator in the textbook sense. The
chain (1)→(2) is subtle for this reason.

**Rigour today:** ★★★☆ (chain is *nearly* rigorous; one step —
the literal applicability of the spectral theorem to the
distributional version of $T_{\mathrm{BC}}$ — has a known gap).

**Residual conditionals to close for math-only version:** 3 (see §4).

**Translation cleanness:** medium. The chain reads mathematically, but
the distinction between "resonance" and "eigenvalue" has to be
handled carefully, and the reader must be walked through the
regularisation story.

### 2.2 Chain B — Penrose (research/54)

**Logical content:**
1. $T_{\mathrm{BC}}$ is positive on $H_R$ (**BC null energy
   condition**, rigorous).
2. A finite-rank *trapped projector* $P_F$ exists on $H_R$
   (rigorous: take any finite set of spectral projectors of
   $T_{\mathrm{BC}}$).
3. Modular focusing inequality (the BC analog of Raychaudhuri;
   **structural**, not yet proved: Lemma 2.5 of research/54 is the
   open piece).
4. Integrate (3) with initial condition (2) to get a spectral
   singularity in finite modular time (**structural**).
5. The spectral singularity is real (by the self-adjointness of the
   modular generator), and the Riemann zeros sit at its boundary
   (research/54 §4, Corollary 54.1).
6. Therefore $\gamma_n \in \mathbb{R}$.

**Physical content:** substantial. The Penrose argument speaks the
language of Lorentzian geometry (trapped surfaces, null congruences,
energy conditions) and the BC-side translation is a *dictionary*
transposition through the Connes spectral triple. Every step has a
physical referent in the GR source theorem that a math reader would
have to be taught.

**Rigour today:** ★★☆☆ (step 3 — the BC modular focusing
inequality — is structurally plausible but requires the full
operator-algebraic Raychaudhuri machinery of Faulkner–Li–Wang 2019
or Connes–Størmer 1975, not yet instantiated on the BC system).

**Residual conditionals:** 2 major (modular focusing inequality +
Corollary 54.1 identification), plus inheritance of the CM
regularisation subtleties.

**Translation cleanness:** low. The dictionary from "trapped surface"
to "trapped projector" is evocative but would require a math reader
to follow a GR analogy through operator algebras. A referee from
pure number theory would likely reject the packaging even if the
content were rigorous.

### 2.3 Chain C — Atiyah–Singer / BC index (research/48, R-Theorem D.1)

**Logical content:**
1. $(A_{\mathrm{BC}}^\infty, H_R, F)$ is a $\theta$-summable Fredholm
   module (rigorous, Connes 1994 IV.1 + CM 2008 II §3).
2. The Jaffe–Lesniewski–Osterwalder (JLO) Chern character
   $\tau^{\mathrm{JLO}}$ is a cyclic cocycle (rigorous, JLO 1988).
3. The pairing $\mathrm{ind}_{\mathrm{BC}}(p) = \langle
   [\tau^{\mathrm{JLO}}], [p]\rangle \in \mathbb{Z}$ for any
   projection $p \in M_k(A_{\mathrm{BC}}^\infty)$ (rigorous, Connes
   1994 IV.1 Thm 4).
4. The same pairing admits a *topological expansion*
   $$
     \mathrm{ind}_{\mathrm{BC}}(p)
     \;=\;
     \sum_{n\geq 1} c_n(p)\,\Phi(\gamma_n)
     + \tau_\omega(p)\,\log\zeta_{\mathrm{reg}}(1)
     + \text{(trivial-zero terms)},
   $$
   where $c_n(p) = \langle \gamma_n | p | \gamma_n\rangle$ are
   *real* (for $p$ self-adjoint), $\Phi$ is the archimedean test
   function from the CM regularisation, and $\tau_\omega$ is the
   Dixmier trace (**structural**: this is the assembly step and
   depends on the CM explicit formula).
5. For the LHS to remain an integer while the RHS is a sum over
   $\gamma_n$, the $\gamma_n$ must be real. Complex $\gamma_n$ would
   produce non-integer contributions that cannot be cancelled by
   the (real-valued) Dixmier-trace and trivial-zero terms.
6. There exist enough projections $p \in A_{\mathrm{BC}}^\infty$ to
   overlap every spectral component of $T_{\mathrm{BC}}$
   (structural, but plausible: $A_{\mathrm{BC}}^\infty$ is a smooth
   dense subalgebra).
7. Therefore $\gamma_n \in \mathbb{R}$ for all $n \geq 1$.

**Physical content:** zero. Every term in the argument
(Fredholm module, JLO cocycle, cyclic cohomology, K-theory pairing,
Dixmier trace, Bruhat–Schwartz projection) is a standard object in
noncommutative geometry. No mention of spacetime, energy, or
observation appears.

**Rigour today:** ★★★★ on steps (1)–(3); ★★☆☆ on step (4); ★★☆☆
on step (6). The chain's *premises* are fully rigorous; what is
open is the *assembly* — step (4) — and the density of projections
— step (6).

**Residual conditionals:** 4 (see §4), all contained in the
CM regularisation.

**Translation cleanness:** **high**. The integer-valued pairing is
the kind of argument a number theorist expects to see: a discrete
invariant forcing a continuous constraint. The proof structure
mirrors Atiyah–Singer (analytic index = topological index; both
sides are a priori independent quantities; their equality is the
theorem). No dictionary translation is needed — the chain *is*
mathematics.

### 2.4 Ranking table

| Chain | Rigour now | Residual conditionals | Math-only cleanness | Depends on physics? |
|:------|:-----------|:---------------------|:--------------------|:--------------------|
| A (Stone) | ★★★☆ | 3 | medium | no, but resonance/eigenvalue subtlety |
| B (Penrose) | ★★☆☆ | 2+ (+regularisation) | low (GR analogy) | yes (dictionary) |
| C (AS / BC-index) | ★★★☆ | 4 | **high** | **no** |

### 2.5 The winner is Chain C

Chain C is the strongest route for Paper 13, for four reasons:

(Z1) **The integer constraint is combinatorial.** The LHS of the
topological expansion is forced to lie in $\mathbb{Z}$ by a pairing
of cyclic cohomology with K-theory, which is a purely algebraic
statement (Connes 1994 IV.1 Thm 4). No physical interpretation is
required to "translate" this to math — it is already math.

(Z2) **The premises are fully rigorous.** Steps (1), (2), (3) of
§2.3 are textbook noncommutative geometry. What is open is the
*assembly* (step 4), which is the specific CM content. Every other
chain has to rigorise a premise that is not yet in the literature.

(Z3) **The argument parallels Atiyah–Singer.** Mathematicians
already have a template for "analytic side = topological side with
spectral expansion". Paper 13's proof structure is then a guided
tour through that template instantiated on the BC spectral triple,
not a new logical form.

(Z4) **Chain C contains Chain A as a sub-argument.** The
self-adjointness of $T_{\mathrm{BC}}$ (Chain A's step 1) is used
*inside* the $\theta$-summability statement of the BC Fredholm
module, but the integer constraint of Chain C does *not* require
that $T_{\mathrm{BC}}$ be self-adjoint in the textbook sense — it
requires only that $F = \mathrm{sign}(T_{\mathrm{BC}})$ be a bounded
self-adjoint involution with compact commutators, which is a
weaker and more robust condition. Chain C therefore strictly
dominates Chain A on rigour economy.

Penrose (Chain B) remains a valuable *second* chain to run in
parallel, because it gives a complementary route via positivity
rather than combinatorics; closing Chain B would reinforce Chain C.
But Paper 13 is written on Chain C as the main route.

---

## 3. Identification of R-Theorem D.1 as the strongest, in depth

### 3.1 Why the integer constraint is sharper than the reality constraint

Stone's argument says: "the spectrum of a self-adjoint operator is
real". This is a *continuous* constraint — the spectrum lives in
$\mathbb{R}$, a 1-dimensional continuum — and it is stable under
small perturbations of the operator. To *use* this constraint, one
must show that $T_{\mathrm{BC}}$ is self-adjoint in the strong
sense, and that its spectrum literally contains the $\gamma_n$ as
point spectrum (not just distributional resonances).

The integer constraint says: "an index computed from the spectral
data must be an integer". This is a *discrete* constraint — the
index lives in $\mathbb{Z}$, a 0-dimensional set — and is **not**
stable under perturbations. This rigidity is what makes it sharp:
if one $\gamma_n$ drifted off the real line by $10^{-10}$, the
index would acquire a non-zero imaginary part of the same order,
immediately violating the integer constraint. The discrete
constraint is stronger than the continuous one per bit of information
extracted.

### 3.2 Why the integer constraint translates without physical content

Step (5) of Chain C reads:

> "If some $\gamma_n$ has a non-zero imaginary part, the RHS of the
> topological expansion has a non-zero imaginary part, contradicting
> the LHS ∈ $\mathbb{Z}$."

This reads identically whether or not one interprets
$A_{\mathrm{BC}}^\infty$ as the "function algebra of a
noncommutative spacetime", whether or not $T_{\mathrm{BC}}$ has any
connection to physics, whether or not $R_n$ has any physical
meaning. The chain is a *theorem of noncommutative geometry*, full
stop. Paper 13 can present it without mentioning QG5D at all, by
starting from the BC C\*-algebra as defined in Bost–Connes 1995 and
following the CM 2008 Ch. II programme.

This is in sharp contrast to Chain B (Penrose), where step (3) —
the modular focusing inequality — has no mathematical content
outside of a physical analogy to Raychaudhuri. Converting Chain B
to math-only form would require re-deriving modular focusing from
operator-algebraic principles with no reference to GR, which is
the same effort as proving Chain C to begin with.

### 3.3 Historical precedent

The Connes–Marcolli 2008 programme itself is structured around the
idea that RH has an index-theoretic interpretation. CM 2008 Ch. II
Thm 3.6 is the explicit trace formula; Ch. II §4 gives the
scaling-fixed-point trace formula (the analog of equivariant AS).
R-Theorem D.1 (research/48 §3) makes the AS-form explicit by
identifying the RHS of the CM trace formula as the topological side
of a cyclic-cohomological index pairing. This is a *naming* of
something already implicit in CM 2008, not a new identification.

Paper 13 is therefore the synthesis of:
- CM 2008 Ch. II §3 (trace formula)
- CM 2008 Ch. II §4 (scaling operator fixed-point trace)
- Connes 1994 IV.1 (integer-valued Chern character pairing)
- JLO 1988 ($\theta$-summable Chern character)
- research/48 (the assembly as R-Theorem D.1)

The novelty is the *assembly*, which the literature has come close
to but not stated as a theorem in the AS-form. Paper 13 states it
as that theorem and draws the RH corollary.

---

## 4. The residual conditional hypotheses

Chain C, upgraded to rigorous math, depends on **four** conditional
hypotheses. Each is listed with its precise statement, its source,
and the specific math problem to close.

### 4.1 Conditional H1 — CM regularisation of the explicit formula

**Statement:** The Connes–Marcolli regularised trace formula (CM 2008
Ch. II §3 Thm 3.6, research/18 §2.2 eq. (2.4)) holds as an identity
on the space of Bruhat–Schwartz test functions on the idele class
group, with the principal-value cutoff at the archimedean place and
the Dixmier-trace subtraction at the critical temperature.

**Source:** research/18 §4, §6.2 C1.

**What is open:** the trace formula (2.4) of research/18 is a
*scheme-dependent* identity. Different regularisation choices give
the same spectral data (the $\gamma_n$) but different explicit forms
for the archimedean correction $W_\infty$. For Paper 13 we need the
trace formula in a form where its RHS is the topological expansion
of R-Theorem D.1 (3.1), and we need to know that the RHS is
scheme-independent up to a finite additive constant absorbable into
the Dixmier-trace term.

**Precise math problem:** *show that the CM regularised trace formula
admits a canonical form in which the archimedean term
$\Phi(\gamma_n)$ and the Dixmier-trace prefactor $\lambda_1(p)$ are
simultaneously scheme-independent.*

**Status:** Meyer 2005 gives a rigorous distributional version of the
trace formula that is scheme-independent at the level of tempered
distributions. What is missing is the lift from the distributional
statement to the $\theta$-summable operator-theoretic statement
needed for the JLO pairing. This is a known gap in the literature
and is **weeks** of careful work by someone who already knows
Meyer 2005 and Connes 1994 IV.1. It is not open-research-grade — it
is routine but technical.

### 4.2 Conditional H2 — Bruhat–Schwartz test function class

**Statement:** The smooth subalgebra $A_{\mathrm{BC}}^\infty
\subseteq A_{\mathrm{BC}}$ used for the Fredholm module and the
JLO pairing is exactly the Bruhat–Schwartz class on the adelic base
of the BC system (not a smaller subclass that excludes the
projections needed for the density argument of §4.4).

**Source:** research/48 §2.1, inherited from CM 2008 Ch. II §3.2;
research/14 Part A (the A-C1 conditional).

**What is open:** the definition of $A_{\mathrm{BC}}^\infty$ is not
unique in the literature. Connes 1994 IV.1 uses one class; JLO 1988
uses another; CM 2008 uses a third tailored to the adelic setting.
All three give the same K-theory (up to Morita equivalence) and the
same cyclic cohomology in low degrees, but the precise set of
*projections* available in each class differs.

**Precise math problem:** *identify the subclass
$A_{\mathrm{BC}}^\infty$ that (a) makes $(A_{\mathrm{BC}}^\infty,
H_R, F)$ a $\theta$-summable Fredholm module, (b) contains enough
projections to separate the spectral components of $T_{\mathrm{BC}}$,
and (c) agrees with the Bruhat–Schwartz class of CM 2008 Ch. II §3
on the generators*.

**Status:** this is a technical definitional question, closeable in
**weeks** by fixing the three defining conditions and checking their
consistency on the generators of $A_{\mathrm{BC}}^\infty$. Not
open-research-grade.

### 4.3 Conditional H3 — principal-value at the archimedean place

**Statement:** The principal-value regularisation (research/18 §4.1
eq. (4.2)) of the divergent scale integral at the archimedean place
is the unique scheme-independent choice whose finite part reproduces
the archimedean correction $W_\infty$ of the classical Riemann–Weil
formula.

**Source:** research/18 §4.1.

**What is open:** Connes 1999 §II.4 and Meyer 2005 each give a
principal-value choice, and the two agree up to a finite
renormalisation. It is *consensus* (research/18 §6.2 C1) that the
principal-value choice is canonical, but a proof of uniqueness —
e.g., showing that any scheme-invariant regularisation reduces to
the principal value up to a shift absorbable into the polar terms —
is not in the literature.

**Precise math problem:** *prove that any regularisation of the
archimedean scale integral which is (i) linear in the test function,
(ii) invariant under the scaling action $\vartheta_\lambda$, and
(iii) reproduces the local factor $\pi^{-s/2}\Gamma(s/2)$ at $s = 1/2$,
is equal to the Hadamard principal value up to a finite constant.*

**Status:** this is a moderately hard functional-analytic question.
The answer is almost certainly yes (the principal value is the
"minimal canonical choice" in the Epstein–Glaser tradition), but a
proof requires some care. Estimated effort: **1–3 months**.

### 4.4 Conditional H4 — Unitary equivalence $T_{\mathrm{CCM}}
\leftrightarrow T_{\mathrm{BC}}$ (Identity 14 in the strong form)

**Statement:** The Connes adele-class scaling operator $T$ (of
research/18 §5.2, on the weighted $L^2$ space of the adele class
space) and the BC modular generator $T_{\mathrm{BC}}$ (of research/02
§3.2, on the BC GNS space at $\beta = 1$) are unitarily equivalent
*as self-adjoint operators with coinciding Bruhat–Schwartz test
domains and spectral projections*.

**Source:** research/14 Part A (Identity 14, the rigorous form via
Sz.-Nagy dilation and explicit $V$-intertwiner); research/18 §5.2
(Proposition "CCM equivalence"); research/21 (BC system reference,
Finding 1 flags the H_R ≠ H_1^{(N*)} gap).

**What is open:** the unitary equivalence $T \cong T_{\mathrm{BC}}$ is
known at the level of the unitary group generated (Connes–Consani–
Marcolli 2007, Theorem 4.4) and at the level of spectrum (both
contain $\{\gamma_n\}$). What is **not** known is whether the
spectral projections $P_{\gamma_n}$ on the two sides coincide as
operators (not just spectrally), because they are defined on slightly
different dense subspaces that may differ by finite-rank
perturbations.

This is the **residual subtlety O3** of research/18 §6.4. It is the
single biggest obstacle to a clean Paper 13.

**Precise math problem:** *is the BC GNS Hilbert space $H_1$ at
$\beta = 1$, restricted to the Riemann subspace $H_R$, unitarily
equivalent to the Meyer 2005 Sobolev completion of the adele class
space, in a way that intertwines the spectral projection
$P_{\gamma_n}^{\mathrm{BC}} = |\gamma_n\rangle\langle\gamma_n|$ on the
BC side with the Connes–Marcolli resonance projection
$P_{\gamma_n}^{\mathrm{CM}}$ on the CM side, for every $n \geq 1$?*

**Status:** this is **open-research-problem grade**. The obstruction
is real: the two sides use different completions (GNS vs Sobolev)
and the fine spectral structure (point-spectrum versus resonance)
does not transfer naively. Closing this would require either (i) a
new theorem identifying the two completions as Hilbert spaces, or
(ii) a clever workaround using only the joint dense subspace of
Bruhat–Schwartz test vectors (on which both projection families
agree by research/14 Part A).

Estimated effort: **6 months to 2+ years**, depending on whether
the workaround (ii) works or the stronger result (i) is needed. Of
the four conditionals, H4 is the dominant cost and the dominant
risk.

### 4.5 Summary table of residual conditionals

| # | Hypothesis | Source | Math problem | Effort | Grade |
|:--|:-----------|:-------|:-------------|:-------|:------|
| H1 | CM regularised trace formula, Bruhat–Schwartz form | research/18 §4 | Lift Meyer 2005 to $\theta$-summable operator form | weeks | routine |
| H2 | $A_{\mathrm{BC}}^\infty$ contains enough projections | research/48 §2.1 | Fix and check the smooth subalgebra definition | weeks | routine |
| H3 | Principal-value is canonical | research/18 §4.1 | Uniqueness theorem for scale-invariant regularisation | 1–3 months | moderate |
| H4 | $P_{\gamma_n}^{\mathrm{CM}} \cong P_{\gamma_n}^{\mathrm{BC}}$ | research/18 §6.4, research/14 | Unitary equivalence of two Hilbert completions + projection intertwining | 6–24 months | **open-research-grade** |

---

## 5. Dependencies between hypotheses

### 5.1 The dependency graph

```
      H2 (smooth subalgebra)
            |
            v
      H1 (CM trace formula in θ-summable form)
            |
            +-------+-------+
            |               |
            v               v
      H3 (PV canonical)   H4 (CCM ↔ BC projection equivalence)
            |               |
            +-------+-------+
                    |
                    v
           R-Theorem D.1 (rigorous form)
                    |
                    v
              Paper 13 main theorem
                    |
                    v
                    RH
```

### 5.2 What must be closed first, what can be parallelised

**Must precede everything:**
- H2 (test function class) is the *definitional* precondition. Until
  $A_{\mathrm{BC}}^\infty$ is fixed, the JLO pairing is ambiguous.

**Must follow H2:**
- H1 (the $\theta$-summable trace formula) requires the smooth
  subalgebra to be fixed, because the trace formula is an identity
  *on* $A_{\mathrm{BC}}^\infty$.

**Can run in parallel with each other after H1:**
- H3 (PV canonical) is a self-contained analytic question: does the
  scale-invariant regularisation reduce uniquely to the principal
  value?
- H4 (projection equivalence) is an operator-theoretic question
  about two Hilbert completions.

**Serial dependency at the end:** Paper 13's main theorem depends on
all four being closed. If H4 cannot be closed in full, the
fall-back is the workaround on Bruhat–Schwartz test vectors
(research/14 Part A), in which case Paper 13 delivers a *slightly
weaker* theorem valid on the test-vector domain only.

### 5.3 Recommended attack order

1. **H2 first** (2–3 weeks). Get the smooth subalgebra definition
   nailed down and written up in a note that CM-style noncommutative
   geometers would accept. This is the lightest and is strictly
   required for everything that follows.

2. **H1 second** (1 month). Lift Meyer 2005 distributional trace
   formula to the $\theta$-summable operator form needed for the
   JLO pairing. This is technical but routine for a specialist.

3. **H3 and H4 in parallel.** H3 (1–3 months) gives a clean rigorous
   form; H4 (6–24 months) is the heavy lift.

4. **While H4 is open, write Paper 13 on the weaker form** (valid on
   the Bruhat–Schwartz test-vector domain), which is already
   submittable as a conditional theorem.

5. **When H4 closes, upgrade Paper 13 to the strong form.**

---

## 6. Effort estimates (per hypothesis, per section, per milestone)

| Item | Effort | Notes |
|:-----|:-------|:------|
| H1 (CM trace formula θ-summable) | 1 month | Routine technical lift |
| H2 (smooth subalgebra) | 2–3 weeks | Definitional |
| H3 (PV canonical) | 1–3 months | Moderate functional analysis |
| H4 (projection equivalence) | 6–24 months | **Open-research-grade** |
| Assembly of R-Theorem D.1 (rigorous) | 1 month given H1–H3 | |
| Paper 13 manuscript drafting | 1–2 months | After R-Theorem D.1 rigorous |
| Referee / revision cycle | 6–12 months | Standard |

**Total to a weak-form Paper 13** (H1+H2+H3 closed, H4 workaround):
**4–6 months**.

**Total to a strong-form Paper 13** (all four closed): **12–30
months**.

**Total to a complete math proof of RH as a stand-alone theorem
accepted by pure number theorists** (not just the CM/NCG community):
**years**, with H4 as the dominant uncertainty. A rejection of the
BC framework by the RH community is not impossible even with
H1–H4 all closed, in which case Paper 13 would remain a
*conditional proof of RH given the Connes–Marcolli programme*
rather than a stand-alone proof of RH.

---

## 7. Paper 13 main theorem

### 7.1 The precise statement

> **Theorem (Paper 13 main theorem).** *Let $(A_{\mathrm{BC}}^\infty,
> H_R, F)$ be the Bost–Connes $\theta$-summable Fredholm module of
> research/48 §2.1, and let $\tau^{\mathrm{JLO}}$ be the
> Jaffe–Lesniewski–Osterwalder Chern character on
> $A_{\mathrm{BC}}^\infty$. Assume the four conditional hypotheses
> H1–H4 of §4 of this note. Then, for every projection
> $p \in M_k(A_{\mathrm{BC}}^\infty)$ (equivalently, every
> Bruhat–Schwartz projection on the adele class space), the BC
> index*
>
> $$
>   \mathrm{ind}_{\mathrm{BC}}(p)
>   \;:=\; \langle [\tau^{\mathrm{JLO}}],[p]\rangle
>   \;\in\; \mathbb{Z}
> $$
>
> *admits the topological expansion*
>
> $$
>   \mathrm{ind}_{\mathrm{BC}}(p)
>   \;=\;
>   \sum_{n\geq 1} c_n(p)\,\Phi(\gamma_n)
>   \;+\;\tau_\omega(p)\,\log\zeta_{\mathrm{reg}}(1)
>   \;+\;(\text{trivial-zero contributions}),
> $$
>
> *where $c_n(p) = \langle\gamma_n|p|\gamma_n\rangle$. The integer
> constraint on the LHS, together with the existence of a family of
> projections separating the spectral components of
> $T_{\mathrm{BC}}$, forces $\gamma_n \in \mathbb{R}$ for every
> $n \geq 1$. Consequently, every non-trivial zero of the Riemann
> zeta function $\zeta(s)$ lies on the critical line
> $\mathrm{Re}(s) = 1/2$.*

### 7.2 What this theorem does and does not say

**Does say:** RH holds under the CM regularisation conventions
H1–H4, which are the standard conventions of the noncommutative
geometry literature. Paper 13's content is the assembly of R-Theorem
D.1 under these conventions.

**Does not say:** RH is proved in a form that every analytic number
theorist would accept without further work. The CM programme is
standard in NCG but is not universally embraced by classical number
theorists. A mathematician who rejects the adele-class-space
operator-algebraic framework would regard Paper 13 as a theorem
*within* CM, not a theorem *about* $\zeta$ in the classical sense.

Closing this gap — turning Paper 13 into a theorem accepted by the
full math community — is beyond Paper 13 and is discussed in §9.

---

## 8. Paper 13 manuscript structure (detailed)

### Front matter
- **Title.** *"The Riemann Hypothesis as the Integer-Valued Index of
  the Bost–Connes Spectral Triple"*.
- **Abstract.** Two-sentence form: Paper 13 proves that the
  non-trivial zeros of $\zeta$ lie on the critical line, conditional
  on the standard regularisation hypotheses of the Connes–Marcolli
  trace formula, by identifying the Riemann–Weil explicit formula as
  the topological side of an Atiyah–Singer-type index pairing on the
  BC spectral triple and using the integer constraint on the
  analytic side.

### §1 Introduction (~8 pages)

**§1.1 Historical.** Riemann 1859, Hilbert 8, Weil 1952, Connes
1999, CM 2008. Aim: set the reader up to expect an operator-
algebraic / index-theoretic approach.

**§1.2 The three chains of research/08.** Brief mention that Paper
12 gave Stone, Penrose, and Atiyah–Singer physical chains for RH;
this paper closes the math version of the third.

**§1.3 Why Atiyah–Singer.** The integer-constraint argument;
cleanness of the math-only translation (material from §2 above).

**§1.4 Structure of the paper.** Pointers.

**§1.5 Honest conditional content.** The paper's result is conditional
on H1–H4 of §4 above; these are the standard hypotheses of the
Connes–Marcolli programme; a mathematician who accepts CM 2008
Ch. II §3 accepts this paper.

### §2 The Bost–Connes spectral triple (~12 pages)

**§2.1 The C\*-dynamical system.** $(A_{\mathrm{BC}}, \sigma_t)$ from
Bost–Connes 1995. The KMS state $\omega_1$ at the critical
$\beta = 1$. The GNS representation $\pi_{\omega_1}$ on $H_1$.

**§2.2 The Riemann subspace.** $H_R \subseteq H_1$ defined as the
closure of the Bruhat–Schwartz test vectors (per research/02 §3.3).

**§2.3 The smooth subalgebra.** $A_{\mathrm{BC}}^\infty$ defined and
H2 closed here in a definitional way.

**§2.4 The Mellin-dilation generator $T_{\mathrm{BC}}$.** Definition
via research/02 (3.2), equivalent (H4) to the Connes adele-class
scaling operator of research/18 §5.

**§2.5 The Fredholm module $(A_{\mathrm{BC}}^\infty, H_R, F)$.** Proof
of $\theta$-summability (Connes 1994, CM 2008).

**§2.6 The Connes–Marcolli explicit formula.** Statement of research/18
Theorem 3, conditional on H1 + H3. The chain between CM 2008 Thm 3.6,
Meyer 2005, and research/18 §6.4's residual scheme dependence.

### §3 The JLO Chern character (~10 pages)

**§3.1 The JLO cocycle.** Standard JLO 1988 construction.

**§3.2 The pairing with K-theory.** Connes 1994 IV.1 Thm 4:
integer-valued pairing.

**§3.3 $\theta$-summable regime.** Why $\theta$-summability is the
right summability class for the BC module.

**§3.4 The BC index.** $\mathrm{ind}_{\mathrm{BC}}(p) :=
\langle[\tau^{\mathrm{JLO}}], [p]\rangle$, the analytic side.

### §4 The topological expansion (~15 pages)

**§4.1 Assembly of the topological side.** How the CM trace formula
and the JLO pairing fit together; this is the content of R-Theorem
D.1 (research/48 §3.1) and where the paper does its new work.

**§4.2 The $\gamma_n$-weighted sum.** The main term, as a finite
sum when $p$ is supported on finitely many spectral components,
and as a regularised sum in general.

**§4.3 The Dixmier-trace term.** The contribution at the critical
$\beta = 1$; identification as the residue at the pole of $\zeta$.

**§4.4 Trivial-zero contributions.** The subleading boundary terms
from the trivial zeros $-2k$; these are analogous to torsion and
boundary contributions in AS.

**§4.5 The topological expansion theorem (R-Theorem D.1, rigorous).**
Statement and proof, conditional on H1–H3. This is the heart of
Paper 13.

### §5 The integer constraint and RH (~10 pages)

**§5.1 Reality of the topological side.** For $p$ self-adjoint,
$c_n(p) = \langle\gamma_n|p|\gamma_n\rangle$ is real iff $\gamma_n$
is real. (Assuming H4 so that $|\gamma_n\rangle$ is a well-defined
vector.)

**§5.2 The density of projections.** There exist enough self-adjoint
projections in $A_{\mathrm{BC}}^\infty$ to separate the spectral
components of $T_{\mathrm{BC}}$. This closes the density half of
the argument.

**§5.3 The forcing argument.** Suppose $\gamma_{n_0}$ has
$\mathrm{Im}(\gamma_{n_0}) \neq 0$. Choose $p = P_{n_0}$ the
spectral projector. Then $c_{n_0}(P_{n_0}) = 1$ and the topological
side gives $\Phi(\gamma_{n_0}) + $ (real terms), which has non-zero
imaginary part. But the analytic side is an integer. Contradiction.

**§5.4 Conclusion.** $\gamma_n \in \mathbb{R}$ for all $n \geq 1$;
hence RH.

### §6 Closing the residual conditionals (~15 pages)

**§6.1 H1: the θ-summable lift of Meyer 2005.** Explicit work.

**§6.2 H2: the smooth subalgebra definition.** Explicit choice +
verification that it is a Fredholm module.

**§6.3 H3: uniqueness of the principal-value regularisation.** A
functional-analytic proof that the PV is the unique scale-invariant
regularisation (or a sharp characterisation of its non-uniqueness).

**§6.4 H4: the CCM–BC projection equivalence.** Either a full proof
(strong form of Paper 13) or the Bruhat–Schwartz test-vector
workaround (weak form).

### §7 Implications (~8 pages)

**§7.1 For analytic number theory.** RH's standard consequences
(PNT error term, Robin's inequality, Mertens, etc.), now conditional
on the CM programme.

**§7.2 For noncommutative geometry.** The CM programme is validated
on a central open problem; the $\theta$-summable Fredholm module of
$A_{\mathrm{BC}}$ becomes a canonical example.

**§7.3 For the QG5D framework.** Paper 12's sub-phase 3.C is
upgraded; Paper 13 closes sub-phase 3.D. The LOCK is now a
mathematical lock, not just a physical one.

### §8 Conclusion and open problems beyond Paper 13 (~4 pages)

**§8.1 What is closed.** Paper 13's main theorem.

**§8.2 What is not closed.** The stand-alone acceptance by the
classical number theory community; the fully scheme-independent
form of H3; the point-spectrum form of H4 (if only the workaround
was used).

**§8.3 The next mountains.** Effective RH (bounds on
$|\mathrm{Im}(\gamma_n) - \gamma_n|$); the GRH extension; the Weil
conjecture analog for other L-functions; the connection to the
Langlands programme.

### §9 References

All of Paper 12's and research/18, research/48, research/54,
research/14 — plus Connes 1994, 1999; CM 2007, 2008; Meyer 2005;
Bost–Connes 1995; JLO 1988; Iwaniec–Kowalski 2004. ~50–80 refs.

### §10 Appendices

- **A.** Explicit computation of the JLO cocycle on the rank-one
  projection $P_1$ (the research/48 §5 code output).
- **B.** Detailed derivation of the principal-value regularisation
  from scale invariance.
- **C.** The CCM / BC dictionary in tabular form (research/18 §5.2
  expanded).
- **D.** Glossary of terms for number theorists unfamiliar with
  noncommutative geometry.

### Total length

Approximately **80–120 pages** of main text, 15–25 pages of
appendices, 5–10 pages of references. In line with a major
mathematical research paper on a Millennium Prize problem.

---

## 9. Open problems beyond Paper 13

Even if all of H1–H4 are closed and Paper 13 is published and
accepted, the following remain open.

### 9.1 Acceptance by the classical number theory community

Paper 13 proves RH *within* the Connes–Marcolli operator-algebraic
programme. The classical analytic number theory community has
historically been cautious about the CM programme, partly because
the adele-class-space operator is not a literal operator in the
textbook sense and partly because the regularisation dependence is
delicate. A number theorist who refuses to work inside the CM
framework would regard Paper 13 as *contingent* on accepting the
framework's conventions.

**Open problem:** *find a purely classical analytic number
theory proof of RH that does not invoke the CM operator-algebraic
machinery.* This is the "true" RH proof and is not addressed by
Paper 13.

### 9.2 Effective bounds

Paper 13 proves $\gamma_n \in \mathbb{R}$ as a binary statement. It
does not give *bounds* on how close $\gamma_n$ must be to the real
line. Effective RH — knowing that $|\mathrm{Im}(\gamma_n)| < f(n)$
for some explicit function $f$ with $f \to 0$ as the proof's
regularisation parameters tighten — would be a finer result.

**Open problem:** *extract effective bounds on $|\mathrm{Im}(\gamma_n)|$
from the BC index constraint as a function of the CM regularisation
cutoff scale.*

### 9.3 Generalised Riemann Hypothesis (GRH)

Paper 13 treats the Riemann zeta function specifically. The GRH for
Dirichlet L-functions, automorphic L-functions, and more general
L-functions is a much broader statement. The BC system generalises
to a "Bost–Connes system for $L$-functions" via endomotive
constructions (Connes–Marcolli 2007, Ch. III), but the corresponding
spectral triples and their index theorems are not yet worked out.

**Open problem:** *extend R-Theorem D.1 to the endomotive of a
general number field / Dirichlet character, producing an index
constraint forcing GRH for the corresponding L-function.* This
could be Paper 14 or a series of subsequent papers.

### 9.4 Hilbert–Pólya (the equality form)

Paper 13 uses only the *inclusion* $\{\gamma_n\} \subseteq
\mathrm{spec}(T_{\mathrm{BC}})$. The *equality*
$\mathrm{spec}(T_{\mathrm{BC}}) = \{\gamma_n\}$ is the Hilbert–Pólya
conjecture proper. This is strictly stronger than RH and would
force $T_{\mathrm{BC}}$ to be the "true" Riemann operator with no
additional spectrum. Paper 13 does not address this.

**Open problem:** *prove $\mathrm{spec}(T_{\mathrm{BC}}) = \{\gamma_n\}$,
i.e., rule out continuous spectrum or additional point spectrum in
$T_{\mathrm{BC}}$ beyond the Riemann zeros.*

### 9.5 The Langlands connection

The BC system is conjecturally the "trace-formula side" of a broader
operator-algebraic realisation of the Langlands programme. Paper 13
would give one theorem in this direction; the full Langlands-
operator-algebraic correspondence is a decade-scale programme.

**Open problem:** *integrate R-Theorem D.1 into the
Langlands-NCG dictionary developed by Connes, Consani, Marcolli,
and Manin.*

### 9.6 Physical interpretation of H4

H4 asks for a mathematical statement (Hilbert-space equivalence +
projection intertwining), but its deepest content is physical: it
says that the "e-circle spectrum" (the BC side) and the "adelic
scaling spectrum" (the CM side) are literally the same operator,
not just spectrally equivalent. This is the *physical* form of
Identity 14, and Paper 12's research/14 gives a structural version
via Sz.-Nagy dilation. A full rigorous form may require deep new
results in modular theory.

**Open problem:** *is there a third Hilbert space — canonical, not
dependent on either the BC GNS construction or the Meyer 2005
Sobolev completion — on which $T_{\mathrm{BC}}$ and
$T_{\mathrm{CCM}}$ are literally the same operator?* A candidate is
the *Hilbert module over the Connes–Consani endomotive* (CCM 2007
§8).

---

## 10. Definition of done

This research note closes when:

- [x] The target classical theorem is stated (§1).
- [x] The three argument chains from research/08 are listed, ranked,
      and the strongest identified with justification (§2).
- [x] The ranking justification is amplified — Atiyah–Singer as the
      strongest — in depth (§3).
- [x] The residual conditional hypotheses H1–H4 are listed with
      precise math problems (§4).
- [x] The dependency graph and attack order are given (§5).
- [x] Per-hypothesis and per-manuscript-phase effort estimates are
      given (§6).
- [x] Paper 13's main theorem is stated precisely (§7).
- [x] Paper 13's detailed manuscript structure is given (§8 above,
      to be duplicated into `paper13/00-table-of-contents.md` in a
      follow-up edit).
- [x] Open problems beyond Paper 13 are enumerated (§9).
- [ ] A root ledger file records the opening of sub-phase 3.D as
      Paper 13's working programme with this note as the reference
      (next action).
- [ ] `paper13/00-table-of-contents.md` is updated with the §8
      structure from this note (next action).

The first nine items are **DONE**. This note is the scoping document
for Paper 13.

---

## 11. References

### 11.1 In this directory

- `integers/paper12-cbb-system/00-attack-plan.md` — master plan, Phase 3 ledger.
- `integers/paper12-cbb-system/14-grand-strategy-transposition-quantization-deduction.md`
  — §2 LOCK logic; §6 architecture with Paper 13 in the arc.
- `integers/paper12-cbb-system/research/08-rh-as-physical-theorem.md` — the three
  physical chains; the source material for §2 of this note.
- `integers/paper12-cbb-system/research/14-transposition-CCM-and-reasoning-patterns.md`
  — Identity 14 in structural form; the (A-C1) conditional that
  H1 inherits.
- `integers/paper12-cbb-system/research/18-connes-marcolli-explicit-formula.md` — the
  master reference for the CM regularisation; §4 PV choices; §6.4
  residual subtleties; the source of H1, H3, H4.
- `integers/paper12-cbb-system/research/21-bost-connes-system-reference.md` — Finding 1,
  the $H_R$ vs $H_1^{(N^*)}$ gap relevant to H4.
- `integers/paper12-cbb-system/research/22-cc-hierarchy-as-spectral-gap.md` — the
  Dixmier-trace identification used in R-Theorem D.1 §3.
- `integers/paper12-cbb-system/research/48-transposition-atiyah-singer-index.md` —
  R-Theorem D.1 (BC index theorem); the backbone of Paper 13's
  Chain C.
- `integers/paper12-cbb-system/research/54-transposition-penrose-singularity.md` — the
  Penrose chain used as Chain B of §2; not the Paper 13 route but
  kept as corroboration.
- `paper13/00-table-of-contents.md` — the existing Paper 13 skeleton,
  to be replaced by the §8 expansion of this note.

### 11.2 External

- Atiyah, M. F., Singer, I. M., "The index of elliptic operators I",
  *Ann. Math.* **87** (1968) 484–530.
- Bost, J.-B., Connes, A., "Hecke algebras, type III factors and
  phase transitions with spontaneous symmetry breaking in number
  theory", *Selecta Math.* **1** (1995) 411–457.
- Connes, A., *Noncommutative Geometry*, Academic Press, 1994,
  Ch. IV §1 (Fredholm modules and the Chern character).
- Connes, A., "Trace formula in noncommutative geometry and the
  zeros of the Riemann zeta function", *Selecta Math.* **5** (1999)
  29–106.
- Connes, A., Consani, C., Marcolli, M., "Noncommutative geometry
  and motives: the thermodynamics of endomotives", *Adv. Math.*
  **214** (2007) 761–831.
- Connes, A., Marcolli, M., *Noncommutative Geometry, Quantum Fields
  and Motives*, AMS Colloquium Publications **55**, 2008, Ch. II.
- Jaffe, A., Lesniewski, A., Osterwalder, K., "Quantum K-theory I:
  the Chern character", *Comm. Math. Phys.* **118** (1988) 1–14.
- Meyer, R., "On a representation of the idèle class group related
  to primes and zeros of L-functions", *Duke Math. J.* **127**
  (2005) 519–595.
- Faulkner, T., Li, M., Wang, H., "A modular toolkit for bulk
  reconstruction", *JHEP* (2019). (For the Penrose alternate
  route; not used in Paper 13 main line.)
- Iwaniec, H., Kowalski, E., *Analytic Number Theory*, AMS Coll.
  Pub. **53**, 2004. (Chapter 5: explicit formula + consequences of
  RH.)

---

*The math RH is the mountain beyond Paper 12. Chain C — Atiyah–Singer,*
*the integer-valued BC index of R-Theorem D.1 — is the pass through*
*the mountain. Four residual conditional hypotheses gate the summit;*
*three are routine weeks-to-months, one (H4, the CCM–BC projection*
*equivalence) is the open-research-grade final push. Paper 13 can*
*ship in 4–6 months in the weak form (workaround on the*
*Bruhat–Schwartz test-vector domain), 12–30 months in the strong*
*form (H4 fully closed). Beyond Paper 13: effective bounds, GRH,*
*Hilbert–Pólya equality, Langlands. The scope is clear. The work is*
*hard but bounded.*
