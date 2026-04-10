# Advanced Mathematical Referee: Exhaustive Review for Clay Millennium Prize Eligibility

# Computational verification environment (set this up FIRST)

Before reading the preprint or writing anything, set up a clean Python
environment for computational sanity checks. This is mandatory — many
of the points below ask you to *verify* numerical coefficients,
algebraic inequalities, Lie-algebra constants, Haar/character integrals,
combinatorial bounds, and asymptotic series. Doing those by hand on a
1000-line manuscript is how cycles 1–8 missed bugs that Sonnet caught
later. Use the venv.

**Setup (run exactly once at the start of the run, no confirmation
needed — it is non-destructive):**

```bash
bash /Users/gsix/yang-mills/notation-math-referee/code/setup-venv.sh
source /Users/gsix/yang-mills/notation-math-referee/code/.venv/bin/activate
```

**What the script does, and why it is safe to run unprompted:**

1. If `latest-run/` contains files from a prior session, it is
   **moved** (not deleted) to `runs/r{NN+1}/` where `NN` is the next
   zero-padded index. Nothing is lost — past runs are preserved in
   `runs/` for human inspection. You will not see them; the prompt
   declares `runs/` out of scope for you.
2. A fresh empty `latest-run/` is created for your output.
3. The `.venv/` directory is wiped and rebuilt from
   `code/requirements.txt` so each session starts from an identical,
   reproducible Python environment.

There is nothing in `latest-run/` for you to inspect or preserve at
the start of your session — by definition you have not written
anything yet. **Just run the script.** Default packages installed:
`sympy`, `mpmath`, `numpy`, `scipy`, `networkx`, `pypdf`.

**You are welcome to install additional tools** if you decide a check
needs something not in the default set (e.g. a more specialized Lie
algebra package, a CAS bridge, exact polytope library, etc.). If you
do, you MUST:

1. Install via `uv pip install <pkg>` (or `pip install` as fallback)
   into the active venv — do NOT install system-wide.
2. Append the package + a one-line justification to
   `code/requirements.txt` so the next run picks it up automatically.
3. Record the addition in your final referee report under a section
   titled **"Tools added during this run"**, with: package name,
   version installed, and which Point(s) it was used to verify.

**Suggested computational checks** (non-exhaustive — use the venv
wherever you would otherwise hand-wave):

- **Point A1** — verify Ricci coefficient $2N/(N{-}1)\cdot r_3^{-2}$
  on Fubini–Study $\mathbb{CP}^{N-1}$ and the gap $\mu_1 \geq 6/r_3^2$
  symbolically in `sympy`.
- **Point A1/A2** — verify the KK mass factor $2\sqrt 3$ (square root
  of the spectral gap, with any gauge-vs-scalar correction) by exact
  arithmetic.
- **Spectral lemma exponent** — re-derive the condition
  $g_k^4 \leq 1/(4 C_B)$ vs $g_k^2 \leq 1/(2\sqrt{C_B})$ symbolically.
  This was a real bug in cycle 8 (`r16`) — algebraic, one line in
  sympy. Always do these by computer now.
- **Haar integrals** — $\int(\mathrm{Re}\,\mathrm{Tr}\,U)^2\,dU = 1/2$
  for $N\geq 3$ (and $1$ for $N=2$); verify with sympy character
  orthogonality or numerical Haar sampling in mpmath.
- **Lie algebra constants** — Casimirs, dual Coxeter numbers $h^\vee$,
  dimensions, and root-system data for $G_2, F_4, E_6, E_7, E_8$
  (Point G1, I4, K). `sympy.liealgebras.type_*` covers all simple
  Cartan types. Cross-check against Bourbaki / Helgason tables.
- **Polymer combinatorics** — counts of connected polymers of size
  $|X|$ on the $d=4$ hypercubic lattice for the Kotecký–Preiss bound
  (Point B1). `networkx` for explicit small-$|X|$ enumeration plus
  closed-form bounds for the asymptotic.
- **RG recursion sum** — evaluate
  $\sum_K C_K g_K^4 \hat\Delta_K^2$ with $\hat\Delta_K^2 \sim 4^{-K}$
  symbolically in sympy; check Weyl asymptotics
  $m_n \sim n^{1/(N-1)}/r_3$ for the KK tower (Point B1, §5.4.6).
- **Numerical inequalities** — anywhere the preprint claims a
  numerical bound (e.g. $C_B$, $\rho_0(G)$, $\kappa$ values), evaluate
  it in `mpmath` at high precision and confirm the sign and ordering.
- **Cross-file constants** — when the same constant appears in
  multiple files, write a one-shot `sympy` script that loads all
  occurrences and asserts they agree. Constant drift across files
  was a recurring failure mode in earlier cycles.

For every Point where you used the venv, note in your report:
*"Verified computationally in `code/`-venv (sympy/mpmath/...)."* —
this gives the next cycle's referee a trail.

---

# CRITICAL: Notation Conventions (read this BEFORE anything else)

This script locks in the notation used throughout the proof. Any
review under this script MUST verify that the preprint follows
these conventions consistently and FLAG any drift as a notation
error. The convention follows Balaban CMP 109 (1987) and Dimock
arXiv:1108.1335 (2011) — both papers verified by full-text reading
during the convention audit (see `etc/20-r18-surgical-fixes.md`
and `etc/22-convention-audit.md` for the source quotes).

