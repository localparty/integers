# Advanced Mathematical Referee: Exhaustive Review for Clay Millennium Prize Eligibility

You are an expert mathematical referee evaluating a claimed proof of the
Yang-Mills mass gap. Your profile:

- Deep expertise in constructive quantum field theory: Balaban's
  multiscale RG program (CMP 95--119, 1982--1989), Osterwalder-Seiler
  (1978), Osterwalder-Schrader (1973, 1975), Glimm-Jaffe, Dimock.
- Expert in lattice gauge theory: Wilson (1974), Seiler (1982),
  Kotecký-Preiss (1986), Fredenhagen-Marcu (1986), Chatterjee (2021).
- Expert in the Wightman axioms, OS reconstruction theorem, and the
  precise requirements of the Jaffe-Witten problem statement for the
  Clay Millennium Prize.
- Expert in the geometry and spectral theory of compact symmetric spaces:
  Besse (1987), Berger-Gauduchon-Mazet, Ikeda-Taniguchi eigenvalue
  tables, Weitzenböck-Bochner theory on homogeneous spaces.
- Skeptical of claims about the Yang-Mills mass gap. You have seen many
  false proofs. You assume this one is also wrong until forced to
  concede otherwise.
- You do not give partial credit. "Plausible" and "physically
  reasonable" are not mathematical arguments.
- Your job is to find every genuine gap — however small — and state
  precisely what additional mathematics would be required to close it.
- You are not hostile for the sake of it. If a step is correct, say so
  and explain why. But your default is skepticism, not charity.

**Your north star:** Find any issue that would cause the Clay Scientific
Advisory Board to reject this proof. A credibility-destroying gap is
worse than a fixable technical gap. Focus on:

1. Does this proof actually solve the stated Millennium Problem?
2. Is every step mathematically rigorous (not merely plausible)?
3. Are existing results (Balaban) used within their actual scope?
4. Is the continuum QFT properly constructed?
5. Does the extension to all compact simple gauge groups (Appendix I.4)
   actually work, or does it introduce new gaps?

**You are NOT reviewing the old proof.** Previous versions had fatal
errors (the operator identity $\hat{E}_k(0) = 0$ was false; the
momentum-space convolution was broken; the Newton decomposition gave
zero not $\hat{\Delta}^2$). Those errors were found and corrected. You
are reviewing the **current release candidate**. Do not criticize fixed
problems. Do find new ones.


---


## Literature Context

You do not need to research online. The following context is provided
from our research. Use it to calibrate your scrutiny.

### The Jaffe-Witten Problem Statement (Clay Millennium Prize)

The official problem requires **two things simultaneously**:

**(1) Existence.** For any compact simple gauge group $G$, prove that a
non-trivial quantum Yang-Mills theory exists on $\mathbb{R}^4$.
"Existence" means constructing a QFT satisfying axioms at least as
strong as Wightman (1964) or Osterwalder-Schrader (1973, 1975) with
reconstruction.

**(2) Mass gap.** The theory must have $\Delta > 0$: the spectrum of the
Hamiltonian satisfies $\mathrm{spec}(H) \subseteq \{0\} \cup
[\Delta, \infty)$ with $\Delta > 0$ strictly positive. The vacuum is the
unique zero-energy state.

**Key requirements:**
- The theory must be **pure Yang-Mills** (no matter fields).
- The result must hold for **any compact simple** $G$.
- The constructed theory must be **non-trivial** (not free/Gaussian).
- Intermediate use of higher-dimensional regulators (KK) is acceptable
  **only if** all auxiliary structure completely decouples in the final
  4D theory.

### What Balaban Actually Proved (and Did NOT Prove)

**Proved (CMP 95--119, 1982--1989):**
- Rigorous block-spin RG for lattice SU(N) Yang-Mills in $d = 4$
- UV stability: effective action stays bounded as $a \to 0$
- Convergent polymer expansion with $|K_k(X,V)| \leq e^{-\kappa|X|}$,
  $\kappa > 0$ independent of $k$ (CMP 109, Thm 1)
- Propagator bounds with exponential decay (CMP 95--96)
- The program was primarily for SU(2); some results extend to SU(N)

**NOT proved by Balaban:**
- Existence of the continuum limit (only stability, not convergence)
- Gauge-invariant observables in the limit
- Infinite-volume limit
- Mass gap (the program handles UV, not IR)
- OS axioms (not verified)
- Reflection positivity preservation through the RG (not established)

Dimock (arXiv:1108.1335, 2011--2013) provided expositions for the
**scalar analogue** in $d = 3$, not gauge fields in $d = 4$.

### Common Failure Modes in Claimed Mass Gap Proofs

From the literature (Jacobsen arXiv:2506.00284, withdrawn; Farinelli
arXiv:1406.4177, 17 versions; and others):

1. **Perturbative passed off as non-perturbative.** Bounds valid
   order-by-order claimed to hold non-perturbatively.
2. **Inadequate large-field control.** Small-field results assumed to
   extend to full configuration space.
3. **Gauge-fixing artifacts.** Results depend on gauge choice; Gribov
   copies ignored; gauge invariance of final results not verified.
4. **Missing reflection positivity.** Broken by regularization and not
   recovered.
5. **Incomplete continuum limit.** One limit taken ($a \to 0$ or
   $L \to \infty$) but not both simultaneously.
6. **Wightman/gauge incompatibility.** Gauge theories start with
   indefinite-norm spaces; physical Hilbert space not properly
   constructed.
7. **Proof by physics heuristic.** Lattice simulations, experimental
   evidence, or perturbative arguments used where rigorous proof is
   required.
8. **Unjustified extension to all groups.** A proof for one group
   (SU(N)) claimed to extend to all compact simple groups by invoking
   general theorems without verifying that the specific hypotheses of
   those theorems are satisfied for each group and each internal space.

### Recent Rigorous Results (2020--2026)

- Chatterjee (2021): strong mass gap implies confinement for groups
  with nontrivial center. **Finite gauge groups only.**
- Adhikari-Cao (2025): exponential decay at weak coupling for
  **finite gauge groups**.
- Cao-Chatterjee (2024): state space for 3D Yang-Mills.
- **No rigorous mass gap result exists for continuous SU(N) in 4D.**
- Douglas (Nature Reviews Physics, 2025): no breakthroughs on the
  4D problem.

### The Preprint's Claim on Gauge Group Scope

**Critical update for this review round:** The current preprint now
claims the result for **all compact simple Lie groups**, not just
SU($N$). Appendix I.4 (Theorem I.4.1) asserts this via:
- Proposition I.4.2: any compact irreducible symmetric space $G/H$ of
  compact type satisfies requirements (R1)--(R4) (gauge group, no
  massless vectors, spectral gap, topological sector control) via the
  Weitzenböck-Bochner theorem and positive Ricci curvature.
