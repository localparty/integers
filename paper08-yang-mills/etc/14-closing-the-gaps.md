# Closing the Three Remaining Gaps: Research Agent Instructions

The hostile referee identified three gaps in the release candidate.
All three have concrete proposed remedies. Your job is to execute
those remedies.

Read this entire document before doing anything. Then read the
files listed for each gap before starting work on that gap.

**Execution order:** Gap A first (it is the only genuine gap and
determines what the paper claims), then Gap B (formal revision,
straightforward once the approach is clear), then Gap C (writing,
standard material).

**Output:** For each gap, produce a written deliverable (a new or
revised preprint section) in the locations specified. Do not modify
any file not listed as an output target.


---


## Required Reading (before any work)

1. `/Users/gsix/yang-mills/hostile-review/report.md`
   — The full hostile review. Read Points 1, 3, and 4 carefully.

2. `/Users/gsix/yang-mills/preprint/sections/04-lattice-proof-part1.md`
   — Sections 4.5 (Theorem 5, the proof sketch) and 4.1 (transfer
   matrix definition). Know exactly what exists now.

3. `/Users/gsix/yang-mills/preprint/sections/05-continuum-limit.md`
   — Sections 5.5.2-5.5.3 (Definition 2.1 and the spectral lemma
   proof). Know exactly what exists now.

4. `/Users/gsix/yang-mills/preprint/sections/C-transfer-matrix.md`
   — The existing transfer matrix appendix. You will extend it.


---


## Gap A: Theorem 5 — Reduced Transfer Matrix Proof

### What exists now

Section 4.5 contains a "Proof sketch" of Theorem 5 (IR equivalence)
using Wilsonian decoupling (Appelquist-Carazzone 1975). The hostile
reviewer correctly identified this as a genuine gap: Appelquist-
Carazzone is a perturbative theorem and cannot establish the non-
perturbative equivalence between the KK-enhanced and standard theories.

The current proof sketch establishes:
- KK modes have mass $m_1 = 2\sqrt{3}/r_3 \sim 10^{15}$ GeV
- Wilson loop corrections are $e^{-m_1 R} \sim e^{-10^{28}}$ at
  physical separations
- The effective action correction to $\sigma$ scales as
  $(\Lambda_\text{QCD}/m_1)^2 \sim 10^{-26}$

These are physically correct but mathematically the argument is
perturbative. What is needed is a non-perturbative operator-theoretic
proof.

### The approach: reduced transfer matrix

The key insight proposed by the hostile reviewer: the KK mode
integration at a *single time slice* is a finite-dimensional
computation, not an infinite RG flow. This makes it tractable.

**Setup.** Both theories have transfer matrices acting on the Hilbert
space of a single time-slice configuration:

- $\hat{T}_\text{KK}$: acts on $\mathcal{H}_\text{KK} = L^2(SU(N)^{|\Lambda_t^1|}) \otimes \mathcal{H}_\text{int}$, where $\mathcal{H}_\text{int} = \bigotimes_{x \in \Lambda_t} L^2(\mathcal{A}_0(\mathbb{CP}^{N-1}))$ is the internal (KK) Hilbert space.

- $\hat{T}_\text{std}$: acts on $\mathcal{H}_\text{std} = L^2(SU(N)^{|\Lambda_t^1|})$, the 4D gauge field Hilbert space.

**Definition of $\hat{T}_\text{red}$.** Define the reduced transfer
matrix by integrating out the internal fields:

$$\hat{T}_\text{red} \;=\; \text{Tr}_{\mathcal{H}_\text{int}}\bigl[\hat{T}_\text{KK} \cdot \hat{P}_0\bigr]$$

where $\hat{P}_0$ is the projector onto the sector where all internal
fields are in their ground state (the $k=0$ vacuum of the KK modes).
More concretely:

$$(\hat{T}_\text{red}\,\psi)(U') = \int d\mu_\text{int}(A,A')\; (\hat{T}_\text{KK}\,(U',A';\,U,A))\; \psi(U)$$

where the integration is over the internal field configuration at both
adjacent time slices, weighted by the internal measure.