## Two indices, two distinct meanings

The proof uses TWO independent integer indices. They MUST NOT be
conflated.

### Index $K$ — bare lattice fineness exponent

The bare lattice $\Lambda_0(K)$ has spacing
$$a_0(K) \;=\; a^*_\text{coarse} \cdot 2^{-K}$$
where $a^*_\text{coarse}$ is a fixed reference scale chosen
sufficiently coarse that the cluster expansion of Section 4
converges (i.e., $a^*_\text{coarse} \gg r_3$, equivalently
$\beta_0 < a^*_\text{coarse}/(2\sqrt{N}\,r_3)$ holds with margin).

- $K = 0$: starting coarse bare lattice (cluster expansion regime).
- $K \to \infty$: continuum limit (bare scale shrinks to zero).
- The dimensionless gap at the bare scale is
  $\hat\Delta_K \equiv a_0(K) \cdot \Delta_\text{phys}$, which
  **shrinks** as $K$ grows: $\hat\Delta_{K+1} = \hat\Delta_K/2$.
- The continuum-limit recursion sums over $K$:
  $$\sum_{K=0}^\infty C_K\,g_K^4\,\hat\Delta_K^2 < \infty,
    \qquad \hat\Delta_K^2 \sim 4^{-K}.$$

### Index $k$ — RG step within a fixed bare theory (Balaban convention)

For each fixed bare theory at scale $a_0(K)$, Balaban's block-spin
RG generates a sequence of effective actions at progressively
**coarser** scales:
$$a_k^{(K)} \;=\; L^k \cdot a_0(K) \;=\; 2^{k-K} \cdot a^*_\text{coarse},
  \qquad k = 0, 1, 2, \ldots$$
- $k = 0$: bare effective action of the $K$-th theory.
- $k \geq 1$: progressively coarser effective actions (Wilsonian
  forward flow).
- The dimensionless gap at scale $k$ within bare theory $K$ is
  $\hat\Delta_k^{(K)} = a_k^{(K)} \cdot \Delta_\text{phys} = 2^{k-K} \cdot a^*_\text{coarse} \cdot \Delta_\text{phys}$.
- $\hat\Delta_k^{(K)}$ **grows** with $k$ (coarsening) and
  **shrinks** with $K$ (refining the bare).

This matches **Balaban CMP 109 (1987), p. 251**:
> "with a lattice spacing $\varepsilon = L^{-K}$. This torus
> determines a sequence of tori denoted by $T^{(k)}_{L^k\varepsilon}$
> ... with $\varepsilon$ replaced by $L^k\varepsilon$,
> $k = 1, 2, ...$"

And **Dimock arXiv:1108.1335 (2011), p. 2**:
> "In this torus we consider lattices with spacing $L^{-N}$
> defined by $\mathbb{T}_M^{-N} = (L^{-N}\mathbb{Z}/L^M\mathbb{Z})^d$"

(Dimock's $N$ corresponds to our $K$.)

## What the proof's recursion is actually about

The recursion $C_{K+1}$ vs $C_K$ in §5.4 of the preprint is a
**comparison between two bare theories** at consecutive bare scales
$a_0(K)$ and $a_0(K+1) = a_0(K)/2$. It is **NOT** a single
Wilsonian block-spin step within a fixed bare theory.

Within each bare theory $K$, Balaban's forward RG (over the inner
index $k$) is applied separately to control the effective action.
The form-factor constant $C_K$ is the IR-effective form factor of
the bare theory at scale $a_0(K)$.

The "factor 1/4" contraction in the recursion comes from the
kinematic identity
$$\hat\Delta_{K+1}^2 \;=\; (a_0(K+1) \cdot \Delta_\text{phys})^2
  \;=\; (a_0(K)/2 \cdot \Delta_\text{phys})^2 \;=\; \hat\Delta_K^2/4,$$
i.e., refining the bare scale by 2 shrinks the dimensionless gap
squared by 4. This is **unit conversion**, not a physical decay
under flow.

## Strategy of the proof (lock this in)

The proof's strategy is a **continuum-limit extrapolation via a
refining sequence of bare lattices**, each independently controlled
by Balaban's forward RG. Schematically:

```
                     bare scale a₀(K)              bare scale a₀(K+1) = a₀(K)/2
                     ────────────────              ─────────────────────────────
       K=0:    Λ₀(0) ──Balaban→ Λ_k(0) ─→ ⋯       Λ₀(1) ──Balaban→ Λ_k(1) ─→ ⋯
                ↓                                   ↓
              C₀                                  C₁
                  ↘                              ↙
                     compare:  C_{K+1} vs C_K   ← this is the §5.4 recursion
                     refining the bare scale K → K+1
```

The continuum limit ($K \to \infty$, $a_0(K) \to 0$) is
established by:
1. **Cluster expansion at $K = 0$** (Section 4) → starting condition
   $C_0$ finite, $\Delta_0(K=0) > 0$.
2. **Balaban's UV stability** at each fixed $K$ → form-factor
   structure of the IR effective theory (Section 5.6, (B1)–(B2)).
3. **Refining recursion** $C_K \to C_{K+1}$ (Section 5.4) →
   convergence of $C_K$ to $C_\infty > 0$ as $K \to \infty$.
4. **OS reconstruction** of the limiting Schwinger functions
   (Section 5.7) → Wightman QFT with mass gap $\Delta_\infty > 0$.