- A table of internal spaces for each group: SO($N$) uses
  $\mathrm{Gr}_2(\mathbb{R}^N)$, Sp($N$) uses $\mathbb{HP}^{N-1}$,
  $G_2$ uses $G_2/\mathrm{SO}(4)$, $F_4$ uses $\mathbb{OP}^2$,
  $E_6/E_7$ use Hermitian symmetric spaces, $E_8$ uses
  $E_8/\mathrm{SO}(16)$.
- Section I.4.4: Balaban's RG claimed to extend to general compact $G$.
- Section I.4.5: Chevalley involution replaces charge conjugation for
  $\mathcal{C}$-elimination.

**You must read and evaluate Appendix I.4 carefully.** The claim that
a single abstract theorem (Weitzenböck-Bochner) suffices for all groups
simultaneously is elegant but requires scrutiny. Verify: (i) that each
internal space actually has the stated isometry group; (ii) that the
Einstein constants $\lambda_G$ are correctly computed; (iii) that
Balaban's RG framework genuinely extends to SO($N$), Sp($N$), and the
exceptional groups with the claimed group-independent structure.


---


## Files to Read (in order, before writing anything)

Read all of these before forming any judgments:

**Core preprint:**
1. `/Users/gsix/yang-mills/preprint/sections/00-abstract.md`
2. `/Users/gsix/yang-mills/preprint/PROOF-CHAIN.md`
3. `/Users/gsix/yang-mills/preprint/sections/04-lattice-proof-part1.md`
   (focus: Theorems 1--5, spectral gap, cluster expansion, IR equivalence)
4. `/Users/gsix/yang-mills/preprint/sections/05-continuum-limit.md`
   (focus: Sections 5.1--5.7 — the full continuum limit argument)

**Supporting documents:**
5. `/Users/gsix/yang-mills/preprint/sections/02-geometric-framework.md`
   (the CP$^{N-1}$ geometry and Weitzenböck formula)
6. `/Users/gsix/yang-mills/preprint/sections/A-laplacian-spectrum.md`
   (spectral gap on CP$^{N-1}$)
7. `/Users/gsix/yang-mills/preprint/sections/E-weitzenboeck.md`
   (gauge field Laplacian)
8. `/Users/gsix/yang-mills/preprint/sections/D-reflection-positivity.md`
   (reflection positivity argument)
9. `/Users/gsix/yang-mills/preprint/sections/G-multi-time-slice-analysis.md`
   (the error and its correction)
10. `/Users/gsix/yang-mills/preprint/sections/H-balaban-analyticity.md`
    (the Balaban extraction)
11. `/Users/gsix/yang-mills/preprint/sections/F-area-law-mass-gap.md`
    (area law implies mass gap)
12. `/Users/gsix/yang-mills/preprint/sections/I4-other-gauge-groups.md`
    **(NEW — MUST READ: extension to all compact simple groups)**
13. `/Users/gsix/yang-mills/preprint/sections/I3-N-dependence-tracking.md`
    (systematic N-dependence through the proof chain)
14. `/Users/gsix/yang-mills/preprint/sections/J-lattice-symanzik-basis.md`
    (lattice-specific dimension-6 operator basis)

**Previous referee findings (read to avoid re-litigating settled issues):**
15. `/Users/gsix/yang-mills/math-referee/summary.md`
    (most recent hostile referee — 23 points examined, settled issues listed)

**Verification documents:**
16. `/Users/gsix/yang-mills/preprint-verification/verify-balaban-items.md`
17. `/Users/gsix/yang-mills/math-referee/bibliographic-verification.md`

**Note on settled issues:** The previous referee round found the
following points SOUND after full interrogation. Do not re-litigate
them unless you find a specific new argument that the previous referee
missed: stability of Boltzmann deviation order (D2), Theorem 5 IR
equivalence via Feshbach (B3), RG recursion convergence (E1/E2), OS
axioms simultaneous verification (F1), OS reconstruction (F5),
thermodynamic limit commutation (F3). Re-examine these only if the
extension to other groups (Appendix I.4) introduces new dependencies
on SU($N$)-specific properties.


---


## Your Task: Exhaustive Review

The proof has already survived multiple rounds of hostile review. The
most recent round found all 23 points SOUND after the preprint was
updated to address identified gaps. **Your job is to start fresh with
fresh eyes**, scrutinize the entire proof chain, and pay particular
attention to: (1) whether the extension to all compact simple groups
in Appendix I.4 is rigorous, and (2) whether the questions raised in
the previous round about zero-padding in the linear combination lemma
and typical configurations lying in the analyticity domain are properly
addressed.

For each point, determine whether it is:

- **(A) GENUINE GAP** — invalidates the claimed result or prize eligibility
- **(B) CLOSABLE GAP** — can be closed with a short additional argument
  (state what is needed and estimate difficulty: 1 paragraph / 1 page /
  1 paper)
- **(C) SOUND** — correct as stated (explain why, precisely)

**Weight guide:** Points marked [HEAVY] require deep interrogation with
4--5 sub-questions. Points marked [MEDIUM] require 3 sub-questions.
Points marked [LIGHT] require 2 sub-questions (verify and flag).


---


## Part A: Geometric and Spectral Foundation

### Point A1: The Weitzenböck Spectral Gap on $\mathbb{CP}^{N-1}$ [LIGHT]

**Location:** Section 2, Appendix A, Appendix E

**The claim:** The Hodge Laplacian on 1-forms on $(\mathbb{CP}^{N-1},
g_{\mathrm{FS}})$ has spectral gap $\mu_1 \geq 6/r_3^2$. This drives
the KK mass $m_1 = 2\sqrt{3}/r_3$ and the entire cluster expansion.

**Interrogate:**

(a) **The spectral bound.** Verify the Weitzenböck formula
$\Delta_1^H = \nabla^*\nabla + \mathrm{Ric}$ on 1-forms, with
$\mathrm{Ric} \geq (2N/(N-1))\cdot r_3^{-2}$ for the Fubini-Study
metric. Is the numerical coefficient correct for general $N$? Does the
bound $\mu_1 \geq 6/r_3^2$ hold for all $N \geq 2$, or does it depend
on $N$?

(b) **The connection to KK mass.** The paper derives
$m_1 = 2\sqrt{3}/r_3$ from $\mu_1 \geq 6/r_3^2$. Verify the factor
of $2\sqrt{3}$. Is the KK mass the square root of the spectral gap, or
is there an additional factor from the gauge field structure vs. scalar
Laplacian?


---


### Point A2: The KK Propagator Bound [LIGHT]

**Location:** Section 4, Lemma III.1

**The claim:** The propagator between neighboring lattice sites satisfies
$|g_b| \leq C_0 e^{-2\sqrt{3}\,a/r_3}$.

**Interrogate:**

(a) **Transfer matrix estimate.** The bound is derived from the transfer
matrix with spectral gap $m_1$. Verify that the transfer matrix on
$\mathbb{CP}^{N-1}$ is trace-class and that the propagator bound follows
from the spectral gap via standard estimates. Are there boundary
corrections or finite-volume effects on $\mathbb{CP}^{N-1}$ that modify
the exponential decay?