**The three claims to prove:**

**Claim 1: $\hat{T}_\text{red}$ is well-defined.**
The integration over $A, A'$ with the Gaussian internal measure is
finite because $\mathbb{CP}^{N-1}$ is compact and the internal action
$S_\text{int}[A]$ provides Gaussian damping of all KK modes. The
integral is absolutely convergent.

**Claim 2: $\|\hat{T}_\text{red} - \hat{T}_\text{std}\|_\text{tr} \leq C e^{-m_1 a}$.**
The difference between the reduced and standard transfer matrices is
trace-class and exponentially small in $m_1 a$. This follows from
the same cluster expansion machinery that bounds the bond activities
in Theorem 2 (Section 4.3). The internal field integration at a
single time slice generates corrections to the effective 4D action
that are suppressed by $e^{-m_1 a}$ per time step.

**Claim 3: $|\Delta_0^\text{std} - \Delta_0^\text{red}| \leq C e^{-m_1 a}$.**
Apply Kato-Rellich perturbation theory: if $\hat{T}_\text{red} -
\hat{T}_\text{std}$ is trace-class with norm $\epsilon$, then the
eigenvalues of $\hat{T}_\text{std}$ and $\hat{T}_\text{red}$ differ
by at most $O(\epsilon)$. Since the mass gap is
$\Delta_0 = -\frac{1}{a}\ln(\lambda_1/\lambda_0)$, a perturbation
of size $\epsilon$ in the eigenvalues changes $\Delta_0$ by at most
$O(\epsilon/(\lambda_0 - \lambda_1)) = O(\epsilon/\hat{\Delta}_0)$.

**Claim 4: $\Delta_0^\text{red} = \Delta_0^\text{KK}$ in the
relevant spectral sector.**
The lightest state in $\mathcal{H}_\text{KK}$ that couples to 4D
gauge-invariant observables is the glueball at mass $\Delta_0^\text{KK}$.
The KK excitations have mass $m_1 \gg \Delta_0^\text{KK}$. Therefore
the spectral projection from $\hat{T}_\text{KK}$ to $\hat{T}_\text{red}$
(integrating out the internal sector) preserves the lowest 4D gap.
Concretely: the eigenvalue $\lambda_0(\hat{T}_\text{KK})$ corresponds
to a state with all KK modes in their ground state (the 4D vacuum), and
$\lambda_1(\hat{T}_\text{KK})$ corresponds to the lightest glueball
(also with KK modes in their ground state, since the first glueball
has mass $\ll m_1$). The reduced matrix $\hat{T}_\text{red}$ preserves
exactly these two eigenvalues.

**Combining the claims:**
$$\Delta_0^\text{std} \geq \Delta_0^\text{red} - Ce^{-m_1 a}
  = \Delta_0^\text{KK} - Ce^{-m_1 a} > 0$$

since $\Delta_0^\text{KK} > 0$ (Theorem 4) and $Ce^{-m_1 a} \sim
e^{-10^{15}}$ is negligible.

### What to write

Produce a complete proof of Theorem 5, replacing the current proof
sketch. The output is a revised version of Section 4.5.

**Write this into a new file:**
`/Users/gsix/yang-mills/preprint-verification/theorem5-proof.md`

Do not modify the preprint directly. The file should contain:

1. **The revised theorem statement** (keep the same statement as
   now — the conclusion is correct, only the proof changes).

2. **The proof** — rigorous, following the four claims above. For
   each claim:
   - State it precisely as a lemma.
   - Prove it. Reference the relevant tools: the KK cluster expansion
     (Theorem 2, Section 4.3) for Claim 2; Kato-Rellich for Claim 3;
     spectral separation for Claim 4.
   - The proof of Claim 2 is the most substantive — it requires
     bounding the trace norm of $\hat{T}_\text{red} - \hat{T}_\text{std}$.
     Use the transfer matrix representation and the bond activity bound
     $|g_b| \leq C_0 e^{-m_1 a}$ from Theorem 2.