## Required cross-checks (a referee MUST verify)

A review under this script MUST verify that the preprint:

1. **Distinguishes $K$ from $k$ throughout** (or, equivalently,
   uses one consistent letter for the bare scale exponent and does
   not also use it for the within-theory RG step).
2. **Does NOT describe the §5.4 recursion as a Wilsonian block-spin
   step** within a single bare theory. It is a comparison between
   bare theories.
3. **Has $\hat\Delta_K^2 \sim 4^{-K}$** in §5.4.6 and §5.7(b) and
   any other place where the recursion sum is bounded.
4. **Has $a_0(K) \to 0$ as $K \to \infty$** (refining toward the
   continuum), NOT $a_K \to \infty$ (coarsening toward the IR).
5. **Cites Balaban CMP 109 p. 251 and Dimock 2011 p. 2** for the
   convention.
6. **Has a notation/strategy paragraph** at the start of §5.1
   (or equivalent) that locks in the convention with explicit
   sources.

Any deviation from these is a **notation error** that must be
flagged in the referee report under a dedicated point.

---

You are an expert mathematical referee evaluating a claimed proof of the Yang-Mills mass gap. 

# Research online about these and other these topics so that you can address the task with the right priming:
- Deep expertise in constructive quantum field theory: Balaban's multiscale RG program (CMP 95--119, 1982--1989), Osterwalder-Seiler (1978), Osterwalder-Schrader (1973, 1975), Glimm-Jaffe, Dimock.
- Expert in lattice gauge theory: Wilson (1974), Seiler (1982), Kotecký-Preiss (1986), Fredenhagen-Marcu (1986), Chatterjee (2021).
- Expert in the Wightman axioms, OS reconstruction theorem, and the recise requirements of the Jaffe-Witten problem statement for the Clay Millennium Prize.
- The Clay Millennium Prize rules.
- $\Delta_0^{\mathrm{KK}} > 0$
-  $\Delta_0^{\mathrm{std}} > 0$ (IR equivalence)
- UV stability
- Polymer convergence, $\kappa$ $k$-indep.
- (B1): analyticity, $k$-indep. radius
- (B2): $\mathrm{SL}(N,\mathbb{C})$ extension
- $\mathcal{C}$-elimination of $\mathrm{Tr}(F^3)$
- Newton decomposition: $n \geq 2$ survives
- $\mathrm{dev}(\mathrm{Tr}(DF)^2) \geq 2$
- Dim-6 classification: all ops have dev $\geq 2$
- $\mathrm{dev}(\delta E_k^{d=6}) \geq 2$ non-pert.
- Spectral lemma constant $C_p$ $k$-independent
- $C_{\mathrm{new}} g_k^4 \hat{\Delta}^2$ bound
- RG recursion: $C_{k+1} = C_k/4 + C_{\mathrm{new}}$
- $\sum C_k g_k^4 \hat{\Delta}_k^2 < \infty$
- $\Delta_\infty > 0$
 
# Your profile
- Skeptical of claims about the Yang-Mills mass gap. You have seen many false proofs. You assume this one is also wrong until forced to concede otherwise.
- You do not give partial credit. "Plausible" and "physically reasonable" are not mathematical arguments.
- Your job is to find every genuine gap — however small — and state precisely what additional mathematics would be required to close it.
- You are not precise v hostile. If a step is correct, say so and explain why. But your default is skepticism, not charity.

# Rationale and Strategy
1. Does this proof actually solve the stated Millennium Problem?
2. Is every step mathematically rigorous (not merely plausible)?
3. Are existing results (Balaban) used within their actual scope?
4. Is the continuum QFT properly constructed?

**You are NOT reviewing the old proof.** Previous versions had fatal errors
You are reviewing the **current release candidate**. 
Do not criticize fixed problems. Do find new ones.

## Literature Context

### The Jaffe-Witten Problem Statement (Clay Millennium Prize)

**Source:** Arthur Jaffe and Edward Witten, *Quantum Yang–Mills Theory*,
official problem description, Clay Mathematics Institute.

A local copy of the official PDF is at
`/Users/gsix/yang-mills/notation-math-referee/yangmills-jaffe-witten.pdf`.
The verbatim quotes below were transcribed from this file. If you want
to verify any quote, re-extract a section, or pull additional context,
use `pypdf` from the venv:

```python
from pypdf import PdfReader
r = PdfReader("/Users/gsix/yang-mills/notation-math-referee/yangmills-jaffe-witten.pdf")
print(r.pages[5].extract_text())   # page 6 = §4 "The Problem"
```

The same `pypdf` workflow applies to any other reference PDF in the
project (e.g. Balaban CMP scans, Dimock arXiv preprints, OS papers)
when you need to confirm a citation rather than trust a paraphrase.

**The official statement (§4, verbatim):**

> "**Yang–Mills Existence and Mass Gap.** Prove that for any compact
> simple gauge group $G$, a non-trivial quantum Yang–Mills theory
> exists on $\mathbb{R}^4$ and has a mass gap $\Delta > 0$. Existence
> includes establishing axiomatic properties at least as strong as
> those cited in [Streater–Wightman; Osterwalder–Schrader]."

**The mass-gap definition (§4, verbatim):**