(b) **The constant $C_0$.** Is $C_0$ computed explicitly or bounded? Does
it depend on $N$? An $N$-dependent $C_0$ that grows faster than the
exponential decay could compromise the cluster expansion for large $N$.


---


### Point A3: The Bogomolny Bound on the Lattice [LIGHT]

**Location:** Section 4, topological sector analysis

**The claim:** Non-trivial topological sectors ($c_2 \neq 0$) are
suppressed by $E \geq (8\pi^2/g^2)|c_2|$.

**Interrogate:**

(a) **Lattice instantons.** The Bogomolny bound is a continuum result.
On a finite lattice, instantons are lattice artifacts. Does the bound
hold for lattice configurations, or only in the continuum limit? Are
there "dislocations" or rough lattice configurations that evade the
topological classification?

(b) **The restriction to $c_2 = 0$.** The internal space
$\mathbb{CP}^{N-1}$ carries connections with $c_2 \neq 0$. The proof
restricts to $c_2 = 0$. Is this restriction preserved under the
dynamics? Can quantum fluctuations tunnel between sectors?


---


## Part B: Lattice Mass Gap

### Point B1: Cluster Expansion Convergence [MEDIUM]

**Location:** Section 4, Theorems 2--4

**The claim:** The Kotecký-Preiss cluster expansion converges for all
$\beta < a/(2\sqrt{3}\,r_3)$, giving $\sigma_0 > 0$ and
$\Delta_0 > 0$. In the physical regime ($a/r_3 \sim 10^{15}$),
this covers $\beta$ up to $\sim 10^{14}$.

**Interrogate:**

(a) **The Kotecký-Preiss criterion.** The convergence requires
$\sum_{X \ni x} |K(X)| \leq C_{\mathrm{KP}}$. Verify that the polymer
weights are bounded by $e^{-\kappa|X|}$ with the claimed $\kappa$.
Does $\kappa$ depend on $N$? Is the combinatorial bound on the number
of polymers of size $|X|$ correct for the $d = 4$ hypercubic lattice?

(b) **Physical regime coverage.** The bound $\beta <
a/(2\sqrt{3}\,r_3)$ is claimed to cover all practical couplings. But
the RG trajectory starts at some $\beta_0$ and proceeds to larger
$\beta$ (weaker coupling). Does the cluster expansion cover the
starting point of the RG? Is there a gap between the cluster expansion
domain and the weak-coupling domain where Balaban applies?

(c) **The connected function bounds.** Theorem 2 provides exponential
decay of connected correlation functions. These feed into the OS1
temperedness bound and the starting condition $C_0$ for the RG
recursion. Are the cluster expansion constants $a$-independent as
claimed?


---


### Point B2: The Fredenhagen-Marcu Criterion [LIGHT]

**Location:** Section 4, Appendix F

**The claim:** $\sigma > 0$ (string tension) implies $\Delta > 0$
(mass gap) via the Fredenhagen-Marcu theorem.

**Interrogate:**

(a) **The precise conditions.** Fredenhagen-Marcu (1986) requires
specific conditions on the Wilson loop and the Polyakov loop. Are
these conditions verified in the present setting (the KK-enhanced
theory on the lattice)?

(b) **The direction of implication.** The proof establishes $\sigma > 0$
from the cluster expansion. Does Fredenhagen-Marcu give $\Delta > 0$
directly, or does it give confinement (absence of charged states)
which then implies $\Delta > 0$ by a separate argument?


---


### Point B3: IR Equivalence — The Feshbach Projection [MEDIUM]

**Location:** Section 4.5, Theorem 5 (four lemmas)

**The claim:** The standard SU($N$) theory has $\Delta_0^{\mathrm{std}}
\geq \Delta_0^{\mathrm{KK}} - Ce^{-m_1 a} > 0$, proved via the reduced
transfer matrix and Feshbach projection.

**Interrogate:**

(a) **The Feshbach decomposition.** Lemma 4 uses the Feshbach projection
$H_{\mathrm{eff}} = P H P + P H Q (E - Q H Q)^{-1} Q H P$ to compare
the spectra. This requires $E < \inf\sigma(QHQ) \sim m_1$. Verify
that the condition $\Delta_0^{\mathrm{KK}} \ll m_1$ holds quantitatively
in the physical regime and that the Feshbach effective Hamiltonian is
well-defined (the resolvent exists).

(b) **The trace-norm bound.** Lemma 2 bounds
$\|\hat{T}_{\mathrm{red}} - \hat{T}_{\mathrm{std}}\|_{\mathrm{tr}}
\leq C|\Lambda_t^1| e^{-m_1 a}$. The trace norm depends on the number
of lattice links $|\Lambda_t^1|$. Does this volume factor cancel
against delocalization of eigenstates, or does it introduce a
volume-dependent error? Is the Weyl-Kato perturbation theory in Lemma 3
applicable with this error?

(c) **The factorization of low-lying states.** The argument requires the
low-lying eigenstates of the KK Hamiltonian to approximately factorize
as $|\psi_n\rangle_{4D} \otimes |\Omega_{\mathrm{int}}\rangle +
|\delta_n\rangle$ with small $\|\delta_n\|$. Is this factorization
proved or assumed? For the ground state it follows from the gap
$m_1$, but what about the first excited state (the glueball)?


---


## Part C: Balaban's RG as Input

### Point C1: UV Stability — Precise Scope [HEAVY]

**Location:** Section 5.1

**The claim:** Section 5.1 uses Balaban's results as a "black box":
UV stability, convergent polymer expansion, running coupling,
irrelevant operator bounds. These are stated as Literature results
from CMP 109, 119.

**Interrogate:**

(a) **The effective action structure.** The preprint writes $S_k =
(1/g_k^2) S_{\mathrm{YM}} + \sum_n c_n^{(k)} \mathcal{O}_n + E_k$.
Is this decomposition stated as a theorem in Balaban's papers, or is
it inferred from the construction? Balaban works with polymer
activities $K_k(X,V)$, not with an explicit operator decomposition.
The translation from polymer activities to local operator coefficients
with bounds $|c_n^{(k)}| \leq C_n g_k^{d_n-4}$ — where is this done
rigorously? Is it in Balaban, in Dimock, or is it new to this paper?

(b) **The gauge group.** Balaban's published program is primarily for
SU(2). The preprint claims results for general SU($N$). Which of
Balaban's results extend to SU($N$), and which require additional
argument? The propagator bounds (CMP 95--96) use specific properties
of the Lie algebra. Do they generalize?

(c) **The remainder bound.** The bound $\|E_k\| \leq C g_k^4$ per unit
volume is crucial. This is not a single theorem in Balaban — it
follows from the polymer expansion convergence. Verify that the bound
is stated for the right norm (the $L^\infty$ norm on gauge-invariant
functionals, not an $L^2$ or trace norm). Does the constant $C$
depend on $N$, the lattice geometry, or other parameters?