3. **A remark** at the end: "This proof replaces the proof sketch in
   the original version of Section 4.5. The Wilsonian decoupling
   argument (Appelquist-Carazzone 1975) provided the physical
   intuition; the transfer matrix argument above makes it rigorous."

4. **At the very end:** an honest assessment in a comment block:
   `<!-- ASSESSMENT: [PROVED / ARGUED / GAP REMAINS] -- [why] -->`

   Be honest. If Claim 2 requires more work than you can do in this
   file, say so precisely and state what additional input is needed.
   A partial proof that identifies exactly where it needs more work
   is much better than a false proof.

### Key references to use
- Kato, T.: *Perturbation Theory for Linear Operators* (1966),
  Section VII.3 (eigenvalue perturbation, trace-class perturbations).
- Reed, M., Simon, B.: *Methods of Modern Mathematical Physics* Vol. IV
  (1978), Section XIII.4 (Kato-Rellich theorem for operators).
- The transfer matrix for lattice gauge theory: Seiler, E.: *Gauge
  Theories as a Problem of Constructive Quantum Field Theory and
  Statistical Mechanics* (1982), Chapter 2.
- The bond activity bound: use Theorem 2 from Section 4.3 of the
  preprint directly.


---


## Gap B: Definition 2.1 and the Spectral Lemma

### What exists now

Section 5.5.2 defines the excitation number $\mathrm{exc}(\mathcal{O})$
as the minimum number $p$ such that all intermediate-state tuples
$\mathbf{n}$ with $W_\alpha^{(m)}(\mathbf{n}) \neq 0$ have
$\#(\mathbf{n}) \geq p$ (where $\#(\mathbf{n})$ counts the number of
non-ground-state intermediate slots).

The hostile reviewer found (Point 1(d) and Point 3): for
$\text{Tr}(D_0 F)^2$ with one $\hat{T}$-insertion, the vacuum
intermediate state ($n_1 = 0$) has $\#(n_1=0) = 0 < 2$ but nonzero
weight $(e^{\hat{\Delta}}-1)^2 \neq 0$. So Definition 2.1 formally
gives $\text{exc}(\text{Tr}(D_0 F)^2) = 0$, not $\geq 2$. The bound
$O(\hat{\Delta}^2)$ is still correct — but it comes from the
*vanishing order* of the Boltzmann weight at the diagonal $n=m$,
not from the absence of low-excitation channels.

### The fix: Boltzmann deviation order

Replace Definition 2.1 with a new definition that captures what the
argument actually uses.

**New definition (to write):**

Define the *Boltzmann deviation order* $\mathrm{dev}(\mathcal{O}) \geq p$
to mean: the weight function $W_\alpha^{(m)}(\mathbf{n})$ vanishes to
order $\geq p$ at the diagonal configuration $\mathbf{n} = (m, m, \ldots, m)$.

More precisely, for a single-insertion operator ($R=1$):
$$\mathrm{dev}(\mathcal{O}) \geq p \iff (e^{E_m - E_{n_1}} - 1)^R \cdot |\langle m|\mathcal{O}|n_1\rangle|^2 = O((E_m - E_{n_1})^p) \text{ as } n_1 \to m$$