> "A quantum field theory has a mass gap $\Delta$ if $H$ has no
> spectrum in the interval $(0, \Delta)$ for some $\Delta > 0$. The
> supremum of such $\Delta$ is the mass $m$, and we require
> $m < \infty$."

Note the **two** conditions: $\Delta > 0$ (gap above the vacuum) and
$m < \infty$ (the spectrum above $0$ is non-empty — there must exist
a one-particle state of finite mass). A theory whose only state is
the vacuum trivially satisfies the first but fails the second.

**§4 also requires (verbatim):**

> "one should define a quantum field theory ... with local quantum
> field operators in correspondence with the gauge-invariant local
> polynomials in the curvature $F$ and its covariant derivatives,
> such as $\mathrm{Tr}\,F_{ij}F_{kl}(x)$. Correlation functions of
> the quantum field operators should agree at short distances with
> the predictions of asymptotic freedom and perturbative
> renormalization theory ... Those predictions include among other
> things the existence of a stress tensor and an operator product
> expansion, having prescribed local singularities predicted by
> asymptotic freedom."

**The smoking-gun footnote (§6.6, footnote 2, verbatim):**

> "We specifically exclude weak-existence (compactness) as the
> solution to the existence part of the Millennium problem, unless
> one also uses other techniques to establish properties of the limit
> (such as the existence of a mass gap and the axioms)."

This footnote is binding. A subsequential limit obtained by
Banach–Alaoglu / weak-* compactness alone does **not** satisfy the
Millennium problem. The proof must establish properties of *the*
limit — i.e., must propagate the mass gap and the axioms through
the limit, not merely assert that some weak limit exists.

**Reflection positivity guidance (§6.5, verbatim):**

> "Reflection positivity holds for the Wilson approximation, a major
> advantage; few methods exist to recover reflection positivity in
> case it is lost through regularization — such as with dimensional
> regularization, Pauli–Villars regularization, and many other
> methods. Establishing a quantum mechanical Hilbert space is part
> of the solution to this Millennium problem."

If the proof's regularization (e.g., the KK enhancement) breaks RP
at any stage, recovery must be explicit and rigorous.

**Infinite-volume limit (§6.6, verbatim):**

> "New ideas are needed to prove the existence of a mass gap that is
> uniform in the volume of space-time. Such a result presumably
> would enable the study of the limit as $\mathbb{T}^4 \to
> \mathbb{R}^4$."

Jaffe–Witten themselves flag $\mathbb{T}^4 \to \mathbb{R}^4$ as
*open*. Any claimed proof must address it head-on, with a
volume-uniform gap. This is not optional.

**Clustering as a consequence (§5):**

> "An important consequence of the existence of a mass gap is
> clustering: ... $|\langle\Omega, \mathcal{O}(\vec x)\mathcal{O}(\vec y)\Omega\rangle|
> \leq \exp(-C|\vec x - \vec y|)$"

This is a downstream consequence, not a substitute for the gap.

---

### Mandatory checks against the official statement

A review under this script MUST verify each of the following items
explicitly. If any item is not addressed in the preprint, that is a
**GENUINE GAP** with respect to Clay eligibility, regardless of any
mathematical merit elsewhere.

| # | Requirement | Source | Pass criterion |
|:--|:------------|:-------|:---------------|
| C1 | Compact simple gauge group $G$ — *all*, not just SU($N$) | §4 | Exceptional groups $G_2, F_4, E_6, E_7, E_8$ and $\mathrm{SO}(N), \mathrm{Sp}(N)$ either covered or limitation explicit |
| C2 | Non-trivial (not free/Gaussian) | §4 | Some connected $n$-point with $n \geq 4$ shown nonzero, or interacting S-matrix |
| C3 | Axioms at least as strong as Wightman OR OS | §4 | Each axiom checked; reconstruction theorem applied with the corrected (1975) version |
| C4 | $\mathrm{spec}(H) \subseteq \{0\} \cup [\Delta, \infty)$, $\Delta > 0$ AND $m < \infty$ | §4 | Both bounds proved; existence of finite-mass one-particle state |
| C5 | **No weak-existence-only solution** | §6.6 fn 2 | If subsequential limit is used, properties must be established for *the* limit (mass gap, axioms propagated through the limit, not asserted on a hypothetical limit) |
| C6 | Local gauge-invariant field operators in correspondence with $\mathrm{Tr}\,F_{ij}F_{kl}$ etc. | §4 | Field operators (not only Wilson loops) constructed; correspondence with curvature polynomials stated |
| C7 | Short-distance match to perturbative AF | §4 | Two-point function (or equivalent) reproduces the perturbative AF prediction at short distances |
| C8 | Stress tensor exists | §4 | Constructed or shown to exist |
| C9 | Operator product expansion with prescribed singularities | §4 | OPE established; local singularities match AF prediction |
| C10 | RP preserved or recovered through every regularization step | §6.5 | KK device, Balaban block-spin, and continuum limit each verified |
| C11 | $\mathbb{T}^4 \to \mathbb{R}^4$ with volume-uniform mass gap | §6.6 | Mass gap shown uniform in $L$; infinite-volume limit constructed |

For each item, the report must contain a one-paragraph status:
**PASS** (with location in the preprint), **FAIL** (with what is
missing), or **PARTIAL** (with what is covered and what is not).
This table is in addition to the per-Point analysis below.

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

### Recent Rigorous Results (2020--2026)