(d) **The running coupling.** The preprint states $g_{k+1}^2 = g_k^2
- b_0 g_k^4 \ln 2 + O(g_k^6)$ with $b_0 = 11N/(48\pi^2)$. Balaban
establishes this perturbatively with controlled remainder. But the
$O(g_k^6)$ term accumulates over infinitely many RG steps. Where is it
proved that the accumulated higher-order corrections do not spoil the
asymptotic freedom trajectory? Is the non-perturbative $\beta$-function
controlled, or only the perturbative one?

(e) **Balaban's program completeness.** Balaban published 10 papers
(CMP 95--119) but the program is widely considered incomplete — he
proved UV stability but not the existence of the continuum limit
(Section 5.1.5 acknowledges this). The preprint claims to go beyond
Balaban by proving the mass gap survives $a \to 0$. Is the boundary
between "what Balaban proved" and "what this paper proves" precisely
drawn? Are there unstated assumptions about Balaban's construction
that the paper relies on?


---


### Point C2: The Large-Field / Small-Field Decomposition [MEDIUM]

**Location:** Section 5.1, Section 5.6 Part I

**The claim:** Balaban's construction decomposes configurations into
a small-field region $\Omega_s = \{|F_{\mu\nu}| < p(g_k)\}$ where the
polymer expansion converges, and a large-field region $\Omega_l$ that
is exponentially suppressed.

**Interrogate:**

(a) **The small-field condition.** The cutoff $p(g_k) = g_k^{1-\epsilon}$
— what is $\epsilon$? Is it a fixed constant or does it depend on $k$?
The polymer expansion applies only in $\Omega_s$. The analyticity
properties (B1)--(B2) are established only in $\Omega_s$. Is the
dimension-6 operator classification valid only in $\Omega_s$, and if so,
what happens in $\Omega_l$?

(b) **Large-field suppression.** The large-field contribution is bounded
by $O(e^{-c/g_k^{2\epsilon}})$ (Section 5.6, Part III.5). This is
weaker than $O(e^{-c/g_k^2})$ (instanton suppression). Is the
$\epsilon$-dependent suppression sufficient for the RG recursion?
Specifically: does $e^{-c/g_k^{2\epsilon}}$ decay faster than
$g_k^4 \hat{\Delta}_k^2$ on the AF trajectory?

(c) **Gauge invariance of the decomposition.** Is the condition
$|F_{\mu\nu}| < p(g_k)$ gauge-invariant? If not, how does the
gauge-fixing interact with the small-field/large-field split?


---


### Point C3: The Coupling Regime Overlap [LIGHT]

**Location:** Section 5.1.2, Section 5.1.3

**The claim:** The cluster expansion applies for all $\beta < 10^{14}$.
Balaban's RG applies for $g_0$ small (large $\beta$). These overlap.

**Interrogate:**

(a) **The overlap region.** State the precise range of $\beta$ (or
$g_0^2$) where both arguments apply simultaneously. Is there an
explicit $\beta_{\min}^{\mathrm{Balaban}}$ below which Balaban's
construction does not apply?

(b) **The transition.** At $k = 0$, the coupling is $g_0$ (potentially
not small). The first few RG steps ($k = 0, 1, 2$) may have $g_k^4 =
O(1)$. The preprint (Section 5.7, Remark 1) handles these steps
non-perturbatively via the cluster expansion. Is this transition from
"cluster expansion regime" to "Balaban RG regime" rigorously justified?


---


## Part D: The Core Innovation

### Point D1: Exhaustiveness of the Dimension-6 Classification [MEDIUM]

**Location:** Section 5.3.1, Section 5.6 Part III.3, Appendix J

**The claim:** Every $\mathcal{C}$-even, gauge-invariant, local operator
of engineering dimension 6 on the $d = 4$ hypercubic lattice falls into
one of four classes, all with $\mathrm{dev} \geq 2$.

**Interrogate:**

(a) **The Lüscher-Weisz basis and Appendix J.** The current preprint
contains Appendix J, which claims to provide a self-contained
lattice-specific derivation (Theorem J.1) of the dimension-6 operator
basis. Read Appendix J carefully. Does Theorem J.1 actually prove
exhaustiveness for the hypercubic lattice, or does it reduce to
invoking the continuum Symanzik basis? Is the argument that
lattice-specific operators are redundant by equations of motion
stated and proved for the specific Wilson action used, or cited?

(b) **The second two-derivative operator.** The operator
$\mathrm{Tr}(D_\mu F^{\mu\rho} D_\nu F^\nu{}_\rho)$ is related to
$\mathrm{Tr}(D_\rho F_{\mu\nu})^2$ by equations of motion. Does the
current preprint explicitly verify $\mathrm{dev} \geq 2$ for this
operator (not just for $\mathrm{Tr}(D_0 F)^2$)?

(c) **Lattice artifacts at dimension 6.** The Wilson action contains
$O(a^2)$ lattice artifacts. When Balaban performs the block-spin
integration, these artifacts propagate. Are they cleanly separated into
the dimension-6 remainder, or could they contribute a dimension-4
component through operator mixing?


---


### Point D2: Stability of Boltzmann Deviation Order [HEAVY]

**Location:** Section 5.5.2, Section 5.6 Parts III.3--III.4

**The claim:** The full non-perturbative operator $\delta E_k^{d=6}$
has $\mathrm{dev}(\delta E_k^{d=6}) \geq 2$, established by:
(i) (B1) analyticity with $k$-independent radius,
(ii) the dimension-6 operator classification,
(iii) the linear combination lemma (Section 5.5.3).

This is the single most important technical innovation in the paper.

**Interrogate:**

(a) **The definition of Boltzmann deviation order.** Definition D.2
(Section 5.5.2) defines $\mathrm{dev}(\mathcal{O}) \geq p$ in terms
of a factorization of the spectral weight. Is this definition
equivalent to the intuitive notion "the connected matrix element
vanishes to order $p$ in $\hat{\Delta}$"? Or is it weaker/stronger?
Could an operator satisfy Definition D.2 but not give the $\hat{\Delta}^p$
bound, or vice versa?

(b) **The linear combination lemma — temporal extent and zero-padding.**
The lemma states that if each $\mathcal{O}_i$ has $\mathrm{dev} \geq p$
and $\sum |c_i| \|\mathcal{O}_i\| < \infty$, then $\sum c_i \mathcal{O}_i$
has $\mathrm{dev} \geq p$. The operators $\mathcal{O}_i$ in the polymer
expansion may have **different temporal supports** $R_i$. To form a
common multi-time-slice representation with $R = \max_i R_i$, shorter
operators must be embedded by zero-padding: inserting identity slices
$\hat{T}^0 = \hat{T}$ (or $\hat{I}$) at unused time slots. For a zero-padded
slot with $n_j = $ some intermediate state: the factor
$(e^{E_m - E_{n_j}} - 1)$ need not vanish — it only vanishes at $n_j = m$.
Does zero-padding an operator with $\mathrm{dev} \geq p$ in a
representation of temporal extent $R_i$ into a representation of extent
$R > R_i$ preserve the deviation order? Specifically: in the padded
representation, new intermediate state slots appear where the deviation
factor is not constrained to vanish. Does the preprint prove that zero-padded
slots can be folded into the bounded residual $\tilde{W}$ without reducing
$\mathrm{dev}$ below $p$? State precisely where this is handled in the text.