For the multi-insertion case: the weight vanishes to order $p$ at
the diagonal means each of the $R$ Boltzmann factors contributes at
least one power of $(E_m - E_n - E_n')$, and the total vanishing
order is $\geq p$.

For $\text{Tr}(D_0 F)^2$ with $R=1$: the weight $(e^{E_m - E_{n_1}}-1)^2$
vanishes to order 2 at $n_1 = m$ (since $(e^x-1)^2 \sim x^2$ as $x\to 0$).
So $\mathrm{dev}(\text{Tr}(D_0 F)^2) \geq 2$. This is the correct
statement.

**Revised spectral lemma (to write):**

State the lemma with hypothesis $\mathrm{dev}(\mathcal{O}) \geq p$
instead of $\mathrm{exc}(\mathcal{O}) \geq p$. The proof modification
is:

Old Step 1: "Restrict to intermediate-state tuples with $\#(\mathbf{n}) \geq p$."
New Step 1: "Factor out $p$ powers of $(e^{E_m - E_{n}} - 1)$ from
the weight $W^{(m)}(\mathbf{n})$, using the hypothesis that the weight
vanishes to order $p$ at the diagonal."

The bound $|e^{E_m - E_n} - 1| \leq C|E_m - E_n| \leq C\hat{\Delta}$
(since the one-particle gap is $\hat{\Delta}$) then gives $p$ powers
of $\hat{\Delta}$ from the $p$ extracted factors. Steps 2-5 proceed
as before.

**Verify:** Show explicitly that the revised definition and lemma
reproduce the bound $|\langle 1|\text{Tr}(D_0 F)^2(0)|1\rangle_c|
\leq C M \hat{\Delta}^2$ by the revised argument.

**Also check:** The stability-of-excitation-number argument in
Section 5.6, Part III uses $\mathrm{dev} \geq 2$ for the full
non-perturbative operator $\delta E_k^{d=6}$. Verify that the
argument still goes through with the new definition: the two-derivative
operators $\text{Tr}(DF)^2$ have weight vanishing to order 2 at the
diagonal (structural zero from the squared temporal difference), and
this property is preserved under analytic continuation (B1).

### What to write

Produce the revised definition and lemma text. Write to:
`/Users/gsix/yang-mills/preprint-verification/definition-revision.md`

The file should contain:

1. **The revised Definition 2.1** — complete, self-contained, in
   LaTeX-compatible markdown. This replaces the current Definition
   2.1 in Section 5.5.2.

2. **The revised Spectral Lemma** (Section 5.5.3) — the statement
   with the new hypothesis, and the proof with the modified Step 1.
   Steps 2-5 can be copied from the current text with minimal changes;
   mark explicitly which steps change and how.

3. **Verification for $\text{Tr}(D_0 F)^2$** — show explicitly that
   the revised definition gives $\mathrm{dev} \geq 2$ and the revised
   proof gives the $O(\hat{\Delta}^2)$ bound.

4. **Verification for $\delta E_k^{d=6}$** — confirm the stability
   argument goes through with the new definition.

5. **A note on the old definition** — one paragraph explaining why
   the old Definition 2.1 was incorrect (the vacuum intermediate
   has $\#=0$ but nonzero weight) and how the new definition fixes
   this without changing the mathematical content.


---


## Gap C: OS Axioms — Expanded Verification

### What exists now

Section 5.7(f) currently has five short paragraphs (one per axiom),
written as part of the previous verification pass. The hostile reviewer
assessed these as correct but flagged:

- **OS1:** The connected→full implication uses the linked cluster
  theorem but doesn't state it.
- **OS2:** The rate of O(4) restoration is stated as $O(a^2\Lambda^2)$
  but the derivation is not given.
- **OS reconstruction:** The simultaneous verification for a single
  convergent subsequence needs to be stated explicitly.

### What to write

Produce the expanded OS axiom verification. Write to:
`/Users/gsix/yang-mills/preprint-verification/os-axioms-expansion.md`

The file should contain a complete replacement for Section 5.7(f)
that a mathematician could verify without further thought. Specifically:

**OS1 (Temperedness):**

State and apply the linked cluster theorem: the full $n$-point function
$S_n(x_1,\ldots,x_n)$ is expressed as a sum over partitions of products
of connected Schwinger functions $S_{|I|}^c$. Each connected function
decays exponentially by the cluster expansion (Section 4.3). Show that
the sum over partitions produces at most a factorial combinatorial
factor (bounded by $n!$ or equivalently $e^n$ in an appropriate norm),
giving overall polynomial growth. This is stronger than the polynomial
growth required for temperedness.

Be explicit: "The full $n$-point Schwinger function satisfies
$|S_n(x_1,\ldots,x_n)| \leq C^n \sum_{\pi} \prod_{I \in \pi}
e^{-\Delta_\infty \cdot \text{diam}(I)}$ where the sum is over
partitions $\pi$ of $\{1,\ldots,n\}$ and $\text{diam}(I) =
\max_{i,j \in I}|x_i - x_j|$." Then bound the sum over partitions.

**OS2 (Euclidean covariance):**

The O(4)-breaking operators in the effective action have engineering
dimension 6 (the leading lattice artifacts are $\text{Tr}(DF)^2$ with
specific index contractions that break O(4) to the hypercubic subgroup).
Their coefficients are $O(g_k^4)$ from Balaban's estimates. On the RG
trajectory, $g_k^4 \to 0$ as $k \to \infty$, and the coefficient of
the O(4)-breaking operator scales as $g_k^4 \cdot (a_k\Lambda)^2$
(where the $(a_k\Lambda)^2$ comes from the dimension-6 suppression).
This vanishes as $a \to 0$.

State the rate explicitly: "$O(4)$-breaking corrections to $n$-point
Schwinger functions are $O(a^2\Lambda^2)$, vanishing in the continuum
limit." Cite the Symanzik improvement program (Symanzik 1983) as the
standard reference for this calculation.

**OS3 (Reflection positivity):**

Two-sentence argument: The Wilson action is reflection-positive for all
$a > 0$ by Osterwalder-Seiler (1978). Weak limits of reflection-positive
functionals are reflection-positive (this follows from the definition of
reflection positivity as a quadratic form condition, which is preserved
under weak limits by the lower semicontinuity of quadratic forms).

**OS4 (Symmetry):** One sentence.

**OS5 (Cluster decomposition):**

The mass gap $\Delta_\infty > 0$ implies exponential clustering: for
any local observables $A, B$ separated by distance $t$,
$|\langle AB(t) \rangle - \langle A \rangle\langle B \rangle|
\leq C e^{-\Delta_\infty t}$. This is the cluster decomposition
property (OS5). The proof: $|\langle AB(t)\rangle - \langle A\rangle
\langle B\rangle| = |\langle A(\hat{T}^{t/a} - \lambda_0^{t/a}
\hat{P}_0)B\rangle| \leq \|A\|\cdot\|B\|\cdot(\lambda_1/\lambda_0)^{t/a}
= \|A\|\cdot\|B\|\cdot e^{-\Delta_\infty t}$.

**OS reconstruction and simultaneity:**

End with a paragraph: "Each of the five axioms holds uniformly in $a$:
OS1 by the uniform cluster expansion bounds, OS2 at rate $O(a^2)$,
OS3 for every $a > 0$, OS4 automatically, OS5 because $\Delta_\infty
> 0$ is $a$-independent. The Banach-Alaoglu theorem (applied to the
space of tempered distributions with the OS1 bound as the bounding
norm) guarantees that at least one subsequence of lattice Schwinger
functions converges as $a \to 0$. For this subsequence, all five
axioms hold simultaneously (they hold for each $a > 0$, hence for
the limit). The Osterwalder-Schrader reconstruction theorem (1973,
1975) then gives a Wightman QFT satisfying all Wightman axioms."


---


## Constraints

1. **Do not modify preprint files directly.** All output goes to
   `/Users/gsix/yang-mills/preprint-verification/`. The preprint
   will be updated in a subsequent pass based on your deliverables.

2. **Be honest about what is proved and what is argued.** Every
   deliverable should end with an assessment comment:
   `<!-- ASSESSMENT: ... -->`.
   For Gap A especially: if the Claim 2 proof (trace-norm bound on
   $\hat{T}_\text{red} - \hat{T}_\text{std}$) is a sketch rather
   than a complete proof, say so and state precisely what additional
   input is needed.

3. **Do not invent new mathematics.** Use only:
   - The transfer matrix and cluster expansion machinery already in
     the preprint (Sections 4.1-4.4)
   - Standard operator theory (Kato, Reed-Simon)
   - Standard functional analysis (Banach-Alaoglu, Weierstrass)
   - The existing Balaban extraction (Appendix H, Section 5.6)

4. **Gap A is the priority.** If you run out of space or time,
   deliver Gap A first, then Gap B, then Gap C.

5. **Preserve all existing [CONFIRMED] markers.** The three Balaban
   verification items remain confirmed. Do not reopen them.