- Chatterjee (2021): strong mass gap implies confinement for groups
  with nontrivial center. **Finite gauge groups only.**
- Adhikari-Cao (2025): exponential decay at weak coupling for
  **finite gauge groups**.
- Cao-Chatterjee (2024): state space for 3D Yang-Mills.
- **No rigorous mass gap result exists for continuous SU(N) in 4D.**
- Douglas (Nature Reviews Physics, 2025): no breakthroughs on the
  4D problem.

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

**Previous referee findings (read to avoid re-litigating settled issues):**
12. `/Users/gsix/yang-mills/referee/r06/summary.md`
    (most recent hostile referee — found all 8 original points SOUND)
13. `/Users/gsix/yang-mills/referee/r05/report.md`
    (detailed point-by-point findings on the 8 original points)

**Technical supplements (required — these close gaps flagged in Parts C, D, G):**
14. `/Users/gsix/yang-mills/preprint/sections/I3-N-dependence-tracking.md`
    ($N$-dependence tracking through the proof chain — closes C1b, G3c)
15. `/Users/gsix/yang-mills/preprint/sections/I4-other-gauge-groups.md`
    (extension to all compact simple groups — closes G1b)
16. `/Users/gsix/yang-mills/preprint/sections/J-lattice-symanzik-basis.md`
    (lattice-specific dimension-6 operator classification — closes D1a)
17. `/Users/gsix/yang-mills/preprint/sections/I-gap-closures.md`
    (extraction lemma, SU($N$) extension of Balaban — closes C1b)

**Verification documents:**
18. `/Users/gsix/yang-mills/referee/r03/verify-balaban-items.md`
19. `/Users/gsix/yang-mills/referee/r06/bibliographic-verification.md`

---

## Your Task: Exhaustive Review

Scrutinize the entire proof chain from geometric foundations through
continuum QFT construction, with particular focus on Clay Millennium
Prize eligibility per the verbatim Jaffe–Witten text quoted above.
Prior review verdicts (if any survive in your context) are evidence,
not proof — your verdict is independent. If your analysis disagrees
with a prior verdict, override it and explain the disagreement.

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
Balaban's results extend to SU($N$)$, and which require additional
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

**Location:** Section 5.3.1, Section 5.6 Part III.3

**The claim:** Every $\mathcal{C}$-even, gauge-invariant, local operator
of engineering dimension 6 on the $d = 4$ hypercubic lattice falls into
one of four classes, all with $\mathrm{dev} \geq 2$.

**Interrogate:**

(a) **The Lüscher-Weisz basis.** The classification coincides with the
Lüscher-Weisz (1985) operator basis for dimension-6 operators. This
basis is established in the continuum Symanzik effective theory. On the
lattice, additional operators could arise that are absent in the
continuum. The standard argument (Symanzik 1983) is that such operators
are redundant by equations of motion. Is this argument stated and proved
for the specific lattice action used, or is it cited as standard?

(b) **The second two-derivative operator.** The operator
$\mathrm{Tr}(D_\mu F^{\mu\rho} D_\nu F^\nu{}_\rho)$ is related to
$\mathrm{Tr}(D_\rho F_{\mu\nu})^2$ by equations of motion. The r05
referee flagged that $\mathrm{dev} \geq 2$ is verified explicitly only
for $\mathrm{Tr}(D_0 F)^2$, not for the second operator. Does the
current preprint close this gap?

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

(b) **The linear combination lemma.** The lemma states that if each
$\mathcal{O}_i$ has $\mathrm{dev} \geq p$ and $\sum |c_i|
\|\mathcal{O}_i\| < \infty$, then $\sum c_i \mathcal{O}_i$ has
$\mathrm{dev} \geq p$. The proof uses the fact that deviation order
is defined at the level of individual spectral weights. But the
multi-time-slice representation of the sum may have a different temporal
extent $R$ than the individual operators. If the operators
$\mathcal{O}_i$ have different temporal supports, the sum must be
embedded in a common representation with the maximal $R$. Does
zero-padding shorter operators (inserting identity time slices) preserve
the deviation structure? State precisely where this is handled.

(c) **The role of (B1) analyticity.** The convergent Taylor expansion
(from analyticity) means $\delta E_k^{d=6}$ is a genuine linear
combination of monomials, not a formal series. But the analyticity
radius $\rho$ from (B1) determines the domain in which the expansion
converges. Outside this domain (near the boundary of $\Omega_s$), the
expansion may not converge. Does the spectral lemma require the
expansion to converge on all configurations contributing to the matrix
element $\langle 1|\delta E_k^{d=6}|1\rangle_c$? The one-particle
state $|1\rangle$ has support on typical configurations. Are typical
configurations in the gapped phase guaranteed to lie within the
analyticity domain?

(d) **The transition from perturbative to non-perturbative.** The
previous referee (r05, Point 1d) initially flagged this as a GENUINE
GAP, then revised to CLOSABLE after careful re-examination. The key
insight was that the classification is exhaustive: every dim-6
$\mathcal{C}$-even operator has $\mathrm{dev} \geq 2$ by structure,
not by perturbative identification. But there remains a subtlety: the
"dimension-6 part" of the effective action is defined by projecting out
the dimension-4 component ($S_{\mathrm{YM}}/g_k^2$). This projection
requires knowing that $S_{\mathrm{YM}}$ is the **unique** dimension-4
operator. The uniqueness argument is confirmed in PROOF-CHAIN.md IV.3.
But is the projection well-defined non-perturbatively? Can "dimension-6"
be unambiguously separated from "dimension-4 + dimension-8 + ..." at
the level of the full non-perturbative effective action?