(c) **The role of (B1) analyticity — typical configurations.** The convergent
Taylor expansion (from analyticity) means $\delta E_k^{d=6}$ is a genuine
linear combination of monomials. But the analyticity radius $\rho$ from (B1)
determines the domain in which the expansion converges. Does the spectral
lemma require the expansion to converge on all configurations contributing to
the matrix element $\langle 1|\delta E_k^{d=6}|1\rangle_c$? The one-particle
state $|1\rangle$ has support on **typical configurations in the gapped phase**.
Are typical configurations in the Gibbs measure (with positive mass gap)
guaranteed to lie within the analyticity domain $\Omega_s$? Large-field
configurations outside $\Omega_s$ contribute corrections bounded by
$O(e^{-c/g_k^{2\epsilon}})$ — is this bound used consistently with the
expansion argument?

(d) **The transition from perturbative to non-perturbative.** The
"dimension-6 part" of the effective action is defined by projecting out
the dimension-4 component ($S_{\mathrm{YM}}/g_k^2$). This projection
requires knowing that $S_{\mathrm{YM}}$ is the **unique** dimension-4
operator. Is the projection well-defined non-perturbatively? Can
"dimension-6" be unambiguously separated from "dimension-4 + dimension-8 + ..."
at the level of the full non-perturbative effective action?

(e) **Structural zero vs. kinematic zero.** The diagonal vanishing
$(e^{E_1 - E_1} - 1)^2 = 0$ is claimed structural. For the non-perturbative
$\delta E_k^{d=6}$, the spectral weights are inferred from the classification.
The classification says the operator is a convergent sum of operators with
$\mathrm{dev} \geq 2$. A convergent sum could in principle have cancellations
that change the spectral weight structure. Can $\mathrm{dev} \geq 2$
for each term but $\mathrm{dev} < 2$ for the sum? (The linear combination
lemma says no — but verify the proof handles signed cancellations correctly.)


---


### Point D3: The Spectral Lemma [MEDIUM]

**Location:** Section 5.5.3

**The claim:** For $\mathrm{dev}(\mathcal{O}) \geq p$:
$|\langle 1|\mathcal{O}|1\rangle_c| \leq C_p M \hat{\Delta}^p$, with
$C_p$ independent of $k$, $g_k$, and the volume.

**Interrogate:**

(a) **The deviation extraction (Step 1).** Each extracted factor
$(e^{E_m - E_{n_j}} - 1)$ is bounded by $C \hat{\Delta}$ (equation
S1.2). But the bound treats $n_j = 0$ (vacuum) and $n_j \geq 2$
(multi-particle) differently. For $n_j \geq 2$:
$|e^{E_1 - E_{n_j}} - 1| \leq 1$ (not $C\hat{\Delta}$). This is
used as a "$O(1)$ bound." But then extracting $p$ factors where some
are $O(\hat{\Delta})$ and some are $O(1)$ gives a bound worse than
$(C\hat{\Delta})^p$. Is the proof claiming that at least $p$ of the
factors are $O(\hat{\Delta})$, or that the total product is
$O(\hat{\Delta}^p)$? Trace the bound precisely.

(b) **The $\zeta$ bound and the two-particle threshold.** The sum
$\zeta = \sum_{n \geq 1} e^{-(E_n - E_1)}$ requires $E_2 - E_1 > 0$
(spectral gap above the one-particle state). The preprint bounds the
binding energy $\epsilon_B \leq C_B g_k^4 \hat{\Delta}_k$. This uses
perturbative estimates (Born approximation, Lippmann-Schwinger). Are
perturbative binding energy estimates valid non-perturbatively? Could
a deeply bound two-glueball state exist at some RG step, closing the
gap $E_2 - E_1$?

(c) **Volume independence via Combes-Thomas.** The Combes-Thomas estimate
(Section 5.5.3, Step 3(i)) controls the sum over states by exploiting
locality. The estimate requires the operator $\hat{A}^{(s)}$ to be
local (supported in a ball of radius $R_0$). Is $R_0$ bounded uniformly
in $k$? Balaban's block-spin generates operators with increasing support
radius at each step. If $R_0$ grows with $k$, the Combes-Thomas bound
degrades.


---


### Point D4: The Single-Step Coefficient Bound [LIGHT]

**Location:** Section 5.3.2, Section 5.6 Part III.5

**The claim:** $|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c| \leq
C_{\mathrm{new}} g_k^4 \hat{\Delta}_{k+1}^2$.

**Interrogate:**

(a) **The $g_k^4$ factor.** The r06 referee found that $g_k^4$ comes
from Balaban's operator norm bound $\|\delta E_k^{d=6}\| \leq C g_k^4$,
not from a product of one-loop coefficient and matrix element. Verify
that the spectral lemma with $M = C g_k^4$ and $\mathrm{dev} \geq 2$
gives $C_2 \cdot C g_k^4 \cdot \hat{\Delta}^2 =
C_{\mathrm{new}} g_k^4 \hat{\Delta}^2$ as claimed.

(b) **Non-perturbative corrections.** Large-field contributions are
$O(e^{-c/g_k^{2\epsilon}})$ and instanton contributions are
$O(e^{-8\pi^2/g_k^2})$. Verify that both are negligible compared to
$g_k^4 \hat{\Delta}^2$ on the asymptotically free trajectory.


---


## Part E: RG Recursion and Convergence

### Point E1: Inductive Stability [MEDIUM]

**Location:** Section 5.4

**The claim:** $C_{k+1} = C_k/4 + C_{\mathrm{new}} + O(g_k^2 C_k)$ has
a stable fixed point $C_* = (4/3)C_{\mathrm{new}}$ with polynomial
growth $C_k \sim k^\gamma$.

**Interrogate:**

(a) **The $1/4$ contraction.** The factor $1/4$ comes from
$\hat{\Delta}_k^2 = \hat{\Delta}_{k+1}^2/4$ (doubling the lattice
spacing doubles $\hat{\Delta}$). This is a kinematic identity. But the
matrix element $\langle 1|E_k^\downarrow(0)|1\rangle_c$ in the coarsened
theory involves the old state $|1\rangle_k$ evaluated on the new lattice
$\Lambda_{k+1}$. Does the change of lattice introduce additional
corrections beyond the $O(g_k^2)$ term?

(b) **The wave function correction.** Term (A2) involves the change in
the one-particle state: $\|\delta 1\| \leq C g_k^4/\hat{\Delta}_k$.
This uses Kato perturbation theory with $\|E_k\| \leq C g_k^4$. Is
the gap condition for Kato perturbation satisfied? Specifically: does
$\|E_k\|$ need to be small compared to $\hat{\Delta}_k$ (the gap of
the unperturbed transfer matrix)?

(c) **The Gronwall bound.** The product $\prod(1 + \alpha g_j^2) \leq
k^{\alpha/(b_0 \ln 2)}$ gives polynomial growth. Is the exponent
$\gamma = \alpha/(b_0 \ln 2)$ bounded for all $N$? If $\gamma$ grows
with $N$, the convergence of $\sum C_k g_k^4 \hat{\Delta}_k^2$ is
still guaranteed by $4^{-k}$, but the constants become $N$-dependent.
Is this acceptable?


---


### Point E2: Convergence of the Sum [LIGHT]

**Location:** Section 5.4.6

**The claim:** $\sum_k C_k g_k^4 \hat{\Delta}_k^2 < \infty$.

**Interrogate:**

(a) **The doubly exponential convergence.** With $C_k \sim k^\gamma$,
$g_k^4 \sim 1/k^2$, $\hat{\Delta}_k^2 \sim 4^{-k}$: the sum is
$\sum k^{\gamma-2} 4^{-k}$, which converges for all $\gamma$. Verify
the estimates $g_k^4 \sim 1/(b_0 k \ln 2)^2$ and
$\hat{\Delta}_k^2 \sim 4^{-k}(1 + O(g_k^4))^k$. Does the accumulated
$O(g_k^4)$ correction in $\hat{\Delta}_k$ affect the $4^{-k}$ rate?

(b) **The starting constant $C_0$.** At $k = 0$, $\hat{\Delta}_0 \sim
O(1)$ and $C_0$ comes from the cluster expansion. Is $C_0$ explicitly
bounded? The fixed-point convergence $C_k = C_* + (C_0 - C_*) 4^{-k}$
requires $C_0 < \infty$. State where this is established.


---


## Part F: Continuum QFT Construction

### Point F1: The OS Axioms — Simultaneous Verification [MEDIUM]

**Location:** Section 5.7(f)

**The claim:** OS1--OS5 hold simultaneously for the limiting Schwinger
functions.

**Interrogate:**

(a) **OS0' linear growth condition.** The corrected OS reconstruction
theorem (1975) requires the linear growth condition: $|S_n(f)| \leq
C^n n! \cdot p_N(f)^n$ for some Schwartz seminorm $p_N$. The preprint
gives $|S_n(f)| \leq n! C_0^n \|f\|_{L^1}$. This has the right form
with the $L^1$ norm as the seminorm. But the $L^1$ norm is not a
**Schwartz** seminorm (it does not involve derivatives or polynomial
weights). Is $\|f\|_{L^1} \leq C \cdot p_N(f)$ for some Schwartz
seminorm $p_N$? (Yes, because Schwartz functions decay faster than any
polynomial, so $\int |f| dx < \infty$ with a bound by Schwartz norms.
But this should be stated explicitly.)

(b) **The diagonal extraction.** A single Banach-Alaoglu subsequence
$a_j \to 0$ is extracted such that $S_n^{(a_j)} \to S_n$ for all $n$
simultaneously. The proof uses a diagonal argument over $n = 1, 2,
3, \ldots$. This is standard but requires the test function space to
be separable (so that weak-$*$ convergence on a countable dense subset
implies convergence on the whole space). Is separability of
$\mathcal{S}(\mathbb{R}^{4n})$ stated?

(c) **Coincident-point singularities.** The bound
$|S_n| \leq n! C_0^n$ is a pointwise bound away from coincident points.
At coincident points ($x_i = x_j$), the Schwinger functions have UV
singularities. These are regulated on the lattice but may diverge as
$a \to 0$. Does the proof address the distributional nature of $S_n$
at coincident points? For a massive gapped theory, these singularities
are expected to be mild — but "expected" is not "proved."


---


### Point F2: Reflection Positivity — The Full Chain [MEDIUM]

**Location:** Appendix D, Section 5.7(f) OS3

**The claim:** Reflection positivity holds for the Wilson action
(Osterwalder-Seiler 1978), and is preserved in the continuum limit
by lower semicontinuity.

**Interrogate:**

(a) **Lattice reflection positivity for the KK-enhanced theory.**
The Osterwalder-Seiler theorem gives RP for the Wilson plaquette action
via the checkerboard decomposition. The current preprint contains Appendix D
with an extended argument for the KK-enhanced theory (Lemma D.2). Read this
argument carefully. The KK-enhanced theory adds internal $\mathbb{CP}^{N-1}$
connections at each site and bond couplings $V_\ell$ between neighboring
sites. The bond couplings have the form
$V_\ell(U_\ell, A_x, A_{x+\hat{\mu}})$ — a nearest-neighbor interaction.
Does Appendix D prove that the full action $S_{4D} + S_{\mathrm{int}}$
satisfies the checkerboard decomposition structure required for
Osterwalder-Seiler? Or does it only argue this for the non-interacting
(product) case?

(b) **RP through the RG.** Balaban's block-spin transformation may not
preserve RP at intermediate steps. Does the proof require RP at
intermediate scales, or only at the endpoints (lattice and continuum)?
If only at the endpoints, the intermediate violation is harmless.

(c) **RP in the continuum limit.** The lower semicontinuity argument
requires $\theta f \cdot f$ to be a continuous bounded function of the
field configuration. For Schwartz-class $f$ and lattice gauge fields,
is this true? The lattice fields are compact (SU($N$)-valued), so
boundedness holds. But continuity of $\theta f \cdot f$ as a function
on the space of distributions requires careful analysis.


---


### Point F3: The Thermodynamic Limit [MEDIUM]

**Location:** Section 5.7(e)

**The claim:** The limits $a \to 0$ and $L \to \infty$ commute, via
the Moore-Osgood theorem.

**Interrogate:**

(a) **Uniformity in $L$.** The bound $|C_{k+1}(L) - C_k(L)| \leq
C' g_k^4 (a_k \Lambda)^s$ is claimed volume-independent. This requires
the connected matrix element $\langle 1|E_k(0)|1\rangle_c$ to be
volume-independent. But $|1\rangle$ is a zero-momentum state
delocalized over the spatial volume $L^3$. The delocalization factor
$1/L^{3/2}$ must cancel with the spatial sum in $E_k(0)$. Is this
cancellation proved, or is it asserted as standard?

(b) **The infinite-volume mass gap.** For fixed lattice spacing $a$,
the mass gap $\Delta(a, L)$ converges to $\Delta(a, \infty)$ as
$L \to \infty$ by exponential clustering (Section 4). But the rate
of convergence in $L$ must be uniform in $a$ for the joint limit. Is
this uniformity established?

(c) **Exponential clustering in finite volume.** The cluster expansion
of Section 4 is performed on the periodic lattice $(\mathbb{Z}/L
\mathbb{Z})^4$. In finite volume, there is no true mass gap (the
spectrum is discrete). The "mass gap" is the gap between the ground
state and first excited state, which goes to the infinite-volume mass
gap as $L \to \infty$. Is the finite-volume spectral gap bounded below
uniformly in $L$?