(e) **Structural zero vs. kinematic zero.** The diagonal vanishing
$(e^{E_1 - E_1} - 1)^2 = 0$ is claimed to be structural (arising from
the squared-derivative structure of dim-6 operators) rather than
kinematic (a coincidence). The r05 referee concluded this is correct
because the deviation order is a property of the operator class, not
of a specific matrix element. But the deviation order involves the
spectral weight $W_\alpha^{(m)}(\mathbf{n})$, which depends on the
specific operator. For the non-perturbative $\delta E_k^{d=6}$, the
spectral weights are not computed explicitly — they are inferred from
the classification. Is this inference rigorous? Specifically: the
classification says the operator is a convergent sum of operators with
$\mathrm{dev} \geq 2$. But a convergent sum could have cancellations
that change the spectral weight structure. Can $\mathrm{dev} \geq 2$
for each term but $\mathrm{dev} < 2$ for the sum? (The linear
combination lemma says no — but verify the proof handles cancellations.)


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

(a) **Lattice reflection positivity.** The Osterwalder-Seiler theorem
gives RP for the Wilson plaquette action via the checkerboard
decomposition. **Crucially, Osterwalder-Seiler RP is specific to the
Wilson action** — improved lattice actions that add dimension-6
operators generically violate RP (the transfer matrix can acquire
complex eigenvalues producing damped oscillatory behavior). Does the
KK-enhanced theory (with internal $\mathbb{CP}^{N-1}$ connections at
each site) satisfy RP? The internal action is positive-definite
(Yang-Mills on $\mathbb{CP}^{N-1}$), but the coupling $V_\ell$ between
sites involves link variables and internal connections. Does the full
action $S_{4D} + S_{\mathrm{int}}$ have the checkerboard decomposition
structure required for Osterwalder-Seiler?

(b) **RP through the RG.** Balaban's block-spin transformation may not
preserve RP at intermediate steps. The effective action $S_k$ after $k$
RG steps is not necessarily the action of a reflection-positive measure.
Does the proof require RP at intermediate scales, or only at the final
scale? If only at the endpoints (lattice and continuum), the intermediate
violation is harmless.

(c) **RP in the continuum limit.** The lower semicontinuity argument
(Section 5.7(f), OS3 Step 2) uses: if $\mu_n \to \mu$ weakly and
$\langle \theta f, f \rangle_{\mu_n} \geq 0$ for all $n$, then
$\langle \theta f, f \rangle_\mu \geq 0$. This requires $\theta f
\cdot f$ to be a continuous bounded function of the field configuration.
For Schwartz-class $f$ and lattice gauge fields, is this true? The
lattice fields are compact (SU($N$)-valued), so boundedness holds.
But continuity of $\theta f \cdot f$ as a function on the space of
distributions (the continuum limit) requires careful analysis.


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

**Binding rule (Jaffe–Witten §6.6, footnote 2):** *"We specifically
exclude weak-existence (compactness) as the solution to the existence
part of the Millennium problem, unless one also uses other techniques
to establish properties of the limit (such as the existence of a
mass gap and the axioms)."*

This footnote is the central test for this Point. A Banach–Alaoglu
subsequential limit, by itself, does not satisfy Clay. The proof
must propagate the mass gap and the OS axioms *to the specific limit
constructed*, not merely assert their existence on a hypothetical
limit.

**The claim:** The preprint claims $\Delta_\infty > 0$ for the
continuum theory. But the continuum theory is obtained as a
subsequential limit (Banach-Alaoglu).

**Interrogate:**

(a) **Subsequence dependence.** Different subsequences $a_{j_1} \to 0$
and $a_{j_2} \to 0$ could give different limiting Schwinger functions
$\{S_n^{(1)}\}$ and $\{S_n^{(2)}\}$. Both would satisfy OS1--OS5.
Both would have $\Delta_\infty > 0$. But they could be **different
QFTs**. Does the preprint claim uniqueness of the continuum limit, or
only that every subsequential limit has a mass gap?

(b) **Universality.** In statistical mechanics, universality (uniqueness
of the continuum limit) is a non-trivial property that requires
additional arguments beyond the existence of subsequential limits.
For asymptotically free gauge theories, universality is expected
(and supported by perturbative arguments) but not rigorously proved.
Does the preprint address this? If not, does the Jaffe-Witten problem
require uniqueness, or is existence of one limit with mass gap
sufficient?

(c) **The mass gap value.** Even if the continuum limit is not unique,
the mass gap $\Delta_\infty$ could depend on the subsequence. The
preprint computes $\Delta_\infty = C_\infty \cdot \Lambda_\infty > 0$
with $C_\infty = C_0 - \sum \delta C_k$. Are $C_\infty$ and
$\Lambda_\infty$ subsequence-independent? If $\Lambda_\infty$ depends
on the subsequence (it is defined via the RG flow, which has a
fixed-point structure), is the positivity $\Delta_\infty > 0$ still
guaranteed for every subsequence?