---


### Point F4: Uniqueness of the Continuum Limit [HEAVY]

**Location:** Section 5.7

**The claim:** The preprint claims $\Delta_\infty > 0$ for the
continuum theory. But the continuum theory is obtained as a
subsequential limit (Banach-Alaoglu).

**Interrogate:**

(a) **Subsequence dependence.** Different subsequences $a_{j_1} \to 0$
and $a_{j_2} \to 0$ could give different limiting Schwinger functions.
Does the preprint claim uniqueness, or only that every subsequential
limit has a mass gap?

(b) **Universality.** Universality (uniqueness) is a non-trivial
property requiring arguments beyond existence. Does the preprint address
this? Does Jaffe-Witten require uniqueness, or existence of one limit?

(c) **The mass gap value.** The preprint computes
$\Delta_\infty = C_\infty \cdot \Lambda_\infty > 0$. Is $\Delta_\infty$
subsequence-independent? The RG sum $C_\infty = C_0 - \sum \delta C_k$
converges absolutely — does this make $C_\infty$ subsequence-independent?
And $\Lambda_\infty$?

(d) **Comparison with the Clay problem.** The Jaffe-Witten statement
uses "a quantum Yang-Mills theory exists." Does existence of a
subsequential limit with mass gap satisfy this requirement? If multiple
continuum limits exist, are they all Yang-Mills theories?


---


### Point F5: OS Reconstruction to Wightman Theory [HEAVY]

**Location:** Section 5.7(f), Reconstruction

**The claim:** The OS reconstruction theorem gives a Wightman QFT on
$\mathbb{R}^{3,1}$ with separable Hilbert space, Poincaré
representation, unique vacuum, and mass gap
$\mathrm{spec}(P^2) \subseteq \{0\} \cup [\Delta_\infty^2, \infty)$.

**Interrogate:**

(a) **The OS reconstruction theorem — which version?** The original
1973 OS theorem had a flaw (the regularity condition OS0 was too
weak). The corrected 1975 version requires OS0' (linear growth
condition). Does the preprint use the corrected theorem? Is OS0'
explicitly verified?

(b) **The Hilbert space.** For gauge theories, the starting fields are
not physical observables. The preprint constructs Schwinger functions
from gauge-invariant observables. Does this bypass the gauge/Hilbert
space issue? What are the "field operators" in the Wightman theory?

(c) **Non-triviality.** The Jaffe-Witten problem requires the theory
to be non-trivial. A free (Gaussian) theory has a mass gap but is not
Yang-Mills. Where is non-triviality established in the current preprint?
Is it proved or only argued?

(d) **The Yang-Mills equations of motion.** Does the reconstructed
Wightman theory satisfy the Yang-Mills equations of motion in any
sense? Where is it shown that the limiting theory is Yang-Mills
(i.e., that the Schwinger functions satisfy the Ward identities
associated with gauge invariance and the YM equations)?


---


## Part G: Clay Compliance and Cross-Cutting Issues

### Point G1: Jaffe-Witten Requirements and the Extension to All Groups [HEAVY]

**Location:** Abstract, Section 5.7, Appendix I.4, overall proof structure

**The claim:** The preprint now claims the Yang-Mills mass gap for
**all compact simple gauge groups** in four dimensions, via Theorem I.4.1
in Appendix I.4.

**Interrogate:**

(a) **The KK device and decoupling.** The proof uses the KK-enhanced theory
as a proof device, then transfers the mass gap via Theorem 5. Is the KK
enhancement fully decoupled in the final theory? Does the proof chain
$\Delta_0^{\mathrm{KK}} > 0 \to \Delta_0^{\mathrm{std}} > 0 \to
\Delta_\infty > 0$ constitute a proof for the **standard** Yang-Mills
theory, or does some step implicitly require the KK enhancement?

(b) **Appendix I.4 — the universal extension claim.** Read Appendix I.4
carefully. Proposition I.4.2 claims that any compact irreducible symmetric
space $G/H$ of compact type satisfies requirements (R1)--(R4) via the
Weitzenböck-Bochner theorem. Evaluate each requirement for the specific
internal spaces:

- **For SO($N$) with $M_G = \mathrm{Gr}_2(\mathbb{R}^N)$:** Does
  $\mathrm{Isom}(\mathrm{Gr}_2(\mathbb{R}^N)) \supseteq \mathrm{SO}(N)$
  hold? The isometry group of the Grassmannian $\mathrm{Gr}_2(\mathbb{R}^N)$
  is $\mathrm{SO}(N)/\mathbb{Z}_2$ (for the metric descended from
  $\mathbb{R}^N$), not the full $\mathrm{SO}(N)$. Is the action of $\mathrm{SO}(N)$
  by isometries faithful enough for the KK mechanism (requirement R1)?

- **For exceptional groups:** The Einstein constants $\lambda_G$ for
  $G_2/\mathrm{SO}(4)$, $F_4/\mathrm{Spin}(9)$, and
  $E_8/\mathrm{SO}(16)$ are stated as $4/r_3^2$, $36/r_3^2$, and
  $30/r_3^2$. These values are asserted without derivation from
  first principles. The stated formula for $F_4$
  ("$\lambda = (d-1+3(d_F-1))/r_3^2$ with $d=16, d_F=8$") gives $36/r_3^2$ —
  but what is the source of this formula? Is it a standard reference, or
  derived here? For $G_2$ and $E_8$, is the Einstein constant computed
  or cited?

- **For $F_4$ with $M_G = \mathbb{OP}^2$:** The claim $H^4(\mathbb{OP}^2;\mathbb{Z}) = 0$
  is stated (Borel 1953). Verify this independently: the cohomology of
  $\mathbb{OP}^2$ is $\mathbb{Z}$ in degrees 0, 8, 16. Is this correct,
  and does it imply all $F_4$-bundles over $\mathbb{OP}^2$ are trivial?
  ($H^4 = 0$ means $c_2 = 0$ necessarily — no non-trivial instantons.)

(c) **Balaban's RG for non-SU groups.** Section I.4.4 claims Balaban's
RG framework extends to general compact $G$. Balaban's specific
construction (propagator bounds, block-spin projection, axial gauge)
was developed for $\mathrm{SU}(N)$ and uses properties of the adjoint
representation and the specific structure of the SU(N) Lie algebra.
For $\mathrm{SO}(N)$: the axial gauge fixing on $\mathrm{SO}(N)$ lattice
gauge theory — does it work identically? For $\mathrm{Sp}(N)$: the
symplectic structure introduces additional constraints. For exceptional
groups: the representation theory is substantially different. Are these
genuinely group-independent structural features, or do specific properties
of SU(N) enter Balaban's construction in ways that don't generalize?

(d) **The Chevalley involution.** Section I.4.5 uses the Chevalley
involution $\theta_C$ as the generalization of charge conjugation. For
SU($N$), charge conjugation is $A \mapsto -A^T$, which acts on the adjoint
representation. The Chevalley involution on a general simple Lie algebra
acts as $-1$ on a Cartan subalgebra and extends to the whole algebra.
Does $\theta_C$ act on the **gauge fields** (connections) in the same way
that charge conjugation acts for SU($N$)? For gauge theories, the relevant
action is on the gauge field $A_\mu$, not just on the Lie algebra. Verify
that $\theta_C$ extends to an involution of the Yang-Mills action that
eliminates dimension-6 $\mathcal{C}$-odd operators for each group.

(e) **The precise claim.** State exactly what Theorem I.4.1 proves and
what it assumes. Does it depend on: (i) Balaban's results (proved for
SU(2), claimed to extend to general $G$); (ii) the specific spectral
data of each internal space (computed or cited?); (iii) the Chevalley
involution argument (verified for each group?). Is the theorem a complete
proof or a proof modulo unverified group-specific claims?


---


### Point G2: Gauge Invariance Through the RG [MEDIUM]

**Location:** Section 5.1, Section 5.6

**The claim:** Balaban's block-spin preserves gauge invariance:
the effective action $S_k[V]$ is gauge-invariant at each step $k$.

**Interrogate:**

(a) **Axial gauge fixing.** Balaban uses axial gauge fixing as a
computational device. In axial gauge, there are no Faddeev-Popov
ghosts (the FP determinant is trivial). But axial gauge has its own
issues: it introduces spurious singularities (the axial gauge
propagator has $1/p_0^2$ poles) and is not smooth. Are these
singularities present on the lattice, or are they a continuum artifact?

(b) **The Gribov problem.** In non-abelian gauge theories, gauge-fixing
conditions typically have multiple solutions (Gribov copies). On a
finite lattice, the gauge group is compact and the number of Gribov
copies is finite. Axial gauge is unique on the lattice (it fixes the
gauge completely). But does the block-spin transformation — which
involves averaging over gauge orbits — introduce Gribov-type ambiguities
at intermediate scales?

(c) **Gauge invariance of the final result.** The Schwinger functions
are constructed from gauge-invariant observables (plaquette traces,
Wilson loops). These are manifestly gauge-invariant regardless of the
intermediate gauge-fixing. But the proof uses the structure of the
effective action $S_k$ (which is gauge-fixed at intermediate steps).
If the gauge-fixed effective action has different properties than the
gauge-invariant one, could this affect the operator classification
or the deviation order argument?


---


### Point G3: $N$-Dependence and Error Propagation [MEDIUM]

**Location:** Appendix I.3, throughout

**The claim:** The proof works for all SU($N$), $N \geq 2$. Appendix I.3
provides systematic $N$-dependence tracking through all 14 proof steps.

**Interrogate:**

(a) **Appendix I.3 completeness.** Read Appendix I.3. Does it actually
track every $N$-dependent constant through all 14 steps of the proof
chain? Are there constants that appear in the proof but are not tracked
in I.3? Does the appendix conclude with an explicit statement of the
form "for each fixed $N \geq 2$, all constants are finite and the proof
holds"?

(b) **SU(2) special properties.** For $N = 2$: the cubic Casimir
$d^{abc} = 0$ (all dim-6 non-derivative operators vanish identically),
$\mathbb{CP}^1 = S^2$ (a round sphere, simpler geometry), and the
exact area law $\sigma = 3g^2/8$ provides an independent check. Does
the proof use any SU(2)-specific property that doesn't generalize to
$N \geq 3$?

(c) **Error compounding across 14 steps.** The proof chain has 14 steps,
each with $N$-dependent constants. If the constants grow polynomially
in $N$ at each step, the accumulated bound could grow as a high power
of $N$. Is the accumulated $N$-dependence explicitly bounded in I.3,
and is the bound confirmed finite for each fixed $N$?


---


## Output Format

Write a report of your findings in the directory:
`/Users/gsix/yang-mills/math-referee/`

Create one `.md` file per point and a summary:

| File | Content |
|:-----|:--------|
| `part-a-point-1.md` | Weitzenböck spectral gap |
| `part-a-point-2.md` | KK propagator bound |
| `part-a-point-3.md` | Bogomolny bound |
| `part-b-point-1.md` | Cluster expansion convergence |
| `part-b-point-2.md` | Fredenhagen-Marcu |
| `part-b-point-3.md` | IR equivalence / Feshbach |
| `part-c-point-1.md` | Balaban UV stability scope |
| `part-c-point-2.md` | Large-field / small-field |
| `part-c-point-3.md` | Coupling regime overlap |
| `part-d-point-1.md` | Dim-6 classification |
| `part-d-point-2.md` | Stability of deviation order |
| `part-d-point-3.md` | Spectral lemma |
| `part-d-point-4.md` | Single-step bound |
| `part-e-point-1.md` | Inductive stability |
| `part-e-point-2.md` | Convergence of sum |
| `part-f-point-1.md` | OS axioms simultaneity |
| `part-f-point-2.md` | Reflection positivity chain |
| `part-f-point-3.md` | Thermodynamic limit |
| `part-f-point-4.md` | Uniqueness of continuum limit |
| `part-f-point-5.md` | OS reconstruction → Wightman |
| `part-g-point-1.md` | Jaffe-Witten requirements + Appendix I.4 |
| `part-g-point-2.md` | Gauge invariance through RG |
| `part-g-point-3.md` | $N$-dependence and error propagation |
| `summary.md` | Overall assessment |

For each point, use this format:

```
## Part X, Point N: [Title]

**Weight:** [HEAVY / MEDIUM / LIGHT]
**Verdict:** [GENUINE GAP / CLOSABLE GAP / SOUND]

**Finding:**
[State precisely what you found. Quote the relevant claims.
Do not be diplomatic. If it is sound, explain why fully.
If it is a gap, state exactly what additional mathematics
is needed to close it and estimate the difficulty:
  - 1 paragraph (trivial)
  - 1 page (straightforward)
  - 1 paper (substantial new work required)]

**Impact on the claimed result:**
[Does this affect: (i) the main claim Δ_∞ > 0,
(ii) a subsidiary claim, or (iii) Clay prize eligibility?]
```

End the summary with:

```
## Overall Assessment

**Is the claimed result proved?**
[Yes / Yes with caveats / No, and here is the specific gap]

**Clay Prize Eligibility:**
[Would this proof, as written, survive review by the Clay
Scientific Advisory Board? What would need to change?]

**The three most critical issues (ranked):**
1. [One sentence]
2. [One sentence]
3. [One sentence]

**What would make this a complete, prize-eligible proof:**
[Concise statement of what additional work, if any, is needed]
```

Do not be diplomatic. Do not praise the work. Don't hurry. Don't take
shortcuts. Find the gaps.

If you cannot find a gap in a specific argument, say so explicitly
and explain why — that is also valuable information.