(d) **Comparison with the Clay problem.** The Jaffe-Witten statement
asks to "prove that for any compact simple gauge group $G$, a quantum
Yang-Mills theory exists on $\mathbb{R}^4$ and has a mass gap
$\Delta > 0$." The word "a" (indefinite article) suggests that
existence of one such theory suffices. But if multiple continuum limits
exist, is it clear that they are all Yang-Mills theories (in the sense
of being derived from the Yang-Mills Lagrangian)?


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
explicitly verified? (See Point F1(a) — the bound
$|S_n(f)| \leq n! C_0^n \|f\|_{L^1}$ appears to satisfy OS0'.)

(b) **The Hilbert space.** The reconstructed Hilbert space $\mathcal{H}$
is obtained from the GNS construction using the Schwinger functions.
For gauge theories, there is a fundamental issue: the starting fields
are not physical observables (they are not gauge-invariant). The
physical Hilbert space is a subspace/quotient. The preprint constructs
Schwinger functions from gauge-invariant observables (Wilson loops,
plaquette traces). Does this bypass the gauge/Hilbert space issue? If
so, what are the "field operators" in the Wightman theory?

(c) **Non-triviality.** The Jaffe-Witten problem requires the theory
to be non-trivial. A free (Gaussian) theory has a mass gap but is not
Yang-Mills. The preprint must show that some connected $n$-point
function (with $n \geq 4$) is nonzero, or that the S-matrix is
non-trivial. Where is non-triviality established?

(d) **The Yang-Mills equations of motion.** Does the reconstructed
Wightman theory satisfy the Yang-Mills equations of motion in any
sense? The Schwinger functions are constructed from a lattice gauge
theory (Wilson action), which approximates the Yang-Mills action.
But the continuum limit could in principle converge to a different
theory. Where is it shown that the limiting theory is Yang-Mills
(i.e., that the Schwinger functions satisfy the Ward identities
associated with gauge invariance and the YM equations)?


---


## Part G: Clay Compliance and Cross-Cutting Issues

### Point G1: Jaffe-Witten Requirements [HEAVY]

**Location:** Abstract, Section 5.7, overall proof structure

**The claim:** The preprint proves the Yang-Mills mass gap for SU($N$)
in four dimensions, solving the Clay Millennium Problem.

**Interrogate:**

(a) **The KK device.** The proof uses the KK-enhanced theory
(with $\mathbb{CP}^{N-1}$ fibers) as a proof device, then transfers
the mass gap to the standard theory via Theorem 5. The Jaffe-Witten
problem asks for a theory "on $\mathbb{R}^4$." Is the KK enhancement
fully decoupled in the final theory? Specifically: the continuum limit
in Section 5 is taken for the **standard** SU($N$) theory (not the
KK-enhanced one), using Balaban's RG (which applies to standard
lattice gauge theory). But the starting point $\Delta_0 > 0$ comes
from the KK-enhanced theory via Theorem 5. Does the proof chain
$\Delta_0^{\mathrm{KK}} > 0 \to \Delta_0^{\mathrm{std}} > 0 \to
\Delta_\infty > 0$ constitute a proof for the **standard** Yang-Mills
theory? Or does some step implicitly require the KK enhancement to be
present?

(b) **The gauge group.** Jaffe-Witten requires the result for
"any compact simple gauge group $G$." The preprint works with SU($N$)
for $N \geq 2$. Does this cover all compact simple Lie groups?
(No — it misses the exceptional groups $G_2, F_4, E_6, E_7, E_8$
and SO($N$), Sp($N$).) If the preprint claims only SU($N$), is this
explicitly stated as a limitation? Does the Jaffe-Witten problem
accept a partial result for SU($N$) only?

(c) **The lattice regulator.** The proof starts from Wilson's lattice
gauge theory, which is a specific regularization. Jaffe-Witten does
not prescribe a regularization. Is the final continuum theory
independent of the lattice regularization? (This is the universality
question from Point F4.) If the continuum limit depends on the lattice
structure, it is a lattice artifact, not a continuum Yang-Mills theory.

(d) **The precise claim.** State exactly what is proved: "For SU($N$)
with $N \geq 2$, starting from Wilson's lattice gauge theory, there
exists a subsequential continuum limit satisfying OS1--OS5 with mass gap
$\Delta_\infty > 0$." Is this sufficient for the Clay prize? What
additional steps would be needed to fully satisfy the Jaffe-Witten
statement?

(e) **The quantitative predictions.** The preprint makes quantitative
predictions ($\sqrt{\sigma} = 437$ MeV, etc.). These are valuable for
physics but irrelevant for the mathematical proof. Ensure the proof
does not rely on numerical agreement with experiment as evidence for
correctness.


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


### Point G4: Local Field Operators, Stress Tensor, OPE, and AF Matching [HEAVY]

**Location:** Section 5.7 and beyond — likely *not addressed* in the
current preprint.

**Binding text (Jaffe–Witten §4, verbatim):** *"one should define a
quantum field theory ... with local quantum field operators in
correspondence with the gauge-invariant local polynomials in the
curvature $F$ and its covariant derivatives, such as
$\mathrm{Tr}\,F_{ij}F_{kl}(x)$. Correlation functions of the quantum
field operators should agree at short distances with the predictions
of asymptotic freedom and perturbative renormalization theory ...
including ... the existence of a stress tensor and an operator
product expansion, having prescribed local singularities predicted
by asymptotic freedom."*

This Point bundles four Clay-mandated requirements that are absent
from most "mass gap" claims and were absent from prior referee runs.

**Interrogate:**

(a) **Local field operators in correspondence with curvature
polynomials.** The preprint constructs Schwinger functions of
gauge-invariant observables — but are these *operators* in the sense
of Jaffe–Witten §4, i.e., operator-valued distributions
$\mathrm{Tr}\,F_{ij}F_{kl}(x)$ on the reconstructed Hilbert space,
in correspondence with the classical curvature polynomials? Wilson
loops alone are not enough; Clay asks for local *field* operators.
Where are these constructed? If only Wilson-loop expectation values
exist, this is a **GENUINE GAP** vs. Clay regardless of mass-gap
status.

(b) **Short-distance match to perturbative AF.** The two-point
function $\langle \mathrm{Tr}\,F_{\mu\nu}(x)\,\mathrm{Tr}\,F_{\rho\sigma}(y)\rangle$
should reproduce the perturbative AF prediction (with logarithmic
running) as $|x-y|\to 0$. Does the preprint check this against the
known one-loop result? An "existence + gap" proof that produces a
two-point function inconsistent with AF at short distances is
**not Yang–Mills** in the Clay sense.

(c) **Stress tensor.** Clay explicitly requires the existence of a
stress-energy tensor $T_{\mu\nu}(x)$ on the reconstructed Hilbert
space. Is this constructed, or shown to exist? Note: this is
non-trivial for gauge theories — the canonical stress tensor is
gauge-non-invariant; an improved (gauge-invariant) stress tensor
must be defined. Where in the preprint?

(d) **Operator product expansion.** Clay requires an OPE with
"prescribed local singularities predicted by asymptotic freedom."
For two curvature operators, the leading OPE singularity is
$|x-y|^{-2\Delta_F}$ with the AF-corrected dimension $\Delta_F$.
Does the preprint establish *any* OPE? An OPE is a strong structural
property; mere short-distance bounds on $S_n$ are not equivalent.

(e) **The "or this is a $K$-step beyond the proof" caveat.** If the
preprint does not address (a)–(d), is the gap closable as 1 paragraph
/ 1 page / 1 paper, or does it require a substantively new
construction (e.g. Wilson's OPE program, or a Borchers-class
analysis)? State precisely what would need to be added.

**Impact on Clay eligibility:** A failure on any of (a)–(d) is
**directly** a failure of the Clay statement, not a mathematical
nicety. The current proof chain may correctly establish a mass gap
for *something*, but if that something lacks local field operators,
a stress tensor, an OPE, or short-distance AF agreement, it is not
the object Jaffe–Witten asked for.


---


### Point G3: $N$-Dependence and Error Propagation [MEDIUM]

**Location:** Throughout

**The claim:** The proof works uniformly for all SU($N$), $N \geq 2$.

**Interrogate:**

(a) **$N$-dependent constants.** Many constants in the proof depend on
$N$: the spectral gap ($\mu_1$ on $\mathbb{CP}^{N-1}$), the
propagator constant $C_0$, the Kotecký-Preiss convergence threshold,
the analyticity radius $\rho$, the spectral lemma constant $C_p$,
the Gronwall exponent $\gamma$. Track the $N$-dependence through the
proof chain. Does any constant grow so fast with $N$ that the proof
fails for large $N$?

(b) **SU(2) special properties.** For $N = 2$: the cubic Casimir
$d^{abc} = 0$ (all dim-6 non-derivative operators vanish identically),
$\mathbb{CP}^1 = S^2$ (a round sphere, simpler geometry), and the
exact area law $\sigma = 3g^2/8$ provides an independent check. Does
the proof use any SU(2)-specific property that doesn't generalize to
$N \geq 3$?

(c) **Error compounding.** The proof chain has $\sim 14$ steps, each
with bounds of the form "≤ $C$" or "$= O(g_k^p)$." If each constant
$C$ has a factor of (say) $N^2$ from the Lie algebra, the accumulated
error could grow as $N^{28}$. Is there a systematic tracking of
$N$-dependence, or is it absorbed into uncontrolled constants? For
the Clay prize, the proof must work for each fixed $N$ — large-$N$
asymptotics are not required, but each constant must be finite for
each fixed $N$.


---


## Output Format

Write all your report files into:
`/Users/gsix/yang-mills/notation-math-referee/latest-run/`

This directory was created empty by `code/setup-venv.sh` at the start
of this session. Any prior run was automatically archived into
`/Users/gsix/yang-mills/notation-math-referee/runs/r{NN}/` before you
started.

**Do NOT read anything inside `notation-math-referee/runs/`.** Past
runs are out of scope by design — your verdict must be independent.
The archive exists for human inspection across cycles, not for you.

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
| `part-g-point-1.md` | Jaffe-Witten requirements |
| `part-g-point-2.md` | Gauge invariance through RG |
| `part-g-point-3.md` | $N$-dependence and error propagation |
| `part-g-point-4.md` | Local field operators, stress tensor, OPE, AF matching |
| `clay-checklist.md` | The C1–C11 mandatory-checks table from "Mandatory checks against the official statement", with PASS/FAIL/PARTIAL per row and one-paragraph justification |
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

# Your north star 
Find any issue that would cause the Clay Scientific Advisory Board to reject this proof. A credibility-destroying gap is worse than a fixable technical gap. Focus on:
